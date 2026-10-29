# gondaliyacpa.ca SEO Master Plan: Status

Plan: Sharad's email, which replaces all earlier SEO change lists. Rules: see the email ("Rules for every change").

- Edit log: `CHANGE-LOG.csv`
- 301 log (for the Astro move): `../astro/redirects.csv`

## Thursday, October 29, 2026

| # | Change | State |
|---|---|---|
| 1 | Security update | Checklist ready for Navneet (`2026-10-29-change-01-security-checklist.md`). Needs Hostinger and wp-admin. |
| 2 | Publishing gate | Rule written (`2026-10-29-change-02-publishing-gate.md`). In force today. |
| 3 | Markham community sentence + sitewide check | Dry run done: 2 named pages plus 6 more pages found (`2026-10-29-change-03-community-lines.md`). Waiting on backup and approval of wording. |
| 4 | Review markup about ourselves | Found on 617 published items as inline JSON-LD (`2026-10-29-change-04-review-markup.md`). Waiting on backup, Privileged tools switch, Trustindex toggle. |
| 5 | llms.txt | Draft in progress, using Rank Math Analytics data. |
| 23 | 2027 EI page | Draft ready for CPA review (`drafts/23-ei-premium-rates-2027.html`). |

## Blockers

- **UpdraftPlus backup.** No API route for it. Navneet runs it before each batch.
- **Easy MCP AI tool switches.** Privileged (search and replace), Plugins, Menus, Rest, Rank Math abilities, and the Search Console and GA4 sources.
- **Missing source files:**
  - Phase 2 audit file (Oct 5)
  - T2 email
  - today's site audit email (the 51 pages)
  - the expert prompt
- **This container cannot reach gondaliyacpa.ca over HTTP** (the proxy refuses it). Live-page checks and the Rich Results Test need a browser.
