"""Turn a vertical's copy into wp_update_page_layout ops against page 2682.

Every Family 1 page is a duplicate of post 2682, so they all share its element
addresses: wp_duplicate_post copies the Elementor layout verbatim and keeps
the ids. This maps each address to the copy field that belongs in it, read
from vertical_copy.py, so the wording on the page is the wording in the repo
rather than something retyped into a tool call.

Usage: python3 genops.py <slug> > ops-<slug>.json
"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vertical_copy import VERTICALS

SLUG = sys.argv[1]
# build_vertical.py reads sys.argv at import time, so give it the arguments it
# expects before importing it for its helpers. It rebuilds the templates as a
# side effect, which is harmless and keeps the two in step.
_SRC = os.environ.get('F1_SRC', '')
sys.argv = ['build_vertical.py', _SRC,
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')]
import build_vertical as B   # noqa: E402  (sched_table, checklist, schema, P)
v = VERTICALS[SLUG]
P = B.P

# address -> value, in page order. Addresses read from post 2682 on
# 2026-11-19 with wp_get_page_layout at depth 12.
TEXT = [
    ('8cb25e',   v['h1']),
    ('45fe07a6', P(v['lede'])),
    ('1e51fde8', v['intro_h']),
    ('17bc390',  P(*v['intro'])),
    ('10225ef5', v['notnil_h']),
    ('2836f299', P(*v['notnil_text'])),
    ('1c749de9', v['sched_h']),
    ('75a774c2', B.sched_table(v)),
    ('69aa86fa', v['why_h']),
    ('11fba7',   v['svc_h']),
    ('36a660c6', B.checklist(v)),
    ('66b11765', v['proc_h']),
    ('7de6f7ca', P(v['proc_lede'])),
    ('15f2167e', P(v['proc_note'])),
    ('2aaff735', P(v['price_eyebrow'])),
    ('230aed9d', v['price_h']),
    ('5bc10a46', P(v['price_text'])),
    ('15f093c3', v['geo_h']),
    ('2d5e7fee', B.geo_html(v)),
    ('711bd395', f'Nil T2 Filing FAQs for {v["name"]}'),
    ('1198c500', v['cta_h']),
    ('52550d10', B.schema(v, SLUG)),
]

# icon-box pairs: (address, (title, description))
BOXES = list(zip(['19265652', '727eca2a', '51b70842', '3bd76c49'], v['notnil_boxes'])) \
      + list(zip(['d21e697', '64303c30', '7ff9b17f'], v['sched_boxes']))

# heading + text pairs
PAIRS = list(zip([('2dc281ff', '6b3052a8'), ('57ec36d5', '1b437231'),
                  ('17d9a5bf', '26b2bafb'), ('6b3009d8', '31be0a80')], v['why'])) \
      + list(zip([('33258475', '617c455f'), ('240c1cb5', '1978eaae'),
                  ('6c886c12', '4feb96fe')], v['strip'])) \
      + list(zip([('1f931000', '8162fe9'), ('6de3c56e', '37197e0e'),
                  ('6c049aee', '56f88844'), ('28604837', '50b97e6f')], v['steps']))

FAQ_ITEMS = ['752e107', 'd34a67d', 'a10a834', '000788c', 'a618478',
             'ab306f2', '93bca0e', '85cea24', '69f7093', 'cfc9d1a']
FAQ_BODIES = ['61a4928', '1a2fa224', '580635c0', '2aa8fc34', '16b6ffbc',
              '362a7752', '59baad1b', '6a6bd6c', '86f7bf', '3fdda18a']

# The two html widgets have no default text field, so the op has to name it.
HTML_ADDRS = {'36a660c6', '52550d10'}

ops = []
for addr, val in TEXT:
    if addr in HTML_ADDRS:
        # An html widget's field holds code, which set_text refuses to write.
        ops.append({'op': 'set_fields', 'element': addr, 'expect': 'html',
                    'fields': {'html': val}})
    else:
        ops.append({'op': 'set_text', 'element': addr, 'value': val})
for addr, (t, d) in BOXES:
    ops.append({'op': 'set_fields', 'element': addr, 'expect': 'icon-box',
                'fields': {'title_text': t, 'description_text': d}})
for (ha, ta), (t, d) in PAIRS:
    ops.append({'op': 'set_text', 'element': ha, 'expect': 'heading', 'value': t})
    ops.append({'op': 'set_text', 'element': ta, 'expect': 'text-editor', 'value': P(d)})
for item, (q, _) in zip(FAQ_ITEMS, v['faq']):
    ops.append({'op': 'set_fields', 'element': '6ff36baa', 'list': 'items',
                'item': item, 'fields': {'item_title': q}})
for i, (addr, (_, a)) in enumerate(zip(FAQ_BODIES, v['faq'])):
    # build_vertical puts the accordion's stylesheet inside the first answer,
    # so an ops run that writes plain answers everywhere strips the FAQ
    # styling off the page. The first answer carries it here too.
    body = (B.FAQ_CSS + P(a)) if i == 0 else P(a)
    ops.append({'op': 'set_text', 'element': addr, 'expect': 'text-editor',
                'value': body})

half = (len(ops) + 1) // 2
print(json.dumps({'total': len(ops),
                  'call1': ops[:half], 'call2': ops[half:]},
                 ensure_ascii=False, separators=(',', ':')))
