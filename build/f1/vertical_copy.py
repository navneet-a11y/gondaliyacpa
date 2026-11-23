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
  'intro_h': 'Flat-Fee Nil T2 Filing for Numbered Holding Corporations',
  'intro': (
    'Filing for a numbered holding corporation can feel pointless, '
    'especially when the entity has a number instead of a name, holds '
    'something rather than trades, and did nothing at all last year. A '
    'holding or investment corporation is not nil in any year it earns, '
    'so the year is tested first. Where it genuinely earned nothing we '
    'file it at $300.00 plus HST per tax year, for owners who want the '
    'years closed off and the record clean.',
    'Whether the corporation holds shares in your operating company, a '
    'parcel of land, a portfolio, or nothing while you decide what comes '
    'next, we test the year against dividends, interest, rent and '
    'dispositions, prepare the T2 with its GIFI schedules and Schedule '
    '50, and transmit it as a registered EFILE electronic filer. The CRA '
    'confirmation reaches you within 3 business days.'),
  'notnil_h': 'What an Unfiled Year Costs a Numbered Holding Corporation',
  'notnil_boxes': [
    ('The Year Never Closes Itself',
     'Doing nothing does not end a tax year. Only the filed return ends '
     'it.'),
    ('A Demand Can Name Several Years',
     'The Agency can require them in writing, and a holdco with a long '
     'gap is usually asked for all of them at once.'),
    ('The Group Below It Is Affected',
     'A holdco with missing years complicates a sale, a refinancing or a '
     'reorganisation of the companies under it.'),
    ('Unwinding the Structure Waits',
     'No clearance certificate is issued while a year is outstanding, so '
     'the holdco cannot be collapsed.'),
  ],
  'notnil_text': (
    'A numbered holding corporation is the easiest entity in a group to '
    'forget, because nothing visibly happens inside it. It is also the '
    'first one a lender, a buyer or a new accountant pulls the filings '
    'for.',
    'Each quiet year is $300.00 plus HST per tax year, filed oldest first '
    'so the balance sheet carries forward, with one T183CORP signed '
    'online for each of them.'),
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

  'intro_h': 'Flat-Fee Nil T2 Filing for Dormant Consulting Corporations',
  'intro': (
    'Filing for a consulting corporation you stopped using can feel like '
    'paperwork for nothing, especially when no invoices went out, the '
    'business number is still open, and the obligation did not stop when '
    'the engagements did. We file nil T2 returns made for quiet years, '
    'for consultants who want the backlog cleared without an engagement '
    'letter or an hourly bill, at $300.00 plus HST per tax year.',
    'Whether you took a salaried job, went on leave, moved abroad, or '
    'stopped looking for the next contract, we check the year '
    'against invoices raised, expenses claimed and retainers held, '
    'prepare the return with its schedules, and have you sign one '
    'T183CORP for each year online. Nothing is printed and nothing is '
    'posted.'),
  'notnil_h': 'What an Unfiled Year Costs a Dormant Consulting Corporation',
  'notnil_boxes': [
    ('The Year Stays Open',
     'Nothing closes an unfiled year except the return. It is still '
     'outstanding years later.'),
    ('A Letter Can Land Instead',
     'The Agency can write and require the return, which turns a quiet '
     'obligation into a dated one.'),
    ('The Figures Can Be Invented',
     'Where no return arrives the Agency can assess on numbers of its '
     'own, and only the real return replaces them.'),
    ('Winding Up Is Blocked',
     'No clearance certificate is issued while a year is missing, so the '
     'corporation cannot be dissolved.'),
  ],
  'notnil_text': (
    'The usual reason a consulting corporation goes unfiled is that '
    'nothing happened in it, which feels like nothing is owed. The return '
    'is owed anyway, and the gap is what a future accountant, buyer or '
    'registrar sees first.',
    'Catching up is ordinary work here rather than an exception. Each '
    'quiet year is $300.00 plus HST per tax year, filed oldest first, '
    'with one T183CORP signed online for each of them.'),
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
   ('Should I dissolve the corporation instead?',
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

  'intro_h': 'Flat-Fee Nil T2 Filing for Shelf Corporations',
  'intro': (
    'A corporation that has never traded still owes returns, especially '
    'one incorporated years ago with no first transaction to point at. '
    'The obligation starts at incorporation rather than at first revenue, '
    'so a company registered in 2019 and never used owes seven returns. '
    'We file the whole run at $300.00 plus HST per tax year, with no '
    'surcharge for how far back it goes.',
    'Whether the articles were filed to reserve a name, to hold an '
    'incorporation date ready for a bank or a tender, to carry a plan '
    'that changed, or because the company was bought ready-made, we file '
    'oldest first, attach Schedule 24 to the earliest return, and sign '
    'one T183CORP per year. You get the CRA confirmation for each.'),
  'notnil_h': 'What the Unfiled Years Cost a Shelf Corporation',
  'notnil_boxes': [
    ('The Years Do Not Age Out',
     'An unfiled year stays outstanding indefinitely. A 2019 '
     'incorporation still owes its 2019 return today.'),
    ('A Demand to File Can Arrive',
     'The Canada Revenue Agency can require the return in writing, with a '
     'deadline of its own attached.'),
    ('Banks and Tenders Ask',
     'An incorporation date is only worth holding with the filing history '
     'behind it, and that is what gets requested.'),
    ('Nothing Can Be Done With It',
     'Selling the shell, using it for a tender and dissolving it all wait '
     'on the outstanding returns.'),
  ],
  'notnil_text': (
    'A shelf corporation is the easiest kind of filing to postpone, '
    'because nothing is happening and nothing is owed in cash. What '
    'accumulates instead is the count of years, and that count only '
    'grows.',
    'Clearing it is the whole point of this service. The run is filed '
    'oldest first at $300.00 plus HST per tax year, Schedule 24 goes with '
    'the earliest return, and the corporation comes out of it with an '
    'unbroken record ready for whatever it was incorporated for.'),
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
   ('Can I dissolve it and forget the returns?',
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

  'intro_h': 'Flat-Fee Nil T2 Filing for Inactive Trucking Corporations',
  'intro': (
    'Keeping an owner-operator corporation filed while you are off the '
    'road can feel like money for nothing, especially with a business '
    'number still open, often a fuel tax account beside it, and a truck '
    'that may or may not still be in the yard. We file nil T2 returns for '
    'exactly those years at $300.00 plus HST per tax year, so the entity '
    'stays clean for whenever you go back.',
    'Whether you are off with a back injury, held up by a licence issue, '
    'driving for a carrier on payroll, or waiting out a market that '
    'turned, we test the year against loads hauled, equipment sold and '
    'plate, insurance or storage costs, then prepare and transmit the '
    'return. Any year with a disposal in it is sent to the right service '
    'instead.'),
  'notnil_h': 'What an Unfiled Year Costs an Owner-Operator Corporation',
  'notnil_boxes': [
    ('The Year Does Not Close Itself',
     'Parking the truck does not end the tax year. Only the filed return '
     'does.'),
    ('The Agency Can Ask In Writing',
     'A written requirement to file turns an open year into one with a '
     'date attached to it.'),
    ('The Truck Sale Gets Messy',
     'Capital cost allowance that never carried forward is harder to '
     'compute on the day the rig finally goes.'),
    ('Going Back to Hauling Gets Harder',
     'Carriers and brokers want a corporation in good standing before '
     'they put you back on the board.'),
  ],
  'notnil_text': (
    'Most owner-operators mean to go back to it, and the corporation is '
    'kept for exactly that reason. A filing gap is the thing that makes '
    'going back awkward later.',
    'Each year off the road is $300.00 plus HST per tax year. Filing them '
    'in order keeps the capital cost allowance on the truck carrying '
    'forward, which is what matters on the day it is finally sold.'),
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
     'Every year the equipment sits unused is $300.00 plus HST, with no '
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

  'intro_h': 'Flat-Fee Nil T2 Filing for Closed Restaurant Corporations',
  'intro': (
    'Closing a restaurant rarely ends tidily. The lease is assigned or '
    'run out, the equipment goes to an auctioneer or sits in a unit '
    'nobody has emptied, and the corporation stays on the registry '
    'collecting filing years nobody is watching. We file those years at '
    '$300.00 plus HST per tax year so the entity can finally be wound up.',
    'Whether the space was handed back, sold to the next tenant, closed '
    'after a partnership split, or shut when the lease ran out, we '
    'separate the closing year from the quiet ones, prepare the nil years '
    'with Schedules 100, 125, 141 and 50, and sign a T183CORP for each. '
    'Dissolution needs every one of them filed first.'),
  'notnil_h': 'What an Unfiled Year Costs a Closed Restaurant Corporation',
  'notnil_boxes': [
    ('The Year Stays Outstanding',
     'Closing the doors does not close the tax year. The return is still '
     'owed for it.'),
    ('A Written Requirement Can Follow',
     'The Agency can demand the return, and a demand carries a date the '
     'quiet years never had.'),
    ('The Clearance Certificate Is Blocked',
     'None is issued while a year is missing, so the corporation cannot '
     'be dissolved.'),
    ('The Registry Keeps the Entity',
     'It stays listed, with its filings outstanding, until the returns '
     'are in and it is formally wound up.'),
  ],
  'notnil_text': (
    'A closed restaurant is usually meant to be finished with, and '
    'dissolution is what finishes it. Every outstanding year sits between '
    'the owner and that.',
    'The quiet years after the closure are $300.00 plus HST per tax year. '
    'Filed oldest first, with the closing year sent to the right service, '
    'they clear the way for a clearance certificate and a wind-up.'),
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
   ('Can several partners sign, or only one?',
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

  'intro_h': 'Flat-Fee Nil T2 Filing for Medicine Professional Corporations',
  'intro': (
    'A professional corporation you are not billing through still files, '
    'especially while the certificate of authorization is held, the '
    'fiscal year end keeps running, and the entity stays on the college '
    'register. We file those years at $300.00 plus HST per tax year, for '
    'physicians who want the corporation current without a full '
    'engagement.',
    'Whether you are on parental leave, away on a fellowship, moved to a '
    'salaried hospital appointment, or winding a locum practice down, we '
    'measure the year against billings and any investment income inside '
    'the corporation, prepare the return with Schedule 50 naming every '
    'shareholder at 10% or more, and transmit it electronically. A year '
    'the portfolio paid in goes to the full service.'),
  'notnil_h': 'What an Unfiled Year Costs a Medicine Professional Corporation',
  'notnil_boxes': [
    ('The Year Remains Due',
     'Not billing through the corporation does not end its tax year. Only '
     'the return does.'),
    ('The Agency Can Require It',
     'A written demand replaces an open-ended obligation with one that '
     'has a date on it.'),
    ('Restarting Practice Gets Complicated',
     'A corporation with missing years is awkward to bill through again.'),
    ('A Buy-In or Sale Looks At It',
     'Partners, lenders and purchasers read the corporate filings before '
     'anything is signed.'),
  ],
  'notnil_text': (
    'Most physicians keep the corporation because the plan is to use it '
    'again, whether after a leave, a fellowship or a move. A gap in the '
    'filings is what gets raised later, by an accountant, a lender or a '
    'purchaser.',
    'Each year the corporation billed nothing is $300.00 plus HST per tax '
    'year, filed in order, with Schedule 50 naming every shareholder at '
    '10% or more and one T183CORP signed for each.'),
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

  'intro_h': 'Flat-Fee Nil T2 Filing for Dormant Construction Corporations',
  'intro': (
    'A trades corporation between phases still owes a return each year, '
    'with tools and a trailer that may still be owned, a workers '
    'compensation account still open, and the entity sitting on the '
    'registry waiting for the next job. We file those seasons at $300.00 '
    'plus HST per tax year so the company stays ready to bid.',
    'Whether you took a payroll job with a larger builder, split a '
    'partnership and stopped bidding, sold the trailer, or are '
    'between contracts, we test the season against released holdback, '
    'subcontractor payments and equipment disposals, then prepare and '
    'transmit the return. An unbroken filing history is what bonding and '
    'prequalification ask for later.'),
  'notnil_h': (
    'What an Unfiled Season Costs a Dormant Construction Corporation'),
  'notnil_boxes': [
    ('The Season Stays Open',
     'No work does not mean no return. The year is outstanding until it '
     'is filed.'),
    ('A Written Demand Can Come',
     'The Agency can require the season be filed, on a timetable that it '
     'sets rather than you.'),
    ('Bonding and Prequalification Ask',
     'Sureties and general contractors want filing history before they '
     'take a trade on.'),
    ('Closing the Company Waits',
     'Dissolution needs every season filed first, so the entity cannot '
     'be abandoned.'),
  ],
  'notnil_text': (
    'A dormant trades corporation is almost always kept on purpose, '
    'because the next job might need it. What makes it usable is the '
    'record behind it, and a gap is what damages the record.',
    'Each empty season is $300.00 plus HST per tax year. Filing them in '
    'order keeps the capital cost allowance on the trucks and tools '
    'carrying forward, and leaves the company ready to bid.'),
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

  'intro_h': 'Flat-Fee Nil T2 Filing for E-Commerce Corporations',
  'intro': (
    'Switching off a storefront does not switch off the corporation '
    'behind it. The seller account is deactivated, the last stock is '
    'cleared at cost or left in a spare room, and the domain renews on '
    'its own while the entity stays registered. We file the dark years at '
    '$300.00 plus HST per tax year.',
    'Whether you sold on a marketplace, ran a direct-to-consumer brand, '
    'dropshipped, or printed on demand, we read every payout channel '
    'before treating a year as nil, carry any remaining stock or held '
    'processor balance on Schedule 100, and sign one T183CORP per year. A '
    'released balance makes that year a full return instead.'),
  'notnil_h': 'What an Unfiled Year Costs an E-Commerce Corporation',
  'notnil_boxes': [
    ('A Dark Year Is Still a Tax Year',
     'Switching the store off ends the trading, not the filing. The '
     'return is what ends that.'),
    ('A Notice Can Arrive Instead',
     'The Agency can require the return in writing, and the notice sets a '
     'date of its own.'),
    ('Selling the Brand Gets Harder',
     'A buyer looking at the store, the domain or the customer list will '
     'want clean corporate filings.'),
    ('Dissolution Waits on the Run',
     'Every dark year goes in before the entity can be formally closed.'),
  ],
  'notnil_text': (
    'Most sellers either come back to it or sell what is left of it. Both '
    'depend on a corporation whose filings are current, and neither is '
    'helped by a run of dark years nobody dealt with.',
    'Each dark year is $300.00 plus HST per tax year, filed oldest first, '
    'with any remaining stock or held processor balance carried on '
    'Schedule 100 so the figures reconcile across the run.'),
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


 'real-estate-holding-corporations': {
  'name':   'Real Estate Holding Corporations',
  'short':  'real estate holding corporation',
  'plural': 'real estate holding corporations',
  'kw':     'nil t2 for real estate holding corporation',
  'title':  'Real Estate Holding Corporation Nil T2 | Unrented Years',
  'desc':   'A corporation that collects rent is not nil. Where it holds land '
            'that earned nothing and cost it nothing, the year can be. What '
            'that costs to file.',

  'h1':   'Nil T2 Filing for Real Estate Holding Corporations',
  'lede': 'A corporation that collected rent in the year is not nil. Where it '
          'held property that earned nothing and cost it nothing, the return '
          'is $300.00 plus HST per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Real Estate Holding Corporations',
  'intro': (
    'Property sitting in a corporation still generates a filing '
    'obligation every year: title in the corporation name, a property tax '
    'bill whether or not anything is built, and a return owed for as long '
    'as the entity exists. A holding, rental or investment corporation is '
    'not nil in any year it earns, so we test each year before charging '
    'for it, and the idle ones are $300.00 plus HST per tax year.',
    'Whether the corporation holds land banked against a build that has '
    'not started, a parcel rolled in before a plan changed, a future '
    'cottage, or a development site left untouched for years, we check '
    'rent and carrying costs first, add Schedule 8 where a building '
    'stands on the land, and transmit the return electronically. Any year '
    'with rent in it goes to the full service.'),
  'notnil_h': (
    'What an Unfiled Year Costs a Real Estate Holding Corporation'),
  'notnil_boxes': [
    ('The Year Runs With the Title',
     'Holding the property through a year does not file for it. Only the '
     'return does that.'),
    ('A Demand Can Reach the Corporation',
     'The Agency can require the outstanding returns in writing, on dates '
     'it chooses.'),
    ('A Sale or Refinancing Stalls',
     'A lender or a buyer looking at the property wants the corporate '
     'filings current before closing.'),
    ('The Property Cannot Be Moved Out',
     'Without a clearance certificate the land cannot be distributed out '
     'and the entity wound up.'),
  ],
  'notnil_text': (
    'A property corporation is almost always holding for a reason, '
    'whether that is a build, a sale or a transfer to the next '
    'generation. All three run through the corporation, and all three get '
    'held up by filings that are not current.',
    'Each idle year is $300.00 plus HST per tax year, filed oldest first '
    'so the property cost base carries forward, with Schedule 8 added '
    'where a building stands on the land.'),
  'sched_h': 'Which T2 Schedules a Real Estate Holding Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Land and buildings sit on the balance sheet at cost, with any mortgage '
     'against them, so it is never an empty schedule.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Reports nil rental revenue and nil carrying costs for a year the '
     'corporation neither collected nor paid.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Goes with Schedules 100 and 125 and names whoever compiled them.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Property is often held by two or more family members or partners. '
     'Anyone at 10% or more of a class is named.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the first T2 after incorporation, which is often the year '
     'the property was bought.'),
    ('Schedule 8', 'Capital cost allowance', 'Only with a building',
     'Land is not depreciable property. A building standing on it is, in '
     'Class 1, so Schedule 8 can apply in a year with no rent at all.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, applied to a corporation holding real '
                'property that produced no income in the tax year. Last '
                'reviewed November 19, 2026.',
  'sched_boxes': [
    ('Land Is Not Depreciable',
     'Land carries no capital cost allowance. A building on it does, which is '
     'why Schedule 8 can apply to a corporation with no tenant.'),
    ('Rent Makes It a Rental Corporation',
     'One month of rent on one unit is enough. That year is a full return '
     'rather than a nil one.'),
    ('Carrying Costs Count as Activity',
     'Property tax or insurance paid by the corporation is an expense on '
     'Schedule 125, and that ends the nil year.'),
  ],
  'chk_yes': [
    'No rent, lease payment or licence fee reached the corporation',
    'No property tax, insurance or mortgage payment was made by it',
    'No property, lot or interest in one was sold or transferred',
    'No deposit, option fee or holding payment was received',
    'No interest was credited on any account it holds',
  ],
  'chk_no': [
    'Rent was collected for any part of the year, from any tenant',
    'The corporation paid property tax, insurance or mortgage interest',
    'Land, a building or part of one was sold or transferred out',
    'An option fee or a deposit on a future sale was taken in',
    'A development, servicing or survey cost was paid by the corporation',
  ],
  'chk_both': [
    'A T2 for every tax year the corporation exists',
    'A T183CORP signed by an authorised signing officer, per tax year',
    'Schedule 8, for as long as a building stands on the land',
    'The provincial land registry record, which the T2 does not touch',
    'A clearance certificate, before the property can be distributed out',
  ],

  'why_h': 'Why Real Estate Holding Corporations Use This Service',
  'why': [
    ('For the Years Before It Earns',
     'Land held and not yet built on or rented is the case this service was '
     'written for.'),
    ('The Rent Question Is Settled First',
     'Any rent at all makes the year a full return, so that is tested before '
     'anything is charged.'),
    ('A Flat Fee Per Idle Year',
     'Each year the property sat still is $300.00 plus HST per tax year, with '
     'nothing billed by the hour.'),
    ('Earning Years Are Referred On',
     'A year with rent, a disposition or carrying costs goes to the full '
     'corporate service.'),
  ],
  'strip': [
    ('Owning Is Not Earning',
     'Title in the corporation name does not by itself make a year active.'),
    ('In Date Order',
     'Years go across earliest first so the property cost base carries '
     'forward.'),
    ('Signed Online',
     'Each T183CORP is signed through a secure portal, with no appointment.'),
  ],

  'svc_h': 'What a Real Estate Holding Corporation Usually Needs Next',
  'proc_h': 'How a Real Estate Holding Corporation Files',
  'proc_lede': 'Four steps through the filing form, beginning with rent and '
               'carrying costs.',
  'proc_note': 'Most owners work through this in one sitting:',
  'steps': [
    ('Test for Rent and Carrying Costs',
     'Rent received, and property tax, insurance or mortgage interest paid by '
     'the corporation, each take the year out of nil.'),
    ('Confirm the Year-End on Record',
     'The fiscal year-end the Agency holds has to agree with the return, or '
     'the transmission is refused.'),
    ('Prepare the Return and Schedules',
     'The T2 with Schedules 100, 125, 141 and 50, plus Schedule 8 where a '
     'building stands on the land.'),
    ('Sign Each Year, Then File',
     'One T183CORP per year, signed online, and the Agency confirmation lands '
     'by email within 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Real Estate Holding Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year. The fee covers the T2, '
    'the GIFI schedules where required, Schedule 50, Schedule 24 on a first '
    'return, the T183CORP package with secure e-signing, CPA review before '
    'transmission, electronic transmission by a registered EFILE electronic '
    'filer, one corrected transmission where the Agency rejects the first, '
    'and the CRA confirmation emailed within 3 business days. A year with '
    'rent, carrying costs or a disposition is $350.00 plus HST per year at '
    'gondaliyacpa.ca.'),

  'geo_h': 'Property Holding Corporation Filing Across Canada',
  'cta_h': 'File the Idle Years Before the Property Moves',

  'faq': [
   ('My corporation owns a rental property. Is any year nil?',
    'Not a year it collected rent. A corporation receiving rent is a rental '
    'corporation for that year and files a full T2. A year before the first '
    'tenant, or after the last one left with nothing paid or received, can '
    'be nil.'),
   ('We bought a lot and have not built on it. Is that nil?',
    'It can be, provided the corporation itself neither received nor paid '
    'anything during the year. Land sitting still earns nothing, so the usual '
    'obstacle is property tax rather than income.'),
   ('I pay the property tax personally. Does that help?',
    'It can. A cost a shareholder pays personally is not the corporation’s '
    'expense. What decides it is which entity paid, and the bank record is '
    'what shows that.'),
   ('Does the corporation file Schedule 8 with no rent?',
    'Where a building stands on the land, yes. A building is depreciable '
    'property in Class 1 whether or not it earned. Bare land is not '
    'depreciable and carries no Schedule 8.'),
   ('We sold the property last year. What does that year look like?',
    'A full return. A disposition puts a capital gain or loss in the year, '
    'and any recapture on a building goes with it, so that year is not nil.'),
   ('A buyer paid a deposit we later returned. Is the year nil?',
    'No. The deposit moving in and out is money through the corporation, so '
    'the year is active even though nothing was kept.'),
   ('My spouse and I hold it together. Who is listed?',
    'Each shareholder at 10% or more of a class is named on Schedule 50, '
    'whatever the split, and one authorised signing officer signs the '
    'T183CORP.'),
   ('Can I transfer the property out and then dissolve?',
    'The transfer is a disposition in its own year, and a clearance '
    'certificate will not be issued while any year is unfiled. The '
    'outstanding returns come first.'),
   ('Does the land registry filing count as the corporate return?',
    'No. The registry records title and the T2 reports the tax year. Neither '
    'one does the other’s job.'),
   ('How many idle years can be filed together?',
    'All of them. One T2 and one T183CORP per year, each at $300.00 plus HST '
    'per tax year, sent earliest first so the property cost base carries '
    'forward.'),
  ],
 },

 'dormant-it-consulting-corporations': {
  'name':   'Dormant IT Consulting Corporations',
  'short':  'dormant IT consulting corporation',
  'plural': 'dormant IT consulting corporations',
  'kw':     'dormant it consulting corporation t2',
  'title':  'Dormant IT Consulting Corporation T2 | Between Contracts',
  'desc':   'The contract ended and the corporation stayed on the register. '
            'Which bench years are nil, what a cloud charge does to one, and '
            'what each costs.',

  'h1':   'Nil T2 Filing for Dormant IT Consulting Corporations',
  'lede': 'A year on the bench between contracts is still a tax year. Where '
          'the corporation neither billed nor paid, the return is $300.00 '
          'plus HST per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Dormant IT Consulting Corporations',
  'intro': (
    'An IT corporation between contracts still files, with a closed '
    'statement of work behind it, a workstation still on the books, and a '
    'business number that stays open until somebody closes it. We file '
    'bench years at $300.00 plus HST per tax year, so the entity is ready '
    'when the next contract needs it.',
    'Whether you incorporated because a client or an agency required it, '
    'moved to agency payroll when the project closed, took ordinary '
    'employment, or are waiting for the next statement of work, we '
    'read the corporate card before treating a year as nil, keep '
    'equipment on Schedule 8 while it is owned, and sign one T183CORP per '
    'year online. Agencies ask for the filing history at onboarding.'),
  'notnil_h': 'What an Unfiled Bench Year Costs an IT Corporation',
  'notnil_boxes': [
    ('The Year Does Not Lapse',
     'Being between contracts does not end the tax year. Only the filed '
     'return does.'),
    ('The Agency Can Put a Date On It',
     'A written requirement to file converts an open-ended obligation '
     'into a deadline.'),
    ('Supplier Onboarding Checks It',
     'Agencies and enterprise clients ask for corporate filing history '
     'before putting you on a contract.'),
    ('Closing It Down Waits',
     'Winding the corporation up needs the bench years filed first.'),
  ],
  'notnil_text': (
    'The corporation is usually kept for the next engagement. What gets '
    'looked at when that engagement arrives is whether the entity is '
    'current, and a filing gap is an awkward thing to explain '
    'mid-onboarding.',
    'Each bench year is $300.00 plus HST per tax year. There is no '
    'engagement letter, no discovery call and nothing to post, and '
    'several years can be signed off in one sitting.'),
  'sched_h': 'Which T2 Schedules a Dormant IT Consulting Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'A bank balance, a shareholder loan or equipment at written-down value '
     'keeps the balance sheet populated between contracts.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Reports nil professional fees and nil costs across a year with no '
     'statement of work billed.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Filed beside Schedules 100 and 125, recording who compiled them.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Most IT corporations have one shareholder, sometimes two. Anyone at '
     '10% or more of a class is named.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the first T2 after incorporation, usually the year the first '
     'contract started.'),
    ('Schedule 8', 'Capital cost allowance', 'While equipment is held',
     'Workstations, servers, monitors and test devices carry capital cost '
     'allowance for as long as the corporation owns them.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, applied to an IT corporation that '
                'billed no statement of work in the tax year. Last reviewed '
                'November 19, 2026.',
  'sched_boxes': [
    ('A Small Charge Is Still a Charge',
     'A few dollars of cloud compute on the corporate card puts a figure on '
     'Schedule 125 and ends the nil year.'),
    ('Agency Payroll Is Personal',
     'Income earned through an agency or as an employee is yours, not the '
     'corporation’s, and does not make its year active.'),
    ('Equipment Keeps Depreciating',
     'A workstation stays on Schedule 8 while it is owned, whether or not it '
     'was used for any work.'),
  ],
  'chk_yes': [
    'No statement of work, milestone or change request was billed',
    'No cloud, hosting, domain or certificate charge hit the corporation',
    'No equipment or licence was bought, sold or written off by it',
    'No referral, affiliate or vendor commission was received',
    'It paid no salary, dividend or management fee to anyone',
  ],
  'chk_no': [
    'A closing milestone or holdback on an old contract was billed',
    'A compute, hosting or domain account charged the corporate card',
    'A workstation, server or device was sold, traded or written off',
    'A vendor or partner programme paid a commission or a rebate',
    'The corporation reimbursed the owner for anything at all',
  ],
  'chk_both': [
    'A T2 for every tax year the corporation exists',
    'One signed T183CORP covering each of those years',
    'An equipment list, because what is on the books decides Schedule 8',
    'The business number, which stays open until it is closed',
    'A clean filing record, which agencies ask for at onboarding',
  ],

  'why_h': 'Why Dormant IT Consulting Corporations Use This Service',
  'why': [
    ('Built for Bench Years',
     'The stretch between one engagement ending and the next beginning is '
     'precisely what gets filed here.'),
    ('The Card Is Read First',
     'Each year is read against cloud, domain and subscription charges before '
     'it is treated as nil.'),
    ('A Flat Fee Per Bench Year',
     'Every bench year is priced the same, $300.00 plus HST per tax year, '
     'with no retainer and nothing on the clock.'),
    ('Billing Years Are Referred On',
     'A year with a milestone, a commission or a disposal goes to the full '
     'corporate service.'),
  ],
  'strip': [
    ('The Entity Outlives the Contract',
     'A closed statement of work does not close the corporation or its '
     'filings.'),
    ('Earliest Year Leads',
     'Returns go across in date order so the equipment schedule carries '
     'forward.'),
    ('No Printer Needed',
     'Each T183CORP is signed in the browser through a secure portal.'),
  ],

  'svc_h': 'What a Dormant IT Consulting Corporation Usually Needs Next',
  'proc_h': 'How a Dormant IT Consulting Corporation Files',
  'proc_lede': 'Four steps through the filing form, starting with what the '
               'corporate card did.',
  'proc_note': 'Most contractors get through it between standups:',
  'steps': [
    ('Read the Corporate Card',
     'Cloud, hosting, domain and subscription charges are read before the '
     'year is treated as nil.'),
    ('Check the Year-End on File',
     'The fiscal year end on the Agency record has to match the return, or '
     'the transmission is refused.'),
    ('Assemble the Filing',
     'The T2 plus its GIFI schedules and Schedule 50, with Schedule 8 for any '
     'equipment still on the books.'),
    ('Sign, Then Transmit',
     'One T183CORP signed in the browser per year. Confirmation from the '
     'Agency lands by email inside 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Dormant IT Consulting Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year. The fee covers the T2, '
    'the GIFI schedules where required, Schedule 50, Schedule 24 on a first '
    'return, the T183CORP package with secure e-signing, CPA review before '
    'transmission, electronic transmission by a registered EFILE electronic '
    'filer, one corrected transmission where the Agency rejects the first, '
    'and the CRA confirmation emailed within 3 business days. A year with a '
    'milestone, a commission or cloud charges on the books is $350.00 plus '
    'HST per year at gondaliyacpa.ca.'),

  'geo_h': 'IT Corporation Filing Across Canada',
  'cta_h': 'File the Bench Years and Keep the Entity Contract-Ready',

  'faq': [
   ('My contract ended and I joined an agency payroll. Does it still file?',
    'Yes, every year it exists. Agency or employment income is yours '
    'personally. The corporation owes its own T2 until it is dissolved, and a '
    'year with nothing billed through it is nil.'),
   ('I left a cloud account running for about six dollars a month. Nil?',
    'No. An expense the corporation incurred is activity whatever its size, '
    'so that year is a full return. The amount changes the figures, not the '
    'test.'),
   ('Can I keep the corporation dormant and use it for the next contract?',
    'Yes. That is usually why a contractor files instead of dissolving: '
    'agencies and enterprise clients want corporate filing history at '
    'supplier onboarding, and a gap in it takes explaining.'),
   ('I had a single client for three years. Does that change anything?',
    'Not the nil years. A single-client arrangement raises questions about '
    'how the income is taxed in the years it was earned, and those belong to '
    'the active returns rather than to a year with no billing in it.'),
   ('My workstation is still on the books. Does that stop a nil year?',
    'No. Owning equipment is not activity. It sits on Schedule 8 at its '
    'written-down value. Selling it or writing it off is what makes the year '
    'active.'),
   ('A final milestone was invoiced after the project closed. Which year?',
    'The year it was billed rather than the year it was paid. That one is a '
    'full return, and the years after it can still be nil.'),
   ('Do I need to close the business number before filing?',
    'No. It stays open and expects whatever it is registered for until you '
    'close it, and the T2 neither opens nor closes it.'),
   ('What if I am working abroad while the corporation sits here?',
    'The corporation is Canadian and files where it is resident. Where you '
    'are working changes your own position, not its filing obligation.'),
   ('Who signs if I am the only shareholder?',
    'You do, as authorised signing officer, once per tax year. Several years '
    'can be signed in one go.'),
   ('How far back can bench years be filed?',
    'As far back as they run. One return and one signature per year, each '
    'priced at $300.00 plus HST per tax year, and they go in date order.'),
  ],
 },

 'inactive-law-professional-corporations': {
  'name':   'Inactive Law Professional Corporations',
  'short':  'inactive law professional corporation',
  'plural': 'inactive law professional corporations',
  'kw':     'inactive law professional corporation t2',
  'title':  'Inactive Law Professional Corporation T2 | Nil Returns',
  'desc':   'A law corporation owes a T2 for every year it stays in '
            'existence. When a year with no account issued is nil, and why '
            'trust money does not change that.',

  'h1':   'Nil T2 Filing for Inactive Law Professional Corporations',
  'lede': 'A year in which the corporation issued no account is still a tax '
          'year on the Agency record. Where no fee was billed through it and '
          'nothing it owns paid out, the return is $300.00 plus HST per tax '
          'year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Inactive Law Professional '
             'Corporations',
  'intro': (
    'A law corporation that has stopped issuing accounts is still an existing '
    'corporation. The certificate of authorization sits with the law society, '
    'the fiscal year end keeps turning over, and the Agency expects a return '
    'for each period whether a docket was opened in it or not. Those years '
    'are $300.00 plus HST per tax year.',
    'Whether you moved in-house, took a government or tribunal appointment, '
    'went to non-practising status, or stopped accepting new retainers '
    'altogether, the year is measured against accounts actually issued by the '
    'corporation and against anything its own accounts or investments paid. '
    'The return is prepared with Schedules 100, 125, 141 and 50 and '
    'transmitted electronically. A year in which a settlement or a referral '
    'fee reached the corporation goes to the full service instead.'),

  'notnil_h': 'What an Unfiled Year Costs an Inactive Law Professional '
              'Corporation',
  'notnil_boxes': [
    ('The Fiscal Year Turns Over Anyway',
     'Closing a practice does not close the corporation. It keeps producing '
     'tax years until it is dissolved.'),
    ('The Agency Can Set the Clock',
     'An obligation with no date on it becomes one with a deadline the moment '
     'a written demand is issued.'),
    ('Going Back Into Practice Means Catching Up',
     'Accounts cannot sensibly be issued again through a corporation whose '
     'filing record has holes in it.'),
    ('A Merger or Retirement Deal Reads the Record',
     'Firms absorbing a practice, and the insurers behind them, look at the '
     'corporate filings before terms are settled.'),
  ],
  'notnil_text': (
    'Counsel usually keep the corporation because they may practise through '
    'it again, or because files remain open under its name. The gap in the '
    'filings is what surfaces later, when a firm, an insurer or a purchaser '
    'asks for the corporate record.',
    'A year in which the corporation issued no account is $300.00 plus HST '
    'per tax year. Outstanding years are worked oldest first so that every '
    'opening balance agrees with the year that closed before it.'),

  'sched_h': 'Which T2 Schedules an Inactive Law Professional Corporation '
             'Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Share capital, retained earnings and any amount still owing to a '
     'shareholder stay on the balance sheet through the quiet years.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Carries nil fee income and nil disbursements where no account went out '
     'in the period.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Accompanies the two GIFI schedules and records who compiled them and on '
     'what basis.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Lists every holder of 10% or more of the shares, whoever the law '
     'society share-ownership rules permit those holders to be.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Goes on the first T2 only, covering the period that begins the day the '
     'corporation came into existence.'),
    ('Schedule 8', 'Capital cost allowance', 'While depreciable property '
     'remains',
     'A library, office furniture and leasehold improvements stay depreciable '
     'property until they are sold, scrapped or taken out of the '
     'corporation.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, read against a law corporation that '
                'issued no account in the tax year. Last reviewed '
                'November 20, 2026.',
  'sched_boxes': [
    ('Trust Money Is Not Corporate Income',
     'Funds held for a client in a mixed trust account are the client’s. '
     'The corporation holds them rather than earning them, so they put no '
     'figure on Schedule 125.'),
    ('The Law Society Filing Is a Different One',
     'The annual report and the annual fee go to the law society on its own '
     'cycle. Neither is a T2, and a T2 does not answer either.'),
    ('Interest on the General Account Does Count',
     'Where the corporation’s own account or a portfolio it holds is '
     'credited with interest or a dividend, that is income to it and the year '
     'becomes an ordinary return.'),
  ],
  'chk_yes': [
    'No account for fees was issued by the corporation during the year',
    'No contingency file in its name settled or was paid out',
    'No referral fee or fee split was received by it',
    'No interest or dividend was credited to anything it owns',
    'Nothing left it as salary, dividend or shareholder draw',
  ],
  'chk_no': [
    'An account went out, even for work docketed in an earlier year',
    'A fee was drawn from trust into the general account',
    'A referral fee arrived from another firm',
    'Interest was credited on the corporation’s own general account',
    'The practice, its open files or its goodwill changed hands for value',
  ],
  'chk_both': [
    'One T2 for every tax year that ends while the corporation exists',
    'A separate T183CORP authorisation for each of those years',
    'Schedule 50, wherever a 10% holding exists',
    'The law society annual report and fee, dealt with on their own cycle',
    'Trust records and client files kept for as long as the law society '
    'requires',
  ],

  'why_h': 'Why Inactive Law Professional Corporations Use This Service',
  'why': [
    ('Written for the Years Off the Roll',
     'In-house, on an appointment, non-practising, or no longer taking '
     'retainers. Those are the years this fee is for.'),
    ('The Fee Test Runs Before the Charge',
     'Each year is checked against accounts issued and against interest or '
     'dividends inside the corporation before it is treated as nil.'),
    ('One Price, One Year',
     'A year with no account issued costs $300.00 plus HST per tax year, '
     'whether it is the only outstanding one or the fourth in a row.'),
    ('Years With Fees Are Handled Elsewhere',
     'Where a settlement, a referral fee or an account appears, that year is '
     'prepared as an ordinary corporate return at the higher fee.'),
  ],
  'strip': [
    ('The Duty Follows the Entity',
     'It attaches to the corporation on the register, not to whether anyone '
     'is practising through it.'),
    ('Earliest Year First',
     'Returns go across in date order so every opening balance matches the '
     'year that closed before it.'),
    ('Nothing Goes in the Post',
     'The signing package opens in an access-controlled portal, so no part of '
     'this needs printing, scanning or a courier.'),
  ],

  'svc_h': 'What an Inactive Law Professional Corporation Usually Needs Next',
  'proc_h': 'How an Inactive Law Professional Corporation Files',
  'proc_lede': 'Four steps, taken from the filing form, starting with the '
               'test that decides the year.',
  'proc_note': 'Counsel generally finish this in one sitting:',
  'steps': [
    ('Check What the Corporation Billed',
     'Accounts issued, contingency fees received, referral fees and interest '
     'credited to its accounts are all measured before a year is called '
     'nil.'),
    ('Match the Year End to the Agency Record',
     'A law corporation often runs a year end that is not December 31. It has '
     'to agree with what the Agency holds or the transmission is rejected.'),
    ('Build the Return',
     'Schedules 100, 125, 141 and 50 are prepared for the year, with '
     'Schedule 24 added where this is the corporation’s first T2.'),
    ('Authorise Each Year and Transmit',
     'One T183CORP covers one year, so the whole set is authorised in a '
     'single sitting. The returns are then transmitted and the Agency '
     'confirmation follows by email inside 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for an Inactive Law Professional '
             'Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Nil T2 filing is $300.00 plus HST per tax year. That covers the T2 '
    'itself, the GIFI schedules where they are required, Schedule 50, '
    'Schedule 24 on a first return, the T183CORP package with secure '
    'e-signing, CPA review before anything is sent, electronic transmission '
    'by a registered EFILE electronic filer, one corrected transmission where '
    'the Agency rejects the first, and the CRA confirmation emailed within 3 '
    'business days. A year in which the corporation billed a fee or earned '
    'investment income is $350.00 plus HST per year at gondaliyacpa.ca.'),

  'geo_h': 'Law Corporation Filing Across Canada',
  'cta_h': 'File the Years Off the Roll and Keep the Entity in Order',

  'faq': [
   ('I moved in-house and stopped billing. Does the corporation still file?',
    'Yes. It is a separate taxpayer and keeps producing tax years for as long '
    'as it is in existence. What an employer pays you is yours rather than '
    'the corporation’s, so it neither makes the corporate year active '
    'nor excuses the return.'),
   ('Does money in my trust account make the year active?',
    'No. Trust funds are the clients’ and the corporation only holds '
    'them. What would make the year active is a fee drawn out of trust into '
    'the general account, because at that point the corporation has billed.'),
   ('A contingency file settled three years after I closed. Which year?',
    'The year the fee was received by the corporation. That year is prepared '
    'as an ordinary return at $350.00 plus HST per year at gondaliyacpa.ca, '
    'and the years on either side of it can still be nil.'),
   ('I am on non-practising status. Is the corporation nil?',
    'It can be, provided it issued no account and nothing it owns was '
    'credited with interest or a dividend. Your status governs practice; the '
    'corporation’s filing duty runs on its own.'),
   ('Can the law society annual report stand in for the T2?',
    'No. They go to different bodies on different cycles, and neither is '
    'accepted in place of the other.'),
   ('A referral fee came in from another firm. Does that end the nil year?',
    'For that year, yes. A referral fee received by the corporation is income '
    'to it, which puts a figure on Schedule 125 and makes the return an '
    'ordinary one.'),
   ('I still practise, but as an employee of a firm. Is my corporation nil?',
    'It can be. Where the firm paid you personally and the corporation issued '
    'no account, nothing was earned inside it. The test is whose name the '
    'account went out under.'),
   ('Can several outstanding years be filed together?',
    'Yes. Each is its own T2 with its own T183CORP at $300.00 plus HST per '
    'tax year, and the set goes across from the earliest year forward.'),
   ('I want to dissolve the corporation. Can the missing years be skipped?',
    'No. They still have to be filed, and a final return falls due six months '
    'after the dissolution date. No clearance certificate is issued while a '
    'year is outstanding.'),
   ('Who signs the T183CORP when I am the only shareholder and director?',
    'You sign it in that capacity, once for each tax year in the set. No '
    'second signatory is needed where you are the only officer.'),
  ],
 },

 'dental-professional-corporations': {
  'name':   'Dental Professional Corporations',
  'short':  'dental professional corporation',
  'plural': 'dental professional corporations',
  'kw':     'nil t2 for dentistry professional corporation',
  'title':  'Dental Professional Corporation Nil T2 | Quiet Years',
  'desc':   'A dental professional corporation files for every tax year it '
            'exists, including a year it treated nobody. What makes such a '
            'year nil, and what ends it.',

  'h1':   'Nil T2 Filing for Dental Professional Corporations',
  'lede': 'A year in which the corporation treated nobody is still a tax '
          'year. Where nothing was billed through it and nothing it holds '
          'earned, the return is $300.00 plus HST per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Dental Professional Corporations',
  'intro': (
    'A dental corporation can stop treating and carry on existing. The '
    'certificate of authorization is held, the operatory may be packed up or '
    'standing idle, and the fiscal year end keeps arriving with a return '
    'behind it. Those years are $300.00 plus HST per tax year.',
    'Whether you took a year out, moved to associating at someone else\u2019s '
    'clinic, closed on retirement, or sold the practice and kept the '
    'corporation, the year is tested against treatment billed through it, '
    'instalments still arriving on long treatment plans, plan and insurer '
    'payments, and anything the corporation holds that earns. The return is '
    'prepared with Schedules 100, 125, 141 and 50 and transmitted '
    'electronically. A year with any of those in it goes to the full '
    'service.'),

  'notnil_h': 'What an Unfiled Year Costs a Dental Professional Corporation',
  'notnil_boxes': [
  ('A Chair That Does Not Turn Still Files',
     'Treating nobody changes what the return says. It does not remove the '
     'return or stop the tax years arriving.'),
    ('Whatever Is Held Inside Is Exposed',
     'A corporation holding retained earnings or sale money is the one '
     'nobody wants questions about years later.'),
    ('The Agency Can Put a Date On It',
     'A written demand converts an open obligation into one with a stated '
     'deadline.'),
    ('The Wind-Up Stalls Without Them',
     'No clearance certificate is issued while a year is missing, so the '
     'money cannot be taken out and the corporation closed.'),
  ],
  'notnil_text': (
    'The corporation is normally kept on purpose: to hold what is in it, to '
    'keep the option of practising through it again, or because dissolving it '
    'was never got round to. Each of those reasons produces tax years, and '
    'each of those years is owed a return.',
    'A year the corporation treated nobody and earned nothing is $300.00 plus '
    'HST per tax year. Where several are outstanding they are prepared '
    'together and filed in the order they arose.'),

  'sched_h': 'Which T2 Schedules a Dental Professional Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Retained earnings from practising years, share capital and any balance '
     'owing to a shareholder keep the balance sheet populated long after the '
     'last appointment.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Shows nil treatment income and nil practice expenses for a year in '
     'which nothing was billed.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Filed alongside the two GIFI schedules and states on what basis the '
     'figures were put together.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Each holder of 10% or more appears, including a spouse or adult child '
     'holding non-voting shares issued while the practice was running.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the corporation’s very first T2 and not again '
     'afterwards.'),
    ('Schedule 8', 'Capital cost allowance', 'While equipment is still owned',
     'Chairs, an imaging unit, sterilisation equipment and leasehold '
     'improvements stay on the schedule until they are sold with the practice '
     'or written off.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, read against a dental corporation '
                'that treated nobody during the year. Reviewed '
                '20 November 2026.',
  'sched_boxes': [
    ('A Long Treatment Plan Can Pay Late',
     'Orthodontic and implant cases are often paid by instalment. An '
     'instalment arriving after the practice closed is income in the year it '
     'is received.'),
    ('Proceeds That Earn End the Nil Year',
     'Sale money left in a corporate account or investment pays interest or '
     'dividends, and either one puts a figure on Schedule 125.'),
    ('The College Registration Is Its Own Matter',
     'Registration and the certificate of authorization renew with the '
     'regulator on its own cycle. The T2 has no bearing on either.'),
  ],
  'chk_yes': [
    'No treatment was billed through the corporation in the year',
    'No instalment on an earlier treatment plan was received by it',
    'No payment arrived from a public or insurance plan',
    'Nothing it holds paid interest, dividends or a gain',
    'No part of the practice or its equipment was sold during the year',
  ],
  'chk_no': [
    'An instalment on an orthodontic or implant case came in',
    'A plan or insurer paid for treatment delivered earlier',
    'The proceeds of sale earned interest or dividends inside it',
    'Equipment, goodwill or the patient records were sold or transferred',
    'A shareholder was paid salary or a dividend out of it',
  ],
  'chk_both': [
    'A return for each year end that falls while the corporation exists',
    'A signing officer\u2019s authorisation attached to each one',
    'Shareholder details wherever a tenth of the shares is held',
    'Regulator registration, renewed quite separately from any of this',
    'Clearance, which is what finally lets the corporation close',
  ],

  'why_h': 'Why Dental Professional Corporations Use This Service',
  'why': [
    ('Built for the Years Without Patients',
     'A year out, a year associating elsewhere, or the years after the '
     'practice closed. Those are the ones this fee is written for.'),
    ('What the Corporation Holds Is Checked First',
     'Interest or dividends on money kept inside it is the usual reason one '
     'of these years turns out not to be nil, so it is tested before '
     'anything is charged.'),
    ('A Fixed Amount Per Year',
     'Each quiet year is $300.00 plus HST per tax year, however far back the '
     'chairs stopped turning.'),
    ('Earning Years Go to the Full Return',
     'A year with an instalment or investment income in it is prepared as an '
     'ordinary corporate return at the higher fee.'),
  ],
  'strip': [
    ('Quiet Is Not Closed',
     'A corporation that treats nobody is still a corporation with a year '
     'end.'),
    ('Earliest Year Leads the Set',
     'Balances only line up down the run if the returns go in that way.'),
    ('No Chair Time Lost',
     'The filing form and the signing portal between them are the whole '
     'engagement.'),
  ],

  'svc_h': 'What a Dental Professional Corporation Usually Needs Next',
  'proc_h': 'How a Dental Professional Corporation Files',
  'proc_lede': 'Four steps from the filing form, with the income test ahead '
               'of everything else.',
  'proc_note': 'Most of this is answered from one set of statements:',
  'steps': [
    ('Put the Year Through the Income Test',
     'Treatment billed, late instalments, plan and insurer payments and '
     'whatever the corporation holds are each checked before the year is '
     'called nil.'),
    ('Settle the Fiscal Year End',
     'Dental corporations often keep a year end set years ago. It must agree '
     'with the Agency record for the return to go through.'),
    ('Prepare the Return',
     'The T2 carries Schedules 100, 125, 141 and 50, with Schedule 24 where '
     'it is the first one and Schedule 8 while equipment is still owned.'),
    ('Authorise Each One, Then File',
     'Every year in the set carries its own T183CORP. The returns go across '
     'together and the Agency confirms by email inside 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Dental Professional Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Every quiet year is charged the same: $300.00 plus HST per tax year. '
    'Sitting behind that are the T2, the GIFI schedules where required, '
    'Schedule 50, Schedule 24 on a first '
    'return, the T183CORP package with secure e-signing, CPA review before '
    'transmission, electronic transmission by a registered EFILE electronic '
    'filer, one corrected transmission where the Agency rejects the first, '
    'and the CRA confirmation emailed within 3 business days. A year with '
    'treatment income, a late instalment or investment income in it is '
    '$350.00 plus HST per year at gondaliyacpa.ca.'),

  'geo_h': 'Dental Corporation Filing Across Canada',
  'cta_h': 'File the Years the Chairs Stood Still',

  'faq': [
   ('I treated nobody through the corporation last year. Does it still file?',
    'Yes, for every year it continues to exist. Stopping treatment changes '
    'what the return reports, and the returns run until the corporation is '
    'dissolved and a clearance certificate is issued.'),
   ('There is money sitting in the corporation. Is the year nil?',
    'Only if it earned nothing. Cash in a chequing account that pays no '
    'interest leaves the year nil. The moment it is in anything paying '
    'interest or dividends, the year is an ordinary return at $350.00 plus '
    'HST per year at gondaliyacpa.ca.'),
   ('An orthodontic instalment arrived after I closed. Which year does it hit?',
    'The year it was received. That one year becomes an ordinary return and '
    'the quiet years around it are unaffected.'),
   ('I work as an associate now and bill through the clinic. Am I nil?',
    'The corporation can be, where the clinic pays you personally and nothing '
    'goes through it. What matters is which entity was paid for the '
    'treatment.'),
   ('Does my college registration have anything to do with the T2?',
    'No. Registration and the certificate of authorization are handled by the '
    'regulator on its own cycle, and neither replaces a corporate return.'),
   ('My spouse holds non-voting shares from when the practice ran. Does that matter?',
    'It matters on Schedule 50, where every holding of 10% or more is listed. '
    'Holding the shares is not activity; being paid during the year would be.'),
   ('The buyer still owes me on a promissory note. Is that income?',
    'The principal repayments are not. Interest charged on the note is, and '
    'interest received in a year makes that year an ordinary return.'),
   ('Can the equipment stay on the books if the practice is gone?',
    'It can, and Schedule 8 keeps reporting it until it is sold or written '
    'off. Owning it does not make the year active; selling it does.'),
   ('How far back can the outstanding years be filed?',
    'As far back as they go. Each is its own T2 and T183CORP at $300.00 plus '
    'HST per tax year, prepared together and filed from the earliest.'),
   ('I want to take what is in it out and close the corporation. What first?',
    'The outstanding returns. A clearance certificate will not be issued '
    'while a year is unfiled, and the final T2 is due six months after the '
    'dissolution date.'),
  ],
 },

 'landscaping-corporations': {
  'name':   'Landscaping Corporations',
  'short':  'landscaping corporation',
  'plural': 'landscaping corporations',
  'kw':     'nil t2 for landscaping corporation',
  'title':  'Landscaping Corporation Nil T2 | Years With No Contracts',
  'desc':   'A landscaping corporation with no contracts in a year still '
            'files a T2. Why selling the mowers or the trailer ends the nil '
            'year, and what the filing costs.',

  'h1':   'Nil T2 Filing for Landscaping Corporations',
  'lede': 'Mowers in a locked trailer earn nothing, and the corporation that '
          'owns them keeps reaching year ends anyway. Where no job was '
          'invoiced and nothing was sold, that year costs $300.00 plus HST '
          'per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Landscaping Corporations',
  'intro': (
    'A landscaping corporation that stops taking work does not stop having '
    'tax years. The trailer is parked, the maintenance contracts were not '
    'renewed, nobody was invoiced, and the fiscal year end still arrives with '
    'a return behind it. Those years are $300.00 plus HST per tax year.',
    'Whether the crew was let go, the condo and municipal contracts went to '
    'someone else, the work moved to a new corporation, or you are doing the '
    'odd job in your own name instead, the year is tested against what the '
    'corporation invoiced and against any equipment it sold. The return is '
    'prepared with Schedules 100, 125, 141 and 50 and transmitted '
    'electronically. A year with an invoice or a sale in it goes to the full '
    'service.'),

  'notnil_h': 'What an Unfiled Year Costs a Landscaping Corporation',
  'notnil_boxes': [
    ('An Empty Order Book Is Still a Year',
     'What the return reports changes. That one is owed does not.'),
    ('A Demand Brings a Deadline With It',
     'Until one is issued the filing has no date attached. Afterwards it '
     'does, and the date is the Agency\u2019s to pick.'),
    ('Bidding Again Needs a Clean Record',
     'Property managers and municipalities ask for the corporate standing '
     'before awarding work, and a filing gap shows up there.'),
    ('The Equipment Is Still on the Books',
     'A trailer, a mower fleet and a truck sit on the schedule whether or not '
     'they were used, and they have to be accounted for eventually.'),
  ],
  'notnil_text': (
    'The corporation is usually kept because the equipment is in it, or '
    'because the plan is to take work again when it suits. Both of those '
    'produce tax years, and the gap is what surfaces when the equipment is '
    'finally sold or the corporation wound up.',
    'Each of those years costs $300.00 plus HST per tax year. They are worked '
    'from the oldest forward, because the equipment values closing one return '
    'are the values that open the next.'),

  'sched_h': 'Which T2 Schedules a Landscaping Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'The truck, trailer, mowers and any amount still owing to a shareholder '
     'keep the balance sheet occupied through a year with no work.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Zero on both sides for a year in which no contract was billed and '
     'nothing was claimed against one.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Sits with Schedules 100 and 125 and sets out how the figures were '
     'arrived at and by whom.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Names anyone at 10% or more, usually the one or two owners who were on '
     'the crew themselves.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Goes in with the very first T2 and never afterwards.'),
    ('Schedule 8', 'Capital cost allowance', 'While the equipment is owned',
     'Mowers, blowers, a trailer and a truck remain depreciable property '
     'until they are sold or taken out, used or not.'),
  ],
  'sched_note': 'Source: the Canada Revenue Agency\u2019s schedule '
                'requirements for a T2 return, applied here to a landscaping '
                'corporation that raised no invoice during the year. '
                'Reviewed 20 November 2026.',
  'sched_boxes': [
    ('Selling the Equipment Ends the Nil Year',
     'A trailer or a mower sold is a disposition, reported whether it made '
     'money or lost it, and that puts the year into an ordinary return.'),
    ('Work Done in Your Own Name Is Personal',
     'Where a customer paid you rather than the corporation, the income is '
     'yours to report and the corporate year can still be nil.'),
    ('Plant Stock on Hand Is Not Revenue',
     'Nursery material and materials left in the yard sit on Schedule 100 '
     'until they are used on a job or sold.'),
  ],
  'chk_yes': [
    'No contract or job was invoiced by the corporation in the year',
    'No maintenance or seasonal retainer was billed by it',
    'No piece of equipment or vehicle of its was sold',
    'No account of the corporation was credited with interest',
    'No money left it for an owner, as pay or as a dividend',
  ],
  'chk_no': [
    'An invoice went out, even for a job finished the year before',
    'A mower, trailer or truck was sold or traded in',
    'A retainer or deposit was applied to work in the year',
    'Interest was credited on an account the corporation holds',
    'A customer paid the corporation for materials it had bought',
  ],
  'chk_both': [
    'The return itself, once for every year end the corporation reaches',
    'Authorisation to transmit it, on its own T183CORP',
    'A shareholder listing wherever someone holds a tenth of the shares',
    'The registry filing, which runs on its own calendar',
    'A clearance certificate, before the trailer and mowers come out',
  ],

  'why_h': 'Why Landscaping Corporations Use This Service',
  'why': [
    ('Written for the Year the Trailer Stayed Parked',
     'A year with no contracts, a year the work moved elsewhere, or a year '
     'you worked in your own name. Those are what this fee covers.'),
    ('Dispositions Come Up First',
     'More of these years fail on a mower or a trailer having been sold than '
     'on anything else, which is why that question is asked before a price '
     'is quoted.'),
    ('The Same Price Each Quiet Year',
     'A year with no invoices is $300.00 plus HST per tax year, whether one '
     'year is outstanding or five.'),
    ('Invoicing Years Are Quoted Properly',
     'A year with contract revenue in it is prepared as an ordinary '
     'corporate return rather than squeezed into a nil filing.'),
  ],
  'strip': [
    ('Parked Equipment, Live Obligation',
     'The trailer sitting still has no bearing on the year end arriving.'),
    ('In Date Order, Always',
     'Each return opens on the balances the one before it closed with.'),
    ('From the Truck, If Need Be',
     'Authorising a year takes a phone and a portal, not an office.'),
  ],

  'svc_h': 'What a Landscaping Corporation Usually Needs Next',
  'proc_h': 'How a Landscaping Corporation Files a Nil Year',
  'proc_lede': 'The filing form asks four things, and the first one decides '
               'whether the year qualifies at all.',
  'proc_note': 'One year of bank statements usually settles it:',
  'steps': [
    ('Check What Was Invoiced and What Was Sold',
     'Contracts billed, deposits applied and any equipment disposed of are '
     'all measured before the year is treated as nil.'),
    ('Separate the Corporation From the Person',
     'Jobs paid to you personally are reported on your own return, which can '
     'leave the corporate year with nothing in it.'),
    ('Build Out the T2',
     'Schedules 100, 125 and 141 carry the figures, Schedule 50 the '
     'ownership, Schedule 24 if this is the first return, and Schedule 8 for '
     'as long as the equipment is on the books.'),
    ('Get It Authorised and Away',
     'Nothing transmits without a T183CORP behind it. Once the run is '
     'signed off the returns go together, and confirmation lands by email '
     'inside 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Landscaping Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Charged by the year end rather than the hour: $300.00 plus HST per tax '
    'year, for a year holding neither an invoice nor a disposition. Included '
    'are the T2, the GIFI schedules where required, '
    'Schedule 50, Schedule 24 on a first return, the T183CORP package with '
    'secure e-signing, CPA review before transmission, electronic '
    'transmission by a registered EFILE electronic filer, one corrected '
    'transmission where the Agency rejects the first, and the CRA '
    'confirmation emailed within 3 business days. Where contract revenue or '
    'a disposition turns up, that year is an ordinary corporate return '
    'instead, at $350.00 plus HST per year at gondaliyacpa.ca.'),

  'geo_h': 'Landscaping Corporation Filing Across Canada',
  'cta_h': 'File the Years With No Contracts in Them',

  'faq': [
   ('No contracts came in all year. Is a return still due?',
    'It is. A corporation produces a tax year for as long as it stays '
    'registered, and a year with no work goes in showing no revenue rather '
    'than being left out.'),
   ('I sold the trailer during the year. Is it still nil?',
    'No. A sale is a disposition and goes on the return whether it produced '
    'a gain or a loss, which makes that year an ordinary T2 at $350.00 plus '
    'HST per year at gondaliyacpa.ca.'),
   ('I did a few jobs for cash in my own name. Does that affect the corporation?',
    'Not the corporate year, where the customers paid you rather than the '
    'corporation. That income belongs on your personal return instead.'),
   ('An invoice for last autumn’s work was paid in the new year. Which year?',
    'The year the corporation invoiced and earned it is normally the year it '
    'belongs to. Either way, a year with that invoice in it is not nil.'),
   ('Does idle machinery have to come out of the corporation?',
    'Not at all. It carries on down Schedule 8 at its existing cost for as '
    'long as the corporation owns it, with no effect on whether the year was '
    'nil. Moving it out is what has an effect.'),
   ('The crew was laid off but the payroll account is still open. Does that matter?',
    'Not for whether the T2 is nil, but an open payroll account keeps '
    'producing its own filing obligations alongside the corporate return.'),
   ('We moved the work into a new corporation. Does the old one still file?',
    'Yes, until it is dissolved. Moving the business does not end the old '
    'corporation’s tax years, and anything transferred between them is '
    'reportable in the year it moved.'),
   ('Four years were never filed. Can they go in together?',
    'Yes. Each is its own T2 with its own T183CORP at $300.00 plus HST per '
    'tax year, prepared as a set and transmitted from the oldest.'),
   ('Is the registry annual return the same thing as the T2?',
    'No. The registry filing keeps the corporation in good standing and the '
    'T2 reports its tax year. Both are owed and neither covers the other.'),
   ('What has to happen before the corporation can be wound up?',
    'Every outstanding year goes in, and a final return follows six months '
    'after the dissolution date. Any machinery still owned is treated as '
    'disposed of on the way out, which lands in the year it leaves.'),
  ],
 },

 'staffing-agency-corporations': {
  'name':   'Staffing Agency Corporations',
  'short':  'staffing agency corporation',
  'plural': 'staffing agency corporations',
  'kw':     'nil t2 for staffing agency corporation',
  'title':  'Staffing Agency Corporation Nil T2 | No-Placement Years',
  'desc':   'A staffing corporation with no placements in a year still files '
            'a T2. Why an open payroll account is a separate problem, and '
            'what the nil filing costs.',

  'h1':   'Nil T2 Filing for Staffing Agency Corporations',
  'lede': 'There are no assets to prompt anyone and no crew to pay, but the '
          'year end still arrives. Where no client was invoiced and nothing '
          'inside the corporation earned, the return is $300.00 plus HST per '
          'tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Staffing Agency Corporations',
  'intro': (
    'A staffing corporation has almost nothing in it once the placements '
    'stop. No crew, no equipment, no inventory, and a margin business with '
    'nobody on assignment produces no revenue at all. The tax year still '
    'arrives, and the return behind it is $300.00 plus HST per tax year.',
    'Whether the client list went quiet, the contract-staffing book was wound '
    'down, the recruiters left, or you moved to working as an employee '
    'yourself, the year is tested against client invoices, permanent '
    'placement fees arriving late, and anything retained profit inside the '
    'corporation earned. The return is prepared with Schedules 100, 125, 141 '
    'and 50 and transmitted electronically. A year with a fee in it goes to '
    'the full service.'),

  'notnil_h': 'What an Unfiled Year Costs a Staffing Agency Corporation',
  'notnil_boxes': [
    ('Nobody Placed, Return Still Owed',
     'An empty desk decides the figures in the return. It does not decide '
     'whether there is one.'),
    ('The Payroll Account Is a Separate Trail',
     'An agency that ran payroll usually left the account open, and that '
     'account keeps generating obligations of its own next to the T2.'),
    ('A Demand Names the Day',
     'Left alone the filing has no date on it. A written demand supplies '
     'one, chosen by the Agency rather than by you.'),
    ('Clients Check Standing Before Signing',
     'A master services agreement or a vendor onboarding pack asks for '
     'corporate standing, and an unfiled year shows there.'),
  ],
  'notnil_text': (
    'These corporations are cheap to keep and easy to forget, because there '
    'are no assets to prompt anyone. That is exactly why the unfiled years '
    'accumulate, and why they are usually found during a vendor onboarding '
    'or a wind-up rather than at filing time.',
    'Put a figure on it and each of those years is $300.00 plus HST per tax '
    'year. The retained earnings only reconcile if the set is transmitted '
    'oldest first, so that is how it is done.'),

  'sched_h': 'Which T2 Schedules a Staffing Agency Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Retained profit from the trading years, share capital and any balance '
     'owing to a shareholder keep the balance sheet populated even with no '
     'assets to speak of.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Reports nil placement revenue and nil wage cost for a year in which '
     'nobody was on assignment.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Goes with the two GIFI schedules and states who assembled the figures '
     'and on what basis.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Every holding of 10% or more appears, including a co-founder who has '
     'long since stopped working in the business.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the corporation’s first T2, covering the stub period '
     'from incorporation to its first year end.'),
    ('Schedule 8', 'Capital cost allowance', 'Only where assets are held',
     'An agency with nothing but laptops and a subscription stack may have '
     'no depreciable property left to report at all.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, read against a staffing corporation '
                'that placed nobody during the year. Reviewed '
                '20 November 2026.',
  'sched_boxes': [
    ('A Late Placement Fee Lands in Its Own Year',
     'A permanent placement invoiced last year and paid this year still makes '
     'a year active. Which year depends on when the corporation earned it.'),
    ('Nil Payroll Remittances Are Not the T2',
     'An open payroll account can owe nil remittances and information returns '
     'in a year the corporation itself has no income. Those are separate '
     'filings from the T2.'),
    ('A Credited-Back Placement Reduces Revenue',
     'A hire that did not stick and was credited back comes off revenue in '
     'the year of the credit. It does not turn that year into a nil one.'),
  ],
  'chk_yes': [
    'Not one client invoice was raised by the corporation all year',
    'No permanent placement fee came in, for this year or an earlier one',
    'Nobody drew wages or assignment pay through its payroll',
    'Retained profit inside it was credited with neither interest nor a '
    'dividend',
    'Not a dollar went out to an owner, as pay or as a dividend',
  ],
  'chk_no': [
    'A client paid a placement or margin invoice in the year',
    'A permanent placement fee arrived for a hire made earlier',
    'Wages or assignment pay went out through its payroll',
    'Interest was credited on retained profit held inside it',
    'A client list, contract or goodwill was sold or transferred',
  ],
  'chk_both': [
    'Every year end the corporation reaches produces a return to file',
    'Each of those returns waits on a T183CORP before it can go',
    'Anyone at a tenth of the shares or more is named on Schedule 50',
    'Payroll and sales tax accounts keep their own obligations running',
    'Dissolution waits on a clearance certificate, which waits on the years',
  ],

  'why_h': 'Why Staffing Agency Corporations Use This Service',
  'why': [
    ('Built for the Year With Nobody on Assignment',
     'A quiet client list, a wound-down contract book, or a year you worked '
     'as an employee instead. Those are the years this fee covers.'),
    ('Late Placement Fees Are Checked First',
     'A fee arriving after the work stopped is the usual reason one of these '
     'years is not nil, so it is tested before anything is charged.'),
    ('One Amount Per Quiet Year',
     'A year with no client invoices is $300.00 plus HST per tax year, '
     'however long the run of unfiled years.'),
    ('Trading Years Go to the Full Return',
     'A year with placement revenue in it is prepared as an ordinary '
     'corporate return at the higher fee.'),
  ],
  'strip': [
    ('A Margin Business Owns Nothing',
     'Which is no help at all: the filing follows the entity, not its '
     'assets.'),
    ('Oldest to Newest',
     'Retained earnings only reconcile if the years go in the order they '
     'happened.'),
    ('One Sitting, Every Year',
     'The whole run of authorisations can be dealt with in a single '
     'session.'),
  ],

  'svc_h': 'What a Staffing Agency Corporation Usually Needs Next',
  'proc_h': 'How a Staffing Agency Corporation Files',
  'proc_lede': 'Four steps from the filing form, starting with what the '
               'clients paid.',
  'proc_note': 'The first step is usually answered from one bank feed:',
  'steps': [
    ('Check What Clients Paid It',
     'Margin invoices, permanent placement fees, credits and anything '
     'retained profit earned are all measured before the year is called '
     'nil.'),
    ('Deal With the Payroll Account Separately',
     'An open payroll account is noted so its own obligations are not '
     'mistaken for the corporate return, which stays nil either way.'),
    ('Prepare the Return',
     'Schedules 100, 125, 141 and 50 for the year, with Schedule 24 where '
     'this is the first return.'),
    ('Authorise the Run and Send It',
     'Each year gets its own T183CORP, the set is transmitted, and the '
     'Agency confirms by email inside 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Staffing Agency Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'One year end, one fee: $300.00 plus HST per tax year for a year with no '
    'client invoice in it. What that buys is the T2, the GIFI schedules '
    'where required, Schedule 50, '
    'Schedule 24 on a first return, the T183CORP package with secure '
    'e-signing, CPA review before transmission, electronic transmission by a '
    'registered EFILE electronic filer, one corrected transmission where the '
    'Agency rejects the first, and the CRA confirmation emailed within 3 '
    'business days. A year with placement revenue or investment income in it '
    'is $350.00 plus HST per year at gondaliyacpa.ca.'),

  'geo_h': 'Staffing Corporation Filing Across Canada',
  'cta_h': 'File the Years With Nobody Placed',

  'faq': [
   ('Nobody was placed in the whole year. Is there still a return?',
    'There is. The corporation keeps reaching year ends while it stays in '
    'existence, and the return for an empty year reports no revenue rather '
    'than being left out.'),
   ('A placement fee was invoiced last year and paid this year. Which year?',
    'The year the corporation earned it is normally the year it belongs in. '
    'What is certain is that a year carrying that fee is not nil.'),
   ('Our payroll account is still open. Does that stop the T2 being nil?',
    'No. The corporate return can still be nil while the payroll account '
    'owes nil remittances or information returns. They are separate filings '
    'to separate programs.'),
   ('I took a salaried recruiting job. Does the corporation keep filing?',
    'Yes, until it is dissolved. Your employment income is personal and has '
    'no effect on whether the corporate year is nil.'),
   ('There is retained profit in the corporation. Is the year still nil?',
    'Only where it earned nothing. Cash that pays no interest leaves the '
    'year nil; interest or dividends on it make the year an ordinary return '
    'at $350.00 plus HST per year at gondaliyacpa.ca.'),
   ('A client credited back a placement that did not work out. What happens?',
    'The credit reduces revenue in the year it was given. It does not turn '
    'that year into a nil year, because there was revenue to reduce.'),
   ('We sold the client list to another agency. Is that year nil?',
    'No. Selling a client list or goodwill is a disposition and is reported '
    'in the year it happened, which makes that year a full return.'),
   ('Nobody is left in the company but me. Who signs?',
    'You do, as the authorised signing officer, once for each tax year. '
    'Several years can be signed in one sitting.'),
   ('Five years were never filed. Can they all go in now?',
    'Yes. Each is a separate T2 with its own T183CORP at $300.00 plus HST '
    'per tax year, prepared together and filed from the earliest forward.'),
   ('We want to close the corporation. What has to happen first?',
    'The outstanding returns, then the final T2 within six months of the '
    'dissolution date. No clearance certificate is issued while a year '
    'remains unfiled.'),
  ],
 },

 'hair-salon-corporations': {
  'name':   'Hair Salon Corporations',
  'short':  'hair salon corporation',
  'plural': 'hair salon corporations',
  'kw':     'nil t2 for hair salon corporation',
  'title':  'Hair Salon Corporation Nil T2 | Years After Closing',
  'desc':   'A salon corporation files for every tax year it exists. Why '
            'chair rent ends the nil year, where outstanding gift '
            'certificates sit, and what the filing costs.',

  'h1':   'Nil T2 Filing for Hair Salon Corporations',
  'lede': 'A year with the doors shut is still a tax year. Where no service '
          'was rung through and no chair was rented out, the return is '
          '$300.00 plus HST per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Hair Salon Corporations',
  'intro': (
    'A salon closes faster than its corporation does. The lease ends or is '
    'assigned, the stylists move on, the chairs and basins go into storage or '
    'to a buyer, and the corporation stays on the register with a year end '
    'that keeps arriving. Those years are $300.00 plus HST per tax year.',
    'Whether the shop closed for good, the lease was given up, the business '
    'moved into a new corporation, or you now rent a chair somewhere else in '
    'your own name, the year is tested against services rung through the '
    'corporation, retail product sold, rent collected from stylists, and any '
    'equipment disposed of. The return carries Schedules 100, 125, 141 and 50 '
    'and is transmitted electronically. A year with any of those goes to the '
    'full service.'),

  'notnil_h': 'What an Unfiled Year Costs a Hair Salon Corporation',
  'notnil_boxes': [
    ('Doors Shut, Year Ends Anyway',
     'Closing decides what goes in the return. Dissolving is what stops '
     'there being one.'),
    ('A Demand Supplies the Deadline',
     'Before one arrives the filing is overdue with no date attached. After '
     'it, there is a date, and it is not yours to choose.'),
    ('The Sales Tax Account Is Its Own Thread',
     'A salon that charged sales tax usually left that account open, and it '
     'keeps asking for returns beside the T2.'),
    ('Gift Certificates Were Never Settled',
     'Certificates sold and never redeemed sit as a liability, and nobody '
     'wants to work that out years later with no filings to read.'),
  ],
  'notnil_text': (
    'The corporation tends to be kept because the equipment is in it, because '
    'there may be another shop one day, or because closing it properly never '
    'reached the top of the list. Each year it is kept is a tax year.',
    'Those years run at $300.00 plus HST per tax year. A whole run of them '
    'can be dealt with at once, provided they go across in the order the '
    'shop lived through them.'),

  'sched_h': 'Which T2 Schedules a Hair Salon Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Chairs, basins and dryers, retail stock still in boxes, unredeemed gift '
     'certificates and any shareholder balance all sit on the balance sheet.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Reports nil service revenue and nil expenses for a year in which the '
     'till never opened.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Rides along with the two GIFI schedules, naming whoever put the '
     'figures together.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Names every holder of 10% or more, which for a salon is often two '
     'partners who opened it together.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the first T2 after incorporation and not again.'),
    ('Schedule 8', 'Capital cost allowance', 'While the fit-out is owned',
     'Styling chairs, wash units, dryers and the leasehold improvements stay '
     'depreciable property until they are sold, scrapped or left behind.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, read against a salon corporation '
                'whose till stayed shut for the year. Reviewed '
                '20 November 2026.',
  'sched_boxes': [
    ('Renting Chairs Out Is Income',
     'Where stylists pay the corporation for a chair, that is rent received '
     'and the corporation is not nil for that year. A corporation collecting '
     'chair rent files a full return.'),
    ('Renting a Chair Yourself Is Personal',
     'Where you pay another salon for a chair and are paid directly, the '
     'money is yours to report and the corporate year can be nil.'),
    ('Unredeemed Certificates Are a Liability',
     'A gift certificate sold in an earlier year sits on Schedule 100 until '
     'it is redeemed or written off. Carrying it does not make the year '
     'active.'),
  ],
  'chk_yes': [
    'No service was rung through the corporation during the year',
    'No retail product was sold by it',
    'No stylist or tenant paid it for the use of a chair or room',
    'No chair, dryer or fixture of its was sold',
    'Nothing it holds was credited with interest or a dividend',
  ],
  'chk_no': [
    'A stylist paid the corporation chair rent for any part of the year',
    'A gift certificate was redeemed for a service in the year',
    'Retail stock was sold off, in the shop or online',
    'The fit-out, the equipment or the client list was sold',
    'The lease was assigned for a payment to the corporation',
  ],
  'chk_both': [
    'One return per year end, for as long as the corporation is on the '
    'register',
    'A signature authorising each return before it can be transmitted',
    'A listing of anyone holding a tenth of the shares or more',
    'The sales tax account either filed or properly closed',
    'Clearance first, then the chairs come out and the corporation goes',
  ],

  'why_h': 'Why Hair Salon Corporations Use This Service',
  'why': [
    ('Written for the Years After the Doors Shut',
     'A closed shop, an assigned lease, or a year you worked out of someone '
     'else’s chair. Those are the years this fee covers.'),
    ('Chair Rent Is the First Thing Checked',
     'Rent from a stylist is the most common reason a quiet salon year turns '
     'out not to be nil, so it is tested before anything is charged.'),
    ('One Amount, Each Quiet Year',
     'A year with nothing rung through is $300.00 plus HST per tax year, '
     'however far back the shop closed.'),
    ('Trading Years Are Quoted as Trading Years',
     'A year with service revenue, retail sales or chair rent in it is '
     'prepared as an ordinary corporate return at the higher fee.'),
  ],
  'strip': [
    ('Shut Is Not Struck Off',
     'The doors closing and the corporation ending are different days.'),
    ('In the Order They Happened',
     'Stock and fit-out values only carry through if the years do.'),
    ('No Envelope, No Stamp',
     'Authorising a year happens in a browser.'),
  ],

  'svc_h': 'What a Hair Salon Corporation Usually Needs Next',
  'proc_h': 'How a Hair Salon Corporation Files a Nil Year',
  'proc_lede': 'Four steps from the filing form, with the chair rent and '
               'takings test first.',
  'proc_note': 'The first step rules out most of the doubt:',
  'steps': [
    ('Check the Takings and Any Chair Rent',
     'Service revenue, retail sales, chair or room rent and any equipment '
     'sold are measured before the year is treated as nil.'),
    ('Separate What Was Yours From the Corporation’s',
     'Where you were paid directly for working elsewhere, that is personal '
     'income and the corporate year can still be nil.'),
    ('Prepare the Return',
     'Schedules 100, 125, 141 and 50 for the year, with Schedule 24 on a '
     'first return and Schedule 8 while the fit-out is owned.'),
    ('Authorise and Send',
     'Each year is authorised on its own T183CORP, the returns are '
     'transmitted, and the Agency confirms by email inside 3 business '
     'days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Hair Salon Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Nothing rung through and no chair rent makes the year a $300.00 plus '
    'HST per tax year filing. Against that fee sit the T2, the GIFI '
    'schedules where required, '
    'Schedule 50, Schedule 24 on a first return, the T183CORP package with '
    'secure e-signing, CPA review before transmission, electronic '
    'transmission by a registered EFILE electronic filer, one corrected '
    'transmission where the Agency rejects the first, and the CRA '
    'confirmation emailed within 3 business days. A year with takings, retail '
    'sales or chair rent in it is $350.00 plus HST per year at '
    'gondaliyacpa.ca.'),

  'geo_h': 'Salon Corporation Filing Across Canada',
  'cta_h': 'File the Years Since the Shop Closed',

  'faq': [
   ('The salon closed two years ago. Does the corporation still file?',
    'Yes, for every tax year it continues to exist. Closing the shop ends the '
    'trading, not the corporation, and the returns run until it is '
    'dissolved.'),
   ('I rent chairs to two stylists. Is the corporation nil?',
    'No. Chair rent paid to the corporation is income to it, so it is a '
    'rental corporation for that year and files a full T2 at $350.00 plus '
    'HST per year at gondaliyacpa.ca.'),
   ('I rent a chair at someone else’s salon now. Is my corporation nil?',
    'It can be, where the clients pay you directly and nothing goes through '
    'the corporation. The test is which one was paid.'),
   ('We still have unredeemed gift certificates out there. Does that matter?',
    'Not for whether the year is nil. They sit as a liability on the balance '
    'sheet until redeemed or written off. A certificate redeemed for a '
    'service makes that year active.'),
   ('The chairs and dryers are in storage. Does holding them count?',
    'No. Schedule 8 keeps reporting them while they are owned, and holding '
    'them is not activity. Selling one is.'),
   ('We sold off the leftover retail stock online. Is the year nil?',
    'No. Those are sales by the corporation, however small, and they put a '
    'figure on Schedule 125.'),
   ('The landlord paid us to take the lease back. What is that?',
    'A payment received by the corporation for giving up the lease, which is '
    'reportable in the year it was received and makes that year a full '
    'return.'),
   ('Our sales tax account is still open. Does that make the T2 non-nil?',
    'No. The corporate return can be nil while the sales tax account owes '
    'its own returns. They are separate filings and both have to be dealt '
    'with.'),
   ('Three years were never filed. Can they all go in?',
    'Yes. Each is its own T2 and T183CORP at $300.00 plus HST per tax year, '
    'prepared as a set and filed from the earliest.'),
   ('We want the equipment out and the corporation closed. What order?',
    'Outstanding returns first. Taking the equipment out is a disposition to '
    'report, and no clearance certificate is issued while a year is '
    'missing.'),
  ],
 },

 'gym-corporations': {
  'name':   'Gym Corporations',
  'short':  'gym corporation',
  'plural': 'gym corporations',
  'kw':     'nil t2 for gym corporation',
  'title':  'Gym Corporation Nil T2 | Years After the Doors Closed',
  'desc':   'A gym corporation files for every tax year it exists. Why one '
            'membership still billing ends the nil year, and what the filing '
            'costs per year.',

  'h1':   'Nil T2 Filing for Gym Corporations',
  'lede': 'The thing that catches people out is the billing. One membership '
          'still renewing on its own is revenue, and the year is not nil. '
          'Where the billing truly stopped, the return is $300.00 plus HST '
          'per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Gym Corporations',
  'intro': (
    'A gym can be shut and the corporation still be collecting. Recurring '
    'membership billing has a habit of running on past the closing date, and '
    'any year it ran is a year with revenue in it. Where the billing was '
    'genuinely switched off and nothing else came in, the return is $300.00 '
    'plus HST per tax year.',
    'Whether the lease ended, the location was handed to a new operator, the '
    'business was moved into another corporation, or the equipment went into '
    'storage while you decide, the year is tested against membership and drop-'
    'in revenue, anything a trainer paid for use of the floor, and any '
    'equipment sold off. The return is prepared with Schedules 100, 125, 141 '
    'and 50 and transmitted electronically. A year with revenue in it goes to '
    'the full service.'),

  'notnil_h': 'What an Unfiled Year Costs a Gym Corporation',
  'notnil_boxes': [
    ('The Corporation Outlasts the Location',
     'Losing the premises ends the gym. The corporation goes on producing tax '
     'years until it is dissolved.'),
    ('The Longer the Gap, the Bigger the Catch-Up',
     'Nothing prompts a quiet corporation, so these gaps tend to be found at '
     'four or five years rather than one.'),
    ('Memberships May Still Be Running',
     'Billing that nobody switched off puts revenue in a year everyone '
     'assumed was empty, which is worse than a nil year filed late.'),
    ('Equipment Has to Be Accounted For',
     'Racks, treadmills and the fit-out sit on the schedules until they are '
     'sold or written off, and that reckoning needs the years filed.'),
  ],
  'notnil_text': (
    'Most of these corporations are kept because the equipment is in them, or '
    'because the plan is a second location one day. Either way the year ends '
    'arrive, and the catch-up is usually triggered by selling the racks or '
    'trying to close the company.',
    'Where the year holds nothing, it is $300.00 plus HST per tax year. '
    'Several years can be prepared at once, and they go across oldest first '
    'so each equipment balance opens where the last one closed.'),

  'sched_h': 'Which T2 Schedules a Gym Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Equipment, leasehold improvements, unused memberships still owed and '
     'any shareholder balance are all on the balance sheet in a quiet year.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Nil membership revenue and nil expenses, for a year in which nothing '
     'was billed and nothing claimed.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Attached to the two GIFI schedules; it says who put the figures '
     'together and how.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Anyone holding 10% or more of the shares, which in a gym is often two '
     'or three founding partners.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'On the very first T2 after incorporation, covering the period up to '
     'that first year end.'),
    ('Schedule 8', 'Capital cost allowance', 'While the equipment is held',
     'Racks, cardio machines, mats and the fit-out are depreciable property '
     'until they are sold, scrapped or taken out of the corporation.'),
  ],
  'sched_note': 'Source: the T2 schedule requirements set by the Canada '
                'Revenue Agency, applied to a gym corporation that billed no '
                'member during the tax year. Reviewed 23 November 2026.',
  'sched_boxes': [
    ('One Live Membership Ends It',
     'Recurring billing does not need a staffed gym to keep charging. A '
     'single membership collected in the year puts revenue on Schedule 125.'),
    ('Unused Memberships Are a Liability',
     'Months paid for and never used sit on Schedule 100 as something owed, '
     'not as income, until they are used or written off.'),
    ('Training Income May Be Personal',
     'Where a client paid you directly for a session, that is yours to '
     'report. The corporate year can still be nil.'),
  ],
  'chk_yes': [
    'No membership, drop-in or class fee reached the corporation',
    'No trainer or tenant paid it to use the floor or a room',
    'No merchandise, supplement or drink was sold through it',
    'No piece of equipment belonging to it was sold',
    'No interest or dividend was credited to anything it holds',
  ],
  'chk_no': [
    'A recurring membership charge went through in the year',
    'A trainer paid rent for use of the space',
    'Leftover stock or equipment was sold off',
    'A member was charged a cancellation or freeze fee',
    'The location, its lease or its member list changed hands for value',
  ],
  'chk_both': [
    'File one T2 for each year end that falls while the company exists',
    'Sign a T183CORP for every one of those returns',
    'Report any 10% shareholding on Schedule 50',
    'Keep the registry annual return going on its own schedule',
    'Obtain clearance before the equipment leaves and the company closes',
  ],

  'why_h': 'Why Gym Corporations Use This Service',
  'why': [
    ('Meant for the Post-Closure Years',
     'A shut location, a handed-over lease, equipment in storage: those years '
     'are what this fee is for.'),
    ('The Billing Is Checked Before the Price',
     'Whether any membership was still collecting is settled first, because '
     'it is the most common reason one of these years is not nil.'),
    ('A Set Amount, Year by Year',
     'Each empty year is $300.00 plus HST per tax year. Five of them cost '
     'five times that and nothing more.'),
    ('Collecting Years Are Priced as Such',
     'A year with membership revenue in it is prepared as an ordinary '
     'corporate return rather than filed as nil.'),
  ],
  'strip': [
    ('Closed Premises, Open Obligation',
     'The landlord has the keys. The Agency still expects the return.'),
    ('Sequence Matters',
     'Equipment values only reconcile if the years are filed in order.'),
    ('Signed From Anywhere',
     'The authorisation for each year is handled in a secure portal.'),
  ],

  'svc_h': 'What a Gym Corporation Usually Needs Next',
  'proc_h': 'How a Gym Corporation Files a Nil Year',
  'proc_lede': 'Four steps. The first is a question about the billing, and it '
               'decides everything after it.',
  'proc_note': 'A merchant statement usually answers step one:',
  'steps': [
    ('Confirm the Billing Was Off',
     'Membership runs, drop-in takings, cancellation fees and floor rent are '
     'all checked for the year before it is treated as nil.'),
    ('Account for Anything Sold',
     'Equipment sold or traded is a disposition and belongs in its year, '
     'which rules that year out of the nil price.'),
    ('Assemble the T2',
     'Schedules 100, 125, 141 and 50, plus Schedule 24 on a first return and '
     'Schedule 8 while the equipment is still owned.'),
    ('Authorise, Then Transmit',
     'A T183CORP covers one year. Once the set is authorised the returns go '
     'across and the Agency confirms by email inside 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Gym Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Where the billing was off and nothing was sold, the year costs $300.00 '
    'plus HST per tax year. That figure covers the T2, the GIFI schedules '
    'where required, Schedule 50, Schedule 24 on a first return, the '
    'T183CORP package with secure e-signing, CPA review before transmission, '
    'electronic transmission by a registered EFILE electronic filer, one '
    'corrected transmission where the Agency rejects the first, and the CRA '
    'confirmation emailed within 3 business days. Find a membership run or a '
    'sale in the year and it becomes an ordinary corporate return at $350.00 '
    'plus HST per year at gondaliyacpa.ca.'),

  'geo_h': 'Gym Corporation Filing Across Canada',
  'cta_h': 'File the Years the Lights Were Off',

  'faq': [
   ('The gym closed last year. Is the corporation finished with returns?',
    'Not until it is dissolved. Closing the location ends the business, and '
    'the corporation keeps reaching year ends and owing a return for each '
    'one.'),
   ('Two memberships were still being charged. Does that matter?',
    'It does. Any membership collected in the year is revenue to the '
    'corporation, so that year is an ordinary return at $350.00 plus HST per '
    'year at gondaliyacpa.ca rather than a nil filing.'),
   ('I train a few clients privately now. Does that affect the corporation?',
    'Not where the clients pay you rather than the corporation. That income '
    'is reported on your personal return and the corporate year can be nil.'),
   ('We sold the treadmills and racks. Which year does that land in?',
    'The year of the sale, as a disposition, whether it produced a gain or a '
    'loss. The years before and after can still be nil.'),
   ('People paid for a year of membership they never used. Is that income?',
    'It was income when it was earned, and what is left unused sits on the '
    'balance sheet as an amount owed. Carrying that balance does not make a '
    'later year active.'),
   ('A member was charged a cancellation fee after we closed. Nil or not?',
    'Not nil for that year. A cancellation or freeze fee collected by the '
    'corporation is its revenue, however small the amount.'),
   ('The equipment is in a storage unit we pay for personally. Does that count?',
    'A cost you carried yourself and the corporation did not claim leaves the '
    'corporate year with nothing in it either way.'),
   ('The lease was taken over by another operator. Is the year nil?',
    'Only if nothing was paid to the corporation for it. A payment to assume '
    'the lease, or for the equipment that came with it, is reportable in the '
    'year received.'),
   ('There are five unfiled years. How is that handled?',
    'As a set. Each year is its own T2 and T183CORP at $300.00 plus HST per '
    'tax year, transmitted from the earliest year forward.'),
   ('Can the corporation be dissolved with years outstanding?',
    'No. They go in first, a final return follows six months after the '
    'dissolution date, and no clearance certificate is issued while a year is '
    'missing.'),
  ],
 },

 'daycare-corporations': {
  'name':   'Daycare Corporations',
  'short':  'daycare corporation',
  'plural': 'daycare corporations',
  'kw':     'nil t2 for daycare corporation',
  'title':  'Daycare Corporation Nil T2 | Years With No Children',
  'desc':   'A daycare corporation owes a T2 for every year it exists, '
            'licence or no licence. When a year with no enrolment is nil, and '
            'what funding payments do to it.',

  'h1':   'Nil T2 Filing for Daycare Corporations',
  'lede': 'Holding the licence is not the same as running the centre. In a '
          'year with no children enrolled and no funding received, the '
          'return is $300.00 plus HST per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Daycare Corporations',
  'intro': (
    'A childcare corporation can sit between operating periods for a long '
    'while. The licence may be held or surrendered, the rooms may be leased '
    'or empty, and the corporation keeps arriving at year ends that each owe '
    'a return. Those years are $300.00 plus HST per tax year.',
    'Whether the centre closed, enrolment never restarted after a move, the '
    'operation was transferred to another corporation, or the licence lapsed '
    'while the premises sat, the year is tested against parent fees, any '
    'government childcare funding received, and anything sold out of the '
    'rooms. The return carries Schedules 100, 125, 141 and 50 and is '
    'transmitted electronically. A year with fees or funding in it goes to '
    'the full service.'),

  'notnil_h': 'What an Unfiled Year Costs a Daycare Corporation',
  'notnil_boxes': [
    ('The Licence and the Return Are Separate',
     'Surrendering a licence stops the childcare. It does nothing at all to '
     'the corporate tax years.'),
    ('A Demand Can Reach Back Years',
     'Where several years are outstanding the Agency can call for all of them '
     'in one written demand.'),
    ('Reopening Means Filing First',
     'A corporation with holes in its filing record is a poor vehicle for a '
     'new licence application or a new lease.'),
    ('Funding Bodies Read the Record',
     'Where public money was involved, the corporate filings tend to be '
     'looked at, and gaps draw questions.'),
  ],
  'notnil_text': (
    'These corporations are often kept deliberately, because the licence took '
    'years to obtain or because another site is being looked for. Each year '
    'of waiting is a tax year with a return behind it.',
    'A year with no enrolment and no funding is $300.00 plus HST per tax '
    'year. Outstanding years are worked as one job and sent from the oldest, '
    'so the balances follow through correctly.'),

  'sched_h': 'Which T2 Schedules a Daycare Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Classroom and playground equipment, leasehold improvements, deposits '
     'held and any shareholder balance stay on the balance sheet.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Nil fee income and nil wage cost, for a year in which no child was '
     'enrolled.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Goes in with the two GIFI schedules and records the basis the figures '
     'were prepared on.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Each holder of 10% or more, which for a centre is frequently a couple '
     'or two operating families.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'With the first T2 only, covering the stub period from incorporation.'),
    ('Schedule 8', 'Capital cost allowance', 'While the fit-out is owned',
     'Playground structures, cots, shelving and leasehold improvements are '
     'depreciable property until disposed of.'),
  ],
  'sched_note': 'Source: what the Canada Revenue Agency requires on a T2 '
                'return, taken here against a childcare corporation that '
                'enrolled nobody for the whole of the tax year. Reviewed '
                '23 November 2026.',
  'sched_boxes': [
    ('Funding Received Is Revenue',
     'A government childcare funding or wage-enhancement payment received by '
     'the corporation is its income for the year it arrives, and the year is '
     'not nil.'),
    ('A Held Licence Is Not Activity',
     'Keeping a licence while the rooms are empty puts nothing on Schedule '
     '125. Enrolling one child does.'),
    ('Subletting the Rooms Is Rent',
     'Where another operator pays the corporation for the space, that is '
     'rent received and the corporation is not nil for that year.'),
  ],
  'chk_yes': [
    'No parent fee was received by the corporation in the year',
    'No government childcare funding or subsidy reached it',
    'No other operator paid it for use of the rooms',
    'No equipment or furnishing of its was sold',
    'No interest or dividend was posted to an account in its name',
  ],
  'chk_no': [
    'A parent fee or deposit was applied to care given in the year',
    'A funding, subsidy or wage-enhancement payment arrived',
    'Rent was collected from another operator using the space',
    'Playground or classroom equipment was sold off',
    'The centre, its licence capacity or its goodwill changed hands',
  ],
  'chk_both': [
    'A T2 return for every tax year ending while the corporation lives',
    'One T183CORP authorisation per return, before it can be sent',
    'Schedule 50 disclosure at the 10% threshold',
    'The corporate registry filing, which is not the tax return',
    'A clearance certificate, as the last step before dissolution',
  ],

  'why_h': 'Why Daycare Corporations Use This Service',
  'why': [
    ('For the Years Between Centres',
     'A closed site, a lapsed licence, a search for new premises. Those are '
     'the years this fee covers.'),
    ('Funding Is the First Question Asked',
     'Public childcare money arriving in a quiet year is the usual reason one '
     'is not nil, so it is checked before a price is given.'),
    ('The Same Fee Each Empty Year',
     'A year with no enrolment and no funding is $300.00 plus HST per tax '
     'year, whatever the length of the run.'),
    ('Operating Years Leave This Page',
     'Find a fee or a funding payment and the year belongs to the full '
     'corporate service, priced on what it actually contains.'),
  ],
  'strip': [
    ('Licence Down, Returns Up',
     'Giving up the licence leaves the filing obligation exactly where it '
     'was.'),
    ('From the Oldest Forward',
     'The set is transmitted in date order so each opening balance agrees.'),
    ('Signed in a Browser',
     'Nothing in this needs an envelope or a scanner.'),
  ],

  'svc_h': 'What a Daycare Corporation Usually Needs Next',
  'proc_h': 'How a Daycare Corporation Files',
  'proc_lede': 'The filing form asks four things. Fees and funding are asked '
               'about first, because they settle the rest.',
  'proc_note': 'Step one is usually a short answer:',
  'steps': [
    ('Test for Fees and Funding',
     'Parent fees, subsidies, wage-enhancement money and rent from another '
     'operator are all measured before the year is called nil.'),
    ('Fix the Year End on Record',
     'A childcare corporation often runs a year end set around the programme '
     'year. It has to agree with the Agency record to transmit.'),
    ('Build the Return Out',
     'Two GIFI schedules and the notes checklist carry the figures. '
     'Schedule 50 carries the ownership, Schedule 24 joins a first filing, '
     'and Schedule 8 stays on while the rooms are still fitted out.'),
    ('Authorise, Then Let Them Go',
     'Nothing leaves without a signed T183CORP behind it. Once the run is '
     'authorised the Agency comes back by email, usually well inside 3 '
     'business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Daycare Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Count the programme years with nobody enrolled and multiply: each one '
    'is $300.00 plus HST per tax year. Each of those fees carries the T2, '
    'the GIFI schedules where required, Schedule 50, '
    'Schedule 24 on a first return, the T183CORP package with secure '
    'e-signing, CPA review before transmission, electronic transmission by a '
    'registered EFILE electronic filer, one corrected transmission where the '
    'Agency rejects the first, and the CRA confirmation emailed within 3 '
    'business days. Where parent fees, funding or rent turn up in the year, '
    'it is an ordinary corporate return at $350.00 plus HST per year at '
    'gondaliyacpa.ca.'),

  'geo_h': 'Childcare Corporation Filing Across Canada',
  'cta_h': 'File the Years the Rooms Were Empty',

  'faq': [
   ('We surrendered the licence. Does the corporation stop filing?',
    'No. The licence governs childcare and the T2 governs the corporation. '
    'Returns keep falling due until the corporation itself is dissolved.'),
   ('A funding payment came through after we closed. Is the year nil?',
    'No. Money received by the corporation is its income in the year it '
    'arrives, so that year is an ordinary return at $350.00 plus HST per year '
    'at gondaliyacpa.ca.'),
   ('Another operator rents the rooms from us now. What does that make us?',
    'A corporation collecting rent, which is not nil for any year it '
    'collected. That year is a full T2 with income to report.'),
   ('I now work as an employee at someone else’s centre. Does that change it?',
    'Not the corporate year. Your wages are personal income and have no '
    'bearing on whether the corporation had a nil year.'),
   ('The playground equipment is still in the yard. Does holding it count?',
    'No. It carries on down Schedule 8 while the corporation owns it. '
    'Selling it is what puts a figure in a year.'),
   ('Parents left deposits we never used. Where do those sit?',
    'On the balance sheet as an amount owed, until they are applied to care '
    'or refunded. Holding them is not activity.'),
   ('We transferred the operation to a new corporation. Does the old one file?',
    'Yes, for as long as it exists, and anything transferred between the two '
    'is reportable in the year it moved.'),
   ('Our fiscal year end is in August, not December. Is that a problem?',
    'Not if it matches what the Agency holds. A mismatch is the usual cause '
    'of a rejected transmission.'),
   ('Three years were missed. Can they be dealt with together?',
    'They can. Every year stands on its own at $300.00 plus HST per tax year '
    'with its own authorisation, and the set is worked from the oldest so the '
    'balances follow through.'),
   ('In what order does winding the corporation up happen?',
    'Returns, then dissolution, then a final T2 within six months of that '
    'date. The certificate that releases the corporation is withheld for as '
    'long as any year is still unfiled.'),
  ],
 },

 'amazon-fba-corporations': {
  'name':   'Amazon FBA Corporations',
  'short':  'Amazon FBA corporation',
  'plural': 'Amazon FBA corporations',
  'kw':     'nil t2 for amazon fba corporation',
  'title':  'Amazon FBA Corporation Nil T2 | Dormant Seller Years',
  'desc':   'An FBA corporation files a T2 for every year it exists. Why '
            'stock left in a fulfilment centre keeps selling, and what a nil '
            'year costs.',

  'h1':   'Nil T2 Filing for Amazon FBA Corporations',
  'lede': 'Stock left in a fulfilment centre does not stop selling because '
          'you stopped looking. Where nothing sold and nothing was '
          'disbursed, the year is $300.00 plus HST per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Amazon FBA Corporations',
  'intro': (
    'An FBA seller goes quiet differently from a shop. There is no lease to '
    'end and nobody to let go, so the corporation carries on with a '
    'marketplace account attached to it and a year end arriving every twelve '
    'months. Where the year holds nothing, it is $300.00 plus HST per tax '
    'year.',
    'Whether the listings were taken down, the account was deactivated, the '
    'remaining units were removed or disposed of, or the brand was moved into '
    'a different corporation, the year is tested against marketplace sales, '
    'disbursements received, reimbursements for lost units and anything the '
    'held funds earned. Schedules 100, 125, 141 and 50 are prepared and the '
    'return is transmitted electronically. A year with a disbursement in it '
    'goes to the full service.'),

  'notnil_h': 'What an Unfiled Year Costs an Amazon FBA Corporation',
  'notnil_boxes': [
    ('No Storefront, Same Obligation',
     'Nothing physical closes when an FBA business stops. The corporation '
     'keeps producing tax years regardless.'),
    ('An Unfiled Year Does Not Expire',
     'There is no point at which an outstanding return stops being '
     'outstanding. It waits, and a written demand puts a date on it.'),
    ('The Marketplace Keeps Its Own Records',
     'Sales and disbursements are documented by the platform whether or not '
     'the corporation reported them.'),
    ('Reopening or Selling Needs the Years',
     'Anyone buying a brand, or a lender behind them, reads the corporate '
     'filings before terms are agreed.'),
  ],
  'notnil_text': (
    'The pattern here is a seller who stopped paying attention rather than '
    'one who closed anything. The corporation stays, the account stays '
    'attached to it, and the unfiled years build up quietly.',
    'Each genuinely empty year is $300.00 plus HST per tax year. Where there '
    'are several, they are prepared together and transmitted oldest first so '
    'the inventory and retained earnings carry through.'),

  'sched_h': 'Which T2 Schedules an Amazon FBA Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Unsold units still at the fulfilment centre, any balance held by the '
     'marketplace, share capital and shareholder loans all appear here.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Nil sales and nil fees, for a year in which no order was fulfilled and '
     'nothing was claimed.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Filed with the two GIFI schedules; it names who compiled them and on '
     'what basis.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Any holder of 10% or more, which for a single-operator seller is one '
     'name.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Attached to the corporation’s first T2 and never repeated.'),
    ('Schedule 8', 'Capital cost allowance', 'Only where assets are held',
     'A photography setup, a laptop or packing equipment, where the '
     'corporation owns any. Many FBA sellers own none at all.'),
  ],
  'sched_note': 'Source: the Canada Revenue Agency’s T2 schedule '
                'requirements, read against a marketplace seller corporation '
                'that fulfilled no order in the tax year. Reviewed '
                '23 November 2026.',
  'sched_boxes': [
    ('Units in a Warehouse Still Sell',
     'An active listing against remaining stock can fulfil an order without '
     'anyone touching the account. One sale makes the year an ordinary '
     'return.'),
    ('Unsold Stock Is Not Income',
     'Inventory sitting at a fulfilment centre is an asset on Schedule 100. '
     'It produces nothing until it is sold or written off.'),
    ('A Reimbursement Is Still Receipt',
     'Money credited for units lost or damaged in the warehouse is received '
     'by the corporation, and it lands in the year it was credited.'),
  ],
  'chk_yes': [
    'No order was fulfilled for the corporation in the year',
    'No disbursement was paid out to it from the marketplace',
    'No reimbursement for lost or damaged units was credited',
    'No remaining stock was sold off or liquidated elsewhere',
    'Nothing the corporation holds was credited with interest',
  ],
  'chk_no': [
    'An order shipped from remaining stock, however few units',
    'A disbursement landed in the corporate bank account',
    'The platform credited a reimbursement or a refund adjustment',
    'Leftover inventory was sold in bulk to a liquidator',
    'The brand, the listings or the account itself was sold',
  ],
  'chk_both': [
    'One return per tax year, for as long as the corporation is registered',
    'A T183CORP signed off before each of those returns can be transmitted',
    'Schedule 50 wherever a shareholding reaches one tenth',
    'Any sales tax registration dealt with on its own cycle',
    'Clearance ahead of dissolving, which the unfiled years block',
  ],

  'why_h': 'Why Amazon FBA Corporations Use This Service',
  'why': [
    ('Written for the Dormant Seller',
     'Delisted, deactivated, or left running with nothing moving. Those are '
     'the years this fee is for.'),
    ('Disbursements Are Checked First',
     'A trickle of sales from leftover stock is the usual reason one of these '
     'years is not nil, so it is settled before a price is quoted.'),
    ('A Single Figure Per Year',
     'An empty year is $300.00 plus HST per tax year, with no hourly billing '
     'and no minimum number of years.'),
    ('Selling Years Are Routed On',
     'A year with disbursements in it is prepared as an ordinary corporate '
     'return at the higher fee.'),
  ],
  'strip': [
    ('Dormant Is Not Closed',
     'An account nobody logs into is still attached to a live corporation.'),
    ('Earliest First, Always',
     'Inventory values only reconcile when the years go in date order.'),
    ('Entirely Online',
     'Authorising each year takes a browser and nothing else.'),
  ],

  'svc_h': 'What an Amazon FBA Corporation Usually Needs Next',
  'proc_h': 'How an Amazon FBA Corporation Files',
  'proc_lede': 'Four steps from the filing form. The first one is a look at '
               'the payout history.',
  'proc_note': 'One year of settlement reports covers most of it:',
  'steps': [
    ('Pull the Disbursement History',
     'Sales, payouts, reimbursements and refund adjustments for the year are '
     'all measured before it is treated as nil.'),
    ('Value What Is Still in the Warehouse',
     'Remaining units are an asset rather than income, and they belong on the '
     'balance sheet at cost.'),
    ('Draft the Return',
     'Schedules 100, 125, 141 and 50, with Schedule 24 where it is the first '
     'return and Schedule 8 only if the corporation owns assets.'),
    ('Sign Off and Submit',
     'Each year carries its own T183CORP. The set is submitted '
     'electronically and the Agency confirms by email inside 3 business '
     'days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for an Amazon FBA Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'A year with no disbursement in it is $300.00 plus HST per tax year. '
    'Behind that figure sit the T2, the GIFI schedules where required, '
    'Schedule 50, Schedule 24 on a first return, the T183CORP package with '
    'secure e-signing, CPA review before transmission, electronic '
    'transmission by a registered EFILE electronic filer, one corrected '
    'transmission where the Agency rejects the first, and the CRA '
    'confirmation emailed within 3 business days. A year with marketplace '
    'sales or investment income in it is $350.00 plus HST per year at '
    'gondaliyacpa.ca.'),

  'geo_h': 'Marketplace Seller Corporation Filing Across Canada',
  'cta_h': 'File the Years Nothing Shipped',

  'faq': [
   ('I stopped selling two years ago but never closed the company. What now?',
    'The returns for those years are still due, and they can be prepared as a '
    'set. The corporation goes on producing tax years until it is dissolved.'),
   ('A few units sold from leftover stock. Is the year still nil?',
    'No. Any sale is revenue to the corporation, so that year is an ordinary '
    'return at $350.00 plus HST per year at gondaliyacpa.ca.'),
   ('There is stock sitting in a fulfilment centre. Does holding it count?',
    'Holding it does not. It is an asset on the balance sheet at cost until '
    'it is sold, written off or removed.'),
   ('The platform reimbursed us for units it lost. Where does that go?',
    'Into the year it was credited, as money received by the corporation. '
    'That year is not nil.'),
   ('Our account was deactivated. Does that end the obligation?',
    'No. A deactivated marketplace account has no effect on the corporate '
    'tax years, which keep arriving.'),
   ('I moved the brand into a new corporation. Does the old one still file?',
    'Yes, until it is dissolved, and the transfer itself is reportable in the '
    'year it happened.'),
   ('A storage fee was charged while nothing sold. Is the year nil?',
    'It can be, provided the corporation claimed nothing and received '
    'nothing. A fee charged against a zero balance does not create income.'),
   ('I sell on my own account now, not the corporation’s. Does that matter?',
    'Not to the corporate year. What the corporation did not receive is not '
    'its income, and the year can be nil.'),
   ('Four years were never filed. Is there a limit?',
    'No limit. Each is its own T2 with its own T183CORP at $300.00 plus HST '
    'per tax year, sent from the earliest forward.'),
   ('How do we close the corporation for good?',
    'File the outstanding years, then a final T2 within six months of '
    'dissolution. A clearance certificate is not issued while a year is '
    'outstanding.'),
  ],
 },

 'crypto-trading-corporations': {
  'name':   'Crypto Trading Corporations',
  'short':  'crypto trading corporation',
  'plural': 'crypto trading corporations',
  'kw':     'nil t2 for crypto trading corporation',
  'title':  'Crypto Trading Corporation T2 | When a Year Is Not Nil',
  'desc':   'A corporation that traded, swapped or staked crypto in a year is '
            'not nil. The narrow case where a holding year is, and what the '
            'return costs.',

  'h1':   'Nil T2 Filing for Crypto Trading Corporations',
  'lede': 'A corporation that traded, swapped or staked in the tax year is '
          'not nil for that year. Where the wallet only sat there, the '
          'return is $300.00 plus HST per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Crypto Trading Corporations',
  'intro': (
    'The part that decides it comes first. A trading or investment '
    'corporation is not a nil corporation in any year it earned, and with '
    'crypto that bar is low: a swap of one coin for another is a disposition, '
    'and staking or lending pays without any trade at all. Any of those makes '
    'the year a full T2 with income to report, at $350.00 plus HST per year '
    'at gondaliyacpa.ca.',
    'The nil case is real but narrow. It is a complete tax year in which the '
    'corporation bought nothing, sold nothing, swapped nothing, staked '
    'nothing and was paid nothing, with the holdings sitting untouched in a '
    'wallet from one year end to the next. Where the year genuinely looks '
    'like that, it is $300.00 plus HST per tax year, prepared with Schedules '
    '100, 125, 141 and 50 and transmitted electronically.'),

  'notnil_h': 'What an Unfiled Year Costs a Crypto Trading Corporation',
  'notnil_boxes': [
    ('A Trading Year Is Never Nil',
     'One swap, one sale or one staking reward and the year is an ordinary '
     'return. This is tested first and it is not a matter of judgement.'),
    ('Every Disposition Is Reportable',
     'Crypto traded for crypto counts, as does crypto spent on goods. No cash '
     'has to be involved for a year to have a disposition in it.'),
    ('Records Get Harder With Time',
     'Exchange histories and wallet records are hard to reconstruct years '
     'later, and a run of unfiled years makes that worse.'),
    ('Cashing Out Draws the Questions',
     'A conversion to dollars through a regulated exchange is where an '
     'unfiled history tends to surface.'),
  ],
  'notnil_text': (
    'Most of these corporations were set up to trade, which means most of '
    'their years are ordinary returns rather than nil ones. What this page '
    'covers is the year in between: the one where a position was held and '
    'nothing was done with it.',
    'That year is $300.00 plus HST per tax year, and it is priced only after '
    'the trading test. A trading year is quoted as an ordinary corporate '
    'return rather than squeezed in here.'),

  'sched_h': 'Which T2 Schedules a Crypto Trading Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'The holdings themselves, at cost, plus share capital and any '
     'shareholder loan, keep the balance sheet occupied in every year.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Nil in a holding year. In any year with a trade, a swap or a reward it '
     'carries figures and the return is not nil.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Travels with the two GIFI schedules and states who prepared the '
     'figures.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Any holder of 10% or more of the shares is named.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the first T2 after incorporation, then not again.'),
    ('Schedule 8', 'Capital cost allowance', 'Rarely',
     'Crypto holdings are not depreciable property. A mining rig or hardware '
     'the corporation owns would be.'),
  ],
  'sched_note': 'Source: the T2 schedule requirements the Canada Revenue '
                'Agency sets, applied to a corporation holding crypto assets '
                'with no transactions in the tax year. Reviewed '
                '23 November 2026.',
  'sched_boxes': [
    ('A Swap Is a Disposition',
     'Exchanging one crypto asset for another is a disposition of the first, '
     'reportable in the year it happened, with no cash involved.'),
    ('Staking and Lending Pay Without a Trade',
     'Rewards or interest credited to the corporation are income to it, and '
     'they arrive in years when nothing was traded at all.'),
    ('Unrealised Movement Is Not Income',
     'Holdings rising or falling in value while untouched put nothing on '
     'Schedule 125. The position carries forward at cost.'),
  ],
  'chk_yes': [
    'Nothing was bought, sold or swapped by the corporation in the year',
    'No staking, lending or liquidity reward was credited to it',
    'No holding was spent on goods, services or fees',
    'No transfer out was made to anyone, including a shareholder',
    'No cash account of the corporation earned interest',
  ],
  'chk_no': [
    'One asset was exchanged for another, at any size',
    'A position was closed, in whole or in part',
    'A staking, lending or airdrop reward was received',
    'Crypto was used to pay for something',
    'Holdings were moved out to a shareholder or a related party',
  ],
  'chk_both': [
    'A return covering each tax year the corporation remains in existence',
    'An authorised T183CORP accompanying every return filed',
    'Shareholder disclosure on Schedule 50 at the 10% level',
    'A transaction record kept for each year, nil or otherwise',
    'Clearance before the corporation can be wound up',
  ],

  'why_h': 'Why Crypto Trading Corporations Use This Service',
  'why': [
    ('The Trading Test Comes Before the Fee',
     'Every year is checked for trades, swaps and rewards first. A year that '
     'fails is not taken at this price.'),
    ('For Holding Years Only',
     'A year in which a position was held and nothing done with it is what '
     'this fee is written for.'),
    ('One Price Where the Year Qualifies',
     'A clean holding year is $300.00 plus HST per tax year, however many are '
     'outstanding.'),
    ('Trading Years Are Quoted as Trading Years',
     'A year with dispositions in it is prepared as an ordinary corporate '
     'return, priced on what it actually involves.'),
  ],
  'strip': [
    ('Holding Can Be Nil, Trading Cannot',
     'The distinction is the whole of it.'),
    ('In Date Order',
     'Cost base only carries forward correctly if the years do.'),
    ('Authorised Electronically',
     'Each year is signed off in a secure portal.'),
  ],

  'svc_h': 'What a Crypto Trading Corporation Usually Needs Next',
  'proc_h': 'How a Crypto Trading Corporation Files a Holding Year',
  'proc_lede': 'Four steps. The first one rules out most years, which is the '
               'point of doing it first.',
  'proc_note': 'Expect the transaction check to disqualify some years:',
  'steps': [
    ('Run the Transaction Check',
     'Every buy, sell, swap, reward and transfer in the year is looked for. '
     'One of any of them and the year is not filed at the nil price.'),
    ('Carry the Cost Base Forward',
     'Holdings untouched through the year keep their existing cost, which '
     'becomes the opening figure for the next return.'),
    ('Prepare the Return',
     'Schedules 100, 125, 141 and 50 for the year, with Schedule 24 where '
     'this is the first return.'),
    ('Authorise and Transmit',
     'One T183CORP for each qualifying year, transmitted electronically, with '
     'the Agency confirmation emailed inside 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Crypto Trading Corporation',
  'price_eyebrow': 'One Fee Per Qualifying Year',
  'price_text': (
    'A year that passes the transaction check is $300.00 plus HST per tax '
    'year. That covers the T2, the GIFI schedules where required, Schedule '
    '50, Schedule 24 on a first return, the T183CORP package with secure '
    'e-signing, CPA review before transmission, electronic transmission by a '
    'registered EFILE electronic filer, one corrected transmission where the '
    'Agency rejects the first, and the CRA confirmation emailed within 3 '
    'business days. Any year with a trade, a swap, a reward or a disposal in '
    'it is a full T2 at $350.00 plus HST per year at gondaliyacpa.ca.'),

  'geo_h': 'Crypto Corporation Filing Across Canada',
  'cta_h': 'Test the Holding Years and File the Ones That Qualify',

  'faq': [
   ('Can a crypto corporation ever file a nil return?',
    'Only for a year in which it transacted nothing at all: no buy, no sale, '
    'no swap, no reward and no transfer out, with the holdings untouched. Any '
    'year with one of those is a full T2 with income to report at $350.00 '
    'plus HST per year at gondaliyacpa.ca.'),
   ('I swapped one coin for another but never cashed out. Is that a year?',
    'Yes. A swap is a disposition of the asset given up, reportable in that '
    'year whether or not any dollars changed hands.'),
   ('The holdings doubled in value. Does that make the year active?',
    'No. An unrealised change in value is not income. The position carries '
    'forward at its existing cost and the year can still be nil.'),
   ('We received staking rewards and nothing else. Nil or not?',
    'Not nil. Rewards credited to the corporation are income to it in the '
    'year received, even in a year with no trading.'),
   ('An airdrop arrived unasked. Does that count?',
    'It is something received by the corporation, so the year is one to treat '
    'as an ordinary return rather than a nil filing.'),
   ('The wallet is self-custodied with no exchange account. Does that change anything?',
    'No. Where the assets are held makes no difference to whether a return is '
    'due or to what has to be reported.'),
   ('I traded in my own name, not the corporation’s. Is the company nil?',
    'It can be, where nothing moved through the corporation. The test is '
    'which holder transacted, not who gave the instruction.'),
   ('We paid a supplier in crypto. Is that year nil?',
    'No. Spending a holding is disposing of it, and the disposition is '
    'reported in the year it was spent.'),
   ('Several years were never filed. How are they handled?',
    'Each is tested on its own. Qualifying years are $300.00 plus HST per tax '
    'year, trading years are quoted as ordinary returns, and the whole set is '
    'filed from the earliest forward.'),
   ('We want to move the holdings out and close the company. What order?',
    'The outstanding returns first. Moving holdings to a shareholder is '
    'itself a disposition to report, and no clearance certificate is issued '
    'while a year is missing.'),
  ],
 },

 'photography-corporations': {
  'name':   'Photography Corporations',
  'short':  'photography corporation',
  'plural': 'photography corporations',
  'kw':     'nil t2 for photography corporation',
  'title':  'Photography Corporation Nil T2 | Years Without Shoots',
  'desc':   'A photography corporation files for every tax year it exists. '
            'Why a stock licence fee years later ends the nil year, and what '
            'the return costs.',

  'h1':   'Nil T2 Filing for Photography Corporations',
  'lede': 'The bodies and lenses are in a bag and the corporation that owns '
          'them keeps arriving at year ends. Where no shoot was billed and '
          'no licence fee came in, the return is $300.00 plus HST per tax '
          'year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Photography Corporations',
  'intro': (
    'Photography corporations go quiet without closing. There is usually no '
    'studio lease and no staff, so what remains is a corporation holding some '
    'gear and a back catalogue, with a return falling due every year. An '
    'empty year is $300.00 plus HST per tax year.',
    'Whether you went in-house, took salaried work, stopped taking bookings, '
    'or shoot occasionally in your own name now, the year is tested against '
    'shoots invoiced, print and album sales, licence or stock royalties '
    'arriving from earlier work, and any gear sold. Schedules 100, 125, 141 '
    'and 50 are prepared and the return goes across electronically. A year '
    'with any of that in it goes to the full service.'),

  'notnil_h': 'What an Unfiled Year Costs a Photography Corporation',
  'notnil_boxes': [
    ('Putting the Camera Down Changes Nothing',
     'The corporation reaches a year end whether or not a shutter was '
     'pressed, and each one owes a return.'),
    ('Nothing About This Lapses',
     'An outstanding year stays outstanding until it is filed. A written '
     'demand is what attaches a deadline to it.'),
    ('The Back Catalogue Can Still Earn',
     'Images licensed years ago can pay again, putting revenue into a year '
     'nobody was watching.'),
    ('Gear Is on the Books',
     'Bodies, lenses and lighting sit on the schedules until they are sold or '
     'written off, and that needs the years filed.'),
  ],
  'notnil_text': (
    'The corporation usually stays because the gear is in it and because '
    'another commission might come. Those are good reasons to keep it and '
    'they do not change the fact that each year of keeping it is a tax year.',
    'An empty year costs $300.00 plus HST per tax year. A run of them is '
    'prepared as one job and sent from the earliest year so the gear values '
    'follow through.'),

  'sched_h': 'Which T2 Schedules a Photography Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Camera bodies, lenses, lighting, any deposit held against a future '
     'booking and the shareholder balance all sit here.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Nil shoot revenue and nil expenses, for a year with nothing invoiced '
     'and nothing claimed.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Accompanies the two GIFI schedules, recording who prepared them and '
     'how.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Holders of 10% or more, usually the single photographer who owns it '
     'outright.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Attached to the first return the corporation ever files, and to no '
     'other.'),
    ('Schedule 8', 'Capital cost allowance', 'While the gear is owned',
     'Bodies, lenses, lighting and computers are depreciable property until '
     'sold or taken out, used or not.'),
  ],
  'sched_note': 'Source: the schedule requirements for a T2 return set by the '
                'Canada Revenue Agency, read against a photography '
                'corporation that invoiced no shoot in the tax year. '
                'Reviewed 23 November 2026.',
  'sched_boxes': [
    ('A Licence Fee Years Later Still Counts',
     'A stock sale or a usage licence on old work is revenue to the '
     'corporation in the year it is paid, which makes that year an ordinary '
     'return.'),
    ('A Booking Deposit Is Not Yet Earned',
     'A retainer held against a shoot that has not happened sits on '
     'Schedule 100 as an amount owed, not as income.'),
    ('Shooting Personally Keeps the Year Clean',
     'Where a client paid you rather than the corporation, that income is '
     'yours to report and the corporate year can be nil.'),
  ],
  'chk_yes': [
    'No shoot or session was invoiced by the corporation in the year',
    'No print, album or digital file sale went through it',
    'No licence, usage or stock royalty was paid to it',
    'No camera body, lens or light of its was sold',
    'No bank or investment account in its name paid it anything',
  ],
  'chk_no': [
    'A shoot was invoiced, even one booked the year before',
    'A stock agency or publisher paid a royalty or licence fee',
    'A deposit held earlier was applied to a shoot in the year',
    'Gear was sold, traded in or passed to a shareholder',
    'The back catalogue, the brand or the client list was sold',
  ],
  'chk_both': [
    'Each year end the corporation reaches needs its own T2',
    'Each of those returns needs a T183CORP before it goes',
    'Schedule 50 applies once anyone holds a tenth of the shares',
    'The registry annual return runs on a separate calendar',
    'Clearance comes before the gear leaves and the company closes',
  ],

  'why_h': 'Why Photography Corporations Use This Service',
  'why': [
    ('For the Years Between Commissions',
     'A year in-house, a year on salary, a year with no bookings. Those are '
     'what this fee covers.'),
    ('Royalties Are the First Thing Looked For',
     'Licence income on old work arriving unannounced is the usual reason one '
     'of these years is not nil, so it is checked before a price is given.'),
    ('One Rate Per Quiet Year',
     'A year with nothing invoiced is $300.00 plus HST per tax year, with no '
     'retainer and no minimum.'),
    ('Earning Years Go Elsewhere',
     'A year with shoot revenue or a royalty in it is prepared as an ordinary '
     'corporate return at the higher fee.'),
  ],
  'strip': [
    ('Idle Gear, Live Company',
     'A bag in a cupboard has no bearing on the year end arriving.'),
    ('Oldest Year Leads',
     'Gear values only carry forward if the returns are filed in order.'),
    ('A Browser Is the Whole Tool',
     'The run of authorisations takes minutes and no paper at all.'),
  ],

  'svc_h': 'What a Photography Corporation Usually Needs Next',
  'proc_h': 'How a Photography Corporation Files',
  'proc_lede': 'Four steps from the filing form, beginning with everything '
               'that might have paid in.',
  'proc_note': 'Most of this comes off a year of statements:',
  'steps': [
    ('Look for Anything That Paid In',
     'Shoots invoiced, print sales, licence fees, stock royalties and gear '
     'sales are all measured before the year is treated as nil.'),
    ('Split the Personal From the Corporate',
     'Work paid to you directly is on your own return, which can leave the '
     'corporate year holding nothing.'),
    ('Put the Return Together',
     'Figures on Schedules 100, 125 and 141, ownership on Schedule 50, '
     'Schedule 24 if this is the corporation\u2019s first filing, and '
     'Schedule 8 for as long as the gear belongs to it.'),
    ('Authorise Each Year, Then Send',
     'A T183CORP per year, transmitted as a set, with the Agency '
     'confirmation emailed inside 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Photography Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'Quiet years are charged one at a time, at $300.00 plus HST per tax year '
    'where nothing was invoiced and no royalty arrived. The fee takes in the '
    'T2, the GIFI schedules where '
    'required, Schedule 50, Schedule 24 on a first return, the T183CORP '
    'package with secure e-signing, CPA review before transmission, '
    'electronic transmission by a registered EFILE electronic filer, one '
    'corrected transmission where the Agency rejects the first, and the CRA '
    'confirmation emailed within 3 business days. A year with shoot revenue, '
    'a licence fee or a gear sale in it is $350.00 plus HST per year at '
    'gondaliyacpa.ca.'),

  'geo_h': 'Photography Corporation Filing Across Canada',
  'cta_h': 'File the Years the Shutter Stayed Closed',

  'faq': [
   ('I have not taken a paid booking in two years. Are returns still due?',
    'They are, for every year the corporation exists. A year with no shoots '
    'is reported as a year with no revenue rather than left unfiled.'),
   ('A stock agency paid a licence fee for an old image. Which year?',
    'The year the corporation was paid. That year becomes an ordinary return '
    'at $350.00 plus HST per year at gondaliyacpa.ca and the years around it '
    'can still be nil.'),
   ('I shoot the odd wedding in my own name now. Does that affect the company?',
    'Not where the couple paid you rather than the corporation. That is '
    'personal income and the corporate year can be nil.'),
   ('I took a salaried job at a studio. Does the corporation keep filing?',
    'Yes, until it is dissolved. Employment income is yours and has no '
    'bearing on the corporate year.'),
   ('A client left a deposit for a shoot that never happened. Is that income?',
    'Not while it is unearned. It sits as an amount owed on the balance sheet '
    'until the shoot happens or it is refunded.'),
   ('The gear is insured and stored but unused. Does owning it count?',
    'No. Schedule 8 keeps reporting it while the corporation owns it. '
    'Selling a lens is what puts a figure in a year.'),
   ('I sold two lenses to another photographer. Nil or not?',
    'Not for that year. A sale is a disposition and goes on the return '
    'whether it produced a gain or a loss.'),
   ('Do the images themselves have to be valued every year?',
    'No. A back catalogue created in the business is not revalued annually. '
    'What matters is whether it earned anything in the year.'),
   ('Six years are outstanding. Is that a problem?',
    'Six returns, is all. They are priced at $300.00 plus HST per tax year '
    'apiece, authorised in one sitting, and transmitted in the order the '
    'years fell.'),
   ('I want to take the gear personally and close the company. What order?',
    'Outstanding returns first. Taking the gear out is a disposition to '
    'report in its year, and clearance is not issued while a year is '
    'missing.'),
  ],
 },

}
