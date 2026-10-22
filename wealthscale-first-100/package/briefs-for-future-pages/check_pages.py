#!/usr/bin/env python3
"""QA for WealthScale page files. Usage: python3 check_pages.py [file ...]  (default: all pages)"""
import csv, glob, html, json, os, re, sys

ROOT = '/home/claude/ws100'
PLAN = {p['id']: p for p in json.load(open(f'{ROOT}/briefs/plan.json'))}
LINKS = {r['url'] for r in csv.DictReader(open(f'{ROOT}/briefs/links.csv'))}
WIDGETS = set(json.load(open(f'{ROOT}/qa/widget_names.json'))) if os.path.exists(f'{ROOT}/qa/widget_names.json') else None
TARGET = {'home': 4000, 'hub': 3000, 'calculator': 3000, 'account-guide': 5000, 'ws-review': 5000, 'ws-guide': 5000,
          'best-of': 6500, 'account-listing': 6500, 'rates': 5000, 'review': 5500, 'versus-platform': 4500,
          'versus-account': 4500, 'learn-guide': 4500, 'markets-guide': 4500, 'benefit-dates': 3500,
          'trust': 1500, 'profile': 1200, 'legal': 300}
BANNED = ['delve', 'dive into', 'navigate', 'landscape', 'realm', 'unlock', 'unleash', 'leverag', 'seamless', 'robust',
          'cutting-edge', 'game-changer', 'game changer', 'empower', 'elevate', 'embark', 'journey', 'tapestry', 'myriad',
          'plethora', 'boasts', 'stands out', 'holistic', 'streamline', 'ever-evolving', "in today's", "it's important to note",
          'it is important to note', "it's worth noting", 'it is worth noting', 'when it comes to', "whether you're",
          'look no further', 'rest assured', 'peace of mind', 'crucial', 'comprehensive guide', 'ultimate guide',
          'in conclusion', 'in summary', 'at the end of the day', 'a testament to', 'nestled', 'vibrant', 'bustling',
          'we tested', 'we opened an account', 'in our experience', 'cfa level', 'level iii', 'cfa certified', ' mba',
          'visit the cra', 'canada.ca', 'cra website', "provider's website", 'official website']
PROFILE_OK = ('/about/sharad-gondaliya/', '/about/neha-gupta/')
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')


def text_of(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()


def check(path):
    raw = open(path, encoding='utf-8').read()
    issues, warn = [], []
    m = re.match(r'\s*<!--(.*?)-->', raw, re.S)
    meta = {}
    if not m:
        issues.append('missing header comment')
    else:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip()
    try:
        pid = int(meta.get('id', os.path.basename(path)[:3]))
    except ValueError:
        pid = int(os.path.basename(path)[:3])
    plan = PLAN.get(pid)
    if not plan:
        return pid, ['id not in plan'], [], 0
    body = raw[m.end():] if m else raw
    page = body.split('<script type="application/ld+json">')[0]
    # header fields
    st, md = meta.get('seo_title', ''), meta.get('meta_description', '')
    if plan['page_type'] != 'legal':
        if not (45 <= len(st) <= 62) and pid != 101: issues.append(f'seo_title length {len(st)}')
        if not (135 <= len(md) <= 160): issues.append(f'meta_description length {len(md)}')
        kw = plan['focus_keyword'].lower()
        if kw.replace("'", '') not in st.lower().replace("'", '').replace('’', '') and plan['page_type'] not in ('profile',):
            warn.append('focus keyword not in seo_title')
        if kw.replace("'", '') not in md.lower().replace("'", '').replace('’', '') and plan['page_type'] not in ('profile',):
            warn.append('focus keyword not in meta_description')
    if meta.get('url') != plan['url']: issues.append(f"url mismatch {meta.get('url')}")
    # H1
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', page, re.S)
    if len(h1s) != 1: issues.append(f'{len(h1s)} h1 tags')
    elif text_of(h1s[0]) != plan['h1'] and plan['year_in_title'] == 'no': issues.append(f'h1 differs: {text_of(h1s[0])}')
    elif plan['h1'] not in text_of(h1s[0]): issues.append(f'h1 differs: {text_of(h1s[0])}')
    # words
    no_exp = re.sub(r'<section class="ws-section" id="experts">.*?</section>', ' ', page, flags=re.S)
    words = len(text_of(no_exp).split())
    tgt = TARGET.get(plan['page_type'], 2000)
    if words < 0.85 * tgt: issues.append(f'words {words} < target {tgt}')
    # keyword in first 120 words of lead
    lead = re.search(r'<p class="ws-lead">(.*?)</p>', page, re.S)
    kw = plan['focus_keyword'].lower().replace("'", '')
    if plan['page_type'] not in ('legal',):
        if not lead: issues.append('no ws-lead paragraph')
        elif kw not in ' '.join(text_of(lead.group(1)).lower().replace("'", '').replace('’', '').split()[:120]) and plan['page_type'] not in ('profile', 'trust', 'home'):
            warn.append('focus keyword not in lead')
    # links
    for href in re.findall(r'href="([^"]+)"', page):
        if href.startswith('#'): continue
        if href.startswith('http') or href.startswith('//'):
            if plan['url'] in PROFILE_OK: continue
            issues.append(f'outbound link {href}')
            continue
        if href.startswith('mailto:') and plan['url'] in ('/contact/', '/privacy-policy/', '/about/'): continue
        base = href.split('#')[0]
        if base not in LINKS: issues.append(f'internal link not in plan {href}')
    # anchors
    ids = set(re.findall(r'\sid="([^"]+)"', page))
    for a in re.findall(r'href="#([^"]+)"', page):
        if a not in ids and not a.startswith('ws-'): issues.append(f'anchor target missing #{a}')
    for a in re.findall(r'href="#(ws-[^"]+)"', page):
        if f'data-ws-widget="{a[3:]}"' not in page: issues.append(f'button points to absent widget #{a}')
    h2 = re.findall(r'<h2([^>]*)>(.*?)</h2>', page, re.S)
    for attrs, t in h2:
        if 'id="' not in attrs: issues.append(f'h2 without id: {text_of(t)[:40]}')
    toc = re.search(r'<nav class="ws-toc".*?</nav>', page, re.S)
    if plan['page_type'] not in ('legal', 'profile', 'trust') and not toc: issues.append('no table of contents')
    if toc:
        tl = set(re.findall(r'href="#([^"]+)"', toc.group(0)))
        for attrs, t in h2:
            i = re.search(r'id="([^"]+)"', attrs)
            if i and i.group(1) not in tl and i.group(1) not in ('at-a-glance', 'meet-the-experts'): warn.append(f'h2 not in toc: {i.group(1)}')
    # snippets
    need = ['ws-byline', 'ws-trust', 'id="meet-the-experts"', 'ws-checked', 'ws-disclaimer', 'Sharad Gondaliya, CPA', 'Neha Gupta, CFA']
    if plan['page_type'] == 'legal': need = ['ws-disclaimer']
    for n in need:
        if n not in page: issues.append(f'missing {n}')
    if plan['page_type'] != 'legal':
        if plan['neha_scope'] == 'yes' and 'data-ws-review="pending"' not in page: issues.append('missing pending review status (in scope)')
        if plan['neha_scope'] == 'no' and 'data-ws-review="pending"' in page: issues.append('review status on out-of-scope page')
    # widgets
    want = [w.strip().split('[')[0] for w in plan['widgets'].split(',') if w.strip()]
    have = re.findall(r'data-ws-widget="([^"]+)"', page)
    for w in want:
        if w not in have: issues.append(f'missing widget {w}')
    if WIDGETS:
        for w in have:
            if w not in WIDGETS: issues.append(f'unknown widget {w}')
    if len(have) != len(set(have)) and have.count('table-filter') < 2: warn.append('a widget repeats')
    # FAQ JSON-LD
    faqs = re.findall(r'<details>\s*<summary>(.*?)</summary>', page, re.S)
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', body, re.S)
    faq_ld = None
    for b in blocks:
        try:
            j = json.loads(b)
        except Exception as e:
            issues.append(f'JSON-LD does not parse: {e}')
            continue
        if isinstance(j, dict) and j.get('@type') == 'FAQPage': faq_ld = j
    if faqs and not faq_ld: issues.append('FAQ without FAQPage JSON-LD')
    if faq_ld:
        qs = [q['name'] for q in faq_ld.get('mainEntity', [])]
        if len(qs) != len(faqs): issues.append(f'FAQ count {len(faqs)} vs JSON-LD {len(qs)}')
        vis = [text_of(f) for f in faqs]
        for q in qs:
            if q not in vis: issues.append(f'JSON-LD question not visible: {q[:50]}')
    # language
    low = text_of(page).lower()
    for b in BANNED:
        if b in low: issues.append(f'banned phrase "{b.strip()}"')
    if '—' in page: issues.append('em dash used')
    if EMOJI.search(page): issues.append('emoji')
    if re.search(r'[a-z]!\s', text_of(page)): issues.append('exclamation mark')
    if re.search(r'\ba CFA\b(?! charterholder)', text_of(page)): issues.append('"a CFA" without charterholder')
    if re.search(r'financial (advisor|planner)', low): warn.append('mentions financial advisor/planner (check it is not about our people)')
    if '/reviews/wealthsimple/' in plan['url'] or '/vs/wealthsimple' in plan['url']:
        if 'WealthScale is independent and not affiliated with Wealthsimple.' not in page: issues.append('missing Wealthsimple independence line')
    for s in re.findall(r'style="([^"]*)"', page):
        if not re.fullmatch(r'width:\d{1,3}(\.\d)?%', s.strip()): issues.append(f'inline style {s}')
    if '<style' in page: issues.append('style tag')
    if re.search(r'<script(?! type="application/ld\+json")', page): issues.append('script tag in body')
    # tables
    for t in re.finditer(r'<table', page):
        before = page[max(0, t.start() - 200):t.start()]
        if 'ws-table-wrap' not in before: issues.append('table not wrapped in ws-table-wrap')
    for td in re.findall(r'<td>(.*?)</td>', page, re.S):
        tt = text_of(td)
        if re.search(r'\d(\.\d+)?%?\s*(to|–|-)\s*\$?\d', tt) and not re.search(r'\d{4}\s*(to|–|-)\s*\d{4}', tt) and not re.search(r'(age|ages|years?)\s', tt.lower()):
            warn.append(f'possible range in table: {tt[:50]}')
    if 'This example is hypothetical' not in page and plan['page_type'] not in ('trust', 'profile', 'legal', 'hub', 'home'):
        warn.append('no hypothetical example label')
    return pid, issues, warn, words


def main():
    files = sys.argv[1:] or sorted(glob.glob(f'{ROOT}/pages/*.html'))
    rows, bad = [], 0
    for f in files:
        pid, iss, w, words = check(f)
        rows.append([pid, os.path.basename(f), words, len(iss), ' | '.join(iss), ' | '.join(w)])
        if iss: bad += 1
        print(f"{os.path.basename(f)}: {words} words, {len(iss)} issues, {len(w)} warnings")
        for i in iss: print('   ISSUE', i)
        for i in w: print('   warn ', i)
    with open(f'{ROOT}/qa/report.csv', 'w', newline='') as fh:
        cw = csv.writer(fh); cw.writerow(['id', 'file', 'words', 'issues', 'issue_list', 'warnings']); cw.writerows(rows)
    print(f'\n{len(files)} files, {bad} with issues')


if __name__ == '__main__':
    main()
