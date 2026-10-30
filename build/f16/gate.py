"""F16 hub gate: line 1224 plus the hard rules.

Takes the hub file as an argument and defaults to guides-hub.html, which is
what it was hardcoded to. It is run over tools-hub.html as well now that that
hub carries all sixty children.
"""
import json, re, sys
NAME = sys.argv[1] if len(sys.argv) > 1 else 'guides-hub.html'
c = open(NAME, encoding='utf-8').read(); low = c.lower(); fail = []

# line 1224 gate: live child count, never hand-typed, plus links to every child.
if '[cnf_child_count' not in c:
    fail.append('no live child count shortcode')
# The old form of this check looked for "<b>N</b> guides published", which is
# the reverse of the markup the hubs actually emit ("Guides published:
# <b>...</b>") and so could never have fired. It now reads the value inside
# the count line itself, whatever the label says.
for m in re.finditer(r'published:\s*<b>(.*?)</b>', c, re.S):
    if not m.group(1).strip().startswith('[cnf_child_count'):
        fail.append('child count is hand-typed (%r); line 1224 forbids it'
                    % m.group(1).strip()[:40])
if 'ei-cards' not in c:
    fail.append('no child list')

BANNED = ['complete list of every accountant','cra authorized','cra agent','cra approved',
          'cra partner','cra endorsed','guarantee','guaranteed','cheapest','best price',
          'unbeatable','fastest','instant filing','book a call','schedule a meeting',
          'free consultation','risk free','five-star','money-back','starting from']
for b in BANNED:
    if b in low: fail.append('banned phrase "%s"' % b)
for bad in ['FAQPage','HowTo','aggregateRating','"Review"']:
    if bad in c: fail.append('banned schema %s' % bad)
if re.search(r'T183(?!CORP)', c): fail.append('bare T183')
if 'including HST' in c: fail.append('"including HST" contradicts the standing correction')
if c.count('<h1') != 1: fail.append('%d H1' % c.count('<h1'))
if 'CPA Ontario Membership 61040184' not in c: fail.append('no byline')
if 'Last reviewed:' not in c: fail.append('no visible date')
# 7.9 line 1570: F16 takes its date in the footer, not under the H1.
body = c.split('</style>', 1)[1]
if body.index('Last reviewed:') < body.index('Also on This Site'):
    fail.append('date is not in the footer of the article body')
if any(ord(ch) > 0x2100 for ch in c): fail.append('possible emoji')
links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', c))
if len(links) > 400: fail.append('%d outbound, cap 400' % len(links))
json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', c, re.S).group(1))

if fail:
    print('GATE FAILED')
    for f in fail: print(' -', f)
    sys.exit(1)
print('gate clear on ' + NAME)
print('  child count   : live shortcode, not hand-typed')
print('  outbound      : %d distinct, cap 400' % len(links))
print('  bytes         : %d' % len(c.encode()))
