# Rate correction extraction (READ-ONLY)

Site: gondaliyacpa.ca, via MCP tools mcp__gondaliya_cpa__* (load with ToolSearch, e.g. "select:mcp__gondaliya_cpa__wp_get_post_full,mcp__gondaliya_cpa__wp_get_page,mcp__gondaliya_cpa__wp_get_post").
NEVER create, update, publish or delete anything. Read only.

For each ID in your list: fetch the raw content (try wp_get_post_full with post_type "pages", context "edit", exclude nothing; if not found use post_type "posts"). Find EVERY occurrence of: `12.2%`, `3.2%`, `12.2 %`, `0.122`, `0.032`, `$600,000`, `$600K`, `600,000`, and any dollar figure clearly computed from 12.2% (e.g. "$12,200 on $100,000").

For each occurrence decide the rule (from Sharad's Existing Page Fixes file):
- R1: 12.2% stated as the CURRENT combined Ontario small business rate -> change to 11.2%, and add " (12.2% before July 1, 2026)" right after 11.2% ONLY on the first R1 change of that page.
- R2: 3.2% stated as the CURRENT Ontario small business rate -> change to 2.2%, and add " (3.2% before July 1, 2026)" only on the first R2 change of that page.
- R3: 12.2% or 3.2% tied to 2025 or earlier, or to income before July 1, 2026 -> LEAVE AS IS (after = before).
- R4: dollar figure computed from 12.2% -> recalculate at 11.2% (show the arithmetic in note). Flag "Sharad to confirm figure".
- R5: example for a December 31, 2026 year-end -> use blended 11.70%.
- R6: calculator code with 0.122 or 0.032 -> do NOT write code; after = "Replace with day-prorated rate logic from /psb-tax-cost-calculator/ (page 7)"; note the variable/line.
- R7: small business limit $600,000 / $600K -> $500,000 / $500K. (If a sentence compares $500,000 and $600,000 as a question or contrast, mark R3-style leave and explain.)
Every changed visible FAQ also has a JSON-LD copy: list the JSON-LD occurrence as its own row with location "JSON-LD".

`before` must be an EXACT substring of the raw post content (copy precisely, including HTML entities like &#8217; and tags if they fall inside), long enough to be unique in the page (normally the full sentence), at most ~400 chars. `after` = the same string with only the needed changes. Keep grammar right ("a 12.2%" -> "an 11.2%").

Write a JSON file per ID to /home/user/gondaliyacpa/psb-contractor-project/rate-correction/batch-01/<id>.json:
{"id":123,"url":"https://gondaliyacpa.ca/slug/","title":"...","rows":[{"location":"Visible|JSON-LD|Calculator code|Meta","section":"short description e.g. FAQ, hero, service card","rule":"R1","before":"...","after":"...","note":""}],"page_note":""}
If the page has no occurrences at all (search false positive), write rows: [] and page_note "No 12.2%/3.2% found".
Final answer: one line per ID: id | rows count | rules used. Under 150 words.
