# Morning Investment Research — Thursday, July 23, 2026
*Window covered: Wednesday, July 22, 2026 00:00 ET – Thursday, July 23, 2026 ~05:15 ET*

**Data-sourcing note (read before the rest):** for the third run in a row, every structured, machine-readable source this briefing normally relies on was unreachable — SEC EDGAR, `data.sec.gov`, ClinicalTrials.gov, the Yahoo Finance quote API, and the Coinbase/Kraken/crypto.com APIs all returned a `403 Forbidden`. This was confirmed independently via direct `curl`, via `WebFetch` (which failed even on a plain HTML control page — reuters.com, fda.gov), and via the repo's own `fetch_quotes.py`. This is a session-level network-policy block, not a site outage — see the administrative note at the end of this report. `WebSearch` was the only working tool, so every item below is sourced from search-result snippets and article text rather than a fetched primary filing, and **no live price quote could be pulled for any equity or crypto asset, so no fills or price-based marks were possible today** (see Portfolio section). Tickers below could not be cross-checked against `data.sec.gov`'s listing ground truth for the same reason; exchange labels rely on what the sourced articles state.

# 📈 Stocks

## Summary
| Ticker | Name | Theme | Headline | Impact | Rec |
|--------|------|-------|----------|--------|-----|
| ARWR | Arrowhead Pharmaceuticals | Medical | Phase 3 SHASTA-3/4 both met primary + all secondary endpoints in severe hypertriglyceridemia | High | Watch |
| DYN | Dyne Therapeutics | Medical *(held position)* | $375M offering expected to close today; no change to the regulatory thesis | Medium | Watch (unchanged) |
| RGNX | Regenxbio | Medical *(watchlist)* | Prior conflicting stock-reaction reports resolved: shares fell ~17% on the July 17 pricing | Medium | Watch |

### Medical

#### Arrowhead Pharmaceuticals (ARWR, Nasdaq) — Impact: High
**What happened:** Arrowhead reported topline results from the Phase 3 SHASTA-3 and SHASTA-4 studies of plozasiran in severe hypertriglyceridemia on July 22. Both trials met the primary endpoint (triglyceride reduction vs. placebo, 79–81% reduction) and all prespecified secondary endpoints, including a statistically significant cut in acute pancreatitis events — 78% overall and 100% in the highest-risk subgroup — with no new safety signals reported. [BioSpace](https://www.biospace.com/press-releases/arrowhead-pharmaceuticals-reports-topline-results-from-phase-3-shasta-3-and-shasta-4-studies-of-plozasiran-in-patients-with-severe-hypertriglyceridemia), [Arrowhead IR](https://ir.arrowheadpharma.com/news-releases/news-release-details/arrowhead-pharmaceuticals-reports-topline-results-phase-3-shasta)
**Market impact:** shares reportedly rose more than 18% in pre-market trading on the announcement, per secondary coverage; that figure is a search-derived data point, not a confirmed exchange quote. Arrowhead intends to file a supplemental NDA to the FDA by year-end.
**Recommendation: Watch** — this is a clean, well-sourced double Phase 3 win on both primary and secondary endpoints, exactly the kind of catalyst this mandate looks for. It would ordinarily be a Buy candidate, but no reliable machine-readable quote was obtainable today, so per the execution rules no fill is made on a headline price. Risk: an ~18% pre-market pop likely already prices in much of the good news, and a supplemental filing still needs FDA review. Monitoring trigger: a confirmed live quote to size an entry, and the sNDA filing timeline.

#### Dyne Therapeutics (DYN, Nasdaq) — Impact: Medium — *held position, see Portfolio section*
**What happened:** No new catalyst since the July 21–22 upsized $375M offering (already noted). The offering was expected to close on or about July 23 (today) per the pricing release — a routine closing mechanic, not new information.
**Market impact:** one secondary aggregator cited a same-day figure near $23.97 (+2.2%), while an separate outlet reported Tuesday's regular close at $23.83 followed by a 10.6% after-hours drop to $21.30 on the offering news. These figures conflict and neither is a confirmed exchange quote, so neither is used as an official mark.
**Recommendation: Watch (unchanged)** — the Priority Review/PDUFA thesis is unaffected by the raise or its closing. Risk: the informal price points above, if accurate, would sit at or below the $19.00 stop's cushion; this needs a live quote to resolve. Monitoring trigger: a confirmed live quote against the $19.00 stop.

#### Regenxbio (RGNX, Nasdaq) — Impact: Medium — *on watchlist since July 20*
**What happened:** Yesterday's briefing flagged conflicting reports on how RGNX reacted to its $100M offering (+5.6% vs. -11.7%, both undated precisely). Today's research found a clearer account: the offering (10,003,889 shares plus pre-funded warrants at $9.00) priced July 17, and shares fell roughly 17% on the pricing, closing at $9.70 that day — down from $15.65 on July 9, a nearly 38% decline over that stretch. A shareholder-rights firm separately opened an investigation into statements about RGX-111's efficacy/safety data. [Investing.com](https://www.investing.com/news/company-news/regenxbio-prices-100m-public-offering-at-9-per-share-93CH-4798047), [StocksToTrade](https://stockstotrade.com/news/regenxbioinc-rgnx-news-2026_07_18/)
**Market impact:** this resolves (does not merely surface) the prior conflict — the negative reaction is the better-supported figure across multiple sources.
**Recommendation: Watch** — hold the existing watchlist entry; dilution plus litigation overhang is a real risk stack, not just financing noise. Risk: continued legal headline risk pending the investigation's outcome. Monitoring trigger: a confirmed live quote, and any update from the shareholder-rights investigation.

*No new catalysts cleared the bar today in Technology/AI & Quantum, Space, Deals, or Emerging Markets.* AMD's "Advancing AI 2026" event (San Francisco, July 22–23) is underway but no results had been announced as of this run's window; the existing AMD watchlist entry stands pending outcomes. Nvidia published new Vera CPU specifications July 21 and Hitachi/Intel/AIST announced a silicon-quantum research collaboration July 22, but neither is a discrete, market-moving event tied to a name in this book. Public Storage completed its previously-announced acquisition of National Storage Affiliates (July 22); this closes a deal disclosed back in March and isn't a fresh signal.

# ₿ Cryptos
*Prices reconstructed from WebSearch results (Yahoo Finance) rather than a direct exchange pull — direct API access to Coinbase/Kraken/crypto.com was blocked this session, same as the prior two runs. Figures below are for the morning of Wednesday, July 22, 2026; no July 23-specific pull was found. Treat as directionally reliable, not tick-accurate.*

## Market snapshot
| Asset | Price (USD, ~Jul 22 AM) | 24h % | Sources agree? | Note |
|-------|-------------|-------|----------------|------|
| BTC   | ~$65,557–$66,509 | opened +2%, eased back by mid-morning | Single source found (Yahoo Finance); not independently cross-checked | 6th consecutive day of spot-ETF inflows |
| ETH   | ~$1,918–$1,929 | opened +1.3%, eased back by mid-morning | Single source found (Yahoo Finance); not independently cross-checked | Inflow streak extends to 4 days |

### Bitcoin (BTC) — ETF inflow streak extends to a sixth day
**What happened:** Spot BTC ETFs added roughly $203M net on July 21 (ET), a sixth consecutive day of inflows, following the $226.9M/5-day streak already noted yesterday. [The Market Periodical](https://themarketperiodical.com/2026/07/22/crypto-etfs-update-bitcoin-etfs-add-227m-log-5th-consecutive-day-of-inflows/), [Blockchainreporter](https://blockchainreporter.net/spot-bitcoin-etfs-record-203-million-in-sixth-straight-day-of-inflows/)
**Price action:** Bitcoin opened July 22 at $66,508.87, roughly +2% from Tuesday's open, then eased to $65,556.99 by 9:20am ET. Only one source (Yahoo Finance's daily crypto roundup) was found for this figure; it was not independently cross-checked against a second exchange this run.
**Read: Watch** — a sixth straight inflow day extends an already-positive trend, but this is an incremental continuation, not new information on its own. Risk: the streak could reverse on any single large redemption day. Monitoring trigger: whether inflows extend through a full second week.

### Ethereum (ETH) — inflow streak extends to four days
**What happened:** Spot ETH ETFs continued their inflow streak (previously noted breaking an 8-week outflow run on July 21); today's window found no new dollar figure beyond what was already reported yesterday, only continued-streak framing. [Yahoo Finance](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-wednesday-july-22-2026-both-cryptos-open-higher-before-losing-steam-153454067.html)
**Price action:** Ethereum opened July 22 at $1,928.62 (+1.3% from Tuesday), then eased to $1,918.35 by 9:21am ET. Same single-source caveat as BTC above.
**Read: Watch** — consistent with yesterday's read; still too short a streak to call a confirmed reversal. Risk: fund flows are volatile week to week. Monitoring trigger: whether the inflow streak holds through a full second week.

### CLARITY Act — White House and Senate reach an ethics-provision deal
**What happened:** Following the ethics-provision negotiations flagged in yesterday's briefing, the White House and Senate Democrats reportedly reached agreement on the ethics package (barring federal officials from issuing or holding digital assets they regulate) that had stalled the CLARITY Act crypto market-structure bill. This clears a specific procedural obstacle toward a floor vote before the Senate's August recess; a vote has still not been scheduled as of this window. [The Motley Fool](https://www.fool.com/coverage/stock-market-today/2026/07/22/crypto-market-today-july-22-clarity-act-progress-balances-inflation-fears/)
**Read: Watch** — this is genuinely new information (a resolved sticking point, not just "talks continuing"), and is the likely driver behind continued strength in crypto-linked equities (COIN/HOOD/BLSH, already covered in prior briefings). Risk: a scheduled vote could still fail or slip past the recess. Monitoring trigger: an actual scheduled Senate floor vote.

### Russia — State Duma passes crypto property-classification law
**What happened:** Russia's State Duma passed a law on July 21 classifying cryptocurrencies as property and permitting regulated trading under Bank of Russia oversight, effective September 1, 2026. [source found via WebSearch synthesis; no direct legislative text or wire-service article link was returned in the search results, so this item carries a lower sourcing bar than the items above and should be treated as provisional]
**Read: Watch** — a large jurisdiction formally legitimizing crypto as property is a real regulatory signal for global sentiment, but has no direct US-listed proxy and no confirmed primary-source link was retrievable this run. Risk: this claim is currently one level less verified than the rest of this briefing. Monitoring trigger: a primary source (Duma record or major wire) once data access allows direct verification.

---
**Sources consulted:** WebSearch only (curl/WebFetch to SEC EDGAR, data.sec.gov, ClinicalTrials.gov, FDA.gov, Yahoo Finance chart API, Coinbase/Kraken/crypto.com APIs, and even a plain-HTML control page all returned 403 or were unreachable this session — see administrative note below). Company press releases, IR pages, and news coverage found via search: BioSpace, Arrowhead IR, Investing.com, StocksToTrade, The Market Periodical, Blockchainreporter, Yahoo Finance, The Motley Fool, TechTimes, GovConWire.
*Informational only; not investment advice. Crypto is volatile and speculative. Verify independently before trading. Generated 2026-07-23 ~05:15 ET.*

---

# Portfolio

## Snapshot
No live quotes were obtainable this run (see data-sourcing note above), so **no dollar-accurate account valuation is possible today**. As of the last confirmed state (July 20 fills; unchanged since):
- Cash: $7,397.92
- Open positions at cost: DYN 63 sh @ $23.75 ($1,496.25) + HUT 11 sh @ $100.53 ($1,105.83) = $2,602.08 at cost
- Total account value at cost basis: $10,000.00 (unchanged from the $10,000 starting value; no realized gains/losses booked yet and no mark-to-market available)
- Benchmark: 13.4281 SPY shares at $744.71 cost ($10,000 equivalent at inception); no current SPY price available to compare.
- Return vs. $10,000 start and vs. SPY benchmark: **cannot be computed today** without a live quote — deferred until data access is restored.

## Open positions (ranked by cost basis; no live P&L available)
| Ticker | Shares | Avg cost | Current price | Unrealized P&L | Thesis status |
|--------|--------|----------|----------------|-----------------|---------------|
| HUT | 11 | $100.53 | Unavailable (quote feed down); an unverified search snippet put shares near $108, up ~128% YTD | N/A | Intact — no new information since the July 20 Beacon Point lease; thesis unaffected. |
| DYN | 63 | $23.75 | Unavailable (quote feed down); unverified search snippets conflict between ~$23.97 and a post-offering after-hours print near $21.30 | N/A | Watch (unchanged from yesterday) — regulatory thesis intact; dilution and price proximity to the $19.00 stop still warrant closer tracking than "intact." |

## Today's trades
**No trades today.** No reliable machine-readable quote existed for any ticker (equities or crypto) — the same 403 policy block that affected the last two runs persisted today. Arrowhead (ARWR) is a strong, well-sourced new Phase 3 win that would ordinarily be Buy-eligible, but per the execution rules no fill is made without a real quote, so it goes to the watchlist instead. DYN and HUT were held unchanged.

## Realized P&L to date
$0.00 realized (no positions have been closed). Combined realized + unrealized total cannot be computed today without a live mark, but stands at $0.00 realized plus an unknown unrealized figure pending restored data access.

## Watchlist changes
Added **ARWR** (Watch — Phase 3 SHASTA-3/4 met all endpoints in severe hypertriglyceridemia, sNDA filing planned by year-end), added 2026-07-23, expiring 2026-08-06.

Updated the **RGNX** entry's reason to reflect the resolved stock-reaction conflict (confirmed ~17% decline on the July 17 pricing, not the earlier +5.6% figure), added-date and expiry unchanged.

The thirteen names carried over from July 20–22 (JSPR, TEM, PSNL, KLRS, ONCY, RGNX, BMNR, AMD, BLTE, GLSI, NBIS, RKLB, MU, ACAD) are otherwise unchanged; none have expired (earliest expiry is 2026-08-03).

## Administrative notes
- `reports/unsent-2026-07-22.md` was found in the repo (yesterday's briefing was drafted but never actually sent, for the same reasons noted below). It has been renamed to `reports/morning-research-2026-07-22.md` in today's commit per the standing procedure, flagged here exactly once.
- **This is the third consecutive run** in which (a) the session's network egress policy blocked every structured data source (SEC EDGAR, ClinicalTrials.gov, FDA.gov, Yahoo Finance, all three crypto exchange APIs) with a 403, confirmed independently via curl, WebFetch, and the repo's own fetch script, and (b) the Gmail connector available to this session exposes only `create_draft` with no send capability, meaning every run's report ends up as an unsent draft rather than delivered mail. Neither issue is a one-off; both are standing configuration gaps at the account/environment level — restoring egress access to market-data and filing endpoints, and granting the Gmail connector send scope — since the paper-trading simulation has not executed a single fill or delivered a single email since it opened on July 20.

```PORTFOLIO_STATE
{
  "version": 1,
  "initialized_at": "2026-07-20T10:50:30-04:00",
  "last_run": "2026-07-23",
  "cash": 7397.92,
  "positions": [
    {
      "ticker": "DYN",
      "shares": 63,
      "avg_cost": 23.75,
      "entry_date": "2026-07-20",
      "stop": 19.00,
      "target": 32.00,
      "thesis": "FDA accepted BLA for z-rostudirsen (DMD, exon 51) with Priority Review, PDUFA Jan 21 2027; the upsized $375M offering priced at $20.50 (expected to close July 23) is dilutive and sits close to the stop, but does not itself invalidate the regulatory thesis.",
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
    { "ticker": "RGNX", "reason": "$100M ($107.8M) follow-on priced at $9.00/sh on July 17; shares fell ~17% on the pricing (resolves prior conflicting reports); separate shareholder-rights investigation into RGX-111 disclosures adds legal-headline risk", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "BMNR", "reason": "Routine ETH treasury update ($11.3-11.5B total holdings); B. Riley trimmed PT to $25 from $33 (kept Buy) on July 21; leveraged proxy on ETH price", "added": "2026-07-20", "expires": "2026-08-03" },
    { "ticker": "AMD", "reason": "Expanded Microsoft/Azure Helios deal; July 21 analyst PT hikes (Rosenblatt $655, UBS $700) after another +8.1% day; Advancing AI 2026 event runs July 22-23, outcomes pending", "added": "2026-07-21", "expires": "2026-08-04" },
    { "ticker": "BLTE", "reason": "New Phase 3 DRAGON secondary-endpoint data for tinlarebant in Stargardt disease at ASRS; NDA already submitted to FDA", "added": "2026-07-21", "expires": "2026-08-04" },
    { "ticker": "GLSI", "reason": "Preliminary FLAMINGO-01 open-label arm data (~70-80% recurrence reduction, company-flagged as immature); DSMB recommended trial continue unmodified", "added": "2026-07-21", "expires": "2026-08-04" },
    { "ticker": "NBIS", "reason": "Nvidia took a 9.3% equity stake (~$5B) plus a planned $2B AI-infra investment; separate >$1B multi-year compute deal with Reflection AI; stock +18.78% July 21", "added": "2026-07-22", "expires": "2026-08-05" },
    { "ticker": "RKLB", "reason": "$266M U.S. Space Force firm-fixed-price contract for 12+6 suborbital launches through 2028; stock +6-9% after hours July 21", "added": "2026-07-22", "expires": "2026-08-05" },
    { "ticker": "MU", "reason": "+12% July 21 on a bullish BofA note (Buy, $1,550 PT) amid an AI-memory chip rally; more analyst/sentiment-driven than a discrete company event", "added": "2026-07-22", "expires": "2026-08-05" },
    { "ticker": "ACAD", "reason": "FDA Fast Track for remlifanserin in Alzheimer's-disease psychosis; Phase 2 RADIANT enrollment complete, topline expected Sept-Oct 2026", "added": "2026-07-22", "expires": "2026-08-05" },
    { "ticker": "ARWR", "reason": "Phase 3 SHASTA-3 and SHASTA-4 both met primary endpoint (79-81% triglyceride reduction) and all secondary endpoints incl. pancreatitis reduction; shares reportedly +18% pre-market; sNDA planned by year-end", "added": "2026-07-23", "expires": "2026-08-06" }
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
    { "key": "RUSSIA-CRYPTO:2026-07-21:state-duma-property-law", "noted": "2026-07-23" }
  ]
}
```
