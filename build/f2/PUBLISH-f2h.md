# Family 2 batch 8 publish state (tools 51 to 60)

BUILT, GATED and DOM-TESTED on October 30, 2026. NOT YET PUBLISHED: the
corpnil connector dropped out of the session before the publish step and
needs re-authorizing, so this file is the handover.

- `gate8.py` clear on all ten pages
- `gate_f2_all.py` clear across all sixty Family 2 pages (5 known pre-existing)
- `test_f2h_dom.js` 36 checks, 0 failures
- `gate_rank_math.py` PASS on 188 ledger items, titles and descriptions unique

## All ten come from Appendix A, which corrects what batch 7 recorded

`build_f2g.py` says Appendix A "cannot supply ten more distinct F2 tools".
That was too sweeping. The groups I had been drawing from were exhausted; the
appendix was not. Every slug below is an Appendix A entry.

Family 2 therefore stands at 40 of the plan's 150 F2 URLs once these publish,
counting only appendix entries. Sixty pages are built: 40 appendix entries and
20 slugs chosen outside it. That gap is worth a line in docs/decisions.md and
a word with Sharad Gondaliya, because the plan's count and the site's count
are measuring different things.

| # | slug | bytes | ID | content | meta | term |
|---|---|---|---|---|---|---|
| 51 | t2-filing-requirement-checker | 29070 | | | | |
| 52 | required-schedules-checker | 30848 | | | | |
| 53 | share-capital-reporting-checker | 29166 | | | | |
| 54 | shareholder-loan-balance-checker | 28659 | | | | |
| 55 | gifi-schedule-125-checker | 28908 | | | | |
| 56 | gifi-schedule-141-checker | 28383 | | | | |
| 57 | dormant-corporation-obligation-checker | 28734 | | | | |
| 58 | annual-return-vs-tax-return-checker | 28877 | | | | |
| 59 | dissolve-or-keep-filing-cost-calculator | 29705 | | | | |
| 60 | federal-annual-return-fee-calculator | 27645 | | | | |

All ten share the same 12,975-byte CSS prefix as batches 5 to 7 (sha256
prefix `8b978623a4fb`), so the publish call for each one is that prefix plus
the page body: `tail -c +12976 <slug>.html`.

## The publish procedure, unchanged from batch 7

Per tool: `wp_create_cpt_item` (rest_base nil_calculator, status publish,
slug, title, content) -> zero-change `wp_replace_in_post` probe on
post_content to confirm content_length equals the byte count above ->
`wp_update_cpt_item` with the Astra layout meta, cnf_primary_keyword,
cnf_last_verified_et and the three Rank Math fields -> `wp_add_post_terms`
cnf_family ["f2"] (term_taxonomy_id 15).

Take the Rank Math values from `f2h-manifest.json` rather than retyping them.
Batch 7 shipped one page with a hand-typed title that did not match the
manifest, and that is the whole reason this instruction is here.

Afterwards: fill the IDs into the table above, write them into
`docs/seo/rank-math-meta.json` under `nil_calculator_batch8` (the items
currently carry `"id": null` and a slug), and confirm from the site that
`nil_calculator` reads 60 published and the `cnf_family` term `f2` has a
count of 60.

## What the gates and the test caught in this batch

Three defects, each in the generator rather than on a published page.

1. **A guard that was wrong about its own data.** The new check requiring
   every date and number field to be read by the module fired on `lac`,
   which is not a field: `yn()` puts an `id` on its label for
   `aria-labelledby`. The check now matches on the `<input>` element rather
   than on any `id=` in the form. A guard that cannot tell a label from a
   field would have failed every future batch using radio groups.

2. **The plan's GIFI rule, four times verbatim.** `gate_f2_all.py` found the
   two-sentence rule repeated identically across three pages and twice within
   one of them. Widening the gate's shared-block exclusion would have silenced
   it; instead each page now frames the rule for its own question and the
   operative clauses stay word-for-word. Four pages leading with an identical
   passage is thin content, and the exclusion list exists for phrases that
   must travel whole, not for passages I found inconvenient to vary.

3. **Tool 58 under-counted the filings, and only the DOM test saw it.** The
   count was one for the T2 plus one per yes, so a corporation answering no
   to both questions was told it owed a single filing. Every corporation is
   incorporated somewhere and owes that registry an annual return, so the
   floor is two. The home registry is now a constant and the second question
   asks about registration outside the jurisdiction of incorporation, which
   it had to anyway: "is it also registered with a province?" has no useful
   answer for a corporation already incorporated in one.

   Every structural gate passed this page. The defect was a wrong answer on
   a result screen, which is the class of thing only a rendered assertion
   catches, and it is the second batch running in which the DOM test found
   the one real bug.

## Topics refused, so the next batch does not re-draft them

Eleven appendix slugs were drafted and dropped on reading the plan: the GIFI
code lookup (no code table in the plan), the GST/HST registration threshold
and small supplier tests (no threshold), six penalty and interest calculators
(no rates; the plan gives exactly two figures of that kind and both are
already live), the three shareholder loan tax calculators (statutory periods
and prescribed rates), two permanent establishment tests (no definition) and
corporate revival (not in the plan). The generator docstring records each one
with its reason.
