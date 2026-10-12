#!/usr/bin/env python3
"""Assemble an industry page from a source file plus the fixed chrome parts.

Usage: python3 scripts/assemble_page.py <src> <out>

Every {{TOKEN}} in the source is replaced by the contents of the matching
templates/parts/<name>.html.  Part files are stored with one trailing newline
for editor sanity; exactly one trailing newline is stripped on substitution so
the assembled page matches the published byte stream.
"""
import os
import sys

TOKENS = {
    "CSS": "css.html",
    "PARTNERS": "partners.html",
    "CREDENTIALS": "credentials.html",
    "STATBAR": "statbar.html",
    "PRICING_RIGHT": "pricing_right.html",
    "TEAM_CARDS": "team_cards.html",
    "MAPAREA": "maparea.html",
}

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS_DIR = os.path.join(REPO, "templates", "parts")


def load_part(filename):
    path = os.path.join(PARTS_DIR, filename)
    with open(path, encoding="utf-8", newline="") as fh:
        body = fh.read()
    # strip exactly one trailing newline (the file's terminator), nothing more
    if body.endswith("\n"):
        body = body[:-1]
    return body


def assemble(src):
    with open(src, encoding="utf-8", newline="") as fh:
        page = fh.read()
    for token, filename in TOKENS.items():
        marker = "{{%s}}" % token
        if marker not in page:
            continue
        page = page.replace(marker, load_part(filename))
    leftover = [t for t in TOKENS if "{{%s}}" % t in page]
    if leftover:
        sys.exit("error: unsubstituted tokens remain: %s" % ", ".join(sorted(leftover)))
    return page


def main(argv):
    if len(argv) != 3:
        sys.exit("usage: assemble_page.py <src> <out>")
    src, out = argv[1], argv[2]
    page = assemble(src)
    data = page.encode("utf-8")
    outdir = os.path.dirname(os.path.abspath(out))
    if outdir and not os.path.isdir(outdir):
        os.makedirs(outdir)
    with open(out, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes)" % (out, len(data)))


if __name__ == "__main__":
    main(sys.argv)
