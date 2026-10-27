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
| 21 | winding-up-an-inactive-corporation | 26159 | | | | |
| 22 | small-business-corporate-filing | 24443 | | | | |
| 23 | corporate-compliance-calendar | 24605 | | | | |
| 24 | numbered-company-maintenance | 24298 | | | | |
| 25 | mandatory-t2-electronic-filing | 24713 | | | | |
| 26 | schedule-50-and-shareholder-reporting | 24239 | | | | |
| 27 | non-resident-owned-corporation-nil-filing | 25030 | | | | |

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
