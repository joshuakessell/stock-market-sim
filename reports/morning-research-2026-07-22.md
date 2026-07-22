# Morning Investment Research — Wednesday, July 22, 2026
*Window covered: Tuesday, July 21, 2026 00:00 ET – Wednesday, July 22, 2026 ~05:00 ET*

**Data-sourcing note (read before the rest):** for the second run in a row, every structured, machine-readable source this briefing normally relies on was unreachable — SEC EDGAR, `data.sec.gov`, ClinicalTrials.gov, the Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com APIs all returned a `403 Forbidden` from this session's network egress policy, confirmed via direct `curl`, via `WebFetch` (which failed even on a plain control fetch), and via the repo's own `fetch_quotes.py`. This is a session-level policy block, not a site outage — see the administrative note at the end of this report. `WebSearch` was the only working tool, so every item below is sourced from search-result snippets and article text rather than a fetched primary filing. That also means **no live price quote could be pulled for any equity or crypto asset, so no fills or price-based marks were possible today** (see Portfolio section).

# 📈 Stocks

## Summary
| Ticker | Name | Theme | Headline | Impact | Rec |
|--------|------|-------|----------|--------|-----|
| DYN | Dyne Therapeutics | Medical *(held position)* | Upsized $375M stock offering priced at $20.50/sh, below our cost basis | Medium | Watch |
| RGNX | Regenxbio | Medical *(watchlist)* | $100M offering priced at $9.00; sources disagree on stock reaction | Medium | Watch |
| ACAD | Acadia Pharmaceuticals | Medical | FDA Fast Track for remlifanserin in Alzheimer's-disease psychosis | Medium | Watch |
| NBIS | Nebius Group | Technology, AI & Quantum | Nvidia takes 9.3% stake (~$5B) plus $2B AI-infra investment | High | Watch |
| MU | Micron Technology | Technology, AI & Quantum | +12% on bullish BofA note amid an AI-memory chip rally | Medium | Watch |
| AMD | Advanced Micro Devices | Technology, AI & Quantum *(watchlist)* | Analyst price-target hikes follow Microsoft/Helios deal; investor event today | High | Watch |
| RKLB | Rocket Lab | Space | $266M Space Force suborbital-launch contract | High | Watch |
| GM | General Motors | Deals & Earnings | Q2 beat, FY2026 guidance raised | Medium | Hold/Watch |
| TEM / PSNL | Tempus AI / Personalis | Deals *(watchlist)* | Routine shareholder-rights investigation opened on the pending acquisition | Low | Watch (unchanged) |
| COIN / HOOD / BLSH | Coinbase / Robinhood / Bullish | Deals *(crypto-linked equities)* | Rallied on CLARITY Act ethics-deal progress in the Senate | Medium | Watch |
| — | China A-shares (FXI / KWEB proxies) | Emerging Markets | State "national team" funds poured a record ~$8.9B into equities/ETFs | Medium-High | Positioning: Neutral |
| — | South Korea (EWY) | ETFs & Fund Flows | Record ETF inflow as investors proxy-trade the SK Hynix Nasdaq listing | Medium | Positioning: Neutral |

### Medical

#### Dyne Therapeutics (DYN, Nasdaq) — Impact: Medium — *held position, see Portfolio section*
**What happened:** Two days after FDA accepted the BLA for z-rostudirsen with Priority Review (already noted July 20), Dyne priced an upsized public offering of 18.3M shares at $20.50, raising roughly $375.15M. [StockTitan](https://www.stocktitan.net/news/DYN/dyne-therapeutics-announces-pricing-of-upsized-375-million-public-zqqq2yd68adm.html), [GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/20/3329635/0/en/Dyne-Therapeutics-Announces-U-S-FDA-Acceptance-of-Biologics-License-Application-BLA-for-Z-Rostudirsen-in-Exon-51-Duchenne-Muscular-Dystrophy-DMD.html)
**Market impact:** A $20.50 offering price sits below our $23.75 cost basis and only about $1.50 above our $19.00 stop — routine biotech runway-funding, not a change to the regulatory thesis, but it puts the position closer to the stop than the BLA news alone would suggest.
**Recommendation: Watch** — the Priority Review/PDUFA thesis is unaffected by the raise, but the dilution and implied price level warrant closer tracking than "intact." Risk: further financings or a soft print could test the stop before the January 2027 PDUFA date arrives. Monitoring trigger: a confirmed live quote against the $19.00 stop, and any further capital-raise activity.

#### Regenxbio (RGNX, Nasdaq) — Impact: Medium — *on watchlist since July 20*
**What happened:** Regenxbio priced a $100M underwritten offering (10,003,889 shares plus pre-funded warrants) at $9.00/share on July 20. Our July 20 watchlist note recorded the stock as *up* 5.6% on the raise; today's research independently found reporting that the stock *fell* roughly 11.7% on the pricing. [StockTitan](https://www.stocktitan.net/news/RGNX/regenxbio-announces-pricing-of-public-offering-of-common-stock-and-cy9ot2ihb5dz.html)
**Market impact:** flagging the conflict rather than averaging it — this may reflect two different reaction windows (announcement vs. pricing) rather than one number being simply wrong, but it isn't resolved.
**Recommendation: Watch** — hold the existing watchlist entry, but don't treat either reaction figure as reliable until a live quote confirms which one holds. Risk: unclear price action means real cost-basis risk if this graduates to a position later. Monitoring trigger: a confirmed live quote once data access is restored.

#### Acadia Pharmaceuticals (ACAD, Nasdaq) — Impact: Medium
**What happened:** FDA granted Fast Track designation to remlifanserin for hallucinations and delusions associated with Alzheimer's disease psychosis; the Phase 2 RADIANT trial has completed enrollment, with topline data expected September–October 2026. [BusinessWire](https://www.businesswire.com/news/home/20260720458854/en/Acadia-Pharmaceuticals-Receives-FDA-Fast-Track-Designation-for-Remlifanserin-in-Alzheimers-Disease-Psychosis)
**Recommendation: Watch** — a designation alone doesn't carry efficacy data, and the market has seen Fast Track headlines before. Risk: the September–October readout could go either way and Fast Track doesn't predict it. Monitoring trigger: the RADIANT topline data.

### Technology, AI & Quantum

#### Nebius Group (NBIS, Nasdaq) — Impact: High
**What happened:** Nvidia disclosed a 9.3% equity stake in Nebius (~22.26M shares/warrants, roughly $5B) alongside a planned $2B investment for AI-infrastructure collaboration; separately, Nebius signed a compute deal worth more than $1B with Reflection AI running through 2029. Stock rose 18.78% July 21. [GuruFocus](https://www.gurufocus.com/news/8968475/nebius-nbis-shares-surge-as-nvidia-nvda-acquires-stake), [Fool.com](https://www.fool.com/investing/2026/07/21/why-nebius-stock-soared-today/)
**Recommendation: Watch** — a strategic stake from Nvidia is a real, high-conviction validation of Nebius's neocloud positioning, not just sentiment, but the ~19% pop likely already prices in much of the news. Risk: neocloud capacity economics remain unproven at scale. Monitoring trigger: disclosed terms of the $2B investment and early utilization data from the Reflection AI contract.

#### Micron Technology (MU, Nasdaq) — Impact: Medium
**What happened:** Micron rose 12% July 21 on a bullish Bank of America note (Buy, $1,550 price target) plus a broader memory/semiconductor rally tied to AI-driven memory demand and strong South Korea chip-export data. [Invezz](https://invezz.com/news/2026/07/21/micron-stock-jumps-12-what-is-driving-the-memory-stock-today/), [Seeking Alpha](https://seekingalpha.com/news/4616000-micron-jumps-12-on-bofa-note-chip-rally)
**Market impact:** this move is analyst- and sector-sentiment driven rather than a company-specific event (no earnings, no product news) — real, but a notch weaker as a standalone catalyst.
**Recommendation: Watch** — the AI-memory demand thesis behind the move is fundamentally real, but a single analyst note is thin support for a 12% day. Risk: the move could unwind on any disappointing read-through from upcoming semiconductor earnings. Monitoring trigger: Micron's next quarterly print and any confirming or conflicting analyst revisions.

#### Advanced Micro Devices (AMD, Nasdaq) — Impact: High — *on watchlist since July 21*
**What happened:** Following Monday's Microsoft/Helios partnership news, AMD rose another 8.1% July 21 to $544.43 on analyst upgrades (Rosenblatt to $655 from $490; UBS to $700 and a 2027 revenue estimate of $83.4B). AMD's "Advancing AI 2026" event runs today and tomorrow (July 22–23). [Fool.com](https://www.fool.com/investing/2026/07/21/why-amd-stock-jumped-today/)
**Recommendation: Watch** — real follow-through confirms the thesis, but the stock is already up sharply on cumulative good news heading into today's event; no live quote was available to evaluate a fill today. Risk: the event could be a "sell the news" moment if it doesn't add materially new information. Monitoring trigger: outcomes disclosed at the Advancing AI 2026 event and a confirmed live quote for sizing.

### Space

#### Rocket Lab (RKLB, Nasdaq) — Impact: High
**What happened:** The U.S. Space Force awarded Rocket Lab a $266M firm-fixed-price contract for 12 (plus 6 optional) suborbital launches from the Pacific Spaceport Complex, Alaska, running through December 2028, with $112M obligated at award. Announced July 21; shares rose 6–9% after hours. [Investing.com](https://www.investing.com/news/stock-market-news/rocket-lab-wins-266-million-defense-contract-93CH-4804328)
**Recommendation: Watch** — a real, sizeable, multi-year defense contract is a strong signal for Rocket Lab's suborbital/defense diversification beyond its core launch business. Risk: no live quote confirmed today's opening reaction, and defense contract revenue recognizes over multiple years, not immediately. Monitoring trigger: a confirmed live quote, and Rocket Lab's next earnings for guidance detail on the contract's revenue cadence.

### Deals

#### General Motors (GM, NYSE) — Impact: Medium
**What happened:** GM reported Q2 2026 adjusted EPS of $3.57 (vs. $3.20 estimate) on $48B revenue (vs. $47.01B estimate), and raised FY2026 adjusted EPS guidance to $12–14 (from $11.50–13.50) and adjusted EBIT guidance to $14–16B, citing steady pricing, lower warranty costs, and narrowing EV losses. Reported July 21. [CNBC](https://www.cnbc.com/2026/07/21/general-motors-gm-earnings-q2-2026.html)
**Recommendation: Hold/Watch** — a clean beat-and-raise is good news already reflected in yesterday's trading; there isn't a fresh overnight edge left to trade on it today. Risk: full-year guidance still depends on tariff and EV-transition variables outside GM's control. Monitoring trigger: Q3 print and any tariff-policy change.

#### Tempus AI (TEM) / Personalis (PSNL), both Nasdaq — Impact: Low *(watchlist, unchanged)*
**What happened:** A shareholder-rights law firm announced a routine investigation of the pending Tempus–Personalis acquisition (Personalis holders get $16.25/share cash-or-stock). This kind of notice is standard practice around most sizeable M&A deals and is not itself a signal the deal is troubled. [PRNewswire](https://www.prnewswire.com/news-releases/hareholder-alert-the-ma-class-action-firm-announces-an-investigation-of-personalis-inc-nasdaq-psnl-302831071.html)
**Recommendation: Watch (unchanged)** — no change to the existing watchlist thesis. Risk: a genuine deal-price challenge, if one emerges, would matter; this notice alone does not indicate one. Monitoring trigger: any amended-deal-terms filing or a substantive (non-boilerplate) legal challenge.

#### Coinbase (COIN) / Robinhood (HOOD) / Bullish (BLSH) — Impact: Medium *(crypto-linked equities — securities, not tokens)*
**What happened:** The three crypto-exposed brokers/exchanges rallied July 21 (COIN +9.6%, from $168.00 to $175.85) on optimism after the White House agreed to an ethics provision as part of a deal aimed at unlocking a Senate floor vote on the CLARITY Act crypto market-structure bill. The vote itself has not yet been scheduled. [CryptoTimes](https://www.cryptotimes.io/2026/07/22/crypto-stocks-rally-coinbase-robinhood-bullish-lead-surge/), [CoinDesk](https://www.coindesk.com/policy/2026/07/21/white-house-pushes-senate-democrats-to-take-historic-crypto-clarity-act-ethics-deal)
**Recommendation: Watch** — the rally is trading ahead of an actual vote, which is a procedural step, not a passed law. Risk: any delay or breakdown in the ethics-deal negotiation would likely reverse the move. Monitoring trigger: an actual scheduled (and then completed) Senate vote on the CLARITY Act.

### Emerging Markets

#### China A-shares — FXI / KWEB proxies (NYSE Arca / Nasdaq) — Impact: Medium-High
**What happened:** Beijing deployed roughly 60B yuan (~$8.9B) of state capital via China Reform Holdings and China Chengtong Holdings into equities and ETFs on July 21 to halt an AI/semiconductor-driven tech selloff. The Shanghai Composite rose 1.79% and the Shenzhen Component 4.81% on the day; the ChinaAMC STAR 50 ETF alone saw a record ~13.8B yuan single-day inflow. This extends the "national team intervention" catalyst already noted July 20–21, now with confirmed scale. [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-21/china-broadens-market-rescue-with-record-inflows-into-tech-etf)
**Positioning: Neutral** — state intervention caps near-term downside but doesn't resolve the underlying tech-sector selloff that triggered it. Risk: intervention-driven rallies can be shallow and reverse once official buying tapers. Monitoring trigger: whether state fund purchases continue or taper over the next week.

### ETFs & Fund Flows

#### iShares MSCI South Korea ETF (EWY, NYSE Arca) — Impact: Medium
**What happened:** EWY recorded a record ~$2.8B weekly inflow and a record ~$814M single-day inflow (reported July 20) as investors used it as a liquid proxy for SK Hynix following SK Hynix's $26.5B Nasdaq ADR listing on July 10 (trading at a 27–51% premium to its Seoul shares). A same-day July 21 flow figure could not be confirmed inside this window. [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-20/emerging-market-etf-inflows-4-39-bln-led-by-south-korea)
**Positioning: Neutral** — real, large flows, but this is an ETF-proxy trade around a single underlying ADR premium, not a broad thematic reset. Risk: if the SK Hynix ADR premium normalizes, the EWY flow trade could reverse quickly. Monitoring trigger: SK Hynix ADR premium versus its Seoul-listed shares.

---
*Quantum computing — sector note, no rated entry:* the Chicago-Quantum-Exchange-led "Bloch Quantum Tech Hub" secured roughly $55M in federal and matching state/private funding on July 20, naming IonQ and IBM as corporate partners and Rigetti as having a separate letter of intent. This is a regional-consortium grant, not a company-specific financial event, and no stock-price reaction was found tied to it.

# ₿ Cryptos
*Prices reconstructed from WebSearch results (Yahoo Finance, Fortune, TradingKey) rather than a direct exchange pull — direct API access to Coinbase/Kraken/crypto.com was blocked this session. Figures below are for the morning of Tuesday, July 21, 2026; no July 22-specific pull was found. Treat as directionally reliable, not tick-accurate.*

## Market snapshot
| Asset | Price (USD, ~Jul 21 AM) | 24h % | Sources agree? | Note |
|-------|-------------|-------|----------------|------|
| BTC   | ~$65,200–$66,400 | +1% to +3% (sources vary) | Moderate (2 sources converge on range; one conflicting lower figure found and flagged, likely a different timeframe) | 5th consecutive day of spot-ETF inflows |
| ETH   | ~$1,900–$1,940 | +1% to +1.7% | Good (3 sources converge) | 3rd consecutive day of inflows, breaking an 8-week outflow streak |
| LDO   | — | +10.8% to +13% (sources vary), volume +108–202% | Fair | Real protocol catalyst: Nansen ETH Vault launched on Lido V3 |

### Bitcoin (BTC) — ETF inflow streak extends
**What happened:** Spot BTC ETFs recorded $226.8M in net inflows July 20 (the 5th straight positive session), with 5-day cumulative inflows around $727.3M; IBIT led with $116.5M. This trims 2026 YTD net outflows for US spot BTC ETFs to under $5B. [Cryptonomist](https://en.cryptonomist.ch/2026/07/21/bitcoin-etf-inflows-market-shift/), [CryptoBriefing](https://cryptobriefing.com/bitcoin-etf-inflows-727m-five-sessions/)
**Price action:** ~$65,200–$66,400 per Yahoo Finance and Fortune, a modest positive overnight move; a third source cited a much lower ~$60,128 figure that appears to reference a different timeframe and was not reconciled.
**Read: Watch** — a five-day inflow streak is a real, positive but not yet decisive shift after a rough 2026 for BTC ETF flows. Risk: the streak could stall as easily as it started. Monitoring trigger: whether inflows extend to a second week.

### Ethereum (ETH) — inflow streak breaks 8-week outflow trend
**What happened:** Spot ETH ETFs saw $37.5M in net inflows July 21, the 3rd consecutive positive day and the first break in an 8-week outflow streak; ETHA (BlackRock) led with +$52.8M while FETH (Fidelity) saw -$15.3M in outflows. [BitcoinWorld](https://bitcoinworld.co.in/ethereum-etf-inflows-july-21/), [Phemex](https://phemex.com/blogs/ethereum-etf-inflows-break-outflow-streak)
**Price action:** ~$1,900–$1,940, +1% to +1.7%, with good agreement across three sources.
**Read: Watch** — breaking an 8-week outflow streak is meaningfully more notable than BTC's continuation, but three days isn't yet a confirmed trend reversal. Risk: fund flows are volatile week to week. Monitoring trigger: whether the inflow streak holds through a full second week.

### CLARITY Act — regulatory context (not a single-asset trade)
**What happened:** The White House agreed to an ethics provision (barring federal officials from issuing or holding digital assets they regulate) as part of a deal meant to unlock a Senate floor vote on the CLARITY Act crypto market-structure bill. No vote has been scheduled yet, with roughly 14 working days left before the August recess. [CoinDesk](https://www.coindesk.com/policy/2026/07/21/white-house-pushes-senate-democrats-to-take-historic-crypto-clarity-act-ethics-deal), [The Hill](https://thehill.com/policy/technology/5981574-white-house-crypto-clarity-act-ethics-provision/)
**Read: Watch** — a procedural deal to unlock a vote, not a passed law. This is the catalyst behind the COIN/HOOD/BLSH equity rally noted in the Stocks section above. Risk: negotiations could stall again before recess. Monitoring trigger: an actual scheduled Senate vote.

---
**Sources consulted:** WebSearch only (curl/WebFetch to SEC EDGAR, data.sec.gov, ClinicalTrials.gov, Yahoo Finance chart API, Coinbase/Kraken/crypto.com APIs all returned 403 and were unreachable this session — see administrative note below). Company press releases, IR pages, and news coverage found via search: GlobeNewswire, StockTitan, BusinessWire, PRNewswire, GuruFocus, Fool.com, Invezz, Seeking Alpha, Investing.com, CNBC, Bloomberg, CoinDesk, The Hill, Cryptonomist, CryptoBriefing, BitcoinWorld, Phemex, CryptoTimes.
*Informational only; not investment advice. Crypto is volatile and speculative. Verify independently before trading. Generated 2026-07-22 ~09:15 ET.*

---

# Portfolio

## Snapshot
No live quotes were obtainable this run (see data-sourcing note above), so **no dollar-accurate account valuation is possible today**. As of the last confirmed state (July 21 close of business):
- Cash: $7,397.92
- Open positions at cost: DYN 63 sh @ $23.75 ($1,496.25) + HUT 11 sh @ $100.53 ($1,105.83) = $2,602.08 at cost
- Total account value at cost basis: $10,000.00 (unchanged from the $10,000 starting value; no realized gains/losses booked yet and no mark-to-market available)
- Benchmark: 13.4281 SPY shares at $744.71 cost ($10,000 equivalent at inception); no current SPY price available to compare.
- Return vs. $10,000 start and vs. SPY benchmark: **cannot be computed today** without a live quote — deferred until data access is restored.

## Open positions (ranked by cost basis; no live P&L available)
| Ticker | Shares | Avg cost | Current price | Unrealized P&L | Thesis status |
|--------|--------|----------|----------------|-----------------|---------------|
| HUT | 11 | $100.53 | Unavailable (quote feed down) | N/A | Intact — no new information since the July 20 Beacon Point lease; thesis unaffected. |
| DYN | 63 | $23.75 | Unavailable via quote feed; a same-week secondary offering priced at $20.50 (see Medical section) is a real, dated data point suggesting the stock may be trading near or below cost, but this is a financing print, not a market quote, and is not used as an official mark. | N/A | **Downgraded from intact to Watch** — the BLA/Priority Review thesis itself is unaffected by the offering, but the dilution and the offering price's proximity to the $19.00 stop (about $1.50/8% above it) call for closer tracking than before. |

## Today's trades
**No trades today.** No reliable machine-readable quote existed for any ticker (equities or crypto) — the same 403 policy block that affected yesterday's run persisted today. Per the execution rules, no fill is made without a real quote, so DYN and HUT were held unchanged and no new watchlist names were bought, regardless of conviction.

## Realized P&L to date
$0.00 realized (no positions have been closed). Combined realized + unrealized total cannot be computed today without a live mark, but stands at $0.00 realized plus an unknown unrealized figure pending restored data access.

## Watchlist changes
Added four names from today's research that would otherwise have been actionable but couldn't be filled without a live quote: **NBIS** (Watch — Nvidia's 9.3% stake plus $2B AI-infra investment), **RKLB** (Watch — $266M Space Force suborbital-launch contract), **MU** (Watch — +12% on a bullish analyst note amid an AI-memory rally; flagged as more sentiment/analyst-driven than the other three), and **ACAD** (Watch — FDA Fast Track for remlifanserin in Alzheimer's psychosis, no efficacy data yet). All four added 2026-07-22, expiring 2026-08-05.

The ten names carried over from July 20–21 (JSPR, TEM, PSNL, KLRS, ONCY, RGNX, BMNR, AMD, BLTE, GLSI) are unchanged and none have expired. Of these, AMD's thesis strengthened materially today (analyst price-target hikes, an investor event today) but remains unfilled pending a live quote. RGNX has a data conflict noted in the Medical section above — the watchlist entry is kept as-is until a live quote resolves it. GM and the EWY/China-EM ETF-flow items were deliberately **not** added to the watchlist: GM is a large-cap earnings beat already reflected in yesterday's price rather than a fresh catalyst-driven entry candidate, and the ETF/EM flow items are positioning reads, not single-name "graduate to a position" candidates.

## Administrative notes
- `reports/unsent-2026-07-21.md` was found in the repo (yesterday's briefing was drafted but never actually sent). It has been renamed to `reports/morning-research-2026-07-21.md` in today's commit per the standing procedure, flagged here exactly once.
- **This is the second consecutive run** in which (a) the session's network egress policy blocked every structured data source (SEC EDGAR, ClinicalTrials.gov, Yahoo Finance, all three crypto exchange APIs) with a 403, confirmed independently via curl, WebFetch, and the repo's own fetch script, and (b) the Gmail connector available to this session exposes only `create_draft` with no send capability, meaning every run's report ends up as an unsent draft rather than delivered mail. Neither issue is a one-off; both are standing configuration gaps worth fixing at the account/environment level — restoring egress access to market-data and filing endpoints, and granting the Gmail connector send scope — since the paper-trading simulation cannot execute a single fill or deliver a single email until they're addressed.

```PORTFOLIO_STATE
{
  "version": 1,
  "initialized_at": "2026-07-20T10:50:30-04:00",
  "last_run": "2026-07-22",
  "cash": 7397.92,
  "positions": [
    {
      "ticker": "DYN",
      "shares": 63,
      "avg_cost": 23.75,
      "entry_date": "2026-07-20",
      "stop": 19.00,
      "target": 32.00,
      "thesis": "FDA accepted BLA for z-rostudirsen (DMD, exon 51) with Priority Review, PDUFA Jan 21 2027; a July 21-22 upsized $375M offering priced at $20.50 is dilutive and sits close to the stop, but does not itself invalidate the regulatory thesis.",
      "status": "watch"
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
    { "ticker": "TEM", "reason": "Definitive deal to acquire Personalis (~$1.5B, floating stock ratio); TEM fell 9% on announcement; routine shareholder-rights investigation opened July 21-22, not itself material", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "PSNL", "reason": "Being acquired by Tempus at nominal $16.25/sh but trading well below that on deal-closing risk and floating ratio; routine shareholder-rights investigation opened July 21-22, not itself material", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "KLRS", "reason": "Positive expanded Phase 1a nAMD durability data but stock fell 5%; watch for Phase 2 initiation", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "ONCY", "reason": "FDA Fast Track for pelareorep combo in anal SCC; designation only, no efficacy data yet", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "RGNX", "reason": "$100-107.8M follow-on priced at $9.00/sh; sources conflict on stock reaction (+5.6% per prior note vs. -11.7% per July 22 research) — unresolved, watch for a confirmed live quote", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "BMNR", "reason": "Routine ETH treasury update ($11.3-11.5B total holdings); B. Riley trimmed PT to $25 from $33 (kept Buy) on July 21; leveraged proxy on ETH price", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "AMD", "reason": "Expanded Microsoft/Azure Helios deal; July 21 analyst PT hikes (Rosenblatt $655, UBS $700) after another +8.1% day; Advancing AI 2026 event July 22-23", "added": "2026-07-21", "expires": "2026-08-04" },
    { "ticker": "BLTE", "reason": "New Phase 3 DRAGON secondary-endpoint data for tinlarebant in Stargardt disease at ASRS; NDA already submitted to FDA", "added": "2026-07-21", "expires": "2026-08-04" },
    { "ticker": "GLSI", "reason": "Preliminary FLAMINGO-01 open-label arm data (~70-80% recurrence reduction, company-flagged as immature); DSMB recommended trial continue unmodified", "added": "2026-07-21", "expires": "2026-08-04" },
    { "ticker": "NBIS", "reason": "Nvidia took a 9.3% equity stake (~$5B) plus a planned $2B AI-infra investment; separate >$1B multi-year compute deal with Reflection AI; stock +18.78% July 21", "added": "2026-07-22", "expires": "2026-08-05" },
    { "ticker": "RKLB", "reason": "$266M U.S. Space Force firm-fixed-price contract for 12+6 suborbital launches through 2028; stock +6-9% after hours July 21", "added": "2026-07-22", "expires": "2026-08-05" },
    { "ticker": "MU", "reason": "+12% July 21 on a bullish BofA note (Buy, $1,550 PT) amid an AI-memory chip rally; more analyst/sentiment-driven than a discrete company event", "added": "2026-07-22", "expires": "2026-08-05" },
    { "ticker": "ACAD", "reason": "FDA Fast Track for remlifanserin in Alzheimer's-disease psychosis; Phase 2 RADIANT enrollment complete, topline expected Sept-Oct 2026", "added": "2026-07-22", "expires": "2026-08-05" }
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
    { "key": "LDO:2026-07-21:nansen-vault-lido-v3-launch", "noted": "2026-07-22" }
  ]
}
```
