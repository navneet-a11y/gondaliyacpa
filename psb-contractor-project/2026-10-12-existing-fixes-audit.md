# Existing Page Fixes: live-site audit (read-only)

Audit date: 2026-10-12. Source table: `pkg/PSB-Contractor-Content-Package/09-Existing-Page-Fixes.md`, rows 1-23.
Method: content fetched through the `gondaliya_cpa` MCP (wp_get_post_full with context=edit for the row 1-21 pages, wp_get_page for the row 22/23 pages). Raw content is saved as `audit/<slug>.html` and meta as `audit/<slug>.meta.json`. Counts are exact substring counts, split into visible content and inline `<script type="application/ld+json">` blocks. I also checked straight vs curly apostrophes, `&#8217;`, `&ndash;`/`&#8211;`, `&amp;` and escaped-quote variants. Nothing was changed on the site.

**Where the JSON-LD lives:** On every page in rows 1-16 and 18-23, the FAQ JSON-LD is inline in post_content (1-2 `ld+json` blocks per page). None of these pages has a Rank Math schema meta key (`rank_math_schema_*`); the only Rank Math meta keys are title, description, seo_score and similar. The team page (row 17) is the exception: its post_content has no JSON-LD. The schema sits in an Elementor HTML widget inside the `_elementor_data` meta, and the same schema is copied in `_elementor_element_cache`.

Counts are written as visible / JSON-LD (or meta, where stated).

| # | URL | Page ID | Status | Current-text count | Corrected-text count | Locations | Notes |
|---|---|---|---|---|---|---|---|
| 1 | /employee-vs-contractor-cost-calculator/ | 48088 (page, publish, modified 2026-08-13) | NOT DONE | 1 / 0 | 0 / 0 | visible (guide) | "44.5%" does not appear anywhere on the page. |
| 2 | /employee-vs-contractor-cost-calculator/ | 48088 | NOT DONE | 1 / 1 | 0 / 0 | visible FAQ + inline JSON-LD | Both places still say 33.5%. In total, "33.5%" appears 2 times visible and 1 time in JSON-LD (rows 1 and 2 combined). |
| 3 | /should-mortgage-broker-incorporate-canada/ | 49284 (**post**, publish, modified 2026-10-08) | PARTIAL | 0 | 0 | visible table | The row now reads `<td>Federal Small Business Deduction</td><td>9%</td>`. The rate was fixed to 9%, but the label still says "Deduction" instead of "Rate". There is no "15%" on the page. |
| 4 | same | 49284 | PARTIAL | 0 | 0 | visible table | The row now reads `Provincial &ndash; Ontario Small Business` / `2.2%`, with the label using the `&ndash;` entity. It has neither the comma wording nor "(3.2% before July 1, 2026)". There is no "3.2%" anywhere on the page. |
| 5 | same | 49284 | PARTIAL | 0 | 0 | visible table | The row now reads `Combined CCPC Rate` / `11.2%`, without "(12.2% before July 1, 2026)". There is no "12.2%" anywhere on the page. |
| 6 | same | 49284 | NOT DONE | 1 / 0 | 1 / 0 (elsewhere) | visible paragraph above the table | "...active business income up to $600K federally." is still live. The single "$500K federally" match is a different sentence ("Small Business Deduction Application: ..."). |
| 7 | same | 49284 | DONE | n/a | `<div class="big">11.2%</div>` | visible metric tile | |
| 8 | same | 49284 | DONE (variant wording) | 0 | 0 exact | visible | The live text is "about 11.2% (from July 1, 2026) on active business income", with an extra parenthetical. |
| 9 | same | 49284 | DONE | 0 | 1 / 0 | visible | |
| 10 | same | 49284 | DONE | 0 | 1 / 0 | visible comparison table | |
| 11 | same | 49284 | DONE | 0 / 0 | 1 / 1 | visible FAQ + inline JSON-LD | |
| 12 | /acupuncturist-tax-planning-canada/ | 49693 (**post**, publish, modified 2026-10-08) | PARTIAL | 0 / 0 | 0 / 0 | visible FAQ + inline JSON-LD | Visible (straight `'`): "Ontario's small business corporate tax rate is 2.2% (from July 1, 2026), while the general corporate tax rate is about 12.5%." JSON-LD (curly `’`): "Ontario’s small business corporate tax rate is 2.2%, while the general corporate tax rate is about 12.5%." The small-business rate was changed with different wording, and visible and JSON-LD no longer match. The general rate is still "about 12.5%" in both. |
| 13 | same | 49693 | PARTIAL | 0 | 0 | visible Key Numbers | The line now reads `Ontario Small Business Corporate Tax Rate: 2.2%`, without "(from July 1, 2026)". |
| 14 | same | 49693 | NOT DONE | 1 / 0 | 0 | visible Key Numbers | |
| 15 | same | 49693 | NOT DONE | 1 / 0 | 0 | visible 2026 Update callout | This callout is a note about the article itself ("Please note the article gives the business limit as $500,000 in two places and $600,000 in three others, gives an Ontario small business rate of 3.2% and a general rate of about 12.5%, ..."). Swapping in the corrected text changes what the note means, so it needs an editorial rewrite. |
| 16 | same | 49693 | NOT DONE | "$600,000": 4 / 2 | "$500,000": 4 / 2 | visible + inline JSON-LD | The 3 target places are all still $600,000: the FAQ answer "The Small Business Deduction limit is $600,000...", the Key Numbers line "Small Business Deduction Limit: $600,000", and the matching JSON-LD answer. "$600,000" also appears in a newer FAQ, "Is the business limit $500,000 or $600,000?" (visible and JSON-LD), and in the 2026 Update note. **A blind replace-all would turn that question into "$500,000 or $500,000".** |
| 17 | /team/sharad-gondaliya-cpa/ | 25185 (page, publish, parent 25186 "team", modified 2026-10-05) | NOT DONE | 0 in content; **4 in meta** | 0 | Elementor meta only | `"postalCode": "M5H 4C9"` appears 2 times in `_elementor_data` and 2 times in `_elementor_element_cache` (the Person address and the nested Organization address). The `streetAddress` in the same objects already says "55 Queen St E Ste 1205, Toronto, ON M5C 1R6, Canada", which is the 4 "M5C 1R6" hits. post_content (19 KB rendered cache) has no JSON-LD. The fix has to be made in `_elementor_data` (escaped JSON), and the element cache needs regenerating. |
| 18 | /accountant-for-truck-dispatch-businesses/ | 54117 (page, publish, modified 2026-10-08) | DONE (variant wording) | 0 | 0 exact | visible service card (1) | The live text is "about 11.2% (from July 1, 2026) up to the $500,000 business limit". It appears only once (it was not found in the FAQ or JSON-LD). There is no "12.2%" on the page. |
| 19 | same | 54117 | DONE | 0 | 1 / 1 | visible + inline JSON-LD | |
| 20 | /accountant-for-customs-brokers/ | 54086 (page, publish, modified 2026-10-08) | DONE (variant wording) | 0 | 0 exact | visible (1) | The live text is "taxed in Ontario at roughly 11.2% (from July 1, 2026) combined". There is no "12.2%" on the page. |
| 21 | same | 54086 | DONE | 0 | 1 / 1 | visible + inline JSON-LD | |
| 22 | accountant-for-* pages carrying the template sentence | see the list below | NOT DONE | 2 pages, 1 each (visible only) | 0 on all pages | visible service card only; 0 in JSON-LD | Only 2 pages contain the exact sentence. 11 more pages have the same sentence with "for the owner," (singular) at 12.2%, which the exact-sentence replace will skip. |
| 23 | Template for new accountant-for-* pages | 17 pages created 2026-10-05 to 10-09 | NOT DONE | see below | 0 | visible + inline JSON-LD | Every accountant-for-* page created on or after 2026-10-05 still states 12.2% as the current rate, has 0 hits for "11.2%", and has no "(12.2% before July 1, 2026)". **The template was not updated.** |

## Row 22 dry run

To build the candidate set, I ran several searches with per_page 100 and fetched every page of results:
- "salary-versus-dividend mix RRSP room 53.53%" gave 110 results, all fetched.
- "salary-versus-dividend" gave 146 results.
- "53.53%" gave 307 results; I used the snippets to triage these.

WP search requires every query term to be present. Any page holding the exact sentence must therefore contain all of those terms, so it is in the 110-page set. I fetched all 110 pages and grep-confirmed them, plus 6 extra pages (handyman, lash and brow, winding down, data analytics, second-generation family, PSB calculator). The REST search covers published content only, so drafts and private pages were not covered.

### EXACT matches (the replacement would change these)

| URL | ID | Created | Visible | JSON-LD | Total |
|---|---|---|---|---|---|
| /accountant-for-product-design-studios/ | 56807 | 2026-10-09 | 1 | 0 | 1 |
| /accountant-for-fertility-clinics/ | 54736 | 2026-10-07 | 1 | 0 | 1 |

The corrected sentence (11.2% version) appears exactly on 0 pages.

### Near variants: NOT exact, the exact-sentence replace will NOT touch these

A. Same sentence with "for the owner," (singular) and still at 12.2%. These are the likely intended targets.
Text: "We set the salary-versus-dividend mix for the owner, paying enough T4 salary to build RRSP room while the balance flows as dividends, so combined tax stays near the 12.2% Ontario small-business rate instead of 53.53%." (visible only, 1 each)

| URL | ID | Created |
|---|---|---|
| /accountant-for-private-investigators/ | 56870 | 2026-10-09 |
| /accountant-for-security-guard-companies/ | 56869 | 2026-10-09 |
| /accountant-for-software-resellers/ | 56803 | 2026-10-09 |
| /accountant-for-no-code-development-agencies/ | 56798 | 2026-10-09 |
| /accountant-for-denturists/ | 56799 | 2026-10-09 |
| /accountant-for-cloud-service-providers/ | 54831 | 2026-10-08 |
| /accountant-for-cybersecurity-companies/ | 54823 | 2026-10-08 |
| /accountant-for-managed-service-providers/ | 54828 | 2026-10-08 |
| /accountant-for-medical-device-distributors/ | 54734 | 2026-10-07 |
| /accountant-for-sleep-clinics/ | 54731 | 2026-10-07 |
| /accountant-for-security-companies/ | 56871 | 2026-10-09 (ends "...rate rather than 53.53% personally.") |

B. Older pages (created before 2026-10-05, mostly 2026-09-07 to 09-28) that already carry an 11.2% version of the sentence. These have different wordings: "for the owners/owner/founders/principals/an incorporated farm", "11.2% (from July 1, 2026)", "instead of the 53.53% top personal rate", and others. They need no row-22 action. There are about 30 such pages, for example environmental-consultants 53518, engineering-consultants 53519, online-course-creators 53439, direct-to-consumer-brands 53436, bus-and-coach 52837, limousine 52835, locksmiths 52542, alarm-and-camera 52541, portable-toilet 52540, audio-visual 52011, wedding-venues 52007, party-rental 52009, factoring 51887, private-lenders 51870, agricultural 51852, farms 51850, auto-parts 51848, market-research 51832, BPO 51831, call-centres 51819, translation 51813, publishers 51812, toy-stores 51785, bookstores 51786. Per-page detail is in `audit/r22.json`.

C. Pages where the stem is worded differently ("We set the salary-versus-dividend mix, paying...", "...mix each...", "We model the salary-versus-dividend mix...") do not contain the sentence at all.

Data analytics (54824) and lash and brow (56872) use different sentences but still state 12.2% (see row 23).

## Row 23: accountant-for-* pages created on or after 2026-10-05

All 17 are published. Counts are "12.2%" visible / JSON-LD; none of them contains "11.2%", "(12.2% before July 1, 2026)" or "$600,000".

| ID | Slug | Created | 12.2% (vis / LD) |
|---|---|---|---|
| 56870 | accountant-for-private-investigators | 2026-10-09 | 3 / 1 |
| 56869 | accountant-for-security-guard-companies | 2026-10-09 | 3 / 1 |
| 56871 | accountant-for-security-companies | 2026-10-09 | 3 / 1 |
| 56872 | accountant-for-lash-and-brow-studios | 2026-10-09 | 2 / 1 |
| 56803 | accountant-for-software-resellers | 2026-10-09 | 3 / 1 |
| 56798 | accountant-for-no-code-development-agencies | 2026-10-09 | 3 / 1 |
| 56807 | accountant-for-product-design-studios | 2026-10-09 | 3 / 1 |
| 56799 | accountant-for-denturists | 2026-10-09 | 3 / 1 |
| 56800 | accountant-for-businesses-winding-down | 2026-10-09 | 1 / 0 |
| 54831 | accountant-for-cloud-service-providers | 2026-10-08 | 3 / 1 |
| 54824 | accountant-for-data-analytics-companies | 2026-10-08 | 3 / 1 |
| 54823 | accountant-for-cybersecurity-companies | 2026-10-08 | 3 / 1 |
| 54828 | accountant-for-managed-service-providers | 2026-10-08 | 3 / 1 |
| 54734 | accountant-for-medical-device-distributors | 2026-10-07 | 3 / 1 |
| 54731 | accountant-for-sleep-clinics | 2026-10-07 | 3 / 1 |
| 54736 | accountant-for-fertility-clinics | 2026-10-07 | 2 / 1 |
| 54334 | accountant-for-second-generation-family-businesses | 2026-10-05 | 1 / 0 |

Every occurrence presents 12.2% as the current rate, for example "roughly the 12.2% Ontario small-business rate against 53.53% personally" and "roughly a 12.2% Ontario combined rate on the first $500,000". In contrast, pages created from about 2026-09-07 to 09-28 already say "11.2% (from July 1, 2026)". **The new-page template appears to have regressed to 12.2%.**

## Reference pages

| URL | ID | Status | Notes |
|---|---|---|---|
| /personal-services-business-tax-calculator/ | 53131 | publish (page; created 2026-09-25, modified 2026-10-07) | Elementor page. |
| /software-development-it-consultants/ | 30733 | publish (page; created 2026-03-02, modified 2026-08-16) | **No link to /accountant-for-it-contractors/.** Zero "it-contractor" strings in content or meta. |
| /accountant-for-it-contractors/ | none found | NOT FOUND | Searches for "IT contractors", "accountant for IT contractors" and "Accounting and Tax Services for IT Contractors" (status any) found no page with this slug. It does not exist yet. |
| /consultation/ | 15736 | publish (page; modified 2026-09-17) | Elementor page with a HubSpot meetings iframe (meetings-na3.hubspot.com/meetings/sharad). |

## Files

- `audit/<slug>.html` holds the raw content for every page fetched (127 pages); `audit/<slug>.meta.json` holds meta for the rows 1-21 pages.
- `audit/r22.json` holds per-page row-22 counts and near-variant text.
