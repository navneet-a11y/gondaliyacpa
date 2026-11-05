#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 2 batch 13: tools 91 to 95, the schedules that end a nil year.

WHY THESE FIVE

All five are Appendix A URLs and they sit contiguously in it, entries 44 to 49
of the Family 2 list:

  /schedule-3-dividends-paid-checker/
  /schedule-7-investment-income-calculator/
  /schedule-9-related-corporations-checker/
  /schedule-23-association-agreement-checker/
  /schedule-88-internet-activities-checker/

They are picked by subject, not by order. On 2026-11-05 the Appendix A list was
scored against the ninety tools already built: 37 of the 95 unbuilt entries are
near-duplicates of a live page under another name, /t2-filing-deadline-
calculator/ against the live nil-t2-deadline-calculator and /penalty-on-zero-
balance-owing-checker/ against the live nil-return-late-penalty-checker among
them. These five scored 0.17 to 0.20 against their nearest live page, which is
to say the subject is genuinely uncovered: the site has GIFI 100, 125 and 141,
Schedule 50, Schedule 24, Schedule 8 and Schedule 546, and nothing else.

THE ONE I DROPPED, AND WHY IT IS A QUESTION FOR SHARAD GONDALIYA

/schedule-1-net-income-reconciliation-calculator/ was in this batch and came
out of it. /guides/t2-schedules-on-a-nil-return/ answers "which schedules a nil
return needs" with a closed list -- GIFI 100, 125 and 141, Schedule 50,
Schedule 24, Schedule 8 -- and says every schedule on it is in the price.
Schedule 1 is not on that list. A tool asserting that a nil return also carries
Schedule 1 would contradict the guide, and the guide is the published position.
Either the guide's list is incomplete or Schedule 1 belongs outside it, and
that is an editorial ruling, not something a tool page should settle on its own.
Logged in docs/decisions.md as an open item.

WHAT HOLDS THIS BATCH TOGETHER

Each of the five answers the same shape of question -- does this schedule reach
my year -- and four of the five answer it in a way that also answers whether
the year is nil at all:

  Schedule 3   a dividend paid or received ends the nil year outright
  Schedule 7   investment income ends it outright
  Schedule 9   reaches a dormant corporation and does NOT end the nil year
  Schedule 23  needs active business income to allocate, so a nil year has none
  Schedule 88  needs income earned from a site, so a parked domain is outside it

Schedule 9 is the deliberate odd one. Without it the batch would read as "every
schedule means you are not nil", which is false, and the site already has the
sentence that sets it up: "Schedule 50 is not the schedule that reports related
or associated corporations."

AGREEING WITH WHAT IS ALREADY PUBLISHED

From /guides/t2-schedules-on-a-nil-return/:

  "Not the amount of income, which is $0.00 on every nil return. What the
   corporation holds, who owns it, and whether this is its first return."

From the live tool pages and Family 1:

  "Interest credited on a balance is investment income, and the corporation is
   not nil for that tax year."
  "A dividend declared is activity whether or not it was paid in cash, and net
   income is activity by definition."

Both are hard rule 8 in the plan's own words, and Schedules 3 and 7 are where
that rule meets a particular schedule. Every page that reaches it carries
NOT_NIL whole.

WHAT NO TOOL HERE DOES

None of them prepares a schedule or files anything, and none of them states a
rate, a threshold or a dollar figure the site does not already publish. The
only money any of them shows is a total the visitor typed in themselves.
"""
import io, json, os
import re as _re

from build_f2 import (render, meta, yn, a, SITE, HUB, FORM, PRICE, NOT_NIL,
                      DATE_JS)
from build_f2b import tool, num, date, PICK, T, G, COST
from build_f2c import MONEY_JS, PRELUDE
from build_f2f import BASE, RBASE

HERE = os.path.dirname(os.path.abspath(__file__))

SCHEDULES_GUIDE = G + 't2-schedules-on-a-nil-return/'
HOLDING_GUIDE = G + 'inactive-holding-company-filing/'
NIL_GUIDE = G + 'nil-t2-return-complete-guide/'


def _tbl(head, rows):
    """A static reference table, in the markup every other batch uses."""
    return ('<table class="ei-tbl"><thead><tr>'
            + ''.join('<th scope="col">%s</th>' % h for h in head)
            + '</tr></thead><tbody>\n'
            + '\n'.join('<tr>' + ''.join('<td>%s</td>' % c for c in r)
                        + '</tr>' for r in rows)
            + '\n</tbody></table>')


# Each page closes on the same idea -- a schedule applying is not the same
# thing as the year being disqualified -- in its own words. A shared sentence
# was written first and gate_f2_all.py refused it, correctly: five pages
# ending identically is the templated-content defect that gate exists to
# catch. Keyed by slug so the per-page assert below can check each one landed.
CLOSE = {
 'schedule-3-dividends-paid-checker':
   'A schedule applying is not always a verdict on the whole year. This one '
   'is, because what puts a year on it is a dividend.',
 'schedule-7-investment-income-calculator':
   'Not every schedule settles whether a year is nil. This one does, and it '
   'settles it on any amount above zero.',
 'schedule-9-related-corporations-checker':
   'So this is the schedule that shows the rule is not uniform: it applies '
   'to the year and the year stays nil.',
 'schedule-23-association-agreement-checker':
   'Sitting inside a group and sitting outside this schedule are both true '
   'at once, and for a dormant corporation that is the ordinary position.',
 'schedule-88-internet-activities-checker':
   'Having a site is not a verdict on the year. What came through it is.',
}

# ------------------------------------------------- 91. Schedule 3, dividends
T91_JS = RBASE + r"""
/* The third column is a fixed property of the question, not something derived
   from the answer, so no later edit can turn a dividend into a nil year. */
var DIV=[
 ['paid','A taxable dividend paid to a shareholder',
  'Schedule 3 reports taxable dividends paid in the year.'],
 ['recd','A dividend received from another corporation',
  'Schedule 3 reports dividends received, and it is where Part IV tax on a '
  +'dividend from a connected corporation is worked out.'],
 ['decl','A dividend declared and left unpaid',
  'A declared dividend is activity whether or not any cash moved.']
];
var out=document.getElementById('out');
function show(){
  var i,v,wait=0,hit=[],miss=[],h;
  for(i=0;i<DIV.length;i++){
    v=pick(DIV[i][0]);
    if(v===null){wait++;continue;}
    (v==='y'?hit:miss).push(DIV[i]);
  }
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  if(hit.length===0){
    h='<h3>Nothing here puts the year on Schedule 3</h3>';
    h+='<p>No dividend was paid, received or declared, so Schedule 3 has '
     +'nothing to report and the year is not disqualified by this question. '
     +'What the corporation holds and who owns it decide the rest.</p>';
  }else{
    h='<h3>'+hit.length+' of three put the year on Schedule 3</h3>';
    h+='<p>A dividend moved, so the year is not a nil year and nil T2 filing '
     +'at '+PRICE_JS+' does not cover it.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">What was asked</th>'
   +'<th scope="col">Your answer</th><th scope="col">What it means</th>'
   +'</tr></thead><tbody>';
  for(i=0;i<DIV.length;i++){
    v=pick(DIV[i][0]);
    h+='<tr><td>'+DIV[i][1]+'</td><td>'+(v==='y'?'Yes':'No')+'</td><td>'
     +(v==='y'?DIV[i][2]:'Nothing to report on this line.')+'</td></tr>';
  }
  h+='</tbody></table>';
  if(hit.length>0){h+='<p>'+NOTNILJS+'</p>';}
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T91 = dict(
 slug='schedule-3-dividends-paid-checker',
 title='Schedule 3 Dividends Paid Checker | Did a Dividend Move',
 h1_pre='Schedule 3 ', h1_span='Dividends Paid Checker',
 h1='Schedule 3 Dividends Paid Checker',
 eyebrow='Schedules',
 keyword='schedule 3 dividends paid',
 seo_title='Schedule 3 Dividends Paid Checker',
 seo_desc=('A dividend paid, received or declared puts the year on '
           'Schedule 3. Three answers show which applies and what it means '
           'for a nil year.'),
 meta=('Schedule 3 reports dividends paid and dividends received. A dividend '
       'either way means the year is not nil.'),
 tags=['Three answers', 'Dividends only', 'Declared still counts',
       'Ends the nil year'],
 form=tool('Dividends in the tax year',
           [yn('paid', 'Did the corporation pay a taxable dividend?'),
            yn('recd', 'Did it receive a dividend from another corporation?'),
            yn('decl', 'Was a dividend declared but left unpaid?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('what-schedule-3-reports', 'What Schedule 3 Reports',
   '<p>Schedule 3 is where dividends go. Taxable dividends the corporation '
   'paid out during the year sit on one side of it, dividends it received '
   'from another corporation on the other, and it is where Part IV tax on a '
   'dividend from a connected corporation is worked out.</p>\n'
   '<p>It is not a GIFI schedule, so nothing on the balance sheet brings it '
   'into play. The only question is whether a dividend moved. The '
   + a(SCHEDULES_GUIDE, 'guide to T2 schedules on a nil return')
   + ' sets out the schedules that are decided the other way, by what the '
   'corporation holds rather than by what it did.</p>'),
  ('three-triggers', 'The Three Things That Put a Year on It',
   _tbl(['What happened', 'Where it lands', 'Is the year still nil'],
        [['A taxable dividend paid to a shareholder',
          'Taxable dividends paid, on Schedule 3', 'No'],
         ['A dividend received from another corporation',
          'Dividends received, on Schedule 3', 'No'],
         ['A dividend declared and left unpaid',
          'Still a dividend, and still reported', 'No'],
         ['No dividend of any kind',
          'Schedule 3 has nothing to report', 'Yes, on this question']])
   + '\n<p>The third row is the one owners get wrong. A declared dividend is '
   'activity whether or not any cash left the account, and the declaration '
   'is what counts rather than the payment.</p>'),
  ('what-it-means-for-the-fee', 'Why a Dividend Ends the Nil Year',
   '<p>' + NOT_NIL + '</p>\n'
   '<p>So this page has a short answer and a long one. The short answer is '
   'which part of Schedule 3 your year reaches. The long answer is that '
   'reaching any part of it settles a different question: the year is not '
   'nil, and ' + a(COST, 'nil T2 filing at ' + PRICE)
   + ' is for years that are. A '
   + a(HOLDING_GUIDE, 'holding corporation that pays or receives dividends')
   + ' is the ordinary case.</p>\n'
   '<p>' + CLOSE['schedule-3-dividends-paid-checker'] + '</p>'),
 ],
 faq=[
  ('Does a dividend paid in cash differ from one declared?',
   'Not for this purpose. A declared dividend is reported whether or not the '
   'cash has moved, so declaring one in a year the account never changed '
   'still puts the year on Schedule 3.'),
  ('My corporation received a dividend and did nothing else. Is the year nil?',
   'No. A dividend received is income, so the year is not nil however quiet '
   'the rest of it was.'),
  ('Is Schedule 3 part of nil T2 filing?',
   'The schedule is not the issue. A year that reaches Schedule 3 is not a '
   'nil year, and nil T2 filing at $300.00 plus HST per tax year is for '
   'years that are.'),
  ('What is Part IV tax doing on this schedule?',
   'Part IV tax can arise on a dividend received from a connected '
   'corporation, and Schedule 3 is where that calculation sits. It is '
   'another reason the schedule is not a formality.'),
  ('Does a dividend between my own two corporations count?',
   'Yes, on both returns. One paid it and one received it, so each of them '
   'reports its own side of the same dividend.'),
  ('Is a shareholder loan repayment a dividend?',
   'No. A loan repayment moves money that was already owed. Whether it is '
   'reported elsewhere is a separate question from this one.'),
  ('Does a return of capital go on Schedule 3?',
   'A return of capital is not a taxable dividend. If that is what happened, '
   'the question to settle first is what was actually resolved and recorded.'),
  ('I paid myself a salary, not a dividend.',
   'Then Schedule 3 has nothing to report on that account. A salary is '
   'payroll rather than a dividend, and it carries its own filings.'),
  ('The dividend was in a year I have not filed yet.',
   'It belongs to the year it was declared in, and that year is not nil. '
   'Each year stands on its own facts.'),
  ('Nothing happened at all. Do I still file a schedule?',
   'Not this one. Schedule 3 is driven by a dividend, and with none there is '
   'nothing for it to report. What the corporation holds still decides the '
   'GIFI schedules.'),
 ],
 related=[
  (T + 'schedule-50-shareholder-threshold-checker/',
   'Schedule 50 shareholder threshold checker'),
  (T + 'required-schedules-checker/', 'Required schedules checker'),
  (T + 'nil-return-vs-full-return-checker/',
   'Nil return versus full return checker'),
  (T + 'gifi-schedule-requirement-checker/',
   'GIFI schedule requirement checker'),
  (SCHEDULES_GUIDE, 'The complete guide to T2 schedules on a nil return'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ---------------------------------------------- 92. Schedule 7, investment income
T92_JS = RBASE + MONEY_JS + r"""
function cents(id){
  var v=document.getElementById(id).value;
  if(v===''){return null;}
  var n=parseInt(v,10);
  if(isNaN(n)){return undefined;}
  if(n<0||n>9999999){return 'range';}
  return n*100;
}
var out=document.getElementById('out');
function show(){
  var ids=[['int','Interest credited on a balance'],
           ['rent','Rent received'],
           ['oth','Other investment income']];
  var i,c,vals=[],total=0,bad=false,blank=0;
  for(i=0;i<ids.length;i++){
    c=cents(ids[i][0]);
    if(c===null){blank++;vals.push(null);continue;}
    if(c===undefined||c==='range'){bad=true;vals.push(c);continue;}
    vals.push(c);total+=c;
  }
  if(bad){
    out.innerHTML='<p class="ei-err">Enter whole dollars, 0 or more.</p>';
    return;
  }
  if(blank===ids.length){
    out.innerHTML='<p>Enter the amounts above. Enter 0 where there was '
     +'none.</p>';return;
  }
  var h='';
  if(total===0){
    h+='<h3>No investment income for the year</h3>';
    h+='<p>Every amount you entered is 0, so there is nothing for Schedule 7 '
     +'to total and the year is not disqualified by this question.</p>';
  }else{
    h+='<h3>'+money(total)+' of investment income</h3>';
    h+='<p>That is income, so the year is not a nil year and nil T2 filing '
     +'at '+PRICE_JS+' does not cover it. The figure is the one you typed '
     +'in, totalled.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Source</th>'
   +'<th scope="col">Amount</th><th scope="col">Is the year still nil</th>'
   +'</tr></thead><tbody>';
  for(i=0;i<ids.length;i++){
    h+='<tr><td>'+ids[i][1]+'</td><td>'
     +(vals[i]===null?'Not entered':money(vals[i]))+'</td><td>'
     +(vals[i]===null?'Unanswered':(vals[i]>0?'No':'Yes, on this line'))
     +'</td></tr>';
  }
  h+='<tr><td>Total</td><td>'+money(total)+'</td><td>'
   +(total>0?'No':'Yes, on these figures')+'</td></tr>';
  h+='</tbody></table>';
  if(blank>0){
    h+='<p>'+blank+' of the three '+(blank===1?'line is':'lines are')
     +' still blank, so the total is only as complete as what you entered.</p>';
  }
  if(total>0){h+='<p>'+NOTNILJS+'</p>';}
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T92 = dict(
 slug='schedule-7-investment-income-calculator',
 title='Schedule 7 Investment Income Calculator | What Totals Up',
 h1_pre='Schedule 7 ', h1_span='Investment Income Calculator',
 h1='Schedule 7 Investment Income Calculator',
 eyebrow='Schedules',
 keyword='schedule 7 investment income',
 seo_title='Schedule 7 Investment Income Calculator',
 seo_desc=('Interest, rent and other investment income total up on '
           'Schedule 7. Enter the amounts to see the total and what it means '
           'for a nil year.'),
 meta=('Schedule 7 is where a private corporation totals its investment '
       'income. Any amount above nil means the year is not nil.'),
 tags=['Three amounts in', 'Totals what you enter', 'Interest counts',
       'Ends the nil year'],
 form=tool('Investment income in the tax year',
           [num('int', 'Interest credited on a balance', 'whole dollars',
                0, 9999999, '12'),
            num('rent', 'Rent received', 'whole dollars', 0, 9999999, '0'),
            num('oth', 'Other investment income', 'whole dollars',
                0, 9999999, '0')],
           'Enter the amounts above. Enter 0 where there was none.'),
 js=None,
 sections=[
  ('what-schedule-7-does', 'What Schedule 7 Does',
   '<p>Schedule 7 is where a private corporation totals its investment '
   'income: interest, rent, and the other passive amounts that arrive '
   'without anybody trading. It is the schedule that separates money the '
   'corporation earned from money it worked for.</p>\n'
   '<p>For a dormant corporation it matters out of all proportion to the '
   'amounts involved, because the amounts are usually tiny and the '
   'consequence is not. Interest of a few dollars credited on a bank balance '
   'is investment income, and the year stops being nil.</p>'),
  ('what-counts', 'What Totals Up, and What It Costs the Year',
   _tbl(['Source', 'Counts as investment income', 'Effect on a nil year'],
        [['Interest credited on a bank balance', 'Yes',
          'The year is not nil, whatever the amount'],
         ['Rent received on a property', 'Yes',
          'A rental corporation is not nil'],
         ['Other passive income', 'Yes', 'The year is not nil'],
         ['Nothing credited at all', 'No',
          'Nil on this question; what the corporation holds decides the '
          'GIFI schedules']])
   + '\n<p>There is no small-amount exception on this list. A balance that '
   'earned $12.00 across the year earned investment income, and that is the '
   'whole of the test.</p>'),
  ('why-it-ends-the-year', 'Why Any Amount Ends the Nil Year',
   '<p>' + NOT_NIL + '</p>\n'
   '<p>The calculator above adds up what you type and nothing else. It '
   'holds no rate, no threshold and no figure of ours: every amount in the '
   'result is one you entered. What it does is apply the test to the total, '
   'so a year with $12.00 of interest gets the same answer as a year with '
   '$12,000.00. See '
   + a(COST, 'what nil T2 filing at ' + PRICE + ' covers')
   + ' and the '
   + a(HOLDING_GUIDE, 'guide to filing for an inactive holding company')
   + '.</p>\n'
   '<p>' + CLOSE['schedule-7-investment-income-calculator'] + '</p>'),
 ],
 faq=[
  ('Is a few dollars of bank interest really enough?',
   'Yes. Interest credited on a balance is investment income, and the '
   'corporation is not nil for that tax year. The amount changes nothing '
   'about the test.'),
  ('Where does the calculator get its figures?',
   'From you. It totals the three amounts you enter and applies the test to '
   'the total. It holds no rate and no threshold of its own.'),
  ('My bank paid interest but I never withdrew it.',
   'Credited is enough. The income arose when it was credited to the '
   'account, whether or not anybody moved it afterwards.'),
  ('Is rent from one property enough to end the nil year?',
   'Yes. A rental corporation is not nil, and one property is a rental '
   'corporation for this purpose.'),
  ('What if the interest was credited in a year I have not filed?',
   'It belongs to that year, and that year is not nil. Each tax year is '
   'tested on its own facts.'),
  ('Does a capital gain go here?',
   'A gain is not the same thing as the interest and rent this page asks '
   'about. Either way a year with a gain in it is not a nil year.'),
  ('My corporation holds shares that paid nothing.',
   'Then nothing was credited and there is nothing to total. Holding an '
   'investment is not the same as earning from it.'),
  ('Does this tell me what tax is owed?',
   'No. It totals investment income and says what that means for the nil '
   'question. It works out no tax and is not a filed return.'),
  ('The amounts are in a foreign currency.',
   'Enter the figures you will report, in the currency the return uses. The '
   'conversion is a question for whoever prepares the return.'),
  ('Everything is 0. What now?',
   'Then this question leaves the year nil, and what the corporation holds '
   'decides the GIFI schedules instead. Share capital, cash, a shareholder '
   'loan, an incorporation cost or a bank charge each make them required.'),
 ],
 related=[
  (T + 'nil-return-eligibility-checker/', 'Nil return eligibility checker'),
  (T + 'holding-corporation-nil-checker/', 'Holding corporation nil checker'),
  (T + 'gifi-schedule-125-checker/', 'GIFI Schedule 125 checker'),
  (T + 'required-schedules-checker/', 'Required schedules checker'),
  (HOLDING_GUIDE, 'The guide to filing for an inactive holding company'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ------------------------------------------- 93. Schedule 9, related corporations
T93_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var rel=pick('rel'),asc=pick('asc'),act=pick('act'),wait=0,h;
  if(rel===null){wait++;}
  if(asc===null){wait++;}
  if(act===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  var owed=(rel==='y'||asc==='y');
  if(!owed){
    h='<h3>Schedule 9 has nothing to report</h3>';
    h+='<p>The corporation stands on its own: not related to another '
     +'corporation and not associated with one. Schedule 9 reports a '
     +'relationship, and there is none to report.</p>';
  }else{
    h='<h3>Schedule 9 reaches this corporation</h3>';
    h+='<p>A relationship exists, so it is reported, and being dormant does '
     +'not remove it. This is the part owners are most often surprised by: '
     +'the schedule reports who the corporation is connected to, not what it '
     +'did.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Your answer</th><th scope="col">What follows</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Related to another corporation</td><td>'
   +(rel==='y'?'Yes':'No')+'</td><td>'
   +(rel==='y'?'Reported on Schedule 9':'Nothing on this line')+'</td></tr>';
  h+='<tr><td>Associated with another corporation</td><td>'
   +(asc==='y'?'Yes':'No')+'</td><td>'
   +(asc==='y'?'Reported on Schedule 9':'Nothing on this line')+'</td></tr>';
  h+='<tr><td>Any activity in the year</td><td>'
   +(act==='y'?'Yes':'No')+'</td><td>'
   +(act==='y'?'A year with activity is not a nil year'
             :'Does not change whether Schedule 9 applies')+'</td></tr>';
  h+='</tbody></table>';
  if(owed&&act==='n'){
    h+='<p>So both answers hold at once: the relationship is reported and '
     +'the year can still be nil. Schedule 9 is not a disqualification, '
     +'which is what separates it from Schedule 3 and Schedule 7. Nil T2 '
     +'filing at '+PRICE_JS+' covers a year like this.</p>';
  }
  if(act==='y'){h+='<p>'+NOTNILJS+'</p>';}
  h+='<p>Schedule 50 is not the schedule that reports related or associated '
   +'corporations. It reports shareholders at 10% or more, which is a '
   +'different question with a different answer.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T93 = dict(
 slug='schedule-9-related-corporations-checker',
 title='Schedule 9 Related Corporations Checker | Not Schedule 50',
 h1_pre='Schedule 9 ', h1_span='Related Corporations Checker',
 h1='Schedule 9 Related Corporations Checker',
 eyebrow='Schedules',
 keyword='schedule 9 related corporations',
 seo_title='Schedule 9 Related Corporations Checker',
 seo_desc=('Schedule 9 reports related and associated corporations, and '
           'Schedule 50 does not. Three answers show whether your '
           'corporation owes one.'),
 meta=('Schedule 9 reports related and associated corporations. It reaches a '
       'dormant corporation and does not end a nil year.'),
 tags=['Three answers', 'Relationships, not income', 'Reaches a dormant year',
       'Still a nil year'],
 form=tool('Corporate relationships',
           [yn('rel', 'Is the corporation related to another corporation?'),
            yn('asc', 'Is it associated with another corporation?'),
            yn('act', 'Was there any activity in the year?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('what-it-reports', 'What Schedule 9 Reports, and What Schedule 50 Does Not',
   '<p>Schedule 9 reports the corporations yours is related to or associated '
   'with. It is a map of the group, and it is filed because the group exists '
   'rather than because anything happened in it.</p>\n'
   '<p>It is routinely confused with Schedule 50, and the confusion runs one '
   'way: an owner who has filed Schedule 50 assumes the relationships are '
   'covered. They are not. Schedule 50 is not the schedule that reports '
   'related or associated corporations. It lists '
   + a(T + 'schedule-50-shareholder-threshold-checker/',
       'shareholders at 10% or more')
   + ', which is a question about who owns this corporation rather than '
   'about which corporations stand beside it.</p>'),
  ('two-questions', 'Two Questions That Look Like One',
   _tbl(['Schedule', 'What it reports', 'Decided by'],
        [['Schedule 9', 'Related and associated corporations',
          'Whether a corporate relationship exists'],
         ['Schedule 50', 'Shareholders at 10% or more',
          'Who holds the shares of this corporation'],
         ['Schedule 24', 'Shareholders and related corporations, once',
          'Whether this is the first return after incorporation'],
         ['Schedule 3', 'Dividends paid and received',
          'Whether a dividend moved in the year']])
   + '\n<p>A single shareholder who owns two corporations outright triggers '
   'all of the first two: each corporation reports the other on its '
   'Schedule 9, and each reports that shareholder on its Schedule 50.</p>'),
  ('a-dormant-year-still-reports', 'A Dormant Year Still Reports It',
   '<p>This is the page in the set that does not end a nil year. A '
   'relationship is reported whether or not either corporation traded, so a '
   'dormant corporation sitting in a group files the schedule and stays '
   'nil. Nil T2 filing at ' + a(COST, PRICE) + ' covers a year like that.</p>\n'
   '<p>The reason is the same one the '
   + a(SCHEDULES_GUIDE, 'guide to T2 schedules on a nil return')
   + ' gives for the rest of them: what decides a schedule is not the amount '
   'of income, which is $0.00 on every nil return, but what the corporation '
   'holds, who owns it, and whether this is its first return. A relationship '
   'is in the same family of facts.</p>\n'
   '<p>' + CLOSE['schedule-9-related-corporations-checker'] + '</p>'),
 ],
 faq=[
  ('Is Schedule 9 the same as Schedule 50?',
   'No, and this is the most common mix-up on a nil return. Schedule 50 '
   'lists shareholders at 10% or more. Schedule 9 reports the corporations '
   'yours is related to or associated with.'),
  ('My corporation did nothing. Does it still report the relationship?',
   'Yes. The relationship exists whether or not either corporation traded, '
   'and the schedule reports its existence.'),
  ('Does filing Schedule 9 mean the year is not nil?',
   'No. This is the one schedule in this set that leaves a nil year nil. It '
   'reports a connection, not income.'),
  ('I own two corporations personally. Are they related?',
   'Common ownership is exactly the kind of fact these questions turn on. '
   'Where the answer is yes, each corporation reports the other.'),
  ('What is the difference between related and associated?',
   'They are two separate tests, which is why the schedule and this page ask '
   'them separately. A corporation can meet one and not the other.'),
  ('One of the two corporations is dissolved.',
   'Then the question is what was true during the tax year being filed. A '
   'relationship that existed in that year is reported on that year.'),
  ('Is this the same as Schedule 24?',
   'No. Schedule 24 is filed once, on the first return after incorporation, '
   'and reports how the corporation came into existence. Schedule 9 is not '
   'a one-off.'),
  ('Does a shareholder loan between the two change this?',
   'It is a separate matter. A balance owed either way is reported where '
   'balances are reported; the relationship is reported here.'),
  ('My corporations are in different provinces.',
   'The relationship is still a relationship. Where each corporation is '
   'registered affects its registry filings, not this schedule.'),
  ('Nothing is related or associated. Do I file a blank one?',
   'There is nothing for it to report, so the question falls away. What the '
   'corporation holds still decides the GIFI schedules.'),
 ],
 related=[
  (T + 'schedule-50-shareholder-threshold-checker/',
   'Schedule 50 shareholder threshold checker'),
  (T + 'schedule-24-first-return-checker/', 'Schedule 24 first return checker'),
  (T + 'multiple-corporation-filing-cost-calculator/',
   'Multiple corporation filing cost calculator'),
  (T + 'required-schedules-checker/', 'Required schedules checker'),
  (SCHEDULES_GUIDE, 'The complete guide to T2 schedules on a nil return'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ---------------------------------------- 94. Schedule 23, association agreement
T94_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var asc=pick('asc'),act=pick('act'),sbd=pick('sbd'),wait=0,h;
  if(asc===null){wait++;}
  if(act===null){wait++;}
  if(sbd===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  var reach=(asc==='y'&&act==='y'&&sbd==='y');
  if(reach){
    h='<h3>There is a business limit to allocate</h3>';
    h+='<p>Associated corporations with active business income claiming the '
     +'small business deduction have one business limit between them, and an '
     +'agreement allocating it is what Schedule 23 carries. That is a '
     +'question for the corporation with the income.</p>';
  }else if(asc==='n'){
    h='<h3>Nothing to allocate: no associated corporation</h3>';
    h+='<p>Schedule 23 allocates a limit between associated corporations. '
     +'With none, there is no limit to share and nothing to agree.</p>';
  }else{
    h='<h3>Nothing to allocate for this corporation</h3>';
    h+='<p>The corporations are associated, but this one has no active '
     +'business income to claim the deduction against, so there is no share '
     +'of the limit for it to take.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Your answer</th><th scope="col">What follows</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Associated with another corporation</td><td>'
   +(asc==='y'?'Yes':'No')+'</td><td>'
   +(asc==='y'?'A limit is shared, in principle'
             :'No limit is shared, so Schedule 23 does not arise')
   +'</td></tr>';
  h+='<tr><td>Active business income this year</td><td>'
   +(act==='y'?'Yes':'No')+'</td><td>'
   +(act==='y'?'There is income to claim against, so the year is not nil'
             :'Nothing to claim against, and the year can still be nil')
   +'</td></tr>';
  h+='<tr><td>Claiming the small business deduction</td><td>'
   +(sbd==='y'?'Yes':'No')+'</td><td>'
   +(sbd==='y'?'The limit matters, so its allocation matters'
             :'The limit is not in issue for this corporation')
   +'</td></tr>';
  h+='</tbody></table>';
  if(act==='y'){
    h+='<p>'+NOTNILJS+'</p>';
  }else{
    h+='<p>A nil year reaches none of this. There is no active business '
     +'income, so there is no deduction to claim and no share of a limit to '
     +'agree. Nil T2 filing at '+PRICE_JS+' covers a year like that, and '
     +'being associated does not change it.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T94 = dict(
 slug='schedule-23-association-agreement-checker',
 title='Schedule 23 Association Agreement Checker | Who Allocates',
 h1_pre='Schedule 23 ', h1_span='Association Agreement Checker',
 h1='Schedule 23 Association Agreement Checker',
 eyebrow='Schedules',
 keyword='schedule 23 association agreement',
 seo_title='Schedule 23 Association Agreement Checker',
 seo_desc=('Associated corporations claiming the small business deduction '
           'share one business limit. Three answers show whether yours has '
           'any of it to allocate.'),
 meta=('Schedule 23 allocates the business limit between associated '
       'corporations. A nil year has no active business income to claim.'),
 tags=['Three answers', 'Associated groups', 'Needs active income',
       'A nil year is outside it'],
 form=tool('The group and the year',
           [yn('asc', 'Is the corporation associated with another?'),
            yn('act', 'Did it have active business income this year?'),
            yn('sbd', 'Is it claiming the small business deduction?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('what-it-allocates', 'What Schedule 23 Allocates',
   '<p>Associated corporations do not each get their own business limit for '
   'the small business deduction. They share one between them, and '
   'Schedule 23 is the agreement that says who takes what share of it.</p>\n'
   '<p>Which means the schedule has two conditions before it means anything, '
   'and a dormant corporation fails the second. There has to be a group, and '
   'there has to be active business income to claim the deduction against. '
   'A nil year has none.</p>'),
  ('who-it-reaches', 'Who It Reaches, and Who It Does Not',
   _tbl(['The corporation', 'Associated', 'Active business income',
          'Schedule 23 in issue'],
        [['An operating corporation in a group', 'Yes', 'Yes', 'Yes'],
         ['A dormant corporation in the same group', 'Yes', 'No', 'No'],
         ['A corporation that stands alone', 'No', 'Yes', 'No'],
         ['A dormant corporation standing alone', 'No', 'No', 'No']])
   + '\n<p>The second row is the one that brings owners here. Being '
   'associated feels like it must create a filing, and on this schedule it '
   'does not: the allocation belongs to whichever corporation in the group '
   'has income to claim against.</p>'),
  ('a-nil-year-is-outside-it', 'Why a Nil Year Sits Outside It',
   '<p>A nil year has no active business income, so there is no small '
   'business deduction to claim, so there is no share of a limit to agree. '
   'The chain breaks at the first link and nothing downstream of it '
   'applies.</p>\n'
   '<p>Being associated still matters elsewhere, and the mistake to avoid is '
   'reading this page as saying it does not. The relationship itself is '
   'reported on '
   + a(T + 'schedule-9-related-corporations-checker/', 'Schedule 9')
   + ', which does reach a dormant corporation. What the dormant corporation '
   'is outside is the allocation, not the group. Nil T2 filing at '
   + a(COST, PRICE) + ' covers the dormant years either way.</p>\n'
   '<p>' + CLOSE['schedule-23-association-agreement-checker'] + '</p>'),
 ],
 faq=[
  ('My corporations are associated. Do I file Schedule 23?',
   'Only where there is a business limit to allocate, which needs active '
   'business income and a small business deduction claim. A dormant '
   'corporation has neither.'),
  ('Does being associated stop the year being nil?',
   'No. Association is a relationship, and a relationship is not income. '
   'The year is tested on what the corporation did.'),
  ('Which corporation files the agreement?',
   'The allocation belongs with the corporations that have income to claim '
   'against. A dormant member of the group has no share to take.'),
  ('What is the business limit?',
   'It is the amount of active business income the small business deduction '
   'can be claimed on, and associated corporations share one between them '
   'rather than each having their own.'),
  ('Is this the same as Schedule 9?',
   'No. Schedule 9 reports that the relationship exists. Schedule 23 divides '
   'a limit between corporations that have income to apply it to.'),
  ('My operating corporation claims the deduction and the holding company '
   'does not.',
   'Then the allocation is a question on the operating corporation. The '
   'dormant or holding side has nothing to allocate.'),
  ('Does a nil corporation reduce the limit for the others?',
   'A corporation with no active business income has no claim to make. What '
   'the group agrees is a matter for the corporations making claims.'),
  ('We never signed anything.',
   'Then what is actually agreed is the question to settle, and it is a '
   'question for whoever prepares the return of the corporation claiming '
   'the deduction.'),
  ('Does this page tell me the amount?',
   'No. It tells you whether the question reaches your corporation at all. '
   'It calculates no limit and is not a filed return.'),
  ('The corporation was dormant all year but associated. What do I file?',
   'Not this. The relationship goes on Schedule 9, and what the corporation '
   'holds decides the GIFI schedules. The allocation does not arise.'),
 ],
 related=[
  (T + 'schedule-9-related-corporations-checker/',
   'Schedule 9 related corporations checker'),
  (T + 'multiple-corporation-filing-cost-calculator/',
   'Multiple corporation filing cost calculator'),
  (T + 'nil-return-vs-full-return-checker/',
   'Nil return versus full return checker'),
  (T + 'required-schedules-checker/', 'Required schedules checker'),
  (NIL_GUIDE, 'The complete guide to the nil T2 return'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# -------------------------------------------- 95. Schedule 88, internet activities
T95_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var site=pick('site'),earn=pick('earn'),sell=pick('sell'),wait=0,h;
  if(site===null){wait++;}
  if(earn===null){wait++;}
  if(sell===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  var earns=(earn==='y'||sell==='y');
  if(site==='n'){
    h='<h3>No web page or site, so nothing to report</h3>';
    h+='<p>Schedule 88 reports income earned from web pages and websites. '
     +'With none, the schedule has nothing to describe.</p>';
  }else if(!earns){
    h='<h3>A site that earns nothing is outside Schedule 88</h3>';
    h+='<p>The corporation has a site, but no income came through it. The '
     +'schedule reports income earned from a site, so a parked domain or a '
     +'page that has sat untouched for years is not what it asks about.</p>';
  }else{
    h='<h3>Income came through the site</h3>';
    h+='<p>Income earned from a web page or website is what Schedule 88 '
     +'reports, and this year has some. It also means the year is not a nil '
     +'year: income is income, wherever it arrived from.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Your answer</th><th scope="col">What follows</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>A web page or website at all</td><td>'
   +(site==='y'?'Yes':'No')+'</td><td>'
   +(site==='y'?'The first condition is met'
              :'Schedule 88 does not arise')+'</td></tr>';
  h+='<tr><td>Income earned through it</td><td>'
   +(earn==='y'?'Yes':'No')+'</td><td>'
   +(earn==='y'?'Reported on Schedule 88, and the year is not nil'
              :'Nothing on this line')+'</td></tr>';
  h+='<tr><td>Goods or services sold online</td><td>'
   +(sell==='y'?'Yes':'No')+'</td><td>'
   +(sell==='y'?'Reported on Schedule 88, and the year is not nil'
              :'Nothing on this line')+'</td></tr>';
  h+='</tbody></table>';
  if(earns){
    h+='<p>'+NOTNILJS+'</p>';
  }else if(site==='y'){
    h+='<p>So a dormant corporation can keep a domain, keep a page up and '
     +'keep its year nil, because the schedule follows the income rather '
     +'than the hosting. Nil T2 filing at '+PRICE_JS+' covers a year like '
     +'that.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T95 = dict(
 slug='schedule-88-internet-activities-checker',
 title='Schedule 88 Internet Activities Checker | Parked or Earning',
 h1_pre='Schedule 88 ', h1_span='Internet Activities Checker',
 h1='Schedule 88 Internet Activities Checker',
 eyebrow='Schedules',
 keyword='schedule 88 internet business activities',
 seo_title='Schedule 88 Internet Activities Checker',
 seo_desc=('Schedule 88 reports income earned from web pages and websites. '
           'Three answers separate a parked domain from a site that is '
           'earning.'),
 meta=('Schedule 88 reports income earned from web pages and websites. A '
       'parked domain that earns nothing is outside it.'),
 tags=['Three answers', 'Income, not hosting', 'A parked domain is outside',
       'Earning ends the nil year'],
 form=tool('The corporation and its site',
           [yn('site', 'Does the corporation have a web page or website?'),
            yn('earn', 'Did it earn any income through it this year?'),
            yn('sell', 'Did it sell goods or services online?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('what-it-asks', 'What Schedule 88 Actually Asks',
   '<p>Schedule 88 reports income earned from web pages and websites. The '
   'operative word is earned: the schedule follows the income, not the '
   'hosting bill and not the domain registration.</p>\n'
   '<p>That distinction is the whole page, because a dormant corporation '
   'very often still has a site. The company that stopped trading in 2019 '
   'frequently still owns the domain, and the page is often still up. '
   'Neither fact is what this schedule asks about.</p>'),
  ('parked-or-earning', 'A Parked Domain and an Earning Site',
   _tbl(['What the corporation has', 'Income through it', 'Schedule 88',
          'Is the year still nil'],
        [['A domain registered and nothing else', 'None', 'No',
          'Yes, on this question'],
         ['A page still up from when it traded', 'None', 'No',
          'Yes, on this question'],
         ['A page taking orders', 'Yes', 'Yes', 'No'],
         ['A site earning from advertising or affiliates', 'Yes', 'Yes',
          'No']])
   + '\n<p>The middle rows are where a dormant corporation usually sits. A '
   'page that has not been touched in four years earns nothing, and a '
   'schedule about income earned has nothing to take from it.</p>'),
  ('when-it-ends-the-nil-year', 'When a Site Ends the Nil Year',
   '<p>Income earned online is income. A corporation that took a single '
   'order through a page it had forgotten about had revenue that year, and '
   'the year is not nil, however dormant everything else was.</p>\n'
   '<p>' + NOT_NIL + '</p>\n'
   '<p>Where nothing came through the site, nothing here disqualifies the '
   'year, and ' + a(COST, 'nil T2 filing at ' + PRICE)
   + ' covers it. What the corporation holds still decides the GIFI '
   'schedules, which the '
   + a(SCHEDULES_GUIDE, 'guide to T2 schedules on a nil return')
   + ' sets out in full.</p>\n'
   '<p>' + CLOSE['schedule-88-internet-activities-checker'] + '</p>'),
 ],
 faq=[
  ('My corporation owns a domain but the site is blank.',
   'Then nothing was earned through it and Schedule 88 has nothing to '
   'report. Owning a domain is not earning from one.'),
  ('The old site is still up from when we traded. Does that count?',
   'Not on its own. A page that earns nothing is outside a schedule about '
   'income earned from a page.'),
  ('We took one small order online.',
   'Then income arrived through the site, and the year is not nil. The size '
   'of the order does not change the test.'),
  ('Does advertising revenue on a site count?',
   'Income earned from a web page is what the schedule reports, whichever '
   'way the page earned it.'),
  ('I pay for hosting every month. Is that reportable here?',
   'A hosting cost is an expense, not income earned from the site. It '
   'belongs where expenses belong, and it does not bring this schedule into '
   'play.'),
  ('Does a social media page count as a website?',
   'The question the schedule asks is whether income was earned through a '
   'page. Where it was, the platform it sat on is not the deciding factor.'),
  ('How many sites do I have to report?',
   'The schedule asks about the pages that earned income. Pages that earned '
   'nothing are not what it is asking after.'),
  ('Our site only has a contact form.',
   'A form that generates no income earns nothing. If work came in through '
   'it and was paid for, that income is the point, not the form.'),
  ('Does this affect GST/HST?',
   'It is a separate account with separate filings. This page is about one '
   'schedule of the corporate return.'),
  ('Nothing came through the site. What decides the schedules then?',
   'What the corporation holds, who owns it, and whether this is its first '
   'return. Income is $0.00 on every nil return, so income is never what '
   'decides them.'),
 ],
 related=[
  (T + 'never-traded-corporation-checker/', 'Never traded corporation checker'),
  (T + 'dormant-corporation-test/', 'Dormant corporation test'),
  (T + 'required-schedules-checker/', 'Required schedules checker'),
  (T + 'expenses-only-year-checker/', 'Expenses only year checker'),
  (SCHEDULES_GUIDE, 'The complete guide to T2 schedules on a nil return'),
  (COST, 'Nil T2 filing cost'),
 ],
)

TOOLS13 = [T91, T92, T93, T94, T95]

STRUCTURE = dict(sections=3, faq=10, related=6, tags=4,
                 body_tables=1, result_tables=1)


def wire(form):
    """The listener block, derived from the form's own controls."""
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


for _t, _js in zip(TOOLS13, [T91_JS, T92_JS, T93_JS, T94_JS, T95_JS]):
    _js = _js + wire(_t['form'])
    _t['js'] = _js if _js.startswith(PRELUDE) else PRELUDE + _js

# ---- the contract, asserted rather than trusted ---------------------------
# A subset test, never an exact count: batches 10 and 11 each asserted an
# exact number and each broke when the next batch wrote files beside them.
_LIVE = {f[:-5] for f in os.listdir(HERE) if f.endswith('.html')}
_THIS = {t['slug'] for t in TOOLS13}
_EARLIER = _LIVE - _THIS
assert len(_EARLIER) >= 90, (
    'expected at least the 90 tools of batches 1 to 12, found %d'
    % len(_EARLIER))
PUBLISHED = _THIS <= _LIVE

# Every one of the five is an Appendix A URL. The plan is the contract, so the
# build checks itself against the plan rather than against my memory of it.
_PLAN = io.open(os.path.join(HERE, '..', '..', 'docs',
                             'corpnilfilingfor300-seo-website-plan.md'),
                encoding='utf-8').read()
for t in TOOLS13:
    assert '\n/%s/\n' % t['slug'] in _PLAN, (
        '%s is not an Appendix A URL' % t['slug'])

for t in TOOLS13:
    s = t['slug']
    if not PUBLISHED:
        assert s not in _LIVE, '%s already exists; pick another slug' % s
    assert len(t['sections']) == STRUCTURE['sections'], s
    assert len(t['faq']) == STRUCTURE['faq'], s
    assert len(t['related']) == STRUCTURE['related'], s
    assert len(t['tags']) == STRUCTURE['tags'], s
    assert sum('<table class="ei-tbl"' in h for _i, _h2, h in t['sections']) \
        >= STRUCTURE['body_tables'], '%s: no static table in the body' % s
    assert t['js'].count('<table class="ei-tbl"') >= STRUCTURE['result_tables'], \
        '%s: the result draws no table' % s
    assert len(t['seo_title']) <= 60, (s, len(t['seo_title']))
    assert 70 <= len(t['seo_desc']) <= 160, (s, len(t['seo_desc']))

    # Hard rule 8 lands on the three pages that can disqualify a year, and it
    # travels whole or not at all.
    _body = ''.join(h for _i, _h2, h in t['sections'])
    assert CLOSE[s] in _body, '%s: its closing sentence is missing' % s
    if s in ('schedule-3-dividends-paid-checker',
             'schedule-7-investment-income-calculator',
             'schedule-88-internet-activities-checker'):
        assert NOT_NIL in _body, '%s: rule 8 block missing or altered' % s

    # every control the form renders is read, and every control read exists
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
    for fid in set(_re.findall(r"getElementById\('([\w-]+)'\)", t['js'])):
        if fid != 'out':
            assert fid in fields, '%s: js reads field %s the form lacks' % (s, fid)

    _all = (t['form'] + _body
            + ''.join(q + aa for q, aa in t['faq'])
            + ''.join(u2 for u2, _x in t['related']) + t['js'])
    # every internal tool link points at something that exists
    for u in _re.findall(r'href="' + SITE + r'/tools/([a-z0-9-]+)/"', _all):
        assert u in _LIVE or u in _THIS, '%s: links to missing tool %s' % (s, u)
    # every guide link points at a guide that exists
    _F9 = {f[:-5] for f in os.listdir(os.path.join(HERE, '..', 'f9'))
           if f.endswith('.html')}
    for u in _re.findall(r'href="' + SITE + r'/guides/([a-z0-9-]+)/"', _all):
        assert u in _F9, '%s: links to missing guide %s' % (s, u)

assert len({t['seo_title'] for t in TOOLS13}) == len(TOOLS13), 'title clash'
assert len({t['seo_desc'] for t in TOOLS13}) == len(TOOLS13), 'desc clash'
assert len({t['keyword'] for t in TOOLS13}) == len(TOOLS13), 'keyword clash'
assert len({t['h1'] for t in TOOLS13}) == len(TOOLS13), 'h1 clash'

if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'November 5, 2026', '2026-11-05'
    recs = []
    for t in TOOLS13:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2m-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-46s %6d bytes' % (r['slug'], len(r['content'].encode())))
