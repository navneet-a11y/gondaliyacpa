# Open Corporation for $35: house format for blog posts

The reference post is "When Does Incorporating Actually Save Tax in Canada?" (September 2026). `template.html` is that post with the content swapped for `{{PLACEHOLDERS}}`. Paste it into one Custom HTML block in WordPress.

## Page order

| # | Block | Required |
|---|---|---|
| 1 | `<style>` block (all `.gcpa-*` classes) and the Organization JSON-LD | Yes |
| 2 | Hero: strip of 4 or 5 keywords and the year, H1, a one-line subtitle, "By Sharad Gondaliya, CPA" with links to the home page and Address Service, and the department line | Yes |
| 3 | H2 with the focus keyword, then an opening paragraph that starts with "**Open Corporation for $35 is a department of Gondaliya CPA.**" | Yes |
| 4 | Quick Summary (`id="toc-summary"`): a short paragraph and a two-column Aspect/Details table | Yes |
| 5 | Author box (top), then the reading time | Yes |
| 6 | Table of Contents: one entry per numbered section | Yes |
| 7 | "The Numbers That Matter" metric cards, 4 or 5, with the $35 fee as the last card | Optional |
| 8 | Scope & Assumptions callout (blue): province, year, CAD, what can change, and "not advice" | Yes |
| 9 | Numbered sections: an SEO H2, then a `gcpa-numhead` (number, H4 with the `toc-` anchor, coloured topic label). Use H3 or `gcpa-pillhead` for sub-sections | Yes |
| 10 | Callouts inside sections: Our Actual Experience (gold), Key Stat (teal), Worth Knowing (blue), Watch For (red), Tip (green) | 2 or more |
| 11 | In-body infographics in a `<figure>` with alt text and a short caption | 3 |
| 12 | Mid-post banner (`gcpa-banner`), once | Yes |
| 13 | CTA box (`gcpa-cta`) about two-thirds of the way down | Yes |
| 14 | FAQ as its own numbered section (`id="toc-faq"`) with collapsible `<details>` boxes | Yes |
| 15 | Closing numbered section: the honest answer to the title, "Quick Answers" list, "Who This Is For / Not For", "People Also Ask" | Yes |
| 16 | Verdict callout (green) | Yes |
| 17 | Readiness Check widget (six yes/no questions; no tax calculated) | Optional |
| 18 | Checklist PDF download link, then the "Why choose us" image | Optional |
| 19 | Closing CTA box (trust badges include 60-Day Fee Matching) | Yes |
| 20 | "What to Send Us" (`gcpa-closing`) | Yes |
| 21 | Author box (bottom) | Yes |
| 22 | Footer: published and updated dates, editorial policy, disclaimer, department line, operator line (WealthBamboo Inc., phone, hours, Interac e-Transfer to info@gondaliyacpa.ca, security question "Not Applicable") | Yes |
| 23 | BlogPosting and FAQPage JSON-LD; the FAQ text must match block 14 word for word | Yes |

## Assets for each post

| Asset | Size | Upload path | Notes |
|---|---|---|---|
| Featured image | 1536 x 1024 | `/wp-content/uploads/YYYY/MM/` | Navy background, keyword strip, H1, subtitle, three badges (white, teal, gold), photo of Sharad, "Written by" and published date, logo, "opencorporationfor35.ca \| Backed by Gondaliya CPA" |
| Infographic 1 to 3 | 1200 x 675 | `{slug-short}-{topic}.png` | Navy title bar with a coloured rule, one idea per image, footer with logo and the same domain line |
| Why choose us | 1200 x 675 | `why-choose-us-{slug-short}.png` | Six cards: run the numbers first, department of Gondaliya CPA (61330051), from $35 including HST, a topic-specific point, filed same day remotely, 30-day money-back plus 60-day fee matching |
| Checklist PDF | Letter, 2 pages | `OpenCorp35-{Topic}-Checklist.pdf` | 8 numbered sections, a booking prompt at the end, and the department, contact and "not advice" footer on every page. Example in `examples/` |

## Rules

- Use "Open Corporation for $35 is a department of Gondaliya CPA." in the hero, the opening, both author boxes and the footer.
- Use exact numbers only, never ranges or "about" (53.53%, not "about 53.5").
- Quote fees one way only: "$35 including HST, plus government fees".
- Use "please" in every CTA paragraph.
- Use one booking link: https://gondaliyacpa.ca/consultation/
- Before publishing, check every figure against the current CRA or registry source, and check the figure printed on the images too.
- Any "Risk Warning" or "House Style" callouts in a draft are review notes. Remove them before publishing.
- Set the Rank Math title to the H1 and the Rank Math description to the excerpt.
