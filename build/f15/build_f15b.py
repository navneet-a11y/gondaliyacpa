# -*- coding: utf-8 -*-
"""Family 15: /how-it-works/ and /faq/.

Navneet, 2026-11-12: "also, create these 28. How It Works, FAQ, About, Refund
Policy if you have data for it", then "we already have about check other 3".

ABOUT is live at /about/ (page 319) and is not rebuilt.

REFUND POLICY IS NOT BUILT, AND THIS IS WHY.
CLAUDE.md puts "legal page text (supplied by Sharad Gondaliya and published as
supplied)" out of scope, and Section 7.9 gives Family 15 to Sharad Gondaliya as
its owner. The only refund wording that exists anywhere on the site is one
sentence inside the not-nil block: "If we find it after you pay, we refund you
in full." A refund policy needs what that sentence does not say -- the window,
what stops being refundable once a return is transmitted to the Canada Revenue
Agency, how a refund is paid back, and how it connects to
/complaints-and-resolution/. Writing those would be inventing the firm's
contractual terms, which is not a drafting gap this build can close. It is
listed for Sharad Gondaliya instead.

WHICH FAMILY 15 LIST THESE COME FROM.
decisions.md 2026-09-28 records that 6(a) and Appendix A give two disjoint
Family 15 sets sharing only three slugs, and that Sharad Gondaliya picks the
set. /how-it-works/ and /faq/ are both Appendix A slugs and appear nowhere in
6(a). They are built on Navneet's instruction naming them directly, and they
are the first two Family 15 pages taken from the Appendix A side of that
unresolved split, which is worth his attention when he rules: building these
two leans the list toward Appendix A.

/how-it-works/ reproduces the ten-step strip from Section 2.8 verbatim and in
order. Line 1225 makes the home page the single source for the flow and says
it is "never reordered", so this page copies it rather than paraphrasing it.
The one departure is the fee line: 2.8 reads "$300.00 including HST per tax
year", which the 2026-09-30 decision replaced, and a national page cannot name
HST because eight of the thirteen jurisdictions do not charge it. It reads
"$300.00 plus applicable sales tax per tax year", which is accurate in all
thirteen. The home page and /pricing/ still say "plus HST" nationally; that is
flagged in decisions.md rather than changed here.

/faq/ answers each question in two or three sentences and links to the Family 5
answer page that carries the full version. It deliberately does not reproduce
those answers: 46 of them are live, and a page that restated them would be the
duplicate pattern 6(k) exists to catch. Hard rule 6 bans FAQPage markup, so
none is emitted -- per decisions.md, "the question format stays, the markup
goes" -- and the visible disclosure markup matches the jurisdiction hubs.
"""
import io, json, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'f4'))
from build_f4_bc import CSS as _CSS, a, SITE, FORM

# The Family 4 style block defines neither the ordered-step list nor the FAQ
# disclosure, so the ten-step strip and every question on /faq/ would have
# rendered unstyled. Same defect the Family 10 build hit with .cnf-qual and
# .cnf-steps. The .cnf-faq rules are the ones already live on the jurisdiction
# hubs, copied so the two pages cannot drift from them; the assertion at the
# bottom of this file fails the build if a class is used without a rule.
_EXTRA = (
 "\n.cnf-steps{margin:16px 0 16px 22px;padding:0}"
 "\n.cnf-steps li{margin:0 0 10px}"
 "\n.cnf-faq{margin:0}"
 "\n.cnf-faq details{border:0;border-radius:14px;background:#fff;"
 "margin:0 0 14px;box-shadow:0 2px 14px rgba(17,34,68,.08)}"
 "\n.cnf-faq summary{cursor:pointer;list-style:none;display:flex;"
 "justify-content:space-between;align-items:center;gap:16px;padding:22px 28px}"
 "\n.cnf-faq summary h3{margin:0;font-family:Poppins,sans-serif;"
 "font-weight:700;font-size:19px;color:#314d8a;line-height:1.4}"
 "\n.cnf-faq summary::-webkit-details-marker{display:none}"
 "\n.cnf-faq summary::after{content:'+';font-weight:400;font-size:28px;"
 "line-height:1;color:#2087c9;flex-shrink:0;transition:transform .15s ease}"
 "\n.cnf-faq details[open] summary::after{transform:rotate(45deg)}"
 "\n.cnf-faq .cnf-faq-a{padding:0 28px 24px}"
 "\n.cnf-faq .cnf-faq-a p{margin:0;line-height:1.7}")

assert _CSS.rstrip().endswith('</style>')
CSS = _CSS.rstrip()[:-len('</style>')] + _EXTRA + '</style>'


HERE = os.path.dirname(os.path.abspath(__file__))
TODAY, ISO = 'November 12, 2026', '2026-11-12'
FEE = '$300.00 plus applicable sales tax per tax year'
FEE_TITLE = '$300.00 Plus Applicable Sales Tax Per Tax Year'

# Section 2.8, verbatim and in order. Line 1225: never reordered.
STEPS = [
 'Type your corporation name.',
 'We fill in your CRA Business Number and incorporation date.',
 'Pick the tax years you have not filed.',
 'Confirm the corporation had no activity.',
 'Attest that you are an authorized signing officer and pass the identity '
 'check.',
 'Pay by credit card, debit, Apple Pay or Google Pay.',
 'We prepare the return, generate your Form T183CORP, and send you a '
 'single-use signing link.',
 'You sign on a secure access-controlled screen.',
 'A CPA reviews it and files it electronically.',
 'Your CRA confirmation arrives by email within 3 business days.',
]

# Section 7.4: the penalty position never appears without the qualification.
QUAL = ('A true nil return carries no percentage late-filing penalty, because '
        'that penalty is a percentage of tax owing and the corporation owes '
        '$0.00. The unfiled year still stays open forever, invites a demand to '
        'file and an arbitrary assessment, blocks a clearance certificate and '
        'dissolution, and costs a non-resident-owned corporation $25.00 per '
        'day up to $2,500.00.')

FAQ = [
 ('Does an inactive corporation still have to file a T2?',
  ['Yes. A corporation files a T2 for every tax year it exists, within six '
   'months of its fiscal year-end, whether or not it earned anything. Being '
   'inactive changes what the return says, not whether it is due. The '
   'obligation stops only when the corporation is formally dissolved.'],
  '/answers/do-i-need-to-file-a-t2-if-my-corporation-had-no-activity/',
  'the full answer on filing with no activity'),

 ('What happens if I do not file a nil T2?',
  ['The year stays open indefinitely. The Canada Revenue Agency can issue a '
   'demand to file and then assess the corporation arbitrarily on figures of '
   'its own.', QUAL],
  '/answers/what-happens-if-i-dont-file-a-nil-t2/',
  'what happens if you do not file'),

 ('How many unfiled years can I file at once?',
  ['There is no cap. We file them together, oldest year first, because a T2 '
   'carries forward figures from the year before it and the years have to be '
   'assessed in order. Each tax year is a separate return and carries the '
   'same fee.'],
  '/answers/how-many-years-of-unfiled-t2-returns-can-i-catch-up/',
  'catching up on unfiled years'),

 ('Can I e-sign Form T183CORP?',
  ['Yes. You sign on a secure access-controlled screen reached through a '
   'single-use link, and the signature carries a date and a timestamp. The '
   'form has to be signed by a signing officer of the corporation before the '
   'return is transmitted.'],
  '/answers/can-i-e-sign-a-t183corp/',
  'how T183CORP signing works'),

 ('Do I need financial statements for a nil return?',
  ['A nil return reports no income and no expenses, so there are no figures '
   'to draw from a set of statements. Which GIFI schedules are required '
   'depends on the corporation, and we work that out from the year being '
   'filed rather than asking you for bookkeeping you do not have.'],
  '/answers/do-i-need-financial-statements-for-a-nil-t2-return/',
  'whether statements are needed'),

 ('Is my corporation nil?',
  ['A corporation with investment income, rental income, or dividends paid or '
   'received is not nil, and nor is a holding corporation earning anything on '
   'what it holds. Neither is a corporation that is not a '
   'Canadian-controlled private corporation, an amalgamation, or one already '
   'dissolved or struck. We check before you pay, and if we find it '
   'afterwards we refund you in full.'],
  '/answers/do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive/',
  'when a corporation counts as inactive'),

 ('How long does it take?',
  ['Your CRA confirmation arrives by email within 3 business days of '
   'transmission. Business days are Monday to Friday. Filing several years '
   'together does not change that window, because the years are transmitted '
   'together.'],
  '/answers/how-long-does-it-take-to-file-a-nil-t2-return/',
  'how long a nil T2 takes'),

 ('Does filing dissolve the corporation?',
  ['No. Filing brings the corporation&rsquo;s tax record up to date and '
   'leaves the corporation in existence. Dissolution is a separate step, and '
   'it needs its own final return plus every earlier year filed before a '
   'clearance certificate can be issued.'],
  '/answers/when-should-i-dissolve-a-dormant-corporation/',
  'when to dissolve a dormant corporation'),
]


def shell(h1, sub, crumb_label, body, url, title, desc, keyword):
    b = ['<!-- wp:html -->', CSS +
         '<div class="cnf-hero"><div class="cnf-hero-in"><h1>' + h1 + '</h1>'
         '<p class="cnf-hero-sub">' + sub + '</p>'
         '<p class="cnf-hero-lede">We are a registered EFILE electronic filer. '
         'Your return is transmitted to the Canada Revenue Agency '
         'electronically.</p>'
         '<p><a class="cnf-hero-btn" href="' + FORM + '">Start Nil T2 Filing '
         'NOW</a></p></div></div>']
    b.append('<div class="cnf-w">')
    b.append('<nav class="cnf-crumb" aria-label="Breadcrumb">'
             + a(SITE + '/', 'Nil T2 filing in Canada') + ' &rsaquo; '
             '<span aria-current="page">' + crumb_label + '</span></nav>')
    b.append('<p class="cnf-by">Written and reviewed by '
             + a(SITE + '/sharad-gondaliya-cpa/',
                 'Sharad Gondaliya, CPA (Ontario)')
             + ', CPA Ontario Membership 61040184.</p>')
    b.append('<p class="cnf-rev">Last reviewed: ' + TODAY + '</p>')
    b.extend(body)
    b.append('<p><a class="cnf-btn" href="' + FORM + '">Start Nil T2 Filing '
             'NOW</a></p>')
    b.append('<p class="cnf-foot">Your return is prepared and transmitted in '
             'Canada. Our credentials are never shared and no part of your '
             'file is sent offshore. ' + a(SITE + '/', 'Nil T2 filing in Canada')
             + '</p>')
    b.append('</div>')
    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "WebPage", "@id": url + "#page", "url": url, "name": title,
       "description": desc, "inLanguage": "en-CA", "dateModified": ISO,
       "author": {"@type": "Person", "name": "Sharad Gondaliya",
                  "honorificSuffix": "CPA",
                  "url": SITE + "/sharad-gondaliya-cpa/"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
         "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": crumb_label,
         "item": url}]}]}
    b.append('<script type="application/ld+json">' + json.dumps(schema)
             + '</script>')
    b.append('<!-- /wp:html -->')
    return '\n'.join(b)


def how_it_works():
    url = SITE + '/how-it-works/'
    body = []
    body.append('<h2>One Screen, Start to Finish</h2>')
    body.append('<p>Nil T2 filing here is a form, not an appointment. You type '
                'your corporation name, we fill in what the Canada Revenue '
                'Agency already knows, you pick the unfiled years and confirm '
                'there was no activity in each, and you pay. We prepare the '
                'return, a CPA reviews it, you sign Form T183CORP, and we '
                'transmit it. The fee is ' + FEE + '.</p>')
    body.append('<p>No meeting. No booking link. No email chain. One screen, '
                'start to finish.</p>')

    body.append('<h2>The Ten Steps, In Order</h2>')
    body.append('<ol class="cnf-steps">')
    for s in STEPS:
        body.append('<li>' + s + '</li>')
    body.append('</ol>')
    body.append('<p class="cnf-cap">The order is fixed. Nothing in it is '
                'skipped and nothing is reordered, because each step depends '
                'on the one before it: the return cannot be prepared before '
                'the years are chosen, and Form T183CORP cannot carry the '
                'return&rsquo;s figures before the return exists.</p>')

    body.append('<h2>What Each Step Is Doing</h2>')
    body.append('<p>Steps one and two exist so you do not have to find your '
                'Business Number or your incorporation date. Steps three and '
                'four are the only ones where you supply anything we cannot '
                'look up, and they are the two that decide whether the return '
                'is nil at all.</p>')
    body.append('<p>Step five is the attestation and the identity check. Step '
                'seven is where Form T183CORP is generated, and it carries '
                'that return&rsquo;s figures, which is why it cannot be signed '
                'in advance. Step eight is a secure access-controlled screen '
                'reached by a single-use link, and your signature carries a '
                'date and a timestamp.</p>')
    body.append('<p>Step nine is the CPA review, and step ten is the Canada '
                'Revenue Agency&rsquo;s confirmation, which arrives by email '
                'within 3 business days. Business days are Monday to '
                'Friday.</p>')

    body.append('<h2>What It Costs</h2>')
    body.append('<p>' + FEE + '. Each tax year is a separate return and '
                'carries the same fee, so six unfiled years is six returns. '
                'The sales tax that applies where your corporation is resident '
                'is added at checkout. See the full '
                + a(SITE + '/pricing/nil-t2-filing-cost/',
                    'nil T2 filing cost')
                + ', or the ' + a(SITE + '/pricing/what-is-not-included/',
                                  'list of what the fee does not cover')
                + '.</p>')

    body.append('<h2>If Your Corporation Turns Out Not To Be Nil</h2>')
    body.append('<div class="cnf-box"><p>This service is for a corporation '
                'with no activity in the tax year. A corporation with '
                'investment income, rental income, or dividends paid or '
                'received is not nil. Other cases that are not nil include a '
                'corporation that is not a Canadian-controlled private '
                'corporation, an amalgamation, or a corporation already '
                'dissolved or struck.</p>'
                '<p>We route you to our sister office at gondaliyacpa.ca at '
                '$350.00 plus applicable sales tax per year before you pay. If '
                'we find it after you pay, we refund you in full.</p></div>')

    body.append('<h2>Before You Start</h2>')
    body.append('<p>You need the corporation&rsquo;s legal name and to know '
                'which tax years are outstanding. If you are not sure which '
                'years those are, the '
                + a(SITE + '/tools/unfiled-years-checker/',
                    'unfiled years checker')
                + ' works through it, and the '
                + a(SITE + '/tools/nil-t2-eligibility-checker/',
                    'nil T2 eligibility checker')
                + ' tests whether the year is nil. For the whole subject in '
                'one place, see the '
                + a(SITE + '/guides/nil-t2-return-complete-guide/',
                    'complete guide to the nil T2 return')
                + ', and the '
                + a(SITE + '/faq/', 'frequently asked questions')
                + ' answer the short ones.</p>')
    return shell(
      'How Nil T2 Filing Works', FEE_TITLE, 'How it works', body, url,
      'How Nil T2 Filing Works',
      'The ten steps from typing your corporation name to your CRA '
      'confirmation, what each one does, and what the fee covers.',
      'how nil t2 filing works')


def faq():
    url = SITE + '/faq/'
    body = []
    body.append('<h2>The Questions We Are Asked Most</h2>')
    body.append('<p>Short answers, each linking to the page that carries the '
                'full one. If your question is not here, the '
                + a(SITE + '/guides/nil-t2-return-complete-guide/',
                    'complete guide to the nil T2 return')
                + ' covers the subject end to end, and '
                + a(SITE + '/contact-us/', 'contact us')
                + ' reaches a CPA.</p>')
    body.append('<div class="cnf-faq">')
    for q, paras, href, label in FAQ:
        body.append('<details open><summary><h3>' + q + '</h3></summary>'
                    '<div class="cnf-faq-a">')
        for p in paras:
            body.append('<p>' + p + '</p>')
        body.append('<p>' + a(SITE + href, 'Read ' + label) + '.</p>')
        body.append('</div></details>')
    body.append('</div>')
    body.append('<h2>How The Filing Itself Works</h2>')
    body.append('<p>The flow is ten steps on one screen, from typing your '
                'corporation name to the Canada Revenue Agency&rsquo;s '
                'confirmation within 3 business days. See '
                + a(SITE + '/how-it-works/', 'how nil T2 filing works')
                + ' for the whole sequence, or go straight to the '
                + a(SITE + '/pricing/', 'price') + '.</p>')
    body.append('<p>There are ' + str(46) + ' answer pages on this site, one '
                'question each, answered in the first 40 words. The eight '
                'above are the ones asked most often.</p>')
    return shell(
      'Nil T2 Filing: Frequently Asked Questions', FEE_TITLE,
      'Frequently asked questions', body, url,
      'Nil T2 Filing FAQ',
      'Short answers on filing a nil T2: whether an inactive corporation must '
      'file, catching up unfiled years, signing T183CORP, and what it costs.',
      'nil t2 filing faq')


PAGES = [
  dict(slug='how-it-works', title='How Nil T2 Filing Works',
       build=how_it_works,
       excerpt='The ten steps from typing your corporation name to your CRA '
               'confirmation, and what the fee covers.',
       rm_title='How Nil T2 Filing Works | ' + '$300.00 Plus Tax',
       rm_desc='The ten steps from typing your corporation name to your CRA '
               'confirmation, what each one does, and what the fee covers.',
       keyword='how nil t2 filing works'),
  dict(slug='faq', title='Nil T2 Filing: Frequently Asked Questions',
       build=faq,
       excerpt='Short answers on filing a nil T2, each linking to the page '
               'that carries the full one.',
       rm_title='Nil T2 Filing FAQ | $300.00 Plus Tax',
       rm_desc='Short answers on filing a nil T2: whether an inactive '
               'corporation must file, catching up unfiled years, signing '
               'T183CORP, and what it costs.',
       keyword='nil t2 filing faq'),
]


def meta(p):
    return {
     'site-sidebar-layout': 'no-sidebar',
     # Navneet, 2026-11-12: "they are going full width fix them". These two
     # shipped with site-content-layout page-builder, copied from the Family 4
     # meta block, which removes Astra's content container and runs the page
     # edge to edge. /about/ (page 319) and the other live trust pages leave
     # this EMPTY and keep ast-site-content-layout full-width-container, so the
     # hero still spans and the body sits in the normal container. Matched to
     # /about/ exactly. The Family 4 pages and the jurisdiction hubs are
     # page-builder by design and were not touched.
     'site-content-layout': '',
     'ast-site-content-layout': 'full-width-container',
     'site-post-title': 'disabled', 'ast-breadcrumbs-content': 'disabled',
     'ast-featured-img': 'disabled',
     'rank_math_title': p['rm_title'],
     'rank_math_description': p['rm_desc'],
     'rank_math_focus_keyword': p['keyword'],
     'cnf_last_verified_et': ISO,
    }


if __name__ == '__main__':
    for p in PAGES:
        c = p['build']()
        assert len(p['rm_title']) <= 60, (len(p['rm_title']), p['rm_title'])
        assert len(p['rm_desc']) <= 160, len(p['rm_desc'])
        import re as _re
        _style = _re.search(r'(?s)<style>(.*?)</style>', c).group(1)
        _body = _re.sub(r'(?s)<style>.*?</style>', '', c)
        _used = set()
        for _v in _re.findall(r'class="([a-z0-9 \-]+)"', _body):
            _used.update(_v.split())
        _def = set(_re.findall(r'\.([a-z][a-z0-9\-]*)', _style))
        _miss = sorted(x for x in _used if x.startswith('cnf') and x not in _def)
        assert not _miss, '%s: class used with no CSS rule: %s' % (p['slug'], _miss)
        # Hard rules, checked here rather than in a separate pass.
        assert 'HST' not in c.replace('GST/HST', ''), p['slug'] + ': names HST'
        assert not _re.search(r'\bT183\b(?!CORP)', c), p['slug'] + ': bare T183'
        assert 'FAQPage' not in c, p['slug'] + ': hard rule 6 FAQPage schema'
        assert 'HowTo' not in c and 'aggregateRating' not in c
        _low = c.lower().replace('authorized signing officer', '')
        for _w in ('authorized', 'cra approved', 'cra agent', 'cra partner',
                   'cheapest', 'best price', 'fastest', 'guaranteed',
                   'risk-free', 'book a call', 'calendly'):
            assert _w not in _low, '%s: banned "%s"' % (p['slug'], _w)
        if 'penalt' in c.lower():
            assert QUAL in c, p['slug'] + ': penalty without the 7.4 block'
        assert c.count('<h1>') == 1, p['slug'] + ': H1 count'
        io.open(os.path.join(HERE, p['slug'] + '.html'), 'w',
                encoding='utf-8').write(c)
        print('%-16s %6d bytes   rm_title %d   rm_desc %d'
              % (p['slug'], len(c.encode()), len(p['rm_title']),
                 len(p['rm_desc'])))
