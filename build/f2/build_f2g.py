# -*- coding: utf-8 -*-
"""Family 2 batch 7: tools 41 to 50.

HOW THESE TEN TOPICS WERE CHOSEN, AND WHY NOT FROM APPENDIX A

Batch 6 established that Appendix A cannot supply ten more distinct F2 tools.
Of the 130 unbuilt F2 slugs in it, twenty-seven are naming variants of tools
already live, and the rest fall into groups that cannot be built without a
figure this project has no approved source for. Nothing has changed that, so
all ten topics here are sourced outside Appendix A, as the last two guide
batches were.

Every fact each page asserts is traceable to the signed plan or to a page
already live. That constraint did real work: three topics I drafted were
dropped on reading the plan rather than on taste.

  Books-and-records retention
      Dropped. The plan's "six years" is the FIRM's retention of the signed
      Form T183CORP (plan lines 189, 390, 1176, 2099). It is not the CRA
      books-and-records rule, which the plan never states. A retention
      calculator would have had to assert a statutory period on my own
      authority, which is the same thing I refused to do for the penalty
      rates in batch 6.

  Normal reassessment period
      Dropped. "Reassess" does not appear in the plan at all. The three-year
      and four-year periods are stable and well known, which is not the test;
      the test is whether this project has approved them. It has not.

  GST/HST nil return due dates
      Dropped. The plan states the GST/HST facts this site may use -- that an
      open account still needs nil filings, and that Form RC145 closes it --
      and says nothing about filing frequencies or their due dates. Tool 44
      below shows the shape of fact that IS approved: a date rule the plan
      names in terms.

What the plan does approve, and which tool uses it:

  "Mandatory T2 E-Filing for Tax Years Starting After 2023"  (plan 2206)
      -> tool 44. A date test, no threshold, no penalty figure. The paper
      filing penalty is a separate approved blog topic but the plan gives no
      amount, so tool 44 names the consequence as a penalty without a figure
      and sends the reader to the guide.

  T183CORP: authorized signing officer, signed before transmission, carries
  the date and an HH:MM:SS Eastern timestamp, never backdated, kept by the
  firm for six years, not sent to CRA unless CRA asks  (plan 189, 390, 1176)
      -> tool 46, which is the one page in the batch whose every assertion is
      quoted from the plan.

  Hard rule 8: Quebec CO-17 is a separate return, Alberta AT1 is the same
      -> tool 47, which exists to say exactly that.

  "Federal Corporations and the $12 Annual Return Within 60 Days of Your
  Anniversary", "Dissolving a Corporation and the Final T2 Within Six
  Months", the six-month filing rule, the two-or-three-month balance rule
  and the 53-week limit, all already live on tools 31, 32 and 8
      -> tools 41, 42, 43, 49.

THE ONE OVERLAP I ACCEPTED ON PURPOSE

Tool 50 is a catch-up schedule generator, and the family already has two
catch-up tools. The division of labour is real and each page states it:

  /tools/unfiled-years-checker/          WHICH years are outstanding
  /tools/unfiled-years-cost-calculator/  WHAT the whole catch-up costs
  /tools/catch-up-filing-schedule-generator/  the DATED schedule, a row per
      year with its period, its deadline and how overdue it is

I set this aside once on duplication grounds and then built it, because the
dated schedule is the artifact the site's core visitor actually wants and
neither live tool produces it. All three cross-link.

Tool 49 is a deliberate consolidator rather than a new fact: one year-end and
one incorporation date in, the whole corporate calendar out. Its rows restate
dates the single-purpose tools own, and it links to each of them, so a reader
who wants one date in depth can get there.
"""
import io, json, os, sys, re as _re

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_f2 import (render, meta, yn, a, SITE, HUB, FORM, PRICE,
                      NOT_NIL, TOOL_DISCLAIMER)
from build_f2b import tool, num, date, PICK, T, G, COST
from build_f2c import MONEY_JS, QUAL, PRELUDE
from build_f2f import BASE, RBASE, ORDER6, LINK_TITLE6, _GUIDES_LIVE

# Ontario's nine Employment Standards Act public holidays, in exactly the
# order holidays(y) returns them. The pairing is positional, so a guard below
# fails the build if the shared module's list ever changes length.
HNAME_JS = r"""var HNAME=['New Year&#8217;s Day','Family Day','Good Friday',
  'Victoria Day','Canada Day','Labour Day','Thanksgiving Day',
  'Christmas Day','Boxing Day'];
function holidayName(dt){
  var hs=holidays(dt.getUTCFullYear());
  for(var i=0;i<hs.length;i++){
    if(hs[i].getTime()===dt.getTime()){return HNAME[i];}
  }
  return null;
}
"""

assert BASE.count('nthMon(y,8,1),nthMon(y,9,2),u(y,11,25),u(y,11,26)') == 1, (
    'the shared holiday list changed shape. HNAME_JS pairs names to it by '
    'position, so re-read holidays() before trusting holidayName().')

# ------------------------------------------------------- 41. year-end options
T41_JS = BASE + r"""
function yearEndOptions(inc){
  if(inc===null){return null;}
  if(inc===undefined){return {err:'read'};}
  var rows=[],y=inc.getUTCFullYear(),m=inc.getUTCMonth();
  for(var k=0;k<14;k++){
    var tm=m+k,ty=y+Math.floor(tm/12),mm=((tm%12)+12)%12;
    var me=u(ty,mm,lastDay(ty,mm));
    if(me.getTime()<=inc.getTime()){continue;}
    var days=spanDays(inc,me);
    if(days>371){break;}
    rows.push({ye:me,days:days,due:nextBusiness(dueDate(me))});
  }
  return {rows:rows,inc:inc};
}
var out=document.getElementById('out');
function show(){
  var r=yearEndOptions(parse('inc'));
  if(r===null){out.innerHTML='<p>Enter the date of incorporation.</p>';
    return;}
  if(r.err){out.innerHTML='<p>That date could not be read.</p>';return;}
  if(!r.rows.length){out.innerHTML='<p>No month-end falls within 53 weeks of '
    +'that date, which should not happen. Check the date.</p>';return;}
  var h='<h3>'+plural(r.rows.length,'month-end')+' available for the first '
   +'year-end</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">First year-end</th>'
   +'<th scope="col">Length of the first tax year</th>'
   +'<th scope="col">T2 due</th></tr></thead><tbody>';
  for(var i=0;i<r.rows.length;i++){
    h+='<tr><td>'+fmt(r.rows[i].ye)+'</td><td>'+plural(r.rows[i].days,'day')
     +'</td><td>'+fmt(r.rows[i].due)+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>Every date in this table is within the 53 weeks a first tax year may '
   +'not exceed, counting the day of incorporation. A year-end beyond the last '
   +'row is not available, and the T2 column already allows for a date landing '
   +'on a weekend or a public holiday.</p>';
  h+='<p>A year-end does not have to be a month-end. The table lists '
   +'month-ends because that is what nearly every corporation chooses, and '
   +'because a month-end year-end makes the six-month rule land on a month-end '
   +'too.</p>';
  h+='<p>Whichever is chosen, the first return is '+PRICE_JS+' where the year '
   +'is nil. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
var e=document.getElementById('inc');
if(e){e.addEventListener('change',show);e.addEventListener('input',show);}
"""

# -------------------------------------------------------- 42. year-end change
T42_JS = BASE + r"""
function changeImpact(cur,nw){
  if(cur===null||nw===null){return null;}
  if(cur===undefined||nw===undefined){return {err:'read'};}
  if(nw.getTime()<=cur.getTime()){return {err:'order'};}
  var start=dayAfter(cur),days=spanDays(start,nw);
  var nextYe=addYear(nw,1);
  return {start:start,nw:nw,days:days,over:days>371,short:days<365,
          due:nextBusiness(dueDate(nw)),
          nextYe:nextYe,nextDue:nextBusiness(dueDate(nextYe))};
}
var out=document.getElementById('out');
function show(){
  var r=changeImpact(parse('cur'),parse('new'));
  if(r===null){out.innerHTML='<p>Enter the year-end on record and the one you '
    +'want to move to.</p>';return;}
  if(r.err==='read'){out.innerHTML='<p>Those dates could not be read.</p>';
    return;}
  if(r.err==='order'){out.innerHTML='<p>The new year-end has to fall after '
    +'the one on record. A year-end cannot be moved backwards into a period '
    +'already reported.</p>';return;}
  var h='<h3>'+(r.over?'That change does not produce a single tax year'
    :'The change creates a period of '+plural(r.days,'day'))+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Item</th>'
   +'<th scope="col">Date</th></tr></thead><tbody>';
  h+='<tr><td>First day of the period the change creates</td><td>'
   +fmt(r.start)+'</td></tr>';
  h+='<tr><td>Last day of it, the new year-end</td><td>'+fmt(r.nw)
   +'</td></tr>';
  h+='<tr><td>Its length, counting both ends</td><td>'+plural(r.days,'day')
   +'</td></tr>';
  h+='<tr><td>T2 for that period due</td><td>'+fmt(r.due)+'</td></tr>';
  h+='<tr><td>The next full year then ends</td><td>'+fmt(r.nextYe)
   +'</td></tr>';
  h+='<tr><td>And its T2 is due</td><td>'+fmt(r.nextDue)+'</td></tr>';
  h+='</tbody></table>';
  if(r.over){
    h+='<div class="ei-danger"><p>A tax year cannot exceed 53 weeks, which is '
     +'371 days, so a gap this long is not one period. Reaching that year-end '
     +'needs an intervening year-end, which means two returns rather than '
     +'one.</p></div>';
  }else if(r.short){
    h+='<p>That is a short tax year, and a short year does not get a short '
     +'deadline: the six-month rule is measured from the day the period ends. '
     +'It is also a separate return, so a change of year-end costs a return '
     +'that would not otherwise exist.</p>';
  }else{
    h+='<p>That period is a full tax year in its own right, so the change '
     +'moves the year-end without creating a stub period.</p>';
  }
  h+='<div class="ei-warn"><p>A fiscal year-end is fixed by the first return '
   +'filed, and changing it needs the written approval of the Canada Revenue '
   +'Agency. A return filed carrying a different date does not change the '
   +'year-end on record; it is rejected against it. This calculator shows '
   +'what an approved change would produce. It cannot tell you the change '
   +'was approved.</p></div>';
  h+='<p>Each return is '+PRICE_JS+' where the year is nil. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
['cur','new'].forEach(function(id){
  var el=document.getElementById(id);
  if(el){el.addEventListener('change',show);el.addEventListener('input',show);}
});
"""

# ---------------------------------------------------- 43. two returns in a year
T43_JS = BASE + MONEY_JS + r"""
function twoReturns(y1,y2){
  if(y1===null||y2===null){return null;}
  if(y1===undefined||y2===undefined){return {err:'read'};}
  if(y2.getTime()<=y1.getTime()){return {err:'order'};}
  var d1=nextBusiness(dueDate(y1)),d2=nextBusiness(dueDate(y2));
  var gap=Math.round((d2.getTime()-d1.getTime())/86400000);
  return {y1:y1,y2:y2,d1:d1,d2:d2,gap:gap,
          same:d1.getUTCFullYear()===d2.getUTCFullYear(),
          tight:gap<=92,total:60000};
}
var out=document.getElementById('out');
function show(){
  var r=twoReturns(parse('y1'),parse('y2'));
  if(r===null){out.innerHTML='<p>Enter both year-ends.</p>';return;}
  if(r.err==='read'){out.innerHTML='<p>Those dates could not be read.</p>';
    return;}
  if(r.err==='order'){out.innerHTML='<p>The second year-end has to fall after '
    +'the first.</p>';return;}
  var h='<h3>'+(r.same?'Both deadlines fall in '+r.d1.getUTCFullYear()
    :'The two deadlines fall in different calendar years')+'</h3>';
  h+='<div class="ei-stats"><div class="ei-stat">'
   +'<span class="ei-stat-l">First T2 due</span>'
   +'<span class="ei-stat-v">'+fmt(r.d1)+'</span></div>'
   +'<div class="ei-stat"><span class="ei-stat-l">Second T2 due</span>'
   +'<span class="ei-stat-v">'+fmt(r.d2)+'</span></div>'
   +'<div class="ei-stat"><span class="ei-stat-l">Days between them</span>'
   +'<span class="ei-stat-v">'+r.gap+'</span></div></div>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Tax year ending</th>'
   +'<th scope="col">T2 due</th></tr></thead><tbody>';
  h+='<tr><td>'+fmt(r.y1)+'</td><td>'+fmt(r.d1)+'</td></tr>';
  h+='<tr><td>'+fmt(r.y2)+'</td><td>'+fmt(r.d2)+'</td></tr>';
  h+='<tr><td>Two returns, at '+money(30000)+' plus HST each</td><td>'
   +money(r.total)+' plus HST</td></tr>';
  h+='</tbody></table>';
  if(r.tight){
    h+='<div class="ei-warn"><p>Those two deadlines are '+plural(r.gap,'day')
     +' apart, which is the part that catches people out. Two returns falling '
     +'this close together are easy to read as one, and filing only the '
     +'second leaves the first year outstanding.</p></div>';
  }
  h+='<p>Each tax year is its own return whatever its length, and both can be '
   +'prepared and transmitted together. They are prepared oldest first, '
   +'because the closing balances of the first year open the second.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
['y1','y2'].forEach(function(id){
  var el=document.getElementById(id);
  if(el){el.addEventListener('change',show);el.addEventListener('input',show);}
});
"""

# ---------------------------------------------------------- 44. mandatory efile
T44_JS = BASE + r"""
function efileRule(st){
  if(st===null){return null;}
  if(st===undefined){return {err:'read'};}
  return {st:st,mandatory:st.getUTCFullYear()>=2024};
}
var out=document.getElementById('out');
function show(){
  var r=efileRule(parse('st'));
  if(r===null){out.innerHTML='<p>Enter the first day of the tax year.</p>';
    return;}
  if(r.err){out.innerHTML='<p>That date could not be read.</p>';return;}
  var h='<h3>Electronic filing '+(r.mandatory?'is mandatory':'was not '
   +'mandatory')+' for a tax year beginning '+fmt(r.st)+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Item</th>'
   +'<th scope="col">This tax year</th></tr></thead><tbody>';
  h+='<tr><td>Tax year begins</td><td>'+fmt(r.st)+'</td></tr>';
  h+='<tr><td>Begins after 2023</td><td>'+(r.mandatory?'Yes':'No')
   +'</td></tr>';
  h+='<tr><td>Electronic filing mandatory</td><td>'
   +(r.mandatory?'Yes':'No')+'</td></tr>';
  h+='<tr><td>How this return is transmitted</td>'
   +'<td>Electronically, either way</td></tr>';
  h+='</tbody></table>';
  if(r.mandatory){
    h+='<p>Electronic filing is mandatory for tax years starting after 2023, '
     +'and filing on paper where it is mandatory carries a penalty. The '
     +'amount is not stated here, because a figure on a web page is the wrong '
     +'place to read it from.</p>';
  }else{
    h+='<p>A tax year beginning before 2024 falls outside the mandatory '
     +'period, so paper was an option for it. That matters on a catch-up, '
     +'where the oldest years in the sequence may predate the rule while the '
     +'newest do not.</p>';
  }
  h+='<p>Either way this makes no practical difference to how your return is '
   +'filed here. Gondaliya CPA Professional Corporation is a registered EFILE '
   +'electronic filer and transmits every return electronically, including '
   +'years the rule never reached.</p>';
  h+='<p>A nil year is '+PRICE_JS+'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
var e=document.getElementById('st');
if(e){e.addEventListener('change',show);e.addEventListener('input',show);}
"""

# -------------------------------------------------------- 45. business days
T45_JS = BASE + HNAME_JS + r"""
function spanCount(f,t){
  if(f===null||t===null){return null;}
  if(f===undefined||t===undefined){return {err:'read'};}
  if(t.getTime()<f.getTime()){return {err:'order'};}
  var cal=spanDays(f,t);
  if(cal>3700){return {err:'long'};}
  var biz=0,wk=0,hol=[],d=new Date(f.getTime());
  while(d.getTime()<=t.getTime()){
    var w=d.getUTCDay();
    if(w===0||w===6){wk++;}
    else if(isHoliday(d)){hol.push({dt:new Date(d.getTime()),
                                    nm:holidayName(d)});}
    else{biz++;}
    d=new Date(d.getTime()+86400000);
  }
  return {f:f,t:t,cal:cal,biz:biz,wk:wk,hol:hol};
}
var out=document.getElementById('out');
function show(){
  var r=spanCount(parse('f'),parse('t'));
  if(r===null){out.innerHTML='<p>Enter both dates.</p>';return;}
  if(r.err==='read'){out.innerHTML='<p>Those dates could not be read.</p>';
    return;}
  if(r.err==='order'){out.innerHTML='<p>The second date falls before the '
    +'first.</p>';return;}
  if(r.err==='long'){out.innerHTML='<p>That span is longer than ten years. '
    +'Narrow it and the count returns.</p>';return;}
  var h='<h3>'+plural(r.biz,'business day')+' in a span of '
   +plural(r.cal,'day')+'</h3>';
  h+='<div class="ei-stats"><div class="ei-stat">'
   +'<span class="ei-stat-l">Calendar days</span>'
   +'<span class="ei-stat-v">'+r.cal+'</span></div>'
   +'<div class="ei-stat"><span class="ei-stat-l">Business days</span>'
   +'<span class="ei-stat-v">'+r.biz+'</span></div>'
   +'<div class="ei-stat"><span class="ei-stat-l">Weekend days</span>'
   +'<span class="ei-stat-v">'+r.wk+'</span></div></div>';
  if(r.hol.length){
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Public holiday</th>'
     +'<th scope="col">Date</th></tr></thead><tbody>';
    for(var i=0;i<r.hol.length;i++){
      h+='<tr><td>'+r.hol[i].nm+'</td><td>'+fmt(r.hol[i].dt)+'</td></tr>';
    }
    h+='</tbody></table>';
  }else{
    h+='<p>No public holiday falls on a weekday inside that span.</p>';
  }
  h+='<p>Both dates are counted, so a span from a Monday to the following '
   +'Monday is eight calendar days. A public holiday landing on a Saturday or '
   +'a Sunday is counted once, as a weekend day, which is why it does not '
   +'appear in the list above.</p>';
  h+='<p>The nine holidays here are Ontario&#8217;s, which is the calendar '
   +'every date tool on this site runs on. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
['f','t'].forEach(function(id){
  var el=document.getElementById(id);
  if(el){el.addEventListener('change',show);el.addEventListener('input',show);}
});
"""

# ------------------------------------------------------------- 46. T183CORP
T46_JS = RBASE + r"""
function t183Check(off,red,bef){
  if(off===null||red===null||bef===null){return null;}
  var fails=[];
  if(off!=='y'){fails.push('The person signing is not an '
    +'authorized signing officer of the corporation.');}
  if(red!=='y'){fails.push('The figures the form carries have not been read '
    +'by the person signing.');}
  if(bef!=='y'){fails.push('The form is not being signed before the return '
    +'is transmitted.');}
  return {fails:fails,ok:fails.length===0,
          off:off==='y',red:red==='y',bef:bef==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=t183Check(pick('off'),pick('red'),pick('bef'));
  if(r===null){out.innerHTML='<p>Answer all three questions.</p>';return;}
  var h='<h3>'+(r.ok?'Form T183CORP can be signed'
    :plural(r.fails.length,'condition')+' is not met')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Condition</th>'
   +'<th scope="col">Met</th></tr></thead><tbody>';
  h+='<tr><td>Signed by an authorized signing officer of the corporation</td>'
   +'<td>'+(r.off?'Yes':'No')+'</td></tr>';
  h+='<tr><td>The signing officer has read the figures on the return</td>'
   +'<td>'+(r.red?'Yes':'No')+'</td></tr>';
  h+='<tr><td>Signed before the return is transmitted</td><td>'
   +(r.bef?'Yes':'No')+'</td></tr>';
  h+='</tbody></table>';
  if(!r.ok){
    h+='<ul>';
    for(var i=0;i<r.fails.length;i++){h+='<li>'+r.fails[i]+'</li>';}
    h+='</ul>';
    h+='<p>None of these is a formality that can be caught up afterwards. '
     +'The form authorizes the transmission, so it has to exist, correctly '
     +'signed, before the transmission happens.</p>';
  }else{
    h+='<p>All three conditions are met, which is what the form needs. It is '
     +'signed on a single-use access-controlled screen and the transmission '
     +'follows it.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">What the form does</th>'
   +'<th scope="col">How it works here</th></tr></thead><tbody>';
  h+='<tr><td>What it carries</td><td>The figures on your own return</td>'
   +'</tr>';
  h+='<tr><td>What it records</td><td>The date, and the hour, minute and '
   +'second, in Eastern Time</td></tr>';
  h+='<tr><td>Backdating</td><td>Never. The timestamp is written by the '
   +'server as you sign</td></tr>';
  h+='<tr><td>How long the firm keeps it</td><td>Six years</td></tr>';
  h+='<tr><td>Is it sent to CRA</td><td>No, unless CRA asks for it</td></tr>';
  h+='</tbody></table>';
  h+='<p>Signing Form T183CORP is part of filing and is inside the fee of '
   +PRICE_JS+'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="off"],input[name="red"],'
    +'input[name="bef"]'),
  function(el){el.addEventListener('change',show);});
"""

# ---------------------------------------------------------- 47. CO-17 and AT1
T47_JS = RBASE + r"""
function provincial(qc,ab){
  if(qc===null||ab===null){return null;}
  var rows=[];
  if(qc==='y'){rows.push(['Quebec','CO-17','A separate provincial return, '
    +'filed with Revenu Quebec']);}
  if(ab==='y'){rows.push(['Alberta','AT1','A separate provincial return, '
    +'filed with Alberta']);}
  return {rows:rows,any:rows.length>0,qc:qc==='y',ab:ab==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=provincial(pick('qc'),pick('ab'));
  if(r===null){out.innerHTML='<p>Answer both questions.</p>';return;}
  var h='<h3>'+(r.any?plural(r.rows.length,'separate provincial return')
    +' in addition to the federal T2'
    :'The federal T2 is the only corporate income tax return')+'</h3>';
  if(r.any){
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Province</th>'
     +'<th scope="col">Return</th><th scope="col">What it is</th></tr>'
     +'</thead><tbody>';
    for(var i=0;i<r.rows.length;i++){
      h+='<tr><td>'+r.rows[i][0]+'</td><td>'+r.rows[i][1]+'</td><td>'
       +r.rows[i][2]+'</td></tr>';
    }
    h+='</tbody></table>';
    h+='<div class="ei-warn"><p>The fee of '+PRICE_JS+' covers one nil '
     +'federal T2 return for one corporation for one tax year. '
     +(r.qc&&r.ab?'CO-17 and AT1 are not covered by it.'
       :(r.qc?'CO-17 is not covered by it.':'AT1 is not covered by it.'))
     +'</p></div>';
    h+='<p>A quiet year is quiet on both returns, so the provincial return is '
     +'nil where the federal one is. That does not make it optional. It is a '
     +'separate return, filed separately, on its own deadline.</p>';
  }else{
    h+='<p>Everywhere else the province levies its corporate income tax '
     +'through the federal return, so the T2 is the only corporate income tax '
     +'return the corporation files. One nil T2 at '+PRICE_JS+' covers the '
     +'tax year.</p>';
    h+='<p>The annual return owed to a corporate registry is a different '
     +'thing from a tax return, and every corporation has one of those '
     +'wherever it is incorporated. It is a registry filing and sits outside '
     +'the fee.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="qc"],input[name="ab"]'),
  function(el){el.addEventListener('change',show);});
"""

# ------------------------------------------------------- 48. account closures
T48_JS = RBASE + r"""
function closureSteps(rp,rt,dis){
  if(rp===null||rt===null||dis===null){return null;}
  var steps=[];
  steps.push(['File every outstanding T2 return, oldest first',
    'Inside the fee, ' + PRICE_JS]);
  if(rp==='y'){steps.push(['Close the payroll account with Form RC145',
    'Outside the fee']);}
  if(rt==='y'){steps.push(['Close the GST/HST account with Form RC145',
    'Outside the fee']);}
  if(dis==='y'){
    steps.push(['File the final T2 for the period ending at dissolution',
      'Inside the fee, ' + PRICE_JS]);
    steps.push(['Request a clearance certificate','Outside the fee']);
    steps.push(['File the registry articles of dissolution',
      'Outside the fee']);
  }
  return {steps:steps,dis:dis==='y',
          accts:(rp==='y'?1:0)+(rt==='y'?1:0)};
}
var out=document.getElementById('out');
function show(){
  var r=closureSteps(pick('rp'),pick('rt'),pick('dis'));
  if(r===null){out.innerHTML='<p>Answer all three questions.</p>';return;}
  var h='<h3>'+plural(r.steps.length,'step')+', in this order</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Order</th>'
   +'<th scope="col">Step</th><th scope="col">Covered by the fee</th></tr>'
   +'</thead><tbody>';
  for(var i=0;i<r.steps.length;i++){
    h+='<tr><td>'+(i+1)+'</td><td>'+r.steps[i][0]+'</td><td>'
     +r.steps[i][1]+'</td></tr>';
  }
  h+='</tbody></table>';
  if(r.accts){
    h+='<p>An account that is open keeps generating obligations whether or '
     +'not the corporation is doing anything, and those obligations are '
     +'separate from the T2. Closing the account is what ends them, and '
     +'Form RC145 is what closes it.</p>';
  }else{
    h+='<p>With no payroll and no GST/HST account open, the T2 is the only '
     +'thing outstanding. That is the simplest position a dormant corporation '
     +'can be in.</p>';
  }
  if(r.dis){
    h+='<p>The order matters at a wind-up. The outstanding returns come '
     +'first, because a clearance request rests on a complete filing record, '
     +'and the registry filing comes last, because dissolving a corporation '
     +'that still owes returns leaves the tax years open behind it.</p>';
  }
  h+='<p>'+QUALJS+'</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="rp"],input[name="rt"],'
    +'input[name="dis"]'),
  function(el){el.addEventListener('change',show);});
"""

# ------------------------------------------------------- 49. whole calendar
T49_JS = RBASE + r"""
function anniversaryAfter(inc,ye){
  for(var k=0;k<200;k++){
    var ann=addYear(inc,k);
    if(ann.getTime()>=ye.getTime()){return ann;}
  }
  return null;
}
function calendar(ye,inc,fed,pay){
  if(ye===null||fed===null||pay===null){return null;}
  if(ye===undefined){return {err:'read'};}
  if(fed==='y'&&inc===null){return null;}
  if(inc===undefined){return {err:'read'};}
  var rows=[];
  rows.push(['Balance of tax due, two months after the year-end',
    fmt(nextBusiness(addMonths(ye,2))),
    'Nothing is owed on a nil year']);
  rows.push(['T2 return due, six months after the year-end',
    fmt(nextBusiness(dueDate(ye))),
    'The one date a dormant corporation has to meet']);
  if(pay==='y'){
    var feb=u(ye.getUTCFullYear()+1,1,lastDay(ye.getUTCFullYear()+1,1));
    rows.push(['T4 information return for '+ye.getUTCFullYear()
      +', end of the following February',
      fmt(nextBusiness(feb)),
      'Expected while the payroll account is open']);
  }
  if(fed==='y'){
    var ann=anniversaryAfter(inc,ye);
    rows.push(['Incorporation anniversary',fmt(ann),
      'The federal annual return runs from this date']);
    rows.push(['Federal annual return, within 60 days of the anniversary',
      fmt(new Date(ann.getTime()+60*86400000)),
      'A registry filing, outside the fee']);
  }
  var next=addYear(ye,1);
  rows.push(['The next fiscal year then ends',fmt(next),
    'And its T2 is due '+fmt(nextBusiness(dueDate(next)))]);
  return {rows:rows,ye:ye,fed:fed==='y',pay:pay==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=calendar(parse('ye'),parse('inc'),pick('fed'),pick('pay'));
  if(r===null){out.innerHTML='<p>Enter the fiscal year-end and answer both '
    +'questions. The incorporation date is needed only for a federal '
    +'corporation.</p>';return;}
  if(r.err){out.innerHTML='<p>Those dates could not be read.</p>';return;}
  var h='<h3>'+plural(r.rows.length,'date')+' for a year ending '
   +fmt(r.ye)+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Date</th>'
   +'<th scope="col">Falls on</th><th scope="col">Note</th></tr></thead>'
   +'<tbody>';
  for(var i=0;i<r.rows.length;i++){
    h+='<tr><td>'+r.rows[i][0]+'</td><td>'+r.rows[i][1]+'</td><td>'
     +r.rows[i][2]+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>Every date here is moved off a Saturday, a Sunday or an Ontario '
   +'public holiday to the next business day, on the one holiday calendar '
   +'this site uses throughout.</p>';
  h+='<p>The balance date assumes the two-month period. A '
   +'Canadian-controlled private corporation meeting the conditions has '
   +'three months, which changes that row and nothing else on this '
   +'calendar.</p>';
  if(r.pay){
    h+='<p>Notice that the T4 row does not derive from the year-end at all. '
     +'It reports a calendar year and is due at the end of the following '
     +'February whatever year-end the corporation uses, which is why the two '
     +'dates can sit months apart.</p>';
  }
  h+='<p>A nil T2 is '+PRICE_JS+'. The registry annual return is a separate '
   +'filing and is not covered by it. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
['ye','inc'].forEach(function(id){
  var el=document.getElementById(id);
  if(el){el.addEventListener('change',show);el.addEventListener('input',show);}
});
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="fed"],input[name="pay"]'),
  function(el){el.addEventListener('change',show);});
"""

# -------------------------------------------------------- 50. catch-up schedule
T50_JS = BASE + MONEY_JS + r"""
function catchUp(y1,n,now){
  if(y1===null||n===null){return null;}
  if(y1===undefined){return {err:'read'};}
  if(!(n>=1)||n>20){return {err:'n'};}
  var rows=[],late=0;
  for(var k=0;k<n;k++){
    var ye=addYear(y1,k),due=nextBusiness(dueDate(ye));
    var over=Math.round((now.getTime()-due.getTime())/86400000);
    if(over>0){late++;}
    rows.push({ye:ye,due:due,over:over});
  }
  return {rows:rows,n:n,late:late,total:n*30000,
          first:rows[0],last:rows[n-1]};
}
var out=document.getElementById('out');
function show(){
  var v=document.getElementById('n').value;
  var r=catchUp(parse('y1'),v===''?null:parseInt(v,10),today());
  if(r===null){out.innerHTML='<p>Enter the earliest unfiled year-end and how '
    +'many years are outstanding.</p>';return;}
  if(r.err==='read'){out.innerHTML='<p>That date could not be read.</p>';
    return;}
  if(r.err==='n'){out.innerHTML='<p>Enter a number of years between 1 and '
    +'20.</p>';return;}
  var h='<h3>'+plural(r.n,'return')+', '+money(r.total)+' plus HST in '
   +'total</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Order</th>'
   +'<th scope="col">Tax year ending</th><th scope="col">T2 was due</th>'
   +'<th scope="col">Overdue by</th></tr></thead><tbody>';
  for(var i=0;i<r.rows.length;i++){
    var o=r.rows[i].over;
    h+='<tr><td>'+(i+1)+'</td><td>'+fmt(r.rows[i].ye)+'</td><td>'
     +fmt(r.rows[i].due)+'</td><td>'
     +(o>0?plural(o,'day'):(o===0?'Due today':'Not yet due, '
        +plural(-o,'day')+' remaining'))+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>They are prepared in this order, oldest first, because each '
   +'year&#8217;s return opens from the closing balances of the one before '
   +'it. A year filed out of order carries opening figures that have not been '
   +'established yet.</p>';
  h+='<p>All '+r.n+' can be transmitted in one sitting once they are '
   +'prepared. You sign one Form T183CORP for each year.</p>';
  if(r.late){
    h+='<div class="ei-warn"><p>'+QUALJS+'</p></div>';
  }
  h+='<p>'+plural(r.n,'year')+' at '+money(30000)+' plus HST each is '
   +money(r.total)+' plus HST. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
['y1','n'].forEach(function(id){
  var el=document.getElementById(id);
  if(el){el.addEventListener('change',show);el.addEventListener('input',show);}
});
"""

TOOLS7 = [
 dict(slug='first-t2-year-end-options-generator',
  title='First T2 Year-End Options Generator | Every Date Available',
  h1_pre='First T2 ', h1_span='Year-End Options Generator',
  h1='First T2 Year-End Options Generator',
  eyebrow='First Year', keyword='first t2 year-end options generator',
  meta=('Enter the incorporation date and every month-end available as a '
        'first year-end appears, with the length of the year and the T2 '
        'date.'),
  tags=['Every option, not one test', 'All within 371 days',
        'T2 date for each', 'Month-ends, and why'],
  form=tool('Your incorporation date',
            [date('inc', 'The date on the certificate of incorporation')],
            'Enter the incorporation date and the options appear here.'),
  js=None,
  sections=[
   ('a-choice', 'The First Year-End Is a Choice, and It Is Made Once',
    '<p>A corporation picks its own fiscal year-end. Nothing assigns one, and '
    'there is no default to fall back on. The choice is made by the first '
    'return filed, and from then on the date is fixed on the record.</p>\n'
    '<p>Changing it afterwards needs the written approval of the Canada '
    'Revenue Agency, which makes this the one decision in a corporation&#8217;s '
    'tax life that is easy now and awkward later. The '
    + a(T + 'year-end-change-impact-calculator/',
        'year-end change impact calculator')
    + ' shows what changing it costs.</p>'),
   ('the-ceiling', 'The 53-Week Limit Sets the Ceiling',
    '<p>A first tax year may not exceed 53 weeks, which is 371 days counting '
    'the day of incorporation. That is what bounds the table: every row in it '
    'is within the limit and there is no row beyond it, because a year-end '
    'past that point is not available.</p>\n'
    '<p>The '
    + a(T + '53-week-first-tax-year-checker/',
        '53-week first tax year checker')
    + ' tests one proposed date against the limit. This page does the '
    'opposite and lists them all, which is the more useful order to see them '
    'in when the date has not been picked yet.</p>'),
   ('month-ends', 'Why the Table Lists Month-Ends',
    '<p>A year-end does not have to be the last day of a month. Any date '
    'inside the limit is available, and a corporation incorporated on the 9th '
    'can keep the 9th if it wants to.</p>\n'
    '<p>Nearly none do, for a reason worth knowing: the six-month filing rule '
    'lands on a month-end when the year-end is a month-end, and on an awkward '
    'mid-month date when it is not. A month-end year-end makes every date '
    'that follows from it easier to hold in your head.</p>'),
   ('late-or-early', 'A Later Year-End Is Not a Longer Reprieve',
    '<p>The last row in the table has the longest first year and the latest '
    'T2 date, which makes it look like the one that buys the most time. Over '
    'one year it does. Over the corporation&#8217;s life it buys nothing, '
    'because the year-end then recurs annually on that date.</p>\n'
    '<p>What a later first year-end does buy is one fewer return. A first '
    'year ending after two months is a return for two months of nothing, and '
    'it is '
    + PRICE + ' like any other. Each tax year is its own return whatever its '
    'length.</p>'),
  ],
  faq=[
   ('How long can my first tax year be?',
    'Up to 53 weeks, which is 371 days counting the day of incorporation. '
    'Every date the generator lists is inside that limit.'),
   ('Does a year-end have to be the end of a month?',
    'No. Any date within the 53-week limit is available. Month-ends are what '
    'nearly every corporation chooses, because the six-month filing rule then '
    'lands on a month-end too.'),
   ('Can I change the year-end later?',
    'Only with the written approval of the Canada Revenue Agency. The date is '
    'fixed by the first return filed, and a later return carrying a different '
    'date is rejected rather than treated as a change.'),
   ('Is a short first year cheaper?',
    'No. A short first year is a separate return at ' + PRICE + ', so '
    'choosing a very early first year-end means paying for a return covering '
    'a few weeks of nothing.'),
   ('Which option should I pick?',
    'That depends on facts a web page does not have. What the generator can '
    'tell you is which dates are available and what each one does to the '
    'filing deadline.'),
  ]),

 dict(slug='year-end-change-impact-calculator',
  title='Year-End Change Impact Calculator | The Period It Creates',
  h1_pre='Year-End ', h1_span='Change Impact Calculator',
  h1='Year-End Change Impact Calculator',
  eyebrow='Date Tool', keyword='year-end change impact calculator',
  meta=('Moving a fiscal year-end creates a period and a return. Enter both '
        'dates for its length, its T2 date and what comes after it.'),
  tags=['Shows the period created', 'Tests the 371-day limit',
        'Gives both T2 dates', 'Written CRA approval required'],
  form=tool('The two year-ends',
            [date('cur', 'The year-end on record now'),
             date('new', 'The year-end you want to move to')],
            'Enter both year-ends and the effect appears here.'),
  js=None,
  sections=[
   ('what-it-creates', 'A Change of Year-End Creates a Period, and a Return',
    '<p>Moving a year-end does not stretch or shrink the year that is already '
    'running. It closes a period on the new date, and that period is a tax '
    'year of its own with its own return and its own deadline.</p>\n'
    '<p>So a change from December 31 to June 30 produces a six-month period, '
    'a return for it, and then full years ending June 30. The cost of the '
    'change is that extra return, at ' + PRICE + '.</p>'),
   ('approval', 'The Approval Is the Part That Is Not Automatic',
    '<p>A fiscal year-end is fixed by the first return filed. Changing it '
    'needs the written approval of the Canada Revenue Agency, and the request '
    'is made before the change rather than demonstrated by filing.</p>\n'
    '<p>A return filed carrying a year-end that does not match the record is '
    'not read as a change of year-end. It is rejected against the date on '
    'record, which means the year is still outstanding and the transmission '
    'achieved nothing. The '
    + a(T + 'corporate-fiscal-year-end-calculator/',
        'corporate fiscal year end calculator')
    + ' works from the date on record.</p>'),
   ('the-ceiling', 'The New Date Cannot Be More Than 53 Weeks Out',
    '<p>A tax year cannot exceed 53 weeks, which is 371 days. Where the gap '
    'between the current year-end and the proposed one is longer than that, '
    'the gap is not a single period and cannot be reported as one.</p>\n'
    '<p>Reaching a year-end that far out means an intervening year-end first, '
    'so two returns rather than one. The calculator says so where the dates '
    'you enter have that effect.</p>'),
   ('short-not-early', 'A Short Period Does Not Get an Early Deadline',
    '<p>The six-month rule runs from the day the period ends, whatever the '
    'period&#8217;s length. A two-month stub has six months after it to file, '
    'which is three times the period itself.</p>\n'
    '<p>What a short period does bring forward is the next year-end, and with '
    'it the next return. The '
    + a(T + 'two-t2-returns-in-one-year-checker/',
        'two T2 returns in one year checker')
    + ' shows how close together two deadlines can land after a change like '
    'this.</p>'),
  ],
  faq=[
   ('Can I change my corporation&#8217;s fiscal year-end?',
    'With the written approval of the Canada Revenue Agency. The request is '
    'made before the change, and filing a return with a different date on it '
    'does not change the year-end on record.'),
   ('Does changing a year-end mean an extra return?',
    'Usually yes. The change closes a period on the new date and that period '
    'is a tax year with its own return, at ' + PRICE + '.'),
   ('How long can the period created be?',
    'No longer than 53 weeks, which is 371 days. A gap longer than that is '
    'not one tax year and needs an intervening year-end.'),
   ('When is the return for that period due?',
    'Six months after the day the period ends, moved to the next business day '
    'where that falls on a weekend or a public holiday. A short period gets '
    'the same six months as a full year.'),
   ('What happens if I just file on the new date?',
    'The return is rejected against the year-end on record. The year stays '
    'outstanding, so nothing has been filed and nothing has been changed.'),
  ]),

 dict(slug='two-t2-returns-in-one-year-checker',
  title='Two T2 Returns in One Year Checker | Both Deadlines',
  h1_pre='Two T2 Returns ', h1_span='in One Year Checker',
  h1='Two T2 Returns in One Year Checker',
  eyebrow='Date Tool', keyword='two t2 returns in one year checker',
  meta=('Two tax years can both come due in one calendar year. Enter the two '
        'year-ends for both deadlines, the gap and the total.'),
  tags=['Both T2 dates', 'Days between them',
        'Flags a tight gap', 'Each year is its own return'],
  form=tool('The two year-ends',
            [date('y1', 'The earlier year-end'),
             date('y2', 'The later year-end')],
            'Enter both year-ends and both deadlines appear here.'),
  js=None,
  sections=[
   ('how-it-happens', 'Three Ways a Corporation Ends Up With Two',
    '<p>A short first year followed by a full one is the commonest. A '
    'corporation incorporated in October with a December 31 year-end has a '
    'three-month first year and then a full one, and both returns come due '
    'within six months of each other.</p>\n'
    '<p>An approved change of year-end is the second, and a final period '
    'ending at dissolution is the third. In each case the two periods are '
    'separate tax years, and nothing about them being close together merges '
    'them.</p>'),
   ('the-trap', 'Two Deadlines Close Together Read as One',
    '<p>This is the practical failure. Two dates a few months apart look like '
    'one obligation, the later one gets filed, and the earlier year sits '
    'outstanding without anyone noticing, often for years.</p>\n'
    '<p>An unfiled year does not expire. It stays open, invites a demand to '
    'file, and blocks a clearance certificate. The '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' is the page for working out whether this has already happened.</p>'),
   ('still-two-fees', 'Two Returns Means Two Returns',
    '<p>Each tax year is its own return whatever its length, so two periods '
    'in one calendar year are two returns at ' + PRICE + ' each. A '
    'three-month period is not a part-return and is not priced as one.</p>\n'
    '<p>They can be prepared and transmitted together, which is how a '
    'catch-up is handled, and they are prepared oldest first because the '
    'closing balances of the first year open the second.</p>'),
   ('order', 'Why the Order Cannot Be Reversed',
    '<p>The second return opens from figures the first one establishes: '
    'retained earnings, the undepreciated balance on Schedule 8, the loss '
    'continuity. Filing the later year first means filing opening figures '
    'that have not been reported yet.</p>\n'
    '<p>The '
    + a(T + 'retained-earnings-rollforward-calculator/',
        'retained earnings rollforward calculator')
    + ' gives the figure the second year has to open from.</p>'),
  ],
  faq=[
   ('Can a corporation file two T2 returns in one year?',
    'Yes, and it must where two tax years end close together. A short first '
    'year followed by a full one, an approved change of year-end and a final '
    'period at dissolution all produce two.'),
   ('Do two returns cost twice as much?',
    'Yes. Each tax year is its own return at ' + PRICE + ' whatever the '
    'length of the period it covers.'),
   ('Can both be filed at the same time?',
    'They can be prepared and transmitted together. They are prepared oldest '
    'first, because the closing balances of the earlier year open the '
    'later one.'),
   ('What if I only filed the later one?',
    'The earlier year is outstanding. It does not expire, it invites a demand '
    'to file, and it blocks a clearance certificate until it is filed.'),
   ('Is the deadline for the short period earlier?',
    'No. The six-month rule runs from the day each period ends, so a short '
    'period gets the same six months as a full year.'),
  ]),

 dict(slug='mandatory-t2-efile-checker',
  title='Mandatory T2 E-Filing Checker | Tax Years After 2023',
  h1_pre='Mandatory T2 ', h1_span='E-Filing Checker',
  h1='Mandatory T2 E-Filing Checker',
  eyebrow='Filing Method', keyword='mandatory t2 efile checker',
  meta=('Electronic filing is mandatory for tax years starting after 2023. '
        'Enter the first day of the tax year to see which side it falls on.'),
  tags=['One date decides it', 'Tax years starting after 2023',
        'Matters most on a catch-up', 'Every return here is electronic'],
  form=tool('The tax year',
            [date('st', 'The first day of the tax year')],
            'Enter the first day of the tax year.'),
  js=None,
  sections=[
   ('the-rule', 'The Rule Turns on One Date',
    '<p>Electronic filing of the T2 is mandatory for tax years starting after '
    '2023. There is no revenue test and no size test in it: a tax year '
    'beginning on or after January 1, 2024 is inside the rule and one '
    'beginning earlier is not.</p>\n'
    '<p>Note that the date tested is the first day of the tax year, not the '
    'year-end and not the day the return is filed. A year that began in '
    'December 2023 and ended in November 2024 began before the rule.</p>'),
   ('catch-up', 'Where This Actually Matters: a Catch-Up',
    '<p>For a single current year the answer is academic, because the return '
    'is going to be transmitted electronically either way. It matters on a '
    'catch-up, where the oldest years in the sequence may predate the rule '
    'while the newest sit inside it.</p>\n'
    '<p>That is a sequence filed under two regimes at once, which is worth '
    'knowing about and makes no difference to how it is done. The '
    + a(T + 'catch-up-filing-schedule-generator/',
        'catch-up filing schedule generator')
    + ' lays out the years and their dates.</p>'),
   ('paper', 'Filing on Paper Where It Is Mandatory Carries a Penalty',
    '<p>There is a penalty for filing on paper where electronic filing is '
    'required. This page does not state the amount, and that is deliberate: a '
    'penalty figure read off a web page is a figure read from the wrong '
    'place.</p>\n'
    '<p>The '
    + a(G + 'mandatory-t2-electronic-filing/',
        'guide to mandatory T2 electronic filing')
    + ' is where that sits. What this checker answers is the prior question, '
    'which is whether the requirement reaches the year in front of you.</p>'),
   ('how-here', 'Every Return Filed Here Is Transmitted Electronically',
    '<p>Gondaliya CPA Professional Corporation is a registered EFILE '
    'electronic filer. Returns are prepared and transmitted in Canada, and '
    'that is true of years the rule never reached as much as years inside '
    'it.</p>\n'
    '<p>So the practical answer for a visitor is that this changes nothing '
    'about their filing. You sign Form T183CORP and the return is '
    'transmitted. The '
    + a(T + 't183corp-signature-requirement-checker/',
        'Form T183CORP signature requirement checker')
    + ' covers that step.</p>'),
  ],
  faq=[
   ('Is electronic T2 filing mandatory?',
    'For tax years starting after 2023, yes. A tax year beginning on or after '
    'January 1, 2024 is inside the requirement.'),
   ('Which date does the rule test?',
    'The first day of the tax year, not the year-end and not the filing date. '
    'A year that began in December 2023 began before the rule.'),
   ('Is there a revenue threshold?',
    'Not in this rule. It turns on when the tax year started, which is why '
    'one date answers it.'),
   ('What happens if a return is filed on paper?',
    'There is a penalty for filing on paper where electronic filing is '
    'required. The amount is not stated here; the guide to mandatory T2 '
    'electronic filing covers it.'),
   ('Does this change how my nil return is filed?',
    'No. Gondaliya CPA Professional Corporation is a registered EFILE '
    'electronic filer and transmits every return electronically, including '
    'years the requirement never reached.'),
  ]),

 dict(slug='business-days-between-dates-calculator',
  title='Business Days Between Dates Calculator | Ontario Holidays',
  h1_pre='Business Days ', h1_span='Between Dates Calculator',
  h1='Business Days Between Dates Calculator',
  eyebrow='Date Tool', keyword='business days between dates calculator',
  meta=('Enter two dates for the calendar days, the business days, the '
        'weekend days and every Ontario public holiday in the span.'),
  tags=['Counts both ends', 'Nine Ontario holidays',
        'Names each holiday', 'The calendar every date tool here uses'],
  form=tool('The two dates',
            [date('f', 'From, counted'),
             date('t', 'To, also counted')],
            'Enter both dates and the counts appear here.'),
  js=None,
  sections=[
   ('why-two-counts', 'Calendar Days and Business Days Answer Different '
    'Questions',
    '<p>A deadline runs on calendar days. The work of meeting it runs on '
    'business days, and on a short span the two differ by enough to change a '
    'decision: ten calendar days over a long weekend is six business '
    'days.</p>\n'
    '<p>A demand to file is where this bites hardest, because the letter '
    'names a date that may be close. The '
    + a(T + 'cra-demand-to-file-deadline-calculator/',
        'CRA demand to file deadline calculator')
    + ' does both counts against a letter.</p>'),
   ('the-nine', 'The Nine Holidays, and Whose They Are',
    '<p>The calendar here is Ontario&#8217;s nine public holidays under the '
    'Employment Standards Act: New Year&#8217;s Day, Family Day, Good Friday, '
    'Victoria Day, Canada Day, Labour Day, Thanksgiving Day, Christmas Day '
    'and Boxing Day.</p>\n'
    '<p>Good Friday moves every year because it is derived from Easter, and '
    'Family Day, Victoria Day, Labour Day and Thanksgiving Day are each '
    'defined by a weekday rather than a date. The calculator works all of '
    'them out rather than reading them from a table, so no year is '
    'missing.</p>'),
   ('one-calendar', 'Every Date Tool Here Runs on This Calendar',
    '<p>This matters more than it sounds. A site with forty date tools can '
    'easily end up with two holiday lists and two answers for the same date, '
    'and a visitor who notices has no way to tell which one to trust.</p>\n'
    '<p>There is one list, in one shared module, and every tool calls it. The '
    + a(T + 'due-date-weekend-holiday-shift-calculator/',
        'due date weekend and holiday shift calculator')
    + ' shows the shift a single date gets from it.</p>'),
   ('counted-once', 'A Holiday on a Weekend Is Counted Once',
    '<p>Where a public holiday falls on a Saturday or a Sunday, this counts it '
    'as a weekend day and not again as a holiday. That keeps the three counts '
    'adding up to the calendar total, which is the property that makes them '
    'checkable.</p>\n'
    '<p>It also means such a holiday does not appear in the list of named '
    'holidays below the counts. The list is the holidays that cost a business '
    'day, not every holiday in the span.</p>'),
  ],
  faq=[
   ('How many business days are between two dates?',
    'Enter both and the calculator counts them. Both dates are included, so a '
    'Monday to the following Monday is eight calendar days.'),
   ('Which holidays does this use?',
    'Ontario&#8217;s nine public holidays under the Employment Standards Act. '
    'It is the same calendar every date tool on this site runs on.'),
   ('Are both dates counted?',
    'Yes. The span is inclusive at both ends, which is how a filing period is '
    'normally read.'),
   ('What about a holiday that falls on a weekend?',
    'It is counted once, as a weekend day, so the three counts still add up '
    'to the calendar total. It is not listed among the named holidays.'),
   ('Does this apply outside Ontario?',
    'The holiday list is Ontario&#8217;s. A province with a different list '
    'will differ on a span containing one of its own holidays.'),
  ]),
]

TOOLS7 += [
 dict(slug='t183corp-signature-requirement-checker',
  title='Form T183CORP Signature Requirement Checker | Who Signs',
  h1_pre='Form T183CORP ', h1_span='Signature Requirement Checker',
  h1='Form T183CORP Signature Requirement Checker',
  eyebrow='T183CORP', keyword='t183corp signature requirement checker',
  meta=('Form T183CORP needs an authorized signing officer, signed before '
        'transmission. Three answers show whether those conditions are met.'),
  tags=['Authorized signing officer', 'Signed before transmission',
        'Date and HH:MM:SS, Eastern', 'Kept six years, not sent to CRA'],
  form=tool('The signature',
            [yn('off', 'Are you an authorized signing officer of the '
                       'corporation?'),
             yn('red', 'Have you read the figures the form carries?'),
             yn('bef', 'Is the form being signed before the return is '
                       'transmitted?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('what-it-is', 'What Form T183CORP Is For',
    '<p>Form T183CORP is the authorization that lets a return be transmitted '
    'electronically on a corporation&#8217;s behalf. It carries the figures '
    'on your own return, and signing it is how you confirm those figures '
    'before anything is sent.</p>\n'
    '<p>It is always Form T183CORP. The name is never shortened on this '
    'site, because the shorter name belongs to a different authorization '
    'for a different return and the two are not interchangeable.</p>'),
   ('who-signs', 'An Authorized Signing Officer, Not Just Anyone Involved',
    '<p>The form is signed by an authorized signing officer of the '
    'corporation. A bookkeeper, a spouse, a shareholder who is not an officer '
    'and the accountant preparing the return are none of them that, however '
    'closely they are involved.</p>\n'
    '<p>The officer also has to have read the figures. The signature is a '
    'confirmation of the return&#8217;s contents, so signing without reading '
    'it is not the thing the form is asking for.</p>'),
   ('before', 'Before Transmission, and the Timestamp Proves It',
    '<p>The form is signed before the return is transmitted, not alongside it '
    'and not afterwards. It authorizes the transmission, so it has to exist '
    'first.</p>\n'
    '<p>Here it is signed on a single-use access-controlled screen, and the '
    'date and the hour, minute and second are recorded on the server in '
    'Eastern Time. It is never backdated. The timestamp is written as you '
    'sign, which is what makes the sequence demonstrable rather than '
    'asserted.</p>'),
   ('kept', 'The Firm Keeps It for Six Years and Does Not Send It',
    '<p>The signed form stays with Gondaliya CPA Professional Corporation for '
    'six years. It is not sent to the Canada Revenue Agency unless the Canada '
    'Revenue Agency asks for it.</p>\n'
    '<p>That surprises people who expect the signature to travel with the '
    'return. It does not. The transmission carries the return; the form is '
    'the record of the signature that permitted it, held in case it is ever '
    'asked for. The '
    + a(G + 't183corp-signing-and-transmission/',
        'guide to T183CORP signing and transmission')
    + ' sets out the whole sequence.</p>'),
  ],
  faq=[
   ('Who can sign Form T183CORP?',
    'An authorized signing officer of the corporation. A bookkeeper, a '
    'non-officer shareholder or the accountant preparing the return cannot '
    'sign it in that officer&#8217;s place.'),
   ('When is Form T183CORP signed?',
    'Before the return is transmitted. It authorizes the transmission, so it '
    'has to exist first, and the timestamp recorded as you sign shows that '
    'it did.'),
   ('Is Form T183CORP sent to CRA?',
    'No, unless the Canada Revenue Agency asks for it. The transmission '
    'carries the return; the signed form is the record of the signature '
    'that permitted it.'),
   ('How long is it kept?',
    'Gondaliya CPA Professional Corporation keeps the signed form for six '
    'years.'),
   ('Can the form be backdated?',
    'No. The date and the hour, minute and second are written by the server '
    'in Eastern Time as you sign.'),
  ]),

 dict(slug='provincial-return-requirement-checker',
  title='Provincial Return Requirement Checker | CO-17 and AT1',
  h1_pre='Provincial Return ', h1_span='Requirement Checker',
  h1='Provincial Return Requirement Checker',
  eyebrow='Provincial', keyword='provincial return requirement checker',
  meta=('Quebec and Alberta each collect their own corporate tax. Two '
        'answers show whether CO-17 or AT1 is a separate return to file.'),
  tags=['Quebec: CO-17', 'Alberta: AT1',
        'Separate returns, separate filings', 'Not covered by the fee'],
  form=tool('Where the corporation operates',
            [yn('qc', 'Does the corporation have a permanent establishment '
                      'in Quebec?'),
             yn('ab', 'Does it have one in Alberta?')],
            'Answer both questions.'),
  js=None,
  sections=[
   ('two-provinces', 'Two Provinces Collect Their Own Corporate Tax',
    '<p>In most of Canada the province levies its corporate income tax '
    'through the federal return, so one T2 settles both. Quebec and Alberta '
    'do not. Each administers its own corporate tax and each has its own '
    'return.</p>\n'
    '<p>Quebec&#8217;s is CO-17, filed with Revenu Quebec. Alberta&#8217;s is '
    'AT1. Both are separate returns in their own right, not schedules '
    'attached to the T2 and not something the T2 covers.</p>'),
   ('still-nil', 'A Quiet Year Is Quiet on Both Returns',
    '<p>A corporation with no activity has nothing to report provincially '
    'either, so the provincial return for that year is nil in the same way '
    'the federal one is.</p>\n'
    '<p>Being nil does not make it optional. It is a separate return, filed '
    'separately, on its own deadline, and the obligation follows from the '
    'permanent establishment rather than from there being anything to '
    'report.</p>'),
   ('not-covered', 'What the Fee Covers, Said Plainly',
    '<p>The fee of ' + PRICE + ' covers one nil federal T2 return for one '
    'corporation for one tax year. CO-17 is not covered by it, and neither '
    'is AT1.</p>\n'
    '<p>That is worth being direct about rather than leaving a visitor to '
    'discover it. The '
    + a(COST, 'nil T2 filing cost') + ' page sets out the whole boundary of '
    'what sits inside the fee and what does not.</p>'),
   ('not-the-registry', 'The Registry Annual Return Is a Different Thing',
    '<p>Every corporation also owes an annual return to the registry it is '
    'incorporated with, federally or provincially. That is a registry filing '
    'confirming the directors and the registered office, and it reports no '
    'income.</p>\n'
    '<p>It is easy to hear "provincial return" and think of that one. They '
    'are unrelated obligations with different consequences: missing a '
    'registry annual return gets a corporation struck, which the '
    + a(T + 'involuntary-dissolution-risk-checker/',
        'involuntary dissolution risk checker')
    + ' covers.</p>'),
  ],
  faq=[
   ('Does Quebec have a separate corporate tax return?',
    'Yes. CO-17 is a separate provincial return, filed with Revenu Quebec. It '
    'is not part of the federal T2.'),
   ('Does Alberta have one?',
    'Yes. AT1 is a separate provincial return in the same way.'),
   ('Is CO-17 or AT1 covered by the fee?',
    'No. The fee of ' + PRICE + ' covers one nil federal T2 return for one '
    'corporation for one tax year.'),
   ('What about the other provinces?',
    'Elsewhere the province levies its corporate income tax through the '
    'federal return, so the T2 is the only corporate income tax return.'),
   ('Is a nil provincial return still required?',
    'The obligation follows the permanent establishment rather than there '
    'being something to report, so a nil year is still a return to file.'),
  ]),

 dict(slug='cra-account-closure-sequencer',
  title='CRA Account Closure Sequencer | What Order and What It Costs',
  h1_pre='CRA Account ', h1_span='Closure Sequencer',
  h1='CRA Account Closure Sequencer',
  eyebrow='Accounts', keyword='cra account closure sequencer',
  meta=('Payroll and GST/HST accounts outlive the activity that opened them. '
        'Three answers give the order of closure and what each step costs.'),
  tags=['Ordered steps', 'Form RC145 closes two of them',
        'Says what is outside the fee', 'Returns come first'],
  form=tool('What is open',
            [yn('rp', 'Is a payroll account open?'),
             yn('rt', 'Is a GST/HST account open?'),
             yn('dis', 'Do you intend to dissolve the corporation?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('accounts-outlive', 'Accounts Outlive the Activity That Opened Them',
    '<p>A business number carries separate accounts: corporate income tax, '
    'payroll, GST/HST. Each is opened for a reason and each stays open until '
    'it is closed, whatever happens to the reason.</p>\n'
    '<p>That is how a dormant corporation ends up with obligations it has no '
    'activity to match. The payroll account from when it had staff and the '
    'GST/HST account from when it was registered both keep generating returns '
    'and remittances, separately from the T2.</p>'),
   ('returns-first', 'The Outstanding Returns Come First',
    '<p>Closing an account does not clear what was owed on it, and it does '
    'not file anything. A closure on top of unfiled years leaves the unfiled '
    'years exactly where they were.</p>\n'
    '<p>So the sequence starts with the returns. The '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' identifies which are outstanding and the '
    + a(T + 'catch-up-filing-schedule-generator/',
        'catch-up filing schedule generator')
    + ' dates them.</p>'),
   ('rc145', 'Form RC145 Closes Both of the Accounts That Matter Here',
    '<p>One form closes a payroll account and the same form closes a GST/HST '
    'account. Until an account is closed, nil returns and nil remittances '
    'remain due on it.</p>\n'
    '<p>Neither closure is covered by the nil T2 fee, which is one of the '
    'clearest boundaries on the site: the fee is for a return, and closing an '
    'account is not a return. The '
    + a(T + 'gst-hst-account-closure-checker/',
        'GST/HST account closure checker')
    + ' and the '
    + a(T + 'payroll-nil-remittance-checker/',
        'payroll nil remittance checker')
    + ' each go further into one of them.</p>'),
   ('why-order', 'Why the Order Is Not Arbitrary at a Wind-Up',
    '<p>A clearance request rests on a complete filing record, so it comes '
    'after the returns rather than alongside them. The registry filing comes '
    'last, because dissolving a corporation that still owes returns leaves '
    'the tax years open behind it.</p>\n'
    '<p>Out of order, each step still happens but none of them finishes the '
    'job. The '
    + a(T + 'dissolution-readiness-checker/',
        'dissolution readiness checker')
    + ' tests whether the corporation is ready for the last step.</p>'),
  ],
  faq=[
   ('How do I close a CRA payroll or GST/HST account?',
    'With Form RC145, which closes either one. Until the account is closed, '
    'nil returns and nil remittances remain due on it.'),
   ('Should I close the accounts before filing the returns?',
    'No. Closing an account does not file anything and does not clear what '
    'was owed on it, so the outstanding returns come first.'),
   ('Is closing an account covered by the fee?',
    'No. The fee of ' + PRICE + ' is for a nil T2 return. An account closure '
    'is not a return and sits outside it.'),
   ('Why does a dormant corporation still owe anything?',
    'Because the obligation follows the open account rather than the '
    'activity. An account nobody closed keeps generating returns and '
    'remittances.'),
   ('Where does the clearance certificate come in the order?',
    'After the returns, including the final one, because the request rests on '
    'a complete filing record. The registry dissolution comes after that.'),
  ]),

 dict(slug='corporate-deadline-calendar-generator',
  title='Corporate Deadline Calendar Generator | Every Date, One Input',
  h1_pre='Corporate Deadline ', h1_span='Calendar Generator',
  h1='Corporate Deadline Calendar Generator',
  eyebrow='Calendar', keyword='corporate deadline calendar generator',
  meta=('One year-end in, the whole corporate calendar out: the balance '
        'date, the T2 date, the T4 date, the annual return and the next '
        'year-end.'),
  tags=['One input, every date', 'All on one holiday calendar',
        'Shows what is outside the fee', 'Links each date to its own tool'],
  form=tool('Your corporation',
            [date('ye', 'The fiscal year-end'),
             date('inc', 'The incorporation date, for a federal corporation'),
             yn('fed', 'Is the corporation federally incorporated?'),
             yn('pay', 'Is a payroll account open?')],
            'Enter the year-end and answer both questions.'),
  js=None,
  sections=[
   ('one-page', 'Every Date a Corporation Owes, From One Year-End',
    '<p>The single-purpose tools on this site each answer one date well. What '
    'they do not do is show you the shape of a year, which is what someone '
    'who has just picked a year-end actually wants.</p>\n'
    '<p>This page restates dates those tools own and links to each of them. '
    'Where you want one date in depth, follow the link; where you want to see '
    'how they sit together, stay here.</p>'),
   ('not-all-from-year-end', 'Not Every Date Derives From the Year-End',
    '<p>Two of the rows do not. The T4 information return reports a calendar '
    'year and is due at the end of the following February whatever year-end '
    'the corporation uses, so a June year-end puts the T2 in December and the '
    'T4 at the end of February.</p>\n'
    '<p>The federal annual return runs from the incorporation anniversary, '
    'which is why this page asks for that date separately. The '
    + a(T + 'federal-annual-return-anniversary-calculator/',
        'federal annual return anniversary calculator')
    + ' is the page for that one on its own.</p>'),
   ('inside-outside', 'Which of These the Fee Covers',
    '<p>One of them. The fee of ' + PRICE + ' covers the nil T2 return. The '
    'registry annual return is a registry filing and sits outside it, and so '
    'does the T4 information return and any account closure.</p>\n'
    '<p>Saying that on the calendar rather than in the small print is the '
    'point of the third column. A visitor should be able to see the whole '
    'obligation and the boundary of the service in the same table.</p>'),
   ('one-calendar', 'Every Row Moves Off a Weekend the Same Way',
    '<p>Each date here is moved to the next business day where it falls on a '
    'Saturday, a Sunday or an Ontario public holiday, on the one shared '
    'holiday calendar. Two rows can shift by different amounts, which is '
    'correct rather than inconsistent.</p>\n'
    '<p>The balance row assumes the two-month period. A '
    'Canadian-controlled private corporation meeting the conditions has '
    'three months, which the '
    + a(T + 'corporate-balance-due-date-calculator/',
        'corporate balance due date calculator')
    + ' handles.</p>'),
  ],
  faq=[
   ('What deadlines does a corporation have each year?',
    'A balance of tax date two months after the year-end, or three for a '
    'qualifying CCPC, the T2 six months after it, the registry annual return, '
    'and a T4 information return where a payroll account is open.'),
   ('Which of them does a nil corporation actually have to meet?',
    'The T2 filing date and the registry annual return. A nil year has no '
    'balance to pay, so the earlier date passes with nothing owed on it.'),
   ('Why does the T4 date not follow my year-end?',
    'Because the T4 reports a calendar year. It is due at the end of the '
    'following February whatever fiscal year-end the corporation uses.'),
   ('Why do you need my incorporation date?',
    'The federal annual return runs from the incorporation anniversary, not '
    'from the fiscal year-end, so that row cannot be derived from the '
    'year-end.'),
   ('Are all these dates covered by the fee?',
    'No. The fee of ' + PRICE + ' covers the nil T2 return. The registry '
    'annual return, the T4 return and account closures all sit outside it.'),
  ]),

 dict(slug='catch-up-filing-schedule-generator',
  title='Catch-Up Filing Schedule Generator | A Row Per Unfiled Year',
  h1_pre='Catch-Up Filing ', h1_span='Schedule Generator',
  h1='Catch-Up Filing Schedule Generator',
  eyebrow='Catch-Up', keyword='catch-up filing schedule generator',
  meta=('Enter the earliest unfiled year-end and how many years are '
        'outstanding for a dated schedule, a row per year, and the total.'),
  tags=['A row per year', 'Each deadline and how overdue',
        'Oldest first, and why', 'Total at the per-year price'],
  form=tool('The outstanding years',
            [date('y1', 'The earliest unfiled year-end'),
             num('n', 'How many years are unfiled', '', 1, 20, '5')],
            'Enter the earliest unfiled year-end and the number of years.'),
  js=None,
  sections=[
   ('three-tools', 'This Is the Third of Three Catch-Up Tools',
    '<p>The family has two already and they answer different questions, so it '
    'is worth saying which is which rather than leaving you to find out.</p>\n'
    '<p>The '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' works out <em>which</em> years are outstanding. The '
    + a(T + 'unfiled-years-cost-calculator/',
        'unfiled years cost calculator')
    + ' gives <em>what the whole catch-up costs</em>. This page gives the '
    '<em>dated schedule</em>: a row per year, with its deadline and how '
    'overdue it is.</p>'),
   ('oldest-first', 'Oldest First Is Not a Preference',
    '<p>Each year&#8217;s return opens from the closing balances of the one '
    'before it: retained earnings, the undepreciated balance on Schedule 8, '
    'the loss continuity. A year filed out of order carries opening figures '
    'that have not been established.</p>\n'
    '<p>That is why the schedule is numbered. The order is part of the work '
    'rather than a tidy way of presenting it, and the '
    + a(T + 'retained-earnings-rollforward-calculator/',
        'retained earnings rollforward calculator')
    + ' is what carries one year&#8217;s closing figure into the next.</p>'),
   ('one-sitting', 'Prepared in Order, Transmitted Together',
    '<p>The years are prepared in sequence and can then be transmitted in one '
    'sitting. You sign one Form T183CORP for each year, because each year is '
    'its own return and each transmission needs its own signature.</p>\n'
    '<p>Each year is ' + PRICE + ', so the total is the number of years at '
    'that price. There is no discount for volume and no part-year rate: a '
    'three-month stub period is a return like any other.</p>'),
   ('what-overdue-means', 'What the Overdue Column Does and Does Not Say',
    '<p>It counts days past the filing deadline, which is a fact about the '
    'calendar. It is not a penalty calculation and it does not grow into one '
    'on a true nil year.</p>\n'
    '<div class="ei-danger"><p>' + QUAL + '</p></div>\n'
    '<p>The '
    + a(T + 'nil-return-late-penalty-checker/',
        'nil return late penalty checker')
    + ' works through that distinction properly, and the '
    + a(G + 'catch-up-unfiled-corporate-tax-returns/',
        'guide to catching up on unfiled corporate tax returns')
    + ' sets out the whole process.</p>'),
  ],
  faq=[
   ('How do I catch up on several unfiled T2 returns?',
    'Oldest first, because each year opens from the closing balances of the '
    'one before it. Once prepared they can be transmitted together.'),
   ('How much does a catch-up cost?',
    'Each tax year is its own return at ' + PRICE + ', so the total is the '
    'number of outstanding years at that price.'),
   ('Can several years be filed at once?',
    'They are prepared in order and can then be transmitted in one sitting. '
    'You sign one Form T183CORP for each year.'),
   ('Does an unfiled year eventually expire?',
    'No. It stays open, invites a demand to file and an arbitrary assessment, '
    'and blocks a clearance certificate until it is filed.'),
   ('Does the overdue count mean I owe a penalty?',
    'It counts days past the deadline, not money. On a true nil year the '
    'percentage late-filing penalty is a percentage of tax owing, and the '
    'corporation owes $0.00.'),
  ]),
]

# ---------------------------------------------------------------------------
# Static reference tables.
#
# Tools 1 to 30 each carry a table in the body prose that a visitor can read
# without touching the form: tool 21's is "What happened / Effect on the count
# / Returns owed". Batches 6 and 7 shipped without one and only drew a table
# after input, which Navneet spotted by comparing a new page against tool 21.
#
# Each table below is a reference a visitor wants before they have entered
# anything, built from facts already approved or already on the site. None of
# them is padding: where a page had nothing worth tabulating it would not get
# a table, and the guard below would fail the build rather than let one ship
# with a filler table.
#
# They attach to a named section so the position is explicit rather than
# implied by list order.
# ---------------------------------------------------------------------------

def _tbl(head, rows):
    h = ('<table class="ei-tbl"><thead><tr>'
         + ''.join('<th scope="col">%s</th>' % c for c in head)
         + '</tr></thead><tbody>')
    for r in rows:
        h += '<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>'
    return h + '</tbody></table>'


TABLES = {
 'first-t2-year-end-options-generator': ('late-or-early', _tbl(
   ['Where the first year-end falls', 'First tax year',
    'Returns in the first two years', 'What it costs you'],
   [['The earliest month-end available', 'A few weeks', 'Two',
     'A return for a few weeks of nothing'],
    ['A month-end around twelve months out', 'Close to a full year', 'One',
     'The usual choice'],
    ['The latest month-end inside 53 weeks', 'Up to 371 days', 'One',
     'The latest first deadline, and that date every year after']])),

 'year-end-change-impact-calculator': ('what-it-creates', _tbl(
   ['How a year-end moves', 'What creates the period', 'Approval needed'],
   [['An approved change', 'The new date closes a period early',
     'Written approval from the Canada Revenue Agency'],
    ['An amalgamation', 'Each predecessor&#8217;s year ends the day before',
     'None, the amalgamation sets it'],
    ['A dissolution', 'The final period ends on the dissolution date',
     'None, the dissolution sets it']])),

 'two-t2-returns-in-one-year-checker': ('how-it-happens', _tbl(
   ['How it happens', 'The two periods', 'Returns owed'],
   [['Incorporated part-way through a year',
     'A short first tax year, then a full one', 'One for each'],
    ['An approved change of year-end',
     'A stub period at the changeover, then full years', 'One for each'],
    ['Dissolved part-way through a year',
     'A full year, then a short final period', 'One for each']])),

 'mandatory-t2-efile-checker': ('the-rule', _tbl(
   ['Tax year begins', 'Electronic filing', 'What it means on a catch-up'],
   [['Before January 1, 2024', 'Not mandatory',
     'Paper was an option for these years'],
    ['On or after January 1, 2024', 'Mandatory',
     'Filing on paper carries a penalty']])),

 'business-days-between-dates-calculator': ('the-nine', _tbl(
   ['Public holiday', 'How the date is set'],
   [['New Year&#8217;s Day', 'January 1'],
    ['Family Day', 'The third Monday in February'],
    ['Good Friday', 'Two days before Easter Sunday, so it moves each year'],
    ['Victoria Day', 'The Monday on or before May 24'],
    ['Canada Day', 'July 1'],
    ['Labour Day', 'The first Monday in September'],
    ['Thanksgiving Day', 'The second Monday in October'],
    ['Christmas Day', 'December 25'],
    ['Boxing Day', 'December 26']])),

 't183corp-signature-requirement-checker': ('who-signs', _tbl(
   ['Who it is', 'Can sign Form T183CORP'],
   [['An authorized signing officer of the corporation', 'Yes'],
    ['A shareholder who is not an officer', 'No'],
    ['The bookkeeper', 'No'],
    ['The accountant who prepared the return', 'No'],
    ['A spouse or family member who is not an officer', 'No']])),

 'provincial-return-requirement-checker': ('two-provinces', _tbl(
   ['Where the corporation operates', 'Corporate income tax returns',
    'Covered by the fee'],
   [['Quebec', 'The federal T2 and CO-17', 'The T2 only'],
    ['Alberta', 'The federal T2 and AT1', 'The T2 only'],
    ['Everywhere else', 'The federal T2 on its own', 'The T2']])),

 'cra-account-closure-sequencer': ('accounts-outlive', _tbl(
   ['Account on the business number', 'What it is for', 'How it closes',
    'Covered by the fee'],
   [['Corporate income tax', 'The T2 return',
    'It ends with the corporation', 'The nil return is'],
    ['Payroll', 'T4 returns and remittances, including nil ones',
     'Form RC145', 'No'],
    ['GST/HST', 'GST/HST returns, including nil ones', 'Form RC145',
     'No']])),

 'corporate-deadline-calendar-generator': ('not-all-from-year-end', _tbl(
   ['Obligation', 'Measured from', 'Covered by the fee'],
   [['Balance of tax', 'Two months after the fiscal year-end, or three for a '
     'qualifying CCPC', 'Nothing is owed on a nil year'],
    ['The T2 return', 'Six months after the fiscal year-end', 'Yes'],
    ['The T4 information return',
     'The calendar year, due at the end of the following February', 'No'],
    ['The federal annual return',
     '60 days after the incorporation anniversary', 'No']])),

 'catch-up-filing-schedule-generator': ('three-tools', _tbl(
   ['What you want to know', 'The tool that answers it'],
   [['Which years are outstanding', 'Unfiled years checker'],
    ['What the whole catch-up costs', 'Unfiled years cost calculator'],
    ['The dated schedule, a row per year', 'This page']])),
}

assert set(TABLES) == {t['slug'] for t in TOOLS7}, (
    'every tool in the batch carries a reference table; TABLES does not '
    'match TOOLS7')

for t in TOOLS7:
    _sid, _html = TABLES[t['slug']]
    _ids = [s for s, _, _ in t['sections']]
    assert _sid in _ids, (
        '%s: table is attached to section %r, which the page does not have '
        '(it has %r)' % (t['slug'], _sid, _ids))
    t['sections'] = [(s, h, (b + '\n' + _html) if s == _sid else b)
                     for s, h, b in t['sections']]


SEO = {
 'first-t2-year-end-options-generator': (
   'First T2 Year-End Options Generator | Every Date',
   'Enter the incorporation date and every month-end available as a first '
   'year-end appears, with its T2 deadline.'),
 'year-end-change-impact-calculator': (
   'Year-End Change Impact Calculator | CRA Approval',
   'Moving a fiscal year-end creates a period and a return. Enter both dates '
   'for its length and its T2 deadline.'),
 'two-t2-returns-in-one-year-checker': (
   'Two T2 Returns in One Year Checker | Both Dates',
   'Two tax years can both come due in one calendar year. Enter the two '
   'year-ends for both deadlines and the gap.'),
 'mandatory-t2-efile-checker': (
   'Mandatory T2 E-Filing Checker | Tax Years After 2023',
   'Electronic filing is mandatory for tax years starting after 2023. Enter '
   'the first day of the tax year to test it.'),
 'business-days-between-dates-calculator': (
   'Business Days Between Dates Calculator | Ontario',
   'Enter two dates for the calendar days, the business days, the weekend '
   'days and every Ontario public holiday between.'),
 't183corp-signature-requirement-checker': (
   'Form T183CORP Signature Requirement Checker',
   'Form T183CORP needs an authorized signing officer, signed before '
   'transmission. Three answers test those conditions.'),
 'provincial-return-requirement-checker': (
   'Provincial Return Requirement Checker | CO-17, AT1',
   'Quebec and Alberta each collect their own corporate tax. Two answers '
   'show whether CO-17 or AT1 is a separate return.'),
 'cra-account-closure-sequencer': (
   'CRA Account Closure Sequencer | Payroll and GST/HST',
   'Payroll and GST/HST accounts outlive the activity that opened them. '
   'Three answers give the order and what it costs.'),
 'corporate-deadline-calendar-generator': (
   'Corporate Deadline Calendar Generator | One Input',
   'One year-end in, the whole corporate calendar out: the balance date, the '
   'T2 date, the T4 date and the annual return.'),
 'catch-up-filing-schedule-generator': (
   'Catch-Up Filing Schedule Generator | Dated Rows',
   'Enter the earliest unfiled year-end and how many years are outstanding '
   'for a dated schedule and the total.'),
}

for t in TOOLS7:
    t['seo_title'], t['seo_desc'] = SEO[t['slug']]
    assert len(t['seo_title']) <= 60, (
        '%s: SEO title is %d characters' % (t['slug'], len(t['seo_title'])))
    assert 70 <= len(t['seo_desc']) <= 160, (
        '%s: SEO description is %d characters'
        % (t['slug'], len(t['seo_desc'])))
assert set(SEO) == {t['slug'] for t in TOOLS7}, 'SEO map does not match TOOLS7'

for t, js in zip(TOOLS7, [T41_JS, T42_JS, T43_JS, T44_JS, T45_JS,
                          T46_JS, T47_JS, T48_JS, T49_JS, T50_JS]):
    t['js'] = js if js.startswith(PRELUDE) else PRELUDE + js

ORDER7 = ORDER6 + [t['slug'] for t in TOOLS7]
LINK_TITLE7 = dict(LINK_TITLE6, **{
 'first-t2-year-end-options-generator':
     'First T2 year-end options generator',
 'year-end-change-impact-calculator': 'Year-end change impact calculator',
 'two-t2-returns-in-one-year-checker':
     'Two T2 returns in one year checker',
 'mandatory-t2-efile-checker': 'Mandatory T2 e-filing checker',
 'business-days-between-dates-calculator':
     'Business days between dates calculator',
 't183corp-signature-requirement-checker':
     'Form T183CORP signature requirement checker',
 'provincial-return-requirement-checker':
     'Provincial return requirement checker',
 'cra-account-closure-sequencer': 'CRA account closure sequencer',
 'corporate-deadline-calendar-generator':
     'Corporate deadline calendar generator',
 'catch-up-filing-schedule-generator':
     'Catch-up filing schedule generator',
})

SIBLINGS7 = {
 'first-t2-year-end-options-generator': [
   '53-week-first-tax-year-checker', 'corporate-fiscal-year-end-calculator',
   'year-end-change-impact-calculator'],
 'year-end-change-impact-calculator': [
   'fiscal-period-length-calculator', 'short-tax-year-deadline-calculator',
   'two-t2-returns-in-one-year-checker'],
 'two-t2-returns-in-one-year-checker': [
   'short-tax-year-deadline-calculator',
   'first-t2-year-end-options-generator', 'nil-t2-deadline-calculator'],
 'mandatory-t2-efile-checker': [
   't183corp-signature-requirement-checker', 't2-short-eligibility-checker',
   'nil-t2-document-checklist-checker'],
 'business-days-between-dates-calculator': [
   'due-date-weekend-holiday-shift-calculator', 'days-overdue-calculator',
   'cra-demand-to-file-deadline-calculator'],
 't183corp-signature-requirement-checker': [
   'nil-t2-document-checklist-checker', 'mandatory-t2-efile-checker',
   'schedule-50-shareholder-threshold-checker'],
 'provincial-return-requirement-checker': [
   'federal-annual-return-anniversary-calculator',
   'involuntary-dissolution-risk-checker',
   'corporate-deadline-calendar-generator'],
 'cra-account-closure-sequencer': [
   'gst-hst-account-closure-checker', 'payroll-nil-remittance-checker',
   'dissolution-readiness-checker'],
 'corporate-deadline-calendar-generator': [
   'nil-t2-deadline-calculator', 'corporate-balance-due-date-calculator',
   'federal-annual-return-anniversary-calculator'],
 'catch-up-filing-schedule-generator': [
   'unfiled-years-checker', 'unfiled-years-cost-calculator',
   'days-overdue-calculator'],
}

GUIDES7 = {
 'first-t2-year-end-options-generator': [
   ('first-year-t2-filing', 'The complete guide to first-year T2 filing')],
 'year-end-change-impact-calculator': [
   ('t2-filing-deadlines', 'The complete guide to T2 filing deadlines')],
 'two-t2-returns-in-one-year-checker': [
   ('t2-filing-deadlines', 'The complete guide to T2 filing deadlines'),
   ('first-year-t2-filing', 'The complete guide to first-year T2 filing')],
 'mandatory-t2-efile-checker': [
   ('mandatory-t2-electronic-filing', 'Mandatory T2 electronic filing')],
 'business-days-between-dates-calculator': [
   ('t2-filing-deadlines', 'The complete guide to T2 filing deadlines')],
 't183corp-signature-requirement-checker': [
   ('t183corp-signing-and-transmission',
    'T183CORP signing and transmission')],
 'provincial-return-requirement-checker': [
   ('provincial-and-federal-annual-returns',
    'Provincial and federal annual returns')],
 'cra-account-closure-sequencer': [
   ('winding-up-an-inactive-corporation',
    'Winding up an inactive corporation'),
   ('final-t2-and-dissolution', 'The final T2 and dissolution')],
 'corporate-deadline-calendar-generator': [
   ('corporate-compliance-calendar', 'The corporate compliance calendar')],
 'catch-up-filing-schedule-generator': [
   ('catch-up-unfiled-corporate-tax-returns',
    'Catching up on unfiled corporate tax returns')],
}

_ORDER = set(ORDER7)

assert len(TOOLS7) == 10, '%d tools in batch 7' % len(TOOLS7)
assert len({t['slug'] for t in TOOLS7}) == 10, 'duplicate slug in the batch'

for t in TOOLS7:
    _sec = {sid for sid, _, _ in t['sections']}
    _fld = set(_re.findall(r'id="([\w-]+)"', t['form']))
    _fld |= set(_re.findall(r'name="([\w-]+)"', t['form']))
    _clash = _sec & _fld
    assert not _clash, ('%s: section anchor collides with a form id: %s'
                        % (t['slug'], sorted(_clash)))

    _vals = set(_re.findall(r'value="([^"]*)"', t['form']))
    assert _vals <= {'y', 'n'}, ('%s: form emits values outside {y,n}: %s'
                                 % (t['slug'], sorted(_vals - {'y', 'n'})))

    assert t['js'].count(PRELUDE) == 1, (
        '%s: the prelude appears %d times in its script'
        % (t['slug'], t['js'].count(PRELUDE)))

    if 'pick(' in t['js']:
        assert 'function pick(' in t['js'], (
            '%s: calls pick() without carrying its definition; build on '
            'RBASE rather than BASE' % t['slug'])

    if 'money(' in t['js']:
        assert 'function money(' in t['js'], (
            '%s: calls money() without carrying its definition; add MONEY_JS'
            % t['slug'])

    if 'holidayName(' in t['js']:
        assert 'function holidayName(' in t['js'], (
            '%s: calls holidayName() without carrying its definition; add '
            'HNAME_JS' % t['slug'])

    _show = t['js'].split('function show()')[1]
    if 'var h=' in _show:
        assert 'pick(' not in _show[_show.index('var h='):], (
            '%s: render reads pick() after the result is computed'
            % t['slug'])

    _ids = set(_re.findall(r'\bid="([\w-]+)"', t['form']))
    _got = set(_re.findall(r"getElementById\('([\w-]+)'\)", t['js']))
    _ghost = _got - _ids - {'out'}
    assert not _ghost, (
        '%s: getElementById(%s) matches no form field. yn() emits name= '
        'without a matching id, so a radio group cannot be bound this way.'
        % (t['slug'], sorted(_ghost)))

    # Every radio group the form emits is listened to, or the page renders
    # nothing when that group changes.
    _names = set(_re.findall(r'name="([\w-]+)"', t['form']))
    for _n in _names:
        assert 'input[name="%s"]' % _n in t['js'], (
            '%s: radio group %r has no change listener' % (t['slug'], _n))
        assert "pick('%s')" % _n in t['js'], (
            '%s: radio group %r is never read' % (t['slug'], _n))

    assert len(t['sections']) == 4, (
        '%s has %d sections' % (t['slug'], len(t['sections'])))
    assert len(t['faq']) == 5, '%s has %d FAQs' % (t['slug'], len(t['faq']))
    assert len(t['tags']) == 4, '%s has %d tags' % (t['slug'], len(t['tags']))

    _body = ' '.join(b for _, _, b in t['sections'])
    _body += ' '.join(q + ' ' + aa for q, aa in t['faq'])
    assert 'no penalty' not in _body.lower(), (
        '%s: the bare phrase "no penalty" appears' % t['slug'])

    # Rule 2: T183 is never written bare.
    assert not _re.search(r'T183(?!CORP)', _body + t['form'] + t['js']
                          + t['title'] + t['seo_title'] + t['seo_desc']), (
        '%s: T183 appears without CORP' % t['slug'])

    # The visible H1 and the schema headline are the same sentence.
    assert t['h1_pre'] + t['h1_span'] == t['h1'], (
        '%s: h1_pre + h1_span is %r but h1 is %r'
        % (t['slug'], t['h1_pre'] + t['h1_span'], t['h1']))

# Every slug is new, and every link target exists.
_LIVE = set(ORDER6)
for t in TOOLS7:
    assert t['slug'] not in _LIVE, '%s is already live' % t['slug']
    for s in SIBLINGS7[t['slug']]:
        assert s in _ORDER, '%s links to tool %s, which does not exist' % (
            t['slug'], s)
        assert s != t['slug'], '%s lists itself as a sibling' % t['slug']
        assert s in LINK_TITLE7, '%s has no link title' % s
    for g, _ttl in GUIDES7[t['slug']]:
        assert g in _GUIDES_LIVE, (
            '%s links to guide %s, which is not live' % (t['slug'], g))
assert set(SIBLINGS7) == {t['slug'] for t in TOOLS7}, 'SIBLINGS7 mismatch'
assert set(GUIDES7) == {t['slug'] for t in TOOLS7}, 'GUIDES7 mismatch'

for t in TOOLS7:
    _all = ' '.join(b for _, _, b in t['sections']) + t['form']
    for s in set(_re.findall(r'/tools/([a-z0-9-]+)/', _all)):
        assert s in _ORDER, (
            '%s: body links to /tools/%s/, which does not exist'
            % (t['slug'], s))
    for g in set(_re.findall(r'/guides/([a-z0-9-]+)/', _all)):
        assert g in _GUIDES_LIVE, (
            '%s: body links to /guides/%s/, which is not live'
            % (t['slug'], g))

for t in TOOLS7:
    rel = [(T + s + '/', LINK_TITLE7[s]) for s in SIBLINGS7[t['slug']]]
    rel += [(G + g + '/', ttl) for g, ttl in GUIDES7[t['slug']]]
    rel.append((COST, 'Nil T2 filing cost'))
    t['related'] = rel


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'October 29, 2026', '2026-10-29'
    recs = []
    for t in TOOLS7:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2g-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-46s %6d bytes' % (r['slug'], len(r['content'].encode())))
