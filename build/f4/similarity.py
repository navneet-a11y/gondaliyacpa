# -*- coding: utf-8 -*-
"""6(k) similarity check across every Family 4 page on disk.

6(k) permits the twelve service slugs for one place only where each carries a
different H1, a different first 120 words and a different primary keyword, and
sets 0.60 as the ratio above which a page is rewritten rather than published.

The measurement that matters here is the CROSS-JURISDICTION one. Twelve
services within one province were always going to differ, because the service
differs. Two provinces' copies of the SAME service are the pair that can
collapse into a placename swap, which is what happened to the four Atlantic
cost pages at 0.94 to 0.96. So this reports both, and the per-service
cross-place maximum is the number to look at.
"""
import difflib, io, os, re, sys, glob


def ratio(a, b):
    """Order-independent similarity over WORD tokens.

    Two reasons this is not a character diff with the library defaults.

    1. ORDER. difflib's autojunk heuristic treats elements appearing in more
       than 1% of a long second sequence as junk, so
       SequenceMatcher(None, a, b).ratio() does NOT equal
       SequenceMatcher(None, b, a).ratio(). On a ~10,000 character page the
       same pair measured 0.64 one way round and 0.76 the other, so the figure
       depended on alphabetical accident and the lower one understated
       duplication. Both orders are measured and the higher is taken.

    2. UNITS. Word tokens, not characters. Autojunk has to be off to make the
       measurement stable, and character-level diffing with it off does not
       finish on this many pairs. Words are also the right unit for the
       question 6(k) actually asks, which is whether two pages say the same
       thing, not whether they share punctuation.
    """
    wa, wb = a.split(), b.split()
    return max(difflib.SequenceMatcher(None, wa, wb, autojunk=False).ratio(),
               difflib.SequenceMatcher(None, wb, wa, autojunk=False).ratio())


HERE = os.path.dirname(os.path.abspath(__file__))
THRESHOLD = 0.60

PLACES = ('ontario', 'british-columbia', 'alberta', 'quebec', 'manitoba',
          'saskatchewan', 'nova-scotia', 'new-brunswick',
          'newfoundland-and-labrador', 'prince-edward-island', 'yukon',
          'northwest-territories', 'nunavut')


def text(path):
    h = io.open(path, encoding='utf-8').read()
    h = re.sub(r'(?s)<style.*?</style>', ' ', h)
    h = re.sub(r'(?s)<script.*?</script>', ' ', h)
    h = re.sub(r'(?s)<!--.*?-->', ' ', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    return ' '.join(h.split())


def split(slug):
    """(service, place) for a Family 4 slug, longest place match first."""
    for p in sorted(PLACES, key=len, reverse=True):
        if slug == p or slug.endswith('-' + p):
            svc = slug[:-(len(p) + 1)] if slug != p else ''
            return svc.rstrip('-').removesuffix('-in'), p
    return None, None


pages = {}
for f in sorted(glob.glob(os.path.join(HERE, '*.html'))):
    slug = os.path.basename(f)[:-5]
    svc, place = split(slug)
    if place:
        pages[slug] = (svc, place, text(f))

def report():
    print('%d Family 4 pages on disk, %d places\n'
          % (len(pages), len({v[1] for v in pages.values()})))

    worst, rows = 0.0, []
    keys = sorted(pages)
    for i, x in enumerate(keys):
        for y in keys[i + 1:]:
            sx, px, tx = pages[x]
            sy, py, ty = pages[y]
            r = ratio(tx, ty)
            kind = ('same-service-across-place' if sx == sy else
                    'same-place-across-service' if px == py else 'unrelated')
            rows.append((r, kind, x, y))
            worst = max(worst, r)

    rows.sort(reverse=True)
    for label in ('same-service-across-place', 'same-place-across-service',
                  'unrelated'):
        sub = [r for r in rows if r[1] == label]
        if not sub:
            continue
        print('%-28s %4d pairs   max %.2f' % (label, len(sub), sub[0][0]))
        for r, _, x, y in sub[:5]:
            print('    %.2f  %s  <->  %s' % (r, x, y))
        print()

    over = [r for r in rows if r[0] >= THRESHOLD]
    print('pairs at or above the 6(k) %.2f rewrite threshold: %d' % (THRESHOLD, len(over)))
    for r, k, x, y in over[:20]:
        print('    %.2f  %-26s %s  <->  %s' % (r, k, x, y))
    print('\nworst pair overall: %.2f' % worst)
    sys.exit(1 if over else 0)


if __name__ == '__main__':
    report()
