#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 8, the two pages Appendix A names outright and nobody built.

NOTE on the style block: it is concatenated with the hero, not joined by a
newline, because the live template has no newline between </style> and the
hero div. An earlier version joined them and was 1 byte longer than what
WordPress holds, which masked a doubled "<" on both pages: the extra
bracket and the extra newline cancelled in the byte total.

    /pricing/cost-to-file-six-unfiled-nil-years/
    /pricing/what-is-not-included/

Both appear in line 1146's sample column beside /pricing/nil-t2-filing-cost/,
which is live. Neither is a jurisdiction page, so neither is touched by the
hard rule 9 question holding the other eight jurisdictions, and neither
carries the near-duplicate problem of the four province cost pages.

THE DUPLICATION PROBLEM THESE TWO HAVE, AND HOW THEY AVOID IT
-------------------------------------------------------------
The live hub at /pricing/nil-t2-filing-cost/ already carries a "Several
Unfiled Years" table and a "What the Fee Does Not Include" list, and the
promise page already carries a six-row table of what sits outside the fee.
So both of these pages are, on their face, expansions of something live.

Writing them as longer versions of those sections would produce exactly what
the four province cost pages produced. They are differentiated on substance
instead:

  - The six-years page is about the SCENARIO, not the arithmetic. The hub
    gives the running total in one table and stops. This page covers why six
    years are six returns rather than one, the order they are filed in, what
    a nil year that sat unfiled actually costs when the penalty is a
    percentage of $0.00, and the point no other page makes: with six years
    the overflow price applies per year, so one non-nil year among six does
    not move the whole file.

  - The not-included page groups the exclusions by WHY the T2 does not reach
    them -- registry filings are not tax returns, two provinces collect
    corporate tax on their own return, other CRA accounts are their own
    accounts -- rather than listing them flat. That grouping is the content;
    the list is live already in two places.

Both are measured against the hub and the promise page before they ship, the
same way Family 7 and the Family 5 batch were.

NO TAX RATE AND NO TAX-INCLUSIVE TOTAL, AS IN THE LAST BATCH
------------------------------------------------------------
The live hub computes Ontario's rate to a total. The newer batch deliberately
does not, for the reason in build_f8_cost.py: the project's own record of
provincial rates is out of date, and these pages cannot verify it from here.
The six-years page therefore gives the fee total and leaves tax to "at the
rate for your province", which is also the only form that stays true in the
eight jurisdictions where HST is the wrong word.
"""
import io
import json
import os
import re

import build_f8_cost as F8

HERE = os.path.dirname(os.path.abspath(__file__))
SITE, PRICING, COST, FORM = F8.SITE, F8.PRICING, F8.COST, F8.FORM
T, C, PRICE = F8.T, F8.C, F8.PRICE
A = SITE + '/answers/'
G = SITE + '/guides/'
PROMISE = PRICING + 'price-transparency-promise/'

QUAL = ('A true nil return carries no percentage late-filing penalty, '
        'because that penalty is a percentage of tax owing and the '
        'corporation owes $0.00. The unfiled year still stays open forever, '
        'invites a demand to file and an arbitrary assessment, blocks a '
        'clearance certificate and dissolution, and costs a non-resident-'
        'owned corporation $25.00 per day up to $2,500.00.')


def six_years_page():
    slug = 'cost-to-file-six-unfiled-nil-years'
    url = PRICING + slug + '/'
    title = 'Cost to File Six Unfiled Nil Years'
    desc = ('Six unfiled nil years are six separate returns at ' + PRICE
            + ', so $1,800.00 in fees. The order they are filed in and what '
              'that does not cover.')
    b = [F8.STYLE + F8.hero(
        'Cost to File Six Unfiled Nil Years',
        '$1,800.00 Plus HST for Six Tax Years',
        'Six unfiled years are six separate returns at the same published '
        'fee. Here is the arithmetic, the order they are filed in, and what '
        'happens if one of the six turns out not to be nil.')]
    b.append('<div class="cnf-w" style="max-width:1000px!important;'
             'margin:0 auto!important;padding:36px 20px 56px!important;'
             'box-sizing:border-box">')
    b.append(F8.crumb(title))
    b.append('<p class="cnf-by">' + F8.BYLINE + '</p>')
    b.append('<p class="cnf-rev">Last reviewed: ' + F8.TODAY + '</p>')
    b.append('<div class="cnf-fee"><p><strong>' + PRICE + '.</strong> '
             'Six tax years is $1,800.00 in fees, plus tax at the rate for '
             'your province.</p><p>Overflow work moves to gondaliyacpa.ca '
             'at $350.00 plus HST per year.</p></div>')

    b.append('<h2>What Six Years Costs</h2>')
    b.append('<p>Each tax year is its own return and carries the same fee, '
             'so the cost is the fee multiplied by the number of years. '
             'There is no bundle rate and no discount for filing several at '
             'once, which is why the column below is simple multiplication '
             'rather than a quote.</p>')
    b.append('<table class="cnf-tbl"><thead><tr>'
             '<th scope="col">Tax years filed</th>'
             '<th scope="col">Our fee, before tax</th></tr></thead><tbody>'
             '<tr><td>1 year</td><td>$300.00</td></tr>'
             '<tr><td>2 years</td><td>$600.00</td></tr>'
             '<tr><td>3 years</td><td>$900.00</td></tr>'
             '<tr><td>4 years</td><td>$1,200.00</td></tr>'
             '<tr><td>5 years</td><td>$1,500.00</td></tr>'
             '<tr><td><strong>6 years</strong></td>'
             '<td><strong>$1,800.00</strong></td></tr>'
             '</tbody></table>')
    b.append('<p>Tax is added at the rate for your province and the whole '
             'amount is on the screen before you pay. The fee itself does '
             'not change by province. The '
             '<a href="' + T + 'unfiled-years-cost-calculator/">unfiled '
             'years cost calculator</a> totals any number of years.</p>')

    b.append('<h2>Why It Is Six Returns and Not One</h2>')
    b.append('<p>A T2 corporation income tax return covers one tax year. '
             'There is no combined return for several years and no way to '
             'report six dormant years on a single form, so six unfiled '
             'years means six returns prepared, reviewed and transmitted '
             'separately.</p>')
    b.append('<p>Each of the six carries its own GIFI schedules for that '
             'year, its own Form T183CORP signed with that year&rsquo;s '
             'figures, and its own confirmation from the Canada Revenue '
             'Agency. We are a registered EFILE electronic filer and each '
             'year is transmitted electronically in its own transmission. '
             'That is the work the fee multiplies against.</p>')

    b.append('<h2>The Order They Are Filed In</h2>')
    b.append('<p>Oldest year first, then forward in sequence. A corporation '
             'carries figures from one year into the next, and even a '
             'dormant corporation carries its share capital and its balance '
             'sheet forward, so a later year transmitted before an earlier '
             'one can be assessed against figures that have not been filed '
             'yet.</p>')
    b.append('<p>Filing in order also matters to what the Canada Revenue '
             'Agency sees. Six years arriving oldest first reads as a '
             'corporation bringing itself current. '
             '<a href="' + A + 'how-do-i-catch-up-on-years-of-unfiled-t2-'
             'returns/">How to catch up on years of unfiled T2 returns</a> '
             'sets out the sequence in full.</p>')

    b.append('<h2>What a Nil Year Costs by Sitting Unfiled</h2>')
    b.append('<p>' + QUAL + '</p>')
    b.append('<p>So the cost of six unfiled nil years is not a penalty '
             'figure. It is the fee for six returns, plus whatever the open '
             'years have already blocked: a clearance certificate, a '
             'dissolution, a financing application or a sale that needs the '
             'corporation current. Our answer on '
             '<a href="' + A + 'how-many-years-of-unfiled-t2-returns-can-i-'
             'catch-up/">how many years you can catch up</a> covers how far '
             'back you can go.</p>')

    b.append('<h2>If One of the Six Years Is Not Nil</h2>')
    b.append('<p>This is the part that only comes up with several years at '
             'once. Nil is decided year by year, not for the corporation as '
             'a whole, so a corporation can have five dormant years and one '
             'year in which it earned interest, paid a dividend or held a '
             'rental property.</p>')
    b.append('<p>Where that happens only that year moves. It goes to '
             'Gondaliya CPA Professional Corporation at gondaliyacpa.ca at '
             '$350.00 plus HST per year, and the five nil years stay here at '
             'the published fee. One year outside the service does not move '
             'the whole file, and nothing at the higher price is charged '
             'without you agreeing to it first.</p>')
    b.append('<p>A holding corporation with investment income, '
             'an inactive corporation that received a dividend, and a '
             'rental corporation are the three cases that catch people out. '
             'None of them is nil. The '
             '<a href="' + T + 'nil-t2-eligibility-checker/">eligibility '
             'checker</a> settles it year by year before you pay.</p>')

    b.append('<h2>What the Six Returns Do Not Cover</h2>')
    b.append('<p>Six years of T2 returns settle six years of corporate '
             'income tax with the Canada Revenue Agency. They do not settle '
             'six years of annual returns with your registry, which is a '
             'separate filing to a separate body and is not a tax return at '
             'all. A corporation six years behind on its T2 returns is '
             'usually six years behind on those too.</p>')
    b.append('<p><a href="' + PRICING + 'what-is-not-included/">What is not '
             'included in the fee</a> sets out every filing that sits '
             'outside it and why the T2 does not reach it.</p>')

    b.append('<p><a class="cnf-btn" href="' + FORM + '">'
             'Start Nil T2 Filing NOW</a>'
             '<a class="cnf-btn" href="' + COST + '">What the fee covers'
             '</a></p>')
    b.append(F8.FOOT)
    b.append('</div>')
    b.append(F8.schema(url, title, desc))
    return slug, title, desc, '\n'.join(b)


def not_included_page():
    slug = 'what-is-not-included'
    url = PRICING + slug + '/'
    title = 'What Is Not Included in the Nil T2 Fee'
    desc = ('The nil T2 fee covers one corporate return for one tax year. '
            'Registry annual returns, CO-17, AT1 and other CRA accounts sit '
            'outside it.')
    b = [F8.STYLE + F8.hero(
        'What Is Not Included in the Nil T2 Fee',
        '$300.00 Plus HST Per Tax Year, and What Sits Outside It',
        'The fee covers one nil T2 corporation income tax return for one '
        'tax year, prepared, CPA reviewed and transmitted. Everything below '
        'is a separate filing to a separate body.')]
    b.append('<div class="cnf-w" style="max-width:1000px!important;'
             'margin:0 auto!important;padding:36px 20px 56px!important;'
             'box-sizing:border-box">')
    b.append(F8.crumb(title))
    b.append('<p class="cnf-by">' + F8.BYLINE + '</p>')
    b.append('<p class="cnf-rev">Last reviewed: ' + F8.TODAY + '</p>')
    b.append('<div class="cnf-fee"><p><strong>' + PRICE + '.</strong> '
             'One nil T2 corporation income tax return, for one tax year, '
             'prepared and transmitted.</p><p>Overflow work moves to '
             'gondaliyacpa.ca at $350.00 plus HST per year.</p></div>')

    b.append('<h2>Why Anything Sits Outside It at All</h2>')
    b.append('<p>A nil T2 is one return, to one body, for one tax year. '
             'Most of what gets mistaken for part of it is not a corporate '
             'income tax return and never travels with one, so no fee for a '
             'T2 could include it. The exclusions below are grouped by the '
             'reason the T2 does not reach them rather than listed flat, '
             'because the reason is what tells you whether you owe the '
             'filing.</p>')

    b.append('<h2>Registry Filings Are Not Tax Returns</h2>')
    b.append('<p>Every corporation has a registry as well as a tax account, '
             'and the registry wants to know the corporation still exists '
             'and who its directors are. That is an annual return, and the '
             'word is the whole problem: it is not an income tax return and '
             'it reports no money.</p>')
    b.append('<p>If you are federally incorporated, Corporations Canada '
             'wants an annual return and charges $12.00 for it. If you are '
             'provincially incorporated, your province&rsquo;s registry '
             'wants its own. In Ontario that has gone through the Ontario '
             'Business Registry since October 2021, which is why it no '
             'longer arrives attached to the T2 the way Schedule 546 once '
             'did. Neither is in the fee.</p>')
    b.append('<p>The <a href="' + C + 'ontario-annual-return-vs-t2/">Ontario '
             'annual return compared with the T2</a> sets the two side by '
             'side, and the '
             '<a href="' + T + 'ontario-business-registry-filing-checker/">'
             'registry filing checker</a> says which of them you owe.</p>')

    b.append('<h2>Two Provinces Collect Corporate Tax on Their Own Return'
             '</h2>')
    b.append('<p>In most of Canada one T2 settles federal and provincial '
             'corporate income tax together, because the province levies it '
             'through the federal return. Two do not.</p>')
    b.append('<p>Quebec collects its corporate income tax on the CO-17, '
             'filed with Revenu Quebec, and Alberta collects its on the AT1. '
             'Each is a separate return in its own right rather than a '
             'schedule of the T2, so a Quebec or Alberta corporation with a '
             'dormant year has two returns to file and the fee covers one of '
             'them. The <a href="' + T + 'provincial-return-requirement-'
             'checker/">provincial return requirement checker</a> answers it '
             'for any province.</p>')

    b.append('<h2>Your Other CRA Accounts Are Filed Separately</h2>')
    b.append('<p>A corporation can hold a GST/HST account and a payroll '
             'account alongside its corporate income tax account. They are '
             'separate accounts with separate filing obligations, and a '
             'dormant year does not close any of them.</p>')
    b.append('<p>A GST/HST return is still due for a period with no sales, '
             'and a payroll account still expects its filings even with no '
             'employees paid. Closing either one is its own form, RC145. '
             'None of that is in the fee, and the '
             '<a href="' + C + 'nil-t2-vs-nil-gst-hst-return/">nil T2 '
             'compared with a nil GST/HST return</a> explains why the two '
             'are not the same filing.</p>')

    b.append('<h2>Bookkeeping, and Years With Something in Them</h2>')
    b.append('<p>A nil year needs nil GIFI schedules, and preparing those '
             'from a dormant year is part of the fee. A year with '
             'transactions in it needs books before any return can be '
             'prepared, and that is bookkeeping rather than filing.</p>')
    b.append('<p>The same line decides the price. A tax year with no '
             'activity is filed here at the published fee. A year with '
             'investment income, rental income, or a dividend paid or '
             'received is not nil, moves to gondaliyacpa.ca at $350.00 plus '
             'HST per year, and is told to you before anything further is '
             'charged. If it is found after you have paid, you are refunded '
             'in full.</p>')

    b.append('<h2>Incorporating, Dissolving and Clearance</h2>')
    b.append('<p>Setting a corporation up and winding one down are both '
             'outside this service. Incorporation is its own filing to the '
             'registry. Dissolution needs a final T2 for the part year, the '
             'registry&rsquo;s own dissolution filing, and in most cases a '
             'clearance certificate from the Canada Revenue Agency before '
             'assets are distributed.</p>')
    b.append('<p>The final return itself is a nil T2 where the last year had '
             'no activity, and that one is in the fee. The rest of the '
             'wind-up is not. The '
             '<a href="' + G + 'final-t2-and-dissolution/">final T2 and '
             'dissolution guide</a> sets out the sequence.</p>')

    b.append('<h2>The Whole List, and Why</h2>')
    b.append('<table class="cnf-tbl"><thead><tr>'
             '<th scope="col">Filing</th>'
             '<th scope="col">Who wants it</th>'
             '<th scope="col">Why the T2 does not reach it</th>'
             '</tr></thead><tbody>'
             '<tr><td>Provincial registry annual return</td>'
             '<td>Your province of incorporation</td>'
             '<td>A registry filing, not an income tax return</td></tr>'
             '<tr><td>Corporations Canada annual return, $12.00</td>'
             '<td>Corporations Canada</td>'
             '<td>A registry filing, not an income tax return</td></tr>'
             '<tr><td>Quebec CO-17</td><td>Revenu Quebec</td>'
             '<td>Quebec collects corporate tax on a separate return</td>'
             '</tr>'
             '<tr><td>Alberta AT1</td><td>Alberta</td>'
             '<td>Alberta collects corporate tax on a separate return</td>'
             '</tr>'
             '<tr><td>Nil GST/HST return</td>'
             '<td>The Canada Revenue Agency</td>'
             '<td>A different account with its own filing cycle</td></tr>'
             '<tr><td>Payroll and T4 filings</td>'
             '<td>The Canada Revenue Agency</td>'
             '<td>A different account with its own filing cycle</td></tr>'
             '<tr><td>RC145 account closures</td>'
             '<td>The Canada Revenue Agency</td>'
             '<td>Closes an account rather than reporting a tax year</td>'
             '</tr>'
             '<tr><td>Bookkeeping for a year with activity</td>'
             '<td>Needed before any return</td>'
             '<td>That year is not nil</td></tr>'
             '<tr><td>Incorporation and dissolution filings</td>'
             '<td>Your registry</td>'
             '<td>Not a tax filing at all</td></tr>'
             '<tr><td>Clearance certificate</td>'
             '<td>The Canada Revenue Agency</td>'
             '<td>A wind-up step that follows the final return</td></tr>'
             '</tbody></table>')

    b.append('<h2>How to Tell Which of These You Owe</h2>')
    b.append('<p>We tell you which ones are outstanding on the way in rather '
             'than afterwards, and that commitment is one of the four on the '
             '<a href="' + PROMISE + '">price transparency promise</a>. The '
             '<a href="' + T + 'what-the-nil-t2-fee-covers-checker/">'
             'fee-covers checker</a> walks the list question by question.</p>')
    b.append('<p>Filing several years at once does not change any of this, '
             'though it does multiply the fee. '
             '<a href="' + PRICING + 'cost-to-file-six-unfiled-nil-years/">'
             'Six unfiled nil years</a> works that case through.</p>')

    b.append('<p><a class="cnf-btn" href="' + FORM + '">'
             'Start Nil T2 Filing NOW</a>'
             '<a class="cnf-btn" href="' + COST + '">What the fee covers'
             '</a></p>')
    b.append(F8.FOOT)
    b.append('</div>')
    b.append(F8.schema(url, title, desc))
    return slug, title, desc, '\n'.join(b)


# The last batch's gate, with the multi-year fee totals and the two figures
# the 7.4 qualification block is obliged to carry added to the money
# allowlist. Nothing else about it is relaxed.
MONEY_OK = {'0.00', '12.00', '25.00', '300.00', '350.00', '600.00',
            '900.00', '1,200.00', '1,500.00', '1,800.00', '2,500.00'}


def gate(slug, html):
    saved = F8.MONEY_OK
    F8.MONEY_OK = MONEY_OK
    try:
        F8.gate(slug, html)
    finally:
        F8.MONEY_OK = saved
    bad = []
    if html.count('<h1>') != 1:
        bad.append('%d H1' % html.count('<h1>'))
    if html.count('<table') != 1:
        bad.append('%d tables, needs exactly 1' % html.count('<table'))
    if 'CPA Ontario Membership 61040184' not in html:
        bad.append('no byline')
    if 'Last reviewed:' not in html:
        bad.append('no last-reviewed line')
    # Hard rule 3: the word may not stand alone anywhere on the page.
    if 'penalty' in html.lower() and QUAL not in html:
        bad.append('penalty mentioned without the 7.4 qualification block')
    links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"',
                           html))
    if len(links) > 15:
        bad.append('%d outbound links, cap is 15' % len(links))
    if any(ord(c) > 0x2100 for c in html):
        bad.append('non-ASCII symbol that may be an emoji')
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>',
                  html, re.S)
    json.loads(m.group(1))
    if bad:
        raise AssertionError('%s GATE FAILED:\n  - %s'
                             % (slug, '\n  - '.join(bad)))


if __name__ == '__main__':
    recs = []
    for slug, title, desc, html in [six_years_page(), not_included_page()]:
        gate(slug, html)
        assert 70 <= len(desc) <= 160, '%s: meta %d chars' % (slug, len(desc))
        io.open(os.path.join(HERE, slug + '.html'), 'w',
                encoding='utf-8').write(html)
        n = len(set(re.findall(
            r'href="(https://corpnilfilingfor300\.ca[^"]*)"', html)))
        recs.append(dict(slug=slug, title=title, desc=desc,
                         url=PRICING + slug + '/',
                         bytes=len(html.encode())))
        print('%-36s %6d bytes  out:%2d  %s'
              % (slug, len(html.encode()), n, PRICING + slug + '/'))
    json.dump(recs, io.open(os.path.join(HERE, 'f8b-manifest.json'), 'w',
                            encoding='utf-8'), indent=1)
    print('\n%d pages, gate clear on both' % len(recs))
