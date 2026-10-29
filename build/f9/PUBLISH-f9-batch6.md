# Family 9 batch 6 publish state (guides 28 to 30) — DONE

Family 9 is complete at the plan's 30 guides. All three are BUILT, GATED
(gate6.py and gate_f9_all.py) and PUBLISHED.

| # | slug | bytes | ID | content | meta | term |
|---|---|---|---|---|---|---|
| 28 | cra-accounts-on-a-dormant-corporation | 29739 | 1464 | verified | set | f9 |
| 29 | choosing-and-changing-a-fiscal-year-end | 26959 | 1466 | verified | set | f9 |
| 30 | quebec-co17-and-alberta-at1 | 26182 | 1468 | verified | set | f9 |

`cnf_family` f9 now reads 30 against 30 live guides.

## The defect this batch nearly shipped

Five sections per guide, fifteen in all, rendered as the single word "True".
`render` takes `(key, title, body, alt)` and I wrote the alt flag third, in
the body's position, so `body` became `True` and `alt` became the body
string. A non-empty string is truthy, so each affected section printed "True"
and came out correctly styled as an alternate band. Each guide lost about 4KB
of written body.

Nothing in the repo caught it. gate6.py counted twelve contents rows and
twelve sections, and there were twelve of each. gate_f9_all.py checked links,
duplicate headings and inbound counts, all fine. It was caught by reading a
built page before publishing it.

Two checks now exist that would have caught it:

- `build_f9_batch6.py` asserts every section body is a string starting with
  `<` and longer than 200 characters, and that a fourth element is a bool.
- `gate6.py` rejects any section whose first body line is a bare `True`,
  `False`, `None` or empty, read off the rendered HTML rather than the source.

Fixing it also exposed a banned hedge word in a body the gate had never been
able to see, because that body was the string "True". A gate cannot check
copy it is not being shown.

## The 12 earlier guides: DONE

The sibling window is circulant, so appending three guides moved the wrap
point. Exactly 12 live guides needed their sibling list changed, indices 15
to 26, by one to three links each.

This was not cosmetic. Under a 30-guide registry the only guides that link to
the three new ones are indices 15 to 26, so leaving them stale would have
given each new guide 0 sibling inbound against the 6(g) minimum of 12.

### How the 12 were patched, and why the obvious way was wrong

The first attempt replaced the changed rows positionally in chunks. The
verification refused it: on `small-business-corporate-filing` a 3-row
anchored search matched twice. The reason is that the new list is a ROTATION
of the old one, so replacing a tail row with a row that still exists earlier
in the same list creates a duplicate mid-sequence, and the next search then
matches both copies.

The decomposition that works is per page: delete the rows that dropped out
(contiguous in the old list, under the 460-character search cap), then insert
the rows that were added, anchored on the pair of rows that surround the
insertion point. Two operations per page, 24 in all, every search verified
unique.

Before any of it was applied, the whole sequence was simulated against a
reconstruction of the live content, built by swapping the new sibling block
back to the old one in each regenerated file. The simulation had to reproduce
each built file exactly or the run did not start. It also produced a free
check: the reconstructed "live now" byte count matched the published byte
count recorded in PUBLISH-f9-batch5.md for all ten batch 5 guides, which
confirmed the reconstruction was right.

| slug | ID | was | now |
|---|---|---|---|
| t2-schedules-on-a-nil-return | 1100 | 22623 | 22652 |
| shelf-corporation-compliance | 1102 | 22889 | 22930 |
| t2-filing-deadlines | 1377 | 25893 | 25907 |
| zero-activity-corporate-tax-returns | 1379 | 25231 | 25238 |
| corporate-tax-arrears-and-interest | 1381 | 25309 | 25342 |
| winding-up-an-inactive-corporation | 1383 | 26159 | 26200 |
| small-business-corporate-filing | 1385 | 24443 | 24465 |
| corporate-compliance-calendar | 1387 | 24605 | 24635 |
| numbered-company-maintenance | 1389 | 24298 | 24345 |
| mandatory-t2-electronic-filing | 1391 | 24713 | 24771 |
| schedule-50-and-shareholder-reporting | 1393 | 24239 | 24289 |
| non-resident-owned-corporation-nil-filing | 1395 | 25030 | 25083 |

Every one landed on exactly its regenerated file's byte count.

## OPEN: the guides hub links 15 of 30

`/guides/` (page 904) carries 15 guide links. Rule 6(g) for Family 16 says
each hub links every child in its family, so it is 15 short, and 3 of those
missing are the guides published here.

This predates this batch: the hub was not extended for batch 5 either. It is
one page and needs Navneet's go-ahead, because bringing it to 30 changes a
page a visitor may have bookmarked and the hub's own copy may need to grow
with the list.
