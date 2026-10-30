# -*- coding: utf-8 -*-
"""Family 2 batch 8: tools 51 to 60.

ALL TEN COME FROM APPENDIX A, WHICH CORRECTS WHAT BATCH 7 SAID

build_f2g.py's docstring states that Appendix A "cannot supply ten more
distinct F2 tools". That was too sweeping and this batch is the proof: all ten
slugs below are Appendix A entries, and every fact each one asserts is quoted
from the signed plan. What was true of batch 7 is narrower than what I wrote:
the GROUPS I had been drawing from were exhausted, not the appendix.

The appendix holds 150 F2 slugs. Thirty of the fifty pages now live are
appendix entries; twenty are slugs I chose. This batch takes ten appendix
entries, so Family 2 stands at forty of the plan's hundred and fifty after it.

THE SOURCE FOR EACH TOOL, BY PLAN LINE

  "must file a T2 within six months of its fiscal year-end, every year, until
  it is formally dissolved. A final T2 is due ..."        (plan 165, 1166, 1586)
      -> tool 51. The requirement, and the three things visitors believe
         exempt them from it.

  "A corporation inactive all year with nothing to report may omit GIFI
  Schedules 100, 125 and 141, but any share capital, cash, shareholder loan,
  incorporation cost or bank charge makes them required."  (plan 1827, 2081, 2151)
      The plan states this rule three times, in three sections, in almost the
      same words. It is the best-attested fact in the whole document.
      -> tools 52, 53, 54, 55. Four pages, one rule, four different questions:
         which schedules in total, the share capital trigger, the shareholder
         loan trigger, and what actually lands on the income statement.

  "Schedule 50 for every shareholder at 10% or more"       (plan 177, 1869)
  "Schedule 24 on a first return", "Schedule 8, loss continuity"  (plan 177)
      -> tool 52, which is the only page on the site that puts the whole
         schedule set behind one set of answers.

  "$12.00 due within 60 days of your anniversary", "$12.00 is a government fee
  and HST does not apply to it"                      (plan 181, 396, 1869, 2125)
      -> tools 58, 59, 60.

  Hard rule 8, and NOT_NIL: a corporation that paid or received a dividend is
  not nil, and goes to gondaliyacpa.ca at $350.00 plus HST per year
      -> tool 53.

  "Form RC145. An inactive T2 does not close those accounts."    (plan 2149)
      -> tool 57.

WHAT I REFUSED, AND WHY, SO THE NEXT BATCH DOES NOT RE-DRAFT THEM

Eleven appendix slugs were drafted and dropped on reading the plan rather than
on taste. They are listed here because the refusal is the reusable part.

  gifi-code-lookup-checker
      A lookup needs the GIFI code numbers. The plan names the schedules and
      never a code. Nothing to look up without inventing the table.

  small-supplier-threshold-calculator, gst-hst-registration-requirement-checker
      Both turn on a dollar threshold the plan never states. The plan says
      what this site may say about GST/HST: that an open account still needs
      nil filings and that Form RC145 closes it. That is all.

  t2-late-filing-penalty-calculator, repeated-failure-to-file-penalty-calculator
  cra-arrears-interest-calculator, instalment-interest-calculator
  annual-return-late-fee-calculator, demand-to-file-penalty-calculator
      Percentages, per-day rates and interest rates. Refused in batch 6 for
      the same reason and still refused: the plan gives exactly two such
      figures, the $25.00 per day up to $2,500.00 for a non-resident-owned
      corporation and the $12.00 federal annual return fee, and both are
      already on live pages.

  subsection-15-2-exposure-checker, shareholder-loan-income-inclusion-calculator
  shareholder-loan-prescribed-interest-calculator
      Statutory periods and prescribed rates. The plan's shareholder loan
      facts are about REPORTING: a loan balance makes the GIFI schedules
      required. Tool 54 answers that and says in terms that the tax treatment
      of a loan is not what it decides.

  permanent-establishment-checker, carrying-on-business-in-canada-checker
      Both need a definition the plan does not carry. Tool 47 already asks the
      only permanent-establishment question this site can answer, which is
      whether there is one in Quebec or Alberta.

  corporate-revival-requirement-checker
      The plan covers being struck (tool 40 is live on it) and says nothing
      about revival.

THE OVERLAPS I ACCEPTED, AND HOW EACH PAGE HANDLES ITS NEIGHBOUR

Tool 57 sits beside two live tools on the same subject: tool 48 orders the
CLOSING of CRA accounts and tool 49 dates a year's obligations. Tool 57 lists
what is still owed while the corporation stays open. Like tool 50, it carries
a table naming which of the three answers which question, because a visitor
who lands on the wrong one of the three should be able to see that in one
glance rather than by reading all three.

Tool 55 and tool 25 (nil-gifi-balance-sheet-checker, live) both run on the
five triggers. Tool 25 is about the balance sheet, Schedule 100. Tool 55 is
about the income statement, Schedule 125, where the useful fact is different:
a single bank charge puts a figure on a schedule people assume stays blank.
"""
import io, json, os, sys, re as _re

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_f2 import (render, meta, yn, a, SITE, HUB, FORM, PRICE,
                      NOT_NIL, TOOL_DISCLAIMER)
from build_f2b import tool, num, date, PICK, T, G, COST
from build_f2c import MONEY_JS, QUAL, PRELUDE
from build_f2f import BASE, RBASE, _GUIDES_LIVE
from build_f2g import ORDER7, LINK_TITLE7

# build_f2f's list predates the three guides that completed Family 9 on
# October 29. All thirty are live, so the link assertions below use this set.
GUIDES_LIVE8 = set(_GUIDES_LIVE) | {
    'cra-accounts-on-a-dormant-corporation',
    'choosing-and-changing-a-fiscal-year-end',
    'quebec-co17-and-alberta-at1',
}

# The five triggers, in the plan's own order, used by four tools in this
# batch. Kept as one list so the four pages cannot drift apart on it.
TRIGGERS = ['share capital', 'cash', 'a shareholder loan',
            'an incorporation cost', 'a bank charge']
assert len(TRIGGERS) == 5


# ------------------------------------------------------ 51. filing required
T51_JS = RBASE + r"""
function fileRequired(ex,di,ac){
  if(ex===null||di===null||ac===null){return null;}
  return {ex:ex==='y',di:di==='y',ac:ac==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=fileRequired(pick('ex'),pick('di'),pick('ac'));
  if(r===null){out.innerHTML='<p>Answer all three questions.</p>';return;}
  var h;
  if(!r.ex){
    h='<h3>No T2 is owed for a year the corporation did not exist in</h3>';
    h+='<p>A tax year belongs to a corporation. Where there was no '
     +'corporation for any part of the year, there is no tax year and no '
     +'return. A year before incorporation is not an unfiled year.</p>';
    h+='<p>The years from incorporation onward are a different question, and '
     +'each of them is owed whether or not anything happened in it.</p>';
    h+='<p>'+DISC_JS+'</p>';
    out.innerHTML=h;return;
  }
  h='<h3>A T2 is owed for this year'+(r.di?', and it is the final one':'')
   +'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Your answer</th><th scope="col">What it changes</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>The corporation existed for part or all of the year</td>'
   +'<td>Yes</td><td>A return is owed for the period it existed</td></tr>';
  h+='<tr><td>It was dissolved part-way through the year</td><td>'
   +(r.di?'Yes':'No')+'</td><td>'+(r.di?'The period ends on the dissolution '
   +'date and the return for it is the final T2':'The return covers the full '
   +'fiscal year')+'</td></tr>';
  h+='<tr><td>It had income, an expense or any activity</td><td>'
   +(r.ac?'Yes':'No')+'</td><td>'+(r.ac?'The figures on the return are not '
   +'all zero, so the year may not be nil':'The figures are zero. The return '
   +'is still owed')+'</td></tr>';
  h+='</tbody></table>';
  h+='<p>A corporation must file a T2 within six months of its fiscal '
   +'year-end, every year, until it is formally dissolved. Having nothing to '
   +'report changes what the return says, never whether it is owed.</p>';
  if(!r.ac){
    h+='<p>A year with no activity is what a nil return is for. The figures '
     +'are zero and the return is '+PRICE_JS+'.</p>';
  }else{
    h+='<p>A year with activity may still be nil, and may not. '+NOTNILJS
     +'</p>';
  }
  if(r.di){
    h+='<p>Dissolution does not retire the obligation, it ends it. The final '
     +'period runs to the dissolution date and its return closes the record. '
     +'A corporation dissolved with years outstanding leaves those years '
     +'open behind it.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="ex"],input[name="di"],'
    +'input[name="ac"]'),
  function(el){el.addEventListener('change',show);});
"""

# ----------------------------------------------------- 52. which schedules
T52_JS = RBASE + r"""
function schedules(fr,sc,ca,ln,ex,s5,d8){
  if(fr===null||sc===null||ca===null||ln===null||ex===null||s5===null
     ||d8===null){return null;}
  var trig=[];
  if(sc==='y'){trig.push('share capital');}
  if(ca==='y'){trig.push('cash or a bank account');}
  if(ln==='y'){trig.push('a shareholder loan balance');}
  if(ex==='y'){trig.push('an incorporation cost or a bank charge');}
  var rows=[];
  rows.push(['GIFI Schedules 100, 125 and 141',trig.length?'Required':'May be omitted',
    trig.length?'On the books: '+trig.join(', ')
    :'Inactive all year with nothing to report']);
  rows.push(['Schedule 24',fr==='y'?'Required':'Not this year',
    fr==='y'?'It is the first return':'Schedule 24 goes on a first return']);
  rows.push(['Schedule 50',s5==='y'?'Required':'Not required',
    s5==='y'?'A shareholder holds 10 percent or more'
    :'No shareholder at 10 percent or more']);
  rows.push(['Schedule 8 and loss continuity',
    d8==='y'?'Required':'Not required',
    d8==='y'?'Depreciable property or a loss carried forward'
    :'Neither depreciable property nor a carried loss']);
  var n=0;
  for(var i=0;i<rows.length;i++){if(rows[i][1]==='Required'){n++;}}
  return {rows:rows,n:n,trig:trig,omit:trig.length===0};
}
var out=document.getElementById('out');
function show(){
  var r=schedules(pick('fr'),pick('sc'),pick('ca'),pick('ln'),pick('ex'),
                  pick('s5'),pick('d8'));
  if(r===null){out.innerHTML='<p>Answer all seven questions.</p>';return;}
  var h='<h3>'+(r.n?plural(r.n,'schedule group')+' on the return'
    :'No schedule is triggered by these answers')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Schedule</th>'
   +'<th scope="col">On this return</th><th scope="col">Why</th></tr>'
   +'</thead><tbody>';
  for(var i=0;i<r.rows.length;i++){
    h+='<tr><td>'+r.rows[i][0]+'</td><td>'+r.rows[i][1]+'</td><td>'
     +r.rows[i][2]+'</td></tr>';
  }
  h+='</tbody></table>';
  if(r.omit){
    h+='<p>A corporation inactive all year with nothing to report may omit '
     +'GIFI Schedules 100, 125 and 141. That is a narrow permission and the '
     +'five things that withdraw it are share capital, cash, a shareholder '
     +'loan, an incorporation cost and a bank charge. None of them is here on '
     +'these answers.</p>';
    h+='<p>Worth re-reading the cash question before relying on it. A '
     +'corporation with an open bank account held cash at some point in the '
     +'year even where the balance is now zero.</p>';
  }else{
    h+='<p>Any one of share capital, cash, a shareholder loan, an '
     +'incorporation cost or a bank charge makes GIFI Schedules 100, 125 and '
     +'141 required, and the corporation having had no activity does not '
     +'change that. One item on the books is enough.</p>';
  }
  h+='<p>Every schedule named here is inside the fee of '+PRICE_JS
   +'. The fee covers the return the corporation actually needs rather than a '
   +'stripped version of it.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="fr"],input[name="sc"],'
    +'input[name="ca"],input[name="ln"],input[name="ex"],'
    +'input[name="s5"],input[name="d8"]'),
  function(el){el.addEventListener('change',show);});
"""


# --------------------------------------------------------- 53. share capital
T53_JS = RBASE + r"""
function shareCapital(sc,s5,dv){
  if(sc===null||s5===null||dv===null){return null;}
  return {sc:sc==='y',s5:s5==='y',dv:dv==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=shareCapital(pick('sc'),pick('s5'),pick('dv'));
  if(r===null){out.innerHTML='<p>Answer all three questions.</p>';return;}
  var h='<h3>'+(r.dv?'A dividend means the year is not nil'
    :(r.sc?'Share capital makes the GIFI schedules required'
      :'No share capital reported'))+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Fact</th>'
   +'<th scope="col">Your answer</th><th scope="col">What it triggers</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Shares have been issued</td><td>'+(r.sc?'Yes':'No')+'</td><td>'
   +(r.sc?'GIFI Schedules 100, 125 and 141 are required'
     :'Nothing on its own')+'</td></tr>';
  h+='<tr><td>A shareholder holds 10 percent or more</td><td>'
   +(r.s5?'Yes':'No')+'</td><td>'
   +(r.s5?'Schedule 50 for every such shareholder'
     :'No Schedule 50 on these answers')+'</td></tr>';
  h+='<tr><td>A dividend was paid or received</td><td>'+(r.dv?'Yes':'No')
   +'</td><td>'+(r.dv?'The year is not nil':'Nil status is not affected')
   +'</td></tr>';
  h+='</tbody></table>';
  if(r.sc){
    h+='<p>Share capital is the first of the five things that withdraw the '
     +'permission to omit GIFI Schedules 100, 125 and 141. A corporation '
     +'inactive all year with nothing to report may omit them; one that '
     +'issued shares has something to report whether or not it traded.</p>';
    h+='<p>This catches almost every corporation, which is the point worth '
     +'taking away. Shares are issued at incorporation, so a corporation that '
     +'has never done anything else still has share capital on its books.</p>';
  }else{
    h+='<p>A corporation with no shares issued is unusual. Before relying on '
     +'that answer, check the incorporation documents rather than memory: '
     +'shares are normally issued at incorporation, and share capital is one '
     +'of the five things that make the GIFI schedules required.</p>';
  }
  if(r.s5){
    h+='<p>Schedule 50 is tied to any shareholder at 10 percent or more, and '
     +'it names every one of them rather than the largest. A corporation with '
     +'one shareholder holding all the shares files it for that person.</p>';
  }
  if(r.dv){
    h+='<div class="ei-warn"><p>'+NOTNILJS+'</p></div>';
  }else{
    h+='<p>Having share capital does not stop a year being nil. Share capital '
     +'sits on the balance sheet and says nothing about whether the year had '
     +'income. A nil year with shares issued is the ordinary case, and it is '
     +PRICE_JS+'.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="sc"],input[name="s5"],'
    +'input[name="dv"]'),
  function(el){el.addEventListener('change',show);});
"""

# ------------------------------------------------------ 54. shareholder loan
T54_JS = RBASE + r"""
function loanBalance(bal,mv,ot){
  if(bal===null||mv===null||ot===null){return null;}
  return {bal:bal==='y',mv:mv==='y',ot:ot==='y',
          req:bal==='y'||ot==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=loanBalance(pick('bal'),pick('mv'),pick('ot'));
  if(r===null){out.innerHTML='<p>Answer all three questions.</p>';return;}
  var h='<h3>'+(r.req?'GIFI Schedules 100, 125 and 141 are required'
    :'Nothing here makes the GIFI schedules required')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Your answer</th><th scope="col">What it means</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>A balance is owing between the corporation and a shareholder</td>'
   +'<td>'+(r.bal?'Yes':'No')+'</td><td>'
   +(r.bal?'A shareholder loan balance. The GIFI schedules are required'
     :'No loan balance on these answers')+'</td></tr>';
  h+='<tr><td>Money moved either way during the year</td><td>'
   +(r.mv?'Yes':'No')+'</td><td>'+(r.mv?'Movement is reported, and does not '
   +'change the answer above':'A balance carried without movement still '
   +'counts')+'</td></tr>';
  h+='<tr><td>Share capital, cash or a cost is also on the books</td><td>'
   +(r.ot?'Yes':'No')+'</td><td>'+(r.ot?'Required on that ground as well'
     :'Nothing further')+'</td></tr>';
  h+='</tbody></table>';
  if(r.bal&&!r.mv){
    h+='<p>This is the case people get wrong. A loan balance that sat still '
     +'all year is a balance on the books, and the permission to omit the '
     +'GIFI schedules belongs to a corporation inactive all year with nothing '
     +'to report. A balance is something to report.</p>';
  }
  h+='<p>The direction does not matter here. A balance the corporation owes '
   +'its shareholder and a balance the shareholder owes the corporation are '
   +'both a shareholder loan for this purpose, and either one makes the GIFI '
   +'schedules required.</p>';
  h+='<div class="ei-info"><p>What this page answers is a reporting '
   +'question: whether the schedules go on the return. The tax treatment of a '
   +'shareholder loan is a different matter, it depends on facts a web page '
   +'does not have, and it is not what a nil filing decides. Where a loan '
   +'raises that question, it belongs with Gondaliya CPA Professional '
   +'Corporation at gondaliyacpa.ca rather than here.</p></div>';
  h+='<p>A loan balance does not stop a year being nil. It is a balance '
   +'sheet item, not income, so a dormant corporation carrying one is the '
   +'ordinary case at '+PRICE_JS+'.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="bal"],input[name="mv"],'
    +'input[name="ot"]'),
  function(el){el.addEventListener('change',show);});
"""


# --------------------------------------------------------- 55. Schedule 125
T55_JS = RBASE + r"""
function incomeStatement(rev,bank,bs){
  if(rev===null||bank===null||bs===null){return null;}
  var figs=[];
  if(rev==='y'){figs.push('revenue');}
  if(bank==='y'){figs.push('a bank charge or another expense');}
  return {rev:rev==='y',bank:bank==='y',bs:bs==='y',figs:figs,
          req:rev==='y'||bank==='y'||bs==='y',
          blank:figs.length===0};
}
var out=document.getElementById('out');
function show(){
  var r=incomeStatement(pick('rev'),pick('bank'),pick('bs'));
  if(r===null){out.innerHTML='<p>Answer all three questions.</p>';return;}
  var h='<h3>'+(r.req?'Schedule 125 goes on the return'
    :'Schedule 125 may be omitted')
   +(r.req&&r.blank?', carrying zeros':'')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Your answer</th><th scope="col">Effect on Schedule 125</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>The corporation had revenue</td><td>'+(r.rev?'Yes':'No')
   +'</td><td>'+(r.rev?'A figure on the revenue side'
     :'The revenue side is zero')+'</td></tr>';
  h+='<tr><td>There was a bank charge or any other expense</td><td>'
   +(r.bank?'Yes':'No')+'</td><td>'+(r.bank?'A figure on the expense side'
     :'The expense side is zero')+'</td></tr>';
  h+='<tr><td>Share capital, cash or a shareholder loan is on the books</td>'
   +'<td>'+(r.bs?'Yes':'No')+'</td><td>'+(r.bs?'The schedule is required even '
   +'with no revenue and no expense':'Nothing on its own')+'</td></tr>';
  h+='</tbody></table>';
  if(r.figs.length){
    h+='<p>The income statement carries '+r.figs.join(' and ')+'. That is '
     +'what Schedule 125 is, so it is not a blank schedule on this return '
     +'whatever the corporation was doing.</p>';
  }
  if(r.bank&&!r.rev){
    h+='<p>A bank charge with no revenue is the fact pattern this page exists '
     +'for. It is a few dollars, and it is an expense, so the income '
     +'statement has a figure on it and the year has something to report. A '
     +'corporation with an open bank account usually has one.</p>';
  }
  if(r.req&&r.blank){
    h+='<p>With no revenue and no expense the schedule carries zeros rather '
     +'than being left out. It is required because something sits on the '
     +'balance sheet, and GIFI Schedules 100, 125 and 141 stand or fall '
     +'together: the permission to omit is for all three or none.</p>';
  }
  if(!r.req){
    h+='<p>A corporation inactive all year with nothing to report may omit '
     +'GIFI Schedules 100, 125 and 141. On these answers nothing withdraws '
     +'that permission. Check the cash question once more before relying on '
     +'it, because an account that was open held cash even where the balance '
     +'reads zero now.</p>';
  }
  h+='<p>Whichever way it falls, the schedule is inside the fee of '+PRICE_JS
   +'. '+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="rev"],input[name="bank"],'
    +'input[name="bs"]'),
  function(el){el.addEventListener('change',show);});
"""

# --------------------------------------------------------- 56. Schedule 141
T56_JS = RBASE + r"""
function notesChecklist(ou,asu,tr){
  if(ou===null||asu===null||tr===null){return null;}
  return {ou:ou==='y',asu:asu==='y',tr:tr==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=notesChecklist(pick('ou'),pick('asu'),pick('tr'));
  if(r===null){out.innerHTML='<p>Answer all three questions.</p>';return;}
  var h='<h3>'+(r.tr?'Schedule 141 goes on the return'
    :'Schedule 141 may be omitted')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Your answer</th><th scope="col">What it settles</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Share capital, cash, a shareholder loan or a cost is on the '
   +'books</td><td>'+(r.tr?'Yes':'No')+'</td><td>'
   +(r.tr?'All three GIFI schedules are required'
     :'The permission to omit all three is intact')+'</td></tr>';
  h+='<tr><td>The financial statements were prepared by someone outside the '
   +'corporation</td><td>'+(r.ou?'Yes':'No')+'</td><td>'
   +(r.ou?'An outside preparer':'Prepared within the corporation')
   +'</td></tr>';
  h+='<tr><td>They were audited or reviewed</td><td>'+(r.asu?'Yes':'No')
   +'</td><td>'+(r.asu?'An assurance engagement was performed'
     :'Neither audited nor reviewed, which is the normal position on a '
     +'dormant corporation')+'</td></tr>';
  h+='</tbody></table>';
  h+='<p>Schedule 141 is the notes checklist. Where the other two GIFI '
   +'schedules carry the figures, this one records who put the statements '
   +'together and what level of work stands behind them.</p>';
  if(!r.asu){
    h+='<p>Neither audited nor reviewed is the ordinary answer for a dormant '
     +'corporation, and it is a complete answer rather than a gap. A nil '
     +'return does not need an assurance engagement behind it.</p>';
  }
  if(r.tr){
    h+='<p>The schedule is required here because something is on the books. '
     +'The three GIFI schedules travel together: a corporation inactive all '
     +'year with nothing to report may omit all three, and any one of share '
     +'capital, cash, a shareholder loan, an incorporation cost or a bank '
     +'charge makes all three required.</p>';
  }
  h+='<p>Preparing the statements and the schedule that describes them is '
   +'inside the fee of '+PRICE_JS+'. Returns are prepared and transmitted in '
   +'Canada by Gondaliya CPA Professional Corporation, a registered EFILE '
   +'electronic filer, so the preparer question has the same answer on every '
   +'return filed here.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="ou"],input[name="asu"],'
    +'input[name="tr"]'),
  function(el){el.addEventListener('change',show);});
"""


# ------------------------------------------------- 57. dormant obligations
T57_JS = RBASE + r"""
function dormantOwes(fed,pay,gst){
  if(fed===null||pay===null||gst===null){return null;}
  var rows=[];
  rows.push(['A T2 return, every year until formal dissolution',
    'The Canada Revenue Agency','Inside the fee']);
  if(fed==='y'){
    rows.push(['The federal annual return, within 60 days of the '
      +'incorporation anniversary','Corporations Canada',
      'Outside the fee, a $12.00 government fee']);
  }else{
    rows.push(['A registry annual return','The registry the corporation is '
      +'incorporated with','Outside the fee']);
  }
  if(pay==='y'){
    rows.push(['T4 information returns and nil remittances',
      'The Canada Revenue Agency','Outside the fee, until the account is '
      +'closed with Form RC145']);
  }
  if(gst==='y'){
    rows.push(['GST/HST returns, including nil ones',
      'The Canada Revenue Agency','Outside the fee, until the account is '
      +'closed with Form RC145']);
  }
  return {rows:rows,fed:fed==='y',accts:(pay==='y'?1:0)+(gst==='y'?1:0)};
}
var out=document.getElementById('out');
function show(){
  var r=dormantOwes(pick('fed'),pick('pay'),pick('gst'));
  if(r===null){out.innerHTML='<p>Answer all three questions.</p>';return;}
  var h='<h3>'+plural(r.rows.length,'obligation')+' while the corporation '
   +'stays open</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">What is owed</th>'
   +'<th scope="col">To whom</th><th scope="col">Covered by the fee</th>'
   +'</tr></thead><tbody>';
  for(var i=0;i<r.rows.length;i++){
    h+='<tr><td>'+r.rows[i][0]+'</td><td>'+r.rows[i][1]+'</td><td>'
     +r.rows[i][2]+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>Doing nothing is not one of the rows. A corporation must file a T2 '
   +'within six months of its fiscal year-end, every year, until it is '
   +'formally dissolved, and the registry filing runs on its own date '
   +'alongside it.</p>';
  if(r.accts){
    h+='<p>The '+(r.accts===2?'two accounts':'account')+' above '
     +(r.accts===2?'are':'is')+' the part people forget, because '
     +(r.accts===2?'they keep':'it keeps')+' generating returns with no '
     +'activity behind them. An inactive T2 does not close '
     +(r.accts===2?'them':'it')+'. Form RC145 does.</p>';
  }else{
    h+='<p>With no payroll and no GST/HST account open, the list is as short '
     +'as it gets for a corporation that is still on the register.</p>';
  }
  h+='<p>Each nil T2 is '+PRICE_JS+'. The registry annual return is a '
   +'separate filing to a separate body and is not covered by it.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="fed"],input[name="pay"],'
    +'input[name="gst"]'),
  function(el){el.addEventListener('change',show);});
"""

# ------------------------------------------- 58. annual return vs tax return
T58_JS = RBASE + r"""
function cmpCol(cls,hdr,rows){
  var h='<div class="ei-cmp-col '+cls+'"><div class="ei-cmp-hdr">'+hdr
   +'</div>';
  for(var i=0;i<rows.length;i++){
    h+='<div class="ei-cmp-row"><span class="ei-cmp-l">'+rows[i][0]
     +'</span><span class="ei-cmp-v">'+rows[i][1]+'</span></div>';
  }
  return h+'</div>';
}
function twoReturns(fed,prov){
  if(fed===null||prov===null){return null;}
  // The T2, plus the home registry's annual return, which every corporation
  // owes wherever it was incorporated, plus one more where it is registered
  // outside that jurisdiction. The floor is two, never one.
  return {fed:fed==='y',prov:prov==='y',n:2+(prov==='y'?1:0)};
}
var out=document.getElementById('out');
function show(){
  var r=twoReturns(pick('fed'),pick('prov'));
  if(r===null){out.innerHTML='<p>Answer both questions.</p>';return;}
  var h='<h3>'+plural(r.n,'separate filing')+', to different bodies</h3>';
  var reg=[];
  reg.push(['What it is','A registry filing confirming the directors and the '
    +'registered office']);
  reg.push(['What it reports','No income and no tax']);
  if(r.fed){
    reg.push(['When','Within 60 days of the incorporation anniversary']);
    reg.push(['Cost','$12.00, a government fee to which HST does not apply']);
  }else{
    reg.push(['When','On the registry&#8217;s own schedule']);
    reg.push(['Cost','Set by the registry']);
  }
  reg.push(['Missing it','The corporation can be struck from the register']);
  reg.push(['Covered by the fee','No']);
  h+='<div class="ei-cmp">'
   +cmpCol('a','The T2, a tax return',
     [['What it is','A corporate income tax return filed with the Canada '
       +'Revenue Agency'],
      ['What it reports','The year&#8217;s figures, which on a nil year are '
       +'zero'],
      ['When','Within six months of the fiscal year-end'],
      ['Cost','Nil T2 filing, '+PRICE_JS],
      ['Missing it','The tax year stays open, invites a demand to file and '
       +'blocks a clearance certificate'],
      ['Covered by the fee','Yes']])
   +cmpCol('b',r.fed?'The federal annual return, a registry filing'
     :'The registry annual return',reg)
   +'</div>';
  h+='<p>They are unrelated obligations that happen to share the word '
   +'return. One reports money to the tax authority and one confirms who the '
   +'directors are to the registry that holds the corporation on its '
   +'register.</p>';
  h+='<p>Filing either does nothing for the other. A corporation up to date '
   +'on its annual returns can have years of unfiled T2 returns behind it, '
   +'and a corporation with every T2 filed can still be struck for missing '
   +'the registry filing.</p>';
  if(r.prov){
    h+='<p>Registering outside the jurisdiction the corporation was '
     +'incorporated in adds a filing rather than replacing one. Where it sits '
     +'on two registers it answers to both, and neither of them is the Canada '
     +'Revenue Agency.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="fed"],input[name="prov"]'),
  function(el){el.addEventListener('change',show);});
"""


# -------------------------------------------------- 59. dissolve or keep on
T59_JS = RBASE + MONEY_JS + r"""
function cmpCol(cls,hdr,rows){
  var h='<div class="ei-cmp-col '+cls+'"><div class="ei-cmp-hdr">'+hdr
   +'</div>';
  for(var i=0;i<rows.length;i++){
    h+='<div class="ei-cmp-row"><span class="ei-cmp-l">'+rows[i][0]
     +'</span><span class="ei-cmp-v">'+rows[i][1]+'</span></div>';
  }
  return h+'</div>';
}
function routes(n,fed,beh){
  if(n===null||fed===null||beh===null){return null;}
  if(!(n>=1)||n>20){return {err:'n'};}
  var behind=beh==='y'?1:0;
  return {n:n,fed:fed==='y',behind:beh==='y',
          t2:n*30000,fee:fed==='y'?n*1200:0};
}
var out=document.getElementById('out');
function show(){
  var v=document.getElementById('n').value;
  var r=routes(v===''?null:parseInt(v,10),pick('fed'),pick('beh'));
  if(r===null){out.innerHTML='<p>Enter the number of years and answer both '
    +'questions.</p>';return;}
  if(r.err==='n'){out.innerHTML='<p>Enter a number of years between 1 and '
    +'20.</p>';return;}
  var keep=[];
  keep.push([plural(r.n,'nil T2 return'),money(r.t2)+' plus HST']);
  if(r.fed){
    keep.push([plural(r.n,'federal annual return'),
      money(r.fee)+', a government fee with no HST']);
  }else{
    keep.push([plural(r.n,'registry annual return'),
      'A government fee set by the registry']);
  }
  keep.push(['What it leaves','A corporation still on the register, and the '
    +'same decision again in '+plural(r.n,'year')]);
  var wind=[];
  wind.push(['The final T2 for the period ending at dissolution',
    money(30000)+' plus HST']);
  wind.push(['A clearance certificate request','Outside the fee']);
  wind.push(['The registry articles of dissolution','Outside the fee']);
  wind.push(['What it leaves','No corporation, and no filing owed again']);
  var h='<h3>'+plural(r.n,'year')+' of filing is '+money(r.t2)+' plus HST'
   +(r.fed?' and '+money(r.fee)+' in annual return fees':'')+'</h3>';
  h+='<div class="ei-cmp">'
   +cmpCol('a','Keep filing for '+plural(r.n,'year'),keep)
   +cmpCol('b','Wind it up now',wind)+'</div>';
  h+='<p>One side of that table totals and the other does not, which is the '
   +'honest shape of the comparison. The returns are priced here. A clearance '
   +'request and the registry dissolution are not covered by this fee, so '
   +'this page gives you the filing cost of staying open and names what the '
   +'other route adds rather than putting a figure on it.</p>';
  if(r.behind){
    h+='<p>With years already outstanding, the choice is narrower than it '
     +'looks. Both routes start by filing them: dissolving a corporation that '
     +'still owes returns leaves those tax years open behind it, and a '
     +'clearance request rests on a complete filing record.</p>';
    h+='<div class="ei-warn"><p>'+QUALJS+'</p></div>';
  }
  h+='<p>Keeping a corporation that does nothing is a decision to pay for a '
   +'return every year for as long as it exists. That is reasonable where '
   +'there is a reason to hold the name or the history, and it is worth '
   +'seeing as a recurring cost rather than a formality.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var e=document.getElementById('n');
if(e){e.addEventListener('change',show);e.addEventListener('input',show);}
Array.prototype.forEach.call(
  document.querySelectorAll('input[name="fed"],input[name="beh"]'),
  function(el){el.addEventListener('change',show);});
"""

# ------------------------------------------- 60. federal annual return fees
T60_JS = BASE + MONEY_JS + r"""
function feeSchedule(inc,n){
  if(inc===null||n===null){return null;}
  if(inc===undefined){return {err:'read'};}
  if(!(n>=1)||n>20){return {err:'n'};}
  var rows=[],first=inc.getUTCFullYear()+1;
  for(var k=0;k<n;k++){
    var ann=addYear(inc,k+1);
    rows.push({ann:ann,due:new Date(ann.getTime()+60*86400000)});
  }
  return {rows:rows,n:n,inc:inc,total:n*1200,first:first};
}
var out=document.getElementById('out');
function show(){
  var v=document.getElementById('n').value;
  var r=feeSchedule(parse('inc'),v===''?null:parseInt(v,10));
  if(r===null){out.innerHTML='<p>Enter the incorporation date and how many '
    +'years to list.</p>';return;}
  if(r.err==='read'){out.innerHTML='<p>That date could not be read.</p>';
    return;}
  if(r.err==='n'){out.innerHTML='<p>Enter a number of years between 1 and '
    +'20.</p>';return;}
  var h='<h3>'+money(r.total)+' over '+plural(r.n,'year')+', with no HST on '
   +'any of it</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Year</th>'
   +'<th scope="col">Incorporation anniversary</th>'
   +'<th scope="col">Annual return due by</th><th scope="col">Fee</th></tr>'
   +'</thead><tbody>';
  for(var i=0;i<r.rows.length;i++){
    h+='<tr><td>'+(i+1)+'</td><td>'+fmt(r.rows[i].ann)+'</td><td>'
     +fmt(r.rows[i].due)+'</td><td>'+money(1200)+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>The federal annual return is due within 60 days of the '
   +'incorporation anniversary, and the fee is '+money(1200)+'. It is a '
   +'government fee and HST does not apply to it, which is why the total '
   +'above carries no tax line.</p>';
  h+='<p>Note that these dates run from the anniversary rather than from the '
   +'fiscal year-end, so they do not move when a year-end moves. A '
   +'corporation can have its T2 date in one month and its annual return date '
   +'in another, every year, and both are correct.</p>';
  h+='<p>This filing is not covered by the nil T2 fee of '+PRICE_JS+'. The '
   +'two are separate filings to separate bodies: one reports the '
   +'year&#8217;s figures to the Canada Revenue Agency and one confirms the '
   +'directors and the registered office to Corporations Canada.</p>';
  h+='<p>Missing it does not create an unfiled tax year. It puts the '
   +'corporation at risk of being struck from the register, which is a '
   +'different consequence with a different cure.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
['inc','n'].forEach(function(id){
  var el=document.getElementById(id);
  if(el){el.addEventListener('change',show);el.addEventListener('input',show);}
});
"""


TOOLS8 = [
 dict(slug='t2-filing-requirement-checker',
  title='T2 Filing Requirement Checker | Is a Return Owed at All',
  h1_pre='T2 Filing ', h1_span='Requirement Checker',
  h1='T2 Filing Requirement Checker',
  eyebrow='The Requirement', keyword='t2 filing requirement checker',
  meta=('A corporation files a T2 every year until it is formally dissolved. '
        'Three answers show whether a return is owed for this year.'),
  tags=['Three answers', 'Covers a dissolution year',
        'No activity is not an exemption', 'Says when nothing is owed'],
  form=tool('This tax year',
            [yn('ex', 'Did the corporation exist for any part of this tax '
                      'year?'),
             yn('di', 'Was it dissolved part-way through the year?'),
             yn('ac', 'Did it have any income, expense or activity?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('the-rule', 'The Rule Has No Activity Test In It',
    '<p>A corporation must file a T2 within six months of its fiscal '
    'year-end, every year, until it is formally dissolved. There is no '
    'threshold in that sentence and no exemption for a quiet year.</p>\n'
    '<p>Which is why the question people ask, whether they have to file, '
    'nearly always has the same answer. The useful question is the one '
    'underneath it: what the return says when there is nothing to report. '
    'That is what a nil return is, and it is '
    + PRICE + '.</p>'),
   ('what-does-not-exempt', 'What People Think Exempts Them',
    '<p>Three beliefs account for most unfiled years, and none of them is '
    'right. No income, no bank account and never having started trading are '
    'all descriptions of a nil year rather than reasons there is no year.</p>\n'
    '<p>The fourth is subtler and more costly: that a corporation nobody has '
    'touched for years has somehow lapsed. It has not. An unfiled year stays '
    'open, and the '
    + a(T + 'unfiled-years-checker/', 'unfiled years checker')
    + ' lists the ones outstanding.</p>'),
   ('when-nothing-is-owed', 'The One Case Where Nothing Is Owed',
    '<p>A year before incorporation is not an unfiled year. A tax year '
    'belongs to a corporation, so where there was no corporation there is no '
    'year and nothing to file.</p>\n'
    '<p>That sounds obvious written down and it is worth stating, because a '
    'visitor counting backwards through years of silence often counts past '
    'the incorporation date. The years to file start there, not at the point '
    'the business stopped being active.</p>'),
   ('the-final-year', 'A Dissolution Year Is Still a Year',
    '<p>Where a corporation is dissolved part-way through a year, the period '
    'runs to the dissolution date and a return is owed for it. That return is '
    'the final T2 and it closes the record rather than being waived because '
    'the corporation has gone.</p>\n'
    '<p>Dissolving with years outstanding leaves those years open behind it. '
    'The '
    + a(T + 'final-t2-return-due-date-calculator/',
        'final T2 return due date calculator')
    + ' dates that last return, and the '
    + a(T + 'dissolution-readiness-checker/',
        'dissolution readiness checker')
    + ' tests whether the corporation is ready for the step.</p>'),
  ],
  faq=[
   ('Does a corporation with no activity have to file a T2?',
    'Yes. A corporation must file a T2 within six months of its fiscal '
    'year-end, every year, until it is formally dissolved. Having nothing to '
    'report changes what the return says, not whether it is owed.'),
   ('Does having no bank account exempt a corporation?',
    'No. There is no activity test and no asset test in the filing '
    'requirement. A corporation with no bank account files a nil return.'),
   ('What if the corporation never started trading?',
    'It still files. A corporation that was incorporated and then left alone '
    'owes a return for every year since incorporation.'),
   ('Do I owe a return for years before incorporation?',
    'No. A tax year belongs to a corporation, so a year before the '
    'corporation existed is not an unfiled year.'),
   ('Is a return owed for the year a corporation is dissolved?',
    'Yes. The period runs to the dissolution date and the return for it is '
    'the final T2.'),
  ]),

 dict(slug='required-schedules-checker',
  title='Required Schedules Checker | Which Schedules a Nil T2 Carries',
  h1_pre='Required ', h1_span='Schedules Checker',
  h1='Required Schedules Checker',
  eyebrow='Schedules', keyword='required schedules checker',
  meta=('Seven answers give the whole schedule set a nil return carries: the '
        'GIFI schedules, Schedule 24, Schedule 50, Schedule 8.'),
  tags=['Seven answers, the whole set', 'The five GIFI triggers',
        'Schedule 50 at 10 percent', 'All of it inside the fee'],
  form=tool('What is on the books',
            [yn('fr', 'Is this the corporation&#8217;s first T2 return?'),
             yn('sc', 'Has share capital been issued?'),
             yn('ca', 'Did it hold cash or a bank account at any time?'),
             yn('ln', 'Is there a shareholder loan balance, either '
                      'direction?'),
             yn('ex', 'Was there an incorporation cost or a bank charge?'),
             yn('s5', 'Does any shareholder hold 10 percent or more?'),
             yn('d8', 'Is there depreciable property or a loss carried '
                      'forward?')],
            'Answer all seven questions.'),
  js=None,
  sections=[
   ('one-page', 'The Whole Set Behind One Set of Answers',
    '<p>Other tools here each test one schedule. This one asks what is on the '
    'books and returns the whole set, which is the order the question '
    'actually arrives in: nobody wonders about Schedule 50 in isolation.</p>\n'
    '<p>Where you want one schedule in depth, the '
    + a(T + 'gifi-schedule-requirement-checker/',
        'GIFI schedule requirement checker')
    + ', the '
    + a(T + 'schedule-50-shareholder-threshold-checker/',
        'Schedule 50 shareholder threshold checker')
    + ' and the '
    + a(T + 'schedule-8-cca-requirement-checker/',
        'Schedule 8 CCA requirement checker')
    + ' each go further than this page does.</p>'),
   ('the-five', 'Five Things Withdraw the GIFI Permission',
    '<p>A corporation inactive all year with nothing to report may omit GIFI '
    'Schedules 100, 125 and 141. Any share capital, cash, shareholder loan, '
    'incorporation cost or bank charge makes them required.</p>\n'
    '<p>Five items, and one of them is enough. The permission is narrower '
    'than it first reads, because a corporation that was incorporated has '
    'share capital and a corporation with a bank account has held cash, which '
    'between them covers nearly every corporation that exists.</p>'),
   ('all-three-together', 'The Three GIFI Schedules Travel Together',
    '<p>Schedules 100, 125 and 141 are the balance sheet, the income '
    'statement and the notes checklist. The permission to omit covers all '
    'three or none of them, so there is no position in which one goes on the '
    'return and the others stay off.</p>\n'
    '<p>That is why a single bank charge matters out of proportion to its '
    'size. It is an item to report, so all three schedules are required, and '
    'two of them then carry mostly zeros.</p>'),
   ('inside-the-fee', 'Every Schedule Here Is Inside the Fee',
    '<p>The fee of $300.00 plus HST per tax year covers the return the '
    'corporation actually needs: the T2 Short where it qualifies, GIFI '
    'Schedules 100, 125 and 141 where they are required, Schedule 24 on a '
    'first return, Schedule 50 for every shareholder at 10 percent or more, '
    'Schedule 8 and loss continuity.</p>\n'
    '<p>So the answer this page gives has no price attached to it. A return '
    'with every schedule required costs what a return with none of them '
    'costs, which is worth knowing before you worry about the count.</p>'),
  ],
  faq=[
   ('Which schedules does a nil T2 return need?',
    'It depends on what is on the books. GIFI Schedules 100, 125 and 141 '
    'where any of five items is present, Schedule 24 on a first return, '
    'Schedule 50 for any shareholder at 10 percent or more, and Schedule 8 '
    'with loss continuity where there is depreciable property or a carried '
    'loss.'),
   ('Can a nil return omit the GIFI schedules?',
    'Only where none of five items is on the books. Any share capital, cash, '
    'shareholder loan, incorporation cost or bank charge makes GIFI Schedules '
    '100, 125 and 141 required; the permission to omit them belongs to a '
    'corporation inactive all year with nothing to report.'),
   ('When is Schedule 50 required?',
    'Schedule 50 is tied to any shareholder at 10 percent or more, and it '
    'names every shareholder who meets that test.'),
   ('When does Schedule 24 go on a return?',
    'On a first return, and only on that one. A corporation filing for the '
    'first time carries it whether or not the first year had any activity.'),
   ('Do more schedules cost more?',
    'No. The fee of $300.00 plus HST per tax year covers the schedules the '
    'return requires, however many that turns out to be.'),
  ]),
]


TOOLS8 += [
 dict(slug='share-capital-reporting-checker',
  title='Share Capital Reporting Checker | GIFI and Schedule 50',
  h1_pre='Share Capital ', h1_span='Reporting Checker',
  h1='Share Capital Reporting Checker',
  eyebrow='Share Capital', keyword='share capital reporting checker',
  meta=('Share capital makes the GIFI schedules required even with no '
        'activity. Three answers show what the shares on your books '
        'trigger.'),
  tags=['Issued at incorporation', 'Makes GIFI required',
        'Schedule 50 at 10 percent', 'Does not stop a year being nil'],
  form=tool('The shares',
            [yn('sc', 'Has the corporation issued any shares?'),
             yn('s5', 'Does any shareholder hold 10 percent or more?'),
             yn('dv', 'Was a dividend paid or received in the year?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('first-of-five', 'Share Capital Is the First of the Five Triggers',
    '<p>A corporation inactive all year with nothing to report may omit GIFI '
    'Schedules 100, 125 and 141. Share capital is the first of the five '
    'things that withdraw that permission, alongside cash, a shareholder '
    'loan, an incorporation cost and a bank charge.</p>\n'
    '<p>It is also the one that catches the most corporations, for a reason '
    'that has nothing to do with trading: shares are issued at '
    'incorporation. A corporation that has never done anything since still '
    'has share capital on its books.</p>'),
   ('not-the-same-as-nil', 'Share Capital Does Not Stop a Year Being Nil',
    '<p>These are two different questions and they get run together. Share '
    'capital sits on the balance sheet. Whether a year is nil is a question '
    'about the income statement, and shares issued years ago say nothing '
    'about whether this year had income.</p>\n'
    '<p>A dormant corporation with shares issued and no activity is the '
    'ordinary nil case, not an exception to it. What it means is that the '
    'return carries the GIFI schedules with the share capital on them, and '
    'the figures for the year are zero.</p>'),
   ('ten-percent', 'Schedule 50 Runs Off a Threshold, Not Off Control',
    '<p>Schedule 50 is tied to any shareholder at 10 percent or more. It is '
    'not a schedule about the controlling shareholder, and it does not list '
    'the largest one: it names every shareholder who meets the test.</p>\n'
    '<p>A corporation with one shareholder holding everything files it for '
    'that person. A corporation with twelve shareholders at 8 percent each '
    'files none. The '
    + a(T + 'schedule-50-shareholder-threshold-checker/',
        'Schedule 50 shareholder threshold checker')
    + ' works through the threshold properly.</p>'),
   ('a-dividend-changes-the-answer', 'A Dividend Takes the Year Out of Nil',
    '<p>Paying or receiving a dividend is activity. A corporation that did '
    'either is not filing a nil return for that year, whatever else was '
    'quiet about it.</p>\n'
    '<p>That is a boundary of this service rather than a complication within '
    'it. Such a year goes to Gondaliya CPA Professional Corporation at '
    'gondaliyacpa.ca at $350.00 plus HST per year, and the '
    + a(T + 'nil-return-vs-full-return-checker/',
        'nil return versus full return checker')
    + ' is where that line is drawn in full.</p>'),
  ],
  faq=[
   ('Does share capital make the GIFI schedules required?',
    'Yes. Any share capital, cash, shareholder loan, incorporation cost or '
    'bank charge makes GIFI Schedules 100, 125 and 141 required, even where '
    'the corporation had no activity.'),
   ('My corporation has never traded. Does it have share capital?',
    'Almost certainly. Shares are normally issued at incorporation, so a '
    'corporation that has done nothing since still has share capital on its '
    'books. Check the incorporation documents rather than memory.'),
   ('Does share capital mean the year is not nil?',
    'No. Share capital is a balance sheet item. Whether a year is nil turns '
    'on the income statement, so a dormant corporation with shares issued '
    'files an ordinary nil return.'),
   ('Who goes on Schedule 50?',
    'Every shareholder at 10 percent or more, not only the largest or the one '
    'with control.'),
   ('What if a dividend was paid?',
    'Then the year is not nil. A corporation that paid or received a dividend '
    'is handled by Gondaliya CPA Professional Corporation at gondaliyacpa.ca '
    'at $350.00 plus HST per year.'),
  ]),

 dict(slug='shareholder-loan-balance-checker',
  title='Shareholder Loan Balance Checker | What It Means for a Nil Return',
  h1_pre='Shareholder Loan ', h1_span='Balance Checker',
  h1='Shareholder Loan Balance Checker',
  eyebrow='Shareholder Loan', keyword='shareholder loan balance checker',
  meta=('A shareholder loan balance makes the GIFI schedules required even '
        'with no activity. Three answers show what yours triggers.'),
  tags=['Either direction counts', 'A still balance counts',
        'Does not stop a year being nil', 'Reporting, not tax treatment'],
  form=tool('The balance',
            [yn('bal', 'Is a balance owing between the corporation and a '
                       'shareholder?'),
             yn('mv', 'Did money move either way during the year?'),
             yn('ot', 'Is share capital, cash or a cost also on the books?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('a-balance-is-something', 'A Balance Sitting Still Is Still Something',
    '<p>A corporation inactive all year with nothing to report may omit GIFI '
    'Schedules 100, 125 and 141. A shareholder loan is one of the five things '
    'that make them required, and nothing in that turns on whether the '
    'balance moved.</p>\n'
    '<p>So a loan that has sat unchanged for six years is reportable in the '
    'seventh. The corporation has something to report, which is the test, and '
    'a dormant year does not empty the balance sheet.</p>'),
   ('either-direction', 'Either Direction Is a Shareholder Loan Here',
    '<p>Money the corporation owes its shareholder and money the shareholder '
    'owes the corporation are both a shareholder loan balance for this '
    'purpose. Bookkeeping distinguishes them and the reporting trigger does '
    'not.</p>\n'
    '<p>Which settles the question people arrive with. Whether the balance is '
    'a due-to or a due-from, the answer about the GIFI schedules is the '
    'same.</p>'),
   ('not-the-nil-question', 'A Loan Does Not Stop a Year Being Nil',
    '<p>A loan balance is a balance sheet item, not income. A dormant '
    'corporation carrying one files an ordinary nil return at '
    + PRICE + ', with the GIFI schedules on it.</p>\n'
    '<p>The thing to separate is the balance from the movement. A balance is '
    'reported. Money moving in a year is activity, and activity is where the '
    'question of whether the year is nil starts to need a real answer.</p>'),
   ('what-this-does-not-answer', 'What This Page Deliberately Does Not Say',
    '<p>It answers a reporting question: whether the schedules go on the '
    'return. It says nothing about how a shareholder loan is taxed, what '
    'happens if it is outstanding too long, or what interest it should '
    'carry.</p>\n'
    '<p>Those turn on facts a web page does not have, and getting them wrong '
    'is expensive. Where a loan raises them it belongs with Gondaliya CPA '
    'Professional Corporation at gondaliyacpa.ca rather than with a nil '
    'filing, which is a return rather than advice.</p>'),
  ],
  faq=[
   ('Does a shareholder loan make the GIFI schedules required?',
    'Yes. A shareholder loan is one of the five things that make GIFI '
    'Schedules 100, 125 and 141 required, even where the corporation had no '
    'activity.'),
   ('What if the balance did not change all year?',
    'It still counts. The permission to omit the schedules belongs to a '
    'corporation inactive all year with nothing to report, and a balance is '
    'something to report.'),
   ('Does the direction of the loan matter?',
    'Not for this. A balance the corporation owes its shareholder and one the '
    'shareholder owes the corporation are both a shareholder loan balance '
    'here.'),
   ('Does a shareholder loan stop the year being nil?',
    'No. It is a balance sheet item rather than income, so a dormant '
    'corporation carrying one files an ordinary nil return.'),
   ('How is a shareholder loan taxed?',
    'That is outside what this page answers and outside a nil filing. It '
    'turns on facts a web page does not have, and it belongs with Gondaliya '
    'CPA Professional Corporation at gondaliyacpa.ca.'),
  ]),
]


TOOLS8 += [
 dict(slug='gifi-schedule-125-checker',
  title='GIFI Schedule 125 Checker | The Income Statement on a Nil Year',
  h1_pre='GIFI Schedule ', h1_span='125 Checker',
  h1='GIFI Schedule 125 Checker',
  eyebrow='Schedule 125', keyword='gifi schedule 125 checker',
  meta=('Schedule 125 is the income statement. Three answers show whether it '
        'goes on a nil return and whether it carries a figure.'),
  tags=['The income statement', 'A bank charge is an expense',
        'All three or none', 'Zeros are an answer'],
  form=tool('The year&#8217;s figures',
            [yn('rev', 'Did the corporation have any revenue?'),
             yn('bank', 'Was there a bank charge or any other expense?'),
             yn('bs', 'Is share capital, cash or a shareholder loan on the '
                      'books?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('what-125-is', 'Schedule 125 Is the Income Statement',
    '<p>Of the three GIFI schedules, 100 is the balance sheet, 125 is the '
    'income statement and 141 is the notes checklist. Schedule 125 is the one '
    'that reports what the year did rather than what the corporation '
    'holds.</p>\n'
    '<p>Which is why people expect it to be the blank one on a dormant year. '
    'Often it very nearly is, and nearly blank is not the same as absent. The '
    + a(T + 'nil-gifi-balance-sheet-checker/',
        'nil GIFI balance sheet checker')
    + ' covers the other side, Schedule 100.</p>'),
   ('the-bank-charge', 'A Bank Charge Is an Expense',
    '<p>This is the fact worth carrying away. A corporation with no revenue, '
    'no staff and no customers still has an income statement with a figure on '
    'it if the bank took a monthly fee off the account.</p>\n'
    '<p>It is a few dollars and it is an expense, so the year has something '
    'to report. A corporation with an open bank account usually has one of '
    'these, which is how a year that feels like nothing turns out to have a '
    'number in it.</p>'),
   ('all-three-or-none', 'The Permission Covers All Three or None',
    '<p>The permission runs to the three schedules together, which is the '
    'part that decides this page. There is no position where Schedule 100 '
    'goes on the return and Schedule 125 stays off, so an item on the balance '
    'sheet puts the income statement on the return too, carrying zeros.</p>\n'
    '<p>What withdraws the permission is any share capital, cash, '
    'shareholder loan, incorporation cost or bank charge. What holds it open '
    'is a corporation inactive all year with nothing to report, and share '
    'capital alone is enough to take it away.</p>'),
   ('zeros-are-an-answer', 'Zeros on a Required Schedule Are Not a Problem',
    '<p>A Schedule 125 of zeros is a complete schedule rather than an '
    'incomplete one. It reports that the year had no revenue and no expense, '
    'which is a fact about the year and the thing a nil return exists to '
    'say.</p>\n'
    '<p>A nil return is not an empty return. It is a full return whose '
    'figures are zero, which is why it carries the schedules the corporation '
    'needs and why all of them are inside the fee of '
    + PRICE + '.</p>'),
  ],
  faq=[
   ('What is GIFI Schedule 125?',
    'The income statement. Schedule 100 is the balance sheet, Schedule 125 is '
    'the income statement and Schedule 141 is the notes checklist.'),
   ('Can a nil return leave Schedule 125 off?',
    'Only where the corporation was inactive all year with nothing to report. '
    'Any share capital, cash, shareholder loan, incorporation cost or bank '
    'charge makes Schedules 100, 125 and 141 required.'),
   ('Does a bank charge count?',
    'Yes. A bank charge is an expense, so it puts a figure on the income '
    'statement and it is one of the five things that make the GIFI schedules '
    'required.'),
   ('Can Schedule 100 be filed without Schedule 125?',
    'No. The permission to omit covers all three GIFI schedules together, so '
    'they go on the return as a set.'),
   ('Is a schedule of zeros acceptable?',
    'Yes. A nil return is a full return whose figures are zero, and a '
    'Schedule 125 of zeros reports that the year had no revenue and no '
    'expense.'),
  ]),

 dict(slug='gifi-schedule-141-checker',
  title='GIFI Schedule 141 Checker | The Notes Checklist on a Nil Return',
  h1_pre='GIFI Schedule ', h1_span='141 Checker',
  h1='GIFI Schedule 141 Checker',
  eyebrow='Schedule 141', keyword='gifi schedule 141 checker',
  meta=('Schedule 141 records who prepared the statements and what work '
        'stands behind them. Three answers show what yours says.'),
  tags=['The notes checklist', 'Who prepared the statements',
        'Audited, reviewed or neither', 'Neither is a complete answer'],
  form=tool('The statements',
            [yn('tr', 'Is share capital, cash, a shareholder loan or a cost '
                      'on the books?'),
             yn('ou', 'Were the statements prepared by someone outside the '
                      'corporation?'),
             yn('asu', 'Were they audited or reviewed?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('what-141-is', 'Schedule 141 Describes the Statements, Not the Figures',
    '<p>Schedules 100 and 125 carry the numbers. Schedule 141 is the notes '
    'checklist: it records who put the financial statements together and what '
    'level of work stands behind them.</p>\n'
    '<p>So it is the one schedule in the set that is about the preparation '
    'rather than the corporation. The '
    + a(G + 'gifi-schedules-100-125-141/',
        'guide to GIFI Schedules 100, 125 and 141')
    + ' sets out what each of the three carries.</p>'),
   ('neither-is-fine', 'Neither Audited Nor Reviewed Is the Normal Answer',
    '<p>For a dormant corporation the honest answer to the assurance question '
    'is usually neither, and that is a complete answer rather than a gap in '
    'the return.</p>\n'
    '<p>A nil return does not need an audit or a review behind it. Reading '
    'the schedule as though it were asking for one is what makes people think '
    'a quiet corporation needs an engagement it does not need.</p>'),
   ('when-it-is-required', 'It Is Required on the Same Trigger as the Other '
    'Two',
    '<p>Schedule 141 has no test of its own. It goes on the return whenever '
    'Schedules 100 and 125 do, and it comes off only when they do, so the '
    'question is never about this schedule in particular.</p>\n'
    '<p>That shared trigger is any share capital, cash, shareholder loan, '
    'incorporation cost or bank charge, against a permission that belongs to '
    'a corporation inactive all year with nothing to report. In practice the '
    'schedule is nearly always required, because a corporation with shares '
    'issued has share capital.</p>'),
   ('who-prepares-them-here', 'On a Return Filed Here, the Preparer Question '
    'Has One Answer',
    '<p>Returns are prepared and transmitted in Canada by Gondaliya CPA '
    'Professional Corporation, a registered EFILE electronic filer. '
    'Credentials are never shared and never used offshore.</p>\n'
    '<p>So the preparer side of the schedule is settled the same way on every '
    'return filed through this site, and preparing both the statements and '
    'the schedule describing them is inside the fee of '
    + PRICE + '.</p>'),
  ],
  faq=[
   ('What is GIFI Schedule 141?',
    'The notes checklist. It records who prepared the financial statements '
    'and what level of work stands behind them, where Schedules 100 and 125 '
    'carry the figures.'),
   ('Does a nil return need an audit or a review?',
    'No. Neither audited nor reviewed is the normal answer for a dormant '
    'corporation and it is a complete answer.'),
   ('When is Schedule 141 required?',
    'On the same trigger as the other two GIFI schedules. Any share capital, '
    'cash, shareholder loan, incorporation cost or bank charge makes all '
    'three required.'),
   ('Is there a separate test for Schedule 141?',
    'No. It goes on the return whenever Schedules 100 and 125 do.'),
   ('Who is recorded as preparing the statements?',
    'On a return filed here, Gondaliya CPA Professional Corporation, which '
    'prepares and transmits in Canada as a registered EFILE electronic '
    'filer.'),
  ]),
]


TOOLS8 += [
 dict(slug='dormant-corporation-obligation-checker',
  title='Dormant Corporation Obligation Checker | What Is Still Owed',
  h1_pre='Dormant Corporation ', h1_span='Obligation Checker',
  h1='Dormant Corporation Obligation Checker',
  eyebrow='Still Owed',
  keyword='dormant corporation obligation checker',
  meta=('A dormant corporation still owes filings. Three answers list every '
        'one of them and say which are covered by the fee.'),
  tags=['Lists what is still owed', 'Separates the registry filing',
        'Open accounts keep running', 'Says what the fee covers'],
  form=tool('The corporation as it stands',
            [yn('fed', 'Is the corporation federally incorporated?'),
             yn('pay', 'Is a payroll account still open?'),
             yn('gst', 'Is a GST/HST account still open?')],
            'Answer all three questions.'),
  js=None,
  sections=[
   ('three-tools', 'Three Tools on This Subject, and Which One You Want',
    '<p>Dormancy comes up in three different questions and there is a tool '
    'for each. This one lists what is still owed while the corporation stays '
    'open.</p>\n'
    '<p>The '
    + a(T + 'dormant-corporation-test/', 'dormant corporation test')
    + ' decides whether the corporation is dormant in the first place. The '
    + a(T + 'cra-account-closure-sequencer/',
        'CRA account closure sequencer')
    + ' gives the order for shutting the accounts down. The '
    + a(T + 'corporate-deadline-calendar-generator/',
        'corporate deadline calendar generator')
    + ' puts dates on the obligations this page lists.</p>'),
   ('nothing-lapses', 'Nothing Lapses Because Nobody Is Looking',
    '<p>A corporation must file a T2 within six months of its fiscal '
    'year-end, every year, until it is formally dissolved. Being dormant is '
    'not a status that suspends that, and no amount of time passing turns it '
    'into one.</p>\n'
    '<p>The registry annual return runs alongside it on its own date. Two '
    'obligations, two bodies, two consequences for missing them, and neither '
    'of them stops because the corporation has gone quiet.</p>'),
   ('open-accounts', 'An Open Account Keeps Generating Returns',
    '<p>A payroll account expects a T4 information return even where nobody '
    'was paid, and a GST/HST account expects returns including nil ones. The '
    'obligation follows the open account rather than the activity.</p>\n'
    '<p>Form RC145 closes either of them. An inactive T2 does not close those '
    'accounts, which is the mistake worth avoiding: filing the tax return '
    'does not tell the payroll account to stop expecting something.</p>'),
   ('what-the-fee-covers', 'One of These Is Inside the Fee',
    '<p>The nil T2 is '
    + PRICE + '. The registry annual return, any T4 return and any GST/HST '
    'return sit outside it, as does closing an account.</p>\n'
    '<p>Which is said here rather than in the small print because a visitor '
    'reading a list of obligations should be able to see, in the same table, '
    'which one this service takes off their hands.</p>'),
  ],
  faq=[
   ('What does a dormant corporation still have to file?',
    'A T2 every year until it is formally dissolved, the annual return to its '
    'registry, and returns on any payroll or GST/HST account that is still '
    'open.'),
   ('Does being dormant suspend the filing requirement?',
    'No. A corporation must file a T2 within six months of its fiscal '
    'year-end, every year, until it is formally dissolved.'),
   ('Does filing a nil T2 close my payroll account?',
    'No. An inactive T2 does not close those accounts. Form RC145 closes a '
    'payroll or a GST/HST account.'),
   ('Is the registry annual return part of the tax return?',
    'No. It is a separate filing to a separate body, reporting the directors '
    'and the registered office rather than any income.'),
   ('Which of these is covered by the fee?',
    'The nil T2 return, at $300.00 plus HST per tax year. The registry annual '
    'return, T4 returns, GST/HST returns and account closures are outside '
    'it.'),
  ]),

 dict(slug='annual-return-vs-tax-return-checker',
  title='Annual Return vs Tax Return Checker | Two Different Filings',
  h1_pre='Annual Return vs ', h1_span='Tax Return Checker',
  h1='Annual Return vs Tax Return Checker',
  eyebrow='Two Filings',
  keyword='annual return vs tax return checker',
  meta=('The annual return and the T2 are unrelated filings to different '
        'bodies. Two answers set them side by side.'),
  tags=['Side by side', 'Different bodies, different dates',
        'Different consequences', 'Only one is in the fee'],
  form=tool('Where the corporation is registered',
            [yn('fed', 'Is it federally incorporated?'),
             yn('prov', 'Is it registered in a province other than where it '
                        'was incorporated?')],
            'Answer both questions.'),
  js=None,
  sections=[
   ('one-word-two-things', 'Two Filings at a Minimum, and One Shared Word',
    '<p>Every corporation owes at least two: a tax return, and an annual '
    'return to the registry that holds it. The annual return and the tax '
    'return share a word and nothing else. '
    'One confirms the directors and the registered office to the registry '
    'that holds the corporation. The other reports the year&#8217;s figures '
    'to the Canada Revenue Agency.</p>\n'
    '<p>Nearly every confusion on this subject comes from the shared noun. '
    'Once they are set beside each other the overlap turns out to be the '
    'word, which is why this page is a comparison rather than an '
    'explanation.</p>'),
   ('neither-covers-the-other', 'Filing One Does Nothing for the Other',
    '<p>A corporation can be up to date on its annual returns and have six '
    'years of unfiled T2 returns behind it. The registry is satisfied and the '
    'tax years are open, because the registry never told the Canada Revenue '
    'Agency anything.</p>\n'
    '<p>It runs the other way too. Every T2 filed on time does not stop a '
    'corporation being struck from the register for missing the annual '
    'return, which the '
    + a(T + 'involuntary-dissolution-risk-checker/',
        'involuntary dissolution risk checker')
    + ' covers.</p>'),
   ('the-federal-numbers', 'The Federal Annual Return Has a Date and a Fee',
    '<p>A federal corporation files its annual return within 60 days of the '
    'incorporation anniversary, and the fee is $12.00. It is a government fee '
    'and HST does not apply to it.</p>\n'
    '<p>Note what that date runs from. The anniversary, not the fiscal '
    'year-end, so the two filings can sit months apart and both be on time. '
    'The '
    + a(T + 'federal-annual-return-anniversary-calculator/',
        'federal annual return anniversary calculator')
    + ' works out the dates.</p>'),
   ('only-one-is-in-the-fee', 'Only One of Them Is Inside the Fee',
    '<p>The nil T2 is '
    + PRICE + '. The annual return is a registry filing and is not covered by '
    'it, which is stated plainly here rather than discovered later.</p>\n'
    '<p>That is not a gap in the service so much as a different counter. A '
    'registry filing is made to the registry, and a corporation can make it '
    'itself in a few minutes once it knows the date.</p>'),
  ],
  faq=[
   ('Is the annual return the same as the tax return?',
    'No. The annual return is a registry filing confirming the directors and '
    'the registered office. The T2 is a corporate income tax return filed '
    'with the Canada Revenue Agency.'),
   ('Does filing my T2 cover the annual return?',
    'No. They go to different bodies and neither one satisfies the other.'),
   ('When is the federal annual return due?',
    'Within 60 days of the incorporation anniversary. That date runs from the '
    'anniversary rather than the fiscal year-end.'),
   ('How much is the federal annual return?',
    '$12.00. It is a government fee and HST does not apply to it.'),
   ('What happens if I miss each one?',
    'An unfiled T2 leaves the tax year open, invites a demand to file and '
    'blocks a clearance certificate. A missed annual return can get the '
    'corporation struck from the register.'),
  ]),
]


TOOLS8 += [
 dict(slug='dissolve-or-keep-filing-cost-calculator',
  title='Dissolve or Keep Filing Cost Calculator | Both Routes Priced',
  h1_pre='Dissolve or ', h1_span='Keep Filing Cost Calculator',
  h1='Dissolve or Keep Filing Cost Calculator',
  eyebrow='The Decision',
  keyword='dissolve or keep filing cost calculator',
  meta=('Keeping a dormant corporation costs a return every year. Enter the '
        'years to compare that with winding it up.'),
  tags=['Both routes side by side', 'Totals the years of filing',
        'Names what is outside the fee', 'Unfiled years come first'],
  form=tool('The decision',
            [num('n', 'How many more years would you keep it?',
                 'Between 1 and 20', 1, 20, '5'),
             yn('fed', 'Is it federally incorporated?'),
             yn('beh', 'Are any years already unfiled?')],
            'Enter the number of years and answer both questions.'),
  js=None,
  sections=[
   ('a-recurring-cost', 'Keeping a Dormant Corporation Is a Recurring Cost',
    '<p>A corporation must file a T2 within six months of its fiscal '
    'year-end, every year, until it is formally dissolved. Holding an empty '
    'corporation is therefore a decision to pay for a return annually for as '
    'long as it exists.</p>\n'
    '<p>Which is often the right decision. There are good reasons to hold a '
    'name, a history or a registration. It is worth seeing as a subscription '
    'rather than as a formality, and that is what the left column of the '
    'comparison does.</p>'),
   ('one-side-totals', 'One Side Totals and the Other Does Not',
    '<p>The returns are priced here, so the cost of staying open totals '
    'exactly. Winding up involves a clearance certificate request and the '
    'registry articles of dissolution, and neither is covered by this '
    'fee.</p>\n'
    '<p>So the comparison names those steps rather than putting a figure on '
    'them. A page that invented a total for the dissolution side would be '
    'more satisfying to read and less use to rely on.</p>'),
   ('unfiled-first', 'Unfiled Years Come First on Either Route',
    '<p>Where years are already outstanding the choice narrows, because both '
    'routes start in the same place. A clearance request rests on a complete '
    'filing record, and dissolving a corporation that still owes returns '
    'leaves those tax years open behind it.</p>\n'
    '<p>The '
    + a(T + 'catch-up-filing-schedule-generator/',
        'catch-up filing schedule generator')
    + ' dates the outstanding years and the '
    + a(T + 'unfiled-years-cost-calculator/',
        'unfiled years cost calculator')
    + ' totals them. Those come before this decision rather than after '
    'it.</p>'),
   ('what-each-ends', 'What Each Route Actually Ends',
    '<p>Filing for another five years ends nothing. At the end of it the '
    'corporation is still on the register and the same question arrives '
    'again, five years of fees later.</p>\n'
    '<p>A completed wind-up ends the obligation. That is the difference the '
    'right-hand column is really reporting, and it is worth more weight than '
    'the arithmetic. The '
    + a(T + 'dissolution-readiness-checker/',
        'dissolution readiness checker')
    + ' tests whether the corporation is ready for it.</p>'),
  ],
  faq=[
   ('Is it cheaper to dissolve a corporation or keep filing?',
    'Keeping it costs $300.00 plus HST per tax year for as long as it exists, '
    'plus the registry annual return. Winding up is one final return plus a '
    'clearance request and the registry dissolution, and those two are not '
    'covered by this fee.'),
   ('Why does the comparison not total both sides?',
    'Because only one side is priced here. The returns are; a clearance '
    'request and the registry articles of dissolution are not, so the page '
    'names them rather than inventing a figure.'),
   ('Can I dissolve without filing the outstanding years?',
    'Dissolving a corporation that still owes returns leaves those tax years '
    'open behind it, and a clearance request rests on a complete filing '
    'record. Both routes start with the outstanding years.'),
   ('What does a nil return cost each year?',
    '$300.00 plus HST per tax year, for one corporation for one tax year.'),
   ('Is there a reason to keep a dormant corporation?',
    'Often, yes. Holding a name, a history or a registration can be worth the '
    'annual cost. The point of the comparison is to show what that cost '
    'is.'),
  ]),

 dict(slug='federal-annual-return-fee-calculator',
  title='Federal Annual Return Fee Calculator | $12.00 a Year, Dated',
  h1_pre='Federal Annual ', h1_span='Return Fee Calculator',
  h1='Federal Annual Return Fee Calculator',
  eyebrow='Annual Return',
  keyword='federal annual return fee calculator',
  meta=('The federal annual return is $12.00 within 60 days of the '
        'anniversary. Enter the incorporation date for a dated schedule.'),
  tags=['$12.00 a year', 'No HST on a government fee',
        'Runs from the anniversary', 'Outside the nil T2 fee'],
  form=tool('The corporation',
            [date('inc', 'The date on the certificate of incorporation'),
             num('n', 'How many years to list', 'Between 1 and 20',
                 1, 20, '5')],
            'Enter the incorporation date and how many years to list.'),
  js=None,
  sections=[
   ('the-two-numbers', 'Two Numbers, and Neither Moves',
    '<p>A federal corporation files its annual return within 60 days of the '
    'incorporation anniversary, and the fee is $12.00. Both are fixed, which '
    'makes this the most predictable obligation a corporation has.</p>\n'
    '<p>It is a government fee and HST does not apply to it. So the total '
    'this page gives is the total: there is no tax line to add to it, unlike '
    'every other price on the site.</p>'),
   ('from-the-anniversary', 'The Date Runs From the Anniversary',
    '<p>Not from the fiscal year-end, which is what makes this obligation '
    'drift out of sight. A corporation whose T2 is due in December and whose '
    'anniversary falls in March has two filing dates nine months apart, every '
    'year, both correct.</p>\n'
    '<p>Changing the fiscal year-end does not move this date either. The '
    + a(T + 'federal-annual-return-anniversary-calculator/',
        'federal annual return anniversary calculator')
    + ' works out a single year&#8217;s dates in more detail than the table '
    'here does.</p>'),
   ('not-a-tax-return', 'It Is Not a Tax Return and Missing It Is a '
    'Different Problem',
    '<p>The annual return reports the directors and the registered office to '
    'Corporations Canada. It reports no income and no tax, and filing it says '
    'nothing to the Canada Revenue Agency.</p>\n'
    '<p>Missing it does not create an unfiled tax year. It puts the '
    'corporation at risk of being struck from the register, which is a '
    'different consequence with a different cure. The '
    + a(T + 'annual-return-vs-tax-return-checker/',
        'annual return versus tax return checker')
    + ' sets the two filings side by side.</p>'),
   ('outside-the-fee', 'Outside the Nil T2 Fee, and Small',
    '<p>This filing is not covered by the nil T2 fee of '
    + PRICE + '. It is a registry filing, made to the registry, and a '
    'corporation can make it itself once it knows the date.</p>\n'
    '<p>Which is the practical reason this page exists. At $12.00 the fee is '
    'not the problem. Not knowing the date is, and a corporation struck off '
    'for the want of a $12.00 filing has an expensive problem from a cheap '
    'cause.</p>'),
  ],
  faq=[
   ('How much is the federal annual return?',
    '$12.00. It is a government fee and HST does not apply to it.'),
   ('When is it due?',
    'Within 60 days of the incorporation anniversary.'),
   ('Does the date move if I change my fiscal year-end?',
    'No. It runs from the incorporation anniversary, so it does not follow '
    'the fiscal year-end.'),
   ('Is the annual return covered by the nil T2 fee?',
    'No. The fee of $300.00 plus HST per tax year covers the nil T2 return. '
    'The annual return is a separate registry filing.'),
   ('What happens if I miss it?',
    'It does not create an unfiled tax year. It puts the corporation at risk '
    'of being struck from the register.'),
  ]),
]

assert len(TOOLS8) == 10, '%d tools in batch 8' % len(TOOLS8)


def _tbl(head, rows):
    h = ('<table class="ei-tbl"><thead><tr>'
         + ''.join('<th scope="col">%s</th>' % c for c in head)
         + '</tr></thead><tbody>')
    for r in rows:
        h += '<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>'
    return h + '</tbody></table>'


# One static reference table per page, in the body, so a visitor who has
# entered nothing still gets the shape of the answer. gate8.py requires it.
TABLES8 = {
 't2-filing-requirement-checker': ('what-does-not-exempt', _tbl(
   ['What people believe', 'What it actually means'],
   [['The corporation had no income',
     'A description of a nil year. The return is still owed'],
    ['It has no bank account',
     'There is no asset test in the filing requirement'],
    ['It never started trading',
     'Returns are owed from incorporation, not from first sale'],
    ['Nobody has touched it for years',
     'Every one of those years is an unfiled year'],
    ['It was dissolved mid-year',
     'A final return is owed for the period up to that date'],
    ['The year is before incorporation',
     'Correct. There is no tax year and nothing to file']])),

 'required-schedules-checker': ('the-five', _tbl(
   ['Schedule', 'What puts it on the return', 'Inside the fee'],
   [['GIFI Schedules 100, 125 and 141',
     'Any of share capital, cash, a shareholder loan, an incorporation cost '
     'or a bank charge', 'Yes'],
    ['Schedule 24', 'A first return', 'Yes'],
    ['Schedule 50', 'Any shareholder at 10 percent or more', 'Yes'],
    ['Schedule 8 and loss continuity',
     'Depreciable property, or a loss carried forward', 'Yes']])),

 'share-capital-reporting-checker': ('first-of-five', _tbl(
   ['The five triggers', 'How a dormant corporation usually acquires it'],
   [['Share capital', 'Shares issued at incorporation'],
    ['Cash', 'A bank account opened and never closed'],
    ['A shareholder loan', 'Money put in to cover a cost, never repaid'],
    ['An incorporation cost', 'The cost of setting the corporation up'],
    ['A bank charge', 'A monthly fee on the account nobody uses']])),

 'shareholder-loan-balance-checker': ('either-direction', _tbl(
   ['The balance', 'What it is called', 'Makes GIFI required'],
   [['The corporation owes the shareholder',
     'A due-to-shareholder balance', 'Yes'],
    ['The shareholder owes the corporation',
     'A due-from-shareholder balance', 'Yes'],
    ['A balance that did not move all year',
     'Still a shareholder loan balance', 'Yes'],
    ['No balance either way', 'Nothing to report on this ground', 'No']])),

 'gifi-schedule-125-checker': ('what-125-is', _tbl(
   ['GIFI schedule', 'What it carries', 'On a dormant year'],
   [['Schedule 100', 'The balance sheet',
     'Share capital, cash and any loan balance'],
    ['Schedule 125', 'The income statement',
     'Zeros, unless there was a bank charge or another expense'],
    ['Schedule 141', 'The notes checklist',
     'Who prepared the statements, and that they were neither audited nor '
     'reviewed']])),

 'gifi-schedule-141-checker': ('what-141-is', _tbl(
   ['What Schedule 141 records', 'The usual answer on a dormant corporation'],
   [['Who prepared the financial statements',
     'The firm that prepared the return'],
    ['Whether they were audited', 'No'],
    ['Whether they were reviewed', 'No'],
    ['Whether any assurance work was performed',
     'None, which is a complete answer on a nil return']])),

 'dormant-corporation-obligation-checker': ('three-tools', _tbl(
   ['What you want to know', 'The tool that answers it'],
   [['Whether the corporation counts as dormant', 'Dormant corporation test'],
    ['What is still owed while it stays open', 'This page'],
    ['The order for closing the CRA accounts',
     'CRA account closure sequencer'],
    ['The dates those obligations fall on',
     'Corporate deadline calendar generator']])),

 'annual-return-vs-tax-return-checker': ('one-word-two-things', _tbl(
   ['', 'The T2', 'The annual return'],
   [['What it is', 'A corporate income tax return', 'A registry filing'],
    ['Filed with', 'The Canada Revenue Agency',
     'The registry the corporation is incorporated with'],
    ['What it reports', 'The year&#8217;s figures',
     'The directors and the registered office'],
    ['Missing it', 'The tax year stays open',
     'The corporation can be struck from the register'],
    ['Inside the fee', 'Yes', 'No']])),

 'dissolve-or-keep-filing-cost-calculator': ('one-side-totals', _tbl(
   ['Step', 'Which route', 'Priced here'],
   [['A nil T2 for each year it stays open', 'Keep filing',
     'Yes, $300.00 plus HST per tax year'],
    ['The registry annual return each year', 'Keep filing',
     'No, a government fee'],
    ['The final T2 for the period ending at dissolution', 'Wind up',
     'Yes, $300.00 plus HST'],
    ['A clearance certificate request', 'Wind up', 'No'],
    ['The registry articles of dissolution', 'Wind up', 'No']])),

 'federal-annual-return-fee-calculator': ('the-two-numbers', _tbl(
   ['Item', 'The federal annual return'],
   [['Fee', '$12.00'],
    ['HST on the fee', 'None. It is a government fee'],
    ['Due', 'Within 60 days of the incorporation anniversary'],
    ['Measured from', 'The incorporation anniversary, not the year-end'],
    ['Filed with', 'Corporations Canada'],
    ['Inside the nil T2 fee', 'No']])),
}

assert set(TABLES8) == {t['slug'] for t in TOOLS8}, (
    'every tool in the batch carries a reference table; TABLES8 does not '
    'match TOOLS8')

for t in TOOLS8:
    _sid, _html = TABLES8[t['slug']]
    _ids = [s for s, _, _ in t['sections']]
    assert _sid in _ids, (
        '%s: table is attached to section %r, which the page does not have '
        '(it has %r)' % (t['slug'], _sid, _ids))
    t['sections'] = [(s, h, (b + '\n' + _html) if s == _sid else b)
                     for s, h, b in t['sections']]


SEO8 = {
 't2-filing-requirement-checker': (
   'T2 Filing Requirement Checker | Is a Return Owed',
   'A corporation files a T2 every year until it is formally dissolved. '
   'Three answers test whether this year is owed.'),
 'required-schedules-checker': (
   'Required Schedules Checker | Nil T2 Schedules',
   'Seven answers give the whole schedule set a nil return carries: the GIFI '
   'schedules, Schedule 24, 50 and 8.'),
 'share-capital-reporting-checker': (
   'Share Capital Reporting Checker | GIFI, Schedule 50',
   'Share capital makes the GIFI schedules required even with no activity. '
   'Three answers show what yours triggers.'),
 'shareholder-loan-balance-checker': (
   'Shareholder Loan Balance Checker | Nil Returns',
   'A shareholder loan balance makes the GIFI schedules required even with no '
   'activity. Either direction counts.'),
 'gifi-schedule-125-checker': (
   'GIFI Schedule 125 Checker | The Income Statement',
   'Schedule 125 is the income statement. Three answers show whether it goes '
   'on a nil return and what it carries.'),
 'gifi-schedule-141-checker': (
   'GIFI Schedule 141 Checker | The Notes Checklist',
   'Schedule 141 records who prepared the statements and what work stands '
   'behind them. Three answers test it.'),
 'dormant-corporation-obligation-checker': (
   'Dormant Corporation Obligation Checker | Still Owed',
   'A dormant corporation still owes filings. Three answers list every one '
   'and say which the fee covers.'),
 'annual-return-vs-tax-return-checker': (
   'Annual Return vs Tax Return Checker | Two Filings',
   'The annual return and the T2 are unrelated filings to different bodies. '
   'Two answers set them side by side.'),
 'dissolve-or-keep-filing-cost-calculator': (
   'Dissolve or Keep Filing Cost Calculator | Compared',
   'Keeping a dormant corporation costs a return every year. Enter the years '
   'to compare that with winding it up.'),
 'federal-annual-return-fee-calculator': (
   'Federal Annual Return Fee Calculator | 12 Dollars',
   'The federal annual return is $12.00 within 60 days of the anniversary. '
   'Enter the incorporation date for a schedule.'),
}

for t in TOOLS8:
    t['seo_title'], t['seo_desc'] = SEO8[t['slug']]
    assert len(t['seo_title']) <= 60, (
        '%s: SEO title is %d characters' % (t['slug'], len(t['seo_title'])))
    assert 70 <= len(t['seo_desc']) <= 160, (
        '%s: SEO description is %d characters'
        % (t['slug'], len(t['seo_desc'])))
assert set(SEO8) == {t['slug'] for t in TOOLS8}, 'SEO8 does not match TOOLS8'

for t, js in zip(TOOLS8, [T51_JS, T52_JS, T53_JS, T54_JS, T55_JS,
                          T56_JS, T57_JS, T58_JS, T59_JS, T60_JS]):
    t['js'] = js if js.startswith(PRELUDE) else PRELUDE + js

ORDER8 = ORDER7 + [t['slug'] for t in TOOLS8]
LINK_TITLE8 = dict(LINK_TITLE7, **{
 't2-filing-requirement-checker': 'T2 filing requirement checker',
 'required-schedules-checker': 'Required schedules checker',
 'share-capital-reporting-checker': 'Share capital reporting checker',
 'shareholder-loan-balance-checker': 'Shareholder loan balance checker',
 'gifi-schedule-125-checker': 'GIFI Schedule 125 checker',
 'gifi-schedule-141-checker': 'GIFI Schedule 141 checker',
 'dormant-corporation-obligation-checker':
     'Dormant corporation obligation checker',
 'annual-return-vs-tax-return-checker':
     'Annual return versus tax return checker',
 'dissolve-or-keep-filing-cost-calculator':
     'Dissolve or keep filing cost calculator',
 'federal-annual-return-fee-calculator':
     'Federal annual return fee calculator',
})

SIBLINGS8 = {
 't2-filing-requirement-checker': [
   'unfiled-years-checker', 'inactive-corporation-filing-checker',
   'final-t2-return-due-date-calculator'],
 'required-schedules-checker': [
   'gifi-schedule-requirement-checker',
   'schedule-50-shareholder-threshold-checker',
   'schedule-8-cca-requirement-checker'],
 'share-capital-reporting-checker': [
   'schedule-50-shareholder-threshold-checker',
   'nil-gifi-balance-sheet-checker', 'nil-return-vs-full-return-checker'],
 'shareholder-loan-balance-checker': [
   'nil-gifi-balance-sheet-checker', 'balance-sheet-balancing-checker',
   'required-schedules-checker'],
 'gifi-schedule-125-checker': [
   'nil-gifi-balance-sheet-checker', 'gifi-schedule-requirement-checker',
   'gifi-schedule-141-checker'],
 'gifi-schedule-141-checker': [
   'gifi-schedule-125-checker', 'nil-gifi-balance-sheet-checker',
   'required-schedules-checker'],
 'dormant-corporation-obligation-checker': [
   'dormant-corporation-test', 'cra-account-closure-sequencer',
   'corporate-deadline-calendar-generator'],
 'annual-return-vs-tax-return-checker': [
   'federal-annual-return-anniversary-calculator',
   'involuntary-dissolution-risk-checker',
   'federal-annual-return-fee-calculator'],
 'dissolve-or-keep-filing-cost-calculator': [
   'dissolution-readiness-checker', 'catch-up-filing-schedule-generator',
   'unfiled-years-cost-calculator'],
 'federal-annual-return-fee-calculator': [
   'federal-annual-return-anniversary-calculator',
   'annual-return-vs-tax-return-checker',
   'involuntary-dissolution-risk-checker'],
}

GUIDES8 = {
 't2-filing-requirement-checker': [
   ('nil-t2-return-complete-guide', 'The complete guide to the nil T2 return')],
 'required-schedules-checker': [
   ('t2-schedules-on-a-nil-return', 'T2 schedules on a nil return')],
 'share-capital-reporting-checker': [
   ('schedule-50-and-shareholder-reporting',
    'Schedule 50 and shareholder reporting')],
 'shareholder-loan-balance-checker': [
   ('gifi-schedules-100-125-141', 'GIFI Schedules 100, 125 and 141')],
 'gifi-schedule-125-checker': [
   ('gifi-schedules-100-125-141', 'GIFI Schedules 100, 125 and 141')],
 'gifi-schedule-141-checker': [
   ('gifi-schedules-100-125-141', 'GIFI Schedules 100, 125 and 141')],
 'dormant-corporation-obligation-checker': [
   ('dormant-and-inactive-corporations', 'Dormant and inactive corporations'),
   ('cra-accounts-on-a-dormant-corporation',
    'CRA accounts on a dormant corporation')],
 'annual-return-vs-tax-return-checker': [
   ('provincial-and-federal-annual-returns',
    'Provincial and federal annual returns')],
 'dissolve-or-keep-filing-cost-calculator': [
   ('winding-up-an-inactive-corporation',
    'Winding up an inactive corporation'),
   ('final-t2-and-dissolution', 'The final T2 and dissolution')],
 'federal-annual-return-fee-calculator': [
   ('provincial-and-federal-annual-returns',
    'Provincial and federal annual returns')],
}

_ORDER = set(ORDER8)

assert len(TOOLS8) == 10, '%d tools in batch 8' % len(TOOLS8)
assert len({t['slug'] for t in TOOLS8}) == 10, 'duplicate slug in the batch'

for t in TOOLS8:
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

    # Every radio group the form emits is listened to and read, or the page
    # renders nothing when that group changes.
    _names = set(_re.findall(r'name="([\w-]+)"', t['form']))
    for _n in _names:
        assert 'input[name="%s"]' % _n in t['js'], (
            '%s: radio group %r has no change listener' % (t['slug'], _n))
        assert "pick('%s')" % _n in t['js'], (
            '%s: radio group %r is never read' % (t['slug'], _n))

    # Every number or date field is read as well. yn() groups are covered
    # above; this catches a date() or num() row the module forgot to bind.
    # It matches on the input element rather than on id="..." anywhere in the
    # form, because yn() also puts an id on its label for aria-labelledby and
    # a label is not a field.
    _inputs = set(_re.findall(r'<input[^>]*\bid="([\w-]+)"', t['form']))
    for _i in _inputs:
        assert "'%s'" % _i in t['js'], (
            '%s: field %r is never read by the module' % (t['slug'], _i))

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

    # Rule 1: "authorized" only inside the one permitted phrase.
    _auth = (_body + t['form'] + t['js'] + t['title']).replace(
        'authorized signing officer', '')
    assert not _re.search(r'\bauthoriz', _auth, _re.I), (
        '%s: "authorized" appears outside the permitted phrase' % t['slug'])

    # Canadian English, and the hedges the F9 gate bans.
    for _w in ('authorise', 'organise', 'recognise', 'analyse'):
        assert _w not in _body.lower(), '%s: British spelling %r' % (
            t['slug'], _w)
    for _w in (' just ', 'simply'):
        assert _w not in _body.lower(), '%s: hedge word %r' % (t['slug'], _w)

    # The visible H1 and the schema headline are the same sentence.
    assert t['h1_pre'] + t['h1_span'] == t['h1'], (
        '%s: h1_pre + h1_span is %r but h1 is %r'
        % (t['slug'], t['h1_pre'] + t['h1_span'], t['h1']))

# Every slug is new, and every link target exists.
_LIVE = set(ORDER7)
for t in TOOLS8:
    assert t['slug'] not in _LIVE, '%s is already live' % t['slug']
    for s in SIBLINGS8[t['slug']]:
        assert s in _ORDER, '%s links to tool %s, which does not exist' % (
            t['slug'], s)
        assert s != t['slug'], '%s lists itself as a sibling' % t['slug']
        assert s in LINK_TITLE8, '%s has no link title' % s
    for g, _ttl in GUIDES8[t['slug']]:
        assert g in GUIDES_LIVE8, (
            '%s links to guide %s, which is not live' % (t['slug'], g))
assert set(SIBLINGS8) == {t['slug'] for t in TOOLS8}, 'SIBLINGS8 mismatch'
assert set(GUIDES8) == {t['slug'] for t in TOOLS8}, 'GUIDES8 mismatch'

for t in TOOLS8:
    _all = ' '.join(b for _, _, b in t['sections']) + t['form']
    for s in set(_re.findall(r'/tools/([a-z0-9-]+)/', _all)):
        assert s in _ORDER, (
            '%s: body links to /tools/%s/, which does not exist'
            % (t['slug'], s))
    for g in set(_re.findall(r'/guides/([a-z0-9-]+)/', _all)):
        assert g in GUIDES_LIVE8, (
            '%s: body links to /guides/%s/, which is not live'
            % (t['slug'], g))

for t in TOOLS8:
    rel = [(T + s + '/', LINK_TITLE8[s]) for s in SIBLINGS8[t['slug']]]
    rel += [(G + g + '/', ttl) for g, ttl in GUIDES8[t['slug']]]
    rel.append((COST, 'Nil T2 filing cost'))
    t['related'] = rel


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'October 30, 2026', '2026-10-30'
    recs = []
    for t in TOOLS8:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2h-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-46s %6d bytes' % (r['slug'], len(r['content'].encode())))
