"""Cross-batch gate for the whole of Family 9.

Each batch gate checks only its own manifest, so nothing until now compared a
new guide against the ones published before it. At 27 guides on closely
related topics that is the likeliest place for a real defect: a duplicate
heading, a recycled paragraph, two guides claiming the same meta description,
or a sibling link pointing at a guide that was renamed.

It also verifies the 6(g) link rules from the RENDERED pages rather than from
the registry, so the inbound count is measured on what will actually be
published.
"""
import json, re, sys, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFESTS = ['f9-manifest.json', 'f9-batch2-manifest.json',
             'f9-batch3-manifest.json', 'f9-batch4-manifest.json',
             'f9-batch5-manifest.json']
INBOUND_MIN = 12   # 6(g) line 1528
OUTBOUND_MAX = 40  # 6(g) line 1528

recs = []
for m in MANIFESTS:
    r = json.load(open(os.path.join(HERE, m), encoding='utf-8'))
    recs.extend(r if isinstance(r, list) else [r])

fail = []
slugs = [r['slug'] for r in recs]
if len(set(slugs)) != len(slugs):
    dupe = [s for s, n in collections.Counter(slugs).items() if n > 1]
    fail.append('duplicate slug across batches: %s' % dupe)

# Uniqueness of the things Google compares between pages.
for field in ('title', 'h1', 'meta_description'):
    seen = collections.defaultdict(list)
    for r in recs:
        seen[r[field]].append(r['slug'])
    for v, where in seen.items():
        if len(where) > 1:
            fail.append('identical %s on %s: %r' % (field, where, v[:70]))

# Section headings must be unique within a guide; the gate already checks that.
# Across guides, a heading repeated more than three times means two pages are
# covering the same ground under the same name.
heads = collections.defaultdict(list)
for r in recs:
    for t in r['toc']:
        heads[t].append(r['slug'])
for t, where in heads.items():
    if t == 'What the Fee Covers':
        continue  # appended to every guide by design
    if len(where) > 3:
        fail.append('heading %r on %d guides: %s' % (t, len(where), where))

# Recycled body copy. The four blocks the plan mandates verbatim are exempt.
MANDATED = ('A true nil return carries no percentage late-filing penalty',
            'A holding corporation with investment income',
            'Gondaliya CPA Professional Corporation is a registered EFILE',
            'Type your corporation name, pick your unfiled years',
            'The fee is $300.00 plus HST per tax year, covering one nil T2')
paras = collections.defaultdict(list)
for r in recs:
    for p in set(re.findall(r'<p>([^<]{120,})</p>', r['content'])):
        paras[p].append(r['slug'])
for p, where in paras.items():
    if any(p.startswith(m) for m in MANDATED):
        continue
    if len(where) > 2:
        fail.append('paragraph on %d guides (%s): %s...'
                    % (len(where), ','.join(where), p[:60]))

# Link integrity and the 6(g) counts, measured on the rendered pages.
inbound = collections.Counter()
for r in recs:
    links = set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"',
                           r['content']))
    if len(links) > OUTBOUND_MAX:
        fail.append('%s: %d outbound links, over the cap of %d'
                    % (r['slug'], len(links), OUTBOUND_MAX))
    for target in re.findall(
            r'href="https://corpnilfilingfor300\.ca/guides/([a-z0-9-]+)/"',
            r['content']):
        if target not in slugs:
            fail.append('%s links to /guides/%s/, which is not a built guide'
                        % (r['slug'], target))
        elif target != r['slug']:
            inbound[target] += 1
    if ('/guides/%s/' % r['slug']) in r['content'].replace(
            '"https://corpnilfilingfor300.ca/guides/%s/#' % r['slug'], ''):
        pass  # self-reference in schema only; not counted above

for s in slugs:
    if inbound[s] < INBOUND_MIN:
        fail.append('%s receives %d sibling inbound links, under the minimum of %d'
                    % (s, inbound[s], INBOUND_MIN))

if fail:
    print('CROSS-BATCH GATE FAILED (%d)' % len(fail))
    for f in fail:
        print(' -', f)
    sys.exit(1)

print('cross-batch gate clear on all %d guides' % len(recs))
print('inbound sibling links: min %d, max %d, against a minimum of %d'
      % (min(inbound[s] for s in slugs), max(inbound[s] for s in slugs),
         INBOUND_MIN))
print('outbound links: max %d, against a cap of %d'
      % (max(len(set(re.findall(r'href="(https://corpnilfilingfor300\.ca[^"]*)"',
                                r['content']))) for r in recs), OUTBOUND_MAX))
