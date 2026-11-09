#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 10: /compare/diy-vs-cpa-nil-t2/

Why this page, and the one claim it must not make
-------------------------------------------------
Appendix A line 3272 lists it, and line 1242's keyword list carries "diy t2
software vs cpa filed nil t2". It is the page in this family most exposed to
Rule 217, because the obvious way to write it is to imply a corporation needs
a CPA. It does not, and our own published answer says so.

From /answers/can-i-file-a-nil-t2-myself-without-an-accountant/:

  "What a corporation takes on by filing itself is the GIFI coding, the
   schedule selection and the year-end accuracy. Our fee covers a CPA
   preparing and reviewing those and transmitting the return, which is what
   the fee buys rather than something the rules demand."

That last clause is the spine of this page. It is quoted in the warning block
verbatim, and the first comparison row says "No" on both sides to whether the
rules require a CPA. A page that sold necessity would contradict a page
already live on the same site, which is the test that matters more than the
gate: the site has to agree with itself.

Two of the ten rows deliberately do not differ
----------------------------------------------
Row 1, whether the rules require a CPA: no on both sides. Row 6, electronic
filing for a tax year beginning after 2023: mandatory on both sides. Those two
are the honest frame, and burying them would be the Rule 217 breach rather
than any individual adjective.

The price column, under the November 5 ruling
---------------------------------------------
Both left-hand price cells decline. We do not sell a DIY route, so there is no
fee of ours to state, and software prices are a third party's: not published by
us, not approved, and barred from an F7 page by gate.py's money allowlist in
any case. check() holds the decline cells to carrying no figure.

Agreeing with what is already published
---------------------------------------
From /guides/how-to-file-a-nil-t2-return/:

  "This is the first step and the one that most often goes wrong. The Canada
   Revenue Agency already holds a fiscal year-end for the corporation, taken
   from the incorporation record, and the return must carry that same date."
  "Owners usually remember the date the business started trading rather than
   the date on the incorporation record. A year-end that differs from the one
   the Agency holds rejects the transmission."
  "That review is what the fee buys. A corporation filing on its own with
   commercial tax software takes on the same checks."

From /guides/zero-activity-corporate-tax-returns/:

  "A zero-activity return is not an empty return."
  "The balance sheet is rarely all zeroes. Share capital issued on
   incorporation, a shareholder loan and retained earnings carried forward all
   sit on Schedule 100 whether or not anything happened during the year."
  "Interest credited to a corporate account is investment income whatever the
   amount."

From /guides/mandatory-t2-electronic-filing/:

  "For tax years beginning after 2023, electronic filing of the T2 is
   mandatory for virtually all corporations."
  "One corrected transmission is included in the fee where the Agency rejects
   the first one."

What is not on this page
------------------------
The $1,000.00 paper charge and the $100.00 preparer charge are not here. Both
routes transmit electronically, so neither arises, and the preparer charge
attaches to a preparer filing on paper where electronic filing was required --
a self-filer is not obviously within it, and the plan does not say. Asserting
either way would be inventing law to make a comparison land.
/compare/paper-t2-vs-efile-t2/ owns those figures.

Nothing is said about whether Form T183CORP is used on a self-filed return.
The form authorizes a third party to transmit, so the answer is probably that
it is not, but no page on this site says so and the plan does not either. An
unsourced row is worse than a missing one.
"""
import build_f7
from build_f7 import T, G, BASE, COST, PRICE, check, write

build_f7.TODAY, build_f7.ISO = 'November 5, 2026', '2026-11-05'

ANSWERS = build_f7.SITE + '/answers/'
DECLINE = 'Not offered. We file nil T2 returns only'

PRICE_ROWS = [
 ('Our published fee for a quiet year', DECLINE, PRICE, True),
 ('A second quiet tax year', DECLINE, PRICE, True),
]

FEATURE_ROWS = [
 ('Whether the rules require a CPA',
  'No. A corporation may file its own return',
  'No. CPA preparation is what the fee buys rather than something the rules '
  'demand', False),
 ('Who does the GIFI coding',
  'The corporation',
  'A CPA Ontario member, from what sits on the books', True),
 ('Who selects the schedules',
  'The corporation',
  'A CPA Ontario member: GIFI Schedules 100, 125 and 141 where required, '
  'Schedule 50, Schedule 24 on a first return, Schedule 8 and loss '
  'continuity', True),
 ('Who checks the fiscal year-end against the Agency&rsquo;s record',
  'The corporation',
  'Checked before transmission, because a year-end that differs from the one '
  'the Agency holds rejects the transmission', True),
 ('Review before the return is sent',
  'Whatever the corporation does for itself. Commercial tax software takes on '
  'the same checks',
  'CPA review before transmission', True),
 ('Electronic filing for a tax year beginning after 2023',
  'Mandatory, through certified software',
  'Mandatory, by a registered EFILE electronic filer', False),
 ('If the first transmission is refused',
  'The corporation reads the error and corrects the return itself',
  'One corrected transmission is included in the fee', True),
 ('Several unfiled years',
  'Each is its own return for its own tax year, prepared oldest first by the '
  'corporation',
  'Each is its own return for its own tax year, prepared oldest first, at '
  + PRICE, True),
]

PAGE = dict(
 col_a='Filing It Yourself', col_b='CPA Filed',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 stamp=('Our own <a href="' + COST + '">published fee</a> is for the return '
        'we prepare. We do not sell a self-filing route, so the left column '
        'carries no fee of ours and no third party&rsquo;s.'),
 disclosure=('This comparison sets filing a return yourself against the '
             'service we sell, and names no other provider and no software. '
             'Where a comparison on this site does name one, it states that '
             'provider&rsquo;s published prices and published features '
             'only.'),
 table_note=('Two rows do not differ, and they are the two worth reading '
             'first. The rules do not require a CPA: a corporation may file '
             'its own return. And electronic filing is mandatory either way '
             'for a tax year beginning after 2023. What differs is who does '
             'the GIFI coding, who selects the schedules, who checks the '
             'year-end, and what happens when a transmission is refused.'),
 slug='diy-vs-cpa-nil-t2',
 title='DIY vs CPA Nil T2 | What Each Route Involves',
 h1='DIY Filing vs a CPA-Filed Nil T2',
 h1_pre='DIY Filing vs a ', h1_span='CPA-Filed Nil T2',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='diy vs cpa nil t2',
 meta=('A corporation may file its own nil T2. What it takes on by doing so '
       'is the GIFI coding, the schedule selection and the year-end '
       'accuracy.'),
 seo_title='DIY vs CPA Nil T2 | What Each Involves',
 seo_desc=('The rules do not require a CPA. What a corporation takes on by '
           'filing its own nil T2, and what the fee covers instead.'),
 answer=('A corporation may file its own nil T2. Nothing in the rules '
         'requires a CPA, and our own answer to that question says so: CPA '
         'preparation is what the fee buys rather than something the rules '
         'demand. What a corporation takes on by filing itself is the GIFI '
         'coding, the schedule selection and the year-end accuracy. '
         'Electronic filing is mandatory either way for a tax year beginning '
         'after 2023. Our fee is ' + PRICE + ', and it covers a CPA '
         'preparing and reviewing the return and transmitting it.'),
 cta2=('See What the Return Needs', T + 'nil-t2-document-checklist-checker/'),
 lead=[('Nothing Here Is a Requirement',
        ['<p>A corporation is entitled to file its own corporate tax return. '
         'There is no rule reserving a nil T2 for an accountant, and this '
         'page is not going to suggest there is. Our own published answer to '
         'the question puts it plainly: CPA preparation is what the fee buys '
         'rather than something the rules demand.</p>',
         '<p>So the comparison is not permission against prohibition. It is '
         'about which of three jobs the corporation does itself: the GIFI '
         'coding, the schedule selection and the year-end accuracy. A '
         'corporation filing on its own with commercial tax software takes '
         'on the same checks a CPA would run.</p>',
         '<p>One thing is the same on both sides and worth saying early. For '
         'a tax year beginning after 2023, electronic filing of the T2 is '
         'mandatory for virtually all corporations, so a self-filed return '
         'goes through certified software rather than through the post.</p>']),
       ],
 detail=dict(
  h2='The Three Jobs That Move, and Where They Go Wrong',
  intro=('These are the checks that sit with whoever prepares the return:'),
  items=[
   'The fiscal year-end is the first step and the one that most often goes '
   'wrong. The Canada Revenue Agency already holds a fiscal year-end for the '
   'corporation, taken from the incorporation record, and the return must '
   'carry that same date.',
   'Owners usually remember the date the business started trading rather than '
   'the date on the incorporation record. A year-end that differs from the '
   'one the Agency holds rejects the transmission.',
   'A zero-activity return is not an empty return. The balance sheet carries '
   'share capital issued on incorporation, any shareholder loan and retained '
   'earnings brought forward even where the income statement is all zeroes.',
   'Interest credited to a corporate account is investment income whatever '
   'the amount, so a year that looked quiet may not be one.',
   'Which schedules the return carries follows what sits on the '
   'corporation&rsquo;s books, not what kind of year it was.',
   'Where the first transmission is refused, the error has to be read, the '
   'return corrected and the transmission sent again.',
  ],
  warn=('CPA preparation is what the fee buys rather than something the rules '
        'demand. A corporation may file its own return, and nothing on this '
        'page should be read as saying otherwise.'),
  close=('Our answer to <a href="' + ANSWERS + 'can-i-file-a-nil-t2-myself-'
         'without-an-accountant/">whether a nil T2 can be filed without an '
         'accountant</a> is the short version, the '
         '<a href="' + T + 'nil-t2-document-checklist-checker/">nil T2 '
         'document checklist</a> builds the list of what the return needs, '
         'and the <a href="' + G + 'how-to-file-a-nil-t2-return/">complete '
         'guide to filing a nil T2 return</a> sets out the whole sequence '
         'either route follows. Where the question is what a provider '
         'charges rather than which route to take, the published-price '
         'pages set six of them beside our own fee: '
         '<a href="' + BASE + 'corpnilfilingfor300-vs-cloudtax/">CloudTax</a>, '
         '<a href="' + BASE + 'corpnilfilingfor300-vs-bluepeak/">BluePeak</a>, '
         '<a href="' + BASE + 'corpnilfilingfor300-vs-turbotax/">TurboTax</a>, '
         '<a href="' + BASE + 'corpnilfilingfor300-vs-t2inc/">T2inc</a>, '
         '<a href="' + BASE + 'corpnilfilingfor300-vs-taxdeep/">TaxDeep</a> '
         'and <a href="' + BASE + 'corpnilfilingfor300-vs-hr-block/">H&amp;R '
         'Block</a>.')),
 band=('What the Fee Buys',
       'A CPA preparing and reviewing the return and transmitting it as a '
       'registered EFILE electronic filer, at ' + PRICE + '.'),
 cards=[('Reviewed by a CPA',
         'The return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('The schedules are inside the fee',
         'GIFI Schedules 100, 125 and 141 where required, Schedule 50, '
         'Schedule 24 on a first return, Schedule 8 and loss continuity.'),
        ('What is not inside the fee',
         'A year that was not quiet. A holding corporation with investment '
         'income, a rental corporation and a corporation that paid or '
         'received a dividend are not nil, and those years are handled at '
         'gondaliyacpa.ca at $350.00 plus HST per year.')],
 case=('A corporation filing its own quiet year, using the date it started '
       'trading as the year-end',
       'The return is otherwise right: no revenue, no expenses, nothing '
       'disposed of, and $0.00 throughout the income statement. The '
       'transmission is refused, because the Canada Revenue Agency holds a '
       'fiscal year-end taken from the incorporation record and the return '
       'carries a different date. A refused transmission is not a filed '
       'return, so the tax year stays exactly as open as it was. Nothing is '
       'charged for the refusal, and the fix is to correct the date and send '
       'it again. That is the check the fee covers rather than a rule the '
       'corporation broke: it may file its own return, and the year-end is '
       'simply the step that most often goes wrong. The figures here '
       'illustrate how the rules apply and are not drawn from a client '
       'file.'),
 faq=[
  ('Can I file my own nil T2?',
   'Yes. A corporation may file its own corporate tax return. Nothing in the '
   'rules requires a CPA.'),
  ('Then what does the fee buy?',
   'A CPA preparing and reviewing the return and transmitting it. That is '
   'what the fee buys rather than something the rules demand.'),
  ('What do I take on by filing it myself?',
   'The GIFI coding, the schedule selection and the year-end accuracy. A '
   'corporation filing on its own with commercial tax software takes on the '
   'same checks.'),
  ('Do you offer a cheaper self-filing option?',
   'No. We file nil T2 returns only, at ' + PRICE + '. There is no '
   'self-serve version of it.'),
  ('Can I post a paper return instead?',
   'For a tax year beginning after 2023, electronic filing is mandatory for '
   'virtually all corporations. Either route transmits electronically.'),
  ('What goes wrong most often on a self-filed return?',
   'The fiscal year-end. The Agency already holds one for the corporation, '
   'taken from the incorporation record, and the return must carry that same '
   'date.'),
  ('Why would the year-end be wrong?',
   'Owners usually remember the date the business started trading rather than '
   'the date on the incorporation record. A year-end that differs from the '
   'one the Agency holds rejects the transmission.'),
  ('Is a nil return just zeroes all the way through?',
   'No. A zero-activity return is not an empty return. The balance sheet '
   'carries share capital, any shareholder loan and retained earnings brought '
   'forward.'),
  ('Could my quiet year not be nil at all?',
   'It is possible. Interest credited to a corporate account is investment '
   'income whatever the amount, so a few dollars takes the year out of it.'),
  ('Which schedules does the return need?',
   'It follows what sits on the corporation&rsquo;s books rather than the '
   'kind of year it was. The nil T2 document checklist builds the list from '
   'four answers.'),
  ('What happens if my own transmission is refused?',
   'A refused transmission is not a filed return, so the year stays open. The '
   'error has to be read, the return corrected and the transmission sent '
   'again.'),
  ('Is a corrected transmission included in your fee?',
   'Yes. One corrected transmission is included where the Agency rejects the '
   'first one.'),
  ('Can I file several unfiled years myself?',
   'Yes. Each is its own return for its own tax year, prepared oldest first '
   'so the closing balances of one open the next.'),
  ('What if the year turns out not to be nil?',
   'A holding corporation with investment income, a rental corporation and a '
   'corporation that paid or received a dividend are not nil. Those years are '
   'handled by Gondaliya CPA Professional Corporation at gondaliyacpa.ca at '
   '$350.00 plus HST per year.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'nil-t2-document-checklist-checker/">nil T2 document '
   'checklist</a>, which names what the return needs before either route '
   'starts.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7j-manifest.json')
