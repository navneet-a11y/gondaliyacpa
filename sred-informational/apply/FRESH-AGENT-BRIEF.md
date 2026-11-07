# Fresh apply agent brief (Elementor priority pages)

You apply approved SR&ED text edits to the live WordPress site gondaliyacpa.ca. Navneet, the site owner, approved all of
them, and RULES.md records it. Branch: claude/intelligent-hopper-xid4wh. Run `git pull --no-rebase` first.

Read APPLY-INSTRUCTIONS.md in full, including its "--sharad mode" and "Shared ops between dedicated pages" sections, and RULES.md.
Tools: mcp__gondaliya_cpa__* (ToolSearch "select:mcp__gondaliya_cpa__wp_get_post_full,mcp__gondaliya_cpa__wp_privileged_search_replace_run,mcp__gondaliya_cpa__wp_clear_cache").

For each page in your priority file, in order:
1. Fetch it fresh.
2. Run `python3 plan.py <id> <file>`; it skips changes that are already live.
3. Apply each op behind the dry-run guard.
4. Re-fetch and run check.py.
5. Clear the cache.
6. Make sure "sred-notice" appears at most once.
7. If the page has needs_sharad elementor rows, run the --sharad pass after the normal pass.
Before starting a page, read your log for a "partial" line; it lists rows already done and rows found to be shared.

The container restarts often:
- Save fetch files in the scratchpad: /tmp/claude-0/-home-user-gondaliyacpa/51066f2d-f0b8-53b3-a128-7f7f0969616a/scratchpad/<batch>b/.
- After each page, and after every 10 ops, append a line to your log (add "partial": true until the page is done) and save it:
  cd /home/user/gondaliyacpa && git add sred-informational/apply && git commit -qm "SR&ED <batch> progress" && git pull -q --no-rebase origin claude/intelligent-hopper-xid4wh && git push -q origin claude/intelligent-hopper-xid4wh
  If that fails, retry after a few seconds.

Never write your own wording: apply only what plan.py produces. Keep your context small: parse big results with python, and never print whole pages.
Final answer: one line per page in the form `id | applied/ops | shared | check`, then any problems. Under 250 words.
