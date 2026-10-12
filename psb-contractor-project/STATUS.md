# PSB Contractor Project: Status

Last update: Monday, October 12, 2026 (evening). Source of truth: `package/`. Slugs, titles and figures are used exactly as given.

## The 20 drafts (all status: draft, built October 12)

All 20 are in WordPress as raw HTML (the same build style as existing pages), wrapped in `.psb-cluster` with the table gridline CSS inline. Each has:
- the H1
- the "Written by" line and "Last updated" date
- the copy, with internal links
- the Trustindex widget (pages only, `loader.js?3d7613063935419a40268ae9f69`, the same widget as 114 existing pages)
- the FAQs
- the "Reviewed by" line
- the JSON-LD inline

Page 7 has the calculator. Posts: author Sharad, categories Blog and Corporate Tax.

Checks:
- The stored content length on the server matches the source file byte for byte on all 20.
- The visible text matches the package copy word for word on all 20.
- The FAQ text matches the FAQ JSON-LD on all 20.
- Calculator: $18,144, $76,095 and 11.70%, with no horizontal scroll at 360px.

The IDs, preview links, focus keywords, SEO titles and meta descriptions are in `build/drafts-table.md`.

| # | ID | Slug |
|---|---|---|
| Page 1 | 57063 | /psb-risk-incorporated-contractors/ |
| Page 2 | 57084 | /accountant-for-it-contractors/ |
| Page 3 | 57086 | /accountant-for-finance-contractors/ |
| Page 4 | 57087 | /40-hour-contract-psb-risk/ |
| Page 5 | 57083 | /contract-review-psb-indicators/ |
| Page 6 | 57085 | /staffing-agency-contractor-tax/ |
| Page 7 | 57088 | /psb-tax-cost-calculator/ |
| Page 8 | 57089 | /salary-vs-dividend-incorporated-contractor/ |
| Page 9 | 57094 | /cra-psb-review-support/ |
| Page 10 | 57096 | /incorporated-contractor-accountant-toronto/ |
| Post 1 | 57095 | /what-is-a-personal-services-business-canada/ |
| Post 2 | 57097 | /40-hour-contract-incorporated-employee/ |
| Post 3 | 57099 | /contract-hours-cra-control-test/ |
| Post 4 | 57098 | /psb-tax-rate-ontario-2026/ |
| Post 5 | 57100 | /wiebe-door-sagaz-tests-contractors/ |
| Post 6 | 57102 | /psb-more-than-five-employees-exception/ |
| Post 7 | 57104 | /contract-clauses-psb-risk/ |
| Post 8 | 57101 | /finance-contractor-bank-agency-psb/ |
| Post 9 | 57103 | /psb-reassessment-denied-deductions/ |
| Post 10 | 57105 | /psb-risk-reduction-checklist/ |

## Existing page fixes (approved by Sharad)

| Row | URL (ID) | Status |
|---|---|---|
| 1-2 | /employee-vs-contractor-cost-calculator/ (48088) | Done Oct 12: 33.5% to 44.5%, 1 + 2 replacements (FAQ and JSON-LD) |
| 3-6 | /should-mortgage-broker-incorporate-canada/ (49284) | Done Oct 12: "Rate" label, "(3.2% before July 1, 2026)", "(12.2% before July 1, 2026)", $600K to $500K |
| 7-11 | same | Already done on Oct 8 |
| 12 | /acupuncturist-tax-planning-canada/ (49693) | Done Oct 12: visible FAQ and JSON-LD, approved wording |
| 13-15 | same | Done Oct 12 |
| 16 | same | Done Oct 12: FAQ (visible and JSON-LD) and Key Numbers, 3 places. Left as is: the FAQ "Is the business limit $500,000 or $600,000?" and the 2026 Update callout's note "$600,000 in three others". Neither is in the approved locations. The callout note is now out of date; flagged for Sharad |
| 17 | /team/sharad-gondaliya-cpa/ (25185) | Manual: postalCode sits only in Elementor data (4 places), which the connector can't edit. See `MANUAL-CHECKLIST.md` |
| 18-21 | truck dispatch (54117), customs brokers (54086) | Already done on Oct 8 |
| 22 | Dry run sent for Sharad's review | Exact sentence on 2 URLs only: /accountant-for-product-design-studios/ (56807) and /accountant-for-fertility-clinics/ (54736). 11 more pages use "for the owner," (singular), which an exact-sentence replace would skip; they are covered in the row 23 sheet. Not applied until Sharad confirms the list |
| 23 | 17 pages created Oct 5-9 still state 12.2% | Before and after for 60 sentences in `existing-fixes/row-23-before-after.md`. Not applied until Sharad approves |

## Next dates

- **Tue Oct 13:** Sharad reviews the 10 built pages on draft preview.
- **Wed Oct 14:** publish pages 1 to 10, pillar first. You set the 301 in Rank Math Redirections and move page 53131 to draft (it is already in `astro/redirects.csv`). Add the rule 8 link once page 2 is live, so the link never points at a draft.
- **Thu Oct 15:** Sharad reviews posts 1 to 5. Featured images are still to do.
- **Fri Oct 16:** publish posts 1 to 5.
- **Mon Oct 19:** Sharad reviews posts 6 to 10.
- **Tue Oct 20:** publish posts 6 to 10.
- **Wed Oct 21 to Thu Oct 22:** QA of all 20 URLs.
- **Fri Oct 23:** final sign-off.
- **Oct 26 to Nov 6:** rate correction in batches of 50.
