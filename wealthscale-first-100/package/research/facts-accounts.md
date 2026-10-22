# Verified facts register: Canadian registered accounts and investor protection

Checked on: 2026-10-22. Prepared in the capacity of a Canadian CPA and registered-plans specialist.
Machine-readable copy: `facts-accounts.json` (224 entries, same keys). Every figure below was read on the official page linked in its row. "Calculated" means arithmetic applied to a verified official figure or formula.

Status counts: 214 verified, 2 not yet published, 8 unverified (listed at the end).

---

## 1. TFSA

### Annual dollar limits (key `tfsa.limit.YYYY`)

| Year | Limit (CAD) | Year | Limit (CAD) |
|---|---|---|---|
| 2009 | 5,000 | 2018 | 5,500 |
| 2010 | 5,000 | 2019 | 6,000 |
| 2011 | 5,000 | 2020 | 6,000 |
| 2012 | 5,000 | 2021 | 6,000 |
| 2013 | 5,500 | 2022 | 6,000 |
| 2014 | 5,500 | 2023 | 6,500 |
| 2015 | 10,000 | 2024 | 7,000 |
| 2016 | 5,500 | 2025 | 7,000 |
| 2017 | 5,500 | 2026 | 7,000 |
| | | **2027** | **Not yet published** |

Source: [CRA, Before you contribute](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html). For 2027: [CRA limits table](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) shows TFSA limits only to 2026. Figures like $7,500 on private sites are estimates.
Note: one worked example on CRA's Calculate your contribution room page mislabels 2023 as $7,000. Both CRA limit tables say $6,500.

### TFSA rules

| Key | Fact | Value | Notes | Source |
|---|---|---|---|---|
| tfsa.cumulative.2026 | Cumulative room 2009 to 2026 | **$109,000** | Calculated from CRA annual limits. Applies to someone 18+ and resident every year since 2009 who never contributed. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html) |
| tfsa.limit.indexation | How the limit is set | Indexed to inflation, rounded to nearest $500 | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html) |
| tfsa.eligibility.open | Who can open | Resident, 18+, valid SIN | Banks, insurers, credit unions and trust companies can issue TFSAs. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/opening.html) |
| tfsa.eligibility.age_of_majority_19 | Where the age of majority is 19 | Open at 19; the year-18 room carries over | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/opening.html) |
| age_of_majority.18 | Age of majority 18 | AB, MB, ON, PE, QC, SK | Same list on IRCC's minors page. | [Justice Canada](https://www.justice.gc.ca/eng/rp-pr/fl-lf/child-enfant/guide/step2-etap2.html) |
| age_of_majority.19 | Age of majority 19 | BC, NB, NL, NT, NS, NU, YT | Same list on [IRCC](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/prepare/minor-children.html). | [Justice Canada](https://www.justice.gc.ca/eng/rp-pr/fl-lf/child-enfant/guide/step2-etap2.html) |
| tfsa.room.start_age_18 | When room starts | Year you turn 18 | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html) |
| tfsa.room.newcomers | Newcomers | Room starts the day you become resident; only years of residency count | CRA example: a 2024 arrival had only $7,000. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html) |
| tfsa.room.part_year_resident | Year of arrival or departure | Full annual limit, no proration | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/non-resident.html) |
| tfsa.room.nonresident_years | Non-resident years | No new room | Withdrawals made while non-resident come back only when you are resident again. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/non-resident.html) |
| tfsa.nonresident.contribution_tax | Contributions while non-resident | 1% per month | Applies until withdrawn or residency resumes. A separate 1% applies if room is also exceeded. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/non-resident.html) |
| tfsa.nonresident.withdrawals | Withdrawals while non-resident | Not taxed in Canada | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/non-resident.html) |
| tfsa.room.formula | Room formula | Current limit + unused room + prior-year withdrawals - this year's contributions | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/calculate-room.html) |
| tfsa.withdrawals.added_back | Withdrawals re-added | January 1 of the following year | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/calculate-room.html) |
| tfsa.overcontribution.tax | Over-contribution tax | 1% per month on the highest excess in each month | No grace amount. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/owing-tax/excess.html) |
| tfsa.overcontribution.filing | TFSA Return deadline | June 30 of the following year | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/owing-tax/excess.html) |
| tfsa.multiple_accounts | More than one TFSA | Allowed; one combined room limit | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html) |
| tfsa.investments.qualified | Qualified investments | Cash, GICs, most listed securities (shares, options, ETFs, REITs), mutual and segregated funds, CSBs and provincial savings bonds, listed-corporation and investment-grade debt, insured mortgages | Generally the same as for an RRSP. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/owing-tax/non-permitted-investment.html) |
| tfsa.investments.nonqualified.tax | Non-qualified investment | 50% of FMV | Income is taxable to the trustee; the 100% advantage tax can apply if income is not withdrawn promptly. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/owing-tax/non-permitted-investment.html) |
| tfsa.investments.prohibited.tax | Prohibited investment | 50% of FMV | Example: a 10%+ interest in a company. Income on it attracts the 100% advantage tax. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/owing-tax/non-permitted-investment.html) |
| tfsa.investments.refund | Refund of the 50% tax | If disposed of by the end of the next calendar year | Not available if the holder knew or should have known. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/owing-tax/non-permitted-investment.html) |
| tfsa.advantage.tax | Advantage tax | 100% | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/owing-tax/non-permitted-investment.html) |
| tfsa.business.trading | Frequent trading | May be taxed as business income | CRA: holders trading with the frequency and experience of a professional trader may have the account deregistered and income taxed as a business. CRA gives no numeric test. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/what.html) |
| tfsa.death.successor_holder | Successor holder | Surviving spouse or common-law partner only | Becomes holder immediately; own room unaffected. CRA notes Quebec does not recognize TFSA successor designations. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/death-of-holder/what-happens.html) |
| tfsa.death.designated_beneficiary | Designated beneficiary | Tax-free up to FMV at death | Earnings after death are taxable. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/death-of-holder/beneficiary.html) |
| tfsa.death.exempt_period | Exempt period | Ends Dec 31 of the year after death | After that the trust becomes a taxable inter vivos trust. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account.html) |
| tfsa.death.exempt_contribution | Survivor exempt contribution | By Dec 31 of the year after death; RC240 within 30 days | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/death-of-holder/what-happens.html) |
| tfsa.transfer.direct | Direct transfer between TFSAs | No effect on room | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/transfer.html) |
| tfsa.transfer.withdraw_redeposit | Withdraw and redeposit yourself | Counts as a new contribution | Room comes back only the next year, so an over-contribution is possible. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/transfer.html) |
| tfsa.transfer.breakdown | Separation or divorce transfer | No effect on either person's room | Requires a court order or written separation agreement. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/transfer.html) |

---

## 2. RRSP

### RRSP dollar limits (key `rrsp.limit.YYYY`)

| Year | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 |
|---|---|---|---|---|---|---|---|---|
| Limit (CAD) | 27,230 | 27,830 | 29,210 | 30,780 | 31,560 | 32,490 | 33,810 | **35,390** |

Source: [CRA limits table](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html). The 2027 figure is published; it equals the 2026 money purchase limit.

### RRSP rules

| Key | Fact | Value | Notes | Source |
|---|---|---|---|---|
| rrsp.deduction_limit.rule | Deduction limit | Lesser of 18% of prior-year earned income and the dollar limit, minus PA and PSPA, plus PAR and unused room | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) |
| rrsp.room.carry_forward | Unused room | Carries forward | Undeducted contributions can also be deducted later. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) |
| rrsp.deadline.rule | Deadline rule | 60th day of the following year | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/financial-slips-summaries/rrsp-contribution-receipt-return/contribution-year.html) |
| rrsp.deadline.2025 | Deadline, 2025 tax year | March 2, 2026 | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/important-dates-rrsp-rrif-rdsp.html) |
| rrsp.deadline.2026 | Deadline, 2026 tax year | **Not yet published** | The 60th-day rule gives Monday, March 1, 2027. Publish it only once CRA posts it. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/important-dates-rrsp-rrif-rdsp.html) |
| rrsp.overcontribution.cushion | Over-contribution cushion | $2,000 | Only if you were 18+ at any time in the previous year. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/what-happens-you-over-your-rrsp-prpp-deduction-limit.html) |
| rrsp.overcontribution.tax | Tax on excess | 1% per month | File T1-OVP within 90 days after year-end; waiver on RC2503. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/what-happens-you-over-your-rrsp-prpp-deduction-limit.html) |
| rrsp.age71.last_contribution | Last contribution to own RRSP | Dec 31 of the year you turn 71 | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/rrsp-options-when-you-turn-71.html) |
| rrsp.age71.options | Options at 71 | Withdraw, transfer to a RRIF, or buy an annuity | No withholding on a direct RRIF transfer. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/rrsp-options-when-you-turn-71/options-your-rrsps.html) |
| rrsp.spousal.after_71 | Spousal contributions after 71 | Until the end of the year the spouse turns 71 | | [CRA T4040](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4040/rrsps-other-registered-plans-retirement.html) |
| rrsp.spousal.attribution | Spousal attribution | Contributions in the withdrawal year or either of the 2 prior years | Contributor includes the withdrawal in income (Form T2205). | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/making-withdrawals/withdrawing-spousal-common-law-partner-rrsps.html) |
| rrsp.pension_adjustment | Pension adjustment | Reduces next year's RRSP room | Total pension credits for the year with an employer; never negative. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/about-pension-adjustment.html) |
| rrsp.withholding.nonresident | Non-resident withholding | 25% | Unless a treaty reduces it. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/making-withdrawals/tax-rates-on-withdrawals.html) |

### Withholding on RRSP lump-sum withdrawals

| Amount | Outside Quebec | Quebec (federal part only) |
|---|---|---|
| $5,000 or less | 10% | 5% |
| $5,001 to $15,000 | 20% | 10% |
| Over $15,000 | 30% | 15% |

Source: [CRA tax rates on withdrawals](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/making-withdrawals/tax-rates-on-withdrawals.html). In Quebec, provincial tax is withheld on top. The provincial rate was not verified.

### Home Buyers' Plan

| Key | Fact | Value | Notes | Source |
|---|---|---|---|---|
| hbp.limit | Withdrawal limit | **$60,000** | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan.html) |
| hbp.limit.effective_date | Effective | Withdrawals after April 16, 2024 (Budget Day) | | [Budget 2024](https://budget.canada.ca/2024/report-rapport/tm-mf-en.html) |
| hbp.limit.previous | Previous limit | $35,000 | | [Budget 2024](https://budget.canada.ca/2024/report-rapport/tm-mf-en.html) |
| hbp.eligibility.first_time_buyer | First-time buyer | No owner-occupied home in the current year (ignoring the 30 days before withdrawal) or the prior 4 calendar years | Waived for disability cases and for marriage or partnership breakdown. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/participate-home-buyers-plan.html) |
| hbp.eligibility.conditions | Other conditions | Written agreement to buy or build; occupy within 1 year; resident at withdrawal | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/participate-home-buyers-plan.html) |
| hbp.deadline.acquire | Buy or build by | Before Oct 1 of the year after the first withdrawal | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/participate-home-buyers-plan.html) |
| hbp.withdrawals.timing | Withdrawal window | Calendar year of the first withdrawal plus January of the next year | One T1036 per withdrawal. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/withdraw-funds-rrsp-s-under-home-buyers-plan.html) |
| hbp.contribution_89_days | Recent contributions | 89-day rule | Contributions made in the 89 days before withdrawal may not be deductible. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/withdraw-funds-rrsp-s-under-home-buyers-plan.html) |
| hbp.repayment.period | Repayment period | 15 years | Minimum each year is the balance divided by the years left (1/15 to start). | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/repay-funds-withdrawn-rrsp-s-under-home-buyers-plan.html) |
| hbp.repayment.start.standard | Normal start | 2nd year after the first withdrawal | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/repay-funds-withdrawn-rrsp-s-under-home-buyers-plan.html) |
| hbp.repayment.deferral.2022_2025 | Deferral, first withdrawals 2022 to 2025 | Starts in the 5th year after withdrawal | Example: 2022 withdrawal, first repayment 2027. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan.html) |
| hbp.repayment.deferral.2026_2028 | Deferral extended | First withdrawals Jan 1, 2026 to Dec 31, 2028 also start in the 5th year | Example: 2026 withdrawal, first repayment 2031. CRA's repayment sub-page still shows only 2022 to 2025. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan.html) |
| hbp.repayment.shortfall | Missed repayment | Added to income (line 12900) | Repay in the year due or the first 60 days after. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan/repay-funds-withdrawn-rrsp-s-under-home-buyers-plan.html) |
| hbp.with_fhsa | HBP plus FHSA, same home | Allowed | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/what-home-buyers-plan.html) |

### Lifelong Learning Plan

| Key | Fact | Value | Notes | Source |
|---|---|---|---|---|
| llp.limit.annual | Per calendar year | $10,000 | Form RC96. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/lifelong-learning-plan/participate.html) |
| llp.limit.total | Per participation | $20,000 | Withdrawals allowed until January of the 4th year after the first one. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/lifelong-learning-plan/participate.html) |
| llp.eligibility | Student | You or your spouse or partner | Full-time study (part-time if disabled) at a designated institution; withdrawer must be resident. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/lifelong-learning-plan/who-participate.html) |
| llp.repayment | Repayment | 10 years, at least 1/10 a year | Starts no later than the 5th year after the first withdrawal; a shortfall is added to income. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/lifelong-learning-plan/repayments-your-rrsp-under.html) |

---

## 3. FHSA

| Key | Fact | Value | Notes | Source |
|---|---|---|---|---|
| fhsa.limit.annual | Annual room | **$8,000** | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/contributing-your-fhsa.html) |
| fhsa.limit.lifetime | Lifetime limit | **$40,000** | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/contributing-your-fhsa.html) |
| fhsa.carryforward.max | Carry-forward cap | $8,000 | So the most in one year is $16,000 (calculated from CRA's formula). | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/contributing-your-fhsa.html) |
| fhsa.room.starts_on_opening | When room starts | Only once the first FHSA is opened | Carry-forward is $0 in the opening year. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/contributing-your-fhsa.html) |
| fhsa.eligibility.open | Who can open | Resident, 18+ (19 where that is the legal age), 71 or younger at Dec 31 of the opening year, first-time buyer | More than one FHSA is allowed. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/opening-your-fhsas.html) |
| fhsa.eligibility.first_time_buyer_opening | First-time buyer (opening) | No home owned and lived in by you or your current spouse or partner in the current year before opening or the prior 4 years | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/definitions.html) |
| fhsa.max_participation_period | Maximum participation period | Ends Dec 31 of the year of the earliest of: 15th anniversary, turning 71, or the year after the first qualifying withdrawal | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/definitions.html) |
| fhsa.qualifying_withdrawal.first_time_buyer | First-time buyer (withdrawal) | Same test at withdrawal, ignoring the 30 days before it | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/definitions.html) |
| fhsa.qualifying_withdrawal.conditions | Qualifying withdrawal | Written agreement with completion before Oct 1 of the year after withdrawal; home not acquired >30 days before; occupy within 1 year; resident | Form RC725. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/withdrawals-transfers-out-your-fhsas.html) |
| fhsa.transfer_to_rrsp | Transfer to RRSP or RRIF | Tax-deferred direct transfer; no effect on RRSP room | Requires no excess FHSA amount. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/withdrawals-transfers-out-your-fhsas.html) |
| fhsa.overcontribution.tax | Over-contribution tax | 1% per month on the highest excess | Fix with a designated withdrawal or transfer (RC727). | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/what-happens-contribute-transfer-too-much.html) |
| fhsa.deduction.carryforward | Deduction carry-forward | Allowed, even after closing | RRSP-to-FHSA transfers are not deductible. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/tax-deductions-fhsa-contributions.html) |
| fhsa.deadline | Contribution deadline | **December 31; no 60-day period** | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/tax-deductions-fhsa-contributions.html) |
| fhsa.with_hbp | FHSA plus HBP, same home | Allowed | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/withdrawals-transfers-out-your-fhsas.html) |
| fhsa.no_home | No home bought | Transfer to RRSP or RRIF, or take a taxable withdrawal | Anything left after the period loses FHSA status and its FMV is taxed. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/closing-your-fhsa.html) |

---

## 4. RESP

| Key | Fact | Value | Notes | Source |
|---|---|---|---|---|
| resp.limit.lifetime | Lifetime contribution limit | $50,000 per beneficiary | No annual limit since 2007; not deductible. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/resp-contributions.html) |
| resp.overcontribution.tax | Excess contributions | 1% per month | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/resp-contributions.html) |
| resp.contributions.end | Last contribution year | Year of the plan's 31st anniversary | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/resp-works.html) |
| resp.close.deadline | Plan must close | End of the year of the 35th anniversary (40th for a specified plan) | After an AIP: by the end of February of the next year. | [CRA RC4092](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4092/registered-education-savings-plans-resps.html) |
| resp.family_plan | Family plan | Multiple beneficiaries related by blood or adoption to each living subscriber, under 21 when named | | [CRA RC4092](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4092/registered-education-savings-plans-resps.html) |
| cesg.basic.rate | CESG basic | 20% of the first $2,500 a year | | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/savings-grant.html) |
| cesg.annual.max | Basic annual max | $500 | | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/savings-grant.html) |
| cesg.annual.max_with_carryforward | Max in a year with carry-forward | $1,000 | | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/savings-grant.html) |
| cesg.lifetime.max | Lifetime CESG | $7,200 | | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/estimating-amounts.html) |
| cesg.age_limit | Age limit | End of the year the child turns 17 | | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/savings-grant.html) |
| cesg.age16_17 | Ages 16 and 17 | $2,000+ by the end of the year the child turns 15, OR $100+ in any 4 years before then | Contributions must not have been withdrawn. | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/savings-grant.html) |
| acesg.rate.lower | Additional CESG, income under $58,523 (2026) | +20% on the first $500 (+$100) | Up to $600 a year in total. | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/estimating-amounts.html) |
| acesg.rate.middle | Additional CESG, $58,523 to $117,045 (2026) | +10% on the first $500 (+$50) | Up to $550 a year in total. | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/estimating-amounts.html) |
| acesg.threshold.2026.lower / upper | 2026 thresholds | $58,523 / $117,045 | No additional CESG above $117,045. | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/estimating-amounts.html) |
| acesg.threshold.2025 | 2025 thresholds (CRA page) | $57,375 / $114,750 | CRA's page has not been updated; use the 2026 ESDC figures. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/canada-education-savings-programs-cesp/canada-education-savings-grant-cesg.html) |
| clb.initial / clb.annual / clb.lifetime | Canada Learning Bond | $500 first year, then $100 a year to age 15, $2,000 max | CRA adds $25 for opening costs; no contribution needed. | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/estimating-amounts.html) |
| clb.eligibility | CLB eligibility | Low-income families, born 2004 or later, apply before 21 | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/canada-education-savings-programs-cesp/canada-learning-bond.html) |
| clb.threshold.* | CLB income thresholds (Jul 2026 to Jun 2027) | 1 to 3 children: $58,523 or less; 4: under $66,036; 5: under $73,577 | For 6+ children, call 1-800-622-6232. | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/estimating-amounts.html) |
| clb.automatic_enrolment | CLB auto RESP | From April 2028 | For eligible children born 2024+; opt-out from 2027. | [ESDC](https://www.canada.ca/en/services/benefits/education/education-savings/canada-learning-bond.html) |
| bctesg.amount | BC Training and Education Savings Grant | $1,200 one time | BC resident, born 2006+, no contribution needed. | [Gov. of BC](https://www2.gov.bc.ca/gov/content/education-training/k-12/support/bc-training-and-education-savings-grant) |
| bctesg.window | BCTESG window | From the 6th birthday to the day before the 9th birthday | | [Gov. of BC](https://www2.gov.bc.ca/gov/content/education-training/k-12/support/bc-training-and-education-savings-grant) |
| qesi.basic | QESI basic | 10% of net contributions, up to $250 a year ($500 with unused rights) | | [Revenu Quebec](https://www.revenuquebec.ca/en/citizens/tax-credits/quebec-education-savings-incentive/determining-the-qesi-amount/) |
| qesi.additional | QESI additional | Up to $50 a year, based on family income | Thresholds not verified. | [Revenu Quebec](https://www.revenuquebec.ca/en/citizens/tax-credits/quebec-education-savings-incentive/determining-the-qesi-amount/) |
| qesi.lifetime | QESI lifetime | $3,600 | | [Revenu Quebec](https://www.revenuquebec.ca/en/citizens/tax-credits/quebec-education-savings-incentive/determining-the-qesi-amount/) |
| qesi.eligibility | QESI eligibility | Under 18, SIN, Quebec resident on Dec 31, named beneficiary | | [Revenu Quebec](https://www.revenuquebec.ca/en/citizens/tax-credits/quebec-education-savings-incentive/eligibility-requirements/) |
| resp.provincial.other | Other provincial grants | None besides QESI and BCTESG | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/provincial-education-savings-programs.html) |
| eap.limit.full_time | EAP, first 13 weeks, full-time | $8,000 | Qualifying program: 10+ hours a week. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/payments-resp.html) |
| eap.limit.part_time | EAP, part-time | $4,000 per 13-week period | Specified program: 12+ hours a month. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/payments-resp.html) |
| aip.conditions | AIP conditions | One resident subscriber; plus (after the 9th-anniversary year with all beneficiaries 21+ and not eligible for EAPs) OR (the 35th-anniversary year) OR (all beneficiaries deceased) | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/payments-resp.html) |
| aip.tax | AIP extra tax | 20% (12% in Quebec) | On top of regular income tax. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/payments-resp.html) |
| aip.rrsp_transfer | AIP to RRSP | $50,000 lifetime | Needs RRSP room; Form T1171. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/payments-resp.html) |

---

## 5. RRIF and LIF

### Minimum withdrawal factors (key `rrif.factor.age.NN`)

Ages 55 to 70 are calculated with CRA's formula 1 / (90 - age). Ages 71 and up come from CRA's chart ("All other RRIFs" column), which matches the Budget 2015 table.

| Age | Factor | Age | Factor | Age | Factor |
|---|---|---|---|---|---|
| 55 | 2.86% | 69 | 4.76% | 83 | 7.71% |
| 56 | 2.94% | 70 | 5.00% | 84 | 8.08% |
| 57 | 3.03% | 71 | 5.28% | 85 | 8.51% |
| 58 | 3.13% | 72 | 5.40% | 86 | 8.99% |
| 59 | 3.23% | 73 | 5.53% | 87 | 9.55% |
| 60 | 3.33% | 74 | 5.67% | 88 | 10.21% |
| 61 | 3.45% | 75 | 5.82% | 89 | 10.99% |
| 62 | 3.57% | 76 | 5.98% | 90 | 11.92% |
| 63 | 3.70% | 77 | 6.17% | 91 | 13.06% |
| 64 | 3.85% | 78 | 6.36% | 92 | 14.49% |
| 65 | 4.00% | 79 | 6.58% | 93 | 16.34% |
| 66 | 4.17% | 80 | 6.82% | 94 | 18.79% |
| 67 | 4.35% | 81 | 7.08% | 95+ | 20.00% |
| 68 | 4.55% | 82 | 7.38% | | |

Source: [CRA chart of prescribed factors](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/t4rsp-t4rif-information-returns/payments/chart-prescribed-factors.html). The "Qualifying RRIFs" column shows 5.26% at age 71; all other ages match.

| Key | Fact | Value | Notes | Source |
|---|---|---|---|---|
| rrif.minimum.formula | Minimum amount | FMV at Jan 1 x factor | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/t4rsp-t4rif-information-returns/payments/minimum-amount-a-rrif.html) |
| rrif.minimum.first_year | First minimum due | The year after the RRIF is set up | | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-retirement-income-fund-rrif/receiving-income-a-rrif.html) |
| rrif.minimum.spouse_age | Spouse's age | Can be elected when the RRIF is set up | A younger spouse gives a lower minimum. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/t4rsp-t4rif-information-returns/payments/minimum-amount-a-rrif.html) |
| rrif.withholding.excess | Withholding | Only the part above the minimum is withheld, at lump-sum rates (10/20/30%; Quebec federal part 5/10/15%) | The guide implies but does not say outright that the minimum has no withholding. | [CRA RC4157](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4157/deducting-income-tax-on-pension-other-income-filing-t4a-slip-summary.html) |
| pension.income_amount | Pension income amount | Up to $2,000 (federal) | RRIF income qualifies at 65+, or earlier if received on a spouse's death. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31400-pension-income-amount.html) |
| pension.splitting | Pension splitting | Up to 50% of eligible pension income | Joint T1032; RRIF and LIF payments qualify if the transferor is 65+ at year-end. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/pension-income-splitting.html) |
| lif.minimum.federal | LIF minimum (federal) | Same as the Income Tax Act RRIF minimum | | [PBSR s. 20.1](https://laws-lois.justice.gc.ca/eng/regulations/SOR-87-19/FullText.html) |
| lif.maximum.federal | LIF maximum (federal) | Formula cap before 90; no cap from the year the holder turns 90 | | [PBSR s. 20.1](https://laws-lois.justice.gc.ca/eng/regulations/SOR-87-19/FullText.html) |

---

## 6. Deposit and investor protection

| Key | Fact | Value | Notes | Source |
|---|---|---|---|---|
| cdic.limit | CDIC limit | $100,000 per category per member institution | Includes principal and interest. | [CDIC](https://www.cdic.ca/your-coverage/) |
| cdic.category.* | Separate CDIC categories | One name; joint; in trust; RRSP; RRIF; TFSA; RESP; RDSP; FHSA | Each is insured separately up to $100,000. | [CDIC](https://www.cdic.ca/your-coverage/) |
| cdic.eligible | Covered vs not | Covers deposits (CAD or foreign currency), GICs and term deposits. Not covered: mutual funds, stocks, bonds, ETFs, crypto | Provincial credit unions use provincial insurance plans ([FCAC](https://www.canada.ca/en/financial-consumer-agency/services/banking/deposit-insurance.html)). | [CDIC](https://www.cdic.ca/your-coverage/) |
| cipf.limit.general | CIPF general accounts | $1,000,000 combined | Includes cash, margin, TFSA and FHSA accounts. | [CIPF](https://www.cipf.ca/cipf-coverage/about-cipf-coverage) |
| cipf.limit.retirement | CIPF retirement accounts | $1,000,000 combined | RRSP, RRIF, LIF. | [CIPF](https://www.cipf.ca/cipf-coverage/about-cipf-coverage) |
| cipf.limit.resp | CIPF RESPs | $1,000,000 combined | Where the client is the subscriber. | [CIPF](https://www.cipf.ca/cipf-coverage/about-cipf-coverage) |
| cipf.scope | CIPF scope | Property missing when a member firm fails; not market losses | Crypto excluded. | [CIPF](https://www.cipf.ca/cipf-coverage/about-cipf-coverage) |
| ciro.role | Regulator | CIRO oversees all investment dealers and mutual fund dealers | CIPF members are CIRO members. | [CIRO](https://www.ciro.ca/) |

---

## 7. US investing from Canada

| Key | Fact | Value | Notes | Source |
|---|---|---|---|---|
| us.dividends.treaty_rate | Treaty rate on US dividends | 15% | Article X(2)(b); 5% only for a company owning 10%+ of the voting stock. | [Canada-US Convention](https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties/country/united-states-america-convention-consolidated-1980-1983-1984-1995-1997-2007.html) |
| us.dividends.statutory_rate | Without treaty documentation | 30% | | [IRS](https://www.irs.gov/individuals/international-taxpayers/nra-withholding) |
| us.w8ben | W-8BEN | Given to the payer by a foreign beneficial owner | Used to claim the reduced rate. | [IRS](https://www.irs.gov/forms-pubs/about-form-w-8-ben) |
| us.exemption.treaty_text | Retirement exemption | Article XXI(2) exempts dividends and interest of arrangements operated exclusively for pension, retirement or employee benefits | | [Canada-US Convention](https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties/country/united-states-america-convention-consolidated-1980-1983-1984-1995-1997-2007.html) |
| us.exempt_accounts.rrsp_rrif | Exempt accounts | RRSP, RRIF, LIRA, LIF | **Unverified:** the treaty text does not name these accounts. | Treaty (as above) |
| us.not_exempt.tfsa_resp_fhsa | Not exempt | TFSA, RESP, FHSA, non-registered | **Unverified:** no official page says this in words. | Treaty (as above) |
| us.ftc.non_registered | Foreign tax credit | Lesser of foreign tax paid and Canadian tax on that income | Form T2209 (line 40500); T2036 for the provincial part outside Quebec. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-40500-federal-foreign-tax-credit.html) |

---

## Not yet published (as of 2026-10-22)

1. **TFSA 2027 dollar limit** (`tfsa.limit.2027`): CRA has not published it. Do not use estimates such as $7,500.
2. **RRSP deadline for the 2026 tax year** (`rrsp.deadline.2026`): CRA has not posted it. The 60th-day rule gives Monday, March 1, 2027.

## Could not verify on an official page

1. `rrsp.spousal.attribution_exceptions`: the exceptions to spousal RRSP attribution were not listed on the CRA page fetched.
2. `rrsp.withholding.qc_provincial`: the Quebec provincial withholding rate on RRSP lump sums (Revenu Quebec page not reached).
3. `resp.individual_plan`: the statement that an individual plan can name anyone of any age, including the subscriber.
4. `qesi.additional.thresholds`: the family income thresholds for the QESI additional $50.
5. `lif.provincial`: provincial LIF maximums and unlocking rules (Ontario e-Laws page would not load).
6. `us.exempt_accounts.rrsp_rrif`: that RRSPs, RRIFs, LIRAs and LIFs are the accounts covered by treaty Article XXI(2). This is standard practice, but no fetched official page names them.
7. `us.not_exempt.tfsa_resp_fhsa`: that TFSA, RESP and FHSA dividends are not exempt from US withholding. No official page says this in words.
8. `us.ftc.15pct_property_cap`: the 15% cap on creditable foreign tax on investment income (s. 20(11)); the CRA folio would not load.

## Source caveats for writers

- CRA's TFSA guides RC4466 (individuals) and RC4477 (issuers) are both marked **CANCELLED**. Cite the current canada.ca TFSA web pages, as this register does.
- CRA's HBP repayment sub-page has not yet been updated for the 2026 to 2028 deferral extension. The main HBP page (modified 2026-02-17) has it.
- CRA's CESG page still shows 2025 income thresholds. ESDC's estimating page has the 2026 figures.
- Web search capacity ran out late in the session. All remaining items were checked by opening official pages directly; nothing in this register relies on memory.
