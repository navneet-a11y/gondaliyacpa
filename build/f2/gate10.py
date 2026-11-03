"""Hard-rule gate for the Family 2 tool pages, batch 10 (tools 71 to 80).

Carries every check gate9 carries, plus the structure block Navneet asked for
on 2026-11-03: "make sure they have all sections tables". build_f2j.py asserts
the section set on the tool dicts; this gate asserts it again on the rendered
HTML, which is the thing that actually ships. The two are deliberately
independent: the builder could pass its own contract and still render a page
with a section missing, and that is exactly the failure batches 6 and 7 had.
"""
import io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_f2 import PRICE, TOOL_DISCLAIMER
from build_f2j import TOOLS10 as TOOLS, STRUCTURE

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
    # Hard rule 1 reserves EFILE for "registered EFILE electronic filer". No
    # F2 gate checked it, so batch 10 built a tool called "EFILE Rejection
    # Reason Checker" and only gate_rank_math.py refused it, after the page
    # was already published. The word is a Canada Revenue Agency mark and a
    # product name is exactly the use the rule forbids.
    for _m in re.finditer(r'EFILE', c):
        if not c.startswith('EFILE electronic filer', _m.start()):
            bad('rule 1 EFILE outside the approved phrase: %r'
                % c[max(0, _m.start() - 30):_m.start() + 30])
            break
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

    # A static reference table in the body prose, which tools 1 to 30 all
    # carry and batches 6 and 7 originally shipped without. A table drawn
    # only by the module does not count: a visitor who has entered nothing
    # should still get the shape of the answer.
    _body_only = re.sub(r'<script.*?</script>', '', c, flags=re.S)
    if '<table class="ei-tbl"' not in _body_only:
        bad('no static reference table in the body')

    # ---------------- the section set, checked on the rendered page --------
    _body = _body_only
    _h2 = re.findall(r'<h2 class="ei-h2">(.*?)</h2>', _body, re.S)
    if len(_h2) != STRUCTURE['sections'] + 2:
        bad('%d H2 sections, the contract is %d prose plus FAQ plus Read Next'
            % (len(_h2), STRUCTURE['sections']))
    if _h2[-2:] != ['Frequently Asked Questions', 'Read Next']:
        bad('the last two sections are not the FAQ and Read Next: %r'
            % (_h2[-2:],))
    if len(set(_h2)) != len(_h2): bad('two sections share a heading')
    _ids = re.findall(r'<div class="ei-section(?:-alt)?" id="([\w-]+)">', c)
    if len(_ids) != STRUCTURE['sections']:
        bad('%d anchored prose sections, the contract is %d'
            % (len(_ids), STRUCTURE['sections']))
    if c.count('<details>') != STRUCTURE['faq']:
        bad('%d FAQ items, the contract is %d'
            % (c.count('<details>'), STRUCTURE['faq']))
    _rel = re.search(r'<ul class="ei-qlist">(.*?)</ul>', _body, re.S)
    if not _rel:
        bad('no Read Next list')
    elif _rel.group(1).count('<li>') != STRUCTURE['related']:
        bad('%d Read Next links, the contract is %d'
            % (_rel.group(1).count('<li>'), STRUCTURE['related']))
    if c.count('<span class="ei-hero-tag">') != STRUCTURE['tags']:
        bad('%d hero tags, the contract is %d'
            % (c.count('<span class="ei-hero-tag">'), STRUCTURE['tags']))
    if _body.count('<table class="ei-tbl"') < STRUCTURE['body_tables']:
        bad('no static reference table in the body')
    _script = c[c.rindex('<script>'):] if '<script>' in c else ''
    if _script.count('<table class="ei-tbl"') < STRUCTURE['result_tables']:
        bad('the result draws no table')
    for _marker, _what in (
            ('ei-hero-eyebrow', 'hero eyebrow'),
            ('ei-hero-by', 'hero byline'),
            ('ei-hero-btns', 'hero call to action'),
            ('ei-updated', 'review stamp'),
            ('ei-tool', 'tool panel'),
            ('ei-info', 'EFILE strip'),
            ('ei-faq', 'FAQ block'),
            ('ei-cta-bottom', 'closing call to action')):
        if _marker not in c: bad('no %s' % _what)
    if '"@type": "BreadcrumbList"' not in c: bad('no breadcrumb schema')
    if '"@type": "WebPage"' not in c: bad('no WebPage schema')

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
