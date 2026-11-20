// Renders every batch 17 result screen in a DOM stub and asserts on the text a
// visitor reads. Harness unchanged from batches 15 and 16; see test_f2o_dom.js.
//
// Every money figure below is worked out by hand from the statute, because the
// first build of the T4 tool had its band array in the wrong column order and
// produced a $100.00 daily rate with the minimum and maximum equal. The text
// read perfectly; only the arithmetic was wrong. That is the class of defect
// these assertions exist for.
// percentage of a number the visitor types, and the fifth computes a ten-year
// window from a year. Both are places where an off-by-one ships silently: the
// text reads correctly and the figure is wrong. Every monetary assertion below
// is therefore an exact dollar string, worked out by hand from the statute,
// not a substring like "17%".
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

// ===================================== 107. T4, subsection 162(7.01)
// Band 1 is $10.00 a day, floor $100.00, ceiling $1,000.00.
const A = 't4-late-filing-penalty-calculator';

// 10 slips, 30 days: $10.00 x 30 = $300.00, between floor and ceiling.
check(A, { slips: '10', days: '30' },
      ['$300.00 under subsection 162(7.01)', '10 slips puts the return in the $10.00 a day band',
       '$100.00', '$1,000.00'],
      ['below the floor', 'above the ceiling']);

// 1 slip, 5 days: $50.00 raw, under the $100.00 floor, so the floor applies.
check(A, { slips: '1', days: '5' },
      ['$100.00 under subsection 162(7.01)', 'below the floor, so the floor applies']);

// 10 slips, 200 days: $2,000.00 raw, over the $1,000.00 ceiling.
check(A, { slips: '10', days: '200' },
      ['$1,000.00 under subsection 162(7.01)', 'above the ceiling, so the ceiling applies']);

// 100 slips crosses into band 2: $15.00 x 30 = $450.00.
check(A, { slips: '100', days: '30' },
      ['$450.00 under subsection 162(7.01)', '$15.00 a day band']);

// 50 is the top of band 1, 51 the bottom of band 2. The boundary is the point.
check(A, { slips: '50', days: '10' }, ['$100.00 under subsection 162(7.01)']);
check(A, { slips: '51', days: '10' }, ['$150.00 under subsection 162(7.01)']);

// The open-ended top band.
check(A, { slips: '20000', days: '10' },
      ['$750.00 under subsection 162(7.01)', '$75.00 a day band']);

// No slips: no return, so no penalty, and it says what the real question is.
check(A, { slips: '0', days: '90' },
      ['No slips means no T4 return', 'T4 nil filing requirement checker'],
      ['under subsection 162(7.01)']);

check(A, { slips: '', days: '' },
      ['2 of the two figures are still to come'], ['162(7.01)']);

// ===================================== 108. shareholder loan, 15(2.6)
const B = 'shareholder-loan-repayment-deadline-calculator';

// A December 31, 2025 year end gives a December 31, 2026 deadline.
check(B, { ye: '2025-12-31', rep: 'n' },
      ['Repay by December 31, 2026', 'December 31, 2025']);

// Repaid: outside 15(2) altogether.
check(B, { ye: '2025-12-31', rep: 'y' },
      ['Repaid, so subsection 15(2) does not reach it'],
      ['Repay by']);

// A deadline already gone by. The consequence is the SHAREHOLDER's, and the
// corporate year can still be nil: the whole point of the page.
check(B, { ye: '2020-06-30', rep: 'n' },
      ['The deadline passed June 30, 2021', 'shareholder', 'The shareholder, personally',
       'Can still be nil'],
      ['Repay by']);

// A mid-month year end keeps its day.
check(B, { ye: '2026-03-15', rep: 'n' }, ['Repay by March 15, 2027']);

check(B, { ye: '' }, ['2 of the two entries are still to come']);

// ===================================== 109. Ontario initial return
const C = 'ontario-initial-return-deadline-calculator';

// 60 days after January 15, 2030 is March 16, 2030. A date far enough ahead
// that this assertion does not expire: the result screen branches on today(),
// so a nearer date would flip to the overdue wording as time passed.
check(C, { inc: '2030-01-15', ont: 'y', filed: 'n' },
      ['Due March 16, 2030', 'January 15, 2030', 'Once', 'Every year']);

// A date long past.
check(C, { inc: '2020-01-15', ont: 'y', filed: 'n' },
      ['It was due March 15, 2020']);

// Filed: one-time, not due again.
check(C, { inc: '2030-01-15', ont: 'y', filed: 'y' },
      ['Filed, and it is not due again', 'It is a one-time filing']);

// Not an Ontario corporation: the federal branch, no date announced.
check(C, { inc: '2030-01-15', ont: 'n', filed: 'n' },
      ['This is not a filing your corporation makes', 'Corporations Canada'],
      ['Due March 16, 2030']);

check(C, { inc: '' }, ['3 of the three entries are still to come']);

// ===================================== 110. gross negligence, 163(2)
const D = 'gross-negligence-penalty-checker';

// Half of $9,000.00 understated, knowledge met.
check(D, { under: '9000', know: 'y', nil: 'n' },
      ['$4,500.00 under subsection 163(2)', 'on top of any late-filing penalty']);

// The $100.00 floor: half of $120.00 is $60.00.
check(D, { under: '120', know: 'y', nil: 'n' },
      ['$100.00 under subsection 163(2)', 'raised to the $100.00 minimum']);

// Knowledge not met: the provision does not apply, and the onus is named.
check(D, { under: '9000', know: 'n', nil: 'n' },
      ['The knowledge element is not met', 'onus', '$4,500.00'],
      ['$4,500.00 under subsection 163(2)']);

// A nil return: no base at all, with rule 3's qualification attached.
check(D, { under: '0', know: 'n', nil: 'y' },
      ['Nothing was understated', 'no percentage late-filing penalty',
       '$300.00 plus applicable sales tax per tax year'],
      ['plus HST']);

check(D, { under: '' }, ['3 of the three entries are still to come']);

// ===================================== 111. GST/HST registration
const E = 'gst-hst-registration-requirement-checker';

// Under on both tests.
check(E, { rev: '12000', qtr: 'n', reg: 'n' },
      ['A small supplier on these answers', '$12,000.00', '$30,000.00']);

// Over on the four-quarter test.
check(E, { rev: '45000', qtr: 'n', reg: 'n' },
      ['Registration is required', '$45,000.00', 'four consecutive calendar quarters']);

// Under on four quarters but over in a single one: still required. This is the
// test people forget and the reason the second question exists.
check(E, { rev: '28000', qtr: 'y', reg: 'n' },
      ['Registration is required', 'single calendar quarter over $30,000.00']);

// Already registered: the question becomes filing, not joining.
check(E, { rev: '0', qtr: 'n', reg: 'y' },
      ['Already registered', 'An open account reports every period'],
      ['A small supplier on these answers']);

// A dormant year, no account: under the threshold and nothing owed.
check(E, { rev: '0', qtr: 'n', reg: 'n' },
      ['A small supplier on these answers', 'account nobody closed']);

check(E, { rev: '' }, ['3 of the three entries are still to come']);

// ---- decoys: each must be caught -------------------------------------
decoy('T4 band order wrong, the bug the first build had',
      function () { check(A, { slips: '10', days: '30' }, ['$3,000.00']); });
decoy('15(2) attributed to the corporation',
      function () { check(B, { ye: '2020-06-30', rep: 'n' },
                          [], ['Can still be nil']); });
decoy('60 days counted as two months',
      function () { check(C, { inc: '2030-01-15', ont: 'y', filed: 'n' },
                          ['Due March 15, 2030']); });
decoy('163(2) floor ignored',
      function () { check(D, { under: '120', know: 'y', nil: 'n' },
                          ['$60.00 under subsection 163(2)']); });
decoy('single-quarter test ignored',
      function () { check(E, { rev: '28000', qtr: 'y', reg: 'n' },
                          ['A small supplier on these answers']); });

console.log(pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
