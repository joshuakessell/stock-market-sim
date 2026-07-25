# Morning Investment Research — Friday, July 24, 2026
*Window covered: Thursday, July 23, 2026 00:00 ET – Friday, July 24, 2026 ~05:05 ET*

**Data-sourcing note (read before the rest):** for the fourth run in a row, every structured, machine-readable source this briefing normally relies on was unreachable — SEC EDGAR, `data.sec.gov`, ClinicalTrials.gov, the Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com APIs all returned `403 Forbidden` / connection-refused. This was confirmed independently via direct `curl`, the proxy's own status endpoint (`connect_rejected`, "gateway answered 403 to CONNECT — policy denial"), and the repo's `fetch_quotes.py`. `WebFetch` also failed this run, even on a plain control page (reuters.com). This is a standing session-level network-policy block, not a site outage — see the administrative note at the end of this report. `WebSearch` was the only working tool, so every item below is sourced from search-result snippets and article text rather than a fetched primary filing, and **no live price quote could be pulled for any equity or crypto asset, so no fills or price-based marks were possible today** (see Portfolio section). Listing/ticker confirmations below carry over from prior verified runs rather than being re-checked against `data.sec.gov` today.

# 📈 Stocks

## Summary
| Ticker | Name | Theme | Headline | Impact | Rec |
|--------|------|-------|----------|--------|-----|
| NBIS | Nebius Group | Technology, AI & Quantum | SEC filing confirms Nvidia's 9.3% stake (22.26M sh/warrants); stock +18.8% | High | Watch |
| AMD | Advanced Micro Devices | Technology, AI & Quantum | Helios rackscale reaches production at Advancing AI 2026; stock fell 4% on broad Nasdaq selloff | Medium-High | Watch |
| DYN | Dyne Therapeutics *(held)* | Medical | Offering closed upsized to ~$431.4M via full over-allotment exercise (vs. $375M headline) | Medium | Hold |
| BMNR | BitMine Immersion | Technology, AI & Quantum | Q3 revenue beat ($46.5M) buried under $83.6M net loss on ETH derivatives | Medium | Watch |
| MU | Micron | Technology, AI & Quantum | Hit ~$1,000/share on hyperscaler capex + NAND-shortage forecast | Medium | Watch |
| BTC/ETH ETFs | IBIT, ETHA, FETH, etc. | ETFs & Fund Flows | BTC inflow streak hits 7 days (~$1B cumulative); ETH streak hits 5 days | Medium | Overweight |

### Technology, AI & Quantum

#### Nebius Group (NBIS, Nasdaq) — Impact: High
**What happened:** A July 23 SEC filing showed Nvidia holding 22,256,412 Nebius shares and pre-funded warrants — a 9.3% stake, the hard number behind the AI-compute relationship flagged in general terms on July 21. Shares jumped as much as 18.8% intraday, trading between $213.60 and $230.22. [Nvidia Delivers Fantastic News for Nebius Stock Investors (Motley Fool)](https://www.fool.com/investing/2026/07/23/nvidia-delivers-fantastic-news-for-nebius-stock-in/), [Why Nebius Stock Soared Today (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/why-nebius-stock-soared-today-232301591.html)
**What's new:** the July 21 entry described the stake in general terms; this is the first filed, quantified figure, and it drove a larger single-day move than the earlier reaction.
**Market impact:** Confirms Nvidia as a large, disclosed equity holder — reinforces the existing read-through rather than changing it.
**Recommendation: Watch** — real filing, large move, but an 18.8% pop on a now-quantified (not new) relationship risks being mostly priced already. Risk: elevated valuation and execution risk on capacity buildout. Monitoring trigger: Nebius's next earnings print, to see whether contracted revenue keeps pace with the re-rating.

#### AMD (AMD, Nasdaq) — Impact: Medium-High
**What happened:** At Advancing AI 2026 (San Francisco, July 22–23), AMD said its Helios rackscale platform is now in production for gigawatt-scale deployment, launched EPYC 9006 Series server CPUs for agentic-AI/HPC workloads, extended Ryzen AI Embedded for robotics, and announced a Ryzen AI Halo/Cisco enterprise collaboration. [AAI 2026: AMD Delivers Full-Stack Compute for the Agentic AI Era (AMD IR)](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era), [AMD Unveils New Products in Pursuit of $2 Trillion Market (Bloomberg)](https://www.bloomberg.com/news/articles/2026-07-23/amd-unveils-new-products-in-pursuit-of-2-trillion-opportunity)
**Market impact:** Despite the substantive product news, AMD fell 4% ($22.85, to $529.48) the same day. That tracks a broader Nasdaq selloff (-2%) driven by Alphabet (-7%) and Tesla (-14%) after their earnings, not a rejection of AMD's own announcements. [AMD Stock Sees 4% Decline Amid Afternoon Trading (GuruFocus)](https://www.gurufocus.com/news/8975301/amd-stock-sees-4-decline-amid-afternoon-trading), [Stock Market Today: Nasdaq falls over 2% (TheStreet)](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-23-2026)
**Recommendation: Watch** — Helios reaching production is a concrete roadmap milestone, but the market isn't rewarding it yet and macro capex jitters are doing the driving short-term. Risk: a broader AI-capex growth scare could keep pressuring the stock regardless of AMD's own execution. Monitoring trigger: next earnings call for Helios revenue recognition and named customers.

#### BitMine Immersion Technologies (BMNR, NYSE American) — Impact: Medium
**What happened:** BMNR's Q3 FY2026 results (period ended May 31, 2026) showed revenue of $46.54M (98% from ETH staking/validation) against a net loss of $83.58M, driven by a $92.1M loss on Ethereum-linked derivatives that more than offset staking revenue. Stock fell roughly 7.7% on July 23, trading $16.33–$17.87. [BitMine Immersion Technologies (BMNR) Releases Q3 2026 Earnings (Quiver Quantitative)](https://www.quiverquant.com/news/Bitmine+Immersion+Technologies+(BMNR)+Releases+Q3+2026+Earnings:+Revenue+Jumps+to+$46.5+Million,+Cash+Surges), [BitMine 10-Q: $45.7M ETH Staking Revenue vs $84M Net Loss (SpotedCrypto)](https://www.spotedcrypto.com/bitmine-eth-staking-10q-q3-2026-net-loss/)
**Market impact:** The staking-revenue growth story is real, but the derivatives book is now the dominant swing factor in BMNR's P&L — a structural risk distinct from the underlying ETH-treasury thesis already tracked on the watchlist.
**Recommendation: Watch** — a genuine earnings surprise (revenue beat, bottom-line miss) that changes the risk picture: results now hinge on derivatives exposure, not just ETH price and staking yield. Risk: continued mark-to-market losses on the derivatives book could pressure shares independent of ETH's own price. Monitoring trigger: next quarter's derivatives P&L and any disclosed hedging-policy change.

#### Micron (MU, Nasdaq) — Impact: Medium
**What happened:** MU rose about 4% to roughly $1,000 on July 23, credited to hyperscaler capex disclosures (Alphabet revenue $119.8B, +24% y/y, in its Q2 print), Nvidia's Vera Rubin platform news, and a TrendForce-flagged 2026 NAND supply-shortage forecast. [Micron (MU) Hits $1,000 on Three Catalysts (TradingKey)](https://www.tradingkey.com/analysis/stocks/us-stocks/262050862-micron-mu-stock-hits-1000-july-23-2026-google-capex-vera-rubin-nand-tradingkey), [Why Micron Stock Popped Today (Motley Fool)](https://www.fool.com/investing/2026/07/23/why-micron-stock-popped-today/)
**What's new:** the July 21 entry was a BofA-note-driven rally; today's move rests on a different, more concrete anchor (hyperscaler capex prints plus a supply-shortage forecast).
**Recommendation: Watch** — the memory-cycle thesis keeps getting corroborated from independent angles, a stronger signal than sentiment alone, but MU is already up sharply and priced for a lot of this. Risk: any capex guidance walk-back from hyperscalers would hit MU disproportionately. Monitoring trigger: Micron's own next quarterly print and HBM contract updates.

### Medical

#### Dyne Therapeutics (DYN, Nasdaq) — Impact: Medium — *held position update*
**What happened:** The offering flagged July 20–21 didn't just close as guided — underwriters fully exercised their 30-day option, upsizing the deal to 21,045,000 total shares at $20.50, for gross proceeds of roughly $431.4M (vs. the $375M headline figure). [Dyne Therapeutics Announces Closing of Upsized Public Offering (GlobeNewswire)](https://www.manilatimes.net/2026/07/24/tmt-newswire/globenewswire/dyne-therapeutics-announces-closing-of-upsized-public-offering-of-common-stock-and-full-exercise-by-underwriters-of-option-to-purchase-additional-shares/2390686), [Dyne Therapeutics 8-K exhibit (SEC.gov)](https://www.sec.gov/Archives/edgar/data/0001818794/000119312526312571/d112911dex991.htm)
**Market impact:** Modestly more dilution than originally modeled, but the balance sheet is now meaningfully stronger heading into the January 21, 2027 PDUFA date for z-rostudirsen.
**Recommendation: Hold** — the core thesis (BLA accepted, Priority Review, PDUFA Jan 21 2027) is unchanged; this is a financing mechanic, not a data or regulatory event. Risk: the additional ~2.7M shares add permanent dilution beyond what was already priced in. Monitoring trigger: price behavior relative to the $20.50 offering print and the $19.00 stop.

### ETFs & Fund Flows

#### Spot Bitcoin & Ethereum ETFs (IBIT, ETHA, FETH, ETHB, etc.) — Impact: Medium
**What happened:** U.S. spot Bitcoin ETFs logged a seventh straight day of net inflows through July 23 (+$68.99M that day), pushing the streak total to roughly $999.38M since July 14 — nearly double the 5-day streak total already flagged July 21. Spot Ethereum ETFs extended their own streak to five sessions, +$26.3M on July 23 (FETH $14.9M, ETHA $8.5M, ETHB $2.9M). [Bitcoin ETF Inflows Near $1 Billion In 7-Day Streak (Benzinga)](https://www.benzinga.com/crypto/cryptocurrency/26/07/60636938/bitcoin-etf-inflows-near-1-billion-in-7-day-streak-is-70000-btc-the-next-stop), [U.S. Spot Ethereum ETFs Extend Inflow Streak To Five Sessions (Bitcoin World)](https://bitcoinworld.co.in/spot-ethereum-etf-inflows-five-sessions/)
**What's new:** streak length and cumulative dollar figures both advanced materially (BTC 5→7 days, nearing a $1B milestone; ETH 4→5 days with a specific $26.3M print) — not a restatement.
**Positioning: Overweight the theme** — sustained multi-day institutional inflows into both BTC and ETH products is a real, verifiable demand signal. Risk: BTC's own spot price pulled back roughly 1–2% over the same window (see Cryptos section) even as flows stayed positive — flows and price can diverge short-term.

### No new catalysts this window (checked, nothing cleared the bar)
- **HUT (held):** +7% intraday July 23, but that traces to continued reaction to the already-covered $9.8B Beacon Point lease (Morgan Stanley's July 20 Overweight initiation, Needham's PT raise to $145 from $128), not a new overnight event. Thesis unchanged, status intact.
- **RKLB (watchlist):** the "$266M Air Force contract" resurfacing in July 23 coverage is the same Space Force award already logged July 21. The larger $8B Iridium acquisition is real but was announced June 29, outside this window.
- **JSPR, TEM, PSNL, RGNX, BLTE, ACAD, ONCY, KLRS, GLSI (watchlist):** no new developments in the window; activity found (analyst PT tweaks, conference mentions, routine IR items) either predates the window or restates catalysts already covered (Kira merger, Personalis deal, the RGNX offering, ASRS data, remlifanserin Fast Track, anal-SCC Fast Track, the nAMD Phase 1a data, FLAMINGO-01).
- **Quantum computing:** nothing both material and tied to a listed name — IonQ/Rigetti activity was routine (Rigetti set an Aug. 6 earnings date); a DARPA award and a tool launch both involve private companies with no public-market proxy.
- **Emerging markets:** no dated, sourced catalyst found beyond generic "EM is up YTD" commentary.

# ₿ Cryptos
*Prices are WebSearch-derived only this session — the exchange APIs (Coinbase, Kraken, crypto.com) this section normally cross-checks against were blocked, so these figures are **not** cross-venue-confirmed as the methodology requires. Figures reflect a spread across sources captured at different times on July 23–24; read the range, not a single number. As of ~05:00 ET July 24, 2026.*

## Market snapshot
| Asset | Price (USD) | 24h % | Sources agree? | Note |
|-------|-------------|-------|----------------|------|
| BTC | ~$64,700–$66,300 (latest prints ~$64,860–$65,050) | approx. -1% to -2% | ✗ — WebSearch only, not exchange-cross-checked | Consolidating below $66K after a 13% July rally stalled |
| ETH | ~$1,890–$1,925 | not independently confirmed this run | ✗ — WebSearch only, not exchange-cross-checked | Range reflects different fetch times across sources |

### Bitcoin (BTC) — ETF inflow streak extends to 7 days, price consolidating
**What happened:** BTC is trading in the mid-$64,000s to mid-$65,000s, down roughly 1-2% over the past 24h by most sources, as "a 13% July recovery runs out of steam" per CoinDesk's July 23 market wrap. [Bitcoin consolidates below $66,000 as a 13% July recovery runs out of steam (CoinDesk)](https://www.coindesk.com/markets/2026/07/23/crypto-catches-its-breath-as-bitcoin-settles-into-a-holding-pattern-after-its-best-month-since-january), [Bitcoin ETF Inflows Near $1 Billion In 7-Day Streak (Benzinga)](https://www.benzinga.com/crypto/cryptocurrency/26/07/60636938/bitcoin-etf-inflows-near-1-billion-in-7-day-streak-is-70000-btc-the-next-stop)
**Price action:** Spot price has slipped even as ETF inflows kept coming (see Stocks → ETFs & Fund Flows) — fund-flow demand hasn't translated into spot strength this week, worth watching for whether that's a lag or a genuine divergence.
**Read: Watch** — the inflow streak is a real, multi-day signal, but price is moving the opposite direction over the same window, so this isn't a clean momentum story. Risk: a break of the $64K area on continued profit-taking despite ETF demand. Monitoring trigger: whether the inflow streak survives a down week for spot price.

### Ethereum (ETH) — inflow streak now 5 days, CLARITY Act timeline slips
**What happened:** ETH trades around $1,890–$1,925. Spot ETH ETFs added a fifth straight day of inflows July 23 ($26.3M). Separately, the CLARITY Act — the crypto market-structure bill whose ethics-provision deal was reported reached July 22 — hit a new snag July 23: Senate Majority Leader Thune said the bill likely won't get floor time before the summer recess, and the newest draft's DOJ-only enforcement of its presidential crypto-issuance ban (rather than state AG enforcement) is causing some Democratic supporters to reconsider. White House crypto adviser Patrick Witt said the first week of August "still has potential." [Clarity Act expected to miss its window before Congress' summer break (CoinDesk)](https://www.coindesk.com/policy/2026/07/23/clarity-act-expected-to-miss-its-window-before-congress-summer-break-leadership-says), [U.S. Spot Ethereum ETFs Extend Inflow Streak To Five Sessions (Bitcoin World)](https://bitcoinworld.co.in/spot-ethereum-etf-inflows-five-sessions/)
**What's new:** July 22's entry was "ethics deal reached"; July 23's reporting shows that deal is now contested on enforcement mechanics and the bill's timeline has slipped — a materially more uncertain state, not a repeat.
**Read: Watch** — ETF demand is holding up, but the regulatory tailwind the market had been pricing just got less certain. Risk: further slippage could push passage into 2027 or kill this legislative window. Monitoring trigger: whether Thune brings the bill to the floor in the "first week of August" window the White House is still citing.

---
**Sources consulted:** WebSearch only (SEC EDGAR, ClinicalTrials.gov, FDA.gov, Yahoo Finance, Coinbase/Kraken/crypto.com APIs all blocked this session — 4th consecutive day). News and press cited inline: GlobeNewswire/company press releases and SEC.gov documents surfaced via search (not fetched directly), Motley Fool, Bloomberg, Benzinga, CoinDesk, TradingKey, GuruFocus, TheStreet, Quiver Quantitative, SpotedCrypto, Bitcoin World.
*Informational only; not investment advice. Crypto is volatile and speculative. Verify independently before trading. Prices and figures in this briefing were not cross-checked against primary/exchange sources due to a standing network-policy block — treat with extra caution until structured-source access is restored. Generated ~05:05 ET, July 24, 2026.*

---

# Portfolio

## Snapshot
No live quotes were obtainable this run (see data-sourcing note above), so **no dollar-accurate account valuation is possible today** — same limitation as the prior three runs. As of the last confirmed state (July 20 fills; unchanged since):
- Cash: $7,397.92
- Open positions at cost: DYN 63 sh @ $23.75 ($1,496.25) + HUT 11 sh @ $100.53 ($1,105.83) = $2,602.08 at cost
- Total account value at cost basis: $10,000.00 (unchanged from the $10,000 starting value; no realized gains/losses booked and no mark-to-market available)
- Benchmark: 13.4281 SPY shares at $744.71 cost ($10,000 equivalent at inception); no current SPY price available to compare.
- Return vs. $10,000 start and vs. SPY benchmark: **cannot be computed today** without a live quote — deferred until data access is restored.

## Open positions (ranked by cost basis; no live P&L available)
| Ticker | Shares | Avg cost | Current price | Unrealized P&L | Thesis status |
|--------|--------|----------|----------------|-----------------|---------------|
| HUT | 11 | $100.53 | Unavailable (quote feed blocked); unverified search snippets suggest continued strength (+7% intraday July 23) but are not used as an official mark | N/A | Intact — no new catalyst since the July 20 Beacon Point lease. |
| DYN | 63 | $23.75 | Unavailable (quote feed blocked) | N/A | Watch (unchanged) — regulatory thesis intact; the now-larger $431.4M offering (vs. $375M) adds dilution and keeps this closer scrutiny warranted than "intact." |

## Today's trades
**No trades today.** No reliable machine-readable quote existed for any ticker (equities or crypto) — the same 403 policy block that has affected every run since July 21 persisted today. Nothing found this window cleared the Buy bar on its own merits either (NBIS, AMD, BMNR, and MU were all rated Watch, not Buy), so the lack of a quote wasn't the only thing holding back a fill today. DYN and HUT were held unchanged.

## Realized P&L to date
$0.00 realized (no positions have been closed). Combined realized + unrealized total cannot be computed today without a live mark, but stands at $0.00 realized plus an unknown unrealized figure pending restored data access.

## Watchlist changes
Refreshed (new information, added-date and expiry reset to today, now expiring 2026-08-07): **NBIS** (SEC filing quantifies the Nvidia stake at 9.3%/22.26M shares), **AMD** (Helios reached production at Advancing AI 2026), **BMNR** (Q3 earnings: revenue beat, larger net loss on ETH derivatives), **MU** (hit ~$1,000/share on hyperscaler capex + NAND-shortage forecast).

No new tickers added — every name that cleared the bar today (NBIS, AMD, BMNR, MU) was already on the watchlist from a prior run.

The remaining eleven names carried over from July 20–23 (JSPR, TEM, PSNL, KLRS, ONCY, RGNX, BLTE, GLSI, RKLB, ACAD, ARWR) are unchanged; none have expired (earliest expiry is 2026-08-03).

## Administrative notes
- `reports/unsent-2026-07-23.md` was found in the repo (yesterday's briefing was drafted but never actually sent, for the same reasons noted below). It has been renamed to `reports/morning-research-2026-07-23.md` in today's commit per the standing procedure, flagged here exactly once.
- **This is the fourth consecutive run** in which (a) the session's network egress policy blocks every structured data source (SEC EDGAR, ClinicalTrials.gov, FDA.gov, Yahoo Finance, all three crypto exchange APIs) with a 403, confirmed independently via curl, the proxy status endpoint, and the repo's own `fetch_quotes.py`, and (b) the Gmail connector available to this session exposes only draft creation with no send capability, meaning every run's report ends up as an unsent draft rather than delivered mail. Neither issue is a one-off; both are standing configuration gaps at the account/environment level — restoring egress access to market-data and filing endpoints, and granting the Gmail connector send scope, since the paper-trading simulation has not executed a single fill or delivered a single email since it opened on July 20.

```PORTFOLIO_STATE
{
  "version": 1,
  "initialized_at": "2026-07-20T10:50:30-04:00",
  "last_run": "2026-07-24",
  "cash": 7397.92,
  "positions": [
    {
      "ticker": "DYN",
      "shares": 63,
      "avg_cost": 23.75,
      "entry_date": "2026-07-20",
      "stop": 19.0,
      "target": 32.0,
      "thesis": "FDA accepted BLA for z-rostudirsen (DMD, exon 51) with Priority Review, PDUFA Jan 21 2027; the offering closed July 24 upsized further via full over-allotment exercise (21,045,000 sh at $20.50, ~$431.4M gross vs. the $375M headline) — more dilutive than initially priced but does not itself invalidate the regulatory thesis.",
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
      "reason": "Hit roughly $1,000/share July 23 on a different anchor than the July 21 BofA note: hyperscaler capex disclosures (Alphabet, Tesla) plus a TrendForce 2026 NAND-shortage forecast, corroborating the memory-cycle thesis from an independent angle",
      "added": "2026-07-24",
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
    }
  ],
  "seen_catalysts": [
    { "key": "HUT:2026-07-20:beacon-point-phase2-lease", "noted": "2026-07-20" },
    { "key": "DYN:2026-07-20:bla-priority-review", "noted": "2026-07-20" },
    { "key": "JSPR:2026-07-20:kira-merger-close", "noted": "2026-07-20" },
    { "key": "TEM:2026-07-20:personalis-acquisition", "noted": "2026-07-20" },
    { "key": "PSNL:2026-07-20:tempus-acquisition", "noted": "2026-07-20" },
    { "key": "KLRS:2026-07-20:phase1a-namd-expanded-data", "noted": "2026-07-20" },
    { "key": "ONCY:2026-07-20:fasttrack-anal-scc", "noted": "2026-07-20" },
    { "key": "RGNX:2026-07-20:follow-on-offering", "noted": "2026-07-20" },
    { "key": "BMNR:2026-07-20:eth-treasury-update", "noted": "2026-07-20" },
    { "key": "EYPT:2026-07-20:doj-dexycu-settlement", "noted": "2026-07-20" },
    { "key": "ETHE:2026-07-20:staking-cash-distribution-amendment", "noted": "2026-07-20" },
    { "key": "LXP:2026-07-20:brookfield-cppib-acquisition", "noted": "2026-07-21" },
    { "key": "MGY:2026-07-20:wildfire-energy-acquisition", "noted": "2026-07-21" },
    { "key": "ZWS:2026-07-20:intellihot-acquisition", "noted": "2026-07-21" },
    { "key": "SNBR:2026-07-20:bankruptcy-sale-sleep-country", "noted": "2026-07-21" },
    { "key": "AMD:2026-07-20:microsoft-helios-partnership", "noted": "2026-07-21" },
    { "key": "ASTS:2026-07-20:convertible-notes-launch-delay", "noted": "2026-07-21" },
    { "key": "BLTE:2026-07-20:asrs-secondary-endpoint-data", "noted": "2026-07-21" },
    { "key": "GLSI:2026-07-20:flamingo01-openlabel-data", "noted": "2026-07-21" },
    { "key": "CHINA-EM:2026-07-20:national-team-intervention", "noted": "2026-07-21" },
    { "key": "BTC:2026-07-21:etf-outflow-streak-easing", "noted": "2026-07-21" },
    { "key": "ETH:2026-07-21:etf-inflow-rotation", "noted": "2026-07-21" },
    { "key": "DYN:2026-07-21:dilutive-375m-offering", "noted": "2026-07-22" },
    { "key": "RGNX:2026-07-21:offering-reaction-conflict", "noted": "2026-07-22" },
    { "key": "ACAD:2026-07-20:fasttrack-alzheimers-psychosis", "noted": "2026-07-22" },
    { "key": "MU:2026-07-21:bofa-note-memory-rally", "noted": "2026-07-22" },
    { "key": "NBIS:2026-07-21:nvidia-stake-reflection-ai-deal", "noted": "2026-07-22" },
    { "key": "AMD:2026-07-21:analyst-upgrades-continued-rally", "noted": "2026-07-22" },
    { "key": "RKLB:2026-07-21:space-force-266m-contract", "noted": "2026-07-22" },
    { "key": "GM:2026-07-21:q2-beat-raised-guidance", "noted": "2026-07-22" },
    { "key": "CHINA-EM:2026-07-21:record-state-intervention-inflows", "noted": "2026-07-22" },
    { "key": "EWY:2026-07-20:record-korea-etf-inflows", "noted": "2026-07-22" },
    { "key": "COIN-HOOD-BLSH:2026-07-21:clarity-act-rally", "noted": "2026-07-22" },
    { "key": "BTC:2026-07-21:etf-inflow-streak-5day", "noted": "2026-07-22" },
    { "key": "ETH:2026-07-21:etf-inflow-breaks-8wk-outflow", "noted": "2026-07-22" },
    { "key": "LDO:2026-07-21:nansen-vault-lido-v3-launch", "noted": "2026-07-22" },
    { "key": "ARWR:2026-07-22:shasta3-4-phase3-topline", "noted": "2026-07-23" },
    { "key": "RGNX:2026-07-22:reaction-resolved-fell-17pct", "noted": "2026-07-23" },
    { "key": "CLARITY-ACT:2026-07-22:ethics-deal-reached", "noted": "2026-07-23" },
    { "key": "BTC:2026-07-22:etf-inflow-streak-6day", "noted": "2026-07-23" },
    { "key": "ETH:2026-07-22:etf-inflow-streak-4day", "noted": "2026-07-23" },
    { "key": "RUSSIA-CRYPTO:2026-07-21:state-duma-property-law", "noted": "2026-07-23" },
    { "key": "NBIS:2026-07-23:nvidia-93pct-stake-filed", "noted": "2026-07-24" },
    { "key": "AMD:2026-07-23:helios-production-advancing-ai", "noted": "2026-07-24" },
    { "key": "BMNR:2026-07-23:q3-earnings-revenue-beat-net-loss", "noted": "2026-07-24" },
    { "key": "MU:2026-07-23:hits-1000-capex-nand-shortage", "noted": "2026-07-24" },
    { "key": "DYN:2026-07-24:offering-closed-upsized-431m", "noted": "2026-07-24" },
    { "key": "BTC:2026-07-23:etf-inflow-streak-7day", "noted": "2026-07-24" },
    { "key": "ETH:2026-07-23:etf-inflow-streak-5day", "noted": "2026-07-24" },
    { "key": "CLARITY-ACT:2026-07-23:timeline-slips-thune", "noted": "2026-07-24" }
  ]
}
```
