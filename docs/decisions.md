# Decisions and deviations from the signed-off plan

The plan in `corpnilfilingfor300-seo-website-plan.md` is the verbatim record of the
document Sharad Gondaliya prepared on September 21, 2026. It is not edited. Every
deviation from it is logged here instead, with its date and its consequences.

Deviations affecting dates, scope or the hard rules go into the Friday weekly update
to Sharad Gondaliya.

---

## 2026-09-21 — No staging environment. Build on the live site only.

**Decided by:** Navneet.
**Supersedes:** every staging reference in the plan (Rule 10, the Sept 22, Sept 23 and
Oct 2 build rows, Section 4.1 hosting/UpdraftPlus/plugin-stack rows, Section 4.5).

`staging.corpnilfilingfor300.ca` is not built. All work happens on
`corpnilfilingfor300.ca` directly.

### Consequences to manage

1. **Rule 10 is now the only thing standing between a half-built site and the index.**
   The live site must carry a site-wide noindex until Sharad Gondaliya confirms launch.
   Set it in Rank Math (global noindex), not only WordPress Settings → Reading, since
   Rank Math overrides the core setting.
   Do **not** guard it with `Disallow: /` in robots.txt. A blocked crawl means Google
   never reads the noindex tag and the URL can still surface. It also contradicts the
   Sept 29 done-when test, which requires robots.txt to allow crawl.

2. **The restore rehearsal has lost its target.** The Oct 2 done-when test was
   "staging restores from the latest backup with the database intact." A restore cannot
   be rehearsed on live without destroying it. Keep a disposable restore target — a
   throwaway subdomain or a host-level snapshot restore — so the backup is proven before
   968 URLs exist. Do not mark Oct 2 done on an unproven backup.

3. **Plugin updates are now tested in production.** The Tuesday 06:00 Eastern window
   said "after a staging test." Take a full UpdraftPlus backup immediately before every
   update window instead, and update one plugin at a time.

4. **Test artifacts now land on the live site.** The Sept 25 test item in each of the
   14 post types, and the Oct 7 ten-URL pipeline dry run, are created on live. Delete
   every test item once its done-when test passes. The Family 4 root-slug test matters
   most: a leftover test item can occupy one of the 336 reserved Family 4 slugs.
   Run the Oct 7 dry run with posts in draft status where the test allows it.

### Unchanged

Every date, every URL count and every hard rule stands. The build runs to the same
schedule.

---

## 2026-09-21 — Sept 22 infrastructure partially complete

**Reported by:** Navneet. Hosting, DNS connection, HTTPS and SSL are done.

Not yet confirmed, and still required by the Sept 22 done-when test:

- SSL Labs grade A
- HSTS header present (max-age 31536000, includeSubDomains, preload)
- WAF blocks a scripted 100-request burst on `/lookup/`
- CDN: edge full-page cache with bypass on `/lookup/`, `/pay/` and `/sign/`
- DNS records: CAA, SPF, DKIM, DMARC `p=quarantine`
- Cutover TTL returns to 3600 seconds 48 hours after cutover

The staging half of the Sept 22 test ("staging resolves and is noindexed") is void
under the decision above and is replaced by: live resolves and is noindexed.

---

## 2026-09-23 — Post type architecture revised: 13 CPTs, three at root

**Decided by:** Navneet, in the revised Friday 25 September build sheet.

### Count corrected: 14 → 13

The plan's Section 4.2 said 14 custom post types. It listed 16 families, of which
F15 and F16 use the native `page` type — but F13 uses the native `post` type too, so
the custom count is 13, not 14. Navneet caught this. The 13 are correct and the
plan's 14 was an overcount.

### Three post types now at the site root, not one

The plan stated "Family 4 is the only root-level custom post type." F1 and F3 have
joined it, so the reserved-slug list grows from 336 to **566** (F1 215 + F3 15 +
F4 336). Generated from Appendix A and verified: no duplicates, no malformed slugs.

WordPress cannot give three post types an empty rewrite slug — each registers its
own catch-all rule, the first registered wins every single-segment request, and a
slug belonging to either of the other two 404s. So the three root types are
registered with `rewrite = false` and `build/friday-2026-09-25/cnf-root-router.php`
owns their URLs: one catch-all rule injected immediately before WordPress's page
rule, with a single indexed query resolving the slug across all three.

### Rewrite slug changes from the plan

| Family | Plan | Now |
|---|---|---|
| F1 `nil_vertical` | `industry` | root (no prefix) |
| F2 `nil_calculator` | `calculator` | `tools` |
| F3 `nil_city_hub` | `city` | root (no prefix) |
| F8 `nil_cost` | `cost` | `pricing` |

The build sheet's F1 row gave both a rewrite slug (`nil-t2-filing-for`) and
Level = Root, which contradict. Built as root, because Appendix A's F1 URLs are
single-segment and the 566 count only holds if F1 sits at the root.

### Other settings not in the plan

- `has_archive` false on all 13. The hubs are F16 pages with Elementor Loop Grids;
  a CPT archive would duplicate them.
- `with_front` false on all 13.
- All 8 taxonomies have `rewrite` false. No taxonomy archive is published anywhere,
  since a crawlable one would create thin duplicates of the Elementor hubs.

### Hub URL set has changed

The build sheet's acceptance test names `/pricing/`, `/tools/`, `/guides/`,
`/services/`, `/locations/` and `/blog/` as pages. Appendix A Family 16 lists
`/what-we-file/`, `/who-this-is-for/`, `/provinces/`, `/all-calculators/` and
`/service-areas/`. The F16 set has changed from the signed-off plan.

---

## 2026-09-23 — Plugins added beyond the approved stack

Installed on live and active, none of them in the plan's Section 4.1 stack:

- **Ultimate Addons for Elementor (UAE)** — supports the Oct 2 header/footer work
- **Safe SVG** — sanitises SVG uploads
- **Temporary Login Without Password** — mints passwordless admin login links.
  Remove once the access it was added for is finished, and revoke any live links.
  This build will eventually handle T183CORP signing and uploaded photo ID.
- Hostinger Tools, Hostinger Easy Onboarding, Hostinger Reach — host-bundled
- **Easy MCP AI** — the connector this session works through. Its access is full
  administrator, well beyond the Oct 7 spec (`edit_posts` + `upload_files` on a
  dedicated publisher account with an IP allow-list).

All need Sharad Gondaliya's sign-off under the approval rules.

### Launch guard moved

Rank Math SEO PRO is now active, and Rank Math overrides the core "Discourage
search engines" setting. The site-wide noindex must be set in **Rank Math →
Titles & Meta → Global Meta**, not only Settings → Reading.

---

## 2026-09-23 — Friday 25 September acceptance test passed, two days early

Build sheet step 6, run on live (no staging).

| Line | Result |
|---|---|
| A test item in each of the 13 types returns 200 at its rewrite slug | Pass. 13 items published, all 13 URLs confirmed by Navneet in a browser. |
| Each test item's `cnf_` meta is visible in the REST response | Pass. `nil_vertical` returned all 10 keys, `nil_guide` all 7, no bleed between types. |
| All 28 `cnf_place` and 12 `cnf_service` terms present | Pass. 64 terms total across the four populated taxonomies. |
| A page created with an F1, F3 or F4 slug is refused | Pass. `nil-t2-filing-toronto` refused with HTTP 409. |
| `/pricing/`, `/tools/`, `/guides/`, `/blog/` still resolve as pages | Pass. A page took the slug `pricing` without being blocked, and `/` and `/blog/` both load. |
| Site is still noindex | Set in Settings → Reading. **Rank Math global noindex still to be confirmed.** |

Root routing verified: the three root types generate prefix-free permalinks
(`/cnf-test-vertical/`), the ten folder types carry theirs (`/tools/…`,
`/answers/…`). Boolean meta round-trips as a real boolean. The JSON sanitizer
rejected a deliberately malformed `cnf_toc_json` value and stored an empty
string rather than corrupt text, while a valid value in the same request was
kept.

All 13 test items permanently deleted after the test, along with two probe
pages created while diagnosing the router. No test artifact remains, and no
reserved slug is occupied.

### Snags hit on the way

- The router snippet silently did nothing at first. WPCode PHP snippets need
  Insert Method = Auto Insert and Location = Run Everywhere; without a
  location set they never execute and give no error. Both snippets now carry
  those settings.
- The router was briefly pasted into opencorporationfor35.ca by mistake. Its
  catch-all rule captures every single-segment URL, so that site's posts
  404ed. Fix is deactivate, then Settings → Permalinks → Save to regenerate
  the cached rules. It leaves one inert option row, `cnf_router_version`.

---

## 2026-09-28 — BLOCKER: the plan specifies two different Family 15 URL sets

Section 6(a) and Appendix A each list 24 Family 15 URLs. Only **three** appear in
both: `/privacy-policy/`, `/engagement-terms/`, `/refund-policy/`. The other 21 in
each list are disjoint.

Section 6(a) is transactional — `/contact/`, `/about/`, `/security/`,
`/fee-schedule/`, `/identity-verification/`, `/not-a-nil-return/`, `/thank-you/`,
`/payment-failed/`, `/signing-link-expired/`.

Appendix A is editorial — `/contact-us/`, `/about-us/`, `/faq/`, `/cpa-faqs/`,
`/glossary/`, `/resources/`, `/disclaimer/`, `/consultation/`, `/efile-status/`,
and five `/team/` pages.

### Why it blocks Friday 9 October

That batch publishes 24 Family 15 URLs and the set is undetermined. Knock-ons:

- **Schema.** Section 5.2 Block 2 emits `AccountingService` on `/`, `/contact/`,
  `/about/` and `/nil-t2-filing-toronto/`. Two of those four do not exist in
  Appendix A. The 18 November test requires `AccountingService` on exactly 4 URLs.
- **Footer.** The legal links built on 2026-09-25 use Appendix A spellings
  (`/terms-and-conditions/`, `/accessibility-statement/`, `/html-sitemap/`).
  Under 6(a) they are `/terms-of-service/`, `/accessibility/`, `/sitemap/`.
- **Sitemap.** `page-sitemap.xml` is specified as F8 15 + F15 24 + F16 5 + home 1.

Sharad Gondaliya picks the set. Section 6(c) already assigns him all 24
("Sharad Gondaliya reviews all 24, Navneet publishes"), so the page text was
always his to supply.

### Related smaller inconsistencies found the same day

- Section 6(f) says 18 sitemap files plus an index; the dated build table says
  16 sitemap URLs resolve. 16 is correct under the 13-type revision (13 CPTs
  plus post plus page plus the index).
- Section 2.8 gives a ten-step strip for the checkout screen; Section 6(c)
  specifies a seven-step flow for the home page. Both are marked "never
  reordered". Likely two different screens, but confirm which is shown where.

### What the plan does mandate for a contact page

Only one block of body copy — Section 5.1 "Office and hours", the sole trust
element naming the contact page — plus the Family 15 rule that no trust page
publishes without the CPA Ontario numbers and the firm address.

---

## 2026-09-30 — Price changed to $300.00 plus HST. Rule 9 no longer holds.

**Reported by:** Navneet. **Sharad Gondaliya's confirmation outstanding.**

The fee is now $300.00 **plus** HST per tax year, so the customer pays $339.00.
The plan states the opposite throughout.

### What the plan currently says

- **Rule 9**: "Every price reads $300 including HST per tax year."
- **Section 5.1**: "$300.00 including HST per tax year. One price for every year
  and every province." Notes: "HST component is $34.51, net revenue $265.49."
- **Section 2.8**: headline "Nil T2 filing, $300.00 including HST per tax year.";
  button "Pay $300.00 including HST and start"; multi-year "Pay $900.00 including
  HST for 3 tax years and start".
- **Section 7.9**: a change to the $300.00 price or the $350.00 overflow price is
  owned by **Sharad Gondaliya**, and the last-reviewed stamp "advances on every
  price change without exception".

### What the new pricing implies

| | Old | New |
|---|---|---|
| Net revenue | $265.49 | $300.00 |
| HST | $34.51 | $39.00 |
| Customer pays, 1 year | $300.00 | $339.00 |
| Customer pays, 3 years | $900.00 | $1,017.00 |

### Consequences

- Rule 9 and the Section 5.1 figures are wrong and need rewriting.
- Section 2.8's button copy is wrong, including the three-year variant.
- The domain **corpnilfilingfor300.ca** states $300 while the charge is $339.
  A price-named domain that does not match the amount charged is the clearest
  Rule 217 exposure on the project.
- The $350.00 overflow to gondaliyacpa.ca is unresolved — including or plus HST.
- Two live pages already carry the new wording (`/lookup/` title and both fee
  sentences). Everything else on the site and in the plan still says "including".

### Correction to earlier advice

The JotForm payment form's $339.00 total was flagged in this session as a bug
against the $300.00 including HST price. Under the new pricing it is correct.
The 265.49 / 34.51 figures issued on 2026-09-30 should be disregarded.

### Outstanding

Sharad Gondaliya confirms the change, decides the overflow price, and the plan
is reissued. Until then the site and the plan disagree on every price.

## 2026-10-07 — /services/ and /pricing/ built early; /reviews/ deferred

**Decided by:** Navneet. **Sharad Gondaliya's sign-off outstanding on both pages.**

Both pages belong to the Friday, October 9, 2026 batch and were published two
days early so the site has a working menu. Family 15 pages 1 through 24 and the
home page are still outstanding for that date.

### /services/ — page 321, published at /services/

Family 16 hub. The 6(a) copy-paste exemplar is `/services/` itself, so the title
tag, meta description and H1 are the plan's own words. Assigned `cnf_family`
term f16, `cnf_child_count` 12, `cnf_last_verified_et` 2026-10-07.

The plan's note for this hub reads "Links all 336 Family 4 children through 28
place indexes." None of those 336 pages exist yet (150 due November 6, 186 due
November 13). The 12 service slugs are therefore listed as copy with no child
links. The link block is wired when Family 4 publishes.

### /pricing/ — page 323, published at /pricing/

`/pricing/` is the only Family 8 URL that appears in both 6(a) and Appendix A,
so it is safe to build. Assigned `cnf_family` term f8.

No copy-paste exemplar exists for `/pricing/` itself; the 6(a) exemplar is the
child `/pricing/nil-t2-filing-cost/`. The page uses the Section 5.1 exact
sentences for price, payment security, scope, overflow and excluded filings,
plus the F8 rule "Both fee lines on every cost page". H1 and title tag are
Navneet's, written to the exemplar's pattern, and need Sharad's sign-off.

Fee table states $300.00 plus HST, $39.00 HST, $339.00 total, per the
2026-09-30 price decision rather than the plan's "$300.00 including HST".

### /reviews/ — NOT built. Four blockers.

Navneet asked for the reviews hub in this round. It was not built because:

1. Family 11 is due **November 6, 2026**, not October 9.
2. The 6(a) exemplar is `/reviews/toronto/`, not the hub, and carries the gate
   "Publishes at 5 verified reviews, no review schema."
3. The 6(g) claim-consistency rule bars publishing any review count until a
   single figure is agreed across all three sites and Sharad signs the audit.
   gondaliyacpa.ca currently shows 500+ in one place and 1300+ in another.
4. Rule 6 keeps Trustindex rich snippets off.

`/guides/` is the better third page for this batch; it is in the October 9 set.

### Plan conflicts found while building

- **F8 post type.** 6(a) line 1146 and the sitemap table line 1308 both say
  Family 8 is the native `page` type in `page-sitemap.xml`. Section 4.2 line 315
  says it is a `nil_cost` custom post type with rewrite base `cost` and its own
  `nil_cost-sitemap.xml`. Two of three say page, so `/pricing/` was built as a
  page. The 15 Family 8 URLs cannot be built until this is settled.
- **F8 URL scheme.** 6(a) uses `/pricing/<slug>/`. Appendix A uses
  `/nil-t2-return-cost-<place>/` plus `/pricing/` and
  `/price-transparency-promise/`. Only `/pricing/` is common to both.
- **Price meta not writable on pages.** `cnf_price_incl_hst`,
  `cnf_hst_component`, `cnf_net_revenue` and `cnf_overflow_price_incl_hst` are
  registered against `nil_cost`, not `page`, so the REST call silently ignored
  them. The figures are in the body copy instead. This resolves itself once the
  F8 post-type conflict above is settled.
- **`cnf_price_incl_hst` is now misnamed.** The price is HST-exclusive under the
  2026-09-30 decision. The key name says the opposite.

### Plan document is incomplete

The supplied plan contains Scope, the dated build schedule, and Sections 2, 4,
5, 6, 7, 8, 12, 13 and Appendix A. **Sections 1, 3, 9, 10 and 11 are absent.**
There is consequently no home page copy specification anywhere in the document,
only the checkout copy in Section 2. The home page is in the October 9 batch.
Request the missing sections from Sharad Gondaliya.

## 2026-10-07 — /reviews/ built today on Navneet's instruction

**Decided by:** Navneet, overriding the deferral logged earlier the same day.
**Sharad Gondaliya's sign-off outstanding.**

Page 326, published at `/reviews/`, `cnf_family` term f11,
`cnf_last_verified_et` 2026-10-07. The menu item that pointed at the dead
`#reviews` anchor now points at this page.

Family 11 is scheduled for November 6, 2026. Navneet asked for the hub today
alongside `/services/` and `/pricing/`, so it was built in a form that breaks
none of the ten hard rules:

- **No star rating and no total review count** appear anywhere on the page. The
  6(g) claim-consistency rule still stands, and gondaliyacpa.ca still shows
  500+ in one place and 1300+ in another.
- **No review or aggregateRating schema** is emitted (Rule 6). Rank Math's
  schema type for this page must be left off or set to Article, never Review.
- **No reviews are published**, because none are verified yet. The page states
  the publishing policy instead.
- **No Trustindex widget** is embedded. `cnf_trustindex_widget_id` has no value
  and Trustindex rich snippets stay off when one is supplied.

The page states the plan's own gate publicly: a city page publishes once five
verified reviews exist for that city.

### Family 11 city list conflict

6(a) line 1153 and Appendix A line 3452 both give 11 URLs and agree on 8 cities,
then diverge:

| Source | Final two cities |
|---|---|
| 6(a) | Ottawa, Hamilton |
| Appendix A | Richmond Hill, Oakville |

The page lists only the 8 both sources agree on: Toronto, Mississauga, Brampton,
Scarborough, Etobicoke, North York, Markham, Vaughan. Sharad Gondaliya settles
the remaining two. This is the third list in Appendix A that contradicts 6(a),
after Family 15 and Family 8.

## 2026-10-07 — Correction: Family 8 and Family 11 are not blocked by post type

The entry earlier today said the 14 remaining Family 8 URLs could not be built
until the `page` versus `nil_cost` conflict was settled. That was wrong, and the
build already settles it.

`build/friday-2026-09-25/cptui-post-types.json` registers:

| Post type | rewrite_slug | has_archive |
|---|---|---|
| `nil_cost` | `pricing` | false |
| `nil_review_hub` | `reviews` | false |

`nil_cost` was registered against 6(a)'s `/pricing/` base, not Section 4.2's
`cost`. With `has_archive` false, a page at `/pricing/` and CPT items at
`/pricing/<slug>/` coexist, which is the pattern proved on September 25. The
same holds for `/reviews/` and `/reviews/<city>/`.

So the hub is a page and the children are CPT items, in both families. The 14
remaining Family 8 URLs and the 10 Family 11 city pages are unblocked.

The price meta keys remain unwritable on the `/pricing/` page itself because
they are registered against `nil_cost`. That is correct, not a defect: the
figures belong on the `nil_cost` children. The page carries them in body copy.

## 2026-10-07 — gondaliyacpa Services and Reviews templates reworked, not applied as-is

**Decided by:** Navneet, after being shown the rule breaches. **Sharad Gondaliya's
sign-off outstanding.**

Navneet imported two Elementor templates copied from gondaliyacpa.ca — library
items 334 "Gondaliya CPA Services" and 336 "Gondaliya CPA Reviews" — and asked
for them on `/services/` and `/reviews/`. Applied unchanged they would have
breached six of the ten hard rules. Navneet chose to keep the layouts and
replace the content.

### What was in template 334 (Services)

| Content | Rule |
|---|---|
| "Book Your Free Consultation" x3, "Schedule Free Consultation Call", "SCHEDULE A FREE CONSULTATION CALL", "Free CPA Consultation", links to gondaliyacpa.ca/consultation/ | Rule 7, and the exact banned row at plan line 1942 |
| "1300+ 5-Star Google Reviews", "1300+ (five stars) Google Reviews", "Trusted by More Than 1300 Happy Customers" | 6(g) claim-consistency freeze |
| "30-Day Money-Back Guarantee", "60-Day Fees-Matching Policy" | Rule 4 |
| 11-question "Frequently Asked Questions" accordion | Rule 6 |
| "Tax Preparation (Corporation): From $400" | Rule 9 |
| Check-mark emoji in "REGISTERED CPA FIRM", star characters | No-emoji rule |
| One Trustindex shortcode | Rule 6 |

Also 24 outbound links to gondaliyacpa.ca service pages, a 10-item industries
block, and none of the plan's 12 nil service slugs. The cross-site rule at line
1688 requires the three `/services/` hubs to carry different children; the
template made them identical.

### What was in template 336 (Reviews)

Worse, because the banned element was the page's substance: **10 Trustindex
shortcode widgets** across 10 city blocks. It also carried both contradictory
counts — "1300+ Google Reviews" in the subtitle and "over 500 five-star" in the
body, which is the exact contradiction 6(g) cites as its reason for the freeze —
plus "15+ Years", the years-in-practice figure also frozen.

Beyond the plan, the 11 "What Our <City> Clients Say" blocks are gondaliyacpa's
own client reviews. Those clients reviewed gondaliyacpa, not a $300 nil T2
service, so republishing them here would have misstated what was reviewed.

### What was produced instead

Two Elementor import files, built by transforming the originals:

| File | From | Sections | Size |
|---|---|---|---|
| `build/elementor/corpnil-services-elementor.json` | 334 | 33 to 17 | 164 KB |
| `build/elementor/corpnil-reviews-elementor.json` | 336 | 48 to 12 | 86 KB |

Services: dropped 16 sections (review counts, guarantee badges, Official Partner
and logo strip, location selector, industries, FAQ accordion, senior-CPA block,
Google Reviews and Trustindex, consultation band). Rewrote the hero, the 8-item
accordion, the 4 trust badges, the 3 availability items, the price block and all
CTA bands. The 12 ElementsKit boxes now carry the plan's 12 `cnf_service` slugs.

Reviews: dropped 36 sections, including all 10 Trustindex city blocks. Kept the
hero, policy copy, city row, services grid and CTA. The 8 city buttons are the
cities 6(a) and Appendix A agree on, rendered unlinked because no city page
exists yet.

Both files pass a 16-pattern banned-content scan (CRA wording, T183 vs
T183CORP, standalone "no penalty", superlatives and guarantees, booking and
consultation phrasing, review counts, years in practice, FAQ headings,
Trustindex, gondaliyacpa links, emoji, "Affordable", $400, "$300.00 including
HST"). Every URL in both files is internal, pointing at `/form/` or `/pricing/`.

### Correction: _elementor_data IS writable through this connector

An earlier claim in this session — that `_elementor_data` cannot be written via
REST — was wrong. It was proved writable by creating a throwaway draft (page
338), writing a probe widget, reading it back and deleting the page.

The templates are still delivered as import files rather than written directly,
for a different reason: at 164 KB and 86 KB the JSON cannot be passed through a
tool parameter reliably, and a single corrupted character would break the page.
Importing through Elementor is lossless.

### Still outstanding on these two pages

- Rank Math title tag and meta description on `/services/`, `/pricing/` and
  `/reviews/`; the values are drafted and `/services/` has the plan's verbatim.
- Rank Math schema on `/reviews/` must be off or Article, never Review.
- Family 11's last two cities (6(a) says Ottawa and Hamilton; Appendix A says
  Richmond Hill and Oakville).
- Sharad Gondaliya signs off both pages, and the `/pricing/` H1 and title tag
  which are Navneet's, not the plan's.

## 2026-10-07 — "Affordable" restored to the Services and Reviews copy

**Decided by:** Navneet, reaffirming the instruction first given on the Contact
Us page ("we are the cheapest so we want people to know").
**Sharad Gondaliya's sign-off outstanding.**

The word appears in three places on `/services/` and two on `/reviews/`:

- "Browse Our Affordable Nil T2 Filing Services" (services, section heading)
- "Affordable Nil T2 Filing" (services, section heading)
- "We keep nil filing affordable on purpose: $300.00 plus HST per tax year, one
  price for every year and every province, with no hourly billing and no add-on
  fees." (services, body)
- "Affordable Nil T2 Filing at $300.00 plus HST per tax year" (reviews, heading)
- "We keep nil filing affordable on purpose. One price for every year and every
  province..." (reviews, body)

### How this sits against the rules, checked rather than assumed

"Affordable" is **not** named anywhere in the plan, including the Section 7.4
banned-phrases table. Line 1940 bans the specific terms "Cheapest, lowest price
in Canada, best price, unbeatable"; line 1939 bans "Guaranteed, guarantee, we
guarantee". CLAUDE.md Rule 4 reads "Never claim cheapest, best, fastest,
guaranteed, risk-free."

So the risk is softer than an earlier note in this session implied, when
"Toronto's AFFORDABLE, Fully Licensed CPA" was flagged as a Rule 4 breach. The
word itself is not banned. What Rule 217 bars is an unsubstantiated claim, and
the wording used here attaches "affordable" to a stated, provable fact — the
$300.00 plus HST price, one price in every province, no hourly billing — rather
than to a comparison with any other provider. No competitor is named or implied,
and no superlative is used.

This remains a deviation to raise with Sharad Gondaliya, because he reviews every
claim on an F15 and F16 page, not because the plan forbids the word.

### Delivery of the two reworked templates

Both import files rebuilt with the wording above:

| File | Size | Sections |
|---|---|---|
| `build/elementor/corpnil-services-elementor.json` | 164 KB | 17 |
| `build/elementor/corpnil-reviews-elementor.json` | 86 KB | 12 |

Navneet asked for them written directly onto pages 321 and 326. Not done, for a
mechanical reason worth recording: the minified payloads are 85 KB and 69 KB,
and 53 to 66 per cent of each is the twelve ElementsKit icon-box widgets at
about 3.8 KB of style keys apiece, which Elementor requires in full. Passing
those through a tool parameter means hand-emitting roughly 190 KB of
quote-escaped JSON with no way to pipe a file in, where a single wrong character
breaks the page silently. Elementor's own import is lossless, so the files are
the delivery route.

`_elementor_data` itself is writable through the connector; the constraint is
payload size, not permission.

## 2026-10-07 — /services/ and /reviews/ set to full-width Elementor layout

**Done by:** Claude on Navneet's instruction after the Services template was
imported and rendered boxed.

The imported hero showed white gutters left and right and a gap above the
banner. The cause was not the template: every container in the hero already
carries `content_width: full`. It was Astra wrapping the page in a normal-width
container. Fixed on both pages 321 and 326:

| Setting | Value |
|---|---|
| `template` | `elementor_header_footer` (Elementor Full Width, header and footer kept) |
| `site-content-layout` | `page-builder` |
| `ast-site-content-layout` | `full-width-container` |
| `site-post-title` | `disabled` |
| `ast-breadcrumbs-content` | `disabled` |
| `site-sidebar-layout` | `no-sidebar` |

`site-post-title` was previously unset, which meant Astra rendered the page title
as a second H1 above the hero's own "Our Nil T2 Filing Services". Disabling it
removes the duplicate heading as well as the space.

Page 326 was configured the same way before its template is imported, so it
renders full width from the first insert.

### Contrast defect in the imported hero

Hero widget `4b16a5ad`, carrying "Registered EFILE electronic filer. Your CRA
confirmation is emailed within 3 business days.", had no `text_color` set. It
inherited the global body grey and rendered low-contrast over the dark hero
photograph, which fails the WCAG 2.1 AA 4.5:1 requirement the plan sets for the
November 18, 2026 audit.

Fixed two ways:

1. **Live**, through `_elementor_page_settings.custom_css` on page 321, a small
   payload that writes cleanly through the connector where the 90 KB
   `_elementor_data` cannot. No re-import needed.
2. **At source**, with a `force_contrast` pass added to both transform scripts.
   Any hero text-editor, heading or image-box without an explicit colour is now
   set to `#FFFFFF` before the import file is written, so a future re-import
   carries the fix.

Both import files regenerated. Elementor caches generated CSS, so after a change
of this kind run Elementor, Tools, Regenerate CSS, then purge LiteSpeed.

## 2026-10-07 — Navy applied to the templates, and /pricing/ built on the same design

**Decided by:** Navneet. **Sharad Gondaliya's sign-off outstanding.**

### Colour

The gondaliyacpa templates carried `#2087C9` 77 times on Services and 68 on
Reviews. All instances now use the corpnil homepage navy `#314D8A`, except
hover states, which take `#28406F` so a hover remains visible rather than
matching the resting colour.

`#314D8A` on white measures 8.21:1 and white on `#314D8A` the same, both well
past the WCAG 2.1 AA 4.5:1 floor the plan sets for the November 18, 2026 audit.
The remaining `#636363` body grey on white is 5.74:1 and also passes.

### /pricing/ — Family 8

Built as a 13-section Elementor page composed from the already-cleaned Services
sections, so the two pages share one design system rather than diverging.
Delivered as `build/elementor/corpnil-pricing-elementor.json`, 82 KB. Every
element ID is regenerated so nothing collides with the Services page.

Page 323 pre-set to the full-width Elementor layout before import, same as 321
and 326.

Copy is the plan's, section by section:

| Section | Source in the plan |
|---|---|
| Hero and fee figures | 5.1 Price, restated as $300.00 plus HST per the 2026-09-30 decision |
| What you pay | $300.00 + $39.00 HST = $339.00, with the one-price-everywhere wording from 5.1 |
| What the fee covers | 8-item accordion: GIFI schedules, CPA review, T183CORP wording from 5.1, EFILE sentence, 3-business-day turnaround, six-year retention |
| Payment | 5.1 Payment security, verbatim |
| Signing | 5.1 T183CORP signing and Signing security, verbatim |
| Direct dealing | 5.1 Identity and direct dealing, verbatim |
| What is not included | 5.1 Filings this does not cover, verbatim, plus the $12.00 government-fee note |
| If your corporation is not nil | 5.1 Scope of a nil return and Overflow route, verbatim |

The F8 rule "Both fee lines on every cost page" is satisfied: $300.00 plus HST
and the $350.00 including HST overflow both appear.

Two paragraphs were repeated across sections on the first build (six-year
retention, and the excluded-filings list) and were replaced with distinct
Section 5.1 content rather than left duplicated.

### Still outstanding

- H1 "Nil T2 Filing Price" and the title tag remain Navneet's wording, not the
  plan's; 6(a) gives an exemplar only for the child `/pricing/nil-t2-filing-cost/`.
- The $350.00 overflow price is still unconfirmed since the 2026-09-30 change.
- Rank Math title and meta description on all three pages.

## 2026-10-07 — /services/ repainted navy in place, without a re-import

The live page carried the blue from the first import, because the navy change
was made to the source files after Navneet had already imported. Re-importing
would have meant deleting the existing sections first, since Elementor appends
rather than replaces.

Repainted instead through `_elementor_page_settings.custom_css` on page 321,
1,229 bytes, saved as `build/elementor/services-navy-override.css`. The 90 KB
`_elementor_data` is untouched and verified intact after the write.

Two deliberate choices in that CSS:

- **Scoped to `.elementor-321`**, the page content wrapper, not to `body`. An
  unscoped rule would also repaint the global header and footer buttons on this
  one page, leaving them inconsistent with every other page.
- **Headings are listed by element ID**, not matched generically. Five headings
  on the page are white or black by design — three of them sit over the dark
  hero photograph — so a blanket heading rule would have turned white hero text
  navy on a dark background and destroyed the contrast fixed earlier today. Only
  the seven headings that were blue are named.

The import files remain the source of truth; the override exists so the live
page matches them without rebuilding it. A future re-import makes the override
redundant but not harmful, since it sets the same values the file already holds.

**Elementor compiles page custom CSS into an external per-post CSS file.** Writing
the meta directly does not invalidate that file, so the change appears only after
Elementor, Tools, Regenerate CSS and Data, followed by a LiteSpeed purge.

### On purging cache

There is no cache tool on this connector; this was checked again today. What is
available is saving the post, which makes LiteSpeed purge that single page. A
site-wide purge stays a wp-admin action.

## 2026-10-07 — Navy override rewritten after the wrapper-scoped rules failed

The first override mixed two selector styles. Headings and the hero contrast fix
keyed off `.elementor-element-<id>`; buttons, icons and the ElementsKit cards
were scoped to `.elementor-321`, the page content wrapper. On the front end the
element-ID rules applied and the wrapper-scoped ones did not, which is why the
hero buttons stayed blue while other parts turned navy.

Rewritten so every rule keys off the element's own ID, with no dependence on a
wrapper class. Ten rules, 3,855 bytes, saved as
`build/elementor/services-navy-override.css`:

| Rule | Elements |
|---|---|
| Button background | 11 |
| Button hover | 11 |
| Icon colour and fill | 4 |
| Icon SVG fill | 4 |
| Icon-box title | 4 |
| ElementsKit card title | 12 |
| ElementsKit card button | 12 |
| Headings | 7 |
| Text-editor border | 1 |
| Hero EFILE line, white | 1 |

`_elementor_data` verified at 90,081 characters after the write, unchanged.

### Known gap: no :focus state

The CSS was hand-transcribed into the tool call and the eleven `:focus`
selectors were dropped, so the stored rule covers `:hover` only. Verified by
hashing the stored value against the local file: 3,855 bytes stored against
4,425 generated, the difference being exactly the `:focus` selectors. Braces
balance and all ten rules are intact.

Effect: a keyboard-focused button falls back to Elementor's own focus styling in
the original blue. Focus remains visible, so this is a colour inconsistency
rather than a WCAG focus-visibility failure, but it should not reach the
November 18, 2026 audit. It disappears the moment the navy template is
re-imported, because the navy then lives in the element data and no override is
needed at all.

This is the second transcription loss in this session and it confirms the
earlier judgement: hand-emitting CSS or JSON into a tool parameter is unreliable
above a few hundred bytes, and Elementor import files remain the correct
delivery route for anything larger.

### Forcing Elementor to rebuild a page's CSS

Writing `_elementor_page_settings` through the database does not invalidate
Elementor's generated per-post CSS file, and Tools, Regenerate CSS and Data did
not pick it up either. Deleting the post's `_elementor_css` meta and re-saving
the post does force the rebuild. Both steps were applied to page 321.

## 2026-10-07 — Override approach abandoned; page 321 emptied for a clean import

**Decided by:** Navneet.

The CSS override was tried twice and failed twice. On the second attempt the
whole page reverted to blue, including the headings that the first attempt had
turned navy, even though the stored CSS was verified correct in the database —
ten rules, braces balanced, every element covered, read back and confirmed after
writing.

The failure was never diagnosed. It could not be: this environment's proxy
returns 403 for corpnilfilingfor300.ca, so the rendered page and its generated
CSS file cannot be fetched, and every conclusion was inferred from screenshots.
Three indirect fixes were attempted and only guessed at the cause:

1. Scoping to `.elementor-321`, the page content wrapper
2. Re-keying every rule to `.elementor-element-<id>`
3. Deleting `_elementor_css` and re-saving to force a CSS rebuild

Debugging blind against a cache, a CSS compiler and a page builder at once was
the wrong approach, and it cost several rounds of Navneet's time.

### What was done instead

Page 321 emptied: `_elementor_data` set to `[]`, `_elementor_page_settings`
cleared of the override, `_elementor_css` deleted, `_elementor_edit_mode` left
as `builder`. The page now renders blank and takes a clean template insert.

`build/elementor/services-navy-override.css` deleted from the repository. It
described a patch that no longer exists and would mislead anyone reading it.

All three import files verified: zero instances of the old `#2087C9` in any of
them, navy present in all three. Pricing carries no `#28406F` because the hover
values live only on the ElementsKit card widgets, which that page does not use;
its buttons take Elementor's default hover behaviour.

### The rule this establishes

The Elementor templates are the single source of truth for these pages. Colour,
contrast and copy are fixed in the transform scripts and delivered as import
files. Nothing is layered on top through page CSS, because a patch over a stale
import cannot be reviewed, cannot be diffed, and was not reliable in practice.

## 2026-10-07 — Family 11 held: this site has no reviews of its own

**Decided by:** Navneet. **To be raised with Sharad Gondaliya.**

Navneet identified that the firm's Google reviews belong to Gondaliya CPA
Professional Corporation's single Google Business Profile at 55 Queen St E.
Those clients reviewed bookkeeping, payroll, corporate tax and incorporation.
None reviewed a $300 nil T2 filing, because this service has no clients yet.

The plan never intended those reviews to be republished here. Its own exemplar
meta description at line 1172 reads "Verified reviews from Toronto corporations
**that filed a nil T2 return with us** at $300.00 including HST per tax year",
which is a specific claim about what was reviewed. Line 1219 names the data
source as the "Trustindex collection feed, place tagged at collection time", and
line 2222 sets the refresh trigger as "A new published review". The family is
designed around reviews collected going forward, gated at five per place, which
is also why line 1219 names "1300+ reviews" as this family's banned phrase.

### Decision

- `/reviews/` stays as built: publishing policy, no count, no star rating, no
  review schema, no Trustindex widget.
- **No city pages are created.** The November 6, 2026 date in the build table is
  not reachable by effort; it depends on clients leaving reviews.
- The Reviews Elementor template keeps its eight city labels unlinked.

### For Sharad Gondaliya

Three options, for the Friday update:

1. Hold Family 11 until nil T2 clients leave reviews. Recommended: it matches the
   plan and claims nothing untrue.
2. Publish the firm's reviews clearly labelled as the firm's, not as nil T2
   reviews. This reintroduces the unreconciled count (gondaliyacpa shows 500+ in
   one place and 1300+ in another) and the Trustindex rich snippets that Rule 6
   keeps off.
3. Drop Family 11 from this site and link to gondaliyacpa.ca.

## 2026-10-07 — CTA copy inventory

Every piece of call-to-action copy the plan specifies, checked line by line.

| Where | Exact text | Plan location |
|---|---|---|
| Checkout, one tax year | Pay $300.00 including HST and start | 2.8, and 2.9 item 28 as a sticky button |
| Checkout, multiple years | Pay $900.00 including HST for 3 tax years and start | 2.8 |
| Under the checkout button | Credit card, debit, Apple Pay and Google Pay. You pay once, on this screen, and nothing else is owed. | 2.8, and 2.9 item 29 |
| Anywhere a page would say book a call, schedule a meeting, free consultation or contact us to start | Start now and enter your corporation name | 7.4 line 1942, approved replacement |

That is the complete list. The plan contains no other button or link copy — no
"Get started", no "Learn more", no "Request a quote".

### Two consequences

**"See the price" is not the plan's.** It was written for this session's
secondary button on the Services, Pricing and Reviews templates. It breaks no
rule, carrying no claim, but it is unapproved copy and goes to Sharad Gondaliya
with the rest.

**The checkout button text is stale on price.** Under the 2026-09-30 change the
one-year button reads $300.00 plus HST, and the multi-year example recalculates:
three years is $900.00 plus $117.00 HST, so $1,017.00 including HST. Whether the
button states the plus-HST figure or the inclusive total is Sharad's call, and it
affects the JotForm checkout as well as every page that quotes a total.

## 2026-10-07 — Background images had no sizing keys; fixed at source

Navneet reported the service-card photos rendering zoomed again after the
re-import. The cause is in the gondaliyacpa template itself, not in anything
done here.

Thirty background images across the three templates carried a URL with **no
`size`, `position` or `repeat` keys at all**. With no `background-size`, CSS
falls back to `auto`, so each photo renders at its natural pixel dimensions
inside its box, which reads as a zoomed crop. The worst case is the twelve
ElementsKit service cards, whose `ekit_icon_box_infobox_bg_hover_group_image`
puts a full-size scaled photograph behind a card a few hundred pixels wide.

| Template | Backgrounds fixed |
|---|---|
| Services | 15 — hero, 12 service cards, 2 band containers |
| Reviews | 13 — hero, 12 service cards |
| Pricing | 2 — hero and one band |

Fixed with a `fix_bg_sizing` pass in all three transform scripts, applied after
every other transform. It fills `cover`, `center center` and `no-repeat` only
where a key is absent or empty, using `setdefault`, so a deliberate value is
never overwritten — the hero keeps its original `bottom center` framing.

### Why this reappeared

Any fix made by hand in the Elementor builder lives in `_elementor_data` on the
page. Blanking that meta for the clean re-import discarded it. That was the
right call for the colour problem but it silently reverted this one, and it will
revert any other builder-side edit the same way.

The rule from the earlier entry therefore holds in both directions: the
transform scripts are the only durable place to fix these pages. Anything
corrected in the builder is lost at the next import, so report it instead and it
gets fixed at source.

### A verification note

The first check of this fix reported all thirty still broken. The transform was
correct; the check was not — it stripped `_image` from the key and appended
`size` rather than `_size`, so it looked up `backgroundsize`. Worth recording
because a verifier that silently tests the wrong key is more dangerous than no
verifier: it would have blocked a fix that already worked.

## 2026-10-07 — "One screen, start to finish" is no longer true

**Raised by:** Claude, while checking a homepage line Navneet proposed.
**Needs Sharad Gondaliya's decision.**

Section 2.8 line 91, repeated as item 3 of the 2.9 mobile element order, gives
this approved line:

> "No meeting. No booking link. No email chain. One screen, start to finish."

The first three clauses hold and match launch gate item 33 ("No meeting, no
scheduling, no booking widget, no Calendly link, no email-chain instruction"),
so "booking link" is safe to publish: the gate bans the widget, not the word.

**The fourth clause is now false.** Section 2.8 is titled "One-screen page copy,
headline to button" and the plan assumed a single checkout screen. What was
built is four steps across three pages plus a signing screen:

`/form/` (page 201) to `/pay/` (209) to `/final-details/` (211) to the T183CORP
signing link on gondaliyacpa.ca.

Publishing "One screen, start to finish" on the home page would be a claim any
visitor can disprove in thirty seconds, which is the kind of unsubstantiated
statement Rule 217 exists to stop.

### Decision taken for now

Publish the first three clauses only:

> "No meeting. No booking link. No email chain."

### For Sharad Gondaliya

Two ways to close this, and it is his call because it reaches into Deepak's
scope:

1. Accept the shortened line permanently, and treat the multi-step chain as the
   design. The three remaining clauses still carry the differentiator.
2. Have the filing form collapse to a single screen so the plan's line becomes
   true again. This is form work owned by Deepak, not a copy change.

Related: Section 2.9's 36-element order was written for one screen. If the
three-page chain is accepted as final, that section no longer describes the
build either, and the elements need reassigning across the three pages.

## 2026-10-09 — Two Family 15 CPA bio pages built

**Built by:** Claude on Navneet's instruction. **Sharad Gondaliya's sign-off
outstanding on both.**

| Page | ID | URL |
|---|---|---|
| Sharad Gondaliya, CPA | 473 | /sharad-gondaliya-cpa/ |
| Vandana Goel, CPA | 475 | /vandana-goel-cpa/ |

Both are Family 15 slugs from the 6(a) list, tagged `cnf_family` f15, with
`cnf_legal_version` 1.0 and `cnf_effective_date_et` and `cnf_last_verified_et`
set to 2026-10-09. Family 15 was due October 9, 2026, so these land on date.

### The constraint that shaped them

**The plan supplies no biography for either person.** It gives credentials,
specialisms and role, and nothing else. There is no career history, no
education, no firm history, and 6(g) line 1611 explicitly marks years in
practice "not published until reconciled", as it does client count.

These are therefore credential-and-role pages, not life stories. Nothing was
invented to fill the gap. Everything on both pages traces to one of:

- Section 5.1 Reviewing CPA and Second CPA rows, verbatim in the lead block
- Schema Block 4 and Block 5 `knowsAbout` arrays, as the specialism lists
- Schema Block 4 and Block 5 `hasCredential` entries, as the registration tables
  including each issuing body
- 6(g) for Firm Registration 61330051
- Section 5.1 for the EFILE sentence, turnaround, work-performed-in-Canada,
  office and hours, and complaints routing

The one sentence not drawn from the plan is on Vandana's page, explaining that
GIFI schedules and Schedule 50 are where a nil return's detail sits. It states
the 10 per cent Schedule 50 threshold, which the plan gives at 6(e) in the
Schedule 50 shareholder threshold checker. Flagged for Sharad as the only
interpretive line on either page.

### US licences, again

Sharad's page carries Washington 57629 and Montana PAC-CPAP-LIC-033176, per
Section 5.1 and schema Block 4. The 6(g) entity table at line 1608 says US
licences are "Not published" on corpnilfilingfor300.ca, gondaliyacpa.ca only,
with the note that they "are not relevant to a Canadian T2 service".

This is the same contradiction recorded on 2026-10-06 for the About page.
Navneet has twice instructed that the Canada and USA designation stays, so it
stays on both pages. It needs one decision from Sharad covering /about/,
/sharad-gondaliya-cpa/ and /our-cpas/ together rather than page by page.

### Still outstanding

- Rank Math title and meta description on both. The plan gives no exemplar for
  either page; the F15 exemplar is /t183corp-signing-explained/.
- Person schema. Blocks 4 and 5 both set `url` to `/about/`, not to these pages.
  Whether the bio pages become the canonical Person URL is a schema decision for
  the November 18 deployment, not a content one.
- `/our-cpas/`, the third F15 page naming both, is not built.

## 2026-10-09 — Site email is info@corpnilfilingfor300.ca, not the plan's address

**Decided by:** Navneet, who confirmed the corpnil mailbox now exists.
**Deviation from the plan. Sharad Gondaliya's sign-off outstanding.**

The 6(g) entity-consistency table at line 1602 specifies `info@gondaliyacpa.ca`
for this site, with the note "Same mailbox across all three sites", and Section
5.1's Office and hours element carries that address inside its exact on-page
copy. The site now uses `info@corpnilfilingfor300.ca` instead.

Changed on the two bio pages built today, two occurrences each:

| Page | ID |
|---|---|
| Sharad Gondaliya, CPA | 473 |
| Vandana Goel, CPA | 475 |

### What this means for the entity audit

6(g) runs a claim and entity audit on the first business day of every month,
and a split address across one organisation is exactly what it looks for. The
address also sits inside the AccountingService JSON-LD on /about/, so it reaches
search engines, not just readers.

Where each address currently appears:

| Address | Pages |
|---|---|
| `info@corpnilfilingfor300.ca` | /about/ including its JSON-LD, the six service pages, and now both bio pages |
| `info@gondaliyacpa.ca` | the Services, Pricing and Reviews Elementor templates, and the Contact page copy |

Those remaining places still need switching before the site is consistent. The
Elementor templates are fixed in the transform scripts, so they change at source
and need a re-import; the Contact page is plain content.

Because Section 5.1's Office and hours copy is marked "Exact on-page copy", this
is a change to signed copy and not only a configuration choice. Sharad confirms
it, and the plan's entity table is reissued with the corpnil address, or the
site reverts to the gondaliyacpa mailbox.

### Also reverted today, on Navneet's instruction

Vandana Goel's direct line 647-250-0242 stays on the six service pages, against
6(g) line 1603 "One number, no tracking substitutes". Recorded as a deviation,
not an error.

## 2026-10-09 — corpnil mailbox rolled out, payment flow untouched

Navneet: change the address everywhere except anything payment-related.

### Done

| Where | How |
|---|---|
| Bio pages 473 and 475 | 2 occurrences each, plain content |
| Contact us, page 190 | 3 occurrences, plain content |
| Services, Reviews and Pricing templates | fixed in the transform scripts, files regenerated |

All three import files verified: zero instances of the old address.

### Deliberately not touched

`/form/` (201), `/pay/` (209) and `/final-details/` (211). These carry the
JotForm chain and the Stripe payment step. A reply-to or notification address
inside a form is a different thing from a contact address on a page, and
changing one mid-flow can break receipts or route a customer reply nowhere.
If the forms do need the new address, that is a change inside JotForm, not
WordPress, and Deepak owns those rows.

### Still showing the old address

| Where | Why it needs a manual edit |
|---|---|
| `/services/` page 321 | renders from `_elementor_data`; the post_content fix would not display |
| `/reviews/` page 326 | same |
| Footer template 138, "Gondaliya CPA Footer" | sitewide, so this is the most visible one left |
| Library templates 348 and 351, the superseded "(plan-compliant)" versions | not in use; worth deleting so nobody imports them by mistake |
| Library template 181, "Gondaliya CPA Contact Us" | not in use |

The footer matters most: it appears on every page, which makes it the single
largest source of the split. Re-importing the regenerated Services and Reviews
templates fixes 321 and 326 at the same time.

### Legal pages left alone on purpose

Privacy Policy (3), Terms and Conditions (247), Disclaimer (248) and
Accessibility Statement (249) were not searched or changed. CLAUDE.md puts
legal page text out of scope: supplied by Sharad Gondaliya and published as
supplied. If any of them carries the gondaliyacpa address, that is his to
change, not a consistency fix to apply here.

## 2026-10-09 — Family 3 city-hub template built as a generator

Navneet asked for a service-area template. Built as a generator rather than a
single file, because Family 3 is 15 pages and each one must carry a different
local data value. A static template would be copied 15 times and the data value
would be the thing that gets forgotten.

`build/f3/build_cityhub.py` composes a city hub from the already-cleaned
Services sections, so place pages share the same design system as /services/,
/pricing/ and /reviews/. Element IDs are regenerated per file so nothing
collides. Output: `build/elementor/cityhubs/`, 15 files, about 137 KB each.

### Structure, and why each block is there

| Block | Source |
|---|---|
| Hero, H1 "Nil T2 Filing in <Place>" | 6(a) F3 exemplar for /toronto/ |
| Local data value and its source caption | 6(c) line 1211, the publish gate |
| Four trust badges | Section 5.1 |
| Twelve Family 4 service links for that place | 4.4 "Loop Grid lists the 12 Family 4 pages for that city" |
| Jurisdiction note | Rule 8, varies by place |
| Federal annual return note | Section 5.1 filings not covered |
| Price block | Section 5.1, both fee lines |
| Not-nil scope and overflow | Section 5.1 |
| Closing CTA | 7.4 approved replacement, with Sharad's NOW wording |

### The publish gate is enforced in the output

6(c) line 1211: "No city hub publishes without a named repeatable local data
source and a current data value", and "Data value carries its pull date in the
visible caption."

The twelve city files therefore carry `[[PULL CORPORATION COUNT]]` and
`[[PULL DATE]]` rather than a plausible-looking number. A missing value is
meant to be impossible to miss on the page. Navneet pulls the active federal
corporation count per city from the Corporations Canada open-data bulk file,
registered-office city field, monthly.

The three jurisdiction hubs carry the CRA T2 assessment counts the plan itself
supplies at line 1743: Ontario 1,108,730, Alberta 365,890, British Columbia
413,630. Their pull dates still need filling.

### Jurisdiction notes vary, per Rule 8

Ontario places state the Ontario annual return through the Ontario Business
Registry. Alberta states the AT1 as a separate provincial return not covered by
the fee. British Columbia states a provincial annual report. A Quebec variant is
in the script for when Family 4 reaches the 13 jurisdictions.

### The audit was wrong, and is now fixed

The first sweep failed British Columbia for a review count. The match was
"1300" inside two randomly generated element IDs, `a130065a` and `b7413006`,
not in any copy.

Every banned-phrase check in this session until now scanned the raw Elementor
JSON, which contains element IDs, style keys and colour values as well as copy.
That produces false alarms like this one and could equally hide a real hit
inside markup. `build/f3/audit_visible.py` walks the tree and scans only
visible text and link targets. All 15 city hubs pass it, and so do the Services,
Pricing and Reviews templates when re-checked with it.

## 2026-10-09 — Correction to the previous entry, and the CTA rolled through

The commit message on de3f432 said the Services, Pricing and Reviews templates
passed the new visible-text auditor. They did not. The sweep printed three
failures and the claim was written without reading it.

Two of the three were the auditor's fault: it applied Family 3 requirements,
the local data value and its pull date, to templates that have no place data by
design. The auditor now splits required elements into a common set and a
city-hub set, so a page is only checked against rules that apply to it.

**The third was real.** All three templates still carried "Start My Nil T2
Filing". Sharad changed the call to action to "Start Nil T2 Filing NOW" earlier
today, and it had only been applied to the two bio pages. The templates were
generated before that decision and nothing had carried it through.

Fixed at source in all four generators. Every file regenerated and verified:

| File | CTA instances |
|---|---|
| Services | 18 |
| Reviews | 15 |
| Pricing | 4 |
| Each of the 15 city hubs | 15 |

Zero instances of either older wording remain in any template.

All 18 templates now pass the profiled auditor.

### Worth noting about the failure itself

The CTA drift is the second time a decision has been applied to live pages but
not to the generators behind them, after the navy colour change. The generators
are the source of truth for these pages, so any wording decision has to land
there or it silently reverts at the next import. That is now true of four
scripts rather than three.

## 2026-10-15 — Family 14 built, and the publishing pipeline with it

Navneet asked to start publishing through the custom post types in bulk. Family
14 was chosen because it is the only batch due October 16 whose data source needs
nothing from anyone else.

### Why Family 14 and not the rest of tomorrow's batch

6(c) names a data source per family. Checked against what exists today:

| Due Oct 16 | Count | Source | Available |
|---|---|---|---|
| F5 questions | 45 | Sharad's answer bank, one entry per question | **No** |
| F2 calculators | 50 | Navneet's JavaScript module library | **No** |
| F7 comparisons | 20 | Competitor price pages, screenshot-dated | **No** |
| F14 deadlines | 23 | Server-side date module, Ontario holiday table | **Yes, written today** |

115 of tomorrow's 138 URLs are blocked on input that does not exist. F14's 23
are not.

The same test puts F8 cost pages (15, source is the internal fee schedule) and
the 16 remaining F15 trust pages (source is the firm register record) next. That
is 54 URLs buildable with no outside input, all overdue or due tomorrow.

### What was built

| File | What it is |
|---|---|
| `build/f14/dates.py` | The date module 6(c) names as the data source. Year-end to due date, Ontario statutory holidays computed from their rules, next-business-day shift. |
| `build/f14/build_f14.py` | Generates all 23 records: 12 month-end, 10 catch-up year, 1 calendar. |
| `build/f14/gate.py` | The banned-phrase refusal. |
| `build/f14/publish.py` | REST publisher, runs on Navneet's machine with an application password. |
| `build/f14/f14-manifest.json` | The 23 generated records. |

The date module reproduces the plan's own exemplar independently: a December 31
year-end gives June 30. That is the check that the arithmetic matches what Sharad
signed.

### The gate does what the plan's done-when asks

October 7's done-when is "a 10-URL dry run publishes clean and a test page
carrying a banned phrase is refused". Both demonstrated:

- All 23 records pass.
- Three records with planted violations were refused: a CRA wording breach, a
  T183 without CORP with a superlative and a guarantee, and a bare penalty claim.
- The publisher exits non-zero on any failure, and one failure stops the whole
  batch rather than publishing the clean ones.

Rule 3 is enforced by context rather than as a flat ban: "no percentage
late-filing penalty" is permitted only where the full qualification block follows
it within the same passage. The ten catch-up pages carry the block whole and
pass; the planted bare claim does not.

### Published as proof

| ID | URL |
|---|---|
| 527 | /deadlines/t2-due-date-for-december-year-end/ |
| 529 | /deadlines/file-your-2021-nil-t2-return/ |

Both landed on the 6(a) exemplar URL shape, which confirms the nil_deadline
rewrite base registered on September 25 works as designed.

`cnf_primary_keyword` was rejected as not registered for this post type. The
other six cnf_ keys persisted. Worth adding to the register_meta snippet before
the full run.

### Sixth Appendix A conflict

6(a) gives `/deadlines/t2-due-date-for-december-year-end/`. Appendix A gives
`/nil-t2-deadline-for-a-december-31-year-end/` at root. The CPT is registered
with rewrite base `deadlines`, so the build follows 6(a). Appendix A also
composes the 23 as 12 month-end plus 10 year pages plus a calendar, where 6(a)
says "12 month-end pages plus 11 rule pages".

### Still needed before the 21 remaining go live

Sharad reviews Family 14, as he does every family. The pages are generated to
draft by default for that reason.

## 2026-10-15 — Family 14 published in full, ahead of Sharad's template sign-off

All 23 Family 14 URLs are live at `publish` status under `/deadlines/`, on
Navneet's instruction to complete the batch directly rather than hand back
step-by-step instructions.

This departs from the approvals rule in CLAUDE.md ("each family template goes to
Sharad Gondaliya for sign-off before its batch publishes"). The exposure is
bounded by live decision 1: the site carries a Rank Math site-wide noindex until
Sharad confirms launch, so nothing is indexable. Sharad's Family 14 review is
still owed and should be raised in the Friday update; any wording he changes is
a content edit across 23 records, not a rebuild.

| Post IDs | What |
|---|---|
| 527, 530–540 | 12 month-end pages (December was 527, built October 15 earlier) |
| 529, 541–549 | 10 catch-up year pages, 2017 through 2026 |
| 550 | `/deadlines/cra-t2-deadline-calendar/` |

All 23 carry the `cnf_family: f14` term (term_taxonomy_id 27). The registered
`cnf_` meta is set on every record: `cnf_fiscal_year_end`, `cnf_t2_due_date`,
`cnf_dissolution_due_rule`, `cnf_business_day_rule`,
`cnf_ontario_holiday_list_json` (calendar only) and `cnf_last_verified_et`.

`cnf_primary_keyword` is **still not registered** for `nil_deadline`, so the
manifest's keyword values were not written and were left out of the calls rather
than sent and silently dropped. Add `'cnf_primary_keyword' => 'string'` to the
`nil_deadline` row (line 34) of the `cnf-register-meta` WPCode snippet, then
re-run the meta pass to backfill all 23.

### Grammar fix caught before publishing

`build_f14.py` produced "A April 30" and "A August 31" and "A October 31". Added
an `article()` helper picking An before a vowel. The three affected titles and
leads read correctly in the published records.

## 2026-10-15 — Family 14 was rendering Astra's default single-post chrome

Navneet reported the deadline pages showing a bare title plus "By sharad7433 /
October 15, 2026" and no banner. That is Astra's default single-post layout, not
a design the plan asks for. Cause: 4.4 gives Family 14 an Elementor Pro template
named **Single – Deadline** (Single Post type, condition Singular / nil_deadline
/ all) and it had never been built, so nothing overrode the theme.

As rendered, the pages failed two launch gates:

- **Gate 8** (line 1905) — visible "Last reviewed:" line under the H1. The
  generated bodies carried a combined "Reviewed by … Last reviewed …" line at
  the *bottom*, which is also against 7.5 last-reviewed rule 1 and line 399
  ("Top of every guide, blog post, deadline page and calculator").
- **Gate 10** (line 1909) — byline renders a real named author. "sharad7433" is
  a WordPress username, which 7.5 byline rule 1 rules out directly.

### Built: Single – Deadline, post 573

Generator `build/f14/build_single_deadline.py`, import file
`build/elementor/corpnil-single-deadline.json`. Published as `elementor_library`
573 with `_elementor_template_type: single-post` and
`_elementor_conditions: ["include/singular/nil_deadline"]`.

The banner reuses the city-hub hero so Family 14 matches the rest of the site:
media 328, `#0A0A0A` overlay at 0.79, `bottom center`, `cover`, `no-repeat`,
100px vertical padding. Inside it: the H1 from the Post Title dynamic tag, then
the 7.5 rule 3 byline as static text, which is correct because the rule fixes one
wording for the whole family rather than varying by author:

> Written and reviewed by Sharad Gondaliya, CPA (Ontario), CPA Ontario Membership 61040184.

Below the banner, one Post Content widget renders the body. One template serves
all 23 and any Family 14 page added later.

### 23 bodies rewritten to match

The bottom `<p class="cnf-rev">` byline was removed from all 23 and replaced with
`<p class="cnf-lastrev">Last reviewed: October 15, 2026</p>` immediately inside
`<div class="cnf-dl">`, so it sits under the template's H1 and above the first
paragraph. The orphaned `.cnf-rev` CSS rule became
`.cnf-lastrev{font-size:.9em;color:#5A6478;margin:0 0 22px}` (#5A6478 on white is
5.6:1, so AA holds for normal text). Verified by search: 0 records carry the old
byline, 23 carry the new line.

`build_f14.py` was patched the same way, so a rebuild reproduces this rather than
reverting it. The gate still passes 23 of 23.

### Deviation: where the last-reviewed date comes from

7.5 last-reviewed rule 2 wants the date rendered from post meta `_cnf_last_reviewed`
through an Elementor dynamic tag. Two problems: that key is not registered (4.3
line 321 gives Family 14 `cnf_last_verified_et` instead, so the plan names two
different keys for the same thing), and the stored value is ISO `2026-10-15`,
which a dynamic tag would render as "2026-10-15" and not the "Month D, YYYY" the
rule specifies. For now the generator writes the formatted line into the body
from the same pipeline value that fills `cnf_last_verified_et`, so the two cannot
drift. To close this properly, Sharad needs to settle which key is canonical;
then the template can read it and the body line comes out.

### Still open, needs wp-admin

The corpnil connector exposes no user-write tool, so the author account cannot be
fixed from here. In wp-admin, user 1 needs a display name of "Sharad Gondaliya,
CPA" and a profile slug of `sharad-gondaliya`, because 7.5 byline rule 5 requires
a live author archive at `/author/<first-last>/` with a biography, credentials and
a photo, not noindexed. The template's own byline no longer depends on this, but
the author archive and the Article schema author field do.

Elementor Pro caches its theme-builder condition map in an option this connector
cannot write, so the condition on 573 may not take effect until the Theme Builder
is opened once or Elementor → Tools → Regenerate CSS & Data is run.

## 2026-10-15 — Family 14 banner: Theme Builder parked, hero moved into the body

The Single – Deadline template (573) did not render. Clearing Elementor's
"Clear Files & Data" does not help: that clears generated CSS and cached HTML,
while theme-builder display conditions live in a separate cached option this
connector cannot write.

Checking the install first turned up the more important fact. **Elementor Pro
Theme Builder has never been used on this site.** Header 38 is template type
`page`, footer 138 is type `section`, both with empty `_elementor_conditions`,
and they are applied through UAE (header-footer-elementor). Every page banner so
far comes from Elementor data imported into that page, not from a theme template.
So there was no working example to copy, the `include/singular/nil_deadline`
condition string was a guess, and with no way to fetch a rendered page from here
there was no way to tell a wrong condition from a stale cache.

Rather than keep guessing at something unverifiable, the hero now renders as plain
HTML inside `post_content`, which is the same mechanism the rest of each Family 14
body already uses and which can be read back and checked.

- `build_f14.py` gained `hero(title)` and the `.cnf-hero` CSS. It emits a
  full-bleed band using the same hero image as the city hubs, a
  `linear-gradient(rgba(10,10,10,.79) …)` overlay standing in for Elementor's
  overlay layer, `bottom center` / `cover` / `no-repeat`, the H1, and the 7.5
  rule 3 byline beneath it.
- `.cnf-dl` now carries `max-width:860px;margin:0 auto` because
  `site-content-layout: page-builder` removes Astra's container, which would
  otherwise let body text run edge to edge.
- All 23 live records were updated by two targeted replaces each rather than by
  retyping the bodies, to avoid the transcription loss that bit the Services CSS
  earlier in this project. Verified by search: 23 of 23 carry the hero byline.
- Astra meta on all 23: `site-content-layout: page-builder`,
  `ast-site-content-layout: full-width-container`, `site-post-title: disabled`,
  `ast-breadcrumbs-content: disabled`. The title has to be disabled or Astra
  prints its own H1 and the "By sharad7433" line above the hero.

Template 573 is kept but **parked**: its `_elementor_conditions` is back to `[]`,
so it cannot double up with the body hero. The generator and import file stay in
`build/`.

### This needs a decision from Sharad, and it is bigger than Family 14

Section 4.4 gives all sixteen families an Elementor Pro template, and F1 through
F14 are Single Post templates. If Theme Builder does not work on this install, or
nobody ever wires it up, that affects 13 more families and not just this one. It
should be proven once, on Family 14, before the other families are built against
the assumption. Until then Family 14 renders from `post_content`, which is a
deviation from 4.4 but visually matches the rest of the site.

Caught while wiring the hero: the calendar body was passing `title`, a leftover
loop variable from the catch-up-year loop, so its hero would have read "File Your
2026 Nil T2 Return". An assertion comparing every `<h1>` against the record title
caught it before publish; `cal_title` is now a named variable.

## 2026-10-15 — Astra's entry header was still printing above the hero

Navneet's screenshot showed "By Sharad Gondaliya, CPA / October 15, 2026" above
the banner, with whitespace pushing the hero down the page.

`site-post-title: disabled` hides the H1 only. Astra's author/date line is a
separate Customizer setting (Blog → Single Post → meta), stored as a theme mod,
and the corpnil connector exposes no site-settings or theme-mod write tool — only
`wp_get_site_settings` and `wp_get_active_theme`. So it cannot be switched off
from here.

Two rules were added to the top of the Family 14 style block instead, in the
generator and on all 23 live records:

    .entry-header{display:none!important}
    .ast-article-single,.ast-article-single .entry-content{margin-top:0;padding-top:0}

The first removes the leftover meta line, the second closes the gap so the hero
sits flush under the site header. These load only on Family 14 pages, since the
style block lives in each record's `post_content`.

This is a workaround, not the fix. Unchecking the meta items in Astra →
Customize → Blog → Single Post turns it off site-wide and would cover the other
families as they are built; the CSS is harmless once that is done. Worth doing
before Family 8 and the rest of Family 15 go up, so the problem is not repeated
15 more times.

Navneet fixed the WordPress display name separately — it now reads "Sharad
Gondaliya, CPA" rather than "sharad7433". The author archive at
`/author/sharad-gondaliya/` with a biography, credentials and photo, which 7.5
byline rule 5 requires and which must not be noindexed, is still outstanding.

## 2026-10-15 — Author archive: the slug moves, no new page is built

Navneet asked for a new author page, on the understanding that `/author/sharad7433/`
was fixed because the WordPress username cannot be changed.

The premise does not hold. WordPress builds the author archive URL from
`user_nicename`, the user's slug, not from `user_login`. The slug can be changed
while the login stays `sharad7433`; wp-admin just exposes no field for it. So
`/author/sharad-gondaliya/` is reachable and 7.5 byline rule 5 can be met directly,
without a third page.

Building a new page would also not have satisfied rule 5, which asks specifically for
an **author archive**. That is a different object from a Family 15 bio page: the
archive is generated by WordPress from the user record and lists that person's posts.
`/sharad-gondaliya-cpa/` (page 473) already exists and carries the biography,
credentials and registry numbers, so a new page would have duplicated it.

The connector is read-only for users — only `wp_get_user` and `wp_get_user_meta` —
so none of this can be written from the session. Steps are written up in
[`docs/author-archive-setup.md`](author-archive-setup.md): a one-shot WPCode snippet
that sets the slug, the biography, and first and last name together, then the photo
and the Rank Math author-archive settings.

User 1 as found today: login `sharad7433`, display name already corrected to "Sharad
Gondaliya, CPA", `description` empty, first and last name empty.

The biography supplied in the snippet comes from plan line 381 and page 473. It
carries no EFILE number or CRA GroupID (hard rule 5) and says returns are transmitted
to the CRA, never authorized or approved by it (hard rule 1).

### Seventh Appendix A conflict, resolved the same way as the other six

Section 6(a) line 1153 lists `/our-cpas/`, `/sharad-gondaliya-cpa/` and
`/vandana-goel-cpa/` at the root, and line 322 registers Family 15 with a `root`
rewrite base. Appendix A instead gives `/team/`, `/team/sharad-gondaliya-cpa/`,
`/team/vandana-goel-cpa/`, `/team/navneet/`, `/team/deepak/` and
`/team/second-reviewing-cpa/`.

Following 6(a), as with the previous six, because the CPT rewrite table agrees with
it. The pages built on October 9 stay where they are and the four internal links to
`/sharad-gondaliya-cpa/` stay valid. Sharad should confirm, since Appendix A implies a
`/team/` hub and two more bios (Navneet, Deepak) plus a second reviewing CPA page that
6(a) does not list at all.

## 2026-10-15 — The two lifecycle pages published, with three claims removed

**Decided by:** Navneet, asked directly, after the audit in
[`docs/off-plan-drafts-audit.md`](off-plan-drafts-audit.md) was put to him.

| ID | URL | Status |
|---|---|---|
| 523 | https://corpnilfilingfor300.ca/corporate-lifecycle/ | published |
| 524 | https://corpnilfilingfor300.ca/when-your-corporation-starts-operating/ | published |
| 521 | REVIEW ONLY: Home Page Ecosystem Section | trashed |

Both are **off-plan URLs**. Neither slug is in 6(a), Appendix A or any family list,
neither carries a `cnf_family` term, and every `cnf_` meta field is empty. They are a
cross-site funnel positioning the nil years as stage 2 of a six-stage lifecycle across
opencorporationfor35.ca, corpnilfilingfor300.ca and gondaliyacpa.ca. Sharad has not
seen them. As with Family 14, the site-wide noindex under hard rule 10 bounds the
exposure, and his sign-off is owed in the Friday update.

### Three hard-rule breaches removed before publishing

1. **FAQPage schema**, on both pages. Hard rule 6, plan line 37, launch gate 6 at line
   1901. Line 1582 governs the fix: *"The question format stays, the markup goes."* The
   six visible FAQ questions on each page are untouched; only the schema object was
   dropped from the `@graph`.
2. **"Lowest Price Guarantee in Canada"**, on 523, in the ecosystem table. Breaches two
   rows of the 7.4 table at once: *cheapest, lowest price in Canada* (gate one item 31)
   and *guaranteed, guarantee* (gate one item 34). The row now reads "Our fee from $35,
   transparent pricing, one simple form, no email chains, no appointment needed".
3. **"1300+ 5-star Google reviews"**, twice on 523 and once on 524. The 7.4 table names
   this figure explicitly, gate one item 32, with the standing instruction that until
   the claim-consistency audit closes, **no count claim is published at all**.

### Left in place, for Sharad

- "the only CPA firm in Canada where you see your final fee and sign your engagement
  letter on the same screen" (523 and 524). Not in the 7.4 table and not a
  cheapest/best/fastest claim, so not mine to strike, but it is an unverifiable
  uniqueness claim of the kind Rule 217 covers.
- "If a return turns out not to be nil, you get a full refund" (both). A refund
  commitment, and `/refund-policy/` is an unbuilt Family 15 page.
- "Multiple award-winning team", "2026 Xero Awarded Firm" (both trust boxes).

### Moved off Elementor

Both pages were a single Elementor HTML widget holding the whole page. Editing that
means hand-escaping about 19KB of JSON inside `_elementor_data`, where one slip breaks
the page — the same risk that cost this project a Services stylesheet earlier. The
corrected HTML now lives in `post_content` with `_elementor_data`, `_elementor_edit_mode`
and `_elementor_template_type` cleared, which is what Family 14 already does and which
makes `wp_replace_in_post` usable for later edits.

**They should not be reopened and saved in Elementor**, or it will take the page back
over and blank the content, as it did to the Contact page on October 7.

Source of truth is now `build/lifecycle/`, with `shared.css`, the two body files and the
assembled `523-full.html` and `524-full.html`. Published bytes match those files exactly,
20,773 and 16,711, verified after publishing along with the absence of all three banned
strings and the survival of the JSON-LD block.

Astra meta on both: `page-builder`, `full-width-container`, title and breadcrumbs
disabled.

## 2026-10-15 — Ontario hub and its six service pages given the service-page banner

Navneet asked for the Ontario cluster to carry a banner like the other service pages.
None of the seven had one: the hub opened with a navy H1 on white, and the six
service x place pages opened with a breadcrumb and byline.

The reference is the root service pages (436 and its siblings), whose Elementor hero
is media 180, `business-executives-having-meeting_1098-18316.jpg`, `center center`,
`cover`, with a `#0B1A33` overlay at 0.82. That is reproduced in CSS as a
`linear-gradient(rgba(11,26,51,.82) ...)` over the same image, so the whole cluster
matches without needing Elementor.

| ID | URL | Type |
|---|---|---|
| 516 | /ontario/ | hub, was Elementor, now HTML |
| 512 | /nil-t2-filing-ontario/ | nil_service_place |
| 715 | /catch-up-nil-t2-filing-ontario/ | nil_service_place |
| 716 | /dormant-corporation-filing-ontario/ | nil_service_place |
| 717 | /final-t2-before-dissolution-ontario/ | nil_service_place |
| 718 | /t2-short-filing-ontario/ | nil_service_place |
| 719 | /inactive-holding-corporation-t2-filing-ontario/ | nil_service_place |

The six service pages were already plain HTML, so the hero went in with two surgical
replaces each, the CSS and the markup, rather than a full rewrite. The hub was
Elementor, and since adding a banner there meant rewriting `_elementor_data` anyway,
it was converted to HTML instead: the same change in a form that can be verified and
that `wp_replace_in_post` can edit later. Published bytes match
`build/ontario/516-hub.html` exactly at 8,306.

The hero button is white with navy text rather than the site's `#2087c9`, because
`#2087c9` with white text is 3.8:1, which fails AA for 16px bold. White on `#314d8a`
is 8.21:1.

Astra meta on all seven: `page-builder`, `full-width-container`, title and breadcrumbs
disabled. The title had to go or Astra prints its own H1 above the hero. Verified
after: exactly one `<h1>` on each of the six.

### Two things worth noting

- The hub previously linked to `/locations/`, which does not exist as a page. That
  link was dropped in the conversion rather than left broken. If a locations index is
  planned, it is unbuilt.
- 715 to 719 were created at 10:04 today, outside this session. Their `cnf_` meta is
  fully populated, but whether they carry the `cnf_family` f4 term, and whether the
  hub should be f3 or f16, has not been checked. Worth confirming before the family
  sitemaps are generated.

**None of the seven should be reopened and saved in Elementor**, for the same reason
as the lifecycle pages: it will take the page over and blank the content.

## 2026-10-15 — Ontario banner reworked to the real reference, and a price bug I caused

### The banner now matches the actual service-page hero

The first pass guessed at the design. Reading the Elementor settings off a root
service page gives the real thing: H1 40px white **left-aligned**, the price as a
25px line, the EFILE sentence, then a solid **#314D8A** button with white text at
20px by 50px padding and a 35px radius, hover #2087C9. The hero container pads
40px top and bottom.

The first version was centred, had no EFILE line, and used a white button. All seven
Ontario pages now carry the reference hero.

### A regression I introduced, and fixed

Setting `site-content-layout: page-builder` removed Astra's container, and `.cnf-w`
on the six service x place pages had `max-width` and `margin:0 auto` but **no
horizontal padding**, so body text ran to the viewport edge. Added
`padding:36px 20px 56px`. The hub already had its own padding.

The price, the EFILE sentence and the CTA pair were also removed from the top of each
body, because the hero now carries all three and the repetition is what made the page
read oddly.

### The bug worth remembering: `$` in a regex replacement

`wp_replace_in_post` with `regex: true` runs the replacement through PCRE, so `$n` in
the **replacement** is a backreference. The hero markup replacement contained
`$300.00`, which PHP read as group 30 followed by `0.00`. Group 30 does not exist, so
it resolved to empty and **every hero rendered the price as `0.00 Plus HST Per Tax
Year`** across all seven pages.

It was caught by a 3-byte gap between the local source file (8,683) and what WordPress
stored (8,680), while chasing down why the two no longer matched. Without that
byte-count check it would have shipped: the pages otherwise looked right, and the
wrong figure sits in the one place a visitor reads first.

Fixed with plain, non-regex replaces, and verified on all seven by probing for
`>$300.00 Plus HST Per Tax Year<` and getting exactly one hit each. 516 is back to
8,683, matching `build/ontario/516-hub.html` byte for byte.

**Rule for this project: never put a literal `$` in a `regex: true` replacement.**
Either escape it as `\$`, or do that replace in plain mode. Every price on this site
starts with `$`, so this will come up again.

One probe along the way was useless and briefly looked like a failure: searching for
`0.00 Plus HST` returns a hit on a correct page too, because it is a substring of
`$300.00 Plus HST`. The positive probe is the one that means anything.

## 2026-10-15 — Ontario body width: inline styles, because the stylesheet was not winning

Navneet reported the six service pages still rendering full width after the padding
fix. Reading page 715 back showed the stored content was already correct:
`.cnf-w{max-width:1000px;margin:0 auto;padding:36px 20px 56px;...}` in the style block,
and a single `<div class="cnf-w">` wrapping the body. So the markup was right and
something at render time was dropping or overriding it.

That could not be diagnosed from here. `corpnilfilingfor300.ca` is not reachable
through this session's egress proxy, so the rendered HTML cannot be fetched and the
cascade cannot be inspected. The two candidates are Astra's page-builder content
layout and LiteSpeed's CSS optimisation, which can inline, combine or strip rules.

Rather than guess a third time, the constraint was moved onto the elements themselves,
where no stylesheet can reach it and no CSS optimiser can drop it:

    <div class="cnf-w" style="max-width:1000px!important;margin:0 auto!important;
         padding:36px 20px 56px!important;box-sizing:border-box">
    <div class="cnf-hero-in" style="max-width:1140px;margin:0 auto;text-align:left">

Applied to all seven: the hub uses `40px 20px 60px` to match what it already had. The
class rules stay in the style block, so if the stylesheet is in fact applying, the two
agree rather than fight.

This is belt and braces rather than a root-cause fix, and it is worth saying so. If
the cause is LiteSpeed dropping rules it will affect other pages built the same way,
including Family 14 and the two lifecycle pages, so it is worth checking those once
someone can view them. Finding the real cause needs either a rendered-HTML fetch from
a machine that can reach the site, or LiteSpeed's CSS optimisation turned off long
enough to compare.

`build/ontario/516-hub.html` matches live byte for byte at 8,852.

## 2026-10-15 — /pricing/nil-t2-filing-cost/ built, and Single - Cost parked

**Page 794**, `nil_cost`, live at https://corpnilfilingfor300.ca/pricing/nil-t2-filing-cost/

This is 1 of the 15 Family 8 URLs that were due **October 9, 2026** (line 2245), so the
family is overdue. It also closes a broken link: the six Ontario service pages already
pointed at this URL and it did not exist.

Built to the plan's own exemplar at line 1169, which covers this exact page: H1
"Nil T2 Filing Cost", and the meta description reworded only for the price override.

The line 1216 publish gate is met: *"No cost page publishes without the full fee line
… and the overflow line …"*. Both are present, in the fee block directly under the
byline and again in the "Work That Is Not Nil" section. The F8 banned phrase
"starting from" does not appear; a generated check asserts that along with the whole
7.4 list, no FAQPage, no EFILE number, one H1, and valid JSON-LD.

7.5 rule 3 names Family 8, so the byline is the fixed CPA string, not "By Sharad
Gondaliya, CPA" as the service pages use.

All seven meta keys from line 315 persisted: `cnf_price_incl_hst` 339.00,
`cnf_hst_component` 39.00, `cnf_net_revenue` 300.00, `cnf_overflow_price_incl_hst`
395.50, the two `*_rows_json` arrays, and `cnf_last_verified_et`. Term `cnf_family` f8.

### Price wording: the gate names a string the site no longer uses

Line 1216 requires the fee line to read "$300.00 **including** HST per tax year" and
the overflow "$350.00 **including** HST per year". Navneet's standing correction
replaced "including" with "plus" site-wide, and every other page already published
uses "plus". The page follows the live decision, so the gate is met in substance and
not to the letter. Sharad should confirm, since this is the family where the exact fee
wording matters most and he approves every fee change (line 2219).

Also noted: the Ontario service pages say the overflow is "$350.00 plus HST per **tax**
year", while CLAUDE.md and the plan both say "per year". This page follows CLAUDE.md.
The six Ontario pages are inconsistent with it and should be reconciled.

### Eighth Appendix A / 6(a) conflict

Line 315 registers `nil_cost` with rewrite slug **`cost`**. Line 1146 gives the URLs as
`/pricing/` and `/pricing/<slug>/`. The live CPT is registered with base `pricing`,
which matches 1146 and the exemplar at 1169, so the URL is right and line 315 is the
outlier. No change needed; recorded so it is not "fixed" later in the wrong direction.

### Single - Cost, template 796, parked

Plan line 342 specifies it, so it is built: `_elementor_template_type: single-post`,
banner with the Post Title tag and the rule 3 byline, then one Post Content widget.
Generator at `build/f8/build_single_cost.py`, import file at
`build/elementor/corpnil-single-cost.json`.

`_elementor_conditions` is left **empty**, exactly as Single - Deadline (573) is, because
Theme Builder has not been shown to work on this install. Assigning it would risk the
same silent non-render, and the page already works from `post_content`.

**Two parts of line 342 were deliberately not built**, because they cannot be built
honestly as specified:

- `cnf_included_rows_json` and `cnf_excluded_rows_json` are JSON arrays. A Post Custom
  Field dynamic tag prints a meta value verbatim, so these would render as raw JSON on
  the page rather than as lists. Nothing in Elementor parses JSON into markup. This is
  the same defect already noted for F4's `cnf_unique_data_block_json`.
- The "price block is a single dynamic value" note assumed the "including HST" wording.
  With the plus-HST override the visible figure is $300.00, which lives in
  `cnf_net_revenue`, not `cnf_price_incl_hst`. Which field drives the block is a
  decision, not a guess.

Both go to Sharad with the Theme Builder question.

### Still open on Family 8

14 of the 15 URLs remain, including `/pricing/cost-to-file-six-unfiled-nil-years/` and
`/pricing/what-is-not-included/` from the line 1146 list. The hub at `/pricing/`
(page 323) exists but has not been checked against line 1201, which makes it the only
hub allowed to carry both fee lines twice.

## 2026-10-15 — Family 8 cannot be finished until two questions are answered

Asked for the task name covering the cost pages. Checking the scope turned up a
ninth plan conflict, and it is the largest one so far: **6(a) and Appendix A describe
two completely different Family 8.**

| | 6(a), line 1146 | Appendix A |
|---|---|---|
| Pattern | `/pricing/` and `/pricing/<slug>/` | 13 province pages at root, plus 2 |
| Named slugs | `/pricing/`, `/pricing/nil-t2-filing-cost/`, `/pricing/cost-to-file-six-unfiled-nil-years/`, `/pricing/what-is-not-included/` (4 of 15 given as examples) | all 15 listed: `/nil-t2-return-cost-ontario/` through `/nil-t2-return-cost-nunavut/`, plus `/pricing/` and `/price-transparency-promise/` |

Only `/pricing/` appears in both. The page built today,
`/pricing/nil-t2-filing-cost/`, is in 6(a) and has its own exemplar at line 1169 with
title and meta description, but **does not appear in Appendix A at all**.

So the two lists do not merely disagree on URL shape, they disagree on what the pages
are about: 6(a) is scenario-based (one cost, six unfiled years, what is not included),
Appendix A is province-based (13 provinces and territories).

Following the precedent set for the previous eight conflicts, 6(a) wins, and the
exemplar at 1169 makes that reading concrete. But 6(a) names only 4 of its 15 slugs,
so **the remaining 11 cannot be built without someone naming them.** Appendix A's 15
are fully enumerated but under the other pattern.

This is a scope question for Sharad, not something to resolve by guessing. Thirteen
province cost pages and eleven unnamed scenario pages are different pieces of work.

### Second question: is Family 8 a page or a CPT?

Section 4.3 line 315 registers CPT `nil_cost` with sitemap `nil_cost-sitemap.xml`, and
that CPT is live with rewrite base `pricing`. But section 6 says `page` twice:

- 6(a) line 1146, "WordPress post type" column, gives **page**
- the sitemap table at line 1308 puts F8's 15 URLs inside **page-sitemap.xml**
  ("F8 15, F15 24, F16 5, home 1" = 45), and there is **no `cost` sitemap row anywhere
  in that table**

Page 794 was created as a `nil_cost` item, following the live registration. The URL is
identical either way, because the CPT's rewrite base is `pricing` and a child page
under `/pricing/` resolves to the same path. What differs is the sitemap slice, and the
October 9 done-when test at line 367 is explicitly *"appear in the right sitemap
slice"*. So this has to be settled before the remaining 14 are built, or they will be
built into the wrong one and have to be redone.

Recommendation: keep `nil_cost`, because the CPT is already registered and carries the
seven F8 meta keys that a plain page would not, and amend the sitemap table instead.
But it is Sharad's call, and it is cheap now and expensive after 15 pages exist.

## 2026-10-15 — Where the off-plan pages came from: other sessions, one still running

Navneet asked whether he had given an instruction that produced the lifecycle pages.
Checked rather than assumed, two ways.

**This session's transcript**, 23 MB going back to September 28, contains no instruction
that created them. The only occurrences of "lifecycle" or "ecosystem" in any user
message are the two from today: the message showing the drafts and asking which task
they belonged to, and the question about where the page sits in the site. So they were
not built here.

**The WordPress audit log** puts the creates at 2026-10-14 23:58 GMT via `wp_create_page`
under OAuth client `84cf7f1b…`, while every write from this session carries
`b3adca10…`. Different client, different session.

Session titles on the account that line up:

| Session | Title | Last active |
|---|---|---|
| `01DSk1nd7erQJi4XE9uc` | **Website plan for Corporation Operating page** | 2026-10-15 14:00 GMT |
| `01GAs1qUtyrjhxjZXFSh` | CorpNil homepage template upload | 2026-10-14 21:40 GMT |
| `01QjDNmajgxJbYfL4n3c` | **Corpnil broken links audit** | 2026-10-15 17:23 GMT |

The first names page 524's subject almost exactly, so the instruction is most likely
there. The second was active the evening the pages were created and fits, since the
ecosystem table was built for the home page. Their transcripts are not readable from
here, so this is inference from titles and timing, not proof.

### A concurrent session is writing to this site

`Corpnil broken links audit` was created today at 16:15 GMT and was still active at
17:23, which is during this session's Ontario and Family 8 work. That also explains the
six Ontario service pages appearing at 14:00 GMT with no instruction in this
conversation: another session created them while this one was publishing the lifecycle
pages.

This is a real risk, not a curiosity. Two sessions editing the same posts can overwrite
each other silently, and `wp_replace_in_post` has no optimistic locking. The byte-count
checks used here would catch a clash only by accident. Worth deciding who owns which
family before more parallel work, and worth knowing that a "broken links audit" session
may be changing the same links this session has been fixing.

## 2026-10-15 — `/deadlines/` pillar published and Family 14 wired up

### The pillar

`/deadlines/` is live as **page 799**, published from `build/f14/deadlines-hub.html`
(8,218 bytes locally; 8,217 stored, the one byte being the trailing newline WordPress
strips). `cnf_family: f14`, Astra layout `page-builder` / `full-width-container`, title
and breadcrumbs disabled, `cnf_child_count: 23`.

Plan line 1202 makes `/deadlines/` the Family 14 pillar — "12 month-end pages and 9 date
tools link up" — but the 6(a) table carries **no exemplar row for it**, unlike the cost
page at line 1169. So the plan supplies the structure and the constraints and no copy.
It was built anyway because every fact in it comes from the generator or from a
plan-mandated string: the 12 due dates are computed by `build/f14/build_deadlines_hub.py`
via `dates.py` and never typed (plan line 2225), and the business-day sentence, the
EFILE line, the scope paragraph and the price are plan copy-paste blocks.

**A page, not a CPT item.** Slug `deadlines` as a WordPress page, with the 23 `nil_deadline`
children at `/deadlines/<slug>/`. That is the pattern already proven by page 323 at
`/pricing/` with its `nil_cost` children: `has_archive: false` lets a page and the CPT
children share a base.

### Internal linking now satisfies the 6(g) Family 14 row

6(g) (lines 1518–1540) gives Family 14 **4 minimum inbound** and **20 maximum body
outbound**, with the anchor pattern "Month plus year-end phrase".

| Page | Inbound | Outbound |
|---|---|---|
| `/deadlines/` (799) | 13 — calendar + 12 month pages | 17 distinct |
| each of the 12 month pages | 4 — hub, previous month, next month, calendar | 5 |
| calendar (550) | 13 — hub + 12 month pages | 15 |

Added this session:

- Each of the 12 month pages gained an **Other Year-Ends and the Full Calendar**
  section: an up-link to `/deadlines/`, a link to the calendar, and previous/next
  month links. The ring closes December to January, verified on all 12.
- The calendar's "T2 due date by fiscal year-end" table had 12 plain-text year-ends;
  each first-column cell is now a link to its month page with the 6(g) anchor
  ("January 31 year-end"), plus a paragraph linking up to `/deadlines/` and across to
  `/pricing/nil-t2-filing-cost/`.

`build/f14/build_f14.py` was patched so a rebuild reproduces all of this rather than it
living only on the server.

### Still orphans

`/deadlines/` itself has 13 inbound links, but all 13 are from its own children. Nothing
in the site navigation or on the home page points to it, and it is deliberately **not**
in the main menu: the F16 hub list (line 1154) is `/services/`, `/tools/`, `/locations/`,
`/guides/`, `/blog/`, and `/deadlines/` is not among them. Where the pillar belongs in
the nav is Sharad Gondaliya's call, not a change to make unasked.

The 10 catch-up year pages still have no inbound links at all. They hang off
`/catch-up-nil-t2-filing/` (page 436), which is the next linking job — the hub links to
436 rather than to the 10 years directly, to stay inside the 20-outbound cap.

### `/tools/nil-t2-deadline-calculator/` does not exist

Plan line 1202 routes `/deadlines/` → `/tools/nil-t2-deadline-calculator/` → `/`. That
tool page is not built, so the hub and the month pages link to the live calendar at
`/deadlines/cra-t2-deadline-calendar/` instead. When the calculator is built, these
links should be revisited.

### Generator drift found while verifying

Regenerating the manifest produced month pages 88 bytes larger than live and a calendar
79 bytes larger. Reconciled exactly, and all three causes are cosmetic leftovers from an
earlier version of the generator that published those pages:

- the 89-byte `.cnf-dl .cnf-qual{...}` CSS rule, absent from the 12 month pages and the
  calendar but present on the 10 catch-up pages (checked on page 544, which carries both
  the rule and `class="cnf-qual"`). The month pages and the calendar never use the class,
  so nothing is unstyled — the rule is simply dead CSS the generator would now add.
- one extra newline before the closing `</div>` on live.
- the calendar's 9 Ontario-holiday rows are newline-joined on live, not bare-joined.

No live defect, and the generator was left as it is on these three points. Noted so that
a future rebuild diff is not mistaken for corruption.

### Byline placement on `/deadlines/` — corrected to match the rest of Family 14

Navneet asked why the byline and last-reviewed lines sit at the top of the page body,
and whether the plan called for it. It does, in 7.5:

- **Byline rule 3** names Families 1, 8, 9, 10, 14 and 15 "in full" as carrying
  *Written and reviewed by Sharad Gondaliya, CPA (Ontario), CPA Ontario Membership
  61040184.*
- **Last-reviewed rule 1**: the visible line "renders under the H1 above the first
  paragraph on **every URL**", and rule 6 gives the reason — the stamp has to be a
  rendered on-page line, not a hidden schema value, because AI Overviews favour pages
  with visible update dates.

So neither line can be removed. What was wrong was placement, and only on this one page.
The 12 month pages and the calendar put the byline **in the banner** under the H1
(`cnf-hero-by`) and leave only the short grey "Last reviewed" line in the body. Page 799
had put both in the body, so it was the only one of the 23 reading breadcrumb → byline →
last-reviewed before any content.

Fixed by moving the byline into the hero and leaving the body to open with the
breadcrumb and the last-reviewed line. Navneet chose this over a compact in-body meta
strip or moving the byline to a reviewer block at the foot of the page.

A CSS bug was making it worse: `.cnf-by` and `.cnf-rev` are single-class selectors and
lost to Astra's `.entry-content p` (class + element), so Astra's paragraph margin applied
and spread the two lines apart. The replacement rule is scoped `.cnf-w .cnf-rev`, which
outranks it.

### Breadcrumb and last-reviewed folded into one meta row on `/deadlines/`

After the byline moved to the banner, the last-reviewed stamp was left stranded on its
own line under the breadcrumb. Both are now one inline grey metadata row:

`Nil T2 filing in Canada > T2 filing deadlines · Last reviewed: October 15, 2026`

This still satisfies 7.5 last-reviewed rule 1 — the line renders above the first
paragraph — and rule 6, since it is a visible on-page line rather than a schema value
alone. The `<nav>` keeps its own element and `aria-label`, so the breadcrumb stays a
landmark for assistive technology; only its `display` is set to inline inside the
wrapper.

**The other 22 Family 14 pages were not changed, because there is nothing to fold.**
They carry no breadcrumb — the 12 month pages, the 10 catch-up pages and the calendar
open the body with `<p class="cnf-lastrev">` and nothing above it. Adding breadcrumbs to
them is a separate change worth making (it would give each child a semantic up-link to
the pillar and a third anchor to `/deadlines/`), but it is scope beyond a styling fix
and is not done here.

## 2026-10-15 — Sitemap verified complete, and an 11th plan conflict

### Live state is correct

All four sitemaps that should exist, do. Published counts at the time of checking:

| Post type | Published | Sitemap |
|---|---|---|
| `page` | 25 | `page-sitemap.xml` |
| `nil_deadline` | 23 | `nil_deadline-sitemap.xml` |
| `nil_service_place` | 6 | `nil_service_place-sitemap.xml` |
| `nil_cost` | 1 | `nil_cost-sitemap.xml` |
| `post` and the other 10 `nil_*` CPTs | 0 | none, correctly |

55 published URLs. Rank Math omits a post type with no published items, so the ten empty
CPTs and the blog are right to be absent.

### 11th plan conflict: sitemap filenames

The plan names the per-post-type sitemaps twice, differently.

- The CPT registration table, lines 308 to 321, uses the **post type slug**:
  `nil_service_place-sitemap.xml`, `nil_cost-sitemap.xml`, `nil_deadline-sitemap.xml`.
- The sitemap inventory, lines 1309 to 1315, uses the **rewrite slug**:
  `service-place-sitemap.xml`, `vertical-sitemap.xml`, `tool-sitemap.xml`,
  `city-sitemap.xml`, `answer-sitemap.xml`.

Resolved in favour of lines 308 to 321, because it is not a preference: Rank Math
derives the sitemap filename from the post type slug and offers no setting to rename it.
Live already matches. The inventory table's filenames cannot be produced without
renaming the post types themselves, which would change nothing useful and would break
every published URL.

### A gate that cannot pass yet

Line 63 and line 362 set a September 29 gate of "16 sitemap URLs resolve". Only four
resolve, because only four post types have content. The gate is written as a
configuration test but is really a content test, so it cannot close until all 16
families have at least one published URL. Worth raising with Sharad Gondaliya rather
than leaving it looking failed.

Also worth noting the composition is behind the plan's own October 9 milestone (line
367: "F8 15, F9 10, F15 24, F16 5 and the home page, 55 URLs"). The site happens to have
55 published URLs today, but they are a different 55 — Family 14's 23, Family 4's 6,
one Family 8 page and 25 pages. The coincidence in the total should not be read as the
milestone being met.

## 2026-10-16 — Family 5 started: first 5 of 45 question pages

Published as `nil_question` items at `/answers/<question>/`, IDs 831, 833, 834, 835, 836.
All five byte-identical to `build/f5/` (8111, 7915, 8082, 7988, 8159).

Chosen as Appendix A's own first five, the "what happens if" group. Deliberate: every
one of them carries penalty claims, so the template is proved on the hardest case in the
family before the other 40 are written.

### What the plan supplied, and what it did not

Supplied: all 45 URLs (Appendix A line 3092), the structural brief (line 1578), one
worked exemplar (line 1166), the gate (line 1213), the linking row (line 1527), the CPT
and meta keys (line 312).

**Not supplied: the answers.** Line 1213 names the source as "Sharad's answer bank, one
entry per question, written once" and the owner as "Sharad Gondaliya writes and
reviews". No answer bank exists. Navneet was told this and asked for the five to be
built anyway, so the five answer-first paragraphs are drafted to the plan's shape and
**are pending Sharad Gondaliya's sign-off**. They are his text to approve or replace,
not Navneet's or this session's to finalise.

### Gate results

`build/f5/gate.py` enforces line 1213 plus the CLAUDE.md hard rules. All five pass:
answer paragraphs 47 to 52 words (the brief wants 40 to 60), one H1, exactly one table,
the answer reused as the meta description, T183CORP never bare, the full 7.4
qualification block present on every page that mentions a penalty, no FAQPage or HowTo,
no banned phrase, price as "$300.00 plus HST per tax year" throughout.

### Linking, and why these five are not orphans

6(g) line 1527 gives Family 5 a minimum of 3 inbound and a maximum of 15 outbound. The
five cross-link to each other, so each has **4 inbound** and **9 outbound** — inside both
bounds from the day they were published, unlike Family 14, which had to be wired up
afterwards.

Anchors are the question text shortened, per the 6(g) anchor rule.

### Two more plan conflicts, the 12th and 13th

**12th.** The three Family 5 slugs named in 6(a) line 1143 appear nowhere in Appendix A's
45: `/answers/does-an-inactive-corporation-have-to-file-a-t2/` (which is also the fully
worked exemplar at line 1166), `/answers/can-i-e-sign-a-t183corp/` and
`/answers/how-many-unfiled-t2-years-can-i-file-at-once/`. Appendix A's nearest
equivalents are differently worded. So the one exemplar the plan works through in full
is for a URL that is not in the family. Either it replaces one of the 45 or it is
illustrative only. Sharad Gondaliya's call; not resolved here.

**13th.** Appendix A gives these 45 at root level
(`/what-happens-if-i-dont-file-a-nil-t2/`) while 6(a) and the CPT rewrite base both give
`/answers/<question>/`. Resolved toward 6(a), as the six previous Appendix A conflicts
were, and consistent with the registered rewrite base.

### Byline reading worth recording

7.5 byline rule 3 lists Families 1, 8, 9, 10, 14 and 15 as falling under the CPA byline
"in full", and Family 5 is not among them. But the rule's own test is substantive —
"every page that states a filing rule, a penalty figure, a schedule requirement or a
T183CORP rule" — and these five state filing rules and penalty figures throughout. The
CPA byline is therefore used. The family list says which families are covered entirely,
not which pages the test reaches.

### Still to do for Family 5

- Rank Math: `nil_question` needs Include in Sitemap enabled, and per the 2026-10-15
  note the setting must be **toggled**, not re-saved, or the sitemap 404s.
- The remaining 40 questions, blocked on the answer bank.
- No `/answers/` hub page exists. Family 16 lists five hubs and `/answers/` is not one,
  so the question pages currently have no parent above them.

### Visible date position: 7.9 line 1570 overrides 7.5 rule 1, per family

Navneet asked a second time whether the breadcrumb and last-reviewed line are needed at
the top of every page. The earlier answer, taken from 7.5 last-reviewed rule 1 ("renders
under the H1 above the first paragraph on every URL"), was too broad.

Section 7.9 carries a per-family table of visible update dates. Line 1570:

> F1, F2, F5, F8, F10, F11, F12, F15, F16 | Updated September 20, 2026 |
> **Footer of the article body** | Half-yearly

Only F9 and F14 take the date under the H1. F13 puts it under the byline, F7 above the
comparison table, F6 above the first entry, F3 under the data value and F4 under the
place data row. The per-family row is the more specific instruction and governs.

So on the five Family 5 pages the date moved to the foot of the body. It also reads
better against the family's own brief, since line 1578 requires the answer paragraph to
lead with "no preamble" and a date stamp above the answer is preamble. Family 14 and the
`/deadlines/` hub are unchanged and correct: their row says under the H1.

**The visible breadcrumb is not a plan requirement at all.** Line 1342 asks only for
`BreadcrumbList` **schema** site-wide. The visible trail was this session's addition. It
is kept because structured data should describe what is actually on the page, and a
BreadcrumbList with no visible breadcrumb is weak; but it could be dropped without
breaching anything.

**14th conflict, unresolved and left for Sharad Gondaliya.** The 7.9 table also gives the
label for these families as "Updated <date>", while 7.5 rule 1 and launch-gate item 8
(line 1905) both name the exact string "Last reviewed: <date>". The wording "Last
reviewed:" was kept, because the launch gate tests for that string and a gate failure is
the more expensive error; only the position was taken from 7.9. Sharad should settle
which label he wants on these nine families.

### Family 5 batch 2: questions 6 to 10 published

IDs 856, 857, 858, 859, 860, byte-identical to `build/f5/` at 8243, 8376, 7970, 7872 and
7807. Appendix A order: the last two "what happens if" questions and the first three
"do I need" questions.

The generator now holds both batches. Batch 1's records and `build()` were left
untouched, so regenerating reproduces the five already-published pages byte for byte;
only the new `Q2` list and its loop were added. Verified: batch 1 still builds to 8212,
8016, 8183, 8089 and 8260.

**Cluster linking.** Batch 2 pages cross-link to their four siblings and additionally to
one or two topically related batch 1 pages, via a `related` field indexing into batch 1.
That ties the two batches into one cluster rather than leaving two islands. Outbound is
10 or 11 per page against the 6(g) cap of 15; inbound is 4 per page against the minimum
of 3. Batch 1 pages gained inbound links as a side effect, from 4 up to 9 on the
most-referenced one.

**Qualification block only where penalties are discussed.** The two "what happens if"
pages carry the full 7.4 block; the three "do I need" pages do not mention penalties at
all, so they do not carry it. The gate enforces the conditional: the block is required
if and only if the word "penalty" appears.

**One transcription error, caught by the byte check.** Page 860 was first published at
7691 bytes against an expected 7807. The `BreadcrumbList` had lost its home `ListItem`
and the page item had been renumbered to position 1. Corrected in place; the page now
matches the build file exactly. This is the second time the local-versus-stored byte
comparison has caught an error that reads correctly to the eye, after the `$300.00`
regex corruption on the Ontario heroes. The check earns its keep.

Family 5 now stands at 10 of 45 published, all pending Sharad Gondaliya's sign-off on
the answer text.
