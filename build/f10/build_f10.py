#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 10, how-to-start and first-filing. The first ten pages.

Family 10 was 0 of 25 before this batch. Nothing under /start/ existed.

WHY THE HUB IS IN THIS BATCH THOUGH APPENDIX A DOES NOT LIST IT
---------------------------------------------------------------
Appendix A's Family 10 roster is 25 URLs: twelve
/start/first-t2-after-incorporating-in-<year>/ pages for 2015 to 2026, and
thirteen /start/what-a-new-<jurisdiction>-corporation-must-file/ pages.

`/start/first-t2-return-after-incorporation/` is NOT among them. It is
nevertheless the most important page in the family, because three separate
parts of the plan point at it:

  - 6(k) names it as the canonical target for the cross-site collision with
    gondaliyacpa.ca /new-corporation-tax-setup/ and opencorporationfor35.ca
    /after-you-incorporate/. Unlike /guides/final-t2-and-dissolution/, which
    an earlier entry wrongly claimed was in 6(k), this one really is.
  - Line 1275 makes it the target for "first t2 return after incorporation",
    260 searches a month, the family's head term.
  - Line 1532 makes it the inbound link target for every Family 10 page.

A family whose own internal linking rule points every page at a URL that does
not exist cannot be built without it. So this batch is the hub plus nine year
pages, and the over-count against the planned 25 is logged rather than
resolved, as with Family 5 at 46 and Family 8 at 18.

THE YEAR SERIES WAS BUILT, MEASURED AT 0.99, AND ABANDONED
----------------------------------------------------------
This batch was first written as the hub plus nine
/start/first-t2-after-incorporating-in-<year>/ pages for 2018 to 2026, on the
theory that the year changes the answer: how many returns are outstanding,
whether mandatory electronic filing reaches the first return, whether that
return is overdue or still ahead.

Measured before publishing, as every batch now is: **worst pair 0.99, with 15
of 45 pairs at or above 0.90.** Six of the nine pages came out at identical
byte counts. That is worse than the four Atlantic cost pages at 0.94 to 0.96
which this repo already records as its cautionary example.

The differentiation was cosmetic. The prose was the same with a digit
substituted, because for a NIL return the incorporation year genuinely does
not change the answer: a dormant year is dormant whenever the corporation was
registered. The mandatory e-filing rule created two buckets rather than nine,
so 2018 through 2023 were the same page nine-tenths of the way through.

This is the same structural fault the thirteen jurisdiction cost pages had,
and it is worth stating plainly: **Appendix A contains year series and place
series that cannot all be written as distinct pages.** Where the axis does not
change the answer, the roster count is not reachable without producing what
the plan's own 6(k) calls the pattern the March 2026 updates removed.

The year pages were deleted rather than published. They are recoverable from
this file's history if a per-year angle is ever found that is not a digit
swap.

SO THIS BATCH IS THE HUB PLUS NINE JURISDICTIONS
------------------------------------------------
Appendix A's other Family 10 series is
/start/what-a-new-<jurisdiction>-corporation-must-file/, and jurisdiction is
an axis that does change the answer. It is the same axis that moved the
Family 8 cost pages from 0.96 to 0.73 earlier today:

  - Quebec files a CO-17 and Alberta an AT1, each a separate provincial
    return, so a new corporation there has two corporate returns, not one.
  - Everywhere else one T2 settles federal and provincial corporate tax, and
    the separate filing is the registry's own annual return.
  - Ontario's annual return has gone through the Ontario Business Registry
    since October 2021 and no longer travels with the T2 as Schedule 546 did.
  - The sales tax added to the fee differs: HST, GST plus QST, GST plus a
    provincial sales tax, or GST alone.

Nine are built here: Ontario, Quebec, British Columbia, Alberta, Manitoba,
Saskatchewan, Nova Scotia, New Brunswick and Newfoundland and Labrador. Prince
Edward Island, Yukon, the Northwest Territories and Nunavut are the next four.

THE FEE LINE
------------
"$300.00 plus applicable sales tax per tax year", the wording Navneet approved
today for the Family 8 jurisdiction pages, with the specific tax named per
jurisdiction in the fee box. A jurisdiction series cannot say "plus HST" when
five of its nine jurisdictions do not charge HST.

WHAT EVERY PAGE MUST CARRY, per line 1218
-----------------------------------------
"No first-filing page publishes without the Schedule 24 line and the 53-week
line." The qualification wording from the same row is used verbatim:

  "The first tax year cannot exceed 53 weeks and the year-end must match
   CRA's record or the transmission is rejected."

Line 344: steps render as an ordered list with NO HowTo markup, which is also
hard rule 6. Line 1532: one cross-domain link per page, to
opencorporationfor35.ca. "instant filing" is the family's banned phrase.
"""
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
OPEN = 'https://opencorporationfor35.ca/'
FORM = SITE + '/form/'
T = SITE + '/tools/'
G = SITE + '/guides/'
A = SITE + '/answers/'
START = SITE + '/start/'
COST = SITE + '/pricing/nil-t2-filing-cost/'
HUB = 'first-t2-return-after-incorporation'
PRICE = '$300.00 plus applicable sales tax per tax year'
OVERFLOW = ('Overflow work moves to gondaliyacpa.ca at $350.00 plus '
            'applicable sales tax per year.')
TODAY, ISO = 'November 11, 2026', '2026-11-11'
NOW_YEAR = 2026
BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')
# The Family 8 style block, plus the two rules this family needs and that one
# does not carry: .cnf-qual for the three-rules box and .cnf-steps for the
# ordered list line 344 requires. Without them both render unstyled.
_EXTRA = ('\n.cnf-qual{background:#f5f8fc;border-left:5px solid #314d8a;'
          'border-radius:0 8px 8px 0;padding:18px 22px;margin:18px 0}'
          '\n.cnf-qual strong{color:#314d8a}'
          '\n.cnf-steps{margin:16px 0 16px 22px;padding:0}'
          '\n.cnf-steps li{margin:0 0 10px}'
          # Full-bleed hero and no gap above it. The theme puts the article in
          # a padded, boxed container, so the hero was inset on both sides and
          # sat below that container's top padding. The calc(50% - 50vw) pair
          # pulls the band out to the viewport edges from inside any centred
          # ancestor; the rules under it zero the container's own top padding.
          # .cnf-w keeps its own max-width and padding inline, so stripping
          # the article padding does not touch the body text.
          '\n.cnf-hero{margin-left:calc(50% - 50vw);'
          'margin-right:calc(50% - 50vw);width:100vw;max-width:100vw}'
          '\n.ast-separate-container .ast-article-single{padding:0!important;'
          'margin:0!important;border-radius:0}'
          '\n.site-content>.ast-container{padding-top:0!important}'
          '\n.ast-separate-container .site-main>.ast-row{margin-top:0!important}'
          '\n.entry-content>:first-child{margin-top:0!important}'
          '\n#primary{padding-top:0!important;margin-top:0!important}')
STYLE = io.open(os.path.join(HERE, '..', 'f8', '_f8_style.txt'),
                encoding='utf-8').read()
assert STYLE.rstrip().endswith('</style>')
STYLE = STYLE.rstrip()[:-len('</style>')] + _EXTRA + '</style>' 

RULE53 = ('The first tax year cannot exceed 53 weeks and the year-end must '
          "match CRA's record or the transmission is rejected.")
SCHED24 = ('Schedule 24, the first-time filer schedule, is required on the '
           'first T2 a corporation ever files.')

PLACES = [
 dict(slug='ontario', name='Ontario', sales='the HST', route='t2',
      angle='The Annual Return Left the T2 in 2021',
      lede=('A new Ontario corporation files one T2 that settles federal and '
            'Ontario corporate income tax together. What it also owes, and '
            'what most new directors miss, is a separate annual return to the '
            'Ontario Business Registry.'),
      paras=['Until October 2021 the Ontario annual return travelled with the '
             'T2 as Schedule 546, so filing the tax return dealt with both. '
             'It does not any more. The annual return now goes to the Ontario '
             'Business Registry on its own, and nothing about filing the T2 '
             'tells the registry the corporation still exists.',
             'That is the single most common gap on a young Ontario '
             'corporation: the tax returns are filed and the registry filings '
             'are years behind. They are caught up separately.']),
 dict(slug='quebec', name='Quebec', sales='the GST and the QST',
      route='separate', sep='CO-17', body='Revenu Quebec',
      angle='Two Corporate Returns From the First Year',
      lede=('A new Quebec corporation files two corporate income tax returns '
            'for its first year, not one: the federal T2 and the CO-17 with '
            'Revenu Quebec.'),
      paras=['Quebec collects its corporate income tax on the CO-17, which is '
             'a separate return in its own right rather than a schedule of '
             'the federal T2. A first year with no activity still needs both '
             'filed.',
             'The fee on this page covers the federal T2. It does not cover '
             'the CO-17, and that is the first thing to understand about what '
             'a new Quebec corporation owes.']),
 dict(slug='british-columbia', name='British Columbia',
      sales='the GST and the provincial sales tax where it applies',
      route='t2',
      angle='One Tax Return, One Registry Filing',
      lede=('A new British Columbia corporation files one T2, which settles '
            'federal and provincial corporate income tax together. The '
            'separate obligation is a registry filing rather than a second '
            'tax return.'),
      paras=['British Columbia levies corporate income tax through the '
             'federal return, so there is no provincial corporate return to '
             'find. That puts it on the opposite footing from Quebec and '
             'Alberta.',
             'The registry still wants to hear from the corporation every '
             'year, and that filing reports no money and is not a tax return. '
             'It is not in this fee.']),
 dict(slug='alberta', name='Alberta', sales='the GST', route='separate',
      sep='AT1', body='Alberta',
      angle='No Sales Tax, and Still a Second Return',
      lede=('Alberta is the only province with no provincial sales tax, so '
            'the tax on this fee is the GST alone. It is also one of only two '
            'provinces that collects corporate income tax on its own return.'),
      paras=['Alberta collects corporate income tax on the AT1, a separate '
             'return rather than a schedule of the federal T2. A new Alberta '
             'corporation therefore has two corporate returns for its first '
             'year even if nothing happened in it.',
             'Having no provincial sales tax is the part people know. Having '
             'a second corporate return is the part that catches them out.']),
 dict(slug='manitoba', name='Manitoba',
      sales='the GST and the provincial sales tax where it applies',
      route='t2',
      angle='What the First Year Actually Owes',
      lede=('A new Manitoba corporation files one T2 for its first tax year. '
            'Manitoba collects its corporate income tax through that same '
            'federal return, so there is no second corporate return.'),
      paras=['That makes the first-year list short: one T2, carrying Schedule '
             '24, for a tax year that cannot exceed 53 weeks. If nothing '
             'happened in that year the figures are nil and the return is '
             'still filed.',
             'The separate item is the registry annual filing, which reports '
             'that the corporation exists and who its directors are, and is '
             'not a tax return.']),
 dict(slug='saskatchewan', name='Saskatchewan',
      sales='the GST and the provincial sales tax where it applies',
      route='t2',
      angle='The Year-End Choice Binds Everything After It',
      lede=('A new Saskatchewan corporation files one T2 that settles both '
            'the federal and the provincial side. The decision that matters '
            'most in the first year is not which returns to file but when the '
            'year ends.'),
      paras=['The first tax year runs from incorporation to a year-end no '
             'more than 53 weeks later, and that date is chosen once. Every '
             'return after it is measured from the same date, and changing it '
             'later needs the Canada Revenue Agency to agree.',
             'A year-end picked without thinking is the reason a corporation '
             'ends up with a deadline in its busiest month for the rest of '
             'its life.']),
 dict(slug='nova-scotia', name='Nova Scotia', sales='the HST', route='t2',
      angle='One Return, and the Registry Separately',
      lede=('A new Nova Scotia corporation files one T2, which settles '
            'federal and provincial corporate income tax together. The '
            'registry filing is separate and is not a tax return.'),
      paras=['Nova Scotia levies its corporate income tax through the federal '
             'return, so a first year with no activity means one nil T2 '
             'carrying Schedule 24, and nothing else to the Canada Revenue '
             'Agency for corporate income tax.',
             'What is easy to miss is that the corporation also has to keep '
             'itself current with its registry, every year, from the first '
             'year onward.']),
 dict(slug='new-brunswick', name='New Brunswick', sales='the HST', route='t2',
      angle='A Dormant First Year Is Still a Filed Year',
      lede=('A new New Brunswick corporation files one T2 for its first tax '
            'year, settling federal and provincial corporate income tax '
            'together. A first year with nothing in it is still a year that '
            'needs a return.'),
      paras=['The most common reason a new corporation misses its first '
             'return is believing that no activity means nothing to file. '
             'It does not. The return reports nil figures and is filed on '
             'time like any other.',
             'That first return is also the only one that carries Schedule '
             '24, so it is the one that cannot simply be copied from the year '
             'before.']),
 dict(slug='newfoundland-and-labrador', name='Newfoundland and Labrador',
      sales='the HST', route='t2',
      angle='Everything Happens Electronically',
      lede=('A new Newfoundland and Labrador corporation files one T2, which '
            'settles federal and provincial corporate income tax together, '
            'and the whole of it happens electronically.'),
      paras=['The return is transmitted rather than posted, and Form T183CORP '
             'is signed on a secure single-use screen rather than printed. '
             'The Canada Revenue Agency accepts an electronic signature on '
             'it.',
             'Mandatory T2 electronic filing reaches tax years beginning '
             'after 2023, so a corporation registered now is inside it from '
             'its very first return.']),
]



# A second, genuinely different section per jurisdiction. Without it the six
# provinces where one T2 settles the corporate tax measured 0.84 against each
# other, because their obligations really are nearly identical. Each heading
# below is a different topic rather than the same topic reworded, which is the
# only thing that moves the number honestly. {T} is the tools base.
SECOND = {
 'ontario': ('Federal or Ontario Incorporation Changes the Count', [
   'A corporation operating in Ontario may be incorporated federally or under '
   'Ontario law, and that choice decides how many annual filings it owes. A '
   'federal corporation answers to Corporations Canada as well, which charges '
   '$12.00 a year for its own annual return.',
   'So a federally incorporated corporation with an Ontario head office has '
   'two registry filings a year on top of the T2, and an Ontario corporation '
   'has one. Neither is in this fee.']),
 'quebec': ('Three Filings, Not Two', [
   'The CO-17 is the second corporate return. The third item is the annual '
   'updating declaration to the Registraire des entreprises, which keeps the '
   "corporation's registry record current and is not a tax return at all.",
   'A new Quebec corporation that has done nothing in its first year still '
   'owes all three: the federal T2, the CO-17 and the registry declaration. '
   'The fee here covers the first.']),
 'british-columbia': ('Operating in Another Province', [
   'Incorporating in British Columbia registers the corporation in British '
   'Columbia. Carrying on business in another province usually means '
   'registering there as well, which is an extra-provincial registration and '
   'a registry matter rather than a tax one.',
   'It can also create a permanent establishment elsewhere, which changes '
   'which province the corporate income is allocated to. On a dormant first '
   'year with no activity anywhere none of that bites, and the '
   '<a href="{T}permanent-establishment-checker/">permanent establishment '
   'checker</a> is where to test it once trading starts.']),
 'alberta': ('The AT1 Has Its Own Deadline', [
   'The AT1 is not filed with the T2 and does not inherit its dates. It is a '
   'separate return with its own filing requirement, and a year with no '
   'activity does not remove it.',
   'That matters in the first year specifically, because a new director who '
   'files the federal return and stops will often not hear anything until the '
   'province asks.']),
 'manitoba': ('What Counts as Activity in the First Year', [
   'A first year is nil when nothing happened in it. Issuing shares at '
   'incorporation does not count as activity, and neither does holding an '
   'empty bank account.',
   'What does count is income of any kind, including interest on a balance, '
   'and a dividend paid or received. One of those in the first year makes it '
   'a year that is not nil, and the test is applied per year rather than '
   'once.']),
 'saskatchewan': ('Schedule 24 Is Filed Once and Never Again', [
   'Schedule 24 identifies a corporation as a first-time filer and reports '
   'who controls it. It is carried on the first T2 a corporation ever files '
   'and on no return after that.',
   'Because it appears once, it is the part of a first return most often left '
   'off, and leaving it off makes the return incomplete rather than late. The '
   '<a href="{T}schedule-24-first-return-checker/">Schedule 24 checker</a> '
   'confirms whether a given return counts as the first.']),
 'nova-scotia': ('A GST/HST Account Is a Separate Decision', [
   'Incorporating does not open a GST/HST account and does not require one. A '
   'corporation registers when it has to, and a dormant corporation with no '
   'sales generally has nothing to register for.',
   'If an account is opened anyway it brings its own filing cycle with it, '
   'and returns fall due on that account whether or not there were any sales. '
   'That is a common way a dormant corporation ends up behind on filings it '
   'did not know it had.']),
 'new-brunswick': ('What Happens If the First Return Is Not Filed', [
   'An unfiled first year does not go quiet. It stays open, and the Canada '
   'Revenue Agency can issue a demand to file and, failing that, assess the '
   'corporation on figures of its own choosing.',
   'An arbitrary assessment on a corporation that earned nothing is replaced '
   'by filing the real return, which is why a nil first year is worth filing '
   'promptly rather than eventually.']),
 'newfoundland-and-labrador': ('Signing the First Return', [
   'Form T183CORP authorises the transmission, and a signing officer of the '
   'corporation signs it before the return goes. On a brand new corporation '
   'that is usually the sole director.',
   'It is signed once per tax year and per return, so catching up several '
   'years means one form for each. It is kept rather than filed, and produced '
   'if the Canada Revenue Agency asks.']),
}

def crumb(title, hub=False):
    mid = ('' if hub else
           '<a href="' + START + HUB + '/">First T2 after incorporation</a>'
           ' &rsaquo; ')
    return ('<nav class="cnf-crumb" aria-label="Breadcrumb">'
            '<a href="' + SITE + '/">Nil T2 filing in Canada</a> &rsaquo; '
            + mid + '<span aria-current="page">' + title + '</span></nav>')


def hero(h1, sub, lede):
    return ('<div class="cnf-hero"><div class="cnf-hero-in" '
            'style="max-width:1140px;margin:0 auto;text-align:left">'
            '<h1>' + h1 + '</h1>'
            '<p class="cnf-hero-sub">' + sub + '</p>'
            '<p class="cnf-hero-lede">' + lede + '</p>'
            '<p><a class="cnf-hero-btn" href="' + FORM + '">'
            'Start Nil T2 Filing NOW</a></p></div></div>')


def schema(url, name, desc):
    crumbs = [{'@type': 'ListItem', 'position': 1,
               'name': 'Nil T2 filing in Canada', 'item': SITE + '/'}]
    if not url.endswith(HUB + '/'):
        crumbs.append({'@type': 'ListItem', 'position': 2,
                       'name': 'First T2 after incorporation',
                       'item': START + HUB + '/'})
    crumbs.append({'@type': 'ListItem', 'position': len(crumbs) + 1,
                   'name': name, 'item': url})
    g = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': url + '#webpage', 'url': url,
         'name': name, 'description': desc, 'inLanguage': 'en-CA',
         'dateModified': ISO,
         'author': {'@type': 'Person', 'name': 'Sharad Gondaliya',
                    'honorificSuffix': 'CPA',
                    'url': SITE + '/sharad-gondaliya-cpa/'}},
        {'@type': 'BreadcrumbList', 'itemListElement': crumbs}]}
    return ('<script type="application/ld+json">'
            + json.dumps(g, separators=(',', ':')) + '</script>')


FOOT = ('<p class="cnf-foot">Your return is prepared and transmitted in '
        'Canada. Our credentials are never shared and no part of your file '
        'is sent offshore. <a href="' + COST + '">Nil T2 filing price</a></p>')


def rules_block():
    """The three first-year rules. Line 1218 requires the Schedule 24 line
    and the 53-week line on every page in this family."""
    return ('<div class="cnf-qual"><p><strong>The three first-year rules.'
            '</strong> ' + RULE53 + ' ' + SCHED24 + ' The year-end you report '
            'is the one the Canada Revenue Agency holds on file, so a '
            'different date on the return is refused rather than '
            'corrected.</p></div>')


def steps_block(first):
    """An ordered list, with no HowTo markup. Line 344 and hard rule 6."""
    rest = ['Confirm the year-end the Canada Revenue Agency holds, because '
            'the return is matched against it.',
            'Check the first tax year against the 53-week limit.',
            'Complete Schedule 24, which the first return always carries.',
            'Prepare the nil GIFI schedules for the year: Schedule 100, '
            'Schedule 125 and Schedule 141.',
            'Sign Form T183CORP for that tax year on a secure single-use '
            'screen.',
            'Transmit the return and keep the confirmation.']
    items = [first] + rest
    return ('<h2>The Order It Happens In</h2><ol class="cnf-steps">'
            + ''.join('<li>' + s + '</li>' for s in items) + '</ol>')


def tail(extra_links):
    return ('<h2>Where the Rest of the Answer Is</h2>'
            '<p>The <a href="' + G + 'first-year-t2-filing/">first-year T2 '
            'filing guide</a> covers the whole subject, the '
            '<a href="' + T + 'schedule-24-first-return-checker/">Schedule 24 '
            'checker</a> confirms whether a return counts as a first return, '
            'and the <a href="' + T + '53-week-first-tax-year-checker/">'
            '53-week checker</a> tests the first year-end. ' + extra_links
            + '</p>'
            '<p>If the corporation does not exist yet, incorporation is a '
            'separate step on a separate site: '
            '<a href="' + OPEN + '">opencorporationfor35.ca</a> covers it, '
            'and this page picks up once the corporation is registered.</p>'
            '<p>Filing here is ' + PRICE + '. See the full '
            '<a href="' + COST + '">nil T2 filing cost</a> and what it '
            'covers.</p>'
            '<p><a class="cnf-btn" href="' + FORM + '">'
            'Start Nil T2 Filing NOW</a>'
            '<a class="cnf-btn" href="' + T
            + 'schedule-24-first-return-checker/">Check Schedule 24</a></p>')


def wrap(title, sub, lede, body, slug, desc, hub=False):
    url = START + slug + '/'
    h = [STYLE + hero(title, sub, lede)]
    h.append('<div class="cnf-w" style="max-width:1000px!important;'
             'margin:0 auto!important;padding:36px 20px 56px!important;'
             'box-sizing:border-box">')
    h.append(crumb(title, hub))
    h.append('<p class="cnf-by">' + BYLINE + '</p>')
    h.append('<p class="cnf-rev">Last reviewed: ' + TODAY + '</p>')
    h.append(body)
    h.append(FOOT)
    h.append('</div>')
    h.append(schema(url, title, desc))
    return slug, title, desc, '\n'.join(h)


def hub_page():
    slug, title = HUB, 'First T2 Return After Incorporation'
    desc = ('What a new corporation files first: the 53-week limit, Schedule '
            '24 and the year-end match. Nil first returns are ' + PRICE + '.')
    b = []
    b.append('<div class="cnf-fee"><p><strong>' + PRICE + '.</strong> '
             'A first return with no activity is a nil T2 and is filed here '
             'at the published fee.</p><p>' + OVERFLOW + '</p></div>')
    b.append('<h2>What the First Return Has That Later Ones Do Not</h2>')
    b.append('<p>Three things decide whether a first T2 is accepted, and all '
             'three are specific to the first return a corporation ever '
             'files. Every other year is simpler.</p>')
    b.append(rules_block())
    b.append('<h2>The Three Rules, Side by Side</h2>')
    b.append('<table class="cnf-tbl"><thead><tr><th scope="col">Rule</th>'
             '<th scope="col">What it means</th>'
             '<th scope="col">If it is wrong</th></tr></thead><tbody>'
             '<tr><td>The 53-week limit</td>'
             '<td>The first tax year runs from incorporation to a year-end no '
             'more than 53 weeks later</td>'
             '<td>The period is invalid and has to be split</td></tr>'
             '<tr><td>Schedule 24</td>'
             '<td>The first-time filer schedule, carried on the first return '
             'only</td>'
             '<td>The return is incomplete</td></tr>'
             '<tr><td>The year-end match</td>'
             "<td>The date on the return equals the date CRA holds</td>"
             '<td>The transmission is rejected</td></tr>'
             '</tbody></table>')
    b.append(steps_block('Fix the first year-end, which is a choice on the '
                         'first return and fixed for every year after it.'))
    b.append('<h2>By Where You Incorporated</h2>')
    b.append('<p>The federal return is the same everywhere. What differs is '
             'whether the province wants a corporate return of its own, which '
             'registry expects an annual filing, and which sales tax is added '
             'to the fee. Each page below works through one jurisdiction.</p>')
    b.append('<ul>' + ''.join(
        '<li><a href="' + START + 'what-a-new-%s-corporation-must-file/">'
        'A new %s corporation</a></li>' % (p['slug'], p['name'])
        for p in PLACES) + '</ul>')
    # No extra link here: the hub already carries nine year links plus six
    # fixed ones, and 6(g) caps a page at 15 outbound internal links.
    b.append(tail('A first year with no activity is a nil return, and that '
                  'is decided year by year rather than once.'))
    return wrap(title, 'What to File, and in What Order',
                'Your first tax year cannot exceed 53 weeks, Schedule 24 is '
                'required on the first return, and the year-end must match '
                "the Canada Revenue Agency's record.", '\n'.join(b), slug,
                desc, hub=True)


def place_page(p, idx):
    name, slug = p['name'], 'what-a-new-%s-corporation-must-file' % p['slug']
    title = 'What a New %s Corporation Must File' % name
    sep = p.get('sep')
    desc = ('What a new %s corporation files first: the T2, Schedule 24 and '
            'the 53-week limit. Nil first returns from $300.00.' % name)
    assert 70 <= len(desc) <= 160, '%s meta %d' % (slug, len(desc))

    body = []
    body.append('<div class="cnf-fee"><p><strong>' + PRICE + '.</strong> '
                'A first year with no activity is a nil T2 and is filed here '
                'at the published fee. In ' + name + ' the tax added to it is '
                + p['sales'] + '.</p><p>' + OVERFLOW + '</p></div>')
    body.append('<h2>' + p['angle'] + '</h2>')
    for para in p['paras']:
        body.append('<p>' + para + '</p>')
    _h2, _ps = SECOND[p['slug']]
    body.append('<h2>' + _h2 + '</h2>')
    for _p in _ps:
        body.append('<p>' + _p.replace('{T}', T) + '</p>')
    body.append(rules_block())
    body.append('<h2>What a New %s Corporation Owes</h2>' % name)
    rows = [
        ('Federal corporate return', 'One T2 for the first tax year'),
        ('Provincial corporate return',
         ('A separate %s return with %s' % (sep, p['body'])) if sep
         else 'None. The federal T2 settles both sides'),
        ('Schedule 24 on that first return', 'Required'),
        ('First tax year limit', 'No more than 53 weeks'),
        ('Registry annual filing', 'Owed yearly, and not a tax return'),
        ('Sales tax added to the fee', p['sales'][0].upper() + p['sales'][1:]),
        ('Fee per tax year', '$300.00 plus applicable sales tax')]
    body.append('<table class="cnf-tbl"><thead><tr><th scope="col">Item</th>'
                '<th scope="col">Position in ' + name + '</th></tr></thead>'
                '<tbody>'
                + ''.join('<tr><td>%s</td><td>%s</td></tr>' % r for r in rows)
                + '</tbody></table>')
    body.append('<p>No tax rate is quoted here. Sales tax rates change, and '
                'the figure that matters when deciding whether to file is the '
                'fee. The whole amount with tax is on the screen before you '
                'pay.</p>')
    body.append(steps_block(
        'Confirm whether %s wants a corporate return of its own, because that '
        'decides how many returns the first year needs.' % name))
    sibs = [PLACES[(idx + k) % len(PLACES)] for k in (1, 2, 3)]
    body.append('<h2>Other Jurisdictions</h2>')
    body.append('<ul><li><a href="' + START + HUB + '/">What every first T2 '
                'return needs</a></li>'
                + ''.join('<li><a href="' + START
                          + 'what-a-new-%s-corporation-must-file/">A new %s '
                            'corporation</a></li>' % (q['slug'], q['name'])
                          for q in sibs) + '</ul>')
    body.append(tail('Which jurisdictions want a corporate return of their '
                     'own is answered by the '
                     '<a href="' + T + 'provincial-return-requirement-checker/'
                     '">provincial return requirement checker</a>.'))
    return wrap(title, 'The First Return, and What Else ' + name + ' Wants',
                p['lede'], '\n'.join(body), slug, desc)


# ------------------------------------------------------------------ the gate
BANNED = ('instant filing', 'cheapest', 'lowest price', 'best price',
          'unbeatable', 'guarantee', 'guaranteed', 'risk-free', 'risk free',
          'fastest', 'no obligation', 'penalty free', 'penalty-free',
          'zero penalty', 'cra agent', 'cra approved', 'cra partner',
          'cra endorsed', 'book a call', 'calendly', 'starting from')
# 12.00 is the published Corporations Canada annual return fee, which the
# Ontario page names because federal incorporation adds that filing.
MONEY_OK = {'300.00', '350.00', '12.00'}


def gate(slug, html):
    low, bad = html.lower(), []
    # Line 1218: the two lines every page in this family must carry.
    if SCHED24 not in html:
        bad.append('line 1218: the Schedule 24 line is missing')
    if RULE53 not in html:
        bad.append('line 1218: the 53-week line is missing')
    for w in BANNED:
        if w in low:
            bad.append('banned phrase %r' % w)
    if re.search(r'\bauthorized\b', low.replace('authorized signing officer', '')):
        bad.append('rule 1 stray "authorized"')
    for m in re.finditer(r'EFILE', html):
        if not html.startswith('EFILE electronic filer', m.start()):
            bad.append('rule 1 EFILE outside the approved phrase')
            break
    if re.search(r'\bT183\b(?!CORP)', html):
        bad.append('rule 2 bare T183')
    # Line 344 and hard rule 6: steps are an ordered list, never HowTo.
    for w in ('howto', 'faqpage', 'aggregaterating', 'trustindex', '"review"'):
        if w in low:
            bad.append('rule 6 forbidden schema %r' % w)
    if '<ol' not in html:
        bad.append('line 344: steps must render as an ordered list')
    for tok in ('CO-17', 'AT1'):
        if tok in html and 'separate return' not in html:
            bad.append('rule 8: %s named without "separate return"' % tok)
    if PRICE not in html:
        bad.append('rule 9 price line missing')
    if 'plus HST' in html or 'including HST' in html:
        bad.append('rule 9: a fixed HST fee line on a jurisdiction page')
    for m in re.finditer(r'\$(\d{1,3}(?:,\d{3})*\.\d\d)', html):
        if m.group(1) not in MONEY_OK:
            bad.append('unexpected money figure $%s' % m.group(1))
    if html.count('<h1>') != 1:
        bad.append('%d H1' % html.count('<h1>'))
    if html.count('<table') != 1:
        bad.append('%d tables, needs exactly 1' % html.count('<table'))
    if 'CPA Ontario Membership 61040184' not in html:
        bad.append('no byline')
    if 'Last reviewed:' not in html:
        bad.append('no last-reviewed line')
    # Line 1532: exactly one cross-domain link, to opencorporationfor35.ca.
    x = re.findall(r'href="(https?://(?!corpnilfilingfor300\.ca)[^"]*)"', html)
    if len(x) != 1 or not x[0].startswith(OPEN):
        bad.append('line 1532: need exactly 1 cross-domain link to %s, got %r'
                   % (OPEN, x))
    links = set(re.findall(
        r'href="(https://corpnilfilingfor300\.ca[^"]*)"', html))
    if len(links) > 15:
        bad.append('%d outbound internal links, cap is 15' % len(links))
    if any(ord(c) > 0x2100 for c in html):
        bad.append('non-ASCII symbol that may be an emoji')
    json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                         html, re.S).group(1))
    if bad:
        raise AssertionError('%s GATE FAILED:\n  - %s'
                             % (slug, '\n  - '.join(bad)))
    return links


if __name__ == '__main__':
    pages = [hub_page()] + [place_page(p, i)
                            for i, p in enumerate(PLACES)]
    recs = []
    for slug, title, desc, html in pages:
        links = gate(slug, html)
        io.open(os.path.join(HERE, slug + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=slug, title=title, desc=desc,
                         url=START + slug + '/', bytes=len(html.encode())))
        print('%-42s %6d bytes  out:%2d' % (slug, len(html.encode()),
                                            len(links)))
    # Line 1532: inbound minimum 3, measured within the batch.
    for r in recs:
        n = sum(1 for o in recs
                if o['slug'] != r['slug'] and r['slug'] + '/' in
                [x for x in re.findall(r'/start/([^"/]*)/',
                 io.open(os.path.join(HERE, o['slug'] + '.html'),
                         encoding='utf-8').read())] or
                ('/start/' + r['slug'] + '/') in
                io.open(os.path.join(HERE, o['slug'] + '.html'),
                        encoding='utf-8').read())
        assert n >= 3, '%s has only %d inbound, needs 3' % (r['slug'], n)
        r['inbound'] = n
    json.dump(recs, io.open(os.path.join(HERE, 'f10-manifest.json'), 'w',
                            encoding='utf-8'), indent=1)
    print('\n%d pages, gate clear on all' % len(recs))
    for r in recs:
        print('  %-42s in:%d' % (r['slug'], r['inbound']))
