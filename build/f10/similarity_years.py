# -*- coding: utf-8 -*-
"""6(k) similarity for the Family 10 year series.

Same measurement as build/f4/similarity.py: word tokens, autojunk off, both
orders, higher taken. Threshold 0.60. Measured against each other AND against
the fourteen Family 10 pages already live, because a new page that duplicates
an existing one is the same fault as two new pages duplicating each other.
"""
import difflib, glob, io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
THRESHOLD = 0.60


def ratio(a, b):
    wa, wb = a.split(), b.split()
    return max(difflib.SequenceMatcher(None, wa, wb, autojunk=False).ratio(),
               difflib.SequenceMatcher(None, wb, wa, autojunk=False).ratio())


def text(path):
    h = io.open(path, encoding='utf-8').read()
    h = re.sub(r'(?s)<style.*?</style>', ' ', h)
    h = re.sub(r'(?s)<script.*?</script>', ' ', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    return ' '.join(h.split())


pages = {os.path.basename(f)[:-5]: text(f)
         for f in sorted(glob.glob(os.path.join(HERE, '*.html')))}
new = sorted(k for k in pages if k.startswith('first-t2-after-incorporating-in-'))
old = sorted(k for k in pages if k not in new)
assert len(new) == 12, len(new)

rows = []
for i, x in enumerate(new):
    for y in new[i + 1:]:
        rows.append((ratio(pages[x], pages[y]), 'new<->new', x, y))
    for y in old:
        rows.append((ratio(pages[x], pages[y]), 'new<->live', x, y))
rows.sort(reverse=True)

over = [r for r in rows if r[0] >= THRESHOLD]
print('%d pairs involving a year page (%d new, %d already live)'
      % (len(rows), len(new), len(old)))
print('worst pair          : %.2f' % rows[0][0])
print('worst new<->new     : %.2f' % max(r[0] for r in rows if r[1] == 'new<->new'))
print('worst new<->live    : %.2f' % max(r[0] for r in rows if r[1] == 'new<->live'))
print('at or above %.2f    : %d' % (THRESHOLD, len(over)))
print('\ntop 10 pairs:')
for r, k, x, y in rows[:10]:
    print('  %.2f  %-11s %s  <->  %s' % (r, k, x.replace('first-t2-after-incorporating-in-', '>'), y.replace('first-t2-after-incorporating-in-', '>')))
print('\nFIRST ATTEMPT, 2026-11-11: worst pair 0.99, 15 of 45 pairs >= 0.90.')
sys.exit(1 if over else 0)
