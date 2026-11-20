# -*- coding: utf-8 -*-
"""Family 2 batch 16: five Appendix A tools, chosen for search volume.

Navneet, 2026-11-20: "create pending 5 calculators which can bring good
traffic from plan". Five of the 85 unbuilt Appendix A slugs, picked on three
tests: the term is one people actually search, no live tool already answers
it, and the answer routes back to a nil T2 rather than away from one.

  101  /t2-late-filing-penalty-calculator/              Appendix A line 2786
  102  /repeated-failure-to-file-penalty-calculator/    Appendix A line 2788
  103  /gst-hst-nil-return-deadline-calculator/         Appendix A line 2954
  104  /voluntary-disclosure-eligibility-checker/       Appendix A line 2802
  105  /taxpayer-relief-eligibility-checker/            Appendix A line 2804

WHY THESE FIVE AND NOT THE OTHER EIGHTY
---------------------------------------
"T2 late filing penalty" is the largest unserved term left in the appendix,
and the funnel it opens is the one Section 7.4 was written for: a visitor
arrives expecting a percentage, the tool computes $0.00 on a nil year, and
QUAL explains what the unfiled year costs instead. That is also why the
penalty pair leads the batch.

Eight candidates were dropped rather than built:

- /penalty-on-zero-balance-owing-checker/ is SPENT. Live
  /tools/nil-return-late-penalty-checker/ already runs that exact question,
  down to a section called "A Nil Year and a Year With Tax Owing, Side by
  Side". A second page on it would be a near-duplicate of a live one.
- /ontario-annual-return-requirement-checker/ and
  /ontario-annual-return-deadline-calculator/ were already recorded spent by
  build_f2o.py.
- /t2-six-month-deadline-calculator/ duplicates live
  /tools/nil-t2-deadline-calculator/, which is the 6(e) tool for the same
  six-month rule.
- /fiscal-year-end-calculator/ and /first-tax-year-53-week-checker/ are the
  Appendix A spellings of two tools already live under their 6(e) slugs.
- /zero-activity-corporation-checker/ and /still-required-to-file-checker/
  duplicate live /tools/never-traded-corporation-checker/ and
  /tools/t2-filing-requirement-checker/.
- /instalment-interest-calculator/ was dropped on relevance: a nil
  corporation owes no instalments, so the tool would answer nothing a visitor
  to this site is asking.

The eleven non-resident withholding slugs (branch tax, Part XIII,
Regulation 105, section 116, T1134, T1135, T106, treaty-based return) are
deliberately NOT in this batch. They are gondaliyacpa.ca work at
$350.00 per year, not nil T2 work, and eleven off-topic tool pages on a
single-service domain is a topical-focus cost the plan's own 6(e) rationale
(tools that earn links ON nil filing terms) does not pay for. Raised with
Navneet on 2026-11-20 and logged in decisions.md as a question for Sharad
Gondaliya, not decided here.

THE TWO PENALTY PROVISIONS ARE DIFFERENT PROVISIONS
---------------------------------------------------
Tool 101 is subsection 162(1): 5% of the tax unpaid at the due date, plus 1%
of that amount for each complete month the return is late, to a maximum of 12
months. Ceiling 17%.

Tool 102 is subsection 162(2), which is NOT a bigger version of 162(1). It
applies only when BOTH are true: the Canada Revenue Agency served a demand to
file under subsection 150(2), AND a 162(1) penalty was assessed for any of
the three preceding tax years. Then it is 10% plus 2% per complete month to a
maximum of 20 months. Ceiling 50%.

Both are percentages of tax unpaid, so both are $0.00 on a true nil year, and
both pages say so with QUAL rather than with a bare "no penalty". Hard rule 3.

THE 10-YEAR RELIEF WINDOW
-------------------------
Tool 105: subsection 220(3.1) lets the Minister waive or cancel penalties and
interest, but a request may only reach a tax year ending within the 10
calendar years before the year the request is made. A request made in any of
2026 therefore reaches tax years ending in 2016 or later. WINDOW_BASE below
holds the arithmetic in one place; it is a function of the CURRENT year, not
of TODAY, so the page does not silently go stale in January.

Relief is relief from penalties and interest. It never touches the tax
itself, and on a nil year there is no penalty and no interest for it to
touch, which is what the result screen says.

THE FEE WORDING
---------------
All five are national tools, so neither names HST. Same 2026-11-12 decision
build_f2o.py records: PRICE and the overflow price inside NOT_NIL are
shadowed here, not edited in build_f2, which stays the accurate record of
what the other 101 live pages currently say.
"""
import io, json, os, sys
import re as _re

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_f2 import render, meta, yn, a, SITE, HUB, FORM, TOOL_DISCLAIMER
from build_f2b import tool, num, date, T, G, COST
from build_f2c import MONEY_JS
from build_f2f import RBASE

# Shadows build_f2.PRICE. See "THE FEE WORDING" in the docstring.
PRICE = '$300.00 plus applicable sales tax per tax year'

TODAY, ISO = 'November 20, 2026', '2026-11-20'

# A request made during 2026 reaches tax years ending 2016 or later.
WINDOW_YEARS = 10
WINDOW_BASE = 2026
WINDOW_FIRST = WINDOW_BASE - WINDOW_YEARS      # 2016

# Live tools these five link to. Every one is asserted to exist below.
NILPEN   = T + 'nil-return-late-penalty-checker/'
DEMAND   = T + 'cra-demand-to-file-deadline-calculator/'
NRPEN    = T + 'non-resident-t2-penalty-calculator/'
ARB      = T + 'arbitrary-assessment-response-checker/'
OVERDUE  = T + 'days-overdue-calculator/'
DEAD     = T + 'nil-t2-deadline-calculator/'
UNFILED  = T + 'unfiled-years-cost-calculator/'
GSTNIL   = T + 'gst-hst-nil-filing-checker/'
GSTCLOSE = T + 'gst-hst-account-closure-checker/'
NEXTDUE  = T + 'next-t2-due-date-checker/'
SHIFT    = T + 'due-date-weekend-holiday-shift-calculator/'
CATCHUP  = T + 'catch-up-filing-schedule-generator/'
COUNT    = T + 'outstanding-returns-count-checker/'
SEQ      = T + 'cra-account-closure-sequencer/'
REQD     = T + 't2-filing-requirement-checker/'

# Section 6(g): every tool page links down to the Family 9 guide that
# covers the same ground. gate_batch.py tests for it and batch 16 was
# built without them.
G_PEN     = G + 't2-late-filing-penalties/'
G_DEMAND  = G + 'cra-demand-to-file-response/'
G_ACCTS   = G + 'cra-accounts-on-a-dormant-corporation/'
G_CATCHUP = G + 'catch-up-unfiled-corporate-tax-returns/'
G_ARREARS = G + 'corporate-tax-arrears-and-interest/'

# This batch's own five, for cross-links between them.
P_LATE   = T + 't2-late-filing-penalty-calculator/'
P_REPEAT = T + 'repeated-failure-to-file-penalty-calculator/'
P_GST    = T + 'gst-hst-nil-return-deadline-calculator/'
P_VDP    = T + 'voluntary-disclosure-eligibility-checker/'
P_RELIEF = T + 'taxpayer-relief-eligibility-checker/'


def _tbl(head, rows):
    return ('<table class="ei-tbl"><thead><tr>'
            + ''.join('<th scope="col">%s</th>' % h for h in head)
            + '</tr></thead><tbody>\n'
            + '\n'.join('<tr>' + ''.join('<td>%s</td>' % c for c in r)
                        + '</tr>' for r in rows)
            + '\n</tbody></table>')


# Each page closes in its own words; gate_f2_all.py caught a shared closing
# sentence on batch 13 and the per-page close is asserted below.
CLOSE = {
 't2-late-filing-penalty-calculator':
   'The percentage needs something to be a percentage of, and that is the '
   'whole reason a nil year and a year with tax owing come out so far apart.',
 'repeated-failure-to-file-penalty-calculator':
   'Two conditions have to be met before this provision applies at all, and '
   'most corporations asking about it have met only one.',
 'gst-hst-nil-return-deadline-calculator':
   'An account that was opened and never closed keeps its own filing '
   'calendar, and that calendar has nothing to do with the T2.',
 'voluntary-disclosure-eligibility-checker':
   'The programme exists to relieve penalties, so a year that was charged '
   'none of them has nothing for it to relieve.',
 'taxpayer-relief-eligibility-checker':
   'Relief reaches the penalty and the interest, never the tax, and on a nil '
   'year there was never any of the three.',
}

# ============================================================ 101. 162(1)
T101_JS = RBASE + MONEY_JS + r"""
var out=document.getElementById('out');
function months(due,filed){
  var n=0;
  while(n < 12){
    if(addMonths(due,n+1).getTime() > filed.getTime()){break;}
    n++;
  }
  return n;
}
function show(){
  var ye=parse('ye'),filed=parse('filed'),
      raw=document.getElementById('tax').value.trim(),h,wait=0;
  if(ye===null||ye===undefined){wait++;}
  if(filed===null||filed===undefined){wait++;}
  if(raw===''){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three entries '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var tax=Math.round(parseFloat(raw)*100);
  if(isNaN(tax)||tax<0){
    out.innerHTML='<p>Enter the tax owing as a number, using 0 for a nil '
     +'return.</p>';return;
  }
  var due=dueDate(ye);
  if(filed.getTime()<=due.getTime()){
    h='<h3>The return is on time, so subsection 162(1) does not reach it'
     +'</h3>';
    h+='<p>A year-end of '+fmt(ye)+' makes the T2 due '+fmt(due)
     +', and this one was filed '+fmt(filed)+'. Subsection 162(1) applies '
     +'only to a return filed after its due date.</p>';
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  var n=months(due,filed),base=Math.round(tax*0.05),
      per=Math.round(tax*0.01),mth=per*n,total=base+mth;
  if(tax===0){
    h='<h3>The penalty is $0.00, and the year is still open</h3>';
    h+='<p>'+QUALJS+'</p>';
  }else{
    h='<h3>'+money(total)+' under subsection 162(1)</h3>';
    h+='<p>Five per cent of the tax unpaid at the due date, plus one per '
     +'cent of it for each of the '+plural(n,'complete month')
     +' between '+fmt(due)+' and '+fmt(filed)+'. The monthly part stops at '
     +'twelve months, so the ceiling is seventeen per cent.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Part</th>'
   +'<th scope="col">Rate</th><th scope="col">Amount</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Tax unpaid at '+fmt(due)+'</td><td>The base figure</td><td>'
   +money(tax)+'</td></tr>';
  h+='<tr><td>Flat part</td><td>5%</td><td>'+money(base)+'</td></tr>';
  h+='<tr><td>Monthly part</td><td>1% &times; '+n+'</td><td>'
   +money(mth)+'</td></tr>';
  h+='<tr><td>Penalty under 162(1)</td><td>'+(5+n)+'%</td><td>'
   +money(total)+'</td></tr>';
  h+='</tbody></table>';
  if(n>=12){
    h+='<p>Twelve complete months have gone by, so the monthly part is at '
     +'its ceiling and will not grow further. Arrears interest on the '
     +'balance does keep running.</p>';
  }
  h+='<p>This figure is subsection 162(1). A corporation that was served a '
   +'demand to file and had a late-filing penalty assessed in any of the '
   +'three preceding years falls under subsection 162(2) instead, which the '
   +'<a href="SITEREPEAT">repeated failure to file penalty calculator</a> '
   +'works out.</p>';
  if(tax===0){
    h+='<p>Nil T2 filing at '+PRICE_JS+' closes a year like this one. '
     +NOTNILJS+'</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITEREPEAT', P_REPEAT)

T101 = dict(
 slug='t2-late-filing-penalty-calculator',
 title='T2 Late Filing Penalty Calculator | Subsection 162(1)',
 h1_pre='T2 Late Filing ', h1_span='Penalty Calculator',
 h1='T2 Late Filing Penalty Calculator',
 eyebrow='Penalty',
 keyword='t2 late filing penalty',
 seo_title='T2 Late Filing Penalty Calculator',
 seo_desc=('Five per cent of the tax owing plus one per cent for each '
           'complete month late, to twelve months. A nil return computes to '
           '$0.00.'),
 meta=('The late-filing penalty is a percentage of the tax unpaid at the due '
       'date, so a return with no tax owing produces no percentage penalty.'),
 tags=['5% plus 1% per month', 'Twelve months maximum',
       'A percentage of tax owing', '$0.00 on a nil year'],
 form=tool('Your return and what it owed',
           [date('ye', 'The fiscal year-end'),
            num('tax', 'Tax owing on the return, in dollars',
                'Enter 0 for a nil return', 0, 100000000, '0'),
            date('filed', 'The date the return was filed')],
           'Enter the year-end, the tax owing and the filing date.'),
 js=None,
 sections=[
  ('how-it-works', 'The Penalty Is a Percentage, Not a Flat Fee',
   '<p>Subsection 162(1) of the Income Tax Act sets the late-filing penalty '
   'at five per cent of the tax that was unpaid when the return came due, '
   'plus a further one per cent of that same amount for each complete month '
   'the return stays unfiled. The monthly part runs for at most twelve '
   'months, which puts the ceiling at seventeen per cent.</p>\n'
   '<p>Two things follow from the words &ldquo;of the tax unpaid&rdquo;. A '
   'month that is not yet complete adds nothing, so filing on day twenty-nine '
   'of a month costs the same as filing on day one of it. And a return with '
   'no tax unpaid has nothing for either percentage to apply to.</p>'),
  ('nil-year', 'What the Same Arithmetic Does to a Nil Year',
   _tbl(['The year', 'Tax unpaid at the due date', 'Penalty at twelve months'],
        [['Owed $9,000.00', '$9,000.00', '$1,530.00, being 17%'],
         ['Owed $1,200.00', '$1,200.00', '$204.00, being 17%'],
         ['A true nil year', '$0.00', '$0.00, because 17% of nil is nil']])
   + '\n<p>That last row is the reason this page exists and also the reason '
   'it does not stop there. A nil year carries no percentage penalty and '
   'still stays open indefinitely, still invites a demand to file and an '
   'arbitrary assessment, and still blocks a clearance certificate and '
   'dissolution. The '
   + a(NILPEN, 'nil return late penalty checker')
   + ' runs that question on its own, and the '
   + a(NRPEN, 'non-resident T2 penalty calculator')
   + ' covers the one charge that does not depend on tax owing at all.</p>\n'
   '<p>' + CLOSE['t2-late-filing-penalty-calculator'] + '</p>'),
  ('after', 'Interest Is Separate, and Keeps Running',
   '<p>The penalty and the arrears interest are two charges. The penalty '
   'stops growing once twelve complete months have passed; interest on an '
   'unpaid balance does not stop until the balance is paid. A nil year has no '
   'balance, so it accrues no interest either.</p>\n'
   '<p>Relief from a penalty already assessed is a separate application '
   'again, and the '
   + a(P_RELIEF, 'taxpayer relief eligibility checker')
   + ' covers the grounds and the ten-year window. For years still unfiled, '
   + a(COST, 'nil T2 filing at ' + PRICE)
   + ' closes one tax year per return, and the '
   + a(UNFILED, 'unfiled years cost calculator')
   + ' totals several at once. The '
   + a(G_PEN, 'guide to T2 late-filing penalties')
   + ' sets out the provisions in full.</p>'),
 ],
 faq=[
  ('How much is the T2 late filing penalty?',
   'Five per cent of the tax unpaid at the due date, plus one per cent of '
   'that amount for each complete month the return is late, to a maximum of '
   'twelve months.'),
  ('What is the maximum?',
   'Seventeen per cent of the tax that was unpaid at the due date, reached '
   'once twelve complete months have gone by.'),
  ('Is there a penalty if the corporation owes no tax?',
   'The percentage produces $0.00, because there is no unpaid tax for it to '
   'apply to. The unfiled year still stays open and still has consequences.'),
  ('Does a part month count?',
   'No. Only complete months are counted, so the figure steps up on the '
   'monthly anniversary of the due date rather than daily.'),
  ('When is the T2 due?',
   'Within six months of the fiscal year-end. The calculator works the due '
   'date out from the year-end you enter.'),
  ('Does the penalty apply to a return filed on the due date?',
   'No. Subsection 162(1) applies only to a return filed after its due date.'),
  ('Is this the same as the repeated failure penalty?',
   'No. That is subsection 162(2), at ten per cent plus two per cent per '
   'month, and it needs a demand to file and a prior penalty before it '
   'applies.'),
  ('Does interest get added on top?',
   'Arrears interest runs on an unpaid balance separately from the penalty, '
   'and unlike the penalty it does not stop at twelve months.'),
  ('Can the penalty be cancelled?',
   'The Minister may waive or cancel a penalty on specified grounds. That is '
   'a taxpayer relief request and it has its own ten-year window.'),
  ('Will filing late years now make the penalty larger?',
   'No. The monthly part is capped at twelve months and most unfiled years '
   'are long past that, so filing stops nothing from growing but closes the '
   'year.'),
 ],
 related=[
  (NILPEN, 'Nil return late penalty checker'),
  (P_REPEAT, 'Repeated failure to file penalty calculator'),
  (NRPEN, 'Non-resident T2 penalty calculator'),
  (P_RELIEF, 'Taxpayer relief eligibility checker'),
  (OVERDUE, 'Days overdue calculator'),
  (DEAD, 'Nil T2 deadline calculator'),
 ],
)

# ============================================================ 102. 162(2)
T102_JS = RBASE + MONEY_JS + r"""
var out=document.getElementById('out');
function show(){
  var dem=pick('dem'),prior=pick('prior'),
      raw=document.getElementById('tax').value.trim(),
      rawm=document.getElementById('mo').value.trim(),h,wait=0;
  if(dem===null){wait++;}
  if(prior===null){wait++;}
  if(raw===''){wait++;}
  if(rawm===''){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the four entries '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var tax=Math.round(parseFloat(raw)*100),mo=parseInt(rawm,10);
  if(isNaN(tax)||tax<0||isNaN(mo)||mo<0){
    out.innerHTML='<p>Enter the tax owing and the months late as numbers, '
     +'using 0 for a nil return.</p>';return;
  }
  var repeat=(dem==='y'&&prior==='y');
  var n1=Math.min(mo,12),n2=Math.min(mo,20);
  var p1=Math.round(tax*0.05)+Math.round(tax*0.01)*n1;
  var p2=Math.round(tax*0.10)+Math.round(tax*0.02)*n2;
  if(tax===0){
    h='<h3>Either provision computes to $0.00 on a nil year</h3>';
    h+='<p>'+QUALJS+'</p>';
  }else if(repeat){
    h='<h3>'+money(p2)+' under subsection 162(2)</h3>';
    h+='<p>Both conditions are met, so the larger provision applies: ten per '
     +'cent of the tax unpaid plus two per cent for each of the '
     +plural(n2,'complete month')+' counted, to a ceiling of twenty months '
     +'and fifty per cent.</p>';
  }else{
    h='<h3>'+money(p1)+' under subsection 162(1)</h3>';
    h+='<p>Subsection 162(2) needs a demand to file AND a late-filing '
     +'penalty assessed for one of the three preceding tax years. '
     +(dem==='y'?'A demand was served, but no prior penalty was assessed'
                :'No demand to file was served')
     +', so the ordinary provision applies instead.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Provision</th>'
   +'<th scope="col">Flat</th><th scope="col">Monthly</th>'
   +'<th scope="col">Months counted</th><th scope="col">Figure</th>'
   +'<th scope="col">Applies here</th></tr></thead><tbody>';
  h+='<tr><td>162(1), ordinary</td><td>5%</td><td>1%</td><td>'+n1
   +' of 12</td><td>'+money(p1)+'</td><td>'+(repeat?'No':'Yes')
   +'</td></tr>';
  h+='<tr><td>162(2), repeated failure</td><td>10%</td><td>2%</td><td>'+n2
   +' of 20</td><td>'+money(p2)+'</td><td>'+(repeat?'Yes':'No')
   +'</td></tr>';
  h+='</tbody></table>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Condition</th>'
   +'<th scope="col">Your answer</th></tr></thead><tbody>';
  h+='<tr><td>A demand to file was served for this year</td><td>'
   +(dem==='y'?'Yes':'No')+'</td></tr>';
  h+='<tr><td>A late-filing penalty was assessed in one of the three '
   +'preceding years</td><td>'+(prior==='y'?'Yes':'No')+'</td></tr>';
  h+='</tbody></table>';
  if(dem==='y'){
    h+='<p>A demand carries its own filing date, which the '
     +'<a href="SITEDEMAND">demand to file deadline calculator</a> works '
     +'out, and ignoring it is what leads to an assessment built from the '
     +'outside.</p>';
  }
  if(tax===0){
    h+='<p>Nil T2 filing at '+PRICE_JS+' closes one tax year per return. '
     +NOTNILJS+'</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITEDEMAND', DEMAND)

T102 = dict(
 slug='repeated-failure-to-file-penalty-calculator',
 title='Repeated Failure to File Penalty Calculator | 162(2)',
 h1_pre='Repeated Failure to File ', h1_span='Penalty Calculator',
 h1='Repeated Failure to File Penalty Calculator',
 eyebrow='Penalty',
 keyword='repeated failure to file penalty',
 seo_title='Repeated Failure to File Penalty Calculator',
 seo_desc=('Subsection 162(2) charges ten per cent plus two per cent a month '
           'to twenty months, but only after a demand to file and a prior '
           'penalty.'),
 meta=('The larger late-filing penalty applies only when a demand to file '
       'was served and a penalty was already assessed in one of the three '
       'preceding years.'),
 tags=['10% plus 2% per month', 'Twenty months maximum',
       'Two conditions, both required', '$0.00 on a nil year'],
 form=tool('The year, and what came before it',
           [num('tax', 'Tax owing on the return, in dollars',
                'Enter 0 for a nil return', 0, 100000000, '0'),
            num('mo', 'Complete months the return is late',
                'Count whole months past the due date', 0, 240, '0'),
            yn('dem', 'Was a demand to file served for this year?'),
            yn('prior', 'Was a late-filing penalty assessed in any of the '
                        'three preceding tax years?')],
           'Enter the two figures and answer the two questions.'),
 js=None,
 sections=[
  ('two-conditions', 'Both Conditions Have to Be Met',
   '<p>Subsection 162(2) is often described as the penalty for filing late '
   'again, which understates what it takes to trigger. Two things must both '
   'be true of the year in question: the Canada Revenue Agency served a '
   'demand to file for it, and a late-filing penalty under subsection 162(1) '
   'was assessed for any of the three tax years immediately before it.</p>\n'
   '<p>Miss either one and the ordinary provision applies instead. A '
   'corporation with nine unfiled years and no demand ever served is on '
   '162(1), not this one, however many years have gone by.</p>'),
  ('the-rates', 'Twice the Rate, and Twenty Months Instead of Twelve',
   _tbl(['', 'Subsection 162(1)', 'Subsection 162(2)'],
        [['Flat part', '5% of tax unpaid', '10% of tax unpaid'],
         ['Each complete month', '1%', '2%'],
         ['Months counted, at most', '12', '20'],
         ['Ceiling', '17%', '50%'],
         ['Needs a demand to file', 'No', 'Yes'],
         ['Needs a prior penalty', 'No', 'Yes, in the preceding three years']])
   + '\n<p>Both are percentages of the tax that was unpaid at the due date, '
   'which is the point most easily lost. Fifty per cent of nil is nil, so a '
   'corporation whose unfiled years were genuinely nil is not exposed to '
   'this figure at all, no matter how many demands arrive. The '
   + a(NILPEN, 'nil return late penalty checker')
   + ' and the '
   + a(P_LATE, 'T2 late filing penalty calculator')
   + ' take the same arithmetic from the other two directions.</p>\n'
   '<p>' + CLOSE['repeated-failure-to-file-penalty-calculator'] + '</p>'),
  ('what-to-do', 'A Demand Is the Part Worth Acting On',
   '<p>Of the two conditions, only one is still in the corporation&rsquo;s '
   'hands. A penalty assessed in an earlier year is history. A demand to '
   'file has a date on it, and filing by that date is what answers it. The '
   + a(DEMAND, 'demand to file deadline calculator')
   + ' works the date out, and the '
   + a(ARB, 'arbitrary assessment response checker')
   + ' covers what happens when the date goes by.</p>\n'
   '<p>Where the years are nil, '
   + a(COST, 'nil T2 filing at ' + PRICE)
   + ' closes one tax year per return and the '
   + a(CATCHUP, 'catch-up filing schedule generator')
   + ' puts several in order, oldest first. The '
   + a(G_DEMAND, 'guide to responding to a demand to file')
   + ' covers what a demand asks and what answering it takes.</p>'),
 ],
 faq=[
  ('What is the repeated failure to file penalty?',
   'Subsection 162(2): ten per cent of the tax unpaid at the due date, plus '
   'two per cent of it for each complete month late, to twenty months.'),
  ('What is the maximum?',
   'Fifty per cent of the tax that was unpaid at the due date, reached at '
   'twenty complete months.'),
  ('When does it apply instead of the ordinary penalty?',
   'Only when a demand to file was served for the year and a late-filing '
   'penalty was assessed for one of the three preceding tax years.'),
  ('I have filed late several years in a row. Does it apply?',
   'Not on its own. Without a demand to file for the year in question, the '
   'ordinary five per cent provision applies however many years are late.'),
  ('Does it apply to a nil return?',
   'The percentage produces $0.00, because there is no unpaid tax. The '
   'unfiled year itself still has consequences.'),
  ('How far back does the prior penalty have to be?',
   'Within the three tax years immediately preceding the year in question.'),
  ('Does a part month count?',
   'No. Only complete months are counted, on the monthly anniversary of the '
   'due date.'),
  ('What is a demand to file?',
   'A written requirement under subsection 150(2) to file a return, with a '
   'date by which it must be filed.'),
  ('Can both penalties apply to one year?',
   'No. One provision or the other applies to a given tax year, not both.'),
  ('Can it be cancelled?',
   'It can be the subject of a taxpayer relief request on specified grounds, '
   'within the ten-year window that applies to those requests.'),
 ],
 related=[
  (P_LATE, 'T2 late filing penalty calculator'),
  (DEMAND, 'CRA demand to file deadline calculator'),
  (ARB, 'Arbitrary assessment response checker'),
  (NILPEN, 'Nil return late penalty checker'),
  (P_RELIEF, 'Taxpayer relief eligibility checker'),
  (CATCHUP, 'Catch-up filing schedule generator'),
 ],
)

# ====================================================== 103. GST/HST nil due
T103_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var pe=parse('pe'),ann=pick('ann'),open=pick('open'),h,wait=0;
  if(pe===null||pe===undefined){wait++;}
  if(ann===null){wait++;}
  if(open===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three entries '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var step=(ann==='y'?3:1),due=addMonths(pe,step);
  if(open==='n'){
    h='<h3>A closed account files nothing further</h3>';
    h+='<p>Once the account is closed there is no reporting period after the '
     +'final return, so no date arises. What a closure needs is the final '
     +'return for the period up to the closure date, and the '
     +'<a href="SITECLOSE">GST/HST account closure checker</a> covers the '
     +'order that goes in.</p>';
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  h='<h3>Due '+fmt(due)+'</h3>';
  h+='<p>'+(ann==='y'?'An annual filer files three months after the end of '
    +'the fiscal year':'A monthly or quarterly filer files one month after '
    +'the end of the reporting period')+', so a period ending '+fmt(pe)
   +' is due '+fmt(due)+'. Nothing about that date comes from the T2.</p>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">What</th>'
   +'<th scope="col">Date</th><th scope="col">Filed with</th>'
   +'<th scope="col">Covered by the nil T2 fee</th></tr></thead><tbody>';
  h+='<tr><td>Reporting period ends</td><td>'+fmt(pe)+'</td>'
   +'<td>Nothing is filed on this date</td><td>Not applicable</td></tr>';
  h+='<tr><td>GST/HST return</td><td>'+fmt(due)+'</td>'
   +'<td>Canada Revenue Agency, against the GST/HST account</td>'
   +'<td>No</td></tr>';
  h+='</tbody></table>';
  h+='<p>A period in which the corporation collected nothing and claimed '
   +'nothing is still a period the account has to report. A nil GST/HST '
   +'return is a return, not an absence of one, and an account left open and '
   +'unreported accrues its own failure-to-file exposure independently of '
   +'the T2.</p>';
  h+='<p>Nil T2 filing at '+PRICE_JS+' covers the federal corporate income '
   +'tax return, not the row above it: the GST/HST account is a separate '
   +'registration with its own returns, and filing it is not part of the '
   +'fee. The '
   +'<a href="SITEGSTNIL">GST/HST nil filing checker</a> covers whether the '
   +'account needs one at all.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITECLOSE', GSTCLOSE).replace('SITEGSTNIL', GSTNIL)

T103 = dict(
 slug='gst-hst-nil-return-deadline-calculator',
 title='GST/HST Nil Return Deadline Calculator | When It Is Due',
 h1_pre='GST/HST Nil Return ', h1_span='Deadline Calculator',
 h1='GST/HST Nil Return Deadline Calculator',
 eyebrow='GST/HST',
 keyword='gst hst nil return deadline',
 seo_title='GST/HST Nil Return Deadline Calculator',
 seo_desc=('An annual filer reports three months after the fiscal year end '
           'and a monthly or quarterly filer one month after the period '
           'ends.'),
 meta=('An open GST/HST account reports every period whether or not anything '
       'was collected, on a calendar of its own that the T2 does not touch.'),
 tags=['Annual filers, three months', 'Monthly and quarterly, one month',
       'A nil return is still a return', 'Separate from the T2'],
 form=tool('Your GST/HST account and its period',
           [date('pe', 'The end of the reporting period'),
            yn('ann', 'Does the account file annually?'),
            yn('open', 'Is the GST/HST account still open?')],
           'Enter the period end and answer the two questions.'),
 js=None,
 sections=[
  ('the-dates', 'Two Calendars, Depending on the Filing Frequency',
   '<p>A GST/HST return is due one month after the end of the reporting '
   'period for a monthly or quarterly filer, and three months after the '
   'fiscal year end for an annual filer. A corporation that registered once '
   'and never looked again is almost always an annual filer, because that is '
   'the default at low revenue.</p>\n'
   '<p>Neither date has anything to do with the six months that governs the '
   'T2. A December 31 year-end puts the T2 at June 30 and an annual GST/HST '
   'return at March 31, so the two land in different quarters and are missed '
   'independently of each other.</p>'),
  ('nil-is-a-return', 'A Period With No Activity Is Still a Period',
   _tbl(['Filing frequency', 'Period ending', 'Return due'],
        [['Annual', 'December 31', 'March 31'],
         ['Annual', 'June 30', 'September 30'],
         ['Quarterly', 'March 31', 'April 30'],
         ['Monthly', 'January 31', 'February 28 or 29']])
   + '\n<p>An account that collected nothing files a nil return rather than '
   'nothing at all, and the obligation runs from the registration, not from '
   'the activity. That is why a dormant corporation can be perfectly correct '
   'on its T2 and still be behind on a second account nobody closed. The '
   + a(GSTNIL, 'GST/HST nil filing checker')
   + ' decides whether the account needs returns, and the '
   + a(GSTCLOSE, 'GST/HST account closure checker')
   + ' covers form RC145 and what closing one takes.</p>\n'
   '<p>' + CLOSE['gst-hst-nil-return-deadline-calculator'] + '</p>'),
  ('not-the-fee', 'What the Nil T2 Fee Does and Does Not Reach',
   '<p>' + a(COST, 'Nil T2 filing at ' + PRICE)
   + ' is the federal corporate income tax return, transmitted '
   'electronically. The GST/HST account is a separate registration with its '
   'own returns, its own periods and its own exposure, and filing it is not '
   'part of that fee. We will tell you the date; the return against that '
   'account stays yours to file or to close.</p>\n'
   '<p>Where several accounts are being wound down at once, the order '
   'matters, and the '
   + a(SEQ, 'CRA account closure sequencer')
   + ' sets it out. For the corporate return itself the '
   + a(NEXTDUE, 'next T2 due date checker')
   + ' gives the date on the other calendar, and the '
   + a(G_ACCTS, 'guide to CRA accounts on a dormant corporation')
   + ' covers every account a quiet corporation still carries.</p>'),
 ],
 faq=[
  ('When is a nil GST/HST return due?',
   'One month after the end of the reporting period for a monthly or '
   'quarterly filer, and three months after the fiscal year end for an '
   'annual filer.'),
  ('Does a dormant corporation have to file GST/HST returns?',
   'If the account is still open, yes. The obligation follows the '
   'registration rather than the activity.'),
  ('Is a nil return the same as not filing?',
   'No. A nil return reports that the period had nothing in it. Not filing '
   'leaves the period unreported.'),
  ('Is it due at the same time as the T2?',
   'No. The T2 runs six months from the fiscal year-end; neither GST/HST '
   'date does.'),
  ('How do I know whether the account files annually?',
   'The Canada Revenue Agency assigns the frequency, and annual is the '
   'default at low revenue. The confirmation of registration states it.'),
  ('Is the GST/HST return included in the nil T2 fee?',
   'No. The fee covers the federal corporate income tax return. The GST/HST '
   'account is a separate registration.'),
  ('What if the account should have been closed years ago?',
   'The periods between then and now are still reportable until it is '
   'closed. Closing it takes a final return and form RC145.'),
  ('Is there a penalty on a nil GST/HST return filed late?',
   'The failure-to-file penalty is calculated on an amount owing, so a nil '
   'period produces no percentage charge. The period stays unreported until '
   'it is filed.'),
  ('Does the due date shift off a weekend?',
   'The Canada Revenue Agency treats a payment or return received on the '
   'next business day as on time when the due date falls on a weekend or a '
   'holiday.'),
  ('Can one return cover several missed periods?',
   'No. Each reporting period is its own return, in the same way each tax '
   'year is its own T2.'),
 ],
 related=[
  (GSTNIL, 'GST/HST nil filing checker'),
  (GSTCLOSE, 'GST/HST account closure checker'),
  (SEQ, 'CRA account closure sequencer'),
  (NEXTDUE, 'Next T2 due date checker'),
  (SHIFT, 'Due date weekend and holiday shift calculator'),
  (REQD, 'T2 filing requirement checker'),
 ],
)

# ============================================================== 104. VDP
T104_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var ct=pick('ct'),old=pick('old'),all=pick('all'),nil=pick('nil'),h,wait=0;
  if(ct===null){wait++;}
  if(old===null){wait++;}
  if(all===null){wait++;}
  if(nil===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the four questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  var vol=(ct==='n'),ok=(vol&&old==='y'&&all==='y');
  if(nil==='y'&&ok){
    h='<h3>The conditions are met, and nil years may not need the '
     +'programme</h3>';
    h+='<p>The Voluntary Disclosures Programme relieves penalties and part '
     +'of the interest. '+QUALJS+' A year carrying neither charge has little '
     +'for the programme to relieve, so unfiled nil years are '
     +'usually simply filed, oldest first.</p>';
  }else if(ok){
    h='<h3>The three conditions are met on these answers</h3>';
    h+='<p>The disclosure looks voluntary, it reaches information at least a '
     +'year past due, and it is complete. An application still has to be '
     +'accepted on its facts, and the estimated tax owing is paid with '
     +'it.</p>';
  }else if(!vol){
    h='<h3>It is unlikely to count as voluntary</h3>';
    h+='<p>The programme requires that the disclosure come before the Canada '
     +'Revenue Agency takes enforcement action on the matter. Once the '
     +'Agency has made contact about these years, a disclosure about them is '
     +'generally no longer voluntary, and the route is to file and respond '
     +'rather than to apply.</p>';
  }else if(old==='n'){
    h='<h3>Nothing is far enough past due yet</h3>';
    h+='<p>An application has to include information that is at least one '
     +'year past its due date. A return that is merely late does not qualify '
     +'and is filed in the ordinary way.</p>';
  }else{
    h='<h3>A partial disclosure does not meet the condition</h3>';
    h+='<p>The programme requires a complete disclosure. Leaving some '
     +'unfiled years out of the application is the condition most often '
     +'failed, and the '
     +'<a href="SITECOUNT">outstanding returns count checker</a> is a way '
     +'to establish how many there actually are.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Condition</th>'
   +'<th scope="col">What it asks</th><th scope="col">On these answers</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Voluntary</td><td>Made before the Agency acts on the matter'
   +'</td><td>'+(vol?'Met':'Not met')+'</td></tr>';
  h+='<tr><td>At least a year past due</td>'
   +'<td>Includes information one year or more overdue</td><td>'
   +(old==='y'?'Met':'Not met')+'</td></tr>';
  h+='<tr><td>Complete</td><td>Covers every year and every account</td><td>'
   +(all==='y'?'Met':'Not met')+'</td></tr>';
  h+='<tr><td>Involves a penalty</td>'
   +'<td>There is a penalty for the programme to relieve</td><td>'
   +(nil==='y'?'Unlikely on nil years':'Likely')+'</td></tr>';
  h+='</tbody></table>';
  if(nil==='y'){
    h+='<p>Nil T2 filing at '+PRICE_JS+' closes one tax year per return, '
     +'and the years go in oldest first. '+NOTNILJS+'</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITECOUNT', COUNT)

T104 = dict(
 slug='voluntary-disclosure-eligibility-checker',
 title='Voluntary Disclosure Eligibility Checker | CRA VDP',
 h1_pre='Voluntary Disclosure ', h1_span='Eligibility Checker',
 h1='Voluntary Disclosure Eligibility Checker',
 eyebrow='Catch-Up',
 keyword='voluntary disclosure eligibility',
 seo_desc=('A disclosure has to be voluntary, complete and at least a year '
           'past due. A nil year carries nothing for the programme to '
           'relieve.'),
 seo_title='Voluntary Disclosure Eligibility Checker',
 meta=('The programme relieves penalties on a disclosure made before the '
       'Canada Revenue Agency acts, which is why a nil year rarely needs '
       'it.'),
 tags=['Voluntary, before the Agency acts', 'One year past due',
       'Complete, or not at all', 'Nil years rarely need it'],
 form=tool('Your unfiled years',
           [yn('ct', 'Has the Canada Revenue Agency contacted you about '
                     'these years?'),
            yn('old', 'Is at least one return more than a year past due?'),
            yn('all', 'Will the disclosure cover every unfiled year?'),
            yn('nil', 'Were all the unfiled years nil?')],
           'Answer the four questions and the conditions are set out here.'),
 js=None,
 sections=[
  ('conditions', 'What the Programme Requires',
   '<p>The Voluntary Disclosures Programme lets a taxpayer correct an '
   'earlier filing position and have penalties relieved. Four things are '
   'asked of an application: that it be voluntary, meaning made before the '
   'Canada Revenue Agency takes enforcement action on the matter; that it be '
   'complete; that it involve the application of a penalty; and that it '
   'include information at least one year past due.</p>\n'
   '<p>The first is the one that closes the door. A letter, a telephone call '
   'or a demand to file about the years in question generally ends the '
   'possibility of a voluntary disclosure about them, which is why the '
   'programme is of no use to someone who waited for contact.</p>'),
  ('nil-years', 'Why a Nil Year Usually Does Not Need It',
   _tbl(['', 'A year with tax owing', 'A true nil year'],
        [['Late-filing penalty', 'Up to 17% of the tax unpaid', '$0.00'],
         ['Arrears interest', 'Runs until the balance is paid', 'None'],
         ['What the programme relieves', 'The penalty and part of the interest',
          'Nothing, because there is neither'],
         ['The practical route', 'Consider an application', 'File the years']])
   + '\n<p>The programme relieves penalties. '
   'Where the unfiled years were genuinely nil there is no percentage '
   'penalty and no interest, so an application spends time and professional '
   'fees to relieve charges that were never assessed. Filing the years is '
   'the shorter route, and the '
   + a(NILPEN, 'nil return late penalty checker')
   + ' sets out what the open years do cost instead.</p>\n'
   '<p>' + CLOSE['voluntary-disclosure-eligibility-checker'] + '</p>'),
  ('practical', 'If the Years Were Not Nil',
   '<p>A corporation with unreported income, a dividend paid or received, '
   'rent collected or investment income in any of the years is not filing '
   'nil returns, and the calculation above does not apply to it. Those years '
   'carry real tax, real penalties and real interest, and an application may '
   'be worth making.</p>\n'
   '<p>That work is not what this site does. It is handled by Gondaliya CPA '
   'Professional Corporation at gondaliyacpa.ca at $350.00 plus applicable '
   'sales tax per year, and a disclosure is a matter to take advice on '
   'before filing anything. Where the years are nil, '
   + a(COST, 'nil T2 filing at ' + PRICE)
   + ' closes one per return and the '
   + a(CATCHUP, 'catch-up filing schedule generator')
   + ' orders them. The '
   + a(G_CATCHUP, 'guide to catching up unfiled corporate tax returns')
   + ' is the longer treatment.</p>'),
 ],
 faq=[
  ('What is the Voluntary Disclosures Programme?',
   'A Canada Revenue Agency programme that relieves penalties, and part of '
   'the interest, on a disclosure a taxpayer makes before the Agency acts.'),
  ('What makes a disclosure voluntary?',
   'That it is made before the Agency takes enforcement action on the '
   'matter. Contact about the years in question generally ends it.'),
  ('How overdue does something have to be?',
   'The application must include information at least one year past its due '
   'date.'),
  ('Can I disclose some years and not others?',
   'No. The programme requires a complete disclosure, and a partial one '
   'fails that condition.'),
  ('Do nil years need a voluntary disclosure?',
   'Usually not. The programme relieves penalties, and a true nil year '
   'carries no percentage penalty and no interest for it to relieve.'),
  ('Does an application stop a demand to file?',
   'No. A demand has its own date, and filing by that date is what answers '
   'it.'),
  ('Does meeting the conditions assure relief?',
   'No. An application is assessed on its facts and may be accepted into '
   'either of the programme tracks, or refused.'),
  ('Is the tax itself forgiven?',
   'No. The estimated tax owing is paid with the application. The relief is '
   'from penalties and part of the interest.'),
  ('How many years back can a disclosure go?',
   'There is no fixed limit on the years disclosed, though interest relief '
   'is bounded by its own ten-year rule.'),
  ('What is the difference from taxpayer relief?',
   'A disclosure corrects a filing position before the Agency acts. '
   'Taxpayer relief asks the Minister to cancel charges already assessed.'),
 ],
 related=[
  (P_RELIEF, 'Taxpayer relief eligibility checker'),
  (NILPEN, 'Nil return late penalty checker'),
  (COUNT, 'Outstanding returns count checker'),
  (CATCHUP, 'Catch-up filing schedule generator'),
  (UNFILED, 'Unfiled years cost calculator'),
  (DEMAND, 'CRA demand to file deadline calculator'),
 ],
)

# =========================================================== 105. relief
T105_JS = RBASE + r"""
var out=document.getElementById('out');
var WFIRST=WINDOWFIRST;
function show(){
  var ground=pick('ground'),filed=pick('filed'),nil=pick('nil'),
      raw=document.getElementById('yr').value.trim(),h,wait=0;
  if(raw===''){wait++;}
  if(ground===null){wait++;}
  if(filed===null){wait++;}
  if(nil===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the four entries '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var yr=parseInt(raw,10);
  if(isNaN(yr)||yr<1970||yr>WFIRST+WINDOWYEARS){
    out.innerHTML='<p>Enter the tax year as a four-digit year.</p>';return;
  }
  var inWindow=(yr>=WFIRST);
  if(nil==='y'){
    h='<h3>A nil year has nothing for relief to reach</h3>';
    h+='<p>'+QUALJS+' Relief under subsection 220(3.1) reaches penalties and '
     +'interest and never the tax, so on a year that carried none of the '
     +'three there is nothing for a request to cancel. Filing the year is '
     +'what closes it.</p>';
  }else if(!inWindow){
    h='<h3>'+yr+' is outside the ten-year window</h3>';
    h+='<p>A request may only reach a tax year ending within the ten '
     +'calendar years before the year the request is made. A request made '
     +'during '+(WFIRST+WINDOWYEARS)+' reaches tax years ending in '+WFIRST
     +' or later, so '+yr+' is out of reach however strong the grounds.</p>';
  }else if(ground==='n'){
    h='<h3>No ground is identified on these answers</h3>';
    h+='<p>The year is inside the window, but relief is discretionary and '
     +'granted on specified grounds. Without extraordinary circumstances, an '
     +'action of the Canada Revenue Agency, or an inability to pay, a '
     +'request has nothing to rest on.</p>';
  }else{
    h='<h3>'+yr+' is in the window and a ground is identified</h3>';
    h+='<p>Form RC4288 is the request, and the Minister may waive or cancel '
     +'the penalty and the interest. It stays discretionary, and the '
     +'outstanding returns are normally filed either before the request or '
     +'with it.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Test</th>'
   +'<th scope="col">What it asks</th><th scope="col">On these answers</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>The ten-year window</td><td>Tax year ending '+WFIRST
   +' or later</td><td>'+(inWindow?'Met, '+yr:'Not met, '+yr)+'</td></tr>';
  h+='<tr><td>A ground</td>'
   +'<td>Extraordinary circumstances, an Agency action, or inability to pay'
   +'</td><td>'+(ground==='y'?'Identified':'None identified')+'</td></tr>';
  h+='<tr><td>The returns are filed</td>'
   +'<td>The years the request covers have been filed</td><td>'
   +(filed==='y'?'Yes':'Not yet')+'</td></tr>';
  h+='<tr><td>Something to relieve</td>'
   +'<td>A penalty or interest was actually charged</td><td>'
   +(nil==='y'?'No, the years were nil':'Yes')+'</td></tr>';
  h+='</tbody></table>';
  if(filed==='n'){
    h+='<p>The returns themselves come first. A request to cancel the '
     +'charges on a year that has still not been filed leaves the year open '
     +'and the charges running, and the '
     +'<a href="SITECATCHUP">catch-up filing schedule generator</a> puts '
     +'them in order.</p>';
  }
  if(nil==='y'){
    h+='<p>Nil T2 filing at '+PRICE_JS+' closes one tax year per return. '
     +NOTNILJS+'</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITECATCHUP', CATCHUP) \
   .replace('WINDOWFIRST', str(WINDOW_FIRST)) \
   .replace('WINDOWYEARS', str(WINDOW_YEARS))

T105 = dict(
 slug='taxpayer-relief-eligibility-checker',
 title='Taxpayer Relief Eligibility Checker | Ten-Year Window',
 h1_pre='Taxpayer Relief ', h1_span='Eligibility Checker',
 h1='Taxpayer Relief Eligibility Checker',
 eyebrow='Relief',
 keyword='taxpayer relief eligibility',
 seo_title='Taxpayer Relief Eligibility Checker',
 seo_desc=('Relief reaches a tax year ending within the ten calendar years '
           'before the request, and it cancels penalties and interest, never '
           'tax.'),
 meta=('The Minister may cancel penalties and interest on specified grounds, '
       'but only for a tax year inside the ten-year window.'),
 tags=['Ten-year window', 'Penalties and interest only',
       'Discretionary, on grounds', 'Form RC4288'],
 form=tool('The year and the grounds',
           [num('yr', 'The tax year the penalty or interest relates to',
                'A four-digit year', 1970, WINDOW_BASE, '2019'),
            yn('ground', 'Extraordinary circumstances, an Agency action, or '
                         'an inability to pay?'),
            yn('filed', 'Have the returns for that year been filed?'),
            yn('nil', 'Was the year a nil year?')],
           'Enter the year and answer the three questions.'),
 js=None,
 sections=[
  ('window', 'The Ten-Year Window Is the First Test',
   '<p>Subsection 220(3.1) of the Income Tax Act lets the Minister waive or '
   'cancel a penalty or interest. The discretion is bounded: a request may '
   'only reach a tax year that ended within the ten calendar years before '
   'the calendar year in which the request is made. A request made during '
   + str(WINDOW_BASE) + ' therefore reaches tax years ending in '
   + str(WINDOW_FIRST) + ' or later.</p>\n'
   '<p>The window moves every January, which cuts both ways: waiting a year '
   'to ask does not improve a request and can put the oldest year it covers '
   'permanently out of reach.</p>'),
  ('what-it-reaches', 'It Cancels Charges, Not Tax',
   _tbl(['What was assessed', 'Can relief reach it'],
        [['Late-filing penalty', 'Yes, on grounds and inside the window'],
         ['Arrears interest', 'Yes, on the same basis'],
         ['The tax itself', 'No. Relief never touches the tax'],
         ['A charge on a nil year', 'There is none to reach']])
   + '\n<p>That last row is where most corporate enquiries about relief '
   'actually land. A true nil year carried no percentage penalty and no '
   'interest, so a request has nothing to cancel, and the thing that closes '
   'the year is the return. The '
   + a(P_LATE, 'T2 late filing penalty calculator')
   + ' shows the arithmetic that produces $0.00, and the '
   + a(NILPEN, 'nil return late penalty checker')
   + ' sets out what an open year costs instead of a percentage.</p>\n'
   '<p>' + CLOSE['taxpayer-relief-eligibility-checker'] + '</p>'),
  ('grounds', 'The Grounds, and the Order of Operations',
   '<p>Three groups of circumstances are recognised: extraordinary '
   'circumstances outside the taxpayer&rsquo;s control, such as a natural '
   'disaster, a serious illness or a death; actions of the Canada Revenue '
   'Agency itself, such as processing delays or incorrect information; and '
   'an inability to pay or financial hardship. Form RC4288 is the request, '
   'and it is decided case by case.</p>\n'
   '<p>Outstanding returns are filed before the request or with it. Asking '
   'for charges to be cancelled on a year that has not been filed leaves the '
   'year open, so '
   + a(COST, 'nil T2 filing at ' + PRICE)
   + ' or the '
   + a(CATCHUP, 'catch-up filing schedule generator')
   + ' comes first. A correction made before the Agency acts is a different '
   'route again, and the '
   + a(P_VDP, 'voluntary disclosure eligibility checker')
   + ' covers it. The '
   + a(G_ARREARS, 'guide to corporate tax arrears and interest')
   + ' covers what the charges are before any request to cancel them.</p>'),
 ],
 faq=[
  ('What is taxpayer relief?',
   'A discretionary cancellation or waiver of penalties and interest by the '
   'Minister under subsection 220(3.1) of the Income Tax Act.'),
  ('How far back can a request go?',
   'To a tax year that ended within the ten calendar years before the '
   'calendar year the request is made in.'),
  ('Can relief cancel the tax owing?',
   'No. It reaches penalties and interest only. The tax itself stands.'),
  ('What grounds are recognised?',
   'Extraordinary circumstances outside your control, actions of the Canada '
   'Revenue Agency, and an inability to pay or financial hardship.'),
  ('Which form is used?',
   'Form RC4288, the request for taxpayer relief.'),
  ('Is relief automatic once a ground applies?',
   'No. It is discretionary and each request is decided on its own facts.'),
  ('Does a nil year qualify for relief?',
   'There is nothing to relieve. A true nil year carries no percentage '
   'penalty and no interest, so filing the return is what resolves it.'),
  ('Do the returns have to be filed first?',
   'They are normally filed before the request or with it. An unfiled year '
   'stays open regardless of the request.'),
  ('Is this the same as a voluntary disclosure?',
   'No. A disclosure corrects a position before the Agency acts; relief '
   'asks for charges already assessed to be cancelled.'),
  ('Does the window move?',
   'Yes, every calendar year, so the oldest year a request can reach moves '
   'forward each January.'),
 ],
 related=[
  (P_VDP, 'Voluntary disclosure eligibility checker'),
  (P_LATE, 'T2 late filing penalty calculator'),
  (P_REPEAT, 'Repeated failure to file penalty calculator'),
  (NILPEN, 'Nil return late penalty checker'),
  (CATCHUP, 'Catch-up filing schedule generator'),
  (ARB, 'Arbitrary assessment response checker'),
 ],
)

TOOLS16 = [T101, T102, T103, T104, T105]
_JS16 = [T101_JS, T102_JS, T103_JS, T104_JS, T105_JS]

STRUCTURE = dict(sections=3, faq=10, related=6, tags=4,
                 body_tables=1, result_tables=1)


def wire(form):
    sel = []
    for tag in _re.findall(r'<input\b[^>]*>', form):
        if 'type="radio"' in tag:
            m = _re.search(r'name="([\w-]+)"', tag)
            if m and 'input[name="%s"]' % m.group(1) not in sel:
                sel.append('input[name="%s"]' % m.group(1))
        else:
            m = _re.search(r'id="([\w-]+)"', tag)
            if m and '#' + m.group(1) not in sel:
                sel.append('#' + m.group(1))
    assert sel, 'a tool form has no input controls'
    return ("\nArray.prototype.forEach.call(\n"
            "  document.querySelectorAll('" + ','.join(sel) + "'),\n"
            "  function(el){el.addEventListener('change',show);"
            "el.addEventListener('input',show);});\nshow();\n")


# RBASE carries PRELUDE, and PRELUDE embeds build_f2.NOT_NIL, which names the
# overflow price with HST. A national tool cannot. Same 2026-11-12 correction
# build_f2o.py applies, shadowed here rather than edited in build_f2.
OVERFLOW_WAS = '$350.00 plus HST per year'
OVERFLOW_NOW = '$350.00 plus applicable sales tax per year'

for _t, _js in zip(TOOLS16, _JS16):
    assert OVERFLOW_WAS in _js, (
        '%s: the overflow price moved; re-check the shadow' % _t['slug'])
    _t['js'] = (_js + wire(_t['form'])).replace(OVERFLOW_WAS, OVERFLOW_NOW)

# ---- the contract, as batch 14 and 15 state it --------------------------
_LIVE = {f[:-5] for f in os.listdir(HERE) if f.endswith('.html')}
_THIS = {t['slug'] for t in TOOLS16}
_EARLIER = _LIVE - _THIS
assert len(_EARLIER) >= 101, (
    'expected at least the 101 tools of batches 1 to 15, found %d'
    % len(_EARLIER))
PUBLISHED = _THIS <= _LIVE

_PLAN = io.open(os.path.join(HERE, '..', '..', 'docs',
                             'corpnilfilingfor300-seo-website-plan.md'),
                encoding='utf-8').read()
for t in TOOLS16:
    assert '\n/%s/\n' % t['slug'] in _PLAN, (
        '%s is not an Appendix A URL' % t['slug'])

for t in TOOLS16:
    s = t['slug']
    if not PUBLISHED:
        assert s not in _LIVE, '%s already exists; pick another slug' % s
    assert len(t['sections']) == STRUCTURE['sections'], s
    assert len(t['faq']) == STRUCTURE['faq'], s
    assert len(t['related']) == STRUCTURE['related'], s
    assert len(t['tags']) == STRUCTURE['tags'], s
    assert sum('<table class="ei-tbl"' in h for _i, _h2, h in t['sections']) \
        >= STRUCTURE['body_tables'], '%s: no static table in the body' % s
    assert t['js'].count('<table class="ei-tbl"') \
        >= STRUCTURE['result_tables'], '%s: the result draws no table' % s
    assert len(t['seo_title']) <= 60, (s, len(t['seo_title']))
    assert 70 <= len(t['seo_desc']) <= 160, (s, len(t['seo_desc']))

    _vars = _re.findall(r'^var ([A-Za-z_]\w*)=', t['js'], _re.M)
    _dupe = sorted({v for v in _vars if _vars.count(v) > 1})
    assert not _dupe, (
        '%s: the module declares %s more than once, which means PRELUDE was '
        'prepended on top of a module that already carried it' % (s, _dupe))

    _body = ''.join(h for _i, _h2, h in t['sections'])
    assert CLOSE[s] in _body, '%s: its closing sentence is missing' % s

    for _form in ('CO-17', 'AT1'):
        if _form in _body:
            assert 'separate' in _body, (
                '%s: names %s without calling it a separate return' % (s, _form))

    radios, fields = set(), set()
    for tag in _re.findall(r'<input\b[^>]*>', t['form']):
        if 'type="radio"' in tag:
            m = _re.search(r'name="([\w-]+)"', tag)
            if m:
                radios.add(m.group(1))
        else:
            m = _re.search(r'id="([\w-]+)"', tag)
            if m:
                fields.add(m.group(1))
    for nm in radios:
        assert "'%s'" % nm in t['js'], '%s: radio %s is never read' % (s, nm)
    for fid in fields:
        assert "'%s'" % fid in t['js'], '%s: field %s is never read' % (s, fid)
    for nm in set(_re.findall(r"pick\('([\w-]+)'\)", t['js'])):
        assert nm in radios, '%s: js reads radio %s the form lacks' % (s, nm)
    for fid in set(_re.findall(r"parse\('([\w-]+)'\)", t['js'])
                   + _re.findall(r"getElementById\('([\w-]+)'\)", t['js'])):
        if fid != 'out':
            assert fid in fields, \
                '%s: js reads field %s the form lacks' % (s, fid)

    _all = (t['form'] + _body + ''.join(q + aa for q, aa in t['faq'])
            + ''.join(u2 for u2, _x in t['related']) + t['js'])
    for u in _re.findall(r'href="' + SITE + r'/tools/([a-z0-9-]+)/"', _all):
        assert u in _LIVE or u in _THIS, '%s: links to missing tool %s' % (s, u)
    _F9 = {f[:-5] for f in os.listdir(os.path.join(HERE, '..', 'f9'))
           if f.endswith('.html')}
    for u in _re.findall(r'href="' + SITE + r'/guides/([a-z0-9-]+)/"', _all):
        assert u in _F9, '%s: links to missing guide %s' % (s, u)

    # Hard rules. A national tool names no HST and no bare T183.
    assert 'plus HST' not in _all and 'including HST' not in _all, \
        '%s: names HST on a national tool' % s
    assert not _re.search(r'\bT183\b(?!CORP)', _all), '%s: bare T183' % s
    assert 'FAQPage' not in _all and 'aggregateRating' not in _all, s
    assert 'HowTo' not in _all, s
    _low = _all.lower()
    for _w in ('cheapest', 'best price', 'fastest', 'guaranteed', 'risk-free',
               'book a call', 'calendly', 'cra approved', 'cra agent',
               'cra authorized', 'cra authorised', 'cra partner'):
        assert _w not in _low, '%s: banned phrase "%s"' % (s, _w)
    # Hard rule 3: "no penalty" never stands alone. QUAL says "no
    # percentage late-filing penalty", so the bare phrase appears nowhere on
    # the 101 live pages either. The meta fields are checked too, because
    # they are not part of _all and Rank Math publishes them verbatim.
    _low = (_all + t['seo_title'] + t['seo_desc'] + t['meta']).lower()
    # The two-word form, and anything that slips words between "no" and
    # "penalty": "so no late-filing penalty arises" shipped past the first
    # version of this check and had to be caught by hand on 2026-11-20.
    # QUAL's own wording is the whole point of rule 3 and is permitted; so is
    # a statement about a PRIOR penalty, which is a fact about an earlier
    # assessment rather than a claim about this return.
    _R3_OK = {'no percentage late-filing penalty', 'no percentage penalty',
              'no prior penalty'}
    for _m in _re.finditer(r'\bno (?:[a-z-]+ ){0,3}penalt\w*', _low):
        _p = _m.group(0)
        _p = _re.sub(r'(penalty|penalties)\w*$', r'\1', _p)
        if not any(_p.startswith(_ok) for _ok in _R3_OK):
            raise AssertionError(
                '%s: rule 3, unqualified %r. Permitted: %s'
                % (s, _m.group(0), sorted(_R3_OK)))
    for _m in _re.finditer(r'penalty[- ]free|zero penalt', _low):
        raise AssertionError('%s: rule 3, %r' % (s, _m.group(0)))

assert len({t['seo_title'] for t in TOOLS16}) == len(TOOLS16), 'title clash'
assert len({t['seo_desc'] for t in TOOLS16}) == len(TOOLS16), 'desc clash'
assert len({t['keyword'] for t in TOOLS16}) == len(TOOLS16), 'keyword clash'
assert len({t['h1'] for t in TOOLS16}) == len(TOOLS16), 'h1 clash'


# ---- the shipped-script gate -------------------------------------------
# Batch 16 published t2-late-filing-penalty-calculator with
#
#     while(n<12&&addMonths(due,n+1).getTime()<=filed.getTime()){n++;}
#
# and the live page threw "Invalid or unexpected token" with the calculator
# dead, because WordPress had rewritten that "&&" as "&#038;&#038;". Inside a
# <script> element character references are NOT decoded, so the entity is a
# syntax error rather than an operator.
#
# The cause is the "<12&&" : a "<" that is followed by anything WordPress's
# filters read as the start of a tag swallows text to the next ">", and an "&"
# inside that span is entity-encoded on output. The 101 pages of batches 1 to
# 15 all carry "w!==0&&w!==6&&!isHoliday(dt)" and are untouched, because none
# of them puts a "<" hard against a token with an "&" after it.
#
# Nothing caught it: the builder's contract reads the tool dicts, gate_batch
# reads the rendered file, gate_f2_all compares pages, and test_f2p_dom runs
# the LOCAL module. All four see the correct "&&". Only the bytes WordPress
# serves are wrong, so the check has to be on the shape that provokes the
# rewrite rather than on the output.
def script_entity_risk(html):
    """Spans inside <script> where an & sits in a tag-like region.

    Returns a list of offending excerpts. A "<" followed by a letter, "!" or
    "/" opens such a region; it closes at the next ">". An "&" inside one is
    rewritten by WordPress and corrupts the module.
    """
    bad = []
    for m in _re.finditer(r'<script\b[^>]*>(.*?)</script>', html, _re.S):
        body = m.group(1)
        for t in _re.finditer(r'<[A-Za-z!/][^>]*', body):
            if '&' in t.group(0):
                bad.append(t.group(0)[:160])
    return bad


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = TODAY, ISO
    build_f2.PRICE = PRICE      # so render()'s PRICE_JS matches the bodies
    recs = []
    for t in TOOLS16:
        html, url = render(t)
        assert 'plus HST' not in html, '%s still names HST' % t['slug']
        _risk = script_entity_risk(html)
        assert not _risk, (
            '%s: an & sits inside a tag-like span in a <script>, which '
            'WordPress will entity-encode and which breaks the module on the '
            'live page. Offending: %r' % (t['slug'], _risk))
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2p-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-48s %6d bytes' % (r['slug'], len(r['content'].encode())))
