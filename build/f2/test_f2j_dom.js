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


// ------------------------------------------------------------- 71 rejection
check('efile-rejection-reason-checker', { nm: 'y', ye: 'y', bn: 'y', fl: 'n' },
  ['None of the four common causes is present',
   'The legal name matches the register',
   'The Business Number is the one on the corporation record',
   'one corrected transmission is included in $300.00 plus HST per tax year']);
check('efile-rejection-reason-checker', { nm: 'n', ye: 'y', bn: 'y', fl: 'n' },
  ['1 cause to clear', 'The legal name does not match the register',
   'corporation number and the suffix'],
  ['None of the four']);
check('efile-rejection-reason-checker', { nm: 'n', ye: 'n', bn: 'n', fl: 'n' },
  ['3 causes to clear', 'does not match the record the Agency holds',
   'is not the one on the corporation record']);
check('efile-rejection-reason-checker', { nm: 'y', ye: 'y', bn: 'y', fl: 'y' },
  ['already been filed and assessed', 'adjustment to it']);
check('efile-rejection-reason-checker', { nm: 'y', ye: 'y' },
  ['of the four questions'], ['cause to clear']);

// ---------------------------------------------------------- 72 expenses only
check('expenses-only-year-checker', { rv: 'n', it: 'n', ex: 'y' },
  ['Costs alone leave the year nil', 'GIFI Schedules 100, 125 and 141',
   'Does not end the nil year'],
  ['gondaliyacpa.ca']);
check('expenses-only-year-checker', { rv: 'n', it: 'n', ex: 'n' },
  ['Costs alone leave the year nil', 'nothing in and nothing out']);
check('expenses-only-year-checker', { rv: 'y', it: 'n', ex: 'y' },
  ['year is not nil', 'Ends the nil year', 'gondaliyacpa.ca',
   '$350.00 plus HST per year']);
check('expenses-only-year-checker', { rv: 'n', it: 'y', ex: 'n' },
  ['Investment income, so the year is not nil', 'gondaliyacpa.ca']);
check('expenses-only-year-checker', { rv: 'n', it: 'n' },
  ['Answer the three questions above'], ['nil year']);

// ------------------------------------------------------------ 73 never traded
// Dates computed independently: 2025-06-10 plus 370 days is June 15, 2026, and
// six months on from a mid-month year-end is December 15, 2026, a Tuesday.
check('never-traded-corporation-checker', { ic: '2025-06-10', ac: 'n', fi: 'n' },
  ['June 10, 2025', 'June 15, 2026', 'December 15, 2026', 'Schedule 24',
   '53 weeks', 'stays open forever'],
  ['Received on time where']);
// 2024-01-02 plus 370 days is January 6, 2025; six months on is July 6, 2025,
// a Sunday, so the business-day row must appear with July 7, 2025.
check('never-traded-corporation-checker', { ic: '2024-01-02', ac: 'n', fi: 'n' },
  ['January 6, 2025', 'July 6, 2025', 'Received on time', 'July 7, 2025']);
check('never-traded-corporation-checker', { ic: '2025-06-10', ac: 'y', fi: 'n' },
  ['not a never-traded year', 'gondaliyacpa.ca']);
check('never-traded-corporation-checker', { ic: '2025-06-10', ac: 'n', fi: 'y' },
  ['ordinary cycle', 'six months after it'],
  ['stays open forever']);
check('never-traded-corporation-checker', { ic: '', ac: 'n', fi: 'n' },
  ['Enter the incorporation date'], ['Schedule 24']);

// -------------------------------------------------------------- 74 restarting
check('restarting-a-dormant-corporation-checker', { rs: 'n', rv: 'n', qy: 'n' },
  ['Still dormant, so every year is a nil year', 'The current year'],
  ['gondaliyacpa.ca']);
check('restarting-a-dormant-corporation-checker', { rs: 'y', rv: 'y', qy: 'y' },
  ['The year it restarted is not a nil year', 'gondaliyacpa.ca',
   '$350.00 plus HST per year', 'oldest first', 'stays open forever']);
check('restarting-a-dormant-corporation-checker', { rs: 'y', rv: 'n', qy: 'n' },
  ['nothing has come in yet', 'Filed here while the year stays quiet'],
  ['stays open forever']);
check('restarting-a-dormant-corporation-checker', { rs: 'y', qy: 'y' },
  ['Answer the questions above'], ['nil year']);

// ---------------------------------------------------------- 75 loss continuity
check('loss-continuity-on-a-nil-return-checker', { pl: 'n', lf: 'n', cn: 'y' },
  ['No earlier loss to carry', 'reports a nil balance'],
  ['oldest first']);
check('loss-continuity-on-a-nil-return-checker', { pl: 'y', lf: 'n', cn: 'y' },
  ['not established until its own year is filed', 'oldest first',
   'stays open forever']);
check('loss-continuity-on-a-nil-return-checker', { pl: 'y', lf: 'y', cn: 'y' },
  ['The loss is established', 'claims nothing against the loss',
   'Schedule 8 and the loss continuity schedule are inside'],
  ['stays open forever']);
check('loss-continuity-on-a-nil-return-checker', { pl: 'y', lf: 'y', cn: 'n' },
  ['not one we file here', 'gondaliyacpa.ca']);
check('loss-continuity-on-a-nil-return-checker', { pl: 'y', cn: 'y' },
  ['Answer the questions above']);

// ------------------------------------------------------ 76 multiple corporations
check('multiple-corporation-filing-cost-calculator', { nc: 3, ny: 3, sm: 'y' },
  ['9 nil returns', '$2,700.00 before tax', 'same date'],
  ['dates to hold rather than one']);
check('multiple-corporation-filing-cost-calculator', { nc: 1, ny: 1, sm: 'n' },
  ['1 nil return,', '$300.00 before tax', 'dates to hold rather than one'],
  ['1 nil returns']);
check('multiple-corporation-filing-cost-calculator', { nc: 20, ny: 10, sm: 'y' },
  ['200 nil returns', '$60,000.00 before tax']);
check('multiple-corporation-filing-cost-calculator', { nc: 99, ny: 1, sm: 'y' },
  ['Enter 1 to 20 corporations'], ['nil return']);
check('multiple-corporation-filing-cost-calculator', { nc: 'x', ny: 1, sm: 'y' },
  ['Enter whole numbers'], ['nil return']);
check('multiple-corporation-filing-cost-calculator', { nc: '', ny: '', sm: 'y' },
  ['Enter both counts']);

// ------------------------------------------------------- 77 post dissolution
// 2026-03-31 is a month end, so six months on is September 30, 2026, a
// Wednesday: no business-day row.
check('post-dissolution-return-checker', { dd: '2026-03-31', fn: 'n', ea: 'y' },
  ['March 31, 2026', 'September 30, 2026', 'the final T2',
   'No tax year arises', 'oldest first', 'stays open forever'],
  ['Received on time by']);
check('post-dissolution-return-checker', { dd: '2026-06-30', fn: 'y', ea: 'n' },
  ['Nothing further arises after the dissolution date', 'December 31, 2026',
   'last one the corporation owes'],
  ['stays open forever']);
check('post-dissolution-return-checker', { dd: '2025-12-31', fn: 'n', ea: 'n' },
  ['June 30, 2026', 'nil return at $300.00 plus HST per tax year']);
check('post-dissolution-return-checker', { dd: '', fn: 'n', ea: 'n' },
  ['Enter the dissolution date'], ['No tax year arises']);

// ---------------------------------------------------------- 78 acquired corp
// 2015-02-01 to 2021-08-15 is 2388 days inclusive, which is 6 whole years.
check('acquired-corporation-unfiled-years-checker',
  { ic: '2015-02-01', aq: '2021-08-15', fl: 'n' },
  ['came with the corporation', 'February 1, 2015', 'August 15, 2021',
   '6 tax years', 'oldest first', 'stays open forever',
   'filing question only']);
check('acquired-corporation-unfiled-years-checker',
  { ic: '2015-02-01', aq: '2021-08-15', fl: 'y' },
  ['record is current', 'ordinary cycle'],
  ['stays open forever']);
check('acquired-corporation-unfiled-years-checker',
  { ic: '2021-08-15', aq: '2015-02-01', fl: 'n' },
  ['cannot fall before the incorporation date'], ['tax years']);
check('acquired-corporation-unfiled-years-checker',
  { ic: '2015-02-01', aq: '', fl: 'n' },
  ['Enter both dates']);

// ------------------------------------------------------- 79 sole shareholder
check('sole-shareholder-corporation-checker', { on: 'y', sh: 'y', ln: 'n' },
  ['One shareholder holds 100 per cent', 'Schedule 50',
   'Share capital issued at incorporation']);
check('sole-shareholder-corporation-checker', { on: 'n', sh: 'n', ln: 'y' },
  ['the 10 per cent test decides', 'shareholder loan balance',
   'does not stop the year being nil']);
check('sole-shareholder-corporation-checker', { on: 'y', sh: 'n', ln: 'n' },
  ['Nothing reported on the books in the year'],
  ['Share capital issued']);
check('sole-shareholder-corporation-checker', { on: 'y', sh: 'y' },
  ['Answer the three questions above']);

// ------------------------------------------------------------- 80 two numbers
check('business-number-versus-corporation-number-checker',
  { bn: 'y', cn: 'y', nm: 'y' },
  ['You have both identifiers', 'The T2 corporate income tax return',
   'The registry annual return', 'Matches'],
  ['cannot be transmitted without']);
check('business-number-versus-corporation-number-checker',
  { bn: 'n', cn: 'y', nm: 'y' },
  ['The T2 needs the Business Number, which you do not have yet',
   'confirm the number against the corporation record']);
check('business-number-versus-corporation-number-checker',
  { bn: 'y', cn: 'y', nm: 'n' },
  ['Does not match', 'refused transmission', 'e-filing rejection']);
check('business-number-versus-corporation-number-checker',
  { bn: 'y', cn: 'n' },
  ['Answer the three questions above']);

console.log('\n' + pass + ' passed, ' + fail + ' failed');
if (fail) { process.exit(1); }
