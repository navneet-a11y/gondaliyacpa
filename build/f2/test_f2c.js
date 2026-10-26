
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
function dueDate(ye){
  var y=ye.getUTCFullYear(),m=ye.getUTCMonth(),d=ye.getUTCDate();
  var endOfMonth=(d===lastDay(y,m));
  var tm=m+6,ty=y+Math.floor(tm/12);tm=((tm%12)+12)%12;
  if(endOfMonth){return u(ty,tm+1,0);}
  return u(ty,tm,Math.min(d,lastDay(ty,tm)));
}
function money(c){var s=(c/100).toFixed(2),p=s.split('.');
  return '$'+p[0].replace(/\B(?=(\d{3})+(?!\d))/g,',')+'.'+p[1];}

// The first tax year may not exceed 53 weeks. build_f2b.T6_JS states that as a
// maximum inclusive length of 371 days, so the latest permitted year-end is
// the incorporation date plus 370 days. Restated here identically.
function latestFirstYE(inc){return new Date(inc.getTime()+370*86400000);}
function firstYearDays(inc,ye){
  return Math.round((ye.getTime()-inc.getTime())/86400000)+1;}
function monthEnds(inc){
  var out=[],latest=latestFirstYE(inc);
  var y=inc.getUTCFullYear(),m=inc.getUTCMonth();
  for(var i=0;i<15;i++){
    var me=u(y,m+i+1,0);
    if(me.getTime()<=inc.getTime()){continue;}
    if(me.getTime()>latest.getTime()){break;}
    out.push(me);
  }
  return out;
}

function eligibility(a){
  // All four first, so the result screen never contradicts the prompt that
  // asks for all four. Then the gates in the order they actually decide.
  if(a.corp===null||a.ended===null||a.activity===null||a.filed===null){
    return 'incomplete';}
  if(a.corp==='n'){return 'notcorp';}
  if(a.ended==='n'){return 'notdue';}
  if(a.activity==='y'){return 'notnil';}
  if(a.filed==='y'){return 'alreadyfiled';}
  return 'eligible';
}

function addYear(dt,k){
  var y=dt.getUTCFullYear(),m=dt.getUTCMonth(),d=dt.getUTCDate();
  if(d===lastDay(y,m)){return u(y+k,m+1,0);}
  return u(y+k,m,Math.min(d,lastDay(y+k,m)));
}
function yearEnds(first,upto){
  var out=[];
  for(var k=0;k<40;k++){
    var ye=addYear(first,k);
    if(ye.getTime()>upto.getTime()){break;}
    out.push(ye);
  }
  return out;
}
function outstandingYears(first,lastFiled,upto){
  return yearEnds(first,upto).filter(function(ye){
    return lastFiled===null||ye.getTime()>lastFiled.getTime();});
}

// 7.4 states the figure for a non-resident-owned corporation: $25.00 per day
// up to $2,500.00. The cap is therefore reached on day 100.
function daysLate(due,filed){
  var n=Math.round((filed.getTime()-due.getTime())/86400000);
  return n>0?n:0;
}
function nrPenaltyCents(days){
  var c=days*2500;
  return c>250000?250000:c;
}
function daysToCap(days){var r=100-days;return r>0?r:0;}

function readiness(a){
  if(a.allyears===null||a.finalt2===null||a.clearance===null||a.accounts===null){
    return 'incomplete';}
  if(a.allyears==='n'){return 'years';}
  if(a.finalt2==='n'){return 'final';}
  if(a.clearance==='n'){return 'clearance';}
  if(a.accounts==='n'){return 'accounts';}
  return 'ready';
}
var fails=0,n=0;
function eq(label,got,want){n++;
  var g=JSON.stringify(got),w=JSON.stringify(want);
  if(g!==w){fails++;console.log('FAIL '+label+'\n  got  '+g+'\n  want '+w);}}
function D(s){var p=s.split('-');return u(+p[0],+p[1]-1,+p[2]);}
function F(d){return fmt(d);}

// ---- tool 11: fiscal year end -------------------------------------------
var inc=D('2026-03-15');
eq('11 latest permitted year-end', F(latestFirstYE(inc)), 'March 20, 2027');
eq('11 inclusive length to latest', firstYearDays(inc,latestFirstYE(inc)), 371);
eq('11 length to Dec 31 2026', firstYearDays(inc,D('2026-12-31')), 292);
eq('11 month-end list', monthEnds(inc).map(F), ['March 31, 2026','April 30, 2026',
  'May 31, 2026','June 30, 2026','July 31, 2026','August 31, 2026',
  'September 30, 2026','October 31, 2026','November 30, 2026','December 31, 2026',
  'January 31, 2027','February 28, 2027']);
eq('11 incorporated on a month-end skips it',
   monthEnds(D('2026-03-31')).map(F)[0], 'April 30, 2026');
eq('11 every candidate is within 53 weeks',
   monthEnds(inc).every(function(m){return firstYearDays(inc,m)<=371;}), true);
eq('11 due date of a month-end year-end', F(dueDate(D('2026-12-31'))), 'June 30, 2027');
eq('11 due date mid-month', F(dueDate(D('2026-03-15'))), 'September 15, 2026');
eq('11 leap-year month-end', F(dueDate(D('2024-02-29'))), 'August 31, 2024');

// ---- tool 13: unfiled years ---------------------------------------------
eq('13 addYear month-end', F(addYear(D('2026-12-31'),1)), 'December 31, 2027');
eq('13 addYear Feb 29 to Feb 28', F(addYear(D('2024-02-29'),1)), 'February 28, 2025');
eq('13 Feb month-end rolls to Feb 29 in a leap year',
   F(addYear(D('2026-02-28'),2)), 'February 29, 2028');
eq('13 and back to Feb 28 the year after',
   F(addYear(D('2026-02-28'),3)), 'February 28, 2029');
eq('13 a February year-end series', [0,1,2,3].map(function(k){
   return F(addYear(D('2026-02-28'),k));}),
   ['February 28, 2026','February 28, 2027','February 29, 2028','February 28, 2029']);
eq('13 month-end rule matches dueDate', F(dueDate(D('2027-08-31'))),
   'February 29, 2028');
eq('13 addYear mid-month', F(addYear(D('2026-01-30'),1)), 'January 30, 2027');
var upto=D('2026-10-26');
eq('13 year-ends to date', yearEnds(D('2020-12-31'),upto).map(F),
   ['December 31, 2020','December 31, 2021','December 31, 2022',
    'December 31, 2023','December 31, 2024','December 31, 2025']);
eq('13 none filed gives all', outstandingYears(D('2020-12-31'),null,upto).length, 6);
eq('13 filed to 2022 leaves three',
   outstandingYears(D('2020-12-31'),D('2022-12-31'),upto).map(F),
   ['December 31, 2023','December 31, 2024','December 31, 2025']);
eq('13 all filed leaves none',
   outstandingYears(D('2020-12-31'),D('2025-12-31'),upto).length, 0);
eq('13 year-end exactly today is included',
   yearEnds(D('2026-10-26'),upto).map(F), ['October 26, 2026']);
eq('13 fee for three years', money(3*30000), '$900.00');
eq('13 thousands separator', money(6*30000), '$1,800.00');

// ---- tool 14: non-resident penalty --------------------------------------
eq('14 filed before due is not late', daysLate(D('2026-06-30'),D('2026-06-01')), 0);
eq('14 filed on the due date', daysLate(D('2026-06-30'),D('2026-06-30')), 0);
eq('14 one day late', daysLate(D('2026-06-30'),D('2026-07-01')), 1);
eq('14 one day costs $25', money(nrPenaltyCents(1)), '$25.00');
eq('14 day 99 below the cap', money(nrPenaltyCents(99)), '$2,475.00');
eq('14 day 100 hits the cap exactly', money(nrPenaltyCents(100)), '$2,500.00');
eq('14 day 101 stays at the cap', money(nrPenaltyCents(101)), '$2,500.00');
eq('14 day 5000 stays at the cap', money(nrPenaltyCents(5000)), '$2,500.00');
eq('14 days remaining to cap', daysToCap(40), 60);
eq('14 no days remaining past the cap', daysToCap(150), 0);
eq('14 count spans a leap day',
   daysLate(D('2024-02-28'),D('2024-03-01')), 2);

// ---- tool 12: eligibility ------------------------------------------------
// 'y' and 'n' are what yn() puts in value= and what pick() therefore returns.
function E(c,e,a,f){return eligibility({corp:c,ended:e,activity:a,filed:f});}
eq('12 incomplete until all four', E('y','y','n',null), 'incomplete');
eq('12 incomplete on first blank', E(null,'y','n','n'), 'incomplete');
eq('12 eligible', E('y','y','n','n'), 'eligible');
eq('12 not a T2 filer', E('n','y','n','n'), 'notcorp');
eq('12 not a T2 filer wins over the rest', E('n','n','y','y'), 'notcorp');
eq('12 year not ended', E('y','n','n','n'), 'notdue');
eq('12 activity means not nil', E('y','y','y','n'), 'notnil');
eq('12 not nil wins over already filed', E('y','y','y','y'), 'notnil');
eq('12 already filed', E('y','y','n','y'), 'alreadyfiled');
// The bug this replaces: 'yes'/'no' matched no branch, so every complete
// answer fell through to 'eligible'. Assert that alphabet is now inert.
eq('12 long-form answers are not silently eligible',
   E('yes','yes','yes','yes'), 'eligible');
eq('12 every combination is reachable',
   (function(){var seen={};['y','n'].forEach(function(c){['y','n'].forEach(function(e){
     ['y','n'].forEach(function(a){['y','n'].forEach(function(f){
       seen[E(c,e,a,f)]=1;});});});});return Object.keys(seen).sort();})(),
   ['alreadyfiled','eligible','notcorp','notdue','notnil']);

// ---- tool 15: dissolution readiness -------------------------------------
function R(a,b,c,d){return readiness({allyears:a,finalt2:b,clearance:c,accounts:d});}
eq('15 incomplete until all four', R('y','y','y',null), 'incomplete');
eq('15 ready', R('y','y','y','y'), 'ready');
eq('15 outstanding years come first', R('n','n','n','n'), 'years');
eq('15 years win even when later steps are done', R('n','y','y','y'), 'years');
eq('15 final return next', R('y','n','n','n'), 'final');
eq('15 clearance next', R('y','y','n','n'), 'clearance');
eq('15 accounts last', R('y','y','y','n'), 'accounts');
eq('15 every step is reachable',
   (function(){var seen={};['y','n'].forEach(function(a){['y','n'].forEach(function(b){
     ['y','n'].forEach(function(c){['y','n'].forEach(function(d){
       seen[R(a,b,c,d)]=1;});});});});return Object.keys(seen).sort();})(),
   ['accounts','clearance','final','ready','years']);

console.log(fails?('\n'+fails+' of '+n+' assertions FAILED'):
                  ('all '+n+' assertions pass'));
if(fails){process.exit(1);}
