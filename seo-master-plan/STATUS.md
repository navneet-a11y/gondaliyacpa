# gondaliyacpa.ca SEO Master Plan: Status

Plan: Sharad's email, which replaces all earlier SEO change lists. Rules: see the email ("Rules for every change").

- Edit log: `CHANGE-LOG.csv`
- 301 log (for the Astro move): `../astro/redirects.csv`

## Thursday, October 29, 2026

| # | Change | State |
|---|---|---|
| 1 | Security update | Checklist ready for Navneet (`2026-10-29-change-01-security-checklist.md`). Needs Hostinger and wp-admin. |
| 2 | Publishing gate | Rule written (`2026-10-29-change-02-publishing-gate.md`). In force today. |
| 3 | Markham community sentence + sitewide check | **Markham sentence deleted** on /how-to-start-a-business-in-markham/, and the community theme removed from /corporate-tax-filing-markham/ (caches purged). Still open: rewording the next Markham sentence ("disproportionate number"), and the 8 lines on 6 other pages (`2026-10-29-change-03-community-lines.md`). Both wait on Navneet's OK of the wording. |
| 4 | Review markup about ourselves | Found on 617 published items as inline JSON-LD (`2026-10-29-change-04-review-markup.md`). Waiting on backup, Privileged tools switch, Trustindex toggle. |
| 5 | llms.txt | Draft ready for review (`drafts/05-llms.txt`). 6 pages wait on Sharad's decision. |
| 23 | 2027 EI page | In WordPress as **Pending Review**, page 57974 (not public). Waiting on Sharad's CPA review. To do after approval: Rank Math title and description (the Rank Math abilities need switching on), byline date, publish, links from the 2026 page and the payroll calculator. |

## Blockers

- **UpdraftPlus backup.** No API route for it. Navneet runs it before each batch.
- **Easy MCP AI tool switches.** Privileged (search and replace), Plugins, Menus, Rest, Rank Math abilities, and the Search Console and GA4 sources.
- **Missing source files:**
  - Phase 2 audit file (Oct 5)
  - T2 email
  - today's site audit email (the 51 pages)
  - the expert prompt
- **This container cannot reach gondaliyacpa.ca over HTTP** (the proxy refuses it). Live-page checks and the Rich Results Test need a browser.
