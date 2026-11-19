"""Per-vertical copy for Family 1.

Section 6(k) sets a 0.60 similarity ceiling across a family. A name swap alone
is nowhere near it: the Family 3 experiment scored 0.976 when only the city
name changed. So every vertical supplies its own prose rather than its own
noun, exactly as build/f3/city_copy.py does for the cities.

Each entry carries the whole page's writing. The builder holds the structure
and nothing else.
"""

VERTICALS = {

 'numbered-holding-corporations': {
  'name':   'Numbered Holding Corporations',
  'short':  'numbered holding corporation',
  'plural': 'numbered holding corporations',
  'kw':     'nil t2 filing for holding company',
  'title':  'Nil T2 Filing for Holding Companies | Numbered Corporations',
  'desc':   'When a numbered holding corporation files a nil T2 and when its '
            'year is not nil, which schedules it files, and what it costs.',

  # Hero
  'h1':   'Nil T2 Filing for Holding Companies',
  'lede': 'A numbered holding corporation files a T2 for every tax year it '
          'exists, whether or not it did anything. Where the year is '
          'genuinely nil, that return is $300.00 plus HST per tax year.',

  # Section 1, the two-paragraph fact pattern the plan requires at line 1209
  'intro_h': 'Nil T2 Filing for Numbered Holding Corporations',
  'intro': (
    'A numbered holding corporation is incorporated to hold something rather '
    'than to trade: shares in an operating company, a parcel of land, a '
    'portfolio, or nothing at all while the owner decides what comes next. It '
    'has a number for a name because it was never given one, which is why so '
    'many sit quiet for years. Quiet is not the same as closed. The '
    'corporation exists until it is dissolved, and paragraph 150(1)(a) makes '
    'the T2 due every year it exists.',
    'The question is never whether the return is due. It is whether the year '
    'was nil. A holding corporation that received no dividend, earned no '
    'interest, collected no rent and disposed of nothing has a nil year, and '
    'that return is prepared, CPA reviewed, signed on a T183CORP and '
    'transmitted electronically for $300.00 plus HST per tax year. A holding '
    'corporation that received any of those has income, and this is not the '
    'service for it.'),

  # Rule 8. This family is the one the rule was written for, so it leads
  # rather than sitting in a footnote.
  'notnil_h': 'When a Numbered Holding Corporation Is Not Nil',
  'notnil_boxes': [
    ('A Dividend Was Received',
     'A dividend from the operating company is income to the holding '
     'corporation. The year is not nil, whatever was done with the money.'),
    ('Interest Was Earned',
     'Interest on a balance, a term deposit or a loan to a related company is '
     'income. A few dollars of it still makes the year not nil.'),
    ('Rent Was Collected',
     'A corporation holding property that collects rent is a rental '
     'corporation for the year. It is not nil and files a full T2.'),
    ('Something Was Disposed Of',
     'A sale of shares, land or any capital property puts a gain or loss in '
     'the year. The year is not nil even where the gain is zero.'),
  ],
  'notnil_text': (
    'This matters more for holding corporations than for any other kind, '
    'because the thing a holding corporation holds tends to pay something. A '
    'single dividend cheque, one interest posting on a bank statement or one '
    'month of rent moves the year out of nil and into an ordinary corporate '
    'return with income to report.',
    'Where that is the year you have, Gondaliya CPA Professional Corporation '
    'prepares it at gondaliyacpa.ca for $350.00 plus HST per year. The nil '
    'service here is for the years in which the holding corporation genuinely '
    'did nothing, and those are usually the unfiled ones.'),

  # Plan line 1209: "No vertical page publishes without its own six-field
  # schedule requirement row". S100, S125, S141, S50, S24, S8.
  'sched_h': 'Which T2 Schedules a Numbered Holding Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information',
     'Required',
     'A holding corporation holds something, so the balance sheet is never '
     'empty. Shares, a loan to a shareholder or share capital alone makes '
     'Schedule 100 required.'),
    ('Schedule 125', 'Income statement information',
     'Required',
     'Filed with Schedule 100. It reports nil revenue and nil expenses for '
     'the year rather than being left out.'),
    ('Schedule 141', 'Notes checklist',
     'Required',
     'Accompanies Schedules 100 and 125 and records who prepared the '
     'financial information and on what basis.'),
    ('Schedule 50', 'Shareholder information',
     'Required',
     'Every shareholder holding 10% or more of any class is listed. A '
     'single-shareholder numbered corporation still files it.'),
    ('Schedule 24', 'First-time filer information',
     'First return only',
     'Filed on the corporation&rsquo;s first T2 after incorporation, then not '
     'again.'),
    ('Schedule 8', 'Capital cost allowance',
     'Only with depreciable property',
     'A holding corporation that owns no depreciable property does not file '
     'it. One that holds a building does.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, read against the facts of a holding '
                'corporation with no activity in the year. Last reviewed '
                'November 19, 2026.',
  'sched_boxes': [
    ('The GIFI Trio Is Not Optional Here',
     'An operating corporation with truly nothing on its books may omit '
     'Schedules 100, 125 and 141. A holding corporation rarely can.'),
    ('Schedule 50 Lists One Name or Many',
     'The 10% test applies per class of share. A sole shareholder is still a '
     'shareholder and still appears.'),
    ('Schedule 24 Catches the First Year',
     'A corporation catching up several unfiled years files Schedule 24 with '
     'the earliest of them, not with the most recent.'),
  ],

  # Original checklist, the plan's second unique-data option at line 1209.
  'chk_yes': [
    'No dividend was received from any corporation it holds shares in',
    'No interest was posted on any account, deposit or inter-company loan',
    'No rent was collected on property it owns',
    'Nothing was sold, transferred or otherwise disposed of',
    'No expense was claimed, including management or accounting fees',
  ],
  'chk_no': [
    'A dividend arrived, even one reinvested or left on account',
    'A bank or investment account paid interest of any amount',
    'Property it holds produced rent for any part of the year',
    'Shares, land or equipment changed hands, at a gain, a loss or neither',
    'The corporation paid anything it intends to deduct',
  ],
  'chk_both': [
    'The T2 return itself, for every year the corporation exists',
    'A T183CORP signed by an authorised signing officer, one per tax year',
    'Schedule 50 listing every shareholder at 10% or more',
    'The federal or provincial annual return, which is a separate filing',
    'Dissolution, before the obligation to file finally ends',
  ],

  'why_h': 'Why Numbered Holding Corporations Use This Service',
  'why': [
    ('Built for the Quiet Year',
     'The whole service assumes a year with nothing in it. There is no '
     'discovery call and no engagement letter for a return that reports nil.'),
    ('One Price, Every Year',
     'Six unfiled years cost six times $300.00 plus HST and nothing else. No '
     'hourly billing, no schedule surcharge.'),
    ('The Nil Test Happens First',
     'The year is checked against the not-nil list above before anything is '
     'charged. A year with a dividend in it is sent to the right service.'),
    ('Filed, Not Advised',
     'The return is prepared, reviewed by a CPA Ontario member, signed on a '
     'T183CORP and transmitted. That is the whole engagement.'),
  ],
  'strip': [
    ('Each Year Is Its Own Return',
     'A holding corporation with four unfiled years files four T2 returns and '
     'signs four T183CORP forms.'),
    ('Oldest Year First',
     'Returns are filed in order so the balance sheet carries forward '
     'correctly from year to year.'),
    ('Nothing to Print',
     'Every T183CORP is signed electronically through an access-controlled '
     'secure portal.'),
  ],

  'svc_h': 'What a Numbered Holding Corporation Usually Needs Next',
  'proc_h': 'How a Holding Corporation&rsquo;s Nil T2 Gets Filed',
  'proc_lede': 'Four steps, no meeting, and no document to post. The whole '
               'engagement runs from the filing form.',
  'proc_note': 'The sequence is the same whether the corporation has one '
               'unfiled year or eight:',
  'steps': [
    ('Confirm the Year Was Nil',
     'The year is tested against dividends, interest, rent and dispositions '
     'before anything is charged.'),
    ('Match the Year-End to the CRA Record',
     'The fiscal year-end on the return has to match the one the Agency '
     'holds, or the transmission is rejected.'),
    ('Prepare the Return and Its Schedules',
     'The T2 with Schedules 100, 125, 141 and 50, plus Schedule 24 where it '
     'is the first return.'),
    ('Sign and Transmit',
     'You sign one T183CORP for each tax year. The CRA confirmation is '
     'emailed within 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Numbered Holding Corporation',
  'price_eyebrow': 'One Price Per Tax Year',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year. That covers the T2, the '
    'GIFI schedules where they are required, Schedule 50, Schedule 24 on a '
    'first return, the T183CORP package with secure e-signing, CPA review '
    'before transmission, electronic transmission by a registered EFILE '
    'electronic filer, one corrected transmission where the Agency rejects '
    'the first, and the CRA confirmation emailed within 3 business days. '
    'A holding corporation year that is not nil is $350.00 plus HST per year '
    'at gondaliyacpa.ca.'),

  'geo_h': 'Nil T2 Filing for Holding Corporations Across Canada',
  'cta_h': 'File the Quiet Years and Close the Gap',

  'faq': [
   ('Does a numbered holding corporation with no activity still file a T2?',
    'Yes. Paragraph 150(1)(a) makes the return due for every tax year the '
    'corporation exists, and a holding corporation exists until it is '
    'dissolved. Holding nothing, trading nothing and banking nothing changes '
    'what goes in the return, not whether it is due.'),
   ('Is a holding company that receives dividends nil?',
    'No. A dividend received is income to the holding corporation, so the '
    'year is not nil and the return is a full T2 with income to report. That '
    'is handled by Gondaliya CPA Professional Corporation at gondaliyacpa.ca '
    'for $350.00 plus HST per year.'),
   ('My holding corporation only holds shares in my operating company. Is '
    'that year nil?',
    'It can be, where the shares paid nothing. Holding an asset is not income '
    'by itself. The year stops being nil the moment the operating company '
    'pays a dividend, the holding corporation earns interest, or anything is '
    'sold.'),
   ('Which schedules does a nil holding corporation file?',
    'Schedules 100, 125, 141 and 50 in almost every case, plus Schedule 24 on '
    'the first return after incorporation. Schedule 8 is filed only where the '
    'corporation owns depreciable property. The table above sets out each one '
    'and when it applies.'),
   ('Can a holding corporation skip the GIFI schedules?',
    'Rarely. The exemption is for a corporation with genuinely nothing to '
    'report, and a holding corporation has a balance sheet by definition. '
    'Share capital, a shareholder loan or the shares it holds all put figures '
    'on Schedule 100, which makes Schedules 125 and 141 required with it.'),
   ('How many unfiled years can be filed at once?',
    'There is no cap. Each year is a separate T2 at $300.00 plus HST per tax '
    'year with its own T183CORP, and they are filed oldest first so the '
    'balance sheet carries forward correctly.'),
   ('Does a numbered corporation need a name before it can file?',
    'No. The number is the legal name. The return carries the corporation '
    'name exactly as the registry holds it, which for a numbered corporation '
    'is the number followed by the legislation it was incorporated under.'),
   ('What happens to a holding corporation that never filed?',
    'The year stays open indefinitely. The Canada Revenue Agency can issue a '
    'demand to file and then assess the corporation arbitrarily, and an '
    'unfiled year blocks the clearance certificate needed to dissolve. '
    'Filing the outstanding returns is what closes it.'),
   ('Is the T183CORP signed once or once per year?',
    'Once per tax year. Each year is a separate return with its own '
    'transmission, so a corporation filing five unfiled years signs five '
    'T183CORP forms. All of them can be signed electronically in one sitting.'),
   ('What if the holding corporation is being wound up?',
    'The final T2 is due within six months of the date of dissolution, and '
    'every earlier year has to be filed before a clearance certificate will '
    'be issued. Nil years in that run are filed at the same $300.00 plus HST '
    'per tax year.'),
  ],
 },

}
