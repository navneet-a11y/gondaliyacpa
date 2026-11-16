#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Family 10, the twelve /start/first-t2-after-incorporating-in-<year>/ pages.

Navneet, 2026-11-16: "can you not add unique content and create those year
pages". So: a second attempt, written to fix the specific fault that killed
the first one rather than to repeat it.

WHAT KILLED THE FIRST ATTEMPT, AND WHAT IS DIFFERENT HERE
---------------------------------------------------------
On 2026-11-11 nine of these were built at a worst pair of 0.99, with six at
identical byte counts, and deleted. The post-mortem in decisions.md is right
about the cause: the prose was one template with a digit substituted, and the
shared furniture this family mandates -- the three first-year rules, the
ordered step list, the tail and the footer, about 440 words -- was most of
each short page. Two pages that are 70 per cent identical furniture cannot
measure apart however the other 30 per cent is worded.

Three things are different this time.

1. EVERY PAGE CARRIES ITS OWN COHORT TABLE, computed rather than written. A
   corporation incorporated in 2015 has twelve rows and eleven overdue
   returns; one incorporated in 2026 has a single row and nothing overdue.
   The table is different in length, in content and in what it concludes.

2. EVERY PAGE HAS ITS OWN ANGLE, hand-written, and the angles are about
   genuinely different things rather than the same thing at different ages:
   whether the company still exists on the registry, what a demand to file
   is, which side of the mandatory electronic filing line the cohort falls,
   what a holding corporation does to nil status, how to choose a first
   year-end. None of these is a digit swap and none of them is reusable on a
   neighbouring year.

3. THE UNIQUE BODY IS LONG ENOUGH TO DOMINATE. The furniture is unchanged, so
   the only way to move the ratio is to make the per-cohort half substantial.
   Roughly 700 to 900 words of it per page against 440 of furniture, where
   the first attempt had a few hundred.

MEASURED, NOT ASSUMED. similarity_years.py runs the same 6(k) measurement the
Family 4 pages use, on these twelve plus the fourteen Family 10 pages already
live. The threshold is 0.60. If the batch does not come in under it, it is not
published: that is the whole lesson of the first attempt, and of the four
Atlantic cost pages before it.

THE SLUG CARRIES A YEAR, WHICH 6(a) FORBIDS
--------------------------------------------
6(a)'s URL grammar, stated as fixed for all 1,423 URLs, says "no dates in the
path, no numbers in the path except a competitor price page". These twelve
slugs are Appendix A's own, and every one of them contains a year.

The deviation is logged rather than resolved here. The argument for taking
Appendix A's spelling is that the Family 9 year-stamp rule, which is where the
plan explains why years do not belong in URLs, is about FRESHNESS stamps: a
guide re-stamped 2026 then 2027 would get a new URL every January and reset its
own ranking, so the plan says one URL per topic forever. That reasoning does
not reach these pages. "Incorporated in 2015" is a fixed historical cohort, not
a freshness stamp. The 2015 page is about 2015 permanently and is never
re-stamped. The set grows by one page a year, at the rollover, and no existing
URL is ever retired or redirected.

That is a reading, not a ruling. **Sharad Gondaliya should confirm it**, and
until he does these twelve are the only URLs on the site with a number in the
path.
"""
import io, json, os, re

from _years_extra import MORE, STEPS, TOOLS, COUNT, NEIGH
from build_f10 import (
    SITE, OPEN, FORM, T, G, A, START, COST, HUB, PRICE, OVERFLOW, BYLINE,
    STYLE, RULE53, SCHED24, FOOT, crumb, hero, schema, rules_block,
    steps_block, BANNED,
)

HERE = os.path.dirname(os.path.abspath(__file__))
TODAY, ISO = 'November 16, 2026', '2026-11-16'
NOW_YEAR = 2026
FIRST, LAST = 2015, 2026

# Status is stated as at the review date, so a page never claims a return is
# overdue before it is. A December 31 year-end makes the T2 due June 30 of the
# following year, which is the worked assumption every table states in its own
# caption rather than leaving implicit.
AS_AT_Y, AS_AT_M, AS_AT_D = 2026, 11, 16


def overdue(tax_year):
    """Is the T2 for this tax year past due as at the review date?"""
    due_y, due_m, due_d = tax_year + 1, 6, 30
    return (due_y, due_m, due_d) < (AS_AT_Y, AS_AT_M, AS_AT_D)


def outstanding(year):
    return [y for y in range(year, LAST + 1) if overdue(y)]


def money(n):
    return '${:,}.00'.format(n)


def table(year):
    """The cohort's own tax years. Different length and different content on
    every page, which is the point: this is the block that cannot be shared."""
    rows = []
    for y in range(year, LAST + 1):
        first = ' (short first tax year)' if y == year else ''
        state = ('Overdue' if overdue(y)
                 else 'Not yet due')
        rows.append('<tr><td>%d%s</td><td>December 31, %d</td>'
                    '<td>June 30, %d</td><td>%s</td></tr>'
                    % (y, first, y, y + 1, state))
    n = len(outstanding(year))
    return ('<table class="cnf-tbl"><thead><tr>'
            '<th scope="col">Tax year</th><th scope="col">Year-end</th>'
            '<th scope="col">T2 due</th><th scope="col">Position</th>'
            '</tr></thead><tbody>' + ''.join(rows) + '</tbody></table>'
            '<p class="cnf-cap">Worked for a corporation incorporated in %d '
            'that chose a December 31 year-end, which makes each T2 due June '
            '30 of the following year. A different year-end moves every due '
            'date but not the number of returns. Position is stated as at %s. '
            'The six-month rule comes from the Income Tax Act and does not '
            'vary by province.</p>' % (year, TODAY))


# ---------------------------------------------------------------------------
# The twelve angles. Each is written about something the neighbouring years do
# not raise, which is what keeps the pages apart. Nothing here is a figure that
# could not be sourced: the six-month rule, the 53-week limit, Schedule 24, the
# mandatory electronic filing line for tax years starting after 2023, and its
# $1,000.00 and $100.00 penalties all come from the plan or the Act.
# ---------------------------------------------------------------------------
ANGLES = {

 2015: dict(
  h2='The First Question Is Whether the Company Still Exists',
  sub='Eleven Returns Outstanding',
  lede='A corporation registered in 2015 that never filed has eleven '
       'outstanding T2 returns and, usually, a registry problem as well.',
  paras=[
   'A corporation that has filed no tax return since 2015 has almost '
   'certainly not filed its annual returns with the registry either, because '
   'the two get forgotten by the same person for the same reason. Those are '
   'different filings made to different bodies, and the registry is the one '
   'with the power to strike the company off. So the first thing to establish '
   'for a 2015 corporation is not what it owes the Canada Revenue Agency. It '
   'is whether the company is still on the register at all.',
   'This matters because the answer changes what we are filing. A corporation '
   'that is still registered files eleven ordinary nil returns. A corporation '
   'that has been dissolved by the registrar has a final tax year that ended '
   'on dissolution, and the returns run to that date and stop. Filing eleven '
   'years for a company that stopped existing in 2019 produces returns the '
   'Agency will not match to anything.',
   'Nothing about the delay reduces what is owed in filings. An unfiled '
   'return does not become statute-barred: the normal reassessment period '
   'runs from the date a return is assessed, so a year that was never filed '
   'has never started its clock and stays open indefinitely. Eleven years is '
   'not too late, and it is not a reason to leave the twelfth.',
  ],
  close='We establish the registry position first, then file what the '
        'corporation actually owes rather than what the calendar suggests.'),

 2016: dict(
  h2='What a Decade of Silence Looks Like From the Agency Side',
  sub='Ten Returns Outstanding',
  lede='Ten years of no returns does not mean the Canada Revenue Agency '
       'stopped expecting them. The account stays open and the expectation '
       'never lapses.',
  paras=[
   'When a corporation gets its Business Number, a corporation income tax '
   'account is opened with it, and that account carries an annual filing '
   'expectation from that point until the corporation is dissolved and the '
   'account is closed. Nothing about a decade of inactivity closes it. The '
   'expectation is recorded against the account every year whether or not '
   'anybody acts on it.',
   'What people read as the Agency having lost interest is usually just the '
   'order work gets done in. A corporation with no income reported is not '
   'where collection effort goes first, so the letters often start years '
   'after the first missed return rather than months. When they do start, '
   'they start from the oldest year, and they ask for all of them.',
   'The practical consequence of ten years rather than one is not a bigger '
   'penalty on a nil year. It is that there is no partial fix. A corporation '
   'cannot bring itself current by filing the recent years and leaving the '
   'early ones, because the gap is what blocks a clearance certificate and '
   'what a demand to file names. The series has to close from the oldest end.',
  ],
  close='We file the whole series in order, oldest year first, so the account '
        'closes rather than shortens.'),

 2017: dict(
  h2='Nobody Kept Records for a Company That Did Nothing',
  sub='Nine Returns Outstanding',
  lede='The usual obstacle to filing nine nil years is not the Agency. It is '
       'the belief that the paperwork has to be found first.',
  paras=[
   'A corporation incorporated in 2017 and never used has no bookkeeping, no '
   'statements anybody filed away and often no idea where the minute book '
   'went. That feels like the blocker, and it is the reason these filings get '
   'postponed year after year. It is worth being precise about what a nil '
   'return actually needs, because it is much less than people assume.',
   'A nil return reports no income and no expenses. What it needs is the '
   'corporation name, the Business Number, the year-end the Agency holds on '
   'file, and a signature from an authorized signing officer on Form '
   'T183CORP. The GIFI schedules it carries report zeroes. There are no '
   'receipts to find, because there were no transactions to receipt.',
   'The one thing that does have to be right is the year-end, and that is a '
   'fact held by the Agency rather than one to be reconstructed from memory. '
   'We confirm it before preparing anything, because a return filed against '
   'the wrong year-end is refused on transmission rather than corrected '
   'afterwards.',
   'Where the corporation did have a transaction nobody remembers, a few '
   'dollars of interest credited on a dormant bank account is the common one, '
   'the year is not nil and we say so before you pay rather than after.',
  ],
  close='Nine years of no paperwork is the normal case for this service, not '
        'an obstacle to it.'),

 2018: dict(
  h2='Eight Years on the Public Record',
  sub='Eight Returns Outstanding',
  lede='A corporation registered in 2018 has been on the corporate rolls for '
       'the whole of the period the Canada Revenue Agency publishes figures '
       'for.',
  paras=[
   'The Agency publishes a count of corporations by jurisdiction, and the '
   'earliest tax year in the current table is 2018. A corporation '
   'incorporated that year has therefore been counted in every year of the '
   'published series, from the first column to the last, whether or not it '
   'ever filed anything. The counts include inactive corporations, which is '
   'the point worth drawing out: being dormant does not take a corporation '
   'off the rolls, and it never has.',
   'That is the whole logic of the nil return in one observation. The '
   'obligation attaches to the corporation existing, not to the corporation '
   'doing anything. A company registered in 2018 and left alone is in the '
   'same statistical population as one that traded every year, and it carries '
   'the same annual filing requirement.',
   'What the published counts do not show is how many of those corporations '
   'are current on their returns, because the count is of corporations on the '
   'rolls rather than of returns received. A corporation can appear in all '
   'six years of the table and have filed in none of them. Being counted is '
   'not evidence of being compliant, and it is the reason a long-dormant '
   'corporation can feel invisible while remaining entirely visible.',
  ],
  close='The count is the same whether the corporation traded or sat, and so '
        'is the fix.'),

 2019: dict(
  h2='Incorporated for a Plan That Did Not Start',
  sub='Seven Returns Outstanding',
  lede='A corporation set up in 2019 and never used is the most ordinary '
       'version of this situation, and the filing obligation started anyway.',
  paras=[
   'Corporations get registered ahead of the thing they are for. Somebody '
   'intends to contract through a company, or to hold an asset in one, or to '
   'take work that required incorporation, and the registration happens '
   'before the work does. When the work then does not happen, the company '
   'stays registered because nobody decides to close something they might '
   'still use.',
   'The filing requirement does not wait for the plan. It begins when the '
   'corporation is registered, and the first T2 is due within six months of '
   'the first year-end regardless of whether the company ever opened a bank '
   'account. A corporation that has never traded owes exactly as many returns '
   'as one that traded and stopped.',
   'There are two ways out of a 2019 registration that was never used, and '
   'both start the same way. Keep the corporation and bring the seven years '
   'current, or close it, in which case the outstanding years have to be '
   'filed first because a clearance certificate will not issue over a gap. '
   'Either road goes through the same returns.',
  ],
  close='The returns are the same work whether the corporation is being kept '
        'or wound up, so the decision about its future can wait until after.'),

 2020: dict(
  h2='A Year With Nothing in It Is Still a Tax Year',
  sub='Six Returns Outstanding',
  lede='A corporation incorporated in 2020 that never traded has six '
       'outstanding returns, every one of them reporting nothing.',
  paras=[
   'The first tax year of a 2020 corporation is usually the one people '
   'hesitate over, because the company was registered and then immediately '
   'did nothing at all. There is an instinct that a year with no activity '
   'whatsoever is not really a tax year and that the first return should '
   'start from whenever the company began operating. That is not how the '
   'return works.',
   'The first tax year runs from the date of incorporation to the first '
   'year-end, and it is a tax year even if it is three weeks long and '
   'contains no transactions. It carries Schedule 24, which is the schedule a '
   'corporation files once in its life, on its first return. Skipping it '
   'because the year looks empty means the first return the Agency ever '
   'receives from the corporation is missing the schedule that identifies it '
   'as a first return.',
   'Everything after that first year is an ordinary nil year. Six returns, '
   'each reporting no income and no expenses, each due six months after its '
   'own year-end, and each one still outstanding until it is filed.',
  ],
  close='An empty year is the easiest return to file and the easiest one to '
        'forget was ever due.'),

 2021: dict(
  h2='Holding Something Is Not the Same as Doing Nothing',
  sub='Five Returns Outstanding',
  lede='Many 2021 corporations were registered to hold an asset rather than '
       'to trade, and holding is where nil status is most often lost.',
  paras=[
   'A corporation registered to hold shares, a property or an investment '
   'account is doing something, in the sense the return cares about, even if '
   'nobody goes to work for it. A holding corporation with investment income, '
   'a rental corporation, and a corporation that paid or received a dividend '
   'are not nil. That is the line this service does not cross, and it is '
   'worth testing before five years of returns get prepared on the wrong '
   'footing.',
   'The commonest way a holding corporation turns out not to be nil is '
   'interest. A balance sitting in a corporate account that credited a few '
   'dollars across the year has earned investment income, and there is no '
   'minimum below which it stops counting. The second commonest is a dividend '
   'moved between related companies that nobody thought of as income because '
   'no cash left the group.',
   'Where the corporation genuinely held its assets through the whole year '
   'and they earned nothing at all, no dividend received, no dividend paid, '
   'no rent, no interest and no inter-company transaction, the year is nil '
   'and we file it here. Where it is not, the work belongs with our sister '
   'office and we route it there before you pay rather than after.',
  ],
  close=OVERFLOW),

 2022: dict(
  h2='Four Years Is Usually When the Letter Arrives',
  sub='Four Returns Outstanding',
  lede='A demand to file is a specific letter with a specific consequence, '
       'and four outstanding years is about where it tends to turn up.',
  paras=[
   'A demand to file names the tax years the Canada Revenue Agency wants and '
   'sets a date. It is not a reminder and it is not the start of a '
   'conversation. The important thing about it is what the Agency may do if '
   'the date passes, which is to assess the corporation itself, without the '
   'return, on figures of its own choosing. That is an arbitrary assessment.',
   'An arbitrary assessment on a corporation that genuinely had no activity '
   'is the worst outcome available here, because it creates a tax debt out of '
   'an estimate for a year in which nothing happened. Reversing it means '
   'filing the actual return anyway and then getting the assessment adjusted, '
   'which is the same work plus an argument. Filing before the date on the '
   'letter avoids the whole sequence.',
   'If a demand has already arrived, it does not change what gets filed. It '
   'changes the order of urgency: the years the letter names go first, and '
   'the rest of the series follows immediately behind so the account closes '
   'rather than partially closes.',
  ],
  close='Four returns filed in one pass is a smaller job than one arbitrary '
        'assessment reversed.'),

 2023: dict(
  h2='The Last Cohort That Could Have Filed Its First Return on Paper',
  sub='Three Returns Outstanding',
  lede='Mandatory electronic filing reaches tax years that start after 2023, '
       'which puts a 2023 corporation on the boundary.',
  paras=[
   'For tax years starting after 2023, electronic filing is mandatory for '
   'virtually all corporations, and a paper T2 filed in breach of that draws '
   'a $1,000.00 penalty, with a separate $100.00 penalty on the preparer. A '
   'corporation incorporated in 2023 has a first tax year that started in '
   '2023, so that first return sits on the near side of the line while every '
   'later year of the same corporation sits on the far side.',
   'This produces a split that no other cohort has. The 2023 return could '
   'lawfully have gone in on paper. The 2024 and 2025 returns could not. A '
   'corporation catching up all three now is filing across a rule change, and '
   'the returns on the far side carry a penalty exposure that has nothing to '
   'do with how much tax is owed, because the penalty is for the method '
   'rather than the amount.',
   'In practice the split changes nothing about how we file, because all '
   'three go electronically regardless. It matters for anyone who has been '
   'told that a dormant corporation can simply post its returns in. That was '
   'never good advice and for the later years it is now an expensive one.',
  ],
  close='We transmit every year electronically, which keeps the whole series '
        'on the right side of the rule.'),

 2024: dict(
  h2='The First Cohort Entirely Inside Mandatory Electronic Filing',
  sub='Two Returns Outstanding',
  lede='A corporation incorporated in 2024 has never had a tax year that '
       'could be filed on paper.',
  paras=[
   'Mandatory electronic filing applies to tax years starting after 2023. A '
   'corporation registered in 2024 has a first tax year that started in 2024, '
   'so every tax year it will ever have falls under the rule. There is no '
   'boundary to think about and no year of its life that could lawfully be '
   'posted in.',
   'The penalty for getting this wrong is fixed rather than proportional: '
   '$1,000.00 on the corporation for a return filed on paper in breach of the '
   'requirement, and $100.00 on the preparer. Neither depends on the tax '
   'owing, which means a nil return filed the wrong way costs more than a nil '
   'return filed the right way by exactly those amounts. It is the one place '
   'in this subject where a dormant corporation can generate a real bill.',
   'Two returns is also still a small enough series to close before it grows. '
   'The third year-end falls on December 31, 2026 and its return follows six '
   'months later, so a corporation that files now is current rather than '
   'catching up.',
  ],
  close='Both returns go electronically, which is the only way they may go.'),

 2025: dict(
  h2='Your First Return Is Already Overdue',
  sub='One Return Outstanding',
  lede='A corporation incorporated in 2025 with a December 31 year-end had '
       'its first T2 due on June 30, 2026, so one return is outstanding now.',
  paras=[
   'This is the cohort where the first return has just gone past its date, '
   'and it is worth being plain about what that means for a corporation that '
   'owes no tax. A percentage late-filing penalty is a percentage of tax '
   'owing, and a true nil return owes $0.00, so the percentage has nothing to '
   'apply to. What is left is everything else: the year stays open '
   'indefinitely, it invites a demand to file and an arbitrary assessment, it '
   'blocks a clearance certificate and dissolution, and for a '
   'non-resident-owned corporation it runs at $25.00 per day up to $2,500.00.',
   'The first return is also the one that has to be right about two things no '
   'later return raises. The first tax year cannot exceed 53 weeks, which '
   'constrains the year-end a corporation incorporated part-way through 2025 '
   'could legitimately have chosen. And the year-end on the return has to '
   'match the one the Agency holds, or the transmission is rejected rather '
   'than corrected.',
   'One return is the smallest version of this job and the one most worth '
   'doing immediately, because the series stops at one only if the next '
   'year-end is met on time.',
  ],
  close='Filing the first year now keeps the corporation current instead of '
        'starting a series.'),

 2026: dict(
  h2='Nothing Is Overdue Yet, and That Is the Useful Part',
  sub='First Return Not Yet Due',
  lede='A corporation incorporated in 2026 has no outstanding return. The '
       'decisions that matter are the ones taken before the first year-end.',
  paras=[
   'This is the only page in this series where the answer is not a catch-up. '
   'A corporation registered in 2026 has a first tax year that has not ended '
   'or has only just ended, and a first T2 that is not due until six months '
   'after whichever year-end it adopts. Everything about the rest of this '
   'series is avoidable from here.',
   'The one decision with lasting consequences is the first year-end, because '
   'the first tax year cannot exceed 53 weeks from the date of incorporation. '
   'That sets an outer limit on how far out the first year-end can be placed, '
   'and the date chosen then fixes every deadline the corporation will ever '
   'have. The Agency records the year-end it is given, and every later return '
   'is matched against that record.',
   'The first return itself carries Schedule 24, which a corporation files '
   'once, and the nil GIFI schedules if the year had no activity. Filing it '
   'on time, even reporting nothing, is what keeps the corporation out of the '
   'position the 2015 page describes.',
  ],
  close='A corporation that files its first year on time never needs any of '
        'the other eleven pages in this series.'),
}


def steps_for(year):
    """The ordered list, written once per cohort in _years_extra.STEPS.

    The shared seven-step block was 126 identical words on every page, and
    with the tail, the count paragraph and the footer it was about half of
    each page by word count. Two pages cannot measure apart while half of
    both is the same text. The order genuinely does differ by cohort -- a
    2015 corporation starts at the registry, a 2026 one starts at a year-end
    it has not chosen yet -- so this is a real difference written down twelve
    times, not padding to move a number.
    """
    return STEPS[year]


def steps_html(year):
    return ('<h2>The Order It Happens In</h2><ol class="cnf-steps">'
            + ''.join('<li>' + s + '</li>' for s in steps_for(year))
            + '</ol>')


# The closing links, written once per cohort in _years_extra.TOOLS.
def tail_for(year):
    return '<p>' + TOOLS[year] + '</p>'


def neighbours(year):
    """Line 1532 wants at least three inbound links per page, measured within
    the batch. Linking only the two adjacent cohorts leaves the second and
    second-last page on two inbound, so the window is two either side plus the
    ends of the series. That also happens to be the comparison a reader wants:
    the year before, the year after, and the two extremes."""
    want, seen = [], set()
    for y in (year - 1, year + 1, year - 2, year + 2, FIRST, LAST):
        if y != year and FIRST <= y <= LAST and y not in seen:
            seen.add(y)
            want.append(y)
    return want[:5]


def slug_for(year):
    return 'first-t2-after-incorporating-in-%d' % year


def page(year):
    a = ANGLES[year]
    out = outstanding(year)
    n = len(out)
    slug = slug_for(year)
    title = 'First T2 After Incorporating in %d' % year
    url = START + slug + '/'

    b = []
    b.append('<h2>' + a['h2'] + '</h2>')
    for p in a['paras']:
        b.append('<p>' + p + '</p>')
    b.append('<p>' + MORE[year] + '</p>')

    b.append('<h2>Every Tax Year a %d Corporation Owes</h2>' % year)
    b.append(table(year))

    if n:
        b.append('<p>%s <strong>%d outstanding %s</strong> as at %s, at %s '
                 'each, so %s before tax for the series.</p>'
                 % (COUNT[year], n, 'return' if n == 1 else 'returns', TODAY,
                    PRICE, money(300 * n)))
    else:
        b.append('<p>%s The first return falls due on June 30, 2027 for a '
                 'December 31 year-end, and filing it costs %s.</p>'
                 % (COUNT[year], PRICE))

    b.append(rules_block())
    b.append(steps_html(year))

    b.append('<h2>' + ('What We Do With the Series' if n else
                       'What Happens Next') + '</h2>')
    b.append('<p>' + a['close'] + '</p>')

    nb = neighbours(year)
    b.append('<h2>The Cohorts Either Side of This One</h2>')
    b.append('<p>' + NEIGH[year] + ' '
             + ' '.join(
                 'A corporation registered in %d is covered on '
                 '<a href="%s%s/">first T2 after incorporating in %d</a>.'
                 % (y, START, slug_for(y), y) for y in nb)
             + ' The whole subject starts at <a href="' + START + HUB
             + '/">first T2 return after incorporation</a>.</p>')

    b.append('<h2>Where the Rest of the Answer Is</h2>')
    b.append(tail_for(year))
    b.append('<p>If the corporation does not exist yet, incorporation is a '
             'separate step on a separate site: '
             '<a href="' + OPEN + '">opencorporationfor35.ca</a> covers it, '
             'and this page picks up once the corporation is registered.</p>')
    b.append('<p>Filing here is ' + PRICE + '. See the full '
             '<a href="' + COST + '">nil T2 filing cost</a> and what it '
             'covers.</p>')
    b.append('<p><a class="cnf-btn" href="' + FORM + '">'
             'Start Nil T2 Filing NOW</a></p>')

    desc = ('%s A corporation incorporated in %d has %s. %s'
            % (a['lede'].split('.')[0] + '.', year,
               ('%d outstanding T2 %s' % (n, 'return' if n == 1 else 'returns'))
               if n else 'no outstanding T2 return yet',
               PRICE + '.'))[:155]

    h = [STYLE + hero(title, a['sub'], a['lede'])]
    h.append('<div class="cnf-w" style="max-width:1000px!important;'
             'margin:0 auto!important;padding:36px 20px 56px!important;'
             'box-sizing:border-box">')
    h.append(crumb(title))
    h.append('<p class="cnf-by">' + BYLINE + '</p>')
    h.append('<p class="cnf-rev">Last reviewed: ' + TODAY + '</p>')
    h.append('\n'.join(b))
    h.append(FOOT)
    h.append('</div>')
    h.append(schema(url, title, desc, ISO))
    return slug, title, desc, '\n'.join(h)


# The year totals, the two mandatory-electronic-filing penalties and the
# non-resident daily penalty and its cap. Each is a figure the page computes or
# the plan states; nothing here is an estimate.
MONEY_OK = ({'0.00', '300.00', '350.00', '12.00', '25.00', '100.00',
             '1,000.00', '2,500.00'}
            | {'{:,}.00'.format(300 * k) for k in range(1, 12)})


def gate(slug, html):
    low, bad = html.lower(), []
    if SCHED24 not in html:
        bad.append('line 1218: the Schedule 24 line is missing')
    if RULE53 not in html:
        bad.append('line 1218: the 53-week line is missing')
    for w in BANNED:
        if w in low:
            bad.append('banned phrase %r' % w)
    if re.search(r'\bauthorized\b', low.replace('authorized signing officer', '')):
        bad.append('rule 1 stray "authorized"')
    for m in re.finditer(r'EFILE', html):
        if not html.startswith('EFILE electronic filer', m.start()):
            bad.append('rule 1 EFILE outside the approved phrase')
            break
    if re.search(r'\bT183\b(?!CORP)', html):
        bad.append('rule 2 bare T183')
    # Hard rule 3: the penalty position never appears without its whole
    # qualification block. The 2025 page is the only one that raises it.
    if 'late-filing penalty' in low and 'blocks a clearance certificate' not in low:
        bad.append('rule 3: penalty mentioned without the 7.4 qualification')
    for w in ('howto', 'faqpage', 'aggregaterating', 'trustindex', '"review"'):
        if w in low:
            bad.append('rule 6 forbidden schema %r' % w)
    if '<ol' not in html:
        bad.append('line 344: steps must render as an ordered list')
    # Hard rule 8: the holding page must say such a corporation is not nil.
    if 'holding corporation' in low and 'are not nil' not in low:
        bad.append('rule 8: holding corporation named without the not-nil line')
    if PRICE not in html:
        bad.append('rule 9 price line missing')
    if 'plus HST' in html or 'including HST' in html:
        bad.append('rule 9: names HST on a page that covers every province')
    for m in re.finditer(r'\$(\d{1,3}(?:,\d{3})*\.\d\d)', html):
        if m.group(1) not in MONEY_OK:
            bad.append('unexpected money figure $%s' % m.group(1))
    if html.count('<h1>') != 1:
        bad.append('%d H1' % html.count('<h1>'))
    if html.count('<table') != 1:
        bad.append('%d tables, needs exactly 1' % html.count('<table'))
    if 'CPA Ontario Membership 61040184' not in html:
        bad.append('no byline')
    if 'Last reviewed:' not in html:
        bad.append('no last-reviewed line')
    x = re.findall(r'href="(https?://(?!corpnilfilingfor300\.ca)[^"]*)"', html)
    if len(x) != 1 or not x[0].startswith(OPEN):
        bad.append('line 1532: need exactly 1 cross-domain link, got %r' % x)
    links = set(re.findall(
        r'href="(https://corpnilfilingfor300\.ca[^"]*)"', html))
    if len(links) > 25:
        bad.append('%d outbound internal links, cap is 25' % len(links))
    if any(ord(c) > 0x2100 for c in html):
        bad.append('non-ASCII symbol that may be an emoji')
    json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                         html, re.S).group(1))
    if bad:
        raise AssertionError('%s GATE FAILED:\n  - %s'
                             % (slug, '\n  - '.join(bad)))
    return links


def _recheck_2018_counts():
    """The 2018 page is the only one that quotes a figure, so the figure is
    re-derived from the data file rather than trusted because it is written
    down. Same rule the Saskatchewan builder applies after three hand-written
    comparative claims turned out not to hold.
    """
    import json as _json
    p = os.path.join(HERE, '..', '..', 'docs', 'seo',
                     'cra-t2-jurisdiction-counts.json')
    J = _json.load(io.open(p, encoding='utf-8'))['jurisdictions']
    assert len(J) == 13, len(J)
    t18 = sum(v['counts'][0] for v in J.values())
    t23 = sum(v['counts'][-1] for v in J.values())
    body = ' '.join(ANGLES[2018]['paras']) + ' ' + MORE[2018]
    for n in ('{:,}'.format(t18), '{:,}'.format(t23), '{:,}'.format(t23 - t18)):
        assert n in body, 'the 2018 page does not carry %s' % n
    assert 'thirteen jurisdictions' in body


if __name__ == '__main__':
    years = list(range(FIRST, LAST + 1))
    _recheck_2018_counts()
    assert set(ANGLES) == set(years), sorted(set(years) ^ set(ANGLES))
    # Line 1717: distinct H1, distinct first 120 words, distinct angle heading.
    assert len({ANGLES[y]['h2'] for y in years}) == 12, 'duplicate angle H2'
    assert len({ANGLES[y]['sub'] for y in years}) == 12, 'duplicate hero sub'
    assert len({ANGLES[y]['lede'] for y in years}) == 12, 'duplicate lede'
    firsts = {ANGLES[y]['paras'][0][:120] for y in years}
    assert len(firsts) == 12, 'the first 120 words must differ'
    # No sentence may appear in two angles. This is the check the first attempt
    # did not have, and it is what a digit-swapped page fails.
    sent = {}
    for y in years:
        for p in ANGLES[y]['paras']:
            for s in re.split(r'(?<=[.]) ', p):
                s = s.strip()
                if len(s) > 40:
                    assert s not in sent, (
                        'sentence shared by %d and %d: %r' % (sent[s], y, s))
                    sent[s] = y

    recs = []
    for y in years:
        slug, title, desc, html = page(y)
        links = gate(slug, html)
        io.open(os.path.join(HERE, slug + '.html'), 'w',
                encoding='utf-8').write(html)
        words = len(re.sub(r'<[^>]+>', ' ', html).split())
        recs.append(dict(year=y, slug=slug, title=title, desc=desc,
                         url=START + slug + '/', bytes=len(html.encode()),
                         words=words, outstanding=len(outstanding(y))))
        print('%-44s %6d bytes  %4d words  out:%2d  returns:%2d'
              % (slug, len(html.encode()), words, len(links),
                 len(outstanding(y))))

    # Byte counts must not collide: six identical byte counts is what the
    # first attempt produced and is the cheapest possible duplicate signal.
    by = [r['bytes'] for r in recs]
    assert len(set(by)) == 12, 'identical byte counts: %s' % sorted(by)

    # Line 1532: inbound minimum 3, measured within the batch.
    for r in recs:
        n = sum(1 for o in recs if o['slug'] != r['slug']
                and ('/start/' + r['slug'] + '/') in
                io.open(os.path.join(HERE, o['slug'] + '.html'),
                        encoding='utf-8').read())
        assert n >= 3, '%s has only %d inbound, needs 3' % (r['slug'], n)
        r['inbound'] = n

    json.dump(recs, io.open(os.path.join(HERE, 'f10-years-manifest.json'), 'w',
                            encoding='utf-8'), indent=1)
    print('\n%d pages, gate clear on all' % len(recs))
