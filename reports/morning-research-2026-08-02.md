# Morning Investment Research — Sunday, August 2, 2026
*Window covered: 2026-08-01 00:00 – 2026-08-02 05:03 ET*

**Data-source notice:** every structured feed this skill normally relies on (SEC EDGAR, ClinicalTrials.gov, the FDA newsroom, arXiv/bioRxiv, NASA, the Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com exchange APIs) was unreachable this run. Direct `curl` requests and the repo's `fetch_quotes.py` both failed with a `403 Forbidden` on the CONNECT tunnel — a policy denial, not a site outage — and `WebFetch` returned `403` on every URL tried, including non-financial control pages (`example.com`, `en.wikipedia.org`, `github.com`, and even `anthropic.com` itself). Only `WebSearch` worked. **This is the thirteenth consecutive run with this exact failure pattern.** New this run: the proxy's own status endpoint confirms this is a narrow *allowlist*, not a blanket outage — plain `curl` succeeds only to `pypi.org`, `registry.npmjs.org`, `index.crates.io`, `proxy.golang.org`, and `*.anthropic.com` (all present in the proxy's configured `noProxy` bypass list), and fails identically (403 on CONNECT) to every other host tested, financial or not. This confirms the fix is a network-egress allowlist change at the environment/config level, not a transient issue — see Administrative notes below. Everything below comes from `WebSearch` summaries of secondary reporting, not fetched primary filings or exchange tickers, so the verification standard is weaker than usual and every rating is capped at Watch/Hold.

# 📈 Stocks

*No significant catalysts across the tracked themes (medical, technology/AI/quantum, space, emerging markets, deals, ETFs) cleared the bar in this window.* Targeted checks against SEC 8-K/6-K activity, FDA actions, quantum/space announcements, and EM/ETF flows (via `WebSearch`, since the structured feeds are down) turned up nothing both dated inside the Aug 1–2 window and not already logged in a prior day's briefing — see `seen_catalysts` in `portfolio.json`. Items surfaced but excluded as stale or already covered: the MarketAxess/ICE merger (dated July 29–30, already logged), Capricor's deramiocel CRL-lift/PDUFA reset (not a position or watchlist name, and the exact lift date could not be pinned inside this window from search snippets alone), and general EM/China-ETF flow commentary (context, not a dated overnight event). Both open positions (DYN, HUT) were checked directly for weekend news — see Portfolio below — and nothing new appeared beyond what July 31's briefing already covered.

# ₿ Cryptos
*Prices from WebSearch-aggregated secondary reporting only this run — direct Coinbase/Kraken/crypto.com/CoinGecko access was unreachable, so the usual cross-venue verification could not be performed. Treat these as approximate. As of ~05:00 ET August 2.*

## Market snapshot
| Asset | Price (USD) | 24h % | Sources agree? | Note |
|-------|-------------|-------|----------------|------|
| BTC   | ~$62,865 | roughly flat to slightly down, weakening momentum (RSI ~44) | Single-source only, not cross-venue verified | No dated catalyst found this window |
| ETH   | ~$1,867 | +0.25% | Single-source only, not cross-venue verified | No dated catalyst found this window |

**No crypto entry rated this run.** Ordinary price drift only — no regulatory action, protocol event, or exchange event confirmed as both real and dated inside this window from the sources available.

---
**Sources consulted:** WebSearch only, this run (SEC EDGAR, ClinicalTrials.gov, FDA newsroom, arXiv/bioRxiv, NASA news, Yahoo Finance chart API, Coinbase/Kraken/crypto.com/CoinGecko — all unreachable via curl and WebFetch, see data-source notice above). Named press/wire sources are linked inline above.
*Informational only; not investment advice. Crypto is volatile and speculative. Verify independently before trading. Generated 2026-08-02T05:03 ET.*

---

# Portfolio

## Snapshot
No live, cross-checked quote could be obtained for SPY, DYN, or HUT this run (`scripts/fetch_quotes.py` returned a `403 Forbidden` for every symbol). Secondary `WebSearch` results for both open positions were themselves internally inconsistent — DYN "current price" queries returned figures ranging from $17.92 to $25.10 depending on source (a >35% spread at the same nominal timestamp), and HUT's July 31 close could not be confirmed at all (one source describes a same-day intraday surge of up to 20% on the Nvidia-tenant news, a different dated article headlines a 12.8% decline the same day; the last figure both sources agree predates, $101.14, is the July 30 close). Per the "never price from memory or a headline" rule, **no total account value, unrealized P&L, or percent-invested figure is reported today** rather than picking one contradictory secondary number and presenting it as fact. Today is also a Sunday — markets are closed and no fills would have been placed regardless.

Last verified state (July 20 fills, unchanged since): cash $7,397.92; DYN 63 sh @ $23.75 cost; HUT 11 sh @ $100.53 cost; SPY benchmark 13.4281 sh @ $744.71 cost (2026-07-20).

## Open positions
| Ticker | Shares | Avg cost | Current price | Unrealized P&L | Status |
|--------|--------|----------|----------------|-----------------|--------|
| DYN | 63 | $23.75 | unavailable (conflicting secondary quotes, see above) | unavailable | watch |
| HUT | 11 | $100.53 | unavailable (last confirmed print $101.14, 7/30; 7/31 move unconfirmed) | unavailable | intact |

Thesis re-check: DYN's regulatory thesis (BLA accepted, Priority Review, PDUFA Jan 21 2027) is unchanged; status stays **watch** pending confirmation the July offering dilution hasn't otherwise impaired the setup. HUT's thesis strengthened on paper July 31 (Nvidia confirmed as Beacon Point anchor tenant, FT), but that news is now two days old and already reflected in the prior briefing; status stays **intact**. Hut 8's Q2 earnings (August 4) is the next hard confirmation point for the Nvidia relationship.

## Today's trades
**No trades today.** No reliable machine-readable quote existed for SPY, DYN, HUT, BTC, or ETH, which rules out pricing any fill from a real source regardless of conviction. Independent of the outage, today is a Sunday — no fills would be placed on a weekend under any circumstance. Nothing in today's (limited) research cleared the bar for new money: no new catalyst appeared on any tracked or candidate name this window.

## Realized P&L to date
$0.00 realized (no positions have been closed). Combined realized + unrealized total cannot be computed today without a live mark; it stands at $0.00 realized plus an unknown unrealized figure pending restored data access.

## Watchlist changes
No adds, no removes. All eighteen previously carried names (JSPR, TEM, PSNL, KLRS, ONCY, RGNX, BMNR, AMD, BLTE, GLSI, NBIS, RKLB, MU, MCHP, ACAD, ARWR, QBTS, IONQ) are unchanged. Six expire tomorrow (2026-08-03: JSPR, TEM, PSNL, KLRS, ONCY, RGNX) — no fresh weekend news surfaced on any of them to refresh the clock, so they will lapse on the next run unless that changes.

`seen_catalysts` was reviewed for pruning (entries older than 30 days); the oldest entries are dated July 20, thirteen days ago, so none qualify for pruning yet. No new entries were logged — nothing found this run was both new and dated inside the window.

## Administrative notes — please read
- `reports/unsent-2026-08-01.md` was found in the repo (yesterday's briefing was compiled but never delivered, for the same reasons below). It has been renamed to `reports/morning-research-2026-08-01.md` in today's commit per the standing procedure, flagged here exactly once.
- **This is the thirteenth consecutive run** in which (a) the session's network egress policy blocks every structured data source (SEC EDGAR, ClinicalTrials.gov, bioRxiv, FDA.gov, arXiv, NASA, Yahoo Finance, all three crypto exchange APIs) with a 403, confirmed independently via `curl`, the proxy status endpoint, `WebFetch` (403 on every domain tried, including non-financial ones), and the repo's own `fetch_quotes.py`; and (b) the Gmail connector available to this session exposes only draft creation (`create_draft`/`update_draft`/`list_drafts`) with no send tool of any kind, so every run's report ends up as an unsent draft rather than delivered mail. **29 "Morning Research"/"Daily Morning Investment Research" drafts are now sitting unsent in Gmail, with the oldest dated June 24, 2026 — over five weeks — meaning this routine has likely never actually delivered a single email to the inbox it targets.** Neither issue is a one-off; both are standing configuration gaps at the account/environment level that need a human fix: the network policy needs the relevant research and market-data hosts allow-listed (the proxy status endpoint shows the current allowlist covers only package registries and `anthropic.com`, nothing else), and the Gmail connector needs send scope granted. The paper-trading simulation has not executed a single fill since it opened on July 20 (thirteen days, thirteen runs) because no fill has ever had a verifiable quote to price from. This run's self-check (`scripts/selfcheck.py`) was run with `--quotes` against a quotes file that is all errors, so the "quote present for every open position" check is expected to fail; that failure is disclosed here, not patched around.

```
PORTFOLIO_STATE
{
  "version": 1,
  "initialized_at": "2026-07-20T10:50:30-04:00",
  "last_run": "2026-08-02",
  "cash": 7397.92,
  "positions": [
    {
      "ticker": "DYN",
      "shares": 63,
      "avg_cost": 23.75,
      "entry_date": "2026-07-20",
      "stop": 19.0,
      "target": 32.0,
      "thesis": "FDA accepted BLA for z-rostudirsen (DMD, exon 51) with Priority Review, PDUFA Jan 21 2027; the offering closed July 24 upsized further via full over-allotment exercise (21,045,000 sh at $20.50, ~$431.4M gross vs. the $375M headline) - more dilutive than initially priced but does not itself invalidate the regulatory thesis.",
      "status": "watch"
    },
    {
      "ticker": "HUT",
      "shares": 11,
      "avg_cost": 100.53,
      "entry_date": "2026-07-20",
      "stop": 82.0,
      "target": 125.0,
      "thesis": "Signed $9.8B, 15-year lease fully commercializes 1GW Beacon Point AI campus with an investment-grade tenant, accelerating the pivot from BTC mining to AI infra leasing. Nvidia confirmed as the anchor tenant July 31, 2026 (FT report); base-term contract value now put at $19.6B, up to $50.2B with renewals.",
      "status": "intact"
    }
  ],
  "realized_pnl": 0.0,
  "benchmark": {
    "spy_shares": 13.4281,
    "spy_cost": 744.71,
    "quote_ts": "2026-07-20T10:50:30-04:00"
  },
  "watchlist": [
    {"ticker": "JSPR", "reason": "Reverse merger with Kira Pharmaceuticals closed + $132M PIPE; stock fell 11% on close, stockholder vote on preferred conversion still pending", "added": "2026-07-20", "expires": "2026-08-03"},
    {"ticker": "TEM", "reason": "Definitive deal to acquire Personalis (~$1.5B, floating stock ratio); TEM fell 9% on announcement; routine shareholder-rights investigation opened July 21-22, not itself material", "added": "2026-07-20", "expires": "2026-08-03"},
    {"ticker": "PSNL", "reason": "Being acquired by Tempus at nominal $16.25/sh but trading well below that on deal-closing risk and floating ratio; routine shareholder-rights investigation opened July 21-22, not itself material", "added": "2026-07-20", "expires": "2026-08-03"},
    {"ticker": "KLRS", "reason": "Positive expanded Phase 1a nAMD durability data but stock fell 5%; watch for Phase 2 initiation", "added": "2026-07-20", "expires": "2026-08-03"},
    {"ticker": "ONCY", "reason": "FDA Fast Track for pelareorep combo in anal SCC; designation only, no efficacy data yet", "added": "2026-07-20", "expires": "2026-08-03"},
    {"ticker": "RGNX", "reason": "$100M ($107.8M) follow-on priced at $9.00/sh on July 17; shares fell ~17% on the pricing (resolves prior conflicting reports); separate shareholder-rights investigation into RGX-111 disclosures adds legal-headline risk", "added": "2026-07-20", "expires": "2026-08-03"},
    {"ticker": "BMNR", "reason": "Q3 FY26 results: revenue beat ($46.5M, 98% ETH staking) but a $92.1M loss on ETH-linked derivatives drove an $83.6M net loss; stock fell ~7.7% July 23. Derivatives exposure is now a structural swing factor distinct from the underlying ETH-treasury thesis", "added": "2026-07-24", "expires": "2026-08-07"},
    {"ticker": "AMD", "reason": "Helios rackscale platform reached production at the July 22-23 Advancing AI 2026 event, plus new EPYC 9006 server CPUs and a Ryzen AI Halo/Cisco collaboration; stock still fell 4% same-day, but that tracks a broad Nasdaq selloff (Alphabet -7%, Tesla -14% on earnings) rather than a reaction to AMD's news", "added": "2026-07-24", "expires": "2026-08-07"},
    {"ticker": "BLTE", "reason": "New Phase 3 DRAGON secondary-endpoint data for tinlarebant in Stargardt disease at ASRS; NDA already submitted to FDA", "added": "2026-07-21", "expires": "2026-08-04"},
    {"ticker": "GLSI", "reason": "Preliminary FLAMINGO-01 open-label arm data (~70-80% recurrence reduction, company-flagged as immature); DSMB recommended trial continue unmodified", "added": "2026-07-21", "expires": "2026-08-04"},
    {"ticker": "NBIS", "reason": "A July 23 SEC filing confirmed the hard number behind the Nvidia stake reported July 21: 22,256,412 shares/warrants, a 9.3% holding; shares jumped as much as +18.8% intraday on the filed confirmation", "added": "2026-07-24", "expires": "2026-08-07"},
    {"ticker": "RKLB", "reason": "$266M U.S. Space Force firm-fixed-price contract for 12+6 suborbital launches through 2028; stock +6-9% after hours July 21", "added": "2026-07-22", "expires": "2026-08-05"},
    {"ticker": "MU", "reason": "Reversal: fell ~8.2% July 24 ($990.21 to $909.35) a day after hitting $1,000 on the capex/NAND-shortage thesis, triggered by SanDisk's own guidance flagging NAND price contraction (Korea chip selloff spillover, SK Hynix also down); bull and bear cases on the memory cycle are now both live within 24 hours", "added": "2026-07-25", "expires": "2026-08-07"},
    {"ticker": "MCHP", "reason": "Definitive agreement to acquire edge-AI chipmaker Hailo (100+ customers, 10,000+ developers); terms undisclosed and company states no material impact to financials, so tracked rather than sized", "added": "2026-07-25", "expires": "2026-08-07"},
    {"ticker": "ACAD", "reason": "FDA Fast Track for remlifanserin in Alzheimer's-disease psychosis; Phase 2 RADIANT enrollment complete, topline expected Sept-Oct 2026", "added": "2026-07-22", "expires": "2026-08-05"},
    {"ticker": "ARWR", "reason": "Phase 3 SHASTA-3 and SHASTA-4 both met primary endpoint (79-81% triglyceride reduction) and all secondary endpoints incl. pancreatitis reduction; shares reportedly +18% pre-market; sNDA planned by year-end", "added": "2026-07-23", "expires": "2026-08-06"},
    {"ticker": "QBTS", "reason": "AT&T expanded its D-Wave quantum-computing partnership to network optimization (a prior workload cut from ~1hr to <15sec); shares +19-20% same-day and D-Wave moved its listing from NYSE to Nasdaq the same day; no primary filing verified given the ongoing data-source outage, corroborated only via press (BusinessWire release plus multiple independent outlets)", "added": "2026-07-28", "expires": "2026-08-11"},
    {"ticker": "IONQ", "reason": "Received final regulatory approval to close its acquisition of SkyWater Technology (semiconductor foundry), securing a domestic scalable supply chain; deal first announced January 2026 so this is a completion event, limited fresh alpha", "added": "2026-07-29", "expires": "2026-08-12"}
  ],
  "seen_catalysts": [
    {"key": "HUT:2026-07-20:beacon-point-phase2-lease", "noted": "2026-07-20"},
    {"key": "DYN:2026-07-20:bla-priority-review", "noted": "2026-07-20"},
    {"key": "JSPR:2026-07-20:kira-merger-close", "noted": "2026-07-20"},
    {"key": "TEM:2026-07-20:personalis-acquisition", "noted": "2026-07-20"},
    {"key": "PSNL:2026-07-20:tempus-acquisition", "noted": "2026-07-20"},
    {"key": "KLRS:2026-07-20:phase1a-namd-expanded-data", "noted": "2026-07-20"},
    {"key": "ONCY:2026-07-20:fasttrack-anal-scc", "noted": "2026-07-20"},
    {"key": "RGNX:2026-07-20:follow-on-offering", "noted": "2026-07-20"},
    {"key": "BMNR:2026-07-20:eth-treasury-update", "noted": "2026-07-20"},
    {"key": "EYPT:2026-07-20:doj-dexycu-settlement", "noted": "2026-07-20"},
    {"key": "ETHE:2026-07-20:staking-cash-distribution-amendment", "noted": "2026-07-20"},
    {"key": "LXP:2026-07-20:brookfield-cppib-acquisition", "noted": "2026-07-21"},
    {"key": "MGY:2026-07-20:wildfire-energy-acquisition", "noted": "2026-07-21"},
    {"key": "ZWS:2026-07-20:intellihot-acquisition", "noted": "2026-07-21"},
    {"key": "SNBR:2026-07-20:bankruptcy-sale-sleep-country", "noted": "2026-07-21"},
    {"key": "AMD:2026-07-20:microsoft-helios-partnership", "noted": "2026-07-21"},
    {"key": "ASTS:2026-07-20:convertible-notes-launch-delay", "noted": "2026-07-21"},
    {"key": "BLTE:2026-07-20:asrs-secondary-endpoint-data", "noted": "2026-07-21"},
    {"key": "GLSI:2026-07-20:flamingo01-openlabel-data", "noted": "2026-07-21"},
    {"key": "CHINA-EM:2026-07-20:national-team-intervention", "noted": "2026-07-21"},
    {"key": "BTC:2026-07-21:etf-outflow-streak-easing", "noted": "2026-07-21"},
    {"key": "ETH:2026-07-21:etf-inflow-rotation", "noted": "2026-07-21"},
    {"key": "DYN:2026-07-21:dilutive-375m-offering", "noted": "2026-07-22"},
    {"key": "RGNX:2026-07-21:offering-reaction-conflict", "noted": "2026-07-22"},
    {"key": "ACAD:2026-07-20:fasttrack-alzheimers-psychosis", "noted": "2026-07-22"},
    {"key": "MU:2026-07-21:bofa-note-memory-rally", "noted": "2026-07-22"},
    {"key": "NBIS:2026-07-21:nvidia-stake-reflection-ai-deal", "noted": "2026-07-22"},
    {"key": "AMD:2026-07-21:analyst-upgrades-continued-rally", "noted": "2026-07-22"},
    {"key": "RKLB:2026-07-21:space-force-266m-contract", "noted": "2026-07-22"},
    {"key": "GM:2026-07-21:q2-beat-raised-guidance", "noted": "2026-07-22"},
    {"key": "CHINA-EM:2026-07-21:record-state-intervention-inflows", "noted": "2026-07-22"},
    {"key": "EWY:2026-07-20:record-korea-etf-inflows", "noted": "2026-07-22"},
    {"key": "COIN-HOOD-BLSH:2026-07-21:clarity-act-rally", "noted": "2026-07-22"},
    {"key": "BTC:2026-07-21:etf-inflow-streak-5day", "noted": "2026-07-22"},
    {"key": "ETH:2026-07-21:etf-inflow-breaks-8wk-outflow", "noted": "2026-07-22"},
    {"key": "LDO:2026-07-21:nansen-vault-lido-v3-launch", "noted": "2026-07-22"},
    {"key": "ARWR:2026-07-22:shasta3-4-phase3-topline", "noted": "2026-07-23"},
    {"key": "RGNX:2026-07-22:reaction-resolved-fell-17pct", "noted": "2026-07-23"},
    {"key": "CLARITY-ACT:2026-07-22:ethics-deal-reached", "noted": "2026-07-23"},
    {"key": "BTC:2026-07-22:etf-inflow-streak-6day", "noted": "2026-07-23"},
    {"key": "ETH:2026-07-22:etf-inflow-streak-4day", "noted": "2026-07-23"},
    {"key": "RUSSIA-CRYPTO:2026-07-21:state-duma-property-law", "noted": "2026-07-23"},
    {"key": "NBIS:2026-07-23:nvidia-93pct-stake-filed", "noted": "2026-07-24"},
    {"key": "AMD:2026-07-23:helios-production-advancing-ai", "noted": "2026-07-24"},
    {"key": "BMNR:2026-07-23:q3-earnings-revenue-beat-net-loss", "noted": "2026-07-24"},
    {"key": "MU:2026-07-23:hits-1000-capex-nand-shortage", "noted": "2026-07-24"},
    {"key": "DYN:2026-07-24:offering-closed-upsized-431m", "noted": "2026-07-24"},
    {"key": "BTC:2026-07-23:etf-inflow-streak-7day", "noted": "2026-07-24"},
    {"key": "ETH:2026-07-23:etf-inflow-streak-5day", "noted": "2026-07-24"},
    {"key": "CLARITY-ACT:2026-07-23:timeline-slips-thune", "noted": "2026-07-24"},
    {"key": "MU:2026-07-24:sandisk-guidance-reversal", "noted": "2026-07-25"},
    {"key": "SNDK:2026-07-24:nand-price-contraction-guidance", "noted": "2026-07-25"},
    {"key": "INTC:2026-07-23:q2-beat-chips-act-gaap-loss", "noted": "2026-07-25"},
    {"key": "MCHP:2026-07-24:hailo-acquisition-definitive-agreement", "noted": "2026-07-25"},
    {"key": "CHINA-EM:2026-07-24:tariff-125pct-effective", "noted": "2026-07-25"},
    {"key": "BTC:2026-07-23:etf-outflow-streak-snapped", "noted": "2026-07-25"},
    {"key": "ETH:2026-07-24:etf-inflow-despite-price-drop", "noted": "2026-07-25"},
    {"key": "QBTS:2026-07-27:att-expanded-quantum-partnership", "noted": "2026-07-28"},
    {"key": "SEMIS:2026-07-27:ai-financing-china-competition-selloff", "noted": "2026-07-28"},
    {"key": "BTC:2026-07-27:etf-outflow-fri-sat-despite-weekly-inflow", "noted": "2026-07-28"},
    {"key": "DYN:2026-07-28:dyne302-ind-clearance-fshd", "noted": "2026-07-29"},
    {"key": "IONQ:2026-07-28:skywater-acquisition-closed", "noted": "2026-07-29"},
    {"key": "DYN:2026-07-29:q2-2026-earnings-results", "noted": "2026-07-30"},
    {"key": "REPL:2026-07-29:fda-not-interpretable-melanoma-data", "noted": "2026-07-30"},
    {"key": "IBM:2026-07-29:hrl-nature-18qubit-spin-qpu", "noted": "2026-07-30"},
    {"key": "PCSA:2026-07-29:vidya-acquisition-200m-pipe", "noted": "2026-07-30"},
    {"key": "FED:2026-07-29:fomc-holds-rates-steady-3-dissents", "noted": "2026-07-30"},
    {"key": "MS-ETP:2026-07-29:eth-sol-etp-launch", "noted": "2026-07-30"},
    {"key": "MKTX:2026-07-30:ice-acquisition-167-cash", "noted": "2026-07-31"},
    {"key": "KPTI:2026-07-30:phase3-xport-ec042-missed-pfs", "noted": "2026-07-31"},
    {"key": "INTC:2026-07-30:tsmc-packaging-report-rally", "noted": "2026-07-31"},
    {"key": "BTC:2026-07-29:etf-inflow-resumes-after-4day-outflow", "noted": "2026-07-31"},
    {"key": "ETH:2026-07-29:etf-flow-conflicting-reports", "noted": "2026-07-31"},
    {"key": "HUT:2026-07-31:nvidia-anchor-tenant-revealed", "noted": "2026-08-01"}
  ]
}
```
