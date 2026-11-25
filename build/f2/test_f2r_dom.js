// Renders every batch 18 result screen in a DOM stub and asserts on the text a
// visitor reads. Harness unchanged from batches 15 through 17; see
// test_f2o_dom.js for where it came from.
//
// Every money figure and every date below is worked out by hand -- the money
// from the statute, the dates from a separate implementation of the holiday
// calendar rather than from the page's own. Batch 17 shipped a build whose
// penalty band array had its columns transposed: every sentence read
// correctly and only the arithmetic was wrong. That is the class of defect
// these assertions exist for, which is why none of them is a loose substring
// like "162(7)" or "April".
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
          .replace(/&#8217;/g, "'").replace(/&rsquo;/g, "'")
          .replace(/&#8212;/g, '-').replace(/&mdash;/g, '-')
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
  // (the tally used to be incremented here as well as after the tag-balance
  // loop, so every check counted twice: batch 12's "42 passed" was 21 checks.)
  // A result screen that emits unbalanced table markup passes every text
  // assertion, because text() strips tags. A decoy proved it, so the tags are
  // counted too.
  for (const tag of ['table', 'tbody', 'thead', 'tr']) {
    const o = (h.match(new RegExp('<' + tag + '[ >]', 'g')) || []).length;
    const c = (h.match(new RegExp('</' + tag + '>', 'g')) || []).length;
    if (o !== c) {
      console.log('UNBALANCED <' + tag + '> ' + slug + ' ' + JSON.stringify(vals)
                  + ': ' + o + ' open, ' + c + ' closed');
      ok = false;
    }
  }
  if (ok) pass++; else fail++;
}

// A decoy must FAIL. Each one is a real defect this harness has to bite on:
// if a decoy passes, the harness is not testing what it claims to.
function decoy(name, fn) {
  const realLog = console.log, p0 = pass, f0 = fail;
  console.log = function () {};
  try { fn(); } catch (e) { /* a throw is a failure too */ }
  console.log = realLog;
  const bit = fail > f0;
  pass = p0; fail = f0;
  if (bit) { pass++; } else { console.log('DECOY NOT CAUGHT: ' + name); fail++; }
}

// ============================ 112. failure to comply, subsection 162(7)
// The greater of $100.00 and $25.00 x days, days counted to 100.
const A = 'failure-to-comply-penalty-calculator';

// 1 day: $25.00 is below the $100.00 floor, so the floor applies.
check(A, { days: '1', info: 'n' },
      ['$100.00 under subsection 162(7)',
       'the daily figure of $25.00 is below the $100.00 floor',
       'between $100.00 and $2,500.00'],
      ['$25.00 under subsection 162(7)']);

// 4 days: $25.00 x 4 = $100.00 exactly, which is the floor, so the daily
// figure applies and the two happen to agree. The boundary case.
check(A, { days: '4', info: 'n' },
      ['$100.00 under subsection 162(7)',
       'the daily figure of $100.00 is above the $100.00 floor']);

// 5 days: $125.00, the first day the daily figure exceeds the floor.
check(A, { days: '5', info: 'n' },
      ['$125.00 under subsection 162(7)', 'At 5 days']);

// 100 days: $2,500.00, the ceiling reached exactly.
check(A, { days: '100', info: 'n' },
      ['$2,500.00 under subsection 162(7)', 'At 100 days'],
      ['The count stops at 100 days']);

// 400 days: still $2,500.00, and the page has to say why.
check(A, { days: '400', info: 'n' },
      ['$2,500.00 under subsection 162(7)', 'The count stops at 100 days']);

// Zero days: nothing has run, and the floor has not been reached either.
check(A, { days: '0', info: 'n' },
      ['Nothing has run yet, so the daily charge is $0.00'],
      ['$100.00 under subsection 162(7)']);

// A slip return is charged under 162(7.01) instead, whatever the days.
check(A, { days: '30', info: 'y' },
      ['charged under subsection 162(7.01) instead'],
      ['under subsection 162(7)<']);

// ============================ 113. Schedule 1, line 9999 to line 300
const B = 'schedule-1-net-income-reconciliation-calculator';

// 100,000 + 20,000 - 15,000 + (4,000 / 2) + 1,000 - 500 = 107,500.
// The items moved total 20,000 + 15,000 + 4,000 + 1,000 + 500 = 40,500.
check(B, { acc: '100000', amort: '20000', cca: '15000', meals: '4000',
           addother: '1000', dedother: '500' },
      ['$107,500.00 of net income for income tax purposes',
       'moves $40,500.00 in total',
       'Half of meals and entertainment of $4,000.00 | $2,000.00']);

// Meals alone: half of 1,000 is 500, not 1,000.
check(B, { acc: '0', amort: '0', cca: '0', meals: '1000',
           addother: '0', dedother: '0' },
      ['$500.00 of net income for income tax purposes',
       'moves $1,000.00 in total'],
      ['$1,000.00 of net income for income tax purposes']);

// A nil year: nothing to reconcile, and the page says so rather than
// printing a reconciliation of zeros as though it had done arithmetic.
check(B, { acc: '0', amort: '0', cca: '0', meals: '0',
           addother: '0', dedother: '0' },
      ['$0.00 of net income for income tax purposes',
       'nothing to reconcile']);

// A loss carries through as a loss. "minus" rather than a bare minus sign,
// because money() would render it as "$-5,000.00".
check(B, { acc: '-5000', amort: '0', cca: '0', meals: '0',
           addother: '0', dedother: '0' },
      ['minus $5,000.00 of net income for income tax purposes',
       'Starting from minus $5,000.00'],
      ['$-5,000.00']);

// CCA is deducted, not added: 0 - 15,000 is a loss for tax purposes.
check(B, { acc: '0', amort: '0', cca: '15000', meals: '0',
           addother: '0', dedother: '0' },
      ['minus $15,000.00 of net income for income tax purposes',
       'Capital cost allowance from Schedule 8 | minus $15,000.00']);

// ============================ 114. GST/HST reporting period
const C = 'gst-hst-filing-frequency-calculator';

// $1,500,000 exactly is annual. The threshold is "more than".
check(C, { supplies: '1500000', dormant: 'n' },
      ['The assigned reporting period is annual',
       'Taxable supplies of $1,500,000.00',
       'three months after the fiscal year end',
       '$3,000.00'],
      ['The assigned reporting period is quarterly']);

// One dollar over is quarterly.
check(C, { supplies: '1500001', dormant: 'n' },
      ['The assigned reporting period is quarterly',
       'one month after the end of each quarter',
       'A shorter period than the assigned one can be elected']);

// $6,000,000 exactly is still quarterly.
check(C, { supplies: '6000000', dormant: 'n' },
      ['The assigned reporting period is quarterly'],
      ['The assigned reporting period is monthly']);

// One dollar over is monthly, with nothing shorter to elect.
check(C, { supplies: '6000001', dormant: 'n' },
      ['The assigned reporting period is monthly',
       'one month after the end of each month']);

// A dormant registrant on annual filing: one nil return a year.
check(C, { supplies: '0', dormant: 'y' },
      ['The assigned reporting period is annual',
       'A dormant registrant still files for every period']);

// ============================ 115. payroll remittance due dates
// Dates computed from a separate implementation of the Ontario holiday
// calendar. 2026: Good Friday is April 3, Family Day February 16.
const D = 'payroll-remittance-due-date-calculator';

// Regular remitter, pay March 10, 2026: the 15th of the following month,
// April 15, 2026, a Wednesday, so no shift.
check(D, { amwa: '10000', pay: '2026-03-10' },
      ['Remit by April 15, 2026', 'regular remitter', 'the whole month',
       '$10,000.00']);

// $24,999 is still regular; $25,000 is threshold 1. The boundary.
check(D, { amwa: '24999', pay: '2026-03-10' },
      ['Remit by April 15, 2026', 'regular remitter']);
check(D, { amwa: '25000', pay: '2026-03-10' },
      ['Remit by March 25, 2026', 'threshold 1', 'the 1st to the 15th'],
      ['regular remitter.']);

// Threshold 1, second half of the month: the 10th of the next month.
check(D, { amwa: '50000', pay: '2026-03-20' },
      ['Remit by April 10, 2026', 'threshold 1',
       'the 16th to the end of the month']);

// Threshold 2, the 1st to the 7th window. March 7, 2026 is a Saturday, so
// the third working day after it is Wednesday March 11, 2026.
check(D, { amwa: '150000', pay: '2026-03-05' },
      ['Remit by March 11, 2026', 'threshold 2', 'the 1st to the 7th']);

// Threshold 2, the last window. Three working days after Tuesday March 31,
// 2026 lands on Monday April 6, because April 3 is Good Friday.
check(D, { amwa: '150000', pay: '2026-03-28' },
      ['Remit by April 6, 2026', 'the 22nd to the end of the month']);

// $100,000 exactly is threshold 2, not threshold 1.
check(D, { amwa: '100000', pay: '2026-03-12' },
      ['remitter, threshold 2', 'the 8th to the 14th'],
      ['remitter, threshold 1']);

// Under $3,000 the quarterly schedule is named as assigned, not elected.
check(D, { amwa: '2000', pay: '2026-03-10' },
      ['Remit by April 15, 2026', 'perfect compliance record']);

// ============================ 116. subsection 15(2) inclusion
const E = 'shareholder-loan-income-inclusion-calculator';

// December 31, 2025 year end: the 15(2.6) deadline is December 31, 2026.
// Not repaid, no exception: the whole amount, in the shareholder's income.
check(E, { ye: '2025-12-31', amt: '50000', rep: 'n', exc: 'n' },
      ["$50,000.00 is included in the shareholder's income",
       'December 31, 2026',
       "Whose income it is included in | The shareholder's",
       'paragraph 20(1)(j)',
       "The corporation's own tax year | Can still be nil"]);

// Repaid in time: nothing included, and the series caveat is stated.
check(E, { ye: '2025-12-31', amt: '50000', rep: 'y', exc: 'n' },
      ['Nothing is included, because it was repaid in time',
       'series of loans and repayments'],
      ["is included in the shareholder's income"]);

// An exception takes it out whatever the repayment answer says.
check(E, { ye: '2025-12-31', amt: '50000', rep: 'n', exc: 'y' },
      ['Nothing is included under subsection 15(2)',
       'subsection 15(2.3)', 'subsection 15(2.4)']);

// A month-end year end stays at month end a year on: February 28, 2026
// gives February 28, 2027, not March 1.
check(E, { ye: '2026-02-28', amt: '1000', rep: 'n', exc: 'n' },
      ['February 28, 2027'],
      ['March 1, 2027']);

// A leap-day year end gives February 28 the following year.
check(E, { ye: '2024-02-29', amt: '1000', rep: 'n', exc: 'n' },
      ['February 28, 2025'],
      ['February 29, 2025']);

// ============================ decoys
decoy('162(7) floor ignored',
      function () { check(A, { days: '1', info: 'n' },
                          ['$25.00 under subsection 162(7)']); });
decoy('162(7) ceiling ignored',
      function () { check(A, { days: '400', info: 'n' },
                          ['$10,000.00 under subsection 162(7)']); });
decoy('meals added back in full',
      function () { check(B, { acc: '0', amort: '0', cca: '0', meals: '1000',
                               addother: '0', dedother: '0' },
                          ['$1,000.00 of net income for income tax purposes']); });
decoy('GST/HST band boundary inclusive the wrong way',
      function () { check(C, { supplies: '1500000', dormant: 'n' },
                          ['The assigned reporting period is quarterly']); });
decoy('remittance due date not shifted off Good Friday',
      function () { check(D, { amwa: '150000', pay: '2026-03-28' },
                          ['Remit by April 3, 2026']); });
decoy('15(2) attributed to the corporation',
      function () { check(E, { ye: '2025-12-31', amt: '50000', rep: 'n',
                               exc: 'n' },
                          [], ["The corporation's own tax year | Can still be nil"]); });

console.log(pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
