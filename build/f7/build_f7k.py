#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 11: /compare/nil-t2-vs-loss-t2/

Why this page
-------------
Line 1242's keyword list carries "nil t2 vs loss t2". It is not in Appendix A,
which lists 13 of its stated 20 F7 URLs; this fills part of that gap on the
same footing as the three off-appendix pages logged earlier.

/compare/nil-t2-vs-zero-return/ (page 7) deliberately left this subject alone
and said so in its docstring: a year with activity that nets to nothing is this
page's business, not that one's. This is where that boundary is honoured.

Both price cells are figures, and neither is a decline
-----------------------------------------------------
Unlike pages 8, 9 and 10, this comparison needs no decline cell. A loss year is
not nil, and the plan already publishes where it goes and at what price: the
sister firm at gondaliyacpa.ca, $350.00 plus HST per year. So both columns
carry our own published fees and the November 5 ruling does not arise.

Hard rule 8 is satisfied in the card block and again in the warning: a
corporation that claims expenses is not nil.

Agreeing with what is already published
---------------------------------------
/guides/schedule-8-and-loss-continuity/ has a section headed "A Nil Year Is
Not a Loss Year", which is this page's whole thesis already written:

  "These two are often confused. A nil year had no activity at all, so net
   income is nil and no loss arises. A loss year had real expenses exceeding
   real revenue, which creates a non-capital loss to carry forward."
  "A corporation that claims expenses is not nil, and this service is for a
   corporation with no activity in the tax year."
  "Schedule 8 is the capital cost allowance schedule."
  "Loss continuity is the running record of the losses a corporation has and
   has not yet used. It is reported on Schedule 4, Corporation Loss Continuity
   and Application, not on Schedule 8."
  "The two are filed together and are often spoken of as one, but they are
   separate schedules. Schedule 8 is the asset pools; Schedule 4 is the
   losses."
  "Capital cost allowance is discretionary. A corporation may claim anything
   from nil up to the maximum the class allows, and the choice is made each
   year."
  "On a nil year the usual answer is to claim nil. Claiming capital cost
   allowance against no income creates a non-capital loss, and a non-capital
   loss expires."
  "A non-capital loss is the ordinary kind, from expenses exceeding revenue. A
   net capital loss comes from selling capital property for less than it
   cost."
  Non-capital loss: 3 years back, 20 years forward. Net capital loss: 3 years
  back, indefinitely forward. Undepreciated capital cost: "Indefinitely, while
  the pool exists."
  "Each class is a pool rather than a list of individual assets."
  "A year that was never filed is a gap in the record."
  "Because continuity only runs forwards."
  "Both are included in the fee of $300.00 plus HST per tax year where the
   corporation has anything to record on them."

The schedule numbering is the detail most easily got wrong
----------------------------------------------------------
The site's own guide slug is `schedule-8-and-loss-continuity`, and the fee
table line reads "Schedule 8 and loss continuity", which invites writing that
Schedule 8 carries the losses. It does not: Schedule 8 is capital cost
allowance and Schedule 4 is Corporation Loss Continuity and Application. The
guide is explicit that they are separate and says why they get conflated. This
page states both numbers correctly and keeps them apart in their own rows.
"""
import build_f7
from build_f7 import T, G, COST, PRICE, check, write

build_f7.TODAY, build_f7.ISO = 'November 5, 2026', '2026-11-05'

OVERFLOW = ('Not nil. Prepared by Gondaliya CPA Professional Corporation at '
            'gondaliyacpa.ca at $350.00 plus HST per year')

PRICE_ROWS = [
 ('Our published fee for the tax year', PRICE, OVERFLOW, True),
 ('A second tax year', PRICE,
  'The same, at $350.00 plus HST per year', True),
]

FEATURE_ROWS = [
 ('What happened in the tax year',
  'No revenue, no expenses, no income of any kind and no disposition of '
  'property',
  'Real expenses exceeding real revenue', True),
 ('Net income for the year',
  'Nil, so no loss arises',
  'A non-capital loss to carry forward', True),
 ('Whether this service covers it',
  'Yes, at ' + PRICE,
  'No. A corporation that claims expenses is not nil', True),
 ('Schedule 4, Corporation Loss Continuity and Application',
  'Filed where there is anything to record. The running total usually carries '
  'forward unchanged',
  'Filed, with the year&rsquo;s new non-capital loss added to the record',
  True),
 ('Schedule 8, capital cost allowance',
  'Filed where the corporation holds depreciable property, usually claiming '
  'nil',
  'Filed, and the size of the claim is a decision taken against real '
  'revenue', True),
 ('How long a non-capital loss lasts',
  'None arises, so nothing is carried and nothing expires',
  'Twenty years forward and three years back', True),
 ('What happens to the capital cost allowance pool',
  'It carries forward, reduced by what is claimed and by anything sold',
  'The same pool, on the same rules', False),
 ('Why the years are filed oldest first',
  'Each return&rsquo;s closing balances are the next one&rsquo;s opening '
  'balances',
  'The same, because continuity only runs forwards', False),
]

PAGE = dict(
 col_a='Nil T2 Return', col_b='Loss T2 Return',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 table_note=('Six rows differ and two do not. The two that do not are the '
             'mechanics both years share: pools and continuity run forwards '
             'either way. What separates them is simpler than the schedules '
             'suggest. A nil year had no activity at all, so net income is '
             'nil and no loss arises. A loss year had real expenses '
             'exceeding real revenue, which creates a non-capital loss to '
             'carry forward.'),
 slug='nil-t2-vs-loss-t2',
 title='Nil T2 vs Loss T2 | A Quiet Year Is Not a Loss',
 h1='Nil T2 vs a Loss T2',
 h1_pre='Nil T2 vs ', h1_span='a Loss T2',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='nil t2 vs loss t2',
 meta=('A nil year had no activity, so no loss arises. A loss year had real '
       'expenses exceeding real revenue. Only one of them is a nil return.'),
 seo_title='Nil T2 vs Loss T2 | Not the Same Year',
 seo_desc=('A quiet year produces no loss, because nothing happened. What a '
           'loss year produces instead, which schedules carry it, and which '
           'of the two this service files.'),
 answer=('A nil year and a loss year are not the same thing, and only one of '
         'them is a nil return. A nil year had no activity at all, so net '
         'income is nil and no loss arises. A loss year had real expenses '
         'exceeding real revenue, which creates a non-capital loss to carry '
         'forward twenty years. A corporation that claims expenses is not '
         'nil, so a loss year is not covered by this service: it is prepared '
         'by Gondaliya CPA Professional Corporation at gondaliyacpa.ca at '
         '$350.00 plus HST per year. The quiet year is ' + PRICE + '.'),
 cta2=('Check Your Loss Position',
       T + 'loss-continuity-on-a-nil-return-checker/'),
 lead=[('A Quiet Year Produces No Loss',
        ['<p>These two are often confused, and the confusion is reasonable: '
         'both years end with no tax to pay. They get there differently. A '
         'nil year had no revenue, no expenses, no income of any kind and no '
         'disposition of property, so net income is nil and there is nothing '
         'to carry anywhere.</p>',
         '<p>A loss year had real figures that went the wrong way. Expenses '
         'exceeded revenue, which creates a non-capital loss, and that loss '
         'is an asset of a kind: it can be carried twenty years forward or '
         'three years back against income in another year.</p>',
         '<p>That is also why the two are priced differently. A corporation '
         'that claims expenses is not nil, so a loss year is not what this '
         'service files. It is prepared at gondaliyacpa.ca at $350.00 plus '
         'HST per year, and we say so before anything is charged.</p>']),
       ],
 detail=dict(
  h2='What the Two Schedules Actually Carry',
  intro=('The numbering is the part most easily got wrong, because the two '
         'schedules are filed together and spoken of as one:'),
  items=[
   'Schedule 8 is the capital cost allowance schedule. It records the '
   'corporation&rsquo;s depreciable property, the class each asset sits in, '
   'and how much depreciation is claimed for the year.',
   'Loss continuity is reported on Schedule 4, Corporation Loss Continuity '
   'and Application, not on Schedule 8.',
   'Capital cost allowance is discretionary. A corporation may claim anything '
   'from nil up to the maximum the class allows, and the choice is made each '
   'year.',
   'On a nil year the usual answer is to claim nil, because claiming against '
   'no income creates a non-capital loss, and a non-capital loss expires.',
   'Leaving the claim unmade keeps the undepreciated capital cost in the '
   'pool, where it lasts indefinitely while the pool exists.',
   'A non-capital loss is the ordinary kind, from expenses exceeding revenue, '
   'and runs twenty years forward and three years back. A net capital loss '
   'comes from selling capital property for less than it cost, and carries '
   'forward indefinitely.',
   'A year that was never filed is a gap in the record, so the continuity has '
   'to be rebuilt before the later years can be assessed correctly.',
  ],
  warn=('A corporation that claims expenses is not nil. This service is for a '
        'corporation with no activity in the tax year; a loss year is '
        'prepared by Gondaliya CPA Professional Corporation at '
        'gondaliyacpa.ca at $350.00 plus HST per year.'),
  close=('The <a href="' + T + 'loss-continuity-on-a-nil-return-checker/">'
         'loss continuity checker</a> takes what carries forward on a quiet '
         'year, the <a href="' + T + 'schedule-8-cca-requirement-checker/">'
         'Schedule 8 requirement checker</a> settles whether the corporation '
         'has depreciable property at all, and the '
         '<a href="' + G + 'schedule-8-and-loss-continuity/">complete guide '
         'to Schedule 8 and loss continuity</a> sets out both schedules in '
         'full.')),
 band=('The Quiet Year Is the One We File',
       'Nil T2 filing covers a tax year with no activity, at ' + PRICE
       + ', with Schedule 4 and Schedule 8 where there is anything to record '
       'on them.'),
 cards=[('Reviewed by a CPA',
         'The return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('Continuity is recorded, not ignored',
         'Schedule 8 and loss continuity are inside the fee where the '
         'corporation has anything to record on them, so the pools and the '
         'running loss total carry forward correctly.'),
        ('What is not inside the fee',
         'A loss year, because a corporation that claims expenses is not nil. '
         'Nor is a holding corporation with investment income, a rental '
         'corporation or a corporation that paid or received a dividend. '
         'Those are handled at gondaliyacpa.ca at $350.00 plus HST per '
         'year.')],
 case=('A corporation still holding a vehicle and a computer from its trading '
       'days, quiet for the tax year',
       'It has depreciable property, so Schedule 8 is in play even though '
       'nothing happened. Claiming capital cost allowance against no income '
       'would create a non-capital loss, and that loss expires twenty years '
       'later; claiming nil keeps the undepreciated capital cost in the pool, '
       'where it lasts as long as the pool does. So the usual answer on a '
       'quiet year is to claim nil, and the year stays a nil return at '
       + PRICE + ' rather than becoming a loss year. The choice is made again '
       'each year, because capital cost allowance is discretionary. The '
       'figures here illustrate how the rules apply and are not drawn from a '
       'client file.'),
 faq=[
  ('Is a nil year the same as a loss year?',
   'No. A nil year had no activity, so net income is nil and no loss arises. '
   'A loss needs real expenses exceeding real revenue.'),
  ('Do you file a loss year?',
   'No. A corporation that claims expenses is not nil. A loss year is '
   'prepared by Gondaliya CPA Professional Corporation at gondaliyacpa.ca at '
   '$350.00 plus HST per year.'),
  ('Can I claim my expenses on a nil return to create a loss?',
   'A year with expenses in it is not a nil year. Claiming them makes the '
   'return a loss return, which is a different service at a different '
   'price.'),
  ('How long does a non-capital loss last?',
   'Twenty years forward and three years back. A net capital loss carries '
   'forward indefinitely and back three years.'),
  ('Which schedule carries the losses?',
   'Schedule 4, Corporation Loss Continuity and Application. Schedule 8 is '
   'the capital cost allowance schedule, and the two are filed together, '
   'which is why they are often spoken of as one.'),
  ('Does a nil year need Schedule 8 at all?',
   'Only where the corporation holds depreciable property. One that still has '
   'equipment, a vehicle or a computer from its trading days does, even in a '
   'year when nothing happened.'),
  ('Should I claim capital cost allowance on a quiet year?',
   'Usually nil. Claiming against no income creates a non-capital loss that '
   'expires, while claiming nothing keeps the undepreciated capital cost in '
   'the pool, where it does not.'),
  ('Is that choice fixed for good?',
   'No. Capital cost allowance is discretionary and the choice is made each '
   'year, anywhere from nil up to the maximum the class allows.'),
  ('What happens to the pool if I claim nothing?',
   'It stays. The undepreciated capital cost remains in the pool '
   'indefinitely, while the pool exists, and carries forward to a future '
   'year.'),
  ('Are Schedule 4 and Schedule 8 included in your fee?',
   'Yes, where the corporation has anything to record on them. Both are '
   'inside ' + PRICE + '.'),
  ('What does an unfiled year do to the continuity?',
   'It leaves a gap in the record. The losses and pools have no filed return '
   'carrying them forward, so the continuity has to be rebuilt before the '
   'later years can be assessed correctly.'),
  ('Why are several years filed oldest first?',
   'Because continuity only runs forwards. Each return&rsquo;s closing '
   'balances are the next one&rsquo;s opening balances.'),
  ('Can a corporation have nil years and loss years mixed together?',
   'Yes. Each tax year is assessed on its own, so a quiet year and a trading '
   'year that lost money can sit side by side in the same catch-up.'),
  ('What if I am not sure which kind of year I had?',
   'Any revenue, any expense, income of any kind or a disposition of property '
   'takes the year out of nil. The amount is irrelevant to that test.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'loss-continuity-on-a-nil-return-checker/">loss '
   'continuity checker</a>, which takes what carries forward on a quiet '
   'year.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7k-manifest.json')
