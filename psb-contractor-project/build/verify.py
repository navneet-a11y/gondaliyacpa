import sys, re, json, os, html
sys.path.insert(0, os.path.dirname(__file__))
from html.parser import HTMLParser
pkg, out = sys.argv[1], sys.argv[2]
class T(HTMLParser):
    def __init__(s): super().__init__(); s.t=[]; s.skip=0; s.links=[]
    def handle_starttag(s,tag,a):
        if tag in('script','style'): s.skip+=1
        if tag=='a': s.links.append(dict(a)['href'])
    def handle_endtag(s,tag):
        if tag in('script','style'): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.t.append(d)
def words(x): return re.findall(r"[\w$%.,’'&:;?!()/+-]+", x)
bad = 0
for sub in ('03-Pages','04-Posts'):
    for f in sorted(os.listdir(os.path.join(pkg,sub))):
        md = open(os.path.join(pkg,sub,f),encoding='utf-8').read()
        h = open(os.path.join(out,f.replace('.md','.html')),encoding='utf-8').read()
        p = T(); p.feed(h.replace('><','> <')); vis = ''.join(p.t)
        copy = re.search(r'^## (?:Page|Post) copy\s*$(.*?)(?=^## Calculator code|^## FAQs)', md, re.S|re.M).group(1)
        faqs = re.search(r'^## FAQs\s*$(.*?)(?=^## )', md, re.S|re.M).group(1)
        src = copy + faqs
        src = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', src)
        src = re.sub(r'^#{2,5}\s*(H[1-4]|Q):\s*', '', src, flags=re.M); src = re.sub(r'^H1:\s*','',src,flags=re.M)
        src = re.sub(r'\[(TRUSTINDEX|CALCULATOR) WIDGET\]','',src)
        src = re.sub(r'^\|[-| ]+\|\s*$','',src,flags=re.M).replace('|',' ').replace('**','')
        src = re.sub(r'^\s*([-*]|\d+\.)\s+','',src,flags=re.M)
        src = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'\1', src)
        a = words(src); v = words(vis.replace('Frequently asked questions',''))
        # drop calculator widget text + byline/review (added) from visible
        ok_seq = ' '.join(a) in ' '.join(v)
        # every source word sequence must appear in order
        import difflib
        sm = difflib.SequenceMatcher(None, a, v, autojunk=False)
        missing = [ ' '.join(a[i1:i2]) for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag in ('delete','replace')]
        ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1))
        faq = next(n for n in ld['@graph'] if n['@type']=='FAQPage')
        qa = re.findall(r'^#### Q:\s*(.+?)\s*\n(.*?)(?=^#### Q:|\Z)', faqs, re.S|re.M)
        faq_mismatch = []
        for (q,a_),e in zip(qa, faq['mainEntity']):
            a_txt = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', ' '.join(a_.split())).replace('**','')
            if q.strip()!=e['name'] or a_txt!=' '.join(e['acceptedAnswer']['text'].split()): faq_mismatch.append(q)
        if len(qa)!=len(faq['mainEntity']): faq_mismatch.append('COUNT %d vs %d'%(len(qa),len(faq['mainEntity'])))
        md_links = re.findall(r'\]\((https?://[^)]+)\)', copy+faqs)
        leftovers = re.findall(r'\*\*|\]\(|^#', vis, re.M)
        status = 'OK' if not missing and not faq_mismatch and not leftovers and sorted(md_links)==sorted(l for l in p.links) else 'CHECK'
        if status!='OK': bad+=1
        print(f[:7], status, 'missing:', missing[:3], 'faq_mismatch:', faq_mismatch[:3], 'links md/html:', len(md_links), len(p.links), 'leftovers:', len(leftovers))
print('files needing check:', bad)
