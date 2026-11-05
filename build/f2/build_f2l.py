#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 2 batch 12: tools 86 to 90, the registry side.

WHY THESE FIVE, AND WHY THEY COME FROM APPENDIX A

Batches 4 to 11 were built outside Appendix A, on the decision logged in
docs/decisions.md. That was never because the appendix had run out: it lists
all 150 Family 2 URLs, and 85 are live. So this batch goes back to it, and
every one of the five is an Appendix A URL:

  /ontario-business-registry-filing-checker/
  /schedule-546-ontario-annual-return-checker/
  /ontario-missed-annual-returns-calculator/
  /extra-provincial-registration-checker/
  /corporate-revival-requirement-checker/

They are also the thinnest part of the site. The /tools/ hub group "Annual
Returns and the Registry" carries four cards against seventeen for the
schedules, and the registry is where a dormant corporation's compliance gap
actually opens: /guides/provincial-and-federal-annual-returns/ calls confusing
the two returns "the most common compliance gap a dormant corporation has".

WHAT I DROPPED, AND THE ONE THAT MATTERED

/ontario-annual-return-deadline-calculator/ is in Appendix A and is the
obvious sixth. It cannot be built here. The guide's own dates table gives a
due window for two of the three filings and not for the third:

  T2 corporate tax return      | The fiscal year-end | Within 6 months
  Corporations Canada annual   | The anniversary date | Within 60 days
  Ontario annual return        | The tax year-end | Filed through the OBR

No window for Ontario, anywhere on the site or in the plan. A tool whose whole
output is a deadline cannot be built on a deadline nobody published, which is
the same test that kept signing-link-expiry-calculator out of batch 11 and
/compare/voluntary-disclosure-vs-plain-late-filing/ out of Family 7.

Also dropped: /ontario-annual-return-requirement-checker/, because the question
"do you owe an annual return as well as a T2" is already
annual-return-vs-tax-return-checker; /annual-return-late-fee-calculator/,
because no late fee figure is published; /gst-hst-filing-frequency-calculator/
and /small-supplier-threshold-calculator/, because both turn on Canada Revenue
Agency thresholds this site does not state.

THE OCTOBER 2021 CUTOVER IS DATED TO THE MONTH, NOT THE DAY

Tool 87 turns on it, and the guide says "Since October 2021" without a day. So
the tool compares against the first of October 2021 and words every output as
"from October 2021", never as a specific date. A day-exact boundary would be
inventing precision the source does not have.

AGREEING WITH WHAT IS ALREADY PUBLISHED

From /guides/provincial-and-federal-annual-returns/:

  "The Ontario Business Registry is the provincial system through which the
   annual return, address changes and director changes are filed. A
   corporation needs its Ontario corporation number and its registry access to
   use it."
  "An Ontario corporation files an annual return confirming its registered
   office address, its directors and its officers. It carries no tax and no
   payment."
  "Until 2021 this was filed alongside the T2. Since October 2021 it is filed
   through the Ontario Business Registry instead, and a corporation that has
   not looked at the rules since then is probably not filing it."
  "Because the filing moved out of the T2, nothing in the corporate tax return
   now prompts an owner to do it. The prompt has to come from the owner or the
   adviser."
  "A federal corporation files an annual return with Corporations Canada for
   $12.00."
  "A federally incorporated corporation operating in Ontario files both: the
   $12.00 Corporations Canada annual return and an Ontario filing. Federal
   incorporation does not remove the provincial obligation."
  "An annual return is not a tax filing, so having no income does not excuse
   it."
  "A missed annual return does not create tax. It creates a registry record
   that is out of date, and after enough missed years it creates a corporation
   the registry treats as abandoned."
  "The two trails are independent."
  "Where annual returns go unfiled for long enough, the registry may dissolve
   or strike the corporation. That is not dissolution for tax purposes, and it
   cancels no outstanding T2 return."
  "Alberta administers its own corporate income tax... It is not an annual
   return and it is not covered by the T2."
  "The CO-17 is a separate return, not a schedule of the T2."
  "Everywhere other than Alberta and Quebec, provincial and territorial
   corporate income tax is collected through the federal T2."
  Table: "Every other province and territory | No, collected through the T2 |
   Yes, with that jurisdiction's registry"

From /guides/winding-up-an-inactive-corporation/:

  "A corporation struck by a registry for failing to file its annual return
   has not been wound up. It has been dissolved involuntarily, with its tax
   years still open and nothing settled."
  "Registries provide for revival, which restores the corporation so the
   outstanding filings can be made and a proper wind-up completed. The open
   tax years survived the striking and are waiting."
  "A corporation found in this state is usually in it because the annual
   return lapsed, not because anyone decided to close it. The tax years are
   the part nobody looked at."
  "A corporation struck from a registry with unfiled tax years is in the worst
   of both positions: it cannot trade and it still owes returns."

WHAT NO TOOL HERE DOES

None of them files anything with a registry. Registry filings are not part of
nil T2 filing and are not covered by the fee, which every one of the five says
in its own words. The tools name what the registry wants; the corporation or
its adviser files it.
"""
import io, json, os
import re as _re

from build_f2 import (render, meta, yn, a, SITE, HUB, FORM, PRICE,
                      DATE_JS)
from build_f2b import tool, num, date, PICK, T, G, COST
from build_f2c import MONEY_JS, PRELUDE
from build_f2f import BASE, RBASE

HERE = os.path.dirname(os.path.abspath(__file__))
CMP = SITE + '/compare/'


def _tbl(head, rows):
    """A static reference table, in the markup every other batch uses."""
    return ('<table class="ei-tbl"><thead><tr>'
            + ''.join('<th scope="col">%s</th>' % h for h in head)
            + '</tr></thead><tbody>\n'
            + '\n'.join('<tr>' + ''.join('<td>%s</td>' % c for c in r)
                        + '</tr>' for r in rows)
            + '\n</tbody></table>')


NOT_A_TAX_FILING = ('An annual return is not a tax filing, so having no income '
                    'does not excuse it.')

# ------------------------------------ 86. Ontario Business Registry filings
T86_JS = RBASE + r"""
/* Each row is a filing that goes through the Ontario Business Registry, with
   the answer that puts it on the list. The "through the registry" column is a
   fixed property of the filing rather than something derived from the
   answers, so no later edit can turn one of these into a T2 matter. */
var OBR=[
 ['ar','The Ontario annual return',
  'Confirms the registered office address, the directors and the officers. It '
  +'carries no tax and no payment.'],
 ['addr','A change of registered office address',
  'Filed through the registry, which is where address changes go.'],
 ['dir','A change of directors or officers',
  'Filed through the registry, in the same place as the annual return.']
];
function show(){
  var need=[],wait=0,i,v,h,key;
  for(i=0;i<OBR.length;i++){
    v=pick(OBR[i][0]);
    if(v===null){wait++;continue;}
    if(v==='y'){need.push(OBR[i]);}
  }
  key=pick('key');
  if(key===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the four questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  if(need.length===0){
    h='<h3>Nothing on this list is outstanding</h3>';
    h+='<p>You answered no to all three, so the registry is not waiting on '
     +'anything just now. The annual return comes round again each year, '
     +'because it is tied to the tax year-end.</p>';
  }else{
    h='<h3>'+need.length+' filing'+(need.length===1?'':'s')
     +' through the Ontario Business Registry</h3>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Filing</th>'
     +'<th scope="col">Filed through the registry</th>'
     +'<th scope="col">What it is</th></tr></thead><tbody>';
    for(i=0;i<need.length;i++){
      h+='<tr><td>'+need[i][1]+'</td><td>Yes</td><td>'+need[i][2]
       +'</td></tr>';
    }
    h+='</tbody></table>';
  }
  if(key==='n'){
    h+='<p>A corporation needs its Ontario corporation number and its '
     +'registry access to use the Ontario Business Registry, so that comes '
     +'before any of these filings.</p>';
  }else{
    h+='<p>You have the corporation number and registry access, which is what '
     +'the registry asks for before any of these filings.</p>';
  }
  h+='<p>None of these is the T2, and none of them is part of nil T2 filing '
   +'at '+PRICE_JS+'. Filing the T2 does not satisfy an annual return, and '
   +'filing an annual return does not satisfy the T2.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var out=document.getElementById('out');
"""

T86 = dict(
 slug='ontario-business-registry-filing-checker',
 title='Ontario Business Registry Filing Checker | What Goes There',
 h1_pre='Ontario Business Registry ', h1_span='Filing Checker',
 h1='Ontario Business Registry Filing Checker',
 eyebrow='Registry',
 keyword='ontario business registry filings',
 seo_title='Ontario Business Registry Filing Checker',
 seo_desc=('The annual return, address changes and director changes go '
           'through the Ontario Business Registry. Four answers name which '
           'of them you owe.'),
 meta=('The annual return, address changes and director changes are filed '
       'through the Ontario Business Registry. None of them is the T2.'),
 tags=['Four answers', 'Registry filings only', 'Not part of the T2',
       'Corporation number needed'],
 form=tool('What the registry may be waiting for',
           [yn('ar', 'Is the Ontario annual return outstanding?'),
            yn('addr', 'Has the registered office address changed?'),
            yn('dir', 'Have the directors or officers changed?'),
            yn('key', 'Do you have the Ontario corporation number and '
                      'registry access?')],
           'Answer the four questions above.'),
 js=None,
 sections=[
  ('what-the-registry-is', 'What the Ontario Business Registry Is For',
   '<p>The Ontario Business Registry is the provincial system through which '
   'the annual return, address changes and director changes are filed. A '
   'corporation needs its Ontario corporation number and its registry access '
   'to use it.</p>\n'
   '<p>It is not where tax is filed. The T2 goes to the Canada Revenue '
   'Agency, and the two trails are independent: a corporation can be fully '
   'current on its T2 filings and still be out of date at the registry.</p>'),
  ('what-goes-where', 'What Goes to Which Body',
   _tbl(['Filing', 'Filed with', 'Carries tax'],
        [['The Ontario annual return', 'The Ontario Business Registry',
          'No. It carries no tax and no payment'],
         ['A change of registered office address',
          'The Ontario Business Registry', 'No'],
         ['A change of directors or officers',
          'The Ontario Business Registry', 'No'],
         ['The T2 corporate return', 'The Canada Revenue Agency',
          'Yes, where there is tax to carry']])
   + '\n<p>The '
   + a(T + 'annual-return-vs-tax-return-checker/',
       'annual return versus tax return checker')
   + ' separates the two filings, and the '
   + a(CMP + 'ontario-annual-return-vs-t2/',
       'Ontario annual return versus the T2')
   + ' sets them side by side.</p>'),
  ('nothing-prompts-it', 'Nothing in the T2 Prompts the Registry Filing',
   '<p>Until 2021 the Ontario annual return was filed alongside the T2, so '
   'one act covered both. Since October 2021 it is filed through the Ontario '
   'Business Registry instead.</p>\n'
   '<p>Because the filing moved out of the T2, nothing in the corporate tax '
   'return now prompts an owner to do it. The prompt has to come from the '
   'owner or the adviser, which is the whole reason this checker exists.</p>'),
 ],
 faq=[
  ('What is filed through the Ontario Business Registry?',
   'The annual return, changes of registered office address and changes of '
   'directors or officers. The T2 is not: it goes to the Canada Revenue '
   'Agency.'),
  ('What do I need to use the registry?',
   'The corporation&rsquo;s Ontario corporation number and its registry '
   'access. Without those, none of the filings can be made.'),
  ('Is any of this included in nil T2 filing?',
   'No. Registry filings are not part of nil T2 filing at $300.00 plus HST '
   'per tax year, and filing the T2 does not satisfy an annual return.'),
 ],
 related=[
  (T + 'annual-return-vs-tax-return-checker/',
   'Annual return versus tax return checker'),
  (T + 'schedule-546-ontario-annual-return-checker/',
   'Schedule 546 checker'),
  (T + 'ontario-missed-annual-returns-calculator/',
   'Ontario missed annual returns calculator'),
  (T + 'involuntary-dissolution-risk-checker/',
   'Involuntary dissolution risk checker'),
  (G + 'provincial-and-federal-annual-returns/',
   'The complete guide to provincial and federal annual returns'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ------------------------------------------------------- 87. Schedule 546
T87_JS = RBASE + r"""
/* The guide dates the cutover as "Since October 2021" with no day, so the
   boundary is the first of that month and every line of output says
   "October 2021" rather than a date. A day-exact answer would be inventing
   precision the source does not have. */
var CUT=u(2021,9,1);
function show(){
  var d=parse('ye'),h,before;
  if(d===null){out.innerHTML='<p>Enter the tax year-end above.</p>';return;}
  if(d===undefined){out.innerHTML='<p>That is not a date we can read.</p>';return;}
  before=(d.getTime()<CUT.getTime());
  if(before){
    h='<h3>That year travelled with the T2</h3>';
    h+='<p>For a tax year ending '+fmt(d)+', before October 2021, the Ontario '
     +'annual return was filed alongside the T2. One act covered both, which '
     +'is why nobody had to know the difference.</p>';
  }else{
    h='<h3>That year goes through the Ontario Business Registry</h3>';
    h+='<p>For a tax year ending '+fmt(d)+', from October 2021 onwards, the '
     +'Ontario annual return is filed through the Ontario Business Registry '
     +'instead of alongside the T2. It is a separate filing.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Tax year ending</th>'
   +'<th scope="col">Where the Ontario annual return went</th>'
   +'<th scope="col">Did the T2 carry it</th></tr></thead><tbody>';
  h+='<tr><td>Before October 2021</td>'
   +'<td>Alongside the T2</td><td>Yes</td></tr>';
  h+='<tr><td>From October 2021</td>'
   +'<td>Through the Ontario Business Registry</td><td>No</td></tr>';
  h+='<tr><td>Yours, ending '+fmt(d)+'</td><td>'
   +(before?'Alongside the T2':'Through the Ontario Business Registry')
   +'</td><td>'+(before?'Yes':'No')+'</td></tr>';
  h+='</tbody></table>';
  if(!before){
    h+='<p>Because the filing moved out of the T2, nothing in the corporate '
     +'tax return now prompts an owner to do it. A corporation that has not '
     +'looked at the rules since then is probably not filing it.</p>';
  }else{
    h+='<p>Later years are different. From October 2021 the filing moved to '
     +'the registry, so a corporation still assuming the T2 carries it is '
     +'probably not filing it at all.</p>';
  }
  h+='<p>Either way the annual return carries no tax and no payment, and it '
   +'is not part of nil T2 filing at '+PRICE_JS+'.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var out=document.getElementById('out');
"""

T87 = dict(
 slug='schedule-546-ontario-annual-return-checker',
 title='Schedule 546 Checker | Does the T2 Still Carry It',
 h1_pre='Schedule 546 ', h1_span='Ontario Annual Return Checker',
 h1='Schedule 546 Ontario Annual Return Checker',
 eyebrow='Registry',
 keyword='schedule 546 ontario annual return',
 seo_title='Schedule 546 Ontario Annual Return Checker',
 seo_desc=('The Ontario annual return travelled with the T2 until 2021. '
           'Enter a tax year-end to see which route applied to that year.'),
 meta=('The Ontario annual return travelled with the T2 until 2021 and goes '
       'through the Ontario Business Registry from October 2021.'),
 tags=['One date in', 'Dates the cutover', 'October 2021',
       'Separate filing now'],
 form=tool('Which tax year',
           [date('ye', 'The tax year-end')],
           'Enter the tax year-end above.'),
 js=None,
 sections=[
  ('what-changed', 'What Changed in October 2021',
   '<p>Until 2021 the Ontario annual return was filed alongside the T2. '
   'Since October 2021 it is filed through the Ontario Business Registry '
   'instead, and a corporation that has not looked at the rules since then '
   'is probably not filing it.</p>\n'
   '<p>That is the whole of it. The filing did not go away and it did not '
   'change what it reports: it changed where it goes, and the T2 stopped '
   'carrying it.</p>'),
  ('the-two-routes', 'The Two Routes, Either Side of the Cutover',
   _tbl(['Tax year ending', 'Where the annual return went', 'What prompted it'],
        [['Before October 2021', 'Alongside the T2',
          'Preparing the T2, because the two travelled together'],
         ['From October 2021', 'Through the Ontario Business Registry',
          'Nothing in the T2. The prompt has to come from the owner or the '
          'adviser']])
   + '\n<p>The '
   + a(T + 'ontario-business-registry-filing-checker/',
       'Ontario Business Registry filing checker')
   + ' names what else goes through the registry.</p>'),
  ('still-owed', 'The Annual Return Is Still Owed Either Way',
   '<p>An annual return confirms the registered office address, the '
   'directors and the officers, and it carries no tax and no payment. '
   + NOT_A_TAX_FILING + '</p>\n'
   '<p>So a dormant corporation owes one for every year, on whichever route '
   'applied to that year. Filing the T2 does not satisfy it, and filing it '
   'does not satisfy the T2.</p>'),
 ],
 faq=[
  ('Does the T2 still carry the Ontario annual return?',
   'Not for a tax year ending from October 2021. Until 2021 it was filed '
   'alongside the T2; since then it goes through the Ontario Business '
   'Registry.'),
  ('Why do people still think it travels with the T2?',
   'Because it did until 2021, and because nothing in the corporate tax '
   'return now prompts an owner to file it separately.'),
  ('Does a dormant corporation still owe one?',
   'Yes. An annual return confirms directors and the registered office '
   'rather than income, so having no activity does not excuse it.'),
 ],
 related=[
  (T + 'ontario-business-registry-filing-checker/',
   'Ontario Business Registry filing checker'),
  (T + 'ontario-missed-annual-returns-calculator/',
   'Ontario missed annual returns calculator'),
  (T + 'annual-return-vs-tax-return-checker/',
   'Annual return versus tax return checker'),
  (T + 'nil-t2-deadline-calculator/', 'Nil T2 deadline calculator'),
  (G + 'provincial-and-federal-annual-returns/',
   'The complete guide to provincial and federal annual returns'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# -------------------------------- 88. Ontario missed annual returns counter
T88_JS = RBASE + r"""
function show(){
  var d=parse('last'),h,i,n,y,now,rows;
  if(d===null){
    out.innerHTML='<p>Enter the tax year-end of the last annual return that '
     +'was filed.</p>';return;}
  if(d===undefined){out.innerHTML='<p>That is not a date we can read.</p>';return;}
  now=today();
  if(d.getTime()>now.getTime()){
    out.innerHTML='<p>That date is in the future. Enter the tax year-end of '
     +'the last annual return that was actually filed.</p>';return;}
  rows=[];n=0;
  for(i=1;i<=40;i++){
    y=addYear(d,i);
    if(y.getTime()>now.getTime()){break;}
    n++;rows.push(y);
  }
  if(n===0){
    h='<h3>Nothing outstanding yet</h3>';
    h+='<p>The last annual return covered the tax year ending '+fmt(d)
     +', and the next tax year-end has not passed. Nothing is outstanding at '
     +'the registry on this count.</p>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Tax year ending</th>'
     +'<th scope="col">Annual return</th></tr></thead><tbody>';
    h+='<tr><td>'+fmt(d)+'</td><td>Filed</td></tr>';
    h+='<tr><td>'+fmt(addYear(d,1))+'</td><td>Not yet reached</td></tr>';
    h+='</tbody></table>';
  }else{
    h='<h3>'+plural(n,'annual return')+' outstanding</h3>';
    h+='<p>The last one covered the tax year ending '+fmt(d)+'. Since then '
     +plural(n,'tax year-end')+' '+(n===1?'has':'have')+' passed, and each '
     +'one owes its own annual return.</p>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Tax year ending</th>'
     +'<th scope="col">Annual return</th></tr></thead><tbody>';
    h+='<tr><td>'+fmt(d)+'</td><td>Filed</td></tr>';
    for(i=0;i<rows.length;i++){
      h+='<tr><td>'+fmt(rows[i])+'</td><td>Outstanding</td></tr>';
    }
    h+='</tbody></table>';
    h+='<p>A missed annual return does not create tax. It creates a registry '
     +'record that is out of date, and after enough missed years it creates a '
     +'corporation the registry treats as abandoned.</p>';
  }
  h+='<p>The T2 side is separate and runs on its own count: the two trails '
   +'are independent, so this says nothing about whether the tax years are '
   +'filed. Nil T2 filing is '+PRICE_JS+' and does not include a registry '
   +'filing.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var out=document.getElementById('out');
"""

T88 = dict(
 slug='ontario-missed-annual-returns-calculator',
 title='Ontario Missed Annual Returns | How Many Are Outstanding',
 h1_pre='Ontario Missed ', h1_span='Annual Returns Calculator',
 h1='Ontario Missed Annual Returns Calculator',
 eyebrow='Registry',
 keyword='ontario missed annual returns',
 seo_title='Ontario Missed Annual Returns Calculator',
 seo_desc=('One annual return falls due for each tax year. Enter the year-end '
           'of the last one filed to count how many are outstanding since.'),
 meta=('One annual return falls due for each tax year. Enter the year-end of '
       'the last one filed to count what is outstanding since.'),
 tags=['One date in', 'Counts the years', 'Registry record only',
       'Separate from the T2'],
 form=tool('The last annual return filed',
           [date('last', 'Tax year-end it covered')],
           'Enter the tax year-end of the last annual return filed.'),
 js=None,
 sections=[
  ('one-per-year', 'One Annual Return for Each Tax Year',
   '<p>The Ontario annual return is tied to the tax year-end, so one falls '
   'due for each tax year the corporation exists. Missing a year does not '
   'remove it: the next year adds its own, and they accumulate.</p>\n'
   '<p>' + NOT_A_TAX_FILING + ' A dormant corporation confirms its directors '
   'and its registered office every year in exactly the way an active one '
   'does.</p>'),
  ('what-a-miss-costs', 'What a Missed Year Actually Causes',
   _tbl(['Missed', 'What it creates', 'What it does not create'],
        [['One annual return', 'A registry record that is out of date',
          'Any tax'],
         ['Several annual returns',
          'A corporation the registry treats as abandoned', 'Any tax'],
         ['Enough of them',
          'A registry that may dissolve or strike the corporation',
          'Dissolution for tax purposes, and it cancels no outstanding T2 '
          'return']])
   + '\n<p>The '
   + a(T + 'involuntary-dissolution-risk-checker/',
       'involuntary dissolution risk checker')
   + ' takes being struck, and the '
   + a(T + 'corporate-revival-requirement-checker/',
       'corporate revival requirement checker')
   + ' takes what happens after it.</p>'),
  ('two-counts', 'The Registry Count and the Tax Count Are Separate',
   '<p>The two trails are independent. A corporation can be fully current on '
   'its T2 filings and still be struck from its registry, and it can be in '
   'good standing at the registry while owing ten years of T2 returns.</p>\n'
   '<p>So this count answers one of the two questions. The '
   + a(T + 'unfiled-years-checker/', 'unfiled years checker')
   + ' answers the other.</p>'),
 ],
 faq=[
  ('How many annual returns do I owe?',
   'One for each tax year since the last one filed. The calculator above '
   'counts the tax year-ends that have passed.'),
  ('Does a missed annual return create tax?',
   'No. It creates a registry record that is out of date, and after enough '
   'missed years a corporation the registry treats as abandoned.'),
  ('Does this tell me whether my T2 returns are filed?',
   'No. The two trails are independent, so a clean registry record says '
   'nothing about the tax years and the reverse is also true.'),
 ],
 related=[
  (T + 'ontario-business-registry-filing-checker/',
   'Ontario Business Registry filing checker'),
  (T + 'involuntary-dissolution-risk-checker/',
   'Involuntary dissolution risk checker'),
  (T + 'corporate-revival-requirement-checker/',
   'Corporate revival requirement checker'),
  (T + 'unfiled-years-checker/', 'Unfiled years checker'),
  (G + 'provincial-and-federal-annual-returns/',
   'The complete guide to provincial and federal annual returns'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ------------------------------------- 89. Extra-provincial registration
T89_JS = RBASE + r"""
function show(){
  var fed=pick('fed'),ont=pick('ont'),oth=pick('oth'),pe=pick('pe'),
      h,wait=0,rows=[];
  if(fed===null){wait++;}
  if(ont===null){wait++;}
  if(oth===null){wait++;}
  if(pe===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the four questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  if(fed==='y'){
    rows.push(['Corporations Canada',
      'An annual return for $12.00, within 60 days of the anniversary date',
      'Registry filing']);
  }
  if(ont==='y'){
    rows.push(['The Ontario Business Registry',
      'An Ontario annual return, carrying no tax and no payment',
      'Registry filing']);
  }
  if(oth==='y'){
    rows.push(['Each other province or territory it is registered in',
      'An annual return with that jurisdiction&rsquo;s registry',
      'Registry filing']);
  }
  if(pe==='y'){
    rows.push(['Alberta or Quebec',
      'The AT1 or the CO-17, a separate provincial income tax return',
      'Income tax return, not an annual return']);
  }
  if(rows.length===0){
    h='<h3>Nothing on this list applies</h3>';
    h+='<p>You answered no to all four, so no registry annual return and no '
     +'separate provincial income tax return arises from them. The T2 is '
     +'still owed for every tax year.</p>';
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  h='<h3>'+plural(rows.length,'filing')+' outside the T2</h3>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Filed with</th>'
   +'<th scope="col">What it wants</th><th scope="col">What kind of filing</th>'
   +'</tr></thead><tbody>';
  for(var i=0;i<rows.length;i++){
    h+='<tr><td>'+rows[i][0]+'</td><td>'+rows[i][1]+'</td><td>'+rows[i][2]
     +'</td></tr>';
  }
  h+='</tbody></table>';
  if(fed==='y'&&ont==='y'){
    h+='<p>A federally incorporated corporation operating in Ontario files '
     +'both: the $12.00 Corporations Canada annual return and an Ontario '
     +'filing. Federal incorporation does not remove the provincial '
     +'obligation.</p>';
  }
  if(pe==='y'){
    h+='<p>Alberta and Quebec administer their own corporate income tax, so '
     +'the AT1 and the CO-17 are separate returns rather than annual '
     +'returns. Neither is covered by the T2 and neither is included in '
     +PRICE_JS+'. Everywhere other than Alberta and Quebec, provincial and '
     +'territorial corporate income tax is collected through the federal '
     +'T2.</p>';
  }
  h+='<p>None of these is part of nil T2 filing. The fee of '+PRICE_JS
   +' covers the federal nil T2 corporate tax return.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var out=document.getElementById('out');
"""

T89 = dict(
 slug='extra-provincial-registration-checker',
 title='Extra-Provincial Registration Checker | Which Registry Wants What',
 h1_pre='Extra-Provincial ', h1_span='Registration Checker',
 h1='Extra-Provincial Registration Checker',
 eyebrow='Registry',
 keyword='extra provincial registration annual return',
 seo_title='Extra-Provincial Registration Checker',
 seo_desc=('A corporation registered in more than one place owes each '
           'registry an annual return. Four answers name which ones, and '
           'which provinces want a tax return too.'),
 meta=('A corporation registered in more than one place owes each registry '
       'an annual return. Federal incorporation removes no provincial '
       'obligation.'),
 tags=['Four answers', 'Registry by registry', 'AT1 and CO-17 separate',
       'None inside the fee'],
 form=tool('Where the corporation is registered',
           [yn('fed', 'Is it federally incorporated?'),
            yn('ont', 'Is it registered in Ontario?'),
            yn('oth', 'Is it registered in any other province or territory?'),
            yn('pe', 'Does it have a permanent establishment in Alberta or '
                     'Quebec?')],
           'Answer the four questions above.'),
 js=None,
 sections=[
  ('each-registry', 'Each Registry Wants Its Own Annual Return',
   '<p>A federal corporation files an annual return with Corporations Canada '
   'for $12.00. An Ontario corporation files one through the Ontario '
   'Business Registry. A corporation registered in another province files '
   'with that jurisdiction&rsquo;s registry.</p>\n'
   '<p>A federally incorporated corporation operating in Ontario files both: '
   'the $12.00 Corporations Canada annual return and an Ontario filing. '
   'Federal incorporation does not remove the provincial obligation.</p>'),
  ('annual-return-or-tax-return', 'An Annual Return Is Not a Tax Return',
   _tbl(['Jurisdiction', 'Its own corporate income tax return',
         'A registry annual return'],
        [['Alberta', 'Yes, the AT1', 'Yes'],
         ['Quebec', 'Yes, the CO-17', 'Yes'],
         ['Ontario', 'No, collected through the T2',
          'Yes, through the Ontario Business Registry'],
         ['Every other province and territory',
          'No, collected through the T2',
          'Yes, with that jurisdiction&rsquo;s registry']])
   + '\n<p>The '
   + a(T + 'provincial-return-requirement-checker/',
       'provincial return requirement checker')
   + ' takes the income tax side on its own.</p>'),
  ('none-inside-the-fee', 'None of It Is Inside the Nil T2 Fee',
   '<p>Registry annual returns, the Alberta AT1 and the Quebec CO-17 are '
   'separate filings and are not included in the fee. The fee of ' + PRICE
   + ' covers the federal nil T2 corporate tax return.</p>\n'
   '<p>' + NOT_A_TAX_FILING + ' So a dormant corporation registered in three '
   'places owes three annual returns and a T2, and none of the four '
   'satisfies any of the others.</p>'),
 ],
 faq=[
  ('Does federal incorporation cover the provinces?',
   'No. A federally incorporated corporation operating in Ontario files both '
   'the $12.00 Corporations Canada annual return and an Ontario filing. '
   'Federal incorporation does not remove the provincial obligation.'),
  ('Is the Alberta AT1 an annual return?',
   'No. Alberta administers its own corporate income tax, so the AT1 is a '
   'separate provincial income tax return. The same is true of the Quebec '
   'CO-17.'),
  ('Are any of these inside the nil T2 fee?',
   'No. Registry annual returns, the AT1 and the CO-17 are separate filings. '
   'The fee covers the federal nil T2 corporate tax return.'),
 ],
 related=[
  (T + 'provincial-return-requirement-checker/',
   'Provincial return requirement checker'),
  (T + 'federal-annual-return-anniversary-calculator/',
   'Federal annual return anniversary calculator'),
  (T + 'ontario-business-registry-filing-checker/',
   'Ontario Business Registry filing checker'),
  (T + 'annual-return-vs-tax-return-checker/',
   'Annual return versus tax return checker'),
  (G + 'quebec-co17-and-alberta-at1/',
   'The complete guide to Quebec CO-17 and Alberta AT1'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# -------------------------------------------- 90. Corporate revival checker
T90_JS = RBASE + r"""
function show(){
  var st=pick('struck'),yr=pick('years'),wd=pick('wind'),h,wait=0;
  if(st===null){wait++;}
  if(yr===null){wait++;}
  if(wd===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  if(st==='n'){
    h='<h3>Revival does not arise</h3>';
    h+='<p>The corporation has not been struck, so there is nothing to '
     +'restore. What the registry wants is the outstanding annual returns, '
     +'and what the Canada Revenue Agency wants is the outstanding tax '
     +'years.</p>';
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Step</th>'
     +'<th scope="col">Applies</th></tr></thead><tbody>';
    h+='<tr><td>Revival with the registry</td><td>No</td></tr>';
    h+='<tr><td>Outstanding annual returns</td><td>'
     +'Still owed to the registry</td></tr>';
    h+='<tr><td>Outstanding tax years</td><td>'
     +(yr==='y'?'Yes, and still open':'None reported')+'</td></tr>';
    h+='</tbody></table>';
    h+='<p>'+DISC_JS+'</p>';out.innerHTML=h;return;
  }
  h='<h3>Struck, not wound up</h3>';
  h+='<p>A corporation struck by a registry for failing to file its annual '
   +'return has not been wound up. It has been dissolved involuntarily, with '
   +'its tax years still open and nothing settled.</p>';
  h+='<table class="ei-tbl"><thead><tr><th scope="col">What</th>'
   +'<th scope="col">Where it stands</th></tr></thead><tbody>';
  h+='<tr><td>The corporation&rsquo;s existence</td>'
   +'<td>Ended by the registry, and restorable by revival</td></tr>';
  h+='<tr><td>The outstanding tax years</td><td>'
   +(yr==='y'
     ? 'Survived the striking and are waiting'
     : 'None reported, but the striking cancelled nothing either way')
   +'</td></tr>';
  h+='<tr><td>Being struck as a tax event</td>'
   +'<td>Not dissolution for tax purposes, and it cancels no outstanding T2 '
   +'return</td></tr>';
  h+='<tr><td>Revival</td><td>Restores the corporation so the outstanding '
   +'filings can be made</td></tr>';
  h+='</tbody></table>';
  if(yr==='y'){
    h+='<p>A corporation struck from a registry with unfiled tax years is in '
     +'the worst of both positions: it cannot trade and it still owes '
     +'returns.</p>';
  }
  if(wd==='y'){
    h+='<p>To wind it up properly the corporation is revived first, because a '
     +'proper wind-up needs the outstanding filings made and a clearance '
     +'certificate, and a clearance certificate cannot be issued while a '
     +'year is unfiled.</p>';
  }else{
    h+='<p>Where there is no intention to wind it up, the outstanding tax '
     +'years are still open and still owed. The striking did not close '
     +'them.</p>';
  }
  h+='<p>A corporation found in this state is usually in it because the '
   +'annual return lapsed, not because anyone decided to close it. The tax '
   +'years are the part nobody looked at, and each quiet one is '+PRICE_JS
   +'.</p>';
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
var out=document.getElementById('out');
"""

T90 = dict(
 slug='corporate-revival-requirement-checker',
 title='Corporate Revival Requirement Checker | Struck, Not Closed',
 h1_pre='Corporate Revival ', h1_span='Requirement Checker',
 h1='Corporate Revival Requirement Checker',
 eyebrow='Registry',
 keyword='corporate revival after being struck',
 seo_title='Corporate Revival Requirement Checker',
 seo_desc=('Being struck by a registry is not a wind-up. Three answers show '
           'what revival restores and which tax years survived the '
           'striking.'),
 meta=('Being struck by a registry is not a wind-up. What revival restores, '
       'and which tax years survived the striking.'),
 tags=['Three answers', 'Struck is not dissolved', 'Tax years survive',
       'Revival restores'],
 form=tool('Where the corporation stands',
           [yn('struck', 'Has the registry struck or dissolved the '
                         'corporation?'),
            yn('years', 'Are there unfiled tax years?'),
            yn('wind', 'Do you intend to wind it up properly?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('struck-is-not-closed', 'Struck Is Not Wound Up',
   '<p>A corporation struck by a registry for failing to file its annual '
   'return has not been wound up. It has been dissolved involuntarily, with '
   'its tax years still open and nothing settled.</p>\n'
   '<p>A corporation found in this state is usually in it because the annual '
   'return lapsed, not because anyone decided to close it. The tax years are '
   'the part nobody looked at.</p>'),
  ('what-survives', 'What the Striking Did and Did Not Do',
   _tbl(['What', 'Effect of being struck'],
        [['The corporation&rsquo;s existence',
          'Ended by the registry, and restorable by revival'],
         ['The outstanding tax years',
          'Survived the striking and are waiting'],
         ['As a tax event',
          'Not dissolution for tax purposes, and it cancels no outstanding '
          'T2 return'],
         ['Trading', 'It cannot trade while struck']])
   + '\n<p>The '
   + a(T + 'post-dissolution-return-checker/',
       'post-dissolution return checker')
   + ' takes what is still owed afterwards, and the '
   + a(T + 'involuntary-dissolution-risk-checker/',
       'involuntary dissolution risk checker')
   + ' takes how a corporation gets here.</p>'),
  ('revival', 'What Revival Is For',
   '<p>Registries provide for revival, which restores the corporation so the '
   'outstanding filings can be made and a proper wind-up completed.</p>\n'
   '<p>So revival is the step that makes the rest possible rather than an '
   'end in itself. A corporation struck from a registry with unfiled tax '
   'years is in the worst of both positions: it cannot trade and it still '
   'owes returns. The '
   + a(CMP + 'dissolving-vs-filing-nil-every-year/',
       'dissolving versus filing nil every year')
   + ' comparison sets out what a completed wind-up ends.</p>'),
 ],
 faq=[
  ('My corporation was struck off. Is it closed?',
   'Not for tax purposes. It was dissolved involuntarily, with its tax years '
   'still open and nothing settled.'),
  ('Did being struck cancel my outstanding T2 returns?',
   'No. Being struck is not dissolution for tax purposes and it cancels no '
   'outstanding T2 return. The open years survived it.'),
  ('What does revival do?',
   'It restores the corporation so the outstanding filings can be made and a '
   'proper wind-up completed.'),
 ],
 related=[
  (T + 'involuntary-dissolution-risk-checker/',
   'Involuntary dissolution risk checker'),
  (T + 'post-dissolution-return-checker/',
   'Post-dissolution return checker'),
  (T + 'ontario-missed-annual-returns-calculator/',
   'Ontario missed annual returns calculator'),
  (T + 'dissolution-readiness-checker/', 'Dissolution readiness checker'),
  (G + 'winding-up-an-inactive-corporation/',
   'The complete guide to winding up an inactive corporation'),
  (COST, 'Nil T2 filing cost'),
 ],
)

TOOLS12 = [T86, T87, T88, T89, T90]

STRUCTURE = dict(sections=3, faq=3, related=6, tags=4,
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


for _t, _js in zip(TOOLS12, [T86_JS, T87_JS, T88_JS, T89_JS, T90_JS]):
    _js = _js + wire(_t['form'])
    _t['js'] = _js if _js.startswith(PRELUDE) else PRELUDE + _js

# ---- the contract, asserted rather than trusted ---------------------------
# Batch 11 asserted "exactly 80 already built" and batch 10 "exactly 70", and
# both broke the moment the next batch landed. The intent in each case was
# that nothing EARLIER has gone missing, which is a subset test, so that is
# what this is. It survives batch 13.
_LIVE = {f[:-5] for f in os.listdir(HERE) if f.endswith('.html')}
_THIS = {t['slug'] for t in TOOLS12}
_EARLIER = _LIVE - _THIS
assert len(_EARLIER) >= 85, (
    'expected at least the 85 tools of batches 1 to 11, found %d'
    % len(_EARLIER))
PUBLISHED = _THIS <= _LIVE

for t in TOOLS12:
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

    _all = (t['form'] + ''.join(h for _i, _h2, h in t['sections'])
            + ''.join(q + aa for q, aa in t['faq'])
            + ''.join(u2 for u2, _x in t['related']) + t['js'])
    # every internal tool link points at something that exists
    for u in _re.findall(r'href="' + SITE + r'/tools/([a-z0-9-]+)/"', _all):
        assert u in _LIVE or u in _THIS, '%s: links to missing tool %s' % (s, u)
    # every comparison link points at one of the thirteen F7 pages
    _F7 = {f[:-5] for f in os.listdir(os.path.join(HERE, '..', 'f7'))
           if f.endswith('.html')}
    for u in _re.findall(r'href="' + SITE + r'/compare/([a-z0-9-]+)/"', _all):
        assert u in _F7, '%s: links to missing comparison %s' % (s, u)

assert len({t['seo_title'] for t in TOOLS12}) == len(TOOLS12), 'title clash'
assert len({t['seo_desc'] for t in TOOLS12}) == len(TOOLS12), 'desc clash'
assert len({t['keyword'] for t in TOOLS12}) == len(TOOLS12), 'keyword clash'
assert len({t['h1'] for t in TOOLS12}) == len(TOOLS12), 'h1 clash'


if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'November 5, 2026', '2026-11-05'
    recs = []
    for t in TOOLS12:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2l-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-46s %6d bytes' % (r['slug'], len(r['content'].encode())))
