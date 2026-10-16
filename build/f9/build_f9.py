"""Family 9 pillar: /guides/nil-t2-return-complete-guide/

Plan sources, all verbatim where the plan gives wording:

  6(a) line 1170   Title "Nil T2 Return | Complete Guide for Canadian
                   Corporations", meta description, H1 "The Complete Guide to
                   the Nil T2 Return", "Visible update date in the first screen".
  line 1194        Pillar for clusters F1, F5 and F13. "Every cluster URL links
                   up once with an exact-match anchor; pillar links down to 30
                   hand-picked children." Largest cluster on the site.
  line 1217 gate   "No pillar publishes without a visible update date and a
                   12-row on-page contents block." Banned term: CRA endorsed.
                   Owner: Sharad Gondaliya reviews, Navneet publishes.
  6(g) line 1528   F9: minimum 12 inbound, maximum 40 outbound.
  7.9 line 1565    Visible date "Under the H1, above the contents block".
  7.6              The 14 REQUIRED QUALIFICATIONS and the NIL-STATUS RULES are
                   the factual spine of this page, used verbatim.
  line 177         The fee-inclusion sentence, split into the coverage table.
  7.4              EFILE sentence for every Family 9 pillar is the three
                   sentence form, not the short one.

Design. The ei-* system Navneet supplied from gondaliyacpa.ca, with every
breaching element removed: no "Book Free Consultation" (hard rule 7 and the
7.6 banned list), no review count (7.4, banned until the claim audit closes),
no "guarantee" (7.4), and no FAQPage markup (hard rule 6). The checkmark
pseudo-element was dropped too, since a dingbat risks the no-emoji rule.

Price. Written "$300.00 plus HST per tax year" per Navneet's standing
correction. The plan's own line 177 says "including HST"; logged for Sharad.
"""
import json, os, re

SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
SLUG = 'nil-t2-return-complete-guide'
URL  = SITE + '/guides/' + SLUG + '/'
TODAY = 'October 16, 2026'
PRICE = '$300.00 plus HST per tax year'

TITLE = 'Nil T2 Return | Complete Guide for Canadian Corporations'
H1    = 'The Complete Guide to the Nil T2 Return'
META  = ('Who must file, what a nil return is, which schedules are required, how '
         'T183CORP is signed, and what happens to unfiled years. Updated monthly.')

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

A = SITE + '/answers/'
QUESTIONS = [
 ('what-happens-if-i-dont-file-a-nil-t2', "What happens if I don't file a nil T2?"),
 ('what-happens-if-i-dont-file-my-t2-for-five-years', "What happens if I don't file my T2 for five years?"),
 ('what-happens-if-i-dont-file-a-t2-before-dissolving-my-corporation', "What happens if I don't file a T2 before dissolving my corporation?"),
 ('what-happens-if-i-dont-report-a-dormant-corporation-to-cra', "What happens if I don't report a dormant corporation to the CRA?"),
 ('what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2', "What happens if I don't respond to a CRA demand to file a T2?"),
 ('what-happens-if-i-dont-file-a-nil-t2-for-a-numbered-company', "What happens if I don't file a nil T2 for a numbered company?"),
 ('what-happens-if-i-dont-file-t2-returns-after-my-corporation-is-dissolved', "What happens if I don't file T2 returns after my corporation is dissolved?"),
 ('do-i-need-to-file-a-t2-if-my-corporation-had-no-activity', 'Do I need to file a T2 if my corporation had no activity?'),
 ('do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account', 'Do I need to file a nil T2 if my corporation has no bank account?'),
 ('do-i-need-financial-statements-for-a-nil-t2-return', 'Do I need financial statements for a nil T2 return?'),
]

# 12-row contents block. Line 1217 makes exactly this the publish gate.
TOC = [
 ('who-must-file', 'Who Must File a T2 Return'),
 ('what-is-nil', 'What Counts as a Nil Return'),
 ('not-nil', 'What Is Not Nil'),
 ('t2-short', 'The T2 Short and Who Qualifies'),
 ('gifi', 'GIFI Schedules 100, 125 and 141'),
 ('other-schedules', 'Schedules 24, 50 and 8'),
 ('first-year', 'Your First Tax Year and the 53-Week Rule'),
 ('t183corp', 'Form T183CORP and How It Is Signed'),
 ('deadlines', 'Filing Deadlines'),
 ('unfiled', 'Unfiled Years and What They Cost'),
 ('other-returns', 'Returns That Are Not the T2'),
 ('fee', 'What the Fee Covers'),
]
assert len(TOC) == 12

CSS = """<style>
.ei-wrap{max-width:1100px;margin:0 auto;padding:0 20px}
.ei-btn-blue{background:rgba(32,135,201,1);color:#fff !important;padding:13px 26px;border-radius:6px;font-weight:700;font-size:0.95em;text-transform:uppercase;text-decoration:none !important;display:inline-block;line-height:1.4;text-align:center;min-width:120px}
.ei-section{padding:26px 20px}
.ei-section-alt{background:#f7f9fc;padding:26px 20px}
.ei-art .ei-h2{font-weight:800;color:#1a2340;margin:0 0 10px;font-size:1.45em;line-height:1.3}
.ei-art > *:last-child{margin-bottom:0}
.ei-art p{color:#4a5568;line-height:1.8}
.ei-art a{color:rgba(32,135,201,1)}
.ei-art ul{color:#4a5568;line-height:1.8}
.ei-info{background:#f0f7fd;border-left:4px solid rgba(32,135,201,1);border-radius:0 8px 8px 0;padding:14px 18px;margin:18px 0}
.ei-info p{margin:0;color:#1a2340;line-height:1.7}
.ei-warn{background:#fffbf0;border-left:4px solid #f6ad1a;border-radius:0 8px 8px 0;padding:14px 18px;margin:18px 0}
.ei-warn p{margin:0;color:#7c5800;line-height:1.7}
.ei-danger{background:#fff5f5;border-left:4px solid #e53e3e;border-radius:0 8px 8px 0;padding:14px 18px;margin:18px 0}
.ei-danger p{margin:0;color:#742a2a;line-height:1.7}
.ei-hero{background:linear-gradient(135deg,#0f1624 0%,#1a2340 55%,#1e3a6e 100%);padding:40px 20px}
.ei-hero-inner{max-width:860px;margin:0 auto;text-align:center}
.ei-hero-eyebrow{display:inline-block;background:rgba(32,135,201,0.15);border:1px solid rgba(32,135,201,0.4);border-radius:50px;padding:5px 16px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:rgba(32,135,201,1);margin-bottom:16px;font-size:.8em}
.ei-hero h1{color:#fff;font-weight:800;line-height:1.2;margin:0 0 14px;font-size:2.1em}
.ei-hero h1 span{color:#f6ad1a}
.ei-hero-sub{color:rgba(255,255,255,0.78);max-width:720px;margin:0 auto 10px;line-height:1.75}
.ei-hero-by{color:rgba(255,255,255,0.6);max-width:720px;margin:0 auto 22px;line-height:1.6;font-size:.86em}
.ei-hero-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.ei-tbl{width:100%;border-collapse:collapse;margin:18px 0;border:1px solid #d1d5db}
.ei-tbl th{background:#1a2340;color:#fff;font-weight:700;padding:12px 14px;text-align:left;border:1px solid #374151}
.ei-tbl td{padding:10px 14px;border:1px solid #d1d5db;color:#2d3748;line-height:1.5}
.ei-tbl tr:nth-child(even){background:#f7f9fc}
.ei-tbl tr:hover{background:#edf2f7}
.ei-updated{color:#718096;font-size:.9em;margin:0 0 18px}
.ei-toc{background:linear-gradient(180deg,#ffffff,#f7f9fc);border:1px solid #e2e8f0;border-radius:12px;padding:18px 22px;margin:0 0 10px;box-shadow:0 1px 2px rgba(26,35,64,.05)}
.ei-toc h2{font-size:.76em;font-weight:800;color:#8795ab;margin:0 0 10px;text-transform:uppercase;letter-spacing:1.3px}
.ei-toc ol{margin:0;padding:0;list-style:none;counter-reset:toc;columns:2;column-gap:30px}
.ei-toc li{break-inside:avoid;counter-increment:toc;margin:0}
.ei-toc a{display:flex;gap:10px;align-items:baseline;padding:6px 9px;border-radius:6px;color:#1a2340;text-decoration:none;line-height:1.45}
.ei-toc a::before{content:counter(toc);color:rgba(32,135,201,1);font-weight:800;font-size:.82em;min-width:15px;flex-shrink:0}
.ei-toc a:hover{background:#eaf3fb;color:rgba(32,135,201,1);text-decoration:none}
.ei-cta-inline{background:#1a2340;border-radius:10px;padding:24px 28px;margin:28px 0;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px}
.ei-cta-inline h3{color:#fff;margin:0 0 4px;font-weight:700}
.ei-cta-inline p{color:rgba(255,255,255,0.65);margin:0}
.ei-cta-inline a,.ei-cta-inline a:visited,.ei-cta-inline a:hover,.ei-cta-bottom a,.ei-cta-bottom a:visited,.ei-cta-bottom a:hover,.ei-hero-btns a,.ei-hero-btns a:visited,.ei-hero-btns a:hover{color:#fff !important;text-decoration:none !important}
.ei-faq{max-width:900px;margin:16px auto 0}\n.ei-faq details{border:1px solid #e2e8f0;border-radius:8px;margin-bottom:9px;background:#fff}\n.ei-faq summary{padding:14px 18px;font-weight:600;color:#1a2340;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:14px;line-height:1.5}\n.ei-faq summary::-webkit-details-marker{display:none}\n.ei-faq summary::after{content:'+';color:rgba(32,135,201,1);font-weight:400;font-size:1.4em;line-height:1;flex-shrink:0;transition:transform .15s ease}\n.ei-faq details[open] summary{color:rgba(32,135,201,1)}\n.ei-faq details[open] summary::after{transform:rotate(45deg)}\n.ei-faq .ei-faq-a{padding:0 18px 15px}\n.ei-faq .ei-faq-a p{margin:0;color:#4a5568;line-height:1.75}\n.ei-art h3{font-weight:700;color:#1a2340;margin:26px 0 8px;font-size:1.15em}\n.ei-qlist{max-width:900px;margin:12px auto 0;padding:0;list-style:none}
.ei-qlist li{border:1px solid #e2e8f0;border-radius:8px;margin-bottom:10px;background:#fff}
.ei-qlist a{display:block;padding:16px 20px;font-weight:600;color:#1a2340 !important;text-decoration:none !important}
.ei-qlist a:hover{background:#f7f9fc;color:rgba(32,135,201,1) !important}
.ei-cta-bottom{background:linear-gradient(135deg,#0f1624,#1a2340);padding:40px 20px;text-align:center}
.ei-cta-bottom h2{color:#fff;font-weight:800;margin:0 0 10px;font-size:1.5em}
.ei-cta-bottom p{color:rgba(255,255,255,0.72);max-width:600px;margin:0 auto 22px;line-height:1.75}
.entry-header{display:none!important}
.ast-article-single,.ast-article-single .entry-content{margin-top:0;padding-top:0}
@media(max-width:900px){.ei-cta-inline{flex-direction:column;text-align:center}.ei-hero h1{font-size:1.6em}.ei-art .ei-h2{font-size:1.3em}.ei-toc ol{columns:1}}
</style>
"""

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
    return ('<div class="%s" id="%s"><div class="ei-wrap ei-art">\n<h2 class="ei-h2">%s</h2>\n%s\n</div></div>\n'
            % (cls, key, title, body))

def cta_inline(h3, p):
    return ('<div class="ei-cta-inline"><div><h3>%s</h3><p>%s</p></div>'
            '<a class="ei-btn-blue" href="%s">Start Nil T2 Filing NOW</a></div>\n' % (h3, p, FORM))

parts = [CSS]

# ---- hero -----------------------------------------------------------------
parts.append(
 '<div class="ei-hero"><div class="ei-hero-inner">'
 '<span class="ei-hero-eyebrow">Nil T2 Guide</span>'
 '<h1>The Complete Guide to the <span>Nil T2 Return</span></h1>'
 '<p class="ei-hero-sub">' + META + ' Nil T2 filing is ' + PRICE + '.</p>'
 '<p class="ei-hero-by">' + BYLINE + '</p>'
 '<div class="ei-hero-btns"><a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
 '<a class="ei-btn-blue" style="background:transparent;border:2px solid rgba(255,255,255,0.4)" href="'
 + SITE + '/pricing/nil-t2-filing-cost/">See the Full Cost</a></div>'
 '</div></div>\n')

# ---- update date + 12-row contents block (the F9 gate) ---------------------
toc_rows = '\n'.join('<li>%s</li>' % a('#' + k, t) for k, t in TOC)
parts.append(
 '<div class="ei-section"><div class="ei-wrap ei-art">\n'
 '<p class="ei-updated">Last reviewed: ' + TODAY + ' &nbsp;&middot;&nbsp; '
 + a(SITE + '/guides/', 'All nil T2 filing guides') + '</p>\n'
 '<div class="ei-toc"><h2>On this page</h2>\n<ol>\n' + toc_rows + '\n</ol></div>\n'
 '<div class="ei-info"><p>' + EFILE_PILLAR + '</p></div>\n'
 '</div></div>\n')

# ---- 1 ---------------------------------------------------------------------
parts.append(sec('who-must-file', 'Who Must File a T2 Return',
 '<p>Every resident corporation, including an inactive one, must file a T2 within six '
 'months of its fiscal year-end, every year, until it is formally dissolved. A final T2 '
 'is due within six months of dissolution.</p>\n'
 '<p>The obligation comes from being an incorporated resident corporation. It does not '
 'depend on earning anything, holding a bank account, or having employees. There is no '
 'minimum income below which the return can be skipped.</p>\n'
 '<div class="ei-warn"><p>For tax years starting after 2023, e-filing is mandatory for '
 'virtually all corporations. A paper T2 draws a $1,000 penalty plus a $100 per-return '
 'preparer penalty.</p></div>', alt=True))

# ---- 2 ---------------------------------------------------------------------
parts.append(sec('what-is-nil', 'What Counts as a Nil Return',
 '<p>A corporation is nil for this service only when it had no activity at all in the '
 'tax year. No revenue, no expenses claimed, no payroll, no asset purchases and no '
 'inter-company transactions.</p>\n'
 + tbl(('Situation in the tax year', 'Still a nil return'),
   [('No revenue and no expenses', 'Yes'),
    ('No bank account, or an account with no movement', 'Yes'),
    ('No employees and no payroll', 'Yes'),
    ('Share capital, cash or a shareholder loan on the books',
     'Yes, but GIFI schedules are required'),
    ('Any revenue, or any expense claimed', 'No'),
    ('Investment income, rental income, or a dividend paid or received', 'No')])))

# ---- 3 ---------------------------------------------------------------------
parts.append(sec('not-nil', 'What Is Not Nil',
 '<p>These corporations are not nil and are handled by Gondaliya CPA Professional '
 'Corporation at gondaliyacpa.ca at $350.00 plus HST per year:</p>\n'
 '<ul><li>a holding company with investment income</li>'
 '<li>a rental corporation</li>'
 '<li>a corporation that received or paid a dividend</li>'
 '<li>a corporation with any revenue, any expense claimed, any payroll, any asset '
 'purchase or any inter-company transaction</li></ul>\n'
 '<div class="ei-info"><p>An open GST/HST account or an open payroll account still needs '
 'nil filings, or a closure using Form RC145. An inactive T2 does not close those '
 'accounts.</p></div>', alt=True))

# ---- 4 ---------------------------------------------------------------------
parts.append(sec('t2-short', 'The T2 Short and Who Qualifies',
 '<p>The T2 Short is a two-page version of the return. It is available only to a '
 'Canadian-controlled private corporation that meets every one of the following:</p>\n'
 + tbl(('Condition', 'Requirement'),
   [('Corporation type', 'Canadian-controlled private corporation'),
    ('Net income', 'Nil net income or a loss for the year'),
    ('Permanent establishments', 'One only'),
    ('Taxable dividends', 'None paid and none received'),
    ('Currency', 'Canadian'),
    ('Refundable credits', 'None claimed'),
    ('Ontario transitional debit', 'None'),
    ('Section 34.2 amount', 'None')])
 + '\n<p>Where the corporation qualifies, the T2 Short is included in the fee. See '
 + a(SITE + '/t2-short-filing/', 'T2 Short filing') + ' for how it differs from the full return.</p>'))

parts.append('<div class="ei-wrap">' + cta_inline(
  'Nil T2 Filing, ' + PRICE,
  'One price for every year and every province. CPA reviewed and transmitted electronically.')
  + '</div>\n')

# ---- 5 ---------------------------------------------------------------------
parts.append(sec('gifi', 'GIFI Schedules 100, 125 and 141',
 '<p>GIFI is the standard code set the Canada Revenue Agency uses for the balance sheet '
 'and income statement inside the T2.</p>\n'
 '<p>A corporation inactive all year with nothing to report may omit GIFI Schedules 100, '
 '125 and 141. But any share capital, cash, shareholder loan, incorporation cost or bank '
 'charge makes them required, even though the corporation had no activity.</p>\n'
 '<div class="ei-warn"><p>This is the single most common reason a return that looks nil '
 'is not filed correctly. A corporation with $100 of share capital and nothing else still '
 'reports that balance.</p></div>\n'
 '<p>See ' + a(A + 'do-i-need-financial-statements-for-a-nil-t2-return/',
               'whether financial statements are needed for a nil T2 return') + '.</p>',
 alt=True))

# ---- 6 ---------------------------------------------------------------------
parts.append(sec('other-schedules', 'Schedules 24, 50 and 8',
 tbl(('Schedule', 'When it is required'),
  [('Schedule 24', 'On the first return after incorporation'),
   ('Schedule 50', 'For every shareholder holding 10% or more'),
   ('Schedule 8', 'Capital cost allowance, recorded with loss continuity'),
   ('Loss continuity', 'Must be recorded so losses carry forward correctly')])))

# ---- 7 ---------------------------------------------------------------------
parts.append(sec('first-year', 'Your First Tax Year and the 53-Week Rule',
 '<p>The first tax year cannot exceed 53 weeks, and the year-end must match the Canada '
 "Revenue Agency's record or the transmission is rejected.</p>\n"
 '<p>Schedule 24 is required on that first return. Getting the year-end wrong is the most '
 'common cause of a rejected first transmission, because the Agency already holds a '
 'year-end from the incorporation record.</p>', alt=True))

# ---- 8 ---------------------------------------------------------------------
parts.append(sec('t183corp', 'Form T183CORP and How It Is Signed',
 '<p>Form T183CORP is the authorisation that lets a registered EFILE electronic filer '
 'transmit the return. It is signed by an authorized signing officer before the return is '
 'transmitted.</p>\n'
 + tbl(('Rule', 'Detail'),
   [('Who signs', 'An authorized signing officer of the corporation'),
    ('When', 'Before transmission, never after'),
    ('Date and time', 'Carries a date and an HH:MM:SS timestamp, never backdated'),
    ('How it may be signed', 'E-signed through an access-controlled secure portal'),
    ('Retention', 'Kept by the firm for six years'),
    ('Sent to the Agency', 'No, not unless requested')])
 + '\n<div class="ei-info"><p>An EFILE number plus a signed T183CORP are enough to '
 'transmit. Representative authorization is optional and post-filing only.</p></div>'))

# ---- 9 ---------------------------------------------------------------------
parts.append(sec('deadlines', 'Filing Deadlines',
 '<p>A T2 is due within six months of the fiscal year-end. Where a due date falls on a '
 'Saturday, a Sunday or a public holiday recognised by the Canada Revenue Agency, a '
 'return received the next business day is on time.</p>\n'
 '<p>Every fiscal year-end and its due date is listed on '
 + a(SITE + '/deadlines/', 'T2 filing deadlines') + ', and the '
 + a(SITE + '/deadlines/cra-t2-deadline-calendar/', 'T2 deadline calendar')
 + ' shows which dates move for a weekend or an Ontario statutory holiday.</p>', alt=True))

# ---- 10 --------------------------------------------------------------------
parts.append(sec('unfiled', 'Unfiled Years and What They Cost',
 '<div class="ei-danger"><p>' + LATE_QUAL + '</p></div>\n'
 '<p>Each year is a separate return with its own fiscal year-end and its own due date. '
 'There is no combined multi-year return and no reduced rate for filing several years '
 'together.</p>\n'
 + tbl(('Tax years outstanding', 'Fee at ' + PRICE),
   [('1 year', '$300.00 plus HST'), ('3 years', '$900.00 plus HST'),
    ('5 years', '$1,500.00 plus HST'), ('10 years', '$3,000.00 plus HST')])
 + '\n<p>See ' + a(SITE + '/catch-up-nil-t2-filing/', 'catch-up nil T2 filing')
 + ' for the years that can still be filed, and '
 + a(SITE + '/final-t2-before-dissolution/', 'the final T2 before dissolution')
 + ' for closing a corporation.</p>'))

# ---- 11 --------------------------------------------------------------------
parts.append(sec('other-returns', 'Returns That Are Not the T2',
 '<p>Filing the T2 does not satisfy these. They are separate obligations with their own '
 'deadlines.</p>\n'
 + tbl(('Return', 'Who files it', 'Detail'),
   [('Ontario annual return', 'Ontario corporations',
     'Filed through the Ontario Business Registry since October 2021, not with the T2'),
    ('Corporations Canada annual return', 'Federal corporations',
     '$12, within 60 days of the anniversary date'),
    ('Alberta AT1', 'Alberta corporations', 'A separate provincial return'),
    ('Quebec CO-17', 'Quebec corporations', 'A separate provincial return')]),
 alt=True))

# ---- 12 --------------------------------------------------------------------
parts.append(sec('fee', 'What the Fee Covers',
 '<p>' + PRICE.capitalize() if False else '<p>The fee is ' + PRICE
 + ', covering one nil T2 return for one corporation for one tax year:</p>\n'
 + tbl(('Included', 'Detail'),
   [('The T2 return', 'Including the T2 Short where the corporation qualifies'),
    ('GIFI Schedules 100, 125 and 141', 'Where they are required'),
    ('Schedule 24', 'On a first return'),
    ('Schedule 50', 'For every shareholder at 10% or more'),
    ('Schedule 8 and loss continuity', 'Recorded'),
    ('Form T183CORP package', 'With single-use secure e-signing'),
    ('CPA review', 'Before transmission'),
    ('Electronic transmission', 'By a registered EFILE electronic filer'),
    ('One corrected transmission', 'If the Agency rejects the first one'),
    ('CRA confirmation', 'Emailed within 3 business days')])
 + '\n<p>See the full ' + a(SITE + '/pricing/nil-t2-filing-cost/', 'nil T2 filing cost')
 + '.</p>'))


# ---------------------------------------------------------------------------
# Pillar FAQ. These eight questions are deliberately NOT among Appendix A's 45
# Family 5 slugs, checked by token overlap, so the pillar adds coverage instead
# of competing with its own children. Answers come from the 7.6 REQUIRED
# QUALIFICATIONS. Rendered with <details>, so no JavaScript and no FAQPage
# markup (hard rule 6, plan line 37, line 1582, launch gate 6).
# ---------------------------------------------------------------------------
FAQ = [
 ('What Is a Nil T2 Return?',
  'A nil T2 is the ordinary corporate return filed for a tax year in which the '
  'corporation had no activity at all. It is a filed return reporting nil amounts, not '
  'a missing return. The obligation and the form are the same as for an active '
  'corporation.'),
 ('Is Electronic Filing Mandatory for a Nil T2?',
  'Yes. For tax years starting after 2023, e-filing is mandatory for virtually all '
  'corporations. A paper T2 draws a $1,000 penalty plus a $100 per-return preparer '
  'penalty.'),
 ('What Is the Difference Between the T2 and the T2 Short?',
  'The T2 Short is a two-page version of the same return. It is available only to a '
  'Canadian-controlled private corporation with nil net income or a loss, one permanent '
  'establishment, no taxable dividends paid or received, Canadian currency, no '
  'refundable credits, no Ontario transitional debit and no section 34.2 amount. Where '
  'the corporation qualifies, it is included in the fee.'),
 ('Who Signs Form T183CORP, and When?',
  'An authorized signing officer of the corporation signs it, before the return is '
  'transmitted and never after. It carries a date and an HH:MM:SS timestamp that is '
  'never backdated, may be e-signed through an access-controlled secure portal, is kept '
  'by the firm for six years, and is not sent to the Canada Revenue Agency unless '
  'requested.'),
 ('Does Filing the T2 Cover My Ontario Annual Return?',
  'No. The Ontario annual return has been filed through the Ontario Business Registry '
  'since October 2021, separately from the T2. Federal corporations also file a separate '
  '$12 Corporations Canada annual return within 60 days of their anniversary date, and '
  'Alberta AT1 and Quebec CO-17 are separate provincial returns.'),
 ('Does a Nil T2 Close My GST/HST or Payroll Account?',
  'No. An open GST/HST account or an open payroll account still needs nil filings of its '
  'own, or a closure using Form RC145. An inactive T2 does not close those accounts.'),
 ('What Is an Arbitrary Assessment?',
  'It is an assessment the Canada Revenue Agency raises on its own figures when no '
  'return is filed, usually after a demand to file. It does not close the year the way a '
  'filed return does, and it is replaced once the real return is assessed.'),
 ('What Does the Fee Include?',
  'The fee covers one nil T2 for one corporation for one tax year: the T2 Short where '
  'the corporation qualifies, GIFI Schedules 100, 125 and 141 where required, Schedule '
  '24 on a first return, Schedule 50 for every shareholder at 10% or more, Schedule 8 '
  'and loss continuity, the Form T183CORP package with single-use secure e-signing, CPA '
  'review, electronic transmission by a registered EFILE electronic filer, one corrected '
  'transmission if the Agency rejects the first, and your CRA confirmation emailed '
  'within 3 business days.'),
]

faq_items = '\n'.join(
 '<details><summary>%s</summary><div class="ei-faq-a"><p>%s</p></div></details>'
 % (q, ans) for q, ans in FAQ)

# ---- cluster children ------------------------------------------------------
qlinks = '\n'.join('<li>%s</li>' % a(A + s + '/', t) for s, t in QUESTIONS)
parts.append(
 '<div class="ei-section-alt"><div class="ei-wrap ei-art">\n'
 '<h2 class="ei-h2">Frequently Asked Questions</h2>\n'
 '<div class="ei-faq">\n' + faq_items + '\n</div>\n'
 '<h3>More Questions, Each Answered in Full</h3>\n'
 '<ul class="ei-qlist">\n' + qlinks + '\n</ul>\n'
 '</div></div>\n')

# ---- bottom CTA ------------------------------------------------------------
parts.append(
 '<div class="ei-cta-bottom"><div class="ei-wrap">'
 '<h2>Nil T2 Filing, ' + PRICE + '</h2>'
 '<p>Type your corporation name, pick your unfiled years, pay, and sign Form T183CORP on '
 'a secure screen. Your CRA confirmation is emailed within 3 business days.</p>'
 '<a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
 '</div></div>\n')

# ---- schema: Article with dateModified (line 1342). No FAQPage, no HowTo. ---
schema = {"@context": "https://schema.org", "@graph": [
 {"@type": "Article", "@id": URL + "#article", "headline": H1, "name": TITLE,
  "description": META, "inLanguage": "en-CA",
  "datePublished": "2026-10-16", "dateModified": "2026-10-16",
  "mainEntityOfPage": URL,
  "author": {"@type": "Person", "name": "Sharad Gondaliya", "honorificSuffix": "CPA",
             "url": SITE + "/sharad-gondaliya-cpa/"},
  "publisher": {"@type": "Organization", "name": "Gondaliya CPA Professional Corporation"}},
 {"@type": "BreadcrumbList", "itemListElement": [
   {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada", "item": SITE + "/"},
   {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/guides/"},
   {"@type": "ListItem", "position": 3, "name": H1, "item": URL}]}]}
parts.append('<script type="application/ld+json">'
             + json.dumps(schema, ensure_ascii=False) + '</script>')

html = ''.join(parts)
d = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(d, SLUG + '.html'), 'w', encoding='utf-8').write(html)
json.dump([dict(slug=SLUG, title=TITLE, meta_description=META, url=URL, content=html,
                h1=H1, toc=[t for _, t in TOC])],
          open(os.path.join(d, 'f9-manifest.json'), 'w'), ensure_ascii=False, indent=1)
print('built %s  %d bytes' % (SLUG, len(html.encode())))
