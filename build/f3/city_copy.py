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

COPY = {
 'mississauga': {'text': MISSISSAUGA_TEXT, 'faq': MISSISSAUGA_FAQ},
}
