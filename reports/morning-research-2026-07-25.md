# Morning Investment Research — Saturday, July 25, 2026
*Window covered: Friday, July 24, 2026 00:00 ET – Saturday, July 25, 2026 ~05:04 ET*

**Data-sourcing note (read before the rest):** for the fifth run in a row, every structured, machine-readable source this briefing normally relies on was unreachable — SEC EDGAR, `data.sec.gov`, ClinicalTrials.gov, the Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com APIs all returned `403 Forbidden`/tunnel-connection-failed. Confirmed independently via direct `curl`, the proxy's own status endpoint (`connect_rejected`, "gateway answered 403 to CONNECT — policy denial"), and the repo's `fetch_quotes.py` (all seven equity tickers and both crypto assets errored). `WebFetch` also failed again this run on a plain control page (reuters.com). `WebSearch` was the only working tool, so every item below is sourced from search-result snippets and article text rather than a fetched primary filing or exchange API, and **no live, cross-checked price quote could be pulled for any equity or crypto asset, so no fills or price-based marks were possible today** — moot for fills regardless, since markets are closed (Saturday). See Portfolio section and the administrative note at the end.

# 📈 Stocks

## Summary
| Ticker | Name | Theme | Headline | Impact | Rec |
|--------|------|-------|----------|--------|-----|
| MU | Micron *(watchlist)* | Technology, AI & Quantum | Fell ~8% a day after hitting $1,000, as SanDisk's own guidance flags NAND price contraction | High | Watch |
| SNDK | SanDisk | Technology, AI & Quantum | Dropped ~11% on weak guidance and a NAND price-contraction warning | Medium | Watch |
| INTC | Intel | Technology, AI & Quantum | Q2 revenue +25% YoY beat, but an $11B GAAP loss (CHIPS-Act warrant mark-to-market) and shares fell 6.5% | Medium | Watch |
| MCHP | Microchip Technology | Technology, AI & Quantum | Definitive agreement to acquire edge-AI chipmaker Hailo; terms undisclosed | Medium | Watch |
| FXI/MCHI | China ETFs | Emerging Markets | New 12.5% US tariff on Chinese goods takes effect; PBOC offsets with CNY 500B liquidity injection | Medium-High | Neutral |

### Technology, AI & Quantum

#### Micron (MU, Nasdaq) *(watchlist)* — Impact: High
**What happened:** One day after the July 23 rally that put MU near $1,000/share on hyperscaler-capex and NAND-shortage optimism, the stock fell to $909.35 (a **previous close of $990.21**, roughly -8.2%) on July 24 as part of a sector-wide memory selloff. [Micron stock price data (Investing.com)](https://www.investing.com/equities/micron-tech). The same-day trigger was SanDisk's own guidance (see below) plus reports that SK Hynix and Micron itself sank alongside it. [SK Hynix and Micron Sink 6%, SanDisk Drops 9% as Korea Chip Selloff Hits U.S. Memory Stocks (247wallst.com)](https://247wallst.com/investing/2026/07/24/sk-hynix-and-micron-sink-6-sandisk-drops-9-as-korea-chip-selloff-hits-u-s-memory-stocks/)
**Market impact:** This directly conflicts with the bullish memory-cycle thesis added to the watchlist just one day earlier (TrendForce NAND-shortage forecast, hyperscaler capex disclosures). Both the bull case (shortage forecast) and a bear signal (a supplier's own guidance flagging price contraction) are now live within the same 24 hours — a genuine conflict, not a smoothed-over one.
**Recommendation: Watch** (refreshed, not upgraded) — the memory-cycle thesis is now contested by data from inside the same sector, not just macro jitters. Risk: if NAND pricing is actually turning down, the capex-driven bull case is premature. Monitoring trigger: Micron's own next quarterly print and guidance, which will settle whether SanDisk's warning was company-specific or sector-wide.

#### SanDisk (SNDK, Nasdaq) — Impact: Medium
**What happened:** SanDisk fell as much as 10.8% to $1,436.56 on July 24 after issuing disappointing quarterly guidance flagging NAND flash price contraction, enterprise storage inventory buildup, and soft consumer demand; multiple analysts downgraded on margin-compression concerns. [Why Did Sandisk Stock Drop Friday? (Motley Fool)](https://www.fool.com/investing/2026/07/24/why-did-sandisk-stock-drop-friday/), [SanDisk Corporation Stock (SNDK) Moved Down by 7.88% on Jul 24 (TradingKey)](https://www.tradingkey.com/news/market-movers/262052980-market-movers-sndk-20260724)
**Market impact:** Direct primary-source counter-signal to the memory-shortage narrative (see MU above); triggered a broader chip-sector pullback (semiconductor gauge -4.3% on the day).
**Recommendation: Watch** — a single company's guidance isn't proof the whole NAND cycle turned, but it is the most concrete, company-specific data point against the shortage thesis so far. Risk: enterprise inventory gluts can persist for multiple quarters. Monitoring trigger: next NAND-pricing data point from a second supplier (Micron, SK Hynix, Kioxia) to confirm or refute.

#### Intel (INTC, Nasdaq) — Impact: Medium
**What happened:** Intel's Q2 2026 revenue rose 25% YoY to $16.1B (vs. $14.42B expected) — its fastest growth in over 15 years — with adjusted EPS of $0.42, double the $0.21 estimate, led by a 59% YoY jump in Data Center & AI revenue to $6.3B. GAAP results showed an $11B net loss ($2.16/share) driven by a $12.5B mark-to-market loss on shares escrowed under Intel's CHIPS Act agreement with the US government — an accounting item, not an operating miss. Shares initially rose on the print but fell 6.5% in Friday trading. [Intel Q2 2026 earnings: revenue up 25%, fastest growth since 2011 (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/intel-q2-2026-earnings-revenue-205531105.html), [Why Did Intel Stock Drop Friday? (Motley Fool)](https://www.fool.com/investing/2026/07/24/why-did-intel-stock-drop-friday/)
**Market impact:** The Friday drop tracks the same broad chip-sector selloff (SanDisk, Micron) rather than a rejection of Intel's own beat — the GAAP headline loss is a warrant-valuation artifact, not a cash or operating problem.
**Recommendation: Watch** — a real operating beat obscured by both a non-cash GAAP charge and sector-wide selling isn't enough on its own to size a new position, especially with no live quote to confirm the current level. Risk: the CHIPS Act equity stake means Intel's reported GAAP earnings will stay volatile with the government's mark-to-market swings. Monitoring trigger: next quarter's Data Center & AI segment trajectory and any follow-through (or reversal) in the stock once sector selling calms.

#### Microchip Technology (MCHP, Nasdaq) — Impact: Medium — [Deal]
**What happened:** Microchip signed a definitive agreement on July 24 to acquire Hailo, an edge-AI processor, vision-processing, and robotics-chip maker with 100+ customers and a 10,000+-developer community. Terms were not disclosed; Microchip stated the deal is not expected to materially affect its financials, and it's expected to close near the end of the September quarter. [Microchip Technology Signs Definitive Agreement to Acquire Hailo (Microchip IR)](https://ir.microchip.com/news-events/press-releases/detail/1406/microchip-technology-signs-definitive-agreement-to-acquire-hailo)
**Market impact:** A real, filed deal, but explicitly sized by the acquirer itself as immaterial — a portfolio tuck-in for edge-AI/robotics exposure, not a transformational acquisition.
**Recommendation: Watch** — Microchip's own "not material" framing sets a low bar for market impact; there's nothing here that clears the Buy threshold. Risk: undisclosed terms make it impossible to judge whether this was a good price. Monitoring trigger: MCHP's next 10-Q for integration detail or a disclosed purchase price.

### Emerging Markets

#### China / broad EM tariff exposure (proxy: FXI, MCHI) — Impact: Medium-High
**What happened:** A new US tariff regime took effect at 12:01 a.m. ET on July 25, replacing an expiring 10% "global tariff." China's rate was set at 12.5%; the EU, Indonesia, and Mexico received 10%; the order covers roughly 99.4% of US imports across 60 trading partners, with the administration citing inadequate action on forced labor and signaling further "excess structural capacity" tariffs targeting China, the EU, and 16 other partners are still under investigation. [Trump announces next phase of global tariffs, affecting 99.4% of US imports (Yahoo Finance)](https://finance.yahoo.com/economy/policy/article/trump-announces-next-phase-of-global-tariffs-affecting-994-of-us-imports-210032314.html), [China Set to Look Past New Trump Tariffs Before Xi's US Trip (Bloomberg)](https://www.bloomberg.com/news/articles/2026-07-24/china-set-to-look-past-trump-s-new-tariffs-before-xi-visit-to-us)
**Market impact:** Shanghai Composite fell 0.6–1.2% and Shenzhen fell 0.6% on July 24; the PBOC moved to offset with a CNY 500B one-year MLF injection, on top of CNY 700B in reverse repos earlier this month. Bloomberg's reporting suggests markets are partly looking past the tariffs on hopes of a planned Xi–US visit.
**Positioning: Neutral** — the tariff headline is real and rate-quantified, but Beijing's monetary offset and de-escalation hopes ahead of a summit are already cushioning the reaction; this reads as a headwind to monitor, not yet a reason to underweight further. Risk: the pending "excess capacity" investigation could add a second, larger tariff round later this year. Monitoring trigger: outcome of the flagged capacity investigation and any Xi–Trump summit announcement.

# ₿ Cryptos
*Prices below are from search-indexed news snippets only — not fetched from crypto.com/Coinbase/Kraken directly, and not cross-checked across venues, due to the standing network block described above. Treat as directional color, not a tradable quote.*

## Market snapshot
| Asset | Price (USD, approx.) | 24h % | Sources agree? | Note |
|-------|-----------------------|-------|-----------------|------|
| BTC | mid-$60,000s (unverified) | ~-1.6% | Not cross-checked (feeds blocked) | ETF inflow streak snapped |
| ETH | ~$1,860–1,877 (unverified) | ~-2.9% | Not cross-checked (feeds blocked) | ETF inflow streak extends to 5 days |

### Bitcoin (BTC) — ETF inflow streak snaps; large options expiry
**What happened:** Spot Bitcoin ETFs recorded a combined $225M in net outflows on July 23, ending a 7-session streak that had pulled in roughly $999M — the streak this repo's `seen_catalysts` had tracked as a bullish signal through July 24. Separately, roughly 19,000 BTC in options (~$1.2B notional) expired July 24, a standard source of short-term volatility. [Bitcoin ETFs Shed $225M to Snap 7-Day Winning Streak, ETH ETFs Gain $26M (CryptoTimes)](https://www.cryptotimes.io/2026/07/24/bitcoin-etfs-shed-225m-to-snap-7-day-winning-streak-eth-etfs-gain-26m/), [Bitcoin price outlook: treasury sell-offs, Poolin bankruptcy and $1.2B options expiry (Invezz)](https://invezz.com/news/2026/07/24/bitcoin-price-outlook-treasury-sell-offs-poolin-bankruptcy-and-1-2b-options-expiry/)
**Price action:** Reported mid-$60,000s, roughly 1.6% below Thursday's open, amid a broader pullback in risk assets tied to higher Treasury yields on new tariff-driven inflation expectations (see EM section above). Not independently confirmed against exchange data this run.
**Read: Watch** — a single day's outflow ending a streak isn't a reversal signal on its own, and the move lines up with a macro (rates/tariff) story rather than a crypto-specific catalyst. Risk: without live exchange data this run, any read here carries extra uncertainty. Monitoring trigger: whether outflows continue into a second session, and restoration of exchange-API access for a verified mark.

### Ethereum (ETH) — ETF inflow streak extends to 5 days despite price pullback
**What happened:** Spot Ethereum ETFs added $26.32M on July 23, extending their inflow streak to five straight trading days even as spot ETH price fell. [Bitcoin ETFs Shed $225M to Snap 7-Day Winning Streak, ETH ETFs Gain $26M (CryptoTimes)](https://www.cryptotimes.io/2026/07/24/bitcoin-etfs-shed-225m-to-snap-7-day-winning-streak-eth-etfs-gain-26m/)
**Price action:** Reported to have opened around $1,876.92 on July 24 (-2.9% vs. Thursday's open) and traded down to roughly $1,860.78 intraday, per a single Yahoo Finance snippet — not independently confirmed against exchange data this run. [Bitcoin and ethereum prices today, Friday, July 24, 2026 (Yahoo Finance)](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-friday-july-24-2026-crypto-prices-retreat-on-higher-us-treasury-yields-152200068.html)
**Read: Watch** — flows and price are diverging (inflows continuing while price falls), which is worth tracking but isn't itself a directional catalyst. Risk: a macro-driven risk-off move (see tariffs/yields above) can overwhelm fund-flow signals short-term. Monitoring trigger: whether the inflow streak continues for a 6th session and whether price stabilizes once exchange data access is restored.

---
**Sources consulted:** WebSearch only (SEC EDGAR, ClinicalTrials.gov, FDA.gov, Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com APIs all blocked this session — 5th consecutive day, confirmed via `curl` and the repo's `fetch_quotes.py`). News and press cited inline: Yahoo Finance, Motley Fool, Bloomberg, CNN Business, TradingKey, 247wallst.com, CryptoTimes, Invezz, Microchip IR, GlobeNewswire.

*Informational only; not investment advice. Crypto is volatile and speculative. Verify independently before trading. Prices and figures in this briefing were not cross-checked against primary/exchange sources due to a standing network-policy block — treat with extra caution until structured-source access is restored. Generated ~05:04 ET, July 25, 2026.*

---

# Portfolio

## Snapshot
No live quotes were obtainable this run (see data-sourcing note above), so **no dollar-accurate account valuation is possible today** — same limitation as the prior four runs. Today is also a Saturday (market closed), so no fills would have occurred regardless. As of the last confirmed state (July 20 fills; unchanged since):
- Cash: $7,397.92
- Open positions at cost: DYN 63 sh @ $23.75 ($1,496.25) + HUT 11 sh @ $100.53 ($1,105.83) = $2,602.08 at cost
- Total account value at cost basis: $10,000.00 (unchanged from the $10,000 starting value; no realized gains/losses booked and no mark-to-market available)
- Benchmark: 13.4281 SPY shares at $744.71 cost ($10,000 equivalent at inception); no current SPY price available to compare.
- Return vs. $10,000 start and vs. SPY benchmark: **cannot be computed today** without a live quote — deferred until data access is restored.

## Open positions (ranked by cost basis; no live P&L available)
| Ticker | Shares | Avg cost | Current price | Unrealized P&L | Thesis status |
|--------|--------|----------|----------------|-----------------|---------------|
| HUT | 11 | $100.53 | Unavailable (quote feed blocked); unverified search snippet suggests ~$108 as of July 24 but is not used as an official mark | N/A | Intact — no new catalyst since the July 20 Beacon Point lease. |
| DYN | 63 | $23.75 | Unavailable (quote feed blocked); unverified search snippet suggests ~$23.21 but carries no confirmed date/time and is not used as an official mark | N/A | Watch (unchanged) — regulatory thesis intact; the now-larger $431.4M offering keeps closer scrutiny warranted than "intact." July 24/25 inducement-grant filing (routine new-hire equity awards under Nasdaq Rule 5635(c)(4)) is not material and is not a new catalyst. |

## Today's trades
**No trades today.** Markets are closed (Saturday), so no fills were possible regardless of findings. Separately, no reliable machine-readable quote existed for any ticker today (equities or crypto) — the same 403 policy block that has affected every run since July 21 persisted. Nothing found this window cleared the Buy bar on its own merits either (MU, SNDK, INTC, and MCHP were all rated Watch, not Buy). DYN and HUT were held unchanged.

## Realized P&L to date
$0.00 realized (no positions have been closed). Combined realized + unrealized total cannot be computed today without a live mark, but stands at $0.00 realized plus an unknown unrealized figure pending restored data access.

## Watchlist changes
**Refreshed** (new information, added-date and expiry reset to today, now expiring 2026-08-07): **MU** — the July 23 hyperscaler-capex/NAND-shortage bull case was directly contradicted a day later by SanDisk's own guidance and a same-day ~8% drop; the thesis is now a live conflict, not a one-sided bull case.

**Added** (expiring 2026-08-07): **MCHP** — definitive agreement to acquire edge-AI chipmaker Hailo; company itself frames the deal as immaterial to financials, so this is tracked rather than sized.

No new EM ticker was added to the watchlist — the tariff story (FXI/MCHI proxy) is a macro/positioning read rather than a single-name catalyst, and is covered in the Stocks section above rather than as a watchlist line.

The remaining fourteen names carried over from July 20–24 (JSPR, TEM, PSNL, KLRS, ONCY, RGNX, BLTE, GLSI, RKLB, ACAD, ARWR, NBIS, AMD, BMNR) are unchanged; none have expired (earliest expiry is 2026-08-03).

## Administrative notes
- `reports/unsent-2026-07-24.md` was found in the repo (yesterday's briefing was drafted but never actually sent, for the same reasons noted below). It has been renamed to `reports/morning-research-2026-07-24.md` in today's commit per the standing procedure, flagged here exactly once.
- **This is the fifth consecutive run** in which (a) the session's network egress policy blocks every structured data source (SEC EDGAR, ClinicalTrials.gov, FDA.gov, Yahoo Finance, all three crypto exchange APIs) with a 403, confirmed independently via curl, the proxy status endpoint, and the repo's own `fetch_quotes.py`, and (b) the Gmail connector available to this session exposes only draft creation with no send capability, meaning every run's report ends up as an unsent draft rather than delivered mail. Neither issue is a one-off; both are standing configuration gaps at the account/environment level — restoring egress access to market-data and filing endpoints, and granting the Gmail connector send scope, remain outstanding, since the paper-trading simulation has not executed a single fill or delivered a single email since it opened on July 20.

```PORTFOLIO_STATE
{
  "version": 1,
  "initialized_at": "2026-07-20T10:50:30-04:00",
  "last_run": "2026-07-25",
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
    }
  ]
}
```
