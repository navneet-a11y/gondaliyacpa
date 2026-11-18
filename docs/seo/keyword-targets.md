# Keyword targets supplied outside the plan

Keywords Navneet supplied with volume data that the signed-off plan does not
target. The plan's 16 family keyword lists (lines 1232-1258 of
`docs/corpnilfilingfor300-seo-website-plan.md`) are built almost entirely
around **"nil t2"** phrasing. These use **"corporate tax return"** and
**"corporation tax"** phrasing instead, which is a separate vocabulary the
site does not currently cover.

Status key: `unassigned` = no page targets it; `secondary` = covered as a
secondary term on an existing page; `primary` = a page's focus keyword.

## Supplied 2026-11-18

Navneet's source reported **8 keywords, 60 total volume**. Three came through
in the message; the remaining five were truncated and have not been supplied.

| Keyword | Vol | KD | In plan? | Page targeting it | Status |
|---|---|---|---|---|---|
| filing a nil corporate tax return | 20 | n/a | no | 976 `/guides/how-to-file-a-nil-t2-return/` | secondary |
| filing a nil return for corporation tax | 20 | n/a | no | 976 `/guides/how-to-file-a-nil-t2-return/` | secondary |
| filing nil t2 return for corporations | ? | n/a | no | 976 `/guides/how-to-file-a-nil-t2-return/` | secondary |

### GSC check, 2026-08-20 to 2026-11-18

Property totals for the window: 683 impressions, 8 clicks, 34 non-anonymised
queries. **None of the three appears.** The nearest queries the site does
surface:

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| how to file a nil return | 1 | 0 | 8 |
| nil return | 2 | 0 | 11 |
| what is a nil tax return | 1 | 0 | 11 |
| how to file a nil t2 return (variants) | - | - | - |

Caveat: GSC omits queries made by very few users, so absence from the query
report is not proof of zero impressions. At 20 searches a month, 90 days is
roughly 60 searches per keyword, which is inside the range GSC anonymises.
The on-page check below is the firmer evidence.

### On-page check

Audited all **302** keyworded pages in `docs/seo/rank-math-meta.json`:

- Exact focus-keyword matches for the three: **zero**.
- Focus keywords starting with "filing": one only, `filing one year vs all unfiled years` (post 1700), unrelated intent.
- Focus keywords using the "corporate tax return" / "corporation tax" vocabulary at all: **eight**, and every one is a different intent - `unfiled` or `no activity` / `zero activity`, mostly place-qualified:

| ID | Focus keyword |
|---|---|
| 947 | unfiled corporate tax returns |
| 1379 | zero activity corporate tax returns |
| 914 | unfiled corporate tax returns in ontario |
| 915 | no activity corporation tax return in ontario |
| 1104 | unfiled corporate tax returns in british columbia |
| 1106 | no activity corporation tax return in british columbia |
| 1605 | unfiled corporate tax returns in alberta |
| 1607 | no activity corporation tax return in alberta |

Nothing covers the plain act of **filing** a nil corporate return under that
vocabulary.

### Recommendation

All three are one intent, so one page should own them. **Do not build a new
page** - that repeats the guide-versus-blog duplication already costing the
Schedule 50 and mandatory-e-filing clusters 158 impressions at zero clicks.

Assign them as secondary terms to **post 976,
`/guides/how-to-file-a-nil-t2-return/`** (focus keyword
`how to file a nil t2 return`, currently 5 impressions at position 6.0, the
closest intent on the site). The work is wording, not a new URL: carry
"nil corporate tax return" and "nil return for corporation tax" into an H2
and the body, and into the meta description, alongside the existing nil T2
phrasing.

### Applied 2026-11-18

Navneet's condition was to apply it only if the page was not already ranking
for better-performing keywords. It was not. Checked before touching it:

- Page totals, 90 days: **5 impressions, 0 clicks, position 6.0**.
- Queries for that page specifically (GSC filtered to the URL): **0 rows**. Every one of its five impressions is in the anonymised bucket, so there is no identifiable query to dilute.

Nothing to protect, so the change went in. Post 976 is classic content, not
Elementor, so it was edited with two `wp_replace_in_post` calls.

**What changed**

1. New H2 inside the opening section, below the EFILE notice:
   `Filing a Nil Corporate Tax Return Is the Same as Filing a Nil T2`.
   Two paragraphs tie the three wordings to the one filing, each phrase in
   bold once, plus an info box noting the T2 is the federal return and that
   Quebec's CO-17 and Alberta's AT1 are separate returns.
2. A table-of-contents entry, `Nil Corporate Tax Return or Nil T2`, anchored
   to `#naming`.
3. Meta description now carries both vocabularies:
   `How to file a nil T2 return, also called a nil corporate tax return: what you need, the year-end, which schedules apply, and signing Form T183CORP.` (146)

**What deliberately did not change**

- **The title.** `How to File a Nil T2 Return | Step by Step for Canada` keeps the primary keyword in first position. Putting a 20-a-month secondary term in the title would dilute the term the page actually ranks for.
- **The focus keyword**, still `how to file a nil t2 return`.
- **No new URL.** A separate page for these three would repeat the duplication already costing the Schedule 50 and e-filing clusters 158 impressions at zero clicks.

**Verified on the live page** after a cache clear: the H2 and its anchor
render, the TOC link resolves, all three phrases are present, the new
description is served. Banned-phrase sweep over the rendered text is clean
(no bare T183, no unqualified "no penalty", no superlative, no prohibited CRA
wording, no emoji), and the required EFILE wording and not-nil scope
statement are both still present.

**Note, not changed:** this page prices at `$300.00 plus HST per tax year`
although it is a national guide. That is the pending HST sweep across the 206
national pages, not something to fix on one page in isolation, and the
current wording is what `build/f3/audit_visible.py` still expects.
