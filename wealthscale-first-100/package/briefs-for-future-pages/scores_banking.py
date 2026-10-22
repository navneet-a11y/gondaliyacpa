#!/usr/bin/env python3
"""Chequing account scores (published on /methodology/brokers/). Inputs come from providers-banking.json (Oct 22, 2026)."""
import json

def interp(x, pts):
    if x <= pts[0][0]: return pts[0][1]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1: return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return pts[-1][1]

RUBRIC = {
    'weights': {'fees': 0.35, 'interest': 0.20, 'transactions': 0.15, 'atm': 0.15, 'protection_features': 0.15},
    'fees': '5.0 = $0 monthly fee with no conditions; 4.5 = $0 monthly fee but per-transaction fees below a balance of $1,000 or less; 3.0 = fee of $4 or less a month; 2.5 = fee over $15 a month waived at a daily balance of $4,500 or less; 1.5 = fee over $15 a month with no balance waiver',
    'interest': 'Everyday interest rate on the chequing balance with no paid plan, interpolated: 0% = 0, 1% = 2.5, 2% = 4.0, 2.75% or more = 5.0. Rate not published = 0. Direct-deposit bonus rates count at half their extra value',
    'transactions': '5.0 = unlimited transactions and free e-Transfers; 3.0 = 18 transactions a month with e-Transfers included; 2.5 = 12 transactions a month; minus 0.5 if sending an e-Transfer costs a fee',
    'atm': '5.0 = no ATM fee anywhere in Canada (or fees reimbursed); 4.0 = large own network plus a shared network, fees elsewhere; 3.5 = own network, fees elsewhere; 2.5 = fees at all ATMs or not published',
    'protection_features': '5.0 = CDIC member (in its own right or through its parent bank) whose account does not rule out cheques; 4.0 = CDIC member whose account offers no cheques; 3.5 = deposits held in trust at CDIC members (provider not a member) with a chequebook available; 3.0 = held in trust at CDIC members, with cheques not offered or not stated',
}

# name, review link (if page exists), monthly fee (number), fee rule score, interest rate %, dd bonus extra %, transactions score, atm score, protection score, fee_text, waive_balance
A = [
 ('Wealthsimple Chequing', '/reviews/wealthsimple/chequing/', 0, 5.0, 1.25, 0.50, 5.0, 5.0, 3.5, '$0', None, 'Core 1.25%; 1.75% with $2,000+ direct deposit in 30 days; Premium 1.75% (2.25% with direct deposit); Generation 2.25%'),
 ('EQ Bank Personal Account', '/reviews/eq-bank/', 0, 5.0, 1.00, 1.75, 5.0, 5.0, 4.0, '$0', None, '1.00%; 2.75% when you direct deposit your pay'),
 ('Simplii No Fee Chequing Account', None, 0, 5.0, 0.0, 0, 5.0, 4.0, 5.0, '$0', None, 'Not published'),
 ('Tangerine No-Fee Daily Chequing Account', None, 0, 5.0, 0.0, 0, 5.0, 4.0, 5.0, '$0', None, 'Not published'),
 ('KOHO Essential', None, 0, 4.5, 2.0, 0, 5.0, 2.5, 3.0, '$7 a month, $0 with direct deposit or $1,000 a month in deposits', None, '2% (Essential plan)'),
 ('Neo Chequing', None, 0, 5.0, 0.1, 0, 4.5, 2.5, 3.0, '$0', None, '0.1%'),
 ('PC Money Account', None, 0, 5.0, 0.0, 0, 5.0, 3.5, 5.0, '$0', None, 'Not published'),
 ('Manulife Bank Advantage Account', None, 0, 4.5, 1.50, 0, 4.5, 2.5, 5.0, '$0; transaction fees below a $1,000 balance', 1000, '1.50% (3.00% promotional for 2 years on new accounts opened by October 30, 2026)'),
 ('National Bank The Minimalist', None, 3.95, 3.0, 0.0, 0, 3.0, 4.0, 5.0, '$3.95 a month (ages 25 and up)', None, 'Not published'),
 ('National Bank The Connected', None, 15.95, 2.5, 0.0, 0, 5.0, 4.0, 5.0, '$15.95 a month, $0 with a $4,500 balance', 4500, 'Not published'),
 ('RBC Day to Day Banking', None, 4.0, 3.0, 0.0, 0, 2.5, 3.5, 5.0, '$4 a month', None, 'Not published'),
 ('RBC Signature No Limit Banking', None, 16.95, 1.5, 0.0, 0, 5.0, 3.5, 5.0, '$16.95 a month', None, 'No interest'),
 ('TD Minimum Chequing Account', None, 3.95, 3.0, 0.0, 0, 2.5, 3.5, 5.0, '$3.95 a month', None, '0.000%'),
 ('TD Unlimited Chequing Account', None, 17.95, 2.5, 0.0, 0, 5.0, 4.0, 5.0, '$17.95 a month, $0 with a $4,000 daily balance', 4000, '0.000%'),
 ('BMO Practical Chequing', None, 4.0, 3.0, 0.0, 0, 2.5, 3.5, 5.0, '$4 a month', None, 'Not published'),
 ('BMO Performance Chequing', None, 17.95, 2.5, 0.0, 0, 5.0, 3.5, 5.0, '$17.95 a month, $0 with a $4,000 daily balance', 4000, 'Not published'),
 ('Scotiabank Basic Bank Account', None, 3.95, 3.0, 0.0, 0, 3.0, 3.5, 5.0, '$3.95 a month', None, 'No interest'),
 ('Scotiabank Preferred Package', None, 16.95, 2.5, 0.0, 0, 5.0, 3.5, 5.0, '$16.95 a month, $0 with $4,000 every day', 4000, 'No interest'),
 ('CIBC Everyday Chequing Account', None, 4.0, 3.0, 0.0, 0, 3.0, 3.5, 5.0, '$4 a month', None, 'Not published'),
 ('CIBC Smart Account', None, 16.95, 2.5, 0.0, 0, 5.0, 3.5, 5.0, '$16.95 a month, rebate with $4,000 every day', 4000, 'Not published'),
]
W = RUBRIC['weights']
out = []
for a in A:
    name, link, fee, fs, rate, dd, ts, atm, prot, fee_text, waive, rate_text = a
    eff = rate + dd / 2
    ints = round(interp(eff, [(0, 0), (1.0, 2.5), (2.0, 4.0), (2.75, 5.0)]), 2)
    score = fs * W['fees'] + ints * W['interest'] + ts * W['transactions'] + atm * W['atm'] + prot * W['protection_features']
    out.append(dict(name=name, review=link, monthly_fee=fee, fee_text=fee_text, waive_balance=waive, base_rate=rate / 100, rate_text=rate_text,
                    sub=dict(fees=fs, interest=ints, transactions=ts, atm=atm, protection_features=prot), score=round(score, 1), score_exact=round(score, 3)))
out.sort(key=lambda x: (-x['score_exact'], x['name']))
for i, o in enumerate(out, 1):
    o['rank'] = i
nofee = [o for o in out if o['monthly_fee'] == 0]
res = {'as_of': '2026-10-22', 'rubric': RUBRIC, 'chequing': out, 'no_fee_chequing_order': [o['name'] for o in nofee]}
json.dump(res, open('/home/claude/ws100/briefs/scores_banking.json', 'w'), indent=1)
for o in out: print(o['rank'], o['name'], o['score'], o['sub'])
