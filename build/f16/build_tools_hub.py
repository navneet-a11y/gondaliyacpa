# -*- coding: utf-8 -*-
"""Family 16 hub: /tools/.

Plan line 1154 puts the tools hub at /tools/, one of five F16 hubs, all due
live on October 9, 2026. Appendix A calls it /all-calculators/; resolved to
/tools/ because the nil_calculator rewrite base already puts every child at
/tools/<slug>/ and the BreadcrumbList on all ten already names /tools/ at
position 2.

Structure mirrors the guides hub (page 904) exactly: raw HTML with no wp:html
wrapper, a <style> block carrying no blank line so wpautop cannot break it, and
the same [cnf_child_count] shortcode for the live count line that line 1224
requires. Nothing here is a new pattern.
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
HUB = SITE + '/tools/'
FORM = SITE + '/form/'
TODAY, ISO = 'October 23, 2026', '2026-10-23'
PRICE = '$300.00 plus HST per tax year'
TITLE = 'Nil T2 Filing Tools and Calculators'
PAGE_TITLE = 'Nil T2 Filing Tools and Calculators for Canadian Corporations'
META = ('Free tools and calculators for a nil T2 corporate return in Canada. '
        'Deadlines, T2 Short eligibility, GIFI schedules, unfiled years and '
        'more. Nil T2 filing is ' + PRICE + '.')

# The ten children, in the order 6(e) lists them.
TOOLS = [
 ('nil-t2-deadline-calculator', 'Nil T2 Deadline Calculator',
  'Enter your fiscal year-end and get the T2 due date, the next business day '
  'where it falls on a weekend or holiday, and the business days remaining.'),
 ('t2-short-eligibility-checker', 'T2 Short Eligibility Checker',
  'All eight T2 Short conditions on one screen. The checker names the condition '
  'that fails, where one does.'),
 ('gifi-schedule-requirement-checker', 'GIFI Schedule Requirement Checker',
  'Five questions decide whether a nil T2 needs GIFI Schedules 100, 125 and '
  '141. Any one yes makes all three required.'),
 ('unfiled-years-cost-calculator', 'Unfiled Years Cost Calculator',
  'Enter how many tax years are unfiled and get the total, at ' + PRICE +
  ', with each year filed as its own return.'),
 ('schedule-50-shareholder-threshold-checker',
  'Schedule 50 Shareholder Threshold Checker',
  'Enter each shareholding and the checker names every shareholder at 10% or '
  'more, who must be listed on Schedule 50.'),
 ('53-week-first-tax-year-checker', '53-Week First Tax Year Checker',
  'Enter the incorporation date and a proposed year-end to see whether the '
  'first tax year is within the 53 weeks it may not exceed.'),
 ('schedule-24-first-return-checker', 'Schedule 24 First Return Checker',
  'Three questions decide whether your T2 is the corporation&rsquo;s first '
  'return and therefore carries Schedule 24.'),
 ('federal-annual-return-anniversary-calculator',
  'Federal Annual Return Anniversary Calculator',
  'Enter your federal incorporation date for the annual return due date, 60 '
  'days after the anniversary, at a $12.00 government fee.'),
 ('dormant-corporation-test', 'Dormant Corporation Test',
  'Ten questions decide whether the corporation is nil for the tax year, or '
  'has activity that puts it outside a nil return.'),
 ('gst-hst-nil-filing-checker', 'GST/HST Nil Filing Checker',
  'Three questions decide whether an open GST/HST or payroll account still '
  'needs nil filings, or whether Form RC145 closes it.'),
]

ALSO = [
 (SITE + '/guides/', 'Nil T2 Filing Guides',
  'Each guide covers one subject end to end, reviewed by a CPA Ontario member.'),
 (SITE + '/deadlines/', 'T2 Filing Deadlines',
  'Every fiscal year-end and its due date, with the business-day rule.'),
 (SITE + '/pricing/nil-t2-filing-cost/', 'Nil T2 Filing Cost',
  'What ' + PRICE + ' covers, and what falls outside a nil return.'),
]

# Copied from page 904 unchanged, so the two hubs cannot drift apart. No blank
# line anywhere inside, which is what keeps wpautop off it without a wrapper.
CSS = io.open(os.path.join(HERE, 'hub.css'), encoding='utf-8').read()


def card(href, title, desc):
    return ('<div class="ei-card"><h3><a href="' + href + '">' + title
            + '</a></h3><p>' + desc + '</p></div>')


def render():
    # The wp:html wrapper is not optional. Without it has_blocks() is false,
    # wpautop runs, and it inserted a stray </p> after the hero eyebrow, an
    # unclosed <p> around the CTA button and a <p> around the JSON-LD. The
    # [cnf_child_count] shortcode still resolves inside the block, because
    # do_shortcode runs on the_content at priority 11, after do_blocks at 9.
    # Both were confirmed against the rendered page, not just reasoned about.
    p = ['<!-- wp:html -->\n<style>\n', CSS, '</style>\n']
    p.append('<div class="ei-hero"><div class="ei-hero-inner">'
             '<span class="ei-hero-eyebrow">Tools</span>'
             '<h1>' + TITLE + '</h1>'
             '<p class="ei-hero-sub">' + META + '</p>'
             '<p class="ei-hero-by">Written and reviewed by Sharad Gondaliya, '
             'CPA (Ontario), CPA Ontario Membership 61040184.</p>'
             '<div class="ei-hero-btns"><a class="ei-btn-blue" href="' + FORM
             + '">Start Nil T2 Filing NOW</a></div></div></div>\n')

    p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
             '<h2 class="ei-h2">Every Tool on This Site</h2>\n'
             '<p class="ei-count">Tools published: '
             '<b>[cnf_child_count type="nil_calculator"]</b></p>\n'
             '<p>Each one answers a single question from the figures you enter, '
             'on one screen, with no sign-up. None of them is a filed return.</p>\n'
             '<div class="ei-cards">\n'
             + '\n'.join(card(HUB + s + '/', t, d) for s, t, d in TOOLS)
             + '\n</div>\n</div></div>\n')

    p.append('<div class="ei-section-alt"><div class="ei-wrap ei-art">\n'
             '<h2 class="ei-h2">Also on This Site</h2>\n<div class="ei-cards">\n'
             + '\n'.join(card(h, t, d) for h, t, d in ALSO)
             + '\n</div>\n<p class="ei-updated">Last reviewed: ' + TODAY
             + '</p>\n</div></div>\n')

    p.append('<div class="ei-cta-bottom"><div class="ei-wrap">'
             '<h2>Nil T2 Filing, ' + PRICE + '</h2>'
             '<p>Type your corporation name, pick your unfiled years, pay, and '
             'sign Form T183CORP on a secure screen. Your CRA confirmation is '
             'emailed within 3 business days.</p>'
             '<a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing '
             'NOW</a></div></div>\n')

    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "CollectionPage", "@id": HUB + "#webpage", "url": HUB,
       "name": PAGE_TITLE, "description": META, "inLanguage": "en-CA",
       "dateModified": ISO,
       "author": {"@type": "Person", "name": "Sharad Gondaliya",
                  "honorificSuffix": "CPA",
                  "url": SITE + "/sharad-gondaliya-cpa/"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
         "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": TITLE, "item": HUB}]}]}
    p.append('<script type="application/ld+json">'
             + json.dumps(schema, ensure_ascii=False)
             + '</script>\n<!-- /wp:html -->')
    return ''.join(p)


if __name__ == '__main__':
    html = render()
    io.open(os.path.join(HERE, 'tools-hub.html'), 'w',
            encoding='utf-8').write(html)
    print('tools-hub.html %d bytes, %d child cards' % (len(html.encode()),
                                                       len(TOOLS)))
