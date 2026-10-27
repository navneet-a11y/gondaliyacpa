"""Family 2, tools 21 to 30.

Ten more calculators and checkers from the Appendix A list of 150.

Which ten, and why these. The list contains long runs of near-synonyms, and
line 1210 requires logic unique to each tool, so the batch was chosen for
distinct logic rather than list order. Six are date arithmetic on the holiday
engine already built and tested for the deadline calculator, which means no
new unverified numbers enter the site. Four are decision trees over facts the
plan states outright.

Skipped, with the reason:

  /t2-late-filing-penalty-calculator/
  /repeated-failure-to-file-penalty-calculator/
  /demand-to-file-penalty-calculator/
  /failure-to-comply-penalty-calculator/
      Each needs the statutory percentage and monthly rate. The plan grounds
      exactly two penalty figures: the non-resident $25.00 per day up to
      $2,500.00, and the qualification that a true nil return carries no
      percentage penalty because the penalty is a percentage of tax owing.
      The percentages themselves are nowhere in it. Putting a dollar figure a
      visitor may rely on in front of them from memory is the same class of
      invention as the per-province tax rate reserved for Sharad Gondaliya.

  /ontario-annual-return-deadline-calculator/
  /ontario-missed-annual-returns-calculator/
      Still blocked on the Ontario annual return due date, outstanding since
      the second batch. The plan states the federal 60-day rule and the
      October 2021 registry move, but never the Ontario date.

  /t2-six-month-deadline-calculator/
  /still-required-to-file-checker/
  /back-year-t2-cost-calculator/
  /outstanding-returns-count-checker/
      Each duplicates a tool already live: the deadline calculator, the
      inactive corporation filing checker, the unfiled years cost calculator
      and the unfiled years checker respectively.

  /small-supplier-threshold-calculator/
  /small-business-deduction-limit-calculator/
  /taxable-capital-employed-in-canada-calculator/
  /t1135-late-penalty-calculator/
      Each turns on a statutory dollar threshold the plan does not state.

The running total of 150 is unaffected by which ten were built first.
"""
import io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_f2 import (render, meta, yn, a, DATE_JS, SITE, HUB, FORM, PRICE,
                      NOT_NIL, TOOL_DISCLAIMER)
from build_f2b import tool, num, date, out_box, PICK, T, G, COST
from build_f2c import (DUE_JS, MONEY_JS, PARSE_JS, QUAL, PRELUDE)
from build_f2d import ORDER4, LINK_TITLE4

# addYear is the month-end-aware year step. A February 28 year-end in a leap
# year steps to February 29, because month-end means the last day of the
# month, which is the same rule dueDate applies six months out.
ADD_YEAR = r"""function addYear(dt,k){
  var y=dt.getUTCFullYear(),m=dt.getUTCMonth(),d=dt.getUTCDate();
  if(d===lastDay(y,m)){return u(y+k,m+1,0);}
  return u(y+k,m,Math.min(d,lastDay(y+k,m)));
}
"""

import build_f2c as _f2c
assert ADD_YEAR.strip() in _f2c.L13, (
    'addYear() has diverged from the unfiled years checker. Two tools would '
    'step the same year-end to different dates.')

# 53 weeks is 371 days counted inclusively, and the latest permitted year-end
# is therefore the incorporation date plus 370 days. Held here as one pair of
# constants so the three tools that use the rule cannot drift apart.
WEEKS53_DAYS = 371
WEEKS53_OFFSET = 370

import build_f2b as _f2b
assert 'var ok=days<=%d;' % WEEKS53_DAYS in _f2b.T6_JS, (
    '53-week test has diverged from the first tax year checker.')
assert 'inc.getTime()+%d*86400000' % WEEKS53_OFFSET in _f2b.T6_JS, (
    'latest permitted year-end has diverged from the first tax year checker.')

# ------------------------------------------------------------------ helpers
# Every date tool here needs the same three things: the inclusive day count
# between two dates, the filing date once the weekend and holiday shift is
# applied, and a guard against a runaway loop.
SPAN_JS = r"""function spanDays(a,b){
  return Math.round((b.getTime()-a.getTime())/86400000)+1;
}
function filingDate(ye){return nextBusiness(dueDate(ye));}
function dayAfter(dt){return new Date(dt.getTime()+86400000);}
function dayBefore(dt){return new Date(dt.getTime()-86400000);}
function plural(n,w){return n+' '+w+(n===1?'':'s');}
"""

BASE = PRELUDE + DATE_JS + DUE_JS + ADD_YEAR + PARSE_JS + SPAN_JS


# ----------------------------------------- 21. tax years since incorporation
# Enumerates every tax year the corporation has had, which is the question
# behind a catch-up. The unfiled years checker counts what is outstanding
# from a year-end; this one works forward from the incorporation date and the
# first year-end chosen, so it also shows the first short year and whether
# that first year was inside 53 weeks.
L21 = r"""
function taxYears(inc,fye,now){
  if(inc===null||fye===null){return null;}
  if(inc===undefined||fye===undefined){return {err:'read'};}
  if(fye.getTime()<=inc.getTime()){return {err:'order'};}
  var first=spanDays(inc,fye);
  var rows=[],ye=fye,n=0;
  while(ye.getTime()<=now.getTime()&&n<60){
    var fd=filingDate(ye);
    rows.push({ye:ye,due:fd,late:fd.getTime()<now.getTime()});
    ye=addYear(ye,1);n++;
  }
  return {first:first,over53:first>371,rows:rows,
          next:{ye:ye,due:filingDate(ye)},
          late:rows.filter(function(r){return r.late;}).length};
}
"""
T21_JS = BASE + L21 + r"""
var out=document.getElementById('out');
function render(){
  var r=taxYears(parse('inc'),parse('fye'),today());
  if(r===null){out.className='ei-out';
    out.innerHTML='<p>Enter the incorporation date and the first fiscal '+
      'year-end, and every tax year since appears here.</p>';return;}
  if(r.err==='read'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';
    return;}
  if(r.err==='order'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">The first fiscal year-end must fall '+
      'after the incorporation date.</p>';return;}
  var h='<h3>'+plural(r.rows.length,'tax year')+' have ended, '+
        (r.late===0?'none of them overdue':plural(r.late,'return')+' overdue')+
        '</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">Tax years ended</span>'+
     '<span class="ei-stat-v">'+r.rows.length+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Returns now overdue</span>'+
     '<span class="ei-stat-v">'+r.late+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Length of the first year</span>'+
     '<span class="ei-stat-v">'+plural(r.first,'day')+'</span></div></div>';
  if(r.over53){
    h+='<div class="ei-warn"><p>The first tax year is '+plural(r.first,'day')+
       ', which is longer than the 53 weeks a first tax year may not exceed. '+
       'The year-end on record with the Canada Revenue Agency may not be the '+
       'one entered here, and a transmission against the wrong year-end is '+
       'rejected.</p></div>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Tax year ended</th>'+
     '<th scope="col">Filing due</th><th scope="col">Status</th>'+
     '</tr></thead><tbody>';
  r.rows.forEach(function(w){
    h+='<tr><td>'+fmt(w.ye)+'</td><td>'+fmt(w.due)+'</td><td>'+
       (w.late?'Overdue':'Not yet due')+'</td></tr>';});
  h+='</tbody></table>';
  h+='<p>The next tax year ends '+fmt(r.next.ye)+' and its return is due '+
     fmt(r.next.due)+'.</p>';
  if(r.late>0){
    h+='<p>'+plural(r.late,'nil return')+' at '+PRICE_JS+
       ' is '+plural(r.late,'return')+' transmitted in one sitting.</p>';
    h+='<div class="ei-info"><p>'+QUALJS+'</p></div>';
  }
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className=r.late>0?'ei-out no':'ei-out ok';
  out.innerHTML=h;
}
['inc','fye'].forEach(function(k){
  document.getElementById(k).addEventListener('change',render);
  document.getElementById(k).addEventListener('input',render);});
render();
"""

# -------------------------------------------------- 22. days overdue
# Calendar days and business days are both wanted, and they are different
# numbers. businessBetween is the engine's own count, so a shift that moved
# the filing date is already accounted for before the counting starts.
L22 = r"""
function overdueBy(fye,now){
  if(fye===null){return null;}
  if(fye===undefined){return {err:'read'};}
  var due=filingDate(fye);
  if(due.getTime()>=now.getTime()){
    return {late:false,due:due,
            cal:Math.round((due.getTime()-now.getTime())/86400000),
            biz:businessBetween(now,due)};
  }
  return {late:true,due:due,
          cal:Math.round((now.getTime()-due.getTime())/86400000),
          biz:businessBetween(due,now)};
}
"""
T22_JS = BASE + L22 + r"""
var out=document.getElementById('out');
function render(){
  var r=overdueBy(parse('fye'),today());
  if(r===null){out.className='ei-out';
    out.innerHTML='<p>Enter the fiscal year-end and the count appears '+
      'here.</p>';return;}
  if(r.err==='read'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';
    return;}
  var h='<h3>'+(r.late?'This return is '+plural(r.cal,'day')+' overdue'
                      :'This return is not due yet')+'</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">Filing due</span>'+
     '<span class="ei-stat-v">'+fmt(r.due)+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Calendar days'+
     (r.late?' overdue':' remaining')+'</span>'+
     '<span class="ei-stat-v">'+r.cal+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Business days'+
     (r.late?' overdue':' remaining')+'</span>'+
     '<span class="ei-stat-v">'+r.biz+'</span></div></div>';
  if(r.late){
    h+='<p>The two counts differ because weekends and the statutory holidays '+
       'the Canada Revenue Agency treats as closed days are not business '+
       'days. The filing date itself already has that shift applied.</p>';
    h+='<div class="ei-info"><p>'+QUALJS+'</p></div>';
    h+='<p>A late nil year is still '+PRICE_JS+
       ', and the return can be transmitted now.</p>';
  }else{
    h+='<p>There are '+plural(r.biz,'business day')+' between today and the '+
       'filing date. A nil return can be transmitted as soon as the tax year '+
       'has ended, so there is no reason to wait for the date.</p>';
  }
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className=r.late?'ei-out no':'ei-out ok';
  out.innerHTML=h;
}
document.getElementById('fye').addEventListener('change',render);
document.getElementById('fye').addEventListener('input',render);
render();
"""

# ------------------------------------------------- 23. next T2 due date
# Not the same as the deadline calculator, which answers "this year-end is
# due when". This answers "which date is next", and the catch is that the
# next date due is usually the PREVIOUS year-end's, not the coming one's: a
# June 30 year-end sitting in October has December 31 next, not the following
# June. Walking back first and then forward is what gets that right.
L23 = r"""
function nextDue(fye,now){
  if(fye===null){return null;}
  if(fye===undefined){return {err:'read'};}
  var ye=fye,n=0;
  while(ye.getTime()>now.getTime()&&n<400){ye=addYear(ye,-1);n++;}
  while(n<800){
    var fd=filingDate(ye);
    if(fd.getTime()>=now.getTime()){
      return {ye:ye,due:fd,ended:ye.getTime()<=now.getTime(),
              days:Math.round((fd.getTime()-now.getTime())/86400000),
              biz:businessBetween(now,fd)};
    }
    ye=addYear(ye,1);n++;
  }
  return {err:'range'};
}
"""
T23_JS = BASE + L23 + r"""
var out=document.getElementById('out');
function render(){
  var r=nextDue(parse('fye'),today());
  if(r===null){out.className='ei-out';
    out.innerHTML='<p>Enter any one of the corporation&rsquo;s fiscal '+
      'year-ends and the next filing date appears here.</p>';return;}
  if(r.err==='read'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';
    return;}
  if(r.err==='range'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That date is too far from today for '+
      'this tool to work from.</p>';return;}
  var h='<h3>The next T2 is due '+fmt(r.due)+'</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">For the tax year ended</span>'+
     '<span class="ei-stat-v">'+fmt(r.ye)+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Filing due</span>'+
     '<span class="ei-stat-v">'+fmt(r.due)+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Business days away</span>'+
     '<span class="ei-stat-v">'+r.biz+'</span></div></div>';
  if(r.ended){
    h+='<p>That tax year has already ended, so this return can be '+
       'transmitted today. Waiting for the date adds nothing.</p>';
  }else{
    h+='<p>That tax year has not ended yet. The return cannot be transmitted '+
       'until it has.</p>';
  }
  h+='<p>Every T2 is due six months after the fiscal year-end, and where '+
     'that date lands on a weekend or a statutory holiday it moves to the '+
     'next business day. The '+
     '<a href="https://corpnilfilingfor300.ca/tools/due-date-weekend-holiday-shift-calculator/">'+
     'due date weekend and holiday shift calculator</a> shows that step on '+
     'its own.</p>';
  h+='<p>A nil return for this year is '+PRICE_JS+'.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out ok';
  out.innerHTML=h;
}
document.getElementById('fye').addEventListener('change',render);
document.getElementById('fye').addEventListener('input',render);
render();
"""


# ------------------------------------------- 24. final T2 return due date
# Dissolution ends the tax year on the date of dissolution, so the final
# return covers a stub period from the day after the last normal year-end.
# The six months runs from the dissolution date, not from the year-end that
# would have applied.
L24 = r"""
function finalReturn(fye,dis){
  if(fye===null||dis===null){return null;}
  if(fye===undefined||dis===undefined){return {err:'read'};}
  if(dis.getTime()<=fye.getTime()){return {err:'order'};}
  var start=dayAfter(fye),days=spanDays(start,dis);
  return {start:start,end:dis,days:days,stub:days<365,
          due:filingDate(dis),
          wouldHave:filingDate(addYear(fye,1))};
}
"""
T24_JS = BASE + L24 + r"""
var out=document.getElementById('out');
function render(){
  var r=finalReturn(parse('fye'),parse('dis'),today());
  if(r===null){out.className='ei-out';
    out.innerHTML='<p>Enter the last fiscal year-end and the date of '+
      'dissolution, and the final return period appears here.</p>';return;}
  if(r.err==='read'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';
    return;}
  if(r.err==='order'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">The dissolution date must fall after '+
      'the last fiscal year-end.</p>';return;}
  var h='<h3>The final T2 is due '+fmt(r.due)+'</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">Final tax year</span>'+
     '<span class="ei-stat-v">'+fmt(r.start)+' to '+fmt(r.end)+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Length</span>'+
     '<span class="ei-stat-v">'+plural(r.days,'day')+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Final T2 due</span>'+
     '<span class="ei-stat-v">'+fmt(r.due)+'</span></div></div>';
  h+='<p>Dissolution ends the tax year on the date of dissolution, so the '+
     'final return covers '+fmt(r.start)+' to '+fmt(r.end)+' and is due six '+
     'months after the dissolution date.</p>';
  if(r.stub){
    h+='<p>That is a short final year of '+plural(r.days,'day')+'. A short '+
       'year does not shorten the six months, and it does not change what '+
       'the return costs.</p>';
  }
  h+='<p>Had the corporation carried on to its usual year-end, the return '+
     'for that year would have been due '+fmt(r.wouldHave)+' instead.</p>';
  h+='<div class="ei-warn"><p>Every earlier year still has to be filed '+
     'before dissolution completes. An unfiled year blocks a clearance '+
     'certificate and blocks the dissolution itself.</p></div>';
  h+='<p>A nil final return is '+PRICE_JS+'.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out ok';
  out.innerHTML=h;
}
['fye','dis'].forEach(function(k){
  document.getElementById(k).addEventListener('change',render);
  document.getElementById(k).addEventListener('input',render);});
render();
"""

# ------------------------------------------ 25. amalgamation T2 due date
# An amalgamation ends each predecessor's tax year on the day BEFORE the
# amalgamation date, and the new corporation's first tax year begins on the
# amalgamation date itself. That off-by-one day is the whole point of the
# tool: a final return filed to the amalgamation date is filed to the wrong
# year-end and the transmission is rejected.
L25 = r"""
function amalgDates(fye,amal){
  if(fye===null||amal===null){return null;}
  if(fye===undefined||amal===undefined){return {err:'read'};}
  if(amal.getTime()<=fye.getTime()){return {err:'order'};}
  var pStart=dayAfter(fye),pEnd=dayBefore(amal);
  if(pEnd.getTime()<pStart.getTime()){return {err:'sameday'};}
  return {pStart:pStart,pEnd:pEnd,pDays:spanDays(pStart,pEnd),
          pDue:filingDate(pEnd),
          nStart:amal,
          nLatest:new Date(amal.getTime()+370*86400000)};
}
"""
T25_JS = BASE + L25 + r"""
var out=document.getElementById('out');
function render(){
  var r=amalgDates(parse('fye'),parse('amal'));
  if(r===null){out.className='ei-out';
    out.innerHTML='<p>Enter a predecessor&rsquo;s last fiscal year-end and '+
      'the date of amalgamation, and the dates appear here.</p>';return;}
  if(r.err==='read'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';
    return;}
  if(r.err==='order'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">The amalgamation date must fall after '+
      'the last fiscal year-end.</p>';return;}
  if(r.err==='sameday'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">The amalgamation falls on the day '+
      'after the year-end, which leaves no period for a final return.</p>';
    return;}
  var h='<h3>The predecessor&rsquo;s final T2 is due '+fmt(r.pDue)+'</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">Predecessor final year</span>'+
     '<span class="ei-stat-v">'+fmt(r.pStart)+' to '+fmt(r.pEnd)+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Final T2 due</span>'+
     '<span class="ei-stat-v">'+fmt(r.pDue)+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">New corporation&rsquo;s first year begins</span>'+
     '<span class="ei-stat-v">'+fmt(r.nStart)+'</span></div></div>';
  h+='<div class="ei-warn"><p>The predecessor&rsquo;s tax year ends '+
     fmt(r.pEnd)+', the day before the amalgamation, not on '+fmt(r.nStart)+
     '. A final return filed to the amalgamation date is filed to a year-end '+
     'the Canada Revenue Agency does not hold, and the transmission is '+
     'rejected.</p></div>';
  h+='<p>Each predecessor files its own final return for its own period. '+
     'One amalgamation of two corporations means two final returns, and each '+
     'nil one is '+PRICE_JS+'.</p>';
  h+='<p>The new corporation&rsquo;s first tax year begins '+fmt(r.nStart)+
     ' and may not exceed 53 weeks, so the latest first year-end it may '+
     'choose is '+fmt(r.nLatest)+'.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out ok';
  out.innerHTML=h;
}
['fye','amal'].forEach(function(k){
  document.getElementById(k).addEventListener('change',render);
  document.getElementById(k).addEventListener('input',render);});
render();
"""

# ------------------------------------------- 26. short tax year deadline
# The common wrong assumption is that a short year gets a proportionally
# shorter filing window. It does not: six months runs from the year-end
# whatever the period's length.
L26 = r"""
function shortYear(st,en){
  if(st===null||en===null){return null;}
  if(st===undefined||en===undefined){return {err:'read'};}
  if(en.getTime()<=st.getTime()){return {err:'order'};}
  var days=spanDays(st,en);
  return {st:st,en:en,days:days,weeks:Math.floor(days/7),rem:days%7,
          short:days<365,over53:days>371,
          due:filingDate(en),
          latest53:new Date(st.getTime()+370*86400000)};
}
"""
T26_JS = BASE + L26 + r"""
var out=document.getElementById('out');
function render(){
  var r=shortYear(parse('st'),parse('en'));
  if(r===null){out.className='ei-out';
    out.innerHTML='<p>Enter the first and last day of the tax year and the '+
      'filing date appears here.</p>';return;}
  if(r.err==='read'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';
    return;}
  if(r.err==='order'){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">The last day must fall after the first '+
      'day.</p>';return;}
  var h='<h3>This return is due '+fmt(r.due)+'</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">Length of the tax year</span>'+
     '<span class="ei-stat-v">'+plural(r.days,'day')+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">In weeks</span>'+
     '<span class="ei-stat-v">'+r.weeks+(r.rem?' weeks and '+plural(r.rem,'day'):' weeks')+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Filing due</span>'+
     '<span class="ei-stat-v">'+fmt(r.due)+'</span></div></div>';
  if(r.over53){
    h+='<div class="ei-warn"><p>A tax year of '+plural(r.days,'day')+
       ' is longer than 53 weeks. A first tax year may not exceed 53 weeks, '+
       'which is 371 days, so a first year starting '+fmt(r.st)+
       ' could end no later than '+fmt(r.latest53)+'. A later tax year may '+
       'run a full twelve months, so this only bites on a first year.</p></div>';
  }
  h+='<p>'+(r.short?'This is a short tax year of '+plural(r.days,'day')+'. '
                   :'This is a full tax year of '+plural(r.days,'day')+'. ')+
     'Six months runs from the year-end whatever the length of the period, '+
     'so a short year does not get a shorter filing window and does not get '+
     'a longer one either.</p>';
  h+='<p>A short year is a separate tax year and needs its own return. Two '+
     'year-ends in one calendar year means two returns, and each nil one is '+
     PRICE_JS+'.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out ok';
  out.innerHTML=h;
}
['st','en'].forEach(function(k){
  document.getElementById(k).addEventListener('change',render);
  document.getElementById(k).addEventListener('input',render);});
render();
"""


# -------------------------------------- 27. nil return late penalty checker
# The one tool on the site whose whole subject is the qualification block.
# It is emitted as a single paragraph in every branch that reaches it, never
# summarised and never split, and the percentage rates are not stated
# anywhere because the plan does not supply them.
L27 = r"""
function latePenalty(a){
  if(a.nil===null||a.nr===null||a.dem===null){return null;}
  return {truly:a.nil==='y',nonres:a.nr==='y',demand:a.dem==='y'};
}
"""
T27_JS = PICK + PRELUDE + L27 + r"""
var out=document.getElementById('out');
var IDS=['nil','nr','dem'];
function render(){
  var a={};IDS.forEach(function(k){a[k]=pick(k);});
  var r=latePenalty(a);
  if(r===null){out.className='ei-out';
    out.innerHTML='<p>Answer all three and the position appears here.</p>';
    return;}
  var h='';
  if(r.truly){
    h+='<h3>No percentage late-filing penalty applies to this year</h3>';
    h+='<div class="ei-info"><p>'+QUALJS+'</p></div>';
    if(r.nonres){
      h+='<p>This corporation is non-resident-owned, so the charge in that '+
         'last sentence is the one that applies here: $25.00 per day up to '+
         '$2,500.00 for the unfiled year. It runs on the lateness itself and '+
         'does not depend on any tax being owed.</p>';
    }else{
      h+='<p>The per-day charge in that last sentence applies to '+
         'non-resident-owned corporations. It does not apply here.</p>';
    }
  }else{
    h+='<h3>This is not a nil year, so the percentage penalty can apply</h3>';
    h+='<p>The late-filing penalty is a percentage of the tax owing. Where '+
       'a corporation owes tax, there is a figure for the percentage to '+
       'apply to, and the amount depends on the tax owing and on how late '+
       'the return is. That calculation is not one this tool does.</p>';
    h+='<div class="ei-cmp"><div><h4>A nil year</h4><p>Owes $0.00, so the '+
       'percentage has nothing to apply to.</p></div><div><h4>A year with '+
       'tax owing</h4><p>Has a balance, so the percentage applies to '+
       'it.</p></div></div>';
    h+='<p>'+NOTNILJS+'</p>';
  }
  if(r.demand){
    h+='<div class="ei-danger"><p>A demand to file has been issued, which '+
       'changes the position. A demand sets its own deadline and opens the '+
       'way to an arbitrary assessment, in which the Canada Revenue Agency '+
       'assesses a figure of its own. The '+
       '<a href="https://corpnilfilingfor300.ca/guides/cra-demand-to-file-response/">'+
       'guide to responding to a demand to file</a> sets out what the letter '+
       'asks for and in what order.</p></div>';
  }
  if(r.truly){
    h+='<p>A late nil year is '+PRICE_JS+', the same as one filed on time, '+
       'and it can be transmitted now.</p>';
  }
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className=r.truly&&!r.demand?'ei-out ok':'ei-out no';
  out.innerHTML=h;
}
IDS.forEach(function(k){
  Array.prototype.forEach.call(document.querySelectorAll('input[name="'+k+'"]'),
    function(e){e.addEventListener('change',render);});});
render();
"""

# ------------------------------- 28. clearance certificate requirement
L28 = r"""
function clearance(a){
  if(a.dist===null||a.dis===null||a.unf===null){return null;}
  return {dist:a.dist==='y',dis:a.dis==='y',unf:a.unf==='y',
          wanted:a.dist==='y'||a.dis==='y'};
}
"""
T28_JS = PICK + PRELUDE + L28 + r"""
var out=document.getElementById('out');
var IDS=['dist','dis','unf'];
function render(){
  var a={};IDS.forEach(function(k){a[k]=pick(k);});
  var r=clearance(a);
  if(r===null){out.className='ei-out';
    out.innerHTML='<p>Answer all three and the position appears here.</p>';
    return;}
  var h='';
  if(!r.wanted){
    h+='<h3>Nothing here calls for a clearance certificate yet</h3>';
    h+='<p>A clearance certificate confirms the Canada Revenue Agency has '+
       'no further claim before property is distributed. With no '+
       'distribution and no dissolution in progress, there is nothing for it '+
       'to clear.</p>';
  }else{
    h+='<h3>A clearance certificate belongs in this plan</h3>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Step</th>'+
       '<th scope="col">Where it stands</th></tr></thead><tbody>';
    h+='<tr><td>Property to be distributed to shareholders</td><td>'+
       (r.dist?'Yes':'No')+'</td></tr>';
    h+='<tr><td>Dissolution in progress</td><td>'+(r.dis?'Yes':'No')+
       '</td></tr>';
    h+='<tr><td>Every tax year filed</td><td>'+(r.unf?'No':'Yes')+
       '</td></tr></tbody></table>';
    if(r.dist){
      h+='<p>Distributing property without a clearance certificate leaves '+
         'the person who distributed it personally exposed for amounts the '+
         'corporation turns out to owe. That is the reason the certificate '+
         'exists.</p>';
    }
  }
  if(r.unf){
    h+='<div class="ei-danger"><p>There is at least one unfiled tax year, '+
       'and that is the blocker. An unfiled year blocks a clearance '+
       'certificate and blocks the dissolution behind it. Every outstanding '+
       'year has to be filed first, nil years included.</p></div>';
    h+='<p>Each outstanding nil year is '+PRICE_JS+
       ', and several years can be transmitted in one sitting. The '+
       '<a href="https://corpnilfilingfor300.ca/tools/unfiled-years-checker/">'+
       'unfiled years checker</a> lists which years are outstanding.</p>';
    h+='<div class="ei-info"><p>'+QUALJS+'</p></div>';
  }else if(r.wanted){
    h+='<p>With every year filed, the filing history is not what holds the '+
       'certificate up.</p>';
  }
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className=r.unf?'ei-out no':'ei-out ok';
  out.innerHTML=h;
}
IDS.forEach(function(k){
  Array.prototype.forEach.call(document.querySelectorAll('input[name="'+k+'"]'),
    function(e){e.addEventListener('change',render);});});
render();
"""

# ---------------------------------------- 29. payroll nil remittance checker
L29 = r"""
function payroll(a){
  if(a.acct===null||a.wag===null||a.clo===null){return null;}
  if(a.acct==='n'){return {kind:'none'};}
  if(a.wag==='y'){return {kind:'active',close:a.clo==='y'};}
  return {kind:'nil',close:a.clo==='y'};
}
"""
T29_JS = PICK + PRELUDE + L29 + r"""
var out=document.getElementById('out');
var IDS=['acct','wag','clo'];
function render(){
  var a={};IDS.forEach(function(k){a[k]=pick(k);});
  var r=payroll(a);
  if(r===null){out.className='ei-out';
    out.innerHTML='<p>Answer all three and the payroll position appears '+
      'here.</p>';return;}
  var h='';
  if(r.kind==='none'){
    h+='<h3>No payroll account, so nothing to remit</h3>';
    h+='<p>With no payroll account on record there is no remittance '+
       'obligation and nothing to close. The nil T2 is unaffected either '+
       'way: it is a separate return on a separate account.</p>';
  }else if(r.kind==='active'){
    h+='<h3>Wages were paid, so this is a real remittance, not a nil one</h3>';
    h+='<p>Where salary or wages were paid, source deductions are owed on '+
       'them and the remittance is not nil. That also means the corporation '+
       'had an expense in the period, so the tax year it falls in is not a '+
       'nil year.</p>';
    h+='<p>'+NOTNILJS+'</p>';
  }else{
    h+='<h3>The account is open with no wages paid, so nil remittances are '+
       'still due</h3>';
    h+='<p>An open payroll account carries its own obligation on its own '+
       'cycle whether or not anyone was paid. Reporting nothing is not the '+
       'same as reporting nil: the account expects to hear from the '+
       'corporation on each due date, and silence on an open account is what '+
       'draws correspondence.</p>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Account</th>'+
       '<th scope="col">What is owed while dormant</th>'+
       '<th scope="col">Covered by '+PRICE_JS+'</th></tr></thead><tbody>'+
       '<tr><td>Corporation income tax</td><td>One T2 for every tax year '+
       'until dissolution</td><td>Yes</td></tr>'+
       '<tr><td>Payroll</td><td>A remittance on the account&rsquo;s own '+
       'cycle, nil ones included</td><td>No</td></tr>'+
       '</tbody></table>';
  }
  if(r.kind!=='none'&&r.close){
    h+='<div class="ei-info"><p>To stop the obligation rather than keep '+
       'meeting it, the account is closed with Form RC145 once its final '+
       'remittance is in. An account left open can still draw '+
       'correspondence after the corporation itself is gone.</p></div>';
  }
  h+='<p>The nil T2 at '+PRICE_JS+' covers the corporation income tax '+
     'account only. Payroll is a separate filing and is not part of the '+
     'fee.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className=r.kind==='none'?'ei-out ok':'ei-out no';
  out.innerHTML=h;
}
IDS.forEach(function(k){
  Array.prototype.forEach.call(document.querySelectorAll('input[name="'+k+'"]'),
    function(e){e.addEventListener('change',render);});});
render();
"""

# -------------------------------------- 30. GST/HST account closure checker
L30 = r"""
function gstClose(a){
  if(a.acct===null||a.sales===null||a.fin===null){return null;}
  if(a.acct==='n'){return {kind:'none'};}
  if(a.sales==='y'){return {kind:'trading'};}
  return {kind:a.fin==='y'?'ready':'returns'};
}
"""
T30_JS = PICK + PRELUDE + L30 + r"""
var out=document.getElementById('out');
var IDS=['acct','sales','fin'];
function render(){
  var a={};IDS.forEach(function(k){a[k]=pick(k);});
  var r=gstClose(a);
  if(r===null){out.className='ei-out';
    out.innerHTML='<p>Answer all three and the closure position appears '+
      'here.</p>';return;}
  var h='',ok=false;
  if(r.kind==='none'){
    ok=true;
    h+='<h3>No GST/HST account, so nothing to close</h3>';
    h+='<p>With no GST/HST account on record there is nothing to file on it '+
       'and nothing to close. The nil T2 is a separate return on a separate '+
       'account and is unaffected.</p>';
  }else if(r.kind==='trading'){
    h+='<h3>The account is still in use, so it is not ready to close</h3>';
    h+='<p>Taxable sales are still being made, so the account is doing its '+
       'job and closing it would be wrong. It also means the corporation has '+
       'revenue, so the tax year those sales fall in is not a nil year.</p>';
    h+='<p>'+NOTNILJS+'</p>';
  }else if(r.kind==='returns'){
    h+='<h3>Returns are outstanding, so the account cannot close yet</h3>';
    h+='<p>Form RC145 closes a GST/HST account, but only once the account '+
       'has its own final return in. Until then the account stays open and '+
       'keeps expecting a return on its own cycle, nil ones included.</p>';
  }else{
    ok=true;
    h+='<h3>This account is ready to close with Form RC145</h3>';
    h+='<p>No taxable sales are being made and the final return is in, which '+
       'is the state Form RC145 expects. Closing it ends the filing '+
       'obligation on the GST/HST account.</p>';
  }
  if(r.kind!=='none'){
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Condition</th>'+
       '<th scope="col">Where it stands</th></tr></thead><tbody>'+
       '<tr><td>GST/HST account open</td><td>Yes</td></tr>'+
       '<tr><td>Taxable sales still being made</td><td>'+
       (r.kind==='trading'?'Yes':'No')+'</td></tr>'+
       '<tr><td>Final return filed on the account</td><td>'+
       (r.kind==='ready'?'Yes':'No')+'</td></tr></tbody></table>';
    h+='<div class="ei-warn"><p>Closing the GST/HST account does nothing '+
       'about the T2. The corporation income tax account is separate, and a '+
       'T2 is due for every tax year until the corporation is formally '+
       'dissolved.</p></div>';
  }
  h+='<p>The nil T2 at '+PRICE_JS+' covers the corporation income tax '+
     'account only. GST/HST is a separate filing and is not part of the '+
     'fee.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className=ok?'ei-out ok':'ei-out no';
  out.innerHTML=h;
}
IDS.forEach(function(k){
  Array.prototype.forEach.call(document.querySelectorAll('input[name="'+k+'"]'),
    function(e){e.addEventListener('change',render);});});
render();
"""


TOOLS5 = [
 dict(slug='tax-years-since-incorporation-calculator',
  title='Tax Years Since Incorporation Calculator | Every Year and Its Due Date',
  h1_pre='Tax Years Since ', h1_span='Incorporation Calculator',
  h1='Tax Years Since Incorporation Calculator',
  eyebrow='Catch-Up', keyword='tax years since incorporation calculator',
  meta=('Enter the incorporation date and the first fiscal year-end to list '
        'every tax year the corporation has had, each filing date and which '
        'returns are now overdue.'),
  tags=['Lists every tax year', 'Names each filing date',
        'Counts what is overdue', 'No sign-up to use it'],
  form=tool('The incorporation date and the first fiscal year-end',
            [date('inc', 'Date of incorporation'),
             date('fye', 'First fiscal year-end')],
            'Enter both dates and every tax year since appears here.'),
  js=None,
  sections=[
   ('why', 'Why the Count Matters More Than the Years',
    '<p>A corporation has a tax year for every year it has existed, whether '
    'or not it traded, and a T2 is due for each one. The number people '
    'usually have in mind is how long ago they incorporated. The number that '
    'matters is how many tax years have ended since, because that is how '
    'many returns are owed.</p>\n'
    '<p>The two can differ, and a short first year is why. A corporation '
    'incorporated in March 2023 that chose a December 31 year-end had its '
    'first tax year end nine months later, in December 2023. By January 2027 '
    'it has four tax years behind it &#8212; 2023, 2024, 2025 and 2026 '
    '&#8212; and owes four returns, which is one more than the three years '
    'it feels like it has been going.</p>'),
   ('first', 'The First Year Is the One That Catches People',
    '<p>A first tax year runs from the date of incorporation to the first '
    'year-end chosen, and it may not exceed 53 weeks, which is 371 days. It '
    'is almost always shorter than twelve months, and it is still a full tax '
    'year needing a full return.</p>\n'
    '<p>Where the first year-end entered here produces a first year longer '
    'than 53 weeks, the year-end on record with the Canada Revenue Agency is '
    'probably not the one entered, and a transmission against the wrong '
    'year-end is rejected. The '
    + a(T + '53-week-first-tax-year-checker/', '53-week first tax year checker')
    + ' tests that one question on its own.</p>'),
   ('late', 'What an Overdue Year Actually Costs',
    '<p>Each outstanding nil year is ' + PRICE + ', and several years are '
    'transmitted in one sitting rather than one at a time.</p>\n'
    '<div class="ei-info"><p>' + QUAL + '</p></div>'),
   ('shape', 'How a Corporation Ends Up With More Tax Years Than It Expects',
    '<p>Four things add a tax year, and all four are common in corporations '
    'that were set up and then left alone.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">What happened</th>'
    '<th scope="col">Effect on the count</th>'
    '<th scope="col">Returns owed</th></tr></thead><tbody>\n'
    '<tr><td>Incorporated part-way through a year</td><td>A short first tax '
    'year, then full ones</td><td>One for the short year, one for each year '
    'after</td></tr>\n'
    '<tr><td>The fiscal year-end was changed</td><td>A short stub year at '
    'the changeover</td><td>One extra return for the stub period</td></tr>\n'
    '<tr><td>The corporation was dissolved mid-year</td><td>A short final '
    'year ending on the dissolution date</td><td>One final return</td></tr>\n'
    '<tr><td>The corporation amalgamated</td><td>Each predecessor&rsquo;s '
    'year ends the day before</td><td>One final return per '
    'predecessor</td></tr>\n'
    '</tbody></table>\n'
    '<p>Each of those is a separate tax year and needs its own return, and '
    'each nil one is ' + PRICE + '. None of them is covered by filing the '
    'year on either side of it.</p>\n'
    '<div class="ei-warn"><p>A corporation that holds shares, owns rental '
    'property or holds investments is not nil, and in any year it receives '
    'something there are figures to report. A Quebec corporation files a '
    'CO-17 as a separate return and an Alberta corporation files an AT1 the '
    'same way, neither of them covered by the fee here.</p></div>'),
  ],
  faq=[
   ('Does a Year With No Activity Still Count as a Tax Year?',
    'Yes. A tax year ends on the fiscal year-end whether anything happened '
    'in it or not, and a T2 is due for it.'),
   ('What If I Do Not Know the First Fiscal Year-End?',
    'It is on the first notice of assessment, and it is the year-end the '
    'Canada Revenue Agency holds. A transmission against a different '
    'year-end is rejected.'),
   ('Is There a Limit on How Many Years Can Be Filed at Once?',
    'No. Several years are transmitted in one sitting. Each nil year is '
    + PRICE + '.'),
   ('Does the Count Include the Year That Has Not Finished?',
    'No. The table lists tax years that have ended, because a return cannot '
    'be transmitted until the year is over. The year in progress is named '
    'separately with its own date.'),
   ('Do I Need Bookkeeping for Every One of Those Years?',
    'Not for a year with no transactions. A nil return is built from the '
    'corporation&rsquo;s own position, and whichever schedules that position '
    'requires are inside ' + PRICE + '.'),
  ]),

 dict(slug='days-overdue-calculator',
  title='Days Overdue Calculator | How Late a T2 Return Is',
  h1_pre='Days Overdue ', h1_span='Calculator',
  h1='Days Overdue Calculator',
  eyebrow='Lateness', keyword='days overdue calculator',
  meta=('Enter the fiscal year-end to see the filing date, how many calendar '
        'days a T2 is overdue and how many business days, counted on the '
        'same holiday calendar the deadline uses.'),
  tags=['Calendar and business days', 'Applies the holiday shift',
        'Says what a late nil year costs', 'No sign-up to use it'],
  form=tool('The fiscal year-end of the return in question',
            [date('fye', 'Fiscal year-end')],
            'Enter the year-end and the count appears here.'),
  js=None,
  sections=[
   ('two', 'Two Counts, Two Different Numbers',
    '<p>Calendar days and business days are not the same count, and the gap '
    'between them widens the longer a return sits. Thirty calendar days is '
    'about twenty business days. A year overdue is about 365 calendar days '
    'and about 250 business days.</p>\n'
    '<p>Both are shown because they answer different questions. Calendar '
    'days is how long the year has been open. Business days is how much '
    'working time has passed, which is the one that matters when a deadline '
    'on the other side of the lateness is being worked towards.</p>'),
   ('shift', 'The Count Starts From the Shifted Date',
    '<p>The filing date is six months after the fiscal year-end, and where '
    'that lands on a weekend or a statutory holiday it moves forward to the '
    'next business day. The count here starts from the moved date, not the '
    'unmoved one, so a return is never shown as overdue on a day the '
    'deadline had not actually passed.</p>\n'
    '<p>The '
    + a(T + 'due-date-weekend-holiday-shift-calculator/',
        'due date weekend and holiday shift calculator')
    + ' shows that step on its own, and the '
    + a(T + 'nil-t2-deadline-calculator/', 'nil T2 deadline calculator')
    + ' works the whole date out from a year-end.</p>'),
   ('cost', 'What Being Late Changes About the Fee',
    '<p>Nothing. A late nil year is ' + PRICE + ', the same as one filed on '
    'time, and it can be transmitted today.</p>\n'
    '<div class="ei-info"><p>' + QUAL + '</p></div>'),
   ('scale', 'What Each Stage of Lateness Changes',
    '<p>Lateness is not one state. What is at stake shifts as a year stays '
    'open, and the fee for the return itself does not move at any point on '
    'this list.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">How late</th>'
    '<th scope="col">What has changed</th>'
    '<th scope="col">Cost of the nil return</th></tr></thead><tbody>\n'
    '<tr><td>Before the filing date</td><td>Nothing. The return can be '
    'transmitted as soon as the year has ended</td><td>' + PRICE
    + '</td></tr>\n'
    '<tr><td>Days late</td><td>The year is open. A non-resident-owned '
    'corporation is already accruing $25.00 per day</td><td>' + PRICE
    + '</td></tr>\n'
    '<tr><td>Months late</td><td>The year stays open, and it blocks a '
    'clearance certificate and dissolution</td><td>' + PRICE + '</td></tr>\n'
    '<tr><td>A demand to file arrives</td><td>The demand sets its own '
    'deadline and opens the way to an arbitrary assessment</td><td>' + PRICE
    + '</td></tr>\n'
    '<tr><td>100 days late, non-resident-owned</td><td>The per-day charge '
    'has reached its $2,500.00 ceiling</td><td>' + PRICE + '</td></tr>\n'
    '<tr><td>Years late</td><td>Every year is still owed, and the oldest is '
    'no closer to closing itself</td><td>' + PRICE + ', for each year '
    'outstanding</td></tr>\n'
    '</tbody></table>\n'
    '<p>An unfiled year does not lapse and does not expire. It stays open '
    'until the return is filed, which is why the oldest year on the list is '
    'usually the one worth starting with.</p>'),
  ],
  faq=[
   ('Does an Unfiled Year Ever Expire?',
    'No. The year stays open until the return is filed. There is no point at '
    'which an unfiled T2 stops being owed.'),
   ('Why Are the Two Day Counts Different?',
    'Weekends and the statutory holidays treated as closed days are not '
    'business days, so the business-day count is always the smaller of the '
    'two.'),
   ('Is a Late Nil Return More Expensive?',
    'No. It is ' + PRICE + ' whether it is on time or years late.'),
   ('Should the Oldest Year Be Filed First?',
    'It is the usual order, because the oldest year is the one that has been '
    'open longest and the one most likely to have drawn correspondence. '
    'Several years are transmitted in one sitting either way.'),
   ('What If a Demand to File Has Already Arrived?',
    'A demand sets its own deadline, and that deadline is on the letter. '
    'Responding to it is a different task from simply filing late, and the '
    + a(G + 'cra-demand-to-file-response/', 'guide to responding to a demand')
    + ' sets out the order.'),
  ]),
]

TOOLS5 += [
 dict(slug='next-t2-due-date-checker',
  title='Next T2 Due Date Checker | Which Filing Date Comes Next',
  h1_pre='Next T2 ', h1_span='Due Date Checker',
  h1='Next T2 Due Date Checker',
  eyebrow='What Is Next', keyword='next t2 due date checker',
  meta=('Enter any one of the corporation fiscal year-ends to see which T2 '
        'filing date comes next, how many business days away it is and '
        'whether the return can be transmitted already.'),
  tags=['Works from any past year-end', 'Names the next date due',
        'Says whether it can be filed now', 'No sign-up to use it'],
  form=tool('Any one of the corporation&rsquo;s fiscal year-ends',
            [date('fye', 'A fiscal year-end')],
            'Enter a year-end and the next filing date appears here.'),
  js=None,
  sections=[
   ('which', 'The Next Date Due Is Usually the Last Year&rsquo;s',
    '<p>This is the part that trips people. The next T2 filing date is '
    'rarely the one belonging to the year-end coming up. It is almost always '
    'the one belonging to the year-end that has already passed, because the '
    'six months sits between them.</p>\n'
    '<p>A corporation with a June 30 year-end, asked in October which date '
    'is next, has December 31 next, for the year that ended in June. The '
    'following June is not the next filing date, it is the next '
    '<em>year-end</em>, and its return is not due until the December after '
    'that.</p>'),
   ('now', 'A Return Can Be Filed the Day the Year Ends',
    '<p>Nothing requires waiting for the filing date. A nil T2 can be '
    'transmitted as soon as the tax year has ended, and filing it the week '
    'the year closes closes the year.</p>\n'
    '<p>Where the year named here has already ended, the return is ready to '
    'go now and the date shown is simply the last day it can go without '
    'being late.</p>'),
   ('chain', 'One Date at a Time, Not a Schedule',
    '<p>This tool names the next date. The '
    + a(T + 'tax-years-since-incorporation-calculator/',
        'tax years since incorporation calculator')
    + ' lists every year and every date at once, which is the better view '
    'where more than one year is outstanding, and the '
    + a(T + 'days-overdue-calculator/', 'days overdue calculator')
    + ' counts how late a year already is.</p>'),
   ('worked', 'The Same Year-End Asked at Four Different Times',
    '<p>The answer depends on when the question is asked, which is why a '
    'remembered date goes stale. These four rows are one corporation with a '
    'June 30 year-end, asked in four different months.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Asked in</th>'
    '<th scope="col">Next filing date</th>'
    '<th scope="col">For the year ended</th>'
    '<th scope="col">Can it be filed today</th></tr></thead><tbody>\n'
    '<tr><td>August 2026</td><td>December 31, 2026</td><td>June 30, 2026</td>'
    '<td>Yes, that year has ended</td></tr>\n'
    '<tr><td>October 2026</td><td>December 31, 2026</td>'
    '<td>June 30, 2026</td><td>Yes, that year has ended</td></tr>\n'
    '<tr><td>February 2027</td><td>December 31, 2027</td>'
    '<td>June 30, 2027</td><td>No, that year has not ended</td></tr>\n'
    '<tr><td>August 2027</td><td>December 31, 2027</td>'
    '<td>June 30, 2027</td><td>Yes, that year has ended</td></tr>\n'
    '</tbody></table>\n'
    '<p>The February row is the one worth noting. The next filing date is '
    'eleven months away, but nothing can be transmitted yet, because the '
    'year it belongs to has not finished. The December 2026 date has already '
    'gone by, so if that return was not filed it is now overdue rather than '
    'upcoming.</p>\n'
    '<div class="ei-info"><p>Every one of these dates is six months after a '
    'fiscal year-end, moved to the next business day where it lands on a '
    'weekend or a statutory holiday. A nil return for any of these years is '
    + PRICE + '.</p></div>'),
  ],
  faq=[
   ('Why Is the Next Date for a Year That Has Already Ended?',
    'Because the six months runs after the year-end. The return for a year '
    'that ended in June is due in December, so between July and December the '
    'next date due belongs to the year just finished.'),
   ('Can a Return Be Filed Before the Due Date?',
    'Yes, and for a nil return there is no reason not to. It can be '
    'transmitted as soon as the tax year has ended.'),
   ('What If the Year-End Entered Is From Years Ago?',
    'It still works. Any past year-end establishes the month and day, and '
    'the tool steps forward from there to the next date that has not passed.'),
   ('Does the Date Move for a Weekend or a Holiday?',
    'Yes. Where six months after the year-end lands on a weekend or a '
    'statutory holiday, the filing date moves to the next business day.'),
   ('What If More Than One Year Is Outstanding?',
    'Then the next date is not the useful number. The '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' lists what is outstanding, and each nil year is ' + PRICE + '.'),
  ]),

 dict(slug='final-t2-return-due-date-calculator',
  title='Final T2 Return Due Date Calculator | Dissolution Filing Date',
  h1_pre='Final T2 Return ', h1_span='Due Date Calculator',
  h1='Final T2 Return Due Date Calculator',
  eyebrow='Dissolution', keyword='final t2 return due date calculator',
  meta=('Enter the last fiscal year-end and the date of dissolution to see '
        'the final tax year period, its length and the date the final T2 is '
        'due.'),
  tags=['Names the final tax year', 'Six months from dissolution',
        'Flags the short final year', 'No sign-up to use it'],
  form=tool('The last fiscal year-end and the date of dissolution',
            [date('fye', 'Last fiscal year-end'),
             date('dis', 'Date of dissolution')],
            'Enter both dates and the final return period appears here.'),
  js=None,
  sections=[
   ('ends', 'Dissolution Ends the Tax Year on Its Own Date',
    '<p>A corporation&rsquo;s last tax year does not run to its usual '
    'year-end. It ends on the date of dissolution, and the final T2 covers '
    'the period from the day after the previous year-end to that date.</p>\n'
    '<p>The six months then runs from the dissolution date. A corporation '
    'with a December 31 year-end dissolved in March does not file to '
    'December and does not get until the following June: it files to the '
    'March date and the return is due six months after that.</p>'),
   ('short', 'The Final Year Is Almost Always Short',
    '<p>Unless dissolution happens to fall on the year-end, the final tax '
    'year is a short one. A short year is a full tax year for every purpose '
    'that matters here: it needs its own return, it gets the same six '
    'months, and a nil one is ' + PRICE + '.</p>\n'
    '<p>The '
    + a(T + 'short-tax-year-deadline-calculator/',
        'short tax year deadline calculator')
    + ' works out the filing date for any short period on its own.</p>'),
   ('before', 'Every Earlier Year Has to Be In First',
    '<p>The final return is the last one, not the only one. Every earlier '
    'tax year still has to be filed, nil years included, and an unfiled year '
    'blocks a clearance certificate and blocks the dissolution behind '
    'it.</p>\n'
    '<div class="ei-info"><p>' + QUAL + '</p></div>\n'
    '<p>The '
    + a(T + 'dissolution-readiness-checker/', 'dissolution readiness checker')
    + ' runs the whole list, and the '
    + a(T + 'clearance-certificate-requirement-checker/',
        'clearance certificate requirement checker')
    + ' covers the certificate itself.</p>'),
   ('order', 'The Order the Dates Fall In',
    '<p>Four dates matter on a dissolution, and they do not fall in the '
    'order people expect. This is one corporation with a December 31 '
    'year-end, dissolved on March 15, 2027.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Date</th>'
    '<th scope="col">What it is</th>'
    '<th scope="col">What is owed</th></tr></thead><tbody>\n'
    '<tr><td>December 31, 2026</td><td>The last ordinary fiscal '
    'year-end</td><td>A T2 for the year ended that day, due June 30, '
    '2027</td></tr>\n'
    '<tr><td>January 1, 2027</td><td>The final tax year begins</td>'
    '<td>Nothing yet</td></tr>\n'
    '<tr><td>March 15, 2027</td><td>Dissolution, and the final tax year '
    'ends</td><td>A final T2 for January 1 to March 15, due September 15, '
    '2027</td></tr>\n'
    '<tr><td>September 15, 2027</td><td>The final T2 filing date</td>'
    '<td>The last return the corporation ever files</td></tr>\n'
    '</tbody></table>\n'
    '<p>Two returns, not one, and the ordinary year&rsquo;s return falls due '
    'in June, before the final one. Each nil return is ' + PRICE + '. A '
    'corporation that held investments or rental property, or that paid or '
    'received a dividend in either period, is not nil for that period.</p>\n'
    '<div class="ei-warn"><p>Distributing property before the final return '
    'is settled leaves the person who distributed it personally exposed for '
    'amounts the corporation turns out to owe, which is what a clearance '
    'certificate is for.</p></div>'),
  ],
  faq=[
   ('Does the Final Return Go to the Usual Year-End?',
    'No. The tax year ends on the date of dissolution, and the return covers '
    'the period to that date.'),
   ('Is the Final Return Due Sooner Because the Year Was Short?',
    'No. Six months runs from the year-end whatever the length of the '
    'period, so a short final year gets the same six months.'),
   ('How Many Returns Does a Mid-Year Dissolution Mean?',
    'Usually two: the ordinary year that ended before it, and the short '
    'final year ending on the dissolution date. Each nil one is '
    + PRICE + '.'),
   ('Can a Corporation Dissolve With Years Unfiled?',
    'An unfiled year blocks a clearance certificate and blocks the '
    'dissolution. The outstanding years have to be filed first.'),
   ('Is the Final T2 Different From an Ordinary One?',
    'It is the same return for a shorter period. What changes is the period '
    'it covers and the date it is due, not the form or what it costs.'),
  ]),
]

TOOLS5 += [
 dict(slug='amalgamation-t2-due-date-calculator',
  title='Amalgamation T2 Due Date Calculator | Predecessor Final Returns',
  h1_pre='Amalgamation T2 ', h1_span='Due Date Calculator',
  h1='Amalgamation T2 Due Date Calculator',
  eyebrow='Amalgamation', keyword='amalgamation t2 due date calculator',
  meta=('Enter a predecessor fiscal year-end and the amalgamation date to '
        'see the predecessor final tax year, the date its return is due and '
        'when the new corporation first tax year begins.'),
  tags=['One final return per predecessor', 'The year ends the day before',
        'Names the new first year window', 'No sign-up to use it'],
  form=tool('A predecessor&rsquo;s last fiscal year-end and the '
            'amalgamation date',
            [date('fye', 'Predecessor&rsquo;s last fiscal year-end'),
             date('amal', 'Date of amalgamation')],
            'Enter both dates and the periods appear here.'),
  js=None,
  sections=[
   ('day', 'The Year Ends the Day Before, Not on the Day',
    '<p>An amalgamation ends each predecessor corporation&rsquo;s tax year '
    'on the day before the amalgamation date. The new corporation&rsquo;s '
    'first tax year begins on the amalgamation date itself. The two periods '
    'do not overlap and there is no gap between them.</p>\n'
    '<p>That one-day offset is the whole reason this calculator exists. A '
    'final return filed to the amalgamation date is filed to a year-end the '
    'Canada Revenue Agency does not hold, and the transmission is rejected '
    'for the year-end rather than for anything in the return.</p>'),
   ('each', 'One Final Return for Each Predecessor',
    '<p>Every predecessor files its own final return for its own period. An '
    'amalgamation of two corporations means two final returns, an '
    'amalgamation of three means three, and each one is a separate '
    'filing.</p>\n'
    '<p>Each predecessor may also have its own year-end, so the periods can '
    'be different lengths even though they all end on the same day. Each nil '
    'final return is ' + PRICE + '.</p>'),
   ('new', 'The New Corporation Starts Its Own Clock',
    '<p>The corporation that comes out of an amalgamation is a new '
    'corporation for tax year purposes, and its first tax year may not '
    'exceed 53 weeks, which is 371 days from the amalgamation date.</p>\n'
    '<p>That first year then has its own return, due six months after '
    'whichever year-end it chooses inside that window. The '
    + a(T + '53-week-first-tax-year-checker/',
        '53-week first tax year checker')
    + ' tests a proposed first year-end against the limit.</p>'),
   ('both', 'What Each Corporation Owes and When',
    '<p>Two predecessors with different year-ends, amalgamating on July 1, '
    '2027. Three corporations appear on this list and three sets of '
    'obligations come out of it.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Corporation</th>'
    '<th scope="col">Final or first tax year</th>'
    '<th scope="col">Return due</th></tr></thead><tbody>\n'
    '<tr><td>Predecessor A, December 31 year-end</td><td>January 1, 2027 to '
    'June 30, 2027</td><td>December 31, 2027</td></tr>\n'
    '<tr><td>Predecessor B, March 31 year-end</td><td>April 1, 2027 to June '
    '30, 2027</td><td>December 31, 2027</td></tr>\n'
    '<tr><td>The amalgamated corporation</td><td>Begins July 1, 2027, first '
    'year-end no later than July 5, 2028</td><td>Six months after whichever '
    'year-end it chooses</td></tr>\n'
    '</tbody></table>\n'
    '<p>Both predecessor years end June 30, 2027, the day before the '
    'amalgamation, so both final returns fall due on the same date even '
    'though the periods are different lengths. Neither one runs to its own '
    'usual year-end.</p>\n'
    '<div class="ei-warn"><p>A predecessor that held shares, owned rental '
    'property or paid or received a dividend in its final period is not nil '
    'for that period. A Quebec corporation files a CO-17 as a separate '
    'return and an Alberta corporation files an AT1 the same way, neither of '
    'them covered by the fee here.</p></div>'),
  ],
  faq=[
   ('Does the Predecessor File to the Amalgamation Date?',
    'No. The tax year ends the day before the amalgamation date. Filing to '
    'the amalgamation date itself is filing to the wrong year-end.'),
   ('How Many Final Returns Does an Amalgamation Need?',
    'One for each predecessor corporation. Each nil one is ' + PRICE + '.'),
   ('Do the Predecessors Have to Share a Year-End?',
    'No. They can have different year-ends and therefore different period '
    'lengths, but all the final periods end on the same day, the day before '
    'the amalgamation.'),
   ('Does the New Corporation Inherit the Old Year-End?',
    'It chooses its own first year-end, and that first tax year may not '
    'exceed 53 weeks from the amalgamation date.'),
   ('Are Earlier Years of a Predecessor Still Owed?',
    'Yes. The final return is the last one, not the only one. Any earlier '
    'unfiled year is still owed and is still ' + PRICE + ' for a nil year.'),
  ]),

 dict(slug='short-tax-year-deadline-calculator',
  title='Short Tax Year Deadline Calculator | Filing Date for a Stub Period',
  h1_pre='Short Tax Year ', h1_span='Deadline Calculator',
  h1='Short Tax Year Deadline Calculator',
  eyebrow='Short Year', keyword='short tax year deadline calculator',
  meta=('Enter the first and last day of a short tax year to see its length '
        'in days and weeks and the date the return is due, six months after '
        'the year-end as for any other year.'),
  tags=['Any period, any length', 'Six months is unchanged',
        'Flags a period over 53 weeks', 'No sign-up to use it'],
  form=tool('The first and last day of the tax year',
            [date('st', 'First day of the tax year'),
             date('en', 'Last day of the tax year')],
            'Enter both dates and the filing date appears here.'),
  js=None,
  sections=[
   ('same', 'A Short Year Does Not Get a Short Deadline',
    '<p>The assumption worth correcting first: a shorter tax year does not '
    'come with a proportionally shorter filing window. Six months runs from '
    'the year-end whatever the length of the period behind it.</p>\n'
    '<p>A two-month stub period and a twelve-month year both get six months '
    'from their year-end. The stub period does not get one month because it '
    'was one-sixth the length, and it does not get longer either.</p>'),
   ('when', 'Where Short Years Come From',
    '<p>Four situations produce one. A first tax year running from '
    'incorporation to the first year-end chosen. A change of fiscal year-end '
    'leaving a stub period at the changeover. A dissolution ending the year '
    'on its own date. An amalgamation ending a predecessor&rsquo;s year the '
    'day before.</p>\n'
    '<p>In all four the short period is a full tax year for filing '
    'purposes, needing its own return at ' + PRICE + ' for a nil one.</p>'),
   ('limit', 'The 53-Week Limit Applies to a First Year',
    '<p>A first tax year may not exceed 53 weeks, which is 371 days counted '
    'from the date of incorporation to the year-end. A later tax year may '
    'run a full twelve months, so the limit only bites on a first year or on '
    'the first year of a corporation coming out of an amalgamation.</p>\n'
    '<p>Where the period entered here is longer than 53 weeks and it is a '
    'first year, the year-end is probably not the one on record. The '
    + a(T + '53-week-first-tax-year-checker/',
        '53-week first tax year checker')
    + ' tests that question on its own.</p>'),
   ('four', 'Four Short Years, Four Filing Dates',
    '<p>Each row is a real short period of the kind that turns up, with its '
    'length and the date its return falls due. The six months is the same in '
    'every row.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Why the year is '
    'short</th><th scope="col">Period</th><th scope="col">Length</th>'
    '<th scope="col">Return due</th></tr></thead><tbody>\n'
    '<tr><td>First year after incorporation</td><td>March 12, 2026 to '
    'December 31, 2026</td><td>295 days</td><td>June 30, 2027</td></tr>\n'
    '<tr><td>Stub period on a year-end change</td><td>January 1, 2027 to '
    'March 31, 2027</td><td>90 days</td><td>September 30, 2027</td></tr>\n'
    '<tr><td>Final year on dissolution</td><td>April 1, 2027 to August 20, '
    '2027</td><td>142 days</td><td>February 22, 2028</td></tr>\n'
    '<tr><td>Predecessor year on amalgamation</td><td>January 1, 2027 to '
    'June 30, 2027</td><td>181 days</td><td>December 31, 2027</td></tr>\n'
    '</tbody></table>\n'
    '<p>The dissolution row shows the shift at work, and it shows it twice. '
    'Six months after August 20, 2027 is February 20, 2028, a Sunday, so the '
    'date moves to the Monday &#8212; and that Monday is Family Day, so it '
    'moves again, to Tuesday February 22. The shift keeps stepping forward '
    'until it lands on a day that is open. The '
    + a(T + 'due-date-weekend-holiday-shift-calculator/',
        'due date weekend and holiday shift calculator')
    + ' shows that step on its own.</p>\n'
    '<div class="ei-info"><p>Two year-ends in one calendar year means two '
    'returns, and each nil one is ' + PRICE + '. A stub period is never '
    'folded into the year on either side of it.</p></div>'),
  ],
  faq=[
   ('Is a Short Year Filed Together With the Next Full Year?',
    'No. It is a separate tax year and needs its own return. Two year-ends '
    'in one calendar year means two returns.'),
   ('Does a Short Year Cost Less to File?',
    'No. A nil return is ' + PRICE + ' whatever the length of the period it '
    'covers.'),
   ('Can a Tax Year Be Longer Than Twelve Months?',
    'A first tax year may not exceed 53 weeks, which is 371 days. Later '
    'years run to the fiscal year-end on record.'),
   ('What Makes a Period a Stub Period?',
    'A change of fiscal year-end leaves a gap between the old year-end and '
    'the new one. That gap is a tax year of its own.'),
   ('Does the Filing Date Still Move for a Weekend?',
    'Yes. The shift applies to a short year exactly as it does to a full '
    'one, so six months landing on a Saturday moves to the Monday.'),
  ]),
]

TOOLS5 += [
 dict(slug='nil-return-late-penalty-checker',
  title='Nil Return Late Penalty Checker | What Applies to a Late Nil Year',
  h1_pre='Nil Return ', h1_span='Late Penalty Checker',
  h1='Nil Return Late Penalty Checker',
  eyebrow='Late Filing', keyword='nil return late penalty checker',
  meta=('Three questions that set out what applies to a late nil T2: why the '
        'percentage penalty has nothing to apply to, and what still follows '
        'from leaving the year unfiled.'),
  tags=['Three questions', 'The full qualification, not a slogan',
        'Separates resident from non-resident', 'No sign-up to use it'],
  form=tool('Three questions about the year and the corporation',
            [yn('nil', 'Was the year truly nil, with no revenue, no expenses '
                       'and nothing bought or sold'),
             yn('nr', 'Is the corporation non-resident-owned'),
             yn('dem', 'Has the Canada Revenue Agency issued a demand to '
                       'file')],
            'Answer all three and the position appears here.'),
  js=None,
  sections=[
   ('percent', 'Why the Percentage Has Nothing to Apply To',
    '<p>The late-filing penalty on a T2 is a percentage of the tax owing. '
    'That is the mechanism, and it is the whole reason a nil year behaves '
    'differently from a year with a balance: a percentage of $0.00 is '
    '$0.00.</p>\n'
    '<p>That is the first half of the position and not the whole of it. What '
    'follows is the whole of it, and the second half is the half that '
    'matters once a year has been sitting unfiled for a while.</p>\n'
    '<div class="ei-info"><p>' + QUAL + '</p></div>'),
   ('open', 'What an Unfiled Year Does Instead',
    '<p>The consequences of a late nil year are not financial at first. They '
    'are that the year stays open and keeps being a year that is open.</p>\n'
    '<p>An open year invites a demand to file, and a demand opens the way to '
    'an arbitrary assessment, in which the Canada Revenue Agency assesses a '
    'figure of its own rather than waiting for the return. It blocks a '
    'clearance certificate, which blocks dissolution. None of that resolves '
    'itself with time.</p>'),
   ('nonres', 'The One Charge That Does Not Depend on Tax Owing',
    '<p>A non-resident-owned corporation is charged $25.00 per day for an '
    'unfiled return, up to $2,500.00. That charge runs on the lateness '
    'itself, so a nil year with no tax owing accrues it exactly as a year '
    'with a balance would, and it reaches its ceiling after 100 days.</p>\n'
    '<p>The '
    + a(T + 'non-resident-t2-penalty-calculator/',
        'non-resident T2 penalty calculator')
    + ' works that figure out from the dates.</p>'),
   ('side', 'A Nil Year and a Year With Tax Owing, Side by Side',
    '<p>The difference is not in the form, the deadline or the fee. It is in '
    'whether there is a figure for a percentage to apply to.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">What follows from '
    'filing late</th><th scope="col">A true nil year</th>'
    '<th scope="col">A year with tax owing</th></tr></thead><tbody>\n'
    '<tr><td>Percentage late-filing penalty</td><td>Nothing for the '
    'percentage to apply to, because the corporation owes $0.00</td>'
    '<td>Applies to the tax owing</td></tr>\n'
    '<tr><td>The year stays open</td><td>Yes</td><td>Yes</td></tr>\n'
    '<tr><td>Invites a demand to file</td><td>Yes</td><td>Yes</td></tr>\n'
    '<tr><td>Opens the way to an arbitrary assessment</td><td>Yes</td>'
    '<td>Yes</td></tr>\n'
    '<tr><td>Blocks a clearance certificate and dissolution</td><td>Yes</td>'
    '<td>Yes</td></tr>\n'
    '<tr><td>$25.00 per day up to $2,500.00 where non-resident-owned</td>'
    '<td>Yes</td><td>Yes</td></tr>\n'
    '<tr><td>Cost of the return itself</td><td>' + PRICE + '</td>'
    '<td>Not a nil return, so not this fee</td></tr>\n'
    '</tbody></table>\n'
    '<p>Of the six rows describing what follows from filing late, five are '
    'identical down both columns. The percentage is the only consequence on '
    'which a nil year sits anywhere different, and it is the one people '
    'remember as though it were the whole list. The last row is not a '
    'consequence at all, it is the fee.</p>\n'
    '<div class="ei-warn"><p>' + NOT_NIL + '</p></div>'),
  ],
  faq=[
   ('Is a Late Nil Return Free of Consequences?',
    'No. ' + QUAL),
   ('Does the Fee Go Up Because the Year Is Late?',
    'No. A late nil year is ' + PRICE + ', the same as one filed on time.'),
   ('How Long Does the Non-Resident Charge Keep Running?',
    'It accrues at $25.00 per day up to a ceiling of $2,500.00, which it '
    'reaches after 100 days.'),
   ('What Changes Once a Demand to File Arrives?',
    'The demand sets its own deadline, stated on the letter, and it opens '
    'the way to an arbitrary assessment. The '
    + a(G + 'cra-demand-to-file-response/',
        'guide to responding to a demand to file')
    + ' sets out what to do in what order.'),
   ('What If the Year Turns Out Not to Have Been Nil?',
    'Then the percentage has a figure to apply to and this is not the right '
    'tool. ' + NOT_NIL),
  ]),

 dict(slug='clearance-certificate-requirement-checker',
  title='Clearance Certificate Requirement Checker | Before Assets Are Distributed',
  h1_pre='Clearance Certificate ', h1_span='Requirement Checker',
  h1='Clearance Certificate Requirement Checker',
  eyebrow='Clearance', keyword='clearance certificate requirement checker',
  meta=('Three questions that set out whether a clearance certificate '
        'belongs in the plan and what has to be filed before one can be '
        'issued.'),
  tags=['Three questions', 'Names the actual blocker',
        'Covers personal exposure', 'No sign-up to use it'],
  form=tool('Three questions about the wind-down',
            [yn('dist', 'Will property be distributed to shareholders'),
             yn('dis', 'Is the corporation being dissolved'),
             yn('unf', 'Is any tax year still unfiled')],
            'Answer all three and the position appears here.'),
  js=None,
  sections=[
   ('what', 'What the Certificate Is For',
    '<p>A clearance certificate confirms the Canada Revenue Agency has no '
    'further claim against the corporation before its property is handed '
    'out. It is not a filing and it is not a tax return. It is a '
    'confirmation sought at the end, once everything that had to be filed '
    'has been.</p>\n'
    '<p>Its purpose is personal rather than corporate. Distributing property '
    'without one leaves the person who distributed it exposed for amounts '
    'the corporation turns out to owe, and the corporation is by then gone '
    'or going.</p>'),
   ('block', 'An Unfiled Year Is the Usual Blocker',
    '<p>A certificate cannot be issued while a tax year is outstanding, '
    'because the position it is confirming is not yet known. That applies to '
    'nil years exactly as to any other: a year with nothing in it still has '
    'to be filed before it stops being outstanding.</p>\n'
    '<p>The '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' lists which years are owed and the '
    + a(T + 'tax-years-since-incorporation-calculator/',
        'tax years since incorporation calculator')
    + ' lists every year the corporation has ever had. Each outstanding nil '
    'year is ' + PRICE + ', and several are transmitted in one '
    'sitting.</p>\n'
    '<div class="ei-info"><p>' + QUAL + '</p></div>'),
   ('order', 'The Order These Steps Fall In',
    '<p>Filing comes first, the certificate second, distribution third and '
    'dissolution last. Taken out of order the sequence stalls: a '
    'distribution made before the certificate cannot be undone by getting '
    'the certificate afterwards.</p>\n'
    '<p>The '
    + a(T + 'dissolution-readiness-checker/', 'dissolution readiness checker')
    + ' runs the full list, and the '
    + a(T + 'final-t2-return-due-date-calculator/',
        'final T2 return due date calculator')
    + ' dates the last return.</p>'),
   ('seq', 'Each Step, What It Needs First and What Goes Wrong Without It',
    '<p>The sequence only works in one direction. This is what each step '
    'depends on and what happens when it is taken early.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Step</th>'
    '<th scope="col">Cannot happen until</th>'
    '<th scope="col">Taken out of order</th></tr></thead><tbody>\n'
    '<tr><td>File every outstanding tax year</td><td>Nothing. This is the '
    'first step</td><td>Everything after it stalls</td></tr>\n'
    '<tr><td>File the final T2 for the period ending on dissolution</td>'
    '<td>The dissolution date is known</td><td>The corporation has an '
    'unfiled final year</td></tr>\n'
    '<tr><td>Request the clearance certificate</td><td>Every year, the final '
    'one included, is filed</td><td>The request cannot be granted while a '
    'year is outstanding</td></tr>\n'
    '<tr><td>Distribute property to shareholders</td><td>The certificate is '
    'issued</td><td>Personal exposure for whatever the corporation turns out '
    'to owe</td></tr>\n'
    '<tr><td>Complete the dissolution</td><td>The property is '
    'distributed</td><td>Property is left in a corporation that no longer '
    'exists, and recovering it means reviving the corporation '
    'first</td></tr>\n'
    '</tbody></table>\n'
    '<p>The second row is the one most often missed. The final T2 covers the '
    'period ending on the dissolution date, so it cannot be filed before '
    'that date is fixed, and the certificate cannot be requested before that '
    'return is in.</p>'),
  ],
  faq=[
   ('Is a Clearance Certificate Always Needed?',
    'It belongs in any wind-down where property is being distributed, '
    'because that is the step it protects. With no distribution and no '
    'dissolution there is nothing for it to clear.'),
   ('Do Nil Years Have to Be Filed First?',
    'Yes. A nil year is an outstanding year until it is filed, and an '
    'outstanding year blocks the certificate.'),
   ('Can Property Be Distributed First and Cleared Afterwards?',
    'The exposure arises at the distribution, so a certificate obtained '
    'afterwards does not undo it. The order is the point.'),
   ('How Many Returns Does a Dissolution Need?',
    'Every unfiled earlier year, plus a final return for the short period '
    'ending on the dissolution date. Each nil one is ' + PRICE + '.'),
   ('Does the Certificate Cover the Annual Return as Well?',
    'No. The federal and Ontario annual returns go to a registry rather '
    'than to the Canada Revenue Agency and are separate from this. The '
    + a(T + 'inactive-corporation-filing-checker/',
        'inactive corporation filing checker')
    + ' sets out which filings go where.'),
  ]),
]

TOOLS5 += [
 dict(slug='payroll-nil-remittance-checker',
  title='Payroll Nil Remittance Checker | An Open Account With No Wages',
  h1_pre='Payroll Nil ', h1_span='Remittance Checker',
  h1='Payroll Nil Remittance Checker',
  eyebrow='Payroll', keyword='payroll nil remittance checker',
  meta=('Three questions that set out whether an open payroll account still '
        'needs nil remittances, what the nil T2 does not cover and how the '
        'account is closed.'),
  tags=['Three questions', 'Open is not the same as dormant',
        'Says what the fee does not cover', 'No sign-up to use it'],
  form=tool('Three questions about the payroll account',
            [yn('acct', 'Is there a payroll account open on the Business '
                        'Number'),
             yn('wag', 'Were any wages or salary paid in the period'),
             yn('clo', 'Is the intention to close the account')],
            'Answer all three and the payroll position appears here.'),
  js=None,
  sections=[
   ('silence', 'Reporting Nothing Is Not the Same as Reporting Nil',
    '<p>An open payroll account expects to hear from the corporation on each '
    'of its due dates. Where no wages were paid, what it expects to hear is '
    'a nil remittance, and that is a positive statement rather than an '
    'absence of one.</p>\n'
    '<p>Silence on an open account is what draws correspondence. The account '
    'has no way to tell the difference between a corporation that paid '
    'nothing and a corporation that paid something and did not report it, so '
    'it assumes the second.</p>'),
   ('separate', 'The Nil T2 Does Not Touch It',
    '<p>Payroll and corporation income tax are separate programme accounts '
    'under one Business Number, each with its own filings. Filing the nil T2 '
    'settles the corporation income tax account for that tax year and does '
    'nothing at all about payroll.</p>\n'
    '<p>The fee of ' + PRICE + ' covers the corporation income tax account '
    'only. The '
    + a(T + 'business-number-status-checker/', 'Business Number status checker')
    + ' sets out which accounts are open and what each one still needs.</p>'),
   ('end', 'Closing It Rather Than Keeping Up With It',
    '<p>Where the account is not going to be used again, the obligation ends '
    'by closing the account rather than by meeting it indefinitely. Form '
    'RC145 closes a Business Number programme account once that account has '
    'its own final remittance in.</p>\n'
    '<p>An account left open can keep drawing correspondence after the '
    'corporation itself is gone, which is the usual reason a closed-down '
    'corporation keeps hearing from the Canada Revenue Agency.</p>'),
   ('three', 'Three Situations and What Each One Owes',
    '<p>The answers split three ways, and the middle one is the case most '
    'people are in and least expect.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Situation</th>'
    '<th scope="col">Payroll obligation</th>'
    '<th scope="col">Effect on the tax year</th></tr></thead><tbody>\n'
    '<tr><td>No payroll account on record</td><td>Nothing to remit and '
    'nothing to close</td><td>None. The year can still be nil</td></tr>\n'
    '<tr><td>Account open, no wages paid</td><td>A nil remittance on the '
    'account&rsquo;s own cycle, for as long as it stays open</td>'
    '<td>None. The year can still be nil</td></tr>\n'
    '<tr><td>Account open, wages paid</td><td>A real remittance of source '
    'deductions, not a nil one</td><td>Wages are an expense, so the year is '
    'not nil</td></tr>\n'
    '</tbody></table>\n'
    '<p>The third row has two consequences rather than one. The payroll '
    'remittance is real, and the tax year it falls in is not a nil year '
    'either, because paying wages is incurring an expense.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Account</th>'
    '<th scope="col">What it carries</th>'
    '<th scope="col">Covered by the fee here</th></tr></thead><tbody>\n'
    '<tr><td>Corporation income tax</td><td>One T2 for every tax year until '
    'the corporation is formally dissolved</td><td>Yes</td></tr>\n'
    '<tr><td>Payroll</td><td>A remittance on its own cycle, nil ones '
    'included, until closed with Form RC145</td><td>No</td></tr>\n'
    '<tr><td>GST/HST</td><td>A return on its own cycle, nil ones included, '
    'until closed with Form RC145</td><td>No</td></tr>\n'
    '</tbody></table>'),
  ],
  faq=[
   ('Does an Open Payroll Account With No Employees Still Need Filing?',
    'Yes. While the account is open it expects a remittance on its own '
    'cycle, and where no wages were paid that remittance is a nil one.'),
   ('Does Filing the Nil T2 Cover the Payroll Account?',
    'No. They are separate programme accounts. The fee of ' + PRICE
    + ' covers the corporation income tax account only.'),
   ('How Is a Payroll Account Closed?',
    'With Form RC145, once the account has its own final remittance in.'),
   ('Does Paying One Month of Wages Make the Year Not Nil?',
    'Yes. Wages are an expense, so the tax year they fall in has a figure to '
    'report and is not a nil year.'),
   ('What If the Account Was Opened and Never Used?',
    'It is still open, so it still carries the obligation. Closing it with '
    'Form RC145 is what ends that.'),
  ]),

 dict(slug='gst-hst-account-closure-checker',
  title='GST/HST Account Closure Checker | Is the Account Ready for RC145',
  h1_pre='GST/HST Account ', h1_span='Closure Checker',
  h1='GST/HST Account Closure Checker',
  eyebrow='GST/HST', keyword='gst hst account closure checker',
  meta=('Three questions that set out whether a GST/HST account is ready to '
        'close with Form RC145, what has to be filed first and what closing '
        'it does not do.'),
  tags=['Three questions', 'Names what has to be filed first',
        'Says what closing it does not do', 'No sign-up to use it'],
  form=tool('Three questions about the GST/HST account',
            [yn('acct', 'Is there a GST/HST account open on the Business '
                        'Number'),
             yn('sales', 'Are taxable sales still being made'),
             yn('fin', 'Has the final return been filed on the account')],
            'Answer all three and the closure position appears here.'),
  js=None,
  sections=[
   ('first', 'The Final Return Comes Before the Closure',
    '<p>Form RC145 closes a Business Number programme account, but it does '
    'not clear what the account was already waiting for. The account has to '
    'have its own final return in first, and until then it stays open and '
    'keeps expecting a return on its own cycle, nil ones included.</p>\n'
    '<p>That is the order, and taking it the other way round is the usual '
    'reason an account that was supposed to be closed is still sending '
    'letters.</p>'),
   ('notthet2', 'Closing It Does Nothing About the T2',
    '<p>The corporation income tax account is a different programme account '
    'under the same Business Number. Closing GST/HST leaves it untouched, '
    'and a T2 is due for every tax year until the corporation is formally '
    'dissolved.</p>\n'
    '<p>The '
    + a(T + 'gst-hst-nil-filing-checker/', 'GST/HST nil filing checker')
    + ' covers whether nil returns are owed on an open account, and the '
    + a(T + 'business-number-status-checker/', 'Business Number status checker')
    + ' sets out every account at once.</p>'),
   ('still', 'Still Trading Means It Is Not Ready',
    '<p>Where taxable sales are still being made the account is doing its '
    'job and closing it would be wrong. It also answers a different '
    'question: a corporation making sales has revenue, so the tax year those '
    'sales fall in is not a nil year.</p>\n'
    '<p>' + NOT_NIL + '</p>'),
   ('states', 'Four States and What Each One Needs',
    '<p>The three answers produce four distinct positions, and only one of '
    'them is ready for Form RC145.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">State</th>'
    '<th scope="col">Ready for Form RC145</th>'
    '<th scope="col">What is needed next</th></tr></thead><tbody>\n'
    '<tr><td>No GST/HST account on record</td><td>Nothing to close</td>'
    '<td>Nothing on this account</td></tr>\n'
    '<tr><td>Open, taxable sales still being made</td><td>No</td>'
    '<td>Keep filing on the account&rsquo;s own cycle. The tax year is not '
    'nil either</td></tr>\n'
    '<tr><td>Open, no sales, returns outstanding</td><td>No</td>'
    '<td>File the final return on the account, then close it</td></tr>\n'
    '<tr><td>Open, no sales, final return filed</td><td>Yes</td>'
    '<td>Form RC145</td></tr>\n'
    '</tbody></table>\n'
    '<p>In every one of these states the T2 position is unchanged. The '
    'corporation income tax account carries one return for every tax year '
    'until dissolution, and ' + PRICE + ' covers that account only.</p>\n'
    '<div class="ei-warn"><p>A Quebec corporation files a CO-17 as a '
    'separate return, and an Alberta corporation files an AT1 the same way. '
    'Neither is covered by the fee here, and neither is affected by closing '
    'a GST/HST account.</p></div>'),
  ],
  faq=[
   ('Can the Account Be Closed With Returns Outstanding?',
    'No. The account needs its own final return in first, and then Form '
    'RC145 closes it.'),
   ('Does Closing GST/HST End the T2 Obligation?',
    'No. They are separate programme accounts. A T2 is due for every tax '
    'year until the corporation is formally dissolved.'),
   ('What If the Account Was Registered and Never Used?',
    'It is still open, so it still expects a return on its own cycle. A nil '
    'return on the account, then Form RC145, is what ends that.'),
   ('Is the GST/HST Return Covered by the Fee?',
    'No. The fee of ' + PRICE + ' covers the corporation income tax '
    'account only. GST/HST is a separate filing.'),
   ('Does Making Sales Affect the T2 as Well?',
    'Yes. A corporation making taxable sales has revenue, so the tax year '
    'those sales fall in is not a nil year. ' + NOT_NIL),
  ]),
]


for t, js in zip(TOOLS5, [T21_JS, T22_JS, T23_JS, T24_JS, T25_JS, T26_JS,
                          T27_JS, T28_JS, T29_JS, T30_JS]):
    t['js'] = js if js.startswith(PRELUDE) else PRELUDE + js

ORDER5 = ORDER4 + [t['slug'] for t in TOOLS5]
LINK_TITLE5 = dict(LINK_TITLE4, **{
 'tax-years-since-incorporation-calculator':
     'Tax years since incorporation calculator',
 'days-overdue-calculator': 'Days overdue calculator',
 'next-t2-due-date-checker': 'Next T2 due date checker',
 'final-t2-return-due-date-calculator':
     'Final T2 return due date calculator',
 'amalgamation-t2-due-date-calculator':
     'Amalgamation T2 due date calculator',
 'short-tax-year-deadline-calculator':
     'Short tax year deadline calculator',
 'nil-return-late-penalty-checker': 'Nil return late penalty checker',
 'clearance-certificate-requirement-checker':
     'Clearance certificate requirement checker',
 'payroll-nil-remittance-checker': 'Payroll nil remittance checker',
 'gst-hst-account-closure-checker': 'GST/HST account closure checker',
})

# Indices into ORDER5. 0 to 19 are the twenty tools already live.
SIBLINGS5 = {20: [12, 3, 5],   21: [0, 19, 12],  22: [0, 19, 21],
             23: [14, 27, 25], 24: [5, 25, 10],  25: [5, 0, 23],
             26: [13, 21, 12], 27: [14, 23, 12], 28: [15, 9, 16],
             29: [9, 15, 28]}

GUIDES5 = {
 'tax-years-since-incorporation-calculator': [
   ('catch-up-unfiled-corporate-tax-returns',
    'The complete guide to catching up unfiled corporate tax returns'),
   ('first-year-t2-filing', 'The complete guide to first-year T2 filing')],
 'days-overdue-calculator': [
   ('t2-late-filing-penalties', 'T2 late filing penalties'),
   ('catch-up-unfiled-corporate-tax-returns',
    'The complete guide to catching up unfiled corporate tax returns')],
 'next-t2-due-date-checker': [
   ('how-to-file-a-nil-t2-return', 'How to file a nil T2 return')],
 'final-t2-return-due-date-calculator': [
   ('final-t2-and-dissolution', 'The final T2 and dissolution')],
 'amalgamation-t2-due-date-calculator': [
   ('final-t2-and-dissolution', 'The final T2 and dissolution'),
   ('first-year-t2-filing', 'The complete guide to first-year T2 filing')],
 'short-tax-year-deadline-calculator': [
   ('first-year-t2-filing', 'The complete guide to first-year T2 filing')],
 'nil-return-late-penalty-checker': [
   ('t2-late-filing-penalties', 'T2 late filing penalties'),
   ('cra-demand-to-file-response', 'Responding to a CRA demand to file')],
 'clearance-certificate-requirement-checker': [
   ('final-t2-and-dissolution', 'The final T2 and dissolution')],
 'payroll-nil-remittance-checker': [
   ('dormant-and-inactive-corporations',
    'The complete guide to dormant and inactive corporations')],
 'gst-hst-account-closure-checker': [
   ('dormant-and-inactive-corporations',
    'The complete guide to dormant and inactive corporations'),
   ('how-to-file-a-nil-t2-return', 'How to file a nil T2 return')],
}

# ------------------------------------------------------------------- guards
import re as _re

# A section anchor sharing an id with a form field is silently wrong, because
# getElementById returns whichever comes first in the document.
for t in TOOLS5:
    _sec = {sid for sid, _, _ in t['sections']}
    _fld = set(_re.findall(r'id="([\w-]+)"', t['form']))
    _fld |= set(_re.findall(r'name="([\w-]+)"', t['form']))
    _clash = _sec & _fld
    assert not _clash, ('%s: section anchor collides with a form id: %s'
                        % (t['slug'], sorted(_clash)))

# Every decision tree compares against the alphabet the form actually emits.
# A tree testing 'yes' against a form emitting 'y' matches no branch at all
# and silently falls through to whatever the last case is.
for t in TOOLS5:
    _vals = set(_re.findall(r'value="([^"]*)"', t['form']))
    assert _vals <= {'y', 'n'}, ('%s: form emits values outside {y,n}: %s'
                                 % (t['slug'], sorted(_vals - {'y', 'n'})))

# Every slug here is an Appendix A entry, and none of them is already live.
_LIVE = set(ORDER4)
for t in TOOLS5:
    assert t['slug'] not in _LIVE, '%s is already live' % t['slug']
assert len({t['slug'] for t in TOOLS5}) == len(TOOLS5), 'duplicate slug'

# Rule 3: wherever a page says the percentage penalty has nothing to apply
# to, the full qualification travels with it as one block.
for t in TOOLS5:
    _body = ' '.join(b for _, _, b in t['sections'])
    _body += ' '.join(q + ' ' + aa for q, aa in t['faq'])
    assert 'no penalty' not in _body.lower(), (
        '%s: the bare phrase "no penalty" appears' % t['slug'])

for t in TOOLS5:
    i = ORDER5.index(t['slug'])
    rel = [(T + ORDER5[j] + '/', LINK_TITLE5[ORDER5[j]]) for j in SIBLINGS5[i]]
    rel += [(G + g + '/', ttl) for g, ttl in GUIDES5[t['slug']]]
    rel.append((COST, 'Nil T2 filing cost'))
    t['related'] = rel


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'October 27, 2026', '2026-10-27'
    recs = []
    for t in TOOLS5:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html, **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2e-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-46s %6d bytes' % (r['slug'], len(r['content'].encode())))
