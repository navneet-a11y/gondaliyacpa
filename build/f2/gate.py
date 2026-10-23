"""Hard-rule gate for the Family 2 tool pages.

Carries the same hard-rule checks as the other families, plus the two that are
specific to this one: 6(c) gates publication on a result screen that changes
with input, and requires the sentence "this tool gives general information and
is not a filed return" on it.
"""
import io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_f2 import TOOLS, PRICE, TOOL_DISCLAIMER

fail = []
for t in TOOLS:
    slug = t['slug']
    c = io.open(slug + '.html', encoding='utf-8').read()
    low = c.lower()
    def bad(m): fail.append('%s: %s' % (slug, m))

    # 1 CRA wording. "authorized signing officer" is permitted by 7.6 on and
    # about Form T183CORP, so it is removed before the test.
    low1 = low.replace('authorized signing officer', '')
    for w in ('cra authorized', 'authorized by cra', 'cra agent', 'agent of cra',
              'cra approved', 'approved by cra', 'cra partner', 'cra endorsed',
              'endorsed by cra', 'cra logo'):
        if w in low1: bad('rule 1 "%s"' % w)
    if re.search(r'\bauthorized\b', low1): bad('rule 1 stray "authorized"')
    # 2 T183CORP never bare
    if re.search(r'\bT183\b(?!CORP)', c): bad('rule 2 bare T183')
    # 3 penalty claims always qualified
    for m in re.finditer(r'(no penalty|penalty[- ]free|zero penalty)', low):
        bad('rule 3 unqualified penalty phrase "%s"' % m.group(1))
    if 'no percentage late-filing penalty' in low and \
       'stays open forever' not in low:
        bad('rule 3 qualification sentence incomplete')
    # 4 superlatives
    for w in ('cheapest', 'best price', 'fastest', 'guaranteed', 'guarantee',
              'risk-free', 'risk free', 'lowest price', 'unbeatable',
              'instant filing', 'same-day filing', 'filed in minutes'):
        if w in low: bad('rule 4 "%s"' % w)
    # 5 EFILE number / GroupID
    if re.search(r'efile\s*(number|#|no\.)', low) or 'groupid' in low:
        bad('rule 5 EFILE number or GroupID')
    # 6 forbidden schema
    for w in ('faqpage', 'howto', 'aggregaterating', '"review"'):
        if w in low: bad('rule 6 schema "%s"' % w)
    # 7 no booking
    for w in ('book a call', 'schedule a meeting', 'free consultation', 'calendly'):
        if w in low: bad('rule 7 "%s"' % w)
    # 9 price wording
    if 'including HST' in c: bad('rule 9 "including HST"')
    if PRICE not in c: bad('rule 9 price string missing')
    # 7.5 byline and stamp
    if 'CPA Ontario Membership 61040184' not in c: bad('7.5 rule 3 byline missing')
    if 'Last reviewed:' not in c: bad('7.5 last-reviewed line missing')

    # 6(c) tool gates
    if TOOL_DISCLAIMER not in c: bad('6(c) result disclaimer missing')
    if 'id="out"' not in c: bad('6(c) no result region')
    if 'aria-live' not in c: bad('result region not announced to screen readers')
    if not re.search(r'<(input|select)\b', c): bad('6(c) no input control')
    if '<script>' not in c: bad('6(c) no calculation module')
    if re.search(r'<script[^>]+\bsrc=', c): bad('module is not self-contained')
    # the module must react to input, not just render once
    if 'addEventListener' not in c: bad('6(c) result does not change with input')

    # structure
    if c.count('<h1') != 1: bad('h1 count %d' % c.count('<h1'))
    if 'nil-t2-filing-cost' not in c: bad('6(g) no link to the cost page')
    if '/guides/' not in c and '/deadlines/' not in c:
        bad('6(g) no matching guide link')
    outbound = len(re.findall(r'href="https://corpnilfilingfor300\.ca', c))
    if outbound > 20: bad('6(g) F2 outbound cap exceeded: %d' % outbound)
    nb = sorted({ch for ch in c if ord(ch) > 127})
    if nb: bad('non-ascii %r' % nb)

if fail:
    print('GATE FAILED')
    for f in fail: print(' -', f)
    raise SystemExit(1)
print('gate clear on all %d tool pages' % len(TOOLS))
for t in TOOLS:
    c = io.open(t['slug'] + '.html', encoding='utf-8').read()
    print('  %-38s %6d bytes  out:%d' % (
        t['slug'], len(c.encode()),
        len(re.findall(r'href="https://corpnilfilingfor300\.ca', c))))
