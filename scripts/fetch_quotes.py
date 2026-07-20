#!/usr/bin/env python3
"""Single-pass quote fetch for a run: every open position, SPY, candidates, and crypto majors.

Usage:
    python3 scripts/fetch_quotes.py --equities SPY DYN HUT --crypto BTC ETH SOL > quotes.json

Equities via Yahoo Finance chart API; crypto cross-checked across Coinbase, Kraken,
and crypto.com. Emits one JSON object to stdout; per-symbol errors are recorded
inline rather than aborting the whole pass.
"""
import argparse
import datetime
import json
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (investment-sim quote fetch)"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def equity(ticker):
    d = get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1m&range=1d")
    m = d["chart"]["result"][0]["meta"]
    ts = m.get("regularMarketTime")
    return {
        "price": m.get("regularMarketPrice"),
        "prev_close": m.get("previousClose") or m.get("chartPreviousClose"),
        "quote_ts_utc": datetime.datetime.utcfromtimestamp(ts).isoformat() + "Z" if ts else None,
        "source": "query1.finance.yahoo.com chart API (regularMarketPrice)",
    }


def crypto(sym):
    out = {}
    try:
        c = get(f"https://api.exchange.coinbase.com/products/{sym}-USD/ticker")
        out["coinbase"] = {"price": float(c["price"]), "time": c.get("time")}
    except Exception as e:
        out["coinbase"] = {"error": str(e)}
    try:
        k = get(f"https://api.kraken.com/0/public/Ticker?pair={sym}USD")
        # Kraken keys the result by its own asset code (XXBTZUSD, XETHZUSD, ...).
        res = next(iter(k["result"].values()))
        last, open_24h = float(res["c"][0]), float(res["o"])
        out["kraken"] = {"price": last, "open_24h": open_24h,
                         "change_24h_pct": round((last / open_24h - 1) * 100, 2)}
    except Exception as e:
        out["kraken"] = {"error": str(e)}
    try:
        cc = get(f"https://api.crypto.com/v2/public/get-ticker?instrument_name={sym}_USDT")
        data = cc["result"]["data"]
        if isinstance(data, list):
            data = data[0]
        # 'a' = last trade price; 'c' = 24h change as a FRACTION (0.021 == +2.1%).
        entry = {"raw": data}
        if "a" in data:
            entry["price_usdt"] = float(data["a"])
        if "c" in data:
            entry["change_24h_pct"] = round(float(data["c"]) * 100, 2)
        out["crypto_com"] = entry
    except Exception as e:
        out["crypto_com"] = {"error": str(e)}

    prices = [v["price"] for v in (out.get("coinbase"), out.get("kraken")) if v and "price" in v]
    if len(prices) >= 2:
        spread_pct = abs(prices[0] - prices[1]) / prices[0] * 100
        out["venues_agree_within_pct"] = round(spread_pct, 3)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--equities", nargs="*", default=[])
    ap.add_argument("--crypto", nargs="*", default=[])
    a = ap.parse_args()

    result = {"fetched_at_utc": datetime.datetime.utcnow().isoformat() + "Z",
              "equities": {}, "crypto": {}}
    for t in a.equities:
        try:
            result["equities"][t] = equity(t)
        except Exception as e:
            result["equities"][t] = {"error": str(e)}
    for s in a.crypto:
        result["crypto"][s] = crypto(s)

    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
