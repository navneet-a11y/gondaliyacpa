# Changes: 116-tax-yukon-tax-brackets.html (Yukon (YT))

## Changes (before -> after)

1. Updated date:
   - before: "Updated October 26, 2026"
   - after: "Updated November 5, 2026"
2. Marginal-rate table header: added two dividend columns:
   - before: "<th>Combined rate on ordinary income</th><th>Capital gains</th></tr></thead>"
   - after: "<th>Combined rate on ordinary income</th><th>Capital gains</th><th>Eligible dividends</th><th>Other than eligible dividends</th></tr></thead>"
3. Marginal-rate table rows: added eligible / other than eligible cells from rows.json:
   - Up to $16,452: ordinary 0.00% (rows.json 0.0) -> added 0.00% / 0.00%
   - Over $16,452 up to $58,523: ordinary 20.40% (rows.json 20.4) -> added -9.16% / 12.30%
   - Over $58,523 up to $117,045: ordinary 29.50% (rows.json 29.5) -> added 3.40% / 22.77%
   - Over $117,045 up to $181,440: ordinary 36.90% (rows.json 36.9) -> added 13.61% / 31.28%
   - Over $181,440 up to $258,482: ordinary 42.23% (rows.json 42.23) -> added 20.96% / 37.41%
   - Over $258,482 up to $500,000: ordinary 45.80% (rows.json 45.8) -> added 25.89% / 41.51%
   - Over $500,000: ordinary 48.00% (rows.json 48.0) -> added 28.93% / 44.04%
4. At a glance: dividends:
   - before: "<p><strong>Dividends: being confirmed.</strong> Yukon's 2026 dividend tax credit rates are not yet confirmed from an official source, so this page shows dividend marginal rates as being confirmed and the calculator asks you to leave dividends at zero for now.<..."
   - after: "<p><strong>Dividends.</strong> Yukon's dividend tax credit is 12.02% of the grossed-up amount for eligible dividends and 0.67% for other than eligible dividends, the rates on CRA's Worksheet YT428 (line 61520). Over $500,000 the combined rate is 28.93% on eligible dividends and 44.04% on other than eligible dividends, and the calculator includes both.</p>"
5. Section 3 intro: one sentence on how dividend columns are built:
   - before: "Capital gains rates are half the ordinary rates because half of a 2026 gain is taxable.</p>"
   - after: "Capital gains rates are half the ordinary rates because half of a 2026 gain is taxable. Dividend rates include the 38% and 15% gross-ups and the federal and Yukon dividend tax credits.</p>"
6. Section 3 dividend note:
   - before: "<p><strong>Dividends: being confirmed.</strong> The table leaves out dividend columns because Yukon's 2026 dividend tax credit rates are being confirmed. The federal part of dividend tax is known: eligible dividends are grossed up by 38% with a federal credit ..."
   - after: "<p><strong>Yukon's dividend tax credit.</strong> Yukon's dividend tax credit is 12.02% of the grossed-up amount for eligible dividends and 0.67% for other than eligible dividends, the rates on CRA's Worksheet YT428 (line 61520). CRA publishes the 2026 worksheet in January 2027; Yukon's 2026 budget made no change to personal income tax. Federally, eligible dividends are grossed up by 38% with a cre..."
7. Section 9 dividends paragraph:
   - before: "<p><strong>Dividends in Yukon.</strong> Yukon's 2026 dividend tax credit rates are being confirmed, so the income tax calculator asks Yukoners to leave dividends at zero and this page shows no dividend rates. The federal half of the calculation is settled: eli..."
   - after: "<p><strong>Dividends in Yukon.</strong> Yukon's dividend tax credit is 12.02% of the grossed-up amount for eligible dividends and 0.67% for other than eligible dividends, the rates on CRA's Worksheet YT428 (line 61520). The federal half is a 38% gross-up and 15.0198% credit for eligible dividends, and a 15% gross-up and 9.0301% credit for other than eligible dividends. Together they give combined ..."
8. Removed mistake paragraph: removed "<p><strong>Entering dividends before the Yukon credit is confirmed.</strong> Without Yukon's 2026 dividend tax credit, any combined dividend rate is incomplete...." (it said the calculator asks you to leave dividends at zero).
9. FAQ (visible): What is the top marginal tax rate in Yukon?:
   - before: "<details><summary>What is the top marginal tax rate in Yukon?</summary><div><p>The top combined rate is 48% on ordinary income over $500,000: 33% federal plus 15% Yukon. From $258,482 to $500,000 it is 45.8%. Capital gains are taxed at half those rates, so the..."
   - after: "<details><summary>What is the top marginal tax rate in Yukon?</summary><div><p>The top combined rate is 48% on ordinary income over $500,000: 33% federal plus 15% Yukon. From $258,482 to $500,000 it is 45.8%. Capital gains are taxed at half those rates, so the top rate on a gain is 24%. For dividends in that top band, the combined rate is 28.93% on eligible dividends and 44.04% on other than eligi..."
10. FAQ (JSON-LD): What is the top marginal tax rate in Yukon?:
   - before: ""name": "What is the top marginal tax rate in Yukon?", "acceptedAnswer": {"@type": "Answer", "text": "The top combined rate is 48% on ordinary income over $500,000: 33% federal plus 15% Yukon. From $258,482 to $500,000 it is 45.8%. Capital gains are taxed at h..."
   - after: ""name": "What is the top marginal tax rate in Yukon?", "acceptedAnswer": {"@type": "Answer", "text": "The top combined rate is 48% on ordinary income over $500,000: 33% federal plus 15% Yukon. From $258,482 to $500,000 it is 45.8%. Capital gains are taxed at half those rates, so the top rate on a gain is 24%. For dividends in that top band, the combined rate is 28.93% on eligible dividends and 44...."
11. FAQ (visible): Can I enter dividends for Yukon in the calculator?:
   - before: "<details><summary>Why can I not enter dividends for Yukon in the calculator?</summary><div><p>We have not yet been able to confirm Yukon's 2026 dividend tax credit rates from an official source. Without them, any combined dividend rate would be wrong, so the c..."
   - after: "<details><summary>Can I enter dividends for Yukon in the calculator?</summary><div><p>Yes. Yukon's dividend tax credit is 12.02% of the grossed-up amount for eligible dividends and 0.67% for other than eligible dividends, the rates on CRA's Worksheet YT428 (line 61520). The calculator combines them with the federal 38% and 15% gross-ups and the federal credits of 15.0198% and 9.0301%. CRA publishe..."
12. FAQ (JSON-LD): Can I enter dividends for Yukon in the calculator?:
   - before: ""name": "Why can I not enter dividends for Yukon in the calculator?", "acceptedAnswer": {"@type": "Answer", "text": "We have not yet been able to confirm Yukon's 2026 dividend tax credit rates from an official source. Without them, any combined dividend rate w..."
   - after: ""name": "Can I enter dividends for Yukon in the calculator?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Yukon's dividend tax credit is 12.02% of the grossed-up amount for eligible dividends and 0.67% for other than eligible dividends, the rates on CRA's Worksheet YT428 (line 61520). The calculator combines them with the federal 38% and 15% gross-ups and the federal credits of 15.0198% an..."

FAQ edits were applied identically to the visible <details> and the JSON-LD FAQPage (question name and answer text).

## Reproduce-first check

The marginal-rate table had no existing dividend cells (columns added), so the check used the same table's ordinary-income column and a published total. Engine rates() at each row midpoint reproduced every published ordinary cell exactly (0.00%, 20.40%, 29.50%, 36.90%, 42.23%, 45.80%, 48.00%), and the capital gains column matches rows.json (21.115 shown as 21.11%). Engine total(75000,'YT') = $13,443.20, matching the published $13,443.20 (hero and FAQ). Engine dividend rates at midpoints equal rows.json for every row (e.g. top band 28.93% / 44.04%). Check passed; new cells filled from rows.json.

## Left unchanged

- 'Figures checked October 23, 2026' (dates line and trust bar): left, brief says change no other dates.
- Section 5 credit table caption 'credit amounts confirmed' and the 'Other Yukon credits' / 'What this page leaves out' paragraphs mention other unconfirmed credits (age, pension, etc.), not dividend credits: left unchanged.
- Did not add dividend tax credit rows to the section 5 credits table (B.C. page has such rows); kept edits minimal.
- Page has no JSON-LD dateModified.

## Validation

JSON-LD check: `ok 0` (all ld+json blocks parse; 0 occurrences of 'eing confirmed').
