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
  // (the tally is incremented once, after the tag-balance loop. It was done here
  // as well until 2026-11-05, so every check counted twice and this suite
  // reported 42 passed for 21 checks.)
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

// Tool 88 counts tax year-ends up to today, so the expected figure is derived
// here with the same arithmetic rather than hard-coded to one run date.
function yearEndsSince(y, m, d) {
  const now = new Date();
  const today = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
  let n = 0;
  for (let i = 1; i <= 40; i++) {
    if (Date.UTC(y + i, m, d) > today) break;
    n++;
  }
  return n;
}

// ---- 86. Ontario Business Registry filings -----------------------------
check('ontario-business-registry-filing-checker',
  { ar: 'y', addr: 'n', dir: 'n', key: 'n' },
  ['1 filing through the Ontario Business Registry', 'The Ontario annual return',
   'needs its Ontario corporation number'],
  ['2 filings']);
check('ontario-business-registry-filing-checker',
  { ar: 'y', addr: 'y', dir: 'y', key: 'y' },
  ['3 filings through the Ontario Business Registry',
   'A change of registered office address', 'A change of directors or officers',
   'You have the corporation number']);
check('ontario-business-registry-filing-checker',
  { ar: 'n', addr: 'n', dir: 'n', key: 'y' },
  ['Nothing on this list is outstanding']);
check('ontario-business-registry-filing-checker', { ar: 'y' },
  ['3 of the four questions are still unanswered']);

// ---- 87. Schedule 546 --------------------------------------------------
check('schedule-546-ontario-annual-return-checker', { ye: '2021-06-30' },
  ['That year travelled with the T2', 'before October 2021', 'Yes'],
  ['goes through the Ontario Business Registry<']);
// The cutover month itself is on the registry side, not the T2 side.
check('schedule-546-ontario-annual-return-checker', { ye: '2021-10-01' },
  ['That year goes through the Ontario Business Registry', 'from October 2021'],
  ['travelled with the T2<']);
check('schedule-546-ontario-annual-return-checker', { ye: '2026-06-30' },
  ['goes through the Ontario Business Registry',
   'nothing in the corporate tax return now prompts an owner']);
check('schedule-546-ontario-annual-return-checker', { ye: '' },
  ['Enter the tax year-end above']);
check('schedule-546-ontario-annual-return-checker', { ye: 'not-a-date' },
  ['not a date we can read']);

// ---- 88. Ontario missed annual returns --------------------------------
const n21 = yearEndsSince(2021, 11, 31);          // Dec 31 2021 onwards
check('ontario-missed-annual-returns-calculator', { last: '2021-12-31' },
  [n21 + ' annual returns outstanding', 'December 31, 2021 | Filed',
   'Outstanding', 'does not create tax']);
// A year-end in the past whose anniversary has not come round yet owes
// nothing. Computed 60 days back so the case stays valid as the date moves.
const recent = new Date(Date.now() - 60 * 86400000)
  .toISOString().slice(0, 10);
check('ontario-missed-annual-returns-calculator', { last: recent },
  ['Nothing outstanding yet', 'Not yet reached']);
check('ontario-missed-annual-returns-calculator', { last: '2099-01-01' },
  ['That date is in the future']);
check('ontario-missed-annual-returns-calculator', { last: '' },
  ['Enter the tax year-end of the last annual return']);

// ---- 89. Extra-provincial registration --------------------------------
check('extra-provincial-registration-checker',
  { fed: 'y', ont: 'y', oth: 'n', pe: 'n' },
  ['2 filings outside the T2', 'Corporations Canada',
   'The Ontario Business Registry', 'files both',
   'does not remove the provincial obligation']);
check('extra-provincial-registration-checker',
  { fed: 'n', ont: 'n', oth: 'y', pe: 'y' },
  ['2 filings outside the T2', 'Alberta or Quebec',
   'Income tax return, not an annual return',
   'collected through the federal T2']);
check('extra-provincial-registration-checker',
  { fed: 'n', ont: 'n', oth: 'n', pe: 'n' },
  ['Nothing on this list applies'],
  ['filings outside the T2']);
check('extra-provincial-registration-checker', { fed: 'y', ont: 'y' },
  ['2 of the four questions are still unanswered']);

// ---- 90. Corporate revival --------------------------------------------
check('corporate-revival-requirement-checker',
  { struck: 'y', years: 'y', wind: 'y' },
  ['Struck, not wound up', 'Survived the striking and are waiting',
   'worst of both positions', 'revived first',
   'cancels no outstanding T2 return']);
check('corporate-revival-requirement-checker',
  { struck: 'y', years: 'n', wind: 'n' },
  ['Struck, not wound up', 'the striking cancelled nothing either way',
   'no intention to wind it up'],
  ['worst of both positions']);
check('corporate-revival-requirement-checker',
  { struck: 'n', years: 'y', wind: 'n' },
  ['Revival does not arise', 'Still owed to the registry',
   'Yes, and still open'],
  ['Struck, not wound up']);
check('corporate-revival-requirement-checker', { struck: 'y' },
  ['2 of the three questions are still unanswered']);

console.log('\n' + pass + ' passed, ' + fail + ' failed');
if (fail) { process.exit(1); }
