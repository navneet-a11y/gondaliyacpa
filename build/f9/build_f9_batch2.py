"""Family 9 batch 2: the six remaining 6(b) pillars.

6(b) line 1194-1200 is the authority for these six URLs, their entry keywords,
their cluster families and their conversion paths. Appendix A's Family 9 list is
not usable: it gives 30 root-level slugs with no /guides/ base, and ten of them
carry a 2026 token, which 6(a) line 1147 ("No year token in any guide URL") and
the 6(k) year-stamp rule ("A guide URL with 2026 or 2027 in the slug is never
created") both forbid outright. Logged as the 19th plan conflict.

  6(a) line 1147   /guides/<guide>/, template "guide", 30 URLs, no year token.
  line 1217 gate   "No pillar publishes without a visible update date and a
                   12-row on-page contents block." Banned term: CRA endorsed.
                   Schedule: 10 on October 9 and 20 on October 30, 2026.
  6(g) line 1528   F9: minimum 12 inbound, maximum 40 outbound.
  7.9 line 1565    Visible date under the H1, above the contents block.
  line 1487        Article schema block for every Family 9 URL.
  7.4              Three-sentence EFILE block on every Family 9 pillar.
  7.6              The 14 REQUIRED QUALIFICATIONS are the factual spine.

Design. The CSS is sliced out of the built pillar rather than copied, so the
six cannot drift from /guides/nil-t2-return-complete-guide/.

Conversion paths. 6(b) names a conversion step for each pillar. Three of them
do not exist yet, so a live substitute is used and the real target is recorded
in decisions.md:
  t2-short-eligibility      -> /tools/t2-short-eligibility-checker/ (F2, 0 of
                               150 live)        substitute /t2-short-filing/
  catch-up-unfiled...       -> /pricing/cost-to-file-six-unfiled-nil-years/
                               (F8, not built)  substitute /catch-up-nil-t2-filing/
  t183corp-signing...       -> /security/ (F15, not built)
                               substitute /sharad-gondaliya-cpa/
  final-t2-and-dissolution  -> /case-studies/... (F13, not built)
                               substitute /final-t2-before-dissolution/

Authorship. Line 1217 owner is "Sharad Gondaliya reviews, Navneet publishes".
These six are drafted to the plan's shape and are pending his sign-off.
"""
import json, os, re

from f9_registry import sibling_links

HERE  = os.path.dirname(os.path.abspath(__file__))
SITE  = 'https://corpnilfilingfor300.ca'
FORM  = SITE + '/form/'
HUB   = SITE + '/guides/'
A     = SITE + '/answers/'
PILLAR = HUB + 'nil-t2-return-complete-guide/'
TODAY, ISO = 'October 19, 2026', '2026-10-19'
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

# CSS sliced from the built pillar so the six cannot drift from it.
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

def cta_inline(h3, p):
    return ('<div class="ei-wrap"><div class="ei-cta-inline"><div><h3>%s</h3><p>%s</p>'
            '</div><a class="ei-btn-blue" href="%s">Start Nil T2 Filing NOW</a></div>'
            '</div>\n' % (h3, p, FORM))

def fee_section(lead, key='fee', alt=False):
    return sec(key, 'What the Fee Covers',
               '<p>' + lead + '</p>\n' + tbl(('Included', 'Detail'), FEE_ROWS)
               + '\n<p>See the full '
               + a(SITE + '/pricing/nil-t2-filing-cost/', 'nil T2 filing cost')
               + '.</p>', alt=alt)

# ---------------------------------------------------------------------------
# Guide 1. /guides/dormant-and-inactive-corporations/
# 6(b): clusters F1 and the F4 dormant and no-activity slugs, 271 URLs,
# entry keyword "dormant corporation", second largest cluster on the site.
# ---------------------------------------------------------------------------
G1 = dict(
 slug='dormant-and-inactive-corporations',
 title='Dormant Corporations | Complete Filing Guide for Canada',
 h1='The Complete Guide to Dormant and Inactive Corporations',
 h1_span='Dormant and Inactive Corporations',
 h1_pre='The Complete Guide to ',
 eyebrow='Dormant Corporation Guide',
 meta=('What dormant means to the Canada Revenue Agency, which returns a dormant '
       'corporation still files, what keeps it compliant, and when to wind it up.'),
 convert=(SITE + '/dormant-corporation-filing/', 'Dormant Corporation Filing'),
 kids=['what-happens-if-i-dont-report-a-dormant-corporation-to-cra',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account',
       'do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
       'can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about'],
 sections=[
  ('what-dormant-means', 'What Dormant and Inactive Actually Mean',
   '<p>Dormant and inactive are descriptions of what a corporation did, not statuses the '
   'Canada Revenue Agency recognises. A corporation that holds no assets, earns nothing '
   'and trades not at all is described as dormant. Its filing obligation is identical to '
   'that of a corporation turning over millions.</p>\n'
   '<p>The obligation comes from being an incorporated resident corporation. It does not '
   'depend on earning anything, holding a bank account, or having employees, and there '
   'is no minimum income below which the return can be skipped.</p>', True),
  ('no-dormancy-filing', 'There Is No Dormancy Filing',
   '<p>There is no form that registers a corporation as dormant and no form that pauses '
   'the T2. Telling the Canada Revenue Agency that a corporation is inactive does not '
   'replace the return, and no letter or phone call changes the due date.</p>\n'
   '<div class="ei-info"><p>The only thing that ends the annual T2 obligation is formal '
   'dissolution. Until then the return is filed every year, with nil amounts where the '
   'corporation had no activity.</p></div>'),
  ('still-nil', 'When a Dormant Corporation Is Still Nil',
   tbl(('Situation in the tax year', 'Still a nil return'),
       [('No revenue and no expenses', 'Yes'),
        ('No bank account, or an account with no movement', 'Yes'),
        ('No employees and no payroll', 'Yes'),
        ('Share capital, cash or a shareholder loan on the books',
         'Yes, but GIFI schedules are required'),
        ('Any revenue, or any expense claimed', 'No'),
        ('Investment income, rental income, or a dividend paid or received', 'No')]),
   True),
  ('not-nil', 'When a Dormant Corporation Is Not Nil',
   '<p>' + NOT_NIL + '</p>\n'
   '<p>The distinction matters because a corporation can look dormant and still fall '
   'outside a nil return. A holding company sitting on an investment portfolio has no '
   'operations, no staff and no customers, and it is not nil, because the portfolio '
   'earns income that belongs on the return.</p>'),
  ('gifi', 'Share Capital, Shareholder Loans and GIFI',
   '<p>GIFI is the standard code set the Canada Revenue Agency uses for the balance '
   'sheet and income statement inside the T2. A corporation inactive all year with '
   'nothing at all to report may omit GIFI Schedules 100, 125 and 141.</p>\n'
   '<div class="ei-warn"><p>Any share capital, cash, shareholder loan, incorporation '
   'cost or bank charge makes those schedules required, even though the corporation had '
   'no activity. This is the single most common reason a return that looks nil is not '
   'filed correctly.</p></div>\n'
   '<p>See ' + a(A + 'do-i-need-financial-statements-for-a-nil-t2-return/',
                 'whether financial statements are needed for a nil T2 return') + '.</p>',
   True),
  ('accounts', 'GST/HST and Payroll Accounts Stay Open',
   '<p>An open GST/HST account or an open payroll account still needs nil filings of its '
   'own, or a closure using Form RC145. An inactive T2 does not close those accounts, '
   'and leaving them open while filing nothing against them creates a second trail of '
   'missed returns alongside the T2.</p>'),
  ('annual-returns', 'The Annual Return Is Separate',
   '<p>Filing the T2 does not satisfy a corporate annual return. The Ontario annual '
   'return has been filed through the Ontario Business Registry since October 2021, and '
   'a federal corporation files a $12.00 Corporations Canada annual return within 60 '
   'days of its anniversary date.</p>\n'
   '<p>The full set is covered in the guide to '
   + a(HUB + 'provincial-and-federal-annual-returns/',
       'provincial and federal annual returns') + '.</p>', True),
  ('deadlines', 'Deadlines for a Dormant Corporation',
   '<p>A T2 is due within six months of the fiscal year-end, dormant or not. Where a due '
   'date falls on a Saturday, a Sunday or a public holiday recognised by the Canada '
   'Revenue Agency, a return received the next business day is on time.</p>\n'
   '<p>Every fiscal year-end and its due date is listed on '
   + a(SITE + '/deadlines/', 'T2 filing deadlines') + '.</p>'),
  ('years-dormant', 'How Long a Corporation Can Stay Dormant',
   '<p>Indefinitely, so far as the Income Tax Act is concerned. There is no limit on how '
   'many consecutive years a corporation may report nil, and no point at which dormancy '
   'itself becomes a problem.</p>\n'
   '<p>What creates the problem is a dormant year that was never filed. The corporation '
   'stays dormant and compliant for as long as the returns keep arriving.</p>', True),
  ('unfiled', 'Dormant Years That Were Never Filed',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>Each year is a separate return with its own fiscal year-end and its own due date. '
   'There is no combined multi-year return and no reduced rate for filing several years '
   'together. The catch-up is covered in the guide to '
   + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
       'catching up on unfiled corporate tax returns') + '.</p>'),
  ('wind-up', 'Keeping It or Winding It Up',
   tbl(('Choice', 'What it costs each year', 'What it preserves'),
       [('Keep the corporation and file nil returns',
         PRICE + ', plus the annual return',
         'The corporate name, the business number and the incorporation date'),
        ('Dissolve the corporation',
         'Nothing after the final year',
         'Nothing; a new incorporation starts a new first tax year')])
   + '\n<p>A corporation kept dormant retains its incorporation date, which matters where '
   'the name or the trading history has value. Closing it is covered in the guide to '
   + a(HUB + 'final-t2-and-dissolution/', 'the final T2 and dissolution') + '.</p>', True),
 ],
 faq=[
  ('Does a Dormant Corporation Have to File a T2 Every Year?',
   'Yes. The return is due within six months of each fiscal year-end, every year, until '
   'the corporation is formally dissolved. Dormancy changes nothing about the obligation '
   'or the due date.'),
  ('Is There a Form That Tells the CRA My Corporation Is Dormant?',
   'No. There is no dormancy form and no way to pause the T2. The annual return is the '
   'only thing that reports the year, and it reports nil amounts where there was no '
   'activity.'),
  ('How Many Years Can a Corporation Stay Dormant?',
   'There is no limit. A corporation may report nil for as many consecutive years as it '
   'exists. What causes trouble is a dormant year left unfiled, not the dormancy.'),
  ('Is a Dormant Holding Company a Nil Filer?',
   'Not where it earns investment income. A holding corporation with investment income, '
   'a rental corporation and a corporation that paid or received a dividend are not nil, '
   'and are handled by Gondaliya CPA Professional Corporation at gondaliyacpa.ca at '
   '$350.00 plus HST per year.'),
  ('Does a Dormant Corporation Still Need GIFI Schedules?',
   'Where it has nothing at all to report, GIFI Schedules 100, 125 and 141 may be '
   'omitted. Any share capital, cash, shareholder loan, incorporation cost or bank '
   'charge makes them required, even with no activity in the year.'),
  ('Should I Dissolve a Dormant Corporation Instead?',
   'That depends on whether the name, the business number and the incorporation date are '
   'worth keeping. A dormant corporation costs the annual nil return and the annual '
   'return each year; a dissolved one costs nothing, and a later incorporation starts a '
   'new first tax year.'),
 ])

# ---------------------------------------------------------------------------
# Guide 2. /guides/catch-up-unfiled-corporate-tax-returns/
# 6(b): clusters F4 catch-up and unfiled slugs, F12, F13, 126 URLs, entry
# keyword "unfiled corporate tax returns", "highest contribution per visit".
# ---------------------------------------------------------------------------
G2 = dict(
 slug='catch-up-unfiled-corporate-tax-returns',
 title='Unfiled Corporate Tax Returns | Catch-Up Guide for Canada',
 h1='The Complete Guide to Catching Up on Unfiled Corporate Tax Returns',
 h1_pre='The Complete Guide to Catching Up on ',
 h1_span='Unfiled Corporate Tax Returns',
 eyebrow='Catch-Up Guide',
 meta=('How many years can be filed, which order to file them in, what a demand to '
       'file means, what an arbitrary assessment is, and what the catch-up costs.'),
 convert=(SITE + '/catch-up-nil-t2-filing/', 'Catch-Up Nil T2 Filing'),
 kids=['what-happens-if-i-dont-file-my-t2-for-five-years',
       'can-i-file-five-years-of-nil-t2-returns-at-once',
       'what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2',
       'can-i-file-a-nil-t2-late-without-a-penalty',
       'can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about',
       'what-happens-if-i-dont-file-a-nil-t2'],
 sections=[
  ('how-many-years', 'How Many Years Can Be Filed',
   '<p>Every year since incorporation that has not been filed is still outstanding and '
   'can still be filed. An unfiled tax year does not expire, and there is no cut-off '
   'after which the Canada Revenue Agency stops wanting the return.</p>\n'
   '<p>That cuts both ways. A year left unfiled stays open forever, which is the reason '
   'to file it; it also means nothing is lost by filing it late.</p>', True),
  ('one-per-year', 'Every Year Is a Separate Return',
   '<p>Five missed fiscal year-ends mean five separate returns. Each year keeps its own '
   'fiscal year-end, its own figures and its own T183CORP signature.</p>\n'
   '<div class="ei-info"><p>There is no combined multi-year return and no reduced rate '
   'for filing several years at once. The work is the same per year whether one year or '
   'ten are outstanding.</p></div>'),
  ('order', 'The Order to File Them In',
   '<p>Oldest first. Each return carries balances forward into the next, so the earliest '
   'outstanding year is prepared and transmitted before the one that follows it.</p>\n'
   '<p>Filing out of order produces returns whose opening balances do not match the '
   'closing balances of the year before, which is the kind of mismatch that draws a '
   'query rather than a clean assessment.</p>', True),
  ('find-outstanding', 'Finding Out Which Years Are Outstanding',
   '<p>The Canada Revenue Agency holds the record of which tax years it has received. '
   'Where the owner is unsure, the outstanding years are confirmed against the Agency '
   'record rather than reconstructed from memory.</p>\n'
   '<p>A corporation that was registered and then forgotten often has more outstanding '
   'years than its owner expects, because the first tax year began on the incorporation '
   'date rather than the day trading started.</p>'),
  ('year-end', 'Confirming the Fiscal Year-End First',
   '<p>The year-end on the return must match the Canada Revenue Agency record or the '
   'transmission is rejected. The Agency already holds a year-end taken from the '
   'incorporation record.</p>\n'
   '<div class="ei-warn"><p>A wrong year-end is the most common cause of a rejected '
   'transmission on a catch-up, because the owner remembers the date the business '
   'started rather than the date on the incorporation record.</p></div>', True),
  ('demand', 'A Demand to File',
   '<p>A demand to file is a formal written request from the Canada Revenue Agency for a '
   'return it has not received. It does not change the due date, which remains six '
   'months after the fiscal year-end, and it does not reduce what is owed on a true nil '
   'year, which is $0.00.</p>\n'
   '<p>What it does signal is that the year has moved from unnoticed to actively '
   'pursued. See '
   + a(A + 'what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2/',
       'what happens if a CRA demand to file is ignored') + '.</p>'),
  ('arbitrary', 'Arbitrary Assessments',
   '<p>An arbitrary assessment is an assessment the Canada Revenue Agency raises on its '
   'own figures when no return arrives, usually after a demand to file. It does not '
   'close the year the way a filed return does.</p>\n'
   '<div class="ei-info"><p>Filing the real return replaces the arbitrary figure with '
   "the corporation's own. An arbitrary assessment is not the end of the matter, and it "
   'is not a reason to leave the year unfiled.</p></div>', True),
  ('what-it-costs', 'What Unfiled Years Cost',
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>The exposure on a true nil year is not a percentage charge. It is the open year '
   'itself: the demand, the arbitrary assessment, the blocked clearance certificate and '
   'the blocked dissolution. For a non-resident-owned corporation it is also a daily '
   'amount, which is why those years are the most urgent to close.</p>'),
  ('fees', 'The Fee for Multiple Years',
   tbl(('Tax years outstanding', 'Fee at ' + PRICE),
       [('1 year', '$300.00 plus HST'), ('2 years', '$600.00 plus HST'),
        ('3 years', '$900.00 plus HST'), ('5 years', '$1,500.00 plus HST'),
        ('7 years', '$2,100.00 plus HST'), ('10 years', '$3,000.00 plus HST')])
   + '\n<p>One price per tax year, every year and every province.</p>', True),
  ('dissolution', 'Catching Up Before Dissolution',
   '<p>Every earlier year must already be filed before a corporation can be wound up '
   'cleanly. An unfiled year is an open year, and a clearance certificate cannot be '
   'issued while one is open.</p>\n'
   '<p>Owners who intend to close a corporation are the ones for whom the catch-up is '
   'urgent rather than optional. The sequence is set out in the guide to '
   + a(HUB + 'final-t2-and-dissolution/', 'the final T2 and dissolution') + '.</p>'),
  ('not-nil', 'When the Back Years Are Not Nil',
   '<p>' + NOT_NIL + '</p>\n'
   '<p>A catch-up often mixes the two. A corporation may have traded for two years, gone '
   'quiet for six, and have both kinds of year outstanding. The nil years are filed at '
   + PRICE + '; the active years are handled at gondaliyacpa.ca.</p>', True),
 ],
 faq=[
  ('How Far Back Can I File Unfiled T2 Returns?',
   'Every year since incorporation that has not been filed is still outstanding and can '
   'still be filed. An unfiled tax year does not expire.'),
  ('Can Several Years Be Filed at the Same Time?',
   'Yes. They are prepared and transmitted in one pass, oldest first, but each year is '
   'a separate return with its own fiscal year-end, its own figures and its own '
   'T183CORP signature.'),
  ('Is There a Discount for Filing Several Years?',
   'No. The fee is ' + PRICE + ', and the work is the same per year whether one year or '
   'ten are outstanding.'),
  ('What Happens if the CRA Already Assessed the Year Arbitrarily?',
   'Filing the real return replaces the arbitrary figure with the corporation&rsquo;s own. '
   'An arbitrary assessment does not close the year the way a filed return does, and it '
   'is not a reason to leave the year unfiled.'),
  ('Will Catching Up Trigger an Audit?',
   'Filing an outstanding return is the ordinary way to close an open year, and a nil '
   'return reports nil amounts. What draws attention is the open year itself, along with '
   'the demand and the arbitrary assessment that follow it.'),
  ('Which Year Is Filed First?',
   'The earliest outstanding one. Each return carries balances forward into the next, so '
   'filing out of order produces opening balances that do not match the closing balances '
   'of the year before.'),
 ])

# ---------------------------------------------------------------------------
# Guide 3. /guides/final-t2-and-dissolution/
# 6(b): clusters F4 final slugs, F14, F12, 66 URLs, entry keyword "final t2
# before dissolution", clearance certificate angle.
# ---------------------------------------------------------------------------
G3 = dict(
 slug='final-t2-and-dissolution',
 title='Final T2 and Dissolution | Complete Guide for Canadian Corporations',
 h1='The Complete Guide to the Final T2 and Dissolution',
 h1_pre='The Complete Guide to the ',
 h1_span='Final T2 and Dissolution',
 eyebrow='Dissolution Guide',
 meta=('When the final T2 is due, what period it covers, why a clearance certificate '
       'matters, and everything that must be filed before a corporation can close.'),
 convert=(SITE + '/final-t2-before-dissolution/', 'Final T2 Before Dissolution'),
 kids=['what-happens-if-i-dont-file-a-t2-before-dissolving-my-corporation',
       'what-happens-if-i-dont-file-t2-returns-after-my-corporation-is-dissolved',
       'do-i-need-to-file-a-t2-for-the-year-my-corporation-was-dissolved',
       'can-i-dissolve-my-corporation-with-unfiled-t2-returns',
       'can-i-still-file-a-t2-after-my-corporation-was-dissolved',
       'what-happens-if-i-dont-file-a-nil-t2'],
 sections=[
  ('what-final', 'What the Final T2 Is',
   '<p>The final T2 is the last corporate return a corporation files. It is the same '
   'form as every other year, covering the period that ends on the dissolution date '
   'rather than on the usual fiscal year-end.</p>\n'
   '<p>Filing it is what closes the corporate tax account. A corporation that is struck '
   'from a registry without one leaves an open year behind it.</p>', True),
  ('period', 'The Period the Final Return Covers',
   '<p>From the start of the fiscal year in which dissolution happened, up to and '
   'including the dissolution date. Nothing after that date belongs on it, because the '
   'corporation no longer exists.</p>\n'
   '<div class="ei-info"><p>Where the corporation had no activity in that closing '
   'period, the final return is a nil return and is filed at ' + PRICE + '.</p></div>'),
  ('short-year', 'The Closing Short Tax Year',
   '<p>The closing period is almost always shorter than twelve months, which makes it a '
   'short tax year. The fiscal year-end on the final return is the dissolution date, not '
   'the year-end the corporation used before.</p>\n'
   '<p>Getting that date wrong is the usual cause of a rejected final transmission, '
   'because the Canada Revenue Agency matches it against the dissolution record.</p>',
   True),
  ('due-date', 'When the Final T2 Is Due',
   tbl(('Return', 'Due'),
       [('Every ordinary T2', 'Within 6 months of the fiscal year-end'),
        ('The final T2', 'Within 6 months of the dissolution date'),
        ('Earlier unfiled years', 'Already overdue; filed as a catch-up')])
   + '\n<p>Every fiscal year-end and its due date is listed on '
   + a(SITE + '/deadlines/', 'T2 filing deadlines') + '.</p>'),
  ('earlier-years', 'Earlier Years Must Already Be Filed',
   '<p>A final return does not sweep up the years before it. Each earlier year is a '
   'separate return with its own fiscal year-end and its own due date, and each stays '
   'outstanding until it is filed.</p>\n'
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>Where several years are outstanding, the catch-up runs first, oldest to newest, '
   'and the final return is last. See '
   + a(HUB + 'catch-up-unfiled-corporate-tax-returns/',
       'catching up on unfiled corporate tax returns') + '.</p>', True),
  ('clearance', 'The Clearance Certificate',
   '<p>A clearance certificate is the confirmation that a corporation has no outstanding '
   'amounts before it is wound up. It cannot be issued while any tax year is open, '
   'because an unfiled year is by definition an unresolved one.</p>\n'
   '<p>Directors who distribute the remaining property without one take on a personal '
   'exposure for whatever later turns out to be owed. That is the practical reason the '
   'returns come before the distribution.</p>'),
  ('registry', 'The Registry and the Agency Are Separate',
   '<p>A corporate registry and the Canada Revenue Agency do not share a filing status. '
   'A registry may strike a corporation for a missed annual return while its tax years '
   'remain outstanding, and the Agency is not told that the corporation has gone.</p>\n'
   '<div class="ei-warn"><p>Being struck from a registry is not dissolution for tax '
   'purposes and does not cancel a single outstanding return.</p></div>', True),
  ('after-dissolution', 'Filing After Dissolution',
   '<p>A dissolved corporation can still file, and still has to. The final return is due '
   'within six months of the dissolution date, and earlier unfiled years can be filed '
   'afterwards.</p>\n'
   '<p>A dissolved corporation with an open year can also still be reassessed, so the '
   'returns are what finish the file rather than the dissolution date. See '
   + a(A + 'can-i-still-file-a-t2-after-my-corporation-was-dissolved/',
       'whether a T2 can still be filed after dissolution') + '.</p>'),
  ('accounts', 'Closing the GST/HST and Payroll Accounts',
   '<p>An open GST/HST account or an open payroll account still needs nil filings of its '
   'own, or a closure using Form RC145. An inactive or final T2 does not close those '
   'accounts.</p>\n'
   '<p>A corporation wound up with those accounts left open keeps generating obligations '
   'against a business number whose owner has stopped looking at the mail.</p>', True),
  ('order', 'The Order of Operations',
   tbl(('Step', 'What happens'),
       [('1', 'Confirm the fiscal year-end against the Canada Revenue Agency record'),
        ('2', 'File every outstanding earlier year, oldest first'),
        ('3', 'Close the GST/HST and payroll accounts, or file them nil'),
        ('4', 'File the final T2 for the period ending on the dissolution date'),
        ('5', 'Request the clearance certificate'),
        ('6', 'Distribute the remaining property and complete the registry filing')])),
  ('not-nil', 'When the Final Year Is Not Nil',
   '<p>' + NOT_NIL + '</p>\n'
   '<p>A winding-up year is often not nil even where the corporation had stopped '
   'trading, because disposing of the remaining assets can itself produce income. Where '
   'that is the case the year is handled at gondaliyacpa.ca rather than here.</p>', True),
 ],
 faq=[
  ('When Is the Final T2 Due?',
   'Within six months of the dissolution date. It covers the period from the start of '
   'that fiscal year up to and including the dissolution date.'),
  ('Can I Dissolve With Unfiled Years Outstanding?',
   'A registry may strike the corporation, but the unfiled years stay due and a '
   'clearance certificate cannot be issued until every return is filed. Dissolving '
   'first and filing later leaves a closed corporation with an open tax account.'),
  ('Does Dissolution Cancel Earlier Unfiled Returns?',
   'No. A final return does not sweep up the years before it, and a dissolved '
   'corporation with an open year can still be reassessed.'),
  ('What Is a Clearance Certificate For?',
   'It confirms the corporation has no outstanding amounts before it is wound up. '
   'Directors who distribute the remaining property without one take on a personal '
   'exposure for whatever later turns out to be owed.'),
  ('Is Being Struck From the Registry the Same as Dissolution?',
   'Not for tax purposes. A registry and the Canada Revenue Agency do not share a filing '
   'status, and a corporation struck for a missed annual return still owes every '
   'outstanding T2.'),
  ('Is the Final Return Filed at the Same Price?',
   'Where the closing period had no activity, the final return is a nil return and is '
   'filed at ' + PRICE + '.'),
 ])

# ---------------------------------------------------------------------------
# Guide 4. /guides/t2-short-eligibility/
# 6(b): clusters F2, F5, F4 t2-short slugs, 223 URLs, entry keyword "t2 short".
# 6(b) names /tools/t2-short-eligibility-checker/ as the conversion step; F2 has
# 0 of 150 tools live, so /t2-short-filing/ stands in. Logged.
# ---------------------------------------------------------------------------
G4 = dict(
 slug='t2-short-eligibility',
 title='T2 Short | Eligibility Guide for Canadian Corporations',
 h1='The Complete Guide to T2 Short Eligibility',
 h1_pre='The Complete Guide to ',
 h1_span='T2 Short Eligibility',
 eyebrow='T2 Short Guide',
 meta=('The eight conditions for the T2 Short, what disqualifies a corporation, how '
       'it differs from the full T2, and which schedules are still required.'),
 convert=(SITE + '/t2-short-filing/', 'T2 Short Filing'),
 kids=['do-i-need-financial-statements-for-a-nil-t2-return',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'can-i-file-a-nil-t2-myself-without-an-accountant',
       'do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account'],
 sections=[
  ('what-it-is', 'What the T2 Short Is',
   '<p>The T2 Short is a two-page version of the corporate return. It is the same filing '
   'obligation discharged on a shorter form, available only to a corporation that meets '
   'every one of eight conditions.</p>\n'
   '<p>It is not a different kind of return and not a lighter obligation. A T2 Short is '
   'a filed T2.</p>', True),
  ('eight-conditions', 'The Eight Conditions',
   tbl(('Condition', 'Requirement'),
       [('Corporation type', 'Canadian-controlled private corporation'),
        ('Net income', 'Nil net income or a loss for the year'),
        ('Permanent establishments', 'One only'),
        ('Taxable dividends', 'None paid and none received'),
        ('Currency', 'Canadian'),
        ('Refundable credits', 'None claimed'),
        ('Ontario transitional debit', 'None'),
        ('Section 34.2 amount', 'None')])
   + '\n<div class="ei-warn"><p>All eight must hold. Failing any one of them puts the '
   'corporation on the full T2 for that year.</p></div>'),
  ('ccpc', 'The Canadian-Controlled Private Corporation Test',
   '<p>The corporation must be a Canadian-controlled private corporation throughout the '
   'tax year. A corporation controlled by non-residents is not one, which is why a '
   'non-resident-owned corporation files the full return.</p>\n'
   '<p>Control is tested on the facts rather than on where the directors happen to live '
   'in a given month, and a change in control during the year affects the test.</p>',
   True),
  ('nil-or-loss', 'Nil Net Income or a Loss',
   '<p>Net income for the year must be nil or negative. A corporation with no activity '
   'at all has nil net income and meets this condition.</p>\n'
   '<p>A corporation with a loss also meets it, which is why the T2 Short is not limited '
   'to dormant corporations. A trading corporation that lost money in the year can '
   'qualify on this condition, though it will usually fail another one.</p>'),
  ('one-pe', 'One Permanent Establishment',
   '<p>The corporation must have a single permanent establishment, in one province or '
   'territory. A corporation with establishments in two provinces allocates income '
   'between them, and that allocation does not fit on the short form.</p>\n'
   '<div class="ei-info"><p>A dormant corporation generally has one establishment, being '
   "its registered office. Where that office is the only Canadian address, the condition "
   'is met.</p></div>', True),
  ('dividends', 'No Taxable Dividends Paid or Received',
   '<p>No taxable dividend may have been paid and none received during the year. A '
   'single dividend in either direction puts the corporation on the full T2.</p>\n'
   '<p>It also takes the corporation outside a nil return altogether. '
   + NOT_NIL + '</p>'),
  ('currency-credits', 'Canadian Currency and No Refundable Credits',
   '<p>The return must be reported in Canadian dollars, and no refundable tax credit may '
   'be claimed for the year.</p>\n'
   '<p>A corporation that functions in United States dollars files the full return. A '
   'corporation claiming a refundable credit does too, because the credit calculation '
   'has no place on the short form.</p>', True),
  ('ontario-342', 'Ontario Transitional Debit and Section 34.2',
   '<p>Two residual conditions rule out particular histories. There must be no Ontario '
   'transitional tax debit, and no amount arising under section 34.2 of the Income Tax '
   'Act, which deals with a corporate partner and a partnership whose fiscal period '
   'differs from the corporation&rsquo;s.</p>\n'
   '<p>Neither applies to an ordinary dormant corporation. Both are worth checking on a '
   'corporation that once traded through a partnership.</p>'),
  ('disqualifies', 'What Disqualifies a Corporation',
   tbl(('Fact in the tax year', 'Effect'),
       [('Controlled by non-residents', 'Full T2'),
        ('Positive net income', 'Full T2'),
        ('Establishments in two or more provinces', 'Full T2'),
        ('Any taxable dividend paid or received', 'Full T2, and not a nil return'),
        ('Reporting currency other than Canadian', 'Full T2'),
        ('Any refundable credit claimed', 'Full T2'),
        ('Ontario transitional tax debit', 'Full T2'),
        ('A section 34.2 amount', 'Full T2')]), True),
  ('vs-full', 'T2 Short Against the Full T2',
   tbl(('', 'T2 Short', 'Full T2'),
       [('Length', 'Two pages', 'Eight pages plus schedules'),
        ('Who may use it', 'A CCPC meeting all eight conditions', 'Any corporation'),
        ('GIFI schedules', 'Required where there is anything to report',
         'Required where there is anything to report'),
        ('Schedule 24 on a first return', 'Required', 'Required'),
        ('Electronic filing', 'Mandatory for virtually all corporations',
         'Mandatory for virtually all corporations'),
        ('Included in our fee', 'Yes, where the corporation qualifies',
         'Yes, where the corporation does not')])),
  ('schedules', 'Schedules Still Required',
   '<p>The short form shortens the return, not the schedules. GIFI Schedules 100, 125 '
   'and 141 are required wherever there is anything to report, Schedule 24 is required '
   'on the first return after incorporation, and Schedule 50 is required for every '
   'shareholder holding 10% or more.</p>\n'
   '<div class="ei-warn"><p>Any share capital, cash, shareholder loan, incorporation '
   'cost or bank charge makes the GIFI schedules required, even on a T2 Short and even '
   'with no activity in the year.</p></div>\n'
   '<p>See ' + a(A + 'do-i-need-financial-statements-for-a-nil-t2-return/',
                 'whether financial statements are needed for a nil T2 return') + '.</p>',
   True),
 ],
 faq=[
  ('Is the T2 Short the Same as a Nil Return?',
   'No. A nil return describes a year with no activity; the T2 Short describes a form. '
   'Most nil years qualify for the short form, but a corporation with a loss and real '
   'trading activity can also qualify, and a dormant corporation that fails one of the '
   'eight conditions cannot.'),
  ('Who Decides Which Form Is Used?',
   'The eight conditions decide it. Where the corporation meets all of them the T2 Short '
   'is filed, and where it fails any one the full T2 is filed. Both are included in the '
   'fee of ' + PRICE + '.'),
  ('Can a Non-Resident-Owned Corporation File the T2 Short?',
   'No. The first condition requires a Canadian-controlled private corporation, and a '
   'corporation controlled by non-residents is not one.'),
  ('Does the T2 Short Skip the GIFI Schedules?',
   'No. The short form shortens the return, not the schedules. GIFI Schedules 100, 125 '
   'and 141 are required wherever there is anything at all to report.'),
  ('What Is a Permanent Establishment for This Test?',
   'A fixed place through which the corporation carries on business, which for a dormant '
   'corporation is generally its registered office. The condition requires exactly one, '
   'in one province or territory.'),
  ('Does Filing the T2 Short Change the Deadline?',
   'No. The return is due within six months of the fiscal year-end whichever form is '
   'used.'),
 ])

# ---------------------------------------------------------------------------
# Guide 5. /guides/provincial-and-federal-annual-returns/
# 6(b): clusters F4 jurisdiction pages, F14, 179 URLs, entry keyword "ontario
# annual return". 6(b) note: "Covers AT1, CO-17, Ontario Business Registry,
# $12.00 federal annual return".
#
# The plan groups AT1 and CO-17 with the annual returns. They are not the same
# thing: an annual return is a registry filing, while AT1 and CO-17 are separate
# provincial income tax returns. Both are covered, and the distinction is drawn
# rather than blurred, because blurring it is what makes owners miss one.
# ---------------------------------------------------------------------------
G5 = dict(
 slug='provincial-and-federal-annual-returns',
 title='Provincial and Federal Annual Returns | Guide for Canadian Corporations',
 h1='The Complete Guide to Provincial and Federal Annual Returns',
 h1_pre='The Complete Guide to ',
 h1_span='Provincial and Federal Annual Returns',
 eyebrow='Annual Return Guide',
 meta=('The Ontario annual return, the $12.00 Corporations Canada annual return, '
       'Alberta AT1 and Quebec CO-17, and why the T2 covers none of them.'),
 convert=(SITE + '/nil-t2-filing-ontario/', 'Nil T2 Filing in Ontario'),
 kids=['do-i-need-a-business-number-to-file-a-nil-t2',
       'do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
       'what-happens-if-i-dont-report-a-dormant-corporation-to-cra',
       'do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
       'do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
       'what-happens-if-i-dont-file-a-nil-t2-for-a-numbered-company'],
 sections=[
  ('not-the-t2', 'The Annual Return Is Not the T2',
   '<p>Two different filings are called a return, and confusing them is the most common '
   'compliance gap a dormant corporation has. The T2 is a tax return filed with the '
   'Canada Revenue Agency. An annual return is a registry filing that confirms who the '
   'directors are and where the registered office is.</p>\n'
   '<p>Filing the T2 does not satisfy an annual return, and filing an annual return does '
   'not satisfy the T2. A corporation needs both, every year, for as long as it '
   'exists.</p>', True),
  ('ontario', 'The Ontario Annual Return',
   '<p>An Ontario corporation files an annual return confirming its registered office '
   'address, its directors and its officers. It carries no tax and no payment.</p>\n'
   '<div class="ei-warn"><p>Until 2021 this was filed alongside the T2. Since October '
   '2021 it is filed through the Ontario Business Registry instead, and a corporation '
   'that has not looked at the rules since then is probably not filing it.</p></div>'),
  ('obr', 'Filing Through the Ontario Business Registry',
   '<p>The Ontario Business Registry is the provincial system through which the annual '
   'return, address changes and director changes are filed. A corporation needs its '
   'Ontario corporation number and its registry access to use it.</p>\n'
   '<p>Because the filing moved out of the T2, nothing in the corporate tax return now '
   'prompts an owner to do it. The prompt has to come from the owner or the adviser.</p>',
   True),
  ('federal', 'The Corporations Canada Annual Return',
   '<p>A federal corporation files an annual return with Corporations Canada for '
   '$12.00. It confirms the same kind of information: directors, registered office and '
   'corporate status.</p>\n'
   '<div class="ei-info"><p>A federally incorporated corporation operating in Ontario '
   'files both: the $12.00 Corporations Canada annual return and an Ontario filing. '
   'Federal incorporation does not remove the provincial obligation.</p></div>'),
  ('anniversary', 'The 60-Day Anniversary Window',
   '<p>The Corporations Canada annual return is due within 60 days of the anniversary '
   'date of incorporation, amalgamation or continuance. That date has nothing to do with '
   'the fiscal year-end that governs the T2.</p>\n'
   + tbl(('Filing', 'Tied to', 'Due'),
         [('T2 corporate tax return', 'The fiscal year-end', 'Within 6 months'),
          ('Corporations Canada annual return', 'The anniversary date',
           'Within 60 days'),
          ('Ontario annual return', 'The tax year-end',
           'Filed through the Ontario Business Registry')]), True),
  ('alberta', 'Alberta AT1',
   '<p>Alberta administers its own corporate income tax. An Alberta corporation files '
   'the AT1, a separate provincial income tax return, in addition to the federal T2.</p>\n'
   '<p>It is not an annual return and it is not covered by the T2. An Alberta corporation '
   'with a nil year has a nil AT1 to deal with as well as a nil T2.</p>'),
  ('quebec', 'Quebec CO-17',
   '<p>Revenu Qu&eacute;bec administers Quebec corporate income tax. A Quebec '
   'corporation files the CO-17, a separate provincial income tax return, in addition to '
   'the federal T2.</p>\n'
   '<div class="ei-warn"><p>The CO-17 is a separate return, not a schedule of the T2. A '
   'Quebec corporation that files only the T2 has filed half of what it owes.</p></div>',
   True),
  ('other-provinces', 'The Other Provinces and Territories',
   '<p>Everywhere other than Alberta and Quebec, provincial and territorial corporate '
   'income tax is collected through the federal T2, so there is no second income tax '
   'return to file.</p>\n'
   + tbl(('Jurisdiction', 'Separate corporate income tax return',
          'Registry annual return'),
         [('Alberta', 'Yes, the AT1', 'Yes'),
          ('Quebec', 'Yes, the CO-17', 'Yes'),
          ('Ontario', 'No, collected through the T2',
           'Yes, through the Ontario Business Registry'),
          ('Every other province and territory', 'No, collected through the T2',
           'Yes, with that jurisdiction&rsquo;s registry')])),
  ('dormant', 'A Dormant Corporation Still Files Them',
   '<p>An annual return is not a tax filing, so having no income does not excuse it. A '
   'dormant corporation confirms its directors and its registered office every year in '
   'exactly the way an active one does.</p>\n'
   '<p>The same holds for the AT1 and the CO-17 where the corporation is in Alberta or '
   'Quebec. A nil year still produces a return in each place that wants one. See the '
   'guide to '
   + a(HUB + 'dormant-and-inactive-corporations/',
       'dormant and inactive corporations') + '.</p>', True),
  ('missed', 'What a Missed Annual Return Causes',
   '<p>A missed annual return does not create tax. It creates a registry record that is '
   'out of date, and after enough missed years it creates a corporation the registry '
   'treats as abandoned.</p>\n'
   '<div class="ei-info"><p>The two trails are independent. A corporation can be fully '
   'current on its T2 filings and still be struck from its registry, and it can be in '
   'good standing at the registry while owing ten years of T2 returns.</p></div>'),
  ('struck', 'Being Struck From the Registry',
   '<p>Where annual returns go unfiled for long enough, the registry may dissolve or '
   'strike the corporation. That is not dissolution for tax purposes, and it cancels no '
   'outstanding T2 return.</p>\n'
   '<p>A corporation struck from a registry with unfiled tax years is in the worst of '
   'both positions: it cannot trade and it still owes returns. Closing it properly is '
   'covered in the guide to '
   + a(HUB + 'final-t2-and-dissolution/', 'the final T2 and dissolution') + '.</p>',
   True),
 ],
 faq=[
  ('Does Filing My T2 Cover the Ontario Annual Return?',
   'No. The Ontario annual return has been filed through the Ontario Business Registry '
   'since October 2021, separately from the T2. Before that it travelled with the '
   'corporate tax return, which is why many owners believe it still does.'),
  ('What Does the Corporations Canada Annual Return Cost?',
   '$12.00, filed within 60 days of the anniversary date of incorporation, '
   'amalgamation or continuance. That date is unrelated to the fiscal year-end.'),
  ('Does a Dormant Corporation File an Annual Return?',
   'Yes. An annual return confirms directors and the registered office rather than '
   'income, so having no activity does not excuse it.'),
  ('Is the AT1 or the CO-17 Part of the T2?',
   'No. Alberta and Quebec administer their own corporate income tax, so an Alberta '
   'corporation files the AT1 and a Quebec corporation files the CO-17 in addition to '
   'the federal T2. Everywhere else provincial corporate income tax is collected '
   'through the T2.'),
  ('Do I File Both Federal and Provincial Annual Returns?',
   'A federal corporation files the $12.00 Corporations Canada annual return and also '
   'files with the registry of each province where it is registered. Federal '
   'incorporation does not remove the provincial obligation.'),
  ('Is the Annual Return Included in Your Fee?',
   'No. Our fee of ' + PRICE + ' covers the nil T2 corporate tax return. Registry '
   'annual returns, the Alberta AT1 and the Quebec CO-17 are separate filings and are '
   'not included.'),
 ])

# ---------------------------------------------------------------------------
# Guide 6. /guides/t183corp-signing-and-transmission/
# 6(b): clusters F15, F5, 69 URLs, entry keyword "t183corp", "Trust pillar, no
# price in the H1". 6(b) names /security/ as the conversion step; F15 is not
# built, so /sharad-gondaliya-cpa/ stands in. Logged.
# Hard rule 2 throughout: T183CORP, never T183.
# ---------------------------------------------------------------------------
G6 = dict(
 slug='t183corp-signing-and-transmission',
 title='Form T183CORP | Signing and Transmission Guide',
 h1='The Complete Guide to Form T183CORP Signing and Transmission',
 h1_pre='The Complete Guide to ',
 h1_span='Form T183CORP',
 h1_post=' Signing and Transmission',
 eyebrow='T183CORP Guide',
 no_price_h1=True,
 meta=('What Form T183CORP authorises, who may sign it, when it must be signed, how '
       'it is e-signed, how long it is kept, and what EFILE transmission involves.'),
 convert=(SITE + '/sharad-gondaliya-cpa/', 'Sharad Gondaliya, CPA'),
 kids=['can-i-file-a-nil-t2-myself-without-an-accountant',
       'do-i-need-a-business-number-to-file-a-nil-t2',
       'do-i-need-financial-statements-for-a-nil-t2-return',
       'can-i-file-five-years-of-nil-t2-returns-at-once',
       'do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
       'what-happens-if-i-dont-file-a-nil-t2'],
 sections=[
  ('what-it-is', 'What Form T183CORP Is',
   '<p>Form T183CORP is the authorisation that lets a registered EFILE electronic filer '
   'transmit a corporate return on behalf of a corporation. It records that the '
   'corporation has seen the return and agreed that it may be sent.</p>\n'
   '<p>It is not the return and it is not a tax form in its own right. It is the consent '
   'that stands behind the transmission.</p>', True),
  ('who-signs', 'Who May Sign It',
   '<p>An authorized signing officer of the corporation signs it. That is a director or '
   'an officer with authority to bind the corporation, not an employee, not a '
   'bookkeeper and not the accountant preparing the return.</p>\n'
   '<div class="ei-info"><p>On a single-director corporation this is almost always the '
   'sole director. On a corporation with several directors, any one of them with signing '
   'authority may sign.</p></div>'),
  ('when', 'When It Must Be Signed',
   '<p>Before the return is transmitted, never after. The sequence is fixed: the return '
   'is prepared, the signing officer reviews it, the form is signed, and only then is '
   'the return sent.</p>\n'
   '<p>A form signed after transmission does not authorise what has already '
   'happened.</p>', True),
  ('timestamp', 'The Date and Timestamp',
   tbl(('Element', 'Requirement'),
       [('Date', 'The actual date of signature'),
        ('Time', 'An HH:MM:SS timestamp'),
        ('Date integrity', 'The date is never backdated'),
        ('Order', 'The timestamp precedes the transmission')])
   + '\n<p>The timestamp exists so the order of events can be proved. A form whose '
   'timestamp falls after the transmission it authorises is a record of a process run '
   'in the wrong order.</p>'),
  ('e-signing', 'How It May Be E-Signed',
   '<p>Form T183CORP may be e-signed. We use an access-controlled secure portal with a '
   'single-use link, so the form is opened and signed by the person it was sent to '
   'rather than by whoever receives a forwarded email.</p>\n'
   '<p>A scanned wet signature is equally valid. The portal exists because it is faster '
   'and because it produces the timestamp automatically.</p>', True),
  ('retention', 'Retention for Six Years',
   '<p>The signed form is kept by the firm for six years. The corporation does not have '
   'to keep its own copy for the filing to stand, though keeping one is sensible.</p>\n'
   '<p>Six years is the retention period that runs alongside the corporate books and '
   'records the Canada Revenue Agency expects a corporation to hold.</p>'),
  ('not-sent', 'It Is Not Sent to the Agency',
   '<p>Form T183CORP is not transmitted with the return and is not filed anywhere. It is '
   'held by the electronic filer and produced only if the Canada Revenue Agency asks '
   'for it.</p>\n'
   '<div class="ei-warn"><p>Because it is never sent, nothing in the Agency&rsquo;s '
   'records shows whether a valid form exists. The discipline around signing it properly '
   'rests entirely with the filer.</p></div>', True),
  ('efile', 'What EFILE Transmission Involves',
   '<p>' + EFILE_PILLAR + '</p>\n'
   '<p>Transmission sends the completed return to the Canada Revenue Agency '
   'electronically. The Agency responds with either an acceptance or a rejection, and '
   'the CRA confirmation is emailed to the corporation within 3 business days.</p>'),
  ('not-authorization', 'T183CORP Is Not Representative Authorization',
   '<p>Two separate things are often taken for one. Form T183CORP authorises a single '
   'transmission. Representative authorization gives an adviser ongoing access to a '
   "corporation's account with the Canada Revenue Agency.</p>\n"
   + tbl(('', 'Form T183CORP', 'Representative authorization'),
         [('What it permits', 'One transmission of one return',
           'Ongoing access to the account'),
          ('Required to file', 'Yes', 'No'),
          ('Sent to the Agency', 'No, unless requested', 'Yes'),
          ('When it matters', 'Before transmission', 'After filing')])
   + '\n<p>An EFILE number plus a signed T183CORP are enough to transmit. '
   'Representative authorization is optional and post-filing only.</p>', True),
  ('mandatory', 'Mandatory Electronic Filing',
   '<p>For tax years starting after 2023, e-filing is mandatory for virtually all '
   'corporations. A paper T2 draws a $1,000.00 penalty plus a $100.00 per-return '
   'preparer penalty.</p>\n'
   '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
   '<p>Because transmission is now the normal route rather than the optional one, '
   'Form T183CORP is part of virtually every corporate filing.</p>'),
  ('rejected', 'If a Transmission Is Rejected',
   '<p>The Canada Revenue Agency rejects a transmission where the return does not match '
   'its records. The most common cause is a fiscal year-end that differs from the one '
   'the Agency holds from the incorporation record.</p>\n'
   '<div class="ei-info"><p>One corrected transmission is included in the fee where the '
   'Agency rejects the first one. A rejection is not a failed filing; it is a filing '
   'that has not landed yet.</p></div>', True),
 ],
 faq=[
  ('Who Is an Authorized Signing Officer?',
   'A director or an officer with authority to bind the corporation. Not an employee, '
   'not a bookkeeper and not the accountant who prepared the return.'),
  ('Can Form T183CORP Be Signed Electronically?',
   'Yes, through an access-controlled secure portal with a single-use link. A scanned '
   'wet signature is equally valid.'),
  ('Does the CRA Receive Form T183CORP?',
   'No, not unless it asks for it. The form is held by the electronic filer for six '
   'years and is never transmitted with the return.'),
  ('What Happens if the Form Is Signed After Transmission?',
   'The sequence is fixed: the form is signed before the return is sent, never after. A '
   'form signed afterwards does not authorise what has already happened, and the date is '
   'never backdated to make it appear that it did.'),
  ('Do I Need to Give You Representative Access to My CRA Account?',
   'No. An EFILE number plus a signed T183CORP are enough to transmit. Representative '
   'authorization is optional and post-filing only.'),
  ('How Many Forms Are Needed for a Multi-Year Catch-Up?',
   'One for each tax year, because each year is a separate return with its own '
   'transmission. Five outstanding years means five signatures.'),
 ])

GUIDES = [G1, G2, G3, G4, G5, G6]

# ---------------------------------------------------------------------------
# Render. Structure mirrors the pillar exactly: hero, update date plus the
# 12-row contents block (the line 1217 gate), 12 anchored sections with one
# inline CTA after the fourth, the FAQ and child lists, the bottom CTA, then
# the Article schema from line 1487.
# ---------------------------------------------------------------------------
KID_TITLES = {}
for _p in ('f5-manifest.json',):
    _f = os.path.join(HERE, '..', 'f5', _p)
    for r in json.load(open(_f, encoding='utf-8')):
        # the H1 is the question; cnf_question_text holds it verbatim
        KID_TITLES[r['slug']] = r['meta']['cnf_question_text']

def render(g):
    url = HUB + g['slug'] + '/'
    # section tuples are (key, title, body) or (key, title, body, alt); the alt
    # flag is omitted on every other section, so normalise to four fields.
    sections = [tuple(t) + ((False,) if len(t) == 3 else ()) for t in g['sections']]
    sections.append((
        'fee', g.get('fee_title', 'What the Fee Covers'),
        '<p>' + g.get('fee_lead', 'The fee is ' + PRICE + ', covering one nil T2 return '
                      'for one corporation for one tax year:') + '</p>\n'
        + tbl(('Included', 'Detail'), FEE_ROWS)
        + ('\n<div class="ei-warn"><p>' + g['fee_note'] + '</p></div>'
           if g.get('fee_note') else '')
        + '\n<p>See the full '
        + a(SITE + '/pricing/nil-t2-filing-cost/', 'nil T2 filing cost') + '.</p>',
        False))
    assert len(sections) == 12, '%s has %d sections' % (g['slug'], len(sections))

    parts = [CSS]

    # hero
    h1_html = (g.get('h1_pre', '') + '<span>' + g['h1_span'] + '</span>'
               + g.get('h1_post', ''))
    sub = g['meta'] if g.get('no_price_h1') else g['meta'] + ' Nil T2 filing is ' + PRICE + '.'
    parts.append(
     '<div class="ei-hero"><div class="ei-hero-inner">'
     '<span class="ei-hero-eyebrow">' + g['eyebrow'] + '</span>'
     '<h1>' + h1_html + '</h1>'
     '<p class="ei-hero-sub">' + sub + '</p>'
     '<p class="ei-hero-by">' + BYLINE + '</p>'
     '<div class="ei-hero-btns"><a class="ei-btn-blue" href="' + FORM + '">'
     'Start Nil T2 Filing NOW</a>'
     '<a class="ei-btn-blue" style="background:transparent;border:2px solid '
     'rgba(255,255,255,0.4)" href="' + g['convert'][0] + '">' + g['convert'][1] + '</a>'
     '</div></div></div>\n')

    # update date + the 12-row contents block
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
            parts.append(cta_inline(
                'Nil T2 Filing, ' + PRICE,
                'One price for every year and every province. CPA reviewed and '
                'transmitted electronically.'))

    # FAQ, child questions, sibling guides
    faq_items = '\n'.join(
     '<details><summary>%s</summary><div class="ei-faq-a"><p>%s</p></div></details>'
     % (q, ans) for q, ans in g['faq'])
    kid_links = '\n'.join('<li>%s</li>' % a(A + s + '/', KID_TITLES[s])
                          for s in g['kids'])
    # 6(g) line 1528: all eleven others, from the shared registry, so these
    # six stay in step as later guides are added.
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

    # bottom CTA
    parts.append(
     '<div class="ei-cta-bottom"><div class="ei-wrap">'
     '<h2>' + ('Start Your Nil T2 Filing' if g.get('no_price_h1')
               else 'Nil T2 Filing, ' + PRICE) + '</h2>'
     '<p>Type your corporation name, pick your unfiled years, pay, and sign Form '
     'T183CORP on a secure screen. Your CRA confirmation is emailed within 3 business '
     'days.</p>'
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

G5['fee_title'] = 'What Our Fee Covers and What It Does Not'
G5['fee_note'] = ('Registry annual returns, the Alberta AT1 and the Quebec CO-17 are '
                  'separate filings and are not included in the fee. The fee covers the '
                  'federal nil T2 corporate tax return.')

records = []
for g in GUIDES:
    html, url = render(g)
    records.append(dict(slug=g['slug'], title=g['title'], h1=g['h1'],
                        meta_description=g['meta'], url=url, content=html,
                        toc=[t[1] for t in g['sections']] + ['What the Fee Covers'],
                        meta={'cnf_last_verified_et': ISO}))
    open(os.path.join(HERE, g['slug'] + '.html'), 'w', encoding='utf-8').write(html)

json.dump(records, open(os.path.join(HERE, 'f9-batch2-manifest.json'), 'w'),
          ensure_ascii=False, indent=1)
for r in records:
    print('%-44s %6d bytes' % (r['slug'], len(r['content'].encode())))
