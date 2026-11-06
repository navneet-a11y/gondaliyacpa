"""Hard-rule gate for any Family 2 batch, taken as an argument.

    python3 gate_batch.py build_f2j TOOLS10
    python3 gate_batch.py build_f2l TOOLS12     (the default)

This is gate10.py with the batch no longer hardcoded. gate10.py through
gate9.py each named one builder in an import line, so gating a new batch meant
copying the file and editing that line -- and on 2026-11-05 it came out that
nobody had: batches 11 and 12 published without any per-page hard-rule gate
being run over their rendered HTML, because "gate10.py clear" was gating batch
10's pages both times. gate_f2_all.py did not cover the gap: it only compares
pages against each other for duplicates.

Every check is the one gate10 carried. The builder asserts its contract on the
tool dicts; this asserts it again on the rendered HTML, which is the thing that
actually ships. The two are deliberately independent: a builder can pass its
own contract and still render a page with a section missing, which is exactly
the failure batches 6 and 7 had.
"""
import importlib, io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_f2 import PRICE, TOOL_DISCLAIMER

MODULE = sys.argv[1] if len(sys.argv) > 1 else 'build_f2l'
ATTR = sys.argv[2] if len(sys.argv) > 2 else 'TOOLS12'
_m = importlib.import_module(MODULE)
TOOLS = getattr(_m, ATTR)
# Batches before 10 predate the structure contract and define no STRUCTURE.
# Their hard-rule checks still apply, so the gate runs them and skips only the
# structure block rather than crashing, which is what it did on build_f2h.
STRUCTURE = getattr(_m, 'STRUCTURE', None)
STRUCTURAL = STRUCTURE is not None
if not STRUCTURAL:
    print('note: %s defines no STRUCTURE, so the section-set block is skipped'
          % MODULE)

fail = []
debt = []
for t in TOOLS:
    slug = t['slug']
    c = io.open(slug + '.html', encoding='utf-8').read()
    # Adjacent JavaScript string literals are glued before any text rule
    # runs. The result screens are built by concatenation, so a phrase can
    # sit across a join: batch 11 writes 'registered EFILE electronic ' +
    # 'filer.', which is the approved wording and which the rule 1 check read
    # as a bare EFILE. The false positive is the harmless half. A BANNED
    # phrase split the same way would have gone through unseen, and that is
    # what this guards.
    c = re.sub(r"'\s*\+\s*'", '', c)
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

    # A static reference table in the body prose. A table drawn only by the
    # module does not count: a visitor who has entered nothing should still
    # get the shape of the answer.
    #
    # gate10's comment here claimed "tools 1 to 30 all carry" one. They do
    # not: pointing this gate at build_f2b on 2026-11-06 failed five of
    # batch 2's ten pages, among them schedule-50-shareholder-threshold-checker
    # and dormant-corporation-test. The rule arrived with the structure
    # contract, so for a batch that predates it the absence is reported as
    # debt and does not fail the run. Nothing published since batch 10 is
    # excused: there STRUCTURAL is true and this is a failure.
    _body_only = re.sub(r'<script.*?</script>', '', c, flags=re.S)
    if '<table class="ei-tbl"' not in _body_only:
        if STRUCTURAL:
            bad('no static reference table in the body')
        else:
            debt.append('%s: no static reference table in the body' % slug)

    if STRUCTURAL:
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
        else:
            _n = _rel.group(1).count('<li>')
            _cmp = _rel.group(1).count('/compare/')
            if _n != STRUCTURE['related'] + _cmp:
                bad('%d Read Next links (%d of them comparisons), the contract is '
                    '%d plus any mapped comparison link'
                    % (_n, _cmp, STRUCTURE['related']))
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
for _d in debt:
    print('DEBT (pre-contract batch, not failing): %s' % _d)
print('gate clear on all %d tool pages of %s.%s'
      % (len(TOOLS), MODULE, ATTR))
for t in TOOLS:
    c = io.open(t['slug'] + '.html', encoding='utf-8').read()
    print('  %-38s %6d bytes  out:%d' % (
        t['slug'], len(c.encode()),
        len(re.findall(r'href="https://corpnilfilingfor300\.ca', c))))
