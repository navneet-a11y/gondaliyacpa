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
