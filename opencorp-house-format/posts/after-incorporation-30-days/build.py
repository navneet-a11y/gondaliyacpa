#!/usr/bin/env python3
"""Build post.html for the first-30-days post from source.md + corrections.json.

Body text comes from the draft (with approved corrections); house elements,
links and callouts are added from the tables below. The page shell (style,
widget CSS/JS) is reused from ../why-35-fee/post.html.
"""
import html, json, re

HERE = __file__.rsplit("/", 1)[0] or "."
src = open(f"{HERE}/source.md", encoding="utf-8").read()
for c in json.load(open(f"{HERE}/corrections.json", encoding="utf-8")):
    src = src.replace(c["from"], c["to"])
lines = src.splitlines()[1:]  # first line is the H1 + SEO H2

H1 = "What Happens After You Incorporate in Canada? The First 30 Days: A Business Owner's Checklist"
H2SEO = "What Happens After Incorporating a Business: First 30 Days After Incorporation Canada Checklist by Open Corporation"
DATE = "November 16, 2026"
ISO = "2026-11-16"
SLUG = "what-happens-after-you-incorporate-canada-first-30-days"

SECTIONS = {  # H2 -> (number, id, label, pill colour, pill text)
    "What Incorporation Means for Your Business in Canada": (1, "toc-meaning", "What Incorporation Means", "blue", "The Basics"),
    "Organizing your corporation after incorporation": (2, "toc-organize", "Organizing the Corporation", "teal", "Setup"),
    "Filing the Initial Return with the Appropriate Authorities": (3, "toc-filings", "Filings and CRA Accounts", "gold", "Filings"),
    "Establishing a shareholders’ agreement: when and why it matters": (4, "toc-records", "Agreements and Records", "green", "Records"),
    "Common Challenges and Solutions": (5, "toc-challenges", "Challenges and Fixes", "red", "Challenges"),
    "Summary of Critical First 30 Days Checklist After Incorporation": (6, "toc-checklist", "The 30-Day Checklist", "gold", "Checklist"),
    "Frequently Asked Questions About the First 30 Days": (7, "toc-faq", "First 30 Days FAQ", "teal", "FAQ"),
    "Post-Incorporation Setup Costs: What To Expect": (8, "toc-costs", "Costs and Quick Reference", "blue", "Costs"),
}
H3 = """Benefits and Legal Implications of Incorporation
How Incorporation Separates Personal and Business Liabilities
Choosing the Right Type of Corporation for Your Needs
Overview of Federal Versus Provincial Incorporation
Incorporation Timeline Across Canadian Jurisdictions
Common Causes For Delays During The Incorporation Process
What is organizational setup?
Roles and responsibilities of first directors
Conducting the initial organizational meeting
Adopting corporate by-laws and their importance
Issuing shares: procedures and legal requirements
Appointment of officers and delegation of duties
Holding the first shareholders’ meeting and key decisions
Setting up and maintaining the corporate minute book
Understanding Differences Between Annual Returns and Tax Filings
Registering for CRA Business Accounts (GST/HST, Payroll, Corporate Income Tax)
Corporate Bank Account Setup and Its Significance
Requirements for Ongoing Filings and Reporting in Ontario and Federally
Procedures for Updating Registered Office Address and Director Changes
Maintaining Good Corporate Standing to Avoid Penalties
Differentiating roles of directors versus officers
Keeping accurate corporate records and legal documentation
Preparing for annual general meetings and reports
Handling corporate amendments and name changes
Best practices for filing corporate documents and tracking deadlines
Frequent mistakes new corporations make in the first 30 days
Risks of incomplete organization and non-compliance
Remedies and corrective steps for delayed post-incorporation tasks
Weighing DIY incorporation setup versus professional assistance
Tips to expedite incorporation and subsequent filings
Managing complex share structures and director appointments
Key Takeaways to Maintain Compliance and Operational Efficiency
Where to Find Official Forms, Templates, and Checklists for Corporation Management
Accessing Expert Guidance and Legal Support When Needed
Encouraging Proactive Management for Long-Term Corporate Success
Contact and Support Options for Further Assistance With Incorporation and Filings
How Open Corporation for $35 Handles Your First 30 Days
Essential Deliverables You Receive With Our Service
Risks, Compliance Issues, and Prevention Controls
Preparing Before Your First 30 Days Start
Numeric Walkthrough: A Realistic Timeline Post-Incorporation
Choosing a CPA For Post-Incorporation Setup: Key Factors
Why Trust Open Corporation for $35?
Sources & References""".splitlines()
H4 = """Federal vs Provincial Corporations
Factors To Consider When Deciding The Structure
Key Differences And Similarities
How To Choose Which Jurisdiction Is Best
Typical Processing Times
Province-Specific Requirements
Incomplete Documents
Name Issues And Other Pitfalls
Realistic Expectations For Processing Times
Required legal documents
Duties, powers, and limitations
Selecting initial directors
Mandatory agenda items
Resolutions to adopt
Why by-laws matter
Typical contents of by-laws
How to issue shares
Documenting share issuance
Designating roles and responsibilities
Legal documentation required
What must be decided
How to record meeting minutes""".splitlines()
H5 = ["References"]
LEVEL = {**{h: 2 for h in SECTIONS}, **{h: 3 for h in H3}, **{h: 4 for h in H4}, **{h: 5 for h in H5}}
LISTY = {"Post-Incorporation Setup Costs: What To Expect", "How Open Corporation for $35 Handles Your First 30 Days",
         "Essential Deliverables You Receive With Our Service", "Risks, Compliance Issues, and Prevention Controls",
         "Preparing Before Your First 30 Days Start", "Numeric Walkthrough: A Realistic Timeline Post-Incorporation",
         "Choosing a CPA For Post-Incorporation Setup: Key Factors", "References"}

LINK_FIX = {  # markdown links whose URL must not be published as written
    "Which Program Accounts Does A New Corporation Need? - Open Corporation For $35": "https://opencorporationfor35.ca/business-number-cra-account-registration/",
    "How To Open A Corporate Bank Account Post-Incorporation - Open Corporation For $35": "https://opencorporationfor35.ca/business-bank-account-setup/",
    "ITA Section 15(2): Shareholder Loans Rules": "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-15.html",
}
OC = "https://opencorporationfor35.ca/"
LINKS = {  # section heading -> (phrase on the page, url); one site link per section
    "_intro": ("first 30 days after incorporation Canada checklist", OC + "guides/what-happens-after-you-incorporate/"),
    "What Incorporation Means for Your Business in Canada": ("limited liability", OC + "convert-sole-proprietorship-corporation/"),
    "Benefits and Legal Implications of Incorporation": ("Corporations often pay less tax", OC + "guides/small-business-deduction/"),
    "Choosing the Right Type of Corporation for Your Needs": ("federal or provincial incorporation", OC + "incorporate-federally-in-canada/"),
    "Federal vs Provincial Corporations": ("Ontario Business Corporations Act (OBCA)", OC + "how-to-incorporate-in-ontario/"),
    "Key Differences And Similarities": ("extra-provincial registration", OC + "guides/extra-provincial-registration/"),
    "Name Issues And Other Pitfalls": ("NUANS report", OC + "nuans-report-20/"),
    "Organizing your corporation after incorporation": ("keep records", OC + "guides/minute-book-requirements/"),
    "Selecting initial directors": ("single director", OC + "guides/director-residency-requirements/"),
    "How to issue shares": ("share certificates", OC + "share-issuance-transfer/"),
    "Setting up and maintaining the corporate minute book": ("minute book", OC + "minute-book-preparation/"),
    "Filing the Initial Return with the Appropriate Authorities": ("file the initial return within 60 days", OC + "initial-return-filing-ontario-form-1/"),
    "Understanding Differences Between Annual Returns and Tax Filings": ("T2 form", OC + "corporate-tax-filing-from-300/"),
    "Requirements for Ongoing Filings and Reporting in Ontario and Federally": ("File each year on time", OC + "corporate-annual-filing/"),
    "Procedures for Updating Registered Office Address and Director Changes": ("new registered office address", OC + "corporate-changes-amendments/"),
    "Maintaining Good Corporate Standing to Avoid Penalties": ("with reminders", OC + "corporate-compliance-subscription/"),
    "Establishing a shareholders’ agreement: when and why it matters": ("A shareholders’ agreement", OC + "guides/shareholder-agreement-what-a-cpa-checks/"),
    "Keeping accurate corporate records and legal documentation": ("Individuals with Significant Control (ISC) register", OC + "guides/individuals-with-significant-control/"),
    "Preparing for annual general meetings and reports": ("Filing annual returns", OC + "guides/corporate-annual-return/"),
    "Best practices for filing corporate documents and tracking deadlines": ("Use checklists", OC + "first-year-filing-calendar-new-corporation/"),
    "Frequent mistakes new corporations make in the first 30 days": ("GST/HST (RT)", OC + "guides/hst-registration-guide/"),
    "Remedies and corrective steps for delayed post-incorporation tasks": ("Register all needed CRA program accounts", OC + "business-number-cra-account-registration/"),
    "Managing complex share structures and director appointments": ("multiple share classes", OC + "guides/share-structure-explained/"),
    "Summary of Critical First 30 Days Checklist After Incorporation": ("Opening a corporate bank account", OC + "business-bank-account-setup/"),
    "Key Takeaways to Maintain Compliance and Operational Efficiency": ("payroll (RP) accounts", OC + "payroll-service/"),
    "Accessing Expert Guidance and Legal Support When Needed": ("Open Corporation for $35", OC + "incorporation-service-35/"),
    "Encouraging Proactive Management for Long-Term Corporate Success": ("Setting up bookkeeping", OC + "incorporation-bookkeeping-bundle/"),
    "Contact and Support Options for Further Assistance With Incorporation and Filings": ("free consultations", "https://gondaliyacpa.ca/consultation/"),
    "Post-Incorporation Setup Costs: What To Expect": ("Government fees", OC + "guides/cost-to-incorporate-in-canada/"),
}


def callout(kind, tag, text):
    lead = f"<strong>{tag}:</strong> " if tag == "Risk Warning" else ""
    return f'<div class="gcpa-callout {kind}">\n<span class="co-tag">{tag}</span>\n<p>{lead}{text}</p>\n</div>'


CTA_MID = """<div class="gcpa-cta" style="background:linear-gradient(135deg,#0f2a4a 0%,#1c4a78 100%) !important;">
<h4>Get your first 30 days done with a CPA</h4>
<p>Incorporation from $35 including HST plus government fees, with a free CPA consultation on your resolutions, shares and CRA accounts after the certificate. Please book a free consultation.</p>
<div class="gcpa-trust"><span>1300+ 5-star Google reviews</span><span>Xero Partner Award Winner 2026</span><span>CPA Ontario Firm 61330051</span><span>30-Day Money-Back Guarantee</span></div>
<div class="gcpa-btnrow"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="https://opencorporationfor35.ca/">Open Corporation For $35</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BANNER = """<div class="gcpa-banner" style="background:linear-gradient(135deg,#0d3b66 0%,#0c7a7a 100%) !important;">
<div class="bt">Just incorporated? Please book a free consultation and we will go through your first 30 days with you, one item at a time.</div>
<div class="bb"><a class="solid" href="https://gondaliyacpa.ca/consultation/">Book Free Consultation</a><a href="mailto:info@gondaliyacpa.ca">info@gondaliyacpa.ca</a><a href="tel:+16472129559">647-212-9559</a></div>
</div>"""
BEFORE = {  # inserted just before the named heading
    "Common Causes For Delays During The Incorporation Process": callout("teal", "Key Stat", "<strong>Same day:</strong> the usual processing time for a complete online incorporation with Corporations Canada or the Ontario Business Registry. The 30-day clock in this checklist starts when you receive the certificate."),
    "Conducting the initial organizational meeting": callout("blue", "Worth Knowing", "Ontario has had no resident director rule since July 5, 2021, so a single director living anywhere can run an Ontario corporation. A federal corporation still needs at least 25% resident Canadian directors."),
    "Holding the first shareholders’ meeting and key decisions": callout("gold", "Our Actual Experience", "The step we see missed most often is issuing the shares. A corporation with no issued shares has no shareholders on paper, which causes trouble at the bank and at tax time, so we prepare the share issuance together with the organizational resolutions."),
    "Requirements for Ongoing Filings and Reporting in Ontario and Federally": callout("red", "Risk Warning", "Money you take out of the corporation before the books are set up can be treated as a shareholder loan under section 15(2) of the Income Tax Act. Please do not pay personal costs from the corporate account, or business costs from your own, without recording them."),
    "Establishing a shareholders’ agreement: when and why it matters": CTA_MID,
    "Handling corporate amendments and name changes": callout("red", "Risk Warning", "A change of director or registered office must be reported within 15 days. Please file the notice of change as soon as the change happens, because a late or missing notice leaves the public record wrong."),
    "Summary of Critical First 30 Days Checklist After Incorporation": BANNER,
    "Post-Incorporation Setup Costs: What To Expect": callout("red", "Risk Warning", "An Ontario corporation, or a federal corporation operating in Ontario, that misses its initial return or annual returns can lose good standing and eventually be dissolved. Please put each deadline in your calendar the day you receive your certificate."),
}

RECORD_HEAD = ["Record", "Requirement", "Where Kept", "When Updated", "Authority"]


def esc(s):
    return html.escape(s, quote=False)


def inline(s):
    out, pos = [], 0
    for m in re.finditer(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", s):
        out.append(esc(s[pos:m.start()]))
        text, url = m.group(1), LINK_FIX.get(m.group(1), m.group(2))
        out.append(f'<a href="{esc(url)}">{esc(text)}</a>')
        pos = m.end()
    out.append(esc(s[pos:]))
    return "".join(out)


def labelled(s):
    m = re.match(r"^([^:]{2,60}?): (.+)$", s)
    if m and "http" not in m.group(1) and not s.startswith("[") and len(m.group(1).split()) <= 6:
        return f"<strong>{inline(m.group(1))}:</strong> {inline(m.group(2))}"
    return inline(s)


def table(rows, head=None):
    head = head or rows.pop(0)
    t = ['<figure class="wp-block-table">', "<table>", "<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>", "<tbody>"]
    t += ["<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows]
    t += ["</tbody>", "</table>", "</figure>"]
    return "\n".join(t)


def numhead(h):
    n, i, label, colour, pill = SECTIONS[h]
    return (f"<h2>{esc(h)}</h2>\n<div class=\"gcpa-numhead\">\n<div class=\"num\" style=\"background:#0f2a4a !important;color:#ffffff !important;\">{n}</div>\n"
            f"<h4 id=\"{i}\" style=\"border:none;padding:0;margin:0;\">{esc(label)}</h4>\n<span class=\"gcpa-pill {colour}\">{esc(pill)}</span>\n</div>")


# ---- parse the body ----
out, i, cur, faq = [], 0, "_intro", []
sections = {"_intro": []}
order = ["_intro"]
FAQ_START = "What is the CRA payroll remittance due date for new corporations?"
INTRO = lines[2]  # the TLDR-style intro paragraph
i = 3
while i < len(lines):
    ln = lines[i].rstrip()
    if not ln or ln == "---":
        i += 1
        continue
    if ln == FAQ_START:
        cur = "Frequently Asked Questions About the First 30 Days"
        order.append(cur)
        sections[cur] = []
        while lines[i].rstrip() != "Post-Incorporation Setup Costs: What To Expect":
            q = lines[i].rstrip()
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
        i += 1
        if ln in LISTY:
            items = []
            while i < len(lines) and lines[i].strip() and lines[i].rstrip() not in LEVEL:
                items.append(lines[i].rstrip())
                i += 1
            sections[cur].append("<ul>\n" + "\n".join(f"<li>{labelled(x)}</li>" for x in items) + "\n</ul>")
        continue
    if ln == "Articles of Incorporation" and cur == "Keeping accurate corporate records and legal documentation":
        rows = [[lines[i + r * 5 + k].strip() for k in range(5)] for r in range(5)]
        sections[cur].append(table(rows, RECORD_HEAD))
        i += 25
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

# ---- links: wrap the first occurrence of the phrase outside tags ----
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

# ---- assemble the body ----
parts = []
for h in order[1:]:
    if h in BEFORE:
        parts.append(BEFORE[h])
    if h in SECTIONS:
        parts.append(numhead(h))
    elif h == "References":
        parts.append(f"<h5>{esc(h)}</h5>")
    else:
        lvl = LEVEL[h]
        parts.append(f"<h{lvl}>{esc(h)}</h{lvl}>")
    if h == "Frequently Asked Questions About the First 30 Days":
        parts.append('<div class="gcpa-faq" id="faq-main">')
        for q, a in faq:
            parts.append(f'<details><summary>{esc(q)}<span class="pl">+</span></summary>\n<div class="ans"><p>{esc(a)}</p></div></details>')
        parts.append("</div>")
    parts.extend(sections[h])
BODY = "\n".join(parts)

TAIL = open(f"{HERE}/tail.html", encoding="utf-8").read()
HEAD = open(f"{HERE}/head.html", encoding="utf-8").read().replace("@@INTRO@@", INTRO_HTML)
A = HEAD + "\n" + BODY + "\n" + TAIL

tpl = open(f"{HERE}/../why-35-fee/post.html", encoding="utf-8").read()
B = open(f"{HERE}/widget.html", encoding="utf-8").read()
C = open(f"{HERE}/closing.html", encoding="utf-8").read()
page = re.sub(r'<div class="gcpa-hero"[\s\S]*?(?=<div id="ocf-chk">)', lambda m: A + "\n", tpl, count=1)
page = re.sub(r'<div class="s-head"[\s\S]*?(?=<button type="button" class="s-go")', lambda m: B, page, count=1)
page = re.sub(r'<div class="gcpa-cta"[^>]*>\s*<h4>Incorporate for \$35, HST included[\s\S]*$', lambda m: C, page, count=1)

strip = lambda s: html.unescape(re.sub("<[^>]+>", "", s))
ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "BlogPosting", "@id": f"{OC}{SLUG}/#article", "headline": H1,
     "description": "The first 30 days after incorporating in Canada: organizational resolutions, shares, minute book, initial return, CRA accounts, bank account and the deadlines that follow.",
     "datePublished": ISO, "dateModified": ISO, "author": {"@type": "Person", "name": "Sharad Gondaliya, CPA"},
     "publisher": {"@type": "Organization", "name": "Open Corporation for $35", "description": "Open Corporation for $35 is a department of Gondaliya CPA.",
                   "parentOrganization": {"@type": "AccountingService", "name": "Gondaliya CPA Professional Corporation", "identifier": "CPA Ontario Firm Registration 61330051"}},
     "mainEntityOfPage": f"{OC}{SLUG}/"},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
page = page.replace("@@JSON@@", '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False) + "\n</script>")
words = len(re.sub("<[^>]+>", " ", html.unescape(re.sub(r"<(style|script)[^>]*>.*?</\1>", "", page, flags=re.S))).split())
page = page.replace("@@READ@@", str(round(words / 220)))
open(f"{HERE}/post.html", "w", encoding="utf-8").write(page)
open(f"{HERE}/headings.txt", "w", encoding="utf-8").write("\n".join([H1, H2SEO] + [h for h in order[1:] if h != "Frequently Asked Questions About the First 30 Days"]) + "\n")
print("words", words, "reading", round(words / 220), "faq", len(faq), "sections", len(order) - 1)
