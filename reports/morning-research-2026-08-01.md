# Morning Investment Research — Saturday, August 1, 2026
*Window covered: 2026-07-31 00:00 – 2026-08-01 05:09 ET*

**Data-source notice:** every structured feed this skill normally relies on (SEC EDGAR, ClinicalTrials.gov, the FDA newsroom, arXiv/bioRxiv, NASA, the Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com exchange APIs) was unreachable this run. Direct `curl` requests and the repo's `fetch_quotes.py` both failed with a 403 from the session's own network egress proxy — a policy denial, not a site outage — and WebFetch returned 403 on every URL tried, including non-financial control pages. Only WebSearch worked. Everything below comes from search-engine summaries of secondary reporting (wire copy, press aggregators), not fetched primary filings or exchange tickers, so the verification standard is weaker than usual and every rating is capped at Watch/Hold. **This is the twelfth consecutive run with this exact failure pattern** (see Administrative notes in the Portfolio section) — it is a standing environment/config issue, not a quiet market.

# 📈 Stocks

## Summary
| Ticker | Name | Theme | Headline | Impact | Rec |
|--------|------|-------|----------|--------|-----|
| HUT | Hut 8 Corp | Technology, AI & Quantum | Nvidia named as Beacon Point anchor tenant, deal value to $19.6B | High | Hold (existing position) |

### Technology, AI & Quantum
#### Hut 8 Corp (HUT, Nasdaq) — Impact: High
**What happened:** Hut 8 shares jumped as much as 20% on July 31 after the Financial Times reported that Nvidia is the previously undisclosed anchor tenant behind Hut 8's 1GW Beacon Point AI data-center campus. Hut 8 had disclosed the lease itself the prior week without naming the counterparty; the base-term contract value across the campus is now put at $19.6B over 15 years, with potential to reach $50.2B if renewal options are exercised. (Investing.com/FT coverage: https://m.au.investing.com/news/stock-market-news/why-is-hut-8-stock-surging-today-93CH-4564912; original lease disclosure: https://www.prnewswire.com/news-releases/hut-8-fully-commercializes-1-gw-beacon-point-ai-data-center-campus-with-second-352-mw-it-lease-bringing-campus-level-base-term-contract-value-to-19-6-billion-302829514.html)
**Market impact:** naming Nvidia as the tenant materially derisks counterparty quality versus the "existing investment-grade customer" language used at initial disclosure, and the scale of the headline figure (up to $50.2B) reframes Hut 8 as an AI-infrastructure landlord backed by the sector's most important buyer, not just a bitcoin miner diversifying.
**Recommendation: Hold** — this is a held position (11 sh @ $100.53 cost, entry 2026-07-20); the news strengthens rather than changes the existing thesis, so no action is warranted on the reveal alone. Risk: no live quote could be confirmed this run, so today's reaction size and current price are unverified against a primary source; secondary reporting puts the stock in the $92–$112 range intraday July 31, which is internally inconsistent enough that it should not be treated as precise. Monitoring trigger: Hut 8's Q2 earnings, due August 4, which should confirm or detail the Nvidia relationship on the record.

*No other theme cleared the significance bar this window under the available (degraded) sourcing.* Medical, Space, Emerging Markets, ETFs & Fund Flows, and Deals turned up nothing both (a) dated inside the July 31–August 1 window and (b) not already logged in a prior day's briefing — see `seen_catalysts` in `portfolio.json` for what was previously covered (MarketAxess/ICE, Karyopharm's Phase 3 miss, and the Intel/TSMC packaging rally were all dated July 30 and already reported in yesterday's briefing).

# ₿ Cryptos
*Prices from WebSearch-aggregated secondary reporting only this run — direct Coinbase/Kraken/crypto.com/CoinGecko access was unreachable, so the usual cross-venue verification could not be performed. Treat these as approximate. As of ~05:00 ET August 1.*

## Market snapshot
| Asset | Price (USD) | 24h % | Sources agree? | Note |
|-------|-------------|-------|----------------|------|
| BTC   | ~$62,900–$64,400 | roughly flat, possibly slightly up | No (not cross-venue verified, proxy/API outage; secondary sources disagreed by over $1,500 within a single query) | No specific dated catalyst confirmed for this window |
| ETH   | ~$1,860–$1,930 | roughly flat, possibly slightly down | No (same outage; secondary sources disagreed on direction) | No specific dated catalyst confirmed for this window |

**No crypto entry rated this run.** Ordinary price drift only — no regulatory action, protocol event, or exchange event could be confirmed as both real and dated inside this window from the sources available. A candidate SEC "15% NAV buffer" rule for yield-bearing Bitcoin ETFs surfaced in search results but its approval date could not be pinned down with confidence (other results describe the underlying comment period as still running into Q3 2026), so it is omitted rather than reported as a dated event.

---
**Sources consulted:** WebSearch only, this run (SEC EDGAR, ClinicalTrials.gov, FDA newsroom, arXiv/bioRxiv, NASA news, Yahoo Finance chart API, Coinbase/Kraken/crypto.com/CoinGecko — all unreachable via curl and WebFetch, see data-source notice above). Named press/wire sources are linked inline above.
*Informational only; not investment advice. Crypto is volatile and speculative. Verify independently before trading. Generated 2026-08-01T05:09 ET.*

---

# Portfolio

## Snapshot
No live quotes were obtainable this run (`scripts/fetch_quotes.py` returned a `403 Forbidden` from the network proxy for every symbol: SPY, DYN, HUT, BTC, ETH). This is the **twelfth consecutive run** with this exact failure. Today is also a Saturday — markets are closed and no fills would have been placed regardless. As of the last confirmed state (July 20 fills; unchanged since):
- Cash: $7,397.92
- Open positions at cost: DYN 63 sh @ $23.75 ($1,496.25) + HUT 11 sh @ $100.53 ($1,105.83) = $2,602.08 at cost
- Total account value at cost basis: $10,000.00 (unchanged from the $10,000 starting value; no realized gains/losses booked and no mark-to-market available)
- Benchmark: 13.4281 SPY shares at $744.71 cost ($10,000 equivalent at inception); no current SPY price available to compare.
- Return vs. $10,000 start and vs. SPY benchmark: cannot be computed today without a live quote.

Unverified, search-sourced context only (not a fill basis, and not cross-checked, which is exactly why it isn't used as a mark): Hut 8 was reported trading intraday between roughly $92 and $112 on July 31 following the Nvidia-tenant reveal above (see Stocks section); no comparable recent price mention turned up for Dyne in this run's searches.

## Open positions (ranked by cost basis; no live P&L available)
| Ticker | Shares | Avg cost | Current price | Unrealized P&L | Thesis status |
|--------|--------|----------|----------------|-----------------|---------------|
| DYN | 63 | $23.75 | Unavailable (quote feed blocked) | N/A | Watch (unchanged). Regulatory thesis (Priority Review BLA, PDUFA Jan 21 2027) intact. No new DYN-specific news found this window. |
| HUT | 11 | $100.53 | Unavailable (quote feed blocked) | N/A | Intact, strengthened. Nvidia named as Beacon Point anchor tenant (see Stocks section); base-term contract value raised to $19.6B. Q2 earnings due August 4 should confirm details on the record. |

## Today's trades
**No trades today.** No reliable machine-readable quote existed for SPY, DYN, HUT, BTC, or ETH, so no fill could be priced from a real source, which rules out any buy or sell regardless of conviction. Independent of the outage, today is a Saturday — no fills would be placed on a weekend under any circumstance. Nothing in today's (limited) research cleared the bar for new money in any case: the sole confirmed catalyst (HUT/Nvidia) is on an existing holding, not a new-money candidate.

## Realized P&L to date
$0.00 realized (no positions have been closed). Combined realized + unrealized total cannot be computed today without a live mark; it stands at $0.00 realized plus an unknown unrealized figure pending restored data access.

## Watchlist changes
No adds, no removes. All eighteen previously carried names (JSPR, TEM, PSNL, KLRS, ONCY, RGNX, BMNR, AMD, BLTE, GLSI, NBIS, RKLB, MU, MCHP, ACAD, ARWR, QBTS, IONQ) are unchanged; none have expired (earliest expiry is 2026-08-03).

`seen_catalysts` was reviewed for pruning (entries older than 30 days); the oldest entries are dated July 20, twelve days ago, so none qualify for pruning yet. One new entry was logged for today's finding (HUT/Nvidia-tenant reveal).

## Administrative notes — please read
- `reports/unsent-2026-07-31.md` was found in the repo (yesterday's briefing was compiled but never delivered, for the same reasons below). It has been renamed to `reports/morning-research-2026-07-31.md` in today's commit per the standing procedure, flagged here exactly once.
- This is the **twelfth consecutive run** in which (a) the session's network egress policy blocks every structured data source (SEC EDGAR, ClinicalTrials.gov, bioRxiv, FDA.gov, arXiv, NASA, Yahoo Finance, all three crypto exchange APIs) with a 403, confirmed independently via `curl`, the proxy status endpoint, WebFetch, and the repo's own `fetch_quotes.py`; and (b) the Gmail connector available to this session exposes only draft creation with no send capability, so every run's report ends up as an unsent draft rather than delivered mail (including this one; 28 "Morning Research"/"Daily Morning Investment Research" drafts are now sitting unsent in Gmail, with the oldest dated **June 24, 2026** — over five weeks — meaning this routine has likely never actually delivered a single email to the inbox it targets). Neither issue is a one-off. Both are standing configuration gaps at the account/environment level: the network policy needs the relevant research and market-data hosts allow-listed, and the Gmail connector needs send scope granted. The paper-trading simulation has not executed a single fill since it opened on July 20 (twelve days, twelve runs) because no fill has ever had a verifiable quote to price from. This run's self-check (`scripts/selfcheck.py`) was run with `--quotes` against a quotes file that is all errors, so the "quote present for every open position" check is expected to fail; that failure is disclosed here, not patched around.

```
PORTFOLIO_STATE
{
  "version": 1,
  "initialized_at": "2026-07-20T10:50:30-04:00",
  "last_run": "2026-08-01",
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
