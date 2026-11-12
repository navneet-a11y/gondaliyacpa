# -*- coding: utf-8 -*-
"""Per-jurisdiction data for the Family 4 jurisdiction half.

THE DATA ROW PROBLEM, AND HOW IT WAS SOLVED ON 2026-11-12.

Plan line 1212: "No service and place page publishes without its own place data
row and its own 120-word place paragraph." decisions.md 2026-10-21 recorded that
the per-jurisdiction figure could not be found -- "the CRA T2 statistics tables
report dollar amounts by jurisdiction, not counts of returns" -- and that is why
British Columbia's data row has no count in it and why the jurisdiction half
stalled.

That finding was wrong, and it is corrected here. The CRA publishes
"T2 Corporate Statistical Tables, Table 1, Number of Corporations by
Jurisdiction, 2018 to 2023", which is a COUNT table covering all thirteen
jurisdictions for six tax years. Fetched 2026-11-12 from www.canada.ca, which
the environment's network policy allows, and extracted with pdftotext.

It reconciles exactly with the three figures the plan states for itself at line
1743 -- Ontario 1,108,730, Alberta 365,890, British Columbia 413,630 -- which
are the 2023 column of this table. So the plan's own numbers and these came
from the same source, and the ten remaining jurisdictions can be stated on the
same footing as the three already live.

The six-year series is what makes these pages differ from one another under
6(k). Each jurisdiction has its own trajectory: Newfoundland and Labrador and
the Northwest Territories have fewer corporations than in 2018, Nunavut has the
same 630 it started with, and Quebec and Manitoba are the only two still at
their 2023 peak. That is a sourced, per-place fact pattern rather than a
placename swap.

CRA Table 1 notes that are carried onto the pages: counts are rounded to the
nearest ten, jurisdiction comes from the line 750 jurisdiction code, the data
are as of June 30, 2025, and -- the note that matters most for a nil-filing
site -- the counts INCLUDE tax-exempt and inactive corporations.

PRICE STRING. Navneet, 2026-11-12: "Plus hst where application dont write hst
where its not", and on the live pages "if hst work in these provinces then let
it be as it is. if not then chaneg". So HST is named only in the five HST
jurisdictions. No tax RATE and no tax-inclusive total appears on any page, in
either group, following the 2026-10-21 ruling that dropped the computation.

WHAT IS WITHHELD. Provincial registry facts -- the annual return's due date,
fee, statutory authority, filing route, and how long non-filing runs before the
registrar may dissolve -- are not sourced for these ten jurisdictions and are
recorded as None rather than estimated, exactly as build_f4_ab does for Alberta.
Revenu Quebec returns 403 to automated clients, so no CO-17 deadline, no nil
exemption and no CO-17 penalty is stated; the one CO-17 claim made is the one
the signed-off plan makes itself at line 1212 and in hard rule 8.
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
_CRA = json.load(io.open(os.path.join(HERE, '..', '..', 'docs', 'seo',
                                      'cra-t2-jurisdiction-counts.json'),
                         encoding='utf-8'))

CRA_SOURCE = 'Canada Revenue Agency T2 Corporate Statistical Tables, Table 1'

# The five HST jurisdictions. Everywhere else, HST is never named.
HST = {'ontario', 'nova-scotia', 'new-brunswick',
       'newfoundland-and-labrador', 'prince-edward-island'}

# The two provinces that administer their own corporate income tax.
OWN_CORPORATE_TAX = {'quebec': 'Quebec CO-17', 'alberta': 'Alberta AT1'}


def fee(slug):
    """The per-tax-year fee string for a jurisdiction. Rule: name HST only
    where HST is charged."""
    return ('$300.00 plus HST per tax year' if slug in HST
            else '$300.00 plus applicable sales tax per tax year')


def fee_title(slug):
    return ('$300.00 Plus HST Per Tax Year' if slug in HST
            else '$300.00 Plus Applicable Sales Tax Per Tax Year')


def overflow(slug):
    return ('$350.00 plus HST per year' if slug in HST
            else '$350.00 plus applicable sales tax per year')


def tax_phrase(slug):
    """How the page refers to the tax added at checkout."""
    return ('HST' if slug in HST else 'the sales tax that applies in your province')


def cra(slug):
    return _CRA['jurisdictions'][slug]


def count(slug):
    return '{:,}'.format(cra(slug)['count_2023'])


def count_2018(slug):
    return '{:,}'.format(cra(slug)['counts'][0])


# The per-place paragraph plan line 1212 requires, one per jurisdiction,
# written around what is actually different about that jurisdiction's own
# six-year series rather than derived from a trend category. An earlier pass
# generated these from the direction of travel and produced word-identical
# sentences for Quebec and Manitoba, and one shared sentence for five others,
# which is the template pattern 6(k) exists to catch.
PLACE_PARA = {

 'quebec':
   'The Canada Revenue Agency assessed returns from 553,570 Quebec '
   'corporations for the 2023 tax year, up from 488,750 in 2018. That is the '
   'second largest corporate population in the country and the only large one '
   'still at its six-year high, having risen in every year the table covers. '
   'Quebec corporations also carry something no other province except Alberta '
   'does: a second corporate income tax return, filed with a second tax '
   'authority, on its own record.',

 'manitoba':
   'The Canada Revenue Agency assessed returns from 69,180 Manitoba '
   'corporations for the 2023 tax year, up from 62,320 in 2018, and 2023 is '
   'the highest figure in the six years the table covers. Manitoba and Quebec '
   'are the only two jurisdictions that had not come off their peak by the end '
   'of the series. Manitoba corporate income tax is reported through the '
   'federal T2, so the return we file settles the provincial side as well as '
   'the federal one.',

 'saskatchewan':
   'The Canada Revenue Agency assessed returns from 73,110 Saskatchewan '
   'corporations for the 2023 tax year, up from 70,550 in 2018. That rise of '
   '2,560 is about one corporation for every twenty-eight that existed in '
   '2018, the slowest proportional growth of any province except Alberta, and '
   'the 2023 figure is 660 below the 73,770 Saskatchewan reached in 2022. A '
   'count that turns down is dissolutions completing, and a dissolution '
   'cannot complete while a tax year is still unfiled.',

 'nova-scotia':
   'The Canada Revenue Agency assessed returns from 47,490 Nova Scotia '
   'corporations for the 2023 tax year, up from 43,740 in 2018. That is the '
   'largest corporate population in Atlantic Canada, larger than Newfoundland '
   'and Labrador and Prince Edward Island combined. Nova Scotia rose in every '
   'year of the series until 2023, when the figure came in 190 below the '
   '47,680 recorded in 2022 &mdash; the first fall in six years.',

 'new-brunswick':
   'The Canada Revenue Agency assessed returns from 34,960 New Brunswick '
   'corporations for the 2023 tax year, up from 33,050 in 2018. The province '
   'added 1,910 corporations across the six years and then gave back 410 of '
   'them between 2022 and 2023, having peaked at 35,370. New Brunswick '
   'corporate income tax is reported through the federal T2, so one return '
   'settles both sides.',

 'newfoundland-and-labrador':
   'The Canada Revenue Agency assessed returns from 17,800 Newfoundland and '
   'Labrador corporations for the 2023 tax year, down from 19,560 in 2018. '
   'This is the only province in the country whose corporate population fell '
   'in every year of the series, and the only one whose high point is 2018 '
   'rather than 2022 or 2023. A corporation that stops trading without being '
   'dissolved does not leave those rolls, which means the fall is dissolutions '
   'rather than closures, and every one of them needed a final return first.',

 'prince-edward-island':
   'The Canada Revenue Agency assessed returns from 9,220 Prince Edward Island '
   'corporations for the 2023 tax year, up from 8,140 in 2018. It is the '
   'smallest corporate population of any province, but proportionally one of '
   'the fastest growing in the country over the six years, adding roughly one '
   'corporation for every eight that existed in 2018. On a base that small, '
   'the 20-corporation fall from the 2022 figure of 9,240 is a handful of '
   'dissolutions.',

 'yukon':
   'The Canada Revenue Agency assessed returns from 2,430 Yukon corporations '
   'for the 2023 tax year, up from 2,270 in 2018. Yukon has the largest '
   'corporate population of the three territories, more than the Northwest '
   'Territories and Nunavut combined, and it is the only one of the three that '
   'has more corporations than it had six years earlier. Territorial corporate '
   'income tax is reported through the federal T2, so there is no separate '
   'territorial corporate income tax return to file.',

 'northwest-territories':
   'The Canada Revenue Agency assessed returns from 1,590 Northwest '
   'Territories corporations for the 2023 tax year, down from 1,770 in 2018. '
   'That is the steepest proportional fall of any jurisdiction in the country '
   'over the six years, and the count fell in every year of it. The '
   'territory has a small enough corporate population that the Canada Revenue '
   'Agency rounds it to the nearest ten and the whole six-year decline is 180 '
   'corporations.',

 'nunavut':
   'The Canada Revenue Agency assessed returns from 630 Nunavut corporations '
   'for the 2023 tax year, the same figure the table shows for 2018. It is the '
   'smallest corporate population in Canada by a wide margin, smaller than the '
   'Northwest Territories and a quarter the size of Yukon, and it has moved by '
   'at most 30 corporations in either direction across the whole series. The '
   'Canada Revenue Agency rounds these counts to the nearest ten, so on a base '
   'of 630 a single dissolution is inside the rounding.',
}


def trajectory(slug, name):
    """The per-place paragraph. Hand-written per jurisdiction; see PLACE_PARA."""
    return PLACE_PARA[slug]


def prov_return(slug):
    """The separate provincial corporate income tax return, where there is one.
    Hard rule 8 and plan line 1212."""
    return OWN_CORPORATE_TAX.get(slug)


def place_rows(slug, name):
    """The place data row plan line 1212 makes mandatory. Sourced rows only."""
    pr = prov_return(slug)
    rows = [
      ('T2 filing deadline', 'Within six months of the fiscal year-end',
       'Income Tax Act'),
      ('Separate provincial corporate income tax return',
       ('Yes, the ' + pr) if pr else
       'No. Corporate income tax is reported through the federal T2',
       'Plan line 1212' if pr else CRA_SOURCE),
      ('Corporations on the T2 rolls, 2023 tax year', count(slug), CRA_SOURCE),
      ('Corporations on the T2 rolls, 2018 tax year', count_2018(slug),
       CRA_SOURCE),
      ('Filing route', 'T2 transmitted electronically to the Canada Revenue '
       'Agency by a registered EFILE electronic filer', 'Canada Revenue Agency'),
    ]
    return rows


def unique_block(slug, name, ptype):
    """cnf_unique_data_block_json. Unsourced fields are None, never estimated."""
    d = cra(slug)
    pr = prov_return(slug)
    return {
      'place': name,
      'place_type': ptype,
      'provincial_corporate_return': pr,
      'provincial_corporate_return_covered_by_fee': False if pr else None,
      'corporate_income_tax_through_federal_t2': pr is None,
      't2_rolls_2023': d['count_2023'],
      't2_rolls_2018': d['counts'][0],
      't2_rolls_series_2018_2023': d['counts'],
      't2_rolls_direction_2018_2023': d['direction'],
      't2_rolls_peak_year': d['peak_year'],
      't2_rolls_source': CRA_SOURCE,
      't2_rolls_source_notes': [
        'Counts are rounded to the nearest ten.',
        'Jurisdiction is determined using the jurisdiction code on the T2 '
        'return (line 750).',
        'Counts include tax-exempt and inactive corporations.',
        'Data are as of June 30, 2025 and are subject to change.'],
      'filing_route': 'T2 transmitted electronically to the Canada Revenue '
                      'Agency by a registered EFILE electronic filer',
      'hst_charged': slug in HST,
      'hst_rate': None,
      'registry_name': None,
      'annual_return_route': None,
      'annual_return_due': None,
      'annual_return_statute': None,
      'annual_return_fee': None,
      'dissolution_after': None,
      'unsourced_note':
        'Provincial registry facts were not sourceable when this page was '
        'built and are recorded as null rather than estimated. '
        + ('Revenu Quebec returns 403 to automated clients, so no CO-17 '
           'deadline, exemption or penalty is stated; the only CO-17 claim '
           'made is the one plan line 1212 and hard rule 8 make.'
           if slug == 'quebec' else ''),
    }


# The ten jurisdictions the F4 jurisdiction half still needs. Ontario, British
# Columbia and Alberta are already live with their own builders.
JURISDICTIONS = [
  dict(slug='quebec', name='Quebec', short='QC', ptype='province',
       article='', hub='/quebec/'),
  dict(slug='manitoba', name='Manitoba', short='MB', ptype='province',
       article='', hub='/manitoba/'),
  dict(slug='saskatchewan', name='Saskatchewan', short='SK', ptype='province',
       article='', hub='/saskatchewan/'),
  dict(slug='nova-scotia', name='Nova Scotia', short='NS', ptype='province',
       article='', hub='/nova-scotia/'),
  dict(slug='new-brunswick', name='New Brunswick', short='NB',
       ptype='province', article='', hub='/new-brunswick/'),
  dict(slug='newfoundland-and-labrador', name='Newfoundland and Labrador',
       short='NL', ptype='province', article='',
       hub='/newfoundland-and-labrador/'),
  dict(slug='prince-edward-island', name='Prince Edward Island', short='PE',
       ptype='province', article='', hub='/prince-edward-island/'),
  dict(slug='yukon', name='Yukon', short='YT', ptype='territory',
       article='', hub='/yukon/'),
  dict(slug='northwest-territories', name='Northwest Territories', short='NT',
       ptype='territory', article='the ', hub='/northwest-territories/'),
  dict(slug='nunavut', name='Nunavut', short='NU', ptype='territory',
       article='', hub='/nunavut/'),
]

BY_SLUG = {j['slug']: j for j in JURISDICTIONS}

if __name__ == '__main__':
    print('%-26s %10s %10s %-11s %s' % ('jurisdiction', '2023', '2018',
                                        'direction', 'fee'))
    for j in JURISDICTIONS:
        s = j['slug']
        print('%-26s %10s %10s %-11s %s' % (
            s, count(s), count_2018(s), cra(s)['direction'], fee(s)))
    print()
    for j in JURISDICTIONS:
        print('--- ' + j['name'] + ' ---')
        print(trajectory(j['slug'], j['name']))
        print()
