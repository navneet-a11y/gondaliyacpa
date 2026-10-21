"""Jurisdiction hub gate: the CLAUDE.md hard rules plus the 7.6 banned list."""
import json, re, sys

recs = json.load(open('jurisdictions-manifest.json'))
fail = []

BANNED = ['cheapest', 'lowest price', 'best price', 'unbeatable', 'guarantee',
          'risk-free', 'risk free', 'fastest', 'instant filing', 'no obligation',
          'penalty free', 'penalty-free', 'zero penalty', 'no penalty',
          'authorized', 'authorised', 'cra agent', 'cra approved', 'cra partner',
          'cra endorsed', 'book a call', 'calendly', 'starting from', 'simply',
          'easily', 'such as', ' just ', 'five-star', 'money-back']
QUAL_HEAD = 'A true nil return carries no percentage late-filing penalty'

# Hard rule 9 / the standing correction. Also the HST-accuracy check: the
# non-HST jurisdictions must not carry a province-specific HST computation.
HST_JURISDICTIONS = {'ontario', 'new-brunswick', 'nova-scotia',
                     'newfoundland-and-labrador', 'prince-edward-island'}

for r in recs:
    s, c = r['slug'], r['content']
    low = c.lower()

    if 'registered EFILE electronic filer' not in c:
        fail.append('%s: missing the approved EFILE sentence' % s)
    if re.search(r'T183(?!CORP)', c):
        fail.append('%s: bare T183' % s)
    # hard rule 3
    if 'penalt' in low and QUAL_HEAD not in c:
        fail.append('%s: penalty mentioned without the 7.4 qualification block' % s)
    for b in BANNED:
        if b in low:
            fail.append('%s: banned phrase "%s"' % (s, b.strip()))
    for bad in ['FAQPage', 'HowTo', 'aggregateRating', '"Review"']:
        if bad in c:
            fail.append('%s: banned schema %s' % (s, bad))
    # hard rule 9 and the standing correction
    if '$300.00 plus HST' not in c:
        fail.append('%s: price line missing' % s)
    if 'including HST' in c:
        fail.append('%s: "including HST" contradicts the standing correction' % s)
    # HST accuracy: no HST rate or HST-inclusive total outside an HST province
    if s not in HST_JURISDICTIONS:
        for m in re.finditer(r'(\d+)\s*per cent HST|HST[^.]{0,30}\$[\d,]+\.\d\d', c):
            fail.append('%s: HST computation on a non-HST jurisdiction: "%s"'
                        % (s, m.group(0)))
    # hard rule 8: the not-nil routing block
    if 'is not nil' not in c:
        fail.append('%s: missing the not-nil statement' % s)
    if 'gondaliyacpa.ca at $350.00 plus HST' not in c:
        fail.append('%s: missing the overflow routing line' % s)
    # structure
    if c.count('<h1>') != 1:
        fail.append('%s: %d H1' % (s, c.count('<h1>')))
    if 'Last reviewed:' not in c:
        fail.append('%s: no last-reviewed line' % s)
    # 7.5 byline rule 3: exact wording, including the membership number, on any
    # page stating a filing rule, a penalty figure, a schedule requirement or a
    # T183CORP rule. A jurisdiction hub states filing rules.
    if 'Written and reviewed by' not in c:
        fail.append('%s: byline is not the 7.5 rule 3 form' % s)
    if 'CPA Ontario Membership 61040184' not in c:
        fail.append('%s: byline missing the membership number' % s)
    if re.search(r'By <a[^>]*>Sharad Gondaliya, CPA</a>, registered EFILE', c):
        fail.append('%s: superseded byline form' % s)
    # 7.5 last-reviewed rule 1: the visible line renders under the H1, above the
    # first paragraph, on every URL.
    if not re.search(r'cnf-rev">Last reviewed: [A-Z][a-z]+ \d{1,2}, \d{4}', c):
        fail.append('%s: no Last reviewed line in the position 7.5 rule 1 gives' % s)
    if any(ord(ch) > 0x2100 for ch in c):
        fail.append('%s: non-ASCII symbol that may be an emoji' % s)
    # no invented statistics: a bare thousands-separated integer in a data cell
    for m in re.finditer(r'<td>([\d]{1,3}(?:,\d{3})+)</td>', c):
        fail.append('%s: unsourced count "%s" in a data cell' % (s, m.group(1)))
    # no internal references
    for pat in [r'\bthe plan\b', r'appendix a', r'6\([a-k]\)', r'line 1[0-9]{3}']:
        for m in re.finditer(pat, c, re.I):
            fail.append('%s: internal reference "%s"' % (s, m.group(0)))
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', c, re.S)
    json.loads(m.group(1))

if fail:
    print('GATE FAILED')
    for f in fail:
        print(' -', f)
    sys.exit(1)

print('gate clear on all %d jurisdiction hubs' % len(recs))
for r in recs:
    links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', r['content']))
    print('  %-20s out:%2d  %6d bytes' % (r['slug'], len(links),
                                          len(r['content'].encode())))
