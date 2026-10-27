#!/usr/bin/env python3
"""Check that a built post keeps every word and heading of its draft.

Usage: check_no_words_removed.py SOURCE.md HEADINGS.txt POST.html [CORRECTIONS.json]

1. Every word of SOURCE.md appears in POST.html, in the same order
   (visible text plus image alt text). Words may be added, never removed.
   Only markdown syntax is ignored: "---" rules, "[^n]:" footnote labels,
   straight double quotes, and the image-brief labels "Alt text suggestion:"
   and "Caption:" (their text becomes the image alt and caption).
2. Every line in HEADINGS.txt is the exact text of an h1 to h5 element.
3. The FAQPage schema matches the visible FAQ word for word.

CORRECTIONS.json lists approved fact fixes as {"from", "to"} pairs. Each
"from" must occur exactly once in SOURCE.md; it is replaced by "to" before
the word check, so only those sentences may differ from the draft.
"""
import html
import json
import re
import sys
from html.parser import HTMLParser

SKIP = {"style", "script"}
HEADINGS = {"h1", "h2", "h3", "h4", "h5"}


class Extract(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text, self.headings, self.scripts = [], [], []
        self.skip = None
        self.head = None
        self.buf = []

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip = tag
            self.buf = []
        if tag in HEADINGS:
            self.head = []
        if tag == "img":
            alt = dict(attrs).get("alt")
            if alt:
                self.text.append(" " + alt + " ")
        if tag in ("p", "li", "td", "th", "div", "br", "summary", "figcaption", "span") + tuple(HEADINGS):
            self.text.append(" ")

    def handle_endtag(self, tag):
        if tag == self.skip:
            if tag == "script":
                self.scripts.append("".join(self.buf))
            self.skip = None
        if tag in HEADINGS and self.head is not None:
            self.headings.append(" ".join("".join(self.head).split()))
            self.head = None
        if tag in ("p", "li", "td", "th", "div", "summary", "figcaption", "span") + tuple(HEADINGS):
            self.text.append(" ")

    def handle_data(self, data):
        if self.skip:
            self.buf.append(data)
            return
        self.text.append(data)
        if self.head is not None:
            self.head.append(data)


def tokens(text):
    out = []
    for t in text.split():
        t = t.replace('"', "")
        if not t or re.fullmatch(r"-+", t) or re.fullmatch(r"\[\^\d+\]:", t):
            continue
        out.append(t)
    return out


def source_tokens(path, corrections=None):
    text = open(path, encoding="utf-8").read()
    for c in json.load(open(corrections, encoding="utf-8")) if corrections else []:
        if text.count(c["from"]) != 1:
            sys.exit(f"FAIL correction does not match the draft exactly once: {c['from'][:60]}")
        text = text.replace(c["from"], c["to"])
    lines = []
    for line in text.splitlines(keepends=True):
        line = re.sub(r"^(Alt text suggestion:|Caption:)\s*", "", line)
        lines.append(line)
    return tokens("".join(lines))


def main(src, heads, post, corrections=None):
    page = Extract()
    page.feed(open(post, encoding="utf-8").read())
    have = tokens("".join(page.text))
    want = source_tokens(src, corrections)
    fails = 0

    i = 0
    for n, w in enumerate(want):
        while i < len(have) and have[i] != w:
            i += 1
        if i == len(have):
            ctx = " ".join(want[max(0, n - 8):n + 8])
            print(f"FAIL word {n + 1} of {len(want)} missing or out of order: {w!r}\n     near: {ctx}")
            fails += 1
            break
        i += 1
    else:
        print(f"PASS all {len(want)} draft words present, in order ({len(have)} words on the page)")

    expected = [l.strip() for l in open(heads, encoding="utf-8") if l.strip()]
    missing = [h for h in expected if h not in page.headings]
    if missing:
        fails += 1
        for h in missing:
            print(f"FAIL heading missing: {h}")
    else:
        print(f"PASS all {len(expected)} draft headings present as headings")

    faq_html = re.search(r'<div class="gcpa-faq" id="faq-main">(.*?)</div>\s*(?=<div class="gcpa-callout|<h2)',
                         open(post, encoding="utf-8").read(), re.S)
    pairs = re.findall(r"<summary>(.*?)<span class=\"pl\">.*?<div class=\"ans\"><p>(.*?)</p>", faq_html.group(1), re.S)
    visible = [(html.unescape(q).strip(), html.unescape(a).strip()) for q, a in pairs]
    schema = []
    for s in page.scripts:
        try:
            data = json.loads(s)
        except ValueError:
            continue
        for node in data.get("@graph", [data]):
            if node.get("@type") == "FAQPage":
                schema = [(q["name"], q["acceptedAnswer"]["text"]) for q in node["mainEntity"]]
    if visible and visible == schema:
        print(f"PASS FAQ schema matches the {len(visible)} visible FAQ answers")
    else:
        fails += 1
        print(f"FAIL FAQ schema ({len(schema)}) does not match visible FAQ ({len(visible)})")
        for v, s in zip(visible, schema):
            if v != s:
                print(f"     visible: {v}\n     schema:  {s}")

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:5]))
