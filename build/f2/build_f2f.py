"""Family 2, tools 31 to 40.

Ten more calculators and checkers from the Appendix A list of 150.

Which ten, and why these. The list still holds long runs of near-synonyms,
and line 1210 requires logic unique to each tool, so this batch was again
chosen for distinct logic rather than list order. Four are arithmetic the
visitor can check by hand, four are decision trees over facts the plan states
outright, and two are date arithmetic on the holiday engine already built and
tested for the deadline calculator, so no new unverified date rule enters the
site.

Nothing here introduces a figure the plan does not state. The only money in
this batch is money the visitor types in, plus the $300.00 price.

Skipped, with the reason. The first three groups were already recorded in
batch 5 and are repeated here because the slugs are still in the list:

  /t2-late-filing-penalty-calculator/
  /repeated-failure-to-file-penalty-calculator/
  /demand-to-file-penalty-calculator/
  /failure-to-comply-penalty-calculator/
  /gross-negligence-penalty-checker/
  /gst-hst-nil-filing-penalty-calculator/
  /t4-late-filing-penalty-calculator/
  /annual-return-late-fee-calculator/
      Each needs a statutory percentage, monthly rate or flat fee the plan
      never states. The plan grounds exactly two penalty figures: the
      non-resident $25.00 per day up to $2,500.00, and the qualification that
      a true nil return carries no percentage penalty because the penalty is a
      percentage of tax owing.

  /cra-arrears-interest-calculator/
  /instalment-interest-calculator/
  /shareholder-loan-prescribed-interest-calculator/
      Each needs the prescribed interest rate, which the plan does not state
      and which changes quarterly. The arrears guide published on October 27
      describes interest qualitatively for exactly this reason.

  /small-supplier-threshold-calculator/
  /small-business-deduction-limit-calculator/
  /taxable-capital-employed-in-canada-calculator/
  /schedule-33-taxable-capital-checker/
  /gst-hst-filing-frequency-calculator/
  /t1135-late-penalty-calculator/
  /t1135-foreign-property-checker/
  /t106-late-filing-penalty-calculator/
  /t1134-filing-requirement-checker/
  /regulation-105-withholding-calculator/
  /part-xiii-withholding-calculator/
  /branch-tax-calculator/
  /paid-up-capital-calculator/
  /capital-dividend-account-calculator/
  /shareholder-loan-income-inclusion-calculator/
  /subsection-15-2-exposure-checker/
      Each turns on a statutory dollar threshold, rate or timing rule the plan
      does not state.

  /ontario-annual-return-deadline-calculator/
  /ontario-annual-return-requirement-checker/
  /ontario-business-registry-filing-checker/
  /ontario-missed-annual-returns-calculator/
  /ontario-initial-return-deadline-calculator/
  /ontario-corporate-key-checker/
  /ontario-dissolution-consent-checker/
  /schedule-546-ontario-annual-return-checker/
      Still blocked on the Ontario annual return due date, outstanding since
      the second batch. The plan states the federal 60-day rule and the
      October 2021 registry move, but never the Ontario date. Eight Appendix A
      slugs now sit behind that one missing fact.

  /t2-filing-deadline-calculator/
  /t2-six-month-deadline-calculator/
  /wind-up-final-return-deadline-calculator/
  /catch-up-nil-filing-cost-calculator/
  /back-year-t2-cost-calculator/
  /multi-year-nil-filing-total-calculator/
  /ten-year-catch-up-cost-calculator/
  /years-behind-filing-cost-calculator/
  /fiscal-year-end-calculator/
  /first-tax-year-53-week-checker/
  /53-week-year-end-calculator/
  /gifi-requirement-checker/
  /required-schedules-checker/
  /still-required-to-file-checker/
  /t2-filing-requirement-checker/
  /outstanding-returns-count-checker/
  /dormant-corporation-obligation-checker/
  /zero-activity-corporation-checker/
  /t2-short-vs-full-return-checker/
  /t2-short-ccpc-condition-checker/
  /t2-short-exclusion-checker/
  /t2-short-nil-income-checker/
  /schedule-50-shareholder-information-checker/
  /gst-hst-nil-remittance-checker/
  /payroll-account-dormant-checker/
  /dissolution-final-t2-checker/
  /dissolution-outstanding-filings-checker/
      Each duplicates a tool already live. Twenty-seven of the hundred and
      thirty unbuilt slugs are synonyms of the thirty that exist, which is
      worth saying plainly: the family will not reach 150 distinct tools from
      this list without new topics.

  /nil-t2-price-with-hst-calculator/
      Needs the provincial tax rate, reserved for Sharad Gondaliya. The
      Ontario cost page publishes a 13 per cent figure, but a calculator under
      a province-neutral slug would need all of them.
"""
import io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_f2 import (render, meta, yn, a, DATE_JS, SITE, HUB, FORM, PRICE,
                      NOT_NIL, TOOL_DISCLAIMER)
from build_f2b import tool, num, date, out_box, PICK, T, G, COST
from build_f2c import DUE_JS, MONEY_JS, PARSE_JS, QUAL, PRELUDE
from build_f2e import ORDER5, LINK_TITLE5, ADD_YEAR, SPAN_JS

# A generic month step, month-end aware, on exactly the convention dueDate
# already uses: a year-end on the last day of its month lands on the last day
# of the target month, and any other day keeps its day number, clamped.
#
# dueDate is the proven version of this at n=6 and stays the function the
# deadline pages call. ADD_MONTHS exists because the balance-due date is two
# months out, or three, and nothing in the stack stepped by an arbitrary
# number of months before. test_f2f.js asserts the two agree at n=6 across
# every month-end and every ordinary day, so a future edit to one that does
# not match the other fails the suite rather than shipping two conventions.
ADD_MONTHS = r"""function addMonths(dt,n){
  var y=dt.getUTCFullYear(),m=dt.getUTCMonth(),d=dt.getUTCDate();
  var endOfMonth=(d===lastDay(y,m));
  var tm=m+n,ty=y+Math.floor(tm/12);tm=((tm%12)+12)%12;
  if(endOfMonth){return u(ty,tm+1,0);}
  return u(ty,tm,Math.min(d,lastDay(ty,tm)));
}
"""

assert 'var tm=m+6,ty=y+Math.floor(tm/12);tm=((tm%12)+12)%12;' in DUE_JS, (
    'dueDate no longer steps months the way addMonths copies. Re-read both '
    'before trusting the balance-due dates.')

BASE = PRELUDE + DATE_JS + DUE_JS + ADD_YEAR + ADD_MONTHS + PARSE_JS + SPAN_JS

# pick() reads a radio group and is NOT part of BASE, because the date-only
# tools have no radios. Every tool with a radio group builds on RBASE
# instead; a guard below fails the build if any script calls pick() without
# carrying its definition, which is a silent ReferenceError on the page.
RBASE = BASE + PICK

# --------------------------------------------------------------- 31. balance
T31_JS = RBASE + r"""
function balanceDates(ye,ccpc){
  if(ye===null){return null;}
  if(ye===undefined){return {err:'read'};}
  var months=(ccpc==='y')?3:2;
  var bal=nextBusiness(addMonths(ye,months));
  var fil=nextBusiness(dueDate(ye));
  return {months:months,bal:bal,fil:fil,
          gap:Math.round((fil.getTime()-bal.getTime())/86400000)};
}
var out=document.getElementById('out');
function show(){
  var r=balanceDates(parse('ye'),pick('ccpc'));
  if(r===null){out.innerHTML='<p>Enter the fiscal year-end and answer the '
    +'question above.</p>';return;}
  if(r.err){out.innerHTML='<p>That date could not be read.</p>';return;}
  var h='<h3>Balance due '+fmt(r.bal)+', return due '+fmt(r.fil)+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Obligation</th>'
   +'<th scope="col">Due</th><th scope="col">On a nil year</th></tr></thead>'
   +'<tbody>';
  h+='<tr><td>Paying a balance of tax</td><td>'+fmt(r.bal)+', being '
   +r.months+' months after the year-end</td><td>Nothing to pay</td></tr>';
  h+='<tr><td>Filing the T2</td><td>'+fmt(r.fil)
   +', being six months after the year-end</td><td>Still due</td></tr>';
  h+='</tbody></table>';
  h+='<p>The two dates are '+r.gap+' days apart. A corporation with no '
   +'activity has no balance and no instalments, which leaves the filing '
   +'date as the only one it has to meet.</p>';
  h+='<p>'+NOTNILJS+'</p>';
  h+='<p>Nil T2 filing is '+PRICE_JS+'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
var yeEl=document.getElementById('ye');
if(yeEl){yeEl.addEventListener('change',show);yeEl.addEventListener('input',show);}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="ccpc"]'),
  function(el){el.addEventListener('change',show);});
"""

# ---------------------------------------------------------------- 32. period
T32_JS = BASE + r"""
function periodLength(st,en){
  if(st===null||en===null){return null;}
  if(st===undefined||en===undefined){return {err:'read'};}
  if(en.getTime()<st.getTime()){return {err:'order'};}
  var days=spanDays(st,en);
  var weeks=Math.floor(days/7),rem=days%7;
  return {days:days,weeks:weeks,rem:rem,
          over:days>371,full:days>=365&&days<=366,
          due:nextBusiness(dueDate(en))};
}
var out=document.getElementById('out');
function show(){
  var r=periodLength(parse('st'),parse('en'));
  if(r===null){out.innerHTML='<p>Enter the first and last day of the fiscal '
    +'period.</p>';return;}
  if(r.err==='read'){out.innerHTML='<p>Those dates could not be read.</p>';
    return;}
  if(r.err==='order'){out.innerHTML='<p>The last day falls before the first '
    +'day. Check the two dates.</p>';return;}
  var kind=r.over?'longer than the 53-week limit'
          :(r.full?'a full tax year':'a short tax year');
  var h='<h3>'+r.days+' days, which is '+kind+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Measure</th>'
   +'<th scope="col">This period</th></tr></thead><tbody>';
  h+='<tr><td>Length in days, counting both ends</td><td>'+r.days+'</td></tr>';
  h+='<tr><td>Length in weeks</td><td>'+r.weeks+' weeks'
   +(r.rem?' and '+plural(r.rem,'day'):'')+'</td></tr>';
  h+='<tr><td>The 53-week limit, which is 371 days</td><td>'
   +(r.over?'Exceeded':'Not exceeded')+'</td></tr>';
  h+='<tr><td>T2 due six months after the last day</td><td>'+fmt(r.due)
   +'</td></tr>';
  h+='</tbody></table>';
  if(r.over){
    h+='<p>A first tax year may not exceed 53 weeks, so a period this long '
     +'is not available as a first year. Where this is a first year, the '
     +'year-end has to fall earlier, which produces a short first year and '
     +'then a full one.</p>';
  }else if(!r.full){
    h+='<p>A short tax year does not get a short deadline. The six-month '
     +'rule is measured from the day the period ends, so this period has '
     +'until '+fmt(r.due)+' however short it is.</p>';
  }else{
    h+='<p>A full tax year of this length is the ordinary case, and the '
     +'six-month rule applies to its last day.</p>';
  }
  h+='<p>Each tax year is its own return at '+PRICE_JS+'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
['st','en'].forEach(function(id){
  var el=document.getElementById(id);
  if(el){el.addEventListener('change',show);el.addEventListener('input',show);}
});
"""

# ---------------------------------------------------------------- 33. demand
T33_JS = BASE + r"""
function demandDeadline(ltr,days,now){
  if(ltr===null||days===null){return null;}
  if(ltr===undefined){return {err:'read'};}
  if(!(days>0)||days>365){return {err:'days'};}
  var raw=new Date(ltr.getTime()+days*86400000);
  var due=nextBusiness(raw);
  var shifted=due.getTime()!==raw.getTime();
  var left=Math.round((due.getTime()-now.getTime())/86400000);
  return {due:due,shifted:shifted,left:left,
          past:due.getTime()<now.getTime(),
          biz:left>0?businessBetween(now,due):0};
}
var out=document.getElementById('out');
function show(){
  var n=document.getElementById('dys').value;
  var r=demandDeadline(parse('ltr'),n===''?null:parseInt(n,10),today());
  if(r===null){out.innerHTML='<p>Enter the date on the letter and the number '
    +'of days it allows.</p>';return;}
  if(r.err==='read'){out.innerHTML='<p>That date could not be read.</p>';
    return;}
  if(r.err==='days'){out.innerHTML='<p>Enter the number of days the letter '
    +'allows, between 1 and 365.</p>';return;}
  var h='<h3>'+(r.past?'The date on the letter has passed: '+fmt(r.due)
                :'Respond by '+fmt(r.due))+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Measure</th>'
   +'<th scope="col">Value</th></tr></thead><tbody>';
  h+='<tr><td>Date the letter allows to</td><td>'+fmt(r.due)
   +(r.shifted?', moved to the next business day':'')+'</td></tr>';
  h+='<tr><td>Calendar days from today</td><td>'
   +(r.past?plural(-r.left,'day')+' ago':plural(r.left,'day'))+'</td></tr>';
  if(!r.past){
    h+='<tr><td>Business days from today</td><td>'+plural(r.biz,'business day')
     +'</td></tr>';
  }
  h+='</tbody></table>';
  if(r.past){
    h+='<div class="ei-danger"><p>Where a demand goes unanswered the Canada '
     +'Revenue Agency may assess the corporation on its own estimate of '
     +'income. That assessment creates a real balance, interest runs on it, '
     +'and it stands until a filed return displaces it.</p></div>';
  }
  h+='<p>'+QUALJS+'</p>';
  h+='<p>Filing the named return is what answers a demand. Each outstanding '
   +'year is its own return at '+PRICE_JS+'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
['ltr','dys'].forEach(function(id){
  var el=document.getElementById(id);
  if(el){el.addEventListener('change',show);el.addEventListener('input',show);}
});
"""

# -------------------------------------------------------------------- 34. T4
T34_JS = RBASE + r"""
function t4Due(yr,acct,emp){
  if(yr===null||acct===null){return null;}
  if(!(yr>=2000)||yr>2100){return {err:'year'};}
  if(acct==='n'){return {none:true};}
  if(emp===null){return null;}
  var raw=u(yr+1,1,lastDay(yr+1,1));
  return {due:nextBusiness(raw),shifted:nextBusiness(raw).getTime()!==raw.getTime(),
          nil:emp==='n',yr:yr};
}
var out=document.getElementById('out');
function show(){
  var v=document.getElementById('yr').value;
  var r=t4Due(v===''?null:parseInt(v,10),pick('acct'),pick('emp'));
  if(r===null){out.innerHTML='<p>Enter the calendar year and answer the '
    +'questions above.</p>';return;}
  if(r.err){out.innerHTML='<p>Enter a calendar year between 2000 and 2100.</p>';
    return;}
  if(r.none){
    out.innerHTML='<h3>No T4 return is expected</h3>'
     +'<p>With no payroll account there is no T4 information return and no '
     +'remittance obligation. Opening one later starts both.</p>'
     +'<p>'+DISC_JS+'</p>';
    return;}
  var h='<h3>'+(r.nil?'A nil T4 information return is still expected by '
                :'T4 slips and the summary are due by ')+fmt(r.due)+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Item</th>'
   +'<th scope="col">For '+r.yr+'</th></tr></thead><tbody>';
  h+='<tr><td>Payroll account</td><td>Open</td></tr>';
  h+='<tr><td>Anyone paid during the year</td><td>'+(r.nil?'No':'Yes')
   +'</td></tr>';
  h+='<tr><td>T4 information return</td><td>Due '+fmt(r.due)
   +(r.shifted?', moved to the next business day':'')+'</td></tr>';
  h+='<tr><td>Covered by the nil T2 fee</td><td>No</td></tr>';
  h+='</tbody></table>';
  if(r.nil){
    h+='<p>An open payroll account keeps generating obligations whether or '
     +'not anyone was paid. The information return is expected, and so are '
     +'the nil remittances through the year. Form RC145 closes the account, '
     +'and closing it is what stops the dates recurring.</p>';
  }else{
    h+='<p>Paying anyone during the year means this is not a payroll nil '
     +'matter. The T4 return reports what was paid, separately from the '
     +'T2.</p>';
  }
  h+='<p>The T4 return and the account closure are not covered by the nil T2 '
   +'fee of '+PRICE_JS+'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
var y=document.getElementById('yr');
if(y){y.addEventListener('change',show);y.addEventListener('input',show);}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="acct"],input[name="emp"]'),
  function(el){el.addEventListener('change',show);});
"""

# -------------------------------------------------------------- 35. retained
T35_JS = BASE + MONEY_JS + r"""
function cents(id){
  var v=document.getElementById(id).value;
  if(v===''){return null;}
  var n=Number(v);
  if(!isFinite(n)){return undefined;}
  return Math.round(n*100);
}
function rollforward(ro,ni,dv){
  if(ro===null||ni===null||dv===null){return null;}
  if(ro===undefined||ni===undefined||dv===undefined){return {err:'read'};}
  var close=ro+ni-dv;
  return {ro:ro,ni:ni,dv:dv,close:close,
          deficit:close<0,quiet:ni===0&&dv===0};
}
var out=document.getElementById('out');
function show(){
  var r=rollforward(cents('ro'),cents('ni'),cents('dv'));
  if(r===null){out.innerHTML='<p>Enter the three figures above. Use 0 where '
    +'there was nothing, and a minus sign for a loss or a deficit.</p>';
    return;}
  if(r.err){out.innerHTML='<p>Those figures could not be read.</p>';return;}
  var h='<h3>Closing '+(r.deficit?'deficit':'retained earnings')+' '
   +money(Math.abs(r.close))+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Line</th>'
   +'<th scope="col">Amount</th></tr></thead><tbody>';
  h+='<tr><td>Opening retained earnings</td><td>'+money(r.ro)+'</td></tr>';
  h+='<tr><td>Net income for the year</td><td>'+money(r.ni)+'</td></tr>';
  h+='<tr><td>Dividends declared</td><td>'+money(r.dv)+'</td></tr>';
  h+='<tr><td>Closing retained earnings</td><td>'+money(r.close)+'</td></tr>';
  h+='</tbody></table>';
  h+='<p>The closing figure is what the next return opens from. A balance '
   +'sheet that does not carry it forward is wrong in a way that persists, '
   +'because each year begins where the last one ended.</p>';
  if(r.quiet){
    h+='<p>With no net income and no dividends, the closing figure equals the '
     +'opening one. That is the ordinary shape of a quiet year: the income '
     +'statement reports zeroes while the balance sheet still carries real '
     +'numbers.</p>';
  }else{
    h+='<div class="ei-warn"><p>Net income or a dividend in the year means '
     +'this is not a nil year. '+NOTNILJS+'</p></div>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
['ro','ni','dv'].forEach(function(id){
  var el=document.getElementById(id);
  if(el){el.addEventListener('change',show);el.addEventListener('input',show);}
});
"""

# ----------------------------------------------------------------- 36. equals
T36_JS = BASE + MONEY_JS + r"""
function cents(id){
  var v=document.getElementById(id).value;
  if(v===''){return null;}
  var n=Number(v);
  if(!isFinite(n)){return undefined;}
  return Math.round(n*100);
}
function balances(as,li,eq){
  if(as===null||li===null||eq===null){return null;}
  if(as===undefined||li===undefined||eq===undefined){return {err:'read'};}
  var side=li+eq,diff=as-side;
  return {as:as,li:li,eq:eq,side:side,diff:diff,ok:diff===0};
}
var out=document.getElementById('out');
function show(){
  var r=balances(cents('as'),cents('li'),cents('eq'));
  if(r===null){out.innerHTML='<p>Enter the three totals above. Use 0 where '
    +'there is nothing on that side.</p>';return;}
  if(r.err){out.innerHTML='<p>Those figures could not be read.</p>';return;}
  var h='<h3>'+(r.ok?'The balance sheet balances'
                :'Out by '+money(Math.abs(r.diff)))+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Side</th>'
   +'<th scope="col">Total</th></tr></thead><tbody>';
  h+='<tr><td>Total assets</td><td>'+money(r.as)+'</td></tr>';
  h+='<tr><td>Total liabilities</td><td>'+money(r.li)+'</td></tr>';
  h+='<tr><td>Total equity</td><td>'+money(r.eq)+'</td></tr>';
  h+='<tr><td>Liabilities plus equity</td><td>'+money(r.side)+'</td></tr>';
  h+='<tr><td>Difference</td><td>'+money(r.diff)+'</td></tr>';
  h+='</tbody></table>';
  if(r.ok){
    h+='<p>Assets equal liabilities plus equity, which is what Schedule 100 '
     +'requires. A nil year still files this schedule, carrying whatever the '
     +'corporation holds.</p>';
  }else{
    h+='<div class="ei-warn"><p>Assets do not equal liabilities plus equity, '
     +'so Schedule 100 will not validate and the transmission is rejected '
     +'rather than filed. The usual causes are share capital left off the '
     +'equity side, a shareholder loan on the wrong side, and retained '
     +'earnings not carried forward from the previous year.</p></div>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
['as','li','eq'].forEach(function(id){
  var el=document.getElementById(id);
  if(el){el.addEventListener('change',show);el.addEventListener('input',show);}
});
"""

# ------------------------------------------------------------------ 37. zeroes
T37_JS = RBASE + r"""
function nilSheet(sc,sl,re,bk){
  if(sc===null||sl===null||re===null||bk===null){return null;}
  var rows=[];
  if(sc==='y'){rows.push(['Share capital issued on incorporation',
    'Equity, on Schedule 100']);}
  if(sl==='y'){rows.push(['A balance owed to or by a shareholder',
    'A liability or an asset, on Schedule 100']);}
  if(re==='y'){rows.push(['Retained earnings or a deficit brought forward',
    'Equity, on Schedule 100']);}
  if(bk==='y'){rows.push(['A bank balance','An asset, on Schedule 100']);}
  return {rows:rows,empty:rows.length===0,interest:bk==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=nilSheet(pick('sc'),pick('sl'),pick('re'),pick('bk'));
  if(r===null){out.innerHTML='<p>Answer all four questions above.</p>';return;}
  var h='<h3>'+(r.empty?'A genuinely empty balance sheet'
    :plural(r.rows.length,'balance')+' must appear on Schedule 100')+'</h3>';
  if(r.empty){
    h+='<p>Nothing on this list is present, so the balance sheet really is '
     +'all zeroes. That is uncommon but it does happen, most often where a '
     +'corporation was registered and never funded.</p>';
    h+='<p>The income statement reports zeroes on a nil year either way. The '
     +'difference this makes is only to Schedule 100.</p>';
  }else{
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Present</th>'
     +'<th scope="col">Where it is reported</th></tr></thead><tbody>';
    for(var i=0;i<r.rows.length;i++){
      h+='<tr><td>'+r.rows[i][0]+'</td><td>'+r.rows[i][1]+'</td></tr>';
    }
    h+='</tbody></table>';
    h+='<div class="ei-warn"><p>A balance sheet filed as entirely zero when '
     +'any of these is present is wrong, and it is wrong in a way that '
     +'persists: the next return opens from the closing balances this one '
     +'reports.</p></div>';
  }
  if(r.interest){
    h+='<p>A bank balance is also the commonest way a quiet year stops being '
     +'nil, because interest credited to the account is investment income '
     +'whatever the amount. '+NOTNILJS+'</p>';
  }
  h+='<p>A nil year is still '+PRICE_JS+'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="sc"],input[name="sl"],'
    +'input[name="re"],input[name="bk"]'),
  function(el){el.addEventListener('change',show);});
"""

# ------------------------------------------------------------- 38. schedule 8
T38_JS = RBASE + r"""
function sched8(dp,uc,ds){
  if(dp===null||uc===null||ds===null){return null;}
  var need=(dp==='y'||uc==='y');
  return {need:need,dp:dp==='y',uc:uc==='y',ds:ds==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=sched8(pick('dp'),pick('uc'),pick('ds'));
  if(r===null){out.innerHTML='<p>Answer the three questions above.</p>';return;}
  var h='<h3>Schedule 8 '+(r.need?'is required':'is not required')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Answer</th><th scope="col">Effect</th></tr></thead>'
   +'<tbody>';
  h+='<tr><td>Holds depreciable property</td><td>'+(r.dp?'Yes':'No')+'</td>'
   +'<td>'+(r.dp?'Schedule 8 is required':'Nothing on its own')+'</td></tr>';
  h+='<tr><td>Carries an undepreciated balance from an earlier year</td><td>'
   +(r.uc?'Yes':'No')+'</td><td>'
   +(r.uc?'Schedule 8 is required, to carry the balance forward'
         :'Nothing on its own')+'</td></tr>';
  h+='<tr><td>Disposed of any of it during the year</td><td>'
   +(r.ds?'Yes':'No')+'</td><td>'
   +(r.ds?'The year is not nil':'No effect on nil status')+'</td></tr>';
  h+='</tbody></table>';
  if(r.need){
    h+='<p>Schedule 8 records capital cost allowance and the undepreciated '
     +'balance carried forward. It is filed on a nil year where the '
     +'corporation holds depreciable property, and the balance continues '
     +'whether or not any allowance is claimed. Claiming nothing in a quiet '
     +'year is a choice, and the balance is simply carried.</p>';
  }else{
    h+='<p>With no depreciable property and no balance brought forward there '
     +'is nothing for Schedule 8 to report. Schedules 100, 125 and 141 are '
     +'still filed, and Schedule 50 still reports every shareholder at 10% '
     +'or more.</p>';
  }
  if(r.ds){
    h+='<div class="ei-danger"><p>A disposition is activity, so the year it '
     +'happened in is not a nil year. '+NOTNILJS+'</p></div>';
  }
  h+='<p>Where the year is nil, Schedule 8 and the loss continuity are '
   +'recorded within the fee of '+PRICE_JS+'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="dp"],input[name="uc"],'
    +'input[name="ds"]'),
  function(el){el.addEventListener('change',show);});
"""

# ----------------------------------------------------------------- 39. struck
T39_JS = RBASE + r"""
function strikeRisk(ar,ad,dr){
  if(ar===null||ad===null||dr===null){return null;}
  var n=0;
  if(ar==='n'){n++;}
  if(ad==='n'){n++;}
  if(dr==='n'){n++;}
  return {n:n,ar:ar==='n',ad:ad==='n',dr:dr==='n',
          level:(ar==='n'?(ad==='n'?'high':'raised'):(n?'low':'none'))};
}
var out=document.getElementById('out');
function show(){
  var r=strikeRisk(pick('ar'),pick('ad'),pick('dr'));
  if(r===null){out.innerHTML='<p>Answer the three questions above.</p>';return;}
  var head={none:'Nothing on this list is outstanding',
            low:'One registry record is out of date',
            raised:'The annual return is outstanding',
            high:'The annual return is outstanding and the address is stale'};
  var h='<h3>'+head[r.level]+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Registry item</th>'
   +'<th scope="col">State</th><th scope="col">What it affects</th></tr>'
   +'</thead><tbody>';
  h+='<tr><td>Annual return for the current period</td><td>'
   +(r.ar?'Not filed':'Filed')+'</td>'
   +'<td>This is the filing whose absence gets a corporation struck</td></tr>';
  h+='<tr><td>Registered office address</td><td>'
   +(r.ad?'Out of date':'Current')+'</td>'
   +'<td>Where the registry sends the warning notice</td></tr>';
  h+='<tr><td>Director record</td><td>'+(r.dr?'Out of date':'Current')
   +'</td><td>Who the registry and the Agency write to</td></tr>';
  h+='</tbody></table>';
  if(r.ar){
    h+='<p>A missed annual return does not produce a charge. It produces a '
     +'striking: the registry dissolves the corporation involuntarily. A '
     +'corporation can be perfectly current on tax and still be dissolved '
     +'this way.</p>';
  }
  if(r.ar&&r.ad){
    h+='<div class="ei-danger"><p>These two together are the case that ends '
     +'badly. The registry sends its warning to the registered office, and a '
     +'stale address means nobody reads it. A dormant corporation is the most '
     +'likely to be in exactly this position, because nobody is checking the '
     +'post at an office nobody uses.</p></div>';
  }
  h+='<p>Being struck settles nothing on the tax side. The corporation&#8217;s '
   +'tax years stay open and unfiled, and registries provide for revival so '
   +'the outstanding filings can be made and a proper wind-up completed.</p>';
  h+='<p>The annual return is a registry filing and is not covered by the '
   +'nil T2 fee of '+PRICE_JS+'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="ar"],input[name="ad"],'
    +'input[name="dr"]'),
  function(el){el.addEventListener('change',show);});
"""

# --------------------------------------------------------------- 40. directors
T40_JS = RBASE + r"""
function exposure(pd,gh,ci){
  if(pd===null||gh===null||ci===null){return null;}
  var reach=[];
  if(pd==='y'){reach.push(['Payroll source deductions',
    'Withheld from pay and owed to the Agency']);}
  if(gh==='y'){reach.push(['Net GST/HST',
    'Collected from customers and owed to the Agency']);}
  return {reach:reach,pd:pd==='y',gh:gh==='y',ci:ci==='y',
          any:reach.length>0};
}
var out=document.getElementById('out');
function show(){
  var r=exposure(pick('pd'),pick('gh'),pick('ci'));
  if(r===null){out.innerHTML='<p>Answer the three questions above.</p>';return;}
  var h='<h3>'+(r.any?plural(r.reach.length,'amount')
                  +' of this kind can be assessed against directors'
                 :'Nothing on this list reaches the directors personally')
   +'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Amount</th>'
   +'<th scope="col">Present</th><th scope="col">Reaches directors</th></tr>'
   +'</thead><tbody>';
  h+='<tr><td>Payroll source deductions unremitted</td><td>'
   +(r.pd?'Yes':'No')+'</td><td>Yes</td></tr>';
  h+='<tr><td>Net GST/HST collected and unremitted</td><td>'
   +(r.gh?'Yes':'No')+'</td><td>Yes</td></tr>';
  h+='<tr><td>Corporate income tax owing</td><td>'+(r.ci?'Yes':'No')
   +'</td><td>No, not on its own</td></tr>';
  h+='</tbody></table>';
  h+='<p>The pattern is that amounts the corporation was required to withhold '
   +'or collect and remit can be assessed against its directors personally, '
   +'because the money was never the corporation&#8217;s to keep. Corporate '
   +'income tax on its own is not among them.</p>';
  if(r.any){
    h+='<div class="ei-warn"><p>This is why an unused payroll or GST/HST '
     +'account is worth closing rather than ignoring. While an account is '
     +'open it keeps generating obligations, and Form RC145 is what closes '
     +'it.</p></div>';
  }
  if(r.ci&&!r.any){
    h+='<p>Corporate income tax owing is collectible from the corporation, '
     +'and the Agency has statutory collection powers it can use without '
     +'going to court. What it is not, on its own, is a personal liability of '
     +'the directors.</p>';
  }
  h+='<p>'+QUALJS+'</p>';
  h+='<p>Filing an outstanding nil year is '+PRICE_JS+'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="pd"],input[name="gh"],'
    +'input[name="ci"]'),
  function(el){el.addEventListener('change',show);});
"""

TOOLS6 = [
 dict(slug='corporate-balance-due-date-calculator',
  title='Corporate Balance Due Date Calculator | Two or Three Months',
  h1_pre='Corporate Balance ', h1_span='Due Date Calculator',
  h1='Corporate Balance Due Date Calculator',
  eyebrow='Date Tool', keyword='corporate balance due date calculator',
  meta=('Paying a balance of tax is due before the return is. Enter the '
        'fiscal year-end for both dates, on the same holiday calendar.'),
  tags=['Two months, or three for a CCPC', 'Filing stays at six months',
        'Moved off weekends and holidays', 'Nothing to pay on a nil year'],
  form=tool('Your fiscal year-end',
            [date('ye', 'The last day of the tax year'),
             yn('ccpc', 'Is it a Canadian-controlled private corporation '
                        'meeting the conditions for the longer period?')],
            'Enter the year-end and answer the question for both dates.'),
  js=None,
  sections=[
   ('two-dates', 'Filing and Paying Are Two Different Deadlines',
    '<p>Almost everything written about the T2 gives one date: six months '
    'after the fiscal year-end. That is the date the return is due. It is not '
    'the date a balance of tax is due, and the balance date comes '
    'first.</p>\n'
    '<p>A balance is due two months after the year-end, or three months for a '
    'Canadian-controlled private corporation that meets the conditions. A '
    'corporation that files on the six-month date and pays at the same time '
    'has filed on time and paid late.</p>'),
   ('nil-year', 'On a Nil Year Only One of Them Applies',
    '<p>A corporation with no activity has no balance to pay, so the earlier '
    'date passes with nothing owed on it. It also has no instalment '
    'obligation, because that arises from the previous year&#8217;s tax and a '
    'nil year sets that at $0.00.</p>\n'
    '<p>That leaves the filing deadline as the only date a dormant '
    'corporation has to meet, which is the whole of its tax calendar. The '
    + a(T + 'nil-t2-deadline-calculator/', 'nil T2 deadline calculator')
    + ' gives that date on its own.</p>\n'
    '<p>' + NOT_NIL + '</p>'),
   ('three-months', 'Where the Three-Month Period Comes From',
    '<p>The longer period is not available to every small corporation. It '
    'turns on the corporation being a Canadian-controlled private '
    'corporation and on conditions about its income and its taxable capital '
    'being met, in the year and in the one before it.</p>\n'
    '<p>This calculator takes the answer as given rather than deciding it, '
    'because the conditions rest on figures a dormant corporation does not '
    'have and a trading one should not read off a web page. Where the answer '
    'is not certain, the two-month date is the safe one to work to.</p>'),
   ('weekend', 'Both Dates Move Off a Weekend or a Holiday',
    '<p>Where either calculated date falls on a Saturday, a Sunday or a '
    'public holiday, it moves to the next business day. The calculation here '
    'runs on the same holiday calendar as the deadline pages, so the two '
    'never disagree.</p>\n'
    '<p>The shift can be more than one day. A date landing on a Sunday '
    'followed by a Monday holiday moves to the Tuesday, which the '
    + a(T + 'due-date-weekend-holiday-shift-calculator/',
        'due date weekend and holiday shift calculator')
    + ' shows on its own.</p>'),
  ],
  faq=[
   ('When is a corporate balance of tax due?',
    'Two months after the fiscal year-end, or three months for a '
    'Canadian-controlled private corporation that meets the conditions. '
    'Filing the return is separately due six months after the year-end.'),
   ('Does a nil year have a balance due date?',
    'The date exists but nothing is owed on it. A corporation with no '
    'activity has no balance of tax and no instalment obligation, which '
    'leaves the six-month filing deadline as the only date it has to meet.'),
   ('Can I pay when I file?',
    'Only where the two dates coincide, which they do not. A corporation that '
    'pays a balance on the six-month filing date has paid four months late, '
    'or three.'),
   ('Which period applies to my corporation?',
    'The three-month period turns on Canadian-controlled private corporation '
    'status and on conditions about income and taxable capital in this year '
    'and the one before. Where that is not certain, work to the two-month '
    'date.'),
   ('What if the date falls on a holiday?',
    'It moves to the next business day, on the same holiday calendar the '
    'filing deadline uses. The shift can be more than one day where a holiday '
    'sits next to a weekend.'),
  ]),

 dict(slug='fiscal-period-length-calculator',
  title='Fiscal Period Length Calculator | Days, Weeks and the 53-Week Limit',
  h1_pre='Fiscal Period ', h1_span='Length Calculator',
  h1='Fiscal Period Length Calculator',
  eyebrow='Date Tool', keyword='fiscal period length calculator',
  meta=('Enter the first and last day of a fiscal period for its length in '
        'days and weeks, whether it clears the 53-week limit, and its T2 '
        'date.'),
  tags=['Counts both ends', 'Tests the 371-day limit',
        'Short years get the same six months', 'Gives the filing date'],
  form=tool('The fiscal period',
            [date('st', 'First day of the period'),
             date('en', 'Last day of the period')],
            'Enter both days and the length appears here.'),
  js=None,
  sections=[
   ('why-length', 'Why the Length of a Period Is Worth Measuring',
    '<p>Three rules turn on how long a fiscal period is, and all three are '
    'easy to get wrong by a few days. A first tax year may not exceed 53 '
    'weeks. A period shorter than twelve months is a short tax year. A period '
    'longer than twelve months is not a tax year at all.</p>\n'
    '<p>Counting it by eye from two dates in different years is where the '
    'mistakes come from. This counts the days, including both the first and '
    'the last, and converts them to weeks.</p>'),
   ('fifty-three', 'The 53-Week Limit Is 371 Days',
    '<p>A first tax year runs from the date of incorporation to the chosen '
    'year-end and may not exceed 53 weeks, which is 371 days counting the day '
    'of incorporation. A year-end chosen beyond that is not available.</p>\n'
    '<p>Where a period here comes out longer, and it is a first year, the '
    'year-end has to fall earlier. That produces a short first year followed '
    'by a full one, and two returns due within a few months of each other. '
    'The ' + a(T + '53-week-first-tax-year-checker/',
                '53-week first tax year checker')
    + ' tests that question on its own.</p>'),
   ('short-years', 'A Short Period Still Gets the Full Six Months',
    '<p>The six-month rule is measured from the day the period ends, whatever '
    'its length. A three-month stub period still has six months after it to '
    'file, which is longer than the period itself.</p>\n'
    '<p>Short periods arise on a first year, on an approved change of '
    'year-end, on an amalgamation and on a final year ending at dissolution. '
    'Each is a separate return at ' + PRICE + '. The '
    + a(T + 'short-tax-year-deadline-calculator/',
        'short tax year deadline calculator')
    + ' goes further into the filing date.</p>'),
   ('changing', 'Changing a Year-End Needs Written Approval',
    '<p>A fiscal year-end is fixed by the first return filed, and changing it '
    'needs the written approval of the Canada Revenue Agency. A return filed '
    'with a different date on it does not change the year-end on record, it '
    'is rejected against it.</p>\n'
    '<p>An approved change produces a short period, and this calculator will '
    'measure it. What it cannot do is tell you the change was approved.</p>'),
  ],
  faq=[
   ('How long can a first tax year be?',
    'Up to 53 weeks, which is 371 days counting the day of incorporation. A '
    'year-end chosen beyond that is not available, so the first year has to '
    'end earlier.'),
   ('Does a short tax year have an earlier deadline?',
    'No. The six-month rule is measured from the day the short period ends, '
    'so a three-month period still has six months after it to file.'),
   ('Is a period longer than twelve months a tax year?',
    'No. A tax year cannot exceed 53 weeks, so a longer period means the '
    'year-end being used is not the one on record, or the dates are wrong.'),
   ('Does this count the first and last day?',
    'Yes, both. A period from January 1 to December 31 counts as 365 days in '
    'an ordinary year, not 364.'),
   ('How do I change my fiscal year-end?',
    'With the written approval of the Canada Revenue Agency. Filing a return '
    'carrying a different date does not change the year-end on record.'),
  ]),

 dict(slug='cra-demand-to-file-deadline-calculator',
  title='CRA Demand to File Deadline Calculator | Days Left to Respond',
  h1_pre='CRA Demand to File ', h1_span='Deadline Calculator',
  h1='CRA Demand to File Deadline Calculator',
  eyebrow='Demand to File', keyword='cra demand to file deadline calculator',
  meta=('A demand to file names a date. Enter the letter date and the days it '
        'allows for the deadline, the days left and the business days left.'),
  tags=['Counts calendar and business days', 'Moves off weekends and holidays',
        'Says when the date has passed', 'Filing is what answers a demand'],
  form=tool('The letter',
            [date('ltr', 'Date on the demand letter'),
             num('dys', 'Days the letter allows', 'As stated on the letter',
                 1, 365, '30')],
            'Enter the letter date and the days it allows.'),
  js=None,
  sections=[
   ('what-changes', 'What a Demand to File Changes',
    '<p>A demand to file is a formal written requirement to file a named '
    'return by a named date. It converts an overdue return into a legal '
    'obligation with its own deadline, and that date is the one this '
    'calculator works to.</p>\n'
    '<p>The number of days a demand allows is stated on the letter rather '
    'than fixed in advance, which is why it is typed in here rather than '
    'assumed. Reading it off the letter is the one step that cannot be '
    'skipped.</p>'),
   ('unanswered', 'What Happens If the Date Passes',
    '<p>Where a demand goes unanswered the Canada Revenue Agency may assess '
    'the corporation on its own estimate of income. That assessment creates a '
    'real balance, interest runs on it, and it stands until a filed return '
    'displaces it.</p>\n'
    '<p>This is how a dormant corporation that genuinely owed nothing ends up '
    'with a collectible debt. The balance was not produced by activity. It '
    'was produced by the missing return, which is also what removes it.</p>\n'
    '<div class="ei-danger"><p>' + QUAL + '</p></div>'),
   ('answering', 'Filing Is What Answers a Demand',
    '<p>Nothing else closes it. A demand names a return, and the return being '
    'filed is the response. Where several years are outstanding they are '
    'prepared oldest first, so the closing balances of one open the next, and '
    'they can be transmitted together.</p>\n'
    '<p>Each year is its own return at ' + PRICE + '. The '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' lists which years are outstanding, and the '
    + a(T + 'unfiled-years-cost-calculator/', 'unfiled years cost calculator')
    + ' totals them.</p>'),
   ('business-days', 'Why Business Days Are Counted Separately',
    '<p>The calendar count is what the letter runs on. The business-day count '
    'is what the work runs on, and on a short deadline the two differ enough '
    'to matter: ten calendar days over a long weekend is six business '
    'days.</p>\n'
    '<p>Where the named date itself falls on a Saturday, a Sunday or a public '
    'holiday, it moves to the next business day, on the same holiday calendar '
    'the filing deadlines use.</p>'),
  ],
  faq=[
   ('How long does a demand to file give me?',
    'The letter states the date or the number of days. It is not a fixed '
    'period, which is why it has to be read off the letter rather than '
    'assumed.'),
   ('What happens if I ignore a demand to file?',
    'The Canada Revenue Agency may assess the corporation on its own estimate '
    'of income. That arbitrary assessment is collectible and stands until the '
    'actual return displaces it.'),
   ('Does a nil return answer a demand?',
    'Yes. The demand names a return, and filing that return answers it. A '
    'year with no activity is filed showing $0.00 and the demand is closed.'),
   ('Can I ask for more time?',
    'That is a matter for the Agency and the particular letter. What does not '
    'help is letting the date pass without filing, because that is what an '
    'arbitrary assessment follows from.'),
   ('What if the named date is a weekend?',
    'It moves to the next business day, on the same holiday calendar the T2 '
    'filing deadline uses.'),
  ]),

 dict(slug='t4-nil-filing-requirement-checker',
  title='T4 Nil Filing Requirement Checker | Open Payroll Account',
  h1_pre='T4 Nil Filing ', h1_span='Requirement Checker',
  h1='T4 Nil Filing Requirement Checker',
  eyebrow='Payroll', keyword='t4 nil filing requirement checker',
  meta=('An open payroll account expects a T4 information return even where '
        'nobody was paid. Three answers give the date and what is owed.'),
  tags=['Due the end of February', 'Expected while the account is open',
        'Form RC145 closes it', 'Not covered by the nil T2 fee'],
  form=tool('The payroll account',
            [num('yr', 'Calendar year', 'The year being reported',
                 2000, 2100, '2026'),
             yn('acct', 'Does the corporation have an open payroll account?'),
             yn('emp', 'Was anyone paid during that calendar year?')],
            'Enter the year and answer both questions.'),
  js=None,
  sections=[
   ('calendar', 'The T4 Runs on the Calendar Year, Not Your Year-End',
    '<p>Almost every other date on this site is measured from the fiscal '
    'year-end. The T4 information return is not. It reports a calendar year '
    'and is due at the end of the following February, whatever year-end the '
    'corporation uses.</p>\n'
    '<p>A corporation with a June 30 year-end therefore has a T2 date in '
    'December and a T4 date at the end of February, four months apart and '
    'neither derived from the other.</p>'),
   ('while-open', 'An Open Account Expects a Return Either Way',
    '<p>The obligation follows the account, not the activity. While a payroll '
    'account is open, the Agency expects the annual information return and '
    'expects the remittances through the year, including nil ones.</p>\n'
    '<p>That is the trap for a dormant corporation: it stopped paying anyone '
    'years ago, and the account is still open and still generating dates. The '
    + a(T + 'payroll-nil-remittance-checker/', 'payroll nil remittance checker')
    + ' covers the remittances; this page covers the annual return.</p>'),
   ('closing', 'Form RC145 Is What Stops It',
    '<p>Closing the payroll account with Form RC145 is the only thing that '
    'ends the obligation. Until it is closed the dates recur every year, and '
    'nothing about the corporation being dormant pauses them.</p>\n'
    '<p>Closing the account is not covered by the nil T2 fee, and neither is '
    'the T4 return itself. The fee of ' + PRICE + ' covers one nil T2 return '
    'for one corporation for one tax year, and the '
    + a(COST, 'nil T2 filing cost') + ' page sets out what sits outside '
    'it.</p>'),
   ('directors', 'Why This One Reaches the Directors',
    '<p>Payroll source deductions are money withheld from someone&#8217;s pay '
    'and owed to the Agency. Amounts of that kind can be assessed against '
    'directors personally, which corporate income tax on its own cannot.</p>\n'
    '<p>That is the practical reason an unused payroll account is worth '
    'closing rather than ignoring. The '
    + a(T + 'director-liability-exposure-checker/',
        'director liability exposure checker')
    + ' sets out which amounts reach a director and which do not.</p>'),
  ],
  faq=[
   ('When is the T4 information return due?',
    'The end of February following the calendar year it reports. It is '
    'measured from the calendar year, not from the corporation&#8217;s fiscal '
    'year-end.'),
   ('Do I file a T4 return if nobody was paid?',
    'While the payroll account is open the return is expected, and so are the '
    'nil remittances through the year. Closing the account with Form RC145 is '
    'what ends both.'),
   ('Is the T4 return covered by the nil T2 fee?',
    'No. The fee covers one nil T2 return for one corporation for one tax '
    'year. The T4 return, the nil remittances and the account closure all sit '
    'outside it.'),
   ('How do I close a payroll account?',
    'With Form RC145. Until it is closed the account keeps generating '
    'obligations whether or not the corporation is doing anything.'),
   ('Does an open payroll account affect my nil T2?',
    'Not the T2 itself, which is still nil where there was no activity. What '
    'it affects is everything alongside the T2, and the directors&#8217; '
    'personal exposure to unremitted amounts.'),
  ]),

 dict(slug='retained-earnings-rollforward-calculator',
  title='Retained Earnings Rollforward Calculator | Opening to Closing',
  h1_pre='Retained Earnings ', h1_span='Rollforward Calculator',
  h1='Retained Earnings Rollforward Calculator',
  eyebrow='Schedule 100', keyword='retained earnings rollforward calculator',
  meta=('Opening, plus net income, less dividends, gives closing. The figure '
        'the next return has to open from, and what it says about nil '
        'status.'),
  tags=['Three figures in, one out', 'The next year opens from it',
        'Handles a deficit', 'Shows what ends a nil year'],
  form=tool('The three figures',
            [num('ro', 'Opening retained earnings',
                 'From the closing figure on last year&#8217;s return',
                 -999999999, 999999999, '0'),
             num('ni', 'Net income for the year',
                 'A loss is entered with a minus sign',
                 -999999999, 999999999, '0'),
             num('dv', 'Dividends declared during the year', 'Enter 0 if none',
                 -999999999, 999999999, '0')],
            'Enter all three figures. Use 0 where there was nothing.'),
  js=None,
  sections=[
   ('one-line', 'The Whole Calculation Is One Line',
    '<p>Opening retained earnings, plus net income for the year, less '
    'dividends declared, gives closing retained earnings. There is nothing '
    'else in it, and the arithmetic can be checked by hand in a '
    'second.</p>\n'
    '<p>What makes it worth a page is not the arithmetic. It is that the '
    'closing figure is the number the next return has to open from, and a '
    'return that does not carry it forward is rejected rather than '
    'filed.</p>'),
   ('nil-years', 'On a Quiet Year the Figure Does Not Move',
    '<p>A year with no net income and no dividends closes exactly where it '
    'opened. That is the ordinary shape of a nil year: the income statement '
    'reports zeroes while the balance sheet still carries real '
    'numbers.</p>\n'
    '<p>Retained earnings brought forward are one of three balances that '
    'commonly sit on a nil return&#8217;s balance sheet, alongside share '
    'capital issued on incorporation and a shareholder loan. The '
    + a(T + 'nil-gifi-balance-sheet-checker/', 'nil GIFI balance sheet checker')
    + ' tests which of them apply.</p>'),
   ('not-nil', 'Net Income or a Dividend Ends the Nil Year',
    '<p>Either figure being something other than zero means the year was not '
    'nil. A dividend declared is activity whether or not it was paid in cash, '
    'and net income is activity by definition.</p>\n'
    '<p>' + NOT_NIL + '</p>\n'
    '<p>The ' + a(T + 'nil-return-vs-full-return-checker/',
                  'nil return versus full return checker')
    + ' works through the whole test rather than these two lines.</p>'),
   ('deficit', 'A Deficit Is the Same Calculation',
    '<p>Where the closing figure is negative the corporation has a deficit '
    'rather than retained earnings. It sits in the same place on Schedule 100 '
    'and carries forward the same way.</p>\n'
    '<p>A corporation that spent money before it earned any, which is most '
    'corporations in their first year or two, will show a deficit. It is '
    'unremarkable and it does not change what is filed.</p>'),
  ],
  faq=[
   ('How is closing retained earnings calculated?',
    'Opening retained earnings, plus net income for the year, less dividends '
    'declared. The closing figure is what the next return opens from.'),
   ('Does retained earnings change on a nil year?',
    'No. With no net income and no dividends the closing figure equals the '
    'opening one, and the balance simply carries forward.'),
   ('Where does this figure go on the return?',
    'On Schedule 100, the balance sheet, reported through the coded GIFI '
    'format. A nil year files it carrying the balances it holds.'),
   ('What if the figure is negative?',
    'That is a deficit rather than retained earnings. It sits in the same '
    'place and carries forward the same way, and it is common in a '
    'corporation&#8217;s first years.'),
   ('Does a dividend end a nil year even if unpaid?',
    'A dividend declared is activity, so that year is not a nil year. Those '
    'returns are handled by Gondaliya CPA Professional Corporation at '
    'gondaliyacpa.ca at $350.00 plus HST per year.'),
  ]),

 dict(slug='balance-sheet-balancing-checker',
  title='Balance Sheet Balancing Checker | Schedule 100 Validation',
  h1_pre='Balance Sheet ', h1_span='Balancing Checker',
  h1='Balance Sheet Balancing Checker',
  eyebrow='Schedule 100', keyword='balance sheet balancing checker',
  meta=('Assets must equal liabilities plus equity or Schedule 100 will not '
        'validate. Enter the three totals to see the difference.'),
  tags=['Three totals in', 'Names the difference',
        'Lists the usual causes', 'A rejection, not a late filing'],
  form=tool('The three totals',
            [num('as', 'Total assets', 'Everything the corporation owns',
                 -999999999, 999999999, '0'),
             num('li', 'Total liabilities', 'Everything it owes',
                 -999999999, 999999999, '0'),
             num('eq', 'Total equity',
                 'Share capital plus retained earnings or deficit',
                 -999999999, 999999999, '0')],
            'Enter all three totals. Use 0 where there is nothing.'),
  js=None,
  sections=[
   ('why-reject', 'An Unbalanced Sheet Is a Rejection, Not a Late Filing',
    '<p>Schedule 100 will not validate where assets do not equal liabilities '
    'plus equity. The consequence is not a late return, it is a transmission '
    'the Agency refuses, and a refused transmission is not a filed '
    'return.</p>\n'
    '<p>That distinction matters on a catch-up, where several years are being '
    'sent in one sitting. One year that will not balance stops the sequence, '
    'because the next year opens from its closing figures.</p>'),
   ('usual-causes', 'The Three Causes Worth Checking First',
    '<p>Share capital left off the equity side is the commonest. A '
    'corporation that issued shares on incorporation has share capital '
    'whether or not anyone thinks of it as money, and a balance sheet filed '
    'as all zeroes omits it.</p>\n'
    '<p>A shareholder loan on the wrong side is the second. A balance owed '
    '<em>to</em> a shareholder is a liability; a balance owed '
    '<em>by</em> one is an asset, and they are not interchangeable.</p>\n'
    '<p>Retained earnings not carried forward is the third. The '
    + a(T + 'retained-earnings-rollforward-calculator/',
        'retained earnings rollforward calculator')
    + ' gives the figure the current year has to open from.</p>'),
   ('nil-sheets', 'A Nil Year Still Has to Balance',
    '<p>The income statement reporting zeroes does not make the balance sheet '
    'optional. Schedule 100 is filed on a nil year carrying whatever the '
    'corporation holds, and it has to balance like any other.</p>\n'
    '<p>A genuinely empty corporation, holding nothing and owing nothing, '
    'balances trivially at zero on all three lines. Most dormant '
    'corporations are not quite that empty.</p>'),
   ('what-this-is-not', 'What This Checker Does Not Do',
    '<p>It compares three totals you supply. It cannot tell you whether the '
    'totals are right, whether an item sits in the correct category, or '
    'whether a balance belongs on the return at all.</p>\n'
    '<p>A sheet that balances can still be wrong, and a sheet that balances '
    'at the wrong figures will transmit cleanly. This finds one specific '
    'defect, which is the one that stops a transmission.</p>'),
  ],
  faq=[
   ('What happens if my balance sheet does not balance?',
    'Schedule 100 will not validate and the transmission is refused. A '
    'refused transmission is not a filed return, so the year stays '
    'outstanding.'),
   ('Does a nil return still file a balance sheet?',
    'Yes. Schedule 100 is filed carrying whatever the corporation holds, even '
    'where the income statement reports nothing but zeroes.'),
   ('What usually causes the difference?',
    'Share capital left off the equity side, a shareholder loan on the wrong '
    'side, or retained earnings not carried forward from the previous '
    'year&#8217;s closing figure.'),
   ('Which side does a shareholder loan go on?',
    'A balance owed to a shareholder is a liability. A balance owed by a '
    'shareholder to the corporation is an asset. They are not '
    'interchangeable.'),
   ('Can a balance sheet balance and still be wrong?',
    'Yes. This checks one specific defect, the one that stops a transmission. '
    'It cannot tell you whether the totals themselves are right.'),
  ]),

 dict(slug='nil-gifi-balance-sheet-checker',
  title='Nil GIFI Balance Sheet Checker | What Schedule 100 Must Carry',
  h1_pre='Nil GIFI ', h1_span='Balance Sheet Checker',
  h1='Nil GIFI Balance Sheet Checker',
  eyebrow='Schedule 100', keyword='nil gifi balance sheet checker',
  meta=('A nil return is not an empty return. Four answers show which '
        'balances Schedule 100 has to carry, and which end the nil year.'),
  tags=['Four questions', 'Names each balance and its place',
        'Catches the all-zero mistake', 'Flags the bank interest trap'],
  form=tool('What the corporation holds',
            [yn('sc', 'Was share capital issued, on incorporation or since?'),
             yn('sl', 'Is there a balance owed to or by a shareholder?'),
             yn('re', 'Are retained earnings or a deficit carried forward?'),
             yn('bk', 'Does the corporation hold a bank balance?')],
            'Answer all four questions.'),
  js=None,
  sections=[
   ('not-empty', 'A Nil Return Is Not an Empty Return',
    '<p>This is the single most common misunderstanding about nil filing. The '
    'income statement reports zeroes, because nothing happened. The balance '
    'sheet reports what the corporation holds, because it holds it whether '
    'or not anything happened.</p>\n'
    '<p>Share capital issued on incorporation, a shareholder loan and '
    'retained earnings brought forward all sit on Schedule 100 on a year '
    'where the corporation did nothing at all.</p>'),
   ('all-zero', 'Filing It as All Zeroes Is Wrong in a Way That Persists',
    '<p>A balance sheet filed as entirely zero when share capital was issued '
    'is wrong, and the error does not stay in one year. The next return opens '
    'from the closing balances this one reports, so a wrong closing figure is '
    'a wrong opening figure next time.</p>\n'
    '<div class="ei-warn"><p>On a catch-up this compounds. Six years filed '
    'from a zeroed balance sheet are six years that will not reconcile '
    'against the corporate record, and the reconciliation is what a clearance '
    'request eventually rests on.</p></div>'),
   ('bank-trap', 'The Bank Balance Is Also the Nil-Status Trap',
    '<p>A bank balance belongs on the asset side, which is this '
    'page&#8217;s subject. It is also the commonest way a quiet year stops '
    'being nil, because interest credited to a corporate account is '
    'investment income whatever the amount.</p>\n'
    '<p>Four dollars of interest answers that question the same way four '
    'thousand would. ' + NOT_NIL + '</p>'),
   ('other-schedules', 'The Other Schedules a Nil Year Carries',
    '<p>Schedule 100 is the balance sheet, Schedule 125 the income statement '
    'and Schedule 141 the notes checklist. Schedule 24 appears on a first '
    'return only, and Schedule 50 reports every shareholder at 10% or '
    'more.</p>\n'
    '<p>The ' + a(T + 'gifi-schedule-requirement-checker/',
                  'GIFI schedule requirement checker')
    + ' works out which are required, and the '
    + a(T + 'balance-sheet-balancing-checker/',
        'balance sheet balancing checker')
    + ' tests whether the one here will validate.</p>'),
  ],
  faq=[
   ('Is a nil return&#8217;s balance sheet all zeroes?',
    'Rarely. Share capital issued on incorporation, a shareholder loan and '
    'retained earnings brought forward all sit on Schedule 100 whether or not '
    'anything happened during the year.'),
   ('What if I filed it as all zeroes?',
    'The closing figures are wrong, and the next return opens from them, so '
    'the error carries forward rather than staying in one year.'),
   ('Does a bank balance end a nil year?',
    'The balance itself does not. Interest credited on it is investment '
    'income whatever the amount, and that does.'),
   ('Where does share capital go?',
    'On the equity side of Schedule 100. A corporation that issued shares on '
    'incorporation has share capital even where no money changed hands in the '
    'year.'),
   ('Which schedules does a nil year file?',
    'Schedules 100, 125 and 141 where required, Schedule 24 on a first return '
    'only, Schedule 50 for every shareholder at 10% or more, and Schedule 8 '
    'where depreciable property is held.'),
  ]),

 dict(slug='schedule-8-cca-requirement-checker',
  title='Schedule 8 CCA Requirement Checker | Depreciable Property',
  h1_pre='Schedule 8 ', h1_span='CCA Requirement Checker',
  h1='Schedule 8 CCA Requirement Checker',
  eyebrow='Schedule 8', keyword='schedule 8 cca requirement checker',
  meta=('Three answers on whether Schedule 8 belongs on the return, why a '
        'carried balance is enough on its own, and what a disposal changes.'),
  tags=['Three questions', 'A carried balance is enough',
        'Claiming nothing is a choice', 'A disposal ends the nil year'],
  form=tool('Depreciable property',
            [yn('dp', 'Does the corporation hold any depreciable property?'),
             yn('uc', 'Is an undepreciated balance carried from an earlier '
                      'year?'),
             yn('ds', 'Was any of it disposed of during the year?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('what-it-is', 'What Schedule 8 Reports',
    '<p>Schedule 8 records capital cost allowance and the undepreciated '
    'balance carried forward. It is the schedule that tracks what the '
    'corporation owns in the way of equipment, vehicles and similar '
    'property, and how much of their cost is still to be claimed.</p>\n'
    '<p>It is filed with the T2 where the corporation holds depreciable '
    'property, and a nil year files it like any other year.</p>'),
   ('carried-balance', 'A Carried Balance Is Enough on Its Own',
    '<p>The schedule is not required only where something was bought or '
    'claimed. An undepreciated balance brought forward from an earlier year '
    'is enough: the balance has to be carried, and Schedule 8 is where it is '
    'carried.</p>\n'
    '<p>That is why a dormant corporation that bought a van four years ago '
    'and has done nothing since still files Schedule 8. The van did not stop '
    'existing because the corporation stopped trading.</p>'),
   ('claiming-nothing', 'Claiming Nothing in a Quiet Year Is a Choice',
    '<p>Capital cost allowance is a claim, not an obligation. A corporation '
    'with no income has nothing to reduce, so claiming allowance in a nil '
    'year generally achieves nothing and simply shrinks the balance '
    'available later.</p>\n'
    '<p>The balance carries forward either way, which is the point of the '
    'schedule. The '
    + a(G + 'schedule-8-and-loss-continuity/',
        'guide to Schedule 8 and loss continuity')
    + ' goes further into the interaction with losses.</p>'),
   ('disposal', 'A Disposal Ends the Nil Year',
    '<p>Selling or transferring depreciable property is a disposition, and a '
    'disposition is activity. The year it happened in is not a nil year, '
    'whatever else the corporation did or did not do.</p>\n'
    '<p>' + NOT_NIL + '</p>\n'
    '<p>This matters most at a wind-up, because a corporation cannot be '
    'dissolved holding property. The '
    + a(T + 'dissolution-readiness-checker/', 'dissolution readiness checker')
    + ' covers that sequence.</p>'),
  ],
  faq=[
   ('When is Schedule 8 required?',
    'Where the corporation holds depreciable property, or carries an '
    'undepreciated balance from an earlier year. Either one on its own is '
    'enough.'),
   ('Does a nil year file Schedule 8?',
    'Yes, where depreciable property is held or a balance is carried forward. '
    'The property does not stop existing because the corporation stopped '
    'trading.'),
   ('Do I have to claim capital cost allowance?',
    'No. It is a claim rather than an obligation, and a corporation with no '
    'income has nothing to reduce. The balance carries forward either way.'),
   ('What if I sold the property during the year?',
    'A disposition is activity, so that year is not a nil year. Those returns '
    'are handled by Gondaliya CPA Professional Corporation at gondaliyacpa.ca '
    'at $350.00 plus HST per year.'),
   ('Is Schedule 8 covered by the fee?',
    'Yes. Where the year is nil, Schedule 8 and the loss continuity are '
    'recorded within the fee of $300.00 plus HST per tax year.'),
  ]),

 dict(slug='involuntary-dissolution-risk-checker',
  title='Involuntary Dissolution Risk Checker | Struck by the Registry',
  h1_pre='Involuntary Dissolution ', h1_span='Risk Checker',
  h1='Involuntary Dissolution Risk Checker',
  eyebrow='Registry', keyword='involuntary dissolution risk checker',
  meta=('A missed annual return gets a corporation struck, not charged. '
        'Three answers on the exposure and why the tax years survive it.')
  ,
  tags=['Three registry questions', 'Striking, not a charge',
        'The tax years survive it', 'Revival is the way back'],
  form=tool('The registry record',
            [yn('ar', 'Has the annual return been filed for the current '
                      'period?'),
             yn('ad', 'Is the registered office address current?'),
             yn('dr', 'Is the director record current?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('not-a-charge', 'A Missed Annual Return Produces a Striking',
    '<p>The annual return is a registry filing, not a tax return. It confirms '
    'the directors, the registered office and that the corporation still '
    'exists, and it reports no income.</p>\n'
    '<p>Missing it does not produce a charge. It produces a striking: the '
    'registry dissolves the corporation involuntarily. A corporation can be '
    'perfectly current on tax and still be dissolved this way, which is the '
    'part that surprises people.</p>'),
   ('address', 'A Stale Address Is What Makes It Happen Quietly',
    '<p>The registry sends its warning to the registered office. Where that '
    'address is a former accountant&#8217;s office or a home the shareholder '
    'moved out of, the warning arrives nowhere and the striking happens '
    'without anyone noticing.</p>\n'
    '<p>A dormant corporation is the most likely to be in exactly this '
    'position, because nobody is checking the post at an office nobody uses. '
    'Keeping the address current is the least demanding piece of maintenance '
    'there is, and the one most often left.</p>'),
   ('tax-survives', 'The Tax Years Survive the Striking',
    '<p>Being struck settles nothing with the Canada Revenue Agency. The '
    'corporation&#8217;s tax years stay open and unfiled, and an unfiled year '
    'does not expire. A corporation struck in 2021 still owes every return it '
    'owed in 2021.</p>\n'
    '<p>That is why a striking is not a way of closing a corporation. It ends '
    'the legal existence and leaves the tax side exactly as it was, which is '
    'the opposite of a clean wind-up.</p>'),
   ('revival', 'Revival Is the Way Back',
    '<p>Registries provide for revival, which restores the corporation so the '
    'outstanding filings can be made and a proper wind-up completed. The open '
    'tax years are waiting, and they are filed oldest first.</p>\n'
    '<p>Each year is its own return at ' + PRICE + '. The '
    + a(G + 'winding-up-an-inactive-corporation/',
        'guide to winding up an inactive corporation')
    + ' sets out the order the steps have to happen in.</p>'),
  ],
  faq=[
   ('What happens if I miss the annual return?',
    'The registry can dissolve the corporation involuntarily. That is a '
    'striking rather than a charge, and it can happen while the corporation '
    'is fully current on tax.'),
   ('Does being struck close my tax account?',
    'No. The tax years stay open and unfiled, and an unfiled year does not '
    'expire. A striking ends the legal existence and settles nothing on the '
    'tax side.'),
   ('Why did I not get a warning?',
    'The registry writes to the registered office. Where that address is out '
    'of date the warning arrives nowhere, which is how most strikings happen '
    'unnoticed.'),
   ('Can a struck corporation be restored?',
    'Registries provide for revival, which restores it so the outstanding '
    'filings can be made and a proper wind-up completed.'),
   ('Is the annual return covered by the nil T2 fee?',
    'No. It is a registry filing and sits outside the fee, which covers one '
    'nil T2 return for one corporation for one tax year.'),
  ]),

 dict(slug='director-liability-exposure-checker',
  title='Director Liability Exposure Checker | Which Amounts Reach You',
  h1_pre='Director Liability ', h1_span='Exposure Checker',
  h1='Director Liability Exposure Checker',
  eyebrow='Directors', keyword='director liability exposure checker',
  meta=('Payroll source deductions and net GST/HST can be assessed against '
        'directors personally. Corporate income tax on its own cannot.')
  ,
  tags=['Three questions', 'Withheld money reaches you',
        'Corporate tax on its own does not', 'Closing accounts ends it'],
  form=tool('What the corporation owes',
            [yn('pd', 'Are there payroll source deductions withheld and not '
                      'remitted?'),
             yn('gh', 'Is there net GST/HST collected and not remitted?'),
             yn('ci', 'Is there corporate income tax owing?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('the-pattern', 'The Pattern Is Money That Was Never the Corporation&#8217;s',
    '<p>Certain amounts a corporation was required to withhold or collect and '
    'remit can be assessed against its directors personally. Payroll source '
    'deductions and net GST/HST are the two that matter here.</p>\n'
    '<p>The reason is that the money was never the '
    'corporation&#8217;s to keep. Source deductions were withheld from '
    'someone&#8217;s pay and GST/HST was collected from customers, both on the '
    'Agency&#8217;s behalf. Corporate income tax is different: it is the '
    'corporation&#8217;s own liability, and on its own it does not reach a '
    'director.</p>'),
   ('dormant', 'Why This Reaches Dormant Corporations',
    '<p>A dormant corporation rarely owes corporate income tax, because a nil '
    'year assesses at $0.00. What it often has is an account nobody closed: a '
    'payroll account from when it had staff, or a GST/HST account from when it '
    'was registered.</p>\n'
    '<p>While those accounts are open they keep generating obligations, and '
    'the amounts they generate are exactly the ones that reach directors. '
    'That is the practical case for closing them rather than ignoring '
    'them.</p>\n'
    '<div class="ei-warn"><p>' + QUAL + '</p></div>'),
   ('closing', 'Closing the Accounts Is What Ends It',
    '<p>Form RC145 closes a GST/HST account and a payroll account. Until an '
    'account is closed, nil returns and nil remittances remain due on it, '
    'separately from the T2.</p>\n'
    '<p>Neither closure is covered by the nil T2 fee. The '
    + a(T + 'gst-hst-account-closure-checker/',
        'GST/HST account closure checker') + ' and the '
    + a(T + 'payroll-nil-remittance-checker/',
        'payroll nil remittance checker')
    + ' each cover one of them.</p>'),
   ('not-advice', 'What This Checker Is Not',
    '<p>It sorts three kinds of amount into the ones that can reach a '
    'director and the one that does not. It does not assess whether a '
    'particular director is liable, which turns on facts about the director '
    'and the period that no web page can take in.</p>\n'
    '<p>Where an assessment has been raised or threatened against a director '
    'personally, that is a matter for Gondaliya CPA Professional Corporation '
    'at gondaliyacpa.ca rather than a form on this site.</p>'),
  ],
  faq=[
   ('Which corporate amounts can reach a director personally?',
    'Amounts the corporation was required to withhold or collect and remit, '
    'including payroll source deductions and net GST/HST.'),
   ('Does corporate income tax reach directors?',
    'Not on its own. It is the corporation&#8217;s own liability, collectible '
    'from the corporation, and the Agency has statutory collection powers it '
    'can use without going to court.'),
   ('Why does this matter to a dormant corporation?',
    'Because a nil year owes no corporate income tax but an unclosed payroll '
    'or GST/HST account keeps generating exactly the amounts that do reach '
    'directors.'),
   ('How do I end the exposure?',
    'Close the accounts. Form RC145 closes a GST/HST account and a payroll '
    'account, and until then nil returns and nil remittances remain due on '
    'them.'),
   ('Is an assessment against me personally covered here?',
    'No. That turns on facts about the director and the period, and it is a '
    'matter for Gondaliya CPA Professional Corporation at gondaliyacpa.ca.'),
  ]),
]

# ---------------------------------------------------------------------------
# Static reference tables, added 2026-10-29 after publication.
#
# Tools 1 to 30 each carry a table in the body prose that a visitor can read
# without touching the form. This batch shipped without one and only drew a
# table after input. Navneet caught it by comparing a new page against tool
# 21, whose table is "What happened / Effect on the count / Returns owed".
#
# Each table restates facts the page already asserts, which is what the
# earlier batches' tables do: the value is that a visitor gets the shape of
# the answer before entering anything. gate6.py now requires one.
# ---------------------------------------------------------------------------

def _tbl(head, rows):
    h = ('<table class="ei-tbl"><thead><tr>'
         + ''.join('<th scope="col">%s</th>' % c for c in head)
         + '</tr></thead><tbody>')
    for r in rows:
        h += '<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>'
    return h + '</tbody></table>'


TABLES6 = {
 'corporate-balance-due-date-calculator': ('two-dates', _tbl(
   ['Obligation', 'When it falls', 'On a nil year'],
   [['A balance of tax', 'Two months after the year-end, or three for a '
     'qualifying CCPC', 'Nothing is owed on it'],
    ['The T2 return', 'Six months after the year-end', 'Still due'],
    ['Instalments', 'Through the year, from the previous year&#8217;s tax',
     'None, because a nil year sets that at $0.00']])),

 'fiscal-period-length-calculator': ('why-length', _tbl(
   ['Length of the period', 'What it is', 'What follows from it'],
   [['Up to 371 days', 'Available as a first tax year', 'One return'],
    ['Under twelve months', 'A short tax year',
     'A separate return, on the same six-month rule'],
    ['Twelve months', 'A full tax year', 'The ordinary case'],
    ['More than 371 days', 'Not a tax year at all',
     'The year-end being used is not the one on record']])),

 'cra-demand-to-file-deadline-calculator': ('what-changes', _tbl(
   ['Stage', 'What it is', 'What ends it'],
   [['An overdue return', 'The year is simply unfiled', 'Filing it'],
    ['A demand to file',
     'A written requirement to file a named return by a named date',
     'Filing the named return'],
    ['An arbitrary assessment',
     'The Agency&#8217;s own estimate of income, which is collectible',
     'A filed return displacing it']])),

 't4-nil-filing-requirement-checker': ('calendar', _tbl(
   ['Obligation', 'Measured from', 'When it falls'],
   [['The T2 return', 'The fiscal year-end', 'Six months after it'],
    ['The T4 information return', 'The calendar year',
     'The end of the following February'],
    ['Nil payroll remittances', 'Each remittance period',
     'For as long as the account is open']])),

 'retained-earnings-rollforward-calculator': ('one-line', _tbl(
   ['Line', 'What it does to the figure'],
   [['Opening retained earnings', 'The starting point'],
    ['Net income for the year', 'Added'],
    ['Dividends declared', 'Subtracted'],
    ['Closing retained earnings',
     'The result, and what the next return opens from']])),

 'balance-sheet-balancing-checker': ('usual-causes', _tbl(
   ['Cause', 'Where the item belongs', 'How it goes wrong'],
   [['Share capital issued on incorporation', 'Equity',
     'Left off, because nobody thinks of it as money'],
    ['A balance owed to a shareholder', 'A liability',
     'Put on the asset side'],
    ['A balance owed by a shareholder', 'An asset',
     'Put on the liability side'],
    ['Retained earnings brought forward', 'Equity',
     'Not carried from last year&#8217;s closing figure']])),

 'nil-gifi-balance-sheet-checker': ('other-schedules', _tbl(
   ['Schedule', 'What it reports', 'On a nil year'],
   [['100', 'The balance sheet',
     'Filed, carrying whatever the corporation holds'],
    ['125', 'The income statement', 'Filed, reporting zeroes'],
    ['141', 'The notes checklist', 'Filed where required'],
    ['24', 'First-return information', 'A first return only'],
    ['50', 'Every shareholder at 10% or more',
     'Filed where there is one'],
    ['8', 'Capital cost allowance',
     'Where depreciable property is held']])),

 'schedule-8-cca-requirement-checker': ('carried-balance', _tbl(
   ['The position', 'Schedule 8 required', 'Effect on nil status'],
   [['Depreciable property is held', 'Yes', 'None'],
    ['An undepreciated balance is carried forward', 'Yes', 'None'],
    ['Property was disposed of during the year', 'Yes',
     'The year is not nil'],
    ['Neither held nor carried forward', 'No', 'None']])),

 'involuntary-dissolution-risk-checker': ('not-a-charge', _tbl(
   ['Filing', 'What it reports', 'What missing it produces'],
   [['The registry annual return',
     'The directors, the registered office, and that the corporation exists',
     'A striking: the registry dissolves the corporation'],
    ['The T2 return', 'The tax year',
     'An unfiled year that stays open and does not expire']])),

 'director-liability-exposure-checker': ('the-pattern', _tbl(
   ['Amount', 'Whose money it was', 'Can be assessed against a director'],
   [['Payroll source deductions', 'Withheld from someone&#8217;s pay',
     'Yes'],
    ['Net GST/HST', 'Collected from customers', 'Yes'],
    ['Corporate income tax', 'The corporation&#8217;s own liability',
     'No, not on its own']])),
}

assert set(TABLES6) == {t['slug'] for t in TOOLS6}, 'TABLES6 vs TOOLS6'
for t in TOOLS6:
    _sid, _html = TABLES6[t['slug']]
    _ids = [s for s, _, _ in t['sections']]
    assert _sid in _ids, '%s: no section %r (has %r)' % (t['slug'], _sid, _ids)
    t['sections'] = [(s, h, (b + '\n' + _html) if s == _sid else b)
                     for s, h, b in t['sections']]


SEO = {
 'corporate-balance-due-date-calculator': (
   'Corporate Balance Due Date Calculator | Two Months',
   'Paying a balance of tax is due before the return is. Enter the fiscal '
   'year-end for both dates, on the same holiday calendar.'),
 'fiscal-period-length-calculator': (
   'Fiscal Period Length Calculator | The 53-Week Limit',
   'Enter the first and last day of a fiscal period for its length in days '
   'and weeks, whether it clears 371 days, and its T2 date.'),
 'cra-demand-to-file-deadline-calculator': (
   'CRA Demand to File Deadline Calculator',
   'A demand to file names a date. Enter the letter date and the days it '
   'allows for the deadline, the days left and the business days left.'),
 't4-nil-filing-requirement-checker': (
   'T4 Nil Filing Requirement Checker | Payroll',
   'An open payroll account expects a T4 information return even where '
   'nobody was paid. Three answers give the date and what is owed.'),
 'retained-earnings-rollforward-calculator': (
   'Retained Earnings Rollforward Calculator',
   'Opening, plus net income, less dividends, gives closing. The figure the '
   'next return opens from, and what it says about nil status.'),
 'balance-sheet-balancing-checker': (
   'Balance Sheet Balancing Checker | Schedule 100',
   'Assets must equal liabilities plus equity or Schedule 100 will not '
   'validate. Enter the three totals to see the difference.'),
 'nil-gifi-balance-sheet-checker': (
   'Nil GIFI Balance Sheet Checker | Schedule 100',
   'A nil return is not an empty return. Four answers show which balances '
   'Schedule 100 has to carry, and which end the nil year.'),
 'schedule-8-cca-requirement-checker': (
   'Schedule 8 CCA Requirement Checker | Nil T2',
   'Three answers on whether Schedule 8 belongs on the return, why a carried '
   'balance is enough on its own, and what a disposal changes.'),
 'involuntary-dissolution-risk-checker': (
   'Involuntary Dissolution Risk Checker | Struck',
   'A missed annual return gets a corporation struck, not charged. Three '
   'answers on the exposure and why the tax years survive it.'),
 'director-liability-exposure-checker': (
   'Director Liability Exposure Checker | Nil T2',
   'Payroll source deductions and net GST/HST can be assessed against '
   'directors personally. Corporate income tax on its own cannot.'),
}

for t in TOOLS6:
    t['seo_title'], t['seo_desc'] = SEO[t['slug']]
    assert len(t['seo_title']) <= 60, (
        '%s: SEO title is %d characters' % (t['slug'], len(t['seo_title'])))
    assert len(t['seo_desc']) <= 160, (
        '%s: SEO description is %d characters'
        % (t['slug'], len(t['seo_desc'])))
assert set(SEO) == {t['slug'] for t in TOOLS6}, 'SEO map does not match TOOLS6'

for t, js in zip(TOOLS6, [T31_JS, T32_JS, T33_JS, T34_JS, T35_JS, T36_JS,
                          T37_JS, T38_JS, T39_JS, T40_JS]):
    t['js'] = js if js.startswith(PRELUDE) else PRELUDE + js

ORDER6 = ORDER5 + [t['slug'] for t in TOOLS6]
LINK_TITLE6 = dict(LINK_TITLE5, **{
 'corporate-balance-due-date-calculator':
     'Corporate balance due date calculator',
 'fiscal-period-length-calculator': 'Fiscal period length calculator',
 'cra-demand-to-file-deadline-calculator':
     'CRA demand to file deadline calculator',
 't4-nil-filing-requirement-checker': 'T4 nil filing requirement checker',
 'retained-earnings-rollforward-calculator':
     'Retained earnings rollforward calculator',
 'balance-sheet-balancing-checker': 'Balance sheet balancing checker',
 'nil-gifi-balance-sheet-checker': 'Nil GIFI balance sheet checker',
 'schedule-8-cca-requirement-checker': 'Schedule 8 CCA requirement checker',
 'involuntary-dissolution-risk-checker':
     'Involuntary dissolution risk checker',
 'director-liability-exposure-checker':
     'Director liability exposure checker',
})

# Siblings are named by slug rather than by index into ORDER6. Batch 5 used
# indices, which worked but meant every entry had to be counted out by hand
# against a list that grows each batch; a mistyped index silently links the
# wrong tool. A slug that does not exist fails the build instead.
SIBLINGS6 = {
 'corporate-balance-due-date-calculator': [
   'nil-t2-deadline-calculator', 'due-date-weekend-holiday-shift-calculator',
   'next-t2-due-date-checker'],
 'fiscal-period-length-calculator': [
   '53-week-first-tax-year-checker', 'short-tax-year-deadline-calculator',
   'corporate-fiscal-year-end-calculator'],
 'cra-demand-to-file-deadline-calculator': [
   'unfiled-years-checker', 'unfiled-years-cost-calculator',
   'days-overdue-calculator'],
 't4-nil-filing-requirement-checker': [
   'payroll-nil-remittance-checker', 'gst-hst-account-closure-checker',
   'gst-hst-nil-filing-checker'],
 'retained-earnings-rollforward-calculator': [
   'nil-gifi-balance-sheet-checker', 'balance-sheet-balancing-checker',
   'gifi-schedule-requirement-checker'],
 'balance-sheet-balancing-checker': [
   'nil-gifi-balance-sheet-checker', 'retained-earnings-rollforward-calculator',
   'gifi-schedule-requirement-checker'],
 'nil-gifi-balance-sheet-checker': [
   'gifi-schedule-requirement-checker', 'balance-sheet-balancing-checker',
   'dormant-corporation-test'],
 'schedule-8-cca-requirement-checker': [
   'gifi-schedule-requirement-checker',
   'schedule-50-shareholder-threshold-checker',
   'nil-t2-document-checklist-checker'],
 'involuntary-dissolution-risk-checker': [
   'federal-annual-return-anniversary-calculator',
   'dissolution-readiness-checker',
   'clearance-certificate-requirement-checker'],
 'director-liability-exposure-checker': [
   'payroll-nil-remittance-checker', 'gst-hst-account-closure-checker',
   'nil-return-late-penalty-checker'],
}

GUIDES6 = {
 'corporate-balance-due-date-calculator': [
   ('t2-filing-deadlines', 'The complete guide to T2 filing deadlines')],
 'fiscal-period-length-calculator': [
   ('first-year-t2-filing', 'The complete guide to first-year T2 filing'),
   ('t2-filing-deadlines', 'The complete guide to T2 filing deadlines')],
 'cra-demand-to-file-deadline-calculator': [
   ('cra-demand-to-file-response', 'Responding to a CRA demand to file'),
   ('corporate-tax-arrears-and-interest',
    'Corporate tax arrears and interest')],
 't4-nil-filing-requirement-checker': [
   ('corporate-compliance-calendar', 'The corporate compliance calendar')],
 'retained-earnings-rollforward-calculator': [
   ('gifi-schedules-100-125-141', 'GIFI Schedules 100, 125 and 141')],
 'balance-sheet-balancing-checker': [
   ('gifi-schedules-100-125-141', 'GIFI Schedules 100, 125 and 141')],
 'nil-gifi-balance-sheet-checker': [
   ('gifi-schedules-100-125-141', 'GIFI Schedules 100, 125 and 141'),
   ('zero-activity-corporate-tax-returns',
    'Zero-activity corporate tax returns')],
 'schedule-8-cca-requirement-checker': [
   ('schedule-8-and-loss-continuity', 'Schedule 8 and loss continuity')],
 'involuntary-dissolution-risk-checker': [
   ('winding-up-an-inactive-corporation',
    'Winding up an inactive corporation'),
   ('provincial-and-federal-annual-returns',
    'Provincial and federal annual returns')],
 'director-liability-exposure-checker': [
   ('corporate-tax-arrears-and-interest',
    'Corporate tax arrears and interest'),
   ('winding-up-an-inactive-corporation',
    'Winding up an inactive corporation')],
}

# ------------------------------------------------------------------- guards
import re as _re

_ORDER = set(ORDER6)
_GUIDES_LIVE = {
 'nil-t2-return-complete-guide', 'dormant-and-inactive-corporations',
 'catch-up-unfiled-corporate-tax-returns', 'final-t2-and-dissolution',
 't2-short-eligibility', 'provincial-and-federal-annual-returns',
 't183corp-signing-and-transmission', 'how-to-file-a-nil-t2-return',
 'gifi-schedules-100-125-141', 'schedule-8-and-loss-continuity',
 'first-year-t2-filing', 'numbered-company-tax-filing',
 't2-late-filing-penalties', 'cra-demand-to-file-response',
 'inactive-holding-company-filing', 't2-schedules-on-a-nil-return',
 'shelf-corporation-compliance', 't2-filing-deadlines',
 'zero-activity-corporate-tax-returns', 'corporate-tax-arrears-and-interest',
 'winding-up-an-inactive-corporation', 'small-business-corporate-filing',
 'corporate-compliance-calendar', 'numbered-company-maintenance',
 'mandatory-t2-electronic-filing', 'schedule-50-and-shareholder-reporting',
 'non-resident-owned-corporation-nil-filing',
}

assert len(TOOLS6) == 10, '%d tools in batch 6' % len(TOOLS6)
assert len({t['slug'] for t in TOOLS6}) == 10, 'duplicate slug in the batch'

for t in TOOLS6:
    # A section anchor sharing an id with a form field is silently wrong,
    # because getElementById returns whichever comes first in the document.
    _sec = {sid for sid, _, _ in t['sections']}
    _fld = set(_re.findall(r'id="([\w-]+)"', t['form']))
    _fld |= set(_re.findall(r'name="([\w-]+)"', t['form']))
    _clash = _sec & _fld
    assert not _clash, ('%s: section anchor collides with a form id: %s'
                        % (t['slug'], sorted(_clash)))

    # Every decision tree compares against the alphabet the form emits.
    _vals = set(_re.findall(r'value="([^"]*)"', t['form']))
    assert _vals <= {'y', 'n'}, ('%s: form emits values outside {y,n}: %s'
                                 % (t['slug'], sorted(_vals - {'y', 'n'})))

    # The prelude is declared once per page.
    assert t['js'].count(PRELUDE) == 1, (
        '%s: the prelude appears %d times in its script'
        % (t['slug'], t['js'].count(PRELUDE)))

    # pick() without its definition is a ReferenceError the moment a radio
    # changes, and the page simply stops updating with no error on screen.
    if 'pick(' in t['js']:
        assert 'function pick(' in t['js'], (
            '%s: calls pick() without carrying its definition; build on '
            'RBASE rather than BASE' % t['slug'])

    # Reading an input during render rather than through the logic function
    # splits the result between two sources, which is how a render and its
    # own logic end up disagreeing.
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

    assert len(t['sections']) == 4, (
        '%s has %d sections' % (t['slug'], len(t['sections'])))
    assert len(t['faq']) == 5, '%s has %d FAQs' % (t['slug'], len(t['faq']))
    assert len(t['tags']) == 4, '%s has %d tags' % (t['slug'], len(t['tags']))

    # Rule 3: the bare phrase never appears; the qualification travels whole.
    _body = ' '.join(b for _, _, b in t['sections'])
    _body += ' '.join(q + ' ' + aa for q, aa in t['faq'])
    assert 'no penalty' not in _body.lower(), (
        '%s: the bare phrase "no penalty" appears' % t['slug'])

# Every slug is new, and every link target exists.
_LIVE = set(ORDER5)
for t in TOOLS6:
    assert t['slug'] not in _LIVE, '%s is already live' % t['slug']
    for s in SIBLINGS6[t['slug']]:
        assert s in _ORDER, '%s links to tool %s, which does not exist' % (
            t['slug'], s)
        assert s != t['slug'], '%s lists itself as a sibling' % t['slug']
        assert s in LINK_TITLE6, '%s has no link title' % s
    for g, _ttl in GUIDES6[t['slug']]:
        assert g in _GUIDES_LIVE, (
            '%s links to guide %s, which is not live' % (t['slug'], g))
assert set(SIBLINGS6) == {t['slug'] for t in TOOLS6}, 'SIBLINGS6 mismatch'
assert set(GUIDES6) == {t['slug'] for t in TOOLS6}, 'GUIDES6 mismatch'

# Body links must resolve too. A /tools/ or /guides/ href typed into prose is
# not covered by the sibling and guide maps above.
for t in TOOLS6:
    _all = ' '.join(b for _, _, b in t['sections']) + t['form']
    for s in set(_re.findall(r'/tools/([a-z0-9-]+)/', _all)):
        assert s in _ORDER, '%s: body links to /tools/%s/, which does not exist' % (
            t['slug'], s)
    for g in set(_re.findall(r'/guides/([a-z0-9-]+)/', _all)):
        assert g in _GUIDES_LIVE, (
            '%s: body links to /guides/%s/, which is not live' % (t['slug'], g))

for t in TOOLS6:
    rel = [(T + s + '/', LINK_TITLE6[s]) for s in SIBLINGS6[t['slug']]]
    rel += [(G + g + '/', ttl) for g, ttl in GUIDES6[t['slug']]]
    rel.append((COST, 'Nil T2 filing cost'))
    t['related'] = rel


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'October 29, 2026', '2026-10-29'
    recs = []
    for t in TOOLS6:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2f-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-46s %6d bytes' % (r['slug'], len(r['content'].encode())))
