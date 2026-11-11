#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 5, the one Appendix A answer slug that is genuinely missing.

Appendix A names three /answers/ slugs. Family 5 is 45 of 45 by count, but it
reached that number with 45 different questions and NONE of the three named
slugs is live. Checked against the full live roster:

  does-an-inactive-corporation-have-to-file-a-t2
      Covered. ID 928 "Do I Need to File a T2 Every Year if My Corporation Is
      Inactive?" is the same question, and ID 858 "Do I Need to File a T2 if
      My Corporation Had No Activity?" overlaps it. Building it would
      cannibalise 928, which 6(k)'s internal rule forbids. NOT BUILT.

  how-many-unfiled-t2-years-can-i-file-at-once
      Covered. ID 2119 "How Many Years of Unfiled T2 Returns Can I Catch Up?"
      is the same question, and ID 929 "Can I File Five Years of Nil T2
      Returns at Once?" overlaps it. NOT BUILT.

  can-i-e-sign-a-t183corp
      NOT covered. Nothing in the 45 asks about signing, e-signing or Form
      T183CORP at all. This is a real gap in a family that reads complete,
      and it is the subject of a pillar guide (955) with no answer page
      feeding it. BUILT HERE.

This takes Family 5 to 46 against a planned 45. That is deliberate: the slug
is one Appendix A names and the family's count was met by substitutes. The
over-count is logged rather than resolved by dropping one of the live 45,
which is Sharad Gondaliya's call.

SOURCING
--------
The facts here were checked against the Canada Revenue Agency rather than
written from memory, because the whole page is a statement about what the
Canada Revenue Agency accepts:

  - It accepts an electronic signature on Form T183CORP, per its own
    electronic-signatures page, and the T2 guide dates that to June 22, 2023.
  - The form is not sent to the Canada Revenue Agency. It is kept and
    produced on request.
  - A signing officer of the corporation signs it where someone else
    transmits the return.
  - It is kept at least six years after filing, and the certificate of
    completion is kept with an electronically signed copy.
  - The acceptance is an ADMINISTRATIVE measure. The 2021 budget measure was
    not enacted, so the Canada Revenue Agency extended its administrative
    position and is still pursuing a permanent one, which needs legislation.

That last point is the reason this page is worth having rather than a line in
the guide. A reader deciding whether to sign electronically should know the
position is settled for filing today and is not entrenched in law.

A note on the Family 5 gate: it bans the bare word "authorized", with no
carve-out of the kind build_f8_cost.py has. So this page says "a signing
officer of the corporation", never "an authorized signing officer". That is
also the Canada Revenue Agency's own phrasing.
"""
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
A = SITE + '/answers/'
# rstrip: the prefix file ends with the newline before the hero. The
# '\n'.join below supplies that newline itself, so keeping both would put
# a blank line where the live pages have none and desync the byte counts.
PREFIX = io.open(os.path.join(HERE, '_f5_prefix.txt'),
                 encoding='utf-8').read().rstrip('\n')
TODAY = 'November 11, 2026'
SLUG = 'can-i-e-sign-a-t183corp'
Q = 'Can I E-Sign a T183CORP?'
URL = A + SLUG + '/'

ANSWER = ('Yes. The Canada Revenue Agency accepts an electronic signature on '
          'Form T183CORP, and has done since June 22, 2023. A signing officer '
          'of the corporation signs it before the return is transmitted. The '
          'form is never sent to the Canada Revenue Agency; your filer keeps '
          'it and produces it on request.')

RELATED = [
    ('how-do-i-file-a-nil-t2-return-in-canada', 'How do I file a nil T2'),
    ('can-i-file-a-nil-t2-myself-without-an-accountant',
     'Can I file it myself'),
    ('do-i-need-a-business-number-to-file-a-nil-t2',
     'Do I need a business number'),
    ('do-i-need-financial-statements-for-a-nil-t2-return',
     'Do I need financial statements'),
    ('how-long-does-it-take-to-file-a-nil-t2-return',
     'How long does filing take'),
    ('how-long-does-cra-take-to-assess-a-nil-t2-return',
     'How long does CRA take to assess'),
]


def build():
    b = [PREFIX]
    b.append('<div class="cnf-hero"><div class="cnf-hero-in"><h1>' + Q
             + '</h1><p class="cnf-hero-sub">$300.00 Plus HST Per Tax Year'
             '</p><p class="cnf-hero-lede">We are a registered EFILE '
             'electronic filer. Your return is transmitted to the Canada '
             'Revenue Agency electronically.</p><p class="cnf-hero-by">'
             'Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
             'CPA Ontario Membership 61040184.</p><p>'
             '<a class="cnf-hero-btn" href="' + SITE + '/form/">'
             'Start Nil T2 Filing NOW</a></p></div></div>')
    b.append('<div class="cnf-w">')
    b.append('<div class="cnf-meta"><nav class="cnf-crumb" '
             'aria-label="Breadcrumb"><a href="' + SITE + '/">Nil T2 filing '
             'in Canada</a> &rsaquo; <span aria-current="page">' + Q
             + '</span></nav></div>')
    b.append('')
    b.append('<p class="cnf-answer">' + ANSWER + '</p>')
    b.append('<h2>' + Q + '</h2>')
    b.append('<table class="cnf-tbl"><thead><tr><th scope="col">Point</th>'
             '<th scope="col">Position</th></tr></thead><tbody>')
    for k, v in [
            ('Electronic signature on Form T183CORP', 'Accepted'),
            ('Accepted since', 'June 22, 2023'),
            ('Who signs', 'A signing officer of the corporation'),
            ('Sent to the Canada Revenue Agency',
             'No. Your filer keeps it and produces it on request'),
            ('How long the signed form is kept',
             'At least six years after filing'),
            ('What the acceptance rests on',
             'An administrative measure, not enacted legislation'),
            ('Fee to file', '$300.00 plus HST per tax year')]:
        b.append('<tr><td>' + k + '</td><td>' + v + '</td></tr>')
    b.append('</tbody></table>')
    b.append('<p>Form T183CORP is the authorization a corporation gives '
             'before someone else transmits its T2 return. Without a signed '
             'T183CORP the return is not transmitted, which makes it the '
             'last step before filing rather than paperwork that follows '
             'it.</p>')

    b.append('<h2>What the Acceptance Rests On</h2>')
    b.append('<p>This is the part worth knowing. The Canada Revenue '
             'Agency&rsquo;s acceptance of an electronic signature on Form '
             'T183CORP is an administrative measure rather than enacted law. '
             'The measure proposed in the 2021 budget was not passed, so the '
             'Canada Revenue Agency extended its administrative position '
             'instead, and it is still pursuing a permanent one. Making it '
             'permanent needs a change in the legislation.</p>')
    b.append('<p>In practice the position is settled for filing today. It is '
             'worth re-checking rather than assuming it is fixed, which is '
             'what the last-reviewed date at the foot of this page is '
             'for.</p>')

    b.append('<h2>What Signing Electronically Does Not Change</h2>')
    b.append('<p><strong>Who may sign.</strong> A signing officer of the '
             'corporation signs Form T183CORP. An electronic signature does '
             'not widen that to anyone else, and it does not let the person '
             'transmitting the return sign on the corporation&rsquo;s '
             'behalf.</p>')
    b.append('<p><strong>Where the form goes.</strong> Nowhere. It is not '
             'filed with the return and it is not sent to the Canada Revenue '
             'Agency separately. It is kept, and produced if the Canada '
             'Revenue Agency asks for it later.</p>')
    b.append('<p><strong>How long it is kept.</strong> At least six years '
             'after filing. Where the signature is electronic, the '
             'certificate of completion is kept with it, which matters most '
             'when the form itself does not show a timestamp.</p>')

    b.append('<h2>Filing a Nil Return</h2>')
    b.append('<p>This service is for a corporation with no activity in the '
             'tax year. A corporation with investment income, rental income, '
             'or dividends paid or received is not nil.</p>')
    b.append('<p>We are a registered EFILE electronic filer. Your return is '
             'transmitted to the Canada Revenue Agency electronically, and '
             'your CRA confirmation is emailed within 3 business days. You '
             'sign Form T183CORP on a secure single-use screen before we '
             'transmit. The fee is $300.00 plus HST per tax year. See the '
             'full <a href="' + SITE + '/pricing/nil-t2-filing-cost/">nil T2 '
             'filing cost</a> and what it covers.</p>')
    b.append('<p>For the whole subject in one place, see the guide to '
             '<a href="' + SITE + '/guides/t183corp-signing-and-transmission/'
             '">Form T183CORP signing and transmission</a>.</p>')

    b.append('<h2>Related Questions</h2>')
    b.append('<ul>' + '\n'.join(
        '<li><a href="' + A + s + '/">' + t + '</a></li>'
        for s, t in RELATED) + '</ul>')
    b.append('<p><a class="cnf-btn" href="' + SITE + '/form/">'
             'Start Nil T2 Filing NOW</a></p>')
    b.append('<p class="cnf-updated">Last reviewed: ' + TODAY + '</p>')
    b.append('</div>')
    g = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': URL + '#webpage', 'url': URL,
         'name': Q, 'description': ANSWER, 'inLanguage': 'en-CA',
         'dateModified': '2026-11-11',
         'author': {'@type': 'Person', 'name': 'Sharad Gondaliya',
                    'honorificSuffix': 'CPA',
                    'url': SITE + '/sharad-gondaliya-cpa/'}},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1,
             'name': 'Nil T2 filing in Canada', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': Q, 'item': URL}]}]}
    b.append('<script type="application/ld+json">'
             + json.dumps(g, separators=(', ', ': ')) + '</script>')
    return '\n'.join(b)


# The Family 5 gate from gate.py, applied to this one page.
BANNED = ['cheapest', 'lowest price', 'best price', 'unbeatable', 'guarantee',
          'guaranteed', 'risk-free', 'risk free', 'fastest', 'instant filing',
          'no obligation', 'penalty free', 'penalty-free', 'zero penalty',
          'authorized', 'authorised', 'cra agent', 'cra approved',
          'cra partner', 'cra endorsed', 'book a call', 'calendly',
          'starting from']
QUAL_HEAD = 'A true nil return carries no percentage late-filing penalty'


def gate(c):
    low, fail = c.lower(), []
    n = len(ANSWER.split())
    if not 40 <= n <= 60:
        fail.append('answer is %d words, needs 40-60' % n)
    if c.count(ANSWER) < 2:
        fail.append('answer not reused as meta description')
    if re.search(r'T183(?!CORP)', c):
        fail.append('bare T183')
    if 'penalty' in low.replace(
            'can-i-file-a-nil-t2-late-without-a-penalty', '') \
            and QUAL_HEAD not in c:
        fail.append('penalty mentioned without the 7.4 qualification block')
    if 'registered EFILE electronic filer' not in c:
        fail.append('missing the approved EFILE sentence')
    for b in BANNED:
        if b in low:
            fail.append('banned phrase "%s"' % b)
    for bad in ['FAQPage', 'HowTo', 'aggregateRating', '"Review"']:
        if bad in c:
            fail.append('banned schema %s' % bad)
    if '$300.00 plus HST per tax year' not in c:
        fail.append('price line missing')
    if 'including HST' in c:
        fail.append('"including HST" contradicts the standing correction')
    if c.count('<h1>') != 1:
        fail.append('%d H1' % c.count('<h1>'))
    if c.count('<table') != 1:
        fail.append('%d tables, needs exactly 1' % c.count('<table'))
    if '<h2>' not in c:
        fail.append('no H2')
    if 'CPA Ontario Membership 61040184' not in c:
        fail.append('no byline')
    if 'Last reviewed:' not in c:
        fail.append('no last-reviewed line')
    links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', c))
    if len(links) > 15:
        fail.append('%d outbound links, cap is 15' % len(links))
    if any(ord(ch) > 0x2100 for ch in c):
        fail.append('non-ASCII symbol that may be an emoji')
    json.loads(re.search(
        r'<script type="application/ld\+json">(.*?)</script>', c, re.S).group(1))
    if fail:
        raise AssertionError('GATE FAILED:\n  - ' + '\n  - '.join(fail))
    return links


if __name__ == '__main__':
    html = build()
    links = gate(html)
    io.open(os.path.join(HERE, SLUG + '.html'), 'w',
            encoding='utf-8').write(html)
    print('%s\n  %d bytes, body from %d, %d outbound links\n  %s'
          % (SLUG, len(html.encode()), len(PREFIX.encode()) + 1,
             len(links), URL))
    print('  answer %d words' % len(ANSWER.split()))
    print('\ngate clear')
