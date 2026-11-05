# Changes: 118-tax-nunavut-tax-brackets.html (Nunavut (NU))

## Changes (before -> after)

1. Updated date:
   - before: "Updated October 26, 2026"
   - after: "Updated November 5, 2026"
2. Marginal-rate table header: added two dividend columns:
   - before: "<th>Combined rate on ordinary income</th><th>Capital gains</th></tr></thead>"
   - after: "<th>Combined rate on ordinary income</th><th>Capital gains</th><th>Eligible dividends</th><th>Other than eligible dividends</th></tr></thead>"
3. Marginal-rate table rows: added eligible / other than eligible cells from rows.json:
   - Up to $16,452: ordinary 0.00% (rows.json 0.0) -> added 0.00% / 0.00%
   - Over $16,452 up to $19,659: ordinary 14.00% (rows.json 14.0) -> added -1.41% / 5.72%
   - Over $19,659 up to $55,801: ordinary 18.00% (rows.json 18.0) -> added -3.49% / 7.31%
   - Over $55,801 up to $58,523: ordinary 21.00% (rows.json 21.0) -> added 0.65% / 10.76%
   - Over $58,523 up to $111,602: ordinary 27.50% (rows.json 27.5) -> added 9.62% / 18.24%
   - Over $111,602 up to $117,045: ordinary 29.50% (rows.json 29.5) -> added 12.38% / 20.54%
   - Over $117,045 up to $181,439: ordinary 35.00% (rows.json 35.0) -> added 19.97% / 26.86%
   - Over $181,440 up to $258,482: ordinary 40.79% (rows.json 40.79) -> added 27.97% / 33.53%
   - Over $258,482: ordinary 44.50% (rows.json 44.5) -> added 33.08% / 37.79%
4. At a glance: dividends:
   - before: "<p><strong>Dividends: being confirmed.</strong> We are still confirming Nunavut's 2026 dividend tax credit from an official source. Until then, dividend rates on this page read as being confirmed and the calculator takes zero dividends.</p>"
   - after: "<p><strong>Dividends.</strong> Nunavut's dividend tax credit is 5.51% of the grossed-up amount for eligible dividends and 2.61% for other than eligible dividends, the rates on CRA's Worksheet NU428 (line 61520). Over $258,482 the combined rate is 33.08% on eligible dividends and 37.79% on other than eligible dividends, and the calculator includes both.</p>"
5. Section 3 intro: one sentence on how dividend columns are built:
   - before: "with the matching capital gains rate, which is half the ordinary rate because half of a 2026 gain is taxable.</p>"
   - after: "with the matching capital gains rate, which is half the ordinary rate because half of a 2026 gain is taxable. Dividend rates include the 38% and 15% gross-ups and the federal and Nunavut dividend tax credits.</p>"
6. Section 3 dividend note:
   - before: "<p><strong>Dividends: being confirmed.</strong> Dividend columns are missing for now, as Nunavut's 2026 credit rates are still being confirmed. On the federal side, an eligible dividend is grossed up by 38% and earns a credit of 15.0198% of the grossed-up amou..."
   - after: "<p><strong>Nunavut's dividend tax credit.</strong> Nunavut's dividend tax credit is 5.51% of the grossed-up amount for eligible dividends and 2.61% for other than eligible dividends, the rates on CRA's Worksheet NU428 (line 61520). CRA publishes the 2026 worksheet in January 2027; Nunavut's 2026 budget made no change to personal income tax. On the federal side, an eligible dividend is grossed up b..."
7. Section 9 dividends paragraph:
   - before: "<p><strong>Dividends.</strong> Nunavut's 2026 dividend tax credit rates are being confirmed. The calculator asks you to leave dividends at zero for Nunavut, and this page shows no combined dividend rate yet. Federal dividend rules are unaffected: the 38% and 1..."
   - after: "<p><strong>Dividends.</strong> Nunavut's dividend tax credit is 5.51% of the grossed-up amount for eligible dividends and 2.61% for other than eligible dividends, the rates on CRA's Worksheet NU428 (line 61520). With the federal 38% and 15% gross-ups and the 15.0198% and 9.0301% federal credits, eligible dividends are taxed from -3.49% between $19,659 and $55,801 to 33.08% over $258,482, and other..."
8. Removed mistake paragraph: removed "<p><strong>Entering dividends before the Nunavut credit is confirmed.</strong> Any combined dividend figure without Nunavut's 2026 credit would be wrong. The ca..." (it said the calculator asks you to leave dividends at zero).
9. FAQ (visible): What is the top marginal tax rate in Nunavut?:
   - before: "<details><summary>What is the top marginal tax rate in Nunavut?</summary><div><p>The top combined rate is 44.5% on ordinary income over $258,482: 33% federal plus 11.5% Nunavut. From $181,440 to $258,482 it is 40.79%. The top rate on capital gains is 22.25%. D..."
   - after: "<details><summary>What is the top marginal tax rate in Nunavut?</summary><div><p>The top combined rate is 44.5% on ordinary income over $258,482: 33% federal plus 11.5% Nunavut. From $181,440 to $258,482 it is 40.79%. The top rate on capital gains is 22.25%. At the top, eligible dividends are taxed at 33.08% and other than eligible dividends at 37.79%.</p></div></details>"
10. FAQ (JSON-LD): What is the top marginal tax rate in Nunavut?:
   - before: ""name": "What is the top marginal tax rate in Nunavut?", "acceptedAnswer": {"@type": "Answer", "text": "The top combined rate is 44.5% on ordinary income over $258,482: 33% federal plus 11.5% Nunavut. From $181,440 to $258,482 it is 40.79%. The top rate on cap..."
   - after: ""name": "What is the top marginal tax rate in Nunavut?", "acceptedAnswer": {"@type": "Answer", "text": "The top combined rate is 44.5% on ordinary income over $258,482: 33% federal plus 11.5% Nunavut. From $181,440 to $258,482 it is 40.79%. The top rate on capital gains is 22.25%. At the top, eligible dividends are taxed at 33.08% and other than eligible dividends at 37.79%."}"
11. FAQ (visible): Can I enter dividends for Nunavut?:
   - before: "<details><summary>Why can I not enter dividends for Nunavut?</summary><div><p>Because no official source we use yet confirms Nunavut's 2026 dividend tax credit, the calculator asks for zero dividends when Nunavut is selected. We know the federal gross-ups of 3..."
   - after: "<details><summary>Can I enter dividends for Nunavut?</summary><div><p>You can. Nunavut's dividend tax credit is 5.51% of the grossed-up amount for eligible dividends and 2.61% for other than eligible dividends, the rates on CRA's Worksheet NU428 (line 61520). The calculator combines them with the federal 38% and 15% gross-ups and the federal credits. CRA publishes the 2026 worksheet in January 202..."
12. FAQ (JSON-LD): Can I enter dividends for Nunavut?:
   - before: ""name": "Why can I not enter dividends for Nunavut?", "acceptedAnswer": {"@type": "Answer", "text": "Because no official source we use yet confirms Nunavut's 2026 dividend tax credit, the calculator asks for zero dividends when Nunavut is selected. We know the..."
   - after: ""name": "Can I enter dividends for Nunavut?", "acceptedAnswer": {"@type": "Answer", "text": "You can. Nunavut's dividend tax credit is 5.51% of the grossed-up amount for eligible dividends and 2.61% for other than eligible dividends, the rates on CRA's Worksheet NU428 (line 61520). The calculator combines them with the federal 38% and 15% gross-ups and the federal credits. CRA publishes the 2026 w..."

FAQ edits were applied identically to the visible <details> and the JSON-LD FAQPage (question name and answer text).

## Reproduce-first check

No existing dividend cells (columns added). Engine rates() at each row midpoint reproduced every published ordinary cell exactly (0.00%, 14.00%, 18.00%, 21.00%, 27.50%, 29.50%, 35.00%, 40.79%, 44.50%); capital gains column matches rows.json (20.397 shown as 20.40%). Engine total(100000,'NU') = $18,932.33 vs published $18,932.34: the page rounds federal ($14,392.73) and territorial ($4,539.61) separately before adding, a one-cent rounding difference, not a method difference. Engine dividend rates at midpoints equal rows.json for every row (top band 33.08% / 37.79%). The page's table omits the one-dollar $181,439-$181,440 band, so its rows.json row (26.32% / 31.88%) was not used. Check passed.

## Left unchanged

- 'Figures checked October 23, 2026': left (change no other dates).
- Calculator intro sentence ('the marginal rate on wages and on capital gains') left: still true, not a dividend-pending statement.
- Section 5 caption and 'Other Nunavut credits' / 'Limits of these figures' paragraphs refer to other credits: left.
- No dividend rows added to the section 5 credits table (minimal edits).
- Page has no JSON-LD dateModified.

## Validation

JSON-LD check: `ok 0` (all ld+json blocks parse; 0 occurrences of 'eing confirmed').
