# -*- coding: utf-8 -*-
"""Family 2, tools 16 to 20.

Structure, CSS, render() and schema come from build_f2; the form helpers from
build_f2b; the shared dueDate/parse/money blocks and the identity assertion
from build_f2c. Four batches, one set of rules.

Selection, and why it departs from Appendix A order for the first time.

Appendix A's next eight F2 entries are, in order: price with HST, business
number status, inactive corporation filing, dormant corporation obligation,
zero activity corporation, nil return vs full return, nil T2 document
checklist, T2 filing requirement. Four of those cannot be built as distinct
tools:

  /dormant-corporation-obligation-checker/  and
  /zero-activity-corporation-checker/       and
  /t2-filing-requirement-checker/
      all ask the question /tools/dormant-corporation-test/ already answers
      with ten activity questions, or the one
      /tools/nil-t2-eligibility-checker/ answers with four gates. Line 1210
      requires a calculator logic block and result strings unique to that
      tool. Three more screens asking the same thing in synonyms would not
      pass that, so they are not built.

  /nil-t2-price-with-hst-calculator/
      needs the tax rate that applies to this service in each province. The
      plan states the price and nothing about the rate, the price itself is
      under a standing correction from including HST to plus HST, and whether
      a provincial sales tax applies to an accounting service supplied from
      Ontario is a tax determination. Line 1212 reserves that kind of claim
      for Sharad Gondaliya. Not built, for the same reason the Ontario annual
      return due date calculator is not built.

That leaves four buildable entries from this stretch. The fifth is
/due-date-weekend-holiday-shift-calculator/, Appendix A item 24, brought
forward because it is fully grounded in the holiday engine the deadline
calculator already uses and tested.

Logged as the twelfth Appendix A conflict. The four skipped slugs are not
lost: they are available if Sharad wants them differentiated rather than
dropped, and the running total of 150 is unaffected by which five were built
first.
"""
import io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_f2 import (render, meta, yn, a, DATE_JS, SITE, HUB, FORM, PRICE,
                      NOT_NIL, TOOL_DISCLAIMER)
from build_f2b import tool, num, date, out_box, PICK, T, G, COST
from build_f2c import (DUE_JS, MONEY_JS, PARSE_JS, QUAL, PRELUDE,
                       ORDER3, LINK_TITLE3)

# --------------------------------------------- 16. business number status
L16 = r"""
// Always four rows, one per answer, because a status checker that only
// reports problems cannot say what the clean answers mean. `act` marks the
// rows that need something done. Note the asymmetry: a MISSING corporation
// income tax account needs action, because a T2 is transmitted against it,
// while an OPEN GST/HST or payroll account needs action, because it carries
// filings of its own.
function bnRows(a){
  if(a.bn===null||a.rc===null||a.rt===null||a.rp===null){return null;}
  return [{k:'bn', v:a.bn, act:a.bn==='n'},
          {k:'rc', v:a.rc, act:a.rc==='n'},
          {k:'rt', v:a.rt, act:a.rt==='y'},
          {k:'rp', v:a.rp, act:a.rp==='y'}];
}
function bnActions(rows){
  return rows.filter(function(r){return r.act;}).length;
}
"""
T16_JS = PICK + L16 + r"""
var out=document.getElementById('out');
var IDS=['bn','rc','rt','rp'];
var LBL={bn:'Business Number',rc:'Corporation income tax',
         rt:'GST/HST',rp:'Payroll'};
var SAY={
 'bn.y':'Known, so a return can be transmitted against it.',
 'bn.n':'Not known yet. It is on a notice of assessment, in My Business Account, and on the corporation&rsquo;s registration documents. A T2 cannot be transmitted without it.',
 'rc.y':'On record. A T2 is due for every tax year until the corporation is formally dissolved, six months after each fiscal year-end.',
 'rc.n':'Not on record. A T2 is transmitted against this account, so confirm with the Canada Revenue Agency that it exists before filing.',
 'rt.y':'Open. It still needs its own returns, nil ones included, or a Form RC145 closure. The nil T2 does not cover it.',
 'rt.n':'Not open, so there is nothing to file and nothing to close.',
 'rp.y':'Open. It still needs its own remittances, nil ones included, or a Form RC145 closure. The nil T2 does not cover it.',
 'rp.n':'Not open, so there is nothing to file and nothing to close.'
};
function render(){
  var a={};IDS.forEach(function(k){a[k]=pick(k);});
  var rows=bnRows(a);
  if(rows===null){out.className='ei-out';
    out.innerHTML='<p>Answer all four and the account picture appears here.</p>';
    return;}
  var acts=bnActions(rows);
  var h='<h3>'+(acts===0?'Nothing on this list needs action'
      :acts+' of 4 need'+(acts===1?'s':'')+' something done')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Account</th>'+
     '<th scope="col">Status</th><th scope="col">What it means</th>'+
     '</tr></thead><tbody>';
  rows.forEach(function(r){
    h+='<tr><td>'+LBL[r.k]+'</td><td>'+(r.act?'Needs action':'Clear')+
       '</td><td>'+SAY[r.k+'.'+r.v]+'</td></tr>';});
  h+='</tbody></table>';
  h+='<p>Only the corporation income tax return is covered by '+PRICE_JS+
     '. The GST/HST and payroll accounts are separate filings.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className=acts===0?'ei-out ok':'ei-out no';
  out.innerHTML=h;
}
IDS.forEach(function(k){
  Array.prototype.forEach.call(document.querySelectorAll('input[name="'+k+'"]'),
    function(e){e.addEventListener('change',render);});});
render();
"""

# ------------------------------------ 17. inactive corporation filing checker
L17 = r"""
// The T2 is always owed. Everything else depends on how the corporation is
// registered and which programme accounts are open.
function extraFilings(a){
  if(a.fed===null||a.ont===null||a.gst===null||a.pay===null){return null;}
  var o=['t2'];
  if(a.fed==='y'){o.push('fedar');}
  if(a.ont==='y'){o.push('ontar');}
  if(a.gst==='y'){o.push('gst');}
  if(a.pay==='y'){o.push('pay');}
  return o;
}
"""
T17_JS = PICK + L17 + r"""
var out=document.getElementById('out');
var IDS=['fed','ont','gst','pay'];
var FIL={
 t2:['Nil T2 corporate return','Canada Revenue Agency','Yes, at '],
 fedar:['Federal annual return','Corporations Canada','No. $12.00 government fee, due within 60 days of the anniversary'],
 ontar:['Ontario annual return','Ontario Business Registry','No. Filed separately from the T2'],
 gst:['GST/HST return, nil or otherwise','Canada Revenue Agency','No. Or close the account with Form RC145'],
 pay:['Payroll remittance, nil or otherwise','Canada Revenue Agency','No. Or close the account with Form RC145']
};
function render(){
  var a={};IDS.forEach(function(k){a[k]=pick(k);});
  var f=extraFilings(a);
  if(f===null){out.className='ei-out';
    out.innerHTML='<p>Answer all four and the list of filings appears here.</p>';
    return;}
  var extra=f.length-1;
  var h='<h3>'+(extra===0
      ? 'The nil T2 is the only filing on this list'
      : extra+' filing'+(extra===1?'':'s')+' sit beside the nil T2')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Filing</th>'+
     '<th scope="col">Goes to</th><th scope="col">Covered by the fee</th>'+
     '</tr></thead><tbody>';
  f.forEach(function(k){
    var cov=FIL[k][2];
    h+='<tr><td>'+FIL[k][0]+'</td><td>'+FIL[k][1]+'</td><td>'+
       (k==='t2'?cov+PRICE_JS:cov)+'</td></tr>';});
  h+='</tbody></table>';
  if(extra){
    h+='<p>The fee covers the nil T2 and nothing else on that list. We tell '+
       'you which of the others you still owe, but they are filed '+
       'separately.</p>';
    out.className='ei-out no';
  }else{
    h+='<p>With no open programme accounts and no separate registry filing, '+
       'the nil T2 is the whole of it.</p>';
    out.className='ei-out ok';
  }
  h+='<p>An Alberta AT1 and a Quebec CO-17 are separate provincial returns '+
     'and are not included in the fee either.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.innerHTML=h;
}
IDS.forEach(function(k){
  Array.prototype.forEach.call(document.querySelectorAll('input[name="'+k+'"]'),
    function(e){e.addEventListener('change',render);});});
render();
"""

# ----------------------------------------- 18. nil return vs full return
L18 = r"""
function whichReturn(a){
  if(a.rev===null||a.inv===null||a.div===null||a.disp===null){return null;}
  var hits=[];
  if(a.rev==='y'){hits.push('revenue or expenses');}
  if(a.inv==='y'){hits.push('investment or rental income');}
  if(a.div==='y'){hits.push('a dividend paid or received');}
  if(a.disp==='y'){hits.push('an asset sold or transferred');}
  return hits;
}
"""
T18_JS = PICK + L18 + r"""
var out=document.getElementById('out');
var IDS=['rev','inv','div','disp'];
function render(){
  var a={};IDS.forEach(function(k){a[k]=pick(k);});
  var hits=whichReturn(a);
  if(hits===null){out.className='ei-out';
    out.innerHTML='<p>Answer all four and the answer appears here.</p>';return;}
  var nil=hits.length===0;
  var h='<h3>'+(nil?'A nil return':'A full return')+'</h3>';
  if(nil){
    h+='<p>Nothing came in and nothing went out, so the year is reported as a '+
       'nil T2: a complete return with the figures at zero.</p>';
  }else{
    h+='<p>This year had '+
       hits.join(', ').replace(/, ([^,]*)$/,' and $1')+
       ', so it is not a nil year and is reported as a full T2.</p>';
  }
  h+='<div class="ei-cmp">'+
     '<div class="ei-cmp-col'+(nil?' a':'')+'">'+
     '<div class="ei-cmp-hdr">Nil return</div>'+
     '<div class="ei-cmp-row"><span class="ei-cmp-l">When it applies</span>'+
     '<span class="ei-cmp-v">No business carried on, nothing earned, nothing paid out</span></div>'+
     '<div class="ei-cmp-row"><span class="ei-cmp-l">Schedules</span>'+
     '<span class="ei-cmp-v">GIFI 100, 125 and 141 where required, Schedule 24 on a first return, Schedule 50 at 10% or more</span></div>'+
     '<div class="ei-cmp-row"><span class="ei-cmp-l">Tax owing</span>'+
     '<span class="ei-cmp-v">$0.00</span></div>'+
     '<div class="ei-cmp-row"><span class="ei-cmp-l">Filed by</span>'+
     '<span class="ei-cmp-v">This service, at '+PRICE_JS+'</span></div></div>'+
     '<div class="ei-cmp-col'+(nil?'':' b')+'">'+
     '<div class="ei-cmp-hdr">Full return</div>'+
     '<div class="ei-cmp-row"><span class="ei-cmp-l">When it applies</span>'+
     '<span class="ei-cmp-v">Any revenue, expense, investment or rental income, dividend, or asset disposed of</span></div>'+
     '<div class="ei-cmp-row"><span class="ei-cmp-l">Schedules</span>'+
     '<span class="ei-cmp-v">The nil set plus whatever the activity requires, income and expense detail included</span></div>'+
     '<div class="ei-cmp-row"><span class="ei-cmp-l">Tax owing</span>'+
     '<span class="ei-cmp-v">Whatever the year produces</span></div>'+
     '<div class="ei-cmp-row"><span class="ei-cmp-l">Filed by</span>'+
     '<span class="ei-cmp-v">Gondaliya CPA Professional Corporation at gondaliyacpa.ca</span></div></div></div>';
  if(!nil){h+='<div class="ei-danger"><p>'+NOTNILJS+'</p></div>';}
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className=nil?'ei-out ok':'ei-out no';
  out.innerHTML=h;
}
IDS.forEach(function(k){
  Array.prototype.forEach.call(document.querySelectorAll('input[name="'+k+'"]'),
    function(e){e.addEventListener('change',render);});});
render();
"""

# ------------------------------------------ 19. nil T2 document checklist
L19 = r"""
// Two items are always needed. The rest are the schedules the live tools
// already encode: any one GIFI trigger pulls in 100, 125 and 141; a first
// return pulls in Schedule 24; a shareholder at 10% or more pulls in
// Schedule 50; a loss carried forward pulls in Schedule 8.
function docList(a){
  if(a.gifi===null||a.first===null||a.share10===null||a.losses===null){
    return null;}
  var o=['id','t183'];
  if(a.gifi==='y'){o.push('gifi');}
  if(a.first==='y'){o.push('s24');}
  if(a.share10==='y'){o.push('s50');}
  if(a.losses==='y'){o.push('s8');}
  return o;
}
"""
T19_JS = PICK + L19 + r"""
var out=document.getElementById('out');
var IDS=['gifi','first','share10','losses'];
var DOC={
 id:['Corporation identification','Name, Business Number and the fiscal year dates for the year being filed'],
 t183:['Form T183CORP','Signed by a signing officer on a secure single-use screen before the return is transmitted'],
 gifi:['GIFI Schedules 100, 125 and 141','Any one of share capital, cash, a shareholder loan, an incorporation cost or a bank charge makes all three required'],
 s24:['Schedule 24','Required on the first return after incorporation'],
 s50:['Schedule 50','Required for every shareholder at 10% or more'],
 s8:['Schedule 8 and loss continuity','Required where a loss is carried forward from an earlier year']
};
function render(){
  var a={};IDS.forEach(function(k){a[k]=pick(k);});
  var d=docList(a);
  if(d===null){out.className='ei-out';
    out.innerHTML='<p>Answer all four and the checklist appears here.</p>';return;}
  var h='<h3>'+d.length+' item'+(d.length===1?'':'s')+' in this return</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Item</th>'+
     '<th scope="col">Why</th></tr></thead><tbody>';
  d.forEach(function(k){
    h+='<tr><td>'+DOC[k][0]+'</td><td>'+DOC[k][1]+'</td></tr>';});
  h+='</tbody></table>';
  h+='<p>Every item above is included in '+PRICE_JS+
     '. No audited financial statements are needed for a nil year.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out ok';out.innerHTML=h;
}
IDS.forEach(function(k){
  Array.prototype.forEach.call(document.querySelectorAll('input[name="'+k+'"]'),
    function(e){e.addEventListener('change',render);});});
render();
"""

# ------------------------------- 20. due date weekend and holiday shift
L20 = r"""
// Names in the same order holidays() builds them.
var HNAME=['New Year&rsquo;s Day','Family Day','Good Friday','Victoria Day',
           'Canada Day','Labour Day','Thanksgiving','Christmas Day',
           'Boxing Day'];
function holidayName(dt){
  var hs=holidays(dt.getUTCFullYear());
  for(var i=0;i<hs.length;i++){
    if(hs[i].getTime()===dt.getTime()){return HNAME[i];}}
  return null;
}
function whyClosed(dt){
  var hn=holidayName(dt);
  if(hn){return hn;}
  var w=dt.getUTCDay();
  if(w===0||w===6){return DAY[w];}
  return null;
}
// Every non-business day from the date given up to, but not including, the
// day it lands on.
function shiftChain(dt){
  var out=[],d=new Date(dt.getTime());
  while(!isBusiness(d)){
    out.push({date:new Date(d.getTime()),why:whyClosed(d)});
    d=new Date(d.getTime()+86400000);
  }
  return out;
}
"""
T20_JS = DATE_JS + L20 + PARSE_JS + r"""
var out=document.getElementById('out');
function render(){
  var d=parse('d');
  if(d===null){out.className='ei-out';
    out.innerHTML='<p>Enter a due date and the shift appears here.</p>';return;}
  if(d===undefined){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';return;}
  var chain=shiftChain(d),eff=nextBusiness(d);
  var h;
  if(!chain.length){
    h='<h3>'+fmt(d)+' is a business day</h3>'+
      '<p>'+DAY[d.getUTCDay()]+', not a weekend and not a statutory holiday, '+
      'so a due date falling on it does not move.</p>';
    out.className='ei-out ok';
  }else{
    h='<h3>Moves to '+fmt(eff)+'</h3>';
    h+='<div class="ei-stats">'+
       '<div class="ei-stat"><span class="ei-stat-l">Date given</span>'+
       '<span class="ei-stat-v">'+fmt(d)+'</span></div>'+
       '<div class="ei-stat"><span class="ei-stat-l">Days skipped</span>'+
       '<span class="ei-stat-v">'+chain.length+'</span></div>'+
       '<div class="ei-stat"><span class="ei-stat-l">Effective date</span>'+
       '<span class="ei-stat-v">'+fmt(eff)+'</span></div></div>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Day skipped</th>'+
       '<th scope="col">Why</th></tr></thead><tbody>';
    chain.forEach(function(c){
      h+='<tr><td>'+fmt(c.date)+'</td><td>'+(c.why||'Not a business day')+
         '</td></tr>';});
    h+='<tr><td>'+fmt(eff)+'</td><td>'+DAY[eff.getUTCDay()]+
       ', the next business day</td></tr>';
    h+='</tbody></table>';
    out.className='ei-out no';
  }
  h+='<p>The nine days treated as statutory holidays here are New Year&rsquo;s '+
     'Day, Family Day, Good Friday, Victoria Day, Canada Day, Labour Day, '+
     'Thanksgiving, Christmas Day and Boxing Day.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.innerHTML=h;
}
document.getElementById('d').addEventListener('input',render);
render();
"""


TOOLS4 = [
 dict(slug='business-number-status-checker',
  title='Business Number Status Checker | Which Accounts Are Open',
  h1_pre='Business Number ', h1_span='Status Checker',
  h1='Business Number Status Checker',
  eyebrow='Account Check', keyword='business number status checker',
  meta=('Four questions that set out which of your Business Number accounts '
        'are open and what each one still needs beyond the nil T2.'),
  tags=['Four questions', 'One row per account',
        'Says what the fee does not cover', 'No sign-up to use it'],
  form=tool('Four questions about the corporation&rsquo;s accounts',
            [yn('bn', 'Do you know the corporation&rsquo;s nine-digit Business '
                      'Number'),
             yn('rc', 'Is there a corporation income tax account on record'),
             yn('rt', 'Is there a GST/HST account open'),
             yn('rp', 'Is there a payroll account open')],
            'Answer all four and the account picture appears here.'),
  js=None,
  sections=[
   ('why', 'One Business Number, Several Accounts Under It',
    '<p>A corporation has one nine-digit Business Number, and each kind of tax '
    'sits under it as its own programme account: corporation income tax, '
    'GST/HST, payroll. They are separate filings with separate deadlines, and '
    'closing one does nothing to the others.</p>\n'
    '<p>That is why a corporation can be dormant for years and still be '
    'behind on more than the T2. An account nobody remembers opening is still '
    'open until it is closed.</p>'),
   ('t2', 'What the T2 Needs',
    '<p>A T2 is transmitted against the corporation income tax account, so the '
    'Business Number has to be known before anything can be filed. It appears '
    'on any notice of assessment, in My Business Account, and on the '
    'corporation&rsquo;s registration documents.</p>\n'
    '<p>The fee of ' + PRICE + ' covers the nil T2. It does not cover a '
    'GST/HST return or a payroll remittance, which is what the rows above '
    'separate out.</p>'),
   ('close', 'Closing an Account You No Longer Need',
    '<p>Form RC145 closes a Business Number programme account, once that '
    'account has its own final return or remittance in. An account left open '
    'can still draw correspondence after the corporation itself is gone, '
    'which is the usual reason a closed-down corporation keeps hearing from '
    'the Canada Revenue Agency.</p>'),
  ],
  faq=[
   ('Can a T2 Be Filed Without the Business Number?',
    'No. The return is transmitted against the corporation income tax account '
    'under that number, so it has to be known first.'),
   ('Does Closing the GST/HST Account Close the T2 Obligation?',
    'No. Each programme account is separate. The T2 is due for every tax year '
    'until the corporation is formally dissolved, whatever happens to the '
    'other accounts.'),
   ('What If I Am Not Sure Whether an Account Is Open?',
    'My Business Account lists the programme accounts on record. Answer yes '
    'here only where you know, and treat the result as the list to confirm '
    'rather than a statement of your account.'),
   ('Is a Nil GST/HST Return Really Needed on a Dormant Corporation?',
    'An open account still has its own filing obligation, nil or not. The '
    + a(T + 'gst-hst-nil-filing-checker/', 'GST/HST nil filing checker')
    + ' covers that account on its own.'),
   ('Does the Fee Cover Any of the Other Accounts?',
    'No. ' + PRICE + ' covers one nil T2 for one corporation for one tax year. '
    'Every other account is a separate filing.'),
  ]),

 dict(slug='inactive-corporation-filing-checker',
  title='Inactive Corporation Filing Checker | What Else You Still Owe',
  h1_pre='Inactive Corporation ', h1_span='Filing Checker',
  h1='Inactive Corporation Filing Checker',
  eyebrow='Scope Check', keyword='inactive corporation filing checker',
  meta=('Four questions that list every filing an inactive corporation still '
        'owes beside the nil T2, and which of them the fee covers.'),
  tags=['What sits beside the T2', 'Who each filing goes to',
        'What the fee does not cover', 'Registry filings are separate'],
  form=tool('Four questions about how the corporation is registered',
            [yn('fed', 'Was it incorporated federally, through Corporations '
                       'Canada'),
             yn('ont', 'Is it registered in Ontario'),
             yn('gst', 'Is there a GST/HST account open'),
             yn('pay', 'Is there a payroll account open')],
            'Answer all four and the list of filings appears here.'),
  js=None,
  sections=[
   ('scope', 'The Nil T2 Is One Filing, Not All of Them',
    '<p>A nil T2 reports the corporation&rsquo;s tax year to the Canada '
    'Revenue Agency. It is not the only thing an inactive corporation owes, '
    'and the fee covers the T2 alone.</p>\n'
    '<p>A nil T2 does not cover an Ontario annual return through the Ontario '
    'Business Registry, a federal Corporations Canada annual return at $12.00 '
    'due within 60 days of the anniversary, an Alberta AT1, a Quebec CO-17, or '
    'a nil GST/HST or payroll filing. We tell you which of these you still '
    'owe.</p>'),
   ('who', 'Two Different Bodies',
    '<p>Registry filings and tax returns go to different places. The annual '
    'return goes to the registry the corporation was incorporated or '
    'registered with, federally through Corporations Canada or provincially. '
    'The T2 and the programme account returns go to the Canada Revenue '
    'Agency.</p>\n'
    '<p>Missing the registry one is what eventually dissolves a corporation '
    'without its owner intending it, which is a separate problem from an '
    'unfiled T2.</p>'),
   ('fee', 'What the Fee Covers',
    '<p>' + PRICE + ' covers one nil T2 for one corporation for one tax year, '
    'including the T2 Short where the corporation qualifies, the GIFI '
    'schedules where they are required, your Form T183CORP package, CPA '
    'review, electronic transmission by a registered EFILE electronic filer, '
    'and your CRA confirmation emailed within 3 business days.</p>\n'
    '<div class="ei-warn"><p>The $12.00 federal annual return fee is a '
    'government fee and tax does not apply to it. It is paid to Corporations '
    'Canada, not to us.</p></div>'),
  ],
  faq=[
   ('Is the Annual Return the Same as the T2?',
    'No. They go to different bodies and have different deadlines. The annual '
    'return keeps the corporation on the registry; the T2 reports its tax '
    'year to the Canada Revenue Agency.'),
   ('Do You File the Ontario Annual Return?',
    'No. It is filed separately through the Ontario Business Registry and is '
    'not covered by the fee. We tell you that you owe it.'),
   ('What About an Alberta AT1 or a Quebec CO-17?',
    'Both are separate provincial returns and neither is included in the fee '
    'for the nil T2.'),
   ('The Corporation Has Been Inactive for Years. Does All of This Apply to Every Year?',
    'The T2 does: one return per tax year until dissolution. Use the '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' to list the years. The other filings follow their own cycles.'),
   ('Is It Cheaper to Just Dissolve the Corporation?',
    'Dissolving does not remove the returns already outstanding. The '
    + a(T + 'dissolution-readiness-checker/', 'dissolution readiness checker')
    + ' sets out the order the steps run in.'),
  ]),

 dict(slug='nil-return-vs-full-return-checker',
  title='Nil Return vs Full Return Checker | Which One Applies',
  h1_pre='Nil Return vs ', h1_span='Full Return Checker',
  h1='Nil Return vs Full Return Checker',
  eyebrow='Compare Tool', keyword='nil return vs full return checker',
  meta=('Four questions that say whether the year is a nil T2 or a full T2, '
        'side by side, and name what pushed it over.'),
  tags=['Side-by-side comparison', 'Names what pushed it over',
        'Four questions', 'Routes a full return'],
  form=tool('Four questions about what happened in the tax year',
            [yn('rev', 'Was there any revenue or any expense'),
             yn('inv', 'Was there any investment income or rental income'),
             yn('div', 'Was a dividend paid or received'),
             yn('disp', 'Was any asset sold or transferred')],
            'Answer all four and the answer appears here.'),
  js=None,
  sections=[
   ('line', 'Where the Line Sits',
    '<p>A nil return and a full return are the same form. What differs is '
    'whether anything happened in the tax year. One revenue entry, one '
    'expense, one dividend or one disposal and the year is a full return, '
    'however small the amount.</p>\n'
    '<p>Existing is not activity. A corporation can hold a bank account, own '
    'assets and stay registered for years without carrying on business, and '
    'every one of those years is nil.</p>'),
   ('diff', 'What Changes When It Is Not Nil',
    '<p>The schedules grow with the activity, the figures stop being zero, and '
    'the work is no longer a fixed-fee filing. That is why a full return is '
    'handled by Gondaliya CPA Professional Corporation at gondaliyacpa.ca '
    'rather than here.</p>\n'
    '<div class="ei-danger"><p>' + NOT_NIL + '</p></div>'),
   ('depth', 'This Tool and the Dormant Test',
    '<p>This one compares the two kinds of return and names which applies. '
    'The ' + a(T + 'dormant-corporation-test/', 'dormant corporation test')
    + ' asks ten activity questions and names the single item that '
    'disqualifies a year, which is the finer instrument of the two. Use this '
    'to understand the difference, that one to settle a close case.</p>'),
  ],
  faq=[
   ('Is a Nil Return a Shorter Form?',
    'No. It is a complete T2 with the figures at zero. The identification, '
    'the fiscal year dates and the GIFI schedules where they are required are '
    'all still part of it.'),
   ('Does One Small Expense Really Make It a Full Return?',
    'Yes. There is no threshold below which activity is ignored. A single '
    'bank charge paid from the corporate account is activity.'),
   ('What If Different Years Are Different?',
    'Each tax year is judged on its own. A corporation can file nil for three '
    'years, full for one, and nil again after it.'),
   ('Is the T2 Short the Same as a Nil Return?',
    'No. The T2 Short is a shorter version of the form that some corporations '
    'qualify to use. The '
    + a(T + 't2-short-eligibility-checker/', 'T2 Short eligibility checker')
    + ' runs all eight conditions.'),
   ('What Happens If We File Nil and It Turns Out Not to Be?',
    'We check before you pay. If we find it afterwards, we refund you in full '
    'and the work moves to gondaliyacpa.ca.'),
  ]),

 dict(slug='nil-t2-document-checklist-checker',
  title='Nil T2 Document Checklist | What Goes Into the Return',
  h1_pre='Nil T2 ', h1_span='Document Checklist',
  h1='Nil T2 Document Checklist Checker',
  eyebrow='Checklist Tool', keyword='nil t2 document checklist',
  meta=('Four questions that build the list of what actually goes into your '
        'nil T2, schedule by schedule, all of it inside the fee.'),
  tags=['Built from four answers', 'Schedule by schedule',
        'No audited statements', 'Everything inside the fee'],
  form=tool('Four questions about the return',
            [yn('gifi', 'Is there any share capital, cash, shareholder loan, '
                        'incorporation cost or bank charge'),
             yn('first', 'Is this the first return after incorporation'),
             yn('share10', 'Is any shareholder at 10% or more'),
             yn('losses', 'Is a loss being carried forward from an earlier '
                          'year')],
            'Answer all four and the checklist appears here.'),
  js=None,
  sections=[
   ('always', 'Two Things Are Always Needed',
    '<p>Every nil T2 needs the corporation identified, which is its name, its '
    'Business Number and the fiscal year dates for the year being filed, and '
    'it needs Form T183CORP signed before the return is transmitted.</p>\n'
    '<p>Everything else on the list depends on what the corporation holds and '
    'whether this is its first return.</p>'),
   ('gifiwhy', 'Why GIFI Turns Up on a Nil Return',
    '<p>The most misunderstood part of a nil return is that it still carries '
    'GIFI schedules. Any one of share capital, cash, a shareholder loan, an '
    'incorporation cost or a bank charge makes Schedules 100, 125 and 141 all '
    'required, and a corporation with shares issued has share capital.</p>\n'
    '<p>The ' + a(T + 'gifi-schedule-requirement-checker/', 'GIFI schedule '
    'requirement checker') + ' runs those five triggers one by one.</p>'),
   ('not', 'What You Do Not Need',
    '<p>No audited financial statements. No bookkeeping for a year with no '
    'transactions. No appointment. The whole return is built from the answers '
    'on the form and the schedules the corporation&rsquo;s own position '
    'requires, and all of it is inside ' + PRICE + '.</p>'),
  ],
  faq=[
   ('Do I Need Financial Statements?',
    'No audited statements. The return still carries the GIFI schedules where '
    'they are required, showing zero, which is a different thing from a set '
    'of prepared statements.'),
   ('What Is Form T183CORP?',
    'It is the form by which a signing officer authorises the electronic '
    'transmission of the return. It is signed on a secure single-use screen '
    'before we transmit, and it is included in the fee.'),
   ('Does a First Return Need Anything Extra?',
    'Schedule 24 is required on the first return after incorporation. The '
    + a(T + 'schedule-24-first-return-checker/', 'Schedule 24 first return '
    'checker') + ' confirms it.'),
   ('How Is the 10% Shareholder Threshold Measured?',
    'Schedule 50 is needed for any shareholder at 10% or more. The '
    + a(T + 'schedule-50-shareholder-threshold-checker/', 'Schedule 50 '
    'shareholder threshold checker') + ' takes the percentages and says which '
    'shareholders are in.'),
   ('Is Anything on the List Charged Separately?',
    'No. ' + PRICE + ' covers every schedule the return requires, the '
    'T183CORP package, CPA review and transmission.'),
  ]),

 dict(slug='due-date-weekend-holiday-shift-calculator',
  title='Due Date Weekend and Holiday Shift Calculator',
  h1_pre='Due Date Weekend and ', h1_span='Holiday Shift Calculator',
  h1='Due Date Weekend and Holiday Shift Calculator',
  eyebrow='Date Tool', keyword='due date weekend holiday shift calculator',
  meta=('Enter a due date and the calculator says whether it moves, which '
        'weekend day or statutory holiday moved it, and the date it lands on.'),
  tags=['Names the holiday', 'Shows every day skipped',
        'Nine statutory holidays', 'Works on any date'],
  form=tool('Your due date',
            [date('d', 'The date a filing falls due')],
            'Enter a due date and the shift appears here.'),
  js=None,
  sections=[
   ('rule', 'A Due Date on a Closed Day Moves Forward',
    '<p>Where a filing date falls on a Saturday, a Sunday or a statutory '
    'holiday, it is met on the next business day. The calculator shows every '
    'day skipped and names what closed it, which matters most around Christmas '
    'and Boxing Day, where two holidays and a weekend can sit together.</p>'),
   ('which', 'The Nine Days Treated as Holidays Here',
    '<table class="ei-tbl"><thead><tr><th scope="col">Holiday</th>'
    '<th scope="col">When it falls</th></tr></thead><tbody>\n'
    '<tr><td>New Year&rsquo;s Day</td><td>January 1</td></tr>\n'
    '<tr><td>Family Day</td><td>Third Monday in February</td></tr>\n'
    '<tr><td>Good Friday</td><td>Two days before Easter Sunday</td></tr>\n'
    '<tr><td>Victoria Day</td><td>Monday on or before May 24</td></tr>\n'
    '<tr><td>Canada Day</td><td>July 1</td></tr>\n'
    '<tr><td>Labour Day</td><td>First Monday in September</td></tr>\n'
    '<tr><td>Thanksgiving</td><td>Second Monday in October</td></tr>\n'
    '<tr><td>Christmas Day</td><td>December 25</td></tr>\n'
    '<tr><td>Boxing Day</td><td>December 26</td></tr>\n'
    '</tbody></table>\n'
    '<p>These are the Ontario statutory holidays the deadline calculator '
    'already applies, so both tools agree about any date you put into '
    'them.</p>'),
   ('use', 'Where This Date Comes From',
    '<p>A T2 is due within six months of the fiscal year-end, and that is the '
    'date to put in here. The '
    + a(T + 'nil-t2-deadline-calculator/', 'nil T2 deadline calculator')
    + ' works it out from a year-end and applies the shift itself, and the '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' lists it for every outstanding year at once.</p>\n'
    '<p>A nil T2 is ' + PRICE + '.</p>'),
  ],
  faq=[
   ('Does the Shift Ever Move a Date Backwards?',
    'No. A date on a closed day is met on the next business day, never an '
    'earlier one.'),
   ('What Happens When Christmas Falls on a Friday?',
    'December 25 closes the Friday, December 26 and the weekend follow, and '
    'the date lands on the Monday. Put the date in and the tool lists each day '
    'it skipped.'),
   ('Are These Federal or Provincial Holidays?',
    'They are the Ontario statutory holidays, which is what this firm files '
    'against. A corporation elsewhere may see a different local list, and the '
    'date the Canada Revenue Agency accepts is the one that matters.'),
   ('Does the Shift Change How Many Days Late a Return Is?',
    'It changes the date the return was due, so it changes the count from it. '
    'For a non-resident-owned corporation that count carries a charge, which '
    'the ' + a(T + 'non-resident-t2-penalty-calculator/', 'non-resident T2 '
    'penalty calculator') + ' works out.'),
   ('Does Filing Early Ever Hurt?',
    'No. The shift only matters at the end of the window. A nil return can be '
    'transmitted as soon as the tax year has ended.'),
  ]),
]

for t, js in zip(TOOLS4, [T16_JS, T17_JS, T18_JS, T19_JS, T20_JS]):
    t['js'] = PRELUDE + js

ORDER4 = ORDER3 + [t['slug'] for t in TOOLS4]
LINK_TITLE4 = dict(LINK_TITLE3, **{
 'business-number-status-checker': 'Business Number status checker',
 'inactive-corporation-filing-checker':
     'Inactive corporation filing checker, what else you owe',
 'nil-return-vs-full-return-checker': 'Nil return vs full return checker',
 'nil-t2-document-checklist-checker': 'Nil T2 document checklist',
 'due-date-weekend-holiday-shift-calculator':
     'Due date weekend and holiday shift calculator',
})

SIBLINGS4 = {15: [16, 9, 11], 16: [15, 9, 8], 17: [8, 11, 18],
             18: [2, 4, 6], 19: [0, 12, 13]}

GUIDES4 = {
 'business-number-status-checker': [
   ('how-to-file-a-nil-t2-return', 'How to file a nil T2 return')],
 'inactive-corporation-filing-checker': [
   ('provincial-and-federal-annual-returns',
    'Provincial and federal annual returns'),
   ('dormant-and-inactive-corporations',
    'The complete guide to dormant and inactive corporations')],
 'nil-return-vs-full-return-checker': [
   ('nil-t2-return-complete-guide', 'The complete guide to the nil T2 return')],
 'nil-t2-document-checklist-checker': [
   ('t2-schedules-on-a-nil-return', 'T2 schedules on a nil return'),
   ('gifi-schedules-100-125-141', 'GIFI Schedules 100, 125 and 141')],
 'due-date-weekend-holiday-shift-calculator': [
   ('t2-late-filing-penalties', 'T2 late filing penalties')],
}

# Same guard build_f2c added: a section anchor sharing an id with a form field
# is silently wrong, because getElementById returns whichever comes first.
for t in TOOLS4:
    import re as _re
    _sec = {sid for sid, _, _ in t['sections']}
    _fld = set(_re.findall(r'id="([\w-]+)"', t['form']))
    _fld |= set(_re.findall(r'name="([\w-]+)"', t['form']))
    _clash = _sec & _fld
    assert not _clash, ('%s: section anchor collides with a form id: %s'
                        % (t['slug'], sorted(_clash)))

for t in TOOLS4:
    i = ORDER4.index(t['slug'])
    rel = [(T + ORDER4[j] + '/', LINK_TITLE4[ORDER4[j]]) for j in SIBLINGS4[i]]
    rel += [(G + g + '/', ttl) for g, ttl in GUIDES4[t['slug']]]
    rel.append((COST, 'Nil T2 filing cost'))
    t['related'] = rel


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'October 26, 2026', '2026-10-26'
    recs = []
    for t in TOOLS4:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html, **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2d-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-44s %6d bytes' % (r['slug'], len(r['content'].encode())))
