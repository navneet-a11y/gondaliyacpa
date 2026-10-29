# -*- coding: utf-8 -*-
"""Family 9 batch 6: guides 28 to 30, which complete the family at the plan's 30.

WHY THESE THREE TOPICS

Appendix A's F9 list was exhausted at guide 27. What remained in it were
naming variants of guides already live, and building those would have put two
pages on one topic competing with each other. So all three topics here come
from the plan's approved blog-topic list instead, which means every fact they
assert still has a source in the signed plan:

  28  cra-accounts-on-a-dormant-corporation
      "Open GST/HST Accounts Still Need Nil Filings", "Closing a GST/HST
      Account With Form RC145", "Nil Payroll Accounts and Your Remittance
      Obligation". The gap this fills is real: the family had guides on the
      T2 and on the registry annual return, and nothing on the other two CRA
      accounts a business number carries, which is where a dormant
      corporation's surprise obligations actually come from.

  29  choosing-and-changing-a-fiscal-year-end
      "Your First Tax Year Cannot Exceed 53 Weeks", "Why a Wrong Year-End
      Gets Your T2 Transmission Rejected". first-year-t2-filing covers the
      first return; t2-filing-deadlines covers the dates that follow from a
      year-end. Neither covers the year-end itself as a decision: how it is
      chosen, that the first return fixes it, and what changing it costs.

  30  quebec-co17-and-alberta-at1
      "Quebec CO-17 Is a Separate Provincial Return", "Alberta AT1 Is a
      Separate Provincial Return", and hard rule 8, which requires this
      wording on any page touching either province. The family's
      provincial-and-federal-annual-returns guide is about REGISTRY annual
      returns, which is a different obligation entirely; nothing covered the
      separate provincial tax returns.

WHAT ADDING THREE GUIDES DOES TO THE OTHER 27

The sibling window is circulant: guide i links the next 12 in registry order,
wrapping. Appending three guides moves the wrap point, so the sibling list
changes on exactly 12 of the live guides, indices 15 to 26, by one to three
links each: 33 individual link swaps in all. Indices 0 to 14 are untouched,
because their twelve targets were already below the old end of the list.

Those 33 swaps are not cosmetic. Under a 30-guide registry the only guides
that link to the three new ones are indices 15 to 26, so leaving them stale
would give each new guide 0 sibling inbound against the 6(g) minimum of 12.
f9_registry.assert_regular() proves the count rather than trusting it, and
PUBLISH-f9-batch6.md records each swap as it is applied to the live page.
"""
import json, os

HERE  = os.path.dirname(os.path.abspath(__file__))
SITE  = 'https://corpnilfilingfor300.ca'
FORM  = SITE + '/form/'
HUB   = SITE + '/guides/'
A     = SITE + '/answers/'
COST  = SITE + '/pricing/nil-t2-filing-cost/'
TODAY, ISO = 'October 29, 2026', '2026-10-29'
PRICE = '$300.00 plus HST per tax year'

BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')
EFILE_PILLAR = ('Gondaliya CPA Professional Corporation is a registered EFILE electronic '
                'filer. Returns are prepared and transmitted in Canada. Credentials are '
                'never shared and never used offshore.')
LATE_QUAL = ('A true nil return carries no percentage late-filing penalty, because that '
             'penalty is a percentage of tax owing and the corporation owes $0.00. The '
             'unfiled year still stays open forever, invites a demand to file and an '
             'arbitrary assessment, blocks a clearance certificate and dissolution, and '
             'costs a non-resident-owned corporation $25.00 per day up to $2,500.00.')
NOT_NIL = ('A holding corporation with investment income, a rental corporation and a '
           'corporation that paid or received a dividend are not nil. Those are handled '
           'by Gondaliya CPA Professional Corporation at gondaliyacpa.ca at $350.00 plus '
           'HST per year.')

_pillar = open(os.path.join(HERE, 'nil-t2-return-complete-guide.html'),
               encoding='utf-8').read()
CSS = _pillar[:_pillar.index('</style>') + len('</style>')] + '\n'

FEE_ROWS = [('The T2 return', 'Including the T2 Short where the corporation qualifies'),
            ('GIFI Schedules 100, 125 and 141', 'Where they are required'),
            ('Schedule 24', 'On a first return'),
            ('Schedule 50', 'For every shareholder at 10% or more'),
            ('Schedule 8 and loss continuity', 'Recorded'),
            ('Form T183CORP package', 'With single-use secure e-signing'),
            ('CPA review', 'Before transmission'),
            ('Electronic transmission', 'By a registered EFILE electronic filer'),
            ('One corrected transmission', 'If the Agency rejects the first one'),
            ('CRA confirmation', 'Emailed within 3 business days')]

from f9_registry import REGISTRY, sibling_links, assert_regular
assert len(REGISTRY) == 30, 'batch 6 completes the family at 30'
assert_regular()

def a(href, text):
    return '<a href="%s">%s</a>' % (href, text)

def tbl(head, rows):
    out = ['<table class="ei-tbl"><thead><tr>'
           + ''.join('<th scope="col">%s</th>' % h for h in head)
           + '</tr></thead><tbody>']
    for r in rows:
        out.append('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>')
    out.append('</tbody></table>')
    return '\n'.join(out)

def sec(key, title, body, alt=False):
    cls = 'ei-section-alt' if alt else 'ei-section'
    return ('<div class="%s" id="%s"><div class="ei-wrap ei-art">\n'
            '<h2 class="ei-h2">%s</h2>\n%s\n</div></div>\n' % (cls, key, title, body))

def cta_inline():
    return ('<div class="ei-wrap"><div class="ei-cta-inline"><div><h3>Nil T2 Filing, '
            + PRICE + '</h3><p>One price for every year and every province. CPA '
            'reviewed and transmitted electronically.</p></div>'
            '<a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
            '</div></div>\n')


# ---------------------------------------------------------------------------
# 28. CRA accounts on a dormant corporation
# ---------------------------------------------------------------------------
G28 = dict(
 slug='cra-accounts-on-a-dormant-corporation',
 title='CRA Accounts on a Dormant Corporation | Complete Guide',
 h1_pre='The Complete Guide to ', h1_span='CRA Accounts on a Dormant Corporation',
 h1='The Complete Guide to CRA Accounts on a Dormant Corporation',
 eyebrow='Accounts',
 meta=('A business number carries separate accounts, and each one keeps its '
       'own obligations until it is closed. What a dormant corporation still '
       'owes, and how to end it.'),
 convert=(SITE + '/tools/cra-account-closure-sequencer/',
          'Sequence the closures'),
 kids=['do-i-need-a-business-number-to-file-a-nil-t2',
       'how-do-i-close-my-corporate-tax-account-after-dissolution',
       'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account',
       'what-happens-if-i-dont-report-a-dormant-corporation-to-cra',
       'how-do-i-know-if-my-corporation-counts-as-dormant',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive'],
 sections=[

 ('three-accounts', 'A Business Number Is Not One Account',
  '<p>A corporation has one business number, and that number carries separate '
  'program accounts. The corporate income tax account is the one everybody '
  'knows about, because it is the one the T2 is filed against. It is rarely '
  'the one that causes trouble.</p>\n'
  '<p>A corporation that ever had staff has a payroll account. One that ever '
  'registered for GST/HST has a GST/HST account. Each was opened for a reason, '
  'and each stays open until somebody closes it, whatever happened to the '
  'reason.</p>\n'
  + tbl(('Account', 'Opened because', 'What it expects', 'How it ends'),
        [('Corporate income tax', 'The corporation exists',
          'A T2 return for every tax year',
          'It ends with the corporation'),
         ('Payroll', 'Someone was going to be paid',
          'Remittances through the year and an annual T4 information return',
          'Form RC145'),
         ('GST/HST', 'The corporation registered',
          'A GST/HST return for every reporting period',
          'Form RC145')])
  + '\n<p>The ' + a(SITE + '/tools/business-number-status-checker/',
                    'business number status checker')
  + ' works through which of them a given corporation is likely to have '
  'open.</p>'),

 ('obligation-follows-account',
  'The Obligation Follows the Account, Not the Activity',
  '<p>This is the sentence that explains almost every unpleasant surprise a '
  'dormant corporation gets. The Canada Revenue Agency expects a return on an '
  'open account because the account is open. It does not wait to see whether '
  'anything happened first.</p>\n'
  '<p>So a corporation that stopped trading four years ago, paid nobody and '
  'sold nothing, still has returns falling due on every account nobody '
  'closed. Each one is a separate filing with its own deadline, and none of '
  'them is the T2.</p>\n'
  '<div class="ei-warn"><p>Being dormant is not a status you register. There '
  'is no form that tells the Agency a corporation has gone quiet and no '
  'notification that pauses an account. Nothing happens until an account is '
  'closed, and until then the dates keep arriving.</p></div>\n'
  '<p>The ' + a(HUB + 'dormant-and-inactive-corporations/',
                'guide to dormant and inactive corporations')
  + ' covers what being dormant does and does not change.</p>'),

 ('gst-hst', 'The GST/HST Account: Nil Returns Until It Is Closed', True,
  '<p>An open GST/HST account expects a return for every reporting period, and '
  'a period with no sales and no tax collected is reported as a nil return '
  'rather than skipped. The return is what the account expects; having nothing '
  'to report changes the figures on it, not whether it is filed.</p>\n'
  '<p>That catches people out twice. Once because they assume no activity '
  'means no return, and again because the reporting period is often quarterly '
  'or monthly, so a single forgotten account generates four or twelve '
  'outstanding returns a year rather than one.</p>\n'
  '<p>The ' + a(SITE + '/tools/gst-hst-nil-filing-checker/',
                'GST/HST nil filing checker')
  + ' tests whether an account is in that position, and the '
  + a(SITE + '/tools/gst-hst-account-closure-checker/',
      'GST/HST account closure checker')
  + ' covers ending it.</p>'),

 ('payroll', 'The Payroll Account: Remittances and an Annual T4',
  '<p>An open payroll account expects two separate things, which is why it is '
  'the account most often underestimated. Through the year it expects '
  'remittances, including nil ones where nobody was paid. After the calendar '
  'year it expects a T4 information return.</p>\n'
  '<p>The T4 deadline is the one that surprises accountants as well as '
  'owners, because it does not derive from the fiscal year-end at all. It '
  'reports a calendar year and is due at the end of the following February, '
  'whatever year-end the corporation uses.</p>\n'
  + tbl(('What the payroll account expects', 'Measured from', 'Due'),
        [('Remittances, including nil ones', 'Each remittance period',
          'For as long as the account is open'),
         ('The T4 information return', 'The calendar year',
          'The end of the following February')])
  + '\n<p>So a corporation with a June 30 year-end has a T2 date in December '
  'and a T4 date at the end of February, four months apart, neither derived '
  'from the other. The '
  + a(SITE + '/tools/t4-nil-filing-requirement-checker/',
      'T4 nil filing requirement checker')
  + ' gives the date, and the '
  + a(SITE + '/tools/payroll-nil-remittance-checker/',
      'payroll nil remittance checker')
  + ' covers the remittances.</p>'),

 ('rc145', 'Form RC145 Closes Both of Them', True,
  '<p>One form closes a payroll account and the same form closes a GST/HST '
  'account. It is the only thing that ends the obligations on either: not '
  'inactivity, not telling an accountant, not letting the returns lapse.</p>\n'
  '<p>Until the account is closed, nil returns and nil remittances remain due '
  'on it, and they accumulate exactly as an unfiled T2 does. A closure is '
  'also not retroactive in the way people hope. Closing an account today does '
  'not file the returns that fell due on it while it was open, and it does not '
  'clear what was owed on it.</p>\n'
  '<div class="ei-info"><p>This is why the order matters, and the order is '
  'the outstanding returns first, then the closure. A closure stacked on top '
  'of unfiled periods leaves the unfiled periods exactly where they '
  'were.</p></div>'),

 ('directors', 'Why These Two Accounts Reach the Directors',
  '<p>The corporate income tax account is the corporation&#8217;s own '
  'liability. The other two are not, and that distinction is the practical '
  'reason an unused payroll or GST/HST account is worth closing rather than '
  'ignoring.</p>\n'
  '<p>Payroll source deductions are money withheld from someone&#8217;s pay. '
  'Net GST/HST is money collected from customers. Neither was ever the '
  'corporation&#8217;s to keep, and amounts of that kind can be assessed '
  'against a corporation&#8217;s directors personally. Corporate income tax, '
  'on its own, cannot.</p>\n'
  + tbl(('Amount', 'Whose money it was', 'Can be assessed against a director'),
        [('Payroll source deductions', 'Withheld from someone&#8217;s pay',
          'Yes'),
         ('Net GST/HST', 'Collected from customers', 'Yes'),
         ('Corporate income tax', 'The corporation&#8217;s own liability',
          'No, not on its own')])
  + '\n<p>A dormant corporation rarely owes corporate income tax, because a '
  'nil year assesses at $0.00. What it may have is an open account generating '
  'exactly the amounts that do reach a director. The '
  + a(SITE + '/tools/director-liability-exposure-checker/',
      'director liability exposure checker')
  + ' sorts which is which.</p>'),

 ('income-tax-account', 'The Corporate Income Tax Account Is Different',
  True,
  '<p>There is no form that closes it while the corporation exists, and '
  'nothing to close: the account is the corporation&#8217;s relationship with '
  'the Agency for income tax, and it ends when the corporation does.</p>\n'
  '<p>So the T2 is not something that can be switched off for a quiet year. '
  'Every tax year gets a return until the corporation is dissolved, and a '
  'year with no activity gets one reporting $0.00 rather than no return at '
  'all.</p>\n'
  '<p>' + LATE_QUAL + '</p>\n'
  '<p>The ' + a(HUB + 'nil-t2-return-complete-guide/',
                'complete guide to the nil T2 return')
  + ' is the pillar for that side of it.</p>'),

 ('order', 'The Order to Deal With Them In',
  '<p>The sequence is not arbitrary, because each step rests on the one '
  'before it. Returns first, because a closure does not file anything. '
  'Closures next, because they stop the dates recurring. Anything to do with '
  'dissolution last, because it rests on a complete filing record.</p>\n'
  + tbl(('Order', 'Step', 'Why it sits here'),
        [('1', 'File every outstanding T2 return, oldest first',
          'Each year opens from the closing balances of the one before it'),
         ('2', 'File the outstanding GST/HST and payroll returns',
          'A closure does not file what fell due while the account was open'),
         ('3', 'Close the payroll account with Form RC145',
          'Ends the remittances and the annual T4'),
         ('4', 'Close the GST/HST account with Form RC145',
          'Ends the reporting periods'),
         ('5', 'The final T2, clearance and the registry filing',
          'Only where the corporation is being wound up')])
  + '\n<p>The ' + a(SITE + '/tools/cra-account-closure-sequencer/',
                    'CRA account closure sequencer')
  + ' produces this list for a particular corporation, naming which steps '
  'apply and which sit outside the fee.</p>'),

 ('dissolution', 'What Has to Be Closed Before a Dissolution', True,
  '<p>A corporation cannot be cleanly wound up with accounts still open and '
  'returns still outstanding. The clearance certificate is the step that '
  'makes this concrete: the request rests on a complete filing record, so an '
  'outstanding GST/HST or payroll period blocks it as surely as an unfiled '
  'T2.</p>\n'
  '<p>Dissolving anyway does not solve it. A corporation dissolved with '
  'unfiled years leaves those years open behind it, and the registry '
  'dissolution settles nothing on the tax side.</p>\n'
  '<p>The ' + a(HUB + 'winding-up-an-inactive-corporation/',
                'guide to winding up an inactive corporation')
  + ' sets out the whole sequence, and the '
  + a(SITE + '/tools/dissolution-readiness-checker/',
      'dissolution readiness checker')
  + ' tests whether a corporation is ready for the last step.</p>'),

 ('not-covered', 'What Sits Outside the Fee, Said Plainly',
  '<p>The fee of ' + PRICE + ' covers one nil T2 return for one corporation '
  'for one tax year. It is worth being direct about what that does not '
  'include, because the accounts on this page are the commonest place the '
  'boundary gets found the hard way.</p>\n'
  + tbl(('Item', 'Covered by the fee'),
        [('A nil T2 return for a tax year', 'Yes'),
         ('A GST/HST return, nil or otherwise', 'No'),
         ('A payroll remittance, nil or otherwise', 'No'),
         ('The T4 information return', 'No'),
         ('Closing an account with Form RC145', 'No'),
         ('The registry annual return', 'No'),
         ('A clearance certificate request', 'No')])
  + '\n<p>Where any of those are needed, they are handled by Gondaliya CPA '
  'Professional Corporation at gondaliyacpa.ca rather than priced here. The '
  'full boundary is on the ' + a(COST, 'nil T2 filing cost') + ' page.</p>'),

 ('mistakes', 'The Four Mistakes Worth Avoiding', True,
  '<p>Each of these is common enough to be worth naming, and each one costs '
  'more to undo than to avoid.</p>\n'
  + tbl(('The mistake', 'What it actually does'),
        [('Assuming no activity means no return',
          'The obligation follows the open account, so the returns fall due '
          'anyway and accumulate'),
         ('Closing an account to deal with the outstanding returns',
          'A closure files nothing. The outstanding periods stay outstanding'),
         ('Reading the T4 deadline off the fiscal year-end',
          'The T4 reports a calendar year and is due at the end of the '
          'following February, which can be months away from the T2 date'),
         ('Dissolving with accounts still open',
          'The tax years stay open behind the dissolution, and a clearance '
          'certificate is blocked until they are filed')])
  + '\n<p>The thread running through all four is the same: an account is a '
  'standing obligation, and only a closure ends it. The '
  + a(HUB + 'corporate-compliance-calendar/',
      'guide to the corporate compliance calendar')
  + ' sets out the dates each open account generates.</p>'),
 ],
 faq=[
  ('Does a dormant corporation still have to file GST/HST returns?',
   'While the account is open, yes. A period with no sales is reported as a '
   'nil return rather than skipped, because the obligation follows the open '
   'account rather than the activity.'),
  ('Do I have to make payroll remittances if nobody was paid?',
   'While the payroll account is open the Agency expects the remittances, '
   'including nil ones, and a T4 information return after each calendar year. '
   'Form RC145 closes the account and ends both.'),
  ('How do I close a GST/HST or payroll account?',
   'With Form RC145, which closes either one. Closing it does not file the '
   'returns that fell due while it was open, so the outstanding returns come '
   'first.'),
  ('Which of these can be assessed against me personally?',
   'Payroll source deductions and net GST/HST can be assessed against '
   'directors personally, because neither was ever the corporation&#8217;s '
   'money. Corporate income tax, on its own, cannot.'),
  ('Is any of this covered by the nil T2 fee?',
   'The nil T2 return is. The GST/HST returns, the payroll remittances, the '
   'T4 return and the account closures all sit outside the fee of '
   + PRICE + '.'),
  ('Can I dissolve the corporation instead of dealing with these?',
   'Not cleanly. A clearance certificate request rests on a complete filing '
   'record, so an outstanding period blocks it, and dissolving anyway leaves '
   'the tax years open behind the corporation.'),
 ])

# ---------------------------------------------------------------------------
# 29. Choosing and changing a fiscal year-end
# ---------------------------------------------------------------------------
G29 = dict(
 slug='choosing-and-changing-a-fiscal-year-end',
 title='Choosing and Changing a Fiscal Year-End | Complete Guide',
 h1_pre='The Complete Guide to ',
 h1_span='Choosing and Changing a Fiscal Year-End',
 h1='The Complete Guide to Choosing and Changing a Fiscal Year-End',
 eyebrow='Year-End',
 meta=('A corporation picks its own year-end, the first return fixes it, and '
       'changing it needs written approval. How to choose it and what a '
       'change costs.'),
 convert=(SITE + '/tools/first-t2-year-end-options-generator/',
          'See every date available'),
 kids=['when-should-i-file-my-first-t2-after-incorporating',
       'when-should-i-file-a-nil-t2-for-a-short-first-tax-year',
       'how-do-i-fix-a-nil-t2-return-i-filed-with-the-wrong-year-end',
       'do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
       'how-do-i-file-a-nil-t2-return-in-canada',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity'],
 sections=[

 ('a-choice', 'Nothing Assigns You a Year-End',
  '<p>A corporation picks its own fiscal year-end. There is no default, '
  'nothing is allocated at incorporation, and December 31 is a convention '
  'rather than a rule. The articles of incorporation do not set it '
  'either.</p>\n'
  '<p>What sets it is the first T2 return filed. From then on the date is on '
  'the record, it recurs annually, and every other date in the '
  'corporation&#8217;s tax life is measured from it. That makes this the one '
  'decision that is free to make now and awkward to revisit.</p>\n'
  '<p>The ' + a(SITE + '/tools/first-t2-year-end-options-generator/',
                'first T2 year-end options generator')
  + ' lists every date available from a given incorporation date, with the '
  'filing deadline each one produces.</p>'),

 ('fifty-three-weeks', 'The First Tax Year Cannot Exceed 53 Weeks',
  '<p>This is the one hard limit on the choice. A first tax year runs from the '
  'date of incorporation to the chosen year-end and may not exceed 53 weeks, '
  'which is 371 days counting the day of incorporation.</p>\n'
  '<p>A year-end beyond that point is not available at all. Where someone '
  'wants one anyway, the consequence is not a longer first year: it is a '
  'first year ending earlier, then a full year, and two returns due within '
  'months of each other.</p>\n'
  '<div class="ei-info"><p>Counting it by eye from two dates in different '
  'years is where the mistakes come from, because 371 days does not line up '
  'with any month boundary. The '
  + a(SITE + '/tools/53-week-first-tax-year-checker/',
      '53-week first tax year checker')
  + ' tests one proposed date and the '
  + a(SITE + '/tools/fiscal-period-length-calculator/',
      'fiscal period length calculator')
  + ' measures a period you already have.</p></div>'),

 ('what-follows', 'Everything Else Is Measured From It', True,
  '<p>Picking the year-end picks the rest of the calendar, which is the real '
  'reason it deserves a decision rather than a default. Two of these dates '
  'follow from it directly and one deliberately does not.</p>\n'
  + tbl(('Obligation', 'Measured from the year-end', 'When'),
        [('The T2 return', 'Yes', 'Six months after it'),
         ('A balance of tax', 'Yes',
          'Two months after it, or three for a qualifying CCPC'),
         ('The T4 information return', 'No',
          'The end of February following the calendar year'),
         ('The registry annual return', 'No',
          'Measured from the incorporation anniversary')])
  + '\n<p>A month-end year-end makes the six-month rule land on a month-end '
  'too, which is the practical argument for choosing one. A year-end on the '
  '9th puts the filing deadline on an awkward mid-month date every year '
  'after. The '
  + a(SITE + '/tools/corporate-deadline-calendar-generator/',
      'corporate deadline calendar generator')
  + ' shows the whole calendar one year-end produces.</p>'),

 ('short-first-year', 'A Short First Year Is a Return for Almost Nothing',
  '<p>Choose the earliest month-end after incorporating and the first tax year '
  'might be three weeks long. It is still a tax year, it still gets a return, '
  'and that return is ' + PRICE + ' like any other. There is no part-year '
  'rate.</p>\n'
  '<p>So an early first year-end means paying for a return covering almost '
  'nothing, and then a second return for the first full year. A year-end '
  'closer to twelve months out produces one return instead of two over the '
  'same stretch of time.</p>\n'
  '<p>Short years also arise for reasons nobody chooses: an approved change of '
  'year-end, an amalgamation, and a final period ending at dissolution. The '
  + a(SITE + '/tools/short-tax-year-deadline-calculator/',
      'short tax year deadline calculator')
  + ' covers the deadline on any of them, and the '
  + a(HUB + 'first-year-t2-filing/',
      'guide to first-year T2 filing')
  + ' covers the first return itself.</p>'),

 ('short-not-early', 'A Short Year Does Not Get an Early Deadline', True,
  '<p>Worth stating on its own because the intuition runs the other way. The '
  'six-month rule is measured from the day the period ends, whatever the '
  'period&#8217;s length. A three-month stub period has six months after it '
  'to file, which is twice the period itself.</p>\n'
  '<p>What a short period does bring forward is the next year-end, and with '
  'it the next return. That is how two filing deadlines end up weeks apart, '
  'and how the earlier one gets missed: two dates close together read as one '
  'obligation. The '
  + a(SITE + '/tools/two-t2-returns-in-one-year-checker/',
      'two T2 returns in one year checker')
  + ' shows both dates and the gap between them.</p>'),

 ('changing', 'Changing It Needs Written Approval',
  '<p>A fiscal year-end is fixed by the first return filed, and changing it '
  'needs the written approval of the Canada Revenue Agency. The request is '
  'made before the change rather than demonstrated by filing.</p>\n'
  '<p>That sequence is the part most often got wrong, and the next section is '
  'about what happens when it is.</p>\n'
  '<p>An approved change closes a period on the new date. That period is a '
  'tax year in its own right with its own return and its own deadline, so the '
  'cost of a change is an extra return that would not otherwise exist. The '
  + a(SITE + '/tools/year-end-change-impact-calculator/',
      'year-end change impact calculator')
  + ' shows the period a given change creates, its length and both filing '
  'dates.</p>'),

 ('wrong-year-end', 'A Wrong Year-End Gets the Transmission Rejected', True,
  '<p>Filing a return carrying a year-end that does not match the record is '
  'not read as a change of year-end. It is rejected against the date on '
  'record.</p>\n'
  '<p>The consequence is worse than it first sounds, because a rejection is '
  'not a late filing. A refused transmission is not a filed return at all, so '
  'the year stays outstanding and the person who sent it believes it is '
  'done.</p>\n'
  '<div class="ei-warn"><p>On a catch-up this compounds. Several years sent in '
  'one sitting against the wrong year-end are several years still '
  'outstanding, and the error is only found when a demand to file arrives or '
  'a clearance request is refused.</p></div>\n'
  '<p>Which is why the year-end on record is confirmed before anything is '
  'transmitted rather than assumed from the incorporation papers. The '
  + a(SITE + '/tools/corporate-fiscal-year-end-calculator/',
      'corporate fiscal year end calculator')
  + ' works from the date on record.</p>'),

 ('the-371-ceiling', 'A Change Cannot Reach More Than 53 Weeks Out',
  '<p>The same 53-week limit that bounds a first tax year bounds the period a '
  'change creates. Where the gap between the current year-end and the '
  'proposed one is longer than 371 days, that gap is not a single tax year '
  'and cannot be reported as one.</p>\n'
  '<p>Reaching a year-end that far out needs an intervening year-end first, '
  'which means two returns rather than one. It is the same arithmetic as the '
  'first-year limit, applied at a different moment.</p>\n'
  + tbl(('Length of the period a change creates', 'What it is'),
        [('Under twelve months', 'A short tax year, with its own return'),
         ('Twelve months', 'A full tax year'),
         ('Up to 371 days', 'Still one tax year'),
         ('More than 371 days',
          'Not one tax year; an intervening year-end is needed')])),

 ('catch-up', 'Why the Year-End Matters Most on a Catch-Up', True,
  '<p>A corporation with one year to file has one date to get right. A '
  'corporation with six has the same date six times, and every one of those '
  'returns is rejected if the date is wrong.</p>\n'
  '<p>The years are also prepared oldest first, because each one opens from '
  'the closing balances of the one before it. A wrong year-end does not just '
  'produce six rejections; it produces a sequence that cannot be '
  'reconciled.</p>\n'
  '<p>The ' + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
                'guide to catching up on unfiled corporate tax returns')
  + ' covers the sequence, and the '
  + a(SITE + '/tools/catch-up-filing-schedule-generator/',
      'catch-up filing schedule generator')
  + ' produces the dated schedule once the year-end is known.</p>'),

 ('nil-years', 'None of This Changes for a Nil Year',
  '<p>A corporation that has never traded still has a year-end, still has it '
  'fixed by its first return, and still needs written approval to change it. '
  'Being nil affects the figures on the return and nothing about the '
  'calendar.</p>\n'
  '<p>' + NOT_NIL + '</p>\n'
  '<p>So the year-end decision is made at incorporation whether or not '
  'anything is happening yet, and a corporation registered and left dormant '
  'has already made it by the time its first return goes in.</p>'),

 ('practical', 'How to Decide, in Practice', True,
  '<p>There is no answer that fits every corporation, and anyone offering one '
  'does not know the facts. What can be said is which considerations actually '
  'bear on it.</p>\n'
  + tbl(('Consideration', 'What it argues for'),
        [('Keeping the calendar simple',
          'A month-end, so the six-month rule lands on a month-end too'),
         ('Avoiding a return for a few weeks of nothing',
          'A first year-end closer to twelve months out'),
         ('Matching the year to a natural business cycle',
          'A year-end after the busy season rather than inside it'),
         ('Never needing to change it',
          'Thinking about the next few years now, since a change costs an '
          'extra return and needs written approval')])
  + '\n<p>Where the corporation is dormant and may be wound up rather than '
  'traded, the last row matters most: a year-end chosen now is the one the '
  'final return will be measured from. The '
  + a(HUB + 'final-t2-and-dissolution/',
      'guide to the final T2 and dissolution')
  + ' covers that end of it.</p>'),
 ],
 faq=[
  ('Who decides my corporation&#8217;s fiscal year-end?',
   'The corporation does. There is no default and nothing is assigned at '
   'incorporation. The first T2 return filed is what fixes the date on the '
   'record.'),
  ('How long can my first tax year be?',
   'Up to 53 weeks, which is 371 days counting the day of incorporation. A '
   'year-end beyond that is not available, so the first year has to end '
   'earlier.'),
  ('Can I change my fiscal year-end later?',
   'With the written approval of the Canada Revenue Agency. The request is '
   'made before the change, and filing a return carrying a different date '
   'does not change the date on record.'),
  ('What happens if I file against the wrong year-end?',
   'The transmission is rejected against the year-end on record. A refused '
   'transmission is not a filed return, so the year stays outstanding.'),
  ('Does changing a year-end cost an extra return?',
   'Usually. The change closes a period on the new date, that period is a tax '
   'year in its own right, and it gets its own return at ' + PRICE + '.'),
  ('Does a short tax year have an earlier deadline?',
   'No. The six-month rule runs from the day the period ends, so a '
   'three-month period gets the same six months as a full year.'),
 ])

# ---------------------------------------------------------------------------
# 30. Quebec CO-17 and Alberta AT1
#
# Hard rule 8 governs this page: a Quebec page states CO-17 is a separate
# return and an Alberta page says the same for AT1. This one does both, in
# those terms, in the hero, the body, a table and the FAQ.
# ---------------------------------------------------------------------------
G30 = dict(
 slug='quebec-co17-and-alberta-at1',
 title='Quebec CO-17 and Alberta AT1 | Complete Guide',
 h1_pre='The Complete Guide to ', h1_span='Quebec CO-17 and Alberta AT1',
 h1='The Complete Guide to Quebec CO-17 and Alberta AT1',
 eyebrow='Provincial',
 meta=('Quebec and Alberta each collect their own corporate tax, so each has '
       'a separate return. CO-17 and AT1 are not part of the federal T2 and '
       'are not covered by the fee.'),
 convert=(SITE + '/tools/provincial-return-requirement-checker/',
          'Check which apply'),
 kids=['do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'how-do-i-file-a-nil-t2-return-in-canada',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'can-i-file-a-nil-t2-myself-without-an-accountant',
       'do-i-need-financial-statements-for-a-nil-t2-return',
       'how-do-i-know-if-my-corporation-counts-as-dormant'],
 sections=[

 ('two-exceptions', 'Most Provinces Collect Through the Federal Return',
  '<p>In most of Canada a corporation files one corporate income tax return. '
  'The province levies its own corporate tax, but it is collected through the '
  'federal T2, so the federal return settles both and there is nothing '
  'separate to send.</p>\n'
  '<p>Quebec and Alberta are the exceptions. Each administers its own '
  'corporate income tax and each has its own return. Quebec&#8217;s is '
  'CO-17, filed with Revenu Quebec. Alberta&#8217;s is AT1.</p>\n'
  + tbl(('Where the corporation operates', 'Corporate income tax returns'),
        [('Quebec', 'The federal T2 and CO-17'),
         ('Alberta', 'The federal T2 and AT1'),
         ('Everywhere else', 'The federal T2 on its own')])),

 ('separate-means-separate', 'Separate Means Separate',
  '<p>CO-17 is a separate provincial return. AT1 is a separate provincial '
  'return. That phrasing is deliberate and it is worth taking literally: '
  'neither is a schedule attached to the T2, neither is produced as a '
  'by-product of filing federally, and filing the T2 does not file '
  'either.</p>\n'
  '<p>Each has its own form, its own filing, and its own deadline. A '
  'corporation that files a perfect T2 and nothing else has met one of its '
  'two obligations.</p>\n'
  '<div class="ei-info"><p>The '
  + a(SITE + '/tools/provincial-return-requirement-checker/',
      'provincial return requirement checker')
  + ' answers which of them apply to a particular corporation, in two '
  'questions.</p></div>'),

 ('a-quiet-year', 'A Quiet Year Is Quiet on Both Returns', True,
  '<p>A corporation with no activity has nothing to report provincially '
  'either, so the provincial return for that year is nil in the same way the '
  'federal one is.</p>\n'
  '<p>Being nil does not make it optional. The obligation follows from the '
  'corporation having a permanent establishment in the province, not from '
  'there being something to report, so a nil year is still a return to '
  'file.</p>\n'
  '<p>This is the same logic as every other obligation on a dormant '
  'corporation, and it is the single most useful thing to understand about '
  'nil filing: the question is never whether anything happened, it is '
  'whether an obligation exists. The '
  + a(HUB + 'zero-activity-corporate-tax-returns/',
      'guide to zero-activity corporate tax returns')
  + ' works through that distinction.</p>'),

 ('not-covered', 'Neither Is Covered by the Fee',
  '<p>The fee of ' + PRICE + ' covers one nil federal T2 return for one '
  'corporation for one tax year. CO-17 is not covered by it, and neither is '
  'AT1.</p>\n'
  '<p>Stating that plainly is better than leaving it to be discovered. A '
  'corporation with a Quebec or Alberta permanent establishment needs work '
  'this service does not price, and pretending otherwise would be worse than '
  'saying so.</p>\n'
  '<p>Where a provincial return is needed it is handled by Gondaliya CPA '
  'Professional Corporation at gondaliyacpa.ca at $350.00 plus HST per year. '
  'The ' + a(COST, 'nil T2 filing cost')
  + ' page sets out the whole boundary of what sits inside the fee.</p>'),

 ('permanent-establishment', 'What Decides Whether a Province Is Involved',
  True,
  '<p>The test is a permanent establishment in the province, not where the '
  'corporation was incorporated and not where the director happens to live. '
  'A federally incorporated corporation operating only in Quebec files CO-17; '
  'an Ontario corporation with no Quebec presence does not.</p>\n'
  '<p>Where that test lands for a particular corporation is a question of '
  'fact rather than something a web page can settle, and it is not a question '
  'to answer by guessing. What this page can do is say which returns exist '
  'and what each one is.</p>\n'
  '<p>A dormant corporation is usually the straightforward case: a '
  'corporation that has never operated anywhere has no permanent '
  'establishment anywhere, and the federal T2 is the whole of its corporate '
  'income tax filing.</p>'),

 ('not-the-registry', 'The Registry Annual Return Is a Different Thing',
  '<p>This is the commonest confusion on the subject, and it is worth '
  'separating carefully, because the two obligations share the words "annual" '
  'and "provincial" and nothing else.</p>\n'
  + tbl(('', 'A provincial tax return', 'A registry annual return'),
        [('What it is', 'CO-17 in Quebec, AT1 in Alberta',
          'A filing confirming the directors and the registered office'),
         ('What it reports', 'Income and provincial corporate tax',
          'No income at all'),
         ('Who it goes to', 'The provincial tax administration',
          'The registry the corporation is incorporated with'),
         ('What missing it does', 'An outstanding return',
          'A striking: the registry dissolves the corporation')])
  + '\n<p>Every corporation owes a registry annual return somewhere, '
  'including the 11 provinces and territories that have no separate tax '
  'return. The '
  + a(HUB + 'provincial-and-federal-annual-returns/',
      'guide to provincial and federal annual returns')
  + ' covers that obligation, and the '
  + a(SITE + '/tools/involuntary-dissolution-risk-checker/',
      'involuntary dissolution risk checker')
  + ' covers what missing it produces.</p>'),

 ('alberta', 'Alberta: AT1', True,
  '<p>AT1 is Alberta&#8217;s corporate income tax return, and it is a '
  'separate provincial return filed with Alberta rather than part of the '
  'federal T2.</p>\n'
  '<p>A corporation with an Alberta permanent establishment files both. A nil '
  'year produces a nil AT1 rather than no AT1, on the same reasoning as '
  'everything else here: the obligation follows the permanent establishment '
  'rather than the activity.</p>\n'
  '<p>AT1 is not covered by the fee of ' + PRICE + '.</p>'),

 ('quebec', 'Quebec: CO-17',
  '<p>CO-17 is Quebec&#8217;s corporate income tax return, filed with Revenu '
  'Quebec. It is a separate provincial return, not a schedule of the federal '
  'T2 and not produced by filing federally.</p>\n'
  '<p>A corporation with a Quebec permanent establishment files both. A nil '
  'year produces a nil CO-17 rather than no CO-17.</p>\n'
  '<p>CO-17 is not covered by the fee of ' + PRICE + '.</p>\n'
  '<div class="ei-warn"><p>Quebec is also the province where the two '
  'obligations on this page are most often conflated, because the registry '
  'filing and the tax return both sit with Quebec institutions. They remain '
  'separate filings with separate consequences.</p></div>'),

 ('what-the-t2-still-does', 'The Federal T2 Is Still Required', True,
  '<p>Worth saying because the logic occasionally runs backwards: a '
  'corporation that files CO-17 or AT1 has not thereby dealt with the federal '
  'return. The T2 is required of every resident corporation, in every '
  'province, every tax year, until the corporation is dissolved.</p>\n'
  '<p>So a Quebec corporation files two returns and an Alberta corporation '
  'files two returns. Neither replaces the other, and a nil year means two '
  'nil returns rather than one.</p>\n'
  '<p>' + LATE_QUAL + '</p>'),

 ('dissolution', 'Both Matter at a Wind-Up',
  '<p>A corporation being wound up has to be current on everything, and a '
  'provincial return is part of everything. An outstanding CO-17 or AT1 is an '
  'outstanding return in the same way an unfiled T2 is.</p>\n'
  '<p>Where a clearance certificate is being sought, the request rests on a '
  'complete filing record. The federal side of that is what this service '
  'covers; the provincial side, where it exists, is handled at '
  'gondaliyacpa.ca.</p>\n'
  '<p>The ' + a(HUB + 'winding-up-an-inactive-corporation/',
                'guide to winding up an inactive corporation')
  + ' sets out the order the steps have to happen in, and the '
  + a(SITE + '/tools/clearance-certificate-requirement-checker/',
      'clearance certificate requirement checker')
  + ' covers the certificate itself.</p>'),

 ('summary', 'The Whole of It, in Five Lines', True,
  '<p>If nothing else on this page is remembered, these are the five facts '
  'that matter.</p>\n'
  + tbl(('', 'The fact'),
        [('1', 'Quebec collects its own corporate tax: CO-17 is a separate '
               'provincial return'),
         ('2', 'Alberta collects its own corporate tax: AT1 is a separate '
               'provincial return'),
         ('3', 'Everywhere else the province collects through the federal '
               'T2, so the T2 is the only corporate income tax return'),
         ('4', 'A nil year still produces a return on each one that applies, '
               'because the obligation follows the permanent establishment'),
         ('5', 'The fee of ' + PRICE + ' covers the federal nil T2 only; '
               'CO-17 and AT1 are handled at gondaliyacpa.ca')])
  + '\n<p>The ' + a(HUB + 'nil-t2-return-complete-guide/',
                    'complete guide to the nil T2 return')
  + ' is the pillar for the federal return this service does cover.</p>'),
 ],
 faq=[
  ('Does Quebec have a separate corporate tax return?',
   'Yes. CO-17 is a separate provincial return, filed with Revenu Quebec. It '
   'is not part of the federal T2, and filing the T2 does not file it.'),
  ('Does Alberta have a separate corporate tax return?',
   'Yes. AT1 is a separate provincial return in the same way, filed with '
   'Alberta rather than as part of the federal T2.'),
  ('What about the other provinces and territories?',
   'Elsewhere the province or territory collects its corporate income tax '
   'through the federal return, so the T2 is the only corporate income tax '
   'return the corporation files.'),
  ('Is a nil CO-17 or AT1 still required?',
   'The obligation follows from having a permanent establishment in the '
   'province rather than from there being something to report, so a nil year '
   'still produces a return on each one that applies.'),
  ('Are CO-17 and AT1 covered by the fee?',
   'No. The fee of ' + PRICE + ' covers one nil federal T2 return for one '
   'corporation for one tax year. Provincial returns are handled by Gondaliya '
   'CPA Professional Corporation at gondaliyacpa.ca at $350.00 plus HST per '
   'year.'),
  ('Is this the same as the provincial annual return?',
   'No, and they are easy to confuse. A registry annual return confirms the '
   'directors and the registered office and reports no income; a provincial '
   'tax return reports income and tax. Missing the registry one gets a '
   'corporation struck.'),
 ])

GUIDES = [G28, G29, G30]

# ---------------------------------------------------------------------------
# Render. Identical to the pillar and batches 2 to 5.
# ---------------------------------------------------------------------------
KID_TITLES = {}
for r in json.load(open(os.path.join(HERE, '..', 'f5', 'f5-manifest.json'),
                        encoding='utf-8')):
    KID_TITLES[r['slug']] = r['meta']['cnf_question_text']

# ---------------------------------------------------------------------------
# Guards. Each of these fired at least once while this batch was written, or
# guards a mistake an earlier batch actually made.
# ---------------------------------------------------------------------------
assert len(GUIDES) == 3, '%d guides in batch 6' % len(GUIDES)

_batch_slugs = [g['slug'] for g in GUIDES]
assert len(set(_batch_slugs)) == 3, 'duplicate slug within the batch'

_registry_slugs = [s for s, _t in REGISTRY]
for _g in GUIDES:
    # A guide missing from the registry renders, publishes, and is silently
    # absent from every sibling list on the site.
    assert _g['slug'] in _registry_slugs, (
        '%s is not in the registry, so no other guide will link to it'
        % _g['slug'])
    assert len(_g['sections']) == 11, (
        '%s has %d sections; render adds the fee section to make the 12 the '
        'gate requires' % (_g['slug'], len(_g['sections'])))
    _keys = [t[0] for t in _g['sections']]
    assert len(set(_keys)) == 11, '%s repeats a section id' % _g['slug']
    _titles = [t[1] for t in _g['sections']]
    assert 'What the Fee Covers' not in _titles, (
        '%s defines a section the render already appends' % _g['slug'])
    assert len(set(_titles)) == 11, (
        '%s repeats a section heading, which the gate counts as a duplicate '
        'contents row' % _g['slug'])
    assert len(_g['faq']) == 6, '%s has %d FAQs' % (_g['slug'], len(_g['faq']))
    assert len(_g['kids']) == 6, '%s has %d kids' % (_g['slug'], len(_g['kids']))
    assert len(set(_g['kids'])) == 6, '%s repeats a kid' % _g['slug']
    for _k in _g['kids']:
        # A kid absent from the manifest is a 404 on a published page.
        assert _k in KID_TITLES, (
            '%s links to /answers/%s/, which is not a built question'
            % (_g['slug'], _k))
    for _f in ('title', 'h1', 'h1_span', 'eyebrow', 'meta', 'convert'):
        assert _g.get(_f), '%s is missing %s' % (_g['slug'], _f)
    assert _g['h1'] == _g.get('h1_pre', '') + _g['h1_span'] + _g.get('h1_post', ''), (
        '%s: h1 does not match the pieces the hero is built from, so the '
        'schema headline and the visible H1 would disagree' % _g['slug'])
    assert _g['convert'][0].startswith(SITE), (
        '%s converts off-site' % _g['slug'])

# Every /answers/ and /guides/ link anywhere in the body must resolve to
# something that exists. Batch 4 had no such check and relied on reading.
_body = '\n'.join(str(_g['sections']) + str(_g['faq']) for _g in GUIDES)
import re as _re
for _slug in set(_re.findall(r'/answers/([a-z0-9-]+)/', _body)):
    assert _slug in KID_TITLES, 'body links to a question that does not exist: ' + _slug
for _slug in set(_re.findall(r'corpnilfilingfor300\.ca/guides/([a-z0-9-]+)/', _body)):
    assert _slug in _registry_slugs, 'body links to a guide that does not exist: ' + _slug

def render(g):
    url = HUB + g['slug'] + '/'
    sections = [tuple(t) + ((False,) if len(t) == 3 else ()) for t in g['sections']]
    sections.append((
        'fee', 'What the Fee Covers',
        '<p>The fee is ' + PRICE + ', covering one nil T2 return for one corporation '
        'for one tax year:</p>\n' + tbl(('Included', 'Detail'), FEE_ROWS)
        + '\n<p>See the full ' + a(COST, 'nil T2 filing cost') + '.</p>', False))
    assert len(sections) == 12, '%s has %d sections' % (g['slug'], len(sections))

    parts = [CSS]
    h1_html = (g.get('h1_pre', '') + '<span>' + g['h1_span'] + '</span>'
               + g.get('h1_post', ''))
    parts.append(
     '<div class="ei-hero"><div class="ei-hero-inner">'
     '<span class="ei-hero-eyebrow">' + g['eyebrow'] + '</span>'
     '<h1>' + h1_html + '</h1>'
     '<p class="ei-hero-sub">' + g['meta'] + ' Nil T2 filing is ' + PRICE + '.</p>'
     '<p class="ei-hero-by">' + BYLINE + '</p>'
     '<div class="ei-hero-btns"><a class="ei-btn-blue" href="' + FORM + '">'
     'Start Nil T2 Filing NOW</a>'
     '<a class="ei-btn-blue" style="background:transparent;border:2px solid '
     'rgba(255,255,255,0.4)" href="' + g['convert'][0] + '">' + g['convert'][1]
     + '</a></div></div></div>\n')

    toc_rows = '\n'.join('<li>%s</li>' % a('#' + k, t) for k, t, _b, _alt in sections)
    parts.append(
     '<div class="ei-section"><div class="ei-wrap ei-art">\n'
     '<p class="ei-updated">Last reviewed: ' + TODAY + ' &nbsp;&middot;&nbsp; '
     + a(HUB, 'All nil T2 filing guides') + '</p>\n'
     '<div class="ei-toc"><h2>On this page</h2>\n<ol>\n' + toc_rows + '\n</ol></div>\n'
     '<div class="ei-info"><p>' + EFILE_PILLAR + '</p></div>\n'
     '</div></div>\n')

    for i, (k, t, body, alt) in enumerate(sections):
        parts.append(sec(k, t, body, alt))
        if i == 3:
            parts.append(cta_inline())

    faq_items = '\n'.join(
     '<details><summary>%s</summary><div class="ei-faq-a"><p>%s</p></div></details>'
     % (q, ans) for q, ans in g['faq'])
    kid_links = '\n'.join('<li>%s</li>' % a(A + s + '/', KID_TITLES[s])
                          for s in g['kids'])
    sib_links = sibling_links(g['slug'])
    parts.append(
     '<div class="ei-section-alt"><div class="ei-wrap ei-art">\n'
     '<h2 class="ei-h2">Frequently Asked Questions</h2>\n'
     '<div class="ei-faq">\n' + faq_items + '\n</div>\n'
     '<h3>Questions Answered in Full</h3>\n'
     '<ul class="ei-qlist">\n' + kid_links + '\n</ul>\n'
     '<h3>The Other Nil T2 Filing Guides</h3>\n'
     '<ul class="ei-qlist">\n' + sib_links + '\n</ul>\n'
     '</div></div>\n')

    parts.append(
     '<div class="ei-cta-bottom"><div class="ei-wrap">'
     '<h2>Nil T2 Filing, ' + PRICE + '</h2>'
     '<p>Type your corporation name, pick your unfiled years, pay, and sign Form '
     'T183CORP on a secure screen. Your CRA confirmation is emailed within 3 '
     'business days.</p>'
     '<a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
     '</div></div>\n')

    schema = {"@context": "https://schema.org", "@graph": [
     {"@type": "Article", "@id": url + "#article", "headline": g['h1'],
      "name": g['title'], "description": g['meta'], "inLanguage": "en-CA",
      "datePublished": ISO, "dateModified": ISO, "mainEntityOfPage": url,
      "author": {"@type": "Person", "name": "Sharad Gondaliya",
                 "honorificSuffix": "CPA", "url": SITE + "/sharad-gondaliya-cpa/"},
      "publisher": {"@type": "Organization",
                    "name": "Gondaliya CPA Professional Corporation"}},
     {"@type": "BreadcrumbList", "itemListElement": [
       {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
        "item": SITE + "/"},
       {"@type": "ListItem", "position": 2, "name": "Guides", "item": HUB},
       {"@type": "ListItem", "position": 3, "name": g['h1'], "item": url}]}]}
    parts.append('<script type="application/ld+json">'
                 + json.dumps(schema, ensure_ascii=False) + '</script>')
    return ''.join(parts), url

records = []
for g in GUIDES:
    html, url = render(g)
    records.append(dict(slug=g['slug'], title=g['title'], h1=g['h1'],
                        meta_description=g['meta'], url=url, content=html,
                        toc=[t[1] for t in g['sections']] + ['What the Fee Covers']))
    open(os.path.join(HERE, g['slug'] + '.html'), 'w', encoding='utf-8').write(html)

json.dump(records, open(os.path.join(HERE, 'f9-batch6-manifest.json'), 'w'),
          ensure_ascii=False, indent=1)

# The 6(g) outbound cap of 40 is the reason the sibling window exists. Report
# it per guide rather than waiting for the gate, so a breach is visible here.
for r in records:
    out = len(set(_re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"',
                              r['content'])))
    print('%-44s %6d bytes  %2d sections  out:%2d'
          % (r['slug'], len(r['content'].encode()), len(r['toc']), out))
    assert out <= 40, '%s carries %d outbound links, over the 40 cap' % (r['slug'], out)
