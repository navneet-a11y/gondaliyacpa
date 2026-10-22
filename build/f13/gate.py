# -*- coding: utf-8 -*-
"""Hard-rule and Section 7.6 gate for Family 13 posts."""
import sys, re, html as H
sys.path.insert(0, '.')
import post1, post2
from posts import QUAL

POSTS = [post1, post2]
fail = []

BANNED = ['cra authorized', 'authorized by cra', 'cra agent', 'agent of cra',
 'cra approved', 'approved by cra', 'cra partner', 'cra endorsed', 'endorsed by cra',
 'guaranteed', 'guarantee', 'cheapest', 'lowest price in canada', 'best price',
 'unbeatable', 'fastest', 'instant filing', 'same-day filing', 'filed in minutes',
 'book a call', 'schedule a meeting', 'free consultation', 'risk free', 'risk-free',
 'audit proof', 'backdate', 'conservatively', 'easily', 'simply', ' just ',
 'e.g.', 'such as', 'including hst']

for m in POSTS:
    c = m.HTML
    low = c.lower()
    sid = m.SLUG
    def bad(s): fail.append('%s: %s' % (sid, s))

    body = c.split('</style>', 1)[1].split('<script', 1)[0]
    text = H.unescape(re.sub(r'<[^>]+>', ' ', body))
    words = len(text.split())

    # --- 7.6 shape ---
    if not (900 <= words <= 1400): bad('word count %d outside 900-1400' % words)
    lead = re.search(r'<p class="cnf-lead">(.*?)</p>', c, re.S)
    if not lead: bad('no answer-first lead paragraph')
    else:
        lw = len(H.unescape(re.sub(r'<[^>]+>', ' ', lead.group(1))).split())
        if lw > 40: bad('lead is %d words, over 40' % lw)
    if c.count('<h1') != 0: bad('content carries an h1; the theme renders the title')
    if c.count('<h2') < 4: bad('only %d h2 headings' % c.count('<h2'))

    # --- 1221 one original table or checklist ---
    if c.count('<table') < 1 and 'cnf-check"' not in c:
        bad('no original table and no original checklist')
    for t in re.findall(r'<table.*?</table>', c, re.S):
        if 'Notes</th>' not in t: bad('a table has no Notes column')
        if re.search(r'<td>[^<]*\bto\b[^<]*\d', t): bad('a table cell looks like a range')

    # --- 1771 six internal links, and no external links ---
    hrefs = re.findall(r'href="([^"]+)"', body)
    internal = [h for h in hrefs if h.startswith('https://corpnilfilingfor300.ca')]
    external = [h for h in hrefs if not h.startswith('https://corpnilfilingfor300.ca')]
    if len(internal) < 6: bad('only %d internal links, 6 required' % len(internal))
    if external: bad('external link(s): %s' % external)

    # --- hard rules ---
    for b in BANNED:
        if b in low: bad('banned phrase "%s"' % b.strip())
    if re.search(r'\bT183\b(?!CORP)', c): bad('bare T183')
    if 'efile number' in low or 'groupid' in low: bad('rule 5 EFILE number or GroupID')
    for s in ('faqpage', 'howto', 'aggregaterating', '"review":'):
        if s in low: bad('rule 6 schema "%s"' % s)
    if re.search(r'\d+\+?\s*(5-star|reviews|clients|years in practice)', low):
        bad('a review, client or years count')
    if '$300.00 plus HST' not in c: bad('price string missing')

    # --- 1590 penalty pairing, both ways ---
    has_pen = 'penalt' in low
    has_qual = QUAL in H.unescape(c)
    if has_pen and not has_qual: bad('mentions a penalty without the 1590 sentence')
    if has_qual and not has_pen: bad('carries the 1590 sentence with no penalty')

    # --- 7.5 byline and date ---
    if 'Written by' not in c: bad('no Written by line')
    if 'CPA Ontario Membership 61040184' not in c: bad('no reviewer line')
    if 'Last reviewed:' not in c: bad('no Last reviewed line')

    nb = sorted({ch for ch in c if ord(ch) > 127})
    if nb: bad('non-ascii %r' % nb)

    print('%-48s %4d words  %d table  %d internal links  qual=%s'
          % (sid, words, c.count('<table'), len(internal), has_qual))

if len({m.SLUG for m in POSTS}) != len(POSTS): fail.append('duplicate slug')
if len({m.TITLE for m in POSTS}) != len(POSTS): fail.append('duplicate title')
for m in POSTS:
    if len(m.DESC) > 160: fail.append('%s: meta %d chars' % (m.SLUG, len(m.DESC)))

print()
if fail:
    print('GATE FAIL'); [print('  ' + f) for f in fail]; raise SystemExit(1)
print('gate clear on %d posts' % len(POSTS))
