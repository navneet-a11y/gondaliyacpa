#!/usr/bin/env python3
"""Assemble post.html from the house template, body.html and the FAQ schema."""
import html, json, math, re, pathlib

here = pathlib.Path(__file__).parent
tpl = (here / "../../template.html").read_text(encoding="utf-8")
body = (here / "body.html").read_text(encoding="utf-8")

head = tpl[tpl.index("<style>"):tpl.index('<div class="gcpa-post">')]
check = tpl[tpl.index('<div id="ocf-chk">'):tpl.index("<!-- 15.")].rstrip()

questions = [
    ("Does your spouse work in the business an average of 20 hours a week or more?", "0",
     "Whether a TOSI exclusion applies, because dividends to a spouse who does not work in the business are usually taxed at the top rate"),
    ("Are you, the business owner, 65 or older this year?", "0",
     "Which TOSI exclusion your spouse can rely on, since the age-based spousal rule needs the owner to be 65 or older"),
    ("Will your spouse's shares be paid for with your money?", "1",
     "Attribution, because income and gains on shares bought with your money can be taxed back to you"),
    ("Is the corporation a professional corporation?", "1",
     "Whether your college allows a spouse to hold shares, and in which class"),
    ("Do you want to keep full voting control?", "1",
     "A non-voting class for your spouse, which must be in the articles or added by articles of amendment"),
    ("Do you have a shareholder agreement or marriage contract in place?", "0",
     "A shareholder agreement and, where needed, a marriage contract covering separation and death"),
]
check = check.replace("{{CHECK_TITLE}}", "Spouse Shareholder Readiness Check")
for n, (q, flag, msg) in enumerate(questions, 1):
    check = check.replace(f'data-flag="1" data-msg="{{{{FLAG_{n}}}}}"',
                          f'data-flag="{flag}" data-msg="{html.escape(msg)}"', 1)
    check = check.replace(f"{{{{CHECK_Q{n}}}}}", html.escape(q, quote=False), 1)
assert "{{" not in check

faq = re.search(r'<div class="gcpa-faq" id="faq-main">(.*?)</div>\s*<div class="gcpa-callout', body, re.S).group(1)
pairs = re.findall(r'<summary>(.*?)<span class="pl">.*?<div class="ans"><p>(.*?)</p>', faq, re.S)
pairs = [(html.unescape(q).strip(), html.unescape(a).strip()) for q, a in pairs]

slug = "spouse-own-shares-corporation-canada"
desc = ("Your spouse can own shares in your corporation. Learn how TOSI, attribution, share classes "
        "and professional corporation rules decide whether it saves tax.")
schema = {"@context": "https://schema.org", "@graph": [
    {"@type": "BlogPosting", "@id": f"https://opencorporationfor35.ca/{slug}/#article",
     "headline": "Can My Spouse Own Shares in My Corporation in Canada? Tax Rules and Considerations", "description": desc,
     "datePublished": "2026-10-27", "dateModified": "2026-10-27",
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
