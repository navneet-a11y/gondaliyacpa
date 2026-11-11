#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 8, cost and pricing. Appendix A's roster, and what is buildable.

Appendix A gives Family 8 as 15 URLs: thirteen jurisdiction cost pages,
/pricing/ and /price-transparency-promise/. Line 1145's samples
(/pricing/nil-t2-filing-cost/, /pricing/cost-to-file-six-unfiled-nil-years/,
/pricing/what-is-not-included/) are illustrations, not the roster, exactly as
line 1145's /compare/corpnilfilingfor300-vs-turbotax-business/ was an
illustration of Appendix A's -vs-turbotax.

The URL base comes from the family table and the nil_cost rewrite, not from
Appendix A, which lists the slugs bare. That is the same resolution Family 2
got: Appendix A lists the tool slugs without /tools/ and every one of the 100
live tools sits under it. So a cost page is /pricing/<slug>/.

EIGHT OF THE THIRTEEN JURISDICTION PAGES ARE NOT BUILT HERE
-----------------------------------------------------------
The decisions log of 2026-10-30 set this out and left it open: hard rule 9
mandates "$300.00 plus HST per tax year" on every page, and HST does not
exist in eight of the thirteen jurisdictions. A client in Alberta pays 5 per
cent GST; a client in Quebec pays GST plus QST. On a page whose whole subject
is what a nil return costs in that jurisdiction, a headline naming the wrong
tax is not a style problem.

Page 996 (British Columbia) handled it by keeping the string for consistency
and dropping the computation. That works on a service page, where the price is
a detail. It does not work on a cost page, where the price is the subject.

So this builder makes the five jurisdictions where HST is the correct tax:

    Ontario, New Brunswick, Nova Scotia,
    Newfoundland and Labrador, Prince Edward Island

and leaves the other eight to the ruling the log already asked for. A wording
that works everywhere -- "$300.00 plus applicable sales tax per tax year" --
needs hard rule 9 amended, which is Sharad Gondaliya's decision.

NO TAX RATE IS STATED ON ANY PAGE HERE
--------------------------------------
Not even on the five. The live cost page computes Ontario's 13 per cent to
$339.00, and that figure is right, but the same log entry records "New
Brunswick, Nova Scotia, Newfoundland and Labrador and Prince Edward Island at
15 per cent" and Nova Scotia's rate is not 15 per cent any more. Rather than
propagate a rate from the project's own record onto a CPA firm's pricing
pages, every page here says the tax is added at the rate for the province and
names no number. The fee is the number these pages are about.

WHAT ACTUALLY DIFFERS BETWEEN THESE FIVE PAGES
----------------------------------------------
Not the fee, which is one price everywhere. What differs is what else the
jurisdiction wants, and that is sourced: the provincial return requirement
checker already publishes that most provinces levy corporate income tax
through the federal return and that Quebec and Alberta do not. For these five
that means one T2 settles the corporate tax, and the separate thing is the
provincial registry's own annual return, which the fee does not cover.

Schema is WebPage plus BreadcrumbList, not the Service-with-Offer graph the
live cost page carries. An Offer node states a price, and a priced Offer on a
per-jurisdiction page is the same accuracy problem in another form.
"""
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
PRICING = SITE + '/pricing/'
COST = SITE + '/pricing/nil-t2-filing-cost/'
T = SITE + '/tools/'
C = SITE + '/compare/'
PRICE = '$300.00 plus HST per tax year'
TODAY, ISO = 'November 11, 2026', '2026-11-11'
BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')
STYLE = io.open(os.path.join(HERE, '_f8_style.txt'), encoding='utf-8').read()

# The five jurisdictions where HST is the tax actually charged, so hard rule
# 9's string is correct rather than merely mandated. Each carries the name of
# its own corporate registry, which is the thing the fee does not cover.
HST_PLACES = [
 dict(slug='ontario', name='Ontario', the='Ontario',
      registry='the Ontario Business Registry',
      registry_short='the Ontario annual return',
      extra=('Schedule 546 and the 2021 Cutover',
             '<p>Ontario has a wrinkle the other provinces do not. The '
             'Ontario annual return used to travel with the T2 on Schedule '
             '546, and since the Ontario Business Registry opened in 2021 it '
             'does not. A corporation that still files Schedule 546 with its '
             'return, or that assumes the T2 carried the annual return the '
             'way it once did, has an outstanding registry filing it does '
             'not know about.</p>\n'
             '<p>The <a href="' + T + 'schedule-546-ontario-annual-return-'
             'checker/">Schedule 546 checker</a> settles which side of the '
             'cutover a given year falls on, the <a href="' + T + 'ontario-'
             'business-registry-filing-checker/">Ontario Business Registry '
             'filing checker</a> covers what the registry wants now, and the '
             '<a href="' + T + 'ontario-missed-annual-returns-calculator/">'
             'missed annual returns calculator</a> counts the years that '
             'went unfiled since. None of those filings is covered by this '
             'fee, and all of them are separate from the T2.</p>')),
 dict(slug='new-brunswick', name='New Brunswick', the='New Brunswick',
      registry='the New Brunswick corporate registry',
      registry_short='the New Brunswick annual return'),
 dict(slug='nova-scotia', name='Nova Scotia', the='Nova Scotia',
      registry='the Nova Scotia Registry of Joint Stock Companies',
      registry_short='the Nova Scotia annual return'),
 dict(slug='newfoundland-and-labrador', name='Newfoundland and Labrador',
      the='Newfoundland and Labrador',
      registry='the Newfoundland and Labrador registry of companies',
      registry_short='the Newfoundland and Labrador annual return'),
 dict(slug='prince-edward-island', name='Prince Edward Island',
      the='Prince Edward Island',
      registry='the Prince Edward Island corporate registry',
      registry_short='the Prince Edward Island annual return'),
]


def crumb(title):
    return ('<nav class="cnf-crumb" aria-label="Breadcrumb">'
            '<a href="' + SITE + '/">Nil T2 filing in Canada</a> &rsaquo; '
            '<a href="' + PRICING + '">Nil T2 filing price</a> &rsaquo; '
            '<span aria-current="page">' + title + '</span></nav>')


def hero(h1, sub, lede):
    return ('<div class="cnf-hero"><div class="cnf-hero-in" '
            'style="max-width:1140px;margin:0 auto;text-align:left">'
            '<h1>' + h1 + '</h1>'
            '<p class="cnf-hero-sub">' + sub + '</p>'
            '<p class="cnf-hero-lede">' + lede + '</p>'
            '<p><a class="cnf-hero-btn" href="' + FORM + '">'
            'Start Nil T2 Filing NOW</a></p></div></div>')


def schema(url, name, desc):
    g = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': url + '#webpage', 'url': url,
         'name': name, 'description': desc, 'inLanguage': 'en-CA',
         'dateModified': ISO,
         'author': {'@type': 'Person', 'name': 'Sharad Gondaliya',
                    'honorificSuffix': 'CPA',
                    'url': SITE + '/sharad-gondaliya-cpa/'}},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1,
             'name': 'Nil T2 filing in Canada', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2,
             'name': 'Nil T2 filing price', 'item': PRICING},
            {'@type': 'ListItem', 'position': 3, 'name': name, 'item': url}]}]}
    return ('<script type="application/ld+json">'
            + json.dumps(g, separators=(',', ':')) + '</script>')


FOOT = ('<p class="cnf-foot">Your return is prepared and transmitted in '
        'Canada. Our credentials are never shared and no part of your file '
        'is sent offshore. <a href="' + PRICING + '">Nil T2 filing price</a>'
        '</p>')


def cost_page(p):
    """One jurisdiction cost page. No tax rate, no total, one fee."""
    name, the = p['name'], p['the']
    slug = 'nil-t2-return-cost-' + p['slug']
    url = PRICING + slug + '/'
    title = 'Nil T2 Return Cost in ' + name
    h1 = 'Nil T2 Return Cost in ' + name
    art = 'an' if name[0] in 'AEIOU' else 'a'
    desc = ('A nil T2 return for ' + art + ' ' + name + ' corporation is '
            + PRICE + '. One price for every tax year, and the annual return '
            'is separate.')
    body = []
    body.append(STYLE)
    body.append(hero(h1, '$300.00 Plus HST Per Tax Year',
                     'We are a registered EFILE electronic filer. Your '
                     'return is transmitted to the Canada Revenue Agency '
                     'electronically.'))
    body.append('<div class="cnf-w" style="max-width:1000px!important;'
                'margin:0 auto!important;padding:36px 20px 56px!important;'
                'box-sizing:border-box">')
    body.append(crumb(title))
    body.append('<p class="cnf-by">' + BYLINE + '</p>')
    body.append('<p class="cnf-rev">Last reviewed: ' + TODAY + '</p>')
    body.append('<div class="cnf-fee"><p><strong>' + PRICE + '.</strong> '
                'One price for every tax year, in ' + the + ' and in every '
                'other province. No hourly billing and no add-on fees.</p>'
                '<p>Overflow work moves to gondaliyacpa.ca at $350.00 plus '
                'HST per year.</p></div>')

    body.append('<h2>What a Nil T2 Return Costs in ' + name + '</h2>')
    body.append('<p>A nil T2 return for ' + art + ' ' + name
                + ' corporation is '
                + PRICE + '. Tax is added at the rate for your province. '
                'Each tax year is its own return and carries the same fee, '
                'so six unfiled years are six returns.</p>')
    body.append('<p>The fee does not change by province. What changes '
                'between provinces is what else the corporation owes, and '
                'that is the useful part of this page.</p>')

    body.append('<h2>One Return Settles the Corporate Tax Here</h2>')
    body.append('<p>' + name + ' levies its corporate income tax through '
                'the federal return, so the T2 settles both the federal and '
                'the provincial corporate tax for the year. There is no '
                'separate provincial corporate return to file.</p>')
    body.append('<p>Two provinces are different. Quebec collects through '
                'CO-17 and Alberta through AT1, and each of those is a '
                'separate return rather than a schedule of the T2. The '
                '<a href="' + T + 'provincial-return-requirement-checker/">'
                'provincial return requirement checker</a> settles which, '
                'if either, applies to a given corporation.</p>')

    body.append('<h2>What ' + name + ' Wants That the Fee Does Not Cover'
                '</h2>')
    _reg = p['registry'][0].upper() + p['registry'][1:]
    body.append('<p>' + _reg
                + ' wants its own annual return. That is a registry filing '
                'confirming the directors and the registered office, it '
                'reports no income, and filing the T2 does not satisfy it. '
                'It is not covered by this fee.</p>')
    body.append('<p>A federally incorporated corporation owes a Corporations '
                'Canada annual return instead, at $12.00, due within 60 days '
                'of the anniversary. The $12.00 is a government fee and HST '
                'does not apply to it. The '
                '<a href="' + T + 'annual-return-vs-tax-return-checker/">'
                'annual return versus tax return checker</a> separates the '
                'two trails, and <a href="' + C + 'nil-t2-vs-ontario-annual-'
                'return-vs-federal-annual-return/">the three filings '
                'compared</a> sets all three side by side.</p>')

    if p.get('extra'):
        body.append('<h2>' + p['extra'][0] + '</h2>')
        body.append(p['extra'][1])
    body.append('<h2>Several Unfiled Years</h2>')
    body.append('<p>Each year is prepared, reviewed and transmitted '
                'separately, so the fee multiplies by the number of years. '
                'They are filed oldest first, because each year&rsquo;s '
                'closing position carries into the next return. The '
                '<a href="' + T + 'unfiled-years-cost-calculator/">unfiled '
                'years cost calculator</a> turns a year count into a total, '
                'and the <a href="' + T + 'outstanding-returns-count-checker/'
                '">outstanding returns count checker</a> works out how many '
                'years are open from the last return filed.</p>')

    body.append('<h2>What the Fee Includes</h2>')
    body.append('<div class="cnf-box"><p>The T2 itself and the GIFI '
                'schedules where the corporation has anything to report, '
                'Schedule 50 for any shareholder at 10% or more, Schedule 24 '
                'on a first return, and Schedule 8 with loss continuity. '
                'Preparation and review by a CPA Ontario member. Form '
                'T183CORP signed on a secure screen, transmission by a '
                'registered EFILE electronic filer, and the CRA confirmation '
                'emailed within 3 business days.</p></div>')
    body.append('<p>The <a href="' + COST + '">nil T2 filing cost page</a> '
                'sets the whole of it out, and the '
                '<a href="' + T + 'what-the-nil-t2-fee-covers-checker/">'
                'fee-covers checker</a> answers it question by question.</p>')

    body.append('<h2>A Year That Is Not Nil</h2>')
    body.append('<p>This fee is for a tax year with no activity. A holding '
                'corporation with investment income, a rental corporation '
                'and a corporation that paid or received a dividend are not '
                'nil. Those are handled by Gondaliya CPA Professional '
                'Corporation at gondaliyacpa.ca at $350.00 plus HST per '
                'year, and we say so before anything further is '
                'charged.</p>')
    body.append('<p><a class="cnf-btn" href="' + FORM + '">'
                'Start Nil T2 Filing NOW</a>'
                '<a class="cnf-btn" href="' + COST + '">What the fee covers'
                '</a></p>')
    body.append(FOOT)
    body.append('</div>')
    body.append(schema(url, title, desc))
    return slug, title, desc, '\n'.join(body)


def promise_page():
    """/price-transparency-promise/. No jurisdiction, so nothing here is
    touched by the hard rule 9 problem. It is the one Family 8 URL outside
    the thirteen that could be built today without a ruling."""
    slug = 'price-transparency-promise'
    url = PRICING + slug + '/'
    title = 'Price Transparency Promise'
    desc = ('One price, stated in full before you pay. Nil T2 filing is '
            + PRICE + ', with everything outside the fee named rather than '
            'discovered later.')
    body = []
    body.append(STYLE)
    body.append(hero('Price Transparency Promise',
                     '$300.00 Plus HST Per Tax Year',
                     'The whole amount is on the screen before you pay. '
                     'Nothing is charged until you confirm.'))
    body.append('<div class="cnf-w" style="max-width:1000px!important;'
                'margin:0 auto!important;padding:36px 20px 56px!important;'
                'box-sizing:border-box">')
    body.append(crumb(title))
    body.append('<p class="cnf-by">' + BYLINE + '</p>')
    body.append('<p class="cnf-rev">Last reviewed: ' + TODAY + '</p>')
    body.append('<div class="cnf-fee"><p><strong>' + PRICE + '.</strong> '
                'One price for every tax year and every province. No hourly '
                'billing and no add-on fees.</p><p>Overflow work moves to '
                'gondaliyacpa.ca at $350.00 plus HST per year.</p></div>')

    body.append('<h2>What This Page Promises</h2>')
    body.append('<p>Four things, and they are the whole of it. The price is '
                'published rather than quoted. The amount you pay is shown '
                'in full before you pay it. What sits outside the fee is '
                'named on the way in rather than discovered on the way out. '
                'And a year that turns out not to be nil is told to you '
                'before any further charge.</p>')

    body.append('<h2>One Price, Published</h2>')
    body.append('<p>Nil T2 filing is ' + PRICE + '. It does not change by '
                'province, by how late the year is, or by how many years '
                'you are filing. Each tax year is its own return at the same '
                'fee, so six unfiled years are six returns.</p>')
    body.append('<p>There is no tier above it and no tier below it. There is '
                'no hourly billing, no filing surcharge and no add-on fee. '
                'The <a href="' + COST + '">nil T2 filing cost page</a> '
                'states the fee and everything inside it.</p>')

    body.append('<h2>The Whole Amount, Before You Pay</h2>')
    body.append('<p>Tax is added at the rate for your province, and the '
                'total with tax is on the screen before you confirm. Nothing '
                'is charged until you do. You pay when you file, on the same '
                'screen, with no call, meeting or email chain in '
                'between.</p>')

    body.append('<h2>What Sits Outside the Fee, Named</h2>')
    body.append('<p>A nil T2 is a tax return, and several things that look '
                'like part of it are separate filings to separate bodies:</p>')
    body.append('<table class="cnf-tbl"><thead><tr>'
                '<th scope="col">Filing</th><th scope="col">Who wants it</th>'
                '<th scope="col">In the fee</th></tr></thead><tbody>'
                '<tr><td>The nil T2 corporate return</td>'
                '<td>The Canada Revenue Agency</td><td>Yes</td></tr>'
                '<tr><td>A provincial registry annual return</td>'
                '<td>The province of incorporation</td><td>No</td></tr>'
                '<tr><td>A Corporations Canada annual return, $12.00</td>'
                '<td>Corporations Canada</td><td>No</td></tr>'
                '<tr><td>Quebec CO-17</td><td>Revenu Quebec</td>'
                '<td>No</td></tr>'
                '<tr><td>Alberta AT1</td><td>Alberta</td><td>No</td></tr>'
                '<tr><td>Nil GST/HST and payroll filings</td>'
                '<td>The Canada Revenue Agency, on their own accounts</td>'
                '<td>No</td></tr>'
                '</tbody></table>')
    body.append('<p>Two rows on that table are corporate tax and still sit '
                'outside the fee. Quebec collects its corporate income tax '
                'through CO-17 and Alberta through AT1, and each is a '
                'separate return in its own right rather than a schedule of '
                'the T2. Everywhere else one T2 settles both.</p>')
    body.append('<p>We tell you which of these you still owe. The '
                '<a href="' + T + 'what-the-nil-t2-fee-covers-checker/">'
                'fee-covers checker</a> answers it question by question, and '
                'the $12.00 Corporations Canada fee is a government fee that '
                'HST does not apply to.</p>')

    body.append('<h2>If the Year Is Not Nil</h2>')
    body.append('<p>This service is for a tax year with no activity. A '
                'holding corporation with investment income, a rental '
                'corporation and a corporation that paid or received a '
                'dividend are not nil.</p>')
    body.append('<p>Where that is the case we say so before anything further '
                'is charged, and the file moves to Gondaliya CPA '
                'Professional Corporation at gondaliyacpa.ca at $350.00 plus '
                'HST per year. No charge is taken at the higher price '
                'without you agreeing to it first. If we find it after you '
                'have paid, you are refunded in full.</p>')

    body.append('<h2>What We Do Not Do</h2>')
    body.append('<p>We do not quote a price and change it. We do not publish '
                'a price that applies only to some corporations and settle '
                'the rest by email. We do not compare our fee with anyone '
                'else&rsquo;s and tell you which is better value: the '
                '<a href="' + C + 'corpnilfilingfor300-vs-cloudtax/">'
                'published-price pages</a> state both figures on the date '
                'each was recorded and leave the conclusion to you.</p>')
    body.append('<p><a class="cnf-btn" href="' + FORM + '">'
                'Start Nil T2 Filing NOW</a>'
                '<a class="cnf-btn" href="' + COST + '">What the fee covers'
                '</a></p>')
    body.append(FOOT)
    body.append('</div>')
    body.append(schema(url, title, desc))
    return slug, title, desc, '\n'.join(body)


# ---------------------------------------------------------------- the gate
BANNED_CRA = ('cra authorized', 'authorized by cra', 'cra agent',
              'cra approved', 'cra partner', 'cra endorsed', 'cra logo')
BANNED_CLAIM = ('cheapest', 'lowest price', 'best price', 'unbeatable',
                'better than', 'worse than', 'guaranteed', 'risk-free',
                'risk free', 'fastest', 'instant filing', 'five-star',
                'reviews')
# Hard rule 9 allows exactly these figures on a Family 8 page. A tax RATE or
# a tax-inclusive TOTAL is deliberately not in here: see the module docstring.
MONEY_OK = {'300.00', '350.00', '12.00'}


def gate(slug, html):
    low = html.lower()
    bad = []
    for w in BANNED_CRA:
        if w in low:
            bad.append('rule 1 CRA wording %r' % w)
    if re.search(r'\bauthorized\b', low.replace('authorized signing officer', '')):
        bad.append('rule 1 stray "authorized"')
    for m in re.finditer(r'EFILE', html):
        if not html.startswith('EFILE electronic filer', m.start()):
            bad.append('rule 1 EFILE outside the approved phrase')
            break
    if re.search(r'\bT183\b(?!CORP)', html):
        bad.append('rule 2 bare T183')
    for m in re.finditer(r'(no penalty|penalty[- ]free|zero penalty)', low):
        bad.append('rule 3 unqualified penalty phrase %r' % m.group(1))
    for w in BANNED_CLAIM:
        if w in low:
            bad.append('rule 4 or 6 banned claim %r' % w)
    for w in ('faqpage', 'howto', 'aggregaterating', 'trustindex'):
        if w in low:
            bad.append('rule 6 forbidden schema %r' % w)
    for w in ('book a call', 'calendly', 'free consultation', 'consultation/'):
        if w in low:
            bad.append('rule 7 booking call to action %r' % w)
    if 'including HST' in html:
        bad.append('rule 9 "including HST" contradicts the standing correction')
    if PRICE not in html:
        bad.append('rule 9 price string missing')
    for m in re.finditer(r'\$(\d{1,3}(?:,\d{3})*\.\d\d)', html):
        if m.group(1) not in MONEY_OK:
            bad.append('unexpected money figure $%s' % m.group(1))
    # The whole point of this batch: no tax rate, no tax-inclusive total.
    if re.search(r'\d+(\.\d+)?\s*per cent (HST|GST|QST)', html, re.I):
        bad.append('a tax RATE is stated; see the module docstring')
    if re.search(r'\b(13|14|15|5)\s*%', html):
        bad.append('a tax rate in % form is stated')
    # Hard rule 8, wherever a page names the two separate-return provinces.
    for tok in ('CO-17', 'AT1'):
        if tok in html and 'separate return' not in html:
            bad.append('rule 8: %s named without "separate return"' % tok)
    if re.search(r'\ba (?=[AEIOU])', html):
        bad.append('article "a" before a vowel-initial province name')
    if bad:
        raise AssertionError('%s GATE FAILED:\n  - %s'
                             % (slug, '\n  - '.join(bad)))


if __name__ == '__main__':
    recs = []
    pages = [cost_page(p) for p in HST_PLACES] + [promise_page()]
    for slug, title, desc, html in pages:
        gate(slug, html)
        assert 70 <= len(desc) <= 160, '%s: meta %d chars' % (slug, len(desc))
        io.open(os.path.join(HERE, slug + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=slug, title=title, desc=desc,
                         url=PRICING + slug + '/', bytes=len(html.encode())))
        print('%-34s %6d bytes   %s'
              % (slug, len(html.encode()), PRICING + slug + '/'))
    json.dump(recs, io.open(os.path.join(HERE, 'f8-cost-manifest.json'), 'w',
                            encoding='utf-8'), indent=1)
    print('\n%d pages, gate clear on all' % len(recs))
