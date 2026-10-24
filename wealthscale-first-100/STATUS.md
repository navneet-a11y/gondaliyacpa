# Status

## Live site snapshot (October 22, 2026, before rebuild)

- 39 published pages, 3 draft pages, 1 published post ("Hello world!")
- 40 of the live or draft pages already sit at a URL in the 101-page list, so each one is updated in place (same page ID), not re-created
- Users: "admin" (display name "admin") and a temporary admin login; no "Sharad Gondaliya" user yet
- Active plugins: GP Premium, Rank Math SEO and PRO, LiteSpeed Cache, Code Snippets, UpdraftPlus, Hostinger tools, Easy MCP AI, Temporary Login Without Password
- No cookie-consent plugin yet (setup step 11)

## Existing page IDs for the 101-page list

| WP ID | URL | Plan ID | Day |
| --- | --- | --- | --- |
| 25 | / | 1 | 1 |
| 86 | /about/ | 2 | 1 |
| 91 | /about/sharad-gondaliya/ | 3 | 1 |
| 198 (draft) | /about/neha-gupta/ | 101 | 1 |
| 88 | /editorial-standards/ | 4 | 1 |
| 89 | /how-we-make-money/ | 5 | 1 |
| 90 | /contact/ | 6 | 1 |
| 92 | /methodology/brokers/ | 9 | 1 |
| 99 | /accounts/ | 10 | 1 |
| 100 | /compare/ | 11 | 1 |
| 101 | /reviews/ | 12 | 1 |
| 110 | /vs/ | 13 | 1 |
| 111 | /savings/ | 14 | 1 |
| 117 | /banking/ | 15 | 1 |
| 118 | /calculators/ | 16 | 1 |
| 119 | /benefits/ | 17 | 1 |
| 120 | /markets/ | 18 | 1 |
| 121 | /learn/ | 19 | 1 |
| 182 | /calculators/tfsa-calculator/ | 20 | 1 |
| 139 | /accounts/tfsa/ | 28 | 1 |
| 183 to 189 | /calculators/ (rrsp, fhsa, resp, rrif, compound-interest, capital-gains-tax, currency-conversion) | 21 to 27 | 2 |
| 137, 138, 140, 141, 152 to 158 | /accounts/ (resp-grants, fhsa, rrsp, fhsa-eligibility, tfsa-contribution-limit, tfsa-withdrawals, us-stocks-in-tfsa, rrsp-contribution-limit, home-buyers-plan, resp, rrif-minimum-withdrawal) | 29 to 39 | 2 |
| 3 | /privacy-policy/ | 7 | 5 (after lawyer) |
| 45 | /terms-of-use/ | 8 | 5 (after lawyer) |

## Redirects (setup step 10)

Only two live or draft URLs are outside the 101-page list:

| Old URL | Action |
| --- | --- |
| /hello-world/ (post 1) | Delete the post (step 9); 301 to / |
| /methodology/ (page 87, draft) | Keep as the draft parent of /methodology/brokers/; 301 /methodology/ to /methodology/brokers/ |

Page 7 "Home (old Astra demo)" is a draft with no public URL: delete it.

## One-time setup (Friday, October 23 morning)

| Step | Action | Who | Status |
| --- | --- | --- | --- |
| 1 | Full backup (files and database) | Navneet | Done Oct 22: UpdraftPlus to Google Drive (Hostinger allows weekly backups only) |
| 2 to 3 | Create /wp-content/uploads/ws/ and /ws/people/; upload CSS and JS | Navneet (File Manager) | Done Oct 22, URLs open |
| 4 | Upload the 4 headshots to /ws/people/ | Navneet (File Manager) | Done Oct 22 (Sharad's 400 px is upscaled from a 240 x 360 photo; replace when a larger original arrives) |
| 5 | Code Snippets PHP snippet | Claude | Done Oct 23: snippet 8 active, no PHP errors |
| 6 | LiteSpeed JS excludes | Navneet | Done Oct 23: wealthscale-widgets in JS Excludes and JS Deferred/Delayed Excludes; cache purged |
| 7 | Author "Sharad Gondaliya, CPA" | Navneet + Claude | Done Oct 22: user 1 display name, bio and names set by Navneet; author slug changed from admin to sharad-gondaliya. Login username stays admin. Still to do Friday: Rank Math author archives off |
| 8 | Rank Math schema, breadcrumbs, Instant Indexing | Navneet | Done Oct 23: Article schema for pages, breadcrumbs on, author archives off, Instant Indexing on; checked in browser and Rich Results test |
| 9 | Delete Hello world!, sample comment, Sample Page | Claude | Done Oct 23: post 1, comment 1 and page 7 trashed |
| 10 | Redirects (above) | Navneet (Claude switched on the Redirections module) | Done Oct 23: both 301, exact match; checked in browser |
| 11 | Cookie banner, GA after consent | Navneet | Not started |

## Schedule

| Day | Date | Pages | Status |
| --- | --- | --- | --- |
| 1 | Fri Oct 23 | 20 | Live Oct 23: all 20 published, each verified byte for byte (file size + 34). Rank Math title, description and focus keyword set Oct 23 for all 20 (through Rank Math's own updateMeta route; the Easy MCP integration switch is not needed). Widget CSS and JS were missing from /uploads/ws/; Navneet moved them there and pages now render. Site Address switched to https |
| 2 | Sat Oct 24 | 20 | Not started |
| 3 | Sun Oct 25 | 20 | Not started |
| 4 | Mon Oct 26 | 20 | Not started |
| 5 | Tue Oct 27 | 21 | Not started |
| 6 | Wed Oct 28 | 0 (QA) | Not started |
| 7 | Thu Oct 29 | 0 (Rich Results, indexing, workbook back) | Not started |

## Open items

The full list (20 items, owners Sharad and Navneet) is in the workbook, sheet "Open items". Navneet's items by date:

| No. | Item | By | Status |
| --- | --- | --- | --- |
| 1 | Ask Neha (Upwork) for an 800 x 800 px headshot and to confirm "investing and account pages" scope | Fri Oct 23 | Done Oct 22: Sharad says use her existing headshot, and she is okay with the wording |
| 2 | Privacy policy and terms drafts to the lawyer | Fri Oct 23 | Open |
| 3 | Update each offer the day after it ends (TD Easy Trade ends October 23) | From Oct 24 | Open |
| 4 | Re-check savings, GIC, USD savings rates and CSA crypto list every 7 days | From Oct 29 | Open |
| 5 | Re-check Wealthsimple figures after the November 5 event | Thu Nov 12 | Open |

Rule: never set ws_neha_reviewed_on before Neha confirms her review in writing in the Upwork thread.

## Decisions on October 22 (Navneet: "follow this plan exactly")

- Plan dates hold: setup and Day 1 on Friday, October 23; nothing goes live before then.
- Header (synced pattern 35) and footer (synced pattern 40): every link must be one of the 101 URLs in links.csv. Friday changes:
  - /savings/1-year-gic-rates/ to /savings/gic-rates/
  - /learn/how-to-buy-stocks/ to /markets/how-to-buy-us-stocks/ ("How to buy US stocks")
  - /learn/open-a-brokerage-account/ to /learn/how-to-invest/ ("How to invest")
  - Tax and Benefits menu: drop /benefits/canada-child-benefit/, /tax/capital-gains-tax/ and /tax/; add the capital gains tax calculator and best tax software
  - Remove the Retirement menu (no retirement pages in the plan)
  - Footer: remove /research/, /retirement/ and /tax/; add /about/neha-gupta/ ("Our CFA reviewer")
  - Footer: remove the LinkedIn button (no links to other websites except on the two profile pages)
- Analytics: the site has no Google Analytics today. Per setup step 11, add a cookie banner (Complianz) and load GA4 only after consent; needs a GA4 Measurement ID (G-...).

## Friday batch (after Navneet confirms "backup done")

1. Add and activate the PHP snippet; check a page loads without errors
2. LiteSpeed JS excludes (wealthscale-widgets); purge
3. Rank Math: Article schema for pages, breadcrumbs on, author archives off, Instant Indexing on
4. Delete Hello world!, sample comment, Sample Page, old Astra demo draft
5. Redirects: /hello-world/ to /, /methodology/ to /methodology/brokers/
6. Header and footer link changes above
7. Publish the 20 Day 1 pages (author Sharad, user 1), Rank Math fields from the workbook; static front page = Home
8. Purge, check /page-sitemap.xml, submit IndexNow

## Day 1 live (Friday, October 23)

| Page | WP ID | Parent | Length on site |
| --- | --- | --- | --- |
| Contact | 90 | 0 | 22014 |
| How We Make Money | 89 | 0 | 23313 |
| Neha Gupta, CFA | 198 | 86 | 24512 |
| Sharad Gondaliya, CPA | 91 | 86 | 26327 |
| Editorial Standards | 88 | 0 | 27363 |
| About | 86 | 0 | 27940 |
| Benefits | 119 | 0 | 38193 |
| TFSA calculator | 182 | 118 | 38222 |
| Banking | 117 | 0 | 42654 |
| Markets | 120 | 0 | 43062 |
| Savings | 111 | 0 | 43995 |
| Learn | 121 | 0 | 44364 |
| Reviews | 101 | 0 | 45383 |
| Calculators | 118 | 0 | 49980 |
| Vs | 110 | 0 | 50375 |
| Accounts | 99 | 0 | 50971 |
| Compare | 100 | 0 | 55282 |
| TFSA Guide | 139 | 99 | 63180 |
| Home | 25 | 0 (front page) | 66606 |
| Broker Rating Methodology | 92 | 87 | 86346 |

All by user 1 (Sharad Gondaliya, CPA), comments closed. ws_neha_reviewed_on not set on any page.

Oct 23 evening: search engine visibility turned on (Settings > Reading, by Navneet); all 20 URLs submitted to IndexNow through Rank Math Instant Indexing ("Successfully submitted 20 URLs").

## Offer updates

- Oct 24: TD Easy Trade transfer cash-back offer ended Oct 23. Removed from the offer tables on pages 53 and 55 and from the detail paragraphs on pages 56 and 58; page 83 now says the offer ended (body, cons list, FAQ and FAQ schema). None of these pages was live yet (days 4 and 5). Schema re-validated.
