# -*- coding: utf-8 -*-
"""Family 2 batch 9: tools 61 to 70.

ALL TEN ARE APPENDIX A ENTRIES. Family 2 stands at fifty of the plan's hundred
and fifty appendix slugs after this batch, and at seventy pages live.

WHAT THE APPENDIX HAS LEFT, MEASURED RATHER THAN GUESSED

A hundred and ten appendix slugs were unbuilt before this batch. That number
flatters the appendix badly, and the next batch should know why:

  Roughly thirty are the live tools under another name. /t2-filing-deadline-
  calculator/ is the live nil-t2-deadline-calculator, /gifi-requirement-
  checker/ is gifi-schedule-requirement-checker, /first-tax-year-53-week-
  checker/ is 53-week-first-tax-year-checker, /fiscal-year-end-calculator/ is
  corporate-fiscal-year-end-calculator. Five separate slugs
  (/back-year-t2-cost-calculator/, /multi-year-nil-filing-total-calculator/,
  /ten-year-catch-up-cost-calculator/, /years-behind-filing-cost-calculator/,
  /catch-up-nil-filing-cost-calculator/) are one live tool,
  unfiled-years-cost-calculator. Building them would be the same page at five
  URLs, which is the template-copy pattern line 1212 exists to prevent.

  Roughly fifty need a figure the plan never states: every penalty, interest,
  withholding and threshold tool, listed in build_f2h.py's refusal block and
  still refused on the same grounds.

  Eight more were drafted and dropped on a measurement made this batch. The
  plan mentions Schedules 546, 9, 11, 23, 88, 3, 7 and 1 exactly zero times,
  so /schedule-546-ontario-annual-return-checker/ and its seven siblings have
  no rule to encode. The Ontario annual return appears ten times and never
  once with its deadline, its fee or its requirement test: the plan says only
  that it is filed through the Ontario Business Registry and is not covered by
  the fee. So /ontario-annual-return-deadline-calculator/,
  /ontario-annual-return-requirement-checker/, /ontario-missed-annual-returns-
  calculator/, /ontario-business-registry-filing-checker/,
  /ontario-corporate-key-checker/ and /ontario-initial-return-deadline-
  calculator/ are all unbuildable from the signed plan, not merely awkward.

  What is left after those three groups is about ten pages, which is this
  batch. Family 2 reaching 150 needs Sharad Gondaliya to supply the missing
  figures, or to accept slugs outside the appendix, or to accept fewer than
  150. That is a decision, not a drafting problem, and it is logged.

THE SOURCE FOR EACH TOOL

  NOT_NIL, which lists "a year-end change needing CRA approval" among the
  cases that are not nil and route to gondaliyacpa.ca at $350.00 plus HST
  per year                                              -> tools 61, 69
  The eight T2 Short conditions, as encoded on the live
  t2-short-eligibility-checker and reused here verbatim  -> tools 62, 63
  NOT_NIL again: "not a Canadian-controlled private corporation"
  is not nil                                            -> tool 63
  "A final T2 is due within six months of the date of dissolution", and
  unfiled years block both a clearance certificate and the dissolution
  itself                                                -> tool 64
  "Form RC145. An inactive T2 does not close those accounts." (plan 2149),
  and an open account still owes nil returns             -> tools 65, 70
  "Schedule 50 for every shareholder at 10% or more"  (plan 177, 1869)
                                                        -> tool 66
  "any share capital, cash, shareholder loan, incorporation cost or bank
  charge makes them required"                   (plan 1827, 2081, 2151)
                                                        -> tool 67
  Arbitrary assessment, which the plan raises eight times: the filed return
  for the year displaces the assessed figures            -> tool 68
  The tax account and the registry record are separate trails, and being
  struck does not cancel an outstanding T2                -> tool 70

WHAT TOOL 67 DOES NOT DECIDE

A shareholder loan has a tax treatment, and that treatment turns on statutory
periods and a prescribed rate the plan does not carry. Tool 67 answers the
reporting question only, which is the one the plan does state: a balance in
either direction makes the GIFI schedules required. It says so on the page
rather than leaving a visitor to assume the silence means no.
"""
import io, json, os
import re as _re

from build_f2 import (render, meta, yn, a, SITE, HUB, FORM, PRICE,
                      NOT_NIL, TOOL_DISCLAIMER)
from build_f2b import tool, num, date, PICK, T, G, COST
from build_f2c import MONEY_JS, QUAL, PRELUDE
from build_f2f import BASE, RBASE
from build_f2h import ORDER8, LINK_TITLE8, GUIDES_LIVE8

HERE = os.path.dirname(os.path.abspath(__file__))

# The thirty live guides, read from the hub's own children file rather than
# retyped, so a guide renamed there cannot leave a dead link here.
_GUIDES_JSON = os.path.join(HERE, '..', 'f16', 'guides-hub-children.json')
GUIDES_LIVE9 = set(json.load(io.open(_GUIDES_JSON, encoding='utf-8'))['slugs'])
assert GUIDES_LIVE8 <= GUIDES_LIVE9, 'batch 8 linked a guide no longer listed'

# The eight T2 Short conditions, in the order the live checker asks them.
SHORT8 = [
 ('ccpc', 'The corporation is a Canadian-controlled private corporation '
          'throughout the tax year.'),
 ('ninc', 'It has nil net income, or a loss, for income tax purposes this '
          'year.'),
 ('pe',   'It has one permanent establishment only.'),
 ('div',  'It paid no taxable dividends and received none in the year.'),
 ('cad',  'It reports in Canadian currency.'),
 ('cred', 'It is claiming no refundable credits.'),
 ('ott',  'It has no Ontario transitional tax debit.'),
 ('s342', 'It has no amount calculated under section 34.2.'),
]


# ------------------------------------------------------------------ 61. y/e
T61_JS = RBASE + r"""
function yeRoute(fy,ch,ap){
  if(fy===null||ch===null){return null;}
  if(fy==='y'){return {kind:'first'};}
  if(ch==='n'){return {kind:'none'};}
  if(ap===null){return null;}
  return {kind:ap==='y'?'approved':'pending'};
}
var out=document.getElementById('out');
function show(){
  var r=yeRoute(pick('fy'),pick('ch'),pick('ap'));
  if(r===null){out.innerHTML='<p>Answer the questions above.</p>';return;}
  var h;
  if(r.kind==='first'){
    h='<h3>There is nothing to approve on a first year-end</h3>';
    h+='<p>A corporation chooses its first fiscal year-end rather than '
     +'applying for it. The one limit is length: the first tax year cannot '
     +'exceed 53 weeks, and the year-end has to match the record the Canada '
     +'Revenue Agency holds or the transmission is rejected.</p>';
    h+='<p>So this is not a year-end change and it does not take you outside '
     +'a nil filing. If the year had no activity, its return is nil at '
     +PRICE_JS+'.</p>';
  }else if(r.kind==='none'){
    h='<h3>No year-end change, so no approval question</h3>';
    h+='<p>Keeping the same fiscal year-end each year is the ordinary case '
     +'and raises nothing to approve. Each year ends on the same date and '
     +'each return is due six months after it.</p>';
    h+='<p>A quiet year on an unchanged year-end is a nil return at '
     +PRICE_JS+'.</p>';
  }else if(r.kind==='approved'){
    h='<h3>The change is settled, and it creates two periods to file</h3>';
    h+='<p>With the change approved, the old year-end closes one tax year and '
     +'the new one opens the next. Each period is its own tax year with its '
     +'own return and its own deadline six months after it ends, and each '
     +'carries the fee separately.</p>';
    h+='<p>Where both periods had no activity, both are nil returns at '
     +PRICE_JS+' each.</p>';
  }else{
    h='<h3>A change still needing approval is outside this service</h3>';
    h+='<p>A year-end change that needs the Canada Revenue Agency to approve '
     +'it is one of the cases this service does not file. '+NOTNILJS+'</p>';
    h+='<p>That is a routing answer rather than a verdict on the change '
     +'itself. Once the change is settled, the periods it created are '
     +'ordinary tax years, and a quiet one is an ordinary nil return.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T61 = dict(
 slug='year-end-change-approval-checker',
 title='Year-End Change Approval Checker | What It Routes To',
 h1_pre='Year-End Change ', h1_span='Approval Checker',
 h1='Year-End Change Approval Checker',
 eyebrow='Year-End Change',
 keyword='year-end change approval checker',
 meta=('A year-end change needing approval is filed elsewhere. Three answers '
       'show whether yours is a nil return or a referral.'),
 tags=['Three answers', 'Covers a first year-end',
       'Says when it is a referral', 'No rates'],
 form=tool('Your fiscal year-end',
           [yn('fy', 'Is this the corporation&rsquo;s first tax year?'),
            yn('ch', 'Are you changing a fiscal year-end that is already '
                     'set?'),
            yn('ap', 'Has the Canada Revenue Agency approved the change?',
               'Yes', 'Not yet')],
           'Answer the questions above.'),
 js=None,
 sections=[
  ('what-this-decides', 'What This Checker Actually Decides',
   '<p>It decides where your return is filed, not whether a year-end change '
   'is a good idea. There is one case in which a change takes a corporation '
   'outside nil filing: where the change still needs the Canada Revenue '
   'Agency to approve it. That case goes to our sister office instead.</p>\n'
   '<p>Every other answer leaves you with ordinary tax years. A first '
   'year-end is chosen rather than approved, an unchanged year-end raises '
   'nothing, and a change already approved simply leaves two periods to '
   'file.</p>'),
  ('the-four-answers', 'The Four Answers Side by Side',
   '<table class="ei-tbl"><thead><tr><th scope="col">Your situation</th>'
   '<th scope="col">Approval</th><th scope="col">What you file</th></tr>'
   '</thead><tbody>\n'
   '<tr><td>First tax year</td><td>Not applicable</td><td>One return, on a '
   'year-end you choose, capped at 53 weeks</td></tr>\n'
   '<tr><td>Year-end unchanged</td><td>Not applicable</td><td>One return per '
   'year on the same date</td></tr>\n'
   '<tr><td>Change already approved</td><td>Settled</td><td>Two periods, two '
   'returns, two deadlines, the fee on each</td></tr>\n'
   '<tr><td>Change still needing approval</td><td>Outstanding</td><td>Filed '
   'by our sister office rather than here</td></tr>\n'
   '</tbody></table>\n'
   '<p>The '
   + a(T + 'year-end-change-impact-calculator/',
       'year-end change impact calculator')
   + ' dates the periods a change creates once it is settled, and the '
   + a(T + 'fiscal-period-length-calculator/',
       'fiscal period length calculator')
   + ' measures one against the 53-week limit.</p>'),
  ('the-53-week-limit', 'The One Limit on a First Year-End',
   '<p>A first tax year cannot exceed 53 weeks. That is a length limit rather '
   'than an approval step, and it is the only constraint on the first '
   'year-end a corporation picks.</p>\n'
   '<p>It still catches people, because a year-end chosen for tidiness can '
   'sit more than 53 weeks after the incorporation date. Where it does, the '
   'first period has to end earlier and a second period picks up the rest.</p>'),
 ],
 faq=[
  ('Does changing a fiscal year-end need CRA approval?',
   'Some changes do. Where a change needs the Canada Revenue Agency to '
   'approve it, the filing is outside this service and we route you to our '
   'sister office at gondaliyacpa.ca at $350.00 plus HST per year. Where the '
   'change is already settled, the periods it created are ordinary tax years '
   'and a quiet one is an ordinary nil return.'),
  ('Does a year-end change mean two returns?',
   'Yes. The old year-end closes one tax year and the new one opens the next, '
   'so there are two periods, each with its own return and its own deadline '
   'six months after it ends. Each carries ' + PRICE + '.'),
  ('Can I choose any year-end for a first return?',
   'Any date, with one limit: the first tax year cannot exceed 53 weeks. The '
   'year-end also has to match the record the Canada Revenue Agency holds, or '
   'the transmission is rejected.'),
 ],
)


# ------------------------------------------------------------- 62. exclusion
T62_JS = RBASE + r"""
var COND=[
 ['ccpc','Canadian-controlled private corporation throughout the year',
  'The short return is for CCPCs. Without that status the full T2 is the '
  +'return, and the corporation is also outside nil filing here.'],
 ['ninc','Nil net income or a loss for income tax purposes',
  'Net income above nil puts the corporation on the full return.'],
 ['pe','One permanent establishment only',
  'A second permanent establishment means an allocation between '
  +'jurisdictions, which the short return does not carry.'],
 ['div','No taxable dividends paid and none received',
  'A dividend either way excludes the short return, and also means the year '
  +'is not nil.'],
 ['cad','Reports in Canadian currency',
  'A functional currency election puts the corporation on the full return.'],
 ['cred','Claiming no refundable credits',
  'A refundable credit claim has no place on the short return.'],
 ['ott','No Ontario transitional tax debit',
  'The debit has to be reported, and the short return has no line for it.'],
 ['s342','No amount calculated under section 34.2',
  'A section 34.2 amount puts the corporation on the full return.']
];
function exclusions(){
  var fails=[],unanswered=0,i,v;
  for(i=0;i<COND.length;i++){
    v=pick(COND[i][0]);
    if(v===null){unanswered++;continue;}
    if(v==='n'){fails.push(COND[i]);}
  }
  if(unanswered>0){return {wait:unanswered};}
  return {fails:fails};
}
var out=document.getElementById('out');
function show(){
  var r=exclusions();
  if(r.wait){
    out.innerHTML='<p>'+r.wait+' of the eight conditions '
     +(r.wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  var h,i;
  if(r.fails.length===0){
    h='<h3>Nothing here excludes the short return</h3>';
    h+='<p>All eight conditions are met, so no exclusion applies and the '
     +'two-page T2 Short is available. We file it where a corporation '
     +'qualifies, and it is inside '+PRICE_JS+' rather than charged '
     +'separately.</p>';
    h+='<p>'+DISC_JS+'</p>';
    out.innerHTML=h;return;
  }
  h='<h3>'+r.fails.length+' of the eight conditions '
   +(r.fails.length===1?'excludes':'exclude')+' the short return</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Condition not met</th>'
   +'<th scope="col">Why it excludes the short return</th></tr></thead>'
   +'<tbody>';
  for(i=0;i<r.fails.length;i++){
    h+='<tr><td>'+r.fails[i][1]+'</td><td>'+r.fails[i][2]+'</td></tr>';
  }
  h+='</tbody></table>';
  h+='<p>Meeting seven of eight is not enough: every condition has to hold. '
   +'Where one does not, the full T2 is the return, and we file that at the '
   +'same fee rather than a different one.</p>';
  var notNil=false;
  for(i=0;i<r.fails.length;i++){
    if(r.fails[i][0]==='ccpc'||r.fails[i][0]==='div'){notNil=true;}
  }
  if(notNil){
    h+='<p>One of the conditions you missed also bears on whether the year is '
     +'nil at all. '+NOTNILJS+'</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T62 = dict(
 slug='t2-short-exclusion-checker',
 title='T2 Short Exclusion Checker | Which Condition Excludes You',
 h1_pre='T2 Short ', h1_span='Exclusion Checker',
 h1='T2 Short Exclusion Checker',
 eyebrow='The Short Return',
 keyword='t2 short exclusion checker',
 meta=('The eight T2 Short conditions, and which of them excludes your '
       'corporation. Naming the condition is the useful part.'),
 tags=['All eight conditions', 'Names the condition that excludes you',
       'Says what each one means', 'Same fee either way'],
 form=tool('The eight conditions',
           [yn(i, q) for i, q in SHORT8],
           'Answer all eight conditions.'),
 js=None,
 sections=[
  ('eligible-or-excluded', 'This Page Answers the No, Not the Yes',
   '<p>There are two questions about the T2 Short and they want different '
   'pages. Whether a corporation qualifies is a yes or a no, and the '
   + a(T + 't2-short-eligibility-checker/', 'T2 Short eligibility checker')
   + ' answers it. Which condition excluded it is a different answer, and '
   'that is this page.</p>\n'
   '<table class="ei-tbl"><thead><tr><th scope="col">Your question</th>'
   '<th scope="col">The page</th></tr></thead><tbody>\n'
   '<tr><td>Can this corporation use the short return?</td><td>T2 Short '
   'eligibility checker</td></tr>\n'
   '<tr><td>Which condition is stopping it, and what does that condition '
   'mean?</td><td>This page</td></tr>\n'
   '<tr><td>Short return or full return, and what changes?</td><td>'
   'Nil return vs full return checker</td></tr>\n'
   '</tbody></table>'),
  ('all-eight-hold', 'Seven of Eight Is a No',
   '<p>The eight conditions are not weighted and there is no substantial '
   'compliance in them. Every one has to hold, so a corporation that meets '
   'seven files the full T2.</p>\n'
   '<p>That is a smaller problem than it sounds. The full T2 is the longer '
   'form, not the dearer service: we file whichever one the corporation '
   'qualifies for, and both sit inside ' + PRICE + '.</p>'),
  ('two-that-go-further', 'Two Conditions Reach Past the Form',
   '<p>Two of the eight say something about the year as well as the form. A '
   'corporation that is not a Canadian-controlled private corporation, and a '
   'corporation that paid or received a taxable dividend, are both outside '
   'nil filing here, not merely outside the short return.</p>\n'
   '<p>Where your answer missed either of those, the result says so. The '
   + a(T + 'nil-t2-eligibility-checker/', 'nil T2 eligibility checker')
   + ' is the page for that question on its own.</p>'),
 ],
 faq=[
  ('What excludes a corporation from the T2 Short?',
   'Failing any one of the eight conditions. The conditions are not weighted '
   'and there is no partial compliance, so a corporation that meets seven '
   'files the full T2 instead.'),
  ('Does the full T2 cost more than the short return?',
   'No. ' + PRICE + ' covers either one. The short return is a shorter form '
   'for a corporation that qualifies, not a cheaper service.'),
  ('Which conditions also affect whether the year is nil?',
   'Two of them. A corporation that is not a Canadian-controlled private '
   'corporation, and one that paid or received a taxable dividend, are '
   'outside nil filing here as well as outside the short return. We route '
   'those to gondaliyacpa.ca at $350.00 plus HST per year.'),
 ],
)


# ------------------------------------------------------------------ 63. ccpc
T63_JS = RBASE + r"""
function ccpcStatus(res,pub,nr,corp){
  if(res===null||pub===null||nr===null||corp===null){return null;}
  var fails=[];
  if(res==='n'){fails.push('not resident in Canada');}
  if(pub==='y'){fails.push('shares traded on a designated stock exchange');}
  if(nr==='y'){fails.push('controlled by non-residents');}
  if(corp==='y'){fails.push('controlled by one or more public corporations');}
  return {ccpc:fails.length===0,fails:fails};
}
var out=document.getElementById('out');
function show(){
  var r=ccpcStatus(pick('res'),pick('pub'),pick('nr'),pick('corp'));
  if(r===null){out.innerHTML='<p>Answer all four questions.</p>';return;}
  var h,i;
  if(r.ccpc){
    h='<h3>The corporation reads as a Canadian-controlled private '
     +'corporation</h3>';
    h+='<p>That clears the first of the eight T2 Short conditions, and it '
     +'keeps the corporation inside nil filing here. Resident in Canada, not '
     +'publicly traded, and not controlled by non-residents or by public '
     +'corporations: those four together are what the status turns on for '
     +'this purpose.</p>';
    h+='<p>Status is held throughout the tax year, not on one date, so a '
     +'change part-way through the year is worth checking against the whole '
     +'period. A quiet year on this footing is a nil return at '+PRICE_JS
     +'.</p>';
  }else{
    h='<h3>The corporation does not read as a CCPC</h3>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">What takes it '
     +'outside CCPC status</th></tr></thead><tbody>';
    for(i=0;i<r.fails.length;i++){
      h+='<tr><td>It is '+r.fails[i]+'</td></tr>';
    }
    h+='</tbody></table>';
    h+='<p>This matters twice. It fails the first of the eight T2 Short '
     +'conditions, so the full T2 is the return. And a corporation that is '
     +'not a Canadian-controlled private corporation is one of the cases '
     +'this service does not file. '+NOTNILJS+'</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T63 = dict(
 slug='t2-short-ccpc-condition-checker',
 title='CCPC Condition Checker | The First T2 Short Condition',
 h1_pre='T2 Short ', h1_span='CCPC Condition Checker',
 h1='T2 Short CCPC Condition Checker',
 eyebrow='CCPC Status',
 keyword='t2 short ccpc condition checker',
 meta=('CCPC status decides the first T2 Short condition and whether the year '
       'is nil here at all. Four answers settle it.'),
 tags=['Four answers', 'Decides a T2 Short condition',
       'Decides nil eligibility too', 'Status is held all year'],
 form=tool('Control and residence',
           [yn('res', 'Is the corporation resident in Canada?'),
            yn('pub', 'Are its shares traded on a designated stock '
                      'exchange?'),
            yn('nr', 'Is it controlled, directly or indirectly, by '
                     'non-residents?'),
            yn('corp', 'Is it controlled by one or more public '
                       'corporations?')],
           'Answer all four questions.'),
 js=None,
 sections=[
  ('why-it-matters-twice', 'One Status, Two Consequences',
   '<p>CCPC status is the first of the eight conditions for the two-page T2 '
   'Short. It is also one of the cases that decides whether a corporation is '
   'filed here at all: a corporation that is not a Canadian-controlled '
   'private corporation goes to our sister office rather than through this '
   'service.</p>\n'
   '<table class="ei-tbl"><thead><tr><th scope="col">If the corporation is a '
   'CCPC</th><th scope="col">If it is not</th></tr></thead><tbody>\n'
   '<tr><td>First T2 Short condition met</td><td>First condition failed, so '
   'the full T2 is the return</td></tr>\n'
   '<tr><td>A quiet year is a nil return at ' + PRICE + '</td><td>Filed by '
   'our sister office at $350.00 plus HST per year</td></tr>\n'
   '<tr><td>The other seven conditions still apply</td><td>The other seven '
   'stop mattering for the short return</td></tr>\n'
   '</tbody></table>'),
  ('throughout-the-year', 'Throughout the Tax Year, Not on One Date',
   '<p>The condition is held throughout the tax year. A corporation that was '
   'a CCPC in January and not in November did not meet it for that year, even '
   'though it would read as one on either date taken alone.</p>\n'
   '<p>Which is why a share issue, a change of control or a listing part-way '
   'through a year is worth checking against the whole period rather than '
   'against the year-end.</p>'),
  ('what-this-is-not', 'What These Four Questions Are Not',
   '<p>They are the four that decide the point for the short return and for '
   'nil filing. CCPC status carries other consequences in corporate tax, and '
   'those turn on rates and limits this page does not carry and does not '
   'guess at.</p>\n'
   '<p>For the whole eight-condition set, the '
   + a(T + 't2-short-eligibility-checker/', 'T2 Short eligibility checker')
   + ' asks them all, and the '
   + a(T + 't2-short-exclusion-checker/', 'T2 Short exclusion checker')
   + ' names whichever one excludes you.</p>'),
 ],
 faq=[
  ('Why does CCPC status appear on a nil filing site?',
   'Because it decides two things at once. It is the first of the eight T2 '
   'Short conditions, and a corporation that is not a Canadian-controlled '
   'private corporation is outside nil filing here and routes to '
   'gondaliyacpa.ca at $350.00 plus HST per year.'),
  ('Does the status have to hold all year?',
   'Yes, throughout the tax year. A corporation that held the status for part '
   'of the year did not meet the condition for that year.'),
  ('What if the corporation is not a CCPC?',
   'The full T2 is the return rather than the short one, and the filing is '
   'one we route to our sister office. ' + TOOL_DISCLAIMER),
 ],
)


# ------------------------------------------------------------- 64. timeline
T64_JS = RBASE + r"""
function windUp(id,un){
  var d=parse(id);
  if(d===null||d===undefined||un===null){return null;}
  return {d:d,due:dueDate(d),un:un==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=windUp('ds',pick('un'));
  if(r===null){
    out.innerHTML='<p>Enter the planned dissolution date and answer the '
     +'question.</p>';return;
  }
  var h='<h3>The final T2 is due '+fmt(r.due)+'</h3>';
  h+='<p>The final tax year ends on '+fmt(r.d)+', the date of dissolution, '
   +'and its return is due six months after that.</p>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Step</th>'
   +'<th scope="col">What it is</th><th scope="col">When</th></tr></thead>'
   +'<tbody>';
  if(r.un){
    h+='<tr><td>1. Outstanding years</td><td>Every unfiled year, oldest '
     +'first, each its own return</td><td>Before the final return is '
     +'assessed</td></tr>';
  }
  h+='<tr><td>'+(r.un?'2':'1')+'. Final T2</td><td>The period ending '
   +fmt(r.d)+'</td><td>Due '+fmt(r.due)+'</td></tr>';
  h+='<tr><td>'+(r.un?'3':'2')+'. Clearance certificate</td><td>Requested '
   +'from the Canada Revenue Agency, not part of the fee</td><td>After the '
   +'returns are assessed</td></tr>';
  h+='<tr><td>'+(r.un?'4':'3')+'. Registry dissolution</td><td>Filed with '
   +'the registry the corporation was incorporated under, not part of the '
   +'fee</td><td>Last</td></tr>';
  h+='</tbody></table>';
  if(r.un){
    h+='<p>The outstanding years come first for a reason: unfiled years block '
     +'a clearance certificate and they block the dissolution itself. Each '
     +'one is its own return at '+PRICE_JS+'.</p>';
  }else{
    h+='<p>With no earlier years outstanding, the final return is the only '
     +'one to file. If that last period had no activity it is a nil return at '
     +PRICE_JS+'.</p>';
  }
  h+='<p>Filing the final T2 does not dissolve the corporation. The '
   +'dissolution is the registry step at the end, and it is not covered by '
   +'the fee.</p>';
  var fd=filingDate(r.d);
  if(fd.getTime()!==r.due.getTime()){
    h+='<p>'+fmt(r.due)+' is a Saturday, a Sunday or a public holiday '
     +'recognised by the Canada Revenue Agency, so a return received by '
     +fmt(fd)+' is on time.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T64 = dict(
 slug='dissolution-timeline-calculator',
 title='Dissolution Timeline Calculator | The Order and the Dates',
 h1_pre='Dissolution ', h1_span='Timeline Calculator',
 h1='Dissolution Timeline Calculator',
 eyebrow='Winding Up',
 keyword='dissolution timeline calculator',
 meta=('A dissolution date gives the final T2 deadline and the order of the '
       'steps around it, including the ones outside the fee.'),
 tags=['Computed final T2 date', 'Puts the steps in order',
       'Names what is outside the fee', 'Covers outstanding years'],
 form=tool('Your wind-up',
           [date('ds', 'Planned date of dissolution'),
            yn('un', 'Are any earlier tax years unfiled?')],
           'Enter the planned dissolution date and answer the question.'),
 js=None,
 sections=[
  ('the-order-matters', 'The Order Is the Useful Part',
   '<p>A wind-up has four steps and only one of them is a date on a form. '
   'Getting them in the wrong order is what stalls a dissolution, because '
   'two of the four depend on the ones before them.</p>\n'
   '<p>Unfiled years block a clearance certificate, and they block the '
   'dissolution itself. So the outstanding years go first, the final T2 '
   'follows, the clearance request comes after the returns are assessed, and '
   'the registry filing is last.</p>'),
  ('what-the-fee-covers', 'Which Steps Are Ours',
   '<table class="ei-tbl"><thead><tr><th scope="col">Step</th>'
   '<th scope="col">Inside ' + PRICE + '</th></tr></thead><tbody>\n'
   '<tr><td>Each outstanding nil year</td><td>Yes, at the fee per tax '
   'year</td></tr>\n'
   '<tr><td>The final T2, where the last period is nil</td><td>Yes, at the '
   'fee</td></tr>\n'
   '<tr><td>The clearance certificate request</td><td>No</td></tr>\n'
   '<tr><td>The registry dissolution filing</td><td>No</td></tr>\n'
   '<tr><td>Closing a GST/HST or payroll account</td><td>No</td></tr>\n'
   '</tbody></table>\n'
   '<p>The '
   + a(T + 'dissolution-readiness-checker/', 'dissolution readiness checker')
   + ' tests whether the corporation is ready to start, and the '
   + a(T + 'clearance-certificate-requirement-checker/',
       'clearance certificate requirement checker')
   + ' covers the third step on its own.</p>'),
  ('filing-does-not-dissolve', 'Filing the Final Return Does Not Dissolve It',
   '<p>The final T2 closes the tax record. It does not close the '
   'corporation, which stays in existence on the register until the registry '
   'dissolution is filed and accepted.</p>\n'
   '<p>Those are two trails and they end separately. A corporation whose '
   'returns are all filed and whose registry record is untouched is still '
   'live, and still accruing a filing obligation each year.</p>'),
 ],
 faq=[
  ('When is the final T2 due?',
   'Within six months of the date of dissolution. The final tax year ends on '
   'that date, and the six-month rule runs from it exactly as it does from an '
   'ordinary year-end.'),
  ('Do unfiled years have to be cleared first?',
   'Yes. They block a clearance certificate and they block the dissolution '
   'itself, so they are filed before the final return is assessed. Each one '
   'is its own return at ' + PRICE + '.'),
  ('Does filing the final return dissolve the corporation?',
   'No. The dissolution is a separate registry filing, made with the registry '
   'the corporation was incorporated under, and it is not covered by the '
   'fee.'),
 ],
)


# -------------------------------------------------------------- 65. payroll
T65_JS = RBASE + r"""
function payroll(op,rem,t4,cl){
  if(op===null){return null;}
  if(op==='n'){return {open:false};}
  if(rem===null||t4===null||cl===null){return null;}
  return {open:true,rem:rem==='y',t4:t4==='y',cl:cl==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=payroll(pick('op'),pick('rem'),pick('t4'),pick('cl'));
  if(r===null){out.innerHTML='<p>Answer the questions above.</p>';return;}
  var h;
  if(!r.open){
    h='<h3>No payroll account, so nothing to close</h3>';
    h+='<p>A corporation that never opened a payroll account has no payroll '
     +'filing to make and no account to close. The T2 is the return, and a '
     +'quiet year is nil at '+PRICE_JS+'.</p>';
    h+='<p>'+DISC_JS+'</p>';
    out.innerHTML=h;return;
  }
  h='<h3>The account is open, so it still expects filings</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">What</th>'
   +'<th scope="col">Your answer</th><th scope="col">What follows</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Salary or remittances this year</td><td>'+(r.rem?'Yes':'No')
   +'</td><td>'+(r.rem?'The year is not a nil payroll year, and the '
   +'corporation may not be nil for the T2 either':'A nil remittance is '
   +'still expected while the account is open')+'</td></tr>';
  h+='<tr><td>T4s filed for every year the account was open</td><td>'
   +(r.t4?'Yes':'No')+'</td><td>'+(r.t4?'Nothing outstanding on that '
   +'front':'Outstanding T4 filings stay outstanding until they are made')
   +'</td></tr>';
  h+='<tr><td>You want the account closed</td><td>'+(r.cl?'Yes':'No')
   +'</td><td>'+(r.cl?'Form RC145 is what closes it, after the outstanding '
   +'filings are made':'The account stays open and keeps expecting filings')
   +'</td></tr>';
  h+='</tbody></table>';
  h+='<p>An inactive T2 does not close a payroll account. Filing the '
   +'corporate return and leaving the account open leaves the account open, '
   +'and an open account goes on expecting returns whether or not anyone was '
   +'paid.</p>';
  if(r.cl){
    h+='<p>Form RC145 is the closure. It is filed with the Canada Revenue '
     +'Agency separately and it is not covered by the fee, and we tell you '
     +'that before you pay rather than after.</p>';
  }
  if(r.rem){
    h+='<p>A year in which salary was paid is a year with activity. '+NOTNILJS
     +'</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T65 = dict(
 slug='payroll-account-closure-checker',
 title='Payroll Account Closure Checker | RC145 and What Comes First',
 h1_pre='Payroll Account ', h1_span='Closure Checker',
 h1='Payroll Account Closure Checker',
 eyebrow='CRA Accounts',
 keyword='payroll account closure checker',
 meta=('An open payroll account outlives the payroll. What it still expects, '
       'and what Form RC145 closes.'),
 tags=['Four answers', 'Names Form RC145',
       'An inactive T2 closes nothing', 'Says what is outside the fee'],
 form=tool('Your payroll account',
           [yn('op', 'Does the corporation have a payroll account with the '
                     'Canada Revenue Agency?'),
            yn('rem', 'Was any salary paid, or any remittance made, this '
                      'year?'),
            yn('t4', 'Have T4s been filed for every year the account was '
                     'open?'),
            yn('cl', 'Do you want the account closed?')],
           'Answer the questions above.'),
 js=None,
 sections=[
  ('an-account-outlives-the-payroll', 'The Account Outlives the Payroll',
   '<p>A payroll account is opened once and then stays open. It does not '
   'lapse when the last employee leaves, and it does not notice that the '
   'corporation went quiet.</p>\n'
   '<p>So a corporation with no employees and an open account is in the '
   'position that surprises people most: nothing to report and a filing '
   'still expected. An inactive T2 does not close those accounts.</p>'),
  ('three-separate-filings', 'Three Filings, Three Places',
   '<table class="ei-tbl"><thead><tr><th scope="col">Filing</th>'
   '<th scope="col">What it answers for</th>'
   '<th scope="col">Inside ' + PRICE + '</th></tr></thead><tbody>\n'
   '<tr><td>The T2</td><td>Corporate income tax for the year</td><td>Yes, '
   'where the year is nil</td></tr>\n'
   '<tr><td>A nil payroll remittance or T4</td><td>The payroll account, while '
   'it is open</td><td>No</td></tr>\n'
   '<tr><td>Form RC145</td><td>Closing the account</td><td>No</td></tr>\n'
   '</tbody></table>\n'
   '<p>The '
   + a(T + 'payroll-nil-remittance-checker/', 'payroll nil remittance checker')
   + ' covers the second row and the '
   + a(T + 'cra-account-closure-sequencer/', 'CRA account closure sequencer')
   + ' puts the closures in order where there is more than one account.</p>'),
  ('order-of-closure', 'Outstanding Filings Come Before the Closure',
   '<p>Form RC145 closes an account. It does not forgive what the account was '
   'waiting for, so outstanding T4s and outstanding remittances are made '
   'first and the closure follows.</p>\n'
   '<p>Closing in the other order leaves filings outstanding against a closed '
   'account, which is a worse position to be in than an open account with '
   'nothing owing.</p>'),
 ],
 faq=[
  ('Does filing a nil T2 close a payroll account?',
   'No. An inactive T2 does not close those accounts. Form RC145 closes a '
   'payroll or GST/HST account, it is filed separately, and it is not covered '
   'by the fee.'),
  ('Does an open payroll account need filings with no employees?',
   'While the account is open it goes on expecting returns, whether or not '
   'anyone was paid. Closing it with Form RC145 is what stops that.'),
  ('What has to happen before the account is closed?',
   'Outstanding T4s and outstanding remittances are made first. Form RC145 '
   'closes the account; it does not clear what the account was waiting '
   'for.'),
 ],
)


# ------------------------------------------------------------- 66. register
T66_JS = RBASE + r"""
var FIELD=[
 ['kn','Every shareholder at 10% or more is identified'],
 ['nm','Full legal name for each of them'],
 ['ad','Address for each of them'],
 ['pc','Percentage held by each of them']
];
function register(){
  var miss=[],un=0,i,v;
  for(i=0;i<FIELD.length;i++){
    v=pick(FIELD[i][0]);
    if(v===null){un++;continue;}
    if(v==='n'){miss.push(FIELD[i][1]);}
  }
  if(un>0){return {wait:un};}
  return {miss:miss};
}
var out=document.getElementById('out');
function show(){
  var r=register();
  if(r.wait){
    out.innerHTML='<p>'+r.wait+' of the four '+(r.wait===1?'is':'are')
     +' still unanswered.</p>';return;
  }
  var h,i;
  if(r.miss.length===0){
    h='<h3>Schedule 50 can be completed from what you have</h3>';
    h+='<p>Schedule 50 names every shareholder holding 10 per cent or more, '
     +'and the four things above are what each row needs. With all four in '
     +'hand the schedule is a transcription rather than an investigation.</p>';
    h+='<p>It goes on the return inside '+PRICE_JS+' rather than being '
     +'charged separately.</p>';
  }else{
    h='<h3>'+r.miss.length+' of the four '+(r.miss.length===1?'is':'are')
     +' missing</h3>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Still needed for '
     +'Schedule 50</th></tr></thead><tbody>';
    for(i=0;i<r.miss.length;i++){h+='<tr><td>'+r.miss[i]+'</td></tr>';}
    h+='</tbody></table>';
    h+='<p>Schedule 50 is a list of people, so a gap in the register is a gap '
     +'on the return. The minute book and the share issuance records are '
     +'where the missing entries normally are.</p>';
  }
  h+='<p>The 10 per cent threshold is a floor, not a cap on how many rows '
   +'there are: a corporation with six shareholders above it names six.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T66 = dict(
 slug='shareholder-register-completeness-checker',
 title='Shareholder Register Checker | What Schedule 50 Needs',
 h1_pre='Shareholder Register ', h1_span='Completeness Checker',
 h1='Shareholder Register Completeness Checker',
 eyebrow='Schedule 50',
 keyword='shareholder register completeness checker',
 meta=('Schedule 50 names every shareholder at 10 per cent or more. Four '
       'answers show whether your register can fill it.'),
 tags=['Four answers', 'The 10 per cent threshold',
       'Names what each row needs', 'Inside the fee'],
 form=tool('Your shareholder register',
           [yn('kn', 'Is every shareholder holding 10 per cent or more '
                     'identified?'),
            yn('nm', 'Do you have a full legal name for each of them?'),
            yn('ad', 'Do you have an address for each of them?'),
            yn('pc', 'Do you know the percentage each of them holds?')],
           'Answer all four questions.'),
 js=None,
 sections=[
  ('a-nil-year-still-names-them', 'A Nil Year Still Names Them',
   '<p>Schedule 50 is required for every shareholder holding 10 per cent or '
   'more. It is a list of people rather than a set of figures, so a year of '
   'zeros does not empty it: the shareholders held their shares throughout '
   'the quiet year exactly as they would in a busy one.</p>\n'
   '<p>Which is the part that catches dormant corporations. The financial '
   'schedules may be all zeros while Schedule 50 is as full as it has ever '
   'been.</p>'),
  ('what-a-row-needs', 'What One Row Needs',
   '<table class="ei-tbl"><thead><tr><th scope="col">For each shareholder at '
   '10 per cent or more</th><th scope="col">Where it usually sits</th></tr>'
   '</thead><tbody>\n'
   '<tr><td>Full legal name</td><td>The share register in the minute '
   'book</td></tr>\n'
   '<tr><td>Address</td><td>The share register, or the annual registry '
   'filing</td></tr>\n'
   '<tr><td>Percentage held</td><td>The share issuance records</td></tr>\n'
   '<tr><td>Whether the holding crosses 10 per cent at all</td><td>The '
   'issuance records, totalled</td></tr>\n'
   '</tbody></table>\n'
   '<p>The '
   + a(T + 'schedule-50-shareholder-threshold-checker/',
       'Schedule 50 shareholder threshold checker')
   + ' answers whether a particular holding crosses the threshold. This page '
   'answers whether you can fill the schedule once you know who does.</p>'),
  ('share-capital-too', 'The Register Also Bears on the GIFI Schedules',
   '<p>Share capital on the books is one of the five things that make GIFI '
   'Schedules 100, 125 and 141 required on a return that would otherwise omit '
   'them. A register that shows issued shares is a register that shows share '
   'capital.</p>\n'
   '<p>So the same records answer two questions. The '
   + a(T + 'share-capital-reporting-checker/',
       'share capital reporting checker')
   + ' covers the GIFI side.</p>'),
 ],
 faq=[
  ('Who has to appear on Schedule 50?',
   'Every shareholder holding 10 per cent or more. The threshold is a floor '
   'rather than a limit on the number of rows, so a corporation with six '
   'holders above it names six.'),
  ('Does a nil return still need Schedule 50?',
   'Yes. It reports who holds the shares, not what the corporation earned, so '
   'a year of zeros does not empty it.'),
  ('Is Schedule 50 charged separately?',
   'No. Every schedule a nil return carries sits inside ' + PRICE + '.'),
 ],
)


# ------------------------------------------------------------ 67. direction
T67_JS = RBASE + r"""
function direction(owe,owed){
  if(owe===null||owed===null){return null;}
  var a=owe==='y',b=owed==='y';
  return {to:a,from:b,both:a&&b,none:!a&&!b};
}
var out=document.getElementById('out');
function show(){
  var r=direction(pick('owe'),pick('owed'));
  if(r===null){out.innerHTML='<p>Answer both questions.</p>';return;}
  var h;
  if(r.none){
    h='<h3>No shareholder balance either way</h3>';
    h+='<p>With nothing owing in either direction there is no shareholder '
     +'loan on the balance sheet, so the loan is not one of the things '
     +'putting figures on the GIFI schedules this year.</p>';
    h+='<p>Four other things still can: share capital, cash, an '
     +'incorporation cost and a bank charge. The '
     +'<a href="/tools/nil-gifi-balance-sheet-checker/">nil GIFI balance '
     +'sheet checker</a> runs through all five.</p>';
    h+='<p>'+DISC_JS+'</p>';
    out.innerHTML=h;return;
  }
  h='<h3>'+(r.both?'A balance in both directions'
   :(r.to?'Due to the shareholder, so a liability'
        :'Due from the shareholder, so an asset'))+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Direction</th>'
   +'<th scope="col">On the balance sheet it is</th>'
   +'<th scope="col">Present?</th></tr></thead><tbody>';
  h+='<tr><td>The corporation owes the shareholder</td><td>A liability, due '
   +'to the shareholder</td><td>'+(r.to?'Yes':'No')+'</td></tr>';
  h+='<tr><td>The shareholder owes the corporation</td><td>An asset, due from '
   +'the shareholder</td><td>'+(r.from?'Yes':'No')+'</td></tr>';
  h+='</tbody></table>';
  h+='<p>Either direction is a balance, and a shareholder loan balance is one '
   +'of the things that puts figures on GIFI Schedules 100, 125 and 141 on a '
   +'return that would otherwise leave them out. The direction changes which '
   +'side of the balance sheet the figure sits on. It does not change whether '
   +'the schedules are required.</p>';
  if(r.both){
    h+='<p>Both directions at once is common and is not a contradiction: an '
     +'amount due to a shareholder and an amount due from the same person are '
     +'separate balances and are reported separately rather than netted on '
     +'sight.</p>';
  }
  h+='<p>What this page does not decide is the tax treatment of the loan. '
   +'That turns on statutory periods and a prescribed rate, and neither is '
   +'something this tool carries. The reporting question is the one answered '
   +'here.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T67 = dict(
 slug='due-to-versus-due-from-shareholder-checker',
 title='Due To vs Due From Shareholder | Which Side It Sits On',
 h1_pre='Due To Versus ', h1_span='Due From Shareholder',
 h1='Due To Versus Due From Shareholder Checker',
 eyebrow='Shareholder Balances',
 keyword='due to versus due from shareholder checker',
 meta=('A shareholder balance can run either way. Which direction it is, and '
       'why either one makes the GIFI schedules required.'),
 tags=['Two answers', 'Both directions at once is normal',
       'Reporting, not tax treatment', 'Names the other four triggers'],
 form=tool('Your shareholder balance',
           [yn('owe', 'Does the corporation owe money to a shareholder?'),
            yn('owed', 'Does a shareholder owe money to the corporation?')],
           'Answer both questions.'),
 js=None,
 sections=[
  ('direction-and-consequence', 'Direction Changes the Side, Not the Duty',
   '<p>A shareholder balance runs one of two ways. Money the corporation owes '
   'a shareholder is a liability, due to the shareholder. Money a shareholder '
   'owes the corporation is an asset, due from the shareholder.</p>\n'
   '<p>For reporting, the direction decides which side of the balance sheet '
   'the figure appears on and nothing more. A balance in either direction is '
   'a balance, and that is what makes GIFI Schedules 100, 125 and 141 '
   'required on a return that would otherwise omit them.</p>'),
  ('five-things', 'The Balance Is One of Five Triggers',
   '<table class="ei-tbl"><thead><tr><th scope="col">On the books</th>'
   '<th scope="col">Makes the GIFI schedules required</th></tr></thead>'
   '<tbody>\n'
   '<tr><td>A shareholder loan, either direction</td><td>Yes</td></tr>\n'
   '<tr><td>Share capital</td><td>Yes</td></tr>\n'
   '<tr><td>Cash</td><td>Yes</td></tr>\n'
   '<tr><td>An incorporation cost</td><td>Yes</td></tr>\n'
   '<tr><td>A bank charge</td><td>Yes</td></tr>\n'
   '</tbody></table>\n'
   '<p>The '
   + a(T + 'shareholder-loan-balance-checker/',
       'shareholder loan balance checker')
   + ' answers whether a balance exists at all, and the '
   + a(T + 'nil-gifi-balance-sheet-checker/',
       'nil GIFI balance sheet checker')
   + ' runs the whole set of five.</p>'),
  ('netting', 'Two Balances Are Not One Balance',
   '<p>An amount due to a shareholder and an amount due from the same person '
   'are two balances. They are reported as two, not netted into whichever is '
   'larger, because they arose separately and are owed separately.</p>\n'
   '<p>That is worth saying because the netted figure is the one people hold '
   'in their heads. A corporation that owes a shareholder and is owed by the '
   'same shareholder has two entries, even where the difference between them '
   'is small.</p>'),
 ],
 faq=[
  ('Does the direction of a shareholder loan change the schedules?',
   'No. A balance in either direction makes GIFI Schedules 100, 125 and 141 '
   'required. The direction decides which side of the balance sheet it sits '
   'on.'),
  ('Can a balance run both ways at once?',
   'Yes, and it often does. The two are separate balances and are reported '
   'separately rather than netted together.'),
  ('Does this tell me the tax treatment of the loan?',
   'No. The tax treatment turns on statutory periods and a prescribed rate, '
   'which this tool does not carry. It answers the reporting question: a '
   'balance makes the GIFI schedules required.'),
 ],
)


# ------------------------------------------------------------- 68. arbitrary
T68_JS = RBASE + r"""
function arb(asd,nil,fl){
  if(asd===null){return null;}
  if(asd==='n'){return {assessed:false};}
  if(nil===null||fl===null){return null;}
  return {assessed:true,nil:nil==='y',filed:fl==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=arb(pick('as'),pick('nil'),pick('fl'));
  if(r===null){out.innerHTML='<p>Answer the questions above.</p>';return;}
  var h;
  if(!r.assessed){
    h='<h3>No assessment on an unfiled year, so the ordinary order '
     +'applies</h3>';
    h+='<p>Where no assessment has been raised for a year you did not file, '
     +'the year is simply outstanding. Filing it is the whole of the answer, '
     +'and an outstanding nil year is '+PRICE_JS+'.</p>';
    h+='<p>The <a href="/tools/unfiled-years-checker/">unfiled years '
     +'checker</a> lists which years are open.</p>';
    h+='<p>'+DISC_JS+'</p>';
    out.innerHTML=h;return;
  }
  h='<h3>'+(r.filed?'The return is in, so the figures should give way'
   :'The answer is to file the real return for that year')+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Step</th>'
   +'<th scope="col">State</th></tr></thead><tbody>';
  h+='<tr><td>An assessment was raised for a year you did not file</td>'
   +'<td>Yes</td></tr>';
  h+='<tr><td>The year was in fact nil</td><td>'+(r.nil?'Yes':'Not sure or '
   +'no')+'</td></tr>';
  h+='<tr><td>The real return has been filed</td><td>'
   +(r.filed?'Yes':'Not yet')+'</td></tr>';
  h+='</tbody></table>';
  h+='<p>An assessment raised on a year nobody filed is built from what the '
   +'Canada Revenue Agency could see rather than from the corporation&rsquo;s '
   +'own figures. The return for that year is what replaces those figures, '
   +'which is why filing it is the response rather than arguing about '
   +'them.</p>';
  if(!r.filed){
    h+='<p>So the order is: file the year that was assessed, and file any '
     +'other outstanding years with it, oldest first. '+QUALJS+'</p>';
  }else{
    h+='<p>With the return filed, the assessed figures have something to give '
     +'way to. What remains is processing rather than a dispute about the '
     +'numbers.</p>';
  }
  if(!r.nil){
    h+='<p>Where the year turns out not to have been nil, it is not one we '
     +'file. '+NOTNILJS+'</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T68 = dict(
 slug='arbitrary-assessment-response-checker',
 title='Arbitrary Assessment Response Checker | What Displaces It',
 h1_pre='Arbitrary Assessment ', h1_span='Response Checker',
 h1='Arbitrary Assessment Response Checker',
 eyebrow='CRA Letters',
 keyword='arbitrary assessment response checker',
 meta=('An assessment raised on a year nobody filed is displaced by the '
       'return for that year. Three answers set the order.'),
 tags=['Three answers', 'The return is the response',
       'Covers other open years', 'Carries the full qualification'],
 form=tool('The assessment',
           [yn('as', 'Has an assessment been raised for a year the '
                     'corporation did not file?'),
            yn('nil', 'Was that year in fact nil?'),
            yn('fl', 'Has the real return for that year been filed?')],
           'Answer the questions above.'),
 js=None,
 sections=[
  ('what-an-arbitrary-assessment-is', 'Built From the Outside',
   '<p>Where a year goes unfiled, an assessment can be raised for it without '
   'the corporation&rsquo;s figures. It is constructed from what the Canada '
   'Revenue Agency can see rather than from the books, which is why the '
   'numbers on it can look unrelated to a corporation that did nothing at '
   'all.</p>\n'
   '<p>The response is not an argument about those numbers. It is the return '
   'for that year, which is the document the figures were standing in '
   'for.</p>'),
  ('the-order', 'File the Assessed Year, and the Others With It',
   '<table class="ei-tbl"><thead><tr><th scope="col">Step</th>'
   '<th scope="col">Why in this order</th></tr></thead><tbody>\n'
   '<tr><td>1. The assessed year</td><td>Its return is what the assessed '
   'figures give way to</td></tr>\n'
   '<tr><td>2. Any earlier outstanding years</td><td>A T2 carries figures '
   'forward, so the years are assessed in order</td></tr>\n'
   '<tr><td>3. Any later outstanding years</td><td>Each one is its own return '
   'and its own year</td></tr>\n'
   '</tbody></table>\n'
   '<p>The '
   + a(T + 'catch-up-filing-schedule-generator/',
       'catch-up filing schedule generator')
   + ' lays the years out in order, and the '
   + a(T + 'cra-demand-to-file-deadline-calculator/',
       'CRA demand to file deadline calculator')
   + ' dates a demand letter where one came first.</p>'),
  ('what-a-nil-year-owes', 'What a Nil Year Owes on an Assessed Year',
   '<p>' + QUAL + '</p>\n'
   '<p>Which is the practical reason to file rather than wait. The year stays '
   'open until its return is in, and the return is the only thing that closes '
   'it.</p>'),
 ],
 faq=[
  ('How do I respond to an assessment for a year I did not file?',
   'By filing the return for that year. The assessment was built without the '
   'corporation&rsquo;s figures, and the return is what those figures give '
   'way to.'),
  ('Should I file the other outstanding years at the same time?',
   'Yes, oldest first. A T2 carries figures forward from the year before it, '
   'so the years are assessed in the order they fell due. Each one is its own '
   'return at ' + PRICE + '.'),
  ('What does a nil year owe on an assessed year?',
   QUAL),
 ],
)


# ------------------------------------------------------------------ 69. stub
T69_JS = RBASE + r"""
function stub(se,di,id){
  if(se===null){return null;}
  if(se==='n'){return {stub:false};}
  if(di===null){return null;}
  var d=parse(id);
  if(d===null||d===undefined){return {stub:true,di:di==='y',d:null};}
  return {stub:true,di:di==='y',d:d,due:dueDate(d)};
}
var out=document.getElementById('out');
function show(){
  var r=stub(pick('se'),pick('di'),'pe');
  if(r===null){out.innerHTML='<p>Answer the questions above.</p>';return;}
  var h;
  if(!r.stub){
    h='<h3>A full fiscal year, so no stub period</h3>';
    h+='<p>Where the period ran its full length there is one tax year and one '
     +'return, due six months after the year-end. A quiet one is a nil return '
     +'at '+PRICE_JS+'.</p>';
    h+='<p>'+DISC_JS+'</p>';
    out.innerHTML=h;return;
  }
  h='<h3>A stub period is its own tax year and its own return</h3>';
  h+='<p>A fiscal period that ended early is a short tax year, not an offcut '
   +'of the one around it. It has its own return, its own deadline six months '
   +'after it ends, and it carries the fee in its own right at '+PRICE_JS
   +'.</p>';
  if(r.d){
    h+='<p>The period you entered ends '+fmt(r.d)+', so its return is due '
     +fmt(r.due)+'.</p>';
  var fd=filingDate(r.d);
    if(fd.getTime()!==r.due.getTime()){
      h+='<p>'+fmt(r.due)+' is a Saturday, a Sunday or a public holiday '
       +'recognised by the Canada Revenue Agency, so a return received by '
       +fmt(fd)+' is on time.</p>';
    }
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">What created it</th>'
   +'<th scope="col">Your answer</th><th scope="col">What follows</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>A dissolution part-way through the year</td><td>'
   +(r.di?'Yes':'No')+'</td><td>'+(r.di?'The stub period is the final tax '
   +'year and its return is the final T2':'The stub period sits between two '
   +'ordinary years and both of those are returns as well')+'</td></tr>';
  h+='</tbody></table>';
  if(r.di){
    h+='<p>The <a href="/tools/dissolution-timeline-calculator/">dissolution '
     +'timeline calculator</a> puts that return in the order of the wind-up '
     +'steps around it.</p>';
  }else{
    h+='<p>A stub period created by a year-end change comes with the change '
     +'itself, and a change still needing approval is one we route '
     +'elsewhere. The <a href="/tools/year-end-change-approval-checker/">'
     +'year-end change approval checker</a> settles which case you are '
     +'in.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T69 = dict(
 slug='stub-period-return-checker',
 title='Stub Period Return Checker | A Short Year Is Still a Year',
 h1_pre='Stub Period ', h1_span='Return Checker',
 h1='Stub Period Return Checker',
 eyebrow='Short Tax Years',
 keyword='stub period return checker',
 meta=('A fiscal period that ended early is its own tax year with its own '
       'return and its own deadline. This dates it.'),
 tags=['Computed deadline', 'Covers a dissolution stub',
       'Covers a year-end change stub', 'Its own fee'],
 form=tool('Your fiscal period',
           [yn('se', 'Did a fiscal period end earlier than the usual '
                     'year-end?'),
            yn('di', 'Was that because the corporation was dissolved?'),
            date('pe', 'Date the short period ended')],
           'Answer the questions above.'),
 js=None,
 sections=[
  ('a-short-year-is-a-year', 'A Short Year Is a Whole Tax Year',
   '<p>A stub period is a fiscal period that ended before the usual year-end '
   'came round. It feels like a fragment and it is not: it is a tax year in '
   'its own right, with its own return, its own six-month deadline and its '
   'own fee.</p>\n'
   '<p>Which is the fact worth having before the work starts, because a '
   'year-end change creates two periods where there was one and both of them '
   'are returns.</p>'),
  ('two-ways-they-arise', 'The Two Things That Create One',
   '<table class="ei-tbl"><thead><tr><th scope="col">Cause</th>'
   '<th scope="col">What the stub period is</th>'
   '<th scope="col">Deadline</th></tr></thead><tbody>\n'
   '<tr><td>Dissolution part-way through a year</td><td>The final tax year, '
   'and its return is the final T2</td><td>Six months after the dissolution '
   'date</td></tr>\n'
   '<tr><td>A fiscal year-end change</td><td>The period closing the old '
   'year-end, with a new period opening after it</td><td>Six months after it '
   'ends</td></tr>\n'
   '</tbody></table>\n'
   '<p>The '
   + a(T + 'short-tax-year-deadline-calculator/',
       'short tax year deadline calculator')
   + ' dates one of these on its own, and the '
   + a(T + 'fiscal-period-length-calculator/',
       'fiscal period length calculator')
   + ' measures how long it ran.</p>'),
  ('the-fee-on-a-stub', 'The Fee Is Per Tax Year, Not Per Twelve Months',
   '<p>' + PRICE + ' is charged per tax year. A stub period is a tax year, so '
   'it carries the fee whether it ran eleven months or three weeks.</p>\n'
   '<p>That reads as a hard line and it is the honest one: the return is the '
   'same return, prepared and reviewed and transmitted the same way, whatever '
   'length the period was.</p>'),
 ],
 faq=[
  ('Does a stub period need its own T2?',
   'Yes. A fiscal period that ended early is a short tax year with its own '
   'return and its own deadline six months after it ends.'),
  ('Does a short period cost less?',
   'No. ' + PRICE + ' is charged per tax year, and a stub period is a tax '
   'year. The return is prepared, reviewed and transmitted the same way '
   'whatever length the period ran.'),
  ('What creates a stub period?',
   'Most often a dissolution part-way through a year, which makes the stub '
   'the final tax year, or a fiscal year-end change, which closes one period '
   'and opens another.'),
 ],
)


# -------------------------------------------------------------- 70. standing
T70_JS = RBASE + r"""
function standing(t2,ar,st){
  if(t2===null||ar===null||st===null){return null;}
  return {t2:t2==='y',ar:ar==='y',st:st==='y'};
}
var out=document.getElementById('out');
function show(){
  var r=standing(pick('t2'),pick('ar'),pick('st'));
  if(r===null){out.innerHTML='<p>Answer all three questions.</p>';return;}
  var behind=(r.t2?1:0)+(r.ar?1:0);
  var h;
  if(behind===0&&!r.st){
    h='<h3>Both records read as current</h3>';
    h+='<p>No outstanding T2 years and no outstanding registry filing means '
     +'both trails are up to date. They go out of step easily, so it is worth '
     +'knowing which is which: the next year will put one of them behind '
     +'again on its own.</p>';
    h+='<p>'+DISC_JS+'</p>';
    out.innerHTML=h;return;
  }
  h='<h3>'+(r.st?'Struck by the registry, and the tax account is separate'
   :(behind===2?'Both records are behind':'One record is behind'))+'</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Record</th>'
   +'<th scope="col">Behind?</th><th scope="col">What brings it current</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Corporate tax account, with the Canada Revenue Agency</td>'
   +'<td>'+(r.t2?'Yes':'No')+'</td><td>'+(r.t2?'Filing each outstanding T2, '
   +'oldest first':'Nothing outstanding')+'</td></tr>';
  h+='<tr><td>Registry record, with the incorporating registry</td><td>'
   +(r.ar?'Yes':'No')+'</td><td>'+(r.ar?'Filing the outstanding annual '
   +'return, which is a registry filing and not covered by the fee'
   :'Nothing outstanding')+'</td></tr>';
  h+='</tbody></table>';
  h+='<p>These are two trails with two keepers. Bringing one current does '
   +'nothing for the other, which is the part that catches people who filed '
   +'their returns and assumed the registry had noticed.</p>';
  if(r.st){
    h+='<p>Being struck does not cancel an outstanding T2. The corporate tax '
     +'account and the registry record are separate, so the years that were '
     +'open before the strike are open after it.</p>';
  }
  if(r.t2){
    h+='<p>Each outstanding nil year is '+PRICE_JS+', and they are filed '
     +'oldest first because a T2 carries figures forward from the year before '
     +'it.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T70 = dict(
 slug='cra-account-standing-checker',
 title='Account Standing Checker | Two Records, Two Keepers',
 h1_pre='CRA Account ', h1_span='Standing Checker',
 h1='CRA Account Standing Checker',
 eyebrow='Two Trails',
 keyword='cra account standing checker',
 meta=('A corporation has a tax record and a registry record. Three answers '
       'show which one is behind and what brings it current.'),
 tags=['Three answers', 'Separates the two records',
       'Covers being struck', 'Says which filings are outside the fee'],
 form=tool('Your two records',
           [yn('t2', 'Are any T2 years outstanding?'),
            yn('ar', 'Is a registry annual return outstanding?'),
            yn('st', 'Has the registry struck or dissolved the '
                     'corporation?')],
           'Answer all three questions.'),
 js=None,
 sections=[
  ('two-records', 'Two Records, Kept by Two Bodies',
   '<p>Every corporation has two standing records and they are kept in '
   'different places. The corporate tax account sits with the Canada Revenue '
   'Agency and is brought current by filing returns. The registry record sits '
   'with the registry the corporation was incorporated under and is brought '
   'current by filing an annual return.</p>\n'
   '<p>Neither one reports to the other. A corporation whose returns are all '
   'filed can be years behind at the registry, and a corporation in good '
   'standing at the registry can have an unfiled year from 2019.</p>'),
  ('which-fixes-which', 'What Each One Answers For',
   '<table class="ei-tbl"><thead><tr><th scope="col">Record</th>'
   '<th scope="col">Kept by</th><th scope="col">Brought current by</th>'
   '<th scope="col">Inside ' + PRICE + '</th></tr></thead><tbody>\n'
   '<tr><td>Corporate tax account</td><td>Canada Revenue Agency</td>'
   '<td>Filing each outstanding T2</td><td>Yes, per nil tax year</td></tr>\n'
   '<tr><td>Registry record</td><td>The incorporating registry</td>'
   '<td>Filing the outstanding annual return</td><td>No</td></tr>\n'
   '</tbody></table>\n'
   '<p>The '
   + a(T + 'unfiled-years-checker/', 'unfiled years checker')
   + ' lists the open tax years, and the '
   + a(T + 'annual-return-vs-tax-return-checker/',
       'annual return versus tax return checker')
   + ' separates the two filings where they are being confused for each '
   'other.</p>'),
  ('struck-is-not-settled', 'Being Struck Does Not Settle the Tax Years',
   '<p>Where a registry strikes a corporation for missed filings, the '
   'registry record closes. The tax account does not. An unfiled year that '
   'was open before the strike is open after it, because the two records are '
   'separate trails and only one of them was touched.</p>\n'
   '<p>The '
   + a(T + 'involuntary-dissolution-risk-checker/',
       'involuntary dissolution risk checker')
   + ' covers the registry side of that, and the open years remain what they '
   'were.</p>'),
 ],
 faq=[
  ('Does filing my T2 returns fix my registry standing?',
   'No. The corporate tax account and the registry record are separate trails '
   'with separate keepers. Filing returns brings the tax account current; the '
   'registry annual return brings the registry record current, and it is not '
   'covered by the fee.'),
  ('Does being struck cancel an unfiled T2?',
   'No. The years that were open before the strike are open after it. The '
   'registry closing its record does not close the tax account.'),
  ('Which of the two does this service file?',
   'The T2. Each outstanding nil year is ' + PRICE + '. Registry annual '
   'returns are filed with the registry and are not covered by the fee, and '
   'we tell you which ones you still owe.'),
 ],
)


TOOLS9 = [T61, T62, T63, T64, T65, T66, T67, T68, T69, T70]

SEO9 = {
 'year-end-change-approval-checker': (
  'Year-End Change Approval Checker',
  'Whether a fiscal year-end change needs CRA approval, and what you file '
  'either way. Nil T2 filing is $300.00 plus HST per tax year.'),
 't2-short-exclusion-checker': (
  'T2 Short Exclusion Checker',
  'The eight T2 Short conditions and which one excludes your corporation. '
  'The full T2 costs the same, at $300.00 plus HST per tax year.'),
 't2-short-ccpc-condition-checker': (
  'T2 Short CCPC Condition Checker',
  'Whether the corporation is a Canadian-controlled private corporation, '
  'which decides a T2 Short condition and nil eligibility here.'),
 'dissolution-timeline-calculator': (
  'Dissolution Timeline Calculator',
  'The final T2 deadline from your dissolution date, and the order of the '
  'wind-up steps around it, including those outside the fee.'),
 'payroll-account-closure-checker': (
  'Payroll Account Closure Checker',
  'What an open payroll account still expects, and what Form RC145 closes. '
  'An inactive T2 does not close a payroll account.'),
 'shareholder-register-completeness-checker': (
  'Shareholder Register Completeness Checker',
  'Whether your register holds what Schedule 50 needs for every shareholder '
  'at 10 per cent or more. Inside $300.00 plus HST per tax year.'),
 'due-to-versus-due-from-shareholder-checker': (
  'Due To Versus Due From Shareholder Checker',
  'Which direction a shareholder balance runs, and why either one makes GIFI '
  'Schedules 100, 125 and 141 required on a nil return.'),
 'arbitrary-assessment-response-checker': (
  'Arbitrary Assessment Response Checker',
  'An assessment raised on a year nobody filed is displaced by the return '
  'for that year. The order to file in, oldest year first.'),
 'stub-period-return-checker': (
  'Stub Period Return Checker',
  'A fiscal period that ended early is its own tax year with its own return '
  'and its own deadline. This dates it from the period end.'),
 'cra-account-standing-checker': (
  'CRA Account Standing Checker',
  'A corporation has a tax record and a registry record. Which one is '
  'behind, what brings it current, and which filings fall outside the fee.'),
}
for t in TOOLS9:
    t['seo_title'], t['seo_desc'] = SEO9[t['slug']]
    assert len(t['seo_title']) <= 60, (
        '%s: SEO title is %d characters' % (t['slug'], len(t['seo_title'])))
    assert 70 <= len(t['seo_desc']) <= 160, (
        '%s: SEO description is %d characters'
        % (t['slug'], len(t['seo_desc'])))
assert set(SEO9) == {t['slug'] for t in TOOLS9}, 'SEO9 does not match TOOLS9'

def wire(form):
    """Build the listener block from the form's own controls.

    Batch 8 hand-listed the selectors at the end of each module. That works
    until a form gains a row and the list does not, and a control nobody wired
    is a control that silently does nothing. Deriving the selectors from the
    form makes the two impossible to disagree, and the assertion below fails
    the build if a form has no controls at all.

    Both events are bound: radios fire change, a date or number field fires
    input as it is typed.
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


for t, js in zip(TOOLS9, [T61_JS, T62_JS, T63_JS, T64_JS, T65_JS,
                          T66_JS, T67_JS, T68_JS, T69_JS, T70_JS]):
    js = js + wire(t['form'])
    t['js'] = js if js.startswith(PRELUDE) else PRELUDE + js

# Every control the form renders must be read by the module, and every name
# the module reads must be a control the form renders. Both directions, because
# each has already gone wrong once: batch 8 shipped a guard that matched on
# id="..." anywhere and misfired on a label, and this batch passed parse() a
# value instead of a field id, so the field was never read at all.
for t in TOOLS9:
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

    # Literal presence rather than pick('name'), because tools 62 and 66 read
    # their groups from a table (pick(COND[i][0])) and never name one inline.
    # It still catches a control the module ignores altogether.
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

ORDER9 = ORDER8 + [t['slug'] for t in TOOLS9]
LINK_TITLE9 = dict(LINK_TITLE8, **{
 'year-end-change-approval-checker': 'Year-end change approval checker',
 't2-short-exclusion-checker': 'T2 Short exclusion checker',
 't2-short-ccpc-condition-checker': 'T2 Short CCPC condition checker',
 'dissolution-timeline-calculator': 'Dissolution timeline calculator',
 'payroll-account-closure-checker': 'Payroll account closure checker',
 'shareholder-register-completeness-checker':
     'Shareholder register completeness checker',
 'due-to-versus-due-from-shareholder-checker':
     'Due to versus due from shareholder checker',
 'arbitrary-assessment-response-checker':
     'Arbitrary assessment response checker',
 'stub-period-return-checker': 'Stub period return checker',
 'cra-account-standing-checker': 'CRA account standing checker',
})

SIBLINGS9 = {
 'year-end-change-approval-checker': [
   'year-end-change-impact-calculator', 'fiscal-period-length-calculator',
   'stub-period-return-checker'],
 't2-short-exclusion-checker': [
   't2-short-eligibility-checker', 'nil-return-vs-full-return-checker',
   't2-short-ccpc-condition-checker'],
 't2-short-ccpc-condition-checker': [
   't2-short-eligibility-checker', 'nil-t2-eligibility-checker',
   't2-short-exclusion-checker'],
 'dissolution-timeline-calculator': [
   'final-t2-return-due-date-calculator', 'dissolution-readiness-checker',
   'clearance-certificate-requirement-checker'],
 'payroll-account-closure-checker': [
   'cra-account-closure-sequencer', 't4-nil-filing-requirement-checker',
   'payroll-nil-remittance-checker'],
 'shareholder-register-completeness-checker': [
   'schedule-50-shareholder-threshold-checker',
   'share-capital-reporting-checker',
   'due-to-versus-due-from-shareholder-checker'],
 'due-to-versus-due-from-shareholder-checker': [
   'shareholder-loan-balance-checker', 'nil-gifi-balance-sheet-checker',
   'shareholder-register-completeness-checker'],
 'arbitrary-assessment-response-checker': [
   'cra-demand-to-file-deadline-calculator', 'unfiled-years-checker',
   'catch-up-filing-schedule-generator'],
 'stub-period-return-checker': [
   'short-tax-year-deadline-calculator', 'year-end-change-impact-calculator',
   'dissolution-timeline-calculator'],
 'cra-account-standing-checker': [
   'business-number-status-checker', 'involuntary-dissolution-risk-checker',
   'annual-return-vs-tax-return-checker'],
}

GUIDES9 = {
 'year-end-change-approval-checker': [
   ('choosing-and-changing-a-fiscal-year-end',
    'Choosing and changing a fiscal year-end'),
   ('t2-filing-deadlines', 'T2 filing deadlines')],
 't2-short-exclusion-checker': [
   ('t2-short-eligibility', 'T2 Short eligibility'),
   ('t2-schedules-on-a-nil-return', 'T2 schedules on a nil return')],
 't2-short-ccpc-condition-checker': [
   ('t2-short-eligibility', 'T2 Short eligibility'),
   ('nil-t2-return-complete-guide',
    'The complete guide to the nil T2 return')],
 'dissolution-timeline-calculator': [
   ('final-t2-and-dissolution', 'The final T2 and dissolution'),
   ('winding-up-an-inactive-corporation',
    'Winding up an inactive corporation')],
 'payroll-account-closure-checker': [
   ('cra-accounts-on-a-dormant-corporation',
    'CRA accounts on a dormant corporation'),
   ('winding-up-an-inactive-corporation',
    'Winding up an inactive corporation')],
 'shareholder-register-completeness-checker': [
   ('schedule-50-and-shareholder-reporting',
    'Schedule 50 and shareholder reporting'),
   ('gifi-schedules-100-125-141', 'GIFI Schedules 100, 125 and 141')],
 'due-to-versus-due-from-shareholder-checker': [
   ('gifi-schedules-100-125-141', 'GIFI Schedules 100, 125 and 141'),
   ('schedule-50-and-shareholder-reporting',
    'Schedule 50 and shareholder reporting')],
 'arbitrary-assessment-response-checker': [
   ('cra-demand-to-file-response', 'Responding to a CRA demand to file'),
   ('catch-up-unfiled-corporate-tax-returns',
    'Catching up on unfiled corporate tax returns')],
 'stub-period-return-checker': [
   ('choosing-and-changing-a-fiscal-year-end',
    'Choosing and changing a fiscal year-end'),
   ('t2-filing-deadlines', 'T2 filing deadlines')],
 'cra-account-standing-checker': [
   ('dormant-and-inactive-corporations', 'Dormant and inactive corporations'),
   ('provincial-and-federal-annual-returns',
    'Provincial and federal annual returns')],
}

_ORDER = set(ORDER9)
for t in TOOLS9:
    for s in SIBLINGS9[t['slug']]:
        assert s in _ORDER, '%s lists a sibling that does not exist: %s' % (
            t['slug'], s)
        assert s != t['slug'], '%s lists itself as a sibling' % t['slug']
        assert s in LINK_TITLE9, '%s has no link title' % s
    for g, _ttl in GUIDES9[t['slug']]:
        assert g in GUIDES_LIVE9, (
            '%s links to guide %s, which is not live' % (t['slug'], g))
assert set(SIBLINGS9) == {t['slug'] for t in TOOLS9}, 'SIBLINGS9 mismatch'
assert set(GUIDES9) == {t['slug'] for t in TOOLS9}, 'GUIDES9 mismatch'

# Body AND script links are both checked. Batch 8 checked sections and the
# form only; this batch puts links inside three of the modules, and an
# unchecked link in a script is exactly as dead as one in a paragraph.
for t in TOOLS9:
    _all = (' '.join(b for _, _, b in t['sections']) + t['form']
            + ' '.join(q + aa for q, aa in t['faq']) + t['js'])
    for s in set(_re.findall(r'/tools/([a-z0-9-]+)/', _all)):
        assert s in _ORDER, (
            '%s: links to /tools/%s/, which does not exist'
            % (t['slug'], s))
    for g in set(_re.findall(r'/guides/([a-z0-9-]+)/', _all)):
        assert g in GUIDES_LIVE9, (
            '%s: links to /guides/%s/, which is not live' % (t['slug'], g))

for t in TOOLS9:
    rel = [(T + s + '/', LINK_TITLE9[s]) for s in SIBLINGS9[t['slug']]]
    rel += [(G + g + '/', ttl) for g, ttl in GUIDES9[t['slug']]]
    rel.append((COST, 'Nil T2 filing cost'))
    t['related'] = rel


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'November 2, 2026', '2026-11-02'
    recs = []
    for t in TOOLS9:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2i-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-46s %6d bytes' % (r['slug'], len(r['content'].encode())))
