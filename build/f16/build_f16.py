"""Family 16 hub: /guides/

  line 1154   F16 is 5 hubs on post type `page`: /services/, /tools/,
              /locations/, /guides/, /blog/. "Each hub links every child in
              its family."
  line 1224   GATE: "No hub publishes without a live child count and links to
              every child family." Unique data block is the "Live child count
              for that family", sourced from a "WordPress query count, cached
              hourly by LiteSpeed Cache", and "Child counts update
              automatically and are never hand-typed." Banned phrase for this
              family: "complete list of every accountant".
  line 350    Intended template is a Loop Grid. Theme Builder is unproven on
              this install, so the child list is written by the pipeline and
              the count is a shortcode. See the note below.
  6(g) F16    20 inbound minimum, 400 outbound maximum, mandatory targets
              "Every child family", anchor "Child title". Hubs are exempt from
              the 40-link body cap.
  7.9 1570    F16 takes its visible date in the footer of the article body.

The count is NOT written into the HTML. `[cnf_child_count type="nil_guide"]`
renders it from a live wp_count_posts call, because line 1224 forbids a
hand-typed number. The shortcode is registered by the WPCode snippet in
docs/hub-child-count-snippet.md, which must be installed before this page
renders correctly.

Appendix A conflict. Appendix A's Family 16 names five entirely different
hubs: /what-we-file/, /who-this-is-for/, /provinces/, /all-calculators/ and
/service-areas/. 6(a) is followed here, corroborated by the 6(g) Home row,
which names the same five as the home page's mandatory targets.
"""
import json, os

SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
URL  = SITE + '/guides/'
TODAY = 'October 16, 2026'
PRICE = '$300.00 plus HST per tax year'

TITLE = 'Nil T2 Filing Guides for Canadian Corporations'
H1    = 'Nil T2 Filing Guides'
META  = ('In-depth guides to filing a nil T2 corporate return in Canada, written and '
         'reviewed by a CPA Ontario member. Nil T2 filing is ' + PRICE + '.')
BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')

# Children: every published nil_guide. Written by the pipeline, re-run when a
# guide is added. The COUNT above it is live; this list is generated.
GUIDES = [
 ('nil-t2-return-complete-guide', 'The Complete Guide to the Nil T2 Return',
  'Who must file, what counts as nil, which GIFI schedules and other schedules are '
  'required, how Form T183CORP is signed, filing deadlines, and what unfiled years '
  'cost.'),
]

RELATED = [
 (SITE + '/deadlines/', 'T2 Filing Deadlines',
  'Every fiscal year-end and its due date, with the business-day rule.'),
 (SITE + '/pricing/nil-t2-filing-cost/', 'Nil T2 Filing Cost',
  'What ' + PRICE + ' covers, and what falls outside a nil return.'),
 (SITE + '/catch-up-nil-t2-filing/', 'Catch-Up Nil T2 Filing',
  'Filing several outstanding years at once, each as its own return.'),
]

CSS = """<style>
.ei-wrap{max-width:1100px;margin:0 auto;padding:0 20px}
.ei-btn-blue{background:rgba(32,135,201,1);color:#fff !important;padding:13px 26px;border-radius:6px;font-weight:700;font-size:0.95em;text-transform:uppercase;text-decoration:none !important;display:inline-block;line-height:1.4;text-align:center;min-width:120px}
.ei-section{padding:26px 20px}
.ei-section-alt{background:#f7f9fc;padding:26px 20px}
.ei-art .ei-h2{font-weight:800;color:#1a2340;margin:0 0 10px;font-size:1.45em;line-height:1.3}
.ei-art > *:last-child{margin-bottom:0}
.ei-art p{color:#4a5568;line-height:1.8}
.ei-art a{color:rgba(32,135,201,1)}
.ei-hero{background:linear-gradient(135deg,#0f1624 0%,#1a2340 55%,#1e3a6e 100%);padding:40px 20px}
.ei-hero-inner{max-width:860px;margin:0 auto;text-align:center}
.ei-hero-eyebrow{display:inline-block;background:rgba(32,135,201,0.15);border:1px solid rgba(32,135,201,0.4);border-radius:50px;padding:5px 16px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:rgba(32,135,201,1);margin-bottom:16px;font-size:.8em}
.ei-hero h1{color:#fff;font-weight:800;line-height:1.2;margin:0 0 14px;font-size:2.1em}
.ei-hero-sub{color:rgba(255,255,255,0.78);max-width:720px;margin:0 auto 10px;line-height:1.75}
.ei-hero-by{color:rgba(255,255,255,0.6);max-width:720px;margin:0 auto 22px;line-height:1.6;font-size:.86em}
.ei-hero-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.ei-hero-btns a,.ei-hero-btns a:visited,.ei-hero-btns a:hover,.ei-cta-bottom a,.ei-cta-bottom a:visited,.ei-cta-bottom a:hover{color:#fff !important;text-decoration:none !important}
.ei-count{display:inline-flex;align-items:baseline;gap:8px;background:#f0f7fd;border:1px solid #cfe4f6;border-radius:50px;padding:6px 16px;margin:0 0 14px;color:#1a2340;font-size:.9em}
.ei-count b{color:rgba(32,135,201,1);font-size:1.15em;font-weight:800}
.ei-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;margin:16px 0 0}
.ei-card{border:1px solid #e2e8f0;border-radius:10px;background:#fff;padding:18px 20px;transition:box-shadow .15s ease,border-color .15s ease}
.ei-card:hover{border-color:#cfe4f6;box-shadow:0 2px 10px rgba(26,35,64,.07)}
.ei-card h3{margin:0 0 6px;font-size:1.08em;font-weight:700;line-height:1.35}
.ei-card h3 a{color:#1a2340;text-decoration:none}
.ei-card:hover h3 a{color:rgba(32,135,201,1)}
.ei-card p{margin:0;color:#4a5568;font-size:.94em;line-height:1.65}
.ei-updated{color:#718096;font-size:.88em;border-top:1px solid #e2e8f0;padding-top:14px;margin:26px 0 0}
.ei-cta-bottom{background:linear-gradient(135deg,#0f1624,#1a2340);padding:40px 20px;text-align:center}
.ei-cta-bottom h2{color:#fff;font-weight:800;margin:0 0 10px;font-size:1.5em}
.ei-cta-bottom p{color:rgba(255,255,255,0.72);max-width:600px;margin:0 auto 22px;line-height:1.75}
.entry-header{display:none!important}
.ast-article-single,.ast-article-single .entry-content{margin-top:0;padding-top:0}
@media(max-width:900px){.ei-hero h1{font-size:1.6em}.ei-art .ei-h2{font-size:1.3em}}
</style>
"""

def card(href, title, desc):
    return ('<div class="ei-card"><h3><a href="%s">%s</a></h3><p>%s</p></div>'
            % (href, title, desc))

p = [CSS]
p.append('<div class="ei-hero"><div class="ei-hero-inner">'
 '<span class="ei-hero-eyebrow">Guides</span>'
 '<h1>' + H1 + '</h1>'
 '<p class="ei-hero-sub">' + META + '</p>'
 '<p class="ei-hero-by">' + BYLINE + '</p>'
 '<div class="ei-hero-btns"><a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing NOW</a></div>'
 '</div></div>\n')

guide_cards = '\n'.join(card(SITE + '/guides/' + s + '/', t, d) for s, t, d in GUIDES)
p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
 '<h2 class="ei-h2">Every Guide on This Site</h2>\n'
 # line 1224: the count is rendered live, never hand-typed.
 '<p class="ei-count"><b>[cnf_child_count type="nil_guide"]</b> guides published</p>\n'
 '<p>Each guide covers one subject end to end, is reviewed by a CPA Ontario member, and '
 'carries the date it was last reviewed.</p>\n'
 '<div class="ei-cards">\n' + guide_cards + '\n</div>\n'
 '</div></div>\n')

rel_cards = '\n'.join(card(h, t, d) for h, t, d in RELATED)
p.append('<div class="ei-section-alt"><div class="ei-wrap ei-art">\n'
 '<h2 class="ei-h2">Also on This Site</h2>\n'
 '<div class="ei-cards">\n' + rel_cards + '\n</div>\n'
 '<p class="ei-updated">Last reviewed: ' + TODAY + '</p>\n'
 '</div></div>\n')

p.append('<div class="ei-cta-bottom"><div class="ei-wrap">'
 '<h2>Nil T2 Filing, ' + PRICE + '</h2>'
 '<p>Type your corporation name, pick your unfiled years, pay, and sign Form T183CORP on '
 'a secure screen. Your CRA confirmation is emailed within 3 business days.</p>'
 '<a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
 '</div></div>\n')

schema = {"@context": "https://schema.org", "@graph": [
 {"@type": "CollectionPage", "@id": URL + "#webpage", "url": URL, "name": TITLE,
  "description": META, "inLanguage": "en-CA", "dateModified": "2026-10-16",
  "author": {"@type": "Person", "name": "Sharad Gondaliya", "honorificSuffix": "CPA",
             "url": SITE + "/sharad-gondaliya-cpa/"}},
 {"@type": "BreadcrumbList", "itemListElement": [
   {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada", "item": SITE + "/"},
   {"@type": "ListItem", "position": 2, "name": H1, "item": URL}]}]}
p.append('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False)
         + '</script>')

html = ''.join(p)
d = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(d, 'guides-hub.html'), 'w', encoding='utf-8').write(html)
print('built /guides/  %d bytes, %d guide cards, %d related'
      % (len(html.encode()), len(GUIDES), len(RELATED)))
