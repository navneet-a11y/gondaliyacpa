#!/usr/bin/env python3
"""Emit the FAQPage JSON-LD block for an industry page, from the page's own FAQ copy.

Usage: python3 scripts/build_faq_schema.py <page.html>

The block goes to stdout; the entity count goes to stderr.
"""
import html
import json
import re
import sys

ITEM_RE = re.compile(
    r'<div class="sb-faq-item">\s*'
    r'<div class="sb-faq-q">(.*?)</div>\s*'
    r'<div class="sb-faq-a">(.*?)</div>\s*'
    r'</div>',
    re.S,
)
TAG_RE = re.compile(r"<[^>]+>")


def clean(fragment):
    """FAQ copy -> plain text for JSON-LD: drop inline tags, decode entities."""
    text = TAG_RE.sub("", fragment)
    text = html.unescape(text)
    return " ".join(text.split())


def faq_items(page):
    return [(clean(q), clean(a)) for q, a in ITEM_RE.findall(page)]


def build(page):
    items = faq_items(page)
    if not items:
        sys.exit("error: no sb-faq-item blocks found")
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in items
        ],
    }
    payload = json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
    block = '<script type="application/ld+json">%s</script>' % payload
    return block, len(items)


def main(argv):
    if len(argv) != 2:
        sys.exit("usage: build_faq_schema.py <page.html>")
    with open(argv[1], encoding="utf-8", newline="") as fh:
        page = fh.read()
    block, count = build(page)
    sys.stderr.write("<!-- %d FAQ entities -->\n" % count)
    sys.stdout.write(block + "\n")


if __name__ == "__main__":
    main(sys.argv)
