#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 4: /compare/t2-short-vs-t2-short-plus-gifi/

Why this page
-------------
Same line 1215 test as pages 2 and 3: both price columns must carry published
prices, so the buildable set is the concept pages where both columns are our
own fee. Here they are, and the question behind it is real -- whether GIFI
Schedules 100, 125 and 141 attach to a quiet return -- with a checker already
on the site that answers it.

Agreeing with what is already published
---------------------------------------
The position and the five triggers are taken from the live pages rather than
written fresh:

  /guides/gifi-schedules-100-125-141/
    "A corporation that was inactive all year and has nothing at all to
     report may omit GIFI Schedules 100, 125 and 141. Nothing at all means no
     assets, no liabilities, no equity balance, no revenue and no expenses.
     That is a narrower case than most owners assume."

  /tools/gifi-schedule-requirement-checker/ -- the five triggers, verbatim,
    and "Any one yes makes all three required."

One deliberate change from the guide's wording: the guide illustrates the
point with a share capital figure. That figure cannot appear here, because
gate.py allows only $300.00 and $350.00 anywhere on an F7 page and a stray
money amount is exactly the kind of thing that rule exists to catch. The
point is made as "share capital of any amount" instead, which is in fact the
stronger statement.
"""
from build_f7 import T, G, COST, PRICE, check, write

# The five triggers, verbatim from /tools/gifi-schedule-requirement-checker/.
TRIGGERS = [
 'Share capital issued at incorporation or since.',
 'Any cash or bank balance held during the year.',
 'A shareholder loan outstanding, owed either way.',
 'An incorporation cost carried on the books.',
 'Any bank charge or other expense in the year.',
]

PRICE_ROWS = [
 ('Our published fee for a quiet year', PRICE, PRICE, True),
 ('A second quiet tax year', PRICE, PRICE, True),
]

FEATURE_ROWS = [
 ('Which corporations it applies to',
  'One that was inactive all year with nothing at all to report',
  'One with anything at all on its books', True),
 ('GIFI Schedules 100, 125 and 141',
  'Omitted',
  'All three filed', True),
 ('What decides which column you are in',
  'All five triggers answered no',
  'Any one of the five triggers answered yes', True),
 ('How often it applies',
  'A narrower case than most owners assume',
  'The usual case for a quiet corporation', True),
 ('The eight T2 Short conditions',
  'Still have to hold',
  'Still have to hold', False),
 ('Filing deadline',
  'Six months after the fiscal year-end',
  'Six months after the fiscal year-end', False),
 ('Form T183CORP',
  'Signed by an authorized signing officer before transmission',
  'Signed by an authorized signing officer before transmission', False),
 ('Filing route and confirmation',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days', False),
]

PAGE = dict(
 col_a='T2 Short Alone', col_b='T2 Short plus GIFI',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 table_note=('Four rows differ and six do not. What changes is whether the '
             'three schedules attach. The eight conditions, the deadline, '
             'the signing, the filing route and the fee do not.'),
 slug='t2-short-vs-t2-short-plus-gifi',
 title='T2 Short vs T2 Short plus GIFI | What Attaches',
 h1='T2 Short vs T2 Short plus GIFI',
 h1_pre='T2 Short vs ', h1_span='T2 Short plus GIFI',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='t2 short vs t2 short plus gifi',
 meta=('When a quiet return may omit GIFI Schedules 100, 125 and 141, the '
       'five triggers that make all three required, and what is the same '
       'either way.'),
 seo_title='T2 Short vs T2 Short plus GIFI | What Attaches',
 seo_desc=('Both are ' + PRICE + '. When a nil T2 may omit GIFI Schedules '
           '100, 125 and 141, and the five triggers that make all three '
           'required.'),
 answer=('Both are the same return at the same price. What differs is '
         'whether GIFI Schedules 100, 125 and 141 attach to it. A '
         'corporation that was inactive all year and has nothing at all to '
         'report may omit the three. Any share capital, any bank balance, '
         'any shareholder loan, any incorporation cost on the books or any '
         'expense in the year makes all three required. Either way the '
         'filing is ' + PRICE + ', is signed on the same Form T183CORP and '
         'is transmitted the same way.'),
 cta2=('Run the Five Triggers', T + 'gifi-schedule-requirement-checker/'),
 lead=[('The Schedules Follow the Books, Not the Form',
        ['<p>Qualifying for the T2 Short does not remove a schedule that is '
         'otherwise required. The eight conditions decide which form the '
         'return goes on; what the corporation holds decides which schedules '
         'that form carries. They are two separate questions and a yes to '
         'one says nothing about the other.</p>',
         '<p>That is why a return can be on the short form and still carry '
         'all three GIFI schedules, which is the ordinary case rather than '
         'the exception. Omitting them is possible, but only for a '
         'corporation with nothing at all to report, and that is a narrower '
         'case than it sounds.</p>']),
       ],
 detail=dict(
  h2='The Five Triggers',
  intro=('Any one of these answered yes makes all three GIFI schedules '
         'required for the year:'),
  items=TRIGGERS,
  warn=('A corporation that was inactive all year and has nothing at all to '
        'report may omit the three schedules. Nothing at all means no '
        'assets, no liabilities, no equity balance, no revenue and no '
        'expenses. Share capital of any amount does not meet it, and neither '
        'does a bank account that merely sat there.'),
  close=('The <a href="' + T + 'gifi-schedule-requirement-checker/">GIFI '
         'schedule requirement checker</a> runs all five at once, the '
         '<a href="' + T + 't2-short-eligibility-checker/">T2 Short '
         'eligibility checker</a> takes the separate question of which form '
         'the return goes on, and the '
         '<a href="' + G + 'gifi-schedules-100-125-141/">complete guide to '
         'GIFI Schedules 100, 125 and 141</a> sets out what each one '
         'reports.')),
 band=('The Same Return Either Way',
       'Whether the three schedules attach or not, the return is prepared, '
       'reviewed and transmitted the same way, at ' + PRICE + '.'),
 cards=[('Reviewed by a CPA',
         'The schedules are decided by a CPA Ontario member reading what the '
         'corporation holds, not by a box you tick when you order.'),
        ('The schedules are inside the fee',
         'All three GIFI schedules where they are required, with Schedule 50 '
         'and Schedule 24 where those apply. Nothing on this list is charged '
         'separately.'),
        ('Transmitted and confirmed',
         'Transmitted electronically by a registered EFILE electronic filer, '
         'with your CRA confirmation emailed within 3 business days.')],
 case=('A corporation incorporated two years ago that has never traded',
       'Say it issued shares at incorporation, opened a bank account that '
       'has sat untouched, and carries its incorporation cost on the books. '
       'Three of the five triggers are answered yes, so all three GIFI '
       'schedules are required, and they are required in both of its quiet '
       'years. The return still goes on the T2 Short if the eight conditions '
       'hold, and the fee is ' + PRICE + ' either way. Omitting the '
       'schedules would need the corporation to hold nothing at all, which '
       'this one does not. The figures here illustrate how the rules apply '
       'and are not drawn from a client file.'),
 faq=[
  ('Does omitting the GIFI schedules make the return cheaper?',
   'No. The fee is ' + PRICE + ' whether the three schedules attach or not. '
   'They are inside the fee, not an extra on top of it.'),
  ('Can I choose to leave the schedules off?',
   'It is not a choice. Any one of the five triggers answered yes makes all '
   'three required, and we check them before the return is prepared.'),
  ('Does qualifying for the T2 Short remove the schedules?',
   'No. The eight conditions decide which form the return goes on. What the '
   'corporation holds decides which schedules that form carries. The two '
   'questions are separate.'),
  ('My corporation has share capital and nothing else. Does that count?',
   'Yes. Share capital of any amount is the first of the five triggers, so '
   'all three schedules are required.'),
  ('The bank account never moved. Does it still count?',
   'Yes. A cash or bank balance held during the year is a trigger whether or '
   'not anything went through it. A balance sheet does not become nil '
   'because the year was nil.'),
  ('What does Schedule 100 report?',
   'The balance sheet: what the corporation owns and owes at the fiscal '
   'year-end. On a dormant corporation that is often a single line of share '
   'capital and a matching line of cash or a shareholder loan.'),
  ('What do Schedules 125 and 141 report?',
   'Schedule 125 is the income statement and Schedule 141 is the notes '
   'checklist. They are filed alongside Schedule 100 where any trigger '
   'applies.'),
  ('Is it really all three, or can one be left off?',
   'All three. Any one trigger answered yes makes the set required, and they '
   'are filed together.'),
  ('How common is it to omit them?',
   'Uncommon. It needs a corporation with no assets, no liabilities, no '
   'equity balance, no revenue and no expenses, which is narrower than most '
   'owners expect.'),
  ('Does a shareholder loan make them required?',
   'Yes. A shareholder loan outstanding, owed in either direction, is one of '
   'the five triggers.'),
  ('Do bank charges count as expenses?',
   'Yes. Any bank charge or other expense in the year is a trigger on its '
   'own, even where nothing else moved.'),
  ('Does this change from year to year?',
   'It can. The triggers are tested against each tax year on its own facts, '
   'so one year may need the schedules and another may not.'),
  ('Does the deadline change if the schedules attach?',
   'No. The return is due six months after the fiscal year-end either way.'),
  ('Is Form T183CORP different?',
   'No. An authorized signing officer signs Form T183CORP before the return '
   'is transmitted, with or without the three schedules.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'gifi-schedule-requirement-checker/">GIFI schedule '
   'requirement checker</a>, which runs all five triggers and tells you '
   'which column your return is in.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7d-manifest.json')
