# SR&ED informational audit (READ-ONLY)

Read `/home/user/gondaliyacpa/sred-informational/RULES.md` first. It is the rule set.

Site: gondaliyacpa.ca through the MCP tools `mcp__gondaliya_cpa__*` (load them with ToolSearch, e.g.
"select:mcp__gondaliya_cpa__wp_get_post_full"). NEVER create, update, publish or delete anything. Read only.

## Fetch each ID
`wp_get_post_full` with `id`, `post_type` "pages" (or "posts"; for an elementor_library template use "elementor_library"),
`context` "edit", `include` ["meta"], `meta_keys` ["_elementor_edit_mode","_elementor_data","rank_math_title","rank_math_description"].
Big results are saved to a file: parse that file with python3 (json.load), never read it whole into context.

- `content.raw` is the post content.
- If meta `_elementor_edit_mode` == "builder", the page RENDERS from `_elementor_data` (a JSON string as stored in the DB,
  slashes stored as `\/`, quotes as `\"`, non-ASCII as `\uXXXX`). Then `content.raw` is only a fallback copy: audit `_elementor_data`.

## Find
Every place that: is a CTA (on dedicated IDs only), offers SR&ED as a firm service, gives SR&ED fees, is SR&ED sales proof,
is Service/Offer schema for SR&ED, is an FAQ answer offering the service, or is a link anchor offering the service.
Search for: SR&ED, SR&amp;ED, SRED, sred, "scientific research", "experimental development", R&D credit, consultation,
pricing-calculation, contact-us, tel:, Book, "we help", "our team", "we prepare", "we file", maximize, "why choose".
On non-dedicated IDs, most mentions are informational: then write rows: [] with page_note saying what the mentions are.

## Each row
- `editor`: "post_content" (raw, non-Elementor), "elementor" (text inside `_elementor_data`), "manual" (needs the Elementor
  editor: deleting a whole button/form/section widget), or "rank_math" (title/description).
- `action`: "replace", "delete" (after = ""), "insert_after" (before = the anchor text, after = anchor text + inserted HTML), "manual".
- `before`: an EXACT substring of the stored string (content.raw, or the stored `_elementor_data` string with its `\/` and `\"`
  escapes exactly as stored). It must occur exactly ONCE in that string: check with python `s.count(before) == 1`. Keep it as
  short as uniqueness allows (normally the sentence). For elementor rows prefer ASCII-only spans.
- `after`: the same string with only the needed change, in the same escaping. Keep grammar, keep every informational word.
- `needs_sharad`: true for H1, SEO title, slug, meta description, and anything in the case study or Best page that is about the firm.
- `location`: Visible | JSON-LD | Button | Form | Meta; `section`: short description (hero, FAQ 3, sidebar CTA...).
- For a "manual" row: `before` = the widget's visible text, `after` = "", `note` = widget type and where it sits, so a person can find it.

For dedicated IDs (`A-ids.txt`) also add ONE "insert_after" row for the notice from RULES.md (calculator wording for the 2
calculators), placed right after the first intro paragraph under the H1. Use `<p class="sred-notice"><strong>...</strong></p>`.

## Output
One JSON file per ID: `/home/user/gondaliyacpa/sred-informational/audit/<id>.json`:
{"id":123,"url":"...","title":"...","type":"page|post|elementor_library","elementor":true,"rows":[{"location":"","section":"","editor":"","action":"","before":"","after":"","needs_sharad":false,"note":""}],"page_note":""}

Final answer: one line per ID: `id | elementor y/n | rows | manual rows | needs_sharad rows`. Under 200 words.
