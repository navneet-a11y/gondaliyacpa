"""F16 hub gate: line 1224 plus the hard rules.

Named hubs are checked; with no argument EVERY hub in this directory is.

It used to default to guides-hub.html alone, so running it reported "gate
clear" after a change to a different hub and checked nothing. That is the same
defect as the F4 gate importing one province: a check that covers one member of
a growing set stops being a check the moment the set grows, and says so in a
reassuring voice. Checking all of them by default is the fix.
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
# Hubs only. The blog hub's two part files are fragments, not pages, and have
# neither an H1 nor a schema block.
NAMES = sys.argv[1:] or sorted(
    os.path.basename(p) for p in glob.glob(os.path.join(HERE, '*-hub.html')))


def check(NAME):
  c = open(os.path.join(HERE, NAME), encoding='utf-8').read()
  low = c.lower(); fail = []

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
  # Hard rule 6 is about schema, so the check reads the page with comments
  # stripped. The /locations/ hub carries a CSS comment that says "hard rule 6
  # forbids FAQPage schema", and the plain substring test failed the page for
  # saying so. A banned type in a real ld+json block still fails: comments are
  # the only thing removed.
  _nc = re.sub(r'/\*.*?\*/', '', re.sub(r'<!--.*?-->', '', c, flags=re.S),
               flags=re.S)
  for bad in ['FAQPage','HowTo','aggregateRating','"Review"']:
      if bad in _nc: fail.append('banned schema %s' % bad)
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
    print('GATE FAILED on ' + NAME)
    for f in fail: print(' -', f)
    return False
  print('gate clear on %-20s %3d outbound, %6d bytes' % (NAME, len(links), len(c.encode())))
  return True


if __name__ == '__main__':
    ok = [check(n) for n in NAMES]
    print('%d of %d hubs clear' % (sum(ok), len(ok)))
    sys.exit(0 if all(ok) else 1)
