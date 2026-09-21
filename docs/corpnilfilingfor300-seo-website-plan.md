# corpnilfilingfor300.ca — SEO and Website Development Plan

Source: `CorpNilFilingfor300-SEO-Website-Plan-Navneet.docx`, prepared for Navneet by Sharad Gondaliya, CPA, Gondaliya CPA Professional Corporation, September 21, 2026. Converted to Markdown verbatim; tables and the full Appendix A URL list are preserved.

---


Prepared for Navneet by Sharad Gondaliya, CPA, Director, Gondaliya CPA Professional Corporation. September 21, 2026.

# Scope

This document covers SEO and website development for corpnilfilingfor300.ca, including the blog and Blog2Social distribution. Navneet is responsible for everything in it, end to end. The project is complete on Friday, November 20, 2026.

| Item | What is included |
|---|---|
| Website development | Hosting, DNS, SSL, WAF, CDN, WordPress and plugins, Custom Post Type UI, Elementor templates, the Python publishing pipeline, the WordPress MCP connector, accessibility and backups |
| Structural pages | 968 URLs across 16 page families, mirroring the gondaliyacpa.ca sitemap. Appendix A lists every URL. |
| SEO | Keyword mapping, titles and meta descriptions, Rank Math schema and sitemaps, Link Whisper internal linking, indexation, AEO and link earning |
| Blog | 10 posts every Friday from October 16, 2026. 60 posts live by November 20, 2026, then weekly after that. |
| Blog2Social | Every blog post scheduled through Blog2Social under the rules in Section 7.7 |
| Filing form | Built by Deepak. Navneet embeds it in the checkout block on every template by October 23, 2026. |
| gondaliyacpa.ca | Page wording updates sent by Sharad Gondaliya on October 6, 2026, deployed by October 9, 2026 |

Not in this document: the filing form build, legal page text (privacy, terms, refund and engagement terms, which Sharad Gondaliya supplies and Navneet publishes as supplied), and all business, compliance and operations planning.

Section numbers match the full roadmap, so cross-references between sections still work.

## Page copy and schema rules

| # | Rule |
|---|---|
| 1 | About CRA, use only the wording "registered EFILE electronic filer". Never use authorized, agent, approved, partner or endorsed about CRA. No CRA logos. |
| 2 | Always write T183CORP, never T183. |
| 3 | Never write "no penalty" on its own. Always add the full wording in Section 7.4. |
| 4 | Never say we are the cheapest or the best. Competitor pages show only the published price and the date it was captured. |
| 5 | The EFILE number and the CRA GroupID never appear on any page, schema, sitemap, image or social post. |
| 6 | No review or aggregateRating schema, no FAQPage and no HowTo. Trustindex rich snippets stay off. |
| 7 | No booking widget, no Calendly and no "book a call" anywhere. The /consultation/ page only explains the hand-off to gondaliyacpa.ca at $350 including HST per year. |
| 8 | Holding, rental and investment pages always state that such a corporation is not nil. Quebec pages state that CO-17 is a separate return, and Alberta pages say the same for AT1. |
| 9 | Every price reads $300 including HST per tax year. |
| 10 | Staging stays noindexed. Live stays noindexed until Sharad Gondaliya confirms launch. Build to the dates regardless. |

## Approval and weekly update

Before a batch publishes, send Sharad Gondaliya each family template, and each blog batch on Thursday, for sign-off. Blog posts go live every Friday by 8:30 PM, with Blog2Social scheduled the same day. Any change to trust-strip wording, every competitor page, and any tool not already in the stack needs approval before it goes live.

| # | Weekly update, every Friday by 5:00 PM from September 25, 2026 |
|---|---|
| 1 | Each dated deliverable, marked done or not done |
| 2 | Structural URLs live against the plan |
| 3 | Blog posts published and Blog2Social posts scheduled |
| 4 | Any date that will move, with its new date |

# Dated build schedule, September 21 to November 20, 2026

968 structural URLs are the 1,422 family URLs less the 455 blog posts, plus the home page. The blog runs at 10 posts every Friday from October 16, 2026, reaching 60 posts by November 20, 2026 and continuing weekly after that.

| Date | Deliverable | Done when |
|---|---|---|
| Tuesday, September 22, 2026 | Hosting, DNS, SSL, WAF and CDN live, staging clone noindexed | SSL grade A, staging resolves and is noindexed |
| Wednesday, September 23, 2026 | WordPress stack installed and licensed on live and staging | All plugins active, no licence warning, auto-update off |
| Friday, September 25, 2026 | 14 custom post types, 8 taxonomies, 28 place terms and 12 service terms set up; post meta registered in WPCode Lite | A test item in every post type returns 200 at its URL and its meta is visible |
| Tuesday, September 29, 2026 | Rank Math sitemap slices, robots.txt, canonical rules, and a schema check that blocks the EFILE number and the CRA GroupID | 16 sitemap URLs resolve and a test block carrying an EFILE-format number is rejected |
| Friday, October 2, 2026 | Elementor global kit, global header and footer with the firm block; UpdraftPlus schedule with a full restore rehearsed | Footer shows on every template and staging restores intact |
| Wednesday, October 7, 2026 | Python publishing pipeline and WordPress MCP connector publishing with meta, terms, Rank Math title and description; banned-phrase sweep blocks a publish | A 10-URL dry run publishes clean and a test page carrying a banned phrase is refused |
| Friday, October 9, 2026 | 16 family templates and 4 global templates built and assigned; first 55 URLs live (pricing 15, guides 10, trust and legal 24, hubs 5, home 1); gondaliyacpa.ca wording updates deployed | Every dynamic field fills, 55 URLs return 200, every updated gondaliyacpa.ca page shows the new wording |
| Friday, October 16, 2026 | 138 URLs: questions 45, comparisons 20, deadlines 23, calculators 50; first 10 blog posts | 193 structural URLs live |
| Friday, October 23, 2026 | 150 URLs: calculators 50, first-filing 25, city hubs 15, verticals 60; filing form embedded in the checkout block on every template; 10 blog posts | 343 structural URLs live and a test purchase and T183CORP signature complete from a live page |
| Friday, October 30, 2026 | 188 URLs: calculators 50, guides 20, listicles 38, verticals 80; 10 blog posts | 531 structural URLs live |
| Friday, November 6, 2026 | 236 URLs: verticals 75, service-by-place 150, reviews 11; 10 blog posts | 767 structural URLs live |
| Friday, November 13, 2026 | 201 URLs: service-by-place 186, case studies 15; 10 blog posts | 968 structural URLs live, all 16 families complete |
| Wednesday, November 18, 2026 | Full QA across every URL: WCAG 2.1 AA and AODA, schema validation, broken-link crawl, banned-phrase and EFILE-number sweep, unique-data check | Zero errors on every check |
| Friday, November 20, 2026 | Project complete: 968 structural URLs and 60 blog posts live, form embedded, sitemaps ready; blog continues at 10 posts every Friday | Written sign-off from Sharad Gondaliya |

# Section 2. Checkout page copy and mobile layout

The form fields inside this page are built by Deepak. Navneet builds the page, its copy and its layout around the form.

## 2.8 One-screen page copy, headline to button

Headline

Nil T2 filing, $300.00 including HST per tax year.

Subhead

Type your corporation name. We fill in your CRA Business Number and your incorporation date. Pick the years you have not filed, confirm there was no activity, and pay. We then prepare the return, generate Form T183CORP carrying that return's figures, you sign it on screen, a CPA reviews it, we transmit it, and your CRA confirmation arrives within 3 business days.

Line under the subhead

No meeting. No booking link. No email chain. One screen, start to finish.

Step strip, in order, never reordered

1.	Type your corporation name.

2.	We fill in your CRA Business Number and incorporation date.

3.	Pick the tax years you have not filed.

4.	Confirm the corporation had no activity.

5.	Attest that you are an authorized signing officer and pass the identity check.

6.	Pay by credit card, debit, Apple Pay or Google Pay.

7.	We prepare the return, generate your Form T183CORP, and send you a single-use signing link.

8.	You sign on a secure access-controlled screen.

9.	A CPA reviews it and files it electronically.

10.	Your CRA confirmation arrives by email within 3 business days.

Field block on the screen

Corporation legal name

Incorporated under

Registry number

CRA Business Number and RC0001

Incorporation date

Registered office postal code

Fiscal year end, month and day

Select the tax years you have not filed

Total including HST

The corporation had no business activity in every year selected.

Signing officer first name

Signing officer last name

Signing officer title

I am an authorized signing officer of this corporation and I can sign Form T183CORP for it.

I am completing this form myself. Nobody is completing it on my behalf.

Signing officer email

Six-digit code emailed to you

Signing officer mobile number

Six-digit code texted to you

Upload government photo identification

The name on the identification matches the signing officer name above.

I accept the engagement terms and the privacy notice.

I consent to the storage described in the privacy notice.

Why you have to file

Every resident corporation, including an inactive one, must file a T2 within six months of its fiscal year-end, every year, until it is formally dissolved. A final T2 is due within six months of dissolution.

Why you have to file electronically

For tax years starting after 2023 e-filing is mandatory for virtually all corporations. A paper T2 draws a $1,000 penalty plus a $100 per-return preparer penalty. We file electronically only.

What a late nil year actually costs you

A true nil return has no percentage late-filing penalty because that penalty is a percentage of tax owing and the corporation owes $0.00, but an unfiled year stays open forever, invites a demand to file and an arbitrary assessment, blocks a clearance certificate and dissolution, and costs a non-resident corporation $25 per day up to $2,500.

What your fee covers, exact scope-of-fee sentence

The fee of $300.00 including HST per tax year covers one nil T2 return for one corporation for one tax year, including the T2 Short where the corporation qualifies, GIFI Schedules 100, 125 and 141 where they are required, Schedule 24 on a first return, Schedule 50 for every shareholder at 10% or more, Schedule 8, loss continuity, your Form T183CORP package, single-use secure e-signing, CPA review, electronic transmission to CRA by a registered EFILE electronic filer, one corrected transmission if CRA rejects the first one, and your CRA confirmation emailed within 3 business days.

What your fee does not cover, exact exclusions sentence

The fee of $300.00 including HST per tax year does not cover the Ontario annual return, the federal $12 annual return, the Alberta AT1, the Quebec CO-17, GST/HST nil returns, payroll nil returns, or RC145 closure of a GST/HST or payroll account.

When this is not a nil return

Investment income, rental income, taxable dividends paid, taxable dividends received, a corporation that is not a Canadian-controlled private corporation, more than one permanent establishment, a reporting currency that is not the Canadian dollar, a refundable credit, an Ontario transitional debit, a section 34.2 amount, an amalgamation, a year-end change needing CRA approval, or a corporation already dissolved or struck. Answer the questions on this screen honestly and we route you to our sister office at gondaliyacpa.ca at $350.00 including HST per tax year before you pay. If we find it after you pay, we refund you in full.

Your Form T183CORP

Form T183CORP carries the figures on your own return. You sign it before we transmit, on a single-use access-controlled screen, with the date and the hour, minute and second recorded on our server in Eastern Time. It is never backdated. We keep it for six years. We do not send it to CRA unless CRA asks for it.

Who files it

Gondaliya CPA Professional Corporation, CPA Ontario Firm Registration 61330051. Your return is reviewed by Sharad Gondaliya, CPA, a registered EFILE electronic filer, and is prepared and transmitted in Canada.

Button text

Pay $300.00 including HST and start

Button text with more than one year selected

Pay $900.00 including HST for 3 tax years and start

Line under the button

Credit card, debit, Apple Pay and Google Pay. You pay once, on this screen, and nothing else is owed.

Footer line

Gondaliya CPA Professional Corporation. 55 Queen St E, Suite 1205, Toronto, ON M5C 1R6. 647-212-9559. info@gondaliyacpa.ca. Open 9:00 AM to 8:30 PM, Monday to Sunday. corpnilfilingfor300.ca is a department of Gondaliya CPA Professional Corporation.

## 2.9 Mobile element order, top to bottom

1.	Headline: Nil T2 filing, $300.00 including HST per tax year.

2.	Subhead.

3.	Line: No meeting. No booking link. No email chain. One screen, start to finish.

4.	Corporation legal name field, with the keyboard opening on load.

5.	Incorporated under, select.

6.	Lookup result card showing registry number, CRA Business Number, incorporation date and registry status.

7.	Registered office postal code field.

8.	Fiscal year end field and the year-end confirmation checkbox.

9.	Tax year checkbox list, newest year first.

10.	Sticky total bar showing Total including HST.

11.	No-activity confirmation checkbox.

12.	No-revenue confirmation checkbox.

13.	Eligibility questions, one Yes or No per row, in the order of screen positions 18 to 33.

14.	Books-and-records questions that set the GIFI, Schedule 24, Schedule 50 and Schedule 8 outcomes.

15.	Account questions on GST/HST, payroll, dissolution, amalgamation, year-end change, non-residency and foreign property.

16.	Signing officer name, title, email and mobile fields.

17.	Email one-time code field.

18.	Text-message one-time code field.

19.	Government photo identification upload and the name-match checkbox.

20.	Authorized signing officer attestation checkbox.

21.	Direct-dealing attestation checkbox.

22.	Engagement terms and privacy notice checkbox.

23.	Storage consent checkbox.

24.	Scope-of-fee sentence.

25.	Exclusions sentence.

26.	Late-nil-year cost paragraph with the $25 per day up to $2,500 qualification.

27.	Stripe payment element, cards, debit, Apple Pay and Google Pay.

28.	Sticky button: Pay $300.00 including HST and start.

29.	Line under the button on payment methods.

30.	Ten-step strip, collapsed, tappable to open.

31.	Why you have to file, collapsed.

32.	Why you have to file electronically, collapsed.

33.	When this is not a nil return, collapsed, with the gondaliyacpa.ca link at $350.00 including HST per tax year.

34.	Your Form T183CORP, collapsed.

35.	Who files it: firm name, CPA Ontario Firm Registration 61330051, registered EFILE electronic filer line.

36.	Footer with address, phone, email and hours.

# Section 4. Technical architecture and build plan

## 4.1 Layer table

| Layer | Owned tool | Configuration | Owner | Build days | Notes |
|---|---|---|---|---|---|
| Hosting | Managed LiteSpeed WordPress account | PHP 8.3, 8 GB RAM, LiteSpeed Enterprise, object cache on, Toronto region, staging clone at staging.corpnilfilingfor300.ca | Navneet | 2 | Cost estimate inside the $400.00 per month hosting and lookup database line |
| DNS | Registrar DNS plus QUIC.cloud | A record to origin, CNAME on www, CAA record, SPF, DKIM, DMARC p=quarantine, TTL 300 seconds during cutover | Navneet | 1 | Included with the domain registration, no vendor added beyond Stripe |
| SSL | Let's Encrypt at host plus QUIC.cloud edge certificate | TLS 1.3 only, HSTS max-age 31536000 with includeSubDomains and preload, 60-day auto renewal, HTTP to HTTPS 301 | Navneet | 1 | Included with hosting |
| WAF | QUIC.cloud WAF plus LiteSpeed rules | OWASP core rule set on, /wp-admin/ restricted to Canadian IP ranges, rate limit 20 requests per minute on /lookup/, /pay/ and /sign/, bot challenge on /sign/ | Navneet | 2 | estimate |
| CDN | QUIC.cloud CDN through LiteSpeed Cache | Edge full-page cache, bypass on /lookup/, /pay/ and /sign/, Imagify WebP, Brotli, 30-day static TTL, purge-on-publish call from the Python pipeline | Navneet | 2 | estimate |
| UpdraftPlus backups | UpdraftPlus | Files daily 03:00 Eastern, database every 4 hours, 30 copies retained, remote target Microsoft 365, monthly restore rehearsal to staging | Navneet | 1 | estimate |
| Python publishing pipeline | Python plus WordPress REST | Renders 1,423 URLs from templates, writes post meta and taxonomy terms, sets Rank Math title and description, runs the schema validator, purges CDN, logs every publish | Navneet | 6 | Built in-house, labour sits in the website and SEO budget |
| WordPress MCP connector | WordPress MCP connector | Application password on a dedicated publisher account, capabilities limited to edit_posts and upload_files, IP allow-list, request log retained 12 months | Navneet | 2 | Bulk publishing path for the pipeline |
| WCAG 2.1 AA and AODA conformance | Astra Pro plus Elementor Pro | Contrast 4.5 to 1 minimum, visible focus ring, skip link, labelled fields, error text not colour-only, full keyboard path through lookup, pay and sign, alt text written by the pipeline, accessibility statement page published | Navneet | 4 | Audit and remediation labour sits in the website and SEO budget |
| WordPress theme and plugin stack | Astra Pro, Elementor Pro, Rank Math PRO, Link Whisper, Imagify, Trustindex, Easy Table of Contents, Popup Maker, Custom Post Type UI, WPCode Lite, Site Kit by Google, Blog2Social | Licences activated on the live domain and the staging clone, auto-update off, update window Tuesday 06:00 Eastern after a staging test | Navneet | 3 | estimate |

## 4.2 Custom Post Type UI specification, all 16 families

Shared taxonomies registered once in Custom Post Type UI: cnf_family with 16 terms f1 through f16; cnf_place with 28 terms toronto, mississauga, brampton, scarborough, etobicoke, north-york, markham, vaughan, richmond-hill, oakville, ottawa, oshawa, guelph, hamilton, windsor, ontario, quebec, british-columbia, alberta, manitoba, saskatchewan, nova-scotia, new-brunswick, newfoundland-and-labrador, prince-edward-island, yukon, northwest-territories, nunavut; cnf_service with 12 terms nil-t2-filing, catch-up-nil-t2-filing, dormant-corporation-filing, final-t2-before-dissolution, t2-short-filing, nil-t2-filing-cost, unfiled-corporate-tax-returns, no-activity-corporation-tax-return, numbered-corporation-nil-filing, inactive-holding-corporation-t2-filing, nil-t2-filing-deadline, nil-t2-filing-for-non-resident-owned-corporations; cnf_tax_year with terms 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026.

| Family | Post type slug | Rewrite slug | Supports | Taxonomies and terms | Post meta keys written by the pipeline | Rank Math sitemap slice |
|---|---|---|---|---|---|---|
| F1 Industry and entity verticals | nil_vertical | industry | title, editor, excerpt, thumbnail, custom-fields, revisions, author | cnf_family term f1, cnf_entity with 215 terms including numbered-corporation, dormant-holding-corporation, rental-corporation, professional-corporation, trucking-corporation | cnf_entity_name, cnf_entity_is_nil, cnf_not_nil_reason, cnf_price_incl_hst, cnf_overflow_price_incl_hst, cnf_last_verified_et, cnf_reviewer_schema_id, cnf_primary_keyword, cnf_internal_links_json, cnf_update_note | nil_vertical-sitemap.xml |
| F2 Calculators and checkers | nil_calculator | calculator | title, editor, excerpt, thumbnail, custom-fields, revisions, author | cnf_family term f2, cnf_tool with 150 terms including nil-t2-deadline-calculator, first-tax-year-53-week-checker, t2-short-eligibility-checker, gifi-omission-checker | cnf_calc_type, cnf_calc_config_json, cnf_calc_inputs_json, cnf_calc_rules_json, cnf_result_copy_json, cnf_last_verified_et, cnf_reviewer_schema_id, cnf_primary_keyword | nil_calculator-sitemap.xml |
| F3 City hubs | nil_city_hub | city | title, editor, excerpt, thumbnail, custom-fields, revisions, author, page-attributes | cnf_family term f3, cnf_place with the 15 city terms | cnf_place_name, cnf_place_type, cnf_place_slug, cnf_child_service_ids_json, cnf_local_filing_note, cnf_last_verified_et, cnf_primary_keyword, cnf_internal_links_json | nil_city_hub-sitemap.xml |
| F4 Service x place matrix | nil_service_place | / | title, editor, excerpt, thumbnail, custom-fields, revisions, author | cnf_family term f4, cnf_place with 28 terms, cnf_service with 12 terms | cnf_service_slug, cnf_place_slug, cnf_place_name, cnf_place_type, cnf_jurisdiction_return, cnf_provincial_return_name, cnf_price_incl_hst, cnf_overflow_price_incl_hst, cnf_deadline_rule, cnf_unique_data_block_json, cnf_last_verified_et, cnf_primary_keyword | nil_service_place-sitemap.xml |
| F5 Question pages | nil_question | answers | title, editor, excerpt, custom-fields, revisions, author | cnf_family term f5, cnf_topic with 45 question topics | cnf_question_text, cnf_short_answer, cnf_long_answer, cnf_last_verified_et, cnf_reviewer_schema_id, cnf_primary_keyword, cnf_internal_links_json | nil_question-sitemap.xml |
| F6 Best and route listicles | nil_listicle | best | title, editor, excerpt, thumbnail, custom-fields, revisions, author | cnf_family term f6, cnf_place, cnf_topic | cnf_list_rows_json, cnf_published_price_source_date, cnf_comparison_disclaimer, cnf_last_verified_et, cnf_primary_keyword | nil_listicle-sitemap.xml |
| F7 Comparison pages | nil_comparison | compare | title, editor, excerpt, thumbnail, custom-fields, revisions, author | cnf_family term f7, cnf_competitor with terms bluepeak, turbotax, t2inc, taxdeep, hrblock, cloudtax | cnf_competitor_name, cnf_competitor_published_price, cnf_competitor_intake_method, cnf_our_price_incl_hst, cnf_feature_rows_json, cnf_price_checked_on, cnf_last_verified_et | nil_comparison-sitemap.xml |
| F8 Cost and pricing | nil_cost | cost | title, editor, excerpt, thumbnail, custom-fields, revisions, author | cnf_family term f8, cnf_place, cnf_service | cnf_price_incl_hst, cnf_hst_component, cnf_net_revenue, cnf_overflow_price_incl_hst, cnf_included_rows_json, cnf_excluded_rows_json, cnf_last_verified_et | nil_cost-sitemap.xml |
| F9 Guides and pillars | nil_guide | guides | title, editor, excerpt, thumbnail, custom-fields, revisions, author, page-attributes | cnf_family term f9, cnf_topic, cnf_tax_year | cnf_guide_sections_json, cnf_toc_json, cnf_reviewer_schema_id, cnf_last_verified_et, cnf_child_ids_json, cnf_primary_keyword, cnf_update_note | nil_guide-sitemap.xml |
| F10 How-to-start and first-filing | nil_first_filing | start | title, editor, excerpt, thumbnail, custom-fields, revisions, author | cnf_family term f10, cnf_place, cnf_tax_year | cnf_step_rows_json, cnf_schedule_24_note, cnf_53_week_rule_note, cnf_year_end_match_note, cnf_last_verified_et, cnf_primary_keyword | nil_first_filing-sitemap.xml |
| F11 Reviews hub and by city | nil_review_hub | reviews | title, editor, excerpt, thumbnail, custom-fields, revisions, author | cnf_family term f11, cnf_place with the 15 city terms | cnf_place_name, cnf_trustindex_widget_id, cnf_review_count_verified_on, cnf_claim_audit_ref, cnf_last_verified_et | nil_review_hub-sitemap.xml |
| F12 Case studies | nil_case_study | case-studies | title, editor, excerpt, thumbnail, custom-fields, revisions, author | cnf_family term f12, cnf_place, cnf_entity | cnf_case_years_filed, cnf_case_jurisdiction, cnf_case_outcome, cnf_case_consent_on_file, cnf_case_anonymised, cnf_last_verified_et | nil_case_study-sitemap.xml |
| F13 Blog posts | post | blog | title, editor, excerpt, thumbnail, custom-fields, revisions, author, comments off | cnf_family term f13, cnf_topic, cnf_place, cnf_tax_year, native category and post_tag | cnf_primary_keyword, cnf_published_et, cnf_modified_et, cnf_reviewer_schema_id, cnf_internal_links_json, cnf_update_note, cnf_hero_image_url, cnf_meta_description | post-sitemap.xml |
| F14 Deadline and date pages | nil_deadline | deadlines | title, editor, excerpt, thumbnail, custom-fields, revisions, author | cnf_family term f14, cnf_tax_year, cnf_place | cnf_fiscal_year_end, cnf_t2_due_date, cnf_dissolution_due_rule, cnf_business_day_rule, cnf_ontario_holiday_list_json, cnf_last_verified_et, cnf_update_note | nil_deadline-sitemap.xml |
| F15 Trust, legal and utility | page | root | title, editor, custom-fields, revisions, author, page-attributes | cnf_family term f15 registered against the page post type | cnf_legal_version, cnf_effective_date_et, cnf_claim_audit_ref, cnf_accessibility_conformance, cnf_last_verified_et | page-sitemap.xml |
| F16 Hub and index pages | page | root | title, editor, custom-fields, revisions, author, page-attributes | cnf_family term f16 registered against the page post type | cnf_hub_children_query_json, cnf_hub_facet_config_json, cnf_child_count, cnf_last_verified_et | page-sitemap.xml |

Family 4 is the only root-level custom post type. Its Custom Post Type UI rewrite slug is a single forward slash with "with front" set to false, and a WPCode Lite snippet registers the catch-all rewrite rule last and enforces a reserved-slug list so no page, hub or blog post can take one of the 336 Family 4 slugs. Families 15 and 16 share page-sitemap.xml and are separated by the cnf_family term for reporting and for Elementor display conditions.

## 4.3 No-ACF custom fields

Every custom field is native WordPress post meta, registered and read without ACF. Custom Post Type UI registers each post type with custom-fields support and "Show in REST" on, and registers cnf_family, cnf_place, cnf_service, cnf_entity, cnf_tool, cnf_topic, cnf_competitor and cnf_tax_year as public taxonomies attached to the right post types. A single WPCode Lite snippet runs register_meta for every cnf_ key listed above with single set to true, show_in_rest set to true, a type declaration of string, number or object, and an auth_callback that requires edit_posts, which puts each key into the REST meta object and into the post editor. The Python publishing pipeline writes those keys through the WordPress MCP connector in the same REST call that creates the post, so title, body, taxonomy terms and meta land atomically. Elementor Pro then reads the same keys with no plugin bridge: the Post Custom Field dynamic tag fills headings, paragraphs, prices, dates and button URLs, the Loop Grid builds hubs from a taxonomy query on cnf_place, cnf_service or cnf_entity, and conditional display on a meta key hides a block when the pipeline leaves that key empty. Rank Math PRO pulls the same values into titles, meta descriptions and schema templates through the %customfield(cnf_place_name)% and %customfield(cnf_price_incl_hst)% variables, so one written value drives body copy, the title tag, the meta description and the JSON-LD without duplication.

## 4.4 Elementor Pro template list

| Family | Elementor Pro template type | Template name | Display condition | Dynamic tags used | Notes |
|---|---|---|---|---|---|
| F1 Industry and entity verticals | Single Post | Single – Industry Vertical | Singular, nil_vertical, all | cnf_entity_name, cnf_entity_is_nil, cnf_not_nil_reason, cnf_price_incl_hst, cnf_last_verified_et | Shows the not-nil warning block only when cnf_entity_is_nil is 0 |
| F2 Calculators and checkers | Single Post | Single – Calculator | Singular, nil_calculator, all | cnf_calc_type, cnf_calc_config_json, cnf_result_copy_json | Calculator runs from a WPCode Lite script that reads cnf_calc_config_json |
| F3 City hubs | Single Post | Single – City Hub | Singular, nil_city_hub, all | cnf_place_name, cnf_local_filing_note, cnf_child_service_ids_json | Loop Grid lists the 12 Family 4 pages for that city |
| F4 Service x place matrix | Single Post | Single – Service and Place | Singular, nil_service_place, all | cnf_service_slug, cnf_place_name, cnf_jurisdiction_return, cnf_unique_data_block_json, cnf_price_incl_hst | The unique data block is mandatory on all 336 pages so no page is a bare template copy |
| F5 Question pages | Single Post | Single – Question | Singular, nil_question, all | cnf_question_text, cnf_short_answer, cnf_last_verified_et | Short answer sits above the fold in one paragraph |
| F6 Best and route listicles | Single Post | Single – Listicle | Singular, nil_listicle, all | cnf_list_rows_json, cnf_published_price_source_date, cnf_comparison_disclaimer | Rows state published prices and features only |
| F7 Comparison pages | Single Post | Single – Comparison | Singular, nil_comparison, all | cnf_competitor_name, cnf_competitor_published_price, cnf_our_price_incl_hst, cnf_price_checked_on | No negative claim about any competitor appears in the template |
| F8 Cost and pricing | Single Post | Single – Cost | Singular, nil_cost, all | cnf_price_incl_hst, cnf_hst_component, cnf_included_rows_json, cnf_excluded_rows_json | Price block is a single dynamic value so both sites cannot drift |
| F9 Guides and pillars | Single Post | Single – Guide | Singular, nil_guide, all | cnf_toc_json, cnf_guide_sections_json, cnf_reviewer_schema_id, cnf_last_verified_et | Easy Table of Contents renders from headings, visible reviewed date in the header |
| F10 How-to-start and first-filing | Single Post | Single – First Filing | Singular, nil_first_filing, all | cnf_step_rows_json, cnf_schedule_24_note, cnf_53_week_rule_note | Steps render as an ordered list with no HowTo markup |
| F11 Reviews hub and by city | Single Post | Single – Reviews Hub | Singular, nil_review_hub, all | cnf_place_name, cnf_trustindex_widget_id, cnf_review_count_verified_on | Trustindex widget renders with rich snippets switched off |
| F12 Case studies | Single Post | Single – Case Study | Singular, nil_case_study, all | cnf_case_years_filed, cnf_case_jurisdiction, cnf_case_outcome | Publishes only when cnf_case_consent_on_file is 1 |
| F13 Blog posts | Single Post | Single – Blog Post | Singular, Posts, all | cnf_published_et, cnf_modified_et, cnf_reviewer_schema_id, cnf_update_note | Visible published and updated dates sit under the title |
| F14 Deadline and date pages | Single Post | Single – Deadline | Singular, nil_deadline, all | cnf_fiscal_year_end, cnf_t2_due_date, cnf_business_day_rule | Date block re-renders on every pipeline refresh |
| F15 Trust, legal and utility | Single Page | Single – Trust and Legal | Pages in cnf_family term f15 | cnf_legal_version, cnf_effective_date_et, cnf_accessibility_conformance | If the taxonomy condition is unavailable on pages, assign by a Specific Pages list of the 24 URLs |
| F16 Hub and index pages | Single Page | Single – Hub Index | Pages in cnf_family term f16 | cnf_hub_children_query_json, cnf_hub_facet_config_json, cnf_child_count | Loop Grid with taxonomy filters on cnf_place, cnf_service and cnf_entity |

Four global templates sit outside the family list: Header – Global, Footer – Global carrying the firm block, Popup – Exit on pricing pages, and Single – 404.

## 4.5 Dated build table, September 21 to November 20, 2026

| Date | Deliverable | Owner | Dependency | Done-when test | Notes |
|---|---|---|---|---|---|
| Tuesday, September 22, 2026 | Hosting, DNS, SSL, WAF and CDN live on corpnilfilingfor300.ca with the staging clone | Navneet | Domain in hand | SSL Labs grade A, HSTS header present, staging resolves and is noindexed, WAF blocks a scripted 100-request burst on /lookup/ | Cutover TTL returns to 3600 seconds after 48 hours |
| Wednesday, September 23, 2026 | WordPress core, Astra Pro, Elementor Pro, Rank Math PRO, LiteSpeed Cache, UpdraftPlus, Custom Post Type UI and WPCode Lite installed and licensed | Navneet | Hosting live | All plugins active on live and staging, no licence warning in the dashboard | Auto-update off, Tuesday 06:00 Eastern update window |
| Friday, September 25, 2026 | 14 custom post types and 8 taxonomies registered in Custom Post Type UI, 28 cnf_place terms and 12 cnf_service terms loaded | Navneet | September 23, 2026 plugin stack | A test item in each post type returns 200 at its rewrite slug, all 28 place terms and 12 service terms present | Family 4 root rewrite tested against a page of the same slug |
| Friday, September 25, 2026 | register_meta snippet in WPCode Lite for every cnf_ key, REST meta visible | Navneet | Post types registered | GET on /wp-json/wp/v2/nil_service_place/{id} returns the meta object with cnf_place_name and cnf_price_incl_hst | Auth callback requires edit_posts |
| Tuesday, September 29, 2026 | Rank Math sitemap slices, robots.txt, canonical rules and the schema validator rule that blocks the EFILE number and CRA GroupID | Navneet | Post types registered | 16 sitemap URLs resolve, robots.txt allows crawl, validator rejects a test block containing an EFILE-format number | Sitemaps carry no credential values |
| Friday, October 2, 2026 | Elementor global kit, Header – Global and Footer – Global with the firm block | Navneet | September 23, 2026 plugin stack | Footer renders the firm block on every template, contrast passes 4.5 to 1 | Footer copy is the exact text in Section 5 |
| Friday, October 2, 2026 | UpdraftPlus schedule live and a full restore rehearsed on staging | Navneet | Hosting live | Staging restores from the latest backup with the database intact | Files daily 03:00 Eastern, database every 4 hours |
| Wednesday, October 7, 2026 | Python publishing pipeline and WordPress MCP connector publishing to live | Navneet | Post types, meta and sitemap rules live | A 10-URL dry run publishes with meta, terms, Rank Math title and description, then purges CDN | Publish log retained 12 months |
| Friday, October 9, 2026 | 16 Elementor Pro family templates plus the 4 global templates built and assigned | Navneet | Post types and meta live | Each template renders a test item with every dynamic tag populated and no empty block | Conditional display hides blocks on empty meta |
| Friday, October 9, 2026 | First content set published: F8 15, F9 10, F15 24, F16 5 and the home page, 55 URLs | Navneet | Pipeline live | 55 URLs return 200, appear in the right sitemap slice and carry a visible last-reviewed date | Matches the dated build table for Friday, October 9, 2026 |
| Friday, October 23, 2026 | Filing form embedded in the checkout block on every template | Navneet, with the form from Deepak | Deepak's form rows above complete by October 16, 2026 and templates assigned | A test purchase and T183CORP signature complete from a live page | Every form row owned by Deepak lands on or before this date |
| Wednesday, November 18, 2026 | WCAG 2.1 AA and AODA audit passed across the home page, a Family 4 page, the pay form and the sign form | Navneet | Form embedded on October 23, 2026 and Family 4 pages live on November 13, 2026 | Keyboard-only run completes a test purchase and signature, contrast and focus checks pass, accessibility statement published | Remediation closed before launch |
| Wednesday, November 18, 2026 | Schema deployed and validated, AccountingService restricted to the four address pages | Navneet | All 16 families live on November 13, 2026 | Rich Results Test returns no error, AccountingService appears on 4 URLs and on no other, validator finds no EFILE number and no CRA GroupID | No FAQPage, no HowTo, no review or aggregateRating markup |

The content batches of October 16, October 23, October 30, November 6 and November 13, 2026 and the blog cadence of 10 posts every Friday follow the Dated build schedule section. Ontario Thanksgiving, Monday, October 12, 2026, carries no deliverable.

# Section 5. Trust and authority layer

## 5.1 Trust-element table

| Element | Exact on-page copy | Placement | Schema type | Schema properties | Notes |
|---|---|---|---|---|---|
| Firm registration | Gondaliya CPA Professional Corporation is a CPA Ontario registered firm. Firm Registration 61330051. | Global footer, every page | Organization | legalName, identifier, parentOrganization, url | Same sentence on gondaliyacpa.ca and opencorporationfor35.ca |
| Reviewing CPA | Sharad Gondaliya, CPA (Canada and USA). CPA Ontario Membership 61040184. Washington 57629. Montana PAC-CPAP-LIC-033176. | About page, every guide header, every blog byline | Person | name, jobTitle, hasCredential, identifier, worksFor | Credential numbers are public registry values, not EFILE values |
| Second CPA | Vandana Goel, CPA. CPA Ontario Membership 61158584. | About page, review step copy | Person | name, jobTitle, hasCredential, identifier, worksFor | Named so clients know two CPAs stand behind the file |
| Electronic filing status | We are a registered EFILE electronic filer. Your return is transmitted to the Canada Revenue Agency electronically. | Home page hero, every Family 4 page, checkout step 1 | None | None | EFILE number never appears on the site, in schema, in a sitemap or in an email |
| Price | $300.00 including HST per tax year. One price for every year and every province. No hourly billing and no add-on fees. | Home page, every cost page, checkout | Offer | price, priceCurrency, valueAddedTaxIncluded, priceSpecification, availability | HST component is $34.51, net revenue $265.49 |
| Turnaround | Your CRA confirmation is emailed within 3 business days. Business days are Monday to Friday and exclude Ontario statutory holidays. | Home page, checkout confirmation screen, confirmation email | Service | serviceOutput, termsOfService | Promise is provable from the transmission log |
| T183CORP signing | You sign Form T183CORP as the authorized signing officer before your return is transmitted. The form carries your return's figures, the date and an HH:MM:SS timestamp, and it is never backdated. | Signing screen, how-it-works section, every guide | None | None | Signature is captured before transmission, without exception |
| Signing security | Your signing link is single-use and expires in 72 hours. It reopens only after you re-enter your corporation name and Business Number. | Signing link email, signing screen | None | None | Tokenised access-controlled screen, no shared link |
| Identity and direct dealing | We verify your identity and your authority to sign before we transmit. We deal with you directly and never through a third party. | Checkout step 3, about page | None | None | No intermediary is permitted in the flow |
| Work performed in Canada | Your return is prepared and transmitted in Canada. Our credentials are never shared and no part of your file is sent offshore. | About page, footer of every Family 4 page | Organization | areaServed, location | Provable from the access log |
| Six-year retention | We keep your signed Form T183CORP for six years. It is not sent to the Canada Revenue Agency unless the Canada Revenue Agency asks for it. | Signing screen, privacy policy | None | None | Retention label is set to six years then review |
| Payment security | Pay by credit card, debit, Apple Pay or Google Pay. Payments are processed by Stripe. We never see or store your card number. | Checkout, pricing pages | Offer | acceptedPaymentMethod | Interac Debit runs through the wallets once Stripe enables it |
| Late-filing qualification | A true nil return owes $0.00, so no percentage late-filing penalty applies to it. An unfiled year still stays open forever, invites a demand to file and an arbitrary assessment, blocks a clearance certificate and dissolution, and costs a non-resident corporation $25.00 per day up to $2,500.00. | Every catch-up page, every unfiled page, every deadline page | None | None | Both sentences publish together or neither publishes |
| Mandatory electronic filing | For tax years starting after 2023 electronic filing is mandatory for virtually all corporations. A paper T2 draws a $1,000.00 penalty plus a $100.00 per-return preparer penalty. | Every guide, every first-filing page | None | None | Both penalty figures are stated together |
| Scope of a nil return | This service is for a corporation with no activity in the tax year. A corporation with investment income, rental income, or dividends paid or received is not nil. | Home page, every vertical page, checkout step 2 | Service | serviceType, audience | Holding companies with investment income, rental corporations and dividend recipients are excluded by name |
| Overflow route | If your corporation is not nil, we move your file to gondaliyacpa.ca at $350.00 including HST per tax year and tell you before any further charge. | Checkout step 2, every vertical page marked not nil | None | None | No charge is taken at the higher price without the client saying yes |
| Filings this does not cover | A nil T2 does not cover your Ontario annual return through the Ontario Business Registry, a federal Corporations Canada annual return at $12.00 due within 60 days of your anniversary, an Alberta AT1, a Quebec CO-17, or a nil GST/HST or payroll filing. We tell you which of these you still owe. | Every Family 4 page, every guide | None | None | $12.00 is a government fee and HST does not apply to it |
| Office and hours | 55 Queen St E, Suite 1205, Toronto, ON M5C 1R6. 647-212-9559. info@gondaliyacpa.ca. Open 9:00 AM to 8:30 PM, Monday to Sunday. | Home page, contact page, about page, Toronto Family 4 page | AccountingService | address, telephone, email, openingHoursSpecification | No other city page carries address or opening hours markup |
| Accessibility | This site is built to WCAG 2.1 Level AA and meets the Accessibility for Ontarians with Disabilities Act. Email info@gondaliyacpa.ca or call 647-212-9559 for any page in another format. | Accessibility statement page, global footer link | None | None | Audit covers the lookup, pay and sign screens |
| Freshness and review | Reviewed by Sharad Gondaliya, CPA, CPA Ontario Membership 61040184. Last reviewed September 20, 2026. | Top of every guide, blog post, deadline page and calculator | Article | author, datePublished, dateModified | Visible update dates matter for AI Overviews and AI Mode |
| Complaints | If something goes wrong, email info@gondaliyacpa.ca or call 647-212-9559. If we do not resolve it, you can take the matter to CPA Ontario. | Global footer, terms of service | None | None | Log is reviewed monthly |
| Reviews display | Client reviews for Gondaliya CPA Professional Corporation. | Reviews hub and the 10 city review pages | None | None | Trustindex rich snippets switched off |

## 5.2 JSON-LD blocks

Block 1. Organization. Emit on every page except the four address pages.

{

"@context": "https://schema.org",

"@type": "Organization",

"@id": "https://corpnilfilingfor300.ca/#organization",

"name": "Corp Nil Filing for $300",

"alternateName": "corpnilfilingfor300.ca",

"url": "https://corpnilfilingfor300.ca/",

"description": "Nil T2 corporate tax returns for inactive Canadian corporations at $300.00 including HST per tax year, prepared and transmitted in Canada by a registered EFILE electronic filer.",

"email": "info@gondaliyacpa.ca",

"telephone": "+1-647-212-9559",

"inLanguage": "en-CA",

"logo": {

"@type": "ImageObject",

"@id": "https://corpnilfilingfor300.ca/#logo",

"url": "https://corpnilfilingfor300.ca/wp-content/uploads/brand/corpnilfilingfor300-logo.png",

"width": 512,

"height": 512,

"caption": "Corp Nil Filing for $300"

},

"image": { "@id": "https://corpnilfilingfor300.ca/#logo" },

"identifier": [

{

"@type": "PropertyValue",

"name": "CPA Ontario Firm Registration",

"value": "61330051"

}

],

"parentOrganization": {

"@type": "Organization",

"@id": "https://gondaliyacpa.ca/#organization",

"name": "Gondaliya CPA Professional Corporation",

"url": "https://gondaliyacpa.ca/",

"identifier": [

{

"@type": "PropertyValue",

"name": "CPA Ontario Firm Registration",

"value": "61330051"

}

]

},

"employee": [

{ "@id": "https://corpnilfilingfor300.ca/#sharad-gondaliya" },

{ "@id": "https://corpnilfilingfor300.ca/#vandana-goel" }

],

"areaServed": {

"@type": "Country",

"name": "Canada"

},

"knowsLanguage": ["en-CA", "fr-CA"],

"contactPoint": [

{

"@type": "ContactPoint",

"contactType": "customer service",

"telephone": "+1-647-212-9559",

"email": "info@gondaliyacpa.ca",

"availableLanguage": ["en-CA"],

"areaServed": "CA",

"hoursAvailable": {

"@type": "OpeningHoursSpecification",

"dayOfWeek": [

"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"

],

"opens": "09:00",

"closes": "20:30"

}

}

]

}

Block 2. AccountingService. Emit only on https://corpnilfilingfor300.ca/, /contact/, /about/ and /nil-t2-filing-toronto/, the four pages that display 55 Queen St E, Suite 1205 as their own business location. On those four pages this block replaces Block 1.

{

"@context": "https://schema.org",

"@type": "AccountingService",

"@id": "https://corpnilfilingfor300.ca/#organization",

"name": "Corp Nil Filing for $300",

"url": "https://corpnilfilingfor300.ca/",

"description": "Nil T2 corporate tax return filing for inactive Canadian corporations at $300.00 including HST per tax year.",

"email": "info@gondaliyacpa.ca",

"telephone": "+1-647-212-9559",

"image": { "@id": "https://corpnilfilingfor300.ca/#logo" },

"logo": { "@id": "https://corpnilfilingfor300.ca/#logo" },

"priceRange": "$300.00",

"currenciesAccepted": "CAD",

"paymentAccepted": "Credit card, Debit card, Apple Pay, Google Pay",

"address": {

"@type": "PostalAddress",

"streetAddress": "55 Queen St E, Suite 1205",

"addressLocality": "Toronto",

"addressRegion": "ON",

"postalCode": "M5C 1R6",

"addressCountry": "CA"

},

"openingHoursSpecification": [

{

"@type": "OpeningHoursSpecification",

"dayOfWeek": [

"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"

],

"opens": "09:00",

"closes": "20:30"

}

],

"identifier": [

{

"@type": "PropertyValue",

"name": "CPA Ontario Firm Registration",

"value": "61330051"

}

],

"parentOrganization": {

"@type": "Organization",

"@id": "https://gondaliyacpa.ca/#organization",

"name": "Gondaliya CPA Professional Corporation",

"url": "https://gondaliyacpa.ca/"

},

"employee": [

{ "@id": "https://corpnilfilingfor300.ca/#sharad-gondaliya" },

{ "@id": "https://corpnilfilingfor300.ca/#vandana-goel" }

],

"areaServed": { "@type": "Country", "name": "Canada" },

"makesOffer": { "@id": "https://corpnilfilingfor300.ca/#offer-nil-t2" }

}

Block 3. Service and Offer. Emit on /nil-t2-filing/, every cost page and every Family 4 page.

{

"@context": "https://schema.org",

"@type": "Service",

"@id": "https://corpnilfilingfor300.ca/#service-nil-t2",

"name": "Nil T2 corporate tax return filing",

"serviceType": "Nil T2 corporate tax return preparation and electronic filing",

"description": "Preparation and electronic filing of a nil T2 corporate tax return for a Canadian corporation with no activity in the tax year. Form T183CORP is signed by the authorized signing officer on a secure access-controlled screen before transmission. CRA confirmation is emailed within 3 business days.",

"url": "https://corpnilfilingfor300.ca/nil-t2-filing/",

"inLanguage": "en-CA",

"provider": {

"@type": "Organization",

"@id": "https://corpnilfilingfor300.ca/#organization",

"name": "Corp Nil Filing for $300",

"url": "https://corpnilfilingfor300.ca/",

"parentOrganization": {

"@type": "Organization",

"@id": "https://gondaliyacpa.ca/#organization",

"name": "Gondaliya CPA Professional Corporation",

"url": "https://gondaliyacpa.ca/"

}

},

"areaServed": [

{ "@type": "AdministrativeArea", "name": "Ontario" },

{ "@type": "AdministrativeArea", "name": "Quebec" },

{ "@type": "AdministrativeArea", "name": "British Columbia" },

{ "@type": "AdministrativeArea", "name": "Alberta" },

{ "@type": "AdministrativeArea", "name": "Manitoba" },

{ "@type": "AdministrativeArea", "name": "Saskatchewan" },

{ "@type": "AdministrativeArea", "name": "Nova Scotia" },

{ "@type": "AdministrativeArea", "name": "New Brunswick" },

{ "@type": "AdministrativeArea", "name": "Newfoundland and Labrador" },

{ "@type": "AdministrativeArea", "name": "Prince Edward Island" },

{ "@type": "AdministrativeArea", "name": "Yukon" },

{ "@type": "AdministrativeArea", "name": "Northwest Territories" },

{ "@type": "AdministrativeArea", "name": "Nunavut" }

],

"audience": {

"@type": "BusinessAudience",

"name": "Canadian corporations with no activity in the tax year"

},

"offers": {

"@type": "Offer",

"@id": "https://corpnilfilingfor300.ca/#offer-nil-t2",

"name": "Nil T2 return, one tax year",

"url": "https://corpnilfilingfor300.ca/start/",

"price": "300.00",

"priceCurrency": "CAD",

"valueAddedTaxIncluded": true,

"availability": "https://schema.org/InStock",

"priceValidUntil": "2027-09-20",

"eligibleRegion": { "@type": "Country", "name": "Canada" },

"priceSpecification": {

"@type": "UnitPriceSpecification",

"price": "300.00",

"priceCurrency": "CAD",

"valueAddedTaxIncluded": true,

"referenceQuantity": {

"@type": "QuantitativeValue",

"value": 1,

"unitText": "tax year"

}

},

"acceptedPaymentMethod": [

{ "@type": "PaymentMethod", "name": "Credit card" },

{ "@type": "PaymentMethod", "name": "Debit card" },

{ "@type": "PaymentMethod", "name": "Apple Pay" },

{ "@type": "PaymentMethod", "name": "Google Pay" }

],

"offeredBy": {

"@type": "Organization",

"@id": "https://corpnilfilingfor300.ca/#organization",

"parentOrganization": {

"@type": "Organization",

"@id": "https://gondaliyacpa.ca/#organization",

"name": "Gondaliya CPA Professional Corporation",

"url": "https://gondaliyacpa.ca/"

}

}

}

}

Block 4. Person, Sharad Gondaliya.

{

"@context": "https://schema.org",

"@type": "Person",

"@id": "https://corpnilfilingfor300.ca/#sharad-gondaliya",

"name": "Sharad Gondaliya",

"givenName": "Sharad",

"familyName": "Gondaliya",

"jobTitle": "Chartered Professional Accountant",

"url": "https://corpnilfilingfor300.ca/about/",

"email": "info@gondaliyacpa.ca",

"telephone": "+1-647-212-9559",

"worksFor": {

"@type": "Organization",

"@id": "https://gondaliyacpa.ca/#organization",

"name": "Gondaliya CPA Professional Corporation",

"url": "https://gondaliyacpa.ca/"

},

"affiliation": { "@id": "https://corpnilfilingfor300.ca/#organization" },

"knowsAbout": [

"T2 corporate tax returns",

"Nil and dormant corporation filings",

"T2 Short return eligibility",

"Form T183CORP",

"Corporate dissolution and final returns"

],

"hasCredential": [

{

"@type": "EducationalOccupationalCredential",

"credentialCategory": "Professional designation",

"name": "Chartered Professional Accountant, Ontario",

"recognizedBy": {

"@type": "Organization",

"name": "Chartered Professional Accountants of Ontario"

},

"identifier": {

"@type": "PropertyValue",

"name": "CPA Ontario Membership",

"value": "61040184"

}

},

{

"@type": "EducationalOccupationalCredential",

"credentialCategory": "Professional licence",

"name": "Certified Public Accountant, Washington",

"recognizedBy": {

"@type": "Organization",

"name": "Washington State Board of Accountancy"

},

"identifier": {

"@type": "PropertyValue",

"name": "Washington CPA Licence",

"value": "57629"

}

},

{

"@type": "EducationalOccupationalCredential",

"credentialCategory": "Professional licence",

"name": "Certified Public Accountant, Montana",

"recognizedBy": {

"@type": "Organization",

"name": "Montana Board of Public Accountants"

},

"identifier": {

"@type": "PropertyValue",

"name": "Montana CPA Licence",

"value": "PAC-CPAP-LIC-033176"

}

}

]

}

Block 5. Person, Vandana Goel.

{

"@context": "https://schema.org",

"@type": "Person",

"@id": "https://corpnilfilingfor300.ca/#vandana-goel",

"name": "Vandana Goel",

"givenName": "Vandana",

"familyName": "Goel",

"jobTitle": "Chartered Professional Accountant",

"url": "https://corpnilfilingfor300.ca/about/",

"email": "info@gondaliyacpa.ca",

"worksFor": {

"@type": "Organization",

"@id": "https://gondaliyacpa.ca/#organization",

"name": "Gondaliya CPA Professional Corporation",

"url": "https://gondaliyacpa.ca/"

},

"affiliation": { "@id": "https://corpnilfilingfor300.ca/#organization" },

"knowsAbout": [

"T2 corporate tax returns",

"GIFI schedules 100, 125 and 141",

"Schedule 50 shareholder reporting",

"Loss continuity and Schedule 8"

],

"hasCredential": [

{

"@type": "EducationalOccupationalCredential",

"credentialCategory": "Professional designation",

"name": "Chartered Professional Accountant, Ontario",

"recognizedBy": {

"@type": "Organization",

"name": "Chartered Professional Accountants of Ontario"

},

"identifier": {

"@type": "PropertyValue",

"name": "CPA Ontario Membership",

"value": "61158584"

}

}

]

}

Block 6. Article template. Emit on every blog post, guide, question page, deadline page and case study.

{

"@context": "https://schema.org",

"@type": "Article",

"@id": "{{URL}}#article",

"mainEntityOfPage": { "@type": "WebPage", "@id": "{{URL}}" },

"url": "{{URL}}",

"headline": "{{HEADLINE}}",

"description": "{{DESCRIPTION}}",

"inLanguage": "en-CA",

"articleSection": "{{SECTION}}",

"keywords": "{{KEYWORDS}}",

"image": {

"@type": "ImageObject",

"url": "{{IMAGE_URL}}",

"width": 1200,

"height": 675

},

"datePublished": "{{DATE_PUBLISHED}}",

"dateModified": "{{DATE_MODIFIED}}",

"author": { "@id": "{{AUTHOR_ID}}" },

"publisher": { "@id": "https://corpnilfilingfor300.ca/#organization" },

"isPartOf": {

"@type": "WebSite",

"@id": "https://corpnilfilingfor300.ca/#website",

"name": "Corp Nil Filing for $300",

"url": "https://corpnilfilingfor300.ca/",

"publisher": { "@id": "https://corpnilfilingfor300.ca/#organization" },

"inLanguage": "en-CA"

},

"about": {

"@type": "Thing",

"name": "Nil T2 corporate tax return filing in Canada"

}

}

Article token map.

| Token | Source | Format written by the pipeline | Notes |
|---|---|---|---|
| {{URL}} | WordPress permalink | Absolute HTTPS URL with a trailing slash | Canonical and schema URL must match exactly |
| {{HEADLINE}} | cnf_headline | Plain text, 110 characters maximum | Truncated by the pipeline, never by the theme |
| {{DESCRIPTION}} | cnf_meta_description | Plain text, 155 characters maximum | Same string feeds the Rank Math meta description |
| {{SECTION}} | Primary cnf_topic term name | Plain text | One term only |
| {{KEYWORDS}} | cnf_primary_keyword | nil t2 filing, dormant corporation t2, inactive corporation tax return | Comma separated on one line |
| {{IMAGE_URL}} | cnf_hero_image_url | Absolute HTTPS URL, 1200 by 675 pixels | Imagify serves WebP to browsers, the schema URL stays the original |
| {{DATE_PUBLISHED}} | cnf_published_et | 2026-09-20T09:00:00-04:00 | Eastern Time offset written server side, never from the browser |
| {{DATE_MODIFIED}} | cnf_modified_et | 2026-09-20T09:00:00-04:00 | Advanced only on a real content review, and shown on the page |
| {{AUTHOR_ID}} | cnf_author_schema_id | https://corpnilfilingfor300.ca/#sharad-gondaliya | The Vandana Goel value is https://corpnilfilingfor300.ca/#vandana-goel |

Schema rules enforced by the pipeline validator. No block contains the EFILE number or the CRA GroupID, and any candidate block matching either pattern fails the build. No Review, no aggregateRating and no ratingValue property is emitted anywhere on the site. AccountingService and any other LocalBusiness subtype appear only on the four pages listed under Block 2, and every other page emits Organization with no address, no geo and no openingHoursSpecification.

FAQPage is omitted because FAQ rich results ended on May 7, 2026 and the markup now returns nothing while adding a parsing and compliance surface. HowTo is omitted because it earns no result and the filing steps read better as visible on-page copy. Trustindex rich snippets stay off because self-serving review schema earns no stars and publishing it would put an unverified aggregate count into markup while the claim-consistency audit across both sites is still a hard launch gate.

# 6. SEO architecture

The sitemap is a 16-family mirror of gondaliyacpa.ca, rebuilt for one offer: a nil T2 return at $300.00 including HST per tax year. Source total 1,178 URLs. Target total 1,422 URLs plus 1 home page = 1,423.

## 6(a) Site structure and URL plan, family by family

URL grammar, fixed for all 1,423 URLs:

- Lowercase, hyphen-separated, trailing slash, no stop words, no dates in the path, no numbers in the path except a competitor price page, no query strings in canonical URLs.
- Maximum depth 2 folders. Money pages sit at root depth 1.
- The word nil appears in the slug only where the page is about a no-activity return. The word t2 appears in every service slug.
- Never write t183 in a slug. Write t183corp.
- Place tokens come only from the 15 fixed city terms and the 13 fixed jurisdiction terms.

| Family | Family name | URL pattern | Count | WordPress post type | Actual slugs already assigned | Notes |
|---|---|---|---|---|---|---|
| F1 | Industry and entity verticals | /nil-t2-filing-for-<vertical>/ | 215 | vertical | /nil-t2-filing-for-numbered-holding-corporations/, /nil-t2-filing-for-dormant-consulting-corporations/, /nil-t2-filing-for-shelf-corporations/, /nil-t2-filing-for-inactive-trucking-corporations/, /nil-t2-filing-for-closed-restaurant-corporations/ | 215 vertical tokens held in a Custom Post Type UI taxonomy |
| F2 | Calculators and checkers | /tools/<tool>/ | 150 | tool | /tools/nil-t2-deadline-calculator/, /tools/t2-short-eligibility-checker/, /tools/gifi-schedule-requirement-checker/, /tools/schedule-50-shareholder-threshold-checker/, /tools/unfiled-years-cost-calculator/ | Folder depth 2 keeps tools out of the money-page namespace |
| F3 | City hubs | /<city>/ | 15 | city | /toronto/, /mississauga/, /brampton/, /markham/, /vaughan/, /richmond-hill/, /oakville/, /ottawa/, /oshawa/, /guelph/, /hamilton/, /windsor/ | 12 slugs listed pass the local-data test in 6(k); 3 substitutes named in 6(k) |
| F4 | Service x place matrix | 12 fixed service slugs x <place> | 336 | service-place | /nil-t2-filing-ontario/, /catch-up-nil-t2-filing-toronto/, /dormant-corporation-filing-alberta/, /final-t2-before-dissolution-ontario/, /t2-short-filing-british-columbia/ | 12 x 15 cities = 180, 12 x 13 jurisdictions = 156 |
| F5 | Question pages | /answers/<question>/ | 45 | answer | /answers/does-an-inactive-corporation-have-to-file-a-t2/, /answers/can-i-e-sign-a-t183corp/, /answers/how-many-unfiled-t2-years-can-i-file-at-once/ | Answer-first template, no FAQPage markup |
| F6 | Best and route listicles | /best/<listicle>/ | 38 | listicle | /best/nil-t2-filing-services-in-canada/, /best/ways-to-catch-up-unfiled-corporate-tax-returns/, /best/order-to-file-six-unfiled-t2-years/ | Published prices and published features only |
| F7 | Comparison pages | /compare/<a>-vs-<b>/ | 20 | comparison | /compare/nil-t2-filing-vs-t2-short-filing/, /compare/corpnilfilingfor300-vs-bluepeak/, /compare/corpnilfilingfor300-vs-turbotax-business/, /compare/paper-t2-vs-efile-t2/ | 6 brand pages, 14 concept pages |
| F8 | Cost and pricing | /pricing/ and /pricing/<slug>/ | 15 | page | /pricing/, /pricing/nil-t2-filing-cost/, /pricing/cost-to-file-six-unfiled-nil-years/, /pricing/what-is-not-included/ | Every price annual and including HST |
| F9 | Guides and pillars | /guides/<guide>/ | 30 | guide | /guides/nil-t2-return-complete-guide/, /guides/catch-up-unfiled-corporate-tax-returns/, /guides/t183corp-signing-and-transmission/, /guides/final-t2-and-dissolution/ | No year token in any guide URL; see the year-stamp rule in 6(k) |
| F10 | How-to-start and first-filing | /start/<slug>/ | 25 | start | /start/first-t2-return-after-incorporation/, /start/choosing-a-first-fiscal-year-end/, /start/schedule-24-on-the-first-return/ | Feeds from opencorporationfor35.ca |
| F11 | Reviews hub and by city | /reviews/ and /reviews/<city>/ | 11 | review | /reviews/, /reviews/toronto/, /reviews/mississauga/, /reviews/brampton/, /reviews/scarborough/, /reviews/etobicoke/, /reviews/north-york/, /reviews/markham/, /reviews/vaughan/, /reviews/ottawa/, /reviews/hamilton/ | 1 hub plus 10 city pages; no review schema anywhere |
| F12 | Case studies | /case-studies/<slug>/ | 15 | case-study | /case-studies/six-unfiled-nil-years-numbered-ontario-corporation/, /case-studies/dormant-holding-corporation-cleared-for-dissolution/ | De-identified, no client names, no logos |
| F13 | Blog posts | /blog/<slug>/ | 455 | post | /blog/cra-demand-to-file-letter-what-to-do/, /blog/share-capital-on-a-nil-t2-return/, /blog/rc145-closing-a-gst-hst-account/ | 0, 20, 30, then 45 per month for months 4 to 12 |
| F14 | Deadline and date pages | /deadlines/<slug>/ | 23 | deadline | /deadlines/, /deadlines/t2-due-date-for-december-year-end/, /deadlines/t2-due-date-for-june-year-end/, /deadlines/efile-january-31-cutover/, /deadlines/53-week-first-tax-year-rule/ | 12 month-end pages plus 11 rule pages |
| F15 | Trust, legal and utility | /<slug>/ | 24 | page | /about/, /contact/, /our-cpas/, /sharad-gondaliya-cpa/, /vandana-goel-cpa/, /cpa-ontario-registration/, /t183corp-signing-explained/, /identity-verification/, /security/, /privacy-policy/, /terms-of-service/, /engagement-terms/, /fee-schedule/, /refund-policy/, /complaints-and-resolution/, /accessibility/, /what-we-do-not-do/, /how-we-protect-your-data/, /referrals-to-gondaliyacpa/, /sitemap/, /thank-you/, /payment-failed/, /signing-link-expired/, /not-a-nil-return/ | 24 slugs listed in full |
| F16 | Hub and index pages | /<hub>/ | 5 | page | /services/, /tools/, /locations/, /guides/, /blog/ | Each hub links every child in its family |
| Home | Home page | / | 1 | page | / | Seven-step flow in fixed order |
| Total | — | — | 1,423 | 14 post types | — | 1,422 plus 1 home page |

Copy-paste title tag, meta description and H1, one exemplar per family.

| Family | URL | Title tag | Meta description | H1 | Notes |  |
|---|---|---|---|---|---|---|
| F1 | /nil-t2-filing-for-numbered-holding-corporations/ | Nil T2 for Numbered Holding Corporations \ | $300.00 Incl HST | File a nil T2 for a numbered holding corporation online. $300.00 including HST per tax year. CPA reviewed. CRA confirmation emailed within 3 business days. | Nil T2 Filing for Numbered Holding Corporations | A holding corporation with dividend, interest or rent income is not nil |
| F2 | /tools/t2-short-eligibility-checker/ | T2 Short Eligibility Checker \ | Free, No Sign-Up | Check in 8 questions whether your corporation can use the T2 Short. Free. No sign-up. Built by a CPA Ontario firm in Toronto. | T2 Short Eligibility Checker | 8 questions map to the 8 T2 Short conditions |
| F3 | /toronto/ | Nil T2 Filing in Toronto \ | $300.00 Incl HST Per Year | Nil T2 filing for Toronto corporations. $300.00 including HST per tax year. Name to signed T183CORP online. CRA confirmation within 3 business days. | Nil T2 Filing in Toronto | Carries the Toronto local data value |
| F4 | /nil-t2-filing-ontario/ | Nil T2 Filing Ontario \ | $300.00 Incl HST Per Tax Year | Nil T2 filing for Ontario corporations at $300.00 including HST per tax year. No meetings. Pay, sign T183CORP, CPA review, CRA confirmation. | Nil T2 Filing in Ontario | Pattern repeats across 28 places |
| F5 | /answers/does-an-inactive-corporation-have-to-file-a-t2/ | Does an Inactive Corporation Have to File a T2? | Yes. Every resident corporation, including an inactive one, must file a T2 within six months of its fiscal year-end, every year, until it is dissolved. | Does an Inactive Corporation Have to File a T2? | Answer-first paragraph is the meta description |  |
| F6 | /best/ways-to-catch-up-unfiled-corporate-tax-returns/ | Best Ways to Catch Up Unfiled Corporate Tax Returns | Six routes to catch up unfiled corporate tax returns in Canada, with published prices and published features for each. Updated monthly. | Best Ways to Catch Up Unfiled Corporate Tax Returns | No negative claim about any named provider |  |
| F7 | /compare/corpnilfilingfor300-vs-bluepeak/ | corpnilfilingfor300.ca vs BluePeak \ | Price and Features | Side-by-side published prices and published features. corpnilfilingfor300.ca $300.00 including HST per tax year. BluePeak $100.00 published price. | corpnilfilingfor300.ca and BluePeak Compared | Published prices only, no negative claim |
| F8 | /pricing/nil-t2-filing-cost/ | Nil T2 Filing Cost \ | $300.00 Including HST Per Tax Year | One price. $300.00 including HST per tax year, CPA reviewed and e-filed. Overflow work moves to gondaliyacpa.ca at $350.00 including HST per year. | Nil T2 Filing Cost | Both fee lines on every cost page |
| F9 | /guides/nil-t2-return-complete-guide/ | Nil T2 Return \ | Complete Guide for Canadian Corporations | Who must file, what a nil return is, which schedules are required, how T183CORP is signed, and what happens to unfiled years. Updated monthly. | The Complete Guide to the Nil T2 Return | Visible update date in the first screen |
| F10 | /start/first-t2-return-after-incorporation/ | First T2 Return After Incorporation \ | What to File | Your first tax year cannot exceed 53 weeks, Schedule 24 is required on the first return, and the year-end must match CRA's record. | First T2 Return After Incorporation | Links to opencorporationfor35.ca |
| F11 | /reviews/toronto/ | Nil T2 Filing Reviews from Toronto Clients | Verified reviews from Toronto corporations that filed a nil T2 return with us at $300.00 including HST per tax year. | Toronto Client Reviews | Publishes at 5 verified reviews, no review schema |  |
| F12 | /case-studies/six-unfiled-nil-years-numbered-ontario-corporation/ | Six Unfiled Nil Years, One Ontario Numbered Corporation | How six unfiled nil T2 years were prepared, signed on T183CORP and transmitted for an Ontario numbered corporation. De-identified case study. | Six Unfiled Nil Years for an Ontario Numbered Corporation | Fee shown as 6 years at $300.00 including HST each |  |
| F13 | /blog/cra-demand-to-file-letter-what-to-do/ | CRA Demand to File Letter: What to Do Next | What a demand to file means for a corporation with no activity, what an arbitrary assessment does, and the order to file missing years. | CRA Demand to File Letter: What to Do Next | Carries one original checklist |  |
| F14 | /deadlines/t2-due-date-for-december-year-end/ | T2 Due Date for a December 31 Year-End | A December 31 year-end makes the T2 due June 30. Filing is mandatory even with no activity. Nil T2 filing at $300.00 including HST per tax year. | T2 Due Date for a December 31 Year-End | Date computed server-side in Eastern Time |  |
| F15 | /t183corp-signing-explained/ | T183CORP Signing Explained \ | Secure E-Signature | Form T183CORP must be signed by an authorized signing officer before transmission, carries a date and HH:MM:SS timestamp, and is kept for six years. | How T183CORP Signing Works | Never shortens T183CORP to T183 |
| F16 | /services/ | Nil T2 Filing Services \ | corpnilfilingfor300.ca | Every nil T2 service in one place. Catch-up years, dormant corporations, final returns before dissolution, T2 Short. $300.00 including HST per year. | Our Nil T2 Filing Services | Links all 336 Family 4 children through 28 place indexes |
| Home | / | Nil T2 Filing Online \ | $300.00 Incl HST Per Tax Year | Type your corporation name. We fill the Business Number and incorporation date. Pick years, pay, sign T183CORP. CRA confirmation within 3 business days. | Nil T2 Filing, $300.00 Including HST Per Tax Year | Flow order never reordered |

Copy-paste on-screen messages for the four utility URLs.

/thank-you/ — "Payment received. Your return is being prepared in TaxCycle. You will receive your T183CORP signing link by email. The link is single use and expires in 24 hours."

/payment-failed/ — "That payment did not go through. Nothing was charged and no return was started. Try another card, Apple Pay or Google Pay. The fee is $300.00 including HST per tax year."

/signing-link-expired/ — "This T183CORP signing link has expired. For your protection each link is single use. Enter your corporation name and Business Number to be sent a new link."

/not-a-nil-return/ — "Your answers show activity in this tax year. A corporation with dividends, interest, rent or any revenue is not a nil filer. This return moves to gondaliyacpa.ca at $350.00 including HST per year. Nothing has been charged here."

## 6(b) Pillar and cluster map

| Pillar URL | Pillar family | Cluster families feeding it | Cluster URL count | Entry keyword | Internal link contract | Conversion path | Notes |
|---|---|---|---|---|---|---|---|
| /guides/nil-t2-return-complete-guide/ | F9 | F1, F5, F13 | 715 | nil t2 return | Every cluster URL links up once with an exact-match anchor; pillar links down to 30 hand-picked children | Pillar to /pricing/nil-t2-filing-cost/ to / | Largest cluster on the site |
| /guides/catch-up-unfiled-corporate-tax-returns/ | F9 | F4 catch-up and unfiled slugs, F12, F13 | 126 | unfiled corporate tax returns | 56 Family 4 URLs link up; 15 case studies link up | Pillar to /pricing/cost-to-file-six-unfiled-nil-years/ to / | Highest contribution per visit |
| /guides/t2-short-eligibility/ | F9 | F2, F5, F4 t2-short slugs | 223 | t2 short | All 28 t2-short place URLs link up | Pillar to /tools/t2-short-eligibility-checker/ to / | Tool is the conversion step |
| /guides/t183corp-signing-and-transmission/ | F9 | F15, F5 | 69 | t183corp | /t183corp-signing-explained/ and /identity-verification/ link up | Pillar to /security/ to / | Trust pillar, no price in the H1 |
| /guides/dormant-and-inactive-corporations/ | F9 | F1, F4 dormant and no-activity slugs | 271 | dormant corporation | All 56 dormant and no-activity place URLs link up | Pillar to /nil-t2-filing-ontario/ to / | Second largest cluster |
| /guides/final-t2-and-dissolution/ | F9 | F4 final slugs, F14, F12 | 66 | final t2 before dissolution | 28 final-return place URLs link up | Pillar to /case-studies/dormant-holding-corporation-cleared-for-dissolution/ to / | Clearance certificate angle |
| /guides/provincial-and-federal-annual-returns/ | F9 | F4 jurisdiction pages, F14 | 179 | ontario annual return | 156 jurisdiction URLs link up once | Pillar to /nil-t2-filing-ontario/ to / | Covers AT1, CO-17, Ontario Business Registry, $12.00 federal annual return |
| /pricing/ | F8 | F7, F8, F6 | 73 | nil t2 filing cost | All 20 comparison pages link up | /pricing/ to / | Only hub allowed to carry both fee lines twice |
| /deadlines/ | F14 | F14, F2 date tools | 173 | t2 filing deadline | 12 month-end pages and 9 date tools link up | /deadlines/ to /tools/nil-t2-deadline-calculator/ to / | Seasonal traffic peak |
| /locations/ | F16 | F3, F4 | 351 | nil t2 filing near me | 15 city hubs and 336 service-place URLs link up | /locations/ to city hub to / | Only place index; no city sub-hubs |

## 6(c) Programmatic page plan

| Family number | Family name | URL pattern | Template | Unique data field per page | Unique data source | Count live December 20, 2026 | Count live March 20, 2027 | Count live June 20, 2027 | Count live September 20, 2027 | Scaled-content safety line | Banned phrase | Required qualification | Reviewer | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | Industry and entity verticals | /nil-t2-filing-for-<vertical>/ | vertical-single | Six-field schedule requirement row: S100, S125, S141, S50, S24, S8 | TaxCycle internal schedule mapping table, refreshed monthly by Navneet | 215 | 215 | 215 | 215 | No vertical page publishes without its own six-field schedule requirement row and its own two-paragraph fact pattern. | no penalty | Holding corporations with investment income, rental corporations and dividend recipients are not nil. | Sharad Gondaliya reviews, Navneet publishes | 60 on October 23, 80 on October 30 and 75 on November 6, 2026 |
| F2 | Calculators and checkers | /tools/<tool>/ | tool-single | Calculator logic block and result strings unique to that tool | Navneet's JavaScript module library, one module per tool | 150 | 150 | 150 | 150 | No tool page publishes without a working calculation and a result screen that changes with input. | CRA approved | Result screens carry: this tool gives general information and is not a filed return. | Sharad Gondaliya checks math and reviews wording | 50 each on October 16, October 23 and October 30, 2026 |
| F3 | City hubs | /<city>/ | city-hub | Active federal corporation count with registered office in that place | Corporations Canada open-data bulk file, registered-office city field, pulled monthly | 15 | 15 | 15 | 15 | No city hub publishes without a named repeatable local data source and a current data value. | CRA partner | Data value carries its pull date in the visible caption. | Navneet pulls, Sharad Gondaliya reviews | All 15 live on October 23, 2026; 3 slugs substituted under the 6(k) test |
| F4 | Service x place matrix | 12 fixed service slugs x <place> | service-place | Place data row: corporation count, incorporation-date median, registry name, filing route | Corporations Canada open-data bulk file plus Ontario Business Registry plus Quebec NEQ register | 336 | 336 | 336 | 336 | No service and place page publishes without its own place data row and its own 120-word place paragraph. | CRA authorized | Alberta AT1 and Quebec CO-17 are separate provincial returns and are not included in the $300.00 including HST fee. | Sharad Gondaliya reviews every jurisdiction claim | 150 on November 6 and 186 on November 13, 2026 |
| F5 | Question pages | /answers/<question>/ | answer-single | 45-word answer-first paragraph written for that question only | Sharad's answer bank, one entry per question, written once | 45 | 45 | 45 | 45 | No question page publishes without a 45-word answer-first paragraph written for that question only. | T183 | A true nil return carries no percentage late-filing penalty because that penalty is a percentage of tax owing and the corporation owes $0.00, but the unfiled year stays open forever. | Sharad Gondaliya writes and reviews | No FAQPage markup, FAQ rich results ended May 7, 2026 |
| F6 | Best and route listicles | /best/<listicle>/ | listicle | Published price column and published feature column per entry | Competitor published price pages, screenshot-dated monthly by Navneet | 38 | 38 | 38 | 38 | No listicle publishes without published prices and published features for every entry and no negative claim. | cheapest guaranteed | Prices shown are the provider's published prices on the date in the caption. | Sharad Gondaliya reviews for Rule 217 | Rule 217 bars unsubstantiated advertising |
| F7 | Comparison pages | /compare/<a>-vs-<b>/ | comparison | Two published price cells and eight published feature cells | Competitor published price pages, screenshot-dated monthly | 20 | 20 | 20 | 20 | No comparison page publishes without both published price columns filled and no negative claim. | better than | Competitor comparisons state published prices and features only. | Sharad Gondaliya reviews for Rule 217 | 6 brand pages, 14 concept pages |
| F8 | Cost and pricing | /pricing/ and /pricing/<slug>/ | pricing | Fee line and multi-year total for that scenario | Internal fee schedule, single source of truth in one post-meta record | 15 | 15 | 15 | 15 | No cost page publishes without the full fee line $300.00 including HST per tax year and the overflow line $350.00 including HST per year. | starting from | Overflow work moves to gondaliyacpa.ca at $350.00 including HST per year. | Sharad Gondaliya approves every fee change | All 15 live on October 9, 2026 |
| F9 | Guides and pillars | /guides/<guide>/ | pillar | Visible update date and a 12-row on-page contents block | Editorial calendar record, refreshed on the fixed pillar schedule | 30 | 30 | 30 | 30 | No pillar publishes without a visible update date and a 12-row on-page contents block. | CRA endorsed | Gondaliya CPA Professional Corporation is a registered EFILE electronic filer. | Sharad Gondaliya reviews, Navneet publishes | 10 on October 9 and 20 on October 30, 2026 |
| F10 | How-to-start and first-filing | /start/<slug>/ | start-single | First-year rule box: year-end date, 53-week test, Schedule 24 flag | Corporations Canada incorporation date field plus TaxCycle first-return checklist | 25 | 25 | 25 | 25 | No first-filing page publishes without the Schedule 24 line and the 53-week line. | instant filing | The first tax year cannot exceed 53 weeks and the year-end must match CRA's record or the transmission is rejected. | Sharad Gondaliya reviews | All 25 live on October 23, 2026 |
| F11 | Reviews hub and by city | /reviews/ and /reviews/<city>/ | review-page | Verified review count and review text for that place | Trustindex collection feed, place tagged at collection time | 11 | 11 | 11 | 11 | No review page publishes until five verified reviews exist for that place. | 1300+ reviews | Review counts are stated once, identically, on both sites. | Sharad Gondaliya signs off the claim-consistency audit | Trustindex rich snippets stay off, self-serving review schema earns no stars |
| F12 | Case studies | /case-studies/<slug>/ | case-study | Year count, province, entity type, outcome, elapsed business days | TaxDome matter record, de-identified export | 15 | 15 | 15 | 15 | No case study publishes without year count, province, entity type and outcome, all de-identified. | guaranteed outcome | No client name, corporation name or Business Number appears on any case study. | Sharad Gondaliya reviews every case study | All 15 live on November 13, 2026 |
| F13 | Blog posts | /blog/<slug>/ | post | One original table or one original checklist per post | Python pipeline writes the table from the TaxCycle mapping or the registry pull | 100 | 230 | 360 | 455 | No blog post publishes without one original table or one original checklist. | no penalty | Every penalty reference carries the full qualification sentence. | Sharad Gondaliya spot-checks 10 per month, Navneet publishes | 10 every Friday from October 16, 2026: 60 by November 20, 2026, the 395 mirror mark passed on July 16, 2027 and 455 reached on August 27, 2027 |
| F14 | Deadline and date pages | /deadlines/<slug>/ | deadline | Computed due date for that year-end month in Eastern Time | Server-side date module, Ontario statutory holiday table maintained by Navneet | 23 | 23 | 23 | 23 | No deadline page publishes without a computed date and the business-day rule sentence. | file late with no consequence | Business days are Monday to Friday, Ontario statutory holidays excluded. | Sharad Gondaliya checks dates and reviews | All 23 live on October 16, 2026 |
| F15 | Trust, legal and utility | /<slug>/ | trust-page | CPA Ontario numbers, address, hours, named CPA | Firm register record, one post-meta source shared with gondaliyacpa.ca | 24 | 24 | 24 | 24 | No trust page publishes without the CPA Ontario numbers and the firm address. | CRA agent | CPA Ontario Membership 61040184, Firm Registration 61330051, Vandana Goel CPA Ontario 61158584. | Sharad Gondaliya reviews all 24, Navneet publishes | EFILE number and CRA GroupID never appear on any page, in any schema block, in any sitemap or in any email |
| F16 | Hub and index pages | /<hub>/ | hub | Live child count for that family | WordPress query count, cached hourly by LiteSpeed Cache | 5 | 5 | 5 | 5 | No hub publishes without a live child count and links to every child family. | complete list of every accountant | Child counts update automatically and are never hand-typed. | Navneet builds and publishes | All 5 live on October 9, 2026 |
| Home | Home page | / | home | Seven-step flow block | Front-end flow definition, single source | 1 | 1 | 1 | 1 | The home page publishes with the full seven-step flow in fixed order and the full fee line. | book a call | Name, auto-fill, years, no-activity confirmation, attestation and identity check, payment, T183CORP signature. | Sharad Gondaliya approves before launch | No meetings, no scheduling, no booking widget, no Calendly |
| Total | 16 families plus home | — | — | — | — | 1,068 | 1,198 | 1,328 | 1,423 | — | — | — | — | September 20, 2027 column is 1,422 family URLs plus 1 home page; 968 structural URLs live from November 13, 2026 |

## 6(d) Keyword map

Family 1, industry and entity verticals: nil t2 filing for holding company, dormant holding company tax return, inactive consulting corporation t2, nil t2 for numbered company, shelf corporation tax return canada, nil t2 for real estate holding corporation, inactive trucking corporation t2 filing, closed restaurant corporation tax return, dormant it consulting corporation t2, nil t2 for medicine professional corporation, inactive law professional corporation t2, nil t2 for dentistry professional corporation, dormant construction corporation t2 return, nil t2 for e-commerce corporation

Family 2, calculators and checkers: t2 short eligibility checker, nil t2 deadline calculator, gifi schedule requirement checker, schedule 50 shareholder checker, schedule 24 first return checker, unfiled years cost calculator, corporate fiscal year end calculator, 53 week first tax year checker, nil return eligibility quiz, dormant corporation test, t2 due date calculator, ontario annual return due date calculator, federal annual return anniversary calculator, gst hst nil filing checker

Family 3, city hubs: nil t2 filing toronto, nil t2 filing mississauga, nil t2 filing brampton, nil t2 filing scarborough, nil t2 filing etobicoke, nil t2 filing north york, nil t2 filing markham, nil t2 filing vaughan, nil t2 filing richmond hill, nil t2 filing oakville, nil t2 filing ottawa, nil t2 filing hamilton

Family 4, service and place matrix: nil t2 filing ontario, catch up nil t2 filing ontario, dormant corporation filing alberta, final t2 before dissolution ontario, t2 short filing british columbia, nil t2 filing cost in toronto, unfiled corporate tax returns ontario, no activity corporation tax return quebec, numbered corporation nil filing ontario, inactive holding corporation t2 filing alberta, nil t2 filing deadline ontario, nil t2 filing for non resident owned corporations ontario, nil t2 filing manitoba, nil t2 filing nova scotia

Family 5, question pages: does an inactive corporation have to file a t2, do i have to file a t2 if my company had no activity, what happens if i never filed my corporate tax return, can i file a nil t2 myself, how many years of unfiled t2 can i file at once, what is a nil t2 return, is a t2 short the same as a nil return, do i need gifi for a nil return, who can sign a t183corp, can i e sign a t183corp, what is the penalty for filing a nil t2 late, does a dormant corporation need an ontario annual return, do i still file gst hst if my corporation is inactive, how long does cra take to confirm a t2

Family 6, best and route listicles: how to choose a nil t2 filing service canada, best online t2 filing for dormant companies, nil t2 filing options compared canada, best way to catch up unfiled corporate returns, best t2 software for a nil return, best cpa for dormant corporation filing, how quickly can a nil t2 be filed, how to choose a nil t2 filing service ontario, online corporate tax filing services compared canada, best way to close an inactive corporation, best order to file six unfiled t2 years, best nil t2 filing for non resident owners

Family 7, comparison pages: nil t2 filing vs t2 short, corpnilfilingfor300 vs bluepeak, corpnilfilingfor300 vs turbotax business, corpnilfilingfor300 vs t2inc, corpnilfilingfor300 vs taxdeep, corpnilfilingfor300 vs h and r block, corpnilfilingfor300 vs cloudtax, diy t2 software vs cpa filed nil t2, nil t2 vs loss t2, paper t2 vs efile t2, nil t2 vs final t2, accountant vs online nil t2 filing

Family 8, cost and pricing: nil t2 filing cost, how much does a nil t2 return cost, dormant company tax return cost canada, catch up corporate tax filing cost, t2 filing fee canada, nil corporate tax return price, cost to file six unfiled t2 years, low cost nil t2 filing, flat fee t2 filing canada, corporate tax return cost for inactive company

Family 9, guides and pillars: nil t2 return guide, how to file a nil t2 return, t2 short return guide, t183corp guide, dormant corporation guide canada, unfiled corporate tax returns guide, final t2 and dissolution guide, gifi schedules 100 125 141 guide, schedule 8 and loss continuity guide, provincial corporate returns at1 co 17 guide

Family 10, how-to-start and first-filing: first t2 return after incorporation, first corporate tax return canada, new corporation tax filing steps, what to file in the first year of a corporation, schedule 24 first return, first fiscal year end choice, 53 week first tax year, first t2 for a numbered company, first t2 for a federal corporation, first t2 for an ontario corporation

Family 11, reviews hub and by city: corpnilfilingfor300 reviews, gondaliya cpa reviews, nil t2 filing service reviews, online t2 filing reviews canada, nil t2 filing reviews toronto, nil t2 filing reviews mississauga, nil t2 filing reviews ottawa, nil t2 filing reviews hamilton

Family 12, case studies: unfiled corporate tax returns case study, six unfiled nil years caught up, dormant corporation cleared for dissolution, non resident owned corporation nil filing case, numbered corporation catch up filing, demand to file response case, arbitrary assessment reversed nil return, clearance certificate blocked by unfiled t2

Family 13, blog posts: dormant company tax return canada, what is a nil corporate tax return, cra demand to file letter, arbitrary assessment corporation, clearance certificate corporation canada, ontario business registry annual return, corporations canada annual return 12 dollars, alberta at1 return, quebec co 17 return, rc145 close account, nil gst hst return, nil payroll remittance, shareholder loan on a nil return, share capital on a nil return, efile mandatory 2024 corporations, 1000 dollar paper t2 penalty

Family 14, deadline and date pages: t2 filing deadline, t2 due date six months after year end, december 31 year end t2 due date, june 30 year end t2 due date, final t2 due date after dissolution, t2 filing deadline ontario, efile january 31 cutover, ontario annual return deadline, federal annual return 60 days, corporate tax deadline calendar 2026, nil t2 filing deadline, t2 deadline on a statutory holiday

Family 15, trust, legal and utility: t183corp signing, authorized signing officer t183corp, secure e signature cra forms, cpa ontario firm registration, is my data safe with an online cpa, refund policy online tax filing, identity verification tax filing, accessibility statement aoda, sitemap nil t2 filing, complaints process cpa ontario

Family 16, hub and index pages: nil t2 filing services, corporate tax tools canada, nil t2 filing locations, nil t2 guides, nil t2 blog, nil t2 filing hub

Total keywords listed: 182.

| Family | Head term | Monthly searches | Intent | Target URL | Conversion path | Notes |
|---|---|---|---|---|---|---|
| F1 | nil t2 filing for holding company | 70 | Commercial | /nil-t2-filing-for-numbered-holding-corporations/ | Vertical page to /tools/nil-return-eligibility-quiz/ to / | Estimate; qualification that investment income is not nil sits above the fold |
| F2 | t2 short eligibility checker | 110 | Informational | /tools/t2-short-eligibility-checker/ | Tool result to /guides/t2-short-eligibility/ to / | Estimate; primary link-earning asset |
| F3 | nil t2 filing toronto | 140 | Commercial | /toronto/ | City hub to /nil-t2-filing-toronto/ to / | Estimate; largest single city term |
| F4 | nil t2 filing ontario | 320 | Transactional | /nil-t2-filing-ontario/ | Service-place page direct to / | Estimate; highest-value non-brand term |
| F5 | does an inactive corporation have to file a t2 | 480 | Informational | /answers/does-an-inactive-corporation-have-to-file-a-t2/ | Answer to /guides/nil-t2-return-complete-guide/ to / | Estimate; top AI Overviews candidate |
| F6 | how to choose a nil t2 filing service canada | 90 | Commercial | /best/nil-t2-filing-services-in-canada/ | Listicle to /pricing/ to / | Estimate; published prices only |
| F7 | nil t2 filing vs t2 short | 60 | Commercial | /compare/nil-t2-filing-vs-t2-short-filing/ | Comparison to /tools/t2-short-eligibility-checker/ to / | Estimate; concept comparison outranks brand comparisons |
| F8 | nil t2 filing cost | 390 | Transactional | /pricing/nil-t2-filing-cost/ | Pricing direct to / | Estimate; second-highest converting term |
| F9 | nil t2 return | 1,900 | Informational | /guides/nil-t2-return-complete-guide/ | Pillar to /pricing/nil-t2-filing-cost/ to / | Estimate; head term of the whole site |
| F10 | first t2 return after incorporation | 260 | Informational | /start/first-t2-return-after-incorporation/ | Start page to /tools/schedule-24-first-return-checker/ to / | Estimate; 199,800 first T2 filers in 2023, 87,990 in Ontario |
| F11 | corpnilfilingfor300 reviews | 20 | Navigational | /reviews/ | Reviews to / | Estimate; brand term, grows with brand mentions |
| F12 | unfiled corporate tax returns canada | 210 | Commercial | /case-studies/six-unfiled-nil-years-numbered-ontario-corporation/ | Case study to /guides/catch-up-unfiled-corporate-tax-returns/ to / | Estimate; highest revenue per visit, multi-year orders |
| F13 | dormant company tax return canada | 170 | Informational | /blog/dormant-company-tax-return-canada/ | Post to /guides/dormant-and-inactive-corporations/ to / | Estimate; blog head term |
| F14 | t2 filing deadline | 2,400 | Informational | /deadlines/ | Deadlines hub to /tools/nil-t2-deadline-calculator/ to / | Estimate; largest volume term on the site, lowest intent |
| F15 | t183corp | 590 | Informational | /t183corp-signing-explained/ | Trust page to /security/ to / | Estimate; never written as T183 |
| F16 | nil t2 filing services | 180 | Commercial | /services/ | Hub to /nil-t2-filing-ontario/ to / | Estimate; hub captures unqualified service demand |

Assumptions behind every traffic figure that uses these terms: 90 average monthly searches per ranked URL and an 18% average click-through rate, both estimates, both carried unchanged from the roadmap forecast.

## 6(e) Free tools that earn links, drawn from Family 2

| Tool name | URL | Input the visitor gives | Output the tool returns | Link hook | Outreach target | Owner | Notes |
|---|---|---|---|---|---|---|---|
| Nil T2 deadline calculator | /tools/nil-t2-deadline-calculator/ | Fiscal year-end date | Due date, business days remaining, Ontario statutory holidays applied | A single date answer that no competitor publishes for free | Small-business bookkeeping blogs, startup incorporation sites | Navneet builds, Sharad Gondaliya checks | Highest link potential of the 150 tools |
| T2 Short eligibility checker | /tools/t2-short-eligibility-checker/ | 8 yes-or-no answers | Eligible or not eligible, with the failing condition named | Encodes all 8 T2 Short conditions in one screen | Accounting forums, CPA study groups | Navneet builds, Sharad Gondaliya reviews | Conditions: CCPC, nil net income or loss, one permanent establishment, no taxable dividends paid or received, Canadian currency, no refundable credits, no Ontario transitional debit, no section 34.2 amount |
| GIFI schedule requirement checker | /tools/gifi-schedule-requirement-checker/ | Share capital, cash, shareholder loan, incorporation cost, bank charge, all yes or no | Schedules 100, 125 and 141 required or omitted | Answers the single most misunderstood nil-return question | Bookkeeper associations, QuickBooks and Xero communities | Navneet builds, Sharad Gondaliya reviews | Any one yes makes the three GIFI schedules required |
| Unfiled years cost calculator | /tools/unfiled-years-cost-calculator/ | Number of unfiled tax years | Total fee at $300.00 including HST per tax year | Turns a vague worry into one number | Debt and business-recovery sites | Navneet builds, Sharad Gondaliya approves the fee line | 6 unfiled years returns $1,800.00 including HST |
| Schedule 50 shareholder threshold checker | /tools/schedule-50-shareholder-threshold-checker/ | Shareholder percentages | Schedule 50 required or not required per shareholder | 10% threshold stated plainly | Corporate lawyers, paralegal blogs | Navneet builds, Sharad Gondaliya checks | Schedule 50 is needed for any shareholder at 10% or more |
| 53-week first tax year checker | /tools/53-week-first-tax-year-checker/ | Incorporation date and proposed year-end | Valid or invalid first tax year | Prevents a rejected transmission | Incorporation services, opencorporationfor35.ca | Navneet builds, Sharad Gondaliya reviews | The first tax year cannot exceed 53 weeks |
| Schedule 24 first return checker | /tools/schedule-24-first-return-checker/ | Is this the first return after incorporation | Schedule 24 required or not required | Ties to 199,800 first-year filers | Startup accelerators, business registries | Navneet builds | Schedule 24 is needed on the first return after incorporation |
| Federal annual return anniversary calculator | /tools/federal-annual-return-anniversary-calculator/ | Federal incorporation date | Annual return due date, 60 days after anniversary | Separates a $12.00 corporate filing from the T2 | Federal incorporation blogs | Navneet builds | The federal annual return is filed with Corporations Canada, not with the T2 |
| Ontario annual return due date calculator | /tools/ontario-annual-return-due-date-calculator/ | Ontario incorporation date | Ontario Business Registry annual return due date | Corrects the most common Ontario error | Ontario small-business media | Navneet builds, Sharad Gondaliya reviews | Filed through the Ontario Business Registry since October 2021, not with the T2 |
| Dormant corporation test | /tools/dormant-corporation-test/ | 10 activity questions | Nil or not nil, with the disqualifying item named | Routes non-nil work to gondaliyacpa.ca at $350.00 including HST per year | General business media | Navneet builds, Sharad Gondaliya reviews | Feeds /not-a-nil-return/ when the answer is not nil |
| GST/HST nil filing checker | /tools/gst-hst-nil-filing-checker/ | Open GST/HST account yes or no | Nil filing still required, or RC145 closure route | Covers the account people forget | Bookkeeping software communities | Navneet builds | Open GST/HST or payroll accounts still need nil filings or an RC145 closure |
| Corporate fiscal year end calculator | /tools/corporate-fiscal-year-end-calculator/ | Incorporation date | Permitted year-end dates and the T2 due date for each | Useful to every new corporation in Canada | Incorporation services, law firm blogs | Navneet builds, Sharad Gondaliya checks | Year-end must match CRA's record or the transmission is rejected |

## 6(f) Technical SEO checklist

Rank Math SEO PRO sitemap split by post type. One sitemap file per post type, 200 links per file.

| Post type | Sitemap file | URLs at September 20, 2027 | Sitemap files | Priority | Change frequency | Notes |
|---|---|---|---|---|---|---|
| page | page-sitemap.xml | 45 | 1 | 0.9 | monthly | F8 15, F15 24, F16 5, home 1 |
| vertical | vertical-sitemap.xml | 215 | 2 | 0.7 | monthly | F1 |
| tool | tool-sitemap.xml | 150 | 1 | 0.8 | monthly | F2 |
| city | city-sitemap.xml | 15 | 1 | 0.9 | weekly | F3, data value refreshed monthly |
| service-place | service-place-sitemap.xml | 336 | 2 | 0.9 | monthly | F4 |
| answer | answer-sitemap.xml | 45 | 1 | 0.7 | monthly | F5 |
| listicle | listicle-sitemap.xml | 38 | 1 | 0.6 | monthly | F6, prices re-dated monthly |
| comparison | comparison-sitemap.xml | 20 | 1 | 0.7 | monthly | F7, prices re-dated monthly |
| guide | guide-sitemap.xml | 30 | 1 | 1.0 | weekly | F9, visible update date drives change frequency |
| start | start-sitemap.xml | 25 | 1 | 0.7 | monthly | F10 |
| review | review-sitemap.xml | 11 | 1 | 0.5 | weekly | F11 |
| case-study | case-study-sitemap.xml | 15 | 1 | 0.6 | monthly | F12 |
| post | post-sitemap.xml | 455 | 3 | 0.6 | monthly | F13 |
| deadline | deadline-sitemap.xml | 23 | 1 | 0.8 | weekly | F14, dates recomputed nightly |
| Total | sitemap_index.xml | 1,423 | 18 | — | — | 18 sitemap files plus 1 index file |

Copy-paste technical checklist, run in this order before each Friday batch in the dated build table publishes.

- [ ] Rank Math sitemap: confirm 18 sitemap files plus sitemap_index.xml at https://corpnilfilingfor300.ca/sitemap_index.xml
- [ ] Rank Math: exclude noindex URLs from every sitemap file
- [ ] Rank Math: confirm /thank-you/, /payment-failed/, /signing-link-expired/ are noindex, follow and absent from every sitemap
- [ ] Rank Math: confirm no sitemap file, no schema block and no page contains the EFILE number or the CRA GroupID
- [ ] robots.txt: allow all, disallow /wp-admin/ except /wp-admin/admin-ajax.php, disallow /?s=, disallow /sign/ token URLs, list sitemap_index.xml
- [ ] HTML sitemap at /sitemap/: all 1,423 links grouped under 16 family headings plus the home link, index and follow, excluded from the body link cap, excluded from Link Whisper
- [ ] Canonical: every URL self-canonical unless 6(k) names a different target
- [ ] Pagination: no paginated archives on money families; /blog/ archives use rel next and rel prev and are noindex from page 2
- [ ] Parameter handling: strip utm parameters from canonical, block ?orderby= and ?filter= in robots.txt
- [ ] 404s: custom 404 links /services/, /tools/, /locations/, /guides/, /blog/
- [ ] Redirects: zero redirect chains, maximum 1 hop, Rank Math redirection module audited monthly
- [ ] LiteSpeed Cache: page cache on, object cache on, CSS and JS minify on, critical CSS generated for the 14 templates
- [ ] Imagify: every image WebP, every image under 120 KB, width and height attributes present
- [ ] Core Web Vitals: Largest Contentful Paint under 2.5 seconds on the 14 templates, Interaction to Next Paint under 200 milliseconds, Cumulative Layout Shift under 0.10
- [ ] Mobile: single column below 768 pixels, tap targets 48 pixels, no horizontal scroll
- [ ] HTTPS on every URL, HSTS on, mixed content zero
- [ ] Schema: Organization, WebSite, BreadcrumbList site-wide, Service on F4 and F8, Article with dateModified on F9 and F13, Person on the two CPA pages
- [ ] Schema: no FAQPage, no HowTo, no Review, no AggregateRating anywhere
- [ ] Trustindex: rich snippet output switched off on every widget
- [ ] Site Kit by Google: Search Console and Analytics verified, sitemap submitted
- [ ] Indexation: compare Search Console indexed count against the month target in the table below
- [ ] WCAG 2.1 AA: contrast 4.5 to 1 on body text and 3 to 1 on large text, visible focus outline on every interactive element, full keyboard operation of the seven-step flow, form labels programmatically linked, error messages in text and not colour alone, alt text on every image, one H1 per page, heading order never skips a level, language attribute lang="en-CA"
- [ ] AODA: /accessibility/ published with the firm name, the Toronto address, the phone number 647-212-9559 and the email info@gondaliyacpa.ca, and a 5-business-day response commitment
- [ ] AODA: accessible-format request route stated in text on /accessibility/ and linked from the footer on all 1,423 URLs
Crawl budget for 1,423 URLs.

| Metric | December 20, 2026 | March 20, 2027 | June 20, 2027 | September 20, 2027 | Notes |
|---|---|---|---|---|---|
| URLs live | 1,068 | 1,198 | 1,328 | 1,423 | From the dated build table: 968 structural URLs from November 13, 2026 plus 10 blog posts every Friday |
| Target crawl requests per day | 60 | 100 | 120 | 140 | Estimate |
| Days to one full crawl | 18 | 12 | 12 | 11 | Estimate, URLs live divided by crawl requests per day, rounded up |
| Maximum acceptable average response time in milliseconds | 400 | 400 | 400 | 400 | LiteSpeed Cache target |
| Non-indexable URLs allowed in the crawl | 3 | 3 | 3 | 3 | /thank-you/, /payment-failed/, /signing-link-expired/ |
| Internal links pointing at a redirect | 0 | 0 | 0 | 0 | Hard rule |
| Orphan URLs allowed | 0 | 0 | 0 | 0 | Hard rule |

Indexation monitoring targets, checked in Search Console on the first business day of each month. URLs live follow the dated build table; the indexed targets apply once Sharad Gondaliya closes the launch gates and the noindex is lifted.

| Month ending | URLs live | Indexed URL target | Indexation rate target % | Notes |
|---|---|---|---|---|
| October 20, 2026 | 203 | 173 | 85.0 | Estimate |
| November 20, 2026 | 1,028 | 874 | 85.0 | Estimate |
| December 20, 2026 | 1,068 | 908 | 85.0 | Estimate |
| January 20, 2027 | 1,108 | 942 | 85.0 | Estimate |
| February 20, 2027 | 1,158 | 984 | 85.0 | Estimate |
| March 20, 2027 | 1,198 | 1,018 | 85.0 | Estimate |
| April 20, 2027 | 1,238 | 1,052 | 85.0 | Estimate |
| May 20, 2027 | 1,278 | 1,086 | 85.0 | Estimate |
| June 20, 2027 | 1,328 | 1,129 | 85.0 | Estimate |
| July 20, 2027 | 1,368 | 1,163 | 85.0 | Estimate |
| August 20, 2027 | 1,418 | 1,205 | 85.0 | Estimate |
| September 20, 2027 | 1,423 | 1,210 | 85.0 | Estimate |

Escalation rule: any family whose indexation rate falls below 70.0% for two consecutive months stops publishing new URLs in that family that month, and the existing URLs in that family are rewritten against the scaled-content safety line in 6(c) before publishing resumes. The March 2026 spam and core updates hit template city pages with no unique per-page data, and this rule exists to stop that pattern forming.

Copy-paste site-wide schema block for the home page.

{

"@context": "https://schema.org",

"@type": "AccountingService",

"@id": "https://corpnilfilingfor300.ca/#organization",

"name": "corpnilfilingfor300.ca",

"legalName": "Gondaliya CPA Professional Corporation",

"url": "https://corpnilfilingfor300.ca/",

"telephone": "+1-647-212-9559",

"email": "info@gondaliyacpa.ca",

"address": {

"@type": "PostalAddress",

"streetAddress": "55 Queen St E, Suite 1205",

"addressLocality": "Toronto",

"addressRegion": "ON",

"postalCode": "M5C 1R6",

"addressCountry": "CA"

},

"openingHoursSpecification": [{

"@type": "OpeningHoursSpecification",

"dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],

"opens": "09:00",

"closes": "20:30"

}],

"areaServed": ["Ontario","Quebec","British Columbia","Alberta","Manitoba","Saskatchewan","Nova Scotia","New Brunswick","Newfoundland and Labrador","Prince Edward Island","Yukon","Northwest Territories","Nunavut"],

"parentOrganization": {

"@type": "AccountingService",

"name": "Gondaliya CPA Professional Corporation",

"url": "https://gondaliyacpa.ca/"

},

"sameAs": ["https://gondaliyacpa.ca/","https://opencorporationfor35.ca/"]

}

Copy-paste service schema block for every Family 4 URL.

{

"@context": "https://schema.org",

"@type": "Service",

"name": "Nil T2 Filing in Ontario",

"serviceType": "Nil corporate income tax return preparation and electronic filing",

"provider": { "@id": "https://corpnilfilingfor300.ca/#organization" },

"areaServed": { "@type": "AdministrativeArea", "name": "Ontario" },

"url": "https://corpnilfilingfor300.ca/nil-t2-filing-ontario/",

"offers": {

"@type": "Offer",

"priceSpecification": {

"@type": "PriceSpecification",

"price": "300.00",

"priceCurrency": "CAD",

"valueAddedTaxIncluded": true

},

"availability": "https://schema.org/InStock",

"url": "https://corpnilfilingfor300.ca/nil-t2-filing-ontario/"

}

}

Copy-paste article schema block for every Family 9 and Family 13 URL.

{

"@context": "https://schema.org",

"@type": "Article",

"headline": "The Complete Guide to the Nil T2 Return",

"url": "https://corpnilfilingfor300.ca/guides/nil-t2-return-complete-guide/",

"datePublished": "2026-10-01",

"dateModified": "2026-10-01",

"author": {

"@type": "Person",

"name": "Sharad Gondaliya, CPA",

"url": "https://corpnilfilingfor300.ca/sharad-gondaliya-cpa/"

},

"publisher": { "@id": "https://corpnilfilingfor300.ca/#organization" },

"inLanguage": "en-CA"

}

## 6(g) Internal linking rules

| Family | Minimum inbound internal links | Maximum body outbound internal links | Mandatory link targets | Anchor rule | Orphan check cadence | Owner | Notes |
|---|---|---|---|---|---|---|---|
| F1 | 4 | 25 | /guides/dormant-and-inactive-corporations/, /pricing/nil-t2-filing-cost/, / | Exact vertical name, never the bare brand | Weekly | Navneet | Inbound from 3 blog posts plus 1 pillar |
| F2 | 3 | 20 | Matching guide, /pricing/nil-t2-filing-cost/ | Tool name as written in the H1 | Weekly | Navneet | Tools also linked from the relevant answer pages |
| F3 | 6 | 40 | /locations/, the 12 Family 4 URLs for that place, / | City name plus service, never city name alone | Weekly | Navneet | City hub is a distribution node |
| F4 | 5 | 25 | Parent city hub or jurisdiction pillar, /pricing/nil-t2-filing-cost/, / | Full service plus place phrase | Weekly | Navneet | 336 URLs, the largest orphan risk |
| F5 | 3 | 15 | Parent pillar, one tool | Question text, shortened to 6 words | Weekly | Navneet | Short pages, low outbound cap |
| F6 | 3 | 30 | /pricing/, /compare/nil-t2-filing-vs-t2-short-filing/ | Listicle title | Monthly | Navneet | External links to competitors are nofollow |
| F7 | 3 | 20 | /pricing/nil-t2-filing-cost/, / | Comparison title | Monthly | Navneet | External competitor links nofollow |
| F8 | 10 | 25 | /, /nil-t2-filing-ontario/ | Price phrase with the amount | Weekly | Navneet | Highest inbound requirement on the site |
| F9 | 12 | 40 | 30 hand-picked cluster children, / | Descriptive, never the bare URL | Weekly | Navneet | Pillars carry the highest outbound cap |
| F10 | 3 | 25 | /start/first-t2-return-after-incorporation/, opencorporationfor35.ca home | First-filing phrase | Weekly | Navneet | One cross-domain link per page |
| F11 | 3 | 15 | /, /pricing/ | Place plus the word reviews | Monthly | Navneet | No review schema, plain HTML output |
| F12 | 3 | 20 | /guides/catch-up-unfiled-corporate-tax-returns/, / | Outcome phrase | Monthly | Navneet | Case studies feed the catch-up pillar |
| F13 | 2 | 20 | One pillar, one tool | Topic phrase, never the brand | Weekly | Navneet | 455 URLs, checked in weekly batches of 45 |
| F14 | 4 | 20 | /deadlines/, /tools/nil-t2-deadline-calculator/ | Month plus year-end phrase | Weekly | Navneet | Dates recomputed nightly, links static |
| F15 | 5 | 15 | /, /about/ | Page title | Monthly | Navneet | Footer links count toward inbound |
| F16 | 20 | 400 | Every child family | Child title | Weekly | Navneet | Hubs are exempt from the 40-link body cap |
| Home | 30 | 60 | /services/, /tools/, /locations/, /guides/, /blog/, /pricing/nil-t2-filing-cost/ | Service phrase | Weekly | Navneet | Home never links to a competitor |

Link Whisper settings, applied once and locked.

- [ ] Automatic linking: off for F4, F8, F15 and the home page; on for F1, F5, F13
- [ ] Maximum automatic links added per post: 5
- [ ] Maximum automatic links pointing at one target URL: 40 site-wide
- [ ] Sentences already containing a link: skipped
- [ ] Self-links: blocked
- [ ] Link to the same target twice in one page: blocked
- [ ] Keyword-to-URL map: imported from the Python pipeline, one row per target URL, refreshed with each Friday batch
- [ ] Reserved anchors: the exact phrases nil t2 filing cost, t183corp, t2 short, catch up unfiled corporate tax returns map to one URL each and to no other
- [ ] Banned anchors: click here, read more, this page, learn more
- [ ] Reports: Link Whisper orphan report run every Monday; any URL at 0 inbound links receives 3 contextual links within 5 business days
- [ ] Footer and navigation links do not count toward the minimum inbound requirement for F1, F4, F13
- [ ] The HTML sitemap at /sitemap/ is excluded from Link Whisper and from every link cap
Orphan prevention at publish time: the Python pipeline refuses to publish any URL whose payload does not already contain the minimum inbound link count for its family. The refusal message is written to the batch log and the URL is held to the next batch.

## 6(h) AEO plan for AI Overviews and AI Mode

AI Overviews and AI Mode favour fresh pages with visible update dates and cite brand mentions more than backlinks. Three levers: visible update dates, brand mentions, entity consistency.

Visible update dates.

| Family | Visible date label | Position on page | Refresh cadence | What must change for the date to move | Owner | Notes |
|---|---|---|---|---|---|---|
| F9 | Updated September 20, 2026 | Under the H1, above the contents block | Monthly | At least one factual sentence or one table row | Navneet | dateModified in schema always equals the visible date |
| F14 | Dates recalculated September 20, 2026 | Under the H1 | Nightly | The computed due date | Navneet | Recalculation alone is a real change |
| F13 | Updated September 20, 2026 | Under the byline | Quarterly | One table row or one checklist item | Navneet | 455 posts rotate on a 3-month cycle, 152 posts per month |
| F7 | Prices checked September 20, 2026 | Above the comparison table | Monthly | Any competitor published price | Navneet | BluePeak $100.00, TurboTax $175.00, T2inc $199.00 and $299.00, TaxDeep $200.00, H&R Block $449.00, CloudTax pay-what-you-want |
| F6 | Prices checked September 20, 2026 | Above the first entry | Monthly | Any competitor published price | Navneet | Same price set as F7 |
| F3 | Local data pulled September 20, 2026 | Under the data value | Monthly | The registry count for that place | Navneet | Caption carries the pull date |
| F4 | Local data pulled September 20, 2026 | Under the place data row | Monthly | The registry count for that place | Navneet | 336 URLs updated in one pipeline run |
| F1, F2, F5, F8, F10, F11, F12, F15, F16 | Updated September 20, 2026 | Footer of the article body | Half-yearly | One factual sentence | Navneet | No date is moved without a content change |

A date is never moved without a content change. A template that stamps today's date on unchanged content is the exact pattern the March 2026 spam update targeted.

Answer-block rules for every page that can be quoted.

- First paragraph answers the H1 question in 40 to 60 words, with no preamble and no brand name.
- The first sentence states the answer. The second sentence states the rule. The third sentence states the exception.
- One H2 per question, written as the question.
- One table per page that holds the numbers, because tables are extracted whole.
- No FAQPage markup and no HowTo markup. FAQ rich results ended May 7, 2026 and HowTo earns nothing. The question format stays, the markup goes.
- Every claim on the page is provable, because Rule 217 bars unsubstantiated advertising and an unprovable claim is the one an AI system repeats.
Copy-paste answer block, reusable pattern, shown filled for /answers/does-an-inactive-corporation-have-to-file-a-t2/.

"Yes. Every resident corporation, including an inactive one, must file a T2 return within six months of its fiscal year-end, every year, until it is formally dissolved. A final T2 is due within six months of dissolution. Having no revenue, no bank activity and no employees does not remove the obligation."

Copy-paste qualification sentence, required wherever a penalty is mentioned on any of the 1,423 URLs.

"A true nil return carries no percentage late-filing penalty, because that penalty is a percentage of tax owing and the corporation owes $0.00. The unfiled year still stays open forever, invites a demand to file and an arbitrary assessment, blocks a clearance certificate and dissolution, and costs a non-resident-owned corporation $25.00 per day up to $2,500.00."

Copy-paste EFILE sentence, the only permitted phrasing, for /about/, /security/ and every Family 9 pillar.

"Gondaliya CPA Professional Corporation is a registered EFILE electronic filer. Returns are prepared and transmitted in Canada. Credentials are never shared and never used offshore."

Entity consistency, audited before launch and on the first business day of every month.

| Entity attribute | Value published on corpnilfilingfor300.ca | Must match gondaliyacpa.ca | Must match opencorporationfor35.ca | Where it appears | Owner | Notes |
|---|---|---|---|---|---|---|
| Legal name | Gondaliya CPA Professional Corporation | Yes | Yes | Footer, /about/, Organization schema | Sharad Gondaliya | Registrar approval of the firm name is required before launch |
| Department name | corpnilfilingfor300.ca, a department of Gondaliya CPA Professional Corporation | Yes | Yes | Footer, /about/ | Sharad Gondaliya | Stated the same way on all three sites |
| Address | 55 Queen St E, Suite 1205, Toronto, ON M5C 1R6 | Yes | Yes | Footer on all 1,423 URLs, Organization schema | Sharad Gondaliya | One office, one address, no variants |
| Phone | 647-212-9559 | Yes | Yes | Footer, /contact/, schema | Sharad Gondaliya | One number, no tracking substitutes |
| Email | info@gondaliyacpa.ca | Yes | Yes | Footer, /contact/, schema | Sharad Gondaliya | Same mailbox across all three sites |
| Hours | 9:00 AM to 8:30 PM, Monday to Sunday | Yes | Yes | Footer, /contact/, schema, Google Business Profile | Sharad Gondaliya | Identical string everywhere |
| CPA Ontario Membership | 61040184 | Yes | Not published | /cpa-ontario-registration/, /sharad-gondaliya-cpa/ | Sharad Gondaliya | Membership number of the practising member |
| Firm Registration | 61330051 | Yes | Not published | /cpa-ontario-registration/ | Sharad Gondaliya | Firm registration number |
| Second CPA | Vandana Goel, CPA Ontario 61158584 | Yes | Not published | /vandana-goel-cpa/, /our-cpas/ | Sharad Gondaliya | Named reviewer on the site |
| US licences | Not published | Yes | Not published | gondaliyacpa.ca only | Sharad Gondaliya | WA 57629 and MT PAC-CPAP-LIC-033176 are not relevant to a Canadian T2 service |
| Review count | Not published until reconciled | Yes | Yes | /reviews/ | Sharad Gondaliya | gondaliyacpa.ca currently shows 500+ in one place and 1300+ in another |
| Years in practice | Not published until reconciled | Yes | Yes | /about/ | Sharad Gondaliya | gondaliyacpa.ca currently shows 10, 15+ and 20+ |
| Client count | Not published until reconciled | Yes | Yes | /about/ | Sharad Gondaliya | gondaliyacpa.ca currently shows 600+ on one page |
| Price | $300.00 including HST per tax year | Yes, as the department price | Yes, as the department price | Every money page | Sharad Gondaliya | Overflow $350.00 including HST per year |

Rule: corpnilfilingfor300.ca publishes no review count, no years-in-practice figure and no client count until a single number for each is agreed and published identically on gondaliyacpa.ca and on opencorporationfor35.ca. Contradictory figures across sites break entity consistency for AI systems and breach Rule 217 at the same time. The claim-consistency audit is signed by Sharad and dated before the home page goes live.

Brand mention plan, because AI Mode cites brand mentions more than backlinks.

| Mention channel | Monthly target mentions | Anchor or plain mention | Asset used | Owner | Notes |
|---|---|---|---|---|---|
| Accounting and bookkeeping community threads | 8 | Plain mention | /tools/t2-short-eligibility-checker/ | Navneet | Estimate |
| Small-business media commentary | 3 | Plain mention | Corporations Canada open-data analysis | Navneet | Estimate |
| LinkedIn firm posts and reposts | 12 | Plain mention | Monthly deadline table | Navneet | Estimate, distributed through Blog2Social |
| Incorporation partner sites | 2 | Linked mention | /start/first-t2-return-after-incorporation/ | Navneet | Estimate |
| Directory and association listings | 2 | Linked mention | /about/ | Navneet | Estimate |
| Podcast and webinar appearances | 1 | Plain mention | Nil filing obligation explainer | Navneet | Estimate |

## 6(i) Backlink and digital PR plan

| Month ending | New referring domain target | Primary asset offered | Outreach volume | Owner | Notes |
|---|---|---|---|---|---|
| October 20, 2026 | 2 | /about/ and /cpa-ontario-registration/ | 20 | Navneet | Estimate; foundational listings only |
| November 20, 2026 | 3 | /tools/nil-t2-deadline-calculator/ | 40 | Navneet | Estimate; all 150 calculators live by October 30, 2026 |
| December 20, 2026 | 5 | /tools/t2-short-eligibility-checker/ | 60 | Navneet | Estimate |
| January 20, 2027 | 6 | /tools/gifi-schedule-requirement-checker/ | 80 | Navneet | Estimate |
| February 20, 2027 | 7 | Corporations Canada open-data analysis of dormant corporation counts | 100 | Navneet | Estimate |
| March 20, 2027 | 8 | /tools/unfiled-years-cost-calculator/ | 100 | Navneet | Estimate |
| April 20, 2027 | 9 | Provincial nil-filing comparison table across 13 jurisdictions | 120 | Navneet | Estimate |
| May 20, 2027 | 10 | /guides/catch-up-unfiled-corporate-tax-returns/ | 120 | Navneet | Estimate |
| June 20, 2027 | 11 | /case-studies/six-unfiled-nil-years-numbered-ontario-corporation/ | 140 | Navneet | Estimate |
| July 20, 2027 | 12 | First T2 filer analysis, 199,800 filers in 2023 and 87,990 in Ontario | 140 | Navneet | Estimate |
| August 20, 2027 | 13 | /tools/ontario-annual-return-due-date-calculator/ | 160 | Navneet | Estimate |
| September 20, 2027 | 14 | Full-year dormant corporation data set, downloadable | 160 | Navneet | Estimate |
| Total | 100 | 12 assets | 1,240 | — | Estimate; 100 new referring domains in year one |

Link asset rules.

- Every outreach asset is a Family 2 tool or an original data table. No guest post is offered without one of the twelve tools attached.
- Competitor comparison pages are never used in outreach, because competitor comparisons state published prices and features only with no negative claim, and outreach invites a negative framing.
- No paid links, no link exchanges, no private blog networks, no directory bundles.
- Outbound links to competitors on F6 and F7 carry rel="nofollow".
- Cross-domain links from gondaliyacpa.ca and opencorporationfor35.ca are placed once per relevant page, in body text, with a descriptive anchor, and are counted separately from the 100 referring domain target.
- Every claim in every pitch is provable and identical to what is published on the site.
- No pitch mentions CRA endorsement, CRA approval, CRA partnership or CRA agency. The only permitted phrase is registered EFILE electronic filer.
Unlinked mention recovery: a monthly scan for the strings corpnilfilingfor300, Gondaliya CPA and Sharad Gondaliya, with a copy-paste request to add a link where the mention is already positive. Target 4 recovered links per month from month 6, estimate.

## 6(j) Google Business Profile handling

One office at 55 Queen St E, Suite 1205, Toronto, ON M5C 1R6 cannot support 15 city Google Business Profiles. A Google Business Profile requires a staffed location at the address it claims. There is one such location. Creating 14 further profiles for Mississauga, Brampton, Scarborough, Etobicoke, North York, Markham, Vaughan, Richmond Hill, Oakville, Ottawa, Oshawa, Guelph, Hamilton and Windsor would mean claiming addresses the firm does not occupy. That is not done. No virtual offices are rented, no mailbox addresses are claimed, no home addresses are listed, and no second profile is created for corpnilfilingfor300.ca at the same address as Gondaliya CPA Professional Corporation, because two profiles at one address for one business is a duplicate listing.

What is done instead.

| Action | Detail | Frequency | Owner | Notes |
|---|---|---|---|---|
| One verified profile | Gondaliya CPA Professional Corporation, 55 Queen St E, Suite 1205, Toronto, ON M5C 1R6, 647-212-9559 | Once, then maintained | Sharad Gondaliya | Profile name matches the Registrar-approved firm name |
| Primary category | Certified Public Accountant | Once | Navneet | One primary category, no keyword stuffing in the name field |
| Service areas on the one profile | 15 city terms listed as service areas | Reviewed quarterly | Navneet | Service areas do not create separate profiles and do not rank as separate listings |
| Services list | Nil T2 filing $300.00 including HST per tax year, catch-up nil filing $300.00 including HST per tax year, final T2 before dissolution $300.00 including HST per tax year | Reviewed monthly | Navneet | Prices identical to /pricing/ |
| Hours | 9:00 AM to 8:30 PM, Monday to Sunday | Reviewed monthly | Navneet | Identical to the footer string and the Organization schema |
| Website field | https://corpnilfilingfor300.ca/ with a UTM campaign parameter | Once | Navneet | UTM stripped from the canonical |
| Google Posts | 4 per month, each linking one Family 14 deadline page or one Family 2 tool | Weekly | Navneet | Posts are the only city-level signal available from one profile |
| Questions and answers | 12 seeded questions answered by Sharad in his own name | Once, then monitored weekly | Sharad Gondaliya | Answers match the site copy word for word |
| Reviews | Requested by email after CRA confirmation, collected through Trustindex, displayed on /reviews/ | Continuous | Navneet | No review schema, no star markup, self-serving review schema earns no stars |
| City coverage on the site | 15 city hubs and 180 city service pages carry the local ranking work instead of profiles | Continuous | Navneet | Local pack coverage outside Toronto is not pursued; organic coverage is |

Stated plainly for the record: outside Toronto, this site competes in organic results, not in the local pack. The 15 city hubs and the 180 city service pages are the entire local strategy for the other 14 cities. No Google Business Profile is created for any of them.

## 6(k) Canonical and cannibalisation rules across the three sites

| corpnilfilingfor300.ca URL | gondaliyacpa.ca URL | opencorporationfor35.ca URL | Overlap risk | Rule | Canonical target | Action | Owner |
|---|---|---|---|---|---|---|---|
| /nil-t2-filing-ontario/ | /corporate-tax-filing-ontario/ | None | High | Price and scope differ, so both stay and both are self-canonical | https://corpnilfilingfor300.ca/nil-t2-filing-ontario/ | Rewrite the gondaliyacpa.ca page to lead on active corporations at $350.00 including HST per year and add one pointer link to the nil page | Navneet |
| /catch-up-nil-t2-filing-toronto/ | /catch-up-corporate-tax-filing-toronto/ | None | High | Nil catch-up and full catch-up are different services | https://corpnilfilingfor300.ca/catch-up-nil-t2-filing-toronto/ | Add the nil qualifier to every corpnil title and H1, add the active qualifier to every gondaliyacpa.ca title and H1 | Navneet |
| /pricing/nil-t2-filing-cost/ | /corporate-tax-filing-cost/ | /incorporation-cost/ | High | One fee table per site, no shared paragraphs | https://corpnilfilingfor300.ca/pricing/nil-t2-filing-cost/ | gondaliyacpa.ca states $350.00 including HST per year for overflow and links across once | Navneet |
| /start/first-t2-return-after-incorporation/ | /new-corporation-tax-setup/ | /after-you-incorporate/ | High | opencorporationfor35.ca owns pre-incorporation and incorporation intent; corpnilfilingfor300.ca owns post-incorporation nil filing | https://corpnilfilingfor300.ca/start/first-t2-return-after-incorporation/ | opencorporationfor35.ca ends its page with one link to the corpnil start page and stops there | Navneet |
| /guides/nil-t2-return-complete-guide/ | /t2-corporate-tax-return-guide/ | None | High | Nil guide and full guide are separate documents with zero shared paragraphs | https://corpnilfilingfor300.ca/guides/nil-t2-return-complete-guide/ | Run a body similarity check; at 60% or above, rewrite the gondaliyacpa.ca guide or 301 it to the corpnil guide | Navneet |
| /t183corp-signing-explained/ | /t183corp-signing/ | None | High | One canonical explanation of T183CORP across the group | https://corpnilfilingfor300.ca/t183corp-signing-explained/ | 301 the gondaliyacpa.ca page to the corpnil page | Navneet |
| /about/ | /about/ | /about/ | Medium | Firm facts identical, page purpose different | Each site self-canonical | Publish identical firm facts, different service paragraphs, on all three | Navneet |
| /reviews/ | /reviews/ | /reviews/ | Medium | One review count across the group | Each site self-canonical | No count published anywhere until the claim-consistency audit is signed | Navneet |
| /deadlines/ | /tax-deadlines/ | None | Medium | Corporate deadlines only on corpnil, personal and corporate on gondaliyacpa.ca | https://corpnilfilingfor300.ca/deadlines/ | gondaliyacpa.ca removes corporate T2 deadline pages and links across once | Navneet |
| /tools/nil-t2-deadline-calculator/ | /tools/tax-deadline-calculator/ | None | Medium | One calculator per function across the group | https://corpnilfilingfor300.ca/tools/nil-t2-deadline-calculator/ | 301 the gondaliyacpa.ca corporate calculator, keep the personal calculator | Navneet |
| /nil-t2-filing-for-non-resident-owned-corporations-ontario/ | /non-resident-tax-returns-filing-toronto/ | None | High | Non-resident corporate nil filing against non-resident personal and corporate filing | https://corpnilfilingfor300.ca/nil-t2-filing-for-non-resident-owned-corporations-ontario/ | gondaliyacpa.ca page restricted to personal non-resident returns | Navneet |
| /toronto/ | /toronto/ | /toronto/ | High | Three Toronto pages for one office | Each site self-canonical | Each Toronto page states a different service and a different price, with one reciprocal link each | Navneet |
| /blog/dormant-company-tax-return-canada/ | /blog/dormant-company-tax-return/ | None | High | Duplicate blog topics across two domains | https://corpnilfilingfor300.ca/blog/dormant-company-tax-return-canada/ | 301 the gondaliyacpa.ca post and keep one post per topic in the group | Navneet |
| /services/ | /services/ | /services/ | Low | Hub pages, different children | Each site self-canonical | No action | Navneet |

Cross-domain rule, stated once: no cross-domain canonical tag is used between corpnilfilingfor300.ca, gondaliyacpa.ca and opencorporationfor35.ca. A cross-domain canonical would hand the ranking to the other domain and remove the $300.00 page from results. Where two pages in the group are near-duplicates, one is rewritten or one is 301 redirected. The similarity threshold is 60% of body text; at or above it, the older page is rewritten or redirected within 10 business days.

Per-pattern collision list for the 336 Family 4 URLs against the four existing gondaliyacpa.ca city services.

| corpnilfilingfor300.ca pattern | Colliding gondaliyacpa.ca pattern | Places affected | Colliding URL count | Collision type | Rule | Canonical target | Action | Notes |
|---|---|---|---|---|---|---|---|---|
| /nil-t2-filing-<place>/ | corporate-tax-filing-<city> | 15 cities | 15 | Head-term overlap on corporate tax filing plus city | Nil qualifier is mandatory in the corpnil title, H1 and first sentence | corpnil URL | Rewrite the gondaliyacpa.ca city page to active corporations at $350.00 including HST per year | 13 jurisdiction URLs in this pattern have no collision |
| /catch-up-nil-t2-filing-<place>/ | catch-up-corporate-tax-filing-<city> | 15 cities | 15 | Direct intent overlap | Nil catch-up on corpnil, catch-up with activity on gondaliyacpa.ca | corpnil URL | Add the phrase with no activity to the corpnil H1 and with revenue to the gondaliyacpa.ca H1 | 13 jurisdiction URLs have no collision |
| /nil-t2-filing-cost-in-<place>/ | corporate-tax-filing-cost-in-<city> | 15 cities | 15 | Price-term overlap | One price per page, no ranges | corpnil URL | corpnil states $300.00 including HST per tax year, gondaliyacpa.ca states $350.00 including HST per year | 13 jurisdiction URLs have no collision |
| /unfiled-corporate-tax-returns-<place>/ | catch-up-corporate-tax-filing-<city> | 15 cities | 15 | Partial overlap on unfiled and catch-up | corpnil owns the word unfiled, gondaliyacpa.ca owns the phrase catch-up with activity | corpnil URL | Remove the word unfiled from all gondaliyacpa.ca city titles and H1s | 13 jurisdiction URLs have no collision |
| /nil-t2-filing-for-non-resident-owned-corporations-<place>/ | non-resident-tax-returns-filing-<city> | 15 cities | 15 | Overlap on non-resident | corpnil owns non-resident corporate nil filing, gondaliyacpa.ca owns non-resident personal filing | corpnil URL | Restrict the gondaliyacpa.ca page to individuals and add the $25.00 per day up to $2,500.00 qualification on the corpnil page | 13 jurisdiction URLs have no collision |
| /dormant-corporation-filing-<place>/ | None | 28 places | 0 | No collision | Self-canonical | corpnil URL | No action | 15 cities plus 13 jurisdictions |
| /final-t2-before-dissolution-<place>/ | None | 28 places | 0 | No collision | Self-canonical | corpnil URL | No action | Final T2 is due within six months of dissolution |
| /t2-short-filing-<place>/ | None | 28 places | 0 | No collision | Self-canonical | corpnil URL | No action | Page carries all 8 T2 Short conditions |
| /no-activity-corporation-tax-return-<place>/ | None | 28 places | 0 | No collision | Self-canonical | corpnil URL | Internal risk only, against /nil-t2-filing-<place>/ | Distinct H1 and distinct first 120 words required |
| /numbered-corporation-nil-filing-<place>/ | None | 28 places | 0 | No collision | Self-canonical | corpnil URL | No action | Numbered-company angle only |
| /inactive-holding-corporation-t2-filing-<place>/ | None | 28 places | 0 | No collision | Self-canonical | corpnil URL | Carries the qualification that a holding corporation with investment income is not nil | Highest misqualification risk of the 12 patterns |
| /nil-t2-filing-deadline-<place>/ | None | 28 places | 0 | No collision | Self-canonical, and internal deduplication against Family 14 | corpnil URL | Family 14 owns year-end months, Family 4 owns place-level deadline pages | Distinct H1 required |
| Total | 4 gondaliyacpa.ca patterns | — | 75 | — | — | — | — | 75 colliding URLs, 261 clean URLs, 336 total |

Internal cannibalisation rule inside Family 4: the 12 service slugs for one place are permitted only where each carries a different H1, a different first 120 words, and a different primary keyword from the keyword map. A place whose 12 pages cannot be written to that standard drops to the 6 patterns with no collision, and the missing pages are replaced one for one by jurisdiction pages from the 13 jurisdiction terms, keeping Family 4 at 336 and the grand total at 1,423.

Family 3 unique-local-data test.

The test: a city hub publishes only where there is a named, repeatable, machine-readable source that returns a different value for that place, refreshable every month, with no manual writing. A city that cannot produce one is not published as a hub, because template city pages with no unique per-page data are what the March 2026 spam and core updates removed.

| City term | Test result | Named repeatable source | Data value published | Refresh | Notes |
|---|---|---|---|---|---|
| toronto | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Toronto | Count of active federal corporations with a Toronto registered office | Monthly | Also cross-checked against the Ontario Business Registry address-city filter |
| mississauga | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Mississauga | Count of active federal corporations with a Mississauga registered office | Monthly | Distinct municipality in the registry city field |
| brampton | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Brampton | Count of active federal corporations with a Brampton registered office | Monthly | Distinct municipality |
| scarborough | Fail | No distinct value; the registry city field records Toronto | None available | Not applicable | Amalgamated into the City of Toronto, no separate registry value |
| etobicoke | Fail | No distinct value; the registry city field records Toronto | None available | Not applicable | Amalgamated into the City of Toronto, no separate registry value |
| north-york | Fail | No distinct value; the registry city field records Toronto | None available | Not applicable | Amalgamated into the City of Toronto, no separate registry value |
| markham | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Markham | Count of active federal corporations with a Markham registered office | Monthly | Distinct municipality |
| vaughan | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Vaughan | Count of active federal corporations with a Vaughan registered office | Monthly | Distinct municipality |
| richmond-hill | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Richmond Hill | Count of active federal corporations with a Richmond Hill registered office | Monthly | Distinct municipality |
| oakville | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Oakville | Count of active federal corporations with an Oakville registered office | Monthly | Distinct municipality |
| ottawa | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Ottawa | Count of active federal corporations with an Ottawa registered office | Monthly | Distinct municipality |
| oshawa | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Oshawa | Count of active federal corporations with an Oshawa registered office | Monthly | Distinct municipality |
| guelph | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Guelph | Count of active federal corporations with a Guelph registered office | Monthly | Distinct municipality |
| hamilton | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Hamilton | Count of active federal corporations with a Hamilton registered office | Monthly | Distinct municipality |
| windsor | Pass | Corporations Canada open-data bulk file, registered-office city field equal to Windsor | Count of active federal corporations with a Windsor registered office | Monthly | Distinct municipality |

Result: 12 of the 15 city terms pass. 3 fail: scarborough, etobicoke, north-york.

Substitution rule that keeps the grand total fixed. Family 3 stays at exactly 15 URLs. The 3 failing city hubs are not published at /scarborough/, /etobicoke/ and /north-york/. They are replaced one for one, in the same batch on Friday, October 23, 2026, by 3 jurisdiction hubs at /ontario/, /alberta/ and /british-columbia/, each of which passes the test on a named repeatable source: the CRA T2 assessment count for that province, 1,108,730 for Ontario, 365,890 for Alberta and 413,630 for British Columbia, refreshed when the annual table is reissued, plus the Corporations Canada open-data bulk file filtered by province, refreshed monthly. Family 3 remains 15, Family 4 remains 336, the site total remains 1,422 plus 1 home page = 1,423, and every count in the December 20, 2026, March 20, 2027, June 20, 2027 and September 20, 2027 columns in 6(c) is unchanged.

The three district names are not lost. Scarborough, Etobicoke and North York become named, anchored sections on /toronto/, each with its own postal forward sortation area list and its own two-paragraph fact pattern, addressed at /toronto/#scarborough, /toronto/#etobicoke and /toronto/#north-york. No separate URL, no separate canonical, no separate title tag. The 36 Family 4 pages that use those three place tokens are retained, because their unique field is the 12-row service data set and the district forward sortation area list, which differs per district.

Family 9 year-stamp rule.

- No Family 9 URL contains a year. /guides/nil-t2-return-complete-guide/ is correct. A guide URL with 2026 or 2027 in the slug is never created.
- The year token lives in three places only: the title tag, the first H2 where the content is year-specific, and the visible update line.
- Title tag pattern, refreshed in place and never duplicated to a new URL: "Nil T2 Return | Complete Guide for Canadian Corporations". Where a year is needed for freshness, the title becomes "Nil T2 Return | Complete Guide for Canadian Corporations (2026)" and the same URL is edited again to (2027) at the rollover. A second URL is never created.
- Visible update line, directly under the H1: "Updated September 20, 2026".
- The schema dateModified always equals the visible update line to the day. A mismatch is a publish-blocking error in the Python pipeline.
- Rollover schedule: all 30 Family 9 guides are reviewed and re-stamped in the first 10 business days of January each year, and at least one factual sentence or one table row changes on each guide before the date moves.
- Year-specific facts carry their own qualification in text: for tax years starting after 2023 e-filing is mandatory for virtually all corporations, and a paper T2 draws a $1,000.00 penalty plus a $100.00 per-return preparer penalty.
- No guide is retired at a year rollover, no guide is redirected at a year rollover, and no annual archive of guides is created. One URL per guide topic, forever.

# Section 7. Content engine: 10 posts per week

## 7.1 Workstreams

| Workstream | Weekly output | Tool | Gate owned | Owner | KPI | Notes |
|---|---|---|---|---|---|---|
| Factual and compliance review | 10 posts reviewed, 1 programmatic batch sampled | TaxCycle, WordPress preview, banned-phrases table in 7.4 | Gate one, factual and compliance | Sharad Gondaliya | 0 banned phrases published per week | Gate one consumes 5.0 hours per week; Sharad Gondaliya is also the EFILE credential holder and return reviewer at launch |
| SEO and publishing | 10 posts published, 1 programmatic batch published | WordPress, Astra Pro, Elementor Pro, Rank Math SEO PRO, LiteSpeed Cache, Imagify | Gate two, SEO and publishing | Navneet | 10 of 10 posts live by Friday 8:30 PM Eastern Time | Sole account with WordPress Editor capability on corpnilfilingfor300.ca |
| Publishing pipeline, post meta and schema validation | 1 pipeline release | Python, WordPress MCP connector, Custom Post Type UI, WPCode Lite | Post meta and schema validation | Navneet | 0 failed bulk publishes per week | No ACF; every custom field is a Custom Post Type UI post type, a taxonomy, or native post meta written by the Python pipeline and rendered by an Elementor dynamic tag |
| Briefs and cluster map | 10 briefs approved, 1 cluster map update | Rank Math SEO PRO, Keyword.com, Site Kit by Google, Link Whisper | Brief approval | Navneet | 213 ranked URLs at September 20, 2027 | Target taken from the roadmap forecast block C month 12 |
| Keyword sets and unique data tables | 10 keyword sets, 10 unique data tables | Keyword.com, Site Kit by Google | Unique-data check | Navneet | 1 unique data table per post | The March 2026 spam and core updates hit template city pages with no unique per-page data; this workstream exists to stop that |
| Drafting | 10 drafts | ChatGPT drafting brief in 7.6, Microsoft Word | Draft completeness | Navneet | 10 of 10 drafts delivered Tuesday | The 4 hardest compliance topics each week are drafted first |
| Line edit and fact check | 10 posts edited | Microsoft Word, banned-phrases table in 7.4 | Pre-gate-one clean copy | Navneet | 0 banned phrases reaching gate one | Every failed catch at gate one is logged against this workstream |
| Links, schema and distribution | 10 posts linked, 10 posts scheduled, 1 programmatic batch linked | Link Whisper, Rank Math SEO PRO, Blog2Social, Short.io, Easy Table of Contents | Link and schema | Navneet | 6 internal links per post | Also carries the Blog2Social rules in 7.7 |
| Total | 10 posts per week | — | — | — | 455 posts | 455 is the Family 13 target; 10 posts every Friday from October 16, 2026 reaches 60 by November 20, 2026 and 455 on August 27, 2027 |

## 7.2 Weekly cadence table

The cadence runs every week from Monday, October 5, 2026: the programmatic batch staged that week publishes on Friday, October 9, 2026, and the first 10 blog posts publish on Friday, October 16, 2026. Ontario Thanksgiving, Monday, October 12, 2026, carries no deliverable, so that week's Monday work runs on Tuesday, October 13, 2026.

| Weekday | Activity | Owner | Volume | Output | Notes |
|---|---|---|---|---|---|
| Monday | Keyword sets and unique data tables built for next week | Navneet | 10 | 10 keyword sets, 10 data tables | Each data table carries a figure that appears on no other URL |
| Monday | Briefs written and approved from the keyword sets | Navneet | 10 | 10 approved briefs | Brief approval is a hard gate before drafting starts |
| Monday | Programmatic batch built and staged for that Friday's count in the dated build table | Navneet | 1 | 1 staged batch | Batch size follows the Dated build schedule section; the last batch publishes on Friday, November 13, 2026 |
| Tuesday | Drafting from the ChatGPT drafting brief in 7.6 | Navneet | 10 | 10 drafts | The 4 hardest compliance topics are drafted first |
| Wednesday | Line edit, number check, banned-phrase sweep | Navneet | 10 | 10 edited drafts | Sweep runs the full banned-phrases table in 7.4 |
| Thursday | Gate one, factual and compliance review | Sharad Gondaliya | 10 | 10 approved or returned drafts | Returned drafts go back to Navneet the same day |
| Friday | Gate two, SEO and publishing | Navneet | 10 | 10 live posts | Live by 8:30 PM Eastern Time |
| Friday | Programmatic batch published from the staged build | Navneet | 1 | 1 published batch | Rank Math SEO PRO index status checked on 10 sampled URLs |
| Saturday | Internal links, schema, table of contents, image compression | Navneet | 10 | 10 linked posts, 60 internal links | 6 internal links per post |
| Saturday | Social scheduling for the coming 7 days | Navneet | 10 | 40 scheduled social posts | 4 networks per post under the Blog2Social rules in 7.7 |
| Sunday | Refresh queue worked from the table in 7.8 | Navneet | 5 | 5 refreshed URLs | Refreshed URLs get a new last-reviewed stamp only when a number or body sentence changed |
| Sunday | Weekly report on URLs published, ranked URLs and organic visits | Navneet | 1 | 1 report | Compared against the dated build schedule |

## 7.3 Two-gate QA

Gate one, factual and compliance review. Owner: Sharad Gondaliya. Copy-paste checklist:

GATE ONE - FACTUAL AND COMPLIANCE - corpnilfilingfor300.ca

URL slug: ____________________  Draft title: ____________________

Reviewer: Sharad Gondaliya, CPA. Date: ____________  Time (HH:MM:SS Eastern): ____________

[ ] 1. Every CRA reference uses the phrase "registered EFILE electronic filer" and nothing else.

[ ] 2. No instance of "authorized", "agent", "approved", "partner" or "endorsed" about CRA.

[ ] 3. No CRA mark, CRA logo or Canada wordmark in text, image or alt text.

[ ] 4. "Authorized signing officer" appears only on or about T183CORP.

[ ] 5. Every instance is written T183CORP. No instance of T183 on its own.

[ ] 6. Every filing-deadline statement says six months after fiscal year-end, every year, until formal dissolution.

[ ] 7. A final T2 is described as due within six months of dissolution wherever dissolution is mentioned.

[ ] 8. E-filing is described as mandatory for virtually all corporations for tax years starting after 2023.

[ ] 9. Paper penalties are stated as $1,000 plus a $100 per-return preparer penalty.

[ ] 10. T2 Short eligibility lists all eight conditions: CCPC, nil net income or a loss, one permanent

establishment, no taxable dividends paid or received, Canadian currency, no refundable credits,

no Ontario transitional debit, no section 34.2 amount.

[ ] 11. Any statement that GIFI Schedules 100, 125 and 141 may be omitted carries the qualification that

share capital, cash, a shareholder loan, an incorporation cost or a bank charge makes them required.

[ ] 12. Schedule 50 is tied to any shareholder at 10 percent or more.

[ ] 13. Schedule 24 is tied to the first return after incorporation.

[ ] 14. Schedule 8 and loss continuity are recorded.

[ ] 15. The first tax year is stated as no longer than 53 weeks.

[ ] 16. The year-end is stated as having to match CRA's record or the transmission is rejected.

[ ] 17. T183CORP is described as signed by an authorized signing officer BEFORE transmission.

[ ] 18. T183CORP is described as carrying a date and an HH:MM:SS timestamp that is never backdated.

[ ] 19. T183CORP e-signature is described as an access-controlled secure portal.

[ ] 20. T183CORP retention is stated as six years by the firm.

[ ] 21. T183CORP is stated as not sent to CRA unless requested.

[ ] 22. Representative authorization is described as optional and post-filing only.

[ ] 23. No EFILE number, no CRA GroupID, in body text, schema, sitemap, image or alt text.

[ ] 24. No claim that returns are prepared or transmitted outside Canada.

[ ] 25. Every "no penalty" statement carries the full qualification in row 8 of the banned-phrases table.

[ ] 26. Holding companies with investment income, rental corporations and dividend recipients are stated

as NOT nil wherever nil status is defined.

[ ] 27. Open GST/HST and payroll accounts are stated as still needing nil filings or an RC145 closure.

[ ] 28. The Ontario annual return is stated as filed through the Ontario Business Registry since

October 2021, not with the T2.

[ ] 29. The federal annual return is stated as $12 within 60 days of the anniversary.

[ ] 30. Alberta AT1 and Quebec CO-17 are stated as separate provincial returns.

[ ] 31. Every price is $300.00 including HST per tax year. Overflow is $350.00 including HST per year.

[ ] 32. Every claim on this page is provable and matches the identical claim on gondaliyacpa.ca.

[ ] 33. No meeting, no scheduling, no booking widget, no Calendly link, no email-chain instruction.

[ ] 34. Banned-phrases table in 7.4 run end to end with zero hits.

Result: [ ] APPROVED  [ ] RETURNED TO NAVNEET

Reviewer signature: ____________________

Gate two, SEO and publishing. Owner: Navneet. Copy-paste checklist:

GATE TWO - SEO AND PUBLISHING - corpnilfilingfor300.ca

URL slug: ____________________  Publisher: Navneet. Date: ____________

[ ] 1. Gate one marked APPROVED by the reviewing CPA. No exceptions, no conditional publishes.

[ ] 2. Slug is lowercase, hyphenated, final. No date in the slug. No stop words.

[ ] 3. Title tag is 60 characters or fewer and carries the exact-match query.

[ ] 4. Meta description is 155 characters or fewer, carries $300.00 including HST, and ends with a verb.

[ ] 5. One H1 only. H2 headings answer the query in the first 80 words.

[ ] 6. Article schema published through Rank Math SEO PRO. No FAQPage schema. No HowTo schema.

[ ] 7. No review schema and no Trustindex rich snippet markup on this URL.

[ ] 8. Visible "Last reviewed:" line renders under the H1 from post meta key _cnf_last_reviewed.

[ ] 9. schema dateModified equals the _cnf_last_reviewed value exactly.

[ ] 10. Byline renders a real named author and the reviewing CPA line from 7.5.

[ ] 11. 6 internal links placed by Link Whisper. 1 link to the checkout page. 1 link to the parent hub.

[ ] 12. Easy Table of Contents rendered on any post over 1,200 words.

[ ] 13. Every image compressed by Imagify. Every image has alt text with no CRA mark and no credential.

[ ] 14. LiteSpeed Cache purged for this URL and its parent hub.

[ ] 15. URL submitted in Site Kit by Google. Rank Math SEO PRO index status is Indexable.

[ ] 16. Blog2Social schedule created under the rules in 7.7.

[ ] 17. Post added to the refresh queue with the family code and the frequency from 7.8.

Result: [ ] PUBLISHED  [ ] HELD

## 7.4 Banned-phrases table

| Banned phrase | Reason | Approved replacement | Where checked | Notes |
|---|---|---|---|---|
| CRA authorized, CRA-authorized e-filer | CRA EFILE advertising rules permit one phrase only | registered EFILE electronic filer | Gate one item 1 | Also bans the hyphenated and title-case variants |
| CRA agent, agent of CRA | Not permitted about CRA | registered EFILE electronic filer | Gate one item 2 | Includes "acting for CRA" |
| CRA approved, approved by CRA | Not permitted about CRA | registered EFILE electronic filer | Gate one item 2 | Includes "CRA-approved software" |
| CRA partner, CRA endorsed, endorsed by CRA | Not permitted about CRA | Delete the sentence | Gate one item 2 | No substitute wording exists |
| CRA logo, CRA wordmark, Canada wordmark | CRA marks may not be used | Delete the asset | Gate one item 3 | Applies to image files, favicons and alt text |
| T183 | The form is T183CORP | T183CORP | Gate one item 5 | Search is case-insensitive and must not match inside T183CORP |
| Authorized signing officer, used away from T183CORP | Permitted and required on and about T183CORP only | Director, officer, owner | Gate one item 4 | Keep the phrase where T183CORP is the subject |
| No penalty, penalty free, zero penalty, standing alone | Rule 217 bars an unsubstantiated claim and the statement is incomplete | A true nil return has no percentage late-filing penalty because the penalty is a percentage of tax owing and the corporation owes $0. The unfiled year still stays open forever, invites a demand to file and an arbitrary assessment, blocks a clearance certificate and dissolution, and costs a non-resident corporation $25 per day up to $2,500. | Gate one item 25 | The full qualification is one block and is never split across sections |
| Guaranteed, guarantee, we guarantee | Rule 217 bars an unsubstantiated claim | Delete the sentence | Gate one item 34 | Includes "guaranteed acceptance" and "guaranteed filing" |
| Cheapest, lowest price in Canada, best price, unbeatable | Rule 217 bars an unsubstantiated claim and a negative competitor claim | $300.00 including HST per tax year | Gate one item 31 | Competitor comparisons state published prices and features only |
| Fastest, instant filing, same-day filing, filed in minutes | Unprovable against the actual process | CRA confirmation emailed within 3 business days | Gate one item 34 | 3 business days is Monday to Friday, Ontario statutory holidays excluded |
| Book a call, schedule a meeting, free consultation, contact us to start | The flow has no meeting step | Start now and enter your corporation name | Gate one item 33 | Calendly is owned but is not used on this site |
| Conservatively, easily, simply, just | Output rule | Delete the word | Gate one item 34 | Never used about a forecast |
| e.g., such as | Output rule | Write the actual slug | Gate one item 34 | Write /nil-t2-filing-toronto/ rather than an example marker |
| 500+ reviews, 1300+ reviews, 600+ clients, 10 years, 15+ years, 20+ years | gondaliyacpa.ca carries conflicting figures and Rule 217 requires one provable figure | One audited figure, identical on both sites | Gate one item 32 | The claim-consistency audit is a hard launch gate; until it closes, no count claim is published at all |
| Risk free, audit proof, CRA will never contact you | Unprovable | Delete the sentence | Gate one item 34 | Includes "we handle any CRA questions forever" |
| Backdate, we can date it earlier, we will sign it for you | The T183CORP timestamp is never backdated and the signing officer signs | The signing officer signs T183CORP before transmission and the timestamp is server-generated in Eastern Time | Gate one item 18 | Any draft containing this is returned and logged |
| Nil holding company with investment income, nil rental corporation, nil dividend recipient | These are not nil | These corporations are not nil and are handed to gondaliyacpa.ca at $350.00 including HST per year | Gate one item 26 | Applies wherever nil status is defined or implied |
| EFILE number, our EFILE number, GroupID | Confidential | Delete | Gate one item 23 | Never in body text, schema, sitemap or email |
| Offshore, overseas team, our team in | Credentials are never used offshore and returns are prepared and transmitted in Canada | Returns are prepared and transmitted in Canada | Gate one item 24 | Ties to the segregation rule in 7.5 |
| Emoji of any kind | Output rule | Delete | Gate two item 3 | Includes emoji in titles, meta descriptions and social copy |

## 7.5 Byline and last-reviewed rules

Byline rules.

1.	Every URL carries a byline naming a real person. No house byline, no "Admin", no "Editorial Team".

2.	Blog posts in Family 13 carry two lines, rendered under the H1: Written by <author full name> and Reviewed by Sharad Gondaliya, CPA (Ontario), CPA Ontario Membership 61040184.

3.	Every page that states a filing rule, a penalty figure, a schedule requirement or a T183CORP rule is bylined to the reviewing CPA directly: Written and reviewed by Sharad Gondaliya, CPA (Ontario), CPA Ontario Membership 61040184. Families 1, 8, 9, 10, 14 and 15 fall under this rule in full.

4.	The reviewer line always names the CPA who actually performed the review, with that CPA's membership number.

5.	Every bylined person has a live author archive at /author/<first-last>/ with a real biography, credentials and a photo. No author archive is noindexed.

6.	A contract or offshore author is never named as the reviewer, and is named as the author only after that author archive is live.

Last-reviewed rules.

1.	The visible line is Last reviewed: <Month D, YYYY> and renders under the H1 above the first paragraph on every URL.

2.	The date comes from native post meta key _cnf_last_reviewed, written by the Python pipeline and rendered with an Elementor dynamic tag. There is no ACF on this stack.

3.	schema dateModified is written from _cnf_last_reviewed and is always equal to it.

4.	The stamp advances only when a number, a figure, a rule statement or a body sentence changed. A link-only edit, an image swap or a cache purge never advances the stamp.

5.	The stamp is written server-side in Eastern Time. It is never set to a future date.

6.	AI Overviews and AI Mode favour fresh pages with visible update dates, so the stamp is a rendered on-page line and not a hidden schema value alone.

## 7.6 ChatGPT drafting brief, copy-paste ready

You are drafting one blog post for corpnilfilingfor300.ca, a department of Gondaliya CPA

Professional Corporation, a CPA Ontario firm in Toronto, Ontario.

THE OFFER, STATED EXACTLY THIS WAY EVERY TIME

A nil (no-activity) T2 corporate tax return, $300.00 including HST per tax year.

The flow, in this order, never reordered: the client types the corporation name only, the

database auto-fills the CRA Business Number and the incorporation date, the client picks the

unfiled years, confirms no activity, attests as authorized signing officer and passes an

identity check, pays by credit card, debit, Apple Pay or Google Pay, the return is prepared in

TaxCycle, Form T183CORP carrying that return's figures is generated, the client signs it on a

tokenised access-controlled screen, a CPA reviews it, the return is transmitted, and CRA

confirmation is emailed within 3 business days (Monday to Friday, Ontario statutory holidays

excluded). There are no meetings, no scheduling, no email chains and no booking widget.

Work that is not nil is handed to gondaliyacpa.ca at $350.00 including HST per year.

WRITING RULES

Plain writing. Short sentences. No emojis. No filler. No preamble. No closing note.

Canadian English and Canadian spelling.

Start with the answer in the first 40 words, then explain.

One H1. H2 headings that are the questions a reader actually types.

900 to 1,400 words.

Every sequential, numeric or comparative item goes in a Markdown pipe table with a header

separator row, an exact number in every cell, never a range, and a Notes column.

Mark any estimate with the word "estimate" in the Notes column.

Every fee includes HST. Every price is annual.

Never write "e.g." or "such as". Write the actual slug, for example write /nil-t2-filing-toronto/

as the literal text.

Never write "conservatively", "easily", "simply" or "just" about a forecast.

No sources. No citations. No external links.

BANNED PHRASES. If you write any of these, the draft is rejected.

"CRA authorized", "authorized by CRA", "CRA agent", "agent of CRA", "CRA approved",

"approved by CRA", "CRA partner", "CRA endorsed", "endorsed by CRA", any CRA logo, wordmark

or mark, "T183" on its own, "guaranteed", "guarantee", "cheapest", "lowest price in Canada",

"best price", "unbeatable", "fastest", "instant filing", "same-day filing", "filed in minutes",

"book a call", "schedule a meeting", "free consultation", "risk free", "audit proof",

"backdate", "conservatively", "easily", "simply", "just", "e.g.", "such as", any emoji,

any review count, any client count, any years-in-practice count.

THE ONLY PERMITTED CRA PHRASE

"registered EFILE electronic filer". Use it and nothing else when describing the firm's ability

to transmit. "Authorized signing officer" is permitted and required, but only on and about

Form T183CORP.

REQUIRED QUALIFICATIONS. Carry these verbatim whenever the topic touches them.

1. Every resident corporation, including an inactive one, must file a T2 within six months of

its fiscal year-end, every year, until it is formally dissolved. A final T2 is due within six

months of dissolution.

2. For tax years starting after 2023 e-filing is mandatory for virtually all corporations. A

paper T2 draws a $1,000 penalty plus a $100 per-return preparer penalty.

3. The T2 Short is available only to a CCPC with nil net income or a loss, one permanent

establishment, no taxable dividends paid or received, Canadian currency, no refundable

credits, no Ontario transitional debit and no section 34.2 amount.

4. A corporation inactive all year with nothing to report may omit GIFI Schedules 100, 125 and

141, but any share capital, cash, shareholder loan, incorporation cost or bank charge makes

them required.

5. Schedule 50 is needed for any shareholder at 10% or more. Schedule 24 is needed on the first

return after incorporation. Schedule 8 and loss continuity must be recorded.

6. The first tax year cannot exceed 53 weeks and the year-end must match CRA's record or the

transmission is rejected.

7. Form T183CORP must be signed by an authorized signing officer BEFORE transmission, must carry

a date and an HH:MM:SS timestamp that is never backdated, may be e-signed through an

access-controlled secure portal, is kept by the firm for six years, and is not sent to CRA

unless requested. Always write T183CORP, never T183.

8. An EFILE number plus a signed T183CORP are enough to transmit. Representative authorization

is optional and post-filing only.

9. Never name, number or hint at an EFILE number or a CRA GroupID.

10. Whenever you say a nil return carries no percentage late-filing penalty, you must complete

the statement in the same paragraph, in these words: a true nil return has no percentage

late-filing penalty because the penalty is a percentage of tax owing and the corporation

owes $0, but an unfiled year stays open forever, invites a demand to file and an arbitrary

assessment, blocks a clearance certificate and dissolution, and costs a non-resident

corporation $25 per day up to $2,500. Never write "no penalty" without that qualification.

11. The Ontario annual return is filed through the Ontario Business Registry since October 2021,

not with the T2.

12. Federal corporations file a separate $12 Corporations Canada annual return within 60 days of

their anniversary.

13. Alberta AT1 and Quebec CO-17 are separate provincial returns.

14. Returns are prepared and transmitted in Canada. Credentials are never shared and never used

offshore.

NIL-STATUS RULES. State these plainly wherever nil status is defined or implied.

A corporation is nil for this service only when it had no activity at all in the tax year.

These are NOT nil and must be sent to gondaliyacpa.ca at $350.00 including HST per year:

a holding company with investment income, a rental corporation, a corporation that received or

paid a dividend, a corporation with any revenue, any expense claimed, any payroll, any asset

purchase or any inter-company transaction.

An open GST/HST account or an open payroll account still needs nil filings, or a closure using

Form RC145. An inactive T2 does not close those accounts.

Share capital, cash, a shareholder loan, an incorporation cost or a bank charge means GIFI

Schedules 100, 125 and 141 are required even though the corporation had no activity.

CLOSING BLOCK. End every post with exactly this, no variation:

"Nil T2 filing is $300.00 including HST per tax year. Type your corporation name, pick your

unfiled years, pay, sign Form T183CORP on a secure screen, and your CRA confirmation is emailed

within 3 business days. Gondaliya CPA Professional Corporation is a registered EFILE electronic

filer. Firm Registration 61330051."

DELIVER

Title tag, 60 characters or fewer.

Meta description, 155 characters or fewer, containing $300.00 including HST.

Slug, lowercase and hyphenated.

H1.

Body with H2 headings.

One table with a Notes column.

The closing block above.

Nothing else.

TOPIC FOR THIS DRAFT: <paste the approved brief here>

UNIQUE DATA TABLE FOR THIS DRAFT: <paste the unique data table here>

## 7.7 Blog2Social posting rules

| Rule | Setting | Volume | Owner | Notes |
|---|---|---|---|---|
| Networks per post | LinkedIn company page, LinkedIn personal, X, Facebook page | 4 | Navneet | 4 networks times 10 posts equals 40 scheduled items per week |
| Schedule shape | 1 post at publication, 1 repost at day 8, 1 repost at day 30 | 3 per network | Navneet | 120 scheduled items per week across the 3 waves |
| Posting window | 9:00 AM to 8:30 PM Eastern Time, Monday to Sunday | 1 window | Navneet | Matches firm hours so a reply is answered the same day |
| Copy source | Hand-written per network. Never the auto-generated excerpt | 4 variants per post | Navneet | Identical copy across 4 networks reads as automation and is not published |
| Copy length | LinkedIn 600 characters, X 240 characters, Facebook 400 characters | 3 limits | Navneet | Exact ceilings, not targets |
| Link handling | Every link is a Short.io branded link with a UTM string | 1 per item | Navneet | UTM source is the network, medium is social, campaign is the family code |
| Banned content | The full banned-phrases table in 7.4 applies to social copy without exception | 0 permitted hits | Navneet | Social copy is swept at the Wednesday edit, not after scheduling |
| Price statement | Any post naming a price states $300.00 including HST per tax year | 1 form of words | Sharad Gondaliya | Overflow price $350.00 including HST per year is never posted socially |
| CRA statement | Any post naming the firm's filing ability says "registered EFILE electronic filer" | 1 form of words | Sharad Gondaliya | No CRA mark in any image or video thumbnail |
| Image rule | 1 image per post, compressed by Imagify, no CRA mark, no credential number visible | 1 | Navneet | Alt text mirrors the post H1 |
| Review schema interaction | Trustindex rich snippets stay off site-wide, and no social post claims a star rating | 0 | Navneet | Self-serving review schema earns no stars |
| Queue audit | Scheduled queue checked against the live URL list every Sunday | 1 audit | Navneet | A scheduled item pointing at an unpublished or 404 URL is deleted, not repaired |

## 7.8 First 40 post titles

What a Nil T2 Return Is and When a Corporation Must File One, Nil T2 Filing Deadline Six Months After Your Fiscal Year-End, Does an Inactive Corporation Still Have to File a T2, T2 Short Versus Full T2 Which One a Nil Corporation Can Use, Mandatory T2 E-Filing for Tax Years Starting After 2023, The Paper T2 Penalty and the Preparer Penalty Explained, Can a Nil T2 Be Late-Filed Without a Penalty, What Happens to a Corporation With Unfiled T2 Returns, Demand to File and Arbitrary Assessment What CRA Does Next, Why an Unfiled Year Blocks Your Clearance Certificate, The $25 a Day Non-Resident Penalty on an Unfiled Nil T2, Which GIFI Schedules a Nil T2 Can Omit, When Share Capital Makes GIFI Schedules Required, Schedule 50 and the 10% Shareholder Rule, Schedule 24 on Your First Corporate Tax Return, Schedule 8 and Loss Continuity on a Nil T2, Your First Tax Year Cannot Exceed 53 Weeks, Why a Wrong Year-End Gets Your T2 Transmission Rejected, Form T183CORP Who Signs It and When, Why T183CORP Must Carry a Date and an HH:MM:SS Timestamp, E-Signing T183CORP Through an Access-Controlled Secure Portal, How Long a Firm Keeps T183CORP and Why It Is Six Years, Is T183CORP Sent to CRA, Authorized Signing Officer What the Term Means on T183CORP, Representative Authorization Is Optional and Post-Filing Only, Holding Companies With Investment Income Are Not Nil, Rental Corporations Are Not Nil, Dividend Recipients Are Not Nil, Open GST/HST Accounts Still Need Nil Filings, Closing a GST/HST Account With Form RC145, Nil Payroll Accounts and Your Remittance Obligation, The Ontario Annual Return Moved to the Ontario Business Registry in October 2021, Federal Corporations and the $12 Annual Return Within 60 Days of Your Anniversary, Alberta AT1 Is a Separate Provincial Return, Quebec CO-17 Is a Separate Provincial Return, Dissolving a Corporation and the Final T2 Within Six Months, Catch-Up Filing Five Years of Nil T2 Returns in One Sitting, Numbered Corporations and Nil T2 Filing, How to Find Your Business Number and Incorporation Date, Nil T2 Filing Cost in Ontario and What $300 Including HST Covers

## 7.9 Refresh table

| Page family | Refresh trigger | Frequency in months | Owner | What changes | Last-reviewed stamp rule | Notes |
|---|---|---|---|---|---|---|
| F1 Industry and entity verticals | A change to nil-status wording or to a schedule requirement | 12 | Navneet | Nil-status block, schedule list, closing block | Stamp advances only when a rule sentence or a number changed | 215 URLs; refreshed in 12 monthly tranches |
| F2 Calculators and checkers | A change to a deadline rule, a penalty figure or the $300.00 price | 6 | Navneet | Calculation logic, on-screen result text, price line | Stamp advances on every logic change, never on a styling change | 150 URLs; logic lives in the Python pipeline, not in page HTML |
| F3 City hubs | A change to the 12 Family 4 service slugs or the city list | 6 | Navneet | Child link block, local data table, intro paragraph | Stamp advances when the child link block or the data table changed | 15 URLs; each hub links all 12 service slugs for its city |
| F4 Service and place matrix | A change to a service slug, a jurisdiction rule or the per-place data table | 6 | Navneet | Per-place data table, jurisdiction paragraph, internal links | Stamp advances only when the per-place data table changed | 336 URLs; the unique per-place data table is what keeps these out of the template-page pattern |
| F5 Question pages | A change to the answer of record at gate one | 6 | Sharad Gondaliya | The first 40 words, the qualification block | Stamp advances when the answer changed, never on a link edit | 45 URLs; each answers one query in the first 40 words |
| F6 Best and route listicles | A competitor published price change | 3 | Navneet | Price column, feature column, published date | Stamp advances on every price or feature change | 38 URLs; published prices and features only, no negative claim |
| F7 Comparison pages | A competitor published price change | 3 | Sharad Gondaliya | Price column, feature column, comparison table Notes | Stamp advances on every price or feature change | 20 URLs; Rule 217 requires every comparison claim to be provable |
| F8 Cost and pricing | A change to the $300.00 price or the $350.00 overflow price | 3 | Sharad Gondaliya | Price line, overflow line, inclusion list | Stamp advances on every price change without exception | 15 URLs; the price appears identically on both sites |
| F9 Guides and pillars | A change to any compliance fact in the gate one checklist | 6 | Sharad Gondaliya | Rule sections, schedule sections, table figures | Stamp advances when a rule or a figure changed | 30 URLs; these carry the CPA byline directly |
| F10 How-to-start and first-filing | A change to the first-return rules, Schedule 24 or the 53-week rule | 12 | Navneet | Step list, Schedule 24 block, 53-week block | Stamp advances when a step or a rule changed | 25 URLs; step order matches the fixed flow order exactly |
| F11 Reviews hub and by city | A new published review | 1 | Navneet | Review list, count figure | Stamp advances on every added review | 11 URLs; Trustindex rich snippets stay off, so no star markup is added |
| F12 Case studies | A new completed engagement approved for publication | 12 | Sharad Gondaliya | Outcome figures, year list, corporation description | Stamp advances when an outcome figure changed | 15 URLs; no client name, no Business Number, no T183CORP detail |
| F13 Blog posts | A change to a fact the post rests on, or the post falling out of the top 10 | 12 | Navneet | Body sections, data table, closing block | Stamp advances when a body sentence or a number changed | 455 URLs; 5 refreshed every Sunday under the weekly cadence |
| F14 Deadline and date pages | The calendar rolling, or an Ontario statutory holiday list change | 1 | Navneet | Date table, next-deadline figure, business-day count | Stamp advances every month because the dates change every month | 23 URLs; dates are computed by the Python pipeline into post meta, never typed |
| F15 Trust, legal and utility | A change to firm registration, membership numbers, address, hours or a policy | 12 | Sharad Gondaliya | Firm block, membership numbers, policy text | Stamp advances on every firm-detail change | 24 URLs; CPA Ontario Membership 61040184 and Firm Registration 61330051 appear here and nowhere else in the body of other families |
| F16 Hub and index pages | A new child URL published in the hub's family | 3 | Navneet | Child link block, count line | Stamp advances when the child link block changed | 5 URLs; the count line states the exact live child count |
| Home page | A change to the price, the flow order or the confirmation window | 1 | Sharad Gondaliya | Hero line, flow steps, price line, confirmation line | Stamp advances every month because the home page carries the freshest proof signal | 1 URL; AI Overviews and AI Mode favour fresh pages with visible update dates |

# Section 8. Publishing plan

## 8.1 Dated build, family by family

The per-family monthly publishing tables are replaced by the Dated build schedule section of this plan. This table reads that schedule family by family. Every structural family is complete on Friday, November 13, 2026, and the build closes on Friday, November 20, 2026.

| Family | URLs | Live on | Notes |
|---|---|---|---|
| F1 Industry and entity verticals | 215 | October 23, October 30 and November 6, 2026 | 60, 80 and 75 |
| F2 Calculators and checkers | 150 | October 16, October 23 and October 30, 2026 | 50 on each date |
| F3 City hubs | 15 | October 23, 2026 | 3 jurisdiction hubs substituted under the 6(k) test |
| F4 Service by place matrix | 336 | November 6 and November 13, 2026 | 150 and 186 |
| F5 Question pages | 45 | October 16, 2026 |  |
| F6 Best and route listicles | 38 | October 30, 2026 |  |
| F7 Comparison pages | 20 | October 16, 2026 |  |
| F8 Cost and pricing | 15 | October 9, 2026 |  |
| F9 Guides and pillars | 30 | October 9 and October 30, 2026 | 10 and 20 |
| F10 How-to-start and first-filing | 25 | October 23, 2026 |  |
| F11 Reviews hub and by city | 11 | November 6, 2026 |  |
| F12 Case studies | 15 | November 13, 2026 |  |
| F13 Blog posts | 455 | 10 every Friday from October 16, 2026 | 60 by November 20, 2026, 100 by December 20, 2026, 230 by March 20, 2027, 360 by June 20, 2027, 455 on August 27, 2027 |
| F14 Deadline and date pages | 23 | October 16, 2026 |  |
| F15 Trust, legal and utility | 24 | October 9, 2026 |  |
| F16 Hub and index pages | 5 | October 9, 2026 |  |
| Home page | 1 | October 9, 2026 |  |
| Total | 1,423 | 968 structural URLs by November 13, 2026; 1,423 by August 27, 2027 | 1,422 family URLs plus 1 home page |

# Section 12. SEO and website KPIs

SEO and website targets for December 20, 2026, March 20, 2027, June 20, 2027 and September 20, 2027. URL counts follow the dated build schedule.

| KPI | Definition | Target December 20, 2026 | Target March 20, 2027 | Target June 20, 2027 | Target September 20, 2027 | Source tool | Review cadence | Owner | Notes |
|---|---|---|---|---|---|---|---|---|---|
| URLs live | Cumulative published URLs on corpnilfilingfor300.ca | 1,068 | 1,198 | 1,328 | 1,423 | WordPress | Weekly | Navneet | Includes the 1 home page; 968 structural URLs live from November 13, 2026 plus 10 blog posts every Friday |
| New URLs published in month | URLs first published inside the month | 40 | 40 | 50 | 5 | WordPress | Weekly | Navneet | Blog posts only after November 13, 2026, 10 every Friday; the 455 target is reached on August 27, 2027 |
| Cumulative blog posts | Family 13 posts live | 100 | 230 | 360 | 455 | WordPress | Monthly | Navneet | Passes the 395 mirror mark on July 16, 2027 and reaches 455 on August 27, 2027 |
| Family 4 pages live | Service by place pages published | 336 | 336 | 336 | 336 | WordPress | Monthly | Navneet | 12 slugs by 15 city terms plus 12 slugs by 13 jurisdiction terms; all 336 live from November 13, 2026 |
| Ranked URLs | URLs in the Google top 10 | 5 | 45 | 123 | 213 | Keyword.com | Weekly | Navneet | Roadmap bottom-up build-up |
| Share of live URLs in the top 10 | Ranked URLs divided by URLs live | 1.5% | 6.0% | 10.5% | 15.0% | Keyword.com | Weekly | Navneet | Uplifted from the 1.74% first-year norm for exact-match long tail |
| Average monthly searches per ranked URL | Search volume per ranked URL | 90 | 90 | 90 | 90 | Keyword.com | Monthly | Navneet | Estimate held flat across all 12 months |
| Click-through rate | Clicks divided by impressions on ranked URLs | 18% | 18% | 18% | 18% | Site Kit by Google | Monthly | Navneet | Estimate; no FAQ rich results after May 7, 2026 and no review stars |
| Organic visits per month | Organic sessions in the month | 81 | 729 | 1,993 | 3,451 | Site Kit by Google | Weekly | Navneet | Roadmap bottom-up build-up |
| Total visits per month, base case | Organic sessions only | 81 | 729 | 1,993 | 3,451 | Site Kit by Google | Monthly | Navneet | Base case is organic only |

# Section 13. Launch checklist, September 21 to November 20, 2026

The sprint runs from Monday, September 21, 2026 to Friday, November 20, 2026. Every date below matches the Dated build schedule section and in Section 4.5. Ontario Thanksgiving, Monday, October 12, 2026, carries no deliverable.

| Date | Task | Owner | Tool | Done-when test | Notes |
|---|---|---|---|---|---|
| Friday, October 2, 2026 | Publish the WHO block in the site footer | Navneet | WordPress | This exact block appears in the footer: "Gondaliya CPA Professional Corporation, CPA Ontario Firm Registration 61330051, is a registered EFILE electronic filer. corpnilfilingfor300.ca is a department of Gondaliya CPA Professional Corporation. Sharad Gondaliya, CPA, holds CPA Ontario Membership 61040184. Vandana Goel, CPA, holds CPA Ontario Membership 61158584. All returns are prepared and transmitted in Canada. Office: 55 Queen St E, Suite 1205, Toronto, ON M5C 1R6. Phone: 647-212-9559. Email: info@gondaliyacpa.ca." | Registered EFILE electronic filer is the only permitted EFILE phrase |
| Wednesday, October 7, 2026 | Build the banned-phrases sweep into the publishing pipeline | Navneet | Python pipeline, WPCode Lite | The sweep blocks a publish on any of these strings: CRA authorized, authorized by CRA, CRA approved, approved by CRA, CRA agent, agent of CRA, CRA partner, partner of CRA, CRA endorsed, endorsed by CRA, CRA certified, official CRA, no penalty, guaranteed, T183 without CORP, conservatively, easily, simply, the EFILE number, the CRA GroupID | The sweep whitelists authorized signing officer on T183CORP pages only |
| Friday, October 9, 2026 | Deploy the gondaliyacpa.ca wording updates sent by Sharad Gondaliya on October 6, 2026 | Navneet | WordPress, UpdraftPlus | Every listed page shows the new wording, with a backup taken before the change | Take the backup first so any page can be restored |
| Friday, October 9, 2026 | Publish the first 55 URLs: Family 8 15, Family 9 10, Family 15 24, Family 16 5, home 1 | Navneet | WordPress, Elementor Pro, Python pipeline | 55 URLs return HTTP 200, each with a unique title and meta description | October 9, 2026 is the only batch with the home page |
| Friday, October 9, 2026 | Apply schema, titles, meta descriptions, internal links and visible update dates to the 55 URLs | Navneet | Rank Math SEO PRO, Link Whisper | Every URL validates with zero schema errors, and the sweep finds no EFILE number and no CRA GroupID anywhere in schema or in the sitemap | Trustindex rich snippets stay off; self-serving review schema earns no stars |
| Friday, October 23, 2026 | Run the WCAG 2.1 AA and AODA check on every template | Navneet | Astra Pro, Elementor Pro | Contrast, keyboard navigation, form labels and focus order pass on the home page, the checkout screen and the signing screen | Fix the template before the full QA on Wednesday, November 18, 2026 |
| Wednesday, November 18, 2026 | Run the full QA across every URL: WCAG 2.1 AA and AODA, schema validation, broken-link crawl, banned-phrase and EFILE-number sweep, unique-data check | Navneet | Site Kit by Google, Rank Math SEO PRO, Link Whisper, Python pipeline | Zero errors on every check across the 968 structural URLs and the 60 blog posts live | Matches the dated build table for Wednesday, November 18, 2026 |

# Appendix A. Full URL list

Enumerated one per line, grouped by family, in a plain list a Python script can read. Family 4 is given as its multiplication. Family 13 is given as its first 40 titles in Section 7.8 plus the slug rule in Section 6(a).

## Family 1. Industry and entity verticals (215 URLs)

/nil-t2-return-for-dormant-consulting-corporations/

/nil-t2-return-for-real-estate-numbered-corporations/

/nil-t2-return-for-trucking-corporations/

/nil-t2-return-for-dental-professional-corporations/

/nil-t2-return-for-shell-corporations/

/nil-t2-return-for-landscaping-corporations/

/nil-t2-return-for-medical-professional-corporations/

/nil-t2-return-for-it-consulting-corporations/

/nil-t2-return-for-staffing-agency-corporations/

/nil-t2-return-for-restaurant-corporations/

/nil-t2-return-for-hair-salon-corporations/

/nil-t2-return-for-gym-corporations/

/nil-t2-return-for-daycare-corporations/

/nil-t2-return-for-ecommerce-corporations/

/nil-t2-return-for-amazon-fba-corporations/

/nil-t2-return-for-crypto-trading-corporations/

/nil-t2-return-for-photography-corporations/

/nil-t2-return-for-taxi-corporations/

/nil-t2-return-for-moving-corporations/

/nil-t2-return-for-cleaning-corporations/

/nil-t2-return-for-hvac-corporations/

/nil-t2-return-for-plumbing-corporations/

/nil-t2-return-for-electrical-contracting-corporations/

/nil-t2-return-for-roofing-corporations/

/nil-t2-return-for-flooring-corporations/

/nil-t2-return-for-painting-corporations/

/nil-t2-return-for-drywall-corporations/

/nil-t2-return-for-welding-corporations/

/nil-t2-return-for-machine-shop-corporations/

/nil-t2-return-for-printing-corporations/

/nil-t2-return-for-signage-corporations/

/nil-t2-return-for-tutoring-corporations/

/nil-t2-return-for-translation-corporations/

/nil-t2-return-for-travel-agency-corporations/

/nil-t2-return-for-event-planning-corporations/

/nil-t2-return-for-catering-corporations/

/nil-t2-return-for-food-truck-corporations/

/nil-t2-return-for-bakery-corporations/

/nil-t2-return-for-brewery-corporations/

/nil-t2-return-for-franchise-corporations/

/nil-t2-return-for-import-corporations/

/nil-t2-return-for-export-corporations/

/nil-t2-return-for-wholesale-corporations/

/nil-t2-return-for-pharmacy-corporations/

/nil-t2-return-for-physiotherapy-corporations/

/nil-t2-return-for-chiropractic-corporations/

/nil-t2-return-for-optometry-corporations/

/nil-t2-return-for-veterinary-corporations/

/nil-t2-return-for-law-professional-corporations/

/nil-t2-return-for-architecture-corporations/

/nil-t2-return-for-engineering-professional-corporations/

/nil-t2-return-for-land-surveying-corporations/

/nil-t2-return-for-real-estate-brokerage-corporations/

/nil-t2-return-for-mortgage-brokerage-corporations/

/nil-t2-return-for-insurance-brokerage-corporations/

/nil-t2-return-for-bookkeeping-corporations/

/nil-t2-return-for-film-production-corporations/

/nil-t2-return-for-music-recording-corporations/

/nil-t2-return-for-esports-corporations/

/nil-t2-return-for-esthetics-corporations/

/nil-t2-return-for-barbering-corporations/

/nil-t2-return-for-tattoo-studio-corporations/

/nil-t2-return-for-pet-grooming-corporations/

/nil-t2-return-for-auto-repair-corporations/

/nil-t2-return-for-towing-corporations/

/nil-t2-return-for-car-rental-corporations/

/nil-t2-return-for-equipment-rental-corporations/

/nil-t2-return-for-security-guard-corporations/

/nil-t2-return-for-janitorial-corporations/

/nil-t2-return-for-snow-removal-corporations/

/nil-t2-return-for-forestry-corporations/

/nil-t2-return-for-mining-exploration-corporations/

/nil-t2-return-for-oil-and-gas-service-corporations/

/nil-t2-return-for-farming-corporations/

/nil-t2-return-for-greenhouse-corporations/

/nil-t2-return-for-cannabis-corporations/

/nil-t2-return-for-fishing-corporations/

/nil-t2-return-for-solar-installation-corporations/

/nil-t2-return-for-ev-charging-corporations/

/nil-t2-return-for-drone-services-corporations/

/nil-t2-return-for-holding-corporations/

/nil-t2-return-for-rental-property-corporations/

/nil-t2-return-for-investment-holding-corporations/

/nil-t2-return-for-dormant-trucking-corporations/

/nil-t2-return-for-dormant-landscaping-corporations/

/nil-t2-return-for-dormant-restaurant-corporations/

/nil-t2-return-for-dormant-hair-salon-corporations/

/nil-t2-return-for-dormant-gym-corporations/

/nil-t2-return-for-dormant-daycare-corporations/

/nil-t2-return-for-dormant-ecommerce-corporations/

/nil-t2-return-for-dormant-amazon-fba-corporations/

/nil-t2-return-for-dormant-crypto-trading-corporations/

/nil-t2-return-for-dormant-photography-corporations/

/nil-t2-return-for-dormant-taxi-corporations/

/nil-t2-return-for-dormant-moving-corporations/

/nil-t2-return-for-dormant-cleaning-corporations/

/nil-t2-return-for-dormant-hvac-corporations/

/nil-t2-return-for-dormant-plumbing-corporations/

/nil-t2-return-for-dormant-roofing-corporations/

/nil-t2-return-for-dormant-numbered-corporations/

/nil-t2-return-for-dormant-holding-corporations/

/nil-t2-return-for-dormant-rental-property-corporations/

/nil-t2-return-for-dormant-franchise-corporations/

/nil-t2-return-for-dormant-snow-removal-corporations/

/nil-t2-return-for-dormant-cannabis-corporations/

/nil-t2-return-for-inactive-it-consulting-corporations/

/nil-t2-return-for-inactive-staffing-agency-corporations/

/nil-t2-return-for-inactive-medical-professional-corporations/

/nil-t2-return-for-inactive-physiotherapy-corporations/

/nil-t2-return-for-inactive-chiropractic-corporations/

/nil-t2-return-for-inactive-optometry-corporations/

/nil-t2-return-for-inactive-veterinary-corporations/

/nil-t2-return-for-inactive-law-professional-corporations/

/nil-t2-return-for-inactive-architecture-corporations/

/nil-t2-return-for-inactive-engineering-professional-corporations/

/nil-t2-return-for-inactive-land-surveying-corporations/

/nil-t2-return-for-inactive-bookkeeping-corporations/

/nil-t2-return-for-inactive-import-corporations/

/nil-t2-return-for-inactive-export-corporations/

/nil-t2-return-for-inactive-wholesale-corporations/

/nil-t2-return-for-inactive-pharmacy-corporations/

/nil-t2-return-for-struck-off-numbered-corporations/

/nil-t2-return-for-struck-off-federal-corporations/

/nil-t2-return-for-struck-off-ontario-corporations/

/nil-t2-return-for-struck-off-trucking-corporations/

/nil-t2-return-for-struck-off-restaurant-corporations/

/nil-t2-return-for-pre-revenue-ecommerce-corporations/

/nil-t2-return-for-pre-revenue-mining-exploration-corporations/

/nil-t2-return-for-pre-revenue-cannabis-corporations/

/nil-t2-return-for-pre-revenue-solar-installation-corporations/

/nil-t2-return-for-pre-revenue-ev-charging-corporations/

/nil-t2-return-for-pre-revenue-esports-corporations/

/nil-t2-return-for-pre-revenue-drone-services-corporations/

/nil-t2-return-for-pre-revenue-greenhouse-corporations/

/nil-t2-return-for-post-sale-dental-professional-corporations/

/nil-t2-return-for-post-sale-pharmacy-corporations/

/nil-t2-return-for-post-sale-restaurant-corporations/

/nil-t2-return-for-post-sale-trucking-corporations/

/nil-t2-return-for-post-sale-franchise-corporations/

/nil-t2-return-for-post-sale-real-estate-brokerage-corporations/

/nil-t2-return-for-post-sale-medical-professional-corporations/

/nil-t2-return-for-wound-down-retail-corporations/

/nil-t2-return-for-wound-down-it-consulting-corporations/

/nil-t2-return-for-wound-down-staffing-agency-corporations/

/nil-t2-return-for-wound-down-event-planning-corporations/

/nil-t2-return-for-wound-down-travel-agency-corporations/

/nil-t2-return-for-wound-down-film-production-corporations/

/nil-t2-return-for-wound-down-music-recording-corporations/

/nil-t2-return-for-seasonal-landscaping-corporations/

/nil-t2-return-for-seasonal-snow-removal-corporations/

/nil-t2-return-for-seasonal-farming-corporations/

/nil-t2-return-for-seasonal-greenhouse-corporations/

/nil-t2-return-for-seasonal-fishing-corporations/

/nil-t2-return-for-seasonal-food-truck-corporations/

/nil-t2-return-for-seasonal-roofing-corporations/

/nil-t2-return-for-seasonal-catering-corporations/

/nil-t2-return-for-paused-gym-corporations/

/nil-t2-return-for-paused-hair-salon-corporations/

/nil-t2-return-for-paused-daycare-corporations/

/nil-t2-return-for-paused-catering-corporations/

/nil-t2-return-for-paused-photography-corporations/

/nil-t2-return-for-paused-tattoo-studio-corporations/

/nil-t2-return-for-paused-esthetics-corporations/

/nil-t2-return-for-paused-tutoring-corporations/

/nil-t2-return-for-shelf-numbered-corporations/

/nil-t2-return-for-shelf-holding-corporations/

/nil-t2-return-for-shelf-federal-corporations/

/nil-t2-return-for-spousal-rental-property-corporations/

/nil-t2-return-for-spousal-consulting-corporations/

/nil-t2-return-for-spousal-bookkeeping-corporations/

/nil-t2-return-for-spousal-ecommerce-corporations/

/nil-t2-return-for-spousal-holding-corporations/

/nil-t2-return-for-single-director-consulting-corporations/

/nil-t2-return-for-single-director-trucking-corporations/

/nil-t2-return-for-single-director-it-consulting-corporations/

/nil-t2-return-for-single-director-photography-corporations/

/nil-t2-return-for-single-director-numbered-corporations/

/nil-t2-return-for-single-director-medical-professional-corporations/

/nil-t2-return-for-two-shareholder-landscaping-corporations/

/nil-t2-return-for-two-shareholder-restaurant-corporations/

/nil-t2-return-for-two-shareholder-auto-repair-corporations/

/nil-t2-return-for-two-shareholder-holding-corporations/

/nil-t2-return-for-two-shareholder-cleaning-corporations/

/nil-t2-return-for-numbered-holding-corporations/

/nil-t2-return-for-numbered-rental-property-corporations/

/nil-t2-return-for-numbered-trucking-corporations/

/nil-t2-return-for-numbered-investment-holding-corporations/

/nil-t2-return-for-named-holding-corporations/

/nil-t2-return-for-named-federal-corporations/

/nil-t2-return-for-named-ontario-corporations/

/nil-t2-return-for-federal-holding-corporations/

/nil-t2-return-for-federal-consulting-corporations/

/nil-t2-return-for-federal-ecommerce-corporations/

/nil-t2-return-for-federal-numbered-corporations/

/nil-t2-return-for-provincial-holding-corporations/

/nil-t2-return-for-provincial-numbered-corporations/

/nil-t2-return-for-non-resident-owned-holding-corporations/

/nil-t2-return-for-non-resident-owned-rental-property-corporations/

/nil-t2-return-for-non-resident-owned-ecommerce-corporations/

/nil-t2-return-for-non-resident-owned-consulting-corporations/

/nil-t2-return-for-non-resident-owned-import-corporations/

/nil-t2-return-for-non-resident-owned-farming-corporations/

/nil-t2-return-for-immigrant-founder-restaurant-corporations/

/nil-t2-return-for-immigrant-founder-trucking-corporations/

/nil-t2-return-for-immigrant-founder-consulting-corporations/

/nil-t2-return-for-immigrant-founder-grocery-corporations/

/nil-t2-return-for-immigrant-founder-cleaning-corporations/

/nil-t2-return-for-immigrant-founder-ecommerce-corporations/

/nil-t2-return-for-immigrant-founder-taxi-corporations/

/nil-t2-return-for-student-founder-tutoring-corporations/

/nil-t2-return-for-student-founder-ecommerce-corporations/

/nil-t2-return-for-student-founder-app-development-corporations/

/nil-t2-return-for-student-founder-esports-corporations/

/nil-t2-return-for-student-founder-photography-corporations/

/nil-t2-return-for-student-founder-drone-services-corporations/

## Family 2. Calculators and checkers (150 URLs)

/nil-t2-eligibility-checker/

/t2-filing-deadline-calculator/

/catch-up-nil-filing-cost-calculator/

/unfiled-years-checker/

/fiscal-year-end-calculator/

/t2-short-eligibility-checker/

/non-resident-t2-penalty-calculator/

/dissolution-readiness-checker/

/first-tax-year-53-week-checker/

/gifi-requirement-checker/

/nil-t2-price-with-hst-calculator/

/business-number-status-checker/

/inactive-corporation-filing-checker/

/dormant-corporation-obligation-checker/

/zero-activity-corporation-checker/

/nil-return-vs-full-return-checker/

/nil-t2-document-checklist-checker/

/t2-filing-requirement-checker/

/still-required-to-file-checker/

/t2-six-month-deadline-calculator/

/corporate-balance-due-date-calculator/

/two-month-balance-due-date-calculator/

/three-month-ccpc-balance-due-date-calculator/

/due-date-weekend-holiday-shift-calculator/

/final-t2-return-due-date-calculator/

/amalgamation-t2-due-date-calculator/

/wind-up-final-return-deadline-calculator/

/short-tax-year-deadline-calculator/

/days-overdue-calculator/

/next-t2-due-date-checker/

/t2-late-filing-penalty-calculator/

/repeated-failure-to-file-penalty-calculator/

/nil-return-late-penalty-checker/

/cra-arrears-interest-calculator/

/instalment-interest-calculator/

/failure-to-comply-penalty-calculator/

/penalty-on-zero-balance-owing-checker/

/gross-negligence-penalty-checker/

/voluntary-disclosure-eligibility-checker/

/taxpayer-relief-eligibility-checker/

/interest-relief-application-checker/

/t1135-late-penalty-calculator/

/t106-late-filing-penalty-calculator/

/t1134-filing-requirement-checker/

/voluntary-dissolution-cost-calculator/

/dissolution-timeline-calculator/

/federal-dissolution-eligibility-checker/

/ontario-dissolution-consent-checker/

/dissolution-final-t2-checker/

/corporate-revival-requirement-checker/

/involuntary-dissolution-risk-checker/

/dissolution-outstanding-filings-checker/

/clearance-certificate-requirement-checker/

/dissolve-or-keep-filing-cost-calculator/

/back-year-t2-cost-calculator/

/multi-year-nil-filing-total-calculator/

/ten-year-catch-up-cost-calculator/

/years-behind-filing-cost-calculator/

/outstanding-returns-count-checker/

/catch-up-filing-timeline-calculator/

/year-end-change-approval-checker/

/fiscal-period-length-calculator/

/tax-year-end-selection-calculator/

/53-week-year-end-calculator/

/short-first-year-calculator/

/tax-years-since-incorporation-calculator/

/stub-period-return-checker/

/gifi-code-lookup-checker/

/nil-gifi-balance-sheet-checker/

/gifi-schedule-100-checker/

/gifi-schedule-125-checker/

/gifi-schedule-141-checker/

/balance-sheet-balancing-checker/

/retained-earnings-rollforward-calculator/

/schedule-50-shareholder-information-checker/

/schedule-8-cca-requirement-checker/

/schedule-1-net-income-reconciliation-calculator/

/schedule-3-dividends-paid-checker/

/schedule-7-investment-income-calculator/

/schedule-9-related-corporations-checker/

/schedule-11-shareholder-transactions-checker/

/schedule-23-association-agreement-checker/

/schedule-88-internet-activities-checker/

/schedule-546-ontario-annual-return-checker/

/required-schedules-checker/

/schedule-33-taxable-capital-checker/

/t2-short-vs-full-return-checker/

/t2-short-ccpc-condition-checker/

/t2-short-exclusion-checker/

/t2-short-nil-income-checker/

/non-resident-corporation-filing-checker/

/treaty-based-return-checker/

/carrying-on-business-in-canada-checker/

/permanent-establishment-checker/

/branch-tax-calculator/

/section-116-clearance-checker/

/regulation-105-withholding-calculator/

/part-xiii-withholding-calculator/

/non-resident-director-checker/

/t1135-foreign-property-checker/

/non-resident-gst-registration-checker/

/ontario-annual-return-deadline-calculator/

/ontario-annual-return-requirement-checker/

/ontario-business-registry-filing-checker/

/federal-annual-return-deadline-calculator/

/corporations-canada-annual-return-checker/

/annual-return-late-fee-calculator/

/annual-return-vs-tax-return-checker/

/ontario-corporate-key-checker/

/extra-provincial-registration-checker/

/federal-annual-return-fee-calculator/

/ontario-missed-annual-returns-calculator/

/ontario-initial-return-deadline-calculator/

/notice-of-change-requirement-checker/

/gst-hst-nil-return-deadline-calculator/

/gst-hst-registration-requirement-checker/

/small-supplier-threshold-calculator/

/gst-hst-filing-frequency-calculator/

/gst-hst-account-closure-checker/

/gst-hst-nil-filing-penalty-calculator/

/gst-hst-nil-remittance-checker/

/payroll-nil-remittance-checker/

/payroll-account-closure-checker/

/t4-nil-filing-requirement-checker/

/payroll-account-dormant-checker/

/payroll-remittance-due-date-calculator/

/t4-late-filing-penalty-calculator/

/paid-up-capital-calculator/

/share-capital-reporting-checker/

/taxable-capital-employed-in-canada-calculator/

/small-business-deduction-limit-calculator/

/stated-capital-account-checker/

/share-issuance-record-checker/

/shareholder-register-completeness-checker/

/capital-dividend-account-calculator/

/shareholder-loan-repayment-deadline-calculator/

/shareholder-loan-income-inclusion-calculator/

/shareholder-loan-prescribed-interest-calculator/

/shareholder-benefit-checker/

/shareholder-loan-balance-checker/

/due-to-versus-due-from-shareholder-checker/

/subsection-15-2-exposure-checker/

/cra-demand-to-file-deadline-calculator/

/demand-to-file-penalty-calculator/

/notional-assessment-risk-checker/

/arbitrary-assessment-response-checker/

/cra-letter-response-deadline-calculator/

/director-liability-exposure-checker/

/collections-action-risk-checker/

/cra-account-standing-checker/

## Family 3. City hubs (15 URLs)

/nil-corporate-tax-filing-toronto/

/nil-corporate-tax-filing-mississauga/

/nil-corporate-tax-filing-brampton/

/nil-corporate-tax-filing-scarborough/

/nil-corporate-tax-filing-etobicoke/

/nil-corporate-tax-filing-north-york/

/nil-corporate-tax-filing-markham/

/nil-corporate-tax-filing-vaughan/

/nil-corporate-tax-filing-richmond-hill/

/nil-corporate-tax-filing-oakville/

/nil-corporate-tax-filing-ottawa/

/nil-corporate-tax-filing-oshawa/

/nil-corporate-tax-filing-guelph/

/nil-corporate-tax-filing-hamilton/

/nil-corporate-tax-filing-windsor/

## Family 4. Service by place matrix (336 URLs, given as a multiplication)

12 service slugs, where <place> is one city term or one jurisdiction term:

/nil-t2-filing-<place>/

/catch-up-nil-t2-filing-<place>/

/dormant-corporation-filing-<place>/

/final-t2-before-dissolution-<place>/

/t2-short-filing-<place>/

/nil-t2-filing-cost-in-<place>/

/unfiled-corporate-tax-returns-<place>/

/no-activity-corporation-tax-return-<place>/

/numbered-corporation-nil-filing-<place>/

/inactive-holding-corporation-t2-filing-<place>/

/nil-t2-filing-deadline-<place>/

/nil-t2-filing-for-non-resident-owned-corporations-<place>/

15 city terms: toronto, mississauga, brampton, scarborough, etobicoke, north-york, markham, vaughan, richmond-hill, oakville, ottawa, oshawa, guelph, hamilton, windsor

13 jurisdiction terms: ontario, quebec, british-columbia, alberta, manitoba, saskatchewan, nova-scotia, new-brunswick, newfoundland-and-labrador, prince-edward-island, yukon, northwest-territories, nunavut

Multiplication: 12 x 15 = 180 city URLs, plus 12 x 13 = 156 jurisdiction URLs, total 336 URLs. Note: /nil-t2-filing-cost-in-<place>/ renders as /nil-t2-filing-cost-in-toronto/, not /nil-t2-filing-cost-in--toronto/.

## Family 5. Question pages (45 URLs)

/what-happens-if-i-dont-file-a-nil-t2/

/what-happens-if-i-dont-file-my-t2-for-five-years/

/what-happens-if-i-dont-file-a-t2-before-dissolving-my-corporation/

/what-happens-if-i-dont-report-a-dormant-corporation-to-cra/

/what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2/

/what-happens-if-i-dont-file-a-nil-t2-for-a-numbered-company/

/what-happens-if-i-dont-file-t2-returns-after-my-corporation-is-dissolved/

/do-i-need-to-file-a-t2-if-my-corporation-had-no-activity/

/do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account/

/do-i-need-financial-statements-for-a-nil-t2-return/

/do-i-need-to-file-a-t2-for-the-year-my-corporation-was-dissolved/

/do-i-need-a-business-number-to-file-a-nil-t2/

/do-i-need-to-file-a-nil-t2-if-i-never-started-operating/

/do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive/

/can-i-file-five-years-of-nil-t2-returns-at-once/

/can-i-file-a-nil-t2-myself-without-an-accountant/

/can-i-dissolve-my-corporation-with-unfiled-t2-returns/

/can-i-file-a-nil-t2-late-without-a-penalty/

/can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about/

/can-i-still-file-a-t2-after-my-corporation-was-dissolved/

/can-i-catch-up-on-unfiled-t2-returns-without-an-audit/

/how-do-i-file-a-nil-t2-return-in-canada/

/how-do-i-catch-up-on-years-of-unfiled-t2-returns/

/how-do-i-know-if-my-corporation-counts-as-dormant/

/how-do-i-find-out-which-t2-years-are-outstanding/

/how-do-i-dissolve-a-corporation-that-has-never-filed-a-t2/

/how-do-i-close-my-corporate-tax-account-after-dissolution/

/how-do-i-fix-a-nil-t2-return-i-filed-with-the-wrong-year-end/

/when-should-i-file-my-first-t2-after-incorporating/

/when-should-i-file-a-nil-t2-for-a-short-first-tax-year/

/when-should-i-dissolve-a-dormant-corporation/

/when-should-i-tell-cra-my-corporation-is-inactive/

/when-should-i-file-the-final-t2-for-a-dissolving-corporation/

/when-should-i-start-catching-up-on-unfiled-t2-returns/

/how-long-does-it-take-to-file-a-nil-t2-return/

/how-long-do-i-have-to-file-a-t2-after-my-year-end/

/how-long-can-a-corporation-stay-dormant-before-cra-acts/

/how-long-does-cra-take-to-assess-a-nil-t2-return/

/how-long-do-i-have-to-keep-records-for-a-dormant-corporation/

/how-long-does-it-take-to-dissolve-a-corporation-in-canada/

/how-many-years-of-unfiled-t2-returns-can-i-catch-up/

/how-many-years-back-can-cra-ask-for-a-t2-return/

/how-many-years-can-a-corporation-go-without-filing-a-t2/

/how-many-years-of-t2-returns-do-i-need-before-dissolving/

/how-many-years-of-penalties-apply-to-late-nil-t2-returns/

## Family 6. Best and route listicles (38 URLs)

/best-way-to-file-a-nil-t2-online-in-canada/

/best-way-to-file-a-nil-t2-for-a-dormant-corporation/

/best-way-to-file-a-nil-t2-for-a-numbered-company/

/best-way-to-file-a-nil-t2-for-a-holding-company/

/best-way-to-file-a-nil-t2-for-a-startup-with-no-revenue/

/best-way-to-file-a-nil-t2-for-multiple-back-years/

/best-way-to-file-a-nil-t2-without-accounting-software/

/best-way-to-file-a-nil-t2-with-a-fixed-fee/

/best-way-to-file-a-nil-t2-before-dissolving/

/best-way-to-file-a-nil-t2-after-a-cra-demand-letter/

/best-way-to-file-a-nil-t2-for-a-short-first-tax-year/

/best-way-to-file-a-nil-t2-for-an-ontario-corporation/

/best-way-to-file-a-nil-t2-for-a-british-columbia-corporation/

/best-way-to-file-a-nil-t2-for-an-alberta-corporation/

/best-way-to-file-a-nil-t2-for-a-federal-corporation/

/best-way-to-file-a-nil-t2-when-you-live-outside-canada/

/best-way-to-file-a-nil-t2-without-visiting-an-accountant/

/best-way-to-file-a-nil-t2-when-you-have-lost-your-records/

/best-way-to-file-a-nil-t2-every-year-on-time/

/cheapest-way-to-file-a-nil-t2-return-in-canada/

/cheapest-way-to-file-five-years-of-nil-t2-returns/

/cheapest-way-to-catch-up-on-unfiled-corporate-tax-returns/

/cheapest-way-to-keep-a-dormant-corporation-compliant/

/cheapest-way-to-dissolve-a-canadian-corporation/

/cheapest-way-to-close-a-corporation-with-no-activity/

/cheapest-way-to-file-corporate-taxes-for-a-holding-company/

/cheapest-way-to-get-a-nil-t2-filed-by-a-cpa/

/cheapest-way-to-file-a-t2-for-a-numbered-company/

/cheapest-way-to-file-back-taxes-for-an-inactive-corporation/

/cheapest-way-to-avoid-late-filing-penalties-on-a-t2/

/cheapest-way-to-maintain-a-shelf-corporation-in-canada/

/cheapest-way-to-file-a-final-t2-before-dissolution/

/cheapest-way-to-handle-a-cra-demand-to-file-letter/

/cheapest-way-to-file-a-nil-t2-for-a-startup-with-no-income/

/cheapest-way-to-file-corporate-taxes-with-no-bookkeeping/

/cheapest-way-to-bring-an-old-corporation-back-into-good-standing/

/cheapest-way-to-file-a-nil-t2-without-a-monthly-accounting-plan/

/cheapest-way-to-file-a-nil-t2-for-a-second-corporation/

## Family 7. Comparison pages (20 URLs)

/nil-t2-vs-zero-return/

/t2-short-vs-full-t2/

/ontario-annual-return-vs-t2/

/nil-return-vs-final-return/

/diy-vs-cpa-nil-t2/

/corpnilfilingfor300-vs-bluepeak/

/corpnilfilingfor300-vs-turbotax/

/corpnilfilingfor300-vs-t2inc/

/corpnilfilingfor300-vs-taxdeep/

/corpnilfilingfor300-vs-hr-block/

/corpnilfilingfor300-vs-cloudtax/

/paper-t2-vs-efile-t2/

/t2-short-vs-t2-short-plus-gifi/

/federal-corporation-vs-ontario-corporation-nil-filing/

/nil-t2-vs-ontario-annual-return-vs-federal-annual-return/

/dissolving-vs-filing-nil-every-year/

/voluntary-disclosure-vs-plain-late-filing/

/filing-one-year-vs-filing-all-unfiled-years/

/nil-t2-vs-nil-gst-hst-return/

/december-31-year-end-vs-a-non-calendar-year-end/

## Family 8. Cost and pricing pages (15 URLs)

/nil-t2-return-cost-ontario/

/nil-t2-return-cost-quebec/

/nil-t2-return-cost-british-columbia/

/nil-t2-return-cost-alberta/

/nil-t2-return-cost-manitoba/

/nil-t2-return-cost-saskatchewan/

/nil-t2-return-cost-nova-scotia/

/nil-t2-return-cost-new-brunswick/

/nil-t2-return-cost-newfoundland-and-labrador/

/nil-t2-return-cost-prince-edward-island/

/nil-t2-return-cost-yukon/

/nil-t2-return-cost-northwest-territories/

/nil-t2-return-cost-nunavut/

/pricing/

/price-transparency-promise/

## Family 9. Guides and pillars (30 URLs)

/nil-t2-filing-guide/

/dormant-corporation-tax-guide/

/unfiled-t2-returns-catch-up-guide/

/corporate-dissolution-tax-guide/

/first-year-t2-filing-guide/

/t2-late-filing-penalty-guide/

/inactive-holding-company-filing-guide/

/numbered-company-tax-filing-guide/

/cra-demand-to-file-response-guide/

/final-t2-return-guide/

/the-ultimate-guide-to-nil-t2-returns/

/the-ultimate-guide-to-dormant-corporations-in-canada/

/the-ultimate-guide-to-catching-up-on-unfiled-corporate-taxes/

/the-ultimate-guide-to-dissolving-a-canadian-corporation/

/the-ultimate-guide-to-t2-filing-deadlines/

/the-ultimate-guide-to-zero-activity-corporate-tax-returns/

/the-ultimate-guide-to-keeping-a-shelf-corporation-compliant/

/the-ultimate-guide-to-t2-schedules-on-a-nil-return/

/the-ultimate-guide-to-corporate-tax-arrears-and-penalties/

/the-ultimate-guide-to-winding-up-an-inactive-corporation/

/2026-canadian-nil-t2-filing-guide/

/2026-canadian-dormant-corporation-guide/

/2026-canadian-t2-deadline-guide/

/2026-canadian-corporate-dissolution-guide/

/2026-canadian-back-tax-catch-up-guide/

/2026-canadian-small-business-corporate-filing-guide/

/2026-canadian-holding-company-tax-guide/

/2026-canadian-t2-penalty-and-interest-guide/

/2026-canadian-corporate-compliance-calendar-guide/

/2026-canadian-numbered-company-maintenance-guide/

## Family 10. How-to-start and first-filing pages (25 URLs)

/first-t2-after-incorporating-in-2015/

/first-t2-after-incorporating-in-2016/

/first-t2-after-incorporating-in-2017/

/first-t2-after-incorporating-in-2018/

/first-t2-after-incorporating-in-2019/

/first-t2-after-incorporating-in-2020/

/first-t2-after-incorporating-in-2021/

/first-t2-after-incorporating-in-2022/

/first-t2-after-incorporating-in-2023/

/first-t2-after-incorporating-in-2024/

/first-t2-after-incorporating-in-2025/

/first-t2-after-incorporating-in-2026/

/what-a-new-ontario-corporation-must-file/

/what-a-new-quebec-corporation-must-file/

/what-a-new-british-columbia-corporation-must-file/

/what-a-new-alberta-corporation-must-file/

/what-a-new-manitoba-corporation-must-file/

/what-a-new-saskatchewan-corporation-must-file/

/what-a-new-nova-scotia-corporation-must-file/

/what-a-new-new-brunswick-corporation-must-file/

/what-a-new-newfoundland-and-labrador-corporation-must-file/

/what-a-new-prince-edward-island-corporation-must-file/

/what-a-new-yukon-corporation-must-file/

/what-a-new-northwest-territories-corporation-must-file/

/what-a-new-nunavut-corporation-must-file/

## Family 11. Reviews hub and reviews by city (11 URLs)

/reviews/

/reviews/toronto/

/reviews/mississauga/

/reviews/brampton/

/reviews/scarborough/

/reviews/etobicoke/

/reviews/north-york/

/reviews/markham/

/reviews/vaughan/

/reviews/richmond-hill/

/reviews/oakville/

## Family 12. Case studies (15 URLs)

/case-studies/five-years-of-nil-t2-returns-filed-in-one-week/

/case-studies/dormant-numbered-company-brought-current-after-a-cra-demand-letter/

/case-studies/startup-that-never-launched-closed-and-dissolved/

/case-studies/holding-company-with-no-activity-filed-three-back-years/

/case-studies/first-t2-filed-late-after-incorporating-without-an-accountant/

/case-studies/corporation-dissolved-with-a-final-nil-t2-return/

/case-studies/late-filing-penalties-reduced-through-taxpayer-relief/

/case-studies/non-resident-owner-catching-up-on-canadian-corporate-filings/

/case-studies/shelf-corporation-kept-compliant-for-under-a-thousand-dollars/

/case-studies/ten-years-of-unfiled-t2-returns-resolved/

/case-studies/corporate-bank-account-never-opened-and-nil-returns-required/

/case-studies/short-first-tax-year-nil-t2-filed-correctly/

/case-studies/second-corporation-forgotten-until-a-cra-notice-arrived/

/case-studies/inactive-corporation-revived-for-a-property-sale/

/case-studies/nil-t2-filings-completed-before-a-mortgage-application/

## Family 14. Deadline and date pages (23 URLs)

/nil-t2-deadline-for-a-january-31-year-end/

/nil-t2-deadline-for-a-february-28-year-end/

/nil-t2-deadline-for-a-march-31-year-end/

/nil-t2-deadline-for-a-april-30-year-end/

/nil-t2-deadline-for-a-may-31-year-end/

/nil-t2-deadline-for-a-june-30-year-end/

/nil-t2-deadline-for-a-july-31-year-end/

/nil-t2-deadline-for-a-august-31-year-end/

/nil-t2-deadline-for-a-september-30-year-end/

/nil-t2-deadline-for-a-october-31-year-end/

/nil-t2-deadline-for-a-november-30-year-end/

/nil-t2-deadline-for-a-december-31-year-end/

/file-your-2017-nil-t2-return/

/file-your-2018-nil-t2-return/

/file-your-2019-nil-t2-return/

/file-your-2020-nil-t2-return/

/file-your-2021-nil-t2-return/

/file-your-2022-nil-t2-return/

/file-your-2023-nil-t2-return/

/file-your-2024-nil-t2-return/

/file-your-2025-nil-t2-return/

/file-your-2026-nil-t2-return/

/cra-t2-deadline-calendar/

## Family 15. Trust, legal and utility (24 URLs)

/about-us/

/team/

/faq/

/cpa-faqs/

/glossary/

/resources/

/html-sitemap/

/privacy-policy/

/terms-and-conditions/

/disclaimer/

/accessibility-statement/

/community-commitment/

/data-security-and-privacy/

/contact-us/

/consultation/

/team/sharad-gondaliya-cpa/

/team/vandana-goel-cpa/

/team/navneet/

/team/deepak/

/team/second-reviewing-cpa/

/efile-status/

/engagement-terms/

/refund-policy/

/how-it-works/

## Family 16. Hub and index pages (5 URLs)

/what-we-file/

/who-this-is-for/

/provinces/

/all-calculators/

/service-areas/
