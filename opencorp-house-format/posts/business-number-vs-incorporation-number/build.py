#!/usr/bin/env python3
"""Build post.html for the business number vs incorporation number post from source.md + corrections.json.

Body text comes from the draft (with approved corrections); house elements, links,
callouts and infographics are added from the tables below. The page shell (style,
widget CSS/JS) comes from template.html (the why-35-fee post as first built).
"""
import html, json, re

HERE = __file__.rsplit("/", 1)[0] or "."
src = open(f"{HERE}/source.md", encoding="utf-8").read()
for c in json.load(open(f"{HERE}/corrections.json", encoding="utf-8")):
    src = src.replace(c["from"], c["to"])
lines = src.splitlines()[1:]  # first line is the H1 + SEO H2

H1 = "Business Number vs Incorporation Number vs HST Number: What Each One Means"
H2SEO = "Business number vs incorporation number: Understanding CRA business number Canada, incorporation number Canada, and HST number differences"
ISO = "2026-11-18"
SLUG = "business-number-vs-incorporation-number-vs-hst-number"
OC = "https://opencorporationfor35.ca/"
UP = OC + "wp-content/uploads/2026/11/"

SECTIONS = {
    "Business Registration and Identification Numbers in Canada": (1, "toc-basics", "The Three Numbers", "blue", "The Basics"),
    "Differentiating Business Number and Incorporation Number": (2, "toc-differences", "BN vs Incorporation Number", "teal", "Comparison"),
    "What Is a GST/HST Number and When Is It Required?": (3, "toc-gst", "The GST/HST Number", "gold", "GST/HST"),
    "How to Obtain and Manage Your CRA Business Number and Program Accounts": (4, "toc-obtain", "Getting Your BN and Accounts", "green", "Registration"),
    "Finding, Maintaining, and Updating Your Business Number Information": (5, "toc-maintain", "Finding and Updating Numbers", "red", "Upkeep"),
    "Updated Information on Business Number vs Incorporation Number and HST Number": (6, "toc-updated", "Quick Answers by Question", "blue", "Updated"),
    "Frequently Asked Questions (FAQs)": (7, "toc-faq", "Frequently Asked Questions", "teal", "FAQ"),
    "Key Checklist for Managing Business Numbers and Program Accounts": (8, "toc-checklist", "Checklist and Options", "gold", "Checklist"),
}
H3 = """Understanding the CRA Business Number (BN) and Its Purpose
Distinguishing Between Business Number and Incorporation Number
HST Number vs. Business Number
What Is an Incorporation Number and How Is It Assigned?
Format and Use of Corporation Numbers Across Provinces and Federally
Business Number Format and Its Associated Program Accounts
Key Differences Between Business Number and Incorporation Number
How the GST/HST Number Relates to the Business Number
Common CRA Program Account Identifiers Linked to the Business Number
Registering for a Business Number via Business Registration Online
Automatic Business Number Issuance Upon Incorporation
Adding or Closing CRA Program Accounts Linked to the Business Number
Program Accounts: Income Tax (RC), Payroll (RP), GST/HST (RT), Import/Export (RM)
Ways to Locate an Existing Business Number
Requirements for Registering a New Business Number After Ownership or Structure Changes
Maintaining Accurate Business and Program Account Records with the CRA
Resources for Support and Contacting Relevant Agencies
What Is the Difference Between a Business Number and an Incorporation Number?
How Is a CRA Business Number Structured?
What Are Program Account Numbers Under Your Business Number?
Is My HST Number the Same as My Business Number?
What Does an Incorporation Number Look Like in Ontario and Federally?
Comparing DIY Incorporation vs Tax Software vs CPA Services
Additional Notes on Canadian Business Identification Numbers""".splitlines()
H4 = """Federal vs Provincial Incorporation Numbers
When You Receive an Incorporation Number
Formats for Federal Corporation Numbers
Provincial Corporation Number Examples
Standard 9-Digit Business Number
Program Account Identifiers Explained""".splitlines()
LEVEL = {**{h: 2 for h in SECTIONS}, **{h: 3 for h in H3}, **{h: 4 for h in H4}}
LISTY = {"Key Checklist for Managing Business Numbers and Program Accounts",
         "Comparing DIY Incorporation vs Tax Software vs CPA Services",
         "Additional Notes on Canadian Business Identification Numbers"}
FAQ_H = "Frequently Asked Questions (FAQs)"

LINKS = {  # section heading -> (phrase on the page, url); one site link per section
    "_intro": ("CRA business number Canada", OC + "guides/business-number-cra-accounts/"),
    "Understanding the CRA Business Number (BN) and Its Purpose": ("payroll taxes", OC + "payroll-service/"),
    "Distinguishing Between Business Number and Incorporation Number": ("Corporations Canada", OC + "incorporate-federally-in-canada/"),
    "HST Number vs. Business Number": ("on invoices", OC + "guides/hst-registration-guide/"),
    "Differentiating Business Number and Incorporation Number": ("starting a company in Canada", OC + "guides/how-to-incorporate-in-canada/"),
    "What Is an Incorporation Number and How Is It Assigned?": ("legal entity", OC + "incorporation-service-35/"),
    "Federal vs Provincial Incorporation Numbers": ("Ontario Business Registry", OC + "how-to-incorporate-in-ontario/"),
    "When You Receive an Incorporation Number": ("incorporation papers are approved", OC + "guides/articles-of-incorporation-explained/"),
    "Provincial Corporation Number Examples": ("Other provinces", OC + "guides/extra-provincial-registration/"),
    "Program Account Identifiers Explained": ("Payroll deductions", OC + "guides/payroll-setup-new-corporation/"),
    "Key Differences Between Business Number and Incorporation Number": ("Open Corporation for $35 is part of Gondaliya CPA", OC),
    "What Is a GST/HST Number and When Is It Required?": ("some non-residents", OC + "open-a-corporation-in-canada-as-a-non-resident-step-by-step-guide/"),
    "How the GST/HST Number Relates to the Business Number": ("corporate income tax", OC + "corporate-tax-filing-from-300/"),
    "Common CRA Program Account Identifiers Linked to the Business Number": ("A CPA can help set things up right", OC + "business-number-cra-account-registration/"),
    "How to Obtain and Manage Your CRA Business Number and Program Accounts": ("Open Corporation for $35 is part of Gondaliya CPA", OC + "services/"),
    "Automatic Business Number Issuance Upon Incorporation": ("After incorporation, you will have", OC + "guides/what-happens-after-you-incorporate/"),
    "Adding or Closing CRA Program Accounts Linked to the Business Number": ("import or export goods", OC + "guides/us-sales-and-canadian-corporations/"),
    "Finding, Maintaining, and Updating Your Business Number Information": ("provincial or federal registries", OC + "guides/incorporation-documents-checklist/"),
    "Ways to Locate an Existing Business Number": ("Corporate minute books", OC + "minute-book-preparation/"),
    "Requirements for Registering a New Business Number After Ownership or Structure Changes": ("Sole proprietor becomes corporation", OC + "convert-sole-proprietorship-corporation/"),
    "Maintaining Accurate Business and Program Account Records with the CRA": ("Updating ownership changes quickly", OC + "corporate-changes-amendments/"),
    "Updated Information on Business Number vs Incorporation Number and HST Number": ("working for yourself", OC + "sole-proprietorship-registration/"),
    "Is My HST Number the Same as My Business Number?": ("collect GST/HST", OC + "first-year-filing-calendar-new-corporation/"),
    "What Does an Incorporation Number Look Like in Ontario and Federally?": ("certificate of incorporation", OC + "guides/minute-book-requirements/"),
    "Key Checklist for Managing Business Numbers and Program Accounts": ("annual returns", OC + "annual-return-filing/"),
    "Comparing DIY Incorporation vs Tax Software vs CPA Services": ("flat fees from providers like Open Corporation for $35", OC + "pricing/"),
    "Additional Notes on Canadian Business Identification Numbers": ("Registered office addresses", OC + "guides/registered-office-address/"),
}


def callout(kind, tag, text):
    lead = f"<strong>{tag}:</strong> " if tag == "Risk Warning" else ""
    return f'<div class="gcpa-callout {kind}">\n<span class="co-tag">{tag}</span>\n<p>{lead}{text}</p>\n</div>'


def figure(name, alt, caption):
    return (f'<figure style="margin:22px 0;"><img src="{UP}{name}" alt="{html.escape(alt)}" style="width:100%;border-radius:12px;border:1px solid #d8e0e8;" />'
            f'<figcaption style="font-size:13px;color:#5a6b7b;text-align:center;padding:6px;">{html.escape(caption)}</figcaption></figure>')


import sys
sys.path.insert(0, f"{HERE}/../../assets")
from config import POSTS  # noqa: E402
CFG = next(p for p in POSTS if p["dir"] == "business-number-vs-incorporation-number")
INFO = {i["after"]: figure(f'{CFG["short"]}-{i["name"]}.png', i["alt"], i["caption"]) for i in CFG["info"]}

CTA_MID = """<div class="gcpa-cta" style="background:linear-gradient(135deg,#0f2a4a 0%,#1c4a78 100%) !important;">
<h4>Not sure which CRA accounts you need?</h4>
<p>Incorporation from $35 including HST plus government fees, with a free CPA consultation on your business number, your GST/HST, payroll and corporate tax accounts, and what goes on your invoices. Please book a free consultation.</p>
<div class="gcpa-trust"><span>1300+ 5-star Google reviews</span><span>Xero Partner Award Winner 2026</span><span>CPA Ontario Firm 61330051</span><span>30-Day Money-Back Guarantee</span></div>
<div class="gcpa-btnrow"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="https://opencorporationfor35.ca/">Open Corporation For $35</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BANNER = """<div class="gcpa-banner" style="background:linear-gradient(135deg,#0d3b66 0%,#0c7a7a 100%) !important;">
<div class="bt">Confused about which number goes where? Please book a free consultation and we will check your incorporation number, business number and CRA accounts with you.</div>
<div class="bb"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="mailto:info@gondaliyacpa.ca">info@gondaliyacpa.ca</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BEFORE = {
    "Distinguishing Between Business Number and Incorporation Number": callout("teal", "Key Stat", "<strong>9 digits:</strong> every CRA business number. A full program account adds two letters and four digits, so a GST/HST number such as 123456789 RT0001 has 15 characters."),
    "Program Account Identifiers Explained": callout("blue", "Worth Knowing", "Customers can check your GST/HST number in the CRA's GST/HST Registry before they claim input tax credits, so please print the full number, with RT0001, exactly as the CRA issued it."),
    "Key Differences Between Business Number and Incorporation Number": callout("gold", "Our Actual Experience", "The mix-up we see most often is a new owner printing the Ontario corporation number on an invoice where the GST/HST number belongs. We check invoice templates during setup so the full business number and RT0001 appear instead."),
    "What Is a GST/HST Number and When Is It Required?": CTA_MID,
    "Adding or Closing CRA Program Accounts Linked to the Business Number": callout("red", "Risk Warning", "Please do not show GST/HST on an invoice until the CRA has confirmed your RT account. Collecting tax without a valid GST/HST number, or under someone else's number, is not allowed and the tax can still be owed."),
    "Requirements for Registering a New Business Number After Ownership or Structure Changes": callout("red", "Risk Warning", "When a sole proprietor incorporates, the corporation gets its own business number. Please stop using the sole proprietorship's GST/HST number for corporate sales, and close or update the old accounts once the corporation's accounts are open."),
    "Updated Information on Business Number vs Incorporation Number and HST Number": BANNER,
    "Is My HST Number the Same as My Business Number?": callout("red", "Risk Warning", "Please do not share your own CRA sign-in with an accountant or bookkeeper. Authorize them as your representative through My Business Account instead, so each person's access can be limited and removed."),
}


def esc(s):
    return html.escape(s, quote=False)


def inline(s):
    out = esc(s)
    out = re.sub(r"\((https://www\.ontario\.ca/[^)\s]+)\)", r'(<a href="\1">\1</a>)', out)
    out = re.sub(r"(\[\d\])", r"<sup>\1</sup>", out)
    out = re.sub(r"(?<=[a-z]\.)(\d)$", r"<sup>\1</sup>", out)
    return out


def labelled(s):
    m = re.match(r"^([^:]{2,60}?): (.+)$", s)
    if m and "http" not in m.group(1) and len(m.group(1).split()) <= 6:
        return f"<strong>{inline(m.group(1))}:</strong> {inline(m.group(2))}"
    return inline(s)


def table(rows):
    head = rows.pop(0)
    t = ['<figure class="wp-block-table">', "<table>", "<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>", "<tbody>"]
    t += ["<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows]
    t += ["</tbody>", "</table>", "</figure>"]
    return "\n".join(t)


def numhead(h):
    n, i, label, colour, pill = SECTIONS[h]
    return (f"<h2>{esc(h)}</h2>\n<div class=\"gcpa-numhead\">\n<div class=\"num\" style=\"background:#0f2a4a !important;color:#ffffff !important;\">{n}</div>\n"
            f"<h4 id=\"{i}\" style=\"border:none;padding:0;margin:0;\">{esc(label)}</h4>\n<span class=\"gcpa-pill {colour}\">{esc(pill)}</span>\n</div>")


SMALL = '<p style="font-size:13.5px;color:#5a6b7b;margin:-6px 0 14px;">{}</p>'

# ---- parse the body ----
i = 0
while lines[i].strip() != "TLDR:":
    i += 1
i += 1
while not lines[i].strip():
    i += 1
INTRO = lines[i].strip()
i += 1
cur, faq, notes = "_intro", [], []
sections, order = {"_intro": []}, ["_intro"]
while i < len(lines):
    ln = lines[i].rstrip()
    if not ln or ln == "---":
        i += 1
        continue
    if ln == FAQ_H:
        cur = ln
        order.append(cur)
        sections[cur] = []
        i += 1
        while lines[i].rstrip() not in LEVEL:
            q = lines[i].strip()
            if q.endswith("?"):
                j = i + 1
                while not lines[j].strip():
                    j += 1
                faq.append((q, lines[j].strip()))
                i = j
            i += 1
        continue
    if ln in LEVEL:
        cur = ln
        order.append(cur)
        sections[cur] = []
        if cur in INFO:
            sections[cur].append(INFO[cur])
        i += 1
        if ln in LISTY:
            while not lines[i].strip():
                i += 1
            items = []
            while i < len(lines) and lines[i].strip():
                items.append(lines[i].rstrip())
                i += 1
            sections[cur].append("<ul>\n" + "\n".join(f"<li>{labelled(x)}</li>" for x in items) + "\n</ul>")
        continue
    m = re.match(r"^\[\^(\d+)\]: (.+)$", ln)
    if m:
        notes.append(m.group(2))
        i += 1
        if not any(re.match(r"^\[\^\d+\]: ", l) for l in lines[i:i + 3]):
            sections[cur].append('<p style="font-size:14px;margin:18px 0 6px;"><strong>Sources</strong></p>\n<ol style="font-size:14px;">\n'
                                 + "\n".join(f"<li>{esc(n)}</li>" for n in notes) + "\n</ol>")
        continue
    if re.match(r"^\d: ", ln):
        sections[cur].append(SMALL.format(inline(ln)))
        i += 1
        continue
    if "\t" in ln:
        rows = []
        while i < len(lines) and "\t" in lines[i]:
            rows.append(lines[i].rstrip().split("\t"))
            i += 1
        sections[cur].append(table(rows))
        continue
    if ln.endswith(":"):
        sections[cur].append(f"<p><strong>{inline(ln)}</strong></p>" if len(ln.split()) <= 6 else f"<p>{inline(ln)}</p>")
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i < len(lines) and "\t" in lines[i]:
            continue
        block, ended_by = [], "blank"
        while i < len(lines):
            x = lines[i].rstrip()
            if not x:
                break
            if x in LEVEL:
                ended_by = "heading"
                break
            if x.endswith(":") or "\t" in x:
                ended_by = "lead"
                break
            block.append(x)
            i += 1
        closer = None
        if ended_by == "blank" and len(block) >= 3:
            closer = block.pop()
        if block:
            sections[cur].append("<ul>\n" + "\n".join(f"<li>{labelled(x)}</li>" for x in block) + "\n</ul>")
        if closer:
            sections[cur].append(f"<p>{labelled(closer)}</p>")
        continue
    sections[cur].append(f"<p>{labelled(ln)}</p>")
    i += 1

# ---- links ----
SITE = r'<a [^>]*href="https://(opencorporationfor35\.ca/(?!wp-content)|gondaliyacpa\.ca/)'
INTRO_HTML = f"<p><strong>Open Corporation for $35 is a department of Gondaliya CPA.</strong> <strong>TLDR:</strong> {esc(INTRO)}</p>"


def add_link(htmltext, phrase, url):
    for m in re.finditer(re.escape(esc(phrase)), htmltext):
        before = htmltext[:m.start()]
        if before.rfind("<") > before.rfind(">") or before.count("<a ") > before.count("</a>"):
            continue
        return htmltext[:m.start()] + f'<a href="{url}">{m.group(0)}</a>' + htmltext[m.end():]
    raise SystemExit(f"link phrase not found: {phrase}")


INTRO_HTML = add_link(INTRO_HTML, *LINKS["_intro"])
for h, (phrase, url) in LINKS.items():
    if h == "_intro":
        continue
    body = "\n".join(sections[h])
    assert not re.search(SITE, body), f"section already has a site link: {h}"
    sections[h] = [add_link(body, phrase, url)]

# ---- assemble ----
parts = []
for h in order[1:]:
    if h in BEFORE:
        parts.append(BEFORE[h])
    if h in SECTIONS:
        parts.append(numhead(h))
    else:
        lvl = LEVEL[h]
        parts.append(f"<h{lvl}>{esc(h)}</h{lvl}>")
    if h == FAQ_H:
        parts.append('<div class="gcpa-faq" id="faq-main">')
        for q, a in faq:
            parts.append(f'<details><summary>{esc(q)}<span class="pl">+</span></summary>\n<div class="ans"><p>{esc(a)}</p></div></details>')
        parts.append("</div>")
        parts.append(callout("teal", "Worth Knowing", "A program account number is only as useful as the records behind it. Please keep the CRA letter that confirms each account with your minute book, so the number is easy to find at tax time."))
    parts.extend(sections[h])
BODY = "\n".join(parts)

HEAD = open(f"{HERE}/head.html", encoding="utf-8").read().replace("@@INTRO@@", INTRO_HTML)
A = HEAD + "\n" + BODY + "\n" + open(f"{HERE}/tail.html", encoding="utf-8").read()
tpl = open(f"{HERE}/template.html", encoding="utf-8").read()
B = open(f"{HERE}/widget.html", encoding="utf-8").read()
C = open(f"{HERE}/closing.html", encoding="utf-8").read()
page = re.sub(r'<div class="gcpa-hero"[\s\S]*?(?=<div id="ocf-chk">)', lambda m: A + "\n", tpl, count=1)
page = re.sub(r'<div class="s-head"[\s\S]*?(?=<button type="button" class="s-go")', lambda m: B, page, count=1)
page = re.sub(r'<div class="gcpa-cta"[^>]*>\s*<h4>Incorporate for \$35, HST included[\s\S]*$', lambda m: C, page, count=1)
assert "@@JSON@@" in page and "Business Number Readiness Check" in page

ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "BlogPosting", "@id": f"{OC}{SLUG}/#article", "headline": H1,
     "description": "Business number vs incorporation number vs HST number in Canada: who issues each one, what it looks like, the CRA program accounts RC, RT, RP and RM, and which number goes on invoices.",
     "datePublished": ISO, "dateModified": ISO, "author": {"@type": "Person", "name": "Sharad Gondaliya, CPA"},
     "image": UP + "Business-Number-vs-Incorporation-Number-Featured.jpg",
     "publisher": {"@type": "Organization", "name": "Open Corporation for $35", "description": "Open Corporation for $35 is a department of Gondaliya CPA.",
                   "parentOrganization": {"@type": "AccountingService", "name": "Gondaliya CPA Professional Corporation", "identifier": "CPA Ontario Firm Registration 61330051"}},
     "mainEntityOfPage": f"{OC}{SLUG}/"},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
page = page.replace("@@JSON@@", '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False) + "\n</script>")
words = len(re.sub("<[^>]+>", " ", html.unescape(re.sub(r"<(style|script)[^>]*>.*?</\1>", "", page, flags=re.S))).split())
page = page.replace("@@READ@@", str(round(words / 220)))
open(f"{HERE}/post.html", "w", encoding="utf-8").write(page)
open(f"{HERE}/headings.txt", "w", encoding="utf-8").write("\n".join([H1, H2SEO] + order[1:]) + "\n")
print("words", words, "reading", round(words / 220), "faq", len(faq), "sections", len(order) - 1, "bytes", len(page))
