# -*- coding: utf-8 -*-
"""Family 7 comparison pages. First page: /compare/t2-short-vs-full-t2/.

WHICH PAGE AND WHY

Appendix A lists twenty F7 URLs, 14 concept and 6 brand. The 6 brand pages
need a competitor's published price with a dated screenshot, and this
environment's network policy denies competitor sites, so they cannot be built
here at all. Of the 14 concept pages, the plan's own keyword table (line 1272)
names this comparison the F7 priority at 60 searches a month and notes that the
concept comparison outranks the brand comparisons. It is also the only one whose
two price cells can be filled truthfully with no external input: both sides are
our own published fee, and they are the same figure. So it is both the page the
plan ranks first and the page that needs nothing from anyone.

THE URL, WHICH THE PLAN SPELLS THREE WAYS

Appendix A line 3266 says /t2-short-vs-full-t2/. The family table at line 1145
gives the base as /compare/<a>-vs-<b>/. The keyword table at line 1272 says
/compare/nil-t2-filing-vs-t2-short-filing/, a slug that appears nowhere in
Appendix A. Reconciled as the appendix slug on the family-table base:

    /compare/t2-short-vs-full-t2/

The third spelling is not built as a second URL: two URLs for one comparison is
the duplication line 1212 exists to prevent. Confirm the /compare/ base on the
first publish, because nil_cost resolves to /pricing/<slug>/ and the CPT UI
registration was never read directly.

THE DESIGN, AND THE EIGHT THINGS REMOVED FROM IT

Navneet supplied a gondaliyacpa.ca page as the design. Its visual system is
taken as given and the class names are kept unchanged, so the two sites can be
compared side by side; nothing on corpnilfilingfor300.ca used the si- prefix.

What could not come across, with the rule for each:

  FAQPage schema                 hard rule 6 forbids FAQPage outright. The
                                 sample carries a thirty-question block of it.
                                 Kept the accordion, dropped the schema, and
                                 built it on <details> so it works without JS.
  "Book Free Consultation", and
  two links to /consultation/    hard rule 7: no booking widget and no "book a
                                 call" anywhere. Replaced with the filing form
                                 and the eligibility checker.
  "30-Day Money-Back Guarantee"  hard rule 4 bars guaranteed. Removed.
  "1450+ Five-Star Reviews"      hard rule 6 bars review and aggregateRating
                                 schema and keeps Trustindex snippets off; a
                                 review count is the same claim in prose.
  "Flat fee, including HST"      hard rule 9 fixes the price wording, and
                                 Navneet's standing correction makes it plus
                                 HST. Every figure here reads $300.00 plus HST
                                 per tax year.
  $30,000, 3%, 15 characters,
  RC/RT/RP/RM/RZ                 the plan states none of these. Unsourced
                                 figures are not published; see build_f2h.py's
                                 refusal block for the same decision.
  telephone +16472129559 and
  AccountingService schema       that is the sister office's number on the
                                 sister domain. This site uses WebPage plus
                                 BreadcrumbList, as all 80 tools and 36 service
                                 pages do.
  No byline, no review stamp     7.5 rules 1 and 3 require both on every page.
                                 Added under the answer card.

WHAT F7 ADDS THAT THE SAMPLE HAS NO SLOT FOR

Line 1215 is the publish gate: two published price cells, eight published
feature cells, and no negative claim. Line 1568 requires a dated price-checked
line above the comparison table. Line 1529 caps the page at 20 outbound links,
requires 3 inbound, and requires any external competitor link to be nofollow.
This page names no competitor, so it carries the disclosure in the form that is
true of it rather than the form written for a brand page, which is a deviation
to put to Sharad Gondaliya with the template.
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
T = SITE + '/tools/'
G = SITE + '/guides/'
COST = SITE + '/pricing/nil-t2-filing-cost/'
BASE = SITE + '/compare/'

PRICE = '$300.00 plus HST per tax year'
TODAY, ISO = 'November 4, 2026', '2026-11-04'
BYLINE = ('Written and reviewed by <a href="' + SITE
          + '/sharad-gondaliya-cpa/">Sharad Gondaliya, CPA (Ontario)</a>, '
          'CPA Ontario Membership 61040184.')
EFILE = ('Gondaliya CPA Professional Corporation is a registered EFILE '
         'electronic filer. Returns are prepared and transmitted in Canada. '
         'Credentials are never shared and never used offshore.')
# Line 1215's required disclosure, in the form that is true of a concept page.
DISCLOSURE = ('This comparison sets two of our own filing routes against each '
              'other and names no other provider. Where a comparison on this '
              'site does name one, it states that provider&rsquo;s published '
              'prices and published features only.')

# The sample's stylesheet, class names unchanged. Raw string: the tick and plus
# markers are CSS escapes and a normal string would read \2713 as octal.
CSS = r"""<style>
.si-wrap{max-width:900px;margin:0 auto;padding:0 20px}.si-btn-blue{background:rgba(32,135,201,1);color:#fff !important;padding:13px 26px;border-radius:6px;font-weight:700;text-transform:uppercase;text-decoration:none !important;display:inline-block}.si-btn-dark{background:#1a2340;color:#fff !important;padding:13px 26px;border-radius:6px;font-weight:700;text-transform:uppercase;text-decoration:none !important;display:inline-block}.si-section{padding:40px 20px}.si-section-alt{background:#f7f9fc;padding:40px 20px}.si-section-dark{background:#1a2340;padding:40px 20px}.si-h2{font-weight:800;color:#1a2340;margin:0 0 10px}.si-h2c{font-weight:800;color:#1a2340;margin:0 0 10px;text-align:center}.si-subc{color:#718096;max-width:640px;margin:0 auto 28px;text-align:center}.article p{color:#4a5568;line-height:1.8;max-width:760px}.article a{color:rgba(32,135,201,1)}.article h3{font-weight:700;color:#1a2340;margin:0 0 8px}.si-info{background:#f0f7fd;border-left:4px solid rgba(32,135,201,1);border-radius:0 8px 8px 0;padding:14px 18px;margin:18px 0}.si-info p{margin:0;color:#1a2340;line-height:1.7}.si-warn{background:#fffbf0;border-left:4px solid #f6ad1a;border-radius:0 8px 8px 0;padding:14px 18px;margin:18px 0}.si-warn p{margin:0;color:#7c5800;line-height:1.7}.si-hero{background:linear-gradient(135deg,#0f1624 0%,#1a2340 55%,#1e3a6e 100%);padding:52px 20px}.si-hero-inner{max-width:800px;margin:0 auto;text-align:center}.si-hero-eyebrow{display:inline-block;background:rgba(32,135,201,0.15);border:1px solid rgba(32,135,201,0.4);border-radius:50px;padding:5px 16px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:rgba(32,135,201,1);margin-bottom:16px;font-size:.8em}.si-hero h1{color:#fff;font-weight:800;line-height:1.2;margin:0 0 14px;font-size:2.1em}.si-hero h1 span{color:#f6ad1a}.si-hero-sub{color:rgba(255,255,255,0.78);max-width:660px;margin:0 auto 22px;line-height:1.75}.si-hero-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}.si-answer{background:#fff;border:2px solid rgba(32,135,201,1);border-radius:12px;padding:26px 30px;max-width:860px;margin:-34px auto 0;box-shadow:0 10px 30px rgba(15,22,36,0.10);position:relative;z-index:2}.si-answer h2{font-weight:800;color:#1a2340;margin:0 0 10px;font-size:1.15em}.si-answer p{margin:0;color:#2d3748;line-height:1.75}.si-tbl{width:100%;border-collapse:collapse;margin:18px 0;border:1px solid #d1d5db}.si-tbl th{background:#1a2340;color:#fff;font-weight:700;padding:12px 14px;text-align:left;border:1px solid #374151}.si-tbl td{padding:10px 14px;border:1px solid #d1d5db;color:#2d3748;line-height:1.5}.si-tbl tr:nth-child(even){background:#f7f9fc}.si-tbl tr:hover{background:#edf2f7}.si-tbl .si-hl{background:#fffbf0;font-weight:600}.si-check{list-style:none;padding:0;margin:16px 0}.si-check li{padding:7px 0;border-bottom:1px solid #e2e8f0;display:flex;align-items:flex-start;gap:10px;color:#2d3748;line-height:1.6}.si-check li::before{content:"\2713";color:#2d9c4b;font-weight:700;flex-shrink:0;margin-top:1px}.si-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin:28px 0}.si-card{background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:24px 20px;border-top:3px solid rgba(32,135,201,1)}.si-card h3{font-weight:700;color:#1a2340;margin:0 0 10px}.si-card p{color:#718096;line-height:1.65}.si-section-dark .si-card{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.14);border-top:3px solid #f6ad1a}.si-section-dark .si-card h3{color:#fff!important}.si-section-dark .si-card p{color:rgba(255,255,255,0.75)!important}.si-case{background:#f0f7fd;border-radius:12px;padding:26px 30px;max-width:820px;margin:0 auto}.si-case h3{font-weight:800;color:#1a2340;margin:0 0 10px}.si-case p{margin:0;color:#2d3748;line-height:1.75}.si-faq-list{max-width:860px;margin:28px auto 0}.si-faq-list details{border:1px solid #e2e8f0;border-radius:8px;margin-bottom:10px;background:#fff}.si-faq-list summary{padding:17px 20px;font-weight:600;color:#1a2340;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:14px}.si-faq-list summary::-webkit-details-marker{display:none}.si-faq-list summary::after{content:"+";color:rgba(32,135,201,1);font-weight:400;font-size:1.4em;line-height:1;flex-shrink:0;transition:transform .15s ease}.si-faq-list details[open] summary{color:rgba(32,135,201,1)}.si-faq-list details[open] summary::after{transform:rotate(45deg)}.si-faq-a{padding:0 20px 16px;color:#718096;line-height:1.7}.si-faq-a p{margin:0;color:#718096;line-height:1.7}.si-faq-a a{color:rgba(32,135,201,1)}.si-cta-bottom{background:linear-gradient(135deg,#0f1624,#1a2340);padding:56px 20px;text-align:center}.si-cta-bottom h2{color:#fff;font-weight:800;margin:0 0 10px}.si-cta-bottom p{color:rgba(255,255,255,0.72);max-width:540px;margin:0 auto 22px}.si-cta-feats{display:flex;justify-content:center;gap:26px;flex-wrap:wrap;margin-bottom:26px}.si-cta-feat{color:rgba(255,255,255,.72);display:flex;align-items:center;gap:6px}.si-cta-feat::before{content:"\2713";color:#f6ad1a;font-weight:700}
.si-crumb{font-size:14px;color:#636363;margin:20px 0 0}.si-crumb a{color:#314d8a;text-decoration:none}
.si-by{font-size:15px;color:#4a5568;margin:12px 0 0}.si-by a{color:rgba(32,135,201,1)}
.si-rev{font-size:15px;color:#718096;margin:2px 0 0}
.si-meta{padding-bottom:0}
.si-lead{padding-top:22px}
.si-section>.si-wrap>:last-child,.si-section-alt>.si-wrap>:last-child{margin-bottom:0}
.si-stamp{font-size:14px;color:#636363;margin:0 0 6px}
.entry-header{display:none!important}
.ast-article-single,.ast-article-single .entry-content{margin-top:0;padding-top:0}
/* width held twice: on the wrap, and on each element that would stretch if the theme overrides the wrap */
.si-section>.si-wrap,.si-section-alt>.si-wrap,.si-section-dark>.si-wrap{max-width:900px;margin-left:auto;margin-right:auto}
.si-wrap .si-tbl,.si-wrap .si-info,.si-wrap .si-warn,.si-wrap .si-check,.si-wrap .si-cards,.si-wrap .si-h2,.si-wrap .si-stamp{max-width:860px}
.si-wrap .si-h2c{max-width:860px;margin-left:auto;margin-right:auto}
.si-section,.si-section-alt,.si-section-dark{padding-left:max(20px,calc((100% - 900px)/2));padding-right:max(20px,calc((100% - 900px)/2))}
@media(max-width:900px){.si-cards{grid-template-columns:1fr}}
@media(max-width:600px){.si-hero h1{font-size:1.6em}.si-answer{padding:20px 22px}}
</style>"""


# The eight T2 Short conditions, in the order the live checker asks them.
# Copied from the published tool rather than restated, so the two cannot drift.
SHORT8 = [
 'The corporation is a Canadian-controlled private corporation throughout the '
 'tax year.',
 'It has nil net income, or a loss, for income tax purposes this year.',
 'It has one permanent establishment only.',
 'It paid no taxable dividends and received none in the year.',
 'It reports in Canadian currency.',
 'It is claiming no refundable credits.',
 'It has no Ontario transitional tax debit.',
 'It has no amount calculated under section 34.2.',
]

# Line 1215: two published price cells and eight published feature cells. In a
# two-column comparison that reads as two price rows and eight feature rows,
# every cell filled on both sides. PRICE_ROWS and FEATURE_ROWS are separate so
# gate.py can count them apart, and cnf_feature_rows_json records both.
PRICE_ROWS = [
 ('Our published fee for a quiet year', PRICE, PRICE, True),
 ('A second quiet tax year', PRICE, PRICE, True),
]

FEATURE_ROWS = [
 ('Which corporations may use it',
  'Only where all eight conditions hold',
  'Any corporation, with no eligibility test', True),
 ('Length of the form',
  'Two pages', 'The full return', True),
 ('Filing deadline',
  'Six months after the fiscal year-end',
  'Six months after the fiscal year-end', False),
 ('GIFI Schedules 100, 125 and 141',
  'Required where anything sits on the books',
  'Required where anything sits on the books', False),
 ('Schedule 24, first-time filer information',
  'On a first return', 'On a first return', False),
 ('Schedule 50, every shareholder at 10 per cent or more',
  'Required', 'Required', False),
 ('Form T183CORP',
  'Signed by an authorized signing officer before transmission',
  'Signed by an authorized signing officer before transmission', False),
 ('Filing route and confirmation',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days', False),
]

PAGE = dict(
 slug='t2-short-vs-full-t2',
 title='T2 Short vs Full T2 | What Actually Changes',
 h1='T2 Short vs Full T2',
 h1_pre='T2 Short vs ', h1_span='Full T2',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='t2 short vs full t2',
 meta=('Which of the two corporate return forms a quiet year uses, what the '
       'eight conditions decide, and the six things that are identical either '
       'way.'),
 seo_title='T2 Short vs Full T2 | What Changes',
 seo_desc=('Both forms are the same return at the same price. What the eight '
           'T2 Short conditions decide, and what stays identical either way.'),
 answer=('Both are the same return at the same price. The T2 Short is a '
         'two-page version of the T2 that a corporation may use only where it '
         'meets every one of the Canada Revenue Agency&rsquo;s eight '
         'conditions for the short return. Where one condition fails, the full '
         'T2 is the return instead. Either way the filing is ' + PRICE
         + ', carries the same schedules, is signed on the same Form T183CORP '
         'and is transmitted the same way.'),
 lead=[('Two Forms, One Return',
        ['<p>The T2 Short is not a lighter obligation or a cheaper service. It '
         'is a shorter version of the same corporate income tax return, and a '
         'corporation either qualifies to use it or does not. Nothing about '
         'the decision is ours to make and nothing about it changes what you '
         'pay.</p>',
         '<p>That is the whole answer, and it is worth stating plainly because '
         'the form is often discussed as though choosing it were a strategy. '
         'It is not a choice. The eight conditions decide it, and where one of '
         'them fails we file the full return at the same fee rather than a '
         'different one.</p>']),
       ],
 cards=[('Reviewed by a CPA',
         'Either form is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted. The review does not get shorter because the form '
         'does.'),
        ('The schedules are inside the fee',
         'GIFI Schedules 100, 125 and 141, Schedule 24 on a first return, '
         'Schedule 50, Schedule 8 and loss continuity, on whichever form '
         'applies.'),
        ('Transmitted and confirmed',
         'Transmitted electronically by a registered EFILE electronic filer, '
         'with your CRA confirmation emailed within 3 business days.')],
 case=('A corporation with a December 31 year-end and no activity in the year',
       'Its return is due the following June 30 on either form. Say it holds '
       'share capital from incorporation and a small bank balance, and nothing '
       'moved: the GIFI schedules are required because something sits on the '
       'books, Schedule 50 lists its sole shareholder, and the fee is ' + PRICE
       + '. If all eight conditions hold, that return goes on the two-page '
       'short form. If the corporation received a dividend, two conditions '
       'fail at once, the full return is used, and the year is no longer a nil '
       'year at all. The figures here illustrate how the rules apply and are '
       'not drawn from a client file.'),
 faq=[('Is the T2 Short cheaper than the full T2?',
       'No. Both are ' + PRICE + '. The T2 Short is included in the fee where '
       'a corporation qualifies for it rather than charged separately, and '
       'where it does not qualify we file the full return at the same fee.'),
      ('Can I choose to file the T2 Short?',
       'It is not a choice. A corporation may use the short return only where '
       'it meets every one of the eight conditions. Meeting seven is not '
       'enough, and we check all eight before the return is prepared.'),
      ('What is actually different between the two forms?',
       'Two things: which corporations may use it, and how long the form is. '
       'The deadline, the schedules, Form T183CORP, the filing route and the '
       'confirmation are the same on both.'),
      ('Does the short form mean fewer schedules?',
       'No. The schedules are decided by what sits on the corporation&rsquo;s '
       'books and by whether it is a first return, not by which form carries '
       'them. A quiet corporation holding share capital still files GIFI '
       'Schedules 100, 125 and 141 either way.'),
      ('Which condition fails most often?',
       'A dividend paid or received, and not being a Canadian-controlled '
       'private corporation throughout the year. Both also mean the year is '
       'not a nil year for this service, so they decide more than the form.'),
      ('Who decides which form my return goes on?',
       'The eight conditions do, tested against your corporation before the '
       'return is prepared. The '
       '<a href="' + T + 't2-short-eligibility-checker/">T2 Short eligibility '
       'checker</a> runs the same test you can run yourself.'),

      # --- the eight conditions, one at a time ---------------------------
      ('What does CCPC throughout the tax year mean?',
       'The corporation has to be a Canadian-controlled private corporation '
       'for every day of the year, not merely on the last day. A change of '
       'control partway through the year breaks the condition even where the '
       'corporation looks the same at the year-end.'),
      ('Does a loss year still qualify for the T2 Short?',
       'Yes. The condition is nil net income or a loss for income tax '
       'purposes, so a loss does not fail it. The loss still has to be '
       'reported and carried forward correctly, which is work the fee '
       'covers on either form.'),
      ('What counts as a permanent establishment?',
       'Broadly, a fixed place of business. The condition is that the '
       'corporation has one only. A corporation operating in two provinces '
       'generally has more than one, fails the condition and goes on the '
       'full return.'),
      ('Does receiving a dividend disqualify the T2 Short?',
       'Yes, and it does more than that. A taxable dividend received fails '
       'the condition outright, and it also means the year is not a nil year '
       'for this service at all.'),
      ('Does paying a dividend disqualify it?',
       'Yes. The condition covers taxable dividends both paid and received, '
       'so either direction fails it and the full return is used instead.'),
      ('What if the corporation reports in a currency other than Canadian dollars?',
       'The condition is that the corporation reports in Canadian currency. '
       'A corporation that has elected a functional currency fails it and '
       'files the full return.'),
      ('What is a refundable credit for this purpose?',
       'A credit the corporation can be paid out even where it owes no tax. '
       'Claiming one fails the condition. A genuinely quiet corporation '
       'usually claims nothing at all, so this condition rarely decides the '
       'form on its own.'),
      ('What is the Ontario transitional tax debit?',
       'A legacy Ontario amount arising from the move to federal '
       'administration of Ontario corporate tax. Where a corporation has one, '
       'the short return cannot be used. Most corporations incorporated since '
       'that transition do not.'),
      ('What is an amount calculated under section 34.2?',
       'An income adjustment for a corporation that is a member of a '
       'partnership with a different fiscal period. Where such an amount '
       'applies, the short return cannot be used.'),
      ('Does the number of shareholders affect eligibility?',
       'Not directly. None of the eight conditions counts shareholders. The '
       'shareholder list affects Schedule 50, which is required on either '
       'form for every shareholder holding 10 per cent or more.'),
      ('Does a corporation with no bank account qualify?',
       'Having no bank account does not fail any of the eight conditions. '
       'What the corporation holds affects which schedules are filed, not '
       'which form carries them.'),
      ('Can a corporation that has never traded use the T2 Short?',
       'Yes, where the eight conditions hold. A corporation that never began '
       'operating still owes a return for each tax year since incorporation, '
       'and each of those years is '
       + PRICE + '.'),

      # --- the schedules --------------------------------------------------
      ('Which schedules does a quiet corporation actually file?',
       'Commonly GIFI Schedules 100, 125 and 141, Schedule 50 where a '
       'shareholder holds 10 per cent or more, and Schedule 24 on a first '
       'return. Loss continuity is added where there is a loss to carry. '
       'The list is the same on either form.'),
      ('Why is Schedule 100 required if nothing happened?',
       'Schedule 100 is the balance sheet. A corporation that issued shares '
       'at incorporation has share capital sitting on its books whether or '
       'not it traded, so there is a balance sheet to report even in a year '
       'with no activity.'),
      ('When is Schedule 24 required?',
       'On a first return. It carries the first-time filer information, and '
       'it is required on the first return whichever form that return '
       'goes on.'),
      ('When is Schedule 50 required?',
       'Where a shareholder holds 10 per cent or more of any class of '
       'shares. A single-shareholder corporation is over that threshold by '
       'definition, so it files Schedule 50 on either form.'),
      ('Does the T2 Short include Schedule 8?',
       'Schedule 8 is capital cost allowance. It is filed where the '
       'corporation has depreciable property, on either form. A corporation '
       'holding nothing but share capital and a bank balance normally has '
       'none.'),
      ('Do the schedules cost extra?',
       'No. Every schedule the corporation needs is inside '
       + PRICE + ', on whichever form applies.'),

      # --- filing, signing and confirmation -------------------------------
      ('When is the return due on either form?',
       'Six months after the fiscal year-end, the same on both. A December '
       '31 year-end is due the following June 30.'),
      ('Is the deadline different for the short form?',
       'No. The form the return goes on does not move the deadline. Only the '
       'fiscal year-end sets it.'),
      ('Can the T2 Short be filed on paper?',
       'We transmit every return electronically as a registered EFILE '
       'electronic filer, and your confirmation is emailed within 3 business '
       'days. Whether a particular corporation is permitted to file on paper '
       'is a separate question and does not change which form its return '
       'goes on.'),
      ('How is Form T183CORP signed?',
       'An authorized signing officer signs Form T183CORP before the return '
       'is transmitted. That requirement is identical on both forms, and '
       'nothing is sent to the Canada Revenue Agency until it is signed.'),
      ('How long until the confirmation arrives?',
       'Your CRA confirmation is emailed within 3 business days of '
       'transmission, on either form.'),
      ('Does the form affect how the return is reviewed?',
       'No. Either form is prepared and reviewed by a CPA Ontario member '
       'before transmission. The review follows the corporation&rsquo;s '
       'facts, not the length of the form.'),

      # --- more than one year ---------------------------------------------
      ('Can past years be filed on the T2 Short?',
       'Yes, where the eight conditions held in that year. Eligibility is '
       'tested year by year against the facts of that year, not against the '
       'corporation as it stands today.'),
      ('What if one year qualifies and another does not?',
       'Each year goes on the form its own facts point to, so a corporation '
       'can file one year on the short return and the next on the full '
       'return. Every quiet year is '
       + PRICE + ' either way.'),
      ('Does switching forms between years cause a problem?',
       'No. The returns are filed year by year and the Canada Revenue Agency '
       'assesses each on its own. A year on the full return does not oblige '
       'the following year to use it.'),
      ('Is the price different if several years are filed at once?',
       'No. The fee is '
       + PRICE + ', counted per year, however many years are filed together.'),
      ('Which checker should I run first?',
       'The '
       '<a href="' + T + 't2-short-eligibility-checker/">T2 Short eligibility '
       'checker</a> tests all eight at once. Where it returns not eligible, '
       'the '
       '<a href="' + T + 't2-short-exclusion-checker/">exclusion checker</a> '
       'names the condition that did it.')],
 related=[(T + 't2-short-eligibility-checker/',
           'T2 Short eligibility checker, all eight conditions'),
          (T + 't2-short-exclusion-checker/',
           'T2 Short exclusion checker, which condition excludes you'),
          (T + 't2-short-ccpc-condition-checker/',
           'CCPC condition checker, the first condition on its own'),
          (G + 't2-short-eligibility/', 'T2 Short eligibility'),
          (G + 't2-schedules-on-a-nil-return/',
           'T2 schedules on a nil return'),
          (COST, 'Nil T2 filing cost')],
)


def _rows(rows):
    out = []
    for item, a, b, differs in rows:
        cls = ' class="si-hl"' if differs else ''
        out.append('<tr%s><td>%s</td><td>%s</td><td>%s</td></tr>'
                   % (cls, item, a, b))
    return '\n'.join(out)


def render(p):
    url = BASE + p['slug'] + '/'
    h = ['<!-- wp:html -->\n', CSS, '\n']

    # Hero. The sample's two buttons were a consultation booking and a service
    # page on the sister domain; hard rule 7 forbids the first outright.
    h.append('<div class="si-hero"><div class="si-hero-inner">'
             '<div class="si-hero-eyebrow">' + p['eyebrow'] + '</div>'
             '<h1>' + p['h1_pre'] + '<span>' + p['h1_span'] + '</span></h1>'
             '<p class="si-hero-sub">' + p['meta'] + '</p>'
             '<div class="si-hero-btns">'
             '<a class="si-btn-blue" href="' + FORM + '">Start Nil T2 Filing '
             'NOW</a>'
             '<a class="si-btn-dark" href="' + T
             + 't2-short-eligibility-checker/">Check the Eight Conditions</a>'
             '</div></div></div>\n')

    # Answer card, overlapping the hero as the sample does, then the byline and
    # the review stamp 7.5 requires and the sample had nowhere for.
    h.append('<div class="si-section si-meta">'
             '<div class="si-wrap">'
             '<div class="si-answer"><h2>Quick Answer</h2><p>'
             + p['answer'] + '</p></div>\n'
             '<nav class="si-crumb" aria-label="Breadcrumb">'
             '<a href="' + SITE + '/">Nil T2 filing in Canada</a> &rsaquo; '
             '<a href="' + COST + '">Nil T2 filing cost</a> &rsaquo; '
             '<span aria-current="page">' + p['h1'] + '</span></nav>\n'
             '<p class="si-by">' + BYLINE + '</p>\n'
             '<p class="si-rev">Last reviewed: ' + TODAY + '</p>\n'
             '</div></div>\n')

    for h2, paras in p['lead']:
        h.append('<div class="si-section si-lead"><div class="si-wrap article">\n'
                 '<h2 class="si-h2">' + h2 + '</h2>\n'
                 + '\n'.join(paras) + '\n</div></div>\n')

    # The comparison table, with the dated price line above it that line 1568
    # requires, and the line 1215 disclosure under it.
    h.append('<div class="si-section-alt" id="the-comparison">'
             '<div class="si-wrap article">\n'
             '<h2 class="si-h2">The Comparison, Row by Row</h2>\n'
             '<p class="si-stamp">Prices checked ' + TODAY + '. '
             'Both figures are our own published fee.</p>\n'
             '<table class="si-tbl"><thead><tr><th scope="col">Item</th>'
             '<th scope="col">T2 Short</th><th scope="col">Full T2</th></tr>'
             '</thead><tbody>\n'
             + _rows(PRICE_ROWS) + '\n' + _rows(FEATURE_ROWS) + '\n'
             '</tbody></table>\n'
             '<p>Two rows differ and eight do not, which is the page&rsquo;s '
             'whole argument put in a table. The form changes; the work, the '
             'deadline and the fee do not.</p>\n'
             '<div class="si-info"><p>' + DISCLOSURE + '</p></div>\n'
             '</div></div>\n')

    h.append('<div class="si-section"><div class="si-wrap article">\n'
             '<h2 class="si-h2">The Eight Conditions Decide It</h2>\n'
             '<p>A corporation may use the short return only where every one '
             'of these holds for the tax year:</p>\n'
             '<ul class="si-check">\n'
             + '\n'.join('<li>%s</li>' % c for c in SHORT8)
             + '\n</ul>\n'
             '<div class="si-warn"><p>Meeting seven of the eight is not '
             'enough. One condition failing puts the corporation on the full '
             'return, which we file at the same fee rather than a different '
             'one.</p></div>\n'
             '<p>The <a href="' + T + 't2-short-eligibility-checker/">T2 Short '
             'eligibility checker</a> tests all eight at once, the '
             '<a href="' + T + 't2-short-exclusion-checker/">exclusion '
             'checker</a> names which one excludes you, and the '
             '<a href="' + T + 't2-short-ccpc-condition-checker/">CCPC '
             'condition checker</a> takes the first condition on its own.</p>\n'
             '<div class="si-info"><p>' + EFILE + '</p></div>\n'
             '</div></div>\n')

    h.append('<div class="si-section-dark"><div class="si-wrap">\n'
             '<h2 class="si-h2c" style="color:#fff;">The Same Work Either '
             'Way</h2>\n'
             '<p style="text-align:center;color:rgba(255,255,255,0.65);'
             'max-width:680px;margin:0 auto;">Whichever form the conditions '
             'point to, the return is prepared, reviewed and transmitted the '
             'same way, at ' + PRICE + '.</p>\n'
             '<div class="si-cards" style="margin-top:28px;">\n'
             + '\n'.join('<div class="si-card"><h3>%s</h3><p>%s</p></div>'
                         % (t, d) for t, d in p['cards'])
             + '\n</div>\n'
             '<div style="text-align:center;margin-top:28px;">'
             '<a class="si-btn-blue" href="' + FORM + '">Start Nil T2 Filing '
             'NOW</a></div>\n'
             '</div></div>\n')

    ch, cb = p['case']
    h.append('<div class="si-section-alt"><div class="si-wrap">'
             '<div class="si-case"><h3>' + ch + '</h3><p>' + cb + '</p></div>'
             '</div></div>\n')

    # FAQ on <details>, so it opens without JavaScript. No FAQPage schema:
    # hard rule 6, which the sample breaches thirty times over.
    h.append('<div class="si-section"><div class="si-wrap">\n'
             '<h2 class="si-h2c">Frequently Asked Questions</h2>\n'
             '<div class="si-faq-list">\n'
             + '\n'.join('<details><summary>%s</summary>'
                         '<div class="si-faq-a"><p>%s</p></div></details>'
                         % (q, a) for q, a in p['faq'])
             + '\n</div>\n</div></div>\n')

    h.append('<div class="si-section-alt"><div class="si-wrap article">\n'
             '<h2 class="si-h2">Read Next</h2>\n<ul class="si-check">\n'
             + '\n'.join('<li><a href="%s">%s</a></li>' % (u, t)
                         for u, t in p['related'])
             + '\n</ul>\n</div></div>\n')

    h.append('<div class="si-cta-bottom">'
             '<h2>Nil T2 Filing, ' + PRICE + '</h2>'
             '<p>Type your corporation name, pick your unfiled years, pay, and '
             'sign Form T183CORP on a secure screen. Your CRA confirmation is '
             'emailed within 3 business days.</p>'
             '<div class="si-cta-feats">'
             '<div class="si-cta-feat">Registered EFILE electronic filer</div>'
             '<div class="si-cta-feat">Prepared and transmitted in Canada</div>'
             '<div class="si-cta-feat">Reviewed by a CPA Ontario member</div>'
             '<div class="si-cta-feat">One price per tax year</div>'
             '</div>'
             '<a class="si-btn-blue" href="' + FORM + '">Start Nil T2 Filing '
             'NOW</a></div>\n')

    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "WebPage", "@id": url + "#webpage", "url": url,
       "name": p['title'], "description": p['meta'], "inLanguage": "en-CA",
       "dateModified": ISO,
       "author": {"@type": "Person", "name": "Sharad Gondaliya",
                  "honorificSuffix": "CPA",
                  "url": SITE + "/sharad-gondaliya-cpa/"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1,
         "name": "Nil T2 filing in Canada", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Nil T2 filing cost",
         "item": COST},
        {"@type": "ListItem", "position": 3, "name": p['h1'], "item": url}]}]}
    h.append('<script type="application/ld+json">'
             + json.dumps(schema, ensure_ascii=False) + '</script>\n'
             '<!-- /wp:html -->')
    return ''.join(h), url


def meta(p):
    return {
     'site-sidebar-layout': 'no-sidebar', 'site-content-layout': 'page-builder',
     'ast-site-content-layout': 'full-width-container',
     'site-post-title': 'disabled', 'ast-breadcrumbs-content': 'disabled',
     'ast-featured-img': 'disabled',
     # A concept comparison names no competitor, so the three competitor
     # fields stay empty rather than carrying a placeholder that would read
     # as data.
     'cnf_competitor_name': '', 'cnf_competitor_published_price': '',
     'cnf_competitor_intake_method': '',
     # Named _incl_hst by the plan, left empty because the standing correction
     # makes the price plus HST and writing a plus-HST figure into a field
     # named incl_hst would be a false record. The fee is in the rows below.
     'cnf_our_price_incl_hst': '',
     'cnf_feature_rows_json': json.dumps({
        'price_rows': [{'item': i, 't2_short': a, 'full_t2': b}
                       for i, a, b, _d in PRICE_ROWS],
        'feature_rows': [{'item': i, 't2_short': a, 'full_t2': b,
                          'differs': d} for i, a, b, d in FEATURE_ROWS],
        'our_price': PRICE,
        'competitor_named': False,
        'price_source': 'Our own published fee, not a competitor price'}),
     'cnf_price_checked_on': ISO,
     'cnf_last_verified_et': ISO,
     'cnf_primary_keyword': p['keyword'],
     'rank_math_title': p['seo_title'],
     'rank_math_description': p['seo_desc'],
     'rank_math_focus_keyword': p['keyword'],
    }


if __name__ == '__main__':
    assert len(PRICE_ROWS) == 2, 'line 1215 wants two price rows'
    assert len(FEATURE_ROWS) == 8, 'line 1215 wants eight feature rows'
    for _i, _a, _b, _d in PRICE_ROWS + FEATURE_ROWS:
        assert _a.strip() and _b.strip(), '%s: an empty cell' % _i
    assert len(SHORT8) == 8, 'the eight conditions'
    assert len(PAGE['faq']) == 35
    assert len(PAGE['related']) == 6
    assert len(PAGE['cards']) == 3
    assert len(PAGE['seo_title']) <= 60, len(PAGE['seo_title'])
    assert 70 <= len(PAGE['seo_desc']) <= 160, len(PAGE['seo_desc'])
    html, url = render(PAGE)
    io.open(os.path.join(HERE, PAGE['slug'] + '.html'), 'w',
            encoding='utf-8').write(html)
    json.dump([dict(slug=PAGE['slug'], title=PAGE['title'], url=url,
                    content=html, **meta(PAGE))],
              io.open(os.path.join(HERE, 'f7-manifest.json'), 'w',
                      encoding='utf-8'), ensure_ascii=False, indent=1)
    print('%-26s %6d bytes   %s' % (PAGE['slug'], len(html.encode()), url))
