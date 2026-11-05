# 148-vs-tfsa-vs-non-registered.html: changes

## Reproduce-first check (engine.py, AB)
Table scenario: extra 2026 tax on $4,000 of interest, $3,000 of eligible dividends or a $5,000 realized gain ($2,500 taxable) on top of taxable income x. I did not use B.C. because the engine does not model the B.C. reduction. Instead I recomputed Alberta's own interest and capital-gain cells in the same table:
- $60,000: interest $1,196.00 (published $1,196.00), gain $738.50 (published $738.50)
- $100,000: interest $1,220.00 (published $1,220.00), gain $762.50 (published $762.50)
- $175,000: interest $1,520.00 (published $1,520.00), gain $950.00 (published $950.00)
All six cells match exactly. The eligible cells are total(x, 'AB', el=3000) - total(x, 'AB') = 280.71 / 304.71 / 615.21.

## Changes (before -> after)
1. ws-dates: "Updated October 26, 2026" -> "Updated November 5, 2026" ("Figures checked" left unchanged).
2. Alberta, $60,000, $3,000 of eligible dividends: "Being confirmed" -> "$280.71".
3. Alberta, $100,000: "Being confirmed" -> "$304.71".
4. Alberta, $175,000: "Being confirmed" -> "$615.21".
5. Table note: "Alberta's 2026 dividend tax credit rate is being confirmed." -> "Alberta's dividend tax credit is 8.12% of the grossed-up amount for eligible dividends, the rate on CRA's Worksheet AB428 (line 61520). CRA publishes the 2026 worksheet in January 2027; Alberta's 2026 budget made no change to personal income tax."

## Left unchanged
- No FAQ answer or JSON-LD text mentions Alberta dividends; the page has no dateModified.
- All Ontario, B.C. and Quebec figures are untouched (the engine cannot model them).
