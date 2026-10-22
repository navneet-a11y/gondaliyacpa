# Verified tax and benefits register, 2026

Checked on 2026-10-22. Each figure comes from an official page opened during this research (canada.ca, CRA, Service Canada/ESDC, Finance Canada, provincial finance ministries, Revenu Quebec, Finances Quebec). The machine-readable register is `facts-tax-benefits.json` (one row per fact, with source URL and status), and the calculator file is `tax-tables-2026.json`.

Status values: **verified** (read on an official page), **not yet published**, **unverified** (no official page confirming it was opened; do not publish).

## Read this first: open issues

1. **Provincial dividend tax credit rates for AB, SK, MB, NB, NS, PE, NL, YT, NT and NU are unverified.** Official 2026 rates were found only for Ontario, B.C. and Quebec. The CRA 428 form files are blocked to automated reading, and the provincial finance pages checked do not list the rates. The web-search quota ran out before other official pages could be found. These are left blank (`null` in the calculator file).
2. **Manitoba bracket thresholds: two CRA sources disagree.** T4127 (Jan and July 2026) and T4032MB say Manitoba thresholds and BPA are not indexed ($47,000 / $100,000; BPA $15,780). The CRA 2026 rates page (modified 2026-06-25) shows $47,564 / $101,200. The register uses the T4127 values and flags the thresholds as unverified. Confirm against the 2026 MB428 form when it is released.
3. **Capital gains inclusion rate for 2026:** CRA confirms 1/2 for 2001 to 2025, and no CRA page shows a 2/3 rate. The March 21, 2025 cancellation announcement could not be opened (fetches of pm.gc.ca and Finance Canada failed). The 2026 rate (1/2) and the cancellation are therefore marked unverified.
4. **Royal Assent of the federal 14% rate (Bill C-4)** was not confirmed. CRA nonetheless publishes 14% as the 2026 rate.
5. **CGEB (formerly the GST/HST credit) reduction rate:** the income threshold ($46,432) is verified. The phase-out percentage is not stated on any page opened.
6. **Not yet published:** 2027 payment dates for CPP/OAS/GIS, CCB, OTB, Canada Disability Benefit and the ACWB. The two 2027 CGEB dates come from the RC4210 rule ('5th day of January and April 2027'), not from the payment-dates page.

## 1. Federal income tax 2026

| Taxable income | Rate |
|---|---|
| $0 to $58,523 | 14% |
| $58,523 to $117,045 | 20.5% |
| $117,045 to $181,440 | 26% |
| $181,440 to $258,482 | 29% |
| over $258,482 | 33% |

- BPA: $16,452 max (net income up to $181,440), phasing down to $14,829 at $258,482 or more ([CRA indexation](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html)).
- Lowest rate: cut from 15% to 14% on July 1, 2025, so the 2025 rate is a blended 14.5%. The full-year 2026 rate is 14% ([CRA 2025 rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html); [Budget 2025 TM](https://budget.canada.ca/2025/report-rapport/tm-mf-en.html)).
- 2026 indexation factor: 2.0%. Refundable Quebec abatement: 16.5% of basic federal tax ([T4127](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html)).

Source for brackets: [CRA 2026 rates and brackets](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html).

## 2. Provincial and territorial income tax 2026

### Alberta

| Taxable income | Rate |
|---|---|
| $0 to $61,200 | 8% |
| $61,200 to $154,259 | 10% |
| $154,259 to $185,111 | 12% |
| $185,111 to $246,813 | 13% |
| $246,813 to $370,220 | 14% |
| over $370,220 | 15% |

- Basic personal amount: $22,769. T4127 July 2026 Table 8.2. alberta.ca: thresholds and credit amounts rise 2% in 2026. Alberta supplemental credit (payroll K5P): 25% of (K1P + K2P - $4,896). ([source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html))
- Notes: Same thresholds and rates on alberta.ca (2026 table). 8% bracket introduced January 1, 2025. ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))

### British Columbia

| Taxable income | Rate |
|---|---|
| $0 to $50,363 | 5.6% |
| $50,363 to $100,728 | 7.7% |
| $100,728 to $115,648 | 10.5% |
| $115,648 to $140,430 | 12.29% |
| $140,430 to $190,405 | 14.7% |
| $190,405 to $265,545 | 16.8% |
| over $265,545 | 20.5% |

- Basic personal amount: $13,216. Also in T4127 July 2026. BC tax reduction 2026: base $690, net income threshold $25,570, reduction 3.56%, eliminated at $44,952. ([source](https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic))
- Notes: gov.bc.ca confirms: lowest rate rose from 5.06% (2025) to 5.60% (2026); brackets indexed 2.2%. Payroll only: T4127 July 2026 uses a prorated 6.14% first-bracket rate for July-December 2026. ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))

### Manitoba

| Taxable income | Rate |
|---|---|
| $0 to $47,000 | 10.8% |
| $47,000 to $100,000 | 12.75% |
| over $100,000 | 17.4% |

- Basic personal amount: $15,780. 'The maximum BPAMB for 2026 will remain at $15,780' (not indexed). Phased out over net income $200,000 to $400,000 effective 2025 (gov.mb.ca). ([source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html))
- Notes: CONFLICT: CRA 2026 rates page (modified 2026-06-25) shows thresholds $47,564 and $101,200. CRA T4127 (Jan and July 2026) and T4032MB state Manitoba thresholds and BPA 'will not be indexed' (from 2025) and use $47,000/$100,000. T4127/T4032MB values used here; confirm against 2026 MB428 when released. ([source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html))

### New Brunswick

| Taxable income | Rate |
|---|---|
| $0 to $52,333 | 9.4% |
| $52,333 to $104,666 | 14% |
| $104,666 to $193,861 | 16% |
| over $193,861 | 19.5% |

- Basic personal amount: $13,664. T4127 July 2026 Table 8.2 basic amount. ([source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html))
- Notes: Matches T4127 Jan 2026 table. ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))

### Newfoundland and Labrador

| Taxable income | Rate |
|---|---|
| $0 to $44,678 | 8.7% |
| $44,678 to $89,354 | 14.5% |
| $89,354 to $159,528 | 15.8% |
| $159,528 to $223,340 | 17.8% |
| $223,340 to $285,319 | 19.8% |
| $285,319 to $570,638 | 20.8% |
| $570,638 to $1,141,275 | 21.3% |
| over $1,141,275 | 21.8% |

- Basic personal amount: $13,094. NL announced BPA increase from $11,188 to $13,094 effective January 1, 2026. Payroll uses a prorated $15,000 from July 2026 (payroll proration only, not the annual credit). ([source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html))
- Notes: Matches T4127 July 2026 Table 8.1. ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))

### Nova Scotia

| Taxable income | Rate |
|---|---|
| $0 to $30,995 | 8.79% |
| $30,995 to $61,991 | 14.95% |
| $61,991 to $97,417 | 16.67% |
| $97,417 to $157,124 | 17.5% |
| over $157,124 | 21% |

- Basic personal amount: $11,932. Also T4127 July Table 8.2. NS BPA now set at the maximum regardless of income (T4127 Jan 2026). ([source](https://www.novascotia.ca/personal-income-tax-rates-and-indexation))
- Notes: Same on novascotia.ca; NS system indexed 1.6% for 2026 (OIC 2025-274). ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))

### Northwest Territories

| Taxable income | Rate |
|---|---|
| $0 to $53,003 | 5.9% |
| $53,003 to $106,009 | 8.6% |
| $106,009 to $172,346 | 12.2% |
| over $172,346 | 14.05% |

- Basic personal amount: $18,198. T4127 July 2026 Table 8.2 basic amount. ([source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html))
- Notes: GNWT: brackets and credits indexed annually using the federal index factor. ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))

### Nunavut

| Taxable income | Rate |
|---|---|
| $0 to $55,801 | 4% |
| $55,801 to $111,602 | 7% |
| $111,602 to $181,439 | 9% |
| over $181,439 | 11.5% |

- Basic personal amount: $19,659. T4127 July 2026 Table 8.2 basic amount. ([source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html))
- Notes: Matches T4127 Jan 2026 table. ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))

### Ontario

| Taxable income | Rate |
|---|---|
| $0 to $53,891 | 5.05% |
| $53,891 to $107,785 | 9.15% |
| $107,785 to $150,000 | 11.16% |
| $150,000 to $220,000 | 12.16% |
| over $220,000 | 13.16% |

- Basic personal amount: $12,989. T4127 July 2026 Table 8.2 basic amount. Ontario tax reduction basic amount (S2) $300. ([source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html))
- Notes: Matches T4127 Jan 2026 table. Ontario surtax and Ontario Health Premium apply in addition (see separate keys). ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))
- Ontario surtax 2026: 20% of basic Ontario tax over $5,818, plus 36% of basic Ontario tax over $7,446 ([T4127](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html)).
- Ontario Health Premium (taxable income): up to $20,000: $0; $20,000 to $36,000: lesser of $300 and 6% over $20,000; $36,000 to $48,000: lesser of $450 and $300 + 6% over $36,000; $48,000 to $72,000: lesser of $600 and $450 + 25% over $48,000; $72,000 to $200,000: lesser of $750 and $600 + 25% over $72,000; over $200,000: lesser of $900 and $750 + 25% over $200,000.

### Prince Edward Island

| Taxable income | Rate |
|---|---|
| $0 to $33,928 | 9.5% |
| $33,928 to $65,820 | 13.47% |
| $65,820 to $106,890 | 16.6% |
| $106,890 to $142,520 | 17.62% |
| $142,520 to $200,000 | 19% |
| over $200,000 | 20% |

- Basic personal amount: $15,000. Raised from $14,650 to $15,000 effective January 1, 2026; T4127: 'No indexing applies to Prince Edward Island.' ([source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html))
- Notes: New 20% bracket over $200,000 from 2026 (T4127 July 2026; payroll uses prorated 21% for July-December 2026). ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))

### Quebec

| Taxable income | Rate |
|---|---|
| $0 to $54,345 | 14% |
| $54,345 to $108,680 | 19% |
| $108,680 to $132,245 | 24% |
| over $132,245 | 25.75% |

- Basic personal amount: $18,952. Finances Quebec indexation document: $18,571 (2025) to $18,952 (2026). ([source](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/))
- Notes: Rates unchanged; thresholds indexed 2.05% for 2026 (Revenu Quebec Principal changes for 2026; Finances Quebec indexation document). ([source](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/income-tax-rates/))

### Saskatchewan

| Taxable income | Rate |
|---|---|
| $0 to $54,532 | 10.5% |
| $54,532 to $155,805 | 12.5% |
| over $155,805 | 14.5% |

- Basic personal amount: $20,381. Up from $19,491 (2025); indexed 2% plus an extra $500 per year for 2025-2028 (Saskatchewan Affordability Act). ([source](https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure))
- Notes: saskatchewan.ca 2026 structure: 10.5% on first $54,532, 12.5% on next $101,273, 14.5% on remainder; indexed 2.0%. ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))

### Yukon

| Taxable income | Rate |
|---|---|
| $0 to $58,523 | 6.4% |
| $58,523 to $117,045 | 9% |
| $117,045 to $181,440 | 10.9% |
| $181,440 to $500,000 | 12.8% |
| over $500,000 | 15% |

- Basic personal amount: $16,452. BPAYT = BPAF (mirrors federal): $16,452 max, phasing to $14,829 between net income $181,440 and $258,482. ([source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html))
- Notes: Matches T4127 Jan 2026 table. ([source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html))

**Other provincial surtax:** the 2026 CRA payroll formulas include a provincial surtax only for Ontario. No PEI surtax appears in the 2026 PEI parameters.

**Changes or non-indexation for 2026:** Manitoba is not indexed (brackets and BPA frozen; BPA phased out between $200,000 and $400,000 of net income). B.C. raised its lowest rate from 5.06% to 5.60% and indexed brackets by 2.2%. PEI added a 20% bracket over $200,000 and set its BPA at $15,000 (T4127: not indexed). NL raised its BPA to $13,094 from January 1, 2026. Saskatchewan indexed by 2.0% and adds $500 a year to the BPA for 2025 to 2028. Nova Scotia indexed by 1.6%, Quebec by 2.05% (rates unchanged), and Alberta by 2%. NWT indexes with the federal factor.

## 3. Dividends

| Item | Value | Unit | Status | Source |
|---|---|---|---|---|
| Eligible dividend gross-up | 38 | percent | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/trust-administrators/t3-slip/complete-t3-slip.html) |
| Non-eligible (other than eligible) dividend gross-up | 15 | percent | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/trust-administrators/t3-slip/complete-t3-slip.html) |
| Federal dividend tax credit, eligible | 15.0198 | percent of grossed-up (taxable) amount | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/trust-administrators/t3-slip/complete-t3-slip.html) |
| Federal dividend tax credit, non-eligible | 9.0301 | percent of grossed-up (taxable) amount | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/trust-administrators/t3-slip/complete-t3-slip.html) |
| Ontario DTC, eligible (2026) | 10.0 | percent of grossed-up amount | verified | [link](https://www.ontario.ca/page/ontario-dividend-tax-credit) |
| Ontario DTC, non-eligible (2026) | 2.9863 | percent of grossed-up amount | verified | [link](https://www.ontario.ca/page/ontario-dividend-tax-credit) |
| Ontario DTC, non-eligible (2027) | 1.9863 | percent of grossed-up amount | verified | [link](https://www.ontario.ca/page/ontario-dividend-tax-credit) |
| BC DTC, eligible (2026) | 12 | percent of taxable dividends | verified | [link](https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic) |
| BC DTC, non-eligible (2026) | 1.96 | percent of taxable dividends | verified | [link](https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic) |
| Quebec DTC, eligible | 11.70 | percent of grossed-up amount | verified | [link](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/how-to-complete-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-415/) |
| Quebec DTC, ordinary (non-eligible) | 3.42 | percent of grossed-up amount | verified | [link](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/how-to-complete-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-415/) |
| Alberta DTC, eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Alberta DTC, non-eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Saskatchewan DTC, eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Saskatchewan DTC, non-eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Manitoba DTC, eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Manitoba DTC, non-eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| New Brunswick DTC, eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| New Brunswick DTC, non-eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Nova Scotia DTC, eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Nova Scotia DTC, non-eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Prince Edward Island DTC, eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Prince Edward Island DTC, non-eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Newfoundland and Labrador DTC, eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Newfoundland and Labrador DTC, non-eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Yukon DTC, eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Yukon DTC, non-eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Northwest Territories DTC, eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Northwest Territories DTC, non-eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Nunavut DTC, eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |
| Nunavut DTC, non-eligible (2026) | (blank) | percent of grossed-up amount | unverified | - |

## 4. Capital gains

| Item | Value | Unit | Status | Source |
|---|---|---|---|---|
| Capital gains inclusion rate, 2001-2025 | 1/2 (50%) | fraction | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| Capital gains inclusion rate for 2026 | 1/2 (50%) | fraction | unverified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| Status of the proposed 2/3 inclusion-rate increase | Cancelled (announced March 21, 2025) | text | unverified | - |
| Lifetime capital gains exemption (proposed) | 1250000 | CAD | verified | [link](https://budget.canada.ca/2025/report-rapport/tm-mf-en.html) |
| Superficial loss rule | Loss denied if you or an affiliated person acquire identical property within 30 calendar days before or after the sale and still hold it 30 days after | text | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| Net capital loss carry-back period | 3 | years | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |
| Net capital loss carry-forward period | indefinitely | text | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html) |

## 5. CPP, OAS and GIS

CPP, OAS and GIS share one payment date each month. 2026 dates: Jan 28, Feb 25, Mar 27, Apr 28, May 27, Jun 26, Jul 29, Aug 27, Sep 25, Oct 28, Nov 26, Dec 22. The 2027 dates are not yet published ([source](https://www.canada.ca/en/services/benefits/calendar.html)).

| Item | Value | Unit | Status | Source |
|---|---|---|---|---|
| CPP maximum monthly retirement pension at 65 (starting 2026) | 1507.65 | CAD per month | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/cpp/cpp-benefit/amount.html) |
| CPP average monthly retirement pension at 65 (July 2026) | 858.34 | CAD per month | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/cpp/cpp-benefit/amount.html) |
| CPP early start reduction | 0.6% per month before 65 (7.2%/yr), max 36% at 60 | text | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/cpp/when-start.html) |
| CPP deferral increase | 0.7% per month after 65 (8.4%/yr), max 42% at 70 | text | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/cpp/when-start.html) |
| CPP YMPE 2026 | 74600 | CAD | verified | [link](https://www.canada.ca/en/employment-social-development/programs/pensions/pension/statistics/2026-quarterly-october-december.html) |
| CPP YAMPE 2026 | 85000 | CAD | verified | [link](https://www.canada.ca/en/employment-social-development/programs/pensions/pension/statistics/2026-quarterly-october-december.html) |
| OAS maximum monthly, age 65-74 (Oct-Dec 2026) | 762.50 | CAD per month | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/old-age-security/payments.html) |
| OAS maximum monthly, age 75+ (Oct-Dec 2026) | 838.75 | CAD per month | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/old-age-security/payments.html) |
| OAS recovery tax (clawback) threshold, 2026 income year | 95323 | CAD net world income | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/old-age-security/recovery-tax.html) |
| OAS recovery threshold, 2025 income year | 93454 | CAD net world income | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/old-age-security/recovery-tax.html) |
| OAS recovery tax rate | 15 | percent of net income above threshold | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/old-age-security/recovery-tax.html) |
| OAS fully recovered at (age 65-74, 2026 income year) | 155320 | CAD | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/old-age-security/recovery-tax.html) |
| OAS fully recovered at (age 75+, 2026 income year) | 161320 | CAD | verified | [link](https://www.canada.ca/en/services/benefits/publicpensions/old-age-security/recovery-tax.html) |
| OAS deferral increase | 0.6% per month delayed, up to 36% at age 70 | text | verified | [link](https://www.canada.ca/en/employment-social-development/programs/pensions/pension/statistics/2026-quarterly-october-december.html) |
| GIS max, single/widowed/divorced (Oct-Dec 2026) | 1138.90 | CAD per month | verified | [link](https://www.canada.ca/en/employment-social-development/programs/pensions/pension/statistics/2026-quarterly-october-december.html) |
| GIS max, spouse/partner does not receive OAS or Allowance (Oct-Dec 2026) | 1138.90 | CAD per month | verified | [link](https://www.canada.ca/en/employment-social-development/programs/pensions/pension/statistics/2026-quarterly-october-december.html) |
| GIS max, spouse/partner receives full OAS (Oct-Dec 2026) | 685.56 | CAD per month | verified | [link](https://www.canada.ca/en/employment-social-development/programs/pensions/pension/statistics/2026-quarterly-october-december.html) |
| GIS max, spouse/partner receives the Allowance (Oct-Dec 2026) | 685.56 | CAD per month | verified | [link](https://www.canada.ca/en/employment-social-development/programs/pensions/pension/statistics/2026-quarterly-october-december.html) |
| Allowance max (60-64), Oct-Dec 2026 | 1448.06 | CAD per month | verified | [link](https://www.canada.ca/en/employment-social-development/programs/pensions/pension/statistics/2026-quarterly-october-december.html) |
| Allowance for the Survivor max (60-64), Oct-Dec 2026 | 1726.18 | CAD per month | verified | [link](https://www.canada.ca/en/employment-social-development/programs/pensions/pension/statistics/2026-quarterly-october-december.html) |

## 6. GST/HST credit, now the Canada Groceries and Essentials Benefit (CGEB)

Timeline: **announced** 2026-01-26 (Finance Canada backgrounder). **Enacted** by Bill C-19, the *Canada Groceries and Essentials Benefit Act*, with Royal Assent on 2026-02-12. The **one-time top-up** (50% of the 2025-26 annual GST credit value) was scheduled for 2026-06-05. The **GST/HST credit was replaced** by the CGEB from the July 3, 2026 payment, with a 25% increase for five years (2026 to 2031).

| Item | Value | Unit | Status | Source |
|---|---|---|---|---|
| CGEB announced | 2026-01-26 | date | verified | [link](https://www.canada.ca/en/department-finance/news/2026/01/the-new-canada-groceries-and-essentials-benefit.html) |
| CGEB enacted (Bill C-19, Canada Groceries and Essentials Benefit Act) | Royal Assent 2026-02-12 | date | verified | [link](https://www.canada.ca/en/department-finance/news/2026/02/legislation-passes-to-deliver-new-canada-groceries-and-essentials-benefit.html) |
| GST/HST credit replaced by CGEB | July 2026 (first CGEB payment July 3, 2026) | text | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-groceries-essentials-benefit.html) |
| CGEB one-time top-up payment date | 2026-06-05 | date | verified | [link](https://www.canada.ca/en/revenue-agency/news/2026/04/canada-groceries-and-essentials-benefit-one-time-top-up-payment-to-make-groceries-and-other-essentials-more-affordable-is-coming-june-5.html) |
| CGEB one-time top-up size | 50% of the 2025-26 annual GST credit value | text | verified | [link](https://www.canada.ca/en/department-finance/news/2026/02/legislation-passes-to-deliver-new-canada-groceries-and-essentials-benefit.html) |
| CGEB ongoing increase | 25% for five years starting July 2026 (2026 to 2031) | text | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-groceries-essentials-benefit.html) |
| CGEB max, single (Jul 2026-Jun 2027) | 679 | CAD per year | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-groceries-essentials-benefit/how-much.html) |
| CGEB max, married or common-law (Jul 2026-Jun 2027) | 890 | CAD per year | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-groceries-essentials-benefit/how-much.html) |
| CGEB max per child under 19 (Jul 2026-Jun 2027) | 234 | CAD per year | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-groceries-essentials-benefit/how-much.html) |
| CGEB adult maximum | 445 | CAD per year | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| CGEB single supplement | 234 | CAD per year | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| CGEB single supplement phase-in threshold | 11564 | CAD | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| CGEB family net income where reduction starts | 46432 | CAD adjusted family net income | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| CGEB reduction rate | (blank) | percent | unverified | - |
| GST/HST credit payment date 2026-01-05 | 2026-01-05 | date | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/benefit-payment-dates.html) |
| GST/HST credit payment date 2026-04-02 | 2026-04-02 | date | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/benefit-payment-dates.html) |
| CGEB payment date 2026-07-03 | 2026-07-03 | date | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/benefit-payment-dates.html) |
| CGEB payment date 2026-10-05 | 2026-10-05 | date | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/benefit-payment-dates.html) |
| CGEB payment date January 2027 | 2027-01-05 | date | verified | [link](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4210/canada-groceries-essentials-benefit.html) |
| CGEB payment date April 2027 | 2027-04-05 | date | verified | [link](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4210/canada-groceries-essentials-benefit.html) |

## 7. Canada Child Benefit

2026 payment dates: Jan 20, Feb 20, Mar 20, Apr 20, May 20, Jun 19, Jul 20, Aug 20, Sep 18, Oct 20, Nov 20, Dec 11. The 2027 dates are not yet published.

| Item | Value | Unit | Status | Source |
|---|---|---|---|---|
| CCB payment dates 2027 | not yet published | date | not yet published | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/benefit-payment-dates.html) |
| CCB max per child under 6 (Jul 2026-Jun 2027) | 8157 | CAD per year | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit-overview/canada-child-benefit-we-calculate-your-ccb.html) |
| CCB max per child 6-17 (Jul 2026-Jun 2027) | 6883 | CAD per year | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit-overview/canada-child-benefit-we-calculate-your-ccb.html) |
| CCB first reduction threshold (AFNI) | 38237 | CAD | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit-overview/canada-child-benefit-we-calculate-your-ccb.html) |
| CCB second reduction threshold (AFNI) | 82847 | CAD | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit-overview/canada-child-benefit-we-calculate-your-ccb.html) |
| Child disability benefit max (Jul 2026-Jun 2027) | 3480 | CAD per year | verified | [link](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit-overview/canada-child-benefit-we-calculate-your-ccb.html) |

## 8. Ontario Trillium Benefit, Canada Disability Benefit, Canada Workers Benefit

- OTB 2026: Jan 9, Feb 10, Mar 10, Apr 10, May 8, Jun 10, Jul 10, Aug 10, Sep 10, Oct 9, Nov 10, Dec 10. 2027 dates are not yet published ([CRA](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/benefit-payment-dates.html)).
- Canada Disability Benefit 2026: Jan 15, Feb 19, Mar 19, Apr 16, May 21, Jun 18, Jul 16, Aug 20, Sep 17, Oct 15, Nov 19, Dec 17. 2027 dates are not yet published ([calendar](https://www.canada.ca/en/services/benefits/calendar.html)).
- Advanced Canada workers benefit 2026: Jan 12, Jul 10, Oct 9. 2027 dates are not yet published.

| Item | Value | Unit | Status | Source |
|---|---|---|---|---|
| Canada Disability Benefit max (Jul 2026-Jun 2027) | 204.20 | CAD per month | verified | [link](https://www.canada.ca/en/services/benefits/disability/canada-disability-benefit/amount.html) |
| Canada Disability Benefit income thresholds | Single $23,000; couple $32,500 | CAD adjusted family net income | verified | [link](https://www.canada.ca/en/services/benefits/disability/canada-disability-benefit/amount.html) |
| CWB max 2026, single no children | 1665 | CAD | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| CWB max 2026, families | 2869 | CAD | verified | [link](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |

## 9. Withholding on RRSP and RRIF withdrawals

| Amount withdrawn | Outside Quebec | Quebec residents (federal) | Quebec provincial |
|---|---|---|---|
| Up to $5,000 | 10% | 5% | 14% |
| $5,000.01 to $15,000 | 20% | 10% | 14% |
| Over $15,000 | 30% | 15% | 14% |

The RRIF minimum amount has no withholding, federal or Quebec. Amounts withdrawn above the minimum are withheld at the lump-sum rates. Quebec VRSP/PRPP single payments: 14% up to $5,000, 19% above. Sources: [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/making-withdrawals/tax-rates-on-withdrawals.html), [RC4157](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4157/deducting-income-tax-on-pension-other-income-filing-t4a-slip-summary.html), [T4079](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4079/t4rsp-t4rif-guide.html), [Revenu Quebec](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/special-cases-source-deductions-and-employer-contributions/payments-from-an-rrsp-a-vrsp-a-prpp-or-a-rrif/).

## Sources opened

- [CRA - Personal income tax: 2026 tax rates and income brackets (modified 2026-06-25)](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html)
- [CRA - 2025 tax rates and income brackets (modified 2026-06-25)](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html)
- [CRA - Indexation adjustment for personal income tax and benefit amounts (modified 2026-03-12)](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html)
- [CRA T4127 Payroll Deductions Formulas, 122nd edition, effective January 1, 2026](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html)
- [CRA T4127 Payroll Deductions Formulas, 123rd edition, effective July 1, 2026 (last update 2026-06-03)](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html)
- [CRA T4032MB Payroll Deductions Tables - Manitoba, January 2026 general information (modified 2025-12-17)](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032mb-jan/t4032mb-january-general-information.html)
- [Manitoba Finance - Personal tax credits](https://www.gov.mb.ca/finance/personal/pcredits.html)
- [Government of B.C. - Personal income tax rates (last updated 2026-04-17)](https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/tax-rates)
- [Government of B.C. - Basic personal income tax credits (last updated 2026-04-20)](https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/basic)
- [Government of Alberta - Personal income tax (published 2026-03-04)](https://www.alberta.ca/personal-income-tax)
- [Government of Saskatchewan - 2026 Personal Income Tax Structure](https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure)
- [Government of Saskatchewan - Personal income tax](https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax)
- [Government of Nova Scotia - Personal income tax rates and indexation (modified 2026-01-02)](https://www.novascotia.ca/personal-income-tax-rates-and-indexation)
- [GNWT Finance - Personal income tax](https://www.fin.gov.nt.ca/en/services/personal-income-tax)
- [Revenu Quebec - Income tax rates](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/income-tax-rates/)
- [Revenu Quebec - Principal changes for 2026 (employers) (updated 2026-04-16)](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/)
- [Finances Quebec - Indexation of the personal income tax system for 2026](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/finances/publications-adm/parametres/AUTEN_IncomeTax2026.pdf)
- [Revenu Quebec - Line 415 Dividend tax credit](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/how-to-complete-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-415/)
- [Revenu Quebec - Line 128 Taxable amount of dividends](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/how-to-complete-your-income-tax-return/line-by-line-help/96-to-164-total-income/line-128/)
- [Revenu Quebec - Payments from an RRSP, a VRSP, a PRPP or a RRIF (source deductions)](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/special-cases-source-deductions-and-employer-contributions/payments-from-an-rrsp-a-vrsp-a-prpp-or-a-rrif/)
- [Government of Ontario - Ontario dividend tax credit (updated 2026-04-27)](https://www.ontario.ca/page/ontario-dividend-tax-credit)
- [CRA - How to fill out the T3 slip (dividend boxes) (modified 2026-05-12)](https://www.canada.ca/en/revenue-agency/services/tax/trust-administrators/t3-slip/complete-t3-slip.html)
- [CRA - Capital losses and deductions (modified 2026-02-05)](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html)
- [CRA - Line 25300 Net capital losses of other years (modified 2026-02-05)](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25300-net-capital-losses-other-years.html)
- [CRA T4037 Capital Gains - 2025 (modified 2026-02-11)](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)
- [Budget 2025 - Tax Measures: Supplementary Information (Finance Canada)](https://budget.canada.ca/2025/report-rapport/tm-mf-en.html)
- [Government of Canada - Benefits payment dates (modified 2026-08-07)](https://www.canada.ca/en/services/benefits/calendar.html)
- [CRA - Benefit payment dates (modified 2026-10-14)](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/benefit-payment-dates.html)
- [Service Canada - CPP retirement pension: How much you could receive (modified 2026-10-13)](https://www.canada.ca/en/services/benefits/publicpensions/cpp/cpp-benefit/amount.html)
- [Service Canada - CPP retirement pension: When to start (modified 2026-10-02)](https://www.canada.ca/en/services/benefits/publicpensions/cpp/when-start.html)
- [Service Canada - Old Age Security payment amounts, October to December 2026 (modified 2026-09-29)](https://www.canada.ca/en/services/benefits/publicpensions/old-age-security/payments.html)
- [ESDC - Maximum Benefit Amounts and Related Figures, CPP (2026) and OAS (October to December 2026) (modified 2026-09-29)](https://www.canada.ca/en/employment-social-development/programs/pensions/pension/statistics/2026-quarterly-october-december.html)
- [Service Canada - OAS pension recovery tax (modified 2026-09-29)](https://www.canada.ca/en/services/benefits/publicpensions/old-age-security/recovery-tax.html)
- [Finance Canada - Backgrounder: The new Canada Groceries and Essentials Benefit (2026-01-26)](https://www.canada.ca/en/department-finance/news/2026/01/the-new-canada-groceries-and-essentials-benefit.html)
- [Finance Canada - Legislation passes to deliver new Canada Groceries and Essentials Benefit (2026-02-12)](https://www.canada.ca/en/department-finance/news/2026/02/legislation-passes-to-deliver-new-canada-groceries-and-essentials-benefit.html)
- [CRA news release - CGEB one-time top-up payment is coming June 5 (2026-04-17)](https://www.canada.ca/en/revenue-agency/news/2026/04/canada-groceries-and-essentials-benefit-one-time-top-up-payment-to-make-groceries-and-other-essentials-more-affordable-is-coming-june-5.html)
- [CRA RC4210 - Canada Groceries and Essentials Benefit (modified 2026-07-02)](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4210/canada-groceries-essentials-benefit.html)
- [CRA - CGEB: How much you can get (modified 2026-07-15)](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-groceries-essentials-benefit/how-much.html)
- [CRA - Canada Groceries and Essentials Benefit (modified 2026-06-08)](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-groceries-essentials-benefit.html)
- [CRA - CCB: How we calculate your CCB (modified 2026-10-05)](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit-overview/canada-child-benefit-we-calculate-your-ccb.html)
- [ESDC - Canada Disability Benefit: How much you could receive (modified 2026-09-15)](https://www.canada.ca/en/services/benefits/disability/canada-disability-benefit/amount.html)
- [CRA - Tax rates on withdrawals (RRSP) (modified 2026-01-29)](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/making-withdrawals/tax-rates-on-withdrawals.html)
- [CRA RC4157 Deducting Income Tax on Pension and Other Income (modified 2026-01-12)](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4157/deducting-income-tax-on-pension-other-income-filing-t4a-slip-summary.html)
- [CRA T4079 T4RSP and T4RIF Guide (modified 2026-01-06)](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4079/t4rsp-t4rif-guide.html)
