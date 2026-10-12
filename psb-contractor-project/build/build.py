"""Convert the PSB package drafts (Markdown) into WordPress-ready HTML.

Copy, figures, links and JSON-LD are taken verbatim from the package; this
script only changes the markup. Run: python3 -I build.py <package_dir> <out_dir>
"""
import html
import json
import os
import re
import sys

TRUSTINDEX = "<script defer async src='https://cdn.trustindex.io/loader.js?3d7613063935419a40268ae9f69'></script>"

# Table CSS from SEO strategy 5.7, plus byline/review styling scoped to .psb-cluster.
CSS = (
    "<style>"
    ".psb-cluster table{border-collapse:collapse;width:100%;margin:16px 0}"
    ".psb-cluster th,.psb-cluster td{border:1px solid #c9d3df;padding:8px 10px;text-align:left;vertical-align:top}"
    ".psb-cluster th{background:#f3f6fa;font-weight:600}"
    "@media (max-width:767px){.psb-cluster table{display:block;overflow-x:auto}}"
    ".psb-cluster .psb-byline{font-size:14px;color:#52606d;margin:0 0 16px}"
    ".psb-cluster .psb-review{font-size:14px;color:#52606d;border-top:1px solid #c9d3df;margin-top:24px;padding-top:12px}"
    ".psb-cluster .psb-reviews{margin:24px 0}"
    "</style>"
)


def inline(text):
    out = html.escape(text, quote=False)
    out = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", out)
    return out


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def render(lines, calculator_html):
    out, i = [], 0
    while i < len(lines):
        line = lines[i].rstrip()
        s = line.strip()
        if not s:
            i += 1
            continue
        if s == "[TRUSTINDEX WIDGET]":
            out.append(f'<div class="psb-reviews">{TRUSTINDEX}</div>')
        elif s == "[CALCULATOR WIDGET]":
            out.append(calculator_html)
        elif m := re.match(r"^#{2,4}\s*H2:\s*(.+)$", s):
            out.append(f"<h2>{inline(m.group(1))}</h2>")
        elif m := re.match(r"^#{2,5}\s*H3:\s*(.+)$", s):
            out.append(f"<h3>{inline(m.group(1))}</h3>")
        elif m := re.match(r"^#{2,5}\s*H4:\s*(.+)$", s):
            out.append(f"<h4>{inline(m.group(1))}</h4>")
        elif s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            head, body = rows[0], [r for r in rows[2:]]
            t = ["<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"]
            for r in body:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue
        elif re.match(r"^[-*]\s+", s):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i].rstrip()))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        elif re.match(r"^\d+\.\s+", s):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i].rstrip()))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>")
            continue
        elif s.startswith("#"):
            raise ValueError(f"Unhandled heading: {s}")
        else:
            para = [s]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||[-*]\s|\d+\.\s|\[)", lines[i].strip()):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline(' '.join(para))}</p>")
            continue
        i += 1
    return out


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else None


def brief_field(text, *names):
    for n in names:
        m = re.search(rf"^\| {re.escape(n)} \| (.*?) \|\s*$", text, re.M)
        if m:
            return re.sub(r"\s*\(\d+ characters\)\s*$", "", m.group(1)).strip()
    return None


def build(path, calculator_html):
    text = open(path, encoding="utf-8").read()
    copy = section(text, "Page copy") or section(text, "Post copy")
    faqs = section(text, "FAQs")
    ld_raw = re.search(r"^## JSON-LD\s*$.*?```json\n(.*?)```", text, re.S | re.M).group(1)
    ld = json.loads(ld_raw)

    info = {
        "file": os.path.basename(path),
        "slug": brief_field(text, "Slug").strip("/"),
        "seo_title": brief_field(text, "SEO title", "Final SEO title"),
        "meta_description": brief_field(text, "Meta description"),
        "primary_keyword": brief_field(text, "Primary keyword"),
        "featured_image_headline": brief_field(text, "Featured image headline"),
        "author_line": brief_field(text, "Author and review line"),
    }
    lines = copy.strip("\n").split("\n")
    h1_line = next(l for l in lines if l.startswith("H1:"))
    info["h1"] = h1_line[3:].strip()
    lines = lines[lines.index(h1_line) + 1:]

    written = re.match(r"(Written by .*?\.)\s+(Reviewed by .*?)\s+(Last updated: .*\.)$", info["author_line"])
    written_by, reviewed_by, updated = written.groups()

    body = render(lines, calculator_html)
    # The 40-60 word direct answer stays the first paragraph; the credentials line sits under the H1.
    parts = [CSS, '<div class="psb-cluster">', f"<h1>{inline(info['h1'])}</h1>",
             f'<div class="psb-byline">{inline(written_by)} {inline(updated)}</div>']
    parts += body

    faq_pairs = re.findall(r"^#### Q:\s*(.+?)\s*\n(.*?)(?=^#### Q:|\Z)", faqs, re.S | re.M)
    parts.append("<h2>Frequently asked questions</h2>")
    for q, a in faq_pairs:
        parts.append(f"<h3>{inline(q)}</h3>")
        parts += render(a.strip("\n").split("\n"), calculator_html)
    parts.append(f'<div class="psb-review">{inline(reviewed_by)} {inline(updated)}</div>')
    parts.append("</div>")
    parts.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False, separators=(",", ":")) + "</script>")
    info["faq_pairs"] = [(q.strip(), a.strip()) for q, a in faq_pairs]
    info["jsonld"] = ld
    return "\n".join(parts) + "\n", info


def main():
    pkg, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    calc = open(os.path.join(pkg, "05-Calculator", "psb-tax-cost-calculator.html"), encoding="utf-8").read()
    calc = "\n".join(l for l in calc.split("\n") if l.strip())  # no blank lines inside the widget
    manifest = []
    for sub in ("03-Pages", "04-Posts"):
        for f in sorted(os.listdir(os.path.join(pkg, sub))):
            content, info = build(os.path.join(pkg, sub, f), calc)
            name = f.replace(".md", ".html")
            open(os.path.join(out, name), "w", encoding="utf-8").write(content)
            info["html_file"] = name
            info.pop("jsonld")
            manifest.append(info)
    json.dump(manifest, open(os.path.join(out, "manifest.json"), "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
