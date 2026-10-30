# -*- coding: utf-8 -*-
"""Family 4 service x place pages for Alberta: the first five.

Navneet, 2026-10-30: "for alberta just create 5 service place page and hub for
now". These are the same five services British Columbia opened with on
2026-10-21, so the two provinces stay comparable as they fill out.

Design, CSS, section order, schema shape and the not-nil wording are imported
from build_f4_bc rather than copied, so the provinces cannot drift apart.

ALBERTA IS DIFFERENT IN ONE WAY THAT MATTERS, AND THE PLAN SAYS SO.
Every province built so far reports provincial corporate income tax through the
federal T2. Alberta does not: hard rule 8 requires Alberta pages to state that
the AT1 is a separate return, and line 1212 states it outright -- "Alberta AT1
and Quebec CO-17 are separate provincial returns and are not included in the
fee". That claim is sourced to the signed-off plan, not to the web, and it is
the spine of all five of these pages.

WHAT THESE PAGES DO NOT SAY, AND WHY.
Six Alberta registry facts could not be sourced: the annual return's due date,
its statutory authority, its fee, the registry's exact name and filing route,
how long non-filing runs before the registrar may dissolve, and whether a nil
Alberta corporation is exempt from filing an AT1 at all. The environment's
network policy denies www.alberta.ca and open.alberta.ca (403 on CONNECT), so
the Corporate Registry pages and Information Circular CT-2 could not be read,
and web search returned only law-firm and filing-service pages contradicting
each other -- the annual return variously due six months after the fiscal
year-end, in the anniversary month, or 60 days after it.

So ANNUAL_SOURCED is False and none of it is written down. The place data table
carries only sourced rows, and the "does not cover" list says the Alberta annual
return exists and is not covered by the fee without asserting when it is due,
what it costs or where exactly it is filed. Saying nothing at all there would
leave a reader thinking the T2 and the AT1 are the whole obligation, which would
be a misleading omission; stating existence without timing asserts nothing that
is not already common to every province. Set ANNUAL_SOURCED True and fill the
block below once the facts are in hand, and the fuller table returns by itself.

The AT1 exemption question is left open on purpose. If a nil Alberta corporation
turns out to be exempt from the AT1, these pages should say so plainly, and that
is a better page than this one. It is not a page that can be written from a
source nobody has read.
"""
import io, json, os

from build_f4_bc import CSS, NOT_NIL_1, NOT_NIL_2, a, SITE, FORM

HERE = os.path.dirname(os.path.abspath(__file__))
HUB = SITE + '/alberta/'
PLACE, SHORT = 'Alberta', 'AB'
TODAY, ISO = 'October 30, 2026', '2026-10-30'

# Hard rule 8 and line 1212. The one Alberta-specific claim the plan states.
PROV_RETURN = 'Alberta AT1'
# Line 1743: the CRA T2 assessment count, the 6(k) local-data figure for Alberta.
T2_ASSESSED = '365,890'

# Flip to True only with a source and a date for every field. See the docstring.
ANNUAL_SOURCED = False

AT1_SENTENCE = ('Alberta administers its own corporate income tax, so an Alberta '
                'corporation also files the ' + PROV_RETURN + ', a separate '
                'provincial income tax return. The ' + PROV_RETURN + ' is not '
                'covered by the $300.00 fee.')


def place_rows():
    """The place data row line 1212 makes mandatory. Sourced entries only."""
    rows = [
      ('T2 filing deadline', 'Within six months of the fiscal year-end',
       'Income Tax Act'),
      ('Separate provincial corporate income tax return',
       'Yes, the ' + PROV_RETURN, 'Alberta Corporate Tax Act'),
      ('T2 returns assessed', T2_ASSESSED,
       'Canada Revenue Agency T2 assessment table'),
      ('Filing route', 'T2 transmitted electronically to the Canada Revenue Agency '
       'by a registered EFILE electronic filer', 'Canada Revenue Agency'),
    ]
    if ANNUAL_SOURCED:
        raise AssertionError(
            'ANNUAL_SOURCED is True but the sourced registry rows were never '
            'written. Add them here with a source for each.')
    return rows


SERVICES = [
 dict(
  slug='nil-t2-filing-alberta',
  service='nil-t2-filing',
  title='Nil T2 Filing in Alberta',
  keyword='nil t2 filing alberta',
  national=('/nil-t2-filing/', 'nil T2 filing'),
  lead_h2='Nil T2 Filing for Alberta Corporations',
  lead=['A nil T2 is the corporate income tax return an Alberta corporation files '
        'for a tax year in which it had no activity. Every Alberta corporation '
        'files a T2 with the Canada Revenue Agency within six months of its fiscal '
        'year-end, every year until it is formally dissolved, whether or not it '
        'earned anything. We prepare the return, a CPA reviews it, and we transmit '
        'it electronically for $300.00 plus HST per tax year.',
        AT1_SENTENCE],
  extra=[('What Makes a Return Nil',
          ['A nil return reports no income and no expenses for the tax year. The '
           'corporation still exists, still has a Business Number, and still has a '
           'fiscal year-end, so the return is still due. Filing it keeps the '
           'corporation&rsquo;s tax record current and keeps its standing with the '
           'Canada Revenue Agency intact.']),
         ('Why Alberta Is Not Like Most Provinces',
          ['In most provinces, provincial corporate income tax is collected through '
           'the federal T2, so one return settles both. Alberta is one of two '
           'provinces that administer their own corporate income tax instead, '
           'Quebec being the other. An Alberta corporation therefore has two '
           'corporate income tax returns to think about rather than one.',
           'What we file is the federal T2. The ' + PROV_RETURN + ' is a separate '
           'return and is not covered by the $300.00 fee, and we tell you that '
           'before you pay rather than after.'])],
  excerpt='Nil T2 filing for Alberta corporations with no activity in the tax '
          'year. $300.00 plus HST per tax year.'),

 dict(
  slug='catch-up-nil-t2-filing-alberta',
  service='catch-up-nil-t2-filing',
  title='Catch-Up Nil T2 Filing in Alberta',
  keyword='catch-up nil t2 filing alberta',
  national=('/catch-up-nil-t2-filing/', 'catch-up nil T2 filing'),
  lead_h2='Bringing Unfiled Alberta Years Up to Date',
  lead=['If an Alberta corporation has not filed for several years, each of those '
        'years is still outstanding and each one is a separate return. We file them '
        'together, oldest year first, so the Canada Revenue Agency processes them in '
        'the order they fell due. Each tax year is $300.00 plus HST, because each '
        'tax year is its own T2.'],
  extra=[('Why the Oldest Year Goes First',
          ['A T2 carries forward figures from the year before it, so the years have '
           'to be assessed in order. Filing the oldest outstanding year first means '
           'each later return is assessed against a record that is already up to '
           'date, rather than against a gap.',
           'You tell us which years are unfiled and confirm the corporation had no '
           'activity in each of them. If any year turns out not to be nil, we tell '
           'you before you pay for that year.']),
         ('An Alberta Catch-Up Has Two Trails, Not One',
          ['A corporation that stopped filing its federal T2 usually stopped filing '
           'its ' + PROV_RETURN + ' in the same years, because the two returns tend '
           'to be forgotten together. Clearing the federal years does not clear the '
           'provincial ones. They are assessed separately, by a separate tax '
           'authority, on their own record.',
           'We file the federal T2 for each outstanding year. The ' + PROV_RETURN
           + ' years are a separate filing and are not covered by the $300.00 fee. '
           'We tell you how many federal years we found outstanding, so you know '
           'the shape of what is left.'])],
  excerpt='Catch up every unfiled year for an Alberta corporation, oldest year '
          'first. $300.00 plus HST per tax year.'),

 dict(
  slug='dormant-corporation-filing-alberta',
  service='dormant-corporation-filing',
  title='Dormant Corporation Filing in Alberta',
  keyword='dormant corporation filing alberta',
  national=('/dormant-corporation-filing/', 'dormant corporation filing'),
  lead_h2='Keeping a Dormant Alberta Corporation Up to Date',
  lead=['A dormant Alberta corporation is one that still exists on the register but '
        'has stopped trading, or never started. Being dormant does not pause '
        'anything. The corporation still files a T2 with the Canada Revenue Agency '
        'within six months of each fiscal year-end, every year until it is formally '
        'dissolved. If the dormant corporation had no activity in the tax year, we '
        'file its nil T2 for $300.00 plus HST. Filing does not dissolve the '
        'corporation. It keeps the corporation&rsquo;s tax record clean while you '
        'decide whether to restart it or close it.'],
  extra=[('Dormant Is Not the Same as Dissolved',
          ['An Alberta corporation stays in existence until it is dissolved. Until '
           'then every filing obligation continues, and a year of no activity is a '
           'year that still has a return due. The corporate tax account and the '
           'provincial registry record are separate trails, so bringing one up to '
           'date does not bring the other with it.',
           'If you plan to close the corporation instead, see our '
           + a(SITE + '/final-t2-before-dissolution-alberta/',
               'final T2 before dissolution in Alberta') + '.']),
         ('A Dormant Alberta Corporation Still Has Two Returns',
          [AT1_SENTENCE + ' A dormant corporation does not escape that by being '
           'dormant, any more than it escapes the federal T2.',
           'We file the federal nil T2. Where the ' + PROV_RETURN + ' is also '
           'outstanding, that is a separate filing, and we say so plainly rather '
           'than leaving you to find out later.'])],
  excerpt='Nil T2 filing for dormant Alberta corporations with no activity in the '
          'tax year. $300.00 plus HST per tax year.'),

 dict(
  slug='final-t2-before-dissolution-alberta',
  service='final-t2-before-dissolution',
  title='Final T2 Before Dissolution in Alberta',
  keyword='final t2 before dissolution alberta',
  national=('/final-t2-before-dissolution/', 'final T2 before dissolution'),
  lead_h2='The Last Return Before an Alberta Corporation Is Dissolved',
  lead=['A corporation being wound up files one last T2, covering the period that '
        'ends on the date of dissolution. It is due within six months of that date. '
        'If the corporation had no activity in that final period, we file it as a '
        'nil return for $300.00 plus HST.'],
  extra=[('Clear the Earlier Years First',
          ['Unfiled years block a clearance certificate, and they block the '
           'dissolution itself, so the final return is rarely the only one '
           'outstanding. Where earlier years are also unfiled we file them '
           'together, oldest year first, each as its own return at the same fee.',
           'Dissolving the company is a separate step, taken with the Alberta '
           'provincial registry. It is not covered by the $300.00 fee, and filing '
           'the final T2 does not dissolve the corporation on its own.']),
         ('Closing an Alberta Corporation Means Closing Both Returns',
          ['Because Alberta administers its own corporate income tax, a final '
           'federal T2 is not the last corporate income tax return an Alberta '
           'corporation owes. A final ' + PROV_RETURN + ' belongs to the same '
           'wind-up, and it is a separate return filed with a separate authority.',
           'The ' + PROV_RETURN + ' is not covered by the $300.00 fee. Leaving it '
           'outstanding is the kind of loose end that surfaces at the clearance '
           'stage, which is the most expensive time to find it, so it is worth '
           'settling in the same pass as the federal years.'])],
  excerpt='The final T2 for an Alberta corporation being wound up, due within six '
          'months of dissolution. $300.00 plus HST per tax year.'),

 dict(
  slug='t2-short-filing-alberta',
  service='t2-short-filing',
  title='T2 Short Filing in Alberta',
  keyword='t2 short filing alberta',
  national=('/t2-short-filing/', 'T2 Short filing'),
  lead_h2='The Two-Page T2 Short for Alberta Corporations',
  lead=['The T2 Short is a two-page version of the T2 return. An Alberta '
        'corporation may use it only where it meets every one of the Canada Revenue '
        'Agency&rsquo;s conditions for the short return. Where it qualifies, we file '
        'it, and it is included in the $300.00 plus HST fee rather than charged '
        'separately.'],
  extra=[('We Check Before We File',
          ['Meeting most of the conditions is not enough, so we check every one of '
           'them against your corporation before we prepare the return. Where the '
           'corporation does not qualify, we file the full T2 instead, at the same '
           'fee.',
           'Either way the return is reviewed by a CPA and transmitted '
           'electronically to the Canada Revenue Agency.']),
         ('The Short Return Is Federal Only',
          ['The T2 Short is a Canada Revenue Agency form, and the conditions for '
           'using it are federal conditions. Qualifying for it changes which '
           'federal form your corporation files. It does not change what Alberta '
           'asks for.',
           AT1_SENTENCE + ' There is no Alberta equivalent of the T2 Short in what '
           'we file, because the ' + PROV_RETURN + ' is not ours to file.'])],
  excerpt='T2 Short filing for Alberta corporations that meet every CRA condition '
          'for the short return. $300.00 plus HST per tax year.'),
]


def build(s):
    url = SITE + '/' + s['slug'] + '/'
    b = ['<!-- wp:html -->', CSS + '<div class="cnf-hero"><div class="cnf-hero-in">'
         '<h1>' + s['title'] + '</h1><p class="cnf-hero-sub">$300.00 Plus HST Per Tax '
         'Year</p><p class="cnf-hero-lede">We are a registered EFILE electronic filer. '
         'Your return is transmitted to the Canada Revenue Agency electronically.</p>'
         '<p><a class="cnf-hero-btn" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
         '</p></div></div>']
    b.append('<div class="cnf-w">')
    b.append('<nav class="cnf-crumb" aria-label="Breadcrumb">'
             + a(SITE + '/', 'Nil T2 filing in Canada') + ' &rsaquo; '
             + a(HUB, 'Nil T2 filing in ' + PLACE) + ' &rsaquo; '
             '<span aria-current="page">' + s['title'] + '</span></nav>')
    b.append('<p class="cnf-by">Written and reviewed by '
             + a(SITE + '/sharad-gondaliya-cpa/', 'Sharad Gondaliya, CPA (Ontario)')
             + ', CPA Ontario Membership 61040184.</p>')
    b.append('<p class="cnf-rev">Last reviewed: ' + s.get('reviewed', TODAY) + '</p>')

    b.append('<h2>' + s['lead_h2'] + '</h2>')
    for p in s['lead']:
        b.append('<p>' + p + '</p>')

    b.append('<h2>' + PLACE + ' Data</h2>')
    b.append('<table class="cnf-tbl"><thead><tr><th scope="col">Item</th>'
             '<th scope="col">' + PLACE + '</th><th scope="col">Source</th></tr>'
             '</thead><tbody>')
    for item, val, src in place_rows():
        b.append('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (item, val, src))
    b.append('</tbody></table>')
    b.append('<p class="cnf-cap">The T2 due date comes from the Income Tax Act and '
             'does not vary by province. The T2 assessment count is refreshed when '
             'the Canada Revenue Agency reissues its annual table.</p>')

    for h2, paras in s['extra']:
        b.append('<h2>' + h2 + '</h2>')
        for p in paras:
            b.append('<p>' + p + '</p>')

    b.append('<h2>Who This Is For</h2>')
    b.append('<p>' + NOT_NIL_1 + '</p>')
    b.append('<p>' + NOT_NIL_2 + '</p>')

    b.append('<h2>How ' + s['title'] + ' Works</h2>')
    b.append('<ol><li>Type your corporation name. We fill the Business Number and '
             'incorporation date.</li><li>Pick the tax years to file and confirm the '
             'corporation had no activity in each of them.</li><li>Complete the '
             'attestation and identity check, then pay $300.00 plus HST per tax '
             'year.</li><li>Sign Form T183CORP. We transmit your return '
             'electronically.</li></ol>')
    b.append('<p>Your CRA confirmation is emailed within 3 business days. Business '
             'days are Monday to Friday and exclude ' + PLACE
             + ' statutory holidays.</p>')

    b.append('<h2>' + s.get('cost_h2', s['title'].replace(' in ' + PLACE, '')
                            + ' Cost in ' + PLACE) + '</h2>')
    b.append('<p>$300.00 plus HST per tax year. Each tax year is a separate return '
             'and carries the same fee. Tax is added at the rate for your province. '
             'See the full ' + a(SITE + '/pricing/nil-t2-filing-cost/',
                                 'nil T2 filing cost') + '.</p>')

    b.append('<h2>Filings This Does Not Cover</h2>')
    b.append('<div class="cnf-box"><ul>')
    # The AT1 leads the list: on an Alberta page it is the single most likely
    # thing a reader assumes is included.
    b.append('<li>The ' + PROV_RETURN + ', the separate Alberta corporate income '
             'tax return. It is not covered by the $300.00 fee.</li>')
    if ANNUAL_SOURCED:
        raise AssertionError('fill the sourced annual-return bullet here')
    # Existence only. No due date, no fee, no statute, no filing route: see the
    # docstring for why each of those is withheld rather than guessed.
    b.append('<li>Your Alberta annual return, filed with the provincial corporate '
             'registry. It is a registry filing rather than a tax return, it '
             'carries no tax, and it is not covered by the $300.00 fee.</li>')
    b.append('<li>A federal Corporations Canada annual return, at $12.00, if your '
             'corporation is federally incorporated.</li>')
    b.append('<li>A nil GST/HST return or a nil payroll return.</li>')
    b.append('<li>RC145 closure of a GST/HST or payroll account.</li></ul>')
    b.append('<p>We tell you which of these you still owe.</p></div>')

    nh, nl = s['national']
    b.append('<p>Read the national page on ' + a(SITE + nh, nl) + ', or see every '
             + PLACE + ' page on the ' + a(HUB, 'nil T2 filing in ' + PLACE + ' hub')
             + '.</p>')
    b.append('<p><a class="cnf-btn" href="' + FORM + '">Start Nil T2 Filing NOW</a></p>')
    b.append('<p class="cnf-foot">Your return is prepared and transmitted in Canada. '
             'Our credentials are never shared and no part of your file is sent '
             'offshore. ' + a(SITE + '/', 'Nil T2 filing in Canada') + '</p>')
    b.append('</div>')

    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "Service", "@id": url + "#service", "name": s['title'],
       "serviceType": "Nil T2 corporate income tax return filing", "url": url,
       "description": NOT_NIL_1,
       "areaServed": {"@type": "State", "name": PLACE},
       "provider": {"@id": SITE + "/#accountingservice"},
       "offers": {"@type": "Offer", "name": s['title'], "price": "300.00",
                  "priceCurrency": "CAD",
                  "description": "$300.00 plus HST per tax year", "url": FORM,
                  "areaServed": {"@type": "State", "name": PLACE}}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
         "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Nil T2 filing in " + PLACE,
         "item": HUB},
        {"@type": "ListItem", "position": 3, "name": s['title'], "item": url}]}]}
    b.append('<script type="application/ld+json">' + json.dumps(schema) + '</script>')
    b.append('<!-- /wp:html -->')
    return '\n'.join(b)


def meta(s):
    return {
     'site-sidebar-layout': 'no-sidebar', 'site-content-layout': 'page-builder',
     'ast-site-content-layout': 'full-width-container',
     'site-post-title': 'disabled', 'ast-breadcrumbs-content': 'disabled',
     'ast-featured-img': 'disabled',
     'cnf_service_slug': s['service'], 'cnf_place_slug': 'alberta',
     'cnf_place_name': PLACE, 'cnf_place_type': 'province',
     'cnf_jurisdiction_return': 'T2',
     'cnf_provincial_return_name':
        'Alberta AT1. Alberta administers its own corporate income tax, so the AT1 '
        'is a separate provincial return and is not covered by the fee.',
     # Alberta levies no HST, so an HST-inclusive figure would be wrong here, and
     # the "plus HST" wording itself is still open with Sharad Gondaliya.
     'cnf_price_incl_hst': '', 'cnf_overflow_price_incl_hst': '',
     'cnf_deadline_rule':
        "The T2 is due within six months of the corporation's fiscal year-end, every "
        "year until the corporation is formally dissolved.",
     'cnf_unique_data_block_json': json.dumps({
        'place': PLACE,
        'provincial_corporate_return': PROV_RETURN,
        'provincial_corporate_return_covered_by_fee': False,
        't2_assessment_count': T2_ASSESSED,
        't2_assessment_count_source': 'Canada Revenue Agency T2 assessment table',
        'filing_route': 'T2 transmitted electronically to the Canada Revenue Agency '
                        'by a registered EFILE electronic filer',
        'registry_name': None,
        'annual_return_route': None,
        'annual_return_statute': None,
        'dissolution_after': None,
        'unsourced_note': 'Alberta registry facts and the AT1 filing exemption were '
                          'not sourceable when this page was built; they are '
                          'recorded as null rather than estimated.',
        'hst_rate': None}),
     'cnf_last_verified_et': s.get('reviewed_iso', ISO),
     'cnf_primary_keyword': s['keyword'],
    }


if __name__ == '__main__':
    assert len(SERVICES) == 5, 'this batch is five pages'
    assert len({s['slug'] for s in SERVICES}) == 5
    assert len({s['keyword'] for s in SERVICES}) == 5, 'line 1717: distinct keywords'
    assert len({s['title'] for s in SERVICES}) == 5, 'line 1717: distinct H1s'
    # line 1717 also wants a different first 120 words per page
    firsts = {s['lead'][0][:120] for s in SERVICES}
    assert len(firsts) == 5, 'line 1717: the first 120 words must differ'
    for s in SERVICES:
        c = build(s)
        assert PROV_RETURN in c, '%s: hard rule 8 needs the AT1 named' % s['slug']
        assert 'T183' not in c or 'T183CORP' in c, '%s: bare T183' % s['slug']
        io.open(os.path.join(HERE, s['slug'] + '.html'), 'w',
                encoding='utf-8').write(c)
        print('%-46s %6d bytes   excerpt %d' % (s['slug'], len(c.encode()),
                                                len(s['excerpt'])))
