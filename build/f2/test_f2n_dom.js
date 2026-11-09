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

// Tool 99 counts tax year-ends and their filing dates against today, so the
// expected figure is derived here with the same arithmetic rather than
// hard-coded to one run date.
function outstandingSince(y, m, d) {
  const now = new Date();
  const today = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
  let n = 0;
  for (let i = 1; i <= 40; i++) {
    const ye = Date.UTC(y + i, m, d);
    if (ye > today) break;
    // six months after the year-end, end-of-month preserved
    const due = Date.UTC(y + i, m + 7, 0);
    if (due <= today) n++;
  }
  return n;
}

// --------------------------------------------- 96 permanent establishment
check('permanent-establishment-checker', { qc: 'n', ab: 'n', only: 'n' },
  ['No Quebec or Alberta establishment on these answers',
   'No CO-17 from this question', 'Owed either way'],
  ['does not price']);
check('permanent-establishment-checker', { qc: 'y', ab: 'n', only: 'n' },
  ['1 separate provincial return on these answers',
   'The CO-17 is a separate return', 'does not price']);
check('permanent-establishment-checker', { qc: 'y', ab: 'y', only: 'y' },
  ['2 separate provincial returns', 'The AT1 is a separate return',
   'registered office is the only address']);
check('permanent-establishment-checker', { qc: 'n' },
  ['2 of the three questions are still unanswered']);

// ----------------------------------------------- 97 carrying on business
check('carrying-on-business-in-canada-checker',
  { bank: 'y', asset: 'n', reg: 'y', trade: 'n' },
  ['Holding, not carrying on business', 'Having is not doing',
   'the year is nil'],
  ['gondaliyacpa.ca']);
check('carrying-on-business-in-canada-checker',
  { bank: 'n', asset: 'n', reg: 'n', trade: 'n' },
  ['Nothing held and nothing done']);
check('carrying-on-business-in-canada-checker',
  { bank: 'y', asset: 'y', reg: 'y', trade: 'y' },
  ['That is carrying on business', 'This is the one that decides it',
   'gondaliyacpa.ca']);
check('carrying-on-business-in-canada-checker', { bank: 'y' },
  ['3 of the four questions are still unanswered']);

// ------------------------------------------------- 98 non-resident filing
check('non-resident-corporation-filing-checker',
  { own: 'y', inc: 'y', act: 'n' },
  ['A return is owed, whoever owns it', '$25.00 per day', '$2,500.00',
   'A nil year is still filed'],
  ['gondaliyacpa.ca']);
check('non-resident-corporation-filing-checker',
  { own: 'n', inc: 'y', act: 'y' },
  ['A return is owed, whoever owns it', 'gondaliyacpa.ca'],
  ['$25.00 per day']);
check('non-resident-corporation-filing-checker',
  { own: 'n', inc: 'n', act: 'n' },
  ['That turns on a different question', 'carries on business in Canada']);
check('non-resident-corporation-filing-checker', { own: 'y', inc: 'y' },
  ['1 of the three questions is still unanswered']);

// ---------------------------------------------- 99 outstanding returns
check('outstanding-returns-count-checker', { last: '', same: 'y' },
  ['Enter the year-end of the last return you filed']);
check('outstanding-returns-count-checker', { last: '2020-12-31', same: 'y' },
  [outstandingSince(2020, 11, 31) + ' returns outstanding',
   'December 31, 2021', 'oldest first']);
check('outstanding-returns-count-checker', { last: '2020-12-31', same: 'n' },
  ['indicative only', 'short tax year']);
check('outstanding-returns-count-checker', { last: '2035-01-31', same: 'y' },
  ['That year-end is in the future']);
check('outstanding-returns-count-checker', { last: 'not-a-date', same: 'y' },
  ['Enter a valid date']);

// -------------------------------------------------------- 100 Schedule 11
check('schedule-11-shareholder-transactions-checker',
  { adv: 'n', pay: 'n', bal: 'y' },
  ['A balance, but no transaction',
   'GIFI Schedules 100, 125 and 141 required', 'nothing for this schedule']);
check('schedule-11-shareholder-transactions-checker',
  { adv: 'y', pay: 'n', bal: 'y' },
  ['Something moved in the year', 'A transaction in the year']);
check('schedule-11-shareholder-transactions-checker',
  { adv: 'n', pay: 'y', bal: 'n' },
  ['Something moved in the year']);
check('schedule-11-shareholder-transactions-checker',
  { adv: 'n', pay: 'n', bal: 'n' },
  ['Nothing on either count']);
check('schedule-11-shareholder-transactions-checker', { adv: 'n' },
  ['2 of the three questions are still unanswered']);

// ---------------------------------------------------------------- decoys
decoy('rule 8 dropped where Quebec applies', function () {
  check('permanent-establishment-checker', { qc: 'y', ab: 'n', only: 'n' },
    [], ['separate return']);
});
decoy('an unanswered question yields a verdict', function () {
  check('carrying-on-business-in-canada-checker', { bank: 'y', trade: 'n' },
    ['Holding, not carrying on business']);
});
decoy('the non-resident charge shown without the cap', function () {
  check('non-resident-corporation-filing-checker',
    { own: 'y', inc: 'y', act: 'n' }, [], ['$2,500.00']);
});
decoy('a future year-end silently counted', function () {
  check('outstanding-returns-count-checker', { last: '2035-01-31', same: 'y' },
    ['returns outstanding']);
});

console.log('\n' + pass + ' passed, ' + fail + ' failed');
if (fail) { process.exit(1); }
