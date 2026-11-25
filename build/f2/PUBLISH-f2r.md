# Family 2 batch 18 publish state (tools 112 to 116)

BUILT, GATED, DOM-TESTED, PUBLISHED and CARDED on November 25, 2026. The
connector dropped out between the gate run and the publish; it came back and
all five went up in one run, with the hub cards in the same pass.

- `gate_batch.py build_f2r TOOLS18` clear on all five pages
- `gate_f2_all.py` clear across all 116 Family 2 pages (5 known pre-existing)
- `test_f2r_dom.js` 36 checks, 0 failures, 6 decoys all caught
- `gate_rank_math.py` unchanged at its 15 pre-existing failures, all of them in
  `nil_cost_non_hst_jurisdictions` and none in this batch

## All five are Appendix A entries

| # | slug | plan line | bytes | ID | content | meta | term | card |
|---|---|---|---|---|---|---|---|---|
| 112 | failure-to-comply-penalty-calculator | 2796 | 33488 | 2904 | verified | set | f2 | yes |
| 113 | schedule-1-net-income-reconciliation-calculator | 2878 | 32621 | 2905 | verified | set | f2 | yes |
| 114 | gst-hst-filing-frequency-calculator | 2960 | 32460 | 2906 | verified | set | f2 | yes |
| 115 | payroll-remittance-due-date-calculator | 2976 | 33411 | 2907 | verified | set | f2 | yes |
| 116 | shareholder-loan-income-inclusion-calculator | 2998 | 35261 | 2908 | verified | set | f2 | yes |

All five share the 12,975-byte CSS prefix batches 5 to 17 use (sha256 prefix
`8b978623a4fb`), so each publish call is that prefix plus the page body:
`tail -c +12976 <slug>.html`.

`nil_calculator` reads **116 published**, 0 draft, 0 trashed, matching the 116
built files, and the `cnf_family` term `f2` has a count of **116**.

## The publish procedure, with one change

Per tool: `wp_create_cpt_item` (rest_base nil_calculator, status publish, slug,
title, content, and the Astra layout meta plus `cnf_primary_keyword`,
`cnf_last_verified_et` and the three Rank Math fields all in the one `meta`
object) -> `wp_add_post_terms` cnf_family ["f2"] -> live verification.

Batch 8 through 17 set the meta in a second `wp_update_cpt_item` call. Passing
it on the create works and is one call rather than two; nothing was reported as
`meta_ignored` on any of the five.

**The byte probe changed, and the new one is better.** Earlier batches ran a
zero-change `wp_replace_in_post` to confirm the stored `content_length`. That
checks the database, and the defect batch 16 found was not in the database: the
content stored was byte-perfect and the *output* filters mangled `&&` inside a
`<script>` into `&#038;&#038;`. So batch 18 fetches each published URL and
compares the rendered module, from `<div class="ei-hero">` to the closing
`</script>`, against the local file byte for byte. All five came back
**IDENTICAL**, with no entity substitution in the module script and the
stylesheet present.

The only entities inside any module script are `&rsquo;` in tool 116, which are
intentional: they sit inside JavaScript string literals that are written to
`innerHTML`, so the HTML parser decodes them at that point. The test harness
folds `&rsquo;` the same way the browser does, which is a change this batch
made to the copied harness.

## The hub, inserted rather than republished

`/tools/` (page 1187) now links **116 of 116**, verified by fetching the live
page and diffing its tool links against the local build: the two sets match
exactly, with nothing live that is not carded and nothing carded that is not
live.

The five cards went in with five `wp_replace_in_post` calls anchored on the
adjacent card, not by republishing the page. That was deliberate. The live
page's `post_content` measured 40,930 bytes before the edits while the local
build with all five cards measures 40,247, so the live page carries roughly
1.4 KB that `build_tools_hub.py` does not produce. A wholesale republish would
have discarded it sight unseen. The link sets match, which is what plan line
1224 requires, so **the residual byte drift on page 1187 is left as an open
item rather than resolved by overwriting.**

One card per group, five groups:

| tool | hub group |
|---|---|
| 112 | Penalties, Interest and Relief |
| 113 | The Return Itself: Schedules and GIFI |
| 114 | CRA Accounts, Payroll and GST/HST |
| 115 | CRA Accounts, Payroll and GST/HST |
| 116 | Shareholders and Share Capital |

## What the gates caught

Three failures on the first gate run, all fixed before anything published.

1. **112 exceeded the 6(g) outbound cap** at 22 same-site links against a
   limit of 20. Two body links came out: the gross negligence checker, which
   the Read Next list already carries, and the voluntary disclosure checker,
   now named in prose instead. It ships at exactly 20.
2. **A duplicate FAQ paragraph.** 112's relief answer was word for word the T4
   penalty tool's. Rewritten.
3. **A duplicate H2.** 116's first section heading matched batch 17's
   shareholder loan deadline tool. Renamed.

The DOM suite caught two of its own: the copied harness folded only the numeric
apostrophe entity, so every assertion carrying an apostrophe failed on a page
that was in fact correct; and a `notWant` of "threshold 1" could never pass,
because the result table lists all four remitter rows on every answer. Both
were test defects rather than page defects, which is the distinction worth
recording.
