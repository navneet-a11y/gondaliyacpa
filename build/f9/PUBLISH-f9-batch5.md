# Family 9 batch 5 publish state (guides 18 to 27)

All ten are BUILT, GATED (gate5.py and gate_f9_all.py) and committed. This
file tracks only the publish step, so an interrupted run can be resumed.

Per new guide: `wp_create_cpt_item` (rest_base nil_guide, status publish,
slug, title, excerpt, content) -> zero-change `wp_replace_in_post` probe to
confirm content_length equals the build file byte for byte ->
`wp_update_cpt_item` with the Astra layout meta, cnf_last_verified_et and the
three Rank Math fields from f9_batch5_seo.py -> `wp_add_post_terms`
cnf_family ["f9"] (term_taxonomy_id 22).

| # | slug | bytes | ID | content | meta | term |
|---|---|---|---|---|---|---|
| 18 | t2-filing-deadlines | 25893 | 1377 | verified | set | f9 |
| 19 | zero-activity-corporate-tax-returns | 25231 | 1379 | verified | set | f9 |
| 20 | corporate-tax-arrears-and-interest | 25309 | 1381 | verified | set | f9 |
| 21 | winding-up-an-inactive-corporation | 26159 | 1383 | verified | set | f9 |
| 22 | small-business-corporate-filing | 24443 | 1385 | verified | set | f9 |
| 23 | corporate-compliance-calendar | 24605 | 1387 | verified | set | f9 |
| 24 | numbered-company-maintenance | 24298 | 1389 | verified | set | f9 |
| 25 | mandatory-t2-electronic-filing | 24713 | 1391 | verified | set | f9 |
| 26 | schedule-50-and-shareholder-reporting | 24239 | 1393 | verified | set | f9 |
| 27 | non-resident-owned-corporation-nil-filing | 25030 | 1395 | verified | set | f9 |

## The 17 earlier guides: DONE

Every one carried a changed sibling list, so all seventeen were patched with
chunked `wp_replace_in_post` operations rather than re-uploading 23KB pages.
Each landed on exactly the byte count its regenerated build file carries:

867 27528, 945 23566, 947 22256, 949 22432, 951 22793, 953 22814, 955 21856,
976 24017, 978 21708, 980 22546, 982 22413, 984 22307, 1094 23585,
1096 22885, 1098 23913, 1100 22623, 1102 22889.

### A transport bug worth remembering

`wp_replace_in_post` received two characters fewer than were sent whenever the
`search` string ENDED with `</`: the fragment reads as the opening of a
closing tag and is eaten in transit. It matched two characters short, so the
deletion left `</` behind and produced a broken URL on two live pages:

    /guides/</t2-late-filing-penalties/

Found on 984 by reading the live content after its final byte count came out
two over target, and the same fix applied to 1094. Both are corrected and
both now match their build file exactly. A probe for `/guides/</` returns zero
matches on 1096, 1098 and 1100, which were the other three at-risk pages
before their plans were regenerated.

A `search` ending with a bare `<` came through intact (the pillar's first
operation did), so only the two-character `</` form is affected. The chunker
in the patch builder now moves a boundary FORWARD to a safe character, which
it has room to do because the chunk size is 460 against the tool's own limit
of 500. Moving the boundary backward was tried first and was worse: it
shortened each following chunk until the last was a single character, and a
one-character search matched hundreds of times.

## Complete

All ten published 2026-10-27, IDs 1377 to 1395 (odd numbers). Every page's
content_length came back equal to its build file on a zero-change probe, so
all ten transferred exactly. nil_guide total is now 27. Family 9 stands at 27
of the 30 in the plan.

### cnf_family f9 backfilled

The f9 term stood at 11 against 27 live guides once this batch was tagged, so
sixteen of the seventeen earlier guides had never been given it. All
seventeen were tagged, and the term now reads 27. The same gap is still open
on cnf_family f2 for the calculators.

### Open for sign-off

- All ten topics. Seven are Appendix A topics with corrected slugs; three
  (mandatory-t2-electronic-filing, schedule-50-and-shareholder-reporting,
  non-resident-owned-corporation-nil-filing) are not in Appendix A at all,
  because its Family 9 list cannot supply ten more distinct topics.
- The sibling window. Every guide now links twelve siblings rather than all
  the others, which is what keeps the family inside the 40-outbound cap as it
  grows to 30.
- New guide copy needs Sharad Gondaliya's review before it counts as
  published under the approvals rule.
