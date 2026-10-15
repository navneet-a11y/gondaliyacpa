# The three 14 October drafts — what they are, and what blocks publishing

| ID | Title | Slug |
|---|---|---|
| 523 | Nil Years Are One Stage: Your Corporation From Opening to Closing | `corporate-lifecycle` |
| 524 | Your Corporation Started Operating: What Changes After the Nil Years | `when-your-corporation-starts-operating` |
| 521 | REVIEW ONLY: Home Page Ecosystem Section | `review-ecosystem-section` |

## Which task are they part of? None

Neither slug appears anywhere in the plan — not in the Section 6(a) URL table, not in
Appendix A, not in Family 15's 24 slugs at line 1153, not in any other family. Neither
is in `docs/decisions.md`. Both carry no `cnf_family` term ("No families" in the admin
list) and every `cnf_` meta field is empty.

They are **new scope**, not a plan deliverable. For the task sheet they are not part of
Family 14, Family 15 or the October 16 batch; they would need their own line.

What they actually are: a cross-site funnel. Page 523 positions the nil years as stage 2
of a six-stage corporate lifecycle running
opencorporationfor35.ca → corpnilfilingfor300.ca → gondaliyacpa.ca, with an "ecosystem"
table linking all three. Page 524 is the hand-off page for the moment a corporation
starts operating. Page 521 is a preview of that ecosystem table, intended for the home
page.

The idea is sound and the pages are well built. The problem is what the copy claims.

## Three hard-rule breaches — these block publishing

### 1. FAQPage schema, on both 523 and 524

Both emit `{"@type":"FAQPage", ...}` in their JSON-LD.

Hard rule 6 and plan line 37: *"No review or aggregateRating schema, no FAQPage and no
HowTo."* Also launch gate 6 (line 1901), the schema checklist at line 1343, and the
November 18 schema deployment test at line 370.

Line 1582 is the one to follow when fixing it: *"No FAQPage markup and no HowTo markup …
The question format stays, the markup goes."* So the visible FAQ sections stay exactly
as they are; only the schema block is removed.

### 2. "Lowest Price Guarantee in Canada", on 523

In the ecosystem table, on the opencorporationfor35.ca row. It breaches two rows of the
7.4 banned-phrase table at once:

- *Cheapest, lowest price in Canada, best price, unbeatable* → gate one item 31
- *Guaranteed, guarantee, we guarantee* → "Delete the sentence", gate one item 34

It describes the other site's offer, but it is published on a corpnil page, so it counts.

### 3. "1300+ 5-star Google reviews", on both 523 and 524

Twice on 523, once on 524, in the trust box and the ecosystem footnote.

The 7.4 table names this figure explicitly: *"500+ reviews, 1300+ reviews, 600+ clients,
10 years, 15+ years, 20+ years"*, gate one item 32, with the note: **"The
claim-consistency audit is a hard launch gate; until it closes, no count claim is
published at all."**

Not "reword it" — no count claim at all until that audit closes.

## Three more that are Sharad's call, not mine

- **"the only CPA firm in Canada where you see your final fee and sign your engagement
  letter on the same screen"** (523 ecosystem table and 524 body). Not in the 7.4 table
  and not a cheapest/best/fastest claim, so not a breach I should act on alone. It is
  still an unverifiable uniqueness claim and Rule 217 is the reason the neighbouring
  phrases are banned.
- **"If a return turns out not to be nil, you get a full refund"** (both pages). A
  refund commitment. The plan has a `/refund-policy/` page in Family 15 that is not
  built, and CLAUDE.md puts legal page text with Sharad, published as supplied.
- **"Multiple award-winning team", "2026 Xero Awarded Firm"** (both trust boxes). Not
  banned, but they sit next to the review count in the same claim-consistency audit.

## What is already fine

- Links all resolve: `/form/`, `/pricing/`, `/catch-up-nil-t2-filing/`,
  `/final-t2-before-dissolution/`, `/sharad-gondaliya-cpa/` are all live pages.
- The portrait exists, media 285.
- CRA wording is correct throughout — "registered EFILE electronic filer", "transmitted
  to the Canada Revenue Agency". No *authorized*, *agent* or *approved*.
- T183CORP is written in full everywhere.
- No EFILE number, no CRA GroupID.
- No booking or meeting language; "No call, meeting or email chain needed" is the
  approved framing.
- Holding, rental and dividend corporations are correctly stated as not nil.
- Price reads "$300.00 plus HST per tax year", matching Navneet's standing correction
  rather than CLAUDE.md's literal "including HST", and consistent with the other pages.

## Page 521 is scratch

"REVIEW ONLY: Home Page Ecosystem Section" is a preview of the table embedded in 523.
The live decision in CLAUDE.md says to delete every test item from live once its
done-when test passes. It should be deleted rather than published, once the ecosystem
section is settled.

## If these go live

They are off-plan URLs Sharad has not seen. The site-wide noindex under hard rule 10
bounds the exposure, as it did for Family 14, but the sign-off is still owed and the
three breaches above have to be fixed first either way.
