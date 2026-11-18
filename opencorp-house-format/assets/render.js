// Render house-format assets: PNG infographics at 1200x675 and Letter PDF checklists.
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch();
  for (const j of jobs) {
    const p = await b.newPage({ viewport: { width: 1200, height: 675 } });
    await p.goto('file://' + j.html);
    await p.waitForTimeout(800);
    if (j.kind === 'pdf') {
      await p.pdf({ path: j.out, format: 'Letter', printBackground: true, displayHeaderFooter: true,
        margin: { top: '0.55in', bottom: '0.85in', left: '0.6in', right: '0.6in' },
        headerTemplate: '<span></span>',
        footerTemplate: '<div style="width:100%;font-family:Arial,sans-serif;font-size:8px;color:#5a6b7b;padding:0 0.6in;border-top:1px solid #d8e0e8;padding-top:5px;">Open Corporation for $35 is a department of Gondaliya CPA. Phone 647-212-9559 | info@gondaliyacpa.ca | opencorporationfor35.ca. This checklist is general information, not tax, legal or financial advice. <span style="float:right">Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>' });
    } else {
      const over = await p.evaluate(() => {
        const h = document.querySelector('.bar h1'); const w = document.querySelector('.wrap');
        return { title: h.scrollWidth, content: w.getBoundingClientRect().bottom };
      });
      if (over.title > 1096 || over.content > 613) console.log('CHECK FIT', j.out, JSON.stringify(over));
      await p.screenshot({ path: j.out, type: 'png' });
    }
    await p.close();
  }
  await b.close();
  console.log('rendered', jobs.length);
})();
