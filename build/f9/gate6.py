"""F9 batch 6 gate: gate3.py run unchanged over guides 28 to 30.

Identical checks, so the three new guides are held to exactly the bar the
twenty-seven already published were held to. Only the manifest filename differs.
"""
import json, re, sys, itertools

recs = json.load(open('f9-batch6-manifest.json'))
fail = []
DATES = set()

BANNED_EXTRA = ['2026', '2027']

for rec in recs:
    s = rec['slug']
    c = rec['content']; low = c.lower()


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
        fail.append(s + ': ' + 'no visible update date')
    toc = re.search(r'<div class="ei-toc">.*?</ol>', c, re.S)
    if not toc:
        fail.append(s + ': ' + 'no contents block')
    else:
        n = toc.group(0).count('<li>')
        if n != 12:
            fail.append(s + ': ' + 'contents block has %d rows, the gate requires 12' % n)
        for k, _t in [(m, m) for m in re.findall(r'href="#([a-z0-9-]+)"', toc.group(0))]:
            if ('id="%s"' % k) not in c:
                fail.append(s + ': ' + 'contents row links to #%s with no matching section' % k)

    # hard rules
    if re.search(r'T183(?!CORP)', c):
        fail.append(s + ': ' + 'bare T183')
    if 'penalty' in low and 'A true nil return carries no percentage late-filing penalty' not in c:
        fail.append(s + ': ' + 'penalty without the 7.4 qualification block')
    if 'registered EFILE electronic filer' not in c:
        fail.append(s + ': ' + 'missing the approved EFILE phrasing')
    if 'Returns are prepared and transmitted in Canada' not in c:
        fail.append(s + ': ' + 'F9 pillars need the three-sentence EFILE block')
    # 7.6 conflict: the banned list bans "backdate" while required qualification 7
    # requires "never backdated". Permit only the negated, compliant form.
    for m in re.finditer(r'backdat\w*', low):
        if not low[max(0, m.start()-6):m.start()].endswith('never '):
            fail.append(s + ': ' + '"%s" not in the required "never backdated" form' % m.group(0))

    for b in BANNED:
        if b in low:
            fail.append(s + ': ' + 'banned phrase "%s"' % b.strip())
    for bad in ['FAQPage', 'HowTo', 'aggregateRating', '"Review"']:
        if bad in c:
            fail.append(s + ': ' + 'banned schema %s' % bad)
    if re.search(r'\b(500\+|1300\+|600\+|\d+\+ (reviews|clients))', low):
        fail.append(s + ': ' + 'count claim, banned until the claim audit closes')
    if 'including HST' in c:
        fail.append(s + ': ' + '"including HST" contradicts the standing correction')
    if c.count('<h1') != 1:
        fail.append(s + ': ' + '%d H1' % c.count('<h1'))
    if 'CPA Ontario Membership 61040184' not in c:
        fail.append(s + ': ' + 'no byline')
    if any(ord(ch) > 0x2100 for ch in c):
        fail.append(s + ': ' + 'non-ASCII symbol that may be an emoji')

    links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', c))
    if len(links) > 40:
        fail.append(s + ': ' + '%d outbound links, F9 cap is 40' % len(links))

    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', c, re.S)
    json.loads(m.group(1))


    # 6(a) line 1147 and the 6(k) year-stamp rule: no year token in a guide URL.
    for y in BANNED_EXTRA:
        if y in s:
            fail.append(s + ': year token "%s" in the slug' % y)

    # the 12 contents rows must be distinct
    toc2 = re.search(r'<div class="ei-toc">.*?</ol>', c, re.S)
    rows = re.findall(r'<li><a href="#[a-z0-9-]+">([^<]+)</a></li>', toc2.group(0))
    if len(set(rows)) != 12:
        fail.append(s + ': %d distinct contents rows of %d' % (len(set(rows)), len(rows)))

    # Article schema, not WebPage (line 1487)
    if '"@type": "Article"' not in c:
        fail.append(s + ': no Article schema')

    # the three-sentence EFILE block and the byline live in the hero/intro
    # The review date is read from the batch rather than hardcoded, so this gate
    # works for any batch. Every guide in one batch must carry the same date.
    m_date = re.search(r'Last reviewed: ([A-Z][a-z]+ \d{1,2}, \d{4})', c)
    if not m_date:
        fail.append(s + ': no review date')
    else:
        DATES.add(m_date.group(1))

# Cross-guide duplication: no TOPICAL body paragraph may appear on more than two
# guides. The plan requires four blocks verbatim on every Family 9 pillar, so
# those are exempt rather than flagged:
#   7.4            the three-sentence EFILE block
#   hard rule 3    the late-filing qualification
#   7.6            the nil-status rule
#   shared         the bottom CTA copy
MANDATED = ('A true nil return carries no percentage late-filing penalty',
            'A holding corporation with investment income',
            'Gondaliya CPA Professional Corporation is a registered EFILE',
            'Type your corporation name, pick your unfiled years')
paras = {}
for rec in recs:
    for p in set(re.findall(r'<p>([^<]{120,})</p>', rec['content'])):
        paras.setdefault(p, []).append(rec['slug'])
for p, where in paras.items():
    if any(p.startswith(m) for m in MANDATED):
        continue
    if len(where) > 2:
        fail.append('paragraph repeated on %d guides: %s...' % (len(where), p[:60]))

if len(DATES) > 1:
    fail.append('batch carries mixed review dates: %s'
                % ', '.join(sorted(DATES)))

if fail:
    print('GATE FAILED')
    for f in fail:
        print(' -', f)
    sys.exit(1)

print('gate clear on all %d guides' % len(recs))
for rec in recs:
    c = rec['content']
    links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"', c))
    print('  %-44s %2d rows  out:%2d  answers:%d  guides:%d  %6d bytes'
          % (rec['slug'][:44], len(rec['toc']), len(links),
             len([l for l in links if '/answers/' in l]),
             len([l for l in links if '/guides/' in l]), len(c.encode())))


# Added after a near-miss on the Schedule 8 guide: internal references to the
# plan document must never reach public copy.
INTERNAL = [r'\bthe plan\b', r'appendix a', r'6\([a-k]\)', r'line 1[0-9]{3}',
            r'decisions\.md', r'Sharad Gondaliya should', r'pending his sign-off']
leaks = []
for rec in recs:
    for pat in INTERNAL:
        for m in re.finditer(pat, rec['content'], re.I):
            leaks.append('%s: internal reference "%s"' % (rec['slug'], m.group(0)))
if leaks:
    print('INTERNAL REFERENCE CHECK FAILED')
    for l in leaks:
        print(' -', l)
    raise SystemExit(1)
print('no internal references in public copy')
