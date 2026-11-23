#!/usr/bin/env python3
"""Build post.html for the side business incorporation post from source.md + corrections.json."""
import html, json, re

HERE = __file__.rsplit("/", 1)[0] or "."
src = open(f"{HERE}/source.md", encoding="utf-8").read()
for c in json.load(open(f"{HERE}/corrections.json", encoding="utf-8")):
    src = src.replace(c["from"], c["to"])
lines = src.splitlines()[1:]

H1 = "Incorporating a Side Business While Employed in Ontario: Tax Benefits, Costs & CRA Rules"
H2SEO = "Incorporating a Side Business While Employed in Ontario: Tax Implications, Costs, and CRA Rules Explained by Open Corporation for $35"
ISO = "2026-11-23"
SLUG = "incorporating-side-business-while-employed-ontario"
OC = "https://opencorporationfor35.ca/"
UP = OC + "wp-content/uploads/2026/11/"
DIR = "side-business-incorporation-ontario"
FEATURED = "Side-Business-Incorporation-Ontario-Featured.jpg"
DESC = "Incorporating a side business while employed in Ontario: when it pays, the $300 filing fee, 12.2% small business rate, CPP on corporate salary, start-up losses, personal services business risk and your employment contract."

SECTIONS = {
    "Who Should Consider Incorporating a Side Business While Employed in Ontario": (1, "toc-who", "Who Should Consider It", "blue", "Fit"),
    "How Incorporating a Side Business Works Under Ontario Law": (2, "toc-law", "How It Works in Ontario", "teal", "The Law"),
    "Tax Implications of Operating a Side Business as Sole Proprietor or Corporation in Ontario": (3, "toc-tax", "Tax Implications", "gold", "Tax"),
    "Cost Comparison: Running a Sole Proprietorship vs. Incorporated Side Business in Ontario": (4, "toc-costs", "Cost Comparison", "green", "Costs"),
    "Step-by-Step Process to Incorporate a Side Business in Ontario": (5, "toc-steps", "Step-by-Step Process", "red", "Setup"),
    "Comparing Reporting Side Business Income Personally Versus Through a Corporation": (6, "toc-reporting", "Reporting, Losses and Risks", "blue", "Reporting"),
    "Frequently Asked Questions (FAQs)": (7, "toc-faq", "Frequently Asked Questions", "teal", "FAQ"),
    "Quick Answers — TL;DR": (8, "toc-quick", "Quick Answers and Next Steps", "gold", "Summary"),
}
H3 = """Understanding Your Default Status: Sole Proprietorship for Side Businesses
When Incorporation Becomes Advantageous for Your Side Business
Reviewing Employment Contracts: Conflicts, Moonlighting, and Non-Compete Clauses
Separating Personal and Business Finances for Liability and Compliance
Key Differences Between Sole Proprietorship and Incorporation for Side Businesses
Liability Protection: Unlimited Personal Liability vs. Limited Corporate Liability
Maintaining the Corporate Veil: Compliance and Record-Keeping Requirements
Impact of Incorporation on Your Employment Status and Obligations
Personal Tax Rates Compared to Corporate Small Business Tax Rates
Benefits and Limitations of the Small Business Deduction for Incorporated Side Businesses
Understanding Personal Services Business Rules and Their Effect on Taxation
Tax Planning Strategies: Salary, Dividends, and CPP Contributions from Your Corporation
Ontario Incorporation Costs, Government Filing Fees, and Annual Compliance Expenses
Ongoing Corporate Filings and Reporting Requirements Including T2, Payroll, and GST/HST
Accounting, Legal, and Professional Review Costs for Incorporated Side Businesses
Financial Considerations When Transitioning from Sole Proprietorship to Corporation
Preparing and Filing the Articles of Incorporation and NUANS Name Search
Registering for GST/HST and Other Required Business Accounts
Setting Up Corporate Governance: Registered Office, Directors, and Share Structure
Managing Corporate Records and Meeting Annual Filing Deadlines
Handling Start-Up Losses, Home Office, and Vehicle Expenses for Tax Purposes
When a Side Hustle is Large Enough to Justify Incorporation
Risks and Audit Considerations Regarding Side Business Incorporation and CRA Assessments
Guidance on Working with Professionals for Incorporation and Tax Planning in Ontario
DIY vs Lawyer vs CPA: Choosing Professional Help
How We Review a Side Business Incorporation for Clients
What Deliverables Do You Get?
What Are the Risks, Compliance Issues and Prevention Controls?
What Should You Prepare Before Meeting a CPA?
How Do Side Businesses Differ Across the 10 Industries We Serve?
A Realistic Numeric Walkthrough
How Should You Choose a CPA for a Side Business?
Why Trust Open Corporation for $35 (a department of Gondaliya CPA)?
People Also Ask
Glossary
Next Steps
Sources & References""".splitlines()
H4 = """Legal Status
Tax Treatment
Liability
Compliance
Losses""".splitlines()
H5 = ["References"]
LEVEL = {**{h: 2 for h in SECTIONS}, **{h: 3 for h in H3}, **{h: 4 for h in H4}, **{h: 5 for h in H5}}
LISTY = {"References", "DIY vs Lawyer vs CPA: Choosing Professional Help", "People Also Ask", "Glossary", "Next Steps", "Sources & References"}
TAILS = ("Open Corporation for $35 is a department", "For employees incorporating", "Call 647")
FAQ_H = "Frequently Asked Questions (FAQs)"

LINKS = {
    "_intro": ("incorporation costs", OC + "guides/cost-to-incorporate-in-canada/"),
    "Who Should Consider Incorporating a Side Business While Employed in Ontario": ("E-commerce Entrepreneurs", OC + "incorporation-service-35/"),
    "Understanding Your Default Status: Sole Proprietorship for Side Businesses": ("sole proprietorships by default", OC + "sole-proprietorship-registration/"),
    "When Incorporation Becomes Advantageous for Your Side Business": ("Small Business Deduction (SBD)", OC + "guides/small-business-deduction/"),
    "Separating Personal and Business Finances for Liability and Compliance": ("Open separate bank accounts", OC + "business-bank-account-setup/"),
    "How Incorporating a Side Business Works Under Ontario Law": ("Ontario Business Registry", OC + "how-to-incorporate-in-ontario/"),
    "Key Differences Between Sole Proprietorship and Incorporation for Side Businesses": ("sole proprietorship vs corporation for a side business", OC + "convert-sole-proprietorship-corporation/"),
    "Liability Protection: Unlimited Personal Liability vs. Limited Corporate Liability": ("pierce the veil", OC + "guides/minute-book-requirements/"),
    "Maintaining the Corporate Veil: Compliance and Record-Keeping Requirements": ("registered office service", OC + "address-service-100/"),
    "Impact of Incorporation on Your Employment Status and Obligations": ("payroll remittances", OC + "payroll-service/"),
    "Tax Implications of Operating a Side Business as Sole Proprietor or Corporation in Ontario": ("its own tax return (T2)", OC + "corporate-tax-filing-from-300/"),
    "Personal Tax Rates Compared to Corporate Small Business Tax Rates": ("small business deduction (SBD)", OC + "guides/small-business-deduction/"),
    "Benefits and Limitations of the Small Business Deduction for Incorporated Side Businesses": ("Associated corporations", OC + "guides/holding-company-canada/"),
    "Understanding Personal Services Business Rules and Their Effect on Taxation": ("check with a CPA", "https://gondaliyacpa.ca/consultation/"),
    "Tax Planning Strategies: Salary, Dividends, and CPP Contributions from Your Corporation": ("Paying yourself wages", OC + "guides/salary-vs-dividends/"),
    "Cost Comparison: Running a Sole Proprietorship vs. Incorporated Side Business in Ontario": ("send annual returns to the Ontario Business Registry", OC + "annual-return-filing/"),
    "Ontario Incorporation Costs, Government Filing Fees, and Annual Compliance Expenses": ("Registered Office Fees", OC + "guides/registered-office-address/"),
    "Ongoing Corporate Filings and Reporting Requirements Including T2, Payroll, and GST/HST": ("register for payroll accounts", OC + "guides/payroll-setup-new-corporation/"),
    "Accounting, Legal, and Professional Review Costs for Incorporated Side Businesses": ("CPAs offer tax-focused advice", OC + "services/"),
    "Financial Considerations When Transitioning from Sole Proprietorship to Corporation": ("Open Corporation charges about $35", OC + "pricing/"),
    "Step-by-Step Process to Incorporate a Side Business in Ontario": ("keeping up with legal requirements", OC + "guides/incorporation-documents-checklist/"),
    "Preparing and Filing the Articles of Incorporation and NUANS Name Search": ("NUANS report", OC + "nuans-report-20/"),
    "Registering for GST/HST and Other Required Business Accounts": ("small supplier threshold", OC + "guides/hst-registration-guide/"),
    "Setting Up Corporate Governance: Registered Office, Directors, and Share Structure": ("Share Structure", OC + "guides/share-structure-explained/"),
    "Managing Corporate Records and Meeting Annual Filing Deadlines": ("Maintain minute books", OC + "minute-book-preparation/"),
    "Comparing Reporting Side Business Income Personally Versus Through a Corporation": ("own T2 tax return", OC + "guides/first-t2-return/"),
    "Handling Start-Up Losses, Home Office, and Vehicle Expenses for Tax Purposes": ("home office expenses", OC + "incorporation-bookkeeping-bundle/"),
    "Guidance on Working with Professionals for Incorporation and Tax Planning in Ontario": ("setting up BN/GST accounts", OC + "business-number-cra-account-registration/"),
    "Quick Answers — TL;DR": ("liability protection or tax deferral", OC + "guides/what-happens-after-you-incorporate/"),
    "DIY vs Lawyer vs CPA: Choosing Professional Help": ("CPAs specialize in tax planning", OC + "corporate-compliance-subscription/"),
    "How We Review a Side Business Incorporation for Clients": ("We handle NUANS name searches", OC + "named-company-incorporation-nuans/"),
    "What Deliverables Do You Get?": ("Corporate minute book templates", OC + "minute-book-preparation/"),
    "Next Steps": ("Use services like Open Corporation for $35", OC + "incorporation-form/"),
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
<h4>Does incorporating your side business pay yet?</h4>
<p>Incorporation from $35 including HST plus government fees, with a free CPA consultation on your contract, the personal services business test, CPP on salary, and whether your profit is high enough. Please book a free consultation.</p>
<div class="gcpa-trust"><span>1300+ 5-star Google reviews</span><span>Xero Partner Award Winner 2026</span><span>CPA Ontario Firm 61330051</span><span>30-Day Money-Back Guarantee</span></div>
<div class="gcpa-btnrow"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="https://opencorporationfor35.ca/">Open Corporation For $35</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BANNER = """<div class="gcpa-banner" style="background:linear-gradient(135deg,#0d3b66 0%,#0c7a7a 100%) !important;">
<div class="bt">Running a side business next to your job? Please book a free consultation and we will tell you whether to incorporate now or wait.</div>
<div class="bb"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="mailto:info@gondaliyacpa.ca">info@gondaliyacpa.ca</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BEFORE = {
    "Reviewing Employment Contracts: Conflicts, Moonlighting, and Non-Compete Clauses": callout("teal", "Key Stat", "<strong>12.2%:</strong> Ontario's combined small business rate on the first $500,000 of active business income in 2026, against a top personal rate of 53.53% on income over $258,482."),
    "Maintaining the Corporate Veil: Compliance and Record-Keeping Requirements": callout("blue", "Worth Knowing", "An Ontario corporation's annual return has no fee and is filed through the Ontario Business Registry within six months after year-end. The T2 return is due on the same six-month timeline, even in a year with no income."),
    "Benefits and Limitations of the Small Business Deduction for Incorporated Side Businesses": callout("gold", "Our Actual Experience", "The question we hear most from employees is whether their corporation can skip CPP because their job already maxed it. It cannot: salary from your own corporation attracts CPP again, so for employees who already max out CPP at work we usually look at dividends first."),
    "Tax Planning Strategies: Salary, Dividends, and CPP Contributions from Your Corporation": callout("red", "Risk Warning", "If your side corporation works mainly for one client who controls your hours and tools, the CRA can treat it as a personal services business and tax its income at 44.5% in Ontario. Please have the client relationship reviewed before you incorporate."),
    "Cost Comparison: Running a Sole Proprietorship vs. Incorporated Side Business in Ontario": CTA_MID,
    "Financial Considerations When Transitioning from Sole Proprietorship to Corporation": callout("red", "Risk Warning", "Please do not pay personal costs from the corporate account. Money taken out without being recorded as salary, dividends or a repaid loan can be taxed as a shareholder benefit or loan under the Income Tax Act."),
    "When a Side Hustle is Large Enough to Justify Incorporation": callout("red", "Risk Warning", "Losses inside a corporation cannot reduce the tax on your salary. If your side business will lose money in its first year or two, please consider staying a sole proprietor until it turns a profit, so the losses reduce your employment income instead."),
    "Guidance on Working with Professionals for Incorporation and Tax Planning in Ontario": BANNER,
}
AFTER_FAQ = callout("teal", "Worth Knowing", "The $30,000 GST/HST threshold counts the taxable sales of associated businesses together. Please add up every business you and your corporation run before deciding you are under it.")


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
while not lines[i].startswith("TLDR:"):
    i += 1
INTRO = lines[i][len("TLDR:"):].strip()
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
assert "@@JSON@@" in page and "Side Business Incorporation Readiness Check" in page

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
