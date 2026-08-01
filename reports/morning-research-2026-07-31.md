# Morning Investment Research — Friday, July 31, 2026
*Window covered: 2026-07-30 00:00 – 2026-07-31 05:08 ET*

**Data-source notice:** every structured feed this skill normally relies on (SEC EDGAR, ClinicalTrials.gov, the FDA newsroom, arXiv/bioRxiv, NASA, the Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com exchange APIs) was unreachable this run. Direct `curl` requests and the repo's `fetch_quotes.py` all failed with a `403` from the session's own network egress proxy, a policy denial rather than a site outage, and `WebFetch` returned `403` or "unable to fetch" on every domain tried. Only `WebSearch` worked. Everything below comes from search-engine summaries of secondary reporting (wire copy, press aggregators), not fetched primary filings or exchange tickers, so the verification standard is weaker than usual. Tickers were cross-checked against the secondary sources' own reporting, not against `data.sec.gov`. Convictions are held a notch lower across the board, and no crypto price below is cross-venue-verified. This is a repo or environment issue to fix, not a quiet market.

# 📈 Stocks

## Summary
| Ticker | Name | Theme | Headline | Impact | Rec |
|--------|------|-------|----------|--------|-----|
| MKTX | MarketAxess | Deals | ICE to buy MarketAxess for $167/sh cash, ~$6.0B | High | Hold |
| KPTI | Karyopharm Therapeutics | Medical | Phase 3 endometrial-cancer trial missed PFS | High | Avoid |
| INTC | Intel | Technology, AI & Quantum | TSMC packaging-tech report sends INTC +12% | Medium | Watch |

### Deals
#### Intercontinental Exchange / MarketAxess (ICE, NYSE / MKTX, Nasdaq) — Impact: High
**What happened:** ICE agreed to acquire MarketAxess in an all-cash deal at $167.00/share, a 33% premium to MarketAxess's July 29 close, worth about $6.0B in equity value and $5.7B enterprise value. Both boards approved unanimously. The deal is cash-financed via new debt and is expected to close in H1 2027, subject to shareholder and regulatory approval. ([CNBC](https://www.cnbc.com/2026/07/30/intercontinental-exchange-to-buy-marketaxess.html), [ICE investor release](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-to-Acquire-MarketAxess-Creating-a-Premier-Fixed-Income-Marketplace/default.aspx))
**Market impact:** MKTX should now trade close to the $167 cash price minus a small merger-arb spread reflecting close timing and regulatory risk. ICE adds MarketAxess's fixed-income data and analytics franchise to its own pricing and index business, funded with incremental leverage.
**Recommendation: Hold** — this is a signed, all-cash deal with roughly ten months to close. There is no thesis left to build on MKTX beyond a standard arb spread, and no position is held today. Risk: regulatory review could slip the timeline or, less likely for this pairing, draw antitrust scrutiny. Monitoring trigger: shareholder vote date and any regulatory-clearance filings.

### Medical
#### Karyopharm Therapeutics (KPTI, Nasdaq) — Impact: High
**What happened:** Karyopharm announced topline Phase 3 XPORT-EC-042 results (selinexor maintenance vs. placebo, TP53-wild-type advanced/recurrent endometrial cancer, n=257). The trial missed its primary endpoint of progression-free survival: 12.75 vs. 7.43 months median PFS, HR 0.76, one-sided p=0.0791, short of the significance bar, with a clean safety profile and no new signals. ([Karyopharm investor release](https://investors.karyopharm.com/2026-07-30-Karyopharm-Announces-Topline-Results-from-Phase-3-XPORT-EC-042-Trial-in-Endometrial-Cancer))
**Market impact:** shares fell sharply on the announcement per secondary reporting. A missed pivotal primary endpoint on a near-term registrational study removes the near-term regulatory path for this indication even though the numerical trend favored the drug.
**Recommendation: Avoid** — a directionally favorable but statistically unmet primary endpoint is not a filing basis on its own, and the safety-clean readout doesn't change that. Risk: a subgroup or biomarker-defined re-cut could still resurrect part of the program. Monitoring trigger: any FDA feedback on a path forward, or full data at a medical congress.

### Technology, AI & Quantum
#### Intel (INTC, Nasdaq) — Impact: Medium
**What happened:** Intel shares jumped roughly 12% and Taiwan Semiconductor rose nearly 7% after a report that TSMC is developing an advanced chip-packaging technology resembling Intel's own EMIB approach, reportedly with Taiwan's Kinsus Interconnect Technology. The move capped a broad chip-sector rebound (the semiconductor ETF SOXX +8% on the day) following the prior week's sharp AI-capex-fear selloff. ([24/7 Wall St.](https://247wallst.com/investing/2026/07/30/intel-and-amd-soar-13-taiwan-semiconductor-rallies-7-as-ai-chip-stocks-bounce-hard/), [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/tsmcs-next-ai-chip-move-195343067.html))
**Market impact:** reads as validation of Intel's packaging IP and positioning relative to TSMC rather than an Intel-specific operational catalyst. The size of the one-day move, and the prior week's opposite-direction rout, suggests a sector whipsawing on sentiment more than a settled repricing.
**Recommendation: Watch** — the rally already happened same-day on a single report, not a confirmed disclosure from either company. A name that moves 12% on a press report deserves confirmation, not a chase. Risk: the report could be walked back or narrower in scope than headlined. Monitoring trigger: an actual 8-K, licensing agreement, or earnings-call confirmation from either company.

*ETF / pure-macro read:* **Positioning: Neutral** on broad semiconductor exposure (SOXX). The sector round-tripped from a steep AI-spend/China-competition selloff the prior week to an 8% single-day rebound, which reads as unresolved sentiment whipsaw rather than a clear trend confirmation either way.

# ₿ Cryptos
*Prices from secondary press aggregation only this run. Direct exchange APIs (Coinbase, Kraken, crypto.com) were unreachable, so the usual cross-venue verification could not be performed. Treat these figures as approximate. As of ~05:00 ET July 31.*

## Market snapshot
| Asset | Price (USD) | 24h % | Sources agree? | Note |
|-------|-------------|-------|----------------|------|
| BTC   | ~$63,300–$64,300 | roughly flat to slightly down | ✗ (not cross-venue verified — proxy/API outage) | Briefly dipped to ~$63,300 intraday July 30 before ETF inflows resumed |
| ETH   | ~$1,900–$1,930    | roughly flat | ✗ (not cross-venue verified — proxy/API outage) | — |

### Bitcoin (BTC) — spot ETF inflows resume after a four-session outflow streak
**What happened:** US spot Bitcoin ETFs took in $32.1M net on July 29, ending four straight sessions of outflows that totaled roughly $526M; July's total spot-BTC ETF inflow is still just ~$205M, reportedly the smallest monthly total on record for the product category. ([The Coin Republic](https://www.thecoinrepublic.com/2026/07/30/crypto-etfs-lose-526m-as-bitcoin-demand-weakens/), [CoinDesk](https://www.coindesk.com/daybook-us/2026/07/30/bitcoin-etfs-on-track-for-the-smallest-monthly-inflows-ever))
**Price action:** BTC briefly touched roughly $63,300 during the outflow stretch before the inflow report; no cross-venue confirmation available this run.
**Read: Watch** — a single day of modest inflows breaking a longer outflow streak is a data point, not a trend reversal, especially against a record-weak monthly total. Risk: one day's flow can reverse again immediately. Monitoring trigger: whether inflows hold for a second consecutive session.

### Ethereum (ETH) — conflicting same-day ETF flow reports
**What happened:** Secondary sources disagree on July 29/30 spot-ETH-ETF flow direction: one report puts Ether ETFs at **$18.65M in net outflows** for the session, another describes a **~$36.7M net inflow** the same day led by BlackRock's iShares Ethereum Trust (~$31.7M). Both agree ETH ETFs have taken in more money month-to-date (~$343M) than BTC ETFs (~$205M). ([Cointribune](https://www.cointribune.com/en/etf-capital-returns-to-bitcoin-as-ethereum-slips/), [GNCrypto](https://www.gncrypto.news/news/bitcoin-etfs-return-to-inflows-ether-etfs-slip/))
**Price action:** ETH roughly $1,900–$1,930 over the window per secondary reporting; not cross-venue verified this run.
**Read: Watch** — the flow direction itself is unresolved between sources for the same session, so no single-day conclusion is safe to draw. Risk: acting on either unverified number could be acting on a reporting error. Monitoring trigger: a consistent, cross-source-confirmed flow reading over 2+ sessions.

---
**Sources consulted:** WebSearch only (SEC EDGAR, ClinicalTrials.gov, FDA newsroom, arXiv/bioRxiv, NASA news, Yahoo Finance chart API, Coinbase/Kraken/crypto.com/CoinGecko — all unreachable via curl/WebFetch this run, see data-source notice above). Named press/wire sources are linked inline above.
*Informational only; not investment advice. Crypto is volatile and speculative. Verify independently before trading. Generated 2026-07-31T05:08 ET.*

---

# Portfolio

## Snapshot
No live quotes were obtainable this run (`scripts/fetch_quotes.py` returned a `403 Forbidden` from the network proxy for every symbol: SPY, DYN, HUT, BTC, ETH). This is the eleventh consecutive run with this exact failure. As of the last confirmed state (July 20 fills; unchanged since):
- Cash: $7,397.92
- Open positions at cost: DYN 63 sh @ $23.75 ($1,496.25) + HUT 11 sh @ $100.53 ($1,105.83) = $2,602.08 at cost
- Total account value at cost basis: $10,000.00 (unchanged from the $10,000 starting value; no realized gains/losses booked and no mark-to-market available)
- Benchmark: 13.4281 SPY shares at $744.71 cost ($10,000 equivalent at inception); no current SPY price available to compare.
- Return vs. $10,000 start and vs. SPY benchmark: cannot be computed today without a live quote.

Unverified, search-sourced context only (not a fill basis, and not cross-checked, which is exactly why it isn't used as a mark): Hut 8 was reported "near $108" and up roughly 202% year-to-date in one recent article, with Benchmark's price target raised to $165 (from $85, Buy) and Rosenblatt at $124 (Buy). Hut 8 reports Q2 earnings August 4. No comparable recent price mention turned up for Dyne in this run's searches.

## Open positions (ranked by cost basis; no live P&L available)
| Ticker | Shares | Avg cost | Current price | Unrealized P&L | Thesis status |
|--------|--------|----------|----------------|-----------------|---------------|
| DYN | 63 | $23.75 | Unavailable (quote feed blocked) | N/A | Watch (unchanged). Regulatory thesis (Priority Review BLA, PDUFA Jan 21 2027) intact. Q2 2026 results (already covered in the July 30 briefing) showed net loss widened to $178.6M but cash plus the July offering proceeds fund operations into Q2 2028, which eases the dilution concern without eliminating it. |
| HUT | 11 | $100.53 | Unavailable (quote feed blocked) | N/A | Intact (unchanged). No news this window contradicts the Beacon Point AI-leasing thesis; reported analyst price-target raises (Benchmark to $165, Rosenblatt $124) stand, with Q2 earnings due August 4. |

## Today's trades
**No trades today.** No reliable machine-readable quote existed for SPY, DYN, HUT, BTC, or ETH, so no fill could be priced from a real source, which rules out any buy or sell regardless of conviction. Independent of the outage, nothing in today's research cleared the bar for new money: the MarketAxess/ICE item is a signed deal with no further thesis to build (Hold, not a buy), Karyopharm is a Phase 3 miss (Avoid), and the Intel/semiconductor move already happened same-day on an unconfirmed report (Watch, not a chase).

## Realized P&L to date
$0.00 realized (no positions have been closed). Combined realized + unrealized total cannot be computed today without a live mark; it stands at $0.00 realized plus an unknown unrealized figure pending restored data access.

## Watchlist changes
No adds, no removes. All eighteen previously carried names (JSPR, TEM, PSNL, KLRS, ONCY, RGNX, BMNR, AMD, BLTE, GLSI, NBIS, RKLB, MU, MCHP, ACAD, ARWR, QBTS, IONQ) are unchanged; none have expired (earliest expiry is 2026-08-03).

`seen_catalysts` was reviewed for pruning (entries older than 30 days); the oldest entries are dated July 20, eleven days ago, so none qualify for pruning yet. Five new entries were logged for today's findings (MKTX/ICE, KPTI, INTC/semiconductor rally, and the two crypto ETF-flow items).

## Administrative notes
- `reports/unsent-2026-07-30.md` was found in the repo (yesterday's briefing was compiled but never delivered, for the same reasons below). It has been renamed to `reports/morning-research-2026-07-30.md` in today's commit per the standing procedure, flagged here exactly once.
- **This is the eleventh consecutive run** in which (a) the session's network egress policy blocks every structured data source (SEC EDGAR, ClinicalTrials.gov, bioRxiv, FDA.gov, arXiv, NASA, Yahoo Finance, all three crypto exchange APIs) with a 403, confirmed independently via curl, the proxy status endpoint, WebFetch, and the repo's own `fetch_quotes.py`; and (b) the Gmail connector available to this session exposes only draft creation with no send capability, so every run's report ends up as an unsent draft rather than delivered mail. Neither issue is a one-off. Both are standing configuration gaps at the account/environment level: the network policy needs the relevant research and market-data hosts allow-listed, and the Gmail connector needs send scope granted. The paper-trading simulation has not executed a single fill or delivered a single email since it opened on July 20, eleven days and eleven runs ago. This run's self-check (`scripts/selfcheck.py`) was run with `--quotes` against a quotes file that is all errors, so the "quote present for every open position" check is expected to fail; that failure is disclosed here, not patched around.

```
PORTFOLIO_STATE
{
  "version": 1,
  "initialized_at": "2026-07-20T10:50:30-04:00",
  "last_run": "2026-07-31",
  "cash": 7397.92,
  "positions": [
    {
      "ticker": "DYN",
      "shares": 63,
      "avg_cost": 23.75,
      "entry_date": "2026-07-20",
      "stop": 19.0,
      "target": 32.0,
      "thesis": "FDA accepted BLA for z-rostudirsen (DMD, exon 51) with Priority Review, PDUFA Jan 21 2027; the offering closed July 24 upsized further via full over-allotment exercise (21,045,000 sh at $20.50, ~$431.4M gross vs. the $375M headline) \u2014 more dilutive than initially priced but does not itself invalidate the regulatory thesis.",
      "status": "watch"
    },
    {
      "ticker": "HUT",
      "shares": 11,
      "avg_cost": 100.53,
      "entry_date": "2026-07-20",
      "stop": 82.0,
      "target": 125.0,
      "thesis": "Signed $9.8B, 15-year lease fully commercializes 1GW Beacon Point AI campus with an investment-grade tenant, accelerating the pivot from BTC mining to AI infra leasing.",
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
    {
      "ticker": "JSPR",
      "reason": "Reverse merger with Kira Pharmaceuticals closed + $132M PIPE; stock fell 11% on close, stockholder vote on preferred conversion still pending",
      "added": "2026-07-20",
      "expires": "2026-08-03"
    },
    {
      "ticker": "TEM",
      "reason": "Definitive deal to acquire Personalis (~$1.5B, floating stock ratio); TEM fell 9% on announcement; routine shareholder-rights investigation opened July 21-22, not itself material",
      "added": "2026-07-20",
      "expires": "2026-08-03"
    },
    {
      "ticker": "PSNL",
      "reason": "Being acquired by Tempus at nominal $16.25/sh but trading well below that on deal-closing risk and floating ratio; routine shareholder-rights investigation opened July 21-22, not itself material",
      "added": "2026-07-20",
      "expires": "2026-08-03"
    },
    {
      "ticker": "KLRS",
      "reason": "Positive expanded Phase 1a nAMD durability data but stock fell 5%; watch for Phase 2 initiation",
      "added": "2026-07-20",
      "expires": "2026-08-03"
    },
    {
      "ticker": "ONCY",
      "reason": "FDA Fast Track for pelareorep combo in anal SCC; designation only, no efficacy data yet",
      "added": "2026-07-20",
      "expires": "2026-08-03"
    },
    {
      "ticker": "RGNX",
      "reason": "$100M ($107.8M) follow-on priced at $9.00/sh on July 17; shares fell ~17% on the pricing (resolves prior conflicting reports); separate shareholder-rights investigation into RGX-111 disclosures adds legal-headline risk",
      "added": "2026-07-20",
      "expires": "2026-08-03"
    },
    {
      "ticker": "BMNR",
      "reason": "Q3 FY26 results: revenue beat ($46.5M, 98% ETH staking) but a $92.1M loss on ETH-linked derivatives drove an $83.6M net loss; stock fell ~7.7% July 23. Derivatives exposure is now a structural swing factor distinct from the underlying ETH-treasury thesis",
      "added": "2026-07-24",
      "expires": "2026-08-07"
    },
    {
      "ticker": "AMD",
      "reason": "Helios rackscale platform reached production at the July 22-23 Advancing AI 2026 event, plus new EPYC 9006 server CPUs and a Ryzen AI Halo/Cisco collaboration; stock still fell 4% same-day, but that tracks a broad Nasdaq selloff (Alphabet -7%, Tesla -14% on earnings) rather than a reaction to AMD's news",
      "added": "2026-07-24",
      "expires": "2026-08-07"
    },
    {
      "ticker": "BLTE",
      "reason": "New Phase 3 DRAGON secondary-endpoint data for tinlarebant in Stargardt disease at ASRS; NDA already submitted to FDA",
      "added": "2026-07-21",
      "expires": "2026-08-04"
    },
    {
      "ticker": "GLSI",
      "reason": "Preliminary FLAMINGO-01 open-label arm data (~70-80% recurrence reduction, company-flagged as immature); DSMB recommended trial continue unmodified",
      "added": "2026-07-21",
      "expires": "2026-08-04"
    },
    {
      "ticker": "NBIS",
      "reason": "A July 23 SEC filing confirmed the hard number behind the Nvidia stake reported July 21: 22,256,412 shares/warrants, a 9.3% holding; shares jumped as much as +18.8% intraday on the filed confirmation",
      "added": "2026-07-24",
      "expires": "2026-08-07"
    },
    {
      "ticker": "RKLB",
      "reason": "$266M U.S. Space Force firm-fixed-price contract for 12+6 suborbital launches through 2028; stock +6-9% after hours July 21",
      "added": "2026-07-22",
      "expires": "2026-08-05"
    },
    {
      "ticker": "MU",
      "reason": "Reversal: fell ~8.2% July 24 ($990.21 to $909.35) a day after hitting $1,000 on the capex/NAND-shortage thesis, triggered by SanDisk's own guidance flagging NAND price contraction (Korea chip selloff spillover, SK Hynix also down); bull and bear cases on the memory cycle are now both live within 24 hours",
      "added": "2026-07-25",
      "expires": "2026-08-07"
    },
    {
      "ticker": "MCHP",
      "reason": "Definitive agreement to acquire edge-AI chipmaker Hailo (100+ customers, 10,000+ developers); terms undisclosed and company states no material impact to financials, so tracked rather than sized",
      "added": "2026-07-25",
      "expires": "2026-08-07"
    },
    {
      "ticker": "ACAD",
      "reason": "FDA Fast Track for remlifanserin in Alzheimer's-disease psychosis; Phase 2 RADIANT enrollment complete, topline expected Sept-Oct 2026",
      "added": "2026-07-22",
      "expires": "2026-08-05"
    },
    {
      "ticker": "ARWR",
      "reason": "Phase 3 SHASTA-3 and SHASTA-4 both met primary endpoint (79-81% triglyceride reduction) and all secondary endpoints incl. pancreatitis reduction; shares reportedly +18% pre-market; sNDA planned by year-end",
      "added": "2026-07-23",
      "expires": "2026-08-06"
    },
    {
      "ticker": "QBTS",
      "reason": "AT&T expanded its D-Wave quantum-computing partnership to network optimization (a prior workload cut from ~1hr to <15sec); shares +19-20% same-day and D-Wave moved its listing from NYSE to Nasdaq the same day; no primary filing verified given the ongoing data-source outage, corroborated only via press (BusinessWire release plus multiple independent outlets)",
      "added": "2026-07-28",
      "expires": "2026-08-11"
    },
    {
      "ticker": "IONQ",
      "reason": "Received final regulatory approval to close its acquisition of SkyWater Technology (semiconductor foundry), securing a domestic scalable supply chain; deal first announced January 2026 so this is a completion event, limited fresh alpha",
      "added": "2026-07-29",
      "expires": "2026-08-12"
    }
  ],
  "seen_catalysts": [
    {
      "key": "HUT:2026-07-20:beacon-point-phase2-lease",
      "noted": "2026-07-20"
    },
    {
      "key": "DYN:2026-07-20:bla-priority-review",
      "noted": "2026-07-20"
    },
    {
      "key": "JSPR:2026-07-20:kira-merger-close",
      "noted": "2026-07-20"
    },
    {
      "key": "TEM:2026-07-20:personalis-acquisition",
      "noted": "2026-07-20"
    },
    {
      "key": "PSNL:2026-07-20:tempus-acquisition",
      "noted": "2026-07-20"
    },
    {
      "key": "KLRS:2026-07-20:phase1a-namd-expanded-data",
      "noted": "2026-07-20"
    },
    {
      "key": "ONCY:2026-07-20:fasttrack-anal-scc",
      "noted": "2026-07-20"
    },
    {
      "key": "RGNX:2026-07-20:follow-on-offering",
      "noted": "2026-07-20"
    },
    {
      "key": "BMNR:2026-07-20:eth-treasury-update",
      "noted": "2026-07-20"
    },
    {
      "key": "EYPT:2026-07-20:doj-dexycu-settlement",
      "noted": "2026-07-20"
    },
    {
      "key": "ETHE:2026-07-20:staking-cash-distribution-amendment",
      "noted": "2026-07-20"
    },
    {
      "key": "LXP:2026-07-20:brookfield-cppib-acquisition",
      "noted": "2026-07-21"
    },
    {
      "key": "MGY:2026-07-20:wildfire-energy-acquisition",
      "noted": "2026-07-21"
    },
    {
      "key": "ZWS:2026-07-20:intellihot-acquisition",
      "noted": "2026-07-21"
    },
    {
      "key": "SNBR:2026-07-20:bankruptcy-sale-sleep-country",
      "noted": "2026-07-21"
    },
    {
      "key": "AMD:2026-07-20:microsoft-helios-partnership",
      "noted": "2026-07-21"
    },
    {
      "key": "ASTS:2026-07-20:convertible-notes-launch-delay",
      "noted": "2026-07-21"
    },
    {
      "key": "BLTE:2026-07-20:asrs-secondary-endpoint-data",
      "noted": "2026-07-21"
    },
    {
      "key": "GLSI:2026-07-20:flamingo01-openlabel-data",
      "noted": "2026-07-21"
    },
    {
      "key": "CHINA-EM:2026-07-20:national-team-intervention",
      "noted": "2026-07-21"
    },
    {
      "key": "BTC:2026-07-21:etf-outflow-streak-easing",
      "noted": "2026-07-21"
    },
    {
      "key": "ETH:2026-07-21:etf-inflow-rotation",
      "noted": "2026-07-21"
    },
    {
      "key": "DYN:2026-07-21:dilutive-375m-offering",
      "noted": "2026-07-22"
    },
    {
      "key": "RGNX:2026-07-21:offering-reaction-conflict",
      "noted": "2026-07-22"
    },
    {
      "key": "ACAD:2026-07-20:fasttrack-alzheimers-psychosis",
      "noted": "2026-07-22"
    },
    {
      "key": "MU:2026-07-21:bofa-note-memory-rally",
      "noted": "2026-07-22"
    },
    {
      "key": "NBIS:2026-07-21:nvidia-stake-reflection-ai-deal",
      "noted": "2026-07-22"
    },
    {
      "key": "AMD:2026-07-21:analyst-upgrades-continued-rally",
      "noted": "2026-07-22"
    },
    {
      "key": "RKLB:2026-07-21:space-force-266m-contract",
      "noted": "2026-07-22"
    },
    {
      "key": "GM:2026-07-21:q2-beat-raised-guidance",
      "noted": "2026-07-22"
    },
    {
      "key": "CHINA-EM:2026-07-21:record-state-intervention-inflows",
      "noted": "2026-07-22"
    },
    {
      "key": "EWY:2026-07-20:record-korea-etf-inflows",
      "noted": "2026-07-22"
    },
    {
      "key": "COIN-HOOD-BLSH:2026-07-21:clarity-act-rally",
      "noted": "2026-07-22"
    },
    {
      "key": "BTC:2026-07-21:etf-inflow-streak-5day",
      "noted": "2026-07-22"
    },
    {
      "key": "ETH:2026-07-21:etf-inflow-breaks-8wk-outflow",
      "noted": "2026-07-22"
    },
    {
      "key": "LDO:2026-07-21:nansen-vault-lido-v3-launch",
      "noted": "2026-07-22"
    },
    {
      "key": "ARWR:2026-07-22:shasta3-4-phase3-topline",
      "noted": "2026-07-23"
    },
    {
      "key": "RGNX:2026-07-22:reaction-resolved-fell-17pct",
      "noted": "2026-07-23"
    },
    {
      "key": "CLARITY-ACT:2026-07-22:ethics-deal-reached",
      "noted": "2026-07-23"
    },
    {
      "key": "BTC:2026-07-22:etf-inflow-streak-6day",
      "noted": "2026-07-23"
    },
    {
      "key": "ETH:2026-07-22:etf-inflow-streak-4day",
      "noted": "2026-07-23"
    },
    {
      "key": "RUSSIA-CRYPTO:2026-07-21:state-duma-property-law",
      "noted": "2026-07-23"
    },
    {
      "key": "NBIS:2026-07-23:nvidia-93pct-stake-filed",
      "noted": "2026-07-24"
    },
    {
      "key": "AMD:2026-07-23:helios-production-advancing-ai",
      "noted": "2026-07-24"
    },
    {
      "key": "BMNR:2026-07-23:q3-earnings-revenue-beat-net-loss",
      "noted": "2026-07-24"
    },
    {
      "key": "MU:2026-07-23:hits-1000-capex-nand-shortage",
      "noted": "2026-07-24"
    },
    {
      "key": "DYN:2026-07-24:offering-closed-upsized-431m",
      "noted": "2026-07-24"
    },
    {
      "key": "BTC:2026-07-23:etf-inflow-streak-7day",
      "noted": "2026-07-24"
    },
    {
      "key": "ETH:2026-07-23:etf-inflow-streak-5day",
      "noted": "2026-07-24"
    },
    {
      "key": "CLARITY-ACT:2026-07-23:timeline-slips-thune",
      "noted": "2026-07-24"
    },
    {
      "key": "MU:2026-07-24:sandisk-guidance-reversal",
      "noted": "2026-07-25"
    },
    {
      "key": "SNDK:2026-07-24:nand-price-contraction-guidance",
      "noted": "2026-07-25"
    },
    {
      "key": "INTC:2026-07-23:q2-beat-chips-act-gaap-loss",
      "noted": "2026-07-25"
    },
    {
      "key": "MCHP:2026-07-24:hailo-acquisition-definitive-agreement",
      "noted": "2026-07-25"
    },
    {
      "key": "CHINA-EM:2026-07-24:tariff-125pct-effective",
      "noted": "2026-07-25"
    },
    {
      "key": "BTC:2026-07-23:etf-outflow-streak-snapped",
      "noted": "2026-07-25"
    },
    {
      "key": "ETH:2026-07-24:etf-inflow-despite-price-drop",
      "noted": "2026-07-25"
    },
    {
      "key": "QBTS:2026-07-27:att-expanded-quantum-partnership",
      "noted": "2026-07-28"
    },
    {
      "key": "SEMIS:2026-07-27:ai-financing-china-competition-selloff",
      "noted": "2026-07-28"
    },
    {
      "key": "BTC:2026-07-27:etf-outflow-fri-sat-despite-weekly-inflow",
      "noted": "2026-07-28"
    },
    {
      "key": "DYN:2026-07-28:dyne302-ind-clearance-fshd",
      "noted": "2026-07-29"
    },
    {
      "key": "IONQ:2026-07-28:skywater-acquisition-closed",
      "noted": "2026-07-29"
    },
    {
      "key": "DYN:2026-07-29:q2-2026-earnings-results",
      "noted": "2026-07-30"
    },
    {
      "key": "REPL:2026-07-29:fda-not-interpretable-melanoma-data",
      "noted": "2026-07-30"
    },
    {
      "key": "IBM:2026-07-29:hrl-nature-18qubit-spin-qpu",
      "noted": "2026-07-30"
    },
    {
      "key": "PCSA:2026-07-29:vidya-acquisition-200m-pipe",
      "noted": "2026-07-30"
    },
    {
      "key": "FED:2026-07-29:fomc-holds-rates-steady-3-dissents",
      "noted": "2026-07-30"
    },
    {
      "key": "MS-ETP:2026-07-29:eth-sol-etp-launch",
      "noted": "2026-07-30"
    },
    {
      "key": "MKTX:2026-07-30:ice-acquisition-167-cash",
      "noted": "2026-07-31"
    },
    {
      "key": "KPTI:2026-07-30:phase3-xport-ec042-missed-pfs",
      "noted": "2026-07-31"
    },
    {
      "key": "INTC:2026-07-30:tsmc-packaging-report-rally",
      "noted": "2026-07-31"
    },
    {
      "key": "BTC:2026-07-29:etf-inflow-resumes-after-4day-outflow",
      "noted": "2026-07-31"
    },
    {
      "key": "ETH:2026-07-29:etf-flow-conflicting-reports",
      "noted": "2026-07-31"
    }
  ]
}
```
