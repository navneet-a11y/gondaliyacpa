// Renders every batch 9 result screen by executing each page's shipped module
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


// ---------------------------------------------------------------- 61 year-end
check('year-end-change-approval-checker', { fy: 'y', ch: 'n', ap: 'n' },
  ['nothing to approve on a first year-end', '53 weeks']);
check('year-end-change-approval-checker', { fy: 'n', ch: 'n', ap: 'n' },
  ['No year-end change, so no approval question']);
check('year-end-change-approval-checker', { fy: 'n', ch: 'y', ap: 'y' },
  ['The change is settled', 'two periods to file'],
  ['outside this service']);
check('year-end-change-approval-checker', { fy: 'n', ch: 'y', ap: 'n' },
  ['still needing approval is outside this service', 'gondaliyacpa.ca',
   '$350.00 plus HST per year']);
// an unanswered first question must not produce a verdict
check('year-end-change-approval-checker', { ch: 'y', ap: 'y' },
  ['Answer the questions above'], ['settled']);

// --------------------------------------------------------------- 62 exclusion
var ALL_OK = { ccpc: 'y', ninc: 'y', pe: 'y', div: 'y', cad: 'y', cred: 'y',
               ott: 'y', s342: 'y' };
function less(o, over) { var c = {}, k;
  for (k in o) { c[k] = o[k]; } for (k in over) { c[k] = over[k]; } return c; }
check('t2-short-exclusion-checker', ALL_OK,
  ['Nothing here excludes the short return']);
check('t2-short-exclusion-checker', less(ALL_OK, { ccpc: 'n' }),
  ['1 of the eight conditions excludes',
   'Canadian-controlled private corporation throughout the year',
   'gondaliyacpa.ca']);
check('t2-short-exclusion-checker', less(ALL_OK, { ninc: 'n', cad: 'n' }),
  ['2 of the eight conditions exclude', 'Reports in Canadian currency'],
  ['gondaliyacpa.ca']);           // neither of those two is a nil question
check('t2-short-exclusion-checker', less(ALL_OK, { div: 'n' }),
  ['1 of the eight conditions excludes', 'gondaliyacpa.ca']);
var SEVEN = less(ALL_OK, {}); delete SEVEN.s342;
check('t2-short-exclusion-checker', SEVEN,
  ['1 of the eight conditions is still unanswered'], ['excludes']);

// -------------------------------------------------------------------- 63 ccpc
check('t2-short-ccpc-condition-checker',
  { res: 'y', pub: 'n', nr: 'n', corp: 'n' },
  ['reads as a Canadian-controlled private corporation',
   'clears the first of the eight T2 Short conditions'],
  ['gondaliyacpa.ca']);
check('t2-short-ccpc-condition-checker',
  { res: 'n', pub: 'n', nr: 'n', corp: 'n' },
  ['does not read as a CCPC', 'not resident in Canada', 'gondaliyacpa.ca']);
check('t2-short-ccpc-condition-checker',
  { res: 'y', pub: 'y', nr: 'y', corp: 'y' },
  ['does not read as a CCPC', 'traded on a designated stock exchange',
   'controlled by non-residents',
   'controlled by one or more public corporations']);

// ---------------------------------------------------------------- 64 timeline
// 2026-03-15 + 6 months = 2026-09-15, a Tuesday, so no business-day shift.
check('dissolution-timeline-calculator', { ds: '2026-03-15', un: 'n' },
  ['The final T2 is due September 15, 2026',
   'The final tax year ends on March 15, 2026',
   '1. Final T2', '2. Clearance certificate', '3. Registry dissolution'],
  ['Outstanding years', 'is a Saturday']);
check('dissolution-timeline-calculator', { ds: '2026-03-15', un: 'y' },
  ['1. Outstanding years', '2. Final T2', '3. Clearance certificate',
   '4. Registry dissolution', 'oldest first']);
// 2026-02-08 + 6 months = 2026-08-08, a Saturday; next business day Monday 10th
// (Monday 3 August is the civic holiday, so the 8th is the date that tests it).
check('dissolution-timeline-calculator', { ds: '2026-02-08', un: 'n' },
  ['The final T2 is due August 8, 2026',
   'August 8, 2026 is a Saturday', 'August 10, 2026 is on time']);
check('dissolution-timeline-calculator', { ds: '', un: 'n' },
  ['Enter the planned dissolution date'], ['due']);

// ----------------------------------------------------------------- 65 payroll
check('payroll-account-closure-checker',
  { op: 'n', rem: 'n', t4: 'n', cl: 'n' },
  ['No payroll account, so nothing to close'], ['RC145']);
check('payroll-account-closure-checker',
  { op: 'y', rem: 'n', t4: 'y', cl: 'y' },
  ['The account is open', 'Form RC145 is the closure',
   'not covered by the fee', 'inactive T2 does not close a payroll account']);
check('payroll-account-closure-checker',
  { op: 'y', rem: 'y', t4: 'n', cl: 'n' },
  ['The account is open', 'gondaliyacpa.ca',
   'Outstanding T4 filings stay outstanding'],
  ['Form RC145 is the closure']);

// ---------------------------------------------------------------- 66 register
check('shareholder-register-completeness-checker',
  { kn: 'y', nm: 'y', ad: 'y', pc: 'y' },
  ['Schedule 50 can be completed from what you have']);
check('shareholder-register-completeness-checker',
  { kn: 'y', nm: 'n', ad: 'n', pc: 'y' },
  ['2 of the four are missing', 'Full legal name for each of them',
   'Address for each of them']);
check('shareholder-register-completeness-checker', { kn: 'y', nm: 'y', ad: 'y' },
  ['1 of the four is still unanswered'], ['can be completed']);

// --------------------------------------------------------------- 67 direction
check('due-to-versus-due-from-shareholder-checker', { owe: 'n', owed: 'n' },
  ['No shareholder balance either way', 'share capital, cash']);
check('due-to-versus-due-from-shareholder-checker', { owe: 'y', owed: 'n' },
  ['Due to the shareholder, so a liability',
   'does not change whether the schedules are required'],
  ['A balance in both directions']);
check('due-to-versus-due-from-shareholder-checker', { owe: 'n', owed: 'y' },
  ['Due from the shareholder, so an asset']);
check('due-to-versus-due-from-shareholder-checker', { owe: 'y', owed: 'y' },
  ['A balance in both directions', 'reported separately']);

// --------------------------------------------------------------- 68 arbitrary
check('arbitrary-assessment-response-checker', { as: 'n', nil: 'y', fl: 'n' },
  ['No assessment on an unfiled year']);
check('arbitrary-assessment-response-checker', { as: 'y', nil: 'y', fl: 'n' },
  ['answer is to file the real return for that year',
   'file the year that was assessed'],
  ['gondaliyacpa.ca']);
check('arbitrary-assessment-response-checker', { as: 'y', nil: 'y', fl: 'y' },
  ['The return is in', 'have something to give way to']);
check('arbitrary-assessment-response-checker', { as: 'y', nil: 'n', fl: 'n' },
  ['gondaliyacpa.ca']);

// -------------------------------------------------------------------- 69 stub
check('stub-period-return-checker', { se: 'n', di: 'n', pe: '' },
  ['A full fiscal year, so no stub period'], ['own tax year and its own']);
// 2026-06-30 is the last day of June, so the end-of-month rule gives 31 Dec.
check('stub-period-return-checker', { se: 'y', di: 'y', pe: '2026-06-30' },
  ['its own tax year and its own return', 'due December 31, 2026',
   'the final tax year and its return is the final T2']);
check('stub-period-return-checker', { se: 'y', di: 'n', pe: '2026-02-08' },
  ['due August 8, 2026', 'August 8, 2026 is a Saturday',
   'August 10, 2026 is on time', 'year-end change approval checker']);
check('stub-period-return-checker', { se: 'y', di: 'n', pe: '' },
  ['its own tax year and its own return'], ['due ']);

// ---------------------------------------------------------------- 70 standing
check('cra-account-standing-checker', { t2: 'n', ar: 'n', st: 'n' },
  ['Both records read as current']);
check('cra-account-standing-checker', { t2: 'y', ar: 'n', st: 'n' },
  ['One record is behind', 'Filing each outstanding T2, oldest first',
   'oldest first because a T2 carries figures forward']);
check('cra-account-standing-checker', { t2: 'y', ar: 'y', st: 'n' },
  ['Both records are behind', 'not covered by the fee']);
check('cra-account-standing-checker', { t2: 'y', ar: 'n', st: 'y' },
  ['Struck by the registry', 'does not cancel an outstanding T2']);

console.log('\n' + pass + ' passed, ' + fail + ' failed');
if (fail) { process.exit(1); }
