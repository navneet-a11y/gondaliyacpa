# 108-tax-alberta-tax-brackets.html: changes

## Reproduce-first checks (engine.py, AB)
- Combined marginal rate table (rates() at band midpoints): the ordinary column reproduced exactly in all 12 bands (0.00, 14.00, 22.00, 28.50, 30.50, 36.00, 38.00, 41.29, 42.29, 43.29, 47.00, 48.00), and so did the capital gains column. rows.json matches the engine.
- "Extra tax on $10,000 at $70,000" table: interest total(80000)-total(70000) = $3,050.00 (published $3,050.00); capital gain total(75000)-total(70000) = $1,525.00 (published $1,525.00). Exact match.
- Other cross-checks: total tax $75,000 = $13,722.21 and $100,000 = $21,347.21, both matching the page.

## Changes (before -> after)
1. ws-dates: "Updated October 26, 2026" -> "Updated November 5, 2026" ("Figures checked October 23, 2026" left unchanged).
2. Trust strip: "Alberta dividend rates shown only once confirmed" -> "Alberta dividend rates confirmed from CRA's Worksheet AB428" (the "Unverified rates left out" heading is kept).
3. At a glance, top combined rate: "Combined rates for dividends are being confirmed, because ... not yet been verified." -> "At that level eligible dividends are taxed at 34.31% and other than eligible dividends at 42.31%."
4. Combined marginal rate table: 24 "Being confirmed" cells -> values from rows.json (eligible / other than eligible): 0.00%/0.00%, -1.41%/5.72%, -1.57%/12.41%, 7.40%/19.88%, 10.16%/22.18%, 17.75%/28.51%, 20.51%/30.81%, 25.05%/34.60%, 26.43%/35.75%, 27.81%/36.90%, 32.93%/41.16%, 34.31%/42.31%.
5. Paragraph under the table: "Why dividend rates say being confirmed. ... We have not yet verified ... until the rates are confirmed." -> "Where the dividend rates come from. ... Alberta's dividend tax credit is 8.12% ... and 2.18% ..., the rates on CRA's Worksheet AB428 (line 61520). CRA publishes the 2026 worksheet in January 2027; Alberta's 2026 budget made no change to personal income tax." The federal gross-up sentence is unchanged.
6. Checklist: "Dividends received (dividend rates for Alberta are being confirmed)" -> "Dividends received".
7. Credits table row: "Being confirmed | 2026 rates not yet verified from an official source" -> "8.12% eligible, 2.18% other than eligible | Percent of the grossed-up dividend, from CRA's Worksheet AB428 (line 61520)".
8. $10,000 investment-income table: eligible ($13,800) "Being confirmed" x2 -> "$1,015.71" / "10.16%"; other than eligible ($11,500) -> "$2,218.34" / "22.18%" (engine: total(70000, el=10000) - total(70000) = 1,015.7076; ne = 2,218.3385).
9. "Reading the comparison": "Dividend figures depend on ... which we will add once the 2026 rates are verified. The dividend tax calculator covers the provinces where the credit is confirmed." -> "Dividends cost less again after Alberta's dividend tax credit of 8.12% (eligible) and 2.18% (other than eligible) of the grossed-up amount: $1,015.71 and $2,218.34 on the same $10,000. The dividend tax calculator covers every province and territory."
10. Common mistakes: "Using a dividend rate that is not confirmed. ... still being confirmed ..." -> "Applying the dividend credit to the cash dividend. Alberta's dividend tax credit is 8.12% ... and 2.18% ..., but of the grossed-up amount, not the cash received: $13,800 for $10,000 of eligible dividends and $11,500 for $10,000 of other than eligible dividends." (The old mistake no longer applies, so it was replaced with a credit-dependent one rather than deleted, which keeps the list structure.)
11. FAQ "What is the top tax rate in Alberta in 2026?" (visible and JSON-LD): "Combined dividend rates are being confirmed, ..." -> "Eligible dividends at that level are taxed at 34.31% and other than eligible dividends at 42.31%."
12. FAQ question (visible summary and JSON-LD name): "Why does this page not show Alberta dividend tax rates?" -> "What is Alberta's dividend tax credit for 2026?"; answer (visible and JSON-LD): the not-verified text -> the standard wording (8.12% / 2.18%, Worksheet AB428 line 61520, January 2027 publication, no 2026 budget change). The last sentence, "The federal gross-ups and credits are verified and explained in our dividend tax credit guide.", is kept.

## Left unchanged
- "Figures checked October 23, 2026" and the ws-checked line: other dates, per the brief.
- Credits table caption "with verified 2026 figures" and the heading "Unverified rates left out": still accurate.
- "Alberta has its own provincial versions of several of these, whose 2026 amounts we have not yet verified" (line ~196): about other credits, not the dividend credit.
- The page has no JSON-LD dateModified.
