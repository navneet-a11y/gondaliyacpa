"""Family 4 service x place pages for British Columbia.

Modelled on the twelve Ontario pages (512, 715-719, 912, 914-918): same
stylesheet, same section order, same schema shape, same closing furniture.

Two deliberate differences from the Ontario siblings, both logged:

 1. No HST computation. Ontario's pages carry "plus $39.00 HST at 13 per cent,
    so $339.00". British Columbia is not an HST province, so the arithmetic
    would be wrong. These pages carry the price string only and say tax is
    added at the rate for the province. The underlying "plus HST" wording
    question is still open with Sharad Gondaliya.
 2. The 7.5 rule 3 byline, with the membership number. The Ontario siblings
    carry the shorter "By Sharad Gondaliya, CPA", which does not satisfy that
    rule. New pages are written to the rule rather than to the defect.

The data table carries verifiable British Columbia rules. The Ontario pages
quote two CRA counts; the CRA publishes dollar amounts by jurisdiction rather
than counts, so those two figures could not be reproduced for BC and are not
invented here.
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
HUB  = SITE + '/british-columbia/'
PLACE, SHORT = 'British Columbia', 'BC'
TODAY, ISO = 'October 21, 2026', '2026-10-21'

REGISTRY = 'BC Registries and Online Services'
ANNUAL_DUE = 'within two months after each anniversary of the date of incorporation'
STATUTE = 'Section 51 of the Business Corporations Act'
STRIKE = 'Two consecutive years of non-filing'

CSS = """<style>.cnf-hero{background-image:linear-gradient(rgba(11,26,51,.82),rgba(11,26,51,.82)),url('https://corpnilfilingfor300.ca/wp-content/uploads/2026/09/business-executives-having-meeting_1098-18316.jpg');background-size:cover;background-position:center center;background-repeat:no-repeat;padding:40px 20px}
.cnf-hero-in{max-width:1140px;margin:0 auto;text-align:left}
.cnf-hero h1{color:#fff;font-family:Poppins,sans-serif;font-weight:700;font-size:40px;line-height:1.25;margin:0}
.cnf-hero .cnf-hero-sub{color:#fff;font-family:Poppins,sans-serif;font-weight:600;font-size:25px;margin:10px 0 0}
.cnf-hero .cnf-hero-lede{color:#fff;font-family:Lato,sans-serif;font-size:17px;line-height:1.6;margin:10px 0 0;max-width:860px}
.cnf-hero .cnf-hero-btn{display:inline-block;background:#314d8a;color:#fff!important;padding:20px 50px;border-radius:35px;font-family:Poppins,sans-serif;font-weight:600;font-size:18px;text-decoration:none!important;margin:24px 0 0}
.cnf-hero .cnf-hero-btn:hover,.cnf-hero .cnf-hero-btn:focus{background:#2087c9;color:#fff!important;text-decoration:none!important}
@media(max-width:767px){.cnf-hero{padding:32px 16px}.cnf-hero h1{font-size:28px}.cnf-hero .cnf-hero-sub{font-size:20px}.cnf-hero .cnf-hero-btn{padding:16px 34px;font-size:16px}}
.entry-header{display:none!important}
.ast-article-single,.ast-article-single .entry-content{margin-top:0;padding-top:0}
.cnf-w{max-width:1000px;margin:0 auto;padding:36px 20px 56px;font-family:Lato,sans-serif;color:#333;font-size:17px;line-height:1.65}
.cnf-w h2{font-family:Poppins,sans-serif;color:#314d8a;font-size:26px;font-weight:600;margin:40px 0 12px}
.cnf-w a{color:#314d8a;font-weight:600}.cnf-w a:hover{color:#2087c9}
.cnf-crumb{font-size:14px;color:#636363}.cnf-crumb a{font-weight:400;text-decoration:none}
.cnf-by{font-size:15px;margin:6px 0 0}.cnf-rev{font-size:15px;color:#636363;margin:2px 0 18px}
.cnf-tbl{width:100%;border-collapse:collapse;font-size:16px}.cnf-tbl th,.cnf-tbl td{border:1px solid #dfe6ef;padding:12px 14px;text-align:left;vertical-align:top}
.cnf-tbl th{background:#314d8a;color:#fff;font-family:Poppins,sans-serif;font-weight:600}.cnf-tbl td:nth-child(2){font-weight:700;color:#314d8a}
.cnf-cap{font-size:14px;color:#636363;margin-top:8px}
.cnf-box{background:#f5f8fc;border-left:5px solid #314d8a;border-radius:8px;padding:18px 22px}
.cnf-btn{display:inline-block;background:#314d8a;color:#fff!important;padding:16px 36px;border-radius:35px;font-family:Poppins,sans-serif;font-weight:600;text-decoration:none;margin:8px 12px 8px 0}.cnf-btn:hover{background:#2087c9}
.cnf-foot{text-align:center;font-size:15px;color:#636363;border-top:1px solid #dfe6ef;padding-top:18px;margin-top:40px}</style>"""

NOT_NIL_1 = ('This service is for a corporation with no activity in the tax year. A '
             'corporation with investment income, rental income, or dividends paid or '
             'received is not nil.')
NOT_NIL_2 = ('Other cases that are not nil include a corporation that is not a '
             'Canadian-controlled private corporation, an amalgamation, or a '
             'corporation already dissolved or struck. We route you to our sister '
             'office at gondaliyacpa.ca at $350.00 plus HST per tax year before you '
             'pay. If we find it after you pay, we refund you in full.')

def a(h, t):
    return '<a href="%s">%s</a>' % (h, t)


SERVICES = [
 dict(
  slug='nil-t2-filing-british-columbia',
  service='nil-t2-filing',
  title='Nil T2 Filing in British Columbia',
  keyword='nil t2 filing british columbia',
  national=('/nil-t2-filing/', 'nil T2 filing'),
  lead_h2='Nil T2 Filing for British Columbia Corporations',
  lead=['A nil T2 is the corporate income tax return a British Columbia '
        'corporation files for a tax year in which it had no activity. Every '
        'British Columbia corporation files a T2 with the Canada Revenue Agency '
        'within six months of its fiscal year-end, every year until it is formally '
        'dissolved, whether or not it earned anything. British Columbia corporate '
        'income tax is reported on the federal T2, so there is no separate British '
        'Columbia corporate income tax return to file alongside it. We prepare the '
        'return, a CPA reviews it, and we transmit it electronically for $300.00 '
        'plus HST per tax year.'],
  extra=[('What Makes a Return Nil',
          ['A nil return reports no income and no expenses for the tax year. The '
           'corporation still exists, still has a Business Number, and still has a '
           'fiscal year-end, so the return is still due. Filing it keeps the '
           'corporation&rsquo;s tax record current and keeps its standing with the '
           'Canada Revenue Agency intact.',
           'The British Columbia annual report is a separate filing, made with '
           + REGISTRY + '. It confirms the company&rsquo;s directors and registered '
           'office, carries no tax, and is not covered by the $300.00 fee.'])],
  excerpt='Nil T2 filing for British Columbia corporations with no activity in the '
          'tax year. $300.00 plus HST per tax year.'),

 dict(
  slug='catch-up-nil-t2-filing-british-columbia',
  service='catch-up-nil-t2-filing',
  title='Catch-Up Nil T2 Filing in British Columbia',
  keyword='catch-up nil t2 filing british columbia',
  national=('/catch-up-nil-t2-filing/', 'catch-up nil T2 filing'),
  lead_h2='Bringing Unfiled British Columbia Years Up to Date',
  lead=['If a British Columbia corporation has not filed for several years, each of '
        'those years is still outstanding and each one is a separate return. We file '
        'them together, oldest year first, so the Canada Revenue Agency processes '
        'them in the order they fell due. Each tax year is $300.00 plus HST, because '
        'each tax year is its own T2.'],
  extra=[('Why the Oldest Year Goes First',
          ['A T2 carries forward figures from the year before it, so the years have '
           'to be assessed in order. Filing the oldest outstanding year first means '
           'each later return is assessed against a record that is already up to '
           'date, rather than against a gap.',
           'You tell us which years are unfiled and confirm the corporation had no '
           'activity in each of them. If any year turns out not to be nil, we tell '
           'you before you pay for that year.'])],
  excerpt='Catch up every unfiled year for a British Columbia corporation, oldest '
          'year first. $300.00 plus HST per tax year.'),

 dict(
  slug='dormant-corporation-filing-british-columbia',
  service='dormant-corporation-filing',
  title='Dormant Corporation Filing in British Columbia',
  keyword='dormant corporation filing british columbia',
  national=('/dormant-corporation-filing/', 'dormant corporation filing'),
  lead_h2='Keeping a Dormant British Columbia Corporation Up to Date',
  lead=['A dormant British Columbia corporation is one that still exists on the '
        'register but has stopped trading, or never started. Being dormant does not '
        'pause anything. The corporation still files a T2 with the Canada Revenue '
        'Agency within six months of each fiscal year-end, and still files its '
        'British Columbia annual report with ' + REGISTRY + ', every year until it '
        'is formally dissolved. If the dormant corporation had no activity in the '
        'tax year, we file its nil T2 for $300.00 plus HST. Filing does not dissolve '
        'the corporation. It keeps the corporation&rsquo;s tax record clean while you '
        'decide whether to restart it or close it.'],
  extra=[('Dormant Is Not the Same as Dissolved',
          ['A British Columbia corporation stays in existence until it is dissolved. '
           'Until then every filing obligation continues. A dormant corporation that '
           'also stops filing its annual report loses its good standing, so the '
           'registry will not issue a certificate of good standing for it, and after '
           'two consecutive years of non-filing the registrar may dissolve the '
           'company. None of that cancels an outstanding T2: the corporate tax '
           'account and the registry record are separate trails.',
           'If you plan to close the corporation instead, see our '
           + a(SITE + '/final-t2-before-dissolution-british-columbia/',
               'final T2 before dissolution in British Columbia') + '.'])],
  excerpt='Nil T2 filing for dormant British Columbia corporations with no activity '
          'in the tax year. $300.00 plus HST per tax year.'),

 dict(
  slug='final-t2-before-dissolution-british-columbia',
  service='final-t2-before-dissolution',
  title='Final T2 Before Dissolution in British Columbia',
  keyword='final t2 before dissolution british columbia',
  national=('/final-t2-before-dissolution/', 'final T2 before dissolution'),
  lead_h2='The Last Return Before a British Columbia Corporation Is Dissolved',
  lead=['A corporation being wound up files one last T2, covering the period that '
        'ends on the date of dissolution. It is due within six months of that date. '
        'If the corporation had no activity in that final period, we file it as a '
        'nil return for $300.00 plus HST.'],
  extra=[('Clear the Earlier Years First',
          ['Unfiled years block a clearance certificate, and they block the '
           'dissolution itself, so the final return is rarely the only one '
           'outstanding. Where earlier years are also unfiled we file them together, '
           'oldest year first, each as its own return at the same fee.',
           'Dissolving the company is a separate step, taken with ' + REGISTRY +
           '. It is not covered by the $300.00 fee, and filing the final T2 does not '
           'dissolve the corporation on its own.'])],
  excerpt='The final T2 for a British Columbia corporation being wound up, due '
          'within six months of dissolution. $300.00 plus HST per tax year.'),

 dict(
  slug='t2-short-filing-british-columbia',
  service='t2-short-filing',
  title='T2 Short Filing in British Columbia',
  keyword='t2 short filing british columbia',
  national=('/t2-short-filing/', 'T2 Short filing'),
  lead_h2='The Two-Page T2 Short for British Columbia Corporations',
  lead=['The T2 Short is a two-page version of the T2 return. A British Columbia '
        'corporation may use it only where it meets every one of the Canada Revenue '
        'Agency&rsquo;s conditions for the short return. Where it qualifies, we file '
        'it, and it is included in the $300.00 plus HST fee rather than charged '
        'separately.'],
  extra=[('We Check Before We File',
          ['Meeting most of the conditions is not enough, so we check every one of '
           'them against your corporation before we prepare the return. Where the '
           'corporation does not qualify, we file the full T2 instead, at the same '
           'fee.',
           'Either way the return is reviewed by a CPA and transmitted '
           'electronically to the Canada Revenue Agency.'])],
  excerpt='T2 Short filing for British Columbia corporations that meet every CRA '
          'condition for the short return. $300.00 plus HST per tax year.'),
 dict(
  slug='unfiled-corporate-tax-returns-british-columbia',
  reviewed='October 23, 2026', reviewed_iso='2026-10-23',
  service='unfiled-corporate-tax-returns',
  title='Unfiled Corporate Tax Returns in British Columbia',
  keyword='unfiled corporate tax returns british columbia',
  national=('/catch-up-nil-t2-filing/', 'catch-up nil T2 filing'),
  lead_h2='Unfiled Years for a British Columbia Corporation',
  lead=['An unfiled T2 year does not close itself. It stays open on the '
        'corporation&rsquo;s record indefinitely, and no number of later filings '
        'settles it. A British Columbia corporation with four unfiled years owes '
        'four returns, each for its own tax year, at $300.00 plus HST per tax '
        'year.'],
  extra=[('What an Unfiled Year Costs',
          ['A true nil return carries no percentage late-filing penalty, because '
           'that penalty is a percentage of tax owing and the corporation owes '
           '$0.00. The unfiled year still stays open forever, invites a demand to '
           'file and an arbitrary assessment, blocks a clearance certificate and '
           'dissolution, and costs a non-resident-owned corporation $25.00 per day '
           'up to $2,500.00.',
           'The cost of leaving a nil year unfiled is almost never a penalty. It is '
           'the demand letter, the arbitrary assessment raised on an estimate the '
           'corporation did not provide, and the dissolution that cannot complete '
           'until every year is filed.']),
         ('The Registry Filing Is Separate',
          ['Two consecutive years without a British Columbia annual report lets the '
           'registrar dissolve the company, and that is a separate failure from an '
           'unfiled T2. A corporation can be fully current with the Canada Revenue '
           'Agency and still be struck from the register.'])],
  excerpt='Bring every unfiled year up to date for a British Columbia corporation. '
          '$300.00 plus HST per tax year.'),

 dict(
  slug='no-activity-corporation-tax-return-british-columbia',
  reviewed='October 23, 2026', reviewed_iso='2026-10-23',
  service='no-activity-corporation-tax-return',
  title='No Activity Corporation Tax Return in British Columbia',
  keyword='no activity corporation tax return british columbia',
  national=('/dormant-corporation-filing/', 'dormant corporation filing'),
  lead_h2='Filing a Year With No Activity in British Columbia',
  lead=['A British Columbia corporation that did nothing at all in a tax year still '
        'files a T2 for that year, within six months of its fiscal year-end. There '
        'is no status to elect that pauses the obligation, and no threshold below '
        'which it stops. The return reports no income and no expenses, and it costs '
        '$300.00 plus HST per tax year.'],
  extra=[('What Counts as No Activity',
          ['No revenue of any kind, no expense claimed, no payroll, no asset bought '
           'or sold, no dividend paid or received, and no inter-company '
           'transaction. Interest credited on a bank balance is income, so a year '
           'with interest in it is not a no-activity year, however small the '
           'amount.',
           'Share capital, cash, a shareholder loan, an incorporation cost or a '
           'bank charge does not stop the year being nil. It does make GIFI '
           'Schedules 100, 125 and 141 required, and those are included in the '
           'fee.'])],
  excerpt='File a no-activity T2 for a British Columbia corporation. $300.00 plus '
          'HST per tax year.'),

 dict(
  slug='numbered-corporation-nil-filing-british-columbia',
  reviewed='October 23, 2026', reviewed_iso='2026-10-23',
  service='numbered-corporation-nil-filing',
  title='Numbered Corporation Nil Filing in British Columbia',
  keyword='numbered corporation nil filing british columbia',
  national=('/nil-t2-filing/', 'nil T2 filing'),
  lead_h2='Nil Filing for a Numbered British Columbia Company',
  lead=['A numbered British Columbia company files exactly as a named one does. The '
        'absence of a trading name changes nothing about the obligation: the T2 is '
        'due within six months of the fiscal year-end, every year, until the '
        'company is formally dissolved. The fee is $300.00 plus HST per tax '
        'year.'],
  extra=[('Why Numbered Companies Fall Behind',
          ['A numbered company is often incorporated to hold a name, a future '
           'structure or a single asset, and then left. Nothing arrives to prompt '
           'anyone, so the first contact is usually a demand to file covering '
           'several years at once.',
           'We file them together, oldest year first, so the Canada Revenue Agency '
           'assesses them in the order they fell due.']),
         ('The Company Number Is the Filing Name',
          ['The return carries the exact legal name as the register holds it, '
           'including the company number and the suffix. A name that does not match '
           'the register is one of the common causes of a rejected transmission, '
           'and one corrected transmission is included in the fee.'])],
  excerpt='Nil T2 filing for a numbered British Columbia company. $300.00 plus HST '
          'per tax year.'),

 dict(
  slug='nil-t2-filing-deadline-british-columbia',
  reviewed='October 23, 2026', reviewed_iso='2026-10-23',
  service='nil-t2-filing-deadline',
  title='Nil T2 Filing Deadline in British Columbia',
  keyword='nil t2 filing deadline british columbia',
  national=('/deadlines/', 'T2 filing deadlines'),
  lead_h2='When a British Columbia Nil T2 Is Due',
  lead=['Within six months of the corporation&rsquo;s fiscal year-end. The deadline '
        'comes from the Income Tax Act and does not vary by province, so a British '
        'Columbia corporation is on the same timetable as one in any other '
        'province. A December 31 year-end is due the following June 30.'],
  extra=[('The Year-End Must Match the Agency&rsquo;s Record',
          ['The Canada Revenue Agency holds a fiscal year-end taken from the '
           'incorporation record. The first tax year cannot exceed 53 weeks and the '
           'year-end must match the Agency&rsquo;s record or the transmission is '
           'rejected.',
           'Where the year-end on file is not the one intended, it is settled with '
           'the Agency before the return is transmitted rather than by filing a '
           'different date.']),
         ('The British Columbia Annual Report Has Its Own Date',
          ['The annual report is filed with ' + REGISTRY + ' ' + ANNUAL_DUE
           + '. It runs from the anniversary of incorporation rather than from the '
           'fiscal year-end, so the two deadlines rarely fall together and missing '
           'one does not show up in the other.'])],
  excerpt='When a nil T2 is due for a British Columbia corporation, and how it '
          'differs from the annual report. $300.00 plus HST per tax year.'),

 dict(
  slug='nil-t2-filing-cost-in-british-columbia',
  cost_h2='What You Pay in British Columbia',
  reviewed='October 23, 2026', reviewed_iso='2026-10-23',
  service='nil-t2-filing-cost',
  title='Nil T2 Filing Cost in British Columbia',
  keyword='nil t2 filing cost british columbia',
  national=('/pricing/nil-t2-filing-cost/', 'nil T2 filing cost'),
  lead_h2='What a Nil T2 Return Costs a British Columbia Corporation',
  lead=['$300.00 plus HST per tax year. Two years is $600.00, three is $900.00 and '
        'five is $1,500.00, each before tax, because each tax year is a separate '
        'return carrying the same preparation and the same CPA review. There is no '
        'reduced rate for filing several years together.',
        'British Columbia is not an HST province, so tax is added at the rate that '
        'applies to your province rather than at a single harmonised rate. British '
        'Columbia corporate income tax is reported on the federal T2, so there is '
        'no second provincial filing fee of the kind an Alberta or Quebec '
        'corporation faces.'],
  extra=[('What the Fee Includes',
          ['One nil T2 for one corporation for one tax year, including the T2 Short '
           'where the corporation qualifies, GIFI Schedules 100, 125 and 141 where '
           'they are required, Schedule 24 on a first return, Schedule 50 for every '
           'shareholder at 10 per cent or more, Schedule 8 and loss continuity, '
           'your Form T183CORP package with single-use secure e-signing, CPA '
           'review, electronic transmission by a registered EFILE electronic filer, '
           'one corrected transmission if the Agency rejects the first one, and '
           'your CRA confirmation emailed within 3 business days.',
           'The price does not change with the age of the year, the size of the '
           'corporation or the number of shareholders.'])],
  excerpt='What a nil T2 return costs a British Columbia corporation. $300.00 plus '
          'HST per tax year.'),

 dict(
  slug='nil-t2-filing-for-non-resident-owned-corporations-british-columbia',
  reviewed='October 23, 2026', reviewed_iso='2026-10-23',
  service='nil-t2-filing-for-non-resident-owned-corporations',
  title='Nil T2 Filing for Non-Resident-Owned Corporations in British Columbia',
  keyword='non-resident owned corporation nil t2 british columbia',
  national=('/nil-t2-filing/', 'nil T2 filing'),
  lead_h2='Non-Resident-Owned British Columbia Corporations',
  lead=['A British Columbia corporation owned from outside Canada files a T2 on the '
        'same timetable as any other: within six months of its fiscal year-end, '
        'every year, until it is formally dissolved. The fee is $300.00 plus HST '
        'per tax year, and the whole process is completed online.'],
  extra=[('The Penalty That Does Not Depend on Tax Owing',
          ['A true nil return carries no percentage late-filing penalty, because '
           'that penalty is a percentage of tax owing and the corporation owes '
           '$0.00. The unfiled year still stays open forever, invites a demand to '
           'file and an arbitrary assessment, blocks a clearance certificate and '
           'dissolution, and costs a non-resident-owned corporation $25.00 per day '
           'up to $2,500.00.',
           'That daily charge is built on days rather than on tax owing, so a nil '
           'year reaches the maximum exactly as a trading year does. It is the '
           'largest single exposure a dormant non-resident-owned corporation '
           'carries.']),
         ('Signing From Outside Canada',
          ['Form T183CORP is signed by an authorized signing officer before '
           'transmission, and it may be signed through an access-controlled secure '
           'portal. There is no requirement to be in Canada, and no meeting is '
           'needed at any point.'])],
  excerpt='Nil T2 filing for a non-resident-owned British Columbia corporation, and '
          'the $25.00 a day exposure. $300.00 plus HST per tax year.'),

 dict(
  slug='inactive-holding-corporation-t2-filing-british-columbia',
  reviewed='October 23, 2026', reviewed_iso='2026-10-23',
  service='inactive-holding-corporation-t2-filing',
  title='Inactive Holding Corporation T2 Filing in British Columbia',
  keyword='inactive holding corporation t2 filing british columbia',
  national=('/inactive-holding-corporation-t2-filing/',
            'inactive holding corporation T2 filing'),
  lead_h2='When a British Columbia Holding Corporation Is Nil',
  lead=['A holding corporation with investment income, a rental corporation and a '
        'corporation that paid or received a dividend are not nil. Those are '
        'handled by Gondaliya CPA Professional Corporation at gondaliyacpa.ca at '
        '$350.00 plus HST per year.',
        'A British Columbia holding corporation is nil for this service only where '
        'it held its assets through the whole tax year and they earned nothing at '
        'all: no dividend received, no dividend paid, no rent, no interest and no '
        'inter-company transaction. That corporation still files a T2 within six '
        'months of its fiscal year-end, at $300.00 plus HST per tax year.'],
  extra=[('The Interest a Holding Corporation Forgets',
          ['The most common reason a holding corporation believed to be nil is not '
           'nil is a few dollars of interest credited on a bank balance nobody '
           'looked at. There is no minimum. Interest credited across the year is '
           'investment income, and the year is not nil.',
           'We check the position before you pay. If the year turns out not to be '
           'nil, we tell you first, and if it is found after you pay we refund you '
           'in full.']),
         ('Schedules a Holding Corporation Still Files',
          ['A holding corporation holds assets by definition, so GIFI Schedules '
           '100, 125 and 141 are required on most of its returns despite there '
           'being no activity. Schedule 50 is required for every shareholder at 10 '
           'per cent or more, and holding structures concentrate ownership, so it '
           'is almost always needed.'])],
  excerpt='When a British Columbia holding corporation is nil and when it is not. '
          '$300.00 plus HST per tax year.'),

]


def build(s):
    url = SITE + '/' + s['slug'] + '/'
    b = ['<!-- wp:html -->', CSS + '<div class="cnf-hero"><div class="cnf-hero-in">'
         '<h1>' + s['title'] + '</h1><p class="cnf-hero-sub">$300.00 Plus HST Per Tax '
         'Year</p><p class="cnf-hero-lede">We are a registered EFILE electronic filer. '
         'Your return is transmitted to the Canada Revenue Agency electronically.</p>'
         '<p><a class="cnf-hero-btn" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
         '</p></div></div>']
    b.append('<div class="cnf-w">')
    b.append('<nav class="cnf-crumb" aria-label="Breadcrumb">'
             + a(SITE + '/', 'Nil T2 filing in Canada') + ' &rsaquo; '
             + a(HUB, 'Nil T2 filing in ' + PLACE) + ' &rsaquo; '
             '<span aria-current="page">' + s['title'] + '</span></nav>')
    # 7.5 rule 3: these pages state filing rules and a T183CORP rule
    b.append('<p class="cnf-by">Written and reviewed by '
             + a(SITE + '/sharad-gondaliya-cpa/', 'Sharad Gondaliya, CPA (Ontario)')
             + ', CPA Ontario Membership 61040184.</p>')
    b.append('<p class="cnf-rev">Last reviewed: ' + s.get('reviewed', TODAY)
             + '</p>')

    b.append('<h2>' + s['lead_h2'] + '</h2>')
    for p in s['lead']:
        b.append('<p>' + p + '</p>')

    b.append('<h2>' + PLACE + ' Data</h2>')
    b.append('<table class="cnf-tbl"><thead><tr><th scope="col">Item</th>'
             '<th scope="col">' + PLACE + '</th><th scope="col">Source</th></tr>'
             '</thead><tbody>')
    for item, val, src in [
      ('T2 filing deadline', 'Within six months of the fiscal year-end',
       'Income Tax Act'),
      ('Separate provincial corporate income tax return',
       'None, collected through the federal T2', 'Income Tax Act'),
      ('Registry', REGISTRY, REGISTRY),
      ('Annual report due', ANNUAL_DUE[0].upper() + ANNUAL_DUE[1:], STATUTE),
      ('Registrar may dissolve the company after', STRIKE, REGISTRY),
      ('Filing route', 'T2 transmitted electronically to the Canada Revenue Agency '
       'by a registered EFILE electronic filer', 'Canada Revenue Agency')]:
        b.append('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (item, val, src))
    b.append('</tbody></table>')
    b.append('<p class="cnf-cap">' + PLACE + ' registry rules confirmed ' + TODAY
             + ' against ' + REGISTRY + '. The T2 due date comes from the Income Tax '
             'Act and does not vary by province.</p>')

    for h2, paras in s['extra']:
        b.append('<h2>' + h2 + '</h2>')
        for p in paras:
            b.append('<p>' + p + '</p>')

    b.append('<h2>Who This Is For</h2>')
    b.append('<p>' + NOT_NIL_1 + '</p>')
    b.append('<p>' + NOT_NIL_2 + '</p>')

    b.append('<h2>How ' + s['title'] + ' Works</h2>')
    b.append('<ol><li>Type your corporation name. We fill the Business Number and '
             'incorporation date.</li><li>Pick the tax years to file and confirm the '
             'corporation had no activity in each of them.</li><li>Complete the '
             'attestation and identity check, then pay $300.00 plus HST per tax '
             'year.</li><li>Sign Form T183CORP. We transmit your return '
             'electronically.</li></ol>')
    b.append('<p>Your CRA confirmation is emailed within 3 business days. Business '
             'days are Monday to Friday and exclude ' + PLACE
             + ' statutory holidays.</p>')

    # The generic heading is "<service> Cost in <place>", which doubles the word
    # on a service already named "... Cost" and repeats the H1 verbatim if the
    # word is simply dropped. Those pages name their own heading instead.
    b.append('<h2>' + s.get('cost_h2', s['title'].replace(' in ' + PLACE, '')
                            + ' Cost in ' + PLACE) + '</h2>')
    b.append('<p>$300.00 plus HST per tax year. Each tax year is a separate return '
             'and carries the same fee. Tax is added at the rate for your province. '
             'See the full ' + a(SITE + '/pricing/nil-t2-filing-cost/',
                                 'nil T2 filing cost') + '.</p>')

    b.append('<h2>Filings This Does Not Cover</h2>')
    b.append('<div class="cnf-box"><ul>')
    b.append('<li>Your ' + PLACE + ' annual report. It is filed with ' + REGISTRY
             + ' ' + ANNUAL_DUE + ', and it is not covered by the $300.00 fee.</li>')
    b.append('<li>A federal Corporations Canada annual return, at $12.00, if your '
             'corporation is federally incorporated.</li>')
    b.append('<li>A nil GST/HST return or a nil payroll return.</li>')
    b.append('<li>RC145 closure of a GST/HST or payroll account.</li></ul>')
    b.append('<p>We tell you which of these you still owe.</p></div>')

    nh, nl = s['national']
    b.append('<p>Read the national page on ' + a(SITE + nh, nl) + ', or see every '
             + PLACE + ' page on the ' + a(HUB, 'nil T2 filing in ' + PLACE + ' hub')
             + '.</p>')
    b.append('<p><a class="cnf-btn" href="' + FORM + '">Start Nil T2 Filing NOW</a></p>')
    b.append('<p class="cnf-foot">Your return is prepared and transmitted in Canada. '
             'Our credentials are never shared and no part of your file is sent '
             'offshore. ' + a(SITE + '/', 'Nil T2 filing in Canada') + '</p>')
    b.append('</div>')

    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "Service", "@id": url + "#service", "name": s['title'],
       "serviceType": "Nil T2 corporate income tax return filing", "url": url,
       "description": NOT_NIL_1,
       "areaServed": {"@type": "State", "name": PLACE},
       "provider": {"@id": SITE + "/#accountingservice"},
       "offers": {"@type": "Offer", "name": s['title'], "price": "300.00",
                  "priceCurrency": "CAD",
                  "description": "$300.00 plus HST per tax year", "url": FORM,
                  "areaServed": {"@type": "State", "name": PLACE}}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
         "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Nil T2 filing in " + PLACE,
         "item": HUB},
        {"@type": "ListItem", "position": 3, "name": s['title'], "item": url}]}]}
    b.append('<script type="application/ld+json">' + json.dumps(schema) + '</script>')
    b.append('<!-- /wp:html -->')
    return '\n'.join(b)


def meta(s):
    return {
     'site-sidebar-layout': 'no-sidebar', 'site-content-layout': 'page-builder',
     'ast-site-content-layout': 'full-width-container',
     'site-post-title': 'disabled', 'ast-breadcrumbs-content': 'disabled',
     'ast-featured-img': 'disabled',
     'cnf_service_slug': s['service'], 'cnf_place_slug': 'british-columbia',
     'cnf_place_name': PLACE, 'cnf_place_type': 'province',
     'cnf_jurisdiction_return': 'T2',
     'cnf_provincial_return_name':
        'None. British Columbia corporate income tax is reported on the federal T2 '
        'return.',
     # left empty on purpose: BC is not an HST province, so an HST-inclusive
     # figure would be wrong, and the "plus HST" wording is still open
     'cnf_price_incl_hst': '', 'cnf_overflow_price_incl_hst': '',
     'cnf_deadline_rule':
        "The T2 is due within six months of the corporation's fiscal year-end, every "
        "year until the corporation is formally dissolved.",
     'cnf_unique_data_block_json': json.dumps({
        'place': PLACE, 'registry_name': REGISTRY,
        'annual_return_route': 'British Columbia annual report filed with ' + REGISTRY
                               + ' ' + ANNUAL_DUE + ', not covered by the $300.00 fee',
        'annual_return_statute': STATUTE,
        'dissolution_after': STRIKE,
        'provincial_corporate_return': None,
        'filing_route': 'T2 transmitted electronically to the Canada Revenue Agency '
                        'by a registered EFILE electronic filer',
        't2_assessment_count': None,
        't2_assessment_count_source':
            'CRA publishes dollar amounts by jurisdiction, not counts; not available '
            'for BC',
        'hst_rate': None}),
     'cnf_last_verified_et': s.get('reviewed_iso', ISO),
     'cnf_primary_keyword': s['keyword'],
    }


if __name__ == '__main__':
    out = {}
    for s in SERVICES:
        c = build(s)
        io.open(os.path.join(HERE, s['slug'] + '.html'), 'w', encoding='utf-8').write(c)
        out[s['slug']] = len(c.encode('utf-8'))
        print('%-48s %6d bytes   excerpt %d' % (s['slug'], out[s['slug']],
                                                len(s['excerpt'])))
