# RUNBOOK — morning research + paper-trading run

This file is the authoritative procedure for the daily scheduled run. The scheduled prompt is deliberately thin: it clones this repo and follows this runbook. Edit the procedure here (versioned, reviewable), not in the prompt.

Every run does two jobs, then emails one combined report to **joshuakessell@icloud.com**:

1. **Research:** compile the morning briefing using the `morning-investment-research` skill that ships in this repo at `.claude/skills/morning-investment-research/` (its endpoint reference is `references/sources.md` alongside it). All of its sourcing, verification, formatting, and preflight rules apply.
2. **Portfolio:** manage the simulated account described below.

This is a paper-trading simulation to measure how AI-driven catalyst research would perform in the real market. No real money is involved, no real orders are placed, and nothing in it is financial advice or will be executed in real life.

## 0. Inputs and invariants

- **Auth:** the fine-grained GitHub PAT lives in the environment variable `INVESTSIM_GITHUB_PAT` (scoped to this single repository, Contents read/write). It is injected by the environment configuration — it never appears in the scheduled prompt, this file, commits, emails, or command output. Never print, log, email, or commit the token, and never show a token-bearing remote URL in any output.
- **Source of truth:** this repository, branch `main`. The local filesystem is per-run scratch; nothing on disk counts as saved state until committed and pushed. Never reconstruct the account from memory, chat history, or old emails, and never treat a failure to reach the repo as evidence that no account exists.
- **WORKDIR:** `~/investment-sim`, the run's fresh clone. Do all state work inside it.

The repo contains:

- `portfolio.json` — current account state (schema in §3)
- `transactions.jsonl` — append-only ledger, one JSON object per line, beginning with an init record
- `reports/` — dated copy of each sent briefing (`morning-research-YYYY-MM-DD.md`); the audit trail the skill's cross-day dedup reads
- `BOOTSTRAP` — empty latch file that exists only before the account has been opened, never again after
- `.claude/skills/` — the research skill (auto-loaded by the session)
- `scripts/fetch_quotes.py`, `scripts/selfcheck.py` — deterministic tooling (§8, §9)

## 1. Startup procedure, in order

1. Clone: `git clone https://x-access-token:${INVESTSIM_GITHUB_PAT}@github.com/joshuakessell/stock-market-sim.git ~/investment-sim`. Set identity: `git -C ~/investment-sim config user.name "investment-sim-bot"` and `git -C ~/investment-sim config user.email "investment-sim-bot@users.noreply.github.com"`.
2. If `INVESTSIM_GITHUB_PAT` is unset, or the clone fails for any reason (network, auth, missing repo): email "state unreachable, run aborted" with the underlying error and stop. No initialization, no trades, no writes. A failed read is never a first-run signal.
3. Read `portfolio.json` from the clone. If it parses, this is a normal daily run. If `BOOTSTRAP` is somehow still present alongside valid state, delete it in today's commit and note that in the email.
4. If `portfolio.json` is missing or corrupt but `transactions.jsonl` exists: do not initialize a new account. Rebuild state by replaying the ledger from its init record, note the recovery in the email, and continue as a normal run.
5. If neither state file exists, this is a first run only if `BOOTSTRAP` exists at the repo root. Do the first-run setup (§5) and delete `BOOTSTRAP` as part of the same end-of-run commit. If `BOOTSTRAP` is absent: email "state files missing and bootstrap latch not set, run aborted" and stop. The absence of state files is never, by itself, permission to initialize.
6. If `last_run` in the loaded state equals today's date, the schedule fired twice. Email a one-line "already ran today" note and stop: no trades, no state writes. A deliberate manual re-run that says "rerun" may refresh prices and marks, but still places no trades.
7. If `reports/` contains any `unsent-*.md` files, mention them in today's email, then rename them to their normal dated names in today's commit so each one is flagged exactly once.

## 2. Research half

Invoke the `morning-investment-research` skill (repo copy). Fetch structured sources with `curl` per the skill's operating principles and `references/sources.md`; reserve WebFetch/WebSearch for open-ended corroboration. The briefing's dated copy is saved in `reports/` at end of run (§10).

## 3. portfolio.json schema

```json
{
  "version": 1,
  "initialized_at": "2026-07-17T08:30:00-05:00",
  "last_run": "2026-07-17",
  "cash": 4321.55,
  "positions": [
    {
      "ticker": "XYZ",
      "shares": 12,
      "avg_cost": 41.20,
      "entry_date": "2026-07-17",
      "stop": 34.00,
      "target": 55.00,
      "thesis": "one line: the catalyst and why it is not fully priced in",
      "status": "intact"
    }
  ],
  "realized_pnl": 0.00,
  "benchmark": {
    "spy_shares": 17.8412,
    "spy_cost": 560.50,
    "quote_ts": "2026-07-17T08:30:00-05:00"
  },
  "watchlist": [
    { "ticker": "ABC", "reason": "one line", "added": "2026-07-15", "expires": "2026-07-29" }
  ],
  "seen_catalysts": [
    { "key": "XYZ:2026-07-16:phase3-topline", "noted": "2026-07-16" }
  ]
}
```

Field notes:

- `benchmark` is written once at first run and never modified afterward.
- `seen_catalysts` prevents re-reporting or re-trading the same news on later runs. Add a key for every catalyst that appears in the briefing. Prune entries older than 30 days.
- `watchlist` entries expire 10 trading days after `added` unless refreshed by new information.
- `status` per position is one of `intact`, `watch`, `invalidated`, re-evaluated every run against the stop, the target, and the thesis.

## 4. transactions.jsonl records

First line, written once during first-run setup:

```json
{"type":"init","date":"2026-07-17","cash":10000.00,"benchmark":{"spy_shares":17.8412,"spy_cost":560.50,"quote_ts":"2026-07-17T08:30:00-05:00"}}
```

Trades:

```json
{"type":"trade","date":"2026-07-17","ticker":"XYZ","side":"buy","shares":12,"price":41.20,"cash_impact":-494.40,"quote_source":"nasdaq.com pre-market","quote_ts":"2026-07-17T08:28:00-05:00","rationale":"one line"}
```

Corporate actions:

```json
{"type":"corp_action","date":"2026-07-17","ticker":"XYZ","action":"split|dividend|acquisition|delisting","detail":"2-for-1 split","cash_impact":0.00}
```

The account must be fully reconstructable from this file alone.

## 5. First run only

Runs only when the startup procedure says so: both state files absent and `BOOTSTRAP` present.

1. Write the init record to `transactions.jsonl`: $10,000.00 in cash.
2. Record the benchmark: a hypothetical $10,000 of SPY at the same quote timestamp used to open the account (prior close if the market is closed). Fractional shares are allowed for the benchmark only.
3. Write the initial `portfolio.json`.
4. Delete `BOOTSTRAP`. All of this lands in the single end-of-run commit.

(The account first opened 2026-07-20; this section exists for disaster recovery. The legacy 5-shares-per-Buy tracker predating this system is retired and unrecoverable — never search for it or mention it in reports.)

## 6. Mandate

Actively manage the account using each day's research findings plus the state of existing positions. Buying, adding, trimming, selling, and doing nothing are all valid moves. There is no requirement to deploy the full $10,000 at any point. Cash is a position, and sitting at 100% cash is acceptable whenever nothing clears the bar. On quiet research days, still run the full portfolio review: existing positions need managing even when there is no new research.

## 7. Strategy (aggressive, not reckless)

- Universe: long-only common stocks and ETFs listed on major US exchanges (NYSE family, Nasdaq). No options, margin, leverage, shorting, or OTC/penny names. Skip anything under roughly $2 per share or too thinly traded to absorb a few thousand dollars.
- Sizing is conviction-weighted. A new position costs at most 15% of total account value; trim any position that grows beyond 25% of the account.
- Target roughly 4 to 10 positions when opportunities justify it. Concentrated conviction is the point of an aggressive book, but never a single bet.
- Every buy requires a written thesis: the catalyst, why it may not be fully priced in yet, the expected holding period, a stop (the thesis-invalidation level, typically 15 to 20% below cost), and a profit-taking or reassessment trigger. These map directly onto the position fields in `portfolio.json`.
- Sell or trim when the thesis breaks, the stop is hit, the catalyst looks fully priced in, or the cash has a clearly better use in a new idea. Winners may run past their target as long as the thesis is restated and still holds.
- Only Buy-grade findings from today's research are eligible for new money on the day they appear. Watch names go on the persistent watchlist with a reason and date, and may graduate to a position on a later run once follow-up confirms the signal.

## 8. Execution rules

- Whole shares only. Zero commissions; slippage is not modeled.
- Fetch quotes once per run in a single pass with the repo script:
  `python3 ~/investment-sim/scripts/fetch_quotes.py --equities SPY {open positions} {candidates} --crypto BTC ETH {notable movers} > {scratch}/quotes.json`
  Use this file for fills, marks, and the crypto snapshot cross-check.
- Fill at the most recent real quote available at run time (pre-market quote, or prior close when the market is closed). Log the exact price, source, and timestamp on every fill. If no reliable machine-readable quote exists for a ticker, do not fill it; put it on the watchlist and move on. Never price a fill from memory or a headline.
- No fills on weekends or market holidays. Mark positions at the last close and say so.
- Never backdate a trade or revise a recorded fill.
- Corporate actions: splits adjust share count and cost basis, dividends credit cash, acquisitions close at the deal price, delistings close at the final print. Each one gets a ledger entry.

## 9. Self-check before sending

After writing today's state files, run:

```
python3 ~/investment-sim/scripts/selfcheck.py --dir ~/investment-sim --quotes {scratch}/quotes.json
```

It mechanically verifies: cash is not negative; every share count is a positive whole number; replaying `transactions.jsonl` reproduces both the portfolio cash and the per-ticker share counts; a quote exists for every open position; and no position exceeds 25% of account value. A non-zero exit is a failed check: state the discrepancy and the correction in the email. Never silently patch numbers.

Two checks the script cannot see, verify manually: no fill today exceeded 15% of account value at the time of the fill, and total account value equals cash plus the sum of shares times current price (the script prints this total as INFO — sanity-check it against the report).

## 10. End of run, in this order

1. Inside the clone: append today's ledger entries to `transactions.jsonl`, write the updated `portfolio.json` atomically (write `portfolio.json.tmp`, then rename it over `portfolio.json`), and save today's report to `reports/morning-research-YYYY-MM-DD.md`.
2. Run the self-check (§9). Fix or disclose failures before proceeding.
3. Commit everything as a single commit: `git add -A && git commit -m "run YYYY-MM-DD"`.
4. Push: `git push origin main`. Verify it landed: `git rev-parse HEAD` must equal the hash from `git ls-remote origin refs/heads/main`. If the push is rejected as non-fast-forward, run `git pull --rebase` once and push again.
5. If the push still fails after that one retry, the run has FAILED. Send the email anyway with the PORTFOLIO_STATE block prominently flagged UNPUSHED, state plainly that today's state was not saved and the next run will load yesterday's state, and stop. State does not exist until the push lands.
6. Only after a verified push, send the email (subject per the skill: `Morning Research — {Mon D}: {N} item(s)`). If the send fails after one retry — including when the Gmail connector only has draft scope — leave the report as a Gmail draft, rename the repo copy to `reports/unsent-YYYY-MM-DD.md`, commit and push that rename, and flag the send failure (and the missing send permission, if that's the cause) in the run summary. Startup step 7 will surface it on the next run.

## 11. Portfolio section of the report

The research half follows the skill's template. Append this after it:

1. Snapshot: total account value, cash, percent invested, total return versus the $10,000 start, and return versus the SPY benchmark (benchmark value = stored `spy_shares` times current SPY price).
2. Open positions ranked from most profitable to least: ticker, shares, average cost, current price, unrealized profit and loss in dollars and percent, and thesis status.
3. Today's trades with rationale, or "No trades today" plus one line on why.
4. Realized profit and loss to date from closed positions, and the combined realized plus unrealized total for the account.
5. End the email with a fenced PORTFOLIO_STATE block containing the exact contents of `portfolio.json`. It is a human-readable mirror and a disaster backup, not the source of truth. If the repository is ever lost, recovery is copying this block into a fresh repo along with the ledger reconstructed from prior emails.
