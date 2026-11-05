# CDB 2026-27 thresholds and CMHC 30-year surcharge: research notes (2026-11-05)

How these were found: canada.ca and laws-lois.justice.gc.ca could not be reached from this session (the hosts are outside the allowed network list). I stopped fetching sites after that. Every finding below comes from WebSearch result summaries, not from reading full pages. Quotes are the excerpts the search returned, which may be shortened. A person should check them against the live pages.

## Part A: CDB income thresholds, July 2026 to June 2027

Short answer: $23,483 (single) and $33,182.50 (couple) look correct. Confidence: medium-high.

1. ESDC amount page (https://www.canada.ca/en/services/benefits/disability/canada-disability-benefit/amount.html). I could not fetch it.
   - A search summary scoped to canada.ca reported that the page says "The maximum monthly benefit you could receive is $204.20", based on the 2025 return. The same summary still showed thresholds of $23,000 and $32,500, and exemptions of $10,000 and $14,000. Those are the unindexed base amounts.
   - So the page probably still shows the base amounts while showing the indexed maximum. This is unconfirmed. Confidence: low-medium.
2. Indexing provision, SOR/2025-35 (from search excerpts of the Justice Laws text and Canada Gazette II, 2025-03-12, https://gazette.gc.ca/rp-pr/p2/2025/2025-03-12/html/sor-dors35-eng.html):
   - Benefit = ((($2,400 × A) − B) ÷ 12), "rounded to the nearest cent". A is the indexing factor and B is the income reduction.
   - Indexing factor = CPI_max ÷ CPI_2024. CPI_max is "the highest Consumer Price Index for any calendar year beginning with 2024" up to the last year that ended before the payment period began.
   - CPI means "the all-items Consumer Price Index for Canada, annual average, not seasonally adjusted, … as published by Statistics Canada".
   - Reduction B = 20% × (C − D − ($23,000 × A)). D is the lesser of working income and "the product of $10,000 and the indexing factor". The couple term uses $14,000 × A for the working-income exemption.
   - The 2024 draft (CG I, https://gazette.gc.ca/rp-pr/p1/2024/2024-06-29/html/reg2-eng.html) had a couple threshold of $32,500 × A.
   - So the income thresholds and exemptions are indexed with the same factor A, not only the $2,400 maximum.
   - Rounding: only the monthly benefit is explicitly rounded (to the nearest cent). I found no rounding rule for the thresholds, and I could not confirm whether A itself is rounded, for example to 3 decimals. A search for that wording returned nothing.
   - The adjustment applies each July, starting July 2026. Some secondary sources also say amounts cannot go down; that is not confirmed.
   - SOR/2026-123 (CG II, 2026-07-01, https://gazette.gc.ca/rp-pr/p2/2026/2026-07-01/html/sor-dors123-eng.html), in force 2026-09-01: adds a $150 supplemental amount for each DTC certification or re-certification, replaces the description of B in s. 6(1), and updates "adjusted income" to match the Income Tax Act. The excerpts did not show the new B text, so I cannot confirm whether the threshold dollar figures changed. Worth checking.
3. Factor used: $204.20 ÷ $200 = 1.021 (2,400 × 1.021 = 2,450.40, and 2,450.40 ÷ 12 = 204.20). StatCan reports that 2025 annual average CPI rose 2.1% (https://www.statcan.gc.ca/o1/en/app/8935-consumer-price-index-annual-review-2025). One summary put the 2025 index at 164.2.
   - An unrounded 164.2 ÷ 2024 average (about 160.8 to 160.9) gives about 1.0205 to 1.0211. ESDC's $204.20 matches a factor of exactly 1.021, so ESDC appears to use 1.021.
4. Other statements of the 2026-27 thresholds:
   - The ISAC (Income Security Advocacy Centre) 2026-27 rates sheet lists $23,483 (single, $10,210 work-income exemption) and $33,182.50 (couple, $14,294 exemption): https://incomesecurity.org/wp-content/uploads/2026/07/ISAC-Canada-Disability-Benefit-Rates-Sheet-2026-2027.pdf. This is an NGO, not official.
   - Several secondary sites give $10,210 and $14,294, which equal 10,000 × 1.021 and 14,000 × 1.021. Some sites give $23,460 and $33,150, which is 2% and inconsistent with the 2.1% factor.
   - I found no ESDC news release or CRA page stating the thresholds. The CRA "CDB table July 2026" page is the Child Disability Benefit, a different program.

Conclusion: 23,000 × 1.021 = 23,483.00 and 32,500 × 1.021 = 33,182.50. Both match ISAC and the factor implied by the official $204.20 maximum. These are the correct indexed figures if A = 1.021. Nothing confirms that the thresholds are rounded; the regulation formula multiplies them directly by A. Caveats: (a) the ESDC page may still show $23,000 and $32,500 (base amounts); (b) I could not verify whether SOR/2026-123 changed B's thresholds.

## Part B: CMHC 0.20% surcharge for 30-year amortization after Dec 15, 2024

Short answer: yes. Every source found says the 20 bp surcharge applies to every insured amortization over 25 years (up to 30), which since Dec 15, 2024 covers all first-time buyers and all new-build buyers. I found no official CMHC text written after Dec 15, 2024 that says this explicitly. Confidence: medium-high.

- CMHC notice (2024), https://www.cmhc-schl.gc.ca/media-newsroom/notices/2024/cmhc-revises-homeowner-mortgage-loan-insurance-premiums: "Effective August 1st, a premium surcharge of 20 basis points will be applied to qualified first-time homebuyers opting for the increased amortization of 30 years." Official.
- CMHC "Premium Information for Homeowner and Small Rental Loans", https://www.cmhc-schl.gc.ca/professionals/project-funding-and-mortgage-financing/mortgage-loan-insurance/mortgage-loan-insurance-homeownership-programs/premium-information-for-homeowner-and-small-rental-loans: excerpt says an "amortization period beyond 25 years is subject to a 0.20% surcharge". This is a general rule with no restriction to a buyer group. Official, but the search engine's cached copy may be old.
- Canada Guaranty Lender Update, Sept 30, 2024 (on the Dec 15, 2024 changes), https://www.canadaguaranty.ca/wp-content/uploads/2021/04/LENDER-UPDATE-Mortgage-Insurance-Rule-Changes_Effective-Dec.-15-2024-Sept-30-2024_En.pdf: covers first-time buyers of new or existing homes and all buyers of newly constructed homes. It says "the premium surcharge for 30-year amortization will continue to be 20 bps." Private insurer, corroborating.
- Sagen Progress Advance, https://www.sagen.ca/products-and-services/progress-advance/: "if a mortgage is eligible for an amortization greater than 25 years (up to 30 years) an additional premium of 0.20% will apply." Private insurer, corroborating.
- CMHC Home Start fact sheet (30-year for first-time buyers or new builds when LTV is over 80%): https://assets.cmhc-schl.gc.ca/sites/cmhc/professional/project-funding-and-mortgage-financing/mortgage-loan-insurance/mortgage-loan-insurance-homeownership-programs/home-start/home-start-fact-sheet-en.pdf. The excerpts did not mention the surcharge.
- Finance Canada, July 2024 release: https://www.canada.ca/en/department-finance/news/2024/07/government-announces-30-year-amortizations-for-insured-mortgages-to-put-homeownership-in-reach-for-millennials-and-gen-z.html. I could not fetch it, and the excerpts did not mention the surcharge.
- Several secondary sources (Ratehub, wowa, and others) give the worked example 4.00% + 0.20% = 4.20%.
- I could not fetch the consumer cost page (https://www.cmhc-schl.gc.ca/consumers/home-buying/mortgage-loan-insurance-for-consumers/cmhc-mortgage-loan-insurance-cost) because I had already stopped fetching sites.
