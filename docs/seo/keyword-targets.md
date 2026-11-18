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
| filing a nil corporate tax return | 20 | n/a | no | none | unassigned |
| filing a nil return for corporation tax | 20 | n/a | no | none | unassigned |
| filing nil t2 return for corporations | ? | n/a | no | none | unassigned |

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

Not yet applied - awaiting Navneet.
