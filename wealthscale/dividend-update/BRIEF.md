# Brief: add the six confirmed 2026 dividend tax credits to WealthScale pages

You edit page files LOCALLY only. Do not publish, do not call any WordPress or website tool.

## The facts (confirmed)

Provincial and territorial dividend tax credit rates, as a percent of the grossed-up (taxable) dividend:

| Province | Eligible | Other than eligible | CRA source (2025 worksheet, line 61520) |
|---|---|---|---|
| Alberta | 8.12% | 2.18% | Worksheet AB428 |
| Saskatchewan | 11% | 2.519% | Worksheet SK428 |
| Manitoba | 8% | 0.7835% | Worksheet MB428 |
| Yukon | 12.02% | 0.67% | Worksheet YT428 |
| Northwest Territories | 11.5% | 6% | Worksheet NT428 |
| Nunavut | 5.51% | 2.61% | Worksheet NU428 |

These are the rates on CRA's 2025 provincial worksheets. CRA publishes the 2026 worksheets in January 2027; none of the six 2026 budgets changed personal income tax, so the pages use them as the 2026 rates. Standard wording to use where a page explains the source (adapt the province name; keep it short):

> "Alberta's dividend tax credit is 8.12% of the grossed-up amount for eligible dividends and 2.18% for other than eligible dividends, the rates on CRA's Worksheet AB428 (line 61520). CRA publishes the 2026 worksheet in January 2027; Alberta's 2026 budget made no change to personal income tax."

All 13 provinces and territories are now confirmed. Any sentence that lists "seven provinces" whose credits are confirmed, or says the others are "being confirmed" / "not yet verified" / "pending", must be updated so it is true now.

## The numbers: always use the engine

`/home/user/gondaliyacpa/wealthscale/dividend-update/engine.py` reproduces the site's own tax method (verified against the site's published B.C., Alberta, N.B., N.S., P.E.I. and N.L. figures to 0.01%). Use it for every number you add:

```python
import sys; sys.path.insert(0, '/home/user/gondaliyacpa/wealthscale/dividend-update')
from engine import rates, total
o, e, n = rates(x, 'AB')          # marginal rates at taxable income x: ordinary, eligible dividend, other-than-eligible dividend (per $1 of actual dividend)
tax = total(x, 'AB', el=1000) - total(x, 'AB')   # extra tax on $1,000 of eligible dividends at income x (use ne= for other than eligible)
```

`rows.json` in the same folder holds the full bracket-by-bracket table for the six provinces: `[from, to, ordinary %, capital gains %, eligible %, other-than-eligible %]`. Use these for bracket tables; if a page's row ranges differ, compute at the row midpoint with `rates()`.

Province codes: AB, SK, MB, YT, NT, NU. The engine does NOT model the Ontario surtax/Health Premium, the B.C./Ontario reductions or the Quebec abatement, so never use it to recompute ON, BC or QC figures.

**Reproduce first.** Before filling any "Being confirmed" cell in a table, recompute one or two existing cells in the SAME table for New Brunswick, Nova Scotia, Prince Edward Island or Newfoundland and Labrador (or the same province's ordinary-income column) with the engine, using the scenario the table uses (income level, amount). Only fill the new cells once your recomputation matches the published cell exactly. Record this check in your change log. If you cannot work out the table's scenario, do NOT guess: leave the cell and say so in the change log.

Format new numbers exactly like the neighbouring cells (same decimals, % or $, minus sign style such as "-1.41%").

## Editing rules

- Minimal, surgical edits. Change only text and cells that depend on these six credits. Do not rewrite other content, reorder sections, or "fix" anything else.
- Replace "Being confirmed" cells with numbers; replace "being confirmed" sentences with the confirmed facts; remove notes that say a calculator "asks you to leave dividends at zero" for these provinces (the calculators now handle them).
- Province pages that say they show no dividend rates yet (Manitoba, Saskatchewan, Yukon, NWT, Nunavut): replace those sentences with the credit rates and the top combined rates; you MAY add "Eligible dividends" and "Other than eligible dividends" columns to the main combined-rate table, using the same column headings and cell style as the Alberta page's table, with values from rows.json.
- FAQ: if a visible FAQ answer changes, make the identical change in the JSON-LD FAQPage block (same text, JSON-escaped). Every `<script type="application/ld+json">` block must still parse as JSON.
- If the page shows an "Updated <date>" line or a JSON-LD dateModified, set it to November 5, 2026 / 2026-11-05. Change no other dates.
- Keep the file otherwise byte-identical: same HTML structure, same classes, no reformatting, no trailing-newline changes.

## Output

For each page file you are given:
1. Write the edited file to `/home/user/gondaliyacpa/wealthscale/dividend-update/edited/<same file name>`.
2. Write `/home/user/gondaliyacpa/wealthscale/dividend-update/edited/<file name>.changes.md`: every change as before -> after (short), the reproduce-first checks with numbers, and anything you left unchanged and why.
3. Run: `python3 -I -c "import re,json,sys;t=open(sys.argv[1]).read();[json.loads(s) for s in re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>',t,re.S)];print('ok', t.count('eing confirmed'))" <edited file>` and report the result.

Report back: per page, number of changes, the reproduce-first check result, the remaining count of "being confirmed" (and why any remain), and the JSON check result.
