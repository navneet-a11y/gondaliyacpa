"""Family 9 batch 4: guides 13 to 17 of 30.

Topics taken from Appendix A's Family 9 list, slugs corrected to the /guides/
base per 6(a) line 1147, continuing the resolution batch 3 recorded as the
19th plan conflict. Appendix A's own URL shapes stay unusable: they are
root-level, which collides with the Family 4 catch-all, and ten of them carry a
year token, which 6(k) line 1749 forbids outright.

  /t2-late-filing-penalty-guide/          -> /guides/t2-late-filing-penalties/
  /cra-demand-to-file-response-guide/     -> /guides/cra-demand-to-file-response/
  /inactive-holding-company-filing-guide/ -> /guides/inactive-holding-company-filing/
  /the-ultimate-guide-to-t2-schedules-on-a-nil-return/
                                          -> /guides/t2-schedules-on-a-nil-return/
  /the-ultimate-guide-to-keeping-a-shelf-corporation-compliant/
                                          -> /guides/shelf-corporation-compliance/

The two "ultimate guide" topics are kept as topics and dropped as titles. Hard
rule 4 bans superlative claims, and while it names price superlatives, putting
"the ultimate guide" in ten H1s and ten URLs is the same move aimed at the
content. Flagged for sign-off rather than decided here.

Guide 15 is the one to read closely. Hard rule 8 says a holding corporation is
not nil, so a guide about holding companies has to carry that in its own first
section rather than bury it, and it does: the narrow case where a holding
company genuinely is nil is stated, and everything else is routed to
gondaliyacpa.ca at $350.00 plus HST per year.

Registry. These five take Family 9 from 12 to 17, so every guide now carries 16
sibling links. The twelve already published must be regenerated and updated or
their sibling lists silently omit this batch.
"""
import json, os

HERE  = os.path.dirname(os.path.abspath(__file__))
SITE  = 'https://corpnilfilingfor300.ca'
FORM  = SITE + '/form/'
HUB   = SITE + '/guides/'
A     = SITE + '/answers/'
COST  = SITE + '/pricing/nil-t2-filing-cost/'
TODAY, ISO = 'October 22, 2026', '2026-10-22'
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
assert len(REGISTRY) == 17, 'registry must carry all 17 before batch 4 renders'

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
# Guide 13. /guides/t2-late-filing-penalties/
# Appendix A topic /t2-late-filing-penalty-guide/, slug corrected to the
# /guides/ base per 6(a) line 1147. This is the guide most exposed to hard
# rule 3, so the qualification sentence sits in its own section near the top
# and every later mention of a nil return and a penalty points back to it.
# ---------------------------------------------------------------------------
G13 = dict(
 slug='t2-late-filing-penalties',
 title='T2 Late Filing Penalties | Guide for Canadian Corporations',
 h1='The Complete Guide to T2 Late Filing Penalties',
 h1_pre='The Complete Guide to ',
 h1_span='T2 Late Filing Penalties',
 eyebrow='Penalties Guide',
 meta=('How the percentage penalty is calculated, why a nil return is different, '
       'the paper and preparer penalties, and what an unfiled year costs.'),
 convert=(SITE + '/catch-up-nil-t2-filing/', 'Catch-Up Nil T2 Filing'),
 kids=['can-i-file-a-nil-t2-late-without-a-penalty',
       'what-happens-if-i-dont-file-a-nil-t2',
       'what-happens-if-i-dont-file-my-t2-for-five-years',
       'what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2',
       'can-i-file-five-years-of-nil-t2-returns-at-once',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive'],
 sections=[
  ('percentage', 'How the Percentage Penalty Is Calculated',
   '<p>The late-filing penalty on a T2 is a percentage of the tax owing on the '
   'return. It is 5% of the unpaid tax, plus 1% of that unpaid tax for each '
   'complete month the return is late, to a maximum of 12 months.</p>\n'
   + tbl(('Element', 'Amount'),
         [('Base penalty', '5% of the unpaid tax'),
          ('Monthly addition', '1% of the unpaid tax per complete month late'),
          ('Maximum months counted', '12'),
          ('Applied to', 'Tax owing on the return, not revenue and not assets')])
   + '\n<p>Every figure above is a percentage of one number: the tax owing. That '
   'is the whole reason a nil return behaves differently.</p>', True),
  ('nil-different', 'Why a Nil Return Is Different',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>Both halves of that statement are true at once, and neither is useful on '
   'its own. A corporation owing $0.00 has nothing for the percentage to be a '
   'percentage of. The same corporation still has an open year on its record, and '
   'that is what the rest of this guide is about.</p>\n'
   '<p>See ' + a(A + 'can-i-file-a-nil-t2-late-without-a-penalty/',
                 'whether a nil T2 can be filed late') + ' for the short answer.</p>'),
  ('repeated', 'The Larger Penalty for a Repeated Failure',
   '<p>Where the Canada Revenue Agency has already issued a demand to file, and a '
   'late-filing penalty was charged in any of the three preceding tax years, the '
   'penalty doubles.</p>\n'
   + tbl(('Situation', 'Base', 'Monthly', 'Maximum months'),
         [('First late return', '5%', '1%', '12'),
          ('Repeated failure after a demand', '10%', '2%', '20')])
   + '\n<p>It is still a percentage of tax owing, so a nil year still produces '
   '$0.00 under it. A corporation that is nil in one year and trading in the next '
   'is the one this rule catches.</p>', True),
  ('paper', 'The Paper Filing Penalty and the Preparer Penalty',
   '<p>For tax years starting after 2023 electronic filing is mandatory for '
   'virtually all corporations. A paper T2 draws a $1,000.00 penalty plus a '
   '$100.00 per-return preparer penalty.</p>\n'
   '<div class="ei-warn"><p>This is the one penalty on this page that is not a '
   'percentage of tax owing. It is a flat amount, and a nil return is not exempt '
   'from it. A corporation with no activity that files on paper is exposed to the '
   'full $1,000.00.</p></div>\n'
   '<p>Returns are transmitted electronically here, by a registered EFILE '
   'electronic filer.</p>'),
  ('non-resident', 'The Non-Resident Penalty of $25.00 a Day',
   '<p>A non-resident-owned corporation that fails to file faces a penalty built on '
   'days rather than on tax owing: $25.00 per day, to a maximum of $2,500.00.</p>\n'
   '<p>Because it is not a percentage, a nil year reaches the maximum exactly as a '
   'trading year does. It is the single largest exposure a dormant '
   'non-resident-owned corporation carries.</p>', True),
  ('demand', 'What a Demand to File Changes',
   '<p>A demand to file is a formal written requirement to file a named return by a '
   'named date. It converts an overdue return into a legal obligation with its own '
   'deadline, and it starts the clock on the repeated-failure rate above.</p>\n'
   '<p>The response is covered in full in the guide to '
   + a(HUB + 'cra-demand-to-file-response/', 'responding to a CRA demand to file')
   + '.</p>'),
  ('arbitrary', 'Arbitrary Assessment',
   '<p>Where a demand goes unanswered, the Canada Revenue Agency may assess the '
   'corporation on its own estimate of income. That assessment is a real debt, '
   'collectible, and it stands until it is displaced by a filed return.</p>\n'
   '<div class="ei-danger"><p>An arbitrary assessment is how a corporation that '
   'owed $0.00 ends up owing a figure with interest running on it. The amount is '
   'an estimate the corporation did not provide and cannot be argued down without '
   'filing the actual return.</p></div>', True),
  ('interest', 'Interest, and What It Attaches To',
   '<p>Interest is charged on an unpaid balance, compounded daily. A nil return '
   'produces no balance, so there is nothing for interest to run on.</p>\n'
   + tbl(('Charge', 'Attaches to', 'On a true nil year'),
         [('Percentage late-filing penalty', 'Tax owing', '$0.00'),
          ('Interest', 'An unpaid balance', '$0.00'),
          ('Paper filing penalty', 'The filing method', '$1,000.00 if filed on paper'),
          ('Preparer penalty', 'Each paper return prepared', '$100.00'),
          ('Non-resident penalty', 'Days late', 'Up to $2,500.00')])
   + '\n<p>Read the table by column rather than by row. Two of the five charges '
   'ignore tax owing entirely.</p>'),
  ('clearance', 'What an Open Year Blocks',
   '<p>An unfiled year blocks a clearance certificate, and a clearance certificate '
   'is what a corporation needs before it can be wound up cleanly. It also stops a '
   'voluntary dissolution from completing.</p>\n'
   '<p>The sequence is set out in the guide to '
   + a(HUB + 'final-t2-and-dissolution/', 'the final T2 and dissolution') + '.</p>', True),
  ('how-long', 'How Long an Unfiled Year Stays Open',
   '<p>Indefinitely. There is no point at which an unfiled T2 year closes itself, '
   'and no number of later filings that settles an earlier gap.</p>\n'
   '<div class="ei-info"><p>This is why the cost of an unfiled nil year is almost '
   'never the penalty. It is the demand, the arbitrary assessment, the blocked '
   'clearance certificate and the dissolution that cannot complete.</p></div>'),
  ('fixing', 'Filing the Missing Years',
   '<p>Unfiled years are filed oldest first, each on its own return for its own tax '
   'year. Five unfiled nil years are five returns, and they can be prepared and '
   'transmitted together.</p>\n'
   '<p>' + NOT_NIL + '</p>\n'
   '<p>See the guide to '
   + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
       'catching up on unfiled corporate tax returns') + '.</p>', True),
 ],
 faq=[
  ('Is There a Penalty for Filing a Nil T2 Late?',
   'A true nil return carries no percentage late-filing penalty, because that '
   'penalty is a percentage of tax owing and the corporation owes $0.00. The '
   'unfiled year still stays open forever, invites a demand to file and an '
   'arbitrary assessment, blocks a clearance certificate and dissolution, and '
   'costs a non-resident-owned corporation $25.00 per day up to $2,500.00.'),
  ('How Is the T2 Late-Filing Penalty Worked Out?',
   '5% of the unpaid tax, plus 1% of that unpaid tax for each complete month the '
   'return is late, counted to a maximum of 12 months. Every component is a '
   'percentage of tax owing.'),
  ('What Is the Penalty for Filing a T2 on Paper?',
   'For tax years starting after 2023 electronic filing is mandatory for virtually '
   'all corporations. A paper T2 draws a $1,000.00 penalty plus a $100.00 '
   'per-return preparer penalty. A nil return is not exempt from either.'),
  ('When Does the Penalty Rate Double?',
   'Where the Canada Revenue Agency has issued a demand to file and a late-filing '
   'penalty was charged in any of the three preceding tax years. The rate becomes '
   '10% plus 2% per complete month, to 20 months.'),
  ('What Happens if I Ignore a Demand to File?',
   'The Canada Revenue Agency may assess the corporation on its own estimate of '
   'income. That arbitrary assessment is collectible and stands until the actual '
   'return displaces it.'),
  ('Does an Unfiled Year Ever Close on Its Own?',
   'No. An unfiled T2 year stays open indefinitely, and later filings do not '
   'settle an earlier gap.'),
 ])

# ---------------------------------------------------------------------------
# Guide 14. /guides/cra-demand-to-file-response/
# Appendix A topic /cra-demand-to-file-response-guide/, slug corrected.
# 6(d) Family 13 carries "cra demand to file letter" and "arbitrary assessment
# corporation" as blog keywords; this is the pillar those posts link up to.
# ---------------------------------------------------------------------------
G14 = dict(
 slug='cra-demand-to-file-response',
 title='CRA Demand to File | Response Guide for Corporations',
 h1='The Complete Guide to Responding to a CRA Demand to File',
 h1_pre='The Complete Guide to ',
 h1_span='Responding to a CRA Demand to File',
 eyebrow='Demand to File Guide',
 meta=('What a demand to file is, the deadline it sets, what happens if it is '
       'ignored, and how an arbitrary assessment is displaced by filing.'),
 convert=(SITE + '/catch-up-nil-t2-filing/', 'Catch-Up Nil T2 Filing'),
 kids=['what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2',
       'what-happens-if-i-dont-file-my-t2-for-five-years',
       'what-happens-if-i-dont-file-a-nil-t2',
       'can-i-file-five-years-of-nil-t2-returns-at-once',
       'can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about',
       'what-happens-if-i-dont-report-a-dormant-corporation-to-cra'],
 sections=[
  ('what-it-is', 'What a Demand to File Is',
   '<p>A written requirement from the Canada Revenue Agency that a named return be '
   'filed by a named date. It is not a reminder and it is not an assessment. It is '
   'a legal obligation with its own deadline, separate from the original filing '
   'deadline the return already missed.</p>\n'
   '<div class="ei-info"><p>A demand is usually the first contact a dormant '
   'corporation receives. Nothing has gone to collections at this point, and the '
   'position is still straightforward to resolve.</p></div>', True),
  ('why-arrives', 'Why It Arrived',
   '<p>Because the Canada Revenue Agency holds a record showing the corporation '
   'exists and a tax year for which no return was received. Incorporation created '
   'that record, and it persists whether or not the corporation ever traded.</p>\n'
   + tbl(('Trigger', 'What the Agency sees'),
         [('Incorporated and never traded', 'An open tax year with no return'),
          ('Stopped trading, kept the corporation', 'A gap after the last return filed'),
          ('An open RC account', 'A filing obligation on the account'),
          ('A year-end passing with no return',
           'The corporation moving into arrears')])
   + '\n<p>None of the four requires the corporation to have earned anything.</p>'),
  ('read-it', 'Reading the Letter',
   '<p>Three things on the letter decide what happens next: which tax year or years '
   'are named, the date the return is required by, and whether the letter names a '
   'specific officer of the corporation.</p>\n'
   '<div class="ei-warn"><p>The named date is the one that matters. A demand '
   'answered by that date closes the matter. A demand answered late is treated as '
   'a repeated failure, which doubles the percentage penalty rate on any year where '
   'tax is owing.</p></div>', True),
  ('nil-still', 'A Nil Year Still Answers the Demand',
   '<p>Filing a nil return satisfies a demand in exactly the way a trading return '
   'does. The obligation is to file, not to owe.</p>\n'
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>See ' + a(A + 'what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2/',
                 'what happens where a demand to file goes unanswered') + '.</p>'),
  ('ignoring', 'What Happens if It Is Ignored',
   '<p>The Canada Revenue Agency proceeds without the corporation. It may assess on '
   'its own estimate of income, and in a persistent case may pursue the failure '
   'through the courts.</p>\n'
   + tbl(('Stage', 'What it means'),
         [('Demand issued', 'A deadline to file is set'),
          ('Demand unanswered', 'The repeated-failure penalty rate becomes available'),
          ('Arbitrary assessment', 'A tax debt is raised on an estimate'),
          ('Collection', 'That debt is pursued like any other'),
          ('Prosecution', 'Available where the failure persists')])
   + '\n<p>The corporation moves down that table by doing nothing.</p>', True),
  ('arbitrary', 'How an Arbitrary Assessment Works',
   '<p>The Agency estimates income from whatever it holds, assesses tax on that '
   'estimate, and issues a notice. The figure is not a guess the corporation can '
   'correct by explaining; it is an assessment that stands until a filed return '
   'replaces it.</p>\n'
   '<p>Interest runs on the assessed balance from the date it is raised. For a '
   'corporation that genuinely had no activity, this is how a year that owed '
   '$0.00 becomes a debt.</p>'),
  ('displace', 'Displacing an Arbitrary Assessment',
   '<p>By filing the actual return for that year. The filed return is assessed on '
   'its own figures and supersedes the estimate.</p>\n'
   '<div class="ei-info"><p>A nil return displaces an arbitrary assessment to '
   '$0.00 where the corporation truly had no activity. The sooner it is filed, the '
   'less interest has accumulated on the estimate in the meantime.</p></div>', True),
  ('multiple', 'Where the Demand Names Several Years',
   '<p>Each year named is a separate return on its own form for its own tax year. '
   'Five years named is five returns. They are prepared and transmitted together, '
   'oldest first.</p>\n'
   '<p>See ' + a(A + 'can-i-file-five-years-of-nil-t2-returns-at-once/',
                 'whether five years of nil T2 returns can be filed at once')
   + '.</p>'),
  ('is-it-nil', 'Checking the Year Really Was Nil',
   '<p>Before filing, the year is tested rather than assumed. A corporation is nil '
   'for this service only where it had no activity at all in the tax year.</p>\n'
   '<div class="ei-warn"><p>' + NOT_NIL + '</p></div>\n'
   '<p>Share capital, cash, a shareholder loan, an incorporation cost or a bank '
   'charge does not stop the year being nil, but it does make GIFI Schedules 100, '
   '125 and 141 required. The detail is in the guide to '
   + a(HUB + 'gifi-schedules-100-125-141/', 'GIFI Schedules 100, 125 and 141')
   + '.</p>', True),
  ('accounts', 'The Accounts a T2 Does Not Close',
   '<p>Answering a demand for a T2 settles the corporate income tax obligation and '
   'nothing else. An open GST/HST account and an open payroll account each carry '
   'their own filing obligations and generate their own demands.</p>\n'
   '<p>A GST/HST account is closed with Form RC145. Until it is closed or filed '
   'nil, it keeps producing letters of its own.</p>'),
  ('after', 'After the Return Is Transmitted',
   '<p>The confirmation of transmission is the record that the demand was answered. '
   'It is kept with the corporation&rsquo;s minute book alongside the assessment '
   'that follows.</p>\n'
   '<p>Where the corporation is being wound up, the clearance certificate is '
   'applied for only once every open year has been filed. That order is set out in '
   'the guide to ' + a(HUB + 'final-t2-and-dissolution/',
                       'the final T2 and dissolution') + '.</p>', True),
 ],
 faq=[
  ('What Is a CRA Demand to File?',
   'A written requirement from the Canada Revenue Agency that a named return be '
   'filed by a named date. It sets its own deadline, separate from the filing '
   'deadline the return already missed.'),
  ('Does Filing a Nil Return Answer a Demand?',
   'Yes. The obligation is to file, not to owe. A nil return satisfies a demand in '
   'the same way a trading return does.'),
  ('What if I Ignore It?',
   'The Canada Revenue Agency may assess the corporation on its own estimate of '
   'income. That arbitrary assessment is a collectible debt with interest running '
   'on it, and it stands until a filed return displaces it.'),
  ('Can an Arbitrary Assessment Be Reversed?',
   'It is displaced rather than argued down. Filing the actual return for that year '
   'replaces the estimate, and a genuine nil year displaces it to $0.00.'),
  ('The Demand Names Four Years. Is That Four Returns?',
   'Yes. Each tax year is its own return on its own form. They are prepared and '
   'transmitted together, oldest first.'),
  ('Does Answering the Demand Close My GST/HST Account?',
   'No. A T2 settles the corporate income tax obligation only. An open GST/HST '
   'account carries its own filing obligation and is closed with Form RC145.'),
 ])

# ---------------------------------------------------------------------------
# Guide 15. /guides/inactive-holding-company-filing/
# Appendix A topic /inactive-holding-company-filing-guide/, slug corrected.
# Hard rule 8: a holding corporation is not nil. The rule is not a footnote
# here, it is section one, and the narrow case where a holding company is
# genuinely nil is stated precisely so the page cannot be read as an invitation.
# Cluster support: the inactive-holding-corporation service page already live.
# ---------------------------------------------------------------------------
G15 = dict(
 slug='inactive-holding-company-filing',
 title='Inactive Holding Company Filing | Nil T2 Guide for Canada',
 h1='The Complete Guide to Inactive Holding Company Filing',
 h1_pre='The Complete Guide to ',
 h1_span='Inactive Holding Company Filing',
 eyebrow='Holding Company Guide',
 meta=('When a holding corporation is nil and when it is not, what investment '
       'income does to the return, and which schedules a holding company needs.'),
 convert=(SITE + '/inactive-holding-corporation-t2-filing/',
          'Inactive Holding Corporation Filing'),
 kids=['do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'do-i-need-financial-statements-for-a-nil-t2-return',
       'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account',
       'what-happens-if-i-dont-report-a-dormant-corporation-to-cra',
       'can-i-file-a-nil-t2-myself-without-an-accountant'],
 sections=[
  ('not-nil', 'A Holding Corporation With Investment Income Is Not Nil',
   '<div class="ei-danger"><p>' + NOT_NIL + '</p></div>\n'
   '<p>Read that before anything else on this page. Most corporations described as '
   '&ldquo;an inactive holding company&rdquo; turn out to hold something that '
   'earns, and earning is activity. Interest credited on a balance is income. A '
   'dividend received is income. Rent is income.</p>\n'
   '<p>This guide covers both cases, and says plainly which one a corporation is '
   'in. It does not try to make the second case into the first.</p>', True),
  ('when-nil', 'When a Holding Corporation Genuinely Is Nil',
   '<p>Where it held assets that earned nothing at all during the tax year, '
   'received no dividend, paid no dividend, had no revenue of any kind, claimed no '
   'expense, ran no payroll, bought no asset and had no inter-company '
   'transaction.</p>\n'
   + tbl(('In the tax year', 'Nil', 'Not nil'),
         [('Shares held, no dividend received', 'Nil', ''),
          ('Shares held, dividend received', '', 'Not nil'),
          ('Cash in an account earning no interest', 'Nil', ''),
          ('Cash in an account earning interest', '', 'Not nil'),
          ('Property held, no rent charged', 'Nil', ''),
          ('Property rented out', '', 'Not nil'),
          ('A dividend paid up to the shareholder', '', 'Not nil'),
          ('A loan to a related corporation, no interest', 'Nil', ''),
          ('A loan to a related corporation, interest charged', '', 'Not nil')])
   + '\n<p>The left column is the whole of the nil case. One entry in the right '
   'column takes the corporation out of it.</p>'),
  ('interest-trap', 'The Interest Trap',
   '<p>The most common reason a holding corporation believed to be nil is not nil '
   'is a few dollars of interest credited on a bank balance nobody looked at.</p>\n'
   '<div class="ei-warn"><p>There is no minimum. Interest of $4.12 credited across '
   'the year is investment income, and the corporation is not nil for that year. '
   'It is checked on the statements rather than assumed from memory.</p></div>', True),
  ('still-file', 'An Inactive Holding Corporation Still Files',
   '<p>Every resident corporation, including an inactive one, must file a T2 within '
   'six months of its fiscal year-end, every year, until it is formally dissolved. '
   'A final T2 is due within six months of dissolution.</p>\n'
   '<p>Holding structures are frequently left for years on the assumption that a '
   'corporation doing nothing owes nothing to anyone. The obligation is to file, '
   'not to owe.</p>'),
  ('schedules', 'The Schedules a Holding Corporation Needs',
   '<p>A holding corporation almost always has a balance sheet, which is what '
   'decides the schedules.</p>\n'
   + tbl(('Schedule', 'When it is required'),
         [('GIFI 100, 125 and 141',
           'Where there is share capital, cash, a shareholder loan, an '
           'incorporation cost or a bank charge'),
          ('Schedule 50', 'For every shareholder at 10% or more'),
          ('Schedule 24', 'On the first return after incorporation'),
          ('Schedule 8 and loss continuity', 'Recorded')])
   + '\n<p>A corporation inactive all year with nothing at all to report may omit '
   'GIFI Schedules 100, 125 and 141, but any share capital, cash, shareholder '
   'loan, incorporation cost or bank charge makes them required. A holding '
   'corporation holds things by definition, so the exemption rarely reaches '
   'it.</p>', True),
  ('s50', 'Schedule 50 in a Holding Structure',
   '<p>Schedule 50 is needed for any shareholder at 10% or more, and holding '
   'structures concentrate ownership, so it is almost always required.</p>\n'
   '<p>Where the shareholder is itself a corporation, the row records that '
   'corporation and its business number rather than an individual. The detail is '
   'in the guide to ' + a(HUB + 'schedule-8-and-loss-continuity/',
                          'Schedule 8 and loss continuity')
   + ' and on the ' + a(SITE + '/blog/schedule-50-and-the-10-percent-shareholder-rule/',
                        'Schedule 50 and the 10% shareholder rule') + ' post.</p>'),
  ('inter-company', 'Inter-Company Transactions',
   '<p>A transfer between a holding corporation and an operating corporation is a '
   'transaction, and a year containing one is not nil. That includes a management '
   'fee charged, a loan advanced on interest, and an expense paid by one and borne '
   'by the other.</p>\n'
   '<div class="ei-info"><p>An interest-free loan outstanding across the year, with '
   'nothing moving and nothing charged, does not by itself make the year active. '
   'It does put a balance on the balance sheet, which makes the GIFI schedules '
   'required.</p></div>', True),
  ('dividends', 'Dividends, In and Out',
   '<p>A dividend received is income. A dividend paid is a transaction. Either one '
   'ends the nil year, and a corporation that did both is firmly outside it.</p>\n'
   '<p>Work that is not nil is handled by Gondaliya CPA Professional Corporation at '
   'gondaliyacpa.ca at $350.00 plus HST per year. There are no meetings, no '
   'scheduling and no email chains in either direction.</p>'),
  ('shelf', 'A Holding Corporation Held in Reserve',
   '<p>A corporation incorporated to hold a name or a future structure, holding '
   'nothing and earning nothing, is the clearest nil holding case there is. It '
   'still files every year.</p>\n'
   '<p>The maintenance position is set out in the guide to '
   + a(HUB + 'shelf-corporation-compliance/', 'shelf corporation compliance')
   + '.</p>', True),
  ('unfiled', 'Years Already Missed',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>Holding corporations accumulate unfiled years quietly, because nothing '
   'happens to prompt anyone. The gap usually surfaces when the structure is being '
   'reorganised or wound up, at the point a clearance certificate is needed and '
   'cannot be issued.</p>'),
  ('winding-up', 'Winding the Structure Up',
   '<p>Every open year is filed before dissolution, and a final T2 is due within '
   'six months of it. A holding corporation sitting at the top of a structure is '
   'usually the last to be wound up and the one carrying the longest filing '
   'gap.</p>\n'
   '<p>The order is set out in the guide to '
   + a(HUB + 'final-t2-and-dissolution/', 'the final T2 and dissolution') + '.</p>'),
 ],
 faq=[
  ('Is a Holding Company a Nil Corporation?',
   'Not where it has investment income. A holding corporation with investment '
   'income, a rental corporation and a corporation that paid or received a '
   'dividend are not nil. Those are handled by Gondaliya CPA Professional '
   'Corporation at gondaliyacpa.ca at $350.00 plus HST per year.'),
  ('My Holding Company Earned $6 of Interest. Is It Still Nil?',
   'No. There is no minimum. Interest credited on a balance is investment income, '
   'and the corporation is not nil for that tax year.'),
  ('Does an Inactive Holding Company Have to File?',
   'Yes. Every resident corporation, including an inactive one, must file a T2 '
   'within six months of its fiscal year-end, every year, until it is formally '
   'dissolved.'),
  ('Does a Holding Company Need the GIFI Schedules?',
   'Almost always. Share capital, cash, a shareholder loan, an incorporation cost '
   'or a bank charge makes Schedules 100, 125 and 141 required, and a holding '
   'corporation holds assets by definition.'),
  ('Does an Interest-Free Loan to a Subsidiary End the Nil Year?',
   'An interest-free loan left outstanding across the year, with nothing moving '
   'and nothing charged, does not by itself make the year active. It does put a '
   'balance on the balance sheet, which makes the GIFI schedules required.'),
  ('Is Schedule 50 Needed for a Corporate Shareholder?',
   'Yes, where that shareholder holds 10% or more. The row records the '
   'shareholding corporation and its business number rather than an individual.'),
 ])

# ---------------------------------------------------------------------------
# Guide 16. /guides/t2-schedules-on-a-nil-return/
# Appendix A topic /the-ultimate-guide-to-t2-schedules-on-a-nil-return/. The
# superlative is dropped from the title and the slug, per the note at the top
# of this file. Sits above the three schedule guides already live and routes
# to each, so it is a hub within the family rather than a repeat of them.
# ---------------------------------------------------------------------------
G16 = dict(
 slug='t2-schedules-on-a-nil-return',
 title='T2 Schedules on a Nil Return | Guide for Canadian Corporations',
 h1='The Complete Guide to T2 Schedules on a Nil Return',
 h1_pre='The Complete Guide to ',
 h1_span='T2 Schedules on a Nil Return',
 eyebrow='Schedules Guide',
 meta=('Which schedules a nil T2 needs and which it can omit, what makes the '
       'GIFI schedules required, and how each one is decided.'),
 convert=(SITE + '/nil-t2-filing/', 'Nil T2 Filing Services'),
 kids=['do-i-need-financial-statements-for-a-nil-t2-return',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account',
       'do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
       'can-i-file-a-nil-t2-myself-without-an-accountant',
       'do-i-need-a-business-number-to-file-a-nil-t2'],
 sections=[
  ('what-decides', 'What Decides Which Schedules Are Needed',
   '<p>Not the amount of income, which is $0.00 on every nil return. What the '
   'corporation holds, who owns it, and whether this is its first return.</p>\n'
   + tbl(('Schedule', 'Decided by'),
         [('GIFI 100, 125 and 141', 'What sits on the balance sheet'),
          ('Schedule 50', 'Who owns 10% or more'),
          ('Schedule 24', 'Whether this is the first return after incorporation'),
          ('Schedule 8 and loss continuity', 'Whether there is anything to carry forward')])
   + '\n<p>Three of the four have nothing to do with trading, which is why a '
   'corporation that did nothing all year still files schedules.</p>', True),
  ('gifi-rule', 'The GIFI Rule, Stated Exactly',
   '<p>A corporation inactive all year with nothing to report may omit GIFI '
   'Schedules 100, 125 and 141, but any share capital, cash, shareholder loan, '
   'incorporation cost or bank charge makes them required.</p>\n'
   '<div class="ei-warn"><p>Read the second half carefully. The exemption needs '
   '<em>nothing at all</em> to report. A corporation holding $100.00 of share '
   'capital issued at incorporation has something to report, and the schedules are '
   'required.</p></div>\n'
   '<p>The full treatment is in the guide to '
   + a(HUB + 'gifi-schedules-100-125-141/', 'GIFI Schedules 100, 125 and 141')
   + '.</p>'),
  ('five-triggers', 'The Five Things That Make GIFI Required',
   tbl(('Trigger', 'Why it counts'),
       [('Share capital', 'Issued at incorporation and sits on the balance sheet'),
        ('Cash', 'A balance in an account is an asset'),
        ('A shareholder loan', 'A balance either owed to or by the corporation'),
        ('An incorporation cost', 'Capitalised, so it remains on the balance sheet'),
        ('A bank charge', 'An expense, so there is something on the income statement')])
   + '\n<p>Four of the five are present in most corporations from the day they are '
   'registered, which is why the exemption is narrower in practice than it '
   'reads.</p>', True),
  ('s100', 'Schedule 100, the Balance Sheet',
   '<p>The balance sheet in GIFI codes: what the corporation owns, what it owes, '
   'and the share capital and retained earnings that make up the difference.</p>\n'
   '<p>On a nil return it is usually short. Share capital on one line, perhaps a '
   'bank balance, perhaps a shareholder loan. Short is not the same as '
   'omitted.</p>'),
  ('s125', 'Schedule 125, the Income Statement',
   '<p>Revenue and expenses in GIFI codes. On a genuinely nil year both sides are '
   '$0.00, and the schedule says so explicitly rather than being left out.</p>\n'
   '<div class="ei-info"><p>A single bank charge is an expense, and it belongs on '
   'Schedule 125. It does not stop the year being nil for this service, but it '
   'does mean the schedule is filed.</p></div>', True),
  ('s141', 'Schedule 141, the Notes Checklist',
   '<p>The notes checklist records who prepared the financial information and what '
   'level of involvement they had. It accompanies Schedules 100 and 125 and is '
   'filed with them.</p>\n'
   '<p>See ' + a(A + 'do-i-need-financial-statements-for-a-nil-t2-return/',
                 'whether financial statements are needed for a nil T2 return')
   + '.</p>'),
  ('s50', 'Schedule 50, Shareholders at 10% or More',
   '<p>Schedule 50 is needed for any shareholder at 10% or more. It lists each of '
   'them, their percentage of common and preferred shares, and their '
   'identification number.</p>\n'
   '<p>The test is ownership of the shares, not involvement in the company. A '
   'shareholder who has never attended a meeting still appears where the holding '
   'reaches the threshold. The detail is on the '
   + a(SITE + '/blog/schedule-50-and-the-10-percent-shareholder-rule/',
       'Schedule 50 and the 10% shareholder rule') + ' post.</p>', True),
  ('s24', 'Schedule 24, First Return Only',
   '<p>Schedule 24 is needed on the first return after incorporation. It reports '
   'the corporation&rsquo;s shareholders, its related corporations and how it came '
   'into existence, and it is filed once.</p>\n'
   '<p>Where a first year was never filed, Schedule 24 is still filed, late, on '
   'whichever return turns out to be the first one transmitted. The detail is in '
   'the guide to ' + a(HUB + 'first-year-t2-filing/', 'first-year T2 filing')
   + '.</p>'),
  ('s8', 'Schedule 8 and Loss Continuity',
   '<p>Schedule 8 and loss continuity must be recorded. A nil year adds nothing to '
   'either, but the continuity has to be carried forward intact so a later year '
   'can use it.</p>\n'
   '<div class="ei-warn"><p>This is the schedule most often skipped on a nil '
   'return, and the one that costs the most to skip. A break in loss continuity is '
   'discovered in the year the corporation finally has income to apply it '
   'against.</p></div>\n'
   '<p>The full treatment is in the guide to '
   + a(HUB + 'schedule-8-and-loss-continuity/', 'Schedule 8 and loss continuity')
   + '.</p>', True),
  ('short', 'The T2 Short and Its Schedules',
   '<p>The T2 Short is available only to a CCPC with nil net income or a loss, one '
   'permanent establishment, no taxable dividends paid or received, Canadian '
   'currency, no refundable credits, no Ontario transitional debit and no section '
   '34.2 amount.</p>\n'
   '<p>Qualifying for the shorter form does not remove a schedule that is '
   'otherwise required. Eligibility is covered in the guide to '
   + a(HUB + 't2-short-eligibility/', 'T2 Short eligibility') + '.</p>'),
  ('included', 'Every Schedule Above Is in the Price',
   '<p>There is no per-schedule charge. The fee of ' + PRICE + ' covers one nil T2 '
   'return for one corporation for one tax year, with whichever of these schedules '
   'that return requires.</p>\n'
   '<p>' + NOT_NIL + '</p>', True),
 ],
 faq=[
  ('Which Schedules Does a Nil T2 Need?',
   'It depends on what the corporation holds rather than what it earned. GIFI '
   'Schedules 100, 125 and 141 where there is anything on the balance sheet, '
   'Schedule 50 for any shareholder at 10% or more, Schedule 24 on a first return, '
   'and Schedule 8 with loss continuity recorded.'),
  ('Can a Nil Return Skip the GIFI Schedules?',
   'Only where the corporation was inactive all year with nothing at all to '
   'report. Any share capital, cash, shareholder loan, incorporation cost or bank '
   'charge makes Schedules 100, 125 and 141 required.'),
  ('Does Share Capital Alone Make GIFI Required?',
   'Yes. Share capital issued at incorporation sits on the balance sheet, which is '
   'something to report, so the schedules are required.'),
  ('Do I Need Schedule 24 Every Year?',
   'No. Schedule 24 is filed once, on the first return after incorporation.'),
  ('Why File Schedule 8 on a Year With Nothing in It?',
   'To carry the continuity forward intact. A break is only discovered in the year '
   'the corporation finally has income to apply a loss against.'),
  ('Is There an Extra Charge for Schedules?',
   'No. The fee is ' + PRICE + ' and covers whichever schedules the return '
   'requires.'),
 ])

# ---------------------------------------------------------------------------
# Guide 17. /guides/shelf-corporation-compliance/
# Appendix A topic /the-ultimate-guide-to-keeping-a-shelf-corporation-compliant/,
# superlative dropped. Cluster support: F1 carries a shelf-corporation vertical
# and the dormant and numbered guides are already live. The angle that keeps
# this off the dormant guide is the non-tax obligations -- the annual returns
# and the registry filings a shelf corporation loses first.
# ---------------------------------------------------------------------------
G17 = dict(
 slug='shelf-corporation-compliance',
 title='Shelf Corporation Compliance | Filing Guide for Canada',
 h1='The Complete Guide to Shelf Corporation Compliance',
 h1_pre='The Complete Guide to ',
 h1_span='Shelf Corporation Compliance',
 eyebrow='Shelf Corporation Guide',
 meta=('What a corporation held in reserve still has to file each year, the '
       'annual returns that are not the T2, and what lapses first.'),
 convert=(SITE + '/dormant-corporation-filing/', 'Dormant Corporation Filing'),
 kids=['do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
       'can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about',
       'what-happens-if-i-dont-report-a-dormant-corporation-to-cra',
       'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account',
       'what-happens-if-i-dont-file-a-nil-t2'],
 sections=[
  ('what-it-is', 'What a Shelf Corporation Is',
   '<p>A corporation registered and then held without trading, kept so the name, '
   'the incorporation date or the structure is available when it is needed.</p>\n'
   '<p>It is a dormant corporation with an intention attached. The filing '
   'obligations are identical either way, because the Canada Revenue Agency and '
   'the corporate registries record what a corporation is, not what it is for.</p>',
   True),
  ('three-obligations', 'Three Separate Obligations, Not One',
   '<p>This is where shelf corporations are lost. Filing a T2 satisfies one '
   'obligation out of three, and the other two sit with different bodies on '
   'different timetables.</p>\n'
   + tbl(('Filing', 'Filed with', 'When'),
         [('T2 corporate income tax return', 'Canada Revenue Agency',
           'Within six months of the fiscal year-end, every year'),
          ('Ontario annual return', 'Ontario Business Registry',
           'Annually, since October 2021, separately from the T2'),
          ('Federal annual return',
           'Corporations Canada, for a federally incorporated corporation',
           'Within 60 days of the anniversary date, $12.00')])
   + '\n<p>A corporation can be perfectly current on its T2 and still be struck '
   'from a registry for missing the other two.</p>'),
  ('t2', 'The T2, Every Year, Without Exception',
   '<p>Every resident corporation, including an inactive one, must file a T2 within '
   'six months of its fiscal year-end, every year, until it is formally dissolved. '
   'A final T2 is due within six months of dissolution.</p>\n'
   '<div class="ei-info"><p>There is no dormant status to elect, no form that '
   'pauses the obligation, and no threshold below which it stops. A corporation '
   'held on a shelf for nine years owes nine returns.</p></div>', True),
  ('ontario', 'The Ontario Annual Return',
   '<p>The Ontario annual return is filed through the Ontario Business Registry '
   'since October 2021, not with the T2. Before that date it travelled with the '
   'corporate tax return, which is why so many corporations stopped filing it '
   'without noticing.</p>\n'
   '<p>A shelf corporation registered before 2021 and left alone since is the exact '
   'profile that has an unfiled registry return and no idea of it.</p>'),
  ('federal', 'The Federal Annual Return and the $12.00 Fee',
   '<p>Federal corporations file a separate $12.00 Corporations Canada annual '
   'return within 60 days of their anniversary. It is not a tax return and it does '
   'not report income.</p>\n'
   '<div class="ei-warn"><p>Missing it is what leads to dissolution for cause. A '
   'federally incorporated shelf corporation can be dissolved by Corporations '
   'Canada while its tax filings are entirely up to date.</p></div>', True),
  ('provincial', 'Alberta and Quebec Have Their Own Returns',
   '<p>Alberta AT1 and Quebec CO-17 are separate provincial returns. A shelf '
   'corporation with a permanent establishment in either province files there as '
   'well as federally.</p>\n'
   '<p>The provincial and federal position is set out in the guide to '
   + a(HUB + 'provincial-and-federal-annual-returns/',
       'provincial and federal annual returns') + '.</p>'),
  ('accounts', 'Open GST/HST and Payroll Accounts',
   '<p>An open GST/HST account or an open payroll account still needs nil filings, '
   'or a closure using Form RC145. An inactive T2 does not close those '
   'accounts.</p>\n'
   '<p>A shelf corporation that once registered for GST/HST and never deregistered '
   'is accruing a second set of missed filings alongside its T2 years.</p>', True),
  ('is-it-nil', 'Whether the Shelf Year Is Actually Nil',
   '<p>Usually yes, and that is the point of the structure. The exceptions are '
   'narrow and worth checking against rather than assuming.</p>\n'
   '<div class="ei-warn"><p>' + NOT_NIL + '</p></div>\n'
   '<p>Interest credited on a dormant bank balance is the common one. It is '
   'investment income, and the year is not nil.</p>'),
  ('schedules', 'What a Shelf Corporation Still Reports',
   '<p>Share capital issued at incorporation sits on the balance sheet from day '
   'one, so GIFI Schedules 100, 125 and 141 are required on most shelf returns '
   'despite there being no activity.</p>\n'
   + tbl(('Schedule', 'On a shelf corporation'),
         [('GIFI 100, 125 and 141', 'Usually required, because share capital exists'),
          ('Schedule 50', 'Required where any shareholder holds 10% or more'),
          ('Schedule 24', 'On the first return only'),
          ('Schedule 8 and loss continuity', 'Recorded, carrying forward unchanged')])
   + '\n<p>The full position is in the guide to '
   + a(HUB + 't2-schedules-on-a-nil-return/', 'T2 schedules on a nil return')
   + '.</p>', True),
  ('catching-up', 'A Shelf Corporation With Missed Years',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>Unfiled years are filed oldest first, one return per tax year. Six years '
   'held on a shelf and never filed is six returns, prepared and transmitted '
   'together.</p>\n'
   '<p>See ' + a(A + 'can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about/',
                 'filing nil T2 returns for a corporation that was forgotten about')
   + '.</p>'),
  ('selling', 'Before the Corporation Is Used or Sold',
   '<p>A shelf corporation is worth what its record is worth. A buyer, a bank or a '
   'lawyer completing a transaction looks at the filing history, and an open year '
   'stops the transaction rather than discounting it.</p>\n'
   '<div class="ei-info"><p>The filings are brought current before the corporation '
   'is needed, not during the week it is needed. Catching up six years takes '
   'preparation time that a closing date does not leave.</p></div>', True),
 ],
 faq=[
  ('Does a Shelf Corporation Have to File a T2?',
   'Yes, every year. Every resident corporation, including an inactive one, must '
   'file a T2 within six months of its fiscal year-end, every year, until it is '
   'formally dissolved.'),
  ('Is There a Dormant Status I Can Elect?',
   'No. There is no status that pauses the filing obligation and no threshold '
   'below which it stops.'),
  ('Is the Ontario Annual Return Part of the T2?',
   'Not since October 2021. It is filed through the Ontario Business Registry, '
   'separately from the corporate tax return.'),
  ('What Is the $12 Federal Annual Return?',
   'A separate Corporations Canada filing for federally incorporated '
   'corporations, due within 60 days of the anniversary date. It is not a tax '
   'return, and missing it can lead to dissolution for cause.'),
  ('My Shelf Corporation Earned Bank Interest. Is It Nil?',
   'No. Interest credited on a balance is investment income, so the year is not '
   'nil for this service.'),
  ('Can I Catch Up Six Years at Once?',
   'Yes. Each year is its own return, filed oldest first, and they are prepared '
   'and transmitted together.'),
 ])

GUIDES = [G13, G14, G15, G16, G17]

# ---------------------------------------------------------------------------
# Render. Identical to the pillar, batch 2 and batch 3.
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

records = []
for g in GUIDES:
    html, url = render(g)
    records.append(dict(slug=g['slug'], title=g['title'], h1=g['h1'],
                        meta_description=g['meta'], url=url, content=html,
                        toc=[t[1] for t in g['sections']] + ['What the Fee Covers']))
    open(os.path.join(HERE, g['slug'] + '.html'), 'w', encoding='utf-8').write(html)

json.dump(records, open(os.path.join(HERE, 'f9-batch4-manifest.json'), 'w'),
          ensure_ascii=False, indent=1)

for r in records:
    print('%-36s %6d bytes  %2d sections' % (r['slug'], len(r['content'].encode()),
                                             len(r['toc'])))
