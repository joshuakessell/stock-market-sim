# Morning Investment Research — Thursday, July 30, 2026
*Window covered: Wednesday, July 29, 2026 00:00 ET – Thursday, July 30, 2026 ~05:06 ET*

**Data-sourcing note (read before the rest):** for the tenth run in a row, every structured, machine-readable source this briefing normally relies on was unreachable — SEC EDGAR, `data.sec.gov`, ClinicalTrials.gov, bioRxiv, FDA.gov, arXiv, NASA, the Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com APIs all returned `403 Forbidden` on the CONNECT tunnel (confirmed independently via direct `curl` to each host, the proxy's own status endpoint showing `connect_rejected` for the same four hosts, `WebFetch` — 403 even on non-financial sites like Wikipedia — and the repo's own `fetch_quotes.py`). `WebSearch` continues to work and is the only source below; nothing here is a fetched primary filing or exchange quote, and **no live, cross-checked price exists for any equity or crypto asset today.** The Gmail connector available to this session again exposes create/update-draft tools only — no send tool of any kind. See the administrative note at the end.

# 📈 Stocks

**Three items are worth noting, none of them a fresh Buy-grade opportunity given no fill can be priced today anyway.**

### Medical
#### Dyne Therapeutics (DYN, Nasdaq) — Impact: Low-Medium (earnings update, existing position)
**What happened:** Dyne reported Q2 2026 results: a net loss of $178.6M ($1.08/share), wider than the $110.9M ($0.97/share) loss a year earlier and missing consensus EPS by $0.34. Cash, equivalents, and marketable securities stood at $898.5M as of June 30, which the company says, combined with July's public offering proceeds, funds operations into Q2 2028. The ACHIEVE registrational cohort for z-basivarsen (DM1) completed enrollment at 71 participants. Reported via GlobeNewswire/Manila Times, StockTitan, and MarketBeat.
**Market impact:** This is a financial/operational update, not a new readout on the lead asset (z-rostudirsen, the actual basis for the position). It does, however, materially address the dilution overhang flagged after the July offering — cash runway is now specified out to Q2 2028.
**Recommendation: Hold (unchanged, watch status stands)** — the extended runway eases the near-term financing risk from the July raise but doesn't touch the z-rostudirsen regulatory thesis itself. Risk: still the PDUFA timeline (Jan 21, 2027) and continued cash burn. Monitoring trigger unchanged: any update on the z-rostudirsen regulatory path.

#### Replimune Group (REPL, Nasdaq) — Impact: Medium-High [not a position or watchlist name]
**What happened:** Ahead of a July 30 FDA advisory committee (Cellular, Tissue, and Gene Therapies Advisory Committee), FDA staff briefing documents called Replimune's single-arm melanoma data package for RP1 (vusolimogene oderparepvec) "not interpretable," citing the absence of an Opdivo-only control arm. This is the drug's third FDA review cycle; an August 2 decision is expected. Shares fell roughly 30-32% on the briefing. Reported via BioSpace, Benzinga, PharmExec, and BioPharm International.
**Market impact:** A negative regulatory signal directly ahead of a binding adcomm vote and PDUFA date.
**Recommendation: Avoid** — this is a "don't buy the dip" situation, not a new opportunity: the FDA's own briefing documents question interpretability of the primary evidence supporting approval. Risk: a surprise adcomm vote in the company's favor could reverse sentiment quickly. Monitoring trigger: the adcomm vote outcome (today) and the August 2 FDA action date.

### Technology, AI & Quantum
#### IBM (IBM, NYSE) / HRL Laboratories — Impact: Low (research validation, pending acquisition)
**What happened:** HRL Laboratories — under a definitive, not-yet-closed agreement to be acquired by IBM (announced July 23, expected to close Q3 2026) — published a Nature study demonstrating an 18-qubit silicon-spin quantum processing unit that operates autonomously at 4 Kelvin via a custom cryogenic CMOS control chip, with basic error-detecting codes on standard silicon-germanium wafers. Reported via Quantum Computing Report and ScienceDaily.
**Market impact:** Technical validation of the silicon-spin approach IBM is acquiring HRL for, ahead of the deal's Q3 close; incremental relative to IBM's overall scale.
**Recommendation: Watch** — a real result, but not sized to move a company IBM's size on its own, and the acquisition itself is already public/priced. Risk: the deal hasn't closed. Monitoring trigger: deal close (Q3 2026) and IBM's next update on integrating spin-qubit manufacturing at its Anderon foundry.

### Deals
#### Processa Pharmaceuticals (PCSA, Nasdaq) / Vidya Therapeutics — Impact: Low [Deal]
**What happened:** Processa announced a definitive agreement to acquire private Vidya Therapeutics (a BTK inhibitor, VT-7208, for immunology/inflammation) alongside a roughly $200M private placement led by Bain Capital, RA Capital, and Cormorant. Reported via GlobeNewswire and MedCity News.
**Market impact:** A dilutive financing paired with an early-stage pipeline addition.
**Recommendation: Not rated — below the account's investable price threshold.** PCSA last traded near $2.01 (previous close $3.05), at or below the roughly-$2 floor this account screens out; noted for completeness, not tracked. Monitoring trigger: none set.

Nothing else in the window (space, emerging markets, ETFs beyond the note below) turned up a genuinely new, unambiguous, multi-source-corroborated catalyst distinct from names already logged in `seen_catalysts`. HUT had no new company-specific news this window: shares were reported lower into its August 4 earnings date amid a broader tech/crypto pullback, with analyst target raises (KBW, Benchmark, Morgan Stanley) that were already in motion prior to this window — thesis unchanged, still intact. Memory names (MU, SNDK) were reported staging a premarket reversal July 29 after the prior week's selloff — a continuation of the situation already on the MU watchlist entry, not a fresh catalyst. SpaceX's reported $1.6B, 18-launch Space Force order (July 29) has no listed public-market proxy (SpaceX is private) and is noted for context only.

# ₿ Cryptos

**No material token-specific catalyst; the macro backdrop was the July 29 FOMC decision, and no cross-checked price is available to report.**

The Fed held its target range at 3.50%-3.75% (9-3 vote), a fifth straight hold; three regional presidents (Hammack, Kashkari, Logan) dissented in favor of a 25bp hike, citing inflation persistently above target. Search snippets (not cross-checked against an exchange) put Bitcoin's July 29 morning range at roughly $63,850-64,250 and Ethereum near $1,905-1,920, with both assets moving in opposite directions intraday ahead of the Fed decision. No comparable snapshot exists yet for July 30. Separately, Morgan Stanley launched Ethereum and Solana ETPs (0.14% expense ratio, staking rewards passed through), extending its crypto ETP lineup alongside its existing Bitcoin product — a distribution/access datapoint, not a token-specific catalyst.

**Positioning: Neutral** on the crypto-ETF-access theme (Morgan Stanley ETH/SOL ETP launch) — broadening institutional access is a slow-moving structural tailwind, not a same-day trigger.

---
**Sources consulted:** WebSearch only (SEC EDGAR, ClinicalTrials.gov, bioRxiv, FDA.gov, arXiv, NASA, Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com APIs all blocked this session — 10th consecutive day, confirmed via `curl`, `WebFetch`, the proxy status endpoint, and the repo's own `fetch_quotes.py`).

*Informational only; not investment advice. Crypto is volatile and speculative. Verify independently before trading. Generated ~05:06 ET, July 30, 2026.*

---

# Portfolio

## Snapshot
No live quotes were obtainable this run (see data-sourcing note above) — the same limitation as the prior nine runs. As of the last confirmed state (July 20 fills; unchanged since):
- Cash: $7,397.92
- Open positions at cost: DYN 63 sh @ $23.75 ($1,496.25) + HUT 11 sh @ $100.53 ($1,105.83) = $2,602.08 at cost
- Total account value at cost basis: $10,000.00 (unchanged from the $10,000 starting value; no realized gains/losses booked and no mark-to-market available)
- Benchmark: 13.4281 SPY shares at $744.71 cost ($10,000 equivalent at inception); no current SPY price available to compare.
- Return vs. $10,000 start and vs. SPY benchmark: **cannot be computed today** without a live quote, deferred until data access is restored.

Unverified, search-sourced context only (not a fill basis, and inconsistent across sources — illustrating exactly why these aren't used as marks): one source put DYN near $23.89 and another near $17.04; HUT was reported between roughly $94.62 and $101.14 (last close) with an intraday range of $86.89-$101.93 on July 29. None of these numbers are cross-checked and none are used to mark the book.

## Open positions (ranked by cost basis; no live P&L available)
| Ticker | Shares | Avg cost | Current price | Unrealized P&L | Thesis status |
|--------|--------|----------|----------------|-----------------|---------------|
| HUT | 11 | $100.53 | Unavailable (quote feed blocked) | N/A | Intact — no contradicting news this window; shares reportedly softer into the Aug 4 earnings date amid a broader sector pullback, but analyst target raises (KBW $157, Benchmark $195, Morgan Stanley $263) remain in place. |
| DYN | 63 | $23.75 | Unavailable (quote feed blocked) | N/A | Watch (unchanged) — regulatory thesis intact; Q2 earnings extend the cash runway to Q2 2028, easing (not eliminating) the dilution concern from the July offering. |

## Today's trades
**No trades today.** No reliable machine-readable quote existed for any ticker — the same policy block that has affected every run since around July 21 persisted for a tenth day, so no fill could be priced from a real source. Independent of the outage, nothing this window cleared the bar for new money: DYN/HUT updates don't change position status, Replimune is an Avoid, the IBM/HRL item is Watch-only and not sized for a name IBM's size, and Processa trades below the account's investable price floor.

## Realized P&L to date
$0.00 realized (no positions have been closed). Combined realized + unrealized total cannot be computed today without a live mark; it stands at $0.00 realized plus an unknown unrealized figure pending restored data access.

## Watchlist changes
No adds, no removes. All eighteen previously carried names (JSPR, TEM, PSNL, KLRS, ONCY, RGNX, BMNR, AMD, BLTE, GLSI, NBIS, RKLB, MU, MCHP, ACAD, ARWR, QBTS, IONQ) are unchanged; none have expired (earliest expiry is 2026-08-03).

`seen_catalysts` was reviewed for pruning (entries older than 30 days); the oldest entries are dated July 20, ten days ago, so none qualify for pruning yet.

## Administrative notes
- `reports/unsent-2026-07-29.md` was found in the repo (Wednesday's briefing was compiled but never actually sent, for the same reasons noted below). It has been renamed to `reports/morning-research-2026-07-29.md` in today's commit per the standing procedure, flagged here exactly once.
- **This is the tenth consecutive run** in which (a) the session's network egress policy blocks every structured data source (SEC EDGAR, ClinicalTrials.gov, bioRxiv, FDA.gov, arXiv, NASA, Yahoo Finance, all three crypto exchange APIs) with a 403, confirmed independently via curl, WebFetch, the proxy status endpoint, and the repo's own `fetch_quotes.py`, and (b) the Gmail connector available to this session exposes only draft creation with no send capability, meaning every run's report ends up as an unsent draft rather than delivered mail. Neither issue is a one-off; both are standing configuration gaps at the account/environment level that a human needs to fix — the network policy needs the relevant hosts allow-listed, and the Gmail connector needs send scope granted. The paper-trading simulation has not executed a single fill or delivered a single email since it opened on July 20, ten days and ten runs ago. This run's self-check (`scripts/selfcheck.py`) was run without `--quotes` since no quote data exists to check against; no numbers were patched to force a pass.

```PORTFOLIO_STATE
{
  "version": 1,
  "initialized_at": "2026-07-20T10:50:30-04:00",
  "last_run": "2026-07-30",
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
    }
  ]
}
```
