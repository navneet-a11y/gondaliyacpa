# -*- coding: utf-8 -*-
"""Per-year step lists, closing tool blocks and one extra paragraph each.

Split into its own module because build_f10_years.py was already long and
because these three dicts are the whole answer to the 6(k) measurement: the
shared seven-step block, the shared tail and the shared count paragraph were
about half of every page by word count, and two pages cannot measure apart
while half of both is the same text. Everything here is written twelve times.
"""

# One further paragraph per cohort, on what people get wrong about THIS year
# rather than about catching up generally.
MORE = {
 2015: 'The other thing a 2015 corporation often has is a director who is no '
       'longer involved. Resigning does not transfer the filing history, and '
       'it does not remove the returns from the corporation. Whoever holds '
       'the corporation now inherits the whole series, which is why the '
       'registry search comes before anything else: it establishes who is '
       'currently on record as able to sign Form T183CORP at all.',
 2016: 'There is a belief that an account with no activity eventually gets '
       'closed by the Agency for inactivity, in the way a bank closes a '
       'dormant account. That does not happen. A corporation income tax '
       'account is closed when the corporation is dissolved and somebody '
       'asks for it to be closed, and not otherwise. Ten years of nothing is '
       'ten years of an open account with ten unmet expectations recorded '
       'against it.',
 2017: 'The second thing people try to find is a prior accountant. If a '
       'corporation was incorporated in 2017 by a lawyer or an incorporation '
       'service, there often was no accountant, because there was nothing to '
       'account for. No prior filing history is not a gap in the record to '
       'be explained; for a corporation that never traded it is the expected '
       'state, and the first return we transmit is simply the first return '
       'the corporation has ever filed.',
 2018: 'The size of that population is worth stating, because it is where '
       'the intuition that somebody must have noticed comes from. The Agency '
       'assessed returns from 2,422,910 corporations across the thirteen '
       'jurisdictions for the 2018 tax year, and 2,698,230 for 2023, a rise '
       'of 275,320. A corporation that has filed nothing since 2018 is one '
       'dormant file among millions of active ones, which explains why the '
       'letters are slow and why they still arrive.',

 2019: 'The year also matters for what the corporation was probably going to '
       'be used for. A 2019 registration that was never activated is usually '
       'a trading company that never traded, rather than a holding company '
       'that holds something, and the distinction decides whether the years '
       'are nil at all. A holding corporation with investment income, a '
       'rental corporation and a corporation that paid or received a '
       'dividend are not nil. A company that holds nothing and earns nothing '
       'is the straightforward case this service is built for.',
 2020: 'The first tax year is also where the 53-week limit does real work. A '
       'corporation incorporated late in 2020 could not lawfully have run '
       'its first tax year to the end of 2021, because that would exceed 53 '
       'weeks. If somebody has told the Agency a year-end that implies a '
       'longer first year, the record needs correcting before any return is '
       'transmitted against it, because the return is matched to the date on '
       'file rather than the date on the return.',
 2021: 'Where a 2021 corporation does hold something, the year it acquired '
       'it matters as much as the year it was registered. A company that was '
       'genuinely empty for its first two years and then received an asset '
       'has nil years and non-nil years in the same series, and they are not '
       'filed the same way. We split the series at that point rather than '
       'treating five years as one block.',
 2022: 'A demand to file is also not the only letter that arrives. A request '
       'to file is softer, carries no assessment power, and is easy to '
       'mistake for the demand. The difference worth knowing is that only the '
       'demand carries the arbitrary assessment behind it, so the letter '
       'should be read for what it actually threatens rather than filed with '
       'the rest of the post.',
 2023: 'There is a second reason the 2023 cohort is worth separating out. A '
       'corporation incorporated late in 2023 may have chosen a first '
       'year-end in 2024, which starts its first tax year in 2023 but ends '
       'it in 2024. The rule turns on when the tax year starts, not when it '
       'ends, so that corporation is still on the near side of the line for '
       'its first return. It is the one case where reading the year-end '
       'rather than the incorporation date gives the wrong answer.',
 2024: 'The absence of a boundary is itself worth saying plainly, because a '
       'corporation incorporated in 2024 may have been given advice written '
       'for the years before it. Anything that describes posting a dormant '
       'return in, or treats electronic filing as the convenient option '
       'rather than the required one, is describing a regime this '
       'corporation has never been in.',
 2025: 'The other thing worth settling now is whether the year was genuinely '
       'nil, because a first year often contains the one transaction nobody '
       'counts: incorporation costs paid by the corporation, a share '
       'subscription, or an opening bank deposit. None of those stops the '
       'year being nil. They do make the GIFI schedules required, and those '
       'are included in the fee rather than charged for separately.',
 2026: 'The common mistake at this stage is to assume the first return is '
       'due twelve months after incorporation. It is due six months after '
       'the first year-end, and the year-end is a date the corporation '
       'chooses rather than an anniversary. A corporation incorporated in '
       'March 2026 that picks a December 31 year-end has a first return due '
       'June 30, 2027; one that picks a March 31 year-end has it due '
       'September 30, 2027.',
}

_S24 = ('Complete Schedule 24 on the earliest return, which is the only one '
        'that carries it.')
_GIFI = ('Prepare the nil GIFI schedules for each year: Schedule 100, '
         'Schedule 125 and Schedule 141.')

STEPS = {
 2015: ['Search the registry for the corporation’s current status, '
        'because a company already struck off has a final tax year rather '
        'than an open series.',
        'Identify who is currently on record as able to sign, since the '
        'director who incorporated it in 2015 may no longer be one.',
        'Confirm the year-end the Canada Revenue Agency holds on file.',
        _S24, _GIFI,
        'Sign Form T183CORP for each of the eleven tax years.',
        'Transmit from 2015 forward, so each year is assessed in the order '
        'it fell due.'],
 2016: ['Confirm the corporation income tax account is still open and that '
        'nothing has been assessed against it already.',
        'Confirm the year-end on file, which fixes all ten due dates.',
        'Check whether a demand to file or an arbitrary assessment has '
        'already been issued for any of the ten years.',
        _S24, _GIFI,
        'Sign Form T183CORP for each of the ten tax years.',
        'Transmit the full series rather than the recent years, because a '
        'part-filed account stays blocked.'],
 2017: ['Confirm the incorporation date and the year-end from the Agency’s '
        'record rather than from memory or the minute book.',
        'Establish that each of the nine years was genuinely nil, which for '
        'a company that never traded is a short conversation.',
        'Check the corporate bank account, if there was one, for interest '
        'credited in any year.',
        _S24, _GIFI,
        'Sign Form T183CORP for each of the nine tax years.',
        'Transmit oldest year first and keep all nine confirmations '
        'together, because they are the corporation’s whole filing '
        'history.'],
 2018: ['Confirm the incorporation date, which puts the first tax year in '
        '2018 and the first due date in 2019.',
        'Confirm the year-end the Agency holds, against which all eight '
        'returns are matched.',
        'Establish which of the eight years had no income and no expenses.',
        _S24, _GIFI,
        'Sign Form T183CORP for each of the eight tax years.',
        'Transmit the series in order and keep the confirmations.'],
 2019: ['Settle whether the corporation holds any asset, because a holding '
        'company and a company that never traded are filed differently.',
        'Confirm the incorporation date and the year-end on file.',
        'Confirm each of the seven years had no income and no expenses.',
        _S24, _GIFI,
        'Sign Form T183CORP for each of the seven tax years.',
        'Transmit from the oldest year forward.'],
 2020: ['Confirm the year-end on file and test the first tax year against '
        'the 53-week limit, which a late-2020 incorporation can breach.',
        'Correct the year-end with the Agency first if the record and the '
        'intended date disagree.',
        'Confirm each of the six years had no activity.',
        _S24, _GIFI,
        'Sign Form T183CORP for each of the six tax years.',
        'Transmit the six returns oldest year first.'],
 2021: ['Establish what the corporation holds and when it started holding '
        'it, because that is what decides which years are nil.',
        'Check every year for a dividend paid or received, rent, and '
        'interest credited on any corporate account.',
        'Split the series at the year the corporation stopped being empty, '
        'if it did.',
        'Confirm the year-end on file for the years that are nil.',
        _S24, _GIFI,
        'Sign Form T183CORP for each nil year and transmit those returns '
        'here; the rest are routed to our sister office.'],
 2022: ['Read any letter from the Agency and establish whether it is a '
        'request to file or a demand to file.',
        'File the years a demand names first, and before the date it sets.',
        'Confirm the year-end on file and that all four years were nil.',
        _S24, _GIFI,
        'Sign Form T183CORP for each of the four tax years.',
        'Transmit the remaining years immediately behind the demanded ones, '
        'so the account closes rather than partly closes.'],
 2023: ['Confirm the incorporation date, which fixes when the first tax year '
        'started and therefore which side of the 2023 line it falls on.',
        'Confirm the year-end on file, reading the start of the first tax '
        'year rather than its end.',
        'Confirm all three years were nil.',
        _S24, _GIFI,
        'Sign Form T183CORP for each of the three tax years.',
        'Transmit all three electronically, whatever the rule permitted for '
        'the earliest one.'],
 2024: ['Confirm the incorporation date and the year-end the Agency holds.',
        'Confirm both years were nil, including any interest credited on a '
        'corporate account.',
        _S24, _GIFI,
        'Sign Form T183CORP for both tax years.',
        'Transmit both electronically, which for these tax years is the only '
        'method the rule allows.'],
 2025: ['Confirm the year-end on file and test the first tax year against '
        'the 53-week limit.',
        'Confirm the year had no income and no expenses, treating '
        'incorporation costs and a share subscription as what they are.',
        'Complete Schedule 24, which this return carries because it is the '
        'corporation’s first.',
        'Prepare the nil GIFI schedules for the year: Schedule 100, '
        'Schedule 125 and Schedule 141.',
        'Sign Form T183CORP for the tax year.',
        'Transmit the return electronically and keep the confirmation, which '
        'is the corporation’s first.'],
 2026: ['Choose the first year-end, keeping the first tax year inside 53 '
        'weeks of the incorporation date.',
        'Tell the Canada Revenue Agency that year-end, because every later '
        'return is matched against the date it holds.',
        'Work out the first due date, which falls six months after the '
        'year-end chosen.',
        'Complete Schedule 24 when the first return is prepared.',
        'Prepare the nil GIFI schedules for the first year: Schedule 100, '
        'Schedule 125 and Schedule 141.',
        'Sign Form T183CORP for the first tax year.',
        'Transmit on or before the due date, so the corporation never starts '
        'a series at all.'],
}

# The closing tools block, written twelve times for the same reason as the
# steps: a shared tail is shared text. Each points at the tools a reader in
# that position would actually open next.
T_ = 'https://corpnilfilingfor300.ca/tools/'
G_ = 'https://corpnilfilingfor300.ca/guides/'

TOOLS = {
 2015: ('Eleven years is enough that the arithmetic is worth checking against '
        'your own dates rather than the December 31 assumption above: the '
        '<a href="%soutstanding-returns-count-checker/">outstanding returns '
        'count checker</a> does that. The '
        '<a href="%scatch-up-unfiled-corporate-tax-returns/">guide to '
        'catching up unfiled corporate tax returns</a> covers the sequence '
        'end to end.' % (T_, G_)),
 2016: ('The <a href="%stax-years-since-incorporation-calculator/">tax years '
        'since incorporation calculator</a> counts the years from your own '
        'incorporation date and year-end, and the '
        '<a href="%scra-demand-to-file-response/">guide to the demand to file '
        'letter</a> sets out what the Agency sends and when.' % (T_, G_)),
 2017: ('If the year-end is the thing nobody can find, the '
        '<a href="%stax-years-since-incorporation-calculator/">tax years '
        'since incorporation calculator</a> shows how the count changes with '
        'it. The <a href="%sfirst-year-t2-filing/">first-year T2 filing '
        'guide</a> sets out what a first return actually needs.' % (T_, G_)),
 2018: ('The <a href="%soutstanding-returns-count-checker/">outstanding '
        'returns count checker</a> works the number of returns from your own '
        'dates, and the <a href="%snil-t2-return-complete-guide/">complete '
        'guide to the nil T2 return</a> covers who must file and what a nil '
        'return contains.' % (T_, G_)),
 2019: ('Whether the corporation holds anything is the question to settle '
        'first, and the <a href="%sinactive-holding-corporation-t2-filing/">'
        'inactive holding corporation page</a> sets out where that line '
        'falls. The <a href="%soutstanding-returns-count-checker/">'
        'outstanding returns count checker</a> does the arithmetic.'
        % ('https://corpnilfilingfor300.ca/', T_)),
 2020: ('The <a href="%s53-week-first-tax-year-checker/">53-week checker</a> '
        'tests whether a first year-end chosen in 2020 or 2021 was within '
        'the limit, and the <a href="%stax-years-since-incorporation-'
        'calculator/">tax years since incorporation calculator</a> counts '
        'the returns from your own dates.' % (T_, T_)),
 2021: ('The <a href="%sinactive-holding-corporation-t2-filing/">inactive '
        'holding corporation page</a> sets out exactly when a holding '
        'company is nil and when it is not, which is the question this '
        'cohort turns on. The <a href="%soutstanding-returns-count-checker/">'
        'outstanding returns count checker</a> handles the count.'
        % ('https://corpnilfilingfor300.ca/', T_)),
 2022: ('The <a href="%scra-demand-to-file-response/">guide to the demand to '
        'file letter</a> sets out what the letter is and what follows it, '
        'and the <a href="%soutstanding-returns-count-checker/">outstanding '
        'returns count checker</a> confirms how many years it is likely to '
        'name.' % (G_, T_)),
 2023: ('The <a href="%smandatory-t2-electronic-filing/">guide to mandatory '
        'T2 electronic filing</a> sets out the requirement and what '
        'breaching it costs, and the '
        '<a href="%s53-week-first-tax-year-checker/">53-week checker</a> '
        'tests when a first tax year that began in 2023 actually started and '
        'ended.' % (G_, T_)),
 2024: ('The <a href="%smandatory-t2-electronic-filing/">guide to mandatory '
        'T2 electronic filing</a> is the one to read for this cohort, '
        'because it is the rule that has applied to the corporation from its '
        'first day. The <a href="%sfirst-year-t2-filing/">first-year T2 '
        'filing guide</a> covers the rest.' % (G_, G_)),
 2025: ('The <a href="%s53-week-first-tax-year-checker/">53-week checker</a> '
        'tests the first year-end, the '
        '<a href="%sschedule-24-first-return-checker/">Schedule 24 checker</a> '
        'confirms that this return counts as a first return, and the '
        '<a href="%sfirst-year-t2-filing/">first-year T2 filing guide</a> '
        'covers the whole subject.' % (T_, T_, G_)),
 2026: ('Before anything is filed, the '
        '<a href="%s53-week-first-tax-year-checker/">53-week checker</a> '
        'tests a year-end you are considering and the '
        '<a href="%snil-t2-deadline-calculator/">nil T2 deadline '
        'calculator</a> turns it into the due date it produces. The '
        '<a href="%sfirst-year-t2-filing/">first-year T2 filing guide</a> '
        'covers what the first return carries.' % (T_, T_, G_)),
}

# The paragraph that states the cohort's own arithmetic. Twelve versions,
# because one template with the digits changed is the fault this batch exists
# to avoid.
COUNT = {
 2015: 'Eleven returns, then, each reporting nothing, and none of them '
       'closed by the passage of time.',
 2016: 'Ten returns, and no version of this where filing some of them '
       'settles the account.',
 2017: 'Nine returns, none of which needs a receipt, a statement or a '
       'ledger to prepare.',
 2018: 'Eight returns, one for every year the corporation has been counted '
       'in the published figures.',
 2019: 'Seven returns for a corporation that, in the ordinary sense of the '
       'word, never started.',
 2020: 'Six returns, the first of them short and the other five ordinary '
       'full years.',
 2021: 'Five returns, assuming the corporation held its assets without '
       'earning anything on them throughout.',
 2022: 'Four returns, which is the number a demand to file would name if one '
       'has not arrived already.',
 2023: 'Three returns, spanning a rule change that fell in the middle of '
       'the corporation\u2019s life.',
 2024: 'Two returns, both of them under the electronic filing requirement '
       'from the start.',
 2025: 'One return, and it is the corporation\u2019s first, which is the one '
       'that carries Schedule 24.',
 2026: 'No returns outstanding, which is the only page in this series that '
       'can say so.',
}

# The lead-in to the neighbouring-cohort links. Twelve versions.
NEIGH = {
 2015: 'This is the oldest cohort in the series, and the only direction from '
       'here is fewer returns.',
 2016: 'One year later or one year earlier changes the count but not the '
       'method.',
 2017: 'The cohorts on either side face the same reconstruction problem with '
       'one year more or less of it.',
 2018: 'Either side of 2018 the published series is shorter or the '
       'corporation predates it.',
 2019: 'The years around 2019 are the ones most often registered and then '
       'left.',
 2020: 'The cohorts next to 2020 share the first-year-end question in a '
       'slightly different form.',
 2021: 'The holding question is sharpest for 2021 but it is not unique to '
       'it.',
 2022: 'Earlier cohorts are likelier to have had the letter already; later '
       'ones have not reached it.',
 2023: 'Only 2023 straddles the electronic filing line. The years on either '
       'side sit cleanly on one side of it.',
 2024: 'Every cohort after 2023 is in the same position as this one, and '
       'every cohort before it is not.',
 2025: 'One year earlier and there are two returns behind you; one year '
       'later and there are none.',
 2026: 'This is the newest cohort, and every page before it describes a '
       'position this corporation can still avoid.',
}

assert set(MORE) == set(STEPS) == set(TOOLS) == set(COUNT) == set(NEIGH) == set(range(2015, 2027))
assert len(set(COUNT.values())) == 12 and len(set(NEIGH.values())) == 12
assert len(set(TOOLS.values())) == 12
assert len({tuple(v) for v in STEPS.values()}) == 12, 'duplicate step list'
assert len(set(MORE.values())) == 12, 'duplicate extra paragraph'
