# Family 2 batch 5 (tools 21-30) publish state

All ten are BUILT, TESTED (195 assertions), GATED and PUSHED on
claude/nice-meitner-xyq53s. This file tracks only the publish step.

Per page: create (rest_base nil_calculator, status publish) -> zero-change
probe to confirm content_length == the build file -> wp_update_cpt_item with
the 8 meta fields from f2e-manifest.json -> wp_add_post_terms cnf_family
["f2"] (term id 15).

| # | slug | bytes | ID | content | meta | term |
|---|---|---|---|---|---|---|
| 21 | tax-years-since-incorporation-calculator | 29302 | 1285 | verified | set | f2 |
| 22 | days-overdue-calculator | 28100 | 1287 | verified | set | f2 |
| 23 | next-t2-due-date-checker | 27721 | 1289 | verified | set | f2 |
| 24 | final-t2-return-due-date-calculator | 28256 | 1291 | verified | set | f2 |
| 25 | amalgamation-t2-due-date-calculator | 28264 | 1293 | verified | set | f2 |
| 26 | short-tax-year-deadline-calculator | 28061 | 1295 | verified | set | f2 |
| 27 | nil-return-late-penalty-checker | 27126 | 1297 | verified | set | f2 |
| 28 | clearance-certificate-requirement-checker | 26753 | 1299 | verified | set | f2 |
| 29 | payroll-nil-remittance-checker | 26286 | 1301 | verified | set | f2 |
| 30 | gst-hst-account-closure-checker | 26416 | 1303 | verified | set | f2 |

## Open item found while publishing

The cnf_family term f2 (term id 15) had a count of 10 before tool 21 was
tagged, against 20 live calculators. So about half the earlier tools were
never given the family term. Needs a sweep: list nil_calculator items, check
each for cnf_family, add f2 where missing.

## Complete

All ten published 2026-10-27, IDs 1285 to 1303 (odd numbers). Every page's
content_length_after matched its build file exactly, confirmed by a zero-change
probe on a distinctive line of each page's own logic. nil_calculator total is
now 30. Family 2 stands at 30 of the 150 in Appendix A.

A defect was caught between publishing tool 26 and tool 27: tools 27 to 30
emitted the shared prelude twice, because their JS constants began with PICK
rather than the prelude and the wiring loop prepended a second copy. Found by
reading the generated script before publishing. Tools 21 to 26 were unaffected
(their JS begins with the prelude already), and their byte counts did not move,
so the six already live were correct. Fixed in the generator, which now asserts
the prelude appears exactly once per tool.
