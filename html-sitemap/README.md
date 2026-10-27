# HTML Sitemap — gondaliyacpa.ca

The HTML sitemap is published as a **hub + section pages** (WordPress), because the
site has outgrown what a single editable page can hold.

## Structure (v8)

| Page | WordPress ID | URL |
|---|---|---|
| Hub | 26586 | https://gondaliyacpa.ca/html-sitemap/ |
| Pages — Part 1 of 2 | 57858 | https://gondaliyacpa.ca/html-sitemap-pages/ |
| Pages — Part 2 of 2 | 57859 | https://gondaliyacpa.ca/html-sitemap-pages-2/ |
| Blog Posts | 57860 | https://gondaliyacpa.ca/html-sitemap-blog/ |

- **1,759 URLs total — 1,261 pages + 498 blog posts** (the 4 sitemap pages themselves
  are excluded from the listings).
- Pages are sorted by most-recently-updated (newest first) and split into two roughly
  equal halves (Part 1 = newest 631, Part 2 = older 630). Blog Posts are all 498 on
  one page, newest-updated first.
- Every entry shows its **Publishing Date** and its **Last Reviewed & Updated Date**,
  grouped by month, with a month quick-jump nav and a section bar linking hub ↔ all
  sections.
- The hub links to the three sections (with counts) and lists the 30 most recently
  updated URLs across the whole site.

### Why split (SEO + mechanics)

A single page with ~1,760 links spreads link equity thin and reads as a low-value
link dump; it had also grown past WordPress's in-place edit ceiling (~204,800 bytes
per `wp_replace_in_post`). Splitting by type mirrors the site's Yoast XML sitemaps
(page vs post), keeps each section a focused, fully-crawlable list one click from the
hub, and keeps every page comfortably under the byte ceiling so builds are reliable.
When a section approaches the ceiling, add another part (e.g. Pages Part 3).

## Files

- `pages_v7.tsv` / `posts_v7.tsv` — source data `date<TAB>modified<TAB>url<TAB>title`
  from the WordPress REST API (`wp/v2/pages`, `wp/v2/posts`, ordered by `modified`).
- `generate8.py` — builds all four pages: normalizes titles to ASCII, sorts by
  `modified` desc, splits pages into halves, groups by month, and emits each section's
  header + byte-verified chunks + full record, plus the hub.
- `header_p1.html` / `header_p2.html` / `header_blog.html` — each section's header
  (styles, title, legend, section bar, month nav) with a `<!--GCPA_ROWS-->` marker.
- `published_p1.html` (159,568 B) / `published_p2.html` (154,433 B) /
  `published_blog.html` (170,240 B) — exact HTML stored in each section's
  `post_content`.
- `hub.html` (11,628 B) — exact HTML stored in the hub page's `post_content`.

## How it's published

Each section page: `post_content` is reset to its header (marker included) via
`wp_update_page`, then rows are appended in byte-verified ≤8 KB chunks via
`wp_replace_in_post` (the final chunk drops the marker). Every page stays under the
~204.8 KB subject limit, so no oversized single write is ever needed. The hub is a
single `wp_update_page`. Elementor is disabled on the hub (`_elementor_edit_mode`
cleared) so raw `post_content` renders; the new section pages render `post_content`
directly.

## Maintenance

Refresh `pages_v7.tsv` / `posts_v7.tsv` from the REST API and re-run `generate8.py`,
then reset + append each section and update the hub.

## Version history

- **v8** (current) — hub + 3 section pages, 1,759 URLs, two dates each.
- **v6/v7** — single `/html-sitemap/` page, 1,344–1,612 URLs, two dates (compact
  M/D/YY); reached the single-page size ceiling, which prompted the v8 split.
- **v2–v5** — single page, 996→1,344 URLs; earlier date/format iterations.
- **v1** — 757 pages only, alphabetical.
