"""Family 3 city-hub Elementor template generator.

Composes a city hub from the already-cleaned Services sections so every place
page shares one design system. Usage:
    python3 build_cityhub.py <out-334.json> <outdir> [city_slug ...]

The plan's hard gate for this family, 6(c) line 1211:
  "No city hub publishes without a named repeatable local data source and a
   current data value." and "Data value carries its pull date in the visible
   caption."
So the corporation count and its pull date are required. Until a real value is
pulled from the Corporations Canada open-data bulk file, the generator writes a
loud placeholder that cannot be mistaken for a number.
"""
import json, copy, random, sys, os

SRC, OUTDIR = sys.argv[1], sys.argv[2]
WANT = sys.argv[3:] or None
src = json.load(open(SRC))
os.makedirs(OUTDIR, exist_ok=True)

FORM  = 'https://corpnilfilingfor300.ca/form/'
PRICE = 'https://corpnilfilingfor300.ca/pricing/'
CTA   = 'Start Nil T2 Filing NOW'
NEEDS_DATA = '[[PULL CORPORATION COUNT]]'
NEEDS_DATE = '[[PULL DATE]]'

# 6(k): 12 cities pass the local-data test; 3 fail and are replaced by
# jurisdiction hubs carrying CRA T2 assessment counts the plan supplies.
PLACES = [
 # slug, display name, kind, jurisdiction note key, supplied data value
 ('toronto','Toronto','city','on',None),
 ('mississauga','Mississauga','city','on',None),
 ('brampton','Brampton','city','on',None),
 ('markham','Markham','city','on',None),
 ('vaughan','Vaughan','city','on',None),
 ('richmond-hill','Richmond Hill','city','on',None),
 ('oakville','Oakville','city','on',None),
 ('ottawa','Ottawa','city','on',None),
 ('oshawa','Oshawa','city','on',None),
 ('guelph','Guelph','city','on',None),
 ('hamilton','Hamilton','city','on',None),
 ('windsor','Windsor','city','on',None),
 ('ontario','Ontario','jurisdiction','on','1,108,730'),
 ('alberta','Alberta','jurisdiction','ab','365,890'),
 ('british-columbia','British Columbia','jurisdiction','bc','413,630'),
]

# 12 Family 4 service slugs. Note the cost slug carries "in": the plan calls
# this out explicitly so it does not render a double hyphen.
SERVICES = [
 ('nil-t2-filing-{p}','Nil T2 Filing','A T2 return for a corporation with no activity in the tax year, CPA reviewed and transmitted electronically.'),
 ('catch-up-nil-t2-filing-{p}','Catch-Up Nil T2 Filing','Several unfiled nil years filed together, oldest year first.'),
 ('dormant-corporation-filing-{p}','Dormant Corporation Filing','For a corporation that has stopped trading but has not been dissolved.'),
 ('final-t2-before-dissolution-{p}','Final T2 Before Dissolution','The last return for a corporation being wound up, due within six months of dissolution.'),
 ('t2-short-filing-{p}','T2 Short Filing','The two-page T2 Short return, where every CRA condition for using it is met.'),
 ('nil-t2-filing-cost-in-{p}','Nil T2 Filing Cost','What the $300.00 plus HST fee covers and what it does not.'),
 ('unfiled-corporate-tax-returns-{p}','Unfiled Corporate Tax Returns','Returns for years already past their due date. An unfiled year stays open until it is filed.'),
 ('no-activity-corporation-tax-return-{p}','No Activity Corporation Tax Return','No revenue, no bank activity and no employees. The filing obligation still applies.'),
 ('numbered-corporation-nil-filing-{p}','Numbered Corporation Nil Filing','For a numbered corporation that was incorporated and never traded, or has gone quiet.'),
 ('inactive-holding-corporation-t2-filing-{p}','Inactive Holding Corporation T2 Filing','A holding corporation with investment income, rental income or dividends paid or received is not nil.'),
 ('nil-t2-filing-deadline-{p}','Nil T2 Filing Deadline','Due within six months of the fiscal year-end, every year, until the corporation is dissolved.'),
 ('nil-t2-filing-for-non-resident-owned-corporations-{p}','Non-Resident Owned Corporations','Nil filing where the shareholders are outside Canada.'),
]

# Rule 8: Alberta states AT1, Quebec states CO-17, both as separate returns.
JNOTE = {
 'on': ('The Ontario annual return is separate',
        'A nil T2 does not cover your Ontario annual return through the Ontario Business Registry. We tell you if you still owe one.'),
 'ab': ('The Alberta AT1 is a separate return',
        'Alberta AT1 is a separate provincial return and is not included in the $300.00 plus HST fee. We tell you if you still owe one.'),
 'bc': ('Your provincial filing is separate',
        'A nil T2 does not cover a provincial annual report. We tell you which filings you still owe.'),
 'qc': ('The Quebec CO-17 is a separate return',
        'Quebec CO-17 is a separate provincial return and is not included in the $300.00 plus HST fee. We tell you if you still owe one.'),
}

def widgets(sec):
    out=[]
    def w(n):
        if isinstance(n,dict):
            if n.get('elType')=='widget': out.append(n)
            if 'elements' in n: w(n['elements'])
        elif isinstance(n,list):
            for v in n: w(v)
    w(sec); return out
def reid(n):
    if isinstance(n,dict):
        if isinstance(n.get('id'),str): n['id']='%08x'%random.randrange(16**8)
        for v in n.values(): reid(v)
    elif isinstance(n,list):
        for v in n: reid(v)
def setlink(w,url):
    s=w['settings']
    for k in ('link','button_link','ekit_icon_box_global_link','ekit_icon_box_btn_url'):
        if isinstance(s.get(k),dict):
            s[k]=dict(s[k]); s[k]['url']=url; s[k]['is_external']=''; s[k]['nofollow']=''
    if not any(isinstance(s.get(k),dict) for k in ('link','button_link')) and w['widgetType']=='button':
        s['link']={'url':url,'is_external':'','nofollow':'','custom_attributes':''}
def P(*p): return ''.join('<p>%s</p>'%x for x in p)

def build(slug,name,kind,jkey,supplied):
    jt,jb = JNOTE[jkey]
    if supplied:
        datum = (f'{supplied} T2 returns were assessed by the Canada Revenue Agency for corporations in {name}.')
        source = ('Source: CRA corporation income tax statistics, refreshed when the annual table is reissued, '
                  f'plus the Corporations Canada open-data bulk file filtered by province. Pulled {NEEDS_DATE}.')
    else:
        datum = (f'{NEEDS_DATA} active federal corporations have a registered office in {name}.')
        source = ('Source: Corporations Canada open-data bulk file, registered-office city field. '
                  f'Pulled {NEEDS_DATE}, refreshed monthly.')

    PLAN=[
     (0,[('title',f'Nil T2 Filing in {name}'),
         ('editor',P(f'Nil T2 filing for {name} corporations. One price for every year and every province, with no hourly billing and no add-on fees.')),
         ('title_text','$300.00'),('description_text','plus HST per tax year'),
         ('editor',P('Registered EFILE electronic filer. Your CRA confirmation is emailed within 3 business days.')),
         ('text',CTA),('text','See the price')],{4:FORM,5:PRICE}),
     (4,[('title',f'Corporations in {name}')],{}),
     (5,[('editor',P(datum, source))],{}),
     (6,[('title_text','CPA Ontario registered firm, Firm Registration 61330051'),
         ('title_text','Registered EFILE electronic filer'),
         ('title_text','CRA confirmation within 3 business days'),
         ('title_text','$300.00 plus HST per tax year')],{}),
     (9,[('title',f'Nil T2 filing services in {name}')],{}),
     (10,None,{}),
     (7,[('title',jt),('editor',P(jb)),
         ('title','The federal annual return is separate'),
         ('editor',P('A federal Corporations Canada annual return costs $12.00 and is due within 60 days of your anniversary. It is a government fee and HST does not apply to it.')),
         ('title','Prepared and transmitted in Canada'),
         ('editor',P('Our credentials are never shared and no part of your file is sent offshore.'))],{}),
     (12,[('editor',P('One price, stated in full before you pay')),
          ('title',f'What {name} corporations pay'),
          ('text',CTA),('text','See the price'),
          ('editor',P('$300.00 per tax year, plus $39.00 HST, so $339.00 in total per tax year. Each tax year is a separate return and carries the same fee.'))],{2:FORM,3:PRICE}),
     (14,[('title','If your corporation is not nil')],{}),
     (15,[('editor',P('This service is for a corporation with no activity in the tax year. A corporation with investment income, rental income, or dividends paid or received is not nil.',
          'If your corporation is not nil, we move your file to gondaliyacpa.ca at $350.00 including HST per tax year and tell you before any further charge.'))],{}),
     (16,[('title',f'File your {name} nil T2 return'),('text',CTA),('text','See the price')],{1:FORM,2:PRICE}),
    ]

    out=[]
    for idx,fields,links in PLAN:
        sec=copy.deepcopy(src[idx]); reid(sec); ws=widgets(sec)
        if fields:
            q=list(fields)
            for w in ws:
                s=w['settings']
                while q:
                    k,v=q[0]
                    if k in s:
                        s[k]=v; q.pop(0)
                        if q and q[0][0] in s and q[0][0]!=k:
                            s[q[0][0]]=q[0][1]; q.pop(0)
                        break
                    else: break
        if idx==10:
            boxes=[w for w in ws if w['widgetType']=='elementskit-icon-box']
            for n,w in enumerate(boxes):
                if n>=len(SERVICES): continue
                pat,t,d=SERVICES[n]; s=w['settings']
                s['ekit_icon_box_title_text']=f'{t} in {name}' if n==0 else t
                s['ekit_icon_box_description_text']=d
                if 'ekit_icon_box_badge_title' in s: s['ekit_icon_box_badge_title']=''
                if 'ekit_icon_box_btn_text' in s: s['ekit_icon_box_btn_text']=CTA
                setlink(w,f'https://corpnilfilingfor300.ca/{pat.format(p=slug)}/')
        for pos,url in links.items():
            if pos<len(ws): setlink(ws[pos],url)
        out.append(sec)
    return out

made=[]
for slug,name,kind,jkey,supplied in PLACES:
    if WANT and slug not in WANT: continue
    content=build(slug,name,kind,jkey,supplied)
    tpl={'version':'0.4','title':f'CorpNil City Hub — {name}','type':'page',
         'content':content,'page_settings':[]}
    path=os.path.join(OUTDIR,f'corpnil-cityhub-{slug}.json')
    json.dump(tpl,open(path,'w'),ensure_ascii=False,separators=(',',':'))
    made.append((slug,name,kind,os.path.getsize(path),supplied is not None))
for slug,name,kind,size,hasdata in made:
    print(f'  {name:18s} {kind:12s} {size:>7,} b  data: {"supplied" if hasdata else "TO PULL"}')
print(f'{len(made)} templates written to {OUTDIR}')
