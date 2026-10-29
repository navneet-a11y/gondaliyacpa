# Family 2 batch 6 publish state (tools 31 to 40)

All ten are BUILT, GATED (gate6.py), DOM-TESTED (test_f2f_dom.js, 36 checks)
and PUBLISHED. This file is the record of the publish step.

Per tool: `wp_create_cpt_item` (rest_base nil_calculator, status publish,
slug, title, content) -> zero-change `wp_replace_in_post` probe to confirm
content_length equals the build file byte for byte -> `wp_update_cpt_item`
with the Astra layout meta, cnf_primary_keyword, cnf_last_verified_et and the
three Rank Math fields -> `wp_add_post_terms` cnf_family ["f2"]
(term_taxonomy_id 15).

| # | slug | bytes | ID | content | meta | term |
|---|---|---|---|---|---|---|
| 31 | corporate-balance-due-date-calculator | 27275 | 1413 | verified | set | f2 |
| 32 | fiscal-period-length-calculator | 27176 | 1415 | verified | set | f2 |
| 33 | cra-demand-to-file-deadline-calculator | 27485 | 1417 | verified | set | f2 |
| 34 | t4-nil-filing-requirement-checker | 27897 | 1419 | verified | set | f2 |
| 35 | retained-earnings-rollforward-calculator | 27398 | 1421 | verified | set | f2 |
| 36 | balance-sheet-balancing-checker | 27106 | 1423 | verified | set | f2 |
| 37 | nil-gifi-balance-sheet-checker | 28299 | 1425 | verified | set | f2 |
| 38 | schedule-8-cca-requirement-checker | 27774 | 1427 | verified | set | f2 |
| 39 | involuntary-dissolution-risk-checker | 28075 | 1432 | verified | set | f2 |
| 40 | director-liability-exposure-checker | 28476 | 1434 | verified | set | f2 |

Every one of the ten `content_length_before` readings equalled the build
file's byte count exactly, so nothing was lost or transformed in transit.

Tool 32 was published at 27,173 bytes and is now 27,176. The cross-batch gate
written during batch 7 (`build/f2/gate_f2_all.py`) found that its third
section heading, "A Short Year Does Not Get a Short Deadline", was the same
heading tool 26 already used. It is now "A Short Period Still Gets the Full
Six Months" in the generator and on the live page, which both read 27,176.
The ten SEO entries are recorded in `docs/seo/rank-math-meta.json` under
`nil_calculator_batch6`, and `build/f2/gate_rank_math.py` passes on 165
items.

## The f2 backfill, now closed

`cnf_family` f2 read 20 against 30 live calculators before this batch, so ten
of the earlier tools had never been tagged. After publishing these ten the
term read 30 against 40 live, which confirmed the same ten-item gap.

`wp_add_post_terms` with append is idempotent and reports `changed`, so it
was run across all thirty earlier tools and the nine that reported
`changed: true` are the ones that had been missing:

1120, 1122, 1172, 1174, 1176, 1178, 1180, 1182, 1184

1124 was the tenth. It hit the connector's rate limit on the first two
attempts and was tagged on a later retry.

Note for future audits: `wp_list_cpt_items` silently ignores a `cnf_family`
argument. Filtering by it returned all forty calculators, and so did
filtering by `f9`, which no calculator carries. `wp_rest_read` on
`/wp/v2/nil_calculator` with a `cnf_family` query answers Forbidden for this
key. The term's own `count` from `wp_list_terms`, compared against the CPT
total, is the reliable check.
