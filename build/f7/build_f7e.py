#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 5: /compare/december-31-year-end-vs-a-non-calendar-year-end/

Why this page
-------------
Same line 1215 test as pages 2 to 4: both price columns are our own fee, so
the comparison can be published without any external input.

Agreeing with what is already published
---------------------------------------
Every factual claim is taken from the live guides rather than written fresh:

  /guides/choosing-and-changing-a-fiscal-year-end/
    "A corporation picks its own fiscal year-end. There is no default,
     nothing is allocated at incorporation, and December 31 is a convention
     rather than a rule. The articles of incorporation do not set it either.
     What sets it is the first T2 return filed."
    and the headings: the first tax year cannot exceed 53 weeks, a short year
    does not get an early deadline, changing it needs written approval, a
    wrong year-end gets the transmission rejected.

  /guides/t2-filing-deadlines/
    "A T2 is due six months after the day the tax year ends."
    "The six months are counted to the same day number in the later month."
    "A first tax year runs from the date of incorporation to the chosen
     year-end, and it may not exceed 53 weeks. That is 371 days, counting the
     day of incorporation."

What is deliberately NOT on the page
------------------------------------
The deadline guide also sets out the T4 information return and the registry
annual return, both of which run on dates that are not measured from the
year-end. That would make a fourth differing row, but payroll obligations on
a service for corporations that did nothing is a claim worth more care than
this page needs, so the fourth difference is the practical one instead: when
in the year the records are wanted.
"""
from build_f7 import T, G, COST, PRICE, check, write

PRICE_ROWS = [
 ('Our published fee for a quiet year', PRICE, PRICE, True),
 ('A second quiet tax year', PRICE, PRICE, True),
]

FEATURE_ROWS = [
 ('The tax year ends',
  'December 31',
  'The date the corporation chose', True),
 ('The T2 is due',
  'June 30 the following year',
  'Six months after that year-end', True),
 ('Working the due date out',
  'June 30, with nothing to count',
  'Six months counted to the same day number in the later month', True),
 ('When the records are wanted',
  'Early in the new calendar year, with everything else dated December 31',
  'At whatever point in the year the chosen date falls', True),
 ('What sets the date in the first place',
  'The first T2 return filed. Nothing assigns one at incorporation',
  'The first T2 return filed. Nothing assigns one at incorporation', False),
 ('The first tax year',
  'From incorporation to that year-end, 53 weeks at most',
  'From incorporation to that year-end, 53 weeks at most', False),
 ('Changing it later',
  'Needs the written approval of the Canada Revenue Agency',
  'Needs the written approval of the Canada Revenue Agency', False),
 ('Filing route and confirmation',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days', False),
]

PAGE = dict(
 col_a='December 31 Year-End', col_b='A Non-Calendar Year-End',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 table_note=('Four rows differ and six do not. The year-end moves the dates '
             'and nothing else. What sets it, the 53-week limit on the first '
             'one, the approval needed to change it and the fee are the same '
             'on any date.'),
 slug='december-31-year-end-vs-a-non-calendar-year-end',
 title='December 31 Year-End vs a Non-Calendar Year-End',
 h1='December 31 Year-End vs a Non-Calendar Year-End',
 h1_pre='December 31 Year-End vs ', h1_span='a Non-Calendar Year-End',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='december 31 year-end vs non-calendar year-end',
 meta=('What the fiscal year-end date changes about a nil T2, what it does '
       'not, and why December 31 is a convention rather than a rule.'),
 seo_title='December 31 Year-End vs a Non-Calendar Year-End',
 seo_desc=('Both are ' + PRICE + '. What the year-end date changes about a '
           'nil T2, what it does not, and why December 31 is a convention '
           'rather than a rule.'),
 answer=('Both are the same return at the same price. The year-end sets the '
         'deadline and almost nothing else. A December 31 year-end makes the '
         'T2 due the following June 30; any other year-end makes it due six '
         'months after that date. December 31 is a convention rather than a '
         'rule, nothing assigns a year-end at incorporation, and what fixes '
         'it is the first T2 return filed. Either way the filing is '
         + PRICE + ', carries the same schedules and is transmitted the same '
         'way.'),
 cta2=('See Every Due Date', T + 'nil-t2-deadline-calculator/'),
 lead=[('The Date Moves the Deadline, Not the Return',
        ['<p>A quiet year is the same piece of work whenever it ends. The '
         'year-end decides when the return is due and when the records are '
         'wanted, and that is the whole of its effect on a nil filing. It '
         'does not change which schedules attach, who signs, how the return '
         'is transmitted or what it costs.</p>',
         '<p>December 31 is worth no more and no less than any other date. '
         'It is common because it lines up with the calendar most people '
         'already keep, not because anything in the rules prefers it, and a '
         'corporation that picked August 31 is in exactly the same position '
         'six months after August 31.</p>']),
       ],
 detail=dict(
  h2='Nothing Assigns You a Year-End',
  intro='The date is a decision rather than a default:',
  items=[
   'A corporation picks its own fiscal year-end. There is no default and '
   'nothing is allocated at incorporation.',
   'The articles of incorporation do not set it either. What sets it is the '
   'first T2 return filed.',
   'A first tax year runs from the date of incorporation to the chosen '
   'year-end and may not exceed 53 weeks, which is 371 days counting the day '
   'of incorporation.',
   'Once the first return is filed the date is on the record and it recurs '
   'annually.',
   'Changing it afterwards needs the written approval of the Canada Revenue '
   'Agency.',
   'A short year does not get an early deadline. The six months are counted '
   'from the day that short year ends.',
  ],
  warn=('A year-end that does not match the one on the record gets the '
        'transmission rejected. Where no return has ever been filed the date '
        'is still unsettled, and the first return filed is what settles it.'),
  close=('The <a href="' + T + 'nil-t2-deadline-calculator/">nil T2 deadline '
         'calculator</a> dates the return from any year-end, the '
         '<a href="' + T + '53-week-first-tax-year-checker/">53-week first '
         'tax year checker</a> tests a proposed first year-end, the '
         '<a href="' + T + 'year-end-change-approval-checker/">year-end '
         'change approval checker</a> takes the question of changing it, and '
         'the <a href="' + G + 'choosing-and-changing-a-fiscal-year-end/">'
         'complete guide to choosing and changing a fiscal year-end</a> sets '
         'out the rest.')),
 band=('The Same Return on Any Year-End',
       'Whichever date the year ends on, the return is prepared, reviewed '
       'and transmitted the same way, at ' + PRICE + '.'),
 cards=[('Reviewed by a CPA',
         'The return is prepared and reviewed by a CPA Ontario member '
         'whatever date the year ended on. An unusual year-end is not an '
         'unusual return.'),
        ('The schedules are inside the fee',
         'GIFI Schedules 100, 125 and 141, Schedule 50, Schedule 24 on a '
         'first return, Schedule 8 and loss continuity, on any year-end.'),
        ('Transmitted and confirmed',
         'Transmitted electronically by a registered EFILE electronic filer, '
         'with your CRA confirmation emailed within 3 business days.')],
 case=('A corporation incorporated in September that picked August 31',
       'Its first tax year runs from the September incorporation date to the '
       'following August 31, which is inside the 53-week limit, so the date '
       'is available. That first return is due the following February 28 or '
       '29, six months after August 31, and every year after it runs on the '
       'same cycle. Nothing about the quiet year is different from a '
       'December 31 corporation: the same schedules where anything sits on '
       'the books, the same Form T183CORP, and ' + PRICE + '. The figures '
       'here illustrate how the rules apply and are not drawn from a client '
       'file.'),
 faq=[
  ('Does the year-end change what a nil return costs?',
   'No. The fee is ' + PRICE + ' on any year-end. The date moves the '
   'deadline, not the price.'),
  ('Is December 31 the default year-end?',
   'No. December 31 is a convention rather than a rule. Nothing is allocated '
   'at incorporation and the articles of incorporation do not set a date '
   'either.'),
  ('Then what sets my year-end?',
   'The first T2 return filed. From then on the date is on the record and it '
   'recurs annually.'),
  ('When is the return due on a December 31 year-end?',
   'June 30 the following year, which is simply the six-month rule applied '
   'to December 31.'),
  ('How do I work out the date on another year-end?',
   'Count six months to the same day number in the later month. An August 31 '
   'year-end falls on the last day of February, because there is no '
   'thirty-first of February.'),
  ('Can I still pick my year-end?',
   'Only until the first return is filed. If no return has ever been filed '
   'the date is still unsettled, and the first one filed settles it.'),
  ('How long can the first tax year be?',
   'Up to 53 weeks, which is 371 days counting the day of incorporation. A '
   'year-end chosen further out than that is not available, so the first '
   'year has to end earlier.'),
  ('Can I change the year-end later?',
   'Changing it needs the written approval of the Canada Revenue Agency. It '
   'is not something a corporation does by filing on a different date.'),
  ('Does a short year get an earlier deadline?',
   'No. The six months are counted from the day the short year ends, exactly '
   'as they are for a full one.'),
  ('What happens if I file on the wrong year-end?',
   'A year-end that does not match the one on the record gets the '
   'transmission rejected, which is one of the more common reasons a return '
   'does not go through first time.'),
  ('Is a December 31 year-end simpler to keep?',
   'It lines up with the calendar most people already keep, so the records '
   'are wanted alongside everything else dated December 31. That is '
   'convenience, not a rule, and it changes nothing about the return.'),
  ('Do the schedules depend on the year-end?',
   'No. The schedules follow what sits on the corporation&rsquo;s books, not '
   'the date the year ended.'),
  ('Does a non-calendar year-end make a nil return harder to file?',
   'No. The work is the same and the route is the same. Only the dates '
   'differ.'),
  ('Which year-end should a new corporation pick?',
   'That is a decision for the corporation and its own circumstances. What '
   'matters here is that the choice is made before the first return goes in, '
   'and that it sits inside the 53-week limit.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'nil-t2-deadline-calculator/">nil T2 deadline '
   'calculator</a>, which dates the return from any year-end you give it.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7e-manifest.json')
