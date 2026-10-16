"""F9 pillar gate: line 1217 plus the CLAUDE.md hard rules and the 7.6 banned list."""
import json, re, sys

rec = json.load(open('f9-manifest.json'))[0]
c = rec['content']; low = c.lower(); fail = []

BANNED = ['cra authorized','authorized by cra','cra agent','agent of cra','cra approved',
          'approved by cra','cra partner','cra endorsed','endorsed by cra','guaranteed',
          'guarantee','cheapest','lowest price in canada','best price','unbeatable',
          'fastest','instant filing','same-day filing','filed in minutes','book a call',
          'schedule a meeting','free consultation','risk free','audit proof',
          'conservatively','easily','simply',' just ','e.g.','such as','starting from',
          # 'backdate' handled separately: 7.6 bans the word, but required
          # qualification 7 mandates "never backdated". See decisions.md.

          'five-star','5-star','money-back']

# line 1217 gate: visible update date AND a 12-row contents block
if 'Last reviewed:' not in c:
    fail.append('no visible update date')
toc = re.search(r'<div class="ei-toc">.*?</ol>', c, re.S)
if not toc:
    fail.append('no contents block')
else:
    n = toc.group(0).count('<li>')
    if n != 12:
        fail.append('contents block has %d rows, the gate requires 12' % n)
    for k, _t in [(m, m) for m in re.findall(r'href="#([a-z0-9-]+)"', toc.group(0))]:
        if ('id="%s"' % k) not in c:
            fail.append('contents row links to #%s with no matching section' % k)

# hard rules
if re.search(r'T183(?!CORP)', c):
    fail.append('bare T183')
if 'penalty' in low and 'A true nil return carries no percentage late-filing penalty' not in c:
    fail.append('penalty without the 7.4 qualification block')
if 'registered EFILE electronic filer' not in c:
    fail.append('missing the approved EFILE phrasing')
if 'Returns are prepared and transmitted in Canada' not in c:
    fail.append('F9 pillars need the three-sentence EFILE block')
# 7.6 conflict: the banned list bans "backdate" while required qualification 7
# requires "never backdated". Permit only the negated, compliant form.
for m in re.finditer(r'backdat\w*', low):
    if not low[max(0, m.start()-6):m.start()].endswith('never '):
        fail.append('"%s" not in the required "never backdated" form' % m.group(0))

for b in BANNED:
    if b in low:
        fail.append('banned phrase "%s"' % b.strip())
for bad in ['FAQPage', 'HowTo', 'aggregateRating', '"Review"']:
    if bad in c:
        fail.append('banned schema %s' % bad)
if re.search(r'\b(500\+|1300\+|600\+|\d+\+ (reviews|clients))', low):
    fail.append('count claim, banned until the claim audit closes')
if 'including HST' in c:
    fail.append('"including HST" contradicts the standing correction')
if c.count('<h1') != 1:
    fail.append('%d H1' % c.count('<h1'))
if 'CPA Ontario Membership 61040184' not in c:
    fail.append('no byline')
if any(ord(ch) > 0x2100 for ch in c):
    fail.append('non-ASCII symbol that may be an emoji')

links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', c))
if len(links) > 40:
    fail.append('%d outbound links, F9 cap is 40' % len(links))

m = re.search(r'<script type="application/ld\+json">(.*?)</script>', c, re.S)
json.loads(m.group(1))

if fail:
    print('GATE FAILED')
    for f in fail: print(' -', f)
    sys.exit(1)

print('gate clear')
print('  contents rows : 12, every row anchored to a real section')
print('  outbound      : %d distinct, cap 40' % len(links))
print('  question pages linked: %d of 10' % len([l for l in links if '/answers/' in l]))
print('  bytes         : %d' % len(c.encode()))
