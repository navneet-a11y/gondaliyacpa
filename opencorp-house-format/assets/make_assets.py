#!/usr/bin/env python3
"""Render the house-format infographics, Why-choose-us images and checklist PDFs.

  python3 make_assets.py          # writes HTML into build/, then renders with render.js
Output goes to ../posts/<dir>/images/.
"""
import html, json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from config import POSTS  # noqa: E402

E = lambda s: html.escape(s, quote=True)
LOGO = os.path.join(HERE, "logo.png")
COLORS = [("#e8f1fc", "#1c6dd0", "#1c6dd0"), ("#e3f4f4", "#0c8f8f", "#0c8f8f"), ("#fbf3dc", "#c9991f", "#9a7416"),
          ("#e6f5ec", "#1f8a4c", "#1f8a4c"), ("#fbeae8", "#c0392b", "#c0392b"), ("#eef1f6", "#0f2a4a", "#0f2a4a")]
FONT = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">'
BASE = """*{box-sizing:border-box;margin:0;padding:0}
body{width:1200px;height:675px;font-family:Poppins,Arial,sans-serif;background:#fff;color:#0f2a4a;position:relative;overflow:hidden}
.bar{background:#112b4c;height:96px;display:flex;align-items:center;padding:0 52px;border-bottom:7px solid #0c8f8f}
.bar h1{color:#fff;font-size:30px;font-weight:800;white-space:nowrap}
.wrap{padding:30px 52px 0}
.sub{font-size:18px;color:#5a6b7b;margin-bottom:22px}
.foot{position:absolute;left:0;right:0;bottom:0;height:62px;border-top:1px solid #d8e0e8;display:flex;align-items:center;justify-content:space-between;padding:0 52px;font-size:15px;color:#5a6b7b}
.foot b{color:#0f2a4a;font-weight:800}
.foot img{height:40px}
"""


def foot():
    return f'<div class="foot"><span><b>opencorporationfor35.ca</b> &nbsp;|&nbsp; Backed by Gondaliya CPA</span><img src="file://{LOGO}"></div>'


def compare(i):
    two = len(i["rows"][0]) == 2
    rows = "".join((f'<tr><td>{E(r[0])}</td><td>{E(r[1])}</td></tr>' if two else f'<tr><td class="k">{E(r[0])}</td><td>{E(r[1])}</td><td>{E(r[2])}</td></tr>') for r in i["rows"])
    n = len(i["rows"])
    fs = 18 if n <= 5 else 16.5
    pad = 13 if n <= 5 else 10
    css = f"""table{{width:100%;border-collapse:collapse;font-size:{fs}px}}
th{{background:#0f2a4a;color:#fff;text-align:left;padding:12px 16px;font-weight:700}}
td{{padding:{pad}px 16px;border:1px solid #d8e0e8;line-height:1.35}}
tr:nth-child(even) td{{background:#f5f8fb}}
td.k{{font-weight:700;color:#15355c;width:32%}}
th:nth-child(2){{background:#1c6dd0}} th:nth-child(3){{background:#0c8f8f}}"""
    if two:
        css += "th:nth-child(1){background:#1c6dd0} th:nth-child(2){background:#0c8f8f} td{width:50%}"
    head = (f'<tr><th>{E(i["cols"][0])}</th><th>{E(i["cols"][1])}</th></tr>' if two else f'<tr><th></th><th>{E(i["cols"][0])}</th><th>{E(i["cols"][1])}</th></tr>')
    return css, f'<table>{head}{rows}</table>'


def cards(i):
    n = len(i["cards"])
    cols = 3 if n > 4 else n
    css = f""".grid{{display:grid;grid-template-columns:repeat({cols},1fr);gap:16px}}
.c{{border-radius:12px;padding:16px 18px;border-top:6px solid;min-height:{180 if n <= 3 else 190}px}}
.c .w{{font-size:24px;font-weight:800;margin-bottom:4px;line-height:1.2}}
.c .t{{font-size:18px;font-weight:700;color:#0f2a4a;margin-bottom:6px;line-height:1.3}}
.c .x{{font-size:15px;line-height:1.45;color:#1d2733}}"""
    if n <= 3:  # few cards: fill the frame
        css += ".c{min-height:370px;padding:28px 26px} .c .w{font-size:44px;margin-bottom:14px} .c .t{font-size:24px;margin-bottom:12px} .c .x{font-size:19px;line-height:1.55}"
    out = []
    for k, (w, t, x) in enumerate(i["cards"]):
        bg, bd, tx = COLORS[k % len(COLORS)]
        out.append(f'<div class="c" style="background:{bg};border-color:{bd}"><div class="w" style="color:{tx}">{E(w)}</div><div class="t">{E(t)}</div><div class="x">{E(x)}</div></div>')
    return css, f'<div class="grid">{"".join(out)}</div>'


def infographic(i):
    css, body = (compare if i["kind"] == "compare" else cards)(i)
    return (f'<!doctype html><html><head><meta charset="utf-8">{FONT}<style>{BASE}{css}</style></head><body>'
            f'<div class="bar"><h1>{E(i["title"])}</h1></div><div class="wrap"><div class="sub">{E(i["sub"])}</div>{body}</div>{foot()}</body></html>')


def why(p):
    topic_t, topic_x = p["why"]
    fifth = p.get("remote", ("Filed same day, remotely", "Complete online filings usually come back the same day, wherever you are."))
    items = [("Run the numbers first", "A free CPA consultation before anything is filed."),
             ("A department of Gondaliya CPA", "CPA Ontario firm registration 61330051."),
             ("From $35 including HST", "Plus government fees, shown on their own line."),
             (topic_t, topic_x), fifth,
             ("30-day money-back guarantee", "Plus our 60-day fee-matching policy.")]
    i = {"title": "Why Business Owners Choose Open Corporation for $35", "sub": f"For {p['topic']}, backed by a CPA firm",
         "kind": "cards", "cards": [[str(k + 1).zfill(2), t, x] for k, (t, x) in enumerate(items)]}
    return infographic(i)


def checklist(p):
    secs = p["checklist"]
    def sec(n, s):
        lis = "".join(f'<li><span class="bx"></span>{E(x)}</li>' for x in s[1])
        return f'<div class="sec"><div class="h"><span class="n">{n}</span>{E(s[0])}</div><ul>{lis}</ul></div>'
    page1 = "".join(sec(k + 1, s) for k, s in enumerate(secs[:4]))
    page2 = "".join(sec(k + 5, s) for k, s in enumerate(secs[4:]))
    return f"""<!doctype html><html><head><meta charset="utf-8">{FONT}<style>

*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Poppins,Arial,sans-serif;color:#1d2733;font-size:11pt}}
.top{{background:#112b4c;color:#fff;border-radius:10px;padding:18px 22px;border-bottom:5px solid #0c8f8f;margin-bottom:16px;display:flex;justify-content:space-between;align-items:center}}
.top h1{{font-size:20pt;font-weight:800;line-height:1.2}}
.top p{{font-size:10pt;color:#cfe2f8;margin-top:4px}}
.top img{{height:44px;background:#fff;border-radius:8px;padding:4px 8px}}
.sec{{border:1px solid #d8e0e8;border-left:5px solid #1c6dd0;border-radius:10px;padding:12px 16px;margin-bottom:14px;break-inside:avoid}}
.h{{font-size:13pt;font-weight:700;color:#0f2a4a;margin-bottom:8px;display:flex;align-items:center;gap:10px}}
.n{{display:inline-flex;width:26px;height:26px;border-radius:7px;background:#0f2a4a;color:#fff;font-size:11pt;align-items:center;justify-content:center}}
ul{{list-style:none}}
li{{display:flex;gap:10px;align-items:flex-start;padding:5px 0;border-bottom:1px dashed #d8e0e8;font-size:11pt}}
li:last-child{{border-bottom:none}}
.bx{{flex:0 0 auto;width:14px;height:14px;border:2px solid #0c8f8f;border-radius:3px;margin-top:4px}}
.brk{{break-before:page}}
.book{{background:#fbf3dc;border:1px solid #ecd79a;border-radius:10px;padding:14px 18px;margin-top:6px}}
.book b{{color:#0f2a4a}}
.ft{{position:fixed;bottom:-0.6in;left:0;right:0;font-size:8.5pt;color:#5a6b7b;border-top:1px solid #d8e0e8;padding-top:6px;line-height:1.45}}
</style></head><body>
<div class="top"><div><h1>{E(p['pdf_title'])} Checklist</h1><p>Open Corporation for $35 | Updated November 2026</p></div><img src="file://{LOGO}"></div>
{page1}
<div class="brk"></div>
{page2}
<div class="book"><b>Ready to go through it with a CPA?</b> Please book a free consultation at gondaliyacpa.ca/consultation or call 647-212-9559, 9:00 AM to 8:30 PM, Monday to Sunday.</div>
</body></html>"""


def main():
    build = os.path.join(HERE, "build")
    os.makedirs(build, exist_ok=True)
    jobs = []
    only = sys.argv[1:]
    for p in POSTS:
        if only and p["dir"] not in only:
            continue
        out = os.path.join(HERE, "..", "posts", p["dir"], "images")
        os.makedirs(out, exist_ok=True)
        for i in p["info"]:
            f = os.path.join(build, f'{p["short"]}-{i["name"]}.html')
            open(f, "w").write(infographic(i))
            jobs.append({"html": f, "out": os.path.join(out, f'{p["short"]}-{i["name"]}.png'), "kind": "png"})
        f = os.path.join(build, f'why-choose-us-{p["short"]}.html')
        open(f, "w").write(why(p))
        jobs.append({"html": f, "out": os.path.join(out, f'why-choose-us-{p["short"]}.png'), "kind": "png"})
        name = "OpenCorp35-" + p["pdf_title"].replace(" ", "-").replace("/", "-") + "-Checklist.pdf"
        f = os.path.join(build, f'checklist-{p["short"]}.html')
        open(f, "w").write(checklist(p))
        jobs.append({"html": f, "out": os.path.join(out, name), "kind": "pdf"})
    json.dump(jobs, open(os.path.join(build, "jobs.json"), "w"), indent=1)
    subprocess.run(["node", os.path.join(HERE, "render.js"), os.path.join(build, "jobs.json")], check=True)


if __name__ == "__main__":
    main()
