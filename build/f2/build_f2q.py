# -*- coding: utf-8 -*-
"""Family 2 batch 17: five more Appendix A tools.

Navneet, 2026-11-20: "NOW create next 5 calculators". Same three tests batch
16 used: the term is one people search, no live tool answers it, and the answer
routes back to a nil T2.

  107  /tools/t4-late-filing-penalty-calculator/              Appendix A 2792
  108  /tools/shareholder-loan-repayment-deadline-calculator/ Appendix A 2866
  109  /tools/ontario-initial-return-deadline-calculator/     Appendix A 2950
  110  /tools/gross-negligence-penalty-checker/               Appendix A 2800
  111  /tools/gst-hst-registration-requirement-checker/       Appendix A 2944

WHAT EACH ONE ADDS THAT A LIVE TOOL DOES NOT
--------------------------------------------
Every one of the five was checked against the 106 live slugs, because batch 16
found seven Appendix A entries that a live tool already answered.

- 107 against live /tools/t4-nil-filing-requirement-checker/: that one answers
  whether a T4 return is owed at all. This one computes what filing it late
  costs, on the sliding scale in subsection 162(7.01), which is a different
  question and a much larger search term.
- 108 against live /tools/shareholder-loan-balance-checker/,
  /tools/due-to-versus-due-from-shareholder-checker/ and
  /tools/schedule-11-shareholder-transactions-checker/: those three cover the
  balance, which side it sits on, and whether it is reportable. None of them
  carries the subsection 15(2.6) repayment deadline, which is the only part of
  the subject with a date in it.
- 109 against live /tools/ontario-annual-return-due-date-calculator/: the
  initial return runs 60 days from incorporation, the annual return six months
  from the year-end. build_f2o.py records that Section 6(e) conflates the two
  and names the incorporation date as the input for the annual one; this is the
  tool that actually takes the incorporation date.
- 110 against live /tools/nil-return-late-penalty-checker/ and batch 16's two
  penalty tools: those are subsection 162(1) and 162(2), both percentages of
  tax unpaid. Subsection 163(2) is a different provision with a different base
  (understated tax), a different rate (50%) and a knowledge element the others
  do not have.
- 111 against live /tools/gst-hst-nil-filing-checker/,
  /tools/gst-hst-account-closure-checker/ and batch 16's
  /tools/gst-hst-nil-return-deadline-calculator/: all three assume an account
  exists. This one answers whether one has to exist, which is the $30,000
  small-supplier question and the highest-volume term in the batch.

THE SUBSECTION 15(2) NUANCE, WHICH IS THE POINT OF 108
------------------------------------------------------
A shareholder loan that misses the 15(2.6) deadline is included in the
SHAREHOLDER's income, under subsection 15(2). It is not corporate income. So
the corporation's year can still be perfectly nil while the shareholder has a
personal problem, and the tool says exactly that rather than implying the
company stopped being nil. Getting this backwards is the obvious way to write
this page wrong, and it is why the result screen separates the two taxpayers.

WHAT IS NOT HERE
----------------
/tools/gifi-code-lookup-checker/ was on the shortlist and was dropped: it would
have to publish specific GIFI code numbers, and those are not facts this file
should assert from memory on a CPA firm's site. It needs the TaxCycle mapping
that plan line 1221 names as the source for Family 2 tables. Left for whoever
has that mapping to hand.

/tools/ontario-corporate-key-checker/ was also dropped, on the same ground:
the useful version of it turns on what the Registry does when a key is lost and
the registered office address is stale, and that process is not something to
state without checking it against ontario.ca first.

THE FEE WORDING
---------------
All five are national tools, so none names HST. Same 2026-11-12 decision, same
shadowing of PRICE and the overflow price that build_f2o.py and build_f2p.py
record.
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
TODAY, ISO = 'November 20, 2026', '2026-11-20'

# Live tools these five link to; every one asserted to exist below.
T4REQ    = T + 't4-nil-filing-requirement-checker/'
PAYNIL   = T + 'payroll-nil-remittance-checker/'
PAYCLOSE = T + 'payroll-account-closure-checker/'
SHBAL    = T + 'shareholder-loan-balance-checker/'
SHDIR    = T + 'due-to-versus-due-from-shareholder-checker/'
SCH11    = T + 'schedule-11-shareholder-transactions-checker/'
ONTANN   = T + 'ontario-annual-return-due-date-calculator/'
ONTREG   = T + 'ontario-business-registry-filing-checker/'
ONTMISS  = T + 'ontario-missed-annual-returns-calculator/'
FEDANN   = T + 'federal-annual-return-anniversary-calculator/'
NILPEN   = T + 'nil-return-late-penalty-checker/'
ARB      = T + 'arbitrary-assessment-response-checker/'
GSTNIL   = T + 'gst-hst-nil-filing-checker/'
GSTCLOSE = T + 'gst-hst-account-closure-checker/'
SEQ      = T + 'cra-account-closure-sequencer/'
DORMTEST = T + 'dormant-corporation-test/'
REQD     = T + 't2-filing-requirement-checker/'
CATCHUP  = T + 'catch-up-filing-schedule-generator/'

# Batch 16's five, now live.
P_LATE   = T + 't2-late-filing-penalty-calculator/'
P_REPEAT = T + 'repeated-failure-to-file-penalty-calculator/'
P_GSTDUE = T + 'gst-hst-nil-return-deadline-calculator/'
P_RELIEF = T + 'taxpayer-relief-eligibility-checker/'
P_VDP    = T + 'voluntary-disclosure-eligibility-checker/'

# This batch's own, for cross-links.
Q_T4     = T + 't4-late-filing-penalty-calculator/'
Q_SHLOAN = T + 'shareholder-loan-repayment-deadline-calculator/'
Q_ONTINI = T + 'ontario-initial-return-deadline-calculator/'
Q_GROSS  = T + 'gross-negligence-penalty-checker/'
Q_GSTREG = T + 'gst-hst-registration-requirement-checker/'

# Section 6(g) guides.
G_PAY    = G + 'cra-accounts-on-a-dormant-corporation/'
G_SHARE  = G + 'schedule-50-and-shareholder-reporting/'
G_ANN    = G + 'provincial-and-federal-annual-returns/'
G_PEN    = G + 't2-late-filing-penalties/'


def _tbl(head, rows):
    return ('<table class="ei-tbl"><thead><tr>'
            + ''.join('<th scope="col">%s</th>' % h for h in head)
            + '</tr></thead><tbody>\n'
            + '\n'.join('<tr>' + ''.join('<td>%s</td>' % c for c in r)
                        + '</tr>' for r in rows)
            + '\n</tbody></table>')


CLOSE = {
 't4-late-filing-penalty-calculator':
   'The slip count sets the rate and the ceiling, so two corporations the same '
   'number of days late can owe very different amounts.',
 'shareholder-loan-repayment-deadline-calculator':
   'The deadline belongs to the corporation&rsquo;s year end and the '
   'consequence belongs to the shareholder, which is why missing it does not '
   'make the company&rsquo;s year stop being nil.',
 'ontario-initial-return-deadline-calculator':
   'Sixty days from incorporation, once, and it is not the return that comes '
   'back every year afterwards.',
 'gross-negligence-penalty-checker':
   'This provision needs something to have been understated before any rate '
   'applies to it, and on a true nil return nothing was.',
 'gst-hst-registration-requirement-checker':
   'Whether an account has to exist and whether an existing one has to file '
   'are two questions, and a dormant corporation often answers them '
   'differently.',
}

# ====================================== 107. T4 late filing, 162(7.01)
T107_JS = RBASE + MONEY_JS + r"""
/* [slip ceiling, minimum, each day, maximum], the last three in cents.
   Subsection 162(7.01): 1-50 slips is $10.00 a day, at least $100.00 and at
   most $1,000.00, and each band above it steps up. A slip ceiling of 0 means
   the open-ended top band. */
var BANDS=[[50,10000,1000,100000],[500,15000,1500,150000],
           [2500,25000,2500,250000],[10000,50000,5000,500000],
           [0,75000,7500,750000]];
var out=document.getElementById('out');
function band(n){
  for(var i=0;i<BANDS.length;i++){
    if(BANDS[i][0]===0){return i;}
    if(!(n > BANDS[i][0])){return i;}
  }
  return BANDS.length-1;
}
function show(){
  var rawS=document.getElementById('slips').value.trim(),
      rawD=document.getElementById('days').value.trim(),h,wait=0;
  if(rawS===''){wait++;}
  if(rawD===''){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the two figures '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var slips=parseInt(rawS,10),days=parseInt(rawD,10);
  if(isNaN(slips)||isNaN(days)||0 > slips||0 > days){
    out.innerHTML='<p>Enter the slip count and the days late as whole '
     +'numbers.</p>';return;
  }
  if(slips===0){
    h='<h3>No slips means no T4 return, so this penalty does not arise</h3>';
    h+='<p>Subsection 162(7.01) charges for filing an information return '
     +'late. A corporation that paid no remuneration in the year has no slips '
     +'to issue and so no T4 return to be late with. Whether the open payroll '
     +'account still owes a nil remittance is a different question, and the '
     +'<a href="SITET4REQ">T4 nil filing requirement checker</a> answers '
     +'it.</p>';
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  var i=band(slips),rate=BANDS[i][2],mn=BANDS[i][1],mx=BANDS[i][3];
  var raw=rate*days,amt=raw;
  if(mn > amt){amt=mn;}
  if(amt > mx){amt=mx;}
  h='<h3>'+money(amt)+' under subsection 162(7.01)</h3>';
  h+='<p>'+slips+' slip'+(slips===1?'':'s')+' puts the return in the '
   +money(rate)+' a day band, with a floor of '+money(mn)+' and a ceiling of '
   +money(mx)+'. At '+days+' day'+(days===1?'':'s')+' late the daily figure '
   +'is '+money(raw)
   +(mn > raw?', below the floor, so the floor applies'
     :(raw > mx?', above the ceiling, so the ceiling applies':''))
   +'.</p>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Slips</th>'
   +'<th scope="col">Each day late</th><th scope="col">Least</th>'
   +'<th scope="col">Most</th><th scope="col">Your band</th>'
   +'</tr></thead><tbody>';
  var LAB=['1 to 50','51 to 500','501 to 2,500','2,501 to 10,000',
           '10,001 or more'];
  for(var k=0;k<BANDS.length;k++){
    h+='<tr><td>'+LAB[k]+'</td><td>'+money(BANDS[k][2])+'</td><td>'
     +money(BANDS[k][1])+'</td><td>'+money(BANDS[k][3])+'</td><td>'
     +(k===i?'Yes':'')+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>The T4 return is due the last day of February for the preceding '
   +'calendar year. This figure is the information-return penalty and is '
   +'separate from anything owed on the T2: nil T2 filing at '+PRICE_JS
   +' covers the corporate income tax return and not a payroll filing. The '
   +'<a href="SITEPAYNIL">payroll nil remittance checker</a> and the '
   +'<a href="SITEPAYCLOSE">payroll account closure checker</a> cover the '
   +'account itself.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITET4REQ', T4REQ).replace('SITEPAYNIL', PAYNIL) \
   .replace('SITEPAYCLOSE', PAYCLOSE)

T107 = dict(
 slug='t4-late-filing-penalty-calculator',
 title='T4 Late Filing Penalty Calculator | Subsection 162(7.01)',
 h1_pre='T4 Late Filing ', h1_span='Penalty Calculator',
 h1='T4 Late Filing Penalty Calculator',
 eyebrow='Payroll',
 keyword='t4 late filing penalty',
 seo_title='T4 Late Filing Penalty Calculator',
 seo_desc=('The slip count sets the daily rate and the ceiling. Enter slips '
           'and days late for the figure under subsection 162(7.01).'),
 meta=('The information-return penalty runs on a sliding scale set by how '
       'many slips the return carries, with a floor and a ceiling for each '
       'band.'),
 tags=['Five bands by slip count', 'A floor and a ceiling each',
       'Due the last day of February', 'Separate from the T2'],
 form=tool('Your T4 return',
           [num('slips', 'Number of T4 slips on the return',
                'Enter 0 if no remuneration was paid', 0, 100000, '0'),
            num('days', 'Days the return is late',
                'Counted from the last day of February', 0, 3650, '0')],
           'Enter the slip count and how many days late the return is.'),
 js=None,
 sections=[
  ('the-scale', 'The Slip Count Sets the Rate, Not the Lateness',
   '<p>Subsection 162(7.01) charges a daily amount for filing an information '
   'return late, and the amount per day depends on how many slips the return '
   'carries. A return with fifty slips or fewer runs at $10.00 a day with a '
   'floor of $100.00 and a ceiling of $1,000.00. Each band above it doubles '
   'or more.</p>\n'
   '<p>Two consequences follow. A small payroll cannot be charged more than '
   '$1,000.00 however long the return sits unfiled, and a return only one or '
   'two days late still meets the floor, so there is no cheap window for '
   'being slightly late.</p>'),
  ('bands', 'The Five Bands, and the Two Figures That Bound Each',
   _tbl(['Slips on the return', 'Each day late', 'Least', 'Most'],
        [['1 to 50', '$10.00', '$100.00', '$1,000.00'],
         ['51 to 500', '$15.00', '$150.00', '$1,500.00'],
         ['501 to 2,500', '$25.00', '$250.00', '$2,500.00'],
         ['2,501 to 10,000', '$50.00', '$500.00', '$5,000.00'],
         ['10,001 or more', '$75.00', '$750.00', '$7,500.00']])
   + '\n<p>A dormant corporation is almost always in the first band or has no '
   'return at all. Where no remuneration was paid in the year there are no '
   'slips, so there is no T4 return to be late with, and the question becomes '
   'whether the open account still owes a nil remittance. The '
   + a(T4REQ, 'T4 nil filing requirement checker')
   + ' settles that, and the '
   + a(PAYNIL, 'payroll nil remittance checker')
   + ' covers the remittance side.</p>\n'
   '<p>' + CLOSE['t4-late-filing-penalty-calculator'] + '</p>'),
  ('not-the-t2', 'A Payroll Filing Is Not the Corporate Return',
   '<p>The T4 return is due the last day of February for the calendar year '
   'before it, which has nothing to do with the six months that governs the '
   'T2. The two filings sit on different calendars, go to different parts of '
   'the Canada Revenue Agency and carry different penalties.</p>\n'
   '<p>' + a(COST, 'Nil T2 filing at ' + PRICE)
   + ' covers the federal corporate income tax return. A payroll account and '
   'its slips are not part of that fee. Where the account is being wound '
   'down, the '
   + a(PAYCLOSE, 'payroll account closure checker')
   + ' and the '
   + a(SEQ, 'CRA account closure sequencer')
   + ' set out the order, and the '
   + a(G_PAY, 'guide to CRA accounts on a dormant corporation')
   + ' covers every account a quiet corporation still carries.</p>'),
 ],
 faq=[
  ('How much is the penalty for filing T4 slips late?',
   'It depends on the slip count. One to fifty slips is $10.00 a day, with a '
   'minimum of $100.00 and a maximum of $1,000.00.'),
  ('When is the T4 return due?',
   'The last day of February for the preceding calendar year.'),
  ('Is there a minimum penalty?',
   'Yes. Each band has a floor, so a return even one day late reaches at '
   'least that amount.'),
  ('Is there a maximum?',
   'Yes, per band. The first band caps at $1,000.00 however long the return '
   'stays unfiled.'),
  ('What if the corporation paid no wages?',
   'Then there are no slips and no T4 return to file late. Whether the open '
   'payroll account still owes a nil remittance is a separate question.'),
  ('Does this penalty apply to the T2?',
   'No. The T2 has its own late-filing provisions, which are percentages of '
   'tax owing rather than a daily amount.'),
  ('Is the penalty per slip or per return?',
   'Per return. The slip count selects which band the return falls in.'),
  ('Does a nil T2 fee cover T4 slips?',
   'No. The fee covers the federal corporate income tax return. Payroll '
   'filings sit outside it.'),
  ('Can the penalty be cancelled?',
   'It can be the subject of a taxpayer relief request on specified grounds, '
   'within the ten-year window those requests carry.'),
  ('Do weekends count in the days late?',
   'The charge is a daily one and runs on calendar days once the return is '
   'past its due date.'),
 ],
 related=[
  (T4REQ, 'T4 nil filing requirement checker'),
  (PAYNIL, 'Payroll nil remittance checker'),
  (PAYCLOSE, 'Payroll account closure checker'),
  (P_LATE, 'T2 late filing penalty calculator'),
  (P_RELIEF, 'Taxpayer relief eligibility checker'),
  (SEQ, 'CRA account closure sequencer'),
 ],
)

# ============================ 108. shareholder loan, 15(2.6)
T108_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var ye=parse('ye'),rep=pick('rep'),h,wait=0;
  if(ye===null||ye===undefined){wait++;}
  if(rep===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the two entries '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var due=addYear(ye,1),now=today(),past=(now.getTime() > due.getTime());
  var days=Math.abs(Math.round((due.getTime()-now.getTime())/86400000));
  if(rep==='y'){
    h='<h3>Repaid, so subsection 15(2) does not reach it</h3>';
    h+='<p>The deadline for a loan advanced in the year ending '+fmt(ye)
     +' was '+fmt(due)+'. A loan repaid by then is outside subsection 15(2) '
     +'altogether, and nothing is added to anyone&rsquo;s income.</p>';
  }else if(past){
    h='<h3>The deadline passed '+fmt(due)+'</h3>';
    h+='<p>That was '+days+' day'+(days===1?'':'s')+' ago. A loan still '
     +'outstanding after the deadline is included in the '
     +'<strong>shareholder&rsquo;s</strong> income under subsection 15(2), '
     +'for the year the loan was made rather than the year the deadline '
     +'passed.</p>';
  }else{
    h='<h3>Repay by '+fmt(due)+'</h3>';
    h+='<p>That is '+days+' day'+(days===1?'':'s')+' away. A loan advanced '
     +'in the tax year ending '+fmt(ye)+' has to be repaid within one year '
     +'after that year end to stay outside subsection 15(2).</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">What</th>'
   +'<th scope="col">Date or effect</th>'
   +'<th scope="col">Whose return it lands on</th></tr></thead><tbody>';
  h+='<tr><td>Tax year the loan was advanced in</td><td>Ends '+fmt(ye)
   +'</td><td>The corporation</td></tr>';
  h+='<tr><td>Repayment deadline, 15(2.6)</td><td>'+fmt(due)
   +'</td><td>Neither, while it is met</td></tr>';
  h+='<tr><td>If it is not repaid by then</td>'
   +'<td>The amount is income under 15(2)</td>'
   +'<td>The shareholder, personally</td></tr>';
  h+='<tr><td>The corporation&rsquo;s own year</td>'
   +'<td>A loan is a balance sheet item, not income</td>'
   +'<td>Can still be nil</td></tr>';
  h+='</tbody></table>';
  h+='<p>That last row is the part most often got backwards. Subsection 15(2) '
   +'puts the amount in the shareholder&rsquo;s hands, not the '
   +'corporation&rsquo;s, so a missed deadline is a personal tax problem and '
   +'does not by itself stop the corporate year from being nil. Nil T2 filing '
   +'at '+PRICE_JS+' still covers that year. '+NOTNILJS+'</p>';
  h+='<p>A balance that simply sat still all year is a different matter '
   +'again, and the '
   +'<a href="SITESHBAL">shareholder loan balance checker</a> covers it.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITESHBAL', SHBAL)

T108 = dict(
 slug='shareholder-loan-repayment-deadline-calculator',
 title='Shareholder Loan Repayment Deadline | Subsection 15(2.6)',
 h1_pre='Shareholder Loan ', h1_span='Repayment Deadline',
 h1='Shareholder Loan Repayment Deadline Calculator',
 eyebrow='Shareholder',
 keyword='shareholder loan repayment deadline',
 seo_title='Shareholder Loan Repayment Deadline Calculator',
 seo_desc=('One year after the end of the corporate tax year the loan was '
           'made in. Miss it and subsection 15(2) taxes the shareholder, not '
           'the company.'),
 meta=('The one-year rule runs from the corporation&rsquo;s year end, and the '
       'consequence of missing it lands on the shareholder rather than the '
       'corporation.'),
 tags=['One year after the year end', 'Subsection 15(2.6)',
       'Taxes the shareholder', 'The company can still be nil'],
 form=tool('The loan and the year it was advanced in',
           [date('ye', 'The corporation&rsquo;s year end for the year the '
                       'loan was advanced'),
            yn('rep', 'Has the loan been repaid?')],
           'Enter that year end and say whether the loan has been repaid.'),
 js=None,
 sections=[
  ('the-rule', 'One Year After the Year End, Not One Year After the Loan',
   '<p>Subsection 15(2) of the Income Tax Act treats a loan from a '
   'corporation to its shareholder as income of that shareholder. Subsection '
   '15(2.6) takes it back out again where the loan is repaid within one year '
   'after the end of the corporation&rsquo;s taxation year in which it was '
   'made.</p>\n'
   '<p>The clock therefore runs from the year end, not from the advance. A '
   'loan taken in the first week of a December year end has nearly two years '
   'to be repaid; one taken a week before that year end has barely one. Same '
   'rule, very different windows, which is why the date is worth working '
   'out rather than assuming.</p>'),
  ('whose-income', 'The Consequence Lands on the Shareholder',
   _tbl(['', 'The corporation', 'The shareholder'],
        [['A loan outstanding at the year end',
          'A balance sheet item, not income', 'Nothing yet'],
         ['Repaid inside the 15(2.6) window', 'Unchanged', 'Nothing'],
         ['Still outstanding after the window', 'Unchanged',
          'The amount is income under 15(2)'],
         ['Effect on a nil year', 'None by itself',
          'A personal filing matter']])
   + '\n<p>A corporation whose only activity was lending money to its own '
   'shareholder has still earned nothing, so its year can be nil and its T2 '
   'can be a nil return. What changes is the shareholder&rsquo;s personal '
   'position. The '
   + a(SHBAL, 'shareholder loan balance checker')
   + ' covers what an outstanding balance means for the return itself, and '
   'the '
   + a(SHDIR, 'due to versus due from shareholder checker')
   + ' settles which direction the balance runs.</p>\n'
   '<p>' + CLOSE['shareholder-loan-repayment-deadline-calculator'] + '</p>'),
  ('reporting', 'What the Return Reports, and What the Fee Covers',
   '<p>A loan balance is reported on the balance sheet in GIFI, and movement '
   'in the year can bring Schedule 11 into play. The '
   + a(SCH11, 'Schedule 11 shareholder transactions checker')
   + ' separates a balance that sat still from a transaction, which is the '
   'distinction that decides whether anything is reportable at all.</p>\n'
   '<p>' + a(COST, 'Nil T2 filing at ' + PRICE)
   + ' covers the corporate return for a nil year, including one in which a '
   'shareholder loan sits on the balance sheet. It does not cover personal '
   'returns, and a 15(2) inclusion is a personal matter to take advice on. '
   'The '
   + a(G_SHARE, 'guide to Schedule 50 and shareholder reporting')
   + ' covers the reporting side in full.</p>'),
 ],
 faq=[
  ('When does a shareholder loan have to be repaid?',
   'Within one year after the end of the corporation&rsquo;s taxation year in '
   'which the loan was made.'),
  ('Does the clock run from the date of the loan?',
   'No. It runs from the corporation&rsquo;s year end for the year the loan '
   'was advanced.'),
  ('What happens if it is not repaid in time?',
   'Subsection 15(2) includes the amount in the shareholder&rsquo;s income '
   'for the year the loan was made.'),
  ('Does the corporation pay tax on it?',
   'No. The inclusion is the shareholder&rsquo;s, not the '
   'corporation&rsquo;s.'),
  ('Can the corporation still file a nil return?',
   'Yes. A loan is a balance sheet item, so a year with no income can still '
   'be nil even with a loan outstanding.'),
  ('Does repaying and re-borrowing restart the clock?',
   'A series of loans and repayments is looked at as a whole rather than '
   'taken at face value, so this is worth advice.'),
  ('Is the loan reported anywhere on the T2?',
   'The balance appears on the balance sheet in GIFI, and movement in the '
   'year may bring Schedule 11 into it.'),
  ('What if the shareholder owes the corporation instead?',
   'That is the same direction this page is about: a balance due from the '
   'shareholder is the one subsection 15(2) looks at.'),
  ('Does interest have to be charged?',
   'A low or no interest loan raises a separate benefit question, which is '
   'not what this page calculates.'),
  ('Is the inclusion reversed if the loan is repaid later?',
   'A deduction may be available to the shareholder in the year of '
   'repayment. The original inclusion stands for its year.'),
 ],
 related=[
  (SHBAL, 'Shareholder loan balance checker'),
  (SHDIR, 'Due to versus due from shareholder checker'),
  (SCH11, 'Schedule 11 shareholder transactions checker'),
  (DORMTEST, 'Dormant corporation test'),
  (REQD, 'T2 filing requirement checker'),
  (NILPEN, 'Nil return late penalty checker'),
 ],
)

# ====================== 109. Ontario initial return, 60 days
T109_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var inc=parse('inc'),ont=pick('ont'),filed=pick('filed'),h,wait=0;
  if(inc===null||inc===undefined){wait++;}
  if(ont===null){wait++;}
  if(filed===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three entries '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var due=new Date(inc.getTime()+60*86400000),now=today();
  var past=(now.getTime() > due.getTime());
  var days=Math.abs(Math.round((due.getTime()-now.getTime())/86400000));
  if(ont==='n'){
    h='<h3>This is not a filing your corporation makes</h3>';
    h+='<p>The initial return under the Corporations Information Act is for a '
     +'corporation incorporated, amalgamated or continued under Ontario law. '
     +'A federal corporation has its own annual return with Corporations '
     +'Canada instead, which the '
     +'<a href="SITEFEDANN">federal annual return anniversary calculator</a> '
     +'works out. Extra-provincial registration in Ontario is a separate '
     +'question again.</p>';
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  if(filed==='y'){
    h='<h3>Filed, and it is not due again</h3>';
    h+='<p>The initial return was due '+fmt(due)+', sixty days after '
     +fmt(inc)+'. It is a one-time filing. What comes back every year is the '
     +'annual return, on a different clock entirely.</p>';
  }else if(past){
    h='<h3>It was due '+fmt(due)+'</h3>';
    h+='<p>That was '+days+' day'+(days===1?'':'s')+' ago, counting sixty '
     +'days from '+fmt(inc)+'. An outstanding initial return leaves the '
     +'corporation out of compliance with the Province and the record '
     +'incomplete.</p>';
  }else{
    h='<h3>Due '+fmt(due)+'</h3>';
    h+='<p>Sixty days after '+fmt(inc)+', which is '+days+' day'
     +(days===1?'':'s')+' away.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Filing</th>'
   +'<th scope="col">What it turns on</th><th scope="col">How often</th>'
   +'<th scope="col">Covered by the nil T2 fee</th></tr></thead><tbody>';
  h+='<tr><td>Ontario initial return</td><td>Sixty days after '+fmt(inc)
   +'</td><td>Once</td><td>No</td></tr>';
  h+='<tr><td>Ontario annual return</td>'
   +'<td>Six months after each fiscal year end</td><td>Every year</td>'
   +'<td>No</td></tr>';
  h+='<tr><td>Federal T2 return</td>'
   +'<td>Six months after each fiscal year end</td><td>Every year</td>'
   +'<td>Yes</td></tr>';
  h+='</tbody></table>';
  h+='<p>Both Ontario filings go through the Ontario Business Registry and '
   +'neither is part of nil T2 filing at '+PRICE_JS+', which covers the '
   +'federal corporate return on the last row. The '
   +'<a href="SITEONTANN">Ontario annual return due date calculator</a> '
   +'handles the recurring one and the '
   +'<a href="SITEONTREG">Ontario Business Registry filing checker</a> '
   +'covers what else goes through the same system.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITEFEDANN', FEDANN).replace('SITEONTANN', ONTANN) \
   .replace('SITEONTREG', ONTREG)

T109 = dict(
 slug='ontario-initial-return-deadline-calculator',
 title='Ontario Initial Return Deadline | Sixty Days, Once',
 h1_pre='Ontario Initial Return ', h1_span='Deadline Calculator',
 h1='Ontario Initial Return Deadline Calculator',
 eyebrow='Ontario',
 keyword='ontario initial return deadline',
 seo_title='Ontario Initial Return Deadline Calculator',
 seo_desc=('Sixty days after incorporation, amalgamation or continuance, '
           'filed once through the Ontario Business Registry rather than with '
           'the T2.'),
 meta=('The initial return is a one-time Registry filing sixty days after '
       'incorporation, and it is not the annual return that follows the '
       'fiscal year end.'),
 tags=['Sixty days after incorporation', 'A one-time filing',
       'Ontario Business Registry', 'Not the annual return'],
 form=tool('Your Ontario corporation',
           [date('inc', 'The date of incorporation, amalgamation or '
                        'continuance'),
            yn('ont', 'Incorporated or continued under Ontario law?'),
            yn('filed', 'Has the initial return been filed?')],
           'Enter the date and answer the two questions.'),
 js=None,
 sections=[
  ('sixty-days', 'Sixty Days, and Only Once',
   '<p>A corporation incorporated, amalgamated or continued under Ontario law '
   'files an initial return under the Corporations Information Act within '
   'sixty days of that date. It records the registered office and the '
   'directors and officers as they stand at the start.</p>\n'
   '<p>It is a one-time filing. The return that comes back every year is the '
   'annual return, which runs six months from each fiscal year end and is a '
   'different filing with a different trigger. A new corporation owes both in '
   'its first eighteen months and the two are easily confused.</p>'),
  ('three-filings', 'Three Filings a New Ontario Corporation Meets',
   _tbl(['The filing', 'What the date turns on', 'How often'],
        [['Ontario initial return', 'Sixty days after incorporation', 'Once'],
         ['Ontario annual return', 'Six months after the fiscal year end',
          'Every year'],
         ['Federal T2 return', 'Six months after the fiscal year end',
          'Every year']])
   + '\n<p>Only the last is a tax return, and only the last is what '
   + a(COST, 'nil T2 filing at ' + PRICE)
   + ' covers. The two Ontario filings are corporate records that go through '
   'the Ontario Business Registry. The '
   + a(ONTANN, 'Ontario annual return due date calculator')
   + ' handles the recurring one, and where several years have gone by '
   'unfiled the '
   + a(ONTMISS, 'Ontario missed annual returns calculator')
   + ' counts them.</p>\n'
   '<p>' + CLOSE['ontario-initial-return-deadline-calculator'] + '</p>'),
  ('dormant', 'A Corporation That Never Traded Still Owes It',
   '<p>The initial return records who and where the corporation is, not what '
   'it earned, so having done nothing since incorporation does not remove it. '
   'A numbered company set up and left idle owes the initial return on the '
   'same sixty days as any other, and its first T2 is still due six months '
   'after its first year end even though the return itself is nil.</p>\n'
   '<p>The '
   + a(ONTREG, 'Ontario Business Registry filing checker')
   + ' covers what else goes through the Registry, and the '
   + a(G_ANN, 'guide to provincial and federal annual returns')
   + ' separates the Ontario and federal obligations end to end.</p>'),
 ],
 faq=[
  ('When is the Ontario initial return due?',
   'Within sixty days after the date of incorporation, amalgamation or '
   'continuance under Ontario law.'),
  ('Is it the same as the annual return?',
   'No. The initial return is filed once; the annual return comes back every '
   'year on the fiscal year end.'),
  ('Where is it filed?',
   'Through the Ontario Business Registry, not with the T2.'),
  ('Does a federal corporation file one?',
   'Not this one. A federal corporation files its annual return with '
   'Corporations Canada on the incorporation anniversary.'),
  ('Does a dormant corporation have to file it?',
   'Yes. It records the registered office and the directors rather than any '
   'activity, so inactivity does not remove it.'),
  ('Is it covered by the nil T2 fee?',
   'No. The fee covers the federal corporate income tax return. Registry '
   'filings sit outside it.'),
  ('What happens if it was never filed?',
   'The corporation is out of compliance with the Province and the public '
   'record is incomplete until it is filed.'),
  ('What does it actually report?',
   'The registered office address and the directors and officers as they '
   'stand at the start.'),
  ('Does an amalgamation trigger a new one?',
   'Yes. The sixty days runs from the date of the amalgamation.'),
  ('Does the T2 due date depend on it?',
   'No. The T2 runs six months from the fiscal year end regardless.'),
 ],
 related=[
  (ONTANN, 'Ontario annual return due date calculator'),
  (ONTREG, 'Ontario Business Registry filing checker'),
  (ONTMISS, 'Ontario missed annual returns calculator'),
  (FEDANN, 'Federal annual return anniversary calculator'),
  (REQD, 'T2 filing requirement checker'),
  (DORMTEST, 'Dormant corporation test'),
 ],
)

# ====================== 110. gross negligence, 163(2)
T110_JS = RBASE + MONEY_JS + r"""
var out=document.getElementById('out');
function show(){
  var know=pick('know'),nil=pick('nil'),
      raw=document.getElementById('under').value.trim(),h,wait=0;
  if(raw===''){wait++;}
  if(know===null){wait++;}
  if(nil===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three entries '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var under=Math.round(parseFloat(raw)*100);
  if(isNaN(under)||0 > under){
    out.innerHTML='<p>Enter the understated tax as a number, using 0 where '
     +'nothing was understated.</p>';return;
  }
  var half=Math.round(under*0.5),floor=10000,amt=(floor > half?floor:half);
  if(nil==='y'||under===0){
    h='<h3>Nothing was understated, so 163(2) has no base</h3>';
    h+='<p>Subsection 163(2) is half of the tax that was understated. On a '
     +'true nil return there is no understatement for the rate to apply to, '
     +'so the provision does not arise. '+QUALJS+'</p>';
  }else if(know==='n'){
    h='<h3>The knowledge element is not met on these answers</h3>';
    h+='<p>Subsection 163(2) applies only where the false statement or '
     +'omission was made knowingly, or in circumstances amounting to gross '
     +'negligence. An honest mistake is not that, and the onus of '
     +'establishing the facts sits with the Minister rather than the '
     +'taxpayer. On '+money(under)+' understated the figure would be '
     +money(amt)+' if it were met.</p>';
  }else{
    h='<h3>'+money(amt)+' under subsection 163(2)</h3>';
    h+='<p>Half of the '+money(under)+' understated'
     +(floor > half?', raised to the $100.00 minimum':'')
     +'. This is on top of any late-filing penalty and any interest, not '
     +'instead of them.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Provision</th>'
   +'<th scope="col">What it is a percentage of</th>'
   +'<th scope="col">Rate</th><th scope="col">On these answers</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>162(1), late filing</td><td>Tax unpaid at the due date</td>'
   +'<td>5% plus 1% a month</td><td>'
   +(nil==='y'?'$0.00 on a nil year':'Separate from this page')+'</td></tr>';
  h+='<tr><td>163(2), false statement</td><td>Tax understated</td>'
   +'<td>50%, at least $100.00</td><td>'
   +(nil==='y'||under===0?'No base':(know==='y'?money(amt):'Not met'))
   +'</td></tr>';
  h+='</tbody></table>';
  h+='<p>The two provisions measure different things. One asks when the '
   +'return arrived, the other asks whether what it said was true. A nil '
   +'return filed late is exposed to the first and has nothing for the '
   +'second to work on. The '
   +'<a href="SITELATE">T2 late filing penalty calculator</a> covers the '
   +'first, and the '
   +'<a href="SITEARB">arbitrary assessment response checker</a> covers what '
   +'happens when the Agency assesses a year itself.</p>';
  if(nil==='y'){
    h+='<p>Nil T2 filing at '+PRICE_JS+' closes a year like this one. '
     +NOTNILJS+'</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITELATE', P_LATE).replace('SITEARB', ARB)

T110 = dict(
 slug='gross-negligence-penalty-checker',
 title='Gross Negligence Penalty Checker | Subsection 163(2)',
 h1_pre='Gross Negligence ', h1_span='Penalty Checker',
 h1='Gross Negligence Penalty Checker',
 eyebrow='Penalty',
 keyword='gross negligence penalty',
 seo_title='Gross Negligence Penalty Checker',
 seo_desc=('Subsection 163(2) is half the tax understated, at least $100.00, '
           'and only where the statement was made knowingly or recklessly.'),
 meta=('This penalty is a percentage of what was understated rather than of '
       'what was owed late, and it carries a knowledge element the '
       'late-filing provisions do not.'),
 tags=['50% of tax understated', 'At least $100.00',
       'Needs knowledge or recklessness', 'No base on a nil return'],
 form=tool('The return and what it said',
           [num('under', 'Tax understated, in dollars',
                'Enter 0 where nothing was understated', 0, 100000000, '0'),
            yn('know', 'Was the statement or omission made knowingly, or in '
                       'circumstances amounting to gross negligence?'),
            yn('nil', 'Was the return a true nil return?')],
           'Enter the amount and answer the two questions.'),
 js=None,
 sections=[
  ('what-it-measures', 'A Percentage of What Was Understated',
   '<p>Subsection 163(2) of the Income Tax Act charges half of the tax that '
   'was understated by a false statement or an omission in a return, with a '
   'minimum of $100.00. It is not a late-filing penalty and has nothing to do '
   'with when the return arrived.</p>\n'
   '<p>It also carries an element the late-filing provisions do not: the '
   'statement or omission has to have been made knowingly, or in '
   'circumstances amounting to gross negligence. Carelessness falling short '
   'of that is not enough, and establishing the facts is the '
   'Minister&rsquo;s job rather than the taxpayer&rsquo;s.</p>'),
  ('versus-late', 'Set Against the Late-Filing Provisions',
   _tbl(['', 'Subsection 162(1)', 'Subsection 163(2)'],
        [['What it asks', 'When did the return arrive',
          'Was what it said true'],
         ['Percentage of', 'Tax unpaid at the due date', 'Tax understated'],
         ['Rate', '5% plus 1% a month to twelve', '50%'],
         ['Minimum', 'None', '$100.00'],
         ['Needs a state of mind', 'No',
          'Yes, knowledge or gross negligence'],
         ['On a true nil return', '$0.00, nothing unpaid',
          'No base, nothing understated']])
   + '\n<p>Both bottom cells matter to anyone filing nil years late. A return '
   'reporting no income, no tax and no credits understates nothing, so there '
   'is no base for this provision however many years went by. The '
   + a(P_LATE, 'T2 late filing penalty calculator')
   + ' and the '
   + a(NILPEN, 'nil return late penalty checker')
   + ' deal with the provision that does apply.</p>\n'
   '<p>' + CLOSE['gross-negligence-penalty-checker'] + '</p>'),
  ('catch-up', 'Why This Comes Up on Catch-Up Filings',
   '<p>The provision gets raised in connection with voluntary disclosures, '
   'because relief from it is one of the things a disclosure can achieve. '
   'That is useful where years carried real income that was never reported. '
   'It is beside the point where the years were genuinely nil, which is the '
   'more common case for a dormant corporation.</p>\n'
   '<p>The '
   + a(P_VDP, 'voluntary disclosure eligibility checker')
   + ' sets out the conditions, and the '
   + a(P_RELIEF, 'taxpayer relief eligibility checker')
   + ' covers cancelling charges already assessed. Where the years are nil, '
   + a(COST, 'nil T2 filing at ' + PRICE)
   + ' closes one per return and the '
   + a(CATCHUP, 'catch-up filing schedule generator')
   + ' orders them oldest first. The '
   + a(G_PEN, 'guide to T2 late-filing penalties')
   + ' sets out the provisions that do bite on an unfiled nil year.</p>'),
 ],
 faq=[
  ('What is the gross negligence penalty?',
   'Subsection 163(2): half of the tax understated by a false statement or '
   'omission, with a minimum of $100.00.'),
  ('Does it apply to filing late?',
   'No. Late filing is subsections 162(1) and 162(2). This one is about what '
   'the return said.'),
  ('Does carelessness count?',
   'Not on its own. The statement must be made knowingly or in circumstances '
   'amounting to gross negligence.'),
  ('Who has to prove it?',
   'The onus of establishing the facts justifying the penalty rests with the '
   'Minister.'),
  ('Can it apply to a nil return?',
   'A return reporting nothing understates nothing, so there is no base for '
   'the percentage.'),
  ('Is it charged instead of the late-filing penalty?',
   'No. It is in addition to any late-filing penalty and any interest.'),
  ('Is there a maximum?',
   'The provision sets a minimum rather than a maximum; the figure follows '
   'the amount understated.'),
  ('Does a voluntary disclosure remove it?',
   'Relief from this penalty is one of the things the programme can achieve, '
   'subject to its conditions.'),
  ('Does it apply to a corporation or a person?',
   'It applies to the taxpayer who made the return, which for a T2 is the '
   'corporation.'),
  ('What if the understated amount is small?',
   'The $100.00 minimum applies, so a small understatement still reaches '
   'that figure once the provision is engaged.'),
 ],
 related=[
  (P_LATE, 'T2 late filing penalty calculator'),
  (P_REPEAT, 'Repeated failure to file penalty calculator'),
  (NILPEN, 'Nil return late penalty checker'),
  (P_VDP, 'Voluntary disclosure eligibility checker'),
  (P_RELIEF, 'Taxpayer relief eligibility checker'),
  (ARB, 'Arbitrary assessment response checker'),
 ],
)

# ================= 111. GST/HST registration, the $30,000 question
T111_JS = RBASE + MONEY_JS + r"""
var out=document.getElementById('out');
function show(){
  var qtr=pick('qtr'),reg=pick('reg'),
      raw=document.getElementById('rev').value.trim(),h,wait=0;
  if(raw===''){wait++;}
  if(qtr===null){wait++;}
  if(reg===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three entries '
     +(wait===1?'is':'are')+' still to come.</p>';return;
  }
  var rev=Math.round(parseFloat(raw)*100),CAP=3000000;
  if(isNaN(rev)||0 > rev){
    out.innerHTML='<p>Enter the taxable revenue as a number, using 0 where '
     +'there was none.</p>';return;
  }
  var over=(rev > CAP),must=(over||qtr==='y');
  if(reg==='y'){
    h='<h3>Already registered, so the question is filing, not joining</h3>';
    h+='<p>An open account reports every period whether or not anything was '
     +'collected. Being under the threshold does not close an account or '
     +'excuse its returns; only closing it does. The '
     +'<a href="SITEGSTNIL">GST/HST nil filing checker</a> covers the '
     +'returns and the '
     +'<a href="SITEGSTCLOSE">GST/HST account closure checker</a> covers '
     +'form RC145.</p>';
  }else if(must){
    h='<h3>Registration is required on these answers</h3>';
    h+='<p>'+(qtr==='y'?'A single calendar quarter over $30,000.00 ends '
      +'small-supplier status on its own'
      :'Taxable revenue of '+money(rev)+' over four consecutive calendar '
      +'quarters is above the $30,000.00 threshold')
     +', so the corporation is no longer a small supplier.</p>';
  }else{
    h='<h3>A small supplier on these answers</h3>';
    h+='<p>'+money(rev)+' over four consecutive calendar quarters is at or '
     +'below the $30,000.00 threshold and no single quarter went over it, so '
     +'registration is not required. It stays available voluntarily.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Test</th>'
   +'<th scope="col">The threshold</th><th scope="col">On these answers</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Four consecutive calendar quarters</td>'
   +'<td>More than $30,000.00</td><td>'
   +money(rev)+(over?', over':', at or under')+'</td></tr>';
  h+='<tr><td>Any single calendar quarter</td>'
   +'<td>More than $30,000.00</td><td>'
   +(qtr==='y'?'Yes, over':'No')+'</td></tr>';
  h+='<tr><td>An account already open</td>'
   +'<td>Files regardless of revenue</td><td>'
   +(reg==='y'?'Yes':'No')+'</td></tr>';
  h+='</tbody></table>';
  h+='<p>A dormant corporation earning nothing is a small supplier and need '
   +'not register. The trap is the account nobody closed: once open it keeps '
   +'its own filing calendar whatever the revenue, which the '
   +'<a href="SITEGSTDUE">GST/HST nil return deadline calculator</a> '
   +'dates.</p>';
  h+='<p>Nil T2 filing at '+PRICE_JS+' covers the federal corporate income '
   +'tax return. A GST/HST account is a separate registration with its own '
   +'returns, and neither registering nor filing it is part of that fee.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
""".replace('SITEGSTNIL', GSTNIL).replace('SITEGSTCLOSE', GSTCLOSE) \
   .replace('SITEGSTDUE', P_GSTDUE)

T111 = dict(
 slug='gst-hst-registration-requirement-checker',
 title='GST/HST Registration Requirement Checker | $30,000',
 h1_pre='GST/HST Registration ', h1_span='Requirement Checker',
 h1='GST/HST Registration Requirement Checker',
 eyebrow='GST/HST',
 keyword='gst hst registration requirement',
 seo_title='GST/HST Registration Requirement Checker',
 seo_desc=('Small-supplier status ends above $30,000.00 over four '
           'consecutive calendar quarters, or in any single quarter that '
           'goes over.'),
 meta=('The threshold is tested two ways, and an account that is already '
       'open files its returns whatever the revenue turns out to be.'),
 tags=['$30,000.00 threshold', 'Four quarters, or any one',
       'A dormant year is under it', 'An open account files anyway'],
 form=tool('Your taxable revenue',
           [num('rev', 'Worldwide taxable revenue over the last four '
                       'calendar quarters, in dollars',
                'Enter 0 where there was none', 0, 100000000, '0'),
            yn('qtr', 'Did any single calendar quarter go over $30,000.00?'),
            yn('reg', 'Is the corporation already registered?')],
           'Enter the revenue and answer the two questions.'),
 js=None,
 sections=[
  ('two-tests', 'The Threshold Is Tested Two Ways',
   '<p>A small supplier is not required to register for GST/HST. The status '
   'ends when taxable revenue goes over $30,000.00, and that is measured over '
   'four consecutive calendar quarters. It also ends where a single calendar '
   'quarter on its own goes over the same figure, which is the test people '
   'forget.</p>\n'
   '<p>Registration stays available voluntarily below the threshold, and '
   'there are reasons to take it, chiefly recovering tax paid on inputs. This '
   'page answers whether it is required, not whether it is wise.</p>'),
  ('dormant', 'A Dormant Corporation Is Under the Threshold and May Still File',
   _tbl(['', 'Must register', 'Must file returns'],
        [['No revenue, no account', 'No', 'No'],
         ['No revenue, account still open', 'Not applicable',
          'Yes, nil returns'],
         ['Over $30,000.00 in four quarters', 'Yes', 'Yes'],
         ['Over $30,000.00 in one quarter', 'Yes', 'Yes']])
   + '\n<p>The second row is where dormant corporations actually sit. '
   'Registering is a question about revenue; filing is a question about '
   'whether an account exists. A corporation that earned nothing but never '
   'closed its account is behind on returns while being comfortably under the '
   'threshold. The '
   + a(GSTNIL, 'GST/HST nil filing checker')
   + ' decides whether returns are owed and the '
   + a(P_GSTDUE, 'GST/HST nil return deadline calculator')
   + ' dates them.</p>\n'
   '<p>' + CLOSE['gst-hst-registration-requirement-checker'] + '</p>'),
  ('closing', 'Closing the Account Is What Ends the Filing',
   '<p>Falling back under the threshold does not close an account and does '
   'not excuse its returns. Closing it takes a final return and form RC145, '
   'and where several accounts are being wound down together the order '
   'matters. The '
   + a(GSTCLOSE, 'GST/HST account closure checker')
   + ' covers the closure and the '
   + a(SEQ, 'CRA account closure sequencer')
   + ' covers the order.</p>\n'
   '<p>' + a(COST, 'Nil T2 filing at ' + PRICE)
   + ' covers the federal corporate income tax return. A GST/HST '
   'registration is separate from it, and the '
   + a(G_PAY, 'guide to CRA accounts on a dormant corporation')
   + ' covers every account a quiet corporation still carries.</p>'),
 ],
 faq=[
  ('When does a corporation have to register for GST/HST?',
   'When taxable revenue goes over $30,000.00 over four consecutive calendar '
   'quarters, or in any single calendar quarter.'),
  ('What is a small supplier?',
   'A person whose taxable revenue stays at or below the $30,000.00 '
   'threshold, and who is therefore not required to register.'),
  ('Does a dormant corporation have to register?',
   'No. With no taxable revenue it is under the threshold.'),
  ('Does being under the threshold close an existing account?',
   'No. An open account keeps filing its returns until it is closed.'),
  ('Can a corporation register voluntarily?',
   'Yes. Registration is available below the threshold, chiefly to recover '
   'tax paid on inputs.'),
  ('Is the test on revenue or on profit?',
   'On taxable revenue, not on profit, and it is measured worldwide.'),
  ('What happens the moment the threshold is passed?',
   'Small-supplier status ends and registration becomes required; the exact '
   'effective date depends on which test was crossed.'),
  ('Does the nil T2 fee cover GST/HST?',
   'No. The fee covers the federal corporate income tax return. GST/HST is a '
   'separate registration.'),
  ('How is an account closed?',
   'With a final return for the period up to the closure date and form '
   'RC145.'),
  ('Does the T2 depend on the GST/HST account?',
   'No. The corporate return is owed on its own terms whether or not an '
   'account exists.'),
 ],
 related=[
  (GSTNIL, 'GST/HST nil filing checker'),
  (P_GSTDUE, 'GST/HST nil return deadline calculator'),
  (GSTCLOSE, 'GST/HST account closure checker'),
  (SEQ, 'CRA account closure sequencer'),
  (DORMTEST, 'Dormant corporation test'),
  (REQD, 'T2 filing requirement checker'),
 ],
)

TOOLS17 = [T107, T108, T109, T110, T111]
_JS17 = [T107_JS, T108_JS, T109_JS, T110_JS, T111_JS]

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

for _t, _js in zip(TOOLS17, _JS17):
    assert OVERFLOW_WAS in _js, (
        '%s: the overflow price moved; re-check the shadow' % _t['slug'])
    _t['js'] = (_js + wire(_t['form'])).replace(OVERFLOW_WAS, OVERFLOW_NOW)

# ---- the contract ------------------------------------------------------
_LIVE = {f[:-5] for f in os.listdir(HERE) if f.endswith('.html')}
_THIS = {t['slug'] for t in TOOLS17}
_EARLIER = _LIVE - _THIS
assert len(_EARLIER) >= 106, (
    'expected at least the 106 tools of batches 1 to 16, found %d'
    % len(_EARLIER))
PUBLISHED = _THIS <= _LIVE

_PLAN = io.open(os.path.join(HERE, '..', '..', 'docs',
                             'corpnilfilingfor300-seo-website-plan.md'),
                encoding='utf-8').read()
for t in TOOLS17:
    assert '\n/%s/\n' % t['slug'] in _PLAN, (
        '%s is not an Appendix A URL' % t['slug'])

for t in TOOLS17:
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

assert len({t['seo_title'] for t in TOOLS17}) == len(TOOLS17), 'title clash'
assert len({t['seo_desc'] for t in TOOLS17}) == len(TOOLS17), 'desc clash'
assert len({t['keyword'] for t in TOOLS17}) == len(TOOLS17), 'keyword clash'
assert len({t['h1'] for t in TOOLS17}) == len(TOOLS17), 'h1 clash'


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = TODAY, ISO
    build_f2.PRICE = PRICE
    recs = []
    for t in TOOLS17:
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
    json.dump(recs, io.open(os.path.join(HERE, 'f2q-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-52s %6d bytes' % (r['slug'], len(r['content'].encode())))
