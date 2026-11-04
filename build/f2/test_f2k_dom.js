// Renders every batch 10 result screen by executing each page's shipped module
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

// ---- 81. T183CORP retention -------------------------------------------
// Six years from transmission, and the table must carry all six year rows
// plus the "after" row. A leap-day transmission is included because addYear
// has to land on a real date.
check('t183corp-retention-expiry-calculator', { tx: '2026-06-30' },
  ['Held until June 30, 2032', 'year 1 of six', 'year 6 of six',
   'not sent to the Canada Revenue Agency'],
  ['year 7 of six']);
check('t183corp-retention-expiry-calculator', { tx: '2024-02-29' },
  ['Held until February 28, 2030', 'year 6 of six']);
check('t183corp-retention-expiry-calculator', { tx: '' },
  ['Enter the date the return was transmitted']);
check('t183corp-retention-expiry-calculator', { tx: 'not-a-date' },
  ['not a date we can read']);

// ---- 82. CRA confirmation due date -------------------------------------
// Three business days AFTER the transmission day, weekends and Ontario
// statutory holidays skipped. Transmit Thursday 2026-11-05: Fri 6, Mon 9,
// Tue 10.
check('cra-confirmation-due-date-calculator', { tx: '2026-11-05' },
  ['Expected by November 10, 2026', 'November 6, 2026', 'November 9, 2026',
   '1 of 3', '3 of 3']);
// Transmit on a Saturday: the count still starts the day after, so the
// first business day is the Monday.
check('cra-confirmation-due-date-calculator', { tx: '2026-11-07' },
  ['is not itself a business day', 'November 9, 2026']);
// Across Christmas Day and Boxing Day 2026 (Fri 25, Sat 26): transmit
// Thu 24 -> Mon 28, Tue 29, Wed 30.
check('cra-confirmation-due-date-calculator', { tx: '2026-12-24' },
  ['Expected by December 30, 2026'],
  ['December 25, 2026']);
check('cra-confirmation-due-date-calculator', { tx: '' },
  ['Enter the date the return was transmitted']);

// ---- 83. what the fee covers -------------------------------------------
check('what-the-nil-t2-fee-covers-checker',
  { ont: 'y', fed: 'n', at1: 'n', co17: 'n', gst: 'n', pay: 'n' },
  ['1 filing outside the fee', 'The Ontario annual return',
   'Ontario Business Registry'],
  ['2 filings outside the fee']);
check('what-the-nil-t2-fee-covers-checker',
  { ont: 'n', fed: 'n', at1: 'y', co17: 'y', gst: 'n', pay: 'n' },
  ['2 filings outside the fee', 'An Alberta AT1', 'A Quebec CO-17',
   'separate provincial return']);
check('what-the-nil-t2-fee-covers-checker',
  { ont: 'n', fed: 'n', at1: 'n', co17: 'n', gst: 'n', pay: 'n' },
  ['nothing on this list is outstanding'],
  ['filings outside the fee']);
check('what-the-nil-t2-fee-covers-checker',
  { ont: 'y', fed: 'y', at1: 'y' },
  ['3 of the six questions are still unanswered']);

// ---- 84. progress tracker ----------------------------------------------
check('nil-t2-filing-progress-checker',
  { paid: 'y', link: 'n', signed: 'n', conf: 'n' },
  ['Next: signing link received', 'Done', 'To come']);
check('nil-t2-filing-progress-checker',
  { paid: 'y', link: 'y', signed: 'y', conf: 'y' },
  ['The year is filed', 'that tax year is closed']);
check('nil-t2-filing-progress-checker',
  { paid: 'n', link: 'n', signed: 'n', conf: 'n' },
  ['Next: payment received']);
check('nil-t2-filing-progress-checker', { paid: 'y' },
  ['3 of the four questions are still unanswered']);

// ---- 85. one signed form per year --------------------------------------
check('multi-year-signing-requirement-checker', { yrs: '6' },
  ['6 returns, 6 signed forms, 6 confirmations', 'Forms T183CORP to sign | 6',
   'counted per year']);
check('multi-year-signing-requirement-checker', { yrs: '1' },
  ['1 return, 1 signed form, 1 confirmation', 'has its own date'],
  ['1 returns']);
check('multi-year-signing-requirement-checker', { yrs: '0' },
  ['whole number of tax years from 1 to 20']);
check('multi-year-signing-requirement-checker', { yrs: '21' },
  ['whole number of tax years from 1 to 20']);
check('multi-year-signing-requirement-checker', { yrs: '' },
  ['Enter how many tax years are being filed']);

console.log('\n' + pass + ' passed, ' + fail + ' failed');
if (fail) { process.exit(1); }
