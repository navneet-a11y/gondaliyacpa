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
- **Rate changes for changes 8 and 9 approved by Navneet (October 30):** the 2026 payroll values, the Ontario 2026 brackets and BPA, the federal BPA, the EI guide totals, the corporate tax rates (Ontario 2.2% from July 1, 2026, and the other provinces from CRA's table), and the calculator logic.

## Handoff (Friday, October 30, 2026): agents stopped to switch sessions

The three agents applying changes 8 to 11 were stopped partway to avoid per-call permission prompts. `.claude/settings.json` was added to the default branch so a new session runs without prompts.

**State when stopped:**
- **Change 8 (pages 38443, 39590): PARTLY applied, not logged.** Before-copies are in `backups/*-before-change08.json`. Compare the live `_elementor_data` with the prep list (`2026-10-30-prep-changes-08-09.md`, 8A/8B) to see which replacements are done. Log them, then finish the rest.
- **Change 9 (pages 35514, 36029): PARTLY applied, not logged.** It was working on the 36029 province cards (Ontario/Quebec) when stopped. Before-copies are in `backups/*-before-change09.json`. Compare and finish the same way as change 8. Calculator check: run `drafts/09-corporate-tax-calculator.test.js` against the live code.
- **Change 10: most link fixes done and logged** (see `CHANGE-LOG.csv`, change_no 10). Still to confirm or do:
  - set 36489, 22 and 21763 to draft
  - noindex /thank-you/ and /tax-intake-form/
  - retitle 44209 to Oshawa
  - rename 43679 ("windor") with a 301
  - add the 301 for the nested best-bookkeeping URL
- **Change 11: started.** Before-copies were taken for 14878, 16, 1707, 17951 and 6621. Check the live pages for the H1 to H2 changes, then do the rest from the prep file. /about-us/ is a manual Elementor edit.
- **Holds still apply:** changes 6, 7 and 12. /review-engagement-services/ stays as is.
- **Every edit must:** be dry-run first, be checked to hit only the intended page, run one at a time, keep a before-copy, be logged in `CHANGE-LOG.csv`, and purge the cache.
