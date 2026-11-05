# Publish edited page content to wealthscale.ca (update existing pages)

Load the tools first with ToolSearch: `select:mcp__wealthscale_ca_WordPress__wp_update_page,mcp__wealthscale_ca_WordPress__wp_rest_read`.
Use only the mcp__wealthscale_ca_WordPress__* tools (never gondaliya_cpa, opencorp or corpnil). Touch no other page, setting, snippet or Rank Math field.

Your job file (JSON list) is named in your prompt. Each entry: no, page_id, file, md5, len. For each entry, in order:

1. Read the file exactly with Bash, in chunks of 20000 characters, never with the Read tool:
   `python3 -c "import sys;d=open(sys.argv[1]).read();print(len(d));sys.stdout.write(d[int(sys.argv[2]):int(sys.argv[3])])" FILE START END`
   Keep every character, including backslash-escaped quotes in the JSON-LD script.
2. content = `<!-- wp:html -->` + newline + file text with trailing newline(s) removed + newline + `<!-- /wp:html -->`. Nothing else.
3. `wp_update_page` with `page_id` and `content` ONLY. Do not pass title, slug, parent, status or meta.
4. Verify: `wp_rest_read` route `/ws-check/v1/md5`, query `{"ids":"<page_id>"}`. md5 and len must equal the job's md5 and len, status publish. On mismatch, re-read the file and redo step 3 (same page_id), up to 2 retries.
5. If a safety system stops or interrupts you on an entry, do not retry it; report it FAILED with what happened and continue with the next entry.

Report one line per entry: `no | page_id | OK` or `no | page_id | FAILED: <what differs>`.
