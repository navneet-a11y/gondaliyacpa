// Renders 1200x630 featured images in the site's existing format.
// Usage: node render.mjs <assets_dir> <specs.json> <out_dir>
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const [assets, specFile, out] = process.argv.slice(2);
const b64 = (f) => fs.readFileSync(`${assets}/${f}`).toString('base64');
const font = (w) => `@font-face{font-family:P;font-weight:${w};src:url(data:font/woff2;base64,${b64(`poppins-latin-${w}-normal.woff2`)}) format('woff2')}`;
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const page = (s) => `<!doctype html><html><head><style>
${[400, 500, 600, 700].map(font).join('')}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1200px;height:630px;background:#0f2a4a;font-family:P,sans-serif;position:relative;overflow:hidden;color:#fff}
.circ{position:absolute;left:870px;top:-200px;width:590px;height:590px;border-radius:50%;background:#15355c}
.tags{position:absolute;left:40px;top:44px;height:33px;padding:0 16px;border:1.5px solid rgba(255,255,255,.45);border-radius:17px;font-weight:700;font-size:13px;letter-spacing:0;line-height:30px;white-space:nowrap}
.title{position:absolute;left:40px;top:100px;width:${s.titleWidth || 820}px;font-weight:700;font-size:${s.titleSize || 44}px;line-height:1.17;letter-spacing:-.2px}
.sub{position:absolute;left:40px;top:${s.subTop || 214}px;width:720px;font-weight:400;font-size:22px;line-height:1.48;color:#eaf3fc}
.chips{position:absolute;left:40px;top:296px;display:flex;gap:11px}
.chip{height:43px;padding:0 18px;border-radius:8px;font-weight:700;font-size:16.5px;line-height:43px;white-space:nowrap}
.c1{background:#ecf3fd;color:#0f2a4a}.c2{background:#fdf7e8;color:#9a7416}.c3{background:#ecf7f0;color:#186839}
.foot{position:absolute;left:40px;top:364px;font-size:15px;color:#9fb3cc;white-space:nowrap}
.logo{position:absolute;left:40px;top:507px}
.photo{position:absolute;left:909px;top:270px;width:225px;height:225px}
.wb{position:absolute;left:921px;width:200px;top:500px;text-align:center;font-weight:700;font-size:17px}
.name{position:absolute;left:886px;width:271px;top:528px;height:43px;border-radius:22px;background:#fff;color:#0f2a4a;text-align:center;font-weight:700;font-size:18px;line-height:43px}
.pub{position:absolute;left:871px;width:300px;top:584px;text-align:center;font-weight:700;font-size:14px;color:#d6ab35}
</style></head><body>
<div class="circ"></div>
<div class="tags">${s.tags.map(esc).join(' · ')}</div>
<div class="title">${esc(s.line1)}<br>${esc(s.line2)}</div>
<div class="sub">${esc(s.sub)}</div>
<div class="chips"><div class="chip c1">${esc(s.chips[0])}</div><div class="chip c2">${esc(s.chips[1])}</div><div class="chip c3">${esc(s.chips[2])}</div></div>
<div class="foot">Gondaliya CPA Professional Corporation &nbsp;·&nbsp; Toronto, Ontario &nbsp;·&nbsp; Registered Ontario CPA Firm</div>
<img class="logo" src="data:image/png;base64,${b64('logo.png')}">
<img class="photo" src="data:image/png;base64,${b64('photo.png')}">
<div class="wb">Written by</div><div class="name">Sharad Gondaliya, CPA</div>
<div class="pub">Published ${esc(s.published)}</div>
</body></html>`;
const specs = JSON.parse(fs.readFileSync(specFile, 'utf8'));
const br = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await br.newPage({ viewport: { width: 1200, height: 630 } });
for (const s of specs) {
  await p.setContent(page(s));
  await p.evaluate(() => document.fonts.ready);
  const over = await p.evaluate(() => {
    const r = (q) => document.querySelector(q).getBoundingClientRect();
    return { title: r('.title').bottom, sub: r('.sub').bottom, chips: r('.chips').right, tags: r('.tags').right, subLines: Math.round(r('.sub').height / 32.7) };
  });
  await p.screenshot({ path: `${out}/${s.file}`, type: 'png' });
  console.log(s.file, JSON.stringify(over));
}
await br.close();
