// Renders every batch 7 result screen by executing each page's shipped module
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


// Every date and total asserted below was computed independently in Python
// against the same month-end and anniversary rules before it was written
// here. Where a page and my expectation disagreed, the page was read first.

// ---- 51 is a return owed at all ------------------------------------------
check('t2-filing-requirement-checker', { ex: 'n', di: 'n', ac: 'n' },
  ['No T2 is owed for a year the corporation did not exist in',
   'not an unfiled year'],
  ['A T2 is owed for this year']);
check('t2-filing-requirement-checker', { ex: 'y', di: 'n', ac: 'n' },
  ['A T2 is owed for this year', 'The figures are zero. The return is still owed',
   'nil return', '$300.00 plus HST per tax year'],
  ['final one']);
check('t2-filing-requirement-checker', { ex: 'y', di: 'y', ac: 'n' },
  ['and it is the final one', 'the final T2',
   'leaves those years open behind it']);
check('t2-filing-requirement-checker', { ex: 'y', di: 'n', ac: 'y' },
  ['may not be nil', 'gondaliyacpa.ca']);

// ---- 52 which schedules --------------------------------------------------
// Nothing on the books and not a first return: the GIFI permission holds and
// no other schedule is triggered, so every row reads not required.
check('required-schedules-checker',
  { fr: 'n', sc: 'n', ca: 'n', ln: 'n', ex: 'n', s5: 'n', d8: 'n' },
  ['No schedule is triggered', 'May be omitted',
   'Inactive all year with nothing to report'],
  ['Required |']);
// Share capital alone withdraws the GIFI permission.
check('required-schedules-checker',
  { fr: 'n', sc: 'y', ca: 'n', ln: 'n', ex: 'n', s5: 'n', d8: 'n' },
  ['1 schedule group on the return', 'On the books: share capital',
   'GIFI Schedules 100, 125 and 141 | Required']);
// All seven yes: four groups, each with its reason.
check('required-schedules-checker',
  { fr: 'y', sc: 'y', ca: 'y', ln: 'y', ex: 'y', s5: 'y', d8: 'y' },
  ['4 schedule groups on the return', 'It is the first return',
   'A shareholder holds 10 percent or more',
   'Depreciable property or a loss carried forward',
   'share capital, cash or a bank account, a shareholder loan balance']);
// A bank charge on its own is enough, which is the point of the five.
check('required-schedules-checker',
  { fr: 'n', sc: 'n', ca: 'n', ln: 'n', ex: 'y', s5: 'n', d8: 'n' },
  ['On the books: an incorporation cost or a bank charge']);

// ---- 53 share capital ----------------------------------------------------
check('share-capital-reporting-checker', { sc: 'y', s5: 'n', dv: 'n' },
  ['Share capital makes the GIFI schedules required',
   'GIFI Schedules 100, 125 and 141 are required',
   'does not stop a year being nil'],
  ['Schedule 50 for every such shareholder']);
check('share-capital-reporting-checker', { sc: 'y', s5: 'y', dv: 'n' },
  ['Schedule 50 for every such shareholder',
   'names every one of them rather than the largest']);
// A dividend takes the year out of nil and routes to the other firm's rate.
check('share-capital-reporting-checker', { sc: 'y', s5: 'y', dv: 'y' },
  ['A dividend means the year is not nil', 'The year is not nil',
   '$350.00 plus HST per year']);
check('share-capital-reporting-checker', { sc: 'n', s5: 'n', dv: 'n' },
  ['No share capital reported', 'check the incorporation documents']);

// ---- 54 shareholder loan -------------------------------------------------
// The case the page exists for: a balance that never moved.
check('shareholder-loan-balance-checker', { bal: 'y', mv: 'n', ot: 'n' },
  ['GIFI Schedules 100, 125 and 141 are required',
   'A balance is something to report',
   'A balance carried without movement still counts',
   'tax treatment of a shareholder loan is a different matter']);
check('shareholder-loan-balance-checker', { bal: 'n', mv: 'n', ot: 'n' },
  ['Nothing here makes the GIFI schedules required',
   'No loan balance on these answers']);
check('shareholder-loan-balance-checker', { bal: 'n', mv: 'n', ot: 'y' },
  ['GIFI Schedules 100, 125 and 141 are required',
   'Required on that ground as well']);
check('shareholder-loan-balance-checker', { bal: 'y', mv: 'y', ot: 'n' },
  ['Movement is reported, and does not change the answer above']);

// ---- 55 Schedule 125 -----------------------------------------------------
// A bank charge with no revenue: a figure on a schedule people expect blank.
check('gifi-schedule-125-checker', { rev: 'n', bank: 'y', bs: 'n' },
  ['Schedule 125 goes on the return', 'A figure on the expense side',
   'A bank charge with no revenue is the fact pattern'],
  ['carrying zeros']);
check('gifi-schedule-125-checker', { rev: 'n', bank: 'n', bs: 'y' },
  ['Schedule 125 goes on the return, carrying zeros',
   'stand or fall together']);
check('gifi-schedule-125-checker', { rev: 'n', bank: 'n', bs: 'n' },
  ['Schedule 125 may be omitted', 'nothing withdraws that permission']);
check('gifi-schedule-125-checker', { rev: 'y', bank: 'y', bs: 'y' },
  ['revenue and a bank charge or another expense']);

// ---- 56 Schedule 141 -----------------------------------------------------
check('gifi-schedule-141-checker', { tr: 'y', ou: 'y', asu: 'n' },
  ['Schedule 141 goes on the return', 'An outside preparer',
   'Neither audited nor reviewed',
   'registered EFILE electronic filer']);
check('gifi-schedule-141-checker', { tr: 'n', ou: 'n', asu: 'n' },
  ['Schedule 141 may be omitted', 'Prepared within the corporation'],
  ['All three GIFI schedules are required']);
check('gifi-schedule-141-checker', { tr: 'y', ou: 'y', asu: 'y' },
  ['An assurance engagement was performed'],
  ['Neither audited nor reviewed is the ordinary answer']);

// ---- 57 dormant obligations ----------------------------------------------
// Federal with both accounts open: four rows, and RC145 named.
check('dormant-corporation-obligation-checker',
  { fed: 'y', pay: 'y', gst: 'y' },
  ['4 obligations while the corporation stays open',
   'within 60 days of the incorporation anniversary',
   '$12.00 government fee', 'Form RC145',
   'An inactive T2 does not close them']);
check('dormant-corporation-obligation-checker',
  { fed: 'n', pay: 'n', gst: 'n' },
  ['2 obligations while the corporation stays open',
   'A registry annual return', 'as short as it gets'],
  ['Form RC145', '$12.00']);
check('dormant-corporation-obligation-checker',
  { fed: 'y', pay: 'y', gst: 'n' },
  ['3 obligations while the corporation stays open',
   'T4 information returns and nil remittances',
   'An inactive T2 does not close it'],
  ['GST/HST returns, including nil ones']);

// ---- 58 annual return versus tax return ----------------------------------
check('annual-return-vs-tax-return-checker', { fed: 'y', prov: 'n' },
  ['2 separate filings', 'The T2, a tax return',
   'The federal annual return, a registry filing',
   'Within 60 days of the incorporation anniversary',
   '$12.00, a government fee to which HST does not apply',
   'struck from the register'],
  ['3 separate filings']);
check('annual-return-vs-tax-return-checker', { fed: 'n', prov: 'y' },
  ['3 separate filings', 'The registry annual return',
   'adds a filing rather than replacing one'],
  ['$12.00']);
// The floor is two. A provincially incorporated corporation with no outside
// registration still owes its own registry an annual return, and an earlier
// build of this page reported one filing here.
check('annual-return-vs-tax-return-checker', { fed: 'n', prov: 'n' },
  ['2 separate filings', "On the registry's own schedule"],
  ['1 separate filing']);

// ---- 59 dissolve or keep filing ------------------------------------------
// 5 years at $300.00 is $1,500.00; 5 federal annual returns at $12.00 is
// $60.00. Both computed in Python first.
check('dissolve-or-keep-filing-cost-calculator', { n: 5, fed: 'y', beh: 'n' },
  ['5 years of filing is $1,500.00 plus HST',
   '$60.00 in annual return fees', 'Keep filing for 5 years',
   'Wind it up now', 'A clearance certificate request Outside the fee',
   'One side of that table totals and the other does not'],
  ['stays open forever']);
check('dissolve-or-keep-filing-cost-calculator', { n: 1, fed: 'n', beh: 'n' },
  ['1 year of filing is $300.00 plus HST',
   '1 registry annual return', 'the same decision again in 1 year'],
  ['in annual return fees']);
// Years already behind: both routes start with them, and the rule 3
// qualification must appear whole.
check('dissolve-or-keep-filing-cost-calculator', { n: 3, fed: 'y', beh: 'y' },
  ['3 years of filing is $900.00 plus HST',
   'Both routes start by filing them', 'stays open forever',
   '$25.00 per day up to $2,500.00']);
check('dissolve-or-keep-filing-cost-calculator', { n: 21, fed: 'y', beh: 'n' },
  ['between 1 and 20']);

// ---- 60 federal annual return fees ---------------------------------------
// Incorporated June 15, 2020, three years listed. Anniversaries June 15 of
// 2021, 2022 and 2023; each deadline 60 days later is August 14. Total $36.00.
check('federal-annual-return-fee-calculator', { inc: '2020-06-15', n: 3 },
  ['$36.00 over 3 years, with no HST on any of it',
   'June 15, 2021 | August 14, 2021',
   'June 15, 2022 | August 14, 2022',
   'June 15, 2023 | August 14, 2023',
   'not covered by the nil T2 fee'],
  ['plus HST over']);
// A February 29 incorporation: the anniversary falls back to February 28 in
// a common year, which addYear handles. 2020-02-29 -> 2021-02-28.
check('federal-annual-return-fee-calculator', { inc: '2020-02-29', n: 2 },
  ['$24.00 over 2 years',
   'February 28, 2021 | April 29, 2021']);
check('federal-annual-return-fee-calculator', { inc: '2020-06-15', n: 0 },
  ['between 1 and 20']);

console.log('\n' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
