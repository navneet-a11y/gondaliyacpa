# 127-tax-dividend-tax-credit.html: changes

Source: pages-paste/127-tax-dividend-tax-credit.html. Edit script: scratchpad/ed/e127.py (exact string replacements, each one checked to match the expected number of times).

## Reproduce-first checks (engine.py)
- Credit table, dollar columns (per $100 received = 138 x eligible rate, 115 x other rate): N.L. 138 x 6.3% = $8.694, shown as **$8.69**; 115 x 3.2% = **$3.68**. PEI 138 x 10.50% = **$14.49**; 115 x 1.3043% = $1.4999, shown as **$1.50**. All match the published cells.
- Top rates (used in the At a glance text), computed with engine `rates()` at very high income: NB 32.40% / 46.83% (published 32.40% / 46.83%), NS 41.58% / 49.99% (published the same), PEI 37.92% / 49.07% (same), NL at $3M 46.20% / 48.96% (same). Section 6 rows were also reproduced for NB/NS/PEI/NL at $30k, $75k and $150k, and section 7 rows at $40k/$90k/$200k (for example NB $756.27 and NL $2,067.27 at $90k). All match.
- New top rates come from rows.json (top bracket, matching engine at $1M): AB 34.31/42.31, SK 29.64/41.34, MB 37.78/46.67, YT 28.93/44.04, NT 28.33/36.82, NU 33.08/37.79.

## Changes (before -> after)
1. Byline: "Updated October 26, 2026" -> "Updated November 5, 2026". "Figures checked October 23, 2026" was left as is, as the brief requires.
2. Trust box: "Seven provinces confirmed for 2026; the rest are marked as being confirmed" -> "All 13 provinces and territories confirmed for 2026".
3. At a glance, provincial credits: "...Newfoundland and Labrador. Alberta, ... Nunavut are being confirmed." -> "All 13 provinces and territories. For Alberta, ..., Nunavut, the rates are those on CRA's 2025 provincial worksheets (line 61520); none of the six 2026 budgets changed personal income tax."
4. At a glance, top rates: "In the seven confirmed provinces ... low of 32.40% (New Brunswick) ... other than eligible from 46.83% (New Brunswick) to 49.99%" -> "Across the 13 provinces and territories ... low of 28.33% (Northwest Territories) to a high of 46.20% (N.L.) ... other than eligible from 36.82% (Northwest Territories) to 49.99% (Nova Scotia)".
5. Section 5 lead: "Thirteen jurisdictions, seven confirmed." -> "Thirteen jurisdictions, all confirmed."
6. Credit table: six "Being confirmed" rows filled in (eligible %, other %, $ per $100 eligible, $ per $100 other, status):
   - Alberta: 8.12%, 2.18%, $11.21, $2.51, "Confirmed; rate on CRA Worksheet AB428"
   - Saskatchewan: 11%, 2.519%, $15.18, $2.90, "... SK428"
   - Manitoba: 8%, 0.7835%, $11.04, $0.90, "... MB428"
   - Yukon: 12.02%, 0.67%, $16.59, $0.77, "... YT428"
   - Northwest Territories: 11.5%, 6%, $15.87, $6.90, "... NT428"
   - Nunavut: 5.51%, 2.61%, $7.60, $3.00, "... NU428"
   The existing row order was kept.
7. "Manitoba and the others." paragraph -> "Alberta, Saskatchewan, Manitoba and the territories." It now names the CRA worksheet source (line 61520, AB428 to NU428), says the 2026 worksheets come in January 2027 and that the six budgets made no change to personal income tax, and says the calculator covers all 13. The same province-page links were kept, now worded "show their dividend rates".
8. Section 6 lead: "for the seven provinces with confirmed 2026 credits" -> "for Ontario, British Columbia, Quebec and the four Atlantic provinces". The tables cover the same seven provinces; only the false reason was removed.
9. Section 12 Common Mistakes: the paragraph "Assuming a confirmed rate for every province ... for the six provinces and territories marked as being confirmed, wait for the official 2026 rate..." was deleted. Its premise no longer holds, and the section has no item count.
10. FAQ "What are the provincial dividend tax credit rates for 2026?" (visible and JSON-LD, identical): "...and Newfoundland and Labrador 6.3% and 3.2%. The other six are being confirmed." -> "...Newfoundland and Labrador 6.3% and 3.2%, Alberta 8.12% and 2.18%, Saskatchewan 11% and 2.519%, Manitoba 8% and 0.7835%, Yukon 12.02% and 0.67%, the Northwest Territories 11.5% and 6%, and Nunavut 5.51% and 2.61%."
11. FAQ "What is Manitoba's dividend tax credit for 2026?" (visible and JSON-LD, identical): "It has not been confirmed. ..." -> "Manitoba's dividend tax credit is 8% of the grossed-up amount for eligible dividends and 0.7835% for other than eligible dividends, the rates on CRA's Worksheet MB428 (line 61520). CRA publishes the 2026 worksheet in January 2027; Manitoba's 2026 budget made no change to personal income tax. Our calculators now work out Manitoba dividend tax."

## Left unchanged, and why
- The section 6 marginal-rate tables and the section 7 "$10,000 of dividends" tables still cover only the seven original provinces. They contain no "Being confirmed" cells, and adding six columns or rows would be a large addition beyond the brief's minimal-edit rule. The engine reproduces these tables exactly, so the six could be added later if wanted.
- "...because its 6.3% credit is the smallest of the seven" (section 6): this still refers to the seven provinces in those tables, so it stays true. Nunavut's 5.51% is lower, but Nunavut is not in those tables.
- Section 5 sentence "Where we could not confirm a 2026 rate from an official source, the row says so; we never fill the gap with an estimate": this is a general policy statement and was left as is.
- The Manitoba FAQ gives no top rate. Manitoba's 2026 rates in the $200k to $400k range (BPA phase-out) are higher than its top-bracket rate, so a single "top rate" figure would mislead.
- No dateModified in the JSON-LD. The "Figures checked" dates were not changed.

## Check
`ok 0`: the JSON-LD parses, and 0 "being confirmed" remain.
