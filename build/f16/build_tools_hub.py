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

OCTOBER 30, 2026: TEN CARDS TO SIXTY, AND WHY THEY ARE GROUPED

The hub shipped with the ten tools 6(e) names and was never extended as
batches 4 to 8 published. On October 30 it linked 10 of 60 children, which
fails line 1224's second half: a hub links every child in its family. All
sixty are now carded.

Sixty cards in one grid is a wall, so they sit in ten groups with their own
H2. Line 1224 requires every child to be linked and says nothing about the
shape of the list, and ten headed groups also give the page ten descriptive
headings where it had one. The count line stays a shortcode: the number is
never hand-typed, and the groups do not change that.

`tools-hub-children.json` holds every published slug, read from the site.
The build asserts the cards match it exactly, so the next tool published
without a card fails this script instead of going quietly unlinked. That is
the check whose absence let this gap open in the first place.
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
HUB = SITE + '/tools/'
FORM = SITE + '/form/'
TODAY, ISO = 'October 30, 2026', '2026-10-30'
PRICE = '$300.00 plus HST per tax year'
TITLE = 'Nil T2 Filing Tools and Calculators'
PAGE_TITLE = 'Nil T2 Filing Tools and Calculators for Canadian Corporations'
META = ('Free tools and calculators for a nil T2 corporate return in Canada. '
        'Deadlines, T2 Short eligibility, GIFI schedules, unfiled years and '
        'more. Nil T2 filing is ' + PRICE + '.')
# Sixty children in ten groups. The first ten descriptions are the ones that
# shipped with the hub on October 23 and are unchanged; the other fifty were
# written for this pass. Each is one sentence saying what the tool answers,
# because a card that restates the title tells a visitor nothing.
GROUPS = [
 ('Deadlines and Dates', [
  ('nil-t2-deadline-calculator', 'Nil T2 Deadline Calculator',
   'Enter your fiscal year-end and get the T2 due date, the next business day '
   'where it falls on a weekend or holiday, and the business days remaining.'),
  ('next-t2-due-date-checker', 'Next T2 Due Date Checker',
   'Which return is the next one owed, and when, for a corporation that files '
   'on an ordinary annual cycle.'),
  ('corporate-balance-due-date-calculator',
   'Corporate Balance Due Date Calculator',
   'Paying a balance of tax comes due before the return does. Two months '
   'after the year-end, or three for a qualifying CCPC.'),
  ('short-tax-year-deadline-calculator', 'Short Tax Year Deadline Calculator',
   'A short tax year still gets the full six months. Enter a stub period to '
   'see the date it lands on.'),
  ('final-t2-return-due-date-calculator',
   'Final T2 Return Due Date Calculator',
   'The last return runs to the dissolution date. Enter that date for the '
   'deadline on the final T2.'),
  ('amalgamation-t2-due-date-calculator',
   'Amalgamation T2 Due Date Calculator',
   'An amalgamation ends each predecessor&rsquo;s tax year the day before. '
   'The dates for every return it creates.'),
  ('due-date-weekend-holiday-shift-calculator',
   'Due Date Weekend and Holiday Shift Calculator',
   'Whether a date moves, and to when, against Ontario&rsquo;s nine public '
   'holidays and both weekend days.'),
  ('business-days-between-dates-calculator',
   'Business Days Between Dates Calculator',
   'Calendar days, business days, weekend days and every public holiday in a '
   'span, with both ends counted.'),
  ('days-overdue-calculator', 'Days Overdue Calculator',
   'How far past its deadline an unfiled return is, counted in calendar days '
   'and in business days.'),
  ('corporate-deadline-calendar-generator',
   'Corporate Deadline Calendar Generator',
   'One year-end in, the whole year out: the balance date, the T2 date, the '
   'T4 date and the annual return.'),
  ('cra-demand-to-file-deadline-calculator',
   'CRA Demand to File Deadline Calculator',
   'A demand names a date. Enter the letter date and the days it allows for '
   'the deadline and the time left.'),
 ]),

 ('Choosing and Changing a Year-End', [
  ('corporate-fiscal-year-end-calculator',
   'Corporate Fiscal Year End Calculator',
   'What a chosen year-end means for the filing date, and how the two move '
   'together from year to year.'),
  ('first-t2-year-end-options-generator',
   'First T2 Year-End Options Generator',
   'Every month-end available as a first year-end, with the length of the '
   'first tax year and its T2 date.'),
  ('53-week-first-tax-year-checker', '53-Week First Tax Year Checker',
   'Enter the incorporation date and a proposed year-end to see whether the '
   'first tax year is within the 53 weeks it may not exceed.'),
  ('year-end-change-impact-calculator',
   'Year-End Change Impact Calculator',
   'Moving a year-end creates a period and a return. The length of it, its '
   'deadline, and the approval needed.'),
  ('fiscal-period-length-calculator', 'Fiscal Period Length Calculator',
   'A period in days and weeks, whether it clears the 53-week limit, and the '
   'T2 date that follows it.'),
  ('two-t2-returns-in-one-year-checker',
   'Two T2 Returns in One Year Checker',
   'Two tax years can both come due in one calendar year. Both deadlines and '
   'the gap between them.'),
 ]),

 ('Is a Return Owed, and Is the Year Nil', [
  ('t2-filing-requirement-checker', 'T2 Filing Requirement Checker',
   'Whether a return is owed for this year at all, and the one case in which '
   'nothing is.'),
  ('nil-t2-eligibility-checker', 'Nil T2 Eligibility Checker',
   'Whether the year qualifies as nil, or has something in it that puts the '
   'return outside a nil filing.'),
  ('dormant-corporation-test', 'Dormant Corporation Test',
   'Ten questions decide whether the corporation is nil for the tax year, or '
   'has activity that puts it outside a nil return.'),
  ('dormant-corporation-obligation-checker',
   'Dormant Corporation Obligation Checker',
   'What a dormant corporation still owes while it stays open, and which of '
   'those filings the fee covers.'),
  ('inactive-corporation-filing-checker',
   'Inactive Corporation Filing Checker',
   'An inactive corporation still files. What else it owes alongside the '
   'return, and to whom.'),
  ('nil-return-vs-full-return-checker', 'Nil Return vs Full Return Checker',
   'Where the line falls between a nil return and a full one, and what '
   'crosses it.'),
  ('tax-years-since-incorporation-calculator',
   'Tax Years Since Incorporation Calculator',
   'How many tax years a corporation has had since it was incorporated, '
   'which is how many returns it owes.'),
 ]),

 ('The Return Itself: Schedules and GIFI', [
  ('t2-short-eligibility-checker', 'T2 Short Eligibility Checker',
   'All eight T2 Short conditions on one screen. The checker names the condition '
   'that fails, where one does.'),
  ('required-schedules-checker', 'Required Schedules Checker',
   'The whole schedule set behind one set of answers: the GIFI schedules, '
   'Schedule 24, Schedule 50 and Schedule 8.'),
  ('gifi-schedule-requirement-checker', 'GIFI Schedule Requirement Checker',
   'Five questions decide whether a nil T2 needs GIFI Schedules 100, 125 and '
   '141. Any one yes makes all three required.'),
  ('nil-gifi-balance-sheet-checker', 'Nil GIFI Balance Sheet Checker',
   'What Schedule 100 has to carry on a quiet year, and which balances end '
   'the nil year altogether.'),
  ('gifi-schedule-125-checker', 'GIFI Schedule 125 Checker',
   'Schedule 125 is the income statement. Whether it goes on the return, and '
   'whether a bank charge puts a figure on it.'),
  ('gifi-schedule-141-checker', 'GIFI Schedule 141 Checker',
   'The notes checklist: who prepared the statements, and why neither audited '
   'nor reviewed is a complete answer.'),
  ('balance-sheet-balancing-checker', 'Balance Sheet Balancing Checker',
   'Assets must equal liabilities plus equity or Schedule 100 will not '
   'validate. Enter the three totals for the difference.'),
  ('retained-earnings-rollforward-calculator',
   'Retained Earnings Rollforward Calculator',
   'Opening, plus net income, less dividends, gives closing: the figure the '
   'next return opens from.'),
  ('schedule-8-cca-requirement-checker', 'Schedule 8 CCA Requirement Checker',
   'Whether Schedule 8 belongs on the return, and why a carried balance is '
   'enough on its own.'),
  ('schedule-24-first-return-checker', 'Schedule 24 First Return Checker',
   'Three questions decide whether your T2 is the corporation&rsquo;s first '
   'return and therefore carries Schedule 24.'),
  ('nil-t2-document-checklist-checker', 'Nil T2 Document Checklist Checker',
   'What you need to hand before filing a nil return, and what you do not '
   'need to find.'),
  ('mandatory-t2-efile-checker', 'Mandatory T2 E-Filing Checker',
   'Electronic filing is mandatory for tax years starting after 2023. One '
   'date decides which side a year falls on.'),
  ('t183corp-signature-requirement-checker',
   'Form T183CORP Signature Requirement Checker',
   'Who may sign, when it is signed, how long the firm keeps it, and whether '
   'it goes to the Canada Revenue Agency.'),
 ]),

 ('Shareholders and Share Capital', [
  ('schedule-50-shareholder-threshold-checker',
   'Schedule 50 Shareholder Threshold Checker',
   'Enter each shareholding and the checker names every shareholder at 10% or '
   'more, who must be listed on Schedule 50.'),
  ('share-capital-reporting-checker', 'Share Capital Reporting Checker',
   'Shares issued at incorporation make the GIFI schedules required. What '
   'else the shares on your books trigger.'),
  ('shareholder-loan-balance-checker', 'Shareholder Loan Balance Checker',
   'A loan balance makes the GIFI schedules required even where it never '
   'moved, and either direction counts.'),
 ]),

 ('Unfiled Years and Catching Up', [
  ('unfiled-years-checker', 'Unfiled Years Checker',
   'Which tax years are outstanding, listed year by year from the '
   'incorporation date.'),
  ('unfiled-years-cost-calculator', 'Unfiled Years Cost Calculator',
   'Enter how many tax years are unfiled and get the total, at ' + PRICE +
   ', with each year filed as its own return.'),
  ('catch-up-filing-schedule-generator',
   'Catch-Up Filing Schedule Generator',
   'A dated row per outstanding year, oldest first, with each deadline and '
   'how overdue it is.'),
  ('nil-return-late-penalty-checker', 'Nil Return Late Penalty Checker',
   'What a late nil return does and does not cost, with the whole '
   'qualification rather than a headline.'),
 ]),

 ('CRA Accounts, Payroll and GST/HST', [
  ('business-number-status-checker', 'Business Number Status Checker',
   'Which accounts sit on the business number, and which of them are still '
   'generating returns.'),
  ('cra-account-closure-sequencer', 'CRA Account Closure Sequencer',
   'The order for closing payroll and GST/HST accounts, and what each step '
   'costs.'),
  ('gst-hst-nil-filing-checker', 'GST/HST Nil Filing Checker',
   'Three questions decide whether an open GST/HST or payroll account still '
   'needs nil filings, or whether Form RC145 closes it.'),
  ('gst-hst-account-closure-checker', 'GST/HST Account Closure Checker',
   'What it takes to close a GST/HST account, and what stays due until it is '
   'closed.'),
  ('payroll-nil-remittance-checker', 'Payroll Nil Remittance Checker',
   'An open payroll account expects remittances even where nobody was paid. '
   'What is owed and when.'),
  ('t4-nil-filing-requirement-checker', 'T4 Nil Filing Requirement Checker',
   'Whether a T4 information return is expected on an open payroll account '
   'with no wages, and its date.'),
 ]),

 ('Annual Returns and the Registry', [
  ('annual-return-vs-tax-return-checker',
   'Annual Return vs Tax Return Checker',
   'Two filings that share a word and nothing else, set side by side with '
   'what happens when each is missed.'),
  ('federal-annual-return-anniversary-calculator',
   'Federal Annual Return Anniversary Calculator',
   'Enter your federal incorporation date for the annual return due date, 60 '
   'days after the anniversary, at a $12.00 government fee.'),
  ('federal-annual-return-fee-calculator',
   'Federal Annual Return Fee Calculator',
   'A dated schedule of anniversaries and deadlines, at $12.00 a year with no '
   'HST on a government fee.'),
  ('involuntary-dissolution-risk-checker',
   'Involuntary Dissolution Risk Checker',
   'A missed annual return gets a corporation struck rather than charged, and '
   'the tax years survive it.'),
 ]),

 ('Winding Up and Dissolution', [
  ('dissolution-readiness-checker', 'Dissolution Readiness Checker',
   'Whether the corporation is ready to be dissolved, or has something '
   'outstanding that has to come first.'),
  ('dissolve-or-keep-filing-cost-calculator',
   'Dissolve or Keep Filing Cost Calculator',
   'Years of filing totalled against winding up, with the steps this fee does '
   'not cover named rather than guessed.'),
  ('clearance-certificate-requirement-checker',
   'Clearance Certificate Requirement Checker',
   'When a clearance certificate is needed before distributing, and what the '
   'request rests on.'),
 ]),

 ('Provincial, Non-Resident and Director Exposure', [
  ('provincial-return-requirement-checker',
   'Provincial Return Requirement Checker',
   'Quebec collects through CO-17 and Alberta through AT1. Whether either is '
   'a separate return for you.'),
  ('non-resident-t2-penalty-calculator', 'Non-Resident T2 Penalty Calculator',
   'A non-resident-owned corporation is charged $25.00 per day up to '
   '$2,500.00 on a late return, nil or not.'),
  ('director-liability-exposure-checker',
   'Director Liability Exposure Checker',
   'Which amounts can be assessed against a director personally, and which '
   'cannot reach past the corporation.'),
 ]),
]

TOOLS = [t for _h, items in GROUPS for t in items]

# Line 1224: a hub links every child in its family. The list of children is
# read from the site, not from this file, so a tool published without a card
# fails the build here.
_LIVE = set(json.load(io.open(os.path.join(HERE, 'tools-hub-children.json'),
                              encoding='utf-8'))['slugs'])
_CARDED = [s for s, _t, _d in TOOLS]
assert len(_CARDED) == len(set(_CARDED)), (
    'the same tool is carded twice: %s'
    % sorted({s for s in _CARDED if _CARDED.count(s) > 1}))
_missing = _LIVE - set(_CARDED)
_ghost = set(_CARDED) - _LIVE
assert not _missing, (
    '%d published tools have no hub card, which breaches line 1224: %s'
    % (len(_missing), sorted(_missing)))
assert not _ghost, (
    'the hub cards a tool that is not published: %s' % sorted(_ghost))

for _s, _t, _d in TOOLS:
    assert _d.endswith('.'), '%s: description does not end in a full stop' % _s
    assert 40 <= len(_d) <= 190, (
        '%s: description is %d characters' % (_s, len(_d)))
    assert _d.lower() != _t.lower(), (
        '%s: the description only restates the title' % _s)

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

    # The lead-in carries the count and nothing else, then one section per
    # group. Sixty cards in a single grid is a wall; ten headed groups give a
    # visitor somewhere to start and the page ten descriptive headings.
    p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
             '<h2 class="ei-h2">Every Tool on This Site</h2>\n'
             '<p class="ei-count">Tools published: '
             '<b>[cnf_child_count type="nil_calculator"]</b></p>\n'
             '<p>Each one answers a single question from the figures you enter, '
             'on one screen, with no sign-up. None of them is a filed return. '
             'They are grouped below by the question they answer.</p>\n'
             '</div></div>\n')

    for i, (heading, items) in enumerate(GROUPS):
        cls = 'ei-section-alt' if i % 2 == 0 else 'ei-section'
        p.append('<div class="' + cls + '"><div class="ei-wrap ei-art">\n'
                 '<h2 class="ei-h2">' + heading + '</h2>\n'
                 '<div class="ei-cards">\n'
                 + '\n'.join(card(HUB + sl + '/', t, d) for sl, t, d in items)
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
    print('tools-hub.html %d bytes, %d child cards in %d groups'
          % (len(html.encode()), len(TOOLS), len(GROUPS)))
    for h, items in GROUPS:
        print('  %-48s %2d' % (h, len(items)))
