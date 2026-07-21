# Morning Investment Research — Tuesday, July 21, 2026
*Window covered: Monday, July 20, 2026 00:00 ET – Tuesday, July 21, 2026 ~05:00 ET*

**Data-sourcing note (read before the rest):** every structured, machine-readable source this briefing normally relies on was unreachable this run — SEC EDGAR full-text search, `data.sec.gov`, ClinicalTrials.gov, bioRxiv/medRxiv, arXiv, the Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com/CoinGecko exchange APIs all returned a blanket `403 Forbidden` from this session's network egress policy, confirmed independently via direct `curl`, via `WebFetch` (which failed even on a plain control URL), and via the repo's own quote-fetch script. This is a policy-level block on this session, not a site-by-site outage. `WebSearch` was the only working tool, so every item below is sourced from search-result snippets and links rather than a fetched primary filing — weaker verification than a normal run. No equity or crypto price could be pulled from a live exchange/API feed at all, which also means **no fills or price-based portfolio marks were possible today** (see Portfolio section). Tickers below are cross-referenced against snippet text and press-release/IR domains, not against `data.sec.gov`'s listing arrays.

# 📈 Stocks

## Summary
| Ticker | Name | Theme | Headline | Impact | Rec |
|--------|------|-------|----------|--------|-----|
| LXP | LXP Industrial Trust | Deals | Brookfield & CPP Investments to acquire for $5.2B cash | High | Hold/Watch |
| MGY | Magnolia Oil & Gas | Deals | To acquire WildFire Energy for ~$4.06B | High | Watch |
| ZWS | Zurn Elkay Water Solutions | Deals | To acquire Intellihot for $320M cash | Medium | Watch |
| SNBR | Sleep Number Corp | Deals | Chapter 11 asset sale to Sleep Country Canada court-approved | Medium | Avoid |
| AMD | Advanced Micro Devices | Technology, AI & Quantum | Microsoft to deploy AMD's Helios AI racks on Azure | Medium | Watch |
| ASTS | AST SpaceMobile | Space | $1B convertible notes close; satellite deployment slips to early 2027 | Low | Avoid |
| BLTE | Belite Bio | Medical | New secondary-endpoint data for tinlarebant (Stargardt) at ASRS | Medium | Watch |
| GLSI | Greenwich LifeSciences | Medical | Preliminary FLAMINGO-01 open-label data; DSMB continues trial | Medium | Watch |
| — | China A-shares (FXI/MCHI/KWEB proxies) | Emerging Markets | State "national team" funds intervene after a ~25% STAR Market drop | Medium-High | Positioning: Neutral |

### Deals

#### LXP Industrial Trust (LXP, NYSE) — Impact: High
**What happened:** Brookfield Asset Management and CPP Investments agreed to acquire LXP Industrial Trust, a 108-property, ~53M-square-foot industrial REIT, in an all-cash deal valued near $5.2B including assumed debt and preferred equity. Holders get $61.20/share, a 12% premium to the 30-day volume-weighted average price. Announced July 20, 2026; expected to close Q4 2026, at which point LXP delists from NYSE. [CPP Investments](https://www.cppinvestments.com/newsroom/brookfield-and-cpp-investments-to-acquire-lxp-industrial-trust-in-5-2-billion-all-cash-transaction/), [GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/20/3329572/19004/en/Brookfield-and-CPP-Investments-to-Acquire-LXP-Industrial-Trust-in-5-2-Billion-All-Cash-Transaction.html)
**Market impact:** A definitive cash buyout caps both downside and upside near the deal price; the stock should now trade at a small discount to $61.20 reflecting deal-close risk and time value.
**Recommendation: Hold/Watch** — this is a merger-arb situation, not a growth thesis: existing holders have little to do but wait for close, and new money faces a thin spread for the risk taken. Risk: HSR clearance or a financing hiccup could delay or break the deal. Monitoring trigger: HSR clearance and the expected Q4 2026 close.

#### Magnolia Oil & Gas (MGY, NYSE) — Impact: High
**What happened:** Magnolia agreed to acquire all of WildFire Intermediate Holdings for roughly $4.06B — $2.65B cash, 32.2M Class A shares, and assumption of $600M in senior notes — adding about 810,000 net acres and making Magnolia the leading Eagle Ford/Austin Chalk operator, with pro forma production near 159,000 boe/d. Announced July 20, 2026, subject to HSR clearance and financing. [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-20/magnolia-oil-agrees-to-buy-wildfire-energy-in-4-1-billion-deal), [Magnolia IR](https://www.magnoliaoilgas.com/investors/press-releases/year/2026/07-20-2026-120106731)
**Market impact:** Roughly doubles Magnolia's core acreage — a scale-defining move if integration goes cleanly, but funded partly with new shares and assumed debt.
**Recommendation: Watch** — the acreage add is real and strategically logical, but dilution from the new share issuance and the assumed $600M note load mean the deal's accretiveness isn't yet proven. Risk: integration execution and leverage post-close. Monitoring trigger: HSR clearance and management's first disclosed pro forma leverage/accretion figures, likely on the next earnings call.

#### Zurn Elkay Water Solutions (ZWS, NYSE) — Impact: Medium
**What happened:** Zurn Elkay signed a definitive agreement to acquire Intellihot, a tankless water-heater maker (~$37M in 2026 net sales), for about $320M cash. Announced July 20, 2026; expected to close early Q3 2026. [StockTitan](https://www.stocktitan.net/sec-filings/ZWS/8-k-zurn-elkay-water-solutions-corp-reports-material-event-ac19c57c57b7.html), [Morningstar/Business Wire](https://www.morningstar.com/news/business-wire/20260720021781/zurn-elkay-water-solutions-corporation-to-acquire-intellihot)
**Market impact:** Small relative to Zurn Elkay's size — a bolt-on into an adjacent product category rather than a scale event.
**Recommendation: Watch** — the strategic logic (cross-sell into existing plumbing/water channels) is sound but the payoff is a margin/synergy story that won't show up until integration. Risk: purchase-price multiple looks full for a $37M-revenue business absent disclosed synergy targets. Monitoring trigger: close (early Q3 2026) and any synergy guidance on the next call.

#### Sleep Number Corp (SNBR, Nasdaq) — Impact: Medium
**What happened:** A U.S. bankruptcy court approved Sleep Country Canada's winning bid, worth about $701M in total value ($529.5M cash plus assumed obligations), for substantially all of Sleep Number's assets via Chapter 11 auction. Approved July 20, 2026; close expected by July 31. [Business Wire](https://www.businesswire.com/news/home/20260720463784/en/Sleep-Number-Receives-Court-Approval-for-Sale-to-Sleep-Country-Canada), [Sleep Number IR](https://ir.sleepnumber.com/news/news-details/2026/Sleep-Number-Receives-Court-Approval-for-Sale-to-Sleep-Country-Canada/default.aspx)
**Market impact:** This is a distressed Chapter 11 asset sale, not a going-concern buyout — sale proceeds are earmarked for creditors under the bankruptcy waterfall, not common equity.
**Recommendation: Avoid** — common shareholders in a Chapter 11 asset sale typically see minimal to no recovery once creditors are paid; there's little reason for new money here. Risk: any residual equity value depends entirely on the final distribution order. Monitoring trigger: the court's final distribution/plan confirmation and the expected July 31 close.

### Technology, AI & Quantum

#### Advanced Micro Devices (AMD, Nasdaq) — Impact: Medium
**What happened:** AMD and Microsoft announced an expanded partnership spanning AMD GPUs, CPUs, and Pensando networking on Azure. Microsoft will deploy AMD's new "Helios" rack-scale AI system — AMD's first true rack-level answer to Nvidia's NVL72 — for frontier-model inference on Azure, with shipments beginning H2 2026. Announced July 20, 2026; AMD closed up roughly 1.6–2% that day and added another ~4.5% in July 21 premarket trading. [CNBC](https://www.cnbc.com/2026/07/20/amd-helios-microsoft-ai-nvidia.html), [SiliconANGLE](https://siliconangle.com/2026/07/20/microsoft-will-use-amds-ai-optimized-helios-racks-azure/), [HPCwire](https://www.hpcwire.com/off-the-wire/amd-expands-microsoft-partnership-with-helios-epyc-and-pensando/)
**Market impact:** A credible flagship-customer win for AMD's rack-scale AI hardware, validating the strategy against Nvidia at the data-center level.
**Recommendation: Watch** — real validation, but Nvidia still holds the dominant share of AI-accelerator spend, and the premarket pop may already reflect the good news. Risk: Helios shipment volumes and Azure's actual purchase commitments are not yet disclosed in dollar terms. Monitoring trigger: H2 2026 shipment cadence and any revenue disclosure tied to the partnership.

**Quantum computing — sector note, no rated entry:** A Simons Foundation/Boston University team reproduced, using classical tensor-network compression on ordinary hardware, results from a quantum dynamics problem previously said to require a quantum computer — reported via ScienceDaily around July 19–21, 2026 (the underlying work traces to a May 2026 Simons Foundation release). [ScienceDaily](https://www.sciencedaily.com/releases/2026/07/260719040000.htm) This doesn't name a specific listed beneficiary; it's a mild sentiment headwind for the quantum-computing group (IonQ, Rigetti, D-Wave, Quantum Computing Inc.) rather than a company-specific catalyst, so it gets a mention but no Buy/Hold/Watch call.

### Space

#### AST SpaceMobile (ASTS, Nasdaq) — Impact: Low
**What happened:** AST SpaceMobile closed a $1.0B private offering of 1.625% convertible senior notes due 2034 to fund its space-based cellular broadband buildout. Coverage tied the raise to a timeline slip: BlueBird satellite deployment (~45 satellites) is now targeted for early 2027, versus the prior end-of-2026 goal. Announced July 20, 2026; shares fell about 2.1% on the day. [TipRanks](https://www.tipranks.com/news/company-announcements/ast-spacemobile-completes-1b-convertible-notes-financing), [ts2.tech](https://ts2.tech/en/ast-spacemobile-shares-dip-after-1-billion-fundraise-highlights-possible-launch-postponement/)
**Recommendation: Avoid** (for new money) — dilutive financing paired with a real schedule slip is an incremental negative for a stock whose bull case leans on hitting deployment milestones. Risk: further delay or additional dilutive raises. Monitoring trigger: a confirmed SpaceX launch manifest update and Q3 2026 deployment progress.

**Not rated — scheduled, not yet occurred:** Northrop Grumman's DARPA/Naval Research Laboratory Mission Robotic Vehicle, billed as the first U.S. multi-mission satellite-servicing spacecraft in geosynchronous orbit, has a launch window later today (~10:15am ET) on a SpaceX Falcon 9. As of this report it hasn't flown yet, so per this briefing's own discipline (expected ≠ occurred) it isn't rated — flagging only as something to watch for confirmation in a future run if it flies successfully. [Aerospace America](https://aerospaceamerica.aiaa.org/joint-darpa-northrop-robotic-servicing-spacecraft-to-launch-in-late-july/)

### Medical

#### Belite Bio (BLTE, Nasdaq) — Impact: Medium
**What happened:** Belite Bio presented additional positive secondary-endpoint data from the Phase 3 DRAGON trial of tinlarebant in Stargardt disease type 1 at the ASRS 2026 Annual Meeting: a bisretinoid/autofluorescence marker was stable (~2% decrease) at month 25 in treated patients versus ~20% increase on placebo, building on the previously reported 35.7% reduction in retinal lesion growth. The company has already completed its NDA submission to the FDA. Announced July 20, 2026. [GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/20/3329667/0/en/Belite-Bio-Announces-Oral-Presentation-at-the-ASRS-Annual-Meeting-Featuring-Additional-Positive-Secondary-Endpoint-Data-from-the-Phase-3-Trial-of-Tinlarebant-in-Stargardt-Disease-T.html)
**Recommendation: Watch** — this corroborates an already-reported primary-endpoint win rather than breaking new ground, and with the NDA already filed the market has had time to price the base case. Risk: secondary-endpoint durability doesn't guarantee an approval decision. Monitoring trigger: FDA's NDA acceptance and PDUFA-date assignment.

#### Greenwich LifeSciences (GLSI, Nasdaq) — Impact: Medium
**What happened:** Greenwich LifeSciences gave a clinical update on its FLAMINGO-01 Phase III trial (GLSI-100 to prevent breast cancer recurrence). The DSMB recommended the study continue without modification. In the fully enrolled, 250-patient, open-label, non-HLA-A*02 arm, a preliminary analysis showed roughly a 70–80% reduction in recurrence rate — data the company itself explicitly flags as early and immature. Announced July 20, 2026. [GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/20/3329545/0/en/Greenwich-LifeSciences-Provides-Clinical-Updates-on-FLAMINGO-01.html)
**Recommendation: Watch** — a real DSMB continuation is a genuine positive procedural signal, but the efficacy figure comes from a single-arm, open-label analysis the company describes as immature, not a controlled readout. Risk: the effect could shrink materially as data mature or in the randomized comparator arms. Monitoring trigger: the next scheduled DSMB review and maturing comparator data.

### Emerging Markets

#### China A-shares / FXI, MCHI, KWEB proxies — Impact: Medium-High
**What happened:** China Reform Holdings Corp and China Chengtong Holdings Group, the country's "national team" state funds, deployed an estimated ¥50–60B (roughly $7.4–8.9B) into equities and ETFs around July 19–20, 2026, after the STAR Market had fallen about 25% and wiped out more than ¥4 trillion in value. The Shanghai Composite closed +0.85% to 3,796.3 on July 20; the Shenzhen Component was -0.71%. Alibaba (BABA, NYSE) rose as much as 5.7% intraday July 20 as part of the same rally. [Caixin Global](https://www.caixinglobal.com/2026-07-20/china-deploys-national-team-in-multi-pronged-stock-market-rescue-102466182.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-20/china-steps-up-efforts-to-stabilize-its-sagging-stock-market)
**Positioning: Neutral** — state intervention provides near-term price support and sentiment relief, but a liquidity backstop doesn't resolve whatever drove a 25% STAR Market decline in the first place. Watch whether the rally holds once state buying tapers, and whether it shows up as real inflows into FXI/MCHI/KWEB rather than a one-day bounce.

---

# ₿ Cryptos
*Prices below are WebSearch-derived from press recaps, not a direct exchange API read — Coinbase, Kraken, crypto.com, and CoinGecko were all unreachable this run (see Data-sourcing note at top). Treat these as approximate. As of ~05:00 ET, July 21, 2026.*

## Market snapshot
| Asset | Price (USD, approx.) | 24h % | Sources agree? | Note |
|-------|-----------------------|-------|-----------------|------|
| BTC | ~$64,700 (range $63,700–$65,400 across sources) | roughly flat to +0.9% | Partial — 3+ press sources in the same range, not exact-matching | Fear & Greed Index fell 29→25 despite the price being up |
| ETH | ~$1,880 (range $1,850–$1,910) | +0.3% to +1% | Partial — 3 sources in range | Whales opening leveraged longs eyeing $2,000 |
| SOL | ~$77.8 | +1.8% | 2 sources agree | — |
| XRP | ~$1.11 | +1.5% | Single source only, not cross-checked | Lower confidence |

### Bitcoin (BTC) — ETF-flow rotation continues, sentiment lags price
**What happened:** Spot bitcoin ETFs logged a second straight week of net inflows (+$75.7M for the week ended July 17, after +$197.4M the prior week), following an eight-week, roughly $8.2B outflow streak earlier in the summer; 2026 net flows are still negative overall (about -$5.2B year-to-date as of mid-July). [Cryptonomist](https://en.cryptonomist.ch/2026/07/09/crypto-etf-flows-rotation/), [Roic.ai](https://www.roic.ai/news/crypto-etf-outflows-extend-into-july-as-bitcoin-ether-see-sustained-withdrawals-07-01-2026)
**Price action:** BTC traded in the roughly $63,700–$65,400 range across the window, a mild net gain, after an intraday dip to about $63,692 tied to Middle East-linked risk-off sentiment. Notably, the Fear & Greed Index worsened from 29 ("Fear") to 25 ("Extreme Fear") even as price ticked up — a sentiment/price divergence worth flagging rather than a clean signal either way.
**Read: Watch** — the outflow streak easing is a mildly constructive data point, but it's a multi-week trend, not a single decisive event, and the sentiment/price divergence argues against reading too much into the modest gain. Risk: renewed geopolitical risk-off flow reversed the ETF trend once already this summer. Monitoring trigger: whether ETF inflows extend to a third consecutive week.

### Ethereum (ETH) — institutional rotation from BTC into ETH ETFs
**What happened:** Ether ETFs have been drawing rotation money out of bitcoin funds, with inflow figures around $105M and $70.5M cited near mid-to-late July, led by BlackRock's ETHA and Fidelity's FETH. Separately, on-chain data shows whales opening about 12,000 ETH of 20x-leveraged long positions, targeting the $2,000 level. [Cryptonews](https://cryptonews.com/news/ethereum-news-etf-inflows-blackrock-etha-reversal/), [The Coin Republic](https://www.thecoinrepublic.com/2026/07/20/ethereum-price-reclaims-1850-as-whale-longs-eye-2000-rally/)
**Price action:** ETH traded roughly $1,850–$1,910 across the window, reclaiming the $1,850 level.
**Read: Watch** — the ETF rotation narrative is a real, if gradual, institutional-flow story, and a modest price gain is consistent with it, but the heavily leveraged whale positioning adds two-sided risk (a fast unwind is as plausible as a breakout) rather than confirming a trend. Monitoring trigger: whether ETH clears $2,000 on rising volume, or the leveraged longs get unwound first.

**Sector risk note (not BTC/ETH-specific):** Two protocol-level security incidents fell inside the window — Ostium, a perpetuals/derivatives protocol, lost about $23.75M on July 20 to an off-chain oracle price-feed manipulation attack (trader collateral reportedly unaffected) [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-steal-237-million-in-crypto-from-ostium-in-off-chain-attack/); and the Wanchain Cardano↔BNB Chain bridge was exploited on July 21 for roughly $10M in NIGHT tokens via a signature-reuse bug [CryptoTimes](https://www.cryptotimes.io/2026/07/21/wanchain-cardano-bridge-exploited-hackers-stole-10m-in-night-tokens/). Neither is systemic, but they're a reminder that DeFi/bridge security risk is ongoing background risk for the space generally.

---
**Sources consulted:** WebSearch only (see Data-sourcing note at top for why). EDGAR 8-K/6-K full-text search, `data.sec.gov`, ClinicalTrials.gov, bioRxiv/medRxiv, FDA press listings, arXiv, NASA/DoD contract pages, and Coinbase/Kraken/crypto.com/CoinGecko exchange APIs were all attempted first and were unreachable (blanket 403 from this session's network policy) — none of this run's findings could be cross-checked against those primary feeds.
*Informational only; not investment advice. Crypto is volatile and speculative. Verify independently before trading. This is a paper-trading simulation; no real money is involved. Generated ~05:00 ET, July 21, 2026.*

---

# Portfolio

## Snapshot
**Live marks were not available this run** — every equity and crypto quote source (Yahoo Finance chart API, Coinbase, Kraken, crypto.com) returned the same network-policy 403 described above, and the repo's `fetch_quotes.py` confirmed the same failure across every symbol. That means today's total account value, percent invested at market, and return versus SPY **cannot be computed today** and are not shown below to avoid presenting a guessed number as real. What's known with certainty from the ledger:

- Cash: $7,397.92
- Cost basis of open positions: $2,602.08 (DYN $1,496.25 + HUT $1,105.83)
- Cash + cost basis: $10,000.00 (matches the account's starting value; no realized gains/losses yet)
- Percent invested at cost: ~26.0%
- SPY benchmark: 13.4281 shares at $744.71 cost (July 20, 2026) — mark unavailable today for the same reason

## Open positions (cost basis; current price/unrealized P&L unavailable this run)
| Ticker | Shares | Avg cost | Cost basis | Thesis status |
|--------|--------|----------|------------|----------------|
| DYN | 63 | $23.75 | $1,496.25 | Intact — no new information found today; yesterday's search reconfirmed the same BLA/Priority Review details, nothing that changes the thesis |
| HUT | 11 | $100.53 | $1,105.83 | Intact — no company-specific news found today; broader AI-datacenter-leasing theme (adjacent to today's AMD/Microsoft item) continues to look supportive, but that's context, not a direct catalyst |

Stop/target levels could not be checked against a live price this run (DYN stop $19.00/target $32.00; HUT stop $82.00/target $125.00) — this is a real gap in today's risk monitoring, not a silent skip; it's called out here explicitly and should self-correct once quotes are reachable again.

## Today's trades
**No trades today.** Every quote source — equity and crypto alike — was unreachable due to the network-policy block described above, so no reliable machine-readable fill price existed for any candidate, including the higher-conviction items above (LXP, MGY, AMD, BLTE, GLSI). Per the execution rules, nothing gets bought without a real quote, regardless of conviction, so no new positions were opened today.

## Realized / unrealized P&L
- Realized P&L to date: $0.00 (no positions have been closed)
- Unrealized P&L: not computable today (no live marks); nothing to add to the realized figure this run
- Combined realized + unrealized: $0.00 known, with an unknown unrealized component pending the next run with working quotes

## Watchlist changes
Added three names from today's research that would otherwise have been actionable but couldn't be filled (see above): AMD (Watch grade — Microsoft/Helios partnership), BLTE (Watch grade — Stargardt secondary-endpoint data), and GLSI (Watch grade — FLAMINGO-01 preliminary data). The seven names carried over from July 20 (JSPR, TEM, PSNL, KLRS, ONCY, RGNX, BMNR) are unchanged and not yet expired (expire August 3, 2026). LXP, MGY, ZWS, and SNBR were deliberately **not** added to the watchlist — they're M&A/bankruptcy situations (merger arb, a dilutive bolt-on, and a distressed-asset sale) that don't fit this account's catalyst-driven growth mandate as a "graduate to a position later" candidate; they're informational in the briefing above only.

## Administrative notes
- `reports/unsent-2026-07-20.md` was found in the repo (yesterday's briefing was drafted but never actually sent — see below). It has been renamed to `reports/morning-research-2026-07-20.md` in today's commit per the standing procedure, flagged here exactly once.
- The Gmail connector available to this session exposes only `create_draft` — there is no send tool. This means every run's email ends up as a draft only, not delivered, which is very likely why yesterday's report was also left unsent. This is a standing configuration gap, not a one-off failure, and is worth fixing (grant the Gmail connector send scope) so future briefings actually land in the inbox rather than sitting as drafts.

```PORTFOLIO_STATE
{
  "version": 1,
  "initialized_at": "2026-07-20T10:50:30-04:00",
  "last_run": "2026-07-21",
  "cash": 7397.92,
  "positions": [
    {
      "ticker": "DYN",
      "shares": 63,
      "avg_cost": 23.75,
      "entry_date": "2026-07-20",
      "stop": 19.00,
      "target": 32.00,
      "thesis": "FDA accepted BLA for z-rostudirsen (DMD, exon 51) with Priority Review, PDUFA Jan 21 2027; muted same-day reaction leaves room if the regulatory path holds.",
      "status": "intact"
    },
    {
      "ticker": "HUT",
      "shares": 11,
      "avg_cost": 100.53,
      "entry_date": "2026-07-20",
      "stop": 82.00,
      "target": 125.00,
      "thesis": "Signed $9.8B, 15-year lease fully commercializes 1GW Beacon Point AI campus with an investment-grade tenant, accelerating the pivot from BTC mining to AI infra leasing.",
      "status": "intact"
    }
  ],
  "realized_pnl": 0.00,
  "benchmark": {
    "spy_shares": 13.4281,
    "spy_cost": 744.71,
    "quote_ts": "2026-07-20T10:50:30-04:00"
  },
  "watchlist": [
    { "ticker": "JSPR", "reason": "Reverse merger with Kira Pharmaceuticals closed + $132M PIPE; stock fell 11% on close, stockholder vote on preferred conversion still pending", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "TEM", "reason": "Definitive deal to acquire Personalis (~$1.5B, floating stock ratio); TEM fell 9% on announcement", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "PSNL", "reason": "Being acquired by Tempus at nominal $16.25/sh but trading well below that on deal-closing risk and floating ratio", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "KLRS", "reason": "Positive expanded Phase 1a nAMD durability data but stock fell 5%; watch for Phase 2 initiation", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "ONCY", "reason": "FDA Fast Track for pelareorep combo in anal SCC; designation only, no efficacy data yet", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "RGNX", "reason": "$107.8M follow-on priced at $9.00/sh, stock up 5.6% on the raise; watch pipeline deployment of proceeds", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "BMNR", "reason": "Routine ETH treasury update ($11.5B total holdings, 4.8% of ETH supply); leveraged proxy on ETH price", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "AMD", "reason": "Expanded Microsoft/Azure deal to deploy AMD's rack-scale Helios AI system; flagship customer validates rack-level competition with Nvidia, +4.5% premarket", "added": "2026-07-21", "expires": "2026-08-04" },
    { "ticker": "BLTE", "reason": "New Phase 3 DRAGON secondary-endpoint data for tinlarebant in Stargardt disease at ASRS; NDA already submitted to FDA", "added": "2026-07-21", "expires": "2026-08-04" },
    { "ticker": "GLSI", "reason": "Preliminary FLAMINGO-01 open-label arm data (~70-80% recurrence reduction, company-flagged as immature); DSMB recommended trial continue unmodified", "added": "2026-07-21", "expires": "2026-08-04" }
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
    { "key": "ETH:2026-07-21:etf-inflow-rotation", "noted": "2026-07-21" }
  ]
}
```
