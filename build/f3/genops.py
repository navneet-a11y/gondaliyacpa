"""Generate wp_update_page_layout text ops for a city hub built from a sibling.

Element addresses are stable across the duplicate chain
(2533 -> 2564 -> 2570 -> ...). FAQ links are repointed to the Ontario service
pages at generation time, because the city's own Family 4 pages do not exist.
"""
import json, re, sys
city = sys.argv[1]
d = json.load(open(f'build/f3/corpnil-cityhub-{city}.json'))
def ws(n, o):
    if isinstance(n, dict):
        if n.get('elType') == 'widget': o.append(n)
        for v in (n.get('elements') or []): ws(v, o)
    elif isinstance(n, list):
        for v in n: ws(v, o)
W = []; ws(d['content'], W)
def by(t): return [w for w in W if w['widgetType'] == t]
head, te, ekh = by('heading'), by('text-editor'), by('elementskit-heading')
ib, eib, eicon, html = by('image-box'), by('elementskit-image-box'), by('elementskit-icon-box'), by('html')
faq = re.sub(rf'(https://corpnilfilingfor300\.ca/[a-z0-9-]+)-{city}/', r'\1-ontario/',
             html[0]['settings']['html'])
assert f'-{city}/' not in faq, 'a city URL survived in the FAQ'
ops = []
def sf(a, t, f): ops.append({"op": "set_fields", "element": a, "expect": t, "fields": f})
sf("14c1d495", "heading", {"title": head[0]['settings']['title']})
sf("101d95a5", "text-editor", {"editor": te[0]['settings']['editor']})
sf("7c0fac59", "elementskit-heading", {k: ekh[0]['settings'][k]
   for k in ("ekit_heading_title", "ekit_heading_extra_title")})
for a, i in (("76d90d59",1),("16bd95c5",2),("35f40f68",3)):
    sf(a, "heading", {"title": head[i]['settings']['title']})
for a, i in (("63cbe5d4",2),("61873591",3),("5900d5",4)):
    sf(a, "text-editor", {"editor": te[i]['settings']['editor']})
sf("7650232a", "heading", {"title": head[4]['settings']['title']})
sf("2534fd26", "text-editor", {"editor": te[5]['settings']['editor']})
sf("705798d8", "elementskit-heading", {"ekit_heading_title": ekh[1]['settings']['ekit_heading_title']})
for a, w in zip(["3be33c42","c81c89a","504678cb","6b770895","1857912f","3441d7dd",
                 "48dd9ca9","344e4603","4fe998e9","94aaf55","14b3ede","41777537"], eicon):
    sf(a, "elementskit-icon-box", {k: w['settings'][k]
       for k in ("ekit_icon_box_title_text", "ekit_icon_box_description_text")})
sf("72f101b0", "elementskit-heading", {"ekit_heading_title": ekh[2]['settings']['ekit_heading_title']})
for a, w in zip(["1d75cc4b","7071a965","2668c69c","4b77af1","6e2e6944","7864c61b"], eib):
    sf(a, "elementskit-image-box", {k: w['settings'][k]
       for k in ("ekit_image_box_title_text", "ekit_image_box_description_text")})
sf("303b6001", "text-editor", {"editor": te[6]['settings']['editor']})
sf("6b43d16b", "heading", {"title": head[5]['settings']['title']})
sf("72d9b7b2", "text-editor", {"editor": te[7]['settings']['editor']})
for a, w in zip(["1b52377a","8857d83","835f821","5d2ba2d2"], ib[1:5]):
    sf(a, "image-box", {k: w['settings'][k] for k in ("title_text", "description_text")})
sf("10ba29f5", "text-editor", {"editor": te[8]['settings']['editor']})
sf("54a884ce", "heading", {"title": head[6]['settings']['title']})
sf("113094d1", "text-editor", {"editor": te[9]['settings']['editor']})
sf("9111b25", "heading", {"title": head[9]['settings']['title']})
sf("f487f53", "html", {"html": faq})
sf("2392e0ac", "heading", {"title": head[8]['settings']['title']})
assert len(ops) <= 50, f'{len(ops)} ops exceeds the per-call cap of 50'
json.dump(ops, sys.stdout, ensure_ascii=False, separators=(',', ':'))
sys.stderr.write(f'{city}: {len(ops)} ops\n')
