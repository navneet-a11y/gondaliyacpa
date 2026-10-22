# WealthScale first-100 rebuild: writer's style guide (October 22, 2026)

Read this whole file before writing. It overrides every older WealthScale template, including "By the WealthScale Editorial Team".

## 1. The goal

WealthScale.ca (published by WealthScale Media Inc., Toronto) wants maximum SEO authority in Canadian investing, accounts, savings and banking. Every page must be the deepest, most useful page in Canada for its keyword, beating MoneySense, NerdWallet Canada and Million Dollar Journey on depth, figures and tools, and it must keep readers on WealthScale. The model for depth and structure is the Gondaliya CPA "Corporate Tax Filing Services" page: an answer-first hero, an at-a-glance box, a table of contents, 10 to 14 numbered deep sections built from bold-labelled paragraphs and tables, mid-page CTAs, what-you-need and what-you-get lists, how-it-works steps, a 10-strategies grid, a worked example with real arithmetic, a large FAQ and a closing experts block.

Theme of the whole site: **Written by a CPA. Financial review by a CFA charterholder.**

## 2. Hard rules (a page that breaks one is rejected)

1. **No outbound links and no references to other websites.** Never link to or name a website as a place to check something ("see canada.ca", "visit the CRA site", "check the provider's website" are all banned). State the figure yourself. Every `href` must be a WealthScale internal path from `links.csv` (root-relative, starting with `/`, ending with `/`, optionally with `#anchor`). The only exceptions are the credential verification links on `/about/sharad-gondaliya/` and `/about/neha-gupta/`, which their writer adds exactly as given.
2. **Only internal links to the 101 URLs in `links.csv`.** No other WealthScale path exists yet. Use descriptive anchor text with the target's keyword ("compare TFSA accounts", "RRSP contribution limit"), never "click here" or "read more".
3. **Figures come only from the research registers** in `/home/claude/ws100/research/` (`facts-accounts`, `facts-tax-benefits`, `facts-wealthsimple`, `providers-investing`, `providers-banking`) and from `scores.json`. Use only entries whose status is `verified`. If a figure is not there as verified, do not state it: describe the rule without the number, or leave it out. Never estimate, round differently, or "recall" a figure from memory. Dates of figures: say "as of October 22, 2026" for rates and fees.
4. **One plain-text checked line per page** (snippet 5 below). It names the type of source in words (for example "Canada Revenue Agency publications" or "each provider's published pricing") but never a URL or website name.
5. **General information only (NI 31-103 s.8.25).** No stock, ETF, fund or coin picks, no model portfolios, no "you should buy". Use "can", "may suit", "is built for", "works for". Naming a provider's own account types, portfolios or plans in a review is fine. On Norbert's Gambit pages you may name the interlisted US Dollar Currency ETF pair (DLR and DLR.U) as the mechanism, with a line that it is not a recommendation.
6. **Rankings follow the published score.** Best-of and listing pages order providers by the score in `scores.json` for that list, show the score as "4.6 / 5", and link to `/methodology/brokers/`. Never invent a score, star rating, award or "editor's pick".
7. **No invented experience or evidence.** No testimonials, reviews, case studies, user counts, "we tested", "we opened an account", "in our experience", screenshots or quotes. Worked examples are clearly labelled: "This example is hypothetical." Every number in an example must compute exactly; show the arithmetic.
8. **Never call anything free without naming the costs that remain** ("$0 commission on Canadian stocks; a 1.5% currency conversion fee applies to US trades").
9. **Wealthsimple pages** (URLs under `/reviews/wealthsimple/`, and `/vs/wealthsimple-...`) include this exact sentence in the hero or at-a-glance box: "WealthScale is independent and not affiliated with Wealthsimple."
10. **People and credentials.** Write "Sharad Gondaliya, CPA" and "Neha Gupta, CFA" or "CFA charterholder". Never "a CFA" on its own, "CFA certified", "Chartered Financial Analyst" as a description of her, "CFA Level", "MBA", "financial advisor" or "financial planner" for either person. Never claim Neha reviewed a specific page; her review line is handled by snippet 2. Never name Gondaliya CPA Professional Corporation as the publisher.
11. **Language.** Canadian English (cheque, centre, favour, licence as a noun, program, enrol). Grade 8 to 9 reading level. Short sentences. Answer first. Active voice. No emojis. No em dashes (use a comma, colon or full stop). No exclamation marks.
12. **Banned words and phrases** (they read as machine-written): delve, dive into, navigate, landscape, realm, unlock, unleash, leverage (as a verb), seamless, robust, cutting-edge, game-changer, empower, elevate, embark, journey, tapestry, myriad, plethora, boasts, stands out, holistic, streamline, ever-evolving, in today's, it's important to note, it's worth noting, when it comes to, whether you're, look no further, rest assured, peace of mind, crucial, comprehensive guide, ultimate guide, in conclusion, in summary, at the end of the day, a testament to, nestled, vibrant, bustling.
13. **Use "please" where it reads naturally** in instructions, once or twice a page ("Please check your latest notice of assessment before you contribute"). Never forced.
14. **Tables** always sit inside `<div class="ws-table-wrap">`. Every table has a header row in `<thead>` and exact figures, never ranges such as "0.12% to 0.25%" (write "from 0.12%" or list each figure). The CSS draws both horizontal and vertical gridlines.
15. **Keyword placement.** Focus keyword: start of the SEO title, the H1, the first sentence of the lead, at least two H2s, the meta description and the last section. Secondary keywords: in H2 or H3 headings and naturally in the body. No stuffing: write for a person.
16. **Year in titles.** Put "2026" in the SEO title and H1 only where the plan's `year_in_title` says yes. In the body, always state the year a figure applies to ("the 2026 TFSA limit is $7,000").

## 3. Output format

One file per page: `/home/claude/ws100/pages/{id:03d}-{slug}.html` (home is `001-home.html`; Neha's profile is `101-about-neha-gupta.html`). The file is pasted into one WordPress Custom HTML block, so it is an HTML fragment, not a full document.

```html
<!--
WEALTHSCALE PAGE
id: 28
url: /accounts/tfsa/
wp_parent: /accounts/
wp_page_title: TFSA Guide
seo_title: TFSA Guide 2026: How a Tax-Free Savings Account Works
meta_description: (140 to 155 characters, contains the focus keyword and one hard figure)
focus_keyword: tfsa
secondary_keywords: tax-free savings account, tfsa rules, tfsa limit 2026, tfsa withdrawal
publish_day: 1
neha_scope: yes
widgets: tfsa-room, tfsa-overcontribution
-->
<div class="ws-page">
  ... page body ...
</div>
<script type="application/ld+json">{ FAQPage JSON-LD that matches the FAQ text exactly }</script>
```

Allowed HTML: `div section h1 h2 h3 p strong em ul ol li a table caption thead tbody tr th td details summary span img br svg path script(type=application/ld+json only)`. No inline `style`, no `<style>`, no `<script>` except JSON-LD, no `<h4>`, no images except the two headshots in the snippets. Use only the CSS classes listed in section 6. Every `h2` has a unique `id` (kebab-case) and appears in the table of contents.

SEO title: 50 to 60 characters, starts with the focus keyword, no "| WealthScale" (Rank Math adds the brand). Meta description: 140 to 155 characters, plain sentence, includes the focus keyword and one concrete figure, no quotation marks.

## 4. Page anatomy (top to bottom)

Adapt the section names to the topic. Skip a block only where the plan says so (trust pages are lighter).

1. **Hero** (`<div class="ws-hero">`): eyebrow (`<span class="ws-eyebrow">`), the H1 exactly as given in the plan, a lead paragraph (`<p class="ws-lead">`) of 80 to 120 words that answers the search intent in the first sentence with the key figure, two or three buttons (`ws-btns` with `ws-btn` and `ws-btn ws-btn-ghost`) pointing to the on-page widget anchor (`#ws-tfsa-room`) and to related internal pages, then the byline (snippet 1 or 2).
2. **Trust strip** (snippet 3).
3. **At a glance** (`<div class="ws-glance">` with `<h2 id="at-a-glance">At a glance</h2>`): four to six paragraphs, each starting with a bold label ("<strong>Who can open one.</strong> ..."). This box is what AI search engines and featured snippets quote, so each line must stand alone and contain a fact.
4. **Key figures** (`ws-figures` with 3 or 4 `ws-figure` cards) where the topic has headline numbers.
5. **Primary widget**: `<div data-ws-widget="NAME"></div>` right after key figures on calculator pages and early on guide pages. Introduce it with one sentence above it. A page may hold two to four widgets, each placed in the section it supports.
6. **On this page** (`<nav class="ws-toc" aria-label="On this page"><strong>On this page</strong><ol>...</ol></nav>`) listing every H2 below it.
7. **Numbered deep sections**: 10 to 14 H2s for guides, reviews and listings (8 to 10 for hubs and calculators). H2 text: "1. TFSA Contribution Room: How It Builds Each Year". Each section is 250 to 450 words made of four to six paragraphs that start with a bold label ("<strong>Newcomers to Canada.</strong> ..."), plus a table wherever data fits. Real detail: rules, exceptions, dates, dollar amounts, edge cases, what happens if you get it wrong. No filler.
8. **Mid-page CTA bands** (two or three, snippet 4) after sections 4 and 8 or so, pointing to an internal calculator, comparison or review.
9. **What you need / What you get** (`ws-two`, two H3 lists of 6 to 10 items) adapted to the topic, for example "What you need to open a TFSA" and "What you get from a TFSA".
10. **How it works** (`<ol class="ws-steps">`, 5 to 7 steps).
11. **Strategies** ("10 TFSA Strategies That Save You Tax", `ws-strategies` grid of 8 to 10 cards, each an H3 plus 40 to 70 words). Strategies are general and rule-based, never product picks.
12. **Illustrative example** (`ws-example`): "This example is hypothetical." then a numbered walk-through with the arithmetic in brackets, for example "($7,000 x 12 = $84,000)".
13. **Comparison tables** where the topic compares options or providers.
14. **Common mistakes** (optional H2 with bold-labelled paragraphs).
15. **FAQ** (`<section class="ws-faq">` with `<h2 id="faq">`): 10 to 15 questions for guides, listings and reviews, 8 to 10 for hubs, calculators and trust pages. Each is a `<details><summary>Question?</summary><div><p>Answer of 40 to 90 words, answer first.</p></div></details>`. The JSON-LD repeats the same questions and answers as plain text.
16. **Closing CTA** (snippet 4).
17. **Meet the experts** (snippet 6, exactly).
18. **Checked line and disclaimer** (snippets 5 and 7).

### Length targets (body words, excluding the experts block and JSON-LD)

| Page type | Target words | H2 sections | FAQs | Widgets |
| --- | --- | --- | --- | --- |
| Home | 4,000 | 10 | 10 | 3 |
| Hub | 3,000 | 8 | 8 | 1 to 3 |
| Calculator | 3,000 | 8 to 10 | 10 | 2 to 3 |
| Account guide | 5,000 | 12 to 14 | 12 | 2 |
| Wealthsimple review or guide | 5,000 | 12 to 14 | 12 | 1 to 2 |
| Best-of or account listing | 6,500 | 12 to 14 plus one ranked card per provider | 12 | 1 to 2 |
| Rates page | 5,000 | 12 | 12 | 2 |
| Provider review | 5,500 | 12 to 14 | 12 | 1 to 2 |
| Versus page | 4,500 | 12 | 12 | 1 to 2 |
| Learn or markets guide | 4,500 | 12 | 12 | 2 to 3 |
| Benefit dates page | 3,500 | 10 | 12 | 2 to 3 |
| Trust or profile page | 1,500 to 2,500 | 6 to 10 | 6 to 8 | 0 |

### Best-of and listing pages: ranked provider cards

After the at-a-glance box and the comparison table, give one `<div class="ws-rank">` per provider in score order:

```html
<div class="ws-rank" id="rank-questrade">
  <div class="ws-rank-head"><h3>1. Questrade: best for (one phrase from scores.json "best_for")</h3>
  <span class="ws-score"><span class="ws-score-n">4.6</span>/ 5</span></div>
  <div class="ws-scorebar"><i style="width:92%"></i></div>  <!-- the ONLY allowed inline style: width = score / 5 -->
  <p><strong>Why it ranks here.</strong> ...</p>
  <p><strong>Costs.</strong> ...</p>
  <p><strong>Accounts.</strong> ...</p>
  <div class="ws-proscons"><div class="ws-pros"><h3>Pros</h3><ul>...</ul></div><div class="ws-cons"><h3>Cons</h3><ul>...</ul></div></div>
  <p><a class="ws-btn ws-btn-ghost" href="/reviews/questrade/">Read our Questrade review</a></p>
</div>
```

Only link to a review page that exists in `links.csv`. For a provider without a review page, leave out the button.

## 5. Snippets (copy exactly; change only what is in square brackets)

Image paths: the two headshots are uploaded to `/wp-content/uploads/ws/people/`.

### Snippet 1: byline for pages in Neha's review scope (neha_scope: yes)

```html
<div class="ws-byline">
  <div class="ws-person"><img src="/wp-content/uploads/ws/people/sharad-gondaliya-cpa-128.jpg" alt="Sharad Gondaliya, CPA" width="44" height="44"><span>Written by <a href="/about/sharad-gondaliya/">Sharad Gondaliya, CPA</a> <span class="ws-badge ws-badge-cpa"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5l-8-3zm-1.2 14.2-3.5-3.5 1.4-1.4 2.1 2.1 4.9-4.9 1.4 1.4-6.3 6.3z"/></svg>CPA</span><span class="ws-role">Chartered Professional Accountant, CPA Ontario No. 61040184</span></span></div>
  <div class="ws-person"><img src="/wp-content/uploads/ws/people/neha-gupta-cfa-128.jpg" alt="Neha Gupta, CFA, Financial Reviewer at WealthScale" width="44" height="44"><span>Financial reviewer: <a href="/about/neha-gupta/">Neha Gupta, CFA</a> <span class="ws-badge ws-badge-cfa"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5l-8-3zm-1.2 14.2-3.5-3.5 1.4-1.4 2.1 2.1 4.9-4.9 1.4 1.4-6.3 6.3z"/></svg>CFA charterholder</span><span class="ws-role ws-review-status" data-ws-review="pending">Review of this page scheduled</span></span></div>
  <div class="ws-dates">Updated October 22, 2026 &middot; Figures checked October 22, 2026</div>
</div>
```

### Snippet 2: byline for pages outside Neha's scope (neha_scope: no)

Same as snippet 1 but the second person line reads:

```html
  <div class="ws-person"><img src="/wp-content/uploads/ws/people/neha-gupta-cfa-128.jpg" alt="Neha Gupta, CFA, Financial Reviewer at WealthScale" width="44" height="44"><span>Our financial reviewer: <a href="/about/neha-gupta/">Neha Gupta, CFA</a> <span class="ws-badge ws-badge-cfa">[same svg]CFA charterholder</span><span class="ws-role">Reviews WealthScale's investing and account pages</span></span></div>
```

### Snippet 3: trust strip

```html
<div class="ws-trust">
  <div><b>Written by a CPA</b>Sharad Gondaliya, CPA Ontario No. 61040184</div>
  <div><b>CFA charterholder reviewer</b>Neha Gupta, CFA reviews our investing and account pages; each page shows its review status</div>
  <div><b>Figures checked</b>October 22, 2026</div>
  <div><b>[Page-specific fourth item]</b>[for example "Ranked by a published score", "Free calculators, no sign-up", "Independent of every provider"]</div>
</div>
```

### Snippet 4: CTA band

```html
<div class="ws-cta"><p>[One sentence that tells the reader what to do next]</p>
<div class="ws-btns"><a class="ws-btn" href="[internal path or #ws-widget-id]">[Action]</a><a class="ws-btn ws-btn-ghost" href="[internal path]">[Second action]</a></div></div>
```

### Snippet 5: checked line (once, just before the experts block)

```html
<p class="ws-checked">Figures on this page were checked against [Canada Revenue Agency publications | each provider's published pricing | Service Canada publications] on October 22, 2026. We update this page when a figure changes.</p>
```

### Snippet 6: meet the experts (every page, exactly as written)

```html
<section class="ws-section" id="experts">
<h2 id="meet-the-experts">Meet the Experts Behind WealthScale</h2>
<div class="ws-experts">
  <div class="ws-expert">
    <div class="ws-expert-head"><img src="/wp-content/uploads/ws/people/sharad-gondaliya-cpa-400.jpg" alt="Sharad Gondaliya, CPA" width="84" height="84" loading="lazy"><div><b>Sharad Gondaliya, CPA</b><span>Writer and tax reviewer</span><span class="ws-badge ws-badge-cpa"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5l-8-3zm-1.2 14.2-3.5-3.5 1.4-1.4 2.1 2.1 4.9-4.9 1.4 1.4-6.3 6.3z"/></svg>CPA Ontario No. 61040184</span></div></div>
    <p>Sharad is a CPA Ontario member (No. 61040184) and a Certified Public Accountant licensed in Washington and Montana, with more than 15 years in accounting and tax, a Diploma in Banking and Finance and a Certificate in Small Business Finance. He checks WealthScale content against primary sources. WealthScale is independent of his firm, Gondaliya CPA Professional Corporation, and provides general information only, not personal financial, investment, tax or legal advice.</p>
    <ul><li>Chartered Professional Accountant, CPA Ontario</li><li>Certified Public Accountant, Washington (No. 57629) and Montana (No. PAC-CPAP-LIC-033176)</li><li>Writing on tax and registered accounts since 2021</li><li>Reader's Choice Award 2025 Winner, Best Accountant (Toronto)</li></ul>
    <p><a href="/about/sharad-gondaliya/">Read Sharad's profile and verify his credentials</a></p>
  </div>
  <div class="ws-expert">
    <div class="ws-expert-head"><img src="/wp-content/uploads/ws/people/neha-gupta-cfa-400.jpg" alt="Neha Gupta, CFA, Financial Reviewer at WealthScale" width="84" height="84" loading="lazy"><div><b>Neha Gupta, CFA</b><span>Financial Reviewer</span><span class="ws-badge ws-badge-cfa"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5l-8-3zm-1.2 14.2-3.5-3.5 1.4-1.4 2.1 2.1 4.9-4.9 1.4 1.4-6.3 6.3z"/></svg>CFA charterholder</span></div></div>
    <p>Neha Gupta is a CFA charterholder based in Winnipeg who has worked in financial markets since December 2005. She has published more than 2,600 investment articles and is Head of Operations and Finance at Whiteland Real Estate. She reviews WealthScale's investing pages for accuracy.</p>
    <ul><li>CFA charter, CFA Institute (awarded 2023)</li><li>Post Graduate Diploma in Business Administration (Finance), 2008</li><li>In financial markets since December 2005</li><li>More than 2,600 published investment articles</li></ul>
    <p><a href="/about/neha-gupta/">Read Neha's profile and verify her credentials</a></p>
  </div>
</div>
</section>
```

### Snippet 7: disclaimer (last element inside `.ws-page`)

```html
<p class="ws-disclaimer">General information only. Not financial, investment, tax or legal advice. WealthScale is independent and is published by WealthScale Media Inc., 55 Queen St E, Suite 1205, Toronto, ON M5C 1R6. CFA&reg; and Chartered Financial Analyst&reg; are registered trademarks owned by CFA Institute.</p>
```

## 6. Allowed CSS classes

ws-page, ws-hero, ws-eyebrow, ws-lead, ws-btns, ws-btn, ws-btn-ghost, ws-byline, ws-person, ws-role, ws-review-status, ws-dates, ws-badge, ws-badge-cpa, ws-badge-cfa, ws-trust, ws-glance, ws-figures, ws-figure, ws-big, ws-cap, ws-toc, ws-section, ws-numbered, ws-num, ws-cta, ws-cards, ws-card, ws-table-wrap, ws-note, ws-two, ws-steps, ws-strategies, ws-example, ws-proscons, ws-pros, ws-cons, ws-verdict, ws-score, ws-score-n, ws-scorebar, ws-rank, ws-rank-head, ws-faq, ws-experts, ws-expert, ws-expert-head, ws-checked, ws-disclaimer, ws-label.

Hub and home pages use `ws-cards` with `<a class="ws-card" href="/path/"><b>Title</b><span>One line</span></a>` to link child pages.

## 7. Widgets (placeholders the site script turns into calculators)

Write `<div data-ws-widget="NAME"></div>` exactly. The script gives it the id `ws-NAME`, so buttons can link to `#ws-NAME`. Add one sentence above each widget saying what it does, and never repeat a widget on the same page. Optional attributes are shown in brackets.

| Widget | What it does |
| --- | --- |
| tfsa-room | TFSA room from birth year, year became a resident, non-resident years, contributions and withdrawals; shows room now, room next January 1, and a year-by-year table |
| tfsa-overcontribution | 1% a month tax on an excess TFSA amount |
| rrsp-room | 2026 RRSP deduction limit from earned income, pension adjustment, carry-forward |
| rrsp-refund | Tax saved by an RRSP deduction in any province, 2026 brackets |
| rrsp-withdrawal | Withholding tax and final tax on an RRSP withdrawal |
| income-tax | 2026 federal and provincial tax, marginal rates by income type |
| capital-gains | Tax on a capital gain, loss carry-forward |
| dividend-tax | Tax on eligible and other than eligible dividends |
| fhsa-room | FHSA participation room by year opened and contributions, lifetime room, closing date |
| fhsa-eligibility | Four-question FHSA eligibility check |
| first-home | FHSA plus Home Buyers' Plan funds for one buyer or a couple |
| hbp-repayment | Home Buyers' Plan repayment schedule |
| resp-grant | CESG, Additional CESG, Canada Learning Bond, BC and Quebec grants, projection to 17 |
| rrif-minimum | RRIF minimum withdrawal and projection |
| tfsa-vs-rrsp | After-tax comparison using marginal rates now and later |
| account-chooser | Which registered accounts fit a goal (general information) |
| us-withholding | US dividend withholding by Canadian account type |
| fx-cost | Currency conversion cost at every broker |
| norberts-gambit | Norbert's Gambit vs broker conversion |
| broker-cost | Yearly cost at every broker for a trading pattern |
| broker-match | Filter brokers by features, ranked by score |
| options-cost | Yearly options commissions by broker |
| margin-interest | Margin interest by broker |
| transfer-fee | Transfer-out fees and which brokers cover them |
| robo-fee | Yearly robo-advisor fees for an amount |
| fee-drag | What a higher fee costs over time |
| compound-interest | Growth with monthly contributions, year-by-year |
| savings-goal | Monthly saving needed for a target |
| gic-calc | GIC maturity value and tax |
| gic-ladder | 1 to 5-year GIC ladder |
| hisa-earnings [data-list="usd"] | Interest at each savings account (or USD account) |
| chequing-cost | Yearly fees and interest at each chequing account |
| card-cashback | Net cash back after card fees |
| deposit-insurance | CDIC coverage by deposit category |
| crypto-fee | Trading fees at each authorized crypto platform |
| ws-tier | Wealthsimple tier and perks by assets |
| tax-software-picker | Tax software that fits a return |
| benefit-dates [data-benefit="cpp_oas", "gst", "ccb", "otb" or omit for all] | Next payment date countdown and full schedule |
| oas-clawback | OAS recovery tax |
| cpp-start-age | CPP and OAS by start age 60 to 70 |
| gst-credit | GST/HST credit estimate |
| countdown [data-date="YYYY-MM-DD" data-label="..."] | Days to a deadline |
| table-filter | Wrap a static table: `<div data-ws-widget="table-filter"><div class="ws-table-wrap"><table>...</table></div></div>` adds search and sorting |

Because widgets render in the browser, the static text around each widget must still carry the key figures for search engines (for example, a static TFSA limit table on the TFSA limit page).

## 8. Internal linking

- Use `links.csv` (id, url, h1, focus keyword). Link only to those URLs.
- Each page links to its hub, its siblings, the related calculator, the related compare page and at least one review or versus page. Targets: home and hubs link to every child; guides 20 to 35 internal links; listings and reviews 25 to 40.
- Link the first natural mention of a topic, not every mention. Vary anchors.
- Every page links to `/about/sharad-gondaliya/` and `/about/neha-gupta/` through the snippets, and to `/editorial-standards/` once in the body or FAQ.
- Best-of, compare, review and versus pages link to `/methodology/brokers/` and `/how-we-make-money/`.

## 9. FAQ JSON-LD

```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Question text exactly as on the page?","acceptedAnswer":{"@type":"Answer","text":"Answer text exactly as on the page, plain text, no HTML."}}
]}
</script>
```

Best-of and listing pages add a second JSON-LD block: an `ItemList` of the ranked providers (`position`, `name`, and `url` only when the provider has a review page in `links.csv`, written as the full `https://wealthscale.ca/...` URL). Provider review pages add a `Review` block: `itemReviewed` `{"@type":"Organization","name":"Questrade"}`, `author` `{"@type":"Person","name":"Sharad Gondaliya","url":"https://wealthscale.ca/about/sharad-gondaliya/"}`, `reviewRating` with the score from `scores.json` and `bestRating` 5, and `publisher` `{"@type":"Organization","name":"WealthScale"}`. Rank Math outputs the Article, breadcrumb and organization schema; do not add those.

## 10. Self-check before you save each page

- [ ] H1 matches the plan exactly; focus keyword in the first sentence; SEO title 50 to 60 characters; meta 140 to 155 characters.
- [ ] Word count meets the target; every H2 has an id and is in the table of contents.
- [ ] Every figure is in a research register as verified; arithmetic in examples is exact.
- [ ] No `http` link except the profile-page verification links; every internal link is in `links.csv`.
- [ ] Snippets 1 or 2, 3, 5, 6 and 7 present; widgets from the plan present and introduced.
- [ ] FAQ JSON-LD matches the visible FAQ exactly and parses as JSON.
- [ ] No banned words, no em dashes, no emojis, no exclamation marks, no stock or ETF picks, no invented claims.
