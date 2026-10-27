// Assertions for Family 2 tools 21 to 30.
//
// The functions under test are not copied in here. They are lifted out of the
// built pages at run time: everything a page's script defines before the line
// that first touches the DOM is pure logic, so that prefix evaluates on its
// own and what gets tested is the code the page actually ships.
var fs = require('fs');

var MON=['January','February','March','April','May','June','July','August',
         'September','October','November','December'];
var DAY=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];

function logicOf(slug, names){
  var h=fs.readFileSync(slug+'.html','utf8');
  var i=h.lastIndexOf('var PRICE_JS=');
  var j=h.indexOf("var out=document.getElementById", i);
  if(i<0||j<0||j<i){throw new Error('cannot locate logic prefix in '+slug);}
  var src=h.slice(i,j);
  return new Function(src+'\nreturn {'+
    names.map(function(n){return n+':'+n;}).join(',')+'};')();
}

var n=0,fails=0;
function eq(label,got,want){n++;
  var g=JSON.stringify(got),w=JSON.stringify(want);
  if(g!==w){fails++;console.log('FAIL '+label+'\n  got  '+g+'\n  want '+w);}}
function D(s){var p=s.split('-');return new Date(Date.UTC(+p[0],+p[1]-1,+p[2]));}

// ------------------------------------------------------------------- shared
var S=logicOf('days-overdue-calculator',
  ['fmt','dueDate','addYear','spanDays','filingDate','dayAfter','dayBefore',
   'plural','isBusiness','isHoliday','nextBusiness','businessBetween',
   'overdueBy']);

eq('shared spanDays is inclusive', S.spanDays(D('2026-01-01'),D('2026-01-01')), 1);
eq('shared spanDays Jan', S.spanDays(D('2026-01-01'),D('2026-01-31')), 31);
eq('shared dayAfter', S.fmt(S.dayAfter(D('2026-12-31'))), 'January 1, 2027');
eq('shared dayBefore', S.fmt(S.dayBefore(D('2027-01-01'))), 'December 31, 2026');
eq('shared plural singular', S.plural(1,'day'), '1 day');
eq('shared plural plural', S.plural(2,'day'), '2 days');
eq('shared plural zero', S.plural(0,'day'), '0 days');

// addYear steps a month-end to a month-end: February 28 in a common year
// becomes February 29 in a leap year, which is the same rule dueDate uses.
eq('shared addYear common-year month-end', S.fmt(S.addYear(D('2026-02-28'),1)),
   'February 28, 2027');
eq('shared addYear 2027->2028 Feb', S.fmt(S.addYear(D('2027-02-28'),1)),
   'February 29, 2028');
eq('shared addYear back one', S.fmt(S.addYear(D('2028-02-29'),-1)),
   'February 28, 2027');
eq('shared addYear mid-month', S.fmt(S.addYear(D('2026-06-15'),1)),
   'June 15, 2027');

// filingDate is dueDate with the weekend and holiday shift applied.
eq('shared filingDate no shift', S.fmt(S.filingDate(D('2026-06-30'))),
   'December 31, 2026');
eq('shared filingDate Family Day chain', S.fmt(S.filingDate(D('2027-08-20'))),
   'February 22, 2028');
eq('shared filingDate Christmas chain', S.fmt(S.filingDate(D('2028-06-23'))),
   'December 27, 2028');

// ------------------------------------------------- 22. days overdue
var NOW=D('2026-10-27');
eq('22 null until a date is entered', S.overdueBy(null,NOW), null);
eq('22 unreadable date', S.overdueBy(undefined,NOW).err, 'read');
(function(){
  // June 30, 2026 was due December 31, 2026, which is after NOW.
  var r=S.overdueBy(D('2026-06-30'),NOW);
  eq('22 not yet due', r.late, false);
  eq('22 due date', S.fmt(r.due), 'December 31, 2026');
  eq('22 calendar days remaining', r.cal, 65);
  eq('22 business days remaining fewer than calendar', r.biz < r.cal, true);
})();
(function(){
  // December 31, 2024 was due June 30, 2025, long past.
  var r=S.overdueBy(D('2024-12-31'),NOW);
  eq('22 overdue', r.late, true);
  eq('22 overdue due date', S.fmt(r.due), 'June 30, 2025');
  eq('22 overdue calendar days', r.cal, 484);
  eq('22 overdue business days fewer', r.biz < r.cal, true);
  eq('22 business days are roughly five sevenths',
     r.biz > r.cal * 0.65 && r.biz < r.cal * 0.75, true);
})();
(function(){
  // A year-end whose due date is today exactly is not overdue.
  var r=S.overdueBy(D('2026-04-27'),NOW);
  eq('22 due today is not overdue', r.late, false);
  eq('22 due today is today', S.fmt(r.due), 'October 27, 2026');
  eq('22 due today has zero days remaining', r.cal, 0);
})();

// ----------------------------------- 21. tax years since incorporation
var A=logicOf('tax-years-since-incorporation-calculator',['taxYears','fmt']);
eq('21 null until both dates', A.taxYears(null,D('2026-12-31'),NOW), null);
eq('21 unreadable', A.taxYears(undefined,D('2026-12-31'),NOW).err, 'read');
eq('21 year-end before incorporation is refused',
   A.taxYears(D('2026-06-01'),D('2026-01-31'),NOW).err, 'order');
eq('21 same day is refused',
   A.taxYears(D('2026-06-01'),D('2026-06-01'),NOW).err, 'order');
(function(){
  // Incorporated March 12, 2020, first year-end December 31, 2020.
  // Years ended: 2020,2021,2022,2023,2024,2025 = 6. The 2026 year-end has
  // not arrived as at October 27, 2026.
  var r=A.taxYears(D('2020-03-12'),D('2020-12-31'),NOW);
  eq('21 six tax years ended', r.rows.length, 6);
  eq('21 first year length', r.first, 295);
  eq('21 first year within 53 weeks', r.over53, false);
  eq('21 earliest year', A.fmt(r.rows[0].ye), 'December 31, 2020');
  eq('21 earliest due', A.fmt(r.rows[0].due), 'June 30, 2021');
  eq('21 latest ended year', A.fmt(r.rows[5].ye), 'December 31, 2025');
  eq('21 latest ended due', A.fmt(r.rows[5].due), 'June 30, 2026');
  eq('21 all six overdue', r.late, 6);
  eq('21 next year-end is the one in progress',
     A.fmt(r.next.ye), 'December 31, 2026');
  eq('21 next due', A.fmt(r.next.due), 'June 30, 2027');
})();
(function(){
  // A first year longer than 53 weeks is flagged, not refused.
  var r=A.taxYears(D('2025-01-01'),D('2026-03-31'),NOW);
  eq('21 over 53 weeks flagged', r.over53, true);
  eq('21 over 53 weeks length', r.first, 455);
  eq('21 still lists the year', r.rows.length, 1);
})();
(function(){
  // A year-end that has passed but whose return is not yet due counts as a
  // year ended and as not overdue.
  var r=A.taxYears(D('2026-01-01'),D('2026-06-30'),NOW);
  eq('21 one year ended', r.rows.length, 1);
  eq('21 not yet overdue', r.late, 0);
  eq('21 due in the future', A.fmt(r.rows[0].due), 'December 31, 2026');
})();
// ----------------------------------------------- 23. next T2 due date
var N=logicOf('next-t2-due-date-checker',['nextDue','fmt']);
eq('23 null until a date', N.nextDue(null,NOW), null);
eq('23 unreadable', N.nextDue(undefined,NOW).err, 'read');
(function(){
  // The whole point of this tool. A June 30 year-end asked on October 27,
  // 2026 has December 31, 2026 next -- belonging to the year that ENDED in
  // June 2026, not the June 2027 year-end still to come.
  var r=N.nextDue(D('2026-06-30'),NOW);
  eq('23 next due is the past year-end\'s', N.fmt(r.due), 'December 31, 2026');
  eq('23 for the year ended June 2026', N.fmt(r.ye), 'June 30, 2026');
  eq('23 that year has ended so it can be filed now', r.ended, true);
})();
(function(){
  // Asked in February 2027 the same corporation has the June 2027 year-end,
  // whose return is not due until December 2027, and nothing can be filed.
  var r=N.nextDue(D('2026-06-30'),D('2027-02-15'));
  eq('23 February: next due', N.fmt(r.due), 'December 31, 2027');
  eq('23 February: for the year ending June 2027', N.fmt(r.ye), 'June 30, 2027');
  eq('23 February: year not ended, cannot file', r.ended, false);
})();
(function(){
  // Any past year-end establishes the month and day and gives the same answer.
  var a=N.nextDue(D('2019-06-30'),NOW), b=N.nextDue(D('2026-06-30'),NOW);
  eq('23 a year-end from years ago gives the same answer',
     N.fmt(a.due), N.fmt(b.due));
})();
(function(){
  // A future year-end is walked back, not forward past the answer.
  var r=N.nextDue(D('2030-06-30'),NOW);
  eq('23 future year-end still answers from today',
     N.fmt(r.due), 'December 31, 2026');
})();
(function(){
  // The returned date is never in the past.
  ['2026-01-31','2026-03-31','2026-06-30','2026-09-30','2026-12-31',
   '2026-02-28','2026-11-15'].forEach(function(s){
    var r=N.nextDue(D(s),NOW);
    eq('23 '+s+' next due is not in the past',
       r.due.getTime()>=NOW.getTime(), true);
  });
})();

// ------------------------------------------- 24. final T2 return due date
var F=logicOf('final-t2-return-due-date-calculator',['finalReturn','fmt']);
eq('24 null until both dates', F.finalReturn(null,D('2027-03-15')), null);
eq('24 unreadable', F.finalReturn(undefined,D('2027-03-15')).err, 'read');
eq('24 dissolution before year-end is refused',
   F.finalReturn(D('2027-06-30'),D('2027-03-15')).err, 'order');
eq('24 dissolution on the year-end is refused',
   F.finalReturn(D('2027-03-15'),D('2027-03-15')).err, 'order');
(function(){
  // The worked example on the page: December 31, 2026 year-end, dissolved
  // March 15, 2027.
  var r=F.finalReturn(D('2026-12-31'),D('2027-03-15'));
  eq('24 final period starts the day after', F.fmt(r.start), 'January 1, 2027');
  eq('24 final period ends on dissolution', F.fmt(r.end), 'March 15, 2027');
  eq('24 final period length', r.days, 74);
  eq('24 short final year flagged', r.stub, true);
  eq('24 final T2 due', F.fmt(r.due), 'September 15, 2027');
  // Dissolving mid-year brings the last filing date FORWARD: the final T2 is
  // due September 15, 2027, where carrying on to the next ordinary year-end
  // of December 31, 2027 would not have fallen due until June 30, 2028.
  eq('24 the ordinary year would have been due',
     F.fmt(r.wouldHave), 'June 30, 2028');
  eq('24 dissolution pulls the filing date earlier',
     r.due.getTime() < r.wouldHave.getTime(), true);
})();
(function(){
  // Dissolution a full year and a day after the year-end is not a stub.
  var r=F.finalReturn(D('2026-12-31'),D('2027-12-31'));
  eq('24 full-length final year is not a stub', r.stub, false);
  eq('24 full-length final year length', r.days, 365);
})();

// --------------------------------------------- 25. amalgamation T2 due date
var M=logicOf('amalgamation-t2-due-date-calculator',['amalgDates','fmt']);
eq('25 null until both dates', M.amalgDates(null,D('2027-07-01')), null);
eq('25 amalgamation before year-end is refused',
   M.amalgDates(D('2027-06-30'),D('2027-01-01')).err, 'order');
eq('25 amalgamation the day after the year-end leaves no period',
   M.amalgDates(D('2027-06-30'),D('2027-07-01')).err, 'sameday');
(function(){
  // Predecessor A on the page: December 31 year-end, amalgamating July 1.
  var r=M.amalgDates(D('2026-12-31'),D('2027-07-01'));
  eq('25 A period starts', M.fmt(r.pStart), 'January 1, 2027');
  // The off-by-one that is the reason the tool exists.
  eq('25 A period ends the DAY BEFORE the amalgamation',
     M.fmt(r.pEnd), 'June 30, 2027');
  eq('25 A period length', r.pDays, 181);
  eq('25 A final return due', M.fmt(r.pDue), 'December 31, 2027');
  eq('25 new corporation begins ON the amalgamation date',
     M.fmt(r.nStart), 'July 1, 2027');
  eq('25 latest first year-end is 370 days later',
     M.fmt(r.nLatest), 'July 5, 2028');
})();
(function(){
  // Predecessor B, a different year-end, same amalgamation: a shorter period
  // but the same due date, which is what the page's table claims.
  var a=M.amalgDates(D('2026-12-31'),D('2027-07-01'));
  var b=M.amalgDates(D('2027-03-31'),D('2027-07-01'));
  eq('25 B period length', b.pDays, 91);
  eq('25 B ends the same day as A', M.fmt(b.pEnd), M.fmt(a.pEnd));
  eq('25 B falls due the same day as A', M.fmt(b.pDue), M.fmt(a.pDue));
  eq('25 the periods are different lengths', a.pDays === b.pDays, false);
})();

// ------------------------------------------- 26. short tax year deadline
var H=logicOf('short-tax-year-deadline-calculator',['shortYear','fmt']);
eq('26 null until both dates', H.shortYear(null,D('2026-12-31')), null);
eq('26 end before start is refused',
   H.shortYear(D('2026-12-31'),D('2026-01-01')).err, 'order');
(function(){
  // Every row of the page's four-row table, re-derived.
  var rows=[['2026-03-12','2026-12-31',295,'June 30, 2027'],
            ['2027-01-01','2027-03-31', 90,'September 30, 2027'],
            ['2027-04-01','2027-08-20',142,'February 22, 2028'],
            ['2027-01-01','2027-06-30',181,'December 31, 2027']];
  rows.forEach(function(w){
    var r=H.shortYear(D(w[0]),D(w[1]));
    eq('26 '+w[0]+' length', r.days, w[2]);
    eq('26 '+w[0]+' due', H.fmt(r.due), w[3]);
    eq('26 '+w[0]+' is short', r.short, true);
  });
})();
(function(){
  // A full year is not flagged short, and a first year over 53 weeks is.
  var full=H.shortYear(D('2026-01-01'),D('2026-12-31'));
  eq('26 full year length', full.days, 365);
  eq('26 full year not short', full.short, false);
  eq('26 full year not over 53 weeks', full.over53, false);
  var over=H.shortYear(D('2025-01-01'),D('2026-03-31'));
  eq('26 455 days is over 53 weeks', over.over53, true);
  eq('26 exactly 371 days is not over', H.shortYear(
     D('2026-01-01'),D('2027-01-06')).over53, false);
  eq('26 372 days is over', H.shortYear(
     D('2026-01-01'),D('2027-01-07')).over53, true);
  eq('26 weeks and remainder', [full.weeks,full.rem], [52,1]);
})();

// --------------------------------------- 27. nil return late penalty
var P=logicOf('nil-return-late-penalty-checker',['latePenalty']);
eq('27 null until all three', P.latePenalty({nil:'y',nr:'y',dem:null}), null);
eq('27 null on first unanswered', P.latePenalty({nil:null,nr:'y',dem:'y'}), null);
// The alphabet the form emits is y and n. Every combination must resolve.
['y','n'].forEach(function(a){['y','n'].forEach(function(b){
  ['y','n'].forEach(function(c){
    var r=P.latePenalty({nil:a,nr:b,dem:c});
    eq('27 '+a+b+c+' resolves', r!==null && r!==undefined, true);
    eq('27 '+a+b+c+' truly', r.truly, a==='y');
    eq('27 '+a+b+c+' nonres', r.nonres, b==='y');
    eq('27 '+a+b+c+' demand', r.demand, c==='y');
  });});});

// ----------------------------------- 28. clearance certificate requirement
var C=logicOf('clearance-certificate-requirement-checker',['clearance']);
eq('28 null until all three', C.clearance({dist:'y',dis:'y',unf:null}), null);
eq('28 distribution alone wants one',
   C.clearance({dist:'y',dis:'n',unf:'n'}).wanted, true);
eq('28 dissolution alone wants one',
   C.clearance({dist:'n',dis:'y',unf:'n'}).wanted, true);
eq('28 neither does not',
   C.clearance({dist:'n',dis:'n',unf:'n'}).wanted, false);
eq('28 an unfiled year is still reported when nothing is wanted',
   C.clearance({dist:'n',dis:'n',unf:'y'}).unf, true);
['y','n'].forEach(function(a){['y','n'].forEach(function(b){
  ['y','n'].forEach(function(c){
    var r=C.clearance({dist:a,dis:b,unf:c});
    eq('28 '+a+b+c+' resolves', r!==null && r!==undefined, true);
  });});});

// --------------------------------------- 29. payroll nil remittance
var Y=logicOf('payroll-nil-remittance-checker',['payroll']);
eq('29 null until all three', Y.payroll({acct:'y',wag:'y',clo:null}), null);
eq('29 no account', Y.payroll({acct:'n',wag:'n',clo:'n'}).kind, 'none');
eq('29 no account ignores the other answers',
   Y.payroll({acct:'n',wag:'y',clo:'y'}).kind, 'none');
eq('29 wages paid is active', Y.payroll({acct:'y',wag:'y',clo:'n'}).kind,
   'active');
eq('29 open with no wages is nil', Y.payroll({acct:'y',wag:'n',clo:'n'}).kind,
   'nil');
eq('29 closing intent carried', Y.payroll({acct:'y',wag:'n',clo:'y'}).close,
   true);
(function(){
  var kinds={};
  ['y','n'].forEach(function(a){['y','n'].forEach(function(b){
    ['y','n'].forEach(function(c){
      var r=Y.payroll({acct:a,wag:b,clo:c});
      eq('29 '+a+b+c+' resolves', r!==null && r!==undefined, true);
      kinds[r.kind]=1;
    });});});
  eq('29 all three outcomes are reachable',
     Object.keys(kinds).sort(), ['active','nil','none']);
})();

// ------------------------------------- 30. GST/HST account closure
var Q=logicOf('gst-hst-account-closure-checker',['gstClose']);
eq('30 null until all three', Q.gstClose({acct:'y',sales:'y',fin:null}), null);
eq('30 no account', Q.gstClose({acct:'n',sales:'n',fin:'n'}).kind, 'none');
eq('30 still trading', Q.gstClose({acct:'y',sales:'y',fin:'y'}).kind,
   'trading');
eq('30 trading outranks a filed final return',
   Q.gstClose({acct:'y',sales:'y',fin:'y'}).kind, 'trading');
eq('30 returns outstanding', Q.gstClose({acct:'y',sales:'n',fin:'n'}).kind,
   'returns');
eq('30 ready to close', Q.gstClose({acct:'y',sales:'n',fin:'y'}).kind,
   'ready');
(function(){
  var kinds={};
  ['y','n'].forEach(function(a){['y','n'].forEach(function(b){
    ['y','n'].forEach(function(c){
      var r=Q.gstClose({acct:a,sales:b,fin:c});
      eq('30 '+a+b+c+' resolves', r!==null && r!==undefined, true);
      kinds[r.kind]=1;
    });});});
  eq('30 all four outcomes are reachable',
     Object.keys(kinds).sort(), ['none','ready','returns','trading']);
})();

console.log(fails?("\n"+fails+" of "+n+" assertions FAILED"):("all "+n+" assertions pass"));if(fails){process.exit(1);}
