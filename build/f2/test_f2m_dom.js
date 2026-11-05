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

// ------------------------------------------------------------ Schedule 3
check('schedule-3-dividends-paid-checker', { paid: 'n', recd: 'n', decl: 'n' },
  ['Nothing here puts the year on Schedule 3', 'Nothing to report on this line',
   'What the corporation holds and who owns it decide the rest'],
  ['not a nil year', 'gondaliyacpa.ca']);
check('schedule-3-dividends-paid-checker', { paid: 'y', recd: 'n', decl: 'n' },
  ['1 of three put the year on Schedule 3', 'not a nil year',
   'taxable dividends paid', 'gondaliyacpa.ca']);
check('schedule-3-dividends-paid-checker', { paid: 'n', recd: 'n', decl: 'y' },
  ['1 of three put the year on Schedule 3',
   'activity whether or not any cash moved']);
check('schedule-3-dividends-paid-checker', { paid: 'y', recd: 'y', decl: 'y' },
  ['3 of three put the year on Schedule 3', 'Part IV tax']);
check('schedule-3-dividends-paid-checker', { paid: 'y' },
  ['2 of the three questions are still unanswered']);

// ------------------------------------------------------------ Schedule 7
check('schedule-7-investment-income-calculator', { int: 0, rent: 0, oth: 0 },
  ['No investment income for the year', '$0.00'],
  ['not a nil year', 'gondaliyacpa.ca']);
check('schedule-7-investment-income-calculator', { int: 12, rent: 0, oth: 0 },
  ['$12.00 of investment income', 'not a nil year', 'gondaliyacpa.ca']);
check('schedule-7-investment-income-calculator', { int: 1000, rent: 2000, oth: 0 },
  ['$3,000.00 of investment income']);
check('schedule-7-investment-income-calculator', { int: '', rent: '', oth: '' },
  ['Enter the amounts above']);
check('schedule-7-investment-income-calculator', { int: 'abc', rent: 0, oth: 0 },
  ['Enter whole dollars']);
check('schedule-7-investment-income-calculator', { int: -5, rent: 0, oth: 0 },
  ['Enter whole dollars']);
check('schedule-7-investment-income-calculator', { int: 5, rent: '', oth: '' },
  ['$5.00 of investment income', '2 of the three lines are still blank']);

// ------------------------------------------------------------ Schedule 9
check('schedule-9-related-corporations-checker',
  { rel: 'n', asc: 'n', act: 'n' },
  ['Schedule 9 has nothing to report',
   'Schedule 50 is not the schedule that reports related or associated']);
check('schedule-9-related-corporations-checker',
  { rel: 'y', asc: 'n', act: 'n' },
  ['Schedule 9 reaches this corporation',
   'the relationship is reported and the year can still be nil'],
  ['gondaliyacpa.ca']);
check('schedule-9-related-corporations-checker',
  { rel: 'y', asc: 'y', act: 'y' },
  ['Schedule 9 reaches this corporation', 'not a nil year', 'gondaliyacpa.ca'],
  ['the year can still be nil']);
check('schedule-9-related-corporations-checker', { rel: 'n' },
  ['2 of the three questions are still unanswered']);

// ----------------------------------------------------------- Schedule 23
check('schedule-23-association-agreement-checker',
  { asc: 'y', act: 'y', sbd: 'y' },
  ['There is a business limit to allocate', 'gondaliyacpa.ca']);
check('schedule-23-association-agreement-checker',
  { asc: 'y', act: 'n', sbd: 'n' },
  ['Nothing to allocate for this corporation', 'A nil year reaches none of this'],
  ['gondaliyacpa.ca']);
check('schedule-23-association-agreement-checker',
  { asc: 'n', act: 'n', sbd: 'n' },
  ['Nothing to allocate: no associated corporation']);
check('schedule-23-association-agreement-checker', { asc: 'y', act: 'y' },
  ['1 of the three questions is still unanswered']);

// ----------------------------------------------------------- Schedule 88
check('schedule-88-internet-activities-checker',
  { site: 'n', earn: 'n', sell: 'n' },
  ['No web page or site, so nothing to report'],
  ['gondaliyacpa.ca', 'keep its year nil']);
check('schedule-88-internet-activities-checker',
  { site: 'y', earn: 'n', sell: 'n' },
  ['A site that earns nothing is outside Schedule 88', 'keep its year nil'],
  ['gondaliyacpa.ca']);
check('schedule-88-internet-activities-checker',
  { site: 'y', earn: 'y', sell: 'n' },
  ['Income came through the site', 'not a nil year', 'gondaliyacpa.ca']);
check('schedule-88-internet-activities-checker',
  { site: 'y', earn: 'n', sell: 'y' },
  ['Income came through the site', 'gondaliyacpa.ca']);

// ---------------------------------------------------------------- decoys
decoy('a wrong heading is accepted', function () {
  check('schedule-3-dividends-paid-checker', { paid: 'n', recd: 'n', decl: 'n' },
    ['3 of three put the year on Schedule 3']);
});
decoy('rule 8 missing where a dividend moved', function () {
  check('schedule-3-dividends-paid-checker', { paid: 'y', recd: 'n', decl: 'n' },
    [], ['gondaliyacpa.ca']);
});
decoy('an unanswered question silently produces a verdict', function () {
  check('schedule-9-related-corporations-checker', { rel: 'y' },
    ['Schedule 9 reaches this corporation']);
});
decoy('a bad number renders as NaN', function () {
  check('schedule-7-investment-income-calculator', { int: 'abc', rent: 0, oth: 0 },
    ['NaN']);
});

console.log('\n' + pass + ' passed, ' + fail + ' failed');
if (fail) { process.exit(1); }
