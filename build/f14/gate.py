"""Banned-phrase publish gate.

The October 7 deliverable's done-when: "a 10-URL dry run publishes clean and a
test page carrying a banned phrase is refused." This is the refusal.

Checks the Section 7.4 table plus the ten hard rules against the visible text of
a manifest record. Exits non-zero if any record fails, so a publisher can simply
refuse to run.
"""
import json, re, sys

BAN = [
 ('CRA wording',        r'CRA[- ](authorized|agent|approved|partner|endorsed)|authorized by CRA|approved by CRA|endorsed by CRA|agent of CRA'),
 ('T183 without CORP',  r'T183(?!CORP)'),
 ('guarantee',          r'guarantee'),
 ('superlative',        r'\bcheapest\b|lowest price|best price|unbeatable|\bfastest\b|risk[- ]free'),
 ('frozen count',       r'\b\d{3,}\+|\b1300\b|\b500\+|5[- ]star|\b\d+\+ ?years'),
 ('booking CTA',        r'book a call|schedule a meeting|free consultation|contact us to start'),
 ('EFILE number',       r'\bEFILE\s*(number|#)|\bGroupID\b'),
 ('emoji',              r'[☀-➿⬀-⯿\U0001F000-\U0001FAFF✅]'),
 ('old price form',     r'\$300\.00 including HST'),
]
# Rule 3: "no penalty" may appear only inside the full qualification block.
QUAL_ANCHOR = 'stays open forever'

def visible(html):
    t = re.sub(r'<style[^>]*>.*?</style>', ' ', html, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

def check(rec):
    blob = ' || '.join([rec.get('title',''), rec.get('meta_description',''), visible(rec.get('content',''))])
    fails = [n for n, p in BAN if re.search(p, blob, re.I)]
    # Rule 3, context-sensitive rather than a flat ban
    for m in re.finditer(r'no (?:percentage )?(?:late-filing )?penalty|penalty[- ]free|zero penalty', blob, re.I):
        window = blob[m.start(): m.start()+420]
        if QUAL_ANCHOR not in window:
            fails.append('penalty claim without the full qualification block'); break
    return fails

if __name__ == '__main__':
    recs = json.load(open(sys.argv[1]))
    bad = 0
    for r in recs:
        f = check(r)
        if f:
            bad += 1
            print(f'  REFUSED  {r["slug"]:46s} {", ".join(f)}')
    print(f'\n{len(recs)-bad} of {len(recs)} records pass the gate')
    if bad:
        print('PUBLISH REFUSED'); sys.exit(1)
    print('gate clear')
