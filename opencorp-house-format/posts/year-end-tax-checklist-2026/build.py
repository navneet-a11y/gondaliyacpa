#!/usr/bin/env python3
"""Build post.html for the year-end tax checklist 2026 post from source.md + corrections.json."""
import html, json, re

HERE = __file__.rsplit("/", 1)[0] or "."
src = open(f"{HERE}/source.md", encoding="utf-8").read()
for c in json.load(open(f"{HERE}/corrections.json", encoding="utf-8")):
    src = src.replace(c["from"], c["to"])
lines = src.splitlines()[1:]

H1 = "Year-End Tax Checklist for Incorporated Business Owners (December 2026)"
H2SEO = "Corporate Year-End Tax Checklist 2026: Year-End Tax Planning for Incorporated Business Owners with Salary vs Dividends, RRSP Room, and December Tax Planning Canada"
ISO = "2026-11-23"
SLUG = "year-end-tax-checklist-incorporated-business-owners-2026"
OC = "https://opencorporationfor35.ca/"
UP = OC + "wp-content/uploads/2026/11/"
DIR = "year-end-tax-checklist-2026"
FEATURED = "Year-End-Tax-Checklist-2026-Featured.jpg"
DESC = "Corporate year-end tax checklist for December 2026: dividends by December 31, accrued bonus within 180 days, CPP and RRSP limits, T4 and T5 slips by March 1, 2027, instalments, shareholder loans and the T2."

SECTIONS = {
    "Understanding Your Business Year-End and Tax Deadlines in Canada": (1, "toc-deadlines", "Year-End and Deadlines", "blue", "Deadlines"),
    "Preparing and Organizing Financial Records for Year-End Tax Filing": (2, "toc-records", "Records and Bookkeeping", "teal", "Records"),
    "Reviewing Income, Deductions, and Expenses Before Year-End": (3, "toc-income", "Income, Expenses and CCA", "gold", "Deductions"),
    "Salary, Dividends, and Bonus Planning for Incorporated Business Owners": (4, "toc-pay", "Salary, Dividends and Bonus", "green", "Pay Yourself"),
    "Managing Payroll, GST/HST, and Instalment Payments": (5, "toc-payments", "Payroll, GST/HST and Instalments", "red", "Payments"),
    "Strategic Year-End Moves and Planning for the Coming Year": (6, "toc-strategy", "Strategic Year-End Moves", "blue", "Strategy"),
    "Frequently Asked Questions (FAQs)": (7, "toc-faq", "Frequently Asked Questions", "teal", "FAQ"),
    "Key Corporate Year-End Reminders from Open Corporation for $35": (8, "toc-reminders", "Reminders and Next Steps", "gold", "Summary"),
}
H3 = """Defining Your Corporation’s Fiscal Year-End
Key CRA Deadlines for Filing and Payments by December 31, 2026 and Early 2027
Overview of T2 Filing, T4 Slip Submission, and Annual Return Requirements
Gathering Necessary Documentation and Financial Statements
Completing Year-End Bookkeeping and Reconciliation Steps
Using Accounting Software to Streamline Bookkeeping Tasks
Assessing Corporate Income and Eligible Deductions
Timing Purchases and Capital Asset Acquisitions for Tax Benefits
Applying the Capital Cost Allowance, Half-Year Rule, and Accelerated Investment Incentive in 2026
Evaluating Salary vs Dividends to Optimize Tax Outcomes
Accrued Bonus Rules and Payment Deadlines for Deductibility
Understanding TOSI Screening and Shareholder Loan Implications
Ensuring Accurate Payroll Source Deductions and CPP Contributions
Final GST/HST Remittance and Reporting Obligations
Reviewing Corporate Instalments Due Dates and Amounts
Monitoring Passive Income Levels and Small Business Deduction Impact
Clearing Shareholder Loans and Updating Minute Book Resolutions
Considering RRSP Contribution Room, TFSA, FHSA, and Other Registered Accounts
Addressing Common Year-End Tax Errors and Edge Cases
Summary of Critical 2026 Tax Rates and Thresholds Affecting Year-End Decisions
Next Steps""".splitlines()
H4 = """T2 Corporate Return
T4/T5 Slips
Ontario Business Registry Annual Return
Corporate Instalments Due Dates""".splitlines()
H5 = []
LEVEL = {**{h: 2 for h in SECTIONS}, **{h: 3 for h in H3}, **{h: 4 for h in H4}}
LISTY = {"Key Corporate Year-End Reminders from Open Corporation for $35", "Next Steps"}
TAILS = ("For expert guidance", "Reach out today")
FAQ_H = "Frequently Asked Questions (FAQs)"

LINKS = {
    "_intro": ("salary vs dividends strategies", OC + "guides/salary-vs-dividends/"),
    "Defining Your Corporation’s Fiscal Year-End": ("fiscal year-end is really important", OC + "guides/fiscal-year-end/"),
    "Key CRA Deadlines for Filing and Payments by December 31, 2026 and Early 2027": ("T2 Corporate Return Filing Deadline", OC + "corporate-tax-filing-from-300/"),
    "T2 Corporate Return": ("Shows all income", OC + "guides/first-t2-return/"),
    "T4/T5 Slips": ("T4 reports employee income", OC + "payroll-service/"),
    "Ontario Business Registry Annual Return": ("file this yearly with ServiceOntario", OC + "annual-return-filing/"),
    "Preparing and Organizing Financial Records for Year-End Tax Filing": ("finish bookkeeping", OC + "incorporation-bookkeeping-bundle/"),
    "Gathering Necessary Documentation and Financial Statements": ("GST/HST filings", OC + "guides/hst-registration-guide/"),
    "Completing Year-End Bookkeeping and Reconciliation Steps": ("Ontario Business Registry annual returns", OC + "guides/corporate-annual-return/"),
    "Using Accounting Software to Streamline Bookkeeping Tasks": ("CPA firms that help incorporated businesses", OC + "services/"),
    "Reviewing Income, Deductions, and Expenses Before Year-End": ("missed opportunities for tax savings", OC + "guides/small-business-deduction/"),
    "Assessing Corporate Income and Eligible Deductions": ("Employee salaries (including owner-managers)", OC + "guides/payroll-setup-new-corporation/"),
    "Applying the Capital Cost Allowance, Half-Year Rule, and Accelerated Investment Incentive in 2026": ("Open Corporation for $35 is a part of Gondaliya CPA", OC),
    "Salary, Dividends, and Bonus Planning for Incorporated Business Owners": ("corporate year-end tax checklist 2026", OC + "first-year-filing-calendar-new-corporation/"),
    "Evaluating Salary vs Dividends to Optimize Tax Outcomes": ("RRSP contribution room", OC + "guides/salary-vs-dividends/"),
    "Accrued Bonus Rules and Payment Deadlines for Deductibility": ("Canada Pension Plan (CPP) amounts", OC + "payroll-service/"),
    "Understanding TOSI Screening and Shareholder Loan Implications": ("TOSI (Tax on Split Income) rules", OC + "guides/tax-on-split-income/"),
    "Managing Payroll, GST/HST, and Instalment Payments": ("corporate instalments", OC + "corporate-compliance-subscription/"),
    "Final GST/HST Remittance and Reporting Obligations": ("registered for GST/HST", OC + "business-number-cra-account-registration/"),
    "Reviewing Corporate Instalments Due Dates and Amounts": ("check with a CPA", "https://gondaliyacpa.ca/consultation/"),
    "Strategic Year-End Moves and Planning for the Coming Year": ("checking passive income", OC + "guides/holding-company-canada/"),
    "Monitoring Passive Income Levels and Small Business Deduction Impact": ("small business deduction limit", OC + "guides/small-business-deduction/"),
    "Clearing Shareholder Loans and Updating Minute Book Resolutions": ("update minute book resolutions", OC + "minute-book-preparation/"),
    "Key Corporate Year-End Reminders from Open Corporation for $35": ("CBCA vs OBCA Compliance", OC + "incorporate-federally-in-canada/"),
    "Next Steps": ("File Ontario Business Registry annual returns promptly", OC + "corporate-annual-filing/"),
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
<h4>Plan your 2026 year-end before December 31</h4>
<p>Incorporation from $35 including HST plus government fees, and a free CPA consultation on your salary, bonus, dividends, shareholder loan and equipment purchases before the year closes. Please book a free consultation.</p>
<div class="gcpa-trust"><span>1300+ 5-star Google reviews</span><span>Xero Partner Award Winner 2026</span><span>CPA Ontario Firm 61330051</span><span>30-Day Money-Back Guarantee</span></div>
<div class="gcpa-btnrow"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="https://opencorporationfor35.ca/">Open Corporation For $35</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BANNER = """<div class="gcpa-banner" style="background:linear-gradient(135deg,#0d3b66 0%,#0c7a7a 100%) !important;">
<div class="bt">Closing your books on December 31? Please book a free consultation and we will go through your year-end checklist with you, one date at a time.</div>
<div class="bb"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="mailto:info@gondaliyacpa.ca">info@gondaliyacpa.ca</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BEFORE = {
    "Overview of T2 Filing, T4 Slip Submission, and Annual Return Requirements": callout("teal", "Key Stat", "<strong>March 1, 2027:</strong> the due date for 2026 T4 and T5 slips and for 2026 RRSP contributions, because February 28, 2027 falls on a Sunday."),
    "Using Accounting Software to Streamline Bookkeeping Tasks": callout("blue", "Worth Knowing", "A dividend counts for the year it is paid, not the year it is declared. Please make sure the money actually leaves the corporate account by December 31 if you want the dividend on your 2026 return."),
    "Timing Purchases and Capital Asset Acquisitions for Tax Benefits": callout("red", "Risk Warning", "Please do not buy assets in December only for the deduction. The asset must be available for use by December 31, and a purchase the business does not need still costs more than the tax it saves."),
    "Salary, Dividends, and Bonus Planning for Incorporated Business Owners": CTA_MID,
    "Understanding TOSI Screening and Shareholder Loan Implications": callout("gold", "Our Actual Experience", "The year-end item we fix most often is a bonus booked at December 31 and never paid. If it is not paid within 180 days, the deduction moves to the year it is paid, so we diarize the June 29, 2027 payment date when we prepare the resolution."),
    "Reviewing Corporate Instalments Due Dates and Amounts": callout("red", "Risk Warning", "If you pay yourself through payroll, please remit December's source deductions by January 15, 2027. Late remittances attract a penalty of 3% to 10% of the amount plus interest, even when the tax is paid in full later."),
    "Considering RRSP Contribution Room, TFSA, FHSA, and Other Registered Accounts": callout("red", "Risk Warning", "A shareholder loan made in 2026 that is not repaid by December 31, 2027 is added to your 2026 income. Please do not repay it with a new loan just before the deadline; the CRA treats a series of loans and repayments as no repayment at all."),
    "Addressing Common Year-End Tax Errors and Edge Cases": BANNER,
}
AFTER_FAQ = callout("teal", "Worth Knowing", "A corporation with a non-calendar year-end still runs payroll, T4 slips and RRSP room on the calendar year. Please keep both calendars in mind when you plan bonuses and dividends.")


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
    if ln.startswith("Income Tax Act (ITA), Subdivision b"):
        items = []
        while i < len(lines) and lines[i].strip():
            items.append(lines[i].strip())
            i += 1
        sections[cur].append('<ul style="font-size:14px;">\n' + "\n".join(f"<li>{inline(x)}</li>" for x in items) + "\n</ul>")
        continue
    if re.match(r"^\[\d\] ", ln) or re.match(r"^\d \S", ln) or ln.startswith("*"):
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
assert "@@JSON@@" in page and "Corporate Year-End Readiness Check" in page

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
