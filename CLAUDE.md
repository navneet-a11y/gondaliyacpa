# Working on the live WordPress sites

gondaliyacpa.ca, haribusinesstax.ca and the other sites on this Hostinger plan share one CPU and memory limit. Heavy work on any one of them can slow down or take down all of them (503 errors).

## Rules for edits through the WordPress MCP tools

- **Never clear the cache.** Do not call `wp_clear_cache` with any scope (site, posts or a single post). LiteSpeed Cache already purges each page automatically when it is saved. A full purge forces every page to be rebuilt at once and pushed the plan to 100% CPU and its memory limit on 2 Nov 2026. This tool is blocked in `.claude/settings.json`.
- **Edit one post at a time.** Do not run edits in parallel.
- **Work in batches of 10 pages, then pause** before the next batch.
- **Search-and-replace:** always run `wp_privileged_search_replace_run` with `dry_run: true` first and report the match count. Before a real run that would change more than 20 posts, ask the user and suggest running it in the evening or at night (Toronto time), when traffic is lowest.
- **Large bulk jobs** (more than 50 pages) should run in the evening or at night, Toronto time.
- If tool calls that normally take under a second start taking several seconds, the server is overloaded. Stop and tell the user before continuing.
