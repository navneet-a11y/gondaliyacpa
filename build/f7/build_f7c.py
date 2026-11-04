#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 3: /compare/filing-one-year-vs-filing-all-unfiled-years/

Why this page next
------------------
Same test as page 2: line 1215 will not publish a comparison unless both
price columns carry published prices, so the buildable set is the concept
pages where both columns are our own fee. Here they are, and the page is
worth more than most of the list because catch-up filing is a core service
and the question is one people actually weigh.

The price rows say the same figure on both sides on purpose. The fee is
counted per tax year whichever route is taken, so the honest comparison is
not about price at all, and the page says so in its first line rather than
implying a discount for volume that does not exist.

No totals appear anywhere. A multi-year total would be a money figure
outside the two the gate allows ($300.00 and $350.00), and inventing one
would also set a price the plan has never stated.

Penalties are not discussed. Hard rule 3 bars "no penalty" standing alone and
requires the full Section 7.4 qualification wherever the subject is raised;
this page does not need the subject to make its point, so it leaves it out
rather than carry a block of qualification it cannot check.
"""
from build_f7 import T, G, COST, PRICE, check, write

PRICE_ROWS = [
 ('Our published fee for a quiet year', PRICE, PRICE, True),
 ('Each additional unfiled tax year', PRICE, PRICE, True),
]

FEATURE_ROWS = [
 ('Which years are filed',
  'The one year you pick',
  'Every year that is outstanding', True),
 ('What is still open afterwards',
  'Every other unfiled year',
  'Nothing. The run is closed', True),
 ('A demand to file from the Canada Revenue Agency',
  'Answered only where the year you filed is the year it named',
  'Answered for every year it named', True),
 ('Loss continuity across the years',
  'Cannot follow a year that is missing',
  'Carried year by year across the whole run', True),
 ('When each return is due',
  'Six months after that year-end',
  'Six months after that year-end', False),
 ('GIFI Schedules 100, 125 and 141',
  'Required where anything sits on the books',
  'Required where anything sits on the books', False),
 ('Form T183CORP',
  'One for each year, signed by an authorized signing officer',
  'One for each year, signed by an authorized signing officer', False),
 ('Filing route and confirmation',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days', False),
]

PAGE = dict(
 col_a='Filing One Year', col_b='Filing All Unfiled Years',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 table_note=('Four rows differ and six do not. What changes is how many '
             'years close and what is left open behind them. The work on '
             'each year, and the fee for it, do not.'),
 slug='filing-one-year-vs-filing-all-unfiled-years',
 title='Filing One Year vs All Unfiled Years | What Changes',
 h1='Filing One Year vs Filing All Unfiled Years',
 h1_pre='Filing One Year vs ', h1_span='Filing All Unfiled Years',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='filing one year vs all unfiled years',
 meta=('What filing a single year closes, what it leaves open, and what '
       'filing every outstanding year does instead.'),
 seo_title='Filing One Year vs All Unfiled Years | What Changes',
 seo_desc=('Both are ' + PRICE + ', counted per year. What filing a single '
           'year leaves open, and what filing every unfiled year closes.'),
 answer=('The fee is the same on both routes and it is counted per tax year, '
         'so the choice is not about price. Filing one year closes that year '
         'and leaves every other unfiled year exactly as it was. Filing all '
         'of them closes the run. Each year is ' + PRICE + ', carries its '
         'own schedules, is signed on its own Form T183CORP and is '
         'transmitted the same way.'),
 cta2=('Count the Unfiled Years', T + 'unfiled-years-checker/'),
 lead=[('The Fee Is Per Year, So the Choice Is Not About Price',
        ['<p>Filing three years costs three times what one year costs, and '
         'filing them in one go costs the same as filing them one at a time. '
         'There is no volume price here and no saving to weigh, which is '
         'worth saying plainly because it is the first thing most people '
         'assume they are deciding.</p>',
         '<p>What the choice actually decides is how many years close. A '
         'year that is not filed does not settle itself, and the ones left '
         'behind keep doing what unfiled years do: they stay open, they sit '
         'against a demand to file, and they block a clearance certificate '
         'and a dissolution.</p>']),
       ],
 detail=dict(
  h2='What Filing One Year Leaves Behind',
  intro='A single year closes one return and nothing else:',
  items=[
   'Every other unfiled year stays open. A year that is not filed does not '
   'close on its own, however long it has been.',
   'A demand to file is answered only for the year it named, and only where '
   'that is the year you filed.',
   'Loss continuity cannot follow a year that is missing, so a later claim '
   'rests on a gap in the run.',
   'Unfiled years block a clearance certificate, and they block a '
   'dissolution.',
   'A corporation that stops filing stays on the register, with every one of '
   'those years still owed.',
   'The fee does not change by filing them together. It is counted per tax '
   'year either way.',
  ],
  warn=('Filing one year is not a partial fix for a run of unfiled years. It '
        'closes that year and leaves the rest exactly as they were.'),
  close=('The <a href="' + T + 'unfiled-years-checker/">unfiled years '
         'checker</a> counts what is outstanding, the '
         '<a href="' + T + 'unfiled-years-cost-calculator/">unfiled years '
         'cost calculator</a> prices the run at the fee per year, and the '
         '<a href="' + T + 'catch-up-filing-schedule-generator/">catch-up '
         'filing schedule generator</a> puts the years in order.')),
 band=('The Same Work Every Year',
       'Whether one year is filed or six, each year is prepared, reviewed '
       'and transmitted the same way, at ' + PRICE + '.'),
 cards=[('Reviewed by a CPA',
         'Every year is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted. An old year gets the same review as a current '
         'one.'),
        ('The schedules are inside the fee',
         'GIFI Schedules 100, 125 and 141, Schedule 50, Schedule 24 on a '
         'first return, Schedule 8 and loss continuity, on every year '
         'filed.'),
        ('Transmitted and confirmed',
         'Transmitted electronically by a registered EFILE electronic filer, '
         'with your CRA confirmation emailed within 3 business days.')],
 case=('A corporation with four quiet years behind it and a demand to file '
       'for one of them',
       'Say nothing has moved through it for four years and the Canada '
       'Revenue Agency has asked for the second of them. Filing that one '
       'year answers the demand and closes that year. The other three stay '
       'open, and they still block a clearance certificate and a dissolution '
       'if either is wanted later. Filing all four closes the run instead. '
       'Every year is ' + PRICE + ' on either route, counted per year, so '
       'nothing about the fee argues for one over the other. The figures '
       'here illustrate how the rules apply and are not drawn from a client '
       'file.'),
 faq=[
  ('Is it cheaper to file all the years at once?',
   'No. The fee is ' + PRICE + ', counted per tax year, and filing them '
   'together does not change it. There is no volume price, so cost is not '
   'what decides this.'),
  ('Can I file just the year the Canada Revenue Agency asked for?',
   'Yes. Filing that year answers that demand and closes that year. It does '
   'nothing to the other unfiled years, which stay open.'),
  ('Do old unfiled years ever close on their own?',
   'No. A year that is not filed stays open, however long it has been. The '
   'return is still owed.'),
  ('Does filing one year make the others easier?',
   'Not by itself. Each year is its own return with its own schedules and '
   'its own Form T183CORP, so the work on the remaining years is unchanged.'),
  ('What order should the years be filed in?',
   'Oldest first, so that loss continuity and opening balances carry forward '
   'correctly. The <a href="' + T + 'catch-up-filing-schedule-generator/">'
   'catch-up filing schedule generator</a> puts them in order.'),
  ('Can loss continuity be claimed across a gap?',
   'The schedule cannot follow a year that is missing. Where a year in the '
   'run is unfiled, a later claim rests on a gap, which is one reason the '
   'whole run is usually filed together.'),
  ('Do unfiled years stop a dissolution?',
   'Yes. Unfiled years block a clearance certificate and they block the '
   'dissolution itself, so a corporation being wound up clears the run '
   'first.'),
  ('How many years back can be filed?',
   'Every year the corporation has existed and not filed. There is no limit '
   'here at which a year stops being owed, and each one is ' + PRICE + '.'),
  ('Is each year signed separately?',
   'Yes. One Form T183CORP for each tax year, signed by an authorized '
   'signing officer before that year is transmitted.'),
  ('Do the quiet years still need the GIFI schedules?',
   'Yes, where anything sits on the books. A corporation holding share '
   'capital from incorporation has a balance sheet to report in every one of '
   'those years.'),
  ('How long until the confirmations arrive?',
   'Your CRA confirmation is emailed within 3 business days of transmission. '
   'Where several years are filed, each year has its own confirmation.'),
  ('Can some years be nil and others not?',
   'Yes. Each year is judged on its own facts. A year in which the '
   'corporation had activity is not a nil year, and it is not covered by '
   'this service.'),
  ('Does filing the whole run change what any single year costs?',
   'No. The fee is ' + PRICE + ' whichever years are filed and however many '
   'go at once.'),
  ('What if we are not sure how many years are outstanding?',
   'The <a href="' + T + 'unfiled-years-checker/">unfiled years checker</a> '
   'counts them from the incorporation date and the year-end, which is '
   'usually enough to see the size of the run.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'unfiled-years-checker/">unfiled years checker</a>, '
   'then the <a href="' + T + 'unfiled-years-cost-calculator/">unfiled years '
   'cost calculator</a> to price the run at the fee per year.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7c-manifest.json')
