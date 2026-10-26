#!/usr/bin/env python3
"""Assemble post.html from the house template, body.html and the FAQ schema."""
import html, json, math, re, pathlib

here = pathlib.Path(__file__).parent
tpl = (here / "../../template.html").read_text(encoding="utf-8")
body = (here / "body.html").read_text(encoding="utf-8")

head = tpl[tpl.index("<style>"):tpl.index('<div class="gcpa-post">')]
check = tpl[tpl.index('<div id="ocf-chk">'):tpl.index("<!-- 15.")].rstrip()

questions = [
    ("Have you chosen and recorded your fiscal year-end?", "0",
     "Choosing a fiscal year-end, which fixes your T2 and balance-due dates and needs CRA approval to change later"),
    ("Do you have CRA My Business Account access, or have you authorised a representative?", "0",
     "Setting up CRA online access, since the T2 is filed electronically and CRA notices arrive there"),
    ("Is your corporation incorporated in Ontario?", "1",
     "The Ontario Initial Return within 60 days of incorporating, and the Annual Return within six months of each year-end"),
    ("Do you expect taxable sales over $30,000 in the next four quarters?", "1",
     "GST/HST registration within 29 days of passing $30,000, and your filing frequency"),
    ("Will the corporation pay you or anyone else a salary this year?", "1",
     "A payroll account, remittances by the 15th of the following month, and T4 slips by the last day of February"),
    ("Will the corporation pay dividends this year?", "1",
     "T5 slips and the T5 summary by the last day of February after the year of payment"),
]
check = check.replace("{{CHECK_TITLE}}", "First-Year Filing Readiness Check")
for n, (q, flag, msg) in enumerate(questions, 1):
    check = check.replace(f'data-flag="1" data-msg="{{{{FLAG_{n}}}}}"',
                          f'data-flag="{flag}" data-msg="{html.escape(msg)}"', 1)
    check = check.replace(f"{{{{CHECK_Q{n}}}}}", html.escape(q, quote=False), 1)
assert "{{" not in check

faq = re.search(r'<div class="gcpa-faq" id="faq-main">(.*?)</div>\s*<div class="gcpa-callout', body, re.S).group(1)
pairs = re.findall(r'<summary>(.*?)<span class="pl">.*?<div class="ans"><p>(.*?)</p>', faq, re.S)
pairs = [(html.unescape(q).strip(), html.unescape(a).strip()) for q, a in pairs]

slug = "first-year-filing-calendar-new-corporation"
desc = ("Every first-year deadline for a new Canadian corporation: T2 filing, balance-due day, "
        "instalments, GST/HST, payroll slips and annual returns, in one calendar.")
schema = {"@context": "https://schema.org", "@graph": [
    {"@type": "BlogPosting", "@id": f"https://opencorporationfor35.ca/{slug}/#article",
     "headline": "First-Year Filing Calendar for a New Corporation", "description": desc,
     "datePublished": "2026-10-26", "dateModified": "2026-10-26",
     "author": {"@type": "Person", "name": "Sharad Gondaliya, CPA"},
     "publisher": {"@type": "Organization", "name": "Open Corporation for $35",
                   "description": "Open Corporation for $35 is a department of Gondaliya CPA.",
                   "parentOrganization": {"@type": "AccountingService",
                                          "name": "Gondaliya CPA Professional Corporation",
                                          "identifier": "CPA Ontario Firm Registration 61330051"}},
     "mainEntityOfPage": f"https://opencorporationfor35.ca/{slug}/"},
    {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}]}

out = body.replace("{{READINESS_CHECK}}", check)
words = len(re.sub(r"<[^>]+>", " ", re.sub(r"<(style|script).*?</\1>", " ", out, flags=re.S)).split())
out = out.replace("{{READING_TIME}}", str(math.ceil(words / 220)))
out = head + out + '\n<script type="application/ld+json">\n' + json.dumps(schema, ensure_ascii=False) + "\n</script>\n"
assert "{{" not in out
(here / "post.html").write_text(out, encoding="utf-8")
print(f"post.html written, {words} words, {len(pairs)} FAQ, slug {slug}")
print("META", desc, len(desc))
