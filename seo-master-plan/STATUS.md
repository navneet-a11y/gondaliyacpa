# gondaliyacpa.ca SEO Master Plan: Status

Plan: Sharad's email, which replaces all earlier SEO change lists. Rules: see the email ("Rules for every change").

- Edit log: `CHANGE-LOG.csv`
- 301 log (for the Astro move): `../astro/redirects.csv`

## Thursday, October 29, 2026

| # | Change | State |
|---|---|---|
| 1 | Security update | Checklist ready for Navneet (`2026-10-29-change-01-security-checklist.md`). Needs Hostinger and wp-admin. |
| 2 | Publishing gate | Rule written (`2026-10-29-change-02-publishing-gate.md`). In force today. |
| 3 | Markham community sentence + sitewide check | **Done.** 14 edits on 8 pages: Markham ×2, Etobicoke, Scarborough corporate tax, Scarborough start-up, and 3 restaurant pages. Caches purged; a site search finds no remaining community-risk lines. One descriptive Scarborough trade sentence kept (see the change 3 file). |
| 4 | Review markup about ourselves | **Done on our side.** Removed from 1,137 records. The WPCode snippet (post 58001) strips the Trustindex schema site-wide; it's active and the error log shows no PHP errors. Waiting on Navneet: a view-source check plus the Rich Results Test on 10 pages. |
| 5 | llms.txt | Draft ready for review (`drafts/05-llms.txt`). 6 pages wait on Sharad's decision. |
| 23 | 2027 EI page | Page 57974 is in WordPress as Pending Review, waiting on Sharad. **Payroll calculator 2027 mode is live**: tax-year selector; 2027 EI at 1.64% / $70,800 / $1,161.12; CPP, CPP2 and federal brackets updated to the change 8 2026 values. Still to do after Sharad approves: publish, then add the links from the 2026 EI page and the calculator. The 301 is logged for 2027-03-01 in astro/redirects.csv. |

## Blockers

- **UpdraftPlus backup.** No API route for it. Navneet runs it before each batch.
- **Easy MCP AI tool switches.** Privileged (search and replace), Plugins, Menus, Rest, Rank Math abilities, and the Search Console and GA4 sources.
- **Missing source files:**
  - Phase 2 audit file (Oct 5)
  - T2 email
  - today's site audit email (the 51 pages)
  - the expert prompt
- **This container cannot reach gondaliyacpa.ca over HTTP** (the proxy refuses it). Live-page checks and the Rich Results Test need a browser.

## Decisions (Friday, October 30, 2026, from Navneet with Sharad's confirmation)

- **Change 7 (one address and one phone): ON HOLD. Do not apply.** The prep report is kept for later.
- **Change 12 (Best/Top pages, noindex and rewrites): ON HOLD. Do not apply.**
- **/review-engagement-services/:** keep its current redirect to /cpa-compilation-report-notice-to-reader/.
- **No staging:** the security updates (change 1) are done live, after a backup. Content edits wait until Navneet confirms the updates are finished.
- **Change 6 (services we do not offer): ON HOLD in this session.** Navneet is handling it in a different session. Do not edit SR&ED or review/audit content here.
