#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 7: /compare/nil-t2-vs-zero-return/

Why this page
-------------
Appendix A line 3264 lists it, and it is one of only two F7 URLs left that can
be built with no further input: both price cells are our own fee, and they are
the same figure, because the two names describe one filing.

That is also the page's whole payload. A searcher typing "zero return" wants to
know whether it is a different thing from a nil return. It is not. There is no
zero-return form; the return is the T2 either way, and what decides whether a
year qualifies is whether anything happened in it.

The one genuine trap, and where it comes from
---------------------------------------------
The word "zero" invites filing the whole return as zeroes, balance sheet
included. /guides/zero-activity-corporate-tax-returns/ is explicit about it:

  "A zero-activity return is not an empty return. Several schedules are filed
   carrying zeroes, and one of them is filed only once."
  "The balance sheet is rarely all zeroes. Share capital issued on
   incorporation, a shareholder loan and retained earnings carried forward all
   sit on Schedule 100 whether or not anything happened during the year."
  "A balance sheet filed as entirely zero when share capital was issued is
   wrong, and it is wrong in a way that persists: the next return opens from
   the closing balances this one reports."

So of the ten rows, the two that differ are the name itself and that mistake.
Six rows identical is the correct answer to the question, not a thin table.

Agreeing with what is already published
---------------------------------------
From /guides/zero-activity-corporate-tax-returns/:

  "Zero activity means the corporation had no revenue, no expenses, no income
   of any kind and no disposition of property during the tax year. The return
   is filed showing those amounts as $0.00."
  "It is a statement about the tax year, not about the corporation."
  "Every resident corporation files a T2 for every tax year, whether or not it
   did anything. The obligation attaches to existing as a corporation, not to
   earning income."
  "The return is how the Agency learns the year was zero. Without it the year
   is not recorded as zero, it is recorded as missing."
  "Amount is irrelevant to every row. Four dollars of interest answers the
   third question yes exactly as four thousand would."
  "Each year is its own return on its own form for its own tax year."

What is not on this page
------------------------
/nil-t2-vs-loss-t2/ is a separate Appendix A URL. A year with activity that
nets to nothing is that page's subject, not this one's, so this page says only
that any revenue, expense, income or disposition takes a year out of zero
activity and leaves what happens next to the page that owns it. Line 1212
exists to stop two URLs covering one comparison.
"""
import build_f7
from build_f7 import T, G, COST, PRICE, check, write

build_f7.TODAY, build_f7.ISO = 'November 5, 2026', '2026-11-05'

PRICE_ROWS = [
 ('Our published fee for a quiet year', PRICE, PRICE, False),
 ('A second quiet tax year', PRICE, PRICE, False),
]

FEATURE_ROWS = [
 ('What the Canada Revenue Agency receives',
  'A T2 return for that tax year',
  'A T2 return for that tax year. There is no separate zero-return form',
  True),
 ('What the income statement carries',
  'Zeroes in the GIFI income statement codes',
  'The same zeroes, filed the same way', False),
 ('What the balance sheet carries',
  'Share capital issued on incorporation, any shareholder loan and retained '
  'earnings brought forward',
  'The same, and a balance sheet filed as entirely zero when share capital '
  'was issued is wrong', True),
 ('Whether Schedule 50 still applies',
  'Yes, for every shareholder at 10% or more',
  'Yes, on the same test', False),
 ('What takes the year out of it',
  'Any revenue, expense, income of any kind or disposition of property in the '
  'tax year',
  'The same test, and the amount is irrelevant to it', False),
 ('Whether the T2 Short is available',
  'Commonly, where the corporation meets the conditions',
  'On the same conditions', False),
 ('Form T183CORP',
  'Signed by an authorized signing officer before the return is transmitted',
  'The same form, signed the same way', False),
 ('Filing route and confirmation',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days',
  'The same route and the same confirmation', False),
]

PAGE = dict(
 col_a='Nil T2 Return', col_b='Zero Return',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 table_note=('Two rows differ. The first is the name: there is no '
             'zero-return form, and the return is the T2 either way. The '
             'second is the mistake the word zero invites, which is filing a '
             'balance sheet as entirely zero when share capital was issued. '
             'The other six rows are identical, because the two names '
             'describe one filing.'),
 slug='nil-t2-vs-zero-return',
 title='Nil T2 vs Zero Return | Same Filing, Two Names',
 h1='Nil T2 Return vs Zero Return',
 h1_pre='Nil T2 Return vs ', h1_span='Zero Return',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='nil t2 vs zero return',
 meta=('Both names describe the same filing: a T2 for a tax year with no '
       'activity. What is reported as $0.00, what is not, and why the '
       'difference matters.'),
 seo_title='Nil T2 vs Zero Return | Same Filing',
 seo_desc=('A zero return is a nil T2. There is no separate form. What is '
           'reported as $0.00, what the balance sheet still carries, and the '
           'one fee for either.'),
 answer=('They are the same filing. A nil return and a zero return both mean '
         'a T2 filed for a tax year in which the corporation had no revenue, '
         'no expenses, no income of any kind and no disposition of property. '
         'There is no zero-return form: the Canada Revenue Agency receives a '
         'T2 either way, at ' + PRICE + '. The word that matters is not nil '
         'or zero but the year, because the test is asked year by year and a '
         'single entry takes a year out of it.'),
 cta2=('Test a Quiet Year', T + 'dormant-corporation-test/'),
 lead=[('One Filing, Two Words for It',
        ['<p>Neither nil nor zero is the name of a form. Both are ways of '
         'describing a tax year in which nothing happened, and the return '
         'that reports such a year is the ordinary T2, filed on the ordinary '
         'deadline with the schedules the corporation&rsquo;s own position '
         'requires.</p>',
         '<p>Every resident corporation files a T2 for every tax year, '
         'whether or not it did anything. The obligation attaches to existing '
         'as a corporation, not to earning income. The return is how the '
         'Agency learns the year was zero, and without it the year is not '
         'recorded as zero, it is recorded as missing.</p>',
         '<p>So the choice of word changes nothing. What does change things '
         'is that zero activity is a statement about the twelve months rather '
         'than about the corporation: the same corporation can have a quiet '
         'year, then a trading year, then another quiet year, and each is '
         'assessed on its own.</p>']),
       ],
 detail=dict(
  h2='What Is Reported as $0.00, and What Is Not',
  intro=('A zero-activity return is not an empty return. These are the parts '
         'that carry zeroes and the parts that do not:'),
  items=[
   'Revenue, expenses, income of any kind and dispositions of property are '
   'reported as $0.00 for the tax year.',
   'The GIFI income statement codes carry those zeroes, filed the same way a '
   'trading year files real figures.',
   'Share capital issued on incorporation sits on Schedule 100 whether or not '
   'anything happened during the year.',
   'A shareholder loan and retained earnings brought forward sit there too, '
   'and neither becomes zero because the year was quiet.',
   'Schedule 50 still reports every shareholder at 10% or more.',
   'Schedule 24 is filed on a first return, and once only.',
   'Interest credited to a corporate account is investment income whatever '
   'the amount, so it takes the year out of zero activity.',
  ],
  warn=('A balance sheet filed as entirely zero when share capital was issued '
        'is wrong, and it is wrong in a way that persists: the next return '
        'opens from the closing balances this one reports.'),
  close=('The <a href="' + T + 'dormant-corporation-test/">dormant '
         'corporation test</a> settles whether a year qualifies, the '
         '<a href="' + T + 'nil-gifi-balance-sheet-checker/">nil GIFI balance '
         'sheet checker</a> takes what Schedule 100 must carry, and the '
         '<a href="' + G + 'zero-activity-corporate-tax-returns/">complete '
         'guide to zero-activity corporate tax returns</a> sets out the whole '
         'subject.')),
 band=('The Same Return Under Either Name',
       'Prepared, reviewed and transmitted the same way whichever word '
       'brought you here, at ' + PRICE + '.'),
 cards=[('Reviewed by a CPA',
         'The return is prepared and reviewed by a CPA Ontario member. The '
         'word you searched for does not change the work.'),
        ('The schedules are inside the fee',
         'GIFI Schedules 100, 125 and 141, Schedule 50, Schedule 24 on a '
         'first return, Schedule 8 and loss continuity.'),
        ('What is not inside the fee',
         'A year that was not quiet. A holding corporation with investment '
         'income, a rental corporation and a corporation that paid or '
         'received a dividend are not nil, and those years are handled at '
         'gondaliyacpa.ca at $350.00 plus HST per year.')],
 case=('A corporation with share capital on its books and nothing else in the '
       'tax year',
       'Its income statement codes are all $0.00, and its balance sheet is '
       'not: the share capital issued on incorporation sits on Schedule 100, '
       'and so do any shareholder loan and the retained earnings brought '
       'forward. The return is a nil T2 at ' + PRICE + ', whichever of the '
       'two names brought the directors to it. Filing it as an entirely zero '
       'balance sheet would be wrong, and the error would carry into the next '
       'year, because that return opens from the closing balances this one '
       'reports. The figures here illustrate how the rules apply and are not '
       'drawn from a client file.'),
 faq=[
  ('Is a zero return the same as a nil T2?',
   'Yes. Both describe a T2 filed for a tax year with no revenue, no '
   'expenses, no income of any kind and no disposition of property.'),
  ('Is there a separate zero-return form?',
   'No. The Canada Revenue Agency receives a T2 for the tax year either way. '
   'Neither nil nor zero is the name of a form.'),
  ('Does the fee differ between the two?',
   'No. There is one filing, so there is one fee: ' + PRICE + '.'),
  ('Does a zero-activity corporation have to file at all?',
   'Yes. Every resident corporation files a T2 for every tax year, whether or '
   'not it did anything. The obligation attaches to existing as a '
   'corporation, not to earning income.'),
  ('What happens if the year is simply not filed?',
   'The year is not recorded as zero, it is recorded as missing. The return '
   'is how the Agency learns the year was empty.'),
  ('Is the whole return filed as zeroes?',
   'No. The income statement codes carry zeroes, but the balance sheet '
   'carries share capital, any shareholder loan and retained earnings brought '
   'forward.'),
  ('Why is the balance sheet not zero if nothing happened?',
   'Because those balances were there before the year started and are still '
   'there after it ends. A quiet year does not clear them.'),
  ('What goes wrong if I file it all as zero?',
   'The error persists. The next return opens from the closing balances this '
   'one reports, so a wrong closing balance becomes a wrong opening balance.'),
  ('Does Schedule 50 still have to be filed?',
   'Yes, for every shareholder at 10% or more. A quiet year does not change '
   'who owns the corporation.'),
  ('What takes a year out of zero activity?',
   'Any revenue, any expense, income of any kind or a disposition of '
   'property. The amount is irrelevant to the test.'),
  ('Does a few dollars of bank interest count?',
   'Yes. Interest credited to a corporate account is investment income '
   'whatever the amount, and a few dollars answers the question the same way '
   'a few thousand would.'),
  ('Is zero activity decided once for the corporation?',
   'No. It is a statement about the tax year. The same corporation can have a '
   'quiet year, then a trading year, then another quiet year.'),
  ('Can several zero-activity years be filed together?',
   'Yes. Each is its own return on its own form for its own tax year, '
   'prepared oldest first so the closing balances of one open the next, at '
   + PRICE + ' each.'),
  ('Can a zero-activity year use the T2 Short?',
   'Commonly, where the corporation meets the conditions. Meeting them is not '
   'automatic, and the conditions are the same under either name.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'dormant-corporation-test/">dormant corporation '
   'test</a>, which asks the six questions that settle whether the year '
   'qualifies.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7g-manifest.json')
