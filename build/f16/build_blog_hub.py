# -*- coding: utf-8 -*-
"""Family 16 hub: /blog/

line 1154  F16 is five hubs on post type `page`: /services/, /tools/,
           /locations/, /guides/, /blog/. "Each hub links every child in its
           family." /blog/ was the last of the five still missing.
line 1224  GATE: no hub publishes without a live child count and links to
           every child. The count is NOT hand-typed: it is rendered by the
           [cnf_child_count] shortcode from docs/hub-child-count-snippet.md,
           here with type="post".

page_for_posts is 0 on this install, so /blog/ is free as a page slug and this
hub does not collide with a WordPress posts archive.

The stylesheet is sliced from the built /guides/ hub so the two cannot drift.
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
URL  = SITE + '/blog/'
TODAY, ISO = 'October 22, 2026', '2026-10-22'
PRICE = '$300.00 plus HST per tax year'

TITLE = 'Nil T2 Filing Blog for Canadian Corporations'
H1    = 'Nil T2 Filing Blog'
META  = ('Posts on filing a nil T2 corporate return in Canada, each written to one '
         'question and reviewed by a CPA Ontario member. Nil T2 filing is '
         + PRICE + '.')
BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')

_g = io.open(os.path.join(HERE, 'guides-hub.html'), encoding='utf-8').read()
CSS = _g[:_g.index('</style>') + len('</style>')] + '\n'

POSTS = [
 ('mandatory-t2-e-filing-after-2023',
  'Mandatory T2 E-Filing for Tax Years Starting After 2023',
  'Electronic filing is mandatory for virtually all corporations for tax years '
  'starting after 2023. What a paper T2 costs, and why a nil return is not exempt.'),
 ('schedule-50-and-the-10-percent-shareholder-rule',
  'Schedule 50 and the 10% Shareholder Rule',
  'Which shareholders must appear, what each row records, and why a dormant '
  'corporation still files Schedule 50 in a year of zeros.'),
]

RELATED = [
 (SITE + '/guides/', 'Nil T2 Filing Guides',
  'Each guide covers one subject end to end, reviewed by a CPA Ontario member.'),
 (SITE + '/deadlines/', 'T2 Filing Deadlines',
  'Every fiscal year-end and its due date, with the business-day rule.'),
 (SITE + '/pricing/nil-t2-filing-cost/', 'Nil T2 Filing Cost',
  'What ' + PRICE + ' covers, and what falls outside a nil return.'),
]

def card(href, title, desc):
    return ('<div class="ei-card"><h3><a href="%s">%s</a></h3><p>%s</p></div>'
            % (href, title, desc))

p = [CSS]
p.append('<div class="ei-hero"><div class="ei-hero-inner">'
 '<span class="ei-hero-eyebrow">Blog</span>'
 '<h1>' + H1 + '</h1>'
 '<p class="ei-hero-sub">' + META + '</p>'
 '<p class="ei-hero-by">' + BYLINE + '</p>'
 '<div class="ei-hero-btns"><a class="ei-btn-blue" href="' + FORM
 + '">Start Nil T2 Filing NOW</a></div>'
 '</div></div>\n')

post_cards = '\n'.join(card(SITE + '/blog/' + s + '/', t, d) for s, t, d in POSTS)
p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
 '<h2 class="ei-h2">Every Post on This Site</h2>\n'
 '<div class="ei-cards">\n' + post_cards + '\n</div>\n'
 '</div></div>\n')

rel_cards = '\n'.join(card(h, t, d) for h, t, d in RELATED)
p.append('<div class="ei-section-alt"><div class="ei-wrap ei-art">\n'
 '<h2 class="ei-h2">Also on This Site</h2>\n'
 '<div class="ei-cards">\n' + rel_cards + '\n</div>\n'
 '<p class="ei-updated">Last reviewed: ' + TODAY + '</p>\n'
 '</div></div>\n')

p.append('<div class="ei-cta-bottom"><div class="ei-wrap">'
 '<h2>Nil T2 Filing, ' + PRICE + '</h2>'
 '<p>Type your corporation name, pick your unfiled years, pay, and sign Form '
 'T183CORP on a secure screen. Your CRA confirmation is emailed within 3 business '
 'days.</p>'
 '<a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
 '</div></div>\n')

schema = {"@context": "https://schema.org", "@graph": [
 {"@type": "CollectionPage", "@id": URL + "#webpage", "url": URL, "name": TITLE,
  "description": META, "inLanguage": "en-CA", "dateModified": ISO,
  "author": {"@type": "Person", "name": "Sharad Gondaliya", "honorificSuffix": "CPA",
             "url": SITE + "/sharad-gondaliya-cpa/"}},
 {"@type": "BreadcrumbList", "itemListElement": [
   {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
    "item": SITE + "/"},
   {"@type": "ListItem", "position": 2, "name": H1, "item": URL}]}]}
p.append('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False)
         + '</script>')

html = ''.join(p)
io.open(os.path.join(HERE, 'blog-hub.html'), 'w', encoding='utf-8').write(html)
print('built /blog/  %d bytes, %d post cards, %d related'
      % (len(html.encode()), len(POSTS), len(RELATED)))
