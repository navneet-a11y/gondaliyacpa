"""Hard-rule gate for the Family 7 comparison pages.

Carries the hard rules every family gate carries, plus the three that are
specific to F7:

  line 1215  two published price cells and eight published feature cells, every
             one filled, and no negative claim
  line 1568  a dated price-checked line above the comparison table
  line 1529  20 outbound links at most, and any external competitor link
             nofollow

It also refuses the eight things taken out of the supplied design, so a later
page cannot quietly put them back: FAQPage schema, a booking call to action, a
guarantee, a review count, including-HST wording, the sister office's phone
number, and a missing byline or review stamp.
"""
import io, re, sys

NAME = sys.argv[1] if len(sys.argv) > 1 else 't2-short-vs-full-t2.html'
c = io.open(NAME, encoding='utf-8').read()
low = c.lower()
fail = []


def bad(m):
    fail.append(m)


# ---- rule 1, CRA wording -------------------------------------------------
low1 = low.replace('authorized signing officer', '')
for w in ('cra authorized', 'authorized by cra', 'cra agent', 'cra approved',
          'cra partner', 'cra endorsed', 'endorsed by the cra', 'cra logo'):
    if w in low1:
        bad('rule 1 banned CRA wording "%s"' % w)
if re.search(r'\bauthorized\b', low1):
    bad('rule 1 stray "authorized"')
for m in re.finditer(r'EFILE', c):
    if not c.startswith('EFILE electronic filer', m.start()):
        bad('rule 1 EFILE outside the approved phrase')
        break
# ---- rule 2, T183CORP ----------------------------------------------------
if re.search(r'\bT183\b(?!CORP)', c):
    bad('rule 2 bare T183')
# ---- rule 3, penalty claims ----------------------------------------------
for m in re.finditer(r'(no penalty|penalty[- ]free|zero penalty)', low):
    bad('rule 3 unqualified penalty phrase "%s"' % m.group(1))
if 'no percentage late-filing penalty' in low and \
        'stays open forever' not in low:
    bad('rule 3 qualification sentence incomplete')
# ---- rule 4 and Rule 217, superlatives and negative claims ---------------
# "better than" is the plan's own example of the banned F7 phrasing.
for w in ('cheapest', 'lowest price', 'best price', 'unbeatable', 'better than',
          'worse than', 'guaranteed', 'guarantee', 'money-back', 'risk-free',
          'risk free', 'fastest', 'instant filing', 'five-star', 'five star',
          'outperform', 'beats ', 'inferior', 'overpriced'):
    if w in low:
        bad('rule 4 or Rule 217 banned claim "%s"' % w)
if re.search(r'\d[\d,+]*\s*(five|5)[- ]star', low) or 'reviews' in low:
    bad('rule 6 review claim in prose')
# ---- rule 5, EFILE number and GroupID ------------------------------------
if re.search(r'efile\s*(number|#|no\.)', low) or 'groupid' in low:
    bad('rule 5 EFILE number or GroupID')
# ---- rule 6, forbidden schema --------------------------------------------
for w in ('faqpage', 'howto', 'aggregaterating', '"review"', 'trustindex'):
    if w in low:
        bad('rule 6 forbidden schema or widget "%s"' % w)
# ---- rule 7, no booking --------------------------------------------------
for w in ('book a call', 'book free', 'book a free', 'schedule a meeting',
          'free consultation', 'calendly', 'consultation/'):
    if w in low:
        bad('rule 7 booking or consultation call to action "%s"' % w)
# ---- rule 9, price wording -----------------------------------------------
if 'including HST' in c:
    bad('rule 9 "including HST" contradicts the standing correction')
if '$300.00 plus HST per tax year' not in c:
    bad('rule 9 price string missing')
for m in re.finditer(r'\$(\d{1,3}(?:,\d{3})*\.\d\d)', c):
    if m.group(1) not in ('300.00', '350.00'):
        bad('unexpected money figure $%s' % m.group(1))
# ---- 7.5, byline and stamp ----------------------------------------------
if 'CPA Ontario Membership 61040184' not in c:
    bad('7.5 rule 3 byline missing')
if 'Last reviewed:' not in c:
    bad('7.5 rule 1 review date missing')
if not re.search(r'class="si-stamp">Prices checked [A-Z][a-z]+ \d{1,2}, \d{4}',
                 c):
    bad('line 1568 dated price-checked line missing')
_body = re.sub(r'<script.*?</script>', '', c, flags=re.S)
if _body.index('Prices checked') > _body.index('<table class="si-tbl"'):
    bad('line 1568 price line is not above the comparison table')

# ---- line 1215, the publish gate ----------------------------------------
_tbl = re.search(r'<table class="si-tbl".*?</table>', _body, re.S)
if not _tbl:
    bad('line 1215 no comparison table')
else:
    rows = re.findall(r'<tr>(?!<th)|<tr class="si-hl">', _tbl.group(0))
    body_rows = re.findall(r'<tr[^>]*>(?:\s*<td>.*?</td>\s*)+</tr>',
                           _tbl.group(0), re.S)
    if len(body_rows) != 10:
        bad('line 1215 expected 2 price rows plus 8 feature rows, found %d'
            % len(body_rows))
    for r in body_rows:
        cells = re.findall(r'<td>(.*?)</td>', r, re.S)
        if len(cells) != 3:
            bad('a comparison row has %d cells, not 3' % len(cells))
        if any(not x.strip() for x in cells):
            bad('line 1215 an empty cell in the comparison table')
    if _tbl.group(0).count('<th scope="col">') != 3:
        bad('the comparison table has no three-column header')

# ---- line 1529, links ----------------------------------------------------
inbound_targets = (c.count('/pricing/nil-t2-filing-cost/'),
                   c.count('corpnilfilingfor300.ca/">'))
if '/pricing/nil-t2-filing-cost/' not in c:
    bad('line 1529 no link up to the cost page')
if 'corpnilfilingfor300.ca/">' not in c:
    bad('line 1529 no link up to the home page')
outbound = len(re.findall(r'href="https://corpnilfilingfor300\.ca', c))
if outbound > 20:
    bad('line 1529 outbound cap exceeded: %d' % outbound)
for m in re.finditer(r'<a [^>]*href="https?://(?!corpnilfilingfor300\.ca)'
                     r'([^"/]+)', c):
    tag = c[m.start():c.index('>', m.start())]
    if 'nofollow' not in tag:
        bad('line 1529 external link to %s is not nofollow' % m.group(1))
if 'gondaliyacpa.ca/consultation' in low:
    bad('rule 7 link to the consultation page')
if '+1647' in c or '647-212' in c or '6472129559' in c:
    bad('the sister office phone number is on the page')
# the required disclosure
if 'published prices and published features only' not in c:
    bad('line 1215 required disclosure missing')

# ---- structure and hygiene ----------------------------------------------
if c.count('<h1') != 1:
    bad('h1 count %d' % c.count('<h1'))
if '<details>' not in c:
    bad('the FAQ is not built on details, so it needs JavaScript to open')
if c.count('<details>') != 35:
    bad('%d FAQ items, expected 35' % c.count('<details>'))
if 'si-answer' not in c:
    bad('no answer card')
if 'si-cta-bottom' not in c:
    bad('no closing call to action')
if '"@type": "WebPage"' not in c or '"@type": "BreadcrumbList"' not in c:
    bad('schema is not the site pattern: WebPage plus BreadcrumbList')
nb = sorted({ch for ch in c if ord(ch) > 127})
if nb:
    bad('non-ascii %r' % nb)
if '  ' in re.sub(r'<[^>]+>', '', _body):
    bad('double space in body text')

if fail:
    print('GATE FAILED')
    for f in fail:
        print(' -', f)
    raise SystemExit(1)
print('gate clear on ' + NAME)
print('  comparison rows : 2 price + 8 feature, every cell filled')
print('  outbound        : %d links to %d distinct URLs, cap 20'
      % (outbound, len(set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', c)))))
print('  bytes           : %d' % len(c.encode()))
