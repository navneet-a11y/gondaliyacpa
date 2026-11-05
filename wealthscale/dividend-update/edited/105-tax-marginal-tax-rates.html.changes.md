# 105-tax-marginal-tax-rates.html: change log (2026-11-05)

Source: pages-paste/105-tax-marginal-tax-rates.html. Edited copy: edited/105-tax-marginal-tax-rates.html.
All edits were Python exact-string replacements, each asserted to match exactly once. Every new number comes from engine.py and was cross-checked against rows.json.

## Reproduce-first checks (all exact matches)
- **Dividend table at $50k / $100k / $250k.** The scenario is the marginal rate per $1 of dividend at that taxable income, from `rates(x, p)`. The engine reproduced every published cell exactly:
  - NB: -7.76 / 7.56 / 27.29 and 13.36 / 26.13 / 42.57
  - NS: 7.01 / 19.50 / 36.47 and 21.18 / 31.59 / 45.73
  - PE: 2.69 / 15.98 / 32.81 and 19.71 / 30.78 / 44.80
  - NL: 9.91 / 20.67 / 38.33 and 18.71 / 27.68 / 42.39
- **Top-rate table.** Computed with `rates()` above the top threshold:
  - NB 32.40% / 46.83%, NS 41.58% / 49.99% and NL 46.20% / 48.96% all match.
  - Note that NL's top rate needs income over $1,141,275. At $600k the engine gives 45.51%, which is the next bracket down.
  - The ordinary-income column also matches for all six new provinces.
- **Province bracket tables.** Every row of the New Brunswick and Nova Scotia tables reproduced exactly at the row midpoint: 21 rows, covering the ordinary, eligible and other-than-eligible columns.
  - For the six new tables, the published ordinary-income column matched the engine in every row (59 rows).
  - Dividend values were computed at the row midpoint and matched rows.json in every row where the ranges line up.
  - The exception is Nunavut "Over $117,045 up to $181,440". rows.json splits this at $181,439, so its value came from the midpoint, and that equals rows.json's 117,045-181,439 row (19.97% / 26.86%).

## Changes (before -> after)
1. `Updated October 26, 2026` -> `Updated November 5, 2026`. "Figures checked October 23, 2026" was left unchanged. The page has no JSON-LD dateModified.
2. Key points: "Rates are shown for the seven provinces whose 2026 dividend credits are confirmed: Ontario, ..." -> "Rates are shown for all 13 provinces and territories."
3. Table of contents: "Manitoba and figures still being confirmed" -> "Manitoba and dividend credit sources". The anchor `#manitoba-and-pending` was kept.
4. Top-rate table, Being confirmed -> eligible / other than eligible:

   | Province | Eligible | Other than eligible |
   |---|---|---|
   | AB | 34.31% | 42.31% |
   | MB | 37.78% | 46.67% |
   | NT | 28.33% | 36.82% |
   | NU | 33.08% | 37.79% |
   | SK | 29.64% | 41.34% |
   | YT | 28.93% | 44.04% |

5. "Top rates on investment income": "from 32.40% in New Brunswick to 46.20% in NL at the top where the provincial credit is confirmed, ... other than eligible ... from 46.83% to 49.99%" -> "from 28.33% in the Northwest Territories to 46.20% in NL at the top, ... from 36.82% to 49.99%". These are the new minimums across all 13; the maximums are unchanged.
6. "How to read these tables": "Dividend columns appear for provinces whose 2026 dividend tax credit is confirmed; for the others, dividend rates are being confirmed." -> "Dividend columns appear for every province and territory."
7. to 12. Province paragraphs for Alberta, Manitoba, Northwest Territories, Nunavut, Saskatchewan and Yukon:
   - Before: "...dividend tax credit (for 2026) is being confirmed."
   - After: the brief's standard wording, e.g. "Alberta's dividend tax credit is 8.12% of the grossed-up amount for eligible dividends and 2.18% for other than eligible dividends, the rates on CRA's Worksheet AB428 (line 61520). CRA publishes the 2026 worksheet in January 2027; Alberta's 2026 budget made no change to personal income tax."
   - The NWT version reads "The territorial dividend tax credit is 11.5% ... 6% ... NT428 ...; the territory's 2026 budget ...".
13. to 18. Province bracket tables for AB, MB, NT, NU, SK and YT:
   - Added "Eligible dividends" and "Other than eligible dividends" columns between Capital gains and What changes here.
   - The headings and cell format are the same as the B.C., N.B. and N.S. tables on this page.
   - Values are engine midpoint rates, equal to rows.json (12 + 11 + 10 + 10 + 9 + 7 rows).
   - This keeps the "Dividend columns appear for every province" sentence true.
19. to 24. Dividend table at $50k / $100k / $250k (eligible x3, other than eligible x3), Being confirmed -> numbers:

   | Province | Eligible $50k | Eligible $100k | Eligible $250k | Other $50k | Other $100k | Other $250k |
   |---|---|---|---|---|---|---|
   | AB | -1.57% | 10.16% | 27.81% | 12.41% | 22.18% | 36.90% |
   | MB | 5.15% | 20.53% | 33.85% | 19.48% | 32.30% | 43.39% |
   | NT | -9.14% | 3.56% | 23.22% | 5.60% | 16.18% | 32.56% |
   | NU | -3.49% | 9.62% | 27.97% | 7.31% | 18.24% | 33.53% |
   | SK | -2.10% | 9.63% | 24.53% | 14.89% | 24.67% | 37.08% |
   | YT | -9.16% | 3.40% | 20.96% | 12.30% | 22.77% | 37.41% |

25. Calculator sentence: "in the seven provinces where the 2026 credit is confirmed." -> "in every province and territory."
26. Section 10 heading: "10. Manitoba and Figures Still Being Confirmed" -> "10. Manitoba and Dividend Credit Sources". The id was kept.
27. Section 10 paragraph:
   - Before: "Dividend credits being confirmed. ... has not yet been confirmed ... shown as being confirmed, and the dividend calculators show a note for those places. Rates on ordinary income and capital gains are complete for all 13."
   - After: "Dividend credits for the last six." It lists the six credits from CRA's 2025 worksheets (line 61520), says CRA publishes the 2026 worksheets in January 2027 and that none of the six 2026 budgets changed personal income tax, and ends "Rates on ordinary income, capital gains and dividends are complete for all 13."
   - The calculator-note sentence was removed.
28. "When figures change": "When a missing credit is confirmed or a province changes its rates" -> "When CRA publishes new worksheets or a province changes its rates".
29. FAQ (visible and JSON-LD, identical text):
   - Question: "Why are dividend rates being confirmed for some provinces?" -> "How are the provincial dividend tax credits confirmed?"
   - Answer: the last two sentences ("Confirmed rates cover Ontario, ... Alberta, Saskatchewan, Manitoba and the three territories are still being confirmed.") -> "All 13 provinces and territories are now confirmed. For Alberta, Saskatchewan, Manitoba and the three territories, we use the rates on CRA's 2025 provincial worksheets (line 61520); CRA publishes the 2026 worksheets in January 2027, and none of those six 2026 budgets changed personal income tax."

## Left unchanged
- The anchor id `manitoba-and-pending`. Changing it could break inbound links.
- "Figures checked October 23, 2026". The brief allows only the Updated line to change.
- All ON, BC and QC figures. The engine does not model them.
- Everything else is byte-identical, including the same trailing newline and LF line endings.

## Checks
- JSON check: `ok 0`. All ld+json blocks parse, and the "eing confirmed" count is 0.
