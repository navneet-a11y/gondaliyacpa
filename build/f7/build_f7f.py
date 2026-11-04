#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 6: /compare/federal-corporation-vs-ontario-corporation-nil-filing/

Why this page
-------------
Same line 1215 test: both columns are our own fee, because the T2 is the same
federal return for either corporation. What differs is the registry and the
annual return, which is exactly the confusion the page exists to clear up.

Agreeing with what is already published
---------------------------------------
From /guides/provincial-and-federal-annual-returns/:

  "Filing the T2 does not satisfy an annual return, and filing an annual
   return does not satisfy the T2. A corporation needs both, every year, for
   as long as it exists."
  "An Ontario corporation files an annual return confirming its registered
   office address, its directors and its officers. It carries no tax and no
   payment. Until 2021 this was filed alongside the T2. Since October 2021 it
   is filed through the Ontario Business Registry."
  "A federally incorporated corporation operating in Ontario files both: the
   Corporations Canada annual return and an Ontario filing. Federal
   incorporation does not remove the provincial obligation."

From /guides/quebec-co17-and-alberta-at1/:

  "The test is a permanent establishment in the province, not where the
   corporation was incorporated and not where the director happens to live."
  CO-17 and AT1 "are not part of the federal T2 and are not covered by the
   fee." (hard rule 8)

The Corporations Canada fee is NOT on this page
-----------------------------------------------
The annual returns guide states that fee as a dollar figure. It cannot be
repeated here: gate.py allows only $300.00 and $350.00 anywhere on an F7
page. That allowlist exists so a stray price cannot appear on a comparison
page, and widening it so this page can say what I want it to say would be
exactly the wrong way round. The page says the fee is set by Corporations
Canada and links to the guide that carries the figure.
"""
from build_f7 import T, G, COST, PRICE, check, write

PRICE_ROWS = [
 ('Our published fee for a quiet year', PRICE, PRICE, True),
 ('A second quiet tax year', PRICE, PRICE, True),
]

FEATURE_ROWS = [
 ('Where it is incorporated',
  'Under federal law, with Corporations Canada',
  'Under Ontario law, on the Ontario Business Registry', True),
 ('The annual return it owes',
  'A Corporations Canada annual return, at the fee that registry sets',
  'An Ontario annual return, which carries no tax and no payment', True),
 ('Where that annual return is filed',
  'With Corporations Canada',
  'Through the Ontario Business Registry, where it has gone since October '
  '2021', True),
 ('Operating in Ontario',
  'Files both: the Corporations Canada annual return and an Ontario filing. '
  'Federal incorporation does not remove the provincial obligation',
  'Files the Ontario annual return', True),
 ('The T2 itself',
  'The same federal return',
  'The same federal return', False),
 ('Is the annual return covered by this fee',
  'No. It is a registry filing, and filing the T2 does not satisfy it',
  'No. It is a registry filing, and filing the T2 does not satisfy it',
  False),
 ('What decides whether a province collects its own corporate tax',
  'A permanent establishment in that province, not the place of '
  'incorporation',
  'A permanent establishment in that province, not the place of '
  'incorporation', False),
 ('Filing route and confirmation',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days', False),
]

PAGE = dict(
 col_a='Federal Corporation', col_b='Ontario Corporation',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 table_note=('Four rows differ and six do not. What changes is the registry '
             'and the annual return that goes with it. The T2, the '
             'schedules, the filing route and the fee are the same for '
             'either corporation.'),
 slug='federal-corporation-vs-ontario-corporation-nil-filing',
 title='Federal vs Ontario Corporation | Nil T2 Filing',
 h1='Federal Corporation vs Ontario Corporation',
 h1_pre='Federal Corporation vs ', h1_span='Ontario Corporation',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='federal corporation vs ontario corporation nil filing',
 meta=('Both file the same federal T2 at the same price. What changes is the '
       'registry, the annual return and where that annual return is filed.'),
 seo_title='Federal vs Ontario Corporation | Nil T2 Filing',
 seo_desc=('Both are ' + PRICE + ' and both file the same federal T2. What '
           'changes is the registry, the annual return and where it is '
           'filed.'),
 answer=('Both file the same federal T2 at the same price. Where a '
         'corporation was incorporated does not change the return, the '
         'schedules or the fee. What it changes is the registry that holds '
         'the record and the annual return that goes with it, which is a '
         'separate filing from the T2 and is not covered by this fee. Either '
         'way the nil T2 is ' + PRICE + ', signed on Form T183CORP and '
         'transmitted the same way.'),
 cta2=('Date the Annual Return',
       T + 'federal-annual-return-anniversary-calculator/'),
 lead=[('One T2, Two Registries',
        ['<p>Corporate income tax is federal. A corporation incorporated in '
         'Ontario and a corporation incorporated federally file the same T2, '
         'on the same deadline, with the same schedules. Nothing about a '
         'quiet year changes because of where the certificate came from.</p>',
         '<p>What does change is the registry obligation sitting alongside '
         'it. Filing the T2 does not satisfy an annual return, and filing an '
         'annual return does not satisfy the T2. A corporation needs both, '
         'every year, for as long as it exists, and the annual return is not '
         'part of this service.</p>']),
       ],
 detail=dict(
  h2='The Annual Return Is a Separate Obligation',
  intro=('Whichever registry holds the corporation, the annual return sits '
         'outside the T2:'),
  items=[
   'An Ontario corporation files an annual return confirming its registered '
   'office address, its directors and its officers. It carries no tax and no '
   'payment.',
   'Since October 2021 that Ontario filing goes through the Ontario Business '
   'Registry. Until 2021 it was filed alongside the T2, which is why older '
   'advice still says otherwise.',
   'A federal corporation files an annual return with Corporations Canada, '
   'at the fee that registry sets.',
   'A federally incorporated corporation operating in Ontario files both. '
   'Federal incorporation does not remove the provincial obligation.',
   'Whether a province collects its own corporate tax turns on a permanent '
   'establishment there, not on where the corporation was incorporated.',
   'Quebec and Alberta each collect their own corporate tax, so CO-17 and '
   'AT1 are separate returns. They are not part of the federal T2 and are '
   'not covered by this fee.',
  ],
  warn=('Neither annual return is included in nil T2 filing, and missing one '
        'is not fixed by filing the other. They are different filings, to '
        'different bodies, on different dates.'),
  close=('The <a href="' + T + 'annual-return-vs-tax-return-checker/">annual '
         'return versus tax return checker</a> separates the two, the '
         '<a href="' + T + 'provincial-return-requirement-checker/">'
         'provincial return requirement checker</a> takes the permanent '
         'establishment question, the '
         '<a href="' + T + 'federal-annual-return-anniversary-calculator/">'
         'federal annual return anniversary calculator</a> dates the '
         'Corporations Canada filing, and the '
         '<a href="' + G + 'provincial-and-federal-annual-returns/">complete '
         'guide to provincial and federal annual returns</a> sets out the '
         'fees and the dates.')),
 band=('The Same T2 Either Way',
       'Federal or Ontario, the return is prepared, reviewed and transmitted '
       'the same way, at ' + PRICE + '.'),
 cards=[('Reviewed by a CPA',
         'The return is prepared and reviewed by a CPA Ontario member. Where '
         'the corporation was incorporated does not change the review.'),
        ('The schedules are inside the fee',
         'GIFI Schedules 100, 125 and 141, Schedule 50, Schedule 24 on a '
         'first return, Schedule 8 and loss continuity, for either '
         'corporation.'),
        ('What is not inside the fee',
         'The annual return to Corporations Canada or the Ontario Business '
         'Registry, and the Quebec CO-17 or Alberta AT1 where a province '
         'collects its own tax.')],
 case=('A corporation incorporated federally with its registered office in '
       'Ontario, quiet for the year',
       'Its T2 is the same federal return any Ontario-incorporated '
       'corporation would file, on the same deadline, with the same '
       'schedules where anything sits on its books, at ' + PRICE + '. '
       'Alongside it the corporation owes a Corporations Canada annual '
       'return and an Ontario filing, because federal incorporation does not '
       'remove the provincial obligation. Neither of those is part of this '
       'service and neither is satisfied by filing the T2. The figures here '
       'illustrate how the rules apply and are not drawn from a client '
       'file.'),
 faq=[
  ('Does a federal corporation pay more for a nil T2?',
   'No. The fee is ' + PRICE + ' for either corporation. Where it was '
   'incorporated does not change the return or the price.'),
  ('Is the T2 different for an Ontario corporation?',
   'No. Corporate income tax is federal, so both file the same T2 on the '
   'same deadline with the same schedules.'),
  ('What is the difference then?',
   'The registry. A federal corporation is on the Corporations Canada '
   'register and an Ontario corporation is on the Ontario Business Registry, '
   'and each owes that registry an annual return.'),
  ('Is the annual return included in the fee?',
   'No. The annual return is a registry filing, not a tax return, and it is '
   'not part of nil T2 filing.'),
  ('Does filing the T2 satisfy the annual return?',
   'No, and the reverse is also true. Filing an annual return does not '
   'satisfy the T2. A corporation needs both, every year, for as long as it '
   'exists.'),
  ('What does the Ontario annual return actually report?',
   'The registered office address, the directors and the officers. It '
   'carries no tax and no payment.'),
  ('Where is the Ontario annual return filed?',
   'Through the Ontario Business Registry. Until 2021 it was filed alongside '
   'the T2, which is why older guidance still describes it that way.'),
  ('What does a federal corporation file instead?',
   'An annual return with Corporations Canada, at the fee that registry '
   'sets. The complete guide to provincial and federal annual returns '
   'carries the current figure.'),
  ('I am federally incorporated but operate in Ontario. Which do I file?',
   'Both. The Corporations Canada annual return and an Ontario filing. '
   'Federal incorporation does not remove the provincial obligation.'),
  ('Does incorporating federally avoid provincial corporate tax?',
   'No. What decides whether a province collects its own corporate tax is a '
   'permanent establishment in that province, not where the corporation was '
   'incorporated.'),
  ('What about Quebec and Alberta?',
   'Quebec and Alberta each collect their own corporate tax, so CO-17 and '
   'AT1 are separate returns. They are not part of the federal T2 and are '
   'not covered by this fee.'),
  ('Do the GIFI schedules differ by registry?',
   'No. The schedules follow what sits on the corporation&rsquo;s books, not '
   'the registry that holds its record.'),
  ('Is the deadline different?',
   'The T2 is due six months after the fiscal year-end for either '
   'corporation. The annual returns run on their own dates, which are not '
   'the T2 deadline.'),
  ('Does the corporation number differ?',
   'A federal corporation and an Ontario corporation are identified on '
   'different registers, which is one reason the two annual returns cannot '
   'be filed in place of each other.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'annual-return-vs-tax-return-checker/">annual '
   'return versus tax return checker</a>, which separates what this service '
   'covers from what the registry wants.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7f-manifest.json')
