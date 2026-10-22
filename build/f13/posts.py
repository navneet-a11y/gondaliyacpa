# -*- coding: utf-8 -*-
"""Family 13 blog posts, written to the Section 7.6 drafting brief.

Both titles come from Section 7.8, the plan's first 40 post titles, and both
were checked against the 20 live /answers/ pages and 12 live /guides/ so
neither duplicates a URL that already exists.

Brief compliance, line by line:
  7.6  answer in the first 40 words, one H1 (rendered by the theme from the
       post title), H2s that are questions a reader types, 900 to 1,400 words,
       every numeric or comparative item in a table with an exact number in
       every cell and a Notes column, no external links, no citations, no
       "e.g.", no "such as", Canadian spelling.
  1221 one original table or one original checklist per post. No exceptions.
  1771 six internal links per post.
  7.5  two byline lines under the H1, then the Last reviewed line.
  1590 the copy-paste qualification sentence, verbatim, wherever a penalty is
       mentioned. Post one mentions penalties; post two deliberately does not.
  393  the mandatory-electronic-filing wording, both figures stated together.

Price wording follows Navneet's standing correction, "plus HST", not the
plan's "including HST". Logged in docs/decisions.md.
"""
import io, json, os

SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
TODAY, ISO = 'October 22, 2026', '2026-10-22'

BYLINE = ('<p class="cnf-by">Written by <a href="%s/sharad-gondaliya-cpa/">Sharad '
          'Gondaliya, CPA</a></p>\n'
          '<p class="cnf-by">Reviewed by <a href="%s/sharad-gondaliya-cpa/">Sharad '
          'Gondaliya, CPA (Ontario)</a>, CPA Ontario Membership 61040184.</p>'
          % (SITE, SITE))

# line 1590, verbatim. Never shortened, never paraphrased.
QUAL = ('A true nil return carries no percentage late-filing penalty, because that '
        'penalty is a percentage of tax owing and the corporation owes $0.00. The '
        'unfiled year still stays open forever, invites a demand to file and an '
        'arbitrary assessment, blocks a clearance certificate and dissolution, and '
        'costs a non-resident-owned corporation $25.00 per day up to $2,500.00.')

# line 393, both figures together.
EFILE_RULE = ('For tax years starting after 2023 electronic filing is mandatory for '
              'virtually all corporations. A paper T2 draws a $1,000.00 penalty plus '
              'a $100.00 per-return preparer penalty.')

CSS = """<style>
.cnf-post{max-width:1100px!important;margin:0 auto;padding:0 20px;font-family:Lato,sans-serif;color:#333;font-size:17px;line-height:1.75}
.cnf-post h2{font-family:Poppins,sans-serif;color:#314d8a;font-size:25px;font-weight:600;margin:38px 0 12px;line-height:1.3}
.cnf-post p{margin:0 0 16px}
.cnf-post a{color:#314d8a;font-weight:600}.cnf-post a:hover{color:#2087c9}
.cnf-post .cnf-by{font-size:15px;margin:0 0 2px;color:#4a5568}
.cnf-post .cnf-rev{font-size:15px;color:#636363;margin:6px 0 22px}
.cnf-post .cnf-lead{font-size:19px;line-height:1.7;color:#1a2340;font-weight:600;border-left:5px solid #2087c9;background:#f5f8fc;border-radius:0 8px 8px 0;padding:16px 20px;margin:0 0 26px}
.cnf-post table{width:100%;border-collapse:collapse;font-size:16px;margin:0 0 18px}
.cnf-post th,.cnf-post td{border:1px solid #dfe6ef;padding:11px 13px;text-align:left;vertical-align:top}
.cnf-post th{background:#314d8a;color:#fff;font-family:Poppins,sans-serif;font-weight:600}
.cnf-post td:nth-child(2){font-weight:700;color:#314d8a}
.cnf-post .cnf-check{background:#f5f8fc;border-left:5px solid #314d8a;border-radius:0 8px 8px 0;padding:18px 22px;margin:0 0 18px}
.cnf-post .cnf-check ul{margin:0;padding-left:20px}
.cnf-post .cnf-check li{margin:0 0 9px}
.cnf-post .cnf-qual{background:#fff8ec;border-left:5px solid #d49b2a;border-radius:0 8px 8px 0;padding:16px 20px;margin:0 0 18px;font-size:16px}
.cnf-post .cnf-cta{background:#314d8a;border-radius:10px;padding:24px 26px;margin:30px 0 0;text-align:center}
.cnf-post .cnf-cta p{color:#fff;margin:0 0 14px;font-size:17px}
.cnf-post .cnf-cta a{display:inline-block;background:#2087c9;color:#fff!important;padding:14px 32px;border-radius:30px;font-family:Poppins,sans-serif;font-weight:600;text-decoration:none!important}
@media(max-width:767px){.cnf-post h2{font-size:21px}}
</style>"""


def wrap(body, slug, title, desc):
    url = SITE + '/blog/' + slug + '/'
    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "Article", "@id": url + "#article", "headline": title,
       "description": desc, "url": url, "inLanguage": "en-CA",
       "datePublished": ISO, "dateModified": ISO,
       "author": {"@type": "Person", "name": "Sharad Gondaliya",
                  "honorificSuffix": "CPA", "url": SITE + "/sharad-gondaliya-cpa/"},
       "reviewedBy": {"@type": "Person", "name": "Sharad Gondaliya",
                      "honorificSuffix": "CPA",
                      "url": SITE + "/sharad-gondaliya-cpa/"},
       "publisher": {"@id": SITE + "/#accountingservice"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
         "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": title, "item": url}]}]}
    return ('<!-- wp:html -->\n' + CSS + '\n<div class="cnf-post">\n' + BYLINE
            + '\n<p class="cnf-rev">Last reviewed: ' + TODAY + '</p>\n' + body
            + '\n<div class="cnf-cta"><p>Nil T2 filing is $300.00 plus HST per tax '
              'year, CPA reviewed and transmitted electronically.</p>'
              '<a href="' + FORM + '">Start Nil T2 Filing NOW</a></div>\n</div>\n'
            + '<script type="application/ld+json">' + json.dumps(schema) + '</script>\n'
            + '<!-- /wp:html -->')
