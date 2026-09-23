# Decisions and deviations from the signed-off plan

The plan in `corpnilfilingfor300-seo-website-plan.md` is the verbatim record of the
document Sharad Gondaliya prepared on September 21, 2026. It is not edited. Every
deviation from it is logged here instead, with its date and its consequences.

Deviations affecting dates, scope or the hard rules go into the Friday weekly update
to Sharad Gondaliya.

---

## 2026-09-21 — No staging environment. Build on the live site only.

**Decided by:** Navneet.
**Supersedes:** every staging reference in the plan (Rule 10, the Sept 22, Sept 23 and
Oct 2 build rows, Section 4.1 hosting/UpdraftPlus/plugin-stack rows, Section 4.5).

`staging.corpnilfilingfor300.ca` is not built. All work happens on
`corpnilfilingfor300.ca` directly.

### Consequences to manage

1. **Rule 10 is now the only thing standing between a half-built site and the index.**
   The live site must carry a site-wide noindex until Sharad Gondaliya confirms launch.
   Set it in Rank Math (global noindex), not only WordPress Settings → Reading, since
   Rank Math overrides the core setting.
   Do **not** guard it with `Disallow: /` in robots.txt. A blocked crawl means Google
   never reads the noindex tag and the URL can still surface. It also contradicts the
   Sept 29 done-when test, which requires robots.txt to allow crawl.

2. **The restore rehearsal has lost its target.** The Oct 2 done-when test was
   "staging restores from the latest backup with the database intact." A restore cannot
   be rehearsed on live without destroying it. Keep a disposable restore target — a
   throwaway subdomain or a host-level snapshot restore — so the backup is proven before
   968 URLs exist. Do not mark Oct 2 done on an unproven backup.

3. **Plugin updates are now tested in production.** The Tuesday 06:00 Eastern window
   said "after a staging test." Take a full UpdraftPlus backup immediately before every
   update window instead, and update one plugin at a time.

4. **Test artifacts now land on the live site.** The Sept 25 test item in each of the
   14 post types, and the Oct 7 ten-URL pipeline dry run, are created on live. Delete
   every test item once its done-when test passes. The Family 4 root-slug test matters
   most: a leftover test item can occupy one of the 336 reserved Family 4 slugs.
   Run the Oct 7 dry run with posts in draft status where the test allows it.

### Unchanged

Every date, every URL count and every hard rule stands. The build runs to the same
schedule.

---

## 2026-09-21 — Sept 22 infrastructure partially complete

**Reported by:** Navneet. Hosting, DNS connection, HTTPS and SSL are done.

Not yet confirmed, and still required by the Sept 22 done-when test:

- SSL Labs grade A
- HSTS header present (max-age 31536000, includeSubDomains, preload)
- WAF blocks a scripted 100-request burst on `/lookup/`
- CDN: edge full-page cache with bypass on `/lookup/`, `/pay/` and `/sign/`
- DNS records: CAA, SPF, DKIM, DMARC `p=quarantine`
- Cutover TTL returns to 3600 seconds 48 hours after cutover

The staging half of the Sept 22 test ("staging resolves and is noindexed") is void
under the decision above and is replaced by: live resolves and is noindexed.

---

## 2026-09-23 — Post type architecture revised: 13 CPTs, three at root

**Decided by:** Navneet, in the revised Friday 25 September build sheet.

### Count corrected: 14 → 13

The plan's Section 4.2 said 14 custom post types. It listed 16 families, of which
F15 and F16 use the native `page` type — but F13 uses the native `post` type too, so
the custom count is 13, not 14. Navneet caught this. The 13 are correct and the
plan's 14 was an overcount.

### Three post types now at the site root, not one

The plan stated "Family 4 is the only root-level custom post type." F1 and F3 have
joined it, so the reserved-slug list grows from 336 to **566** (F1 215 + F3 15 +
F4 336). Generated from Appendix A and verified: no duplicates, no malformed slugs.

WordPress cannot give three post types an empty rewrite slug — each registers its
own catch-all rule, the first registered wins every single-segment request, and a
slug belonging to either of the other two 404s. So the three root types are
registered with `rewrite = false` and `build/friday-2026-09-25/cnf-root-router.php`
owns their URLs: one catch-all rule injected immediately before WordPress's page
rule, with a single indexed query resolving the slug across all three.

### Rewrite slug changes from the plan

| Family | Plan | Now |
|---|---|---|
| F1 `nil_vertical` | `industry` | root (no prefix) |
| F2 `nil_calculator` | `calculator` | `tools` |
| F3 `nil_city_hub` | `city` | root (no prefix) |
| F8 `nil_cost` | `cost` | `pricing` |

The build sheet's F1 row gave both a rewrite slug (`nil-t2-filing-for`) and
Level = Root, which contradict. Built as root, because Appendix A's F1 URLs are
single-segment and the 566 count only holds if F1 sits at the root.

### Other settings not in the plan

- `has_archive` false on all 13. The hubs are F16 pages with Elementor Loop Grids;
  a CPT archive would duplicate them.
- `with_front` false on all 13.
- All 8 taxonomies have `rewrite` false. No taxonomy archive is published anywhere,
  since a crawlable one would create thin duplicates of the Elementor hubs.

### Hub URL set has changed

The build sheet's acceptance test names `/pricing/`, `/tools/`, `/guides/`,
`/services/`, `/locations/` and `/blog/` as pages. Appendix A Family 16 lists
`/what-we-file/`, `/who-this-is-for/`, `/provinces/`, `/all-calculators/` and
`/service-areas/`. The F16 set has changed from the signed-off plan.

---

## 2026-09-23 — Plugins added beyond the approved stack

Installed on live and active, none of them in the plan's Section 4.1 stack:

- **Ultimate Addons for Elementor (UAE)** — supports the Oct 2 header/footer work
- **Safe SVG** — sanitises SVG uploads
- **Temporary Login Without Password** — mints passwordless admin login links.
  Remove once the access it was added for is finished, and revoke any live links.
  This build will eventually handle T183CORP signing and uploaded photo ID.
- Hostinger Tools, Hostinger Easy Onboarding, Hostinger Reach — host-bundled
- **Easy MCP AI** — the connector this session works through. Its access is full
  administrator, well beyond the Oct 7 spec (`edit_posts` + `upload_files` on a
  dedicated publisher account with an IP allow-list).

All need Sharad Gondaliya's sign-off under the approval rules.

### Launch guard moved

Rank Math SEO PRO is now active, and Rank Math overrides the core "Discourage
search engines" setting. The site-wide noindex must be set in **Rank Math →
Titles & Meta → Global Meta**, not only Settings → Reading.
