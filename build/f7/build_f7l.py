#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 12: /compare/nil-t2-vs-nil-gst-hst-return/

Why this page
-------------
Not in Appendix A, which lists 13 of its stated 20 F7 URLs. It fills part of
that gap, and line 1254's blog keyword list carries "nil gst hst return", so
the subject is already in the plan's own vocabulary.

It is also the comparison that corrects the most expensive misunderstanding on
the site: that a quiet year produces one filing. On an open GST/HST account a
quiet year produces four or twelve, because the reporting period is often
quarterly or monthly.

The price cell declines, and $350.00 would be wrong here
--------------------------------------------------------
Under the November 5 ruling the GST/HST column carries a statement. It must not
carry $350.00: that figure is the sister firm's published fee for a tax year
that is not nil, which is a T2 matter. /guides/cra-accounts-on-a-dormant-
corporation/ is precise about GST/HST work -- it is "handled by Gondaliya CPA
Professional Corporation at gondaliyacpa.ca rather than priced here", so there
is no published figure to state and the page says so instead of reaching for
the nearest one.

Agreeing with what is already published
---------------------------------------
From /guides/cra-accounts-on-a-dormant-corporation/:

  "A corporation has one business number, and that number carries separate
   program accounts."
  "The obligation follows the account, not the activity."
  "The Canada Revenue Agency expects a return on an open account because the
   account is open. It does not wait to see whether anything happened."
  "Each was opened for a reason, and each stays open until somebody closes it,
   whatever happened to the reason."
  "An open GST/HST account expects a return for every reporting period, and a
   period with no sales and no tax collected is reported as a nil return
   rather than skipped."
  "the reporting period is often quarterly or monthly, so a single forgotten
   account generates four or twelve outstanding returns"
  "Being dormant is not a status you register. There is no form that tells the
   Agency a corporation has gone quiet and no notification that pauses an
   account."
  "One form closes a payroll account and the same form closes a GST/HST
   account. It is the only thing that ends the obligations on either: not
   inactivity, not telling an accountant, not letting the returns lapse."
  "Closing an account today does not file the [periods that fell due]."
  "the order is the outstanding returns first, then the closure. A closure
   stacked on top of unfiled periods leaves the unfiled periods exactly where
   they were."
  "There is no form that closes it while the corporation exists... the account
   is the corporation's relationship with the Agency for income tax, and it
   ends when the corporation does."
  "Every tax year gets a return until the corporation is dissolved, and a year
   with no activity gets one reporting $0.00 rather than no return at all."
  "Net GST/HST is money collected from customers. Neither was ever the
   corporation's to keep, and amounts of that kind can be assessed against a
   corporation's directors."
  "Corporate income tax | The corporation's own liability | No, not on its
   own"
  The fee boundary table: "A GST/HST return, nil or otherwise | No".
  "Where any of those are needed, they are handled by Gondaliya CPA
   Professional Corporation at gondaliyacpa.ca rather than priced here."

What is not on this page
------------------------
The payroll account and the T4 information return are in the same guide and
are deliberately left out. This comparison is two accounts, not three, and
/compare/nil-t2-vs-ontario-annual-return-vs-federal-annual-return/ is a
separate planned URL for the multi-way version. The cards name payroll and the
T4 among what sits outside the fee, which is a boundary statement rather than a
comparison of them.
"""
import build_f7
from build_f7 import T, G, COST, PRICE, check, write

build_f7.TODAY, build_f7.ISO = 'November 5, 2026', '2026-11-05'

DECLINE = ('Not offered. We file nil T2 returns only, and GST/HST work is '
           'handled at gondaliyacpa.ca rather than priced here')

PRICE_ROWS = [
 ('Our published fee for a quiet year', PRICE, DECLINE, True),
 ('What the fee covers on this account',
  'One T2 return for one corporation for one tax year',
  'Nothing. A GST/HST return, nil or otherwise, sits outside the fee', True),
]

FEATURE_ROWS = [
 ('What created the obligation',
  'The corporation exists',
  'The corporation registered for GST/HST', True),
 ('Whether having no activity removes it',
  'No. Every tax year gets a return until the corporation is dissolved',
  'No. The obligation follows the open account rather than the activity',
  False),
 ('How many filings one quiet year produces',
  'One, for the tax year',
  'One for every reporting period, so four or twelve where the period is '
  'quarterly or monthly', True),
 ('What a period with nothing in it is reported as',
  'A return reporting $0.00',
  'A nil return rather than a skipped period', False),
 ('How the obligation ends',
  'It ends with the corporation. No form closes the account while the '
  'corporation exists',
  'Form RC145 closes the account, and it is the only thing that ends the '
  'obligation', True),
 ('Whether closing the account files the outstanding periods',
  'Does not arise, because the account is not closed',
  'No. A closure does not file what fell due while the account was open',
  True),
 ('Whether the amounts can reach a director personally',
  'Corporate income tax, on its own, cannot',
  'Net GST/HST can, because it was money collected from customers', True),
 ('Where it sits in the order of work',
  'First, with the outstanding years filed oldest first',
  'Next, with the outstanding periods filed before the account is closed',
  True),
]

PAGE = dict(
 col_a='Nil T2 Return', col_b='Nil GST/HST Return',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 stamp=('Our own <a href="' + COST + '">published fee</a> is for the nil T2. '
        'We file nil T2 returns only, so the GST/HST column carries no fee of '
        'ours.'),
 disclosure=('This comparison sets the return we file against a filing on a '
             'different Canada Revenue Agency account, and names no other '
             'provider. Where a comparison on this site does name one, it '
             'states that provider&rsquo;s published prices and published '
             'features only.'),
 table_note=('Eight rows differ and two do not, and the two that do not are '
             'the point. Neither obligation goes away because nothing '
             'happened. The Agency expects a return on an open account '
             'because the account is open, and it does not wait to see '
             'whether anything was done.'),
 slug='nil-t2-vs-nil-gst-hst-return',
 title='Nil T2 vs Nil GST/HST Return | Two Accounts',
 h1='Nil T2 vs a Nil GST/HST Return',
 h1_pre='Nil T2 vs a ', h1_span='Nil GST/HST Return',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='nil t2 vs nil gst hst return',
 meta=('One business number, two separate accounts. A quiet year produces one '
       'T2 and, on an open GST/HST account, a return for every reporting '
       'period.'),
 seo_title='Nil T2 vs Nil GST/HST Return',
 seo_desc=('Two separate Canada Revenue Agency accounts, two separate '
           'filings. Why a quiet year can produce twelve GST/HST returns and '
           'only one T2.'),
 answer=('They are filings on two different accounts. A corporation has one '
         'business number carrying separate program accounts, and the '
         'obligation follows the account rather than the activity: the Agency '
         'expects a return on an open account because the account is open. '
         'The T2 covers the tax year, one return, at ' + PRICE + '. An open '
         'GST/HST account expects a return for every reporting period, which '
         'is often quarterly or monthly, so one quiet year can produce four '
         'or twelve of them. We file the T2 side only.'),
 cta2=('Check an Open GST/HST Account', T + 'gst-hst-nil-filing-checker/'),
 lead=[('One Business Number, Separate Accounts',
        ['<p>A corporation has one business number, and that number carries '
         'separate program accounts. The corporate income tax account is the '
         'one everybody knows about, because it is the one the T2 is filed '
         'against. It is rarely the one that causes the trouble.</p>',
         '<p>A corporation that ever registered for GST/HST has a GST/HST '
         'account. It was opened for a reason, and it stays open until '
         'somebody closes it, whatever happened to the reason. Being dormant '
         'is not a status you register: there is no form that tells the '
         'Agency a corporation has gone quiet and no notification that pauses '
         'an account.</p>',
         '<p>So the comparison is not really between two kinds of nil return. '
         'It is between one filing a year and a filing every reporting '
         'period, on an account most owners have stopped thinking about.</p>']),
       ],
 detail=dict(
  h2='The Obligation Follows the Account, Not the Activity',
  intro=('That one sentence explains almost every unpleasant surprise a '
         'dormant corporation gets:'),
  items=[
   'The Canada Revenue Agency expects a return on an open account because the '
   'account is open. It does not wait to see whether anything happened.',
   'An open GST/HST account expects a return for every reporting period, and '
   'a period with no sales and no tax collected is reported as a nil return '
   'rather than skipped.',
   'The reporting period is often quarterly or monthly, so a single forgotten '
   'account generates four or twelve outstanding returns where the T2 '
   'generates one.',
   'Form RC145 closes a GST/HST account, and it is the only thing that ends '
   'the obligation: not inactivity, not telling an accountant, not letting '
   'the returns lapse.',
   'A closure is not retroactive. Closing an account today does not file the '
   'periods that fell due while it was open.',
   'So the order is the outstanding returns first and the closure second. A '
   'closure stacked on top of unfiled periods leaves the unfiled periods '
   'exactly where they were.',
   'The corporate income tax account is different again: no form closes it '
   'while the corporation exists, because it ends when the corporation does.',
  ],
  warn=('Net GST/HST was money collected from customers, so amounts of that '
        'kind can be assessed against a corporation&rsquo;s directors '
        'personally. Corporate income tax, on its own, cannot. That is the '
        'practical reason an unused GST/HST account is worth closing rather '
        'than ignoring.'),
  close=('The <a href="' + T + 'gst-hst-nil-filing-checker/">GST/HST nil '
         'filing checker</a> tests whether an account is in that position, '
         'the <a href="' + T + 'cra-account-closure-sequencer/">CRA account '
         'closure sequencer</a> puts the steps in order for a particular '
         'corporation, and the '
         '<a href="' + G + 'cra-accounts-on-a-dormant-corporation/">complete '
         'guide to CRA accounts on a dormant corporation</a> covers every '
         'account and every date.')),
 band=('The T2 Side Is What We File',
       'Nil T2 filing covers the corporate income tax account for a quiet '
       'year, at ' + PRICE + '. The GST/HST account is a separate filing on a '
       'separate schedule.'),
 cards=[('Reviewed by a CPA',
         'The return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('What the fee covers',
         'The T2 itself, GIFI Schedules 100, 125 and 141 where required, '
         'Schedule 50, Schedule 24 on a first return, Schedule 8 and loss '
         'continuity, and electronic transmission.'),
        ('What sits outside it',
         'A GST/HST return nil or otherwise, a payroll remittance, the T4 '
         'information return, closing an account with Form RC145 and the '
         'registry annual return. Those are handled at gondaliyacpa.ca rather '
         'than priced here.')],
 case=('A corporation quiet for four years, with a GST/HST account nobody '
       'closed and a quarterly reporting period',
       'On the corporate income tax account it owes four returns, one for '
       'each tax year, each reporting $0.00 and each ' + PRICE + '. On the '
       'GST/HST account it owes sixteen, because a quarterly period produces '
       'four a year and the account stayed open throughout. Nothing was sold '
       'and no tax was collected in any of them, which changes none of it: '
       'the obligation followed the open account. Closing the account now '
       'would not file the sixteen periods, so they come first and Form RC145 '
       'comes after. The T2 side is what we file; the GST/HST side is handled '
       'at gondaliyacpa.ca. The figures here illustrate how the rules apply '
       'and are not drawn from a client file.'),
 faq=[
  ('Does a dormant corporation still file GST/HST returns?',
   'While the account is open, yes. A period with no sales is reported as a '
   'nil return rather than skipped, because the obligation follows the open '
   'account rather than the activity.'),
  ('Do you file nil GST/HST returns?',
   'No. We file nil T2 returns only. GST/HST work is handled by Gondaliya CPA '
   'Professional Corporation at gondaliyacpa.ca rather than priced here.'),
  ('Is a GST/HST return included in the ' + PRICE + ' fee?',
   'No. The fee covers one nil T2 return for one corporation for one tax '
   'year. A GST/HST return, nil or otherwise, sits outside it.'),
  ('Why does one quiet year produce more than one GST/HST return?',
   'Because the obligation runs per reporting period rather than per year, '
   'and the period is often quarterly or monthly. That is four or twelve '
   'returns for a year in which nothing happened.'),
  ('Does filing the T2 cover the GST/HST account?',
   'No. They are separate program accounts on the same business number, each '
   'with its own filings and its own dates.'),
  ('How do I stop the GST/HST returns falling due?',
   'Form RC145 closes the account. It is the only thing that ends the '
   'obligation: not inactivity, not telling an accountant, not letting the '
   'returns lapse.'),
  ('If I close the account, do the outstanding periods go away?',
   'No. A closure does not file what fell due while the account was open, so '
   'the outstanding returns come first and the closure second.'),
  ('Can I just tell the Agency the corporation is dormant?',
   'Being dormant is not a status you register. There is no form that says a '
   'corporation has gone quiet and no notification that pauses an account.'),
  ('Can the corporate income tax account be closed the same way?',
   'No. No form closes it while the corporation exists, because the account '
   'is the corporation&rsquo;s relationship with the Agency for income tax '
   'and it ends when the corporation does.'),
  ('Why is an unused GST/HST account worth closing?',
   'Because net GST/HST was money collected from customers, and amounts of '
   'that kind can be assessed against a corporation&rsquo;s directors '
   'personally.'),
  ('Can corporate income tax reach a director personally?',
   'Not on its own. That is the difference between the two accounts on this '
   'page.'),
  ('Which should be dealt with first?',
   'The outstanding returns on both accounts, then the closure. A closure '
   'files nothing, so stacking it on top of unfiled periods leaves them '
   'exactly where they were.'),
  ('Does an open account block a dissolution?',
   'A clearance certificate request rests on a complete filing record, so an '
   'outstanding period blocks it. Dissolving anyway leaves the tax years open '
   'behind the corporation.'),
  ('What if there is a payroll account as well?',
   'That is a third account with its own filings, including remittances and a '
   'T4 information return after each calendar year. Form RC145 closes it '
   'too.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'gst-hst-nil-filing-checker/">GST/HST nil filing '
   'checker</a>, which tests whether an open account is generating returns '
   'nobody is filing.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7l-manifest.json')
