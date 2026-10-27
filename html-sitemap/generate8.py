import html, unicodedata, os

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES_TSV = os.path.join(HERE, "pages_v7.tsv")
POSTS_TSV = os.path.join(HERE, "posts_v7.tsv")

HUB_URL  = "https://gondaliyacpa.ca/html-sitemap/"
P1_URL   = "https://gondaliyacpa.ca/html-sitemap-pages/"
P2_URL   = "https://gondaliyacpa.ca/html-sitemap-pages-2/"
BLOG_URL = "https://gondaliyacpa.ca/html-sitemap-blog/"

def to_ascii(s):
    trans = {"–":"-","—":"-","‑":"-","‒":"-","―":"-","‘":"'","’":"'","‚":"'","‛":"'","“":'"',"”":'"',"„":'"',"…":"..."," ":" "," ":" "," ":" "}
    s = s.translate({ord(k): v for k, v in trans.items()})
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.encode("ascii", "ignore").decode("ascii")

def norm_title(raw):
    prev = raw
    for _ in range(4):
        cur = html.unescape(prev)
        if cur == prev: break
        prev = cur
    t = to_ascii(prev).strip()
    return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def read_tsv(path, is_post):
    out = []
    with open(path) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line: continue
            p = line.split("\t")
            if len(p) < 4: continue
            date, mod, url, title = p[0], p[1], p[2], "\t".join(p[3:])
            out.append((norm_title(title), url.strip(), date[:10], mod[:10], is_post))
    return out

pages = read_tsv(PAGES_TSV, False)
posts = read_tsv(POSTS_TSV, True)
# dedupe by url globally
seen=set()
def dedupe(lst):
    r=[]
    for e in lst:
        if e[1] in seen: continue
        seen.add(e[1]); r.append(e)
    return r
pages = dedupe(pages)
posts = dedupe(posts)

# Exclude the sitemap pages themselves (hub + the section pages)
_EXCLUDE = {
    "https://gondaliyacpa.ca/html-sitemap/",
    "https://gondaliyacpa.ca/html-sitemap-pages/",
    "https://gondaliyacpa.ca/html-sitemap-pages-2/",
    "https://gondaliyacpa.ca/html-sitemap-blog/",
}
def _norm_url(u):
    return u.rstrip("/") + "/"
pages = [e for e in pages if _norm_url(e[1]) not in _EXCLUDE]
posts = [e for e in posts if _norm_url(e[1]) not in _EXCLUDE]

def sort_desc(lst):
    lst.sort(key=lambda e: e[0].lower())
    lst.sort(key=lambda e: e[3], reverse=True)
    return lst
sort_desc(pages); sort_desc(posts)

# split pages into 2 roughly-equal halves (newest first)
half = (len(pages)+1)//2
pages1 = pages[:half]
pages2 = pages[half:]

MONTHS=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
MONTHS_FULL=["January","February","March","April","May","June","July","August","September","October","November","December"]
def fmt_date(d):
    y,m,dd=d.split("-"); return f"{MONTHS[int(m)-1]} {int(dd)}, {y}"
def month_label(ym):
    y,m=ym.split("-"); return f"{MONTHS_FULL[int(m)-1]} {y}"

def group_by_month(entries):
    groups=[]; cur=None
    for e in entries:
        ym=e[3][:7]
        if ym!=cur: groups.append((ym,[])); cur=ym
        groups[-1][1].append(e)
    return groups

STYLE = """<style>
.gcpa-sitemap-wrapper{max-width:1200px;margin:0 auto;padding:40px 20px;}
.gcpa-sitemap-title{font-size:2.5rem;color:#1a1a1a;margin-bottom:10px;font-weight:700;text-align:center;}
.gcpa-sitemap-description{text-align:center;color:#666;font-size:1.05rem;margin-bottom:10px;}
.gcpa-sitemap-legend{text-align:center;color:#8a94a2;font-size:.85rem;margin-bottom:22px;}
.gcpa-sitemap-legend b{color:#0a7d33;font-weight:700;}
.gcpa-sitemap-sections{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-bottom:22px;}
.gcpa-sitemap-sections a{display:inline-block;padding:7px 14px;border:1px solid #cfe0f5;border-radius:8px;color:#0066cc;text-decoration:none;font-weight:600;font-size:.9rem;background:#f5f9ff;}
.gcpa-sitemap-sections a:hover{background:#0066cc;color:#fff;}
.gcpa-sitemap-sections a.cur{background:#0066cc;color:#fff;border-color:#0066cc;}
.gcpa-sitemap-nav{text-align:center;margin-bottom:36px;line-height:2;}
.gcpa-sitemap-nav a{display:inline-block;padding:4px 10px;margin:3px;border:1px solid #dfe6ee;border-radius:6px;color:#0066cc;text-decoration:none;font-weight:600;font-size:.85rem;}
.gcpa-sitemap-nav a:hover{background:#0066cc;color:#fff;}
.gcpa-sitemap-section{margin-bottom:38px;scroll-margin-top:120px;}
.gcpa-sitemap-section h2{font-size:1.5rem;color:#0066cc;margin:0 0 16px;font-weight:700;border-bottom:2px solid #0066cc;padding-bottom:8px;}
.gcpa-sitemap-list{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(430px,1fr));gap:6px 40px;}
.gcpa-sitemap-list li{margin:0;padding:8px 0;border-bottom:1px solid #f0f2f5;display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;}
.gcpa-sitemap-list a{color:#333;text-decoration:none;font-size:1rem;line-height:1.5;flex:1;min-width:220px;}
.gcpa-sitemap-list a:hover{color:#0066cc;text-decoration:underline;}
.gcpa-type{display:inline-block;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em;color:#0a7d33;background:#e5f6ea;border-radius:4px;padding:1px 6px;margin-left:6px;vertical-align:middle;}
.gcpa-dt{color:#8a94a2;font-size:.8rem;white-space:nowrap;flex-shrink:0;}
.gcpa-dt .gcpa-upd{color:#0a7d33;}
.gcpa-hub-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;margin:10px 0 40px;}
.gcpa-hub-card{border:1px solid #e2e8f0;border-radius:12px;padding:22px 24px;}
.gcpa-hub-card h3{margin:0 0 6px;font-size:1.2rem;}
.gcpa-hub-card h3 a{color:#0066cc;text-decoration:none;}
.gcpa-hub-card p{margin:0;color:#667;font-size:.92rem;}
@media (max-width:768px){.gcpa-sitemap-title{font-size:2rem;}.gcpa-sitemap-wrapper{padding:30px 15px;}.gcpa-sitemap-list{grid-template-columns:1fr;}.gcpa-dt{white-space:normal;}}
</style>"""

def li_html(e):
    title,url,pub,mod,is_post=e
    badge='<span class="gcpa-type">Blog</span>' if is_post else ''
    return (f'<li><a href="{url}">{title}</a>{badge}'
            f'<span class="gcpa-dt">Published: {fmt_date(pub)} &middot; '
            f'<span class="gcpa-upd">Updated: {fmt_date(mod)}</span></span></li>')

def sections_bar(cur):
    def a(url,label,key):
        c=' class="cur"' if key==cur else ''
        return f'<a href="{url}"{c}>{label}</a>'
    return ('<div class="gcpa-sitemap-sections">'
            + a(HUB_URL,"Sitemap Home","hub")
            + a(P1_URL,"Pages &middot; Part 1","p1")
            + a(P2_URL,"Pages &middot; Part 2","p2")
            + a(BLOG_URL,"Blog Posts","blog")
            + '</div>')

MARKER="<!--GCPA_ROWS-->"

def build_section(key, title, subtitle, entries, out_key):
    groups = group_by_month(entries)
    nav = "".join(f'<a href="#m-{ym}">{MONTHS[int(ym[5:7])-1]} {ym[:4]}</a>' for ym,_ in groups)
    legend=('Each entry shows its <strong>Publishing Date</strong> and its '
            '<b>Last Reviewed &amp; Updated Date</b> (shown as "Updated").')
    header=(STYLE+"\n"
        +'<div class="gcpa-sitemap-wrapper">'
        +f'<h1 class="gcpa-sitemap-title">{title}</h1>'
        +f'<p class="gcpa-sitemap-description">{subtitle}</p>'
        +f'<p class="gcpa-sitemap-legend">{legend}</p>'
        +sections_bar(key)
        +'<div class="gcpa-sitemap-nav">'+nav+'</div>'
        +MARKER+'</div>')
    with open(os.path.join(HERE,f"header_{out_key}.html"),"w") as f: f.write(header)
    # full record
    parts=[header.replace(MARKER,"")]  # not used for upload; record only
    # chunks (<=8KB), sections may span chunks
    BUDGET=8000; small=[]; cur=""
    def flush(buf):
        return buf
    chunks=[]; cur=""
    for ym,items in groups:
        openf=f'<div class="gcpa-sitemap-section" id="m-{ym}"><h2>{month_label(ym)}</h2><ul class="gcpa-sitemap-list">'
        openc='<div class="gcpa-sitemap-section"><ul class="gcpa-sitemap-list">'
        CLOSE='</ul></div>'
        cur+=openf
        for e in items:
            li=li_html(e)
            if len(cur)+len(li)+len(CLOSE)>BUDGET:
                cur+=CLOSE; chunks.append(cur); cur=openc
            cur+=li
        cur+=CLOSE
    if cur: chunks.append(cur)
    for i,ch in enumerate(chunks):
        with open(os.path.join(HERE,f"c_{out_key}_{i:02d}.html"),"w") as f: f.write(ch)
    # faithful full record
    full=header.replace(MARKER,"")+ "".join(chunks) + ""  # header already has closing </div>? no: header ends with MARKER then </div>
    # rebuild record properly: header_without_marker already includes trailing </div>; chunks must go BEFORE that </div>
    hdr_open=header[:header.rindex(MARKER)]
    hdr_close=header[header.rindex(MARKER)+len(MARKER):]
    full=hdr_open+"".join(chunks)+hdr_close
    with open(os.path.join(HERE,f"published_{out_key}.html"),"w") as f: f.write(full)
    # byte table
    hb=len(header.encode()); L=hb; table=[("header",hb)]
    for i,ch in enumerate(chunks):
        L+=len(ch.encode()); table.append((f"c_{out_key}_{i:02d}",L))
    final_len=L-16  # last append removes marker
    return dict(key=out_key,title=title,n=len(entries),months=len(groups),
                chunks=len(chunks),header_bytes=hb,full_bytes=len(full.encode()),
                final_len=final_len,table=table)

r1=build_section("p1","HTML Sitemap — Pages (Part 1 of 2)",
   f"The {len(pages1)} most recently updated pages on gondaliyacpa.ca (newest first). See Part 2 for older pages and the Blog Posts sitemap for articles.",
   pages1,"p1")
r2=build_section("p2","HTML Sitemap — Pages (Part 2 of 2)",
   f"The remaining {len(pages2)} pages on gondaliyacpa.ca (older, newest first). See Part 1 for the most recent pages.",
   pages2,"p2")
rb=build_section("blog","HTML Sitemap — Blog Posts",
   f"All {len(posts)} blog posts on gondaliyacpa.ca, sorted by most recently updated.",
   posts,"blog")

# HUB page (small): intro + section cards + most-recently-updated top 30 across everything
allitems=pages+posts
allitems.sort(key=lambda e:e[0].lower()); allitems.sort(key=lambda e:e[3],reverse=True)
recent=allitems[:30]
total=len(pages)+len(posts)
hub_parts=[STYLE,"\n",'<div class="gcpa-sitemap-wrapper">',
    '<h1 class="gcpa-sitemap-title">HTML Sitemap</h1>',
    f'<p class="gcpa-sitemap-description">All {total} pages and blog posts on gondaliyacpa.ca ({len(pages)} pages, {len(posts)} blog posts). Browse by section below — each lists its Publishing Date and Last Reviewed &amp; Updated Date.</p>',
    sections_bar("hub"),
    '<div class="gcpa-hub-cards">',
    f'<div class="gcpa-hub-card"><h3><a href="{P1_URL}">Pages — Part 1</a></h3><p>{len(pages1)} most recently updated pages.</p></div>',
    f'<div class="gcpa-hub-card"><h3><a href="{P2_URL}">Pages — Part 2</a></h3><p>{len(pages2)} older pages.</p></div>',
    f'<div class="gcpa-hub-card"><h3><a href="{BLOG_URL}">Blog Posts</a></h3><p>{len(posts)} articles and guides.</p></div>',
    '</div>',
    '<div class="gcpa-sitemap-section"><h2>Recently updated</h2><ul class="gcpa-sitemap-list">',
    "".join(li_html(e) for e in recent),
    '</ul></div>',
    '</div>']
hub="".join(hub_parts)
with open(os.path.join(HERE,"hub.html"),"w") as f: f.write(hub)

for r in (r1,r2,rb):
    print(f"=== {r['key']}: {r['title']}")
    print(f"  entries={r['n']} months={r['months']} chunks={r['chunks']} header={r['header_bytes']} full={r['full_bytes']} final_len={r['final_len']}")
    print("  table:", " ".join(f"{name}:{val}" for name,val in r['table']))
print("HUB bytes:", len(hub.encode()))
print("pages split:", len(pages1), "+", len(pages2), "| posts:", len(posts), "| total:", total)
