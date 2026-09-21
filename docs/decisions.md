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
