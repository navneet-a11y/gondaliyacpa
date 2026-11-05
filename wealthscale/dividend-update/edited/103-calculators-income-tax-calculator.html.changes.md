# 103-calculators-income-tax-calculator.html: changes

1. Dates line: "Updated October 26, 2026" -> "Updated November 5, 2026" ("Figures checked October 23, 2026" unchanged). No JSON-LD dateModified on the page.
2. Section "How to enter" (Dividends paragraph): "Dividend tax credit rates are confirmed for seven provinces: ... For Alberta, Saskatchewan, Manitoba and the three territories, the calculator asks you to leave dividends at zero for now." -> "Dividend tax credit rates are confirmed for all 13 provinces and territories. For Alberta, Saskatchewan, Manitoba and the three territories, the calculator uses the rates on CRA's 2025 provincial worksheets (line 61520); CRA publishes the 2026 worksheets in January 2027, and none of those six 2026 budgets changed personal income tax."
3. "Included" paragraph: "dividend tax credits in the seven provinces where 2026 rates are confirmed" -> "dividend tax credits in all 13 provinces and territories".
4. Section 8, eligible-dividend credit list: appended "8.12% in Alberta, 11% in Saskatchewan, 8% in Manitoba, 12.02% in Yukon, 11.5% in the Northwest Territories and 5.51% in Nunavut".
5. Section 8, other-than-eligible list: appended "2.18% in Alberta, 2.519% in Saskatchewan, 0.7835% in Manitoba, 0.67% in Yukon, 6% in the Northwest Territories and 2.61% in Nunavut".
6. Marginal-rates intro: "in the seven provinces with confirmed dividend credits" -> "in all 13 provinces and territories" (B.C. 1.63% at $80,000 is still the lowest eligible rate of the 13: next are Yukon 3.40%, NWT 3.56%).
7. Table caption: "...in the seven provinces with confirmed dividend credits" -> "...in all 13 provinces and territories".
8. Table: added 12 rows after Newfoundland and Labrador (each at $80,000 / $150,000; ordinary, capital gains, eligible, other than eligible):
   - Alberta 30.50/15.25/10.16/22.18; 36.00/18.00/17.75/28.51
   - Saskatchewan 33.00/16.50/9.63/24.67; 38.50/19.25/17.22/30.99
   - Manitoba 33.25/16.63/14.12/26.95; 43.40/21.70/28.12/38.62
   - Yukon 29.50/14.75/3.40/22.77; 36.90/18.45/13.61/31.28
   - Northwest Territories 29.10/14.55/3.56/16.18; 38.20/19.10/16.12/26.65
   - Nunavut 27.50/13.75/9.62/18.24; 35.00/17.50/19.97/26.86
   (engine rates(); capital gains = half ordinary rounded half-up, page convention e.g. 37.17 -> 18.59; Manitoba 33.25 -> 16.63. Ordinary rates match the page's own marginal-rate columns in section 4 for these provinces.)
9. "The other six." paragraph: "being confirmed ... asks you to leave dividends at zero there, rather than show a figure we cannot stand behind." -> standard wording for Alberta (8.12%/2.18%, Worksheet AB428, line 61520) plus the other five with worksheet codes, and "CRA publishes the 2026 worksheets in January 2027; none of the six 2026 budgets changed personal income tax." Rest of paragraph (capital gains sentence, links) unchanged.

## Reproduce-first check (marginal-rate table, next $100 at $80,000 and $150,000)
Engine vs published cells (ordinary / cap gains / eligible / other):
- New Brunswick $80,000: 34.50/17.25/7.56/26.13 = published; $150,000: 42.00/21.00/17.91/34.75 = published
- Nova Scotia $80,000: 37.17/18.59/18.35/30.64 = published; $150,000: 43.50/21.75/27.09/37.92 = published
- PEI $80,000: 37.10/18.55/15.98/30.78 = published; $150,000: 45.00/22.50/26.88/39.87 = published
- NL $80,000: 35.00/17.50/18.88/26.19 = published; $150,000: 41.80/20.90/28.26/34.01 = published
All 32 cells match exactly; new rows filled after that.

## Left unchanged
- FAQ (visible and JSON-LD): no FAQ answer mentions the six pending credits, so no FAQ edits.
- No "Being confirmed" table cells existed on this page.
- Ontario/B.C./Quebec figures not touched.
