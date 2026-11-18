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
# An Elementor page export is {"content": [...], "title": ..., ...}; an earlier
# source was saved as the bare section list. Accept either.
if isinstance(src, dict):
    src = src['content']
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
 ('nil-t2-filing-cost-in-{p}','Nil T2 Filing Cost','What the $300.00 fee covers and what it does not.'),
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
        'Alberta AT1 is a separate provincial return and is not included in the $300.00 plus applicable sales tax fee. We tell you if you still owe one.'),
 'bc': ('Your provincial filing is separate',
        'A nil T2 does not cover a provincial annual report. We tell you which filings you still owe.'),
 'qc': ('The Quebec CO-17 is a separate return',
        'Quebec CO-17 is a separate provincial return and is not included in the $300.00 plus applicable sales tax fee. We tell you if you still owe one.'),
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

# The supplied template is a gondaliyacpa.ca page, so it carries that domain's
# assets and links: a hero background, decorative staff photos behind the
# service cards, and two trust cells linking to a money-back guarantee and a
# fee-matching policy. The guarantee links breach hard rule 4 on their own, and
# every one of them is a cross-domain dependency on a page that has to stand by
# itself. This strips all of them and puts this site's own hero image back.
HERO_IMG = ('https://corpnilfilingfor300.ca/wp-content/uploads/2026/09/'
            'business-executives-having-meeting_1098-18316.jpg')


def desource(n, hero_done=[False]):
    """Remove every gondaliyacpa.ca asset and link target from a section."""
    if isinstance(n, dict):
        st = n.get('settings')
        if isinstance(st, dict):
            for k, v in list(st.items()):
                if isinstance(v, dict) and isinstance(v.get('url'), str) \
                        and 'gondaliyacpa.ca' in v['url']:
                    if k == 'background_image' and not hero_done[0]:
                        v['url'] = HERO_IMG
                        v.pop('id', None)
                        hero_done[0] = True
                    else:
                        v['url'] = ''
                        v.pop('id', None)
        for v in (n.get('elements') or []):
            desource(v)
    elif isinstance(n, list):
        for v in n:
            desource(v)

def build(slug,name,kind,jkey,supplied):
    jt,jb = JNOTE[jkey]  # jt unused in this map; the shell has one heading
    if supplied:
        datum = (f'{supplied} T2 returns were assessed by the Canada Revenue Agency for corporations in {name}.')
        source = ('Source: CRA corporation income tax statistics, refreshed when the annual table is reissued, '
                  f'plus the Corporations Canada open-data bulk file filtered by province. Pulled {NEEDS_DATE}.')
    else:
        datum = (f'{NEEDS_DATA} active federal corporations have a registered office in {name}.')
        source = ('Source: Corporations Canada open-data bulk file, registered-office city field. '
                  f'Pulled {NEEDS_DATE}, refreshed monthly.')

    # SECTION MAP FOR THE SUPPLIED TEMPLATE, 2026-11-18.
    #
    # The previous map (sections 0,4,5,6,7,9,10,12,14,15,16) was written for an
    # export that is not in this repository. Run against the template Navneet
    # supplied it filled only section 0 and left every other section reading
    # "Mississauga", so it is replaced rather than kept.
    #
    # Only sections that can be made compliant are used. The supplied file is a
    # gondaliyacpa.ca full-service page and most of it cannot go on this site at
    # all: consultation CTAs (hard rule 7), a review count and a Google Reviews
    # widget (hard rule 6), money-back and fees-matching guarantees (hard rule
    # 4), twelve services this site does not sell, a second office address, and
    # case studies that need client consent. Those sections are dropped, not
    # rewritten. Sections 6 and 7 are plain heading and text shells, so each is
    # used twice.
    PLAN=[
     # hero: heading, lede, price box, EFILE line, two buttons
     (0,[('title',f'Nil T2 Filing in {name}'),
         ('editor',P(f'Nil T2 filing for {name} corporations. One price for every '
                     'tax year, with no hourly billing and no add-on fees.')),
         ('title_text','$300.00'),('description_text','plus HST per tax year'),
         ('editor',P('Registered EFILE electronic filer. Your CRA confirmation is '
                     'emailed within 3 business days.')),
         ('text',CTA),('text','See the price')],{4:FORM,5:PRICE}),
     # trust strip: all four cells overwritten, see TRUST below
     (2,None,{}),
     (6,[('title',f'Corporations in {name}')],{}),
     (7,[('editor',P(datum, source))],{}),
     # the twelve Family 4 service pages for this place
     (9,None,{}),
     (6,[('title','What the Fee Does Not Cover')],{}),
     (7,[('editor',P(jb,
          'A federal Corporations Canada annual return costs $12.00 and is due '
          'within 60 days of your anniversary. It is a government fee and HST '
          'does not apply to it.',
          'This service is for a corporation with no activity in the tax year. A '
          'corporation with investment income, rental income, or dividends paid '
          'or received is not nil. If your corporation is not nil, we move your '
          'file to gondaliyacpa.ca at $350.00 plus applicable sales tax per year '
          'and tell you before any further charge.'))],{}),
     (35,[('title',f'File your {name} nil T2 return'),
          ('text',CTA),('text','See the price')],{1:FORM,2:PRICE}),
    ]
    TRUST=['CPA Ontario registered firm, Firm Registration 61330051',
           'Registered EFILE electronic filer',
           'CRA confirmation within 3 business days',
           '$300.00 plus HST per tax year']

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
        if idx==2:
            # Every cell is overwritten. The originals are a review count and
            # two guarantees, so leaving any of them is a hard-rule breach.
            for n,w in enumerate([x for x in ws if x['widgetType']=='icon-box']):
                if n<len(TRUST):
                    w['settings']['title_text']=TRUST[n]
                    if 'description_text' in w['settings']:
                        w['settings']['description_text']=''
        if idx==9:
            boxes=[w for w in ws if w['widgetType']=='elementskit-icon-box']
            for n,w in enumerate(boxes):
                if n>=len(SERVICES): continue
                pat,t,d=SERVICES[n]; s=w['settings']
                # Line 1525: "City name plus service, never city name alone",
                # so every card carries the place, not only the first.
                s['ekit_icon_box_title_text']=f'{t} in {name}'
                s['ekit_icon_box_description_text']=d
                if 'ekit_icon_box_badge_title' in s: s['ekit_icon_box_badge_title']=''
                if 'ekit_icon_box_btn_text' in s: s['ekit_icon_box_btn_text']=CTA
                setlink(w,f'https://corpnilfilingfor300.ca/{pat.format(p=slug)}/')
        for pos,url in links.items():
            if pos<len(ws): setlink(ws[pos],url)
        desource(sec)
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
