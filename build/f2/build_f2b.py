# -*- coding: utf-8 -*-
"""Family 2, tools 4 to 10.

Everything structural is imported from build_f2 so the two batches cannot
drift: the same CSS (including the navy panel, the 1000px column, the FAQ
accordion and the stat cards), the same render(), the same schema and the same
wp:html wrapper.

Slugs follow 6(e), not Appendix A, for the same reason recorded for the first
three: the nil_calculator rewrite base decides the URL. Appendix A's
/catch-up-nil-filing-cost-calculator/, /unfiled-years-checker/,
/first-tax-year-53-week-checker/ and /gifi-requirement-checker/ are the tenth
Appendix A conflict and resolve to the 6(e) names.

The Ontario annual return due date calculator named in 6(e) is NOT here. The
plan states the Ontario annual return is filed through the Ontario Business
Registry and is not covered by the fee, but nowhere states its due date, and
line 1212 reserves every jurisdiction claim for Sharad Gondaliya. Building it
would have meant inventing the rule. The GST/HST nil filing checker, also from
6(e) and fully grounded, takes its place in this batch.
"""
import io, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_f2 import (render, meta, yn, a, DATE_JS, SITE, HUB, FORM, PRICE,
                      TODAY, ISO, NOT_NIL, TOOL_DISCLAIMER)

T = HUB  # tools base
G = SITE + '/guides/'
COST = SITE + '/pricing/nil-t2-filing-cost/'


def out_box(msg):
    return ('<div class="ei-out" id="out" role="status" aria-live="polite">'
            '<p>' + msg + '</p></div>')


def tool(legend, rows, msg):
    return ('<div class="ei-tool">\n<fieldset><legend>' + legend + '</legend>\n'
            + '\n'.join(rows) + '\n</fieldset>\n' + out_box(msg) + '\n</div>')


def num(i, label, hint, mn, mx, ph):
    return ('<div class="ei-f"><label for="%s">%s</label>'
            '<input type="number" id="%s" min="%s" max="%s" step="1" '
            'placeholder="%s" inputmode="numeric"></div>' % (i, label, i, mn, mx, ph))


def date(i, label):
    return ('<div class="ei-f"><label for="%s">%s</label>'
            '<input type="date" id="%s"></div>' % (i, label, i))


PICK = """function pick(n){var e=document.querySelector('input[name="'+n+'"]:checked');
  return e?e.value:null;}
"""

# ---------------------------------------------------------------- 4. unfiled
T4_JS = r"""
var el=document.getElementById('n'),out=document.getElementById('out');
function money(c){var s=(c/100).toFixed(2),p=s.split('.');
  return '$'+p[0].replace(/\B(?=(\d{3})+(?!\d))/g,',')+'.'+p[1];}
function render(){
  var v=el.value.trim();
  if(v===''){out.className='ei-out';
    out.innerHTML='<p>Enter how many tax years are unfiled and the total appears here.</p>';
    return;}
  var n=parseInt(v,10);
  if(isNaN(n)||n<1||n>20){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">Enter a whole number of years from 1 to 20.</p>';
    return;}
  var total=n*30000;
  var h='<h3>'+n+' unfiled tax year'+(n===1?'':'s')+'</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">Returns to file</span>'+
     '<span class="ei-stat-v">'+n+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Fee per tax year</span>'+
     '<span class="ei-stat-v">$300.00</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Total before HST</span>'+
     '<span class="ei-stat-v">'+money(total)+'</span></div></div>';
  h+='<p>'+n+' tax year'+(n===1?'':'s')+' at '+PRICE_JS+' is '+money(total)+
     ' plus HST. Each tax year is a separate return and carries the same fee.</p>';
  h+='<p>Unfiled years are filed oldest first, one return per tax year, so the '+
     'Canada Revenue Agency assesses them in the order they fell due.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out ok';out.innerHTML=h;
}
el.addEventListener('input',render);render();
"""

# ------------------------------------------------------------- 5. schedule 50
T5_JS = r"""
var IDS=['s1','s2','s3','s4','s5'],out=document.getElementById('out');
function render(){
  var vals=[],bad=false,sum=0,need=[],no=[];
  IDS.forEach(function(id,i){
    var v=document.getElementById(id).value.trim();
    if(v===''){return;}
    var n=parseFloat(v);
    if(isNaN(n)||n<0||n>100){bad=true;return;}
    vals.push([i+1,n]);sum+=n;
    if(n>=10){need.push('Shareholder '+(i+1)+' at '+n+'%');}
    else{no.push('Shareholder '+(i+1)+' at '+n+'%');}
  });
  if(bad){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">Each holding must be a number from 0 to 100.</p>';
    return;}
  if(vals.length===0){out.className='ei-out';
    out.innerHTML='<p>Enter at least one shareholder percentage and the result appears here.</p>';
    return;}
  var h='<h3>'+(need.length>0?'Schedule 50 is required':'Schedule 50 is not required')+'</h3>';
  h+='<span class="ei-big">'+need.length+' of '+vals.length+' shareholder'+
     (vals.length===1?'':'s')+' at 10% or more</span>';
  if(need.length>0){
    h+='<p>Schedule 50 reports every shareholder holding 10% or more:</p><ul><li>'+
       need.join('</li><li>')+'</li></ul>';
  }else{
    h+='<p>No holding reaches 10%, so no shareholder has to be listed on Schedule 50.</p>';
  }
  if(no.length>0&&need.length>0){
    h+='<p>Below the threshold, and not listed: '+no.join(', ')+'.</p>';
  }
  if(sum>100.0001){
    h+='<p class="ei-err">The holdings entered add up to '+(Math.round(sum*100)/100)+
       '%, which is more than the whole corporation. Check the figures.</p>';
  }
  h+='<p>Schedule 50 is included in the fee of '+PRICE_JS+' where it is required.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out '+(need.length>0?'no':'ok');out.innerHTML=h;
}
IDS.forEach(function(id){document.getElementById(id).addEventListener('input',render);});
render();
"""

# ----------------------------------------------------------------- 6. 53 week
T6_JS = DATE_JS + r"""
var out=document.getElementById('out');
function parse(id){var v=document.getElementById(id).value;
  if(!v){return null;}var p=v.split('-');var d=u(+p[0],+p[1]-1,+p[2]);
  return isNaN(d.getTime())?undefined:d;}
function render(){
  var inc=parse('inc'),ye=parse('ye');
  if(inc===null||ye===null){out.className='ei-out';
    out.innerHTML='<p>Enter both dates and the first tax year is checked here.</p>';
    return;}
  if(inc===undefined||ye===undefined){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';return;}
  if(ye.getTime()<=inc.getTime()){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">The year-end must fall after the incorporation date.</p>';
    return;}
  var days=Math.round((ye.getTime()-inc.getTime())/86400000)+1;
  var latest=new Date(inc.getTime()+370*86400000);
  var ok=days<=371;
  var h='<h3>'+(ok?'This first tax year is within 53 weeks':
                   'This first tax year is longer than 53 weeks')+'</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">Length of the first tax year</span>'+
     '<span class="ei-stat-v">'+days+' days</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Maximum permitted</span>'+
     '<span class="ei-stat-v">371 days</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Latest permitted year-end</span>'+
     '<span class="ei-stat-v">'+fmt(latest)+'</span></div></div>';
  if(ok){
    h+='<p>A first tax year of '+days+' days runs from '+fmt(inc)+' to '+fmt(ye)+
       ', which is within the 53 weeks a first tax year may not exceed.</p>';
  }else{
    h+='<p>A first tax year of '+days+' days exceeds 53 weeks by '+(days-371)+
       ' day'+(days-371===1?'':'s')+'. The latest year-end this corporation may '+
       'choose for its first tax year is '+fmt(latest)+'.</p>';
  }
  h+='<p>The year-end must also match the date the Canada Revenue Agency holds, '+
     'or the transmission is rejected.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out '+(ok?'ok':'no');out.innerHTML=h;
}
['inc','ye'].forEach(function(id){
  document.getElementById(id).addEventListener('input',render);
  document.getElementById(id).addEventListener('change',render);});
render();
"""

# ------------------------------------------------------------- 7. schedule 24
T7_ITEMS = [('q1', 'This is the first T2 the corporation has filed since it was '
                   'incorporated.'),
            ('q2', 'The Canada Revenue Agency has already assessed an earlier T2 '
                   'for this corporation.'),
            ('q3', 'The corporation was incorporated in the tax year you are '
                   'filing.')]
T7_JS = PICK + r"""
var out=document.getElementById('out');
function render(){
  var a=pick('q1'),b=pick('q2'),c=pick('q3');
  if(a===null||b===null||c===null){
    var n=[a,b,c].filter(function(x){return x===null;}).length;
    out.className='ei-out';
    out.innerHTML='<p>'+n+' of 3 still to answer.</p>';return;}
  var first=(a==='y'&&b==='n');
  var h;
  if(first){
    h='<h3>Schedule 24 is required</h3><span class="ei-big">Required</span>'+
      '<p>Schedule 24 is filed with the first T2 after incorporation. It reports '+
      'the corporation&rsquo;s first-time filer information.</p>';
    if(c==='n'){
      h+='<p>The corporation was incorporated in an earlier year, so this first '+
         'return is also a late one. Unfiled years are filed oldest first.</p>';
    }
  }else if(b==='y'){
    h='<h3>Schedule 24 is not required</h3><span class="ei-big">Not required</span>'+
      '<p>An earlier T2 has already been assessed, so this is not the first '+
      'return and Schedule 24 does not belong on it.</p>';
  }else{
    h='<h3>Schedule 24 is not required</h3><span class="ei-big">Not required</span>'+
      '<p>On your answers this is not the corporation&rsquo;s first T2, so '+
      'Schedule 24 does not belong on it.</p>';
  }
  h+='<p>Schedule 24 is included in the fee of '+PRICE_JS+' where it is required. '+
     'There is no per-schedule charge.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out '+(first?'no':'ok');out.innerHTML=h;
}
Array.prototype.forEach.call(document.querySelectorAll('.ei-tool input[type=radio]'),
  function(r){r.addEventListener('change',render);});
render();
"""

# ------------------------------------------------------------- 8. federal 60d
T8_JS = DATE_JS + r"""
var out=document.getElementById('out');
function render(){
  var v=document.getElementById('inc').value;
  if(!v){out.className='ei-out';
    out.innerHTML='<p>Enter your federal incorporation date and the annual return due date appears here.</p>';
    return;}
  var p=v.split('-'),inc=u(+p[0],+p[1]-1,+p[2]);
  if(isNaN(inc.getTime())){out.className='ei-out no';
    out.innerHTML='<p class="ei-err">That is not a date we can read.</p>';return;}
  var t=today(),y=t.getUTCFullYear();
  var m=inc.getUTCMonth(),d=inc.getUTCDate();
  var ann=u(y,m,Math.min(d,lastDay(y,m)));
  if(ann.getTime()<t.getTime()){ann=u(y+1,m,Math.min(d,lastDay(y+1,m)));}
  var due=new Date(ann.getTime()+60*86400000);
  var h='<h3>Your federal annual return</h3>';
  h+='<div class="ei-stats">'+
     '<div class="ei-stat"><span class="ei-stat-l">Next anniversary</span>'+
     '<span class="ei-stat-v">'+fmt(ann)+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Annual return due</span>'+
     '<span class="ei-stat-v">'+fmt(due)+'</span></div>'+
     '<div class="ei-stat"><span class="ei-stat-l">Government fee</span>'+
     '<span class="ei-stat-v">$12.00</span></div></div>';
  h+='<p>The federal annual return is due within 60 days of the anniversary of '+
     'incorporation, so for an anniversary of '+fmt(ann)+' it is due by '+fmt(due)+
     '. It is filed with Corporations Canada, not with the T2, and the $12.00 is '+
     'a government fee to which HST does not apply.</p>';
  h+='<p>This filing is separate from your nil T2 and is not covered by the fee '+
     'of '+PRICE_JS+'. We tell you if you still owe it.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out ok';out.innerHTML=h;
}
['input','change'].forEach(function(e){
  document.getElementById('inc').addEventListener(e,render);});
render();
"""

# ----------------------------------------------------------------- 9. dormant
T9_ITEMS = [
 ('d1', 'Revenue or sales of any amount in the tax year.', 'revenue or sales'),
 ('d2', 'Interest credited on a bank balance, however small.', 'interest credited on a bank balance'),
 ('d3', 'A dividend paid to a shareholder.', 'a dividend paid'),
 ('d4', 'A dividend received from another corporation.', 'a dividend received'),
 ('d5', 'Rental income from property the corporation owns.', 'rental income'),
 ('d6', 'Investment income of any kind.', 'investment income'),
 ('d7', 'Wages, salary or any payroll paid.', 'payroll paid'),
 ('d8', 'An asset bought or sold.', 'an asset bought or sold'),
 ('d9', 'A transaction with a related or associated corporation.', 'an inter-company transaction'),
 ('d10', 'GST/HST charged or collected on anything.', 'GST/HST charged or collected'),
]
T9_JS = PICK + r"""
var ITEMS=""" + json.dumps([[i[0], i[2]] for i in T9_ITEMS]) + r""";
var out=document.getElementById('out');
function render(){
  var hits=[],un=0;
  ITEMS.forEach(function(g){var v=pick(g[0]);
    if(v===null){un++;}else if(v==='y'){hits.push(g[1]);}});
  if(un>0){out.className='ei-out';
    out.innerHTML='<p>'+un+' of 10 still to answer.</p>';return;}
  var h;
  if(hits.length===0){
    h='<h3>This corporation looks nil for the tax year</h3>'+
      '<span class="ei-big">Nil</span>'+
      '<p>Nothing you have reported is activity, so the year is reported as a nil '+
      'T2 at '+PRICE_JS+'. Share capital, cash, a shareholder loan, an '+
      'incorporation cost or a bank charge does not stop a year being nil, though '+
      'it does make GIFI Schedules 100, 125 and 141 required.</p>';
  }else{
    h='<h3>This corporation is not nil for the tax year</h3>'+
      '<span class="ei-big">Not nil</span>'+
      '<p>Because the corporation has '+
      hits.join(', ').replace(/,([^,]*)$/,(hits.length>1?' and':'')+'$1')+
      '. Any one of the ten on its own is enough.</p>'+
      '<p>A corporation like this is routed to our sister office at '+
      'gondaliyacpa.ca at $350.00 plus HST per year, before you pay. If we find '+
      'it after you pay, we refund you in full.</p>';
  }
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out '+(hits.length>0?'no':'ok');out.innerHTML=h;
}
Array.prototype.forEach.call(document.querySelectorAll('.ei-tool input[type=radio]'),
  function(r){r.addEventListener('change',render);});
render();
"""

# ---------------------------------------------------------------- 10. gst/hst
T10_ITEMS = [('g1', 'The corporation has an open GST/HST account with the Canada '
                    'Revenue Agency.'),
             ('g2', 'The corporation has an open payroll account.'),
             ('g3', 'The corporation expects to trade again in the next few years.')]
T10_JS = PICK + r"""
var out=document.getElementById('out');
function render(){
  var g=pick('g1'),p=pick('g2'),f=pick('g3');
  if(g===null||p===null||f===null){
    var n=[g,p,f].filter(function(x){return x===null;}).length;
    out.className='ei-out';
    out.innerHTML='<p>'+n+' of 3 still to answer.</p>';return;}
  var open=[];
  if(g==='y'){open.push('GST/HST');}
  if(p==='y'){open.push('payroll');}
  var h;
  if(open.length===0){
    h='<h3>No nil GST/HST or payroll filing is outstanding</h3>'+
      '<span class="ei-big">Nothing open</span>'+
      '<p>With neither account open there is no nil GST/HST return and no nil '+
      'payroll return to file. Your T2 obligation is unaffected and continues '+
      'every year until the corporation is dissolved.</p>';
  }else{
    h='<h3>A nil filing is still required</h3>'+
      '<span class="ei-big">'+open.join(' and ')+' still open</span>'+
      '<p>An open account carries its own filing obligation whether or not the '+
      'corporation traded. Nil returns are due on the '+open.join(' and ')+
      ' account'+(open.length>1?'s':'')+' until '+(open.length>1?'they are':'it is')+
      ' closed.</p>';
    if(f==='n'){
      h+='<p>Since the corporation is not expected to trade again, the account'+
         (open.length>1?'s':'')+' can be closed with Form RC145, which ends the '+
         'nil filings rather than repeating them every period.</p>';
    }else{
      h+='<p>Since the corporation expects to trade again, keeping the account'+
         (open.length>1?'s':'')+' open is reasonable, and the nil returns continue '+
         'in the meantime. Form RC145 closes an account when you no longer want it.</p>';
    }
  }
  h+='<p>Neither a nil GST/HST return, a nil payroll return nor an RC145 closure '+
     'is covered by the nil T2 fee of '+PRICE_JS+'. We tell you which of these '+
     'you still owe.</p>';
  h+='<p class="ei-note">'+DISC_JS+'</p>';
  out.className='ei-out '+(open.length>0?'no':'ok');out.innerHTML=h;
}
Array.prototype.forEach.call(document.querySelectorAll('.ei-tool input[type=radio]'),
  function(r){r.addEventListener('change',render);});
render();
"""

# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------
TOOLS2 = [
 dict(slug='unfiled-years-cost-calculator',
  title='Unfiled Years Cost Calculator | Nil T2 Catch-Up Total',
  h1_pre='Unfiled Years ', h1_span='Cost Calculator', h1='Unfiled Years Cost Calculator',
  eyebrow='Cost Tool', keyword='unfiled years cost calculator',
  meta=('Enter how many tax years are unfiled and the calculator returns the '
        'total at $300.00 plus HST per tax year.'),
  tags=['One return per tax year', 'Same fee every year',
        'Oldest year filed first', 'No hourly billing'],
  form=tool('How many tax years are unfiled',
            [num('n', 'Number of unfiled tax years',
                 '', '1', '20', '6')],
            'Enter how many tax years are unfiled and the total appears here.'),
  js=T4_JS,
  sections=[
   ('how', 'One Return, One Year, One Fee',
    '<p>Each tax year is a separate T2 and carries the same fee of ' + PRICE +
    '. There is no hourly billing, no per-schedule charge and no surcharge for '
    'a year that is late.</p>\n'
    '<table class="ei-tbl"><thead><tr><th scope="col">Unfiled tax years</th>'
    '<th scope="col">Total before HST</th></tr></thead><tbody>\n'
    '<tr><td>1</td><td>$300.00</td></tr>\n'
    '<tr><td>3</td><td>$900.00</td></tr>\n'
    '<tr><td>5</td><td>$1,500.00</td></tr>\n'
    '<tr><td>6</td><td>$1,800.00</td></tr>\n'
    '</tbody></table>\n'
    '<p>Tax is added at the rate for your province.</p>'),
   ('order', 'Years Are Filed Oldest First',
    '<p>Unfiled years are filed oldest first, one return per tax year, so the '
    'Canada Revenue Agency assesses them in the order they fell due.</p>\n'
    '<div class="ei-danger"><p>A true nil return carries no percentage '
    'late-filing penalty, because that penalty is a percentage of tax owing and '
    'the corporation owes $0.00. The unfiled year still stays open forever, '
    'invites a demand to file and an arbitrary assessment, blocks a clearance '
    'certificate and dissolution, and costs a non-resident-owned corporation '
    '$25.00 per day up to $2,500.00.</p></div>'),
   ('covers', 'What Each Return Includes',
    '<p>The fee covers one nil T2 for one corporation for one tax year, '
    'including the T2 Short where the corporation qualifies, GIFI Schedules '
    '100, 125 and 141 where they are required, Schedule 24 on a first return, '
    'Schedule 50 for every shareholder at 10% or more, Schedule 8 and loss '
    'continuity, your Form T183CORP package, single-use secure e-signing, CPA '
    'review, electronic transmission by a registered EFILE electronic filer, '
    'one corrected transmission if the Agency rejects the first one, and your '
    'CRA confirmation emailed within 3 business days.</p>'),
  ],
  faq=[
   ('Does a Late Year Cost More Than a Current One?',
    'No. A year filed late costs the same as a current one, ' + PRICE + ', '
    'with no late surcharge and no hourly billing.'),
   ('How Many Years Can Be Filed at Once?',
    'There is no limit in the tool or in the filing. Years are prepared '
    'together and transmitted oldest first, one return per tax year.'),
   ('Is HST Included in the Figure the Calculator Shows?',
    'No. The calculator shows the fee before tax, the number of years '
    'multiplied by $300.00. Tax is then added at the rate for your province, '
    'because the price is ' + PRICE + '.'),
   ('Does Every Unfiled Year Need Its Own Form T183CORP?',
    'Yes. Each tax year is a separate return and carries its own T183CORP, '
    'signed before that year is transmitted. All of them are included in the '
    'fee for those years.'),
   ('What If One of the Years Is Not Nil?',
    NOT_NIL + ' We check before you pay. If we find it afterwards, we refund '
    'you in full.'),
  ]),

 dict(slug='schedule-50-shareholder-threshold-checker',
  title='Schedule 50 Shareholder Threshold Checker | The 10% Rule',
  h1_pre='Schedule 50 ', h1_span='Shareholder Checker',
  h1='Schedule 50 Shareholder Threshold Checker',
  eyebrow='Shareholder Tool', keyword='schedule 50 shareholder threshold checker',
  meta=('Enter each shareholding and the checker names every shareholder at 10% '
        'or more, who must be listed on Schedule 50.'),
  tags=['The 10% threshold', 'Up to five shareholders',
        'Named shareholder by shareholder', 'Included in the fee'],
  form=tool('Each shareholder&rsquo;s percentage of the corporation',
            [num('s%d' % i, 'Shareholder %d, percentage held' % i,
                 '', '0', '100', '')
             for i in range(1, 6)],
            'Enter at least one shareholder percentage and the result appears here.'),
  js=T5_JS,
  sections=[
   ('rule', 'The 10% Rule, Stated Exactly',
    '<p>Schedule 50 is required for any shareholder holding 10% or more of the '
    'corporation. Exactly 10% is inside the threshold, not outside it.</p>\n'
    '<div class="ei-info"><p>A nil year does not remove the schedule. Schedule '
    '50 reports who owns the corporation, and ownership does not depend on '
    'whether the corporation traded.</p></div>'),
   ('what', 'What Schedule 50 Reports',
    '<p>For each shareholder at or above the threshold, Schedule 50 carries the '
    'name, the percentage of common and preferred shares held, and the business '
    'number or social insurance number as applicable.</p>\n'
    '<p>A corporation held entirely by one person reports that one shareholder '
    'at 100%. A corporation with ten shareholders at 10% each reports all ten.</p>'),
   ('fee', 'Included in the Fee',
    '<p>Schedule 50 is included in the fee of ' + PRICE + ' where it is '
    'required. There is no per-schedule charge, and adding shareholders does '
    'not change the price.</p>'),
  ],
  faq=[
   ('Is a Shareholder at Exactly 10% Included?',
    'Yes. The threshold is 10% or more, so a holding of exactly 10% is '
    'reported on Schedule 50.'),
   ('Does a Nil Year Remove Schedule 50?',
    'No. Schedule 50 reports who owns the corporation, not what it earned, so '
    'a year with no activity does not remove it.'),
   ('What If the Corporation Has Only One Shareholder?',
    'That shareholder holds 100%, which is above the threshold, so Schedule 50 '
    'is required and reports the single holding.'),
   ('Are Preferred Shares Counted Separately?',
    'Schedule 50 carries the percentage of common shares and the percentage of '
    'preferred shares held, so a shareholder can appear for either or both.'),
   ('Does Adding Shareholders Increase the Fee?',
    'No. The fee is ' + PRICE + ' however many shareholders the schedule '
    'reports. There is no per-schedule and no per-shareholder charge.'),
  ]),

 dict(slug='53-week-first-tax-year-checker',
  title='53-Week First Tax Year Checker | First T2 Year-End',
  h1_pre='53-Week ', h1_span='First Tax Year Checker',
  h1='53-Week First Tax Year Checker',
  eyebrow='Year-End Tool', keyword='53 week first tax year checker',
  meta=('Enter the incorporation date and a proposed year-end. The checker '
        'returns whether the first tax year is within the 53 weeks it may not '
        'exceed.'),
  tags=['53 weeks is 371 days', 'Latest permitted year-end',
        'Prevents a rejected transmission', 'First return only'],
  form=tool('Your incorporation date and proposed first year-end',
            [date('inc', 'Date the corporation was incorporated'),
             date('ye', 'Proposed end of the first tax year')],
            'Enter both dates and the first tax year is checked here.'),
  js=T6_JS,
  sections=[
   ('rule', 'The Rule This Applies',
    '<p>A corporation&rsquo;s first tax year cannot exceed 53 weeks. Fifty-three '
    'weeks is 371 days, counted from the date of incorporation to the chosen '
    'year-end inclusive.</p>\n'
    '<p>After the first year, a tax year cannot exceed 53 weeks either, and the '
    'corporation keeps the year-end it chose unless the Agency approves a '
    'change.</p>'),
   ('rejected', 'Why a Wrong Year-End Is Rejected',
    '<div class="ei-warn"><p>The year-end on the return must match the date the '
    'Canada Revenue Agency holds for the corporation. A year-end that does not '
    'match is one of the common causes of a rejected transmission, and one '
    'corrected transmission is included in the fee of ' + PRICE + '.</p></div>\n'
    '<p>A first tax year longer than 53 weeks is rejected on the rule itself, '
    'whatever the Agency holds.</p>'),
   ('choosing', 'Choosing the First Year-End',
    '<p>Any date within 53 weeks of incorporation is permitted. A corporation '
    'that expects to stay dormant often takes the longest permitted year-end, '
    'which puts the first T2 as far out as the rule allows. The T2 is then due '
    'within six months of that year-end.</p>'),
  ],
  faq=[
   ('How Many Days Is 53 Weeks?',
    '371 days, counted from the date of incorporation to the year-end '
    'inclusive. A first tax year of 372 days or more is too long.'),
   ('Can the First Tax Year Be Shorter Than a Year?',
    'Yes. There is no minimum. A corporation incorporated in November may take '
    'a December 31 year-end, giving a first tax year of a few weeks.'),
   ('Does the 53-Week Rule Apply After the First Year?',
    'Yes. No tax year may exceed 53 weeks. The first year is where the rule is '
    'usually met, because that is when the year-end is chosen.'),
   ('What Happens If the Year-End Does Not Match CRA Records?',
    'The transmission is rejected. One corrected transmission is included in '
    'the fee of ' + PRICE + ', so a mismatch costs time rather than money.'),
   ('When Is the First T2 Due?',
    'Within six months of the first year-end, the same rule that applies to '
    'every later year, and it applies whether or not the corporation traded.'),
  ]),

 dict(slug='schedule-24-first-return-checker',
  title='Schedule 24 First Return Checker | First T2 After Incorporation',
  h1_pre='Schedule 24 ', h1_span='First Return Checker',
  h1='Schedule 24 First Return Checker',
  eyebrow='Schedules Tool', keyword='schedule 24 first return checker',
  meta=('Three questions decide whether your T2 is the corporation&rsquo;s first '
        'return and therefore needs Schedule 24.'),
  tags=['First return after incorporation', 'Three questions',
        'Included in the fee', 'Catch-up years covered'],
  form=tool('Whether this is the corporation&rsquo;s first return',
            [yn(i[0], i[1]) for i in T7_ITEMS],
            'Answer all three and the result appears here.'),
  js=T7_JS,
  sections=[
   ('rule', 'The Rule, Stated Exactly',
    '<p>Schedule 24 is filed with the first T2 after incorporation. It reports '
    'the corporation&rsquo;s first-time filer information, and it belongs on '
    'that return only.</p>\n'
    '<div class="ei-info"><p>First means first ever, not first this year. A '
    'corporation catching up five unfiled years files Schedule 24 with the '
    'oldest of them, because that is the first return.</p></div>'),
   ('catchup', 'Catch-Up Years and the First Return',
    '<p>Where several years are filed together, they are transmitted oldest '
    'first, and Schedule 24 rides with the oldest. The later years do not carry '
    'it.</p>\n'
    '<p>Each of those years is still a separate return at ' + PRICE + '.</p>'),
   ('fee', 'Included in the Fee',
    '<p>Schedule 24 is included in the fee of ' + PRICE + ' where it is '
    'required, alongside GIFI Schedules 100, 125 and 141, Schedule 50 and '
    'Schedule 8. There is no per-schedule charge.</p>'),
  ],
  faq=[
   ('Does First Return Mean First This Year?',
    'No. It means the first T2 the corporation has ever filed. A corporation '
    'catching up several unfiled years files Schedule 24 with the oldest.'),
   ('Does Schedule 24 Go on Every Return?',
    'No. It belongs on the first return only. Once an earlier T2 has been '
    'assessed, Schedule 24 does not go on later ones.'),
   ('Is Schedule 24 Needed on a Nil First Return?',
    'Yes. The schedule reports first-time filer information, not income, so a '
    'nil first return carries it the same as any other first return.'),
   ('Does Schedule 24 Cost Extra?',
    'No. It is included in the fee of ' + PRICE + ' where it is required, and '
    'there is no per-schedule charge.'),
   ('What If the Corporation Was Incorporated Years Ago?',
    'The first return is still the first return. It is filed for the oldest '
    'unfiled tax year, carries Schedule 24, and the later years follow in '
    'order.'),
  ]),

 dict(slug='federal-annual-return-anniversary-calculator',
  title='Federal Annual Return Anniversary Calculator | 60-Day Due Date',
  h1_pre='Federal Annual Return ', h1_span='Anniversary Calculator',
  h1='Federal Annual Return Anniversary Calculator',
  eyebrow='Annual Return Tool',
  keyword='federal annual return anniversary calculator',
  meta=('Enter your federal incorporation date and the calculator returns the '
        'anniversary and the annual return due date 60 days after it.'),
  tags=['Within 60 days of the anniversary', '$12.00 government fee',
        'Corporations Canada, not CRA', 'Separate from your T2'],
  form=tool('Your federal incorporation date',
            [date('inc', 'Date the corporation was incorporated federally')],
            'Enter your federal incorporation date and the annual return due date appears here.'),
  js=T8_JS,
  sections=[
   ('rule', 'The Rule This Applies',
    '<p>A federally incorporated corporation files an annual return with '
    'Corporations Canada within 60 days of the anniversary of incorporation. '
    'The fee is $12.00, and it is a government fee to which HST does not '
    'apply.</p>\n'
    '<div class="ei-warn"><p>This is not a tax return and it is not the T2. It '
    'is a corporate filing with Corporations Canada, and filing one does '
    'nothing for the other.</p></div>'),
   ('separate', 'Two Filings, Two Deadlines',
    '<table class="ei-tbl"><thead><tr><th scope="col">Filing</th>'
    '<th scope="col">Filed with</th><th scope="col">Due</th>'
    '<th scope="col">Fee</th></tr></thead><tbody>\n'
    '<tr><td>T2 corporate income tax return</td><td>Canada Revenue Agency</td>'
    '<td>Within six months of the fiscal year-end</td><td>' + PRICE + '</td></tr>\n'
    '<tr><td>Federal annual return</td><td>Corporations Canada</td>'
    '<td>Within 60 days of the anniversary of incorporation</td>'
    '<td>$12.00, a government fee</td></tr>\n'
    '</tbody></table>\n'
    '<p>The two dates rarely coincide, because one follows the fiscal year-end '
    'and the other follows the incorporation date.</p>'),
   ('covered', 'Not Covered by the Nil T2 Fee',
    '<p>The federal annual return is not covered by the fee of ' + PRICE +
    '. Nor is an Ontario annual return through the Ontario Business Registry, '
    'an Alberta AT1, a Quebec CO-17, or a nil GST/HST or payroll filing. We '
    'tell you which of these you still owe.</p>'),
  ],
  faq=[
   ('Is the Federal Annual Return the Same as the T2?',
    'No. The T2 is a tax return filed with the Canada Revenue Agency within '
    'six months of the fiscal year-end. The annual return is a corporate '
    'filing with Corporations Canada within 60 days of the anniversary of '
    'incorporation.'),
   ('Does HST Apply to the $12.00?',
    'No. The $12.00 is a government fee and HST does not apply to it.'),
   ('Does a Dormant Corporation Still File It?',
    'Yes. The annual return reports that the corporation still exists, so it '
    'is due every year until the corporation is dissolved, whether or not it '
    'traded.'),
   ('Is It Covered by the Nil T2 Fee?',
    'No. The fee of ' + PRICE + ' covers the T2 only. We tell you if the '
    'federal annual return is still outstanding.'),
   ('What If the Corporation Is Provincially Incorporated?',
    'Then there is no federal annual return. The province has its own registry '
    'filing instead, on its own schedule.'),
  ]),

 dict(slug='dormant-corporation-test',
  title='Dormant Corporation Test | Is Your Corporation Nil?',
  h1_pre='Dormant ', h1_span='Corporation Test', h1='Dormant Corporation Test',
  eyebrow='Eligibility Tool', keyword='dormant corporation test',
  meta=('Ten questions decide whether your corporation is nil for the tax year '
        'or has activity that puts it outside a nil return.'),
  tags=['Ten activity questions', 'Names the disqualifying item',
        'Interest counts as income', 'Checked before you pay'],
  form=tool('What the corporation did in the tax year',
            [yn(i[0], i[1]) for i in T9_ITEMS],
            'Answer all ten and the result appears here.'),
  js=T9_JS,
  sections=[
   ('counts', 'What Counts as Activity',
    '<p>No revenue of any kind, no expense claimed, no payroll, no asset bought '
    'or sold, no dividend paid or received, and no inter-company transaction. '
    'Interest credited on a bank balance is income, so a year with interest in '
    'it is not a no-activity year, however small the amount.</p>\n'
    '<div class="ei-info"><p>Share capital, cash, a shareholder loan, an '
    'incorporation cost or a bank charge does not stop the year being nil. It '
    'does make GIFI Schedules 100, 125 and 141 required, and those are included '
    'in the fee.</p></div>'),
   ('not-nil', 'Where the Corporation Is Not Nil',
    '<div class="ei-warn"><p>' + NOT_NIL + '</p></div>\n'
    '<p>Other cases that are not nil include a corporation that is not a '
    'Canadian-controlled private corporation, an amalgamation, or a corporation '
    'already dissolved or struck. We route you to our sister office at '
    'gondaliyacpa.ca at $350.00 plus HST per year before you pay. If we find it '
    'after you pay, we refund you in full.</p>'),
   ('obligation', 'Dormant Does Not Mean Exempt',
    '<p>A dormant corporation files a T2 within six months of each fiscal '
    'year-end, every year, until it is formally dissolved. There is no dormancy '
    'form, no status to elect and no threshold below which the obligation '
    'stops.</p>'),
  ],
  faq=[
   ('Does Bank Interest Make a Year Not Nil?',
    'Yes. Interest credited on a bank balance is income, so a year with '
    'interest in it is not a no-activity year, however small the amount.'),
   ('Is There a Form That Tells CRA a Corporation Is Dormant?',
    'No. There is no dormancy form and no way to pause the T2. The annual '
    'return is the only thing that reports the year, and it reports nil '
    'amounts where there was no activity.'),
   ('Does Share Capital Stop a Year Being Nil?',
    'No. Share capital, cash, a shareholder loan, an incorporation cost or a '
    'bank charge does not stop a year being nil. It does make GIFI Schedules '
    '100, 125 and 141 required, and those are included in the fee.'),
   ('What Happens If the Test Says Not Nil?',
    'We route the work to our sister office at gondaliyacpa.ca at $350.00 plus '
    'HST per year, before you pay. If we find it after you pay, we refund you '
    'in full.'),
   ('Can a Corporation Be Dormant for Many Years?',
    'Yes. There is no limit on consecutive nil years. What causes trouble is a '
    'dormant year left unfiled, not the dormancy itself.'),
  ]),

 dict(slug='gst-hst-nil-filing-checker',
  title='GST/HST Nil Filing Checker | Open Accounts and RC145',
  h1_pre='GST/HST ', h1_span='Nil Filing Checker',
  h1='GST/HST Nil Filing Checker',
  eyebrow='Accounts Tool', keyword='gst hst nil filing checker',
  meta=('Three questions decide whether an open GST/HST or payroll account '
        'still needs nil filings, or whether Form RC145 closes it.'),
  tags=['Open accounts still file', 'Form RC145 closure',
        'Separate from the T2', 'Payroll accounts too'],
  form=tool('Your GST/HST and payroll accounts',
            [yn(i[0], i[1]) for i in T10_ITEMS],
            'Answer all three and the result appears here.'),
  js=T10_JS,
  sections=[
   ('rule', 'An Open Account Files Whether or Not You Trade',
    '<p>An open GST/HST account carries its own filing obligation, and so does '
    'an open payroll account. A corporation that stopped trading but left the '
    'accounts open still owes nil returns on them for every period.</p>\n'
    '<div class="ei-warn"><p>Filing your T2 does nothing for these accounts. '
    'They are separate registrations with separate periods and separate '
    'returns.</p></div>'),
   ('rc145', 'Closing an Account With Form RC145',
    '<p>Form RC145 closes a GST/HST or payroll account. Closing the account '
    'ends the nil filings rather than repeating them every period, which is '
    'usually what a corporation that has stopped trading wants.</p>\n'
    '<p>A corporation that expects to trade again may prefer to keep the '
    'account open and file the nil returns in the meantime.</p>'),
   ('covered', 'Not Covered by the Nil T2 Fee',
    '<p>Neither a nil GST/HST return, a nil payroll return nor an RC145 closure '
    'is covered by the fee of ' + PRICE + '. We tell you which of these you '
    'still owe.</p>'),
  ],
  faq=[
   ('Does Filing a Nil T2 Close a GST/HST Account?',
    'No. They are separate registrations. The T2 is a tax return; the GST/HST '
    'account carries its own filing obligation until it is closed.'),
   ('What Does Form RC145 Do?',
    'It closes a GST/HST or payroll account, which ends the nil filings on it '
    'rather than repeating them every period.'),
   ('Does an Open Payroll Account Need Nil Remittances?',
    'An open payroll account carries its own filing obligation whether or not '
    'wages were paid, until the account is closed.'),
   ('Should a Dormant Corporation Close Its Accounts?',
    'A corporation that does not expect to trade again usually closes them, '
    'since that ends the filings. One that expects to trade again often keeps '
    'them open and files nil returns in the meantime.'),
   ('Is Any of This Covered by the $300.00 Fee?',
    'No. The fee of ' + PRICE + ' covers the nil T2 only. We tell you which '
    'account filings you still owe.'),
  ]),
]

# ---------------------------------------------------------------------------
# Cross-links. 6(g) wants at least three inbound links per URL. The ten tools
# form a link graph in which every tool is linked from at least three others,
# so the batch is compliant before the /tools/ hub exists rather than after.
# ---------------------------------------------------------------------------
ORDER = ['nil-t2-deadline-calculator', 't2-short-eligibility-checker',
         'gifi-schedule-requirement-checker', 'unfiled-years-cost-calculator',
         'schedule-50-shareholder-threshold-checker',
         '53-week-first-tax-year-checker', 'schedule-24-first-return-checker',
         'federal-annual-return-anniversary-calculator',
         'dormant-corporation-test', 'gst-hst-nil-filing-checker']

LINK_TITLE = {
 'nil-t2-deadline-calculator': 'Nil T2 deadline calculator',
 't2-short-eligibility-checker': 'T2 Short eligibility checker, all eight conditions',
 'gifi-schedule-requirement-checker': 'GIFI schedule requirement checker',
 'unfiled-years-cost-calculator': 'Unfiled years cost calculator',
 'schedule-50-shareholder-threshold-checker':
     'Schedule 50 shareholder threshold checker',
 '53-week-first-tax-year-checker': '53-week first tax year checker',
 'schedule-24-first-return-checker': 'Schedule 24 first return checker',
 'federal-annual-return-anniversary-calculator':
     'Federal annual return anniversary calculator',
 'dormant-corporation-test': 'Dormant corporation test',
 'gst-hst-nil-filing-checker': 'GST/HST nil filing checker',
}

SIBLINGS = {3: [4, 5, 6], 4: [5, 6, 7], 5: [3, 6, 7, 8], 6: [7, 8, 9],
            7: [8, 9, 0], 8: [9, 0, 1], 9: [0, 1, 2]}

GUIDES = {
 'unfiled-years-cost-calculator': [
   ('catch-up-unfiled-corporate-tax-returns',
    'The complete guide to catching up unfiled corporate tax returns'),
   ('t2-late-filing-penalties', 'T2 late filing penalties')],
 'schedule-50-shareholder-threshold-checker': [
   ('t2-schedules-on-a-nil-return', 'T2 schedules on a nil return')],
 '53-week-first-tax-year-checker': [
   ('first-year-t2-filing', 'The complete guide to first-year T2 filing')],
 'schedule-24-first-return-checker': [
   ('first-year-t2-filing', 'The complete guide to first-year T2 filing'),
   ('t2-schedules-on-a-nil-return', 'T2 schedules on a nil return')],
 'federal-annual-return-anniversary-calculator': [
   ('provincial-and-federal-annual-returns',
    'Provincial and federal annual returns')],
 'dormant-corporation-test': [
   ('dormant-and-inactive-corporations',
    'The complete guide to dormant and inactive corporations')],
 'gst-hst-nil-filing-checker': [
   ('provincial-and-federal-annual-returns',
    'Provincial and federal annual returns')],
}

for t in TOOLS2:
    i = ORDER.index(t['slug'])
    rel = [(T + ORDER[j] + '/', LINK_TITLE[ORDER[j]]) for j in SIBLINGS[i]]
    rel += [(G + g + '/', ttl) for g, ttl in GUIDES[t['slug']]]
    rel.append((COST, 'Nil T2 filing cost'))
    t['related'] = rel


if __name__ == '__main__':
    recs = []
    for t in TOOLS2:
        html, url = render(t)
        io.open(os.path.join(HERE, t['slug'] + '.html'), 'w',
                encoding='utf-8').write(html)
        recs.append(dict(slug=t['slug'], title=t['title'], h1=t['h1'], url=url,
                         meta_description=t['meta'], meta=meta(t)))
        print('%-46s %6d bytes' % (t['slug'], len(html.encode())))
    json.dump(recs, io.open(os.path.join(HERE, 'f2b-manifest.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
