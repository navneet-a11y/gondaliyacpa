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
| 1 | Full backup (files and database) in Hostinger | Navneet (hPanel) | Not started |
| 2 to 3 | Create /wp-content/uploads/ws/ and /ws/people/; upload CSS and JS | Navneet (File Manager) | Done Oct 22, URLs open |
| 4 | Upload the 4 headshots to /ws/people/ | Navneet (File Manager) | Done Oct 22 (Sharad's 400 px is upscaled from a 240 x 360 photo; replace when a larger original arrives) |
| 5 | Code Snippets PHP snippet | Can be done through the WordPress connection | Not started |
| 6 | LiteSpeed JS excludes | Can be done through the WordPress connection | Not started |
| 7 | Author user "Sharad Gondaliya, CPA"; rename "admin" display name | Navneet (user creation) | Not started |
| 8 | Rank Math schema, breadcrumbs, Instant Indexing | Rank Math settings | Not started |
| 9 | Delete Hello world!, sample comment, Sample Page | Can be done through the WordPress connection | Not started |
| 10 | Redirects (above) | Rank Math | Not started |
| 11 | Cookie banner, GA after consent | Navneet | Not started |

## Schedule

| Day | Date | Pages | Status |
| --- | --- | --- | --- |
| 1 | Fri Oct 23 | 20 | Ready to publish after setup steps 1 to 5 |
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
| 1 | Ask Neha (Upwork) for an 800 x 800 px headshot and to confirm "investing and account pages" scope | Fri Oct 23 | Open |
| 2 | Privacy policy and terms drafts to the lawyer | Fri Oct 23 | Open |
| 3 | Update each offer the day after it ends (TD Easy Trade ends October 23) | From Oct 24 | Open |
| 4 | Re-check savings, GIC, USD savings rates and CSA crypto list every 7 days | From Oct 29 | Open |
| 5 | Re-check Wealthsimple figures after the November 5 event | Thu Nov 12 | Open |

Rule: never set ws_neha_reviewed_on before Neha confirms her review in writing in the Upwork thread.
