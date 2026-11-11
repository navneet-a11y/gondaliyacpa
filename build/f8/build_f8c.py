#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 8, the eight remaining Appendix A jurisdiction cost pages.

Appendix A's Family 8 roster, at plan line 3304, is exactly 15 URLs: thirteen
jurisdiction cost pages, /pricing/ and /price-transparency-promise/. Seven are
live. These are the other eight:

    Quebec, British Columbia, Alberta, Manitoba, Saskatchewan,
    Yukon, Northwest Territories, Nunavut

and they are, without exception, the eight jurisdictions where HST does not
exist. That is not a coincidence of ordering: the five already built are the
five genuine HST jurisdictions, so every page left in this family is one the
hard rule 9 wording cannot describe correctly.

WHY THESE PAGES CANNOT CARRY THE STANDING PRICE STRING
------------------------------------------------------
Hard rule 9 reads "$300 including HST per tax year"; the standing correction
in decisions.md makes it "$300.00 plus HST per tax year", and the Family 5 and
Family 8 gates both enforce that exact string.

Checked against the Canada Revenue Agency rather than from memory:

    Alberta, Yukon, Northwest Territories, Nunavut   5 per cent GST, no PST
    British Columbia, Manitoba, Saskatchewan         GST plus a provincial PST
    Quebec                                           GST plus QST

So "plus HST" names a tax that is not charged in any of the eight. On a page
whose entire subject is what a nil return costs in that jurisdiction, that is
not a wording preference.

The same check turned up why naming the tax per jurisdiction is also wrong
here: Nova Scotia's HST moved to 14 per cent on April 1, 2025, which is the
figure the project's own 2026-10-30 log still records as 15. A project record
that is stale on a rate is not a source to build eight pricing pages on. And
whether a provincial PST reaches a professional accounting fee is a different
question from whether the province has a PST at all -- it varies, and this
session cannot verify it. Naming "GST and PST" on the British Columbia page
would be the same class of error as naming HST.

What is left is the formulation this builder uses:

    $300.00 plus applicable sales tax per tax year

It is accurate in all thirteen jurisdictions, it names no tax that might not
apply, and it states no rate. It is also a deviation from hard rule 9 and
from the standing correction, which is Sharad Gondaliya's call and nobody
else's, so EVERY PAGE HERE IS BUILT AS A DRAFT AND NONE IS PUBLISHED.

Flipping them to publish is one status change per page once that line is
ruled on. Nothing else about them depends on it.

A NOTE ON THE COUNT
-------------------
Seven of the fifteen roster URLs are live, plus three line 1146 sample slugs
that are not on the roster (/pricing/nil-t2-filing-cost/,
cost-to-file-six-unfiled-nil-years, what-is-not-included). Family 8 therefore
reads 10 live. Publishing these eight would take it to 18 against a planned
15. That is the same off-roster drift Family 2 has with 35 slugs and Family 5
has with 45, and it is logged rather than fixed here.

DUPLICATION, WHICH IS THE REAL RISK
-----------------------------------
The four province pages published earlier today measure 0.94 to 0.96 against
each other. The cause was that New Brunswick, Nova Scotia, Newfoundland and
Labrador and Prince Edward Island differ in nothing this site can state.

Of these eight, only two differ structurally: Quebec files a CO-17 and
Alberta files an AT1, each a separate provincial return. The other six all
have one T2 settling federal and provincial or territorial corporate income
tax. Yukon, the Northwest Territories and Nunavut are identical on every axis
this site can speak to: GST only, no territorial sales tax, one T2.

So each page is given a different angle and a different second half rather
than the same page with a placename substituted, and then all eight are
measured against each other and against the seven live pages. The numbers go
in the report. Where a page is thin, it is reported as thin rather than
published and logged as a decision.
"""
import io
import json
import os
import re

import build_f8_cost as F8

HERE = os.path.dirname(os.path.abspath(__file__))
SITE, PRICING, COST, FORM = F8.SITE, F8.PRICING, F8.COST, F8.FORM
T, C = F8.T, F8.C
A = SITE + '/answers/'
G = SITE + '/guides/'
PROMISE = PRICING + 'price-transparency-promise/'
NOTINC = PRICING + 'what-is-not-included/'
SIX = PRICING + 'cost-to-file-six-unfiled-nil-years/'

# The deviation. See the module docstring.
PRICE = '$300.00 plus applicable sales tax per tax year'
OVERFLOW = ('Overflow work moves to gondaliyacpa.ca at $350.00 plus '
            'applicable sales tax per year.')

PLACES = [
 dict(slug='quebec', name='Quebec', art='a',
      sales='the GST and the QST',
      route='separate', sep='CO-17', body_with='Revenu Quebec',
      angle='Two Returns, Not One',
      lead=["A Quebec corporation with a dormant year has two corporate "
            "income tax returns to file, not one. Quebec collects its "
            "corporate income tax on the CO-17, filed with Revenu Quebec, "
            "and that is a separate return in its own right rather than a "
            "schedule of the federal T2.",
            "The fee on this page covers the federal T2. It does not cover "
            "the CO-17. That is the single most important thing to know "
            "about what a nil return costs in Quebec, and it is why this "
            "page exists separately from the others."],
      extra=[("What the CO-17 Means for a Dormant Year",
              ["A year with no activity still needs the CO-17 filed. Quebec "
               "does not waive the return because the figures are nil, any "
               "more than the Canada Revenue Agency waives the T2.",
               "So a Quebec corporation catching up on six dormant years is "
               "looking at six federal returns and six provincial ones. The "
               "federal side is what this fee covers, at the same price per "
               "year as everywhere else in Canada."])]),
 dict(slug='alberta', name='Alberta', art='an',
      sales='the GST',
      route='separate', sep='AT1', body_with='Alberta',
      angle='No Provincial Sales Tax, and Still a Second Return',
      lead=["Alberta is the only province with no provincial sales tax, so "
            "the tax added to this fee is the GST alone. That is the simple "
            "part.",
            "The part that catches people out is that Alberta collects its "
            "corporate income tax on the AT1, which is a separate return "
            "rather than a schedule of the federal T2. Having no provincial "
            "sales tax does not mean having no provincial return."],
      extra=[("Why the Two Are Easy to Confuse",
              ["Most of Canada runs provincial corporate income tax through "
               "the federal return, so one T2 settles both and there is "
               "nothing else to file. Alberta and Quebec are the two "
               "exceptions, and Alberta is the one people are most often "
               "surprised by.",
               "The fee here covers the federal T2 for one tax year. The AT1 "
               "is not in it."])]),
 dict(slug='british-columbia', name='British Columbia', art='a',
      sales='the GST and the provincial sales tax where it applies',
      route='t2', sep=None, body_with=None,
      angle='One T2 Settles the Corporate Tax',
      lead=["British Columbia levies its corporate income tax through the "
            "federal return, so one T2 settles both the federal and the "
            "provincial side. There is no separate British Columbia "
            "corporate return to file, which is the opposite of the position "
            "in Alberta and Quebec.",
            "That makes the separate filing in British Columbia a registry "
            "matter rather than a tax one. The corporation still has to tell "
            "its registry it exists, every year, and that filing is not a "
            "tax return and is not in this fee."],
      extra=[("What a Dormant Year Still Owes",
              ["One federal T2, which this fee covers. One registry annual "
               "filing, which it does not. And any GST/HST or payroll "
               "account the corporation holds keeps its own filing cycle "
               "whether the year was dormant or not.",
               "None of that changes the fee. It is the same price per tax "
               "year in British Columbia as in every other province and "
               "territory."])]),
 dict(slug='manitoba', name='Manitoba', art='a',
      sales='the GST and the provincial sales tax where it applies',
      route='t2', sep=None, body_with=None,
      angle='What the Fee Is Not',
      lead=["The quickest way to understand what a nil return costs in "
            "Manitoba is to be clear about what the fee is not paying for. "
            "It is one federal T2 corporation income tax return, for one tax "
            "year, prepared and transmitted.",
            "Manitoba collects its corporate income tax through that same "
            "federal return, so there is no separate Manitoba corporate "
            "return. What sits outside the fee is the registry filing, not a "
            "second tax return."],
      extra=[("The Annual Return Is the One People Miss",
              ["A registry annual filing reports that the corporation still "
               "exists and who its directors are. It reports no money, which "
               "is exactly why it is so often assumed to travel with the tax "
               "return. It does not.",
               "A corporation that has not filed a T2 for several years has "
               "usually not filed those either, and the two are caught up "
               "separately."])]),
 dict(slug='saskatchewan', name='Saskatchewan', art='a',
      sales='the GST and the provincial sales tax where it applies',
      route='t2', sep=None, body_with=None,
      angle='Several Outstanding Years, and the Order They Go In',
      lead=["Saskatchewan collects its corporate income tax through the "
            "federal return, so one T2 per tax year settles both sides and "
            "the fee is the same per year as anywhere else in Canada.",
            "Where a Saskatchewan corporation has several dormant years "
            "outstanding, the cost is simple multiplication and the sequence "
            "is not. Each year is its own return, and they are filed oldest "
            "first."],
      extra=[("Why Oldest First",
              ["A corporation carries figures from one year into the next. "
               "Even a dormant one carries its share capital and its balance "
               "sheet forward, so a later year transmitted before an earlier "
               "one can be assessed against figures that have not been filed "
               "yet.",
               "Six dormant years is six returns at the same fee each. The "
               "arithmetic is on the six unfiled years page; the per-year "
               "price does not change because there are several."])]),
 dict(slug='yukon', name='Yukon', art='a', terr=True,
      sales='the GST',
      route='t2', sep=None, body_with=None,
      angle='A Territory With No Sales Tax of Its Own',
      lead=["Yukon levies no territorial sales tax, so the only tax added to "
            "this fee is the GST. Yukon also collects its corporate income "
            "tax through the federal return, so one T2 per tax year settles "
            "the federal and the territorial side together.",
            "That makes a dormant Yukon corporation one of the simpler "
            "filing positions in Canada: one return, one fee, and no second "
            "corporate return to find."],
      extra=[("The Territorial Rate Does Not Come Into It",
              ["Yukon sets its own corporate income tax rates, and on a nil "
               "return they make no difference at all. A rate applies to "
               "income, and a true nil year has none, so the tax payable is "
               "$0.00 whatever the rate happens to be.",
               "What the year does need is the return itself. An unfiled "
               "dormant year stays open, and the territorial registry still "
               "expects its own annual filing, which this fee does not "
               "cover."])]),
 dict(slug='northwest-territories', name='Northwest Territories',
      art='a', the='the ', terr=True,
      sales='the GST',
      route='t2', sep=None, body_with=None,
      angle='Filing From Anywhere',
      lead=["The Northwest Territories levies no territorial sales tax, so "
            "the GST is the only tax added to this fee, and territorial "
            "corporate income tax runs through the federal return, so one T2 "
            "per tax year settles both.",
            "Everything about the filing happens electronically, which "
            "matters more here than in most places. There is no office to "
            "attend and no document to post."],
      extra=[("What Electronic Filing Covers",
              ["The return is transmitted to the Canada Revenue Agency "
               "electronically. Form T183CORP is signed on a secure "
               "single-use screen rather than printed, and the Canada "
               "Revenue Agency accepts an electronic signature on it.",
               "A registered office in the Northwest Territories changes "
               "none of the fee and none of the process. The territorial "
               "registry still wants its own annual filing, separately."])]),
 dict(slug='nunavut', name='Nunavut', art='a', terr=True,
      sales='the GST',
      route='t2', sep=None, body_with=None,
      angle='Nil Means Nil, Wherever the Office Is',
      lead=["Nunavut levies no territorial sales tax, so the GST is the only "
            "tax added to this fee. Nunavut collects its corporate income "
            "tax through the federal return, so one T2 per tax year settles "
            "the federal and the territorial side.",
            "The test for whether a year is nil is the same in Nunavut as "
            "everywhere else, and it is a test about the corporation's "
            "activity rather than about where it is registered."],
      extra=[("The Test That Decides the Price",
              ["A tax year with no activity is filed here at the published "
               "fee. A corporation with investment income, with rental "
               "income, or that paid or received a dividend is not nil in "
               "that year, and no registered office changes that.",
               "Nil is decided year by year. A corporation can have five "
               "dormant years and one year that is not, and only the year "
               "that is not moves to the higher price."])]),
]


def page(p):
    name, slug = p['name'], p['slug']
    the = p.get('the', '')
    url = PRICING + 'nil-t2-return-cost-' + slug + '/'
    title = 'Nil T2 Return Cost in ' + name
    desc = ('Nil T2 return cost in ' + name + ': ' + PRICE
            + '. What the fee covers and what it does not.')
    assert 70 <= len(desc) <= 160, '%s meta %d chars' % (slug, len(desc))
    b = [F8.STYLE]
    b.append(F8.hero(
        title, '$300.00 Plus Applicable Sales Tax Per Tax Year',
        p['lead'][0]))
    b.append('<div class="cnf-w" style="max-width:1000px!important;'
             'margin:0 auto!important;padding:36px 20px 56px!important;'
             'box-sizing:border-box">')
    b.append(F8.crumb(title))
    b.append('<p class="cnf-by">' + F8.BYLINE + '</p>')
    b.append('<p class="cnf-rev">Last reviewed: ' + F8.TODAY + '</p>')
    b.append('<div class="cnf-fee"><p><strong>' + PRICE + '.</strong> '
             'The fee does not change by province or territory. In ' + the
             + name + ' the tax added to it is ' + p['sales']
             + '.</p><p>' + OVERFLOW + '</p></div>')

    b.append('<h2>' + p['angle'] + '</h2>')
    for para in p['lead'][1:]:
        b.append('<p>' + para + '</p>')

    b.append('<h2>What a Nil T2 Costs in ' + name + '</h2>')
    rows = [('Our fee, one tax year', '$300.00'),
            ('Tax added', p['sales'][0].upper() + p['sales'][1:]),
            ('Returns for one dormant year',
             'Two: the federal T2 and ' + the.capitalize() + name
             + "'s " + str(p['sep']) if p['route'] == 'separate'
             else 'One: the federal T2'),
            ('Provincial or territorial corporate tax',
             'On a separate ' + str(p['sep']) + ' return'
             if p['route'] == 'separate' else 'Settled by the federal T2'),
            ('Registry annual filing', 'Not in the fee'),
            ('Overflow price, a year that is not nil',
             '$350.00 plus applicable sales tax per year')]
    b.append('<table class="cnf-tbl"><thead><tr>'
             '<th scope="col">Item</th><th scope="col">Position in ' + name
             + '</th></tr></thead><tbody>'
             + ''.join('<tr><td>' + k + '</td><td>' + v + '</td></tr>'
                       for k, v in rows)
             + '</tbody></table>')
    b.append('<p>No rate is quoted on this page. Sales tax rates change, and '
             'the figure that matters to a reader deciding whether to file is '
             'the fee. The whole amount with tax is on the screen before you '
             'pay, and nothing is charged until you confirm.</p>')

    for head, paras in p['extra']:
        b.append('<h2>' + head + '</h2>')
        for para in paras:
            b.append('<p>' + para + '</p>')

    b.append('<h2>Where the Rest of the Answer Is</h2>')
    b.append('<p>The fee is the same in every province and territory, so '
             'these pages cover what else the jurisdiction wants rather than '
             'a different price. The '
             '<a href="' + COST + '">nil T2 filing cost page</a> sets out '
             'the fee and everything inside it, '
             '<a href="' + NOTINC + '">what is not included</a> groups every '
             'filing that sits outside it, and '
             '<a href="' + SIX + '">six unfiled nil years</a> works through '
             'the catch-up case.</p>')
    b.append('<p>The <a href="' + PROMISE + '">price transparency promise</a> '
             'is the commitment behind all of them, and the '
             '<a href="' + T + 'provincial-return-requirement-checker/">'
             'provincial return requirement checker</a> answers whether your '
             'jurisdiction wants a separate corporate return.</p>')
    b.append('<p><a class="cnf-btn" href="' + FORM + '">'
             'Start Nil T2 Filing NOW</a>'
             '<a class="cnf-btn" href="' + COST + '">What the fee covers'
             '</a></p>')
    b.append(F8.FOOT)
    b.append('</div>')
    b.append(F8.schema(url, title, desc))
    return slug, title, desc, '\n'.join(b)


MONEY_OK = {'0.00', '300.00', '350.00'}


def gate(slug, html):
    """The Family 8 gate, with the price rule swapped for this batch only."""
    bad = []
    for w in F8.BANNED_CRA:
        if w in html.lower():
            bad.append('rule 1 CRA wording %r' % w)
    if re.search(r'\bauthorized\b',
                 html.lower().replace('authorized signing officer', '')):
        bad.append('rule 1 stray "authorized"')
    for m in re.finditer(r'EFILE', html):
        if not html.startswith('EFILE electronic filer', m.start()):
            bad.append('rule 1 EFILE outside the approved phrase')
            break
    if re.search(r'\bT183\b(?!CORP)', html):
        bad.append('rule 2 bare T183')
    for m in re.finditer(r'(no penalty|penalty[- ]free|zero penalty)',
                         html.lower()):
        bad.append('rule 3 unqualified penalty phrase %r' % m.group(1))
    for w in F8.BANNED_CLAIM:
        if w in html.lower():
            bad.append('rule 4 or 6 banned claim %r' % w)
    for w in ('faqpage', 'howto', 'aggregaterating', 'trustindex'):
        if w in html.lower():
            bad.append('rule 6 forbidden schema %r' % w)
    for w in ('book a call', 'calendly', 'free consultation', 'consultation/'):
        if w in html.lower():
            bad.append('rule 7 booking call to action %r' % w)
    # The deviation, enforced positively: the jurisdiction-safe string must be
    # present, and neither HST wording may appear anywhere on these pages.
    if PRICE not in html:
        bad.append('the jurisdiction-safe price string is missing')
    # "GST/HST" is the CRA's own name for the account and is allowed; it is a
    # tax ACCOUNT, not this page's price. Any other mention of HST on a page
    # about a jurisdiction that has none is the error being guarded against.
    _h = html.replace('GST/HST', '')
    for w in ('including HST', 'plus HST', 'HST'):
        if w in _h:
            bad.append('HST named on a non-HST jurisdiction page (%r)' % w)
            break
    for m in re.finditer(r'\$(\d{1,3}(?:,\d{3})*\.\d\d)', html):
        if m.group(1) not in MONEY_OK:
            bad.append('unexpected money figure $%s' % m.group(1))
    # Rate checks run on the body only: the shared style block is full of CSS
    # percentages (width:100% and the like) and a bare \d\s*% hits those.
    _body = re.sub(r'(?s)<style.*?</style>', '', html)
    if re.search(r'\d+(\.\d+)?\s*per cent', _body, re.I):
        bad.append('a tax rate is stated in words')
    if re.search(r'\d\s*%', _body):
        bad.append('a rate in % form is stated')
    for tok in ('CO-17', 'AT1'):
        if tok in html and 'separate return' not in html:
            bad.append('rule 8: %s named without "separate return"' % tok)
    if re.search(r'\ba (?=[AEIOU])', html):
        bad.append('article "a" before a vowel-initial name')
    if html.count('<h1>') != 1:
        bad.append('%d H1' % html.count('<h1>'))
    if html.count('<table') != 1:
        bad.append('%d tables, needs 1' % html.count('<table'))
    if 'CPA Ontario Membership 61040184' not in html:
        bad.append('no byline')
    if 'Last reviewed:' not in html:
        bad.append('no last-reviewed line')
    links = set(re.findall(
        r'href="(https://corpnilfilingfor300\.ca[^"]*)"', html))
    if len(links) > 15:
        bad.append('%d outbound links, cap 15' % len(links))
    if any(ord(c) > 0x2100 for c in html):
        bad.append('non-ASCII symbol that may be an emoji')
    json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                         html, re.S).group(1))
    if bad:
        raise AssertionError('%s GATE FAILED:\n  - %s'
                             % (slug, '\n  - '.join(bad)))
    return links


if __name__ == '__main__':
    recs = []
    for p in PLACES:
        slug, title, desc, html = page(p)
        links = gate(slug, html)
        fn = 'nil-t2-return-cost-' + slug + '.html'
        io.open(os.path.join(HERE, fn), 'w', encoding='utf-8').write(html)
        recs.append(dict(slug='nil-t2-return-cost-' + slug, title=title,
                         desc=desc, url=PRICING + 'nil-t2-return-cost-'
                         + slug + '/', bytes=len(html.encode())))
        print('%-44s %6d bytes  out:%2d' % (slug, len(html.encode()),
                                            len(links)))
    json.dump(recs, io.open(os.path.join(HERE, 'f8c-manifest.json'), 'w',
                            encoding='utf-8'), indent=1)
    print('\n%d pages, gate clear on all' % len(recs))
