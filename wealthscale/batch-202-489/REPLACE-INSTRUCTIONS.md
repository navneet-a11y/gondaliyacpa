# Replace live WealthScale pages (content + Rank Math)

Load tools first with ToolSearch: `select:mcp__wealthscale_ca_WordPress__wp_update_page,mcp__wealthscale_ca_WordPress__wp_rest_write,mcp__wealthscale_ca_WordPress__wp_rest_read`.
Use only mcp__wealthscale_ca_WordPress__* tools (never gondaliya_cpa, opencorp or corpnil). Touch no other page, setting, menu, snippet or redirect.

Your job file (JSON list) is named in your prompt. Each entry: no, page_id, file, md5, len, seo_title, meta_description, focus_keyword, seo_md5. For each entry, in order:

1. Read the file exactly with Bash in chunks of 20000 characters, never with the Read tool:
   `python3 -c "import sys;d=open(sys.argv[1]).read();print(len(d));sys.stdout.write(d[int(sys.argv[2]):int(sys.argv[3])])" FILE START END`
   Keep every character, including backslash-escaped quotes inside the JSON-LD script.
2. content = `<!-- wp:html -->` + newline + the file text with trailing newline(s) removed + newline + `<!-- /wp:html -->`. Nothing else.
3. `wp_update_page` with `page_id` and `content` ONLY (no title, slug, parent, status or meta).
4. `wp_rest_write` route `/rankmath/v1/updateMeta`, body `{"objectType":"post","objectID":<page_id>,"meta":{"rank_math_title":<seo_title>,"rank_math_description":<meta_description>,"rank_math_focus_keyword":<focus_keyword>}}` with the exact strings from the job.
5. Verify: `wp_rest_read` route `/ws-check/v1/md5`, query `{"ids":"<page_id>"}`: md5, len and seo_md5 must equal the job's, status publish. On an md5/len mismatch re-read the file and redo step 3 (same page_id), up to 2 retries; on a seo_md5 mismatch redo step 4.
6. If a safety system stops or interrupts you on an entry, do not retry it; report it FAILED with what happened and continue.

Report one line per entry: `no | page_id | OK` or `no | page_id | FAILED: <what differs>`.
