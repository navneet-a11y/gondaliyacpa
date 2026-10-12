#!/usr/bin/env python3
"""Verify an assembled industry page: every section of the 22-block format is
present, in page order, with the expected counts, and the fixed chrome is intact.

Usage: python3 scripts/verify_industry_page.py <page.html> [...]

Prints one [PASS]/[FAIL] line per check (28 section checks, then 11 fixed-chrome
checks) and a RESULT line per page.  Exit 0 only if every check passed.
"""
import re
import sys

OK = "  RESULT: PASS - every section present, hero banner through final CTA"


def count(page, needle):
    return page.count(needle)


def region(page, start, end):
    """Slice between two markers; empty string if either is missing."""
    i = page.find(start)
    if i < 0:
        return ""
    j = page.find(end, i)
    return page[i:j if j > 0 else len(page)]


def section_checks(page):
    exp = region(page, '<div class="sb-exp">', "<!-- 11.")
    quiz = region(page, '<div class="sb-quiz-band">', "<!-- 12.")
    return [
        ("hero banner (sb-hero2)",
         count(page, '<div class="sb-hero2">') == 1),
        ("exactly one <h1>",
         len(re.findall(r"<h1[ >]", page)) == 1),
        ("'1300+' social proof x3+",
         count(page, "1300+") >= 3),
        ("hero CTA pills (sb-pill)",
         count(page, 'class="sb-pill"') >= 2),
        ("intro two-column block (sb-intro + photo)",
         count(page, '<div class="sb-intro">') == 1 and count(page, '<div class="sb-intro-img">') == 1),
        ("official partners strip",
         "Our Official Partners" in page and count(page, '<div class="logo-section">') == 1),
        ("4-icon block (sb-icon4, 4 cards)",
         count(page, '<div class="sb-icon4">') == 1
         and count(region(page, '<div class="sb-icon4">', "<!-- 5."), '<div class="sb-ic">') == 4),
        ("3-icon block (sb-icon3, 3 cards)",
         count(page, '<div class="sb-icon3">') == 1
         and count(region(page, '<div class="sb-icon3">', "<!-- 6."), '<div class="sb-ic">') == 3),
        ("experts slider + list",
         count(page, '<div class="sb-slider">') == 1 and count(page, '<div class="sb-expert-list">') == 1),
        ("why-choose 4 steps",
         count(page, '<div class="sb-step-grid">') == 1 and count(page, '<div class="sb-step">') == 4),
        ("stat bar band + 3 status cards",
         count(page, "Registered CPA Ontario") == 1
         and count(page, "grid-template-columns:repeat(3,1fr);gap:16px") == 1),
        ("12 service boxes (sb-svc)",
         count(page, '<div class="sb-svc">') == 12),
        ("expanded-services band (sb-exp, 12 items)",
         count(page, '<div class="sb-exp">') == 1 and count(page, '<div class="sb-exp-item">') == 12),
        ("expanded-services bullets (exactly 60 <li>)",
         count(exp, "<li>") == 60),
        ("readiness quiz (6 questions + scoring script)",
         count(page, '<div class="sb-quiz-q">') == 6 and "sb-quiz-btn" in quiz and "<script>" in quiz),
        ("HubSpot meetings embed",
         'class="meetings-iframe-container"' in page and "MeetingsEmbedCode.js" in page),
        ("3 case studies",
         count(page, '<div class="sb-case-card">') == 3),
        ("5 process steps",
         count(page, '<div class="sb-proc-hero">') == 1 and count(page, '<div class="sb-step2">') == 5),
        ("CTA band",
         count(page, '<div class="sb-ctaband">') == 1),
        ("pricing heading 'Affordable Pricing for'",
         "Affordable Pricing for" in page and count(page, '<div class="sb-price">') == 1),
        ("Interac e-Transfer to info@gondaliyacpa.ca",
         "Interac e-Transfer to info@gondaliyacpa.ca" in page),
        ("2 team cards",
         count(page, '<div class="sb-team-card">') == 2),
        ("Trustindex reviews loader",
         "cdn.trustindex.io/loader.js" in page),
        ("map: 12 location cards + 15 city links",
         count(page, "data-map-src=") == 12 and count(page, 'class="city-card"') == 15),
        ("FAQ items (13+)",
         count(page, '<div class="sb-faq-item">') >= 13),
        ("4 related industries",
         count(page, '<div class="sb-ind-card">') == 4),
        ("final CTA (sb-cta-split)",
         count(page, '<div class="sb-cta-split">') == 1),
        ("2 schema blocks (FAQPage + AccountingService, reviewCount 1381)",
         count(page, '<script type="application/ld+json">') == 2
         and '"@type":"FAQPage"' in page
         and '"@type":"AccountingService"' in page
         and '"reviewCount":"1381"' in page),
    ]


def chrome_checks(page):
    maparea = region(page, '<div class="sb-maparea">', "<!-- 18.")
    return [
        ("chrome css: <style> block with .sb-wrap base rules",
         page.startswith("<style>") and ".sb-wrap{max-width:1100px" in page and "</style>" in page),
        ("chrome css: hero/pricing/map rules present",
         ".sb-hero2{" in page and ".sb-price{" in page and ".sb-maparea{" in page),
        ("chrome css: multibyte check glyphs preserved",
         count(page, "✓") >= 2),
        ("chrome partners: 9 partner logos",
         count(region(page, '<div class="logo-section">', "<!-- 4."), '<div class="logo-item') == 9),
        ("chrome partners: QuickBooks / Xero / Stripe / Wagepoint",
         all(alt in page for alt in ('alt="QuickBooks"', 'alt="Xero"', 'alt="Stripe"', 'alt="Wagepoint"'))),
        ("chrome credentials: registered CPA firm badge",
         '<div class="sb-hero2-cpa">' in page and "REGISTERED CPA FIRM" in page and "VERIFY NOW" in page),
        ("chrome statbar: 4 star stats",
         all(s in page for s in ("Registered CPA Ontario", "Google Reviews",
                                 "30-Day Money-Back Guarantee", "60-Day Fees-Matching Policy"))),
        ("chrome pricing_right: 11 fee lines + HST note",
         count(region(page, '<div class="sb-price-right">', '<!-- 15.'), "<li>") == 11
         and "All fees include HST." in page),
        ("chrome team_cards: Sharad Gondaliya + Vandana Goel",
         "Sharad Gondaliya, CPA" in page and "Vandana Goel, CPA" in page
         and "sharad@gondaliyacpa.ca" in page and "vandana@gondaliyacpa.ca" in page),
        ("chrome maparea: 12 location cards + sb-map-embed iframe",
         count(maparea, 'class="one-location') == 12 and '<iframe id="sb-map-embed"' in maparea),
        ("chrome maparea: .one-location click script",
         "document.querySelectorAll('.one-location')" in maparea),
    ]


def verify(path):
    with open(path, encoding="utf-8", newline="") as fh:
        page = fh.read()
    checks = section_checks(page) + chrome_checks(page)
    failed = 0
    print("%s  (%d section checks, %d fixed-chrome checks)"
          % (path, len(section_checks(page)), len(chrome_checks(page))))
    for label, ok in checks:
        print("[%s] %s" % ("PASS" if ok else "FAIL", label))
        if not ok:
            failed += 1
    if failed:
        print("  RESULT: FAIL - %d of %d checks failed" % (failed, len(checks)))
        return False
    print(OK)
    return True


def main(argv):
    if len(argv) < 2:
        sys.exit("usage: verify_industry_page.py <page.html> [...]")
    ok = True
    for path in argv[1:]:
        ok = verify(path) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
