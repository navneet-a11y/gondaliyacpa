"""Per-city prose for Family 3 city hubs.

Plan line 1721: a city hub publishes only where it carries data that differs by
place, "because template city pages with no unique per-page data are what the
March 2026 spam and core updates removed." A name swap alone scores 0.976
against Toronto on the 6(k) body-similarity measure, far above the 0.60
threshold, so each city needs its own writing, not its own tokens.

COPY[slug]['text'] is a list of (old, new) substring pairs applied to every
string setting in the built template, in order, after the city's default text
has been composed. A city with no entry renders the default wording, which is
what /toronto/ carries, so Toronto's output is unaffected by anything here.

COPY[slug]['faq'] replaces the whole question list.

What never varies, because it is fact or a hard rule: the price wording, the
"registered EFILE electronic filer" phrasing, T183CORP, the "is not nil"
sentence, and the CRA confirmation window.
"""

MISSISSAUGA_FAQ = [
 ('Is a Mississauga corporation that never started trading still required to file?',
  '<p>Yes. The requirement follows the corporation, not the trading. A company '
  'incorporated for a venture that never began still files a T2 for each tax '
  'year it exists. '
  '<a href="https://corpnilfilingfor300.ca/numbered-corporation-nil-filing-mississauga/">'
  'Numbered corporation filing</a>.</p>'),
 ('How do I know my year was actually nil?',
  '<p>Nothing came in and nothing went out: no sales, no expenses claimed, no '
  'movement through the bank account, nobody on payroll. If any of those is '
  'untrue the year is not nil, and we say so before charging anything. '
  '<a href="https://corpnilfilingfor300.ca/no-activity-corporation-tax-return-mississauga/">'
  'What no activity means</a>.</p>'),
 ('What is my filing date?',
  '<p>Six months after your own fiscal year end, not a fixed date in the '
  'calendar. A September 30 year end means a March 31 filing date. '
  '<a href="https://corpnilfilingfor300.ca/nil-t2-filing-deadline-mississauga/">'
  'Work out your date</a>.</p>'),
 ('Four years are outstanding. Where do I start?',
  '<p>At the oldest one. Each year is its own return and its own $300.00 plus '
  'HST, filed in sequence so the CRA account reconciles year by year. '
  '<a href="https://corpnilfilingfor300.ca/catch-up-nil-t2-filing-mississauga/">'
  'Catch-up filing</a>.</p>'),
 ('What am I signing, and can I do it from my phone?',
  '<p>A T183CORP, one per tax year, which authorises the electronic '
  'transmission. It is signed on screen, on any device, and nothing is printed. '
  '<a href="https://corpnilfilingfor300.ca/guides/t183corp-signing-and-transmission/">'
  'How signing works</a>.</p>'),
 ('Is my Ontario annual return part of this?',
  '<p>No, and the two are often confused. The annual return is filed with the '
  'Ontario Business Registry and is a separate obligation from the T2. We '
  'check whether yours is outstanding and tell you. '
  '<a href="https://corpnilfilingfor300.ca/tools/ontario-annual-return-due-date-calculator/">'
  'Check your date</a>.</p>'),
 ('The corporation holds a rental property. Does it qualify?',
  '<p>No. Rent received is income, so the year is not nil whatever the profit '
  'was. The same applies to interest, dividends received or dividends paid out. '
  '<a href="https://corpnilfilingfor300.ca/inactive-holding-corporation-t2-filing-mississauga/">'
  'Holding corporations</a>.</p>'),
 ('I have moved abroad. Can the filing still go ahead?',
  '<p>Yes. Signing is electronic, so a director can authorise the return from '
  'any country. '
  '<a href="https://corpnilfilingfor300.ca/nil-t2-filing-for-non-resident-owned-corporations-mississauga/">'
  'Non-resident owned corporations</a>.</p>'),
 ('We are winding the company up. Is a final return needed?',
  '<p>Yes, and it is what closes the file. A final T2 runs to the dissolution '
  'date and is due six months after it. '
  '<a href="https://corpnilfilingfor300.ca/final-t2-before-dissolution-mississauga/">'
  'Final T2 before dissolution</a>.</p>'),
 ('Does a dormant company really have to keep filing every year?',
  '<p>Every year, until it is dissolved. A year that is skipped does not fall '
  'away; it stays outstanding on the CRA account until the return is '
  'transmitted. '
  '<a href="https://corpnilfilingfor300.ca/answers/does-an-inactive-corporation-have-to-file-a-t2/">'
  'The full answer</a>.</p>'),
]

MISSISSAUGA_TEXT = [
 # --- hero lede
 ('Nil T2 filing for Mississauga corporations. One price for every tax year, '
  'with no hourly billing and no add-on fees.',
  'For Mississauga corporations that did not trade this year. A flat fee per '
  'year, filed online, confirmed by the CRA in writing.'),

 # --- intro block
 ('Nil T2 Filing for Mississauga Corporations',
  'Nil T2 Filing in Mississauga for Dormant and Numbered Corporations'),
 ('A nil T2 is the corporate return a Mississauga corporation files for a tax '
  'year in which it had no revenue, no expenses and no bank activity. The '
  'corporation still exists, so the return is still due. Incorporating and '
  'then going quiet does not end the obligation, and a year left unfiled stays '
  'open until the return is transmitted.',
  'Plenty of Mississauga corporations spend a year doing nothing at all. The '
  'company was set up for a venture that never started, or it traded once and '
  'went quiet, or it exists only to hold a name. None of that removes the '
  'return. The Canada Revenue Agency expects a T2 for the year regardless, and '
  'the only thing that ends the requirement is dissolving the corporation.'),
 ('Nil T2 filing in Mississauga covers the year end to end. The return is '
  'prepared and reviewed, you sign a T183CORP for each tax year, and the '
  'return is transmitted to the Canada Revenue Agency electronically. It is '
  'done online from start to finish, so there is nothing to print, mail or '
  'sign in person, wherever in the city your registered office sits.',
  'That is the whole of what this service does. We take the corporation number '
  'and the year end, confirm the year really was nil, prepare the return, send '
  'a T183CORP for signature and transmit it. Whether the registered office is '
  'in Meadowvale, Port Credit or a home address off Hurontario, the work is '
  'the same and happens entirely online.'),

 # --- three-cell strip
 ('One Fee Per Tax Year', 'Priced by the Year'),
 ('No hourly billing and no add-on charges for schedules or transmission.',
  'One figure covers the year. Nothing is added for schedules, review or '
  'transmission.'),
 ('Every Unfiled Year Counts', 'Older Years Are Not Written Off'),
 ('Each year is a separate T2 return at $300.00 plus HST per tax year.',
  'A missed year stays on the CRA account until its own return is filed, at '
  '$300.00 plus HST per tax year.'),
 ('Signed and Filed Online', 'Nothing Printed or Posted'),
 ('Nothing to print. You sign the T183CORP electronically for each tax year.',
  'The T183CORP is signed on screen, one for each tax year.'),

 # --- local data block
 # 'exact': this is also a substring of the non-resident service card's
 # title, which must keep its own wording.
 ('Corporations in Mississauga',
  'Federal Corporations Registered in Mississauga', 'exact'),
 ('36,448 active federal business corporations have a registered office in '
  'Mississauga.',
  'Mississauga is the registered office of 36,448 active federal business '
  'corporations.'),

 # --- service grid heading
 ('Nil T2 Filing Services in Mississauga',
  'What We File for Mississauga Corporations'),

 # --- the twelve service card descriptions
 ('A T2 return for a corporation with no activity in the tax year, CPA '
  'reviewed and transmitted electronically.',
  'The standard filing: one quiet tax year, checked by a CPA and sent '
  'electronically to the CRA.'),
 ('Several unfiled nil years filed together, oldest year first.',
  'Two or more outstanding years cleared in one go, in date order.'),
 ('For a corporation that has stopped trading but has not been dissolved.',
  'The company has stopped operating but still legally exists, so the returns '
  'keep coming due.'),
 ('The last return for a corporation being wound up, due within six months of '
  'dissolution.',
  'The closing return when a company is wound up, filed within six months of '
  'the dissolution date.'),
 ('The two-page T2 Short return, where every CRA condition for using it is met.',
  'The shorter two-page return, used only where the corporation meets every '
  'CRA condition for it.'),
 ('What the $300.00 fee covers and what it does not.',
  'A plain breakdown of what is included in the fee and what sits outside it.'),
 ('Returns for years already past their due date. An unfiled year stays open '
  'until it is filed.',
  'Years that have gone past their date. Nothing lapses on its own.'),
 ('No revenue, no bank activity and no employees. The filing obligation still '
  'applies.',
  'Nothing earned, nothing spent, nobody paid, and the return is still owed.'),
 ('For a numbered corporation that was incorporated and never traded, or has '
  'gone quiet.',
  'Set up and never used, or long since idle. Common among numbered companies.'),
 ('A holding corporation with investment income, rental income or dividends '
  'paid or received is not nil.',
  'Rent, interest or dividends mean the year is not nil, whatever the profit '
  'was.'),
 ('Due within six months of the fiscal year-end, every year, until the '
  'corporation is dissolved.',
  'Six months after your own year end, repeating annually until dissolution.'),
 ('Nil filing where the shareholders are outside Canada.',
  'Filing for a corporation whose directors or shareholders live abroad.'),

 # --- what you get
 ('What You Get for $300.00 in Mississauga',
  'What the Mississauga Filing Includes'),
 ('CPA Prepared and Reviewed', 'Checked by a CPA'),
 ('Your T2 is prepared and reviewed by a CPA Ontario registered firm, Firm '
  'Registration 61330051, before it is transmitted.',
  'A CPA Ontario registered firm, Firm Registration 61330051, prepares and '
  'reviews the return before it leaves.'),
 ('Registered EFILE Electronic Filer', 'Sent Electronically to the CRA'),
 ('The return goes to the Canada Revenue Agency electronically, not by mail.',
  'As a registered EFILE electronic filer we transmit directly. Nothing is '
  'posted.'),
 ('One Price Per Tax Year', 'A Figure Fixed in Advance'),
 ('$300.00 plus HST per tax year, quoted before any work starts. No hourly '
  'billing and no add-on charges.',
  '$300.00 plus HST per tax year, agreed before anything begins and not '
  'revised afterwards.'),
 ('T183CORP Signed Online', 'One T183CORP a Year, Signed on Screen'),
 ('You receive a T183CORP for each tax year and sign it electronically. One '
  'form per year.',
  'Each tax year needs its own authorisation, signed on any device.'),
 ('CRA Confirmation in Writing', 'Written Confirmation Back'),
 ('Your CRA confirmation is emailed within 3 business days of transmission.',
  'The CRA confirmation reaches you by email within 3 business days of '
  'transmission.'),
 ('We Tell You If You Are Not Nil', 'An Honest Answer If It Does Not Qualify'),
 ('A corporation with investment income, rental income, or dividends paid or '
  'received is not nil. We tell you before any further charge.',
  'Investment income, rent or dividends mean the corporation is not nil. You '
  'hear that before any further charge.'),

 # --- process
 ('How it works', 'The process'),
 ('How Nil T2 Filing Works in Mississauga', 'Four Steps, Start to Finish'),
 ('Four steps, all online. You send the corporation details, a CPA prepares '
  'and reviews the return, you sign the T183CORP, and the return is '
  'transmitted to the Canada Revenue Agency.',
  'No appointment and no office visit. You hand over a few details, a CPA does '
  'the work, you authorise it, and the CRA confirms receipt.'),
 ('Send Details', 'Tell Us About the Corporation'),
 ('Corporation number, tax year end, and which years are unfiled. Online, with '
  'no appointment.',
  'The corporation number, the fiscal year end, and which years are still '
  'outstanding.'),
 ('CPA Review', 'A CPA Looks at It'),
 ('A CPA checks that the year is nil and prepares the T2 return.',
  'The year is checked against the nil test, then the T2 is prepared.'),
 ('Sign T183CORP', 'You Authorise It'),
 ('You sign one T183CORP for each tax year, electronically.',
  'A T183CORP for each year, signed on screen.'),
 ('CRA Confirmation', 'The CRA Confirms'),
 ('The return is transmitted and your CRA confirmation is emailed within 3 '
  'business days.',
  'We transmit, and the confirmation is emailed to you inside 3 business days.'),

 # --- price block
 ('Nil T2 filing price', 'The fee'),
 ('Nil T2 Filing Price in Mississauga', 'What a Mississauga Nil T2 Costs'),
 ('$300.00 plus HST per tax year. The fee covers preparation, CPA review, the '
  'T183CORP for signature, and electronic transmission to the Canada Revenue '
  'Agency. Each unfiled tax year is a separate return at the same price.',
  '$300.00 plus HST per tax year, and the year is the unit. Preparation, the '
  'CPA review, the T183CORP and the transmission are all inside that figure. '
  'Three outstanding years means three returns at the same price each.'),

 # --- closing CTA and FAQ heading
 ('File your Mississauga nil T2 return', 'Start your Mississauga filing'),
 ('Nil T2 Filing in Mississauga: Common Questions',
  'Mississauga Nil T2 Filing: Questions We Are Asked'),
]

BRAMPTON_FAQ = [
 ('How many years can I leave before it becomes a problem?',
  '<p>There is no point at which an unfiled year is written off. It stays open '
  'on the CRA account until its return is transmitted, however long that takes. '
  '<a href="https://corpnilfilingfor300.ca/unfiled-corporate-tax-returns-brampton/">'
  'Unfiled returns</a>.</p>'),
 ('Do the years have to be filed in order?',
  '<p>Oldest first. Each year is its own return, and filing them in sequence is '
  'what lets the account reconcile cleanly rather than leaving gaps. '
  '<a href="https://corpnilfilingfor300.ca/catch-up-nil-t2-filing-brampton/">'
  'Catch-up filing</a>.</p>'),
 ('What does it cost for several years at once?',
  '<p>$300.00 plus HST per tax year, with no discount and no surcharge for '
  'volume. Five outstanding years is five returns at that figure. '
  '<a href="https://corpnilfilingfor300.ca/nil-t2-filing-cost-in-brampton/">'
  'What the fee covers</a>.</p>'),
 ('What do you need from me to begin?',
  '<p>The corporation number, the fiscal year end, and which years are '
  'outstanding. That is enough to start; we come back if anything else is '
  'needed.</p>'),
 ('How do I know the year qualifies as nil?',
  '<p>Nothing in, nothing out, nobody paid, no movement in the bank account. '
  'Where that is not the case we say so before charging. '
  '<a href="https://corpnilfilingfor300.ca/no-activity-corporation-tax-return-brampton/">'
  'What no activity means</a>.</p>'),
 ('Is a signature needed for every year separately?',
  '<p>Yes. A T183CORP authorises one tax year, so five years means five forms, '
  'each signed on screen. '
  '<a href="https://corpnilfilingfor300.ca/guides/t183corp-signing-and-transmission/">'
  'How signing works</a>.</p>'),
 ('Does catching up on the T2 also catch up my Ontario annual return?',
  '<p>No. The Ontario annual return is a separate filing through the Ontario '
  'Business Registry and is not part of this. We check whether yours is behind '
  'and tell you. '
  '<a href="https://corpnilfilingfor300.ca/tools/ontario-annual-return-due-date-calculator/">'
  'Check your date</a>.</p>'),
 ('One of those years the company earned a little. What then?',
  '<p>That year is not nil and is priced separately; the surrounding nil years '
  'still are. We separate them before anything is charged. '
  '<a href="https://corpnilfilingfor300.ca/inactive-holding-corporation-t2-filing-brampton/">'
  'When a year is not nil</a>.</p>'),
 ('Can this be done if I am not in Canada?',
  '<p>Yes. Everything including the signature is electronic, so where a '
  'director lives makes no difference. '
  '<a href="https://corpnilfilingfor300.ca/nil-t2-filing-for-non-resident-owned-corporations-brampton/">'
  'Non-resident owned corporations</a>.</p>'),
 ('Once I am caught up, does it stop?',
  '<p>No. A return is due for every year the corporation exists. Only '
  'dissolution ends it, and that needs a final return of its own. '
  '<a href="https://corpnilfilingfor300.ca/final-t2-before-dissolution-brampton/">'
  'Final T2 before dissolution</a>.</p>'),
]

BRAMPTON_TEXT = [
 ('Nil T2 filing for Brampton corporations. One price for every tax year, '
  'with no hourly billing and no add-on fees.',
  'Behind on your Brampton corporation\u2019s returns? Each outstanding year '
  'filed at one flat fee, in order, online.'),

 ('Nil T2 Filing for Brampton Corporations',
  'Nil T2 Filing in Brampton, Including Years You Have Missed'),
 ('A nil T2 is the corporate return a Brampton corporation files for a tax '
  'year in which it had no revenue, no expenses and no bank activity. The '
  'corporation still exists, so the return is still due. Incorporating and '
  'then going quiet does not end the obligation, and a year left unfiled stays '
  'open until the return is transmitted.',
  'Most people who come to us from Brampton are not one year behind. They are '
  'three, or five, or more. A corporation was set up, it did little or '
  'nothing, and the filing quietly stopped being thought about. Nothing in '
  'that chain cancels the returns. Each of those years is still owed, and each '
  'stays on the CRA account until it is filed.'),
 ('Nil T2 filing in Brampton covers the year end to end. The return is '
  'prepared and reviewed, you sign a T183CORP for each tax year, and the '
  'return is transmitted to the Canada Revenue Agency electronically. It is '
  'done online from start to finish, so there is nothing to print, mail or '
  'sign in person, wherever in the city your registered office sits.',
  'Catching up is less work than it sounds. Send the corporation number, the '
  'year end and the list of years outstanding. We confirm which of them were '
  'genuinely nil, prepare each return, send a T183CORP for each year to sign, '
  'and transmit them oldest first so the account clears in order. From '
  'Bramalea to Mount Pleasant, it is the same process and none of it needs a '
  'visit.'),

 ('One Fee Per Tax Year', 'The Same Figure Every Year'),
 ('No hourly billing and no add-on charges for schedules or transmission.',
  'Five years behind costs five times one year. No volume pricing either way.'),
 ('Every Unfiled Year Counts', 'Nothing Expires on Its Own'),
 ('Each year is a separate T2 return at $300.00 plus HST per tax year.',
  'An old year does not drop off. It waits at $300.00 plus HST per tax year '
  'until it is filed.'),
 ('Signed and Filed Online', 'One Signature a Year'),
 ('Nothing to print. You sign the T183CORP electronically for each tax year.',
  'Each year needs its own T183CORP, signed on screen, never printed.'),

 ('Corporations in Brampton',
  'How Many Federal Corporations Sit in Brampton', 'exact'),
 ('67,667 active federal business corporations have a registered office in '
  'Brampton.',
  'There are 67,667 active federal business corporations with a registered '
  'office in Brampton.'),

 ('Nil T2 Filing Services in Brampton',
  'Every Filing We Handle for Brampton'),

 ('A T2 return for a corporation with no activity in the tax year, CPA '
  'reviewed and transmitted electronically.',
  'A single quiet year, prepared, reviewed by a CPA and filed electronically.'),
 ('Several unfiled nil years filed together, oldest year first.',
  'The usual case here: a run of missed years, cleared in sequence.'),
 ('For a corporation that has stopped trading but has not been dissolved.',
  'Trading has stopped, the company has not been wound up, the returns '
  'continue.'),
 ('The last return for a corporation being wound up, due within six months of '
  'dissolution.',
  'The return that closes the file, due six months from dissolution.'),
 ('The two-page T2 Short return, where every CRA condition for using it is met.',
  'A two-page return, available only when the CRA\u2019s conditions are all '
  'met.'),
 ('What the $300.00 fee covers and what it does not.',
  'Exactly where the fee starts and stops.'),
 ('Returns for years already past their due date. An unfiled year stays open '
  'until it is filed.',
  'Overdue years, however far back they go.'),
 ('No revenue, no bank activity and no employees. The filing obligation still '
  'applies.',
  'An empty year on paper is still a year that must be filed.'),
 ('For a numbered corporation that was incorporated and never traded, or has '
  'gone quiet.',
  'Numbered companies that were registered and then left alone.'),
 ('A holding corporation with investment income, rental income or dividends '
  'paid or received is not nil.',
  'Where income arrives from rent, interest or dividends, the year is not nil.'),
 ('Due within six months of the fiscal year-end, every year, until the '
  'corporation is dissolved.',
  'Six months past the year end, and again the year after that.'),
 ('Nil filing where the shareholders are outside Canada.',
  'For corporations owned or directed from outside Canada.'),

 ('What You Get for $300.00 in Brampton', 'What Is Included, Year by Year'),
 ('CPA Prepared and Reviewed', 'A CPA Does the Work'),
 ('Your T2 is prepared and reviewed by a CPA Ontario registered firm, Firm '
  'Registration 61330051, before it is transmitted.',
  'Every return is prepared and reviewed inside a CPA Ontario registered firm, '
  'Firm Registration 61330051.'),
 ('Registered EFILE Electronic Filer', 'Filed Straight to the CRA'),
 ('The return goes to the Canada Revenue Agency electronically, not by mail.',
  'We are a registered EFILE electronic filer, so nothing travels by post.'),
 ('One Price Per Tax Year', 'Priced Per Year, Always'),
 ('$300.00 plus HST per tax year, quoted before any work starts. No hourly '
  'billing and no add-on charges.',
  '$300.00 plus HST per tax year, known before we begin and unchanged after.'),
 ('T183CORP Signed Online', 'A T183CORP for Each Year'),
 ('You receive a T183CORP for each tax year and sign it electronically. One '
  'form per year.',
  'One authorisation per tax year, signed on screen in a few seconds.'),
 ('CRA Confirmation in Writing', 'Proof for Every Year Filed'),
 ('Your CRA confirmation is emailed within 3 business days of transmission.',
  'A CRA confirmation arrives by email within 3 business days of each '
  'transmission.'),
 ('We Tell You If You Are Not Nil', 'A Year That Does Not Qualify Is Flagged'),
 ('A corporation with investment income, rental income, or dividends paid or '
  'received is not nil. We tell you before any further charge.',
  'Where a year carried investment income, rent or dividends it is not nil. '
  'You are told before any further charge.'),

 ('How it works', 'Catching up'),
 ('How Nil T2 Filing Works in Brampton',
  'From Behind to Up to Date'),
 ('Four steps, all online. You send the corporation details, a CPA prepares '
  'and reviews the return, you sign the T183CORP, and the return is '
  'transmitted to the Canada Revenue Agency.',
  'However many years are outstanding, the sequence is the same and runs '
  'entirely online.'),
 ('Send Details', 'List the Years'),
 ('Corporation number, tax year end, and which years are unfiled. Online, with '
  'no appointment.',
  'Corporation number, year end, and every year still outstanding.'),
 ('CPA Review', 'We Sort the Nil Years'),
 ('A CPA checks that the year is nil and prepares the T2 return.',
  'A CPA confirms which years were genuinely nil and prepares each return.'),
 ('Sign T183CORP', 'Sign Once Per Year'),
 ('You sign one T183CORP for each tax year, electronically.',
  'A T183CORP for each year on the list, all signed on screen.'),
 ('CRA Confirmation', 'Filed Oldest First'),
 ('The return is transmitted and your CRA confirmation is emailed within 3 '
  'business days.',
  'Transmitted in order, with a CRA confirmation for each within 3 business '
  'days.'),

 ('Nil T2 filing price', 'Cost'),
 ('Nil T2 Filing Price in Brampton', 'What Catching Up Costs in Brampton'),
 ('$300.00 plus HST per tax year. The fee covers preparation, CPA review, the '
  'T183CORP for signature, and electronic transmission to the Canada Revenue '
  'Agency. Each unfiled tax year is a separate return at the same price.',
  'The unit is the year, not the job: $300.00 plus HST per tax year. That '
  'figure includes preparation, the CPA review, the T183CORP and transmission '
  'to the Canada Revenue Agency. Four years behind means four returns, each at '
  'that price, with nothing added for doing them together.'),

 ('File your Brampton nil T2 return', 'Bring your Brampton filings up to date'),
 ('Nil T2 Filing in Brampton: Common Questions',
  'Catching Up in Brampton: What People Ask'),
]

OTTAWA_FAQ = [
 ('The corporation traded last year but not this one. Does that still count?',
  '<p>Yes. The test is applied year by year, not to the corporation as a whole. '
  'A quiet year between two active ones is filed as nil on its own. '
  '<a href="https://corpnilfilingfor300.ca/no-activity-corporation-tax-return-ottawa/">'
  'What no activity means</a>.</p>'),
 ('Can you file only the nil years and leave the rest to my own accountant?',
  '<p>Yes. We file the years that qualify and hand the others back untouched, '
  'so nothing is done twice and nothing is billed twice.</p>'),
 ('Where exactly is the line between nil and not nil?',
  '<p>Any revenue, any expense claimed, any payroll, any movement through the '
  'bank account puts a year on the other side of it. Investment income, rent '
  'and dividends do the same. '
  '<a href="https://corpnilfilingfor300.ca/inactive-holding-corporation-t2-filing-ottawa/">'
  'When a year is not nil</a>.</p>'),
 ('I invoiced once in the year, for a small amount. Is it still nil?',
  '<p>No. One invoice is revenue, so the year is a regular T2 rather than a '
  'nil filing. We tell you that before anything is charged.</p>'),
 ('What is the deadline when the year end is not December?',
  '<p>Six months after whatever your year end is. A March 31 year end is due '
  'September 30. '
  '<a href="https://corpnilfilingfor300.ca/nil-t2-filing-deadline-ottawa/">'
  'Work out your date</a>.</p>'),
 ('How is the return authorised?',
  '<p>With a T183CORP for that tax year, signed on screen. One year, one form. '
  '<a href="https://corpnilfilingfor300.ca/guides/t183corp-signing-and-transmission/">'
  'How signing works</a>.</p>'),
 ('Several quiet years in a row. Are they priced any differently?',
  '<p>No. Each is its own return at $300.00 plus HST per tax year, filed oldest '
  'first. '
  '<a href="https://corpnilfilingfor300.ca/catch-up-nil-t2-filing-ottawa/">'
  'Catch-up filing</a>.</p>'),
 ('Is my Ontario annual return handled at the same time?',
  '<p>No. That one goes to the Ontario Business Registry and sits outside this '
  'service, though we check whether it is outstanding. '
  '<a href="https://corpnilfilingfor300.ca/tools/ontario-annual-return-due-date-calculator/">'
  'Check your date</a>.</p>'),
 ('I am winding the corporation down after a quiet year. What is left to do?',
  '<p>A final T2 covering the period to dissolution, due six months after it. '
  'That is what closes the account. '
  '<a href="https://corpnilfilingfor300.ca/final-t2-before-dissolution-ottawa/">'
  'Final T2 before dissolution</a>.</p>'),
 ('Do I have to be in Canada to sign?',
  '<p>No. The signature is electronic, so a director can authorise the return '
  'from anywhere. '
  '<a href="https://corpnilfilingfor300.ca/nil-t2-filing-for-non-resident-owned-corporations-ottawa/">'
  'Non-resident owned corporations</a>.</p>'),
]

OTTAWA_TEXT = [
 ('Nil T2 filing for Ottawa corporations. One price for every tax year, '
  'with no hourly billing and no add-on fees.',
  'A quiet year for your Ottawa corporation still needs a T2. One flat fee for '
  'that year, filed online.'),

 ('Nil T2 Filing for Ottawa Corporations',
  'Nil T2 Filing in Ottawa for a Year With No Activity'),
 ('A nil T2 is the corporate return an Ottawa corporation files for a tax '
  'year in which it had no revenue, no expenses and no bank activity. The '
  'corporation still exists, so the return is still due. Incorporating and '
  'then going quiet does not end the obligation, and a year left unfiled stays '
  'open until the return is transmitted.',
  'A corporation does not have to be finished to have a nil year. Plenty of '
  'Ottawa companies work steadily, then spend a full tax year without '
  'invoicing anything at all, and pick up again afterwards. That middle year '
  'is still a filing year. It is filed as nil, separately from the years on '
  'either side of it.'),
 ('Nil T2 filing in Ottawa covers the year end to end. The return is '
  'prepared and reviewed, you sign a T183CORP for each tax year, and the '
  'return is transmitted to the Canada Revenue Agency electronically. It is '
  'done online from start to finish, so there is nothing to print, mail or '
  'sign in person, wherever in the city your registered office sits.',
  'Which is why the first thing we do is check the year rather than assume it. '
  'One invoice, one expense claimed or one movement through the bank account '
  'and the year is not nil, and we say so before charging for it. Where it '
  'does qualify, the return is prepared, reviewed by a CPA, signed with a '
  'T183CORP and transmitted. Nepean, Kanata or downtown, the work is the same '
  'and none of it is done in person.'),

 ('One Fee Per Tax Year', 'A Year at a Time'),
 ('No hourly billing and no add-on charges for schedules or transmission.',
  'Each nil year is priced on its own. Active years are not part of this and '
  'are not charged for.'),
 ('Every Unfiled Year Counts', 'Quiet Does Not Mean Exempt'),
 ('Each year is a separate T2 return at $300.00 plus HST per tax year.',
  'A year with nothing in it is still owed, at $300.00 plus HST per tax year.'),
 ('Signed and Filed Online', 'Checked Before It Is Charged'),
 ('Nothing to print. You sign the T183CORP electronically for each tax year.',
  'We confirm the year really was nil first, then send the T183CORP to sign.'),

 ('Corporations in Ottawa', 'Federal Corporations Based in Ottawa', 'exact'),
 ('42,154 active federal business corporations have a registered office in '
  'Ottawa, including the former municipalities of Nepean, Kanata, Gloucester, '
  'Orleans and Stittsville.',
  'Ottawa holds 42,154 active federal business corporations, counting Nepean, '
  'Kanata, Gloucester, Orleans and Stittsville, which became part of the city '
  'in 2001.'),

 ('Nil T2 Filing Services in Ottawa', 'What We File in Ottawa'),

 ('A T2 return for a corporation with no activity in the tax year, CPA '
  'reviewed and transmitted electronically.',
  'One tax year with nothing in it, checked, prepared and sent to the CRA.'),
 ('Several unfiled nil years filed together, oldest year first.',
  'More than one quiet year, filed in date order.'),
 ('For a corporation that has stopped trading but has not been dissolved.',
  'Work has stopped for now; the company and its filings have not.'),
 ('The last return for a corporation being wound up, due within six months of '
  'dissolution.',
  'The closing return, six months from the dissolution date.'),
 ('The two-page T2 Short return, where every CRA condition for using it is met.',
  'The short form, where the CRA\u2019s conditions for it are all met.'),
 ('What the $300.00 fee covers and what it does not.',
  'What sits inside the fee, and what does not.'),
 ('Returns for years already past their due date. An unfiled year stays open '
  'until it is filed.',
  'Years whose date has passed and which remain open.'),
 ('No revenue, no bank activity and no employees. The filing obligation still '
  'applies.',
  'Nothing invoiced, nothing paid, nothing banked, and still a return to file.'),
 ('For a numbered corporation that was incorporated and never traded, or has '
  'gone quiet.',
  'A numbered company between projects, or one that never got going.'),
 ('A holding corporation with investment income, rental income or dividends '
  'paid or received is not nil.',
  'Investment income, rent or dividends take the year out of nil territory.'),
 ('Due within six months of the fiscal year-end, every year, until the '
  'corporation is dissolved.',
  'Six months from your year end, whichever month that falls in.'),
 ('Nil filing where the shareholders are outside Canada.',
  'Where the people behind the corporation are outside Canada.'),

 ('What You Get for $300.00 in Ottawa', 'What the Fee Buys'),
 ('CPA Prepared and Reviewed', 'The Year Is Checked First'),
 ('Your T2 is prepared and reviewed by a CPA Ontario registered firm, Firm '
  'Registration 61330051, before it is transmitted.',
  'Before anything is prepared, a CPA Ontario registered firm, Firm '
  'Registration 61330051, confirms the year qualifies.'),
 ('Registered EFILE Electronic Filer', 'Transmitted, Not Posted'),
 ('The return goes to the Canada Revenue Agency electronically, not by mail.',
  'As a registered EFILE electronic filer we send it straight to the CRA.'),
 ('One Price Per Tax Year', 'One Figure, One Year'),
 ('$300.00 plus HST per tax year, quoted before any work starts. No hourly '
  'billing and no add-on charges.',
  '$300.00 plus HST per tax year, settled at the start and not added to.'),
 ('T183CORP Signed Online', 'Authorised With a T183CORP'),
 ('You receive a T183CORP for each tax year and sign it electronically. One '
  'form per year.',
  'A T183CORP covers one tax year and is signed on screen.'),
 ('CRA Confirmation in Writing', 'Confirmation You Can Keep'),
 ('Your CRA confirmation is emailed within 3 business days of transmission.',
  'The CRA confirmation is emailed within 3 business days of transmission.'),
 ('We Tell You If You Are Not Nil', 'Told Early If the Year Does Not Qualify'),
 ('A corporation with investment income, rental income, or dividends paid or '
  'received is not nil. We tell you before any further charge.',
  'Investment income, rent or dividends received or paid mean the year is not '
  'nil. You hear that before any further charge.'),

 ('How it works', 'The steps'),
 ('How Nil T2 Filing Works in Ottawa', 'Check the Year, Then File It'),
 ('Four steps, all online. You send the corporation details, a CPA prepares '
  'and reviews the return, you sign the T183CORP, and the return is '
  'transmitted to the Canada Revenue Agency.',
  'The order matters: the year is tested before it is prepared, so nothing is '
  'charged for a year that turns out not to be nil.'),
 ('Send Details', 'Tell Us the Year'),
 ('Corporation number, tax year end, and which years are unfiled. Online, with '
  'no appointment.',
  'The corporation number, the year end, and the year you believe was quiet.'),
 ('CPA Review', 'We Test It'),
 ('A CPA checks that the year is nil and prepares the T2 return.',
  'A CPA confirms the year meets the nil test, then prepares the return.'),
 ('Sign T183CORP', 'You Authorise'),
 ('You sign one T183CORP for each tax year, electronically.',
  'A T183CORP for that year, signed on screen.'),
 ('CRA Confirmation', 'It Goes to the CRA'),
 ('The return is transmitted and your CRA confirmation is emailed within 3 '
  'business days.',
  'Transmitted electronically, with confirmation emailed within 3 business '
  'days.'),

 ('Nil T2 filing price', 'Price'),
 ('Nil T2 Filing Price in Ottawa', 'What a Quiet Year Costs in Ottawa'),
 ('$300.00 plus HST per tax year. The fee covers preparation, CPA review, the '
  'T183CORP for signature, and electronic transmission to the Canada Revenue '
  'Agency. Each unfiled tax year is a separate return at the same price.',
  '$300.00 plus HST per tax year covers the check, the preparation, the CPA '
  'review, the T183CORP and transmission to the Canada Revenue Agency. Only '
  'years that are genuinely nil are filed under it, and only those are '
  'charged for.'),

 ('File your Ottawa nil T2 return', 'File your Ottawa corporation\u2019s quiet year'),
 ('Nil T2 Filing in Ottawa: Common Questions',
  'Nil Years in Ottawa: Questions We Get'),
]

COPY = {
 'mississauga': {'text': MISSISSAUGA_TEXT, 'faq': MISSISSAUGA_FAQ},
 'brampton':    {'text': BRAMPTON_TEXT,    'faq': BRAMPTON_FAQ},
 'ottawa':      {'text': OTTAWA_TEXT,      'faq': OTTAWA_FAQ},
}
