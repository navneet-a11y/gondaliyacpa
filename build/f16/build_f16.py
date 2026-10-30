"""Family 16 hub: /guides/

  line 1154   F16 is 5 hubs on post type `page`: /services/, /tools/,
              /locations/, /guides/, /blog/. "Each hub links every child in
              its family."
  line 1224   GATE: "No hub publishes without a live child count and links to
              every child family." Unique data block is the "Live child count
              for that family", sourced from a "WordPress query count, cached
              hourly by LiteSpeed Cache", and "Child counts update
              automatically and are never hand-typed." Banned phrase for this
              family: "complete list of every accountant".
  line 350    Intended template is a Loop Grid. Theme Builder is unproven on
              this install, so the child list is written by the pipeline and
              the count is a shortcode. See the note below.
  6(g) F16    20 inbound minimum, 400 outbound maximum, mandatory targets
              "Every child family", anchor "Child title". Hubs are exempt from
              the 40-link body cap.
  7.9 1570    F16 takes its visible date in the footer of the article body.

The count is NOT written into the HTML. `[cnf_child_count type="nil_guide"]`
renders it from a live wp_count_posts call, because line 1224 forbids a
hand-typed number. The shortcode is registered by the WPCode snippet in
docs/hub-child-count-snippet.md, which must be installed before this page
renders correctly.

Appendix A conflict. Appendix A's Family 16 names five entirely different
hubs: /what-we-file/, /who-this-is-for/, /provinces/, /all-calculators/ and
/service-areas/. 6(a) is followed here, corroborated by the 6(g) Home row,
which names the same five as the home page's mandatory targets.
"""
import io, json, os, re as _re

SITE = 'https://corpnilfilingfor300.ca'
FORM = SITE + '/form/'
URL  = SITE + '/guides/'
TODAY = 'October 30, 2026'
PRICE = '$300.00 plus HST per tax year'

TITLE = 'Nil T2 Filing Guides for Canadian Corporations'
H1    = 'Nil T2 Filing Guides'
META  = ('In-depth guides to filing a nil T2 corporate return in Canada, written and '
         'reviewed by a CPA Ontario member. Nil T2 filing is ' + PRICE + '.')
BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')
# Children: every published nil_guide, in seven groups.
#
# OCTOBER 30, 2026. The live page carried 12 cards against 30 published
# guides, so it failed line 1224's second half the same way /tools/ did. All
# thirty are now carded. The twelve descriptions that were live are unchanged
# except for one spelling fix noted below; the other eighteen were written for
# this pass.
#
# Thirty cards in one grid is a wall, so they sit in groups with their own H2.
# Line 1224 requires every child to be linked and says nothing about the shape
# of the list. The count line stays a shortcode.
#
# guides-hub-children.json holds every published slug, read from the site, and
# the assertion below compares the cards against it. A guide published without
# a card now fails this script rather than going quietly unlinked.
GROUPS = [
 ('Start Here', [
  ('nil-t2-return-complete-guide', 'The Complete Guide to the Nil T2 Return',
   'Who must file, what counts as nil, which GIFI schedules and other schedules are '
   'required, how Form T183CORP is signed, filing deadlines, and what unfiled years '
   'cost.'),
  ('how-to-file-a-nil-t2-return', 'How to File a Nil T2 Return',
   'What you need before you start, confirming the fiscal year-end, choosing the '
   'form, the schedules, CPA review, signing Form T183CORP and transmission.'),
  ('zero-activity-corporate-tax-returns',
   'Zero-Activity Corporate Tax Returns',
   'What a year with no transactions still has to report, and why no activity '
   'describes the figures rather than excusing the return.'),
  ('t2-schedules-on-a-nil-return', 'T2 Schedules on a Nil Return',
   'Every schedule a nil return can carry, what puts each one on it, and why all '
   'of them sit inside the fee.'),
  ('small-business-corporate-filing', 'Small Business Corporate Filing',
   'What a small corporation files in a quiet year, and where the line falls '
   'between a nil return and one that needs more.'),
 ]),

 ('Dormant, Inactive and Numbered Corporations', [
  ('dormant-and-inactive-corporations',
   'The Complete Guide to Dormant and Inactive Corporations',
   'What dormant and inactive actually mean, why there is no dormancy filing, when '
   'a dormant corporation is still nil, and whether to keep it or wind it up.'),
  ('inactive-holding-company-filing', 'Inactive Holding Company Filing',
   'Why a holding corporation with investment income is not nil, and what an '
   'inactive one files instead.'),
  ('shelf-corporation-compliance', 'Shelf Corporation Compliance',
   'A corporation incorporated and left on the shelf still owes a return for every '
   'year since. What that takes to put right.'),
  ('numbered-company-tax-filing',
   'The Complete Guide to Numbered Company Tax Filing',
   'Why a numbered company files exactly like a named one, shelf corporations, and '
   'when a numbered holding corporation is not a nil filer.'),
  ('numbered-company-maintenance', 'Numbered Company Maintenance',
   'What keeping a numbered company in good standing involves: the return, the '
   'registry filing, and the accounts nobody closed.'),
 ]),

 ('Deadlines, Year-Ends and the Calendar', [
  ('t2-filing-deadlines', 'The Complete Guide to T2 Filing Deadlines',
   'The six-month rule, the balance date that comes before it, the weekend and '
   'holiday shift, and every date that follows from a year-end.'),
  ('choosing-and-changing-a-fiscal-year-end',
   'Choosing and Changing a Fiscal Year-End',
   'How the first year-end is chosen, what the 53-week limit allows, and what '
   'moving it later costs in approval and in returns.'),
  ('corporate-compliance-calendar', 'The Corporate Compliance Calendar',
   'Every recurring obligation a corporation has in a year, which body each one '
   'goes to, and which of them the fee covers.'),
  ('first-year-t2-filing', 'The Complete Guide to First-Year T2 Filing',
   'When the first tax year starts, the 53-week rule, choosing a year-end, '
   'Schedule 24, and why first transmissions are the ones most often rejected.'),
 ]),

 ('The Forms, Schedules and Transmission', [
  ('t2-short-eligibility', 'The Complete Guide to T2 Short Eligibility',
   'The eight conditions for the two-page T2 Short, what disqualifies a '
   'corporation from using it, and which schedules are still required either way.'),
  ('gifi-schedules-100-125-141',
   'The Complete Guide to GIFI Schedules 100, 125 and 141',
   'What each schedule reports, the narrow case where a nil return may omit them, '
   'and why share capital or a shareholder loan makes them required.'),
  ('schedule-8-and-loss-continuity',
   'The Complete Guide to Schedule 8 and Loss Continuity',
   'Capital cost allowance in a nil year, why claiming nil usually beats claiming '
   'the maximum, and what a skipped year does to the continuity.'),
  ('schedule-50-and-shareholder-reporting',
   'Schedule 50 and Shareholder Reporting',
   'The 10 percent threshold, who has to be named on it, and what share capital on '
   'the books means for the rest of the return.'),
  ('mandatory-t2-electronic-filing', 'Mandatory T2 Electronic Filing',
   'Electronic filing is mandatory for tax years starting after 2023, what that '
   'means on a catch-up, and what filing on paper costs.'),
  # "authorises" was live in this description until October 30: British
  # spelling in Canadian English copy, and the sentence reads better without
  # the word at all.
  ('t183corp-signing-and-transmission',
   'The Complete Guide to Form T183CORP Signing and Transmission',
   'What Form T183CORP permits, who may sign it, when and how it is signed, how '
   'long it is kept, and what EFILE transmission involves.'),
 ]),

 ('Unfiled Years, Penalties and CRA Letters', [
  ('catch-up-unfiled-corporate-tax-returns',
   'The Complete Guide to Catching Up on Unfiled Corporate Tax Returns',
   'How many years can still be filed, the order to file them in, what a demand to '
   'file and an arbitrary assessment mean, and what the catch-up costs.'),
  ('t2-late-filing-penalties', 'The Complete Guide to T2 Late Filing Penalties',
   'How the late-filing penalty is worked out, why a true nil year sits '
   'differently, and the costs that do not depend on tax owing.'),
  ('cra-demand-to-file-response', 'Responding to a CRA Demand to File',
   'What a demand letter is, the date it names, what an arbitrary assessment does, '
   'and the order to answer it in.'),
  ('corporate-tax-arrears-and-interest',
   'Corporate Tax Arrears and Interest',
   'How arrears build on a balance that was owing, and why a nil year gives them '
   'nothing to build on.'),
 ]),

 ('CRA Accounts, Annual Returns and the Provinces', [
  ('cra-accounts-on-a-dormant-corporation',
   'CRA Accounts on a Dormant Corporation',
   'Payroll and GST/HST accounts outlive the activity that opened them. What each '
   'still expects, and how Form RC145 closes it.'),
  ('provincial-and-federal-annual-returns',
   'The Complete Guide to Provincial and Federal Annual Returns',
   'The Ontario annual return, the $12.00 Corporations Canada annual return, '
   'Alberta AT1 and Quebec CO-17, and why the T2 covers none of them.'),
  ('quebec-co17-and-alberta-at1', 'Quebec CO-17 and Alberta AT1',
   'Two provinces collect their own corporate tax. Why each is a separate return, '
   'and what the federal T2 does not reach.'),
  ('non-resident-owned-corporation-nil-filing',
   'Non-Resident-Owned Corporation Nil Filing',
   'A non-resident-owned corporation is charged $25.00 per day up to $2,500.00 on '
   'a late return, nil or not, which changes the order of the work.'),
 ]),

 ('Winding Up and Dissolution', [
  ('final-t2-and-dissolution',
   'The Complete Guide to the Final T2 and Dissolution',
   'When the final T2 is due, what period it covers, why a clearance certificate '
   'matters, and the order of operations for closing a corporation.'),
  ('winding-up-an-inactive-corporation',
   'Winding Up an Inactive Corporation',
   'The whole sequence for closing a corporation down: the outstanding returns, '
   'the accounts, the clearance request and the registry filing.'),
 ]),
]

GUIDES = [g for _h, items in GROUPS for g in items]

_LIVE = set(json.load(io.open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 'guides-hub-children.json'), encoding='utf-8'))['slugs'])
_CARDED = [s for s, _t, _d in GUIDES]
assert len(_CARDED) == len(set(_CARDED)), 'a guide is carded twice'
assert not (_LIVE - set(_CARDED)), (
    '%d published guides have no hub card, which breaches line 1224: %s'
    % (len(_LIVE - set(_CARDED)), sorted(_LIVE - set(_CARDED))))
assert not (set(_CARDED) - _LIVE), (
    'the hub cards a guide that is not published: %s'
    % sorted(set(_CARDED) - _LIVE))
for _s, _t, _d in GUIDES:
    assert _d.endswith('.'), '%s: description does not end in a full stop' % _s
    assert 60 <= len(_d) <= 230, '%s: description is %d chars' % (_s, len(_d))
assert not _re.search(r'authoris|organis|recognis',
                      ' '.join(d for _s, _t, d in GUIDES)), 'British spelling'

RELATED = [
 (SITE + '/deadlines/', 'T2 Filing Deadlines',
  'Every fiscal year-end and its due date, with the business-day rule.'),
 (SITE + '/pricing/nil-t2-filing-cost/', 'Nil T2 Filing Cost',
  'What ' + PRICE + ' covers, and what falls outside a nil return.'),
 (SITE + '/catch-up-nil-t2-filing/', 'Catch-Up Nil T2 Filing',
  'Filing several outstanding years at once, each as its own return.'),
]

CSS = """<style>
.ei-wrap{max-width:1100px;margin:0 auto;padding:0 20px}
.ei-btn-blue{background:rgba(32,135,201,1);color:#fff !important;padding:13px 26px;border-radius:6px;font-weight:700;font-size:0.95em;text-transform:uppercase;text-decoration:none !important;display:inline-block;line-height:1.4;text-align:center;min-width:120px}
.ei-section{padding:26px 20px}
.ei-section-alt{background:#f7f9fc;padding:26px 20px}
.ei-art .ei-h2{font-weight:800;color:#1a2340;margin:0 0 10px;font-size:1.45em;line-height:1.3}
.ei-art > *:last-child{margin-bottom:0}
.ei-art p{color:#4a5568;line-height:1.8}
.ei-art a{color:rgba(32,135,201,1)}
.ei-hero{background:linear-gradient(135deg,#0f1624 0%,#1a2340 55%,#1e3a6e 100%);padding:40px 20px}
.ei-hero-inner{max-width:860px;margin:0 auto;text-align:center}
.ei-hero-eyebrow{display:inline-block;background:rgba(32,135,201,0.15);border:1px solid rgba(32,135,201,0.4);border-radius:50px;padding:5px 16px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:rgba(32,135,201,1);margin-bottom:16px;font-size:.8em}
.ei-hero h1{color:#fff;font-weight:800;line-height:1.2;margin:0 0 14px;font-size:2.1em}
.ei-hero-sub{color:rgba(255,255,255,0.78);max-width:720px;margin:0 auto 10px;line-height:1.75}
.ei-hero-by{color:rgba(255,255,255,0.6);max-width:720px;margin:0 auto 22px;line-height:1.6;font-size:.86em}
.ei-hero-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.ei-hero-btns a,.ei-hero-btns a:visited,.ei-hero-btns a:hover,.ei-cta-bottom a,.ei-cta-bottom a:visited,.ei-cta-bottom a:hover{color:#fff !important;text-decoration:none !important}
.ei-count{display:inline-flex;align-items:baseline;gap:8px;background:#f0f7fd;border:1px solid #cfe4f6;border-radius:50px;padding:6px 16px;margin:0 0 14px;color:#4a5568;font-size:.9em}
.ei-count b{color:rgba(32,135,201,1);font-size:1.2em;font-weight:800}
.ei-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;margin:16px 0 0}
.ei-card{border:1px solid #e2e8f0;border-radius:10px;background:#fff;padding:18px 20px;transition:box-shadow .15s ease,border-color .15s ease}
.ei-card:hover{border-color:#cfe4f6;box-shadow:0 2px 10px rgba(26,35,64,.07)}
.ei-card h3{margin:0 0 6px;font-size:1.08em;font-weight:700;line-height:1.35}
.ei-card h3 a{color:#1a2340;text-decoration:none}
.ei-card:hover h3 a{color:rgba(32,135,201,1)}
.ei-card p{margin:0;color:#4a5568;font-size:.94em;line-height:1.65}
.ei-updated{color:#718096;font-size:.88em;border-top:1px solid #e2e8f0;padding-top:14px;margin:26px 0 0}
.ei-cta-bottom{background:linear-gradient(135deg,#0f1624,#1a2340);padding:40px 20px;text-align:center}
.ei-cta-bottom h2{color:#fff;font-weight:800;margin:0 0 10px;font-size:1.5em}
.ei-cta-bottom p{color:rgba(255,255,255,0.72);max-width:600px;margin:0 auto 22px;line-height:1.75}
.entry-header{display:none!important}
.ast-article-single,.ast-article-single .entry-content{margin-top:0;padding-top:0}
@media(max-width:900px){.ei-hero h1{font-size:1.6em}.ei-art .ei-h2{font-size:1.3em}}
</style>
"""

def card(href, title, desc):
    return ('<div class="ei-card"><h3><a href="%s">%s</a></h3><p>%s</p></div>'
            % (href, title, desc))

p = [CSS]
p.append('<div class="ei-hero"><div class="ei-hero-inner">'
 '<span class="ei-hero-eyebrow">Guides</span>'
 '<h1>' + H1 + '</h1>'
 '<p class="ei-hero-sub">' + META + '</p>'
 '<p class="ei-hero-by">' + BYLINE + '</p>'
 '<div class="ei-hero-btns"><a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing NOW</a></div>'
 '</div></div>\n')

# The lead-in carries the count and nothing else, then one section per group.
p.append('<div class="ei-section"><div class="ei-wrap ei-art">\n'
 '<h2 class="ei-h2">Every Guide on This Site</h2>\n'
 # line 1224: the count is rendered live by the WPCode shortcode in
 # docs/hub-child-count-snippet.md, never hand-typed. Label-first so it
 # reads correctly at one guide as well as at thirty.
 '<p class="ei-count">Guides published: <b>[cnf_child_count type="nil_guide"]</b></p>\n'
 '<p>Each guide covers one subject end to end, is reviewed by a CPA Ontario member, and '
 'carries the date it was last reviewed. They are grouped below by subject.</p>\n'
 '</div></div>\n')

for _i, (_heading, _items) in enumerate(GROUPS):
    _cls = 'ei-section-alt' if _i % 2 == 0 else 'ei-section'
    p.append('<div class="' + _cls + '"><div class="ei-wrap ei-art">\n'
     '<h2 class="ei-h2">' + _heading + '</h2>\n'
     '<div class="ei-cards">\n'
     + '\n'.join(card(SITE + '/guides/' + _s + '/', _t, _d)
                 for _s, _t, _d in _items)
     + '\n</div>\n</div></div>\n')

rel_cards = '\n'.join(card(h, t, d) for h, t, d in RELATED)
# Keep the bands alternating: whatever the last group used, this takes the
# other one. Hardcoding alt put two grey bands next to each other at seven
# groups.
_ALSO_CLS = 'ei-section' if (len(GROUPS) - 1) % 2 == 0 else 'ei-section-alt'
p.append('<div class="' + _ALSO_CLS + '"><div class="ei-wrap ei-art">\n'
 '<h2 class="ei-h2">Also on This Site</h2>\n'
 '<div class="ei-cards">\n' + rel_cards + '\n</div>\n'
 '<p class="ei-updated">Last reviewed: ' + TODAY + '</p>\n'
 '</div></div>\n')

p.append('<div class="ei-cta-bottom"><div class="ei-wrap">'
 '<h2>Nil T2 Filing, ' + PRICE + '</h2>'
 '<p>Type your corporation name, pick your unfiled years, pay, and sign Form T183CORP on '
 'a secure screen. Your CRA confirmation is emailed within 3 business days.</p>'
 '<a class="ei-btn-blue" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
 '</div></div>\n')

schema = {"@context": "https://schema.org", "@graph": [
 {"@type": "CollectionPage", "@id": URL + "#webpage", "url": URL, "name": TITLE,
  "description": META, "inLanguage": "en-CA", "dateModified": "2026-10-30",
  "author": {"@type": "Person", "name": "Sharad Gondaliya", "honorificSuffix": "CPA",
             "url": SITE + "/sharad-gondaliya-cpa/"}},
 {"@type": "BreadcrumbList", "itemListElement": [
   {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada", "item": SITE + "/"},
   {"@type": "ListItem", "position": 2, "name": H1, "item": URL}]}]}
p.append('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False)
         + '</script>')

html = ''.join(p)
d = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(d, 'guides-hub.html'), 'w', encoding='utf-8').write(html)
print('built /guides/  %d bytes, %d guide cards in %d groups, %d related'
      % (len(html.encode()), len(GUIDES), len(GROUPS), len(RELATED)))
for _h, _it in GROUPS:
    print('  %-46s %2d' % (_h, len(_it)))
