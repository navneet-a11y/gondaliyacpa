"""Family 2, the first three tools from the 6(e) link-earning table.

6(c) makes the unique element "Calculator logic block and result strings unique
to that tool", sourced from a JavaScript module library, and gates publication
on "a working calculation and a result screen that changes with input". So the
deliverable here is working JavaScript, not prose. Each page carries its own
self-contained module with no external dependency.

6(e) gives the full brief for all three: the input, the output, and in the Notes
column the actual rule. Nothing below is invented -- the eight T2 Short
conditions and the five GIFI triggers are the plan's own lists, and the T2 due
date follows the Income Tax Act rule that the Canada Revenue Agency publishes:
a year-end on the last day of a month is due the last day of the sixth month
after, and any other year-end is due the same day of the sixth month after.

URL base. 6(a) and 6(e) both say /tools/<tool>/, and the CPT's registered
rewrite base is `tools`, so that is what is built. Appendix A lists Family 2 at
root instead, which would put 150 pages inside the Family 4 catch-all; that is
the same conflict resolved the same way seven times already, and the root form
is what 404'd a blog post on 2026-10-22.

Ontario statutory holidays are the nine public holidays under the Employment
Standards Act. The Civic Holiday in August and Remembrance Day are not among
them and are not applied. Good Friday is computed from Easter rather than
tabulated, so the tool stays correct in every future year without a data file.
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
HUB  = SITE + '/tools/'
TODAY, ISO = 'October 23, 2026', '2026-10-23'
PRICE = '$300.00 plus HST per tax year'

BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')
EFILE = ('Gondaliya CPA Professional Corporation is a registered EFILE electronic '
         'filer. Returns are prepared and transmitted in Canada. Credentials are '
         'never shared and never used offshore.')
# 6(c) requires this sentence on the result screen of every tool page.
TOOL_DISCLAIMER = ('This tool gives general information and is not a filed return.')
NOT_NIL = ('A holding corporation with investment income, a rental corporation and a '
           'corporation that paid or received a dividend are not nil. Those are '
           'handled by Gondaliya CPA Professional Corporation at gondaliyacpa.ca at '
           '$350.00 plus HST per year.')

_pillar = io.open(os.path.join(HERE, '..', 'f9', 'nil-t2-return-complete-guide.html'),
                  encoding='utf-8').read()
BASE_CSS = _pillar[:_pillar.index('</style>')]

TOOL_CSS = """
/* Narrower than the guides' 1100px, at Navneet's request. 1000px is the
   measure the Family 4 service pages already use, so this is a house value
   rather than a new one. The hero band stays full-bleed: it is .ei-hero that
   spans, and .ei-hero-inner caps its text at 860px, so neither is touched.

   A service page has exactly one band that spans the viewport, the hero. The
   guides alternate white and grey .ei-section bands, which span whatever the
   window is and make the body read full width even with the text capped at
   1000px. Dropping the grey leaves one continuous column, which is what a
   service page looks like. The hero still spans. */
.ei-wrap{max-width:1000px}
.ei-section-alt{background:none}
.ei-tool{background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:22px 24px;margin:18px 0;box-shadow:0 1px 2px rgba(26,35,64,.05)}
.ei-tool legend{font-weight:800;color:#1a2340;font-size:1.05em;padding:0 0 6px}
.ei-tool fieldset{border:0;margin:0;padding:0}
.ei-f{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:0 0 14px}
.ei-f label{font-weight:600;color:#1a2340;flex:1 1 320px;line-height:1.5}
.ei-f input[type=date]{font:inherit;padding:9px 11px;border:1px solid #cbd5e0;border-radius:7px;color:#1a2340;background:#fff}
.ei-yn{display:inline-flex;border:1px solid #cbd5e0;border-radius:7px;overflow:hidden;flex:0 0 auto}
.ei-yn label{flex:0 0 auto;margin:0;padding:8px 16px;cursor:pointer;font-weight:700;color:#4a5568;background:#fff;line-height:1.2}
.ei-yn input{position:absolute;opacity:0;width:0;height:0}
.ei-yn input:checked+span{background:rgba(32,135,201,1);color:#fff}
.ei-yn span{display:block;padding:8px 16px;margin:-8px -16px}
.ei-yn label:focus-within span{outline:2px solid #1a2340;outline-offset:-2px}
.ei-out{margin:16px 0 0;padding:16px 18px;border-radius:9px;border-left:5px solid #cbd5e0;background:#f7f9fc}
.ei-out.ok{border-left-color:#2f855a;background:#f0fff4}
.ei-out.no{border-left-color:#c53030;background:#fff5f5}
.ei-out h3{margin:0 0 6px;font-size:1.1em;color:#1a2340}
.ei-out p{margin:0 0 8px;color:#4a5568;line-height:1.7}
.ei-out ul{margin:6px 0 8px 20px;color:#4a5568;line-height:1.7}
.ei-out .ei-note{font-size:.88em;color:#718096;margin:10px 0 0}
.ei-big{font-size:1.5em;font-weight:800;color:rgba(32,135,201,1);display:block;margin:2px 0 6px}
.ei-tool .ei-err{color:#c53030;font-weight:600;margin:6px 0 0}
</style>
"""
CSS = BASE_CSS + TOOL_CSS

def a(h, t):
    return '<a href="%s">%s</a>' % (h, t)

# ---------------------------------------------------------------------------
# Shared date module. Ontario's nine Employment Standards Act public holidays.
# Good Friday is derived from Easter so no year needs a lookup table.
# ---------------------------------------------------------------------------
DATE_JS = r"""
var MON=['January','February','March','April','May','June','July','August',
         'September','October','November','December'];
var DAY=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
function u(y,m,d){return new Date(Date.UTC(y,m,d));}
function lastDay(y,m){return new Date(Date.UTC(y,m+1,0)).getUTCDate();}
function fmt(dt){return MON[dt.getUTCMonth()]+' '+dt.getUTCDate()+', '+dt.getUTCFullYear();}
function nthMon(y,m,n){var d=u(y,m,1);return u(y,m,1+((1-d.getUTCDay()+7)%7)+7*(n-1));}
function monOnOrBefore(y,m,day){var d=u(y,m,day);return u(y,m,day-((d.getUTCDay()+6)%7));}
function easter(y){
  var a=y%19,b=Math.floor(y/100),c=y%100,d=Math.floor(b/4),e=b%4,
      f=Math.floor((b+8)/25),g=Math.floor((b-f+1)/3),h=(19*a+b-d-g+15)%30,
      i=Math.floor(c/4),k=c%4,l=(32+2*e+2*i-h-k)%7,
      m=Math.floor((a+11*h+22*l)/451),
      mo=Math.floor((h+l-7*m+114)/31),da=((h+l-7*m+114)%31)+1;
  return u(y,mo-1,da);
}
function holidays(y){
  var e=easter(y),gf=new Date(e.getTime()-2*86400000);
  return [u(y,0,1),nthMon(y,1,3),gf,monOnOrBefore(y,4,24),u(y,6,1),
          nthMon(y,8,1),nthMon(y,9,2),u(y,11,25),u(y,11,26)];
}
var HCACHE={};
function isHoliday(dt){
  var y=dt.getUTCFullYear();
  if(!HCACHE[y]){HCACHE[y]={};holidays(y).forEach(function(h){HCACHE[y][h.getTime()]=1;});}
  return !!HCACHE[y][dt.getTime()];
}
function isBusiness(dt){
  var w=dt.getUTCDay();
  return w!==0&&w!==6&&!isHoliday(dt);
}
function nextBusiness(dt){
  var d=new Date(dt.getTime());
  while(!isBusiness(d)){d=new Date(d.getTime()+86400000);}
  return d;
}
function businessBetween(from,to){
  var n=0,d=new Date(from.getTime()+86400000);
  while(d.getTime()<=to.getTime()){if(isBusiness(d)){n++;}d=new Date(d.getTime()+86400000);}
  return n;
}
function today(){var n=new Date();return u(n.getFullYear(),n.getMonth(),n.getDate());}
"""

# ---------------------------------------------------------------------------
# Tool 1. /tools/nil-t2-deadline-calculator/
# 6(e): input a fiscal year-end date, return the due date, business days
# remaining, Ontario statutory holidays applied. Notes: highest link potential
# of the 150 tools.
# ---------------------------------------------------------------------------
T1_FORM = """<div class="ei-tool">
<fieldset><legend>Your fiscal year-end</legend>
<div class="ei-f"><label for="ye">The last day of your corporation&rsquo;s tax year</label>
<input type="date" id="ye" name="ye"></div>
</fieldset>
<div class="ei-out" id="out" role="status" aria-live="polite">
<p>Enter a fiscal year-end above and the due date appears here.</p></div>
</div>"""

T1_JS = DATE_JS + r"""
function dueDate(ye){
  var y=ye.getUTCFullYear(),m=ye.getUTCMonth(),d=ye.getUTCDate();
  var endOfMonth=(d===lastDay(y,m));
  var tm=m+6,ty=y+Math.floor(tm/12);tm=((tm%12)+12)%12;
  if(endOfMonth){return u(ty,tm+1,0);}
  return u(ty,tm,Math.min(d,lastDay(ty,tm)));
}
function render(){
  var v=document.getElementById('ye').value,out=document.getElementById('out');
  if(!v){out.className='ei-out';
    out.innerHTML='<p>Enter a fiscal year-end above and the due date appears here.</p>';
    return;}
  var p=v.split('-'),ye=u(+p[0],+p[1]-1,+p[2]);
  if(isNaN(ye.getTime())){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';return;}
  var due=dueDate(ye),eff=nextBusiness(due),t=today();
  var h='<h3>Your nil T2 for the year ended '+fmt(ye)+'</h3>';
  h+='<span class="ei-big">Due '+fmt(due)+'</span>';
  if(eff.getTime()!==due.getTime()){
    h+='<p>'+fmt(due)+' is a '+DAY[due.getUTCDay()]+
       (isHoliday(due)?' and an Ontario statutory holiday':'')+
       ', so the next business day is '+fmt(eff)+'.</p>';
  }
  var n=businessBetween(t,eff);
  if(eff.getTime()<t.getTime()){
    h+='<p><strong>This deadline has passed.</strong> An unfiled year stays open '+
       'indefinitely, and each unfiled year is its own return at '+PRICE_JS+'.</p>';
  }else{
    h+='<p><strong>'+n+' business day'+(n===1?'':'s')+' remaining</strong>, counting '+
       'from today and excluding weekends and Ontario statutory holidays.</p>';
  }
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out '+(eff.getTime()<t.getTime()?'no':'ok');
  out.innerHTML=h;
}
document.getElementById('ye').addEventListener('input',render);
document.getElementById('ye').addEventListener('change',render);
render();
"""

def yn(i, label, yes='Yes', no='No'):
    """One yes-or-no row. Neither option is preselected, so the result screen
    cannot show a verdict the visitor did not actually answer for."""
    return ('<div class="ei-f"><label id="l%s">%s</label>'
            '<span class="ei-yn" role="radiogroup" aria-labelledby="l%s">'
            '<label><input type="radio" name="%s" value="y"><span>%s</span></label>'
            '<label><input type="radio" name="%s" value="n"><span>%s</span></label>'
            '</span></div>' % (i, label, i, i, yes, i, no))

# ---------------------------------------------------------------------------
# Tool 2. /tools/t2-short-eligibility-checker/
# 6(e): 8 yes-or-no answers in, eligible or not eligible with the failing
# condition named. The eight conditions are the plan's own list, verbatim.
# ---------------------------------------------------------------------------
T2_CONDS = [
 ('c1', 'The corporation is a Canadian-controlled private corporation throughout the tax year.',
  'it is not a Canadian-controlled private corporation throughout the tax year'),
 ('c2', 'It has nil net income, or a loss, for income tax purposes this year.',
  'it does not have nil net income or a loss'),
 ('c3', 'It has one permanent establishment only.',
  'it has more than one permanent establishment'),
 ('c4', 'It paid no taxable dividends and received none in the year.',
  'it paid or received taxable dividends'),
 ('c5', 'It reports in Canadian currency.',
  'it does not report in Canadian currency'),
 ('c6', 'It is claiming no refundable credits.',
  'it is claiming refundable credits'),
 ('c7', 'It has no Ontario transitional tax debit.',
  'it has an Ontario transitional tax debit'),
 ('c8', 'It has no amount calculated under section 34.2.',
  'it has a section 34.2 amount'),
]

T2_FORM = ('<div class="ei-tool">\n<fieldset><legend>The eight T2 Short conditions'
           '</legend>\n'
           + '\n'.join(yn(c[0], c[1]) for c in T2_CONDS)
           + '\n</fieldset>\n<div class="ei-out" id="out" role="status" '
             'aria-live="polite"><p>Answer all eight and the result appears here.'
             '</p></div>\n</div>')

T2_JS = r"""
var CONDS=""" + json.dumps([[c[0], c[2]] for c in T2_CONDS]) + r""";
function pick(n){var e=document.querySelector('input[name="'+n+'"]:checked');
  return e?e.value:null;}
function render(){
  var out=document.getElementById('out'),fails=[],unanswered=0;
  CONDS.forEach(function(c){
    var v=pick(c[0]);
    if(v===null){unanswered++;}else if(v==='n'){fails.push(c[1]);}
  });
  if(unanswered>0){
    out.className='ei-out';
    out.innerHTML='<p>'+unanswered+' of 8 still to answer.</p>';
    return;
  }
  var h;
  if(fails.length===0){
    h='<h3>The T2 Short can be used</h3><span class="ei-big">Eligible</span>'+
      '<p>All eight conditions are met, so this corporation may file on the T2 '+
      'Short rather than the full T2. The T2 Short is included in the fee of '+
      PRICE_JS+'.</p>';
  }else{
    h='<h3>The T2 Short cannot be used</h3><span class="ei-big">Not eligible</span>'+
      '<p>The full T2 is filed instead, because '+
      (fails.length===1?'':'each of the following applies: ')+'</p><ul>';
    fails.forEach(function(f){h+='<li>'+f+'</li>';});
    h+='</ul><p>The full T2 carries the same fee of '+PRICE_JS+'.</p>';
  }
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out '+(fails.length===0?'ok':'no');
  out.innerHTML=h;
}
Array.prototype.forEach.call(document.querySelectorAll('.ei-tool input[type=radio]'),
  function(r){r.addEventListener('change',render);});
render();
"""

# ---------------------------------------------------------------------------
# Tool 3. /tools/gifi-schedule-requirement-checker/
# 6(e): five yes-or-no inputs, Schedules 100, 125 and 141 required or omitted.
# Notes: any one yes makes the three GIFI schedules required.
# ---------------------------------------------------------------------------
T3_ITEMS = [
 ('g1', 'Share capital issued at incorporation or since.', 'share capital'),
 ('g2', 'Any cash or bank balance held during the year.', 'cash or a bank balance'),
 ('g3', 'A shareholder loan outstanding, owed either way.', 'a shareholder loan'),
 ('g4', 'An incorporation cost carried on the books.', 'an incorporation cost'),
 ('g5', 'Any bank charge or other expense in the year.', 'a bank charge or other expense'),
]

T3_FORM = ('<div class="ei-tool">\n<fieldset><legend>What the corporation held or '
           'paid in the tax year</legend>\n'
           + '\n'.join(yn(g[0], g[1]) for g in T3_ITEMS)
           + '\n</fieldset>\n<div class="ei-out" id="out" role="status" '
             'aria-live="polite"><p>Answer all five and the result appears here.'
             '</p></div>\n</div>')

T3_JS = r"""
var ITEMS=""" + json.dumps([[g[0], g[2]] for g in T3_ITEMS]) + r""";
function pick(n){var e=document.querySelector('input[name="'+n+'"]:checked');
  return e?e.value:null;}
function render(){
  var out=document.getElementById('out'),hits=[],unanswered=0;
  ITEMS.forEach(function(g){
    var v=pick(g[0]);
    if(v===null){unanswered++;}else if(v==='y'){hits.push(g[1]);}
  });
  if(unanswered>0){
    out.className='ei-out';
    out.innerHTML='<p>'+unanswered+' of 5 still to answer.</p>';
    return;
  }
  var h;
  if(hits.length>0){
    h='<h3>GIFI Schedules 100, 125 and 141 are required</h3>'+
      '<span class="ei-big">Required</span><p>Because the corporation has '+
      hits.join(', ').replace(/,([^,]*)$/,(hits.length>1?' and':'')+'$1')+
      '. Any one of the five on its own is enough.</p>'+
      '<p>The three schedules are included in the fee of '+PRICE_JS+'.</p>';
  }else{
    h='<h3>GIFI Schedules 100, 125 and 141 may be omitted</h3>'+
      '<span class="ei-big">Not required</span>'+
      '<p>A corporation inactive all year with nothing at all to report may omit '+
      'them. That is a narrow case: most corporations hold share capital from the '+
      'day they are registered, which on its own makes the schedules required.</p>';
  }
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out '+(hits.length>0?'no':'ok');
  out.innerHTML=h;
}
Array.prototype.forEach.call(document.querySelectorAll('.ei-tool input[type=radio]'),
  function(r){r.addEventListener('change',render);});
render();
"""

TOOLS = [
 dict(
  slug='nil-t2-deadline-calculator',
  faq=[
   ('Does the Due Date Move If It Falls on a Weekend?',
    'Yes. Where the due date falls on a Saturday, a Sunday or a public holiday, a return received on the next business day is on time. The calculator shows that next business day whenever it applies.'),
   ('My Year-End Is the Last Day of a Month. How Is Six Months Counted?',
    'From the last day of a month, the due date is the last day of the sixth month after it, so a year-end of August 31 is due the last day of February. From any other day it is the same day of the sixth month after, so a year-end of August 15 is due February 15.'),
   ('Which Public Holidays Does the Business Days Count Use?',
    'The nine Ontario public holidays under the Employment Standards Act: New Year&rsquo;s Day, Family Day, Good Friday, Victoria Day, Canada Day, Labour Day, Thanksgiving, Christmas Day and Boxing Day. The August civic holiday is not among them and is not applied.'),
   ('Is the Due Date Different for a Nil Return?',
    'No. The deadline comes from the Income Tax Act and does not vary with the amounts on the return or by province. A nil T2 is due within six months of the fiscal year-end, the same as any other T2.'),
   ('What Happens to a Due Date That Has Already Passed?',
    'A true nil return carries no percentage late-filing penalty, because that penalty is a percentage of tax owing and the corporation owes $0.00. The unfiled year still stays open forever, invites a demand to file and an arbitrary assessment, blocks a clearance certificate and dissolution, and costs a non-resident-owned corporation $25.00 per day up to $2,500.00. Unfiled years are filed oldest first, one return per tax year.'),
   ('When Is the Final T2 Due After Dissolution?',
    'Within six months of dissolution. Until the corporation is formally dissolved a T2 remains due within six months of every fiscal year-end.'),
  ],
  title='Nil T2 Deadline Calculator | When Your T2 Is Due',
  h1_pre='Nil T2 ', h1_span='Deadline Calculator',
  h1='Nil T2 Deadline Calculator',
  eyebrow='Deadline Tool',
  keyword='nil t2 deadline calculator',
  meta=('Enter your fiscal year-end and get the T2 due date, the next business '
        'day where it falls on a weekend, and the business days remaining.'),
  form=T1_FORM, js=T1_JS,
  sections=[
   ('rule', 'The Rule This Applies',
    '<p>A T2 is due within six months of the corporation&rsquo;s fiscal year-end, '
    'every year, until the corporation is formally dissolved. A final T2 is due '
    'within six months of dissolution.</p>\n'
    '<p>Six months is counted two ways, and the difference matters:</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Where the year-end falls</th>'
    '<th scope="col">The due date</th><th scope="col">Example</th></tr></thead><tbody>\n'
    '<tr><td>On the last day of a month</td><td>The last day of the sixth month '
    'after</td><td>Year-end August 31 is due the last day of February</td></tr>\n'
    '<tr><td>On any other day</td><td>The same day of the sixth month after</td>'
    '<td>Year-end August 15 is due February 15</td></tr>\n'
    '</tbody></table>\n'
    '<p>The deadline comes from the Income Tax Act and does not vary by '
    'province.</p>'),
   ('holidays', 'Weekends and Ontario Statutory Holidays',
    '<p>Where the due date falls on a Saturday, a Sunday or a public holiday, a '
    'return received on the next business day is on time. The calculator shows '
    'that next business day whenever it applies.</p>\n'
    '<p>The business days remaining count excludes weekends and the nine Ontario '
    'public holidays under the Employment Standards Act: New Year&rsquo;s Day, '
    'Family Day, Good Friday, Victoria Day, Canada Day, Labour Day, Thanksgiving, '
    'Christmas Day and Boxing Day. The August civic holiday is not among them and '
    'is not applied.</p>'),
   ('missed', 'A Deadline Already Passed',
    '<div class="ei-danger"><p>A true nil return carries no percentage late-filing '
    'penalty, because that penalty is a percentage of tax owing and the corporation '
    'owes $0.00. The unfiled year still stays open forever, invites a demand to '
    'file and an arbitrary assessment, blocks a clearance certificate and '
    'dissolution, and costs a non-resident-owned corporation $25.00 per day up to '
    '$2,500.00.</p></div>\n'
    '<p>Unfiled years are filed oldest first, one return per tax year.</p>'),
  ],
  related=[(HUB + 't2-short-eligibility-checker/',
            'T2 Short eligibility checker, all eight conditions'),
           (HUB + 'gifi-schedule-requirement-checker/',
            'GIFI schedule requirement checker'),
           (SITE + '/deadlines/', 'Every fiscal year-end and its due date'),
           (SITE + '/guides/first-year-t2-filing/',
            'The complete guide to first-year T2 filing'),
           (SITE + '/pricing/nil-t2-filing-cost/', 'Nil T2 filing cost')]),

 dict(
  slug='t2-short-eligibility-checker',
  faq=[
   ('Does Qualifying for the T2 Short Change the Price?',
    'No. Nil T2 filing is $300.00 plus HST per tax year whichever form the corporation files on. Qualifying for the shorter form does not lower it, and failing to qualify does not raise it.'),
   ('What Happens If the Corporation Fails One Condition?',
    'One failure puts the corporation on the full T2. The T2 Short is available only to a corporation that meets every one of the eight conditions.'),
   ('Does the T2 Short Remove Schedules That Would Otherwise Be Required?',
    'No. Qualifying does not remove a schedule that is otherwise required. The schedules are decided by what the corporation holds and who owns it, not by which form carries them.'),
   ('Must the Corporation Be a CCPC for the Whole Year?',
    'Yes. The condition is that the corporation is a Canadian-controlled private corporation throughout the tax year, not merely at the year-end.'),
   ('Do Taxable Dividends Disqualify the T2 Short?',
    'Yes, in either direction. A corporation with taxable dividends received fails the T2 Short test and is also outside a nil return altogether, so the checker returning not eligible on that condition is worth reading twice.'),
   ('Does Nil Net Income Mean Nil for Accounting Purposes?',
    'No. The condition is nil net income or a loss for income tax purposes, not for accounting purposes.'),
  ],
  title='T2 Short Eligibility Checker | All Eight Conditions',
  h1_pre='T2 Short ', h1_span='Eligibility Checker',
  h1='T2 Short Eligibility Checker',
  eyebrow='Eligibility Tool',
  keyword='t2 short eligibility checker',
  meta=('All eight T2 Short conditions on one screen. Answer them and the checker '
        'names the condition that fails, where one does.'),
  form=T2_FORM, js=T2_JS,
  sections=[
   ('conditions', 'The Eight Conditions',
    '<p>The T2 Short is available only to a corporation that meets every one of '
    'these. One failure puts the corporation on the full T2.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Condition</th>'
    '<th scope="col">What it means</th></tr></thead><tbody>\n'
    '<tr><td>Canadian-controlled private corporation</td><td>Throughout the tax '
    'year, not merely at the year-end</td></tr>\n'
    '<tr><td>Nil net income or a loss</td><td>For income tax purposes, not for '
    'accounting purposes</td></tr>\n'
    '<tr><td>One permanent establishment</td><td>A second province or a second '
    'fixed place of business ends it</td></tr>\n'
    '<tr><td>No taxable dividends paid or received</td><td>Either direction '
    'disqualifies</td></tr>\n'
    '<tr><td>Canadian currency</td><td>A functional currency election ends it</td>'
    '</tr>\n'
    '<tr><td>No refundable credits</td><td>Claiming one puts the corporation on '
    'the full return</td></tr>\n'
    '<tr><td>No Ontario transitional tax debit</td><td>Applies to certain Ontario '
    'corporations</td></tr>\n'
    '<tr><td>No section 34.2 amount</td><td>Applies where a corporation has a '
    'stub-period accrual</td></tr>\n'
    '</tbody></table>'),
   ('either-way', 'The Fee Is the Same Either Way',
    '<p>Qualifying for the shorter form does not change the price, and failing to '
    'qualify does not raise it. Nil T2 filing is ' + PRICE + ' whichever form the '
    'corporation files on.</p>\n'
    '<p>Qualifying also does not remove a schedule that is otherwise required. The '
    'schedules are decided by what the corporation holds and who owns it, not by '
    'which form carries them.</p>'),
   ('not-nil', 'Where the Corporation Is Not Nil at All',
    '<div class="ei-warn"><p>' + NOT_NIL + '</p></div>\n'
    '<p>A corporation with taxable dividends received fails the T2 Short test and '
    'is also outside a nil return altogether, so the checker returning "not '
    'eligible" on that condition is worth reading twice.</p>'),
  ],
  related=[(HUB + 'nil-t2-deadline-calculator/',
            'Nil T2 deadline calculator'),
           (HUB + 'gifi-schedule-requirement-checker/',
            'GIFI schedule requirement checker'),
           (SITE + '/guides/t2-short-eligibility/',
            'The complete guide to T2 Short eligibility'),
           (SITE + '/guides/t2-schedules-on-a-nil-return/',
            'T2 schedules on a nil return'),
           (SITE + '/pricing/nil-t2-filing-cost/', 'Nil T2 filing cost')]),

 dict(
  slug='gifi-schedule-requirement-checker',
  faq=[
   ('Does a Nil Corporation Still File GIFI Schedules?',
    'Usually yes. A corporation inactive all year with nothing at all to report may omit Schedules 100, 125 and 141, but any share capital, cash, shareholder loan, incorporation cost or bank charge makes all three required.'),
   ('Are the Three Schedules Included in the Fee?',
    'Yes. All three are included in the fee of $300.00 plus HST per tax year where they are required. There is no per-schedule charge.'),
   ('Does $100.00 of Share Capital Make the Schedules Required?',
    'Yes. The exemption needs nothing at all to report. A corporation holding $100.00 of share capital issued at incorporation has something to report, so the schedules are required.'),
   ('What Are Schedules 100, 125 and 141?',
    'Schedule 100 is the balance sheet in GIFI codes. Schedule 125 is the income statement, which on a genuinely nil year reports $0.00 on both sides rather than being left out. Schedule 141 is the notes checklist that records who prepared the financial information.'),
   ('How Many of the Five Triggers Does It Take?',
    'One. Any one of the five on its own makes all three schedules required.'),
   ('Why Is the Exemption Narrower Than It Reads?',
    'Four of the five triggers are present in most corporations from the day they are registered. Most hold share capital, which on its own makes the schedules required.'),
  ],
  title='GIFI Schedule Requirement Checker | Schedules 100, 125, 141',
  h1_pre='GIFI Schedule ', h1_span='Requirement Checker',
  h1='GIFI Schedule Requirement Checker',
  eyebrow='Schedules Tool',
  keyword='gifi schedule requirement checker',
  meta=('Five questions decide whether a nil T2 needs GIFI Schedules 100, 125 and '
        '141. Any one yes makes all three required.'),
  form=T3_FORM, js=T3_JS,
  sections=[
   ('rule', 'The Rule, Stated Exactly',
    '<p>A corporation inactive all year with nothing to report may omit GIFI '
    'Schedules 100, 125 and 141, but any share capital, cash, shareholder loan, '
    'incorporation cost or bank charge makes them required.</p>\n'
    '<div class="ei-warn"><p>Read the second half carefully. The exemption needs '
    '<em>nothing at all</em> to report. A corporation holding $100.00 of share '
    'capital issued at incorporation has something to report, so the schedules are '
    'required.</p></div>'),
   ('five', 'Why Each of the Five Counts',
    '<table class="ei-tbl"><thead><tr><th scope="col">Trigger</th>'
    '<th scope="col">Why it counts</th></tr></thead><tbody>\n'
    '<tr><td>Share capital</td><td>Issued at incorporation and sits on the balance '
    'sheet</td></tr>\n'
    '<tr><td>Cash</td><td>A balance in an account is an asset</td></tr>\n'
    '<tr><td>A shareholder loan</td><td>A balance either owed to or by the '
    'corporation</td></tr>\n'
    '<tr><td>An incorporation cost</td><td>Capitalised, so it remains on the '
    'balance sheet</td></tr>\n'
    '<tr><td>A bank charge</td><td>An expense, so there is something on the income '
    'statement</td></tr>\n'
    '</tbody></table>\n'
    '<p>Four of the five are present in most corporations from the day they are '
    'registered, which is why the exemption is narrower in practice than it '
    'reads.</p>'),
   ('three', 'What the Three Schedules Are',
    '<p>Schedule 100 is the balance sheet in GIFI codes. Schedule 125 is the income '
    'statement, which on a genuinely nil year reports $0.00 on both sides rather '
    'than being left out. Schedule 141 is the notes checklist that records who '
    'prepared the financial information.</p>\n'
    '<p>All three are included in the fee of ' + PRICE + ' where they are '
    'required. There is no per-schedule charge.</p>'),
  ],
  related=[(HUB + 'nil-t2-deadline-calculator/',
            'Nil T2 deadline calculator'),
           (HUB + 't2-short-eligibility-checker/',
            'T2 Short eligibility checker, all eight conditions'),
           (SITE + '/guides/gifi-schedules-100-125-141/',
            'The complete guide to GIFI Schedules 100, 125 and 141'),
           (SITE + '/guides/t2-schedules-on-a-nil-return/',
            'T2 schedules on a nil return'),
           (SITE + '/pricing/nil-t2-filing-cost/', 'Nil T2 filing cost')]),
]

# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------
def render(t):
    """Wrapped in a wp:html block, which is not optional here.

    Without it the content is classic content and wpautop runs over it. That
    filter does not just add paragraphs: it treats the literal "<p>" and "</p>"
    inside the module's own JavaScript strings as markup, rewrites them with
    newlines around them, and leaves string literals broken across lines. The
    module then fails to parse and nothing runs. It also splits the stylesheet
    at the blank line between the base and tool rules.

    `has_blocks()` is true as soon as the content holds a "<!-- wp:" comment,
    and do_blocks then removes wpautop from the_content for that render. The
    Family 4 pages have used this wrapper from the start, which is why their
    markup survives and these pages did not.
    """
    url = HUB + t['slug'] + '/'
    p = ['<!-- wp:html -->\n', CSS]
    p.append(
     '<div class="ei-hero"><div class="ei-hero-inner">'
     '<span class="ei-hero-eyebrow">' + t['eyebrow'] + '</span>'
     '<h1>' + t['h1_pre'] + '<span>' + t['h1_span'] + '</span></h1>'
     '<p class="ei-hero-sub">' + t['meta'] + '</p>'
     '<p class="ei-hero-by">' + BYLINE + '</p>'
     '<div class="ei-hero-btns"><a class="ei-btn-blue" href="' + FORM + '">'
     'Start Nil T2 Filing NOW</a></div></div></div>\n')

    p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
             '<p class="ei-updated">Last reviewed: ' + TODAY + '</p>\n'
             + t['form'] + '\n'
             '<div class="ei-info"><p>' + EFILE + '</p></div>\n'
             '</div></div>\n')

    for i, (k, h2, body) in enumerate(t['sections']):
        cls = 'ei-section-alt' if i % 2 == 0 else 'ei-section'
        p.append('<div class="%s" id="%s"><div class="ei-wrap ei-art">\n'
                 '<h2 class="ei-h2">%s</h2>\n%s\n</div></div>\n' % (cls, k, h2, body))

    p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
             '<h2 class="ei-h2">Frequently Asked Questions</h2>\n'
             '<div class="ei-faq">\n'
             + '\n'.join(
               '<details><summary>%s</summary><div class="ei-faq-a">'
               '<p>%s</p></div></details>' % (q, ans) for q, ans in t['faq'])
             + '\n</div>\n</div></div>\n')

    p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
             '<h2 class="ei-h2">Read Next</h2>\n<ul class="ei-qlist">\n'
             + '\n'.join('<li>%s</li>' % a(h, l) for h, l in t['related'])
             + '\n</ul>\n</div></div>\n')

    p.append('<div class="ei-cta-bottom"><div class="ei-wrap">'
             '<h2>Nil T2 Filing, ' + PRICE + '</h2>'
             '<p>Type your corporation name, pick your unfiled years, pay, and sign '
             'Form T183CORP on a secure screen. Your CRA confirmation is emailed '
             'within 3 business days.</p>'
             '<a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
             '</div></div>\n')

    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": t['title'],
       "description": t['meta'], "inLanguage": "en-CA", "dateModified": ISO,
       "author": {"@type": "Person", "name": "Sharad Gondaliya",
                  "honorificSuffix": "CPA",
                  "url": SITE + "/sharad-gondaliya-cpa/"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
         "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Tools", "item": HUB},
        {"@type": "ListItem", "position": 3, "name": t['h1'], "item": url}]}]}
    p.append('<script type="application/ld+json">'
             + json.dumps(schema, ensure_ascii=False) + '</script>\n')

    # The module runs last so the markup it binds to already exists. PRICE and the
    # 6(c) disclaimer are passed in rather than repeated inside the module.
    p.append('<script>\n(function(){\nvar PRICE_JS=' + json.dumps(PRICE)
             + ';\nvar DISC_JS=' + json.dumps(TOOL_DISCLAIMER) + ';\n'
             + t['js'] + '\n})();\n</script>\n<!-- /wp:html -->')
    return ''.join(p), url


def meta(t):
    return {
     'site-sidebar-layout': 'no-sidebar', 'site-content-layout': 'page-builder',
     'ast-site-content-layout': 'full-width-container',
     'site-post-title': 'disabled', 'ast-breadcrumbs-content': 'disabled',
     'ast-featured-img': 'disabled',
     'cnf_primary_keyword': t['keyword'],
     'cnf_last_verified_et': ISO,
    }


if __name__ == '__main__':
    recs = []
    for t in TOOLS:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], h1=t['h1'], url=url,
                         meta_description=t['meta'], content=html, meta=meta(t)))
        print('%-38s %6d bytes' % (t['slug'], len(html.encode())))
    json.dump([{k: v for k, v in r.items() if k != 'content'} for r in recs],
              io.open(os.path.join(HERE, 'f2-manifest.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
