
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

function whichReturn(a){
  if(a.rev===null||a.inv===null||a.div===null||a.disp===null){return null;}
  var hits=[];
  if(a.rev==='y'){hits.push('revenue or expenses');}
  if(a.inv==='y'){hits.push('investment or rental income');}
  if(a.div==='y'){hits.push('a dividend paid or received');}
  if(a.disp==='y'){hits.push('an asset sold or transferred');}
  return hits;
}

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
var fails=0,n=0;
function eq(label,got,want){n++;
  var g=JSON.stringify(got),w=JSON.stringify(want);
  if(g!==w){fails++;console.log('FAIL '+label+'\n  got  '+g+'\n  want '+w);}}
function D(s){var p=s.split('-');return u(+p[0],+p[1]-1,+p[2]);}
function F(d){return fmt(d);}

// ---- 16 business number status --------------------------------------------
function B(bn,rc,rt,rp){return bnRows({bn:bn,rc:rc,rt:rt,rp:rp});}
function BA(bn,rc,rt,rp){var r=B(bn,rc,rt,rp);return r&&bnActions(r);}
eq('16 incomplete', B('y','y','n',null), null);
eq('16 always four rows', B('y','y','n','n').length, 4);
eq('16 clean case needs nothing', BA('y','y','n','n'), 0);
eq('16 missing BN needs action', BA('n','y','n','n'), 1);
// The bug this replaces: answering no to the income tax account produced no
// item at all, so a corporation with no RC account on record was told there
// was nothing outstanding.
eq('16 a missing income tax account needs action', BA('y','n','n','n'), 1);
eq('16 and is not reported as clear',
   B('y','n','n','n').filter(function(r){return r.k==='rc';})[0].act, true);
eq('16 an open GST/HST account needs action', BA('y','y','y','n'), 1);
eq('16 an open payroll account needs action', BA('y','y','n','y'), 1);
eq('16 worst case is all four', BA('n','n','y','y'), 4);
eq('16 row order is fixed', B('y','y','n','n').map(function(r){return r.k;}),
   ['bn','rc','rt','rp']);

// ---- 17 inactive corporation filings --------------------------------------
function X(f,o,g,p){return extraFilings({fed:f,ont:o,gst:g,pay:p});}
eq('17 incomplete', X('y','y','y',null), null);
eq('17 T2 is always owed', X('n','n','n','n'), ['t2']);
eq('17 federal adds the annual return', X('y','n','n','n'), ['t2','fedar']);
eq('17 everything', X('y','y','y','y'), ['t2','fedar','ontar','gst','pay']);
eq('17 provincial only', X('n','y','n','n'), ['t2','ontar']);
eq('17 T2 is always first', X('y','y','y','y')[0], 't2');

// ---- 18 nil vs full -------------------------------------------------------
function W(r,i,d,s){return whichReturn({rev:r,inv:i,div:d,disp:s});}
eq('18 incomplete', W('y','n','n',null), null);
eq('18 nothing happened is nil', W('n','n','n','n'), []);
eq('18 revenue alone makes it full', W('y','n','n','n'), ['revenue or expenses']);
eq('18 names every trigger', W('y','y','y','y'),
   ['revenue or expenses','investment or rental income',
    'a dividend paid or received','an asset sold or transferred']);
eq('18 a dividend alone is enough', W('n','n','y','n'),
   ['a dividend paid or received']);
eq('18 rental income alone is enough', W('n','y','n','n'),
   ['investment or rental income']);

// ---- 19 document checklist ------------------------------------------------
function C(g,f,s,l){return docList({gifi:g,first:f,share10:s,losses:l});}
eq('19 incomplete', C('y','n','n',null), null);
eq('19 two items always', C('n','n','n','n'), ['id','t183']);
eq('19 GIFI pulls in the three schedules', C('y','n','n','n'),
   ['id','t183','gifi']);
eq('19 a first return adds Schedule 24', C('n','y','n','n'),
   ['id','t183','s24']);
eq('19 a 10% shareholder adds Schedule 50', C('n','n','y','n'),
   ['id','t183','s50']);
eq('19 a carried loss adds Schedule 8', C('n','n','n','y'),
   ['id','t183','s8']);
eq('19 everything, in order', C('y','y','y','y'),
   ['id','t183','gifi','s24','s50','s8']);

// ---- 20 weekend and holiday shift ----------------------------------------
// 2026: Jan 1 is a Thursday. Christmas Day 2026 is a Friday.
eq('20 a plain Tuesday does not move', shiftChain(D('2026-06-30')).length, 0);
eq('20 Dec 25 2026 is Christmas Day',
   shiftChain(D('2026-12-25')).map(function(c){return c.why;}),
   ['Christmas Day','Boxing Day','Sunday']);
eq('20 and lands on the Monday', F(nextBusiness(D('2026-12-25'))),
   'December 28, 2026');
eq('20 a Saturday names the day',
   shiftChain(D('2026-07-04')).map(function(c){return c.why;}),
   ['Saturday','Sunday']);
eq('20 New Year 2027 is a Friday holiday', holidayName(D('2027-01-01')),
   'New Year&rsquo;s Day');
eq('20 Canada Day 2026', holidayName(D('2026-07-01')), 'Canada Day');
eq('20 Good Friday 2026 is April 3', holidayName(D('2026-04-03')),
   'Good Friday');
eq('20 Victoria Day 2026 is May 18', holidayName(D('2026-05-18')),
   'Victoria Day');
eq('20 Thanksgiving 2026 is October 12', holidayName(D('2026-10-12')),
   'Thanksgiving');
eq('20 a working day has no reason', whyClosed(D('2026-06-30')), null);
eq('20 every holiday in a year is named',
   holidays(2026).every(function(h){return holidayName(h)!==null;}), true);
eq('20 the chain always ends on a business day',
   isBusiness(nextBusiness(D('2026-12-25'))), true);

// ---------------------------------------------------------------- drift guard
// The worked-examples table in due-date-weekend-holiday-shift-calculator.html
// is written into the page source by hand. Re-derive every row from the engine
// here, so the table can never quietly disagree with the calculator beside it.
(function(){
  var fs=require('fs');
  var h=fs.readFileSync('due-date-weekend-holiday-shift-calculator.html','utf8');
  // dueDate() is not redefined here on purpose: pull the exact function the
  // deadline calculator ships, so this guard tests shipped code and not a copy
  // of it. Page 20 itself only shifts a date it is given -- the six-month step
  // is the deadline calculator's, and the table spans both.
  var dh=fs.readFileSync('nil-t2-deadline-calculator.html','utf8');
  var m=dh.match(/function dueDate\(ye\)\{[\s\S]*?\n\}/);
  eq('20 dueDate() found in page source', !!m, true);
  if(!m){return;}
  var callDue=function(ye){
    return new Function('ye','u','lastDay', m[0]+'\nreturn dueDate(ye);')
      (ye,u,lastDay);
  };
  var i=h.indexOf('id="worked"');
  eq('20 worked section is present', i>=0, true);
  if(i<0){return;}
  var seg=h.slice(i), t0=seg.indexOf('<tbody>'), t1=seg.indexOf('</tbody>');
  var rows=seg.slice(t0+7,t1).split('</tr>').filter(function(r){
    return r.indexOf('<td>')>=0;});
  eq('20 worked table has 8 rows', rows.length, 8);
  rows.forEach(function(r){
    var c=r.split(/<td>/).slice(1).map(function(x){
      return x.replace(/<\/td>.*$/,'').replace(/&rsquo;/g,'’').trim();});
    var p=c[0].replace(',','').split(' ');
    var ye=u(+p[2], MON.indexOf(p[0]), +p[1]);
    eq('20 worked: '+c[0]+' parses', isNaN(ye.getTime()), false);
    var due=callDue(ye), ch=shiftChain(due);
    eq('20 worked: '+c[0]+' due date', c[1], fmt(due));
    eq('20 worked: '+c[0]+' weekday', c[2], DAY[due.getUTCDay()]);
    eq('20 worked: '+c[0]+' skipped days',
       c[3], ch.map(function(x){return x.why;}).join(', ')
               .replace(/&rsquo;/g,'’'));
    eq('20 worked: '+c[0]+' filing due', c[4], fmt(nextBusiness(due)));
  });
})();


// The 'cases' heading states a row count in words. Assert it matches reality,
// so adding or dropping a row cannot leave the heading lying.
(function(){
  var fs=require('fs');
  var h=fs.readFileSync('nil-return-vs-full-return-checker.html','utf8');
  var WORDS={Ten:10,Eleven:11,Twelve:12,Thirteen:13,Fourteen:14,Fifteen:15,
             Sixteen:16,Seventeen:17,Eighteen:18,Nineteen:19,Twenty:20};
  var m=h.match(/id="cases"[\s\S]{0,200}?<h2[^>]*>([A-Z][a-z]+) Situations/);
  eq('18 cases heading found', !!m, true);
  if(!m){return;}
  var seg=h.slice(h.indexOf('id="cases"'));
  seg=seg.slice(seg.indexOf('<tbody>'), seg.indexOf('</tbody>'));
  var rows=seg.split('</tr>').filter(function(r){return r.indexOf('<td>')>=0;});
  eq('18 cases heading count matches rows', WORDS[m[1]], rows.length);
  var nil=rows.filter(function(r){return /<td>Nil<\/td>/.test(r);}).length;
  var full=rows.filter(function(r){return /<td>Full<\/td>/.test(r);}).length;
  eq('18 every case row is either Nil or Full', nil+full, rows.length);
  eq('18 both outcomes appear', nil>0&&full>0, true);
})();


console.log(fails?('\n'+fails+' of '+n+' assertions FAILED'):
                  ('all '+n+' assertions pass'));
if(fails){process.exit(1);}
