import re, sys, html, os
A = sys.argv[1]
pages = [(56870,'accountant-for-private-investigators'),(56869,'accountant-for-security-guard-companies'),(56871,'accountant-for-security-companies'),(56872,'accountant-for-lash-and-brow-studios'),(56803,'accountant-for-software-resellers'),(56798,'accountant-for-no-code-development-agencies'),(56807,'accountant-for-product-design-studios'),(56799,'accountant-for-denturists'),(56800,'accountant-for-businesses-winding-down'),(54831,'accountant-for-cloud-service-providers'),(54824,'accountant-for-data-analytics-companies'),(54823,'accountant-for-cybersecurity-companies'),(54828,'accountant-for-managed-service-providers'),(54734,'accountant-for-medical-device-distributors'),(54731,'accountant-for-sleep-clinics'),(54736,'accountant-for-fertility-clinics'),(54334,'accountant-for-second-generation-family-businesses')]
out = ["# Row 23 before and after: accountant-for-* pages created October 5 to 9, 2026","",
"These 17 pages went live after the October 5 template change but still state 12.2% as the current rate. Proposed: 11.2%, per row 23. Nothing here is changed until Sharad approves. Where the JSON-LD repeats the FAQ text, it changes with it.","",
"| # | Page (ID) | Where | Before | After |","|---|---|---|---|---|"]
n = 0
for pid, slug in pages:
    t = open(os.path.join(A, slug + '.html'), encoding='utf-8').read()
    ld = ''.join(re.findall(r'<script type="application/ld\+json">.*?</script>', t, re.S))
    vis = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', t, flags=re.S)
    txt = html.unescape(re.sub(r'<[^>]+>', ' ', vis)); txt = re.sub(r'\s+', ' ', txt)
    for where, src in (('Visible', txt), ('JSON-LD', html.unescape(ld))):
        sents = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9])|"\s*[,:}]\s*"?|\s{2,}', src)
        for s in sorted(set(x.strip() for x in sents if '12.2%' in x)):
            n += 1
            after = re.sub(r'\ba 12\.2%', 'an 11.2%', s).replace('12.2%', '11.2%')
            out.append(f"| {n} | /{slug}/ ({pid}) | {where} | {s} | {after} |")
open('existing-fixes/row-23-before-after.md', 'w').write('\n'.join(out) + '\n')
print(n)
