// Renders every batch 7 result screen by executing each page's shipped module
// in a DOM stub, then asserts on the text a visitor would actually read.
//
// Why this exists. The node suites test the logic functions and the gate tests
// the wording, and batch 5 still shipped a tool that drew a table with headers
// and no rows, because nothing had ever rendered a result screen. The stub used
// then could not do it either: the page calls show() from an event listener, and
// a stub whose addEventListener is a no-op never fires one. This one reaches into
// the closure and calls show() directly.
const fs = require('fs');
let pass = 0, fail = 0;

function render(slug, vals) {
  const html = fs.readFileSync(slug + '.html', 'utf8');
  const i = html.lastIndexOf('<script>'), j = html.indexOf('</script>', i);
  let src = html.slice(i + 8, j);
  // Expose show() so it can be called without an event.
  src = src.replace(/\}\)\(\);\s*$/, 'globalThis.__show=show;})();');
  if (!/__show/.test(src)) throw new Error(slug + ': could not reach show()');

  const els = {}, out = { className: '', innerHTML: '' };
  Object.keys(vals).forEach(function (id) {
    els[id] = { id: id, value: String(vals[id]), className: '', innerHTML: '',
                addEventListener: function () {} };
  });
  global.document = {
    getElementById: function (id) {
      if (id === 'out') return out;
      if (!(id in els)) return null;      // the real DOM returns null
      return els[id];
    },
    querySelector: function (sel) {
      const m = /name="([^"]+)"/.exec(sel || '');
      if (m && vals[m[1]] !== undefined) return { value: String(vals[m[1]]) };
      return null;
    },
    querySelectorAll: function () { return []; }
  };
  global.window = global;
  new Function(src)();
  globalThis.__show();
  return out.innerHTML;
}

function text(h) {
  return h.replace(/<\/t[dh]>/g, ' | ').replace(/<[^>]+>/g, ' ')
          .replace(/&#8217;/g, "'").replace(/&#8212;/g, '-')
          .replace(/\s+/g, ' ').trim();
}

function check(slug, vals, want, notWant) {
  let t;
  try { t = text(render(slug, vals)); }
  catch (e) { console.log('THREW  ' + slug + ' ' + JSON.stringify(vals) + ': ' + e.message); fail++; return; }
  let ok = true;
  (want || []).forEach(function (w) {
    if (t.indexOf(w) === -1) { console.log('MISSING ' + slug + ' ' + JSON.stringify(vals) + '\n  want: ' + w + '\n  got:  ' + t.slice(0, 260)); ok = false; }
  });
  (notWant || []).forEach(function (w) {
    if (t.indexOf(w) !== -1) { console.log('PRESENT ' + slug + ' ' + JSON.stringify(vals) + '\n  must not contain: ' + w); ok = false; }
  });
  // No result screen may ship an empty table, an undefined, or a NaN.
  ['undefined', 'NaN', 'null'].forEach(function (w) {
    if (t.indexOf(w) !== -1) { console.log('BAD TOKEN ' + slug + ' ' + JSON.stringify(vals) + ': ' + w + '\n  ' + t.slice(0, 260)); ok = false; }
  });
  const h = render(slug, vals);
  if (/<tbody>\s*<\/tbody>/.test(h)) {
    console.log('EMPTY TABLE ' + slug + ' ' + JSON.stringify(vals)); ok = false;
  }
  if (ok) pass++; else fail++;
}


// Every date asserted below was computed independently in Python against the
// same nine Ontario holidays before it was written here. Where a page and my
// expectation disagreed, the page was checked first.

// ---- 41 first year-end options -------------------------------------------
// 371 days from 2026-03-15 inclusive ends 2027-03-20, so the last month-end
// inside the limit is 2027-02-28: twelve rows, March 2026 through Feb 2027.
check('first-t2-year-end-options-generator', { inc: '2026-03-15' },
  ['12 month-ends available', 'March 31, 2026 | 17 days | September 30, 2026',
   'February 28, 2027 | 351 days | August 31, 2027',
   'does not have to be a month-end']);
// Incorporated ON a month-end: that month-end is not offered, because a
// one-day first tax year ending the day you incorporated is not a choice
// anyone is making, and spanDays would read it as day one.
check('first-t2-year-end-options-generator', { inc: '2026-03-31' },
  ['April 30, 2026'], ['March 31, 2026 | 1 day']);
check('first-t2-year-end-options-generator', { inc: '' },
  ['Enter the date of incorporation']);

// ---- 42 year-end change --------------------------------------------------
// Jan 1 to Jun 30 2027 is 181 days; six months on from a month-end lands on
// Dec 31 2027. The following year ends Jun 30 2028, whose Dec 31 2028 due
// date is a Sunday and whose Jan 1 is New Year's Day, so it moves to Jan 2.
check('year-end-change-impact-calculator',
  { cur: '2026-12-31', new: '2027-06-30' },
  ['creates a period of 181 days', 'December 31, 2027', 'June 30, 2028', 'January 2, 2029',
   'short year does not get a short deadline', 'written approval']);
check('year-end-change-impact-calculator',
  { cur: '2026-12-31', new: '2028-06-30' },
  ['does not produce a single tax year', '547 days', 'intervening year-end']);
check('year-end-change-impact-calculator',
  { cur: '2027-06-30', new: '2026-12-31' },
  ['has to fall after']);
check('year-end-change-impact-calculator', { cur: '', new: '' },
  ['Enter the year-end on record']);

// ---- 43 two returns in one year -----------------------------------------
// Jan 31 2026 is due Jul 31 2026; Mar 31 2026 is due Sep 30 2026. Both in
// 2026, 61 days apart, which is inside the tight threshold of 92.
check('two-t2-returns-in-one-year-checker',
  { y1: '2026-01-31', y2: '2026-03-31' },
  ['Both deadlines fall in 2026', 'July 31, 2026', 'September 30, 2026',
   '61', '$600.00 plus HST', '61 days apart']);
check('two-t2-returns-in-one-year-checker',
  { y1: '2025-12-31', y2: '2026-12-31' },
  ['different calendar years', 'June 30, 2026', 'June 30, 2027'],
  ['days apart, which is the part']);
check('two-t2-returns-in-one-year-checker',
  { y1: '2026-12-31', y2: '2026-01-31' }, ['has to fall after the first']);

// ---- 44 mandatory e-filing ----------------------------------------------
check('mandatory-t2-efile-checker', { st: '2024-01-01' },
  ['is mandatory for a tax year beginning January 1, 2024', 'Yes',
   'registered EFILE electronic filer']);
// A year that BEGAN in Dec 2023 and ran into 2024 began before the rule.
check('mandatory-t2-efile-checker', { st: '2023-12-01' },
  ['was not mandatory', 'paper was an option', 'catch-up']);
check('mandatory-t2-efile-checker', { st: '' },
  ['Enter the first day of the tax year']);

// ---- 45 business days ----------------------------------------------------
// Dec 24 2026 to Jan 4 2027 is 12 calendar days: 6 business, 4 weekend, and
// two weekday holidays. Boxing Day 2026 falls on a Saturday, so it is
// counted once as a weekend day and is not named.
check('business-days-between-dates-calculator',
  { f: '2026-12-24', t: '2027-01-04' },
  ['6 business days in a span of 12 days', 'Christmas Day | December 25, 2026',
   "New Year's Day | January 1, 2027", 'counted once, as a weekend day'],
  ['Boxing Day']);
check('business-days-between-dates-calculator',
  { f: '2026-11-02', t: '2026-11-06' },
  ['5 business days in a span of 5 days',
   'No public holiday falls on a weekday']);
// Same day both ends: one day, inclusive.
check('business-days-between-dates-calculator',
  { f: '2026-11-02', t: '2026-11-02' },
  ['1 business day in a span of 1 day']);
check('business-days-between-dates-calculator',
  { f: '2027-01-04', t: '2026-12-24' }, ['falls before the first']);
check('business-days-between-dates-calculator',
  { f: '2000-01-01', t: '2026-01-01' }, ['longer than ten years']);

// ---- 46 T183CORP signature ----------------------------------------------
check('t183corp-signature-requirement-checker',
  { off: 'y', red: 'y', bef: 'y' },
  ['Form T183CORP can be signed', 'All three conditions are met',
   'hour, minute and second', 'Six years', 'unless CRA asks for it']);
check('t183corp-signature-requirement-checker',
  { off: 'n', red: 'y', bef: 'y' },
  ['1 condition is not met', 'not an authorized signing officer']);
check('t183corp-signature-requirement-checker',
  { off: 'n', red: 'n', bef: 'n' },
  ['3 conditions is not met', 'before the return is transmitted']);
check('t183corp-signature-requirement-checker', {},
  ['Answer all three questions']);

// ---- 47 provincial returns ----------------------------------------------
check('provincial-return-requirement-checker', { qc: 'y', ab: 'n' },
  ['1 separate provincial return in addition to the federal T2',
   'Quebec | CO-17', 'CO-17 is not covered by it'], ['AT1']);
check('provincial-return-requirement-checker', { qc: 'n', ab: 'y' },
  ['Alberta | AT1', 'AT1 is not covered by it'], ['CO-17']);
check('provincial-return-requirement-checker', { qc: 'y', ab: 'y' },
  ['2 separate provincial returns', 'CO-17 and AT1 are not covered by it']);
check('provincial-return-requirement-checker', { qc: 'n', ab: 'n' },
  ['the only corporate income tax return', 'registry']);
check('provincial-return-requirement-checker', {},
  ['Answer both questions']);

// ---- 48 account closure order -------------------------------------------
check('cra-account-closure-sequencer', { rp: 'y', rt: 'y', dis: 'y' },
  ['6 steps, in this order', '1 | File every outstanding T2 return',
   '2 | Close the payroll account with Form RC145',
   '3 | Close the GST/HST account with Form RC145',
   '6 | File the registry articles of dissolution',
   'rests on a complete filing record']);
check('cra-account-closure-sequencer', { rp: 'n', rt: 'n', dis: 'n' },
  ['1 step, in this order', 'simplest position'],
  ['Form RC145']);
check('cra-account-closure-sequencer', { rp: 'y', rt: 'n', dis: 'n' },
  ['2 steps, in this order', 'Close the payroll account'],
  ['Close the GST/HST account']);
check('cra-account-closure-sequencer', {},
  ['Answer all three questions']);

// ---- 49 whole calendar ---------------------------------------------------
// Dec 31 2026: +2 months is Feb 28 2027, a Sunday, so the balance date and
// the T4 date both land on Mon Mar 1 2027. The anniversary of a 2020-05-10
// incorporation falling on or after the year-end is May 10 2027, and 60 days
// past it is Jul 9 2027.
check('corporate-deadline-calendar-generator',
  { ye: '2026-12-31', inc: '2020-05-10', fed: 'y', pay: 'y' },
  ['6 dates for a year ending December 31, 2026', 'March 1, 2027',
   'June 30, 2027', 'May 10, 2027', 'July 9, 2027', 'December 31, 2027',
   'T4 information return for 2026', 'does not derive from the year-end']);
check('corporate-deadline-calendar-generator',
  { ye: '2026-12-31', inc: '', fed: 'n', pay: 'n' },
  ['3 dates for a year ending December 31, 2026', 'June 30, 2027'],
  ['T4 information return', 'anniversary']);
check('corporate-deadline-calendar-generator',
  { ye: '', inc: '', fed: 'y', pay: 'y' },
  ['Enter the fiscal year-end']);
// Federal but no incorporation date yet: the calendar waits rather than
// printing a calendar with a hole in it.
check('corporate-deadline-calendar-generator',
  { ye: '2026-12-31', inc: '', fed: 'y', pay: 'n' },
  ['Enter the fiscal year-end']);

// ---- 50 catch-up schedule ------------------------------------------------
// Dec 31 2023 is due Jun 30 2024, a Sunday, and Jul 1 is Canada Day, so it
// moves to Jul 2 2024.
check('catch-up-filing-schedule-generator', { y1: '2019-12-31', n: '5' },
  ['5 returns, $1,500.00 plus HST in total',
   '1 | December 31, 2019 | June 30, 2020',
   '5 | December 31, 2023 | July 2, 2024',
   'oldest first', 'one Form T183CORP for each year']);
check('catch-up-filing-schedule-generator', { y1: '2025-12-31', n: '1' },
  ['1 return, $300.00 plus HST in total', '1 | December 31, 2025']);
check('catch-up-filing-schedule-generator', { y1: '2019-12-31', n: '21' },
  ['between 1 and 20']);
check('catch-up-filing-schedule-generator', { y1: '2019-12-31', n: '0' },
  ['between 1 and 20']);
check('catch-up-filing-schedule-generator', { y1: '', n: '' },
  ['Enter the earliest unfiled year-end']);

console.log('\n' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
