"""Family 14 content generator: 23 deadline pages.

Produces a publish manifest, one record per URL, with title, slug, meta
description, body HTML, cnf_ post meta and taxonomy terms. Nothing here is
invented: the title and meta description follow the 6(a) exemplar as a formula,
every factual sentence is a plan copy-paste block, and the dates come from
build/f14/dates.py.

Slug note. 6(a) gives /deadlines/t2-due-date-for-december-year-end/ and the
nil_deadline post type is registered with rewrite base "deadlines", so that is
what is used. Appendix A gives root-level slugs of a different shape
(/nil-t2-deadline-for-a-december-31-year-end/). Sixth Appendix A conflict,
logged for Sharad Gondaliya.
"""
import json, sys, os
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dates import MONTHS, last_day, due_date, due_month_name, ontario_holidays, next_business_day

TODAY = '2026-10-15'
PRICE = '$300.00 plus HST per tax year'
FORM  = 'https://corpnilfilingfor300.ca/form/'
CTA   = 'Start Nil T2 Filing NOW'

# Plan copy-paste blocks, used verbatim.
MUST_FILE = ('Every resident corporation, including an inactive one, must file a T2 return within six '
             'months of its fiscal year-end, every year, until it is formally dissolved. A final T2 is '
             'due within six months of dissolution. Having no revenue, no bank activity and no employees '
             'does not remove the obligation.')
LATE_QUAL = ('A true nil return carries no percentage late-filing penalty, because that penalty is a '
             'percentage of tax owing and the corporation owes $0.00. The unfiled year still stays open '
             'forever, invites a demand to file and an arbitrary assessment, blocks a clearance '
             'certificate and dissolution, and costs a non-resident-owned corporation $25.00 per day up '
             'to $2,500.00.')
EFILE = ('We are a registered EFILE electronic filer. Your return is transmitted to the Canada Revenue '
         'Agency electronically, and your CRA confirmation is emailed within 3 business days. Business '
         'days are Monday to Friday and exclude Ontario statutory holidays.')
SCOPE = ('This service is for a corporation with no activity in the tax year. A corporation with '
         'investment income, rental income, or dividends paid or received is not nil.')
# 7.5 byline rule 3: the CPA byline is rendered by the "Single - Deadline"
# Elementor template (one fixed string for all of Family 14), not typed into
# each body. 7.5 last-reviewed rule 1 puts this line under the H1, which is
# the first thing in post_content once the template owns the banner.
LAST_REVIEWED = '<p class="cnf-lastrev">Last reviewed: October 15, 2026</p>\n'

CSS = ("<style>\n"
 ".cnf-dl h2{color:#314D8A;margin-top:32px}\n"
 ".cnf-dl table{width:100%;border-collapse:collapse;margin:18px 0 26px}\n"
 ".cnf-dl th,.cnf-dl td{text-align:left;padding:10px 12px;border-bottom:1px solid #DDE1E8}\n"
 ".cnf-dl th{color:#314D8A}\n"
 ".cnf-dl .cnf-lead{border-left:4px solid #314D8A;padding:2px 0 2px 16px;margin:22px 0;font-size:1.05em}\n"
 ".cnf-dl .cnf-qual{background:#f5f8fc;border-radius:10px;padding:18px 20px;margin:24px 0}\n"
 ".cnf-dl .cnf-cta{display:inline-block;background:#314D8A;color:#FFFFFF !important;text-decoration:none;"
 "padding:14px 28px;border-radius:6px;font-weight:600;margin:8px 0 28px}\n"
 ".cnf-dl .cnf-cta:hover,.cnf-dl .cnf-cta:focus{background:#28406F;color:#FFFFFF !important}\n"
 ".cnf-dl .cnf-lastrev{font-size:.9em;color:#5A6478;margin:0 0 22px}\n"
 "</style>\n")

def article(word):
    return 'An' if word[0].upper() in 'AEIOU' else 'A'

def P(*p): return ''.join(f'<p>{x}</p>\n' for x in p)
def cta(): return f'<p><a class="cnf-cta" href="{FORM}">{CTA}</a></p>\n'

records = []

# ---- 12 month-end pages -------------------------------------------------
for m in range(1, 13):
    ye_day = last_day(2026, m)
    ye_name = f'{MONTHS[m-1]} {ye_day}'
    due_name = due_month_name(m)
    # concrete due dates for the next three tax years, with weekend/holiday shift
    rows = []
    for y in (2025, 2026, 2027):
        dd = due_date(y, m)
        nbd = next_business_day(dd)
        shifted = '' if nbd == dd else f' (falls on a {dd.strftime("%A")}, so {nbd.strftime("%B %d, %Y")})'
        rows.append(f'<tr><td>{MONTHS[m-1]} {last_day(y,m)}, {y}</td>'
                    f'<td>{dd.strftime("%B %d, %Y")}{shifted}</td></tr>')
    due_example = due_date(2026, m)

    title = f'T2 Due Date for a {ye_name} Year-End'
    meta  = (f'{article(ye_name)} {ye_name} year-end makes the T2 due {due_example.strftime("%B %d")}. '
             f'Filing is mandatory even with no activity. Nil T2 filing at {PRICE}.')
    body = (CSS + '<div class="cnf-dl">\n' + LAST_REVIEWED
      + f'<div class="cnf-lead"><p>{article(ye_name)} {ye_name} year-end makes the T2 due '
        f'{due_example.strftime("%B %d")}, six months after the end of the tax year.</p></div>\n'
      + P(MUST_FILE)
      + '<h2>Due dates by tax year</h2>\n'
      + '<table><tr><th>Fiscal year-end</th><th>T2 due</th></tr>\n' + '\n'.join(rows) + '</table>\n'
      + P('Where a due date falls on a Saturday, a Sunday or a public holiday recognised by the Canada '
          'Revenue Agency, a return received the next business day is on time.')
      + '<h2>Filing a nil return for this year-end</h2>\n'
      + P(SCOPE, EFILE)
      + f'<h2>What it costs</h2>\n'
      + P(f'{PRICE}. One price for every year and every province. No hourly billing and no add-on fees.')
      + cta() + '</div>')
    records.append(dict(
        kind='month-end', slug=f't2-due-date-for-{MONTHS[m-1].lower()}-year-end',
        title=title, meta_description=meta, content=body,
        terms={'cnf_family': ['f14']},
        meta={'cnf_fiscal_year_end': ye_name,
              'cnf_t2_due_date': due_example.strftime('%B %d'),
              'cnf_business_day_rule': 'Next business day where the due date falls on a weekend or a CRA-recognised public holiday.',
              'cnf_dissolution_due_rule': 'A final T2 is due within six months of dissolution.',
              'cnf_primary_keyword': f't2 due date {MONTHS[m-1].lower()} year end',
              'cnf_last_verified_et': TODAY}))

# ---- 10 catch-up year pages --------------------------------------------
for y in range(2017, 2027):
    title = f'File Your {y} Nil T2 Return'
    meta  = (f'File an outstanding {y} nil T2 return. An unfiled year stays open until it is filed. '
             f'{PRICE}, CPA reviewed and transmitted electronically.')
    body = (CSS + '<div class="cnf-dl">\n' + LAST_REVIEWED
      + f'<div class="cnf-lead"><p>A {y} nil T2 return that has not been filed is still outstanding. '
        f'It does not expire and it does not resolve itself.</p></div>\n'
      + P(MUST_FILE)
      + '<h2>What an unfiled year actually costs</h2>\n'
      + f'<div class="cnf-qual"><p>{LATE_QUAL}</p></div>\n'
      + '<h2>Filing it now</h2>\n'
      + P(f'Each tax year is a separate return at {PRICE}. If you have several years outstanding, you '
          f'pick every year you have not filed and each is prepared, reviewed and transmitted.',
          SCOPE, EFILE)
      + cta() + '</div>')
    records.append(dict(
        kind='catch-up-year', slug=f'file-your-{y}-nil-t2-return',
        title=title, meta_description=meta, content=body,
        terms={'cnf_family': ['f14'], 'cnf_tax_year': [str(y)] if y >= 2019 else []},
        meta={'cnf_fiscal_year_end': f'Tax year {y}',
              'cnf_primary_keyword': f'file {y} nil t2 return',
              'cnf_business_day_rule': 'Next business day where the due date falls on a weekend or a CRA-recognised public holiday.',
              'cnf_last_verified_et': TODAY}))

# ---- 1 calendar page ----------------------------------------------------
cal_rows = []
for m in range(1, 13):
    dd = due_date(2026, m)
    cal_rows.append(f'<tr><td>{MONTHS[m-1]} {last_day(2026,m)}</td>'
                    f'<td>{dd.strftime("%B %d")}</td></tr>')
hol = ontario_holidays(2027)
hol_rows = ''.join(f'<tr><td>{d.strftime("%B %d, %Y")}</td><td>{n}</td></tr>'
                   for n, d in sorted(hol.items(), key=lambda x: x[1]))
body = (CSS + '<div class="cnf-dl">\n' + LAST_REVIEWED
  + '<div class="cnf-lead"><p>Every T2 is due six months after the fiscal year-end. '
    'This calendar gives the due date for each of the twelve month-end dates.</p></div>\n'
  + P(MUST_FILE)
  + '<h2>T2 due date by fiscal year-end</h2>\n'
  + '<table><tr><th>Fiscal year-end</th><th>T2 due</th></tr>\n' + '\n'.join(cal_rows) + '</table>\n'
  + P('Where a due date falls on a Saturday, a Sunday or a public holiday recognised by the Canada '
      'Revenue Agency, a return received the next business day is on time.')
  + '<h2>Ontario statutory holidays, 2027</h2>\n'
  + '<table><tr><th>Date</th><th>Holiday</th></tr>' + hol_rows + '</table>\n'
  + '<h2>Filing a nil return</h2>\n' + P(SCOPE, EFILE)
  + P(f'{PRICE}. One price for every year and every province. No hourly billing and no add-on fees.')
  + cta() + '</div>')
records.append(dict(
    kind='calendar', slug='cra-t2-deadline-calendar',
    title='T2 Deadline Calendar for Canadian Corporations',
    meta_description=('Every T2 due date by fiscal year-end, with the Ontario statutory holidays that '
                      f'move a deadline. Nil T2 filing at {PRICE}.'),
    content=body, terms={'cnf_family': ['f14']},
    meta={'cnf_primary_keyword': 't2 filing deadline',
          'cnf_ontario_holiday_list_json': json.dumps({n: d.isoformat() for n, d in hol.items()}),
          'cnf_business_day_rule': 'Next business day where the due date falls on a weekend or a CRA-recognised public holiday.',
          'cnf_last_verified_et': TODAY}))

out = sys.argv[1] if len(sys.argv) > 1 else 'build/f14/f14-manifest.json'
json.dump(records, open(out, 'w'), ensure_ascii=False, indent=1)
from collections import Counter
print(f'{len(records)} records -> {out}')
for k, v in Counter(r['kind'] for r in records).items():
    print(f'   {k:16s} {v}')
