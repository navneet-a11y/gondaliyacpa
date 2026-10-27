#!/usr/bin/env python3
"""Validate docs/seo/rank-math-meta.json against the CLAUDE.md hard rules.

Read-only: it never writes the ledger. Run it from the repo root after any
edit to the ledger, and before committing one:

    python3 -I build/f2/gate_rank_math.py

Exits non-zero and prints every violation. The rules enforced are the ones
that can be checked from the meta text alone -- rules 1, 2, 3, 4, 9 and the
no-emoji rule -- plus Rank Math's own length limits and a uniqueness check,
since duplicate titles or descriptions across 145 URLs are an SEO defect in
their own right.
"""
import json
import re
import sys

LEDGER = 'docs/seo/rank-math-meta.json'

# Rule 1: the only permitted CRA wording is "registered EFILE electronic filer".
BAD_CRA = [r'\bCRA[- ]authori[sz]ed\b', r'\bauthori[sz]ed by (the )?CRA\b',
           r'\bCRA agent\b', r'\bCRA[- ]approved\b', r'\bCRA partner\b',
           r'\bCRA[- ]endorsed\b', r'\bauthori[sz]ed e?-?filer\b']
EFILE_OK = 'registered EFILE electronic filer'
# Rule 2: always T183CORP, never a bare T183.
T183 = re.compile(r'T183(?!CORP)')
# Rule 3: a penalty claim never stands alone, and meta is too short to carry
# the Section 7.4 qualification block, so it may not appear in meta at all.
NO_PENALTY = [r'\bno penalt', r'\bpenalty[- ]free\b', r'\bzero penalt',
              r'\bpenalty free\b']
# Rule 4: no superlatives.
SUPERLATIVE = [r'\bcheapest\b', r'\bbest\b', r'\bfastest\b', r'\bguaranteed\b',
               r'\brisk[- ]free\b']
# Rule 9: a price figure only ever appears in this exact form.
PRICE_OK = '$300.00 plus HST per tax year'
PRICE_FIGURE = re.compile(r'\$\s?300(\.00)?')
EMOJI = re.compile('[\U0001F000-\U0001FAFF☀-➿️]')

LIMITS = (('title', 60, 20), ('desc', 160, 70))


def main():
    led = json.load(open(LEDGER))
    err = []
    seen = {}
    total = 0

    for section in sorted(led):
        body = led[section]
        if not (isinstance(body, dict) and 'items' in body):
            continue
        for item in body['items']:
            total += 1
            for field, cap, floor in LIMITS:
                text = item[field]
                tag = '%s:%s %s' % (section, item['id'], field)
                if len(text) > cap:
                    err.append('%s: %d chars, max %d' % (tag, len(text), cap))
                if len(text) < floor:
                    err.append('%s: only %d chars' % (tag, len(text)))
                for pat in BAD_CRA + NO_PENALTY + SUPERLATIVE:
                    if re.search(pat, text, re.I):
                        err.append('%s: matches %r -> %r' % (tag, pat, text))
                if T183.search(text):
                    err.append('%s: bare T183 -> %r' % (tag, text))
                if EMOJI.search(text):
                    err.append('%s: emoji' % tag)
                if re.search(r'\bEFILE\b', text) and EFILE_OK not in text:
                    err.append('%s: EFILE outside the approved phrase -> %r'
                               % (tag, text))
                for m in PRICE_FIGURE.finditer(text):
                    if text[m.start():m.start() + len(PRICE_OK)] != PRICE_OK:
                        err.append('%s: price not in the full form -> %r'
                                   % (tag, text[m.start():m.start() + 45]))
                if re.search(r'plus hst', text) and 'plus HST' not in text:
                    err.append('%s: lowercase hst' % tag)
                if 'including HST' in text:
                    err.append('%s: "including HST"; the wording in force is '
                               '"plus HST"' % tag)
            keyword = item['kw']
            if keyword != keyword.lower().strip():
                err.append('%s:%s focus keyword not lowercase and trimmed -> %r'
                           % (section, item['id'], keyword))
            where = '%s:%s' % (section, item['id'])
            seen.setdefault(('desc', item['desc']), []).append(where)
            seen.setdefault(('title', item['title']), []).append(where)

    for (kind, _), where in seen.items():
        if len(where) > 1:
            err.append('duplicate %s across %s' % (kind, where))

    if err:
        print('FAIL (%d)' % len(err))
        for e in err:
            print(' -', e)
        return 1
    print('PASS - %d items, hard rules clean, titles and descriptions unique'
          % total)
    return 0


if __name__ == '__main__':
    sys.exit(main())
