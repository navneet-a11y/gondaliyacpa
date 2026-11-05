# 147-accounts-non-registered-account.html: changes

Source: pages-paste/147-accounts-non-registered-account.html. Edit script: scratchpad/ed/e147.py (exact string replacements; new cells computed with engine.py).

## Reproduce-first check (engine.py)
Table "2026 tax on $1,000 of investment income at $90,000 of taxable income, every province and territory". Scenario: $1,000 of each income type on top of $90,000 of taxable income; tax = total(90000, p, el/ne=1000) - total(90000, p).
- New Brunswick: eligible $75.63, other $261.28 (published $75.63 / $261.28). Match.
- Newfoundland and Labrador: $206.73 / $276.80 (published the same). Match.
- Nova Scotia: $183.54 / $306.36. Match. PEI: $159.81 / $307.80. Match.
- Each of the six provinces' own interest and capital gain cells also matches: AB $305.00 / $152.50, MB $332.50 / $166.25, NT $291.00 / $145.50, NU $275.00 / $137.50, SK $330.00 / $165.00, YT $295.00 / $147.50.

## Changes (before -> after)
1. Byline: "Updated October 26, 2026" -> "Updated November 5, 2026". The "Figures checked" date was not changed.
2. Section 3 paragraph: "The table lists the 2026 provincial rates confirmed so far; the rates for Alberta, Manitoba, Saskatchewan and the three territories are being confirmed, so our dividend calculator does not yet cover them." -> "The table lists the 2026 provincial rates. For Alberta, Manitoba, Saskatchewan and the three territories they are the rates on CRA's 2025 provincial worksheets (line 61520); CRA publishes the 2026 worksheets in January 2027, and none of the six 2026 budgets changed personal income tax."
3. Dividend tax credit rates table: the shared row "Alberta, Manitoba, Saskatchewan, Yukon, Northwest Territories, Nunavut | Being confirmed | Being confirmed" was removed. Six rows in the same format were inserted in alphabetical order, which the rest of the table uses (Federal first, then alphabetical; the same order as the page's every-province table): Alberta 8.12% / 2.18%; Manitoba 8% / 0.7835%; Northwest Territories 11.5% / 6%; Nunavut 5.51% / 2.61%; Saskatchewan 11% / 2.519%; Yukon 12.02% / 0.67%.
4. Every-province table at $90,000, "Being confirmed" -> engine values (eligible / other than eligible):
   - Alberta $101.57 / $221.83
   - Manitoba $141.18 / $269.52
   - Northwest Territories $35.61 / $161.80
   - Nunavut $96.19 / $182.39
   - Saskatchewan $96.33 / $246.69
   - Yukon $33.95 / $227.70
5. Note under that table: the sentence '"Being confirmed" means the 2026 provincial dividend tax credit rate has not yet been verified.' was removed. The Quebec abatement sentence was kept.

## Left unchanged, and why
- The paragraph "What the tables show" is still true with the new rows: interest is still the highest in every row, and eligible dividends are below capital gains in all six. It was not edited.
- The Ontario and B.C. tables by income have no "Being confirmed" cells and were not touched.
- No FAQ or JSON-LD text referred to these credits, so the JSON-LD was not changed.

## Check
`ok 0`: the JSON-LD parses, and 0 "being confirmed" remain.
