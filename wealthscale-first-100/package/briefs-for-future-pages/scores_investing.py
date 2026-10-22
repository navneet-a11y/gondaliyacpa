#!/usr/bin/env python3
"""WealthScale scores for brokers, robo-advisors, crypto platforms and tax software (published on /methodology/brokers/).
Inputs: providers-investing.json and facts-wealthsimple.json, October 22, 2026. Every input below is a published figure or a yes/no from those registers.
Writes briefs/scores.json (with banking) and site-wide/src/providers-widget-data.json."""
import json

PRIME = 0.0445
MEDIAN_FX = 0.015  # used only for scoring when a broker publishes no conversion rate or only an undisclosed spread

def clamp(x, a=0.0, b=5.0): return max(a, min(b, x))

# ------------------------------------------------------------------ brokers
# trade costs are for a $2,000 order of 40 shares; US-dollar fees are counted at par
BR = [
 dict(id='wealthsimple', nomin=1, name='Wealthsimple', review='/reviews/wealthsimple/trade/', cad=0, us=0, fx=0.015, fx_pub=True, fx_text='1.5% (all tiers; lower inside a USD account on large conversions)',
      usd_reg='paid', usd_reg_text='TFSA, FHSA, RRSP, spousal RRSP, LIRA and RESP: $10 a month on Core, included on Premium and Generation', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=1, fhsa=1, resp=1, rrif=1, lira=1, margin=1, joint=1, corporate=1),
      frac=1, drip=1, options=1, adv=0, mobile=1, cash=0, margin_cad=0.0495, margin_text='4.95% Core, 4.45% Premium, 3.95% Generation',
      opt_base=0, opt_contract=0, opt_min=0, opt_text='$0 per contract on US equity and ETF options',
      safety=4.0, bank=0, transfer_text='Reimburses the other institution\'s transfer-out fee, up to $150 per account, on transfers of $25,000 or more', transfer_min=25000, transfer_max=150, per_client=False,
      cad_text='$0', us_text='$0'),
 dict(id='questrade', nomin=0.5, name='Questrade', review='/reviews/questrade/', cad=0, us=0, fx=0.015, fx_pub=True, fx_text='1.5%',
      usd_reg='free', usd_reg_text='USD held in registered accounts at no extra cost', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=1, fhsa=1, resp=1, rrif=1, lira=1, margin=1, joint=1, corporate=1),
      frac=1, drip=1, options=1, adv=1, mobile=0.5, cash=0, margin_cad=PRIME + 0.0425, margin_text='Prime + 4.25% under $100,000 (8.70%)',
      opt_base=0, opt_contract=0, opt_min=0, opt_text='$0 on US equity options; Canadian options $0.99 per contract',
      safety=3.5, bank=0, transfer_text='Rebates the other institution\'s fee, up to $150 per account, on eligible transfers', transfer_min=None, transfer_max=150, per_client=False,
      cad_text='$0', us_text='$0'),
 dict(id='interactive-brokers', nomin=1, name='Interactive Brokers Canada', review='/reviews/interactive-brokers/', cad=1.00, us=1.00, fx=0.0, fx_fixed=2.0, fx_pub=True, fx_text='0.20 basis points, minimum US$2 per conversion',
      usd_reg='unknown', usd_reg_text='Not stated for registered accounts', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=1, fhsa=1, resp=0, rrif=1, lira=0, margin=1, joint=1, corporate=1),
      frac=1, drip=1, options=1, adv=1, mobile=1, cash=0.01675, margin_cad=0.03675, margin_text='3.675% up to CAD 130,000 (IBKR Pro)',
      opt_base=0, opt_contract=0.65, opt_min=1.00, opt_text='US$0.65 per contract, minimum US$1',
      safety=4.0, bank=0, transfer_text='', transfer_min=None, transfer_max=None, per_client=False,
      cad_text='CAD 0.01 a share, minimum CAD 1', us_text='USD 0.005 a share, minimum USD 1'),
 dict(id='moomoo', nomin=1, name='moomoo Canada', review='/reviews/moomoo/', cad=1.49, us=1.99, fx=None, fx_pub=False, fx_text='0% fee; spread of undisclosed size',
      usd_reg='free', usd_reg_text='TFSA and RRSP can hold CAD and USD; no fee stated', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=1, fhsa=0, resp=0, rrif=0, lira=0, margin=1, joint=0, corporate=0),
      frac=0, drip=0, options=1, adv=1, mobile=1, cash=0, margin_cad=0.0385, margin_text='From 3.85% (as of November 3, 2025)',
      opt_base=0, opt_contract=0.65, opt_min=1.00, opt_text='US$0.65 per contract, minimum US$1',
      safety=4.0, bank=0, transfer_text='Promotion: typically reimburses $100 on transfers of $10,000 or more', transfer_min=10000, transfer_max=100, per_client=True,
      cad_text='CA$0.0149 a share, minimum CA$1.49', us_text='US$0.0099 a share, minimum US$1.99'),
 dict(id='webull', nomin=1, name='Webull Canada', review='/reviews/webull/', cad=0, us=0, fx=0.015, fx_pub=True, fx_text='1.5%',
      usd_reg='unknown', usd_reg_text='Not stated', admin=8.40,
      accts=dict(tfsa=1, rrsp=1, spousal=0, fhsa=0, resp=0, rrif=0, lira=0, margin=1, joint=0, corporate=0),
      frac=0, drip=0, options=1, adv=1, mobile=1, cash=0, margin_cad=PRIME + 0.03, margin_text='Prime + 3% under $100,000 (7.45%)',
      opt_base=0, opt_contract=0.99, opt_min=0, opt_text='US$0.99 per contract',
      safety=4.0, bank=0, transfer_text='Transfer bonus of $150 (terms not published)', transfer_min=None, transfer_max=None, per_client=True,
      cad_text='$0', us_text='$0'),
 dict(id='qtrade', nomin=1, name='Qtrade Direct Investing', review='/reviews/qtrade/', cad=0, us=0, fx=None, fx_pub=False, fx_text='Not published',
      usd_reg='paid', usd_reg_text='RRSP, RRIF and TFSA: US$15 a quarter per account (free with Investor Plus)', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=1, fhsa=1, resp=1, rrif=1, lira=1, margin=1, joint=1, corporate=1),
      frac=0, drip=1, options=1, adv=0, mobile=1, cash=0, margin_cad=PRIME + 0.0155, margin_text='Prime + 1.55% under $100,000 (6.00%)',
      opt_base=0, opt_contract=0.75, opt_min=0, opt_text='$0.75 per contract',
      safety=4.0, bank=0, transfer_text='Fall Offer 2026: up to $150 per client on transfers of $15,000 or more', transfer_min=15000, transfer_max=150, per_client=True,
      cad_text='$0', us_text='$0'),
 dict(id='national-bank', nomin=1, name='National Bank Direct Brokerage', review=None, cad=0, us=0, fx=0.017, fx_pub=True, fx_text='About 1.70% under US$25,000',
      usd_reg='free', usd_reg_text='TFSA, RRSP, RRIF, spousal RRSP and LIRA (not FHSA); no USD fee listed', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=1, fhsa=1, resp=1, rrif=1, lira=1, margin=1, joint=0, corporate=1),
      frac=0, drip=1, options=1, adv=0.5, mobile=0.5, cash=0, margin_cad=0.0625, margin_text='6.25%',
      opt_base=0, opt_contract=1.25, opt_min=6.25, opt_text='$1.25 per contract, minimum $6.25',
      safety=3.5, bank=1, transfer_text='Reimburses transfer fees depending on the amount (threshold not published)', transfer_min=None, transfer_max=None, per_client=False,
      cad_text='$0', us_text='$0'),
 dict(id='cibc', nomin=1, name='CIBC Investor\'s Edge', review=None, cad=6.95, us=6.95, fx=0.016, fx_pub=True, fx_text='About 1.6% under $25,000',
      usd_reg='unknown', usd_reg_text='Not stated', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=0, fhsa=1, resp=1, rrif=1, lira=1, margin=1, joint=1, corporate=1),
      frac=1, drip=0, options=1, adv=0, mobile=1, cash=0, margin_cad=0.0625, margin_text='6.25% under $100,000',
      opt_base=6.95, opt_contract=1.25, opt_min=0, opt_text='$6.95 + $1.25 per contract',
      safety=3.5, bank=1, transfer_text='', transfer_min=None, transfer_max=None, per_client=False,
      cad_text='$6.95 ($0 under 25 with Smart Start)', us_text='$6.95'),
 dict(id='td', nomin=0.5, name='TD Direct Investing', review='/reviews/td-direct-investing/', cad=9.99, us=9.99, fx=0.0126, fx_pub=True, fx_text='1.26% under $25,000',
      usd_reg='unknown', usd_reg_text='TD Easy Trade: no fee for USD in TFSA and RRSP; TD Direct Investing not stated', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=0, fhsa=1, resp=0, rrif=0, lira=0, margin=1, joint=0, corporate=0),
      frac=1, drip=1, options=1, adv=1, mobile=1, cash=0, margin_cad=None, margin_text='Not published',
      opt_base=9.99, opt_contract=1.25, opt_min=0, opt_text='$9.99 + $1.25 per contract',
      safety=3.5, bank=1, transfer_text='', transfer_min=None, transfer_max=None, per_client=False,
      cad_text='$9.99 (TD Easy Trade: 100 free trades a year)', us_text='$9.99'),
 dict(id='rbc', nomin=1, name='RBC Direct Investing', review='/reviews/rbc-direct-investing/', cad=9.95, us=9.95, fx=0.016, fx_pub=True, fx_text='About 1.6% under $25,000',
      usd_reg='unknown', usd_reg_text='Accounts can hold CAD and USD; USD registered pricing not stated', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=1, fhsa=1, resp=1, rrif=1, lira=1, margin=1, joint=1, corporate=1),
      frac=0, drip=1, options=1, adv=1, mobile=1, cash=0, margin_cad=None, margin_text='Not published',
      opt_base=9.95, opt_contract=1.25, opt_min=0, opt_text='$9.95 + $1.25 per contract',
      safety=4.0, bank=1, transfer_text='Reimburses up to $200 of transfer fees on transfers of $15,000 or more', transfer_min=15000, transfer_max=200, per_client=True,
      cad_text='$9.95', us_text='$9.95'),
 dict(id='bmo', nomin=1, name='BMO InvestorLine', review=None, cad=0, us=0, fx=0.016, fx_pub=True, fx_text='About 1.6% under US$25,000',
      usd_reg='unknown', usd_reg_text='Not stated', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=0, fhsa=1, resp=1, rrif=1, lira=1, margin=1, joint=1, corporate=1),
      frac=0, drip=0, options=1, adv=1, mobile=1, cash=0, margin_cad=None, margin_text='Not published',
      opt_base=0, opt_contract=0.90, opt_min=0, opt_text='$0.90 per contract',
      safety=4.0, bank=1, transfer_text='', transfer_min=None, transfer_max=None, per_client=False,
      cad_text='$0', us_text='$0'),
 dict(id='scotia', nomin=0.5, name='Scotia iTRADE', review=None, cad=9.99, us=9.99, fx=None, fx_pub=False, fx_text='Not published',
      usd_reg='free', usd_reg_text='USD RRSP and RRIF available; no USD fee listed (TFSA and FHSA not stated)', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=0, fhsa=1, resp=1, rrif=1, lira=1, margin=1, joint=0, corporate=1),
      frac=0, drip=0, options=1, adv=0.5, mobile=0.5, cash=0, margin_cad=PRIME + 0.0165, margin_text='Prime + 1.65% under $25,000 (6.10%)',
      opt_base=9.99, opt_contract=1.25, opt_min=0, opt_text='$9.99 + $1.25 per contract',
      safety=4.0, bank=1, transfer_text='Newcomers (StartRight): credit of up to $150', transfer_min=None, transfer_max=None, per_client=True,
      cad_text='$9.99', us_text='$9.99'),
 dict(id='desjardins', nomin=1, name='Desjardins Online Brokerage (Disnat)', review=None, cad=0, us=0, fx=None, fx_pub=False, fx_text='Up to 1.90%, depending on the amount',
      usd_reg='free', usd_reg_text='USD RRSP, TFSA, LIRA, RRIF and LIF; no fee stated', admin=0,
      accts=dict(tfsa=1, rrsp=1, spousal=1, fhsa=1, resp=1, rrif=1, lira=1, margin=1, joint=0, corporate=1),
      frac=0, drip=0, options=1, adv=1, mobile=1, cash=0, margin_cad=PRIME + 0.0125, margin_text='Prime + 1.25% under $100,000 (5.70%)',
      opt_base=0, opt_contract=1.25, opt_min=8.75, opt_text='$1.25 per contract, minimum $8.75',
      safety=4.0, bank=1, transfer_text='', transfer_min=None, transfer_max=None, per_client=False,
      cad_text='$0', us_text='$0'),
]

BW = {'cost': 0.35, 'accounts': 0.15, 'us': 0.15, 'cash_margin': 0.10, 'platform': 0.15, 'safety': 0.10}
CAT = {
    'overall': BW,
    'us_stocks': {'cost': 0.25, 'accounts': 0.10, 'us': 0.40, 'cash_margin': 0.05, 'platform': 0.10, 'safety': 0.10},
    'beginners': {'cost': 0.35, 'accounts': 0.15, 'us': 0.05, 'cash_margin': 0.0, 'beginner_platform': 0.25, 'safety': 0.20},
    'options': {'options_cost': 0.50, 'platform': 0.25, 'cash_margin': 0.10, 'safety': 0.10, 'accounts': 0.05},
}

def fx_for_cost(b): return b['fx'] if b['fx'] is not None else MEDIAN_FX

def annual_cost(b, cad_trades, us_trades, conv, conversions=4):
    fx = fx_for_cost(b) * conv + b.get('fx_fixed', 0) * (conversions if conv else 0)
    return 12 * (cad_trades * b['cad'] + us_trades * b['us']) + fx + b['admin']

def options_annual(b, trades=4, contracts=2):
    per = max(b['opt_base'] + b['opt_contract'] * contracts, b['opt_min'])
    return 12 * trades * per

def sub_scores(b):
    a = annual_cost(b, 2, 1, 6000)          # active profile: 2 Canadian + 1 US trade a month, $6,000 converted a year
    h = annual_cost(b, 1, 0, 0)             # buy-and-hold profile: 1 Canadian trade a month, no conversions
    cost = clamp(5 - ((a + h) / 2) / 80)
    accts = 5 * sum(b['accts'].values()) / 10
    usd = {'free': 2.0, 'paid': 1.0, 'unknown': 0.5}[b['usd_reg']]
    if b['fx'] is None: fxs = 0.5
    elif b['fx'] <= 0.001: fxs = 2.0
    elif b['fx'] <= 0.013: fxs = 1.25
    elif b['fx'] <= 0.015: fxs = 1.0
    else: fxs = 0.75
    usc = 1.0 if b['us'] == 0 else (0.75 if b['us'] <= 2 else 0)
    us = usd + fxs + usc
    m = b['margin_cad']
    mpts = 0.5 if m is None else (2.5 if m <= 0.04 else 2.0 if m <= 0.05 else 1.5 if m <= 0.06 else 1.0 if m <= 0.065 else 0.5)
    cpts = 2.5 if b['cash'] >= 0.01 else (1.0 if b['cash'] > 0 else 0)
    cm = mpts + cpts
    plat = b['frac'] + b['drip'] + b['options'] + b['adv'] + b['mobile']
    beg = 1.5 * b['frac'] + 1.5 * min(b['mobile'], 1) + b['drip'] + b['nomin']
    saf = clamp(b['safety'] + b['bank'])
    oc = options_annual(b)
    opt = clamp(5 - oc / 120)
    return dict(cost=round(cost, 2), accounts=round(accts, 2), us=round(us, 2), cash_margin=round(cm, 2), platform=round(plat, 2), beginner_platform=round(beg, 2), safety=round(saf, 2), options_cost=round(opt, 2)), dict(active=round(a, 2), hold=round(h, 2), options=round(oc, 2))

brokers_out = []
for b in BR:
    s, costs = sub_scores(b)
    row = dict(id=b['id'], name=b['name'], review=b['review'], sub=s, profile_costs=costs)
    for cat, w in CAT.items():
        row['score_' + cat] = round(sum(s[k] * v for k, v in w.items()), 3)
    brokers_out.append(row)

def ranked(cat, filt=None):
    rows = [r for r in brokers_out if (filt is None or filt(r))]
    rows.sort(key=lambda r: (-r['score_' + cat], r['name']))
    return [dict(rank=i + 1, id=r['id'], name=r['name'], score=round(r['score_' + cat], 1), review=r['review']) for i, r in enumerate(rows)]

bid = {b['id']: b for b in BR}
lists = {
    'best-online-brokers': ranked('overall'),
    'best-brokers-for-us-stocks': ranked('us_stocks'),
    'best-brokers-for-beginners': ranked('beginners'),
    'best-options-trading-platforms': ranked('options'),
    'best-commission-free-brokers': ranked('overall', lambda r: bid[r['id']]['cad'] == 0 and bid[r['id']]['us'] == 0),
    'best-investing-apps': ranked('beginners', lambda r: bid[r['id']]['mobile'] >= 1),
}
for acct in ('tfsa', 'rrsp', 'fhsa', 'resp', 'rrif', 'lira'):
    lists[f'brokers-offering-{acct}'] = ranked('overall', lambda r, a=acct: bid[r['id']]['accts'][a] == 1)
lists['best-tfsa-for-us-stocks'] = ranked('us_stocks', lambda r: bid[r['id']]['accts']['tfsa'] == 1)
lists['best-rrsp-for-us-stocks'] = ranked('us_stocks', lambda r: bid[r['id']]['accts']['rrsp'] == 1)
# stated-metric lists
fx_rows = sorted([b for b in BR if b['fx'] is not None], key=lambda b: b['fx'] * 10000 + b.get('fx_fixed', 0))
lists['lowest-fx-fees_by_cost_on_10000'] = [dict(rank=i + 1, id=b['id'], name=b['name'], cost_on_10000=round(b['fx'] * 10000 + b.get('fx_fixed', 0), 2), fx_text=b['fx_text']) for i, b in enumerate(fx_rows)]
lists['lowest-fx-fees_not_published'] = [dict(id=b['id'], name=b['name'], fx_text=b['fx_text']) for b in BR if b['fx'] is None]
m_rows = sorted([b for b in BR if b['margin_cad'] is not None], key=lambda b: b['margin_cad'])
lists['margin-rates_by_rate'] = [dict(rank=i + 1, id=b['id'], name=b['name'], cad_margin_rate=round(b['margin_cad'] * 100, 3), margin_text=b['margin_text']) for i, b in enumerate(m_rows)]
lists['margin-rates_not_published'] = [b['name'] for b in BR if b['margin_cad'] is None]

# ------------------------------------------------------------------ robo-advisors (ranked only where fee and fund costs are both published)
RB = [
 dict(id='questwealth', name='Questwealth Portfolios', review='/reviews/questrade/', tiers=[[99999.99, 0.0025], [None, 0.0020]], mode='flat', mer=0.0012, mer_text='up to 0.12% (standard portfolios)',
      fee_text='0.25%; 0.20% from $100,000', minimum=250, accts=9, portfolios=2, advice=2.0, accounts_text='TFSA, RRSP, spousal RRSP, RESP, family RESP, RRIF, LIRA, LIF, cash, margin, corporate'),
 dict(id='wealthsimple-managed', name='Wealthsimple Managed Investing', review='/reviews/wealthsimple/managed-investing/', tiers=[[99999.99, 0.005], [None, 0.004]], mode='flat', mer=0.0015, mer_text='up to 0.15% (Classic portfolios)',
      fee_text='0.5% Core; 0.4% Premium ($100,000+); 0.4% falling to 0.2% at $10M+ on Generation', minimum=1, accts=9, portfolios=4, advice=4.5, accounts_text='TFSA, RRSP, spousal RRSP, FHSA, RESP, RRIF, LIRA, non-registered, corporate'),
 dict(id='rbc-investease', name='RBC InvestEase', review='/reviews/rbc-direct-investing/', tiers=[[None, 0.005]], mode='flat', mer=0.0020, mer_text='up to 0.20% (Core portfolios)',
      fee_text='0.50% flat', minimum=100, accts=4, portfolios=2, advice=4.5, accounts_text='TFSA, FHSA, RRSP, non-registered'),
 dict(id='ci-direct', name='CI Direct Investing', review=None, tiers=[[150000, 0.006], [500000, 0.004], [None, 0.0035]], mode='marginal', mer=0.0023, mer_text='up to 0.23% (ETF portfolios)',
      fee_text='0.60% on the first $150,000; 0.40% on the next $350,000; 0.35% above $500,000', minimum=100, accts=9, portfolios=3, advice=5.0, accounts_text='TFSA, RRSP, spousal RRSP, RESP, RRIF, LIRA, LIF, non-registered, joint'),
]
def robo_fee(r, amt):
    fee = 0
    if r['mode'] == 'flat':
        for up, rate in r['tiers']:
            if up is None or amt <= up: fee = amt * rate; break
    else:
        lo = 0
        for up, rate in r['tiers']:
            hi = float('inf') if up is None else up
            if amt > lo: fee += (min(amt, hi) - lo) * rate
            lo = hi
    return fee + amt * r['mer']
RW = {'fees': 0.45, 'accounts': 0.15, 'portfolios': 0.15, 'minimum': 0.10, 'advice': 0.15}
robos_out = []
for r in RB:
    total_pct = robo_fee(r, 50000) / 50000
    s = dict(fees=round(clamp(5 - (total_pct * 100 - 0.35) * 5), 2), accounts=round(5 * r['accts'] / 10, 2),
             portfolios={1: 2.0, 2: 3.0, 3: 4.0}.get(r['portfolios'], 5.0), minimum=5.0 if r['minimum'] <= 100 else (4.5 if r['minimum'] <= 500 else 4.0), advice=r['advice'])
    robos_out.append(dict(id=r['id'], name=r['name'], review=r['review'], total_cost_pct_at_50000=round(total_pct * 100, 3), sub=s, score=round(sum(s[k] * w for k, w in RW.items()), 3)))
robos_out.sort(key=lambda x: (-x['score'], x['name']))
for i, r in enumerate(robos_out, 1): r['rank'] = i
robo_not_ranked = [
    dict(name='BMO SmartFolio', reason='Advisory fee of 0.4% to 0.7% with breakpoints not published, and fund costs not published.'),
    dict(name='Justwealth', reason='Fee tiers are published only as an image; minimum fee $4.99 a month ($2.50 for RESP, FHSA and RDSP); $5,000 minimum except RESP and FHSA.'),
    dict(name='TD Automated Investing', reason='Not listed among TD\'s current investing services; could not confirm it accepts new clients.'),
    dict(name='Nest Wealth', reason='Website shows it is temporarily unavailable; could not confirm it accepts retail clients.'),
    dict(name='Qtrade Guided Portfolios', reason='No longer shown on Qtrade\'s site; could not confirm it is offered.'),
]

# ------------------------------------------------------------------ crypto (CSA-authorized platforms)
CR = [
 dict(name='NDAX', fee=0.002, fee_text='0.20% flat', coins=None, staking=1, withdrawals=1, funding=4.0, reg=4.0),
 dict(name='Wealthsimple Crypto', link='/reviews/wealthsimple/crypto/', fee=0.005, fee_text='0.5% plus a spread (no spread on limit orders)', coins=170, staking=1, withdrawals=1, funding=4.0, reg=5.0),
 dict(name='Kraken', fee=0.01, fee_text='1% on app instant buys; Kraken Pro 0.40% maker, 0.80% taker', coins=None, staking=0, withdrawals=0, funding=2.5, reg=3.0),
 dict(name='Newton', fee=0.0115, fee_text='Up to 1.15% on BTC, ETH and USDC; up to 1.60% on other coins', coins=50, staking=1, withdrawals=1, funding=5.0, reg=5.0),
 dict(name='Coinbase Canada', fee=None, fee_text='Varies by payment method and order size; spread included in the price', coins=200, staking=1, withdrawals=1, funding=4.0, reg=3.0),
 dict(name='Shakepay', fee=None, fee_text='No commission; spread of undisclosed size', coins=2, staking=0, withdrawals=1, funding=5.0, reg=5.0),
 dict(name='Netcoins', fee=None, fee_text='No separate fee; spread of undisclosed size', coins=60, staking=1, withdrawals=1, funding=4.0, reg=3.0),
 dict(name='Crypto.com', fee=None, fee_text='No app trading fee up to Level Up limits; spread may apply', coins=400, staking=1, withdrawals=0, funding=4.0, reg=3.0),
 dict(name='Robinhood Canada (Coinsquare)', fee=None, fee_text='Fee schedule not published on the pages checked', coins=50, staking=0, withdrawals=1, funding=2.5, reg=5.0),
]
CWt = {'fees': 0.35, 'coins': 0.15, 'features': 0.15, 'funding': 0.15, 'regulation': 0.20}
crypto_out = []
for c in CR:
    fees = 2.5 if c['fee'] is None else clamp(5 - (c['fee'] * 100 - 0.2) * 2.5)
    n = c['coins']; coins = 2.5 if n is None else (5 if n >= 150 else 4 if n >= 100 else 3 if n >= 50 else 2 if n >= 10 else 1)
    s = dict(fees=round(fees, 2), coins=coins, features=3 * c['staking'] + 2 * c['withdrawals'], funding=c['funding'], regulation=c['reg'])
    crypto_out.append(dict(name=c['name'], link=c.get('link'), fee_text=c['fee_text'], sub=s, score=round(sum(s[k] * w for k, w in CWt.items()), 3)))
crypto_out.sort(key=lambda x: (-x['score'], x['name']))
for i, c in enumerate(crypto_out, 1): c['rank'] = i

# ------------------------------------------------------------------ tax software
TS = [
 dict(name='Wealthsimple Tax', link='/reviews/wealthsimple/tax/', price=5.0, features=5.0, support=4.0, qc=5.0),
 dict(name='TurboTax Canada', price=3.5, features=5.0, support=5.0, qc=5.0),
 dict(name='H&R Block Canada', price=3.5, features=5.0, support=5.0, qc=5.0),
 dict(name='UFile', price=3.5, features=4.0, support=3.0, qc=5.0),
 dict(name='CloudTax', price=5.0, features=4.0, support=5.0, qc=2.5),
 dict(name='GenuTax', price=5.0, features=3.0, support=1.0, qc=2.5),
 dict(name='StudioTax', price=3.0, features=3.0, support=1.0, qc=2.5),
]
TW = {'price': 0.35, 'features': 0.35, 'support': 0.15, 'qc': 0.15}
tax_out = []
for t in TS:
    s = {k: t[k] for k in TW}
    tax_out.append(dict(name=t['name'], link=t.get('link'), sub=s, score=round(sum(s[k] * w for k, w in TW.items()), 3)))
tax_out.sort(key=lambda x: (-x['score'], x['name']))
for i, t in enumerate(tax_out, 1): t['rank'] = i

banking = json.load(open('/home/claude/ws100/briefs/scores_banking.json'))
methodology = {
    'brokers': {'weights_overall': BW, 'category_weights': CAT,
                'cost': 'Average yearly cost of two profiles at published prices for a TFSA with $20,000: active (two Canadian and one US trade a month, $6,000 converted to US dollars a year in four conversions) and buy-and-hold (one Canadian trade a month). Trades are $2,000 orders of 40 shares; US-dollar fees are counted at par. Where a broker publishes no conversion rate or only an undisclosed spread, its conversion cost is counted at the median published rate of 1.5%. Score = 5 minus the average cost divided by $80, from 0 to 5.',
                'accounts': 'Half a point for each of 10 account types: TFSA, RRSP, spousal RRSP, FHSA, RESP, RRIF, LIRA or LIF, margin, joint and corporate.',
                'us': 'USD in registered accounts: 2 if offered with no fee, 1 if a fee applies, 0.5 if not stated. Conversion fee: 2 at 0.1% or less, 1.25 up to 1.3%, 1 at 1.5%, 0.75 above 1.5%, 0.5 if not published. US commission: 1 at $0, 0.75 at $2 or less, 0 above.',
                'cash_margin': 'CAD margin rate under $100,000: 2.5 at 4% or less, 2 up to 5%, 1.5 up to 6%, 1 up to 6.5%, 0.5 above 6.5% or not published. Headline interest on uninvested CAD cash: 2.5 at 1% or more, 1 above 0%, 0 otherwise; rates paid only on balances above $1,000,000 are not counted.',
                'platform': 'One point each for fractional shares, DRIP, options, an advanced trading platform and a mobile app; half a point where only partly offered or not named.',
                'safety': '4 when CIRO and CIPF membership are both stated by the broker, 3.5 when CIPF membership is confirmed and CIRO membership follows from it; plus 1 when the broker is owned by a bank or a financial cooperative group.',
                'beginner_platform': 'Fractional shares 1.5, a mobile app 1.5, DRIP 1 and no account minimum 1 (0.5 where the minimum is not stated).',
                'ties': 'Scores are shown to one decimal. Ties are ordered by the unrounded score, then by name.',
                'options_cost': 'Yearly cost of four US equity options trades a month of two contracts each; score = 5 minus cost divided by $120, from 0 to 5.'},
    'robos': {'weights': RW, 'fees': 'Management fee plus the highest published fund cost (MER) for the core portfolios, on $50,000: score = 5 minus (total % minus 0.35) x 5.',
              'accounts': 'Half a point for each of 10 account types.', 'portfolios': 'Portfolio families: 1 = 2, 2 = 3, 3 = 4, 4 or more = 5.',
              'minimum': 'The stated minimum, or where none is stated, the lowest balance in the published fee schedule (Wealthsimple Core starts at $1; Questwealth\'s lowest fee tier starts at $250): 5 at $100 or less, 4.5 up to $500, 4 above.', 'advice': '5 = planners or advisors for every client; 4.5 = advisors by phone or email; 2 = no client advice described.',
              'not_ranked_rule': 'A robo-advisor is ranked only when both its management fee schedule and its fund costs are published in text we can verify.'},
    'crypto': {'weights': CWt, 'fees': 'Published trading fee f%: 5 minus (f minus 0.2) x 2.5; 2.5 where only an undisclosed spread or no fee schedule is published.',
               'coins': '5 at 150 or more, 4 at 100, 3 at 50, 2 at 10, 1 below; 2.5 if not published.', 'features': '3 for staking available in Canada, 2 for crypto withdrawals to outside wallets.',
               'funding': '5 = free CAD deposits and withdrawals; 4 = free deposits, fees or no statement on withdrawals; 2.5 = not published.',
               'regulation': '5 = CIRO investment dealer and CIPF member; 4 = on CIPF\'s member list; 3 = registered with securities regulators (for example as a restricted dealer) but not on CIPF\'s list. Only platforms on the CSA list of authorized crypto trading platforms are included.'},
    'tax_software': {'weights': TW, 'price': '5 = a full-featured free tier; 3.5 = free only for simple returns; 3 = price not published.',
                     'features': '5 = all income types including self-employment and investments; 4 = most; 3 = basic or not confirmed.',
                     'support': '5 = expert review or full service available; 4 = expert consultation on a paid tier; 3 = phone support; 1 = none.',
                     'qc': '5 = files Quebec returns; 2.5 = not confirmed.'},
    'chequing': banking['rubric'],
}
out = dict(as_of='2026-10-22', brokers=brokers_out, broker_lists=lists, robos=robos_out, robos_not_ranked=robo_not_ranked,
           crypto=crypto_out, tax_software=tax_out, chequing=banking['chequing'], no_fee_chequing_order=banking['no_fee_chequing_order'], methodology=methodology)
json.dump(out, open('/home/claude/ws100/briefs/scores.json', 'w'), indent=1)

# ------------------------------------------------------------------ widget data
widget = {'brokers': [], 'robos': [], 'crypto': [], 'tax_software_year': 2025}
FX_TIERS = {
    'interactive-brokers': [[None, 0.00002]],
    'national-bank': [[24999.99, 0.017], [249999.99, 0.012], [499999.99, 0.009], [999999.99, 0.007], [None, 0.006]],
    'cibc': [[24999.99, 0.016], [99999.99, 0.009], [249999.99, 0.005]],
    'td': [[24999, 0.0126], [99999, 0.0078], [499999, 0.0046], [999999, 0.0027], [None, 0.0019]],
    'rbc': [[24999, 0.016], [99999, 0.010], [499999, 0.006], [999999, 0.004], [1999999, 0.002], [None, 0.001]],
    'bmo': [[24999.99, 0.016], [74999.99, 0.009], [99999.99, 0.008], [249999.99, 0.005], [None, 0.004]],
}
# Wealthsimple's tiers apply only inside its USD account ($10 a month on Core); US trades from a CAD account pay 1.5%.
USD_ACCT_TIERS = {'wealthsimple': [[9999.99, 0.015], [24999.99, 0.01], [99999.99, 0.005], [None, 0.0]]}
TIERS_CCY = {'national-bank': 'USD', 'bmo': 'USD'}
FX_TIER_NOTE = {
    'wealthsimple': 'US trades from a CAD account pay 1.5%.',
    'national-bank': 'Tiers are set in US dollars.', 'bmo': 'Tiers are set in US dollars; above US$250,000 the spread is no more than 0.4%.',
    'cibc': 'Above $250,000 CIBC publishes its spread in basis points of the rate, not as a percentage; the cost shown uses 0.5%, so the real cost is lower.',
    'rbc': 'From $2,000,000 the spread is no more than 10 basis points.',
}
for b, row in zip(BR, brokers_out):
    flags = [k for k, v in b['accts'].items() if v == 1]
    if b['frac']: flags.append('fractional')
    if b['drip']: flags.append('drip')
    if b['cad'] == 0 and b['us'] == 0: flags.append('zero_commission')
    if b['usd_reg'] in ('free', 'paid'): flags.append('usd_reg')
    widget['brokers'].append(dict(id=b['id'], name=b['name'], review=b['review'] or '/compare/best-online-brokers/', cad_trade=b['cad'], us_trade=b['us'],
                                  fx_pct=(0.00002 if b['id'] == 'interactive-brokers' else b['fx']), fx_fixed=b.get('fx_fixed', 0), fx_text=b['fx_text'], fx_tiers=FX_TIERS.get(b['id']), usd_acct_tiers=USD_ACCT_TIERS.get(b['id']), tiers_ccy=TIERS_CCY.get(b['id'], 'CAD'), fx_note=FX_TIER_NOTE.get(b['id']), usd_reg_text=b['usd_reg_text'], annual_fee=b['admin'],
                                  opt_base=b['opt_base'], opt_contract=b['opt_contract'], opt_min=b['opt_min'], opt_text=b['opt_text'],
                                  margin_cad=b['margin_cad'], margin_text=b['margin_text'], transfer_in_text=b['transfer_text'] or None,
                                  transfer_min=b['transfer_min'], transfer_max=b['transfer_max'], per_client=b['per_client'],
                                  cad_text=b['cad_text'], us_text=b['us_text'], flags=flags, score=round(row['score_overall'], 1)))
widget['broker_features'] = [['tfsa', 'TFSA'], ['rrsp', 'RRSP'], ['spousal', 'Spousal RRSP'], ['fhsa', 'FHSA'], ['resp', 'RESP'], ['rrif', 'RRIF'], ['lira', 'LIRA or LIF'],
                             ['margin', 'Margin'], ['joint', 'Joint account'], ['corporate', 'Corporate account'], ['usd_reg', 'USD in registered accounts'],
                             ['zero_commission', '$0 stock and ETF commissions'], ['fractional', 'Fractional shares'], ['drip', 'DRIP']]
for r in RB:
    widget['robos'].append(dict(name=r['name'], review=r['review'], tiers=r['tiers'], tier_mode=r['mode'], mer=r['mer'], mer_text=r['mer_text'], fee_text=r['fee_text'], min=r['minimum']))
for c in CR:
    widget['crypto'].append(dict(name=c['name'], link=c.get('link'), fee_pct=c['fee'], fee_text=c['fee_text']))
widget['tax_software'] = [
 dict(name='Wealthsimple Tax', link='/reviews/wealthsimple/tax/', netfile=True, qc=True, tiers=[
     dict(name='Basic', price_text='Pay what you want, including $0 (up to 2 returns)', self=True, rent=None, inv=True, help=False, qc=True),
     dict(name='Plus', price_text='$40 plus tax (included for Premium clients)', self=True, rent=None, inv=True, help=False, qc=True),
     dict(name='Pro', price_text='$80 plus tax (included for Generation clients); 30-minute expert consultation', self=True, rent=None, inv=True, help=True, qc=False)]),
 dict(name='TurboTax Canada', netfile=True, qc=True, tiers=[
     dict(name='TurboTax Free', price_text='$0 for simple returns', self=False, rent=False, inv=False, help=False, qc=True),
     dict(name='Do It Yourself', price_text='Price depends on the complexity of your return', self=True, rent=None, inv=True, help=False, qc=True),
     dict(name='Expert Assist', price_text='Price depends on the complexity of your return', self=True, rent=None, inv=True, help=True, qc=True)]),
 dict(name='H&R Block Canada', netfile=True, qc=True, tiers=[
     dict(name='Free', price_text='$0 for returns that qualify', self=False, rent=None, inv=None, help=False, qc=True),
     dict(name='Self Employed', price_text='Paid tier (price for the 2025 tax year not confirmed)', self=True, rent=None, inv=None, help=False, qc=True)]),
 dict(name='UFile', netfile=True, qc=True, tiers=[
     dict(name='UFile ONLINE', price_text='From $20.95; free for students, first-time filers and family income under $20,000', self=None, rent=None, inv=None, help=False, qc=True),
     dict(name='UFile PREMIUM', price_text='From $32.95', self=None, rent=None, inv=None, help=False, qc=True)]),
 dict(name='CloudTax', netfile=True, qc=None, tiers=[
     dict(name='Free', price_text='$0 or pay what you want (up to 2 returns)', self=None, rent=None, inv=None, help=False, qc=None),
     dict(name='Review & File', price_text='From $49 per return', self=None, rent=None, inv=None, help=True, qc=None)]),
 dict(name='GenuTax', netfile=True, qc=None, tiers=[dict(name='GenuTax Standard', price_text='Free (donations optional)', self=None, rent=None, inv=None, help=False, qc=None)]),
 dict(name='StudioTax', netfile=True, qc=None, tiers=[
     dict(name='Mobile app', price_text='Free', self=None, rent=None, inv=None, help=False, qc=None),
     dict(name='Computer download', price_text='Paid; price not published', self=None, rent=None, inv=None, help=False, qc=None)]),
]
wsT = dict(household=True, list=[
    dict(name='Core', **{'from': 1}, perks=['Chequing interest 1.25% (1.75% with $2,000+ direct deposit in 30 days)', 'Managed investing fee 0.5%', 'USD account $10 a month', 'CAD margin 4.95%', 'Instant deposits up to $50,000']),
    dict(name='Premium', **{'from': 100000}, perks=['Chequing interest 1.75% (2.25% with $2,000+ direct deposit in 30 days)', 'Managed investing fee 0.4% and tax-loss harvesting', 'USD account included', 'CAD margin 4.45%', 'Wealthsimple Tax Plus included', 'Priority phone support', 'Credit card monthly fee waived ($100,000+ in assets)']),
    dict(name='Generation', **{'from': 500000}, perks=['Chequing interest 2.25%', 'Managed investing fee 0.4%, falling to 0.2% at $10,000,000+', 'USD account included', 'CAD margin 3.95%', 'Wealthsimple Tax Pro included', 'Priority phone and email support', 'Domestic wire fee waived'])],
    rows=[['Assets needed', '$1', '$100,000', '$500,000'], ['Chequing interest', '1.25%', '1.75%', '2.25%'], ['With $2,000+ direct deposit', '1.75%', '2.25%', '2.25%'],
          ['Managed investing fee', '0.5%', '0.4%', '0.4% to 0.2%'.replace(' to ', ', down to ')], ['USD account', '$10 a month', 'Included', 'Included'],
          ['FX fee on US trades from a CAD account', '1.5%', '1.5%', '1.5%'], ['CAD margin rate', '4.95%', '4.45%', '3.95%'], ['Wealthsimple Tax', 'Basic', 'Plus included', 'Pro included']])
widget['ws_tiers'] = wsT
widget['cards'] = [dict(name='Wealthsimple Visa Infinite+', rate=0.02, fee_month=20, fee_note='$20 a month, waived with $100,000+ in assets or $4,000+ a month in direct deposits')]
json.dump(widget, open('/home/claude/ws100/site-wide/src/providers-widget-data.json', 'w'), indent=1)

print('BROKERS overall'); [print(' ', x['rank'], x['name'], x['score']) for x in lists['best-online-brokers']]
print('US'); [print(' ', x['rank'], x['name'], x['score']) for x in lists['best-brokers-for-us-stocks']]
print('Beginners'); [print(' ', x['rank'], x['name'], x['score']) for x in lists['best-brokers-for-beginners']]
print('Options'); [print(' ', x['rank'], x['name'], x['score']) for x in lists['best-options-trading-platforms']]
print('ROBOS'); [print(' ', r['rank'], r['name'], round(r['score'], 2), r['total_cost_pct_at_50000']) for r in robos_out]
print('CRYPTO'); [print(' ', c['rank'], c['name'], round(c['score'], 2)) for c in crypto_out]
print('TAX'); [print(' ', t['rank'], t['name'], round(t['score'], 2)) for t in tax_out]
for r in brokers_out: print(r['name'], r['sub'], r['profile_costs'])
