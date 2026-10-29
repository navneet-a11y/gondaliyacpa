// Renders every batch 6 result screen by executing each page's shipped module
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

// ---- 31 balance due ------------------------------------------------------
check('corporate-balance-due-date-calculator', { ye: '2026-12-31', ccpc: 'y' },
  ['Balance due March 31, 2027', 'return due June 30, 2027', '3 months after']);
// Dec 31 is month-end, so +2 months lands on the last day of February 2027,
// which is a Sunday, and the balance date moves to Monday March 1.
check('corporate-balance-due-date-calculator', { ye: '2026-12-31', ccpc: 'n' },
  ['Balance due March 1, 2027', '2 months after']);
// Aug 31 + 2 months is October 31 2026, a Saturday, so it moves to Monday
// November 2. The filing date is the last day of February 2027, a Sunday,
// so it moves to Monday March 1 -- which is also addMonths(ye,6) agreeing
// with dueDate(ye) on a month-end input.
check('corporate-balance-due-date-calculator', { ye: '2026-08-31', ccpc: 'n' },
  ['Balance due November 2, 2026', 'return due March 1, 2027',
   'Nothing to pay']);
check('corporate-balance-due-date-calculator', { ye: '', ccpc: 'y' },
  ['Enter the fiscal year-end']);

// ---- 32 period length ----------------------------------------------------
check('fiscal-period-length-calculator', { st: '2026-01-01', en: '2026-12-31' },
  ['365 days', 'a full tax year', '52 weeks and 1 day', 'Not exceeded']);
check('fiscal-period-length-calculator', { st: '2026-01-01', en: '2026-03-31' },
  ['90 days', 'a short tax year', 'does not get a short deadline']);
check('fiscal-period-length-calculator', { st: '2026-01-01', en: '2027-03-31' },
  ['longer than the 53-week limit', 'Exceeded']);
check('fiscal-period-length-calculator', { st: '2026-12-31', en: '2026-01-01' },
  ['last day falls before the first day']);

// ---- 33 demand deadline --------------------------------------------------
check('cra-demand-to-file-deadline-calculator', { ltr: '2026-11-02', dys: '30' },
  ['Respond by December 2, 2026', 'Business days from today']);
check('cra-demand-to-file-deadline-calculator', { ltr: '2026-01-05', dys: '30' },
  ['has passed', 'own estimate of income']);
check('cra-demand-to-file-deadline-calculator', { ltr: '2026-11-02', dys: '' },
  ['Enter the date on the letter']);
check('cra-demand-to-file-deadline-calculator', { ltr: '2026-11-02', dys: '0' },
  ['between 1 and 365']);

// ---- 34 T4 ---------------------------------------------------------------
check('t4-nil-filing-requirement-checker', { yr: '2026', acct: 'y', emp: 'n' },
  ['nil T4 information return is still expected', 'March 1, 2027'],  // Feb 28 2027 Sunday
  ['Covered by the nil T2 fee | Yes']);
check('t4-nil-filing-requirement-checker', { yr: '2026', acct: 'y', emp: 'y' },
  ['T4 slips and the summary are due']);
check('t4-nil-filing-requirement-checker', { yr: '2026', acct: 'n', emp: 'n' },
  ['No T4 return is expected']);

// ---- 35 retained earnings ------------------------------------------------
check('retained-earnings-rollforward-calculator', { ro: '1000', ni: '0', dv: '0' },
  ['Closing retained earnings $1,000.00', 'closing figure equals the opening one']);
check('retained-earnings-rollforward-calculator', { ro: '1000', ni: '500', dv: '200' },
  ['$1,300.00', 'not a nil year']);
check('retained-earnings-rollforward-calculator', { ro: '-5000', ni: '-1000', dv: '0' },
  ['Closing deficit $6,000.00']);
check('retained-earnings-rollforward-calculator', { ro: '', ni: '0', dv: '0' },
  ['Enter the three figures']);

// ---- 36 balancing --------------------------------------------------------
check('balance-sheet-balancing-checker', { as: '100', li: '40', eq: '60' },
  ['The balance sheet balances', 'Difference | $0.00']);
check('balance-sheet-balancing-checker', { as: '100', li: '40', eq: '50' },
  ['Out by $10.00', 'will not validate']);
check('balance-sheet-balancing-checker', { as: '0', li: '0', eq: '0' },
  ['The balance sheet balances']);

// ---- 37 nil GIFI balance sheet -------------------------------------------
check('nil-gifi-balance-sheet-checker', { sc: 'n', sl: 'n', re: 'n', bk: 'n' },
  ['A genuinely empty balance sheet']);
check('nil-gifi-balance-sheet-checker', { sc: 'y', sl: 'n', re: 'n', bk: 'y' },
  ['2 balances must appear', 'Share capital', 'bank balance', 'investment income']);
check('nil-gifi-balance-sheet-checker', { sc: 'y', sl: 'y', re: 'y', bk: 'y' },
  ['4 balances must appear']);

// ---- 38 schedule 8 -------------------------------------------------------
check('schedule-8-cca-requirement-checker', { dp: 'n', uc: 'n', ds: 'n' },
  ['Schedule 8 is not required', 'nothing for Schedule 8 to report']);
check('schedule-8-cca-requirement-checker', { dp: 'n', uc: 'y', ds: 'n' },
  ['Schedule 8 is required', 'carry the balance forward']);
check('schedule-8-cca-requirement-checker', { dp: 'y', uc: 'y', ds: 'y' },
  ['Schedule 8 is required', 'not a nil year']);

// ---- 39 involuntary dissolution -----------------------------------------
check('involuntary-dissolution-risk-checker', { ar: 'y', ad: 'y', dr: 'y' },
  ['Nothing on this list is outstanding']);
check('involuntary-dissolution-risk-checker', { ar: 'n', ad: 'n', dr: 'y' },
  ['annual return is outstanding and the address is stale', 'ends badly']);
check('involuntary-dissolution-risk-checker', { ar: 'n', ad: 'y', dr: 'y' },
  ['The annual return is outstanding'], ['ends badly']);
check('involuntary-dissolution-risk-checker', { ar: 'y', ad: 'n', dr: 'y' },
  ['One registry record is out of date']);

// ---- 40 director liability ----------------------------------------------
check('director-liability-exposure-checker', { pd: 'n', gh: 'n', ci: 'y' },
  ['Nothing on this list reaches the directors personally',
   'is a personal liability of the directors']);
check('director-liability-exposure-checker', { pd: 'y', gh: 'y', ci: 'n' },
  ['2 amounts of this kind can be assessed', 'worth closing']);
check('director-liability-exposure-checker', { pd: 'y', gh: 'n', ci: 'n' },
  ['1 amount of this kind can be assessed']);

// ---- addMonths must not drift from dueDate -------------------------------
// The balance-due date steps months with addMonths; every filing date on the
// site steps six months with dueDate. If the two conventions ever diverge,
// the balance dates and the filing dates stop agreeing with each other.
(function () {
  const html = fs.readFileSync('corporate-balance-due-date-calculator.html', 'utf8');
  const i = html.lastIndexOf('<script>'), j = html.indexOf('</script>', i);
  const src = html.slice(i + 8, j).replace(/\}\)\(\);\s*$/,
    'globalThis.__f={addMonths:addMonths,dueDate:dueDate,u:u,lastDay:lastDay};})();');
  global.document = { getElementById: () => ({ value: '', addEventListener() {}, innerHTML: '' }),
                      querySelector: () => null, querySelectorAll: () => [] };
  global.window = global;
  new Function(src)();
  const f = globalThis.__f;
  let n = 0, bad = 0;
  for (let y = 2019; y <= 2032; y++) {
    for (let m = 0; m < 12; m++) {
      const days = f.lastDay(y, m);
      for (const d of [1, 15, days - 1, days]) {
        if (d < 1) continue;
        const ye = f.u(y, m, d);
        n++;
        if (f.addMonths(ye, 6).getTime() !== f.dueDate(ye).getTime()) {
          bad++;
          if (bad < 6) console.log('DISAGREE addMonths/dueDate at ' + y + '-' + (m + 1) + '-' + d);
        }
      }
    }
  }
  if (bad) { fail++; } else { pass++; }
  console.log(n + ' year-ends compared, ' + bad + ' addMonths/dueDate disagreements');
})();

console.log('\n' + pass + ' checks passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
