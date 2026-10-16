"""Family 5 launch gate. Line 1213 plus the hard rules in CLAUDE.md and 7.4."""
import json, re, sys

recs = json.load(open('f5-manifest.json'))
fail = []

BANNED = ['cheapest', 'lowest price', 'best price', 'unbeatable', 'guarantee',
          'guaranteed', 'risk-free', 'risk free', 'fastest', 'instant filing',
          'no obligation', 'penalty free', 'penalty-free', 'zero penalty',
          'authorized', 'authorised', 'cra agent', 'cra approved', 'cra partner',
          'cra endorsed', 'book a call', 'calendly', 'starting from']
QUAL_HEAD = 'A true nil return carries no percentage late-filing penalty'

for r in recs:
    s, c = r['slug'], r['content']
    low = c.lower()

    # Gate line 1213: 40 to 60 word answer-first paragraph, per question.
    n = len(r['answer'].split())
    if not 40 <= n <= 60:
        fail.append('%s: answer is %d words, needs 40-60' % (s, n))
    if c.count(r['answer']) < 2:   # body paragraph + schema description
        fail.append('%s: answer paragraph not reused as meta description' % s)

    # Hard rule 2: T183CORP, never bare T183.
    if re.search(r'T183(?!CORP)', c):
        fail.append('%s: bare T183' % s)

    # Hard rule 3: no standalone "no penalty"; the full block must be present.
    if 'penalty' in low and QUAL_HEAD not in c:
        fail.append('%s: penalty mentioned without the 7.4 qualification block' % s)

    # Hard rule 1: CRA wording.
    if 'registered EFILE electronic filer' not in c:
        fail.append('%s: missing the approved EFILE sentence' % s)

    # Hard rule 4 and the 7.4 table.
    for b in BANNED:
        if b in low:
            fail.append('%s: banned phrase "%s"' % (s, b))

    # Hard rule 5: no EFILE number, no GroupID.
    if re.search(r'\b\d{6}\b', c) and 'EFILE' in c:
        if re.search(r'EFILE[^.]{0,40}\d{6}', c):
            fail.append('%s: possible EFILE number near EFILE wording' % s)

    # Hard rule 6: no FAQPage, no HowTo, no review schema.
    for bad in ['FAQPage', 'HowTo', 'aggregateRating', '"Review"']:
        if bad in c:
            fail.append('%s: banned schema %s' % (s, bad))

    # Hard rule 9 / standing correction: price wording.
    if '$300.00 plus HST per tax year' not in c:
        fail.append('%s: price line missing' % s)
    if 'including HST' in c:
        fail.append('%s: "including HST" contradicts the standing correction' % s)

    # Structure from line 1578.
    if c.count('<h1>') != 1:
        fail.append('%s: %d H1' % (s, c.count('<h1>')))
    if c.count('<table') != 1:
        fail.append('%s: needs exactly one table, has %d' % (s, c.count('<table')))
    if '<h2>' not in c:
        fail.append('%s: no H2' % s)

    # 7.5: byline and last-reviewed.
    if 'CPA Ontario Membership 61040184' not in c:
        fail.append('%s: no byline' % s)
    if 'Last reviewed:' not in c:
        fail.append('%s: no last-reviewed line' % s)

    # 6(g) line 1527: max 15 outbound body links.
    links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', c))
    if len(links) > 15:
        fail.append('%s: %d outbound links, cap is 15' % (s, len(links)))

    # No emoji anywhere.
    if any(ord(ch) > 0x2100 for ch in c):
        fail.append('%s: non-ASCII symbol that may be an emoji' % s)

    # Valid schema.
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', c, re.S)
    json.loads(m.group(1))

# Inbound: each page must be linked by at least 3 others (6(g) minimum).
for r in recs:
    inbound = sum(1 for o in recs if o['slug'] != r['slug'] and r['slug'] in o['content'])
    if inbound < 3:
        fail.append('%s: only %d inbound sibling links, needs 3' % (r['slug'], inbound))

if fail:
    print('GATE FAILED')
    for f in fail:
        print(' -', f)
    sys.exit(1)

print('gate clear on all %d pages' % len(recs))
for r in recs:
    links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', r['content']))
    inbound = sum(1 for o in recs if o['slug'] != r['slug'] and r['slug'] in o['content'])
    print('  %-62s %2d words  in:%d  out:%2d  %5d bytes'
          % (r['slug'][:62], len(r['answer'].split()), inbound, len(links),
             len(r['content'].encode())))
