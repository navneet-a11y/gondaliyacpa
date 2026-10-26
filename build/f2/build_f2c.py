# -*- coding: utf-8 -*-
"""Family 2, tools 11 to 15.

Structure, CSS, render(), schema and the wp:html wrapper all come from
build_f2, and the form helpers from build_f2b, so the three batches cannot
drift.

Selection. Appendix A order is followed, skipping the entries that duplicate a
tool already live under its 6(e) name. Appendix A items 2 and 3
(/t2-filing-deadline-calculator/, /catch-up-nil-filing-cost-calculator/) and
item 6 are already built as /nil-t2-deadline-calculator/,
/unfiled-years-cost-calculator/ and /t2-short-eligibility-checker/, so the next
five are Appendix A items 1, 4, 5, 7 and 8. Item 5
(/fiscal-year-end-calculator/) is the same tool as 6(e)'s corporate fiscal year
end calculator and is built at the 6(e) slug, which is the eleventh Appendix A
conflict and resolves the same way as the previous ten: the nil_calculator
rewrite base decides the URL.

That also finishes the buildable half of 6(e). The Ontario annual return due
date calculator is the one 6(e) tool still not built, for the reason recorded
in build_f2b: the plan nowhere states the Ontario annual return due date and
line 1212 reserves every jurisdiction claim for Sharad Gondaliya.

Arithmetic. The six-month due date and the 53-week limit are the two rules the
live tools already encode, so they are reused rather than restated:
dueDate() is asserted below to be character-identical to the copy inside
build_f2.T1_JS, and the 53-week limit uses the same "latest permitted year-end
is incorporation plus 370 days, maximum inclusive length 371 days" as
build_f2b.T6_JS. If either upstream copy is edited, this module refuses to
build.

Line 1210 gates publication on a working calculation and a result screen that
changes with input; Sharad Gondaliya checks the math on every tool. The pure
arithmetic of each tool is kept in its own LOGIC block, separate from the DOM
wiring, so test_f2c.js can call it directly.
"""
import io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_f2 import (render, meta, yn, a, DATE_JS, T1_JS, SITE, HUB, FORM,
                      PRICE, TODAY, ISO, NOT_NIL, TOOL_DISCLAIMER)
from build_f2b import tool, num, date, out_box, PICK, T, G, COST, ORDER, LINK_TITLE

# --------------------------------------------------------------------------
# Shared arithmetic, held identical to what is already live.
# --------------------------------------------------------------------------
DUE_JS = r"""function dueDate(ye){
  var y=ye.getUTCFullYear(),m=ye.getUTCMonth(),d=ye.getUTCDate();
  var endOfMonth=(d===lastDay(y,m));
  var tm=m+6,ty=y+Math.floor(tm/12);tm=((tm%12)+12)%12;
  if(endOfMonth){return u(ty,tm+1,0);}
  return u(ty,tm,Math.min(d,lastDay(ty,tm)));
}
"""
assert DUE_JS.strip() in T1_JS, (
    'dueDate() has diverged from build_f2.T1_JS; the deadline calculator and '
    'these tools would disagree about the same date.')

MONEY_JS = r"""function money(c){var s=(c/100).toFixed(2),p=s.split('.');
  return '$'+p[0].replace(/\B(?=(\d{3})+(?!\d))/g,',')+'.'+p[1];}
"""

PARSE_JS = r"""function parse(id){var v=document.getElementById(id).value;
  if(!v){return null;}var p=v.split('-');var d=u(+p[0],+p[1]-1,+p[2]);
  return isNaN(d.getTime())?undefined:d;}
"""

# --------------------------------------------- 11. corporate fiscal year end
L11 = r"""
// The first tax year may not exceed 53 weeks. build_f2b.T6_JS states that as a
// maximum inclusive length of 371 days, so the latest permitted year-end is
// the incorporation date plus 370 days. Restated here identically.
function latestFirstYE(inc){return new Date(inc.getTime()+370*86400000);}
function firstYearDays(inc,ye){
  return Math.round((ye.getTime()-inc.getTime())/86400000)+1;}
function monthEnds(inc){
  var out=[],latest=latestFirstYE(inc);
  var y=inc.getUTCFullYear(),m=inc.getUTCMonth();
  for(var i=0;i<15;i++){
    var me=u(y,m+i+1,0);
    if(me.getTime()<=inc.getTime()){continue;}
    if(me.getTime()>latest.getTime()){break;}
    out.push(me);
  }
  return out;
}
"""
T11_JS = DATE_JS + DUE_JS + L11 + PARSE_JS + r"""
var out=document.getElementById('out');
function render(){
  var inc=parse('inc');
  if(inc===null){out.className='ei-out';
    out.innerHTML='<p>Enter the incorporation date and the permitted year-ends appear here.</p>';
    return;}
  if(inc===undefined){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';return;}
  var latest=latestFirstYE(inc),ends=monthEnds(inc);
  if(!ends.length){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">No month-end falls between that date and 53 weeks after it.</p>';
    return;}
  var h='<h3>Permitted first year-ends from '+fmt(inc)+'</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">First tax year starts</span>'+
     '<span class="ei-stat-v">'+fmt(inc)+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Latest permitted year-end</span>'+
     '<span class="ei-stat-v">'+fmt(latest)+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Maximum first year</span>'+
     '<span class="ei-stat-v">371 days</span></div></div>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Year-end</th>'+
     '<th scope="col">First tax year</th><th scope="col">T2 due</th></tr></thead><tbody>';
  ends.forEach(function(me){
    var dys=firstYearDays(inc,me),due=dueDate(me),eff=nextBusiness(due);
    h+='<tr><td>'+fmt(me)+'</td><td>'+dys+' days</td><td>'+fmt(eff)+'</td></tr>';
  });
  h+='</tbody></table>';
  h+='<p>Every month-end above gives a first tax year within 53 weeks. The '+
     'choice is the corporation&rsquo;s, and it is made on the first return. '+
     'Once it is on record with the Canada Revenue Agency, every later year-end '+
     'follows it, and a transmission is rejected when the year-end sent does '+
     'not match the Agency&rsquo;s record.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out ok';out.innerHTML=h;
}
document.getElementById('inc').addEventListener('input',render);
render();
"""

# ------------------------------------------------- 12. nil T2 eligibility
L12 = r"""
function eligibility(a){
  // All four first, so the result screen never contradicts the prompt that
  // asks for all four. Then the gates in the order they actually decide.
  if(a.corp===null||a.ended===null||a.activity===null||a.filed===null){
    return 'incomplete';}
  if(a.corp==='n'){return 'notcorp';}
  if(a.ended==='n'){return 'notdue';}
  if(a.activity==='y'){return 'notnil';}
  if(a.filed==='y'){return 'alreadyfiled';}
  return 'eligible';
}
"""
T12_JS = PICK + L12 + r"""
var out=document.getElementById('out');
var IDS=['corp','ended','activity','filed'];
function render(){
  var a={};IDS.forEach(function(k){a[k]=pick(k);});
  var r=eligibility(a);
  if(r==='incomplete'){out.className='ei-out';
    out.innerHTML='<p>Answer all four and the result appears here.</p>';return;}
  var h='',cls='ei-out no';
  if(r==='eligible'){
    cls='ei-out ok';
    h='<h3>This is a nil T2 we can file</h3>'+
      '<p>A corporation that files a T2, a tax year that has ended, no activity '+
      'in that year and no return filed for it yet is exactly what this service '+
      'is for. The fee is '+PRICE_JS+'.</p>';
  }else if(r==='notcorp'){
    h='<h3>This service files corporate T2 returns only</h3>'+
      '<p>A sole proprietorship, a partnership and a trust do not file a T2, so '+
      'there is no nil T2 to file. '+NOTNILJS+'</p>';
  }else if(r==='notdue'){
    h='<h3>That tax year has not ended yet</h3>'+
      '<p>A T2 covers a tax year that has finished, and it is due within six '+
      'months of the year-end. Nothing can be filed for a year still running.</p>';
  }else if(r==='notnil'){
    h='<h3>That year is not nil</h3><p>'+NOTNILJS+'</p>';
  }else{
    h='<h3>That year is already filed</h3>'+
      '<p>A year already filed and assessed needs nothing further. If another '+
      'year is outstanding, check that year instead.</p>';
  }
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className=cls;out.innerHTML=h;
}
IDS.forEach(function(k){
  Array.prototype.forEach.call(document.querySelectorAll('input[name="'+k+'"]'),
    function(e){e.addEventListener('change',render);});});
render();
"""

# --------------------------------------------------- 13. unfiled years checker
L13 = r"""
function addYear(dt,k){
  var y=dt.getUTCFullYear(),m=dt.getUTCMonth(),d=dt.getUTCDate();
  if(d===lastDay(y,m)){return u(y+k,m+1,0);}
  return u(y+k,m,Math.min(d,lastDay(y+k,m)));
}
function yearEnds(first,upto){
  var out=[];
  for(var k=0;k<40;k++){
    var ye=addYear(first,k);
    if(ye.getTime()>upto.getTime()){break;}
    out.push(ye);
  }
  return out;
}
function outstandingYears(first,lastFiled,upto){
  return yearEnds(first,upto).filter(function(ye){
    return lastFiled===null||ye.getTime()>lastFiled.getTime();});
}
"""
T13_JS = DATE_JS + DUE_JS + MONEY_JS + L13 + PARSE_JS + r"""
var out=document.getElementById('out');
function render(){
  var first=parse('first'),last=parse('last'),t=today();
  if(first===null){out.className='ei-out';
    out.innerHTML='<p>Enter your first fiscal year-end and the outstanding years appear here.</p>';
    return;}
  if(first===undefined||last===undefined){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';return;}
  if(first.getTime()>t.getTime()){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That first year-end is in the future, so no year has fallen due yet.</p>';
    return;}
  if(last!==null&&last.getTime()<first.getTime()){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">The year already filed cannot fall before the first year-end.</p>';
    return;}
  var ys=outstandingYears(first,last,t);
  if(!ys.length){out.className='ei-out ok';
    out.innerHTML='<h3>No tax year is outstanding</h3>'+
      '<p>Every tax year that has ended is filed. The next return is due six '+
      'months after the next year-end.</p><p class="ei-note">'+DISC_JS+'</p>';
    return;}
  var h='<h3>'+ys.length+' tax year'+(ys.length===1?'':'s')+' outstanding</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">Years to file</span>'+
     '<span class="ei-stat-v">'+ys.length+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Oldest outstanding</span>'+
     '<span class="ei-stat-v">'+fmt(ys[0])+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Fee before tax</span>'+
     '<span class="ei-stat-v">'+money(ys.length*30000)+'</span></div></div>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Tax year ended</th>'+
     '<th scope="col">T2 was due</th><th scope="col">Status</th></tr></thead><tbody>';
  ys.forEach(function(ye){
    var eff=nextBusiness(dueDate(ye)),over=eff.getTime()<t.getTime();
    h+='<tr><td>'+fmt(ye)+'</td><td>'+fmt(eff)+'</td><td>'+
       (over?'Overdue':'Not yet due')+'</td></tr>';
  });
  h+='</tbody></table>';
  h+='<p>Each year above is a separate T2 at '+PRICE_JS+'. They are filed '+
     'oldest first, because each year&rsquo;s closing position carries into the '+
     'next return.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out no';out.innerHTML=h;
}
['first','last'].forEach(function(k){
  document.getElementById(k).addEventListener('input',render);});
render();
"""

# ------------------------------------- 14. non-resident T2 penalty calculator
L14 = r"""
// 7.4 states the figure for a non-resident-owned corporation: $25.00 per day
// up to $2,500.00. The cap is therefore reached on day 100.
function daysLate(due,filed){
  var n=Math.round((filed.getTime()-due.getTime())/86400000);
  return n>0?n:0;
}
function nrPenaltyCents(days){
  var c=days*2500;
  return c>250000?250000:c;
}
function daysToCap(days){var r=100-days;return r>0?r:0;}
"""
T14_JS = DATE_JS + L14 + MONEY_JS + PARSE_JS + r"""
var out=document.getElementById('out');
function render(){
  var due=parse('due'),filed=parse('filed'),t=today();
  if(due===null){out.className='ei-out';
    out.innerHTML='<p>Enter the due date and the figure appears here.</p>';return;}
  if(due===undefined||filed===undefined){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';return;}
  var end=filed===null?t:filed;
  var dys=daysLate(due,end),cents=nrPenaltyCents(dys),left=daysToCap(dys);
  var h;
  if(dys===0){
    h='<h3>Not late on that date</h3>'+
      '<p>The return was due '+fmt(due)+' and '+
      (filed===null?'today is ':'the filing date given is ')+fmt(end)+
      ', so no day-count penalty has started.</p>';
    out.className='ei-out ok';
  }else{
    h='<h3>'+dys+' day'+(dys===1?'':'s')+' late</h3>';
    h+='<div class="ei-stats">'+
       '<div class="ei-stat"><span class="ei-stat-l">Days late</span>'+
       '<span class="ei-stat-v">'+dys+'</span></div>'+
       '<div class="ei-stat"><span class="ei-stat-l">Rate per day</span>'+
       '<span class="ei-stat-v">$25.00</span></div>'+
       '<div class="ei-stat"><span class="ei-stat-l">Amount</span>'+
       '<span class="ei-stat-v">'+money(cents)+'</span></div>'+
       '<div class="ei-stat"><span class="ei-stat-l">Maximum</span>'+
       '<span class="ei-stat-v">$2,500.00</span></div></div>';
    h+='<p>'+(cents>=250000
        ? 'The $2,500.00 maximum was reached on day 100 and the figure does not grow after that.'
        : 'The maximum of $2,500.00 is reached on day 100, which is '+left+
          ' day'+(left===1?'':'s')+' from the count above.')+'</p>';
    out.className='ei-out no';
  }
  h+='<div class="ei-danger"><p>'+QUALJS+'</p></div>';
  h+='<p>This figure is the one 7.4 states for a <strong>non-resident-owned '+
     'corporation</strong>. A corporation owned by residents of Canada filing a '+
     'true nil return is not charged a percentage late-filing penalty, because '+
     'that penalty is a percentage of tax owing and the corporation owes '+
     '$0.00.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.innerHTML=h;
}
['due','filed'].forEach(function(k){
  document.getElementById(k).addEventListener('input',render);});
render();
"""

# ---------------------------------------------- 15. dissolution readiness
L15 = r"""
function readiness(a){
  if(a.allyears===null||a.finalt2===null||a.clearance===null||a.accounts===null){
    return 'incomplete';}
  if(a.allyears==='n'){return 'years';}
  if(a.finalt2==='n'){return 'final';}
  if(a.clearance==='n'){return 'clearance';}
  if(a.accounts==='n'){return 'accounts';}
  return 'ready';
}
"""
T15_JS = PICK + L15 + r"""
var out=document.getElementById('out');
var IDS=['allyears','finalt2','clearance','accounts'];
function render(){
  var a={};IDS.forEach(function(k){a[k]=pick(k);});
  var r=readiness(a);
  if(r==='incomplete'){out.className='ei-out';
    out.innerHTML='<p>Answer all four and the result appears here.</p>';return;}
  var h,cls='ei-out no';
  if(r==='ready'){
    cls='ei-out ok';
    h='<h3>Nothing on this list is outstanding</h3>'+
      '<p>Every tax year filed, the final T2 filed to the dissolution date, a '+
      'clearance certificate requested and the other Business Number accounts '+
      'closed is the order these four steps run in.</p>';
  }else if(r==='years'){
    h='<h3>Start with the outstanding tax years</h3>'+
      '<p>An open tax year blocks a clearance certificate, so the returns come '+
      'before anything else. Each outstanding year is a separate T2 at '+
      PRICE_JS+'.</p>';
  }else if(r==='final'){
    h='<h3>The final T2 is still to file</h3>'+
      '<p>The final return covers the period from the start of that fiscal year '+
      'to the dissolution date, and is due within six months of dissolution. It '+
      'is required even when the closing year had no activity.</p>';
  }else if(r==='clearance'){
    h='<h3>The clearance certificate has not been requested</h3>'+
      '<p>The returns are filed, so that request is the next step. Dissolving '+
      'before it is settled leaves a dissolved corporation that can still be '+
      'reassessed on an open year.</p>';
  }else{
    h='<h3>The other Business Number accounts are still open</h3>'+
      '<p>A GST/HST or payroll account left open can still draw correspondence '+
      'after the corporation is gone. Form RC145 closes the programme accounts '+
      'once their own final returns are in.</p>';
  }
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className=cls;out.innerHTML=h;
}
IDS.forEach(function(k){
  Array.prototype.forEach.call(document.querySelectorAll('input[name="'+k+'"]'),
    function(e){e.addEventListener('change',render);});});
render();
"""

QUAL = ('A true nil return carries no percentage late-filing penalty, because '
        'that penalty is a percentage of tax owing and the corporation owes '
        '$0.00. The unfiled year still stays open forever, invites a demand to '
        'file and an arbitrary assessment, blocks a clearance certificate and '
        'dissolution, and costs a non-resident-owned corporation $25.00 per day '
        'up to $2,500.00.')

# render() already emits PRICE_JS and DISC_JS into every tool page, so only
# the two this batch adds are declared here. Shadowing the other two under
# second names put four vars where two were needed.
PRELUDE = ('var NOTNILJS=' + json.dumps(NOT_NIL) + ';'
           'var QUALJS=' + json.dumps(QUAL) + ';\n')


TOOLS3 = [
 dict(slug='corporate-fiscal-year-end-calculator',
  title='Corporate Fiscal Year End Calculator | Permitted Year-Ends',
  h1_pre='Corporate Fiscal ', h1_span='Year End Calculator',
  h1='Corporate Fiscal Year End Calculator',
  eyebrow='Date Tool', keyword='corporate fiscal year end calculator',
  meta=('Enter your incorporation date and the calculator lists every month-end '
        'a first tax year may use, with the T2 due date for each.'),
  tags=['First year cannot exceed 53 weeks', 'Every month-end listed',
        'T2 due six months after', 'The choice is made once'],
  form=tool('Your incorporation date',
            [date('inc', 'The date the corporation was incorporated')],
            'Enter the incorporation date and the permitted year-ends appear here.'),
  js=None,
  sections=[
   ('rule', 'The First Tax Year Sets Everything After It',
    '<p>A corporation chooses its own fiscal year-end. The first tax year '
    'starts on the incorporation date, and it may not exceed 53 weeks, which '
    'is a maximum of 371 days counted inclusively. Every month-end inside that '
    'window is available.</p>\n'
    '<p>The choice is made on the first return and then stays. The Canada '
    'Revenue Agency holds the year-end on record, and a transmission is '
    'rejected when the dates sent do not match that record, so the year-end is '
    'worth getting right the first time rather than correcting later.</p>'),
   ('due', 'Each Year-End Carries Its Own Due Date',
    '<p>A T2 is due within six months of the fiscal year-end, so the year-end '
    'chosen also fixes every filing date that follows. The calculator shows '
    'the due date beside each permitted year-end, shifted to the next business '
    'day where it falls on a weekend or a statutory holiday.</p>\n'
    '<p>A year with no activity is still a filing year, and the fee is '
    + PRICE + '.</p>'),
   ('match', 'A Short First Year Is Normal',
    '<p>Most first tax years are shorter than twelve months, because the '
    'year-end is chosen to suit the corporation rather than to fill a calendar '
    'year. A short first year is a complete tax year, needs its own T2, and '
    'does not reduce the fee.</p>'),
  ],
  faq=[
   ('Can the Year-End Be Changed Later?',
    'Not freely. A fiscal year-end already on record with the Canada Revenue '
    'Agency cannot be moved without the Agency agreeing to the change, which '
    'is why the first return matters.'),
   ('Why Does the Calculator Only Show Month-Ends?',
    'Because almost every corporation uses one, and a month-end keeps the '
    'year-end stable from year to year. A year-end mid-month is permitted and '
    'the 53-week limit is the same; ask us if that is what you need.'),
   ('Is the Longest First Year Always the Best?',
    'No. A longer first year delays the first return but moves every later '
    'due date with it. The calculator shows both effects so the trade is '
    'visible rather than guessed at.'),
   ('Does a First Year With No Activity Still Need a Return?',
    'Yes. The obligation follows the existence of the corporation, not its '
    'activity. A first year in which nothing happened is filed at ' + PRICE
    + '.'),
   ('What Else Is Due in the First Year?',
    'A first return also carries Schedule 24. A federally incorporated '
    'corporation separately files its annual return with Corporations Canada '
    'within 60 days of its anniversary, which is a $12.00 government fee and '
    'is not part of the T2.'),
  ]),

 dict(slug='nil-t2-eligibility-checker',
  title='Nil T2 Eligibility Checker | Can We File Your Return',
  h1_pre='Nil T2 ', h1_span='Eligibility Checker',
  h1='Nil T2 Eligibility Checker',
  eyebrow='Service Check', keyword='nil t2 eligibility checker',
  meta=('Four questions that say whether a nil T2 is the return you need and '
        'whether this service can file it, at ' + PRICE + '.'),
  tags=['Four questions', 'Names the reason either way',
        'Routes work that is not nil', 'No sign-up to use it'],
  form=tool('Four questions about the year you want filed',
            [yn('corp', 'Does the business file a T2 corporate return, rather '
                        'than being a sole proprietorship, a partnership or a trust'),
             yn('ended', 'Has the tax year you want to file already ended'),
             yn('activity', 'Did the corporation have any revenue, expenses, '
                            'investment income, rental income, or dividends '
                            'paid or received in that year'),
             yn('filed', 'Has a return for that year already been filed and '
                         'assessed')],
            'Answer all four and the result appears here.'),
  js=None,
  sections=[
   ('what', 'What This Checker Decides, and What It Does Not',
    '<p>This checker answers one question: is a nil T2 the return you need, '
    'and can this service file it. It is deliberately narrow. The four gates '
    'are the kind of return, whether the year has ended, whether the year was '
    'nil, and whether it is already filed.</p>\n'
    '<p>It does not grade how nil the year was. That is the '
    + a(T + 'dormant-corporation-test/', 'dormant corporation test') + ', which '
    'asks ten activity questions and names the item that disqualifies the '
    'year. Use this one to find out whether to start, and that one to find out '
    'whether the year itself qualifies.</p>'),
   ('nil', 'What Makes a Year Nil',
    '<p>A nil tax year is one in which the corporation carried on no business, '
    'earned nothing and paid nothing out. The corporation can still exist, '
    'hold a bank account and own assets.</p>\n'
    '<div class="ei-danger"><p>' + NOT_NIL + '</p></div>'),
   ('next', 'What Happens When the Answer Is Yes',
    '<p>The fee is ' + PRICE + '. You give the corporation details, pick the '
    'tax years, pay, confirm the filing information and sign Form T183CORP on '
    'a secure single-use screen. Your return is transmitted electronically by '
    'a registered EFILE electronic filer and your CRA confirmation is emailed '
    'within 3 business days.</p>'),
  ],
  faq=[
   ('What If More Than One Year Is Outstanding?',
    'Check the oldest one here, then use the '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' to list every year still outstanding and what each one was due.'),
   ('The Corporation Has Never Traded at All. Does It Still File?',
    'Yes. A corporation that was incorporated and never started operating '
    'files a T2 for every tax year until it is formally dissolved.'),
   ('What If the Year Turns Out Not to Be Nil After I Pay?',
    'We check before you pay. If we find it afterwards, we refund you in '
    'full, and the work is handled by Gondaliya CPA Professional Corporation '
    'at gondaliyacpa.ca instead.'),
   ('Does an Open GST/HST Account Change the Answer?',
    'Not for the T2. It does mean that account has its own nil filings or an '
    'RC145 closure, which the '
    + a(T + 'gst-hst-nil-filing-checker/', 'GST/HST nil filing checker')
    + ' covers.'),
   ('Is a Nil T2 a Shorter Form?',
    'No. It is a complete T2 with the figures at zero. The identification, '
    'the fiscal year dates and the GIFI schedules where they are required are '
    'all still part of the return.'),
  ]),

 dict(slug='unfiled-years-checker',
  title='Unfiled Years Checker | Which T2 Years Are Outstanding',
  h1_pre='Unfiled ', h1_span='Years Checker',
  h1='Unfiled Years Checker',
  eyebrow='Catch-Up Tool', keyword='unfiled years checker',
  meta=('Enter your first fiscal year-end and the last year you filed, and the '
        'checker lists every T2 year still outstanding and what each was due.'),
  tags=['Lists the years, not just a count', 'Due date for each',
        'Oldest filed first', 'Overdue years marked'],
  form=tool('Your year-ends',
            [date('first', 'Your first fiscal year-end'),
             date('last', 'The last tax year-end you filed (leave blank if none)')],
            'Enter your first fiscal year-end and the outstanding years appear here.'),
  js=None,
  sections=[
   ('how', 'One Return Per Tax Year, Oldest First',
    '<p>There is no combined return covering several years. Each outstanding '
    'tax year is its own T2, with its own fiscal year dates and its own due '
    'date six months after that year-end.</p>\n'
    '<p>They are filed oldest first, because each year&rsquo;s closing '
    'position carries into the next return. Filing out of order means going '
    'back over earlier years.</p>'),
   ('why', 'Why an Open Year Matters When Nothing Was Owed',
    '<div class="ei-danger"><p>' + QUAL + '</p></div>\n'
    '<p>That is the whole reason to catch up a nil year: not a bill, but a '
    'year that stays open and a file that cannot be closed.</p>'),
   ('fee', 'What the Catch-Up Costs',
    '<p>Every year costs the same, ' + PRICE + ', whether it is current or '
    'years late. There is no hourly billing and no surcharge for a late year. '
    'The ' + a(T + 'unfiled-years-cost-calculator/', 'unfiled years cost '
    'calculator') + ' turns a year count into the total.</p>'),
  ],
  faq=[
   ('What If I Do Not Know My First Fiscal Year-End?',
    'It is on your first notice of assessment, and your corporate tax account '
    'in My Business Account lists each tax year on record. The '
    + a(T + 'corporate-fiscal-year-end-calculator/', 'fiscal year end '
    'calculator') + ' shows which month-ends a first year could have used.'),
   ('I Have Never Filed Anything. What Do I Enter?',
    'Leave the second date blank. Every tax year that has ended is then '
    'listed as outstanding, starting from the first year-end.'),
   ('Does the Checker Look at My CRA Account?',
    'No. It works only from the two dates you type, so it cannot see what the '
    'Canada Revenue Agency has on record. Treat the list as the years to ask '
    'about, not as a statement of your account.'),
   ('How Many Years Can Be Filed at Once?',
    'There is no limit. Years are prepared together and transmitted oldest '
    'first, one return per tax year, each with its own Form T183CORP.'),
   ('What If One of Those Years Was Not Nil?',
    NOT_NIL),
  ]),

 dict(slug='non-resident-t2-penalty-calculator',
  title='Non-Resident T2 Penalty Calculator | $25.00 a Day to $2,500.00',
  h1_pre='Non-Resident ', h1_span='T2 Penalty Calculator',
  h1='Non-Resident T2 Penalty Calculator',
  eyebrow='Penalty Tool', keyword='non resident t2 penalty calculator',
  meta=('For a non-resident-owned corporation, a late T2 costs $25.00 per day '
        'to a maximum of $2,500.00. Enter the dates and the calculator counts it.'),
  tags=['$25.00 per day', 'Maximum $2,500.00', 'Cap reached on day 100',
        'Non-resident-owned corporations'],
  form=tool('Your dates',
            [date('due', 'The date the T2 was due'),
             date('filed', 'The date it was filed (leave blank for today)')],
            'Enter the due date and the figure appears here.'),
  js=None,
  sections=[
   ('who', 'Who This Figure Applies To',
    '<p>This calculator is for a corporation owned by non-residents of Canada. '
    'For that corporation a late T2 carries a day-count charge of $25.00 per '
    'day, to a maximum of $2,500.00, which is reached on day 100 and does not '
    'grow after it.</p>\n'
    '<p>A corporation owned by residents of Canada filing a true nil return is '
    'in a different position, and the block below is the whole of it.</p>\n'
    '<div class="ei-danger"><p>' + QUAL + '</p></div>'),
   ('due', 'Working Out the Due Date First',
    '<p>The figure depends entirely on the due date, which is six months after '
    'the fiscal year-end, shifted to the next business day where it lands on a '
    'weekend or a statutory holiday. The '
    + a(T + 'nil-t2-deadline-calculator/', 'nil T2 deadline calculator')
    + ' works that date out from a year-end, and the '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' lists it for every outstanding year at once.</p>'),
   ('stop', 'The Count Stops When the Return Is Filed',
    '<p>The day count runs to the filing date, so it stops on the day the '
    'return is transmitted. Filing a nil year that is already past the cap '
    'does not reduce the charge, but it does close the year, which is what '
    'unblocks a clearance certificate and a dissolution.</p>\n'
    '<p>A nil T2 is ' + PRICE + '.</p>'),
  ],
  faq=[
   ('Is This the Same as the Percentage Late-Filing Charge?',
    'No. The percentage charge is calculated on tax owing, so on a true nil '
    'return it is $0.00. The $25.00 a day is a separate day-count charge '
    'stated for a non-resident-owned corporation.'),
   ('What Counts as Non-Resident-Owned?',
    'That depends on who holds the shares and where they are resident, and it '
    'is a determination Sharad Gondaliya, CPA, makes on the file rather than '
    'something a calculator should decide. Use the figure here once you know '
    'the corporation is in that position.'),
   ('Does the Maximum Reset Each Year?',
    'Each tax year is its own return with its own due date, so the day count '
    'and the maximum are worked out per year. Six late years are six separate '
    'counts, not one.'),
   ('Will Filing Now Remove the Charge?',
    'Filing stops the day count at the filing date. It does not erase the days '
    'already counted, and we never promise an outcome on a charge the Canada '
    'Revenue Agency assesses.'),
   ('Does the Calculator Include Interest?',
    'No. It counts only the day-count charge at $25.00 a day to $2,500.00. '
    'Interest is a separate calculation on an amount owing, and a true nil '
    'return has none.'),
  ]),

 dict(slug='dissolution-readiness-checker',
  title='Dissolution Readiness Checker | Before You Wind Up',
  h1_pre='Dissolution ', h1_span='Readiness Checker',
  h1='Dissolution Readiness Checker',
  eyebrow='Closing Check', keyword='dissolution readiness checker',
  meta=('Four questions in the order the steps actually run, naming the first '
        'one still outstanding before a corporation is dissolved.'),
  tags=['Four steps in order', 'Names the first gap',
        'Returns come before clearance', 'Accounts closed last'],
  form=tool('Four questions about where the file stands',
            [yn('allyears', 'Has a T2 been filed for every tax year up to the '
                            'final one'),
             yn('finalt2', 'Has the final T2 to the dissolution date been filed'),
             yn('clearance', 'Has a clearance certificate been requested from '
                             'the Canada Revenue Agency'),
             yn('accounts', 'Have the GST/HST and payroll accounts been closed, '
                            'or were there none')],
            'Answer all four and the result appears here.'),
  js=None,
  sections=[
   ('order', 'The Steps Run in One Order',
    '<p>Dissolution is not a single filing. Four things happen, and they happen '
    'in this order, because each one depends on the one before it.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Step</th>'
    '<th scope="col">What it is</th></tr></thead><tbody>\n'
    '<tr><td>1</td><td>Every outstanding T2 year filed</td></tr>\n'
    '<tr><td>2</td><td>The final T2 filed to the dissolution date</td></tr>\n'
    '<tr><td>3</td><td>A clearance certificate requested</td></tr>\n'
    '<tr><td>4</td><td>The Business Number programme accounts closed</td></tr>\n'
    '</tbody></table>\n'
    '<p>An open tax year blocks a clearance certificate, which is why the '
    'returns are first and not last.</p>'),
   ('two', 'Two Different Bodies, Two Different Filings',
    '<p>Dissolving the corporation and closing its tax accounts are separate '
    'acts with separate bodies. The dissolution goes through the registry the '
    'corporation was incorporated with, federally through Corporations Canada '
    'or provincially. The returns and the account closures go to the Canada '
    'Revenue Agency.</p>\n'
    '<p>Doing one without the other is the common failure: a corporation '
    'dissolved at the registry while an open tax year sits at the Agency can '
    'still be reassessed on that year.</p>'),
   ('final', 'What the Final Return Covers',
    '<p>The final T2 runs from the start of that fiscal year to the '
    'dissolution date, and it is due within six months of dissolution. It is '
    'required even when the closing year had no activity at all, and a nil '
    'final return is ' + PRICE + '.</p>\n'
    '<div class="ei-danger"><p>' + QUAL + '</p></div>'),
  ],
  faq=[
   ('Can a Corporation Be Dissolved With Years Still Unfiled?',
    'The registry and the Agency are separate, so a dissolution can be '
    'registered while years are open, but it leaves a dissolved corporation '
    'that can still be reassessed and a clearance certificate that cannot be '
    'settled. Filing first is what finishes the file.'),
   ('How Many Years Might Be Outstanding?',
    'Use the ' + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' to list every tax year still outstanding and what each one was due.'),
   ('Is the Final Return Different From a Normal One?',
    'It covers a shorter period, from the start of the fiscal year to the '
    'dissolution date, and that period is what makes it final. A nil final '
    'return is otherwise an ordinary nil T2.'),
   ('What Closes the GST/HST and Payroll Accounts?',
    'Form RC145 closes the Business Number programme accounts, once each of '
    'those accounts has its own final return or remittance in.'),
   ('What If the Corporation Held Assets?',
    'Then the closing year is not nil. ' + NOT_NIL),
  ]),
]

for t, js in zip(TOOLS3, [T11_JS, T12_JS, T13_JS, T14_JS, T15_JS]):
    t['js'] = PRELUDE + js

ORDER3 = ORDER + [t['slug'] for t in TOOLS3]
LINK_TITLE3 = dict(LINK_TITLE, **{
 'corporate-fiscal-year-end-calculator': 'Corporate fiscal year end calculator',
 'nil-t2-eligibility-checker': 'Nil T2 eligibility checker',
 'unfiled-years-checker': 'Unfiled years checker, every outstanding year',
 'non-resident-t2-penalty-calculator': 'Non-resident T2 penalty calculator',
 'dissolution-readiness-checker': 'Dissolution readiness checker',
})

# Siblings mix this batch with the ten already live, so the new pages are not
# an island and the established pages gain inbound links from them.
SIBLINGS3 = {10: [5, 6, 11], 11: [8, 2, 12], 12: [3, 0, 13],
             13: [0, 12, 14], 14: [12, 8, 1]}

GUIDES3 = {
 'corporate-fiscal-year-end-calculator': [
   ('first-year-t2-filing', 'The complete guide to first-year T2 filing')],
 'nil-t2-eligibility-checker': [
   ('nil-t2-return-complete-guide', 'The complete guide to the nil T2 return'),
   ('dormant-and-inactive-corporations',
    'The complete guide to dormant and inactive corporations')],
 'unfiled-years-checker': [
   ('catch-up-unfiled-corporate-tax-returns',
    'The complete guide to catching up unfiled corporate tax returns'),
   ('cra-demand-to-file-response', 'Responding to a CRA demand to file')],
 'non-resident-t2-penalty-calculator': [
   ('t2-late-filing-penalties', 'T2 late filing penalties')],
 'dissolution-readiness-checker': [
   ('final-t2-and-dissolution', 'The final T2 and dissolution')],
}

for t in TOOLS3:
    i = ORDER3.index(t['slug'])
    rel = [(T + ORDER3[j] + '/', LINK_TITLE3[ORDER3[j]]) for j in SIBLINGS3[i]]
    rel += [(G + g + '/', ttl) for g, ttl in GUIDES3[t['slug']]]
    rel.append((COST, 'Nil T2 filing cost'))
    t['related'] = rel


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'October 26, 2026', '2026-10-26'
    recs = []
    for t in TOOLS3:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html, **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2c-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-42s %6d bytes  %s' % (r['slug'], len(r['content'].encode()),
                                       r['url']))
