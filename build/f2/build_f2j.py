# -*- coding: utf-8 -*-
"""Family 2 batch 10: tools 71 to 80.

NONE OF THESE TEN IS AN APPENDIX A SLUG, AND THAT IS DELIBERATE.

build_f2i.py measured what the appendix has left and the answer was about ten
pages, which batch 9 built. Of the three appendix tool slugs still unbuilt,
/nil-return-eligibility-quiz/ and /tax-deadline-calculator/ are the live
nil-t2-eligibility-checker and nil-t2-deadline-calculator under another name,
and /ontario-annual-return-due-date-calculator/ needs the Ontario annual return
deadline, which the plan states nowhere. Building any of the three would put the
same page at a second URL, which is the pattern line 1212 exists to prevent.

So this batch takes the second of the three options already logged for Sharad
Gondaliya: slugs outside the appendix, each answering a question the plan's own
facts already settle. No tool here needs a figure the plan does not carry. The
source for each is named below.

WHAT NAVNEET ASKED FOR THIS BATCH

"make sure they have all sections tables". Batches 6 and 7 shipped tool pages
with no static table in the body, and gate9 added a check for one. This batch
makes the whole section set a build-time contract rather than a habit:
STRUCTURE below is asserted for every page, and gate10.py re-checks it against
the rendered HTML. Every page carries three prose sections, a static reference
table in the body, a table drawn in the result, three FAQ items, six Read Next
links, the hero tag strip, the byline, the review stamp, the EFILE strip and
the closing call to action. A page missing any one of them fails the build.

THE SOURCE FOR EACH TOOL

  "the year-end must match the record the Agency holds or the transmission is
  rejected", and "one corrected transmission is included in the fee", both
  already on the live Family 4 pages                      -> tools 71, 80
  "any share capital, cash, shareholder loan, incorporation cost or bank
  charge makes the GIFI schedules required"   (plan 1827, 2081, 2151)
                                                          -> tools 72, 79
  "a bank charge does not stop the year being nil", and interest credited on a
  balance is income, so the year is not nil               -> tools 72, 74
  "The first tax year cannot exceed 53 weeks", and Schedule 24 on a first
  return                                                  -> tool 73
  NOT_NIL: revenue, a dividend either way, rent or investment income is not
  nil and routes to gondaliyacpa.ca at $350.00 plus HST per year
                                                          -> tools 72, 74
  "Schedule 8 and loss continuity" are inside the fee, and a year is only
  established by its own filed return                     -> tool 75
  PRICE is charged per tax year, per return                -> tools 76, 78
  "A final T2 is due within six months of the date of dissolution", and
  unfiled years block a clearance certificate and the dissolution
                                                          -> tool 77
  An unfiled year stays open until its own return is filed, and it is the
  corporation's year rather than any owner's              -> tool 78
  "Schedule 50 for every shareholder at 10% or more"   (plan 177, 1869)
                                                          -> tool 79

WHAT TOOL 78 DOES NOT DECIDE

Buying a corporation has tax consequences of its own, and an acquisition of
control has an effect on a tax year that the plan does not state. Tool 78
answers the filing question only: the outstanding years belong to the
corporation and are still outstanding after it changes hands. It says on the
page that the wider question is not one it answers, rather than leaving the
silence to be read as "nothing happens".
"""
import io, json, os
import re as _re

from build_f2 import (render, meta, yn, a, SITE, HUB, FORM, PRICE,
                      NOT_NIL, TOOL_DISCLAIMER)
from build_f2b import tool, num, date, PICK, T, G, COST
from build_f2c import MONEY_JS, QUAL, PRELUDE
from build_f2f import BASE, RBASE
from build_f2i import ORDER9, LINK_TITLE9, GUIDES_LIVE9

HERE = os.path.dirname(os.path.abspath(__file__))

# Read from the hub's own children file rather than retyped, same as batch 9.
_GUIDES_JSON = os.path.join(HERE, '..', 'f16', 'guides-hub-children.json')
GUIDES_LIVE10 = set(json.load(io.open(_GUIDES_JSON, encoding='utf-8'))['slugs'])
assert GUIDES_LIVE9 <= GUIDES_LIVE10, 'batch 9 linked a guide no longer listed'

# The seventy live tool slugs, read the same way, so a sibling link cannot
# point at a tool that was never published.
_TOOLS_JSON = os.path.join(HERE, '..', 'f16', 'tools-hub-children.json')
TOOLS_LIVE = set(json.load(io.open(_TOOLS_JSON, encoding='utf-8'))['slugs'])
# The file holds whatever is live, so this builder has to run correctly both
# before this batch publishes (seventy live) and after (eighty). Checking the
# base set rather than the total means a rebuild after publishing still fails
# if some OTHER tool has gone missing from the hub's children.
_THIS_BATCH = {
 'efile-rejection-reason-checker', 'expenses-only-year-checker',
 'never-traded-corporation-checker',
 'restarting-a-dormant-corporation-checker',
 'loss-continuity-on-a-nil-return-checker',
 'multiple-corporation-filing-cost-calculator',
 'post-dissolution-return-checker',
 'acquired-corporation-unfiled-years-checker',
 'sole-shareholder-corporation-checker',
 'business-number-versus-corporation-number-checker'}
assert len(TOOLS_LIVE - _THIS_BATCH) == 70, (
    'expected the seventy tools live before this batch, got %d'
    % len(TOOLS_LIVE - _THIS_BATCH))
PUBLISHED = _THIS_BATCH <= TOOLS_LIVE


def _tbl(head, rows):
    """A static reference table, in the markup the other batches use."""
    return ('<table class="ei-tbl"><thead><tr>'
            + ''.join('<th scope="col">%s</th>' % h for h in head)
            + '</tr></thead><tbody>\n'
            + '\n'.join('<tr>' + ''.join('<td>%s</td>' % c for c in r)
                        + '</tr>' for r in rows)
            + '\n</tbody></table>')


# ----------------------------------------------------- 71. e-filing rejection
T71_JS = RBASE + r"""
/* Each row carries its own affirmative wording rather than deriving one by
   rewriting the negative. A first draft built the all-clear table with
   .replace('does not match','matches'), which left the Business Number row
   reading "is not the one on the corporation record" beside the word
   "Matches". */
var CAUSE=[
 ['nm','The legal name does not match the register',
  'The return carries the exact legal name the register holds, including the '
  +'corporation number and the suffix. Correct the name and transmit again: '
  +'one corrected transmission is included in the fee.',
  'The legal name matches the register'],
 ['ye','The fiscal year-end does not match the record the Agency holds',
  'The year-end on file comes from the incorporation record. It is settled '
  +'with the Canada Revenue Agency before the return goes again, rather than '
  +'by filing a different date and hoping it lands.',
  'The fiscal year-end matches the record the Agency holds'],
 ['bn','The Business Number is not the one on the corporation record',
  'A return transmitted against another account cannot be assessed against '
  +'this corporation. The Business Number is confirmed against the '
  +'corporation name before the return is prepared.',
  'The Business Number is the one on the corporation record']
];
function rejects(){
  var rows=[],i,v,wait=0;
  for(i=0;i<CAUSE.length;i++){
    v=pick(CAUSE[i][0]);
    if(v===null){wait++;continue;}
    if(v==='n'){rows.push(CAUSE[i]);}
  }
  var fl=pick('fl');
  if(fl===null){wait++;}
  if(wait>0){return {wait:wait};}
  return {rows:rows,filed:fl==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=rejects(),h,i;
  if(r.wait){
    out.innerHTML='<p>'+r.wait+' of the four questions '
     +(r.wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  if(r.rows.length===0&&!r.filed){
    h='<h3>None of the four common causes is present</h3>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Checked</th>'
     +'<th scope="col">State</th></tr></thead><tbody>';
    for(i=0;i<CAUSE.length;i++){
      h+='<tr><td>'+CAUSE[i][3]+'</td><td>Matches</td></tr>';
    }
    h+='<tr><td>The year has already been filed</td><td>No</td></tr>';
    h+='</tbody></table>';
    h+='<p>Where all four hold and a transmission is still refused, the cause '
     +'is in the return rather than in its identifiers. We read the rejection '
     +'message, correct the return and transmit it again, and one corrected '
     +'transmission is included in '+PRICE_JS+'.</p>';
    h+='<p>'+DISC_JS+'</p>';
    out.innerHTML=h;return;
  }
  h='<h3>'+(r.rows.length||1)+' cause'+(r.rows.length===1?'':'s')
   +' to clear before the next transmission</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Cause</th>'
   +'<th scope="col">What clears it</th></tr></thead><tbody>';
  for(i=0;i<r.rows.length;i++){
    h+='<tr><td>'+r.rows[i][1]+'</td><td>'+r.rows[i][2]+'</td></tr>';
  }
  if(r.filed){
    h+='<tr><td>The tax year has already been filed and assessed</td>'
     +'<td>A year already assessed is not transmitted again. What changes an '
     +'assessed year is an adjustment to it, which is a different filing and '
     +'is not covered by the fee.</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>A rejection is not an assessment and it carries nothing by itself. '
   +'The year stays unfiled until a transmission is accepted, which is the '
   +'reason to clear the cause rather than leave it.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T71 = dict(
 slug='efile-rejection-reason-checker',
 # Hard rule 1 reserves EFILE for the phrase "registered EFILE electronic
 # filer". This page first shipped as "EFILE Rejection Reason Checker",
 # which gate_rank_math.py refused: the word is a Canada Revenue Agency
 # mark, and using it as a product name is the thing the rule exists to
 # stop. The live mandatory-t2-efile-checker already writes "E-Filing" in
 # its visible wording, so this follows that. The slug keeps efile, as that
 # one does.
 title='E-Filing Rejection Reason Checker | What Refused the Return',
 h1_pre='E-Filing Rejection ', h1_span='Reason Checker',
 h1='E-Filing Rejection Reason Checker',
 eyebrow='Transmission',
 keyword='t2 efile rejection checker',
 meta=('A refused transmission is usually one of four identifier mismatches. '
       'Four answers name the cause and what clears it.'),
 tags=['Four answers', 'Names the cause', 'Says what clears it',
       'One corrected transmission included'],
 form=tool('What the return carries',
           [yn('nm', 'Does the corporation name on the return match the '
                     'register exactly?'),
            yn('ye', 'Does the fiscal year-end match the record the Canada '
                     'Revenue Agency holds?'),
            yn('bn', 'Is the Business Number the one on the corporation '
                     'record?'),
            yn('fl', 'Has this tax year already been filed and assessed?')],
           'Answer the four questions above.'),
 js=None,
 sections=[
  ('what-a-rejection-is', 'A Rejection Is Not an Assessment',
   '<p>A refused transmission means the return was never received, so the tax '
   'year stays exactly as open as it was before. Nothing is assessed, nothing '
   'is charged for the refusal itself, and no record of it reaches the '
   'corporation&rsquo;s account.</p>\n'
   '<p>That is the reason a rejection is worth clearing rather than leaving. '
   'It reads like a setback and it is really an unfiled year with a note '
   'attached saying which field to fix.</p>'),
  ('the-four-causes', 'The Four Identifier Mismatches',
   _tbl(['Cause', 'Where the right value comes from', 'What clears it'],
        [['The legal name does not match the register',
          'The register the corporation was incorporated under',
          'Transmit the exact legal name, corporation number and suffix '
          'included'],
         ['The fiscal year-end does not match the Agency record',
          'The incorporation record the Canada Revenue Agency holds',
          'Settle the year-end with the Agency, then transmit'],
         ['The Business Number is not the corporation&rsquo;s own',
          'The corporation&rsquo;s own Canada Revenue Agency record',
          'Confirm the Business Number against the corporation name'],
         ['The year has already been filed and assessed',
          'The assessment already on the account',
          'An assessed year is adjusted rather than refiled']])
   + '\n<p>The '
   + a(T + 'business-number-versus-corporation-number-checker/',
       'Business Number versus corporation number checker')
   + ' separates the two identifiers these mismatches confuse, and the '
   + a(T + 'mandatory-t2-efile-checker/', 'mandatory T2 e-filing checker')
   + ' covers which tax years have to be transmitted electronically at '
   'all.</p>'),
  ('what-the-fee-covers', 'One Corrected Transmission Is Inside the Fee',
   '<p>Where a first transmission is refused, we read the rejection, correct '
   'the return and transmit it again, and that second transmission is '
   'included in ' + PRICE + ' rather than charged separately.</p>\n'
   '<p>What is not inside the fee is an adjustment to a year that has already '
   'been assessed. That is a different filing on a year that is already '
   'closed, and we say so before you pay rather than after.</p>'),
 ],
 faq=[
  ('Why was my T2 rejected?',
   'Most often one of four identifier mismatches: the legal name does not '
   'match the register, the fiscal year-end does not match the record the '
   'Canada Revenue Agency holds, the Business Number is not the '
   'corporation&rsquo;s own, or the year has already been filed. The checker '
   'names which of the four applies to you.'),
  ('Does a rejected return count as filed?',
   'No. A refused transmission was never received, so the tax year stays '
   'open and unfiled until a transmission is accepted. Nothing is assessed '
   'and nothing is charged for the refusal itself.'),
  ('Do I pay again to transmit a corrected return?',
   'No. One corrected transmission is included in ' + PRICE + '. An '
   'adjustment to a year that has already been assessed is a different '
   'filing and is not covered.'),
 ],
)


# ----------------------------------------------------------- 72. expenses only
T72_JS = RBASE + r"""
function expenses(rv,it,ex){
  if(rv===null||it===null||ex===null){return null;}
  return {rev:rv==='y',int:it==='y',exp:ex==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=expenses(pick('rv'),pick('it'),pick('ex'));
  if(r===null){out.innerHTML='<p>Answer the three questions above.</p>';
    return;}
  var h,income=r.rev||r.int;
  h='<h3>'+(income?'The year is not nil, because something came in'
   :'Costs alone leave the year nil')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">What the year held</th>'
   +'<th scope="col">Your answer</th><th scope="col">Effect on the nil '
   +'test</th></tr></thead><tbody>';
  h+='<tr><td>Revenue of any kind</td><td>'+(r.rev?'Yes':'No')+'</td><td>'
   +(r.rev?'Ends the nil year':'Nothing to report')+'</td></tr>';
  h+='<tr><td>Interest credited on a balance</td><td>'+(r.int?'Yes':'No')
   +'</td><td>'+(r.int?'Investment income, so the year is not nil'
   :'Nothing to report')+'</td></tr>';
  h+='<tr><td>Costs paid out</td><td>'+(r.exp?'Yes':'No')+'</td><td>'
   +(r.exp?'Does not end the nil year, and makes GIFI Schedules 100, 125 and '
   +'141 required':'Nothing to report')+'</td></tr>';
  h+='</tbody></table>';
  if(income){
    h+='<p>A year with revenue or interest in it is not a nil year, whatever '
     +'the costs were. '+NOTNILJS+'</p>';
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  h+='<p>Money going out does not make a year active. A bank charge, an '
   +'accounting fee or a registry fee is an expense with no revenue against '
   +'it, and the return reports a loss for the year rather than income. That '
   +'is still a nil return for this service at '+PRICE_JS+'.</p>';
  if(r.exp){
    h+='<p>Because something sat on the books, GIFI Schedules 100, 125 and '
     +'141 are required on the return. They are inside the fee rather than '
     +'charged separately, and the loss is carried on the loss continuity '
     +'schedule.</p>';
  }else{
    h+='<p>With nothing in and nothing out, the return still reports the '
     +'balance sheet the corporation carries: share capital, cash or a '
     +'shareholder loan each make the GIFI schedules required on their '
     +'own.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T72 = dict(
 slug='expenses-only-year-checker',
 title='Expenses Only Year Checker | Costs but No Income',
 h1_pre='Expenses Only ', h1_span='Year Checker',
 h1='Expenses Only Year Checker',
 eyebrow='Is It Nil',
 keyword='expenses only year checker',
 meta=('A year with costs and no revenue is still a nil year. Three answers '
       'confirm it and name the schedules it triggers.'),
 tags=['Three answers', 'Costs do not end a nil year',
       'Names the GIFI trigger', 'Interest does end it'],
 form=tool('What the year held',
           [yn('rv', 'Did the corporation receive revenue of any kind?'),
            yn('it', 'Was any interest credited on a bank balance?'),
            yn('ex', 'Were any costs paid, such as a bank charge or a filing '
                     'fee?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('money-out-is-not-activity', 'Money Going Out Is Not Activity',
   '<p>A corporation that paid a bank charge, an annual registry fee or an '
   'accounting bill, and took nothing in, had no activity in the sense the '
   'nil test uses. The return reports expenses against no revenue, which is a '
   'loss for the year rather than income, and it is still a nil return at '
   + PRICE + '.</p>\n'
   '<p>The asymmetry is the part worth stating plainly: what ends a nil year '
   'is something coming in, not something going out.</p>'),
  ('what-each-entry-does', 'What Each Entry Does to the Year',
   _tbl(['What the year held', 'Still nil?',
         'What it does to the return'],
        [['A bank charge or a filing fee', 'Yes',
          'Makes GIFI Schedules 100, 125 and 141 required'],
         ['An accounting or legal cost', 'Yes',
          'Reported as an expense, with the loss carried forward'],
         ['Interest credited on a balance', 'No',
          'Investment income, so the year is not nil'],
         ['Revenue of any kind', 'No',
          'Ends the nil year whatever the costs were'],
         ['A dividend paid or received', 'No',
          'Not nil, and handled by gondaliyacpa.ca']])
   + '\n<p>The '
   + a(T + 'nil-gifi-balance-sheet-checker/', 'nil GIFI balance sheet checker')
   + ' shows what Schedule 100 has to carry on a quiet year, and the '
   + a(T + 'dormant-corporation-test/', 'dormant corporation test')
   + ' settles the nil question across every entry at once.</p>'),
  ('the-loss-still-matters', 'The Loss Is Only Real Once the Year Is Filed',
   '<p>A year of costs with no revenue produces a loss, and that loss is only '
   'established by the filed return for that year. Leaving the year unfiled '
   'leaves the loss unestablished, which is the quiet cost of skipping a year '
   'that felt too small to bother with.</p>\n'
   '<p>Schedule 8 and the loss continuity schedule travel with the return and '
   'are inside the fee. The '
   + a(T + 'loss-continuity-on-a-nil-return-checker/',
       'loss continuity on a nil return checker')
   + ' covers what happens to a loss while its year sits unfiled.</p>'),
 ],
 faq=[
  ('Is a year with expenses but no income still nil?',
   'Yes, for this service. Costs going out do not make a year active. What '
   'ends a nil year is something coming in: revenue, interest credited on a '
   'balance, rent or a dividend either way.'),
  ('Do the expenses make extra schedules necessary?',
   'They make GIFI Schedules 100, 125 and 141 required, because something '
   'sat on the books during the year. Those schedules are inside ' + PRICE
   + ' rather than charged separately.'),
  ('What happens to the loss from a year like that?',
   'It is established by the filed return for that year and carried on the '
   'loss continuity schedule. A year left unfiled leaves its loss '
   'unestablished, which is one reason to file a small year rather than skip '
   'it.'),
 ],
)


# -------------------------------------------------------- 73. never traded
T73_JS = RBASE + r"""
function neverTraded(id,ac,fi){
  var d=parse(id);
  if(d===null||d===undefined||ac===null||fi===null){return null;}
  var cap=new Date(d.getTime()+370*86400000);
  return {inc:d,cap:cap,due:dueDate(cap),act:ac==='y',filed:fi==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=neverTraded('ic',pick('ac'),pick('fi'));
  if(r===null){out.innerHTML='<p>Enter the incorporation date and answer '
   +'both questions.</p>';return;}
  var h,fd=filingDate(r.cap);
  h='<h3>'+(r.filed?'The first return is in, so the ordinary cycle has '
   +'started':'A corporation that never traded still owes its first '
   +'return')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Step</th>'
   +'<th scope="col">Date</th></tr></thead><tbody>';
  h+='<tr><td>Incorporated, and the first tax year begins</td><td>'
   +fmt(r.inc)+'</td></tr>';
  h+='<tr><td>Latest first year-end the 53-week limit allows</td><td>'
   +fmt(r.cap)+'</td></tr>';
  h+='<tr><td>Return due on that year-end</td><td>'+fmt(r.due)+'</td></tr>';
  if(fd.getTime()!==r.due.getTime()){
    h+='<tr><td>Received on time where the due date is a closed day</td>'
     +'<td>'+fmt(fd)+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>The first tax year begins on the incorporation date whether or not '
   +'anything happens in it, and it cannot exceed 53 weeks. A year-end later '
   +'than '+fmt(r.cap)+' is not available, so the first return is due on the '
   +'chosen year-end at the latest by '+fmt(r.due)+'.</p>';
  if(r.act){
    h+='<p>You answered that the corporation did have activity, so this is '
     +'not a never-traded year. '+NOTNILJS+'</p>';
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  h+='<p>With no activity at all, the first return is a nil return at '
   +PRICE_JS+'. It still carries Schedule 24 because it is a first return, '
   +'and the GIFI schedules where shares were issued or costs were paid.</p>';
  if(!r.filed){
    h+='<p>'+QUALJS+'</p>';
  }else{
    h+='<p>With the first return filed, each later year runs on the same '
     +'year-end and is due six months after it, nil or not.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T73 = dict(
 slug='never-traded-corporation-checker',
 title='Never Traded Corporation Checker | The First Return',
 h1_pre='Never Traded ', h1_span='Corporation Checker',
 h1='Never Traded Corporation Checker',
 eyebrow='First Return',
 keyword='never traded corporation checker',
 meta=('A corporation that never started still owes a first return. This '
       'dates it from the incorporation date and the 53-week limit.'),
 tags=['Computed dates', 'Carries the 53-week limit', 'Schedule 24 included',
       'Three inputs'],
 form=tool('Your corporation',
           [date('ic', 'Date of incorporation'),
            yn('ac', 'Has the corporation had any activity at all since '
                     'then?'),
            yn('fi', 'Has the first T2 been filed?')],
           'Enter the incorporation date and answer both questions.'),
 js=None,
 sections=[
  ('the-clock-starts-at-incorporation', 'The Clock Starts at Incorporation',
   '<p>A corporation that was set up and never used is still a corporation. '
   'Its first tax year begins on the incorporation date, not on the day it '
   'first trades, and the return for that year is due six months after '
   'whichever year-end it adopts.</p>\n'
   '<p>Nothing arrives to prompt anyone, which is why the first contact is '
   'often a demand to file covering several years at once.</p>'),
  ('what-a-first-return-carries', 'What a First Return Carries',
   _tbl(['On the return', 'Needed on a never-traded year?', 'Why'],
        [['Schedule 24, first-time filer information', 'Yes',
          'It is a first return, whatever happened in the year'],
         ['GIFI Schedules 100, 125 and 141', 'Where shares were issued or '
          'costs were paid',
          'Share capital, cash or an incorporation cost puts a balance on '
          'the books'],
         ['Schedule 50, shareholder information', 'Where a shareholder holds '
          '10 per cent or more',
          'A single shareholder holds 100 per cent, so Schedule 50 applies'],
         ['The T2 Short', 'Where every condition holds',
          'Included in the fee rather than charged separately']])
   + '\n<p>The '
   + a(T + '53-week-first-tax-year-checker/', '53-week first tax year checker')
   + ' tests a proposed year-end against the limit, and the '
   + a(T + 'first-t2-year-end-options-generator/',
       'first T2 year-end options generator')
   + ' lists every month-end the first year may use.</p>'),
  ('a-shelf-corporation-is-the-same', 'A Parked Corporation Is No Different',
   '<p>A corporation incorporated to hold a name, a structure or a single '
   'asset is on the same footing as one that trades. Every year since '
   'incorporation is a tax year, and each one is its own return at ' + PRICE
   + '.</p>\n'
   '<p>Where several of those years are outstanding, they are filed oldest '
   'first, because a T2 carries figures forward from the year before it. The '
   + a(T + 'catch-up-filing-schedule-generator/',
       'catch-up filing schedule generator')
   + ' lays them out in order.</p>'),
 ],
 faq=[
  ('Does a corporation that never traded have to file?',
   'Yes. The first tax year begins on the incorporation date whether or not '
   'anything happened in it, and a T2 is due six months after the year-end. '
   'With no activity the return is nil, at ' + PRICE + '.'),
  ('How late can the first year-end be?',
   'The first tax year cannot exceed 53 weeks from the incorporation date, so '
   'the checker dates the latest year-end the limit allows and the return due '
   'on it.'),
  ('Does a never-traded first return still need schedules?',
   'Schedule 24 is on every first return. The GIFI schedules are required '
   'where shares were issued or any cost was paid, and Schedule 50 applies to '
   'any shareholder at 10 per cent or more, which a sole shareholder always '
   'is.'),
 ],
)


# ------------------------------------------------------ 74. restarting dormant
T74_JS = RBASE + r"""
function restart(rs,rv,qy){
  if(rs===null){return null;}
  if(rs==='n'){if(qy===null){return null;}return {resumed:false,
    quiet:qy==='y'};}
  if(rv===null||qy===null){return null;}
  return {resumed:true,received:rv==='y',quiet:qy==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=restart(pick('rs'),pick('rv'),pick('qy'));
  if(r===null){out.innerHTML='<p>Answer the questions above.</p>';return;}
  var h;
  h='<h3>'+(!r.resumed?'Still dormant, so every year is a nil year'
   :(r.received?'The year it restarted is not a nil year'
   :'Restarted, but nothing has come in yet'))+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Year</th>'
   +'<th scope="col">Nil?</th><th scope="col">Who files it</th></tr>'
   +'</thead><tbody>';
  h+='<tr><td>Each quiet year before the restart</td><td>Yes</td>'
   +'<td>Filed here at '+PRICE_JS+'</td></tr>';
  if(r.resumed){
    h+='<tr><td>The year activity resumed</td><td>'
     +(r.received?'No':'Not yet')+'</td><td>'
     +(r.received?'Gondaliya CPA Professional Corporation at gondaliyacpa.ca'
     :'Filed here while the year stays quiet')+'</td></tr>';
    h+='<tr><td>Every year after it</td><td>No, once trading</td>'
     +'<td>Gondaliya CPA Professional Corporation at gondaliyacpa.ca</td>'
     +'</tr>';
  }else{
    h+='<tr><td>The current year</td><td>Yes</td><td>Filed here at '
     +PRICE_JS+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>Restarting does not reopen the quiet years and it does not close '
   +'them either. Each one is still its own tax year with its own return, and '
   +'a quiet year stays a nil return however active the corporation becomes '
   +'later.</p>';
  if(r.resumed&&r.received){
    h+='<p>The year money started coming in is not nil. '+NOTNILJS+'</p>';
  }
  if(r.quiet){
    h+='<p>You answered that earlier quiet years are still unfiled. Those are '
     +'ours to file, oldest first, each at '+PRICE_JS+'. '+QUALJS+'</p>';
  }else{
    h+='<p>With the earlier quiet years filed, the record is current up to '
     +'the restart and nothing older is outstanding.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T74 = dict(
 slug='restarting-a-dormant-corporation-checker',
 title='Restarting a Dormant Corporation | Which Years Stay Nil',
 h1_pre='Restarting a Dormant ', h1_span='Corporation Checker',
 h1='Restarting a Dormant Corporation Checker',
 eyebrow='Dormant to Active',
 keyword='restarting a dormant corporation checker',
 meta=('Trading again does not change the quiet years behind it. Which years '
       'are still nil returns, and which one is not.'),
 tags=['Three answers', 'Separates the quiet years',
       'Says when it is a referral', 'Covers the unfiled years'],
 form=tool('Where the corporation is now',
           [yn('rs', 'Has the corporation started trading again?'),
            yn('rv', 'Did it receive revenue, rent or a dividend in the year '
                     'it restarted?'),
            yn('qy', 'Are earlier quiet years still unfiled?')],
           'Answer the questions above.'),
 js=None,
 sections=[
  ('the-years-do-not-move', 'The Quiet Years Do Not Move',
   '<p>A corporation that goes back to trading carries its history with it. '
   'The years it spent dormant are still tax years, each with its own return, '
   'and each of those returns is still a nil return however busy the '
   'corporation becomes afterwards.</p>\n'
   '<p>So a restart splits the record rather than resetting it: quiet years '
   'behind, active years ahead, and a line between them that falls on a '
   'year-end rather than on the day the first invoice went out.</p>'),
  ('which-year-goes-where', 'Which Year Goes Where',
   _tbl(['Year', 'Nil?', 'Filed by', 'Fee'],
        [['Each quiet year before the restart', 'Yes',
          'This service', PRICE],
         ['The year activity resumed, if nothing came in yet', 'Yes',
          'This service', PRICE],
         ['The year revenue, rent or a dividend arrived', 'No',
          'Gondaliya CPA Professional Corporation at gondaliyacpa.ca',
          '$350.00 plus HST per year'],
         ['Every year after that, while trading', 'No',
          'Gondaliya CPA Professional Corporation at gondaliyacpa.ca',
          '$350.00 plus HST per year']])
   + '\n<p>The '
   + a(T + 'dormant-corporation-obligation-checker/',
       'dormant corporation obligation checker')
   + ' covers what a dormant year still owes, and the '
   + a(T + 'unfiled-years-checker/', 'unfiled years checker')
   + ' lists which of the quiet years are still open.</p>'),
  ('clear-the-quiet-years-first', 'Clear the Quiet Years First',
   '<p>Where quiet years are still outstanding, they are filed oldest first, '
   'because a T2 carries figures forward from the year before it. Filing the '
   'active year on top of a gap leaves the gap exactly where it was.</p>\n'
   '<p>' + QUAL + '</p>'),
 ],
 faq=[
  ('Does restarting a dormant corporation change the old years?',
   'No. Each dormant year is still its own tax year with its own return, and '
   'each is still a nil return at ' + PRICE + '. Trading again changes the '
   'years ahead, not the years behind.'),
  ('Who files the year the corporation restarted?',
   'If revenue, rent or a dividend arrived in that year, it is not a nil year '
   'and it is handled by Gondaliya CPA Professional Corporation at '
   'gondaliyacpa.ca at $350.00 plus HST per year. If nothing came in yet, it '
   'is still a nil return here.'),
  ('Should the quiet years be filed before the active one?',
   'Yes, oldest first. A T2 carries figures forward from the year before it, '
   'so the years are assessed in the order they fell due and a gap left '
   'behind stays open.'),
 ],
)


# ----------------------------------------------------------- 75. loss continuity
T75_JS = RBASE + r"""
function lossPos(pl,lf,cn){
  if(pl===null){return null;}
  if(pl==='n'){if(cn===null){return null;}return {loss:false,nil:cn==='y'};}
  if(lf===null||cn===null){return null;}
  return {loss:true,filed:lf==='y',nil:cn==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=lossPos(pick('pl'),pick('lf'),pick('cn'));
  if(r===null){out.innerHTML='<p>Answer the questions above.</p>';return;}
  var h;
  h='<h3>'+(!r.loss?'No earlier loss to carry, so nothing is continued'
   :(r.filed?'The loss is established, and the schedule travels with every '
   +'return':'The loss is not established until its own year is filed'))
   +'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Your answer</th><th scope="col">What follows</th></tr>'
   +'</thead><tbody>';
  h+='<tr><td>An earlier year produced a loss</td><td>'
   +(r.loss?'Yes':'No')+'</td><td>'+(r.loss?'There is a balance to carry '
   +'forward':'Nothing to carry forward')+'</td></tr>';
  if(r.loss){
    h+='<tr><td>The return for that loss year is filed</td><td>'
     +(r.filed?'Yes':'Not yet')+'</td><td>'+(r.filed?'The loss is on the '
     +'record and continues year to year':'The loss is not established, '
     +'because a year is only established by its own filed return')
     +'</td></tr>';
  }
  h+='<tr><td>This year is nil</td><td>'+(r.nil?'Yes':'No')+'</td><td>'
   +(r.nil?'A nil year uses none of the loss and still reports the balance'
   :'A year with income is not one we file here')+'</td></tr>';
  h+='</tbody></table>';
  if(r.loss&&!r.filed){
    h+='<p>So the order matters: file the loss year first, then the years '
     +'after it, oldest first. Each is its own return at '+PRICE_JS+'.</p>';
    h+='<p>'+QUALJS+'</p>';
  }else if(r.loss){
    h+='<p>A nil year claims nothing against the loss, because there is no '
     +'income to claim it against. The balance is still reported, which is '
     +'what keeps it on the record for a year that can use it.</p>';
  }else{
    h+='<p>With no earlier loss, the loss continuity schedule carries nothing '
     +'and the return reports a nil balance. That is still a line on the '
     +'return rather than an omission.</p>';
  }
  if(!r.nil){
    h+='<p>You answered that this year is not nil. '+NOTNILJS+'</p>';
  }else{
    h+='<p>Schedule 8 and the loss continuity schedule are inside '+PRICE_JS
     +' rather than charged separately.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T75 = dict(
 slug='loss-continuity-on-a-nil-return-checker',
 title='Loss Continuity on a Nil Return | What Carries Forward',
 h1_pre='Loss Continuity on a ', h1_span='Nil Return Checker',
 h1='Loss Continuity on a Nil Return Checker',
 eyebrow='Schedules',
 keyword='loss continuity on a nil return',
 meta=('A nil year claims nothing against a loss and still reports it. What '
       'an unfiled loss year does to the balance.'),
 tags=['Three answers', 'Covers an unfiled loss year',
       'Schedule 8 inside the fee', 'Says what a nil year reports'],
 form=tool('Your loss position',
           [yn('pl', 'Did an earlier year produce a loss to carry forward?'),
            yn('lf', 'Has the return for that loss year been filed?'),
            yn('cn', 'Is the year you are filing now a nil year?')],
           'Answer the questions above.'),
 js=None,
 sections=[
  ('a-loss-is-made-by-a-return', 'A Loss Is Established by a Filed Return',
   '<p>A loss is not a fact about a year. It is a figure reported on the '
   'return for that year, which means a year left unfiled leaves its loss '
   'unestablished however clearly the books show it.</p>\n'
   '<p>That is the quiet cost of skipping a small year. The expense was real, '
   'the loss was real, and without the return there is nothing on the record '
   'to carry forward to a year that could use it.</p>'),
  ('what-a-nil-year-reports', 'What a Nil Year Does With a Loss',
   _tbl(['Position', 'On the nil return', 'Inside the fee?'],
        [['An earlier loss, its year filed',
          'Reported on the loss continuity schedule and carried forward',
          'Yes'],
         ['An earlier loss, its year unfiled',
          'Nothing to carry: file that year first, oldest first',
          'Yes, each year at its own fee'],
         ['A loss arising this year, from costs with no revenue',
          'Established by this return and carried forward', 'Yes'],
         ['No loss at all', 'The schedule reports a nil balance', 'Yes'],
         ['Income this year to claim a loss against',
          'Not a nil year, so not one we file', 'No']])
   + '\n<p>The '
   + a(T + 'schedule-8-cca-requirement-checker/',
       'Schedule 8 CCA requirement checker')
   + ' covers the depreciable property side of the same schedule set, and the '
   + a(T + 'required-schedules-checker/', 'required schedules checker')
   + ' lists the whole set a nil return carries.</p>'),
  ('nothing-is-claimed-on-a-nil-year', 'A Nil Year Claims Nothing',
   '<p>A nil year has no income, so there is nothing for a loss to be applied '
   'against and nothing is claimed. The balance is reported and carried, '
   'which is the only thing a nil year can usefully do with it.</p>\n'
   '<p>Schedule 8 and the loss continuity schedule are inside ' + PRICE
   + '. What falls outside is a year with income in it, which is not a nil '
   'return and is handled by Gondaliya CPA Professional Corporation at '
   'gondaliyacpa.ca at $350.00 plus HST per year.</p>'),
 ],
 faq=[
  ('Does a nil return still carry the loss continuity schedule?',
   'Yes. The schedule reports the balance carried forward even where the year '
   'claims nothing against it, and a nil balance is reported as a nil '
   'balance. It is inside ' + PRICE + '.'),
  ('What happens to a loss while its year is unfiled?',
   'It is not established. A year is only established by its own filed '
   'return, so the loss has nothing on the record to carry forward from. '
   'Filing that year, oldest first, is what puts it there.'),
  ('Can a nil year use an earlier loss?',
   'There is nothing to use it against. A nil year has no income, so the '
   'balance is reported and carried rather than claimed.'),
 ],
)


# --------------------------------------------------- 76. multiple corporations
T76_JS = RBASE + MONEY_JS + r"""
function multi(ncId,nyId,sm){
  var nc=document.getElementById(ncId).value;
  var ny=document.getElementById(nyId).value;
  if(nc===''||ny===''||sm===null){return null;}
  nc=parseInt(nc,10);ny=parseInt(ny,10);
  if(isNaN(nc)||isNaN(ny)){return undefined;}
  if(nc<1||nc>20||ny<1||ny>10){return 'range';}
  return {nc:nc,ny:ny,returns:nc*ny,cents:nc*ny*30000,same:sm==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=multi('nc','ny',pick('sm'));
  if(r===null){out.innerHTML='<p>Enter both counts and answer the '
   +'question.</p>';return;}
  if(r===undefined){out.innerHTML='<p class="ei-err">Enter whole numbers.</p>';
    return;}
  if(r==='range'){out.innerHTML='<p class="ei-err">Enter 1 to 20 '
   +'corporations and 1 to 10 years each.</p>';return;}
  var h;
  h='<h3>'+plural(r.returns,'nil return')+', '+money(r.cents)
   +' before tax</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Item</th>'
   +'<th scope="col">Figure</th></tr></thead><tbody>';
  h+='<tr><td>Corporations</td><td>'+r.nc+'</td></tr>';
  h+='<tr><td>Quiet tax years each</td><td>'+r.ny+'</td></tr>';
  h+='<tr><td>Returns owed in total</td><td>'+r.returns+'</td></tr>';
  h+='<tr><td>Price per tax year</td><td>'+money(30000)+' plus HST</td></tr>';
  h+='<tr><td>Total before tax</td><td>'+money(r.cents)+'</td></tr>';
  h+='</tbody></table>';
  h+='<p>Each corporation is a separate taxpayer and each tax year is a '
   +'separate return, so '+r.returns+' returns carry the fee '+r.returns
   +' times. There is no reduced rate for filing several corporations or '
   +'several years together: each return is prepared, reviewed by a CPA and '
   +'transmitted on its own.</p>';
  if(r.same){
    h+='<p>With the same fiscal year-end across all '+r.nc+', every return '
     +'falls due on the same date, six months after that year-end. One date '
     +'to hold rather than '+r.nc+'.</p>';
  }else{
    h+='<p>With different year-ends, each corporation has its own deadline '
     +'six months after its own year-end, so there are up to '+r.nc
     +' dates to hold rather than one.</p>';
  }
  h+='<p>'+QUALJS+'</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T76 = dict(
 slug='multiple-corporation-filing-cost-calculator',
 title='Multiple Corporation Filing Cost | Returns and Total',
 h1_pre='Multiple Corporation ', h1_span='Filing Cost Calculator',
 h1='Multiple Corporation Filing Cost Calculator',
 eyebrow='Cost',
 keyword='multiple corporation filing cost calculator',
 meta=('Several quiet corporations, each with its own years. The number of '
       'returns owed and the total before tax.'),
 tags=['Computed total', 'Per corporation and per year',
       'No bulk rate', 'Covers the deadlines'],
 form=tool('Your corporations',
           [num('nc', 'How many quiet corporations?', '1 to 20', 1, 20, '3'),
            num('ny', 'How many unfiled tax years each?', '1 to 10', 1, 10,
                '2'),
            yn('sm', 'Do they all share the same fiscal year-end?')],
           'Enter both counts and answer the question.'),
 js=None,
 sections=[
  ('each-one-is-its-own-taxpayer', 'Each Corporation Is Its Own Taxpayer',
   '<p>Holding several quiet corporations does not consolidate them. Each is '
   'its own taxpayer with its own Business Number, its own fiscal year-end '
   'and its own return for every tax year it has existed, and the fee is '
   + PRICE + ' on each of those returns.</p>\n'
   '<p>So the arithmetic is corporations multiplied by years, which is the '
   'figure people are usually surprised by when they own three or four '
   'dormant companies rather than one.</p>'),
  ('the-arithmetic', 'What the Multiplication Looks Like',
   _tbl(['Corporations', 'Quiet years each', 'Returns', 'Before tax'],
        [['1', '2', '2', '$600.00'],
         ['2', '2', '4', '$1,200.00'],
         ['3', '3', '9', '$2,700.00'],
         ['5', '1', '5', '$1,500.00'],
         ['5', '5', '25', '$7,500.00']])
   + '\n<p>There is no reduced rate for several corporations or several years '
   'in one sitting: every return is prepared, reviewed and transmitted on its '
   'own. The '
   + a(T + 'unfiled-years-cost-calculator/', 'unfiled years cost calculator')
   + ' prices one corporation across its years, and the '
   + a(T + 'dissolve-or-keep-filing-cost-calculator/',
       'dissolve or keep filing cost calculator')
   + ' sets years of filing against winding one up.</p>'),
  ('the-dates-multiply-too', 'The Deadlines Multiply as Well',
   '<p>Where the corporations share a fiscal year-end, every return falls due '
   'on the same date, six months after it. Where they do not, each has its '
   'own deadline and there are as many dates to hold as there are '
   'corporations.</p>\n'
   '<p>The '
   + a(T + 'corporate-deadline-calendar-generator/',
       'corporate deadline calendar generator')
   + ' dates one corporation&rsquo;s year end to end, and running it once per '
   'corporation is the practical way to hold several at once.</p>'),
 ],
 faq=[
  ('Is there a discount for filing several corporations?',
   'No. ' + PRICE + ' is charged per tax year per corporation, because each '
   'return is prepared, reviewed by a CPA and transmitted separately. Five '
   'corporations with one quiet year each is five returns.'),
  ('Can several corporations be filed on one form?',
   'Each corporation is filed as its own return against its own Business '
   'Number. The calculator totals them so the figure is known before any of '
   'them starts.'),
  ('Do they all share a deadline?',
   'Only where they share a fiscal year-end. Otherwise each return is due six '
   'months after that corporation&rsquo;s own year-end.'),
 ],
)


# ------------------------------------------------------- 77. post dissolution
T77_JS = RBASE + r"""
function postDis(id,fn,ea){
  var d=parse(id);
  if(d===null||d===undefined||fn===null||ea===null){return null;}
  return {dd:d,due:dueDate(d),final:fn==='y',earlier:ea==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=postDis('dd',pick('fn'),pick('ea'));
  if(r===null){out.innerHTML='<p>Enter the dissolution date and answer both '
   +'questions.</p>';return;}
  var h,fd=filingDate(r.dd);
  h='<h3>'+(r.final&&!r.earlier?'Nothing further arises after the '
   +'dissolution date':'What is still owed up to the dissolution date')
   +'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Period</th>'
   +'<th scope="col">Return owed?</th><th scope="col">Deadline</th></tr>'
   +'</thead><tbody>';
  h+='<tr><td>Each full tax year before the final one</td><td>'
   +(r.earlier?'Yes, still outstanding':'Filed')+'</td>'
   +'<td>Six months after each year-end</td></tr>';
  h+='<tr><td>The final period, ending '+fmt(r.dd)+'</td><td>'
   +(r.final?'Filed':'Yes, the final T2')+'</td><td>'+fmt(r.due)
   +'</td></tr>';
  if(fd.getTime()!==r.due.getTime()){
    h+='<tr><td>Where that deadline falls on a closed day</td>'
     +'<td>Received on time by</td><td>'+fmt(fd)+'</td></tr>';
  }
  h+='<tr><td>Any period after '+fmt(r.dd)+'</td><td>No</td>'
   +'<td>No tax year arises, so there is nothing to file</td></tr>';
  h+='</tbody></table>';
  h+='<p>A dissolved corporation stops having tax years. The final period '
   +'ends on the dissolution date and its return is due six months later, on '
   +fmt(r.due)+'. After that date there is no year to report, which is the '
   +'one piece of good news in a wind-up.</p>';
  if(!r.final){
    h+='<p>The final T2 is still outstanding. Where that final period had no '
     +'activity it is a nil return at '+PRICE_JS+'.</p>';
  }
  if(r.earlier){
    h+='<p>Earlier years are also outstanding, and those come first: a T2 '
     +'carries figures forward, so they are filed oldest first and the final '
     +'return goes last. Unfiled years block a clearance certificate and the '
     +'dissolution itself.</p>';
    h+='<p>'+QUALJS+'</p>';
  }else{
    h+='<p>With the earlier years filed, the final return is the last one the '
     +'corporation owes.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T77 = dict(
 slug='post-dissolution-return-checker',
 title='Post-Dissolution Return Checker | What Is Still Owed',
 h1_pre='Post-Dissolution ', h1_span='Return Checker',
 h1='Post-Dissolution Return Checker',
 eyebrow='Wind-Up',
 keyword='post dissolution return checker',
 meta=('A dissolved corporation stops having tax years. Which periods are '
       'still owed up to the dissolution date, and which never arise.'),
 tags=['Computed deadline', 'Says what never arises',
       'Covers the earlier years', 'Three inputs'],
 form=tool('The wind-up',
           [date('dd', 'Date of dissolution'),
            yn('fn', 'Has the final T2 to that date been filed?'),
            yn('ea', 'Are any earlier tax years still unfiled?')],
           'Enter the dissolution date and answer both questions.'),
 js=None,
 sections=[
  ('the-years-stop', 'The Tax Years Stop at the Dissolution Date',
   '<p>Dissolution ends the corporation, and with it the sequence of tax '
   'years. The final period runs to the dissolution date and its return is '
   'due six months after that date. No period after it is a tax year, so '
   'there is nothing further to file.</p>\n'
   '<p>What dissolution does not do is clear what came before. A year that '
   'was unfiled on the day of dissolution is unfiled afterwards, and it is '
   'still the corporation&rsquo;s year.</p>'),
  ('which-periods-are-owed', 'Which Periods Are Owed and Which Are Not',
   _tbl(['Period', 'Return owed?', 'Deadline'],
        [['Each full tax year before the final one', 'Yes, until filed',
          'Six months after each year-end'],
         ['The final period, ending on the dissolution date',
          'Yes, the final T2', 'Six months after the dissolution date'],
         ['Any period after the dissolution date', 'No',
          'No tax year arises'],
         ['A year already filed and assessed', 'No',
          'Closed, unless adjusted']])
   + '\n<p>The '
   + a(T + 'final-t2-return-due-date-calculator/',
       'final T2 return due date calculator')
   + ' dates the final return on its own, and the '
   + a(T + 'dissolution-timeline-calculator/', 'dissolution timeline calculator')
   + ' puts it in the order of the wind-up steps around it.</p>'),
  ('why-the-order-matters', 'The Earlier Years Come First',
   '<p>A T2 carries figures forward from the year before it, so outstanding '
   'years are filed oldest first and the final return goes last. Filing the '
   'final return on top of a gap leaves the gap where it was, and an unfiled '
   'year blocks both a clearance certificate and the dissolution itself.</p>\n'
   '<p>' + QUAL + '</p>'),
 ],
 faq=[
  ('Does a dissolved corporation owe returns for later years?',
   'No. The final period ends on the dissolution date and no tax year arises '
   'after it, so there is nothing further to file.'),
  ('When is the final T2 due?',
   'Six months after the date of dissolution. Where that date falls on a '
   'Saturday, a Sunday or a public holiday recognised by the Canada Revenue '
   'Agency, a return received by the next business day is on time.'),
  ('Does dissolution clear the years that were never filed?',
   'No. Those years stay open and stay the corporation&rsquo;s, and they '
   'block a clearance certificate and the dissolution itself until they are '
   'filed.'),
 ],
)


# ----------------------------------------------------- 78. acquired corporation
T78_JS = RBASE + r"""
function acquired(incId,acqId,fl){
  var inc=parse(incId),acq=parse(acqId);
  if(inc===null||inc===undefined||acq===null||acq===undefined||fl===null){
    return null;}
  if(acq.getTime()<inc.getTime()){return 'order';}
  var held=Math.floor(spanDays(inc,acq)/365);
  var since=Math.floor(spanDays(acq,today())/365);
  return {inc:inc,acq:acq,before:held,after:since,filed:fl==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=acquired('ic','aq',pick('fl'));
  if(r===null){out.innerHTML='<p>Enter both dates and answer the '
   +'question.</p>';return;}
  if(r==='order'){out.innerHTML='<p class="ei-err">The acquisition date '
   +'cannot fall before the incorporation date.</p>';return;}
  var h;
  h='<h3>'+(r.filed?'The record is current, so only the years ahead are '
   +'yours to hold':'The outstanding years came with the corporation')
   +'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Period</th>'
   +'<th scope="col">Whose years</th><th scope="col">Still owed?</th></tr>'
   +'</thead><tbody>';
  h+='<tr><td>Incorporated '+fmt(r.inc)+' to '+fmt(r.acq)+', about '
   +plural(r.before,'tax year')+'</td><td>The corporation&rsquo;s, under the '
   +'previous owner</td><td>'+(r.filed?'Filed':'Yes, until each is filed')
   +'</td></tr>';
  h+='<tr><td>Since '+fmt(r.acq)+', about '+plural(r.after,'tax year')
   +'</td><td>The corporation&rsquo;s, under you</td><td>Yes, as each falls '
   +'due</td></tr>';
  h+='<tr><td>Any year already filed and assessed</td><td>The '
   +'corporation&rsquo;s</td><td>No, closed unless adjusted</td></tr>';
  h+='</tbody></table>';
  h+='<p>A tax account belongs to the corporation rather than to whoever owns '
   +'it, so buying the shares buys the filing history with them. An unfiled '
   +'year from before the purchase is still outstanding on the same account '
   +'the new returns go to.</p>';
  if(!r.filed){
    h+='<p>Those years are filed oldest first, because a T2 carries figures '
     +'forward from the year before it. Each quiet year is a nil return at '
     +PRICE_JS+'.</p>';
    h+='<p>'+QUALJS+'</p>';
  }else{
    h+='<p>With the earlier years filed, what remains is the ordinary cycle: '
     +'one return per tax year, due six months after each year-end, nil or '
     +'not.</p>';
  }
  h+='<p>The year count here is approximate, because it is measured in whole '
   +'years from the dates you entered rather than against the fiscal year-end '
   +'the Canada Revenue Agency holds. This tool answers the filing question '
   +'only: buying a corporation has wider tax consequences that it does not '
   +'decide.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T78 = dict(
 slug='acquired-corporation-unfiled-years-checker',
 title='Acquired Corporation Unfiled Years | What Came With It',
 h1_pre='Acquired Corporation ', h1_span='Unfiled Years Checker',
 h1='Acquired Corporation Unfiled Years Checker',
 eyebrow='Change of Owner',
 keyword='acquired corporation unfiled years checker',
 meta=('A tax account belongs to the corporation, not its owner. Which years '
       'came with the purchase and which are yours.'),
 tags=['Two dates in', 'Splits the years at the purchase',
       'Says what it does not decide', 'Covers the catch-up order'],
 form=tool('The corporation you bought',
           [date('ic', 'Date the corporation was incorporated'),
            date('aq', 'Date you acquired it'),
            yn('fl', 'Are all years before the purchase already filed?')],
           'Enter both dates and answer the question.'),
 js=None,
 sections=[
  ('the-account-is-the-corporations', 'The Account Belongs to the Corporation',
   '<p>A corporate tax account is the corporation&rsquo;s, not the '
   'shareholder&rsquo;s. Buying the shares changes who owns the corporation '
   'and changes nothing about the account: the Business Number, the fiscal '
   'year-end and every outstanding year stay exactly where they were.</p>\n'
   '<p>So a quiet corporation bought cheaply can arrive with several unfiled '
   'years attached, and those years are outstanding on the same account the '
   'new owner&rsquo;s returns will go to.</p>'),
  ('which-years-are-whose', 'Which Years Came With It',
   _tbl(['Period', 'Whose years', 'Still owed?'],
        [['From incorporation to the purchase',
          'The corporation&rsquo;s, under the previous owner',
          'Yes, until each one is filed'],
         ['From the purchase onward', 'The corporation&rsquo;s, under you',
          'Yes, as each falls due'],
         ['A year already filed and assessed', 'The corporation&rsquo;s',
          'No, closed unless adjusted'],
         ['A year before incorporation', 'Nobody&rsquo;s',
          'No tax year exists']])
   + '\n<p>The '
   + a(T + 'tax-years-since-incorporation-calculator/',
       'tax years since incorporation calculator')
   + ' counts the years from the incorporation date, and the '
   + a(T + 'unfiled-years-checker/', 'unfiled years checker')
   + ' lists which of them are open.</p>'),
  ('what-this-does-not-decide', 'What This Checker Does Not Decide',
   '<p>Buying a corporation has consequences beyond the filing calendar, and '
   'this tool does not reach them. It answers one question: the outstanding '
   'years belong to the corporation and are still outstanding after it '
   'changes hands.</p>\n'
   '<p>Where a quiet year is outstanding, it is a nil return at ' + PRICE
   + ', filed oldest first. Where a year had activity under either owner, it '
   'is not a nil year and is handled by Gondaliya CPA Professional '
   'Corporation at gondaliyacpa.ca at $350.00 plus HST per year.</p>'),
 ],
 faq=[
  ('Do unfiled years come with a corporation you buy?',
   'Yes. The tax account belongs to the corporation rather than to its owner, '
   'so every outstanding year is still outstanding after the shares change '
   'hands, on the same account the new returns go to.'),
  ('Who is responsible for the previous owner&rsquo;s unfiled years?',
   'The returns are the corporation&rsquo;s to file, and the corporation is '
   'now yours. Each quiet year is a nil return at ' + PRICE + ', filed oldest '
   'first because a T2 carries figures forward.'),
  ('Does the fiscal year-end change when a corporation is sold?',
   'The year-end on the Canada Revenue Agency record is the one the return '
   'has to match, and buying the shares does not change it. A return filed to '
   'a different date is rejected for the year-end.'),
 ],
)


# ------------------------------------------------------- 79. sole shareholder
T79_JS = RBASE + r"""
function sole(on,sh,ln){
  if(on===null||sh===null||ln===null){return null;}
  return {one:on==='y',shares:sh==='y',loan:ln==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=sole(pick('on'),pick('sh'),pick('ln'));
  if(r===null){out.innerHTML='<p>Answer the three questions above.</p>';
    return;}
  var h,gifi=r.shares||r.loan;
  h='<h3>'+(r.one?'One shareholder holds 100 per cent, so Schedule 50 '
   +'applies':'More than one holding, so the 10 per cent test decides')
   +'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Schedule</th>'
   +'<th scope="col">Required?</th><th scope="col">What triggers it</th></tr>'
   +'</thead><tbody>';
  h+='<tr><td>Schedule 50, shareholder information</td><td>'
   +(r.one?'Yes':'For each holding at 10 per cent or more')+'</td>'
   +'<td>'+(r.one?'A single shareholder holds 100 per cent, which is above '
   +'the 10 per cent threshold':'The threshold is 10 per cent, so small '
   +'holdings may fall outside it')+'</td></tr>';
  h+='<tr><td>GIFI Schedules 100, 125 and 141</td><td>'
   +(gifi?'Yes':'Only where something sits on the books')+'</td><td>'
   +(r.shares?'Share capital issued at incorporation sits on the balance '
   +'sheet':(r.loan?'A shareholder loan balance sits on the balance sheet'
   :'Nothing reported on the books in the year'))+'</td></tr>';
  h+='<tr><td>The T2 Short</td><td>Where every condition holds</td>'
   +'<td>Inside '+PRICE_JS+' rather than charged separately</td></tr>';
  h+='</tbody></table>';
  if(r.one){
    h+='<p>A one-person corporation sometimes reads as too small for '
     +'shareholder reporting, and it is the opposite: a sole shareholder '
     +'holds the whole corporation, so the holding is always above the 10 '
     +'per cent threshold and always listed.</p>';
  }else{
    h+='<p>With more than one holding, each is measured against the 10 per '
     +'cent threshold on its own. The '
     +'<a href="/tools/schedule-50-shareholder-threshold-checker/">Schedule '
     +'50 shareholder threshold checker</a> takes the holdings and names who '
     +'has to be listed.</p>';
  }
  if(r.loan){
    h+='<p>A loan balance in either direction makes the GIFI schedules '
     +'required, and it does not stop the year being nil. What it means for '
     +'tax is a separate question this tool does not answer.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T79 = dict(
 slug='sole-shareholder-corporation-checker',
 title='Sole Shareholder Corporation Checker | Schedule 50',
 h1_pre='Sole Shareholder ', h1_span='Corporation Checker',
 h1='Sole Shareholder Corporation Checker',
 eyebrow='Shareholders',
 keyword='sole shareholder corporation checker',
 meta=('A single shareholder holds 100 per cent, which is above the Schedule '
       '50 threshold. What a one-person corporation reports.'),
 tags=['Three answers', 'Schedule 50 always applies',
       'Names the GIFI trigger', 'Inside the fee'],
 form=tool('Your corporation',
           [yn('on', 'Is there exactly one shareholder?'),
            yn('sh', 'Were shares issued at incorporation?'),
            yn('ln', 'Is there a shareholder loan balance in either '
                     'direction?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('one-hundred-per-cent-is-above-ten', 'One Hundred Per Cent Is Above Ten',
   '<p>Schedule 50 lists every shareholder holding 10 per cent or more. A '
   'sole shareholder holds the whole corporation, so the test is met by a '
   'wide margin and the schedule is always on the return.</p>\n'
   '<p>It reads like a rule for corporations with outside investors, and the '
   'one-person company is the case where it most reliably applies.</p>'),
  ('what-a-one-person-return-carries',
   'What a One-Person Nil Return Carries',
   _tbl(['On the return', 'Required?', 'What triggers it'],
        [['Schedule 50, shareholder information', 'Always, for a sole holder',
          'A single shareholder holds 100 per cent'],
         ['GIFI Schedules 100, 125 and 141',
          'Where anything sits on the books',
          'Share capital, cash, a shareholder loan or a cost paid'],
         ['Schedule 24, first-time filer information', 'On a first return',
          'The corporation&rsquo;s first tax year'],
         ['The T2 Short', 'Where every condition holds',
          'Inside the fee rather than charged separately'],
         ['Schedule 8 and loss continuity', 'Where there is a balance',
          'Depreciable property or a loss carried forward']])
   + '\n<p>The '
   + a(T + 'schedule-50-shareholder-threshold-checker/',
       'Schedule 50 shareholder threshold checker')
   + ' measures several holdings against the threshold, and the '
   + a(T + 'shareholder-register-completeness-checker/',
       'shareholder register completeness checker')
   + ' checks what the register has to hold for each one.</p>'),
  ('the-loan-is-a-reporting-question',
   'The Shareholder Loan Is a Reporting Question Here',
   '<p>A balance owed either way makes the GIFI schedules required, and it '
   'does not stop the year being nil. That is the reporting answer, and it is '
   'the one these pages give.</p>\n'
   '<p>What a loan balance means for tax turns on periods and a rate this '
   'service does not carry, so it is not answered here rather than answered '
   'badly. The '
   + a(T + 'due-to-versus-due-from-shareholder-checker/',
       'due to versus due from shareholder checker')
   + ' shows which side of the balance sheet the balance sits on.</p>'),
 ],
 faq=[
  ('Does a one-person corporation file Schedule 50?',
   'Yes. The schedule lists every shareholder at 10 per cent or more, and a '
   'sole shareholder holds 100 per cent, so the holding is always listed.'),
  ('Do shares issued at incorporation make the GIFI schedules necessary?',
   'Yes. Share capital sits on the balance sheet, which makes GIFI Schedules '
   '100, 125 and 141 required even on a year with no activity. They are '
   'inside ' + PRICE + '.'),
  ('Does a shareholder loan stop the year being nil?',
   'No. A balance in either direction makes the GIFI schedules required and '
   'leaves the year nil. What the loan means for tax is a separate question '
   'this service does not answer.'),
 ],
)


# ------------------------------------------- 80. Business Number vs corp number
T80_JS = RBASE + r"""
function numbers(bn,cn,nm){
  if(bn===null||cn===null||nm===null){return null;}
  return {bn:bn==='y',cn:cn==='y',name:nm==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=numbers(pick('bn'),pick('cn'),pick('nm'));
  if(r===null){out.innerHTML='<p>Answer the three questions above.</p>';
    return;}
  var h,both=r.bn&&r.cn;
  h='<h3>'+(both?'You have both identifiers, and each goes on its own filing'
   :(r.bn?'The Business Number is the one the T2 needs'
   :'The T2 needs the Business Number, which you do not have yet'))+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Filing</th>'
   +'<th scope="col">Identifier it uses</th><th scope="col">Do you have '
   +'it?</th></tr></thead><tbody>';
  h+='<tr><td>The T2 corporate income tax return</td><td>The Business '
   +'Number, issued by the Canada Revenue Agency</td><td>'
   +(r.bn?'Yes':'Not yet')+'</td></tr>';
  h+='<tr><td>The registry annual return</td><td>The corporation number, '
   +'issued by the register</td><td>'+(r.cn?'Yes':'Not yet')+'</td></tr>';
  h+='<tr><td>Either filing</td><td>The exact legal name on the register'
   +'</td><td>'+(r.name?'Matches':'Does not match')+'</td></tr>';
  h+='</tbody></table>';
  h+='<p>The two numbers come from two bodies and do different work. The '
   +'Business Number identifies the corporation to the Canada Revenue Agency '
   +'and carries its program accounts. The corporation number identifies it '
   +'to the register it was incorporated under. Neither one substitutes for '
   +'the other on a filing.</p>';
  if(!r.bn){
    h+='<p>A T2 cannot be transmitted without the Business Number. Where you '
     +'do not have it to hand, we take the corporation name and date of '
     +'incorporation on the filing form and confirm the number against the '
     +'corporation record before the return is prepared.</p>';
  }
  if(!r.name){
    h+='<p>A name that does not match the register is one of the common '
     +'causes of a refused transmission, whichever number is on the return. '
     +'The <a href="/tools/efile-rejection-reason-checker/">e-filing '
     +'rejection reason checker</a> names the mismatch and what clears it, and one '
     +'corrected transmission is included in '+PRICE_JS+'.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T80 = dict(
 slug='business-number-versus-corporation-number-checker',
 title='Business Number vs Corporation Number | Which Goes Where',
 h1_pre='Business Number Versus ', h1_span='Corporation Number Checker',
 h1='Business Number Versus Corporation Number Checker',
 eyebrow='Two Identifiers',
 keyword='business number versus corporation number',
 meta=('Two numbers from two bodies, doing different work. Which one the T2 '
       'needs and which one the registry filing needs.'),
 tags=['Three answers', 'Separates the two numbers',
       'Covers the name match', 'Says what we look up for you'],
 form=tool('What you have to hand',
           [yn('bn', 'Do you have the Business Number the Canada Revenue '
                     'Agency issued?'),
            yn('cn', 'Do you have the corporation number from the register?'),
            yn('nm', 'Does the legal name you hold match the register '
                     'exactly?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('two-numbers-two-bodies', 'Two Numbers, Issued by Two Bodies',
   '<p>A corporation carries two identifiers and they are not '
   'interchangeable. The Business Number identifies it to the Canada Revenue '
   'Agency and carries the program accounts hanging off it. The corporation '
   'number identifies it to the register it was incorporated under.</p>\n'
   '<p>Confusing the two is a filing problem rather than a paperwork one: a '
   'return transmitted against the wrong identifier cannot be assessed '
   'against the right corporation.</p>'),
  ('which-filing-uses-which', 'Which Filing Uses Which',
   _tbl(['Filing', 'Identifier', 'Issued by', 'Inside the fee?'],
        [['The T2 corporate income tax return', 'Business Number',
          'Canada Revenue Agency', 'Yes'],
         ['A nil GST/HST or payroll return',
          'Business Number with its program account',
          'Canada Revenue Agency', 'No'],
         ['The registry annual return', 'Corporation number',
          'The register of incorporation', 'No'],
         ['A provincial corporate return, where one applies',
          'The provincial account for that return',
          'The provincial authority', 'No']])
   + '\n<p>The '
   + a(T + 'business-number-status-checker/', 'Business Number status checker')
   + ' shows which program accounts are open on the Business Number, and the '
   + a(T + 'annual-return-vs-tax-return-checker/',
       'annual return versus tax return checker')
   + ' separates the two filings these identifiers belong to.</p>'),
  ('what-we-look-up', 'What We Confirm Before the Return Is Prepared',
   '<p>You do not need either number to hand to start. The filing form takes '
   'the corporation name, and the Business Number and incorporation date are '
   'confirmed against the corporation record before the return is '
   'prepared.</p>\n'
   '<p>What matters more than either number is the name: the return carries '
   'the exact legal name the register holds, corporation number and suffix '
   'included, and a mismatch is one of the common causes of a refused '
   'transmission. One corrected transmission is included in ' + PRICE
   + '.</p>'),
 ],
 faq=[
  ('Is the Business Number the same as the corporation number?',
   'No. The Business Number is issued by the Canada Revenue Agency and '
   'carries the program accounts; the corporation number is issued by the '
   'register the corporation was incorporated under. The T2 uses the Business '
   'Number and the registry annual return uses the corporation number.'),
  ('Do I need my Business Number to start?',
   'No. The filing form takes the corporation name, and the Business Number '
   'and incorporation date are confirmed against the corporation record '
   'before the return is prepared.'),
  ('What happens if the legal name does not match the register?',
   'It is one of the common causes of a refused transmission, whichever '
   'number is on the return. The return carries the exact legal name the '
   'register holds, and one corrected transmission is included in '
   + PRICE + '.'),
 ],
)


TOOLS10 = [T71, T72, T73, T74, T75, T76, T77, T78, T79, T80]

SEO10 = {
 'efile-rejection-reason-checker': (
  'E-Filing Rejection Reason Checker',
  'A refused T2 transmission is usually one of four identifier mismatches. '
  'Four answers name the cause and what clears it.'),
 'expenses-only-year-checker': (
  'Expenses Only Year Checker',
  'A year with costs and no revenue is still nil. What the expenses do to '
  'the return, and what ends a nil year instead.'),
 'never-traded-corporation-checker': (
  'Never Traded Corporation Checker',
  'A corporation that never started still owes a first return. Dated from '
  'the incorporation date and the 53-week limit.'),
 'restarting-a-dormant-corporation-checker': (
  'Restarting a Dormant Corporation Checker',
  'Trading again does not change the quiet years behind it. Which years are '
  'still nil returns at $300.00 plus HST per tax year.'),
 'loss-continuity-on-a-nil-return-checker': (
  'Loss Continuity on a Nil Return',
  'A nil year claims nothing against a loss and still reports it. What an '
  'unfiled loss year does to the balance carried forward.'),
 'multiple-corporation-filing-cost-calculator': (
  'Multiple Corporation Filing Cost Calculator',
  'Several quiet corporations, each with its own years. The returns owed and '
  'the total at $300.00 plus HST per tax year.'),
 'post-dissolution-return-checker': (
  'Post-Dissolution Return Checker',
  'A dissolved corporation stops having tax years. Which periods are owed up '
  'to the dissolution date, and which never arise.'),
 'acquired-corporation-unfiled-years-checker': (
  'Acquired Corporation Unfiled Years Checker',
  'A tax account belongs to the corporation, not its owner. Which unfiled '
  'years came with the purchase and which are yours.'),
 'sole-shareholder-corporation-checker': (
  'Sole Shareholder Corporation Checker',
  'A single shareholder holds 100 per cent, above the Schedule 50 threshold. '
  'What a one-person nil return carries.'),
 'business-number-versus-corporation-number-checker': (
  'Business Number vs Corporation Number',
  'Two numbers from two bodies. Which one the T2 needs, which one the '
  'registry annual return needs, and what we look up for you.'),
}
for t in TOOLS10:
    t['seo_title'], t['seo_desc'] = SEO10[t['slug']]
    assert len(t['seo_title']) <= 60, (
        '%s: SEO title is %d characters' % (t['slug'], len(t['seo_title'])))
    assert 70 <= len(t['seo_desc']) <= 160, (
        '%s: SEO description is %d characters'
        % (t['slug'], len(t['seo_desc'])))
assert set(SEO10) == {t['slug'] for t in TOOLS10}, 'SEO10 does not match'


def wire(form):
    """The listener block, derived from the form's own controls.

    Same as batch 9: a selector list typed by hand drifts from the form it is
    meant to bind, and a control nobody wired does nothing at all.
    """
    tags = _re.findall(r'<input\b[^>]*>', form)
    sel = []
    for tag in tags:
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
            "el.addEventListener('input',show);});\n")


for t, js in zip(TOOLS10, [T71_JS, T72_JS, T73_JS, T74_JS, T75_JS,
                           T76_JS, T77_JS, T78_JS, T79_JS, T80_JS]):
    js = js + wire(t['form'])
    t['js'] = js if js.startswith(PRELUDE) else PRELUDE + js

# Every control the form renders must be read by the module, and every radio
# the module reads must be a control the form renders. Both directions, kept
# from batch 9 where each had already gone wrong once.
for t in TOOLS10:
    _radios, _fields = set(), set()
    for tag in _re.findall(r'<input\b[^>]*>', t['form']):
        if 'type="radio"' in tag:
            m = _re.search(r'name="([\w-]+)"', tag)
            if m:
                _radios.add(m.group(1))
        else:
            m = _re.search(r'id="([\w-]+)"', tag)
            if m:
                _fields.add(m.group(1))
    for nm in _radios:
        assert "'%s'" % nm in t['js'], (
            '%s: form renders radio %r that the module never reads'
            % (t['slug'], nm))
    for fid in _fields:
        assert "'%s'" % fid in t['js'], (
            '%s: form renders field %r that the module never reads'
            % (t['slug'], fid))
    for nm in set(_re.findall(r"pick\('([\w-]+)'\)", t['js'])):
        assert nm in _radios, (
            '%s: module reads radio %r, which the form does not render'
            % (t['slug'], nm))
    # A date or number field is read through parse() or getElementById, and
    # either way the id has to be a field the form renders.
    for fid in set(_re.findall(r"parse\('([\w-]+)'\)", t['js'])
                   + _re.findall(r"getElementById\('([\w-]+)'\)", t['js'])):
        assert fid in _fields or fid == 'out', (
            '%s: module reads field %r, which the form does not render'
            % (t['slug'], fid))

# ---------------------------------------------------------------------------
# The structure contract. Navneet, 2026-11-03: "make sure they have all
# sections tables". Batches 6 and 7 shipped tool pages with no table in the
# body and gate9 added one check for it. Here the whole section set is a
# build-time contract: three prose sections, the middle one carrying a static
# reference table, a table drawn in the result, three FAQ items, six Read Next
# links. gate10.py re-checks the same list against the rendered HTML, so a
# page cannot reach the site missing a piece of it.
# ---------------------------------------------------------------------------
STRUCTURE = dict(sections=3, faq=3, related=6, tags=4,
                 body_tables=1, result_tables=1)

for t in TOOLS10:
    assert len(t['sections']) == STRUCTURE['sections'], (
        '%s: %d prose sections, the contract is %d'
        % (t['slug'], len(t['sections']), STRUCTURE['sections']))
    assert len(t['faq']) == STRUCTURE['faq'], (
        '%s: %d FAQ items, the contract is %d'
        % (t['slug'], len(t['faq']), STRUCTURE['faq']))
    assert len(t['tags']) == STRUCTURE['tags'], (
        '%s: %d hero tags, the contract is %d'
        % (t['slug'], len(t['tags']), STRUCTURE['tags']))
    _bt = sum(b.count('<table class="ei-tbl"') for _, _, b in t['sections'])
    assert _bt >= STRUCTURE['body_tables'], (
        '%s: no static reference table in the body' % t['slug'])
    assert t['js'].count('<table class="ei-tbl"') >= STRUCTURE['result_tables'], (
        '%s: the result draws no table' % t['slug'])
    # The table belongs to a section of its own, not bolted onto the lead.
    assert t['sections'][1][2].count('<table class="ei-tbl"') >= 1, (
        '%s: the second section is not the table section' % t['slug'])
    for _k, _h2, _b in t['sections']:
        assert _b.count('<p>') >= 1, (
            '%s: section %s has no prose at all' % (t['slug'], _k))
    assert len({k for k, _, _ in t['sections']}) == STRUCTURE['sections'], (
        '%s: duplicate section id' % t['slug'])

ORDER10 = ORDER9 + [t['slug'] for t in TOOLS10]
assert len(ORDER10) == len(set(ORDER10)), 'a slug is repeated in ORDER10'
LINK_TITLE10 = dict(LINK_TITLE9, **{
 'efile-rejection-reason-checker': 'E-Filing rejection reason checker',
 'expenses-only-year-checker': 'Expenses only year checker',
 'never-traded-corporation-checker': 'Never traded corporation checker',
 'restarting-a-dormant-corporation-checker':
     'Restarting a dormant corporation checker',
 'loss-continuity-on-a-nil-return-checker':
     'Loss continuity on a nil return checker',
 'multiple-corporation-filing-cost-calculator':
     'Multiple corporation filing cost calculator',
 'post-dissolution-return-checker': 'Post-dissolution return checker',
 'acquired-corporation-unfiled-years-checker':
     'Acquired corporation unfiled years checker',
 'sole-shareholder-corporation-checker':
     'Sole shareholder corporation checker',
 'business-number-versus-corporation-number-checker':
     'Business Number versus corporation number checker',
})

SIBLINGS10 = {
 'efile-rejection-reason-checker': [
   'mandatory-t2-efile-checker', 't183corp-signature-requirement-checker',
   'business-number-versus-corporation-number-checker'],
 'expenses-only-year-checker': [
   'dormant-corporation-test', 'nil-gifi-balance-sheet-checker',
   'nil-t2-eligibility-checker'],
 'never-traded-corporation-checker': [
   '53-week-first-tax-year-checker', 'schedule-24-first-return-checker',
   'first-t2-year-end-options-generator'],
 'restarting-a-dormant-corporation-checker': [
   'dormant-corporation-obligation-checker',
   'inactive-corporation-filing-checker',
   'nil-return-vs-full-return-checker'],
 'loss-continuity-on-a-nil-return-checker': [
   'schedule-8-cca-requirement-checker', 'required-schedules-checker',
   'retained-earnings-rollforward-calculator'],
 'multiple-corporation-filing-cost-calculator': [
   'unfiled-years-cost-calculator', 'dissolve-or-keep-filing-cost-calculator',
   'corporate-deadline-calendar-generator'],
 'post-dissolution-return-checker': [
   'final-t2-return-due-date-calculator', 'dissolution-timeline-calculator',
   'clearance-certificate-requirement-checker'],
 'acquired-corporation-unfiled-years-checker': [
   'unfiled-years-checker', 'tax-years-since-incorporation-calculator',
   'catch-up-filing-schedule-generator'],
 'sole-shareholder-corporation-checker': [
   'schedule-50-shareholder-threshold-checker',
   'share-capital-reporting-checker',
   'shareholder-register-completeness-checker'],
 'business-number-versus-corporation-number-checker': [
   'business-number-status-checker', 'efile-rejection-reason-checker',
   'cra-account-standing-checker'],
}

GUIDES10 = {
 'efile-rejection-reason-checker': [
   ('t183corp-signing-and-transmission',
    'Form T183CORP signing and transmission'),
   ('mandatory-t2-electronic-filing', 'Mandatory T2 electronic filing')],
 'expenses-only-year-checker': [
   ('zero-activity-corporate-tax-returns',
    'Zero-activity corporate tax returns'),
   ('gifi-schedules-100-125-141', 'GIFI Schedules 100, 125 and 141')],
 'never-traded-corporation-checker': [
   ('first-year-t2-filing', 'First-year T2 filing'),
   ('shelf-corporation-compliance', 'Shelf corporation compliance')],
 'restarting-a-dormant-corporation-checker': [
   ('dormant-and-inactive-corporations', 'Dormant and inactive corporations'),
   ('zero-activity-corporate-tax-returns',
    'Zero-activity corporate tax returns')],
 'loss-continuity-on-a-nil-return-checker': [
   ('schedule-8-and-loss-continuity', 'Schedule 8 and loss continuity'),
   ('t2-schedules-on-a-nil-return', 'T2 schedules on a nil return')],
 'multiple-corporation-filing-cost-calculator': [
   ('numbered-company-maintenance', 'Numbered company maintenance'),
   ('small-business-corporate-filing', 'Small business corporate filing')],
 'post-dissolution-return-checker': [
   ('final-t2-and-dissolution', 'The final T2 and dissolution'),
   ('winding-up-an-inactive-corporation',
    'Winding up an inactive corporation')],
 'acquired-corporation-unfiled-years-checker': [
   ('catch-up-unfiled-corporate-tax-returns',
    'Catching up on unfiled corporate tax returns'),
   ('shelf-corporation-compliance', 'Shelf corporation compliance')],
 'sole-shareholder-corporation-checker': [
   ('schedule-50-and-shareholder-reporting',
    'Schedule 50 and shareholder reporting'),
   ('numbered-company-tax-filing', 'Numbered company tax filing')],
 'business-number-versus-corporation-number-checker': [
   ('how-to-file-a-nil-t2-return', 'How to file a nil T2 return'),
   ('provincial-and-federal-annual-returns',
    'Provincial and federal annual returns')],
}

_ORDER = set(ORDER10)
_NEW = {t['slug'] for t in TOOLS10}
for t in TOOLS10:
    assert t['slug'] in _THIS_BATCH, (
        '%s is not in _THIS_BATCH, so the live-state check cannot see it'
        % t['slug'])
    # Before publishing, none of the ten is live and a slug already in
    # TOOLS_LIVE would mean this batch duplicates an existing page. After
    # publishing they are all live, so the check only applies in the first
    # state.
    if not PUBLISHED:
        assert t['slug'] not in TOOLS_LIVE, (
            '%s is already live: this batch would duplicate it' % t['slug'])
    for s in SIBLINGS10[t['slug']]:
        assert s in _ORDER, '%s lists a sibling that does not exist: %s' % (
            t['slug'], s)
        assert s != t['slug'], '%s lists itself as a sibling' % t['slug']
        assert s in LINK_TITLE10, '%s has no link title' % s
        # A sibling is either live or in this batch. Anything else is a link
        # to a page nobody has published.
        assert s in TOOLS_LIVE or s in _NEW, (
            '%s links to %s, which is neither live nor in this batch'
            % (t['slug'], s))
    for g, _ttl in GUIDES10[t['slug']]:
        assert g in GUIDES_LIVE10, (
            '%s links to guide %s, which is not live' % (t['slug'], g))
assert set(SIBLINGS10) == _NEW, 'SIBLINGS10 mismatch'
assert set(GUIDES10) == _NEW, 'GUIDES10 mismatch'
assert len({t['keyword'] for t in TOOLS10}) == 10, 'duplicate focus keyword'
assert len({t['h1'] for t in TOOLS10}) == 10, 'duplicate H1'

# Body, form, FAQ and module links are all checked: an unchecked link in a
# script is exactly as dead as one in a paragraph.
for t in TOOLS10:
    _all = (' '.join(b for _, _, b in t['sections']) + t['form']
            + ' '.join(q + aa for q, aa in t['faq']) + t['js'])
    for s in set(_re.findall(r'/tools/([a-z0-9-]+)/', _all)):
        assert s in _ORDER, (
            '%s: links to /tools/%s/, which does not exist' % (t['slug'], s))
        assert s in TOOLS_LIVE or s in _NEW, (
            '%s: links to /tools/%s/, which is not published' % (t['slug'], s))
    for g in set(_re.findall(r'/guides/([a-z0-9-]+)/', _all)):
        assert g in GUIDES_LIVE10, (
            '%s: links to /guides/%s/, which is not live' % (t['slug'], g))

for t in TOOLS10:
    rel = [(T + s + '/', LINK_TITLE10[s]) for s in SIBLINGS10[t['slug']]]
    rel += [(G + g + '/', ttl) for g, ttl in GUIDES10[t['slug']]]
    rel.append((COST, 'Nil T2 filing cost'))
    assert len(rel) == STRUCTURE['related'], (
        '%s: %d Read Next links, the contract is %d'
        % (t['slug'], len(rel), STRUCTURE['related']))
    t['related'] = rel


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'November 3, 2026', '2026-11-03'
    recs = []
    for t in TOOLS10:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2j-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-46s %6d bytes' % (r['slug'], len(r['content'].encode())))
