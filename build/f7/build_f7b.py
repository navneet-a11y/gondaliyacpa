#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 2: /compare/nil-return-vs-final-return/

Why this page next
------------------
Appendix A lists twenty F7 URLs. Six are brand comparisons and stay blocked
until dated competitor prices arrive (see docs/decisions.md). Of the concept
pages, line 1215 requires BOTH price columns filled with published prices, so
the buildable ones are those where both columns are our own fee. This is one:
a nil return and a final return are the same service at the same price, filed
for different tax years.

The price on the right-hand column is not assumed. The live Family 4 pages for
final T2 before dissolution carry "$300.00 Plus HST Per Tax Year", so both
cells are the published fee and the comparison is truthful without any
external input.

Wording taken from what is already published
--------------------------------------------
The facts about the final return are lifted from the live F4 final-T2 pages
rather than written fresh, so the site does not say two different things:

  "covering the period that ends on the date of dissolution. That period is
   dated from the dissolution rather than from the usual year-end, and the
   return is due within six months of it."
  "Unfiled years block a clearance certificate, and they block the
   dissolution itself."
  "filing the final T2 does not dissolve the corporation on its own"

FAQ count
---------
Fifteen, set by Navneet on 2026-11-04 ("15 faqs are enough") after page 1 ran
to thirty-five. The plan sets no FAQ count for F7, so this is the house
standard from here. Still no FAQPage markup: hard rule 6 bars it, and the list
stays plain details/summary that opens without JavaScript.
"""
import build_f7 as b
from build_f7 import T, G, COST, PRICE, check, write

PRICE_ROWS = [
 ('Our published fee for a quiet year', PRICE, PRICE, True),
 ('A second quiet tax year', PRICE, PRICE, True),
]

# Four differ, four do not. With the two price rows that is four of ten rows
# different, which is the page's argument: the year changes, the work does not.
FEATURE_ROWS = [
 ('Which corporation files it',
  'One that is carrying on and was quiet for the year',
  'One that is being wound up', True),
 ('The period the return covers',
  'The full fiscal year',
  'The period that ends on the date of dissolution', True),
 ('When it is due',
  'Six months after the end of the tax year',
  'Six months after the end of the tax year', False),
 ('What comes after it',
  'Another return for every year until the corporation stops',
  'Nothing further once the dissolution completes', True),
 ('Does filing it dissolve the corporation',
  'Not applicable, the corporation carries on',
  'No. The final T2 does not dissolve the corporation on its own', True),
 ('GIFI Schedules 100, 125 and 141',
  'Required where anything sits on the books',
  'Required where anything sits on the books', False),
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
 col_a='Nil Return', col_b='Final Return',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 table_note=('Four rows differ and six do not. What changes is which year the '
             'return covers and what happens after it. The schedules, the '
             'signing, the filing route and the fee do not.'),
 cta2=('See What Is Still Outstanding',
       T + 'dissolution-readiness-checker/'),
 slug='nil-return-vs-final-return',
 title='Nil Return vs Final Return | What Changes',
 h1='Nil Return vs Final Return',
 h1_pre='Nil Return vs ', h1_span='Final Return',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='nil return vs final return',
 meta=('Which return a quiet corporation files while it carries on, which it '
       'files when it is wound up, and the six things that are the same '
       'either way.'),
 seo_title='Nil Return vs Final Return | What Changes',
 seo_desc=('Both are ' + PRICE + '. Which one a corporation files while it '
           'carries on, which one when it is wound up, and what stays the '
           'same.'),
 answer=('Both are the same return at the same price, filed for different '
         'tax years. A nil return is the T2 for a year in which the '
         'corporation carried on and did nothing. A final return is the T2 '
         'for the last tax year, covering the period that ends on the date of '
         'dissolution. Either way the filing is ' + PRICE + ', carries the '
         'same schedules, is signed on the same Form T183CORP and is '
         'transmitted the same way.'),
 lead=[('One Return, Two Points in a Corporation&rsquo;s Life',
        ['<p>A nil return and a final return are not two services. They are '
         'the same corporate income tax return filed for two different tax '
         'years: one while the corporation is still on the register and '
         'quiet, and one for the year it is wound up.</p>',
         '<p>Which one applies is decided by where the corporation stands at '
         'the end of the year, not by anything you choose. A corporation that '
         'stopped trading but has not dissolved is still carrying on for '
         'filing purposes, so it files a nil return every year until the '
         'dissolution happens, and only then a final one.</p>']),
       ],
 detail=dict(
  h2='What Decides Which One You Are Filing',
  intro=('The corporation&rsquo;s own position at the end of the tax year '
         'decides it:'),
  items=[
   'The corporation is on the register and did nothing in the year. That '
   'year is a nil return.',
   'The corporation is being wound up. Its last tax year ends on the date of '
   'dissolution, and that return is the final one.',
   'Every year before the final one is still its own return, filed on its '
   'own, at the same fee.',
   'A corporation that stopped trading but has not dissolved is still '
   'carrying on for filing purposes. It files a nil return every year.',
   'Unfiled earlier years block a clearance certificate, and they block the '
   'dissolution itself.',
   'The final return does not dissolve the corporation on its own. The '
   'dissolution is done with the registry the corporation is incorporated '
   'under.',
  ],
  warn=('A corporation that stops trading and simply stops filing is not '
        'finished with its returns. It stays on the register, and every year '
        'it does not file stays open until that return is filed.'),
  close=('The <a href="' + T + 'final-t2-return-due-date-calculator/">final '
         'T2 return due date calculator</a> dates the last return, the '
         '<a href="' + T + 'dissolution-readiness-checker/">dissolution '
         'readiness checker</a> says what is still outstanding, and the '
         '<a href="' + T + 'clearance-certificate-requirement-checker/">'
         'clearance certificate requirement checker</a> takes that question '
         'on its own.')),
 band=('The Same Work Either Way',
       'Whichever year the return covers, it is prepared, reviewed and '
       'transmitted the same way, at ' + PRICE + '.'),
 cards=[('Reviewed by a CPA',
         'Either return is prepared and reviewed by a CPA Ontario member '
         'before it is transmitted. The last year gets the same review as '
         'every year before it.'),
        ('The schedules are inside the fee',
         'GIFI Schedules 100, 125 and 141, Schedule 50, Schedule 24 on a '
         'first return, Schedule 8 and loss continuity, on whichever year '
         'applies.'),
        ('Transmitted and confirmed',
         'Transmitted electronically by a registered EFILE electronic filer, '
         'with your CRA confirmation emailed within 3 business days.')],
 case=('A corporation that stopped trading three years ago and is dissolving '
       'now',
       'Say nothing has moved through it since, and no return has been filed '
       'for those years. Each of those quiet years is its own nil return, and '
       'the last one is the final return, covering the period that ends on '
       'the date of dissolution. Every year is ' + PRICE + ', counted per '
       'year. The earlier years are not optional: unfiled years block a '
       'clearance certificate and they block the dissolution itself, so they '
       'are filed first and the final return goes last. The figures here '
       'illustrate how the rules apply and are not drawn from a client file.'),
 faq=[
  ('Does a final return cost more than a nil return?',
   'No. Both are ' + PRICE + '. The fee is counted per tax year, and the last '
   'year is charged the same as any other quiet year.'),
  ('Does filing the final T2 dissolve the corporation?',
   'No. Filing the final T2 does not dissolve the corporation on its own. The '
   'dissolution is done with the registry the corporation is incorporated '
   'under, and the return settles the corporation&rsquo;s position with the '
   'Canada Revenue Agency.'),
  ('What period does the final return cover?',
   'The period that ends on the date of dissolution. It is dated from the '
   'dissolution rather than from the usual year-end, so the last period is '
   'often shorter than a full year.'),
  ('When is the final return due?',
   'Six months after the end of that final period, which is the same rule '
   'that sets the deadline for any other tax year.'),
  ('Can the years before the final one be skipped?',
   'No. Each year is its own return. Unfiled years block a clearance '
   'certificate and they block the dissolution itself, so in practice the '
   'final return is rarely the only one outstanding.'),
  ('The corporation stopped trading years ago. Is each of those a nil return?',
   'Yes, where nothing moved through it. A corporation that has stopped '
   'trading but has not dissolved is still carrying on for filing purposes, '
   'so every one of those years is a return at ' + PRICE + '.'),
  ('What is a clearance certificate?',
   'It is the Canada Revenue Agency&rsquo;s confirmation of the '
   'corporation&rsquo;s position before its property is distributed. It is '
   'requested separately from the return, and unfiled years block it.'),
  ('Does a final return still need the GIFI schedules?',
   'Yes, where anything sits on the books. The schedules follow what the '
   'corporation holds, not which year of its life the return covers.'),
  ('Is Form T183CORP needed on a final return?',
   'Yes. An authorized signing officer signs Form T183CORP before the return '
   'is transmitted, on the final return exactly as on any other.'),
  ('How long until the confirmation arrives?',
   'Your CRA confirmation is emailed within 3 business days of transmission, '
   'on either return.'),
  ('What if the corporation is dissolved before the returns are filed?',
   'The returns are still owed for the years the corporation existed. '
   'Dissolving does not close the years behind it, which is why the unfiled '
   'years are cleared first.'),
  ('Can the final return be filed on the T2 Short?',
   'Yes, where the corporation meets every one of the eight conditions for '
   'that year. Which form carries the return is a separate question from '
   'which year it covers, and it is set out in '
   '<a href="' + b.BASE + 't2-short-vs-full-t2/">T2 Short vs Full T2</a>.'),
  ('Is the price different if several years are filed at once?',
   'No. The fee is ' + PRICE + ', counted per year, however many years are '
   'filed together.'),
  ('What happens if we stop filing instead of dissolving?',
   'The corporation stays on the register and every year it does not file '
   'stays open. Stopping is not the same as finishing, and the returns are '
   'still owed when the corporation is eventually wound up.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'dissolution-readiness-checker/">dissolution '
   'readiness checker</a>, which names what is still outstanding. The '
   '<a href="' + T + 'final-t2-return-due-date-calculator/">final T2 return '
   'due date calculator</a> then dates the last return.'),
 ],
 related=[(T + 'final-t2-return-due-date-calculator/',
           'Final T2 return due date calculator'),
          (T + 'dissolution-readiness-checker/',
           'Dissolution readiness checker, what is still outstanding'),
          (T + 'clearance-certificate-requirement-checker/',
           'Clearance certificate requirement checker'),
          (G + 'final-t2-and-dissolution/', 'Final T2 and dissolution'),
          (G + 'winding-up-an-inactive-corporation/',
           'Winding up an inactive corporation'),
          (COST, 'Nil T2 filing cost')],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7b-manifest.json')
