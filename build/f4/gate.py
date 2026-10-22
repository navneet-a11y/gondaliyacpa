"""Hard-rule gate for the British Columbia F4 service pages."""
import io, re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_f4_bc import SERVICES, PLACE

HST_PROVINCES = ('ontario', 'new brunswick', 'nova scotia',
                 'newfoundland and labrador', 'prince edward island')
fail = []
for s in SERVICES:
    slug = s['slug']
    c = io.open(slug + '.html', encoding='utf-8').read()
    low = c.lower()
    def bad(msg): fail.append('%s: %s' % (slug, msg))

    # 1 CRA wording. 7.6 permits "authorized signing officer", and requires it,
    # but only on and about Form T183CORP, so that phrase is removed before the
    # test. "CRA authorized" and "authorized by CRA" are still caught.
    low1 = low.replace('authorized signing officer', '')
    for w in ('authorized', 'cra agent', 'cra-approved', 'cra approved',
              'cra partner', 'endorsed by the cra', 'cra logo'):
        if w in low1: bad('rule 1 banned CRA wording "%s"' % w)
    # 2 T183CORP
    if re.search(r'\bT183\b(?!CORP)', c): bad('rule 2 bare T183')
    # 3 penalty claims
    if re.search(r'(no penalty|penalty[- ]free|zero penalty)', low):
        bad('rule 3 unqualified penalty claim')
    # 4 superlatives
    for w in ('cheapest', 'best price', 'fastest', 'guaranteed', 'risk-free',
              'risk free', 'lowest price'):
        if w in low: bad('rule 4 "%s"' % w)
    # 5 EFILE number / GroupID
    if re.search(r'efile\s*(number|#|no\.)', low) or 'groupid' in low:
        bad('rule 5 EFILE number or GroupID')
    # 6 forbidden schema
    for w in ('faqpage', 'howto', 'aggregaterating', '"review"'):
        if w in low: bad('rule 6 schema "%s"' % w)
    # 9 price wording
    if 'including HST' in c: bad('rule 9 "including HST"')
    if '$300.00 plus HST' not in c: bad('rule 9 price string missing')
    # BC is not an HST province: no HST arithmetic anywhere
    if re.search(r'\d+\s*per cent HST', c) or re.search(r'\$3[0-9]{2}\.\d\d\s*in total', c):
        bad('HST computation on a non-HST province')
    ALLOWED_MONEY = {
      '300.00':   'the price',
      '350.00':   'the gondaliyacpa.ca overflow price',
      '12.00':    'the Corporations Canada annual return fee',
      '0.00':     'tax owing on a nil return, in the 7.6 qualification sentence',
      '25.00':    'the non-resident daily penalty, same sentence',
      '2,500.00': 'that penalty\'s maximum, same sentence',
      '600.00':   'two tax years at the price',
      '900.00':   'three tax years at the price',
      '1,500.00': 'five tax years at the price',
    }
    for m in re.finditer(r'\$(\d{1,3}(?:,\d{3})*\.\d\d)', c):
        if m.group(1) not in ALLOWED_MONEY:
            bad('unexpected money figure $%s' % m.group(1))
    # 7.5 rule 3 byline
    if 'CPA Ontario Membership 61040184' not in c: bad('7.5 rule 3 byline missing')
    if 'Last reviewed:' not in c: bad('7.5 rule 1 review date missing')
    # structure
    if c.count('<h1') != 1: bad('h1 count %d' % c.count('<h1'))
    if a := [x for x in re.findall(r'<(h[1-6])', c) if x == 'h3']:
        bad('unexpected h3 on a service page')
    if 'areaServed' not in c or PLACE not in c: bad('schema areaServed missing')
    # no invented counts in the data table
    for m in re.finditer(r'<td>(\d{1,3}(?:,\d{3})+)</td>', c):
        bad('unsourced count "%s"' % m.group(1))
    # text hygiene
    nb = sorted({ch for ch in c if ord(ch) > 127})
    if nb: bad('non-ascii %r' % nb)
    if '  ' in re.sub(r'<[^>]+>', '', c): bad('double space in body text')

# cross-page: every page must link the hub and its national sibling, and
# descriptions must be distinct
bodies = {s['slug']: io.open(s['slug'] + '.html', encoding='utf-8').read()
          for s in SERVICES}
for s in SERVICES:
    c = bodies[s['slug']]
    if '/british-columbia/' not in c: fail.append('%s: no hub link' % s['slug'])
    if s['national'][0] not in c:
        fail.append('%s: no national sibling link' % s['slug'])
leads = [s['lead'][0] for s in SERVICES]
if len(set(leads)) != len(leads): fail.append('duplicate lead paragraph')
excs = [s['excerpt'] for s in SERVICES]
if len(set(excs)) != len(excs): fail.append('duplicate excerpt')
for s in SERVICES:
    if len(s['excerpt']) > 155:
        fail.append('%s: excerpt %d chars' % (s['slug'], len(s['excerpt'])))

if fail:
    print('GATE FAIL')
    for f in fail: print('  ' + f)
    raise SystemExit(1)
print('gate clear on all %d British Columbia service pages' % len(SERVICES))
for s in SERVICES:
    print('  %-46s %6d bytes' % (s['slug'], len(bodies[s['slug']].encode('utf-8'))))
