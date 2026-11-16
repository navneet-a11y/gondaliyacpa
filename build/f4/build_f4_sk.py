# -*- coding: utf-8 -*-
"""Family 4 service x place pages for Saskatchewan: the first five.

Navneet, 2026-11-16: "start next jurisdiction with 5 of its pages and hub".
Saskatchewan is next by corporate population among the nine jurisdictions left
after Quebec closed, and the five are the five every province has opened with:
nil-t2-filing, catch-up, dormant, final-t2-before-dissolution and
t2-short-filing.

Design, CSS, section order, schema shape and the not-nil wording are imported
from build_f4_bc rather than copied, so the provinces cannot drift apart. The
container fix is imported from build_f4_qc for the same reason.

SASKATCHEWAN HAS NO SEPARATE PROVINCIAL RETURN, AND THAT IS THE CLAIM.
Only Quebec and Alberta administer their own corporate income tax. Everywhere
else, including Saskatchewan, provincial corporate income tax is collected
through the federal T2, so the return we file settles both levels. Plan line
1212 requires this to be stated rather than left out: a reader who has heard
that Alberta files an AT1 will wonder what Saskatchewan's equivalent is, and
the answer is that there isn't one.

THE PAGES ARE BUILT AROUND SASKATCHEWAN'S OWN NUMBER, NOT A TEMPLATE.
British Columbia is the other large province with no separate return, so these
five had to be written away from the British Columbia pages or they would have
collapsed into a placename swap -- the failure 6(k) sets its 0.60 threshold to
catch, and the one that produced four Atlantic cost pages at 0.94 to 0.96.

What is different about Saskatchewan is the shape of its series. Among the
provinces that grew at all over 2018 to 2023, only Alberta grew more slowly,
and Saskatchewan's count peaked before the series ended: 73,770 in 2022, down
to 73,110 in 2023. A corporate population that turns down is dissolutions
completing, and a
dissolution cannot complete while a tax year is still unfiled. So these pages
are written from the closing end of a corporation's life rather than the
opening end, which is where the British Columbia pages sit.

Every comparative claim in the Saskatchewan paragraph is re-asserted against
docs/seo/cra-t2-jurisdiction-counts.json at build time, below. An earlier pass
on another province shipped three comparative claims that the table did not
support, so no claim of that kind is trusted here because it was written down
once.

WHAT THESE PAGES DO NOT SAY, AND WHY.
www.saskatchewan.ca, corporateregistry.isc.ca and www.isc.ca are all denied by
the environment's network policy (no CONNECT at the agent proxy), so the
Corporate Registry pages and The Business Corporations Act could not be read.
None of the following appears anywhere: the Saskatchewan annual return's due
date, its fee, its statutory authority, its filing route, or how long
non-filing runs before the registrar may dissolve a corporation. The pages say
the annual return exists, is a registry filing rather than a tax return,
carries no tax and is not covered by the fee. Each of those is true by the
nature of a registry filing and none of them is a figure. The Alberta
precedent in build_f4_ab is that an unsourceable fact is withheld, not
estimated.

PRICE. Saskatchewan charges GST plus PST, not HST, so the fee reads "$300.00
plus applicable sales tax per tax year" per Navneet's 2026-11-12 instruction,
and no rate and no tax-inclusive total appears.
"""
import io, json, os

from build_f4_bc import NOT_NIL_1, NOT_NIL_2, a, SITE, FORM
from build_f4_qc import CSS           # the 2026-11-12 container fix

import jur_data as JD

HERE = os.path.dirname(os.path.abspath(__file__))
PLACE_SLUG = 'saskatchewan'
J = JD.BY_SLUG[PLACE_SLUG]
PLACE, SHORT = J['name'], J['short']
HUB = SITE + J['hub']
TODAY, ISO = 'November 16, 2026', '2026-11-16'

FEE = JD.fee(PLACE_SLUG)              # $300.00 plus applicable sales tax per tax year
FEE_TITLE = JD.fee_title(PLACE_SLUG)
OVERFLOW = JD.overflow(PLACE_SLUG)
PROV_RETURN = JD.prov_return(PLACE_SLUG)        # None: no separate return
PLACE_PARA = JD.trajectory(PLACE_SLUG, PLACE)

assert PROV_RETURN is None, 'Saskatchewan must not acquire a separate return'

# Saskatchewan is not an HST province, so the imported not-nil block's overflow
# fee is restated without naming HST. The wording is otherwise untouched.
NOT_NIL_2_SK = NOT_NIL_2.replace('$350.00 plus HST per tax year', OVERFLOW)
assert 'HST' not in NOT_NIL_2_SK

# Section 7.4: the penalty position never appears without the whole
# qualification block. One definition, used wherever a penalty is mentioned.
QUAL = ('A true nil return carries no percentage late-filing penalty, because '
        'that penalty is a percentage of tax owing and the corporation owes '
        '$0.00. The unfiled year still stays open forever, invites a demand to '
        'file and an arbitrary assessment, blocks a clearance certificate and '
        'dissolution, and costs a non-resident-owned corporation $25.00 per '
        'day up to $2,500.00.')

# The Saskatchewan counterpart to Quebec's CO-17 block: the thing a reader
# most needs to know, which here is that there is nothing else to file.
ONE_RETURN = (
 'Saskatchewan does not run a corporate income tax of its own. Provincial '
 'corporate income tax is collected through the federal T2, so the one return '
 'we prepare settles the Saskatchewan side and the federal side together. '
 'Only Quebec and Alberta are otherwise, and a Saskatchewan corporation has no '
 'equivalent of the Quebec CO-17 or the Alberta AT1 waiting behind the T2.')

# The twelve cnf_service terms, verbatim from plan line 304. Five are built
# here; the list is checked in full so a typo fails the build.
SERVICE_SLUGS = (
 'nil-t2-filing', 'catch-up-nil-t2-filing', 'dormant-corporation-filing',
 'final-t2-before-dissolution', 't2-short-filing', 'nil-t2-filing-cost',
 'unfiled-corporate-tax-returns', 'no-activity-corporation-tax-return',
 'numbered-corporation-nil-filing', 'inactive-holding-corporation-t2-filing',
 'nil-t2-filing-deadline', 'nil-t2-filing-for-non-resident-owned-corporations')

SERVICES = [

 dict(
  slug='nil-t2-filing-saskatchewan',
  service='nil-t2-filing',
  title='Nil T2 Filing in Saskatchewan',
  keyword='nil t2 filing saskatchewan',
  national=('/nil-t2-filing/', 'nil T2 filing'),
  lead_h2='One Return Settles Both Levels of Tax',
  lead=['Where a Saskatchewan corporation had no activity in a tax year, the '
        'return it still owes is the federal T2, and that single return is '
        'the whole of its corporate income tax obligation. It is due within '
        'six months of the fiscal year-end, in that year and in every year '
        'after it, until the corporation is formally dissolved. Having earned '
        'nothing changes what goes on the return and changes nothing about '
        'whether it is owed. We prepare it, a CPA reviews it, and we transmit '
        'it electronically for ' + FEE + '.',
        ONE_RETURN],
  extra=[('What Makes a Return Nil',
          ['A nil return reports no income and no expenses for the tax year. '
           'The corporation still exists, still has a Business Number, and '
           'still has a fiscal year-end, so the return is still due. Filing '
           'it keeps the corporation&rsquo;s tax record current and keeps its '
           'standing with the Canada Revenue Agency intact.']),
         ('A Quiet Year Is Not an Exemption',
          ['The commonest reason a Saskatchewan corporation falls behind is '
           'not a decision to stop filing. It is that nothing happened, so '
           'nothing prompted anyone, and a year went by without a return the '
           'Agency was still expecting. Nothing arrives to say a year has '
           'been missed until the Agency notices, and by then it is usually '
           'more than one.',
           'An unfiled nil year does not close itself with time. It stays '
           'open, and it is still there when somebody wants to sell the '
           'corporation, borrow against it, or wind it up.'])],
  excerpt='Nil T2 filing for Saskatchewan corporations with no activity in '
          'the tax year. ' + FEE + '.'),

 dict(
  slug='catch-up-nil-t2-filing-saskatchewan',
  service='catch-up-nil-t2-filing',
  title='Catch-Up Nil T2 Filing in Saskatchewan',
  keyword='catch-up nil t2 filing saskatchewan',
  national=('/catch-up-nil-t2-filing/', 'catch-up nil T2 filing'),
  lead_h2='Several Saskatchewan Years at Once, Oldest First',
  lead=['Years behind do not merge. Four missed years are four separate T2 '
        'returns, each for its own tax year, each carrying its own '
        'preparation and its own CPA review, and each at ' + FEE + '. We file '
        'them in the order they fell due, oldest first, because the Canada '
        'Revenue Agency carries figures forward from one year into the next '
        'and a year filed out of sequence can be assessed against a balance '
        'the Agency has not yet been told about.',
        'Two years is $600.00, three is $900.00 and five is $1,500.00, each '
        'before tax. There is no reduced rate for filing several together, '
        'and the age of a year does not change its price.'],
  extra=[('What the Catch-Up Reaches, and What It Does Not',
          ['Every year in which the corporation had no activity can be filed '
           'this way, however far back it goes. A year in which something did '
           'happen is a different return and is not nil: we tell you which '
           'years fall on which side before you pay, not after.',
           'What it does not reach is a second provincial return, because '
           'Saskatchewan has none. Provincial corporate income tax is '
           'collected through the federal T2, so bringing the T2 series '
           'current brings the whole corporate income tax position current '
           'with it.']),
         ('The Position on Penalties, in Full',
          [QUAL,
           'That is the whole of it, and it is the reason catching up is '
           'worth doing in one pass rather than one year at a time. The '
           'exposure on a nil year is not a bill; it is that the year stays '
           'open and blocks things that need every year closed.'])],
  excerpt='Every unfiled Saskatchewan tax year brought up to date, oldest '
          'year first. ' + FEE + '.'),

 dict(
  slug='dormant-corporation-filing-saskatchewan',
  service='dormant-corporation-filing',
  title='Dormant Corporation Filing in Saskatchewan',
  keyword='dormant corporation filing saskatchewan',
  national=('/dormant-corporation-filing/', 'dormant corporation filing'),
  lead_h2='Dormant Is a Description, Not a Status',
  lead=['A dormant Saskatchewan corporation is one that is doing nothing. '
        'That is a description of its activity, not a standing the Canada '
        'Revenue Agency grants it and not something anybody registers. The '
        'corporation exists, it keeps its Business Number, it keeps its '
        'fiscal year-end, and it keeps filing a T2 within six months of that '
        'year-end, for ' + FEE + ', until it is formally dissolved.',
        'Stopping trading is not the same act as closing a company, and only '
        'the second one ends the filing obligation. A corporation left '
        'dormant and unfiled is still accruing missed years.'],
  extra=[('Dormant, Inactive, Nil: What the Words Do',
          ['Dormant and inactive describe the corporation. Nil describes the '
           'return. A dormant corporation files a nil return, but the two '
           'words answer different questions, and only the second has any '
           'bearing on what gets transmitted.',
           'The distinction matters at one point: a corporation can be '
           'dormant in the ordinary sense and still have a return that is not '
           'nil, because a dollar of bank interest is income. Dormancy is '
           'about intention. Nil is about the ledger.']),
         ('What Still Runs While a Corporation Sits',
          [ONE_RETURN,
           'The Saskatchewan annual return with the provincial registry is a '
           'different filing again, and it carries on through a dormant '
           'period as well. It is a registry filing rather than a tax return, '
           'it carries no tax, and it is not covered by the fee.'])],
  excerpt='A dormant Saskatchewan corporation files a T2 every year until it '
          'is dissolved. ' + FEE + '.'),

 dict(
  slug='final-t2-before-dissolution-saskatchewan',
  service='final-t2-before-dissolution',
  title='Final T2 Before Dissolution in Saskatchewan',
  keyword='final t2 before dissolution saskatchewan',
  national=('/final-t2-before-dissolution/', 'final T2 before dissolution'),
  lead_h2='Closing a Saskatchewan Corporation Needs Every Year Filed',
  lead=['A corporation being wound up files a final T2 for the period ending '
        'on dissolution, due within six months of that date. The final '
        'return is rarely the obstacle. What holds a dissolution up is the '
        'years behind it: a clearance certificate will not issue while any '
        'tax year is outstanding, and an outstanding nil year counts as much '
        'as any other. Each year is ' + FEE + '.',
        'This is the end of the process people reach and find blocked. The '
        'decision to close has been made, the corporation has done nothing '
        'for years, and the thing standing in the way is a stack of returns '
        'nobody filed because there was nothing to report.'],
  extra=[('What the Saskatchewan Numbers Show About This',
          ['Saskatchewan is one of the provinces whose corporate population '
           'has started to come down rather than up, and a falling count is '
           'dissolutions completing. Those are corporations that got to the '
           'end of this process. The ones that have not are the ones with a '
           'year still open.',
           'We file every outstanding year and the final return together, so '
           'the sequence that has to be clean is clean before the clearance '
           'certificate is applied for.']),
         ('The Order These Things Happen In',
          ['Outstanding years are filed first, oldest to newest. The final '
           'return for the short period ending on dissolution is filed last. '
           'Only then is the clearance certificate worth applying for, '
           'because the Agency will check the whole series.',
           'There is no second series to close out alongside it. Saskatchewan '
           'corporate income tax is collected through the federal T2, so a '
           'corporation being wound up here has one set of returns to bring '
           'current, where a Quebec or Alberta corporation has two.',
           QUAL])],
  excerpt='A final T2 is due within six months of dissolution, and unfiled '
          'years block it. ' + FEE + '.'),

 dict(
  slug='t2-short-filing-saskatchewan',
  service='t2-short-filing',
  title='T2 Short Filing in Saskatchewan',
  keyword='t2 short filing saskatchewan',
  national=('/t2-short-filing/', 'T2 Short filing'),
  lead_h2='Which Form a Saskatchewan Nil Year Goes On',
  lead=['The T2 Short is a two-page version of the T2 that a corporation may '
        'use where it meets every one of the Canada Revenue Agency&rsquo;s '
        'conditions for it. Many nil Saskatchewan corporations do. Working '
        'out whether yours is one of them is our job rather than yours, and '
        'the answer does not change the price: the T2 Short is included in '
        'the ' + FEE + ' fee, not charged at a discount and not charged as an '
        'extra.',
        'A corporation that does not qualify is filed on the full T2 at the '
        'same fee. Nothing about the quote depends on which form the year '
        'ends up on.'],
  extra=[('Eligibility Is Tested Per Year, Not Per Corporation',
          ['A corporation can qualify for the T2 Short in one tax year and '
           'not in the next. The conditions are tested against each year on '
           'its own, so a catch-up covering several years can transmit some '
           'of them on the short return and some on the full one.',
           'That is a detail of preparation rather than a decision anybody '
           'has to make. We test each year as we reach it.']),
         ('What the Short Return Does Not Shorten',
          ['Using the T2 Short does not reduce the schedules a year genuinely '
           'needs. GIFI Schedules 100, 125 and 141 are required where they '
           'are required, Schedule 24 is required on a first return, and '
           'Schedule 50 is required for every shareholder at 10 per cent or '
           'more. All of them are included in the fee.',
           'Nor does it shorten the list of returns owed, though in '
           'Saskatchewan that list is already short: provincial corporate '
           'income tax is collected through the federal T2, so whichever form '
           'the year goes on, that form is the only corporate income tax '
           'return the year needs.'])],
  excerpt='The T2 Short for a qualifying Saskatchewan corporation, at the '
          'same fee as the full return. ' + FEE + '.'),

]


def build(s):
    url = SITE + '/' + s['slug'] + '/'
    b = ['<!-- wp:html -->', CSS + '<div class="cnf-hero"><div class="cnf-hero-in">'
         '<h1>' + s['title'] + '</h1><p class="cnf-hero-sub">' + FEE_TITLE +
         '</p><p class="cnf-hero-lede">We are a registered EFILE electronic '
         'filer. Your return is transmitted to the Canada Revenue Agency '
         'electronically.</p>'
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

    # Plan line 1212: the place data row and the place paragraph.
    b.append('<h2>' + PLACE + ' Data</h2>')
    b.append('<table class="cnf-tbl"><thead><tr><th scope="col">Item</th>'
             '<th scope="col">' + PLACE + '</th><th scope="col">Source</th></tr>'
             '</thead><tbody>')
    for item, val, src in JD.place_rows(PLACE_SLUG, PLACE):
        b.append('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (item, val, src))
    b.append('</tbody></table>')
    b.append('<p>' + PLACE_PARA + '</p>')
    b.append('<p class="cnf-cap">The T2 due date comes from the Income Tax Act '
             'and does not vary by province. Corporation counts are the Canada '
             'Revenue Agency&rsquo;s own, rounded to the nearest ten, taken '
             'from the jurisdiction code on the T2 return, and they include '
             'tax-exempt and inactive corporations. They are refreshed when '
             'the Canada Revenue Agency reissues the table.</p>')

    for h2, paras in s['extra']:
        b.append('<h2>' + h2 + '</h2>')
        for p in paras:
            b.append('<p>' + p + '</p>')

    b.append('<h2>Who This Is For</h2>')
    b.append('<p>' + NOT_NIL_1 + '</p>')
    b.append('<p>' + NOT_NIL_2_SK + '</p>')

    b.append('<h2>How ' + s['title'] + ' Works</h2>')
    b.append('<ol><li>Type your corporation name. We fill the Business Number '
             'and incorporation date.</li><li>Pick the tax years to file and '
             'confirm the corporation had no activity in each of them.</li>'
             '<li>Complete the attestation and identity check, then pay '
             '$300.00 plus applicable sales tax per tax year.</li><li>Sign '
             'Form T183CORP. We transmit your return electronically.</li></ol>')
    b.append('<p>Your CRA confirmation is emailed within 3 business days. '
             'Business days are Monday to Friday and exclude ' + PLACE
             + ' statutory holidays.</p>')

    b.append('<h2>' + s.get('cost_h2', s['title'].replace(' in ' + PLACE, '')
                            + ' Cost in ' + PLACE) + '</h2>')
    b.append('<p>' + FEE + '. Each tax year is a separate return and carries '
             'the same fee. The sales tax that applies where your corporation '
             'is resident is added at checkout. See the full '
             + a(SITE + '/pricing/nil-t2-filing-cost/', 'nil T2 filing cost')
             + '.</p>')

    b.append('<h2>Filings This Does Not Cover</h2>')
    b.append('<div class="cnf-box"><ul>')
    # Existence only. No due date, no fee, no statute, no filing route and no
    # dissolution threshold: see the docstring for why each is withheld.
    b.append('<li>Your Saskatchewan annual return with the provincial '
             'registry. It is a registry filing rather than a tax return, it '
             'carries no tax, and it is not covered by the $300.00 fee.</li>')
    b.append('<li>A federal Corporations Canada annual return, at $12.00, if '
             'your corporation is federally incorporated.</li>')
    b.append('<li>A nil GST/HST return or a nil payroll return.</li>')
    b.append('<li>RC145 closure of a GST/HST or payroll account.</li></ul>')
    b.append('<p>We tell you which of these you still owe.</p></div>')

    nh, nl = s['national']
    b.append('<p>Read the national page on ' + a(SITE + nh, nl) + ', or see '
             'every ' + PLACE + ' page on the '
             + a(HUB, 'nil T2 filing in ' + PLACE + ' hub') + '.</p>')
    b.append('<p><a class="cnf-btn" href="' + FORM + '">Start Nil T2 Filing NOW</a></p>')
    b.append('<p class="cnf-foot">Your return is prepared and transmitted in '
             'Canada. Our credentials are never shared and no part of your '
             'file is sent offshore. ' + a(SITE + '/', 'Nil T2 filing in Canada')
             + '</p>')
    b.append('</div>')

    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "Service", "@id": url + "#service", "name": s['title'],
       "serviceType": "Nil T2 corporate income tax return filing", "url": url,
       "description": NOT_NIL_1,
       "areaServed": {"@type": "State", "name": PLACE},
       "provider": {"@id": SITE + "/#accountingservice"},
       "offers": {"@type": "Offer", "name": s['title'], "price": "300.00",
                  "priceCurrency": "CAD",
                  "description": FEE, "url": FORM,
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
     'cnf_service_slug': s['service'], 'cnf_place_slug': PLACE_SLUG,
     'cnf_place_name': PLACE, 'cnf_place_type': J['ptype'],
     'cnf_jurisdiction_return': 'T2',
     'cnf_provincial_return_name':
        'None. Saskatchewan corporate income tax is collected through the '
        'federal T2 return.',
     # Saskatchewan charges GST plus PST, so an HST-inclusive figure would name
     # the wrong tax. Left empty rather than filled with a figure that is
     # wrong; the schema gap is open with Sharad Gondaliya.
     'cnf_price_incl_hst': '', 'cnf_overflow_price_incl_hst': '',
     'cnf_price': FEE, 'cnf_overflow_price': OVERFLOW,
     'cnf_deadline_rule':
        "The T2 is due within six months of the corporation's fiscal year-end, "
        "every year until the corporation is formally dissolved.",
     'cnf_unique_data_block_json': json.dumps(
        JD.unique_block(PLACE_SLUG, PLACE, J['ptype'])),
     'cnf_last_verified_et': s.get('reviewed_iso', ISO),
     'cnf_primary_keyword': s['keyword'],
    }


def _recheck_place_claims():
    """Re-assert the Saskatchewan paragraph's claims against the CRA table.

    Written because an earlier province shipped three comparative claims the
    table did not support. A sentence that was checked once by hand is not
    checked; a sentence the build re-derives is.
    """
    TERR = {'yukon', 'northwest-territories', 'nunavut'}
    prov = {k: v for k, v in JD._CRA['jurisdictions'].items() if k not in TERR}
    sk = prov[PLACE_SLUG]
    assert sk['counts'][-1] == 73110 and sk['counts'][0] == 70550, sk
    # "Among the provinces that grew at all over those six years, only Alberta
    # grew more slowly." Newfoundland and Labrador shrank, so it is not a
    # counter-example; an earlier draft said "any province except Alberta",
    # which that province falsified.
    grew = {k: (v['counts'][-1] - v['counts'][0]) / v['counts'][0]
            for k, v in prov.items() if v['counts'][-1] > v['counts'][0]}
    slower = sorted(k for k, g in grew.items() if g < grew[PLACE_SLUG])
    assert slower == ['alberta'], slower
    # "it reached 73,770 in 2022 and gave back 660 of that in 2023"
    assert sk['peak'] == 73770 and sk['peak_year'] == 2022, sk
    assert sk['peak'] - sk['counts'][-1] == 660, sk
    # The docstring says Saskatchewan peaked before the series ended. An
    # earlier draft of it claimed Saskatchewan was one of only two provinces
    # under three per cent growth; this check rejected that, because
    # Saskatchewan is at 3.6 per cent. The sentence was rewritten, not the
    # check.
    assert (sk['counts'][-1] - sk['counts'][0]) / sk['counts'][0] > 0.03
    assert sk['peak_year'] < sk['years'][-1], sk
    for n in ('73,110', '70,550', '73,770', '660'):
        assert n in PLACE_PARA, n


if __name__ == '__main__':
    N = 5
    _recheck_place_claims()
    assert len(SERVICES) == N, 'Saskatchewan opens with five, as every province has'
    assert len({s['slug'] for s in SERVICES}) == N
    assert len({s['service'] for s in SERVICES}) == N, 'one page per cnf_service'
    assert len({s['keyword'] for s in SERVICES}) == N, 'line 1717: distinct keywords'
    assert len({s['title'] for s in SERVICES}) == N, 'line 1717: distinct H1s'
    firsts = {s['lead'][0][:120] for s in SERVICES}
    assert len(firsts) == N, 'line 1717: the first 120 words must differ'
    # Every service slug must be one of the twelve line 304 fixes.
    assert set(s['service'] for s in SERVICES) <= set(SERVICE_SLUGS), (
        'service slugs do not match line 304: %s'
        % sorted({s['service'] for s in SERVICES} - set(SERVICE_SLUGS)))
    for s in SERVICES:
        c = build(s)
        assert 'T183' not in c or 'T183CORP' in c, '%s: bare T183' % s['slug']
        # Saskatchewan charges no HST. "GST/HST" is the name of the CRA account
        # and is not a price claim, so it is removed before the test.
        assert 'HST' not in c.replace('GST/HST', ''), '%s: names HST' % s['slug']
        # Hard rule 8's converse: the page must say there is no separate
        # provincial return rather than leave the subject out.
        assert 'collected through the federal T2' in c, (
            '%s: must state that provincial corporate income tax is collected '
            'through the federal T2' % s['slug'])
        io.open(os.path.join(HERE, s['slug'] + '.html'), 'w',
                encoding='utf-8').write(c)
        print('%-46s %6d bytes   excerpt %d' % (s['slug'], len(c.encode()),
                                                len(s['excerpt'])))
