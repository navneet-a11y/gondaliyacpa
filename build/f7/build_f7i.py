#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 9: /compare/ontario-annual-return-vs-t2/

Why this page, and why it could not be built until today
--------------------------------------------------------
Appendix A line 3268 lists it. It was blocked because the left-hand column is
the Ontario annual return, a filing this service does not sell, so line 1215's
"two published price cells, every one filled" had nothing to put there.

Navneet ruled on November 5, 2026: such a cell carries a statement about this
firm and never a figure. So the first price row reads "Not offered. We file nil
T2 returns only", and build_f7.check() now refuses any decline cell that
contains a dollar sign. This is the first page built on that ruling.

The second price row is not a decline. /guides/provincial-and-federal-annual-
returns/ states what the Ontario annual return costs the corporation in its own
words -- "It carries no tax and no payment" -- so that row is published fact on
both sides rather than a gap.

The $12.00 Corporations Canada fee is not on this page
-----------------------------------------------------
The guide states it, and gate.py's money allowlist could carry it. It is left
off because this comparison is the Ontario annual return against the T2, and a
federal registry fee on it would be a third subject. Page 6
(/compare/federal-corporation-vs-ontario-corporation-nil-filing/) made the same
call for the same reason.

Not the same page as page 6
---------------------------
Page 6 compares two corporations and concludes the T2 does not change with the
place of incorporation. This page compares two filings and concludes neither
satisfies the other. They touch the same guide and answer different questions;
line 1212 is about two URLs covering one comparison, not two URLs citing one
source. The boundary held here: this page says nothing about which registry a
corporation belongs to, and page 6 says nothing about what a missed annual
return causes.

Agreeing with what is already published
---------------------------------------
From /guides/provincial-and-federal-annual-returns/:

  "The T2 is a tax return filed with the Canada Revenue Agency. An annual
   return is a registry filing that confirms who the directors are."
  "Filing the T2 does not satisfy an annual return, and filing an annual
   return does not satisfy the T2. A corporation needs both, every year, for
   as long as it exists."
  "An Ontario corporation files an annual return confirming its registered
   office address, its directors and its officers. It carries no tax and no
   payment."
  "Until 2021 this was filed alongside the T2. Since October 2021 it is filed
   through the Ontario Business Registry instead, and a corporation that has
   not looked at the rules since then is probably not filing it."
  "Because the filing moved out of the T2, nothing in the corporate tax return
   now prompts an owner to do it."
  "An annual return is not a tax filing, so having no income does not excuse
   it."
  "A missed annual return does not create tax. It creates a registry record
   that is out of date, and after enough missed years it creates a corporation
   the registry treats as abandoned."
  "The two trails are independent. A corporation can be fully current on its
   T2 filings and still be struck from its registry, and it can be in good
   standing at the registry while owing ten years of T2 returns."
  "Where annual returns go unfiled for long enough, the registry may dissolve
   or strike the corporation. That is not dissolution for tax purposes, and it
   cancels no outstanding T2 return."
  "A corporation struck from a registry with unfiled tax years is in the worst
   of both positions: it cannot trade and it still owes returns."
  "Registry annual returns, the Alberta AT1 and the Quebec CO-17 are separate
   filings and are not included in the fee."
"""
import build_f7
from build_f7 import T, G, COST, PRICE, check, write

build_f7.TODAY, build_f7.ISO = 'November 5, 2026', '2026-11-05'

DECLINE = 'Not offered. We file nil T2 returns only'

PRICE_ROWS = [
 ('Our published fee for a quiet year', DECLINE, PRICE, True),
 ('What the filing itself costs the corporation',
  'No tax and no payment',
  'No tax on a quiet year, because the corporation owes $0.00. The fee above '
  'is for preparing, reviewing and transmitting the return', True),
]

FEATURE_ROWS = [
 ('Which body receives it',
  'The Ontario Business Registry',
  'The Canada Revenue Agency', True),
 ('What it reports',
  'The registered office address, the directors and the officers',
  'The corporation&rsquo;s income and financial position for the tax year',
  True),
 ('When it is due',
  'At the tax year-end, through the Ontario Business Registry',
  'Six months after the fiscal year-end', True),
 ('Whether filing one satisfies the other',
  'No. Filing an annual return does not satisfy the T2',
  'No. Filing the T2 does not satisfy an annual return', True),
 ('Whether a dormant corporation owes it',
  'Yes. It confirms directors rather than income, so having no activity does '
  'not excuse it',
  'Yes. Every resident corporation files for every tax year, whether or not '
  'it did anything', False),
 ('Where it was filed before October 2021',
  'Alongside the T2, which is why many owners believe it still travels with '
  'it',
  'On its own, as it always has been', True),
 ('What a missed year causes',
  'A registry record that is out of date, and after enough missed years a '
  'corporation the registry treats as abandoned',
  'A tax year that stays open, a demand to file and an arbitrary assessment',
  True),
 ('Whether this fee covers it',
  'No. A registry filing is not part of nil T2 filing',
  'Yes, at ' + PRICE, True),
]

PAGE = dict(
 col_a='Ontario Annual Return', col_b='Nil T2 Return',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 stamp=('Our own <a href="' + COST + '">published fee</a> is for the nil T2. '
        'We file nil T2 returns only, so the left column carries no fee of '
        'ours.'),
 disclosure=('This comparison sets a registry filing we do not offer against '
             'the tax return we do, and names no other provider. Where a '
             'comparison on this site does name one, it states that '
             'provider&rsquo;s published prices and published features '
             'only.'),
 table_note=('Nine rows differ and one does not. The one that does not is the '
             'row owners most often get wrong: a dormant corporation owes '
             'both, because an annual return confirms who the directors are '
             'rather than what the corporation earned.'),
 slug='ontario-annual-return-vs-t2',
 title='Ontario Annual Return vs T2 | Two Different Filings',
 h1='Ontario Annual Return vs the T2',
 h1_pre='Ontario Annual Return vs ', h1_span='the T2',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='ontario annual return vs t2',
 meta=('Two filings are both called a return. One goes to the Ontario '
       'Business Registry and one to the Canada Revenue Agency, and neither '
       'satisfies the other.'),
 seo_title='Ontario Annual Return vs T2',
 seo_desc=('Two filings, two bodies, two deadlines. What the Ontario annual '
           'return reports, what the T2 reports, and why a dormant '
           'corporation owes both.'),
 answer=('They are two different filings. The T2 is a tax return filed with '
         'the Canada Revenue Agency. The Ontario annual return is a registry '
         'filing that confirms the registered office address, the directors '
         'and the officers, and it carries no tax and no payment. Filing the '
         'T2 does not satisfy an annual return, and filing an annual return '
         'does not satisfy the T2: a corporation needs both, every year, for '
         'as long as it exists. We file the nil T2, at ' + PRICE + '. The '
         'registry filing is not part of that.'),
 cta2=('Separate the Two Filings', T + 'annual-return-vs-tax-return-checker/'),
 lead=[('Two Filings, Both Called a Return',
        ['<p>Two different things are called a return, and confusing them is '
         'the most common compliance gap a dormant corporation has. One is a '
         'tax return and one is a registry filing, and they go to different '
         'bodies on different dates for different reasons.</p>',
         '<p>Until 2021 the Ontario annual return was filed alongside the T2, '
         'so one act covered both and nobody had to know the difference. '
         'Since October 2021 it is filed through the Ontario Business '
         'Registry instead, and a corporation that has not looked at the '
         'rules since then is probably not filing it.</p>',
         '<p>That is the whole problem in one sentence. Because the filing '
         'moved out of the T2, nothing in the corporate tax return now '
         'prompts an owner to do it. The prompt has to come from the owner or '
         'the adviser.</p>']),
       ],
 detail=dict(
  h2='The Two Trails Are Independent',
  intro=('Being current on one says nothing at all about the other:'),
  items=[
   'Filing the T2 does not satisfy an annual return, and filing an annual '
   'return does not satisfy the T2. A corporation needs both, every year, for '
   'as long as it exists.',
   'A corporation can be fully current on its T2 filings and still be struck '
   'from its registry.',
   'It can be in good standing at the registry while owing ten years of T2 '
   'returns.',
   'An annual return is not a tax filing, so having no income does not excuse '
   'it. A dormant corporation confirms its directors and its registered '
   'office every year exactly as an active one does.',
   'A missed annual return does not create tax. It creates a registry record '
   'that is out of date, and after enough missed years a corporation the '
   'registry treats as abandoned.',
   'Where annual returns go unfiled for long enough, the registry may '
   'dissolve or strike the corporation. That is not dissolution for tax '
   'purposes, and it cancels no outstanding T2 return.',
  ],
  warn=('A corporation struck from a registry with unfiled tax years is in '
        'the worst of both positions: it cannot trade and it still owes '
        'returns.'),
  close=('The <a href="' + T + 'annual-return-vs-tax-return-checker/">annual '
         'return versus tax return checker</a> separates the two for your own '
         'corporation, the <a href="' + T + 'involuntary-dissolution-risk-'
         'checker/">involuntary dissolution checker</a> takes being struck '
         'from the registry, and the '
         '<a href="' + G + 'provincial-and-federal-annual-returns/">complete '
         'guide to provincial and federal annual returns</a> sets out every '
         'registry and every date.')),
 band=('The T2 Is the Part We File',
       'Nil T2 filing covers the federal corporate return for a quiet year, '
       'at ' + PRICE + '. The registry filing stays with the corporation.'),
 cards=[('Reviewed by a CPA',
         'The return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('What the fee covers',
         'The T2 itself, GIFI Schedules 100, 125 and 141 where required, '
         'Schedule 50, Schedule 24 on a first return, Schedule 8 and loss '
         'continuity, and electronic transmission.'),
        ('What it does not cover',
         'Registry annual returns are separate filings and are not included. '
         'So are the Alberta AT1 and the Quebec CO-17, each a separate '
         'provincial return where the corporation is in that province.')],
 case=('An Ontario corporation with six years of filed T2 returns and no '
       'annual returns since 2021',
       'Its tax record is clean: six quiet years, each filed, each with a CRA '
       'confirmation. Its registry record is four years out of date, because '
       'the annual return stopped travelling with the T2 in October 2021 and '
       'nothing in the tax return prompted anyone to file it. The two trails '
       'are independent, so the clean tax record does not help at the '
       'registry, and after enough missed years the registry may strike the '
       'corporation. Being struck is not dissolution for tax purposes and '
       'cancels no outstanding T2 return. We file the T2 side at ' + PRICE
       + '; the annual returns are filed through the Ontario Business '
       'Registry by the corporation. The figures here illustrate how the '
       'rules apply and are not drawn from a client file.'),
 faq=[
  ('Is the Ontario annual return the same as the T2?',
   'No. The T2 is a tax return filed with the Canada Revenue Agency. The '
   'annual return is a registry filing that confirms the registered office '
   'address, the directors and the officers.'),
  ('Does filing my T2 cover the annual return?',
   'No, and the reverse is also true. Filing an annual return does not '
   'satisfy the T2. A corporation needs both, every year, for as long as it '
   'exists.'),
  ('Do you file the Ontario annual return for me?',
   'No. We file nil T2 returns only. The annual return is filed through the '
   'Ontario Business Registry.'),
  ('Is it included in the ' + PRICE + ' fee?',
   'No. Registry annual returns are separate filings. The fee covers the '
   'federal nil T2 corporate tax return.'),
  ('What does the Ontario annual return cost?',
   'It carries no tax and no payment. What it costs is the filing itself, '
   'through the Ontario Business Registry.'),
  ('Did it used to be filed with the T2?',
   'Yes. Until 2021 it was filed alongside the T2. Since October 2021 it goes '
   'through the Ontario Business Registry instead, which is why many owners '
   'believe it still travels with the tax return.'),
  ('Why did nobody tell me it changed?',
   'Because the filing moved out of the T2, nothing in the corporate tax '
   'return now prompts an owner to do it. The prompt has to come from the '
   'owner or the adviser.'),
  ('Does a dormant corporation have to file an annual return?',
   'Yes. An annual return is not a tax filing, so having no income does not '
   'excuse it. A dormant corporation confirms its directors and registered '
   'office exactly as an active one does.'),
  ('What happens if I miss an annual return?',
   'It does not create tax. It creates a registry record that is out of date, '
   'and after enough missed years a corporation the registry treats as '
   'abandoned.'),
  ('Can I be struck from the registry while my taxes are current?',
   'Yes. The two trails are independent. A corporation can be fully current '
   'on its T2 filings and still be struck from its registry.'),
  ('Can it work the other way round?',
   'Yes. A corporation can be in good standing at the registry while owing '
   'ten years of T2 returns.'),
  ('If the registry strikes my corporation, do the T2 returns go away?',
   'No. Being struck is not dissolution for tax purposes and it cancels no '
   'outstanding T2 return.'),
  ('When is each one due?',
   'The T2 is due six months after the fiscal year-end. The Ontario annual '
   'return goes at the tax year-end, through the Ontario Business Registry.'),
  ('What about Alberta and Quebec?',
   'Those are a different thing again. Alberta administers its own corporate '
   'income tax through the AT1 and Quebec through the CO-17, each a separate '
   'provincial return rather than an annual return.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'annual-return-vs-tax-return-checker/">annual return '
   'versus tax return checker</a>, which separates what this service covers '
   'from what the registry wants.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7i-manifest.json')
