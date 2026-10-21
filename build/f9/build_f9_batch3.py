"""Family 9 batch 3: guides 8 to 12 of 30.

Guides 8, 9 and 10 are the last three topics in the 6(d) Family 9 keyword list
(line 1246), which completes the batch of 10 that gate row 1217 scheduled for
October 9, 2026. Guides 11 and 12 start the batch of 20 due October 30.

The 19th plan conflict stands: Appendix A's 30 Family 9 slugs are root-level and
ten carry a year token, both forbidden by 6(a) line 1147 and the 6(k) year-stamp
rule. But Appendix A's *topics* are not what either rule forbids, only its URL
shapes. So guides 11 and 12 take two Appendix A topics and give them compliant
slugs:

  /first-year-t2-filing-guide/        -> /guides/first-year-t2-filing/
  /numbered-company-tax-filing-guide/ -> /guides/numbered-company-tax-filing/

Chosen as the two Appendix A topics with the least overlap against the seven
6(b) pillars and real cluster support already live. Pending sign-off.

A second reason Appendix A's F9 list cannot be used verbatim, found while
picking these two: it duplicates itself and the 6(b) pillars heavily. Three
entries are a general nil T2 guide and four more restate pillars already live.
Building it as written would have produced near-duplicates competing with each
other. Logged.

Linking. Every guide lists all eleven others, so each of the twelve carries
eleven sibling inbound links plus the hub: the first time Family 9 meets the
6(g) line 1528 minimum of 12 inbound.

Rebuild note. This file was lost when the container was re-provisioned onto a
different branch history before batch 3 was committed. Rebuilt from the same
inputs and verified byte-for-byte against guides 8, 9 and 10 as already
published (23902, 21557 and 22390 bytes).
"""
import json, os, re

HERE  = os.path.dirname(os.path.abspath(__file__))
SITE  = 'https://corpnilfilingfor300.ca'
FORM  = SITE + '/form/'
HUB   = SITE + '/guides/'
A     = SITE + '/answers/'
COST  = SITE + '/pricing/nil-t2-filing-cost/'
TODAY, ISO = 'October 21, 2026', '2026-10-21'
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

from f9_registry import REGISTRY, sibling_links
assert len(REGISTRY) == 12

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
# Guide 8. /guides/how-to-file-a-nil-t2-return/
# 6(d) line 1246 keyword: "how to file a nil t2 return".
# Written as prose rather than marked-up steps. Hard rule 6 bans HowTo schema,
# so the sequence is in the contents block and the headings, not in markup.
# ---------------------------------------------------------------------------
G8 = dict(
 slug='how-to-file-a-nil-t2-return',
 title='How to File a Nil T2 Return | Step by Step for Canada',
 h1='How to File a Nil T2 Return',
 h1_pre='How to File a ',
 h1_span='Nil T2 Return',
 eyebrow='Filing Guide',
 meta=('What you need before you start, how the fiscal year-end is confirmed, which '
       'schedules are filed, how Form T183CORP is signed, and how the return is sent.'),
 convert=(COST, 'See the Full Cost'),
 kids=['can-i-file-a-nil-t2-myself-without-an-accountant',
       'do-i-need-a-business-number-to-file-a-nil-t2',
       'do-i-need-financial-statements-for-a-nil-t2-return',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'can-i-file-five-years-of-nil-t2-returns-at-once',
       'do-i-need-to-file-a-nil-t2-if-i-never-started-operating'],
 sections=[
  ('what-you-need', 'What You Need Before You Start',
   tbl(('Item', 'Why it is needed'),
       [('The exact legal corporation name', 'It must match the registry record'),
        ('The nine-digit business number',
         'The return is filed against it and its RC account'),
        ('The fiscal year-end on record with the Canada Revenue Agency',
         'A mismatch rejects the transmission'),
        ('Which tax years are outstanding', 'Each year is a separate return'),
        ('Any balances on the books',
         'Share capital, cash or a shareholder loan make GIFI schedules required'),
        ('A signing officer available to sign',
         'Form T183CORP is signed before transmission')])
   + '\n<p>Nothing else is needed for a true nil year. There are no receipts to '
   'gather and no statements to prepare, because there was no activity to '
   'report.</p>', True),
  ('year-end', 'Confirming the Fiscal Year-End',
   '<p>This is the first step and the one that most often goes wrong. The Canada '
   'Revenue Agency already holds a fiscal year-end for the corporation, taken from '
   'the incorporation record, and the return must carry that same date.</p>\n'
   '<div class="ei-warn"><p>Owners usually remember the date the business started '
   'trading rather than the date on the incorporation record. A year-end that '
   'differs from the one the Agency holds rejects the transmission.</p></div>'),
  ('business-number', 'The Business Number and RC Account',
   '<p>The return is filed against the nine-digit business number and its RC '
   'corporation income tax account. Most corporations receive the number at '
   'incorporation.</p>\n'
   '<p>A corporation that was never registered with the Canada Revenue Agency has '
   'to obtain one before anything can be transmitted. See '
   + a(A + 'do-i-need-a-business-number-to-file-a-nil-t2/',
       'whether a business number is needed to file a nil T2') + '.</p>', True),
  ('nil-test', 'Checking the Year Is Actually Nil',
   '<p>' + NOT_NIL + '</p>\n'
   + tbl(('Was there any of this in the year', 'Still nil'),
         [('Revenue of any amount', 'No'),
          ('An expense claimed', 'No'),
          ('Payroll', 'No'),
          ('An asset purchase', 'No'),
          ('An inter-company transaction', 'No'),
          ('Investment or rental income', 'No'),
          ('A dividend paid or received', 'No'),
          ('None of the above', 'Yes')])),
  ('form-choice', 'T2 Short or the Full T2',
   '<p>The T2 Short is a two-page version of the return, available to a '
   'Canadian-controlled private corporation that meets eight conditions. Most nil '
   'years qualify.</p>\n'
   '<div class="ei-info"><p>Either form is included in the fee. The choice is made '
   'from the facts of the year rather than by the corporation, and it changes '
   'nothing about the deadline.</p></div>\n'
   '<p>The conditions are set out in the guide to '
   + a(HUB + 't2-short-eligibility/', 'T2 Short eligibility') + '.</p>', True),
  ('gifi', 'The GIFI Schedules',
   '<p>A corporation inactive all year with nothing at all to report may omit GIFI '
   'Schedules 100, 125 and 141. Any share capital, cash, shareholder loan, '
   'incorporation cost or bank charge makes them required.</p>\n'
   '<p>This is where a return that looks nil is most often filed incorrectly. The '
   'detail is in the guide to '
   + a(HUB + 'gifi-schedules-100-125-141/', 'GIFI Schedules 100, 125 and 141')
   + '.</p>'),
  ('schedules', 'Schedules 24, 50 and 8',
   tbl(('Schedule', 'When it is required'),
       [('Schedule 24', 'On the first return after incorporation'),
        ('Schedule 50', 'For every shareholder holding 10% or more'),
        ('Schedule 8', 'Capital cost allowance, recorded with loss continuity')])
   + '\n<p>Schedule 8 and the loss continuity that travels with it are covered in '
   'the guide to '
   + a(HUB + 'schedule-8-and-loss-continuity/', 'Schedule 8 and loss continuity')
   + '.</p>', True),
  ('review', 'CPA Review Before Transmission',
   '<p>A CPA Ontario member reviews the completed return before it is transmitted: '
   'the year-end against the Agency record, the GIFI coding, the schedule selection '
   'and the nil status itself.</p>\n'
   '<p>That review is what the fee buys. A corporation filing on its own with '
   'commercial tax software takes on the same checks. See '
   + a(A + 'can-i-file-a-nil-t2-myself-without-an-accountant/',
       'whether a nil T2 can be filed without an accountant') + '.</p>'),
  ('t183corp', 'Signing Form T183CORP',
   '<p>An authorized signing officer signs Form T183CORP before the return is '
   'transmitted, never after. It carries a date and an HH:MM:SS timestamp that is '
   'never backdated, and may be e-signed through an access-controlled secure '
   'portal.</p>\n'
   '<div class="ei-info"><p>One form is signed per tax year, because each year is a '
   'separate return with its own transmission. The form is kept by the firm for six '
   'years and is not sent to the Agency unless requested.</p></div>\n'
   '<p>The full detail is in the guide to '
   + a(HUB + 't183corp-signing-and-transmission/',
       'Form T183CORP signing and transmission') + '.</p>', True),
  ('transmit', 'Transmission and CRA Confirmation',
   '<p>' + EFILE_PILLAR + '</p>\n'
   '<p>For tax years starting after 2023, e-filing is mandatory for virtually all '
   'corporations, and a paper T2 draws a $1,000.00 penalty plus a $100.00 '
   'per-return preparer penalty. Your CRA confirmation is emailed within 3 business '
   'days. One corrected transmission is included where the Agency rejects the '
   'first.</p>\n'
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>'),
  ('multi-year', 'Filing More Than One Year',
   '<p>Each outstanding year is its own return, with its own fiscal year-end, its '
   'own figures and its own T183CORP signature. They are filed oldest first, so the '
   'balances carry forward correctly.</p>\n'
   + tbl(('Tax years outstanding', 'Fee at ' + PRICE),
         [('1 year', '$300.00 plus HST'), ('3 years', '$900.00 plus HST'),
          ('5 years', '$1,500.00 plus HST'), ('10 years', '$3,000.00 plus HST')])
   + '\n<p>The sequence for a catch-up is set out in the guide to '
   + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
       'catching up on unfiled corporate tax returns') + '.</p>', True),
 ],
 faq=[
  ('How Long Does Filing a Nil T2 Take?',
   'The return itself is short, and the usual wait is for the fiscal year-end to be '
   'confirmed and for the signing officer to sign Form T183CORP. The CRA '
   'confirmation is emailed within 3 business days of transmission.'),
  ('What Do I Have to Send You?',
   'The legal corporation name, the business number, the fiscal year-end, which '
   'years are outstanding, and any balances sitting on the books. For a true nil '
   'year there are no receipts and no statements to prepare.'),
  ('Can I File Without Knowing My Fiscal Year-End?',
   'No. The year-end must match the record the Canada Revenue Agency holds or the '
   'transmission is rejected, so it is confirmed before the return is prepared '
   'rather than guessed.'),
  ('Do I Have to Sign Anything?',
   'Yes. An authorized signing officer signs Form T183CORP before the return is '
   'transmitted, one for each tax year being filed. It can be e-signed through a '
   'secure portal with a single-use link.'),
  ('What if the CRA Rejects the Return?',
   'One corrected transmission is included in the fee. A rejection is usually a '
   'year-end that does not match the Agency record, and it is a filing that has not '
   'landed yet rather than a failed one.'),
  ('Is a Paper T2 Still an Option?',
   'Not in practice. For tax years starting after 2023, e-filing is mandatory for '
   'virtually all corporations, and a paper T2 draws a $1,000.00 penalty plus a '
   '$100.00 per-return preparer penalty.'),
 ])

# ---------------------------------------------------------------------------
# Guide 9. /guides/gifi-schedules-100-125-141/
# 6(d) line 1246 keyword: "gifi schedules 100 125 141 guide".
# ---------------------------------------------------------------------------
G9 = dict(
 slug='gifi-schedules-100-125-141',
 title='GIFI Schedules 100, 125 and 141 | Nil T2 Guide',
 h1='The Complete Guide to GIFI Schedules 100, 125 and 141',
 h1_pre='The Complete Guide to ',
 h1_span='GIFI Schedules 100, 125 and 141',
 eyebrow='GIFI Guide',
 meta=('What GIFI is, what Schedules 100, 125 and 141 report, when a nil return may '
       'omit them, and why share capital or a shareholder loan makes them required.'),
 convert=(COST, 'See the Full Cost'),
 kids=['do-i-need-financial-statements-for-a-nil-t2-return',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'can-i-file-a-nil-t2-myself-without-an-accountant',
       'do-i-need-a-business-number-to-file-a-nil-t2'],
 sections=[
  ('what-is-gifi', 'What GIFI Is',
   '<p>GIFI stands for the General Index of Financial Information. It is the '
   'standard code set the Canada Revenue Agency uses for the balance sheet and the '
   'income statement inside the T2.</p>\n'
   '<p>It exists so that every corporation reports the same item under the same '
   'code, whatever its own bookkeeping calls it. A corporation does not file its '
   'accountant&rsquo;s statements; it files the figures mapped onto GIFI codes.</p>',
   True),
  ('three-schedules', 'Schedules 100, 125 and 141',
   tbl(('Schedule', 'What it reports'),
       [('Schedule 100', 'The balance sheet: assets, liabilities and equity'),
        ('Schedule 125', 'The income statement: revenue and expenses'),
        ('Schedule 141',
         'A checklist about who prepared the figures and whether a review or '
         'audit was done')])
   + '\n<p>The three travel together. A return that files one generally files all '
   'three.</p>'),
  ('s100', 'Schedule 100, the Balance Sheet',
   '<p>Schedule 100 reports what the corporation owns and owes at the fiscal '
   'year-end. On a dormant corporation this is often a single line of share capital '
   'and a matching line of cash or a shareholder loan.</p>\n'
   '<div class="ei-info"><p>A balance sheet does not become nil because the year '
   'was nil. Balances sit on the books until something removes them, and they are '
   'reported every year they exist.</p></div>', True),
  ('s125', 'Schedule 125, the Income Statement',
   '<p>Schedule 125 reports revenue and expenses for the year. On a true nil year '
   'this is where the nil actually appears: no revenue, no expenses, nil net '
   'income.</p>\n'
   '<p>A single bank charge is an expense, and a corporation that paid one has '
   'something to report on Schedule 125 even though it traded not at all.</p>'),
  ('s141', 'Schedule 141, the Notes Checklist',
   '<p>Schedule 141 is a short set of questions about the financial information '
   'itself: who prepared it, whether an accountant was involved, and whether the '
   'statements were audited, reviewed or neither.</p>\n'
   '<div class="ei-info"><p>For a nil return the answer is normally that no audit '
   'and no review was performed, which is accurate and expected. It is a disclosure '
   'rather than a judgement.</p></div>', True),
  ('when-omitted', 'When a Nil Return May Omit Them',
   '<p>A corporation that was inactive all year and has nothing at all to report '
   'may omit GIFI Schedules 100, 125 and 141. Nothing at all means no assets, no '
   'liabilities, no equity balance, no revenue and no expenses.</p>\n'
   '<p>That is a narrower case than most owners assume. A corporation with $100.00 '
   'of share capital does not meet it.</p>'),
  ('when-required', 'What Makes Them Required',
   tbl(('On the books at the year-end', 'GIFI schedules required'),
       [('Share capital of any amount', 'Yes'),
        ('Cash in a corporate bank account', 'Yes'),
        ('A shareholder loan in either direction', 'Yes'),
        ('Incorporation costs capitalised', 'Yes'),
        ('A bank charge paid during the year', 'Yes'),
        ('Nothing at all', 'No')]), True),
  ('share-capital', 'Share Capital and Shareholder Loans',
   '<p>These two are the usual reason a dormant corporation still files GIFI. Share '
   'capital was issued when the corporation was set up and has sat on the balance '
   'sheet ever since. A shareholder loan is whatever the owner put in or took '
   'out.</p>\n'
   '<div class="ei-warn"><p>Neither is income and neither creates tax. They are '
   'balances, and a balance is reported because it exists, not because anything '
   'happened to it during the year.</p></div>'),
  ('common-error', 'The Most Common Nil-Return Error',
   '<p>Omitting the GIFI schedules on a corporation that has balances is the single '
   'most common reason a return that looks nil is not filed correctly.</p>\n'
   '<p>The return goes in, the year looks closed, and the omission surfaces later '
   'as a query or a reassessment. Filing the schedules with nil amounts where they '
   'are required is what makes the year a filed nil year rather than an incomplete '
   'one.</p>', True),
  ('no-statements', 'No Audited Statements Are Needed',
   '<p>GIFI is not the same thing as financial statements. No audited or reviewed '
   'statements are needed for a nil T2, and none are prepared as part of this '
   'service.</p>\n'
   '<p>What is filed is the GIFI schedules inside the return. See '
   + a(A + 'do-i-need-financial-statements-for-a-nil-t2-return/',
       'whether financial statements are needed for a nil T2 return') + '.</p>'),
  ('codes', 'How the Codes Work',
   '<p>Each line of the balance sheet and income statement carries a GIFI code: a '
   'four-digit number that tells the Canada Revenue Agency what the figure is. Cash '
   'has its own code, share capital has its own code, bank charges have their '
   'own.</p>\n'
   '<div class="ei-info"><p>Mapping a corporation&rsquo;s own account names onto '
   'the right codes is the work in a nil GIFI filing, and it is what the CPA review '
   'checks before transmission.</p></div>', True),
 ],
 faq=[
  ('Does a Nil Return Always Need GIFI Schedules?',
   'No, but the exemption is narrow. A corporation inactive all year with nothing '
   'at all to report may omit Schedules 100, 125 and 141. Any share capital, cash, '
   'shareholder loan, incorporation cost or bank charge makes them required.'),
  ('Is GIFI the Same as Financial Statements?',
   'No. GIFI is a code set used inside the T2 for the balance sheet and income '
   'statement. No audited or reviewed financial statements are needed for a nil '
   'return.'),
  ('My Corporation Only Has Share Capital. Do I File GIFI?',
   'Yes. Share capital of any amount is a balance on the books, and a balance is '
   'reported in every year it exists. This is the case owners most often get '
   'wrong.'),
  ('What Does Schedule 141 Actually Ask?',
   'Who prepared the financial information, whether an accountant was involved, and '
   'whether the statements were audited, reviewed or neither. For a nil return the '
   'answer is normally neither, which is accurate and expected.'),
  ('Does Filing GIFI With Zeros Create Tax?',
   'No. GIFI reports figures; it does not calculate tax. A true nil year reports '
   'nil net income and the corporation owes $0.00.'),
  ('Are the GIFI Schedules Included in the Fee?',
   'Yes, where they are required. The fee is ' + PRICE + ' and covers Schedules '
   '100, 125 and 141 along with the return itself.'),
 ])

# ---------------------------------------------------------------------------
# Guide 10. /guides/schedule-8-and-loss-continuity/
# 6(d) line 1246 keyword: "schedule 8 and loss continuity guide".
#
# Accuracy note. The plan pairs the two throughout ("Schedule 8 and loss
# continuity | Recorded" in the 6(c) fee table), but they are two schedules:
# Schedule 8 is capital cost allowance, and Schedule 4 is Corporation Loss
# Continuity and Application. Named correctly on the page. The page itself
# never refers to the plan; that reference was caught by the gate and removed.
# ---------------------------------------------------------------------------
G10 = dict(
 slug='schedule-8-and-loss-continuity',
 title='Schedule 8 and Loss Continuity | Nil T2 Guide',
 h1='The Complete Guide to Schedule 8 and Loss Continuity',
 h1_pre='The Complete Guide to ',
 h1_span='Schedule 8 and Loss Continuity',
 eyebrow='Schedules Guide',
 meta=('What Schedule 8 records, how capital cost allowance works in a nil year, why '
       'loss continuity has to be carried forward, and what a skipped year costs.'),
 convert=(COST, 'See the Full Cost'),
 kids=['do-i-need-financial-statements-for-a-nil-t2-return',
       'what-happens-if-i-dont-file-my-t2-for-five-years',
       'can-i-file-five-years-of-nil-t2-returns-at-once',
       'can-i-dissolve-my-corporation-with-unfiled-t2-returns',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'what-happens-if-i-dont-file-a-t2-before-dissolving-my-corporation'],
 sections=[
  ('what-s8', 'What Schedule 8 Is',
   '<p>Schedule 8 is the capital cost allowance schedule. It records the '
   'corporation&rsquo;s depreciable property, the class each asset sits in, and how '
   'much depreciation is claimed for the year.</p>\n'
   '<p>A corporation with no depreciable property has no Schedule 8 to file. One '
   'that still holds equipment, a vehicle or a computer from its trading days does, '
   'even in a year when nothing happened.</p>', True),
  ('cca', 'Capital Cost Allowance in a Nil Year',
   '<p>Capital cost allowance is the tax version of depreciation. Each class of '
   'asset has a rate, and the undepreciated capital cost of the class is what '
   'remains to be claimed in future years.</p>\n'
   '<div class="ei-info"><p>Capital cost allowance is discretionary. A corporation '
   'may claim anything from nil up to the maximum the class allows, and the choice '
   'is made each year.</p></div>'),
  ('claim-or-not', 'Claiming It or Leaving It',
   '<p>On a nil year the usual answer is to claim nil. Claiming capital cost '
   'allowance against no income creates a non-capital loss, and a non-capital loss '
   'expires. Leaving the claim unmade keeps the undepreciated capital cost in the '
   'pool, where it does not expire at all.</p>\n'
   + tbl(('Choice in a nil year', 'What happens'),
         [('Claim nil capital cost allowance',
           'The undepreciated capital cost stays in the pool for a future year'),
          ('Claim the maximum',
           'A non-capital loss is created, which expires 20 years later')]), True),
  ('pools', 'The Pools Carry Forward',
   '<p>Each class is a pool rather than a list of individual assets. The pool '
   'carries forward from year to year, reduced by what is claimed and by anything '
   'sold, and increased by anything bought.</p>\n'
   '<p>That carry-forward is why the years are filed in order. A pool balance on one '
   'return is the opening balance on the next.</p>'),
  ('loss-continuity', 'What Loss Continuity Is',
   '<p>Loss continuity is the running record of the losses a corporation has and has '
   'not yet used. It is reported on Schedule 4, Corporation Loss Continuity and '
   'Application, not on Schedule 8.</p>\n'
   '<div class="ei-info"><p>The two are filed together and are often spoken of as '
   'one, but they are separate schedules. Schedule 8 is the asset pools; '
   'Schedule 4 is the losses.</p></div>', True),
  ('carryforward', 'How Long Losses Carry Forward',
   tbl(('Type of loss', 'Carry back', 'Carry forward'),
       [('Non-capital loss', '3 years', '20 years'),
        ('Net capital loss', '3 years', 'Indefinitely'),
        ('Undepreciated capital cost in a pool', 'Not applicable',
         'Indefinitely, while the pool exists')])
   + '\n<p>A non-capital loss is the ordinary kind, from expenses exceeding revenue. '
   'A net capital loss comes from selling capital property for less than it '
   'cost.</p>'),
  ('skipped-year', 'What a Skipped Year Does to the Continuity',
   '<p>A year that was never filed is a gap in the record. The losses and pools from '
   'the year before it have no filed return carrying them into the year after, so '
   'the continuity has to be rebuilt before the later years can be assessed '
   'correctly.</p>\n'
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>On a true nil year the figures themselves are simple, which is what makes '
   'rebuilding the continuity straightforward rather than forensic.</p>', True),
  ('s4-and-s8', 'Schedule 4 and Schedule 8 Together',
   tbl(('Schedule', 'Name', 'What it carries forward'),
       [('Schedule 8', 'Capital Cost Allowance',
         'Undepreciated capital cost, by class'),
        ('Schedule 4', 'Corporation Loss Continuity and Application',
         'Non-capital and net capital losses')])
   + '\n<p>Both are included in the fee of ' + PRICE + ' where the corporation has '
   'anything to record on them.</p>'),
  ('nil-vs-loss', 'A Nil Year Is Not a Loss Year',
   '<p>These two are often confused. A nil year had no activity at all, so net '
   'income is nil and no loss arises. A loss year had real expenses exceeding real '
   'revenue, which creates a non-capital loss to carry forward.</p>\n'
   '<div class="ei-warn"><p>A corporation that claims expenses is not nil, and this '
   'service is for a corporation with no activity in the tax year. ' + NOT_NIL
   + '</p></div>', True),
  ('catch-up', 'Rebuilding Continuity on a Catch-Up',
   '<p>Where several years are outstanding, the pools and losses are carried through '
   'each return in turn. The earliest outstanding year is prepared first, its '
   'closing balances become the next year&rsquo;s opening balances, and so on to the '
   'present.</p>\n'
   '<p>The full sequence is in the guide to '
   + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
       'catching up on unfiled corporate tax returns') + '.</p>'),
  ('order', 'Why the Years Are Filed Oldest First',
   '<p>Because continuity only runs forwards. A return filed out of order has '
   'opening balances that do not match the closing balances of the year before it, '
   'and that mismatch is what draws a query rather than a clean assessment.</p>\n'
   '<p>It is the single practical reason the order matters on a multi-year '
   'filing.</p>', True),
 ],
 faq=[
  ('Does a Nil Return Need Schedule 8?',
   'Only where the corporation holds depreciable property. A corporation with no '
   'assets of that kind has no Schedule 8 to file.'),
  ('Should I Claim Capital Cost Allowance in a Nil Year?',
   'Usually nil. Claiming against no income creates a non-capital loss that expires '
   'in 20 years, while claiming nothing keeps the undepreciated capital cost in the '
   'pool, where it does not expire.'),
  ('Is Loss Continuity on Schedule 8?',
   'No. Schedule 8 is capital cost allowance. Loss continuity is reported on '
   'Schedule 4, Corporation Loss Continuity and Application. The two are filed '
   'together, which is why they are often spoken of as one.'),
  ('How Long Can a Non-Capital Loss Be Carried Forward?',
   'Twenty years forward and three years back. A net capital loss carries forward '
   'indefinitely and back three years.'),
  ('Does a Nil Year Create a Loss I Can Use Later?',
   'No. A nil year had no activity, so net income is nil and no loss arises. A loss '
   'needs real expenses exceeding real revenue, and a corporation claiming expenses '
   'is not a nil filer.'),
  ('What if an Unfiled Year Breaks the Continuity?',
   'The gap is rebuilt by filing the missing years oldest first, so each '
   'return&rsquo;s closing balances become the next one&rsquo;s opening balances. On '
   'nil years the figures are simple enough that this is routine.'),
 ])

# ---------------------------------------------------------------------------
# Guide 11. /guides/first-year-t2-filing/
# Appendix A topic /first-year-t2-filing-guide/, slug corrected to the
# /guides/ base per 6(a) line 1147. Cluster support: F10 (25 first-filing URLs
# planned), and the F5 answers on never having operated and on the business
# number. Pending sign-off.
# ---------------------------------------------------------------------------
G11 = dict(
 slug='first-year-t2-filing',
 title='First-Year T2 Filing | Guide for New Canadian Corporations',
 h1='The Complete Guide to First-Year T2 Filing',
 h1_pre='The Complete Guide to ',
 h1_span='First-Year T2 Filing',
 eyebrow='First Year Guide',
 meta=('When the first tax year starts and ends, the 53-week rule, Schedule 24, '
       'choosing a year-end, and why first transmissions are the ones rejected.'),
 convert=(SITE + '/nil-t2-filing/', 'Nil T2 Filing Services'),
 kids=['do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
       'do-i-need-a-business-number-to-file-a-nil-t2',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'can-i-file-a-nil-t2-myself-without-an-accountant'],
 sections=[
  ('when-starts', 'When the First Tax Year Starts',
   '<p>On the incorporation date. Not on the day the first invoice goes out, not on '
   'the day the bank account opens, and not on the first of the following '
   'month.</p>\n'
   '<div class="ei-warn"><p>This is the single most misunderstood point about a '
   'first return. A corporation registered in March and never traded still has a '
   'tax year that began in March, and a return due for it.</p></div>', True),
  ('53-weeks', 'The 53-Week Rule',
   '<p>A corporation&rsquo;s first tax year cannot exceed 53 weeks. That is the only '
   'hard limit on where the first year-end falls.</p>\n'
   '<p>Within that window the date is the corporation&rsquo;s own choice, which is '
   'why two corporations incorporated on the same day can have different year-ends '
   'and different due dates.</p>'),
  ('choosing', 'Choosing the First Year-End',
   tbl(('Consideration', 'Effect'),
       [('Any date within 53 weeks of incorporation', 'Permitted'),
        ('A month-end rather than a mid-month date',
         'Simpler to administer, no tax effect'),
        ('A short first year', 'Brings the first filing deadline forward'),
        ('A full 53-week first year', 'Pushes the first filing deadline out'),
        ('Changing it later', 'Needs the Agency&rsquo;s permission')])
   + '\n<p>Once the first return is filed, the year-end is set and later years run '
   'twelve months from it.</p>', True),
  ('cra-record', 'The Year-End the CRA Already Holds',
   '<p>The Canada Revenue Agency takes a year-end from the incorporation record and '
   'holds it before the corporation has filed anything. The first return has to '
   'carry that same date.</p>\n'
   '<div class="ei-info"><p>Where the owner intended a different year-end than the '
   'one on record, that is settled with the Agency before the return is '
   'transmitted, not by filing a different date and hoping.</p></div>'),
  ('s24', 'Schedule 24, Required on a First Return',
   '<p>Schedule 24 is the first-time filer schedule, required on the first return '
   'after incorporation. It reports the corporation&rsquo;s shareholders, its '
   'related corporations and how it came into existence.</p>\n'
   '<p>It is filed once and not again. It is included in the fee of ' + PRICE
   + '.</p>', True),
  ('never-traded', 'A First Year With No Trading',
   '<p>A corporation registered and then left unused has a nil first year, and a nil '
   'return is filed for it. Filing nothing is not an option the rules offer, and '
   '"we never started" is not a filing status.</p>\n'
   '<p>' + NOT_NIL + '</p>\n'
   '<p>See '
   + a(A + 'do-i-need-to-file-a-nil-t2-if-i-never-started-operating/',
       'whether a nil T2 is needed if the corporation never started operating')
   + '.</p>'),
  ('rejected', 'Why First Transmissions Get Rejected',
   '<p>Because the year-end on the return does not match the one the Agency holds. '
   'It is the most common cause of a rejected first transmission, ahead of every '
   'other error combined.</p>\n'
   + tbl(('Cause', 'Fix'),
         [('Year-end taken from when trading started',
           'Use the date on the incorporation record'),
          ('Year-end more than 53 weeks after incorporation',
           'Bring it inside the 53-week limit'),
          ('Business number or RC account not yet active',
           'Confirm the account before transmitting'),
          ('Corporation name not matching the registry', 'Use the exact legal name')])
   + '\n<p>One corrected transmission is included in the fee where the Agency '
   'rejects the first.</p>', True),
  ('bn', 'The Business Number and RC Account',
   '<p>The return is filed against the nine-digit business number and its RC '
   'corporation income tax account. Most corporations receive the number at '
   'incorporation, but it is confirmed as active before the first return goes '
   'out.</p>\n'
   '<p>A corporation that never received one obtains it from the Canada Revenue '
   'Agency first.</p>'),
  ('gifi-first', 'GIFI on a First Return',
   '<p>A first-year corporation almost always has something on its balance sheet: '
   'the share capital issued on incorporation, and often the incorporation costs '
   'themselves.</p>\n'
   '<div class="ei-warn"><p>That makes GIFI Schedules 100, 125 and 141 required on '
   'most first returns, even where the corporation never traded. The exemption for '
   'a corporation with nothing at all to report rarely applies in year one.</p>'
   '</div>\n'
   '<p>The detail is in the guide to '
   + a(HUB + 'gifi-schedules-100-125-141/', 'GIFI Schedules 100, 125 and 141')
   + '.</p>', True),
  ('deadline', 'The First Filing Deadline',
   '<p>Six months after the first fiscal year-end, like every other year. A '
   'corporation incorporated in March with a December year-end has its first return '
   'due the following June.</p>\n'
   '<p>Every fiscal year-end and its due date is listed on '
   + a(SITE + '/deadlines/', 'T2 filing deadlines') + '.</p>'),
  ('missed-first', 'A First Year That Was Never Filed',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>An unfiled first year is the one that compounds, because every later year '
   'sits on top of it and the Agency has no opening record for the corporation at '
   'all. Schedule 24 is still filed, late, on whichever return turns out to be the '
   'first one transmitted.</p>', True),
 ],
 faq=[
  ('When Does My First Tax Year Start?',
   'On the incorporation date, not the day trading started. A corporation '
   'registered and never used still has a tax year running from the date on its '
   'incorporation record.'),
  ('How Long Can My First Tax Year Be?',
   'Up to 53 weeks. Within that window the year-end date is the '
   'corporation&rsquo;s own choice, and it is fixed once the first return is '
   'filed.'),
  ('Do I File a T2 if I Never Started the Business?',
   'Yes. Incorporating creates the obligation. A corporation that never opened for '
   'business files a nil return rather than no return.'),
  ('What Is Schedule 24?',
   'The first-time filer schedule, required on the first return after '
   'incorporation. It reports shareholders, related corporations and how the '
   'corporation came into existence, and it is filed once.'),
  ('Why Was My First Return Rejected?',
   'Almost always a fiscal year-end that differs from the one the Canada Revenue '
   'Agency holds from the incorporation record. One corrected transmission is '
   'included in the fee.'),
  ('Does a First-Year Nil Return Still Need GIFI?',
   'Usually yes. Share capital issued on incorporation and capitalised '
   'incorporation costs both sit on the balance sheet, and either one makes '
   'Schedules 100, 125 and 141 required.'),
 ])

# ---------------------------------------------------------------------------
# Guide 12. /guides/numbered-company-tax-filing/
# Appendix A topic /numbered-company-tax-filing-guide/, slug corrected.
# Cluster support: F5 answer on numbered companies, the Ontario numbered
# service page, and the shelf and holding corporation angle. Hard rule 8 is
# handled head-on in the holding section. Pending sign-off.
# ---------------------------------------------------------------------------
G12 = dict(
 slug='numbered-company-tax-filing',
 title='Numbered Company Tax Filing | Nil T2 Guide for Canada',
 h1='The Complete Guide to Numbered Company Tax Filing',
 h1_pre='The Complete Guide to ',
 h1_span='Numbered Company Tax Filing',
 eyebrow='Numbered Company Guide',
 meta=('Why a numbered company files exactly like a named one, how the CRA identifies '
       'it, what shelf and holding corporations need, and what the filing costs.'),
 convert=(SITE + '/nil-t2-filing/', 'Nil T2 Filing Services'),
 kids=['what-happens-if-i-dont-file-a-nil-t2-for-a-numbered-company',
       'can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'do-i-need-a-business-number-to-file-a-nil-t2',
       'can-i-dissolve-my-corporation-with-unfiled-t2-returns'],
 sections=[
  ('what-is', 'What a Numbered Company Is',
   '<p>A corporation whose legal name is the number the registry assigned it, in the '
   'form 1234567 Ontario Inc. or 9876543 Canada Inc. Nothing was chosen; the '
   'registry issued a number and the corporation kept it.</p>\n'
   '<p>Owners pick a numbered name to incorporate quickly, to avoid a name search, '
   'or because the corporation was never meant to trade under a name of its '
   'own.</p>', True),
  ('same-obligation', 'The Obligation Is Identical',
   '<p>A numbered company is an ordinary corporation. It files a T2 within six '
   'months of each fiscal year-end, every year, until it is formally dissolved, on '
   'exactly the same terms as a corporation with a chosen name.</p>\n'
   '<div class="ei-info"><p>There is no lighter regime for a numbered company, no '
   'different deadline and no different form. The numbered name affects nothing '
   'about the filing.</p></div>'),
  ('bn-not-name', 'The CRA Identifies It by Business Number',
   '<p>The Canada Revenue Agency works from the nine-digit business number and its '
   'RC corporation income tax account, not from the corporate name. For filing '
   'purposes the name is a label on a record the number already identifies.</p>\n'
   '<p>That is why a numbered company is no harder to file for. See '
   + a(A + 'do-i-need-a-business-number-to-file-a-nil-t2/',
       'whether a business number is needed to file a nil T2') + '.</p>', True),
  ('shelf', 'Shelf Corporations',
   '<p>A shelf corporation is one registered and then left unused, held in case it '
   'is wanted later. Most are numbered, because no name was needed for a '
   'corporation that was not going to trade.</p>\n'
   '<p>A shelf corporation is the textbook nil filer: no revenue, no expenses, no '
   'payroll, a return every year reporting nil amounts. What it is not is '
   'exempt.</p>'),
  ('holding', 'Numbered Holding Corporations Are Often Not Nil',
   '<div class="ei-warn"><p>' + NOT_NIL + '</p></div>\n'
   '<p>Many numbered corporations are holding companies, and a holding company '
   'earning investment income has no operations, no staff and no customers while '
   'still falling outside a nil return. The portfolio earns income that belongs on '
   'the return.</p>\n'
   '<p>A numbered holding corporation that genuinely holds nothing and earns nothing '
   'is nil. One holding investments is not.</p>', True),
  ('registry', 'The Registry Record and the Annual Return',
   '<p>A numbered company files an annual return with its registry in exactly the '
   'way a named one does, confirming directors and the registered office. Filing '
   'the T2 does not satisfy it.</p>\n'
   '<p>The full set is in the guide to '
   + a(HUB + 'provincial-and-federal-annual-returns/',
       'provincial and federal annual returns') + '.</p>'),
  ('forgotten', 'Numbered Companies Are the Ones Most Often Forgotten',
   '<p>A numbered corporation has no brand, no website and no letterhead to remind '
   'anyone it exists. It generates no mail the owner recognises and appears on no '
   'invoice.</p>\n'
   '<div class="ei-info"><p>That is why unfiled years cluster on numbered '
   'companies. The obligation did not stop; the reminder did.</p></div>\n'
   '<p>See '
   + a(A + 'can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about/',
       'whether nil T2 returns can be filed for a forgotten corporation') + '.</p>',
   True),
  ('unfiled', 'Unfiled Years on a Numbered Company',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>Each year is a separate return with its own fiscal year-end and its own due '
   'date. Filing several at once is routine and closes the years in a single pass; '
   'the sequence is in the guide to '
   + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
       'catching up on unfiled corporate tax returns') + '.</p>'),
  ('naming', 'Adding a Business Name Later',
   '<p>A numbered company can register a business name and trade under it while '
   'keeping the number as its legal name. The corporation does not change and '
   'neither does its business number.</p>\n'
   '<div class="ei-info"><p>The T2 is filed under the legal numbered name whatever '
   'the corporation trades as. A registered business name is a separate registry '
   'filing, not a change to the corporation.</p></div>', True),
  ('dissolving', 'Dissolving a Numbered Company',
   '<p>Identical to dissolving a named one. Every earlier year must already be '
   'filed, the final T2 is due within six months of the dissolution date, and a '
   'clearance certificate cannot be issued while any tax year is open.</p>\n'
   '<p>Because a numbered company usually has no name worth keeping, dissolution is '
   'more often the right answer than it is for a named corporation. The sequence is '
   'in the guide to '
   + a(HUB + 'final-t2-and-dissolution/', 'the final T2 and dissolution') + '.</p>'),
  ('deadlines', 'Deadlines',
   '<p>Six months after the fiscal year-end, every year. Where a due date falls on a '
   'Saturday, a Sunday or a public holiday recognised by the Canada Revenue Agency, '
   'a return received the next business day is on time.</p>\n'
   '<p>Every fiscal year-end and its due date is listed on '
   + a(SITE + '/deadlines/', 'T2 filing deadlines') + '.</p>', True),
 ],
 faq=[
  ('Does a Numbered Company File a Different Return?',
   'No. It files the same T2, on the same deadline, with the same schedules. The '
   'numbered name affects nothing about the filing obligation.'),
  ('How Does the CRA Know Which Corporation It Is?',
   'By the nine-digit business number and its RC corporation income tax account. '
   'The corporate name is a label on a record the number already identifies.'),
  ('Is a Shelf Corporation a Nil Filer?',
   'Usually yes. A corporation registered and left unused has no revenue and no '
   'expenses, so it files a nil return every year until it is dissolved.'),
  ('Is a Numbered Holding Company Nil?',
   'Not where it earns investment income. A holding corporation with investment '
   'income, a rental corporation and a corporation that paid or received a dividend '
   'are not nil, and are handled by Gondaliya CPA Professional Corporation at '
   'gondaliyacpa.ca at $350.00 plus HST per year.'),
  ('Can I Trade Under a Name Instead of the Number?',
   'Yes, by registering a business name with the registry. The corporation and its '
   'business number do not change, and the T2 is still filed under the legal '
   'numbered name.'),
  ('Why Do Numbered Companies End Up With Unfiled Years?',
   'Because nothing reminds the owner they exist. No brand, no letterhead, no '
   'invoices. The filing obligation continues whether or not anything prompts '
   'it.'),
 ])

GUIDES = [G8, G9, G10, G11, G12]

# ---------------------------------------------------------------------------
# Render. Same structure as the pillar and batch 2.
# ---------------------------------------------------------------------------
KID_TITLES = {}
for r in json.load(open(os.path.join(HERE, '..', 'f5', 'f5-manifest.json'),
                        encoding='utf-8')):
    KID_TITLES[r['slug']] = r['meta']['cnf_question_text']

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

# Guides 8, 9 and 10 are already published. Their byte counts are the check
# that this rebuilt generator reproduces the original output exactly.
PUBLISHED = {'how-to-file-a-nil-t2-return': 23902,
             'gifi-schedules-100-125-141': 21557,
             'schedule-8-and-loss-continuity': 22390}

records = []
for g in GUIDES:
    html, url = render(g)
    records.append(dict(slug=g['slug'], title=g['title'], h1=g['h1'],
                        meta_description=g['meta'], url=url, content=html,
                        toc=[t[1] for t in g['sections']] + ['What the Fee Covers']))
    open(os.path.join(HERE, g['slug'] + '.html'), 'w', encoding='utf-8').write(html)

json.dump(records, open(os.path.join(HERE, 'f9-batch3-manifest.json'), 'w'),
          ensure_ascii=False, indent=1)

ok = True
for r in records:
    n = len(r['content'].encode())
    want = PUBLISHED.get(r['slug'])
    if want is None:
        print('%-36s %6d bytes' % (r['slug'], n))
    elif n == want:
        print('%-36s %6d bytes  matches published' % (r['slug'], n))
    else:
        ok = False
        print('%-36s %6d bytes  MISMATCH, published is %d' % (r['slug'], n, want))
raise SystemExit(0 if ok else 1)
