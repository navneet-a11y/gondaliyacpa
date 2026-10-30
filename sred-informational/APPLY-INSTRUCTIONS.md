# SR&ED informational: apply the audited changes (WRITES TO THE LIVE SITE)

Folder: `/home/user/gondaliyacpa/sred-informational/`. Rules: `RULES.md`. Audit rows: `audit/<id>.json`.
Navneet asked for these changes and Sharad approved the approach. Apply ONLY what `plan.py` produces:
never edit a row, never write your own wording, never touch a row flagged needs_sharad, manual or rank_math.
Tools: `mcp__gondaliya_cpa__*` (load with ToolSearch "select:..."). Work files go in your own subfolder of the
scratchpad (`.../scratchpad/<your batch name>/`); other agents share the scratchpad.

## For each `<id> <post_type>` line in your batch file, in order

1. Fetch fresh: `wp_get_post_full` id, post_type (the second word: pages / posts / elementor_library), context "edit",
   include ["meta"], meta_keys ["_elementor_edit_mode","_elementor_data"]. Note the path of the saved result file
   (if the result comes back inline, save it to a file yourself exactly as returned).
2. Plan: `python3 plan.py <id> <result_file>` writes `apply/ops/<id>.json`. If it errors, skip the page and report.
3. Apply each op in order.

### editor "post_content"
`wp_replace_in_post`: id, field "post_content", search = op.search, replace = op.replace, regex = op.regex,
max_replacements 1. `replacements_count` must be 1. If 0, stop this page and report.

### editor "elementor"
`wp_privileged_search_replace_run` with old = op.search, new = op.replace.
- First, once per page: a dry run (dry_run true, log true) of the page's LONGEST op. Its log rows show
  `wp_postmeta.meta_value:<meta_id>` rows. That set of meta ids is the page's own set (normally 1 to 3: live data,
  revision, element cache). If any wp_posts row other than `wp_posts.post_content:<id>` appears, or more than 3 meta
  rows appear, stop this page and report.
- Each op: dry run (dry_run true, log true). Apply with the SAME old/new and dry_run false only if every log row is in
  the page's own meta id set or is `wp_posts.post_content:<id>`, and at least one meta row matched. If another page's
  row matches too, do NOT apply: record the op as "shared" (row number, other row ids) and go on to the next op.
  If `log_more` > 0, treat it as shared.

4. Verify: fetch again (step 1) and run `python3 check.py <id> <result_file>`. MATCH is expected when nothing was
   skipped or shared; otherwise report DIFFERS with the reason.
5. `wp_clear_cache` scope "posts", post_ids [id] (up to 50 ids per call, so you can batch this at the end).

## Log
Append one JSON line per page to `apply/log-<batch>.jsonl`:
{"id":..,"editor":..,"ops":n,"applied":n,"shared":[{"row":..,"rows":[..]}],"failed":[..],"check":"MATCH|DIFFERS|-"}

Final answer: one line per page `id | applied/ops | shared | check`, then any problems. Under 250 words. Do not commit.
