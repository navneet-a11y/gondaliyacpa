# -*- coding: utf-8 -*-
"""Featured / Open Graph cards, 1200x630, in the layout Navneet supplied.

Two deliberate departures from the example card:
  - the logo is Corp Nil Filing, not Gondaliya CPA, as asked.
  - the example's "1300+ 5-star Google reviews" line is REMOVED. Plan line
    1615 bars corpnilfilingfor300.ca from publishing any review count, client
    count or years-in-practice figure until the claim-consistency audit is
    signed, and line 2053 lists them among the banned items. It is replaced
    with "Registered EFILE electronic filer", the only permitted CRA phrase.

Rendered by headless Chromium at device scale 2, then downsampled, so the
Poppins and Lato text is crisp at 1200x630.
"""
import base64, io, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = ('/tmp/claude-0/-home-user-gondaliyacpa/'
           'b101a947-acc7-5358-b348-fefda00aad11/scratchpad')
FONTS, ASSETS = SCRATCH + '/fonts', SCRATCH + '/og'
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

def b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()

def font_face(fam, weight, file):
    return ("@font-face{font-family:'%s';font-weight:%d;font-style:normal;"
            "src:url(data:font/ttf;base64,%s) format('truetype');}"
            % (fam, weight, b64(os.path.join(FONTS, file))))

CARDS = [
 dict(out='og-mandatory-t2-e-filing-after-2023.png',
      eyebrow='T2 E-FILING &middot; PAPER RETURNS &middot; NIL T2 &middot; 2026',
      h1='Mandatory T2 E-Filing for Tax Years Starting After 2023',
      sub='Electronic filing is mandatory for virtually all corporations. '
          'A paper T2 draws two separate penalties.',
      chips=[('Paper is not an option', 'blue'),
             ('$1,000.00 plus $100.00', 'amber'),
             ('Nil is not exempt', 'green')]),
 dict(out='og-schedule-50-and-the-10-percent-shareholder-rule.png',
      eyebrow='SCHEDULE 50 &middot; SHAREHOLDERS &middot; NIL T2 &middot; 2026',
      h1='Schedule 50 and the 10% Shareholder Rule',
      sub='Every shareholder at 10% or more appears. Ownership does not switch '
          'off because the corporation stopped trading.',
      chips=[('10% or more', 'blue'),
             ('Read per class', 'amber'),
             ('Nil returns too', 'green')]),
]

CSS = """
%(faces)s
*{margin:0;padding:0;box-sizing:border-box}
body{width:1200px;height:630px;overflow:hidden;background:#0f2a4a;
     font-family:'Lato',sans-serif;-webkit-font-smoothing:antialiased}
.card{position:relative;width:1200px;height:630px;background:#0f2a4a;overflow:hidden}
.blob{position:absolute;right:-150px;top:-230px;width:700px;height:700px;
      border-radius:50%%;background:#15355c}
.l{position:absolute;left:40px;top:40px;width:770px}
.eyebrow{display:inline-block;border:2px solid rgba(255,255,255,.55);border-radius:40px;
   padding:9px 18px;font-family:'Poppins',sans-serif;font-weight:700;font-size:15px;
   letter-spacing:.06em;color:#fff}
h1{font-family:'Poppins',sans-serif;font-weight:700;font-size:48px;line-height:1.13;
   color:#fff;margin:26px 0 0;letter-spacing:-.01em}
h1.sm{font-size:42px}
.sub{font-size:21px;line-height:1.42;color:rgba(255,255,255,.88);margin:16px 0 0}
.chips{display:flex;gap:14px;margin:24px 0 0;flex-wrap:wrap}
.chip{font-family:'Poppins',sans-serif;font-weight:600;font-size:16px;
      border-radius:10px;padding:13px 18px;white-space:nowrap}
.blue{background:#e8f1fb;color:#1b3a6b}
.amber{background:#fdf3e0;color:#8a5a12}
.green{background:#e7f5ec;color:#1d6b3f}
.firm{font-size:16px;color:rgba(255,255,255,.55);margin:22px 0 0}
.logobox{position:absolute;left:40px;bottom:40px;background:#fff;border-radius:12px;
   padding:14px 20px;display:flex;align-items:center}
.logobox img{height:56px;display:block}
.r{position:absolute;right:72px;top:268px;width:280px;text-align:center}
.r .ring{width:216px;height:216px;border-radius:50%%;border:8px solid #2087c9;
   margin:0 auto;overflow:hidden;background:#dfe6ef}
.r .ring img{width:100%%;height:100%%;display:block}
.wb{font-size:17px;color:rgba(255,255,255,.80);margin:18px 0 0}
.name{display:inline-block;background:#fff;border-radius:40px;padding:12px 26px;
   font-family:'Poppins',sans-serif;font-weight:700;font-size:19px;color:#0f2a4a;
   margin:10px 0 0;white-space:nowrap}
.pub{font-family:'Poppins',sans-serif;font-weight:600;font-size:16px;color:#f2b544;
   margin:14px 0 0}
"""

TPL = """<!doctype html><html><head><meta charset="utf-8"><style>%(css)s</style></head>
<body><div class="card"><div class="blob"></div>
<div class="l">
  <span class="eyebrow">%(eyebrow)s</span>
  <h1 class="%(h1cls)s">%(h1)s</h1>
  <p class="sub">%(sub)s</p>
  <div class="chips">%(chips)s</div>
  <p class="firm">Gondaliya CPA Professional Corporation &middot; Toronto, Ontario
     &middot; Registered EFILE electronic filer</p>
</div>
<div class="logobox"><img src="data:image/png;base64,%(logo)s" alt=""></div>
<div class="r">
  <div class="ring"><img src="data:image/png;base64,%(portrait)s" alt=""></div>
  <p class="wb">Written by</p>
  <span class="name">Sharad Gondaliya, CPA</span>
  <p class="pub">Published 22 October 2026</p>
</div>
</div></body></html>"""


def build():
    faces = ''.join([font_face('Poppins', 500, 'Poppins-500.ttf'),
                     font_face('Poppins', 600, 'Poppins-600.ttf'),
                     font_face('Poppins', 700, 'Poppins-700.ttf'),
                     font_face('Lato', 400, 'Lato-400.ttf'),
                     font_face('Lato', 700, 'Lato-700.ttf')])
    css = CSS % {'faces': faces}
    logo, portrait = b64(ASSETS + '/logo.png'), b64(ASSETS + '/portrait.png')
    from PIL import Image
    for c in CARDS:
        chips = ''.join('<span class="chip %s">%s</span>' % (k, t) for t, k in c['chips'])
        htmlfile = os.path.join(SCRATCH, 'card.html')
        open(htmlfile, 'w', encoding='utf-8').write(TPL % {
            'css': css, 'eyebrow': c['eyebrow'], 'h1': c['h1'],
            'h1cls': 'sm' if len(c['h1']) > 44 else '', 'sub': c['sub'],
            'chips': chips, 'logo': logo, 'portrait': portrait})
        raw = os.path.join(SCRATCH, 'raw.png')
        if os.path.exists(raw):
            os.remove(raw)
        subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-sandbox',
                        '--hide-scrollbars', '--force-device-scale-factor=2',
                        # headless reserves ~87px of the window for chrome, so a
                        # 1200x630 window gives a 1200x543 viewport and clips the
                        # bottom of the card. Capture tall, then crop the card.
                        '--window-size=1200,800', '--disable-component-update',
                        '--no-first-run', '--disable-features=Translate', '--virtual-time-budget=4000',
                        '--screenshot=' + raw, 'file://' + htmlfile],
                       check=True, capture_output=True, timeout=180)
        if not os.path.exists(raw):
            raise SystemExit('chromium produced no screenshot for ' + c['out'])
        im = Image.open(raw).convert('RGB')
        im = im.crop((0, 0, 1200 * 2, 630 * 2))      # the card sits at top: 0
        im = im.resize((1200, 630), Image.LANCZOS)
        out = os.path.join(HERE, c['out'])
        im.save(out, 'PNG', optimize=True)
        print('%-56s %s  %d bytes' % (c['out'], im.size, os.path.getsize(out)))

if __name__ == '__main__':
    build()
