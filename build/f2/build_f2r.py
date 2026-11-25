# -*- coding: utf-8 -*-
"""Family 2 batch 18: five more Appendix A tools.

Navneet, 2026-11-23: "next 5 calculators next ones". Same three tests batches
16 and 17 used: the term is one people search, no live tool answers it, and the
answer routes back to a nil T2.

  112  /tools/failure-to-comply-penalty-calculator/             Appendix A 2796
  113  /tools/schedule-1-net-income-reconciliation-calculator/  Appendix A 2878
  114  /tools/gst-hst-filing-frequency-calculator/              Appendix A 2960
  115  /tools/payroll-remittance-due-date-calculator/           Appendix A 2976
  116  /tools/shareholder-loan-income-inclusion-calculator/     Appendix A 2998

One per subject group on the tools hub, deliberately: penalties, schedules,
GST/HST, payroll and shareholders. Batch 17 put two penalty tools in one batch
and both landed in the same hub group.

WHAT EACH ONE ADDS THAT A LIVE TOOL DOES NOT
--------------------------------------------
Checked against all 111 live slugs, because batch 16 found seven Appendix A
entries a live tool already answered.

- 112 against the three live penalty tools and batch 17's two: 162(1), 162(2)
  and 163(2) are all percentages of an amount of tax. 162(7) is the one
  provision in the set whose base is nothing at all -- the greater of $100.00
  and $25.00 a day to a hundred days -- which makes it the only one of them
  that bites a corporation owing $0.00. That is the whole point of the page.
- 113 against live /tools/gifi-schedule-125-checker/,
  /tools/nil-gifi-balance-sheet-checker/ and
  /tools/schedule-8-cca-requirement-checker/: those cover the GIFI statements
  and the capital cost allowance schedule. None of them reconciles the
  accounting figure to the tax one, which is the single arithmetic step
  between Schedule 125 and line 300 of the return.
- 114 against live /tools/gst-hst-nil-filing-checker/,
  /tools/gst-hst-nil-return-deadline-calculator/ and batch 17's
  /tools/gst-hst-registration-requirement-checker/: 111 answers whether an
  account must exist, the deadline tool answers when a period's return is due
  once the period is known. Nothing on the site decides which period applies,
  and that is the input the deadline tool assumes the visitor already has.
- 115 against live /tools/payroll-nil-remittance-checker/ and
  /tools/payroll-account-closure-checker/: one answers whether a nil
  remittance is owed, the other how to close the account. Neither carries a
  date, and the remitter type that sets the date is fixed by a figure from two
  calendar years ago, which is the part people get wrong.
- 116 against batch 17's /tools/shareholder-loan-repayment-deadline-calculator/
  and live /tools/shareholder-loan-balance-checker/: 108 gives the date. This
  gives the consequence of missing it -- the amount, whose income it goes in,
  which tax year it lands in, and what reverses it.

WHY 116 EXISTS SEPARATELY FROM 108
----------------------------------
108 was built to get the attribution right: a loan that misses the 15(2.6)
deadline is included in the SHAREHOLDER's income, not the corporation's. 116
is the arithmetic half of the same point. It states the amount, names the two
taxpayers in separate rows, and says the corporation's own year can still be
nil. The subsection 80.4(2) interest benefit is named but never computed,
because the prescribed rate moves every quarter and this file does not assert
a rate from memory.

WHAT IS NOT HERE
----------------
/tools/cra-arrears-interest-calculator/ and
/tools/shareholder-loan-prescribed-interest-calculator/ were both on the
shortlist and both dropped for the same reason: each needs the prescribed
interest rate for a quarter, and those are published quarterly and are not
facts to state from memory on a CPA firm's site.

/tools/small-business-deduction-limit-calculator/ was dropped on a different
ground. The business limit grind now runs on two tests, a taxable capital one
whose upper bound moved and a passive income one, and getting the effective
date of that change wrong would be worse than not building the page.

/tools/paid-up-capital-calculator/ and
/tools/capital-dividend-account-calculator/ were dropped on scope: both are
multi-year running balances rather than a single computation, and neither has
anything to do with whether a quiet year is nil.

THE FEE WORDING
---------------
All five are national tools, so none names HST. Same 2026-11-12 decision and
the same shadowing of PRICE and the overflow price that build_f2o.py,
build_f2p.py and build_f2q.py record.
"""
import io, json, os, sys
import re as _re

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_f2 import render, meta, yn, a, SITE, HUB, FORM, TOOL_DISCLAIMER
from build_f2b import tool, num, date, T, G, COST
from build_f2c import MONEY_JS
from build_f2f import RBASE
from build_f2p import script_entity_risk

PRICE = '$300.00 plus applicable sales tax per tax year'
TODAY, ISO = 'November 23, 2026', '2026-11-23'

# Live tools these five link to; every one asserted to exist below.
P_LATE    = T + 't2-late-filing-penalty-calculator/'
P_REPEAT  = T + 'repeated-failure-to-file-penalty-calculator/'
P_GROSS   = T + 'gross-negligence-penalty-checker/'
P_NILPEN  = T + 'nil-return-late-penalty-checker/'
P_NRPEN   = T + 'non-resident-t2-penalty-calculator/'
P_RELIEF  = T + 'taxpayer-relief-eligibility-checker/'
P_VDP     = T + 'voluntary-disclosure-eligibility-checker/'
P_DEMAND  = T + 'cra-demand-to-file-deadline-calculator/'
P_ARB     = T + 'arbitrary-assessment-response-checker/'
P_T4PEN   = T + 't4-late-filing-penalty-calculator/'
P_T4REQ   = T + 't4-nil-filing-requirement-checker/'
P_PAYNIL  = T + 'payroll-nil-remittance-checker/'
P_PAYCLOSE= T + 'payroll-account-closure-checker/'
P_SEQ     = T + 'cra-account-closure-sequencer/'
P_STAND   = T + 'cra-account-standing-checker/'
P_GSTREG  = T + 'gst-hst-registration-requirement-checker/'
P_GSTNIL  = T + 'gst-hst-nil-filing-checker/'
P_GSTDUE  = T + 'gst-hst-nil-return-deadline-calculator/'
P_GSTCLOSE= T + 'gst-hst-account-closure-checker/'
P_G125    = T + 'gifi-schedule-125-checker/'
P_G141    = T + 'gifi-schedule-141-checker/'
P_GREQ    = T + 'gifi-schedule-requirement-checker/'
P_NILGIFI = T + 'nil-gifi-balance-sheet-checker/'
P_CCA     = T + 'schedule-8-cca-requirement-checker/'
P_REQSCH  = T + 'required-schedules-checker/'
P_EXPONLY = T + 'expenses-only-year-checker/'
P_SHBAL   = T + 'shareholder-loan-balance-checker/'
P_SHDUE   = T + 'shareholder-loan-repayment-deadline-calculator/'
P_SHDIR   = T + 'due-to-versus-due-from-shareholder-checker/'
P_SCH11   = T + 'schedule-11-shareholder-transactions-checker/'
P_SCH50   = T + 'schedule-50-shareholder-threshold-checker/'
P_DORM    = T + 'dormant-corporation-test/'
P_REQD    = T + 't2-filing-requirement-checker/'
P_NILDUE  = T + 'nil-t2-deadline-calculator/'

# This batch's own, for cross-links.
R_COMPLY  = T + 'failure-to-comply-penalty-calculator/'
R_SCH1    = T + 'schedule-1-net-income-reconciliation-calculator/'
R_FREQ    = T + 'gst-hst-filing-frequency-calculator/'
R_REMIT   = T + 'payroll-remittance-due-date-calculator/'
R_SHINC   = T + 'shareholder-loan-income-inclusion-calculator/'

# Section 6(g) guides.
G_PEN     = G + 't2-late-filing-penalties/'
G_PAY     = G + 'cra-accounts-on-a-dormant-corporation/'
G_GIFI    = G + 'gifi-schedules-100-125-141/'
G_SCHED   = G + 't2-schedules-on-a-nil-return/'
G_SHARE   = G + 'schedule-50-and-shareholder-reporting/'
G_DEMAND  = G + 'cra-demand-to-file-response/'
G_DORMANT = G + 'dormant-and-inactive-corporations/'


def _tbl(head, rows):
    return ('<table class="ei-tbl"><thead><tr>'
            + ''.join('<th scope="col">%s</th>' % h for h in head)
            + '</tr></thead><tbody>\n'
            + '\n'.join('<tr>' + ''.join('<td>%s</td>' % c for c in r)
                        + '</tr>' for r in rows)
            + '\n</tbody></table>')


CLOSE = {
 'failure-to-comply-penalty-calculator':
   'A percentage of nothing is nothing, which is exactly why the flat and '
   'daily charges are the ones a dormant corporation has to watch.',
 'schedule-1-net-income-reconciliation-calculator':
   'Schedule 1 is a bridge rather than a second income statement: it starts '
   'at the accounting figure and ends at the one the return taxes.',
 'gst-hst-filing-frequency-calculator':
   'The supplies set the frequency, an election can only make the periods '
   'shorter, and a dormant registrant still files on whichever one applies.',
 'payroll-remittance-due-date-calculator':
   'The remitter type is set by what the payroll looked like two years ago '
   'rather than what it looks like now, which is how a wound-down payroll '
   'ends up on an accelerated schedule.',
 'shareholder-loan-income-inclusion-calculator':
   'The amount goes in the shareholder&rsquo;s income for the year the loan '
   'was received, which is why the consequence usually lands on a personal '
   'return that was filed long ago.',
}

# ====================================== 112. failure to comply, 162(7)
T112_JS = RBASE + MONEY_JS + r"""
var FLOOR=10000,DAILY=2500,CAPDAYS=100;
var out=document.getElementById('out');
function scale(mark){
  var ROWS=[[1,'1 day'],[3,'3 days'],[4,'4 days'],[5,'5 days'],
            [20,'20 days'],[100,'100 days'],[365,'365 days']];
  var h='<table class="ei-tbl"><thead><tr>'
   +'<th scope="col">The failure continues</th>'
   +'<th scope="col">$25.00 a day</th>'
   +'<th scope="col">Penalty under 162(7)</th>'
   +'<th scope="col">Your answer</th></tr></thead><tbody>';
  for(var i=0;i!==ROWS.length;i++){
    var d=ROWS[i][0],cap=d;
    if(cap > CAPDAYS){cap=CAPDAYS;}
    var raw=DAILY*cap,amt=raw;
    if(FLOOR > amt){amt=FLOOR;}
    h+='<tr><td>'+ROWS[i][1]+'</td><td>'+money(DAILY*cap)+'</td><td>'
     +money(amt)+'</td><td>'+(d===mark?'Yes':'')+'</td></tr>';
  }
  h+='</tbody></table>';
  return h;
}
function show(){
  var raw=document.getElementById('days').value.trim(),
      info=pick('info'),wait=0;
  if(raw===''){wait++;}
  if(info===null){wait++;}
  if(wait > 0){
    out.innerHTML='<p>'+wait+' of the two answers '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var days=parseInt(raw,10),h;
  if(isNaN(days)||0 > days){
    out.innerHTML='<p>Enter the number of days as a whole number.</p>';return;
  }
  if(info==='y'){
    h='<h3>A slip return is charged under subsection 162(7.01) instead</h3>';
    h+='<p>Subsection 162(7) is the residual provision. Where the failure is '
     +'a late information return carrying slips, the sliding scale in '
     +'subsection 162(7.01) applies to it and this one does not. The '
     +'<a href="SITET4PEN">T4 late filing penalty calculator</a> runs that '
     +'scale, which is set by how many slips the return carries.</p>';
    h+=scale(0);
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  if(days===0){
    h='<h3>Nothing has run yet, so the daily charge is $0.00</h3>';
    h+='<p>The charge runs for each day the failure continues. At zero days '
     +'the daily figure is $0.00 and the floor has not been reached either, '
     +'because the floor applies to a failure that has begun. The table '
     +'below is what one day onward costs.</p>';
    h+=scale(0);
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  var cap=days,note='';
  if(cap > CAPDAYS){cap=CAPDAYS;note=' The count stops at 100 days, so the '
   +'figure does not grow after that however long the failure continues.';}
  var rawAmt=DAILY*cap,amt=rawAmt,why;
  if(FLOOR > amt){amt=FLOOR;why='the daily figure of '+money(rawAmt)
   +' is below the $100.00 floor, so the floor applies';}
  else{why='the daily figure of '+money(rawAmt)+' is above the $100.00 '
   +'floor, so the daily figure applies';}
  h='<h3>'+money(amt)+' under subsection 162(7)</h3>';
  h+='<p>At '+plural(days,'day')+', '+why+'.'+note+' The provision charges '
   +'the greater of $100.00 and $25.00 multiplied by the number of days, to '
   +'a maximum of 100 days, which puts the whole provision between $100.00 '
   +'and $2,500.00.</p>';
  h+=scale(days > 365?0:days);
  h+='<p>This figure does not depend on tax being owed. A corporation that '
   +'owes $0.00 is charged the same amount as one that owes a great deal, '
   +'which is what separates this provision from the percentage ones. The '
   +'<a href="SITELATE">T2 late filing penalty calculator</a> and the '
   +'<a href="SITEREPEAT">repeated failure to file penalty calculator</a> '
   +'run those, and both come to $0.00 on a true nil year.</p>';
  h+='<p>Nil T2 filing itself is '+PRICE_JS+' and each unfiled year is its '
   +'own return at that fee. '+NOTNILJS+'</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITET4PEN', P_T4PEN).replace('SITELATE', P_LATE) \
   .replace('SITEREPEAT', P_REPEAT)

T112 = dict(
 slug='failure-to-comply-penalty-calculator',
 title='Failure to Comply Penalty Calculator | Subsection 162(7)',
 h1_pre='Failure to Comply ', h1_span='Penalty Calculator',
 h1='Failure to Comply Penalty Calculator',
 eyebrow='Penalties',
 keyword='failure to comply penalty',
 seo_title='Failure to Comply Penalty Calculator',
 seo_desc=('Subsection 162(7) charges the greater of $100.00 and $25.00 a '
           'day, counted to 100 days. Enter the days to see the figure.'),
 meta=('The one penalty in the set whose base is nothing at all, which is '
       'why it is the one a corporation owing $0.00 still has to watch.'),
 tags=['Greater of $100.00 and $25.00 a day', 'Counted to 100 days',
       'Not a percentage of tax', 'Subsection 162(7)'],
 form=tool('The failure',
           [num('days', 'Days the failure has continued',
                'Counted from the day the filing or the request was due',
                0, 3650, '0'),
            yn('info', 'Is it a late information return carrying slips, '
                       'such as a T4 or a T5018?')],
           'Enter the days and answer the question above.'),
 js=None,
 sections=[
  ('greater-of', 'The Greater of $100.00 and $25.00 a Day, Counted to 100 Days',
   '<p>Subsection 162(7) is the residual penalty in the Income Tax Act. It '
   'reaches a failure to file an information return when no other provision '
   'covers it, and a failure to comply with any other duty or obligation the '
   'Act or the Regulations impose. The charge is the greater of $100.00 and '
   '$25.00 multiplied by the number of days the failure continues, with the '
   'day count stopping at 100.</p>\n'
   '<p>Two things follow from that shape. The first four days all cost '
   '$100.00, because four days at $25.00 is exactly the floor and anything '
   'shorter is below it. And the charge stops growing at $2,500.00, which it '
   'reaches on the hundredth day, however many years the failure then '
   'continues.</p>\n'
   + _tbl(['The failure continues', '$25.00 a day', 'Penalty under 162(7)'],
          [['1 day', '$25.00', '$100.00'],
           ['3 days', '$75.00', '$100.00'],
           ['4 days', '$100.00', '$100.00'],
           ['5 days', '$125.00', '$125.00'],
           ['20 days', '$500.00', '$500.00'],
           ['100 days', '$2,500.00', '$2,500.00'],
           ['365 days', 'Counted to 100 days', '$2,500.00']])),
  ('which-provision', 'Five Penalties, and the Base Each One Multiplies',
   '<p>Most of the late-filing provisions people have in mind are '
   'percentages of an amount of tax. This one is not, and that single '
   'difference is why it matters to a corporation with nothing to report.</p>\n'
   + _tbl(['Provision', 'What it charges', 'What it multiplies'],
          [['162(1), a late return of income',
            '5% of the unpaid tax, plus 1% a month to 12 months',
            'Tax unpaid at the due date'],
           ['162(2), a repeated failure after a demand',
            '10% of the unpaid tax, plus 2% a month to 20 months',
            'Tax unpaid at the due date'],
           ['162(7), a failure to comply',
            'The greater of $100.00 and $25.00 a day to 100 days',
            'Nothing. It is a flat and daily amount'],
           ['162(7.01), an information return with slips',
            'A daily rate set by the slip count, with a floor and a ceiling',
            'Nothing. The slip count picks the band'],
           ['163(2), gross negligence',
            '50% of the understated tax, subject to a minimum',
            'Tax that was understated']])
   + '\n<p>The two percentage provisions are run by the '
   + a(P_LATE, 'T2 late filing penalty calculator')
   + ' and the '
   + a(P_REPEAT, 'repeated failure to file penalty calculator')
   + '. The slip scale is run by the '
   + a(P_T4PEN, 'T4 late filing penalty calculator')
   + ', and subsection 163(2) has a checker of its own in the list below. '
   'The '
   + a(G_PEN, 'guide to T2 late filing penalties')
   + ' sets out how they interact.</p>'),
  ('on-a-nil-year', 'Why This Is the Provision a Dormant Corporation Watches',
   '<p>A true nil return carries no percentage late-filing penalty, because '
   'that penalty is a percentage of tax owing and the corporation owes '
   '$0.00. That is a real and useful point, and it is also the point people '
   'stop at. The exposure on a quiet corporation is not the percentage '
   'provisions at all. It is the flat ones, the ones that do not ask what is '
   'owed.</p>\n'
   '<p>The unfiled year also stays open indefinitely, invites a demand to '
   'file and then an arbitrary assessment, and blocks the clearance '
   'certificate a dissolution needs. The '
   + a(P_DEMAND, 'CRA demand to file deadline calculator')
   + ' and the '
   + a(P_ARB, 'arbitrary assessment response checker')
   + ' cover that sequence, and a non-resident-owned corporation has its own '
   'daily charge, which the '
   + a(P_NRPEN, 'non-resident T2 penalty calculator')
   + ' computes.</p>\n'
   '<p>' + a(COST, 'Nil T2 filing at ' + PRICE)
   + ' covers the federal corporate income tax return for one tax year, and '
   'each unfiled year is its own return at that fee. Where a charge has '
   'already been assessed, the '
   + a(P_RELIEF, 'taxpayer relief eligibility checker')
   + ' sets out the grounds for having it reconsidered, and a voluntary '
   'disclosure is the other route where the filings themselves are the '
   'problem.</p>\n'
   '<p>' + CLOSE['failure-to-comply-penalty-calculator'] + '</p>'),
 ],
 faq=[
  ('How much is the penalty under subsection 162(7)?',
   'The greater of $100.00 and $25.00 multiplied by the number of days the '
   'failure continues, with the day count stopping at 100. That puts it '
   'between $100.00 and $2,500.00.'),
  ('Does it depend on how much tax is owing?',
   'No. It is a flat and daily amount, which is what makes it the provision '
   'that still reaches a corporation owing $0.00.'),
  ('What is the maximum?',
   '$2,500.00. The day count stops at 100, so the figure does not grow '
   'after the hundredth day.'),
  ('Is there a minimum?',
   'Yes, $100.00. The first four days all come to $100.00, because four days '
   'at $25.00 is the floor exactly.'),
  ('Does it apply to a late T2 return?',
   'A return of income is charged under subsection 162(1) instead. This '
   'provision is the residual one, for information returns no other '
   'provision covers and for other duties under the Act.'),
  ('Does it apply to late T4 slips?',
   'No. An information return carrying slips is charged on the sliding scale '
   'in subsection 162(7.01), which is set by the slip count.'),
  ('What kind of failure does it actually cover?',
   'A failure to file an information return that no other provision reaches, '
   'and a failure to comply with another duty or obligation the Act or the '
   'Regulations impose.'),
  ('Can it be charged on a nil year?',
   'It can. Nothing in the provision asks whether any tax was payable, which '
   'is the difference between it and the percentage provisions.'),
  ('Can it be cancelled?',
   'Relief can be requested on the statutory grounds, and the request reaches '
   'back ten years. Cancelling a charge is discretionary rather than '
   'automatic, so the request has to be made on one of those grounds.'),
  ('Does the nil T2 fee cover an assessed penalty?',
   'No. The fee covers preparing and transmitting the corporate income tax '
   'return. An amount the Agency has already assessed sits outside it.'),
 ],
 related=[
  (P_LATE, 'T2 late filing penalty calculator'),
  (P_REPEAT, 'Repeated failure to file penalty calculator'),
  (P_T4PEN, 'T4 late filing penalty calculator'),
  (P_GROSS, 'Gross negligence penalty checker'),
  (P_RELIEF, 'Taxpayer relief eligibility checker'),
  (P_NRPEN, 'Non-resident T2 penalty calculator'),
 ],
)

# ====================================== 113. Schedule 1 reconciliation
T113_JS = RBASE + MONEY_JS + r"""
var out=document.getElementById('out');
function amt(c){return (0 > c)?('minus '+money(-c)):money(c);}
function cents(id){
  var v=document.getElementById(id).value.trim();
  if(v===''){return null;}
  var n=parseFloat(v.replace(/,/g,''));
  if(isNaN(n)){return undefined;}
  return Math.round(n*100);
}
function show(){
  var IDS=['acc','amort','cca','meals','addother','dedother'],v={},bad=0,i;
  for(i=0;i!==IDS.length;i++){
    var c=cents(IDS[i]);
    if(c===undefined){bad++;}
    v[IDS[i]]=(c===null||c===undefined)?0:c;
  }
  if(bad > 0){
    out.innerHTML='<p>One of the figures could not be read. Enter dollar '
     +'amounts without symbols.</p>';return;
  }
  var mealsBack=Math.round(v.meals/2);
  var line300=v.acc+v.amort-v.cca+mealsBack+v.addother-v.dedother;
  var h,ROWS=[
    ['Net income or loss per the financial statements',v.acc,'Starting figure'],
    ['Amortisation and depreciation per the statements',v.amort,'Added back'],
    ['Capital cost allowance from Schedule 8',-v.cca,'Deducted'],
    ['Half of meals and entertainment of '+money(v.meals),mealsBack,
     'Added back'],
    ['Other amounts that are not deductible',v.addother,'Added back'],
    ['Other amounts deductible for tax only',-v.dedother,'Deducted']];
  var moved=v.amort+v.cca+v.meals+v.addother+v.dedother;
  if(v.acc===0&&moved===0){
    h='<h3>$0.00 of net income for income tax purposes</h3>';
    h+='<p>A nil year starts at $0.00 on the financial statements and has '
     +'nothing to reconcile, so line 300 of the return is $0.00 as well. '
     +'Where the accounting figure and the tax figure are the same, Schedule '
     +'1 carries that figure through unchanged.</p>';
  }else{
    h='<h3>'+amt(line300)+' of net income for income tax purposes</h3>';
    h+='<p>Starting from '+amt(v.acc)+' on the financial statements, the '
     +'reconciliation moves '+money(moved)+' in total across the items '
     +'below and ends at '+amt(line300)+', which is the figure that goes on '
     +'line 300 of the T2.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Item</th>'
   +'<th scope="col">Amount</th><th scope="col">Effect</th></tr></thead>'
   +'<tbody>';
  for(i=0;i!==ROWS.length;i++){
    h+='<tr><td>'+ROWS[i][0]+'</td><td>'+amt(ROWS[i][1])+'</td><td>'
     +ROWS[i][2]+'</td></tr>';
  }
  h+='<tr><td><strong>Net income for income tax purposes, line 300</strong>'
   +'</td><td><strong>'+amt(line300)+'</strong></td><td>Result</td></tr>';
  h+='</tbody></table>';
  h+='<p>The starting figure is line 9999 of Schedule 125 and the result is '
   +'line 300 of the return itself. The '
   +'<a href="SITEG125">Schedule 125 checker</a> covers what goes on the '
   +'income statement, and the '
   +'<a href="SITECCA">Schedule 8 CCA requirement checker</a> covers the '
   +'deduction on the third row.</p>';
  h+='<p>Nil T2 filing at '+PRICE_JS+' includes the GIFI schedules where '
   +'they are required. '+NOTNILJS+'</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITEG125', P_G125).replace('SITECCA', P_CCA)

T113 = dict(
 slug='schedule-1-net-income-reconciliation-calculator',
 title='Schedule 1 Net Income Reconciliation Calculator',
 h1_pre='Schedule 1 Net Income ', h1_span='Reconciliation Calculator',
 h1='Schedule 1 Net Income Reconciliation Calculator',
 eyebrow='Schedules',
 keyword='schedule 1 net income reconciliation',
 seo_title='Schedule 1 Net Income Reconciliation Calculator',
 seo_desc=('Schedule 1 runs from line 9999 of Schedule 125 to line 300 of '
           'the T2. Enter the accounting figure and the add-backs.'),
 meta=('The one arithmetic step between the accounting profit and the figure '
       'the corporate return actually taxes, item by item.'),
 tags=['Line 9999 to line 300', 'Amortisation added back',
       'Capital cost allowance deducted', 'Half of meals added back'],
 form=tool('The reconciliation',
           [num('acc', 'Net income or loss per the financial statements',
                'Enter a loss with a minus sign', -99999999, 99999999, '0'),
            num('amort', 'Amortisation and depreciation per the statements',
                'Added back, because tax uses capital cost allowance instead',
                0, 99999999, '0'),
            num('cca', 'Capital cost allowance claimed on Schedule 8',
                'Deducted in its place', 0, 99999999, '0'),
            num('meals', 'Meals and entertainment, total for the year',
                'Half of it is added back', 0, 99999999, '0'),
            num('addother', 'Other amounts that are not deductible',
                'Club dues, fines, non-deductible reserves',
                0, 99999999, '0'),
            num('dedother', 'Other amounts deductible for tax only',
                'Anything claimed on the return but not in the statements',
                0, 99999999, '0')],
           'Enter the accounting figure and leave the rest at zero on a nil '
           'year.'),
 js=None,
 sections=[
  ('from-9999-to-300', 'What Schedule 1 Sits Between',
   '<p>The financial statements and the tax return disagree, on purpose. The '
   'statements are prepared to an accounting standard and the return is '
   'prepared to the Income Tax Act, and the two treat several ordinary items '
   'differently. Schedule 1 is where that disagreement is written down and '
   'resolved.</p>\n'
   '<p>It starts at the net income or loss on line 9999 of Schedule 125, '
   'adds back what the statements deducted and the Act does not allow, '
   'deducts what the Act allows and the statements did not, and ends at net '
   'income for income tax purposes on line 300 of the T2. Everything the '
   'return then computes runs from line 300, not from the accounting '
   'figure.</p>\n'
   + _tbl(['Item', 'In the statements', 'On the return', 'Schedule 1'],
          [['Amortisation and depreciation', 'Deducted',
            'Not deductible', 'Added back'],
           ['Capital cost allowance', 'Not shown',
            'Deductible on Schedule 8', 'Deducted'],
           ['Meals and entertainment', 'Deducted in full',
            'Half of it allowed', 'Half added back'],
           ['Club dues and membership fees', 'Deducted',
            'Not deductible', 'Added back'],
           ['Fines and penalties', 'Deducted',
            'Generally not deductible', 'Added back'],
           ['Non-deductible reserves', 'Deducted',
            'Not deductible unless the Act allows it', 'Added back']])),
  ('amortisation-and-meals', 'The Two Items That Account for Most of It',
   '<p>Amortisation is the largest reconciling item on most returns and the '
   'easiest to describe. The statements write an asset down on whatever '
   'basis the accountant considers reasonable. The Act ignores that figure '
   'entirely and substitutes capital cost allowance, computed by class at a '
   'prescribed rate on Schedule 8. So the accounting figure comes out and '
   'the tax figure goes in, and the two are rarely the same.</p>\n'
   '<p>Meals and entertainment is the one most often missed. The statements '
   'carry the whole cost as an expense; the Act allows half of it. The other '
   'half is added back on Schedule 1 every year, which on a modest expense '
   'account is a small number that nonetheless has to be there.</p>\n'
   '<p>Where no asset is owned there is no amortisation and no capital cost '
   'allowance, and the '
   + a(P_CCA, 'Schedule 8 CCA requirement checker')
   + ' settles whether the schedule is needed at all. The '
   + a(P_G125, 'Schedule 125 checker')
   + ' and the '
   + a(P_G141, 'Schedule 141 checker')
   + ' cover the two statements this one reconciles, and the '
   + a(G_GIFI, 'guide to the GIFI schedules')
   + ' covers the set.</p>\n'
   '<p>' + CLOSE['schedule-1-net-income-reconciliation-calculator'] + '</p>'),
  ('on-a-nil-year', 'A Nil Year Has Nothing to Reconcile',
   '<p>On a year with no revenue and no expenses the accounting figure is '
   '$0.00, there is no amortisation to add back and no capital cost '
   'allowance to deduct, and line 300 is $0.00 as well. The reconciliation '
   'has nothing to do, which is the honest description of the schedule on a '
   'dormant corporation rather than a reason to leave it out of the '
   'thinking.</p>\n'
   '<p>A year with expenses and no revenue is different, and it is the one '
   'worth being careful about. The statements show a loss, the loss may or '
   'may not be deductible, and line 300 is then a negative figure that '
   'carries forward. The '
   + a(P_EXPONLY, 'expenses only year checker')
   + ' covers whether such a year is nil at all, and the '
   + a(P_REQSCH, 'required schedules checker')
   + ' lists what the return then carries.</p>\n'
   '<p>' + a(COST, 'Nil T2 filing at ' + PRICE)
   + ' includes the GIFI schedules where they are required, Schedule 50 and '
   'Schedule 24 on a first return. The '
   + a(G_SCHED, 'guide to T2 schedules on a nil return')
   + ' sets out the whole set, and the '
   + a(P_NILGIFI, 'nil GIFI balance sheet checker')
   + ' covers the balance sheet side.</p>'),
 ],
 faq=[
  ('What is Schedule 1 for?',
   'It reconciles the net income on the financial statements to net income '
   'for income tax purposes, which is line 300 of the T2.'),
  ('Where does the starting figure come from?',
   'Line 9999 of Schedule 125, the income statement information.'),
  ('Why is amortisation added back?',
   'Because the Act does not allow it. Capital cost allowance, computed by '
   'class on Schedule 8, is deducted in its place.'),
  ('How much of meals and entertainment is added back?',
   'Half. The statements carry the full cost and the Act allows fifty per '
   'cent of it.'),
  ('Are club dues deductible?',
   'No, so they are added back on Schedule 1 along with the other amounts '
   'the Act disallows.'),
  ('What does Schedule 1 look like on a nil year?',
   'It carries $0.00 through. There is no accounting income and nothing to '
   'reconcile, so line 300 is $0.00.'),
  ('Can line 300 be negative?',
   'Yes. A year with expenses and no revenue produces a loss for tax '
   'purposes, which carries forward rather than disappearing.'),
  ('Is Schedule 1 the same as Schedule 125?',
   'No. Schedule 125 is the income statement itself. Schedule 1 is the '
   'reconciliation that starts where Schedule 125 ends.'),
  ('Does the nil T2 fee include it?',
   'Yes, along with the GIFI schedules where they are required, Schedule 50 '
   'and Schedule 24 on a first return.'),
  ('What if the accounting and tax figures are the same?',
   'Then the schedule carries the figure through unchanged, which is the '
   'ordinary case on a corporation with nothing to reconcile.'),
 ],
 related=[
  (P_G125, 'Schedule 125 checker'),
  (P_G141, 'Schedule 141 checker'),
  (P_CCA, 'Schedule 8 CCA requirement checker'),
  (P_NILGIFI, 'Nil GIFI balance sheet checker'),
  (P_REQSCH, 'Required schedules checker'),
  (P_EXPONLY, 'Expenses only year checker'),
 ],
)

# ====================================== 114. GST/HST reporting period
T114_JS = RBASE + MONEY_JS + r"""
var B1=150000000,B2=600000000;
var out=document.getElementById('out');
function freqTable(mark){
  var ROWS=[
   ['$1,500,000 or less','Annual','Monthly or quarterly',
    'Three months after the fiscal year end'],
   ['More than $1,500,000 up to $6,000,000','Quarterly','Monthly',
    'One month after the quarter ends'],
   ['More than $6,000,000','Monthly','None available',
    'One month after the month ends']];
  var h='<table class="ei-tbl"><thead><tr>'
   +'<th scope="col">Annual taxable supplies</th>'
   +'<th scope="col">Assigned period</th>'
   +'<th scope="col">May elect</th>'
   +'<th scope="col">Return due</th>'
   +'<th scope="col">Yours</th></tr></thead><tbody>';
  for(var i=0;i!==ROWS.length;i++){
    h+='<tr><td>'+ROWS[i][0]+'</td><td>'+ROWS[i][1]+'</td><td>'+ROWS[i][2]
     +'</td><td>'+ROWS[i][3]+'</td><td>'+(i===mark?'Yes':'')+'</td></tr>';
  }
  h+='</tbody></table>';
  return h;
}
function show(){
  var raw=document.getElementById('supplies').value.trim(),
      dorm=pick('dormant'),wait=0;
  if(raw===''){wait++;}
  if(dorm===null){wait++;}
  if(wait > 0){
    out.innerHTML='<p>'+wait+' of the two answers '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var dollars=parseFloat(raw.replace(/,/g,''));
  if(isNaN(dollars)||0 > dollars){
    out.innerHTML='<p>Enter the annual taxable supplies as a dollar '
     +'amount.</p>';return;
  }
  var c=Math.round(dollars*100),band,period,may,due,h;
  if(c > B2){band=2;period='monthly';may='none';
    due='one month after the end of each month';}
  else if(c > B1){band=1;period='quarterly';may='monthly only';
    due='one month after the end of each quarter';}
  else{band=0;period='annual';may='monthly or quarterly';
    due='three months after the fiscal year end';}
  h='<h3>The assigned reporting period is '+period+'</h3>';
  h+='<p>Taxable supplies of '+money(c)+' for the year put the registrant in '
   +'the '+period+' band, so the return and any payment are due '+due+'. '
   +'The elections available from there are '+may+'.</p>';
  h+=freqTable(band);
  if(band===0){
    h+='<p>An annual filer whose net tax for the year reaches $3,000.00 also '
     +'has to pay quarterly instalments through the year, with the return '
     +'reconciling them afterwards. A registrant with nothing to remit does '
     +'not reach that figure.</p>';
  }else{
    h+='<p>A shorter period than the assigned one can be elected, never a '
     +'longer one. A registrant in this band cannot move to annual filing '
     +'while the supplies stay where they are.</p>';
  }
  if(dorm==='y'){
    h+='<p>A dormant registrant still files for every period in the '
     +'assigned frequency, and files it at nil. The '
     +'<a href="SITEGSTNIL">GST/HST nil filing checker</a> covers whether '
     +'the return is owed, the '
     +'<a href="SITEGSTDUE">GST/HST nil return deadline calculator</a> '
     +'dates it, and the '
     +'<a href="SITEGSTCLOSE">GST/HST account closure checker</a> covers '
     +'closing the account so the periods stop arriving at all.</p>';
  }else{
    h+='<p>Whether an account has to exist in the first place is a separate '
     +'question from which period applies to one that does. The '
     +'<a href="SITEGSTREG">GST/HST registration requirement checker</a> '
     +'answers it, on the $30,000.00 small supplier test.</p>';
  }
  h+='<p>This is the sales tax account and not the corporate income tax '
   +'return. Nil T2 filing at '+PRICE_JS+' covers the T2 and not a GST/HST '
   +'return. '+NOTNILJS+'</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITEGSTNIL', P_GSTNIL).replace('SITEGSTDUE', P_GSTDUE) \
   .replace('SITEGSTCLOSE', P_GSTCLOSE).replace('SITEGSTREG', P_GSTREG)

T114 = dict(
 slug='gst-hst-filing-frequency-calculator',
 title='GST/HST Filing Frequency Calculator | Reporting Periods',
 h1_pre='GST/HST Filing ', h1_span='Frequency Calculator',
 h1='GST/HST Filing Frequency Calculator',
 eyebrow='GST/HST',
 keyword='gst hst filing frequency',
 seo_title='GST/HST Filing Frequency Calculator',
 seo_desc=('Annual taxable supplies set the reporting period. Enter the '
           'figure for the assigned frequency and the filing deadline.'),
 meta=('Two thresholds decide whether a registrant files annually, '
       'quarterly or monthly, and the deadline moves with the answer.'),
 tags=['$1,500,000 and $6,000,000', 'Annual, quarterly or monthly',
       'One month or three', 'Elections shorten only'],
 form=tool('The registrant',
           [num('supplies', 'Annual taxable supplies, in dollars',
                'Worldwide, including the supplies of associated persons',
                0, 999999999, '0'),
            yn('dormant', 'Is the corporation dormant, with nil returns '
                          'expected?')],
           'Enter the taxable supplies and answer the question above.'),
 js=None,
 sections=[
  ('the-two-thresholds', 'Two Figures Decide It, and Nothing Else Does',
   '<p>A registrant does not choose a reporting period from a standing '
   'start. The period is assigned by annual taxable supplies, and there are '
   'only two numbers in the test. At $1,500,000 or less the assigned period '
   'is annual. Above that and up to $6,000,000 it is quarterly. Above '
   '$6,000,000 it is monthly.</p>\n'
   '<p>From the assigned period a registrant may elect a shorter one, never '
   'a longer one. An annual filer can elect quarterly or monthly, a '
   'quarterly filer can elect monthly, and a monthly filer has nothing '
   'shorter to move to. The supplies figure is worldwide and includes the '
   'supplies of associated persons, which is the part that catches a group '
   'of small corporations under common control.</p>\n'
   + _tbl(['Annual taxable supplies', 'Assigned period', 'May elect',
           'Return due'],
          [['$1,500,000 or less', 'Annual', 'Monthly or quarterly',
            'Three months after the fiscal year end'],
           ['More than $1,500,000 up to $6,000,000', 'Quarterly',
            'Monthly', 'One month after the quarter ends'],
           ['More than $6,000,000', 'Monthly', 'None available',
            'One month after the month ends']])),
  ('why-the-deadline-moves', 'The Annual Filer Gets Three Months, the Others One',
   '<p>The deadline is not a fixed number of days from the period end. A '
   'monthly or quarterly filer has one month after the period closes to file '
   'and to pay. An annual filer has three months after the fiscal year end '
   'for both. That is a real difference and it is the reason the period '
   'matters to a quiet corporation at all.</p>\n'
   '<p>There is one condition attached to annual filing. Where net tax for '
   'the year reaches $3,000.00, the annual filer also pays quarterly '
   'instalments through the year and the return reconciles them at the end. '
   'A registrant with nothing to remit never reaches that figure, so a '
   'dormant corporation on annual filing has one nil return a year and '
   'nothing in between.</p>\n'
   '<p>' + CLOSE['gst-hst-filing-frequency-calculator'] + '</p>'),
  ('on-a-dormant-corporation', 'A Nil Return Is Still a Return, Once Per Period',
   '<p>Nothing about being dormant changes the assigned frequency. A monthly '
   'filer that stopped trading still has twelve returns a year to file, each '
   'of them at nil, until either the frequency is changed or the account is '
   'closed. That is the single strongest argument for electing or reverting '
   'to annual filing before a corporation goes quiet.</p>\n'
   '<p>The '
   + a(P_GSTNIL, 'GST/HST nil filing checker')
   + ' settles whether the return is owed, the '
   + a(P_GSTDUE, 'GST/HST nil return deadline calculator')
   + ' dates it once the period is known, and the '
   + a(P_GSTCLOSE, 'GST/HST account closure checker')
   + ' covers closing the account so the periods stop arriving. Where the '
   'question is whether an account has to exist at all, the '
   + a(P_GSTREG, 'GST/HST registration requirement checker')
   + ' runs the $30,000.00 small supplier test.</p>\n'
   '<p>This is the sales tax account, which is not the corporate income tax '
   'return. ' + a(COST, 'Nil T2 filing at ' + PRICE)
   + ' covers the T2 for one tax year and no GST/HST filing is part of it. '
   'The '
   + a(G_PAY, 'guide to CRA accounts on a dormant corporation')
   + ' covers every account a quiet corporation still carries, and the '
   + a(P_SEQ, 'CRA account closure sequencer')
   + ' sets out the order they come off in.</p>'),
 ],
 faq=[
  ('How is the GST/HST reporting period decided?',
   'By annual taxable supplies. At $1,500,000 or less the assigned period is '
   'annual, above that to $6,000,000 it is quarterly, and above $6,000,000 '
   'it is monthly.'),
  ('Can a registrant choose a different period?',
   'A shorter one, yes. An annual filer may elect quarterly or monthly and a '
   'quarterly filer may elect monthly. A longer period than the assigned one '
   'is not available.'),
  ('When is a quarterly return due?',
   'One month after the quarter ends, for both the return and the payment.'),
  ('When is an annual return due?',
   'Three months after the fiscal year end for a corporation, for both the '
   'return and the payment.'),
  ('Do associated corporations count in the supplies figure?',
   'Yes. The test is worldwide taxable supplies including those of '
   'associated persons, which is what catches a group of small '
   'corporations.'),
  ('Does a dormant registrant still file?',
   'Yes, once per period in the assigned frequency, at nil, until the '
   'frequency changes or the account is closed.'),
  ('What are the instalments an annual filer pays?',
   'Where net tax for the year reaches $3,000.00 the annual filer pays '
   'quarterly instalments and the return reconciles them. A registrant with '
   'nothing to remit does not reach that figure.'),
  ('Is a monthly filer that stopped trading stuck with twelve returns?',
   'Until the frequency is changed or the account is closed, yes. That is '
   'the usual reason to deal with the frequency before a corporation goes '
   'quiet.'),
  ('Is the GST/HST return part of the nil T2 fee?',
   'No. The fee covers the federal corporate income tax return. The sales '
   'tax account is a separate filing to a separate programme.'),
  ('Does the fiscal year end matter?',
   'For an annual filer it sets the deadline, because the three months run '
   'from it. For monthly and quarterly filers the period end does.'),
 ],
 related=[
  (P_GSTREG, 'GST/HST registration requirement checker'),
  (P_GSTNIL, 'GST/HST nil filing checker'),
  (P_GSTDUE, 'GST/HST nil return deadline calculator'),
  (P_GSTCLOSE, 'GST/HST account closure checker'),
  (P_SEQ, 'CRA account closure sequencer'),
  (P_STAND, 'CRA account standing checker'),
 ],
)

# ====================================== 115. payroll remittance due date
T115_JS = RBASE + MONEY_JS + r"""
var A1=2500000,A2=10000000,QTR=300000;
var out=document.getElementById('out');
function thirdWorking(dt){
  var d=new Date(dt.getTime()),n=3;
  while(n > 0){d=nextBusiness(dayAfter(d));n--;}
  return d;
}
function typeTable(mark){
  var ROWS=[
   ['Quarterly','Under $3,000.00 with a perfect compliance record',
    'Once a quarter','The 15th of the month after the quarter ends'],
   ['Regular','Under $25,000.00','Once a month',
    'The 15th of the month after the month of payment'],
   ['Accelerated, threshold 1','$25,000.00 to $99,999.99','Twice a month',
    'The 25th for the 1st to the 15th, the 10th of next month for the rest'],
   ['Accelerated, threshold 2','$100,000.00 or more','Four times a month',
    'The third working day after the 7th, 14th, 21st and last day']];
  var h='<table class="ei-tbl"><thead><tr>'
   +'<th scope="col">Remitter type</th>'
   +'<th scope="col">Average monthly withholding amount</th>'
   +'<th scope="col">How often</th>'
   +'<th scope="col">Due</th>'
   +'<th scope="col">Yours</th></tr></thead><tbody>';
  for(var i=0;i!==ROWS.length;i++){
    h+='<tr><td>'+ROWS[i][0]+'</td><td>'+ROWS[i][1]+'</td><td>'+ROWS[i][2]
     +'</td><td>'+ROWS[i][3]+'</td><td>'+(i===mark?'Yes':'')+'</td></tr>';
  }
  h+='</tbody></table>';
  return h;
}
function show(){
  var raw=document.getElementById('amwa').value.trim(),
      pay=parse('pay'),wait=0;
  if(raw===''){wait++;}
  if(pay===null){wait++;}
  if(wait > 0){
    out.innerHTML='<p>'+wait+' of the two figures '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  if(pay===undefined){
    out.innerHTML='<p>That pay date could not be read.</p>';return;
  }
  var dollars=parseFloat(raw.replace(/,/g,''));
  if(isNaN(dollars)||0 > dollars){
    out.innerHTML='<p>Enter the average monthly withholding amount as a '
     +'dollar figure.</p>';return;
  }
  var c=Math.round(dollars*100),y=pay.getUTCFullYear(),m=pay.getUTCMonth(),
      d=pay.getUTCDate(),row,label,due,window,h;
  if(!(A2 > c)){
    row=3;label='accelerated remitter, threshold 2';
    if(!(d > 7)){window='the 1st to the 7th';due=thirdWorking(u(y,m,7));}
    else if(!(d > 14)){window='the 8th to the 14th';
      due=thirdWorking(u(y,m,14));}
    else if(!(d > 21)){window='the 15th to the 21st';
      due=thirdWorking(u(y,m,21));}
    else{window='the 22nd to the end of the month';
      due=thirdWorking(u(y,m,lastDay(y,m)));}
  }else if(!(A1 > c)){
    row=2;label='accelerated remitter, threshold 1';
    if(!(d > 15)){window='the 1st to the 15th';
      due=nextBusiness(u(y,m,25));}
    else{window='the 16th to the end of the month';
      due=nextBusiness(u(y,m+1,10));}
  }else{
    row=1;label='regular remitter';
    window='the whole month';
    due=nextBusiness(u(y,m+1,15));
  }
  h='<h3>Remit by '+fmt(due)+'</h3>';
  h+='<p>An average monthly withholding amount of '+money(c)+' makes the '
   +'corporation '+(row===1?'a ':'an ')+label+'. A payment made on '
   +fmt(pay)+' falls in '+window+', and the remittance for that window is '
   +'due '+fmt(due)+'.</p>';
  h+=typeTable(row);
  if(QTR > c){
    h+='<p>Below $3,000.00 a quarterly schedule is also available, but it is '
     +'not automatic: the Canada Revenue Agency assigns it, and only to an '
     +'employer with a perfect compliance record over the preceding twelve '
     +'months. Until it is assigned, the monthly date above is the one that '
     +'applies.</p>';
  }
  h+='<p>Where a due date falls on a Saturday, a Sunday or a public holiday, '
   +'the remittance is on time if it reaches the Agency on the next business '
   +'day, and the date above already carries that shift.</p>';
  h+='<p>The withholding figure is the one from two calendar years ago, not '
   +'from the current year, so a payroll that has shrunk can still be on an '
   +'accelerated schedule. Where nothing is being paid at all, the '
   +'<a href="SITEPAYNIL">payroll nil remittance checker</a> covers '
   +'reporting the period at nil and the '
   +'<a href="SITEPAYCLOSE">payroll account closure checker</a> covers '
   +'closing the account.</p>';
  h+='<p>Payroll is a separate programme account from the corporate income '
   +'tax return. Nil T2 filing at '+PRICE_JS+' covers the T2 and no payroll '
   +'filing is part of it. '+NOTNILJS+'</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITEPAYNIL', P_PAYNIL).replace('SITEPAYCLOSE', P_PAYCLOSE)

T115 = dict(
 slug='payroll-remittance-due-date-calculator',
 title='Payroll Remittance Due Date Calculator | Remitter Types',
 h1_pre='Payroll Remittance ', h1_span='Due Date Calculator',
 h1='Payroll Remittance Due Date Calculator',
 eyebrow='Payroll',
 keyword='payroll remittance due date',
 seo_title='Payroll Remittance Due Date Calculator',
 seo_desc=('The remitter type sets the date, and a figure from two years ago '
           'sets the type. Enter it with the pay date for the deadline.'),
 meta=('Four remitter types, two thresholds between them, and a withholding '
       'figure from two calendar years ago that decides which one applies.'),
 tags=['Four remitter types', '$25,000 and $100,000',
       'Two calendar years back', 'Weekend and holiday shift'],
 form=tool('The payroll',
           [num('amwa', 'Average monthly withholding amount, in dollars',
                'From two calendar years ago, not the current year',
                0, 9999999, '0'),
            date('pay', 'Date the employees were paid')],
           'Enter the withholding figure and the pay date.'),
 js=None,
 sections=[
  ('four-types', 'Four Remitter Types, and Two Thresholds Between Them',
   '<p>There is no single payroll remittance deadline. There are four '
   'schedules, and which one a corporation is on depends on its average '
   'monthly withholding amount: the total of its remittances for a calendar '
   'year divided by the number of months it remitted. Two thresholds split '
   'the four, at $25,000.00 and at $100,000.00.</p>\n'
   '<p>The regular remitter has the deadline most people know, the 15th of '
   'the month after the month of payment. Above $25,000.00 the schedule '
   'becomes twice monthly and above $100,000.00 four times monthly, and at '
   'that point the dates stop being calendar dates and become working-day '
   'counts.</p>\n'
   + _tbl(['Remitter type', 'Average monthly withholding amount',
           'How often', 'Due'],
          [['Quarterly',
            'Under $3,000.00 with a perfect compliance record',
            'Once a quarter',
            'The 15th of the month after the quarter ends'],
           ['Regular', 'Under $25,000.00', 'Once a month',
            'The 15th of the month after the month of payment'],
           ['Accelerated, threshold 1', '$25,000.00 to $99,999.99',
            'Twice a month',
            'The 25th for the 1st to the 15th, the 10th of the next month '
            'for the 16th to the end'],
           ['Accelerated, threshold 2', '$100,000.00 or more',
            'Four times a month',
            'The third working day after the 7th, the 14th, the 21st and '
            'the last day of the month']])),
  ('two-years-back', 'The Figure That Sets the Type Is Two Years Old',
   '<p>This is the part that catches people, and it catches them in exactly '
   'one direction. The average monthly withholding amount used for the '
   'current year is the one from two calendar years ago. A corporation that '
   'has wound its payroll down to nothing can therefore still be an '
   'accelerated remitter, on a twice-monthly or four-times-monthly schedule, '
   'because the test looks at a year when the payroll was running.</p>\n'
   '<p>It cuts the other way too. A payroll that has grown sharply is not '
   'moved onto a faster schedule until the two-year lag catches up. Neither '
   'direction is something the employer chooses; the Agency sets the type '
   'and notifies it, and the quarterly schedule in the first row is assigned '
   'rather than elected.</p>\n'
   '<p>Where a due date falls on a Saturday, a Sunday or a public holiday, '
   'the remittance is on time if it reaches the Agency on the next business '
   'day. The '
   + a(P_STAND, 'CRA account standing checker')
   + ' covers what the Agency currently shows for each account, and the '
   + a(G_PAY, 'guide to CRA accounts on a dormant corporation')
   + ' covers the set of them.</p>\n'
   '<p>' + CLOSE['payroll-remittance-due-date-calculator'] + '</p>'),
  ('nothing-paid', 'When Nothing Was Paid, There Is Still a Period to Report',
   '<p>An open payroll account does not go quiet because the payroll did. '
   'The account keeps its periods, and where no remuneration was paid in a '
   'period the sensible course is to report that period at nil rather than '
   'to send nothing, because sending nothing is what produces a '
   'non-filing notice and an estimate. The '
   + a(P_PAYNIL, 'payroll nil remittance checker')
   + ' covers that, and the '
   + a(P_T4REQ, 'T4 nil filing requirement checker')
   + ' covers whether the annual slip return is owed as well.</p>\n'
   '<p>Where the payroll has stopped for good, closing the account is what '
   'ends the periods. The '
   + a(P_PAYCLOSE, 'payroll account closure checker')
   + ' sets out what has to be done first and the '
   + a(P_SEQ, 'CRA account closure sequencer')
   + ' sets out the order the accounts come off in, which matters because '
   'closing them in the wrong order leaves filings owed on an account that '
   'no longer accepts them.</p>\n'
   '<p>Payroll is a separate programme account from corporate income tax. '
   + a(COST, 'Nil T2 filing at ' + PRICE)
   + ' covers the federal corporate income tax return for one tax year, and '
   'no payroll remittance or slip return is part of that fee. Where a slip '
   'return has gone in late, the '
   + a(P_T4PEN, 'T4 late filing penalty calculator')
   + ' computes the charge.</p>'),
 ],
 faq=[
  ('When is a payroll remittance due?',
   'For a regular remitter, the 15th of the month after the month the '
   'employees were paid. The accelerated schedules are more frequent than '
   'that.'),
  ('What is the average monthly withholding amount?',
   'The total of the remittances for a calendar year divided by the number '
   'of months the corporation remitted in it.'),
  ('Which year does that figure come from?',
   'Two calendar years before the current one, which is why a shrinking '
   'payroll can still be on an accelerated schedule.'),
  ('What are the two thresholds?',
   '$25,000.00 and $100,000.00. Below the first is a regular remitter, '
   'between them is threshold 1, and at or above the second is threshold 2.'),
  ('When does a threshold 1 remitter pay?',
   'Twice a month: the 25th for pay dates in the 1st to the 15th, and the '
   '10th of the following month for the rest.'),
  ('When does a threshold 2 remitter pay?',
   'Four times a month, on the third working day after the 7th, the 14th, '
   'the 21st and the last day of the month.'),
  ('Can a small employer remit quarterly?',
   'Where the figure is under $3,000.00 and the compliance record over the '
   'preceding twelve months is perfect, the Agency can assign a quarterly '
   'schedule. It is assigned rather than elected.'),
  ('What if the due date is a weekend or a holiday?',
   'The remittance is on time if it reaches the Agency on the next business '
   'day.'),
  ('What if no wages were paid in the period?',
   'The period is still part of the account. Reporting it at nil is what '
   'keeps a non-filing notice and an estimate from following.'),
  ('Is payroll part of the nil T2 fee?',
   'No. The fee covers the corporate income tax return. Payroll is a '
   'separate programme account with its own filings.'),
 ],
 related=[
  (P_PAYNIL, 'Payroll nil remittance checker'),
  (P_PAYCLOSE, 'Payroll account closure checker'),
  (P_T4REQ, 'T4 nil filing requirement checker'),
  (P_T4PEN, 'T4 late filing penalty calculator'),
  (P_SEQ, 'CRA account closure sequencer'),
  (P_STAND, 'CRA account standing checker'),
 ],
)

# ====================================== 116. shareholder loan, 15(2) amount
T116_JS = RBASE + MONEY_JS + r"""
var out=document.getElementById('out');
function rowTbl(rows){
  var h='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Answer</th></tr></thead><tbody>';
  for(var i=0;i!==rows.length;i++){
    h+='<tr><td>'+rows[i][0]+'</td><td>'+rows[i][1]+'</td></tr>';
  }
  h+='</tbody></table>';
  return h;
}
function show(){
  var ye=parse('ye'),raw=document.getElementById('amt').value.trim(),
      rep=pick('rep'),exc=pick('exc'),wait=0;
  if(ye===null){wait++;}
  if(raw===''){wait++;}
  if(rep===null){wait++;}
  if(exc===null){wait++;}
  if(wait > 0){
    out.innerHTML='<p>'+wait+' of the four answers '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  if(ye===undefined){
    out.innerHTML='<p>That year end could not be read.</p>';return;
  }
  var dollars=parseFloat(raw.replace(/,/g,''));
  if(isNaN(dollars)||0 > dollars){
    out.innerHTML='<p>Enter the loan amount as a dollar figure.</p>';return;
  }
  var c=Math.round(dollars*100),deadline=addYear(ye,1),h;
  if(exc==='y'){
    h='<h3>Nothing is included under subsection 15(2)</h3>';
    h+='<p>Where an exception applies, the amount is outside subsection 15(2) '
     +'whatever happens to the repayment date. The two that come up are '
     +'subsection 15(2.3), for a loan made in the ordinary course of a '
     +'lending business, and subsection 15(2.4), for certain loans to an '
     +'employee with bona fide repayment arrangements made at the time. Both '
     +'depend on facts worth confirming with the agreement in front of '
     +'you.</p>';
    h+=rowTbl([['Amount of the loan',money(c)],
      ['Repayment deadline under 15(2.6)',fmt(deadline)],
      ['Included in anyone&rsquo;s income under 15(2)','No, an exception applies'],
      ['Interest benefit under 80.4(2)','Still possible while it is outstanding'],
      ['The corporation&rsquo;s own tax year','Can still be nil']]);
  }else if(rep==='y'){
    h='<h3>Nothing is included, because it was repaid in time</h3>';
    h+='<p>Subsection 15(2.6) takes the loan out of subsection 15(2) where it '
     +'is repaid within one year after the end of the corporation&rsquo;s '
     +'taxation year in which it was made, so the deadline here is '
     +fmt(deadline)+'. The one condition is that the repayment is not part of '
     +'a series of loans and repayments: paying it off and drawing it again '
     +'does not satisfy the subsection.</p>';
    h+=rowTbl([['Amount of the loan',money(c)],
      ['Repayment deadline under 15(2.6)',fmt(deadline)],
      ['Included in anyone&rsquo;s income under 15(2)','No, repaid in time'],
      ['Interest benefit under 80.4(2)',
       'Still arises for the period it was outstanding'],
      ['The corporation&rsquo;s own tax year','Can still be nil']]);
  }else{
    h='<h3>'+money(c)+' is included in the shareholder&rsquo;s income</h3>';
    h+='<p>The deadline under subsection 15(2.6) was '+fmt(deadline)+', one '
     +'year after the end of the corporation&rsquo;s taxation year in which '
     +'the loan was made. With the amount still outstanding past it, the '
     +'whole '+money(c)+' is included in income under subsection 15(2) and '
     +'the taxpayer it is included for is the shareholder, not the '
     +'corporation.</p>';
    h+=rowTbl([['Amount included',money(c)],
      ['Repayment deadline under 15(2.6)',fmt(deadline)],
      ['Whose income it is included in','The shareholder&rsquo;s'],
      ['Which tax year',
       'The shareholder&rsquo;s year in which the loan was received'],
      ['What reverses it',
       'A deduction under paragraph 20(1)(j) in the year it is repaid'],
      ['The corporation&rsquo;s own tax year','Can still be nil']]);
    h+='<p>The year it lands in is the year the loan was received rather than '
     +'the year the deadline passed, which usually means a personal return '
     +'already filed and assessed. Repaying the amount later does not undo '
     +'the inclusion; it produces a deduction under paragraph 20(1)(j) in the '
     +'year of repayment instead.</p>';
  }
  h+='<p>A separate benefit can arise under subsection 80.4(2) on a loan '
   +'carrying no interest or interest below the prescribed rate, for the '
   +'period it is outstanding. The prescribed rate is set quarterly, so that '
   +'figure is not computed here.</p>';
  h+='<p>None of this changes whether the corporation&rsquo;s own year was '
   +'nil. A corporation that earned nothing and claimed nothing still files a '
   +'nil return for the year, at '+PRICE_JS+'. The '
   +'<a href="SITESHDUE">shareholder loan repayment deadline calculator</a> '
   +'dates the deadline on its own and the '
   +'<a href="SITESHBAL">shareholder loan balance checker</a> covers the '
   +'balance itself. '+NOTNILJS+'</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITESHDUE', P_SHDUE).replace('SITESHBAL', P_SHBAL)

T116 = dict(
 slug='shareholder-loan-income-inclusion-calculator',
 title='Shareholder Loan Income Inclusion Calculator | 15(2)',
 h1_pre='Shareholder Loan ', h1_span='Income Inclusion Calculator',
 h1='Shareholder Loan Income Inclusion Calculator',
 eyebrow='Shareholders',
 keyword='shareholder loan income inclusion',
 seo_title='Shareholder Loan Income Inclusion Calculator',
 seo_desc=('Subsection 15(2) includes the loan in the shareholder income, '
           'not the corporation. Enter the year end and the amount.'),
 meta=('Miss the one-year deadline and the whole loan is income, in the '
       'shareholder hands and in the year the money was taken.'),
 tags=['One year after the year end', 'The shareholder&rsquo;s income',
       'A 20(1)(j) deduction on repayment', 'The corporate year can be nil'],
 form=tool('The loan',
           [date('ye', 'The corporation&rsquo;s year end in the year the '
                       'loan was made'),
            num('amt', 'Amount of the loan or indebtedness, in dollars',
                'The principal still outstanding', 0, 99999999, '0'),
            yn('rep', 'Was it repaid in full within one year after that '
                      'year end?'),
            yn('exc', 'Does an exception apply: an ordinary lending '
                      'business, or an employee loan with bona fide '
                      'repayment arrangements?')],
           'Enter the year end and the amount, and answer both questions.'),
 js=None,
 sections=[
  ('the-deadline', 'The Window Hangs Off the Year End, Which Is Why It Varies',
   '<p>Subsection 15(2) includes the amount of a loan from a corporation to '
   'a shareholder in income. Subsection 15(2.6) takes it back out where the '
   'loan is repaid within one year after the end of the corporation&rsquo;s '
   'taxation year in which the loan was made. The deadline therefore hangs '
   'off the year end rather than off the date of the loan, which is what '
   'makes the available time vary so widely.</p>\n'
   '<p>A loan taken the day after a December 31 year end has almost two '
   'years to run. A loan taken on December 30 has one year and a day. Same '
   'provision, same corporation, and the second one is the shape that goes '
   'wrong.</p>\n'
   + _tbl(['Corporation&rsquo;s year end', 'Loan made',
           'Repay by', 'Time available'],
          [['December 31, 2025', 'January 2, 2026', 'December 31, 2026',
            'Almost two years'],
           ['December 31, 2025', 'December 30, 2026', 'December 31, 2026',
            'One day'],
           ['June 30, 2026', 'July 1, 2026', 'June 30, 2027',
            'Almost two years'],
           ['June 30, 2026', 'June 29, 2026', 'June 30, 2027',
            'One year and a day'],
           ['February 28, 2026', 'March 1, 2026', 'February 28, 2027',
            'Almost two years']])
   + '\n<p>The '
   + a(P_SHDUE, 'shareholder loan repayment deadline calculator')
   + ' computes that date on its own, and the '
   + a(P_SHBAL, 'shareholder loan balance checker')
   + ' and the '
   + a(P_SHDIR, 'due to versus due from shareholder checker')
   + ' cover the balance and which side of the balance sheet it sits on.</p>'),
  ('whose-income', 'The Amount Lands on a Personal Return, in an Earlier Year',
   '<p>Two things about the inclusion are easy to get backwards, and getting '
   'either backwards changes the advice entirely.</p>\n'
   '<p>The first is whose income it is. The amount is included in the '
   '<strong>shareholder&rsquo;s</strong> income under subsection 15(2). It is '
   'not corporate income and it does not appear on the T2. A corporation '
   'that earned nothing, claimed nothing and lent its shareholder money that '
   'was never repaid still has a nil tax year, and the problem sits entirely '
   'on the personal side.</p>\n'
   '<p>The second is which year. The inclusion is for the year the loan was '
   'received, not the year the deadline passed. That is very often a '
   'personal return filed and assessed long ago, which is why the practical '
   'consequence is a reassessment of an earlier year rather than a line on '
   'the next one. A later repayment does not undo it: paragraph 20(1)(j) '
   'gives a deduction in the year of repayment, which only helps if there is '
   'income in that year to apply it against.</p>\n'
   '<p>' + CLOSE['shareholder-loan-income-inclusion-calculator'] + '</p>'),
  ('what-is-left-out', 'The Exceptions, and the Benefit That Survives Them',
   '<p>Three routes keep an amount out of subsection 15(2). Repayment inside '
   'the 15(2.6) window is the common one, provided the repayment is not part '
   'of a series of loans and repayments, because paying a balance down at a '
   'year end and drawing it again afterwards does not satisfy the '
   'subsection. Subsection 15(2.3) covers a loan made in the ordinary course '
   'of a lending business. Subsection 15(2.4) covers certain loans to an '
   'employee, including one to acquire a dwelling or shares of the employer, '
   'where bona fide repayment arrangements were made when the loan was '
   'granted.</p>\n'
   '<p>A separate charge survives all three. Where a loan carries no '
   'interest, or interest below the prescribed rate, subsection 80.4(2) '
   'brings an interest benefit into income for the period the loan is '
   'outstanding. The prescribed rate is set quarterly, so the amount is not '
   'computed on this page; the point is that repaying inside the deadline '
   'answers subsection 15(2) and does not answer subsection 80.4(2).</p>\n'
   '<p>On the corporate side the balance is a reportable transaction with a '
   'shareholder, which the '
   + a(P_SCH11, 'Schedule 11 shareholder transactions checker')
   + ' covers, and the shareholder may need naming on Schedule 50, which '
   'the '
   + a(P_SCH50, 'Schedule 50 shareholder threshold checker')
   + ' settles. ' + a(COST, 'Nil T2 filing at ' + PRICE)
   + ' covers the corporate return for the year including those schedules '
   'where they are required, and the '
   + a(G_SHARE, 'guide to Schedule 50 and shareholder reporting')
   + ' covers the disclosure side.</p>'),
 ],
 faq=[
  ('How much of a shareholder loan is included in income?',
   'The whole amount of the loan or indebtedness, where no exception applies '
   'and it is not repaid within the subsection 15(2.6) window.'),
  ('Whose income is it included in?',
   'The shareholder&rsquo;s. It is not corporate income and it does not '
   'appear on the T2.'),
  ('Which tax year does it land in?',
   'The year the loan was received, not the year the repayment deadline '
   'passed. That often means an earlier personal return being reassessed.'),
  ('What is the repayment deadline?',
   'One year after the end of the corporation&rsquo;s taxation year in which '
   'the loan was made.'),
  ('Does repaying it later fix the inclusion?',
   'It does not reverse the inclusion. Paragraph 20(1)(j) gives a deduction '
   'in the year of repayment instead.'),
  ('Can the corporation still file a nil return?',
   'Yes. A corporation that earned nothing and claimed nothing has a nil tax '
   'year whatever happened to the loan on the shareholder&rsquo;s side.'),
  ('What if the loan is repaid and drawn again?',
   'A repayment that is part of a series of loans and repayments does not '
   'satisfy subsection 15(2.6), so the amount stays within subsection 15(2).'),
  ('Are there exceptions to the inclusion?',
   'Yes. Subsection 15(2.3) for a loan made in the ordinary course of a '
   'lending business, and subsection 15(2.4) for certain employee loans with '
   'bona fide repayment arrangements.'),
  ('Is there interest on top of the inclusion?',
   'A separate benefit can arise under subsection 80.4(2) where the loan '
   'carries no interest or interest below the prescribed rate. The rate is '
   'set quarterly and is not computed here.'),
  ('Does the loan have to be reported on the T2?',
   'The balance is a transaction with a shareholder and is reportable on the '
   'corporate return, which is a different thing from being corporate '
   'income.'),
 ],
 related=[
  (P_SHDUE, 'Shareholder loan repayment deadline calculator'),
  (P_SHBAL, 'Shareholder loan balance checker'),
  (P_SHDIR, 'Due to versus due from shareholder checker'),
  (P_SCH11, 'Schedule 11 shareholder transactions checker'),
  (P_SCH50, 'Schedule 50 shareholder threshold checker'),
  (P_REQD, 'T2 filing requirement checker'),
 ],
)


TOOLS18 = [T112, T113, T114, T115, T116]
_JS18 = [T112_JS, T113_JS, T114_JS, T115_JS, T116_JS]

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


OVERFLOW_WAS = '$350.00 plus HST per year'
OVERFLOW_NOW = '$350.00 plus applicable sales tax per year'

for _t, _js in zip(TOOLS18, _JS18):
    assert OVERFLOW_WAS in _js, (
        '%s: the overflow price moved; re-check the shadow' % _t['slug'])
    _t['js'] = (_js + wire(_t['form'])).replace(OVERFLOW_WAS, OVERFLOW_NOW)

# ---- the contract ------------------------------------------------------
_LIVE = {f[:-5] for f in os.listdir(HERE) if f.endswith('.html')}
_THIS = {t['slug'] for t in TOOLS18}
_EARLIER = _LIVE - _THIS
assert len(_EARLIER) >= 111, (
    'expected at least the 111 tools of batches 1 to 17, found %d'
    % len(_EARLIER))
PUBLISHED = _THIS <= _LIVE

_PLAN = io.open(os.path.join(HERE, '..', '..', 'docs',
                             'corpnilfilingfor300-seo-website-plan.md'),
                encoding='utf-8').read()
for t in TOOLS18:
    assert '\n/%s/\n' % t['slug'] in _PLAN, (
        '%s is not an Appendix A URL' % t['slug'])

for t in TOOLS18:
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
    assert not _dupe, '%s: %s declared twice, PRELUDE applied twice' % (s, _dupe)

    _body = ''.join(h for _i, _h2, h in t['sections'])
    assert CLOSE[s] in _body, '%s: its closing sentence is missing' % s

    for _form in ('CO-17', 'AT1'):
        if _form in _body:
            assert 'separate' in _body, '%s: %s not called separate' % (s, _form)

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
            assert fid in fields, '%s: js reads field %s the form lacks' % (s, fid)

    _all = (t['form'] + _body + ''.join(q + aa for q, aa in t['faq'])
            + ''.join(u2 for u2, _x in t['related']) + t['js'])
    for u in _re.findall(r'href="' + SITE + r'/tools/([a-z0-9-]+)/"', _all):
        assert u in _LIVE or u in _THIS, '%s: links to missing tool %s' % (s, u)
    _F9 = {f[:-5] for f in os.listdir(os.path.join(HERE, '..', 'f9'))
           if f.endswith('.html')}
    for u in _re.findall(r'href="' + SITE + r'/guides/([a-z0-9-]+)/"', _all):
        assert u in _F9, '%s: links to missing guide %s' % (s, u)

    assert 'plus HST' not in _all and 'including HST' not in _all, \
        '%s: names HST on a national tool' % s
    assert not _re.search(r'\bT183\b(?!CORP)', _all), '%s: bare T183' % s
    assert 'FAQPage' not in _all and 'aggregateRating' not in _all, s
    assert 'HowTo' not in _all, s
    _low = (_all + t['seo_title'] + t['seo_desc'] + t['meta']).lower()
    for _w in ('cheapest', 'best price', 'fastest', 'guaranteed', 'risk-free',
               'book a call', 'calendly', 'cra approved', 'cra agent',
               'cra authorized', 'cra authorised', 'cra partner'):
        assert _w not in _low, '%s: banned phrase "%s"' % (s, _w)
    _R3_OK = {'no percentage late-filing penalty', 'no percentage penalty',
              'no prior penalty'}
    for _m in _re.finditer(r'\bno (?:[a-z-]+ ){0,3}penalt\w*', _low):
        _p = _re.sub(r'(penalty|penalties)\w*$', r'\1', _m.group(0))
        if not any(_p.startswith(_ok) for _ok in _R3_OK):
            raise AssertionError('%s: rule 3, unqualified %r'
                                 % (s, _m.group(0)))
    for _m in _re.finditer(r'penalty[- ]free|zero penalt', _low):
        raise AssertionError('%s: rule 3, %r' % (s, _m.group(0)))

assert len({t['seo_title'] for t in TOOLS18}) == len(TOOLS18), 'title clash'
assert len({t['seo_desc'] for t in TOOLS18}) == len(TOOLS18), 'desc clash'
assert len({t['keyword'] for t in TOOLS18}) == len(TOOLS18), 'keyword clash'
assert len({t['h1'] for t in TOOLS18}) == len(TOOLS18), 'h1 clash'


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = TODAY, ISO
    build_f2.PRICE = PRICE
    recs = []
    for t in TOOLS18:
        html, url = render(t)
        assert 'plus HST' not in html, '%s still names HST' % t['slug']
        _risk = script_entity_risk(html)
        assert not _risk, (
            '%s: an & sits inside a tag-like span in a <script>, which '
            'WordPress entity-encodes and which breaks the module live. '
            'Offending: %r' % (t['slug'], _risk))
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2r-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-52s %6d bytes' % (r['slug'], len(r['content'].encode())))
