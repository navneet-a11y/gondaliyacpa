#!/usr/bin/env python3
"""Builds wealthscale-widgets.js (data + code) from the research registers. Run after any figure changes."""
import json, os, re

R = '/home/claude/ws100/research'
S = '/home/claude/ws100/site-wide'
B = '/home/claude/ws100/briefs'
tax = json.load(open(f'{R}/tax-tables-2026.json'))
acc = {x['key']: x for x in json.load(open(f'{R}/facts-accounts.json'))}
ben = {x['key']: x for x in json.load(open(f'{R}/facts-tax-benefits.json'))}
bank_scores = json.load(open(f'{B}/scores_banking.json'))
prov_path = f'{S}/src/providers-widget-data.json'
providers = json.load(open(prov_path)) if os.path.exists(prov_path) else {}


def v(d, k, cast=float):
    x = d[k]
    assert x['status'] == 'verified', (k, x['status'])
    return cast(str(x['value']).replace(',', ''))


D = {'asOf': '2026-10-22', 'year': 2026}
names = [('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'),
         ('NS', 'Nova Scotia'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'),
         ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon')]
D['provinces'] = names
D['provName'] = dict(names)
D['age_of_majority'] = {p: (19 if p in ('BC', 'NB', 'NL', 'NT', 'NS', 'NU', 'YT') else 18) for p, _ in names}

# ---- tax ----
T = {'federal': {k: tax['federal'][k] for k in ('brackets', 'bpa', 'bpa_min', 'bpa_phase')}, 'provinces': {}, 'qc_abatement': tax['federal']['quebec_abatement']}
for p, pv in tax['provinces'].items():
    q = {'brackets': pv['brackets'], 'bpa': pv['bpa']}
    if 'surtax' in pv: q['surtax'] = pv['surtax']
    if p == 'MB' and 'bpa_phase' in pv: q['bpa_phase'] = [pv['bpa_phase'][0], pv['bpa_phase'][1], 0]
    if p == 'YT': q['bpa_phase'] = [pv['bpa_phase'][0], pv['bpa_phase'][1], pv['bpa_min']]
    if p == 'ON':
        # convert [upper, base, rate, cap] bands to [from, to, base, rate, cap]
        bands, lo = [], 0
        for up, base, rate, cap in pv['health_premium_bands']:
            if rate > 0: bands.append([lo, up, base, rate, cap])
            lo = up
        q['health_premium'] = bands
    T['provinces'][p] = q
dv = tax['dividends']
T['dividends'] = {k: dv[k] for k in ('eligible_grossup', 'noneligible_grossup', 'federal_dtc_eligible', 'federal_dtc_noneligible')}
T['dividends']['provincial_dtc'] = {p: r for p, r in dv['provincial_dtc'].items() if r}
T['capital_gains_inclusion'] = tax['capital_gains_inclusion']
D['tax'] = T

# ---- TFSA, RRSP, FHSA, RESP, RRIF, HBP ----
D['tfsa'] = {'limits': {y: v(acc, f'tfsa.limit.{y}', int) for y in range(2009, 2027)}, 'over_tax_month': v(acc, 'tfsa.overcontribution.tax') / 100}
D['rrsp'] = {'limits': {y: v(acc, f'rrsp.limit.{y}', int) for y in range(2020, 2028)}, 'pct': 0.18, 'cushion': 2000,
             'deadline': {2025: '2026-03-02', 2026: '2027-03-01'},
             'withholding': {'other': tax['withholding']['lump_sum_outside_qc'], 'QC': tax['withholding']['lump_sum_qc_federal']},
             'withholding_text': '10% up to $5,000, 20% over $5,000 to $15,000 and 30% over $15,000 (outside Quebec)'}
D['fhsa'] = {'annual': v(acc, 'fhsa.limit.annual', int), 'lifetime': v(acc, 'fhsa.limit.lifetime', int), 'carry': v(acc, 'fhsa.carryforward.max', int),
             'max_years': 15, 'max_age': 71, 'first_year': 2023}
D['resp'] = {'lifetime': v(acc, 'resp.limit.lifetime', int), 'cesg_rate': v(acc, 'cesg.basic.rate') / 100, 'cesg_on': 2500, 'cesg_annual': v(acc, 'cesg.annual.max', int),
             'cesg_max_year': v(acc, 'cesg.annual.max_with_carryforward', int), 'cesg_lifetime': v(acc, 'cesg.lifetime.max', int),
             'cesg_age16_total': 2000, 'cesg_age16_years': 4,
             'acesg_rates': [v(acc, 'acesg.rate.lower') / 100, v(acc, 'acesg.rate.middle') / 100], 'acesg_on_first': 500,
             'acesg_income': [v(acc, 'acesg.threshold.2026.lower', int), v(acc, 'acesg.threshold.2026.upper', int)],
             'clb_first': v(acc, 'clb.initial', int), 'clb_yearly': v(acc, 'clb.annual', int), 'clb_max': v(acc, 'clb.lifetime', int),
             'clb_thresholds': [None, v(acc, 'clb.threshold.1_to_3_children', int), v(acc, 'clb.threshold.1_to_3_children', int), v(acc, 'clb.threshold.1_to_3_children', int),
                                v(acc, 'clb.threshold.4_children', int), v(acc, 'clb.threshold.5_children', int)],
             'bctesg': v(acc, 'bctesg.amount', int), 'qesi_rate': 0.10, 'qesi_annual': 250, 'qesi_lifetime': v(acc, 'qesi.lifetime', int)}
D['rrif'] = {'factors': {a: v(acc, f'rrif.factor.age.{a}') for a in range(71, 95)}}
D['rrif']['factors'][95] = v(acc, 'rrif.factor.age.95_plus')
D['hbp'] = {'max': v(acc, 'hbp.limit', int), 'repay_years': 15, 'deferral': [2022, 2028], 'deferral_start': 5}
D['us_withholding'] = {'treaty': 0.15, 'no_w8': 0.30, 'accounts': [
    ['rrsp', 'RRSP', True, 'Not needed', 'RRSPs are exempt from US withholding on dividends from US-listed securities held directly, under Article XXI of the Canada-US tax treaty.'],
    ['rrif', 'RRIF', True, 'Not needed', 'RRIFs are treated like RRSPs: no US withholding on dividends from US-listed securities held directly.'],
    ['lira', 'LIRA or LIF', True, 'Not needed', 'Locked-in retirement accounts are retirement arrangements, so the treaty exemption applies.'],
    ['tfsa', 'TFSA', False, 'No', 'The tax withheld in a TFSA is a permanent cost: there is no Canadian tax to credit it against.'],
    ['fhsa', 'FHSA', False, 'No', 'FHSAs are not retirement accounts, so withholding applies and cannot be recovered.'],
    ['resp', 'RESP', False, 'No', 'RESPs are not retirement accounts, so withholding applies and cannot be recovered.'],
    ['nonreg', 'Non-registered (cash or margin)', False, 'Yes, as a foreign tax credit', 'You report the gross dividend and claim a foreign tax credit for the US tax on your Canadian return.']]}
D['deposit_insurance'] = {'limit': v(acc, 'cdic.limit', int),
                          'categories': ['Deposits in your name', 'Joint deposits', 'Deposits in trust', 'RRSP deposits', 'RRIF deposits', 'TFSA deposits', 'FHSA deposits', 'RESP deposits', 'RDSP deposits'],
                          'note': 'Credit unions are covered by provincial deposit insurance instead.'}

# ---- benefits ----
def dates(prefix):
    out = sorted(x['value'] for k, x in ben.items() if k.startswith(prefix) and x['status'] == 'verified' and re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(x['value'])))
    return out
cpp_dates = dates('benefit.cpp_oas.paydate.')
D['benefits'] = {
    'cpp_oas': {'name': 'CPP and OAS', 'dates': cpp_dates, 'note': 'Old Age Security and the Guaranteed Income Supplement are paid on the same day as the Canada Pension Plan. 2027 dates have not been published yet.'},
    'gst': {'name': 'Canada Groceries and Essentials Benefit (formerly the GST/HST credit)', 'dates': dates('benefit.cgeb.paydate.'), 'note': 'The Canada Groceries and Essentials Benefit replaced the GST/HST credit in July 2026.'},
    'ccb': {'name': 'Canada Child Benefit', 'dates': dates('benefit.ccb.paydate.'), 'note': '2027 dates have not been published yet.'},
    'otb': {'name': 'Ontario Trillium Benefit', 'dates': dates('benefit.otb.paydate.'), 'note': '2027 dates have not been published yet.'},
    'cdb': {'name': 'Canada Disability Benefit', 'dates': dates('benefit.cdb.paydate.'), 'note': '2027 dates have not been published yet.'},
    'acwb': {'name': 'Canada Workers Benefit advance payments', 'dates': dates('benefit.acwb.paydate.'), 'note': '2027 dates have not been published yet.'}}
O = tax['oas']
D['oas'] = {'threshold': O['clawback_threshold_2026_income'], 'rate': O['clawback_rate'], 'income_year': 2026, 'max65': O['max_monthly_2026q4']['65_74'],
            'max75': O['max_monthly_2026q4']['75_plus'], 'defer': O['deferral_per_month']}
Cp = tax['cpp']
D['cpp'] = {'max65': Cp['max_monthly_65_2026'], 'avg65': Cp['avg_monthly_65_jul2026'], 'early': Cp['early_per_month'], 'late': Cp['late_per_month']}
D['gst_credit'] = {'period': 'July 2026 to June 2027', 'income_year': 2025, 'adult': v(ben, 'benefit.cgeb.2026_27.adult_max', int), 'child': v(ben, 'benefit.cgeb.2026_27.max_per_child', int),
                   'single_supp': v(ben, 'benefit.cgeb.2026_27.single_supplement', int), 'supp_base': v(ben, 'benefit.cgeb.2026_27.single_supplement_phasein', int),
                   'supp_rate': 0.02, 'threshold': v(ben, 'benefit.cgeb.2026_27.phaseout_start', int), 'reduce': 0.05,
                   'note': 'From July 2026 this payment is the Canada Groceries and Essentials Benefit, which replaced the GST/HST credit with amounts 25% higher. The phase-in and reduction rates used here are the ones set for the GST/HST credit; CRA calculates your exact amount from your return.'}

# ---- banking ----
D['chequing'] = [{'name': c['name'], 'link': c['review'], 'fee': c['monthly_fee'], 'fee_text': c['fee_text'], 'waive_bal': c['waive_balance'], 'rate': c['base_rate']} for c in bank_scores['chequing']]
D['hisa'] = [
    {'name': 'Saven High Interest Savings', 'rate': 0.0285, 'ins': 'DICO, up to $250,000'},
    {'name': 'Oaken Savings Account', 'rate': 0.0280, 'ins': 'CDIC'},
    {'name': 'EQ Bank 30 Day Notice Savings', 'link': '/reviews/eq-bank/', 'rate': 0.0275, 'rate_note': '30 days\' notice to withdraw', 'ins': 'CDIC'},
    {'name': 'Hubert High Interest Savings', 'rate': 0.0250, 'ins': 'Deposit Guarantee Corporation of Manitoba'},
    {'name': 'Wealthsimple Savings', 'link': '/reviews/wealthsimple/', 'rate': 0.0250, 'ins': 'CIPF, not CDIC'},
    {'name': 'KOHO Essential', 'rate': 0.0200, 'rate_note': '$7 a month plan, $0 with direct deposit', 'ins': 'CDIC through partner institutions (opt-in)'},
    {'name': 'Neo Savings (Essentials)', 'rate': 0.0200, 'ins': 'Not stated'},
    {'name': 'Outlook High Interest Savings', 'rate': 0.0195, 'ins': 'Deposit Guarantee Corporation of Manitoba'},
    {'name': 'Manulife Bank Advantage Account', 'rate': 0.0150, 'rate_note': '3.00% promo on new accounts opened by Oct 30, 2026', 'ins': 'CDIC'},
    {'name': 'Peoples Trust e-Savings', 'rate': 0.0120, 'ins': 'CDIC'},
    {'name': 'Alterna High Interest eSavings', 'rate': 0.0105, 'ins': 'CDIC'},
    {'name': 'EQ Bank Personal Account', 'link': '/reviews/eq-bank/', 'rate': 0.0100, 'rate_note': '2.75% with pay direct deposit', 'ins': 'CDIC'},
    {'name': 'RBC High Interest eSavings', 'rate': 0.0055, 'ins': 'CDIC'},
    {'name': 'National Bank High Interest Savings', 'rate': 0.0055, 'ins': 'CDIC'},
    {'name': 'Scotia MomentumPLUS Savings', 'rate': 0.0040, 'rate_note': 'base rate', 'ins': 'CDIC'},
    {'name': 'Simplii High Interest Savings', 'rate': 0.0030, 'rate_note': 'up to $50,000', 'ins': 'CDIC'}]
D['usd_savings'] = [
    {'name': 'EQ Bank US Dollar Account', 'link': '/reviews/eq-bank/', 'rate': 0.0250, 'ins': 'Not stated for USD on the product page'},
    {'name': 'Manulife US Dollar Advantage Account', 'rate': 0.0020, 'ins': 'Not stated for USD on the product page'},
    {'name': 'National Bank USD Progress Account', 'rate': 0.0010, 'rate_note': 'from $10,000', 'ins': 'Not stated for USD on the product page'},
    {'name': 'Scotia U.S. Dollar Daily Interest', 'rate': 0.0005, 'rate_note': 'top tier', 'ins': 'Not stated for USD on the product page'},
    {'name': 'TD U.S. Daily Interest Chequing', 'rate': 0.0001, 'ins': 'Not stated for USD on the product page'}]
D['gic_best'] = {1: 3.85, 2: 4.25, 3: 4.30, 4: 4.35, 5: 4.50}
D['gic_default_rate'] = 3.85
D['median_fx'] = 0.015
D['usdcad_example'] = 1.38  # editable example assumption in the FX widgets, used only for tiers set in US dollars

# ---- providers (brokers, robos, crypto, tax software, Wealthsimple tiers, cards) ----
for k in ('brokers', 'robos', 'crypto', 'tax_software', 'tax_software_year', 'broker_features', 'ws_tiers', 'cards'):
    if k in providers: D[k] = providers[k]
D.setdefault('brokers', []); D.setdefault('robos', []); D.setdefault('crypto', []); D.setdefault('tax_software', []); D.setdefault('broker_features', [])

src = open(f'{S}/src/ws-widgets.src.js').read()
data = json.dumps(D, separators=(',', ':'), ensure_ascii=False)
out = src.replace('/*@@DATA@@*/{}', data)
assert out != src
open(f'{S}/wealthscale-widgets.js', 'w').write(out)
json.dump(D, open(f'{S}/src/ws-data.json', 'w'), indent=1, ensure_ascii=False)
print('built', len(out), 'bytes; cpp dates', len(cpp_dates), '; gst dates', D['benefits']['gst']['dates'])
