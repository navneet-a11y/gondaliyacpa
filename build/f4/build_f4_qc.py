# -*- coding: utf-8 -*-
"""Family 4 service x place pages for Quebec: the first five.

Navneet, 2026-11-12: "continue with jurisdiction then follow plan for it", then
"just build main province page and 5 of its pages firsy". So this is the hub
plus five service pages, which is exactly the shape British Columbia opened
with on 2026-10-21 and Alberta on 2026-10-30, and the five are the same five
both of those opened with: nil-t2-filing, catch-up, dormant, final-t2-before-
dissolution and t2-short-filing.

Design, CSS, section order, schema shape and the not-nil wording are imported
from build_f4_bc rather than copied, so the provinces cannot drift apart.

QUEBEC'S SPINE IS THE CO-17, AND THE PLAN STATES IT.
Hard rule 8 requires Quebec pages to say the CO-17 is a separate return, and
plan line 1212 says it outright: "Alberta AT1 and Quebec CO-17 are separate
provincial returns and are not included in the fee". Quebec and Alberta are the
only two provinces that administer their own corporate income tax, so a Quebec
corporation has two corporate income tax returns and two tax authorities rather
than one of each. That is the difference these five pages are built around, and
it is sourced to the signed-off plan rather than to the web.

WHAT THESE PAGES DO NOT SAY, AND WHY.
www.revenuquebec.ca returns 403 to automated clients, so neither corporation
income tax page could be read. None of the following is stated anywhere:
  - the CO-17 filing deadline
  - whether a Quebec corporation with no activity is exempt from the CO-17, or
    may use a simplified return
  - any CO-17 late-filing penalty
  - CO-17.SP and who may use it
  - the Registraire des entreprises, the annual updating declaration, its due
    date, its fee, or how long non-filing runs before dissolution
Each of those is a figure or a rule nobody here has read a source for, and the
Alberta precedent in build_f4_ab is that an unsourceable fact is withheld
rather than estimated. What the pages do say is that the CO-17 exists, is a
separate return filed with a separate tax authority, and is not covered by the
fee. Saying nothing at all would leave a reader thinking the federal T2 is the
whole obligation, which would be a misleading omission on a Quebec page.

THE PLACE DATA ROW IS NOW REAL, FOR THE FIRST TIME ON THIS FAMILY.
Plan line 1212 forbids publishing without a place data row. decisions.md
2026-10-21 recorded the per-jurisdiction count as unfindable, which is why the
British Columbia data row has no count in it. That finding was wrong: the CRA
publishes "T2 Corporate Statistical Tables, Table 1, Number of Corporations by
Jurisdiction, 2018 to 2023", a count table for all thirteen jurisdictions whose
2023 column reproduces the plan's own three figures at line 1743 exactly. See
jur_data.py and docs/seo/cra-t2-jurisdiction-counts.json.

PRICE. Quebec charges GST plus QST, not HST, so the fee reads "$300.00 plus
applicable sales tax per tax year" per Navneet's 2026-11-12 instruction, and no
rate and no tax-inclusive total appears.
"""
import io, json, os

from build_f4_bc import CSS as _CSS, NOT_NIL_1, NOT_NIL_2, a, SITE, FORM

# Navneet, 2026-11-12: "they are going full width fix them", then "move banner
# text little riht as well like other pages".
#
# Astra's full-width container mode overrides the content wrapper's own
# max-width, so .cnf-w and .cnf-hero-in lost their centring and both the body
# copy and the hero ran hard against the left edge. Changing the page's
# site-content-layout meta did NOT fix it -- ast-site-content-layout
# full-width-container is the key that drives it -- so the widths are asserted
# here instead, which holds whichever container mode the page ends up in.
#
# The first diagnosis was that this was a stale cache. It was not: the body
# text sat at the wrapper's own 20px padding, which only happens when the rule
# is applied and the max-width alone is being beaten.
_FIX = (
 "\n.cnf-w{max-width:1000px!important;margin-left:auto!important;"
 "margin-right:auto!important;float:none!important}"
 "\n.entry-content>.cnf-w,.ast-container>.cnf-w{max-width:1000px!important}"
 "\n.cnf-hero-in{max-width:1140px!important;margin-left:auto!important;"
 "margin-right:auto!important;float:none!important}")

assert _CSS.rstrip().endswith('</style>')
CSS = _CSS.rstrip()[:-len('</style>')] + _FIX + '</style>'

import jur_data as JD

HERE = os.path.dirname(os.path.abspath(__file__))
PLACE_SLUG = 'quebec'
J = JD.BY_SLUG[PLACE_SLUG]
PLACE, SHORT = J['name'], J['short']
HUB = SITE + J['hub']
TODAY, ISO = 'November 12, 2026', '2026-11-12'
# The seven services added on 2026-11-13 carry their own review date, as
# Alberta's later seven do: the date on a page is the date its text was
# checked, not the date the province opened.
LATER, LATER_ISO = 'November 13, 2026', '2026-11-13'

FEE = JD.fee(PLACE_SLUG)                      # $300.00 plus applicable sales tax per tax year
FEE_TITLE = JD.fee_title(PLACE_SLUG)
OVERFLOW = JD.overflow(PLACE_SLUG)
PROV_RETURN = JD.prov_return(PLACE_SLUG)      # Quebec CO-17
PLACE_PARA = JD.trajectory(PLACE_SLUG, PLACE)

# Quebec is not an HST province, so the imported not-nil block's overflow fee is
# restated without naming HST. The wording is otherwise untouched.
NOT_NIL_2_QC = NOT_NIL_2.replace('$350.00 plus HST per tax year', OVERFLOW)
assert 'HST' not in NOT_NIL_2_QC

# Section 7.4: the penalty position never appears without the whole
# qualification block. One definition, used wherever a penalty is mentioned.
QUAL = ('A true nil return carries no percentage late-filing penalty, because '
        'that penalty is a percentage of tax owing and the corporation owes '
        '$0.00. The unfiled year still stays open forever, invites a demand to '
        'file and an arbitrary assessment, blocks a clearance certificate and '
        'dissolution, and costs a non-resident-owned corporation $25.00 per day '
        'up to $2,500.00.')

CO17 = ('A Quebec corporation answers to two tax authorities. The federal T2 '
        'goes to the Canada Revenue Agency; the ' + PROV_RETURN + ' goes to '
        'Revenu Quebec, which assesses it on a record of its own and '
        'corresponds about it separately. The ' + PROV_RETURN + ' is not '
        'covered by the $300.00 fee.')

# The twelve cnf_service terms, verbatim from plan line 304. Five are built
# here; the list is checked in full so a typo fails the build.
SERVICE_SLUGS = (
 'nil-t2-filing', 'catch-up-nil-t2-filing', 'dormant-corporation-filing',
 'final-t2-before-dissolution', 't2-short-filing', 'nil-t2-filing-cost',
 'unfiled-corporate-tax-returns', 'no-activity-corporation-tax-return',
 'numbered-corporation-nil-filing', 'inactive-holding-corporation-t2-filing',
 'nil-t2-filing-deadline', 'nil-t2-filing-for-non-resident-owned-corporations')

SERVICES = [

 dict(
  slug='nil-t2-filing-quebec',
  service='nil-t2-filing',
  title='Nil T2 Filing in Quebec',
  keyword='nil t2 filing quebec',
  national=('/nil-t2-filing/', 'nil T2 filing'),
  lead_h2='Nil T2 Filing for Quebec Corporations',
  lead=['A nil T2 is the federal corporate income tax return a Quebec '
        'corporation files for a tax year in which it had no activity. Every '
        'Quebec corporation files a T2 with the Canada Revenue Agency within '
        'six months of its fiscal year-end, every year until it is formally '
        'dissolved, whether or not it earned anything. We prepare the return, '
        'a CPA reviews it, and we transmit it electronically for ' + FEE + '.',
        CO17],
  extra=[('What Makes a Return Nil',
          ['A nil return reports no income and no expenses for the tax year. '
           'The corporation still exists, still has a Business Number, and '
           'still has a fiscal year-end, so the return is still due. Filing it '
           'keeps the corporation&rsquo;s federal tax record current and keeps '
           'its standing with the Canada Revenue Agency intact.']),
         ('Two Assessments, Arriving From Two Places',
          ['The practical consequence of Quebec running its own corporate '
           'income tax is not really a second form. It is that the '
           'corporation has two tax records, each held by a different '
           'authority, each assessed on its own timetable, and each capable '
           'of being up to date while the other is not. A notice from one '
           'says nothing about the state of the other.',
           'We file the federal T2, so what we put right is the Canada '
           'Revenue Agency side. If you have had no federal correspondence '
           'for years, that is not evidence the Revenu Quebec side is clear, '
           'and the ' + PROV_RETURN + ' is not covered by the $300.00 fee. We '
           'say so before you pay rather than after.'])],
  excerpt='Nil T2 filing for Quebec corporations with no activity in the tax '
          'year. ' + FEE + '.'),

 dict(
  slug='catch-up-nil-t2-filing-quebec',
  service='catch-up-nil-t2-filing',
  title='Catch-Up Nil T2 Filing in Quebec',
  keyword='catch-up nil t2 filing quebec',
  national=('/catch-up-nil-t2-filing/', 'catch-up nil T2 filing'),
  lead_h2='Bringing Unfiled Quebec Years Up to Date',
  lead=['If a Quebec corporation has not filed for several years, each of '
        'those years is still outstanding and each one is a separate return. '
        'We file them together, oldest year first, so the Canada Revenue '
        'Agency processes them in the order they fell due. Each tax year is '
        '$300.00 plus applicable sales tax, because each tax year is its own '
        'T2.'],
  extra=[('Why the Oldest Year Goes First',
          ['A T2 carries forward figures from the year before it, so the years '
           'have to be assessed in order. Filing the oldest outstanding year '
           'first means each later return is assessed against a record that is '
           'already up to date, rather than against a gap.',
           'You tell us which years are unfiled and confirm the corporation '
           'had no activity in each of them. If any year turns out not to be '
           'nil, we tell you before you pay for that year.']),
         ('Half of a Quebec Catch-Up Is Not Ours to Do',
          ['The years a Quebec corporation owes federally and the years it '
           'owes provincially are usually the same years, because a '
           'corporation that goes quiet goes quiet on both at once. They are '
           'not the same work. Each set is assessed by its own authority '
           'against its own record, and finishing one leaves the other '
           'exactly where it was.',
           'What we do is the federal half: the T2 for every outstanding '
           'year, oldest first. We tell you how many federal years we found, '
           'which is also the best indication of how many ' + PROV_RETURN + ' '
           'years are likely sitting behind them. Those are not covered by '
           'the $300.00 fee, so you are not paying us twice for the same '
           'year.']),
         ('What a Late Nil Year Actually Costs',
          [QUAL])],
  excerpt='Catch up every unfiled year for a Quebec corporation, oldest year '
          'first. ' + FEE + '.'),

 dict(
  slug='dormant-corporation-filing-quebec',
  service='dormant-corporation-filing',
  title='Dormant Corporation Filing in Quebec',
  keyword='dormant corporation filing quebec',
  national=('/dormant-corporation-filing/', 'dormant corporation filing'),
  lead_h2='Keeping a Dormant Quebec Corporation Up to Date',
  lead=['A dormant Quebec corporation is one that still exists on the register '
        'but has stopped trading, or never started. Being dormant does not '
        'pause anything. The corporation still files a T2 with the Canada '
        'Revenue Agency within six months of each fiscal year-end, every year '
        'until it is formally dissolved. If the dormant corporation had no '
        'activity in the tax year, we file its nil T2 for $300.00 plus '
        'applicable sales tax. Filing does not dissolve the corporation. It '
        'keeps the corporation&rsquo;s tax record clean while you decide '
        'whether to restart it or close it.'],
  extra=[('Dormant Is Not the Same as Dissolved',
          ['A dormant corporation is still a corporation. It still has a '
           'Business Number, still has a fiscal year-end, and still owes a '
           'return for every year it exists. A dissolved corporation has been '
           'formally wound up and stops owing returns after its final one. '
           'Until that final return is filed and the dissolution completes, '
           'the obligation runs on.',
           'The Canada Revenue Agency counts tax-exempt and inactive '
           'corporations in its own figures, which is why a dormant '
           'corporation does not quietly disappear from its records by being '
           'inactive.']),
         ('A Dormant Quebec Corporation Has Two Records to Keep Current',
          ['The federal T2 and the ' + PROV_RETURN + ' are assessed by '
           'different tax authorities on separate records. A corporation that '
           'has gone quiet usually goes quiet on both at once, and bringing '
           'the federal record up to date leaves the provincial one exactly '
           'where it was.',
           'We file the federal nil T2. The ' + PROV_RETURN + ' is not covered '
           'by the $300.00 fee.'])],
  excerpt='A dormant Quebec corporation still files a T2 every year until it '
          'is dissolved. ' + FEE + '.'),

 dict(
  slug='final-t2-before-dissolution-quebec',
  service='final-t2-before-dissolution',
  title='Final T2 Before Dissolution in Quebec',
  keyword='final t2 before dissolution quebec',
  national=('/final-t2-before-dissolution/', 'final T2 before dissolution'),
  lead_h2='The Last Return a Quebec Corporation Files',
  lead=['A corporation being wound up files one last T2 covering the period '
        'ending on the date of dissolution, and that return is due within six '
        'months of the dissolution date. If the corporation had no activity in '
        'that final period, it is a nil return and we file it for $300.00 plus '
        'applicable sales tax. Every earlier year has to be filed too: a '
        'dissolution does not clear the years behind it.'],
  extra=[('Unfiled Years Block the Clearance Certificate',
          ['A clearance certificate is what confirms the corporation&rsquo;s '
           'tax accounts are settled before its assets are distributed. It '
           'cannot be issued while a year is outstanding, so one unfiled nil '
           'year is enough to hold a dissolution open indefinitely.',
           QUAL]),
         ('Dissolving a Quebec Corporation Means Clearing Two Tax Authorities',
          ['The federal T2 record and the ' + PROV_RETURN + ' record are '
           'settled separately. Filing the final federal T2 settles the '
           'federal side; the provincial side is assessed by Revenu Quebec on '
           'its own record and is not covered by the $300.00 fee.',
           'We file the final federal T2 and any earlier federal years still '
           'outstanding, and we tell you how many we found, so the remaining '
           'provincial work is a known quantity rather than a surprise.'])],
  excerpt='The final T2 for a Quebec corporation being wound up, due within '
          'six months of dissolution. ' + FEE + '.'),

 dict(
  slug='t2-short-filing-quebec',
  service='t2-short-filing',
  title='T2 Short Filing in Quebec',
  keyword='t2 short filing quebec',
  national=('/t2-short-filing/', 'T2 Short filing'),
  lead_h2='When a Quebec Corporation Can Use the T2 Short',
  lead=['The T2 Short is a two-page version of the federal T2 that a '
        'corporation may use where it meets every one of the conditions the '
        'Canada Revenue Agency sets for it. Where a Quebec corporation '
        'qualifies, we file the T2 Short; where it does not, we file the full '
        'T2. The fee is the same either way, $300.00 plus applicable sales '
        'tax per tax year, because which form fits is our judgement to make '
        'and not something to charge for.'],
  extra=[('Choosing the Form Is Not the Client&rsquo;s Job',
          ['A corporation that files the T2 Short without meeting the '
           'conditions has filed on the wrong form, and a corporation that '
           'files the full T2 when the Short would have done has lost nothing '
           'but time. We check the conditions against the year being filed '
           'before the return is prepared, which is why the fee does not '
           'depend on the answer.',
           'You can work through the conditions yourself first with the '
           + a(SITE + '/tools/t2-short-eligibility-checker/',
               'T2 Short eligibility checker') + '.']),
         ('The T2 Short Is a Federal Form Only',
          ['The T2 Short is a form of the federal T2 and has nothing to do '
           'with the provincial return. Whichever federal form the corporation '
           'uses, the ' + PROV_RETURN + ' is filed with Revenu Quebec '
           'separately and is not covered by the $300.00 fee.'])],
  excerpt='The T2 Short for a qualifying Quebec corporation, at the same fee '
          'as the full return. ' + FEE + '.'),
 dict(
  slug='nil-t2-filing-cost-in-quebec',
  reviewed=LATER, reviewed_iso=LATER_ISO,
  service='nil-t2-filing-cost',
  title='Nil T2 Filing Cost in Quebec',
  keyword='nil t2 filing cost quebec',
  national=('/pricing/nil-t2-filing-cost/', 'nil T2 filing cost'),
  cost_h2='What Changes the Price, and What Does Not',
  lead_h2='What a Nil T2 Costs a Quebec Corporation',
  lead=['One nil T2 for one Quebec corporation for one tax year is $300.00 '
        'plus applicable sales tax. The figure does not move with the size of '
        'the corporation, the number of schedules the return needs, or how '
        'late the year is. Six unfiled years is six returns at the same price '
        'each, and you see the total before you pay rather than after.'],
  extra=[('The Price Does Not Depend on the Year Being Difficult',
          ['A nil year that needs GIFI schedules costs the same as one that '
           'does not, and a year filed nine years late costs the same as the '
           'current one. Working out which schedules a year needs is our job, '
           'and charging for the answer would make the quote depend on '
           'something you cannot check in advance.',
           'There is no hourly billing, no file-opening fee and no charge for '
           'telling you that a year is not nil.']),
         ('Sales Tax, and the One Thing Quebec Adds',
          ['Quebec charges GST and QST, so the tax added at checkout is the '
           'tax that applies where your corporation is resident. The price '
           'itself is the same in every province and territory.',
           'What the fee does not reach is the ' + PROV_RETURN + '. Quebec '
           'runs its own corporate income tax, so that return is filed with '
           'Revenu Quebec separately and is not covered here. The full '
           + a(SITE + '/pricing/what-is-not-included/',
               'list of what the fee does not cover')
           + ' sets out the rest.'])],
  excerpt='What one nil T2 costs a Quebec corporation, and what moves the '
          'price. ' + FEE + '.'),

 dict(
  slug='unfiled-corporate-tax-returns-quebec',
  reviewed=LATER, reviewed_iso=LATER_ISO,
  service='unfiled-corporate-tax-returns',
  title='Unfiled Corporate Tax Returns in Quebec',
  keyword='unfiled corporate tax returns quebec',
  national=('/catch-up-nil-t2-filing/', 'catch-up nil T2 filing'),
  lead_h2='What an Unfiled Year Does While It Sits There',
  lead=['An unfiled T2 does not expire. The year stays open on the Canada '
        'Revenue Agency&rsquo;s record indefinitely, and a Quebec corporation '
        'carrying several of them is usually carrying the same years on the '
        'Revenu Quebec record as well. Nothing about the passage of time '
        'closes either one. We file the federal years, oldest first, at '
        '$300.00 plus applicable sales tax each.'],
  extra=[('Demand to File, and What Follows It',
          ['The Canada Revenue Agency can issue a demand to file for an '
           'outstanding year. If that is not answered it can assess the '
           'corporation arbitrarily, on figures of its own choosing, and the '
           'corporation then has to displace that assessment rather than '
           'simply file.',
           'An arbitrary assessment on a corporation that genuinely had no '
           'activity is a worse starting point than a nil return filed late, '
           'because the figures in it are not yours.']),
         ('What Being Behind Actually Costs',
          [QUAL]),
         ('Finding Out Which Years Are Open',
          ['You do not need to know the list before you start. The '
           + a(SITE + '/tools/unfiled-years-checker/', 'unfiled years checker')
           + ' works through which years a corporation still owes, and we '
           'confirm what we find against the Canada Revenue Agency&rsquo;s '
           'record before anything is filed.'])],
  excerpt='Every year a Quebec corporation has not filed, brought up to date '
          'oldest year first. ' + FEE + '.'),

 dict(
  slug='no-activity-corporation-tax-return-quebec',
  reviewed=LATER, reviewed_iso=LATER_ISO,
  service='no-activity-corporation-tax-return',
  title='No Activity Corporation Tax Return in Quebec',
  keyword='no activity corporation tax return quebec',
  national=('/nil-t2-filing/', 'nil T2 filing'),
  lead_h2='What No Activity Means on a Return',
  lead=['No activity means the corporation had no income and no expenses in '
        'the tax year. Not low income, and not income that nets to nothing: '
        'none. A Quebec corporation in that position still files a T2 with '
        'the Canada Revenue Agency within six months of its fiscal year-end, '
        'and we file it for $300.00 plus applicable sales tax.'],
  extra=[('The Things People Think Are Nothing',
          ['Bank interest is income. Rent received is income. A dividend paid '
           'out or taken in is activity, and so is a sale of anything the '
           'corporation owned. A corporation that did one transaction in '
           'twelve months did not have a nil year.',
           'Paying an annual registry fee or a bank charge is not income, but '
           'it is an expense, and a year with expenses and no income is a loss '
           'year rather than a nil one. The '
           + a(SITE + '/tools/nil-t2-eligibility-checker/',
               'nil T2 eligibility checker')
           + ' walks through the distinction.']),
         ('Why It Matters Which One It Is',
          ['A loss year is worth filing properly, because the loss can be '
           'carried forward against income in a later year, and that is a '
           'different return from a nil one.',
           'If the year turns out not to be nil we tell you before you pay, '
           'and route you to our sister office rather than file the wrong '
           'return. The federal position is what we settle; the '
           + PROV_RETURN + ' is assessed separately by Revenu Quebec.'])],
  excerpt='The T2 a Quebec corporation files for a year in which it carried '
          'on no activity at all. ' + FEE + '.'),

 dict(
  slug='numbered-corporation-nil-filing-quebec',
  reviewed=LATER, reviewed_iso=LATER_ISO,
  service='numbered-corporation-nil-filing',
  title='Numbered Corporation Nil Filing in Quebec',
  keyword='numbered corporation nil filing quebec',
  national=('/nil-t2-filing/', 'nil T2 filing'),
  lead_h2='Filing for a Quebec Corporation With No Business Name',
  lead=['A numbered corporation files exactly the same T2 as a named one. '
        'Having no business name changes nothing about the return, the '
        'deadline or the fee, which is $300.00 plus applicable sales tax per '
        'tax year. What it changes is how easy the corporation is to find in '
        'your own paperwork, which is why numbered corporations are the ones '
        'most often left unfiled.'],
  extra=[('Numbers a Quebec Corporation Carries',
          ['A corporation has more than one number and they are not '
           'interchangeable. The Business Number is the Canada Revenue '
           'Agency&rsquo;s, and it is the one a T2 is filed under. The '
           'corporation also carries its registration number from the '
           'provincial enterprise register, which identifies it provincially '
           'and not federally.',
           'You do not need to have either to hand. Type the corporation name '
           'and we fill in the Business Number and the incorporation date. '
           'The '
           + a(SITE + '/tools/business-number-versus-corporation-number-checker/',
               'Business Number versus corporation number checker')
           + ' sets out which is which.']),
         ('The Corporation Nobody Remembers',
          ['A numbered corporation set up for one purpose and never wound up '
           'is the usual shape of a long unfiled backlog. It has no trading '
           'name to prompt anyone, no bank activity, and often no mail that '
           'anyone opens. The obligation runs regardless, every year, until '
           'the corporation is formally dissolved.'])],
  excerpt='Nil T2 filing for a Quebec numbered corporation, filed under its '
          'Business Number. ' + FEE + '.'),

 dict(
  slug='inactive-holding-corporation-t2-filing-quebec',
  reviewed=LATER, reviewed_iso=LATER_ISO,
  service='inactive-holding-corporation-t2-filing',
  title='Inactive Holding Corporation T2 Filing in Quebec',
  keyword='inactive holding corporation t2 filing quebec',
  national=('/inactive-holding-corporation-t2-filing/',
            'inactive holding corporation T2 filing'),
  lead_h2='When a Quebec Holding Corporation Is, and Is Not, Nil',
  lead=['A holding corporation holds assets by definition, so the question is '
        'always whether those assets produced anything in the tax year. A '
        'holding corporation with investment income, rental income, or '
        'dividends paid or received is not nil, and this service is not for '
        'it. Where the year genuinely produced nothing, the return is nil and '
        'we file it for $300.00 plus applicable sales tax.',
        'We check that position before you pay. If the year turns out not to '
        'be nil we tell you first, and if it is found after you pay we refund '
        'you in full.'],
  extra=[('What Counts as Income to a Holding Corporation',
          ['Interest credited on a balance is investment income even if '
           'nobody withdrew it. A dividend received from a subsidiary is '
           'income even if it was never moved. Rent on a property the '
           'corporation holds is income even where the property runs at a '
           'loss. Any one of those makes the year not nil.',
           'A holding corporation that held shares which paid nothing, owned '
           'property that earned nothing, and had no bank interest did have a '
           'nil year, and that is the case this page is for.']),
         ('Holding Structures and the Second Return',
          ['A Quebec holding corporation sits under two tax authorities like '
           'any other. Where the federal year is nil, the '
           + PROV_RETURN + ' position is assessed separately by Revenu Quebec '
           'on its own record and is not covered by the $300.00 fee.',
           'The '
           + a(SITE + '/guides/inactive-holding-company-filing/',
               'guide to inactive holding company filing')
           + ' works through the schedules a holding corporation still files '
           'even in a nil year.'])],
  excerpt='A Quebec holding corporation with no investment income and no '
          'dividends in the year files a nil T2. ' + FEE + '.'),

 dict(
  slug='nil-t2-filing-deadline-quebec',
  reviewed=LATER, reviewed_iso=LATER_ISO,
  service='nil-t2-filing-deadline',
  title='Nil T2 Filing Deadline in Quebec',
  keyword='nil t2 filing deadline quebec',
  national=('/deadlines/', 'T2 deadlines'),
  lead_h2='When a Quebec Corporation&rsquo;s Nil T2 Is Due',
  lead=['The T2 is due within six months of the end of the corporation&rsquo;s '
        'fiscal year. That rule comes from the Income Tax Act and is the same '
        'in every province, so a Quebec corporation has no different federal '
        'deadline from an Ontario one. A December 31 year-end is due June 30. '
        'A March 31 year-end is due September 30.'],
  extra=[('The Deadline Runs From Your Year-End, Not From December',
          ['A corporation picks its own fiscal year-end when it first files, '
           'and it does not have to be December 31. The six months run from '
           'whatever date the corporation chose, which is why two '
           'corporations in the same city can owe returns in different months.',
           'If you are not sure what year-end the Canada Revenue Agency has '
           'on record, that is one of the things we fill in from the '
           'corporation name. The '
           + a(SITE + '/tools/nil-t2-deadline-calculator/',
               'nil T2 deadline calculator')
           + ' works the date out from a year-end you already know.']),
         ('Missing It Does Not Change What Is Owed',
          ['A nil return filed after the deadline is still the same return. '
           'The year does not close itself and the obligation does not lapse.',
           QUAL]),
         ('The Quebec Deadline Is a Separate Question',
          ['The date above is the federal one. The ' + PROV_RETURN + ' has its '
           'own filing requirements with Revenu Quebec, assessed on its own '
           'record, and it is not covered by the $300.00 fee. We do not state '
           'its date here, because it is not ours to administer.'])],
  excerpt='When a Quebec corporation&rsquo;s nil T2 is due, with the '
          'six-month rule worked through. ' + FEE + '.'),

 dict(
  slug='nil-t2-filing-for-non-resident-owned-corporations-quebec',
  reviewed=LATER, reviewed_iso=LATER_ISO,
  service='nil-t2-filing-for-non-resident-owned-corporations',
  title='Nil T2 Filing for Non-Resident-Owned Corporations in Quebec',
  keyword='non resident owned corporation nil t2 quebec',
  national=('/nil-t2-filing/', 'nil T2 filing'),
  lead_h2='What Changes When the Shares Are Held Outside Canada',
  lead=['A Quebec corporation owned from outside Canada files the same nil T2 '
        'as any other, within six months of its fiscal year-end, for $300.00 '
        'plus applicable sales tax per tax year. One thing is materially '
        'different, and it is the reason this page exists: a late nil return '
        'carries a dollar penalty for a non-resident-owned corporation where '
        'it carries none for a resident-owned one.'],
  extra=[('The $25.00 a Day Penalty',
          ['A corporation that is not resident in Canada and files its return '
           'late is charged $25.00 for each day the return is late, up to '
           '$2,500.00 for that year. That charge does not depend on tax being '
           'owed, which is exactly why it reaches a nil year.',
           QUAL]),
         ('Filing From Another Country',
          ['Nothing in the process requires anyone to be in Canada. The '
           'corporation name is typed, the years are chosen, Form T183CORP is '
           'signed on a secure access-controlled screen, and the return is '
           'transmitted electronically. Your CRA confirmation is emailed '
           'within 3 business days.',
           'Your return is prepared and transmitted in Canada, by a CPA '
           'Ontario firm, and the ' + PROV_RETURN + ' remains a separate '
           'filing with Revenu Quebec.'])],
  excerpt='What changes for a Quebec corporation whose shares are held '
          'outside Canada. ' + FEE + '.'),

]


def build(s):
    url = SITE + '/' + s['slug'] + '/'
    b = ['<!-- wp:html -->', CSS + '<div class="cnf-hero"><div class="cnf-hero-in">'
         '<h1>' + s['title'] + '</h1><p class="cnf-hero-sub">' + FEE_TITLE +
         '</p><p class="cnf-hero-lede">We are a registered EFILE electronic '
         'filer. Your return is transmitted to the Canada Revenue Agency '
         'electronically.</p>'
         '<p><a class="cnf-hero-btn" href="' + FORM + '">Start Nil T2 Filing NOW</a>'
         '</p></div></div>']
    b.append('<div class="cnf-w">')
    b.append('<nav class="cnf-crumb" aria-label="Breadcrumb">'
             + a(SITE + '/', 'Nil T2 filing in Canada') + ' &rsaquo; '
             + a(HUB, 'Nil T2 filing in ' + PLACE) + ' &rsaquo; '
             '<span aria-current="page">' + s['title'] + '</span></nav>')
    b.append('<p class="cnf-by">Written and reviewed by '
             + a(SITE + '/sharad-gondaliya-cpa/', 'Sharad Gondaliya, CPA (Ontario)')
             + ', CPA Ontario Membership 61040184.</p>')
    b.append('<p class="cnf-rev">Last reviewed: ' + s.get('reviewed', TODAY) + '</p>')

    b.append('<h2>' + s['lead_h2'] + '</h2>')
    for p in s['lead']:
        b.append('<p>' + p + '</p>')

    # Plan line 1212: the place data row and the 120-word place paragraph.
    b.append('<h2>' + PLACE + ' Data</h2>')
    b.append('<table class="cnf-tbl"><thead><tr><th scope="col">Item</th>'
             '<th scope="col">' + PLACE + '</th><th scope="col">Source</th></tr>'
             '</thead><tbody>')
    for item, val, src in JD.place_rows(PLACE_SLUG, PLACE):
        b.append('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (item, val, src))
    b.append('</tbody></table>')
    b.append('<p>' + PLACE_PARA + '</p>')
    b.append('<p class="cnf-cap">The T2 due date comes from the Income Tax Act '
             'and does not vary by province. Corporation counts are the Canada '
             'Revenue Agency&rsquo;s own, rounded to the nearest ten, taken '
             'from the jurisdiction code on the T2 return, and they include '
             'tax-exempt and inactive corporations. They are refreshed when '
             'the Canada Revenue Agency reissues the table.</p>')

    for h2, paras in s['extra']:
        b.append('<h2>' + h2 + '</h2>')
        for p in paras:
            b.append('<p>' + p + '</p>')

    b.append('<h2>Who This Is For</h2>')
    b.append('<p>' + NOT_NIL_1 + '</p>')
    b.append('<p>' + NOT_NIL_2_QC + '</p>')

    b.append('<h2>How ' + s['title'] + ' Works</h2>')
    b.append('<ol><li>Type your corporation name. We fill the Business Number '
             'and incorporation date.</li><li>Pick the tax years to file and '
             'confirm the corporation had no activity in each of them.</li>'
             '<li>Complete the attestation and identity check, then pay '
             '$300.00 plus applicable sales tax per tax year.</li><li>Sign '
             'Form T183CORP. We transmit your return electronically.</li></ol>')
    b.append('<p>Your CRA confirmation is emailed within 3 business days. '
             'Business days are Monday to Friday and exclude ' + PLACE
             + ' statutory holidays.</p>')

    b.append('<h2>' + s.get('cost_h2', s['title'].replace(' in ' + PLACE, '')
                            + ' Cost in ' + PLACE) + '</h2>')
    b.append('<p>' + FEE + '. Each tax year is a separate return and carries '
             'the same fee. The sales tax that applies where your corporation '
             'is resident is added at checkout. See the full '
             + a(SITE + '/pricing/nil-t2-filing-cost/', 'nil T2 filing cost')
             + '.</p>')

    b.append('<h2>Filings This Does Not Cover</h2>')
    b.append('<div class="cnf-box"><ul>')
    # The CO-17 leads: on a Quebec page it is the single most likely thing a
    # reader assumes is included.
    b.append('<li>The ' + PROV_RETURN + ', the separate Quebec corporate '
             'income tax return filed with Revenu Quebec. It is not covered by '
             'the $300.00 fee.</li>')
    # Existence only. No due date, no fee, no statute, no filing route and no
    # dissolution threshold: see the docstring for why each is withheld.
    b.append('<li>Your Quebec annual filing with the provincial enterprise '
             'register. It is a registry filing rather than a tax return, it '
             'carries no tax, and it is not covered by the $300.00 fee.</li>')
    b.append('<li>A federal Corporations Canada annual return, at $12.00, if '
             'your corporation is federally incorporated.</li>')
    b.append('<li>A nil GST/HST return or a nil payroll return.</li>')
    b.append('<li>RC145 closure of a GST/HST or payroll account.</li></ul>')
    b.append('<p>We tell you which of these you still owe.</p></div>')

    nh, nl = s['national']
    b.append('<p>Read the national page on ' + a(SITE + nh, nl) + ', or see '
             'every ' + PLACE + ' page on the '
             + a(HUB, 'nil T2 filing in ' + PLACE + ' hub') + '.</p>')
    b.append('<p><a class="cnf-btn" href="' + FORM + '">Start Nil T2 Filing NOW</a></p>')
    b.append('<p class="cnf-foot">Your return is prepared and transmitted in '
             'Canada. Our credentials are never shared and no part of your '
             'file is sent offshore. ' + a(SITE + '/', 'Nil T2 filing in Canada')
             + '</p>')
    b.append('</div>')

    schema = {"@context": "https://schema.org", "@graph": [
      {"@type": "Service", "@id": url + "#service", "name": s['title'],
       "serviceType": "Nil T2 corporate income tax return filing", "url": url,
       "description": NOT_NIL_1,
       "areaServed": {"@type": "State", "name": PLACE},
       "provider": {"@id": SITE + "/#accountingservice"},
       "offers": {"@type": "Offer", "name": s['title'], "price": "300.00",
                  "priceCurrency": "CAD",
                  "description": FEE, "url": FORM,
                  "areaServed": {"@type": "State", "name": PLACE}}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Nil T2 filing in Canada",
         "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Nil T2 filing in " + PLACE,
         "item": HUB},
        {"@type": "ListItem", "position": 3, "name": s['title'], "item": url}]}]}
    b.append('<script type="application/ld+json">' + json.dumps(schema) + '</script>')
    b.append('<!-- /wp:html -->')
    return '\n'.join(b)


def meta(s):
    return {
     'site-sidebar-layout': 'no-sidebar', 'site-content-layout': 'page-builder',
     'ast-site-content-layout': 'full-width-container',
     'site-post-title': 'disabled', 'ast-breadcrumbs-content': 'disabled',
     'ast-featured-img': 'disabled',
     'cnf_service_slug': s['service'], 'cnf_place_slug': PLACE_SLUG,
     'cnf_place_name': PLACE, 'cnf_place_type': J['ptype'],
     'cnf_jurisdiction_return': 'T2',
     'cnf_provincial_return_name':
        PROV_RETURN + '. Quebec administers its own corporate income tax, so '
        'the CO-17 is a separate provincial return filed with Revenu Quebec '
        'and is not covered by the fee.',
     # Quebec charges GST plus QST, so an HST-inclusive figure would name the
     # wrong tax. Left empty rather than filled with a figure that is wrong.
     'cnf_price_incl_hst': '', 'cnf_overflow_price_incl_hst': '',
     'cnf_price': FEE, 'cnf_overflow_price': OVERFLOW,
     'cnf_deadline_rule':
        "The T2 is due within six months of the corporation's fiscal year-end, "
        "every year until the corporation is formally dissolved.",
     'cnf_unique_data_block_json': json.dumps(
        JD.unique_block(PLACE_SLUG, PLACE, J['ptype'])),
     'cnf_last_verified_et': s.get('reviewed_iso', ISO),
     'cnf_primary_keyword': s['keyword'],
    }


if __name__ == '__main__':
    N = 12
    assert len(SERVICES) == N, 'Quebec is now the full twelve-service set'
    assert len({s['slug'] for s in SERVICES}) == N
    assert len({s['service'] for s in SERVICES}) == N, 'one page per cnf_service'
    assert len({s['keyword'] for s in SERVICES}) == N, 'line 1717: distinct keywords'
    assert len({s['title'] for s in SERVICES}) == N, 'line 1717: distinct H1s'
    firsts = {s['lead'][0][:120] for s in SERVICES}
    assert len(firsts) == N, 'line 1717: the first 120 words must differ'
    # Every service slug must be one of the twelve line 304 fixes.
    assert {s['service'] for s in SERVICES} == set(SERVICE_SLUGS), (
        'service slugs do not match line 304: %s'
        % sorted({s['service'] for s in SERVICES} ^ set(SERVICE_SLUGS)))
    for s in SERVICES:
        c = build(s)
        assert PROV_RETURN in c, '%s: hard rule 8 needs the CO-17 named' % s['slug']
        assert 'T183' not in c or 'T183CORP' in c, '%s: bare T183' % s['slug']
        # Quebec charges no HST. "GST/HST" is the name of the CRA account and
        # is not a price claim, so it is removed before the test.
        assert 'HST' not in c.replace('GST/HST', ''), '%s: names HST' % s['slug']
        io.open(os.path.join(HERE, s['slug'] + '.html'), 'w',
                encoding='utf-8').write(c)
        print('%-44s %6d bytes   excerpt %d' % (s['slug'], len(c.encode()),
                                                len(s['excerpt'])))
