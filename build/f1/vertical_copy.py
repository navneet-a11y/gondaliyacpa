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

}
