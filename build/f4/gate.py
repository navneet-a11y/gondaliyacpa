"""F4 gate: line 1212 plus the CLAUDE.md hard rules."""
import json, re, sys
recs = json.load(open('f4-ontario-manifest.json')); fail = []
BANNED = ['cra authorized','authorized by cra','cra agent','cra approved','cra partner',
          'cra endorsed','guarantee','guaranteed','cheapest','lowest price','best price',
          'unbeatable','fastest','instant filing','book a call','schedule a meeting',
          'free consultation','risk free','five-star','money-back','starting from',
          'audit proof']
QUAL = 'A true nil return carries no percentage late-filing penalty'

for r in recs:
    s, c, low = r['slug'], r['content'], r['content'].lower()
    # line 1212 gate
    if not 100 <= r['place_words'] <= 140:
        fail.append('%s: place paragraph %d words, target 120' % (s, r['place_words']))
    if '<h2>Ontario Data</h2>' not in c:
        fail.append('%s: no place data row' % s)
    for field in ('T2 returns assessed', 'Registry', 'Filing route'):
        if field not in c:
            fail.append('%s: data row missing "%s"' % (s, field))
    # hard rules
    if re.search(r'T183(?!CORP)', c): fail.append('%s: bare T183' % s)
    if 'penalty' in low and QUAL not in c:
        fail.append('%s: penalty without the 7.4 qualification block' % s)
    if 'registered EFILE electronic filer' not in c:
        fail.append('%s: missing approved EFILE phrasing' % s)
    for b in BANNED:
        if b in low: fail.append('%s: banned phrase "%s"' % (s, b))
    for bad in ['FAQPage','HowTo','aggregateRating','"Review"']:
        if bad in c: fail.append('%s: banned schema %s' % (s, bad))
    if '$300.00 plus HST per tax year' not in c: fail.append('%s: price line missing' % s)
    if 'including HST' in c: fail.append('%s: "including HST" contradicts the correction' % s)
    if c.count('<h1') != 1: fail.append('%s: %d H1' % (s, c.count('<h1')))
    if 'CPA Ontario Membership 61040184' not in c: fail.append('%s: no 7.5 rule 3 byline' % s)
    if 'Last reviewed:' not in c: fail.append('%s: no last-reviewed line' % s)
    if any(ord(ch) > 0x2100 for ch in c): fail.append('%s: possible emoji' % s)
    links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', c))
    if len(links) > 25: fail.append('%s: %d outbound, F4 cap is 25' % (s, len(links)))
    json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', c, re.S).group(1))

slugs = [r['slug'] for r in recs]
if len(set(slugs)) != len(slugs): fail.append('duplicate slug')

if fail:
    print('GATE FAILED')
    for f in fail: print(' -', f)
    sys.exit(1)
print('gate clear on all %d pages' % len(recs))
for r in recs:
    links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', r['content']))
    print('  %-58s place:%3dw  out:%2d  %5d bytes'
          % (r['slug'][:58], r['place_words'], len(links), len(r['content'].encode())))
