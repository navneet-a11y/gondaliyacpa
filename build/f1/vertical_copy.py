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


 'dormant-consulting-corporations': {
  'name':   'Dormant Consulting Corporations',
  'short':  'dormant consulting corporation',
  'plural': 'dormant consulting corporations',
  'kw':     'inactive consulting corporation t2',
  'title':  'Inactive Consulting Corporation T2 | Nil Filing',
  'desc':   'A consulting corporation that stopped taking work still files a '
            'T2 every year. What makes the year nil, which accounts keep '
            'filing, and what it costs.',

  'h1':   'Nil T2 Filing for Dormant Consulting Corporations',
  'lede': 'The contracts stopped, the invoicing stopped, and the corporation '
          'stayed registered. That year is still a filing year, and where it '
          'is genuinely nil the return is $300.00 plus HST per tax year.',

  'intro_h': 'The Consulting Corporation That Went Quiet',
  'intro': (
    'Consulting corporations go dormant more often than almost any other '
    'kind, and usually for the same reason: the owner took a salaried job, '
    'went on leave, moved abroad, or simply stopped looking for the next '
    'engagement. Nothing is wound up because nothing feels finished. The '
    'corporation sits there with a name, a business number and no work going '
    'through it.',
    'None of that ends the filing obligation. A corporation files a T2 for '
    'every tax year it exists, and the year a consultant bills nothing is '
    'still a tax year. What changes is the content of the return, not whether '
    'it is owed. A year with no invoices raised, no expenses claimed and no '
    'money moving is a nil year, filed here at $300.00 plus HST per tax year.'),

  'notnil_h': 'When a Dormant Consulting Corporation Is Not Nil',
  'notnil_boxes': [
    ('A Final Invoice Landed',
     'Work billed in a previous year but paid in this one is still revenue '
     'for the year it was earned. Check the year it was invoiced, not banked.'),
    ('Subscriptions Kept Running',
     'Software, a phone line, accounting fees or a registered-office service '
     'billed to the corporation is an expense. That year is not nil.'),
    ('The Corporation Paid Anyone',
     'A salary, a dividend or a management fee out of the corporation makes '
     'the year active, however small the amount.'),
    ('A Retainer Was Held',
     'Money held on account for a client is a liability that moves. A year '
     'with a retainer taken or released is not nil.'),
  ],
  'notnil_text': (
    'The catch for consultants is almost always the expense side rather than '
    'the income side. A corporation that invoiced nothing all year can still '
    'be paying twelve dollars a month for a cloud subscription or a phone '
    'number nobody answers, and a single claimed expense turns a nil year '
    'into an ordinary one with a loss to report.',
    'A loss year is worth filing properly, because a non-capital loss carries '
    'forward and can shelter income if the consulting work starts again. That '
    'return is prepared by Gondaliya CPA Professional Corporation at '
    'gondaliyacpa.ca for $350.00 plus HST per year. The nil service here is '
    'for the years where genuinely nothing moved.'),

  'sched_h': 'Which T2 Schedules a Dormant Consulting Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Usually required',
     'A consulting corporation that still holds a bank balance, a shareholder '
     'loan or issued share capital has a balance sheet to report.'),
    ('Schedule 125', 'Income statement information', 'Usually required',
     'Filed alongside Schedule 100, reporting nil revenue and nil expenses '
     'for the year.'),
    ('Schedule 141', 'Notes checklist', 'Usually required',
     'Records who prepared the financial information and on what basis. It '
     'accompanies Schedules 100 and 125.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Most consulting corporations have one or two shareholders. Each holding '
     '10% or more of any class is listed by name.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the first T2 after incorporation. A consultant catching up '
     'several years files it with the earliest one.'),
    ('Schedule 8', 'Capital cost allowance', 'Only with depreciable property',
     'A laptop or office furniture still on the books is depreciable '
     'property. Claiming no capital cost allowance in a nil year is normal.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, applied to a consulting corporation '
                'with no billings in the year. Last reviewed November 19, '
                '2026.',
  'sched_boxes': [
    ('The Empty-Books Exemption Is Narrow',
     'Schedules 100, 125 and 141 can be omitted only where there is literally '
     'nothing to report. A bank balance alone rules that out.'),
    ('One Shareholder Still Means Schedule 50',
     'A single-director, single-shareholder consulting corporation files it '
     'with one name on it.'),
    ('Capital Cost Allowance Is Optional',
     'Claiming none in a dormant year keeps the undepreciated balance intact '
     'for a year when the corporation earns again.'),
  ],
  'chk_yes': [
    'No work was invoiced and no fee was earned in the tax year',
    'No subscription, phone, insurance or accounting fee was charged to the corporation',
    'No salary, dividend or management fee was paid out',
    'No equipment was bought, sold or written down',
    'The bank account sat still, or was closed before the year began',
  ],
  'chk_no': [
    'An invoice was raised, even one that went unpaid',
    'A recurring subscription or phone line kept billing the corporation',
    'The corporation paid the owner anything at all',
    'A client retainer was taken in or released',
    'Interest was credited on a business account',
  ],
  'chk_both': [
    'The T2 return, every year until the corporation is dissolved',
    'A T183CORP signed by an authorised signing officer, one per tax year',
    'Any open GST/HST account, which files on its own schedule',
    'Any open payroll account, which files even at nil',
    'The provincial or federal annual return, a separate filing entirely',
  ],

  'why_h': 'Why Dormant Consulting Corporations Use This Service',
  'why': [
    ('No Engagement Overhead',
     'There is no discovery call, no proposal and no engagement letter for a '
     'return that reports nothing.'),
    ('Catch-Up Is the Normal Case',
     'Consultants usually arrive with three or four years outstanding. Each '
     'is $300.00 plus HST, filed oldest first.'),
    ('The Expense Check Happens First',
     'The year is tested against subscriptions and fees before anything is '
     'charged, because that is what usually breaks a nil year.'),
    ('Filed by a CPA, Not Software',
     'A CPA Ontario member reviews the return before it is transmitted '
     'electronically.'),
  ],
  'strip': [
    ('Each Year Files Separately',
     'Four quiet years means four T2 returns and four T183CORP signatures.'),
    ('Filed Oldest First',
     'Returns go in order so balances and any loss carry forward correctly.'),
    ('No Paper Anywhere',
     'The T183CORP is signed electronically through a secure portal.'),
  ],

  'svc_h': 'What a Dormant Consulting Corporation Usually Needs Next',
  'proc_h': 'How a Dormant Consulting Corporation Files',
  'proc_lede': 'Four steps, no meeting, and no paperwork to post. Everything '
               'runs from the filing form.',
  'proc_note': 'The same sequence whether one year is outstanding or six:',
  'steps': [
    ('Test the Year Against Expenses',
     'Subscriptions, phone, insurance and accounting fees are checked before '
     'the year is treated as nil.'),
    ('Confirm the Year-End on Record',
     'The fiscal year-end has to match the one the Canada Revenue Agency '
     'holds or the transmission is rejected.'),
    ('Prepare the Return',
     'The T2 with its schedules, and Schedule 24 where it is the first return '
     'after incorporation.'),
    ('Sign and Transmit',
     'One T183CORP per tax year, signed electronically. The CRA confirmation '
     'is emailed within 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Dormant Consulting Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year. That covers the T2, the '
    'GIFI schedules where they are required, Schedule 50, Schedule 24 on a '
    'first return, the T183CORP package with secure e-signing, CPA review '
    'before transmission, electronic transmission by a registered EFILE '
    'electronic filer, one corrected transmission where the Agency rejects '
    'the first, and the CRA confirmation emailed within 3 business days. A '
    'consulting year with billings or expenses in it is $350.00 plus HST per '
    'year at gondaliyacpa.ca.'),

  'geo_h': 'Nil T2 Filing for Consulting Corporations Across Canada',
  'cta_h': 'Bring the Quiet Years Current',

  'faq': [
   ('I stopped consulting two years ago. Do I still have to file?',
    'Yes. The obligation runs until the corporation is dissolved, not until '
    'the work stops. Both years are due, each as a separate T2, and each is '
    '$300.00 plus HST per tax year.'),
   ('I had no income but I paid for software. Is that year nil?',
    'No. A claimed expense makes the year active, with a loss to report '
    'rather than nil amounts. It is worth filing properly, because a '
    'non-capital loss carries forward against future consulting income.'),
   ('Should I just dissolve the corporation instead?',
    'That is often the right answer, but dissolution does not skip the '
    'filings. Every outstanding year has to be filed before a clearance '
    'certificate is issued, and a final T2 is due within six months of '
    'dissolution.'),
   ('What about my GST/HST number?',
    'It files on its own schedule, separately from the T2, and keeps filing '
    'at nil until the account is closed on Form RC145. An open GST/HST '
    'account with no returns filed draws its own follow-up.'),
   ('I had a payroll account for myself. Does that matter?',
    'It matters for payroll, not for the T2. A payroll account stays open '
    'until it is closed and expects filings even where no wages were paid. '
    'The nil T2 does not close it.'),
   ('Can I file four years at once?',
    'Yes, and most consultants do. They are filed oldest first so balances '
    'carry forward correctly, with a separate T183CORP for each year.'),
   ('My laptop is still on the books. Does that stop the year being nil?',
    'No, as long as nothing was bought, sold or written down. Owning an asset '
    'is not activity. Claiming capital cost allowance on it would be, so none '
    'is claimed in a nil year.'),
   ('I invoiced in December and got paid in February. Which year is it?',
    'The year it was earned, which for most consulting corporations is the '
    'year the work was done and invoiced. That year is not nil, and the one '
    'the money landed in may well be.'),
   ('Does the CRA treat a dormant corporation differently?',
    'Only in what the return contains. The deadline, the schedules and the '
    'electronic filing requirement are the same as for any other corporation.'),
   ('What happens if I keep ignoring it?',
    'The years stay open indefinitely. The Canada Revenue Agency can issue a '
    'demand to file and then assess the corporation arbitrarily on figures of '
    'its own, which then has to be undone with the real return.'),
  ],
 },


 'shelf-corporations': {
  'name':   'Shelf Corporations',
  'short':  'shelf corporation',
  'plural': 'shelf corporations',
  'kw':     'shelf corporation tax return canada',
  'title':  'Shelf Corporation Tax Return Canada | Nil T2 Filing',
  'desc':   'A shelf corporation that has never traded still owes a T2 for '
            'every year since incorporation. What it files, and what the '
            'catch-up costs.',

  'h1':   'Nil T2 Filing for Shelf Corporations',
  'lede': 'A corporation that was incorporated and then left on the shelf '
          'owes a return for every year since. Each of those years is '
          '$300.00 plus HST per tax year.',

  'intro_h': 'The Corporation That Never Started',
  'intro': (
    'A shelf corporation is one that exists on paper and has never done '
    'anything. Some are incorporated to reserve a name, some to have an '
    'incorporation date ready for a bank or a tender, some because a plan '
    'changed the week after the articles were filed. The common thread is '
    'that there is no first transaction to point at.',
    'That makes shelf corporations the clearest nil case there is, and the '
    'one with the most years outstanding. The obligation starts at '
    'incorporation, not at first revenue, so a corporation registered in 2019 '
    'and never used owes seven returns and has never filed one. Each is a '
    'separate T2 at $300.00 plus HST per tax year, and the first of them '
    'carries Schedule 24.'),

  'notnil_h': 'When a Shelf Corporation Stops Being Nil',
  'notnil_boxes': [
    ('The Bank Account Opened',
     'An account opened in the corporation name that earns any interest puts '
     'income in the year. The year is not nil.'),
    ('The First Invoice Went Out',
     'One invoice ends the shelf period. From that tax year the corporation '
     'is trading and files an ordinary T2.'),
    ('An Asset Was Transferred In',
     'Property rolled into the corporation, often on a section 85 transfer, '
     'is a transaction with its own reporting.'),
    ('Incorporation Costs Were Claimed',
     'The registration fee and legal costs are expenses. Claiming them makes '
     'that year active rather than nil.'),
  ],
  'notnil_text': (
    'The usual complication is the incorporation year itself. Articles, name '
    'search and registry fees were paid by somebody, and where the '
    'corporation claimed them, its first year is an expense year with a loss '
    'rather than a nil year. Where the owner paid them personally and never '
    'put them through, the first year is nil like the rest.',
    'A first year with costs in it is prepared by Gondaliya CPA Professional '
    'Corporation at gondaliyacpa.ca for $350.00 plus HST per year, and the '
    'remaining shelf years are filed here. Mixing the two in one catch-up is '
    'normal and the price applies year by year.'),

  'sched_h': 'Which T2 Schedules a Shelf Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Depends on share capital',
     'A corporation with issued shares has share capital to report even where '
     'nothing was paid for them. A nominal balance still puts figures on the '
     'schedule.'),
    ('Schedule 125', 'Income statement information', 'With Schedule 100',
     'Reports nil revenue and nil expenses. Filed whenever Schedule 100 is.'),
    ('Schedule 141', 'Notes checklist', 'With Schedule 100',
     'Accompanies the other two and records who prepared the figures.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'The subscriber who took the first share is a shareholder from day one '
     'and is listed, even on a corporation that never traded.'),
    ('Schedule 24', 'First-time filer information', 'Required, once',
     'This is the schedule that matters most for a shelf corporation. It goes '
     'with the earliest outstanding year, not the most recent.'),
    ('Schedule 8', 'Capital cost allowance', 'Almost never',
     'A corporation that never started owns no depreciable property, so '
     'Schedule 8 does not arise.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, applied to a corporation with no '
                'transactions since incorporation. Last reviewed November 19, '
                '2026.',
  'sched_boxes': [
    ('Schedule 24 Goes on the Oldest Year',
     'Filing the recent years first and the oldest last puts Schedule 24 in '
     'the wrong return. Order matters here more than anywhere.'),
    ('Share Capital Is Still a Balance',
     'One share issued for one dollar is a balance sheet. That is usually '
     'what makes the GIFI schedules required.'),
    ('The Count Starts at Incorporation',
     'Not at first revenue, and not at the date the owner meant to start. '
     'The registry date sets the first tax year.'),
  ],
  'chk_yes': [
    'No invoice has ever been raised in the corporation name',
    'No bank account was opened, or one was opened and never used',
    'No asset was transferred into the corporation',
    'Incorporation costs were paid personally and never claimed',
    'No director or shareholder was paid anything',
  ],
  'chk_no': [
    'A business account paid interest, however little',
    'A first invoice was issued, even if it was never paid',
    'Registration or legal costs were claimed by the corporation',
    'Property was rolled in, on a section 85 transfer or otherwise',
    'A government rebate or credit was received',
  ],
  'chk_both': [
    'A T2 for every year since the incorporation date',
    'Schedule 24 with the earliest outstanding return',
    'Schedule 50 naming the subscriber who holds the shares',
    'The annual return to the registry, which is not the T2',
    'Dissolution, if the corporation is never going to be used',
  ],

  'why_h': 'Why Shelf Corporations Use This Service',
  'why': [
    ('Built for Long Catch-Ups',
     'Six or eight outstanding years is the normal case here, not the '
     'exception, and the price is the same for each one.'),
    ('Nothing to Reconstruct',
     'A corporation that never traded has no books to rebuild, so the '
     'catch-up is paperwork rather than forensics.'),
    ('Schedule 24 in the Right Year',
     'The first return is identified from the registry date, so the '
     'first-time filer schedule lands where it belongs.'),
    ('Dissolution-Ready at the End',
     'Once the years are filed the corporation can be dissolved without an '
     'unfiled year blocking the clearance certificate.'),
  ],
  'strip': [
    ('Count From the Registry Date',
     'The first tax year starts at incorporation, whatever the owner '
     'intended.'),
    ('Oldest Year First, Always',
     'Schedule 24 belongs with the earliest return, so the order is not '
     'optional.'),
    ('One Signature Per Year',
     'Eight outstanding years means eight T183CORP forms, all signable in '
     'one sitting.'),
  ],

  'svc_h': 'What a Shelf Corporation Usually Needs Next',
  'proc_h': 'How a Shelf Corporation Catches Up',
  'proc_lede': 'Four steps from the filing form, however many years are '
               'outstanding.',
  'proc_note': 'A shelf corporation almost always runs the full sequence:',
  'steps': [
    ('Fix the Incorporation Date',
     'The registry date sets the first tax year and therefore how many '
     'returns are owed.'),
    ('Confirm the Year-End',
     'The fiscal year-end the Canada Revenue Agency holds has to match the '
     'return, or the transmission is rejected.'),
    ('Prepare Every Year in Order',
     'Oldest first, with Schedule 24 on the earliest and the GIFI schedules '
     'where share capital requires them.'),
    ('Sign and Transmit Each One',
     'One T183CORP per tax year. Each CRA confirmation is emailed within 3 '
     'business days.'),
  ],

  'price_h': 'What Catching Up a Shelf Corporation Costs',
  'price_eyebrow': 'Per Tax Year, However Many',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year, so six outstanding '
    'years is six times that and nothing else. The fee covers the T2, the '
    'GIFI schedules where required, Schedule 50, Schedule 24 on the first '
    'return, the T183CORP package with secure e-signing, CPA review before '
    'transmission, electronic transmission by a registered EFILE electronic '
    'filer, one corrected transmission where the Agency rejects the first, '
    'and the CRA confirmation emailed within 3 business days. A year in '
    'which the corporation started trading is $350.00 plus HST per year at '
    'gondaliyacpa.ca.'),

  'geo_h': 'Shelf Corporation Filing Across Canada',
  'cta_h': 'File Every Year Since Incorporation',

  'faq': [
   ('My corporation has never done anything. Do I owe returns?',
    'Yes, one for every tax year since the incorporation date. The obligation '
    'starts when the corporation comes into existence, not when it first '
    'earns anything.'),
   ('How many years back do I have to go?',
    'All of them. An unfiled year does not expire, so a corporation '
    'incorporated in 2019 and never used owes every year from its first tax '
    'year to the most recent one.'),
   ('What is Schedule 24 and why does it matter here?',
    'It is the first-time filer schedule, and it goes with the first T2 after '
    'incorporation. For a shelf corporation that is the oldest outstanding '
    'year, which is why the returns are filed in order rather than newest '
    'first.'),
   ('I never opened a bank account. Does that simplify it?',
    'It helps. With no account there is no interest and no movement, which is '
    'the cleanest nil year there is. Share capital on the books may still put '
    'figures on the GIFI schedules.'),
   ('Who paid the incorporation fee changes things?',
    'It can. Where the corporation claimed the registration and legal costs, '
    'that year has expenses and is not nil. Where the owner paid personally '
    'and never charged them through, the year stays nil.'),
   ('Can I just dissolve it and forget the returns?',
    'No. A clearance certificate will not be issued while a year is unfiled, '
    'and dissolution adds a final T2 due within six months. Filing first is '
    'what makes dissolution possible.'),
   ('Does an unused corporation still need an annual return?',
    'Yes, and it is a different filing from the T2. The federal annual return '
    'and the provincial equivalents are registry filings and are not included '
    'in this fee.'),
   ('What if I want to start using the corporation now?',
    'Then the shelf years are filed as nil and the year trading begins is an '
    'ordinary T2. Bringing the back years current first is what keeps the '
    'account clean.'),
   ('Will the CRA have assessed it already?',
    'It may have. A demand to file followed by an arbitrary assessment is '
    'common on long-unfiled corporations, and the real return is what '
    'replaces the figures the Agency invented.'),
   ('Is a numbered corporation the same thing?',
    'Often, since many shelf corporations are never named. The number is the '
    'legal name and the return carries it exactly as the registry holds it.'),
  ],
 },


 'inactive-trucking-corporations': {
  'name':   'Inactive Trucking Corporations',
  'short':  'inactive trucking corporation',
  'plural': 'inactive trucking corporations',
  'kw':     'inactive trucking corporation t2 filing',
  'title':  'Inactive Trucking Corporation T2 Filing | Nil Returns',
  'desc':   'An owner-operator corporation that parked the truck still files '
            'a T2. Why selling the truck ends the nil year, and what the '
            'filing costs.',

  'h1':   'Nil T2 Filing for Inactive Trucking Corporations',
  'lede': 'The truck is parked, the authority is dormant and the corporation '
          'is still registered. A year with no loads and no disposals is nil, '
          'at $300.00 plus HST per tax year.',

  'intro_h': 'The Owner-Operator Corporation That Stopped Hauling',
  'intro': (
    'Owner-operators incorporate because the carriers they haul for ask them '
    'to. When the driving stops, for a back injury, a licence issue, a move '
    'to company driving or simply a market that turned, the corporation '
    'rarely gets wound up. It sits with a business number, maybe a fuel tax '
    'account, and a truck that may or may not still be in the yard.',
    'The return is due for every one of those years. What decides whether a '
    'year is nil is not whether the truck moved but whether anything was '
    'bought, sold, claimed or earned. A year with no loads, no expenses '
    'claimed and the truck sitting exactly where it was is a nil year at '
    '$300.00 plus HST per tax year.'),

  'notnil_h': 'When an Inactive Trucking Corporation Is Not Nil',
  'notnil_boxes': [
    ('The Truck Was Sold',
     'A disposal is the single most common thing that ends a nil run. Selling '
     'the tractor or a trailer triggers recapture or a terminal loss.'),
    ('A Load Was Hauled',
     'One settlement from a carrier, even a part month at the start of the '
     'year, is revenue. The year is not nil.'),
    ('Plates, Insurance or Storage Were Paid',
     'Keeping a truck insured or stored costs money, and a claimed cost makes '
     'the year active with a loss to report.'),
    ('A Rebate or Refund Arrived',
     'A fuel tax refund, an insurance rebate or a returned deposit is income '
     'to the corporation in the year it is received.'),
  ],
  'notnil_text': (
    'Trucking corporations differ from most dormant corporations because they '
    'usually own something substantial. A tractor sitting in the yard is '
    'depreciable property, and the year it is sold is never nil: the proceeds '
    'are measured against the undepreciated balance and the difference is '
    'recapture or a terminal loss, either of which has to be reported.',
    'That year is prepared by Gondaliya CPA Professional Corporation at '
    'gondaliyacpa.ca for $350.00 plus HST per year. The quiet years either '
    'side of it, where the truck simply sat, are filed here.'),

  'sched_h': 'Which T2 Schedules an Inactive Trucking Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'A truck on the books is an asset, and any loan against it is a '
     'liability. There is always a balance sheet to report.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Reports nil revenue and nil expenses for a year with no hauling and '
     'nothing claimed.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Accompanies Schedules 100 and 125 and records who prepared the '
     'financial information.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Owner-operator corporations are usually held by one person, sometimes '
     'with a spouse. Anyone at 10% or more is listed.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the first T2 after incorporation and not again.'),
    ('Schedule 8', 'Capital cost allowance', 'Required while the truck is owned',
     'This is the schedule that matters here. It carries the undepreciated '
     'balance forward year to year, which is what the eventual sale is '
     'measured against.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, applied to an owner-operator '
                'corporation holding depreciable property and hauling '
                'nothing. Last reviewed November 19, 2026.',
  'sched_boxes': [
    ('Schedule 8 Runs Even at Nil',
     'The undepreciated balance has to keep moving forward correctly, or the '
     'gain or loss on the eventual sale is wrong.'),
    ('Claiming No Capital Cost Allowance Is Deliberate',
     'A dormant year usually claims none, which keeps the balance intact for '
     'the year the truck is sold or the hauling resumes.'),
    ('Fuel Tax Accounts Are Separate',
     'An IFTA or provincial fuel tax account files on its own schedule and is '
     'not closed by the T2.'),
  ],
  'chk_yes': [
    'No load was hauled and no settlement was received in the tax year',
    'The truck and any trailer stayed on the books, unsold',
    'No plates, insurance, storage or repair cost was claimed',
    'No capital cost allowance was claimed for the year',
    'No driver or owner was paid out of the corporation',
  ],
  'chk_no': [
    'The tractor, a trailer or any equipment was sold or traded',
    'Any carrier settlement arrived, even for a part year',
    'Insurance, storage or plate costs were charged to the corporation',
    'A fuel tax refund or insurance rebate was received',
    'The corporation paid a wage, a dividend or a draw',
  ],
  'chk_both': [
    'The T2 return, for every year until dissolution',
    'A T183CORP signed by an authorised signing officer, per tax year',
    'Schedule 8, carrying the undepreciated balance on the truck forward',
    'Any open fuel tax or GST/HST account, on its own schedule',
    'The provincial or federal annual return, a separate registry filing',
  ],

  'why_h': 'Why Inactive Trucking Corporations Use This Service',
  'why': [
    ('The Disposal Test Comes First',
     'The year is checked for a sale or trade before anything is charged, '
     'because that is what usually takes a trucking year out of nil.'),
    ('Schedule 8 Kept Straight',
     'The undepreciated balance carries forward correctly, so the figures are '
     'right when the truck is eventually sold.'),
    ('One Price While the Truck Sits',
     'Every year the equipment simply sits is $300.00 plus HST, with no '
     'hourly billing.'),
    ('Reviewed by a CPA',
     'A CPA Ontario member reviews the return before it is transmitted '
     'electronically.'),
  ],
  'strip': [
    ('A Parked Truck Is Not a Disposal',
     'Owning equipment is not activity. Selling it is.'),
    ('Years Go in Order',
     'Oldest first, so the undepreciated balance carries forward correctly.'),
    ('Signed Online',
     'One T183CORP per tax year, signed through a secure portal.'),
  ],

  'svc_h': 'What an Inactive Trucking Corporation Usually Needs Next',
  'proc_h': 'How an Inactive Trucking Corporation Files',
  'proc_lede': 'Four steps from the filing form, with the disposal check '
               'first.',
  'proc_note': 'The sequence holds whether one year is open or five:',
  'steps': [
    ('Check for a Disposal',
     'A truck, trailer or piece of equipment sold in the year takes it out of '
     'nil and into an ordinary return.'),
    ('Match the Year-End to the CRA Record',
     'A year-end that differs from the one the Agency holds rejects the '
     'transmission.'),
    ('Prepare the Return and Schedule 8',
     'The T2 with its schedules, carrying the undepreciated capital cost '
     'forward unchanged where no allowance is claimed.'),
    ('Sign and Transmit',
     'One T183CORP per tax year. The CRA confirmation is emailed within 3 '
     'business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for an Inactive Trucking Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year. The fee covers the T2, '
    'the GIFI schedules, Schedule 50, Schedule 8 carrying the undepreciated '
    'balance forward, Schedule 24 on a first return, the T183CORP package '
    'with secure e-signing, CPA review before transmission, electronic '
    'transmission by a registered EFILE electronic filer, one corrected '
    'transmission where the Agency rejects the first, and the CRA '
    'confirmation emailed within 3 business days. The year the truck is sold '
    'is $350.00 plus HST per year at gondaliyacpa.ca.'),

  'geo_h': 'Trucking Corporation Filing Across Canada',
  'cta_h': 'File the Years the Truck Sat Still',

  'faq': [
   ('My truck has been parked for two years. Are those years nil?',
    'They can be. A parked truck is not a transaction. What breaks the nil '
    'year is a sale, a load hauled, or a cost like insurance or storage '
    'claimed through the corporation.'),
   ('I sold the truck last year. Is that year nil?',
    'No. A disposal is measured against the undepreciated capital cost and '
    'produces recapture or a terminal loss, both of which have to be '
    'reported. That year is an ordinary T2.'),
   ('Do I claim capital cost allowance in a dormant year?',
    'Usually not. Claiming none keeps the undepreciated balance intact, which '
    'matters when the truck is eventually sold or the hauling starts again.'),
   ('What happens to my IFTA or fuel tax account?',
    'It is separate from the T2 and files on its own schedule. A nil T2 does '
    'not close it, and leaving it open with no filings draws its own '
    'follow-up.'),
   ('I kept the insurance running. Does that matter?',
    'If the corporation paid it and claimed it, yes, and the year is a loss '
    'year rather than nil. If the premium was paid personally and never '
    'charged through, the year can still be nil.'),
   ('Can I file three parked years at once?',
    'Yes. Each year is a separate T2 at $300.00 plus HST with its own '
    'T183CORP, filed oldest first so the capital cost balance carries forward '
    'correctly.'),
   ('I drove for a carrier as an employee instead. Does the corporation care?',
    'No. Personal employment income is yours, not the corporation\u2019s. The '
    'corporation files its own nil return for the years it did nothing.'),
   ('The truck is financed and I still make payments. Is the year nil?',
    'The loan balance sits on the balance sheet, which is reported. Principal '
    'payments are not an expense. Interest claimed through the corporation '
    'would make the year active.'),
   ('What if the CRA already assessed me?',
    'An arbitrary assessment after a demand to file is common. The real '
    'return is what replaces it, and the outstanding years still have to be '
    'filed to clear the account.'),
   ('I want to close the corporation. What comes first?',
    'Every outstanding year, then the final T2 within six months of '
    'dissolution. An unfiled year blocks the clearance certificate that '
    'dissolution needs.'),
  ],
 },


 'closed-restaurant-corporations': {
  'name':   'Closed Restaurant Corporations',
  'short':  'closed restaurant corporation',
  'plural': 'closed restaurant corporations',
  'kw':     'closed restaurant corporation tax return',
  'title':  'Closed Restaurant Corporation Tax Return | Nil T2',
  'desc':   'The restaurant shut but the corporation did not. Which years are '
            'nil, which are not, and how the filings clear the way to '
            'dissolve.',

  'h1':   'Nil T2 Filing for Closed Restaurant Corporations',
  'lede': 'Closing the doors does not close the corporation. The years after '
          'the last service still need returns, and a year with nothing left '
          'moving is $300.00 plus HST per tax year.',

  'intro_h': 'The Years Between Closing and Dissolving',
  'intro': (
    'A restaurant closing is rarely tidy. The lease ends or gets assigned, '
    'the equipment goes to an auctioneer or stays in a unit nobody has '
    'emptied, the staff are paid out, and the corporation that held it all '
    'is quietly left alone. Owners move on to the next thing and the entity '
    'stays on the registry, accumulating filing years nobody is watching.',
    'Those years matter, because the corporation cannot be dissolved while '
    'any of them is unfiled. The year the restaurant actually closed is '
    'almost never nil, since equipment is sold and accounts are settled. The '
    'years after it, once everything has gone, usually are, and each of those '
    'is $300.00 plus HST per tax year.'),

  'notnil_h': 'When a Closed Restaurant Corporation Is Not Nil',
  'notnil_boxes': [
    ('Equipment or Fixtures Were Sold',
     'An auction, a private sale or a transfer of the kitchen to the next '
     'tenant is a disposal with a gain or loss to report.'),
    ('The Lease Was Settled',
     'A returned deposit, an assignment payment or a negotiated exit from the '
     'landlord is money moving through the corporation.'),
    ('Gift Cards Were Redeemed',
     'Outstanding gift cards honoured elsewhere, or written off, change the '
     'liability on the books.'),
    ('A Licence Refund Arrived',
     'A refunded liquor, food premises or municipal licence fee is income in '
     'the year it is received.'),
  ],
  'notnil_text': (
    'The closing year is the complicated one and it is worth getting right. '
    'Equipment sold for less than its depreciated value produces a terminal '
    'loss, which is a deduction, and a corporation that simply stops filing '
    'never claims it. Staff final pay, the GST/HST on an asset sale and the '
    'lease settlement all land in that same year.',
    'That return is prepared by Gondaliya CPA Professional Corporation at '
    'gondaliyacpa.ca for $350.00 plus HST per year. The years afterwards, '
    'once the unit is empty and the accounts are still, are filed here as nil '
    'returns at $300.00 plus HST per tax year.'),

  'sched_h': 'Which T2 Schedules a Closed Restaurant Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'A closed restaurant usually still has something on the books: a '
     'shareholder loan, an unpaid supplier, or share capital.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Reports nil revenue and nil expenses for a year after everything has '
     'been wound down.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Accompanies Schedules 100 and 125 and records who prepared the '
     'figures.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Restaurant corporations often have two or three shareholders. Each at '
     '10% or more is listed, including silent partners.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the first T2 after incorporation, which for most closed '
     'restaurants is years in the past.'),
    ('Schedule 8', 'Capital cost allowance', 'Until the equipment is gone',
     'Kitchen equipment and leaseholds are depreciable property. Once '
     'everything is disposed of there is nothing left to carry.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, applied to a corporation whose '
                'restaurant has closed and whose assets have been disposed '
                'of. Last reviewed November 19, 2026.',
  'sched_boxes': [
    ('A Terminal Loss Is Worth Claiming',
     'Kitchen equipment usually sells below its depreciated value. That '
     'difference is a deduction in the closing year.'),
    ('Shareholder Loans Outlive the Restaurant',
     'A loan owed to or from an owner stays on the balance sheet until it is '
     'repaid or written off.'),
    ('GST/HST and Payroll Close Separately',
     'Both accounts stay open until they are closed on their own forms. The '
     'T2 does not touch either.'),
  ],
  'chk_yes': [
    'No sales were made and no service was run in the tax year',
    'No equipment, fixtures or leaseholds were sold or transferred',
    'No lease deposit, licence refund or rebate was received',
    'No supplier, staff or rent cost was claimed by the corporation',
    'No shareholder loan was repaid or written off in the year',
  ],
  'chk_no': [
    'Kitchen equipment or fixtures were auctioned, sold or handed over',
    'The lease was assigned, surrendered or settled with the landlord',
    'A liquor, food premises or municipal licence fee was refunded',
    'Outstanding gift cards were redeemed or written off',
    'Any staff payment or final payroll ran in the year',
  ],
  'chk_both': [
    'A T2 for every year until the corporation is dissolved',
    'A T183CORP signed by an authorised signing officer, per tax year',
    'The GST/HST account, closed on Form RC145 rather than abandoned',
    'The payroll account, which expects filings until it is closed',
    'The clearance certificate, which no unfiled year will allow',
  ],

  'why_h': 'Why Closed Restaurant Corporations Use This Service',
  'why': [
    ('Aimed at the Years After Closing',
     'The quiet years between the last service and dissolution are exactly '
     'what this service is for.'),
    ('Dissolution Is the Point',
     'Filing the outstanding years is what clears the way for a clearance '
     'certificate and a wind-up.'),
    ('One Price Per Year',
     'Three years sitting empty is three times $300.00 plus HST, with no '
     'hourly billing.'),
    ('The Closing Year Goes Elsewhere',
     'A year with an equipment sale in it is sent to the right service '
     'rather than filed as nil.'),
  ],
  'strip': [
    ('Closed Is Not Dissolved',
     'The obligation runs until the registry says the corporation is gone.'),
    ('Oldest Year First',
     'Returns are filed in order so balances carry forward correctly.'),
    ('Nothing to Post',
     'Each T183CORP is signed electronically through a secure portal.'),
  ],

  'svc_h': 'What a Closed Restaurant Corporation Usually Needs Next',
  'proc_h': 'How a Closed Restaurant Corporation Files',
  'proc_lede': 'Four steps from the filing form, with the closing year '
               'identified first.',
  'proc_note': 'Most closed restaurants run this in one sitting:',
  'steps': [
    ('Separate the Closing Year',
     'The year the equipment went and the lease ended is an ordinary return, '
     'not a nil one.'),
    ('Confirm the Year-End',
     'The fiscal year-end on record with the Canada Revenue Agency has to '
     'match, or the transmission is rejected.'),
    ('Prepare the Quiet Years',
     'The T2 with its schedules for each year after the unit was emptied.'),
    ('Sign and Transmit',
     'One T183CORP per tax year, signed online. The CRA confirmation is '
     'emailed within 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Closed Restaurant Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year. The fee covers the T2, '
    'the GIFI schedules where required, Schedule 50, Schedule 24 on a first '
    'return, the T183CORP package with secure e-signing, CPA review before '
    'transmission, electronic transmission by a registered EFILE electronic '
    'filer, one corrected transmission where the Agency rejects the first, '
    'and the CRA confirmation emailed within 3 business days. The closing '
    'year, with its equipment sale and lease settlement, is $350.00 plus HST '
    'per year at gondaliyacpa.ca.'),

  'geo_h': 'Closed Restaurant Filing Across Canada',
  'cta_h': 'Clear the Years and Close the Corporation',

  'faq': [
   ('The restaurant closed three years ago. What do I owe?',
    'A T2 for each of those three years and for every year since, until the '
    'corporation is dissolved. The closing year itself is usually an ordinary '
    'return rather than a nil one.'),
   ('We sold the kitchen equipment at auction. Is that year nil?',
    'No. A disposal produces a gain or, far more often with restaurant '
    'equipment, a terminal loss. That is a deduction worth claiming, and it '
    'makes the year an ordinary T2.'),
   ('Can I dissolve without filing the back years?',
    'No. A clearance certificate will not be issued while a year is '
    'outstanding, and dissolution adds a final T2 due within six months of '
    'the dissolution date.'),
   ('What happens to the GST/HST number?',
    'It stays open and expects returns until it is closed on Form RC145. '
    'Closing the restaurant does not close the account, and the T2 does not '
    'either.'),
   ('We still have a payroll account. Does it matter?',
    'Yes, separately. A payroll account expects filings until it is closed, '
    'even where no wages were paid after the closure.'),
   ('There is still a shareholder loan on the books. Is the year nil?',
    'It can be, as long as nothing was repaid or written off during the year. '
    'The balance is reported on Schedule 100, and a balance sitting still is '
    'not activity.'),
   ('The landlord returned our deposit. Which year does that hit?',
    'The year it was received. A returned deposit is money moving through the '
    'corporation, so that year is not nil.'),
   ('What about gift cards people never used?',
    'The outstanding balance is a liability. Writing it off or honouring it '
    'changes the books and takes that year out of nil.'),
   ('Can several partners sign, or just one?',
    'One authorised signing officer signs the T183CORP for each tax year. '
    'Every shareholder at 10% or more is still listed on Schedule 50.'),
   ('The CRA sent a demand to file. What now?',
    'File the outstanding years. A demand is usually followed by an arbitrary '
    'assessment on figures the Agency invents, and the real returns are what '
    'replace them.'),
  ],
 },



'medicine-professional-corporations': {
  'name':   'Medicine Professional Corporations',
  'short':  'medicine professional corporation',
  'plural': 'medicine professional corporations',
  'kw':     'nil t2 for medicine professional corporation',
  'title':  'Medicine Professional Corporation Nil T2 | Inactive Years',
  'desc':   'A physician professional corporation files for every year it '
            'exists. When a year with no billings is nil, and when a portfolio '
            'inside it is not.',

  'h1':   'Nil T2 Filing for Medicine Professional Corporations',
  'lede': 'A year with nothing billed through the corporation is still a tax '
          'year. Where nothing was earned and nothing was held, the return is '
          '$300.00 plus HST per tax year.',

  'intro_h': 'The Year a Physician Stops Billing Through the Corporation',
  'intro': (
    'Medicine professional corporations go quiet for ordinary reasons. A '
    'parental leave runs across a fiscal year. A fellowship abroad takes a '
    'physician off the provincial plan. A locum practice winds down into a '
    'salaried hospital appointment, and the billings that used to route '
    'through the corporation now land on a personal T4 instead.',
    'The corporation notices none of that. It holds a certificate of '
    'authorization from the provincial college, it keeps its own fiscal year '
    'end, and it owes a T2 for every one of those years. Where the '
    'corporation billed nothing, paid nobody and held nothing that earned, '
    'that is a nil year, filed here at $300.00 plus HST per tax year.'),

  'notnil_h': 'When a Medicine Professional Corporation Is Not Nil',
  'notnil_boxes': [
    ('A Portfolio Sits Inside the Corporation',
     'Interest, dividends or a realised gain on investments the corporation '
     'owns is income to it, whoever manages them.'),
    ('Billings Settled Late',
     'A year-end reconciliation from the provincial plan, or a shadow '
     'billing payment, counts in the year it arrives.'),
    ('A Family Shareholder Was Paid',
     'Salary or a dividend to a spouse or adult child holding non-voting '
     'shares is activity.'),
    ('The Practice Changed Hands',
     'Goodwill, a patient list or examination equipment transferred to a '
     'buyer is a disposal.'),
  ],
  'notnil_text': (
    'The portfolio is what catches physicians out. Retained earnings left '
    'inside a professional corporation are very often invested, and the '
    'moment those holdings pay interest or a dividend the corporation has '
    'income, even in a year its physician saw no patients through it. '
    'Passive investment income also carries treatment of its own, which a '
    'nil return does not provide.',
    'Such a year is an ordinary corporate return. Gondaliya CPA Professional '
    'Corporation takes it at gondaliyacpa.ca, where the fee is $350.00 plus '
    'HST per year. Only a year in which the corporation neither earned nor '
    'paid anything belongs on this page, at $300.00 plus HST per tax year.'),

  'sched_h': 'Which T2 Schedules a Medicine Professional Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Share capital and retained earnings from practising years stay on the '
     'balance sheet whether or not the year was active.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Reports nil professional income and nil expenses where no clinical '
     'work was billed through the corporation.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Travels with Schedules 100 and 125 and names whoever compiled them.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Medicine professional corporations commonly issue non-voting shares to '
     'a spouse or adult children. Every holder at 10% or more appears here.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Attached to the very first T2, filed after incorporation and the issue '
     'of the certificate of authorization.'),
    ('Schedule 8', 'Capital cost allowance', 'While equipment remains',
     'Examination equipment, office furniture and leasehold improvements are '
     'depreciable property until disposed of.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, applied to a professional corporation '
                'that billed nothing through itself in the tax year. Last '
                'reviewed November 19, 2026.',
  'sched_boxes': [
    ('Investment Income Ends a Nil Year',
     'One dividend or interest credit inside the corporation puts a figure on '
     'Schedule 125 and makes the year an ordinary return.'),
    ('The College Certificate Is Separate',
     'A certificate of authorization renews on the college cycle. The T2 does '
     'not renew it and the college does not file it.'),
    ('Retained Earnings Are Not Activity',
     'A balance carried forward from practising years sits on Schedule 100 '
     'without making the year active, provided it earned nothing.'),
  ],
  'chk_yes': [
    'Nothing was billed to the provincial plan through the corporation',
    'No private, insurance or third-party fee was invoiced by it',
    'No investment it owns paid interest, a dividend or a gain',
    'No salary or dividend went to any shareholder',
    'No equipment, goodwill or patient list was sold or transferred',
  ],
  'chk_no': [
    'A reconciliation or shadow billing payment arrived from the plan',
    'A portfolio inside the corporation paid interest, dividends or a gain',
    'A spouse or adult child shareholder drew salary or a dividend',
    'The practice, its goodwill or its patient list was sold',
    'The corporation paid rent, staff or an association fee',
  ],
  'chk_both': [
    'A T2 for every tax year the corporation exists',
    'A T183CORP signed by an authorised signing officer, per tax year',
    'Schedule 50, naming every shareholder at 10% or more',
    'The certificate of authorization, renewed with the college separately',
    'A record of what was billed, which decides the year either way',
  ],

  'why_h': 'Why Medicine Professional Corporations Use This Service',
  'why': [
    ('Built for the Years Off',
     'Leave, a fellowship or a salaried appointment leaves the corporation '
     'intact and owing returns. Those are the years this service covers.'),
    ('The Portfolio Test Comes First',
     'Every year is measured against investment income before anything is '
     'charged, since that is what usually ends a nil year here.'),
    ('A Flat Fee Per Year',
     'Each quiet year is $300.00 plus HST per tax year. No retainer, no '
     'hourly billing, no minimum engagement.'),
    ('Earning Years Are Referred On',
     'Where billings or portfolio income appear, the year goes to the full '
     'corporate service.'),
  ],
  'strip': [
    ('A Quiet Year Still Files',
     'The obligation follows the corporation, not the practice.'),
    ('Filed in Sequence',
     'Earlier years are transmitted before later ones so retained earnings '
     'reconcile.'),
    ('No Paper, No Courier',
     'T183CORP signatures are captured online through an access-controlled '
     'portal.'),
  ],

  'svc_h': 'What a Medicine Professional Corporation Usually Needs Next',
  'proc_h': 'How a Medicine Professional Corporation Files',
  'proc_lede': 'Four steps, taken from the filing form, with the investment '
               'test first.',
  'proc_note': 'Most physicians complete this between clinics:',
  'steps': [
    ('Test the Year for Income',
     'Billings, private fees and anything a portfolio inside the corporation '
     'paid are measured before the year is treated as nil.'),
    ('Agree the Fiscal Year End',
     'Professional corporations frequently run a non-calendar year end. It '
     'has to agree with the Agency record or the return will not transmit.'),
    ('Assemble the Return',
     'Schedules 100, 125, 141 and 50 go on the T2, with Schedule 24 added '
     'where this is the first one.'),
    ('Sign and File',
     'A T183CORP is signed for each year, the returns go across, and the CRA '
     'confirmation reaches you within 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Medicine Professional Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year. The fee covers the T2, '
    'the GIFI schedules where required, Schedule 50, Schedule 24 on a first '
    'return, the T183CORP package with secure e-signing, CPA review before '
    'transmission, electronic transmission by a registered EFILE electronic '
    'filer, one corrected transmission where the Agency rejects the first, '
    'and the CRA confirmation emailed within 3 business days. A year with '
    'billings or investment income inside the corporation is $350.00 plus HST '
    'per year at gondaliyacpa.ca.'),

  'geo_h': 'Professional Corporation Filing Across Canada',
  'cta_h': 'File the Quiet Years and Keep the Corporation Current',

  'faq': [
   ('I was on parental leave all year. Is the corporation nil?',
    'It can be, provided nothing was billed through it and nothing it owns '
    'earned. Leave interrupts the practice, not the filing obligation, so the '
    'T2 is still due.'),
   ('My corporation holds investments. Does that end the nil year?',
    'Yes, as soon as they pay. Interest, a dividend or a realised gain is '
    'income to the corporation, which makes the year a full T2 at $350.00 '
    'plus HST per year at gondaliyacpa.ca.'),
   ('I took a salaried hospital job. Do I still file?',
    'Yes, every year the corporation exists. Employment income is yours '
    'personally and has no bearing on the corporate return, which runs until '
    'the corporation is dissolved.'),
   ('Does the college certificate of authorization affect the T2?',
    'No. The certificate renews on the college cycle and the T2 runs on the '
    'fiscal year. Neither filing substitutes for the other.'),
   ('My spouse holds non-voting shares. Does that change anything?',
    'Only on Schedule 50, which names every shareholder at 10% or more. '
    'Holding shares is not activity. Being paid during the year is.'),
   ('What if I only did a few locum shifts, billed personally?',
    'Where the billings went to you rather than through the corporation, the '
    'corporate year can still be nil. What decides it is which entity earned, '
    'not which person worked.'),
   ('A plan reconciliation arrived two years after I stopped. Which year?',
    'The year of receipt. That year becomes an ordinary return, and the years '
    'on either side of it can still be nil.'),
   ('How many quiet years can be filed at once?',
    'As many as are outstanding. One T2 and one T183CORP per year, each at '
    '$300.00 plus HST per tax year, sent in date order from the oldest.'),
   ('Can I wind the corporation up instead of filing?',
    'Winding up does not replace the outstanding years. No clearance '
    'certificate is issued while a year is missing, and the wind-up itself '
    'adds a final T2 due six months after the dissolution date.'),
   ('Who signs when I am the only physician and shareholder?',
    'You do, as authorised signing officer, once per tax year. Several years '
    'can be signed in a single sitting.'),
  ],
 },

 'dormant-construction-corporations': {
  'name':   'Dormant Construction Corporations',
  'short':  'dormant construction corporation',
  'plural': 'dormant construction corporations',
  'kw':     'dormant construction corporation t2 return',
  'title':  'Dormant Construction Corporation T2 Return | Nil Filing',
  'desc':   'A trades corporation with no jobs in the year still files a T2. '
            'Which years are nil, why a released holdback is not, and what '
            'filing costs.',

  'h1':   'Nil T2 Filing for Dormant Construction Corporations',
  'lede': 'A season with no contracts is still a tax year. Where no work was '
          'invoiced and no holdback was released, the return is $300.00 plus '
          'HST per tax year.',

  'intro_h': 'The Trades Corporation That Stopped Taking Jobs',
  'intro': (
    'Construction corporations go dormant between phases of a working life. '
    'A contractor takes a payroll job with a larger builder. A partnership '
    'splits and one side keeps bidding while the other stops. A general '
    'contractor sells the trailer and the tools and never formally closes '
    'the entity that invoiced for them.',
    'The corporation carries on existing, and the Canada Revenue Agency '
    'expects a T2 for each year it does. A season with no contracts invoiced, '
    'no subcontractors paid and no holdback released is a nil year at $300.00 '
    'plus HST per tax year. The entity stays on the registry, ready to bid '
    'again, with its filing history unbroken.'),

  'notnil_h': 'When a Dormant Construction Corporation Is Not Nil',
  'notnil_boxes': [
    ('A Holdback Was Released',
     'Statutory holdback from a job finished years earlier counts as revenue '
     'the year the owner finally pays it out.'),
    ('Equipment or a Vehicle Was Sold',
     'A truck, an excavator, scaffolding or a trailer sold or traded is a '
     'disposal with a gain or a terminal loss.'),
    ('A Subcontractor Was Paid',
     'Any payment to a subcontractor is activity, and it brings a T5018 '
     'contract payment information return with it.'),
    ('A Deficiency Claim Was Settled',
     'Money paid or received over warranty work on a finished project moves '
     'through the corporation.'),
  ],
  'notnil_text': (
    'Holdbacks are the usual reason a season a contractor thought was empty '
    'turns out not to be. Statutory holdback on a substantial project can be '
    'released long after the last crew left the site, and it belongs to '
    'whichever year the cheque clears rather than the year the work was '
    'done.',
    'Any of those makes the year an ordinary corporate return, taken by '
    'Gondaliya CPA Professional Corporation at gondaliyacpa.ca for $350.00 '
    'plus HST per year. The empty seasons in between belong on this page at '
    '$300.00 plus HST per tax year.'),

  'sched_h': 'Which T2 Schedules a Dormant Construction Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'A dormant trades corporation usually still shows equipment, a '
     'shareholder loan or an unpaid supplier on its books.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Reports nil contract revenue and nil job costs across a season with no '
     'work invoiced.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Accompanies Schedules 100 and 125 and records who compiled the '
     'figures.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Trades corporations are often held by two or three partners, and each '
     'at 10% or more appears here.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Goes with the first T2 after incorporation, which for a long-dormant '
     'contractor is well in the past.'),
    ('Schedule 8', 'Capital cost allowance', 'While equipment is owned',
     'Trucks, excavators, trailers and tools stay depreciable property until '
     'sold or scrapped.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, applied to a construction corporation '
                'that invoiced no contracts in the tax year. Last reviewed '
                'November 19, 2026.',
  'sched_boxes': [
    ('A Released Holdback Is Revenue',
     'It belongs to the year of receipt, not the year the work finished, and '
     'it takes that year out of nil.'),
    ('T5018 Follows Subcontractor Payments',
     'Paying a subcontractor brings an information return of its own, due six '
     'months after the reporting period ends.'),
    ('Workers Compensation Reports Separately',
     'A provincial board account expects its own reporting until closed with '
     'the board. The T2 does not close it.'),
  ],
  'chk_yes': [
    'No contract, progress draw or change order was invoiced',
    'No holdback from any earlier project was released to the corporation',
    'No subcontractor, labourer or supplier was paid by it',
    'No truck, machine, trailer or tool was sold, traded or scrapped',
    'No warranty or deficiency claim was settled either way',
  ],
  'chk_no': [
    'A statutory holdback was released, however old the project',
    'Any subcontractor payment was made, which also brings a T5018',
    'Equipment or a vehicle was sold, traded in or written off',
    'A progress draw or final invoice went out on an old job',
    'A deficiency or warranty settlement moved money',
  ],
  'chk_both': [
    'A T2 for every tax year until the corporation is dissolved',
    'A T183CORP signed by an authorised signing officer, per tax year',
    'The GST/HST account, which expects returns until it is closed',
    'The workers compensation account, closed with the provincial board',
    'Schedule 8, for as long as any equipment is still owned',
  ],

  'why_h': 'Why Dormant Construction Corporations Use This Service',
  'why': [
    ('Built for Seasons With No Work',
     'A year between contracts is the kind of year this service files, and it '
     'keeps the entity ready to bid again.'),
    ('Holdbacks Are Settled First',
     'Every season is measured against released holdback before it is treated '
     'as nil, because that is the usual surprise.'),
    ('A Flat Fee Per Season',
     'Each dormant year is $300.00 plus HST per tax year. Four of them is '
     'four fees, with nothing billed by the hour.'),
    ('Working Years Are Referred On',
     'Invoicing, a disposal or subcontractor payments route the year to the '
     'full corporate service.'),
  ],
  'strip': [
    ('Dormant Is Not Closed',
     'The filing obligation runs until the registry says the corporation is '
     'gone.'),
    ('Earliest Season First',
     'Years are transmitted in sequence so capital cost allowance carries '
     'forward intact.'),
    ('Signed From the Truck',
     'T183CORP signatures are captured online, with no printing and no office '
     'visit.'),
  ],

  'svc_h': 'What a Dormant Construction Corporation Usually Needs Next',
  'proc_h': 'How a Dormant Construction Corporation Files',
  'proc_lede': 'Four steps from the filing form. The holdback question is '
               'settled before anything else.',
  'proc_note': 'Most contractors finish this from a phone on a lunch break:',
  'steps': [
    ('Check for Released Holdback',
     'Holdback paid out during the year, from any project however old, takes '
     'that year out of nil.'),
    ('Match the Year-End on File',
     'The fiscal year-end the Agency holds has to agree with the return, or '
     'the transmission comes back rejected.'),
    ('Prepare the Return and Schedules',
     'The T2 with Schedules 100, 125, 141 and 50, plus Schedule 8 while '
     'equipment is still owned.'),
    ('Sign Each Year and File',
     'A T183CORP goes with every year. Once transmitted, the CRA confirmation '
     'arrives by email inside 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Dormant Construction Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year. The fee covers the T2, '
    'the GIFI schedules where required, Schedule 50, Schedule 24 on a first '
    'return, the T183CORP package with secure e-signing, CPA review before '
    'transmission, electronic transmission by a registered EFILE electronic '
    'filer, one corrected transmission where the Agency rejects the first, '
    'and the CRA confirmation emailed within 3 business days. A year with a '
    'released holdback, an equipment sale or subcontractor payments is '
    '$350.00 plus HST per year at gondaliyacpa.ca.'),

  'geo_h': 'Construction Corporation Filing Across Canada',
  'cta_h': 'File the Dormant Seasons and Keep the Corporation Bid-Ready',

  'faq': [
   ('I took a payroll job and parked the company. Does it still file?',
    'Yes, every year it exists. Your T4 income is personal. The corporation '
    'owes its own T2 until dissolution, and a season with no contracts in it '
    'is nil.'),
   ('A holdback from an old job was finally released. Is that year nil?',
    'No. Released holdback is contract revenue in the year of receipt, '
    'whatever year the work was done, which makes that one an ordinary '
    'return.'),
   ('I sold the truck and the trailer. What does that do?',
    'It is a disposal. Against the depreciated value it produces either a '
    'recapture or a terminal loss, the year stops being nil, and the figures '
    'belong on Schedule 8.'),
   ('I paid one subcontractor for a small favour. Does that matter?',
    'Twice over. The payment is activity, so the year is not nil, and it also '
    'brings a T5018 contract payment information return of its own.'),
   ('Does my workers compensation account close with the T2?',
    'No. A provincial board account keeps expecting its own reporting until '
    'you close it with the board. The corporate return has no effect on it.'),
   ('What about the GST/HST number on a dormant company?',
    'That account is separate and keeps expecting returns until it is closed '
    'on Form RC145. A dormant corporation with an open number still has '
    'obligations of its own.'),
   ('There is still a shareholder loan on the books. Is the year nil?',
    'Usually yes. A loan balance that neither grew nor shrank is a balance '
    'sheet figure on Schedule 100, not activity. An advance or a repayment '
    'during the year is.'),
   ('My partner and I each own half. Who signs?',
    'One authorised signing officer signs per tax year. Both of you still '
    'appear on Schedule 50 at 50% each.'),
   ('Can I keep the company dormant and bid again in a few years?',
    'Yes, and that is the usual reason to file rather than dissolve. An '
    'unbroken filing history is what keeps the entity usable for bonding and '
    'prequalification later.'),
   ('How far back can unfiled seasons be filed?',
    'As far back as they go. Each is its own T2 at $300.00 plus HST per tax '
    'year with its own T183CORP, transmitted earliest first so equipment '
    'balances reconcile.'),
  ],
 },

 'e-commerce-corporations': {
  'name':   'E-Commerce Corporations',
  'short':  'e-commerce corporation',
  'plural': 'e-commerce corporations',
  'kw':     'nil t2 for e-commerce corporation',
  'title':  'E-Commerce Corporation Nil T2 | Closed Online Stores',
  'desc':   'The store is switched off but the corporation is not. Which years '
            'are nil, why a processor payout is not, and what each year costs '
            'to file.',

  'h1':   'Nil T2 Filing for E-Commerce Corporations',
  'lede': 'Switching off a storefront does not end the corporation behind it. '
          'A year with nothing sold and nothing paid out is $300.00 plus HST '
          'per tax year.',

  'intro_h': 'The Storefront Went Dark, the Corporation Did Not',
  'intro': (
    'Online stores stop quietly. A seller account is deactivated, a '
    'subscription lapses, the last of the stock is cleared at cost, and the '
    'domain renews on its own for another year or two. Nothing is filed to '
    'mark the end, because shutting a storefront asks for no filing.',
    'The corporation that held the seller account remains registered, and it '
    'owes a T2 for every year it does. Where nothing sold, no processor paid '
    'out and no stock moved, that is a nil year at $300.00 plus HST per tax '
    'year.'),

  'notnil_h': 'When an E-Commerce Corporation Is Not Nil',
  'notnil_boxes': [
    ('A Processor Paid Out',
     'A residual transfer from a payment processor or a marketplace, months '
     'after the last order, counts in the year it lands.'),
    ('Remaining Stock Was Cleared',
     'Liquidating inventory, selling it to another seller or writing it off '
     'changes the books.'),
    ('A Refund or Chargeback Settled',
     'Money going back to a customer, or a chargeback resolved either way, '
     'moves through the corporation.'),
    ('The Store or Domain Was Sold',
     'Selling the brand, the domain, the customer list or the seller account '
     'is a disposal.'),
  ],
  'notnil_text': (
    'Payment processors are the usual complication. A balance can sit with a '
    'processor or a marketplace for months after the storefront goes dark, '
    'held back against refunds and chargebacks, and its release is revenue to '
    'the corporation in that year. A foreign currency balance converted on '
    'the way out behaves the same.',
    'Where a year holds one of those it stops being nil and becomes a full '
    'return. Gondaliya CPA Professional Corporation deals with it from '
    'gondaliyacpa.ca, charged at $350.00 plus HST per year. Anything '
    'quieter than that is priced on this page.'),

  'sched_h': 'Which T2 Schedules an E-Commerce Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Remaining stock, a processor balance or a shareholder loan sits on the '
     'balance sheet after the store closes.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Reports nil sales and nil cost of goods across a year in which no order '
     'shipped.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Sits alongside Schedules 100 and 125 and identifies the preparer.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'An online store often has two or three founders. Anyone holding 10% or '
     'more of the shares is named on it.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Attached to the very first T2 the corporation ever files, usually the '
     'year the seller account opened.'),
    ('Schedule 8', 'Capital cost allowance', 'While assets remain',
     'Photography gear, packing equipment and a purchased platform licence '
     'stay depreciable property until disposed of.'),
  ],
  'sched_note': 'Source: what the Canada Revenue Agency requires on a T2, '
                'read against a seller account that shipped nothing all '
                'year. Last reviewed November 19, 2026.',
  'sched_boxes': [
    ('A Processor Balance Is Still Money',
     'Funds held by a processor belong to the corporation and show on '
     'Schedule 100 until released.'),
    ('Unsold Stock Stays on the Books',
     'Inventory nobody has cleared is an asset. Holding it is not activity. '
     'Selling or writing it off is.'),
    ('Foreign Sales Do Not Change the T2',
     'Where the buyers were does not decide the return. What the corporation '
     'earned decides it.'),
  ],
  'chk_yes': [
    'No order was sold, shipped or fulfilled',
    'No payment processor or marketplace released funds to the corporation',
    'No remaining stock was sold, liquidated or written off',
    'No refund, chargeback or dispute was settled',
    'The store, domain, brand or seller account was not sold',
  ],
  'chk_no': [
    'A processor or marketplace transferred a residual balance out',
    'Leftover inventory was cleared, sold on or written down',
    'A customer refund or a chargeback was settled either way',
    'The domain, brand or customer list changed hands',
    'An advertising rebate or platform credit reached the corporation',
  ],
  'chk_both': [
    'One T2 per tax year, right up to the day the corporation is struck',
    'A signed T183CORP covering each of those years',
    'A closed GST/HST number, which shutting the storefront did not close',
    'Any processor balance, shown on Schedule 100 until it is released',
    'Proof of the last shipped order, which fixes the first dark year',
  ],

  'why_h': 'Why E-Commerce Corporations Use This Service',
  'why': [
    ('Built for Stores That Stopped',
     'The years between the last order and dissolution are what this service '
     'covers.'),
    ('Payout Channels Are Read First',
     'Every year is measured against marketplace and processor transfers '
     'before it is treated as nil.'),
    ('A Flat Fee Per Year',
     'Each dark year costs $300.00 plus HST per tax year. Nothing is billed '
     'by the hour and nothing is held on retainer.'),
    ('Trading Years Are Referred On',
     'Sales, a payout or a stock clearance route the year to the full '
     'corporate service.'),
  ],
  'strip': [
    ('Dark Is Not Dissolved',
     'Until the registry removes the corporation, the returns keep coming '
     'due.'),
    ('Oldest Dark Year Leads',
     'Filing in date order keeps stock and held balances reconciling across '
     'the run.'),
    ('Filed From Anywhere',
     'T183CORP signatures are captured online, wherever the seller happens to '
     'be.'),
  ],

  'svc_h': 'What an E-Commerce Corporation Usually Needs Next',
  'proc_h': 'How an E-Commerce Corporation Files',
  'proc_lede': 'The filing form runs in four steps, and reading the payout '
               'channels is the first of them.',
  'proc_note': 'Most sellers finish this in a single sitting:',
  'steps': [
    ('Read Every Payout Channel',
     'Processor, marketplace and advertising accounts are read for transfers '
     'before the year is treated as nil.'),
    ('Match the Fiscal Year End',
     'A year end that disagrees with the Agency record will bounce the '
     'transmission straight back.'),
    ('Build the Return',
     'A T2 carrying Schedules 100, 125, 141 and 50, together with any stock '
     'or processor balance still outstanding.'),
    ('Sign and Send',
     'One signature per year on the T183CORP. Confirmation from the Agency '
     'reaches your inbox inside 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for an E-Commerce Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year. The fee covers the T2, '
    'the GIFI schedules where required, Schedule 50, Schedule 24 on a first '
    'return, the T183CORP package with secure e-signing, CPA review before '
    'transmission, electronic transmission by a registered EFILE electronic '
    'filer, one corrected transmission where the Agency rejects the first, '
    'and the CRA confirmation emailed within 3 business days. A year with '
    'sales, a processor payout or a stock clearance is $350.00 plus HST per '
    'year at gondaliyacpa.ca.'),

  'geo_h': 'Online Store Corporation Filing Across Canada',
  'cta_h': 'File the Dark Years and Close the Store Properly',

  'faq': [
   ('My Shopify store closed two years ago. What do I owe?',
    'A T2 for each of those years and for every year since, until the '
    'corporation is dissolved. A year with nothing sold and nothing paid out '
    'is nil at $300.00 plus HST per tax year.'),
   ('Stripe released a held balance last year. Is that year nil?',
    'No. A released balance is the corporation receiving its own money as '
    'revenue in that year, which makes it an ordinary return.'),
   ('I still have stock in a spare room. Does that stop a nil year?',
    'No. Holding inventory is not activity. It sits on Schedule 100 as an '
    'asset. Selling it, clearing it or writing it off is what ends the nil '
    'year.'),
   ('All my customers were in the United States. Does that change the T2?',
    'No. Where the buyers were does not decide the corporate return. A '
    'Canadian corporation files a T2 on what it earned, wherever it earned '
    'it.'),
   ('The domain renews automatically. Does that count as activity?',
    'A cost the corporation pays is activity and takes the year out of nil. A '
    'renewal a shareholder pays personally does not.'),
   ('What happens to the GST/HST number?',
    'It is a separate account with obligations of its own, and Form RC145 '
    'is what closes it. Taking the storefront offline does nothing to it.'),
   ('I sold the brand and the customer list. Which year is that?',
    'The year of the sale, which is a disposal and so a full return. The '
    'years on either side of it can still be nil.'),
   ('There are two of us who founded it. Who signs?',
    'One authorised signing officer signs per tax year. Both founders still '
    'appear on Schedule 50 where each holds 10% or more.'),
   ('Can I dissolve without filing the dark years?',
    'Dissolution does not clear them. No clearance certificate is issued '
    'while a year is missing, and winding up adds one more T2, due six months '
    'after the dissolution date.'),
   ('How many unfiled years can go in at once?',
    'There is no limit. Every outstanding year gets a T2 of its own and a '
    'T183CORP of its own, priced at $300.00 plus HST per tax year, and they '
    'go across oldest to newest.'),
  ],
 },

}
