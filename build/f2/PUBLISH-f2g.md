# Family 2 batch 7 publish state (tools 41 to 50)

BUILT, GATED (`gate7.py`, and `gate_f2_all.py` across all fifty pages) and
DOM-TESTED (`test_f2g_dom.js`, 40 checks). This file tracks the publish step
so an interrupted run can be resumed.

Per tool: `wp_create_cpt_item` (rest_base nil_calculator, status publish,
slug, title, content) -> zero-change `wp_replace_in_post` probe on
post_content to confirm content_length equals the build file byte for byte ->
`wp_update_cpt_item` with the Astra layout meta, cnf_primary_keyword,
cnf_last_verified_et and the three Rank Math fields -> `wp_add_post_terms`
cnf_family ["f2"] (term_taxonomy_id 15).

| # | slug | bytes | ID | content | meta | term |
|---|---|---|---|---|---|---|
| 41 | first-t2-year-end-options-generator | 26936 | | | | |
| 42 | year-end-change-impact-calculator | 27833 | | | | |
| 43 | two-t2-returns-in-one-year-checker | 27171 | | | | |
| 44 | mandatory-t2-efile-checker | 26578 | | | | |
| 45 | business-days-between-dates-calculator | 27360 | | | | |
| 46 | t183corp-signature-requirement-checker | 28107 | | | | |
| 47 | provincial-return-requirement-checker | 27146 | | | | |
| 48 | cra-account-closure-sequencer | 28019 | | | | |
| 49 | corporate-deadline-calendar-generator | 28934 | | | | |
| 50 | catch-up-filing-schedule-generator | 27636 | | | | |

All ten share the same 12,975-byte CSS prefix as batches 5 and 6
(sha256 prefix `8b978623a4fb`), so the publish call for each one is that
prefix plus the page body.

## What the gates and the test caught in this batch

Four defects, each in the generator rather than on a published page:

1. **A bare `T183`.** I wrote "It is always Form T183CORP, never T183" to
   explain hard rule 2, which breaks hard rule 2. The guard added in this
   batch fired on it. The sentence now says the name is never shortened
   without writing the short form.
2. **`authorized` outside the one permitted phrase.** `gate7.py` carries the
   rule 1 check that strips "authorized signing officer" and then rejects any
   remaining use of the word. Three sentences used it of a transmission being
   authorized; all three were reworded.
3. **The permitted phrase split across a line in the emitted script.** The
   same check could not recognise "authorized signing officer" where the
   generator broke the JS string literal inside it. The literal now breaks
   after the phrase. This is worth remembering: the gate reads the rendered
   HTML, so a phrase it whitelists has to survive as one string in the
   output.
4. **"a 181 days period".** The DOM test rejected it. `plural()` returns
   "181 days", so the heading read ungrammatically; it now says "creates a
   period of 181 days".

Two of my own test expectations were wrong rather than the pages: the empty
state on tool 41 reads "Enter the date of incorporation", and tool 42's prose
says "a short year does not get a short deadline". Both were checked against
the page before the test was changed.

Every date the DOM test asserts was computed independently in Python against
the same nine Ontario holidays before being written into the test, including
the two that move: December 31, 2028 is a Sunday followed by New Year's Day,
so a June 30, 2028 year-end is due January 2, 2029; and June 30, 2024 is a
Sunday followed by Canada Day, so a December 31, 2023 year-end is due July 2,
2024.

## The cross-batch gate, and the debt it exposed

`build/f2/gate_f2_all.py` is new in this batch and is the Family 2 equivalent
of `build/f9/gate_f9_all.py`. On its first run it found six duplicates across
the fifty pages. One was mine from batch 6 and is fixed in the generator and
on the live page: tool 32 shared a section heading with tool 26.

The other five predate this batch, are on live pages, and are listed in
`KNOWN` in that file. They are printed on every run and do not fail it. Three
of them change a section heading, which is a visible edit to a live page, so
they are left for Navneet to approve rather than changed quietly.

## Topics: why none came from Appendix A

Recorded in full in the docstring of `build/f2/build_f2g.py`. In short:
Appendix A cannot supply ten more distinct F2 tools, and three topics I
drafted were dropped on reading the plan rather than on taste, because the
plan does not approve the figures they would have had to assert.
