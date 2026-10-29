"""Cross-batch gate for every built Family 2 tool page.

The per-batch gates (gate.py through gate7.py) only ever compare a page
against its own manifest, so nothing checked a new tool against the ones
published before it. At fifty tools on closely related topics that is the
likeliest place for a real defect, and the equivalent gate on Family 9
(build/f9/gate_f9_all.py) caught one on its first run.

It checks duplicate body paragraphs, duplicate section headings and duplicate
schema names across every page in this directory, and it excludes the blocks
that are shared on purpose:

  the EFILE trust strip          every page carries it, by design
  the bottom CTA                 the same on every page in the family
  the rule 3 qualification        must travel whole, so it cannot be varied
  the not-nil overflow sentence   same reason
  "Frequently Asked Questions" and "Read Next"   structural headings

Run it from build/f2 after any batch builds.
"""
import io, os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_f2 import NOT_NIL
from build_f2c import QUAL

SHARED_HEAD = {'Frequently Asked Questions', 'Read Next'}

# Defects on pages that were already live when this gate was written, from
# batches 1 to 5. They are reported on every run and do not fail it, so the
# gate is usable now and the debt stays visible. Fixing them means editing
# live pages, which is its own piece of work and needs Navneet's go-ahead
# because three of them change a section heading a visitor may have linked to.
#
# Remove an entry when its page is fixed. Nothing is added to this list for a
# page built after 2026-10-29; a new duplicate is a build to redo.
KNOWN = {
 ('paragraph', ('gifi-schedule-requirement-checker.html',
                'gifi-schedule-requirement-checker.html')),
 ('heading', ('schedule-24-first-return-checker.html',
              'schedule-50-shareholder-threshold-checker.html')),
 ('heading', ('federal-annual-return-anniversary-calculator.html',
              'gst-hst-nil-filing-checker.html')),
 ('heading', ('53-week-first-tax-year-checker.html',
              'federal-annual-return-anniversary-calculator.html',
              'nil-t2-deadline-calculator.html')),
 ('heading', ('gifi-schedule-requirement-checker.html',
              'schedule-24-first-return-checker.html')),
}


def norm(x):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', x)).strip()


SHARED_P = {norm(QUAL), norm(NOT_NIL)}


def body(path):
    c = io.open(path, encoding='utf-8').read()
    c = re.sub(r'<script.*?</script>', '', c, flags=re.S)
    c = re.sub(r'<style.*?</style>', '', c, flags=re.S)
    c = re.sub(r'<div class="ei-info">.*?</div>', '', c, flags=re.S)
    c = re.sub(r'<div class="ei-cta-bottom">.*?$', '', c, flags=re.S)
    return c


def main():
    pages = sorted(glob.glob(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '*.html')))
    paras, heads, names, fail, known = {}, {}, {}, [], []
    for p in pages:
        c = body(p)
        for m in re.findall(r'<p>(.*?)</p>', c, re.S):
            t = norm(m)
            if len(t) > 120 and t not in SHARED_P:
                paras.setdefault(t, []).append(os.path.basename(p))
        for m in re.findall(r'<h2 class="ei-h2">(.*?)</h2>', c, re.S):
            t = norm(m)
            if t not in SHARED_HEAD:
                heads.setdefault(t, []).append(os.path.basename(p))
        m = re.search(r'"name": "([^"]+)"', c)
        if m:
            names.setdefault(m.group(1), []).append(os.path.basename(p))

    for label, table in (('paragraph', paras), ('heading', heads),
                         ('schema name', names)):
        for k, v in sorted(table.items()):
            if len(v) > 1:
                msg = 'duplicate %s on %s: %s' % (label, v, k[:120])
                if (label, tuple(v)) in KNOWN:
                    known.append(msg)
                else:
                    fail.append(msg)

    for m in known:
        print('KNOWN (pre-existing, not failing):', m)
    if fail:
        print('CROSS-BATCH GATE FAILED')
        for f in fail:
            print(' -', f)
        return 1
    print('cross-batch gate clear on %d Family 2 tool pages (%d known '
          'pre-existing)' % (len(pages), len(known)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
