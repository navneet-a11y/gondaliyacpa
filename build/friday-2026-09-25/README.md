# Friday 25 September 2026 — post types, taxonomies, root router

Built from the revised build sheet (13 CPTs, three root-level types, 566 reserved slugs).
Reserved slugs are generated from Appendix A, not hand-typed: 215 + 15 + 336 = 566,
verified for duplicates and malformed slugs.

## Files

| File | Where it goes |
|---|---|
| `cptui-taxonomies.json` | CPT UI → Tools → Import/Export → **Taxonomies** → Import |
| `cptui-post-types.json` | CPT UI → Tools → Import/Export → **Post Types** → Import |
| `cnf-root-router.php` | WPCode → Add Snippet → PHP Snippet, Run Everywhere |
| `reserved-slugs.json` | Source list for the Python pipeline |

## Order matters

1. **Taxonomies first.** Post types reference them; importing post types first
   leaves the taxonomy boxes unattached.
2. **Post types second.**
3. **Router snippet last**, and save it *inactive* first — see below.
4. Settings → Permalinks → Save (flushes rewrite rules).

## Why the three root types have `rewrite: false`

WordPress cannot give three post types an empty rewrite slug. Each would register
its own catch-all rule, the first registered would win every single-segment
request, and any slug belonging to the other two would 404. The plan avoided this
by keeping F4 as the only root type; with F1 and F3 also at root, the collision is
real.

So `nil_vertical`, `nil_city_hub` and `nil_service_place` are imported with rewrite
switched off, and the snippet owns their URLs: one catch-all rule injected
immediately *before* WordPress's page rule, so every core rule (REST, feeds,
sitemaps, the ten folder post types) still matches first and pages keep working.
A single indexed query resolves the slug across the three types; anything else
falls through to normal page handling.

This satisfies "register the catch-all rule last" more precisely than ordering the
`init` hook would — it positions the rule within the rules array itself.

## Acceptance test (build sheet step 6)

| Line | Covered by |
|---|---|
| Test item in each of 13 types returns 200 | Folder types by CPT UI rewrite; the 3 root types by the router |
| `cnf_` meta visible in editor and REST | **Not this snippet** — needs the `register_meta` snippet, see below |
| 28 `cnf_place` + 12 `cnf_service` terms present | Loadable over MCP once taxonomies exist |
| Page with an F1/F3/F4 slug is refused | `wp_unique_post_slug` + `rest_pre_insert_*` (409) |
| `/pricing/`, `/tools/`, `/guides/` etc. still resolve as pages | Router falls through to `pagename` |
| Site still noindex | Settings → Reading, unchanged by any of this |

## Extra control the plan does not have

`GET /wp-json/cnf/v1/slug-check?slug=<slug>` returns `{reserved, family, taken_by}`.
The Python pipeline calls this **before** creating a post, so a collision is caught
at item 1 rather than at item 400 of 566.

## Rollback

The snippet is one WPCode entry — deactivate it and the three root types simply
stop resolving; nothing else changes. Then Settings → Permalinks → Save.
No database migration, no content touched.

## Still outstanding for Friday

The `register_meta` snippet for every `cnf_` key (second Friday deliverable, and the
REST half of the acceptance test) is **not** in this batch. It depends on the final
meta key list per type.
