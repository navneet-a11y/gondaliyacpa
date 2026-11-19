"""Section 6(k) pairwise similarity across the Family 1 templates.

Same measure the city hubs use: word tokens of the visible text only,
SequenceMatcher with autojunk off, run both ways and the larger taken.
Threshold 0.60.
"""
import json, glob, re, sys, os
from difflib import SequenceMatcher

TEXT = ('title','title_text','description_text','editor','text','item_title','html',
        'ekit_icon_box_title_text','ekit_icon_box_description_text',
        'ekit_heading_title','ekit_heading_extra_title')

def words(path):
    out = []
    def walk(n):
        if isinstance(n, dict):
            st = n.get('settings')
            if isinstance(st, dict):
                for k, v in st.items():
                    if isinstance(v, str) and k in TEXT:
                        out.append(re.sub(r'<[^>]+>', ' ', v))
                    if isinstance(v, list):
                        for it in v:
                            if isinstance(it, dict):
                                for k2, v2 in it.items():
                                    if isinstance(v2, str) and k2 in TEXT:
                                        out.append(re.sub(r'<[^>]+>', ' ', v2))
            for c in (n.get('elements') or []):
                walk(c)
        elif isinstance(n, list):
            for c in n:
                walk(c)
    d = json.load(open(path))
    walk(d.get('content', d))
    return re.findall(r"[A-Za-z0-9$%.,'-]+", ' '.join(out).lower())

files = sorted(glob.glob(sys.argv[1]))
names = [os.path.basename(f).replace('corpnil-vertical-', '').replace('.json', '') for f in files]
toks = [words(f) for f in files]
print(f'{"":34s}' + ''.join(f'{n[:13]:>15s}' for n in names[:-1]))
worst = 0.0
for i in range(1, len(files)):
    row = f'{names[i][:33]:34s}'
    for j in range(i):
        a = SequenceMatcher(None, toks[i], toks[j], autojunk=False).ratio()
        b = SequenceMatcher(None, toks[j], toks[i], autojunk=False).ratio()
        r = max(a, b); worst = max(worst, r)
        row += f'{r:>15.3f}'
    print(row)
print(f'\nhighest pair: {worst:.3f}   threshold 0.60   '
      f'{"PASS" if worst < 0.60 else "FAIL"}')
