# Source endpoints, headers, and field maps

All of these are plain-HTTP endpoints. Fetch them with `curl` via Bash and parse the response yourself (Python `json`/`re`). Do NOT route them through WebFetch/WebSearch — those proxy through an LLM summarizer that fails transiently and adds nothing for structured data. Reserve WebFetch/WebSearch for open-ended corroboration only.

## 1. SEC EDGAR full-text search (primary signal, all themes)

```
curl -s -A "MorningResearch research@example.com" \
  "https://efts.sec.gov/LATEST/search-index?q=%22{phrase}%22&forms=8-K,6-K&startdt={YYYY-MM-DD}&enddt={YYYY-MM-DD}"
```

- The `-A` (User-Agent) header is **mandatory** — SEC blocks generic/absent UAs. Use a descriptive app name + contact address.
- Response: `hits.total.value` (count), `hits.hits[]._source.display_names` (company name + ticker(s) + CIK), `._source.file_date`, `._source.root_forms`. `_id` is `{accession-with-dashes}:{primary-document}`.
- Run one query per theme phrase and union results: *topline*, *primary endpoint*, *FDA*, *definitive agreement*, *merger*, *acquisition*, *bitcoin*, *digital asset*, *spacecraft*, *quantum computing*, *artificial intelligence*, *data readout*.
- Omitting `forms=` returns everything (13F, NPORT, S-1 noise) — keep the forms filter on for the main sweep.

### 8-K item codes (priority order)
| Item | Meaning |
|------|---------|
| 8.01 | Other events (most PR-driven catalysts land here) |
| 2.02 | Results of operations / guidance (earnings) |
| 1.01 | Entry into material agreement (deals, partnerships, licensing) |
| 2.01 | Completion of acquisition/disposition |
| 7.01 | Reg FD disclosure (often paired with 8.01) |
| 5.02 | Officer/director changes (usually noise; check context) |

## 2. Confirm listing / ticker (ground truth)

```
curl -s -A "MorningResearch research@example.com" "https://data.sec.gov/submissions/CIK{10-digit-zero-padded-cik}.json"
```

Top-level `tickers` and `exchanges` arrays are authoritative. Accept NYSE / NYSE American / NYSE Arca / Nasdaq. Note: this API collapses NYSE American into `NYSE`; trust the issuer's own filing for the precise venue. `filings.recent` (parallel arrays: `form`, `filingDate`, `accessionNumber`, `primaryDocument`, `items`) lets you list a company's filings in the window without another FTS query.

## 3. Fetch a filing document

```
https://www.sec.gov/Archives/edgar/data/{cik-no-leading-zeros}/{accession-no-dashes}/{primary-document}
```

HTML. Strip tags with `re.sub(r'<[^>]+>', ' ', html)` then collapse whitespace. Fetching the accession directory (trailing `/`) and grepping `href=".*\.htm"` lists exhibits (press release is usually `ex99-1.htm` / `*ex99_1.htm`).

## 4. ClinicalTrials.gov v2 API

```
curl -s "https://clinicaltrials.gov/api/v2/studies?query.term={term}&filter.advanced=AREA%5BLastUpdatePostDate%5DRANGE%5B{YYYY-MM-DD},{YYYY-MM-DD}%5D&format=json&pageSize=50"
```

URL-encode the brackets. Key fields: `protocolSection.identificationModule` (title, NCT ID), `.sponsorCollaboratorsModule.leadSponsor`, `.designModule.phases`, `.statusModule`, `hasResults`.

## 5. bioRxiv / medRxiv preprints

```
curl -s "https://api.biorxiv.org/details/biorxiv/{YYYY-MM-DD}/{YYYY-MM-DD}/0/json"
```

(`medrxiv` for medRxiv.) Paged 100 per call via the trailing cursor. `collection[]` has `title`, `authors`, `date`, `doi`, `category`. Preprints are unreviewed — label them as such.

## 6. FDA press announcements

`https://www.fda.gov/news-events/fda-newsroom/press-announcements` — HTML listing; grep titles + dates. Company 8-Ks referencing FDA actions (found via §1) are an acceptable primary source when the FDA page lags.

## 7. Crypto market data (Cryptos section)

Quote at least two venues and confirm agreement within a fraction of a percent; name the venue for every number.

- **Coinbase:** `https://api.exchange.coinbase.com/products/{SYM}-USD/ticker` → `price`, `time`.
- **Kraken:** `https://api.kraken.com/0/public/Ticker?pair={SYM}USD` → **result key is Kraken's own asset code**, not your request string (BTC → `XXBTZUSD`, ETH → `XETHZUSD`; newer listings like SOL use `SOLUSD`). Take the first/only key. `c[0]` = last trade, `o` = 24h open (compute 24h % from these).
- **crypto.com:** `https://api.crypto.com/v2/public/get-ticker?instrument_name={SYM}_USDT` → `result.data`: `a` = last price, `c` = **24h change as a fraction** (0.021 = +2.1%, not already a percent). USDT-quoted, so expect a small basis vs USD venues.
- **CoinGecko (aggregator/sanity):** `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true`.

## 8. Equity/ETF quotes (fills, SPY benchmark, reaction checks)

```
curl -s -A "Mozilla/5.0" "https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?interval=1m&range=1d"
```

`chart.result[0].meta`: `regularMarketPrice`, `previousClose` (or `chartPreviousClose`), `regularMarketTime` (unix). Works pre-market and after-hours for any US-listed ticker including SPY. `scripts/fetch_quotes.py` in this repo wraps this plus the crypto venues for the single-pass quote fetch.

## 9. arXiv (AI / quantum)

```
curl -s "http://export.arxiv.org/api/query?search_query=cat:quant-ph&sortBy=submittedDate&sortOrder=descending&max_results=25"
```

Atom XML (`<entry><title>/<published>/<summary>`). Categories: `cs.AI`, `cs.LG`, `quant-ph`, `astro-ph`. Only genuine results, mapped to a listed beneficiary when one clearly exists.

## 10. NASA / space

`https://www.nasa.gov/news-release/` — HTML; grep `<h3` headings and date attributes. DoD contract announcements: `https://www.defense.gov/News/Contracts/`.
