# Changes: 117-tax-northwest-territories-tax-brackets.html (Northwest Territories (NT))

## Changes (before -> after)

1. Updated date:
   - before: "Updated October 26, 2026"
   - after: "Updated November 5, 2026"
2. Marginal-rate table header: added two dividend columns:
   - before: "<th>Combined rate on ordinary income</th><th>Capital gains</th></tr></thead>"
   - after: "<th>Combined rate on ordinary income</th><th>Capital gains</th><th>Eligible dividends</th><th>Other than eligible dividends</th></tr></thead>"
3. Marginal-rate table rows: added eligible / other than eligible cells from rows.json:
   - Up to $16,452: ordinary 0.00% (rows.json 0.0) -> added 0.00% / 0.00%
   - Over $16,452 up to $18,198: ordinary 14.00% (rows.json 14.0) -> added -1.41% / 5.72%
   - Over $18,198 up to $53,003: ordinary 19.90% (rows.json 19.9) -> added -9.14% / 5.60%
   - Over $53,003 up to $58,523: ordinary 22.60% (rows.json 22.6) -> added -5.41% / 8.71%
   - Over $58,523 up to $106,009: ordinary 29.10% (rows.json 29.1) -> added 3.56% / 16.18%
   - Over $106,009 up to $117,045: ordinary 32.70% (rows.json 32.7) -> added 8.53% / 20.32%
   - Over $117,045 up to $172,346: ordinary 38.20% (rows.json 38.2) -> added 16.12% / 26.65%
   - Over $172,346 up to $181,440: ordinary 40.05% (rows.json 40.05) -> added 18.67% / 28.77%
   - Over $181,440 up to $258,482: ordinary 43.34% (rows.json 43.34) -> added 23.22% / 32.56%
   - Over $258,482: ordinary 47.05% (rows.json 47.05) -> added 28.33% / 36.82%
4. At a glance: dividends:
   - before: "<p><strong>Dividends: being confirmed.</strong> Until the territory's 2026 dividend tax credit is confirmed from an official source, this page lists dividend rates as being confirmed, and the calculator asks you to enter zero dividends.</p>"
   - after: "<p><strong>Dividends.</strong> The Northwest Territories' dividend tax credit is 11.5% of the grossed-up amount for eligible dividends and 6% for other than eligible dividends, the rates on CRA's Worksheet NT428 (line 61520). Over $258,482 the combined rate is 28.33% on eligible dividends and 36.82% on other than eligible dividends, and the calculator includes both.</p>"
5. Section 3 intro: one sentence on how dividend columns are built:
   - before: "including the effect of the shrinking federal basic personal amount between $181,440 and $258,482. Capital gains rates are half the ordinary rate.</p>"
   - after: "including the effect of the shrinking federal basic personal amount between $181,440 and $258,482. Capital gains rates are half the ordinary rate. Dividend rates include the 38% and 15% gross-ups and the federal and territorial dividend tax credits.</p>"
6. Section 3 dividend note:
   - before: "<p><strong>Dividends: being confirmed.</strong> The table has no dividend columns because the Northwest Territories' 2026 dividend tax credit rates are not yet confirmed from an official source. Only the federal side is fixed so far: eligible dividends carry a..."
   - after: "<p><strong>The territorial dividend tax credit.</strong> The Northwest Territories' dividend tax credit is 11.5% of the grossed-up amount for eligible dividends and 6% for other than eligible dividends, the rates on CRA's Worksheet NT428 (line 61520). CRA publishes the 2026 worksheet in January 2027; the territory's 2026 budget made no change to personal income tax. On the federal side, eligible d..."
7. Section 9 dividends paragraph:
   - before: "<p><strong>Dividends.</strong> The NWT's 2026 dividend tax credit rates are being confirmed, so this page shows no combined dividend rate and the income tax calculator asks you to leave dividends at zero for the Northwest Territories. The federal gross-up and ..."
   - after: "<p><strong>Dividends.</strong> The Northwest Territories' dividend tax credit is 11.5% of the grossed-up amount for eligible dividends and 6% for other than eligible dividends, the rates on CRA's Worksheet NT428 (line 61520). The federal gross-up and credit are 38% and 15.0198% for eligible dividends, 15% and 9.0301% for other than eligible dividends. Combined, eligible dividends are taxed from -9..."
8. Removed mistake paragraph: removed "<p><strong>Entering dividends before the NWT credit is confirmed.</strong> Without the territorial dividend tax credit, any combined dividend result would be wr..." (it said the calculator asks you to leave dividends at zero).
9. FAQ (visible): What is the top marginal tax rate in the Northwest Territories?:
   - before: "<details><summary>What is the top marginal tax rate in the Northwest Territories?</summary><div><p>The top combined rate is 47.05% on ordinary income over $258,482: 33% federal plus 14.05% territorial. From $181,440 to $258,482 it is 43.34%. Because only half ..."
   - after: "<details><summary>What is the top marginal tax rate in the Northwest Territories?</summary><div><p>The top combined rate is 47.05% on ordinary income over $258,482: 33% federal plus 14.05% territorial. From $181,440 to $258,482 it is 43.34%. Because only half a gain is taxable, a capital gain at the top pays 23.525%. Eligible dividends at the top are taxed at 28.33% and other than eligible dividen..."
10. FAQ (JSON-LD): What is the top marginal tax rate in the Northwest Territories?:
   - before: ""name": "What is the top marginal tax rate in the Northwest Territories?", "acceptedAnswer": {"@type": "Answer", "text": "The top combined rate is 47.05% on ordinary income over $258,482: 33% federal plus 14.05% territorial. From $181,440 to $258,482 it is 43...."
   - after: ""name": "What is the top marginal tax rate in the Northwest Territories?", "acceptedAnswer": {"@type": "Answer", "text": "The top combined rate is 47.05% on ordinary income over $258,482: 33% federal plus 14.05% territorial. From $181,440 to $258,482 it is 43.34%. Because only half a gain is taxable, a capital gain at the top pays 23.525%. Eligible dividends at the top are taxed at 28.33% and othe..."
11. FAQ (visible): Can I calculate dividend tax for the NWT?:
   - before: "<details><summary>Can I calculate dividend tax for the NWT?</summary><div><p>Not yet. The territory's 2026 dividend tax credit rates have not been confirmed from an official source, so the calculator asks you to leave dividends at zero for the NWT. The federal..."
   - after: "<details><summary>Can I calculate dividend tax for the NWT?</summary><div><p>Yes. The Northwest Territories' dividend tax credit is 11.5% of the grossed-up amount for eligible dividends and 6% for other than eligible dividends, the rates on CRA's Worksheet NT428 (line 61520). The calculator combines them with the federal 38% and 15% gross-ups and the federal credits. CRA publishes the 2026 workshe..."
12. FAQ (JSON-LD): Can I calculate dividend tax for the NWT?:
   - before: ""name": "Can I calculate dividend tax for the NWT?", "acceptedAnswer": {"@type": "Answer", "text": "Not yet. The territory's 2026 dividend tax credit rates have not been confirmed from an official source, so the calculator asks you to leave dividends at zero f..."
   - after: ""name": "Can I calculate dividend tax for the NWT?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. The Northwest Territories' dividend tax credit is 11.5% of the grossed-up amount for eligible dividends and 6% for other than eligible dividends, the rates on CRA's Worksheet NT428 (line 61520). The calculator combines them with the federal 38% and 15% gross-ups and the federal credits. CRA pub..."

FAQ edits were applied identically to the visible <details> and the JSON-LD FAQPage (question name and answer text).

## Reproduce-first check

No existing dividend cells (columns added). Engine rates() at each row midpoint reproduced every published ordinary cell exactly (0.00%, 14.00%, 19.90%, 22.60%, 29.10%, 32.70%, 38.20%, 40.05%, 43.34%, 47.05%); capital gains column matches rows.json. Engine total(75000,'NT') = $13,212.96, matching the published $13,212.96 (At a glance). Engine dividend rates at midpoints equal rows.json for every row (top band 28.33% / 36.82%). Check passed.

## Left unchanged

- 'Figures checked October 23, 2026': left (change no other dates).
- Section 5 caption and 'Other territorial credits' / 'What this page leaves out' paragraphs refer to other credits, not dividend credits: left.
- No dividend rows added to the section 5 credits table (minimal edits).
- Page has no JSON-LD dateModified.

## Validation

JSON-LD check: `ok 0` (all ld+json blocks parse; 0 occurrences of 'eing confirmed').
