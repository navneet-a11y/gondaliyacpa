#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 14:
/compare/nil-t2-vs-ontario-annual-return-vs-federal-annual-return/

Why this page, and why it needed the template changed
-----------------------------------------------------
It is an Appendix A URL, and it is the last concept page in Family 7 that can
be built at all. Of the eight Appendix A entries still unbuilt on 2026-11-06,
six are the brand pages (Sharad Gondaliya reviews each for Rule 217, plan line
1215, and the approvals section requires approval before any goes live) and
one is /compare/voluntary-disclosure-vs-plain-late-filing/, blocked on his
ruling since the site publishes no voluntary disclosure terms.

The deviation
-------------
Plan line 1215 fixes this family at "Two published price cells and eight
published feature cells", and its publish gate reads "No comparison page
publishes without both published price columns filled". Both is two. This URL
names three filings, so it cannot be built honestly inside that contract: a
two-column table would have to fold the Ontario and federal annual returns
into one column, and the whole point of the page is that they are two
different filings to two different registries.

So build_f7.py now takes an optional col_c, and gate.py reads the expected row
width from the page's own header and allows four header cells on this slug
only. Two things were checked before that went in, and both hold:

  * all thirteen pages built before it rebuild BYTE-IDENTICAL, which this file
    asserts below rather than leaving to memory;
  * all thirteen still pass gate.py unchanged.

Logged in docs/decisions.md on 2026-11-06. Navneet asked for it to publish on
that log rather than wait, which is how every other deviation on this project
has been handled; Sharad Gondaliya's sign-off on the third column is
outstanding and the log says so.

What the price rows may and may not say
--------------------------------------
Two of the three columns are filings this service does not sell, and Navneet's
ruling of November 5, 2026 governs that case: a price cell for a route the
service does not sell states that it is not offered and carries no figure.
Both price cells on the annual return columns therefore open with "Not
offered." and hold no money at all.

The $12.00 Corporations Canada fee is published, so it does appear -- but in a
feature row, not a price row, because it is a government charge and not a
price of ours. The Ontario side carries no fee figure anywhere, because the
site publishes none: the same reason /ontario-annual-return-deadline-calculator/
was refused in Family 2 batch 12.

What this page must not claim
-----------------------------
No Ontario filing window. The annual returns guide publishes a due window for
the T2 (six months) and for the federal annual return (60 days after the
anniversary) and states only "Filed through the OBR" for Ontario. So the
"What dates it" row says the Ontario return is tied to the tax year-end rather
than to an anniversary, and names no period.

Agreeing with what is already published
---------------------------------------
From /guides/provincial-and-federal-annual-returns/ and the Family 2 tools:

  "The Ontario Business Registry is the provincial system through which the
   annual return, address changes and director changes are filed."
  "The Ontario annual return has been filed through the Ontario Business
   Registry since October 2021, and a federal corporation files a $12.00
   [Corporations Canada annual return]."
  "Enter your federal incorporation date for the annual return due date, 60
   days after the anniversary, at a $12.00 government fee."
  "A registry and the Canada Revenue Agency do not share a filing status, and
   a corporation struck for a missed annual return still owes every
   outstanding T2."
  "A missed annual return gets a corporation struck rather than charged, and
   the tax years survive it."
  "An annual return is not a tax filing, so having no income does not excuse
   it."
  "A dormant corporation confirms its directors and its registered office
   every year in exactly the way an active one does."
  "Federal incorporation does not remove the provincial obligation."
"""
import os

import build_f7
from build_f7 import check, write, PRICE, COST, T, G, DECLINE

HERE = os.path.dirname(os.path.abspath(__file__))

build_f7.TODAY, build_f7.ISO = 'November 6, 2026', '2026-11-06'

OBR = 'Ontario Business Registry'

PRICE_ROWS = [
 ('Our published fee for this filing',
  'Nil T2 filing, at ' + PRICE,
  DECLINE + ' We file the corporate tax return; this one goes through the '
  + OBR,
  DECLINE + ' We file the corporate tax return; this one goes to '
  'Corporations Canada', True),
 ('What our fee covers here',
  'The return itself, its schedules where they are required, and electronic '
  'transmission',
  DECLINE + ' Filing the T2 does not satisfy an annual return, so nothing on '
  'this column is inside the fee',
  DECLINE + ' The same applies, and federal incorporation does not remove the '
  'provincial obligation either', True),
]

FEATURE_ROWS = [
 ('Who receives it',
  'The Canada Revenue Agency',
  'The ' + OBR,
  'Corporations Canada', True),
 ('What it reports',
  'Income, which on a nil year is $0.00 across the return',
  'The registered office address, the directors and the officers',
  'The directors and the registered office', True),
 ('What dates it',
  'The fiscal year-end, with the return due within six months of it',
  'The tax year-end, rather than an anniversary. No filing window for it is '
  'published on this site',
  'The anniversary of incorporation, with 60 days to file', True),
 ('The government fee',
  'None. The only fee on this filing is ours',
  'A registry charge, which this site does not state',
  '$12.00 a year, with no HST on a government fee', True),
 ('What a missed filing produces',
  'The year stays open, invites a demand to file and an arbitrary assessment, '
  'and blocks a clearance certificate',
  'The registry record goes out of date, and after enough missed years the '
  'corporation can be struck',
  'The same exposure: the corporation can be struck from the federal register',
  True),
 ('Whether a dormant corporation still owes it',
  'Yes',
  'Yes',
  'Yes', False),
 ('Whether filing one satisfies another',
  'No',
  'No',
  'No', False),
 ('Where it sits against the fee on this site',
  'Inside nil T2 filing',
  'Outside it',
  'Outside it', True),
]

PAGE = dict(
 col_a='Nil T2 Return', col_b='Ontario Annual Return',
 col_c='Federal Annual Return',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 stamp=('The only fee of ours on this page is our own '
        '<a href="' + COST + '">published fee</a>. The $12.00 Corporations '
        'Canada charge is a government fee and sits in the table as one; the '
        'Ontario charge is not stated here because this site does not '
        'publish it.'),
 disclosure=('This comparison sets three filings against each other, one of '
             'which we file, and names no other provider. Where a comparison '
             'on this site does name one, it states that provider&rsquo;s '
             'published prices and published features only.'),
 table_note=('Six rows differ and two do not, and the two that do not are the '
             'ones most often got wrong: every one of the three is owed by a '
             'dormant corporation, and filing any one of them satisfies '
             'neither of the others. Two columns are filings we do not sell, '
             'so their price cells say so rather than carrying a figure.'),
 slug='nil-t2-vs-ontario-annual-return-vs-federal-annual-return',
 title='Nil T2 vs Ontario and Federal Annual Returns | Three Filings',
 h1='Nil T2 vs Ontario Annual Return vs Federal Annual Return',
 h1_pre='Nil T2 vs ', h1_span='Ontario and Federal Annual Returns',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='nil t2 vs annual return',
 meta=('Three filings, three recipients, and none of them satisfies the '
       'others. What the T2, the Ontario annual return and the federal '
       'annual return each report and when each is due.'),
 seo_title='Nil T2 vs Ontario and Federal Annual Returns',
 seo_desc=('Three filings to three different bodies, and filing one satisfies '
           'neither of the others. What each reports, what dates it, and '
           'which sits inside the fee.'),
 answer=('These are three separate filings to three different bodies. The T2 '
         'goes to the Canada Revenue Agency and reports income, which on a '
         'nil year is $0.00, and it is due within six months of the fiscal '
         'year-end. The Ontario annual return goes through the '
         + OBR + ' and reports the registered office and the directors. The '
         'federal annual return goes to Corporations Canada, costs $12.00 a '
         'year and is due within 60 days of the anniversary of incorporation. '
         'A dormant corporation owes each one that applies to it, and filing '
         'any one of them satisfies neither of the others.'),
 cta2=('Check Which You Owe', T + 'annual-return-vs-tax-return-checker/'),
 lead=[('Three Filings That Share a Word',
        ['<p>Two of these three are called a return and all three are called '
         'annual, which is most of the reason they are confused. They have '
         'almost nothing else in common: a different body receives each one, '
         'each reports something different, and each is dated by something '
         'different.</p>',
         '<p>The T2 is a tax return. The other two are registry filings, and '
         'an annual return is not a tax filing, so having no income does not '
         'excuse it. A corporation can be fully current on its T2 and still '
         'be struck from a register for missing one.</p>',
         '<p>Which of the two registry filings you owe depends on where the '
         'corporation is incorporated and registered, not on which you have '
         'heard of. A federally incorporated corporation operating in Ontario '
         'can owe both, because federal incorporation does not remove the '
         'provincial obligation.</p>']),
       ],
 detail=dict(
  h2='Why Filing One Does Nothing for the Others',
  intro=('A registry and the Canada Revenue Agency keep separate records and '
         'neither reports a filing status to the other. Everything below '
         'follows from that:'),
  items=[
   'A corporation can be in good standing at its registry while owing ten '
   'years of T2 returns, and it can be current on every T2 and still be '
   'struck from the register.',
   'The T2 is due within six months of the fiscal year-end. The federal '
   'annual return is due within 60 days of the anniversary of incorporation, '
   'at a $12.00 government fee. Those are two unrelated dates, and a '
   'corporation that files on one of them has not answered the other.',
   'Until 2021 the Ontario annual return travelled with the T2, which is why '
   'so many owners still expect the T2 to carry it. Since October 2021 it has '
   'been filed through the ' + OBR + ' instead, and nothing in the corporate '
   'tax return now prompts anyone to file it.',
   'A missed annual return gets a corporation struck rather than charged. A '
   'missed T2 leaves the tax year open, invites a demand to file and an '
   'arbitrary assessment, and blocks a clearance certificate. Two different '
   'consequences with two different cures.',
   'Being struck settles nothing on the tax side: the tax years survive it, '
   'and the outstanding returns are still outstanding.',
   'A dormant corporation confirms its directors and its registered office '
   'every year in exactly the way an active one does, so none of the three '
   'goes away for want of activity.',
  ],
  warn=('Only one of the three is inside the fee on this site. Nil T2 filing '
        'at ' + PRICE + ' covers the corporate tax return. Neither annual '
        'return is a filing we make, and neither is covered, which the two '
        'price rows above state rather than price.'),
  close=''),
 band=('Which of the Three You Owe Is a Short Question',
       'The checker sets the annual return against the tax return and names '
       'which of them a given corporation still owes.'),
 cards=[('Reviewed by a CPA',
         'Each return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('What the fee covers',
         'The T2 itself, GIFI Schedules 100, 125 and 141 where required, '
         'Schedule 50, Schedule 24 on a first return, Schedule 8 and loss '
         'continuity, and electronic transmission.'),
        ('What sits outside it',
         'The Ontario annual return, the federal annual return, '
         'extra-provincial registrations, and closing a GST/HST or payroll '
         'account with Form RC145.')],
 case=('A corporation incorporated federally in 2019, registered in Ontario, '
       'dormant since 2021',
       'It owes three separate things for each year since. A T2 for every '
       'tax year, each at ' + PRICE + ', due within six months of its '
       'year-end and still owed however quiet the year was. A federal annual '
       'return for each year, $12.00 each, due within 60 days of the 2019 '
       'anniversary date. And an Ontario annual return for each tax year, '
       'through the ' + OBR + ', because registering in Ontario brought that '
       'obligation and federal incorporation did not remove it. Filing the '
       'T2 returns clears the first column only: the corporation can come '
       'fully current with the Canada Revenue Agency and still be struck off '
       'by either registry. The figures here illustrate how the rules apply '
       'and are not drawn from a client file.'),
 faq=[
  ('Is the annual return the same as the T2?',
   'No. The T2 is a tax return filed with the Canada Revenue Agency. An '
   'annual return is a registry filing that confirms the registered office '
   'and the directors, and it reports no income at all.'),
  ('Does filing my T2 cover the annual return?',
   'No, and not since 2021 for Ontario. The two go to different bodies and '
   'neither carries anything to the other.'),
  ('Do I owe both annual returns, or one?',
   'It depends where the corporation is incorporated and registered. A '
   'federal corporation registered in Ontario can owe both, because federal '
   'incorporation does not remove the provincial obligation.'),
  ('What does the federal annual return cost?',
   '$12.00 a year, with no HST on a government fee. It is due within 60 days '
   'of the anniversary of incorporation.'),
  ('What does the Ontario annual return cost?',
   'This site does not publish a figure for it, so this page does not state '
   'one. The ' + OBR + ' is where the filing is made and what it charges is a '
   'question for the registry.'),
  ('When is the Ontario annual return due?',
   'It is tied to the tax year-end rather than to an anniversary. No filing '
   'window for it is published on this site, so this page gives none.'),
  ('My corporation is dormant. Do I still owe all three?',
   'Each one that applies to it, yes. A dormant corporation confirms its '
   'directors and its registered office every year in exactly the way an '
   'active one does.'),
  ('What happens if I miss an annual return?',
   'The registry record goes out of date and, after enough missed years, the '
   'corporation can be struck. That is a different consequence from a missed '
   'T2, and it has a different cure.'),
  ('What happens if I miss the T2?',
   'The year stays open, invites a demand to file and an arbitrary '
   'assessment, and blocks a clearance certificate until it is filed.'),
  ('My corporation was struck off. Are the tax years gone?',
   'No. Being struck settles nothing on the tax side: the open years survive '
   'it, and every outstanding return is still outstanding.'),
  ('Can I be current with one body and behind with the other?',
   'Easily, and it is common. A registry and the Canada Revenue Agency do not '
   'share a filing status, so being current in one place proves nothing about '
   'the other.'),
  ('Why did the Ontario filing change?',
   'Until 2021 it travelled with the T2. Since October 2021 it has gone '
   'through the ' + OBR + ' separately, and nothing in the corporate tax '
   'return prompts an owner to file it any more.'),
  ('Which of the three do you file?',
   'The T2, at ' + PRICE + '. Neither annual return is a filing we make, and '
   'neither is covered by the fee.'),
  ('How many annual returns am I behind on?',
   'One falls due for each tax year since the last one filed. The '
   '<a href="' + T + 'ontario-missed-annual-returns-calculator/">Ontario '
   'missed annual returns calculator</a> counts the Ontario side, and the '
   '<a href="' + T + 'federal-annual-return-anniversary-calculator/">federal '
   'annual return anniversary calculator</a> dates the federal one.'),
  ('Where is all of this set out in full?',
   'In the guide to <a href="' + G + 'provincial-and-federal-annual-returns/">'
   'provincial and federal annual returns</a>, which covers the Ontario '
   'Business Registry, the $12.00 federal annual return, and where the '
   'Alberta AT1 and Quebec CO-17 sit.'),
 ],
)

# ---- the deviation, asserted rather than trusted -------------------------
# A third column is a change to a template thirteen live pages share. The
# guard is not a comment: every one of those thirteen is rebuilt and compared
# byte for byte before this page is written, so a change that disturbs them
# fails here instead of going live.
_THIS = PAGE['slug'] + '.html'
_OTHERS = sorted(f for f in os.listdir(HERE)
                 if f.endswith('.html') and f != _THIS)
assert len(_OTHERS) >= 13, (
    'expected at least the 13 comparison pages built before this one, found %d'
    % len(_OTHERS))

assert PAGE['col_c'], 'this page is the three-way; it needs col_c'
assert len(PAGE['price_rows'][0]) == 5, 'three columns means five-field rows'
for _row in PRICE_ROWS:
    for _cell in _row[1:-1]:
        if _cell.startswith(DECLINE):
            assert '$' not in _cell, (
                'the November 5 ruling: %r carries a figure' % _cell[:60])
# The Ontario column states no fee and no filing window anywhere on the page.
_ONT = ' '.join(r[2] for r in PRICE_ROWS + FEATURE_ROWS)
assert '$' not in _ONT, (
    'the Ontario column carries a figure, and this site publishes none: %r'
    % _ONT[:80])

if __name__ == '__main__':
    import filecmp
    import shutil
    import subprocess
    import tempfile

    tmp = tempfile.mkdtemp()
    for _f in _OTHERS:
        shutil.copy(os.path.join(HERE, _f), os.path.join(tmp, _f))
    for _b in sorted(f for f in os.listdir(HERE)
                     if f.startswith('build_f7') and f.endswith('.py')
                     and f != 'build_f7n.py'):
        subprocess.run(['python3', os.path.join(HERE, _b)], cwd=HERE,
                       capture_output=True)
    _moved = [f for f in _OTHERS
              if not filecmp.cmp(os.path.join(HERE, f), os.path.join(tmp, f),
                                 shallow=False)]
    shutil.rmtree(tmp)
    assert not _moved, (
        'the third column changed %d page(s) that must be byte-identical: %s'
        % (len(_moved), _moved))
    print('the %d earlier comparison pages are byte-identical' % len(_OTHERS))

    check(PAGE)
    write(PAGE, 'f7n-manifest.json')
