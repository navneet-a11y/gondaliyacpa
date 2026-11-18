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
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from city_copy import COPY

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

# Local data values, pulled by build/f3/pull_corp_counts.py from the
# Corporations Canada open data "Federal Corporations" dataset
# (open.canada.ca dataset 0032ce54-c5dd-4b66-99a0-320a7b5e99f2, refreshed
# daily at source). Counted over corporations-active-cbca-en.csv, every row
# of which carries Status "Active", on the registered-office City/town field
# with Province/territory "ON" and Country "CA".
#
# Toronto's figure includes the five former municipalities amalgamated into
# the City of Toronto in 1998: a registered office in Scarborough or North
# York is a registered office in Toronto. The literal "Toronto" city value
# alone is 81,327; the six-municipality total is 106,120. The wider figure is
# used because the sentence claims a registered office *in Toronto*, and the
# source line names the method so the pull stays reproducible.
CITY_DATA = {
 'mississauga': {
   # Port Credit, Streetsville, Malton, Erin Mills and Dixie were absorbed in
   # 1974 but survive in only 18 registered-office rows between them, against
   # Toronto's 24,793, so the literal city value stands alone here and the
   # sentence carries no "including" clause.
   'count':    '36,448',
   'includes': '',
   'pulled':   'November 18, 2026',
 },
 'toronto': {
   'count':    '106,120',
   'includes': 'including the former municipalities of Scarborough, '
               'North York, Etobicoke, York and East York',
   'pulled':   'November 18, 2026',
 },
}

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

# Attachment 273 on corpnilfilingfor300.ca: the same team photograph the
# source template hotlinked from gondaliyacpa.ca, already uploaded to this
# site. Used so section 1 carries its image instead of an empty frame.
INTRO_IMG_ID = 273
INTRO_IMG = ('https://corpnilfilingfor300.ca/wp-content/uploads/2026/09/'
             '169A7423-1-scaled-2.jpg')

# Hero banner, matched to the service page /nil-t2-filing/ (post 434,
# container sv00001) read from its generated Elementor stylesheet on
# 2026-11-18. The template arrived with a #000000 overlay at 0.03 opacity,
# which is no overlay at all: the photograph rendered at full brightness
# under white headings. The service page darkens the same photograph with
# #0B1A33 at 0.82 and centres it.
HERO = {
    'background_position':       'center center',
    'background_overlay_color':  '#0B1A33',
    'background_overlay_opacity': {'unit':'px','size':0.82,'sizes':[]},
    'custom_height':             {'unit':'px','size':340,'sizes':[]},
}


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
                # An emptied image keeps its alt text, which still named the
                # other firm and its principal ("Sharad Gondaliya, CPA") on an
                # image box with no image left. Alt text is not visible text,
                # so the audit cannot see it, but it ships in the HTML.
                if isinstance(v, dict) and 'alt' in v and isinstance(v['alt'], str):
                    if not v.get('url') or 'Gondaliya' in v['alt']:
                        v['alt'] = ''
            # ElementsKit decoration carried over from the source page: a
            # watermark word rendered behind the heading (the original reads
            # "bussiness", misspelled), and the inert Read More label on image
            # boxes whose button is switched off. Neither belongs on this site.
            if st.get('shadow_text_content'):
                st['shadow_text_content'] = ''
            if st.get('ekit_image_box_btn_text') and not st.get('ekit_image_box_enable_btn'):
                st['ekit_image_box_btn_text'] = ''
        for v in (n.get('elements') or []):
            desource(v)
    elif isinstance(n, list):
        for v in n:
            desource(v)

# Family 3 FAQ. The source template's FAQ (section 34) is a raw html widget
# holding nineteen Mississauga municipal-licensing questions -- City business
# licences, By-law 0001-2006, home-based business rules -- none of which this
# site answers. It also carries a <script> and no <style>, so its styling came
# from the other page's stylesheet and it would have rendered unstyled here.
# It is replaced outright with this self-contained block.
#
# Hard rule 6 bans FAQPage schema. Native <details> emits none and no JSON-LD
# is added, so the accordion is plain content. No <script>: <details> opens and
# closes without JavaScript.
FAQ_CSS = (
 '<style>'
 '.cnf-faq{max-width:1140px;margin:0 auto;padding:0 20px}'
 '.cnf-faq details{background:#f5f8fc;border-radius:12px;margin:0 0 12px;'
 'padding:16px 20px}'
 '.cnf-faq summary{cursor:pointer;font-family:Poppins,sans-serif;'
 'font-weight:600;font-size:17px;line-height:1.45;color:#0B1A33;'
 'list-style:none}'
 '.cnf-faq summary::-webkit-details-marker{display:none}'
 '.cnf-faq summary:after{content:"+";float:right;margin-left:12px;'
 'font-weight:700;color:#314D8A}'
 '.cnf-faq details[open] summary:after{content:"\\2013"}'
 '.cnf-faq .cnf-a{margin:12px 0 0;font-family:Lato,sans-serif;font-size:16px;'
 'line-height:1.6;color:#4a5568}'
 '.cnf-faq .cnf-a p{margin:0 0 10px}'
 '.cnf-faq .cnf-a p:last-child{margin:0}'
 '.cnf-faq .cnf-a a{color:#314D8A}'
 '</style>'
)

def faq_html(name, slug, qa=None):
    """Eight questions, each answered in a sentence or two, linking on to the
    page that answers it in full rather than restating it (6(k))."""
    B = 'https://corpnilfilingfor300.ca'
    default = [
     (f'Does a {name} corporation with no activity still have to file a T2?',
      f'<p>Yes. A corporation files a T2 for every tax year it exists, whether or '
      f'not it earned anything. The obligation ends when the corporation is '
      f'dissolved, not when it stops trading. '
      f'<a href="{B}/answers/does-an-inactive-corporation-have-to-file-a-t2/">'
      f'Read the full answer</a>.</p>'),
     ('What counts as a nil year?',
      '<p>No revenue, no expenses, no bank activity and no employees in the tax '
      'year. A corporation with investment income, rental income, or dividends '
      'paid or received is not nil, and we tell you before any further charge.</p>'),
     (f'When is the nil T2 due for a {name} corporation?',
      f'<p>Within six months of the fiscal year end, the same deadline as any '
      f'other T2. The year end is your corporation\u2019s own, not December 31. '
      f'<a href="{B}/nil-t2-filing-deadline-{slug}/">See the deadline page</a>.</p>'),
     ('I have several unfiled years. Can they be filed together?',
      f'<p>Yes. They are filed oldest year first, each as its own return at '
      f'$300.00 plus HST per tax year. '
      f'<a href="{B}/catch-up-nil-t2-filing-{slug}/">See catch-up filing</a>.</p>'),
     ('Do I have to sign anything?',
      f'<p>One T183CORP for each tax year, signed electronically. Nothing is '
      f'printed or mailed. '
      f'<a href="{B}/guides/t183corp-signing-and-transmission/">How signing '
      f'works</a>.</p>'),
     ('Does this cover my Ontario annual return?',
      f'<p>No. The Ontario annual return goes through the Ontario Business '
      f'Registry and is separate from the T2. We tell you if you still owe one. '
      f'<a href="{B}/tools/ontario-annual-return-due-date-calculator/">Check when '
      f'yours is due</a>.</p>'),
     ('My corporation only holds shares or property. Is that nil?',
      f'<p>Usually not. A holding corporation with investment income, rental '
      f'income or dividends paid or received is not nil, and the return is not a '
      f'$300.00 nil filing. '
      f'<a href="{B}/inactive-holding-corporation-t2-filing-{slug}/">What applies '
      f'instead</a>.</p>'),
     (f'I live outside Canada and my corporation is registered in {name}. Can you '
      f'still file?',
      f'<p>Yes. The T183CORP is signed electronically, so a director outside '
      f'Canada can sign it. '
      f'<a href="{B}/nil-t2-filing-for-non-resident-owned-corporations-{slug}/">'
      f'Non-resident owned corporations</a>.</p>'),
     ('I am not sure whether my year is nil. Can you check before I pay?',
      f'<p>Yes. Send the year end and what the corporation did, if anything, and '
      f'we confirm whether the year is nil before any charge. If it is not, we '
      f'say so and what it would cost instead. '
      f'<a href="{B}/no-activity-corporation-tax-return-{slug}/">What counts as '
      f'no activity</a>.</p>'),
     ('I am closing the corporation. Do I still need a return?',
      f'<p>Yes. A final T2 covers the period up to dissolution and is due within '
      f'six months of it. Filing it is what closes the corporation\u2019s account '
      f'with the Canada Revenue Agency. '
      f'<a href="{B}/final-t2-before-dissolution-{slug}/">Final T2 before '
      f'dissolution</a>.</p>'),
    ]
    qa = qa or default
    rows = ''.join(
        f'<details><summary>{q}</summary><div class="cnf-a">{a}</div></details>'
        for q, a in qa)
    return (FAQ_CSS + '<div class="cnf-faq">' + rows + '</div>')

def build(slug,name,kind,jkey,supplied):
    C = COPY.get(slug, {})
    jt,jb = JNOTE[jkey]  # jt unused in this map; the shell has one heading
    if supplied:
        datum = (f'{supplied} T2 returns were assessed by the Canada Revenue Agency for corporations in {name}.')
        source = ('Source: CRA corporation income tax statistics, refreshed when the annual table is reissued, '
                  f'plus the Corporations Canada open-data bulk file filtered by province. Pulled {NEEDS_DATE}.')
    else:
        cd = CITY_DATA.get(slug)
        if cd:
            inc = (', ' + cd['includes']) if cd.get('includes') else ''
            datum = (f"{cd['count']} active federal business corporations have a "
                     f"registered office in {name}{inc}.")
            source = ('Source: Corporations Canada open data, active CBCA corporations '
                      'file, registered-office city and province fields. '
                      f"Pulled {cd['pulled']}.")
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
         # 2026-11-18: the hero's right cell carried the price, which the
         # price block further down already states twice. It now carries
         # the strongest proof this site may make. Reviews and star
         # ratings, which the source page used here, are barred by hard
         # rule 6 and by audit_visible's 'review or year count' pattern.
         ('title_text','CPA Ontario Registered Firm'),
         ('description_text','Firm Registration 61330051'),
         ('editor',P('Registered EFILE electronic filer. Your CRA confirmation is '
                     'emailed within 3 business days.')),
         ('text',CTA),('text','See the price')],{4:FORM,5:PRICE}),
     # 2026-11-18: intro block with the team photograph. The original led
     # with "AFFORDABLE Business Tax Accountant" (hard rule 4) over copy for
     # the other firm's full service list, and both buttons pointed at
     # gondaliyacpa.ca consultation and pricing pages (hard rule 7). Heading,
     # body, both buttons and the image are all replaced. The facts are the
     # ones /nil-t2-filing/ already publishes.
     (1,[('ekit_heading_title',f'Nil T2 Filing for {name} Corporations'),
         ('ekit_heading_extra_title',
          P(f'A nil T2 is the corporate return a {name} corporation files for a '
            'tax year in which it had no revenue, no expenses and no bank '
            'activity. The corporation still exists, so the return is still due. '
            'Incorporating and then going quiet does not end the obligation, and '
            'a year left unfiled stays open until the return is transmitted.',
            f'Nil T2 filing in {name} covers the year end to end. The return is '
            'prepared and reviewed, you sign a T183CORP for each tax year, and '
            'the return is transmitted to the Canada Revenue Agency '
            'electronically. It is done online from start to finish, so there is '
            'nothing to print, mail or sign in person, wherever in the city your '
            'registered office sits.')),
         ('text',CTA),('text','See the price')],{1:FORM,2:PRICE}),
     # trust strip: all four cells overwritten, see TRUST below
     (2,None,{}),
     # 2026-11-18: three-cell strip. The original made availability claims
     # ("Weekend and evening support until 9 PM"), which this site does not
     # make, so all six fields are overwritten.
     (3,[('title','One Fee Per Tax Year'),
         ('editor',P('No hourly billing and no add-on charges for schedules '
                     'or transmission.')),
         ('title','Every Unfiled Year Counts'),
         ('editor',P('Each year is a separate T2 return at $300.00 plus HST '
                     'per tax year.')),
         ('title','Signed and Filed Online'),
         ('editor',P('Nothing to print. You sign the T183CORP electronically '
                     'for each tax year.'))],{}),
     (6,[('title',f'Corporations in {name}')],{}),
     (7,[('editor',P(datum, source))],{}),
     # 2026-11-18: section 8 heads the service grid.
     (8,[('ekit_heading_title',f'Nil T2 Filing Services in {name}')],{}),
     # the twelve Family 4 service pages for this place
     (9,None,{}),
     # What the fee buys. Six cards, every claim one this site already makes.
     (16,[('ekit_heading_title',f'What You Get for $300.00 in {name}'),
          ('ekit_image_box_title_text','CPA Prepared and Reviewed'),
          ('ekit_image_box_description_text',
           'Your T2 is prepared and reviewed by a CPA Ontario registered firm, '
           'Firm Registration 61330051, before it is transmitted.'),
          ('ekit_image_box_title_text','Registered EFILE Electronic Filer'),
          ('ekit_image_box_description_text',
           'The return goes to the Canada Revenue Agency electronically, not by mail.'),
          ('ekit_image_box_title_text','One Price Per Tax Year'),
          ('ekit_image_box_description_text',
           '$300.00 plus HST per tax year, quoted before any work starts. '
           'No hourly billing and no add-on charges.'),
          ('ekit_image_box_title_text','T183CORP Signed Online'),
          ('ekit_image_box_description_text',
           'You receive a T183CORP for each tax year and sign it electronically. '
           'One form per year.'),
          ('ekit_image_box_title_text','CRA Confirmation in Writing'),
          ('ekit_image_box_description_text',
           'Your CRA confirmation is emailed within 3 business days of transmission.'),
          ('ekit_image_box_title_text','We Tell You If You Are Not Nil'),
          ('ekit_image_box_description_text',
           'A corporation with investment income, rental income, or dividends paid '
           'or received is not nil. We tell you before any further charge.')],{}),
     # Process: intro shell, then the four steps.
     (21,[('editor',P('How it works')),
          ('title',f'How Nil T2 Filing Works in {name}'),
          ('text',CTA),('text','See the price'),
          ('editor',P('Four steps, all online. You send the corporation details, a '
                      'CPA prepares and reviews the return, you sign the T183CORP, '
                      'and the return is transmitted to the Canada Revenue Agency.'))],
      {2:FORM,3:PRICE}),
     (22,[('title_text','Send Details'),
          ('description_text','Corporation number, tax year end, and which years are '
                              'unfiled. Online, with no appointment.'),
          ('title_text','CPA Review'),
          ('description_text','A CPA checks that the year is nil and prepares the '
                              'T2 return.'),
          ('title_text','Sign T183CORP'),
          ('description_text','You sign one T183CORP for each tax year, '
                              'electronically.'),
          ('title_text','CRA Confirmation'),
          ('description_text','The return is transmitted and your CRA confirmation '
                              'is emailed within 3 business days.')],{}),
     # Pricing shell. The original carried a money-back guarantee, a
     # fees-matching policy and tick emoji; all three are replaced outright.
     (23,[('editor',P('Nil T2 filing price')),
          ('title',f'Nil T2 Filing Price in {name}'),
          ('text','See the price'),
          ('editor',P('$300.00 plus HST per tax year. The fee covers preparation, '
                      'CPA review, the T183CORP for signature, and electronic '
                      'transmission to the Canada Revenue Agency. Each unfiled tax '
                      'year is a separate return at the same price.'))],{2:PRICE}),
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
     # 2026-11-18: the FAQ closes the page, after the final call to action,
     # at Navneet's request.
     (33,[('title',f'Nil T2 Filing in {name}: Common Questions')],{}),
     (34,[('html',faq_html(name,slug,C.get('faq')))],{}),
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
        if idx==0:
            sec['settings'].update(copy.deepcopy(HERO))
            for w in ws:
                st = w['settings']
                if w['widgetType']=='image-box':
                    # Sized for "$300.00"; the replacement text needs less.
                    st['title_typography_typography']='custom'
                    st['title_typography_font_family']='Poppins'
                    st['title_typography_font_size']={'unit':'px','size':26,'sizes':[]}
                    st['title_typography_font_weight']='600'
                if w['widgetType']=='text-editor' and 'text_color' not in st:
                    # The EFILE line carried no colour at all, so it inherited
                    # the theme's grey and rendered dim on the dark banner.
                    st['text_color']='#FFFFFF'
                    st['typography_typography']='custom'
                    st['typography_font_family']='Poppins'
                    st['typography_font_size']={'unit':'px','size':16,'sizes':[]}
                    st['typography_font_weight']='400'
        if idx==1:
            # The image widget carries a gondaliyacpa.ca URL that desource()
            # would blank, leaving an empty frame. Point it at this site's own
            # copy of the same photograph instead, with alt text that does not
            # repeat the firm name (desource() strips alt naming the other
            # firm, which is correct for the assets it removes).
            for w in ws:
                if w['widgetType']=='image' and isinstance(w['settings'].get('image'),dict):
                    w['settings']['image']={
                        'url':INTRO_IMG,'id':INTRO_IMG_ID,'source':'library','size':'',
                        'alt':f'CPA Ontario registered firm filing nil T2 returns '
                              f'for {name} corporations'}
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

    # Per-city prose (city_copy.COPY). A name swap alone scores 0.976 against
    # Toronto on the 6(k) measure, so each city rewrites the shared wording
    # rather than only its place name. Applied last, over the composed
    # template, so the section map stays one thing and the writing another.
    pairs = C.get('text') or []
    if pairs:
        hits = {}
        def sub(n):
            if isinstance(n, dict):
                st = n.get('settings')
                if isinstance(st, dict):
                    for k, v in list(st.items()):
                        if isinstance(v, str) and v:
                            for i, pair in enumerate(pairs):
                                a, b = pair[0], pair[1]
                                # 'exact' replaces only a whole setting value.
                                # Needed where the default text is a substring
                                # of another string on the page: "Corporations
                                # in <city>" is the local-data heading and also
                                # sits inside the non-resident service card.
                                if len(pair) > 2 and pair[2] == 'exact':
                                    if v == a:
                                        v = b
                                        hits[i] = hits.get(i, 0) + 1
                                elif a in v:
                                    v = v.replace(a, b)
                                    hits[i] = hits.get(i, 0) + 1
                            st[k] = v
                for v in (n.get('elements') or []):
                    sub(v)
            elif isinstance(n, list):
                for v in n:
                    sub(v)
        sub(out)
        missed = [p[0] for i, p in enumerate(pairs) if i not in hits]
        if missed:
            raise SystemExit(
                f'{slug}: {len(missed)} replacement(s) matched nothing, so the '
                f'default wording would ship. First: {missed[0][:90]!r}')
    return out

made=[]
for slug,name,kind,jkey,supplied in PLACES:
    if WANT and slug not in WANT: continue
    content=build(slug,name,kind,jkey,supplied)
    tpl={'version':'0.4','title':f'CorpNil City Hub — {name}','type':'page',
         'content':content,'page_settings':[]}
    path=os.path.join(OUTDIR,f'corpnil-cityhub-{slug}.json')
    json.dump(tpl,open(path,'w'),ensure_ascii=False,separators=(',',':'))
    made.append((slug,name,kind,os.path.getsize(path),
                 supplied is not None or slug in CITY_DATA))
for slug,name,kind,size,hasdata in made:
    print(f'  {name:18s} {kind:12s} {size:>7,} b  data: {"supplied" if hasdata else "TO PULL"}')
print(f'{len(made)} templates written to {OUTDIR}')
