"""Family 1 industry-and-entity vertical template generator.

Usage:
    python3 build_vertical.py <industry-pages-template.json> <outdir> [slug ...]

Source is the gondaliyacpa.ca "industry pages template" export Navneet
supplied on 2026-11-19: 39 sections built for an OnlyFans-creator service
page. 24 of those sections carry over; the rest cannot go on this site at all
and are dropped rather than rewritten.

Dropped, with the rule that drops them:
  [2][3]   "Official Partner" strip and a scrolling logo rail  - hard rule 1
  [9][12]  "1450+ 5-star Google reviews", "30-Day Money-Back Guarantee",
           "60-Day Fees-Matching Policy"                       - hard rules 4, 6
  [18]     HubSpot lead-magnet form for a downloadable PDF     - tool not in the
           stack, and nine stray PDFs are already indexed
  [19][20][21][22]  Case studies with client figures           - Family 12, and
           needs client consent
  [27][28] "Meet your accountants" cards, cross-domain photos
  [29][30] Google Reviews heading and the Trustindex shortcode - hard rule 6
  [33][34] Location-switcher JavaScript for the other site

Every surviving section is rewritten end to end. Nothing from the source
copy ships.
"""
import json, copy, random, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vertical_copy import VERTICALS

SRC, OUTDIR = sys.argv[1], sys.argv[2]
WANT = sys.argv[3:] or None
src = json.load(open(SRC))
if isinstance(src, dict):
    src = src['content']
os.makedirs(OUTDIR, exist_ok=True)

SITE  = 'https://corpnilfilingfor300.ca'
FORM  = f'{SITE}/form/'
PRICE = f'{SITE}/pricing/nil-t2-filing-cost/'
CTA   = 'Start Nil T2 Filing NOW'

# Hero photograph already on this site. The source hero is a gondaliyacpa.ca
# asset and desource() blanks it, which would leave the banner flat.
HERO_IMG = (f'{SITE}/wp-content/uploads/2026/09/'
            'business-executives-having-meeting_1098-18316.jpg')
# Matched to the service page /nil-t2-filing/ (post 434). The source banner
# carried a #000000 overlay at 0.03, which is no overlay at all.
HERO = {
    'background_position':        'center center',
    'background_overlay_color':   '#0B1A33',
    'background_overlay_opacity': {'unit': 'px', 'size': 0.82, 'sizes': []},
    'custom_height':              {'unit': 'px', 'size': 360, 'sizes': []},
}

# Twelve cards in source section 16. Every target verified live in Search
# Console's page report on 2026-11-19, so none of these is a guess.
SERVICES = [
 ('/nil-t2-filing/',                               'Nil T2 Filing',
  'The service itself: one T2 for one corporation for one tax year.'),
 ('/guides/inactive-holding-company-filing/',      'Inactive Holding Company Filing',
  'The full guide to filing for a holding corporation that did nothing.'),
 ('/guides/dormant-and-inactive-corporations/',    'Dormant and Inactive Corporations',
  'What dormant means to the Canada Revenue Agency and what still falls due.'),
 ('/guides/gifi-schedules-100-125-141/',           'GIFI Schedules 100, 125 and 141',
  'When the GIFI trio is required and the narrow case for omitting it.'),
 ('/guides/schedule-50-and-shareholder-reporting/', 'Schedule 50 and Shareholders',
  'The 10% rule, what each row records, and why a nil return still files it.'),
 ('/guides/catch-up-unfiled-corporate-tax-returns/', 'Catching Up Unfiled Returns',
  'The order to file several outstanding years in, and why order matters.'),
 ('/guides/final-t2-and-dissolution/',             'Final T2 and Dissolution',
  'Winding the corporation up and the return due within six months.'),
 ('/compare/t2-short-vs-full-t2/',                 'T2 Short or Full T2',
  'The eight conditions, and which form a nil year actually qualifies for.'),
 ('/guides/t2-filing-deadlines/',                  'T2 Filing Deadlines',
  'Six months after the fiscal year-end, and how the date moves.'),
 ('/pricing/nil-t2-filing-cost/',                  'Nil T2 Filing Cost',
  'What $300.00 plus HST per tax year covers, line by line.'),
 ('/tools/nil-return-vs-full-return-checker/',     'Nil or Full Return Checker',
  'Answer five questions and find out which return the year needs.'),
 ('/tools/shareholder-loan-balance-checker/',      'Shareholder Loan Checker',
  'What a loan sitting on the books does to a return that looks nil.'),
]

# Jurisdiction and city links for the geography section. All live.
GEO = [('Ontario', '/nil-t2-filing-ontario/'),
       ('British Columbia', '/nil-t2-filing-british-columbia/'),
       ('Alberta', '/nil-t2-filing-alberta/'),
       ('Quebec', '/nil-t2-filing-quebec/'),
       ('Saskatchewan', '/nil-t2-filing-saskatchewan/')]
CITIES = [('Toronto', '/toronto/'), ('Mississauga', '/mississauga/'),
          ('Brampton', '/brampton/'), ('Ottawa', '/ottawa/')]

TRUST_BOX = ('CPA Ontario Registered Firm', 'Firm Registration 61330051')


def widgets(sec):
    out = []
    def w(n):
        if isinstance(n, dict):
            if n.get('elType') == 'widget':
                out.append(n)
            if 'elements' in n:
                w(n['elements'])
        elif isinstance(n, list):
            for v in n:
                w(v)
    w(sec)
    return out


def reid(n):
    if isinstance(n, dict):
        if isinstance(n.get('id'), str):
            n['id'] = '%08x' % random.randrange(16 ** 8)
        for v in n.values():
            reid(v)
    elif isinstance(n, list):
        for v in n:
            reid(v)


def setlink(w, url):
    s = w['settings']
    hit = False
    for k in ('link', 'button_link', 'ekit_icon_box_global_link',
              'ekit_icon_box_btn_url'):
        if isinstance(s.get(k), dict):
            s[k] = dict(s[k])
            s[k]['url'] = url
            s[k]['is_external'] = ''
            s[k]['nofollow'] = ''
            hit = True
    if not hit and w.get('widgetType') == 'button':
        s['link'] = {'url': url, 'is_external': '', 'nofollow': '',
                     'custom_attributes': ''}


def desource(n, hero=[False]):
    """Strip every gondaliyacpa.ca asset and link target."""
    if isinstance(n, dict):
        st = n.get('settings')
        if isinstance(st, dict):
            for k, v in list(st.items()):
                if isinstance(v, dict) and isinstance(v.get('url'), str) \
                        and 'gondaliyacpa.ca' in v['url']:
                    if k == 'background_image' and not hero[0]:
                        v['url'] = HERO_IMG
                        v.pop('id', None)
                        hero[0] = True
                    else:
                        v['url'] = ''
                        v.pop('id', None)
                # Alt text survives a blanked image and still named the other
                # firm and its principal. Not visible text, but it ships.
                if isinstance(v, dict) and isinstance(v.get('alt'), str):
                    if not v.get('url') or 'Gondaliya' in v['alt']:
                        v['alt'] = ''
            if st.get('shadow_text_content'):
                st['shadow_text_content'] = ''
        for v in (n.get('elements') or []):
            desource(v)
    elif isinstance(n, list):
        for v in n:
            desource(v)


def P(*ps):
    return ''.join('<p>%s</p>' % p for p in ps)


# Source section 17 looked like a CSS-only widget in the outline. It is not:
# it is a 22,883-byte html widget holding a second services grid written for
# the source page, with 73 mentions of its industry. The whole value is
# replaced. The grid keeps the three-column card shape, which is the one
# genuinely reusable thing in it, under this site's own class prefix.
CHECK_CSS = (
 '<style>'
 '.cnf-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;'
 'max-width:1140px;margin:0 auto;padding:4px 20px 0}'
 '.cnf-card{background:#fff;border:1px solid #e2e8f0;border-radius:12px;'
 'padding:26px 22px}'
 '.cnf-card h3{font-family:Poppins,sans-serif;font-size:18px;font-weight:700;'
 'color:#0B1A33;margin:0 0 14px}'
 '.cnf-card ul{list-style:none;padding:0;margin:0}'
 '.cnf-card li{position:relative;padding-left:18px;margin:0 0 11px;'
 'font-family:Lato,sans-serif;font-size:15px;line-height:1.6;color:#39414d}'
 '.cnf-card li:last-child{margin:0}'
 '.cnf-card li:before{content:"";position:absolute;left:0;top:9px;width:7px;'
 'height:7px;border-radius:50%;background:#314D8A}'
 '.cnf-card.cnf-no li:before{background:#c05621}'
 '@media(max-width:900px){.cnf-grid{grid-template-columns:1fr}}'
 '</style>'
)


def checklist(v):
    """The plan's other unique-data option at line 1209: an original checklist.

    This page already carries the six-field schedule table, so the checklist
    is the second original asset rather than the required one. It answers the
    question the whole family turns on before anyone pays.
    """
    def card(cls, head, items):
        lis = ''.join('<li>%s</li>' % i for i in items)
        return (f"<div class='cnf-card {cls}'><h3>{head}</h3>"
                f"<ul>{lis}</ul></div>")
    return (CHECK_CSS + "<div class='cnf-grid'>"
            + card('', 'The year is nil', v['chk_yes'])
            + card('cnf-no', 'The year is not nil', v['chk_no'])
            + card('', 'Due either way', v['chk_both'])
            + '</div>')


SCHED_CSS = (
 '<style>'
 '.cnf-sched{width:100%;border-collapse:collapse;margin:0 0 14px;'
 'font-family:Lato,sans-serif;font-size:15.5px}'
 '.cnf-sched th{background:#0B1A33;color:#fff;text-align:left;padding:11px 14px;'
 'font-family:Poppins,sans-serif;font-weight:600;font-size:15px;'
 'border:1px solid #233457}'
 '.cnf-sched td{padding:10px 14px;border:1px solid #d9e1ee;color:#39414d;'
 'line-height:1.55;vertical-align:top}'
 '.cnf-sched tr:nth-child(even) td{background:#f5f8fc}'
 '.cnf-sched .cnf-req{white-space:nowrap;font-weight:600;color:#0B1A33}'
 '.cnf-src{font-family:Lato,sans-serif;font-size:14px;color:#6b7686;'
 'line-height:1.6;margin:0}'
 '@media(max-width:780px){.cnf-sched,.cnf-sched tbody,.cnf-sched tr,'
 '.cnf-sched td{display:block;width:100%}.cnf-sched thead{display:none}'
 '.cnf-sched tr{margin:0 0 12px;border:1px solid #d9e1ee;border-radius:8px;'
 'overflow:hidden}.cnf-sched td{border:0;border-bottom:1px solid #eef2f8}}'
 '</style>'
)


def sched_table(v):
    rows = ''.join(
        f'<tr><td><strong>{a}</strong></td><td>{b}</td>'
        f"<td class='cnf-req'>{c}</td><td>{d}</td></tr>"
        for a, b, c, d in v['sched_rows'])
    return (SCHED_CSS +
            "<table class='cnf-sched'><thead><tr>"
            "<th scope='col'>Schedule</th><th scope='col'>What it reports</th>"
            "<th scope='col'>On a nil year</th><th scope='col'>Why</th>"
            '</tr></thead><tbody>' + rows + '</tbody></table>'
            f"<p class='cnf-src'>{v['sched_note']}</p>")


def geo_html(v):
    j = ', '.join(f"<a href='{SITE}{u}'>{n}</a>" for n, u in GEO)
    c = ', '.join(f"<a href='{SITE}{u}'>{n}</a>" for n, u in CITIES)
    return P(
        f'The return is prepared and transmitted electronically, so a '
        f'{v["short"]} is filed the same way wherever its registered office '
        f'sits. Jurisdiction pages: {j}.',
        f'City pages: {c}. A Quebec corporation also files the CO-17 and an '
        f'Alberta corporation also files the AT1. Both are separate '
        f'provincial returns and neither is included in the fee.')


FAQ_CSS = (
 '<style>'
 '.cnf-faq details{background:#f5f8fc;border-radius:12px;margin:0 0 12px;'
 'padding:16px 20px}'
 '.cnf-faq summary{cursor:pointer;font-family:Poppins,sans-serif;'
 'font-weight:600;font-size:17px;line-height:1.45;color:#0B1A33;'
 'list-style:none}'
 '.cnf-faq summary::-webkit-details-marker{display:none}'
 '.cnf-faq summary:after{content:"+";float:right;margin-left:12px;'
 'font-weight:700;color:#314D8A}'
 '.cnf-faq details[open] summary:after{content:"\\2013"}'
 '.cnf-faq .cnf-a{margin:12px 0 0;font-family:Lato,sans-serif;font-size:16px;'
 'line-height:1.6;color:#4a5568}'
 '.cnf-faq .cnf-a p{margin:0 0 10px}.cnf-faq .cnf-a p:last-child{margin:0}'
 '</style>'
)


def schema(v, slug):
    """Service plus BreadcrumbList.

    Hard rule 6 bars review, aggregateRating, FAQPage and HowTo, so the graph
    carries none of them even though the page has an FAQ block and a numbered
    process. The source template's graph had a malformed "@graph" holding a
    single object rather than a list; this emits a list.
    """
    url = f'{SITE}/nil-t2-filing-for-{slug}/'
    g = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'Service', '@id': url + '#service',
         'name': f'Nil T2 Filing for {v["name"]}',
         'description': v['desc'],
         'serviceType': 'Nil T2 corporate income tax return preparation and '
                        'electronic filing',
         'areaServed': {'@type': 'Country', 'name': 'Canada'},
         'provider': {'@type': 'Organization',
                      'name': 'Gondaliya CPA Professional Corporation',
                      'url': SITE},
         'offers': {'@type': 'Offer', 'price': '300.00',
                    'priceCurrency': 'CAD',
                    'description': '$300.00 plus HST per tax year',
                    'url': PRICE}},
        {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb',
         'itemListElement': [
            {'@type': 'ListItem', 'position': 1,
             'name': 'Nil T2 filing in Canada', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2,
             'name': 'Nil T2 filing by corporation type',
             'item': SITE + '/services/'},
            {'@type': 'ListItem', 'position': 3,
             'name': f'Nil T2 Filing for {v["name"]}', 'item': url}]}]}
    return ("<script type='application/ld+json'>"
            + json.dumps(g, ensure_ascii=False).replace('"', chr(39)) + '</script>')


def build(slug):
    v = VERTICALS[slug]

    # (source index, {widget index: {setting: value}}, {widget index: url})
    PLAN = [
     # ---- hero -------------------------------------------------------------
     (0, {1: {'title': v['h1']},
          2: {'editor': P(v['lede'])},
          3: {'title_text': TRUST_BOX[0], 'description_text': TRUST_BOX[1]},
          # The source line here was "✅ REGISTERED CPA FIRM- VERIFY NOW":
          # an emoji, which is banned outright, over a claim this site does
          # not make in those words.
          4: {'editor': P('Registered EFILE electronic filer. Your CRA '
                          'confirmation is emailed within 3 business days.')},
          5: {'text': CTA}, 6: {'text': 'See the price'}},
         {5: FORM, 6: PRICE}),
     # ---- intro, the two-paragraph fact pattern -----------------------------
     (1, {0: {'title': v['intro_h']},
          1: {'editor': P(*v['intro'])},
          2: {'text': CTA}, 3: {'text': 'See the price'}},
         {2: FORM, 3: PRICE}),
     # ---- rule 8 block ------------------------------------------------------
     (4, {0: {'title': v['notnil_h']}}, {}),
     (6, {i: {'title_text': t, 'description_text': d}
          for i, (t, d) in enumerate(v['notnil_boxes'])}, {}),
     (5, {0: {'editor': P(*v['notnil_text'])}}, {}),
     # ---- six-field schedule row (plan line 1209) ---------------------------
     (7, {0: {'title': v['sched_h']}}, {}),
     (32, {0: {'editor': sched_table(v)}}, {}),
     (8, {i: {'title_text': t, 'description_text': d}
          for i, (t, d) in enumerate(v['sched_boxes'])}, {}),
     # ---- why --------------------------------------------------------------
     (10, {0: {'title': v['why_h']}}, {}),
     # Section 11 is image/heading/text repeated four times, section 13 is
     # heading/text repeated three times. Both were briefly emitted twice,
     # once for the headings and once for the bodies, which shipped the
     # section twice and left the source copy standing in the first.
     (11, {**{1 + i * 3: {'title': t} for i, (t, _) in enumerate(v['why'])},
           **{2 + i * 3: {'editor': P(d)} for i, (_, d) in enumerate(v['why'])}},
          {}),
     (13, {**{i * 2: {'title': t} for i, (t, _) in enumerate(v['strip'])},
           **{i * 2 + 1: {'editor': P(d)} for i, (_, d) in enumerate(v['strip'])}},
          {}),
     (14, {0: {'text': CTA}, 1: {'text': 'See the price'}}, {0: FORM, 1: PRICE}),
     # ---- twelve cards ------------------------------------------------------
     (15, {0: {'title': v['svc_h']}}, {}),
     (16, None, {}),
     (17, {0: {'html': checklist(v)}}, {}),
     # ---- process -----------------------------------------------------------
     (23, {0: {'editor': P('HOW IT WORKS')},
           1: {'title': v['proc_h']},
           2: {'text': CTA},
           3: {'editor': P(v['proc_lede'])},
           4: {'editor': P(v['proc_note'])}}, {2: FORM}),
     (24, {}, {}),
     (25, {0: {'title': 'Every unfiled year stays open until the return is '
                        'transmitted.'},
           1: {'text': CTA}, 2: {'text': 'See the price'}},
         {1: FORM, 2: PRICE}),
     # ---- price -------------------------------------------------------------
     (26, {0: {'editor': P(v['price_eyebrow'])},
           1: {'title': v['price_h']},
           2: {'text': CTA},
           3: {'editor': P(v['price_text'])}}, {2: FORM}),
     # ---- geography ---------------------------------------------------------
     (31, {0: {'title': v['geo_h']}}, {}),
     (5,  {0: {'editor': geo_html(v)}}, {}),
     # ---- FAQ ---------------------------------------------------------------
     (35, {0: {'title': f'{v["name"]} and Nil T2 Filing: Questions'}}, {}),
     (36, None, {}),
     (37, {0: {'title': v['cta_h']},
           1: {'text': CTA}, 2: {'text': 'See the price'}},
         {1: FORM, 2: PRICE}),
     (38, {0: {'html': schema(v, slug)}}, {}),
    ]

    out = []
    for idx, fields, links in PLAN:
        sec = copy.deepcopy(src[idx])
        reid(sec)
        ws = widgets(sec)

        if fields:
            for wi, kv in fields.items():
                if wi >= len(ws):
                    raise SystemExit(
                        f'{slug}: section {idx} has {len(ws)} widgets, '
                        f'index {wi} requested')
                for k, val in kv.items():
                    if k not in ws[wi]['settings']:
                        raise SystemExit(
                            f'{slug}: section {idx} widget {wi} '
                            f'({ws[wi].get("widgetType")}) has no {k!r}')
                    ws[wi]['settings'][k] = val

        if idx == 0:
            if not isinstance(sec.get('settings'), dict):
                sec['settings'] = {}
            sec['settings'].update(copy.deepcopy(HERO))
            for w in ws:
                st = w['settings']
                if w.get('widgetType') == 'image-box':
                    st['title_typography_typography'] = 'custom'
                    st['title_typography_font_family'] = 'Poppins'
                    st['title_typography_font_size'] = {'unit': 'px',
                                                        'size': 24, 'sizes': []}
                    st['title_typography_font_weight'] = '600'
                if w.get('widgetType') == 'text-editor' and 'text_color' not in st:
                    st['text_color'] = '#FFFFFF'

        if idx == 16:
            boxes = [w for w in ws if w.get('widgetType') == 'elementskit-icon-box']
            if len(boxes) != len(SERVICES):
                raise SystemExit(f'{slug}: section 16 has {len(boxes)} cards, '
                                 f'{len(SERVICES)} links defined')
            for w, (path, t, d) in zip(boxes, SERVICES):
                s = w['settings']
                s['ekit_icon_box_title_text'] = t
                s['ekit_icon_box_description_text'] = d
                # The source badge read "EXCLUSIVE" on all twelve.
                if 'ekit_icon_box_badge_title' in s:
                    s['ekit_icon_box_badge_title'] = ''
                if 'ekit_icon_box_btn_text' in s:
                    s['ekit_icon_box_btn_text'] = 'Read it'
                setlink(w, SITE + path)

        if idx == 24:
            heads = [w for w in ws if w.get('widgetType') == 'heading']
            texts = [w for w in ws if w.get('widgetType') == 'text-editor']
            for i, (t, d) in enumerate(v['steps']):
                heads[i * 2].setdefault('settings', {})
                heads[i * 2]['settings']['title'] = f'Step {i + 1}'
                heads[i * 2 + 1]['settings']['title'] = t
                texts[i]['settings']['editor'] = P(d)

        if idx == 36:
            acc = [w for w in ws if w.get('widgetType') == 'nested-accordion'][0]
            items = acc['settings'].get('items') or []
            texts = [w for w in ws if w.get('widgetType') == 'text-editor']
            if len(items) != len(v['faq']) or len(texts) != len(v['faq']):
                raise SystemExit(
                    f'{slug}: accordion has {len(items)} items and '
                    f'{len(texts)} panels, copy has {len(v["faq"])} entries')
            for i, (q, a) in enumerate(v['faq']):
                items[i]['item_title'] = q
                body = P(a) if i else FAQ_CSS + P(a)
                texts[i]['settings']['editor'] = body
            # The panels live in containers; wrap the lot so .cnf-faq applies.
            # Elementor writes an empty settings object as [], not {}.
            if not isinstance(sec.get('settings'), dict):
                sec['settings'] = {}
            cls = sec['settings'].get('css_classes', '')
            sec['settings']['css_classes'] = (cls + ' cnf-faq').strip()

        desource(sec)
        out.append(sec)
    return out


made = []
for slug in (WANT or list(VERTICALS)):
    v = VERTICALS[slug]
    content = build(slug)
    tpl = {'version': '0.4', 'title': f'CorpNil Vertical — {v["name"]}',
           'type': 'page', 'content': content,
           'page_settings': {'hide_title': 'yes'}}
    path = os.path.join(OUTDIR, f'corpnil-vertical-{slug}.json')
    json.dump(tpl, open(path, 'w'), ensure_ascii=False, separators=(',', ':'))
    made.append((slug, v['name'], len(content), os.path.getsize(path)))

for slug, name, nsec, size in made:
    print(f'  {name:34s} {nsec:>2} sections  {size:>8,} b')
print(f'{len(made)} template(s) written to {OUTDIR}')
