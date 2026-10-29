# Change 4: Review markup about our own firm

Dry run: Thursday, October 29, 2026. **Nothing has been edited yet.**

## What I found

| Source | Finding |
|---|---|
| Inline JSON-LD in page and post content | **617 published pages and posts** contain "AggregateRating" in their content. Most are the niche industry pages, plus many blog posts. Example from page 57966, /accountant-for-employment-agencies/: `"aggregateRating":{"@type":"AggregateRating","ratingValue":"5.0","reviewCount":"1381"}` inside an `AccountingService` node. The count (1381) is out of date and differs from the 1,450+ line. Per your decision I'm removing the node, not updating the count. |
| Rank Math schema templates (Schemas post type) | **0 templates.** So the rating isn't coming from a Rank Math template. Still to check: per-post Rank Math schema saved in post meta, and the Local SEO knowledge-graph settings. |
| Trustindex (Widgets for Google Reviews 14.2) | The plugin's REST routes don't expose the schema setting, so **this needs a click in wp-admin**: Trustindex › Widget › turn off "Display rich snippet / schema". |
| Elementor HTML widgets and templates | The same JSON-LD is also stored escaped inside `_elementor_data` (post meta). The search and replace must cover `wp_postmeta` as well as `wp_posts`. |
| Header and footer code | Still to check: WPCode Lite snippets, Elementor Custom Code (`elementor_snippet`) and Astra hooks (`astra-advanced-hook`), for a sitewide rating or review node. |

## Planned run (after the backup, with the privileged tool switched on)

1. **Dry run, plain JSON:** a regex dry run with log on `wp_posts.post_content`. It removes `,"aggregateRating":{...}` (and the variant where the field comes first and is followed by a comma). Pattern: `,\s*"aggregateRating"\s*:\s*\{[^{}]*\}`. I'll also search separately for `"@type":"Review"` and `"review":[` to see whether any individual Review nodes exist.
2. **Dry run, escaped JSON:** the same in `wp_postmeta.meta_value` for `_elementor_data`, with the JSON-escaped pattern `\\"aggregateRating\\"`.
3. **Send you the counts:** cells and occurrences per table, plus about 20 before and after samples, so you can check that no other JSON is broken.
4. **Live run, then verify:** run it live, then:
   - regenerate Elementor CSS and data
   - do a full LiteSpeed purge
   - test 10 templates in Google's Rich Results Test, logging each result in the change log: home, /about-us/, a service page, a city page, a niche "accountant-for-" page, a blog post, a calculator, a Best/Top page, /contact-us/ and /team/sharad-gondaliya-cpa/
5. **Trustindex schema switched off by hand** (above).

## Needs you

- The UpdraftPlus backup (database and files) before step 4.
- Switch on Easy MCP AI › Settings › Advanced › Disabled tools › **Privileged** (for the search and replace).
- The Trustindex schema toggle in wp-admin. I can't reach it through the API.
- The Rich Results Test has to run from a browser. This container can't reach gondaliyacpa.ca directly: the outbound proxy refused the connection.
