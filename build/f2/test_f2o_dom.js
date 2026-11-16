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
// ---------------------------------------- Ontario annual return due date
// Six months after the fiscal year-end, with the end-of-month convention.
const S = 'ontario-annual-return-due-date-calculator';

// December 31 year-end -> June 30. The canonical case.
check(S, { ye: '2025-12-31', ont: 'y', since: 'y' },
      ['Both are due June 30, 2026', 'Ontario Business Registry',
       'Canada Revenue Agency, electronically', 'December 31, 2025'],
      ['incorporation anniversary rather than the year-end']);

// March 31 year-end -> September 30, the other example the body states.
check(S, { ye: '2026-03-31', ont: 'y', since: 'y' },
      ['Both are due September 30, 2026']);

// A mid-month year-end keeps the day of the month.
check(S, { ye: '2026-01-15', ont: 'y', since: 'y' },
      ['Both are due July 15, 2026']);

// Feb 28 in a non-leap year is the last day of its month, so the
// end-of-month convention carries it to August 31, not August 28.
check(S, { ye: '2026-02-28', ont: 'y', since: 'y' },
      ['Both are due August 31, 2026']);

// Not an Ontario corporation: the federal anniversary branch, no due date.
check(S, { ye: '2025-12-31', ont: 'n', since: 'n' },
      ['This is not the return your corporation files',
       'Corporations Canada', 'still due June 30, 2026'],
      ['Both are due']);

// Nothing filed since October 2021: the correcting branch appears.
check(S, { ye: '2025-12-31', ont: 'y', since: 'n' },
      ['There is probably more than one outstanding', 'May 15, 2021',
       'October 18, 2021']);

// Having filed one already must NOT show the catch-up branch.
check(S, { ye: '2025-12-31', ont: 'y', since: 'y' },
      ['the route is the one you know'],
      ['There is probably more than one outstanding']);

// The fee line is on every Ontario branch, and never names HST.
check(S, { ye: '2025-12-31', ont: 'y', since: 'y' },
      ['$300.00 plus applicable sales tax per tax year',
       'filing it is a Registry transaction we do not make on your behalf'],
      ['plus HST', 'including HST']);

// Each input still missing is counted, and no date is announced early.
// The date input is always in the DOM with an empty value, so it is modelled
// as present-and-empty rather than absent; an absent element is not a state
// the shipped page can reach.
check(S, { ye: '', ont: 'y', since: 'y' },
      ['1 of the three entries is still to come'], ['Both are due']);
check(S, { ye: '' }, ['3 of the three entries are still to come'],
      ['Both are due']);

// A year-end whose six-month date lands on a weekend states the T2 shift
// and does not silently move the Ontario date with it.
// 2026-05-31 -> November 30, 2026 is a Monday, so pick one that is not:
// 2025-09-30 -> March 30, 2026 (Monday). 2026-06-30 -> December 30 (Wed).
// 2026-08-31 -> February 28, 2027 is a Sunday.
check(S, { ye: '2026-08-31', ont: 'y', since: 'y' },
      ['Both are due February 28, 2027', 'March 1, 2027',
       'treat February 28, 2027 as the Ontario date']);

// ---- decoys: each must be caught -------------------------------------
decoy('wrong due date accepted',
      function () { check(S, { ye: '2025-12-31', ont: 'y', since: 'y' },
                          ['Both are due June 29, 2026']); });
decoy('catch-up branch leaking into the filed-already case',
      function () { check(S, { ye: '2025-12-31', ont: 'y', since: 'y' },
                          [], ['the route is the one you know']); });

console.log(pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
