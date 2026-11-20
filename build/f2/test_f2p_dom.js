// Renders every batch 16 result screen by executing each page's shipped module
// in a DOM stub, then asserts on the text a visitor would actually read.
//
// The harness is the one batch 15 used, unchanged: it reaches into the page's
// IIFE closure and calls show() directly, because the page only ever calls it
// from an event listener and a stub whose addEventListener is a no-op never
// fires one. See test_f2o_dom.js for the full reasoning.
//
// What this batch needs it for. Four of the five tools compute money from a
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

// =========================================== 101. subsection 162(1)
// 5% of tax unpaid at the due date, plus 1% of it per complete month, to 12.
const A = 't2-late-filing-penalty-calculator';

// A June 15 year-end is due December 15. Filed March 20 is three complete
// months late (Jan 15, Feb 15, Mar 15), so 5% + 3% = 8% of $9,000.00.
// $450.00 flat + $90.00 x 3 = $720.00.
check(A, { ye: '2025-06-15', tax: '9000', filed: '2026-03-20' },
      ['$720.00 under subsection 162(1)', '3 complete months',
       'December 15, 2025', 'March 20, 2026', '8%', '$450.00', '$270.00'],
      ['on time']);

// Filed on the due date itself is not late at all.
check(A, { ye: '2025-12-31', tax: '9000', filed: '2026-06-30' },
      ['The return is on time', 'due June 30, 2026'],
      ['under subsection 162(1)', '$1,530.00']);

// Past twelve complete months the monthly part is at its ceiling: 17%.
// $450.00 + $90.00 x 12 = $1,530.00.
check(A, { ye: '2025-12-31', tax: '9000', filed: '2028-01-01' },
      ['$1,530.00 under subsection 162(1)', '17%',
       'Twelve complete months have gone by', 'Arrears interest'],
      ['13 complete months']);

// A nil year: the same arithmetic on $0.00, and rule 3's qualification
// travels with it rather than a bare claim.
check(A, { ye: '2025-12-31', tax: '0', filed: '2027-01-01' },
      ['The penalty is $0.00, and the year is still open',
       'no percentage late-filing penalty', 'stays open forever',
       'blocks a clearance certificate',
       '$300.00 plus applicable sales tax per tax year'],
      ['plus HST', 'including HST']);

// Every entry still missing is counted, and no figure is announced early.
check(A, { ye: '', tax: '', filed: '' },
      ['3 of the three entries are still to come'],
      ['under subsection 162(1)']);
check(A, { ye: '2025-12-31', tax: '', filed: '2027-01-01' },
      ['1 of the three entries is still to come']);

// =========================================== 102. subsection 162(2)
// Both conditions met: 10% + 2% per month to 20. Neither: back to 162(1).
const B = 'repeated-failure-to-file-penalty-calculator';

// Demand served AND a prior penalty: 10% + 2% x 20 = 50% of $9,000.00.
// $900.00 + $180.00 x 20 = $4,500.00.
check(B, { tax: '9000', mo: '20', dem: 'y', prior: 'y' },
      ['$4,500.00 under subsection 162(2)', 'Both conditions are met',
       '20 complete months', '20 of 20', 'Yes'],
      ['No demand to file was served']);

// A demand but no prior penalty falls back to 162(1), capped at 12 months:
// $450.00 + $90.00 x 12 = $1,530.00.
check(B, { tax: '9000', mo: '20', dem: 'y', prior: 'n' },
      ['$1,530.00 under subsection 162(1)',
       'A demand was served, but no prior penalty was assessed',
       '12 of 12', 'demand to file deadline calculator'],
      ['under subsection 162(2)']);

// No demand at all: 162(1) again, and the demand paragraph stays away.
check(B, { tax: '9000', mo: '20', dem: 'n', prior: 'y' },
      ['$1,530.00 under subsection 162(1)',
       'No demand to file was served'],
      ['demand to file deadline calculator']);

// A nil year, both conditions met: still $0.00, with the qualification.
check(B, { tax: '0', mo: '20', dem: 'y', prior: 'y' },
      ['Either provision computes to $0.00 on a nil year',
       'no percentage late-filing penalty',
       '$300.00 plus applicable sales tax per tax year'],
      ['plus HST']);

check(B, { tax: '', mo: '' },
      ['4 of the four entries are still to come'], ['subsection 162']);

// =========================================== 103. GST/HST nil return
// Annual filers three months after the fiscal year end, others one month.
const C = 'gst-hst-nil-return-deadline-calculator';

check(C, { pe: '2025-12-31', ann: 'y', open: 'y' },
      ['Due March 31, 2026', 'An annual filer files three months',
       'A nil GST/HST return is a return, not an absence of one',
       '$300.00 plus applicable sales tax per tax year', 'No'],
      ['one month after', 'plus HST']);

check(C, { pe: '2025-12-31', ann: 'n', open: 'y' },
      ['Due January 31, 2026',
       'A monthly or quarterly filer files one month after'],
      ['three months after']);

// A quarter ending March 31 is due April 30.
check(C, { pe: '2026-03-31', ann: 'n', open: 'y' },
      ['Due April 30, 2026']);

// A closed account has no further period, so no date is announced.
check(C, { pe: '2025-12-31', ann: 'y', open: 'n' },
      ['A closed account files nothing further', 'final return',
       'GST/HST account closure checker'],
      ['Due March 31, 2026']);

check(C, { pe: '' }, ['3 of the three entries are still to come'],
      ['Due ']);

// =========================================== 104. voluntary disclosure
const D = 'voluntary-disclosure-eligibility-checker';

// All three conditions met on years that were not nil.
check(D, { ct: 'n', old: 'y', all: 'y', nil: 'n' },
      ['The three conditions are met on these answers',
       'the estimated tax owing is paid with it', 'Met', 'Likely'],
      ['unlikely to count as voluntary']);

// Met, but the years were nil: the page says the programme may be redundant
// rather than selling an application nobody needs.
check(D, { ct: 'n', old: 'y', all: 'y', nil: 'y' },
      ['nil years may not need the programme',
       'no percentage late-filing penalty',
       'Unlikely on nil years',
       '$300.00 plus applicable sales tax per tax year']);

// The Agency has already been in touch: not voluntary.
check(D, { ct: 'y', old: 'y', all: 'y', nil: 'n' },
      ['It is unlikely to count as voluntary', 'Not met'],
      ['The three conditions are met']);

// Nothing a year past due yet.
check(D, { ct: 'n', old: 'n', all: 'y', nil: 'n' },
      ['Nothing is far enough past due yet'],
      ['The three conditions are met']);

// A partial disclosure fails the completeness condition.
check(D, { ct: 'n', old: 'y', all: 'n', nil: 'n' },
      ['A partial disclosure does not meet the condition',
       'outstanding returns count checker']);

check(D, {}, ['4 of the four questions are still unanswered'],
      ['conditions are met']);

// =========================================== 105. taxpayer relief
// A request made in 2026 reaches tax years ending 2016 or later.
const E = 'taxpayer-relief-eligibility-checker';

check(E, { yr: '2019', ground: 'y', filed: 'y', nil: 'n' },
      ['2019 is in the window and a ground is identified', 'RC4288',
       'Met, 2019', 'Identified'],
      ['outside the ten-year window']);

// 2016 is the earliest year in reach, so it must be inside.
check(E, { yr: '2016', ground: 'y', filed: 'y', nil: 'n' },
      ['2016 is in the window'], ['outside the ten-year window']);

// 2015 is one year too early, and the boundary is the whole point.
check(E, { yr: '2015', ground: 'y', filed: 'y', nil: 'n' },
      ['2015 is outside the ten-year window',
       'reaches tax years ending in 2016 or later', 'Not met, 2015'],
      ['is in the window']);

// In the window but nothing to rest on.
check(E, { yr: '2019', ground: 'n', filed: 'y', nil: 'n' },
      ['No ground is identified on these answers', 'None identified'],
      ['RC4288']);

// A nil year: nothing for relief to reach, whatever the other answers.
check(E, { yr: '2019', ground: 'y', filed: 'y', nil: 'y' },
      ['A nil year has nothing for relief to reach',
       'no percentage late-filing penalty',
       'never the tax', 'No, the years were nil'],
      ['RC4288']);

// Returns not filed: the order of operations is stated.
check(E, { yr: '2019', ground: 'y', filed: 'n', nil: 'n' },
      ['The returns themselves come first',
       'catch-up filing schedule generator', 'Not yet']);

check(E, { yr: '' }, ['4 of the four entries are still to come'],
      ['ten-year window']);

// ---- decoys: each must be caught -------------------------------------
decoy('wrong 162(1) figure accepted',
      function () { check(A, { ye: '2025-06-15', tax: '9000',
                               filed: '2026-03-20' }, ['$721.00']); });
decoy('162(2) applied without a prior penalty',
      function () { check(B, { tax: '9000', mo: '20', dem: 'y', prior: 'n' },
                          ['under subsection 162(2)']); });
decoy('annual and monthly dates confused',
      function () { check(C, { pe: '2025-12-31', ann: 'y', open: 'y' },
                          ['Due January 31, 2026']); });
decoy('ten-year boundary off by one',
      function () { check(E, { yr: '2015', ground: 'y', filed: 'y',
                               nil: 'n' }, ['is in the window']); });

console.log(pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
