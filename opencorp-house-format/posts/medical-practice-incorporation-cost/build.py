#!/usr/bin/env python3
"""Build post.html for the medical practice incorporation cost post from source.md + corrections.json.

Body text comes from the draft (with approved corrections); house elements, links,
callouts and infographics are added from the tables below. The page shell comes from
template.html (the why-35-fee post as first built).
"""
import html, json, re

HERE = __file__.rsplit("/", 1)[0] or "."
src = open(f"{HERE}/source.md", encoding="utf-8").read()
for c in json.load(open(f"{HERE}/corrections.json", encoding="utf-8")):
    src = src.replace(c["from"], c["to"])
lines = src.splitlines()[1:]

H1 = "Cost to Incorporate a Medical Practice in Canada by Province"
H2SEO = "Cost to Incorporate Medical Practice in Canada: Understanding Doctor Incorporation and Physician Professional Corporation Costs by Province"
ISO = "2026-11-18"
SLUG = "cost-to-incorporate-medical-practice-canada-by-province"
OC = "https://opencorporationfor35.ca/"
UP = OC + "wp-content/uploads/2026/11/"
DIR = "medical-practice-incorporation-cost"
FEATURED = "Medical-Practice-Incorporation-Cost-Featured.jpg"
DESC = "Cost to incorporate a medical practice in Canada by province: CPSO, CPSBC and CPSA fees, registry and NUANS costs, yearly renewals, and when a physician professional corporation pays."

SECTIONS = {
    "What Incorporation Means for Medical Practices in Canada": (1, "toc-meaning", "What Incorporation Means", "blue", "The Basics"),
    "Advantages of Medical Practice Incorporation: Tax Deferral, Income Splitting, and Liability Protection": (2, "toc-advantages", "Advantages and Drawbacks", "teal", "Pros and Cons"),
    "Step-by-Step Guide to Setting Up a Physician Professional Corporation": (3, "toc-steps", "Setting Up Step by Step", "gold", "Setup"),
    "Financial Insights and Cost Breakdown by Province": (4, "toc-costs", "Cost Breakdown by Province", "green", "Costs"),
    "When Should Physicians Consider Incorporation Based on Career Phase?": (5, "toc-timing", "When to Incorporate", "red", "Timing"),
    "Frequently Asked Questions Addressing Incorporation Eligibility, Naming, Shareholders, and Renewal": (6, "toc-eligibility", "Eligibility and Support", "blue", "Eligibility"),
    "Frequently Asked Questions (FAQs)": (7, "toc-faq", "Frequently Asked Questions", "teal", "FAQ"),
    "Key Points: Medical Practice Incorporation Costs & Compliance": (8, "toc-keypoints", "Key Points", "gold", "Summary"),
}
H3 = """Understanding Physician Professional Corporations (PCs) and Their Legal Structure
Differences Between Individual Practice and Professional Corporation
Ownership, Shareholder Roles, and Legal Responsibilities in Medical PCs
Why Physicians Consider Incorporation: Overview of Financial and Legal Motivations
Potential Disadvantages: Administrative Burden, Costs, and Restrictions on Funds Retention
Balancing Financial Benefits and Operational Challenges for Physicians
How Incorporation Impacts Retirement Planning and Practice Succession
Provincial Variations in Benefits and Regulatory Environment
Choosing a Name and Business Structure
Filing Articles of Incorporation and Obtaining Provincial Approval
Acquiring Necessary Practice Permits and Registrations
Procedures for Updating Your PC: Address, Shareholders, and Corporate Structure
How to Amend the Name or Structure of a Medical PC
Amalgamating Multiple Professional Corporations: Process and Considerations
Closing a Medical Practice Corporation: Legal and Financial Implications
Reviving a Dormant or Closed Professional Corporation: Steps and Requirements
Transparent Overview of Incorporation Costs Across Canadian Provinces
Initial Registration Fees, Annual Maintenance Costs, and Other Administrative Expenses
Tax Considerations Unique to Physician PCs: Deferrals, Passive Income Rules, and TOSI Screening
Remuneration Strategies for Physicians: Salary, Dividends, and Bonuses Explained
Cost Comparison Tables Highlighting Provincial Differences and Typical Expense Ranges
Timing strategies for incorporation decisions
Advice for New Physicians: Financial Literacy and Timing for Incorporation
Considerations for Retired Physicians, Medical Students, and Licensed Practitioners on Work Permits
Common Challenges and Potential Snags: Passive Income Traps, Corporate Structure Complexities, and Compliance Risks
Planning for Practice Sale or Transition: Section 85 Rollover and Capital Gains Strategies
Provincial Registration and Regulatory Bodies: CPSA, CPSO, Alberta Health, and Others
Importance of Specialized Accounting and Legal Advice for Medical Professional Corporations
How to Access Professional Support and Guidance for Incorporation and Ongoing Compliance
Encouraging Contact with Experts for Personalized Incorporation Planning and Review
Related Reading and Tools for Managing Your Medical Practice Incorporation Effectively""".splitlines()
H4 = """Making Business Address or Shareholder Changes
Managing Changes in Organizational Structure
Early-career tips for maximizing benefits
Unique issues for special career situations
Mistakes to avoid when managing a professional corporation""".splitlines()
H5 = ["References"]
LEVEL = {**{h: 2 for h in SECTIONS}, **{h: 3 for h in H3}, **{h: 4 for h in H4}, **{h: 5 for h in H5}}
LISTY = {"Key Points: Medical Practice Incorporation Costs & Compliance", "Mistakes to avoid when managing a professional corporation", "References"}
FAQ_H = "Frequently Asked Questions (FAQs)"

LINKS = {
    "_intro": ("physician professional corporation", OC + "professional-corporation-incorporation/"),
    "What Incorporation Means for Medical Practices in Canada": ("legal company separate from yourself", OC + "convert-sole-proprietorship-corporation/"),
    "Understanding Physician Professional Corporations (PCs) and Their Legal Structure": ("limited liability", OC + "guides/professional-corporations-ontario/"),
    "Ownership, Shareholder Roles, and Legal Responsibilities in Medical PCs": ("keep good financial records", OC + "incorporation-bookkeeping-bundle/"),
    "Why Physicians Consider Incorporation: Overview of Financial and Legal Motivations": ("Retirement Planning", OC + "guides/holding-company-canada/"),
    "Advantages of Medical Practice Incorporation: Tax Deferral, Income Splitting, and Liability Protection": ("TOSI (Tax on Split Income)", OC + "guides/tax-on-split-income/"),
    "Potential Disadvantages: Administrative Burden, Costs, and Restrictions on Funds Retention": ("file corporate taxes (T2)", OC + "corporate-tax-filing-from-300/"),
    "Balancing Financial Benefits and Operational Challenges for Physicians": ("12.2% combined small business rate", OC + "guides/small-business-deduction/"),
    "How Incorporation Impacts Retirement Planning and Practice Succession": ("non-voting share classes", OC + "guides/share-structure-explained/"),
    "Provincial Variations in Benefits and Regulatory Environment": ("physician corporations across Canada", OC + "guides/cost-to-incorporate-in-canada/"),
    "References": ("contact Open Corporation", OC + "contact-us/"),
    "Step-by-Step Guide to Setting Up a Physician Professional Corporation": ("follow the rules", OC + "guides/incorporation-documents-checklist/"),
    "Choosing a Name and Business Structure": ("NUANS Name Search", OC + "nuans-report-20/"),
    "Filing Articles of Incorporation and Obtaining Provincial Approval": ("Ontario Business Registry charges $300", OC + "how-to-incorporate-in-ontario/"),
    "Procedures for Updating Your PC: Address, Shareholders, and Corporate Structure": ("inform both the corporate registry", OC + "corporate-changes-amendments/"),
    "Making Business Address or Shareholder Changes": ("registered office", OC + "guides/registered-office-address/"),
    "Managing Changes in Organizational Structure": ("adding new share classes", OC + "share-issuance-transfer/"),
    "How to Amend the Name or Structure of a Medical PC": ("board resolutions", OC + "minute-book-preparation/"),
    "Transparent Overview of Incorporation Costs Across Canadian Provinces": ("In British Columbia", OC + "how-to-incorporate-in-british-columbia/"),
    "Initial Registration Fees, Annual Maintenance Costs, and Other Administrative Expenses": ("Corporate Annual Return Filing", OC + "annual-return-filing/"),
    "Tax Considerations Unique to Physician PCs: Deferrals, Passive Income Rules, and TOSI Screening": ("small business deduction", OC + "guides/small-business-deduction/"),
    "Remuneration Strategies for Physicians: Salary, Dividends, and Bonuses Explained": ("Salary Payments", OC + "guides/salary-vs-dividends/"),
    "Cost Comparison Tables Highlighting Provincial Differences and Typical Expense Ranges": ("Open Corporation for $35 is part of Gondaliya CPA", OC + "pricing/"),
    "When Should Physicians Consider Incorporation Based on Career Phase?": ("nearing retirement", OC + "guides/lifetime-capital-gains-exemption/"),
    "Timing strategies for incorporation decisions": ("Talking with a CPA", "https://gondaliyacpa.ca/consultation/"),
    "Early-career tips for maximizing benefits": ("Use free CPA advice like Open Corporation for $35", OC + "incorporation-service-35/"),
    "Unique issues for special career situations": ("Licensed practitioners on work permits", OC + "open-a-corporation-in-canada-on-a-work-permit/"),
    "Common Challenges and Potential Snags: Passive Income Traps, Corporate Structure Complexities, and Compliance Risks": ("yearly filings", OC + "corporate-compliance-subscription/"),
    "Mistakes to avoid when managing a professional corporation": ("GST/HST rules", OC + "guides/hst-registration-guide/"),
    "Planning for Practice Sale or Transition: Section 85 Rollover and Capital Gains Strategies": ("Section 85 rollovers", OC + "guides/section-85-rollover/"),
    "Frequently Asked Questions Addressing Incorporation Eligibility, Naming, Shareholders, and Renewal": ("Only licensed doctors in good standing", OC + "professional-corporation-incorporation/"),
    "Provincial Registration and Regulatory Bodies: CPSA, CPSO, Alberta Health, and Others": ("registry fees", OC + "guides/cost-to-incorporate-in-canada/"),
    "Importance of Specialized Accounting and Legal Advice for Medical Professional Corporations": ("CPA firms", OC + "services/"),
    "Related Reading and Tools for Managing Your Medical Practice Incorporation Effectively": ("one-time vs recurring fees", OC + "first-year-filing-calendar-new-corporation/"),
    "Key Points: Medical Practice Incorporation Costs & Compliance": ("T2 filings", OC + "guides/first-t2-return/"),
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
<h4>Does incorporating pay at your income?</h4>
<p>Incorporation from $35 including HST plus government and college fees, with a free CPA consultation on your college application, share structure, and whether the tax deferral covers the yearly cost. Please book a free consultation.</p>
<div class="gcpa-trust"><span>1300+ 5-star Google reviews</span><span>Xero Partner Award Winner 2026</span><span>CPA Ontario Firm 61330051</span><span>30-Day Money-Back Guarantee</span></div>
<div class="gcpa-btnrow"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="https://opencorporationfor35.ca/">Open Corporation For $35</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BANNER = """<div class="gcpa-banner" style="background:linear-gradient(135deg,#0d3b66 0%,#0c7a7a 100%) !important;">
<div class="bt">Thinking about a medical professional corporation? Please book a free consultation and we will run your numbers and the college steps for your province with you.</div>
<div class="bb"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="mailto:info@gondaliyacpa.ca">info@gondaliyacpa.ca</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BEFORE = {
    "Ownership, Shareholder Roles, and Legal Responsibilities in Medical PCs": callout("teal", "Key Stat", "<strong>$725:</strong> first-year government and college fees for an Ontario medical professional corporation: the CPSO certificate at $400, the Ontario Business Registry at $300 and a $25 NUANS report."),
    "Why Physicians Consider Incorporation: Overview of Financial and Legal Motivations": callout("blue", "Worth Knowing", "In Ontario, family members can hold non-voting shares of a medicine professional corporation, but dividends paid to them are usually caught by TOSI unless an exception applies, such as a spouse once the physician is 65 or older."),
    "Balancing Financial Benefits and Operational Challenges for Physicians": callout("gold", "Our Actual Experience", "The step physicians most often get out of order is billing. The corporation cannot bill OHIP until the CPSO certificate is issued and the billing number is linked, so we file the articles and prepare the CPSO application together and ask clients not to switch billing until both are done."),
    "Acquiring Necessary Practice Permits and Registrations": callout("red", "Risk Warning", "Please do not bill through the corporation before the college has issued its certificate or permit. Claims billed to the corporation before approval can be refused, and correcting them takes weeks."),
    "Financial Insights and Cost Breakdown by Province": CTA_MID,
    "Remuneration Strategies for Physicians: Salary, Dividends, and Bonuses Explained": callout("red", "Risk Warning", "Please keep personal and corporate money apart. Personal costs paid from the corporation without being recorded as salary, dividends or a shareholder loan can be taxed as a benefit under the Income Tax Act."),
    "Encouraging Contact with Experts for Personalized Incorporation Planning and Review": BANNER,
    "Planning for Practice Sale or Transition: Section 85 Rollover and Capital Gains Strategies": callout("red", "Risk Warning", "A missed college renewal can lead to a revoked certificate or permit. Please diarize the date: the CPSO renewal falls on the certificate's issue date, the CPSBC permit renews each March 1 and the CPSA renewal is due December 31."),
}
AFTER_FAQ = callout("teal", "Worth Knowing", "The fees in this article are government and college charges only. Please budget separately for bookkeeping and the yearly T2 return, which usually cost more than the college renewal.")


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
    out = re.sub(r"(https://laws-lois\.justice\.gc\.ca/\S+?)(?=\.?$)", r'<a href="\1">\1</a>', out)
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
    t += ["<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r + [""] * (len(head) - len(r))) + "</tr>" for r in rows]
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
            tail = items.pop() if items and items[-1].startswith(("Open Corporation for $35 offers", "If you want personalized", "Avoiding these mistakes")) else None
            sections[cur].append("<ul>\n" + "\n".join(f"<li>{labelled(x)}</li>" for x in items) + "\n</ul>")
            if tail:
                sections[cur].append(f"<p>{labelled(tail)}</p>")
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
        if ended_by == "blank" and len(block) >= 3 and len(block[-1].split()) >= 14:
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
        parts.append(AFTER_FAQ)
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
assert "@@JSON@@" in page and "Medical Professional Corporation Readiness Check" in page

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
open(f"{HERE}/headings.txt", "w", encoding="utf-8").write("\n".join([H1, H2SEO] + order[1:]) + "\n")
print("words", words, "reading", round(words / 220), "faq", len(faq), "sections", len(order) - 1, "bytes", len(page))
