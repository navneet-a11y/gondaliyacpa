# PSB Contractor Project: Status as of Monday, October 12, 2026

Source of truth: `package/` (Sharad's package dated October 3, 2026). Slugs, titles and figures are used exactly as given.

## Week 1 (due October 5 to 9): behind schedule

| Task | Due | Status |
|---|---|---|
| Keyword.com validation and "PSB Contractors" project (40 keywords) | Oct 6 | Not checkable from here (no Keyword.com access) |
| Sharad approval: page drafts and fix before/afters | Oct 6 | No written approval on file in this project |
| 23 existing page fixes live | Oct 8 | 8 done, 5 partial, 10 not done. See `2026-10-12-existing-fixes-audit.md` |
| Table CSS (`.psb-cluster`) in Astra Custom CSS | Oct 9 | Not checked |
| 10 pages built as drafts with calculator, schema and Rank Math settings | Oct 9 | Not started: none of the 10 slugs exist in WordPress under any status |
| Sharad approval: post drafts | Oct 9 | No written approval on file in this project |

## Checks done on the package (October 12)

- Calculator (`package/05-Calculator`) passes all 3 roadmap tests in Chromium: $18,144 and $76,095 (Dec 31, 2027 year-end), 11.70% (Dec 31, 2026 year-end). No horizontal scroll at 360px.
- All 20 JSON-LD blocks parse as valid JSON. Pages: AccountingService, Person, Service, BreadcrumbList, FAQPage. Posts: same, with Article in place of Service.
- All 10 pages have exactly one `[TRUSTINDEX WIDGET]` line. The posts have none.

## Existing page fixes: what is left (details in the audit file)

| Row | URL (ID) | Left to do |
|---|---|---|
| 1-2 | /employee-vs-contractor-cost-calculator/ (48088) | 33.5% to 44.5% (2 visible, 1 JSON-LD) |
| 3-5 | /should-mortgage-broker-incorporate-canada/ (post 49284) | Row 3 label "Deduction" to "Rate"; add the "(… before July 1, 2026)" notes in rows 4-5 |
| 6 | same | "$600K federally" to "$500K federally" |
| 12-16 | /acupuncturist-tax-planning-canada/ (post 49693) | 12.5% to 11.5%, the callout, $600,000 to $500,000 (not by blind replace: one FAQ asks "$500,000 or $600,000?") |
| 17 | /team/sharad-gondaliya-cpa/ (25185) | postalCode M5H 4C9 to M5C 1R6 (Elementor data only, 4 places) |
| 22 | exact sentence: 2 URLs only, 56807 and 54736 | 11 more pages have the "owner," (singular) variant. Needs Sharad's ruling |
| 23 | Template | All 17 accountant-for-* pages created Oct 5-9 still state 12.2% as current. The template was not updated |

## Fixed dates still ahead

- Oct 13: Sharad reviews the built pages. Oct 14: pages go live, plus the 301 redirect (also in `astro/redirects.csv`). Oct 16: posts 1-5. Oct 20: posts 6-10. Oct 23: QA done and final sign-off.
- Oct 26 to Nov 6: rate correction, in daily batches of 50 URLs. Nov 19: 30-day review. Dec 18: 60-day review.
