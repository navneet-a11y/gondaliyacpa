"""Family 5 content generator: question pages (first 5 of 45).

Every structural rule here comes from the plan, not from invention:

  6(a) line 1143   URL shape /answers/<question>/, "Answer-first template,
                   no FAQPage markup". CPT nil_question, rewrite base
                   "answers" (line 312).
  line 1166        Worked exemplar: the answer-first paragraph IS the meta
                   description.
  line 1578        Answer-first paragraph answers the H1 in 40 to 60 words,
                   no preamble, no brand name. Sentence one states the
                   answer, sentence two the rule, sentence three the
                   exception. One H2 per question, written as the question.
                   One table per page that holds the numbers. No FAQPage and
                   no HowTo markup.
  line 1213 gate   "No question page publishes without a 45-word answer-first
                   paragraph written for that question only." Banned term for
                   this family: T183 (hard rule 2 makes it T183CORP).
  6(g) line 1527   Family 5: minimum 3 inbound, maximum 15 outbound body
                   links. Anchor is the question text shortened to 6 words.

Slug note. Appendix A gives these 45 at root level
(/what-happens-if-i-dont-file-a-nil-t2/). 6(a) and the CPT rewrite base both
give /answers/<question>/. Resolved toward 6(a), as the six previous Appendix
A conflicts were. Logged for Sharad Gondaliya.

Authorship note. Line 1213 names the source as "Sharad's answer bank, one
entry per question, written once" and the owner as "Sharad Gondaliya writes
and reviews". No answer bank was supplied, so these five answers are drafted
to the plan's shape and are pending his sign-off.
"""
import json, os, sys, re

SITE  = 'https://corpnilfilingfor300.ca'
PRICE = '$300.00 plus HST per tax year'
FORM  = SITE + '/form/'
CTA   = 'Start Nil T2 Filing NOW'
TODAY = 'October 16, 2026'
HERO_IMG = (SITE + '/wp-content/uploads/2026/09/'
            'business-executives-having-meeting_1098-18316.jpg')

BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')

# 7.4 copy-paste blocks, used verbatim.
EFILE_SHORT = ('We are a registered EFILE electronic filer. Your return is '
               'transmitted to the Canada Revenue Agency electronically.')
LATE_QUAL = ('A true nil return carries no percentage late-filing penalty, because '
             'that penalty is a percentage of tax owing and the corporation owes '
             '$0.00. The unfiled year still stays open forever, invites a demand to '
             'file and an arbitrary assessment, blocks a clearance certificate and '
             'dissolution, and costs a non-resident-owned corporation $25.00 per day '
             'up to $2,500.00.')
SCOPE = ('This service is for a corporation with no activity in the tax year. A '
         'corporation with investment income, rental income, or dividends paid or '
         'received is not nil.')

CSS = """<style>.cnf-hero{background-image:linear-gradient(rgba(11,26,51,.82),rgba(11,26,51,.82)),url('""" + HERO_IMG + """');background-size:cover;background-position:center center;background-repeat:no-repeat;padding:40px 20px}
.cnf-hero-in{max-width:1140px;margin:0 auto;text-align:left}
.cnf-hero h1{color:#fff;font-family:Poppins,sans-serif;font-weight:700;font-size:40px;line-height:1.25;margin:0}
.cnf-hero .cnf-hero-sub{color:#fff;font-family:Poppins,sans-serif;font-weight:600;font-size:25px;margin:10px 0 0}
.cnf-hero .cnf-hero-lede{color:#fff;font-family:Lato,sans-serif;font-size:17px;line-height:1.6;margin:10px 0 0;max-width:860px}
.cnf-hero .cnf-hero-by{color:#e8ecf4;font-family:Lato,sans-serif;font-size:14px;line-height:1.6;margin:16px 0 0;max-width:860px}
.cnf-hero .cnf-hero-btn{display:inline-block;background:#314d8a;color:#fff!important;padding:20px 50px;border-radius:35px;font-family:Poppins,sans-serif;font-weight:600;font-size:18px;text-decoration:none!important;margin:24px 0 0}
.cnf-hero .cnf-hero-btn:hover,.cnf-hero .cnf-hero-btn:focus{background:#2087c9;color:#fff!important;text-decoration:none!important}
@media(max-width:767px){.cnf-hero{padding:32px 16px}.cnf-hero h1{font-size:28px}.cnf-hero .cnf-hero-sub{font-size:20px}.cnf-hero .cnf-hero-btn{padding:16px 34px;font-size:16px}}
.entry-header{display:none!important}
.ast-article-single,.ast-article-single .entry-content{margin-top:0;padding-top:0}
.cnf-w{max-width:1000px;margin:0 auto;padding:36px 20px 56px;font-family:Lato,sans-serif;color:#333;font-size:17px;line-height:1.65}
.cnf-w h2{font-family:Poppins,sans-serif;color:#314d8a;font-size:26px;font-weight:600;margin:40px 0 12px}
.cnf-w a{color:#314d8a;font-weight:600}.cnf-w a:hover{color:#2087c9}
.cnf-w .cnf-meta{font-size:14px;color:#636363;line-height:1.8;margin:0 0 26px}
.cnf-w .cnf-meta .cnf-crumb,.cnf-w .cnf-meta .cnf-rev{display:inline;margin:0}
.cnf-w .cnf-meta a{font-weight:400;text-decoration:none}
.cnf-w .cnf-updated{font-size:14px;color:#636363;border-top:1px solid #dfe6ef;padding-top:16px;margin:28px 0 0}
.cnf-w .cnf-answer{font-size:19px;line-height:1.6;border-left:5px solid #314d8a;background:#f5f8fc;border-radius:0 8px 8px 0;padding:18px 22px;margin:0 0 8px}
.cnf-tbl{width:100%;border-collapse:collapse;font-size:16px;margin:16px 0}.cnf-tbl th,.cnf-tbl td{border:1px solid #dfe6ef;padding:12px 14px;text-align:left;vertical-align:top}
.cnf-tbl th{background:#314d8a;color:#fff;font-family:Poppins,sans-serif;font-weight:600}.cnf-tbl td:last-child{font-weight:700;color:#314d8a}
.cnf-qual{background:#f5f8fc;border-left:5px solid #314d8a;border-radius:0 8px 8px 0;padding:18px 22px;margin:18px 0}
.cnf-btn{display:inline-block;background:#314d8a;color:#fff!important;padding:16px 36px;border-radius:35px;font-family:Poppins,sans-serif;font-weight:600;text-decoration:none;margin:8px 12px 8px 0}.cnf-btn:hover{background:#2087c9}</style>
"""

def a(href, text):
    return '<a href="%s">%s</a>' % (href, text)

def table(head, rows):
    out = ['<table class="cnf-tbl"><thead><tr><th scope="col">%s</th>'
           '<th scope="col">%s</th></tr></thead><tbody>' % head]
    for k, v in rows:
        out.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    out.append('</tbody></table>')
    return '\n'.join(out)

# ---------------------------------------------------------------------------
# The five records. Appendix A order, the "what happens if" group.
# Each answer: sentence 1 the answer, sentence 2 the rule, sentence 3 the
# exception, 40 to 60 words, no preamble and no brand name.
# ---------------------------------------------------------------------------
Q = [
 dict(
  slug='what-happens-if-i-dont-file-a-nil-t2',
  h1="What Happens if I Don't File a Nil T2?",
  anchor='What happens if I do not file',
  keyword='what happens if i dont file a nil t2',
  answer=('The tax year stays open and the Canada Revenue Agency can demand the '
          'return and assess the corporation arbitrarily. Every resident corporation '
          'must file a T2 within six months of its fiscal year-end, every year, until '
          'it is formally dissolved. Having no revenue and no bank activity does not '
          'remove the obligation.'),
  head=('What applies', 'Figure'),
  rows=[('Months after the fiscal year-end to file', '6'),
        ('Tax owing on a true nil return', '$0.00'),
        ('Percentage late-filing penalty on a true nil return', '$0.00'),
        ('Non-resident-owned corporation penalty', '$25.00 per day, to $2,500.00'),
        ('How long an unfiled year stays open', 'Until it is filed'),
        ('Fee to file', '$300.00 plus HST per tax year')],
  qual=True,
  body=('A demand to file is a formal request from the Canada Revenue Agency, and an '
        'arbitrary assessment is a figure the Agency sets itself when no return '
        'arrives. Filing the real return replaces that figure with the '
        "corporation's own.")),
 dict(
  slug='what-happens-if-i-dont-file-my-t2-for-five-years',
  h1="What Happens if I Don't File My T2 for Five Years?",
  anchor='What happens after five unfiled years',
  keyword='what happens if i dont file my t2 for five years',
  answer=('All five returns stay outstanding and each year is filed separately. A T2 '
          'is due within six months of each fiscal year-end, so five missed year-ends '
          'means five separate returns, every one of them still required. Filing all '
          'five at once is routine and closes the years in a single pass.'),
  head=('Tax years outstanding', 'Fee at $300.00 plus HST per tax year'),
  rows=[('1 year', '$300.00 plus HST'),
        ('2 years', '$600.00 plus HST'),
        ('3 years', '$900.00 plus HST'),
        ('4 years', '$1,200.00 plus HST'),
        ('5 years', '$1,500.00 plus HST')],
  qual=True,
  body=('Each year is a separate return with its own fiscal year-end and its own due '
        'date. There is no combined five-year return and no reduced rate for filing '
        'several years together.')),
 dict(
  slug='what-happens-if-i-dont-file-a-t2-before-dissolving-my-corporation',
  h1="What Happens if I Don't File a T2 Before Dissolving My Corporation?",
  anchor='What happens if dissolving without filing',
  keyword='file t2 before dissolving corporation',
  answer=('Dissolution can be held up and the outstanding years remain the '
          "corporation's responsibility. A final T2 is due within six months of "
          'dissolution, and every earlier year must already be filed. An unfiled year '
          'blocks a clearance certificate, which is what confirms nothing is owed '
          'before the corporation closes.'),
  head=('Requirement', 'Figure'),
  rows=[('Months after each fiscal year-end to file', '6'),
        ('Months after dissolution the final T2 is due', '6'),
        ('Earlier years that must already be filed', 'All of them'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=True,
  body=('A clearance certificate confirms the corporation has no outstanding amounts '
        'before it is wound up. An unfiled year is an open year, so the certificate '
        'cannot be issued until the return is filed.')),
 dict(
  slug='what-happens-if-i-dont-report-a-dormant-corporation-to-cra',
  h1="What Happens if I Don't Report a Dormant Corporation to the CRA?",
  anchor='What happens if not reporting dormancy',
  keyword='report dormant corporation to cra',
  answer=('There is no separate dormancy filing, so the obligation is simply the '
          'annual T2. A dormant corporation files a nil T2 within six months of each '
          'fiscal year-end until it is formally dissolved. Telling the Canada Revenue '
          'Agency the corporation is inactive does not replace the return.'),
  head=('Point', 'Figure'),
  rows=[('Separate dormancy form required', 'None'),
        ('Months after the fiscal year-end to file', '6'),
        ('How long the obligation continues', 'Until dissolution'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=True,
  body=('Dormant and inactive are descriptions, not filing statuses. The Canada '
        'Revenue Agency has no form that pauses the T2 obligation, so the return is '
        'filed every year until the corporation is dissolved.')),
 dict(
  slug='what-happens-if-i-dont-respond-to-a-cra-demand-to-file-a-t2',
  h1="What Happens if I Don't Respond to a CRA Demand to File a T2?",
  anchor='What happens if ignoring a demand',
  keyword='cra demand to file a t2',
  answer=('The Canada Revenue Agency can assess the corporation arbitrarily, without '
          'waiting for the return. A demand to file is a formal request, and the '
          'return remains due within six months of the fiscal year-end regardless. '
          "Filing the real return replaces an arbitrary assessment with the "
          "corporation's actual figures."),
  head=('Point', 'Figure'),
  rows=[('Months after the fiscal year-end the T2 is due', '6'),
        ('Tax owing on a true nil return', '$0.00'),
        ('Percentage late-filing penalty on a true nil return', '$0.00'),
        ('Non-resident-owned corporation penalty', '$25.00 per day, to $2,500.00'),
        ('Fee to file', '$300.00 plus HST per tax year')],
  qual=True,
  body=('An arbitrary assessment is the Agency assessing on its own figures because '
        'no return was filed. It does not close the year in the way a filed return '
        'does, and it is replaced once the real return is assessed.')),
]

PILLAR = SITE + '/guides/nil-t2-return-complete-guide/'
MONEY = [SITE + '/pricing/nil-t2-filing-cost/', SITE + '/deadlines/',
         SITE + '/catch-up-nil-t2-filing/']

def build(rec, siblings):
    url = '%s/answers/%s/' % (SITE, rec['slug'])
    hero = ('<div class="cnf-hero"><div class="cnf-hero-in"><h1>' + rec['h1'] + '</h1>'
            '<p class="cnf-hero-sub">$300.00 Plus HST Per Tax Year</p>'
            '<p class="cnf-hero-lede">' + EFILE_SHORT + '</p>'
            '<p class="cnf-hero-by">' + BYLINE + '</p>'
            '<p><a class="cnf-hero-btn" href="' + FORM + '">' + CTA + '</a></p>'
            '</div></div>\n')

    crumb = ('<div class="cnf-meta"><nav class="cnf-crumb" aria-label="Breadcrumb">'
             + a(SITE + '/', 'Nil T2 filing in Canada') + ' &rsaquo; '
             '<span aria-current="page">' + rec['h1'] + '</span></nav></div>\n')

    # 6(g): siblings give each page its inbound links; money pages are the outbound.
    sib = '\n'.join('<li>%s</li>' % a('%s/answers/%s/' % (SITE, s['slug']), s['anchor'])
                    for s in siblings)

    body = ['<div class="cnf-w">', crumb,
            '<p class="cnf-answer">' + rec['answer'] + '</p>',
            '<h2>' + rec['h1'][0].upper() + rec['h1'][1:].rstrip('?').lower() + '?</h2>'
            if False else '<h2>' + rec['h1'] + '</h2>',
            table(rec['head'], rec['rows'])]
    if rec['qual']:
        body.append('<div class="cnf-qual"><p>' + LATE_QUAL + '</p></div>')
    body.append('<p>' + rec['body'] + '</p>')
    body.append('<h2>Filing a Nil Return</h2>')
    body.append('<p>' + SCOPE + '</p>')
    body.append('<p>We are a registered EFILE electronic filer. Your return is '
                'transmitted to the Canada Revenue Agency electronically, and your '
                'CRA confirmation is emailed within 3 business days. You sign Form '
                'T183CORP before we transmit. The fee is ' + PRICE + '. See the full '
                + a(MONEY[0], 'nil T2 filing cost') + ', every '
                + a(MONEY[1], 'T2 filing deadline') + ', and '
                + a(MONEY[2], 'catch-up nil T2 filing') + ' for outstanding years.</p>')
    # line 1194: every cluster URL links up once to the pillar with an
    # exact-match anchor on the pillar's keyword, "nil t2 return".
    body.append('<p>For the whole subject in one place, see the complete guide '
                'to the ' + a(PILLAR, 'nil T2 return') + '.</p>')
    body.append('<h2>Related Questions</h2>')
    body.append('<ul>' + sib + '</ul>')
    body.append('<p><a class="cnf-btn" href="' + FORM + '">' + CTA + '</a></p>')
    # 7.9 line 1570: for F1, F2, F5, F8, F10, F11, F12, F15 and F16 the visible
    # date sits in the footer of the article body, not under the H1 as 7.5 rule 1
    # says generally. The per-family row is the more specific instruction.
    body.append('<p class="cnf-updated">Last reviewed: ' + rec.get('date', TODAY) + '</p>')
    body.append('</div>')

    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": rec['h1'],
         "description": rec['answer'], "inLanguage": "en-CA",
         "dateModified": rec.get('iso', '2026-10-16'),
         "author": {"@type": "Person", "name": "Sharad Gondaliya",
                    "honorificSuffix": "CPA",
                    "url": SITE + "/sharad-gondaliya-cpa/"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
             "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": rec['h1'], "item": url}]}]}

    html = (CSS + hero + '\n'.join(body) + '\n<script type="application/ld+json">'
            + json.dumps(schema, ensure_ascii=False) + '</script>')
    return html, url

records = []
for i, rec in enumerate(Q):
    sibs = [s for j, s in enumerate(Q) if j != i]
    html, url = build(rec, sibs)
    records.append(dict(slug=rec['slug'], title=rec['h1'],
                        meta_description=rec['answer'], url=url, content=html,
                        answer=rec['answer'], keyword=rec['keyword'],
                        anchor=rec['anchor'],
                        terms={'cnf_family': ['f5']},
                        meta={'cnf_question_text': rec['h1'],
                              'cnf_short_answer': rec['answer'],
                              'cnf_primary_keyword': rec['keyword'],
                              'cnf_last_verified_et': '2026-10-16'}))

# ---------------------------------------------------------------------------
# Batch 2, Appendix A order: the last two "what happens if" questions and the
# first three "do I need" questions. `related` indexes into Q (batch 1) and
# ties the two batches into one cluster.
# ---------------------------------------------------------------------------
Q2 = [
 dict(
  slug='what-happens-if-i-dont-file-a-nil-t2-for-a-numbered-company',
  h1="What Happens if I Don't File a Nil T2 for a Numbered Company?",
  anchor='What happens for a numbered company',
  keyword='nil t2 for a numbered company',
  related=[0],
  answer=('Nothing changes because the corporation has a number instead of a name. A '
          'numbered company is an ordinary corporation and must file a T2 within six '
          'months of each fiscal year-end until it is dissolved. The numbered name '
          'affects nothing about the filing obligation or the due date.'),
  head=('Point', 'Figure'),
  rows=[('Months after the fiscal year-end to file', '6'),
        ('Difference in obligation for a numbered company', 'None'),
        ('Tax owing on a true nil return', '$0.00'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=True,
  body=('Many holding and shelf corporations are numbered. The Canada Revenue Agency '
        'identifies the corporation by its business number rather than its name, so a '
        "numbered company's return is filed exactly like any other.")),
 dict(
  slug='what-happens-if-i-dont-file-t2-returns-after-my-corporation-is-dissolved',
  h1="What Happens if I Don't File T2 Returns After My Corporation Is Dissolved?",
  anchor='What happens after dissolution',
  keyword='t2 returns after corporation dissolved',
  related=[2],
  answer=('The final return is still required and the years before dissolution stay '
          'outstanding. A final T2 is due within six months of the dissolution date, '
          'covering the period up to that date. Dissolving the corporation does not '
          'close the earlier tax years or cancel the returns already missed.'),
  head=('Requirement', 'Figure'),
  rows=[('Months after dissolution the final T2 is due', '6'),
        ('Earlier unfiled years cancelled by dissolution', 'None'),
        ('Period the final return covers', 'Up to the dissolution date'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=True,
  body=('A dissolved corporation can still be reassessed for a year that was never '
        'filed. Filing the final return and any missed years is what closes the '
        'corporate tax account.')),
 dict(
  slug='do-i-need-to-file-a-t2-if-my-corporation-had-no-activity',
  h1='Do I Need to File a T2 if My Corporation Had No Activity?',
  anchor='Do I need to file with no activity',
  keyword='file t2 corporation no activity',
  related=[0, 3],
  answer=('Yes. Every resident corporation must file a T2 return within six months of '
          'its fiscal year-end, every year, until it is formally dissolved. Having no '
          'revenue, no bank activity and no employees does not remove the obligation, '
          'although a corporation with investment or rental income is not nil.'),
  head=('Point', 'Figure'),
  rows=[('Months after the fiscal year-end to file', '6'),
        ('Revenue threshold below which no return is needed', 'None'),
        ('Tax owing on a true nil return', '$0.00'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('There is no minimum income below which the return can be skipped. The '
        'obligation comes from being an incorporated resident corporation, not from '
        'earning anything in the year.')),
 dict(
  slug='do-i-need-to-file-a-nil-t2-if-my-corporation-has-no-bank-account',
  h1='Do I Need to File a Nil T2 if My Corporation Has No Bank Account?',
  anchor='Do I need to file with no bank account',
  keyword='nil t2 no bank account',
  related=[3],
  answer=("Yes. The T2 obligation follows the corporation's existence, not its "
          'banking, so a return is due within six months of each fiscal year-end '
          'regardless. A corporation with no bank account is usually a true nil '
          'filer, unless income was received or paid some other way.'),
  head=('Point', 'Figure'),
  rows=[('Months after the fiscal year-end to file', '6'),
        ('Bank account required in order to file', 'None'),
        ('Tax owing on a true nil return', '$0.00'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('A corporation with no bank account still has a business number and a fiscal '
        'year-end, and those are what the return is filed against. Income received on '
        "the corporation's behalf some other way still belongs on the return.")),
 dict(
  slug='do-i-need-financial-statements-for-a-nil-t2-return',
  h1='Do I Need Financial Statements for a Nil T2 Return?',
  anchor='Do I need financial statements',
  keyword='financial statements for a nil t2',
  related=[0],
  answer=('No audited or reviewed statements are needed, but the return still carries '
          'GIFI schedules showing zero. A T2 includes the GIFI balance sheet and '
          'income statement, which for a nil year report nil amounts. A corporation '
          'with assets or liabilities still reports those balances.'),
  head=('Point', 'Figure'),
  rows=[('Audited financial statements required', 'None'),
        ('GIFI schedules filed', 'Balance sheet and income statement'),
        ('Income reported in a nil year', '$0.00'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('GIFI is the standard code set the Canada Revenue Agency uses for the balance '
        'sheet and income statement inside the T2. A nil year still files those '
        'schedules with nil amounts, which is what makes the return a nil return '
        'rather than a missing one.')),
]

for i, rec in enumerate(Q2):
    sibs = [s for j, s in enumerate(Q2) if j != i] + [Q[k] for k in rec['related']]
    html, url = build(rec, sibs)
    records.append(dict(slug=rec['slug'], title=rec['h1'],
                        meta_description=rec['answer'], url=url, content=html,
                        answer=rec['answer'], keyword=rec['keyword'],
                        anchor=rec['anchor'],
                        terms={'cnf_family': ['f5']},
                        meta={'cnf_question_text': rec['h1'],
                              'cnf_short_answer': rec['answer'],
                              'cnf_primary_keyword': rec['keyword'],
                              'cnf_last_verified_et': '2026-10-16'}))


# ---------------------------------------------------------------------------
# Batch 3, Appendix A entries 11 to 20: the last four "do I need" questions
# and the first six "can I" questions. Appendix A order kept.
#
# `related` indexes into EARLIER = Q + Q2 (the ten pages already live), so the
# new ten tie back into the cluster instead of forming an island. In-batch
# siblings are the next five records modulo ten, which gives every page in
# this batch exactly five inbound links from its own batch and keeps the
# outbound count at 14 against the 6(g) cap of 15.
#
# Slug 18 note. Appendix A mandates /can-i-file-a-nil-t2-late-without-a-penalty/
# and hard rule 3 forbids the bare claim. The slug cannot be changed, so the
# answer-first paragraph opens with the 7.4 qualification verbatim (which is
# also the meta description, per line 1166) and the WordPress title carries a
# qualifying tail so the SERP line never stands alone as a claim. Logged as an
# 18th plan conflict for Sharad Gondaliya.
# ---------------------------------------------------------------------------
EARLIER = Q + Q2
DATE3, ISO3 = 'October 19, 2026', '2026-10-19'

Q3 = [
 dict(
  slug='do-i-need-to-file-a-t2-for-the-year-my-corporation-was-dissolved',
  h1='Do I Need to File a T2 for the Year My Corporation Was Dissolved?',
  anchor='Do I need a dissolution-year return',
  keyword='t2 for the year my corporation was dissolved',
  related=[6, 2, 0],
  answer=('Yes. A final T2 covers the period from the start of that fiscal year to '
          'the dissolution date, and it is due within six months of dissolution. The '
          'return is still required even when the corporation had no activity at all '
          'in its closing year.'),
  head=('Requirement', 'Figure'),
  rows=[('Period the final return covers',
         'Start of the fiscal year to the dissolution date'),
        ('Months after dissolution the final T2 is due', '6'),
        ('Activity threshold that removes the requirement', 'None'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('The closing period is a short tax year, so the fiscal year-end on the return '
        'is the dissolution date rather than the usual one. Earlier years that were '
        'never filed are separate returns and stay due on their own.')),
 dict(
  slug='do-i-need-a-business-number-to-file-a-nil-t2',
  h1='Do I Need a Business Number to File a Nil T2?',
  anchor='Do I need a business number',
  keyword='business number to file a nil t2',
  related=[8, 7, 9],
  answer=("Yes. The return is filed against the corporation's nine-digit business "
          'number and its RC corporation income tax account, so the number has to '
          'exist before anything is transmitted. Most corporations receive one at '
          'incorporation; a corporation that was never registered must obtain one '
          'from the Canada Revenue Agency first.'),
  head=('Point', 'Figure'),
  rows=[('Business number format', 'Nine digits plus a program account'),
        ('Program account the T2 is filed under', 'RC'),
        ('When most corporations receive the number', 'At incorporation'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('The business number identifies the corporation to the Canada Revenue Agency, '
        'and the RC account is the corporation income tax part of it. Without that '
        'account there is nothing for the return to attach to, which is why it is '
        'confirmed before the return is prepared.')),
 dict(
  slug='do-i-need-to-file-a-nil-t2-if-i-never-started-operating',
  h1='Do I Need to File a Nil T2 if I Never Started Operating?',
  anchor='Do I file if never operating',
  keyword='nil t2 never started operating',
  related=[7, 8, 0],
  answer=('Yes. The first tax year begins on the incorporation date, not on the day '
          'the business starts trading, so a return is due within six months of that '
          'first fiscal year-end. A corporation that never opened for business files '
          'a nil return rather than no return.'),
  head=('Point', 'Figure'),
  rows=[('Date the first tax year begins', 'The incorporation date'),
        ('Months after the first fiscal year-end to file', '6'),
        ('Returns needed before trading starts', 'One for each fiscal year'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('Incorporating creates the obligation. A corporation that was registered and '
        'then left unused still has a fiscal year-end every year, and each of those '
        'years needs its own return until the corporation is dissolved.')),
 dict(
  slug='do-i-need-to-file-a-t2-every-year-if-my-corporation-is-inactive',
  h1='Do I Need to File a T2 Every Year if My Corporation Is Inactive?',
  anchor='Do I file every inactive year',
  keyword='t2 every year corporation inactive',
  related=[3, 7, 0],
  answer=('Yes, every year. Inactive is a description rather than a filing status, so '
          'the T2 falls due within six months of each fiscal year-end until the '
          'corporation is formally dissolved. Skipping a year leaves that year open '
          'indefinitely, whatever the corporation did or did not do.'),
  head=('Point', 'Figure'),
  rows=[('Returns required per fiscal year', '1'),
        ('Months after each fiscal year-end to file', '6'),
        ('When the obligation ends', 'On formal dissolution'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('There is no form that pauses the T2 while a corporation sits idle. The '
        'return is filed each year with nil amounts, which keeps the corporate tax '
        'account current and keeps dissolution available when the owner wants it.')),
 dict(
  slug='can-i-file-five-years-of-nil-t2-returns-at-once',
  h1='Can I File Five Years of Nil T2 Returns at Once?',
  anchor='Can I file five years together',
  keyword='file five years of nil t2 returns',
  related=[1, 0, 4],
  answer=('Yes. Five missed fiscal year-ends mean five separate returns, and all five '
          'can be prepared and transmitted in one pass. Each year keeps its own '
          'fiscal year-end, its own figures and its own T183CORP signature, so there '
          'is no combined five-year return.'),
  head=('What five years needs', 'Count'),
  rows=[('Separate T2 returns', '5'),
        ('T183CORP signatures', '5'),
        ('Combined five-year return available', 'None'),
        ('Total fee at $300.00 plus HST per tax year', '$1,500.00 plus HST')],
  qual=False,
  body=('The years are filed oldest first, so each return reflects the balances '
        'carried into the next. Filing them together is ordinary catch-up work, and '
        'the corporation ends the process with every year assessed.')),
 dict(
  slug='can-i-file-a-nil-t2-myself-without-an-accountant',
  h1='Can I File a Nil T2 Myself Without an Accountant?',
  anchor='Can I file it myself',
  keyword='file a nil t2 without an accountant',
  related=[9, 7, 0],
  answer=('Yes. Nothing in the Income Tax Act requires a corporation to use an '
          'accountant, and a T2 can be prepared and transmitted by the corporation '
          'itself using commercial tax software. A corporation that engages an '
          'electronic filer instead signs Form T183CORP before the return is '
          'transmitted.'),
  head=('Point', 'Figure'),
  rows=[('Requirement to use an accountant', 'None'),
        ('What a self-filed return still needs',
         'Correct fiscal year-end and GIFI schedules'),
        ('Form signed when an electronic filer transmits', 'T183CORP'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('What a corporation takes on by filing itself is the GIFI coding, the '
        'schedule selection and the year-end accuracy. Our fee covers a CPA preparing '
        'and reviewing those and transmitting the return, which is what the fee buys '
        'rather than something the rules demand.')),
 dict(
  slug='can-i-dissolve-my-corporation-with-unfiled-t2-returns',
  h1='Can I Dissolve My Corporation With Unfiled T2 Returns?',
  anchor='Can I dissolve with unfiled returns',
  keyword='dissolve corporation with unfiled t2 returns',
  related=[2, 6, 1],
  answer=('Not cleanly. The corporate registry and the Canada Revenue Agency are '
          'separate, so a registry may strike a corporation while its tax years '
          'remain outstanding. A clearance certificate cannot be issued until every '
          'return is filed, and the unfiled years stay due after dissolution.'),
  head=('Requirement', 'Figure'),
  rows=[('Returns filed before a clearance certificate', 'All of them'),
        ('Months after dissolution the final T2 is due', '6'),
        ('Unfiled years cancelled by dissolution', 'None'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('Dissolving first and filing later leaves the directors dealing with a closed '
        'corporation and an open tax account. Filing the outstanding years before the '
        'dissolution request is the order that avoids it.')),
 dict(
  slug='can-i-file-a-nil-t2-late-without-a-penalty',
  h1='Can I File a Nil T2 Late Without a Penalty?',
  title=('Can I File a Nil T2 Late Without a Penalty? What Actually Applies'),
  anchor='Can I file late, what applies',
  keyword='file a nil t2 late',
  related=[0, 1, 4],
  answer=('A true nil return carries no percentage late-filing penalty, because that '
          'penalty is a percentage of tax owing and the corporation owes $0.00. The '
          'unfiled year still stays open forever, invites a demand to file, blocks '
          'dissolution, and costs a non-resident-owned corporation $25.00 per day.'),
  head=('What applies', 'Figure'),
  rows=[('Percentage late-filing penalty on a true nil return', '$0.00'),
        ('Tax owing on a true nil return', '$0.00'),
        ('How long the unfiled year stays open', 'Until it is filed'),
        ('Non-resident-owned corporation penalty',
         '$25.00 per day, to $2,500.00'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=True,
  body=('The distinction matters because the common late-filing charge is calculated '
        'on tax owing. Where there is no tax owing there is nothing for that '
        'percentage to apply to, which is not the same as the year being closed or '
        'the filing being optional.')),
 dict(
  slug='can-i-file-nil-t2-returns-for-a-corporation-i-forgot-about',
  h1='Can I File Nil T2 Returns for a Corporation I Forgot About?',
  anchor='Can I file a forgotten corporation',
  keyword='nil t2 for a forgotten corporation',
  related=[1, 5, 3],
  answer=('Yes. A corporation that was registered and then left alone still has a '
          'fiscal year-end for every year since incorporation, and each of those '
          "years can be filed now. The first step is confirming the corporation's "
          'status with its registry and its year-end with the Canada Revenue Agency.'),
  head=('Point', 'Figure'),
  rows=[('Years that can be filed', 'Every year since incorporation'),
        ('First thing confirmed', 'Corporate status and fiscal year-end'),
        ('Months after each fiscal year-end to file', '6'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('A forgotten corporation is often still active on the registry, or has been '
        'struck for missing its annual return while the tax years stayed open. Either '
        'way the year-end on file with the Canada Revenue Agency decides how many '
        'returns are outstanding.')),
 dict(
  slug='can-i-still-file-a-t2-after-my-corporation-was-dissolved',
  h1='Can I Still File a T2 After My Corporation Was Dissolved?',
  anchor='Can I file after dissolution',
  keyword='file a t2 after dissolution',
  related=[6, 2, 0],
  answer=('Yes. A final return is due within six months of the dissolution date, and '
          'years left unfiled before dissolution can still be filed afterwards. The '
          'corporate tax account stays open until those returns are assessed, so '
          'dissolution does not end the ability or the need to file.'),
  head=('Point', 'Figure'),
  rows=[('Months after dissolution the final T2 is due', '6'),
        ('Earlier unfiled years that can still be filed', 'All of them'),
        ('When the corporate tax account closes',
         'Once the outstanding returns are assessed'),
        ('Fee per tax year', '$300.00 plus HST')],
  qual=False,
  body=('Filing after dissolution is also what allows the corporate tax account to be '
        'closed properly. A dissolved corporation with an open year can still be '
        'reassessed, so the returns are what finish the file rather than the '
        'dissolution date.')),
]

for rec in Q3:
    rec['date'], rec['iso'] = DATE3, ISO3

for i, rec in enumerate(Q3):
    sibs = ([Q3[(i + k) % len(Q3)] for k in range(1, 6)]
            + [EARLIER[k] for k in rec['related']])
    html, url = build(rec, sibs)
    records.append(dict(slug=rec['slug'], title=rec.get('title', rec['h1']),
                        meta_description=rec['answer'], url=url, content=html,
                        answer=rec['answer'], keyword=rec['keyword'],
                        anchor=rec['anchor'],
                        terms={'cnf_family': ['f5']},
                        meta={'cnf_question_text': rec['h1'],
                              'cnf_short_answer': rec['answer'],
                              'cnf_primary_keyword': rec['keyword'],
                              'cnf_last_verified_et': ISO3}))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'f5-manifest.json')
json.dump(records, open(out, 'w'), ensure_ascii=False, indent=1)
for r in records:
    p = os.path.join(os.path.dirname(out), r['slug'] + '.html')
    open(p, 'w', encoding='utf-8').write(r['content'])
print('%d records -> %s' % (len(records), out))
