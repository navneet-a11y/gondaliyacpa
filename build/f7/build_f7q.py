#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 21: /compare/nil-t2-filing-vs-t2-short-filing/

Navneet, 2026-11-18: "build compare page first using same template as other
compare pages. make it seo friendly detailed. follow plan".

WHY THIS URL
------------
6(d) line 1272 makes it a head term: "nil t2 filing vs t2 short", 60 monthly
searches, commercial intent, conversion path "Comparison to
/tools/t2-short-eligibility-checker/ to /". Line 1145 names it first among the
family's illustrative URLs, and line 1528 has the Family 6 listicles linking
to it. It was the only unbuilt F7 URL with a 6(d) head term behind it.

THE ANGLE, AND WHY IT IS NOT /compare/t2-short-vs-full-t2/
----------------------------------------------------------
This family already has /compare/t2-short-vs-full-t2/, and the blog carries
"T2 Short vs Full T2: Which Can a Nil Corporation Use?". Both set one FORM
against another FORM. Google currently shows the T2 Short cluster at positions
61 to 87, so a third page arguing the same axis would make that worse, not
better.

This page argues a different thing, and the query implies the mistake it
corrects: "nil T2 filing" and "T2 Short filing" are not two services to choose
between. One names the TAX YEAR, the other names the FORM. A quiet year is
usually filed on the short return, but it does not have to be, and the short
return is not reserved for quiet years. They answer different questions.

The eight conditions are deliberately NOT restated here. /compare/
t2-short-vs-full-t2/ lists all eight and answers the loss question, and
repeating them is what 6(k) exists to catch. This page links there instead and
keeps to the distinction.

Where the two axes do meet is stated once, because the live page already says
it: a dividend paid or received, and not being a Canadian-controlled private
corporation, each fail a short-return condition AND make the year not nil for
this service. That is agreement with what is published, not a new claim.

THE FEE WORDING
---------------
build_f7.PRICE still reads "$300.00 plus HST per tax year" and is NOT changed,
because it is the accurate record of what the twenty live F7 pages say. This
page is national, so under Navneet's 2026-11-12 ruling it may not name HST,
and it defines its own PRICE. gate.py was widened to accept either string; the
twenty siblings still need the sweep recorded in docs/decisions.md.
"""
import build_f7 as b
from build_f7 import T, COST, check, write

# Shadows build_f7.PRICE. See "THE FEE WORDING" above.
PRICE = '$300.00 plus applicable sales tax per tax year'

SHORT_VS_FULL = b.BASE + 't2-short-vs-full-t2/'
ELIG = T + 't2-short-eligibility-checker/'
EXCL = T + 't2-short-exclusion-checker/'
NIL_ELIG = T + 'nil-t2-eligibility-checker/'

# Both columns are our own published fee: the service files the year whichever
# form carries it, so line 1215's two price cells are both ours and filled.
PRICE_ROWS = [
 ('Our published fee for one tax year', PRICE, PRICE, False),
 ('A second tax year filed at the same time', PRICE, PRICE, False),
]

FEATURE_ROWS = [
 ('What the term describes',
  'The tax year: one in which nothing moved through the corporation',
  'The form: the two-page short return in place of the full T2', True),
 ('What decides whether it applies',
  'What the corporation did, or did not do, during the year',
  'Whether that year meets every one of the eight conditions', True),
 ('Can one tax year be both',
  'Yes. A quiet year is usually filed on the short return',
  'Yes. The short return usually carries a quiet year', False),
 ('Can a year be one without the other',
  'Yes. A quiet year that fails a condition goes on the full T2',
  'Yes. A year with a loss can meet every condition without being quiet',
  True),
 ('GIFI Schedules 100, 125 and 141',
  'Required where anything sits on the books',
  'Required where anything sits on the books', False),
 ('Form T183CORP',
  'Signed by an authorized signing officer before transmission',
  'Signed by an authorized signing officer before transmission', False),
 ('Filing route and confirmation',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days',
  'Transmitted electronically, CRA confirmation emailed within 3 business '
  'days', False),
 ('What this service does with it',
  'Files the quiet year, whichever of the two forms carries it',
  'Puts the year on the short return where every condition holds', True),
]

PAGE = dict(
 price=PRICE,          # overrides build_f7.PRICE in the closing CTA and schema
 col_a='Nil T2 Filing', col_b='T2 Short Filing',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 table_note=('Four rows differ and six do not, and the first two carry the '
             'whole point: one term names the year, the other names the form. '
             'The schedules, the signing, the filing route and the fee are the '
             'same whichever way the question is asked.'),
 cta2=('Check the Eight Conditions', ELIG),
 slug='nil-t2-filing-vs-t2-short-filing',
 title='Nil T2 Filing vs T2 Short Filing | Year or Form',
 h1='Nil T2 Filing vs T2 Short Filing',
 h1_pre='Nil T2 Filing vs ', h1_span='T2 Short Filing',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='nil t2 filing vs t2 short',
 meta=('Why these are not two services to choose between: one names the tax '
       'year, the other names the form, and most quiet years are filed on the '
       'short return.'),
 seo_title='Nil T2 Filing vs T2 Short Filing | Year or Form',
 seo_desc=('One names the tax year, the other names the form. Both are '
           + PRICE + ', and a quiet year usually goes on the short return.'),
 answer=('They are not alternatives. Nil T2 filing describes the tax year, '
         'one in which nothing moved through the corporation. T2 Short filing '
         'describes the form, the two-page short return used in place of the '
         'full T2 where the year meets every one of the eight conditions. '
         'A quiet year is usually filed on the short return, but a quiet year '
         'that fails a condition goes on the full T2 instead. Either way the '
         'filing is ' + PRICE + ', carries the same schedules, is signed on '
         'the same Form T183CORP and is transmitted the same way.'),
 lead=[('One Names the Year, the Other Names the Form',
        ['<p>Asking whether to choose nil T2 filing or T2 Short filing is '
         'like asking whether to choose a Tuesday or a short letter. The two '
         'words answer different questions. One is about what happened in '
         'the tax year. The other is about which sheet of paper the return '
         'goes on.</p>',
         '<p>Nil T2 filing is what this service does: it files the corporate '
         'income tax return for a year in which the corporation did nothing. '
         'The T2 Short is a form the Canada Revenue Agency publishes, a '
         'two-page version of the T2 that a corporation may use where the '
         'year meets every one of eight conditions. A quiet year usually '
         'meets them, which is why the two are so often confused, but '
         '"usually" is not "always" and the two tests are separate.</p>']),
       ('Why the Confusion Is Reasonable',
        ['<p>Most quiet years do qualify for the short return, so in practice '
         'the two travel together and it can look as though choosing one is '
         'choosing the other. It is not. The year is decided by what the '
         'corporation did. The form is decided by the eight conditions, '
         'tested against that same year.</p>',
         '<p>The two tests also overlap at two points, which is worth knowing '
         'before you assume a quiet year is automatically a short-return '
         'year. A dividend paid or received, and not being a '
         'Canadian-controlled private corporation throughout the year, each '
         'fail one of the eight conditions. They also mean the year is not a '
         'nil year for this service at all. Those two facts decide more than '
         'the form.</p>']),
       ],
 detail=dict(
  h2='Which Question You Are Actually Asking',
  intro=('Work out which of the two you need an answer to, because they are '
         'tested separately:'),
  items=[
   'Did anything move through the corporation in the tax year? That decides '
   'whether the year is a nil year, and whether this service files it.',
   'Does that year meet all eight conditions for the short return? That '
   'decides which form carries it, and nothing else.',
   'A quiet year that fails a condition is still a nil year. It goes on the '
   'full T2 at the same fee.',
   'A year with a loss can meet every condition without being quiet. The '
   'short return carries it, but it is not a nil year and this service does '
   'not price it.',
   'Neither question is answered by preference. Both are decided by what is '
   'true of the corporation for that year.',
   'Both are tested year by year. A corporation can qualify one year and not '
   'the next, even where nothing looks different at the year-end.',
  ],
  warn=('Choosing the short return because it is shorter is not a choice that '
        'exists. Where a condition fails, the full T2 is the return, and '
        'filing the short one anyway risks the transmission being rejected.'),
  close=('<a href="' + SHORT_VS_FULL + '">T2 Short vs Full T2</a> lists all '
         'eight conditions and takes the form question on its own. The '
         '<a href="' + ELIG + '">T2 Short eligibility checker</a> tests the '
         'eight at once, the <a href="' + EXCL + '">T2 Short exclusion '
         'checker</a> names the one that excludes you, and the '
         '<a href="' + NIL_ELIG + '">nil T2 eligibility checker</a> answers '
         'the other question, whether the year is nil at all.')),
 band=('The Same Work Either Way',
       'Whichever form carries the year, it is prepared, reviewed and '
       'transmitted the same way, at ' + PRICE + '.'),
 cards=[('Reviewed by a CPA',
         'The return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted, on the short form exactly as on the full one.'),
        ('The schedules are inside the fee',
         'GIFI Schedules 100, 125 and 141, Schedule 50, Schedule 24 on a '
         'first return, Schedule 8 and loss continuity, on whichever form '
         'applies.'),
        ('Transmitted and confirmed',
         'Transmitted electronically by a registered EFILE electronic filer, '
         'with your CRA confirmation emailed within 3 business days.')],
 case=('A numbered corporation that has been quiet for four years',
       'Say nothing moved through it in any of the four years and it has one '
       'address, one shareholder and no dividends. Each year is a nil year, '
       'so this service files all four, and each year is tested separately '
       'against the eight conditions. In a case like that they are usually '
       'met and all four go on the short return. If a dividend had been paid '
       'in one of those years, that year would fail a condition and would '
       'also stop being a nil year, so it would not be ours to file at all. '
       'Every year is ' + PRICE + ', counted per year. The figures here '
       'illustrate how the rules apply and are not drawn from a client file.'),
 faq=[
  ('Is T2 Short filing cheaper than nil T2 filing?',
   'No, and they are not two prices to compare. The fee is ' + PRICE + ' for '
   'the tax year, whichever of the two forms carries the return.'),
  ('Which one should I ask for?',
   'Neither is asked for. Tell us the years that were quiet and we file them. '
   'Which form each year goes on is worked out from the eight conditions.'),
  ('Is a nil return always filed on the T2 Short?',
   'No. It usually is, because a quiet year usually meets the conditions. A '
   'quiet year that fails one goes on the full T2 at the same fee.'),
  ('Is the T2 Short only for nil years?',
   'No. The condition is nil net income or a loss, so a year with a loss can '
   'use the short return without being a nil year.'),
  ('What are the eight conditions?',
   'They are listed in full on <a href="' + SHORT_VS_FULL + '">T2 Short vs '
   'Full T2</a>, and the <a href="' + ELIG + '">T2 Short eligibility '
   'checker</a> tests all eight at once.'),
  ('Which condition fails most often?',
   'A dividend paid or received, and not being a Canadian-controlled private '
   'corporation throughout the year. Each also means the year is not a nil '
   'year for this service, so they decide more than the form.'),
  ('Does the short return carry fewer schedules?',
   'No. GIFI Schedules 100, 125 and 141 are required where anything sits on '
   'the books, on either form. The short return is shorter, not lighter.'),
  ('Does the fee change if the full T2 is needed?',
   'No. The fee is ' + PRICE + ' either way. Which form the year goes on does '
   'not change what the work costs.'),
  ('Can some of my years use one form and some the other?',
   'Yes. Each tax year is tested on its own, so a corporation can be on the '
   'short return one year and the full T2 the next.'),
  ('Is Form T183CORP needed on the short return?',
   'Yes. An authorized signing officer signs Form T183CORP before the return '
   'is transmitted, on either form.'),
  ('How long until the confirmation arrives?',
   'Your CRA confirmation is emailed within 3 business days of transmission, '
   'on either form.'),
  ('What happens if the short return is filed when a condition fails?',
   'The return is the wrong one for that year, and the transmission risks '
   'being rejected. That is why the conditions are tested before the return '
   'is prepared rather than after.'),
  ('My year had a loss. Is that a nil year?',
   'Not necessarily. A loss means something happened. A nil year is one in '
   'which nothing moved through the corporation, and the '
   '<a href="' + NIL_ELIG + '">nil T2 eligibility checker</a> tests it.'),
  ('Does using the short return change the deadline?',
   'No. The return is due six months after the end of the tax year on either '
   'form.'),
  ('Which tool should I run first?',
   'The <a href="' + NIL_ELIG + '">nil T2 eligibility checker</a>, which says '
   'whether the year is nil. The <a href="' + ELIG + '">T2 Short eligibility '
   'checker</a> then says which form carries it.'),
 ],
)


if __name__ == '__main__':
    # build_f7 carries November 4 for the twenty pages built that day. Both
    # price columns here are our own published fee rather than a competitor's,
    # so "Prices checked" is the date our own fee was confirmed, and it is the
    # build date. Set before write() so the stamp, the review line and
    # cnf_last_verified_et all follow.
    b.TODAY, b.ISO = 'November 18, 2026', '2026-11-18'
    assert 'HST' not in str(PAGE), 'a national page may not name HST'
    check(PAGE)
    write(PAGE, 'f7q-manifest.json')
