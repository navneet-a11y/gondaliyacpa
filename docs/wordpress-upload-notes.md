# Uploading a built page to WordPress

Built pages run past 110KB, which is beyond what a single `wp_create_page` call
reliably carries. What follows is what many batches established, including one
silent content loss and one container loss.

## Count bytes, not characters

`wp_replace_in_post` returns `content_length_after` as a **byte** count. The
chrome CSS contains multibyte glyphs, so a character offset computed in Python
will not match. Compute from `len(chunk.encode('utf-8'))`, and add the
sentinel's own byte length to every intermediate assertion.

## The method that works

1. **Single call when the content fits.** Nothing to go wrong at a boundary.
2. **When it does not fit:** create the page with one short plain-text sentinel
   as its entire content, then swap sentinel-for-chunk with successive
   `wp_replace_in_post` calls on `post_content`. Ten chunks is routine.
3. **Never use an HTML comment as the sentinel.** Use a plain-text token such as
   `VCFCHUNKMARKER01`. Confirm afterwards that no sentinel survives.
4. **Pre-compute the whole byte ledger before the first call** and assert
   `content_length_after` after every call. That localises a loss to the chunk
   that caused it instead of surfacing it as a mystery shortfall at the end.

## The comment-boundary rule has to look through blank lines

A split must not land adjacent to an HTML comment — the one silent content loss
in this project was a 35-byte comment lost at a boundary, which no word count
would ever have caught. Checking only the last line of a chunk and the first
line of the next is **not enough**: a boundary can land on a *blank* line that
is itself followed by a comment, which passes a naive adjacency test while being
the riskiest split on the page. That is exactly where a one-byte loss happened.

Treat a blank line as transparent and look through it to the next non-blank
line. Test the last non-blank line of the accumulated chunk and the next
non-blank line of the remainder.

The injected FAQ schema is one unbreakable line of roughly 12KB. Let a chunk
exceed the size target rather than split beside a comment.

## When a call errors or rate-limits with no confirmed result

The write may already have landed. **Do not blind-retry** — replaying a chunk
applies it twice. Probe with a no-op replace (sentinel for itself) and read
`content_length_after`. If it equals that chunk's target the write succeeded;
continue from the next chunk. If it equals the previous target, re-send safely.

## Resuming an upload that was killed mid-chunk

1. Probe the length with a no-op replace; subtract the sentinel's byte length.
2. **Do not trust that number alone.** Take the last ~120 bytes of the local file
   at that offset, append the sentinel, and run a no-op replace with that as the
   search string. `replacements_count` of exactly 1 proves the stored prefix ends
   on precisely that byte. A matching length alone does not.
3. Only then split the remainder and resume.

## `wp_replace_in_post` has no dry run

There is **no `dry_run` parameter**. The tool declares only `id`, `field`,
`search`, `replace`, `regex` and `max_replacements`, and it accepts unknown keys
silently instead of rejecting them — so a call passing `dry_run: true` executes
as a normal write and the flag is discarded without a warning.

A probe is therefore only safe when `replace` is **byte-identical** to `search`.
That is the whole reason the sections above say "no-op replace (sentinel for
itself)": the safety comes from the two strings matching, never from a flag.

This cost a live page. A probe shaped as `search: '<h1>[^<]{0,200}</h1>'`,
`replace: 'X'`, `regex: true`, `dry_run: true`, intended to read page 47834's H1,
instead deleted it — 108,780 bytes to 108,690. Recovery path, in order:

1. `wp_list_revisions` was no help. WordPress saves the revision *after* the
   update, so the only revision held the damaged body.
2. `wp_history_list` with `object_id` found the MCP write, and
   `wp_history_get` on that row carries `content_before` (pre-change) alongside
   `revision_content` (post-change).
3. That payload overflows context, so let the harness spill it to disk and pull
   the original out with Python rather than reading it in. A
   `difflib.SequenceMatcher` over the two fields prints the exact opcode, which
   is what proves only one span changed.
4. Restore with a unique anchor spanning the wound — the surrounding markup plus
   the damaged byte — not the bare damaged byte, which recurs all over the body.
5. Confirm the stored length returns to the logged original exactly.

Never read a value by writing over it. If a page's text is needed, fetch the
page and grep the spilled file.

## Verifying what landed

- Read back with `wp_get_post_full`, `post_type: "pages"`, **`context: "edit"`**.
  The default `view` context returns `content.rendered`, which differs by
  `wpautop` paragraph tags and `wptexturize` curly quotes. Comparing against it
  produces false alarms.
- The post is nested under a `post` key: `content.raw` is at
  `data["post"]["content"]["raw"]`.
- **Assert the returned `id` and `slug` before trusting anything.** Concurrent
  agents share a scratchpad and a collision has produced a diff against the
  wrong page, which is worse than a false failure.
- When the readback overflows context and the harness spills it to disk, parse
  `content.raw` out with Python straight to a file. **Prefer this** — it keeps
  hand transcription out of the verification path, and the only real content
  error in this project came from retyping a page by hand.
- Save to a page-id-scoped filename. **Never `live.html`.**
- Compare **byte-for-byte** by hash, and compare HTML comment counts. A word
  count match is not sufficient.
- Re-run `scripts/verify_industry_page.py` on the extracted file.

## Publishing

Re-probe each page *after* the status change, not only before. The write path's
sanitizer is where bytes have gone missing, so confirm the stored length and the
H1 are unchanged once the page is live.

## Keep the repository pushed

74 commits were lost when a container was reclaimed while `git push` was
returning 403. The published pages survived on the live site; the sources,
briefs, spines, scripts and chrome did not. Push after every batch.

## WordPress escapes `<` as `\x3c` inside `<script>` blocks

The byte ledger can legitimately drift **upward by 3 bytes per `<`** that sits
inside a JavaScript string literal in a `<script>` block. WordPress (or the
Easy MCP AI sanitiser) rewrites those as `\x3c`, so

    innerHTML='<div class="sb-quiz-bar"><span ...></span></div>'

is stored as

    innerHTML='\x3cdiv class="sb-quiz-bar">\x3cspan ...>\x3c/span>\x3c/div>'

**This is benign and must not be "corrected".** In a JS string literal `\x3c`
is exactly `<`, so the readiness-quiz widget renders and behaves identically;
the escaped form is the safer one, since it cannot terminate the script tag
early. Writing the raw `<` back only invites the sanitiser to redo it.

Two consequences worth remembering:

- The drift does **not** appear on every page, and may land on a *later* save
  rather than on the write that introduced the script. On the trade-schools
  page it appeared between the chunk-2 and chunk-3 writes (across an MCP
  reconnect); on the health-and-safety page it never appeared at all and the
  final length matched the local file exactly.
- It also lowers the `<div` and `</div>` counts, because `\x3cdiv` and
  `\x3c/div>` no longer match those literals. A div count that is short by one
  or two with a positive byte drift is this, not lost markup.

**Diagnosing a drift properly.** Do not reach for `difflib.SequenceMatcher` on
a 100KB+ body; it does not finish. Fetch the page with `wp_get_page` (the
harness spills an oversized result to a file), then find the common prefix and
common suffix in a single O(n) pass and print only the divergent slice between
them. That localises any drift to a handful of characters immediately.
