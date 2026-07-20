---
name: morning-investment-research
description: Compile the daily morning investment-research briefing on overnight catalysts, split into a Stocks section (US-listed equities and ETFs across medical, technology, AI, quantum computing, space, deals, and emerging markets) and a Cryptos section (major digital assets priced off exchanges like crypto.com, Coinbase, and Kraken). Covers clinical-trial results, FDA actions, scientific-journal and preprint findings, regulatory moves, deals, and crypto market data, then formats it for email. Use this whenever the user asks for a morning or daily investment-research report, a catalyst or breakthrough briefing, an overnight roundup, "study results / deals / what moved in the last 24 hours," or similar — and especially when this runs as a scheduled routine. Trigger even if the request only says "run the morning report," "daily research report," or "any actionable opportunities overnight?" without naming this skill.
---

# Morning Investment Research

Produce one email-ready briefing covering overnight catalysts, split into two parts: **Stocks** (US-listed equities and ETFs across medical, technology/AI/quantum, space, emerging markets, deals, and funds) and **Cryptos** (digital assets themselves, priced off major exchanges). Both give a disciplined, source-traceable read on what (if anything) is worth attention over the last ~24 hours.

- **Stocks section:** every entry maps to a security on a **major US exchange** — the NYSE family (NYSE, NYSE American, NYSE Arca, where most ETFs list) or Nasdaq. Crypto-*equities* (exchanges, miners, treasury-strategy companies) and crypto *ETFs* are securities, so they live here, not in the Cryptos section.
- **Cryptos section:** covers the tokens directly, using live market data cross-checked across a few major exchanges (crypto.com, Coinbase, Kraken, with CoinGecko as an aggregator). Catalysts come from regulatory actions, protocol/network news, and exchange events.

This is decision-support for the reader's own research. It is informational, not financial advice, and the briefing says so. Crypto especially is volatile and speculative — treat every read as a starting point for the reader's own diligence, never a directive.

## Operating principles

Read these first — they're the difference between a useful briefing and plausible-sounding noise.

1. **Authoritative, timestamped feeds beat web search for "the last 24 hours."** A regulatory filing, a trial-registry update, or a journal/preprint with a real post date is verifiable to the day. Search snippets are not. Lead with structured sources (Step 2); use web search to corroborate and to catch gaps, not as the backbone.
2. **Every claim traces to a fetched source with a link.** If you can't point to the filing, registry entry, paper, or press release you read, it doesn't go in the briefing. No exceptions, no "reportedly."
3. **Never invent a ticker, exchange, sponsor, endpoint, or number.** Verify the company is real and the listing is real (Step 3). A wrong ticker in a 4am email is worse than an omission.
4. **Be honest about conviction.** A single overnight headline rarely justifies high confidence. When the signal is real but unconfirmed, say so and prefer "Watch" over "Buy."
5. **Quiet mornings are normal.** If nothing clears the significance bar, send the short confirmation note (Step 6). Don't manufacture entries to fill the template.
6. **Broad coverage, same bar.** More themes is not license for more noise. Every entry is still a real, dated, primary-sourced catalyst tied to a verifiable US-listed security. A theme with nothing material simply gets no section that morning — an eight-theme template half-filled with thin items is worse than three solid ones.
7. **Fetch machine-readable sources with `curl` via Bash, not WebFetch/WebSearch.** Every source in Step 2 has a plain JSON or HTML endpoint (EDGAR full-text search, `data.sec.gov`, ClinicalTrials.gov, crypto exchange tickers, NASA/press HTML). Fetch those directly with `curl -s -A "MorningResearch research@example.com" {url}` and parse the response yourself (Python's `json`/`re` are fine) instead of routing through WebFetch or WebSearch. WebFetch/WebSearch proxy through an LLM summarization call that has been observed failing transiently (`529 Overloaded` / "Server error mid-response") on a majority of calls in some runs — a failure mode unrelated to whether the target site is up, and `curl` to the same URL succeeds every time. Reserve WebFetch/WebSearch for the corroboration pass where you genuinely need open-ended web search or a natural-language summary of a long article, not for pulling structured data you can parse yourself. If a WebFetch/WebSearch call does fail with a transient server error, just reissue the same call once or twice immediately — never insert a bare `sleep`, which the harness blocks outright for standalone waits (use `curl` for that source instead if it fails twice).

## The workflow

### Step 1 — Fix the time window

Anchor everything to the run time in **America/New_York** (regulatory and US-market sources use ET).

- Default window: from **00:00 ET on the prior calendar day** to the run time. This is wider than a literal rolling 24h on purpose — filings and journals post on a business-day cadence, and a strict 24h window silently drops late-afternoon news.
- **Weekend/Monday handling:** on a Monday run, widen the start to **00:00 ET on the prior Friday** so Fri/Sat/Sun is covered. Same logic after market holidays.
- State the exact window at the top of the briefing so the reader knows what was and wasn't in scope.
- **Track which sources actually responded.** If a feed errors out or returns nothing, note it — a silent failure must never read as "quiet morning." The footer lists sources *checked* and flags any that were unreachable, so the reader can tell "nothing happened" apart from "the data was down."

### Step 2 — Gather from sources (priority order)

For each source, prefer a connected MCP connector if one is enabled; otherwise fetch the endpoint directly with `curl` (see Operating principle 7). **Exact endpoints, query construction, required headers, and the field map are in `references/sources.md` — read that file before fetching if it is present.** That file is not guaranteed to exist in every run environment; if `Read`/`Glob` shows it is missing, do not waste further calls looking for it — fall back to the endpoint list below (the same ones that have worked in practice) and proceed:

- **EDGAR full-text search (JSON):** `https://efts.sec.gov/LATEST/search-index?q=%22{phrase}%22&forms=8-K,6-K&startdt={YYYY-MM-DD}&enddt={YYYY-MM-DD}` — always send `-A "MorningResearch research@example.com"` (or similar descriptive UA); SEC blocks generic/absent user agents. Response `hits.hits[]._source` has `display_names` (name + ticker(s) + CIK) and `file_date`; `_id` is `{accession-no-dashes}:{primary-doc}`.
- **Confirm listing/ticker:** `https://data.sec.gov/submissions/CIK{10-digit-cik}.json` → top-level `tickers`/`exchanges` arrays are ground truth. Same UA header required.
- **Fetch a filing document:** `https://www.sec.gov/Archives/edgar/data/{cik-no-leading-zeros}/{accession-no-dashes}/{primary-doc}` — HTML; strip tags with a quick regex (`re.sub(r'<[^>]+>', ' ', html)`) rather than WebFetch.
- **ClinicalTrials.gov v2 API (JSON):** `https://clinicaltrials.gov/api/v2/studies?query.term={term}&filter.advanced=AREA%5BLastUpdatePostDate%5DRANGE%5B{start},{end}%5D&format=json`.
- **Crypto tickers:** Coinbase `https://api.exchange.coinbase.com/products/{PAIR}-USD/ticker`; Kraken `https://api.kraken.com/0/public/Ticker?pair={PAIR}USD` (note Kraken's response key is its own asset code, e.g. `XETHZUSD` for ETH, `XXBTZUSD` for BTC — don't assume the key matches the request param); crypto.com `https://api.crypto.com/v2/public/get-ticker?instrument_name={PAIR}_USDT` (24h change field is a **fraction**, e.g. `0.021` = 2.1%, not already a percent).
- **NASA news:** `https://www.nasa.gov/news-release/` (HTML listing) — grep `<h3...>`/date attributes rather than WebFetch-summarizing the whole page.
- **Stock/ETF quotes (for fills, benchmark marks, or a quick price check):** `https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?interval=1m&range=1d` (JSON; `chart.result[0].meta.regularMarketPrice`, `.previousClose`, `.regularMarketTime` as a unix timestamp) — reliable via plain `curl -A "Mozilla/5.0"`, no key needed, works for any US-listed ticker including SPY.
- All of the above are plain `curl` + parse; none need WebFetch. Use WebSearch/WebFetch only for open-ended corroboration queries that don't have a structured endpoint.

**Primary signal — company & fund disclosures (all themes):**
- **SEC EDGAR full-text search**, filtered to the window, across **8-K** (domestic issuers) *and* **6-K** (foreign private issuers — many ADRs and emerging-market names file here, not 8-K). Run topic queries spanning the themes (e.g. *topline*, *primary endpoint*, *FDA*, *definitive agreement*, *merger*, *acquisition*, *bitcoin*, *digital asset*, *spacecraft*, *quantum*, *artificial intelligence*, *data readout*) and union results. Prioritize by item code (map in `references/sources.md`): **8.01** other events, **2.02** earnings/guidance, **1.01** material agreements (deals, partnerships, licensing), **2.01** completion of an acquisition.

Then sweep the theme-specific sources below — only the ones plausibly in play that morning.

**Medical:**
- **ClinicalTrials.gov** — studies whose results or status posted/updated within the window (lead sponsor, phase, indication, endpoint, whether results are now posted). Connector if available, else the `LastUpdatePostDate` range filter.
- **bioRxiv / medRxiv** — preprints dated within the window; often where a breakthrough surfaces before formal publication.
- **FDA** — press announcements and novel-drug-approval feeds (approvals, CRLs, designations, safety actions).
- **PDUFA / catalyst calendar** — context only: was a decision *expected* today? Prioritize with it, don't treat it as proof.

**Technology, AI & quantum:**
- **Company IR/newsroom + reputable tech/science press** — products, model releases, benchmarks, partnerships with measurable significance.
- **arXiv** — `cs.AI`/`cs.LG` (AI), `quant-ph` (quantum) — and major journals (Nature, Science). Genuine results, not incremental papers; label preprints as unreviewed.
- Map a research/tech breakthrough to a US-listed beneficiary where one clearly exists (a quantum result → a listed quantum name; an AI-chip advance → the listed vendor). If there's no clean public-market proxy, note it but don't invent a ticker.

**Space:**
- **NASA / Space Force / DoD contract announcements**, commercial-space press, `astro-ph` preprints, and journals (e.g. Nature Astronomy). Launches, contract awards, mission milestones. Map to listed space names or a space ETF.

**Crypto-linked equities & ETFs → the Stocks section:**
- Crypto-equity disclosures (8-K) and news for listed names (exchanges, miners, treasury-strategy companies), plus **spot crypto ETF** flows/launches and SEC/regulatory crypto actions. These are securities — verify the listing and rate them like any stock, in Stocks.

**Crypto market data → the Cryptos section:**
- The tokens themselves, priced off a few major exchanges and cross-checked: **crypto.com, Coinbase, Kraken** (CoinGecko as an aggregator for market cap and a sanity reference). Lead with the majors (BTC, ETH) plus a few high-volume names and any notable overnight mover; pull the instrument list and rank by volume to find movers. Exact endpoints and field maps — including the gotcha that crypto.com reports 24h change as a fraction — are in `references/sources.md` §7. Pair each move with its catalyst (regulatory action, protocol/network news, exchange listing, ETF flow) and a real source.

**Deals (cross-theme):**
- M&A, strategic partnerships, and large financings via 8-K **1.01/2.01** and press. A deal is a catalyst *type*, not a sector — tag the entry to its theme, and note both sides when both are US-listed.

**Emerging markets:**
- ADR/foreign-issuer disclosures (**6-K / 20-F**), index actions (e.g. MSCI reclassifications), and country/region macro that moves a US-listed proxy. Surface via the ADR or an EM/country ETF, not the local share line.

**ETFs & fund flows:**
- Notable thematic/broad ETF launches, large flow or AUM moves, and methodology changes, via issuer press and flow data (`references/sources.md`). An ETF entry gets a **positioning read**, not a single-stock-style Buy/Hold.

**Earnings & guidance** cut across every theme — overnight/after-hours surprises are among the biggest single-day movers, and breakthroughs often surface first on the call. Catch them via 8-K **Item 2.02** and, optionally, an earnings calendar (`references/sources.md`).

**Corroboration:** after the structured pull, run targeted web searches to (a) confirm anything thin and (b) catch material news the feeds missed. Anything found only via loose search needs a primary source before it earns a row.

### Step 3 — Normalize, dedup, verify listing

- **One entry per company.** The same event often shows up in EDGAR *and* a press release *and* the registry — merge them into a single entry, citing each source once.
- **When sources conflict, surface the conflict — don't average it.** A company's press release may spin a result positively while the 8-K reveals a delay, a missed secondary endpoint, or a going-concern note. Lead with the primary/regulatory source and flag the discrepancy explicitly; a contradiction between the spin and the filing is itself signal.
- **Don't re-report yesterday.** A catalyst that broke late can fall inside today's window too. If a prior-day briefing was saved (see Step 7), skip anything already covered unless there's genuinely new information (e.g. results now posted, or the market reaction has materially evolved) — and say what's new.
- **Confirm public vs. private and get the listing.** A company that filed an 8-K is SEC-registered, but confirm it actually trades and capture the ticker + exchange. The authoritative, free way: from the EDGAR hit, take the CIK and read `https://data.sec.gov/submissions/CIK{cik}.json` — its `tickers` and `exchanges` arrays are ground truth (see `references/sources.md`). Accept the **NYSE family (NYSE, NYSE American, NYSE Arca — Arca is where most ETFs list)** and **Nasdaq** as "major US exchange." Note `data.sec.gov` collapses NYSE American into `NYSE`; trust the issuer's own filing for the precise venue. Mark OTC, foreign-only, private, or pre-IPO accordingly — and for those, omit the rating.
- **Foreign issuers & ADRs.** Emerging-market and other non-US companies file **6-K / 20-F**, not 8-K, and trade via ADRs. Confirm the ADR ticker lists on a major US exchange; if only the local line or a thin OTC ADR exists, surface the theme via an EM/country ETF instead.
- **Route crypto by instrument type.** Crypto-*equities* and crypto *ETFs* are securities — verify the listing and put them in **Stocks**. The *tokens* go in **Cryptos**, sourced from exchange market data (§7), not from a listing. Don't double-count: if both COIN (the stock) and BTC (the token) are in play, COIN is a Stocks entry and BTC is a Cryptos entry.
- **Crypto data integrity (Cryptos section).** Price and 24h-change figures come from the named exchanges, not memory. Quote at least two and confirm they agree to within a fraction of a percent; note which exchange a number came from, since 24h windows differ slightly across venues.
- **ETFs are instruments, not issuers.** An ETF doesn't file 8-Ks; verify it via its issuer and listing (NYSE Arca / Nasdaq) and treat it as a positioning read, not a company catalyst.
- **Drop anything you can't tie to a real named entity and a real source link.** Better a shorter briefing than a fabricated one.

### Step 4 — Rate impact and recommend (with discipline)

**Impact rating** — one of High / Medium / Low, applied consistently across themes:
- **High:** a pivotal/Phase 3 readout, FDA approval or CRL, primary endpoint met/missed on a lead asset; a platform-defining technology, AI, or quantum result; a transformational deal (large or definitive M&A); a major regulatory shift for a crypto proxy (e.g. a spot-ETF decision); a market-moving space contract or mission outcome.
- **Medium:** mid-stage data; a meaningful partnership, designation, or financing; a notable product, model release, or benchmark; a sizeable but non-transformational deal; a clear EM-index or macro move; a large or notable ETF flow or launch.
- **Low:** early-stage/preclinical, minor or incremental, or a development the market has very likely already priced.

**Recommendation** — Buy / Hold / Watch / Avoid, but every call must:
- be tied to *this specific* overnight catalyst (not generic sentiment about the company),
- name at least one concrete risk or uncertainty,
- end with a **monitoring trigger** — the next event or threshold that would confirm or kill the thesis (full data at a congress, the PDUFA date, deal close, next print), so the call is falsifiable rather than a vibe,
- fit in 2–3 sentences, and
- carry honest conviction — when the data is real but the readthrough is unconfirmed, that's a **Watch**, not a **Buy**.

Three adjustments for the broader scope:
- **ETF and pure-macro entries** take a *positioning read* — Overweight / Underweight / Neutral the theme, with the flow or catalyst as the reason — not a single-name Buy/Hold/Watch/Avoid.
- **Cryptos (the tokens) are data-led.** Lead each entry with the price and 24h move (cross-checked across exchanges) and its catalyst; a 24h price swing on its own is information, not a thesis. Any Buy/Hold/Watch/Avoid must hang on a real catalyst, not momentum, and given the volatility default to **Watch** unless something decisive (a major regulatory ruling, a network event) justifies more.
- **Emerging-market names** also carry elevated volatility; hold conviction a notch lower.

**Example — the bar:**
- Weak (do not write like this): "Strong pipeline and great momentum — Buy."
- Strong: "BICO's Phase 3 met its primary endpoint with a clean safety profile, derisking its lead asset ahead of a 2026 filing. The reaction may already be partly priced after yesterday's run, and a single trial doesn't settle commercial uptake — **Watch** for the full data at the upcoming medical congress before sizing a position."

### Step 5 — Assemble the briefing

The report has two top-level sections: **Stocks** and **Cryptos**. Each leads with its own summary table, then detailed entries. Within Stocks, group entries under theme sub-headings; only include sub-sections (and either top-level section) that have content. Order by impact (and for cryptos, by how much moved / how material the catalyst).

Stocks theme sub-sections: **Medical · Technology, AI & Quantum · Space · Emerging Markets · ETFs & Fund Flows · Deals** (Deals = cross-theme M&A; a deal inside one theme stays there, tagged `[Deal]`). Crypto-equities and crypto ETFs are securities and belong here, not under Cryptos.

```markdown
# Morning Investment Research — {Weekday, Month D, YYYY}
*Window covered: {start} – {end} ET*

# 📈 Stocks

## Summary
| Ticker | Name | Theme | Headline | Impact | Rec |
|--------|------|-------|----------|--------|-----|
| {TICK} | {name} | {Theme} | {≤8-word headline} | High | Watch |

### {Theme}
#### {Name} ({TICKER}, {Exchange}) — Impact: {High/Med/Low}
**What happened:** {1–2 sentences, with source link(s)}
**Market impact:** {who/what it moves and why}
**Recommendation: {Buy/Hold/Watch/Avoid}** — {2–3 sentences, catalyst-tied, names a risk, ends with a monitoring trigger}

*ETF / pure-macro entries instead read:* **Positioning: {Overweight/Underweight/Neutral the theme}** — {what the flow or catalyst signals}.

# ₿ Cryptos
*Prices from crypto.com / Coinbase / Kraken, cross-checked. As of {time} ET.*

## Market snapshot
| Asset | Price (USD) | 24h % | Sources agree? | Note |
|-------|-------------|-------|----------------|------|
| BTC   | {price}     | {±%}  | ✓ (3 venues)   | {1-line context or "—"} |
| ETH   | …           | …     | …              | … |

### {Asset} ({SYMBOL}) — {catalyst headline}
**What happened:** {the catalyst — regulatory action, protocol/network event, ETF flow, listing — with source link}
**Price action:** {move across the window, which exchanges, any cross-venue divergence}
**Read: {Watch/Avoid/Hold}** — {2–3 sentences tied to the catalyst, names a risk; momentum alone is not a thesis}

---
**Sources consulted:** {EDGAR 8-K/6-K, ClinicalTrials.gov, bioRxiv/medRxiv, FDA, arXiv, ETF flow data, crypto.com/Coinbase/Kraken/CoinGecko, named press — flag any that were unreachable}
*Informational only; not investment advice. Crypto is volatile and speculative. Verify independently before trading. Generated {timestamp ET}.*
```

### Step 6 — No-news fallback

"Significant" = at least one development that would plausibly move a stock or token, or reflects a real scientific/technical breakthrough (a High or Medium under Step 4). Routine pipeline chatter, status flips with no results, minor papers, and ordinary day-to-day crypto drift don't count.

Handle the two sections independently — Stocks can be quiet while Cryptos has a real catalyst, or vice versa. Keep whichever section has content and replace the empty one with a one-line "nothing cleared the bar." If both are empty, send the short note:

```markdown
# Morning Investment Research — {Weekday, Month D, YYYY}
*Window covered: {start} – {end} ET*

**Stocks:** No significant catalysts across the tracked themes (medical, technology/AI/quantum, space, emerging markets, deals, ETFs) cleared the bar in this window.
**Cryptos:** No material catalyst beyond ordinary price movement. {Optional: BTC {±%}, ETH {±%} over the window for context.}

Sources checked: {list}.
*Informational only; not investment advice.*
```

### Step 7 — Humanize, then send

- **Strip the AI tells before sending.** Apply the `humanize-ai-writing` skill's conventions to the prose (kill em-dash overuse, "it's not just X, it's Y," formulaic openers, hollow hedging). The reader is skimming half-awake — clean, direct sentences matter.
- **Send** the briefing by email to **joshuakessell@icloud.com**, subject: `Morning Research — {Mon D}: {N} item(s)` (or `Morning Research — {Mon D}: nothing actionable` on a quiet day). This is the reader's own configured routine delivering to their own inbox.
- **Keep a dated copy** of each briefing (e.g. `morning-research-YYYY-MM-DD.md`) if the run environment has any persistence. It's the audit trail and it's what Step 3's cross-day dedup reads to avoid repeating a catalyst the next morning.

## Preflight checks (run before sending)

Borrowed from the discipline of a data-quality pass: don't trust the draft, *check* it. Run these as a quick checklist over the assembled briefing. Anything that fails gets fixed or the entry gets cut — a shorter, correct briefing always beats a fuller, shaky one.

1. **Ticker integrity** — every ticker (stock, ADR, or ETF) was verified against its listing (`data.sec.gov` for issuers; issuer/exchange for ETFs), not recalled from memory. No ticker appears without a confirmed exchange.
2. **Source-traceability** — every factual claim (result, number, endpoint, sponsor, date) links to a primary source you actually fetched. No "reportedly," no orphan claims.
3. **No invented figures** — percentages, p-values, dollar amounts, and patient counts are quoted from a source, not approximated or filled in.
4. **Date / weekday consistency** — the briefing's date and weekday agree (if it says "Monday, June 22" but the 22nd is a Tuesday, something is wrong), and every event date falls inside the stated window.
5. **Catalyst actually happened** — each item is a *real overnight event*, not a calendar entry for a decision that's merely scheduled. Expected ≠ occurred.
6. **Listing status correct** — major-exchange entries carry a recommendation; OTC/foreign/private entries are labeled and carry none.
7. **Conflicts surfaced** — where sources disagreed, the discrepancy is stated, not smoothed over.
8. **Conviction honest** — no "Buy" resting on a single unconfirmed headline; unconfirmed-but-real signals are "Watch."
9. **Disclaimer present** — the footer carries the "informational, not investment advice" line.
10. **Section routing** — ETF entries read as a positioning call, not a single-name Buy/Hold. Foreign issuers are correctly identified (6-K/ADR). Crypto-equities and crypto ETFs sit in **Stocks**; the tokens sit in **Cryptos** — neither leaks into the other, and nothing is double-counted (the COIN stock and the BTC token are separate entries).
11. **Crypto data integrity** — every price and 24h-change figure came from a named exchange (not memory), was cross-checked across at least two venues, and the source venue is stated. Each crypto read hangs on a real catalyst, not momentum, and the "crypto is volatile and speculative" line is present.

If the briefing is the no-news note, only checks 4 and 9 apply.
