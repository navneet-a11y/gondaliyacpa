# WealthScale publishing: handoff for a new session

Source package: WealthScale-201-Pages.zip (re-attach it to the new session). Plan: 01-PUBLISHING-GUIDE.md inside the zip.

## State at October 30, 2026 (morning)
- Done: Step 1, Step 2, Step 3 (all 101 first pages, verified by checksum), October 29 check. See STATUS-2026-10-27.md.
- Day 6 done October 30 except page 105 (see STATUS). Next: Day 7 (Saturday, October 31). /tax/ is page ID 482.
- Parent IDs on the live site: /calculators/ 118, /compare/ 100, /banking/ 117, /accounts/ 99, /benefits/ 119, /reviews/ 101, /reviews/wealthsimple/ 278, /vs/ 110, /learn/ 121, /savings/ 111, /about/ 86.
- Page 198 offers checked October 30: all four still open by their stated end dates (Neo and KOHO no end date, Tangerine April 30, 2027, Simplii January 31, 2027).
- Open item 1 (Sharad's CPA review of pages 102-201 "before Day 6") is still Open in the workbook: ask Navneet whether to publish anyway.

## Method
- Content of each page = `<!-- wp:html -->\n` + file from pages-paste/ (trailing newlines removed) + `\n<!-- /wp:html -->`.
- Rank Math fields: POST /rankmath/v1/updateMeta {objectType:"post", objectID, meta:{rank_math_title, rank_math_description, rank_math_focus_keyword}} from the workbook "Pages" sheet.
- Verify with the temporary Code Snippets snippet 9 (admin-only): GET /ws-check/v1/md5?ids=... returns md5/len of post_content and seo_md5 = md5(title|description|focus keyword). GET /ws-check/v1/fetch?paths=... loads the site's own URLs (mode=sitemap returns <loc> list). Delete snippet 9 after November 3.
- Redirects: Rank Math's /updateRedirection REST route reports success but saves nothing; use POST /ws-check/v1/redirects {from, to}.
- Submit each day's URLs with POST /rankmath/v1/in/submitUrls {urls: newline-separated}.
- Workbook: after editing with openpyxl, recalculate with LibreOffice (soffice --headless --convert-to xlsx) or the Schedule sheet shows zeros in viewers.
- Parallel workers follow WORKER-INSTRUCTIONS.md; keep batches to about 3 pages each (a 7-page worker was cut off on October 28).
