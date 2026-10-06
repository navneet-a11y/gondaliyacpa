# About page — everything the plan specifies

Source: docs/corpnilfilingfor300-seo-website-plan.md. Nothing here is invented;
every line cites its plan location. Build date: Friday, October 9, 2026.

## 1. URL — unresolved conflict (needs Sharad's sign-off)

| Plan location | Slug given |
|---|---|
| 6(a) Family 15 list, line 1153 | `/about/` |
| Schema Block 2, line 543 | `/about/` |
| Schema Block 4 (Sharad), line 829 | `/about/` |
| Schema Block 5 (Vandana), line 971 | `/about/` |
| 6(h) internal-link table, line 1537 | `/about/` |
| 6(g) entity-consistency table, lines 1600-1612 | `/about/` |
| Brand-mention table, line 1625 | `/about/` |
| 6(i) backlink plan, line 1632 | `/about/` |
| Cross-site duplication table, line 1688 | `/about/` |
| **Appendix A, Family 15, line 3556** | **`/about-us/`** |

Nine references to `/about/`, one to `/about-us/`. This is the same Family 15
conflict already logged in docs/decisions.md.

## 2. Build and ownership

- Build date: Friday, October 9, 2026 (4.5 dated build table, line 367 and line 2252).
  Part of the 55-URL first content set: F8 15, F9 10, **F15 24**, F16 5, home 1.
- Done-when test for that set: 55 URLs return 200, appear in the right sitemap
  slice, and carry a visible last-reviewed date.
- Reviewer: Sharad Gondaliya reviews all 24 F15 pages; Navneet publishes (line 1223).
- Hard gate: "No trust page publishes without the CPA Ontario numbers and the
  firm address." (line 1223)
- Banned phrase flagged for F15: "CRA agent" (line 1223).

## 3. Technical build (4.2 line 322, 4.4 line 349)

| Setting | Value |
|---|---|
| Post type | native `page`, root-level slug |
| Supports | title, editor, custom-fields, revisions, author, page-attributes |
| Taxonomy | `cnf_family` term `f15` |
| Post meta | `cnf_legal_version`, `cnf_effective_date_et`, `cnf_claim_audit_ref`, `cnf_accessibility_conformance`, `cnf_last_verified_et` |
| Sitemap slice | `page-sitemap.xml` (45 URLs: F8 15, F15 24, F16 5, home 1 — line 1308) |
| Elementor template | Single Page, named **Single – Trust and Legal** |
| Display condition | Pages in `cnf_family` term `f15`; if the taxonomy condition is unavailable on pages, assign by a Specific Pages list of the 24 URLs |
| Dynamic tags used | `cnf_legal_version`, `cnf_effective_date_et`, `cnf_accessibility_conformance` |

## 4. Exact on-page copy required (Section 5.1, lines 381-397)

Five trust elements name the About page as a placement. Copy verbatim.

1. **Reviewing CPA** — "Sharad Gondaliya, CPA (Canada and USA). CPA Ontario
   Membership 61040184. Washington 57629. Montana PAC-CPAP-LIC-033176."
   Schema: Person (name, jobTitle, hasCredential, identifier, worksFor).
2. **Second CPA** — "Vandana Goel, CPA. CPA Ontario Membership 61158584."
   Note in plan: "Named so clients know two CPAs stand behind the file."
3. **Identity and direct dealing** — "We verify your identity and your authority
   to sign before we transmit. We deal with you directly and never through a
   third party."
4. **Work performed in Canada** — "Your return is prepared and transmitted in
   Canada. Our credentials are never shared and no part of your file is sent
   offshore." Schema: Organization (areaServed, location).
5. **Office and hours** — "55 Queen St E, Suite 1205, Toronto, ON M5C 1R6.
   647-212-9559. info@gondaliyacpa.ca. Open 9:00 AM to 8:30 PM, Monday to
   Sunday." Schema: AccountingService (address, telephone, email,
   openingHoursSpecification).

Plus the designated EFILE paragraph for `/about/`, `/security/` and every
Family 9 pillar (line 1592), described in the plan as "the only permitted
phrasing":

> "Gondaliya CPA Professional Corporation is a registered EFILE electronic
> filer. Returns are prepared and transmitted in Canada. Credentials are never
> shared and never used offshore."

And the global footer sentence that appears on every page (line 380):

> "Gondaliya CPA Professional Corporation is a CPA Ontario registered firm.
> Firm Registration 61330051."

## 5. Firm facts for /about/ (6(g), lines 1600-1612)

| Attribute | Value to publish | Match gondaliyacpa.ca | Match opencorporationfor35.ca |
|---|---|---|---|
| Legal name | Gondaliya CPA Professional Corporation | Yes | Yes |
| Department name | corpnilfilingfor300.ca, a department of Gondaliya CPA Professional Corporation | Yes | Yes |
| Years in practice | **Not published until reconciled** | Yes | Yes |
| Client count | **Not published until reconciled** | Yes | Yes |

Governing rule, line 1614: corpnilfilingfor300.ca publishes no review count, no
years-in-practice figure and no client count until a single number for each is
agreed and published identically on all three sites. The claim-consistency audit
is signed by Sharad and dated before the home page goes live.

Reason given: gondaliyacpa.ca currently shows 10, 15+ and 20+ years in three
places, 600+ clients on one page, and 500+ / 1300+ reviews in two places.

## 6. Internal contradiction to resolve with Sharad

The 6(g) table, line 1608, says **US licences: "Not published"** on
corpnilfilingfor300.ca — gondaliyacpa.ca only — with the note "WA 57629 and
MT PAC-CPAP-LIC-033176 are not relevant to a Canadian T2 service."

But Section 5.1 puts them in the About-page copy, and schema Block 4 carries
both as `hasCredential` entries. Two placements say publish, one says do not.

Two further placement mismatches, same pattern:
- Line 1606 assigns CPA Ontario 61040184 to `/cpa-ontario-registration/` and
  `/sharad-gondaliya-cpa/`; Section 5.1 also puts it on the About page.
- Line 1609 assigns Vandana Goel 61158584 to `/vandana-goel-cpa/` and
  `/our-cpas/`; Section 5.1 also puts her on the About page.

Line 2226 resolves these as within-family duplication, which is allowed: the
numbers "appear here and nowhere else in the body of other families."

## 7. Schema on this page

- **Block 2, AccountingService** — emitted on only four URLs: `/`, `/contact/`,
  `/about/` and `/nil-t2-filing-toronto/`, the four pages that display
  55 Queen St E, Suite 1205 as their own business location. On those four pages
  it **replaces** Block 1 Organization (line 543).
- **Block 4, Person Sharad Gondaliya** — `"url": "https://corpnilfilingfor300.ca/about/"`
- **Block 5, Person Vandana Goel** — `"url": "https://corpnilfilingfor300.ca/about/"`
- Forbidden, per Rule 6: no review or aggregateRating markup, no FAQPage, no HowTo.

Launch gate, line 371: AccountingService must appear on exactly 4 URLs and on no
other, verified by Rich Results Test, with no EFILE number and no CRA GroupID.

## 8. Internal linking (6(h), line 1537)

| Setting | Value |
|---|---|
| Minimum inbound links to each F15 page | 5 |
| Maximum outbound body links | 15 |
| Primary internal link targets for F15 | `/` and `/about/` |
| Anchor style | Page title |
| Audit cadence | Monthly |
| Owner | Navneet |
| Note | Footer links count toward inbound |

Link Whisper, line 1543: automatic linking is **off** for F15.

`/about/` is also one of the two primary link targets for the whole family, so
other F15 pages link to it.

## 9. Off-page use of this page

- 6(i) backlink plan, line 1632: for the month ending **October 20, 2026**,
  `/about/` and `/cpa-ontario-registration/` are the two primary assets offered.
  Target 2 new referring domains, 20 outreach contacts, foundational listings only.
- Brand-mention table, line 1625: directory and association listings, 2 linked
  mentions per month, pointing at `/about/`.

## 10. Freshness and refresh

- 7.9 freshness table, line 1572: F15 carries "Updated September 20, 2026" in the
  footer of the article body. Review half-yearly. One factual sentence per update.
- Refresh trigger table, line 2226: refresh on "a change to firm registration,
  membership numbers, address, hours or a policy." Maximum 12-month interval.
  Owner Sharad Gondaliya. The `cnf_last_verified_et` stamp advances on every
  firm-detail change.
- Line 1574: "A date is never moved without a content change. A template that
  stamps today's date on unchanged content is the exact pattern the March 2026
  spam update targeted."

## 11. Cross-site rule (line 1688)

`/about/` exists on all three sites. Overlap risk: Medium. Rule: "Firm facts
identical, page purpose different." Canonical: each site self-canonical. Action:
"Publish identical firm facts, different service paragraphs, on all three."

So the five Section 5.1 sentences and the firm facts are byte-identical across
the three sites; only the service paragraphs differ. On this site the service
paragraphs are about nil T2 filing at $300 including HST per tax year.

## 12. What the plan does NOT specify

- **No title tag, meta description or H1.** The 6(a) copy-paste exemplar for F15
  is `/t183corp-signing-explained/` (line 1176), not the About page.
- **No word count.** The plan sets no length anywhere for F15.
- **No section order.** Unlike the home page, which has the fixed 36-element
  order in Section 2.9, the About page has no prescribed structure.
- **No body copy** beyond the five Section 5.1 sentences, the EFILE paragraph and
  the firm facts.
- **No team photos, no bios, no history, no mission statement** are mentioned.

These are Navneet's to draft, within the Section 7.4 banned-phrase table and the
ten hard rules. They go to Sharad for sign-off like every other F15 page.
