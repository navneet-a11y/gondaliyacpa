/*! WealthScale widgets v1.0 | October 22, 2026 | (c) WealthScale Media Inc.
 * One file, loaded site-wide. Place <div data-ws-widget="NAME"></div> in any page.
 * All figures live in the WS_DATA block below. Update a figure there once and every page updates.
 * General information only. Not financial, investment, tax or legal advice.
 */
(function () {
  'use strict';

  /* =====================================================================
   * 1. DATA: every figure the widgets use. EDIT FIGURES HERE ONLY.
   * ===================================================================== */
  var D = /*@@DATA@@*/{};
  window.WS_DATA = D;

  /* =====================================================================
   * 2. HELPERS
   * ===================================================================== */
  var NOW = new Date();
  var CUR = D.year || NOW.getFullYear();
  var uid = 0;
  function nf(n, d) { return Number(n).toLocaleString('en-CA', { minimumFractionDigits: d || 0, maximumFractionDigits: d || 0 }); }
  function money(n, d) { if (!isFinite(n)) return '$0'; var s = '$' + nf(Math.abs(n), d || 0); return n < 0 ? '−' + s : s; }
  function money2(n) { return money(n, 2); }
  function pct(x, d) { return nf(x * 100, d == null ? 2 : d) + '%'; }
  function num(v) { if (v == null) return 0; var n = parseFloat(String(v).replace(/[^0-9.\-]/g, '')); return isFinite(n) ? n : 0; }
  function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function sum(a) { return a.reduce(function (s, x) { return s + x; }, 0); }
  function fmtDate(iso, opt) {
    var p = String(iso).split('-'); var dt = new Date(+p[0], +p[1] - 1, +p[2]);
    return dt.toLocaleDateString('en-CA', opt || { year: 'numeric', month: 'long', day: 'numeric' });
  }
  function daysUntil(iso) {
    var p = String(iso).split('-'); var dt = new Date(+p[0], +p[1] - 1, +p[2]);
    var t = new Date(NOW.getFullYear(), NOW.getMonth(), NOW.getDate());
    return Math.round((dt - t) / 86400000);
  }
  var MEM = (function () {
    var k = 'ws_mem_v1', o = {};
    try { o = JSON.parse(window.localStorage.getItem(k) || '{}') || {}; } catch (e) { o = {}; }
    return {
      get: function (n, d) { return o[n] != null ? o[n] : d; },
      set: function (n, v) { o[n] = v; try { window.localStorage.setItem(k, JSON.stringify(o)); } catch (e) { /* storage unavailable */ } }
    };
  })();
  function track(name, detail) {
    try { document.dispatchEvent(new CustomEvent('ws:calc', { detail: { widget: name, data: detail || {} } })); } catch (e) { /* old browser */ }
    try { if (window.gtag) window.gtag('event', 'ws_calc', { widget: name }); } catch (e) { /* no analytics */ }
  }

  /* ---------- form field builders ---------- */
  function F(p) { return p.id; }
  function fNum(p, id, label, val, o) {
    o = o || {};
    return '<div class="ws-field"><label for="' + p + id + '">' + label + '</label>' +
      '<input type="number" inputmode="decimal" id="' + p + id + '" name="' + id + '" value="' + (val == null ? '' : val) + '"' +
      (o.min != null ? ' min="' + o.min + '"' : '') + (o.max != null ? ' max="' + o.max + '"' : '') +
      ' step="' + (o.step || 'any') + '"' + (o.ph ? ' placeholder="' + esc(o.ph) + '"' : '') + '>' +
      (o.help ? '<small>' + o.help + '</small>' : '') + '</div>';
  }
  function fTxt(p, id, label, val, o) {
    o = o || {};
    return '<div class="ws-field"><label for="' + p + id + '">' + label + '</label>' +
      '<input type="text" id="' + p + id + '" name="' + id + '" value="' + esc(val || '') + '"' + (o.ph ? ' placeholder="' + esc(o.ph) + '"' : '') + '>' +
      (o.help ? '<small>' + o.help + '</small>' : '') + '</div>';
  }
  function fSel(p, id, label, opts, val, o) {
    o = o || {};
    var h = '<div class="ws-field"><label for="' + p + id + '">' + label + '</label><select id="' + p + id + '" name="' + id + '">';
    opts.forEach(function (x) { var v = Array.isArray(x) ? x[0] : x, t = Array.isArray(x) ? x[1] : x; h += '<option value="' + esc(v) + '"' + (String(v) === String(val) ? ' selected' : '') + '>' + esc(t) + '</option>'; });
    return h + '</select>' + (o.help ? '<small>' + o.help + '</small>' : '') + '</div>';
  }
  function fRadio(p, id, label, opts, val) {
    var h = '<div class="ws-field" role="radiogroup" aria-label="' + esc(label) + '"><span class="ws-flabel">' + label + '</span><div class="ws-radio">';
    opts.forEach(function (x) { h += '<label><input type="radio" name="' + p + id + '" value="' + esc(x[0]) + '"' + (String(x[0]) === String(val) ? ' checked' : '') + '> ' + esc(x[1]) + '</label>'; });
    return h + '</div></div>';
  }
  function provOpts() { return D.provinces.map(function (p) { return [p[0], p[1]]; }); }
  function yearOpts(a, b) { var o = []; for (var y = b; y >= a; y--) o.push([y, String(y)]); return o; }

  /* ---------- widget shell ---------- */
  function shell(el, name, cfg) {
    var p = 'ws' + (++uid) + '-';
    el.classList.add('ws-widget');
    if (!el.id) el.id = 'ws-' + name;
    var fields = typeof cfg.fields === 'function' ? cfg.fields(p) : cfg.fields;
    el.innerHTML =
      '<div class="ws-w-head"><div class="ws-w-title" role="heading" aria-level="3">' + cfg.title + '</div>' + (cfg.intro ? '<p>' + cfg.intro + '</p>' : '') + '</div>' +
      '<div class="ws-w-body"><form novalidate onsubmit="return false">' + fields +
      (cfg.button === false ? '' : '<div class="ws-w-actions"><button type="submit" class="ws-w-btn">' + (cfg.button || 'Calculate') + '</button>' +
        '<button type="reset" class="ws-w-btn ws-secondary">Reset</button></div>') +
      '</form><div class="ws-result" aria-live="polite"></div></div>' +
      '<div class="ws-w-foot">' + (cfg.foot || ('Figures as of ' + fmtDate(D.asOf) + '. General information only, not personal financial, tax or investment advice.')) + '</div>';
    var form = el.querySelector('form'), out = el.querySelector('.ws-result');
    function val(id) { var n = form.querySelector('[name="' + id + '"]'); if (n) return n.value; var r = form.querySelector('input[name="' + p + id + '"]:checked'); return r ? r.value : ''; }
    function set(id, v) { var n = form.querySelector('[name="' + id + '"]'); if (n) n.value = v; }
    var api = { p: p, el: el, form: form, out: out, val: val, n: function (id) { return num(val(id)); }, set: set };
    var timer;
    function run(e) {
      try {
        var html = cfg.calc(api, e);
        if (html != null) out.innerHTML = html + nextLinks(cfg.next);
      } catch (err) { out.innerHTML = '<div class="ws-msg ws-err">Please check your entries and try again.</div>'; if (window.console) console.error(err); }
    }
    form.addEventListener('submit', function (e) { e.preventDefault(); run(e); track(name); });
    form.addEventListener('input', function (e) { clearTimeout(timer); timer = setTimeout(function () { run(e); }, 250); });
    form.addEventListener('change', function (e) { clearTimeout(timer); timer = setTimeout(function () { run(e); }, 50); });
    form.addEventListener('reset', function () { setTimeout(function () { out.innerHTML = ''; if (cfg.auto) run(); }, 10); });
    if (cfg.init) cfg.init(api);
    if (cfg.auto !== false) run();
    return api;
  }
  function nextLinks(list) {
    if (!list || !list.length) return '';
    return '<div class="ws-next">Next: ' + list.map(function (x) { return '<a href="' + x[0] + '">' + x[1] + '</a>'; }).join(' &middot; ') + '</div>';
  }
  function kv(items) { return '<div class="ws-kv">' + items.map(function (x) { return '<div><span>' + x[0] + '</span><b>' + x[1] + '</b></div>'; }).join('') + '</div>'; }
  function head(label, value, neg) { return '<p class="ws-headline">' + label + '</p><p class="ws-answer' + (neg ? ' ws-neg' : '') + '">' + value + '</p>'; }
  function msg(type, text) { return '<div class="ws-msg ws-' + type + '">' + text + '</div>'; }
  function how(text) { return '<details class="ws-how"><summary>How this is worked out</summary><div>' + text + '</div></details>'; }
  function table(headers, rows, cap) {
    return '<div class="ws-table-wrap"><table>' + (cap ? '<caption>' + cap + '</caption>' : '') + '<thead><tr>' + headers.map(function (h) { return '<th scope="col">' + h + '</th>'; }).join('') +
      '</tr></thead><tbody>' + rows.map(function (r) { return '<tr>' + r.map(function (c) { return '<td>' + c + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div>';
  }
  function bars(series, labels) {
    var max = Math.max.apply(null, series.map(function (s) { return s.total; }).concat([1]));
    return '<div class="ws-bars" aria-hidden="true">' + series.map(function (s) {
      return '<i style="height:' + (s.total / max * 100).toFixed(1) + '%" title="' + esc(s.label) + '"><b style="height:' + (s.total ? (s.part / s.total * 100) : 0).toFixed(1) + '%"></b></i>';
    }).join('') + '</div><div class="ws-legend"><span><i style="background:var(--ws-copper)"></i>' + labels[0] + '</span><span><i style="background:var(--ws-step2)"></i>' + labels[1] + '</span></div>';
  }

  /* =====================================================================
   * 3. CALCULATION ENGINES (pure functions, exposed as WS.calc for testing)
   * ===================================================================== */
  var C = {};

  /* ---------- income tax ---------- */
  C.bracketTax = function (br, inc) {
    var t = 0, lo = 0;
    for (var i = 0; i < br.length; i++) {
      var hi = br[i][0] == null ? Infinity : br[i][0], r = br[i][1];
      if (inc > lo) t += (Math.min(inc, hi) - lo) * r;
      lo = hi;
      if (inc <= hi) break;
    }
    return t;
  };
  C.fedBPA = function (inc) {
    var f = D.tax.federal, a = f.bpa, b = f.bpa_min, s = f.bpa_phase[0], e = f.bpa_phase[1];
    if (inc <= s) return a; if (inc >= e) return b;
    return a - (a - b) * (inc - s) / (e - s);
  };
  C.ohp = function (inc) {
    var bands = D.tax.provinces.ON.health_premium; // [[from, to, base, rate, cap]]
    for (var i = bands.length - 1; i >= 0; i--) {
      var b = bands[i];
      if (inc > b[0]) return Math.min(b[2] + (inc - b[0]) * b[3], b[4]);
    }
    return 0;
  };
  /* income: taxable income including grossed-up dividends and taxable capital gains.
     opts: {elig: grossed-up eligible dividends, nonelig: grossed-up non-eligible dividends} */
  C.tax = function (prov, inc, opts) {
    opts = opts || {};
    inc = Math.max(0, inc);
    var T = D.tax, f = T.federal, P = T.provinces[prov] || T.provinces.ON;
    var fLow = f.brackets[0][1];
    var fDTC = (opts.elig || 0) * T.dividends.federal_dtc_eligible + (opts.nonelig || 0) * T.dividends.federal_dtc_noneligible;
    var fed = C.bracketTax(f.brackets, inc) - C.fedBPA(inc) * fLow - fDTC;
    fed = Math.max(0, fed);
    if (prov === 'QC') fed = fed * (1 - T.qc_abatement);
    var pLow = P.brackets[0][1];
    var pd = (T.dividends.provincial_dtc[prov] || [0, 0]);
    var pDTC = (opts.elig || 0) * pd[0] + (opts.nonelig || 0) * pd[1];
    var pbpa = P.bpa;
    if (P.bpa_phase) { // e.g. Manitoba, Nova Scotia, Yukon: [start, end, minimum]
      var ps = P.bpa_phase[0], pe = P.bpa_phase[1], pm = P.bpa_phase[2];
      if (inc >= pe) pbpa = pm; else if (inc > ps) pbpa = P.bpa - (P.bpa - pm) * (inc - ps) / (pe - ps);
    }
    var pr = Math.max(0, C.bracketTax(P.brackets, inc) - pbpa * pLow - pDTC);
    var sur = 0;
    if (P.surtax) P.surtax.forEach(function (s) { if (pr > s[0]) sur += (pr - s[0]) * s[1]; });
    var hp = prov === 'ON' && P.health_premium ? C.ohp(inc) : 0;
    var total = fed + pr + sur + hp;
    return { federal: fed, provincial: pr + sur, surtax: sur, premium: hp, total: total, avg: inc > 0 ? total / inc : 0 };
  };
  C.marginal = function (prov, inc, kind) {
    var d = 100, base, up;
    if (kind === 'cg') { base = C.tax(prov, inc).total; up = C.tax(prov, inc + d * D.tax.capital_gains_inclusion).total; }
    else if (kind === 'elig' || kind === 'nonelig') {
      var g = kind === 'elig' ? D.tax.dividends.eligible_grossup : D.tax.dividends.noneligible_grossup;
      var o = {}; o[kind] = d * (1 + g);
      base = C.tax(prov, inc).total; up = C.tax(prov, inc + d * (1 + g), o).total;
    } else { base = C.tax(prov, inc).total; up = C.tax(prov, inc + d).total; }
    return (up - base) / d;
  };

  /* ---------- TFSA room ---------- */
  C.tfsaRoom = function (o) {
    // o: {birth, resident (year became resident or 0), nonres: [years], contrib (before this year), wdPrior (before this year), contribNow, wdNow}
    var L = D.tfsa.limits, start = Math.max(2009, o.birth + 18, o.resident || 0), rows = [], accrued = 0;
    for (var y = start; y <= CUR; y++) {
      var lim = L[y] || 0, skip = o.nonres.indexOf(y) >= 0;
      if (!skip) accrued += lim;
      rows.push([y, skip ? 0 : lim, accrued, skip]);
    }
    var startNow = accrued - o.contrib + o.wdPrior;
    var avail = startNow - o.contribNow;
    var nextLim = L[CUR + 1] || null;
    return { start: start, rows: rows, accrued: accrued, startOfYear: startNow, available: avail, next: nextLim != null ? avail + o.wdNow + nextLim : null, nextLim: nextLim, wdNow: o.wdNow };
  };

  /* ---------- RRSP ---------- */
  C.rrspRoom = function (earned, pa, carry, par) {
    var lim = D.rrsp.limits[CUR];
    var base = Math.min(earned * D.rrsp.pct, lim);
    return { base: base, limit: lim, room: Math.max(0, base - pa + par) + carry };
  };

  /* ---------- FHSA ---------- */
  C.fhsa = function (opened, contribByYear) {
    var F = D.fhsa, carry = 0, total = 0, rows = [];
    for (var y = opened; y <= CUR; y++) {
      var room = Math.min(F.annual + carry, F.lifetime - total);
      var c = contribByYear[y] || 0;
      rows.push([y, room, c]);
      if (y < CUR) { carry = clamp(room - c, 0, F.carry); total += c; }
    }
    var last = rows[rows.length - 1];
    var cNow = last ? last[2] : 0, roomNow = last ? last[1] : F.annual;
    var lifetimeLeft = F.lifetime - total - cNow;
    var nextCarry = clamp(roomNow - cNow, 0, F.carry);
    var nextRoom = Math.min(F.annual + nextCarry, Math.max(0, lifetimeLeft));
    return { rows: rows, roomNow: roomNow, leftNow: roomNow - cNow, lifetimeLeft: lifetimeLeft, nextRoom: nextRoom, totalPrior: total };
  };

  /* ---------- RESP grants ---------- */
  C.resp = function (o) {
    // o: {birth, prov, income, kids, annual, pastContrib, pastCesg, ret}
    var R = D.resp, age0 = CUR - o.birth, rows = [];
    var room = 0; for (var y = Math.max(o.birth, 2007); y <= CUR; y++) room += R.cesg_annual;
    room = Math.max(0, room - o.pastCesg);
    var cesgTot = o.pastCesg, contribTot = o.pastContrib, bal = o.pastContrib + o.pastCesg, extraTot = 0, clbTot = 0, provTot = 0;
    var yearsBy15 = 0, contribBy15 = o.pastContrib;
    var acesgRate = o.income <= R.acesg_income[0] ? R.acesg_rates[0] : (o.income <= R.acesg_income[1] ? R.acesg_rates[1] : 0);
    var clbOk = o.income <= R.clb_thresholds[Math.min(Math.max(1, o.kids), 5)];
    if (o.pastContrib >= R.cesg_age16_total) contribBy15 = o.pastContrib;
    for (var a = age0; a <= 17; a++) {
      var yr = o.birth + a;
      if (a > age0) room += R.cesg_annual;
      var c = o.annual;
      var eligible = a <= 15 || contribBy15 >= R.cesg_age16_total || yearsBy15 >= R.cesg_age16_years;
      var g = 0;
      if (eligible && yr >= 2007) g = Math.min(c * R.cesg_rate, Math.min(room, R.cesg_max_year), R.cesg_lifetime - cesgTot);
      g = Math.max(0, g);
      room -= g; cesgTot += g;
      var x = eligible ? Math.min(c, R.acesg_on_first) * acesgRate : 0;
      if (cesgTot >= R.cesg_lifetime) x = 0; // A-CESG counts toward the same lifetime limit
      x = Math.min(x, Math.max(0, R.cesg_lifetime - cesgTot));
      cesgTot += x; extraTot += x;
      var b = 0;
      if (clbOk && yr >= 2004 && a <= 15) { b = (clbTot === 0 ? R.clb_first : R.clb_yearly); b = Math.min(b, R.clb_max - clbTot); clbTot += b; }
      var pg = 0;
      if (o.prov === 'QC') { pg = Math.min(c * R.qesi_rate, R.qesi_annual, R.qesi_lifetime - provTot); provTot += pg; }
      if (o.prov === 'BC' && a >= 6 && a <= 9 && provTot === 0 && o.birth >= 2006) { pg = R.bctesg; provTot += pg; }
      contribTot += c; if (a <= 15) { contribBy15 += c; if (c >= 100) yearsBy15++; }
      bal = bal * (1 + o.ret) + c + g + x + b + pg;
      rows.push([yr, a, c, g + x, b, pg, bal]);
    }
    return { rows: rows, cesg: cesgTot - o.pastCesg, extra: extraTot, clb: clbTot, prov: provTot, contrib: contribTot, bal: bal, thisYear: rows[0] };
  };

  /* ---------- RRIF ---------- */
  C.rrifFactor = function (age) {
    if (age < 71) return 1 / (90 - age);
    if (age >= 95) return D.rrif.factors[95];
    return D.rrif.factors[age];
  };

  /* ---------- growth ---------- */
  C.grow = function (pv, pmtMonthly, rateAnnual, years, comp) {
    // comp: compounding periods per year (1, 2, 4, 12, 365). Contributions monthly at month end.
    var m = Math.round(years * 12), bal = pv, contrib = pv, rows = [];
    var er = Math.pow(1 + rateAnnual / comp, comp / 12) - 1; // effective monthly rate
    for (var i = 1; i <= m; i++) {
      bal = bal * (1 + er) + pmtMonthly; contrib += pmtMonthly;
      if (i % 12 === 0 || i === m) rows.push([Math.ceil(i / 12), contrib, bal]);
    }
    return { bal: bal, contrib: contrib, interest: bal - contrib, rows: rows };
  };

  /* ---------- broker cost ---------- */
  C.brokerAnnual = function (b, o) {
    // o: {cad, us, usdConv, opts, contracts}
    var cad = (b.cad_trade == null ? 0 : b.cad_trade) * o.cad * 12;
    var us = (b.us_trade == null ? 0 : b.us_trade) * o.us * 12;
    var n = o.convs || 1, per = o.usdConv / n;
    var fx = o.usdConv ? (b.fx_pct == null ? D.median_fx * o.usdConv : n * fxCost(b, per)) : 0;
    var op = o.opts ? 12 * o.opts * Math.max((b.opt_base || 0) + (b.opt_contract || 0) * (o.contracts || 1), b.opt_min || 0) : 0;
    return { cad: cad, us: us, fx: fx, opts: op, fees: b.annual_fee || 0, total: cad + us + fx + op + (b.annual_fee || 0) };
  };
  C.roboFee = function (r, amt) {
    var fee = 0;
    if (r.tiers) { // [[upTo, rate]] marginal or flat
      if (r.tier_mode === 'flat') { for (var i = 0; i < r.tiers.length; i++) { if (r.tiers[i][0] == null || amt <= r.tiers[i][0]) { fee = amt * r.tiers[i][1]; break; } } }
      else { var lo = 0; r.tiers.forEach(function (t) { var hi = t[0] == null ? Infinity : t[0]; if (amt > lo) fee += (Math.min(amt, hi) - lo) * t[1]; lo = hi; }); }
    }
    fee = Math.max(fee, r.min_fee || 0);
    var mer = amt * (r.mer || 0);
    return { mgmt: fee, mer: mer, total: fee + mer };
  };

  window.WS = window.WS || {};
  window.WS.calc = C;

  /* =====================================================================
   * 4. WIDGETS
   * ===================================================================== */
  var W = {};
  var bornDefault = function () { return MEM.get('birth', 1995); };
  var provDefault = function () { return MEM.get('prov', 'ON'); };

  /* ---------- TFSA contribution room ---------- */
  W['tfsa-room'] = function (el) {
    shell(el, 'tfsa-room', {
      title: 'TFSA contribution room calculator',
      intro: 'Enter your birth year and when you became a resident of Canada. We add up every annual limit you qualify for since ' + 2009 + ' and give your room for ' + CUR + '.',
      fields: function (p) {
        return '<div class="ws-w-grid">' +
          fNum(p, 'birth', 'Year you were born', bornDefault(), { min: 1900, max: CUR, help: 'Room starts in the year you turn 18.' }) +
          fNum(p, 'resident', 'Year you became a resident of Canada', '', { min: 1900, max: CUR, ph: 'Leave blank if always resident', help: 'Newcomers get the full limit for the year they arrive.' }) +
          fTxt(p, 'nonres', 'Full calendar years you lived outside Canada (optional)', '', { ph: 'e.g. 2015, 2016', help: 'No room is added for a year you were a non-resident for the whole year.' }) +
          fSel(p, 'prov', 'Province or territory', provOpts(), provDefault(), { help: 'Opening age depends on your province.' }) +
          fNum(p, 'contrib', 'Total contributions before ' + CUR, 0, { min: 0, help: 'All years before this one. Leave out direct transfers between TFSAs.' }) +
          fNum(p, 'wdprior', 'Total withdrawals before ' + CUR, 0, { min: 0, help: 'Withdrawals come back as room on January 1 of the next year.' }) +
          fNum(p, 'contribnow', 'Contributions so far in ' + CUR, 0, { min: 0 }) +
          fNum(p, 'wdnow', 'Withdrawals so far in ' + CUR, 0, { min: 0, help: 'Added back to your room on January 1, ' + (CUR + 1) + '.' }) +
          '</div>';
      },
      calc: function (a) {
        var birth = a.n('birth'), res = a.n('resident'), prov = a.val('prov');
        if (birth < 1900 || birth > CUR) return msg('warnmsg', 'Please enter a birth year between 1900 and ' + CUR + '.');
        MEM.set('birth', birth); MEM.set('prov', prov);
        if (birth + 18 > CUR) return msg('warnmsg', 'You turn 18 in ' + (birth + 18) + '. TFSA room starts that year: ' + money(D.tfsa.limits[birth + 18] || D.tfsa.limits[CUR]) + (D.tfsa.limits[birth + 18] ? '' : ' if the limit stays the same') + '.');
        var nonres = (a.val('nonres').match(/\d{4}/g) || []).map(Number);
        var r = C.tfsaRoom({ birth: birth, resident: res, nonres: nonres, contrib: a.n('contrib'), wdPrior: a.n('wdprior'), contribNow: a.n('contribnow'), wdNow: a.n('wdnow') });
        var maj = D.age_of_majority[prov] || 18;
        var h = head('Your TFSA room available now (' + CUR + ')', money(r.available), r.available < 0);
        if (r.available < 0) {
          var tax = -r.available * D.tfsa.over_tax_month;
          h += msg('err', 'You are over your limit by ' + money(-r.available) + '. The tax is 1% of the highest excess amount for each month it stays in the account: about ' + money2(tax) + ' a month. Withdrawing the excess stops the tax from the next month.');
        }
        h += kv([['Room earned since ' + r.start, money(r.accrued)], ['Room on January 1, ' + CUR, money(r.startOfYear)], ['Used so far in ' + CUR, money(a.n('contribnow'))],
          ['Room on January 1, ' + (CUR + 1), r.next != null ? money(r.next) : (money(r.available + r.wdNow) + ' plus the ' + (CUR + 1) + ' limit')]]);
        if (maj > 18 && CUR - birth < maj) h += msg('warnmsg', 'In your province you can open a TFSA at ' + maj + '. Room still builds from the year you turn 18, so nothing is lost.');
        h += table(['Year', 'Annual limit', 'Your cumulative room'], r.rows.map(function (x) { return [x[0], x[3] ? 'Non-resident: $0' : money(x[1]), money(x[2])]; }), 'Room added each year');
        h += how('Room starts in the latest of 2009, the year you turn 18 (' + (birth + 18) + ') and the year you became a resident' + (res ? ' (' + res + ')' : '') + '. Each year adds that year\'s limit. Contributions reduce room. Withdrawals made in an earlier year are added back on January 1. Withdrawals this year come back on January 1, ' + (CUR + 1) + '. Your CRA My Account figure can differ if contributions or withdrawals were reported differently.');
        return h;
      },
      next: [['/accounts/tfsa-contribution-limit/', 'TFSA limit by year'], ['/accounts/tfsa-withdrawals/', 'Withdrawal rules'], ['/compare/best-tfsa-accounts/', 'Compare TFSA accounts']]
    });
  };

  /* ---------- TFSA over-contribution tax ---------- */
  W['tfsa-overcontribution'] = function (el) {
    shell(el, 'tfsa-overcontribution', {
      title: 'TFSA over-contribution penalty calculator',
      intro: 'See the 1% monthly tax on an excess TFSA amount and how much you save by withdrawing it now.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'excess', 'Highest excess amount in the month', 2000, { min: 0 }) +
          fNum(p, 'months', 'Months the excess stays in the account', 3, { min: 1, max: 120, step: 1, help: 'Count each month in which any excess existed.' }) + '</div>';
      },
      calc: function (a) {
        var ex = a.n('excess'), m = Math.round(a.n('months'));
        var t = ex * D.tfsa.over_tax_month * m;
        return head('Estimated tax on the excess', money2(t)) + kv([['Tax per month', money2(ex * D.tfsa.over_tax_month)], ['Months', String(m)], ['Saved by removing it a month sooner', money2(ex * D.tfsa.over_tax_month)]]) +
          how('The tax is 1% of the highest excess TFSA amount in each month the excess exists. Withdrawing the excess, or new room arriving on January 1, ends it. You report it on the TFSA Return and pay it by June 30 of the following year, so please withdraw any excess as soon as you find it.');
      },
      next: [['/calculators/tfsa-calculator/', 'TFSA room calculator'], ['/accounts/tfsa-withdrawals/', 'TFSA withdrawal rules']]
    });
  };

  /* ---------- RRSP deduction limit ---------- */
  W['rrsp-room'] = function (el) {
    shell(el, 'rrsp-room', {
      title: 'RRSP contribution room calculator',
      intro: 'Your ' + CUR + ' RRSP room is 18% of your ' + (CUR - 1) + ' earned income up to the dollar limit, minus your pension adjustment, plus unused room carried forward.',
      fields: function (p) {
        return '<div class="ws-w-grid">' +
          fNum(p, 'earned', 'Earned income in ' + (CUR - 1), MEM.get('income', 75000), { min: 0, help: 'Employment and self-employment income, net rental income and similar. Not investment income.' }) +
          fNum(p, 'pa', 'Pension adjustment (box 52 of your T4)', 0, { min: 0, help: 'Only if you belong to a workplace pension or DPSP.' }) +
          fNum(p, 'carry', 'Unused room carried forward', 0, { min: 0, help: 'From your latest notice of assessment.' }) +
          fNum(p, 'par', 'Pension adjustment reversal (PAR)', 0, { min: 0 }) +
          fNum(p, 'done', 'RRSP contributions already made for ' + CUR, 0, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var e = a.n('earned'); MEM.set('income', e);
        var r = C.rrspRoom(e, a.n('pa'), a.n('carry'), a.n('par'));
        var left = r.room - a.n('done');
        var h = head('Your ' + CUR + ' RRSP deduction limit', money(r.room));
        h += kv([['18% of ' + (CUR - 1) + ' earned income', money(e * D.rrsp.pct)], [CUR + ' dollar limit', money(r.limit)], ['New room this year', money(Math.max(0, r.base - a.n('pa') + a.n('par')))], ['Left after contributions', money(left)]]);
        if (left < -D.rrsp.cushion) h += msg('err', 'You are ' + money(-left - D.rrsp.cushion) + ' over the $2,000 buffer. The excess is taxed at 1% a month until removed.');
        else if (left < 0) h += msg('warnmsg', 'You are within the $2,000 lifetime buffer, so no penalty tax applies, but the extra amount is not deductible until you have new room.');
        h += msg('ok', 'Contribution deadline for the ' + CUR + ' tax year: ' + fmtDate(D.rrsp.deadline[CUR]) + ', the 60th day of ' + (CUR + 1) + ' under CRA\'s rule. CRA confirms the date each year.');
        h += how('New room = the lower of 18% of last year\'s earned income and the ' + CUR + ' dollar limit (' + money(r.limit) + '), minus your pension adjustment, plus any pension adjustment reversal. Unused room from earlier years is added on top. Your notice of assessment shows the official figure.');
        return h;
      },
      next: [['/calculators/rrsp-calculator/', 'RRSP tax refund calculator'], ['/accounts/rrsp-contribution-limit/', 'RRSP limit by year'], ['/compare/best-rrsp-accounts/', 'Compare RRSP accounts']]
    });
  };

  /* ---------- RRSP tax refund ---------- */
  W['rrsp-refund'] = function (el) {
    shell(el, 'rrsp-refund', {
      title: 'RRSP tax refund calculator',
      intro: 'Pick your province, enter your taxable income and an RRSP contribution. We work out the tax saved with ' + CUR + ' federal and provincial brackets.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Taxable income before the RRSP deduction', MEM.get('income', 75000), { min: 0 }) +
          fNum(p, 'contrib', 'RRSP contribution to deduct', 5000, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), inc = a.n('income'), c = Math.min(a.n('contrib'), inc);
        MEM.set('prov', prov); MEM.set('income', inc);
        var t0 = C.tax(prov, inc), t1 = C.tax(prov, inc - c), save = t0.total - t1.total;
        var h = head('Estimated tax saved by a ' + money(c) + ' deduction', money(save));
        h += kv([['Marginal rate before', pct(C.marginal(prov, inc), 1)], ['Marginal rate after', pct(C.marginal(prov, inc - c), 1)], ['Average saving per $1', money2(c ? save / c : 0)], ['Net cost of the contribution', money(c - save)]]);
        h += table(['', 'Without RRSP', 'With RRSP'], [['Federal tax', money(t0.federal), money(t1.federal)], [D.provName[prov] + ' tax', money(t0.provincial + t0.premium), money(t1.provincial + t1.premium)], ['Total', money(t0.total), money(t1.total)]]);
        h += how('Tax saved = tax on your income without the deduction minus tax with it, using ' + CUR + ' brackets and basic personal amounts' + (prov === 'ON' ? ', the Ontario surtax and the Ontario Health Premium' : '') + (prov === 'QC' ? ' and the 16.5% Quebec abatement on federal tax' : '') + '. Your actual refund also depends on tax already withheld, other credits and CPP and EI. A refund only appears if withholding was more than your final tax.');
        return h;
      },
      next: [['/calculators/rrsp-calculator/', 'RRSP calculator'], ['/vs/tfsa-vs-rrsp/', 'TFSA vs RRSP'], ['/accounts/rrsp/', 'RRSP guide']]
    });
  };

  /* ---------- Income tax ---------- */
  W['income-tax'] = function (el) {
    shell(el, 'income-tax', {
      title: 'Canada income tax calculator ' + CUR,
      intro: 'Federal and provincial tax, your marginal rate on each type of income, and your average rate.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Employment and other ordinary income', MEM.get('income', 75000), { min: 0 }) +
          fNum(p, 'cg', 'Capital gains realized', 0, { min: 0 }) +
          fNum(p, 'elig', 'Eligible dividends received', 0, { min: 0 }) +
          fNum(p, 'nonelig', 'Other than eligible dividends received', 0, { min: 0 }) +
          fNum(p, 'rrsp', 'RRSP and FHSA deductions', 0, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'); MEM.set('prov', prov);
        var dtcOk = !!D.tax.dividends.provincial_dtc[prov];
        if (!dtcOk && (a.n('elig') > 0 || a.n('nonelig') > 0)) return msg('warnmsg', 'Dividend tax credit rates for ' + D.provName[prov] + ' are being confirmed for ' + CUR + '. Please set dividends to 0 for now, or choose Ontario, British Columbia or Quebec.');
        var T = D.tax, eg = a.n('elig') * (1 + T.dividends.eligible_grossup), ng = a.n('nonelig') * (1 + T.dividends.noneligible_grossup);
        var ti = Math.max(0, a.n('income') + a.n('cg') * T.capital_gains_inclusion + eg + ng - a.n('rrsp'));
        var t = C.tax(prov, ti, { elig: eg, nonelig: ng });
        var gross = a.n('income') + a.n('cg') + a.n('elig') + a.n('nonelig');
        var h = head('Estimated ' + CUR + ' income tax', money(t.total));
        h += kv([['Taxable income', money(ti)], ['Federal tax', money(t.federal)], [D.provName[prov] + ' tax', money(t.provincial + t.premium)], ['Average rate on all income', pct(gross ? t.total / gross : 0, 1)], ['After-tax income', money(gross - a.n('rrsp') - t.total)]]);
        h += table(['Next $100 of', 'Marginal rate'], [['Ordinary income', pct(C.marginal(prov, ti), 2)], ['Capital gains', pct(C.marginal(prov, ti, 'cg'), 2)], ['Eligible dividends', dtcOk ? pct(C.marginal(prov, ti, 'elig'), 2) : 'Being confirmed'], ['Other than eligible dividends', dtcOk ? pct(C.marginal(prov, ti, 'nonelig'), 2) : 'Being confirmed']], 'Marginal tax rates at your income');
        if (prov === 'MB') h += msg('warnmsg', 'Manitoba\'s 2026 bracket thresholds are being confirmed: CRA\'s payroll tables use $47,000 and $100,000, which this estimate uses.');
        h += how('Uses ' + CUR + ' federal and ' + D.provName[prov] + ' brackets, basic personal amounts, the dividend gross-up and dividend tax credits, and the ' + pct(T.capital_gains_inclusion, 0) + ' capital gains inclusion rate' + (prov === 'ON' ? ', plus the Ontario surtax and Health Premium' : '') + (prov === 'QC' ? ', plus the 16.5% Quebec abatement' : '') + '. CPP and EI contributions, the Canada employment amount and other credits are not included, so your final tax will usually be a little lower. A negative dividend tax result is set to zero.');
        return h;
      },
      next: [['/calculators/capital-gains-tax-calculator/', 'Capital gains tax calculator'], ['/calculators/rrsp-calculator/', 'RRSP refund calculator']]
    });
  };

  /* ---------- Capital gains ---------- */
  W['capital-gains'] = function (el) {
    shell(el, 'capital-gains', {
      title: 'Capital gains tax calculator',
      intro: 'Tax on a gain from selling shares, ETFs or other investments in a non-registered account.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Other taxable income this year', MEM.get('income', 75000), { min: 0 }) +
          fNum(p, 'proceeds', 'Sale proceeds', 20000, { min: 0 }) +
          fNum(p, 'acb', 'Adjusted cost base (what you paid, including commissions)', 12000, { min: 0 }) +
          fNum(p, 'costs', 'Selling costs', 0, { min: 0 }) +
          fNum(p, 'losses', 'Net capital losses carried forward (full loss amount)', 0, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'); MEM.set('prov', prov);
        var gain = a.n('proceeds') - a.n('acb') - a.n('costs'), inc = a.n('income'), inc_r = D.tax.capital_gains_inclusion;
        if (gain <= 0) return head('Capital loss', money(gain), true) + msg('ok', 'A capital loss of ' + money(-gain) + ' first offsets other capital gains this year. Any unused part can be carried back 3 years or forward with no time limit, against capital gains only. Watch the superficial loss rule if you or an affiliated person buy the same property within 30 days before or after the sale.');
        var net = Math.max(0, gain - a.n('losses')), taxable = net * inc_r;
        var tax = C.tax(prov, inc + taxable).total - C.tax(prov, inc).total;
        return head('Estimated tax on this gain', money(tax)) + kv([['Capital gain', money(gain)], ['Taxable capital gain (' + pct(inc_r, 0) + ')', money(taxable)], ['Effective tax rate on the gain', pct(gain ? tax / gain : 0, 1)], ['You keep', money(gain - tax)]]) +
          how('Capital gain = proceeds minus adjusted cost base minus selling costs. ' + pct(inc_r, 0) + ' of the net gain is added to your income and taxed at your marginal rate, using ' + CUR + ' ' + D.provName[prov] + ' and federal brackets. Gains inside a TFSA, RRSP, FHSA or RESP are not taxed this way.');
      },
      next: [['/accounts/tfsa/', 'Shelter gains in a TFSA'], ['/calculators/', 'All calculators']]
    });
  };

  /* ---------- Dividend tax ---------- */
  W['dividend-tax'] = function (el) {
    shell(el, 'dividend-tax', {
      title: 'Dividend tax calculator',
      intro: 'Tax on Canadian eligible and other than eligible dividends after the gross-up and dividend tax credit.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Other taxable income', MEM.get('income', 75000), { min: 0 }) +
          fNum(p, 'elig', 'Eligible dividends (actual amount)', 5000, { min: 0 }) +
          fNum(p, 'nonelig', 'Other than eligible dividends (actual amount)', 0, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), T = D.tax, inc = a.n('income');
        if (!T.dividends.provincial_dtc[prov]) return msg('warnmsg', 'Dividend tax credit rates for ' + D.provName[prov] + ' are being confirmed for ' + CUR + '. This calculator currently covers ' + Object.keys(T.dividends.provincial_dtc).map(function (k) { return D.provName[k]; }).join(', ') + '.');
        var eg = a.n('elig') * (1 + T.dividends.eligible_grossup), ng = a.n('nonelig') * (1 + T.dividends.noneligible_grossup);
        var t = C.tax(prov, inc + eg + ng, { elig: eg, nonelig: ng }).total - C.tax(prov, inc).total;
        var d = a.n('elig') + a.n('nonelig');
        return head('Estimated tax on these dividends', money(t, 0), t < 0) + kv([['Grossed-up amount', money(eg + ng)], ['Effective rate on dividends', pct(d ? t / d : 0, 1)], ['You keep', money(d - t)]]) +
          how('Eligible dividends are grossed up by ' + pct(T.dividends.eligible_grossup, 0) + ' and other than eligible dividends by ' + pct(T.dividends.noneligible_grossup, 0) + '. Federal and ' + D.provName[prov] + ' dividend tax credits are then deducted. Credits cannot reduce tax below zero, but they can shelter tax on your other income, which is why the result can be lower than you expect. Foreign dividends get no gross-up or credit.');
      },
      next: [['/calculators/capital-gains-tax-calculator/', 'Capital gains calculator'], ['/accounts/us-stocks-in-tfsa/', 'US dividends in a TFSA']]
    });
  };

  /* ---------- FHSA room ---------- */
  W['fhsa-room'] = function (el) {
    shell(el, 'fhsa-room', {
      title: 'FHSA contribution room calculator',
      intro: 'Room starts only when you open your first FHSA: ' + money(D.fhsa.annual) + ' a year, up to ' + money(D.fhsa.carry) + ' of unused room carried forward, ' + money(D.fhsa.lifetime) + ' lifetime.',
      fields: function (p) {
        var h = '<div class="ws-w-grid">' + fSel(p, 'opened', 'Year you opened your first FHSA', yearOpts(D.fhsa.first_year, CUR), CUR, { help: 'Room does not build before you open one.' }) +
          fNum(p, 'birth', 'Year you were born', bornDefault(), { min: 1900, max: CUR }) + '</div><div class="ws-rows"></div>';
        return h;
      },
      init: function (a) {
        function rows() {
          var o = a.n('opened'), box = a.form.querySelector('.ws-rows'), h = '<p class="ws-flabel" style="margin:14px 0 6px;font-weight:800">Contributions by year</p>';
          for (var y = o; y <= CUR; y++) h += '<div class="ws-rowgrid"><span>' + y + '</span><input type="number" min="0" step="any" name="c' + y + '" aria-label="FHSA contributions in ' + y + '" value="' + (y === CUR ? 0 : D.fhsa.annual) + '"><small>' + (y === CUR ? 'so far this year' : '') + '</small></div>';
          box.innerHTML = h;
        }
        rows();
        a.form.querySelector('[name="opened"]').addEventListener('change', rows);
      },
      calc: function (a) {
        var o = a.n('opened'), birth = a.n('birth'), cy = {};
        for (var y = o; y <= CUR; y++) cy[y] = a.n('c' + y);
        var r = C.fhsa(o, cy);
        var close = Math.min(o + D.fhsa.max_years, birth + D.fhsa.max_age);
        var h = head('FHSA room left in ' + CUR, money(Math.max(0, r.leftNow)), r.leftNow < 0);
        if (r.leftNow < 0) h += msg('err', 'This is ' + money(-r.leftNow) + ' over your room. Excess FHSA amounts are taxed at 1% a month until removed or absorbed by new room.');
        h += kv([['Room for ' + CUR, money(r.roomNow)], ['Lifetime room left', money(Math.max(0, r.lifetimeLeft))], ['Room on January 1, ' + (CUR + 1), money(r.nextRoom)], ['Account must close by', 'December 31, ' + close]]);
        h += table(['Year', 'Participation room', 'Contributed'], r.rows.map(function (x) { return [x[0], money(x[1]), money(x[2])]; }));
        h += how('Each year adds ' + money(D.fhsa.annual) + '. Unused room carries forward, but only up to ' + money(D.fhsa.carry) + ', so the most you can contribute in one year is ' + money(D.fhsa.annual + D.fhsa.carry) + '. Lifetime contributions are capped at ' + money(D.fhsa.lifetime) + '. The FHSA must close by the end of the ' + D.fhsa.max_years + 'th year after you opened it or the year you turn ' + D.fhsa.max_age + ', whichever is first. Contributions made in the first 60 days of a year count for that year, not the previous one.');
        return h;
      },
      next: [['/accounts/fhsa/', 'FHSA guide'], ['/accounts/fhsa-eligibility/', 'FHSA eligibility'], ['/compare/best-fhsa-accounts/', 'Compare FHSA accounts']]
    });
  };

  /* ---------- FHSA eligibility ---------- */
  W['fhsa-eligibility'] = function (el) {
    shell(el, 'fhsa-eligibility', {
      title: 'FHSA eligibility checker',
      intro: 'Answer five quick questions to see if you can open a First Home Savings Account today.',
      button: 'Check eligibility',
      fields: function (p) {
        return fRadio(p, 'res', 'Are you a resident of Canada?', [['y', 'Yes'], ['n', 'No']], 'y') +
          fNum(p, 'birth', 'Year you were born', bornDefault(), { min: 1900, max: CUR }) +
          fRadio(p, 'own', 'At any time in ' + CUR + ' or the previous four calendar years (since January 1, ' + (CUR - 4) + '), did you live in a home that you owned or jointly owned as your main home?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fRadio(p, 'spouse', 'At any time in ' + CUR + ' or the previous four calendar years, did you live in a home owned by your current spouse or common-law partner?', [['n', 'No'], ['y', 'Yes'], ['na', 'No spouse or partner']], 'na') +
          fRadio(p, 'prior', 'Have you already made a qualifying FHSA withdrawal for a home?', [['n', 'No'], ['y', 'Yes']], 'n');
      },
      calc: function (a) {
        var age = CUR - a.n('birth'), reasons = [];
        if (a.val('res') === 'n') reasons.push('You must be a resident of Canada to open an FHSA.');
        if (age < 18) reasons.push('You must be at least 18. In some provinces the age of majority is 19.');
        if (age > D.fhsa.max_age) reasons.push('You can open an FHSA only up to December 31 of the year you turn ' + D.fhsa.max_age + '.');
        if (a.val('own') === 'y') reasons.push('You do not meet the first-time home buyer test: you lived in a home you owned in ' + CUR + ' or the previous four calendar years.');
        if (a.val('spouse') === 'y') reasons.push('You do not meet the first-time home buyer test: you lived in a home owned by your current spouse or common-law partner in ' + CUR + ' or the previous four calendar years.');
        var warn = a.val('prior') === 'y' ? msg('warnmsg', 'Your FHSA participation period ends on December 31 of the year after your first qualifying withdrawal, so room stops building then.') : '';
        if (!reasons.length) return warn + head('Result', 'You appear eligible') + msg('ok', 'You can open an FHSA. Room of ' + money(D.fhsa.annual) + ' starts in the year you open it, so opening sooner builds more room, even with a $0 balance.') +
          (age >= 18 && age <= 19 ? msg('warnmsg', 'If your province\'s age of majority is 19 (British Columbia, New Brunswick, Newfoundland and Labrador, Nova Scotia, Northwest Territories, Nunavut, Yukon), some institutions will open it only at 19.') : '');
        return warn + head('Result', 'Not eligible right now', true) + '<ul>' + reasons.map(function (r) { return '<li>' + r + '</li>'; }).join('') + '</ul>';
      },
      next: [['/accounts/fhsa/', 'FHSA guide'], ['/calculators/fhsa-calculator/', 'FHSA calculator'], ['/vs/fhsa-vs-rrsp/', 'FHSA vs RRSP Home Buyers\' Plan']]
    });
  };

  /* ---------- RESP grants ---------- */
  W['resp-grant'] = function (el) {
    shell(el, 'resp-grant', {
      title: 'RESP grant calculator',
      intro: 'See the Canada Education Savings Grant, Additional CESG, Canada Learning Bond and provincial grants your contributions can attract, and the plan value at 17.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'birth', 'Child\'s year of birth', CUR - 3, { min: CUR - 17, max: CUR }) +
          fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Adjusted family net income', 80000, { min: 0, help: 'Used for the Additional CESG and Canada Learning Bond.' }) +
          fNum(p, 'kids', 'Number of qualified dependants', 1, { min: 1, max: 10, step: 1 }) +
          fNum(p, 'annual', 'Contribution per year from now', R().cesg_on, { min: 0 }) +
          fNum(p, 'past', 'Contributions already made', 0, { min: 0 }) +
          fNum(p, 'pastg', 'CESG already received', 0, { min: 0 }) +
          fNum(p, 'ret', 'Example assumption: yearly return (%)', 4, { min: -10, max: 15, help: 'An assumption for illustration, not a forecast.' }) + '</div>';
      },
      calc: function (a) {
        var birth = a.n('birth');
        if (CUR - birth > 17) return msg('warnmsg', 'CESG is paid until the end of the year the child turns 17.');
        var r = C.resp({ birth: birth, prov: a.val('prov'), income: a.n('income'), kids: Math.max(1, a.n('kids')), annual: a.n('annual'), pastContrib: a.n('past'), pastCesg: a.n('pastg'), ret: a.n('ret') / 100 });
        var t = r.thisYear;
        var h = head('Grants on your ' + CUR + ' contribution', money(t[3] + t[4] + t[5]));
        h += kv([['CESG and Additional CESG to age 17', money(r.cesg)], ['Canada Learning Bond', money(r.clb)], ['Provincial grant', money(r.prov)], ['Your contributions', money(r.contrib)], ['Estimated plan value at 17', money(r.bal)]]);
        h += table(['Year', 'Age', 'You contribute', 'CESG + A-CESG', 'CLB', 'Provincial', 'Value at year end'], r.rows.map(function (x) { return [x[0], x[1], money(x[2]), money(x[3]), money(x[4]), money(x[5]), money(x[6])]; }));
        h += how('Basic CESG is ' + pct(R().cesg_rate, 0) + ' of contributions, up to ' + money(R().cesg_annual) + ' a year, or ' + money(R().cesg_max_year) + ' when you catch up unused room, to a lifetime ' + money(R().cesg_lifetime) + '. Additional CESG adds ' + pct(R().acesg_rates[0], 0) + ' or ' + pct(R().acesg_rates[1], 0) + ' on the first ' + money(R().acesg_on_first) + ' each year, depending on family income. The Canada Learning Bond needs no contribution: ' + money(R().clb_first) + ' in the first eligible year and ' + money(R().clb_yearly) + ' a year after, up to ' + money(R().clb_max) + ', for lower-income families. For 16 and 17 year olds, CESG is paid only if at least ' + money(R().cesg_age16_total) + ' was contributed, or at least $100 a year in any 4 years, before the end of the year the child turned 15. Growth uses your example return.');
        return h;
      },
      next: [['/accounts/resp-grants/', 'RESP grants explained'], ['/accounts/resp/', 'RESP guide'], ['/compare/best-resp-providers/', 'Compare RESP providers']]
    });
    function R() { return D.resp; }
  };

  /* ---------- RRIF minimum withdrawal ---------- */
  W['rrif-minimum'] = function (el) {
    shell(el, 'rrif-minimum', {
      title: 'RRIF minimum withdrawal calculator',
      intro: 'Your minimum is the RRIF value on January 1 times the factor for your age at the start of the year. You can use a younger spouse\'s age.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'age', 'Age on January 1 (yours or your younger spouse\'s)', 72, { min: 50, max: 110, step: 1 }) +
          fNum(p, 'fmv', 'RRIF value on January 1', 300000, { min: 0 }) +
          fNum(p, 'ret', 'Example assumption: yearly return (%)', 4, { min: -10, max: 15 }) +
          fNum(p, 'years', 'Years to project', 10, { min: 1, max: 40, step: 1 }) + '</div>';
      },
      calc: function (a) {
        var age = Math.round(a.n('age')), v = a.n('fmv'), r = a.n('ret') / 100, n = Math.round(a.n('years')), rows = [];
        var f = C.rrifFactor(age), m = v * f;
        for (var i = 0; i < n && v > 0; i++) {
          var fa = C.rrifFactor(age + i), mi = v * fa; rows.push([age + i, pct(fa, 2), money(v), money(mi)]); v = (v - mi) * (1 + r);
        }
        return head('Minimum withdrawal this year', money(m)) + kv([['Factor at age ' + age, pct(f, 2)], ['Per month', money(m / 12)], ['Withholding on the minimum', '$0']]) +
          msg('ok', 'No tax is withheld on the minimum. Amounts above it have withholding of ' + D.rrsp.withholding_text + '. All RRIF income is taxable in the year received.') +
          table(['Age on Jan 1', 'Factor', 'Value on Jan 1', 'Minimum'], rows, 'Projection with your example return (minimum taken at the start of each year)') +
          how('Under age 71 the factor is 1 / (90 - age). From 71 the prescribed factors apply, reaching 20% at 95 and over. No minimum applies in the year the RRIF is opened.');
      },
      next: [['/accounts/rrif-minimum-withdrawal/', 'RRIF minimum withdrawal table'], ['/compare/best-rrif-accounts/', 'Compare RRIF accounts']]
    });
  };

  /* ---------- Home Buyers' Plan repayment ---------- */
  W['hbp-repayment'] = function (el) {
    shell(el, 'hbp-repayment', {
      title: 'Home Buyers\' Plan repayment calculator',
      intro: 'Withdraw up to ' + money(D.hbp.max) + ' from your RRSP for a first home and repay it over ' + D.hbp.repay_years + ' years.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Amount withdrawn under the HBP', 35000, { min: 0, max: D.hbp.max }) +
          fSel(p, 'yr', 'Year of the first withdrawal', yearOpts(2015, CUR + 1), CUR) + '</div>';
      },
      calc: function (a) {
        var amt = Math.min(a.n('amt'), D.hbp.max), y = a.n('yr');
        var deferred = y >= D.hbp.deferral[0] && y <= D.hbp.deferral[1];
        var start = y + (deferred ? D.hbp.deferral_start : 2);
        var ann = amt / D.hbp.repay_years;
        var h = head('Minimum yearly repayment', money2(ann)) + kv([['First repayment year', String(start)], ['Last repayment year', String(start + D.hbp.repay_years - 1)], ['Repay by', 'within 60 days after December 31, ' + start]]);
        if (deferred) h += msg('ok', 'Withdrawals from ' + D.hbp.deferral[0] + ' to ' + D.hbp.deferral[1] + ' get extra time: repayment starts in the ' + D.hbp.deferral_start + 'th year after the withdrawal.');
        h += msg('warnmsg', 'Any amount below the yearly minimum is added to your income for that year and taxed.');
        h += how('The HBP balance is repaid in ' + D.hbp.repay_years + ' equal yearly amounts. You can repay more, which lowers later minimums. Designate repayments on Schedule 7 of your return.');
        return h;
      },
      next: [['/accounts/home-buyers-plan/', 'Home Buyers\' Plan guide'], ['/vs/fhsa-vs-rrsp/', 'FHSA vs RRSP Home Buyers\' Plan']]
    });
  };

  /* ---------- First home down payment planner (FHSA + HBP) ---------- */
  W['first-home'] = function (el) {
    shell(el, 'first-home', {
      title: 'First home savings planner: FHSA plus Home Buyers\' Plan',
      intro: 'See how much a single buyer or a couple could put toward a first home from FHSAs and RRSPs.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fRadio(p, 'who', 'Buying', [['1', 'Alone'], ['2', 'With a spouse or partner']], '1') +
          fNum(p, 'years', 'Years until you buy', 4, { min: 1, max: 15, step: 1 }) +
          fNum(p, 'fhsa', 'Current FHSA balance, per person', 0, { min: 0 }) +
          fNum(p, 'rrsp', 'RRSP balance available for the HBP, per person', 20000, { min: 0 }) +
          fNum(p, 'ret', 'Example assumption: yearly return (%)', 3, { min: -10, max: 15 }) + '</div>';
      },
      calc: function (a) {
        var who = +a.val('who') || 1, n = Math.round(a.n('years')), r = a.n('ret') / 100, F = D.fhsa;
        var bal = a.n('fhsa'), contrib = 0, room = F.annual;
        for (var i = 0; i < n; i++) { var c = Math.min(room, F.lifetime - contrib); bal = (bal + c) * (1 + r); contrib += c; room = F.annual; }
        var hbp = Math.min(D.hbp.max, a.n('rrsp') * Math.pow(1 + r, n));
        var tot = (bal + hbp) * who;
        return head('Possible first-home funds in ' + n + ' year' + (n > 1 ? 's' : ''), money(tot)) +
          kv([['FHSA, per person', money(bal)], ['FHSA contributions, per person', money(contrib)], ['HBP withdrawal, per person', money(hbp)], ['Persons', String(who)]]) +
          how('Assumes the maximum ' + money(F.annual) + ' FHSA contribution each year from now, capped at ' + money(F.lifetime) + ' lifetime, and the HBP limit of ' + money(D.hbp.max) + ' per person. FHSA withdrawals for a qualifying home are tax-free and never repaid. HBP withdrawals must be repaid over ' + D.hbp.repay_years + ' years. You can use both for the same home.');
      },
      next: [['/vs/fhsa-vs-rrsp/', 'FHSA vs RRSP'], ['/vs/fhsa-vs-tfsa/', 'FHSA vs TFSA'], ['/compare/best-fhsa-accounts/', 'Compare FHSA accounts']]
    });
  };

  /* ---------- TFSA vs RRSP ---------- */
  W['tfsa-vs-rrsp'] = function (el) {
    shell(el, 'tfsa-vs-rrsp', {
      title: 'TFSA vs RRSP calculator',
      intro: 'Compare what the same pre-tax dollars are worth after tax in each account, based on your tax rate now and in retirement.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'now', 'Taxable income now', MEM.get('income', 75000), { min: 0 }) +
          fNum(p, 'later', 'Expected taxable income when you withdraw', 50000, { min: 0 }) +
          fNum(p, 'amt', 'Pre-tax amount to invest', 10000, { min: 0 }) +
          fNum(p, 'years', 'Years invested', 25, { min: 1, max: 60, step: 1 }) +
          fNum(p, 'ret', 'Example assumption: yearly return (%)', 5, { min: -10, max: 15 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), tn = C.marginal(prov, a.n('now')), tl = C.marginal(prov, a.n('later')), amt = a.n('amt'), g = Math.pow(1 + a.n('ret') / 100, a.n('years'));
        var rr = amt * g * (1 - tl), tf = amt * (1 - tn) * g, diff = rr - tf;
        var h = head(Math.abs(diff) < 1 ? 'Same result in both accounts' : ((diff > 0 ? 'RRSP' : 'TFSA') + ' leaves you more, by'), Math.abs(diff) < 1 ? money(0) : money(Math.abs(diff)));
        h += kv([['Your marginal rate now', pct(tn, 1)], ['Marginal rate at withdrawal', pct(tl, 1)], ['RRSP after tax', money(rr)], ['TFSA after tax', money(tf)]]);
        h += how('RRSP: the full pre-tax amount is invested because the deduction refunds the tax, then withdrawals are taxed at your future rate. TFSA: you invest after-tax dollars and withdraw tax-free. When the two rates are equal, the results are equal. Withdrawals can also reduce income-tested benefits such as OAS and GIS, which this does not include.');
        return h;
      },
      next: [['/vs/tfsa-vs-rrsp/', 'TFSA vs RRSP guide'], ['/calculators/rrsp-calculator/', 'RRSP refund calculator'], ['/calculators/tfsa-calculator/', 'TFSA room calculator']]
    });
  };

  /* ---------- Which account fits (general information) ---------- */
  W['account-chooser'] = function (el) {
    shell(el, 'account-chooser', {
      title: 'Which account fits your goal?',
      intro: 'Five quick questions. We show which registered accounts are built for your goal and why. General information, not a recommendation.',
      button: 'Show my accounts',
      fields: function (p) {
        return fSel(p, 'goal', 'What are you saving for?', [['home', 'A first home'], ['retire', 'Retirement'], ['kid', 'A child\'s education'], ['flex', 'Flexible savings or any goal']], 'retire') +
          fNum(p, 'age', 'Your age', CUR - bornDefault(), { min: 16, max: 100, step: 1 }) +
          fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Taxable income', MEM.get('income', 60000), { min: 0 }) +
          fRadio(p, 'own', 'Have you owned and lived in a home in the last four calendar years or this year?', [['n', 'No'], ['y', 'Yes']], 'n');
      },
      calc: function (a) {
        var goal = a.val('goal'), age = a.n('age'), mr = C.marginal(a.val('prov'), a.n('income')), own = a.val('own') === 'y', L = [];
        var hi = mr >= 0.30;
        if (goal === 'home') {
          if (!own && age >= 18 && age <= D.fhsa.max_age) L.push(['FHSA', 'Deductible like an RRSP and tax-free out for a qualifying first home: ' + money(D.fhsa.annual) + ' a year, ' + money(D.fhsa.lifetime) + ' lifetime.', '/accounts/fhsa/']);
          L.push(['TFSA', 'Tax-free growth and withdrawals at any time, with no home-buying conditions.', '/accounts/tfsa/']);
          if (!own) L.push(['RRSP Home Buyers\' Plan', 'Borrow up to ' + money(D.hbp.max) + ' from your RRSP for a first home and repay over ' + D.hbp.repay_years + ' years.', '/accounts/home-buyers-plan/']);
        } else if (goal === 'retire') {
          if (hi) { L.push(['RRSP', 'At your ' + pct(mr, 1) + ' marginal rate, the deduction is valuable. Withdrawals are taxed later, often at a lower rate.', '/accounts/rrsp/']); L.push(['TFSA', 'Tax-free growth; withdrawals do not affect OAS or GIS.', '/accounts/tfsa/']); }
          else { L.push(['TFSA', 'At a ' + pct(mr, 1) + ' marginal rate, the RRSP deduction is worth less, and TFSA withdrawals never count as income.', '/accounts/tfsa/']); L.push(['RRSP', 'Still useful if you expect a lower rate in retirement or have workplace matching.', '/accounts/rrsp/']); }
          if (age >= 65) L.push(['RRIF', 'Your RRSP must become a RRIF or annuity by the end of the year you turn 71.', '/accounts/rrif-minimum-withdrawal/']);
        } else if (goal === 'kid') {
          L.push(['RESP', 'Grants of 20% on contributions through the CESG, up to ' + money(D.resp.cesg_lifetime) + ' per child, plus the Canada Learning Bond for lower-income families.', '/accounts/resp/']);
          L.push(['TFSA', 'A flexible back-up with no education conditions.', '/accounts/tfsa/']);
        } else {
          L.push(['TFSA', 'The most flexible account: tax-free growth and withdrawals at any time, and room comes back the next year.', '/accounts/tfsa/']);
          L.push(['Non-registered account', 'No limits, but interest, dividends and gains are taxable each year.', '/accounts/']);
        }
        return head('Accounts built for this goal', L.map(function (x) { return x[0]; }).join(', ')) + '<ol>' + L.map(function (x) { return '<li><a href="' + x[2] + '"><b>' + x[0] + '</b></a>: ' + x[1] + '</li>'; }).join('') + '</ol>' +
          msg('warnmsg', 'General information only. The right mix depends on your full situation, including workplace plans, debts and benefits.');
      },
      next: [['/accounts/', 'All account types'], ['/compare/best-online-brokers/', 'Where to open them']]
    });
  };

  /* ---------- US withholding tax ---------- */
  W['us-withholding'] = function (el) {
    var A = D.us_withholding;
    shell(el, 'us-withholding', {
      title: 'US dividend withholding tax calculator',
      intro: 'See how much of your US dividends the IRS keeps in each Canadian account, and whether you can get it back.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'acct', 'Account type', A.accounts.map(function (x) { return [x[0], x[1]]; }), 'tfsa') +
          fNum(p, 'div', 'US dividends per year (USD)', 1000, { min: 0 }) +
          fRadio(p, 'w8', 'W-8BEN on file with your broker?', [['y', 'Yes'], ['n', 'No']], 'y') + '</div>';
      },
      calc: function (a) {
        var acc = A.accounts.filter(function (x) { return x[0] === a.val('acct'); })[0], d = a.n('div');
        var rate = acc[2] ? 0 : (a.val('w8') === 'y' ? A.treaty : A.no_w8);
        var h = head('US tax withheld each year', money2(d * rate) + ' USD') + kv([['Withholding rate', pct(rate, 0)], ['Recoverable?', acc[3]]]);
        h += msg(acc[2] ? 'ok' : 'warnmsg', acc[4]);
        h += how('The Canada-US tax treaty sets ' + pct(A.treaty, 0) + ' withholding on US dividends for Canadian residents who file a W-8BEN, and ' + pct(A.no_w8, 0) + ' without one. The treaty exempts accounts set up for retirement income, such as an RRSP, RRIF or LIRA, when you hold US-listed securities directly. A TFSA, RESP and FHSA are not treated as retirement accounts, so the withholding is a permanent cost there.');
        return h;
      },
      next: [['/accounts/us-stocks-in-tfsa/', 'US stocks in a TFSA'], ['/compare/best-rrsp-for-us-stocks/', 'Best RRSP for US stocks']]
    });
  };

  /* ---------- Currency conversion cost by broker ---------- */
  W['fx-cost'] = function (el) {
    shell(el, 'fx-cost', {
      title: 'Brokerage currency conversion fee calculator',
      intro: 'What each broker charges to convert Canadian dollars to US dollars or back, at its published rate.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Amount to convert (CAD)', 10000, { min: 0 }) + fRadio(p, 'trip', 'Conversions', [['1', 'One way'], ['2', 'Round trip (in and back out)']], '1') +
        fNum(p, 'xr', 'Example assumption: Canadian dollars per US$1', D.usdcad_example, { min: 0.5, max: 3, step: 0.01, help: 'Used only for brokers that set their tiers in US dollars. Use the rate your broker quotes.' }) + '</div>'; },
      calc: function (a) {
        var amt = a.n('amt'), k = +a.val('trip') || 1, xr = a.n('xr') || D.usdcad_example;
        var rows = D.brokers.filter(function (b) { return b.fx_pct != null; }).map(function (b) { var c = fxCost(b, amt, xr) * k; return { b: b, c: c }; }).sort(function (x, y) { return x.c - y.c; });
        var usdNote = function (b) { return b.usd_acct_tiers ? ' Inside a USD account ($10 a month on Core, included on Premium and Generation): ' + pct(tierRate(b.usd_acct_tiers, amt), 2) + ' at this amount.' : ''; };
        return head('Lowest published cost', money2(rows[0].c) + ' at ' + rows[0].b.name) +
          table(['Broker', 'Rate at this amount', 'Your cost', 'USD in registered accounts'], rows.map(function (r) { return ['<a href="' + r.b.review + '">' + r.b.name + '</a>', (r.b.id === 'interactive-brokers' ? r.b.fx_text : pct(fxRate(r.b, amt, xr), 2)) + ((r.b.fx_note || r.b.usd_acct_tiers) ? ' <span class="ws-note">' + (r.b.fx_note || '') + usdNote(r.b) + '</span>' : ''), money2(r.c), r.b.usd_reg_text]; })) +
          '<p class="ws-note">Not shown because no single rate is published: ' + D.brokers.filter(function (b) { return b.fx_pct == null; }).map(function (b) { return b.name + ' (' + b.fx_text + ')'; }).join('; ') + '.</p>' +
          how('Cost = the published conversion rate for the size of each conversion, times the amount (Interactive Brokers: 0.20 basis points with a US$2 minimum). Tier thresholds are applied to the amount you enter; National Bank and BMO set their tiers in US dollars, so for them the amount is first converted at the exchange rate you enter. Wealthsimple charges 1.5% on US trades from a Canadian-dollar account; its lower tiers apply only inside its USD account. Brokers that quote a spread build it into the exchange rate rather than charging it separately. Holding US dollars in a USD account avoids converting back and forth. Norbert\'s Gambit can cut the cost on large amounts.');
      },
      next: [['/learn/norberts-gambit/', 'Norbert\'s Gambit guide'], ['/compare/best-brokers-low-fx-fees/', 'Lowest FX fee brokers']]
    });
  };

  /* ---------- Norbert's Gambit ---------- */
  W['norberts-gambit'] = function (el) {
    shell(el, 'norberts-gambit', {
      title: 'Norbert\'s Gambit savings calculator',
      intro: 'Compare your broker\'s conversion fee with the cost of journaling an interlisted ETF.',
      fields: function (p) {
        var opts = D.brokers.filter(function (b) { return b.fx_pct != null; }).map(function (b) { return [b.id, b.name + ' (' + b.fx_text + ')']; });
        return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Amount to convert (CAD)', 25000, { min: 0 }) +
          fSel(p, 'broker', 'Your broker', opts, 'questrade') +
          fNum(p, 'comm', 'Commission per trade at your broker', 0, { min: 0, help: 'Two trades: buy in CAD, sell in USD.' }) +
          fNum(p, 'spread', 'Example assumption: bid-ask and ECN cost (%)', 0.05, { min: 0, max: 2, help: 'Depends on the market at the time. Check the quote before you trade.' }) +
          fNum(p, 'xr', 'Example assumption: Canadian dollars per US$1', D.usdcad_example, { min: 0.5, max: 3, step: 0.01, help: 'Used only for brokers that set their conversion tiers in US dollars.' }) + '</div>';
      },
      init: function (a) {
        a.form.querySelector('[name="broker"]').addEventListener('change', function () { var b = byId(a.val('broker')); if (b) a.set('comm', b.cad_trade || 0); });
      },
      calc: function (a) {
        var b = byId(a.val('broker')), amt = a.n('amt');
        var xr = a.n('xr') || D.usdcad_example, fx = fxCost(b, amt, xr), ng = 2 * a.n('comm') + amt * a.n('spread') / 100;
        var save = fx - ng;
        return head(save > 0 ? 'Norbert\'s Gambit could save you about' : 'Converting at your broker costs less here', money2(Math.abs(save))) +
          kv([['Broker conversion cost', money2(fx)], ['Norbert\'s Gambit cost', money2(ng)], ['Your broker\'s rate at this amount', pct(fxRate(b, amt, xr), 2)]]) +
          how('Norbert\'s Gambit: buy an interlisted ETF in Canadian dollars, ask your broker to journal it to the US-dollar side, then sell it in US dollars. You pay two commissions and the bid-ask spread instead of the conversion fee. The share price can move while the journal is processed, which this estimate does not include.');
      },
      next: [['/learn/norberts-gambit/', 'Step-by-step guide'], ['/markets/how-to-buy-us-stocks/', 'How to buy US stocks']]
    });
  };

  /* ---------- Annual broker cost ---------- */
  W['broker-cost'] = function (el) {
    shell(el, 'broker-cost', {
      title: 'What will each broker cost you in a year?',
      intro: 'Enter how you invest. We total commissions, currency conversion and account fees at every broker we cover, at published prices.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'cad', 'Canadian stock and ETF trades per month', 2, { min: 0, step: 1 }) +
          fNum(p, 'us', 'US stock and ETF trades per month', 1, { min: 0, step: 1 }) +
          fNum(p, 'conv', 'CAD converted to USD per year', 6000, { min: 0 }) +
          fNum(p, 'convs', 'Number of conversions per year', 4, { min: 1, step: 1 }) +
          fNum(p, 'opts', 'Options trades per month', 0, { min: 0, step: 1 }) +
          fNum(p, 'contracts', 'Contracts per options trade', 1, { min: 1, step: 1 }) + '</div>';
      },
      calc: function (a) {
        var o = { cad: a.n('cad'), us: a.n('us'), usdConv: a.n('conv'), convs: Math.max(1, a.n('convs')), opts: a.n('opts'), contracts: a.n('contracts') };
        var rows = D.brokers.map(function (b) { return { b: b, c: C.brokerAnnual(b, o) }; }).filter(function (r) { return !(o.opts > 0 && r.b.opt_base == null); }).sort(function (x, y) { return x.c.total - y.c.total; });
        return head('Lowest estimated yearly cost', money(rows[0].c.total) + ' at ' + rows[0].b.name) +
          table(['Broker', 'Commissions', 'Currency conversion', 'Options', 'Account fees', 'Total a year'], rows.map(function (r) {
            return ['<a href="' + r.b.review + '">' + r.b.name + '</a>', money(r.c.cad + r.c.us), money(r.c.fx) + (r.b.fx_pct == null && o.usdConv ? '*' : ''), money(r.c.opts), money(r.c.fees), '<b>' + money(r.c.total) + '</b>'];
          })) + '<p class="ws-note">* This broker does not publish a conversion rate or uses an undisclosed spread, so we count ' + pct(D.median_fx, 1) + ', the median published rate.</p>' + how('Uses each broker\'s published standard pricing for a self-directed account. Per-share commissions assume 40 shares per order. Account fees include any recurring fee you cannot avoid at a typical balance; most fees can be waived. ECN fees, regulatory fees and promotional pricing are not included. Prices change, so check the review for the date each price was confirmed.');
      },
      next: [['/compare/best-online-brokers/', 'Best online brokers'], ['/methodology/brokers/', 'How we rate brokers']]
    });
  };

  /* ---------- Options cost ---------- */
  W['options-cost'] = function (el) {
    shell(el, 'options-cost', {
      title: 'Options trading cost calculator',
      intro: 'Yearly options commissions at each broker for your trading pattern.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'trades', 'Options trades per month', 4, { min: 0, step: 1 }) + fNum(p, 'contracts', 'Contracts per trade', 2, { min: 1, step: 1 }) + '</div>'; },
      calc: function (a) {
        var t = a.n('trades'), k = a.n('contracts');
        var rows = D.brokers.filter(function (b) { return b.opt_base != null; }).map(function (b) { var per = Math.max(b.opt_base + b.opt_contract * k, b.opt_min || 0); return { b: b, per: per, yr: per * t * 12 }; }).sort(function (x, y) { return x.yr - y.yr; });
        return head('Lowest yearly options cost', money(rows[0].yr) + ' at ' + rows[0].b.name) + table(['Broker', 'Pricing', 'Per trade', 'Per year'], rows.map(function (r) { return ['<a href="' + r.b.review + '">' + r.b.name + '</a>', r.b.opt_text, money2(r.per), money(r.yr)]; })) +
          how('Per trade = base commission plus the per-contract fee times the number of contracts. Exercise and assignment fees, and exchange or regulatory fees, are extra at most brokers.');
      },
      next: [['/compare/best-options-trading-platforms/', 'Best options platforms']]
    });
  };

  /* ---------- Margin interest ---------- */
  W['margin-interest'] = function (el) {
    shell(el, 'margin-interest', {
      title: 'Margin interest calculator',
      intro: 'Interest on a margin loan at each broker\'s published rate, or a rate you enter.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Amount borrowed (CAD)', 20000, { min: 0 }) + fNum(p, 'days', 'Days borrowed', 365, { min: 1, step: 1 }) + fNum(p, 'rate', 'Or your own annual rate (%)', '', { min: 0, max: 30, ph: 'optional' }) + '</div>'; },
      calc: function (a) {
        var amt = a.n('amt'), d = a.n('days'), own = a.val('rate');
        if (own !== '') { var i = amt * num(own) / 100 * d / 365; return head('Interest for ' + d + ' days', money2(i)) + how('Interest = amount x annual rate x days / 365. Brokers charge interest daily and post it monthly.'); }
        var rows = D.brokers.filter(function (b) { return b.margin_cad != null; }).map(function (b) { return { b: b, i: amt * b.margin_cad * d / 365 }; }).sort(function (x, y) { return x.i - y.i; });
        return head('Lowest interest for ' + d + ' days', money2(rows[0].i) + ' at ' + rows[0].b.name) + table(['Broker', 'Published CAD margin rate', 'Interest'], rows.map(function (r) { return ['<a href="' + r.b.review + '">' + r.b.name + '</a>', r.b.margin_text, money2(r.i)]; })) +
          how('Uses the published rate for this loan size where a broker tiers its rates. Rates float with the prime rate or the broker\'s benchmark and change without notice. Margin interest on money borrowed to earn investment income in a non-registered account is generally tax-deductible.');
      },
      next: [['/compare/best-margin-accounts/', 'Lowest margin rates']]
    });
  };

  /* ---------- Robo-advisor fees ---------- */
  W['robo-fee'] = function (el) {
    shell(el, 'robo-fee', {
      title: 'Robo-advisor fee calculator',
      intro: 'Yearly management fee plus fund costs at each robo-advisor for the amount you invest.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Amount invested', 50000, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var amt = a.n('amt');
        var rows = D.robos.map(function (r) { return { r: r, c: C.roboFee(r, amt), ok: amt >= (r.min || 0) }; }).sort(function (x, y) { return x.c.total - y.c.total; });
        return head('Lowest yearly cost', money(rows[0].c.total) + ' at ' + rows[0].r.name) + table(['Robo-advisor', 'Management fee', 'Fund costs (MER)', 'Total a year', 'Minimum'], rows.map(function (x) {
          return [x.r.review ? '<a href="' + x.r.review + '">' + x.r.name + '</a>' : x.r.name, money(x.c.mgmt) + ' <span class="ws-note">' + x.r.fee_text + '</span>', money(x.c.mer) + ' <span class="ws-note">' + x.r.mer_text + '</span>', '<b>' + money(x.c.total) + '</b>', x.ok ? money(x.r.min || 0) : '<span style="color:var(--ws-bad)">' + money(x.r.min) + ' needed</span>'];
        })) + how('Management fee from each robo-advisor\'s published schedule. Fund costs use the midpoint of the MER range each publishes for its core portfolios. Your actual fund costs depend on the portfolio you choose.');
      },
      next: [['/compare/best-robo-advisors/', 'Best robo-advisors'], ['/calculators/compound-interest-calculator/', 'Fee drag over time']]
    });
  };

  /* ---------- Fee drag ---------- */
  W['fee-drag'] = function (el) {
    shell(el, 'fee-drag', {
      title: 'Investment fee impact calculator',
      intro: 'See what a higher fee costs over time on the same investments.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'pv', 'Starting amount', 25000, { min: 0 }) + fNum(p, 'pmt', 'Monthly contribution', 300, { min: 0 }) + fNum(p, 'years', 'Years', 25, { min: 1, max: 60, step: 1 }) +
          fNum(p, 'ret', 'Example assumption: return before fees (%)', 6, { min: -10, max: 15 }) + fNum(p, 'fa', 'Fee A (% a year)', 0.25, { min: 0, max: 5 }) + fNum(p, 'fb', 'Fee B (% a year)', 2, { min: 0, max: 5 }) + '</div>';
      },
      calc: function (a) {
        var y = a.n('years'), r = a.n('ret') / 100;
        var A = C.grow(a.n('pv'), a.n('pmt'), r - a.n('fa') / 100, y, 12), B = C.grow(a.n('pv'), a.n('pmt'), r - a.n('fb') / 100, y, 12);
        return head('Difference after ' + y + ' years', money(A.bal - B.bal)) + kv([['Ending value at ' + a.n('fa') + '%', money(A.bal)], ['Ending value at ' + a.n('fb') + '%', money(B.bal)], ['You contribute', money(A.contrib)]]) +
          how('Fees are taken from returns every year, so the gap compounds. Each scenario grows monthly at the return minus its fee.');
      },
      next: [['/compare/best-robo-advisors/', 'Compare robo-advisor fees'], ['/learn/how-to-invest/', 'How to invest in Canada']]
    });
  };

  /* ---------- Compound interest ---------- */
  W['compound-interest'] = function (el) {
    shell(el, 'compound-interest', {
      title: 'Compound interest calculator',
      intro: 'Starting amount, monthly saving, rate and time. See the year-by-year growth.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'pv', 'Starting amount', 10000, { min: 0 }) + fNum(p, 'pmt', 'Monthly contribution', 500, { min: 0 }) +
          fNum(p, 'rate', 'Annual interest or return (%)', 5, { min: -10, max: 30 }) + fNum(p, 'years', 'Years', 20, { min: 1, max: 70, step: 1 }) +
          fSel(p, 'comp', 'Compounding', [[1, 'Yearly'], [2, 'Semi-annually'], [4, 'Quarterly'], [12, 'Monthly'], [365, 'Daily']], 12) + '</div>';
      },
      calc: function (a) {
        var g = C.grow(a.n('pv'), a.n('pmt'), a.n('rate') / 100, a.n('years'), a.n('comp') || 12);
        return head('Value after ' + a.n('years') + ' years', money(g.bal)) + kv([['Total contributed', money(g.contrib)], ['Interest and growth', money(g.interest)], ['Growth share of the total', pct(g.bal ? g.interest / g.bal : 0, 0)]]) +
          bars(g.rows.map(function (r) { return { total: r[2], part: Math.max(0, r[2] - r[1]), label: 'Year ' + r[0] }; }), ['Growth', 'Contributions']) +
          table(['Year', 'Contributed to date', 'Value at year end'], g.rows.map(function (r) { return [r[0], money(r[1]), money(r[2])]; })) +
          how('Contributions are added at the end of each month. The rate is converted to an effective monthly rate using your compounding choice. Tax and fees are not included; use a TFSA or RRSP to shelter growth.');
      },
      next: [['/accounts/tfsa/', 'Grow it tax-free in a TFSA'], ['/savings/gic-rates/', 'GIC rates'], ['/savings/high-interest-savings-accounts/', 'Savings rates']]
    });
  };

  /* ---------- Savings goal ---------- */
  W['savings-goal'] = function (el) {
    shell(el, 'savings-goal', {
      title: 'Savings goal calculator',
      intro: 'How much to save each month to reach a target by a date.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'goal', 'Target amount', 50000, { min: 0 }) + fNum(p, 'have', 'Saved so far', 5000, { min: 0 }) + fNum(p, 'years', 'Years to reach it', 5, { min: 0.25, max: 60 }) + fNum(p, 'rate', 'Interest or return (% a year)', 3, { min: 0, max: 20 }) + '</div>'; },
      calc: function (a) {
        var n = Math.round(a.n('years') * 12), i = Math.pow(1 + a.n('rate') / 100, 1 / 12) - 1, fv = a.n('goal') - a.n('have') * Math.pow(1 + i, n);
        var pmt = fv <= 0 ? 0 : (i ? fv * i / (Math.pow(1 + i, n) - 1) : fv / n);
        return head('Save each month', money(pmt)) + kv([['Months', String(n)], ['Total you put in', money(pmt * n + a.n('have'))], ['Interest earned', money(a.n('goal') - pmt * n - a.n('have'))]]) + how('Monthly saving at the end of each month, growing at the effective monthly rate.');
      },
      next: [['/savings/high-interest-savings-accounts/', 'Best savings rates'], ['/accounts/fhsa/', 'Saving for a home? FHSA']]
    });
  };

  /* ---------- GIC ---------- */
  W['gic-calc'] = function (el) {
    shell(el, 'gic-calc', {
      title: 'GIC calculator',
      intro: 'Interest and maturity value for a GIC at any rate, term and compounding.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'pv', 'Amount invested', 10000, { min: 0 }) + fNum(p, 'rate', 'Annual rate (%)', D.gic_default_rate || 3, { min: 0, max: 15 }) +
          fNum(p, 'term', 'Term (years)', 2, { min: 0.25, max: 10, step: 0.25 }) +
          fSel(p, 'comp', 'Interest paid', [['1', 'Compounded yearly'], ['2', 'Compounded semi-annually'], ['12', 'Compounded monthly'], ['simple', 'Paid out yearly (simple)']], '1') +
          fSel(p, 'prov', 'Province (for tax outside a TFSA)', provOpts(), provDefault()) + fNum(p, 'income', 'Your taxable income', MEM.get('income', 60000), { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var pv = a.n('pv'), r = a.n('rate') / 100, t = a.n('term'), c = a.val('comp');
        var mv = c === 'simple' ? pv + pv * r * t : pv * Math.pow(1 + r / +c, +c * t);
        var intr = mv - pv, mr = C.marginal(a.val('prov'), a.n('income'));
        return head('Value at maturity', money2(mv)) + kv([['Interest earned', money2(intr)], ['Tax in a non-registered account', money2(intr * mr)], ['Interest after tax', money2(intr * (1 - mr))], ['In a TFSA', money2(intr) + ' tax-free']]) +
          how('Compound GICs reinvest interest at the same rate. Interest on a multi-year compound GIC held outside a registered account is taxable every year on each anniversary, even though you receive it at maturity.');
      },
      next: [['/savings/gic-rates/', 'Best GIC rates'], ['/vs/gic-vs-hisa/', 'GIC vs savings account']]
    });
  };

  W['gic-ladder'] = function (el) {
    shell(el, 'gic-ladder', {
      title: 'GIC ladder builder',
      intro: 'Split one amount across 1 to 5-year GICs so part of your money comes due every year.',
      fields: function (p) {
        var b = D.gic_best || {};
        return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Total to invest', 25000, { min: 0 }) +
          [1, 2, 3, 4, 5].map(function (y) { return fNum(p, 'r' + y, y + '-year rate (%)', b[y] || '', { min: 0, max: 15 }); }).join('') + '</div>';
      },
      calc: function (a) {
        var part = a.n('amt') / 5, rows = [], tot = 0;
        for (var y = 1; y <= 5; y++) { var r = a.n('r' + y) / 100, mv = part * Math.pow(1 + r, y); tot += mv - part; rows.push([y + ' year', pct(r, 2), money(part), money(mv), String(CUR + y)]); }
        var avg = 0; for (var k = 1; k <= 5; k++) avg += a.n('r' + k); avg /= 5;
        return head('Average rate across the ladder', nf(avg, 2) + '%') + table(['Rung', 'Rate', 'Invested', 'At maturity', 'Matures in'], rows) +
          how('Each rung holds one fifth of the money. When a rung matures, reinvesting it in a new 5-year GIC keeps one GIC maturing every year. Rates default to the best published rates in our GIC table and can be changed.');
      },
      next: [['/savings/gic-rates/', 'Best GIC rates']]
    });
  };

  /* ---------- HISA earnings (data-list="usd" for US-dollar accounts) ---------- */
  W['hisa-earnings'] = function (el) {
    var usd = el.getAttribute('data-list') === 'usd', list = usd ? D.usd_savings : D.hisa, cur = usd ? ' USD' : '';
    shell(el, 'hisa-earnings', {
      title: usd ? 'US dollar savings interest calculator' : 'Savings account interest calculator',
      intro: 'Compare what your balance earns at each account\'s published everyday rate.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'bal', 'Balance' + cur, usd ? 10000 : 20000, { min: 0 }) + fNum(p, 'months', 'Months', 12, { min: 1, max: 120, step: 1 }) + '</div>'; },
      calc: function (a) {
        var bal = a.n('bal'), m = a.n('months');
        var rows = list.map(function (h) { return { h: h, i: bal * (Math.pow(1 + h.rate / 12, m) - 1) }; }).sort(function (x, y) { return y.i - x.i; });
        return head('Most interest in ' + m + ' months', money2(rows[0].i) + cur + ' at ' + rows[0].h.name) + table(['Account', 'Everyday rate', 'Interest earned' + cur, 'Protection'], rows.map(function (r) { return [r.h.link ? '<a href="' + r.h.link + '">' + r.h.name + '</a>' : r.h.name, pct(r.h.rate, 2) + (r.h.rate_note ? ' <span class="ws-note">' + r.h.rate_note + '</span>' : ''), money2(r.i), r.h.ins]; })) +
          how('Everyday (non-promotional) rates, interest calculated daily and paid monthly, rates held steady for the period. Savings rates change often; our rate table shows the date each rate was checked.' + (usd ? ' Interest on US dollar accounts is taxable in Canada and is reported in Canadian dollars.' : ''));
      },
      next: usd ? [['/savings/usd-savings-accounts/', 'Best USD savings accounts'], ['/markets/how-to-buy-us-stocks/', 'How to buy US stocks']] : [['/savings/high-interest-savings-accounts/', 'Best savings accounts'], ['/vs/gic-vs-hisa/', 'GIC vs savings account']]
    });
  };

  /* ---------- Credit card cash back ---------- */
  W['card-cashback'] = function (el) {
    var K = D.cards || [];
    shell(el, 'card-cashback', {
      title: 'Cash back calculator',
      intro: 'Your yearly cash back after the card fee, at your own spending.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'spend', 'Monthly card spending', 2000, { min: 0 }) +
          fNum(p, 'rate', 'Cash back rate (%)', K[0] ? K[0].rate * 100 : 2, { min: 0, max: 10 }) +
          fNum(p, 'fee', 'Card fee per month', K[0] ? K[0].fee_month : 0, { min: 0, help: K[0] ? K[0].fee_note : '' }) + '</div>';
      },
      calc: function (a) {
        var yr = a.n('spend') * 12, cb = yr * a.n('rate') / 100, fee = a.n('fee') * 12, net = cb - fee;
        var be = a.n('rate') ? a.n('fee') / (a.n('rate') / 100) : 0;
        return head('Net cash back a year', money(net), net < 0) + kv([['Cash back earned', money(cb)], ['Card fees', money(fee)], ['Monthly spend to cover the fee', money(be)]]) +
          how('Cash back = yearly spending x the rate. Net = cash back minus fees. Fee waivers, caps on rewards and foreign transaction fees are listed in the card review.');
      },
      next: [['/reviews/wealthsimple/visa-infinite-card/', 'Wealthsimple credit card review'], ['/reviews/wealthsimple/membership-tiers/', 'Wealthsimple tiers']]
    });
  };

  /* ---------- CDIC deposit insurance checker ---------- */
  W['deposit-insurance'] = function (el) {
    var I = D.deposit_insurance;
    shell(el, 'deposit-insurance', {
      title: 'CDIC coverage checker',
      intro: 'CDIC covers eligible deposits up to ' + money(I.limit) + ' per category at each member institution. Enter your balances at one bank.',
      fields: function (p) { return '<div class="ws-w-grid">' + I.categories.map(function (c, i) { return fNum(p, 'c' + i, c, i === 0 ? 50000 : 0, { min: 0 }); }).join('') + '</div>'; },
      calc: function (a) {
        var tot = 0, cov = 0, rows = I.categories.map(function (c, i) { var b = a.n('c' + i), cv = Math.min(b, I.limit); tot += b; cov += cv; return [c, money(b), money(cv), b > I.limit ? '<span style="color:var(--ws-bad)">' + money(b - I.limit) + ' over</span>' : 'Fully covered']; });
        return head('Covered by CDIC', money(cov) + ' of ' + money(tot), cov < tot) + table(['Category', 'Your balance', 'Covered', 'Status'], rows) +
          how('Each category is covered separately up to ' + money(I.limit) + ' at each CDIC member, including principal and interest. Joint accounts, trust deposits and each registered plan type are separate categories. Mutual funds, stocks, ETFs and crypto are not covered by CDIC; securities at a CIRO dealer are protected by CIPF if the dealer fails. ' + (I.note || ''));
      },
      next: [['/reviews/wealthsimple/is-wealthsimple-safe/', 'Is Wealthsimple safe?'], ['/savings/high-interest-savings-accounts/', 'Best savings accounts']]
    });
  };

  /* ---------- Chequing account cost ---------- */
  W['chequing-cost'] = function (el) {
    shell(el, 'chequing-cost', {
      title: 'Chequing account cost calculator',
      intro: 'Your yearly cost or earnings at each account, based on your balance and monthly fee waivers.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'bal', 'Typical lowest monthly balance', 2000, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var b = a.n('bal');
        var rows = D.chequing.map(function (c) { var fee = (c.waive_bal != null && b >= c.waive_bal) ? 0 : c.fee; var i = b * (c.rate || 0); return { c: c, fee: fee * 12, i: i, net: i - fee * 12 }; }).sort(function (x, y) { return y.net - x.net; });
        return head('Best yearly result at your balance', money(rows[0].net) + ' at ' + rows[0].c.name) + table(['Account', 'Monthly fee', 'Fees a year', 'Interest a year', 'Net a year'], rows.map(function (r) { return [r.c.link ? '<a href="' + r.c.link + '">' + r.c.name + '</a>' : r.c.name, r.c.fee_text, money(r.fee), money(r.i), '<b>' + money(r.net) + '</b>']; })) +
          how('Fees are waived where your balance meets the published minimum. Interest uses the published rate on the whole balance. Other waivers, such as direct deposit or bundles, are listed in each account\'s details.');
      },
      next: [['/banking/best-chequing-accounts/', 'Best chequing accounts'], ['/banking/best-no-fee-chequing-accounts/', 'No-fee chequing']]
    });
  };

  /* ---------- Crypto fees ---------- */
  W['crypto-fee'] = function (el) {
    shell(el, 'crypto-fee', {
      title: 'Crypto trading fee calculator',
      intro: 'The published fee on one trade at each authorized platform.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Trade size (CAD)', 1000, { min: 0 }) + fNum(p, 'n', 'Trades per year', 12, { min: 1, step: 1 }) + '</div>'; },
      calc: function (a) {
        var amt = a.n('amt'), n = a.n('n');
        var rows = D.crypto.filter(function (c) { return c.fee_pct != null; }).map(function (c) { return { c: c, f: amt * c.fee_pct }; }).sort(function (x, y) { return x.f - y.f; });
        return head('Lowest published fee per trade', money2(rows[0].f) + ' at ' + rows[0].c.name) + table(['Platform', 'Published fee', 'Per trade', 'Per year'], rows.map(function (r) { return [r.c.link ? '<a href="' + r.c.link + '">' + r.c.name + '</a>' : r.c.name, r.c.fee_text, money2(r.f), money2(r.f * n)]; })) +
          '<p class="ws-note">Not shown because no single fee is published: ' + D.crypto.filter(function (c) { return c.fee_pct == null; }).map(function (c) { return c.name + ' (' + c.fee_text + ')'; }).join('; ') + '.</p>' +
          how('Uses each platform\'s published trading fee or spread for a standard market order. Some platforms build a spread into the price on top of, or instead of, a fee, which changes with the market. Deposit and withdrawal fees are extra where they apply.');
      },
      next: [['/compare/best-crypto-platforms/', 'Best crypto platforms'], ['/reviews/wealthsimple/crypto/', 'Wealthsimple Crypto review']]
    });
  };

  /* ---------- Wealthsimple tier ---------- */
  W['ws-tier'] = function (el) {
    var T = D.ws_tiers;
    shell(el, 'ws-tier', {
      title: 'Wealthsimple tier finder',
      intro: 'Enter the assets you hold or plan to move to Wealthsimple to see your tier and what changes at each level.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'assets', 'Total assets at Wealthsimple', 25000, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var x = a.n('assets'), t = T.list[0];
        T.list.forEach(function (z) { if (x >= z.from) t = z; });
        var nx = T.list.filter(function (z) { return z.from > x; })[0];
        var h = head('Your tier', t.name) + '<ul>' + t.perks.map(function (q) { return '<li>' + q + '</li>'; }).join('') + '</ul>';
        if (nx) h += msg('ok', money(nx.from - x) + ' more in assets reaches ' + nx.name + '.');
        h += table(['Feature'].concat(T.list.map(function (z) { return z.name; })), T.rows);
        h += how('Tier is set by the total of eligible assets across your Wealthsimple accounts' + (T.household ? ', and household members\' combined assets can count' : '') + '. WealthScale is independent and not affiliated with Wealthsimple.');
        return h;
      },
      next: [['/reviews/wealthsimple/membership-tiers/', 'Core vs Premium vs Generation'], ['/reviews/wealthsimple/fees/', 'Every Wealthsimple fee']]
    });
  };

  /* ---------- Benefit payment dates ---------- */
  W['benefit-dates'] = function (el) {
    var which = el.getAttribute('data-benefit') || 'all';
    var B = D.benefits;
    var keys = which === 'all' ? Object.keys(B) : [which];
    shell(el, 'benefit-dates', {
      title: which === 'all' ? 'Next government payment dates' : 'Next ' + B[which].name + ' payment',
      intro: 'Today is ' + NOW.toLocaleDateString('en-CA', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }) + '.',
      button: false,
      fields: function (p) { return keys.length > 1 ? fSel(p, 'b', 'Benefit', keys.map(function (k) { return [k, B[k].name]; }), keys[0]) : ''; },
      calc: function (a) {
        var k = keys.length > 1 ? a.val('b') : keys[0], b = B[k];
        var next = b.dates.filter(function (d) { return daysUntil(d) >= 0; });
        var h = next.length ? head('Next ' + b.name + ' payment', fmtDate(next[0], { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' })) +
          '<p class="ws-countdown">' + (daysUntil(next[0]) === 0 ? 'Today' : daysUntil(next[0]) + ' day' + (daysUntil(next[0]) === 1 ? '' : 's') + ' to go') + '</p>' : msg('warnmsg', 'The next dates have not been published yet.');
        h += table(['Payment', 'Date', 'Status'], b.dates.map(function (d) { var n = daysUntil(d); return [fmtDate(d, { month: 'long', year: 'numeric' }), fmtDate(d, { weekday: 'short', month: 'long', day: 'numeric', year: 'numeric' }), n < 0 ? 'Paid' : (n === 0 ? 'Today' : 'Upcoming')]; }), b.name + ' payment dates');
        if (b.note) h += '<p class="ws-note">' + b.note + '</p>';
        return h;
      },
      next: [['/benefits/', 'All benefit payment dates'], ['/benefits/cpp-oas-payment-dates/', 'CPP and OAS dates'], ['/benefits/gst-hst-credit/', 'GST/HST credit']]
    });
  };

  /* ---------- OAS clawback ---------- */
  W['oas-clawback'] = function (el) {
    var O = D.oas;
    shell(el, 'oas-clawback', {
      title: 'OAS clawback calculator',
      intro: 'The OAS recovery tax takes back 15% of net income above the threshold, up to the full pension.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'inc', 'Net income for ' + O.income_year + ' (line 23400)', 100000, { min: 0 }) + fRadio(p, 'age', 'Age', [['65', '65 to 74'], ['75', '75 and over']], '65') + '</div>'; },
      calc: function (a) {
        var inc = a.n('inc'), full = (a.val('age') === '75' ? O.max75 : O.max65) * 12;
        var cb = Math.min(full, Math.max(0, inc - O.threshold) * O.rate);
        return head('Estimated yearly OAS repayment', money(cb)) + kv([['Threshold (' + O.income_year + ' income)', money(O.threshold)], ['Yearly OAS at current rates', money(full)], ['OAS you keep', money(full - cb)], ['Income where OAS is fully clawed back', money(O.threshold + full / O.rate)]]) +
          how('Repayment = 15% of net income over the threshold, capped at the OAS you receive. It is collected by reducing monthly payments from July to June of the following year. Uses current quarterly OAS rates, which are indexed each quarter.');
      },
      next: [['/benefits/cpp-oas-payment-dates/', 'CPP and OAS payment dates'], ['/vs/tfsa-vs-rrsp/', 'TFSA withdrawals do not count']]
    });
  };

  /* ---------- CPP start age ---------- */
  W['cpp-start-age'] = function (el) {
    var P = D.cpp;
    shell(el, 'cpp-start-age', {
      title: 'CPP and OAS start age calculator',
      intro: 'How your monthly CPP and OAS change if you start earlier or later than 65.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'cpp', 'Your CPP at 65 (monthly)', P.avg65 || 900, { min: 0, help: 'From your My Service Canada Account statement. The ' + CUR + ' maximum at 65 is ' + money2(P.max65) + '.' }) + fNum(p, 'oas', 'OAS at 65 (monthly)', D.oas.max65, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var c = a.n('cpp'), o = a.n('oas'), rows = [];
        for (var age = 60; age <= 70; age++) {
          var cf = age < 65 ? 1 - P.early * 12 * (65 - age) : 1 + P.late * 12 * (age - 65);
          var of = age < 65 ? null : 1 + D.oas.defer * 12 * (age - 65);
          rows.push([age, pct(cf - 1, 1), money2(c * cf), of ? money2(o * of) : 'Not available', of ? money2(c * cf + o * of) : money2(c * cf)]);
        }
        return head('CPP at 70 vs 60', money2(c * (1 + P.late * 60)) + ' vs ' + money2(c * (1 - P.early * 60))) + table(['Start age', 'CPP change', 'CPP monthly', 'OAS monthly', 'Total monthly'], rows) +
          how('CPP falls ' + pct(P.early, 1) + ' for each month before 65 (up to ' + pct(P.early * 60, 0) + ' at 60) and rises ' + pct(P.late, 1) + ' for each month after 65 (up to ' + pct(P.late * 60, 0) + ' at 70). OAS starts at 65 at the earliest and rises ' + pct(D.oas.defer, 1) + ' for each month you defer, up to ' + pct(D.oas.defer * 60, 0) + ' at 70. Amounts are in today\'s dollars; both are indexed to inflation.');
      },
      next: [['/benefits/cpp-oas-payment-dates/', 'CPP and OAS payment dates']]
    });
  };

  /* ---------- GST/HST credit ---------- */
  W['gst-credit'] = function (el) {
    var G = D.gst_credit;
    shell(el, 'gst-credit', {
      title: 'GST/HST credit calculator',
      intro: 'Estimate your credit for ' + G.period + ', based on your ' + G.income_year + ' family net income.',
      fields: function (p) { return '<div class="ws-w-grid">' + fRadio(p, 'st', 'Marital status', [['s', 'Single'], ['m', 'Married or common-law']], 's') + fNum(p, 'kids', 'Children under 19', 0, { min: 0, max: 15, step: 1 }) + fNum(p, 'inc', 'Adjusted family net income (' + G.income_year + ')', 30000, { min: 0 }) + fNum(p, 'own', 'Your own net income (singles: same as above)', 30000, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var single = a.val('st') === 's', k = Math.round(a.n('kids')), inc = a.n('inc'), own = single ? inc : a.n('own');
        // A single parent claims the adult amount for one child (eligible dependant) and gets the full single supplement.
        var base = single ? (k > 0 ? 2 * G.adult + (k - 1) * G.child : G.adult) : 2 * G.adult + k * G.child;
        var supp = 0;
        if (single && k === 0) supp = Math.min(G.single_supp, Math.max(0, (own - G.supp_base) * G.supp_rate));
        if (single && k > 0) supp = G.single_supp;
        var full = base + supp, red = Math.max(0, inc - G.threshold) * G.reduce, credit = Math.max(0, full - red);
        var h = head('Estimated yearly credit', money2(credit)) + kv([['Each quarterly payment', money2(credit / 4)], ['Maximum before income reduction', money2(full)], ['Income reduction', money2(Math.min(full, red))]]);
        if (G.note) h += msg('ok', G.note);
        h += how('Base amounts for ' + G.period + ': ' + money(G.adult) + ' for you, ' + money(G.adult) + ' for a spouse or partner (or for one child of a single parent), ' + money(G.child) + ' per other child, plus a single supplement of up to ' + money(G.single_supp) + '. The total is reduced by ' + pct(G.reduce, 0) + ' of adjusted family net income over ' + money(G.threshold) + '. Credits under $50 a quarter are paid in one July payment.');
        return h;
      },
      next: [['/benefits/gst-hst-credit/', 'GST/HST credit dates and amounts'], ['/benefits/', 'All benefit dates']]
    });
  };

  /* ---------- RRSP withdrawal ---------- */
  W['rrsp-withdrawal'] = function (el) {
    shell(el, 'rrsp-withdrawal', {
      title: 'RRSP withdrawal tax calculator',
      intro: 'Tax withheld at source on an RRSP withdrawal, and the tax you may owe when you file.',
      fields: function (p) { return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'amt', 'Withdrawal amount', 10000, { min: 0 }) + fNum(p, 'inc', 'Other taxable income this year', MEM.get('income', 60000), { min: 0 }) + '</div>'; },
      calc: function (a) {
        var prov = a.val('prov'), amt = a.n('amt'), W8 = D.rrsp.withholding, br = prov === 'QC' ? W8.QC : W8.other, rate = br[br.length - 1][1];
        for (var i = 0; i < br.length; i++) if (br[i][0] == null || amt <= br[i][0]) { rate = br[i][1]; break; }
        var wh = amt * rate, tax = C.tax(prov, a.n('inc') + amt).total - C.tax(prov, a.n('inc')).total;
        return head('Withheld at source', money(wh)) + kv([['Withholding rate', pct(rate, 0)], ['Estimated tax on the withdrawal', money(tax)], [tax > wh ? 'More owed at tax time' : 'Possible refund at tax time', money(Math.abs(tax - wh))], ['RRSP room', 'Not restored']]) +
          how('Withholding depends only on the size of each withdrawal' + (prov === 'QC' ? ' (Quebec: federal plus provincial rates)' : '') + '. The withdrawal is added to your income, so your final tax is based on your marginal rate. Withdrawals under the Home Buyers\' Plan and Lifelong Learning Plan have no withholding.');
      },
      next: [['/accounts/rrsp/', 'RRSP guide'], ['/accounts/home-buyers-plan/', 'Home Buyers\' Plan']]
    });
  };

  /* ---------- Tax software picker ---------- */
  W['tax-software-picker'] = function (el) {
    shell(el, 'tax-software-picker', {
      title: 'Which tax software fits your return?',
      intro: 'Tick what applies. We show the lowest tier of each NETFILE-certified product that covers your situation, and flag anything the company does not confirm.',
      button: 'Show matches',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fRadio(p, 'self', 'Self-employment or business income?', [['n', 'No'], ['y', 'Yes']], 'n') + fRadio(p, 'rent', 'Rental income?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fRadio(p, 'inv', 'Investments with capital gains?', [['n', 'No'], ['y', 'Yes']], 'n') + fRadio(p, 'qc', 'Filing a Quebec return?', [['n', 'No'], ['y', 'Yes']], 'n') + fRadio(p, 'help', 'Want an expert to review or file?', [['n', 'No'], ['y', 'Yes']], 'n') + '</div>';
      },
      calc: function (a) {
        var need = ['self', 'rent', 'inv', 'qc', 'help'].filter(function (k) { return a.val(k) === 'y'; });
        var rows = [];
        D.tax_software.forEach(function (s) {
          var pick = null, unsure = false;
          for (var i = 0; i < s.tiers.length && !pick; i++) {
            var t = s.tiers[i], vals = need.map(function (k) { return t[k]; });
            if (vals.every(function (x) { return x === true; })) pick = t;
          }
          if (!pick) for (var j = 0; j < s.tiers.length && !pick; j++) {
            var t2 = s.tiers[j], v2 = need.map(function (k) { return t2[k]; });
            if (v2.every(function (x) { return x !== false; })) { pick = t2; unsure = true; }
          }
          rows.push([s.link ? '<a href="' + s.link + '">' + s.name + '</a>' : s.name, pick ? pick.name : 'No tier covers this', pick ? pick.price_text : '\u2014', pick ? (unsure ? 'Not confirmed by the company' : 'Yes') : 'No']);
        });
        var good = rows.filter(function (r) { return r[3] === 'Yes'; }).length;
        return head('Products confirmed for your situation', String(good)) + table(['Software', 'Lowest tier that fits', 'Price', 'Confirmed?'], rows) +
          how('Every product listed is NETFILE-certified for the ' + D.tax_software_year + ' tax year. "Not confirmed" means the company does not state on its pricing pages whether that tier handles your situation, so please check before you pay.');
      },
      next: [['/compare/best-tax-software/', 'Best tax software'], ['/reviews/wealthsimple/tax/', 'Wealthsimple Tax review']]
    });
  };

  /* ---------- Broker match (filter by needs) ---------- */
  W['broker-match'] = function (el) {
    shell(el, 'broker-match', {
      title: 'Find brokers that match your needs',
      intro: 'Tick the features you need. We list every broker that has them, ranked by our published score.',
      button: 'Show matches',
      fields: function (p) {
        var feats = D.broker_features;
        return '<div class="ws-radio">' + feats.map(function (f) { return '<label><input type="checkbox" name="' + f[0] + '" value="1"> ' + f[1] + '</label>'; }).join('') + '</div>';
      },
      calc: function (a) {
        var want = D.broker_features.filter(function (f) { var n = a.form.querySelector('[name="' + f[0] + '"]'); return n && n.checked; }).map(function (f) { return f[0]; });
        var rows = D.brokers.filter(function (b) { return want.every(function (w) { return b.flags && b.flags.indexOf(w) >= 0; }); }).sort(function (x, y) { return (y.score || 0) - (x.score || 0); });
        if (!rows.length) return msg('warnmsg', 'No broker we cover has every feature you ticked. Try removing one.');
        return head('Brokers that match', String(rows.length)) + table(['Rank', 'Broker', 'Our score', 'Canadian trades', 'US trades', 'FX fee'], rows.map(function (b, i) { return [i + 1, '<a href="' + b.review + '">' + b.name + '</a>', (b.score || 0).toFixed(1) + ' / 5', b.cad_text, b.us_text, b.fx_text]; })) +
          how('Matches use the features each broker publishes. Ranking uses the overall score from our broker methodology, which is never changed by partnerships.');
      },
      next: [['/compare/best-online-brokers/', 'Best online brokers'], ['/methodology/brokers/', 'How we rate brokers']]
    });
  };

  /* ---------- Transfer fee ---------- */
  W['transfer-fee'] = function (el) {
    shell(el, 'transfer-fee', {
      title: 'Account transfer fee calculator',
      intro: 'What it costs to move accounts out of your current institution, and which receiving brokers cover the fee.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'n', 'Number of accounts to move', 2, { min: 1, max: 10, step: 1 }) + fNum(p, 'fee', 'Transfer-out fee per account at your current institution', 150, { min: 0, help: 'Many banks and brokers charge a fee per account; check your fee schedule.' }) + fNum(p, 'val', 'Value per account', 30000, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var n = a.n('n'), fee = a.n('fee'), v = a.n('val'), cost = n * fee;
        var rows = D.brokers.filter(function (b) { return b.transfer_in_text; }).map(function (b) {
          var known = b.transfer_min != null || (b.transfer_max != null && !b.per_client);
          var ok = b.transfer_min == null ? known : v * n >= b.transfer_min;
          var cov = 0;
          if (ok) cov = b.per_client ? Math.min(cost, b.transfer_max == null ? cost : b.transfer_max) : n * Math.min(fee, b.transfer_max == null ? fee : b.transfer_max);
          return ['<a href="' + b.review + '">' + b.name + '</a>', b.transfer_in_text, known ? money(cov) : 'Depends on eligibility', known ? money(cost - cov) : '\u2014']; });
        return head('Transfer-out fees you would pay', money(cost)) + table(['Receiving broker', 'Published transfer fee policy', 'Covered for you', 'Left to pay'], rows) + how('Coverage depends on each broker\'s published minimum and cap, and usually requires a request with your statement showing the fee. Transfers between registered accounts must be done institution to institution to keep them tax-free.');
      },
      next: [['/learn/transfer-investment-account/', 'How to transfer an account']]
    });
  };

  /* ---------- Generic countdown ---------- */
  W['countdown'] = function (el) {
    var d = el.getAttribute('data-date'), lab = el.getAttribute('data-label') || 'Deadline';
    el.classList.add('ws-widget');
    var n = daysUntil(d);
    el.innerHTML = '<div class="ws-w-head"><div class="ws-w-title" role="heading" aria-level="3">' + esc(lab) + '</div><p>' + fmtDate(d, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }) + '</p></div><div class="ws-w-body"><p class="ws-countdown">' + (n > 0 ? n + ' day' + (n === 1 ? '' : 's') + ' left' : (n === 0 ? 'Today' : 'Passed')) + '</p></div>';
  };

  /* ---------- Table filter (progressive enhancement on a static table) ---------- */
  W['table-filter'] = function (el) {
    var tbl = el.querySelector('table'); if (!tbl) return;
    var box = document.createElement('div'); box.className = 'ws-filter';
    box.innerHTML = '<label class="ws-sr" for="wsf' + (++uid) + '">Filter this table</label><input type="search" id="wsf' + uid + '" placeholder="Type to filter, e.g. FHSA, USD, $0">';
    el.insertBefore(box, el.firstChild);
    var inp = box.querySelector('input');
    inp.addEventListener('input', function () {
      var q = inp.value.toLowerCase().trim().split(/\s+/);
      Array.prototype.forEach.call(tbl.tBodies[0].rows, function (r) { var t = r.textContent.toLowerCase(); r.style.display = q.every(function (w) { return t.indexOf(w) >= 0; }) ? '' : 'none'; });
    });
    Array.prototype.forEach.call(tbl.tHead ? tbl.tHead.rows[0].cells : [], function (th, i) {
      th.style.cursor = 'pointer'; th.setAttribute('tabindex', '0'); th.setAttribute('aria-sort', 'none'); th.title = 'Sort by this column';
      function sort() {
        var asc = th.getAttribute('aria-sort') !== 'ascending';
        Array.prototype.forEach.call(tbl.tHead.rows[0].cells, function (o) { o.setAttribute('aria-sort', 'none'); });
        th.setAttribute('aria-sort', asc ? 'ascending' : 'descending');
        var rows = Array.prototype.slice.call(tbl.tBodies[0].rows);
        rows.sort(function (a, b) {
          var x = a.cells[i].textContent.trim(), y = b.cells[i].textContent.trim();
          var nx = parseFloat(x.replace(/[^0-9.\-]/g, '')), ny = parseFloat(y.replace(/[^0-9.\-]/g, ''));
          var c = (isFinite(nx) && isFinite(ny)) ? nx - ny : x.localeCompare(y);
          return asc ? c : -c;
        });
        rows.forEach(function (r) { tbl.tBodies[0].appendChild(r); });
      }
      th.addEventListener('click', sort);
      th.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sort(); } });
    });
  };

  function byId(id) { return D.brokers.filter(function (b) { return b.id === id; })[0]; }
  function tierRate(tiers, amt) {
    for (var i = 0; i < tiers.length; i++) { var t = tiers[i]; if (t[0] == null || amt <= t[0]) return t[1]; }
    return tiers[tiers.length - 1][1];
  }
  /* amt is in CAD; brokers that set tiers in US dollars are looked up on amt / xr (CAD per US$1). */
  function fxRate(b, amt, xr) {
    if (!b.fx_tiers) return b.fx_pct;
    var base = b.tiers_ccy === 'USD' ? amt / (xr || D.usdcad_example) : amt;
    return tierRate(b.fx_tiers, base);
  }
  function fxCost(b, amt, xr) { return Math.max(fxRate(b, amt, xr) * amt, b.fx_fixed || 0); }
  C.fxCost = function (b, amt, xr) { return fxCost(b, amt, xr); };
  C.fxRate = function (b, amt, xr) { return fxRate(b, amt, xr); };

  /* =====================================================================
   * 5. START
   * ===================================================================== */
  function start() {
    var els = document.querySelectorAll('[data-ws-widget]');
    Array.prototype.forEach.call(els, function (el) {
      if (el.getAttribute('data-ws-ready')) return;
      var name = el.getAttribute('data-ws-widget');
      if (!W[name]) { if (window.console) console.warn('WealthScale widget not found: ' + name); return; }
      el.setAttribute('data-ws-ready', '1');
      try { W[name](el); } catch (e) { el.innerHTML = '<p class="ws-note">This calculator could not load. Please refresh the page.</p>'; if (window.console) console.error(e); }
    });
  }
  window.WS.start = start;
  window.WS.widgets = Object.keys(W);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
