#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate every internal link in build/**/*.html against the live slugs.

WHY THIS EXISTS
---------------
On 2026-11-11 a link audit found two broken internal links out of 277, both
in Family 2 "Read Next" lists:

    /tools/nil-return-eligibility-checker/   (pages 1898, 1975)
    /tools/holding-corporation-nil-checker/  (page 1898)

Neither tool was ever built under that slug. The batch builders assert their
body links against the live slug list for the batch, which is why Families 5,
7 and 8 came out clean, but the Family 2 "Read Next" lists are hand-written
per page and had nothing checking them. This script is that check, for every
family at once.

Run it before any publish batch:

    python3 build/check_links.py

Exit status is 1 when anything is broken, so it can gate a build.

THE MANIFEST GOES STALE, AND THAT IS THE DANGEROUS CASE
-------------------------------------------------------
docs/seo/live-slugs.json is a snapshot. A link to a page published after the
snapshot is reported broken when it is not, and that is the failure mode to
watch: a checker that cries wolf gets ignored, and then a real break passes.
Regenerate the manifest after every publish batch.

The reverse is harmless here: a slug removed from the site but still in the
manifest shows up as a link that passes when it should not. That is why the
manifest is pulled with _fields=slug straight from the REST API rather than
assembled by hand.
"""
import io
import json
import os
import re
import sys
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = 'https://corpnilfilingfor300.ca'

# URL prefix -> manifest key. Anything at the site root goes to "root".
PREFIX = {'tools': 'tools', 'compare': 'compare', 'answers': 'answers',
          'guides': 'guides', 'deadlines': 'deadlines', 'pricing': 'pricing',
          'blog': 'blog', 'start': 'start', 'best': 'best',
          'case-studies': 'case-studies', 'reviews': 'reviews'}

# Paths that are not slugs: hubs that live as pages, and the home page.
ALWAYS_OK = {'', 'form', 'pay', 'final-details'}


def load():
    p = os.path.join(ROOT, 'docs', 'seo', 'live-slugs.json')
    d = json.load(io.open(p, encoding='utf-8'))
    return {k: set(v) for k, v in d.items() if isinstance(v, list)}


def main():
    live = load()
    bad = collections.defaultdict(list)
    files = []
    for dirpath, _dirs, names in os.walk(HERE):
        for n in names:
            if n.endswith('.html'):
                files.append(os.path.join(dirpath, n))

    targets = collections.defaultdict(set)
    for f in files:
        try:
            h = io.open(f, encoding='utf-8').read()
        except Exception:
            continue
        for u in re.findall(r'href="' + re.escape(SITE) + r'([^"]*)"', h):
            parts = [x for x in u.split('/') if x]
            rel = os.path.relpath(f, HERE)
            if not parts:
                continue                      # the home page
            if len(parts) == 1:
                group, slug = 'root', parts[0]
            else:
                group, slug = PREFIX.get(parts[0]), '/'.join(parts[1:])
                if group is None:
                    bad['unknown URL prefix'].append((rel, u))
                    continue
            if slug in ALWAYS_OK:
                continue
            targets[group].add(slug)
            known = live.get(group)
            if known is None:
                bad['no manifest entry for "%s"' % group].append((rel, u))
            elif slug not in known:
                bad[u].append((rel, u))

    print('checked %d files, %d distinct targets in %d groups\n'
          % (len(files), sum(len(v) for v in targets.values()), len(targets)))
    for g in sorted(targets):
        n = len(live.get(g, ()))
        print('  %-13s %3d linked   %3d live' % (g, len(targets[g]), n))

    if not bad:
        print('\nOK: every internal link resolves to a live slug.')
        return 0
    print('\n%d BROKEN TARGET(S):' % len(bad))
    for u in sorted(bad):
        where = sorted(set(w for w, _ in bad[u]))
        print('  %s' % u)
        for w in where:
            print('      in %s' % w)
    return 1


if __name__ == '__main__':
    sys.exit(main())
