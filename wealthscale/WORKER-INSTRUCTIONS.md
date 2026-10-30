# Worker instructions: replace WealthScale pages on the live site

You publish a fixed list of pages to wealthscale.ca through the `mcp__wealthscale_ca_WordPress__*` tools.
Load them first with ToolSearch: `select:mcp__wealthscale_ca_WordPress__wp_update_page,mcp__wealthscale_ca_WordPress__wp_create_page,mcp__wealthscale_ca_WordPress__wp_rest_write,mcp__wealthscale_ca_WordPress__wp_rest_read`.

Your job file (JSON list) is named in your prompt. Do the entries in order. Touch NO other page, redirect, snippet or setting.

## For each entry

1. **Read the file exactly.** Use Bash to print it in chunks, never the Read tool (Read truncates long lines):
   `python3 -c "import sys;d=open(sys.argv[1]).read();print(len(d));sys.stdout.write(d[int(sys.argv[2]):int(sys.argv[3])])" FILE START END`
   in steps of 20000 characters until you have the whole file. The JSON-LD `<script>` at the end has very long lines; keep every character, including backslash-escaped quotes (`\"`).
2. **Build content** = `<!-- wp:html -->` + newline + the file text with its trailing newline(s) removed + newline + `<!-- /wp:html -->`. Nothing else, no extra spaces, no changes, no "fixes".
3. **Write the page.**
   - `page_id` is a number: `wp_update_page` with `page_id`, `title`, `content`, `parent` = `parent_id`, `slug`, `status: "publish"`.
     Exception: when `url` is `/` (home page) do NOT pass `slug`.
   - `page_id` is null: `wp_create_page` with `title`, `content`, `parent` = `parent_id`, `slug`, `status: "publish"`. If the result status is not `publish`, call `wp_update_page` on the new id with `status: "publish"`. Record the new id.
4. **Rank Math.** `wp_rest_write` route `/rankmath/v1/updateMeta`, body
   `{"objectType":"post","objectID":<id>,"meta":{"rank_math_title":<seo_title>,"rank_math_description":<meta_description>,"rank_math_focus_keyword":<focus_keyword>}}` with the exact strings from the job file.
5. **Verify.** `wp_rest_read` route `/ws-check/v1/md5`, query `{"ids":"<id>"}`. It must show `md5` == job `md5`, `len` == job `len`, `seo_md5` == job `seo_md5`, `status` publish, `slug` == job slug (home: `home`), `parent` == `parent_id`.
   - On an md5/len mismatch: re-read the file chunks carefully and redo step 3 (update the same id; never create a second page). Up to 2 retries.
   - On seo_md5 mismatch: redo step 4.
6. Move on to the next entry.

## Report back
One line per entry: `no | id | OK` or `no | id | FAILED: <what differs>`. For created pages give the new id. Nothing else.
