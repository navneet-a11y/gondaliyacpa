#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 7, page 13: /compare/dissolving-vs-filing-nil-every-year/

Why this page
-------------
Not in Appendix A, which lists 13 of its stated 20 F7 URLs. It is the last of
the concept pages that can be built from published material, and it is the one
where the site's own commercial interest points the wrong way, which is the
reason it needs care rather than enthusiasm.

The asymmetry is already the site's published position
------------------------------------------------------
/tools/dissolve-or-keep-filing-cost-calculator/ prices both routes and says
plainly why only one of them totals:

  "The returns are priced here, so the cost of staying open totals exactly.
   Winding up involves a clearance certificate request and the registry
   articles of dissolution, and neither is covered by this fee."
  "So the comparison names those steps rather than putting a figure on them. A
   page that invented a total for the dissolution side would be more
   satisfying to read and less use to rely on."

So the second price row names the steps instead of pricing them. That is not
the November 5 decline rule being stretched: it is the same reasoning the live
tool already published, and it means neither price cell is empty and no figure
is invented.

The one thing this page must not do
-----------------------------------
This service sells a nil return for every year a corporation stays open. A page
that argued for dissolution would be arguing against its own revenue, and a
page that argued for keeping the corporation would be selling a subscription.
The tool already refuses both, and this page quotes it:

  "Which is often the right decision. There are good reasons to hold a name, a
   history or a registration. It is worth seeing as a subscription rather than
   as a formality."
  "Filing for another five years ends nothing. At the end of it the
   corporation is still on the register and the same question arrives again,
   five years of fees later."
  "A completed wind-up ends the obligation. That is the difference the
   right-hand column is really reporting, and it is worth more weight than the
   arithmetic."

Both sentences are on the page, the second in the warning block, so the reader
gets the cost of staying open and the limit of paying it, from the same source.

Agreeing with what is already published
---------------------------------------
From /guides/winding-up-an-inactive-corporation/:

  "Closing a corporation involves two authorities that do not talk to each
   other on your behalf."
  "A corporation struck from a registry with open tax years still has those
   years open, and a corporation fully filed but never dissolved keeps
   acquiring new filing obligations."
  "A corporation cannot be wound up cleanly with an open year on its record."
  "Nine dormant years are nine returns. They are prepared oldest first and can
   be transmitted together, each at $300.00 plus HST per tax year."
  "It is requested in writing and it cannot be issued while a year is
   unfiled."
  "distributing the corporation's property without one can leave them liable"
  "The final return covers the period from the start of the last tax year to
   the date of dissolution. It is due six months after that date."
  "It is marked as the final return, which is what tells the Agency to expect
   no further years."
  "A corporation cannot be dissolved holding property."
  "A disposition is activity. A corporation that sells or transfers property in
   its last period does not have a nil final year, and that return is handled
   by Gondaliya CPA Professional Corporation at gondaliyacpa.ca at $350.00
   [plus HST per year]."
  "The registry is the one the corporation was incorporated under... Filing
   with the wrong one achieves nothing."
  "Dissolution does not seal the record. An assessment, a reassessment or a
   demand relating to a period before dissolution can still be issued."
  Accounts: GST/HST and payroll each closed with Form RC145; until then "Nil
  returns remain due" and "Nil remittances remain expected".

From /tools/dissolve-or-keep-filing-cost-calculator/, the fee boundary:
"The registry annual return each year | Keep filing | No, a government fee";
"A clearance certificate request | Wind up | No"; "The registry articles of
dissolution | Wind up | No".

What is not on this page
------------------------
No registry fee figure. The winding-up guide says a federal dissolution carries
"its own fee" and that a provincial one "depends on the province", without
stating either, so there is nothing to quote. The order of the six wind-up
steps is in the guide and is summarised rather than reproduced: this is a
comparison, and /guides/winding-up-an-inactive-corporation/ owns the sequence.
"""
import build_f7
from build_f7 import T, G, COST, PRICE, check, write

build_f7.TODAY, build_f7.ISO = 'November 5, 2026', '2026-11-05'

PRICE_ROWS = [
 ('Our published fee on this route',
  'A nil T2 for every year it stays open, at ' + PRICE,
  'The final T2 for the period ending at dissolution, at ' + PRICE, True),
 ('What the route costs beyond that fee',
  'The registry annual return each year, which is a government fee rather '
  'than ours',
  'A clearance certificate request and the registry articles of dissolution. '
  'Neither is covered by this fee, so this page names them rather than '
  'putting a figure on them', True),
]

FEATURE_ROWS = [
 ('How long the filing obligation runs',
  'Every year, within six months of the fiscal year-end, until the '
  'corporation is formally dissolved',
  'It ends once the wind-up is complete and the final return is marked final',
  True),
 ('What the route ends',
  'Nothing. At the end of it the corporation is still on the register and the '
  'same question arrives again',
  'The obligation', True),
 ('Years already outstanding',
  'Filed first, oldest first',
  'Filed first, oldest first. Both routes start in the same place', False),
 ('Whether a clearance certificate is involved',
  'No',
  'Not a filing requirement, but distributing the corporation&rsquo;s '
  'property without one can leave the directors personally liable, and it '
  'cannot be issued while a year is unfiled', True),
 ('What the registry is for',
  'The annual return each year, filed with the registry the corporation was '
  'incorporated under',
  'Articles of dissolution, filed with that same registry. Filing with the '
  'wrong one achieves nothing', True),
 ('Whether the corporation can still hold property',
  'Yes',
  'No. A corporation cannot be dissolved holding property, and a disposition '
  'is activity: that final year is not nil and is handled at gondaliyacpa.ca '
  'at $350.00 plus HST per year', True),
 ('The GST/HST and payroll accounts',
  'Nil returns and nil remittances remain due for as long as they are open',
  'Closed with Form RC145, after the final T2', True),
 ('Whether anything can still arrive afterwards',
  'Yes, next year&rsquo;s return',
  'Yes. Dissolution does not seal the record: an assessment, a reassessment '
  'or a demand for a pre-dissolution period can still be issued', False),
]

PAGE = dict(
 col_a='Keep Filing Nil Returns', col_b='Wind the Corporation Up',
 price_rows=PRICE_ROWS, feature_rows=FEATURE_ROWS, faq_n=15,
 stamp=('Both fees are our own <a href="' + COST + '">published fee</a>. A '
        'clearance certificate request and the registry articles of '
        'dissolution are not priced here, so the table names them instead.'),
 disclosure=('This comparison sets two courses of action against each other, '
             'both of which begin with returns we file, and names no other '
             'provider. Where a comparison on this site does name one, it '
             'states that provider&rsquo;s published prices and published '
             'features only.'),
 table_note=('Eight rows differ and two do not, and the two that do not are '
             'the ones to read first: outstanding years come first on either '
             'route, and neither route seals the record. Only one side also '
             'totals. The returns are priced here; a clearance certificate '
             'request and the registry articles of dissolution are not, so '
             'this page names those steps rather than inventing a figure for '
             'them.'),
 slug='dissolving-vs-filing-nil-every-year',
 title='Dissolving vs Filing Nil Every Year | Both Routes',
 h1='Dissolving vs Filing Nil Every Year',
 h1_pre='Dissolving vs ', h1_span='Filing Nil Every Year',
 eyebrow='Comparison &#183; Nil T2 Filing &#183; Canada',
 keyword='dissolving vs filing nil every year',
 meta=('Keeping an empty corporation is a return every year for as long as it '
       'exists. Winding it up ends the obligation. What each route costs and '
       'what each one ends.'),
 seo_title='Dissolving vs Filing Nil Every Year',
 seo_desc=('A return every year for as long as the corporation exists, or a '
           'wind-up that ends the obligation. What each route costs, and why '
           'only one of them totals.'),
 answer=('Keeping an empty corporation is a decision to file a return every '
         'year, within six months of the fiscal year-end, for as long as it '
         'exists, at ' + PRICE + '. Winding it up is one final return plus a '
         'clearance certificate request and the registry articles of '
         'dissolution, and those last two are not covered by this fee. Either '
         'route starts in the same place: every outstanding year is filed '
         'first, because a clearance request rests on a complete filing '
         'record and dissolving anyway leaves those years open behind the '
         'corporation.'),
 cta2=('Price Both Routes', T + 'dissolve-or-keep-filing-cost-calculator/'),
 lead=[('Two Authorities That Do Not Talk to Each Other',
        ['<p>Closing a corporation involves two authorities that do not talk '
         'to each other on your behalf. The tax side is settled with the '
         'Canada Revenue Agency; the legal existence of the corporation is '
         'ended by the registry it was incorporated under.</p>',
         '<p>Doing one and not the other is the usual failure. A corporation '
         'struck from a registry with open tax years still has those years '
         'open, and a corporation fully filed but never dissolved keeps '
         'acquiring new filing obligations.</p>',
         '<p>So the question is not really which is cheaper this year. It is '
         'whether the corporation is being kept for a reason, because a '
         'return falls due every year until it is formally dissolved, and '
         'nothing about being empty changes that.</p>']),
       ],
 detail=dict(
  h2='Only One Side Totals, and That Is Deliberate',
  intro=('The tool that prices both routes is direct about why, and the same '
         'applies here:'),
  items=[
   'A corporation files a T2 within six months of its fiscal year-end, every '
   'year, until it is formally dissolved. Holding an empty corporation is a '
   'decision to pay for a return annually for as long as it exists.',
   'The returns are priced here, so the cost of staying open totals exactly.',
   'Winding up involves a clearance certificate request and the registry '
   'articles of dissolution, and neither is covered by this fee.',
   'A page that invented a total for the dissolution side would be more '
   'satisfying to read and less use to rely on.',
   'Where years are already outstanding the choice narrows, because both '
   'routes start in the same place. A clearance request rests on a complete '
   'filing record, and dissolving a corporation that still owes returns '
   'leaves those years open behind it.',
   'Filing for another five years ends nothing. At the end of it the '
   'corporation is still on the register and the same question arrives again, '
   'five years of fees later.',
   'A completed wind-up ends the obligation, and that is worth more weight '
   'than the arithmetic.',
  ],
  warn=('Keeping an empty corporation is often the right decision. There are '
        'good reasons to hold a name, a history or a registration, and this '
        'page is not an argument for either route. It is worth seeing as a '
        'subscription rather than as a formality, and then deciding.'),
  # Removed by Navneet on November 5, 2026. The three links it carried are
  # not lost: the cost calculator is the hero's second button, and all three
  # pages still link in to this one, so nothing is orphaned by dropping it.
  close=''),
 band=('Either Route Starts With the Returns',
       'Every outstanding year is filed first, oldest first, at ' + PRICE
       + '. The decision comes after that rather than instead of it.'),
 cards=[('Reviewed by a CPA',
         'Each return is prepared and reviewed by a CPA Ontario member before '
         'it is transmitted.'),
        ('What the fee covers',
         'The T2 itself, GIFI Schedules 100, 125 and 141 where required, '
         'Schedule 50, Schedule 24 on a first return, Schedule 8 and loss '
         'continuity, and electronic transmission.'),
        ('What sits outside it',
         'A clearance certificate request, the registry articles of '
         'dissolution, the registry annual return, and closing a GST/HST or '
         'payroll account with Form RC145.')],
 case=('A corporation dormant for nine years, whose directors are deciding '
       'whether to keep it',
       'Nine dormant years are nine returns. They are prepared oldest first '
       'and can be transmitted together, each at ' + PRICE + '. That part is '
       'the same whichever route the directors choose, because a clearance '
       'request cannot be issued while a year is unfiled and dissolving '
       'anyway would leave the nine years open behind the corporation. Once '
       'they are filed the choice is real: keep it, and a tenth return falls '
       'due within six months of the next year-end; or wind it up, with a '
       'clearance certificate request and articles of dissolution, neither '
       'priced here, and a final T2 marked final so the Agency expects no '
       'further years. The figures here illustrate how the rules apply and '
       'are not drawn from a client file.'),
 faq=[
  ('Is it cheaper to dissolve or to keep filing?',
   'Only one side of that totals. Keeping it is ' + PRICE + ' for as long as '
   'it exists, plus the registry annual return. Winding up is one final '
   'return plus a clearance request and the registry dissolution, and those '
   'two are not covered by this fee.'),
  ('Why will you not give me a total for dissolving?',
   'Because a clearance certificate request and the registry articles of '
   'dissolution are not priced here. A page that invented a total for them '
   'would be more satisfying to read and less use to rely on.'),
  ('How long do I have to keep filing if I do nothing?',
   'Every year, within six months of the fiscal year-end, until the '
   'corporation is formally dissolved. Being empty changes nothing.'),
  ('Does filing for a few more years settle anything?',
   'No. At the end of it the corporation is still on the register and the '
   'same question arrives again, with the fees for those years spent.'),
  ('Can I dissolve without filing the outstanding years?',
   'Not cleanly. A clearance certificate cannot be issued while a year is '
   'unfiled, and dissolving anyway leaves those tax years open behind the '
   'corporation.'),
  ('So both routes start the same way?',
   'Yes. Every outstanding year is filed first, oldest first. The decision '
   'comes after that rather than instead of it.'),
  ('Is a clearance certificate compulsory?',
   'It is not a filing requirement. Distributing the corporation&rsquo;s '
   'property without one can leave the directors personally liable for '
   'amounts the corporation turns out to owe.'),
  ('What is the final T2?',
   'The return covering the period from the start of the last tax year to the '
   'date of dissolution, due six months after that date and marked as the '
   'final return.'),
  ('Why does the final return come after the registry filing?',
   'Because it runs to the date of dissolution, and that date does not exist '
   'until the registry sets it.'),
  ('Can the corporation still own things when it is dissolved?',
   'No. A corporation cannot be dissolved holding property, and a disposition '
   'is activity, so that final year is not nil. It is handled at '
   'gondaliyacpa.ca at $350.00 plus HST per year.'),
  ('What happens to the GST/HST and payroll accounts?',
   'Each is closed with Form RC145 after the final T2. Until then nil returns '
   'and nil remittances remain due on them.'),
  ('Is keeping an empty corporation ever the right answer?',
   'Often. There are good reasons to hold a name, a history or a '
   'registration. The point is to see the annual return as a subscription '
   'rather than a formality.'),
  ('Does dissolution close the file for good?',
   'No. An assessment, a reassessment or a demand relating to a '
   'pre-dissolution period can still be issued, and a return for such a year '
   'can still be filed.'),
  ('My corporation was struck off by the registry. Is that a wind-up?',
   'No. It was dissolved involuntarily and its tax years are still open. '
   'Registries provide for revival so the outstanding filings can be made and '
   'a proper wind-up completed.'),
  ('Which tool should I run first?',
   'The <a href="' + T + 'dissolve-or-keep-filing-cost-calculator/">dissolve '
   'or keep filing cost calculator</a>, which totals the priced side for the '
   'number of years you have in mind.'),
 ],
)


if __name__ == '__main__':
    check(PAGE)
    write(PAGE, 'f7m-manifest.json')
