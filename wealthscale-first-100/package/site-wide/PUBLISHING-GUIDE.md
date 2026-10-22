# WealthScale first-100 rebuild: publishing guide for Navneet

Site: wealthscale.ca (WordPress, GeneratePress Pro, Rank Math SEO, LiteSpeed Cache, Code Snippets).
Owner of every step: Navneet. Sharad approves pages as CPA.
Schedule: 101 pages in 5 days, Friday October 23 to Tuesday October 27, 2026 (20 a day, 21 on day 5).

## What is in the package

| Folder or file | What it is |
| --- | --- |
| pages-paste/ | 101 page files, ready to paste into one Custom HTML block each (no header) |
| pages-source/ | The same pages with a header listing URL, parent, SEO title, meta description, focus keyword, widgets and publish day |
| WealthScale_First_100_Index.xlsx | One row per page with every field you need, plus the 5-day schedule and the open items list |
| site-wide/wealthscale-widgets.css | Styles for every page component and calculator |
| site-wide/wealthscale-widgets.js | All 43 calculators and tools in one file; every figure lives in its data block at the top |
| site-wide/wealthscale-site-snippet.php | One Code Snippets snippet: loads the files, hides the duplicate H1, full-width pages, breadcrumbs, Neha's review line and reviewer schema |
| site-wide/images/ | Neha's headshot at 400 and 128 px (JPG and WebP), metadata removed |
| research/ | The verified fact registers and scores behind every page (keep for updates) |

## One-time setup (Day 1, before the first page)

| Step | Action | Done when |
| --- | --- | --- |
| 1 | Back up the site in Hostinger (files and database) | Backup listed in hPanel |
| 2 | In Hostinger File Manager create /public_html/wp-content/uploads/ws/ and /public_html/wp-content/uploads/ws/people/ | Both folders exist |
| 3 | Upload wealthscale-widgets.css and wealthscale-widgets.js to /wp-content/uploads/ws/ | https://wealthscale.ca/wp-content/uploads/ws/wealthscale-widgets.js opens |
| 4 | Upload neha-gupta-cfa-128.jpg and neha-gupta-cfa-400.jpg to /wp-content/uploads/ws/people/. Export Sharad's existing headshot (the one on his Gondaliya CPA team page) as square JPGs named sharad-gondaliya-cpa-128.jpg (128 x 128) and sharad-gondaliya-cpa-400.jpg (400 x 400), strip metadata, and upload them to the same folder | All four images open in a browser |
| 5 | Code Snippets, Add New, PHP snippet "WealthScale: assets, page layout, reviewer schema": paste wealthscale-site-snippet.php without the first line `<?php`, Run everywhere, Activate | No error notice; a test page shows no theme title |
| 6 | LiteSpeed Cache, Page Optimization, Tuning: add `wealthscale-widgets` to JS Excludes and JS Deferred/Delayed Excludes; Purge All | Calculators load on a test page |
| 7 | Users: create the user "Sharad Gondaliya" (display name "Sharad Gondaliya, CPA", bio = the one-line credit) and make him author of every page; change the display name of "admin" so it never shows | Page source shows no "admin" author |
| 8 | Rank Math: Titles & Meta, Pages: Schema Type Article, Article Type Article; General Settings, Breadcrumbs: on; Instant Indexing module: on, with Bing IndexNow key | Settings saved |
| 9 | Delete the "Hello world!" post, its sample comment and the "Sample Page" | Gone from Posts and Pages |
| 10 | Rank Math, Redirections: 301 every live URL that is not in the 101-page list to its closest new page (list the pairs in the workbook, sheet "Open items") | No old URL returns 404 |
| 11 | Cookie banner live, and Google Analytics set to load only after the visitor accepts (the calculators send a "calculator used" event with the calculator name only) | No analytics request before consent in the browser's network tab |

## How to publish each page (about 10 minutes a page)

| Step | Action |
| --- | --- |
| 1 | Pages, Add New (or open the existing page with the same URL and replace its content, which keeps the page ID and history) |
| 2 | Title: the "WP page title" column. Page Attributes, Parent: the "Parent" column. Slug: the last part of the URL |
| 3 | Add one Custom HTML block and paste the whole file from pages-paste/ |
| 4 | Rank Math box: Focus Keyword, SEO Title and Meta Description from the workbook, exactly as written |
| 5 | Preview on desktop and at 390 px wide: calculators load, no sideways scrolling, both photos show |
| 6 | Publish. For the home page: Settings, Reading, static front page = Home |
| 7 | Mark the row "Live" in the workbook with the date |

Links to pages scheduled for a later day return 404 until those pages go live. That clears by Day 5; do not remove or change any link.

## Every evening after publishing

| Step | Action |
| --- | --- |
| 1 | LiteSpeed: Purge All |
| 2 | Rank Math sitemap: confirm the day's pages are listed at /page-sitemap.xml |
| 3 | Google Search Console: URL Inspection, Request Indexing for the day's 5 most important pages (home and hubs on Day 1) |
| 4 | Rank Math Instant Indexing: submit the day's URLs to IndexNow (Bing) |
| 5 | Rich Results Test on two pages of the day: FAQ structured data valid, no errors |

## Neha's review line

Every investing and account page shows "Financial reviewer: Neha Gupta, CFA" with "Review of this page scheduled". When Neha signs off a page in her Upwork batch, add a custom field to that page in WordPress:

| Field name | Value |
| --- | --- |
| ws_neha_reviewed_on | Her sign-off date, written as 2026-10-31 |

The line then reads "Reviewed on October 31, 2026" and the page schema adds her as a reviewer. Never set this field without her written sign-off.

## Updating a figure later

All calculator figures live in the data block at the top of wealthscale-widgets.js. Change the figure there, upload the file, change the version number in the snippet (for example 1.0.0 to 1.0.1), and purge the cache. Page text with the same figure must be updated at the same time; the research folder shows where each figure came from.

## The 5-day schedule

| Day | Date | Pages |
| --- | --- | --- |
| 1 | Friday, October 23, 2026 | Home, About, both reviewer profiles, Editorial Standards, How We Make Money, Contact, Methodology, all 10 hubs, TFSA calculator, TFSA guide (20) |
| 2 | Saturday, October 24, 2026 | 7 calculators, 11 account guides, How to Buy US Stocks, How to Invest (20) |
| 3 | Sunday, October 25, 2026 | 13 Wealthsimple pages, 4 Wealthsimple comparisons, Norbert's Gambit, Account Transfers, CPP and OAS Dates (20) |
| 4 | Monday, October 26, 2026 | 20 best-of and account listing pages (20) |
| 5 | Tuesday, October 27, 2026 | Banking and savings pages, 8 reviews, 5 comparisons, GST/HST credit page, privacy policy and terms after the lawyer's review (21) |
