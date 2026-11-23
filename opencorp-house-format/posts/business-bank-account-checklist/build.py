#!/usr/bin/env python3
"""Build post.html for the corporate bank account checklist post from source.md + corrections.json."""
import html, json, re

HERE = __file__.rsplit("/", 1)[0] or "."
src = open(f"{HERE}/source.md", encoding="utf-8").read()
for c in json.load(open(f"{HERE}/corrections.json", encoding="utf-8")):
    src = src.replace(c["from"], c["to"])
lines = src.splitlines()[1:]

H1 = "Business Bank Account Opening Checklist for a New Corporation"
H2SEO = "Business Account Checklist and Documents Needed to Open a Corporate Bank Account in Canada | Open Corporation for $35"
ISO = "2026-11-23"
SLUG = "business-bank-account-opening-checklist-new-corporation"
OC = "https://opencorporationfor35.ca/"
UP = OC + "wp-content/uploads/2026/11/"
DIR = "business-bank-account-checklist"
FEATURED = "Corporate-Bank-Account-Checklist-Featured.jpg"
DESC = "Business bank account opening checklist for a new Canadian corporation: certificate and articles, corporate profile, banking resolution, registers and ISC, ID for signers and 25% owners, and how to fund the account."

SECTIONS = {
    "Introduction to Business Bank Accounts in Canada": (1, "toc-intro", "Why a Corporate Account", "blue", "The Basics"),
    "Business Account Checklist for Canadian Corporations": (2, "toc-checklist", "The Document Checklist", "teal", "Checklist"),
    "Step-by-Step Guide to Opening a Corporate Bank Account in Canada": (3, "toc-steps", "Step-by-Step Opening", "gold", "Steps"),
    "Understanding Different Types of Business Bank Accounts": (4, "toc-types", "Types of Accounts", "green", "Accounts"),
    "Managing Your Business Bank Account Effectively": (5, "toc-managing", "Managing the Account", "red", "Managing"),
    "Contact and Support Resources for Business Banking Customers": (6, "toc-support", "Fees, Rules and Support", "blue", "Support"),
    "FAQs on Corporate Bank Account Setup and Compliance": (7, "toc-faq", "Frequently Asked Questions", "teal", "FAQ"),
    "Additional Key Points on Corporate Banking Compliance": (8, "toc-keypoints", "Key Points and Delays", "gold", "Summary"),
}
H3 = """Importance of Opening a Business Bank Account for Your Corporation
Key Benefits of Having a Dedicated Corporate Bank Account
Overview of Business Banking Requirements in Canada
Essential Documents Needed to Open a Corporate Bank Account
Corporate Banking Checklist: What You Should Prepare Before Applying
CRA Business Number and Its Role in Business Banking
Articles of Incorporation and Shareholder Information Requirements
Eligibility Criteria for Opening a Corporate Bank Account
Procedure for Opening a Business Banking Account After Incorporation
How to Apply for a Business Bank Account Online
What to Expect During the Account Opening Process
Types of Business Bank Accounts Available for Canadian Corporations
Choosing the Right Bank Account Based on Business Needs
Features and Benefits of Various Business Account Options
Managing Sub-Accounts, Bill Payments, and Money Transfers
Tips for Organizing Finances Using a Business Account
How to Use Overdraft Protection and Access Loans or Credit
Making Payments Easy with Interac e-Transfers® and EFTs
Planning for Tax Time Using Your Business Bank Account
Common Business Bank Account Fees and How to Avoid Them
Legal Disclaimers and Terms Related to Corporate Bank Accounts
Encouragement to Apply and Start Your Business Banking Journey with Open Corporation for $35
Beneficial Ownership and Reporting Essentials
Tips on Avoiding Common Corporate Bank Account Delays
Comparing Professional Support Options""".splitlines()
H4 = """Professional image and credibility
Separation of personal and business finances
Easier accounting and bookkeeping
Streamlined tax preparation
General requirements for corporations
Regulatory guidelines and compliance""".splitlines()
H5 = []
LEVEL = {**{h: 2 for h in SECTIONS}, **{h: 3 for h in H3}, **{h: 4 for h in H4}}
LISTY = {"Additional Key Points on Corporate Banking Compliance", "Beneficial Ownership and Reporting Essentials", "Tips on Avoiding Common Corporate Bank Account Delays"}
TAILS = ("Open Corporation for $35 offers expert",)
FAQ_H = "FAQs on Corporate Bank Account Setup and Compliance"

LINKS = {
    "_intro": ("corporate banking checklist", OC + "business-bank-account-setup/"),
    "Introduction to Business Bank Accounts in Canada": ("Starting a corporation in Canada", OC + "guides/how-to-incorporate-in-canada/"),
    "Professional image and credibility": ("articles of incorporation", OC + "guides/articles-of-incorporation-explained/"),
    "Easier accounting and bookkeeping": ("makes tracking money easier", OC + "incorporation-bookkeeping-bundle/"),
    "Streamlined tax preparation": ("taxes get clearer", OC + "corporate-tax-filing-from-300/"),
    "General requirements for corporations": ("proof of where your company’s office is", OC + "guides/registered-office-address/"),
    "Business Account Checklist for Canadian Corporations": ("business account checklist", OC + "guides/business-bank-account/"),
    "Essential Documents Needed to Open a Corporate Bank Account": ("Certificate of Incorporation", OC + "incorporation-service-35/"),
    "Corporate Banking Checklist: What You Should Prepare Before Applying": ("Individual with Significant Control (ISC)", OC + "guides/individuals-with-significant-control/"),
    "CRA Business Number and Its Role in Business Banking": ("program accounts like GST/HST", OC + "business-number-cra-account-registration/"),
    "Articles of Incorporation and Shareholder Information Requirements": ("share classes", OC + "guides/share-structure-explained/"),
    "Step-by-Step Guide to Opening a Corporate Bank Account in Canada": ("business bank account requirements Canada", OC + "guides/what-happens-after-you-incorporate/"),
    "Eligibility Criteria for Opening a Corporate Bank Account": ("officially incorporated either federally or provincially", OC + "incorporate-federally-in-canada/"),
    "Procedure for Opening a Business Banking Account After Incorporation": ("By-laws or banking resolution", OC + "minute-book-preparation/"),
    "What to Expect During the Account Opening Process": ("ownership info is missing", OC + "guides/incorporation-documents-checklist/"),
    "Types of Business Bank Accounts Available for Canadian Corporations": ("handling payroll", OC + "payroll-service/"),
    "Features and Benefits of Various Business Account Options": ("Works with tools like QuickBooks", OC + "incorporation-bookkeeping-bundle/"),
    "Tips for Organizing Finances Using a Business Account": ("Update your bookkeeping regularly", OC + "services/"),
    "How to Use Overdraft Protection and Access Loans or Credit": ("updated financial statements", OC + "corporate-compliance-subscription/"),
    "Planning for Tax Time Using Your Business Bank Account": ("filing T2 returns", OC + "guides/first-t2-return/"),
    "Contact and Support Resources for Business Banking Customers": ("Ontario Business Registry", OC + "how-to-incorporate-in-ontario/"),
    "Legal Disclaimers and Terms Related to Corporate Bank Accounts": ("A CPA should review loans vs subscriptions", "https://gondaliyacpa.ca/consultation/"),
    "Encouragement to Apply and Start Your Business Banking Journey with Open Corporation for $35": ("simple online incorporation", OC + "incorporation-form/"),
    "Additional Key Points on Corporate Banking Compliance": ("Registered Office Proof Matching Registry", OC + "corporate-changes-amendments/"),
    "Beneficial Ownership and Reporting Essentials": ("Layered Holding Company Ownership Tracing", OC + "guides/holding-company-canada/"),
    "Tips on Avoiding Common Corporate Bank Account Delays": ("Prepare a clear minute book", OC + "guides/minute-book-requirements/"),
    "Comparing Professional Support Options": ("Open Corporation for $35 offers expert CPA-backed support", OC + "pricing/"),
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
CFG = next(p for p in POSTS if p["dir"] == DIR)
INFO = {i["after"]: figure(f'{CFG["short"]}-{i["name"]}.png', i["alt"], i["caption"]) for i in CFG["info"]}

CTA_MID = """<div class="gcpa-cta" style="background:linear-gradient(135deg,#0f2a4a 0%,#1c4a78 100%) !important;">
<h4>Walk into the bank once</h4>
<p>Incorporation from $35 including HST plus government fees, with a free CPA consultation on your banking resolution, registers, ISC register and how to fund the account. Please book a free consultation.</p>
<div class="gcpa-trust"><span>1300+ 5-star Google reviews</span><span>Xero Partner Award Winner 2026</span><span>CPA Ontario Firm 61330051</span><span>30-Day Money-Back Guarantee</span></div>
<div class="gcpa-btnrow"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="https://opencorporationfor35.ca/">Open Corporation For $35</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BANNER = """<div class="gcpa-banner" style="background:linear-gradient(135deg,#0d3b66 0%,#0c7a7a 100%) !important;">
<div class="bt">Bank appointment coming up? Please book a free consultation and we will check your documents and registers before you go.</div>
<div class="bb"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="mailto:info@gondaliyacpa.ca">info@gondaliyacpa.ca</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BEFORE = {
    "Corporate Banking Checklist: What You Should Prepare Before Applying": callout("teal", "Key Stat", "<strong>25%:</strong> the ownership level at which banks must identify a person as a beneficial owner under FINTRAC rules, and the same level that puts a person on your ISC register under the CBCA and OBCA."),
    "Procedure for Opening a Business Banking Account After Incorporation": callout("red", "Risk Warning", "Please do not deposit business income into your personal account while the corporate account is being opened. Mixed funds make the corporation's records harder to prove and can be treated as a shareholder loan or benefit."),
    "How to Apply for a Business Bank Account Online": callout("blue", "Worth Knowing", "A CRA business number is not legally required to open a corporate account, but Ontario and federal incorporations receive one automatically, so please bring the business number confirmation to the bank."),
    "Understanding Different Types of Business Bank Accounts": CTA_MID,
    "Types of Business Bank Accounts Available for Canadian Corporations": callout("gold", "Our Actual Experience", "The most common reason we see a bank meeting rescheduled is a name mismatch. The legal name on the certificate, the corporate profile and the banking resolution must match exactly, including punctuation and Inc. versus Incorporated."),
    "Planning for Tax Time Using Your Business Bank Account": callout("red", "Risk Warning", "Please do not pay personal expenses from the corporate account. Unless they are recorded as salary, dividends or a shareholder loan that is repaid on time, the CRA can tax them as a shareholder benefit."),
    "Legal Disclaimers and Terms Related to Corporate Bank Accounts": BANNER,
    "Tips on Avoiding Common Corporate Bank Account Delays": callout("red", "Risk Warning", "Please keep your ISC register and corporate profile current. An outdated register, or a former director still on file, is a common reason banks pause onboarding and ask for full re-verification."),
}
AFTER_FAQ = callout("teal", "Worth Knowing", "Canada joined the Apostille Convention on January 11, 2024, so many foreign documents for non-resident directors can now be apostilled instead of going through consular legalization. Please ask your bank which format it accepts.")


def esc(s):
    return html.escape(s, quote=False)


def inline(s):
    parts, pos = [], 0
    for m in re.finditer(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", s):
        parts.append(plain(s[pos:m.start()]))
        text, url = m.group(1), m.group(2)
        a = f'<a href="{esc(url)}">{esc(text)}</a>'
        parts.append(f"<sup>{a}</sup>" if text.isdigit() else a)
        pos = m.end()
    parts.append(plain(s[pos:]))
    return "".join(parts)


def plain(s):
    out = esc(s)
    out = re.sub(r"(https://\S+?)(?=\.?$)", r'<a href="\1">\1</a>', out)
    out = re.sub(r"(\[\d\])(?!:)", r"<sup>\1</sup>", out)
    out = re.sub(r"(?<=[a-z]\.)(\d)$", r"<sup>\1</sup>", out)
    return out


def labelled(s):
    m = re.match(r"^([^:]{2,60}?): (.+)$", s)
    if m and "http" not in m.group(1) and not s.startswith("[") and len(m.group(1).split()) <= 6:
        return f"<strong>{inline(m.group(1))}:</strong> {inline(m.group(2))}"
    return inline(s)


def table(rows):
    head = rows.pop(0)
    t = ['<figure class="wp-block-table">', "<table>", "<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>", "<tbody>"]
    t += ["<tr>" + "".join(f"<td>{'<br>'.join(inline(p) for p in c.split(chr(10)))}</td>" for c in r + [""] * (len(head) - len(r))) + "</tr>" for r in rows]
    t += ["</tbody>", "</table>", "</figure>"]
    return "\n".join(t)


def numhead(h):
    n, i, label, colour, pill = SECTIONS[h]
    return (f"<h2>{esc(h)}</h2>\n<div class=\"gcpa-numhead\">\n<div class=\"num\" style=\"background:#0f2a4a !important;color:#ffffff !important;\">{n}</div>\n"
            f"<h4 id=\"{i}\" style=\"border:none;padding:0;margin:0;\">{esc(label)}</h4>\n<span class=\"gcpa-pill {colour}\">{esc(pill)}</span>\n</div>")


SMALL = '<p style="font-size:13.5px;color:#5a6b7b;margin:-6px 0 14px;">{}</p>'

# ---- parse the body ----
i = 0
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
        cur = ln if ln not in sections else f"{ln}#{len(order)}"
        order.append(cur)
        sections[cur] = []
        if cur in INFO:
            sections[cur].append(INFO[cur])
        i += 1
        if ln in LISTY:
            while not lines[i].strip():
                i += 1
            items = []
            while i < len(lines) and lines[i].strip() and lines[i].rstrip() not in LEVEL:
                items.append(lines[i].rstrip())
                i += 1
            tail = items.pop() if items and items[-1].startswith(TAILS) else None
            sections[cur].append("<ul>\n" + "\n".join(f"<li>{labelled(x)}</li>" for x in items) + "\n</ul>")
            if tail:
                sections[cur].append(f"<p>{labelled(tail)}</p>")
        continue
    if ln == "[References]":
        sections[cur].append('<p style="font-size:14px;margin:18px 0 6px;"><strong>[References]</strong></p>')
        i += 1
        while not lines[i].strip():
            i += 1
        items = []
        while i < len(lines) and lines[i].strip():
            items.append(lines[i].strip())
            i += 1
        sections[cur].append('<ul style="font-size:14px;">\n' + "\n".join(f"<li>{inline(x)}</li>" for x in items) + "\n</ul>")
        continue
    if ln.startswith("https://"):
        items = []
        while i < len(lines) and lines[i].startswith("https://"):
            u = lines[i].strip()
            items.append(f'<li><a href="{esc(u)}">{esc(u)}</a></li>')
            i += 1
        sections[cur].append('<ul style="font-size:14px;">\n' + "\n".join(items) + "\n</ul>")
        continue
    if ln.startswith("Option\tDescription"):
        rows = [ln.split("\t")]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("Verdict:"):
            x = lines[i].rstrip()
            if "\t" in x:
                rows.append(x.split("\t"))
            else:
                rows[-1][-1] += "\n" + x
            i += 1
        t = table([[c for c in r] for r in rows])
        sections[cur].append(t.replace("\n<br>", "<br>"))
        continue
    if ln.endswith("?") and ln not in LEVEL:
        sections[cur].append(f"<p><strong>{inline(ln)}</strong></p>")
        i += 1
        continue
    if ln == "--- References":
        ln = "References"
        lines[i] = ln
        continue
    if re.match(r"^\[[¹²³⁴⁵⁶⁷]", ln) or re.match(r"^\[\d\]: ", ln) or ln.startswith("*Data"):
        sections[cur].append(SMALL.format(inline(ln)))
        i += 1
        continue
    m = re.match(r"^\[\^(\d+)\]: (.+)$", ln)
    if m:
        notes.append((m.group(1), m.group(2)))
        i += 1
        if not any(re.match(r"^\[\^\d+\]: ", l) for l in lines[i:i + 3]):
            sections[cur].append(f'<p style="font-size:14px;margin:18px 0 6px;"><strong>Sources</strong></p>\n<ol start="{notes[0][0]}" style="font-size:14px;">\n'
                                 + "\n".join(f"<li>{esc(n)}</li>" for _, n in notes) + "\n</ol>")
            notes = []
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
        if ended_by == "blank" and len(block) >= 3 and len(block[-1].split()) >= 12:
            closer = block.pop()
        if len(block) == 1 or (len(block) == 2 and len(ln.split()) <= 3):
            sections[cur].extend(f"<p>{labelled(x)}</p>" for x in block)
        elif block:
            sections[cur].append("<ul>\n" + "\n".join(f"<li>{labelled(x)}</li>" for x in block) + "\n</ul>")
        if closer:
            sections[cur].append(f"<p>{labelled(closer)}</p>")
        continue
    sections[cur].append(f"<p>{labelled(ln)}</p>")
    i += 1

# ---- links ----
SITE = r'<a [^>]*href="https://(opencorporationfor35\.ca/(?!wp-content)|gondaliyacpa\.ca/)'
INTRO_HTML = f"<p><strong>Open Corporation for $35 is a department of Gondaliya CPA.</strong> {esc(INTRO)}</p>"


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
for key in order[1:]:
    h = key.split("#")[0]
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
        parts.append(AFTER_FAQ)
    parts.extend(sections[key])
BODY = "\n".join(parts)

HEAD = open(f"{HERE}/head.html", encoding="utf-8").read().replace("@@INTRO@@", INTRO_HTML)
A = HEAD + "\n" + BODY + "\n" + open(f"{HERE}/tail.html", encoding="utf-8").read()
tpl = open(f"{HERE}/template.html", encoding="utf-8").read()
B = open(f"{HERE}/widget.html", encoding="utf-8").read()
C = open(f"{HERE}/closing.html", encoding="utf-8").read()
page = re.sub(r'<div class="gcpa-hero"[\s\S]*?(?=<div id="ocf-chk">)', lambda m: A + "\n", tpl, count=1)
page = re.sub(r'<div class="s-head"[\s\S]*?(?=<button type="button" class="s-go")', lambda m: B, page, count=1)
page = re.sub(r'<div class="gcpa-cta"[^>]*>\s*<h4>Incorporate for \$35, HST included[\s\S]*$', lambda m: C, page, count=1)
assert "@@JSON@@" in page and "Corporate Bank Account Readiness Check" in page

ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "BlogPosting", "@id": f"{OC}{SLUG}/#article", "headline": H1,
     "description": DESC,
     "datePublished": ISO, "dateModified": ISO, "author": {"@type": "Person", "name": "Sharad Gondaliya, CPA"},
     "image": UP + FEATURED,
     "publisher": {"@type": "Organization", "name": "Open Corporation for $35", "description": "Open Corporation for $35 is a department of Gondaliya CPA.",
                   "parentOrganization": {"@type": "AccountingService", "name": "Gondaliya CPA Professional Corporation", "identifier": "CPA Ontario Firm Registration 61330051"}},
     "mainEntityOfPage": f"{OC}{SLUG}/"},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
page = page.replace("@@JSON@@", '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False) + "\n</script>")
words = len(re.sub("<[^>]+>", " ", html.unescape(re.sub(r"<(style|script)[^>]*>.*?</\1>", "", page, flags=re.S))).split())
page = page.replace("@@READ@@", str(round(words / 220)))
open(f"{HERE}/post.html", "w", encoding="utf-8").write(page)
open(f"{HERE}/headings.txt", "w", encoding="utf-8").write("\n".join([H1, H2SEO] + [k.split("#")[0] for k in order[1:]]) + "\n")
print("words", words, "reading", round(words / 220), "faq", len(faq), "sections", len(order) - 1, "bytes", len(page))
