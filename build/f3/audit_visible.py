"""Scan only the text a visitor actually sees, not the raw Elementor JSON.

Scanning the whole blob produces false positives: random element IDs contain
digit runs that look like review counts, and style keys contain words that look
like copy. This walks the tree and collects visible text and link targets only.
"""
import json,re,sys,glob,os

TEXT_KEYS=('title','title_text','description_text','editor','text','item_title','html','shortcode',
           'ekit_icon_box_title_text','ekit_icon_box_description_text','ekit_icon_box_btn_text',
           'ekit_icon_box_badge_title')

def visible(node,out,links):
    if isinstance(node,dict):
        st=node.get('settings')
        if isinstance(st,dict):
            for k,v in st.items():
                if isinstance(v,str) and v.strip() and k in TEXT_KEYS:
                    out.append(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',v)).strip())
                if isinstance(v,dict) and v.get('url'): links.append(v['url'])
        for v in (node.get('elements') or []): visible(v,out,links)
    elif isinstance(node,list):
        for v in node: visible(v,out,links)

BAN=[('CRA wording',r'CRA[- ](authorized|agent|approved|partner|endorsed)|authorized by CRA'),
     ('T183 alone',r'T183(?!CORP)'),
     ('no penalty alone',r'\bno penalty\b|penalty[- ]free|zero penalty'),
     ('guarantee',r'guarantee'),
     ('superlative',r'cheapest|lowest price|best price|unbeatable|fastest'),
     ('review or year count',r'\b\d{3,}\+|\b1300\b|5[- ]star|\b\d+\+ ?years'),
     ('booking CTA',r'book a call|schedule a meeting|free consultation|contact us to start'),
     ('emoji',r'[☀-➿\U0001F000-\U0001FAFF✅]')]
REQ=[('EFILE wording',r'[Rr]egistered EFILE electronic filer'),
     ('price',r'\$300\.00 plus HST'),('overflow price',r'\$350\.00 including HST'),
     ('not-nil scope',r'is not nil'),('CTA',r'Start Nil T2 Filing NOW'),
     ('local data value',r'PULL CORPORATION COUNT|T2 returns were assessed'),
     ('pull date caption',r'PULL DATE|Pulled ')]

fail=0
for f in sorted(glob.glob(sys.argv[1])):
    doc=json.load(open(f)); out=[];links=[]
    visible(doc.get('content',doc),out,links)
    blob=' || '.join(out)
    name=os.path.basename(f)
    probs=[n for n,p in BAN if re.search(p,blob,re.I)]
    miss=[n for n,p in REQ if not re.search(p,blob)]
    ext=[l for l in links if 'gondaliyacpa.ca' in l]
    if probs or miss or ext: fail+=1
    print(f'  {name:42s} {"FAIL" if (probs or miss or ext) else "OK  "} '
          f'{len(out):>3} strings  {"banned: "+",".join(probs) if probs else ""}'
          f'{"  missing: "+",".join(miss) if miss else ""}{"  ext: "+str(len(ext)) if ext else ""}')
print(f'\n{fail} failures')
