"""Family 9 batch 5: guides 18 to 27 of 30.

Topic sourcing, and where it departs from Appendix A
---------------------------------------------------
Batch 3 established the reading that Appendix A's Family 9 entries supply
TOPICS while their URL shapes are unusable: they are root-level, which collides
with the Family 4 catch-all, and ten carry a year token that 6(k) line 1749
forbids outright. Batches 3 and 4 took topics from that list and gave them
compliant slugs. This batch does the same for seven of its ten:

  /the-ultimate-guide-to-t2-filing-deadlines/
      -> /guides/t2-filing-deadlines/
  /the-ultimate-guide-to-zero-activity-corporate-tax-returns/
      -> /guides/zero-activity-corporate-tax-returns/
  /the-ultimate-guide-to-corporate-tax-arrears-and-penalties/
      -> /guides/corporate-tax-arrears-and-interest/
  /the-ultimate-guide-to-winding-up-an-inactive-corporation/
      -> /guides/winding-up-an-inactive-corporation/
  /2026-canadian-small-business-corporate-filing-guide/
      -> /guides/small-business-corporate-filing/
  /2026-canadian-corporate-compliance-calendar-guide/
      -> /guides/corporate-compliance-calendar/
  /2026-canadian-numbered-company-maintenance-guide/
      -> /guides/numbered-company-maintenance/

"The ultimate guide to" is dropped from slug and title, as in batch 4: hard
rule 4 bans superlative claims, and that phrase is the same move aimed at the
content rather than the price.

The remaining three topics are NOT in Appendix A, and that is a deviation worth
reading twice:

  /guides/mandatory-t2-electronic-filing/
  /guides/schedule-50-and-shareholder-reporting/
  /guides/non-resident-owned-corporation-nil-filing/

Appendix A's Family 9 list cannot supply ten more distinct topics. Of its
thirty entries, eleven are already built, and every one of the remaining
nineteen is either a naming variant of a guide already live -- the three
general nil T2 guides, the three dormant guides, the three catch-up guides,
the three dissolution guides, the two deadline guides, the two penalty guides
and the holding-company guide all collapse onto pages that exist -- or the
near-duplicate /final-t2-return-guide/, which restates
/guides/final-t2-and-dissolution/. Building those as written would have put
near-identical pages into competition with each other, which batch 3 already
recorded as the reason the list needs redefining rather than slug-patching.

So the last three are chosen on the same basis batch 3 used for its two: live
cluster support and the least overlap with what exists. Each has a Family 13
post or a Family 4 set already live pointing at it, and each covers a rule the
site states repeatedly but nowhere explains in full -- the e-filing mandate and
its flat penalties, the 10% shareholder threshold on Schedule 50, and the
non-resident daily penalty. Sharad Gondaliya to confirm all ten topics, the
seven slug corrections and the three additions.

The sibling window
------------------
This batch takes Family 9 from 17 to 27, and that broke the old "every guide
lists every other" design against the 6(g) outbound cap of 40. Measured at 17,
the pillar carried 34 outbound links; ten more siblings would have taken it to
44. The registry now hands out a 12-wide window instead, so every guide still
receives 12 sibling links plus the hub against a 6(g) minimum of 12, while
outbound falls by 14 on every guide. Batches 1 to 4 must be regenerated and
their live pages updated, because their sibling lists change too.
"""
import json, os

HERE  = os.path.dirname(os.path.abspath(__file__))
SITE  = 'https://corpnilfilingfor300.ca'
FORM  = SITE + '/form/'
HUB   = SITE + '/guides/'
A     = SITE + '/answers/'
COST  = SITE + '/pricing/nil-t2-filing-cost/'
TODAY, ISO = 'October 27, 2026', '2026-10-27'
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
assert len(REGISTRY) == 27, 'batch 5 renders against the 27-guide registry'
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
# Guide 18. /guides/t2-filing-deadlines/
# Appendix A topic /the-ultimate-guide-to-t2-filing-deadlines/, superlative
# dropped and slug moved to the /guides/ base. The /deadlines/ hub lists the
# due date for every fiscal year-end; this guide explains the rules that
# produce those dates, and links down to the hub rather than repeating it.
# ---------------------------------------------------------------------------
G18 = dict(
 slug='t2-filing-deadlines',
 title='T2 Filing Deadlines | Complete Guide for Canadian Corporations',
 h1='The Complete Guide to T2 Filing Deadlines',
 h1_pre='The Complete Guide to ',
 h1_span='T2 Filing Deadlines',
 eyebrow='Deadlines Guide',
 meta=('The six-month rule, how a weekend or a statutory holiday moves a due '
       'date, short and first tax years, and the deadlines that run separately.'),
 convert=(SITE + '/deadlines/', 'Every T2 Deadline by Year-End'),
 kids=['when-should-i-file-my-first-t2-after-incorporating',
       'when-should-i-file-a-nil-t2-for-a-short-first-tax-year',
       'how-do-i-find-out-which-t2-years-are-outstanding',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'what-happens-if-i-dont-file-a-nil-t2',
       'do-i-need-to-file-a-t2-for-the-year-my-corporation-was-dissolved'],
 sections=[
  ('six-month', 'The Six-Month Rule',
   '<p>A T2 is due six months after the day the tax year ends. That is the whole '
   'rule, and every other date on this page is produced by applying it to a '
   'particular year-end and then adjusting for the calendar.</p>\n'
   + tbl(('Fiscal year-end', 'Six months later', 'T2 due'),
         [('December 31', 'June 30', 'June 30'),
          ('March 31', 'September 30', 'September 30'),
          ('June 30', 'December 31', 'December 31'),
          ('August 31', 'February 28 or 29', 'The last day of February')])
   + '\n<p>The six months are counted to the same day number in the later month. '
   'Where that day does not exist, the deadline is the last day of that month, '
   'which is why an August 31 year-end lands on the end of February rather than '
   'on a non-existent February 31.</p>', True),
  ('year-end', 'Finding Your Fiscal Year-End',
   '<p>A corporation chooses its first fiscal year-end by filing its first T2 with '
   'that date on it. Once filed, the year-end is fixed and changing it needs the '
   'written approval of the Canada Revenue Agency.</p>\n'
   '<p>The year-end is not the incorporation anniversary and it is not December 31 '
   'by default. If no return has ever been filed, the year-end is still unsettled, '
   'and the first return to be filed sets it.</p>\n'
   '<div class="ei-info"><p>A corporation that has never filed can still choose. '
   'A corporation that has filed once cannot, and a return carrying a different '
   'year-end from the one on record is the single most common reason a '
   'transmission is rejected.</p></div>\n'
   '<p>See ' + a(A + 'how-do-i-fix-a-nil-t2-return-i-filed-with-the-wrong-year-end/',
                 'how to fix a return filed with the wrong year-end') + '.</p>'),
  ('weekend', 'When the Due Date Falls on a Weekend or Holiday',
   '<p>Where the calculated due date is a Saturday, a Sunday or a public holiday, '
   'the return is on time if the Agency receives it on the next business day.</p>\n'
   '<p>The holidays that matter are the ones observed where the return is filed, '
   'and a provincial holiday can move a date for a corporation in that province '
   'while leaving it unmoved elsewhere.</p>\n'
   + tbl(('Calculated due date', 'Why it moves', 'Return due'),
         [('Saturday', 'Not a business day', 'The following Monday'),
          ('Sunday', 'Not a business day', 'The following Monday'),
          ('A statutory holiday', 'Not a business day', 'The next business day'),
          ('A holiday followed by a weekend', 'Three days in a row',
           'The first business day after all three')])
   + '\n<p>The shift can be more than one day. A due date landing on a Sunday '
   'followed by a Monday holiday moves to the Tuesday.</p>', True),
  ('first', 'The First Tax Year and the 53-Week Limit',
   '<p>A first tax year runs from the date of incorporation to the chosen '
   'year-end, and it may not exceed 53 weeks. That is 371 days, counting the day '
   'of incorporation.</p>\n'
   '<p>A year-end chosen more than 53 weeks after incorporation is not available, '
   'and the first year has to end earlier, which produces a short first year and '
   'then a full one.</p>\n'
   '<p>See ' + a(A + 'when-should-i-file-my-first-t2-after-incorporating/',
                 'when the first T2 is due after incorporating')
   + ' and the guide to ' + a(HUB + 'first-year-t2-filing/', 'first-year T2 filing')
   + '.</p>'),
  ('short', 'Short Tax Years and Their Deadlines',
   '<p>A short tax year is any year shorter than twelve months. It arises on a '
   'first year, on an approved change of year-end, on an amalgamation and on a '
   'final year ending at dissolution.</p>\n'
   '<p>A short year does not get a short deadline. The six-month rule applies to '
   'the day the short year ends, so a three-month year still has six months after '
   'it to file.</p>\n'
   + tbl(('Short year arises from', 'Year ends on', 'Deadline measured from'),
         [('Incorporation', 'The chosen first year-end', 'That year-end'),
          ('An approved year-end change', 'The new year-end', 'That year-end'),
          ('An amalgamation', 'The day before amalgamating', 'That day'),
          ('Dissolution', 'The date of dissolution', 'That date')])
   + '\n<p>Two returns can therefore be due within a few months of each other, '
   'and both are separate filings at ' + PRICE + '.</p>', True),
  ('final', 'The Final Return After Dissolution',
   '<p>A final T2 covers the period from the start of the last tax year to the '
   'date of dissolution, and it is due six months after that date.</p>\n'
   '<p>Every earlier year has to be filed before a corporation can be wound up, so '
   'the final return is the last of a sequence rather than a substitute for '
   'it.</p>\n'
   '<p>The sequence is set out in the guide to '
   + a(HUB + 'final-t2-and-dissolution/', 'the final T2 and dissolution') + '.</p>'),
  ('payment', 'The Payment Deadline Is Not the Filing Deadline',
   '<p>Filing is due at six months. A balance of tax is due earlier: two months '
   'after the year-end, or three months for a Canadian-controlled private '
   'corporation that meets the conditions.</p>\n'
   + tbl(('Obligation', 'Due', 'On a nil year'),
         [('Filing the T2', 'Six months after year-end', 'Still due'),
          ('Paying the balance', 'Two or three months after year-end',
           'Nothing to pay'),
          ('Instalments', 'Monthly or quarterly through the year',
           'Not required')])
   + '\n<p>A corporation with no activity has no balance and no instalments, which '
   'leaves the filing deadline as the only one it has to meet.</p>', True),
  ('nil-same', 'A Nil Return Has the Same Deadline',
   '<p>There is no separate deadline for a corporation with no activity. The '
   'six-month rule applies in full, every year, until the corporation is formally '
   'dissolved.</p>\n'
   '<div class="ei-warn"><p>Dormancy is not an exemption and it is not a deferral. '
   'A corporation that has done nothing for nine years owes nine returns, each on '
   'its own six-month deadline, all of which have passed.</p></div>\n'
   '<p>See ' + a(A + 'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive/',
                 'whether an inactive corporation files every year') + '.</p>'),
  ('missed', 'What Happens After the Deadline Passes',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>The deadline does not stop mattering once it has gone. It is the date from '
   'which the year counts as outstanding, and that is what a demand to file, an '
   'arbitrary assessment and a blocked dissolution all follow from.</p>\n'
   '<p>The full picture is in the guide to '
   + a(HUB + 't2-late-filing-penalties/', 'T2 late filing penalties') + '.</p>', True),
  ('provincial', 'Provincial Deadlines That Run Separately',
   '<p>Three filings are commonly mistaken for part of the T2 and are not. Each '
   'has its own form, its own deadline and its own filing channel.</p>\n'
   + tbl(('Filing', 'Applies to', 'Relationship to the T2'),
         [('Alberta AT1', 'Alberta corporations', 'A separate return'),
          ('Quebec CO-17', 'Quebec corporations', 'A separate return'),
          ('The annual return', 'Corporations in most registries',
           'A registry filing, not a tax return')])
   + '\n<p>An Alberta corporation files the AT1 as well as the T2, and a Quebec '
   'corporation files the CO-17 as well as the T2. Neither is covered by the '
   'federal filing and neither is covered by the fee on this page.</p>\n'
   '<p>See the guide to '
   + a(HUB + 'provincial-and-federal-annual-returns/',
       'provincial and federal annual returns') + '.</p>'),
  ('calendar', 'Working Out Every Deadline You Owe',
   '<p>Start from the year-end on record, add a year at a time up to the present, '
   'and apply the six-month rule to each. Every year whose six months have elapsed '
   'and which has not been filed is outstanding.</p>\n'
   '<p>' + NOT_NIL + '</p>\n'
   '<p>The due date for every fiscal year-end is listed on '
   + a(SITE + '/deadlines/', 'the deadlines page') + ', and '
   + a(A + 'how-do-i-find-out-which-t2-years-are-outstanding/',
       'finding out which years are outstanding')
   + ' covers reading it off your own record.</p>'),
 ],
 faq=[
  ('When Is a T2 Due?',
   'Six months after the day the tax year ends. A December 31 year-end makes the '
   'T2 due June 30, and a March 31 year-end makes it due September 30.'),
  ('Does a Nil T2 Have a Later Deadline?',
   'No. The six-month rule applies in full to a corporation with no activity, '
   'every year, until the corporation is formally dissolved.'),
  ('What if the Deadline Is a Saturday?',
   'The return is on time if the Canada Revenue Agency receives it on the next '
   'business day. The same applies to a Sunday and to a public holiday, and the '
   'shift can be more than one day.'),
  ('How Long Can a First Tax Year Be?',
   'Up to 53 weeks, which is 371 days counting the day of incorporation. A '
   'year-end chosen beyond that is not available.'),
  ('Is the Payment Deadline the Same as the Filing Deadline?',
   'No. Filing is due at six months, while a balance of tax is due two months '
   'after the year-end, or three for a Canadian-controlled private corporation '
   'that meets the conditions. A nil year has no balance to pay.'),
  ('Does a Short Tax Year Get a Shorter Deadline?',
   'No. The six-month rule is measured from the day the short year ends, so a '
   'three-month year still has six months after it to file.'),
 ])

# ---------------------------------------------------------------------------
# Guide 19. /guides/zero-activity-corporate-tax-returns/
# Appendix A topic /the-ultimate-guide-to-zero-activity-corporate-tax-returns/.
# The nearest live page is the pillar, so this one is deliberately narrower:
# it is about the TEST for zero activity and the things that look like zero
# activity and are not, rather than about nil filing in general.
# ---------------------------------------------------------------------------
G19 = dict(
 slug='zero-activity-corporate-tax-returns',
 title='Zero-Activity Corporate Tax Returns | Canadian Guide',
 h1='The Complete Guide to Zero-Activity Corporate Tax Returns',
 h1_pre='The Complete Guide to ',
 h1_span='Zero-Activity Corporate Tax Returns',
 eyebrow='Zero-Activity Guide',
 meta=('What counts as zero activity, the entries that quietly take a year out '
       'of it, and which schedules a zero-activity return still carries.'),
 convert=(SITE + '/nil-t2-filing/', 'Nil T2 Filing Services'),
 kids=['do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account',
       'do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
       'how-do-i-know-if-my-corporation-counts-as-dormant',
       'do-i-need-financial-statements-for-a-nil-t2-return',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive'],
 sections=[
  ('definition', 'What Zero Activity Means on a Return',
   '<p>Zero activity means the corporation had no revenue, no expenses, no income '
   'of any kind and no disposition of property during the tax year. The return is '
   'filed showing those amounts as $0.00.</p>\n'
   '<p>It is a statement about the tax year, not about the corporation. The same '
   'corporation can have a zero-activity year, then a trading year, then another '
   'zero-activity year, and each is assessed on its own.</p>\n'
   '<div class="ei-info"><p>Zero activity is a property of the twelve months, '
   'which is why the question is always asked year by year and never once for the '
   'life of the corporation.</p></div>', True),
  ('still-file', 'Why a Zero-Activity Corporation Still Files',
   '<p>Every resident corporation files a T2 for every tax year, whether or not it '
   'did anything. The obligation attaches to existing as a corporation, not to '
   'earning income.</p>\n'
   '<p>The return is how the Agency learns the year was zero. Without it the year '
   'is not recorded as zero, it is recorded as missing.</p>\n'
   '<p>See ' + a(A + 'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity/',
                 'whether a corporation with no activity files') + '.</p>'),
  ('tests', 'The Tests That Decide Whether a Year Is Nil',
   '<p>Six questions settle it. A single yes takes the year out of zero activity, '
   'and the questions are asked about the tax year rather than about today.</p>\n'
   + tbl(('Question', 'If yes'),
         [('Was there any revenue?', 'Not a zero-activity year'),
          ('Were there any expenses?', 'Not a zero-activity year'),
          ('Was there investment income of any amount?',
           'Not a zero-activity year'),
          ('Was there rental income?', 'Not a zero-activity year'),
          ('Was a dividend paid or received?', 'Not a zero-activity year'),
          ('Was any property disposed of?', 'Not a zero-activity year')])
   + '\n<p>Amount is irrelevant to every row. Four dollars of interest answers the '
   'third question yes exactly as four thousand would.</p>', True),
  ('not-zero', 'What Looks Like Zero Activity and Is Not',
   '<p>These are the entries that most often turn up on a year the directors '
   'believed was empty.</p>\n'
   + tbl(('Entry', 'Why it is not zero activity'),
         [('Bank interest credited to a corporate account',
           'Investment income, whatever the amount'),
          ('An annual registry fee paid from the corporate account',
           'An expense'),
          ('Accounting or filing fees paid by the corporation', 'An expense'),
          ('Rent received on a property the corporation owns', 'Rental income'),
          ('A dividend received from another corporation',
           'Income, and it changes the schedules'),
          ('Sale of equipment the corporation still held', 'A disposition')])
   + '\n<p>' + NOT_NIL + '</p>\n'
   '<p>A shareholder paying the registry fee personally, from a personal account, '
   'and not charging it to the corporation, leaves the year zero.</p>'),
  ('bank', 'No Bank Account and No Business Number',
   '<p>Neither changes the filing obligation. A corporation with no bank account '
   'files, and a corporation that was never given a business number files once it '
   'has one.</p>\n'
   '<p>A corporation with no bank account has one advantage on this page: with no '
   'account there is no credited interest, so the most common accidental entry '
   'cannot arise.</p>\n'
   '<p>See ' + a(A + 'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account/',
                 'filing with no bank account') + ' and '
   + a(A + 'do-i-need-a-business-number-to-file-a-nil-t2/',
       'whether a business number is needed') + '.</p>', True),
  ('schedules', 'Which Schedules a Zero-Activity Return Carries',
   '<p>A zero-activity return is not an empty return. Several schedules are filed '
   'carrying zeroes, and one of them is filed only once.</p>\n'
   + tbl(('Schedule', 'On a zero-activity year'),
         [('Schedule 100, the balance sheet', 'Filed, carrying the balances'),
          ('Schedule 125, the income statement', 'Filed, carrying zeroes'),
          ('Schedule 141, the notes checklist', 'Filed'),
          ('Schedule 24', 'On a first return only'),
          ('Schedule 50', 'For every shareholder at 10% or more'),
          ('Schedule 8', 'Filed where the corporation holds depreciable property')])
   + '\n<p>The full set is in the guide to '
   + a(HUB + 't2-schedules-on-a-nil-return/', 'T2 schedules on a nil return')
   + '.</p>'),
  ('gifi', 'Reporting Zeroes Through the GIFI',
   '<p>The General Index of Financial Information is the coded format the balance '
   'sheet and income statement are filed in. A zero-activity year reports through '
   'it the same way a trading year does, with zeroes in the income statement '
   'codes.</p>\n'
   '<p>The balance sheet is rarely all zeroes. Share capital issued on '
   'incorporation, a shareholder loan and retained earnings carried forward all sit '
   'on Schedule 100 whether or not anything happened during the year.</p>\n'
   '<div class="ei-warn"><p>A balance sheet filed as entirely zero when share '
   'capital was issued is wrong, and it is wrong in a way that persists: the next '
   'return opens from the closing balances this one reports.</p></div>\n'
   '<p>See the guide to ' + a(HUB + 'gifi-schedules-100-125-141/',
                              'GIFI Schedules 100, 125 and 141') + '.</p>', True),
  ('short-form', 'The T2 Short on a Zero-Activity Year',
   '<p>The T2 Short is a two-page version of the return available to a '
   'Canadian-controlled private corporation that meets a list of conditions. A '
   'zero-activity year commonly meets them.</p>\n'
   '<p>Meeting the conditions is not automatic. A second permanent establishment, '
   'a reporting currency other than the Canadian dollar, a refundable credit or an '
   'amalgamation in the year each rule it out.</p>\n'
   '<p>Eligibility is set out in the guide to '
   + a(HUB + 't2-short-eligibility/', 'T2 Short eligibility') + '.</p>'),
  ('multiple', 'Several Zero-Activity Years at Once',
   '<p>Each year is its own return on its own form for its own tax year. Six '
   'zero-activity years are six returns, and they are prepared oldest first so the '
   'closing balances of one open the next.</p>\n'
   '<p>They can be prepared and transmitted together. Each is ' + PRICE + '.</p>\n'
   '<p>See ' + a(A + 'can-i-file-five-years-of-nil-t2-returns-at-once/',
                 'filing five years at once') + ' and the guide to '
   + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
       'catching up on unfiled corporate tax returns') + '.</p>', True),
  ('consequences', 'Leaving a Zero-Activity Year Unfiled',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>The year with nothing in it is the one most often left, and it is the one '
   'that blocks a dissolution years later. A corporation cannot be wound up with '
   'an open year on its record, however empty that year was.</p>\n'
   '<p>See ' + a(A + 'what-happens-if-i-dont-file-a-nil-t2/',
                 'what happens if a nil T2 is not filed') + '.</p>'),
  ('moving-on', 'When Activity Starts',
   '<p>The year activity begins is not a zero-activity year, even if it begins in '
   'the last week of it. Revenue in December makes the whole year a trading '
   'year.</p>\n'
   '<p>From that point the return carries real figures, and preparation moves to '
   'Gondaliya CPA Professional Corporation at gondaliyacpa.ca.</p>\n'
   '<p>The transition is covered at '
   + a(SITE + '/when-your-corporation-starts-operating/',
       'when your corporation starts operating') + '.</p>'),
 ],
 faq=[
  ('What Counts as Zero Activity?',
   'No revenue, no expenses, no income of any kind and no disposition of property '
   'during the tax year. The return is filed showing those amounts as $0.00.'),
  ('Does Bank Interest Take a Year Out of Zero Activity?',
   'Yes. Interest credited to a corporate account is investment income whatever '
   'the amount, and a few dollars answers the question the same way a few thousand '
   'would.'),
  ('Is a Zero-Activity Return an Empty Return?',
   'No. The income statement carries zeroes, but the balance sheet carries share '
   'capital, any shareholder loan and retained earnings brought forward, and '
   'Schedule 50 still reports every shareholder at 10% or more.'),
  ('Does a Corporation With No Bank Account Still File?',
   'Yes. The obligation attaches to existing as a corporation. With no account '
   'there is no credited interest, so the year is more likely to be genuinely '
   'zero.'),
  ('Can Six Zero-Activity Years Be Filed Together?',
   'Yes. They are six separate returns prepared oldest first, so the closing '
   'balances of each open the next, and they can be transmitted in one sitting at '
   '$300.00 plus HST per tax year each.'),
  ('What if Activity Started Late in the Year?',
   'The whole year is a trading year. Revenue in December means the return for '
   'that year is not a zero-activity return.'),
 ])

# ---------------------------------------------------------------------------
# Guide 20. /guides/corporate-tax-arrears-and-interest/
# Appendix A topics /the-ultimate-guide-to-corporate-tax-arrears-and-penalties/
# and /2026-canadian-t2-penalty-and-interest-guide/, which are the same topic
# under two naming wrappers. "Penalties" is dropped from the slug in favour of
# "interest": the penalty guide is already live at
# /guides/t2-late-filing-penalties/, and this one is about the balance owing
# rather than the charge for filing late. No interest RATE appears anywhere
# here, because no rate is given in any approved source for this site.
# ---------------------------------------------------------------------------
G20 = dict(
 slug='corporate-tax-arrears-and-interest',
 title='Corporate Tax Arrears and Interest | Canadian Guide',
 h1='The Complete Guide to Corporate Tax Arrears and Interest',
 h1_pre='The Complete Guide to ',
 h1_span='Corporate Tax Arrears and Interest',
 eyebrow='Arrears Guide',
 meta=('What arrears are, what interest attaches to, why a nil year creates '
       'none, and how an unfiled year manufactures a balance that was never owed.'),
 convert=(SITE + '/catch-up-nil-t2-filing/', 'Catch-Up Nil T2 Filing'),
 kids=['what-happens-if-i-dont-file-my-t2-for-five-years',
       'what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2',
       'can-i-file-a-nil-t2-late-without-a-penalty',
       'can-i-catch-up-on-unfiled-t2-returns-without-an-audit',
       'what-happens-if-i-dont-file-a-nil-t2',
       'how-do-i-catch-up-on-years-of-unfiled-t2-returns'],
 sections=[
  ('what', 'What Corporate Tax Arrears Are',
   '<p>Arrears are an unpaid balance on a corporation\'s tax account. The balance '
   'can come from an assessed return, from a reassessment, from an assessment the '
   'Agency raised on its own estimate, or from a charge added to the account.</p>\n'
   '<p>Arrears are a balance, not a filing. A corporation can be years behind on '
   'filing and owe nothing, and it can be fully filed and owe a great deal.</p>\n'
   '<div class="ei-info"><p>Separating the two is the point of this page. The rest '
   'of it is about which one a dormant corporation actually has.</p></div>', True),
  ('interest', 'How Interest Is Charged on an Unpaid Balance',
   '<p>Interest runs on an unpaid balance and compounds daily. It starts from the '
   'day the balance was due and continues until the balance is paid.</p>\n'
   '<p>It attaches to the balance, which means it needs a balance to attach to. '
   'Interest is not charged on a return that was filed late and showed nothing '
   'owing.</p>\n'
   + tbl(('Charge', 'Attaches to', 'Needs'),
         [('Interest', 'An unpaid balance', 'A balance owing'),
          ('Instalment interest', 'Instalments not paid when due',
           'An instalment obligation'),
          ('Percentage late-filing penalty', 'Tax owing on the return',
           'Tax owing')])
   + '\n<p>All three columns describe the same dependency from different sides. '
   'None of the three has anything to work on where the corporation owes '
   '$0.00.</p>'),
  ('nil-balance', 'Why a Nil Year Produces No Arrears',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>A year with no activity assesses at $0.00. There is no balance, so there is '
   'nothing for interest to compound on and nothing for the percentage charge to '
   'be a percentage of.</p>\n'
   '<p>That is the end of the matter only while the year is filed. The next '
   'section is about what happens when it is not.</p>', True),
  ('arbitrary', 'Arbitrary Assessments and Manufactured Arrears',
   '<p>Where a return is not filed and a demand to file goes unanswered, the '
   'Agency may assess the corporation on its own estimate of income. The amount is '
   'an estimate the corporation did not supply.</p>\n'
   '<p>That assessment creates a real balance. Interest then runs on it, and the '
   'corporation is in arrears on a figure it never earned.</p>\n'
   '<div class="ei-warn"><p>This is how a dormant corporation that genuinely owed '
   'nothing ends up with a collectible debt and interest compounding daily. The '
   'balance was not produced by activity. It was produced by the missing '
   'return.</p></div>\n'
   '<p>An arbitrary assessment stands until a filed return displaces it, which '
   'makes filing the only way to remove it. See '
   + a(A + 'what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2/',
       'what happens if a demand to file goes unanswered') + '.</p>'),
  ('instalments', 'Instalment Interest',
   '<p>A corporation with tax owing above the threshold pays by instalments through '
   'the year. Where an instalment is missed or paid short, interest is charged on '
   'the shortfall.</p>\n'
   '<p>A corporation with no activity has no instalment obligation, so it cannot '
   'incur instalment interest. The obligation arises from the previous year\'s tax, '
   'and a nil year sets that at $0.00.</p>\n'
   + tbl(('Year', 'Tax owing', 'Instalments the following year'),
         [('A nil year', '$0.00', 'None required'),
          ('A trading year below the threshold', 'Small', 'None required'),
          ('A trading year above the threshold', 'Above the threshold',
           'Monthly or quarterly')])
   + '\n<p>A corporation emerging from dormancy into a profitable year is the case '
   'to watch, because its instalment position for the following year changes.</p>',
   True),
  ('order', 'The Order Payments Are Applied In',
   '<p>A payment to a tax account is not applied to whichever year the payer had '
   'in mind. It is applied according to the Agency\'s own ordering, and interest '
   'already accrued is generally taken before the balance it accrued on.</p>\n'
   '<p>The practical consequence is that a partial payment reduces a balance more '
   'slowly than the payer expects, because part of it clears interest that then '
   'stops growing only from that date.</p>\n'
   '<p>None of this reaches a corporation whose years are all nil. It matters to a '
   'corporation that traded, stopped, and left a balance behind.</p>'),
  ('relief', 'Taxpayer Relief and What It Covers',
   '<p>The Agency may cancel or waive interest and penalties in defined '
   'circumstances. Relief is discretionary, it is requested in writing, and it is '
   'decided on the facts of the particular account.</p>\n'
   + tbl(('Relief can be requested for', 'Relief does not extend to'),
         [('Interest charged on a balance', 'The underlying tax itself'),
          ('A late-filing penalty', 'The obligation to file the return'),
          ('Charges arising from circumstances beyond the corporation\'s control',
           'A decision not to file')])
   + '\n<p>Relief is not a route around filing. The return still has to be filed, '
   'and a request made while years remain outstanding has little to work with.</p>',
   True),
  ('collections', 'Collections and Director Liability',
   '<p>An assessed balance is collectible. The Agency has statutory collection '
   'powers it can use without going to court, and it can act on a balance produced '
   'by an arbitrary assessment exactly as on one produced by a filed return.</p>\n'
   '<p>Certain amounts a corporation was required to withhold and remit, including '
   'payroll source deductions and net GST/HST, can be assessed against directors '
   'personally. Corporate income tax on its own is not among them.</p>\n'
   '<div class="ei-warn"><p>A dormant corporation with an unclosed payroll or '
   'GST/HST account is the case where this becomes personal. Closing those '
   'accounts is covered in the guide to '
   + a(HUB + 'winding-up-an-inactive-corporation/',
       'winding up an inactive corporation') + '.</p></div>'),
  ('clearing', 'Clearing Arrears Created by an Unfiled Year',
   '<p>Filing the actual return is what removes an arbitrary assessment. The filed '
   'figures displace the estimate, and a nil year reassesses to $0.00.</p>\n'
   '<p>Interest that accrued on the estimated balance falls away with the balance '
   'it was charged on. Where charges remain after reassessment, that is when a '
   'relief request has something definite to address.</p>\n'
   + tbl(('Step', 'Effect'),
         [('File the outstanding year', 'Displaces the estimate'),
          ('The year reassesses at $0.00', 'The balance goes'),
          ('Interest charged on that balance', 'Falls away with it'),
          ('Anything left standing', 'Can be put to a relief request')])
   + '\n<p>Oldest year first, each on its own return. See '
   + a(A + 'how-do-i-catch-up-on-years-of-unfiled-t2-returns/',
       'how to catch up on years of unfiled returns') + '.</p>', True),
  ('statute', 'How Long Arrears Last',
   '<p>A collectible balance does not expire on a fixed anniversary. Collection '
   'limitation periods can be restarted by Agency action and by acknowledgement of '
   'the debt, so a balance left alone is not a balance running down.</p>\n'
   '<p>An unfiled year does not expire at all. There is no point at which it closes '
   'itself, which is why an arbitrary assessment raised years ago can still be '
   'sitting on an account today.</p>'),
  ('avoiding', 'Keeping a Dormant Corporation Out of Arrears',
   '<p>A dormant corporation stays out of arrears by filing each year on time. '
   'That is the whole mechanism: with the year filed at $0.00 there is no estimate, '
   'no balance and nothing to compound.</p>\n'
   '<p>' + NOT_NIL + '</p>\n'
   '<p>Each outstanding year is a separate return at ' + PRICE + '. See the full '
   + a(COST, 'nil T2 filing cost') + '.</p>'),
 ],
 faq=[
  ('Does a Nil Year Create Arrears?',
   'No. A year with no activity assesses at $0.00, so there is no balance for '
   'interest to compound on and nothing for a percentage charge to apply to.'),
  ('How Can a Dormant Corporation Owe Money Then?',
   'Through an arbitrary assessment. Where a return is unfiled and a demand goes '
   'unanswered, the Canada Revenue Agency may assess on its own estimate of '
   'income, and interest then runs on that estimated balance.'),
  ('Does Filing the Return Remove an Arbitrary Assessment?',
   'Yes. The filed figures displace the estimate, a nil year reassesses to $0.00, '
   'and interest charged on the estimated balance falls away with it.'),
  ('Does Interest Run on a Return Filed Late With Nothing Owing?',
   'No. Interest attaches to an unpaid balance, so it needs a balance to attach '
   'to.'),
  ('Can Directors Be Held Personally Liable?',
   'For amounts the corporation was required to withhold and remit, including '
   'payroll source deductions and net GST/HST, yes. Corporate income tax on its '
   'own is not among them.'),
  ('Do Arrears Expire if Left Alone?',
   'A collection limitation period can be restarted by Agency action and by '
   'acknowledgement of the debt, so a balance left alone is not a balance running '
   'down. An unfiled year does not expire at all.'),
 ])

# ---------------------------------------------------------------------------
# Guide 21. /guides/winding-up-an-inactive-corporation/
# Appendix A topic /the-ultimate-guide-to-winding-up-an-inactive-corporation/.
# /guides/final-t2-and-dissolution/ covers the RETURN. This one covers the
# PROCESS around it: the order of operations, the accounts, the assets and the
# registry filing. Kept apart deliberately so the two do not compete.
# ---------------------------------------------------------------------------
G21 = dict(
 slug='winding-up-an-inactive-corporation',
 title='Winding Up an Inactive Corporation | Canadian Guide',
 h1='The Complete Guide to Winding Up an Inactive Corporation',
 h1_pre='The Complete Guide to ',
 h1_span='Winding Up an Inactive Corporation',
 eyebrow='Wind-Up Guide',
 meta=('The order the steps have to happen in, every return due first, the '
       'clearance certificate, closing the accounts and the registry filing.'),
 convert=(SITE + '/final-t2-before-dissolution/', 'Final T2 Before Dissolution'),
 kids=['can-i-dissolve-my-corporation-with-unfiled-t2-returns',
       'how-do-i-dissolve-a-corporation-that-has-never-filed-a-t2',
       'how-do-i-close-my-corporate-tax-account-after-dissolution',
       'what-happens-if-i-dont-file-a-t2-before-dissolving-my-corporation',
       'do-i-need-to-file-a-t2-for-the-year-my-corporation-was-dissolved',
       'can-i-still-file-a-t2-after-my-corporation-was-dissolved'],
 sections=[
  ('two-steps', 'Winding Up Is Two Separate Processes',
   '<p>Closing a corporation involves two authorities that do not talk to each '
   'other on your behalf. The tax side is settled with the Canada Revenue Agency. '
   'The legal existence of the corporation is ended by the registry it was '
   'incorporated under.</p>\n'
   + tbl(('Side', 'Who', 'What it ends'),
         [('Tax', 'Canada Revenue Agency',
           'The filing and remittance obligations'),
          ('Legal', 'The incorporating registry',
           'The corporation\'s existence')])
   + '\n<p>Doing one and not the other is the usual failure. A corporation struck '
   'from a registry with open tax years still has those years open, and a '
   'corporation fully filed but never dissolved keeps acquiring new filing '
   'obligations every year.</p>', True),
  ('order', 'The Order the Steps Have to Happen In',
   '<p>The sequence is not a preference. Each step depends on the one before it, '
   'and taking them out of order is what leaves a wind-up half-finished for '
   'years.</p>\n'
   + tbl(('Order', 'Step', 'Depends on'),
         [('1', 'File every outstanding tax year', 'Nothing'),
          ('2', 'Distribute or dispose of the remaining assets',
           'Knowing the tax position'),
          ('3', 'Request a clearance certificate', 'Step 1 being complete'),
          ('4', 'File articles of dissolution with the registry', 'Step 3'),
          ('5', 'File the final T2', 'The date of dissolution existing'),
          ('6', 'Close the remaining accounts', 'Step 5')])
   + '\n<p>Step 5 comes after step 4 because the final return runs to the date of '
   'dissolution, and that date does not exist until the registry sets it.</p>'),
  ('filings', 'Every Return Due Before You Can Wind Up',
   '<p>A corporation cannot be wound up cleanly with an open year on its record. '
   'Every tax year from incorporation to the present has to be filed, including '
   'the years in which nothing happened.</p>\n'
   '<p>Nine dormant years are nine returns. They are prepared oldest first and can '
   'be transmitted together, each at ' + PRICE + '.</p>\n'
   '<div class="ei-warn"><p>This is the step that stops most wind-ups. The '
   'directors discover the open years at the point of requesting a clearance '
   'certificate, which is the latest possible moment to find out.</p></div>\n'
   '<p>See ' + a(A + 'can-i-dissolve-my-corporation-with-unfiled-t2-returns/',
                 'whether a corporation can be dissolved with unfiled returns')
   + '.</p>', True),
  ('clearance', 'The Clearance Certificate',
   '<p>A clearance certificate is the Agency\'s confirmation that the corporation '
   'has no outstanding amounts. It protects the directors personally: distributing '
   'the corporation\'s property without one can leave them liable for amounts the '
   'corporation turns out to owe.</p>\n'
   '<p>It is requested in writing and it cannot be issued while a year is '
   'unfiled.</p>\n'
   + tbl(('Clearance certificate', 'Position'),
         [('All years filed, nothing owing', 'Can be issued'),
          ('A year unfiled', 'Cannot be issued'),
          ('A balance outstanding', 'Not until the balance is settled'),
          ('Assets already distributed without one',
           'Directors exposed to the corporation\'s liabilities')])
   + '\n<p>A dormant corporation with all years filed at $0.00 is the simplest '
   'case there is for a clearance request.</p>'),
  ('final-t2', 'The Final T2',
   '<p>The final return covers the period from the start of the last tax year to '
   'the date of dissolution. It is due six months after that date.</p>\n'
   '<p>It is marked as the final return, which is what tells the Agency to expect '
   'no further years. Without that marking the account stays open and the '
   'corporation keeps appearing to owe returns.</p>\n'
   '<p>The return itself is covered in full in the guide to '
   + a(HUB + 'final-t2-and-dissolution/', 'the final T2 and dissolution')
   + ', and ' + a(A + 'do-i-need-to-file-a-t2-for-the-year-my-corporation-was-dissolved/',
                  'the year of dissolution')
   + ' answers whether that year is still owed.</p>', True),
  ('accounts', 'Closing the GST/HST and Payroll Accounts',
   '<p>A corporation often has program accounts beyond the corporate income tax '
   'one. Each is closed separately, and each keeps generating obligations until it '
   'is.</p>\n'
   + tbl(('Account', 'Closed by', 'Until it is closed'),
         [('GST/HST', 'Form RC145', 'Nil returns remain due'),
          ('Payroll', 'Form RC145', 'Nil remittances remain expected'),
          ('Corporate income tax', 'The final T2, marked final',
           'T2 returns remain due')])
   + '\n<p>An unclosed payroll or GST/HST account is the one that can reach the '
   'directors personally, because those are amounts the corporation was required '
   'to withhold or collect and remit.</p>\n'
   '<p>Closing the accounts is not covered by the fee on this page. See '
   + a(A + 'how-do-i-close-my-corporate-tax-account-after-dissolution/',
       'closing a corporate tax account after dissolution') + '.</p>'),
  ('assets', 'Distributing Assets Before Dissolution',
   '<p>A corporation cannot be dissolved holding property. Whatever it still owns '
   'is distributed to the shareholders or disposed of first, and both have tax '
   'consequences the final return reports.</p>\n'
   '<div class="ei-danger"><p>A disposition is activity. A corporation that sells '
   'or transfers property in its last period does not have a nil final year, and '
   'that return is handled by Gondaliya CPA Professional Corporation at '
   'gondaliyacpa.ca at $350.00 plus HST per year.</p></div>\n'
   '<p>A genuinely empty corporation, holding nothing but perhaps a nominal share '
   'balance, has nothing to distribute and a nil final year.</p>'),
  ('articles', 'Articles of Dissolution',
   '<p>The registry ends the corporation\'s existence on receiving articles of '
   'dissolution, and the date it records is the date the final tax period runs '
   'to.</p>\n'
   '<p>The registry is the one the corporation was incorporated under: the federal '
   'registry for a federally incorporated corporation, and the provincial registry '
   'otherwise. Filing with the wrong one achieves nothing.</p>\n'
   + tbl(('Incorporated', 'Dissolved through', 'Separate annual return'),
         [('Federally', 'The federal registry', 'Yes, with its own fee'),
          ('In a province', 'That province\'s registry',
           'Depends on the province')])
   + '\n<p>The annual return is a registry filing and not a tax return. See the '
   'guide to ' + a(HUB + 'provincial-and-federal-annual-returns/',
                   'provincial and federal annual returns') + '.</p>', True),
  ('after', 'What Can Still Arrive After Dissolution',
   '<p>Dissolution does not seal the record. An assessment, a reassessment or a '
   'demand relating to a period before dissolution can still be issued, and a '
   'return for a pre-dissolution year can still be filed.</p>\n'
   '<p>Keeping the clearance certificate and the dissolution record is what makes '
   'those straightforward to deal with.</p>\n'
   '<p>See ' + a(A + 'can-i-still-file-a-t2-after-my-corporation-was-dissolved/',
                 'filing a T2 after dissolution') + ' and '
   + a(A + 'what-happens-if-i-dont-file-t2-returns-after-my-corporation-is-dissolved/',
       'returns left unfiled after dissolution') + '.</p>'),
  ('revival', 'Revival and Involuntary Dissolution',
   '<p>A corporation struck by a registry for failing to file its annual return '
   'has not been wound up. It has been dissolved involuntarily, with its tax years '
   'still open and nothing settled.</p>\n'
   '<p>Registries provide for revival, which restores the corporation so the '
   'outstanding filings can be made and a proper wind-up completed. The open tax '
   'years survived the striking and are waiting.</p>\n'
   '<div class="ei-info"><p>A corporation found in this state is usually in it '
   'because the annual return lapsed, not because anyone decided to close it. The '
   'tax years are the part nobody looked at.</p></div>\n'
   '<p>See ' + a(A + 'how-do-i-dissolve-a-corporation-that-has-never-filed-a-t2/',
                 'dissolving a corporation that never filed') + '.</p>', True),
  ('records', 'Keeping the Records Afterwards',
   '<p>Corporate records are kept after dissolution, not discarded with it. The '
   'books, the returns, the clearance certificate and the dissolution record all '
   'remain relevant for years.</p>\n'
   '<p>Form T183CORP for each year filed here is retained for six years and is '
   'never backdated. The signing record is covered in the guide to '
   + a(HUB + 't183corp-signing-and-transmission/',
       'Form T183CORP signing and transmission') + '.</p>'),
 ],
 faq=[
  ('Can I Dissolve a Corporation With Unfiled T2 Returns?',
   'Not cleanly. A clearance certificate cannot be issued while a year is '
   'unfiled, and distributing the corporation\'s property without one can leave '
   'the directors personally liable.'),
  ('What Order Do the Steps Go In?',
   'File every outstanding year, deal with the remaining assets, request a '
   'clearance certificate, file articles of dissolution, then file the final T2 '
   'and close the remaining accounts. The final return runs to the dissolution '
   'date, so it comes after the registry sets that date.'),
  ('Is a Clearance Certificate Compulsory?',
   'It is not a filing requirement, but distributing the corporation\'s property '
   'without one exposes the directors to amounts the corporation turns out to owe. '
   'For a dormant corporation with every year filed at $0.00 it is the simplest '
   'case there is.'),
  ('Do I Have to Close the GST/HST and Payroll Accounts Separately?',
   'Yes. Each is closed with Form RC145, and until it is closed nil returns and '
   'nil remittances remain due on it. Those closures are not covered by the fee '
   'for a nil T2.'),
  ('What if the Registry Already Struck the Corporation?',
   'It was dissolved involuntarily and its tax years are still open. Registries '
   'provide for revival, which restores the corporation so the outstanding '
   'filings can be made and a proper wind-up completed.'),
  ('Does Dissolution Close the Tax Record?',
   'No. An assessment, a reassessment or a demand relating to a pre-dissolution '
   'period can still be issued, and a return for such a year can still be filed.'),
 ])

# ---------------------------------------------------------------------------
# Guide 22. /guides/small-business-corporate-filing/
# Appendix A topic /2026-canadian-small-business-corporate-filing-guide/, year
# token dropped per 6(k). This is the orientation page for a director who does
# not yet know which of the filings apply to them, so it is the one guide that
# deliberately covers the non-tax filings alongside the T2.
# ---------------------------------------------------------------------------
G22 = dict(
 slug='small-business-corporate-filing',
 title='Small Business Corporate Filing | Canadian Guide',
 h1='The Complete Guide to Small Business Corporate Filing',
 h1_pre='The Complete Guide to ',
 h1_span='Small Business Corporate Filing',
 eyebrow='Small Business Guide',
 meta=('Everything a small Canadian corporation files each year, which of it is '
       'tax and which is registry, and how to tell a nil year from a trading one.'),
 convert=(SITE + '/nil-t2-filing/', 'Nil T2 Filing Services'),
 kids=['can-i-file-a-nil-t2-myself-without-an-accountant',
       'do-i-need-financial-statements-for-a-nil-t2-return',
       'do-i-need-a-business-number-to-file-a-nil-t2',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'when-should-i-file-my-first-t2-after-incorporating',
       'how-do-i-file-a-nil-t2-return-in-canada'],
 sections=[
  ('obligation', 'What Every Small Corporation Owes Each Year',
   '<p>A small corporation faces a short list of recurring obligations. Not all of '
   'them are tax, and the ones that are not catch people out more often than the '
   'ones that are.</p>\n'
   + tbl(('Filing', 'Type', 'Applies'),
         [('The T2 corporate income tax return', 'Tax', 'Every year, always'),
          ('The annual return', 'Registry',
           'Every year in most jurisdictions'),
          ('Provincial corporate return', 'Tax',
           'Alberta and Quebec, separately'),
          ('GST/HST return', 'Tax', 'Where the corporation has an account'),
          ('Payroll remittances and T4s', 'Tax',
           'Where the corporation has an account')])
   + '\n<p>The first row is the only one that applies to every corporation in '
   'every year without exception.</p>', True),
  ('nil-or-not', 'Deciding Whether Your Year Is Nil',
   '<p>The return is nil where the corporation had no revenue, no expenses, no '
   'income of any kind and no disposition of property in the tax year. Amount does '
   'not come into it.</p>\n'
   '<p>' + NOT_NIL + '</p>\n'
   '<p>The entries that most often take a year out of nil are bank interest '
   'credited to a corporate account and a registry fee paid from it. The full test '
   'is in the guide to ' + a(HUB + 'zero-activity-corporate-tax-returns/',
                             'zero-activity corporate tax returns') + '.</p>'),
  ('t2-short', 'The T2 Short and Who Qualifies',
   '<p>The T2 Short is a two-page return available to a Canadian-controlled private '
   'corporation meeting a list of conditions. A small corporation with a quiet year '
   'commonly meets them.</p>\n'
   + tbl(('Condition', 'Requirement'),
         [('Corporation type', 'Canadian-controlled private corporation'),
          ('Permanent establishments', 'One only'),
          ('Reporting currency', 'Canadian dollars'),
          ('Refundable credits claimed', 'None'),
          ('Amalgamation in the year', 'None')])
   + '\n<p>Eligibility is tested year by year. See the guide to '
   + a(HUB + 't2-short-eligibility/', 'T2 Short eligibility') + '.</p>', True),
  ('schedules', 'The Schedules a Small Corporation Files',
   '<p>The return is not the whole filing. Several schedules accompany it, and one '
   'of them appears only on a first return.</p>\n'
   + tbl(('Schedule', 'Reports', 'When'),
         [('100', 'The balance sheet', 'Every year'),
          ('125', 'The income statement', 'Every year'),
          ('141', 'The notes checklist', 'Every year'),
          ('24', 'First-time filer information', 'The first return only'),
          ('50', 'Shareholders at 10% or more', 'Where there are any'),
          ('8', 'Capital cost allowance',
           'Where depreciable property is held')])
   + '\n<p>Full detail is in the guide to '
   + a(HUB + 't2-schedules-on-a-nil-return/', 'T2 schedules on a nil return')
   + '.</p>'),
  ('ccpc', 'Canadian-Controlled Private Corporation Status',
   '<p>Most small Canadian corporations are Canadian-controlled private '
   'corporations, and the status matters on a nil return for one reason: it is a '
   'condition of the T2 Short.</p>\n'
   '<p>The status turns on who controls the corporation and whether its shares are '
   'publicly traded. A corporation controlled by non-residents or by a public '
   'corporation does not have it.</p>\n'
   '<div class="ei-info"><p>Where the status is absent the return is a full T2 '
   'rather than the short form, and the figures reported are the same.</p></div>',
   True),
  ('annual-returns', 'The Annual Return Is a Separate Filing',
   '<p>The annual return is filed with the registry the corporation was '
   'incorporated under. It confirms the directors, the registered office and the '
   'corporation\'s continued existence. It reports no income and it is not a tax '
   'return.</p>\n'
   '<p>Missing it is what gets a corporation struck from a registry, which is a '
   'different and more abrupt problem than an unfiled T2.</p>\n'
   '<p>It is not covered by the fee on this page. See the guide to '
   + a(HUB + 'provincial-and-federal-annual-returns/',
       'provincial and federal annual returns') + '.</p>'),
  ('gst-payroll', 'GST/HST and Payroll Accounts',
   '<p>These exist only where the corporation registered for them, and once they '
   'exist they generate obligations independently of the T2.</p>\n'
   + tbl(('Account', 'Obligation while open', 'Closed by'),
         [('GST/HST', 'Returns remain due, nil ones included', 'Form RC145'),
          ('Payroll', 'Remittances remain expected, nil ones included',
           'Form RC145')])
   + '\n<p>A dormant corporation with an open GST/HST account owes nil GST/HST '
   'returns as well as its nil T2. Neither closure is covered by the fee on this '
   'page.</p>', True),
  ('records', 'Records a Small Corporation Keeps',
   '<p>Books and records are kept whether or not the corporation traded, and a nil '
   'year still has records: the bank statements that show no movement, the registry '
   'filings and the minute book.</p>\n'
   '<p>A nil T2 does not require prepared financial statements. The balance sheet '
   'and income statement are reported through the coded GIFI format on the return '
   'itself.</p>\n'
   '<p>See ' + a(A + 'do-i-need-financial-statements-for-a-nil-t2-return/',
                 'whether financial statements are needed') + '.</p>'),
  ('first-year', 'The First Year After Incorporating',
   '<p>The first tax year runs from incorporation to the chosen year-end and may '
   'not exceed 53 weeks. The first return filed is what fixes the year-end, and '
   'Schedule 24 appears on it.</p>\n'
   '<p>Many first years are nil, because the corporation was set up before trading '
   'began. A nil first year is filed exactly as any other.</p>\n'
   '<p>See the guide to ' + a(HUB + 'first-year-t2-filing/',
                              'first-year T2 filing') + ' and '
   + a(A + 'when-should-i-file-my-first-t2-after-incorporating/',
       'when the first T2 is due') + '.</p>', True),
  ('dormant-years', 'Dormant Years Between Active Ones',
   '<p>A corporation that traded, stopped and may trade again files a nil return '
   'for each quiet year. The earlier trading does not change what the quiet year '
   'is.</p>\n'
   '<p>Each year is assessed on its own facts, so a nil year sitting between two '
   'trading years is still a nil year.</p>\n'
   '<p>See the guide to ' + a(HUB + 'dormant-and-inactive-corporations/',
                              'dormant and inactive corporations') + '.</p>'),
  ('growing', 'When the Corporation Outgrows a Nil Return',
   '<p>The year revenue arrives is a trading year, whatever month it arrives in. '
   'From that point the return carries real figures and real schedules.</p>\n'
   '<p>Filing then moves to Gondaliya CPA Professional Corporation at '
   'gondaliyacpa.ca, at $350.00 plus HST per year.</p>\n'
   '<p>The handover is described at '
   + a(SITE + '/when-your-corporation-starts-operating/',
       'when your corporation starts operating') + '.</p>', True),
 ],
 faq=[
  ('What Does a Small Corporation Have to File Every Year?',
   'The T2 corporate income tax return, always. In most jurisdictions an annual '
   'return with the registry as well, and separately the Alberta AT1 or the Quebec '
   'CO-17 where the corporation is in those provinces.'),
  ('Is the Annual Return the Same as the T2?',
   'No. The annual return is a registry filing confirming the directors, the '
   'registered office and the corporation\'s existence. It reports no income and '
   'missing it is what gets a corporation struck from a registry.'),
  ('Do I Need Financial Statements for a Nil T2?',
   'No. The balance sheet and income statement are reported through the coded GIFI '
   'format on the return itself, so no separately prepared statements are '
   'required.'),
  ('Can I File a Nil T2 Myself?',
   'A director can, but for tax years starting after 2023 electronic filing is '
   'mandatory for virtually all corporations, and a paper return draws a flat '
   'charge. Returns here are transmitted electronically by a registered EFILE '
   'electronic filer.'),
  ('Does an Open GST/HST Account Matter on a Dormant Corporation?',
   'Yes. While the account is open, GST/HST returns remain due including nil ones, '
   'separately from the T2. It is closed with Form RC145.'),
  ('What Happens When the Corporation Starts Trading?',
   'That whole year is a trading year, whatever month the revenue arrives in. '
   'Filing moves to Gondaliya CPA Professional Corporation at gondaliyacpa.ca at '
   '$350.00 plus HST per year.'),
 ])

# ---------------------------------------------------------------------------
# Guide 23. /guides/corporate-compliance-calendar/
# Appendix A topic /2026-canadian-corporate-compliance-calendar-guide/, year
# token dropped per 6(k). Dropping it matters here for a second reason: a
# calendar guide carrying a year in its slug would need replacing annually,
# which is exactly the churn the year-stamp rule exists to prevent. No fixed
# calendar dates are given, because they depend on the corporation's own
# year-end; the guide teaches the derivation instead.
# ---------------------------------------------------------------------------
G23 = dict(
 slug='corporate-compliance-calendar',
 title='Corporate Compliance Calendar | Canadian Guide',
 h1='The Complete Guide to the Corporate Compliance Calendar',
 h1_pre='The Complete Guide to the ',
 h1_span='Corporate Compliance Calendar',
 eyebrow='Compliance Guide',
 meta=('Every recurring date a Canadian corporation owes, which ones derive '
       'from your year-end, and the shortest calendar a dormant corporation keeps.'),
 convert=(SITE + '/deadlines/', 'Every T2 Deadline by Year-End'),
 kids=['do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'how-do-i-find-out-which-t2-years-are-outstanding',
       'when-should-i-file-my-first-t2-after-incorporating',
       'when-should-i-file-a-nil-t2-for-a-short-first-tax-year',
       'what-happens-if-i-dont-report-a-dormant-corporation-to-cra',
       'how-do-i-fix-a-nil-t2-return-i-filed-with-the-wrong-year-end'],
 sections=[
  ('what', 'What Belongs on a Corporate Compliance Calendar',
   '<p>A compliance calendar holds the dates a corporation owes something to '
   'somebody, whether or not it traded. Two kinds of date sit on it, and they '
   'behave differently.</p>\n'
   + tbl(('Kind of date', 'Derived from', 'Example'),
         [('Year-end driven', 'The corporation\'s own fiscal year-end',
           'The T2 deadline'),
          ('Anniversary driven', 'The date of incorporation',
           'The annual return in some registries'),
          ('Fixed calendar', 'The calendar year',
           'The T4 deadline at the end of February')])
   + '\n<p>No two corporations have the same calendar unless they share a '
   'year-end and an incorporation date, which is why a calendar has to be derived '
   'rather than copied.</p>', True),
  ('t2', 'The T2 Deadline',
   '<p>Six months after the fiscal year-end, every year, for every corporation. '
   'This is the one date on the calendar that never has an exception.</p>\n'
   '<p>A balance of tax, where there is one, is due earlier: two months after the '
   'year-end, or three for a Canadian-controlled private corporation meeting the '
   'conditions. A corporation with no activity has no balance.</p>\n'
   '<p>Every year-end and its due date is listed on '
   + a(SITE + '/deadlines/', 'the deadlines page') + ', and the rules behind them '
   'are in the guide to ' + a(HUB + 't2-filing-deadlines/', 'T2 filing deadlines')
   + '.</p>'),
  ('annual-return', 'The Annual Return Deadline',
   '<p>The annual return is a registry filing. It confirms the directors, the '
   'registered office and that the corporation still exists, and it reports no '
   'income.</p>\n'
   '<p>Its date is set by the registry rather than by the tax year, and it is '
   'commonly tied to the anniversary of incorporation. A federally incorporated '
   'corporation files one with its own fee.</p>\n'
   '<div class="ei-warn"><p>This is the filing whose absence gets a corporation '
   'struck from a registry. A corporation can be perfectly current on tax and '
   'still be dissolved involuntarily for missing it.</p></div>\n'
   '<p>See the guide to ' + a(HUB + 'provincial-and-federal-annual-returns/',
                              'provincial and federal annual returns') + '.</p>',
   True),
  ('provincial', 'Provincial Returns and Their Own Dates',
   '<p>Two provinces collect corporate income tax on their own returns, filed '
   'separately from the T2 and on their own deadlines.</p>\n'
   + tbl(('Province', 'Return', 'Relationship to the T2'),
         [('Alberta', 'AT1', 'A separate return with its own deadline'),
          ('Quebec', 'CO-17', 'A separate return with its own deadline'),
          ('Elsewhere', 'None',
           'Provincial tax is calculated within the T2')])
   + '\n<p>Neither the AT1 nor the CO-17 is covered by the fee on this page, and '
   'neither is satisfied by filing the T2.</p>'),
  ('gst', 'GST/HST Filing Dates',
   '<p>A corporation with a GST/HST account files on the frequency assigned to it: '
   'monthly, quarterly or annually. The frequency determines the dates, and the '
   'account generates them whether or not there was any activity.</p>\n'
   '<p>A nil GST/HST return is still a return. It does not disappear because there '
   'was nothing to report, and it is not covered by the fee for a nil T2.</p>\n'
   '<p>The account is closed with Form RC145, which is the only thing that stops '
   'the dates recurring.</p>', True),
  ('payroll', 'Payroll Remittance and the T4',
   '<p>A payroll account carries two kinds of date: the remittance dates through '
   'the year and the annual information return.</p>\n'
   + tbl(('Obligation', 'Timing', 'With no employees'),
         [('Source deduction remittances', 'On the assigned frequency',
           'Nil remittances expected'),
          ('T4 information return', 'The end of February',
           'Still expected while the account is open')])
   + '\n<p>Remittance amounts are the ones that can be assessed against directors '
   'personally, which makes an unused open payroll account worth closing rather '
   'than ignoring.</p>'),
  ('year-end-change', 'Changing a Fiscal Year-End',
   '<p>A year-end is fixed by the first return filed and changing it needs the '
   'written approval of the Canada Revenue Agency. The change is not made by '
   'filing a return with a different date on it.</p>\n'
   '<p>An approved change produces a short tax year, and the whole calendar moves '
   'with it: the T2 date, the balance date and the instalment pattern all shift.</p>\n'
   '<p>See ' + a(A + 'how-do-i-fix-a-nil-t2-return-i-filed-with-the-wrong-year-end/',
                 'fixing a return filed with the wrong year-end') + '.</p>', True),
  ('registered-office', 'Registered Office and Director Changes',
   '<p>These are not annual dates. They are event-driven, and the clock starts '
   'when the change happens rather than at a year-end.</p>\n'
   '<p>A registry has to be told within a set period of a change of registered '
   'office or of directors. A corporation whose registered address is stale is a '
   'corporation that does not receive the registry notice warning it is about to '
   'be struck.</p>\n'
   '<div class="ei-info"><p>A dormant corporation is the most likely to have a '
   'stale address, because nobody is checking the post at an office nobody '
   'uses.</p></div>'),
  ('minute-book', 'The Minute Book and Annual Resolutions',
   '<p>The minute book holds the articles, the register of directors and '
   'shareholders, the share certificates and the resolutions. It is maintained '
   'whether or not the corporation traded.</p>\n'
   '<p>Annual resolutions are passed each year even in a dormant corporation: the '
   'shareholders consider the year, appoint or reappoint directors, and record the '
   'decision. A nil year has a short minute, not no minute.</p>\n'
   '<p>Shareholdings recorded there are what Schedule 50 reports. See the guide to '
   + a(HUB + 'schedule-50-and-shareholder-reporting/',
       'Schedule 50 and shareholder reporting') + '.</p>', True),
  ('dormant', 'The Shortest Calendar a Dormant Corporation Can Keep',
   '<p>Once the unused accounts are closed, a dormant corporation\'s calendar '
   'reduces to two recurring items and one maintained record.</p>\n'
   + tbl(('Item', 'Frequency', 'Consequence of missing it'),
         [('The nil T2', 'Annually, six months after year-end',
           'The year stays open indefinitely'),
          ('The annual return', 'Annually, per the registry',
           'The corporation can be struck'),
          ('The minute book', 'Maintained',
           'Gaps in the corporate record')])
   + '\n<p>That is the floor. It cannot be reduced further while the corporation '
   'exists, and the only way to end it is to wind the corporation up.</p>\n'
   '<p>See the guide to ' + a(HUB + 'winding-up-an-inactive-corporation/',
                              'winding up an inactive corporation') + '.</p>'),
  ('building', 'Building Your Own Calendar From Your Year-End',
   '<p>Take the year-end on record, add six months for the T2, add the registry '
   'date for the annual return, and add the frequency dates for any account still '
   'open. Everything else is event-driven.</p>\n'
   '<p>' + NOT_NIL + '</p>\n'
   '<p>Each nil T2 year is ' + PRICE + '. Years already past are worked out by '
   + a(A + 'how-do-i-find-out-which-t2-years-are-outstanding/',
       'finding out which years are outstanding') + '.</p>', True),
 ],
 faq=[
  ('What Dates Does a Dormant Corporation Actually Owe?',
   'Once unused accounts are closed, two recurring filings: the nil T2 six months '
   'after each fiscal year-end, and the annual return on the registry\'s date. The '
   'minute book is maintained alongside them.'),
  ('Is the Annual Return on the Same Date as the T2?',
   'No. The T2 is six months after the fiscal year-end. The annual return is set '
   'by the registry and is commonly tied to the anniversary of incorporation.'),
  ('Can I Change My Fiscal Year-End to Make the Calendar Simpler?',
   'Only with the written approval of the Canada Revenue Agency. Filing a return '
   'with a different date on it does not change the year-end on record.'),
  ('Do I Still Owe GST/HST Returns With No Activity?',
   'Yes, while the account is open. A nil GST/HST return is still a return, and it '
   'is separate from the nil T2. The account is closed with Form RC145.'),
  ('Do I Need Annual Resolutions in a Dormant Year?',
   'Yes. The shareholders still consider the year and record the decision. A nil '
   'year has a short minute rather than no minute.'),
  ('Why Does the Registered Office Address Matter?',
   'Because that is where a registry sends the notice warning that a corporation '
   'is about to be struck for a missed annual return. A dormant corporation is the '
   'most likely to have a stale address on file.'),
 ])

# ---------------------------------------------------------------------------
# Guide 24. /guides/numbered-company-maintenance/
# Appendix A topic /2026-canadian-numbered-company-maintenance-guide/, year
# token dropped per 6(k). /guides/numbered-company-tax-filing/ covers the
# RETURN for a numbered company. This covers keeping one alive between
# returns, so the two divide along the same line as guides 21 and 4.
# ---------------------------------------------------------------------------
G24 = dict(
 slug='numbered-company-maintenance',
 title='Numbered Company Maintenance | Canadian Guide',
 h1='The Complete Guide to Numbered Company Maintenance',
 h1_pre='The Complete Guide to ',
 h1_span='Numbered Company Maintenance',
 eyebrow='Numbered Company Guide',
 meta=('Keeping a numbered company current between returns: the registry, the '
       'registered office, the minute book and the years nobody filed.'),
 convert=(SITE + '/dormant-corporation-filing/', 'Dormant Corporation Filing'),
 kids=['what-happens-if-i-dont-file-a-nil-t2-for-a-numbered-company',
       'can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about',
       'do-i-need-a-business-number-to-file-a-nil-t2',
       'how-do-i-know-if-my-corporation-counts-as-dormant',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'how-do-i-find-out-which-t2-years-are-outstanding'],
 sections=[
  ('what', 'What a Numbered Company Is',
   '<p>A numbered company is a corporation that was incorporated without choosing '
   'a name, so the registry assigned it a number instead. In Ontario that reads as '
   'a seven-digit number followed by Ontario Inc.</p>\n'
   '<p>The number is the corporation\'s legal name. It is not a placeholder and it '
   'does not need replacing.</p>\n'
   '<div class="ei-info"><p>Incorporating with a number is a deliberate choice, '
   'often because a name search was not wanted or the corporation was set up to '
   'hold something rather than to trade under a brand.</p></div>', True),
  ('same-rules', 'A Number Changes Nothing About Filing',
   '<p>Every obligation a named corporation has, a numbered one has identically. '
   'The return, the schedules, the deadlines and the annual return are the '
   'same.</p>\n'
   + tbl(('Obligation', 'Named corporation', 'Numbered corporation'),
         [('Annual T2', 'Yes', 'Yes'),
          ('Nil return when inactive', 'Yes', 'Yes'),
          ('Six-month deadline', 'Yes', 'Yes'),
          ('Annual return with the registry', 'Yes', 'Yes'),
          ('Dissolution to end the obligations', 'Yes', 'Yes')])
   + '\n<p>The guide to ' + a(HUB + 'numbered-company-tax-filing/',
                              'numbered company tax filing')
   + ' covers the return itself.</p>'),
  ('finding', 'Finding Your Corporation Number and Business Number',
   '<p>Two different numbers are in play, issued by two different bodies, and they '
   'are routinely confused.</p>\n'
   + tbl(('Number', 'Issued by', 'Used for'),
         [('Corporation number', 'The incorporating registry',
           'Registry filings and the corporation\'s identity'),
          ('Business number', 'The Canada Revenue Agency',
           'Tax accounts, including the T2')])
   + '\n<p>A corporation can have a corporation number and no business number if '
   'it never registered for anything. The business number is obtained before the '
   'first return is transmitted.</p>\n'
   '<p>See ' + a(A + 'do-i-need-a-business-number-to-file-a-nil-t2/',
                 'whether a business number is needed to file') + '.</p>', True),
  ('annual', 'The Annual Return and the Registry',
   '<p>The annual return keeps the corporation on the register. It confirms the '
   'directors, the registered office and that the corporation still exists, and it '
   'reports no income.</p>\n'
   '<p>A numbered company is the most common casualty of a missed annual return, '
   'because there is no trading activity reminding anyone it exists.</p>\n'
   '<div class="ei-warn"><p>Missing it does not produce a charge. It produces a '
   'striking: the registry dissolves the corporation involuntarily, while its tax '
   'years stay open and unsettled.</p></div>\n'
   '<p>See the guide to ' + a(HUB + 'provincial-and-federal-annual-returns/',
                              'provincial and federal annual returns') + '.</p>'),
  ('registered-office', 'Keeping the Registered Office Current',
   '<p>The registered office is the address the registry and the Agency write to. '
   'A change has to be filed within the period the registry sets.</p>\n'
   '<p>A numbered holding company whose registered office is a former accountant\'s '
   'address, or a home the shareholder moved out of, receives nothing. The warning '
   'that it is about to be struck goes to an address nobody reads.</p>\n'
   '<p>This is the least demanding piece of maintenance there is, and the one most '
   'often left.</p>', True),
  ('directors', 'Director Records',
   '<p>Directors are recorded with the registry and changes are filed when they '
   'happen. A corporation whose sole director has died or resigned without a '
   'replacement is not properly constituted.</p>\n'
   '<p>Directors remain exposed to certain corporate amounts, including payroll '
   'source deductions and net GST/HST, which makes an accurate record a matter of '
   'personal interest rather than paperwork.</p>\n'
   + tbl(('Event', 'Filed with the registry', 'Timing'),
         [('A director appointed', 'Yes', 'Within the registry\'s period'),
          ('A director resigned', 'Yes', 'Within the registry\'s period'),
          ('A director\'s address changed', 'Yes',
           'Within the registry\'s period')])
   + '\n<p>None of these are tax filings and none are covered by the fee on this '
   'page.</p>'),
  ('minute-book', 'The Minute Book',
   '<p>The minute book holds the articles, the registers of directors and '
   'shareholders, the share certificates and the resolutions. It is the '
   'corporation\'s own record of itself.</p>\n'
   '<p>It is maintained through dormant years. Annual resolutions are still passed, '
   'and the shareholdings recorded in it are what Schedule 50 reports on the '
   'return.</p>\n'
   '<p>See the guide to ' + a(HUB + 'schedule-50-and-shareholder-reporting/',
                              'Schedule 50 and shareholder reporting') + '.</p>',
   True),
  ('nil-years', 'Nil Years on a Numbered Company',
   '<p>A numbered company that holds nothing and does nothing files a nil T2 for '
   'every tax year, six months after each year-end, until it is dissolved.</p>\n'
   '<p>' + NOT_NIL + '</p>\n'
   '<p>Each year is ' + PRICE + '. See '
   + a(A + 'what-happens-if-i-dont-file-a-nil-t2-for-a-numbered-company/',
       'what happens when a numbered company does not file') + '.</p>'),
  ('forgotten', 'The Forgotten Numbered Company',
   '<p>A numbered company set up years ago for a purpose that never materialised is '
   'the commonest version of this. Nobody traded through it, nobody filed for it, '
   'and it has been quietly accruing open years.</p>\n'
   '<p>Those years can all be filed. They are prepared oldest first and transmitted '
   'together, and a corporation nobody used has the simplest possible set of '
   'figures.</p>\n'
   '<div class="ei-info"><p>Finding the corporation number, the year-end on record '
   'and the list of open years is the first step, and it is usually the only part '
   'that takes any effort.</p></div>\n'
   '<p>See ' + a(A + 'can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about/',
                 'filing for a corporation you forgot about') + ' and the guide to '
   + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
       'catching up on unfiled corporate tax returns') + '.</p>', True),
  ('name', 'Adding an Operating Name Later',
   '<p>A numbered company can register a business name to trade under without '
   'changing its legal name. The number remains the corporation\'s name on every '
   'filing.</p>\n'
   '<p>Registering a business name is a registry matter and has no effect on the '
   'T2. The return continues to be filed in the corporation\'s numbered name.</p>\n'
   '<p>Trading under the new name is, of course, trading. That year is not a nil '
   'year.</p>'),
  ('closing', 'Closing a Numbered Company',
   '<p>Maintenance ends only at dissolution. Until then the corporation exists and '
   'acquires a new filing obligation every year, whether or not anyone is '
   'attending to it.</p>\n'
   '<p>Every outstanding year is filed first, then a clearance certificate, then '
   'articles of dissolution, then the final T2 running to the dissolution '
   'date.</p>\n'
   '<p>The sequence is in the guide to '
   + a(HUB + 'winding-up-an-inactive-corporation/',
       'winding up an inactive corporation') + '.</p>', True),
 ],
 faq=[
  ('Is a Numbered Company Treated Differently by the Agency?',
   'No. Every obligation a named corporation has, a numbered one has identically: '
   'the return, the schedules, the deadlines and the annual return.'),
  ('What Is the Difference Between a Corporation Number and a Business Number?',
   'The corporation number is issued by the incorporating registry and is used for '
   'registry filings. The business number is issued by the Canada Revenue Agency '
   'and is used for tax accounts, including the T2.'),
  ('What Happens if a Numbered Company Misses Its Annual Return?',
   'The registry can dissolve it involuntarily. That is a striking rather than a '
   'charge, and the corporation\'s tax years stay open and unsettled afterwards.'),
  ('Does a Numbered Company That Holds Nothing Still File?',
   'Yes, a nil T2 for every tax year, six months after each year-end, until it is '
   'formally dissolved.'),
  ('Can I File for a Numbered Company I Forgot I Had?',
   'Yes. The open years are prepared oldest first and can be transmitted together. '
   'A corporation nobody used has the simplest possible set of figures.'),
  ('Can a Numbered Company Trade Under a Name?',
   'It can register a business name to trade under while its legal name remains '
   'the number. Registering the name has no effect on the T2, though trading under '
   'it means that year is not nil.'),
 ])

# ---------------------------------------------------------------------------
# Guide 25. /guides/mandatory-t2-electronic-filing/
# NOT an Appendix A topic. Added because the e-filing mandate and its two flat
# charges are stated on the form page, the pricing page and several guides
# without being explained in full anywhere, and because the Family 13 post
# /blog/mandatory-t2-e-filing-after-2023/ is live with nothing to link up to.
# This is the one page on the site where a flat charge applies to a nil return
# in full, so hard rule 3's qualification block sits next to it rather than
# somewhere further down.
# ---------------------------------------------------------------------------
G25 = dict(
 slug='mandatory-t2-electronic-filing',
 title='Mandatory T2 Electronic Filing | Canadian Guide',
 h1='The Complete Guide to Mandatory T2 Electronic Filing',
 h1_pre='The Complete Guide to ',
 h1_span='Mandatory T2 Electronic Filing',
 eyebrow='Electronic Filing Guide',
 meta=('The rule for tax years starting after 2023, the flat charge for filing '
       'on paper, why a nil return is not exempt, and how transmission works.'),
 convert=(SITE + '/nil-t2-filing/', 'Nil T2 Filing Services'),
 kids=['can-i-file-a-nil-t2-myself-without-an-accountant',
       'how-do-i-file-a-nil-t2-return-in-canada',
       'how-do-i-fix-a-nil-t2-return-i-filed-with-the-wrong-year-end',
       'do-i-need-financial-statements-for-a-nil-t2-return',
       'do-i-need-a-business-number-to-file-a-nil-t2',
       'what-happens-if-i-dont-file-a-nil-t2'],
 sections=[
  ('rule', 'The Rule for Tax Years Starting After 2023',
   '<p>For tax years beginning after 2023, electronic filing of the T2 is '
   'mandatory for virtually all corporations. It is not a preference and it is not '
   'limited to large corporations.</p>\n'
   '<p>The change removed a threshold that had previously exempted smaller '
   'corporations from mandatory electronic filing. The obligation now reaches '
   'almost every corporation that files a T2 at all.</p>\n'
   '<div class="ei-info"><p>The rule is about the method, not the content. A '
   'return with nothing in it is transmitted electronically exactly as a return '
   'with everything in it.</p></div>', True),
  ('who', 'Which Corporations It Applies To',
   '<p>Virtually all of them. The exceptions are narrow and defined, and a '
   'corporation with no activity is not among them.</p>\n'
   + tbl(('Corporation', 'Electronic filing'),
         [('Trading, any size', 'Mandatory'),
          ('Dormant, filing nil returns', 'Mandatory'),
          ('A numbered company holding nothing', 'Mandatory'),
          ('Filing a first return', 'Mandatory'),
          ('Filing a final return before dissolution', 'Mandatory')])
   + '\n<p>Every row above is a corporation this site files for, and every one of '
   'them is transmitted electronically.</p>'),
  ('paper-penalty', 'The Paper Filing Penalty',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>That block is about filing late. The charge for filing on paper is a '
   'different thing entirely, and it is the reason this guide exists: a paper T2 '
   'draws a flat $1,000.00, and a flat amount does not care that the corporation '
   'owes $0.00.</p>\n'
   + tbl(('Charge', 'Calculated as', 'On a nil return'),
         [('Percentage late-filing charge', 'A percentage of tax owing',
           '$0.00, because the tax owing is $0.00'),
          ('Paper filing charge', 'A flat amount per return',
           '$1,000.00 in full')])
   + '\n<p>Read the right-hand column. The two charges behave in opposite ways on '
   'the same return.</p>', True),
  ('preparer', 'The Preparer Penalty',
   '<p>A separate charge of $100.00 per return applies to a preparer who files a '
   'corporate return on paper where electronic filing was required.</p>\n'
   '<p>It attaches to the person who prepared and filed the return, not to the '
   'corporation. A professional preparer filing on paper is exposed to it on every '
   'return.</p>\n'
   '<p>Returns here are transmitted electronically by a registered EFILE '
   'electronic filer, so neither charge arises.</p>'),
  ('nil-included', 'A Nil Return Is Not Exempt',
   '<p>Nothing about having no activity removes the electronic filing obligation '
   'or the charge for ignoring it. A dormant corporation that posts a paper T2 is '
   'exposed to the full $1,000.00 on a return reporting $0.00.</p>\n'
   '<div class="ei-warn"><p>This is the largest single amount a genuinely nil '
   'corporation can be charged, and the only one it can incur by being careful in '
   'the wrong way. Posting the return is not the safe option.</p></div>\n'
   '<p>See ' + a(A + 'can-i-file-a-nil-t2-myself-without-an-accountant/',
                 'whether a nil T2 can be filed without an accountant') + '.</p>',
   True),
  ('how', 'How an Electronic Return Reaches the Agency',
   '<p>The return is prepared in certified software, validated against the '
   'Agency\'s rules, and transmitted directly. There is no envelope, no posting '
   'date and no question about whether it arrived.</p>\n'
   + tbl(('Step', 'What happens'),
         [('Preparation', 'The return and its schedules are built'),
          ('Validation', 'The software checks it against the Agency\'s rules'),
          ('Authorisation', 'Form T183CORP is signed by a signing officer'),
          ('Transmission', 'The return is sent by a registered EFILE electronic '
           'filer'),
          ('Confirmation', 'The Agency returns a result on the transmission')])
   + '\n<p>The whole sequence for a nil return is covered in the guide to '
   + a(HUB + 'how-to-file-a-nil-t2-return/', 'how to file a nil T2 return')
   + '.</p>'),
  ('t183corp', 'Form T183CORP and Electronic Signing',
   '<p>Form T183CORP is what authorises the transmission. It carries the figures '
   'from the return it belongs to, and it is signed by an authorized signing '
   'officer of the corporation before anything is sent.</p>\n'
   '<p>It is signed here on a single-use access-controlled screen, with the date '
   'and the time recorded. It is never backdated, it is kept for six years, and it '
   'is not sent to the Agency unless the Agency asks for it.</p>\n'
   '<p>The full detail is in the guide to '
   + a(HUB + 't183corp-signing-and-transmission/',
       'Form T183CORP signing and transmission') + '.</p>', True),
  ('rejections', 'What Happens When a Transmission Is Rejected',
   '<p>A rejected transmission is not a filed return. The Agency returns an error '
   'identifying what it would not accept, the return is corrected, and it is sent '
   'again.</p>\n'
   + tbl(('Common rejection', 'Cause'),
         [('Year-end does not match the record',
           'A different year-end than the one on file'),
          ('Business number not recognised',
           'A wrong number, or no account for the return type'),
          ('A required schedule missing',
           'A schedule the return\'s own answers made mandatory'),
          ('Balances do not carry forward',
           'Opening figures that do not match the prior year\'s close')])
   + '\n<p>One corrected transmission is included in the fee where the Agency '
   'rejects the first one. The year-end mismatch is the most frequent of the four, '
   'and ' + a(A + 'how-do-i-fix-a-nil-t2-return-i-filed-with-the-wrong-year-end/',
              'fixing a wrong year-end') + ' covers it.</p>'),
  ('confirmation', 'The Confirmation You Receive',
   '<p>An accepted transmission produces a confirmation from the Agency. That is '
   'the evidence the year was filed, and it is what a clearance request, a '
   'dissolution and a lender all eventually ask for.</p>\n'
   '<p>It is emailed within 3 business days of transmission. Keep it with the '
   'corporate records: it is easier to retain than to retrieve years later.</p>\n'
   '<div class="ei-info"><p>A return nobody can evidence is, in practice, a return '
   'that gets filed twice. The confirmation takes no effort to keep and a great '
   'deal of effort to reconstruct years later.</p></div>', True),
  ('exceptions', 'The Narrow Exceptions',
   '<p>A small number of corporations fall outside mandatory electronic filing, '
   'defined by what the corporation is rather than by how little it did. An '
   'insurer, a non-resident corporation in certain circumstances and a corporation '
   'reporting in a functional currency are the kinds of case involved.</p>\n'
   '<p>Being dormant is not an exception, having no bank account is not an '
   'exception, and finding the software inconvenient is not an exception.</p>\n'
   '<p>' + NOT_NIL + '</p>'),
  ('older-years', 'Filing Older Years Electronically',
   '<p>Earlier tax years are transmitted electronically too. Catching up on six '
   'unfiled years does not mean posting six paper returns, and the Agency accepts '
   'prior-year returns through the same channel.</p>\n'
   '<p>Each year is its own return on its own form for its own tax year, prepared '
   'oldest first, at ' + PRICE + '.</p>\n'
   '<p>See the guide to ' + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
                              'catching up on unfiled corporate tax returns')
   + '.</p>', True),
 ],
 faq=[
  ('Is Electronic Filing of a T2 Compulsory?',
   'For tax years beginning after 2023 it is mandatory for virtually all '
   'corporations. The earlier threshold that exempted smaller corporations was '
   'removed.'),
  ('What Is the Charge for Filing a T2 on Paper?',
   'A flat $1,000.00, plus a separate $100.00 per-return charge on the preparer. '
   'Neither is a percentage of anything.'),
  ('Is a Nil Return Exempt From the Paper Filing Charge?',
   'No. It is a flat amount, so a dormant corporation that posts a paper return '
   'reporting $0.00 is exposed to the full $1,000.00.'),
  ('What if the Transmission Is Rejected?',
   'A rejected transmission is not a filed return. The Agency identifies the '
   'error, the return is corrected and sent again, and one corrected transmission '
   'is included in the fee.'),
  ('Can Older Unfiled Years Be Filed Electronically?',
   'Yes. Prior-year returns go through the same channel, prepared oldest first, '
   'each on its own form for its own tax year.'),
  ('What Proof Do I Get That the Year Was Filed?',
   'A confirmation from the Canada Revenue Agency, emailed within 3 business days '
   'of transmission. It is what a clearance request and a dissolution eventually '
   'ask for.'),
 ])

# ---------------------------------------------------------------------------
# Guide 26. /guides/schedule-50-and-shareholder-reporting/
# NOT an Appendix A topic. Added because the 10% threshold is stated in the
# fee table on every page of this site and explained on none of them, and
# because the Family 13 post
# /blog/schedule-50-and-the-10-percent-shareholder-rule/ is live with nothing
# to link up to. /guides/t2-schedules-on-a-nil-return/ gives Schedule 50 one
# row; this is the page that row should have pointed at.
# ---------------------------------------------------------------------------
G26 = dict(
 slug='schedule-50-and-shareholder-reporting',
 title='Schedule 50 and Shareholder Reporting | Nil T2 Guide',
 h1='The Complete Guide to Schedule 50 and Shareholder Reporting',
 h1_pre='The Complete Guide to ',
 h1_span='Schedule 50 and Shareholder Reporting',
 eyebrow='Schedule 50 Guide',
 meta=('What Schedule 50 reports, the 10% threshold, what goes in each row, '
       'and why a nil return still files it in full.'),
 convert=(SITE + '/t2-short-filing/', 'T2 Short Filing'),
 kids=['do-i-need-financial-statements-for-a-nil-t2-return',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'do-i-need-a-business-number-to-file-a-nil-t2',
       'can-i-file-a-nil-t2-myself-without-an-accountant',
       'how-do-i-know-if-my-corporation-counts-as-dormant',
       'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account'],
 sections=[
  ('what', 'What Schedule 50 Reports',
   '<p>Schedule 50 is the shareholder information schedule. It lists the people '
   'and entities holding a significant stake in the corporation, and it is filed '
   'with the T2.</p>\n'
   '<p>It reports ownership, not money. No income, no dividend and no valuation '
   'appears on it.</p>\n'
   '<div class="ei-info"><p>It is the schedule that tells the Agency who stands '
   'behind the corporation. That is why it survives on a return where every '
   'financial figure is $0.00.</p></div>', True),
  ('threshold', 'The 10% Threshold',
   '<p>A shareholder is reported where they hold 10% or more of any class of '
   'shares. Below 10% of every class, they are not reported.</p>\n'
   + tbl(('Holding', 'Reported on Schedule 50'),
         [('Sole shareholder, 100%', 'Yes'),
          ('Two shareholders at 50% each', 'Both'),
          ('Four shareholders at 25% each', 'All four'),
          ('A shareholder at 10% exactly', 'Yes, the threshold is inclusive'),
          ('A shareholder at 9%', 'No'),
          ('9% of common but 40% of preferred',
           'Yes, on the strength of the preferred class')])
   + '\n<p>The last two rows are the ones to read together. The test runs class by '
   'class, so a holding that is small in one class and large in another is '
   'reported.</p>'),
  ('details', 'What Goes in Each Row',
   '<p>Each reported shareholder takes a row carrying their identifying details '
   'and the holding itself.</p>\n'
   + tbl(('Field', 'For an individual', 'For a corporation'),
         [('Name', 'Full legal name', 'Full legal name'),
          ('Identifier', 'Social insurance number', 'Business number'),
          ('Share class held', 'The class', 'The class'),
          ('Percentage held', 'Of that class', 'Of that class')])
   + '\n<p>An identifier that does not match the Agency\'s record is a frequent '
   'cause of a rejected transmission, and it is worth checking before the return '
   'is sent rather than after.</p>', True),
  ('nil-years', 'Schedule 50 on a Nil Return',
   '<p>It is filed in full. A corporation with no activity still has shareholders, '
   'and who they are has not changed because the corporation did nothing.</p>\n'
   '<p>This is what people mean when they find a nil return is not an empty '
   'return. The income statement is zeroes, and Schedule 50 carries real names and '
   'real percentages.</p>\n'
   '<p>The other schedules a nil return carries are in the guide to '
   + a(HUB + 't2-schedules-on-a-nil-return/', 'T2 schedules on a nil return')
   + '.</p>'),
  ('corporate', 'Corporate and Trust Shareholders',
   '<p>A shareholder does not have to be a person. Where a corporation holds 10% '
   'or more, it is reported with its business number rather than a social '
   'insurance number.</p>\n'
   '<p>A holding structure is therefore visible on the schedule: the operating '
   'corporation reports its parent, and the parent reports its own '
   'shareholders.</p>\n'
   '<div class="ei-warn"><p>A holding corporation receiving a dividend from the '
   'corporation below it does not have a nil year. ' + NOT_NIL + '</p></div>\n'
   '<p>See the guide to ' + a(HUB + 'inactive-holding-company-filing/',
                              'inactive holding company filing') + '.</p>', True),
  ('changes', 'Shareholder Changes During the Year',
   '<p>The schedule reflects the holdings as the return reports them for the tax '
   'year. A transfer during the year is reflected in what the schedule shows, and '
   'the minute book is what evidences it.</p>\n'
   '<p>A transfer of shares is not by itself income to the corporation, so it does '
   'not take a quiet year out of nil. What a transfer changes is the schedule, not '
   'the income statement.</p>\n'
   '<p>Where shares were sold by a shareholder, that is the shareholder\'s personal '
   'matter rather than the corporation\'s.</p>'),
  ('common-errors', 'The Errors That Get Returns Rejected',
   '<p>Schedule 50 produces a disproportionate share of rejections, because it is '
   'the schedule carrying identifiers the Agency can check against its own '
   'records.</p>\n'
   + tbl(('Error', 'Result'),
         [('A social insurance number that does not match the name',
           'Rejected transmission'),
          ('A business number for a corporate shareholder that is wrong',
           'Rejected transmission'),
          ('Percentages for a class totalling more than 100',
           'Validation failure'),
          ('A 10% shareholder omitted', 'An incomplete return'),
          ('Reporting by overall ownership instead of class by class',
           'Shareholders wrongly included or left out')])
   + '\n<p>The last row is the conceptual error rather than a typing one, and it is '
   'the one that survives a careful proofread.</p>', True),
  ('related', 'Related and Associated Corporations',
   '<p>Schedule 50 is not the schedule that reports related or associated '
   'corporations. It reports shareholders. Relatedness and association are '
   'separate concepts with their own schedules and their own consequences.</p>\n'
   '<p>Association matters on a trading return because it affects how much of the '
   'small business deduction is available. On a nil return there is nothing to '
   'allocate, which is why the subject rarely arises here.</p>\n'
   '<p>A corporation in a group with trading members has figures to report and is '
   'handled by Gondaliya CPA Professional Corporation at gondaliyacpa.ca at '
   '$350.00 plus HST per year.</p>'),
  ('loans', 'Shareholder Loans Are Reported Elsewhere',
   '<p>A balance owed to or by a shareholder is a balance sheet item. It appears on '
   'Schedule 100 through the GIFI, not on Schedule 50.</p>\n'
   '<p>A shareholder loan does not by itself produce income or expense, so a '
   'dormant corporation carrying one on its balance sheet can still have a nil '
   'year.</p>\n'
   + tbl(('Item', 'Reported on'),
         [('Who the shareholders are', 'Schedule 50'),
          ('A balance owed to a shareholder', 'Schedule 100, the balance sheet'),
          ('Share capital issued', 'Schedule 100, the balance sheet'),
          ('A dividend paid to a shareholder',
           'The return, and it ends the nil year')])
   + '\n<p>See the guide to ' + a(HUB + 'gifi-schedules-100-125-141/',
                                  'GIFI Schedules 100, 125 and 141') + '.</p>',
   True),
  ('dividends', 'Dividends Take the Year Out of Nil',
   '<p>A dividend paid or received is activity. The corporation that pays one does '
   'not have a nil year, and neither does the corporation that receives one.</p>\n'
   '<p>Schedule 50 still reports the shareholders in such a year, but the return is '
   'no longer a nil return and is not the service this page describes.</p>\n'
   '<p>The handover is described at '
   + a(SITE + '/when-your-corporation-starts-operating/',
       'when your corporation starts operating') + '.</p>'),
  ('privacy', 'Who Can See Schedule 50',
   '<p>Schedule 50 is filed with the Agency and is subject to the confidentiality '
   'rules that cover a corporation\'s tax information. It is not a public register '
   'and it is not published.</p>\n'
   '<p>The public record of ownership, where one exists, is the registry\'s, not '
   'the Agency\'s, and the two hold different information.</p>\n'
   '<p>Returns here are prepared and transmitted in Canada by a registered EFILE '
   'electronic filer. Credentials are never shared and never used offshore.</p>',
   True),
 ],
 faq=[
  ('Who Has to Be Reported on Schedule 50?',
   'Any shareholder holding 10% or more of any class of shares. The threshold is '
   'inclusive, so a holding of exactly 10% is reported.'),
  ('Is the 10% Test on Overall Ownership or Per Class?',
   'Per class. A shareholder holding 9% of the common shares but 40% of the '
   'preferred shares is reported on the strength of the preferred class.'),
  ('Does a Nil Return Still File Schedule 50?',
   'Yes, in full. A corporation with no activity still has shareholders, and who '
   'they are has not changed because the corporation did nothing.'),
  ('What if the Shareholder Is Another Corporation?',
   'It is reported with its business number rather than a social insurance '
   'number. A holding structure is therefore visible across the two returns.'),
  ('Does a Shareholder Loan Go on Schedule 50?',
   'No. A balance owed to or by a shareholder is a balance sheet item reported on '
   'Schedule 100 through the GIFI. Schedule 50 reports who the shareholders are.'),
  ('Is Schedule 50 Public?',
   'No. It is filed with the Canada Revenue Agency and covered by the '
   'confidentiality rules for a corporation\'s tax information. A registry\'s '
   'public ownership record, where one exists, is separate and holds different '
   'information.'),
 ])

# ---------------------------------------------------------------------------
# Guide 27. /guides/non-resident-owned-corporation-nil-filing/
# NOT an Appendix A topic. Added because the $25.00 a day to $2,500.00 figure
# appears in the qualification block on every page of this site, which means
# the site states the single largest exposure a dormant corporation can carry
# and nowhere explains who it applies to. Family 4 already has live
# non-resident-owned pages in Ontario and British Columbia with no pillar
# above them.
#
# Nothing here advises on residence, treaties or foreign reporting. Each is
# named as a separate obligation with the route to it, because a guide that
# explained them would be giving advice this site does not offer.
# ---------------------------------------------------------------------------
G27 = dict(
 slug='non-resident-owned-corporation-nil-filing',
 title='Non-Resident-Owned Corporation Nil Filing | Canadian Guide',
 h1='The Complete Guide to Non-Resident-Owned Corporation Nil Filing',
 h1_pre='The Complete Guide to ',
 h1_span='Non-Resident-Owned Corporation Nil Filing',
 eyebrow='Non-Resident Guide',
 meta=('Why the daily charge is the largest exposure a dormant corporation '
       'carries, who it reaches, and how a nil year is filed from outside Canada.'),
 convert=(COST, 'Nil T2 Filing Cost'),
 kids=['what-happens-if-i-dont-file-a-nil-t2',
       'what-happens-if-i-dont-file-my-t2-for-five-years',
       'do-i-need-a-business-number-to-file-a-nil-t2',
       'can-i-file-five-years-of-nil-t2-returns-at-once',
       'can-i-file-a-nil-t2-late-without-a-penalty',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity'],
 sections=[
  ('who', 'Which Corporations This Covers',
   '<p>This guide is about a corporation incorporated in Canada whose shares are '
   'held by people or entities outside Canada. It is a Canadian corporation with '
   'non-resident owners.</p>\n'
   '<p>That is a different thing from a corporation incorporated abroad, and the '
   'distinction decides which rules apply.</p>\n'
   + tbl(('Corporation', 'What it is here'),
         [('Incorporated in Canada, Canadian owners', 'An ordinary resident '
           'corporation'),
          ('Incorporated in Canada, owners abroad',
           'Resident, and the subject of this guide'),
          ('Incorporated abroad, managed from Canada',
           'Residence is a question of fact and is not decided here'),
          ('Incorporated abroad, no Canadian presence',
           'Outside what this site files')])
   + '\n<p>Only the second row is straightforward, and it is the common case: a '
   'Canadian corporation set up by someone who has since left, or who never '
   'lived here.</p>', True),
  ('residence', 'Corporate Residence and Where It Is Decided',
   '<p>A corporation incorporated in Canada is a resident of Canada. Where a '
   'corporation was incorporated elsewhere, residence turns on where it is '
   'centrally managed and controlled, which is a question of fact.</p>\n'
   '<p>Residence is the corporation\'s own, not its shareholders\'. Owners living '
   'abroad do not make a Canadian corporation non-resident.</p>\n'
   '<div class="ei-info"><p>This site files for corporations incorporated in '
   'Canada. Where residence is genuinely in question, that is a determination for '
   'Gondaliya CPA Professional Corporation at gondaliyacpa.ca rather than a form '
   'on this one.</p></div>'),
  ('still-file', 'The Filing Obligation',
   '<p>A Canadian corporation with non-resident owners files a T2 for every tax '
   'year, six months after each year-end, until it is dissolved. Having no '
   'activity does not change that and neither does having no Canadian resident '
   'involved in it.</p>\n'
   '<p>The return is the same return. The owners\' location changes who signs and '
   'how, not what is filed.</p>\n'
   '<p>See ' + a(A + 'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity/',
                 'whether a corporation with no activity files') + '.</p>'),
  ('daily-penalty', 'The Penalty Built on Days, Not Tax Owing',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>The last clause of that block is this guide\'s subject. A '
   'non-resident-owned corporation that fails to file faces a charge of $25.00 per '
   'day, to a maximum of $2,500.00, and it is built on days rather than on tax '
   'owing.</p>\n'
   + tbl(('Days late', 'Charge at $25.00 a day'),
         [('10 days', '$250.00'),
          ('30 days', '$750.00'),
          ('60 days', '$1,500.00'),
          ('100 days', '$2,500.00, the maximum'),
          ('A year or more', '$2,500.00, the maximum')])
   + '\n<p>The maximum is reached in a little over three months. After that the '
   'charge stops growing while everything else about the open year continues.</p>',
   True),
  ('nil-exposure', 'Why a Nil Year Carries the Full Exposure',
   '<p>A percentage of $0.00 is $0.00. Twenty-five dollars a day for a hundred '
   'days is $2,500.00 whether the corporation earned millions or nothing at '
   'all.</p>\n'
   '<div class="ei-warn"><p>This is the one charge in this family of rules that '
   'reaches its maximum on a completely empty year. A dormant Canadian corporation '
   'owned from abroad is the single most exposed thing this site files for, and the '
   'exposure comes from the calendar rather than from anything it did.</p></div>\n'
   '<p>Filing the year is what stops the days counting. See '
   + a(A + 'can-i-file-a-nil-t2-late-without-a-penalty/',
       'filing a nil T2 late') + '.</p>'),
  ('t106-t1134', 'Other Returns That May Be Due',
   '<p>A corporation with non-resident connections can owe information returns '
   'beyond the T2. They are separate filings with their own deadlines and their own '
   'charges for lateness.</p>\n'
   + tbl(('Return', 'Concerns'),
         [('T106', 'Transactions with non-arm\'s length non-residents'),
          ('T1134', 'Interests in foreign affiliates'),
          ('T1135', 'Specified foreign property above the threshold'),
          ('NR4', 'Amounts paid or credited to non-residents')])
   + '\n<p>None of these is covered by the fee on this page and none is a nil T2. '
   'A corporation that may owe one is handled by Gondaliya CPA Professional '
   'Corporation at gondaliyacpa.ca at $350.00 plus HST per year.</p>\n'
   '<p>A genuinely dormant corporation with no transactions and no foreign holdings '
   'generally owes none of them, but that is a conclusion to reach deliberately '
   'rather than to assume.</p>'),
  ('treaty', 'Treaty-Based Returns',
   '<p>Where a tax treaty affects a corporation\'s Canadian tax position, the '
   'return may need to disclose the treaty relied on. That is a trading-return '
   'matter: a corporation with no income has no treaty position to take.</p>\n'
   '<p>A nil year reports $0.00 of income from every source, so there is nothing '
   'for a treaty to exempt or reduce.</p>\n'
   '<p>Where a treaty position is in play, the return is not nil and is not filed '
   'here.</p>', True),
  ('signing', 'Signing From Outside Canada',
   '<p>Form T183CORP is signed by an authorized signing officer of the '
   'corporation. The officer\'s location is irrelevant: a director abroad signs the '
   'same form in the same way.</p>\n'
   '<p>It is signed here on a single-use access-controlled screen, with the date '
   'and the time recorded on the server in Eastern Time. It is never backdated. '
   'Time zones do not change the recorded moment.</p>\n'
   '<p>The signing rules are in the guide to '
   + a(HUB + 't183corp-signing-and-transmission/',
       'Form T183CORP signing and transmission') + '.</p>'),
  ('bn', 'Getting a Business Number Without a Canadian Address',
   '<p>A business number is needed before a return can be transmitted. A '
   'corporation obtains one whether or not its directors live in Canada.</p>\n'
   '<p>The registered office address on the registry record is the corporation\'s '
   'own, and keeping it current matters more here than anywhere, because '
   'correspondence has further to travel and the directors are not nearby to '
   'collect it.</p>\n'
   '<p>See ' + a(A + 'do-i-need-a-business-number-to-file-a-nil-t2/',
                 'whether a business number is needed to file') + '.</p>', True),
  ('catch-up', 'Catching Up Several Non-Resident Years',
   '<p>Each outstanding year is its own return for its own tax year, prepared '
   'oldest first. Six unfiled years are six returns, each at ' + PRICE + '.</p>\n'
   '<p>The daily charge is per return rather than per corporation, which is why '
   'several open years are worth dealing with together rather than one at a '
   'time.</p>\n'
   '<p>See ' + a(A + 'can-i-file-five-years-of-nil-t2-returns-at-once/',
                 'filing five years at once') + ' and the guide to '
   + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
       'catching up on unfiled corporate tax returns') + '.</p>'),
  ('dissolution', 'Dissolving a Non-Resident-Owned Corporation',
   '<p>The sequence is the same as for any other corporation: every outstanding '
   'year filed, a clearance certificate, articles of dissolution, then the final '
   'T2 running to the dissolution date.</p>\n'
   '<p>Non-resident ownership gives it more urgency rather than a different shape. '
   'Each year the corporation is left standing is another year able to attract the '
   'daily charge.</p>\n'
   '<p>' + NOT_NIL + '</p>\n'
   '<p>See the guide to ' + a(HUB + 'winding-up-an-inactive-corporation/',
                              'winding up an inactive corporation') + '.</p>',
   True),
 ],
 faq=[
  ('Does a Canadian Corporation With Owners Abroad Still File a T2?',
   'Yes, for every tax year, six months after each year-end, until it is formally '
   'dissolved. Owners living abroad do not change the obligation.'),
  ('What Is the $25.00 a Day Charge?',
   'A non-resident-owned corporation that fails to file faces $25.00 per day to a '
   'maximum of $2,500.00. It is built on days rather than on tax owing, so the '
   'maximum is reached in a little over three months.'),
  ('Does It Apply to a Year With No Activity?',
   'Yes, in full. It is calculated on days, so an entirely empty year reaches the '
   'same $2,500.00 maximum a trading year would.'),
  ('Does Owning a Canadian Corporation From Abroad Make It Non-Resident?',
   'No. A corporation incorporated in Canada is a resident of Canada. Residence is '
   'the corporation\'s own, not its shareholders\'.'),
  ('Can Form T183CORP Be Signed From Outside Canada?',
   'Yes. An authorized signing officer signs it wherever they are, on a '
   'single-use access-controlled screen, with the date and time recorded on the '
   'server in Eastern Time.'),
  ('Are the T106, T1134 and T1135 Covered by the Fee?',
   'No. Those are separate information returns with their own deadlines, and a '
   'corporation that may owe one is handled by Gondaliya CPA Professional '
   'Corporation at gondaliyacpa.ca at $350.00 plus HST per year.'),
 ])

GUIDES = [G18, G19, G20, G21, G22, G23, G24, G25, G26, G27]

# ---------------------------------------------------------------------------
# Render. Identical to the pillar and batches 2, 3 and 4.
# ---------------------------------------------------------------------------
KID_TITLES = {}
for r in json.load(open(os.path.join(HERE, '..', 'f5', 'f5-manifest.json'),
                        encoding='utf-8')):
    KID_TITLES[r['slug']] = r['meta']['cnf_question_text']

# ---------------------------------------------------------------------------
# Guards. Each of these fired at least once while this batch was written, or
# guards a mistake an earlier batch actually made.
# ---------------------------------------------------------------------------
assert len(GUIDES) == 10, '%d guides in batch 5' % len(GUIDES)

_batch_slugs = [g['slug'] for g in GUIDES]
assert len(set(_batch_slugs)) == 10, 'duplicate slug within the batch'

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

json.dump(records, open(os.path.join(HERE, 'f9-batch5-manifest.json'), 'w'),
          ensure_ascii=False, indent=1)

# The 6(g) outbound cap of 40 is the reason the sibling window exists. Report
# it per guide rather than waiting for the gate, so a breach is visible here.
for r in records:
    out = len(set(_re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"',
                              r['content'])))
    print('%-44s %6d bytes  %2d sections  out:%2d'
          % (r['slug'], len(r['content'].encode()), len(r['toc']), out))
    assert out <= 40, '%s carries %d outbound links, over the 40 cap' % (r['slug'], out)
