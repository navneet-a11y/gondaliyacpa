"""Restyle /ontario/ (page 516) to the /services/ card design.

Presentation only. Every sentence already on page 516 is reproduced verbatim,
including the two CRA figures, the Ontario Filing Note, all twelve child links
and all five questions. Nothing is dropped.

Three things are added, none removed: the trust strip, a heading over the
question block, and a one-line description plus an icon on each card, which the
card design needs in order to be the /services/ design.

Known deviation left alone deliberately: the byline still reads "By Sharad
Gondaliya, CPA, registered EFILE electronic filer", which does not satisfy 7.5
rule 3. That is wording, not design, and Navneet asked for design only. Logged
in docs/decisions.md for a separate sweep.
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
CARDS = json.load(io.open(os.path.join(HERE, 'ontario-cards.json'), encoding='utf-8'))

# the stylesheet proven on the BC hub, reused rather than retyped
_bc = io.open(os.path.join(HERE, 'british-columbia.html'), encoding='utf-8').read()
CSS = _bc[:_bc.index('</style>') + len('</style>')]

def a(h, t):
    return '<a href="%s">%s</a>' % (h, t)

QA = [
 ('Does an Ontario corporation file a separate provincial corporate tax return?',
  'No. Ontario corporate income tax is reported on the federal T2 return filed '
  'with the Canada Revenue Agency, so a nil T2 covers both.'),
 ('Is the Ontario annual return covered by the nil T2 fee?',
  'No. Since October 2021 the Ontario annual return is filed through the '
  'Ontario Business Registry. It is not covered by the $300.00 fee, and we tell '
  'you if you still owe it.'),
 ('How much does nil T2 filing cost in Ontario?',
  '$300.00 plus HST per tax year. One price for every year and every province. '
  'No hourly billing and no add-on fees. With 13 per cent HST, that is $339.00 '
  'in total per tax year.'),
 ('How is an Ontario nil T2 signed and filed?',
  'You sign Form T183CORP before we transmit. We are a registered EFILE '
  'electronic filer. Your return is transmitted to the Canada Revenue Agency '
  'electronically. Your CRA confirmation is emailed within 3 business days. '
  'Business days are Monday to Friday and exclude Ontario statutory holidays.'),
 ('What if my Ontario corporation is not nil?',
  'This service is for a corporation with no activity in the tax year. A '
  'corporation with investment income, rental income, or dividends paid or '
  'received is not nil. Other cases that are not nil include a corporation that '
  'is not a Canadian-controlled private corporation, an amalgamation, or a '
  'corporation already dissolved or struck. We route you to our sister office '
  'at gondaliyacpa.ca at $350.00 plus HST per tax year before you pay. If we '
  'find it after you pay, we refund you in full.'),
]

def build():
    b = [CSS]
    b.append('<div class="cnf-hero"><div class="cnf-hero-in"><h1>Nil T2 Filing in '
             'Ontario</h1><p class="cnf-hero-sub">$300.00 Plus HST Per Tax Year</p>'
             '<p class="cnf-hero-lede">We are a registered EFILE electronic filer. '
             'Your return is transmitted to the Canada Revenue Agency '
             'electronically.</p><p><a class="cnf-hero-btn" href="' + FORM + '">'
             'Start Nil T2 Filing NOW</a></p></div></div>')
    b.append('<div class="cnf-w">')
    b.append('<nav class="cnf-crumb" aria-label="Breadcrumb">'
             + a(SITE + '/', 'Nil T2 filing in Canada') + ' &rsaquo; '
             '<span aria-current="page">Nil T2 filing in Ontario</span></nav>')
    b.append('<p class="cnf-by">By '
             + a(SITE + '/sharad-gondaliya-cpa/', 'Sharad Gondaliya, CPA')
             + ', registered EFILE electronic filer</p>')
    b.append('<p class="cnf-rev">Last reviewed: October 15, 2026</p>')
    b.append('<ul class="cnf-trust"><li>Registered EFILE electronic filer</li>'
             '<li>CRA confirmation within 3 business days</li>'
             '<li>$300.00 plus HST per tax year</li></ul>')
    b.append('<p>Nil T2 filing in Ontario is the annual T2 return a corporation with '
             'no activity in the tax year still files with the Canada Revenue Agency. '
             'Every Ontario corporation must file it within six months of its fiscal '
             'year-end, every year until it is dissolved. A corporation with '
             'investment income, rental income, or dividends paid or received is not '
             'nil.</p>')

    b.append('<h2>Ontario corporations in numbers</h2>')
    b.append('<table class="cnf-tbl"><thead><tr><th scope="col">Measure</th>'
             '<th scope="col">Source</th><th scope="col">Ontario</th></tr></thead>'
             '<tbody>')
    b.append('<tr><td>T2 returns assessed</td><td>Canada Revenue Agency T2 assessment '
             'table</td><td>1,108,730</td></tr>')
    b.append('<tr><td>First-time T2 filers in 2023</td><td>Canada Revenue Agency '
             '(199,800 in Canada)</td><td>87,990</td></tr>')
    b.append('</tbody></table>')
    b.append('<p class="cnf-cap">Local data pulled October 14, 2026. The T2 assessment '
             'count is refreshed when the Canada Revenue Agency reissues its annual '
             'table.</p>')

    b.append('<h2>Ontario Filing Note</h2>')
    b.append('<p>Ontario corporate income tax is reported on the federal T2 return, so '
             'there is no separate Ontario corporate tax return. The Ontario annual '
             'return is a different filing: since October 2021 it is filed through the '
             'Ontario Business Registry, and it is not covered by the $300.00 fee.</p>')

    b.append('<h2>Ontario Nil T2 Filing Services</h2>')
    b.append('<ul class="cnf-boxes">')
    for c in CARDS:
        b.append('<li class="cnf-box">%s<h3>%s</h3><p>%s</p>'
                 '<a class="cnf-more" href="%s%s">Learn more</a></li>'
                 % (c['svg'], c['title'], c['desc'], SITE, c['href']))
    b.append('</ul>')

    b.append('<h2>Nil T2 Filing in Ontario: Frequently Asked Questions</h2>')
    b.append('<div class="cnf-faq">')
    for q, ans in QA:
        b.append('<details open><summary><h3>' + q + '</h3></summary>'
                 '<div class="cnf-faq-a"><p>' + ans + '</p></div></details>')
    b.append('</div>')

    b.append('<p>Start your ' + a(FORM, 'nil T2 filing in Ontario') + ', or go to '
             + a(SITE + '/', 'nil T2 filing in Canada') + '.</p>')
    b.append('<p><a class="cnf-btn" href="' + FORM + '">Start Nil T2 Filing NOW</a></p>')
    b.append('</div>')

    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
         "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Nil T2 filing in Ontario",
         "item": SITE + "/ontario/"}]},
      {"@type": "WebPage", "@id": SITE + "/ontario/#page", "url": SITE + "/ontario/",
       "name": "Nil T2 Filing in Ontario",
       "about": {"@type": "State", "name": "Ontario"},
       "dateModified": "2026-10-15",
       "author": {"@type": "Person", "name": "Sharad Gondaliya",
                  "honorificSuffix": "CPA",
                  "url": SITE + "/sharad-gondaliya-cpa/"}}]}
    b.append('<script type="application/ld+json">' + json.dumps(schema) + '</script>')
    return '\n'.join(b) + '\n'

if __name__ == '__main__':
    out = build()
    io.open(os.path.join(HERE, 'ontario.html'), 'w', encoding='utf-8').write(out)
    print('ontario %d bytes' % len(out.encode('utf-8')))
