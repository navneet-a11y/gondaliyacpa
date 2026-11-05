#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 8: /compare/paper-t2-vs-efile-t2/

Why this page
-------------
Appendix A line 3286 lists it, the family table at line 1145 names it as one of
its five worked examples, and the keyword table at line 1242 carries "paper t2
vs efile t2". It is the last F7 URL that needs nothing from anyone: the plan
states both figures the comparison turns on, so no competitor price and no
ruling is required.

The slug and the H1 disagree, deliberately
------------------------------------------
Appendix A says /paper-t2-vs-efile-t2/ and the slug is kept, because that is
the URL the plan published. The H1 reads "Electronic Filing" rather than
"EFILE", because hard rule 1 reserves that word for the phrase "registered
EFILE electronic filer" and using it as a shorthand is the thing the rule
exists to stop. The live mandatory-t2-efile-checker made the same split on the
same reasoning: visible wording "E-Filing", slug keeps efile.

The price column, which is the reason the other twelve pages are blocked
------------------------------------------------------------------------
Line 1215 wants two filled price cells and no negative claim. The left column
here is a route this service does not sell, so there is no fee of ours to put
in it. The plan settles it at line 169: "We file electronically only." That is
a statement about this firm, not a price for someone else, so the cell is
filled truthfully and nothing is claimed about any provider.

The second price row carries what the route itself costs, which is where the
plan's two figures go. That is not a fee anyone charges us or we charge anyone,
and it is the only honest way to fill a price row for a route we do not sell.
The twelve remaining F7 URLs do not have a plan sentence to lean on, which is
exactly why they still wait on a ruling.

Both money figures together, never one alone
--------------------------------------------
Line 1819, QA item 9: "Paper penalties are stated as $1,000 plus a $100
per-return preparer penalty." Line 393 and line 1755 say the same. gate.py now
refuses a page carrying one figure without the other, so the pairing cannot be
broken by a later edit. Both were added to gate.py's money allowlist with the
plan line that states them; nothing went in because this page wanted it.

Agreeing with what is already published
---------------------------------------
From /guides/mandatory-t2-electronic-filing/:

  "For tax years beginning after 2023, electronic filing of the T2 is
   mandatory for virtually all corporations. It is not a preference and it is
   not limited to large corporations."
  "The change removed a threshold that had previously exempted smaller
   corporations from mandatory electronic filing."
  "The rule is about the method, not the content. A return with nothing in it
   is transmitted electronically exactly as a return with everything in it."
  "a paper T2 draws a flat $1,000.00, and a flat amount does not care that the
   corporation owes $0.00"
  "A separate charge of $100.00 per return applies to a preparer who files a
   corporate return on paper where electronic filing was required."
  "It attaches to the person who prepared and filed the return, not to the
   corporation."
  "Returns here are transmitted electronically by a registered EFILE
   electronic filer, so neither charge arises."
  "Being dormant is not an exception, having no bank account is not an
   exception, and finding the software inconvenient is not an exception."
  "An insurer, a non-resident corporation in certain circumstances and a
   corporation reporting in a functional currency are the kinds of case
   involved."
  "The return is prepared in certified software, validated against the
   Agency's rules, and transmitted directly. There is no envelope, no posting
   date and no question about whether it arrived."
  "Earlier tax years are transmitted electronically too."
  "One corrected transmission is included in the fee where the Agency rejects
   the first one."

What is not on this page
------------------------
The late-filing qualification block is not here. The guide uses it to contrast
a percentage charge with a flat one, but reproducing it would put $25.00 and
$2,500.00 on an F7 page to make a point this page does not need, and the
comparison is paper against electronic, not late against on time. The flat
nature of the charge is stated directly instead.
"""
import build_f7
from build_f7 import T, G, COST, PRICE, check, write

build_f7.TODAY, build_f7.ISO = 'November 5, 2026', '2026-11-05'

PRICE_ROWS = [
 ('Our published fee for a quiet year',
  'Not offered. We file electronically only', PRICE, True),
 ('What the filing route itself can cost',
  'A flat $1,000.00, plus a separate $100.00 per-return charge on the '
  'preparer',
  'Nothing. Neither charge arises', True),
]

FEATURE_ROWS = [
 ('Available for a tax year beginning after 2023',
  'No for virtually all corporations. The threshold that had exempted '
  'smaller corporations was removed',
  'Yes, and mandatory rather than a preference', True),
 ('Whether having no activity changes that',
  'No. Being dormant is not an exception, and neither is having no bank '
  'account',
  'No. A return with nothing in it is transmitted exactly as a return with '
  'everything in it', True),
 ('What the $1,000.00 charge depends on',
  'Nothing about the figures. It is flat, so a return reporting $0.00 is '
  'exposed to all of it',
  'It does not arise', True),
 ('Who the per-return charge attaches to',
  'The preparer who filed on paper where electronic filing was required, not '
  'the corporation',
  'Nobody. The return is transmitted by a registered EFILE electronic filer',
  True),
 ('The narrow exceptions to the rule',
  'An insurer, a non-resident corporation in certain circumstances and a '
  'corporation reporting in a functional currency',
  'Everything else, which is every corporation this site files for', True),
 ('What checks the return before it goes',
  'Nothing checks it before it is posted',
  'Prepared in certified software and validated against the Agency&rsquo;s '
  'rules before transmission', True),
 ('When a transmission is refused',
  'Does not apply, because there is no transmission',
  'An error naming what it would not accept. One corrected transmission is '
  'included in the fee', True),
 ('Evidence the return arrived',
  'An envelope and a posting date',
  'A confirmation from the Canada Revenue Agency, emailed within 3 business '
  'days', True),
]

PAGE = dict(
 col_a='Paper T2', col_b='Electronic T2',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 stamp=('Our own <a href="' + COST + '">published fee</a> is for electronic '
        'filing. We file electronically only, so the left column carries no '
        'fee of ours.'),
 disclosure=('This comparison sets the filing route the rules require against '
             'the one it replaced, and names no other provider. Where a '
             'comparison on this site does name one, it states that '
             'provider&rsquo;s published prices and published features '
             'only.'),
 table_note=('Every row differs, which is the point: the two routes are not '
             'two ways of doing the same thing. For a tax year beginning '
             'after 2023 one of them is what the rules require and the other '
             'carries a flat charge that does not depend on how little the '
             'corporation did.'),
 slug='paper-t2-vs-efile-t2',
 title='Paper T2 vs Electronic Filing | What the Rules Require',
 h1='Paper T2 vs Electronic Filing',
 h1_pre='Paper T2 vs ', h1_span='Electronic Filing',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='paper t2 vs efile t2',
 meta=('For tax years beginning after 2023 electronic filing is mandatory for '
       'virtually all corporations. A paper T2 draws a flat $1,000.00 plus a '
       '$100.00 per-return charge on the preparer.'),
 seo_title='Paper T2 vs Electronic Filing | The Rule',
 seo_desc=('Electronic filing is mandatory for tax years beginning after '
           '2023. What a paper T2 costs, who the preparer charge attaches '
           'to, and the narrow exceptions.'),
 answer=('Electronic filing is what the rules require. For tax years '
         'beginning after 2023 it is mandatory for virtually all '
         'corporations, it is not a preference, and it is not limited to '
         'large corporations. A paper T2 draws a flat $1,000.00, plus a '
         'separate $100.00 per-return charge on the preparer who filed it. '
         'The flat amount does not depend on how much tax is owing, so a '
         'return reporting $0.00 is exposed to all of it. We file '
         'electronically only, at ' + PRICE + ', with the CRA confirmation '
         'emailed within 3 business days.'),
 cta2=('Check the Rule for Your Year', T + 'mandatory-t2-efile-checker/'),
 lead=[('The Rule Is About the Method, Not the Content',
        ['<p>For tax years beginning after 2023, electronic filing of the T2 '
         'is mandatory for virtually all corporations. The change removed a '
         'threshold that had previously exempted smaller corporations, so the '
         'obligation now reaches almost every corporation that files a T2 at '
         'all.</p>',
         '<p>It says nothing about what the return contains. A return with '
         'nothing in it is transmitted electronically exactly as a return '
         'with everything in it, which is why a dormant corporation is not '
         'outside the rule and never was.</p>',
         '<p>That catches people out in a particular way. Posting a return '
         'feels like the careful option, and on a quiet year it is the '
         'expensive one: a flat charge does not get smaller because the '
         'corporation did less.</p>']),
       ],
 detail=dict(
  h2='What the Paper Route Costs on a Quiet Year',
  intro=('The charge for filing on paper behaves differently from anything '
         'else a corporation with no activity can be charged:'),
  items=[
   'A paper T2 draws a flat $1,000.00, and a flat amount does not depend on '
   'how much tax the corporation owes.',
   'A separate $100.00 per-return charge applies to a preparer who files a '
   'corporate return on paper where electronic filing was required.',
   'That per-return charge attaches to the person who prepared and filed the '
   'return, not to the corporation.',
   'Nothing about having no activity removes the obligation or the charge for '
   'ignoring it.',
   'Being dormant is not an exception, having no bank account is not an '
   'exception, and finding the software inconvenient is not an exception.',
   'Earlier tax years are transmitted electronically too, so catching up on '
   'six unfiled years does not mean posting six paper returns.',
   'Returns here are transmitted electronically by a registered EFILE '
   'electronic filer, so neither charge arises.',
  ],
  warn=('A dormant corporation that posts a paper T2 is exposed to the full '
        '$1,000.00 on a return reporting $0.00. It is the largest single '
        'amount a genuinely nil corporation can be charged, and it is the '
        'one it can incur by being careful in the wrong way.'),
  close=('The <a href="' + T + 'mandatory-t2-efile-checker/">mandatory T2 '
         'e-filing checker</a> tests the rule against your own tax year, the '
         '<a href="' + T + 'efile-rejection-reason-checker/">e-filing '
         'rejection reason checker</a> takes a refused transmission, and the '
         '<a href="' + G + 'mandatory-t2-electronic-filing/">complete guide '
         'to mandatory T2 electronic filing</a> sets out both charges in '
         'full.')),
 band=('Transmitted, Not Posted',
       'Every return here is prepared in certified software and transmitted '
       'by a registered EFILE electronic filer, at ' + PRICE + '.'),
 cards=[('Reviewed by a CPA',
         'The return is prepared and reviewed by a CPA Ontario member before '
         'anything is transmitted.'),
        ('Validated before it is sent',
         'Prepared in certified software and validated against the '
         'Agency&rsquo;s rules, so there is no envelope, no posting date and '
         'no question about whether it arrived.'),
        ('One corrected transmission',
         'Where the Canada Revenue Agency refuses the first transmission, one '
         'corrected transmission is included in the fee.')],
 case=('A dormant corporation posting its own T2 for a quiet year',
       'The return reports $0.00 throughout the income statement, and the '
       'directors treat posting it as the cautious choice. For a tax year '
       'beginning after 2023 it is not: electronic filing is mandatory for '
       'virtually all corporations, a paper T2 draws a flat $1,000.00, and a '
       'separate $100.00 per-return charge attaches to whoever prepared and '
       'filed it. Because the $1,000.00 is flat it does not depend on tax '
       'owing, so a return reporting $0.00 is exposed to all of it. The same '
       'return transmitted electronically is ' + PRICE + ', with Form '
       'T183CORP signed by an authorized signing officer beforehand and the '
       'CRA confirmation emailed within 3 business days. The figures here '
       'illustrate how the rules apply and are not drawn from a client '
       'file.'),
 faq=[
  ('Is electronic filing of the T2 mandatory?',
   'For tax years beginning after 2023 it is mandatory for virtually all '
   'corporations. The earlier threshold that exempted smaller corporations '
   'was removed.'),
  ('What does filing a paper T2 cost?',
   'A flat $1,000.00, plus a separate $100.00 per-return charge on the '
   'preparer. Neither is a percentage of anything.'),
  ('Does a nil return escape that?',
   'No. The amount is flat, so a dormant corporation that posts a paper '
   'return reporting $0.00 is exposed to the full $1,000.00.'),
  ('Who pays the $100.00 per-return charge?',
   'The preparer who filed a corporate return on paper where electronic '
   'filing was required. It attaches to that person, not to the '
   'corporation.'),
  ('Can I file on paper through this service?',
   'No. We file electronically only. Every return is transmitted by a '
   'registered EFILE electronic filer.'),
  ('Does the rule depend on what is in the return?',
   'No. It is about the method, not the content. A return with nothing in it '
   'is transmitted exactly as a return with everything in it.'),
  ('Is being dormant an exception?',
   'No. Being dormant is not an exception, having no bank account is not an '
   'exception, and finding the software inconvenient is not an exception.'),
  ('What are the real exceptions?',
   'A small number of cases defined by what the corporation is: an insurer, a '
   'non-resident corporation in certain circumstances and a corporation '
   'reporting in a functional currency.'),
  ('Can older unfiled years be filed electronically?',
   'Yes. Earlier tax years go through the same channel, prepared oldest '
   'first, each on its own form for its own tax year at ' + PRICE + '.'),
  ('How do I know an electronic return arrived?',
   'A confirmation from the Canada Revenue Agency, emailed within 3 business '
   'days of transmission. There is no envelope and no posting date to argue '
   'about.'),
  ('What happens if the transmission is refused?',
   'A refused transmission is not a filed return. The Agency names what it '
   'would not accept, the return is corrected and sent again, and one '
   'corrected transmission is included in the fee.'),
  ('Is anything checked before the return is sent?',
   'Yes. It is prepared in certified software and validated against the '
   'Agency&rsquo;s rules before it is transmitted.'),
  ('Does Form T183CORP change because the return is electronic?',
   'Form T183CORP is what makes an electronic transmission possible. It is '
   'signed by an authorized signing officer before anything is sent, and it '
   'is kept for six years.'),
  ('Does electronic filing cost more than posting a return?',
   'The fee here is ' + PRICE + ' whichever way you look at it, and the paper '
   'route carries a flat $1,000.00 plus the $100.00 per-return charge on the '
   'preparer.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'mandatory-t2-efile-checker/">mandatory T2 e-filing '
   'checker</a>, which tests the rule against the first day of your tax '
   'year.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7h-manifest.json')
