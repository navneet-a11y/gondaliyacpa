# WealthScale: five open tax items, research for Sharad's review (November 5, 2026)

Prepared for a quick confirm / change decision on each item. Nothing below has been changed on the site yet.

**Limit on this research.** The research session's network blocked canada.ca, laws-lois.justice.gc.ca, cmhc-schl.gc.ca, revenuquebec.ca and the provincial government sites. Figures marked "search excerpt" come from search-engine summaries of the named pages, not from reading the pages in full. Items marked "re-check" should be confirmed on the official page (by Sharad, or by a re-run once those sites are allowed) before any change goes live.

Where each item is used: `site-wide/ws-data.json` (calculators) and the pages listed.

---

## 1. 2026 dividend tax credit rates: AB, SK, MB, YT, NT, NU

**Site now:** no rate for these six; pages and calculators show "being confirmed". Pages: 102, 103, 105, 108, 110, 111, 116, 117, 118, 127, 147, 148, 170, plus several first-101 pages that mention it.

Rates are a percent of the grossed-up (taxable) dividend. The 2026 CRA 428 forms are not out yet (normally January 2027); no 2026 change was found, but 2026 legislation could not be read.

| Province | Eligible | Non-eligible | Source and quality | Re-check |
|---|---|---|---|---|
| Alberta | 8.12% | 2.18% | Eligible: CRA Alberta guide, "decreases from 10% to 8.12% for 2021 and subsequent years" (official, search excerpt). Non-eligible: TaxTips (unofficial) | AB428 worksheet line 61520 |
| Saskatchewan | 11% | 2.519% | Eligible: CRA SK428 worksheet 2018 (official but old). Non-eligible: TaxTips, says Bill 30 (Dec 2024) cancelled the planned changes; one calculator shows 2.11% (conflict) | SK428 2025 |
| Manitoba | 8% | 0.7835% | Manitoba Finance for 2024-2025 (official); EY 2026 table; March 2026 budget reported no rate changes | MB428 2025 |
| Yukon | 12.02% | 0.67% | Unofficial only (Accountor, worksheet copies) | YT428 2025 |
| Northwest Territories | 11.5% | 6% | Unofficial only (TaxTips, EY 2025) | NT428 2025 |
| Nunavut | 5.51% | 2.61% | Unofficial only; one older source uses a different basis | NU428 2025 |

**Recommendation:** do not publish yet. Sharad (or a re-run with canada.ca allowed) checks line 61520 of the six 2025 worksheets; if they match, publish the six rates as 2026 rates "unchanged from 2025" and turn dividend figures on for every province.

## 2. Low-income tax reductions: NB, NS, PE, NL

**Site now:** not modelled (only Ontario and B.C. reductions are in the tax engine); pages say only the basic personal amounts are counted, so tax at $20,000 to $40,000 may be overstated in these four provinces.

| Province | Maximum | Threshold | Phase-out | Income used | Source and quality |
|---|---|---|---|---|---|
| Newfoundland and Labrador | $842 single (official: NLR 18/26 s. 3(b), filed May 14, 2026); spouse/dependant amount not found (2025: $557) | $24,191 individual (EY; = 2025 official $23,928 x 1.011) | 16% (EY; reproduces 2025 official figures) | Individual, with a family threshold | Maximum official; rest medium |
| New Brunswick | about $817-818 single plus the same for spouse/dependant (third-party; 2025: $802 + $802) | $22,358 (EY; = 2025 official $21,920 x 1.02) | 3% (official, GNB Finance) | Adjusted family net income (official, CRA) | Medium to medium-high |
| Nova Scotia | $300 basic + $300 spouse/dependant + $165 per child ($165 official CRA 2025; $300 from a 2011 NS Finance document) | $15,000 | 5% | Adjusted family net income (official) | Medium; no evidence it is indexed |
| Prince Edward Island | $350 self + $350 spouse/dependant (not confirmed for 2026); $300 per child (older CRA) | $23,000, up from $22,650 (EY, MNP; budget confirms an increase) | 5% (EY) | Adjusted family net income (official) | Medium-high |

**Recommendation:** these are close but not fully official. Sharad confirms the four rows (the CRA NB428/NS428/PE428/NL428 2026 forms or T4127 will have them); then one data change adds the reductions to every calculator and table, and the "only the basic personal amounts are counted" wording on the four province pages is updated.

## 3. Quebec 14% credit rate

**Site now:** the Quebec take-home pay calculator values Quebec non-refundable credit amounts at 14%.

- Quebec 2026 first-bracket rate is 14% (up to $54,345): Revenu Quebec, "the income tax rates remain unchanged for 2026", and Finance Quebec 2026 parameters, Table 3 (official, search excerpt).
- Credit conversion rate 14%: stated in words only by KPMG's 2026 Quebec table ("Tax rate applied to credits 14%") and TaxTips (2023 Quebec budget reduced the credit rate to 14%). No official page wording retrieved.
- 2026 Quebec basic personal amount $18,952 (official, Finance Quebec Table 3), matching the site.
- Not every Quebec credit uses 14% (donations 20% / 24% / 25.75%; union dues 10%); the calculator only applies 14% to the basic and similar amounts.

**Recommendation:** confirm. 14% is correct; Sharad can confirm from the TP-1 guide (line 399) wording. No site change needed.

## 4. Canada Disability Benefit thresholds, July 2026 to June 2027

**Site now:** $23,483 single, $33,182.50 couple; work-income exemptions $10,210 / $14,294; maximum $204.20 a month. Pages 159 and 164.

- SOR/2025-35 indexes the $23,000 / $32,500 thresholds and the $10,000 / $14,000 exemptions by the same factor A as the $2,400 maximum (all-items CPI, annual average). Official (Canada Gazette II, search excerpt).
- ESDC's $204.20 maximum implies A = 1.021 (2,400 x 1.021 / 12 = 204.20); Statistics Canada reports 2025 CPI up 2.1%.
- 23,000 x 1.021 = 23,483.00; 32,500 x 1.021 = 33,182.50. The Income Security Advocacy Centre 2026-27 rates sheet (non-government) gives the same four figures.
- ESDC's amount page appears still to show the base $23,000 / $32,500 (not confirmed).
- Re-check: SOR/2026-123 (in force September 1, 2026) replaced the description of B in s. 6(1); confirm the threshold wording did not change.

**Recommendation:** keep the site figures, subject to the SOR/2026-123 check.

## 5. CMHC 0.20% surcharge on 30-year amortizations

**Site now:** the mortgage calculators add 0.20% to every insured 30-year amortization. Pages 172, 173, 175.

- CMHC "Premium Information for Homeowner and Small Rental Loans": "amortization period beyond 25 years is subject to a 0.20% surcharge" (official, search excerpt, no buyer-type limit).
- Canada Guaranty lender update on the December 15, 2024 changes (all first-time buyers and all new builds): "the premium surcharge for 30-year amortization will continue to be 20 bps."
- Sagen: "if a mortgage is eligible for an amortization greater than 25 years (up to 30 years) an additional premium of 0.20% will apply."
- No CMHC text after December 15, 2024 naming the expanded groups was found.

**Recommendation:** keep the site rule.

---

## Summary for Sharad

| # | Item | Proposed decision |
|---|---|---|
| 1 | Dividend tax credit, six provinces | Check line 61520 on the six 2025 worksheets, then publish |
| 2 | Low-income reductions, four provinces | Confirm the four rows, then add to the tax engine |
| 3 | Quebec 14% | Confirm; no change |
| 4 | CDB thresholds | Keep $23,483 / $33,182.50 after the SOR/2026-123 check |
| 5 | CMHC 0.20% surcharge | Keep |

Full research notes: dtc.md, lowincome-quebec.md and cdb-cmhc.md (copied next to this file in wealthscale/research-2026-11-05/).

---

## Update, November 5 (after canada.ca was allowed): official CRA 2025 forms read

The 2025 CRA forms were downloaded from canada.ca and read directly (copies in research-2026-11-05/cra-2025-forms/).

**Item 1, dividend tax credit: CONFIRMED for 2025 from CRA worksheets (line 61520), matching every figure in the table above.** Rate x line 12000 minus line 12010 (eligible, grossed-up) and rate x line 12010 (non-eligible, grossed-up):

| Province | Eligible | Non-eligible | CRA source |
|---|---|---|---|
| Alberta | 8.12% | 2.18% | Worksheet AB428 2025 (5009-d-fill-25e.pdf) |
| Saskatchewan | 11% | 2.519% | Worksheet SK428 2025 (5008-d-fill-25e.pdf) |
| Manitoba | 8% | 0.7835% | Worksheet MB428 2025 (5007-d-fill-25e.pdf) |
| Yukon | 12.02% | 0.67% | Worksheet YT428 2025 (5011-d-fill-25e.pdf) |
| Northwest Territories | 11.5% | 6% | Worksheet NT428 2025 (5012-d-fill-25e.pdf) |
| Nunavut | 5.51% | 2.61% | Worksheet NU428 2025 (5014-d-fill-25e.pdf) |

These are the 2025 rates. CRA publishes the 2026 worksheets in January 2027; no 2026 change to any of the six was found. For Sharad: confirm they may be shown as the 2026 rates (or as "2025 rates, 2026 not yet published").

**Item 2, low-income reductions: 2025 official, 2026 NOT confirmed.** The 2025 forms give: NB eligibility single net income under $48,653 / family under $75,387; NS $300 basic + $300 spouse or eligible dependant (max $600) + $165 per child; PE $350 basic plus a $250 age reduction (born 1960 or earlier) and further amounts; NL $997 basic + $557 spouse. Several 2026 figures differ (NL basic $842 under NLR 18/26; PE threshold raised; NB indexed), and the 2026 forms are not out, so the 2026 values remain unconfirmed.

**Item 3, Quebec:** revenuquebec.ca still refuses automated access; unchanged (no site change needed).
