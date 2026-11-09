#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 2 batch 14: tools 96 to 100.

Why these five
--------------
All five are Appendix A URLs. They were chosen on 2026-11-09 by scoring the
90 remaining Appendix A entries against the 95 pages already live: 37 are
near-duplicates of a live page under another name, and most of the rest turn
on a figure this site does not publish. These five score 0.00 to 0.33 against
anything live and need no unpublished figure:

  /permanent-establishment-checker/
  /carrying-on-business-in-canada-checker/
  /non-resident-corporation-filing-checker/
  /outstanding-returns-count-checker/
  /schedule-11-shareholder-transactions-checker/

What was refused, and why
-------------------------
Checked on 2026-11-09 and nothing is published for any of these, so every tool
that depends on one stays unbuilt: the T1135 $100,000 threshold, the GST/HST
$30,000 small-supplier threshold, GIFI code numbers, the Ontario corporate
key, subsection 15(2), non-resident directors, the Ontario initial-return
window, prescribed interest rates (instalment interest, arrears interest),
Part XIII and Regulation 105 withholding rates, branch tax, the small business
deduction limit and the taxable capital thresholds. A tool may not be the
first place a figure appears on this site.

/nil-t2-price-with-hst-calculator/ is refused for a different reason worth
recording: its whole output is HST arithmetic on the fee, and the fee wording
is the one standing contradiction on this project. Hard rule 9 says "$300
including HST" and every page says "plus HST" on a logged deviation. That tool
cannot be built until the wording is settled.

Schedule 11 is in, and Schedule 1 is still out
----------------------------------------------
Schedule 1 was refused in batch 13 because /guides/t2-schedules-on-a-nil-
return/ answers "which schedules a nil return needs" with a closed list that
excludes it, so a tool asserting a nil return carries Schedule 1 would
contradict the published guide.

Schedule 11 does not have that problem, and the difference is the whole
reason it is here. For a typical nil year the honest answer is that there was
no transaction with a shareholder, so the schedule has nothing to report. That
agrees with the guide's list rather than contradicting it. Tool 100 is
therefore written to separate a transaction in the year from a standing
balance carried from an earlier one, and it never says a nil return must file
the schedule.

Agreeing with what is already published
---------------------------------------
From Family 1 and the provincial guide:

  "A corporation with a Quebec permanent establishment files both."
  "A corporation with an Alberta permanent establishment files both."
  "A corporation with a Quebec or Alberta permanent establishment needs work
   this service does not price, and pretending otherwise would be worse than
   saying so."
  "A fixed place through which the corporation carries on business, which for
   a dormant corporation is generally its registered office."
  "A corporation can hold a bank account, own assets and stay registered for
   years without carrying on business, and every one of those years is nil."
  "$25.00 per day up to $2,500.00" for a non-resident-owned corporation.

Tool 96 therefore says CO-17 and AT1 are separate returns wherever it names
them, which hard rule 8 requires, and says plainly that a corporation with
such an establishment is not priced by this service.
"""
import io, json, os
import re as _re

from build_f2 import (render, meta, yn, a, SITE, HUB, FORM, PRICE, NOT_NIL,
                      DATE_JS)
from build_f2b import tool, num, date, PICK, T, G, COST
from build_f2c import MONEY_JS, PRELUDE
from build_f2f import BASE, RBASE

HERE = os.path.dirname(os.path.abspath(__file__))

SCHED_GUIDE = G + 't2-schedules-on-a-nil-return/'
PROV_GUIDE = G + 'quebec-co17-and-alberta-at1/'
NR_GUIDE = G + 'non-resident-owned-corporation-nil-filing/'
ZERO_GUIDE = G + 'zero-activity-corporate-tax-returns/'
CATCHUP_GUIDE = G + 'catch-up-unfiled-corporate-tax-returns/'
DEADLINE_GUIDE = G + 't2-filing-deadlines/'

NOT_PRICED = ('A corporation with a Quebec or Alberta permanent establishment '
              'needs work this service does not price, and pretending '
              'otherwise would be worse than saying so.')


def _tbl(head, rows):
    return ('<table class="ei-tbl"><thead><tr>'
            + ''.join('<th scope="col">%s</th>' % h for h in head)
            + '</tr></thead><tbody>\n'
            + '\n'.join('<tr>' + ''.join('<td>%s</td>' % c for c in r)
                        + '</tr>' for r in rows)
            + '\n</tbody></table>')


# Each page closes in its own words. A shared closing sentence was the defect
# gate_f2_all.py caught on batch 13, so the per-page close is asserted below.
CLOSE = {
 'permanent-establishment-checker':
   'Where the corporation has its fixed place of business is a different '
   'question from whether the year was nil, and this page answers only the '
   'first.',
 'carrying-on-business-in-canada-checker':
   'Holding things is not the same as doing things, and that distinction is '
   'the whole of this page.',
 'non-resident-corporation-filing-checker':
   'Who owns the corporation changes what a late return costs. It does not '
   'change whether one is owed.',
 'outstanding-returns-count-checker':
   'The count is the easy part. Filing them oldest first is the part that '
   'closes the years.',
 'schedule-11-shareholder-transactions-checker':
   'A balance that sat still all year is not a transaction, and that is why '
   'most dormant years have nothing for this schedule to report.',
}

# ------------------------------------------- 96. permanent establishment
T96_JS = RBASE + 'var NOTPRICEDJS=' + json.dumps(NOT_PRICED) \
    + ';\n' + r"""
var out=document.getElementById('out');
function show(){
  var qc=pick('qc'),ab=pick('ab'),only=pick('only'),wait=0,h;
  if(qc===null){wait++;}
  if(ab===null){wait++;}
  if(only===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  var prov=[];
  if(qc==='y'){prov.push(['Quebec','CO-17','Quebec administers its own '
    +'corporate income tax, so the CO-17 is a separate return']);}
  if(ab==='y'){prov.push(['Alberta','AT1','Alberta administers its own '
    +'corporate income tax, so the AT1 is a separate return']);}
  if(prov.length===0){
    h='<h3>No Quebec or Alberta establishment on these answers</h3>';
    h+='<p>Neither of the two provinces that collect their own corporate '
     +'income tax has a fixed place of business here, so neither the CO-17 '
     +'nor the AT1 arises from this question.</p>';
  }else{
    h='<h3>'+prov.length+' separate provincial return'
     +(prov.length===1?'':'s')+' on these answers</h3>';
    h+='<p>A fixed place of business in a province that collects its own '
     +'corporate income tax brings that province&rsquo;s return with it, in '
     +'addition to the federal T2.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Where</th>'
   +'<th scope="col">Fixed place of business</th>'
   +'<th scope="col">What follows</th></tr></thead><tbody>';
  h+='<tr><td>Quebec</td><td>'+(qc==='y'?'Yes':'No')+'</td><td>'
   +(qc==='y'?'The CO-17 is a separate return, in addition to the T2'
             :'No CO-17 from this question')+'</td></tr>';
  h+='<tr><td>Alberta</td><td>'+(ab==='y'?'Yes':'No')+'</td><td>'
   +(ab==='y'?'The AT1 is a separate return, in addition to the T2'
             :'No AT1 from this question')+'</td></tr>';
  h+='<tr><td>The federal T2</td><td>Not a provincial question</td>'
   +'<td>Owed either way, within six months of the fiscal year-end</td>'
   +'</tr></tbody></table>';
  if(only==='y'){
    h+='<p>You answered that the registered office is the only address the '
     +'corporation has. For a dormant corporation that address is generally '
     +'its establishment, which is why a company that does nothing still has '
     +'one somewhere.</p>';
  }
  if(prov.length>0){
    h+='<p>'+NOTPRICEDJS+'</p>';
  }else{
    h+='<p>Nil T2 filing at '+PRICE_JS+' covers the federal corporate '
     +'return. No separate provincial return arises on these answers.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T96 = dict(
 slug='permanent-establishment-checker',
 title='Permanent Establishment Checker | Which Province Wants a Return',
 h1_pre='Permanent ', h1_span='Establishment Checker',
 h1='Permanent Establishment Checker',
 eyebrow='Provincial',
 keyword='permanent establishment corporation',
 seo_title='Permanent Establishment Checker',
 seo_desc=('A fixed place of business in Quebec or Alberta brings that '
           'province&#8217;s own return with it. Three answers name which '
           'ones apply.'),
 meta=('A permanent establishment is a fixed place through which a '
       'corporation carries on business. Quebec and Alberta collect their '
       'own corporate income tax.'),
 tags=['Three answers', 'Quebec and Alberta', 'CO-17 and AT1 separate',
       'Federal T2 either way'],
 form=tool('Where the corporation has a fixed place of business',
           [yn('qc', 'A fixed place of business in Quebec?'),
            yn('ab', 'A fixed place of business in Alberta?'),
            yn('only', 'Is the registered office the only address it has?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('what-it-is', 'What a Permanent Establishment Is',
   '<p>A fixed place through which the corporation carries on business. For a '
   'dormant corporation that is generally its registered office, which is why '
   'a company that does nothing all year still has an establishment '
   'somewhere.</p>\n'
   '<p>It matters because two provinces collect their own corporate income '
   'tax. An establishment in either one brings that province&rsquo;s return '
   'with it, in addition to the federal T2, and the '
   + a(PROV_GUIDE, 'guide to the Quebec CO-17 and the Alberta AT1')
   + ' sets out both.</p>'),
  ('which-provinces', 'Which Provinces Collect Their Own',
   _tbl(['Where the establishment is', 'The provincial return',
         'Is it separate from the T2'],
        [['Quebec', 'CO-17', 'Yes, a separate return'],
         ['Alberta', 'AT1', 'Yes, a separate return'],
         ['Ontario', 'Collected with the federal return',
          'No separate provincial income tax return'],
         ['Anywhere else', 'Not named on this site',
          'This site states no other provincial return']])
   + '\n<p>The last row is deliberate. This site publishes the Quebec and '
   'Alberta position because those two administer their own corporate income '
   'tax, and it does not state a position for provinces it has not '
   'published.</p>'),
  ('what-it-means-for-the-fee', 'What That Means for the Fee',
   '<p>' + NOT_PRICED + '</p>\n'
   '<p>So this page is a boundary rather than a quotation. Where the answers '
   'bring a CO-17 or an AT1 into play, the work is outside '
   + a(COST, 'nil T2 filing at ' + PRICE)
   + '. Where they do not, the federal return is the whole of it. The '
   + a(T + 'provincial-return-requirement-checker/',
       'provincial return requirement checker')
   + ' asks the same question from the other end.</p>\n'
   '<p>' + CLOSE['permanent-establishment-checker'] + '</p>'),
 ],
 faq=[
  ('What counts as a permanent establishment?',
   'A fixed place through which the corporation carries on business. For a '
   'dormant corporation that is generally its registered office.'),
  ('My corporation is dormant. Does it have one?',
   'Generally yes, at its registered office. Being dormant does not remove '
   'the address, and the address is what the test turns on.'),
  ('Why only Quebec and Alberta?',
   'Because those two administer their own corporate income tax, so each has '
   'its own return. Ontario corporate tax is collected with the federal '
   'return instead.'),
  ('Is the CO-17 part of the T2?',
   'No. Quebec administers its own corporate income tax, so the CO-17 is a '
   'separate return filed in addition to the federal one.'),
  ('Is the AT1 part of the T2?',
   'No. The same applies in Alberta: the AT1 is a separate provincial '
   'return.'),
  ('Do you file the CO-17 or the AT1?',
   'No. A corporation with a Quebec or Alberta permanent establishment needs '
   'work this service does not price, and pretending otherwise would be '
   'worse than saying so.'),
  ('I am registered in Quebec but have no office there.',
   'Registration and a fixed place of business are different questions. '
   'What this page asks about is the fixed place.'),
  ('Does an establishment make the year not nil?',
   'Not by itself. Where the corporation has its fixed place of business and '
   'whether it did anything in the year are two separate questions.'),
  ('What if I have establishments in two provinces?',
   'Then each province that collects its own corporate income tax wants its '
   'own return. The table above names them one at a time.'),
  ('What is the federal position either way?',
   'The T2 is owed within six months of the fiscal year-end wherever the '
   'establishment is.'),
 ],
 related=[
  (T + 'provincial-return-requirement-checker/',
   'Provincial return requirement checker'),
  (T + 'carrying-on-business-in-canada-checker/',
   'Carrying on business in Canada checker'),
  (T + 'non-resident-t2-penalty-calculator/',
   'Non-resident T2 penalty calculator'),
  (T + 'nil-return-eligibility-checker/', 'Nil return eligibility checker'),
  (PROV_GUIDE, 'The guide to the Quebec CO-17 and the Alberta AT1'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ------------------------------------------ 97. carrying on business
T97_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var hold=[['bank','Held a bank account'],
            ['asset','Owned assets'],
            ['reg','Stayed registered']];
  var i,v,wait=0,held=[],trade=pick('trade'),h;
  for(i=0;i<hold.length;i++){
    v=pick(hold[i][0]);
    if(v===null){wait++;continue;}
    if(v==='y'){held.push(hold[i][1]);}
  }
  if(trade===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the four questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  if(trade==='y'){
    h='<h3>That is carrying on business</h3>';
    h+='<p>Selling, invoicing or employing someone is the corporation doing '
     +'something rather than merely having something. The year is not a nil '
     +'year.</p>';
  }else if(held.length===0){
    h='<h3>Nothing held and nothing done</h3>';
    h+='<p>On these answers the corporation neither traded nor held anything '
     +'in the year. The year is nil, and with nothing at all to report the '
     +'GIFI schedules may be the narrow exemption rather than the rule.</p>';
  }else{
    h='<h3>Holding, not carrying on business</h3>';
    h+='<p>A corporation can hold a bank account, own assets and stay '
     +'registered for years without carrying on business, and every one of '
     +'those years is nil.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">In the year</th>'
   +'<th scope="col">Your answer</th>'
   +'<th scope="col">Is it carrying on business</th></tr></thead><tbody>';
  for(i=0;i<hold.length;i++){
    v=pick(hold[i][0]);
    h+='<tr><td>'+hold[i][1]+'</td><td>'+(v==='y'?'Yes':'No')
     +'</td><td>No. Having is not doing</td></tr>';
  }
  h+='<tr><td>Sold, invoiced or employed anyone</td><td>'
   +(trade==='y'?'Yes':'No')+'</td><td>'
   +(trade==='y'?'Yes. This is the one that decides it'
                :'Nothing on this line')+'</td></tr>';
  h+='</tbody></table>';
  if(trade==='y'){
    h+='<p>'+NOTNILJS+'</p>';
  }else{
    h+='<p>So the year is nil and nil T2 filing at '+PRICE_JS+' covers it. '
     +'What the corporation holds still decides which GIFI schedules the '
     +'return carries: share capital, cash, a shareholder loan, an '
     +'incorporation cost or a bank charge each make them required.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T97 = dict(
 slug='carrying-on-business-in-canada-checker',
 title='Carrying On Business Checker | Holding Is Not Doing',
 h1_pre='Carrying On ', h1_span='Business in Canada Checker',
 h1='Carrying on Business in Canada Checker',
 eyebrow='Is the Year Nil',
 keyword='carrying on business in canada',
 seo_desc=('A corporation can hold a bank account, own assets and stay '
           'registered without carrying on business. Four answers separate '
           'holding from doing.'),
 seo_title='Carrying On Business in Canada Checker',
 meta=('Holding a bank account, owning assets and staying registered are not '
       'carrying on business, and every one of those years is nil.'),
 tags=['Four answers', 'Holding is not doing', 'One answer decides it',
       'A nil year either way'],
 form=tool('What the corporation did, and what it merely had',
           [yn('bank', 'Did it hold a bank account at any time?'),
            yn('asset', 'Did it own any assets?'),
            yn('reg', 'Did it stay registered?'),
            yn('trade', 'Did it sell anything, invoice anyone or employ '
                        'anyone?')],
           'Answer all four questions above.'),
 js=None,
 sections=[
  ('having-and-doing', 'Having Something and Doing Something',
   '<p>A corporation can hold a bank account, own assets and stay registered '
   'for years without carrying on business, and every one of those years is '
   'nil. That sentence does most of the work on this page.</p>\n'
   '<p>The confusion is understandable. A corporation that still owns a '
   'building, still has a bank balance and is still on the register looks '
   'active from outside. None of those is the corporation carrying on '
   'business, and the '
   + a(ZERO_GUIDE, 'guide to zero-activity corporate tax returns')
   + ' works through the same distinction at length.</p>'),
  ('what-decides-it', 'What Decides It, and What Does Not',
   _tbl(['In the year', 'Carrying on business', 'Effect on the nil question'],
        [['A bank account held', 'No', 'The year can still be nil'],
         ['Assets owned', 'No', 'The year can still be nil'],
         ['Registration kept up', 'No', 'The year can still be nil'],
         ['Something sold or invoiced', 'Yes', 'The year is not nil'],
         ['Someone employed', 'Yes', 'The year is not nil']])
   + '\n<p>One caution on the first row. A bank account that pays interest '
   'is a different matter: interest credited on a balance is investment '
   'income, and the corporation is not nil for that tax year. Holding the '
   'account is not activity; being paid on it is income.</p>'),
  ('what-it-does-not-answer', 'What This Page Does Not Answer',
   '<p>It does not tell you whether a return is owed. One is, for every tax '
   'year, whether or not the corporation carried on business, and it is due '
   'within six months of the fiscal year-end.</p>\n'
   '<p>Nor does it decide the schedules. What the corporation holds does '
   'that, which is the point of the '
   + a(T + 'required-schedules-checker/', 'required schedules checker')
   + ', and ' + a(COST, 'nil T2 filing at ' + PRICE)
   + ' covers the return either way.</p>\n'
   '<p>' + CLOSE['carrying-on-business-in-canada-checker'] + '</p>'),
 ],
 faq=[
  ('Is holding a bank account carrying on business?',
   'No. A corporation can hold a bank account, own assets and stay '
   'registered for years without carrying on business, and every one of '
   'those years is nil.'),
  ('My corporation owns a building and nothing else happened.',
   'Owning an asset is not carrying on business. If rent came in, that is '
   'different: a rental corporation is not nil.'),
  ('The bank paid a few dollars of interest.',
   'Then the year is not nil. Interest credited on a balance is investment '
   'income, whatever the amount, even though holding the account is not '
   'activity.'),
  ('I invoiced one client and nothing else.',
   'That is carrying on business, and the year is not nil.'),
  ('Does a return still have to be filed?',
   'Yes, for every tax year, within six months of the fiscal year-end. This '
   'page answers whether the year was nil, not whether a return is owed.'),
  ('What about a corporation that has never traded at all?',
   'Then nothing was held and nothing done, and the GIFI exemption may '
   'actually apply, which it rarely does once there is share capital or a '
   'bank balance.'),
  ('Is paying a bank charge activity?',
   'It is an expense rather than carrying on business, so the year can still '
   'be nil, but it is something to report and that makes the GIFI schedules '
   'required.'),
  ('Does keeping the registration up count?',
   'No. Staying on the register is not carrying on business, though the '
   'registry still wants its annual return.'),
  ('Does this decide which schedules I file?',
   'No. What the corporation holds decides those, not what it did.'),
  ('Is a dormant year covered by the fee?',
   'Yes. Nil T2 filing at $300.00 plus HST per tax year covers a year like '
   'that.'),
 ],
 related=[
  (T + 'dormant-corporation-test/', 'Dormant corporation test'),
  (T + 'never-traded-corporation-checker/',
   'Never traded corporation checker'),
  (T + 'required-schedules-checker/', 'Required schedules checker'),
  (T + 'permanent-establishment-checker/',
   'Permanent establishment checker'),
  (ZERO_GUIDE, 'The guide to zero-activity corporate tax returns'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# -------------------------------------- 98. non-resident filing requirement
T98_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var own=pick('own'),inc=pick('inc'),act=pick('act'),wait=0,h;
  if(own===null){wait++;}
  if(inc===null){wait++;}
  if(act===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  if(inc==='y'){
    h='<h3>A return is owed, whoever owns it</h3>';
    h+='<p>A corporation incorporated in Canada files a T2 for every tax '
     +'year, within six months of its fiscal year-end. Where the '
     +'shareholders live does not change that.</p>';
  }else{
    h='<h3>That turns on a different question</h3>';
    h+='<p>A corporation incorporated outside Canada is not what this page '
     +'settles. Whether Canada wants a return from it turns on whether it '
     +'carries on business in Canada, which is its own test.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">Question</th>'
   +'<th scope="col">Your answer</th><th scope="col">What follows</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Owned by non-residents</td><td>'+(own==='y'?'Yes':'No')
   +'</td><td>'+(own==='y'
     ?'Changes what a late return costs, not whether one is owed'
     :'The ordinary late-filing position applies')+'</td></tr>';
  h+='<tr><td>Incorporated in Canada</td><td>'+(inc==='y'?'Yes':'No')
   +'</td><td>'+(inc==='y'
     ?'A T2 is owed for every tax year'
     :'Turns on carrying on business in Canada, not on this page')
   +'</td></tr>';
  h+='<tr><td>Any activity in the year</td><td>'+(act==='y'?'Yes':'No')
   +'</td><td>'+(act==='y'?'The year is not a nil year'
                          :'The year can be nil, and is still filed')
   +'</td></tr>';
  h+='</tbody></table>';
  if(own==='y'){
    h+='<p>Because the corporation is non-resident-owned, a late return is '
     +'charged differently: $25.00 per day applies regardless, to a maximum '
     +'of $2,500.00. That is the figure a nil year cannot argue its way out '
     +'of, because it does not depend on tax owing.</p>';
  }
  if(act==='y'){
    h+='<p>'+NOTNILJS+'</p>';
  }else if(inc==='y'){
    h+='<p>A nil year is still filed, and nil T2 filing at '+PRICE_JS+' '
     +'covers it.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T98 = dict(
 slug='non-resident-corporation-filing-checker',
 title='Non-Resident Corporation Filing Checker | What Is Owed',
 h1_pre='Non-Resident ', h1_span='Corporation Filing Checker',
 h1='Non-Resident Corporation Filing Checker',
 eyebrow='Non-Resident',
 keyword='non resident corporation t2 filing',
 seo_title='Non-Resident Corporation Filing Checker',
 seo_desc=('Where the shareholders live does not decide whether a T2 is '
           'owed. Three answers show what is owed and what a late return '
           'costs.'),
 meta=('A corporation incorporated in Canada files a T2 whoever owns it. '
       'Non-resident ownership changes what a late return costs.'),
 tags=['Three answers', 'Ownership is not residence',
       '$25.00 per day if late', 'A nil year is still filed'],
 form=tool('The corporation and the year',
           [yn('own', 'Is the corporation owned by non-residents?'),
            yn('inc', 'Was it incorporated in Canada?'),
            yn('act', 'Was there any activity in the year?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('two-questions', 'Ownership and Incorporation Are Two Questions',
   '<p>A corporation incorporated in Canada files a T2 for every tax year, '
   'within six months of its fiscal year-end, whoever its shareholders are '
   'and wherever they live. Non-resident ownership does not remove the '
   'return.</p>\n'
   '<p>What it does change is the cost of being late, and that is the part '
   'worth knowing in advance. The '
   + a(NR_GUIDE, 'guide to non-resident-owned corporation nil filing')
   + ' sets out the position in full.</p>'),
  ('what-late-costs', 'What a Late Return Costs Here',
   _tbl(['The corporation', 'A late nil return', 'Why'],
        [['Resident-owned, nil year',
          'No percentage late-filing penalty on a nil year',
          'That penalty is a percentage of tax owing, and the corporation '
          'owes $0.00'],
         ['Non-resident-owned, nil year',
          '$25.00 per day, to a maximum of $2,500.00',
          'It applies regardless, because it does not depend on tax owing'],
         ['Either, unfiled and left',
          'The year stays open',
          'It invites a demand to file and an arbitrary assessment, and '
          'blocks a clearance certificate']])
   + '\n<p>The second row is the one that catches people out. Every other '
   'argument for leaving a nil year unfiled rests on there being no tax '
   'owing, and this charge does not.</p>'),
  ('incorporated-outside-canada', 'A Corporation Incorporated Outside Canada',
   '<p>That is a different question and this page does not settle it. '
   'Whether Canada wants a return from a corporation incorporated elsewhere '
   'turns on whether it carries on business in Canada, which the '
   + a(T + 'carrying-on-business-in-canada-checker/',
       'carrying on business in Canada checker')
   + ' and the '
   + a(T + 'permanent-establishment-checker/',
       'permanent establishment checker')
   + ' each take from a different side.</p>\n'
   '<p>What this page answers is the common case: a Canadian corporation '
   'whose owners are not in Canada. '
   + a(COST, 'Nil T2 filing at ' + PRICE) + ' covers those years.</p>\n'
   '<p>' + CLOSE['non-resident-corporation-filing-checker'] + '</p>'),
 ],
 faq=[
  ('My shareholders live abroad. Do I still file a T2?',
   'Yes. A corporation incorporated in Canada files a T2 for every tax year, '
   'whoever owns it and wherever they live.'),
  ('Does a nil year still have to be filed?',
   'Yes, and for a non-resident-owned corporation that matters more than '
   'usual, because a late one is charged $25.00 per day up to $2,500.00.'),
  ('Why is the penalty different?',
   'Because it does not depend on tax owing. The percentage late-filing '
   'penalty is a percentage of tax owing and a nil return owes $0.00; this '
   'charge applies regardless.'),
  ('Is the maximum really $2,500.00?',
   'That is the maximum published for this charge, reached at 100 days.'),
  ('My corporation was incorporated outside Canada.',
   'Then this page does not settle it. That turns on whether the '
   'corporation carries on business in Canada, which is a separate test.'),
  ('Does non-resident ownership make the year not nil?',
   'No. Who owns the corporation and what it did in the year are separate '
   'questions.'),
  ('Does the six-month deadline change?',
   'No. The return is due within six months of the fiscal year-end either '
   'way.'),
  ('Do you file for non-resident-owned corporations?',
   'A nil year is covered at $300.00 plus HST per tax year, the same as any '
   'other nil year.'),
  ('What if several years are unfiled?',
   'Each year is its own return and the daily charge runs on each late one. '
   'They are filed oldest first.'),
  ('Where is the whole position set out?',
   'In the <a href="' + NR_GUIDE + '">guide to non-resident-owned '
   'corporation nil filing</a>.'),
 ],
 related=[
  (T + 'non-resident-t2-penalty-calculator/',
   'Non-resident T2 penalty calculator'),
  (T + 'carrying-on-business-in-canada-checker/',
   'Carrying on business in Canada checker'),
  (T + 'permanent-establishment-checker/', 'Permanent establishment checker'),
  (T + 'nil-return-late-penalty-checker/', 'Nil return late penalty checker'),
  (NR_GUIDE, 'The guide to non-resident-owned corporation nil filing'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# ------------------------------------------- 99. outstanding returns count
T99_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var ye=parse('last'),same=pick('same');
  if(ye===null){
    out.innerHTML='<p>Enter the year-end of the last return you filed.</p>';
    return;
  }
  if(ye===undefined){
    out.innerHTML='<p class="ei-err">Enter a valid date.</p>';return;
  }
  var now=today();
  if(ye.getTime()>now.getTime()){
    out.innerHTML='<p class="ei-err">That year-end is in the future. Enter '
     +'the year-end of a return already filed.</p>';return;
  }
  var rows=[],d=ye,i,due,out_n=0,soon=0;
  for(i=1;i<=40;i++){
    d=addYear(ye,i);
    if(d.getTime()>now.getTime()){break;}
    due=filingDate(d);
    if(due.getTime()<=now.getTime()){out_n++;rows.push([d,due,'Outstanding']);}
    else{soon++;rows.push([d,due,'Not yet due']);}
  }
  var h='';
  if(rows.length===0){
    h+='<h3>Nothing has fallen due since</h3>';
    h+='<p>No tax year-end has passed since '+fmt(ye)+', so no further '
     +'return has arisen yet.</p>';
  }else if(out_n===0){
    h+='<h3>Nothing outstanding yet</h3>';
    h+='<p>'+plural(rows.length,'tax year')+' has ended since '+fmt(ye)
     +', and the filing date has not passed on '
     +(rows.length===1?'it':'any of them')+' yet.</p>';
  }else{
    h+='<h3>'+plural(out_n,'return')+' outstanding</h3>';
    h+='<p>Counting from '+fmt(ye)+', '+plural(out_n,'tax year')+' has '
     +'passed its filing date and has not been filed on these answers. '
     +'Each one is a return at '+PRICE_JS+'.</p>';
  }
  if(rows.length>0){
    h+='<table class="ei-tbl"><thead><tr><th scope="col">Tax year-end</th>'
     +'<th scope="col">Filing date</th><th scope="col">Status</th>'
     +'</tr></thead><tbody>';
    for(i=0;i<rows.length;i++){
      h+='<tr><td>'+fmt(rows[i][0])+'</td><td>'+fmt(rows[i][1])+'</td><td>'
       +rows[i][2]+'</td></tr>';
    }
    h+='</tbody></table>';
  }
  if(same==='n'){
    h+='<p>You answered that the year-end has not stayed the same. Then this '
     +'count is indicative only: a changed year-end produces a short tax '
     +'year, and the sequence of year-ends is not a simple run of '
     +'anniversaries.</p>';
  }
  if(out_n>0){
    h+='<p>They are filed oldest first, and can be transmitted together. An '
     +'unfiled year does not expire: it stays open, invites a demand to file '
     +'and an arbitrary assessment, and blocks a clearance certificate until '
     +'it is filed.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T99 = dict(
 slug='outstanding-returns-count-checker',
 title='Outstanding Returns Count | How Many T2 Years Are Open',
 h1_pre='Outstanding ', h1_span='Returns Count Checker',
 h1='Outstanding Returns Count Checker',
 eyebrow='Unfiled Years',
 keyword='how many t2 returns outstanding',
 seo_title='Outstanding Returns Count Checker',
 seo_desc=('One T2 falls due for each tax year. Enter the year-end of the '
           'last one filed to count how many have passed their filing date '
           'since.'),
 meta=('One T2 falls due for each tax year, six months after the year-end. '
       'This counts the years that have passed their filing date.'),
 tags=['One date in', 'Counts the tax side', 'Dates each filing day',
       'Oldest first'],
 form=tool('The last return you filed',
           [date('last', 'The tax year-end of the last T2 you filed'),
            yn('same', 'Has the year-end stayed the same since?')],
           'Enter the year-end of the last return you filed.'),
 js=None,
 sections=[
  ('one-per-year', 'One Return for Each Tax Year',
   '<p>A corporation files a T2 for every tax year it has existed, due '
   'within six months of the fiscal year-end. So the count is mechanical: '
   'one return for each year-end that has passed, and the filing date six '
   'months after each.</p>\n'
   '<p>The calculator above walks the year-ends forward from the last return '
   'you filed and dates each filing day, so a year that has ended but not '
   'yet reached its filing date is shown as not yet due rather than as '
   'outstanding.</p>'),
  ('what-the-count-is-not', 'What the Count Is Not',
   _tbl(['Trail', 'What falls due each year', 'What counts it'],
        [['The corporate tax return',
          'One T2, six months after the fiscal year-end', 'This page'],
         ['The Ontario annual return',
          'One registry filing for each tax year',
          'The Ontario missed annual returns calculator'],
         ['The federal annual return',
          'One filing, 60 days after the anniversary',
          'The federal annual return anniversary calculator']])
   + '\n<p>The three are separate trails to three different bodies, and '
   'being current on one says nothing about the others. This page counts the '
   'first row only.</p>'),
  ('what-happens-next', 'What Happens to the Years It Counts',
   '<p>An unfiled year does not expire. It stays open, invites a demand to '
   'file and an arbitrary assessment, and blocks a clearance certificate '
   'until it is filed. That is why the count matters more than it looks.</p>\n'
   '<p>They are filed oldest first and can be transmitted together, each at '
   + a(COST, PRICE) + '. The '
   + a(T + 'unfiled-years-cost-calculator/', 'unfiled years cost calculator')
   + ' totals them and the '
   + a(CATCHUP_GUIDE, 'guide to catching up on unfiled corporate tax returns')
   + ' sets out the order.</p>\n'
   '<p>' + CLOSE['outstanding-returns-count-checker'] + '</p>'),
 ],
 faq=[
  ('How many returns am I behind?',
   'One for each tax year-end that has passed its filing date since the last '
   'return you filed. The calculator above counts them and dates each one.'),
  ('What is the filing date?',
   'Six months after the fiscal year-end, moved to the next business day '
   'where it falls on a weekend or a holiday.'),
  ('A year has ended but the six months are not up.',
   'Then it is not outstanding yet, and the table says so rather than '
   'counting it.'),
  ('Do unfiled years expire?',
   'No. An unfiled year stays open, invites a demand to file and an '
   'arbitrary assessment, and blocks a clearance certificate until it is '
   'filed.'),
  ('I changed my year-end part way through.',
   'Then the count is indicative only. A changed year-end produces a short '
   'tax year, so the year-ends are not a plain run of anniversaries.'),
  ('Is this the same as the annual returns I owe?',
   'No. Those are registry filings on their own trails. This page counts the '
   'corporate tax returns only.'),
  ('Can they all be filed at once?',
   'They are prepared oldest first and can be transmitted together.'),
  ('What does each one cost?',
   'A nil year is $300.00 plus HST per tax year, one price for each return.'),
  ('What if some of those years were not nil?',
   'Then those years are not covered by that fee. A holding corporation '
   'with investment income, a rental corporation and a corporation that paid '
   'or received a dividend are not nil.'),
  ('I do not know when the last one was filed.',
   'The corporation&rsquo;s own records settle it. The count runs from '
   'whatever date you enter, so an uncertain date gives an uncertain count.'),
 ],
 related=[
  (T + 'unfiled-years-cost-calculator/', 'Unfiled years cost calculator'),
  (T + 'catch-up-filing-schedule-generator/',
   'Catch-up filing schedule generator'),
  (T + 'nil-t2-deadline-calculator/', 'Nil T2 deadline calculator'),
  (T + 'ontario-missed-annual-returns-calculator/',
   'Ontario missed annual returns calculator'),
  (CATCHUP_GUIDE, 'The guide to catching up on unfiled corporate tax returns'),
  (COST, 'Nil T2 filing cost'),
 ],
)

# -------------------------------- 100. Schedule 11, shareholder transactions
T100_JS = RBASE + r"""
var out=document.getElementById('out');
function show(){
  var adv=pick('adv'),pay=pick('pay'),bal=pick('bal'),wait=0,h;
  if(adv===null){wait++;}
  if(pay===null){wait++;}
  if(bal===null){wait++;}
  if(wait>0){
    out.innerHTML='<p>'+wait+' of the three questions '
     +(wait===1?'is':'are')+' still unanswered.</p>';return;
  }
  var moved=(adv==='y'||pay==='y');
  if(moved){
    h='<h3>Something moved in the year</h3>';
    h+='<p>A transaction with a shareholder, an officer or an employee is '
     +'what Schedule 11 reports, and on these answers the year has one.</p>';
  }else if(bal==='y'){
    h='<h3>A balance, but no transaction</h3>';
    h+='<p>The loan balance sat where it was all year. A balance is not a '
     +'transaction: it is reported where balances are reported, on the GIFI '
     +'schedules, and there is nothing here for Schedule 11 to take.</p>';
  }else{
    h='<h3>Nothing on either count</h3>';
    h+='<p>No transaction and no balance, so nothing arises for Schedule 11 '
     +'and nothing for the shareholder lines of the balance sheet.</p>';
  }
  h+='<table class="ei-tbl"><thead><tr><th scope="col">In the year</th>'
   +'<th scope="col">Your answer</th><th scope="col">Where it lands</th>'
   +'</tr></thead><tbody>';
  h+='<tr><td>Money advanced to or from a shareholder</td><td>'
   +(adv==='y'?'Yes':'No')+'</td><td>'
   +(adv==='y'?'A transaction in the year':'Nothing on this line')
   +'</td></tr>';
  h+='<tr><td>Anything paid to a shareholder, officer or employee other '
   +'than salary</td><td>'+(pay==='y'?'Yes':'No')+'</td><td>'
   +(pay==='y'?'A transaction in the year':'Nothing on this line')
   +'</td></tr>';
  h+='<tr><td>A standing balance from an earlier year</td><td>'
   +(bal==='y'?'Yes':'No')+'</td><td>'
   +(bal==='y'?'A balance, reported on the GIFI schedules rather than here'
              :'Nothing on this line')+'</td></tr>';
  h+='</tbody></table>';
  if(bal==='y'){
    h+='<p>Note what the balance does do: a shareholder loan is one of the '
     +'five things that make GIFI Schedules 100, 125 and 141 required, '
     +'whichever direction it runs.</p>';
  }
  if(!moved){
    h+='<p>So a dormant year with a loan that did not move has nothing for '
     +'this schedule, and nil T2 filing at '+PRICE_JS+' covers a year like '
     +'that.</p>';
  }
  h+='<p>'+DISC_JS+'</p>';
  out.innerHTML=h;
}
"""

T100 = dict(
 slug='schedule-11-shareholder-transactions-checker',
 title='Schedule 11 Shareholder Transactions | Movement or Balance',
 h1_pre='Schedule 11 ', h1_span='Shareholder Transactions Checker',
 h1='Schedule 11 Shareholder Transactions Checker',
 eyebrow='Schedules',
 keyword='schedule 11 transactions with shareholders',
 seo_title='Schedule 11 Shareholder Transactions Checker',
 seo_desc=('Schedule 11 reports transactions with shareholders, officers and '
           'employees. Three answers separate a transaction from a standing '
           'balance.'),
 meta=('Schedule 11 reports transactions with shareholders, officers and '
       'employees. A balance that did not move in the year is not a '
       'transaction.'),
 tags=['Three answers', 'Movement, not balance', 'A dormant year often has '
       'none', 'Balances go to GIFI'],
 form=tool('Shareholder dealings in the tax year',
           [yn('adv', 'Was money advanced to or from a shareholder?'),
            yn('pay', 'Was anything paid to a shareholder, officer or '
                      'employee other than salary?'),
            yn('bal', 'Is there a standing loan balance from an earlier '
                      'year?')],
           'Answer the three questions above.'),
 js=None,
 sections=[
  ('movement-not-balance', 'A Transaction Is Movement, Not a Balance',
   '<p>Schedule 11 reports transactions with shareholders, officers and '
   'employees. The word doing the work is transaction: something has to have '
   'moved during the year.</p>\n'
   '<p>That is why most dormant years have nothing for it. A shareholder '
   'loan sitting at the same figure it was a year ago is a balance, and a '
   'balance is reported where balances are reported. The '
   + a(T + 'shareholder-loan-balance-checker/',
       'shareholder loan balance checker')
   + ' deals with the balance itself.</p>'),
  ('where-each-one-goes', 'Where Each One Goes',
   _tbl(['What happened', 'Is it a transaction', 'Where it is reported'],
        [['Money advanced to a shareholder in the year', 'Yes',
          'Schedule 11'],
         ['A shareholder repaid part of a loan in the year', 'Yes',
          'Schedule 11'],
         ['A benefit or payment other than salary', 'Yes', 'Schedule 11'],
         ['A loan balance unchanged all year', 'No',
          'The GIFI schedules, as a balance'],
         ['Salary paid through payroll', 'Not for this purpose',
          'Payroll, with its own filings']])
   + '\n<p>The fourth row is the one that matters on a nil return, and it is '
   'also the row that still has a consequence: a shareholder loan is one of '
   'the five things that make GIFI Schedules 100, 125 and 141 required, '
   'whichever direction the balance runs.</p>'),
  ('what-a-nil-year-usually-has', 'What a Nil Year Usually Has Here',
   '<p>Nothing, and that is the useful answer. A corporation that did not '
   'trade generally did not advance anything to its shareholder or take '
   'anything back, so there is no transaction to report even where a loan '
   'has sat on the books for years.</p>\n'
   '<p>Which schedules a nil return does carry is a different list, and the '
   + a(SCHED_GUIDE, 'guide to T2 schedules on a nil return')
   + ' gives it: the GIFI schedules where there is anything to report, '
   'Schedule 50 for a shareholder at 10% or more, Schedule 24 on a first '
   'return, and Schedule 8 with loss continuity. '
   + a(COST, 'Nil T2 filing at ' + PRICE) + ' covers them.</p>\n'
   '<p>' + CLOSE['schedule-11-shareholder-transactions-checker'] + '</p>'),
 ],
 faq=[
  ('What does Schedule 11 report?',
   'Transactions with shareholders, officers and employees. Something has to '
   'have moved during the year for it to have anything to take.'),
  ('My shareholder loan has not changed in years. Does it go here?',
   'No. A balance that did not move is not a transaction. It is reported '
   'where balances are reported, on the GIFI schedules.'),
  ('I took money out of the corporation this year.',
   'That is a transaction with a shareholder, and it is what this schedule '
   'reports.'),
  ('I repaid part of my shareholder loan.',
   'That is also a transaction. Movement in either direction counts.'),
  ('Does a dormant corporation file Schedule 11?',
   'Usually there is nothing for it to report, because nothing moved. This '
   'page asks the question rather than assuming the answer.'),
  ('Is salary a transaction for this purpose?',
   'Salary runs through payroll and carries its own filings. What this page '
   'asks about is the other dealings.'),
  ('Does the loan balance matter at all then?',
   'Yes, elsewhere. A shareholder loan is one of the five things that make '
   'GIFI Schedules 100, 125 and 141 required, whichever direction it runs.'),
  ('Is this the same as Schedule 50?',
   'No. Schedule 50 lists shareholders at 10% or more. This one is about '
   'dealings with them during the year.'),
  ('Does a transaction make the year not nil?',
   'Not by itself, and this page does not say it does. Whether the year was '
   'nil turns on whether the corporation carried on business or had income.'),
  ('Which schedules does a nil return actually carry?',
   'The GIFI schedules where there is anything to report, Schedule 50 for a '
   'shareholder at 10% or more, Schedule 24 on a first return, and Schedule '
   '8 with loss continuity.'),
 ],
 related=[
  (T + 'shareholder-loan-balance-checker/', 'Shareholder loan balance checker'),
  (T + 'due-to-versus-due-from-shareholder-checker/',
   'Due to versus due from shareholder checker'),
  (T + 'schedule-50-shareholder-threshold-checker/',
   'Schedule 50 shareholder threshold checker'),
  (T + 'required-schedules-checker/', 'Required schedules checker'),
  (SCHED_GUIDE, 'The complete guide to T2 schedules on a nil return'),
  (COST, 'Nil T2 filing cost'),
 ],
)

TOOLS14 = [T96, T97, T98, T99, T100]

STRUCTURE = dict(sections=3, faq=10, related=6, tags=4,
                 body_tables=1, result_tables=1)


def wire(form):
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


for _t, _js in zip(TOOLS14, [T96_JS, T97_JS, T98_JS, T99_JS, T100_JS]):
    _js = _js + wire(_t['form'])
    _t['js'] = _js if _js.startswith(PRELUDE) else PRELUDE + _js

# ---- the contract -------------------------------------------------------
_LIVE = {f[:-5] for f in os.listdir(HERE) if f.endswith('.html')}
_THIS = {t['slug'] for t in TOOLS14}
_EARLIER = _LIVE - _THIS
assert len(_EARLIER) >= 95, (
    'expected at least the 95 tools of batches 1 to 13, found %d'
    % len(_EARLIER))
PUBLISHED = _THIS <= _LIVE

_PLAN = io.open(os.path.join(HERE, '..', '..', 'docs',
                             'corpnilfilingfor300-seo-website-plan.md'),
                encoding='utf-8').read()
for t in TOOLS14:
    assert '\n/%s/\n' % t['slug'] in _PLAN, (
        '%s is not an Appendix A URL' % t['slug'])

for t in TOOLS14:
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

    _vars = _re.findall(r'^var ([A-Za-z_]\w*)=', t['js'], _re.M)
    _dupe = sorted({v for v in _vars if _vars.count(v) > 1})
    assert not _dupe, (
        '%s: the module declares %s more than once, which means PRELUDE was '
        'prepended on top of a module that already carried it' % (s, _dupe))

    _body = ''.join(h for _i, _h2, h in t['sections'])
    assert CLOSE[s] in _body, '%s: its closing sentence is missing' % s

    # Hard rule 8: wherever CO-17 or AT1 is named, it is named as separate.
    for _form in ('CO-17', 'AT1'):
        if _form in _body:
            assert 'separate' in _body, (
                '%s: names %s without calling it a separate return' % (s, _form))

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

    _all = (t['form'] + _body
            + ''.join(q + aa for q, aa in t['faq'])
            + ''.join(u2 for u2, _x in t['related']) + t['js'])
    for u in _re.findall(r'href="' + SITE + r'/tools/([a-z0-9-]+)/"', _all):
        assert u in _LIVE or u in _THIS, '%s: links to missing tool %s' % (s, u)
    _F9 = {f[:-5] for f in os.listdir(os.path.join(HERE, '..', 'f9'))
           if f.endswith('.html')}
    for u in _re.findall(r'href="' + SITE + r'/guides/([a-z0-9-]+)/"', _all):
        assert u in _F9, '%s: links to missing guide %s' % (s, u)

assert len({t['seo_title'] for t in TOOLS14}) == len(TOOLS14), 'title clash'
assert len({t['seo_desc'] for t in TOOLS14}) == len(TOOLS14), 'desc clash'
assert len({t['keyword'] for t in TOOLS14}) == len(TOOLS14), 'keyword clash'
assert len({t['h1'] for t in TOOLS14}) == len(TOOLS14), 'h1 clash'

if __name__ == '__main__':
    import build_f2
    build_f2.TODAY, build_f2.ISO = 'November 9, 2026', '2026-11-09'
    recs = []
    for t in TOOLS14:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], url=url,
                         content=html,
                         rank_math_title=t['seo_title'],
                         rank_math_description=t['seo_desc'],
                         rank_math_focus_keyword=t['keyword'],
                         **meta(t)))
    json.dump(recs, io.open(os.path.join(HERE, 'f2n-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in recs:
        print('%-48s %6d bytes' % (r['slug'], len(r['content'].encode())))
