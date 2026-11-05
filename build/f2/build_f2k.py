#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 2 batch 11: tools 81 to 85.

WHAT I DROPPED BEFORE BUILDING, AND WHY

Navneet asked for five. I shortlisted eight and cut three, because line 1212
exists to stop the same page appearing at a second URL and three of the eight
would have done exactly that:

  gifi-schedule-100-checker        the five triggers it would ask are already
                                   gifi-schedule-requirement-checker's five,
                                   and what Schedule 100 carries is already
                                   nil-gifi-balance-sheet-checker and
                                   balance-sheet-balancing-checker
  quebec-co17-requirement-checker  the question "does a province collect its
  alberta-at1-requirement-checker  own tax from this corporation" is
                                   provincial-return-requirement-checker,
                                   restricted to one province

A FOURTH WAS DROPPED FOR A DIFFERENT REASON

signing-link-expiry-calculator would have rested on how long a T183CORP
signing link lasts, and THE PLAN STATES THAT TWO WAYS:

  line 387  "Your signing link is single-use and expires in 72 hours."
  line 1182 "The link is single use and expires in 24 hours."

The live /pricing/ page says 72 hours. A tool whose whole output is a
deadline cannot be built on a figure the signed-off plan gives twice with
different numbers, so it is not here. Logged for Sharad Gondaliya.

THE SOURCE FOR EACH TOOL BUILT

  "We keep your signed Form T183CORP for six years. It is not sent to the
   Canada Revenue Agency unless the Canada Revenue Agency asks for it."
   (plan line 390)                                              -> tool 81
  "Your CRA confirmation is emailed within 3 business days", business days
   being Monday to Friday excluding Ontario statutory holidays   -> tool 82
  "What the fee does not include": the Ontario annual return, the
   Corporations Canada annual return, Alberta AT1, Quebec CO-17, nil GST/HST
   and payroll filings (live /pricing/, plan 177 and hard rule 8)
                                                                 -> tool 83
  The seven-step process at plan line 107, and the 3-business-day
   confirmation                                                  -> tool 84
  "Each tax year is a separate return at the same fee", and one Form
   T183CORP signed per tax year before transmission              -> tool 85

Tool 82 is not business-days-between-dates-calculator: that one counts the
business days between two dates a visitor supplies, and this one applies the
service's own three-business-day promise forward from a transmission date.
Different input, different question, different answer.

STRUCTURE is the batch 10 contract, unchanged and asserted here too.
"""
import io, json, os
import re as _re

from build_f2 import (render, meta, yn, a, SITE, HUB, FORM, PRICE,
                      DATE_JS)
from build_f2b import tool, num, date, PICK, T, G, COST
from build_f2c import MONEY_JS, PRELUDE
from build_f2f import BASE, RBASE

HERE = os.path.dirname(os.path.abspath(__file__))


def _tbl(head, rows):
    """A static reference table, in the markup every other batch uses."""
    return ('<table class="ei-tbl"><thead><tr>'
            + ''.join('<th scope="col">%s</th>' % h for h in head)
            + '</tr></thead><tbody>\n'
            + '\n'.join('<tr>' + ''.join('<td>%s</td>' % c for c in r)
                        + '</tr>' for r in rows)
            + '\n</tbody></table>')


# --------------------------------------------------- 81. T183CORP retention
T81_JS = RBASE + r"""
function show(){
  var d=parse('tx'),h,i,y,end;
  if(d===null){out.innerHTML='<p>Enter the date the return was transmitted.</p>';return;}
  if(d===undefined){out.innerHTML='<p>That is not a date we can read.</p>';return;}
  end=addYear(d,6);
  h='<h3>Held until '+fmt(end)+'</h3>';
  h+='<p>The signed Form T183CORP for a return transmitted on '+fmt(d)
   +' is kept for six years, so it is on file until '+fmt(end)+'.</p>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">From</th>'
   +'<th scope="col">Until</th><th scope="col">State of the signed form</th>'
   +'</tr></thead><tbody>';
  for(i=0;i<6;i++){
    y=addYear(d,i);
    h+='<tr><td>'+fmt(y)+'</td><td>'+fmt(addYear(d,i+1))+'</td>'
     +'<td>Held, year '+(i+1)+' of six</td></tr>';
  }
  h+='<tr><td>'+fmt(end)+'</td><td>After</td>'
   +'<td>The six-year period has run</td></tr>';
  h+='</tbody></table>';
  h+='<p>The form is not sent to the Canada Revenue Agency unless the Canada '
   +'Revenue Agency asks for it. Holding it is what lets us produce it if '
   +'they do.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var out=document.getElementById('out');
"""

T81 = dict(
 slug='t183corp-retention-expiry-calculator',
 title='T183CORP Retention Calculator | Six Years, Dated',
 h1_pre='T183CORP Retention ', h1_span='Calculator',
 h1='T183CORP Retention Calculator',
 eyebrow='Signing',
 keyword='t183corp retention period',
 seo_title='T183CORP Retention Calculator',
 seo_desc=('A signed Form T183CORP is kept for six years. Enter the '
           'transmission date and the calculator dates the end of that '
           'period, year by year.'),
 meta=('A signed Form T183CORP is kept for six years. Enter the '
       'transmission date to date the end of that period.'),
 tags=['Six-year retention', 'Dated year by year',
       'Not sent to the Agency', 'One date in'],
 form=tool('When the return was transmitted',
           [date('tx', 'Date the return was transmitted')],
           'Enter the transmission date above.'),
 js=None,
 sections=[
  ('why-six-years', 'Why the Signed Form Is Kept at All',
   '<p>Form T183CORP is the authorisation to transmit. It carries the '
   'figures on the return, the date and an HH:MM:SS timestamp, and it is '
   'signed by an authorized signing officer before anything is sent. Keeping '
   'it is what makes that authorisation provable afterwards.</p>\n'
   '<p>It is not filed with the return. The Canada Revenue Agency does not '
   'receive it unless it asks for it, which is the reason the firm holds it '
   'rather than the Agency.</p>'),
  ('what-is-kept', 'What Is Kept and for How Long',
   _tbl(['What', 'How long', 'Who receives it'],
        [['The signed Form T183CORP', 'Six years from transmission',
          'Nobody, unless the Canada Revenue Agency asks'],
         ['The transmitted return itself', 'Held by the Canada Revenue '
          'Agency on the corporation&rsquo;s account', 'The Agency'],
         ['Your CRA confirmation', 'Emailed to you within 3 business days',
          'You'],
         ['The date and HH:MM:SS timestamp on the signature',
          'On the signed form, for the same six years',
          'Nobody, unless the Canada Revenue Agency asks']])
   + '\n<p>The '
   + a(T + 't183corp-signature-requirement-checker/',
       'T183CORP signature requirement checker')
   + ' takes the separate question of who may sign it.</p>'),
  ('one-per-year', 'One Signed Form for Each Tax Year',
   '<p>Each tax year is its own return, so each carries its own Form '
   'T183CORP with its own date and timestamp. Six quiet years filed together '
   'produce six signed forms, each with its own six-year period running from '
   'the day that year was transmitted.</p>\n'
   '<p>They do not expire together. A run filed in one sitting still has six '
   'separate retention end dates, because the period runs from transmission '
   'rather than from the tax year.</p>'),
 ],
 faq=[
  ('How long do you keep my signed T183CORP?',
   'Six years from the day the return was transmitted. The calculator above '
   'dates the end of that period from the transmission date.'),
  ('Is Form T183CORP sent to the Canada Revenue Agency?',
   'No. It is not sent unless the Canada Revenue Agency asks for it. It '
   'authorises the transmission rather than forming part of it.'),
  ('Do several years share one retention period?',
   'No. Each tax year has its own signed form, and each six-year period runs '
   'from the day that year was transmitted.'),
 ],
 related=[
  (T + 't183corp-signature-requirement-checker/',
   'T183CORP signature requirement checker'),
  (T + 'nil-t2-document-checklist-checker/', 'Nil T2 document checklist'),
  (T + 'efile-rejection-reason-checker/', 'E-filing rejection reason checker'),
  (G + 't183corp-signing-and-transmission/',
   'The complete guide to T183CORP signing and transmission'),
  (G + 'nil-t2-return-complete-guide/', 'The complete guide to the nil T2 return'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ------------------------------------------------- 82. confirmation due date
T82_JS = RBASE + r"""
function show(){
  var d=parse('tx'),h,i,n,cur,days=[];
  if(d===null){out.innerHTML='<p>Enter the date the return was transmitted.</p>';return;}
  if(d===undefined){out.innerHTML='<p>That is not a date we can read.</p>';return;}
  cur=new Date(d.getTime());n=0;
  while(n<3){
    cur=new Date(cur.getTime()+86400000);
    if(isBusiness(cur)){n++;days.push(new Date(cur.getTime()));}
  }
  h='<h3>Expected by '+fmt(days[2])+'</h3>';
  h+='<p>A return transmitted on '+fmt(d)+' ('+DAY[d.getUTCDay()]
   +') has its CRA confirmation emailed within 3 business days, so by '
   +fmt(days[2])+'.</p>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Business day</th>'
   +'<th scope="col">Date</th><th scope="col">Weekday</th></tr></thead><tbody>';
  for(i=0;i<3;i++){
    h+='<tr><td>'+(i+1)+' of 3</td><td>'+fmt(days[i])+'</td><td>'
     +DAY[days[i].getUTCDay()]+'</td></tr>';
  }
  h+='</tbody></table>';
  if(!isBusiness(d)){
    h+='<p>'+fmt(d)+' is not itself a business day, so the count starts from '
     +'the next one.</p>';
  }
  h+='<p>Business days are Monday to Friday and exclude Ontario statutory '
   +'holidays, so a long weekend pushes the date out rather than shortening '
   +'it.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var out=document.getElementById('out');
"""

T82 = dict(
 slug='cra-confirmation-due-date-calculator',
 title='CRA Confirmation Due Date | 3 Business Days, Dated',
 h1_pre='CRA Confirmation ', h1_span='Due Date Calculator',
 h1='CRA Confirmation Due Date Calculator',
 eyebrow='Transmission',
 keyword='cra confirmation 3 business days',
 seo_title='CRA Confirmation Due Date Calculator',
 seo_desc=('Your CRA confirmation is emailed within 3 business days. Enter '
           'the transmission date and the calculator dates it, Ontario '
           'statutory holidays excluded.'),
 meta=('Your CRA confirmation is emailed within 3 business days. Enter the '
       'transmission date to see which three days those are.'),
 tags=['3 business days', 'Ontario holidays excluded',
       'Names each day', 'One date in'],
 form=tool('When the return was transmitted',
           [date('tx', 'Date the return was transmitted')],
           'Enter the transmission date above.'),
 js=None,
 sections=[
  ('what-the-confirmation-is', 'What the Confirmation Actually Is',
   '<p>The confirmation is the Canada Revenue Agency&rsquo;s acknowledgement '
   'that the transmitted return was received. It is what turns a year from '
   'unfiled into filed, and it is emailed to you rather than left somewhere '
   'to be found.</p>\n'
   '<p>Until it arrives the year is still open. That is the reason the date '
   'is worth knowing rather than waiting on: three business days from '
   'transmission is the window, and a long weekend moves it.</p>'),
  ('what-counts', 'What Counts as a Business Day',
   _tbl(['Day', 'Counts', 'Why'],
        [['Monday to Friday', 'Yes', 'An ordinary business day'],
         ['Saturday and Sunday', 'No', 'Not business days'],
         ['An Ontario statutory holiday', 'No',
          'Excluded even when it falls on a weekday'],
         ['The transmission day itself', 'No',
          'The count starts the day after transmission']])
   + '\n<p>Ontario&rsquo;s nine Employment Standards Act public holidays are '
   'the ones excluded. The '
   + a(T + 'business-days-between-dates-calculator/',
       'business days between dates calculator')
   + ' counts them between any two dates you choose.</p>'),
  ('if-it-does-not-arrive', 'If the Confirmation Does Not Arrive',
   '<p>A transmission that is refused produces no confirmation, because the '
   'return was never received. That is a rejection rather than a delay, and '
   'it leaves the tax year exactly as open as it was before.</p>\n'
   '<p>Where that happens we read the rejection message, correct the return '
   'and transmit it again. One corrected transmission is included in the '
   'fee.</p>'),
 ],
 faq=[
  ('How long does the CRA confirmation take?',
   'It is emailed within 3 business days of transmission. The calculator '
   'above names which three days those are for your date.'),
  ('Do weekends and holidays count?',
   'No. Business days are Monday to Friday and exclude Ontario statutory '
   'holidays, so a long weekend pushes the date out.'),
  ('What if no confirmation arrives at all?',
   'That usually means the transmission was refused rather than delayed. A '
   'refused return was never received, so the year stays unfiled until a '
   'transmission is accepted.'),
 ],
 related=[
  (T + 'business-days-between-dates-calculator/',
   'Business days between dates calculator'),
  (T + 'efile-rejection-reason-checker/', 'E-filing rejection reason checker'),
  (T + 'due-date-weekend-holiday-shift-calculator/',
   'Due date weekend and holiday shift calculator'),
  (G + 't183corp-signing-and-transmission/',
   'The complete guide to T183CORP signing and transmission'),
  (G + 't2-filing-deadlines/', 'The complete guide to T2 filing deadlines'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ------------------------------------------------------ 83. what the fee covers
T83_JS = RBASE + r"""
/* Each row names the filing, whether the nil T2 fee covers it, and what it
   is instead. The "covered" column is a fixed property of the filing, not
   something derived from the answers, so no row can be rewritten by a
   later edit into claiming cover the fee does not give. */
var ITEM=[
 ['ont','The Ontario annual return',false,
  'A registry filing through the Ontario Business Registry. It carries no '
  +'tax and no payment, and filing the T2 does not satisfy it.'],
 ['fed','A Corporations Canada annual return',false,
  'A registry filing for a federal corporation, at the fee that registry '
  +'sets, due on its own date rather than the T2 deadline.'],
 ['at1','An Alberta AT1',false,
  'Alberta collects its own corporate tax, so AT1 is a separate provincial '
  +'return and is not part of the federal T2.'],
 ['co17','A Quebec CO-17',false,
  'Quebec collects its own corporate tax, so CO-17 is a separate provincial '
  +'return and is not part of the federal T2.'],
 ['gst','A nil GST/HST return',false,
  'An open GST/HST account needs its own nil filing. The T2 does not close '
  +'it and does not file it.'],
 ['pay','A nil payroll remittance',false,
  'An open payroll account has its own remittance obligation, separate from '
  +'the corporate return.']
];
function show(){
  var need=[],wait=0,i,v,h;
  for(i=0;i<ITEM.length;i++){
    v=pick(ITEM[i][0]);
    if(v===null){wait++;continue;}
    if(v==='y'){need.push(ITEM[i]);}
  }
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the six questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  h='<h3>Inside the fee: the nil T2 return for each tax year</h3>';
  h+='<p>Nil T2 filing is '+PRICE_JS+'. That covers the T2 itself for one '
   +'corporation for one tax year, with the schedules the return requires, '
   +'CPA review, Form T183CORP and electronic transmission.</p>';
  if(need.length===0){
    h+='<p>You answered no to all six, so nothing on this list is '
     +'outstanding alongside the return. Where one of them turns out to '
     +'apply later, it is still a separate filing.</p>';
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  h+='<h3>'+need.length+' filing'+(need.length===1?'':'s')
   +' outside the fee</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Filing</th>'
   +'<th scope="col">Inside the nil T2 fee</th>'
   +'<th scope="col">What it is</th></tr></thead><tbody>';
  for(i=0;i<need.length;i++){
    h+='<tr><td>'+need[i][1]+'</td><td>No</td><td>'+need[i][3]+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>We tell you which of these you still owe. None of them is filed by '
   +'filing the T2, and none of them is charged inside '+PRICE_JS+'.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var out=document.getElementById('out');
"""

T83 = dict(
 slug='what-the-nil-t2-fee-covers-checker',
 title='What the Nil T2 Fee Covers | Inside It and Outside It',
 h1_pre='What the Nil T2 Fee ', h1_span='Covers',
 h1='What the Nil T2 Fee Covers',
 eyebrow='Scope',
 keyword='what nil t2 filing covers',
 seo_title='What the Nil T2 Fee Covers | Checker',
 seo_desc=('The nil T2 fee covers the corporate return. Six answers name '
           'which of the registry, provincial and account filings sit '
           'outside it.'),
 meta=('The fee covers the corporate return. Six answers name which other '
       'filings sit outside it and what each one is.'),
 tags=['Six answers', 'Names what is separate',
       'Registry and provincial filings', 'One price per tax year'],
 form=tool('Which of these might apply',
           [yn('ont', 'Is the corporation on the Ontario Business Registry?'),
            yn('fed', 'Is it a federal corporation with Corporations Canada?'),
            yn('at1', 'Does it have a permanent establishment in Alberta?'),
            yn('co17', 'Does it have a permanent establishment in Quebec?'),
            yn('gst', 'Does it have an open GST/HST account?'),
            yn('pay', 'Does it have an open payroll account?')],
           'Answer the six questions above.'),
 js=None,
 sections=[
  ('one-price-one-return', 'One Price, One Return, One Tax Year',
   '<p>The fee buys the corporate income tax return for one corporation for '
   'one tax year: the T2 itself, the GIFI schedules the return requires, '
   'Schedule 50 and Schedule 24 where they apply, CPA review, Form T183CORP '
   'and electronic transmission by a registered EFILE electronic filer.</p>\n'
   '<p>What it does not buy is anything filed with a registry or a province, '
   'or any account the corporation holds besides its corporate tax account. '
   'Those are separate filings on separate dates, and filing the T2 does not '
   'satisfy any of them.</p>'),
  ('inside-and-outside', 'Inside the Fee and Outside It',
   _tbl(['Filing', 'Inside the fee', 'Filed with'],
        [['The T2 corporate return for the tax year', 'Yes',
          'The Canada Revenue Agency'],
         ['GIFI Schedules 100, 125 and 141 where required', 'Yes',
          'Attached to the T2'],
         ['Form T183CORP and the transmission', 'Yes',
          'Signed by you, transmitted by us'],
         ['The Ontario annual return', 'No',
          'The Ontario Business Registry'],
         ['A Corporations Canada annual return', 'No', 'Corporations Canada'],
         ['Alberta AT1 and Quebec CO-17', 'No',
          'The province, which collects its own corporate tax'],
         ['Nil GST/HST and payroll filings', 'No',
          'The Canada Revenue Agency, on their own accounts']])
   + '\n<p>The '
   + a(T + 'provincial-return-requirement-checker/',
       'provincial return requirement checker')
   + ' takes the question of which provinces are involved at all.</p>'),
  ('if-not-nil', 'A Year That Is Not Nil Is Not Covered Either',
   '<p>This fee is for a tax year with no activity. A holding corporation '
   'with investment income, a rental corporation and a corporation that paid '
   'or received a dividend are not nil, and those years are not covered.</p>\n'
   '<p>Where a year turns out not to be nil we say so before anything '
   'further is charged, and the file moves to Gondaliya CPA Professional '
   'Corporation at gondaliyacpa.ca. Nothing is taken at the higher price '
   'without you agreeing to it first.</p>'),
 ],
 faq=[
  ('Does the fee cover my annual return?',
   'No. The Ontario annual return and the Corporations Canada annual return '
   'are registry filings, not tax returns, and filing the T2 does not '
   'satisfy either.'),
  ('Does it cover Alberta AT1 or Quebec CO-17?',
   'No. Alberta and Quebec each collect their own corporate tax, so AT1 and '
   'CO-17 are separate provincial returns and are not part of the federal '
   'T2.'),
  ('What about GST/HST and payroll?',
   'Both are separate accounts with their own filings. An open account still '
   'needs its nil filing even in a year the corporation did nothing.'),
 ],
 related=[
  (T + 'provincial-return-requirement-checker/',
   'Provincial return requirement checker'),
  (T + 'annual-return-vs-tax-return-checker/',
   'Annual return versus tax return checker'),
  (T + 'gst-hst-nil-filing-checker/', 'GST/HST nil filing checker'),
  (T + 't4-nil-filing-requirement-checker/', 'T4 nil filing requirement checker'),
  (G + 'provincial-and-federal-annual-returns/',
   'The complete guide to provincial and federal annual returns'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ------------------------------------------------------- 84. progress tracker
T84_JS = RBASE + r"""
var STEP=[
 ['paid','Payment received',
  'We prepare the return in TaxCycle and generate your Form T183CORP.'],
 ['link','Signing link received',
  'Open the single-use link and check the figures on the form before you '
  +'sign. The link reopens only after you re-enter the corporation name and '
  +'Business Number.'],
 ['signed','Form T183CORP signed',
  'We transmit the return electronically as a registered EFILE electronic '
  +'filer. Nothing is transmitted before the form is signed.'],
 ['conf','CRA confirmation received',
  'The tax year is filed. Keep the confirmation; we keep the signed form for '
  +'six years.']
];
function show(){
  var done=0,wait=0,i,v,h;
  for(i=0;i<STEP.length;i++){
    v=pick(STEP[i][0]);
    if(v===null){wait++;continue;}
    if(v==='y'){done=i+1;}
  }
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the four questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  if(done===STEP.length){
    h='<h3>The year is filed</h3>';
    h+='<p>Confirmation received, so the return was accepted and that tax '
     +'year is closed. Each further tax year is its own return at '
     +PRICE_JS+'.</p>';
  }else{
    h='<h3>Next: '+STEP[done][1].toLowerCase()+'</h3>';
    h+='<p>'+STEP[done][2]+'</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Step</th>'
   +'<th scope="col">State</th><th scope="col">What happens there</th>'
   +'</tr></thead><tbody>';
  for(i=0;i<STEP.length;i++){
    h+='<tr><td>'+STEP[i][1]+'</td><td>'
     +(i<done?'Done':(i===done?'Next':'To come'))+'</td><td>'
     +STEP[i][2]+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>Your CRA confirmation is emailed within 3 business days of '
   +'transmission.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var out=document.getElementById('out');
"""

T84 = dict(
 slug='nil-t2-filing-progress-checker',
 title='Nil T2 Filing Progress Checker | What Happens Next',
 h1_pre='Nil T2 Filing ', h1_span='Progress Checker',
 h1='Nil T2 Filing Progress Checker',
 eyebrow='Process',
 keyword='nil t2 filing what happens next',
 seo_title='Nil T2 Filing Progress Checker',
 seo_desc=('Four answers place your return in the filing sequence and name '
           'what happens next, from payment through to the CRA '
           'confirmation.'),
 meta=('Four answers place your return in the sequence and name what '
       'happens next, from payment to the CRA confirmation.'),
 tags=['Four answers', 'Names the next step',
       'Confirmation in 3 business days', 'Signed before transmission'],
 form=tool('Where the return has got to',
           [yn('paid', 'Has the payment gone through?'),
            yn('link', 'Have you received the T183CORP signing link?'),
            yn('signed', 'Have you signed Form T183CORP?'),
            yn('conf', 'Has your CRA confirmation arrived?')],
           'Answer the four questions above.'),
 js=None,
 sections=[
  ('the-order', 'The Order Is Fixed',
   '<p>The steps do not run in parallel and none of them is skipped. Payment '
   'comes first, the return is prepared from what you entered, Form T183CORP '
   'is generated from the prepared figures, you sign it, and only then is '
   'the return transmitted.</p>\n'
   '<p>That order is what makes the signature mean something. The form '
   'carries the figures on your own return, with the date and an HH:MM:SS '
   'timestamp, and it is never backdated.</p>'),
  ('each-step', 'What Each Step Produces',
   _tbl(['Step', 'What you do', 'What we do'],
        [['Payment', 'Enter the corporation name and the unfiled years, and '
          'pay', 'Start preparing the return'],
         ['Preparation', 'Nothing', 'Prepare the T2 and generate Form '
          'T183CORP from its figures'],
         ['Signing', 'Open the single-use link and sign as the authorized '
          'signing officer', 'Hold the signed form for six years'],
         ['Transmission', 'Nothing',
          'Transmit electronically as a registered EFILE electronic filer'],
         ['Confirmation', 'Keep the email',
          'Email your CRA confirmation within 3 business days']])
   + '\n<p>The '
   + a(T + 'cra-confirmation-due-date-calculator/',
       'CRA confirmation due date calculator')
   + ' dates the last step from the day the return was transmitted.</p>'),
  ('several-years', 'Several Years Run the Same Way',
   '<p>Each tax year is a separate return, so a run of unfiled years goes '
   'through this sequence once per year: one Form T183CORP to sign for each, '
   'one transmission for each, one confirmation for each.</p>\n'
   '<p>They can be prepared together, and the fee is '
   '$300.00 plus HST per tax year however many go at once.</p>'),
 ],
 faq=[
  ('What happens after I pay?',
   'We prepare the return and generate your Form T183CORP, then send you a '
   'single-use signing link by email.'),
  ('Can the return be transmitted before I sign?',
   'No. Form T183CORP is signed by an authorized signing officer before '
   'anything is transmitted, and it is never backdated.'),
  ('How long until the year is actually filed?',
   'The year is filed once the transmission is accepted, and your CRA '
   'confirmation is emailed within 3 business days of transmission.'),
 ],
 related=[
  (T + 'cra-confirmation-due-date-calculator/',
   'CRA confirmation due date calculator'),
  (T + 't183corp-signature-requirement-checker/',
   'T183CORP signature requirement checker'),
  (T + 'nil-t2-document-checklist-checker/', 'Nil T2 document checklist'),
  (T + 't183corp-retention-expiry-calculator/',
   'T183CORP retention calculator'),
  (G + 't183corp-signing-and-transmission/',
   'The complete guide to T183CORP signing and transmission'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ------------------------------------------------ 85. one signed form per year
T85_JS = RBASE + MONEY_JS + r"""
function show(){
  var n=document.getElementById('yrs').value,h,i,k;
  if(n===''){out.innerHTML='<p>Enter how many tax years are being filed.</p>';return;}
  k=parseInt(n,10);
  if(isNaN(k)||k<1||k>20){
    out.innerHTML='<p>Enter a whole number of tax years from 1 to 20.</p>';return;
  }
  h='<h3>'+k+' return'+(k===1?'':'s')+', '+k+' signed form'
   +(k===1?'':'s')+', '+k+' confirmation'+(k===1?'':'s')+'</h3>';
  h+='<p>Each tax year is a separate return, so filing '+k+' year'
   +(k===1?'':'s')+' produces '+k+' of each. They can be prepared in one '
   +'sitting, and each still carries its own signature and its own '
   +'confirmation.</p>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Per tax year</th>'
   +'<th scope="col">How many for '+k+' year'+(k===1?'':'s')+'</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>T2 returns prepared</td><td>'+k+'</td></tr>';
  h+='<tr><td>Forms T183CORP to sign</td><td>'+k+'</td></tr>';
  h+='<tr><td>Transmissions</td><td>'+k+'</td></tr>';
  h+='<tr><td>CRA confirmations emailed</td><td>'+k+'</td></tr>';
  h+='<tr><td>Fee</td><td>'+PRICE_JS+', counted per year</td></tr>';
  h+='</tbody></table>';
  h+='<p>Each signed form is held for six years from the day that year was '
   +'transmitted, so '+k+' form'+(k===1?'':'s')+' filed together still '
   +(k===1?'has its own date':'have their own dates')+'.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var out=document.getElementById('out');
"""

T85 = dict(
 slug='multi-year-signing-requirement-checker',
 title='Multi-Year Signing Requirement | One Form Per Year',
 h1_pre='Multi-Year Signing ', h1_span='Requirement Checker',
 h1='Multi-Year Signing Requirement Checker',
 eyebrow='Signing',
 keyword='how many t183corp forms to sign',
 seo_title='Multi-Year Signing Requirement Checker',
 seo_desc=('Each tax year is its own return with its own Form T183CORP. '
           'Enter the number of years to see how many signatures and '
           'confirmations that is.'),
 meta=('Each tax year is its own return with its own Form T183CORP. Enter '
       'the number of years to see what that produces.'),
 tags=['One form per year', 'One confirmation per year',
       'Prepared in one sitting', 'Fee counted per year'],
 form=tool('How many tax years',
           [num('yrs', 'Tax years being filed', 'A whole number from 1 to 20',
                1, 20, '6')],
           'Enter how many tax years are being filed.'),
 js=None,
 sections=[
  ('why-one-each', 'Why Each Year Needs Its Own Signature',
   '<p>Form T183CORP authorises the transmission of one return. It carries '
   'the figures on that return, so a form signed for one tax year cannot '
   'authorise another: the figures on it would be the wrong ones.</p>\n'
   '<p>That is why a run of six quiet years is six signatures rather than '
   'one. The work is prepared together, and the authorisations stay '
   'separate.</p>'),
  ('what-a-run-produces', 'What a Run of Years Produces',
   _tbl(['Per tax year', 'One each', 'Why'],
        [['A T2 return', 'Yes', 'Each tax year is a separate return'],
         ['A Form T183CORP', 'Yes',
          'It carries that year&rsquo;s own figures'],
         ['A transmission', 'Yes', 'One return goes per transmission'],
         ['A CRA confirmation', 'Yes',
          'Each accepted return is acknowledged on its own'],
         ['A six-year retention period', 'Yes',
          'It runs from the day that year was transmitted'],
         ['The fee', 'Yes', 'Counted per tax year, not per sitting']])
   + '\n<p>The '
   + a(T + 'unfiled-years-cost-calculator/', 'unfiled years cost calculator')
   + ' prices a run at the fee per year.</p>'),
  ('order-matters', 'The Years Are Filed Oldest First',
   '<p>A run is filed from the oldest year forward, so that opening '
   'balances and loss continuity carry correctly from one year into the '
   'next. A schedule cannot follow a year that is missing.</p>\n'
   '<p>The signing follows the same order, which is why the forms arrive as '
   'a sequence rather than all at once.</p>'),
 ],
 faq=[
  ('Do I sign once for all my years?',
   'No. One Form T183CORP is signed for each tax year, because each form '
   'carries that year&rsquo;s own figures.'),
  ('Do I get one confirmation or several?',
   'One for each accepted return. Six years filed together produce six '
   'confirmations.'),
  ('Does filing several years at once change the fee?',
   'No. The fee is $300.00 plus HST per tax year, counted per year however '
   'many are filed together.'),
 ],
 related=[
  (T + 'unfiled-years-cost-calculator/', 'Unfiled years cost calculator'),
  (T + 'catch-up-filing-schedule-generator/',
   'Catch-up filing schedule generator'),
  (T + 't183corp-signature-requirement-checker/',
   'T183CORP signature requirement checker'),
  (T + 't183corp-retention-expiry-calculator/',
   'T183CORP retention calculator'),
  (G + 'catch-up-unfiled-corporate-tax-returns/',
   'The complete guide to catch-up filing'),
  (COST, 'Nil T2 filing cost'),
 ],
)

TOOLS11 = [T81, T82, T83, T84, T85]

STRUCTURE = dict(sections=3, faq=3, related=6, tags=4,
                 body_tables=1, result_tables=1)


def wire(form):
    """The listener block, derived from the form's own controls.

    Same as batches 9 and 10: a hand-typed selector list drifts from the form
    it binds, and a control nobody wired does nothing at all.
    """
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


for _t, _js in zip(TOOLS11, [T81_JS, T82_JS, T83_JS, T84_JS, T85_JS]):
    _js = _js + wire(_t['form'])
    _t['js'] = _js if _js.startswith(PRELUDE) else PRELUDE + _js

# ---- the contract, asserted rather than trusted ---------------------------
_LIVE = {f[:-5] for f in os.listdir(HERE) if f.endswith('.html')}
_THIS = {t['slug'] for t in TOOLS11}
# A subset test, not an exact count: the next batch adds files to this
# directory and an "== 80" here breaks every earlier builder the moment it
# does. Batch 12 broke this one on 2026-11-05, as batch 11 broke build_f2j's.
_EARLIER = _LIVE - _THIS
assert len(_EARLIER) >= 80, (
    'expected at least the 80 tools of batches 1 to 10, found %d'
    % len(_EARLIER))
PUBLISHED = _THIS <= _LIVE

for t in TOOLS11:
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
    for fid in set(_re.findall(r"parse\('([\w-]+)'\)", t['js'])
                   + _re.findall(r"getElementById\('([\w-]+)'\)", t['js'])):
        if fid != 'out':
            assert fid in fields, '%s: js reads field %s the form lacks' % (s, fid)

    # every internal link points at something that exists
    for u in _re.findall(r'href="' + SITE + r'/tools/([a-z0-9-]+)/"',
                         t['form'] + ''.join(h for _i, _h2, h in t['sections'])
                         + ''.join(q + aa for q, aa in t['faq'])
                         + ''.join(u2 for u2, _x in t['related'])):
        assert u in _LIVE or u in _THIS, '%s: links to missing tool %s' % (s, u)

assert len({t['seo_title'] for t in TOOLS11}) == len(TOOLS11), 'title clash'
assert len({t['seo_desc'] for t in TOOLS11}) == len(TOOLS11), 'desc clash'


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'November 4, 2026', '2026-11-04'
    recs = []
    for t in TOOLS11:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2k-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-44s %6d bytes' % (r['slug'], len(r['content'].encode())))
