#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, the brand pages. Pages 15 and 16:

  /compare/corpnilfilingfor300-vs-cloudtax/
  /compare/corpnilfilingfor300-vs-bluepeak/

Why these two first
-------------------
Navneet's instruction on 2026-11-09 was to use the prices the plan already
holds. Line 1568 holds six of them, "Prices checked September 20, 2026":
BluePeak $100.00, TurboTax $175.00, T2inc $199.00 and $299.00, TaxDeep
$200.00, H&R Block $449.00, CloudTax pay-what-you-want.

These two are built first because they are the two ends of what that
instruction produces, and the difference is worth seeing before the other four
are written to the same pattern:

  CloudTax  -- captured from cloudtax.ca on 2026-11-06, so the competitor
               column carries real published detail and a current date.
  BluePeak  -- the plan's figure and nothing else, so the competitor column is
               one price and eight cells that say the published price does not
               state it.

Both are honest. Only one is informative. That is a fact about the source
material, not about the template, and the pages say so rather than papering
over it.

The capture date is the date of the capture
-------------------------------------------
build_f7.py now takes price_checked separately from TODAY. Before that, the
"Prices checked" line and the "Last reviewed" line both printed the build
date, so building a brand page today would have claimed a competitor's price
was re-checked today. It was not. BluePeak's stamp reads September 20, 2026,
because that is when Sharad Gondaliya captured it; CloudTax's reads November
6, 2026, because that is when this session captured it. cnf_price_checked_on
follows the same date.

check_competitor() in build_f7.py refuses a brand page that lacks the
competitor's name, the price, the capture date and its ISO form, refuses one
whose stamp is silently the build date, and refuses a comparative or negative
word anywhere in the answer, the table or the note. Line 1215 puts a Rule 217
review on each of these pages for exactly that reason.

What the competitor column may hold
-----------------------------------
Only what the provider publishes. Where the published price we hold does not
state something, the cell says so in those terms. It never says "no", because
"not stated" and "no" are different claims and only one of them is sourced.

What this page cannot do, and does not try to
---------------------------------------------
CloudTax publishes Pay What You Want including $0 for eligible nil returns. An
honest table shows that against $300.00 plus HST per tax year, and hard rule 4
bars any cheapest claim while line 1215 bars any negative one. So the page
states both prices and then says what the fee covers. It does not argue.

Agreeing with what is already published
---------------------------------------
Our own column is drawn from the live site and nothing else: the fee, the CPA
Ontario review, the registered EFILE electronic filer line, Form T183CORP on a
secure screen, the CRA confirmation within 3 business days, and the schedules
the fee covers.
"""
import os

import build_f7
from build_f7 import check, write, PRICE, COST, T, G, FORM

HERE = os.path.dirname(os.path.abspath(__file__))

build_f7.TODAY, build_f7.ISO = 'November 9, 2026', '2026-11-09'

US = 'corpnilfilingfor300.ca'
NS = 'Not stated in the published price we hold.'
NS_PAGE = 'Not stated on the page captured.'

# Our side, written once. Every cell is on the live site today.
OURS = {
 'covers': 'The T2 itself, GIFI Schedules 100, 125 and 141 where required, '
           'Schedule 50, Schedule 24 on a first return, Schedule 8 and loss '
           'continuity, and electronic transmission',
 # Worded to avoid the literal substring "reviews", which gate.py bans as a
 # rule 6 review-claim guard. "Reviewed by" says the same thing.
 'who': 'Prepared and reviewed by a CPA Ontario member before it is '
        'transmitted',
 'transmit': 'Transmitted by a registered EFILE electronic filer, prepared '
             'and transmitted in Canada',
 'sign': 'Form T183CORP signed on a secure screen',
 'confirm': 'The CRA confirmation is emailed within 3 business days',
 'unit': 'One price for one tax year, for one corporation',
 'offshore': 'Credentials are never shared and never used offshore',
 'overflow': 'A year that is not nil is handled by Gondaliya CPA Professional '
             'Corporation at gondaliyacpa.ca at $350.00 plus HST per year',
}


def rows(their_covers, their_who, their_transmit, their_sign, their_confirm,
         their_unit, their_offshore, their_overflow):
    """The eight feature rows. Our column is fixed; theirs is whatever the
    provider publishes, cell by cell."""
    return [
     ('What the price covers', OURS['covers'], their_covers, True),
     ('Who prepares the return', OURS['who'], their_who, True),
     ('How it reaches the Canada Revenue Agency', OURS['transmit'],
      their_transmit, True),
     ('How the return is signed', OURS['sign'], their_sign, True),
     ('When the confirmation arrives', OURS['confirm'], their_confirm, True),
     ('What one price buys', OURS['unit'], their_unit, True),
     ('Where the work is done', OURS['offshore'], their_offshore, True),
     ('A year that turns out not to be nil', OURS['overflow'], their_overflow,
      True),
    ]


def disclosure(name, when):
    return ('This comparison states ' + name + '&rsquo;s published prices and '
            'published features only, as published on ' + when + ', and makes '
            'no claim about them beyond that. Prices change: the figure here '
            'is the one published on that date, not a quotation, and '
            + name + ' is the place to confirm it.')


# ======================================================================
# Page 15: CloudTax. Captured from cloudtax.ca on 2026-11-06.
# ======================================================================
CLOUDTAX = dict(
 competitor='CloudTax',
 competitor_price='Pay What You Want, including $0, for eligible nil returns',
 price_checked='November 6, 2026', price_checked_iso='2026-11-06',
 col_a=US, col_b='CloudTax',
 price_rows=[
  ('Published price for a nil T2 return',
   PRICE,
   'Pay What You Want, including $0, for eligible corporations with no '
   'activity. Its corporate page also publishes a Nil Return tier at $199.00 '
   'per year, and states on that same page that nil T2 returns start at '
   '$250.00', True),
  ('What else the published price list holds',
   'One price. There is no tier above or below it for a nil year',
   'T2 Basic DIY at $199.00 per year-end, Review and File at $499.00 per '
   'year-end, and Done For You from $749.00 per year-end', True),
 ],
 feature_rows=rows(
  'Its nil offer is described as being for eligible corporations with no '
  'activity or simple startup costs. What the filing itself includes is not '
  'stated on the page captured',
  NS_PAGE,
  NS_PAGE,
  NS_PAGE,
  NS_PAGE,
  'Priced per year-end on the tiers above',
  NS_PAGE,
  'Its tiers above the nil offer are priced for returns that are not nil'),
 faq_n=10,
 stamp=('Our figure is our own <a href="' + COST + '">published fee</a>. '
        'The CloudTax figures were captured from cloudtax.ca on that date and '
        'are its published prices, not a quotation.'),
 disclosure=disclosure('CloudTax', 'November 6, 2026'),
 table_note=('Two things about the right-hand column. Its nil offer is a Pay '
             'What You Want model including $0, so the lowest published '
             'figure on this page is not ours. And CloudTax publishes more '
             'than one nil figure on its own site, $199.00 per year on one '
             'part of its corporate page and $250.00 on another, so both are '
             'stated here rather than one being picked.'),
 slug='corpnilfilingfor300-vs-cloudtax',
 title=US + ' vs CloudTax | Published Prices',
 h1=US + ' vs CloudTax',
 h1_pre=US + ' vs ', h1_span='CloudTax',
 eyebrow='Comparison &#183; Published Prices &#183; Canada',
 keyword='corpnilfilingfor300 vs cloudtax',
 meta=('Published prices and published features, side by side. Nil T2 filing '
       'here is ' + PRICE + '. CloudTax publishes Pay What You Want, '
       'including $0, for eligible nil returns.'),
 seo_title=US + ' and CloudTax Compared',
 seo_desc=('Side-by-side published prices and published features. Nil T2 '
           'filing here is $300.00 plus HST per tax year; CloudTax prices '
           'captured November 6, 2026.'),
 answer=('Both file a nil T2 corporate return and the published prices are '
         'not alike. Nil T2 filing here is ' + PRICE + ', one price for one '
         'tax year, covering the return, its schedules where required, a CPA '
         'Ontario review and electronic transmission. CloudTax publishes a '
         'Pay What You Want model for eligible nil returns, including $0, '
         'alongside a Nil Return tier at $199.00 per year and higher tiers '
         'for returns that are not nil. Those figures were captured from '
         'cloudtax.ca on November 6, 2026 and are its published prices '
         'rather than a quotation.'),
 cta2=('What the Fee Covers', COST),
 lead=[('Two Published Prices, Stated as Published',
        ['<p>This page does one thing: it puts the published price and the '
         'published features of each side in one table, on a stated date. It '
         'makes no claim about which is better value, because that depends on '
         'what a particular corporation needs and because a comparison page '
         'is not the place to argue it.</p>',
         '<p>The lowest published figure here is not ours. CloudTax publishes '
         'a Pay What You Want model for eligible nil returns, including $0. '
         'That is its published position and it is stated plainly above.</p>',
         '<p>What the right-hand column does not hold is detail. Its '
         'published pages give prices and the eligibility of the nil offer; '
         'they do not state who prepares the return, how it is signed, or '
         'when a confirmation arrives. Those cells say so rather than '
         'guessing.</p>']),
       ],
 detail=dict(
  h2='What the Fee Here Covers',
  intro=('Since the prices differ, what each one buys is the part worth '
         'reading. Ours covers:'),
  items=[
   'The T2 itself, and GIFI Schedules 100, 125 and 141 where the corporation '
   'has anything to report.',
   'Schedule 50 for any shareholder at 10% or more, Schedule 24 on a first '
   'return, and Schedule 8 with loss continuity carried forward intact.',
   'Preparation and review by a CPA Ontario member before anything is '
   'transmitted.',
   'Transmission by a registered EFILE electronic filer, prepared and '
   'transmitted in Canada, with credentials never shared and never used '
   'offshore.',
   'Form T183CORP signed on a secure screen, and the CRA confirmation '
   'emailed within 3 business days.',
   'One price for one tax year for one corporation, with no tier above or '
   'below it.',
  ],
  warn=('A year that turns out not to be nil is not covered by this fee. A '
        'holding corporation with investment income, a rental corporation and '
        'a corporation that paid or received a dividend are not nil. Those '
        'are handled by Gondaliya CPA Professional Corporation at '
        'gondaliyacpa.ca at $350.00 plus HST per year.'),
  close=''),
 band=('What the Fee Covers, in Full',
       'The cost page sets out the fee and everything inside it, and what '
       'falls outside a nil return.'),
 cards=[('Reviewed by a CPA',
         'Each return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('Published prices only',
         'The figures in the table are each side&rsquo;s published prices on '
         'the date above. Neither is a quotation.'),
        ('What sits outside the fee',
         'The Ontario annual return, the federal annual return, '
         'extra-provincial registrations, and closing a GST/HST or payroll '
         'account with Form RC145.')],
 case=('A dormant corporation with one shareholder and three unfiled years',
       'Here that is three returns at ' + PRICE + ', prepared oldest first, '
       'each reviewed by a CPA Ontario member and transmitted electronically, '
       'with Form T183CORP signed once for each year and a CRA confirmation '
       'for each within 3 business days. What the same three years would cost '
       'on the other column depends on which of its published tiers the '
       'corporation is eligible for, and its nil offer is a Pay What You Want '
       'model including $0. The figures here illustrate the published prices '
       'above and are not drawn from a client file.'),
 faq=[
  ('Is CloudTax cheaper?',
   'Its published nil offer is a Pay What You Want model including $0, and '
   'ours is ' + PRICE + '. Both figures are above, as published. What each '
   'one buys is the part this page sets out, and which suits a particular '
   'corporation is not something a comparison page can answer.'),
  ('When were these prices checked?',
   'The CloudTax figures were captured from cloudtax.ca on November 6, 2026. '
   'Prices change, so that date is stated above the table and its own site is '
   'the place to confirm them.'),
  ('Why are two different CloudTax nil figures shown?',
   'Because its corporate page publishes both. One part of that page gives a '
   'Nil Return tier at $199.00 per year and another states that nil T2 '
   'returns start at $250.00. Picking one would be choosing on its behalf.'),
  ('Why do so many cells say the price does not state it?',
   'Because they do not. The published pages captured give prices and the '
   'eligibility of the nil offer, not who prepares a return or how it is '
   'signed. An empty cell is reported as not stated rather than as a no.'),
  ('What does your fee include?',
   'The T2, GIFI Schedules 100, 125 and 141 where required, Schedule 50, '
   'Schedule 24 on a first return, Schedule 8 and loss continuity, a CPA '
   'Ontario review, and electronic transmission, at ' + PRICE + '.'),
  ('Is there a cheaper tier here?',
   'No. There is one price for a nil year, and no tier above or below it.'),
  ('Who actually files the return here?',
   'Gondaliya CPA Professional Corporation, a registered EFILE electronic '
   'filer. Returns are prepared and transmitted in Canada.'),
  ('What if my year is not nil after all?',
   'Then this fee does not cover it. It moves to Gondaliya CPA Professional '
   'Corporation at gondaliyacpa.ca at $350.00 plus HST per year.'),
  ('Do either of you file my annual return?',
   'Not as part of this fee. A registry annual return is a separate filing, '
   'which the <a href="' + T + 'annual-return-vs-tax-return-checker/">annual '
   'return versus tax return checker</a> sets out.'),
  ('Where can I see the whole fee?',
   'On the <a href="' + COST + '">nil T2 filing cost page</a>, which states '
   'the fee and everything inside it.'),
 ],
)

# ======================================================================
# Page 16: BluePeak. Plan line 1568 and nothing else.
# ======================================================================
BLUEPEAK = dict(
 competitor='BluePeak',
 competitor_price='$100.00',
 price_checked='September 20, 2026', price_checked_iso='2026-09-20',
 col_a=US, col_b='BluePeak',
 price_rows=[
  ('Published price for a nil T2 return', PRICE, '$100.00', True),
  ('What else the published price list holds',
   'One price. There is no tier above or below it for a nil year',
   NS, True),
 ],
 feature_rows=rows(NS, NS, NS, NS, NS, NS, NS, NS),
 faq_n=10,
 stamp=('Our figure is our own <a href="' + COST + '">published fee</a>. '
        'The BluePeak figure is its published price on that date, recorded by '
        'Sharad Gondaliya, CPA, and is not a quotation.'),
 disclosure=disclosure('BluePeak', 'September 20, 2026'),
 table_note=('The right-hand column holds what was published on the date '
             'above and no more. Where a cell says the published price does '
             'not state something, that is what it means: not that the answer '
             'is no, and not that it is unavailable. The price is seven weeks '
             'old at the time of writing and its own site is the place to '
             'confirm it.'),
 slug='corpnilfilingfor300-vs-bluepeak',
 title=US + ' vs BluePeak | Published Prices',
 h1=US + ' vs BluePeak',
 h1_pre=US + ' vs ', h1_span='BluePeak',
 eyebrow='Comparison &#183; Published Prices &#183; Canada',
 keyword='corpnilfilingfor300 vs bluepeak',
 meta=('Published prices side by side. Nil T2 filing here is ' + PRICE + '. '
       'BluePeak published $100.00 on September 20, 2026.'),
 seo_title=US + ' and BluePeak Compared',
 seo_desc=('Side-by-side published prices. Nil T2 filing here is $300.00 plus '
           'HST per tax year; the BluePeak figure is its published price on '
           'September 20, 2026.'),
 answer=('Nil T2 filing here is ' + PRICE + ', one price for one tax year, '
         'covering the return, its schedules where required, a CPA Ontario '
         'review and electronic transmission by a registered EFILE electronic '
         'filer. BluePeak published $100.00, recorded on September 20, 2026. '
         'That figure is its published price on that date rather than a '
         'quotation, and the published price we hold does not state what it '
         'includes, who prepares the return or how it is signed, so this page '
         'does not state those either.'),
 cta2=('What the Fee Covers', COST),
 lead=[('What This Page Can and Cannot Tell You',
        ['<p>It can tell you two published prices on a stated date, and it '
         'can tell you in full what the fee on this site covers. That is the '
         'whole of what it claims.</p>',
         '<p>What it cannot tell you is what the other price includes. The '
         'published price recorded on September 20, 2026 is a figure and not '
         'a description, so the right-hand column of the table says, cell by '
         'cell, that the published price does not state it. That is a fact '
         'about the source rather than about the provider, and it is not a '
         'criticism of them.</p>',
         '<p>Prices also move. Seven weeks have passed since that figure was '
         'recorded, and the date sits above the table so you can see how old '
         'it is. Its own site is the place to confirm it.</p>']),
       ],
 detail=dict(
  h2='What the Fee Here Covers',
  intro=('Since one column is a figure on its own, the useful detail is what '
         'the fee on this site buys:'),
  items=[
   'The T2 itself, and GIFI Schedules 100, 125 and 141 where the corporation '
   'has anything to report.',
   'Schedule 50 for any shareholder at 10% or more, Schedule 24 on a first '
   'return, and Schedule 8 with loss continuity carried forward intact.',
   'Preparation and review by a CPA Ontario member before anything is '
   'transmitted.',
   'Transmission by a registered EFILE electronic filer, prepared and '
   'transmitted in Canada, with credentials never shared and never used '
   'offshore.',
   'Form T183CORP signed on a secure screen, and the CRA confirmation '
   'emailed within 3 business days.',
   'One price for one tax year for one corporation, with no tier above or '
   'below it.',
  ],
  warn=('A year that turns out not to be nil is not covered by this fee. A '
        'holding corporation with investment income, a rental corporation and '
        'a corporation that paid or received a dividend are not nil. Those '
        'are handled by Gondaliya CPA Professional Corporation at '
        'gondaliyacpa.ca at $350.00 plus HST per year.'),
  close=''),
 band=('What the Fee Covers, in Full',
       'The cost page sets out the fee and everything inside it, and what '
       'falls outside a nil return.'),
 cards=[('Reviewed by a CPA',
         'Each return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('Published prices only',
         'The figures in the table are each side&rsquo;s published prices on '
         'the date above. Neither is a quotation.'),
        ('What sits outside the fee',
         'The Ontario annual return, the federal annual return, '
         'extra-provincial registrations, and closing a GST/HST or payroll '
         'account with Form RC145.')],
 case=('A dormant corporation with one shareholder and three unfiled years',
       'Here that is three returns at ' + PRICE + ', prepared oldest first, '
       'each reviewed by a CPA Ontario member and transmitted electronically, '
       'with Form T183CORP signed once for each year and a CRA confirmation '
       'for each within 3 business days. What three years would come to on '
       'the other column is not something the published price we hold states, '
       'so this page does not say. The figures here illustrate the published '
       'price above and are not drawn from a client file.'),
 faq=[
  ('What is the difference in price?',
   'Nil T2 filing here is ' + PRICE + '. The BluePeak figure recorded on '
   'September 20, 2026 is $100.00. Both are above, as published on their '
   'dates.'),
  ('When was the BluePeak price checked?',
   'September 20, 2026, recorded by Sharad Gondaliya, CPA. Prices change, so '
   'the date sits above the table and its own site is the place to confirm '
   'the current figure.'),
  ('Why does the table say the published price does not state things?',
   'Because the figure recorded is a price rather than a description. Saying '
   'the published price does not state something is accurate; saying the '
   'answer is no would not be.'),
  ('Does the $100.00 cover the same work?',
   'The published price we hold does not say what it covers, so this page '
   'does not claim either way. What the fee here covers is set out in full '
   'above.'),
  ('What does your fee include?',
   'The T2, GIFI Schedules 100, 125 and 141 where required, Schedule 50, '
   'Schedule 24 on a first return, Schedule 8 and loss continuity, a CPA '
   'Ontario review, and electronic transmission, at ' + PRICE + '.'),
  ('Is there a cheaper tier here?',
   'No. There is one price for a nil year, and no tier above or below it.'),
  ('Who actually files the return here?',
   'Gondaliya CPA Professional Corporation, a registered EFILE electronic '
   'filer. Returns are prepared and transmitted in Canada.'),
  ('What if my year is not nil after all?',
   'Then this fee does not cover it. It moves to Gondaliya CPA Professional '
   'Corporation at gondaliyacpa.ca at $350.00 plus HST per year.'),
  ('Do you file my annual return as well?',
   'Not as part of this fee. A registry annual return is a separate filing, '
   'which the <a href="' + T + 'annual-return-vs-tax-return-checker/">annual '
   'return versus tax return checker</a> sets out.'),
  ('Where can I see the whole fee?',
   'On the <a href="' + COST + '">nil T2 filing cost page</a>, which states '
   'the fee and everything inside it.'),
 ],
)

PAGES = [CLOUDTAX, BLUEPEAK]

# ---- guards -------------------------------------------------------------
_PLAN = io.open(os.path.join(HERE, '..', '..', 'docs',
                             'corpnilfilingfor300-seo-website-plan.md'),
                encoding='utf-8').read() if False else None
import io as _io
_PLAN = _io.open(os.path.join(HERE, '..', '..', 'docs',
                              'corpnilfilingfor300-seo-website-plan.md'),
                 encoding='utf-8').read()
for _p in PAGES:
    # gate.py bans the substring "reviews" as a rule 6 review-claim guard,
    # and it is easy to reintroduce in prose about who prepares a return.
    # Caught at build time rather than at the gate.
    _txt = ' '.join([_p['answer'], _p['table_note'], _p.get('stamp', ''),
                     _p.get('disclosure', ''),
                     ' '.join(h for _h in _p['lead'] for h in _h[1]),
                     ' '.join(_p['detail']['items']),
                     _p['detail']['warn'], _p['case'][1],
                     ' '.join(q + a for q, a in _p['faq']),
                     ' '.join(str(c) for r in _p['price_rows']
                              + _p['feature_rows'] for c in r)]).lower()
    assert 'reviews' not in _txt, (
        '%s: the substring "reviews" is banned by gate.py rule 6; use '
        '"reviewed by" or "prepares"' % _p['slug'])
    # A cell built by concatenating one of the not-stated constants onto
    # other prose produced "costs. Not stated on the page captured. for what
    # the filing itself includes" on the first build. A constant that ends in
    # a full stop may only ever be a whole cell.
    for _r in _p['price_rows'] + _p['feature_rows']:
        for _c in _r[1:-1]:
            for _const in (NS, NS_PAGE):
                assert _c == _const or _const not in _c, (
                    '%s: %r is spliced into a longer cell: %r'
                    % (_p['slug'], _const, _c[:90]))
    # every brand slug is an Appendix A URL
    assert '\n/%s/\n' % _p['slug'] in _PLAN, (
        '%s is not an Appendix A URL' % _p['slug'])
    # the competitor's price appears in the right-hand price cell
    assert _p['price_rows'][0][2], _p['slug']
    # our own fee is stated, hard rule 9 as deviated
    assert _p['price_rows'][0][1] == PRICE, _p['slug']
    # the capture date is never the build date
    assert _p['price_checked'] != build_f7.TODAY, _p['slug']

# BluePeak's figure is the plan's, so the plan must actually say so.
assert 'BluePeak $100.00' in _PLAN, 'plan line 1568 no longer states BluePeak'
assert 'Prices checked September 20, 2026' in _PLAN, 'the capture date moved'

if __name__ == '__main__':
    import filecmp
    import shutil
    import subprocess
    import tempfile

    _mine = {p['slug'] + '.html' for p in PAGES}
    _others = sorted(f for f in os.listdir(HERE)
                     if f.endswith('.html') and f not in _mine)
    # Re-entrancy: two builders in this family verify the others by
    # rebuilding them, so each must not sweep when it is itself the child of
    # such a sweep. Without this they call each other without end, which is
    # what happened on 2026-11-09.
    _verify = not os.environ.get('F7_NO_VERIFY')
    tmp = tempfile.mkdtemp()
    if _verify:
        for _f in _others:
            shutil.copy(os.path.join(HERE, _f), os.path.join(tmp, _f))
        _env = dict(os.environ, F7_NO_VERIFY='1')
        for _b in sorted(f for f in os.listdir(HERE)
                         if f.startswith('build_f7') and f.endswith('.py')
                         and f != 'build_f7o.py'):
            subprocess.run(['python3', os.path.join(HERE, _b)], cwd=HERE,
                           capture_output=True, env=_env)
    _moved = [f for f in _others
              if _verify
              and not filecmp.cmp(os.path.join(HERE, f),
                                  os.path.join(tmp, f), shallow=False)]
    shutil.rmtree(tmp)
    assert not _moved, 'these pages must not move: %s' % _moved
    if _verify:
        print('the %d earlier comparison pages are byte-identical'
              % len(_others))

    for i, _p in enumerate(PAGES, 1):
        check(_p)
        # gate.py globs f7*-manifest.json, and write() replaces the file
        # rather than appending, so one file per page.
        write(_p, 'f7o%d-manifest.json' % i)
