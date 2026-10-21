"""Jurisdiction hub pages, modelled on /ontario/ (page 516).

Plan basis, stated plainly because there is a problem with it. The plan has no
jurisdiction-hub family:

  F3  City hubs            /<city>/      15, and the listed slugs are all
                                         Ontario cities (toronto, hamilton...)
  F4  Service x place      12 slugs x place, e.g. /nil-t2-filing-ontario/
  F16 Hub and index pages  5 named hubs: /services/, /tools/, /locations/,
                                         /guides/, /blog/

So a bare /ontario/ or /british-columbia/ belongs to none of them. Page 516
was built anyway, and it also shares its exact title with its own child
/nil-t2-filing-ontario/ (item 512). Logged as the 20th plan conflict. This
generator follows Navneet's instruction to match /ontario/, and differentiates
the title and H1 from the F4 child so the two do not compete.

Template is page 516's, reproduced in the same CSS, with three departures that
the Ontario page gets wrong or cannot carry for another province:

1. No corporation-count table. Page 516 carries "T2 returns assessed
   1,108,730" and "first-time T2 filers 87,990" sourced to a Canada Revenue
   Agency assessment table. No per-province count table was findable, so the
   equivalent British Columbia figures cannot be sourced and are NOT invented.
   What replaces it is a table of verifiable British Columbia filing rules,
   which is the more useful place data row anyway.

2. No HST computation. Page 516 says "With 13 per cent HST, that is $339.00 in
   total per tax year". That is the Ontario rate. **British Columbia is not an
   HST province.** The computation is omitted here. The standing price string
   "$300.00 plus HST per tax year" is kept for consistency with the other 94
   live URLs, because changing it is Sharad Gondaliya's call, not this
   generator's. Flagged in decisions.md: the string is inaccurate for the eight
   non-HST jurisdictions and needs a decision before 11 more hubs are built.

3. The services grid links the live root service pages rather than
   service-x-place children, because no British Columbia F4 pages exist yet.
   The grid is replaced by the real children as they are built.

Sources for the British Columbia rules, checked 2026-10-21:
  BC Registries annual report, two months from the anniversary, filed online,
  Registrar may dissolve after two consecutive years of non-filing
  https://www.corporateonline.gov.bc.ca/WebHelp/overview_annbc.htm
  https://www.corporateonline.gov.bc.ca/WebHelp/good_standing.htm
  https://www2.gov.bc.ca/assets/gov/employment-business-and-economic-development/business-management/permits-licences-and-registration/registries-forms/form06com-annualreport.pdf
"""
import json, os, re

SITE  = 'https://corpnilfilingfor300.ca'
FORM  = SITE + '/form/'
TODAY, ISO = 'October 21, 2026', '2026-10-21'
PRICE = '$300.00 plus HST per tax year'
HERO_IMG = (SITE + '/wp-content/uploads/2026/09/'
            'business-executives-having-meeting_1098-18316.jpg')

NOT_NIL = ('This service is for a corporation with no activity in the tax year. A '
           'corporation with investment income, rental income, or dividends paid or '
           'received is not nil. Other cases that are not nil include a corporation '
           'that is not a Canadian-controlled private corporation, an amalgamation, '
           'or a corporation already dissolved or struck. We route you to our sister '
           'office at gondaliyacpa.ca at $350.00 plus HST per tax year before you '
           'pay. If we find it after you pay, we refund you in full.')

# The six live root service pages, plus the three live hubs. Replaced per
# jurisdiction by the real F4 children once they exist.
GENERIC_SERVICES = [
 ('/nil-t2-filing/', 'Nil T2 Filing Services'),
 ('/catch-up-nil-t2-filing/', 'Catch-Up Nil T2 Filing'),
 ('/dormant-corporation-filing/', 'Dormant Corporation Filing'),
 ('/final-t2-before-dissolution/', 'Final T2 Before Dissolution'),
 ('/t2-short-filing/', 'T2 Short Filing'),
 ('/inactive-holding-corporation-t2-filing/', 'Inactive Holding Corporation T2 Filing'),
 ('/pricing/nil-t2-filing-cost/', 'Nil T2 Filing Cost'),
 ('/deadlines/', 'T2 Filing Deadlines'),
 ('/guides/', 'Nil T2 Filing Guides'),
]

CSS = """<style>.cnf-hero{background-image:linear-gradient(rgba(11,26,51,.82),rgba(11,26,51,.82)),url('""" + HERO_IMG + """');background-size:cover;background-position:center center;background-repeat:no-repeat;padding:40px 20px}
.cnf-hero-in{max-width:1140px;margin:0 auto;text-align:left}
.cnf-hero h1{color:#fff;font-family:Poppins,sans-serif;font-weight:700;font-size:40px;line-height:1.25;margin:0}
.cnf-hero .cnf-hero-sub{color:#fff;font-family:Poppins,sans-serif;font-weight:600;font-size:25px;margin:10px 0 0}
.cnf-hero .cnf-hero-lede{color:#fff;font-family:Lato,sans-serif;font-size:17px;line-height:1.6;margin:10px 0 0;max-width:860px}
.cnf-hero .cnf-hero-btn{display:inline-block;background:#314d8a;color:#fff!important;padding:20px 50px;border-radius:35px;font-family:Poppins,sans-serif;font-weight:600;font-size:18px;text-decoration:none!important;margin:24px 0 0}
.cnf-hero .cnf-hero-btn:hover,.cnf-hero .cnf-hero-btn:focus{background:#2087c9;color:#fff!important;text-decoration:none!important}
@media(max-width:767px){.cnf-hero{padding:32px 16px}.cnf-hero h1{font-size:28px}.cnf-hero .cnf-hero-sub{font-size:20px}.cnf-hero .cnf-hero-btn{padding:16px 34px;font-size:16px}}
.entry-header{display:none!important}
.ast-article-single,.ast-article-single .entry-content{margin-top:0;padding-top:0}
.cnf-w{max-width:1000px;margin:0 auto;padding:40px 20px 60px;font-family:Lato,sans-serif;color:#333;font-size:17px;line-height:1.65}
.cnf-w h2{font-family:Poppins,sans-serif;color:#314d8a;font-size:24px;font-weight:600;margin:34px 0 10px}
.cnf-w a{color:#314d8a;font-weight:600}.cnf-w a:hover{color:#2087c9}
.cnf-crumb{font-size:14px;color:#636363}.cnf-crumb a{font-weight:400;text-decoration:none}
.cnf-by{font-size:15px;margin:6px 0 0}.cnf-rev{font-size:15px;color:#636363;margin:2px 0 18px}
.cnf-tbl{width:100%;border-collapse:collapse;font-size:16px}.cnf-tbl th,.cnf-tbl td{border:1px solid #dfe6ef;padding:12px 14px;text-align:left;vertical-align:top}
.cnf-tbl th{background:#314d8a;color:#fff;font-family:Poppins,sans-serif;font-weight:600}.cnf-tbl td:last-child{font-weight:700;color:#314d8a}
.cnf-cap{font-size:14px;color:#636363;margin-top:8px}
.cnf-kids{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.cnf-kids .cnf-kid{display:block;padding:20px;border:1px solid #dfe6ef;border-top:4px solid #314d8a;border-radius:10px;font-family:Poppins,sans-serif;font-weight:600;color:#314d8a;text-decoration:none}
.cnf-kids a:hover{background:#f5f8fc}@media(max-width:767px){.cnf-kids{grid-template-columns:1fr}}
.cnf-btn{display:inline-block;background:#314d8a;color:#fff!important;padding:16px 36px;border-radius:35px;font-family:Poppins,sans-serif;font-weight:600;text-decoration:none;margin:20px 12px 8px 0}.cnf-btn:hover{background:#2087c9}</style>
"""

def a(href, text):
    return '<a href="%s">%s</a>' % (href, text)

def tbl(head, rows):
    out = ['<table class="cnf-tbl"><thead><tr>'
           + ''.join('<th scope="col">%s</th>' % h for h in head)
           + '</tr></thead><tbody>']
    for r in rows:
        out.append('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>')
    out.append('</tbody></table>')
    return '\n'.join(out)

# ---------------------------------------------------------------------------
# Jurisdiction data. Everything province-specific lives here, so the remaining
# eleven are a data change rather than a template change.
#
# separate_return is the hard rule 8 field: Quebec pages must state CO-17 is a
# separate return and Alberta pages the same for AT1. For every other
# jurisdiction the correct statement is the opposite, that provincial corporate
# income tax is collected through the federal T2, and that is said explicitly
# rather than left out.
# ---------------------------------------------------------------------------
BC = dict(
 slug='british-columbia',
 name='British Columbia',
 short='BC',
 title='Nil T2 Filing for British Columbia Corporations',
 h1='Nil T2 Filing in British Columbia',
 meta=('The nil T2 a British Columbia corporation files every year, why there is no '
       'separate BC corporate return, and how the BC annual report differs.'),
 separate_return=None,
 registry='BC Registries and Online Services',
 annual_filing='annual report',
 annual_due='Within two months after each anniversary of the date of incorporation',
 annual_statute='Section 51 of the Business Corporations Act',
 annual_online=True,
 strike_after='Two consecutive years of non-filing',
 # The Ontario page computes the HST total. British Columbia is not an HST
 # province, so no tax computation appears on this page at all.
 quote_tax_total=False,
)

JURISDICTIONS = [BC]

def build(j):
    url = '%s/%s/' % (SITE, j['slug'])
    name, short = j['name'], j['short']

    hero = ('<div class="cnf-hero"><div class="cnf-hero-in"><h1>' + j['h1'] + '</h1>'
            '<p class="cnf-hero-sub">$300.00 Plus HST Per Tax Year</p>'
            '<p class="cnf-hero-lede">We are a registered EFILE electronic filer. Your '
            'return is transmitted to the Canada Revenue Agency electronically.</p>'
            '<p><a class="cnf-hero-btn" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
            '</p></div></div>\n')

    b = ['<div class="cnf-w">']
    b.append('<nav class="cnf-crumb" aria-label="Breadcrumb">'
             + a(SITE + '/', 'Nil T2 filing in Canada') + ' &rsaquo; '
             '<span aria-current="page">Nil T2 filing in ' + name + '</span></nav>')
    # 7.5 byline rule 3: a page stating a filing rule, a penalty figure, a
    # schedule requirement or a T183CORP rule carries this exact byline, with
    # the membership number. A jurisdiction hub states filing rules, so it does.
    # Page 516 and the twelve Ontario service pages still carry the older
    # "By Sharad Gondaliya, CPA, registered EFILE electronic filer" form, which
    # does not satisfy rule 3. Logged for a sweep.
    b.append('<p class="cnf-by">Written and reviewed by '
             + a(SITE + '/sharad-gondaliya-cpa/', 'Sharad Gondaliya, CPA (Ontario)')
             + ', CPA Ontario Membership 61040184.</p>')
    b.append('<p class="cnf-rev">Last reviewed: ' + TODAY + '</p>')

    b.append('<p>Nil T2 filing in ' + name + ' is the annual T2 return a corporation '
             'with no activity in the tax year still files with the Canada Revenue '
             'Agency. Every ' + name + ' corporation must file it within six months of '
             'its fiscal year-end, every year until it is dissolved. A corporation with '
             'investment income, rental income, or dividends paid or received is not '
             'nil.</p>')

    # ---- the place data row: verifiable rules, not invented counts ----------
    sep = ('Yes, the ' + j['separate_return'] if j['separate_return']
           else 'None, collected through the federal T2')
    b.append('<h2>' + name + ' filing obligations at a glance</h2>')
    b.append(tbl(('Obligation', 'Detail', name),
      [('T2 corporate tax return', 'Filed with the Canada Revenue Agency',
        'Within 6 months of the fiscal year-end'),
       ('Separate provincial corporate income tax return',
        'A second income tax return, filed with the province', sep),
       ('Corporate ' + j['annual_filing'], 'A registry filing, not a tax return',
        j['annual_due']),
       ('Where the ' + j['annual_filing'] + ' is filed', j['registry'],
        'Online' if j['annual_online'] else 'With the registry'),
       ('Authority for the ' + j['annual_filing'], j['annual_statute'],
        'Provincial'),
       ('Registrar may dissolve the company after', 'Missed registry filings',
        j['strike_after']),
       ('Our fee', 'One nil T2 for one corporation for one tax year',
        '$300.00 plus HST')]))
    b.append('<p class="cnf-cap">' + name + ' registry rules confirmed '
             + TODAY + ' against ' + j['registry'] + '. The T2 due date comes from '
             'the Income Tax Act and does not vary by province.</p>')

    # ---- the filing note ---------------------------------------------------
    b.append('<h2>' + name + ' Filing Note</h2>')
    if j['separate_return']:
        b.append('<p>' + name + ' administers its own corporate income tax, so a '
                 + name + ' corporation files the ' + j['separate_return'] + ', a '
                 'separate provincial income tax return, in addition to the federal '
                 'T2. The ' + j['separate_return'] + ' is not covered by the $300.00 '
                 'fee.</p>')
    else:
        b.append('<p>' + name + ' corporate income tax is reported on the federal T2 '
                 'return, so there is no separate ' + name + ' corporate tax return. '
                 'Alberta and Quebec are the two provinces that do administer their '
                 'own, through the AT1 and the CO-17.</p>')
    b.append('<p>The ' + name + ' ' + j['annual_filing'] + ' is a different filing. It '
             'is a registry filing that confirms the company&rsquo;s directors and '
             'registered office, it carries no tax, and it is not covered by the '
             '$300.00 fee. It is due '
             + j['annual_due'][0].lower() + j['annual_due'][1:] + '.</p>')

    # ---- services grid ----------------------------------------------------
    b.append('<h2>Nil T2 Filing Services for ' + name + ' Corporations</h2>')
    b.append('<ul class="cnf-kids">')
    for href, label in GENERIC_SERVICES:
        b.append('<li>' + '<a class="cnf-kid" href="%s%s">%s</a>' % (SITE, href, label)
                 + '</li>')
    b.append('</ul>')

    # ---- question blocks --------------------------------------------------
    b.append('<h2>Does a ' + name + ' corporation file a separate provincial corporate '
             'tax return?</h2>')
    if j['separate_return']:
        b.append('<p>Yes. ' + name + ' corporate income tax is filed on the '
                 + j['separate_return'] + ', separately from the federal T2.</p>')
    else:
        b.append('<p>No. ' + name + ' corporate income tax is reported on the federal '
                 'T2 return filed with the Canada Revenue Agency, so a nil T2 covers '
                 'both.</p>')

    b.append('<h2>Is the ' + name + ' ' + j['annual_filing']
             + ' covered by the nil T2 fee?</h2>')
    b.append('<p>No. It is filed with ' + j['registry'] + ', '
             + j['annual_due'][0].lower() + j['annual_due'][1:]
             + '. It is not covered by the $300.00 fee, and we tell you if you still '
             'owe it.</p>')

    b.append('<h2>What happens if the ' + name + ' ' + j['annual_filing']
             + ' is not filed?</h2>')
    b.append('<p>The company stops being in good standing, so the registry will not '
             'issue a certificate of good standing for it. After '
             + j['strike_after'][0].lower() + j['strike_after'][1:]
             + ' the registrar may dissolve the company. None of that cancels an '
             'outstanding T2: the corporate tax account and the registry record are '
             'separate trails.</p>')

    b.append('<h2>How much does nil T2 filing cost in ' + name + '?</h2>')
    cost = ('<p>' + PRICE[0].upper() + PRICE[1:] + '. One price for every year and '
            'every province. No hourly billing and no add-on fees.')
    cost += ' Tax is added at the rate for your province.</p>'
    b.append(cost)

    b.append('<h2>How is a ' + name + ' nil T2 signed and filed?</h2>')
    b.append('<p>You sign Form T183CORP before we transmit. We are a registered EFILE '
             'electronic filer. Your return is transmitted to the Canada Revenue Agency '
             'electronically. Your CRA confirmation is emailed within 3 business days. '
             'Business days are Monday to Friday and exclude ' + name
             + ' statutory holidays.</p>')

    b.append('<h2>What if my ' + name + ' corporation is not nil?</h2>')
    b.append('<p>' + NOT_NIL + '</p>')

    b.append('<p>For the whole subject in one place, see the '
             + a(SITE + '/guides/nil-t2-return-complete-guide/',
                 'complete guide to the nil T2 return') + ', or the guide to '
             + a(SITE + '/guides/provincial-and-federal-annual-returns/',
                 'provincial and federal annual returns') + '.</p>')
    b.append('<p>Start your ' + a(FORM, 'nil T2 filing in ' + name) + ', or go to '
             + a(SITE + '/', 'nil T2 filing in Canada') + '.</p>')
    b.append('<p><a class="cnf-btn" href="' + FORM + '">Start Nil T2 Filing NOW</a></p>')
    b.append('</div>')

    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
         "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Nil T2 filing in " + name,
         "item": url}]},
      {"@type": "WebPage", "@id": url + "#page", "url": url, "name": j['title'],
       "description": j['meta'], "inLanguage": "en-CA",
       "about": {"@type": "State", "name": name},
       "dateModified": ISO,
       "author": {"@type": "Person", "name": "Sharad Gondaliya",
                  "honorificSuffix": "CPA",
                  "url": SITE + "/sharad-gondaliya-cpa/"}}]}

    html = (CSS + hero + '\n'.join(b) + '\n<script type="application/ld+json">'
            # No trailing newline: WordPress strips it, so emitting one makes
            # every local-versus-live byte comparison off by one.
            + json.dumps(schema, ensure_ascii=False) + '</script>')
    return html, url

HERE = os.path.dirname(os.path.abspath(__file__))
records = []
for j in JURISDICTIONS:
    html, url = build(j)
    records.append(dict(slug=j['slug'], title=j['title'], h1=j['h1'],
                        meta_description=j['meta'], url=url, content=html))
    open(os.path.join(HERE, j['slug'] + '.html'), 'w', encoding='utf-8').write(html)
json.dump(records, open(os.path.join(HERE, 'jurisdictions-manifest.json'), 'w'),
          ensure_ascii=False, indent=1)
for r in records:
    print('%-20s %6d bytes' % (r['slug'], len(r['content'].encode())))
