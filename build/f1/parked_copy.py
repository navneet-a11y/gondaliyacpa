"""Family 1 copy written but not yet published, parked for the next batch.

Both entries were drafted on 2026-11-20 before the Appendix A vertical list
was located, so they are held here rather than in vertical_copy.py: adding
them there would put them in the 6(k) similarity matrix and the visible-text
audit for pages that do not exist. They map to real Appendix A slugs and are
ready to move across:

  rental-property-corporations   Appendix A #82   rule 8 spine, written to
                                                 state plainly that a
                                                 corporation collecting rent
                                                 is not nil
  farming-corporations           Appendix A #75   cash rent on the land,
                                                 grain in the bin, farm
                                                 support programme payments

Neither has been through gate_batch, audit_visible or similarity.py. Run
both gates after moving an entry into VERTICALS.

A third draft, for dormant personal real estate corporations, was discarded:
Appendix A has no personal-real-estate-corporation slug, only
real-estate-brokerage-corporations (#53), so that page would have been
off-plan.
"""

PARKED = {

 'rental-property-corporations': {
  'name':   'Rental Corporations',
  'short':  'rental corporation',
  'plural': 'rental corporations',
  'kw':     'nil t2 for rental corporation',
  'title':  'Rental Corporation T2 | When a Year Is Not Nil',
  'desc':   'A corporation that collected rent in a year is not nil and files '
            'a full T2. The narrow case where a rental corporation does have '
            'a nil year, and what it costs.',

  'h1':   'Nil T2 Filing for Rental Corporations',
  'lede': 'A corporation that collected rent for any part of a tax year is '
          'not nil for that year. Where a full year passed with no rent and '
          'no expense claimed, the return is $300.00 plus HST per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Rental Corporations',
  'intro': (
    'Start with the part that decides it. A rental corporation is not a nil '
    'corporation in any year it collected rent, and rent for one month of '
    'twelve settles the question for the whole year. That year is a full T2 '
    'with income to report, which is $350.00 plus HST per year at '
    'gondaliyacpa.ca.',
    'There is a real nil case and it is narrower than people expect: a '
    'complete tax year in which no rent was received, nothing the '
    'corporation owns earned, and no expense was claimed against the '
    'property. In practice that is the year after the building was sold, or '
    'a year the unit stood empty while the shareholder carried the taxes and '
    'utilities personally. Where the year genuinely looks like that, we file '
    'it at $300.00 plus HST per tax year.'),

  'notnil_h': 'What an Unfiled Year Costs a Rental Corporation',
  'notnil_boxes': [
    ('A Rental Corporation Is Not Nil',
     'Any year with rent in it is a full T2 with income. This is the first '
     'thing tested and it is not a judgement call.'),
    ('The Years Accumulate Quietly',
     'Property is held for a long time, so a corporation that stopped filing '
     'usually owes several years rather than one.'),
    ('The Agency Can Demand Them',
     'A written demand replaces an obligation with no date with one that '
     'carries a deadline.'),
    ('A Sale or Refinancing Reads Them',
     'Lenders and purchasers ask for the corporate returns before a property '
     'moves, and a gap holds the transaction up.'),
  ],
  'notnil_text': (
    'The usual pattern is a corporation that rented a property for years, '
    'stopped at some point, and kept existing. The renting years are ordinary '
    'returns. What can be nil is a complete year on the far side of that, '
    'with no rent, no earnings and nothing claimed.',
    'Those years are $300.00 plus HST per tax year. The renting years are '
    'not, and they are not filed at this price: the year is tested first and '
    'priced afterwards.'),

  'sched_h': 'Which T2 Schedules a Rental Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'The property, the mortgage and any tenant deposit held all sit on the '
     'balance sheet, so it is never empty while the corporation owns '
     'anything.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'In a nil year it reports nil rent and nil expenses. In any year with '
     'rent it carries real figures and the return is not nil.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Travels with the two GIFI schedules and records who prepared the '
     'figures.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Rental corporations are frequently split between family members. Every '
     'holding of 10% or more is listed.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the first T2 after incorporation, often the year the '
     'property was bought.'),
    ('Schedule 8', 'Capital cost allowance', 'Only where claimed',
     'The building is depreciable property, but capital cost allowance is not '
     'claimed in a year with no rental income to claim it against.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, applied to a corporation that owns '
                'rental property. Last reviewed November 20, 2026.',
  'sched_boxes': [
    ('Rent for Part of a Year Counts for All of It',
     'There is no proration. A corporation that received rent in February is '
     'not nil for that tax year.'),
    ('A Deposit Held Is Not Rent Yet',
     'Last month’s rent held against a future month is a liability on '
     'Schedule 100. It becomes income when the month it covers arrives.'),
    ('T776 Is a Personal Form',
     'Where the property is owned personally rather than by the corporation, '
     'the rent belongs on a personal return and the corporation can be nil.'),
  ],
  'chk_yes': [
    'No rent was received by the corporation at any point in the year',
    'No tenant deposit was applied to a month falling in the year',
    'Nothing the corporation owns paid interest, dividends or a gain',
    'No expense was claimed against the property by the corporation',
    'Nothing was sold, transferred or otherwise disposed of',
  ],
  'chk_no': [
    'Rent arrived for any month of the year, from any tenant',
    'A deposit held earlier was applied to a month in this year',
    'The property was sold, gifted or rolled out of the corporation',
    'Mortgage interest, property tax or repairs were claimed by it',
    'A shareholder took rent, salary or a dividend out of it',
  ],
  'chk_both': [
    'A return for every tax year the corporation stays in existence',
    'A signed T183CORP accompanying each of those returns',
    'Schedule 50 once a holder reaches 10%',
    'The provincial or federal annual return, which is not the T2',
    'Clearance before the corporation can be wound up',
  ],

  'why_h': 'Why Rental Corporations Use This Service',
  'why': [
    ('The Rent Test Is Applied Before Anything Else',
     'The year is checked for rent first. Where rent is found, the year is '
     'not taken at this price and is routed to the full corporate service.'),
    ('For the Years Either Side of the Letting',
     'The year before the first tenant and the years after the last one are '
     'what this fee covers.'),
    ('One Amount, Each Quiet Year',
     'Where the year clears the test it is $300.00 plus HST per tax year, '
     'however many years are outstanding.'),
    ('Renting Years Are Priced Properly',
     'A year with rental income is an ordinary T2 and is quoted as one '
     'rather than squeezed into a nil filing.'),
  ],
  'strip': [
    ('Rent Decides It',
     'One month of rent makes the whole tax year an ordinary return.'),
    ('Oldest Outstanding Year First',
     'They are filed in sequence so the property and mortgage balances carry '
     'forward.'),
    ('Signed Without Paper',
     'Each T183CORP is signed in a secure portal with nothing printed.'),
  ],

  'svc_h': 'What a Rental Corporation Usually Needs Next',
  'proc_h': 'How a Rental Corporation Files a Nil Year',
  'proc_lede': 'Four steps from the filing form. The first one decides '
               'whether the year qualifies at all.',
  'proc_note': 'Expect the first step to rule some years out:',
  'steps': [
    ('Test the Year for Rent and Earnings',
     'Rent, applied deposits, interest, dividends and any disposition are '
     'checked. A year with any of them is not filed at the nil price.'),
    ('Confirm Who Owns the Property',
     'Where the title is personal rather than corporate, the rent is '
     'reported personally and the corporate year can be nil.'),
    ('Prepare the Return',
     'Schedules 100, 125, 141 and 50 are completed, with Schedule 24 on a '
     'first return and no capital cost allowance claimed in a nil year.'),
    ('Sign and Transmit',
     'One T183CORP per year, transmitted electronically, with the Agency '
     'confirmation emailed within 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for a Rental Corporation',
  'price_eyebrow': 'One Fee Per Qualifying Year',
  'price_text': (
    'A year that passes the rent test is $300.00 plus HST per tax year. The '
    'fee covers the T2, the GIFI schedules where required, Schedule 50, '
    'Schedule 24 on a first return, the T183CORP package with secure '
    'e-signing, CPA review before transmission, electronic transmission by a '
    'registered EFILE electronic filer, one corrected transmission where the '
    'Agency rejects the first, and the CRA confirmation emailed within 3 '
    'business days. Any year in which the corporation collected rent is a '
    'full T2 at $350.00 plus HST per year at gondaliyacpa.ca.'),

  'geo_h': 'Rental Corporation Filing Across Canada',
  'cta_h': 'Test the Quiet Years and File the Ones That Qualify',

  'faq': [
   ('Is a rental corporation ever nil?',
    'Not in a year it collected rent. A corporation that received rent for '
    'any part of the year is a rental corporation for that year and files a '
    'full T2 with income to report, at $350.00 plus HST per year at '
    'gondaliyacpa.ca. A complete year with no rent, no earnings and no '
    'expense claimed can be nil.'),
   ('The tenant left in March and the unit sat empty. Is that year nil?',
    'No. Rent was received for part of the year, so the whole tax year is an '
    'ordinary return. The next full year, if it stayed empty and nothing was '
    'claimed, can be nil.'),
   ('We sold the building. Is the year of sale nil?',
    'No. A disposition is reported whether it produced a gain or a loss, so '
    'the sale year is a full return. The first complete year after the sale '
    'can be nil, provided the proceeds earned nothing.'),
   ('I hold last month’s rent as a deposit. Does holding it count?',
    'Holding it does not. It sits as a liability until the month it covers '
    'arrives, and it becomes income in the year that month falls.'),
   ('The property is in my own name, not the corporation’s. Who reports the rent?',
    'You do, personally. Where the corporation neither owns the property nor '
    'receives the rent, its own year can be nil even though the property is '
    'earning.'),
   ('I paid the property tax myself and claimed nothing. Is the year nil?',
    'It can be. A cost you carried personally and the corporation did not '
    'claim leaves the corporate year with nothing in it either way.'),
   ('Can capital cost allowance be claimed in a nil year?',
    'No. There is no rental income for the year to claim it against, so the '
    'claim is not made and the building simply carries forward at its '
    'existing cost.'),
   ('Several years were never filed. Can they go in together?',
    'Yes, once each is tested separately. The ones that qualify are $300.00 '
    'plus HST per tax year, the ones with rent are quoted as ordinary '
    'returns, and all of them are filed from the earliest forward.'),
   ('Does the annual return to the registry cover this?',
    'No. The registry filing keeps the corporation in good standing and the '
    'T2 reports its tax year. They are separate filings and neither one '
    'substitutes for the other.'),
   ('We want to transfer the property out and close the corporation. What order?',
    'Outstanding years go in first. The transfer is itself a disposition to '
    'report, and no clearance certificate is issued while a year is missing.'),
  ],
 },

 'farming-corporations': {
  'name':   'Inactive Farming Corporations',
  'short':  'inactive farming corporation',
  'plural': 'inactive farming corporations',
  'kw':     'inactive farm corporation t2',
  'title':  'Inactive Farm Corporation T2 Filing | Nil Returns',
  'desc':   'A farm corporation that seeded nothing still files a T2. Why '
            'renting the land out ends the nil year, where grain in the bin '
            'sits, and what the filing costs.',

  'h1':   'Nil T2 Filing for Inactive Farming Corporations',
  'lede': 'A crop year with nothing seeded is still a tax year. Where the '
          'corporation sold nothing, rented nothing out and received no '
          'program payment, the return is $300.00 plus HST per tax year.',

  'intro_h': 'Flat-Fee Nil T2 Filing for Inactive Farming Corporations',
  'intro': (
    'A farm corporation can go quiet without going away. The land is still '
    'held, the bins may still be full, the equipment is parked, and the '
    'fiscal year end arrives on schedule with a return behind it. Those '
    'years are $300.00 plus HST per tax year.',
    'Whether the operation was wound down on retirement, paused after a '
    'transfer to the next generation, stopped while the land is decided on, '
    'or sat out a season, the year is measured against grain and livestock '
    'sold, land rented out, custom work done and anything received under a '
    'farm support program. The return carries Schedules 100, 125, 141 and 50 '
    'and is transmitted electronically. A year with any of those in it goes '
    'to the full service.'),

  'notnil_h': 'What an Unfiled Year Costs an Inactive Farming Corporation',
  'notnil_boxes': [
    ('The Year Arrives Whether or Not You Seed',
     'A fallow season changes what the return reports. It does not remove the '
     'return.'),
    ('Land Is Held for Decades',
     'A farm corporation that stopped filing usually owes a long run of '
     'years, not one or two.'),
    ('The Agency Can Put a Date On It',
     'A written demand turns an open-ended obligation into one with a '
     'deadline attached.'),
    ('A Transfer or Sale Stops at the Filings',
     'Moving land to the next generation or to a buyer means the corporate '
     'record gets read, and a gap in it holds everything up.'),
  ],
  'notnil_text': (
    'The land keeps its value while the corporation goes quiet, which is '
    'exactly why the corporation is kept. Each year it is kept is a tax year, '
    'and a succession plan is where the missing ones surface.',
    'A year with no sales, no rent and no program payment is $300.00 plus '
    'HST per tax year. Outstanding years are prepared as a set and filed '
    'from the oldest so the inventory and land balances carry through.'),

  'sched_h': 'Which T2 Schedules an Inactive Farming Corporation Files',
  'sched_rows': [
    ('Schedule 100', 'Balance sheet information', 'Required',
     'Land, buildings, grain still in the bin, breeding stock and the '
     'machinery line all keep the balance sheet full through a quiet year.'),
    ('Schedule 125', 'Income statement information', 'Required',
     'Reports nil farm revenue and nil farm expenses for a year in which '
     'nothing was sold and nothing was claimed.'),
    ('Schedule 141', 'Notes checklist', 'Required',
     'Filed with the two GIFI schedules and records who prepared them and on '
     'what basis.'),
    ('Schedule 50', 'Shareholder information', 'Required',
     'Farm corporations are commonly held across a family. Every holding of '
     '10% or more is named here.'),
    ('Schedule 24', 'First-time filer information', 'First return only',
     'Filed with the first T2 after incorporation, frequently the year the '
     'land was rolled in.'),
    ('Schedule 8', 'Capital cost allowance', 'While the machinery is owned',
     'Tractors, combines, bins, fencing and farm buildings stay depreciable '
     'property until they are sold or scrapped, whether or not they were '
     'used.'),
  ],
  'sched_note': 'Source: the schedule requirements the Canada Revenue Agency '
                'sets for a T2 return, applied to a farm corporation that '
                'produced and sold nothing in the tax year. Last reviewed '
                'November 20, 2026.',
  'sched_boxes': [
    ('Renting the Land Out Ends the Nil Year',
     'Cash rent or a crop share received by the corporation is income to it. '
     'A corporation collecting rent on its land is a rental corporation for '
     'that year and is not nil.'),
    ('Grain in the Bin Is Not Yet Income',
     'Unsold inventory sits on Schedule 100 and produces nothing until it is '
     'delivered and paid for. The sale year is the year it counts.'),
    ('A Program Payment Lands in the Year Received',
     'A payment under a farm support program such as AgriStability or '
     'AgriInvest is income to the corporation in the year it arrives, even '
     'for a season already finished.'),
  ],
  'chk_yes': [
    'No grain, livestock or produce was sold by the corporation',
    'No cash rent or crop share was received on land it owns',
    'No custom seeding, harvesting or trucking was done for anyone',
    'No farm support program payment or insurance proceeds arrived',
    'No machinery, quota or land was sold or transferred',
  ],
  'chk_no': [
    'Grain held from an earlier season was delivered and paid for',
    'A neighbour paid cash rent or a crop share for the land',
    'A program or crop insurance payment was received',
    'Custom work was invoiced to another operation',
    'Machinery, quota or a parcel of land changed hands',
  ],
  'chk_both': [
    'A T2 for each tax year the corporation remains in existence',
    'A T183CORP signed for each of those years before it is sent',
    'Schedule 50 once any holding reaches 10%',
    'The provincial or federal annual return, filed separately',
    'Clearance before land can be taken out and the corporation closed',
  ],

  'why_h': 'Why Inactive Farming Corporations Use This Service',
  'why': [
    ('Built for the Seasons Nothing Went In',
     'A retirement year, a year after a transfer, or a season sat out. Those '
     'are the years this fee covers.'),
    ('Rent and Program Payments Are Checked First',
     'Those two are the usual reasons a quiet farm year turns out not to be '
     'nil, so both are tested before anything is charged.'),
    ('A Flat Amount Per Year',
     'Each qualifying year is $300.00 plus HST per tax year, however long '
     'the run of outstanding years is.'),
    ('Selling Years Go to the Full Return',
     'A year with a delivery, rent or a program payment in it is prepared as '
     'an ordinary corporate return at the higher fee.'),
  ],
  'strip': [
    ('A Fallow Year Still Reports',
     'The obligation follows the corporation, not the crop plan.'),
    ('Oldest Season First',
     'Returns go in date order so inventory and land values carry forward '
     'correctly.'),
    ('Nothing to Drive Into Town For',
     'The T183CORP for each year is signed in a secure portal.'),
  ],

  'svc_h': 'What an Inactive Farming Corporation Usually Needs Next',
  'proc_h': 'How an Inactive Farming Corporation Files',
  'proc_lede': 'Four steps from the filing form, with the income test ahead '
               'of the paperwork.',
  'proc_note': 'Most of this comes off one year of bank statements:',
  'steps': [
    ('Test the Year for Receipts',
     'Deliveries, cash rent, crop shares, custom work and program payments '
     'are all checked before the year is treated as nil.'),
    ('Fix the Fiscal Year End',
     'Farm corporations often run a year end set around the crop cycle '
     'rather than December. It has to match the Agency record to transmit.'),
    ('Prepare the Return',
     'Schedules 100, 125, 141 and 50 for the year, Schedule 24 where it is '
     'the first return, and Schedule 8 while machinery is owned.'),
    ('Sign and Transmit',
     'One T183CORP for each year in the run, transmitted electronically, '
     'with the Agency confirmation emailed within 3 business days.'),
  ],

  'price_h': 'Nil T2 Filing Cost for an Inactive Farming Corporation',
  'price_eyebrow': 'One Fee Per Tax Year',
  'price_text': (
    'A season with nothing sold and nothing received is $300.00 plus HST per '
    'tax year. The fee covers the T2, the GIFI schedules where required, '
    'Schedule 50, Schedule 24 on a first return, the T183CORP package with '
    'secure e-signing, CPA review before transmission, electronic '
    'transmission by a registered EFILE electronic filer, one corrected '
    'transmission where the Agency rejects the first, and the CRA '
    'confirmation emailed within 3 business days. A year with a delivery, '
    'cash rent or a program payment in it is $350.00 plus HST per year at '
    'gondaliyacpa.ca.'),

  'geo_h': 'Farm Corporation Filing Across Canada',
  'cta_h': 'File the Quiet Seasons Before the Land Moves',

  'faq': [
   ('We seeded nothing last year. Does the corporation still file?',
    'Yes, for every tax year it is in existence. A fallow season is reported '
    'as a year with no revenue rather than skipped.'),
   ('We rent the land to a neighbour now. Is the corporation nil?',
    'No. Cash rent or a crop share received by the corporation is income to '
    'it, which makes it a rental corporation for that year and the return an '
    'ordinary one at $350.00 plus HST per year at gondaliyacpa.ca.'),
   ('There is grain in the bin from two seasons ago. Does that count?',
    'Not until it is sold. Unsold inventory sits on the balance sheet, and '
    'the year it is delivered and paid for is the year it becomes income.'),
   ('A program payment arrived for a season we had already finished. Which year?',
    'The year it was received. That year becomes an ordinary return and the '
    'years around it can still be nil.'),
   ('The land was transferred to my son but the corporation still holds some. Do we file?',
    'Yes, while the corporation exists. The transfer itself is a disposition '
    'to report in its year, and the quiet years afterwards are filed on their '
    'own terms.'),
   ('Can capital cost allowance be claimed on machinery that sat all year?',
    'There is no farm income in a nil year to claim it against, so the claim '
    'is not made and the machinery carries forward at its existing cost.'),
   ('I did a bit of custom combining for a neighbour. Is the year still nil?',
    'No, if the corporation invoiced for it. Custom work billed by the '
    'corporation is revenue to it, however small.'),
   ('Our year end is not December 31. Does that complicate it?',
    'No, provided it matches what the Agency holds. The return is prepared to '
    'that date, and a mismatch is what causes a rejected transmission.'),
   ('Six years were never filed. Can they all go in?',
    'Yes. Each is its own T2 and T183CORP at $300.00 plus HST per tax year, '
    'and they are sent from the oldest so the land and inventory balances '
    'reconcile down the run.'),
   ('We want to wind the corporation up and keep the land personally. What order?',
    'The outstanding returns first. Taking the land out is a disposition to '
    'report, and no clearance certificate is issued while a year is missing.'),
  ],
 },

}
