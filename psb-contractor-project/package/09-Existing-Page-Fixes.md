# Existing Page Fixes and Rate Correction Rules

These are the only approved changes to existing pages. Everything else on the site stays as it is during the PSB project. Kindly send each before and after to Sharad for CPA review before you update the live page, and update the FAQ JSON-LD wherever the visible FAQ text changes.

## Week 1 fixes (Sharad review by Tuesday, October 6; live by Thursday, October 8, 2026)

Responsible person: Navneet.

| # | URL | Location | Current text | Corrected text |
|---|---|---|---|---|
| 1 | /employee-vs-contractor-cost-calculator/ | Guide, PSB paragraph | pays corporate tax at 33.5% in Ontario | pays corporate tax at 44.5% in Ontario |
| 2 | /employee-vs-contractor-cost-calculator/ | FAQ answer and FAQ JSON-LD (2 places) | taxed as a personal services business at 33.5% in Ontario | taxed as a personal services business at 44.5% in Ontario |
| 3 | /should-mortgage-broker-incorporate-canada/ | Rate table, row 1 | Federal Small Business Deduction: 15% | Federal Small Business Rate: 9% |
| 4 | /should-mortgage-broker-incorporate-canada/ | Rate table, row 2 | Provincial – Ontario Small Business: 3.2% | Provincial, Ontario Small Business: 2.2% (3.2% before July 1, 2026) |
| 5 | /should-mortgage-broker-incorporate-canada/ | Rate table, row 3 | Combined CCPC Rate: 18.2% | Combined CCPC Rate: 11.2% (12.2% before July 1, 2026) |
| 6 | /should-mortgage-broker-incorporate-canada/ | Paragraph above the table | up to $600K federally | up to $500K federally |
| 7 | /should-mortgage-broker-incorporate-canada/ | Metric tile | 12.2% | 11.2% |
| 8 | /should-mortgage-broker-incorporate-canada/ | Comparison paragraph | about 12.2% on active business income | about 11.2% on active business income |
| 9 | /should-mortgage-broker-incorporate-canada/ | Corporate rates section | most CCPCs pay about 12.2% tax | most CCPCs pay about 11.2% tax |
| 10 | /should-mortgage-broker-incorporate-canada/ | Comparison table cell | Corporate small-business rate (~12%) | Corporate small-business rate (~11%) |
| 11 | /should-mortgage-broker-incorporate-canada/ | FAQ and FAQ JSON-LD | small business tax rate around 12.2% on qualifying | small business tax rate around 11.2% on qualifying |
| 12 | /acupuncturist-tax-planning-canada/ | FAQ and FAQ JSON-LD (the JSON-LD uses a curly apostrophe in Ontario’s) | small business corporate tax rate is 3.2%, while the general corporate tax rate is about 12.5%. | small business corporate tax rate is 2.2% from July 1, 2026 (3.2% before), while the general corporate tax rate is 11.5%. |
| 13 | /acupuncturist-tax-planning-canada/ | Key Numbers list, line 1 | Ontario Small Business Corporate Tax Rate: 3.2% | Ontario Small Business Corporate Tax Rate: 2.2% (from July 1, 2026) |
| 14 | /acupuncturist-tax-planning-canada/ | Key Numbers list, line 2 | General Corporate Tax Rate (Ontario): 12.5% | General Corporate Tax Rate (Ontario): 11.5% |
| 15 | /acupuncturist-tax-planning-canada/ | 2026 Update callout | an Ontario small business rate of 3.2% and a general rate of about 12.5%, | an Ontario small business rate of 2.2% from July 1, 2026 and a general rate of 11.5%, |
| 16 | /acupuncturist-tax-planning-canada/ | FAQ, Key Numbers and JSON-LD (3 places) | $600,000 | $500,000 |
| 17 | /team/sharad-gondaliya-cpa/ | Organization schema | "postalCode": "M5H 4C9" | "postalCode": "M5C 1R6" |
| 18 | /accountant-for-truck-dispatch-businesses/ | Service card, FAQ and FAQ JSON-LD | about 12.2% up to the $500,000 business limit | about 11.2% up to the $500,000 business limit |
| 19 | /accountant-for-truck-dispatch-businesses/ | Service card, FAQ and FAQ JSON-LD | taxed at roughly 12.2% in Ontario | taxed at roughly 11.2% in Ontario |
| 20 | /accountant-for-customs-brokers/ | Service card, FAQ and FAQ JSON-LD | taxed in Ontario at roughly 12.2% combined | taxed in Ontario at roughly 11.2% combined |
| 21 | /accountant-for-customs-brokers/ | Service card, FAQ and FAQ JSON-LD | pays roughly 12.2% combined in Ontario | pays roughly 11.2% combined in Ontario |
| 22 | All accountant-for-* pages carrying the repeated template sentence (exact-sentence replace only) | Service card, FAQ and FAQ JSON-LD | We set the salary-versus-dividend mix for the owners, paying enough T4 salary to build RRSP room while the balance flows as dividends, so combined tax stays near the 12.2% Ontario small-business rate instead of 53.53%. | We set the salary-versus-dividend mix for the owners, paying enough T4 salary to build RRSP room while the balance flows as dividends, so combined tax stays near the 11.2% Ontario small-business rate instead of 53.53%. |
| 23 | Page template for all new accountant-for-* pages | Template text | Any 12.2% stated as the current Ontario small business rate | 11.2%, effective for every new page from Monday, October 5, 2026 |

Row 22 is an exact-sentence replacement. Kindly run a dry run first and send Sharad the list of URLs it will change. Do not replace the bare text "12.2%" anywhere.

## Rate correction project (Monday, October 26 to Friday, November 6, 2026)

About 400 existing URLs still show 12.2% or 3.2% as the current rate. Responsible person: Navneet. Each URL is corrected individually with these rules. Navneet sends the before and after to Sharad in daily batches of 50 URLs from Monday, October 26, Sharad approves each batch within one business day, and every corrected URL is live by Friday, November 6, 2026.

| # | Where the figure appears | Action |
|---|---|---|
| 1 | 12.2% stated as the current combined Ontario small business rate | Change to 11.2% and add "(12.2% before July 1, 2026)" once per page |
| 2 | 3.2% stated as the current Ontario small business rate | Change to 2.2% and add "(3.2% before July 1, 2026)" once per page |
| 3 | 12.2% or 3.2% tied to 2025 or an earlier year, or to income earned before July 1, 2026 | Leave as is |
| 4 | Dollar figures worked out from 12.2%, for example tax of $12,200 on $100,000 | Recalculate at 11.2%, for example $11,200 on $100,000, and send to Sharad before updating |
| 5 | An example for a December 31, 2026 year-end | Use the blended 11.70% |
| 6 | Calculators with 0.122 or 0.032 in the code | Navneet replaces the rate with the day-prorated logic used in the page 7 calculator |
| 7 | Small business limit shown as $600,000 | Change to $500,000 |
| 8 | Every changed URL | Sharad CPA review before update; FAQ JSON-LD updated to match the visible text |
