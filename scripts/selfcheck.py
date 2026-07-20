#!/usr/bin/env python3
"""Deterministic end-of-run checks for the paper-trading state. Run before committing.

Usage:
    python3 scripts/selfcheck.py [--dir ~/investment-sim] [--quotes quotes.json]

Checks (FAIL = fix before commit; never silently patch numbers):
  - portfolio.json parses and cash is non-negative
  - every position's share count is a positive whole number
  - ledger replay: init cash + sum(cash_impact) across transactions.jsonl == portfolio cash
  - ledger replay: per-ticker share counts match portfolio positions
    (skipped with a warning if corp_action records exist, since splits aren't modeled here)
  - with --quotes (output of fetch_quotes.py): a quote exists for every open position,
    and no position exceeds 25% of total account value

Exit code 0 = all checks pass, 1 = at least one FAIL.
"""
import argparse
import json
import os
import sys

fails = []


def check(name, ok, detail=""):
    line = f"{'PASS' if ok else 'FAIL'}: {name}"
    if detail:
        line += f" ({detail})"
    print(line)
    if not ok:
        fails.append(name)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=".")
    ap.add_argument("--quotes", help="JSON file produced by scripts/fetch_quotes.py")
    a = ap.parse_args()
    d = os.path.expanduser(a.dir)

    p = json.load(open(os.path.join(d, "portfolio.json")))
    check("cash non-negative", p["cash"] >= 0, f"cash={p['cash']}")

    for pos in p.get("positions", []):
        check(f"{pos['ticker']} shares positive whole number",
              isinstance(pos["shares"], int) and pos["shares"] > 0, f"shares={pos['shares']}")

    cash = None
    shares = {}
    has_corp_actions = False
    with open(os.path.join(d, "transactions.jsonl")) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if rec["type"] == "init":
                cash = rec["cash"]
            elif rec["type"] == "trade":
                cash += rec.get("cash_impact", 0)
                delta = rec["shares"] if rec["side"] == "buy" else -rec["shares"]
                shares[rec["ticker"]] = shares.get(rec["ticker"], 0) + delta
            elif rec["type"] == "corp_action":
                cash += rec.get("cash_impact", 0)
                has_corp_actions = True

    check("ledger has init record", cash is not None)
    if cash is not None:
        check("ledger replay matches portfolio cash", abs(cash - p["cash"]) < 0.01,
              f"replayed={round(cash, 2)} portfolio={p['cash']}")

    if has_corp_actions:
        print("WARN: corp_action records present; share-count replay skipped "
              "(splits/adjustments not modeled by this script)")
    else:
        held = {pos["ticker"]: pos["shares"] for pos in p.get("positions", [])}
        ledger_open = {t: n for t, n in shares.items() if n != 0}
        check("ledger replay matches position share counts", held == ledger_open,
              f"portfolio={held} ledger={ledger_open}")

    if a.quotes:
        q = json.load(open(a.quotes))["equities"]
        missing = [pos["ticker"] for pos in p.get("positions", [])
                   if pos["ticker"] not in q or "price" not in q.get(pos["ticker"], {})]
        check("quote present for every open position", not missing, ",".join(missing))
        if not missing:
            total = p["cash"] + sum(pos["shares"] * q[pos["ticker"]]["price"]
                                    for pos in p["positions"])
            print(f"INFO: total account value at supplied quotes = {round(total, 2)}")
            for pos in p["positions"]:
                w = pos["shares"] * q[pos["ticker"]]["price"] / total
                check(f"{pos['ticker']} within 25% concentration cap", w <= 0.25, f"{w:.1%}")

    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
