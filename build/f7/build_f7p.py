#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, the last four brand pages. Pages 17 to 20:

  /compare/corpnilfilingfor300-vs-turbotax/
  /compare/corpnilfilingfor300-vs-t2inc/
  /compare/corpnilfilingfor300-vs-taxdeep/
  /compare/corpnilfilingfor300-vs-hr-block/

These complete Appendix A's Family 7 roster except for
/compare/voluntary-disclosure-vs-plain-late-filing/, which is not buildable:
the Voluntary Disclosures Programme appears nowhere in the plan and nowhere
on the site, so neither column has a published position to state. That one is
Sharad Gondaliya's ruling, not a writing job.

The slugs are Appendix A's
-------------------------
Appendix A gives `corpnilfilingfor300-vs-turbotax`. Line 1145's illustrative
sample says `corpnilfilingfor300-vs-turbotax-business`, and line 1242's
keyword list says "corpnilfilingfor300 vs turbotax business". Appendix A is
the roster and the sample is an illustration, so the slug follows Appendix A
and the keyword follows line 1242. The same split applies to
`corpnilfilingfor300-vs-hr-block`, whose keyword is "corpnilfilingfor300 vs
h and r block".

The source is plan line 1568 and nothing else
---------------------------------------------
Navneet's instruction on 2026-11-09 was to use the prices the plan already
holds: TurboTax $175.00, T2inc $199.00 and $299.00, TaxDeep $200.00, H&R
Block $449.00, "Prices checked September 20, 2026". A capture attempt on
2026-11-06 found nothing publishable for any of these four, so all four are
the BluePeak pattern: one published figure, a September 20 stamp, and eight
cells saying the published price does not state it.

Line 1568 sets a monthly re-check and that figure is now fifty days old. The
date sits above every table and the table note on each page says how old it
is, which is the honest handling of a stale source. Re-dating it is Navneet's
monthly task, not something a build can do.

Three of the four published figures are below our fee
-----------------------------------------------------
$175.00, $199.00 and $200.00 are each below $300.00 plus HST per tax year,
and $449.00 is above it. None of that is argued on any of these pages. Hard
rule 4 bars a cheapest claim and line 1215 bars a negative one, and the
direction of the gap does not change what a page may say: both prices, the
date, and what our own fee covers. check_competitor() refuses a comparative
word in the answer, the table or the note, in either direction.

What makes each page different from the others
----------------------------------------------
Four pages built from one price each would be four copies, and the gate's
cross-page duplicate check is not the reason to avoid that. Each has a real
subject of its own:

  TurboTax  -- a corporation weighing software it drives itself against a
               return prepared for it is asking a question this site already
               answers at /compare/diy-vs-cpa-nil-t2/. That page is about the
               two routes generically and attributes nothing to TurboTax,
               which the published price we hold could not support.
  T2inc     -- two published figures, $199.00 and $299.00. Both are stated and
               neither is picked, because the price we hold does not say what
               separates them. Same handling as CloudTax's two nil figures.
  TaxDeep   -- one figure and nothing else, so this page is the clearest case
               of the whole pattern and says so: what a published price can
               and cannot tell a reader.
  H&R Block -- the one figure in the set published above our fee. The page
               states it and does not reason from it, which is the discipline
               line 1215 exists to impose.
"""
import os

import build_f7
from build_f7 import check, write, PRICE, COST, T, G, FORM

HERE = os.path.dirname(os.path.abspath(__file__))

build_f7.TODAY, build_f7.ISO = 'November 9, 2026', '2026-11-09'

US = 'corpnilfilingfor300.ca'
NS = 'Not stated in the published price we hold.'
SEP20, SEP20_ISO = 'September 20, 2026', '2026-09-20'

# Our side, written once and identical to build_f7o's. Every cell is on the
# live site today.
OURS = {
 'covers': 'The T2 itself, GIFI Schedules 100, 125 and 141 where required, '
           'Schedule 50, Schedule 24 on a first return, Schedule 8 and loss '
           'continuity, and electronic transmission',
 # "reviews" as a literal substring is banned by gate.py as a rule 6
 # review-claim guard, so this says "reviewed by" instead.
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


def stamp(name):
    return ('Our figure is our own <a href="' + COST + '">published fee</a>. '
            'The ' + name + ' figure is its published price on that date, '
            'recorded by Sharad Gondaliya, CPA, and is not a quotation.')


# The detail block is the same on all four, because on all four it is our own
# fee that carries the detail and our fee does not change between pages. Its
# intro sentence differs per page so the section opens on that page's subject.
def detail(intro):
    return dict(
     h2='What the Fee Here Covers',
     intro=intro,
     items=[
      'The T2 itself, and GIFI Schedules 100, 125 and 141 where the '
      'corporation has anything to report.',
      'Schedule 50 for any shareholder at 10% or more, Schedule 24 on a '
      'first return, and Schedule 8 with loss continuity carried forward '
      'intact.',
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
           'holding corporation with investment income, a rental corporation '
           'and a corporation that paid or received a dividend are not nil. '
           'Those are handled by Gondaliya CPA Professional Corporation at '
           'gondaliyacpa.ca at $350.00 plus HST per year.'),
     close='')


BAND = ('What the Fee Covers, in Full',
        'The cost page sets out the fee and everything inside it, and what '
        'falls outside a nil return.')


# ======================================================================
# Page 17: TurboTax. Plan line 1568, $175.00.
# ======================================================================
TURBOTAX = dict(
 competitor='TurboTax',
 competitor_price='$175.00',
 price_checked=SEP20, price_checked_iso=SEP20_ISO,
 col_a=US, col_b='TurboTax',
 price_rows=[
  ('Published price for a nil T2 return', PRICE, '$175.00', True),
  ('What else the published price list holds',
   'One price. There is no tier above or below it for a nil year',
   NS, True),
 ],
 feature_rows=rows(NS, NS, NS, NS, NS, NS, NS, NS),
 faq_n=10,
 stamp=stamp('TurboTax'),
 disclosure=disclosure('TurboTax', SEP20),
 table_note=('The right-hand column holds the figure published on the date '
             'above and no more. A cell saying the published price does not '
             'state something means exactly that, not that the answer is no. '
             'The figure is fifty days old at the time of writing and its own '
             'site is the place to confirm it.'),
 slug='corpnilfilingfor300-vs-turbotax',
 title=US + ' vs TurboTax | Published Prices',
 h1=US + ' vs TurboTax',
 h1_pre=US + ' vs ', h1_span='TurboTax',
 eyebrow='Comparison &#183; Published Prices &#183; Canada',
 keyword='corpnilfilingfor300 vs turbotax business',
 meta=('Published prices side by side. Nil T2 filing here is ' + PRICE + '. '
       'TurboTax published $175.00 on September 20, 2026.'),
 seo_title=US + ' and TurboTax Compared',
 seo_desc=('Side-by-side published prices. Nil T2 filing here is $300.00 plus '
           'HST per tax year; the TurboTax figure is its published price on '
           'September 20, 2026.'),
 answer=('Nil T2 filing here is ' + PRICE + ', one price for one tax year, '
         'covering the return, its schedules where required, a CPA Ontario '
         'review and electronic transmission by a registered EFILE electronic '
         'filer. TurboTax published $175.00, recorded on September 20, 2026. '
         'That figure is its published price on that date rather than a '
         'quotation. The published price we hold does not state what it '
         'includes or who prepares the return, so this page does not state '
         'those either, and the two routes a corporation is really choosing '
         'between are set out on their own page.'),
 cta2=('What the Fee Covers', COST),
 lead=[('Two Published Prices, and the Question Underneath Them',
        ['<p>Two figures sit in the table above, each as published on the '
         'date shown. This page makes no claim about which is better value, '
         'because that turns on what a particular corporation needs and '
         'because a comparison page is not the place to argue it.</p>',
         '<p>There is usually a question underneath a comparison like this '
         'one, and it is not really about either price. It is whether to '
         'drive the filing yourself or have it prepared and transmitted for '
         'you. That question has its own page: '
         '<a href="https://corpnilfilingfor300.ca/compare/diy-vs-cpa-nil-t2/">'
         'filing a nil T2 yourself against having a CPA file it</a> sets out '
         'both routes, what each one asks of you, and where each one tends to '
         'go wrong.</p>',
         '<p>That page is about the two routes and attributes nothing to any '
         'provider, which is the only honest way to write it: the published '
         'price recorded here is a figure, not a description of how the work '
         'is done.</p>']),
       ],
 detail=detail('Since the right-hand column is a figure on its own, the '
               'useful detail on this page is what the fee here buys:'),
 band=BAND,
 cards=[('Reviewed by a CPA',
         'Each return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('Published prices only',
         'Both figures in the table are published prices on the date above. '
         'Neither is a quotation.'),
        ('The route, not the brand',
         'Whether to file it yourself or have it filed is the real question, '
         'and it has its own page on this site.')],
 case=('A single-shareholder corporation with one quiet year to file',
       'Here that is one return at ' + PRICE + ', prepared and reviewed by a '
       'CPA Ontario member, with Form T183CORP signed on a secure screen and '
       'the CRA confirmation emailed within 3 business days. What the same '
       'year would involve on the other column is not something the published '
       'price we hold states, so this page does not say. The figures here '
       'illustrate the published price above and are not drawn from a client '
       'file.'),
 faq=[
  ('What is the difference in price?',
   'Nil T2 filing here is ' + PRICE + '. The TurboTax figure recorded on '
   'September 20, 2026 is $175.00. Both are above, as published on their '
   'dates.'),
  ('When was the TurboTax price checked?',
   'September 20, 2026, recorded by Sharad Gondaliya, CPA. Prices change, so '
   'the date sits above the table and its own site is the place to confirm '
   'the current figure.'),
  ('Does the $175.00 cover the same work?',
   'The published price we hold does not say what it covers, so this page '
   'does not claim either way. What the fee here covers is set out in full '
   'above.'),
  ('Should I file it myself or have it filed?',
   'That is the question underneath this one, and it has its own page: '
   '<a href="https://corpnilfilingfor300.ca/compare/diy-vs-cpa-nil-t2/">'
   'filing a nil T2 yourself against having a CPA file it</a>.'),
  ('Can I file a nil T2 myself?',
   'Yes, and the return is still due within six months of the fiscal '
   'year-end either way. What the route changes is who carries the '
   'schedules, the signature and the transmission, which is what the '
   '<a href="https://corpnilfilingfor300.ca/compare/diy-vs-cpa-nil-t2/">'
   'route comparison</a> sets out.'),
  ('What is actually involved in a nil T2?',
   'More than a zero: GIFI Schedules 100, 125 and 141 where the corporation '
   'has anything to report, Schedule 50 for a shareholder at 10% or more, '
   'Schedule 24 on a first return, and Schedule 8 with loss continuity. The '
   '<a href="' + T + 'required-schedules-checker/">required schedules '
   'checker</a> names the ones a given year carries.'),
  ('Does transmitting it myself need anything special?',
   'Electronic filing is mandatory for most corporations, which the '
   '<a href="' + T + 'mandatory-t2-efile-checker/">mandatory T2 e-filing '
   'checker</a> settles. Here it is transmitted by a registered EFILE '
   'electronic filer and Form T183CORP is signed on a secure screen.'),
  ('Is there a cheaper tier here?',
   'No. There is one price for a nil year, and no tier above or below it.'),
  ('What if my year is not nil after all?',
   'Then this fee does not cover it. It moves to Gondaliya CPA Professional '
   'Corporation at gondaliyacpa.ca at $350.00 plus HST per year.'),
  ('Where can I see the whole fee?',
   'On the <a href="' + COST + '">nil T2 filing cost page</a>, which states '
   'the fee and everything inside it.'),
 ],
)


# ======================================================================
# Page 18: T2inc. Plan line 1568, two figures: $199.00 and $299.00.
# ======================================================================
T2INC = dict(
 competitor='T2inc',
 competitor_price='$199.00 and $299.00',
 price_checked=SEP20, price_checked_iso=SEP20_ISO,
 col_a=US, col_b='T2inc',
 price_rows=[
  ('Published price for a nil T2 return', PRICE,
   'Two figures were published on the date recorded, $199.00 and $299.00. '
   'The published price we hold does not state which applies to a nil year',
   True),
  ('What else the published price list holds',
   'One price. There is no tier above or below it for a nil year',
   'Both figures above, with nothing recorded about what separates them',
   True),
 ],
 feature_rows=rows(NS, NS, NS, NS, NS, NS, NS, NS),
 faq_n=10,
 stamp=('Our figure is our own <a href="' + COST + '">published fee</a>. '
        'The two T2inc figures are its published prices on that date, '
        'recorded by Sharad Gondaliya, CPA, and are not a quotation.'),
 disclosure=disclosure('T2inc', SEP20),
 table_note=('Two figures were recorded on the date above, and both are '
             'stated rather than one being chosen on the provider&rsquo;s '
             'behalf. What separates them is not something the published '
             'price we hold records, so this page does not guess: picking the '
             'lower would understate it and picking the higher would overstate '
             'it. The figures are fifty days old at the time of writing and '
             'its own site is the place to confirm them.'),
 slug='corpnilfilingfor300-vs-t2inc',
 title=US + ' vs T2inc | Published Prices',
 h1=US + ' vs T2inc',
 h1_pre=US + ' vs ', h1_span='T2inc',
 eyebrow='Comparison &#183; Published Prices &#183; Canada',
 keyword='corpnilfilingfor300 vs t2inc',
 meta=('Published prices side by side. Nil T2 filing here is ' + PRICE + '. '
       'T2inc published $199.00 and $299.00 on September 20, 2026.'),
 seo_title=US + ' and T2inc Compared',
 seo_desc=('Side-by-side published prices. Nil T2 filing here is $300.00 plus '
           'HST per tax year; T2inc published two figures on September 20, '
           '2026 and both are stated.'),
 answer=('Nil T2 filing here is ' + PRICE + ', one price for one tax year, '
         'covering the return, its schedules where required, a CPA Ontario '
         'review and electronic transmission by a registered EFILE electronic '
         'filer. Two T2inc figures were recorded on September 20, 2026, '
         '$199.00 and $299.00. Both are stated here because the published '
         'price we hold does not record what separates them, and both are '
         'published prices on that date rather than quotations.'),
 cta2=('What the Fee Covers', COST),
 lead=[('Why Two Figures Appear in One Column',
        ['<p>The right-hand column of the table carries two prices rather '
         'than one. That is what was published on the date recorded, and the '
         'honest rendering is to state both.</p>',
         '<p>The alternative would be to pick one. Picking the lower figure '
         'would understate what a corporation might pay and picking the '
         'higher would overstate it, and neither is supported by what we '
         'hold: the record is two numbers without a note of what distinguishes '
         'them. So both sit in the table and the question of which applies to '
         'a nil year is left to the provider&rsquo;s own site, which is where '
         'it can actually be answered.</p>',
         '<p>Our column has the opposite shape. There is one figure for a nil '
         'year, and the section below sets out in full what it covers, which '
         'is the detail a published price alone cannot carry.</p>']),
       ],
 detail=detail('One column holds two figures and no description, so the '
               'useful detail on this page is what the single fee here '
               'buys:'),
 band=BAND,
 cards=[('Reviewed by a CPA',
         'Each return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('Both figures stated',
         'Two prices were published on the date above and both appear in the '
         'table. Neither was picked on the provider&rsquo;s behalf.'),
        ('One price here',
         'A nil year is one figure with no tier above or below it, and the '
         'cost page sets out everything inside it.')],
 case=('A numbered company with two quiet years and no bookkeeping',
       'Here that is two returns at ' + PRICE + ', prepared oldest first, '
       'each reviewed by a CPA Ontario member, with Form T183CORP signed once '
       'for each year and a CRA confirmation for each within 3 business days. '
       'Which of the two figures in the other column two such years would '
       'fall under is not something the published prices we hold record, so '
       'this page does not say. The figures here illustrate the published '
       'price above and are not drawn from a client file.'),
 faq=[
  ('Why are there two T2inc prices on this page?',
   'Because two were published on the date recorded, $199.00 and $299.00, '
   'and the record does not say what separates them. Both are stated rather '
   'than one being chosen.'),
  ('Which of the two applies to a nil return?',
   'The published prices we hold do not say, so this page does not claim '
   'either way. Its own site is the place to settle it.'),
  ('When were those figures checked?',
   'September 20, 2026, recorded by Sharad Gondaliya, CPA. Prices change, so '
   'the date sits above the table.'),
  ('What is the price here?',
   PRICE + ' for a nil year, one figure for one tax year for one '
   'corporation.'),
  ('What does your fee include?',
   'The T2, GIFI Schedules 100, 125 and 141 where required, Schedule 50, '
   'Schedule 24 on a first return, Schedule 8 and loss continuity, a CPA '
   'Ontario review, and electronic transmission.'),
  ('Do either of those figures cover the same work?',
   'The published prices we hold do not say what they cover, so this page '
   'does not claim either way. What the fee here covers is set out in full '
   'above.'),
  ('Is there a cheaper tier here?',
   'No. There is one price for a nil year, and no tier above or below it.'),
  ('Who actually files the return here?',
   'Gondaliya CPA Professional Corporation, a registered EFILE electronic '
   'filer. Returns are prepared and transmitted in Canada.'),
  ('What if my year is not nil after all?',
   'Then this fee does not cover it. It moves to Gondaliya CPA Professional '
   'Corporation at gondaliyacpa.ca at $350.00 plus HST per year.'),
  ('Where can I see the whole fee?',
   'On the <a href="' + COST + '">nil T2 filing cost page</a>, which states '
   'the fee and everything inside it.'),
 ],
)


# ======================================================================
# Page 19: TaxDeep. Plan line 1568, $200.00.
# ======================================================================
TAXDEEP = dict(
 competitor='TaxDeep',
 competitor_price='$200.00',
 price_checked=SEP20, price_checked_iso=SEP20_ISO,
 col_a=US, col_b='TaxDeep',
 price_rows=[
  ('Published price for a nil T2 return', PRICE, '$200.00', True),
  ('What else the published price list holds',
   'One price. There is no tier above or below it for a nil year',
   NS, True),
 ],
 feature_rows=rows(NS, NS, NS, NS, NS, NS, NS, NS),
 faq_n=10,
 stamp=stamp('TaxDeep'),
 disclosure=disclosure('TaxDeep', SEP20),
 table_note=('Eight cells in the right-hand column say the published price '
             'does not state something. That is a statement about the record '
             'we hold, which is a figure, and not a statement about the '
             'provider: not stated and no are different claims, and only one '
             'of them is sourced here. The figure is fifty days old at the '
             'time of writing and its own site is the place to confirm it.'),
 slug='corpnilfilingfor300-vs-taxdeep',
 title=US + ' vs TaxDeep | Published Prices',
 h1=US + ' vs TaxDeep',
 h1_pre=US + ' vs ', h1_span='TaxDeep',
 eyebrow='Comparison &#183; Published Prices &#183; Canada',
 keyword='corpnilfilingfor300 vs taxdeep',
 meta=('Published prices side by side. Nil T2 filing here is ' + PRICE + '. '
       'TaxDeep published $200.00 on September 20, 2026.'),
 seo_title=US + ' and TaxDeep Compared',
 seo_desc=('Side-by-side published prices. Nil T2 filing here is $300.00 plus '
           'HST per tax year; the TaxDeep figure is its published price on '
           'September 20, 2026.'),
 answer=('Nil T2 filing here is ' + PRICE + ', one price for one tax year, '
         'covering the return, its schedules where required, a CPA Ontario '
         'review and electronic transmission by a registered EFILE electronic '
         'filer. TaxDeep published $200.00, recorded on September 20, 2026, '
         'which is its published price on that date rather than a quotation. '
         'What that figure includes is not part of the record we hold, so the '
         'comparison this page can honestly make is between one price with '
         'its contents stated and one price without.'),
 cta2=('What the Fee Covers', COST),
 lead=[('A Price on Its Own Answers One Question',
        ['<p>A published price tells a reader what a provider charges. It '
         'does not tell them what arrives for the money, who does the work, '
         'or what happens when a year turns out not to be nil, and those are '
         'usually the questions that decide the choice.</p>',
         '<p>This page is the plainest case of that on the site. One figure '
         'was recorded on the date above and nothing else was, so eight cells '
         'of the right-hand column say the published price does not state it. '
         'Each of those cells is deliberate wording: it says what the record '
         'holds, not what the provider does.</p>',
         '<p>So the honest use of this page is to read the left-hand column '
         'closely. Every line of it is on this site and can be checked, and '
         'the section below sets the whole of it out.</p>']),
       ],
 detail=detail('Since the comparison is one described price against one '
               'undescribed figure, here is the description in full:'),
 band=BAND,
 cards=[('Reviewed by a CPA',
         'Each return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('Not stated, not no',
         'Where a cell says the published price does not state something, it '
         'means the record is silent, not that the answer is no.'),
        ('Everything inside the fee',
         'The cost page lists what the fee covers and what falls outside a '
         'nil return.')],
 case=('A corporation struck off the register with four unfiled years behind '
       'it',
       'Here that is four returns at ' + PRICE + ', prepared oldest first, '
       'each reviewed by a CPA Ontario member and transmitted electronically, '
       'with a CRA confirmation for each within 3 business days. The revival '
       'itself is a registry matter and sits outside this fee. What four '
       'years would come to on the other column is not something the '
       'published price we hold states. The figures here illustrate the '
       'published price above and are not drawn from a client file.'),
 faq=[
  ('What is the difference in price?',
   'Nil T2 filing here is ' + PRICE + '. The TaxDeep figure recorded on '
   'September 20, 2026 is $200.00. Both are above, as published on their '
   'dates.'),
  ('When was the TaxDeep price checked?',
   'September 20, 2026, recorded by Sharad Gondaliya, CPA. Prices change, so '
   'the date sits above the table and its own site is the place to confirm '
   'the current figure.'),
  ('Why does nearly every cell say the published price does not state it?',
   'Because the record we hold is a figure rather than a description. Saying '
   'the published price does not state something is accurate; saying the '
   'answer is no would not be.'),
  ('Does the $200.00 cover the same work?',
   'The published price we hold does not say what it covers, so this page '
   'does not claim either way. What the fee here covers is set out in full '
   'above.'),
  ('What should I ask a provider whose price is all I can see?',
   'What the price covers, who prepares and signs the return, how it is '
   'transmitted, and what happens if the year turns out not to be nil. '
   'Those four are the whole of the table above, and every one of them is '
   'answered in the left-hand column.'),
  ('Is there a cheaper tier here?',
   'No. There is one price for a nil year, and no tier above or below it.'),
  ('Who actually files the return here?',
   'Gondaliya CPA Professional Corporation, a registered EFILE electronic '
   'filer. Returns are prepared and transmitted in Canada.'),
  ('How do I know which years I even owe?',
   'The <a href="' + T + 'outstanding-returns-count-checker/">outstanding '
   'returns count checker</a> counts them from the last return filed, and '
   'each one is its own return at ' + PRICE + '.'),
  ('Does the fee cover reviving a struck corporation?',
   'No. A revival is a registry filing and sits outside the fee, which is '
   'for the return. The <a href="' + T + 'corporate-revival-requirement-checker/">'
   'corporate revival requirement checker</a> sets out what it involves.'),
  ('Where can I see the whole fee?',
   'On the <a href="' + COST + '">nil T2 filing cost page</a>, which states '
   'the fee and everything inside it.'),
 ],
)


# ======================================================================
# Page 20: H&R Block. Plan line 1568, $449.00. The one figure in the set
# published above our own fee, which changes nothing about what may be said.
# ======================================================================
HRBLOCK = dict(
 competitor='H&R Block',
 competitor_price='$449.00',
 price_checked=SEP20, price_checked_iso=SEP20_ISO,
 col_a=US, col_b='H&amp;R Block',
 price_rows=[
  ('Published price for a nil T2 return', PRICE, '$449.00', True),
  ('What else the published price list holds',
   'One price. There is no tier above or below it for a nil year',
   NS, True),
 ],
 feature_rows=rows(NS, NS, NS, NS, NS, NS, NS, NS),
 faq_n=10,
 stamp=stamp('H&amp;R Block'),
 disclosure=disclosure('H&amp;R Block', SEP20),
 table_note=('The right-hand column holds the figure published on the date '
             'above and no more. Where a cell says the published price does '
             'not state something, the record is silent rather than the '
             'answer being no, and a figure on its own says nothing about '
             'what it buys in either direction. The figure is fifty days old '
             'at the time of writing and its own site is the place to confirm '
             'it.'),
 slug='corpnilfilingfor300-vs-hr-block',
 title=US + ' vs H&amp;R Block | Published Prices',
 h1=US + ' vs H&amp;R Block',
 h1_pre=US + ' vs ', h1_span='H&amp;R Block',
 eyebrow='Comparison &#183; Published Prices &#183; Canada',
 keyword='corpnilfilingfor300 vs h and r block',
 meta=('Published prices side by side. Nil T2 filing here is ' + PRICE + '. '
       'H&amp;R Block published $449.00 on September 20, 2026.'),
 seo_title=US + ' and H&amp;R Block Compared',
 seo_desc=('Side-by-side published prices. Nil T2 filing here is $300.00 plus '
           'HST per tax year; the H&amp;R Block figure is its published price '
           'on September 20, 2026.'),
 answer=('Nil T2 filing here is ' + PRICE + ', one price for one tax year, '
         'covering the return, its schedules where required, a CPA Ontario '
         'review and electronic transmission by a registered EFILE electronic '
         'filer. H&amp;R Block published $449.00, recorded on September 20, '
         '2026, which is its published price on that date rather than a '
         'quotation. The published price we hold does not state what it '
         'includes, so this page states both figures and what the fee here '
         'covers, and reasons from neither.'),
 cta2=('What the Fee Covers', COST),
 lead=[('Both Figures, and No Argument From Either',
        ['<p>The two prices in the table above sit either side of each other, '
         'and this page draws no conclusion from which is which. That is not '
         'reticence: a published price is a figure, and a figure cannot '
         'support a claim about what the money buys.</p>',
         '<p>A higher published price can reflect work a lower one does not '
         'include, and a lower one can reflect a narrower job. Neither '
         'direction can be read off the number, and the record we hold for '
         'the right-hand column is a number with nothing attached. So the '
         'table states both and stops there.</p>',
         '<p>What the left-hand column can do is account for itself line by '
         'line, because every one of those lines is published on this site. '
         'The section below does exactly that.</p>']),
       ],
 detail=detail('A figure cannot say what it buys, so here is what the fee on '
               'this site buys, in full:'),
 band=BAND,
 cards=[('Reviewed by a CPA',
         'Each return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('No argument from a number',
         'A published price cannot say what the money buys, in either '
         'direction, so this page states both figures and reasons from '
         'neither.'),
        ('What sits outside the fee',
         'The Ontario annual return, the federal annual return, '
         'extra-provincial registrations, and closing a GST/HST or payroll '
         'account with Form RC145.')],
 case=('A holding company that has been quiet for three years',
       'If those years really were nil, that is three returns at ' + PRICE
       + ', each reviewed by a CPA Ontario member and transmitted '
       'electronically. If investment income was credited in any of them, '
       'that year is not nil and is not covered by this fee: it moves to '
       'Gondaliya CPA Professional Corporation at gondaliyacpa.ca at $350.00 '
       'plus HST per year. What any of that would come to on the other column '
       'is not something the published price we hold states. The figures here '
       'illustrate the published price above and are not drawn from a client '
       'file.'),
 faq=[
  ('What is the difference in price?',
   'Nil T2 filing here is ' + PRICE + '. The H&amp;R Block figure recorded '
   'on September 20, 2026 is $449.00. Both are above, as published on their '
   'dates.'),
  ('When was the H&amp;R Block price checked?',
   'September 20, 2026, recorded by Sharad Gondaliya, CPA. Prices change, so '
   'the date sits above the table and its own site is the place to confirm '
   'the current figure.'),
  ('Does the higher figure mean more is included?',
   'The published price we hold does not say what it includes, so this page '
   'does not claim either way. A figure on its own cannot answer that in '
   'either direction.'),
  ('Why does the table not draw a conclusion?',
   'Because the record for one column is a price with no description '
   'attached, and a comparison built on that would not be provable.'),
  ('What does your fee include?',
   'The T2, GIFI Schedules 100, 125 and 141 where required, Schedule 50, '
   'Schedule 24 on a first return, Schedule 8 and loss continuity, a CPA '
   'Ontario review, and electronic transmission, at ' + PRICE + '.'),
  ('Is there a cheaper tier here?',
   'No. There is one price for a nil year, and no tier above or below it.'),
  ('Who actually files the return here?',
   'Gondaliya CPA Professional Corporation, a registered EFILE electronic '
   'filer. Returns are prepared and transmitted in Canada.'),
  ('My corporation is a holding company. Is that nil?',
   'Not if investment income was credited in the year. A holding corporation '
   'with investment income is not nil, and nor is a rental corporation or '
   'one that paid or received a dividend.'),
  ('What if my year is not nil after all?',
   'Then this fee does not cover it. It moves to Gondaliya CPA Professional '
   'Corporation at gondaliyacpa.ca at $350.00 plus HST per year.'),
  ('Where can I see the whole fee?',
   'On the <a href="' + COST + '">nil T2 filing cost page</a>, which states '
   'the fee and everything inside it.'),
 ],
)

PAGES = [TURBOTAX, T2INC, TAXDEEP, HRBLOCK]

# ----------------------------------------------------------------------
# The source is the plan, so the plan is asserted rather than trusted to
# memory. Line 1568 holds all four figures and the capture date.
# ----------------------------------------------------------------------
_PLAN = open(os.path.join(HERE, '..', '..', 'docs',
                          'corpnilfilingfor300-seo-website-plan.md'),
             encoding='utf-8').read()
for _frag in ('TurboTax $175.00', 'T2inc $199.00 and $299.00',
              'TaxDeep $200.00', 'H&R Block $449.00',
              'Prices checked September 20, 2026'):
    assert _frag in _PLAN, 'plan line 1568 no longer states %r' % _frag

# Appendix A's roster, not line 1145's illustrative sample. If a slug here is
# not in Appendix A, this batch is inventing URLs and should stop.
for _p in PAGES:
    assert '/' + _p['slug'] + '/' in _PLAN, (
        '%s is not an Appendix A URL' % _p['slug'])
    # Every stamp on this batch is the plan's September 20 capture, never the
    # build date. check_competitor enforces "not today"; this enforces the
    # actual date, because a wrong-but-not-today date would pass that.
    assert _p['price_checked'] == SEP20, _p['slug']
    assert _p['price_checked_iso'] == SEP20_ISO, _p['slug']
    # Hard rule 4 and line 1215 in the direction that is easy to miss: three
    # of these four figures are below our fee and one is above it, and no page
    # may reason from either direction.
    _body = (_p['answer'] + _p['table_note'] + _p['stamp']
             + ''.join(''.join(ps) for _h, ps in _p['lead'])
             + ''.join(q + aa for q, aa in _p['faq'])).lower()
    # "Is there a cheaper tier here?" is about OUR OWN price list and says
    # there is not. It is on the two brand pages already live, so it is
    # stripped before the scan rather than reworded here, which would leave
    # six pages answering the same question in two ways. gate.py strips
    # "authorized signing officer" before its rule 1 scan for the same
    # reason: the guard is for claims about the competitor.
    # Both carve-outs point at wording already live on pages 15 and 16, and
    # both are the opposite of the claim being guarded against: one says we
    # have no cheaper tier, the other says the page draws no value comparison
    # at all. Stripping them keeps the guard aimed at the assertion.
    for _ok in ('cheaper tier here', 'no claim about which is better value'):
        _body = _body.replace(_ok, '')
    for _w in ('cheaper', 'more expensive', 'better value', 'poor value',
               'worth more', 'worth less', 'costs less', 'costs more'):
        assert _w not in _body, '%s: %r' % (_p['slug'], _w)

if __name__ == '__main__':
    import filecmp
    import shutil
    import subprocess
    import tempfile

    _mine = {p['slug'] + '.html' for p in PAGES}
    _others = sorted(f for f in os.listdir(HERE)
                     if f.endswith('.html') and f not in _mine)
    # Re-entrancy, as in build_f7n and build_f7o: these builders verify each
    # other by rebuilding, so none may sweep when it is itself a child.
    _verify = not os.environ.get('F7_NO_VERIFY')
    tmp = tempfile.mkdtemp()
    if _verify:
        for _f in _others:
            shutil.copy(os.path.join(HERE, _f), os.path.join(tmp, _f))
        _env = dict(os.environ, F7_NO_VERIFY='1')
        for _b in sorted(f for f in os.listdir(HERE)
                         if f.startswith('build_f7') and f.endswith('.py')
                         and f != 'build_f7p.py'):
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
        write(_p, 'f7p%d-manifest.json' % i)
