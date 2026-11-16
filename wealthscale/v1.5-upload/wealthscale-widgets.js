/*! WealthScale widgets v1.5 | November 9, 2026 | (c) WealthScale Media Inc.
 * One file, loaded site-wide. Place <div data-ws-widget="NAME"></div> in any page.
 * All figures live in the WS_DATA block below. Update a figure there once and every page updates.
 * General information only. Not financial, investment, tax or legal advice.
 */
(function () {
  'use strict';

  /* =====================================================================
   * 1. DATA: every figure the widgets use. EDIT FIGURES HERE ONLY.
   * ===================================================================== */
  var D = {"asOf":"2026-10-23","year":2026,"provinces":[["AB","Alberta"],["BC","British Columbia"],["MB","Manitoba"],["NB","New Brunswick"],["NL","Newfoundland and Labrador"],["NS","Nova Scotia"],["NT","Northwest Territories"],["NU","Nunavut"],["ON","Ontario"],["PE","Prince Edward Island"],["QC","Quebec"],["SK","Saskatchewan"],["YT","Yukon"]],"provName":{"AB":"Alberta","BC":"British Columbia","MB":"Manitoba","NB":"New Brunswick","NL":"Newfoundland and Labrador","NS":"Nova Scotia","NT":"Northwest Territories","NU":"Nunavut","ON":"Ontario","PE":"Prince Edward Island","QC":"Quebec","SK":"Saskatchewan","YT":"Yukon"},"age_of_majority":{"AB":18,"BC":19,"MB":18,"NB":19,"NL":19,"NS":19,"NT":19,"NU":19,"ON":18,"PE":18,"QC":18,"SK":18,"YT":19},"tax":{"federal":{"brackets":[[58523,0.14],[117045,0.205],[181440,0.26],[258482,0.29],[null,0.33]],"bpa":16452,"bpa_min":14829,"bpa_phase":[181440,258482]},"provinces":{"AB":{"brackets":[[61200,0.08],[154259,0.1],[185111,0.12],[246813,0.13],[370220,0.14],[null,0.15]],"bpa":22769},"BC":{"brackets":[[50363,0.056],[100728,0.077],[115648,0.105],[140430,0.1229],[190405,0.147],[265545,0.168],[null,0.205]],"bpa":13216,"reduction":{"type":"bc","base":690,"threshold":25570,"rate":0.0356}},"MB":{"brackets":[[47000,0.108],[100000,0.1275],[null,0.174]],"bpa":15780,"bpa_phase":[200000,400000,0]},"NB":{"brackets":[[52333,0.094],[104666,0.14],[193861,0.16],[null,0.195]],"bpa":13664},"NL":{"brackets":[[44678,0.087],[89354,0.145],[159528,0.158],[223340,0.178],[285319,0.198],[570638,0.208],[1141275,0.213],[null,0.218]],"bpa":13094},"NS":{"brackets":[[30995,0.0879],[61991,0.1495],[97417,0.1667],[157124,0.175],[null,0.21]],"bpa":11932},"NT":{"brackets":[[53003,0.059],[106009,0.086],[172346,0.122],[null,0.1405]],"bpa":18198},"NU":{"brackets":[[55801,0.04],[111602,0.07],[181439,0.09],[null,0.115]],"bpa":19659},"ON":{"brackets":[[53891,0.0505],[107785,0.0915],[150000,0.1116],[220000,0.1216],[null,0.1316]],"bpa":12989,"surtax":[[5818,0.2],[7446,0.36]],"health_premium":[[20000,36000,0,0.06,300],[36000,48000,300,0.06,450],[48000,72000,450,0.25,600],[72000,200000,600,0.25,750],[200000,null,750,0.25,900]],"reduction":{"type":"on","base":300.0,"dep":554.0}},"PE":{"brackets":[[33928,0.095],[65820,0.1347],[106890,0.166],[142520,0.1762],[200000,0.19],[null,0.2]],"bpa":15000},"QC":{"brackets":[[54345,0.14],[108680,0.19],[132245,0.24],[null,0.2575]],"bpa":18952},"SK":{"brackets":[[54532,0.105],[155805,0.125],[null,0.145]],"bpa":20381},"YT":{"brackets":[[58523,0.064],[117045,0.09],[181440,0.109],[500000,0.128],[null,0.15]],"bpa":16452,"bpa_phase":[181440,258482,14829]}},"qc_abatement":0.165,"dividends":{"eligible_grossup":0.38,"noneligible_grossup":0.15,"federal_dtc_eligible":0.150198,"federal_dtc_noneligible":0.090301,"provincial_dtc":{"AB":[0.0812,0.0218],"BC":[0.12,0.0196],"MB":[0.08,0.007835],"NB":[0.14,0.0275],"NL":[0.063,0.032],"NS":[0.0885,0.015],"NT":[0.115,0.06],"NU":[0.0551,0.0261],"ON":[0.1,0.029863],"PE":[0.105,0.013043],"QC":[0.117,0.0342],"SK":[0.11,0.02519],"YT":[0.1202,0.0067]}},"capital_gains_inclusion":0.5},"tfsa":{"limits":{"2009":5000,"2010":5000,"2011":5000,"2012":5000,"2013":5500,"2014":5500,"2015":10000,"2016":5500,"2017":5500,"2018":5500,"2019":6000,"2020":6000,"2021":6000,"2022":6000,"2023":6500,"2024":7000,"2025":7000,"2026":7000},"over_tax_month":0.01},"rrsp":{"limits":{"2020":27230,"2021":27830,"2022":29210,"2023":30780,"2024":31560,"2025":32490,"2026":33810,"2027":35390},"pct":0.18,"cushion":2000,"deadline":{"2025":"2026-03-02","2026":"2027-03-01"},"withholding":{"other":[[5000,0.1],[15000,0.2],[null,0.3]],"QC":[[5000,0.05],[15000,0.1],[null,0.15]],"QC_prov":0.14},"withholding_text":"10% up to $5,000, 20% over $5,000 to $15,000 and 30% over $15,000 (outside Quebec)"},"fhsa":{"annual":8000,"lifetime":40000,"carry":8000,"max_years":15,"max_age":71,"first_year":2023},"resp":{"lifetime":50000,"cesg_rate":0.2,"cesg_on":2500,"cesg_annual":500,"cesg_max_year":1000,"cesg_lifetime":7200,"cesg_age16_total":2000,"cesg_age16_years":4,"acesg_rates":[0.2,0.1],"acesg_on_first":500,"acesg_income":[58523,117045],"clb_first":500,"clb_yearly":100,"clb_max":2000,"clb_thresholds":[null,58523,58523,58523,66036,73577],"bctesg":1200,"qesi_rate":0.1,"qesi_annual":250,"qesi_lifetime":3600},"rrif":{"factors":{"71":0.0528,"72":0.054,"73":0.0553,"74":0.0567,"75":0.0582,"76":0.0598,"77":0.0617,"78":0.0636,"79":0.0658,"80":0.0682,"81":0.0708,"82":0.0738,"83":0.0771,"84":0.0808,"85":0.0851,"86":0.0899,"87":0.0955,"88":0.1021,"89":0.1099,"90":0.1192,"91":0.1306,"92":0.1449,"93":0.1634,"94":0.1879,"95":0.2}},"hbp":{"max":60000,"repay_years":15,"deferral":[2022,2028],"deferral_start":5,"prev":35000,"prev_until":"April 16, 2024"},"us_withholding":{"treaty":0.15,"no_w8":0.3,"accounts":[["rrsp","RRSP",true,"Not needed","RRSPs are exempt from US withholding on dividends from US-listed securities held directly, under Article XXI of the Canada-US tax treaty."],["rrif","RRIF",true,"Not needed","RRIFs are treated like RRSPs: no US withholding on dividends from US-listed securities held directly."],["lira","LIRA or LIF",true,"Not needed","Locked-in retirement accounts are retirement arrangements, so the treaty exemption applies."],["tfsa","TFSA",false,"No","The tax withheld in a TFSA is a permanent cost: there is no Canadian tax to credit it against."],["fhsa","FHSA",false,"No","FHSAs are not retirement accounts, so withholding applies and cannot be recovered."],["resp","RESP",false,"No","RESPs are not retirement accounts, so withholding applies and cannot be recovered."],["nonreg","Non-registered (cash or margin)",false,"Yes, as a foreign tax credit","You report the gross dividend and claim a foreign tax credit for the US tax on your Canadian return."]]},"deposit_insurance":{"limit":100000,"categories":["Deposits in your name","Joint deposits","Deposits in trust","RRSP deposits","RRIF deposits","TFSA deposits","FHSA deposits","RESP deposits","RDSP deposits"],"note":"Credit unions are covered by provincial deposit insurance instead."},"cipf":{"limit":1000000,"groups":[["General accounts","cash, margin, TFSA and FHSA accounts combined"],["Registered retirement accounts","RRSP, RRIF and LIF accounts combined"],["RESPs","RESP accounts"]]},"benefits":{"cpp_oas":{"name":"CPP and OAS","dates":["2026-01-28","2026-02-25","2026-03-27","2026-04-28","2026-05-27","2026-06-26","2026-07-29","2026-08-27","2026-09-25","2026-10-28","2026-11-26","2026-12-22"],"note":"Old Age Security and the Guaranteed Income Supplement are paid on the same day as the Canada Pension Plan. 2027 dates have not been published yet."},"gst":{"name":"Canada Groceries and Essentials Benefit (formerly the GST/HST credit)","dates":["2026-01-05","2026-04-02","2026-07-03","2026-10-05","2027-01-05","2027-04-05"],"note":"The Canada Groceries and Essentials Benefit replaced the GST/HST credit in July 2026."},"ccb":{"name":"Canada Child Benefit","dates":["2026-01-20","2026-02-20","2026-03-20","2026-04-20","2026-05-20","2026-06-19","2026-07-20","2026-08-20","2026-09-18","2026-10-20","2026-11-20","2026-12-11"],"note":"2027 dates have not been published yet."},"otb":{"name":"Ontario Trillium Benefit","dates":["2026-01-09","2026-02-10","2026-03-10","2026-04-10","2026-05-08","2026-06-10","2026-07-10","2026-08-10","2026-09-10","2026-10-09","2026-11-10","2026-12-10"],"note":"2027 dates have not been published yet."},"cdb":{"name":"Canada Disability Benefit","dates":["2026-01-15","2026-02-19","2026-03-19","2026-04-16","2026-05-21","2026-06-18","2026-07-16","2026-08-20","2026-09-17","2026-10-15","2026-11-19","2026-12-17"],"note":"2027 dates have not been published yet."},"acwb":{"name":"Canada Workers Benefit advance payments","dates":["2026-01-12","2026-07-10","2026-10-09"],"note":"2027 dates have not been published yet."},"odsp":{"name":"Ontario Disability Support Program (ODSP)","dates":["2026-11-30"],"note":"Paid on the last business day of each month, for that month; the December payment usually comes earlier in the month."},"ow":{"name":"Ontario Works","dates":["2026-10-30","2026-11-30"],"note":"Paid on the last business day of the month before the month it covers, usually the same day as ODSP."},"aish":{"name":"Assured Income for the Severely Handicapped (AISH)","dates":["2026-10-27","2026-11-25","2026-12-22"],"note":"Direct deposit four business days before the first of the month."},"bcpwd":{"name":"BC disability and income assistance","dates":["2026-10-21","2026-11-18","2026-12-16","2027-01-20","2027-02-24","2027-03-24","2027-04-21","2027-05-19","2027-06-23","2027-07-21","2027-08-25","2027-09-22","2027-10-20","2027-11-24","2027-12-22"],"note":"Cheque issue dates set by the BC government each year."},"acfb":{"name":"Alberta Child and Family Benefit","dates":["2026-11-27"],"note":"Paid in August, November, February and May."},"solidarity":{"name":"Quebec solidarity tax credit","dates":["2026-07-03","2026-08-05","2026-09-04","2026-10-05","2026-11-05","2026-12-04","2027-01-05","2027-02-05","2027-03-05","2027-04-05","2027-05-05","2027-06-04"],"note":"Paid in the first five days of each month when paid monthly."},"bcfb":{"name":"BC Family Benefit","dates":["2026-01-20","2026-02-20","2026-03-20","2026-04-20","2026-05-20","2026-06-19","2026-07-20","2026-08-20","2026-09-18","2026-10-20","2026-11-20","2026-12-11"],"note":"Paid monthly with the Canada Child Benefit, on the same dates."}},"oas":{"threshold":95323,"rate":0.15,"income_year":2026,"max65":762.5,"max75":838.75,"defer":0.006,"full_years":40,"min_years":10,"inc75":0.1},"cpp":{"max65":1507.65,"avg65":858.34,"early":0.006,"late":0.007},"gst_credit":{"period":"July 2026 to June 2027","income_year":2025,"adult":445,"child":234,"single_supp":234,"supp_base":11564,"supp_rate":0.02,"threshold":46432,"reduce":0.05,"note":"From July 2026 this payment is the Canada Groceries and Essentials Benefit, which replaced the GST/HST credit with amounts 25% higher. The 2% phase-in of the single supplement and the 5% income reduction are set by the Income Tax Act for this benefit; CRA calculates your exact amount from your return."},"superficial":{"days":30},"pension":{"split_max":0.5,"amount":2000},"spousal":{"years":3,"lesser":true},"fedcred":{"age":9208.0,"age_thr":46432.0,"age_rate":0.15,"pension":2000.0},"ccb":{"period":"July 2026 to June 2027","income_year":2025,"max_u6":8157.0,"max_6_17":6883.0,"t1":38237.0,"t2":82847.0,"r1":[0.07,0.135,0.19,0.23],"b2":[3123.0,6022.0,8476.0,10260.0],"r2":[0.032,0.057,0.08,0.095],"cdb_max":3480.0,"cdb_t":82847.0,"cdb_r":[0.032,0.057]},"cdb":{"period":"July 2026 to June 2027","max_month":204.2,"A":1.021,"wie_single":10210.0,"wie_couple":14294.0,"t_single":23483.0,"t_couple":33182.5,"rate":0.2,"rate_both":0.1},"cwb":{"year":2026,"max_single":1665.0,"max_family":2869.0,"wit":3000.0,"phase_in":0.27,"po_single":27392,"po_family":31251,"po_rate":0.15,"sec_exempt":16714.0,"dis_max":860.0,"dis_wit":1150.0,"dis_po_single":38495.0,"dis_po_family":50377.0,"dis_rate":0.15,"dis_rate_both":0.075,"advance":0.5,"reconfigured":["AB","QC","NU"]},"gis":{"quarter":"October to December 2026","rows":[["single","Single, widowed or divorced, receiving OAS",1138.9,23112.0],["spouse_full_oas","Spouse or partner receives the full OAS pension",685.56,30528.0],["spouse_no_oas","Spouse or partner does not receive OAS",1138.9,55392.0],["spouse_allowance","Spouse or partner receives the Allowance",685.56,42768.0]],"allowance":[1448.06,42768],"survivor":[1726.18,31152.0]},"otb":{"period":"July 2026 to June 2027","income_year":2025,"lump":500.0,"energy_max":290.0,"pt_ns":[944,73],"pt_s":[581,617],"t_single_ns":29047.0,"t_family_ns":36309.0,"t_single_s":36309.0,"t_couple_s":43571.0,"oeptc_rate":0.02,"noec":[189.0,290.0,50833.0,65356.0,0.01],"ostc":[378.0,29047.0,36309.0,37273.0,0.04]},"ltt":{"ON":{"br":[[55000,0.005],[250000,0.01],[400000,0.015],[2000000,0.02],[null,0.025]],"fthb":4000.0},"TO":{"br":[[55000,0.005],[250000,0.01],[400000,0.015],[2000000,0.02],[3000000,0.025],[4000000,0.044000000000000004],[5000000,0.0545],[10000000,0.065],[20000000,0.0755],[null,0.086]],"fthb":4475.0},"BC":{"br":[[200000,0.01],[2000000,0.02],[null,0.03]],"extra_from":3000000,"extra":0.02,"fthb_full":835000.0,"fthb_part":500000.0,"fthb_max":8000.0,"fthb_zero":860000,"nbh_full":1100000.0,"nbh_zero":1150000.0},"QC":{"br":[[62900,0.005],[315000,0.01],[null,0.015]]},"MTL":{"br":[[62900,0.005],[315000,0.01],[552300,0.015],[1104700,0.02],[2136500,0.025],[3113000,0.035],[null,0.04]],"fthb_none":true,"fthb_closed":"2026-07-07"},"QCC":{"br":[[62900,0.005],[315000,0.01],[500000,0.015],[750000,0.025],[null,0.03]]},"MB":{"br":[[30000,0.0],[90000,0.005],[150000,0.01],[200000,0.015],[null,0.02]]},"NB":{"rate":0.01},"NS":{"halifax":0.015},"PE":{"rate":0.01,"low":30000.0},"NL":{"base":100,"per100":0.4,"from":500,"mort_cap":5000.0},"AB":{"base":50.0,"per5000":5,"mort_base":50.0},"SK":{"transfer":[[500,0,"flat"],[6300,25.0,"flat"],[null,0.004,"rate"]],"mortgage":[[249999.99,200.0],[500000,275.0],[750000,525.0],[1000000,775.0],[null,1000.0]]}},"mortgage":{"insured_max":1500000,"premium_non_trad":0.045,"premiums":[[0.65,0.006],[0.75,0.017],[0.8,0.024],[0.85,0.027999999999999997],[0.9,0.031],[0.95,0.04]],"surcharge_30":0.002,"pst":{"ON":0.08,"QC":0.09,"SK":0.06},"pst_text":"in Ontario (8%), Quebec (9%, rising to 9.975% for premiums paid after December 31, 2026) and Saskatchewan (6%), provincial sales tax on the premium is paid in cash at closing and cannot be added to the loan.","buffer":0.02,"floor":0.0525,"gds":0.39,"tds":0.44},"payroll":{"year":2026,"cpp":{"ympe":74600.0,"exemption":3500.0,"base_rate":0.0495,"first_add_rate":0.01,"yampe":85000.0,"rate2":0.04,"max1":4230.45,"max2":416.0},"qpp":{"ympe":74600.0,"exemption":3500.0,"base_rate":0.053,"first_add_rate":0.01,"yampe":85000.0,"rate2":0.04,"max1":4479.3,"max2":416.0},"ei":{"mie":68900.0,"rate":0.0163,"rate_qc":0.013000000000000001,"max":1123.07,"max_qc":895.7},"qpip":{"mie":103000.0,"rate":0.0043,"max":442.9},"cea":1501.0,"k2p":{"AB":"lowest","BC":"lowest","MB":"lowest","NB":"lowest","NL":"lowest","NS":"lowest","NT":"lowest","NU":"lowest","ON":"lowest","PE":"lowest","SK":"lowest","YT":"lowest"},"qc_workers":{"rate":0.06,"max":1450.0}},"prescribed_rate":{"current":0.03,"quarter":"October 1 to December 31, 2026"},"donation_federal":{"first":0.14,"above":0.29,"top":0.33,"top_from":258482},"donation_rates":{"AB":[0.6,0.21,null,null],"BC":[0.056,0.168,0.205,265545],"MB":[0.108,0.174,null,null],"NB":[0.094,0.1795,null,null],"NL":[0.087,0.218,null,null],"NT":[0.059,0.1405,null,null],"NS":[0.0879,0.21,null,null],"NU":[0.04,0.115,null,null],"ON":[0.0505,0.1116,null,null],"PE":[0.095,0.19,null,null],"SK":[0.105,0.145,null,null],"YT":[0.064,0.128,null,null],"QC":[0.2,0.24,null,null]},"donation_rates_year":{"AB":2025,"BC":2026,"MB":2025,"NB":2025,"NL":2025,"NS":2025,"NT":2025,"NU":2025,"ON":2025,"PE":2025,"QC":2025,"SK":2025,"YT":2025},"ei":{"benefit_rate":0.55,"max_weekly":729.0},"dtc":{"federal":10341,"federal_supplement":6032.0,"provincial":{"AB":null,"BC":9913.0,"MB":null,"NB":10210.0,"NL":null,"NS":null,"NT":14758.0,"NU":null,"ON":10494.0,"PE":null,"QC":4208.0,"SK":14266.0,"YT":null},"provincial_supplement":{"AB":null,"BC":5783.0,"MB":null,"NB":null,"NL":null,"NS":null,"NT":null,"NU":null,"ON":null,"PE":null,"QC":null,"SK":14266.0,"YT":null}},"rdsp":{"income_threshold":117045,"bond_lower":38237,"bond_upper":58523,"grant_lifetime":70000,"bond_lifetime":20000,"bond_max":1000,"max_age":49,"grant_low":[[500,3],[1000,2]],"grant_high":[[1000,1]],"status":"verified October 28, 2026 (facts-invtax-2026)"},"markets":{"tsx":{"hours":{"open":"09:30","close":"16:00","tz":"America/Toronto"},"holidays_2026":[["2026-01-01","New Year's Day"],["2026-02-16","Family Day"],["2026-04-03","Good Friday"],["2026-05-18","Victoria Day"],["2026-07-01","Canada Day"],["2026-08-03","Civic Holiday"],["2026-09-07","Labour Day"],["2026-10-12","Thanksgiving Day"],["2026-12-25","Christmas Day"],["2026-12-28","Boxing Day (observed)"]],"holidays_2027":[],"early_closes":[["2026-12-24","13:00"]]},"nyse":{"hours":{"open":"09:30","close":"16:00","tz":"America/Toronto"},"holidays_2026":[["2026-01-01","New Year's Day"],["2026-01-19","Martin Luther King Jr. Day"],["2026-02-16","Washington's Birthday"],["2026-04-03","Good Friday"],["2026-05-25","Memorial Day"],["2026-06-19","Juneteenth"],["2026-07-03","Independence Day (observed)"],["2026-09-07","Labor Day"],["2026-11-26","Thanksgiving Day"],["2026-12-25","Christmas Day"]],"holidays_2027":[["2027-01-01","New Year's Day"],["2027-01-18","Martin Luther King Jr. Day"],["2027-02-15","Washington's Birthday"],["2027-03-26","Good Friday"],["2027-05-31","Memorial Day"],["2027-06-18","Juneteenth (observed)"],["2027-07-05","Independence Day (observed)"],["2027-09-06","Labor Day"],["2027-11-25","Thanksgiving Day"],["2027-12-24","Christmas Day (observed)"]],"early_closes":[["2026-11-27","13:00"],["2026-12-24","13:00"],["2027-11-26","13:00"]]}},"business_chequing":[{"name":"RBC Digital Choice Business Account Package","bank":"RBC","link":null,"fee":6,"waive_balance":null,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":0,"cash_fee_per_1000":5.0,"cash_fee_per_deposit":null,"etransfer_note":"10 outgoing included a month; $1.50 each after"},{"name":"RBC Flex Choice Business Account Package","bank":"RBC","link":null,"fee":7.0,"waive_balance":null,"included_tx":0,"fee_per_tx":null,"cash_deposit_free":0,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"None included; $1.50 each"},{"name":"RBC Ultimate Business Account Package","bank":"RBC","link":null,"fee":100,"waive_balance":75000,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":25000,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"500 outgoing included a month; fee after 500 not stated"},{"name":"TD Business Digital Account","bank":"TD","link":null,"fee":6,"waive_balance":null,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":0,"cash_fee_per_1000":5.0,"cash_fee_per_deposit":null,"etransfer_note":"10 included a month; $1.50 each after"},{"name":"TD Business Essential Account","bank":"TD","link":null,"fee":35,"waive_balance":45000,"included_tx":40,"fee_per_tx":1.25,"cash_deposit_free":5000,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"10 included a month; $1.50 each after"},{"name":"TD Business Unlimited Account","bank":"TD","link":null,"fee":125,"waive_balance":65000,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":25000,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"Unlimited"},{"name":"TD Business Basic Account","bank":"TD","link":null,"fee":7,"waive_balance":null,"included_tx":7,"fee_per_tx":1.25,"cash_deposit_free":0,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"$1.50 each; number included not stated"},{"name":"Essential Business Account","bank":"BMO","link":null,"fee":5,"waive_balance":null,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":0,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"6 included a month; $1.50 each after"},{"name":"Everyday Business Account","bank":"BMO","link":null,"fee":25,"waive_balance":null,"included_tx":35,"fee_per_tx":0.6,"cash_deposit_free":2500,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"15 included a month; $1.50 each after"},{"name":"Enhanced Business Account","bank":"BMO","link":null,"fee":50,"waive_balance":35000,"included_tx":70,"fee_per_tx":0.6,"cash_deposit_free":4000,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"30 included a month; $1.50 each after"},{"name":"Elite Business Account","bank":"BMO","link":null,"fee":75,"waive_balance":75000,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":25000,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"500 included a month; $1.50 each after"},{"name":"Select Account for business, Plan A","bank":"Scotiabank","link":null,"fee":20,"waive_balance":20000,"included_tx":25,"fee_per_tx":1.5,"cash_deposit_free":6000,"cash_fee_per_1000":2.6,"cash_fee_per_deposit":null,"etransfer_note":"First 20 a month free through ScotiaOnLine; $1.00 each from the 21st"},{"name":"Select Account for business, Plan B","bank":"Scotiabank","link":null,"fee":40,"waive_balance":35000,"included_tx":70,"fee_per_tx":1.5,"cash_deposit_free":8000,"cash_fee_per_1000":2.6,"cash_fee_per_deposit":null,"etransfer_note":"First 20 a month free through ScotiaOnLine; $1.00 each from the 21st"},{"name":"Select Account for business, Plan C","bank":"Scotiabank","link":null,"fee":75,"waive_balance":45000,"included_tx":125,"fee_per_tx":1.5,"cash_deposit_free":10000,"cash_fee_per_1000":2.6,"cash_fee_per_deposit":null,"etransfer_note":"First 20 a month free through ScotiaOnLine; $1.00 each from the 21st"},{"name":"Select Account for business, Unlimited","bank":"Scotiabank","link":null,"fee":120,"waive_balance":75000,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":30000,"cash_fee_per_1000":2.6,"cash_fee_per_deposit":null,"etransfer_note":"Free and unlimited through ScotiaOnLine"},{"name":"Right Size Account for business","bank":"Scotiabank","link":null,"fee":6,"waive_balance":null,"included_tx":0,"fee_per_tx":1.25,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"Not stated"},{"name":"Basic Business Account","bank":"Scotiabank","link":null,"fee":10.95,"waive_balance":8000,"included_tx":0,"fee_per_tx":null,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"Not stated"},{"name":"Scotia Professional Plan Plus","bank":"Scotiabank","link":null,"fee":38,"waive_balance":null,"included_tx":110,"fee_per_tx":null,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"Not stated"},{"name":"Basic Business Operating Account","bank":"CIBC","link":null,"fee":6.0,"waive_balance":null,"included_tx":0,"fee_per_tx":1.0,"cash_deposit_free":0,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"$1.50 each to send"},{"name":"Everyday Business Operating Account","bank":"CIBC","link":null,"fee":20,"waive_balance":20000,"included_tx":30,"fee_per_tx":1.0,"cash_deposit_free":3000,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"Included in the 30 transactions; $1.50 each beyond"},{"name":"Advanced Business Operating Account","bank":"CIBC","link":null,"fee":40,"waive_balance":35000,"included_tx":100,"fee_per_tx":1.0,"cash_deposit_free":5000,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"Included in the 100 transactions; $1.50 each beyond"},{"name":"Unlimited Business Operating Account","bank":"CIBC","link":null,"fee":65,"waive_balance":65000,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":15000,"cash_fee_per_1000":2.5,"cash_fee_per_deposit":null,"etransfer_note":"Included in unlimited transactions"},{"name":"Digital Business Package","bank":"National Bank","link":null,"fee":7,"waive_balance":null,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":0,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"12 outgoing included a month; then $1.50 service fee plus transaction fees; incoming free"},{"name":"Hybrid Business Package","bank":"National Bank","link":null,"fee":10,"waive_balance":null,"included_tx":10,"fee_per_tx":null,"cash_deposit_free":0,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"2 outgoing included a month; then $1.50 service fee plus transaction fees"},{"name":"Premium Business Package","bank":"National Bank","link":null,"fee":100,"waive_balance":80000,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":25000,"cash_fee_per_1000":3.5,"cash_fee_per_deposit":null,"etransfer_note":"Unlimited outgoing"},{"name":"Digital plan","bank":"Desjardins","link":null,"fee":5.95,"waive_balance":null,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":0,"cash_fee_per_1000":2.25,"cash_fee_per_deposit":1.2,"etransfer_note":"Included in unlimited digital transactions; incoming free"},{"name":"35 transaction plan","bank":"Desjardins","link":null,"fee":26,"waive_balance":null,"included_tx":35,"fee_per_tx":null,"cash_deposit_free":3000,"cash_fee_per_1000":2.25,"cash_fee_per_deposit":1.2,"etransfer_note":"Outgoing $1.50; incoming free"},{"name":"55 transaction plan","bank":"Desjardins","link":null,"fee":42,"waive_balance":null,"included_tx":55,"fee_per_tx":null,"cash_deposit_free":8000,"cash_fee_per_1000":2.25,"cash_fee_per_deposit":1.2,"etransfer_note":"Outgoing $1.50; incoming free"},{"name":"75 transaction plan","bank":"Desjardins","link":null,"fee":57,"waive_balance":null,"included_tx":75,"fee_per_tx":null,"cash_deposit_free":8000,"cash_fee_per_1000":2.25,"cash_fee_per_deposit":1.2,"etransfer_note":"Outgoing $1.50; incoming free"},{"name":"100 transaction plan","bank":"Desjardins","link":null,"fee":76,"waive_balance":null,"included_tx":100,"fee_per_tx":null,"cash_deposit_free":8000,"cash_fee_per_1000":2.25,"cash_fee_per_deposit":1.2,"etransfer_note":"Outgoing $1.50; incoming free"},{"name":"300 transaction plan","bank":"Desjardins","link":null,"fee":175,"waive_balance":null,"included_tx":300,"fee_per_tx":null,"cash_deposit_free":25000,"cash_fee_per_1000":2.25,"cash_fee_per_deposit":1.2,"etransfer_note":"Outgoing $1.50; incoming free"},{"name":"Business chequing","bank":"Wealthsimple","link":null,"fee":0,"waive_balance":null,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"Included; send up to $50,000 daily; incoming free and unlimited"},{"name":"Independent Business Account","bank":"Vancity","link":null,"fee":6.5,"waive_balance":1500,"included_tx":0,"fee_per_tx":0.6,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"Free to send, receive, request or autodeposit"},{"name":"Business Self-Serve, up to 20 transactions","bank":"Vancity","link":null,"fee":8,"waive_balance":null,"included_tx":20,"fee_per_tx":0.85,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"$0.90 each, not counted in the electronic limit"},{"name":"Business Self-Serve, up to 35 transactions","bank":"Vancity","link":null,"fee":14,"waive_balance":null,"included_tx":35,"fee_per_tx":0.85,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"$0.90 each, not counted in the electronic limit"},{"name":"Business Self-Serve, up to 50 transactions","bank":"Vancity","link":null,"fee":20,"waive_balance":null,"included_tx":50,"fee_per_tx":0.85,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"$0.90 each, not counted in the electronic limit"},{"name":"Business Self-Serve, up to 75 transactions","bank":"Vancity","link":null,"fee":28,"waive_balance":null,"included_tx":75,"fee_per_tx":0.85,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"$0.90 each, not counted in the electronic limit"},{"name":"Business Full-Serve, up to 20 transactions","bank":"Vancity","link":null,"fee":15,"waive_balance":null,"included_tx":20,"fee_per_tx":0.85,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"$0.90 each, not counted in the transaction limit"},{"name":"Business Full-Serve, up to 35 transactions","bank":"Vancity","link":null,"fee":24,"waive_balance":null,"included_tx":35,"fee_per_tx":0.85,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"$0.90 each, not counted in the transaction limit"},{"name":"Business Full-Serve, up to 50 transactions","bank":"Vancity","link":null,"fee":30,"waive_balance":null,"included_tx":50,"fee_per_tx":0.85,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"$0.90 each, not counted in the transaction limit"},{"name":"Business Full-Serve, up to 75 transactions","bank":"Vancity","link":null,"fee":40,"waive_balance":null,"included_tx":75,"fee_per_tx":0.85,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"$0.90 each, not counted in the transaction limit"},{"name":"Business Full-Serve, up to 125 transactions","bank":"Vancity","link":null,"fee":55,"waive_balance":null,"included_tx":125,"fee_per_tx":0.85,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"$0.90 each, not counted in the transaction limit"},{"name":"Business Core Chequing","bank":"Coast Capital","link":null,"fee":6,"waive_balance":null,"included_tx":0,"fee_per_tx":1.25,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"2 free sent a month, then $1.50 each; receiving free"},{"name":"Business Essential Chequing","bank":"Coast Capital","link":null,"fee":28,"waive_balance":null,"included_tx":15,"fee_per_tx":1.25,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"5 free sent a month, then $1.50 each; receiving free"},{"name":"Business Premium Chequing","bank":"Coast Capital","link":null,"fee":65,"waive_balance":75000,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"Free and unlimited, sending and receiving"},{"name":"Business Self-serve Account","bank":"ATB","link":null,"fee":6,"waive_balance":null,"included_tx":null,"fee_per_tx":null,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"First 10 included, then $1.50 each"},{"name":"Business Plus Account","bank":"ATB","link":null,"fee":40,"waive_balance":null,"included_tx":150,"fee_per_tx":1.5,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"50 included, then $1.50 each"},{"name":"Business Premium Service Account","bank":"ATB","link":null,"fee":100,"waive_balance":75000,"included_tx":9999,"fee_per_tx":0,"cash_deposit_free":null,"cash_fee_per_1000":null,"cash_fee_per_deposit":null,"etransfer_note":"100 included, then $1.50 each"}],"corp_rates":{"federal_small":0.09,"federal_general":0.15,"business_limit":500000,"aaii_threshold":50000,"grind_rate":5,"provinces":{"AB":{"small":0.02,"general":0.08,"parallels_grind":null},"BC":{"small":0.02,"general":0.12,"parallels_grind":null},"MB":{"small":0.0,"general":0.12,"parallels_grind":true},"NB":{"small":0.025,"general":0.14,"parallels_grind":false},"NL":{"small":0.02,"general":0.15,"parallels_grind":null},"NS":{"small":0.015,"general":0.14,"parallels_grind":null},"NT":{"small":0.02,"general":0.115,"parallels_grind":null},"NU":{"small":0.03,"general":0.12,"parallels_grind":null},"ON":{"small":0.022,"general":0.115,"parallels_grind":false},"PE":{"small":0.01,"general":0.15,"parallels_grind":null},"QC":{"small":0.022,"general":0.115,"parallels_grind":true},"SK":{"small":null,"general":0.12,"parallels_grind":null},"YT":{"small":0.0,"general":0.12,"parallels_grind":null}},"status":"verified October 28, 2026 (facts-business-2026); provincial small rates as in effect on October 28, 2026"},"credit_cards":[{"id":"amex_aeroplan","name":"American Express Aeroplan Card","issuer":"American Express","link":null,"annual_fee":120,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"amex_aeroplan_reserve","name":"American Express Aeroplan Reserve Card","issuer":"American Express","link":null,"annual_fee":599,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"amex_cobalt","name":"American Express Cobalt Card","issuer":"American Express","link":null,"annual_fee":191.88,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":0.05,"gas":0.02,"dining":0.05,"transit":0.02,"recurring":0.01,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["grocery","dining"],"annual_spend_limit":30000,"rate_after":0.01}]},{"id":"amex_gold_rewards","name":"American Express Gold Rewards Card","issuer":"American Express","link":null,"annual_fee":250,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":0.02,"gas":0.02,"dining":0.01,"transit":0.01,"recurring":0.01,"travel":0.02,"other":0.01},"caps_struct":[]},{"id":"amex_platinum","name":"The Platinum Card","issuer":"American Express","link":null,"annual_fee":799,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":0.01,"gas":0.01,"dining":0.02,"transit":0.01,"recurring":0.01,"travel":0.02,"other":0.01},"caps_struct":[]},{"id":"amex_simplycash","name":"SimplyCash Card from American Express","issuer":"American Express","link":null,"annual_fee":null,"first_year_fee":null,"tags":["cash-back"],"earn":{"grocery":0.02,"gas":0.02,"dining":0.0125,"transit":0.0125,"recurring":0.0125,"travel":0.0125,"other":0.0125},"caps_struct":[{"categories":["grocery","gas"],"annual_spend_limit":15000,"rate_after":0.0125}]},{"id":"amex_simplycash_preferred","name":"SimplyCash Preferred Card from American Express","issuer":"American Express","link":null,"annual_fee":null,"first_year_fee":null,"tags":["cash-back"],"earn":{"grocery":0.04,"gas":0.04,"dining":0.02,"transit":0.02,"recurring":0.02,"travel":0.02,"other":0.02},"caps_struct":[{"categories":["grocery","gas"],"annual_spend_limit":30000,"rate_after":0.02}]},{"id":"bmo_ascend_we","name":"BMO Ascend World Elite Mastercard","issuer":"BMO","link":null,"annual_fee":150,"first_year_fee":0,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"bmo_blue_rewards_we","name":"BMO Blue Rewards World Elite Mastercard (formerly BMO AIR MILES World Elite)","issuer":"BMO","link":null,"annual_fee":150,"first_year_fee":0,"tags":["travel"],"earn":{"grocery":0.013333,"gas":0.013333,"dining":0.006667,"transit":0.006667,"recurring":0.006667,"travel":0.006667,"other":0.006667},"caps_struct":[{"categories":["grocery"],"annual_spend_limit":5000,"rate_after":0.006667},{"categories":["gas"],"annual_spend_limit":5000,"rate_after":0.006667},{"categories":["dining","transit","recurring","travel","other"],"annual_spend_limit":10000,"rate_after":0.0}]},{"id":"bmo_cashback","name":"BMO CashBack Mastercard","issuer":"BMO","link":null,"annual_fee":0,"first_year_fee":null,"tags":["cash-back","no-fee"],"earn":{"grocery":0.03,"gas":0.005,"dining":0.005,"transit":0.005,"recurring":0.01,"travel":0.005,"other":0.005},"caps_struct":[{"categories":["grocery"],"annual_spend_limit":6000,"rate_after":0.005},{"categories":["recurring"],"annual_spend_limit":6000,"rate_after":0.005}]},{"id":"bmo_cashback_student","name":"Student BMO CashBack Mastercard","issuer":"BMO","link":null,"annual_fee":0,"first_year_fee":null,"tags":["cash-back","no-fee","student"],"earn":{"grocery":0.03,"gas":0.005,"dining":0.005,"transit":0.005,"recurring":0.01,"travel":0.005,"other":0.005},"caps_struct":[{"categories":["grocery"],"annual_spend_limit":6000,"rate_after":0.005},{"categories":["recurring"],"annual_spend_limit":6000,"rate_after":0.005}]},{"id":"bmo_cashback_world_elite","name":"BMO CashBack World Elite Mastercard","issuer":"BMO","link":null,"annual_fee":139,"first_year_fee":0,"tags":["cash-back"],"earn":{"grocery":0.05,"gas":0.03,"dining":0.01,"transit":0.04,"recurring":0.02,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["grocery"],"annual_spend_limit":6000,"rate_after":0.01},{"categories":["transit"],"annual_spend_limit":3600,"rate_after":0.01},{"categories":["gas"],"annual_spend_limit":3600,"rate_after":0.01},{"categories":["recurring"],"annual_spend_limit":6000,"rate_after":0.01}]},{"id":"bmo_eclipse_vi","name":"BMO eclipse Visa Infinite Card","issuer":"BMO","link":null,"annual_fee":120,"first_year_fee":0,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"bmo_eclipse_vip","name":"BMO eclipse Visa Infinite Privilege Card","issuer":"BMO","link":null,"annual_fee":599,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":0.033333,"gas":0.033333,"dining":0.033333,"transit":0.006667,"recurring":0.006667,"travel":0.033333,"other":0.006667},"caps_struct":[]},{"id":"bmo_preferred_rate","name":"BMO Preferred Rate Mastercard","issuer":"BMO","link":null,"annual_fee":29,"first_year_fee":null,"tags":["low-interest"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"brim_world_elite","name":"Brim World Elite Mastercard","issuer":"Brim Financial","link":null,"annual_fee":89,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":0.01,"gas":0.01,"dining":0.01,"transit":0.01,"recurring":0.01,"travel":0.01,"other":0.01},"caps_struct":[]},{"id":"capital_one_secured","name":"Capital One Guaranteed Secured Mastercard","issuer":"Capital One","link":null,"annual_fee":null,"first_year_fee":null,"tags":["secured"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"cibc_aeroplan_vi","name":"CIBC Aeroplan Visa Infinite Card","issuer":"CIBC","link":null,"annual_fee":139,"first_year_fee":0,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"cibc_aeroplan_vip","name":"CIBC Aeroplan Visa Infinite Privilege Card","issuer":"CIBC","link":null,"annual_fee":599,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"cibc_aventura_vi","name":"CIBC Aventura Visa Infinite Card","issuer":"CIBC","link":null,"annual_fee":139,"first_year_fee":0,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"cibc_aventura_vip","name":"CIBC Aventura Visa Infinite Privilege Card","issuer":"CIBC","link":null,"annual_fee":499,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"cibc_dividend","name":"CIBC Dividend Visa Card","issuer":"CIBC","link":null,"annual_fee":0,"first_year_fee":null,"tags":["cash-back","no-fee"],"earn":{"grocery":0.02,"gas":0.01,"dining":0.01,"transit":0.01,"recurring":0.01,"travel":0.01,"other":0.005},"caps_struct":[]},{"id":"cibc_dividend_student","name":"CIBC Dividend Visa Card for Students","issuer":"CIBC","link":null,"annual_fee":0,"first_year_fee":null,"tags":["cash-back","no-fee","student"],"earn":{"grocery":0.02,"gas":0.01,"dining":0.01,"transit":0.01,"recurring":0.01,"travel":0.01,"other":0.005},"caps_struct":[]},{"id":"cibc_dividend_vi","name":"CIBC Dividend Visa Infinite Card","issuer":"CIBC","link":null,"annual_fee":120,"first_year_fee":0,"tags":["cash-back"],"earn":{"grocery":0.04,"gas":0.04,"dining":0.02,"transit":0.02,"recurring":0.02,"travel":0.02,"other":0.01},"caps_struct":[]},{"id":"cibc_select","name":"CIBC Select Visa Card","issuer":"CIBC","link":null,"annual_fee":29,"first_year_fee":0,"tags":[],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"desjardins_odyssey_vip","name":"Desjardins Odyssey Visa Infinite Privilege Card","issuer":"Desjardins","link":null,"annual_fee":395,"first_year_fee":null,"tags":["travel","low-interest"],"earn":{"grocery":0.03,"gas":0.015,"dining":0.04,"transit":0.04,"recurring":0.015,"travel":0.03,"other":0.015},"caps_struct":[{"categories":["travel"],"annual_spend_limit":25000,"rate_after":0.015}]},{"id":"desjardins_odyssey_we","name":"Desjardins Odyssey World Elite Mastercard","issuer":"Desjardins","link":null,"annual_fee":130,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":0.03,"gas":0.01,"dining":0.03,"transit":0.02,"recurring":0.01,"travel":0.02,"other":0.01},"caps_struct":[{"categories":["grocery"],"annual_spend_limit":10000,"rate_after":0.01},{"categories":["dining"],"annual_spend_limit":6000,"rate_after":0.01},{"categories":["travel"],"annual_spend_limit":20000,"rate_after":0.01}]},{"id":"home_trust_secured","name":"Home Trust Secured Visa","issuer":"Home Trust Company","link":null,"annual_fee":0,"first_year_fee":null,"tags":["secured"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"mbna_rewards_we","name":"MBNA Rewards World Elite Mastercard","issuer":"MBNA","link":null,"annual_fee":120,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":0.05,"gas":0.01,"dining":0.05,"transit":0.01,"recurring":0.05,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["grocery"],"annual_spend_limit":50000,"rate_after":0.01},{"categories":["dining"],"annual_spend_limit":50000,"rate_after":0.01},{"categories":["recurring"],"annual_spend_limit":50000,"rate_after":0.01}]},{"id":"mbna_true_line","name":"MBNA True Line Mastercard","issuer":"MBNA (TD)","link":null,"annual_fee":0,"first_year_fee":null,"tags":["low-interest"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"nbc_mycredit","name":"National Bank mycredit Mastercard","issuer":"National Bank","link":null,"annual_fee":null,"first_year_fee":null,"tags":["cash-back"],"earn":{"grocery":0.005,"gas":0.005,"dining":0.01,"transit":0.005,"recurring":0.01,"travel":0.005,"other":0.005},"caps_struct":[]},{"id":"nbc_world_elite","name":"National Bank World Elite Mastercard","issuer":"National Bank","link":null,"annual_fee":150,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"neo_secured","name":"Neo Secured Mastercard (secured versions of Neo cards)","issuer":"Neo Financial","link":null,"annual_fee":null,"first_year_fee":null,"tags":["cash-back","secured"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"neo_world_elite","name":"Neo World Elite Mastercard","issuer":"Neo Financial","link":null,"annual_fee":149,"first_year_fee":null,"tags":["cash-back"],"earn":{"grocery":0.05,"gas":0.03,"dining":0.01,"transit":0.01,"recurring":0.04,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["grocery"],"annual_spend_limit":12000,"rate_after":0.01},{"categories":["gas"],"annual_spend_limit":12000,"rate_after":0.01},{"categories":["recurring"],"annual_spend_limit":6000,"rate_after":0.01}]},{"id":"pc_mastercard","name":"PC Mastercard","issuer":"President's Choice Bank (PC Financial)","link":null,"annual_fee":0,"first_year_fee":null,"tags":["travel","no-fee"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"pc_world_elite","name":"PC World Elite Mastercard","issuer":"President's Choice Bank (PC Financial)","link":null,"annual_fee":0,"first_year_fee":null,"tags":["travel","no-fee"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"rbc_avion_vi","name":"RBC Avion Visa Infinite","issuer":"RBC","link":null,"annual_fee":120,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":0.01,"gas":0.01,"dining":0.01,"transit":0.01,"recurring":0.01,"travel":0.0125,"other":0.01},"caps_struct":[]},{"id":"rbc_avion_vip","name":"RBC Avion Visa Infinite Privilege","issuer":"RBC","link":null,"annual_fee":399,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":0.0125,"gas":0.0125,"dining":0.0125,"transit":0.0125,"recurring":0.0125,"travel":0.0125,"other":0.0125},"caps_struct":[]},{"id":"rbc_cash_back","name":"RBC Cash Back Mastercard","issuer":"RBC","link":null,"annual_fee":0,"first_year_fee":null,"tags":["cash-back","no-fee"],"earn":{"grocery":0.02,"gas":0.01,"dining":0.005,"transit":0.01,"recurring":0.005,"travel":0.005,"other":0.005},"caps_struct":[]},{"id":"rbc_visa_classic_low_rate","name":"RBC Visa Classic Low Rate Option","issuer":"RBC","link":null,"annual_fee":20,"first_year_fee":0,"tags":["low-interest"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"rbc_westjet_we","name":"WestJet RBC World Elite Mastercard","issuer":"RBC","link":null,"annual_fee":139,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":0.02,"gas":0.02,"dining":0.015,"transit":0.02,"recurring":0.015,"travel":0.015,"other":0.015},"caps_struct":[]},{"id":"scotia_gold_amex","name":"Scotiabank Gold American Express Card","issuer":"Scotiabank","link":null,"annual_fee":120,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"scotia_momentum_no_fee","name":"Scotia Momentum No-Fee Visa Card","issuer":"Scotiabank","link":null,"annual_fee":0,"first_year_fee":null,"tags":["cash-back","no-fee"],"earn":{"grocery":0.01,"gas":0.01,"dining":0.005,"transit":0.01,"recurring":0.01,"travel":0.005,"other":0.005},"caps_struct":[{"categories":["grocery","gas","transit","recurring"],"annual_spend_limit":15000,"rate_after":0.005}]},{"id":"scotia_momentum_vi","name":"Scotia Momentum Visa Infinite Card","issuer":"Scotiabank","link":null,"annual_fee":120,"first_year_fee":0,"tags":["cash-back"],"earn":{"grocery":0.04,"gas":0.02,"dining":0.01,"transit":0.02,"recurring":0.04,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["grocery","recurring"],"annual_spend_limit":25000,"rate_after":0.01},{"categories":["gas","transit"],"annual_spend_limit":25000,"rate_after":0.01}]},{"id":"scotia_passport_vi","name":"Scotiabank Passport Visa Infinite Card","issuer":"Scotiabank","link":null,"annual_fee":150,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"scotia_platinum_amex","name":"Scotiabank Platinum American Express Card","issuer":"Scotiabank","link":null,"annual_fee":399,"first_year_fee":null,"tags":["travel","low-interest"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"scotia_value","name":"Scotiabank Value Visa Card","issuer":"Scotiabank","link":null,"annual_fee":29,"first_year_fee":0,"tags":["low-interest"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"simplii_cash_back","name":"Simplii Financial Cash Back Visa Card","issuer":"Simplii Financial","link":null,"annual_fee":0,"first_year_fee":null,"tags":["cash-back","no-fee"],"earn":{"grocery":0.015,"gas":0.015,"dining":0.04,"transit":0.005,"recurring":0.015,"travel":0.005,"other":0.005},"caps_struct":[{"categories":["dining"],"annual_spend_limit":5000,"rate_after":0.005},{"categories":["grocery","gas","recurring"],"annual_spend_limit":15000,"rate_after":0.005}]},{"id":"tangerine_money_back","name":"Tangerine Money-Back Credit Card (2% on groceries and recurring bills, the two categories chosen in our profiles)","issuer":"Tangerine","link":null,"annual_fee":0,"first_year_fee":null,"tags":["cash-back","no-fee"],"earn":{"grocery":0.02,"gas":0.005,"dining":0.005,"transit":0.005,"recurring":0.02,"travel":0.005,"other":0.005},"caps_struct":[]},{"id":"tangerine_world","name":"Tangerine Money-Back World Mastercard (2% on groceries and recurring bills, the two categories chosen in our profiles)","issuer":"Tangerine","link":null,"annual_fee":0,"first_year_fee":null,"tags":["cash-back","no-fee"],"earn":{"grocery":0.02,"gas":0.005,"dining":0.005,"transit":0.005,"recurring":0.02,"travel":0.005,"other":0.005},"caps_struct":[]},{"id":"td_aeroplan_vi","name":"TD Aeroplan Visa Infinite Card","issuer":"TD","link":null,"annual_fee":139,"first_year_fee":0,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"td_aeroplan_vip","name":"TD Aeroplan Visa Infinite Privilege Card","issuer":"TD","link":null,"annual_fee":599,"first_year_fee":null,"tags":["travel"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"td_cash_back","name":"TD Cash Back Visa Card","issuer":"TD","link":null,"annual_fee":0,"first_year_fee":null,"tags":["cash-back","no-fee"],"earn":{"grocery":0.01,"gas":0.01,"dining":0.005,"transit":0.01,"recurring":0.01,"travel":0.005,"other":0.005},"caps_struct":[{"categories":["grocery"],"annual_spend_limit":5000,"rate_after":0.005},{"categories":["gas"],"annual_spend_limit":5000,"rate_after":0.005},{"categories":["transit"],"annual_spend_limit":5000,"rate_after":0.005},{"categories":["recurring"],"annual_spend_limit":5000,"rate_after":0.005}]},{"id":"td_cash_back_vi","name":"TD Cash Back Visa Infinite Card","issuer":"TD","link":null,"annual_fee":139,"first_year_fee":0,"tags":["cash-back"],"earn":{"grocery":0.03,"gas":0.03,"dining":0.01,"transit":0.03,"recurring":0.03,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["grocery"],"annual_spend_limit":15000,"rate_after":0.01},{"categories":["gas"],"annual_spend_limit":15000,"rate_after":0.01},{"categories":["transit"],"annual_spend_limit":15000,"rate_after":0.01},{"categories":["recurring"],"annual_spend_limit":15000,"rate_after":0.01}]},{"id":"td_first_class_vi","name":"TD First Class Travel Visa Infinite Card","issuer":"TD","link":null,"annual_fee":139,"first_year_fee":0,"tags":["travel"],"earn":{"grocery":0.03,"gas":0.01,"dining":0.03,"transit":0.03,"recurring":0.02,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["grocery"],"annual_spend_limit":25000,"rate_after":0.01},{"categories":["dining"],"annual_spend_limit":25000,"rate_after":0.01},{"categories":["transit"],"annual_spend_limit":25000,"rate_after":0.01},{"categories":["recurring"],"annual_spend_limit":25000,"rate_after":0.01}]},{"id":"td_low_rate","name":"TD Low Rate Visa Card","issuer":"TD","link":null,"annual_fee":25,"first_year_fee":0,"tags":["low-interest"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"td_business_travel_visa","name":"TD Business Travel Visa Card","issuer":"TD","link":null,"annual_fee":149,"first_year_fee":0,"tags":["business"],"earn":{"grocery":0.01,"gas":0.01,"dining":0.03,"transit":0.01,"recurring":0.03,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["dining"],"annual_spend_limit":80000,"rate_after":0.01},{"categories":["recurring"],"annual_spend_limit":80000,"rate_after":0.01}]},{"id":"td_aeroplan_visa_business","name":"TD Aeroplan Visa Business Card","issuer":"TD","link":null,"annual_fee":149,"first_year_fee":0,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"td_business_cash_back_visa","name":"TD Business Cash Back Visa Card","issuer":"TD","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.005,"gas":0.02,"dining":0.005,"transit":0.02,"recurring":0.02,"travel":0.005,"other":0.005},"caps_struct":[{"categories":["gas","transit"],"annual_spend_limit":15000,"rate_after":0.005},{"categories":["recurring"],"annual_spend_limit":15000,"rate_after":0.005}]},{"id":"td_business_select_rate_visa","name":"TD Business Select Rate Visa Card","issuer":"TD","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"rbc_avion_vi_business","name":"RBC Avion Visa Infinite Business","issuer":"RBC","link":null,"annual_fee":175,"first_year_fee":0,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"rbc_avion_visa_business","name":"RBC Avion Visa Business","issuer":"RBC","link":null,"annual_fee":120,"first_year_fee":0,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"rbc_visa_business","name":"RBC Visa Business","issuer":"RBC","link":null,"annual_fee":12,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"rbc_business_cash_back_mc","name":"RBC Business Cash Back Mastercard","issuer":"RBC","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.01,"gas":0.01,"dining":0.01,"transit":0.01,"recurring":0.01,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["grocery","gas","dining","transit","recurring","travel","other"],"annual_spend_limit":65000,"rate_after":0.0}]},{"id":"rbc_westjet_we_business","name":"WestJet RBC World Elite Mastercard for Business","issuer":"RBC","link":null,"annual_fee":175,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"cibc_aventura_visa_business","name":"CIBC Aventura Visa Card for Business","issuer":"CIBC","link":null,"annual_fee":139,"first_year_fee":0,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"cibc_aventura_visa_business_plus","name":"CIBC Aventura Visa Card for Business Plus","issuer":"CIBC","link":null,"annual_fee":139,"first_year_fee":0,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"cibc_aeroplan_visa_business","name":"CIBC Aeroplan Visa Business Card","issuer":"CIBC","link":null,"annual_fee":180,"first_year_fee":0,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"cibc_aeroplan_visa_business_plus","name":"CIBC Aeroplan Visa Business Plus Card","issuer":"CIBC","link":null,"annual_fee":139,"first_year_fee":0,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"cibc_bizline_visa","name":"CIBC bizline Visa Card","issuer":"CIBC","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"cibc_costco_business_mc","name":"CIBC Costco Business Mastercard","issuer":"CIBC","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.01,"gas":0.02,"dining":0.03,"transit":0.01,"recurring":0.01,"travel":0.01,"other":0.01},"caps_struct":[]},{"id":"cibc_corporate_classic_plus","name":"CIBC Corporate Classic Plus Visa Card","issuer":"CIBC","link":null,"annual_fee":20,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"scotia_momentum_business","name":"Scotia Momentum for business Visa Card","issuer":"Scotiabank","link":null,"annual_fee":79,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.01,"gas":0.03,"dining":0.03,"transit":0.01,"recurring":0.03,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["gas","dining","recurring"],"annual_spend_limit":40000,"rate_after":0.01}]},{"id":"scotia_momentum_business_no_fee","name":"Scotia Momentum for business No Fee Visa Card","issuer":"Scotiabank","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.01,"gas":0.01,"dining":0.01,"transit":0.01,"recurring":0.01,"travel":0.01,"other":0.01},"caps_struct":[]},{"id":"scotia_passport_vi_business","name":"Scotiabank Passport Visa Infinite Business Card","issuer":"Scotiabank","link":null,"annual_fee":199,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"scotia_home_hardware_pro_business","name":"Scotia Home Hardware PRO Visa Business Card","issuer":"Scotiabank","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"scotialine_business_visa","name":"ScotiaLine for business Visa Credit Card","issuer":"Scotiabank","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"bmo_cashback_we_business","name":"BMO CashBack World Elite Business Mastercard","issuer":"BMO","link":null,"annual_fee":175,"first_year_fee":0,"tags":["business"],"earn":{"grocery":0.0125,"gas":0.05,"dining":0.0125,"transit":0.0125,"recurring":0.04,"travel":0.0125,"other":0.0125},"caps_struct":[]},{"id":"bmo_cashback_business","name":"BMO CashBack Business Mastercard","issuer":"BMO","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.0075,"gas":0.015,"dining":0.0075,"transit":0.0075,"recurring":0.0075,"travel":0.0075,"other":0.0075},"caps_struct":[]},{"id":"bmo_ascend_we_business","name":"BMO Ascend World Elite Business Mastercard","issuer":"BMO","link":null,"annual_fee":175,"first_year_fee":0,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"bmo_ascend_business","name":"BMO Ascend Business Mastercard","issuer":"BMO","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"bmo_blue_rewards_we_business","name":"BMO Blue Rewards World Elite Business Mastercard","issuer":"BMO","link":null,"annual_fee":175,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.008333,"gas":0.016667,"dining":0.008333,"transit":0.008333,"recurring":0.008333,"travel":0.008333,"other":0.008333},"caps_struct":[]},{"id":"bmo_blue_rewards_business","name":"BMO Blue Rewards Business Mastercard","issuer":"BMO","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.006667,"gas":0.013333,"dining":0.006667,"transit":0.006667,"recurring":0.006667,"travel":0.006667,"other":0.006667},"caps_struct":[]},{"id":"amex_business_platinum","name":"Business Platinum Card from American Express","issuer":"American Express","link":null,"annual_fee":799,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"amex_aeroplan_business_reserve","name":"American Express Aeroplan Business Reserve Card","issuer":"American Express","link":null,"annual_fee":599,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"amex_business_gold","name":"American Express Business Gold Rewards Card","issuer":"American Express","link":null,"annual_fee":null,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"amex_marriott_bonvoy_business","name":"Marriott Bonvoy Business American Express Card","issuer":"American Express","link":null,"annual_fee":null,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"nbc_platinum_business_mc","name":"National Bank Platinum Business Mastercard","issuer":"National Bank","link":null,"annual_fee":125,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"nbc_business_mc","name":"National Bank Business Mastercard","issuer":"National Bank","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.0,"gas":0.0,"dining":0.0,"transit":0.0,"recurring":0.0,"travel":0.0,"other":0.0},"caps_struct":[]},{"id":"nbc_business_line_mc","name":"National Bank Business Line Mastercard","issuer":"National Bank","link":null,"annual_fee":50,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"nbc_corporate_mc","name":"National Bank Corporate Mastercard","issuer":"National Bank","link":null,"annual_fee":35,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"desjardins_visa_business","name":"Desjardins Visa Business Card","issuer":"Desjardins","link":null,"annual_fee":60,"first_year_fee":0,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"desjardins_visa_business_advantage","name":"Desjardins Visa Business Advantage","issuer":"Desjardins","link":null,"annual_fee":25,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"desjardins_visa_business_freedom","name":"Desjardins Visa Business Freedom Solutions","issuer":"Desjardins","link":null,"annual_fee":204,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"desjardins_visa_corporate","name":"Desjardins Visa Corporate Card","issuer":"Desjardins","link":null,"annual_fee":20,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"float","name":"Float corporate cards","issuer":"Float","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"loop","name":"Loop corporate cards","issuer":"Loop","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":null,"gas":null,"dining":null,"transit":null,"recurring":null,"travel":null,"other":null},"caps_struct":[]},{"id":"venn","name":"Venn Mastercard Charge Card","issuer":"Venn","link":null,"annual_fee":0,"first_year_fee":null,"tags":["business"],"earn":{"grocery":0.01,"gas":0.01,"dining":0.01,"transit":0.01,"recurring":0.01,"travel":0.01,"other":0.01},"caps_struct":[{"categories":["grocery","gas","dining","transit","recurring","travel","other"],"annual_spend_limit":60000,"rate_after":0.0}]}],"sales_tax":{"AB":{"gst":0.05,"hst":null,"pst":0,"label":null},"BC":{"gst":0.05,"hst":null,"pst":0.07,"label":"PST"},"MB":{"gst":0.05,"hst":null,"pst":0.07,"label":"RST"},"NB":{"gst":null,"hst":0.15,"pst":null,"label":"HST"},"NL":{"gst":null,"hst":0.15,"pst":null,"label":"HST"},"NS":{"gst":null,"hst":0.14,"pst":null,"label":"HST"},"NT":{"gst":0.05,"hst":null,"pst":0,"label":null},"NU":{"gst":0.05,"hst":null,"pst":0,"label":null},"ON":{"gst":null,"hst":0.13,"pst":null,"label":"HST"},"PE":{"gst":null,"hst":0.15,"pst":null,"label":"HST"},"QC":{"gst":0.05,"hst":null,"pst":0.09975,"label":"QST"},"SK":{"gst":0.05,"hst":null,"pst":0.06,"label":"PST"},"YT":{"gst":0.05,"hst":null,"pst":0,"label":null}},"cpi":{"annual":{"1914":6.0,"1915":6.1,"1916":6.7,"1917":7.9,"1918":8.9,"1919":9.8,"1920":11.4,"1921":10.0,"1922":9.2,"1923":9.2,"1924":9.0,"1925":9.1,"1926":9.2,"1927":9.1,"1928":9.1,"1929":9.2,"1930":9.1,"1931":8.2,"1932":7.5,"1933":7.1,"1934":7.2,"1935":7.3,"1936":7.4,"1937":7.7,"1938":7.7,"1939":7.7,"1940":8.0,"1941":8.5,"1942":8.8,"1943":9.0,"1944":9.1,"1945":9.2,"1946":9.4,"1947":10.3,"1948":11.8,"1949":12.2,"1950":12.5,"1951":13.8,"1952":14.2,"1953":14.0,"1954":14.1,"1955":14.1,"1956":14.3,"1957":14.8,"1958":15.2,"1959":15.3,"1960":15.5,"1961":15.7,"1962":15.9,"1963":16.1,"1964":16.4,"1965":16.8,"1966":17.5,"1967":18.1,"1968":18.8,"1969":19.7,"1970":20.3,"1971":20.9,"1972":21.9,"1973":23.6,"1974":26.2,"1975":29.0,"1976":31.1,"1977":33.6,"1978":36.6,"1979":40.0,"1980":44.0,"1981":49.5,"1982":54.9,"1983":58.1,"1984":60.6,"1985":63.0,"1986":65.6,"1987":68.5,"1988":71.2,"1989":74.8,"1990":78.4,"1991":82.8,"1992":84.0,"1993":85.6,"1994":85.7,"1995":87.6,"1996":88.9,"1997":90.4,"1998":91.3,"1999":92.9,"2000":95.4,"2001":97.8,"2002":100.0,"2003":102.8,"2004":104.7,"2005":107.0,"2006":109.1,"2007":111.5,"2008":114.1,"2009":114.4,"2010":116.5,"2011":119.9,"2012":121.7,"2013":122.8,"2014":125.2,"2015":126.6,"2016":128.4,"2017":130.4,"2018":133.4,"2019":136.0,"2020":137.0,"2021":141.6,"2022":151.2,"2023":157.1,"2024":160.9,"2025":164.2},"monthly":{"2025-01":161.3,"2025-02":163.0,"2025-03":163.5,"2025-04":163.4,"2025-05":164.3,"2025-06":164.4,"2025-07":164.9,"2025-08":164.8,"2025-09":164.9,"2025-10":165.3,"2025-11":165.4,"2025-12":165.0,"2026-01":165.0,"2026-02":165.9,"2026-03":167.4,"2026-04":168.0,"2026-05":169.6,"2026-06":169.0,"2026-07":169.9,"2026-08":169.8,"2026-09":170.0},"latest_month":"2026-09"},"ei_parental":{"maternity_weeks":15,"standard_weeks":35,"extended_weeks":61,"shared_standard_weeks":40,"shared_extended_weeks":69,"standard_rate":0.55,"extended_rate":0.33,"max_weekly_standard":729.0,"max_weekly_extended":437},"cdcp":{"income_limit":90000,"tiers":[[70000,0.0],[80000,0.4],[90000,0.6]],"groups_note":"Applications for the 2026-2027 benefit period are open to every eligible resident who meets all four requirements."},"chequing":[{"name":"EQ Bank Personal Account","link":"/reviews/eq-bank/","fee":0,"fee_text":"$0","waive_bal":null,"rate":0.01},{"name":"Wealthsimple Chequing","link":"/reviews/wealthsimple/chequing/","fee":0,"fee_text":"$0","waive_bal":null,"rate":0.0125},{"name":"Manulife Bank Advantage Account","link":null,"fee":0,"fee_text":"$0; transaction fees below a $1,000 balance","waive_bal":1000,"rate":0.0165},{"name":"KOHO Essential","link":"/reviews/koho/","fee":0,"fee_text":"$7 a month, $0 with direct deposit or $1,000 a month in deposits","waive_bal":null,"rate":0.02},{"name":"Simplii No Fee Chequing Account","link":"/reviews/simplii/","fee":0,"fee_text":"$0","waive_bal":null,"rate":0.0},{"name":"Tangerine No-Fee Daily Chequing Account","link":"/reviews/tangerine/","fee":0,"fee_text":"$0","waive_bal":null,"rate":0.0},{"name":"PC Money Account","link":null,"fee":0,"fee_text":"$0","waive_bal":null,"rate":0.0},{"name":"Neo Chequing","link":"/reviews/neo-financial/","fee":0,"fee_text":"$0","waive_bal":null,"rate":0.0},{"name":"National Bank The Connected","link":null,"fee":15.95,"fee_text":"$15.95 a month, $0 with a $4,500 balance","waive_bal":4500,"rate":0.0},{"name":"TD Unlimited Chequing Account","link":null,"fee":17.95,"fee_text":"$17.95 a month, $0 with a $4,000 daily balance","waive_bal":4000,"rate":0.0},{"name":"BMO Performance Chequing","link":null,"fee":17.95,"fee_text":"$17.95 a month, $0 with a $4,000 daily balance ($4,500 from February 1, 2027)","waive_bal":4000,"rate":0.0},{"name":"CIBC Smart Account","link":null,"fee":16.95,"fee_text":"$16.95 a month, rebate with $4,000 every day","waive_bal":4000,"rate":0.0},{"name":"Scotiabank Preferred Package","link":null,"fee":16.95,"fee_text":"$16.95 a month, $0 with $4,000 every day or recurring mortgage payments","waive_bal":4000,"rate":0.0},{"name":"National Bank The Minimalist","link":null,"fee":3.95,"fee_text":"$3.95 a month (ages 25 and up)","waive_bal":null,"rate":0.0},{"name":"CIBC Everyday Chequing Account","link":null,"fee":4.0,"fee_text":"$4 a month","waive_bal":null,"rate":0.0},{"name":"Scotiabank Basic Bank Account","link":null,"fee":3.95,"fee_text":"$3.95 a month","waive_bal":null,"rate":0.0},{"name":"BMO Practical Chequing","link":null,"fee":4.0,"fee_text":"$4 a month","waive_bal":null,"rate":0.0},{"name":"RBC Day to Day Banking","link":null,"fee":4.0,"fee_text":"$4 a month","waive_bal":null,"rate":0.0},{"name":"TD Minimum Chequing Account","link":null,"fee":3.95,"fee_text":"$3.95 a month","waive_bal":null,"rate":0.0},{"name":"RBC Signature No Limit Banking","link":null,"fee":16.95,"fee_text":"$16.95 a month","waive_bal":null,"rate":0.0}],"hisa":[{"name":"Saven High Interest Savings","rate":0.03,"ins":"Not stated"},{"name":"Oaken Savings Account","link":"/reviews/oaken-financial/","rate":0.03,"ins":"CDIC"},{"name":"EQ Bank 30 Day Notice Savings","link":"/reviews/eq-bank/","rate":0.0275,"rate_note":"30 days' notice to withdraw","ins":"CDIC"},{"name":"Hubert High Interest Savings","rate":0.0275,"ins":"Deposit Guarantee Corporation of Manitoba"},{"name":"Wealthsimple Savings","link":"/reviews/wealthsimple/","rate":0.025,"ins":"CIPF, not CDIC"},{"name":"Neo Savings (Essentials)","link":"/reviews/neo-financial/","rate":0.0225,"ins":"Eligible for CDIC (institution not named)"},{"name":"Outlook High Interest Savings","rate":0.022,"ins":"Deposit Guarantee Corporation of Manitoba"},{"name":"KOHO Essential","link":"/reviews/koho/","rate":0.02,"rate_note":"$7 a month plan, $0 with direct deposit","ins":"CDIC through partner institutions (opt-in)"},{"name":"Manulife Bank Advantage Account","rate":0.0165,"ins":"CDIC"},{"name":"Peoples Trust e-Savings","rate":0.012,"ins":"CDIC"},{"name":"Alterna High Interest eSavings","rate":0.0105,"ins":"CDIC"},{"name":"EQ Bank Personal Account","link":"/reviews/eq-bank/","rate":0.01,"rate_note":"2.75% with pay direct deposit","ins":"CDIC"},{"name":"RBC High Interest eSavings","rate":0.0065,"ins":"CDIC"},{"name":"National Bank High Interest Savings","rate":0.0065,"ins":"CDIC"},{"name":"Scotia MomentumPLUS Savings","rate":0.004,"rate_note":"base rate","ins":"CDIC"},{"name":"Simplii High Interest Savings","link":"/reviews/simplii/","rate":0.003,"rate_note":"up to $50,000","ins":"CDIC"}],"usd_savings":[{"name":"EQ Bank US Dollar Account","link":"/reviews/eq-bank/","rate":0.025,"ins":"Not stated for USD on the product page"},{"name":"Manulife US Dollar Advantage Account","rate":0.002,"ins":"Not stated for USD on the product page"},{"name":"National Bank USD Progress Account","rate":0.001,"rate_note":"from $10,000","ins":"Not stated for USD on the product page"},{"name":"Scotia U.S. Dollar Daily Interest","rate":0.0005,"rate_note":"top tier","ins":"Not stated for USD on the product page"},{"name":"TD U.S. Daily Interest Chequing","rate":0.0001,"ins":"Not stated for USD on the product page"}],"gic_best":{"1":4.0,"2":4.3,"3":4.35,"4":4.4,"5":4.5},"gic_default_rate":4.0,"lif":{"year":2026,"ref":0.0349,"mb_ref":0.06,"jur":{"FED":{"from":20,"rates":[0.045331,0.045384,0.04544,0.0455,0.045564,0.045631,0.045703,0.045779,0.04586,0.045947,0.046038,0.046136,0.04624,0.046351,0.046469,0.046595,0.046729,0.046872,0.047025,0.047188,0.047361,0.047547,0.047745,0.047957,0.048184,0.048427,0.048687,0.048966,0.049265,0.049586,0.049931,0.050302,0.050701,0.051131,0.051595,0.052096,0.052637,0.053224,0.053861,0.054552,0.055304,0.056125,0.057022,0.058005,0.059084,0.060272,0.061586,0.063042,0.064662,0.066474,0.068508,0.070804,0.073413,0.076397,0.079836,0.083837,0.088423,0.093729,0.099935,0.107287,0.116128,0.126955,0.140512,0.15797,0.18128,0.213952,0.263008,0.344831,0.508575,1.0],"below":null,"plus":true,"basis":"dec31","kind":"pct","greater":false},"ON":{"from":41,"rates":[0.0598531,0.06006,0.0602808,0.0605167,0.0607687,0.0610382,0.0613265,0.061635,0.0619655,0.0623197,0.0626996,0.0631073,0.0635454,0.0640164,0.0645234,0.0650697,0.0656589,0.0662952,0.0669833,0.0677285,0.0685367,0.0694147,0.0703703,0.0714124,0.0725513,0.0737988,0.0751689,0.0766778,0.0783449,0.080193,0.0822496,0.084548,0.0871288,0.0900423,0.0933511,0.0971347,0.1014952,0.1065661,0.1125255,0.119616,0.1281773,0.1387002,0.1519207,0.1689953,0.1918515,0.2239589,0.2722561,0.3529338,0.5145631,1.0],"below":null,"plus":false,"basis":"attained","kind":"pct","greater":true},"BC":{"from":50,"rates":[0.0627,0.0631,0.0635,0.064,0.0645,0.0651,0.0657,0.0663,0.067,0.0677,0.0685,0.0694,0.0704,0.0714,0.0726,0.0738,0.0752,0.0767,0.0783,0.0802,0.0822,0.0845,0.0871,0.09,0.0934,0.0971,0.1015,0.1066,0.1125,0.1196,0.1282,0.1387,0.1519,0.169,0.1919,0.224,0.2723,0.3529,0.5146,1.0],"below":null,"plus":true,"basis":"jan1","kind":"pct","greater":true},"MB":{"from":55,"rates":[0.064,0.065,0.065,0.066,0.067,0.067,0.068,0.069,0.07,0.071,0.072,0.073,0.074,0.076,0.077,0.079,0.081,0.083,0.085,0.088,0.091,0.094,0.098,0.103,0.108,0.115,0.121,0.129,0.138,0.148,0.16,0.173,0.189,0.2],"below":0.061,"plus":true,"basis":"dec31","kind":"factor","greater":true},"NB":{"from":19,"rates":[0.0574696,0.0575224,0.0575784,0.057638,0.0577012,0.0577684,0.0578398,0.0579157,0.0579964,0.0580821,0.0581733,0.0582702,0.0583733,0.058483,0.0585998,0.058724,0.0588563,0.0589971,0.0591472,0.0593071,0.0594775,0.0596592,0.0598531,0.06006,0.0602808,0.0605167,0.0607687,0.0610382,0.0613265,0.061635,0.0619655,0.0623197,0.0626996,0.0631073,0.0635454,0.0640164,0.0645234,0.0650697,0.0656589,0.0662952,0.0669833,0.0677285,0.0685367,0.0694147,0.0703703,0.0714124,0.0725513,0.0737988,0.0751689,0.0766778,0.0783449,0.080193,0.0822496,0.084548,0.0871288,0.0900423,0.0933511,0.0971347,0.1014952,0.1065661,0.1125255,0.119616,0.1281773,0.1387002,0.1519207,0.1689953,0.1918515,0.2239589,0.2722561,0.3529338,0.5145631,1.0],"below":null,"plus":false,"basis":"attained","kind":"pct","greater":false},"NL":{"from":40,"rates":[0.0598531,0.06006,0.0602808,0.0605167,0.0607687,0.0610382,0.0613265,0.061635,0.0619655,0.0623197,0.0626996,0.0631073,0.0635454,0.0640164,0.0645234,0.0650697,0.0656589,0.0662952,0.0669833,0.0677285,0.0685367,0.0694147,0.0703703,0.0714124,0.0725513,0.0737988,0.0751689,0.0766778,0.0783449,0.080193,0.0822496,0.084548,0.0871288,0.0900423,0.0933511,0.0971347,0.1014952,0.1065661,0.1125255,0.119616,0.1281773,0.1387002,0.1519207,0.1689953,0.1918515,0.2239589,0.2722561,0.3529338,0.5145631,1.0],"below":null,"plus":true,"basis":"jan1","kind":"pct","greater":true},"QC":{"basis":"jan1","kind":"qc","age":55,"under":0.0625},"AB":null,"NS":null,"SK":null}},"brokers":[{"id":"wealthsimple","name":"Wealthsimple","review":"/reviews/wealthsimple/trade/","cad_trade":0,"us_trade":0,"usd_reg_text":"TFSA, FHSA, RRSP, spousal RRSP, LIRA and RESP: $10 a month on Core, included on Premium and Generation","annual_fee":0,"opt_base":0,"opt_contract":0,"opt_min":0,"opt_text":"$0 per contract on US equity and ETF options; Canadian-listed options $0 commission plus a $0.04 regulatory and exchange fee per contract","margin_cad":0.052,"margin_text":"5.20% Core, 4.70% Premium, 4.20% Generation","transfer_in_text":"Reimburses the other institution's transfer-out fee, up to $150 per account, on transfers of $25,000 or more","transfer_min":25000,"transfer_max":150,"per_client":false,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","joint","corporate","fractional","drip","zero_commission","usd_reg"],"score":4.2},{"id":"questrade","name":"Questrade","review":"/reviews/questrade/","cad_trade":0,"us_trade":0,"usd_reg_text":"USD held in registered accounts at no extra cost","annual_fee":0,"opt_base":0,"opt_contract":0,"opt_min":0,"opt_text":"$0 on US equity options; Canadian options $0.99 per contract","margin_cad":0.0895,"margin_text":"Prime + 4.25% under $100,000 (8.95%)","transfer_in_text":"Rebates the other institution's fee, up to $150 per account, on eligible transfers","transfer_min":null,"transfer_max":150,"per_client":false,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","joint","corporate","fractional","drip","zero_commission","usd_reg"],"score":4.4},{"id":"interactive-brokers","name":"Interactive Brokers Canada","review":"/reviews/interactive-brokers/","cad_trade":1.0,"us_trade":1.0,"usd_reg_text":"Not stated for registered accounts","annual_fee":0,"opt_base":0,"opt_contract":0.65,"opt_min":1.0,"opt_text":"US$0.65 per contract, minimum US$1","margin_cad":0.03631,"margin_text":"3.631% up to CAD 130,000 (IBKR Pro, as published; IBKR does not show the benchmark date, so the rate may predate the October 29, 2026 prime change)","transfer_in_text":null,"transfer_min":null,"transfer_max":null,"per_client":false,"cad_text":"CAD 0.01 a share, minimum CAD 1","us_text":"USD 0.005 a share, minimum USD 1","flags":["tfsa","rrsp","spousal","fhsa","rrif","margin","joint","corporate","fractional","drip"],"score":4.2},{"id":"moomoo","name":"moomoo Canada","review":"/reviews/moomoo/","cad_trade":1.49,"us_trade":1.99,"usd_reg_text":"TFSA and RRSP can hold CAD and USD; no fee stated","annual_fee":0,"opt_base":0,"opt_contract":0.65,"opt_min":1.0,"opt_text":"US$0.65 per contract, minimum US$1","margin_cad":0.0385,"margin_text":"From 3.85% (as of November 3, 2025)","transfer_in_text":"Promotion: typically reimburses $100 on transfers of $10,000 or more","transfer_min":10000,"transfer_max":100,"per_client":true,"cad_text":"CA$0.0149 a share, minimum CA$1.49","us_text":"US$0.0099 a share, minimum US$1.99","flags":["tfsa","rrsp","spousal","margin","usd_reg"],"score":3.7},{"id":"webull","name":"Webull Canada","review":"/reviews/webull/","cad_trade":0,"us_trade":0,"usd_reg_text":"Each Webull account comes with a USD and a CAD account; no USD account fee stated","annual_fee":8.4,"opt_base":0,"opt_contract":0.99,"opt_min":0,"opt_text":"US$0.99 per contract","margin_cad":null,"margin_text":"Prime + 3% under $100,000 (Webull's prime not published)","transfer_in_text":"Transfer bonus of $150 (terms not published)","transfer_min":null,"transfer_max":null,"per_client":true,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","margin","zero_commission","usd_reg"],"score":3.6},{"id":"qtrade","name":"Qtrade Direct Investing","review":"/reviews/qtrade/","cad_trade":0,"us_trade":0,"usd_reg_text":"RRSP, RRIF and TFSA: US$15 a quarter per account (free with Investor Plus)","annual_fee":0,"opt_base":0,"opt_contract":0.75,"opt_min":0,"opt_text":"$0.75 per contract","margin_cad":0.06,"margin_text":"Prime + 1.55% under $100,000 (6.00% at Qtrade's published prime of 4.45%, as of October 30, 2025)","transfer_in_text":"Fall Offer 2026: up to $150 per client on transfers of $15,000 or more","transfer_min":15000,"transfer_max":150,"per_client":true,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","joint","corporate","drip","zero_commission","usd_reg"],"score":4.0},{"id":"national-bank","name":"National Bank Direct Brokerage","review":"/reviews/national-bank-direct-brokerage/","cad_trade":0,"us_trade":0,"usd_reg_text":"TFSA, RRSP, RRIF, spousal RRSP and LIRA (not FHSA); no USD fee listed","annual_fee":0,"opt_base":0,"opt_contract":0.95,"opt_min":6.25,"opt_text":"$0.95 per contract, minimum $6.25 (November 7, 2026)","margin_cad":0.065,"margin_text":"6.50%","transfer_in_text":"Reimburses transfer fees depending on the amount invested (amount and minimum transfer not published)","transfer_min":null,"transfer_max":null,"per_client":true,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","corporate","drip","zero_commission","usd_reg"],"score":4.3},{"id":"cibc","name":"CIBC Investor's Edge","review":"/reviews/cibc-investors-edge/","cad_trade":6.95,"us_trade":6.95,"usd_reg_text":"Not stated","annual_fee":0,"opt_base":6.95,"opt_contract":1.25,"opt_min":0,"opt_text":"$6.95 + $1.25 per contract","margin_cad":0.065,"margin_text":"6.50% under $100,000","transfer_in_text":null,"transfer_min":null,"transfer_max":null,"per_client":false,"cad_text":"$6.95 ($0 under 25 with Smart Start)","us_text":"$6.95","flags":["tfsa","rrsp","fhsa","resp","rrif","lira","margin","joint","corporate","fractional","drip"],"score":3.0},{"id":"td","name":"TD Direct Investing","review":"/reviews/td-direct-investing/","cad_trade":9.99,"us_trade":9.99,"usd_reg_text":"TD Easy Trade: no fee for USD in TFSA and RRSP; TD Direct Investing not stated","annual_fee":0,"opt_base":9.99,"opt_contract":1.25,"opt_min":0,"opt_text":"$9.99 + $1.25 per contract","margin_cad":0.0675,"margin_text":"6.75%","transfer_in_text":"Reimburses up to $150 of the other institution's transfer fees on transfers of $25,000 or more","transfer_min":25000,"transfer_max":150,"per_client":true,"cad_text":"$9.99 (TD Easy Trade: 100 free trades a year)","us_text":"$9.99","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","joint","corporate","fractional","drip"],"score":2.8},{"id":"rbc","name":"RBC Direct Investing","review":"/reviews/rbc-direct-investing/","cad_trade":9.95,"us_trade":9.95,"usd_reg_text":"Accounts can hold CAD and USD; USD registered pricing not stated","annual_fee":0,"opt_base":9.95,"opt_contract":1.25,"opt_min":0,"opt_text":"$9.95 + $1.25 per contract","margin_cad":0.065,"margin_text":"6.50%","transfer_in_text":"Reimburses up to $200 of transfer fees on transfers of $15,000 or more","transfer_min":15000,"transfer_max":200,"per_client":true,"cad_text":"$9.95","us_text":"$9.95","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","joint","corporate","drip"],"score":2.8},{"id":"bmo","name":"BMO InvestorLine","review":"/reviews/bmo-investorline/","cad_trade":0,"us_trade":0,"usd_reg_text":"Not stated","annual_fee":0,"opt_base":0,"opt_contract":0.9,"opt_min":0,"opt_text":"$0.90 per contract","margin_cad":0.06,"margin_text":"6.00% (on BMO's published prime of 4.45%; rate sheet last updated December 10, 2025, not yet updated for the October 29, 2026 prime change)","transfer_in_text":null,"transfer_min":null,"transfer_max":null,"per_client":false,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","joint","corporate","drip","zero_commission"],"score":4.2},{"id":"scotia","name":"Scotia iTRADE","review":"/reviews/scotia-itrade/","cad_trade":9.99,"us_trade":9.99,"usd_reg_text":"All registered accounts except RESP have a USD side; no USD fee listed (FHSA not named individually)","annual_fee":0,"opt_base":9.99,"opt_contract":1.25,"opt_min":0,"opt_text":"$9.99 + $1.25 per contract","margin_cad":0.0635,"margin_text":"Prime + 1.65% under $25,000 (6.35%)","transfer_in_text":"Newcomers (StartRight): credit of up to $150","transfer_min":null,"transfer_max":null,"per_client":true,"cad_text":"$9.99","us_text":"$9.99","flags":["tfsa","rrsp","fhsa","resp","rrif","lira","margin","corporate","drip","usd_reg"],"score":3.0},{"id":"desjardins","name":"Desjardins Online Brokerage (Disnat)","review":"/reviews/desjardins-online-brokerage/","cad_trade":0,"us_trade":0,"usd_reg_text":"USD RRSP, TFSA, LIRA, RRIF and LIF; no fee stated","annual_fee":0,"opt_base":0,"opt_contract":1.25,"opt_min":8.75,"opt_text":"$1.25 per contract, minimum $8.75","margin_cad":0.0595,"margin_text":"Prime + 1.25% under $100,000 (5.95%)","transfer_in_text":"Asset consolidation offer for Quebec and Ontario residents (transfer requests November 2 to December 4, 2026): $150 per eligible transfer, minimum $5,000 combined","transfer_min":5000,"transfer_max":150,"per_client":false,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","corporate","zero_commission","usd_reg"],"score":4.3}],"robos":[{"name":"Questwealth Portfolios","review":"/reviews/questwealth/","tiers":[[99999.99,0.0025],[null,0.002]],"tier_mode":"flat","mer":0.0012,"mer_text":"up to 0.12% (standard portfolios)","fee_text":"0.25%; 0.20% from $100,000","min":250},{"name":"Wealthsimple Managed Investing","review":"/reviews/wealthsimple/managed-investing/","tiers":[[99999.99,0.005],[null,0.004]],"tier_mode":"flat","mer":0.0015,"mer_text":"up to 0.15% (Classic portfolios)","fee_text":"0.5% Core; 0.4% Premium ($100,000+); 0.4% falling to 0.2% at $10M+ on Generation","min":1},{"name":"RBC InvestEase","review":"/reviews/rbc-investease/","tiers":[[null,0.005]],"tier_mode":"flat","mer":0.002,"mer_text":"up to 0.20% (Core portfolios)","fee_text":"0.50% flat","min":100},{"name":"CI Direct Investing","review":null,"tiers":[[150000,0.006],[500000,0.004],[null,0.0035]],"tier_mode":"marginal","mer":0.0023,"mer_text":"up to 0.23% (ETF portfolios)","fee_text":"0.60% on the first $150,000; 0.40% on the next $350,000; 0.35% above $500,000","min":100},{"name":"BMO SmartFolio","review":"/reviews/bmo-smartfolio/","tiers":[[100000,0.007],[250000,0.006],[500000,0.005],[null,0.004]],"tier_mode":"marginal","mer":0.0035,"mer_text":"up to 0.35% (weighted average BMO says is likely 0.20% to 0.35%)","fee_text":"0.70% on the first $100,000; 0.60% on the next $150,000; 0.50% on the next $250,000; 0.40% on the next $500,000 (above $1,000,000 not published)","min":1000}],"crypto":[{"name":"NDAX","link":null,"fee_pct":0.002,"fee_text":"0.20% flat"},{"name":"Wealthsimple Crypto","link":"/reviews/wealthsimple/crypto/","fee_pct":0.005,"fee_text":"0.5% plus a spread (no spread on limit orders)"},{"name":"Kraken","link":"/reviews/kraken/","fee_pct":0.01,"fee_text":"1% on app instant buys; Kraken Pro 0.40% maker, 0.80% taker"},{"name":"Newton","link":"/reviews/newton/","fee_pct":0.0115,"fee_text":"Up to 1.15% on BTC, ETH and USDC; up to 1.60% on other coins"},{"name":"Coinbase Canada","link":"/reviews/coinbase/","fee_pct":null,"fee_text":"Varies by payment method and order size; spread included in the price"},{"name":"Shakepay","link":"/reviews/shakepay/","fee_pct":0.0125,"fee_text":"No commission; published spread of 0.5% to 2.0% (up to 1.5% more in volatile markets), scored at the 1.25% midpoint"},{"name":"Netcoins","link":null,"fee_pct":null,"fee_text":"No separate fee; spread of undisclosed size"},{"name":"Crypto.com","link":null,"fee_pct":null,"fee_text":"No app trading fee up to Level Up limits; spread may apply"},{"name":"Robinhood Canada (Coinsquare)","link":null,"fee_pct":0.0095,"fee_text":"0.95% of trade value on Robinhood Trading (from November 1, 2026)"}],"tax_software":[{"name":"Wealthsimple Tax","link":"/reviews/wealthsimple/tax/","netfile":true,"qc":true,"tiers":[{"name":"Basic","price_text":"Pay what you want, including $0 (up to 2 returns)","self":true,"rent":true,"inv":true,"help":false,"qc":true},{"name":"Plus","price_text":"$40 plus tax (included for Premium clients)","self":true,"rent":true,"inv":true,"help":false,"qc":true},{"name":"Pro","price_text":"$80 plus tax (included for Generation clients); 30-minute expert consultation","self":true,"rent":true,"inv":true,"help":true,"qc":false}]},{"name":"TurboTax Canada","netfile":true,"qc":true,"tiers":[{"name":"TurboTax Free","price_text":"$0 for simple returns","self":false,"rent":false,"inv":false,"help":false,"qc":true},{"name":"Deluxe","price_text":"$30 per return (2025 tax year)","self":false,"rent":false,"inv":false,"help":false,"qc":true},{"name":"Premier","price_text":"$50 per return (2025 tax year); adds capital gains and investment income","self":false,"rent":false,"inv":true,"help":false,"qc":true},{"name":"Self-Employed","price_text":"$70 per return (2025 tax year); adds self-employment and rental income","self":true,"rent":true,"inv":true,"help":false,"qc":true},{"name":"Expert Assist","price_text":"Price depends on the complexity of your return","self":true,"rent":null,"inv":true,"help":true,"qc":true}]},{"name":"H&R Block Canada","netfile":true,"qc":true,"tiers":[{"name":"Free","price_text":"$0 for returns that qualify","self":false,"rent":false,"inv":false,"help":false,"qc":true},{"name":"Deluxe","price_text":"$29.99 per return (2025 tax year)","self":false,"rent":false,"inv":false,"help":false,"qc":true},{"name":"Premier","price_text":"$49.99 per return (2025 tax year); adds capital gains and losses","self":false,"rent":false,"inv":true,"help":false,"qc":true},{"name":"Self-Employed","price_text":"$69.99 per return (2025 tax year); adds self-employment and rental income","self":true,"rent":true,"inv":true,"help":false,"qc":true}]},{"name":"UFile","netfile":true,"qc":true,"tiers":[{"name":"UFile ONLINE","price_text":"From $20.95; free for students, first-time filers and family income under $20,000","self":null,"rent":null,"inv":null,"help":false,"qc":true},{"name":"UFile PREMIUM","price_text":"From $32.95","self":null,"rent":null,"inv":null,"help":false,"qc":true}]},{"name":"CloudTax","netfile":true,"qc":null,"tiers":[{"name":"Free","price_text":"$0 or pay what you want (up to 2 returns)","self":null,"rent":null,"inv":null,"help":false,"qc":null},{"name":"Review & File","price_text":"From $49 per return","self":null,"rent":null,"inv":null,"help":true,"qc":null}]},{"name":"GenuTax","netfile":true,"qc":null,"tiers":[{"name":"GenuTax Standard","price_text":"Free (donations optional)","self":null,"rent":null,"inv":null,"help":false,"qc":null}]},{"name":"StudioTax","netfile":true,"qc":null,"tiers":[{"name":"Mobile app","price_text":"Free","self":null,"rent":null,"inv":null,"help":false,"qc":null},{"name":"Computer download","price_text":"Paid; price not published","self":null,"rent":null,"inv":null,"help":false,"qc":null}]}],"tax_software_year":2025,"broker_features":[["tfsa","TFSA"],["rrsp","RRSP"],["spousal","Spousal RRSP"],["fhsa","FHSA"],["resp","RESP"],["rrif","RRIF"],["lira","LIRA or LIF"],["margin","Margin"],["joint","Joint account"],["corporate","Corporate account"],["usd_reg","USD in registered accounts"],["zero_commission","$0 stock and ETF commissions"],["fractional","Fractional shares"],["drip","DRIP"]],"ws_tiers":{"household":true,"list":[{"name":"Core","from":1,"perks":["Chequing interest 1.25% (1.75% with $2,000+ direct deposit in 30 days)","Managed investing fee 0.5%","USD account $10 a month","Instant deposits up to $50,000"]},{"name":"Premium","from":100000,"perks":["Chequing interest 1.75% (2.25% with $2,000+ direct deposit in 30 days)","Managed investing fee 0.4% and tax-loss harvesting","USD account included","Wealthsimple Tax Plus included","Priority phone support","Credit card monthly fee waived ($100,000+ in assets)","Instant deposits up to $250,000"]},{"name":"Generation","from":500000,"perks":["Chequing interest 2.25%","Managed investing fee 0.4%, falling to 0.2% at $10,000,000+","USD account included","Wealthsimple Tax Pro included","Priority phone and email support","Instant deposits up to $250,000","Credit card monthly fee waived"]}],"rows":[["Assets needed","$1","$100,000","$500,000"],["Chequing interest","1.25%","1.75%","2.25%"],["With $2,000+ direct deposit","1.75%","2.25%","2.25%"],["Managed investing fee","0.5%","0.4%","0.4%, down to 0.2%"],["USD account","$10 a month","Included","Included"],["Wealthsimple Tax","Basic","Plus included","Pro included"]]},"cards":[{"name":"Wealthsimple Visa Infinite+","rate":0.02,"fee_month":20,"fee_note":"$20 a month, waived with $100,000+ in assets or $4,000+ a month in direct deposits"}]};
  window.WS_DATA = D;

  /* =====================================================================
   * 2. HELPERS
   * ===================================================================== */
  var NOW = new Date();
  var CUR = D.year || NOW.getFullYear();
  var uid = 0;
  // Round half up with a tiny nudge so binary noise (9.524999999999636) shows as 9.53, the same as qa/wscalc.py r2().
  function rnd(n, d) { var p = Math.pow(10, d || 0); var r = Math.floor(Number(n) * p + 0.5 + 1e-6) / p; return r === 0 ? 0 : r; }
  function nf(n, d) { return rnd(n, d).toLocaleString('en-CA', { minimumFractionDigits: d || 0, maximumFractionDigits: d || 0 }); }
  function money(n, d) { if (!isFinite(n)) return '$0'; var v = rnd(n, d || 0); var s = '$' + nf(Math.abs(v), d || 0); return v < 0 ? '−' + s : s; }
  function money2(n) { return money(n, 2); }
  function pct(x, d) { return nf(x * 100, d == null ? 2 : d) + '%'; }
  function num(v) { if (v == null) return 0; var n = parseFloat(String(v).replace(/[^0-9.\-]/g, '')); return isFinite(n) ? n : 0; }
  function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function sum(a) { return a.reduce(function (s, x) { return s + x; }, 0); }
  function fmtDate(iso, opt) {
    var p = String(iso).split('-'); var dt = new Date(+p[0], +p[1] - 1, +p[2]);
    return dt.toLocaleDateString('en-CA', opt || { year: 'numeric', month: 'long', day: 'numeric' });
  }
  function daysUntil(iso) {
    var p = String(iso).split('-'); var dt = new Date(+p[0], +p[1] - 1, +p[2]);
    var t = new Date(NOW.getFullYear(), NOW.getMonth(), NOW.getDate());
    return Math.round((dt - t) / 86400000);
  }
  var AUTO = false;   // true while a widget runs its first, automatic calculation
  var PRESET = {};    // data-province / data-benefit of the widget being built
  var MEM = (function () {
    var k = 'ws_mem_v1', o = {};
    try { o = JSON.parse(window.localStorage.getItem(k) || '{}') || {}; } catch (e) { o = {}; }
    return {
      get: function (n, d) { return o[n] != null ? o[n] : d; },
      set: function (n, v) { if (AUTO) return; o[n] = v; try { window.localStorage.setItem(k, JSON.stringify(o)); } catch (e) { /* storage unavailable */ } }
    };
  })();
  function track(name, detail) {
    try { document.dispatchEvent(new CustomEvent('ws:calc', { detail: { widget: name, data: detail || {} } })); } catch (e) { /* old browser */ }
    try { if (window.gtag) window.gtag('event', 'ws_calc', { widget: name }); } catch (e) { /* no analytics */ }
  }

  /* ---------- form field builders ---------- */
  function F(p) { return p.id; }
  function fNum(p, id, label, val, o) {
    o = o || {};
    return '<div class="ws-field"><label for="' + p + id + '">' + label + '</label>' +
      '<input type="number" inputmode="decimal" id="' + p + id + '" name="' + id + '" value="' + (val == null ? '' : val) + '"' +
      (o.min != null ? ' min="' + o.min + '"' : '') + (o.max != null ? ' max="' + o.max + '"' : '') +
      ' step="' + (o.step || 'any') + '"' + (o.ph ? ' placeholder="' + esc(o.ph) + '"' : '') + '>' +
      (o.help ? '<small>' + o.help + '</small>' : '') + '</div>';
  }
  function fTxt(p, id, label, val, o) {
    o = o || {};
    return '<div class="ws-field"><label for="' + p + id + '">' + label + '</label>' +
      '<input type="text" id="' + p + id + '" name="' + id + '" value="' + esc(val || '') + '"' + (o.ph ? ' placeholder="' + esc(o.ph) + '"' : '') + '>' +
      (o.help ? '<small>' + o.help + '</small>' : '') + '</div>';
  }
  function fSel(p, id, label, opts, val, o) {
    o = o || {};
    var h = '<div class="ws-field"><label for="' + p + id + '">' + label + '</label><select id="' + p + id + '" name="' + id + '">';
    opts.forEach(function (x) { var v = Array.isArray(x) ? x[0] : x, t = Array.isArray(x) ? x[1] : x; h += '<option value="' + esc(v) + '"' + (String(v) === String(val) ? ' selected' : '') + '>' + esc(t) + '</option>'; });
    return h + '</select>' + (o.help ? '<small>' + o.help + '</small>' : '') + '</div>';
  }
  function fRadio(p, id, label, opts, val) {
    var h = '<div class="ws-field" role="radiogroup" aria-label="' + esc(label) + '"><span class="ws-flabel">' + label + '</span><div class="ws-radio">';
    opts.forEach(function (x) { h += '<label><input type="radio" name="' + p + id + '" value="' + esc(x[0]) + '"' + (String(x[0]) === String(val) ? ' checked' : '') + '> ' + esc(x[1]) + '</label>'; });
    return h + '</div></div>';
  }
  function fDate(p, id, label, val, o) {
    o = o || {};
    return '<div class="ws-field"><label for="' + p + id + '">' + label + '</label><input type="date" id="' + p + id + '" name="' + id + '" value="' + esc(val || '') + '">' + (o.help ? '<small>' + o.help + '</small>' : '') + '</div>';
  }
  function isoAdd(iso, days) { var q = String(iso).split('-'); var d = new Date(+q[0], +q[1] - 1, +q[2] + days); return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function todayIso() { return isoAdd(NOW.getFullYear() + '-' + (NOW.getMonth() + 1) + '-' + NOW.getDate(), 0); }
  function dtcProvs() { var l = D.provinces.filter(function (p) { return D.tax.dividends.provincial_dtc[p[0]]; }).map(function (p) { return p[1]; }); return l.length > 1 ? l.slice(0, -1).join(', ') + ' or ' + l[l.length - 1] : l.join(''); }
  function provOpts() { return D.provinces.map(function (p) { return [p[0], p[1]]; }); }
  function yearOpts(a, b) { var o = []; for (var y = b; y >= a; y--) o.push([y, String(y)]); return o; }

  /* ---------- widget shell ---------- */
  function shell(el, name, cfg) {
    var p = 'ws' + (++uid) + '-';
    el.classList.add('ws-widget');
    if (!el.id) el.id = 'ws-' + name;
    var fields = typeof cfg.fields === 'function' ? cfg.fields(p) : cfg.fields;
    el.innerHTML =
      '<div class="ws-w-head"><div class="ws-w-title" role="heading" aria-level="3">' + cfg.title + '</div>' + (cfg.intro ? '<p>' + cfg.intro + '</p>' : '') + '</div>' +
      '<div class="ws-w-body"><form novalidate onsubmit="return false">' + fields +
      (cfg.button === false ? '' : '<div class="ws-w-actions"><button type="submit" class="ws-w-btn">' + (cfg.button || 'Calculate') + '</button>' +
        '<button type="reset" class="ws-w-btn ws-secondary">Reset</button></div>') +
      '</form><div class="ws-result" aria-live="polite"></div></div>' +
      '<div class="ws-w-foot">' + (cfg.foot || ('Figures as of ' + fmtDate(D.asOf) + '. General information only, not personal financial, tax or investment advice.')) + '</div>';
    var form = el.querySelector('form'), out = el.querySelector('.ws-result');
    function val(id) { var n = form.querySelector('[name="' + id + '"]'); if (n) return n.value; var r = form.querySelector('input[name="' + p + id + '"]:checked'); return r ? r.value : ''; }
    function set(id, v) { var n = form.querySelector('[name="' + id + '"]'); if (n) n.value = v; }
    var api = { p: p, el: el, form: form, out: out, val: val, n: function (id) { return num(val(id)); }, set: set };
    var timer;
    function run(e) {
      try {
        var html = cfg.calc(api, e);
        if (html != null) out.innerHTML = html + nextLinks(cfg.next);
      } catch (err) { out.innerHTML = '<div class="ws-msg ws-err">Please check your entries and try again.</div>'; if (window.console) console.error(err); }
    }
    form.addEventListener('submit', function (e) { e.preventDefault(); run(e); track(name); });
    form.addEventListener('input', function (e) { clearTimeout(timer); timer = setTimeout(function () { run(e); }, 250); });
    form.addEventListener('change', function (e) { clearTimeout(timer); timer = setTimeout(function () { run(e); }, 50); });
    form.addEventListener('reset', function () { setTimeout(function () { out.innerHTML = ''; if (cfg.auto) run(); }, 10); });
    if (cfg.init) cfg.init(api);
    if (cfg.auto !== false) { AUTO = true; try { run(); } finally { AUTO = false; } }
    return api;
  }
  function nextLinks(list) {
    if (!list || !list.length) return '';
    return '<div class="ws-next">Next: ' + list.map(function (x) { return '<a href="' + x[0] + '">' + x[1] + '</a>'; }).join(' &middot; ') + '</div>';
  }
  function kv(items) { return '<div class="ws-kv">' + items.map(function (x) { return '<div><span>' + x[0] + '</span><b>' + x[1] + '</b></div>'; }).join('') + '</div>'; }
  function head(label, value, neg) { return '<p class="ws-headline">' + label + '</p><p class="ws-answer' + (neg ? ' ws-neg' : '') + '">' + value + '</p>'; }
  function msg(type, text) { return '<div class="ws-msg ws-' + type + '">' + text + '</div>'; }
  function how(text) { return '<details class="ws-how"><summary>How this is worked out</summary><div>' + text + '</div></details>'; }
  function table(headers, rows, cap) {
    return '<div class="ws-table-wrap"><table>' + (cap ? '<caption>' + cap + '</caption>' : '') + '<thead><tr>' + headers.map(function (h) { return '<th scope="col">' + h + '</th>'; }).join('') +
      '</tr></thead><tbody>' + rows.map(function (r) { return '<tr>' + r.map(function (c) { return '<td>' + c + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div>';
  }
  function bars(series, labels) {
    var max = Math.max.apply(null, series.map(function (s) { return s.total; }).concat([1]));
    return '<div class="ws-bars" aria-hidden="true">' + series.map(function (s) {
      return '<i style="height:' + (s.total / max * 100).toFixed(1) + '%" title="' + esc(s.label) + '"><b style="height:' + (s.total ? (s.part / s.total * 100) : 0).toFixed(1) + '%"></b></i>';
    }).join('') + '</div><div class="ws-legend"><span><i style="background:var(--ws-copper)"></i>' + labels[0] + '</span><span><i style="background:var(--ws-step2)"></i>' + labels[1] + '</span></div>';
  }

  /* =====================================================================
   * 3. CALCULATION ENGINES (pure functions, exposed as WS.calc for testing)
   * ===================================================================== */
  var C = {};

  /* ---------- income tax ---------- */
  C.bracketTax = function (br, inc) {
    var t = 0, lo = 0;
    for (var i = 0; i < br.length; i++) {
      var hi = br[i][0] == null ? Infinity : br[i][0], r = br[i][1];
      if (inc > lo) t += (Math.min(inc, hi) - lo) * r;
      lo = hi;
      if (inc <= hi) break;
    }
    return t;
  };
  C.fedBPA = function (inc) {
    var f = D.tax.federal, a = f.bpa, b = f.bpa_min, s = f.bpa_phase[0], e = f.bpa_phase[1];
    if (inc <= s) return a; if (inc >= e) return b;
    return a - (a - b) * (inc - s) / (e - s);
  };
  C.ohp = function (inc) {
    var bands = D.tax.provinces.ON.health_premium; // [[from, to, base, rate, cap]]
    for (var i = bands.length - 1; i >= 0; i--) {
      var b = bands[i];
      if (inc > b[0]) return Math.min(b[2] + (inc - b[0]) * b[3], b[4]);
    }
    return 0;
  };
  /* income: taxable income including grossed-up dividends and taxable capital gains.
     opts: {elig: grossed-up eligible dividends, nonelig: grossed-up non-eligible dividends} */
  C.tax = function (prov, inc, opts) {
    opts = opts || {};
    inc = Math.max(0, inc);
    var T = D.tax, f = T.federal, P = T.provinces[prov] || T.provinces.ON;
    var fLow = f.brackets[0][1];
    var fDTC = (opts.elig || 0) * T.dividends.federal_dtc_eligible + (opts.nonelig || 0) * T.dividends.federal_dtc_noneligible;
    var fed = C.bracketTax(f.brackets, inc) - (C.fedBPA(inc) + (opts.cf || 0)) * fLow - fDTC;
    fed = Math.max(0, fed);
    if (prov === 'QC') fed = fed * (1 - T.qc_abatement);
    var pLow = P.brackets[0][1];
    var pd = (T.dividends.provincial_dtc[prov] || [0, 0]);
    var pDTC = (opts.elig || 0) * pd[0] + (opts.nonelig || 0) * pd[1];
    var pbpa = P.bpa;
    if (P.bpa_phase) { // e.g. Manitoba, Nova Scotia, Yukon: [start, end, minimum]
      var ps = P.bpa_phase[0], pe = P.bpa_phase[1], pm = P.bpa_phase[2];
      if (inc >= pe) pbpa = pm; else if (inc > ps) pbpa = P.bpa - (P.bpa - pm) * (inc - ps) / (pe - ps);
    }
    var pinc = Math.max(0, inc - (opts.pd || 0));
    if (P.bpa_phase && opts.pd) { var ps2 = P.bpa_phase[0], pe2 = P.bpa_phase[1], pm2 = P.bpa_phase[2]; pbpa = pinc >= pe2 ? pm2 : (pinc > ps2 ? P.bpa - (P.bpa - pm2) * (pinc - ps2) / (pe2 - ps2) : P.bpa); }
    // Ontario (ON428): the surtax is worked out on basic tax BEFORE the dividend tax credit; the credit comes off after the surtax.
    var pr0 = Math.max(0, C.bracketTax(P.brackets, pinc) - (pbpa + (opts.cp || 0)) * pLow);
    var sur = 0;
    if (P.surtax) P.surtax.forEach(function (s) { if (pr0 > s[0]) sur += (pr0 - s[0]) * s[1]; });
    var pr = Math.max(0, pr0 + sur - pDTC) - sur; // so that pr + sur = tax after surtax and dividend tax credit (never below zero)
    var red = 0, R = P.reduction;
    if (R && R.type === 'bc') red = Math.min(pr, Math.max(0, R.base - R.rate * Math.max(0, inc - R.threshold)));
    if (R && R.type === 'on') red = Math.min(pr + sur, Math.max(0, 2 * (R.base + R.dep * (opts.deps || 0)) - (pr + sur)));
    var hp = prov === 'ON' && P.health_premium ? C.ohp(inc) : 0;
    var total = fed + pr + sur - red + hp;
    return { federal: fed, provincial: pr + sur - red, surtax: sur, reduction: red, premium: hp, total: total, avg: inc > 0 ? total / inc : 0 };
  };
  C.marginal = function (prov, inc, kind) {
    var d = 100, base, up;
    if (kind === 'cg') { base = C.tax(prov, inc).total; up = C.tax(prov, inc + d * D.tax.capital_gains_inclusion).total; }
    else if (kind === 'elig' || kind === 'nonelig') {
      var g = kind === 'elig' ? D.tax.dividends.eligible_grossup : D.tax.dividends.noneligible_grossup;
      var o = {}; o[kind] = d * (1 + g);
      base = C.tax(prov, inc).total; up = C.tax(prov, inc + d * (1 + g), o).total;
    } else { base = C.tax(prov, inc).total; up = C.tax(prov, inc + d).total; }
    return (up - base) / d;
  };

  /* ---------- TFSA room ---------- */
  C.tfsaRoom = function (o) {
    // o: {birth, resident (year became resident or 0), nonres: [years], contrib (before this year), wdPrior (before this year), contribNow, wdNow}
    var L = D.tfsa.limits, start = Math.max(2009, o.birth + 18, o.resident || 0), rows = [], accrued = 0;
    for (var y = start; y <= CUR; y++) {
      var lim = L[y] || 0, skip = o.nonres.indexOf(y) >= 0;
      if (!skip) accrued += lim;
      rows.push([y, skip ? 0 : lim, accrued, skip]);
    }
    var startNow = accrued - o.contrib + o.wdPrior;
    var avail = startNow - o.contribNow;
    var nextLim = L[CUR + 1] || null;
    return { start: start, rows: rows, accrued: accrued, startOfYear: startNow, available: avail, next: nextLim != null ? avail + o.wdNow + nextLim : null, nextLim: nextLim, wdNow: o.wdNow };
  };

  /* ---------- RRSP ---------- */
  C.rrspRoom = function (earned, pa, carry, par) {
    var lim = D.rrsp.limits[CUR];
    var base = Math.min(earned * D.rrsp.pct, lim);
    return { base: base, limit: lim, room: Math.max(0, base - pa + par) + carry };
  };

  /* ---------- FHSA ---------- */
  C.fhsa = function (opened, contribByYear) {
    var F = D.fhsa, carry = 0, total = 0, rows = [];
    for (var y = opened; y <= CUR; y++) {
      var room = Math.min(F.annual + carry, F.lifetime - total);
      var c = contribByYear[y] || 0;
      rows.push([y, room, c]);
      if (y < CUR) { carry = clamp(room - c, 0, F.carry); total += c; }
    }
    var last = rows[rows.length - 1];
    var cNow = last ? last[2] : 0, roomNow = last ? last[1] : F.annual;
    var lifetimeLeft = F.lifetime - total - cNow;
    var nextCarry = clamp(roomNow - cNow, 0, F.carry);
    var nextRoom = Math.min(F.annual + nextCarry, Math.max(0, lifetimeLeft));
    return { rows: rows, roomNow: roomNow, leftNow: roomNow - cNow, lifetimeLeft: lifetimeLeft, nextRoom: nextRoom, totalPrior: total };
  };

  /* ---------- RESP grants ---------- */
  C.resp = function (o) {
    // o: {birth, prov, income, kids, annual, pastContrib, pastCesg, ret}
    var R = D.resp, age0 = CUR - o.birth, rows = [];
    var room = 0; for (var y = Math.max(o.birth, 2007); y <= CUR; y++) room += R.cesg_annual;
    room = Math.max(0, room - o.pastCesg);
    var cesgTot = o.pastCesg, contribTot = o.pastContrib, bal = o.pastContrib + o.pastCesg, extraTot = 0, clbTot = 0, provTot = 0;
    var yearsBy15 = 0, contribBy15 = o.pastContrib;
    var acesgRate = o.income <= R.acesg_income[0] ? R.acesg_rates[0] : (o.income <= R.acesg_income[1] ? R.acesg_rates[1] : 0);
    var clbOk = o.income <= R.clb_thresholds[Math.min(Math.max(1, o.kids), 5)];
    if (o.pastContrib >= R.cesg_age16_total) contribBy15 = o.pastContrib;
    for (var a = age0; a <= 17; a++) {
      var yr = o.birth + a;
      if (a > age0) room += R.cesg_annual;
      var c = o.annual;
      var eligible = a <= 15 || contribBy15 >= R.cesg_age16_total || yearsBy15 >= R.cesg_age16_years;
      var g = 0;
      if (eligible && yr >= 2007) g = Math.min(c * R.cesg_rate, Math.min(room, R.cesg_max_year), R.cesg_lifetime - cesgTot);
      g = Math.max(0, g);
      room -= g; cesgTot += g;
      var x = eligible ? Math.min(c, R.acesg_on_first) * acesgRate : 0;
      if (cesgTot >= R.cesg_lifetime) x = 0; // A-CESG counts toward the same lifetime limit
      x = Math.min(x, Math.max(0, R.cesg_lifetime - cesgTot));
      cesgTot += x; extraTot += x;
      var b = 0;
      if (clbOk && yr >= 2004 && a <= 15) { b = (clbTot === 0 ? R.clb_first : R.clb_yearly); b = Math.min(b, R.clb_max - clbTot); clbTot += b; }
      var pg = 0;
      if (o.prov === 'QC') { pg = Math.min(c * R.qesi_rate, R.qesi_annual, R.qesi_lifetime - provTot); provTot += pg; }
      if (o.prov === 'BC' && a >= 6 && a <= 9 && provTot === 0 && o.birth >= 2006) { pg = R.bctesg; provTot += pg; }
      contribTot += c; if (a <= 15) { contribBy15 += c; if (c >= 100) yearsBy15++; }
      bal = bal * (1 + o.ret) + c + g + x + b + pg;
      rows.push([yr, a, c, g + x, b, pg, bal]);
    }
    return { rows: rows, cesg: cesgTot - o.pastCesg, extra: extraTot, clb: clbTot, prov: provTot, contrib: contribTot, bal: bal, thisYear: rows[0] };
  };

  /* ---------- RRIF ---------- */
  C.rrifFactor = function (age) {
    if (age < 71) return 1 / (90 - age);
    if (age >= 95) return D.rrif.factors[95];
    return D.rrif.factors[age];
  };

  /* ---------- growth ---------- */
  C.grow = function (pv, pmtMonthly, rateAnnual, years, comp) {
    // comp: compounding periods per year (1, 2, 4, 12, 365). Contributions monthly at month end.
    var m = Math.round(years * 12), bal = pv, contrib = pv, rows = [];
    var er = Math.pow(1 + rateAnnual / comp, comp / 12) - 1; // effective monthly rate
    for (var i = 1; i <= m; i++) {
      bal = bal * (1 + er) + pmtMonthly; contrib += pmtMonthly;
      if (i % 12 === 0 || i === m) rows.push([Math.ceil(i / 12), contrib, bal]);
    }
    return { bal: bal, contrib: contrib, interest: bal - contrib, rows: rows };
  };

  /* ---------- broker cost ---------- */
  C.brokerAnnual = function (b, o) {
    // o: {cad, us, opts, contracts}
    var cad = (b.cad_trade == null ? 0 : b.cad_trade) * o.cad * 12;
    var us = (b.us_trade == null ? 0 : b.us_trade) * o.us * 12;
    var op = o.opts ? 12 * o.opts * Math.max((b.opt_base || 0) + (b.opt_contract || 0) * (o.contracts || 1), b.opt_min || 0) : 0;
    return { cad: cad, us: us, opts: op, fees: b.annual_fee || 0, total: cad + us + op + (b.annual_fee || 0) };
  };
  C.roboFee = function (r, amt) {
    var fee = 0;
    if (r.tiers) { // [[upTo, rate]] marginal or flat
      if (r.tier_mode === 'flat') { for (var i = 0; i < r.tiers.length; i++) { if (r.tiers[i][0] == null || amt <= r.tiers[i][0]) { fee = amt * r.tiers[i][1]; break; } } }
      else { var lo = 0; r.tiers.forEach(function (t) { var hi = t[0] == null ? Infinity : t[0]; if (amt > lo) fee += (Math.min(amt, hi) - lo) * t[1]; lo = hi; }); }
    }
    fee = Math.max(fee, r.min_fee || 0);
    var mer = amt * (r.mer || 0);
    return { mgmt: fee, mer: mer, total: fee + mer };
  };

  window.WS = window.WS || {};
  window.WS.calc = C;

  /* =====================================================================
   * 4. WIDGETS
   * ===================================================================== */
  var W = {};
  var bornDefault = function () { return MEM.get('birth', 1995); };
  var provDefault = function () { return (PRESET.prov && D.provName[PRESET.prov]) ? PRESET.prov : MEM.get('prov', 'ON'); };

  /* ---------- TFSA contribution room ---------- */
  W['tfsa-room'] = function (el) {
    shell(el, 'tfsa-room', {
      title: 'TFSA contribution room calculator',
      intro: 'Enter your birth year and when you became a resident of Canada. We add up every annual limit you qualify for since ' + 2009 + ' and give your room for ' + CUR + '.',
      fields: function (p) {
        return '<div class="ws-w-grid">' +
          fNum(p, 'birth', 'Year you were born', bornDefault(), { min: 1900, max: CUR, help: 'Room starts in the year you turn 18.' }) +
          fNum(p, 'resident', 'Year you became a resident of Canada', '', { min: 1900, max: CUR, ph: 'Leave blank if always resident', help: 'Newcomers get the full limit for the year they arrive.' }) +
          fTxt(p, 'nonres', 'Full calendar years you lived outside Canada (optional)', '', { ph: 'e.g. 2015, 2016', help: 'No room is added for a year you were a non-resident for the whole year.' }) +
          fSel(p, 'prov', 'Province or territory', provOpts(), provDefault(), { help: 'Opening age depends on your province.' }) +
          fNum(p, 'contrib', 'Total contributions before ' + CUR, 0, { min: 0, help: 'All years before this one. Leave out direct transfers between TFSAs.' }) +
          fNum(p, 'wdprior', 'Total withdrawals before ' + CUR, 0, { min: 0, help: 'Withdrawals come back as room on January 1 of the next year.' }) +
          fNum(p, 'contribnow', 'Contributions so far in ' + CUR, 0, { min: 0 }) +
          fNum(p, 'wdnow', 'Withdrawals so far in ' + CUR, 0, { min: 0, help: 'Added back to your room on January 1, ' + (CUR + 1) + '.' }) +
          '</div>';
      },
      calc: function (a) {
        var birth = a.n('birth'), res = a.n('resident'), prov = a.val('prov');
        if (birth < 1900 || birth > CUR) return msg('warnmsg', 'Please enter a birth year between 1900 and ' + CUR + '.');
        MEM.set('birth', birth); MEM.set('prov', prov);
        if (birth + 18 > CUR) return msg('warnmsg', 'You turn 18 in ' + (birth + 18) + '. TFSA room starts that year: ' + money(D.tfsa.limits[birth + 18] || D.tfsa.limits[CUR]) + (D.tfsa.limits[birth + 18] ? '' : ' if the limit stays the same') + '.');
        var nonres = (a.val('nonres').match(/\d{4}/g) || []).map(Number);
        var r = C.tfsaRoom({ birth: birth, resident: res, nonres: nonres, contrib: a.n('contrib'), wdPrior: a.n('wdprior'), contribNow: a.n('contribnow'), wdNow: a.n('wdnow') });
        var maj = D.age_of_majority[prov] || 18;
        var h = head('Your TFSA room available now (' + CUR + ')', money(r.available), r.available < 0);
        if (r.available < 0) {
          var tax = -r.available * D.tfsa.over_tax_month;
          h += msg('err', 'You are over your limit by ' + money(-r.available) + '. The tax is 1% of the highest excess amount for each month it stays in the account: about ' + money2(tax) + ' a month. Withdrawing the excess stops the tax from the next month.');
        }
        h += kv([['Room earned since ' + r.start, money(r.accrued)], ['Room on January 1, ' + CUR, money(r.startOfYear)], ['Used so far in ' + CUR, money(a.n('contribnow'))],
          ['Room on January 1, ' + (CUR + 1), r.next != null ? money(r.next) : (money(r.available + r.wdNow) + ' plus the ' + (CUR + 1) + ' limit')]]);
        if (maj > 18 && CUR - birth < maj) h += msg('warnmsg', 'In your province you can open a TFSA at ' + maj + '. Room still builds from the year you turn 18, so nothing is lost.');
        h += table(['Year', 'Annual limit', 'Your cumulative room'], r.rows.map(function (x) { return [x[0], x[3] ? 'Non-resident: $0' : money(x[1]), money(x[2])]; }), 'Room added each year');
        h += how('Room starts in the latest of 2009, the year you turn 18 (' + (birth + 18) + ') and the year you became a resident' + (res ? ' (' + res + ')' : '') + '. Each year adds that year\'s limit. Contributions reduce room. Withdrawals made in an earlier year are added back on January 1. Withdrawals this year come back on January 1, ' + (CUR + 1) + '. Your CRA My Account figure can differ if contributions or withdrawals were reported differently.');
        return h;
      },
      next: [['/accounts/tfsa-contribution-limit/', 'TFSA limit by year'], ['/accounts/tfsa-withdrawals/', 'Withdrawal rules'], ['/compare/best-tfsa-accounts/', 'Compare TFSA accounts']]
    });
  };

  /* ---------- TFSA over-contribution tax ---------- */
  W['tfsa-overcontribution'] = function (el) {
    shell(el, 'tfsa-overcontribution', {
      title: 'TFSA over-contribution penalty calculator',
      intro: 'See the 1% monthly tax on an excess TFSA amount and how much you save by withdrawing it now.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'excess', 'Highest excess amount in the month', 2000, { min: 0 }) +
          fNum(p, 'months', 'Months the excess stays in the account', 3, { min: 1, max: 120, step: 1, help: 'Count each month in which any excess existed.' }) + '</div>';
      },
      calc: function (a) {
        var ex = a.n('excess'), m = Math.round(a.n('months'));
        var t = ex * D.tfsa.over_tax_month * m;
        return head('Estimated tax on the excess', money2(t)) + kv([['Tax per month', money2(ex * D.tfsa.over_tax_month)], ['Months', String(m)], ['Saved by removing it a month sooner', money2(ex * D.tfsa.over_tax_month)]]) +
          how('The tax is 1% of the highest excess TFSA amount in each month the excess exists. Withdrawing the excess, or new room arriving on January 1, ends it. You report it on the TFSA Return and pay it by June 30 of the following year, so please withdraw any excess as soon as you find it.');
      },
      next: [['/calculators/tfsa-calculator/', 'TFSA room calculator'], ['/accounts/tfsa-withdrawals/', 'TFSA withdrawal rules']]
    });
  };

  /* ---------- RRSP deduction limit ---------- */
  W['rrsp-room'] = function (el) {
    shell(el, 'rrsp-room', {
      title: 'RRSP contribution room calculator',
      intro: 'Your ' + CUR + ' RRSP room is 18% of your ' + (CUR - 1) + ' earned income up to the dollar limit, minus your pension adjustment, plus unused room carried forward.',
      fields: function (p) {
        return '<div class="ws-w-grid">' +
          fNum(p, 'earned', 'Earned income in ' + (CUR - 1), MEM.get('income', 75000), { min: 0, help: 'Employment and self-employment income, net rental income and similar. Not investment income.' }) +
          fNum(p, 'pa', 'Pension adjustment (box 52 of your T4)', 0, { min: 0, help: 'Only if you belong to a workplace pension or DPSP.' }) +
          fNum(p, 'carry', 'Unused room carried forward', 0, { min: 0, help: 'From your latest notice of assessment.' }) +
          fNum(p, 'par', 'Pension adjustment reversal (PAR)', 0, { min: 0 }) +
          fNum(p, 'done', 'RRSP contributions already made for ' + CUR, 0, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var e = a.n('earned'); MEM.set('income', e);
        var r = C.rrspRoom(e, a.n('pa'), a.n('carry'), a.n('par'));
        var left = r.room - a.n('done');
        var h = head('Your ' + CUR + ' RRSP deduction limit', money(r.room));
        h += kv([['18% of ' + (CUR - 1) + ' earned income', money(e * D.rrsp.pct)], [CUR + ' dollar limit', money(r.limit)], ['New room this year', money(Math.max(0, r.base - a.n('pa') + a.n('par')))], ['Left after contributions', money(left)]]);
        if (left < -D.rrsp.cushion) h += msg('err', 'You are ' + money(-left - D.rrsp.cushion) + ' over the $2,000 buffer. The excess is taxed at 1% a month until removed.');
        else if (left < 0) h += msg('warnmsg', 'You are within the $2,000 the CRA allows above your deduction limit at any time, so no penalty tax applies, but the extra amount is not deductible until you have new room.');
        h += msg('ok', 'Contribution deadline for the ' + CUR + ' tax year: ' + fmtDate(D.rrsp.deadline[CUR]) + ', the 60th day of ' + (CUR + 1) + ' under CRA\'s rule. CRA confirms the date each year.');
        h += how('New room = the lower of 18% of last year\'s earned income and the ' + CUR + ' dollar limit (' + money(r.limit) + '), minus your pension adjustment, plus any pension adjustment reversal. Unused room from earlier years is added on top. Your notice of assessment shows the official figure.');
        return h;
      },
      next: [['/calculators/rrsp-calculator/', 'RRSP tax refund calculator'], ['/accounts/rrsp-contribution-limit/', 'RRSP limit by year'], ['/compare/best-rrsp-accounts/', 'Compare RRSP accounts']]
    });
  };

  /* ---------- RRSP tax refund ---------- */
  W['rrsp-refund'] = function (el) {
    shell(el, 'rrsp-refund', {
      title: 'RRSP tax refund calculator',
      intro: 'Pick your province, enter your taxable income and an RRSP contribution. We work out the tax saved with ' + CUR + ' federal and provincial brackets.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Taxable income before the RRSP deduction', MEM.get('income', 75000), { min: 0 }) +
          fNum(p, 'contrib', 'RRSP contribution to deduct', 5000, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), inc = a.n('income'), c = Math.min(a.n('contrib'), inc);
        MEM.set('prov', prov); MEM.set('income', inc);
        var t0 = C.tax(prov, inc), t1 = C.tax(prov, inc - c), save = t0.total - t1.total;
        var h = head('Estimated tax saved by a ' + money(c) + ' deduction', money(save));
        h += kv([['Marginal rate before', pct(C.marginal(prov, inc), 1)], ['Marginal rate after', pct(C.marginal(prov, inc - c), 1)], ['Average saving per $1', money2(c ? save / c : 0)], ['Net cost of the contribution', money(c - save)]]);
        h += table(['', 'Without RRSP', 'With RRSP'], [['Federal tax', money(t0.federal), money(t1.federal)], [D.provName[prov] + ' tax', money(t0.provincial + t0.premium), money(t1.provincial + t1.premium)], ['Total', money(t0.total), money(t1.total)]]);
        h += how('Tax saved = tax on your income without the deduction minus tax with it, using ' + CUR + ' brackets and basic personal amounts' + (prov === 'ON' ? ', the Ontario surtax and the Ontario Health Premium' : '') + (prov === 'QC' ? ' and the 16.5% Quebec abatement on federal tax' : '') + '. Your actual refund also depends on tax already withheld, other credits and CPP and EI. A refund only appears if withholding was more than your final tax.');
        return h;
      },
      next: [['/calculators/rrsp-calculator/', 'RRSP calculator'], ['/vs/tfsa-vs-rrsp/', 'TFSA vs RRSP'], ['/accounts/rrsp/', 'RRSP guide']]
    });
  };

  /* ---------- Income tax ---------- */
  W['income-tax'] = function (el) {
    shell(el, 'income-tax', {
      title: 'Canada income tax calculator ' + CUR,
      intro: 'Federal and provincial tax, your marginal rate on each type of income, and your average rate.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Employment and other ordinary income', MEM.get('income', 75000), { min: 0 }) +
          fNum(p, 'cg', 'Capital gains realized', 0, { min: 0 }) +
          fNum(p, 'elig', 'Eligible dividends received', 0, { min: 0 }) +
          fNum(p, 'nonelig', 'Other than eligible dividends received', 0, { min: 0 }) +
          fNum(p, 'rrsp', 'RRSP and FHSA deductions', 0, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'); MEM.set('prov', prov);
        var dtcOk = !!D.tax.dividends.provincial_dtc[prov];
        if (!dtcOk && (a.n('elig') > 0 || a.n('nonelig') > 0)) return msg('warnmsg', 'Dividend tax credit rates for ' + D.provName[prov] + ' are being confirmed for ' + CUR + '. Please set dividends to 0 for now, or choose ' + dtcProvs() + '.');
        var T = D.tax, eg = a.n('elig') * (1 + T.dividends.eligible_grossup), ng = a.n('nonelig') * (1 + T.dividends.noneligible_grossup);
        var ti = Math.max(0, a.n('income') + a.n('cg') * T.capital_gains_inclusion + eg + ng - a.n('rrsp'));
        var t = C.tax(prov, ti, { elig: eg, nonelig: ng });
        var gross = a.n('income') + a.n('cg') + a.n('elig') + a.n('nonelig');
        var h = head('Estimated ' + CUR + ' income tax', money(t.total));
        h += kv([['Taxable income', money(ti)], ['Federal tax', money(t.federal)], [D.provName[prov] + ' tax', money(t.provincial + t.premium)], ['Average rate on all income', pct(gross ? t.total / gross : 0, 1)], ['After-tax income', money(gross - a.n('rrsp') - t.total)]]);
        h += table(['Next $100 of', 'Marginal rate'], [['Ordinary income', pct(C.marginal(prov, ti), 2)], ['Capital gains', pct(C.marginal(prov, ti, 'cg'), 2)], ['Eligible dividends', dtcOk ? pct(C.marginal(prov, ti, 'elig'), 2) : 'Being confirmed'], ['Other than eligible dividends', dtcOk ? pct(C.marginal(prov, ti, 'nonelig'), 2) : 'Being confirmed']], 'Marginal tax rates at your income');
        h += how('Uses ' + CUR + ' federal and ' + D.provName[prov] + ' brackets, basic personal amounts, the dividend gross-up and dividend tax credits, and the ' + pct(T.capital_gains_inclusion, 0) + ' capital gains inclusion rate' + (prov === 'ON' ? ', plus the Ontario surtax and Health Premium' : '') + (prov === 'QC' ? ', plus the 16.5% Quebec abatement' : '') + '. CPP and EI contributions, the Canada employment amount and other credits are not included, so your final tax will usually be a little lower. A negative dividend tax result is set to zero.');
        return h;
      },
      next: [['/calculators/capital-gains-tax-calculator/', 'Capital gains tax calculator'], ['/calculators/rrsp-calculator/', 'RRSP refund calculator']]
    });
  };

  /* ---------- Capital gains ---------- */
  W['capital-gains'] = function (el) {
    shell(el, 'capital-gains', {
      title: 'Capital gains tax calculator',
      intro: 'Tax on a gain from selling shares, ETFs or other investments in a non-registered account.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Other taxable income this year', MEM.get('income', 75000), { min: 0 }) +
          fNum(p, 'proceeds', 'Sale proceeds', 20000, { min: 0 }) +
          fNum(p, 'acb', 'Adjusted cost base (what you paid, including commissions)', 12000, { min: 0 }) +
          fNum(p, 'costs', 'Selling costs', 0, { min: 0 }) +
          fNum(p, 'losses', 'Net capital losses carried forward (full loss amount)', 0, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'); MEM.set('prov', prov);
        var gain = a.n('proceeds') - a.n('acb') - a.n('costs'), inc = a.n('income'), inc_r = D.tax.capital_gains_inclusion;
        if (gain <= 0) return head('Capital loss', money(gain), true) + msg('ok', 'A capital loss of ' + money(-gain) + ' first offsets other capital gains this year. Any unused part can be carried back 3 years or forward with no time limit, against capital gains only. Watch the superficial loss rule if you or an affiliated person buy the same property within 30 days before or after the sale.');
        var net = Math.max(0, gain - a.n('losses')), taxable = net * inc_r;
        var tax = C.tax(prov, inc + taxable).total - C.tax(prov, inc).total;
        return head('Estimated tax on this gain', money(tax)) + kv([['Capital gain', money(gain)], ['Taxable capital gain (' + pct(inc_r, 0) + ')', money(taxable)], ['Effective tax rate on the gain', pct(gain ? tax / gain : 0, 1)], ['You keep', money(gain - tax)]]) +
          how('Capital gain = proceeds minus adjusted cost base minus selling costs. ' + pct(inc_r, 0) + ' of the net gain is added to your income and taxed at your marginal rate, using ' + CUR + ' ' + D.provName[prov] + ' and federal brackets. Gains inside a TFSA, RRSP, FHSA or RESP are not taxed this way.');
      },
      next: [['/accounts/tfsa/', 'Shelter gains in a TFSA'], ['/calculators/', 'All calculators']]
    });
  };

  /* ---------- Dividend tax ---------- */
  W['dividend-tax'] = function (el) {
    shell(el, 'dividend-tax', {
      title: 'Dividend tax calculator',
      intro: 'Tax on Canadian eligible and other than eligible dividends after the gross-up and dividend tax credit.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Other taxable income', MEM.get('income', 75000), { min: 0 }) +
          fNum(p, 'elig', 'Eligible dividends (actual amount)', 5000, { min: 0 }) +
          fNum(p, 'nonelig', 'Other than eligible dividends (actual amount)', 0, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), T = D.tax, inc = a.n('income');
        if (!T.dividends.provincial_dtc[prov]) return msg('warnmsg', 'Dividend tax credit rates for ' + D.provName[prov] + ' are being confirmed for ' + CUR + '. This calculator currently covers ' + Object.keys(T.dividends.provincial_dtc).map(function (k) { return D.provName[k]; }).join(', ') + '.');
        var eg = a.n('elig') * (1 + T.dividends.eligible_grossup), ng = a.n('nonelig') * (1 + T.dividends.noneligible_grossup);
        var t = C.tax(prov, inc + eg + ng, { elig: eg, nonelig: ng }).total - C.tax(prov, inc).total;
        var d = a.n('elig') + a.n('nonelig');
        return head('Estimated tax on these dividends', money(t, 0), t < 0) + kv([['Grossed-up amount', money(eg + ng)], ['Effective rate on dividends', pct(d ? t / d : 0, 1)], ['You keep', money(d - t)]]) +
          how('Eligible dividends are grossed up by ' + pct(T.dividends.eligible_grossup, 0) + ' and other than eligible dividends by ' + pct(T.dividends.noneligible_grossup, 0) + '. Federal and ' + D.provName[prov] + ' dividend tax credits are then deducted. Credits cannot reduce tax below zero, but they can shelter tax on your other income, which is why the result can be lower than you expect. Foreign dividends get no gross-up or credit.');
      },
      next: [['/calculators/capital-gains-tax-calculator/', 'Capital gains calculator'], ['/accounts/us-stocks-in-tfsa/', 'US dividends in a TFSA']]
    });
  };

  /* ---------- FHSA room ---------- */
  W['fhsa-room'] = function (el) {
    shell(el, 'fhsa-room', {
      title: 'FHSA contribution room calculator',
      intro: 'Room starts only when you open your first FHSA: ' + money(D.fhsa.annual) + ' a year, up to ' + money(D.fhsa.carry) + ' of unused room carried forward, ' + money(D.fhsa.lifetime) + ' lifetime.',
      fields: function (p) {
        var h = '<div class="ws-w-grid">' + fSel(p, 'opened', 'Year you opened your first FHSA', yearOpts(D.fhsa.first_year, CUR), CUR, { help: 'Room does not build before you open one.' }) +
          fNum(p, 'birth', 'Year you were born', bornDefault(), { min: 1900, max: CUR }) + '</div><div class="ws-rows"></div>';
        return h;
      },
      init: function (a) {
        function rows() {
          var o = a.n('opened'), box = a.form.querySelector('.ws-rows'), h = '<p class="ws-flabel" style="margin:14px 0 6px;font-weight:800">Contributions by year</p>';
          for (var y = o; y <= CUR; y++) h += '<div class="ws-rowgrid"><span>' + y + '</span><input type="number" min="0" step="any" name="c' + y + '" aria-label="FHSA contributions in ' + y + '" value="' + (y === CUR ? 0 : D.fhsa.annual) + '"><small>' + (y === CUR ? 'so far this year' : '') + '</small></div>';
          box.innerHTML = h;
        }
        rows();
        a.form.querySelector('[name="opened"]').addEventListener('change', rows);
      },
      calc: function (a) {
        var o = a.n('opened'), birth = a.n('birth'), cy = {};
        for (var y = o; y <= CUR; y++) cy[y] = a.n('c' + y);
        var r = C.fhsa(o, cy);
        var close = Math.min(o + D.fhsa.max_years, birth + D.fhsa.max_age);
        var h = head('FHSA room left in ' + CUR, money(Math.max(0, r.leftNow)), r.leftNow < 0);
        if (r.leftNow < 0) h += msg('err', 'This is ' + money(-r.leftNow) + ' over your room. Excess FHSA amounts are taxed at 1% a month until removed or absorbed by new room.');
        h += kv([['Room for ' + CUR, money(r.roomNow)], ['Lifetime room left', money(Math.max(0, r.lifetimeLeft))], ['Room on January 1, ' + (CUR + 1), money(r.nextRoom)], ['Account must close by', 'December 31, ' + close]]);
        h += table(['Year', 'Participation room', 'Contributed'], r.rows.map(function (x) { return [x[0], money(x[1]), money(x[2])]; }));
        h += how('Each year adds ' + money(D.fhsa.annual) + '. Unused room carries forward, but only up to ' + money(D.fhsa.carry) + ', so the most you can contribute in one year is ' + money(D.fhsa.annual + D.fhsa.carry) + '. Lifetime contributions are capped at ' + money(D.fhsa.lifetime) + '. The FHSA must close by the end of the ' + D.fhsa.max_years + 'th year after you opened it or the year you turn ' + D.fhsa.max_age + ', whichever is first. Contributions made in the first 60 days of a year count for that year, not the previous one.');
        return h;
      },
      next: [['/accounts/fhsa/', 'FHSA guide'], ['/accounts/fhsa-eligibility/', 'FHSA eligibility'], ['/compare/best-fhsa-accounts/', 'Compare FHSA accounts']]
    });
  };

  /* ---------- FHSA eligibility ---------- */
  W['fhsa-eligibility'] = function (el) {
    shell(el, 'fhsa-eligibility', {
      title: 'FHSA eligibility checker',
      intro: 'Answer five quick questions to see if you can open a First Home Savings Account today.',
      button: 'Check eligibility',
      fields: function (p) {
        return fRadio(p, 'res', 'Are you a resident of Canada?', [['y', 'Yes'], ['n', 'No']], 'y') +
          fNum(p, 'birth', 'Year you were born', bornDefault(), { min: 1900, max: CUR }) +
          fRadio(p, 'own', 'At any time in ' + CUR + ' or the previous four calendar years (since January 1, ' + (CUR - 4) + '), did you live in a home that you owned or jointly owned as your main home?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fRadio(p, 'spouse', 'At any time in ' + CUR + ' or the previous four calendar years, did you live in a home owned by your current spouse or common-law partner?', [['n', 'No'], ['y', 'Yes'], ['na', 'No spouse or partner']], 'na') +
          fRadio(p, 'prior', 'Have you already made a qualifying FHSA withdrawal for a home?', [['n', 'No'], ['y', 'Yes']], 'n');
      },
      calc: function (a) {
        var age = CUR - a.n('birth'), reasons = [];
        if (a.val('res') === 'n') reasons.push('You must be a resident of Canada to open an FHSA.');
        if (age < 18) reasons.push('You must be at least 18. In some provinces the age of majority is 19.');
        if (age > D.fhsa.max_age) reasons.push('You can open an FHSA only up to December 31 of the year you turn ' + D.fhsa.max_age + '.');
        if (a.val('own') === 'y') reasons.push('You do not meet the first-time home buyer test: you lived in a home you owned in ' + CUR + ' or the previous four calendar years.');
        if (a.val('spouse') === 'y') reasons.push('You do not meet the first-time home buyer test: you lived in a home owned by your current spouse or common-law partner in ' + CUR + ' or the previous four calendar years.');
        var warn = a.val('prior') === 'y' ? msg('warnmsg', 'Your FHSA participation period ends on December 31 of the year after your first qualifying withdrawal, so room stops building then.') : '';
        if (!reasons.length) return warn + head('Result', 'You appear eligible') + msg('ok', 'You can open an FHSA. Room of ' + money(D.fhsa.annual) + ' starts in the year you open it, so opening sooner builds more room, even with a $0 balance.') +
          (age >= 18 && age <= 19 ? msg('warnmsg', 'If your province\'s age of majority is 19 (British Columbia, New Brunswick, Newfoundland and Labrador, Nova Scotia, Northwest Territories, Nunavut, Yukon), some institutions will open it only at 19.') : '');
        return warn + head('Result', 'Not eligible right now', true) + '<ul>' + reasons.map(function (r) { return '<li>' + r + '</li>'; }).join('') + '</ul>';
      },
      next: [['/accounts/fhsa/', 'FHSA guide'], ['/calculators/fhsa-calculator/', 'FHSA calculator'], ['/vs/fhsa-vs-rrsp/', 'FHSA vs RRSP Home Buyers\' Plan']]
    });
  };

  /* ---------- RESP grants ---------- */
  W['resp-grant'] = function (el) {
    shell(el, 'resp-grant', {
      title: 'RESP grant calculator',
      intro: 'See the Canada Education Savings Grant, Additional CESG, Canada Learning Bond and provincial grants your contributions can attract, and the plan value at 17.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'birth', 'Child\'s year of birth', CUR - 3, { min: CUR - 17, max: CUR }) +
          fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Adjusted family net income', 80000, { min: 0, help: 'Used for the Additional CESG and Canada Learning Bond.' }) +
          fNum(p, 'kids', 'Number of qualified dependants', 1, { min: 1, max: 10, step: 1 }) +
          fNum(p, 'annual', 'Contribution per year from now', R().cesg_on, { min: 0 }) +
          fNum(p, 'past', 'Contributions already made', 0, { min: 0 }) +
          fNum(p, 'pastg', 'CESG already received', 0, { min: 0 }) +
          fNum(p, 'ret', 'Example assumption: yearly return (%)', 4, { min: -10, max: 15, help: 'An assumption for illustration, not a forecast.' }) + '</div>';
      },
      calc: function (a) {
        var birth = a.n('birth');
        if (CUR - birth > 17) return msg('warnmsg', 'CESG is paid until the end of the year the child turns 17.');
        var r = C.resp({ birth: birth, prov: a.val('prov'), income: a.n('income'), kids: Math.max(1, a.n('kids')), annual: a.n('annual'), pastContrib: a.n('past'), pastCesg: a.n('pastg'), ret: a.n('ret') / 100 });
        var t = r.thisYear;
        var h = head('Grants on your ' + CUR + ' contribution', money(t[3] + t[4] + t[5]));
        h += kv([['CESG and Additional CESG to age 17', money(r.cesg)], ['Canada Learning Bond', money(r.clb)], ['Provincial grant', money(r.prov)], ['Your contributions', money(r.contrib)], ['Estimated plan value at 17', money(r.bal)]]);
        h += table(['Year', 'Age', 'You contribute', 'CESG + A-CESG', 'CLB', 'Provincial', 'Value at year end'], r.rows.map(function (x) { return [x[0], x[1], money(x[2]), money(x[3]), money(x[4]), money(x[5]), money(x[6])]; }));
        h += how('Basic CESG is ' + pct(R().cesg_rate, 0) + ' of contributions, up to ' + money(R().cesg_annual) + ' a year, or ' + money(R().cesg_max_year) + ' when you catch up unused room, to a lifetime ' + money(R().cesg_lifetime) + '. Additional CESG adds ' + pct(R().acesg_rates[0], 0) + ' or ' + pct(R().acesg_rates[1], 0) + ' on the first ' + money(R().acesg_on_first) + ' each year, depending on family income. The Canada Learning Bond needs no contribution: ' + money(R().clb_first) + ' in the first eligible year and ' + money(R().clb_yearly) + ' a year after, up to ' + money(R().clb_max) + ', for lower-income families. For 16 and 17 year olds, CESG is paid only if at least ' + money(R().cesg_age16_total) + ' was contributed, or at least $100 a year in any 4 years, before the end of the year the child turned 15. Growth uses your example return.');
        return h;
      },
      next: [['/accounts/resp-grants/', 'RESP grants explained'], ['/accounts/resp/', 'RESP guide'], ['/compare/best-resp-providers/', 'Compare RESP providers']]
    });
    function R() { return D.resp; }
  };

  /* ---------- RRIF minimum withdrawal ---------- */
  W['rrif-minimum'] = function (el) {
    shell(el, 'rrif-minimum', {
      title: 'RRIF minimum withdrawal calculator',
      intro: 'Your minimum is the RRIF value on January 1 times the factor for your age at the start of the year. You can use a younger spouse\'s age.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'age', 'Age on January 1 (yours or your younger spouse\'s)', 72, { min: 50, max: 110, step: 1 }) +
          fNum(p, 'fmv', 'RRIF value on January 1', 300000, { min: 0 }) +
          fNum(p, 'ret', 'Example assumption: yearly return (%)', 4, { min: -10, max: 15 }) +
          fNum(p, 'years', 'Years to project', 10, { min: 1, max: 40, step: 1 }) + '</div>';
      },
      calc: function (a) {
        var age = Math.round(a.n('age')), v = a.n('fmv'), r = a.n('ret') / 100, n = Math.round(a.n('years')), rows = [];
        var f = C.rrifFactor(age), m = v * f;
        for (var i = 0; i < n && v > 0; i++) {
          var fa = C.rrifFactor(age + i), mi = v * fa; rows.push([age + i, pct(fa, 2), money(v), money(mi)]); v = (v - mi) * (1 + r);
        }
        return head('Minimum withdrawal this year', money(m)) + kv([['Factor at age ' + age, pct(f, 2)], ['Per month', money(m / 12)], ['Withholding on the minimum', '$0']]) +
          msg('ok', 'No tax is withheld on the minimum. Amounts above it have withholding of ' + D.rrsp.withholding_text + '. All RRIF income is taxable in the year received.') +
          table(['Age on Jan 1', 'Factor', 'Value on Jan 1', 'Minimum'], rows, 'Projection with your example return (minimum taken at the start of each year)') +
          how('Under age 71 the factor is 1 / (90 - age). From 71 the prescribed factors apply, reaching 20% at 95 and over. No minimum applies in the year the RRIF is opened.');
      },
      next: [['/accounts/rrif-minimum-withdrawal/', 'RRIF minimum withdrawal table'], ['/compare/best-rrif-accounts/', 'Compare RRIF accounts']]
    });
  };

  /* ---------- Home Buyers' Plan repayment ---------- */
  W['hbp-repayment'] = function (el) {
    shell(el, 'hbp-repayment', {
      title: 'Home Buyers\' Plan repayment calculator',
      intro: 'Withdraw up to ' + money(D.hbp.max) + ' from your RRSP for a first home and repay it over ' + D.hbp.repay_years + ' years.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Amount withdrawn under the HBP', 35000, { min: 0, max: D.hbp.max }) +
          fSel(p, 'yr', 'Year of the first withdrawal', yearOpts(2015, CUR + 1), CUR) + '</div>';
      },
      calc: function (a) {
        var y = a.n('yr'), cap = y < 2024 ? D.hbp.prev : D.hbp.max, amt = Math.min(a.n('amt'), cap);   // v1.5: limit in force in the withdrawal year
        var deferred = y >= D.hbp.deferral[0] && y <= D.hbp.deferral[1];
        var start = y + (deferred ? D.hbp.deferral_start : 2);
        var ann = amt / D.hbp.repay_years;
        var h = head('Minimum yearly repayment', money2(ann)) + kv([['First repayment year', String(start)], ['Last repayment year', String(start + D.hbp.repay_years - 1)], ['Repay by', 'within 60 days after December 31, ' + start]]);
        if (a.n('amt') > cap) h += msg('warnmsg', 'The limit for withdrawals in ' + y + ' was ' + money(cap) + ', so the calculation uses ' + money(cap) + '.');
        if (y === 2024 && amt > D.hbp.prev) h += msg('warnmsg', 'The ' + money(D.hbp.max) + ' limit applies to withdrawals made after ' + D.hbp.prev_until + '. Withdrawals on or before that date had a ' + money(D.hbp.prev) + ' limit.');
        if (deferred) h += msg('ok', 'Withdrawals from ' + D.hbp.deferral[0] + ' to ' + D.hbp.deferral[1] + ' get extra time: repayment starts in the ' + D.hbp.deferral_start + 'th year after the withdrawal.');
        h += msg('warnmsg', 'Any amount below the yearly minimum is added to your income for that year and taxed.');
        h += how('The HBP balance is repaid in ' + D.hbp.repay_years + ' equal yearly amounts. You can repay more, which lowers later minimums. Designate repayments on Schedule 7 of your return.');
        return h;
      },
      next: [['/accounts/home-buyers-plan/', 'Home Buyers\' Plan guide'], ['/vs/fhsa-vs-rrsp/', 'FHSA vs RRSP Home Buyers\' Plan']]
    });
  };

  /* ---------- First home down payment planner (FHSA + HBP) ---------- */
  W['first-home'] = function (el) {
    shell(el, 'first-home', {
      title: 'First home savings planner: FHSA plus Home Buyers\' Plan',
      intro: 'See how much a single buyer or a couple could put toward a first home from FHSAs and RRSPs.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fRadio(p, 'who', 'Buying', [['1', 'Alone'], ['2', 'With a spouse or partner']], '1') +
          fNum(p, 'years', 'Years until you buy', 4, { min: 1, max: 15, step: 1 }) +
          fNum(p, 'fhsa', 'Current FHSA balance, per person', 0, { min: 0 }) +
          fNum(p, 'rrsp', 'RRSP balance available for the HBP, per person', 20000, { min: 0 }) +
          fNum(p, 'ret', 'Example assumption: yearly return (%)', 3, { min: -10, max: 15 }) + '</div>';
      },
      calc: function (a) {
        var who = +a.val('who') || 1, n = Math.round(a.n('years')), r = a.n('ret') / 100, F = D.fhsa;
        var bal = a.n('fhsa'), contrib = 0, room = F.annual;
        for (var i = 0; i < n; i++) { var c = Math.min(room, F.lifetime - contrib); bal = (bal + c) * (1 + r); contrib += c; room = F.annual; }
        var hbp = Math.min(D.hbp.max, a.n('rrsp') * Math.pow(1 + r, n));
        var tot = (bal + hbp) * who;
        return head('Possible first-home funds in ' + n + ' year' + (n > 1 ? 's' : ''), money(tot)) +
          kv([['FHSA, per person', money(bal)], ['FHSA contributions, per person', money(contrib)], ['HBP withdrawal, per person', money(hbp)], ['Persons', String(who)]]) +
          how('Assumes the maximum ' + money(F.annual) + ' FHSA contribution each year from now, capped at ' + money(F.lifetime) + ' lifetime, and the HBP limit of ' + money(D.hbp.max) + ' per person. FHSA withdrawals for a qualifying home are tax-free and never repaid. HBP withdrawals must be repaid over ' + D.hbp.repay_years + ' years. You can use both for the same home.');
      },
      next: [['/vs/fhsa-vs-rrsp/', 'FHSA vs RRSP'], ['/vs/fhsa-vs-tfsa/', 'FHSA vs TFSA'], ['/compare/best-fhsa-accounts/', 'Compare FHSA accounts']]
    });
  };

  /* ---------- TFSA vs RRSP ---------- */
  W['tfsa-vs-rrsp'] = function (el) {
    shell(el, 'tfsa-vs-rrsp', {
      title: 'TFSA vs RRSP calculator',
      intro: 'Compare what the same pre-tax dollars are worth after tax in each account, based on your tax rate now and in retirement.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'now', 'Taxable income now', MEM.get('income', 75000), { min: 0 }) +
          fNum(p, 'later', 'Expected taxable income when you withdraw', 50000, { min: 0 }) +
          fNum(p, 'amt', 'Pre-tax amount to invest', 10000, { min: 0 }) +
          fNum(p, 'years', 'Years invested', 25, { min: 1, max: 60, step: 1 }) +
          fNum(p, 'ret', 'Example assumption: yearly return (%)', 5, { min: -10, max: 15 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), tn = C.marginal(prov, a.n('now')), tl = C.marginal(prov, a.n('later')), amt = a.n('amt'), g = Math.pow(1 + a.n('ret') / 100, a.n('years'));
        var rr = amt * g * (1 - tl), tf = amt * (1 - tn) * g, diff = rr - tf;
        var h = head(Math.abs(diff) < 1 ? 'Same result in both accounts' : ((diff > 0 ? 'RRSP' : 'TFSA') + ' leaves you more, by'), Math.abs(diff) < 1 ? money(0) : money(Math.abs(diff)));
        h += kv([['Your marginal rate now', pct(tn, 1)], ['Marginal rate at withdrawal', pct(tl, 1)], ['RRSP after tax', money(rr)], ['TFSA after tax', money(tf)]]);
        h += how('RRSP: the full pre-tax amount is invested because the deduction refunds the tax, then withdrawals are taxed at your future rate. TFSA: you invest after-tax dollars and withdraw tax-free. When the two rates are equal, the results are equal. Withdrawals can also reduce income-tested benefits such as OAS and GIS, which this does not include.');
        return h;
      },
      next: [['/vs/tfsa-vs-rrsp/', 'TFSA vs RRSP guide'], ['/calculators/rrsp-calculator/', 'RRSP refund calculator'], ['/calculators/tfsa-calculator/', 'TFSA room calculator']]
    });
  };

  /* ---------- Which account fits (general information) ---------- */
  W['account-chooser'] = function (el) {
    shell(el, 'account-chooser', {
      title: 'Which account fits your goal?',
      intro: 'Five quick questions. We show which registered accounts are built for your goal and why. General information, not a recommendation.',
      button: 'Show my accounts',
      fields: function (p) {
        return fSel(p, 'goal', 'What are you saving for?', [['home', 'A first home'], ['retire', 'Retirement'], ['kid', 'A child\'s education'], ['flex', 'Flexible savings or any goal']], 'retire') +
          fNum(p, 'age', 'Your age', CUR - bornDefault(), { min: 16, max: 100, step: 1 }) +
          fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'income', 'Taxable income', MEM.get('income', 60000), { min: 0 }) +
          fRadio(p, 'own', 'Have you owned and lived in a home in the last four calendar years or this year?', [['n', 'No'], ['y', 'Yes']], 'n');
      },
      calc: function (a) {
        var goal = a.val('goal'), age = a.n('age'), mr = C.marginal(a.val('prov'), a.n('income')), own = a.val('own') === 'y', L = [];
        var hi = mr >= 0.30;
        if (goal === 'home') {
          if (!own && age >= 18 && age <= D.fhsa.max_age) L.push(['FHSA', 'Deductible like an RRSP and tax-free out for a qualifying first home: ' + money(D.fhsa.annual) + ' a year, ' + money(D.fhsa.lifetime) + ' lifetime.', '/accounts/fhsa/']);
          L.push(['TFSA', 'Tax-free growth and withdrawals at any time, with no home-buying conditions.', '/accounts/tfsa/']);
          if (!own) L.push(['RRSP Home Buyers\' Plan', 'Borrow up to ' + money(D.hbp.max) + ' from your RRSP for a first home and repay over ' + D.hbp.repay_years + ' years.', '/accounts/home-buyers-plan/']);
        } else if (goal === 'retire') {
          if (hi) { L.push(['RRSP', 'At your ' + pct(mr, 1) + ' marginal rate, the deduction is valuable. Withdrawals are taxed later, often at a lower rate.', '/accounts/rrsp/']); L.push(['TFSA', 'Tax-free growth; withdrawals do not affect OAS or GIS.', '/accounts/tfsa/']); }
          else { L.push(['TFSA', 'At a ' + pct(mr, 1) + ' marginal rate, the RRSP deduction is worth less, and TFSA withdrawals never count as income.', '/accounts/tfsa/']); L.push(['RRSP', 'Still useful if you expect a lower rate in retirement or have workplace matching.', '/accounts/rrsp/']); }
          if (age >= 65) L.push(['RRIF', 'Your RRSP must become a RRIF or annuity by the end of the year you turn 71.', '/accounts/rrif-minimum-withdrawal/']);
        } else if (goal === 'kid') {
          L.push(['RESP', 'Grants of 20% on contributions through the CESG, up to ' + money(D.resp.cesg_lifetime) + ' per child, plus the Canada Learning Bond for lower-income families.', '/accounts/resp/']);
          L.push(['TFSA', 'A flexible back-up with no education conditions.', '/accounts/tfsa/']);
        } else {
          L.push(['TFSA', 'The most flexible account: tax-free growth and withdrawals at any time, and room comes back the next year.', '/accounts/tfsa/']);
          L.push(['Non-registered account', 'No limits, but interest, dividends and gains are taxable each year.', '/accounts/']);
        }
        return head('Accounts built for this goal', L.map(function (x) { return x[0]; }).join(', ')) + '<ol>' + L.map(function (x) { return '<li><a href="' + x[2] + '"><b>' + x[0] + '</b></a>: ' + x[1] + '</li>'; }).join('') + '</ol>' +
          msg('warnmsg', 'General information only. The right mix depends on your full situation, including workplace plans, debts and benefits.');
      },
      next: [['/accounts/', 'All account types'], ['/compare/best-online-brokers/', 'Where to open them']]
    });
  };

  /* ---------- US withholding tax ---------- */
  W['us-withholding'] = function (el) {
    var A = D.us_withholding;
    shell(el, 'us-withholding', {
      title: 'US dividend withholding tax calculator',
      intro: 'See how much of your US dividends the IRS keeps in each Canadian account, and whether you can get it back.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'acct', 'Account type', A.accounts.map(function (x) { return [x[0], x[1]]; }), 'tfsa') +
          fNum(p, 'div', 'US dividends per year (USD)', 1000, { min: 0 }) +
          fRadio(p, 'w8', 'W-8BEN on file with your broker?', [['y', 'Yes'], ['n', 'No']], 'y') + '</div>';
      },
      calc: function (a) {
        var acc = A.accounts.filter(function (x) { return x[0] === a.val('acct'); })[0], d = a.n('div');
        var rate = acc[2] ? 0 : (a.val('w8') === 'y' ? A.treaty : A.no_w8);
        var h = head('US tax withheld each year', money2(d * rate) + ' USD') + kv([['Withholding rate', pct(rate, 0)], ['Recoverable?', acc[3]]]);
        h += msg(acc[2] ? 'ok' : 'warnmsg', acc[4]);
        h += how('The Canada-US tax treaty sets ' + pct(A.treaty, 0) + ' withholding on US dividends for Canadian residents who file a W-8BEN, and ' + pct(A.no_w8, 0) + ' without one. The treaty exempts accounts set up for retirement income, such as an RRSP, RRIF or LIRA, when you hold US-listed securities directly. A TFSA, RESP and FHSA are not treated as retirement accounts, so the withholding is a permanent cost there.');
        return h;
      },
      next: [['/accounts/us-stocks-in-tfsa/', 'US stocks in a TFSA'], ['/compare/best-rrsp-for-us-stocks/', 'Best RRSP for US stocks']]
    });
  };

  /* ---------- Annual broker cost ---------- */
  W['broker-cost'] = function (el) {
    shell(el, 'broker-cost', {
      title: 'What will each broker cost you in a year?',
      intro: 'Enter how you invest. We total commissions, options fees and account fees at every broker we cover, at published prices.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'cad', 'Canadian stock and ETF trades per month', 2, { min: 0, step: 1 }) +
          fNum(p, 'us', 'US stock and ETF trades per month', 1, { min: 0, step: 1 }) +
          fNum(p, 'opts', 'Options trades per month', 0, { min: 0, step: 1 }) +
          fNum(p, 'contracts', 'Contracts per options trade', 1, { min: 1, step: 1 }) + '</div>';
      },
      calc: function (a) {
        var o = { cad: a.n('cad'), us: a.n('us'), opts: a.n('opts'), contracts: a.n('contracts') };
        var rows = D.brokers.map(function (b) { return { b: b, c: C.brokerAnnual(b, o) }; }).filter(function (r) { return !(o.opts > 0 && r.b.opt_base == null); }).sort(function (x, y) { return x.c.total - y.c.total; });
        var tied = rows.filter(function (r) { return Math.abs(r.c.total - rows[0].c.total) < 0.005; });
        return head('Lowest estimated yearly cost', money(rows[0].c.total) + ' at ' + (tied.length > 1 ? tied.length + ' brokers: ' + tied.map(function (r) { return r.b.name; }).join(', ') : rows[0].b.name)) +
          table(['Broker', 'Commissions', 'Options', 'Account fees', 'Total a year'], rows.map(function (r) {
            return ['<a href="' + r.b.review + '">' + r.b.name + '</a>', money(r.c.cad + r.c.us), money(r.c.opts), money(r.c.fees), '<b>' + money(r.c.total) + '</b>'];
          })) + how('Uses each broker\'s published standard pricing for a self-directed account. Per-share commissions assume 40 shares per order. Account fees include any recurring fee you cannot avoid at a typical balance; most fees can be waived. ECN fees, regulatory fees and promotional pricing are not included. Prices change, so check the review for the date each price was confirmed.');
      },
      next: [['/compare/best-online-brokers/', 'Best online brokers'], ['/methodology/brokers/', 'How we rate brokers']]
    });
  };

  /* ---------- Options cost ---------- */
  W['options-cost'] = function (el) {
    shell(el, 'options-cost', {
      title: 'Options trading cost calculator',
      intro: 'Yearly options commissions at each broker for your trading pattern.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'trades', 'Options trades per month', 4, { min: 0, step: 1 }) + fNum(p, 'contracts', 'Contracts per trade', 2, { min: 1, step: 1 }) + '</div>'; },
      calc: function (a) {
        var t = a.n('trades'), k = a.n('contracts');
        var rows = D.brokers.filter(function (b) { return b.opt_base != null; }).map(function (b) { var per = Math.max(b.opt_base + b.opt_contract * k, b.opt_min || 0); return { b: b, per: per, yr: per * t * 12 }; }).sort(function (x, y) { return x.yr - y.yr; });
        var tied = rows.filter(function (r) { return Math.abs(r.yr - rows[0].yr) < 0.005; });
        return head('Lowest yearly options cost', money(rows[0].yr) + ' at ' + (tied.length > 1 ? tied.length + ' brokers: ' + tied.map(function (r) { return r.b.name; }).join(', ') : rows[0].b.name)) + table(['Broker', 'Pricing', 'Per trade', 'Per year'], rows.map(function (r) { return ['<a href="' + r.b.review + '">' + r.b.name + '</a>', r.b.opt_text, money2(r.per), money(r.yr)]; })) +
          how('Per trade = base commission plus the per-contract fee times the number of contracts. Exercise and assignment fees, and exchange or regulatory fees, are extra at most brokers.');
      },
      next: [['/compare/best-options-trading-platforms/', 'Best options platforms']]
    });
  };

  /* ---------- Margin interest ---------- */
  W['margin-interest'] = function (el) {
    shell(el, 'margin-interest', {
      title: 'Margin interest calculator',
      intro: 'Interest on a margin loan at each broker\'s published rate, or a rate you enter.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Amount borrowed (CAD)', 20000, { min: 0 }) + fNum(p, 'days', 'Days borrowed', 365, { min: 1, step: 1 }) + fNum(p, 'rate', 'Or your own annual rate (%)', '', { min: 0, max: 30, ph: 'optional' }) + '</div>'; },
      calc: function (a) {
        var amt = a.n('amt'), d = a.n('days'), own = a.val('rate');
        if (own !== '') { var i = amt * num(own) / 100 * d / 365; return head('Interest for ' + d + ' days', money2(i)) + how('Interest = amount x annual rate x days / 365. Brokers charge interest daily and post it monthly.'); }
        var rows = D.brokers.filter(function (b) { return b.margin_cad != null; }).map(function (b) { return { b: b, i: amt * b.margin_cad * d / 365 }; }).sort(function (x, y) { return x.i - y.i; });
        return head('Lowest interest for ' + d + ' days', money2(rows[0].i) + ' at ' + rows[0].b.name) + table(['Broker', 'Published CAD margin rate', 'Interest'], rows.map(function (r) { return ['<a href="' + r.b.review + '">' + r.b.name + '</a>', r.b.margin_text, money2(r.i)]; })) +
          how('Uses each broker\'s published rate for its smallest loan tier, as shown in the table, on the whole amount. Several brokers charge less on larger balances; the margin page lists their tiers. Rates float with the prime rate or the broker\'s benchmark and change without notice. Margin interest on money borrowed to earn investment income in a non-registered account is generally tax-deductible.');
      },
      next: [['/compare/best-margin-accounts/', 'Lowest margin rates']]
    });
  };

  /* ---------- Robo-advisor fees ---------- */
  W['robo-fee'] = function (el) {
    shell(el, 'robo-fee', {
      title: 'Robo-advisor fee calculator',
      intro: 'Yearly management fee plus fund costs at each robo-advisor for the amount you invest.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Amount invested', 50000, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var amt = a.n('amt');
        var rows = D.robos.map(function (r) { return { r: r, c: C.roboFee(r, amt), ok: amt >= (r.min || 0) }; }).sort(function (x, y) { return x.c.total - y.c.total; });
        return head('Lowest yearly cost', money(rows[0].c.total) + ' at ' + rows[0].r.name) + table(['Robo-advisor', 'Management fee', 'Fund costs (MER)', 'Total a year', 'Minimum'], rows.map(function (x) {
          return [x.r.review ? '<a href="' + x.r.review + '">' + x.r.name + '</a>' : x.r.name, money(x.c.mgmt) + ' <span class="ws-note">' + x.r.fee_text + '</span>', money(x.c.mer) + ' <span class="ws-note">' + x.r.mer_text + '</span>', '<b>' + money(x.c.total) + '</b>', x.ok ? money(x.r.min || 0) : '<span style="color:var(--ws-bad)">' + money(x.r.min) + ' needed</span>'];
        })) + how('Management fee from each robo-advisor\'s published schedule. Fund costs use the highest published fund cost (MER) for each robo-advisor\'s core portfolios, as in our methodology. Your actual fund costs depend on the portfolio you choose.');
      },
      next: [['/compare/best-robo-advisors/', 'Best robo-advisors'], ['/calculators/compound-interest-calculator/', 'Fee drag over time']]
    });
  };

  /* ---------- Fee drag ---------- */
  W['fee-drag'] = function (el) {
    shell(el, 'fee-drag', {
      title: 'Investment fee impact calculator',
      intro: 'See what a higher fee costs over time on the same investments.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'pv', 'Starting amount', 25000, { min: 0 }) + fNum(p, 'pmt', 'Monthly contribution', 300, { min: 0 }) + fNum(p, 'years', 'Years', 25, { min: 1, max: 60, step: 1 }) +
          fNum(p, 'ret', 'Example assumption: return before fees (%)', 6, { min: -10, max: 15 }) + fNum(p, 'fa', 'Fee A (% a year)', 0.25, { min: 0, max: 5 }) + fNum(p, 'fb', 'Fee B (% a year)', 2, { min: 0, max: 5 }) + '</div>';
      },
      calc: function (a) {
        var y = a.n('years'), r = a.n('ret') / 100;
        var A = C.grow(a.n('pv'), a.n('pmt'), r - a.n('fa') / 100, y, 12), B = C.grow(a.n('pv'), a.n('pmt'), r - a.n('fb') / 100, y, 12);
        return head('Difference after ' + y + ' years', money(A.bal - B.bal)) + kv([['Ending value at ' + a.n('fa') + '%', money(A.bal)], ['Ending value at ' + a.n('fb') + '%', money(B.bal)], ['You contribute', money(A.contrib)]]) +
          how('Fees are taken from returns every year, so the gap compounds. Each scenario grows monthly at the return minus its fee.');
      },
      next: [['/compare/best-robo-advisors/', 'Compare robo-advisor fees'], ['/learn/how-to-invest/', 'How to invest in Canada']]
    });
  };

  /* ---------- Compound interest ---------- */
  W['compound-interest'] = function (el) {
    shell(el, 'compound-interest', {
      title: 'Compound interest calculator',
      intro: 'Starting amount, monthly saving, rate and time. See the year-by-year growth.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'pv', 'Starting amount', 10000, { min: 0 }) + fNum(p, 'pmt', 'Monthly contribution', 500, { min: 0 }) +
          fNum(p, 'rate', 'Annual interest or return (%)', 5, { min: -10, max: 30 }) + fNum(p, 'years', 'Years', 20, { min: 1, max: 70, step: 1 }) +
          fSel(p, 'comp', 'Compounding', [[1, 'Yearly'], [2, 'Semi-annually'], [4, 'Quarterly'], [12, 'Monthly'], [365, 'Daily']], 12) + '</div>';
      },
      calc: function (a) {
        var g = C.grow(a.n('pv'), a.n('pmt'), a.n('rate') / 100, a.n('years'), a.n('comp') || 12);
        return head('Value after ' + a.n('years') + ' years', money(g.bal)) + kv([['Total contributed', money(g.contrib)], ['Interest and growth', money(g.interest)], ['Growth share of the total', pct(g.bal ? g.interest / g.bal : 0, 0)]]) +
          bars(g.rows.map(function (r) { return { total: r[2], part: Math.max(0, r[2] - r[1]), label: 'Year ' + r[0] }; }), ['Growth', 'Contributions']) +
          table(['Year', 'Contributed to date', 'Value at year end'], g.rows.map(function (r) { return [r[0], money(r[1]), money(r[2])]; })) +
          how('Contributions are added at the end of each month. The rate is converted to an effective monthly rate using your compounding choice. Tax and fees are not included; use a TFSA or RRSP to shelter growth.');
      },
      next: [['/accounts/tfsa/', 'Grow it tax-free in a TFSA'], ['/savings/gic-rates/', 'GIC rates'], ['/savings/high-interest-savings-accounts/', 'Savings rates']]
    });
  };

  /* ---------- Savings goal ---------- */
  W['savings-goal'] = function (el) {
    shell(el, 'savings-goal', {
      title: 'Savings goal calculator',
      intro: 'How much to save each month to reach a target by a date.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'goal', 'Target amount', 50000, { min: 0 }) + fNum(p, 'have', 'Saved so far', 5000, { min: 0 }) + fNum(p, 'years', 'Years to reach it', 5, { min: 0.25, max: 60 }) + fNum(p, 'rate', 'Interest or return (% a year)', 3, { min: 0, max: 20 }) + '</div>'; },
      calc: function (a) {
        var n = Math.round(a.n('years') * 12), i = Math.pow(1 + a.n('rate') / 100, 1 / 12) - 1, fv = a.n('goal') - a.n('have') * Math.pow(1 + i, n);
        var pmt = fv <= 0 ? 0 : (i ? fv * i / (Math.pow(1 + i, n) - 1) : fv / n);
        return head('Save each month', money(pmt)) + kv([['Months', String(n)], ['Total you put in', money(pmt * n + a.n('have'))], ['Interest earned', money(a.n('goal') - pmt * n - a.n('have'))]]) + how('Monthly saving at the end of each month, growing at the effective monthly rate.');
      },
      next: [['/savings/high-interest-savings-accounts/', 'Best savings rates'], ['/accounts/fhsa/', 'Saving for a home? FHSA']]
    });
  };

  /* ---------- GIC ---------- */
  W['gic-calc'] = function (el) {
    shell(el, 'gic-calc', {
      title: 'GIC calculator',
      intro: 'Interest and maturity value for a GIC at any rate, term and compounding.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'pv', 'Amount invested', 10000, { min: 0 }) + fNum(p, 'rate', 'Annual rate (%)', D.gic_default_rate || 3, { min: 0, max: 15 }) +
          fNum(p, 'term', 'Term (years)', 2, { min: 0.25, max: 10, step: 0.25 }) +
          fSel(p, 'comp', 'Interest paid', [['1', 'Compounded yearly'], ['2', 'Compounded semi-annually'], ['12', 'Compounded monthly'], ['simple', 'Paid out yearly (simple)']], '1') +
          fSel(p, 'prov', 'Province (for tax outside a TFSA)', provOpts(), provDefault()) + fNum(p, 'income', 'Your taxable income', MEM.get('income', 60000), { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var pv = a.n('pv'), r = a.n('rate') / 100, t = a.n('term'), c = a.val('comp');
        var mv = c === 'simple' ? pv + pv * r * t : pv * Math.pow(1 + r / +c, +c * t);
        var intr = mv - pv, mr = C.marginal(a.val('prov'), a.n('income'));
        return head('Value at maturity', money2(mv)) + kv([['Interest earned', money2(intr)], ['Tax in a non-registered account', money2(intr * mr)], ['Interest after tax', money2(intr * (1 - mr))], ['In a TFSA', money2(intr) + ' tax-free']]) +
          how('Compound GICs reinvest interest at the same rate. Interest on a multi-year compound GIC held outside a registered account is taxable every year on each anniversary, even though you receive it at maturity.');
      },
      next: [['/savings/gic-rates/', 'Best GIC rates'], ['/vs/gic-vs-hisa/', 'GIC vs savings account']]
    });
  };

  W['gic-ladder'] = function (el) {
    shell(el, 'gic-ladder', {
      title: 'GIC ladder builder',
      intro: 'Split one amount across 1 to 5-year GICs so part of your money comes due every year.',
      fields: function (p) {
        var b = D.gic_best || {};
        return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Total to invest', 25000, { min: 0 }) +
          [1, 2, 3, 4, 5].map(function (y) { return fNum(p, 'r' + y, y + '-year rate (%)', b[y] || '', { min: 0, max: 15 }); }).join('') + '</div>';
      },
      calc: function (a) {
        var part = a.n('amt') / 5, rows = [], tot = 0;
        for (var y = 1; y <= 5; y++) { var r = a.n('r' + y) / 100, mv = part * Math.pow(1 + r, y); tot += mv - part; rows.push([y + ' year', pct(r, 2), money(part), money(mv), String(CUR + y)]); }
        var avg = 0; for (var k = 1; k <= 5; k++) avg += a.n('r' + k); avg /= 5;
        return head('Average rate across the ladder', nf(avg, 2) + '%') + table(['Rung', 'Rate', 'Invested', 'At maturity', 'Matures in'], rows) +
          how('Each rung holds one fifth of the money. When a rung matures, reinvesting it in a new 5-year GIC keeps one GIC maturing every year. Rates default to the best published rates in our GIC table and can be changed.');
      },
      next: [['/savings/gic-rates/', 'Best GIC rates']]
    });
  };

  /* ---------- HISA earnings (data-list="usd" for US-dollar accounts) ---------- */
  W['hisa-earnings'] = function (el) {
    var usd = el.getAttribute('data-list') === 'usd', list = usd ? D.usd_savings : D.hisa, cur = usd ? ' USD' : '';
    shell(el, 'hisa-earnings', {
      title: usd ? 'US dollar savings interest calculator' : 'Savings account interest calculator',
      intro: 'Compare what your balance earns at each account\'s published everyday rate.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'bal', 'Balance' + cur, usd ? 10000 : 20000, { min: 0 }) + fNum(p, 'months', 'Months', 12, { min: 1, max: 120, step: 1 }) + '</div>'; },
      calc: function (a) {
        var bal = a.n('bal'), m = a.n('months');
        var rows = list.map(function (h) { return { h: h, i: bal * (Math.pow(1 + h.rate / 12, m) - 1) }; }).sort(function (x, y) { return y.i - x.i; });
        return head('Most interest in ' + m + ' months', money2(rows[0].i) + cur + ' at ' + rows[0].h.name) + table(['Account', 'Everyday rate', 'Interest earned' + cur, 'Protection'], rows.map(function (r) { return [r.h.link ? '<a href="' + r.h.link + '">' + r.h.name + '</a>' : r.h.name, pct(r.h.rate, 2) + (r.h.rate_note ? ' <span class="ws-note">' + r.h.rate_note + '</span>' : ''), money2(r.i), r.h.ins]; })) +
          how('Everyday (non-promotional) rates, interest calculated daily and paid monthly, rates held steady for the period. Savings rates change often; our rate table shows the date each rate was checked.' + (usd ? ' Interest on US dollar accounts is taxable in Canada and is reported in Canadian dollars.' : ''));
      },
      next: usd ? [['/savings/usd-savings-accounts/', 'Best USD savings accounts'], ['/markets/how-to-buy-us-stocks/', 'How to buy US stocks']] : [['/savings/high-interest-savings-accounts/', 'Best savings accounts'], ['/vs/gic-vs-hisa/', 'GIC vs savings account']]
    });
  };

  /* ---------- Credit card cash back ---------- */
  W['card-cashback'] = function (el) {
    // v1.5: opens with the Wealthsimple card only when the page asks for it (data-card="wealthsimple"); otherwise neutral values.
    // A page can preset its own card with data-rate (cash back %) and data-fee (fee per month).
    var K = D.cards || [], ws = el.getAttribute('data-card') === 'wealthsimple' && K[0] ? K[0] : null;
    var r0 = parseFloat(el.getAttribute('data-rate')), f0 = parseFloat(el.getAttribute('data-fee'));
    var rate0 = !isNaN(r0) ? r0 : (ws ? ws.rate * 100 : 2), fee0 = !isNaN(f0) ? f0 : (ws ? ws.fee_month : 0);
    shell(el, 'card-cashback', {
      title: 'Cash back calculator',
      intro: 'Your yearly cash back after the card fee, at your own spending.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'spend', 'Monthly card spending', 2000, { min: 0 }) +
          fNum(p, 'rate', 'Cash back rate (%)', rate0, { min: 0, max: 10 }) +
          fNum(p, 'fee', 'Card fee per month', fee0, { min: 0, help: ws ? ws.fee_note : 'Divide a yearly fee by 12.' }) + '</div>';
      },
      calc: function (a) {
        var yr = a.n('spend') * 12, cb = yr * a.n('rate') / 100, fee = a.n('fee') * 12, net = cb - fee;
        var be = a.n('rate') ? a.n('fee') / (a.n('rate') / 100) : 0;
        return head('Net cash back a year', money(net), net < 0) + kv([['Cash back earned', money(cb)], ['Card fees', money(fee)], ['Monthly spend to cover the fee', money(be)]]) +
          how('Cash back = yearly spending x the rate. Net = cash back minus fees. Fee waivers and caps on rewards are listed in the card review.');
      },
      next: ws ? [['/reviews/wealthsimple/visa-infinite-card/', 'Wealthsimple credit card review'], ['/reviews/wealthsimple/membership-tiers/', 'Wealthsimple tiers']]
        : [['/credit-cards/best-cash-back-credit-cards/', 'Best cash back credit cards'], ['/credit-cards/best-credit-cards/', 'Best credit cards']]
    });
  };

  /* ---------- CDIC deposit insurance checker ---------- */
  W['deposit-insurance'] = function (el) {
    var I = D.deposit_insurance;
    shell(el, 'deposit-insurance', {
      title: 'CDIC coverage checker',
      intro: 'CDIC covers eligible deposits up to ' + money(I.limit) + ' per category at each member institution. Enter your balances at one bank.',
      fields: function (p) { return '<div class="ws-w-grid">' + I.categories.map(function (c, i) { return fNum(p, 'c' + i, c, i === 0 ? 50000 : 0, { min: 0 }); }).join('') + '</div>'; },
      calc: function (a) {
        var tot = 0, cov = 0, rows = I.categories.map(function (c, i) { var b = a.n('c' + i), cv = Math.min(b, I.limit); tot += b; cov += cv; return [c, money(b), money(cv), b > I.limit ? '<span style="color:var(--ws-bad)">' + money(b - I.limit) + ' over</span>' : 'Fully covered']; });
        return head('Covered by CDIC', money(cov) + ' of ' + money(tot), cov < tot) + table(['Category', 'Your balance', 'Covered', 'Status'], rows) +
          how('Each category is covered separately up to ' + money(I.limit) + ' at each CDIC member, including principal and interest. Joint accounts, trust deposits and each registered plan type are separate categories. Mutual funds, stocks, ETFs and crypto are not covered by CDIC; securities at a CIRO dealer are protected by CIPF if the dealer fails. ' + (I.note || ''));
      },
      next: [['/reviews/wealthsimple/is-wealthsimple-safe/', 'Is Wealthsimple safe?'], ['/savings/high-interest-savings-accounts/', 'Best savings accounts']]
    });
  };

  /* ---------- CIPF coverage ---------- */
  W['cipf-coverage'] = function (el) {
    var P = D.cipf;
    shell(el, 'cipf-coverage', {
      title: 'CIPF coverage checker',
      intro: 'CIPF protects client property held at a member firm that becomes insolvent, up to ' + money(P.limit) + ' in each of three account groups. Enter your balances at one investment dealer.',
      fields: function (p) { return '<div class="ws-w-grid">' + P.groups.map(function (g, i) { return fNum(p, 'g' + i, g[0], i === 0 ? 150000 : 0, { min: 0, help: g[1] }); }).join('') + '</div>'; },
      calc: function (a) {
        var tot = 0, cov = 0, rows = P.groups.map(function (g, i) { var b = a.n('g' + i), cv = Math.min(b, P.limit); tot += b; cov += cv; return [g[0], money(b), money(cv), b > P.limit ? '<span style="color:var(--ws-bad)">' + money(b - P.limit) + ' over the limit</span>' : 'Within the limit']; });
        return head('Within CIPF limits at this dealer', money(cov) + ' of ' + money(tot), cov < tot) + table(['Account group', 'Your balance', 'Within the limit', 'Status'], rows) +
          how('CIPF covers client property, meaning cash and securities, held by a member firm that becomes insolvent, up to ' + money(P.limit) + ' per account group at each member firm. It does not cover market losses or a fall in the value of your investments. ' + P.groups.map(function (g) { return g[0] + ': ' + g[1] + '.'; }).join(' '));
      },
      next: [['/learn/cipf-vs-cdic/', 'CIPF vs CDIC'], ['/reviews/wealthsimple/is-wealthsimple-safe/', 'Is Wealthsimple safe?']]
    });
  };

  /* ---------- DRIP growth ---------- */
  W['drip-growth'] = function (el) {
    shell(el, 'drip-growth', {
      title: 'Dividend reinvestment (DRIP) calculator',
      intro: 'See how reinvesting dividends adds shares over time, with fractional or whole-share reinvestment.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'sh', 'Shares you own', 200, { min: 0, step: 1 }) +
          fNum(p, 'px', 'Share price today ($)', 50, { min: 0.01 }) +
          fNum(p, 'dps', 'Yearly dividend per share ($)', 2, { min: 0 }) +
          fNum(p, 'yrs', 'Years', 10, { min: 1, max: 50, step: 1 }) +
          fNum(p, 'dg', 'Example assumption: yearly dividend growth (%)', 3, { min: -20, max: 20 }) +
          fNum(p, 'pg', 'Example assumption: yearly share price growth (%)', 3, { min: -20, max: 20 }) +
          fRadio(p, 'mode', 'How dividends are reinvested', [['frac', 'Fractional shares'], ['whole', 'Whole shares only'], ['none', 'Not reinvested (paid in cash)']], 'frac') + '</div>';
      },
      calc: function (a) {
        var sh = a.n('sh'), px = a.n('px'), dps = a.n('dps'), yrs = Math.max(1, Math.round(a.n('yrs'))), dg = a.n('dg') / 100, pg = a.n('pg') / 100, mode = a.val('mode');
        var cash = 0, paid = 0, rows = [];
        for (var y = 1; y <= yrs; y++) {
          var d = sh * dps; paid += d;
          px = px * (1 + pg);
          if (mode === 'frac') { sh += d / px; }
          else if (mode === 'whole') { cash += d; var k = Math.floor(cash / px); sh += k; cash -= k * px; }
          else { cash += d; }
          dps = dps * (1 + dg);
          rows.push([y, mode === 'frac' ? sh.toFixed(3) : String(Math.round(sh)), money2(d), money(sh * px + cash)]);
        }
        var shTxt = mode === 'frac' ? sh.toFixed(3) : String(Math.round(sh));
        return head('Shares after ' + yrs + ' years', shTxt) +
          kv([['Dividends received over the period', money2(paid)], ['Cash not reinvested', money2(cash)], ['Shares plus cash at the end', money(sh * px + cash)]]) +
          table(['Year', 'Shares at year end', 'Dividends that year', 'Value at year end'], rows) +
          how('Each year the dividend equals the shares held times the dividend per share, reinvested once at the year-end price. Fractional reinvestment buys part shares; whole-share reinvestment keeps the remainder as cash until it buys a full share, as a broker DRIP that buys only whole shares does. Growth rates are example assumptions, not forecasts. Taxes, withholding and commissions are not included.');
      },
      next: [['/compare/best-brokers-for-dividend-investing/', 'Best brokers for dividend investing'], ['/calculators/compound-interest-calculator/', 'Compound interest calculator']]
    });
  };

  /* ---------- Chequing account cost ---------- */
  W['chequing-cost'] = function (el) {
    shell(el, 'chequing-cost', {
      title: 'Chequing account cost calculator',
      intro: 'Your yearly cost or earnings at each account, based on your balance and monthly fee waivers.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'bal', 'Typical lowest monthly balance', 2000, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var b = a.n('bal');
        var rows = D.chequing.map(function (c) { var fee = (c.waive_bal != null && b >= c.waive_bal) ? 0 : c.fee; var i = b * (c.rate || 0); return { c: c, fee: fee * 12, i: i, net: i - fee * 12 }; }).sort(function (x, y) { return y.net - x.net; });
        return head('Best yearly result at your balance', money(rows[0].net) + ' at ' + rows[0].c.name) + table(['Account', 'Monthly fee', 'Fees a year', 'Interest a year', 'Net a year'], rows.map(function (r) { return [r.c.link ? '<a href="' + r.c.link + '">' + r.c.name + '</a>' : r.c.name, r.c.fee_text, money(r.fee), money(r.i), '<b>' + money(r.net) + '</b>']; })) +
          how('Fees are waived where your balance meets the published minimum. Interest uses the published rate on the whole balance. Other waivers, such as direct deposit or bundles, are listed in each account\'s details.');
      },
      next: [['/banking/best-chequing-accounts/', 'Best chequing accounts'], ['/banking/best-no-fee-chequing-accounts/', 'No-fee chequing']]
    });
  };

  /* ---------- Crypto fees ---------- */
  W['crypto-fee'] = function (el) {
    shell(el, 'crypto-fee', {
      title: 'Crypto trading fee calculator',
      intro: 'The published fee on one trade at each authorized platform.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Trade size (CAD)', 1000, { min: 0 }) + fNum(p, 'n', 'Trades per year', 12, { min: 1, step: 1 }) + '</div>'; },
      calc: function (a) {
        var amt = a.n('amt'), n = a.n('n');
        var rows = D.crypto.filter(function (c) { return c.fee_pct != null; }).map(function (c) { return { c: c, f: amt * c.fee_pct }; }).sort(function (x, y) { return x.f - y.f; });
        return head('Lowest published fee per trade', money2(rows[0].f) + ' at ' + rows[0].c.name) + table(['Platform', 'Published fee', 'Per trade', 'Per year'], rows.map(function (r) { return [r.c.link ? '<a href="' + r.c.link + '">' + r.c.name + '</a>' : r.c.name, r.c.fee_text, money2(r.f), money2(r.f * n)]; })) +
          '<p class="ws-note">Not shown because no single fee is published: ' + D.crypto.filter(function (c) { return c.fee_pct == null; }).map(function (c) { return (c.link ? '<a href="' + c.link + '">' + c.name + '</a>' : c.name) + ' (' + c.fee_text + ')'; }).join('; ') + '.</p>' +
          how('Uses each platform\'s published trading fee or spread for a standard market order. Some platforms build a spread into the price on top of, or instead of, a fee, which changes with the market. Deposit and withdrawal fees are extra where they apply.');
      },
      next: [['/compare/best-crypto-platforms/', 'Best crypto platforms'], ['/reviews/wealthsimple/crypto/', 'Wealthsimple Crypto review']]
    });
  };

  /* ---------- Wealthsimple tier ---------- */
  W['ws-tier'] = function (el) {
    var T = D.ws_tiers;
    shell(el, 'ws-tier', {
      title: 'Wealthsimple tier finder',
      intro: 'Enter the assets you hold or plan to move to Wealthsimple to see your tier and what changes at each level.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'assets', 'Total assets at Wealthsimple', 25000, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var x = a.n('assets'), t = T.list[0];
        T.list.forEach(function (z) { if (x >= z.from) t = z; });
        var nx = T.list.filter(function (z) { return z.from > x; })[0];
        var h = head('Your tier', t.name) + '<ul>' + t.perks.map(function (q) { return '<li>' + q + '</li>'; }).join('') + '</ul>';
        if (nx) h += msg('ok', money(nx.from - x) + ' more in assets reaches ' + nx.name + '.');
        h += table(['Feature'].concat(T.list.map(function (z) { return z.name; })), T.rows);
        h += how('Tier is set by the total of eligible assets across your Wealthsimple accounts' + (T.household ? ', and household members\' combined assets can count' : '') + '. WealthScale is independent and not affiliated with Wealthsimple.');
        return h;
      },
      next: [['/reviews/wealthsimple/membership-tiers/', 'Core vs Premium vs Generation'], ['/reviews/wealthsimple/fees/', 'Every Wealthsimple fee']]
    });
  };

  /* ---------- Benefit payment dates ---------- */
  W['benefit-dates'] = function (el) {
    var which = el.getAttribute('data-benefit') || 'all';
    var B = D.benefits;
    var keys = which === 'all' ? Object.keys(B).filter(function (k) { return B[k].dates && B[k].dates.length; }) : [which];
    shell(el, 'benefit-dates', {
      title: which === 'all' ? 'Next government payment dates' : 'Next ' + B[which].name + ' payment',
      intro: 'Today is ' + NOW.toLocaleDateString('en-CA', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }) + '.',
      button: false,
      fields: function (p) { return keys.length > 1 ? fSel(p, 'b', 'Benefit', keys.map(function (k) { return [k, B[k].name]; }), keys[0]) : ''; },
      calc: function (a) {
        var k = keys.length > 1 ? a.val('b') : keys[0], b = B[k];
        if (!b.dates || !b.dates.length) return msg('warnmsg', 'Payment dates being confirmed.') + (b.note ? '<p class="ws-note">' + b.note + '</p>' : '');
        var next = b.dates.filter(function (d) { return daysUntil(d) >= 0; });
        var h = next.length ? head('Next ' + b.name + ' payment', fmtDate(next[0], { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' })) +
          '<p class="ws-countdown">' + (daysUntil(next[0]) === 0 ? 'Today' : daysUntil(next[0]) + ' day' + (daysUntil(next[0]) === 1 ? '' : 's') + ' to go') + '</p>' : msg('warnmsg', 'The next dates have not been published yet.');
        h += table(['Payment', 'Date', 'Status'], b.dates.map(function (d) { var n = daysUntil(d); return [fmtDate(d, { month: 'long', year: 'numeric' }), fmtDate(d, { weekday: 'short', month: 'long', day: 'numeric', year: 'numeric' }), n < 0 ? 'Paid' : (n === 0 ? 'Today' : 'Upcoming')]; }), b.name + ' payment dates');
        if (b.note) h += '<p class="ws-note">' + b.note + '</p>';
        return h;
      },
      next: [['/benefits/', 'All benefit payment dates'], ['/benefits/cpp-oas-payment-dates/', 'CPP and OAS dates'], ['/benefits/gst-hst-credit/', 'GST/HST credit']]
    });
  };

  /* ---------- OAS clawback ---------- */
  W['oas-clawback'] = function (el) {
    var O = D.oas;
    shell(el, 'oas-clawback', {
      title: 'OAS clawback calculator',
      intro: 'The OAS recovery tax takes back 15% of net income above the threshold, up to the full pension.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'inc', 'Net income for ' + O.income_year + ' (line 23400)', 100000, { min: 0 }) + fRadio(p, 'age', 'Age', [['65', '65 to 74'], ['75', '75 and over']], '65') + '</div>'; },
      calc: function (a) {
        var inc = a.n('inc'), full = (a.val('age') === '75' ? O.max75 : O.max65) * 12;
        var cb = Math.min(full, Math.max(0, inc - O.threshold) * O.rate);
        return head('Estimated yearly OAS repayment', money(cb)) + kv([['Threshold (' + O.income_year + ' income)', money(O.threshold)], ['Yearly OAS at current rates', money(full)], ['OAS you keep', money(full - cb)], ['Income where OAS is fully clawed back', money(O.threshold + full / O.rate)]]) +
          how('Repayment = 15% of net income over the threshold, capped at the OAS you receive. It is collected by reducing monthly payments from July to June of the following year. Uses current quarterly OAS rates, which are indexed each quarter.');
      },
      next: [['/benefits/cpp-oas-payment-dates/', 'CPP and OAS payment dates'], ['/vs/tfsa-vs-rrsp/', 'TFSA withdrawals do not count']]
    });
  };

  /* ---------- CPP start age ---------- */
  W['cpp-start-age'] = function (el) {
    var P = D.cpp;
    shell(el, 'cpp-start-age', {
      title: 'CPP and OAS start age calculator',
      intro: 'How your monthly CPP and OAS change if you start earlier or later than 65.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'cpp', 'Your CPP at 65 (monthly)', P.avg65 || 900, { min: 0, help: 'From your My Service Canada Account statement. The ' + CUR + ' maximum at 65 is ' + money2(P.max65) + '.' }) + fNum(p, 'oas', 'OAS at 65 (monthly)', D.oas.max65, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var c = a.n('cpp'), o = a.n('oas'), rows = [];
        for (var age = 60; age <= 70; age++) {
          var cf = age < 65 ? 1 - P.early * 12 * (65 - age) : 1 + P.late * 12 * (age - 65);
          var of = age < 65 ? null : 1 + D.oas.defer * 12 * (age - 65);
          rows.push([age, pct(cf - 1, 1), money2(c * cf), of ? money2(o * of) : 'Not available', of ? money2(c * cf + o * of) : money2(c * cf)]);
        }
        return head('CPP at 70 vs 60', money2(c * (1 + P.late * 60)) + ' vs ' + money2(c * (1 - P.early * 60))) + table(['Start age', 'CPP change', 'CPP monthly', 'OAS monthly', 'Total monthly'], rows) +
          how('CPP falls ' + pct(P.early, 1) + ' for each month before 65 (up to ' + pct(P.early * 60, 0) + ' at 60) and rises ' + pct(P.late, 1) + ' for each month after 65 (up to ' + pct(P.late * 60, 0) + ' at 70). OAS starts at 65 at the earliest and rises ' + pct(D.oas.defer, 1) + ' for each month you defer, up to ' + pct(D.oas.defer * 60, 0) + ' at 70. Amounts are in today\'s dollars; both are indexed to inflation.');
      },
      next: [['/benefits/cpp-oas-payment-dates/', 'CPP and OAS payment dates']]
    });
  };

  /* ---------- GST/HST credit ---------- */
  W['gst-credit'] = function (el) {
    var G = D.gst_credit;
    shell(el, 'gst-credit', {
      title: 'GST/HST credit calculator',
      intro: 'Estimate your credit for ' + G.period + ', based on your ' + G.income_year + ' family net income.',
      fields: function (p) { return '<div class="ws-w-grid">' + fRadio(p, 'st', 'Marital status', [['s', 'Single'], ['m', 'Married or common-law']], 's') + fNum(p, 'kids', 'Children under 19', 0, { min: 0, max: 15, step: 1 }) + fNum(p, 'inc', 'Adjusted family net income (' + G.income_year + ')', 30000, { min: 0 }) + fNum(p, 'own', 'Your own net income (singles: same as above)', 30000, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var single = a.val('st') === 's', k = Math.round(a.n('kids')), inc = a.n('inc'), own = single ? inc : a.n('own');
        // A single parent claims the adult amount for one child (eligible dependant) and gets the full single supplement.
        var base = single ? (k > 0 ? 2 * G.adult + (k - 1) * G.child : G.adult) : 2 * G.adult + k * G.child;
        var supp = 0;
        if (single && k === 0) supp = Math.min(G.single_supp, Math.max(0, (own - G.supp_base) * G.supp_rate));
        if (single && k > 0) supp = G.single_supp;
        var full = base + supp, red = Math.max(0, inc - G.threshold) * G.reduce, credit = Math.max(0, full - red);
        var h = head('Estimated yearly credit', money2(credit)) + kv([['Each quarterly payment', money2(credit / 4)], ['Maximum before income reduction', money2(full)], ['Income reduction', money2(Math.min(full, red))]]);
        if (G.note) h += msg('ok', G.note);
        h += how('Base amounts for ' + G.period + ': ' + money(G.adult) + ' for you, ' + money(G.adult) + ' for a spouse or partner (or for one child of a single parent), ' + money(G.child) + ' per other child, plus a single supplement of up to ' + money(G.single_supp) + '. The total is reduced by ' + pct(G.reduce, 0) + ' of adjusted family net income over ' + money(G.threshold) + '. Credits under $50 a quarter are paid in one July payment.');
        return h;
      },
      next: [['/benefits/gst-hst-credit/', 'GST/HST credit dates and amounts'], ['/benefits/', 'All benefit dates']]
    });
  };

  /* ---------- RRSP withdrawal ---------- */
  W['rrsp-withdrawal'] = function (el) {
    shell(el, 'rrsp-withdrawal', {
      title: 'RRSP withdrawal tax calculator',
      intro: 'Tax withheld at source on an RRSP withdrawal, and the tax you may owe when you file.',
      fields: function (p) { return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'amt', 'Withdrawal amount', 10000, { min: 0 }) + fNum(p, 'inc', 'Other taxable income this year', MEM.get('income', 60000), { min: 0 }) + '</div>'; },
      calc: function (a) {
        var prov = a.val('prov'), amt = a.n('amt'), W8 = D.rrsp.withholding, br = prov === 'QC' ? W8.QC : W8.other, rate = br[br.length - 1][1];
        for (var i = 0; i < br.length; i++) if (br[i][0] == null || amt <= br[i][0]) { rate = br[i][1]; break; }
        if (prov === 'QC' && W8.QC_prov) rate += W8.QC_prov;
        var wh = amt * rate, tax = C.tax(prov, a.n('inc') + amt).total - C.tax(prov, a.n('inc')).total;
        return head('Withheld at source', money(wh)) + kv([['Withholding rate', pct(rate, 0)], ['Estimated tax on the withdrawal', money(tax)], [tax > wh ? 'More owed at tax time' : 'Possible refund at tax time', money(Math.abs(tax - wh))], ['RRSP room', 'Not restored']]) +
          how('Withholding depends only on the size of each withdrawal' + (prov === 'QC' ? ' (Quebec: federal 5%, 10% or 15% plus ' + pct(W8.QC_prov || 0, 0) + ' Quebec tax)' : '') + '. The withdrawal is added to your income, so your final tax is based on your marginal rate. Withdrawals under the Home Buyers\' Plan and Lifelong Learning Plan have no withholding.');
      },
      next: [['/accounts/rrsp/', 'RRSP guide'], ['/accounts/home-buyers-plan/', 'Home Buyers\' Plan']]
    });
  };

  /* ---------- Tax software picker ---------- */
  W['tax-software-picker'] = function (el) {
    shell(el, 'tax-software-picker', {
      title: 'Which tax software fits your return?',
      intro: 'Tick what applies. We show the lowest tier of each NETFILE-certified product that covers your situation, and flag anything the company does not confirm.',
      button: 'Show matches',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fRadio(p, 'self', 'Self-employment or business income?', [['n', 'No'], ['y', 'Yes']], 'n') + fRadio(p, 'rent', 'Rental income?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fRadio(p, 'inv', 'Investments with capital gains?', [['n', 'No'], ['y', 'Yes']], 'n') + fRadio(p, 'qc', 'Filing a Quebec return?', [['n', 'No'], ['y', 'Yes']], 'n') + fRadio(p, 'help', 'Want an expert to review or file?', [['n', 'No'], ['y', 'Yes']], 'n') + '</div>';
      },
      calc: function (a) {
        var need = ['self', 'rent', 'inv', 'qc', 'help'].filter(function (k) { return a.val(k) === 'y'; });
        var rows = [];
        D.tax_software.forEach(function (s) {
          var pick = null, unsure = false;
          for (var i = 0; i < s.tiers.length && !pick; i++) {
            var t = s.tiers[i], vals = need.map(function (k) { return t[k]; });
            if (vals.every(function (x) { return x === true; })) pick = t;
          }
          if (!pick) for (var j = 0; j < s.tiers.length && !pick; j++) {
            var t2 = s.tiers[j], v2 = need.map(function (k) { return t2[k]; });
            if (v2.every(function (x) { return x !== false; })) { pick = t2; unsure = true; }
          }
          rows.push([s.link ? '<a href="' + s.link + '">' + s.name + '</a>' : s.name, pick ? pick.name : 'No tier covers this', pick ? pick.price_text : '\u2014', pick ? (unsure ? 'Not confirmed by the company' : 'Yes') : 'No']);
        });
        var good = rows.filter(function (r) { return r[3] === 'Yes'; }).length;
        return head('Products confirmed for your situation', String(good)) + table(['Software', 'Lowest tier that fits', 'Price', 'Confirmed?'], rows) +
          how('Every product listed is NETFILE-certified for the ' + D.tax_software_year + ' tax year. "Not confirmed" means the company does not state on its pricing pages whether that tier handles your situation, so please check before you pay.');
      },
      next: [['/compare/best-tax-software/', 'Best tax software'], ['/reviews/wealthsimple/tax/', 'Wealthsimple Tax review']]
    });
  };

  /* ---------- Broker match (filter by needs) ---------- */
  W['broker-match'] = function (el) {
    shell(el, 'broker-match', {
      title: 'Find brokers that match your needs',
      intro: 'Tick the features you need. We list every broker that has them, ranked by our published score.',
      button: 'Show matches',
      fields: function (p) {
        var feats = D.broker_features;
        return '<div class="ws-radio">' + feats.map(function (f) { return '<label><input type="checkbox" name="' + f[0] + '" value="1"> ' + f[1] + '</label>'; }).join('') + '</div>';
      },
      calc: function (a) {
        var want = D.broker_features.filter(function (f) { var n = a.form.querySelector('[name="' + f[0] + '"]'); return n && n.checked; }).map(function (f) { return f[0]; });
        var rows = D.brokers.filter(function (b) { return want.every(function (w) { return b.flags && b.flags.indexOf(w) >= 0; }); }).sort(function (x, y) { return (y.score || 0) - (x.score || 0); });
        if (!rows.length) return msg('warnmsg', 'No broker we cover has every feature you ticked. Try removing one.');
        return head('Brokers that match', String(rows.length)) + table(['Rank', 'Broker', 'Our score', 'Canadian trades', 'US trades'], rows.map(function (b, i) { return [i + 1, '<a href="' + b.review + '">' + b.name + '</a>', (b.score || 0).toFixed(1) + ' / 5', b.cad_text, b.us_text]; })) +
          how('Matches use the features each broker publishes. Ranking uses the overall score from our broker methodology, which is never changed by partnerships.');
      },
      next: [['/compare/best-online-brokers/', 'Best online brokers'], ['/methodology/brokers/', 'How we rate brokers']]
    });
  };

  /* ---------- Transfer fee ---------- */
  W['transfer-fee'] = function (el) {
    shell(el, 'transfer-fee', {
      title: 'Account transfer fee calculator',
      intro: 'What it costs to move accounts out of your current institution, and which receiving brokers cover the fee.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'n', 'Number of accounts to move', 2, { min: 1, max: 10, step: 1 }) + fNum(p, 'fee', 'Transfer-out fee per account at your current institution', 150, { min: 0, help: 'Many banks and brokers charge a fee per account; check your fee schedule.' }) + fNum(p, 'val', 'Value per account', 30000, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var n = a.n('n'), fee = a.n('fee'), v = a.n('val'), cost = n * fee;
        var rows = D.brokers.filter(function (b) { return b.transfer_in_text; }).map(function (b) {
          var known = b.transfer_min != null || (b.transfer_max != null && !b.per_client);
          var ok = b.transfer_min == null ? known : v * n >= b.transfer_min;
          var cov = 0;
          if (ok) cov = b.per_client ? Math.min(cost, b.transfer_max == null ? cost : b.transfer_max) : n * Math.min(fee, b.transfer_max == null ? fee : b.transfer_max);
          return ['<a href="' + b.review + '">' + b.name + '</a>', b.transfer_in_text, known ? money(cov) : 'Depends on eligibility', known ? money(cost - cov) : '\u2014']; });
        return head('Transfer-out fees you would pay', money(cost)) + table(['Receiving broker', 'Published transfer fee policy', 'Covered for you', 'Left to pay'], rows) + how('Coverage depends on each broker\'s published minimum and cap, and usually requires a request with your statement showing the fee. Transfers between registered accounts must be done institution to institution to keep them tax-free.');
      },
      next: [['/learn/transfer-investment-account/', 'How to transfer an account']]
    });
  };

  /* ---------- Generic countdown ---------- */
  W['countdown'] = function (el) {
    var d = el.getAttribute('data-date'), lab = el.getAttribute('data-label') || 'Deadline';
    el.classList.add('ws-widget');
    var n = daysUntil(d);
    el.innerHTML = '<div class="ws-w-head"><div class="ws-w-title" role="heading" aria-level="3">' + esc(lab) + '</div><p>' + fmtDate(d, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }) + '</p></div><div class="ws-w-body"><p class="ws-countdown">' + (n > 0 ? n + ' day' + (n === 1 ? '' : 's') + ' left' : (n === 0 ? 'Today' : 'Passed')) + '</p></div>';
  };

  /* ---------- Table filter (progressive enhancement on a static table) ---------- */
  W['table-filter'] = function (el) {
    var tbl = el.querySelector('table'); if (!tbl) return;
    var box = document.createElement('div'); box.className = 'ws-filter';
    box.innerHTML = '<label class="ws-sr" for="wsf' + (++uid) + '">Filter this table</label><input type="search" id="wsf' + uid + '" placeholder="Type to filter, e.g. FHSA, USD, $0">';
    el.insertBefore(box, el.firstChild);
    var inp = box.querySelector('input');
    inp.addEventListener('input', function () {
      var q = inp.value.toLowerCase().trim().split(/\s+/);
      Array.prototype.forEach.call(tbl.tBodies[0].rows, function (r) { var t = r.textContent.toLowerCase(); r.style.display = q.every(function (w) { return t.indexOf(w) >= 0; }) ? '' : 'none'; });
    });
    Array.prototype.forEach.call(tbl.tHead ? tbl.tHead.rows[0].cells : [], function (th, i) {
      th.style.cursor = 'pointer'; th.setAttribute('tabindex', '0'); th.setAttribute('aria-sort', 'none'); th.title = 'Sort by this column';
      function sort() {
        var asc = th.getAttribute('aria-sort') !== 'ascending';
        Array.prototype.forEach.call(tbl.tHead.rows[0].cells, function (o) { o.setAttribute('aria-sort', 'none'); });
        th.setAttribute('aria-sort', asc ? 'ascending' : 'descending');
        var rows = Array.prototype.slice.call(tbl.tBodies[0].rows);
        rows.sort(function (a, b) {
          var x = a.cells[i].textContent.trim(), y = b.cells[i].textContent.trim();
          var nx = parseFloat(x.replace(/[^0-9.\-]/g, '')), ny = parseFloat(y.replace(/[^0-9.\-]/g, ''));
          var c = (isFinite(nx) && isFinite(ny)) ? nx - ny : x.localeCompare(y);
          return asc ? c : -c;
        });
        rows.forEach(function (r) { tbl.tBodies[0].appendChild(r); });
      }
      th.addEventListener('click', sort);
      th.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sort(); } });
    });
  };

  /* =====================================================================
   * 4b. WIDGETS ADDED FOR PAGES 102 TO 201 (October 23, 2026)
   * ===================================================================== */
  var OPT_PERIODS = [['52', 'Weekly (52 a year)'], ['26', 'Every two weeks (26 a year)'], ['24', 'Twice a month (24 a year)'], ['12', 'Monthly (12 a year)']];
  function perLabel(n) { return { 52: 'week', 26: 'two weeks', 24: 'half month', 12: 'month' }[n] || 'pay'; }
  function mbNote(prov) { return ''; }

  /* ---------- bracket slices (land transfer tax and similar) ---------- */
  C.slices = function (br, amt) {
    var lo = 0, rows = [], tot = 0;
    for (var i = 0; i < br.length; i++) {
      var hi = br[i][0] == null ? Infinity : br[i][0], r = br[i][1];
      if (amt > lo) { var part = Math.min(amt, hi) - lo, t = part * r; rows.push([lo, hi, r, part, t]); tot += t; }
      lo = hi;
      if (amt <= hi) break;
    }
    return { rows: rows, total: tot };
  };

  /* ---------- payroll engine ---------- */
  C.payroll = function (prov, salary, rrsp) {
    var Pp = D.payroll; if (!Pp) return null;
    rrsp = rrsp || 0;
    var qc = prov === 'QC', pen = qc ? Pp.qpp : Pp.cpp, rate = pen.base_rate + pen.first_add_rate;
    var c1 = Math.max(0, Math.min(salary, pen.ympe) - pen.exemption) * rate;
    var c2 = Math.max(0, Math.min(salary, pen.yampe) - pen.ympe) * pen.rate2;
    var ei = Math.min(salary, Pp.ei.mie) * (qc ? Pp.ei.rate_qc : Pp.ei.rate);
    var qpip = qc ? Math.min(salary, Pp.qpip.mie) * Pp.qpip.rate : 0;
    var base = c1 * pen.base_rate / rate, enh = c1 - base + c2;
    var taxable = Math.max(0, salary - rrsp - enh);
    var cf = base + ei + qpip + Math.min(Pp.cea, salary);
    var cp = (Pp.k2p && Pp.k2p[prov] === 'lowest') ? base + ei + qpip : 0;
    if (prov === 'YT') cp += Math.min(Pp.cea, salary);
    var pd = qc && Pp.qc_workers ? Math.min(Pp.qc_workers.rate * salary, Pp.qc_workers.max) : 0;
    var t = C.tax(prov, taxable, { cf: cf, cp: cp, pd: pd });
    var ded = c1 + c2 + ei + qpip + t.total;
    return { cpp: c1, cpp2: c2, ei: ei, qpip: qpip, enhanced: enh, taxable: taxable, tax: t, deductions: ded, net: salary - rrsp - ded };
  };

  /* ---------- Take-home pay ---------- */
  W['take-home-pay'] = function (el) {
    shell(el, 'take-home-pay', {
      title: 'Take-home pay calculator ' + CUR,
      intro: 'Your pay after income tax, CPP, CPP2 and EI (QPP and QPIP in Quebec), per year and per pay.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory where you work', provOpts(), provDefault()) +
          fNum(p, 'sal', 'Yearly salary or wages before deductions', MEM.get('income', 75000), { min: 0 }) +
          fSel(p, 'n', 'How often you are paid', OPT_PERIODS, '26') +
          fNum(p, 'rrsp', 'RRSP contributions deducted from your pay (per year)', 0, { min: 0, help: 'Group RRSP or payroll RRSP deductions lower the tax taken off each pay.' }) + '</div>';
      },
      calc: function (a) {
        if (!D.payroll) return msg('warnmsg', 'Payroll figures for ' + CUR + ' are being confirmed. Please try again soon.');
        var prov = a.val('prov'), sal = a.n('sal'), n = +a.val('n') || 26, r = C.payroll(prov, sal, a.n('rrsp')), qc = prov === 'QC';
        MEM.set('prov', prov); MEM.set('income', sal);
        var rows = [['Gross pay', money2(sal), money2(sal / n)]];
        if (a.n('rrsp') > 0) rows.push(['RRSP deducted at source', money2(-a.n('rrsp')), money2(-a.n('rrsp') / n)]);
        rows.push(['Federal income tax', money2(-r.tax.federal), money2(-r.tax.federal / n)]);
        rows.push([D.provName[prov] + ' income tax' + (r.tax.premium ? ' and Health Premium' : ''), money2(-(r.tax.provincial + r.tax.premium)), money2(-(r.tax.provincial + r.tax.premium) / n)]);
        rows.push([(qc ? 'QPP' : 'CPP') + ' contributions', money2(-r.cpp), money2(-r.cpp / n)]);
        if (r.cpp2) rows.push([(qc ? 'QPP2' : 'CPP2') + ' contributions', money2(-r.cpp2), money2(-r.cpp2 / n)]);
        rows.push(['EI premiums', money2(-r.ei), money2(-r.ei / n)]);
        if (qc) rows.push(['QPIP premiums', money2(-r.qpip), money2(-r.qpip / n)]);
        rows.push(['<b>Take-home pay</b>', '<b>' + money2(r.net) + '</b>', '<b>' + money2(r.net / n) + '</b>']);
        var P = D.payroll, pen = qc ? P.qpp : P.cpp;
        return head('Take-home pay per ' + perLabel(n), money2(r.net / n)) +
          kv([['Take-home pay per year', money2(r.net)], ['Total deductions', money2(r.deductions)], ['Share of pay deducted', pct(sal ? (r.deductions) / sal : 0, 1)], ['Marginal tax rate', pct(C.marginal(prov, r.taxable), 2)]]) +
          table(['', 'Per year', 'Per pay'], rows, 'Your ' + CUR + ' pay, step by step') + mbNote(prov) +
          how((qc ? 'QPP' : 'CPP') + ': ' + pct(pen.base_rate + pen.first_add_rate, 2) + ' of earnings between ' + money(pen.exemption) + ' and ' + money(pen.ympe) + ' (maximum ' + money2(pen.max1) + '), plus ' + pct(pen.rate2, 0) + ' between ' + money(pen.ympe) + ' and ' + money(pen.yampe) + ' (maximum ' + money2(pen.max2) + '). EI: ' + pct(qc ? P.ei.rate_qc : P.ei.rate, 2) + ' of insurable earnings up to ' + money(P.ei.mie) + ' (maximum ' + money2(qc ? P.ei.max_qc : P.ei.max) + ').' + (qc ? ' QPIP: ' + pct(P.qpip.rate, 3) + ' up to ' + money(P.qpip.mie) + '.' : '') + ' Income tax uses ' + CUR + ' federal and ' + D.provName[prov] + ' brackets with the basic personal amount, the Canada employment amount, the federal credit for base contributions and EI, and the deduction for enhanced and second contributions. It assumes one employer and no other income, credits or deductions, so the tax your employer withholds can differ a little.');
      },
      next: [['/calculators/income-tax-calculator/', 'Income tax calculator'], ['/tax/cpp-ei-contributions/', 'CPP and EI contributions ' + CUR]]
    });
  };

  /* ---------- Superficial loss checker ---------- */
  W['superficial-loss'] = function (el) {
    var S = D.superficial || { days: 30 };
    shell(el, 'superficial-loss', {
      title: 'Superficial loss checker',
      intro: 'Check whether a capital loss is denied because you, your spouse or another affiliated person bought the same investment within ' + S.days + ' days before or after the sale.',
      fields: function (p) {
        var t = todayIso();
        return '<div class="ws-w-grid">' + fDate(p, 'sale', 'Date you sold at a loss', t) + fNum(p, 'qty', 'Number of shares or units sold', 100, { min: 0 }) +
          fNum(p, 'loss', 'Capital loss on the sale', 2000, { min: 0 }) +
          fDate(p, 'd1', 'Date of a purchase of the same investment (by you or an affiliated person)', isoAdd(t, 10), { help: 'Leave blank if none.' }) + fNum(p, 'q1', 'Shares or units bought that day', 100, { min: 0 }) +
          fDate(p, 'd2', 'Date of another purchase (optional)', '') + fNum(p, 'q2', 'Shares or units bought that day', 0, { min: 0 }) +
          fNum(p, 'held', 'Shares or units still held ' + S.days + ' days after the sale (by you or an affiliated person)', 100, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var sale = a.val('sale'); if (!sale) return msg('warnmsg', 'Please enter the sale date.');
        var start = isoAdd(sale, -S.days), end = isoAdd(sale, S.days), bought = 0;
        [['d1', 'q1'], ['d2', 'q2']].forEach(function (x) { var d = a.val(x[0]); if (d && d >= start && d <= end) bought += a.n(x[1]); });
        var held = a.n('held'), qty = a.n('qty'), loss = a.n('loss'), sup = bought > 0 && held > 0;
        var h = head('Is it a superficial loss?', sup ? 'Yes' : 'No', sup) + kv([['Window starts', fmtDate(start)], ['Sale date', fmtDate(sale)], ['Window ends', fmtDate(end)], ['Bought in the window', nf(bought)], ['Still held at the end', nf(held)]]);
        if (sup) {
          var full = Math.min(qty, bought, held) >= qty;
          if (S.partial) {
            var denied = qty > 0 ? loss * Math.min(qty, bought, held) / qty : 0;
            h += kv([['Loss denied', money2(denied)], ['Loss you can claim', money2(loss - denied)]]);
          } else if (full) {
            h += kv([['Loss denied', money2(loss)], ['Loss you can claim', '$0']]);
          } else {
            h += msg('warnmsg', 'You bought back fewer shares than you sold, so only part of the loss may be denied.');
          }
          h += msg('ok', 'A denied loss can usually be added to the adjusted cost base of the shares you bought, so you get the benefit when you sell those later.');
        } else {
          h += msg('ok', bought === 0 ? 'No purchase of the same investment falls inside the ' + (S.days * 2 + 1) + '-day window, so the superficial loss rule does not deny this loss.' : 'Nothing was still held at the end of the window, so the rule does not deny this loss.');
        }
        return h + how('The window runs from ' + S.days + ' calendar days before the sale to ' + S.days + ' calendar days after it. The loss is denied when you or an affiliated person (including your spouse or common-law partner) buys identical property in that window and still holds it at the end. General information only.');
      },
      next: [['/tax/superficial-loss-rule/', 'Superficial loss rule'], ['/tax/capital-losses/', 'Capital losses']]
    });
  };

  /* ---------- Spousal RRSP attribution ---------- */
  W['spousal-attribution'] = function (el) {
    shell(el, 'spousal-attribution', {
      title: 'Spousal RRSP withdrawal calculator',
      intro: 'How much of a spousal RRSP withdrawal is taxed to the contributor, and the tax each spouse pays.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'yr', 'Year of the withdrawal', CUR, { min: 2000, max: CUR + 10, step: 1 }) +
          fNum(p, 'w', 'Amount withdrawn', 10000, { min: 0 }) +
          fNum(p, 'c0', 'Contributions to spousal RRSPs in the withdrawal year', 0, { min: 0 }) +
          fNum(p, 'c1', 'Contributions in the year before', 5000, { min: 0 }) +
          fNum(p, 'c2', 'Contributions two years before', 0, { min: 0 }) +
          fNum(p, 'ic', 'Contributor\'s other taxable income', 100000, { min: 0 }) +
          fNum(p, 'ia', 'Account holder\'s (annuitant\'s) other taxable income', 30000, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), yr = a.n('yr'), wd = a.n('w'), c = a.n('c0') + a.n('c1') + a.n('c2');
        var lesser = D.spousal && D.spousal.lesser;
        var attr = c > 0 ? (lesser ? Math.min(wd, c) : wd) : 0, own = wd - attr;
        var tc = C.tax(prov, a.n('ic') + attr).total - C.tax(prov, a.n('ic')).total;
        var ta = C.tax(prov, a.n('ia') + own).total - C.tax(prov, a.n('ia')).total;
        var tnone = C.tax(prov, a.n('ia') + wd).total - C.tax(prov, a.n('ia')).total;
        var last = a.n('c0') > 0 ? yr : (a.n('c1') > 0 ? yr - 1 : (a.n('c2') > 0 ? yr - 2 : null));
        var h = head('Taxed to the contributor', money(attr)) + kv([['Taxed to the account holder', money(own)], ['Extra tax for the contributor', money(tc)], ['Extra tax for the account holder', money(ta)], ['Total tax on the withdrawal', money(tc + ta)]]);
        if (attr > 0) h += msg('warnmsg', 'If no contributions are made after ' + last + ', a withdrawal from January 1, ' + (last + 3) + ' is taxed to the account holder: ' + money(tnone) + ' of tax at today\'s incomes, saving ' + money(tc + ta - tnone) + ' compared with now.');
        else h += msg('ok', 'No spousal RRSP contributions in the withdrawal year or the two years before, so the withdrawal is taxed to the account holder.');
        return h + mbNote(prov) + how((lesser ? 'The contributor includes the lesser of the withdrawal and the contributions made to any spousal RRSP in the withdrawal year and the two years before.' : 'If the contributor made spousal RRSP contributions in the withdrawal year or either of the two years before, the contributor generally includes the withdrawal in income.') + ' Exceptions exist (for example on separation or death), and Form T2205 is used to work out the amounts. Tax figures use ' + CUR + ' rates and are estimates.');
      },
      next: [['/accounts/spousal-rrsp/', 'Spousal RRSP guide'], ['/calculators/rrsp-withdrawal-calculator/', 'RRSP withdrawal calculator']]
    });
  };

  /* ---------- Pension income splitting ---------- */
  W['pension-split'] = function (el) {
    var O = D.oas, FC = D.fedcred || { age: 0, age_thr: 0, age_rate: 0, pension: 0 }, mx = D.pension ? D.pension.split_max : 0.5;
    shell(el, 'pension-split', {
      title: 'Pension income splitting calculator',
      intro: 'Find the share of eligible pension income to move to your spouse or partner (up to ' + pct(mx, 0) + ') that gives the lowest combined tax and OAS clawback.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fNum(p, 'pa', 'Spouse A: eligible pension income (for example RRIF payments at 65 or older)', 60000, { min: 0 }) +
          fNum(p, 'oa', 'Spouse A: other taxable income (CPP and other income, not OAS)', 15000, { min: 0 }) +
          fNum(p, 'xa', 'Spouse A: yearly OAS received', Math.round(O.max65 * 12), { min: 0 }) +
          fRadio(p, 'aa', 'Spouse A 65 or older at year-end?', [['y', 'Yes'], ['n', 'No']], 'y') +
          fNum(p, 'ob', 'Spouse B: other taxable income (not OAS, not pension income)', 6000, { min: 0 }) +
          fNum(p, 'pb', 'Spouse B: own eligible pension income', 0, { min: 0 }) +
          fNum(p, 'xb', 'Spouse B: yearly OAS received', Math.round(O.max65 * 12), { min: 0 }) +
          fRadio(p, 'ab', 'Spouse B 65 or older at year-end?', [['y', 'Yes'], ['n', 'No']], 'y') + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), pa = a.n('pa'), oa = a.n('oa'), ob = a.n('ob'), pb = a.n('pb'), xa = a.n('xa'), xb = a.n('xb'), a65 = a.val('aa') === 'y', b65 = a.val('ab') === 'y';
        function person(other, pens, oas, is65) {
          var net = other + pens + oas, claw = Math.min(oas, Math.max(0, net - O.threshold) * O.rate), ti = net - claw, cf = 0;
          if (is65) { cf += Math.min(FC.pension, pens) + Math.max(0, FC.age - FC.age_rate * Math.max(0, ti - FC.age_thr)); }
          var t = C.tax(prov, ti, { cf: cf }).total;
          return { tax: t, claw: claw, cost: t + claw };
        }
        function cost(f) {
          var s = pa * f, A = person(oa, pa - s, xa, a65), Bq = person(ob, pb + s, xb, b65);
          if (!b65) { var nb = ob + pb + s + xb, cl = Math.min(xb, Math.max(0, nb - O.threshold) * O.rate), tb = C.tax(prov, nb - cl).total; Bq = { tax: tb, claw: cl, cost: tb + cl }; }
          return { f: f, s: s, A: A, B: Bq, total: A.cost + Bq.cost };
        }
        if (!a65) return msg('warnmsg', 'RRIF and LIF payments can be split only when the spouse receiving them is 65 or older at year-end (or receives them because of a spouse\'s death). Registered pension plan annuities can be split at any age.');
        var base = cost(0), best = base, rows = [];
        for (var i = 0; i <= mx * 100 + 0.001; i++) { var c = cost(i / 100); if (c.total < best.total - 0.005) best = c; }
        [0, 0.1, 0.2, 0.3, 0.4, 0.5].concat([best.f]).filter(function (x, i, arr) { return x <= mx && arr.indexOf(x) === i; }).sort(function (x, y) { return x - y; }).forEach(function (f) {
          var c = cost(f); rows.push([pct(f, 0) + (f === best.f ? ' (best)' : ''), money(c.s), money(c.A.cost), money(c.B.cost), money(c.total)]);
        });
        return head('Best amount to split', money(best.s) + ' (' + pct(best.f, 0) + ')') + kv([['Combined tax and clawback, no split', money(base.total)], ['With the best split', money(best.total)], ['Yearly saving', money(base.total - best.total)]]) +
          table(['Share split', 'Amount moved', 'Spouse A tax and clawback', 'Spouse B tax and clawback', 'Combined'], rows, 'Household cost at each split') +
          (prov === 'QC' ? msg('warnmsg', 'Quebec has its own rules for splitting on the Quebec return, so the Quebec part of this estimate may differ.') : '') +
          how('Up to ' + pct(mx, 0) + ' of eligible pension income can be allocated to a spouse or common-law partner on a joint election (Form T1032), filed with both returns. RRIF and LIF payments qualify when the transferring spouse is 65 or older at year-end. The estimate includes the OAS recovery tax (' + pct(O.rate, 0) + ' of net income above ' + money(O.threshold) + ', deducted from income), the federal pension income amount (up to ' + money(FC.pension) + ') and the federal age amount (' + money(FC.age) + ', reduced by ' + pct(FC.age_rate, 0) + ' of net income above ' + money(FC.age_thr) + ') for each spouse 65 or older. Provincial age and pension credits are not included, so the real saving can be a little different.');
      },
      next: [['/tax/pension-income-splitting/', 'Pension income splitting'], ['/benefits/oas-clawback/', 'OAS clawback ' + CUR]]
    });
  };

  /* ---------- Net worth ---------- */
  W['net-worth'] = function (el) {
    var A = [['cash', 'Cash, chequing and savings', 10000], ['tfsa', 'TFSA', 25000], ['rrsp', 'RRSP, RRIF, LIRA or pension value', 60000], ['fhsa', 'FHSA', 0], ['resp', 'RESP', 0],
             ['nonreg', 'Non-registered investments', 0], ['home', 'Home (market value)', 0], ['prop', 'Other real estate', 0], ['car', 'Vehicles', 15000], ['other', 'Other assets', 0]];
    var L = [['mort', 'Mortgage', 0], ['heloc', 'Home equity line of credit', 0], ['carl', 'Car loans or leases', 8000], ['student', 'Student loans', 0], ['cards', 'Credit cards', 2000], ['otherl', 'Other debts', 0]];
    shell(el, 'net-worth', {
      title: 'Net worth calculator',
      intro: 'Add up what you own and what you owe. Your figures stay in your browser.',
      fields: function (p) {
        return '<p class="ws-flabel">What you own</p><div class="ws-w-grid">' + A.map(function (x) { return fNum(p, x[0], x[1], x[2], { min: 0 }); }).join('') + '</div>' +
          '<p class="ws-flabel">What you owe</p><div class="ws-w-grid">' + L.map(function (x) { return fNum(p, x[0], x[1], x[2], { min: 0 }); }).join('') + '</div>';
      },
      calc: function (a) {
        var ta = sum(A.map(function (x) { return a.n(x[0]); })), tl = sum(L.map(function (x) { return a.n(x[0]); })), nw = ta - tl;
        var liquid = a.n('cash') + a.n('tfsa') + a.n('nonreg'), fixed = a.n('home') + a.n('prop') + a.n('car');
        var rows = A.filter(function (x) { return a.n(x[0]) > 0; }).map(function (x) { return [x[1], money(a.n(x[0])), pct(ta ? a.n(x[0]) / ta : 0, 1)]; });
        L.filter(function (x) { return a.n(x[0]) > 0; }).forEach(function (x) { rows.push([x[1], money(-a.n(x[0])), pct(ta ? a.n(x[0]) / ta : 0, 1) + ' of assets']); });
        return head('Your net worth', money(nw), nw < 0) + kv([['Total assets', money(ta)], ['Total debts', money(tl)], ['Debt to assets', ta ? pct(tl / ta, 1) : '—'],
          ['Cash and investments you can reach quickly', money(liquid)], ['Home equity', money(a.n('home') - a.n('mort') - a.n('heloc'))], ['Retirement savings', money(a.n('rrsp'))]]) +
          table(['Item', 'Amount', 'Share'], rows, 'Your net worth by item') +
          how('Net worth is everything you own at today\'s value minus everything you owe. Registered retirement savings are shown at their full value, but withdrawals from an RRSP or RRIF are taxed, so their after-tax value is lower. A vehicle loses value every year, so it counts for less over time than investments do.');
      },
      next: [['/calculators/compound-interest-calculator/', 'Compound interest calculator'], ['/calculators/retirement-calculator/', 'Retirement calculator']]
    });
  };

  /* ---------- Retirement income ---------- */
  W['retirement-income'] = function (el) {
    var O = D.oas, P = D.cpp;
    shell(el, 'retirement-income', {
      title: 'Retirement income calculator',
      intro: 'Yearly retirement income from your savings, CPP and OAS, before tax.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'age', 'Your age now', 45, { min: 18, max: 90, step: 1 }) + fNum(p, 'ret', 'Age you plan to retire', 65, { min: 50, max: 75, step: 1 }) +
          fNum(p, 'bal', 'Retirement savings today (RRSP, TFSA and other)', 150000, { min: 0 }) + fNum(p, 'mon', 'Monthly saving until you retire', 750, { min: 0 }) +
          fNum(p, 'r', 'Yearly return after fees (%)', 5, { min: -10, max: 15, step: 0.1, help: 'Enter a return after inflation to see results in today\'s dollars.' }) +
          fNum(p, 'to', 'Plan for savings to last to age', 95, { min: 70, max: 105, step: 1 }) +
          fNum(p, 'cpp', 'CPP at 65 (monthly, from your statement)', Math.round(P.avg65 || 900), { min: 0, help: 'The ' + CUR + ' maximum at 65 is ' + money2(P.max65) + '.' }) +
          fNum(p, 'cppage', 'Age you start CPP', 65, { min: 60, max: 70, step: 1 }) + fNum(p, 'oasage', 'Age you start OAS', 65, { min: 65, max: 70, step: 1 }) +
          fNum(p, 'yrs', 'Years you will have lived in Canada after 18, by 65', 40, { min: 0, max: 47, step: 1 }) + '</div>';
      },
      calc: function (a) {
        var age = a.n('age'), ret = Math.max(a.n('ret'), age), r = a.n('r') / 100, to = a.n('to');
        var g = C.grow(a.n('bal'), a.n('mon'), r, ret - age, 12), bal = g.bal, N = Math.max(1, to - ret);
        var draw = r === 0 ? bal / N : bal * r / (1 - Math.pow(1 + r, -N));
        var ca = a.n('cppage'), cf = ca < 65 ? 1 - P.early * 12 * (65 - ca) : 1 + P.late * 12 * (ca - 65), cpp = a.n('cpp') * 12 * cf;
        var full = O.full_years || 40, yrs = a.n('yrs'), share = yrs < (O.min_years || 10) ? 0 : Math.min(1, yrs / full);
        var oa = a.n('oasage'), oas = O.max65 * 12 * share * (1 + O.defer * 12 * (oa - 65));
        var ages = [ret, 65, 70, 75, 85].filter(function (x, i, arr) { return x >= ret && x <= to && arr.indexOf(x) === i; }).sort(function (x, y) { return x - y; });
        var rows = ages.map(function (x) {
          var s = x < to ? draw : 0, c = x >= ca ? cpp : 0, o = x >= oa ? oas * (x >= 75 ? 1 + (O.inc75 || 0.1) : 1) : 0;
          return [x, money(s), money(c), money(o), money(s + c + o)];
        });
        var first = rows.length ? rows[rows.length - 1] : null;
        return head('Savings at ' + ret, money(bal)) + kv([['Yearly income from savings to ' + to, money(draw)], ['CPP from ' + ca + ' (yearly)', money(cpp)], ['OAS from ' + oa + ' (yearly)', share ? money(oas) : 'Not eligible (under ' + (O.min_years || 10) + ' years)'], ['Your contributions until retirement', money(g.contrib)]]) +
          table(['Age', 'From savings', 'CPP', 'OAS', 'Total before tax'], rows, 'Yearly retirement income') +
          how('Savings grow at your return with monthly contributions until you retire, then pay a level amount each year until age ' + to + '. CPP changes by ' + pct(P.early, 1) + ' a month before 65 and ' + pct(P.late, 1) + ' a month after. OAS: ' + money2(O.max65) + ' a month at 65 (' + (D.oas.income_year || CUR) + ' figures), ' + pct(O.defer, 1) + ' more for each month you defer, 10% more from 75, and a partial pension of years in Canada after 18 divided by ' + full + '. Income above ' + money(O.threshold) + ' reduces OAS through the clawback, and all of these amounts are taxable.');
      },
      next: [['/calculators/cpp-calculator/', 'CPP calculator'], ['/calculators/oas-calculator/', 'OAS calculator']]
    });
  };

  /* ---------- Canada Child Benefit ---------- */
  W['ccb-calc'] = function (el) {
    var B = D.ccb;
    shell(el, 'ccb-calc', {
      title: 'Canada Child Benefit calculator',
      intro: B ? 'Your Canada Child Benefit for ' + B.period + ', based on your ' + B.income_year + ' adjusted family net income.' : 'Canada Child Benefit estimate.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'inc', 'Adjusted family net income (' + (B ? B.income_year : CUR - 1) + ')', 70000, { min: 0, help: 'Line 23600 of both returns, added together.' }) +
          fNum(p, 'u6', 'Children under 6', 1, { min: 0, max: 12, step: 1 }) + fNum(p, 'o6', 'Children 6 to 17', 1, { min: 0, max: 12, step: 1 }) +
          fNum(p, 'dis', 'Children eligible for the disability tax credit', 0, { min: 0, max: 12, step: 1 }) +
          fRadio(p, 'sh', 'Shared custody (50% each)?', [['n', 'No'], ['y', 'Yes']], 'n') + '</div>';
      },
      calc: function (a) {
        if (!B) return msg('warnmsg', 'Figures are being confirmed.');
        function ccb(inc, u6, o6, dis) {
          var n = u6 + o6; if (!n) return { max: 0, red: 0, ccb: 0, cdb: 0, total: 0 };
          var i = Math.min(n, 4) - 1, mx = u6 * B.max_u6 + o6 * B.max_6_17;
          var red = inc <= B.t1 ? 0 : (inc <= B.t2 ? B.r1[i] * (inc - B.t1) : B.b2[i] + B.r2[i] * (inc - B.t2));
          var c = Math.max(0, mx - red), d = Math.min(dis, n), cm = d * B.cdb_max;
          var cr = inc > B.cdb_t ? (d === 1 ? B.cdb_r[0] : B.cdb_r[1]) * (inc - B.cdb_t) : 0, cd = d ? Math.max(0, cm - cr) : 0;
          return { max: mx, red: Math.min(red, mx), ccb: c, cdb: cd, total: c + cd };
        }
        var f = a.val('sh') === 'y' ? 0.5 : 1, u6 = a.n('u6'), o6 = a.n('o6'), dis = a.n('dis'), r = ccb(a.n('inc'), u6, o6, dis);
        if (!(u6 + o6)) return msg('warnmsg', 'Please enter at least one child under 18.');
        var rows = [30000, 50000, 70000, 90000, 120000, 150000, 200000].map(function (x) { var q = ccb(x, u6, o6, dis); return [money(x), money2(q.total * f), money2(q.total * f / 12)]; });
        return head('Estimated monthly payment', money2(r.total * f / 12)) + kv([['Yearly Canada Child Benefit', money2(r.ccb * f)], ['Child Disability Benefit (yearly)', money2(r.cdb * f)], ['Maximum before the income reduction', money2(r.max * f)], ['Income reduction', money2(r.red * f)]]) +
          table(['Family net income', 'Yearly benefit', 'Monthly'], rows, 'Your family\'s benefit at other incomes') +
          how('Maximum ' + money(B.max_u6) + ' a year for each child under 6 and ' + money(B.max_6_17) + ' for each child aged 6 to 17. No reduction up to ' + money(B.t1) + ' of adjusted family net income; between ' + money(B.t1) + ' and ' + money(B.t2) + ' it is reduced by ' + B.r1.map(function (x) { return pct(x, 1); }).join(', ') + ' of income over ' + money(B.t1) + ' for 1, 2, 3 and 4 or more children; above ' + money(B.t2) + ' the reduction is a fixed amount plus ' + B.r2.map(function (x) { return pct(x, 1); }).join(', ') + ' of the excess. The Child Disability Benefit adds up to ' + money(B.cdb_max) + ' a child and is reduced above ' + money(B.cdb_t) + '. Shared custody pays each parent 50%, worked out on that parent\'s own income. The CRA recalculates every July.');
      },
      next: [['/benefits/canada-child-benefit/', 'Canada Child Benefit guide'], ['/benefits/ccb-payment-dates/', 'CCB payment dates']]
    });
  };

  /* ---------- GIS and Allowance ---------- */
  W['gis-calc'] = function (el) {
    var G = D.gis;
    shell(el, 'gis-calc', {
      title: 'GIS and Allowance eligibility check',
      intro: G ? 'See whether your income is under the limit for the Guaranteed Income Supplement or the Allowance, and the highest monthly amount for your situation (' + G.quarter + ').' : '',
      fields: function (p) {
        if (!G) return '';
        var opts = G.rows.map(function (r) { return [r[0], 'GIS: ' + r[1]]; }).concat([['allowance', 'Allowance: age 60 to 64, spouse or partner receives OAS and GIS'], ['survivor', 'Allowance for the Survivor: age 60 to 64, widowed']]);
        return '<div class="ws-w-grid">' + fSel(p, 'sit', 'Your situation', opts, 'single') + fNum(p, 'inc', 'Yearly income for the previous year, not counting OAS or GIS', 15000, { min: 0, help: 'For couples, add both spouses\' income together.' }) + '</div>';
      },
      calc: function (a) {
        if (!G) return msg('warnmsg', 'Figures are being confirmed.');
        var k = a.val('sit'), row = null;
        G.rows.forEach(function (r) { if (r[0] === k) row = [r[1], r[2], r[3]]; });
        if (k === 'allowance') row = ['Allowance', G.allowance[0], G.allowance[1]];
        if (k === 'survivor') row = ['Allowance for the Survivor', G.survivor[0], G.survivor[1]];
        var ok = a.n('inc') < row[2];
        return head(ok ? 'Your income is under the limit' : 'Your income is over the limit', ok ? 'May qualify' : 'Not eligible', !ok) +
          kv([['Highest monthly amount', money2(row[1])], ['Income limit', 'Under ' + money(row[2])], ['Your income', money(a.n('inc'))]]) +
          table(['Situation', 'Maximum monthly', 'Income must be under'], G.rows.map(function (r) { return [r[1], money2(r[2]), money(r[3])]; }).concat([['Allowance', money2(G.allowance[0]), money(G.allowance[1])], ['Allowance for the Survivor', money2(G.survivor[0]), money(G.survivor[1])]]), G.quarter + ' amounts') +
          how('The maximum is the most paid in ' + G.quarter + '. The actual payment falls as income rises and reaches zero at the income limit; Service Canada works it out from the previous year\'s income on your tax return (combined income for couples). GIS is paid only to people receiving the OAS pension, so it is not paid while OAS is deferred.');
      },
      next: [['/benefits/guaranteed-income-supplement/', 'GIS guide'], ['/benefits/cpp-oas-payment-dates/', 'Payment dates']]
    });
  };

  /* ---------- Canada Disability Benefit ---------- */
  W['cdb-calc'] = function (el) {
    var B = D.cdb;
    shell(el, 'cdb-calc', {
      title: 'Canada Disability Benefit calculator',
      intro: B ? 'Estimate your monthly Canada Disability Benefit for ' + B.period + ' (maximum ' + money2(B.max_month) + ' a month).' : '',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'sit', 'Your situation', [['single', 'Single'], ['one', 'Couple, only you eligible'], ['both', 'Couple, both eligible']], 'single') +
          fNum(p, 'inc', 'Net income from the 2025 tax return (couples: both added together)', 20000, { min: 0 }) +
          fNum(p, 'wk', 'Working income in 2025 (couples: both added together)', 0, { min: 0, help: 'Employment and self-employment income.' }) + '</div>';
      },
      calc: function (a) {
        if (!B) return msg('warnmsg', 'Figures are being confirmed.');
        var sit = a.val('sit'), single = sit === 'single', inc = a.n('inc'), wk = a.n('wk');
        var wie = single ? B.wie_single : B.wie_couple, thr = single ? B.t_single : B.t_couple, rate = sit === 'both' ? B.rate_both : B.rate;
        var red = rate * Math.max(0, inc - Math.min(wk, wie) - thr), yr = Math.max(0, B.max_month * 12 - red), mo = Math.round(yr / 12 * 100) / 100;
        var zero = thr + Math.min(wk, wie) + B.max_month * 12 / rate;
        return head('Estimated monthly benefit' + (sit === 'both' ? ' (each)' : ''), money2(mo)) + kv([['Yearly', money2(yr)], ['Income reduction', money2(Math.min(red, B.max_month * 12))], ['Income where the benefit ends', money(zero)]]) +
          how('Maximum ' + money2(B.max_month) + ' a month. The benefit is reduced by ' + pct(B.rate, 0) + ' of income above ' + money(B.t_single) + ' for a single person, or above ' + money(B.t_couple) + ' of family income for a couple (' + pct(B.rate_both, 0) + ' each when both are eligible). Working income up to ' + money(B.wie_single) + ' (single) or ' + money(B.wie_couple) + ' (couple) is not counted. The income thresholds are the regulation\'s $23,000 and $32,500 multiplied by the ' + B.period + ' indexing factor of ' + B.A + '; the government\'s benefit page still shows $23,000 and $32,500. You must be 18 to 64, approved for the disability tax credit, and you and any spouse must have filed 2025 returns.');
      },
      next: [['/benefits/canada-disability-benefit/', 'Canada Disability Benefit guide'], ['/benefits/canada-disability-benefit-payment-dates/', 'Payment dates']]
    });
  };

  /* ---------- Ontario Trillium Benefit ---------- */
  W['otb-calc'] = function (el) {
    var T = D.otb;
    shell(el, 'otb-calc', {
      title: 'Ontario Trillium Benefit calculator',
      intro: T ? 'Estimate your Ontario Trillium Benefit for ' + T.period + ': the energy and property tax credit, the sales tax credit and the Northern Ontario energy credit.' : '',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fRadio(p, 'sen', 'Were you (or your spouse) 64 or older on December 31, 2025?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fRadio(p, 'mar', 'Married or common-law on December 31, 2025?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fNum(p, 'kids', 'Children under 19 living with you', 0, { min: 0, max: 12, step: 1 }) +
          fNum(p, 'inc', 'Adjusted family net income for 2025', 30000, { min: 0 }) +
          fNum(p, 'ptax', 'Ontario property tax paid in 2025', 0, { min: 0 }) + fNum(p, 'rent', 'Rent paid in Ontario in 2025', 18000, { min: 0 }) +
          fRadio(p, 'north', 'Lived in Northern Ontario on December 31, 2025?', [['n', 'No'], ['y', 'Yes']], 'n') + '</div>';
      },
      calc: function (a) {
        if (!T) return msg('warnmsg', 'Figures are being confirmed.');
        var sen = a.val('sen') === 'y', mar = a.val('mar') === 'y', kids = a.n('kids'), inc = a.n('inc'), fam = mar || kids > 0;
        var occ = a.n('ptax') + 0.2 * a.n('rent'), en = Math.min(T.energy_max, occ);
        var pt = sen ? Math.min(occ, Math.min(0.1 * occ, T.pt_s[0]) + T.pt_s[1]) : Math.min(occ, Math.min(0.1 * occ, T.pt_ns[0]) + T.pt_ns[1]);
        var thr = sen ? (mar ? T.t_couple_s : T.t_single_s) : (fam ? T.t_family_ns : T.t_single_ns);
        var oeptc = Math.max(0, en + pt - T.oeptc_rate * Math.max(0, inc - thr));
        var people = 1 + (mar ? 1 : 0) + kids, ostThr = fam ? Math.max(T.ostc[2], sen ? T.ostc[3] : 0) : (sen ? Math.max(T.ostc[1], T.ostc[3]) : T.ostc[1]);
        var ostc = Math.max(0, T.ostc[0] * people - T.ostc[4] * Math.max(0, inc - ostThr));
        var noec = a.val('north') === 'y' ? Math.max(0, (fam ? T.noec[1] : T.noec[0]) - T.noec[4] * Math.max(0, inc - (fam ? T.noec[3] : T.noec[2]))) : 0;
        var tot = oeptc + ostc + noec;
        return head('Estimated yearly Trillium benefit', money2(tot)) + kv([['Energy and property tax credit', money2(oeptc)], ['Sales tax credit', money2(ostc)], ['Northern Ontario energy credit', money2(noec)],
          ['How it is paid', tot <= 2 ? 'No payment (a yearly total of $2 or less is not paid)' : (tot < 10 ? 'One payment of $10 in July 2026' : (tot <= T.lump ? 'One payment in July 2026' : money2(tot / 12) + ' on the 10th of each month, or one payment in June 2027 if you choose it'))]]) +
          how('Energy and property tax credit: occupancy cost is property tax plus 20% of rent; the energy part is the lesser of ' + money(T.energy_max) + ' and occupancy cost; the property tax part is ' + (sen ? money(T.pt_s[1]) + ' plus 10% of occupancy cost (up to ' + money(T.pt_s[0]) + ')' : money(T.pt_ns[1]) + ' plus 10% of occupancy cost (up to ' + money(T.pt_ns[0]) + ')') + ', no more than occupancy cost; the total falls by ' + pct(T.oeptc_rate, 0) + ' of income over ' + money(thr) + '. Sales tax credit: ' + money(T.ostc[0]) + ' for each adult and child, less ' + pct(T.ostc[4], 0) + ' of income over ' + money(ostThr) + '. Northern credit: up to ' + money(fam ? T.noec[1] : T.noec[0]) + ', less ' + pct(T.noec[4], 0) + ' of income over ' + money(fam ? T.noec[3] : T.noec[2]) + '. A yearly total of ' + money(T.lump) + ' or less is paid in July 2026. The estimate leaves out long-term care, student residence and the senior homeowners\' grant adjustment.');
      },
      next: [['/benefits/ontario-trillium-benefit/', 'Ontario Trillium Benefit guide'], ['/benefits/ontario-trillium-benefit-payment-dates/', 'Payment dates']]
    });
  };

  /* ---------- Canada Workers Benefit ---------- */
  W['cwb-calc'] = function (el) {
    var B = D.cwb;
    shell(el, 'cwb-calc', {
      title: 'Canada Workers Benefit calculator ' + (B ? B.year : CUR),
      intro: 'Estimate your Canada Workers Benefit and disability supplement, and how much may be paid in advance.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fRadio(p, 'fam', 'Family situation', [['s', 'Single'], ['f', 'Spouse, partner or eligible dependant']], 's') +
          fNum(p, 'wk', 'Working income (families: combined)', 15000, { min: 0 }) + fNum(p, 'ni', 'Adjusted net income (families: combined)', 15000, { min: 0 }) +
          fNum(p, 'low', 'Families: the lower earner\'s working income', 0, { min: 0 }) +
          fSel(p, 'dis', 'Eligible for the disability tax credit', [['0', 'No one'], ['1', 'You (or one spouse)'], ['2', 'Both spouses']], '0') + '</div>';
      },
      calc: function (a) {
        if (!B) return msg('warnmsg', 'Figures are being confirmed.');
        var prov = a.val('prov'); if (B.reconfigured.indexOf(prov) >= 0) return msg('warnmsg', D.provName[prov] + ' has its own version of the Canada Workers Benefit with different amounts, which this calculator does not cover.');
        var fam = a.val('fam') === 'f', wk = a.n('wk'), ni = Math.max(0, a.n('ni') - (fam ? Math.min(a.n('low'), B.sec_exempt) : 0)), dis = +a.val('dis');
        var basic = Math.max(0, Math.min(fam ? B.max_family : B.max_single, B.phase_in * Math.max(0, wk - B.wit)) - B.po_rate * Math.max(0, ni - (fam ? B.po_family : B.po_single)));
        var sup = dis ? Math.max(0, Math.min(B.dis_max, B.phase_in * Math.max(0, wk - B.dis_wit)) - (dis === 2 ? B.dis_rate_both : B.dis_rate) * Math.max(0, ni - (fam ? B.dis_po_family : B.dis_po_single))) : 0;
        var tot = basic + sup;
        return head('Estimated ' + B.year + ' Canada Workers Benefit', money2(tot)) + kv([['Basic amount', money2(basic)], ['Disability supplement', money2(sup)], ['Paid in advance (up to ' + pct(B.advance, 0) + ')', money2(tot * B.advance)], ['Rest, when you file your ' + B.year + ' return', money2(tot * (1 - B.advance))]]) +
          how('Basic amount: ' + pct(B.phase_in, 0) + ' of working income over ' + money(B.wit) + ', up to ' + money(B.max_single) + ' (single) or ' + money(B.max_family) + ' (family), reduced by ' + pct(B.po_rate, 0) + ' of adjusted net income over ' + money(B.po_single) + ' (single) or ' + money(B.po_family) + ' (family). For couples, the lower earner\'s income is reduced by up to ' + money(B.sec_exempt) + ' of their working income. Disability supplement: up to ' + money(B.dis_max) + ', ' + pct(B.phase_in, 0) + ' of working income over ' + money(B.dis_wit) + ', reduced by ' + pct(B.dis_rate, 0) + ' (' + pct(B.dis_rate_both, 1) + ' when both spouses are eligible) of income over ' + money(B.dis_po_single) + ' (single) or ' + money(B.dis_po_family) + ' (family). Full-time students for more than 13 weeks are generally not eligible.');
      },
      next: [['/benefits/canada-workers-benefit/', 'Canada Workers Benefit guide'], ['/calculators/take-home-pay-calculator/', 'Take-home pay calculator']]
    });
  };

  /* ---------- Mortgage helpers ---------- */
  C.periodRate = function (annual, perYear) { return Math.pow(1 + annual / 2, 2 / perYear) - 1; }; // semi-annual compounding, not in advance
  C.pmt = function (loan, i, n) { return i === 0 ? loan / n : loan * i / (1 - Math.pow(1 + i, -n)); };
  C.minDown = function (price) {
    var M = D.mortgage; if (price >= M.insured_max) return price * 0.2;
    return Math.min(price, 500000) * 0.05 + Math.max(0, price - 500000) * 0.10;
  };
  C.premiumRate = function (ltv, nonTrad) {
    var M = D.mortgage, r = 0;
    for (var i = 0; i < M.premiums.length; i++) if (ltv <= M.premiums[i][0] + 1e-9) { r = M.premiums[i][1]; break; }
    if (nonTrad && ltv > 0.90) r = M.premium_non_trad;
    return ltv <= 0.80 ? 0 : r;
  };
  var FREQ = [['12', 'Monthly'], ['24', 'Semi-monthly'], ['26', 'Biweekly'], ['26a', 'Accelerated biweekly'], ['52', 'Weekly'], ['52a', 'Accelerated weekly']];
  function mortgageSchedule(loan, rate, years, f) {
    var mi = C.periodRate(rate, 12), monthly = C.pmt(loan, mi, years * 12), acc = /a$/.test(f), n = parseInt(f, 10);
    var pay = n === 12 ? monthly : (n === 24 ? monthly / 2 : (acc ? (n === 26 ? monthly / 2 : monthly / 4) : monthly * 12 / n));
    var i = C.periodRate(rate, n), bal = loan, k = 0, yrs = [], yi = 0, yp = 0;
    while (bal > 0.005 && k < n * 40) {
      var int = bal * i, prin = Math.min(pay - int, bal); if (prin <= 0) break;
      bal -= prin; k++; yi += int; yp += prin;
      if (k % n === 0 || bal <= 0.005) { yrs.push([Math.ceil(k / n), yi, yp, Math.max(0, bal)]); yi = 0; yp = 0; }
    }
    return { pay: pay, monthly: monthly, n: n, periods: k, years: yrs, i: i };
  }

  /* ---------- Mortgage payment ---------- */
  W['mortgage-payment'] = function (el) {
    shell(el, 'mortgage-payment', {
      title: 'Mortgage payment calculator',
      intro: 'Your payment, the default insurance premium if you put down less than 20%, the interest over your term and the balance left at renewal.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'price', 'Purchase price', 700000, { min: 0 }) + fNum(p, 'down', 'Down payment', 70000, { min: 0 }) +
          fNum(p, 'rate', 'Interest rate (%)', 4.5, { min: 0, max: 25, step: 0.01, help: 'Enter the rate your lender quotes; rates are compounded semi-annually.' }) +
          fSel(p, 'am', 'Amortization', [['15', '15 years'], ['20', '20 years'], ['25', '25 years'], ['30', '30 years']], '25') +
          fSel(p, 'f', 'Payment frequency', FREQ, '12') + fSel(p, 'term', 'Term', [['1', '1 year'], ['2', '2 years'], ['3', '3 years'], ['4', '4 years'], ['5', '5 years'], ['7', '7 years'], ['10', '10 years']], '5') +
          fRadio(p, 'ftb', 'First-time buyer or buying a newly built home?', [['n', 'No'], ['y', 'Yes']], 'y') + '</div>';
      },
      calc: function (a) {
        if (!D.mortgage) return msg('warnmsg', 'Mortgage rules are being confirmed.');
        var M = D.mortgage, prov = a.val('prov'), price = a.n('price'), down = a.n('down'), rate = a.n('rate') / 100, am = +a.val('am'), f = a.val('f'), term = +a.val('term');
        if (price <= 0) return msg('warnmsg', 'Please enter the purchase price.');
        var need = C.minDown(price), base = Math.max(0, price - down), ltv = base / price, insured = ltv > 0.80;
        if (down < need - 0.5) return msg('warnmsg', 'The minimum down payment on a ' + money(price) + ' home is ' + money(need) + (price >= M.insured_max ? ' (20%, because default insurance is not available at ' + money(M.insured_max) + ' or more).' : ' (5% of the first $500,000 and 10% of the rest).'));
        if (insured && am > 25 && a.val('ftb') !== 'y') return msg('warnmsg', 'With less than 20% down, the longest amortization is 25 years unless you are a first-time buyer or buying a newly built home (then 30 years).');
        var prem = insured ? C.premiumRate(ltv) + (am > 25 ? M.surcharge_30 : 0) : 0, premAmt = base * prem, loan = base + premAmt;
        var pst = insured && M.pst[prov] ? premAmt * M.pst[prov] : 0;
        var s = mortgageSchedule(loan, rate, am, f), tp = Math.min(term * s.n, s.periods), intTerm = 0, prinTerm = 0;
        s.years.forEach(function (y) { if (y[0] <= term) { intTerm += y[1]; prinTerm += y[2]; } });
        var balEnd = s.years.length >= term ? s.years[term - 1][3] : 0, intAll = sum(s.years.map(function (y) { return y[1]; }));
        var lab = FREQ.filter(function (x) { return x[0] === f; })[0][1].toLowerCase();
        var rows = s.years.filter(function (y) { return y[0] <= 5 || y[0] % 5 === 0 || y[0] === s.years.length; }).map(function (y) { return [y[0], money(y[1]), money(y[2]), money(y[3])]; });
        return head('Your ' + lab + ' payment', money2(s.pay)) + kv([['Mortgage amount', money(loan)], ['Default insurance premium', insured ? money(premAmt) + ' (' + pct(prem, 2) + ')' : 'None (20% or more down)'],
          ['Sales tax on the premium, paid at closing', pst ? money(pst) : '$0'], ['Interest over the ' + term + '-year term', money(intTerm)], ['Balance at renewal', money(balEnd)], ['Interest over the full amortization', money(intAll)], ['Paid off in', (s.periods / s.n).toFixed(1) + ' years']]) +
          table(['Year', 'Interest', 'Principal', 'Balance at year end'], rows, 'Amortization by year') +
          how('Canadian fixed-rate mortgages are compounded semi-annually, not in advance, and the calculator uses the same compounding for every frequency. Semi-monthly is half the monthly payment, biweekly is the monthly payment times 12 divided by 26, and accelerated payments are half (biweekly) or a quarter (weekly) of the monthly payment, which adds about one monthly payment a year. Default insurance premiums are a percentage of the loan and are added to it; ' + (M.pst_text || '') + ' The rate you enter is held for the whole amortization, so treat results past your term as an estimate.');
      },
      next: [['/calculators/mortgage-affordability-calculator/', 'Mortgage affordability calculator'], ['/calculators/land-transfer-tax-calculator/', 'Land transfer tax calculator']]
    });
  };

  /* ---------- Mortgage affordability ---------- */
  W['mortgage-affordability'] = function (el) {
    shell(el, 'mortgage-affordability', {
      title: 'Mortgage affordability calculator',
      intro: 'The most you can borrow and the highest price you can pay under the debt service limits and the stress test.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'inc', 'Gross household income (yearly, before tax)', 120000, { min: 0 }) +
          fNum(p, 'debt', 'Monthly debt payments (car, loans; credit cards at 3% of the balance)', 400, { min: 0 }) + fNum(p, 'down', 'Down payment available', 80000, { min: 0 }) +
          fNum(p, 'ptax', 'Property tax (monthly)', 350, { min: 0 }) + fNum(p, 'heat', 'Heating (monthly)', 100, { min: 0 }) + fNum(p, 'condo', 'Condo fees (monthly)', 0, { min: 0 }) +
          fNum(p, 'rate', 'Interest rate you expect (%)', 4.5, { min: 0, max: 25, step: 0.01 }) + fSel(p, 'am', 'Amortization', [['25', '25 years'], ['30', '30 years']], '25') +
          fRadio(p, 'ftb', 'First-time buyer or buying a newly built home?', [['n', 'No'], ['y', 'Yes']], 'y') + '</div>';
      },
      calc: function (a) {
        if (!D.mortgage) return msg('warnmsg', 'Mortgage rules are being confirmed.');
        var M = D.mortgage, inc = a.n('inc') / 12, rate = a.n('rate') / 100, q = Math.max(rate + M.buffer, M.floor), am = +a.val('am'), down = a.n('down');
        var house = a.n('ptax') + a.n('heat') + 0.5 * a.n('condo');
        var maxPI = Math.max(0, Math.min(M.gds * inc - house, M.tds * inc - house - a.n('debt')));
        var qi = C.periodRate(q, 12);
        function loanFor(price) {
          var base = Math.max(0, price - down), ltv = base / price, ins = ltv > 0.80, years = (ins && a.val('ftb') !== 'y') ? 25 : am;
          var pr = ins ? C.premiumRate(ltv) + (years > 25 ? M.surcharge_30 : 0) : 0;
          return { base: base, loan: base * (1 + pr), years: years, ins: ins, prem: pr };
        }
        function fits(price) {
          if (down < C.minDown(price) - 0.5) return false;
          var L = loanFor(price);
          return C.pmt(L.loan, qi, L.years * 12) <= maxPI + 0.005;
        }
        var lo = down, hi = down + 5000000;
        if (!fits(lo + 1)) return msg('warnmsg', 'With these figures the debt service limits leave no room for a mortgage payment. Lower debts or a larger income would change that.');
        for (var k = 0; k < 60; k++) { var mid = (lo + hi) / 2; if (fits(mid)) lo = mid; else hi = mid; }
        var price = Math.floor(lo / 100) * 100, L = loanFor(price), qp = C.pmt(L.loan, qi, L.years * 12), cp = C.pmt(L.loan, C.periodRate(rate, 12), L.years * 12);
        var limit = C.minDown(price) >= down - 0.5 ? 'your down payment' : ((M.gds * inc - house) < (M.tds * inc - house - a.n('debt')) ? 'the 39% housing cost limit' : 'the 44% total debt limit');
        return head('Highest home price', money(price)) + kv([['Mortgage (including any insurance premium)', money(L.loan)], ['Qualifying rate (stress test)', pct(q, 2)], ['Payment at the qualifying rate', money2(qp) + ' a month'], ['Payment at your rate', money2(cp) + ' a month'],
          ['Housing costs to income (GDS)', pct((qp + house) / inc, 1)], ['Total debt to income (TDS)', pct((qp + house + a.n('debt')) / inc, 1)], ['What limits you', limit]]) +
          how('Lenders qualify you at the greater of your rate plus ' + pct(M.buffer, 0) + ' or ' + pct(M.floor, 2) + '. Housing costs (mortgage payment at that rate, property tax, heating and 50% of condo fees) can be up to ' + pct(M.gds, 0) + ' of gross income, and housing costs plus other debt payments up to ' + pct(M.tds, 0) + '. With less than 20% down the price must be under ' + money(M.insured_max) + ', the minimum down payment is 5% of the first $500,000 and 10% of the rest, and a default insurance premium is added to the loan. Lenders also look at your credit and may set lower limits.');
      },
      next: [['/calculators/mortgage-payment-calculator/', 'Mortgage payment calculator'], ['/calculators/cmhc-insurance-calculator/', 'CMHC insurance calculator']]
    });
  };

  /* ---------- Land transfer tax ---------- */
  // Pure engine behind land-transfer-tax (mirrored by ltt() in qa/wscalc.py). loc: a LTT_LOC code. o: {price, mort, ftb, nb, assess, ns}
  // (ns = the Nova Scotia municipal rate as a decimal). Returns {ok, tax, reb, net, items}; each item {label, desc, lo, hi, rate, amt}:
  // desc 'slice' is a bracket slice (hi null = and up); the others are flat lines the widget words by desc. ok is false where the
  // calculator has no figures for the location.
  var LTT_LOC = [['ON', 'Ontario (outside Toronto)'], ['TO', 'Toronto'], ['BC', 'British Columbia'], ['QC', 'Quebec (provincial rates)'], ['MTL', 'Montreal'], ['QCC', 'Quebec City'], ['MB', 'Manitoba'], ['NB', 'New Brunswick'],
                 ['NS', 'Nova Scotia'], ['PE', 'Prince Edward Island'], ['NL', 'Newfoundland and Labrador'], ['AB', 'Alberta'], ['SK', 'Saskatchewan'], ['YT', 'Yukon'], ['NT', 'Northwest Territories'], ['NU', 'Nunavut']];
  C.ltt = function (loc, o) {
    var T = D.ltt, price = o.price || 0, ftb = !!o.ftb, items = [], tax = 0, reb = 0;
    if (!T) return { ok: false, tax: null, reb: null, net: null, items: [] };
    function it(label, desc, lo, hi, rate, amt) { items.push({ label: label, desc: desc, lo: lo, hi: hi, rate: rate, amt: amt }); }
    function sl(label, br, base) { var s = C.slices(br, base); s.rows.forEach(function (r) { it(label, 'slice', r[0], r[1] === Infinity ? null : r[1], r[2], r[4]); }); return s.total; }
    if (loc === 'ON' || loc === 'TO') {
      var on = sl('Ontario', T.ON.br, price); tax += on; if (ftb) reb += Math.min(T.ON.fthb, on);
      if (loc === 'TO') { var to = sl('Toronto', T.TO.br, price); tax += to; if (ftb) reb += Math.min(T.TO.fthb, to); }
    } else if (loc === 'BC') {
      tax = sl('B.C.', T.BC.br, price);
      if (price > T.BC.extra_from) { var ex = (price - T.BC.extra_from) * T.BC.extra; it('B.C. further tax', 'bc_extra', T.BC.extra_from, null, T.BC.extra, ex); tax += ex; }
      if (o.nb) reb = price <= T.BC.nbh_full ? tax : (price < T.BC.nbh_zero ? tax * (T.BC.nbh_zero - price) / (T.BC.nbh_zero - T.BC.nbh_full) : 0);
      else if (ftb) reb = price <= T.BC.fthb_part ? tax : (price <= T.BC.fthb_full ? T.BC.fthb_max : (price < T.BC.fthb_zero ? T.BC.fthb_max * (T.BC.fthb_zero - price) / (T.BC.fthb_zero - T.BC.fthb_full) : 0));
    } else if (loc === 'QC' || loc === 'MTL' || loc === 'QCC') {
      tax = sl(loc === 'MTL' ? 'Montreal' : (loc === 'QCC' ? 'Quebec City' : 'Quebec'), T[loc].br, Math.max(price, o.assess || 0));
    } else if (loc === 'MB') { tax = sl('Manitoba', T.MB.br, price);
    } else if (loc === 'NB') { tax = Math.max(price, o.assess || 0) * T.NB.rate; it('New Brunswick', 'assessed', null, null, T.NB.rate, tax);
    } else if (loc === 'NS') { tax = price * (o.ns || 0); it('Municipal deed transfer tax', 'ns', null, null, o.ns || 0, tax);
    } else if (loc === 'PE') { var bp = Math.max(price, o.assess || 0); tax = bp <= T.PE.low ? 0 : bp * T.PE.rate; it('Prince Edward Island', 'assessed', null, null, T.PE.rate, tax); if (ftb) reb = tax;
    } else if (loc === 'NL') {
      var m = o.mort || 0, d1 = T.NL.base + Math.ceil(Math.max(0, price - T.NL.from) / 100) * T.NL.per100, d2 = m > 0 ? Math.min(T.NL.mort_cap, T.NL.base + Math.ceil(Math.max(0, m - T.NL.from) / 100) * T.NL.per100) : 0;
      tax = d1 + d2; it('Deed registration', 'nl_deed', null, null, null, d1); if (d2) it('Mortgage registration', 'nl_mort', null, null, null, d2);
    } else if (loc === 'AB') {
      var mm = o.mort || 0, f1 = T.AB.base + T.AB.per5000 * Math.floor(price / 5000), f2 = mm > 0 ? T.AB.mort_base + T.AB.per5000 * Math.floor(mm / 5000) : 0;
      tax = f1 + f2; it('Land title transfer', 'ab_title', null, null, null, f1); if (f2) it('Mortgage registration', 'ab_mort', null, null, null, f2);
    } else if (loc === 'SK' && T.SK) {
      var tf = 0, tt = T.SK.transfer; for (var j = 0; j < tt.length; j++) { if (tt[j][0] == null || price <= tt[j][0]) { tf = tt[j][2] === 'rate' ? price * tt[j][1] : tt[j][1]; break; } }
      var sm = o.mort || 0, mf = 0; if (sm > 0) { var mt = T.SK.mortgage; for (var q = 0; q < mt.length; q++) { if (mt[q][0] == null || sm <= mt[q][0]) { mf = mt[q][1]; break; } } }
      tax = tf + mf; it('Title transfer', price > 6300 ? 'sk_rate' : 'sk_flat', null, null, null, tf); if (mf) it('Mortgage registration', 'sk_mort', null, null, null, mf);
    } else return { ok: false, tax: null, reb: null, net: null, items: [] };
    return { ok: true, tax: tax, reb: reb, net: tax - reb, items: items };
  };

  W['land-transfer-tax'] = function (el) {
    var LOC = LTT_LOC;
    shell(el, 'land-transfer-tax', {
      title: 'Land transfer tax calculator',
      intro: 'Land transfer tax or registration fees on a home purchase, with first-time buyer rebates where they apply.',
      fields: function (p) {
        // data-province takes any location code: a province, or TO (Toronto), MTL (Montreal) or QCC (Quebec City).
        var d = PRESET.prov && LOC.some(function (x) { return x[0] === PRESET.prov; }) ? PRESET.prov : 'ON';
        return '<div class="ws-w-grid">' + fSel(p, 'loc', 'Where the home is', LOC, d) + fNum(p, 'price', 'Purchase price', 700000, { min: 0 }) +
          fNum(p, 'mort', 'Mortgage amount (Alberta, Saskatchewan and Newfoundland and Labrador registration fees)', 560000, { min: 0 }) +
          fRadio(p, 'ftb', 'First-time buyer?', [['n', 'No'], ['y', 'Yes']], 'y') + fRadio(p, 'nb', 'Newly built home (British Columbia)?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fNum(p, 'assess', 'Assessed value, if higher than the price (New Brunswick and Prince Edward Island)', 0, { min: 0 }) +
          fNum(p, 'ns', 'Nova Scotia municipal deed transfer tax rate (%)', 1.5, { min: 0, max: 2, step: 0.05, help: 'Halifax charges 1.5%; other municipalities charge 1% to 1.5%.' }) + '</div>';
      },
      calc: function (a) {
        var T = D.ltt; if (!T) return msg('warnmsg', 'Figures are being confirmed.');
        var loc = a.val('loc'), price = a.n('price'), ftb = a.val('ftb') === 'y', nb = a.val('nb') === 'y', note = '', h;
        var R = C.ltt(loc, { price: price, mort: a.n('mort'), ftb: ftb, nb: nb, assess: a.n('assess'), ns: a.n('ns') / 100 });
        if (!R.ok) return msg('warnmsg', 'This calculator does not cover ' + LOC.filter(function (x) { return x[0] === loc; })[0][1] + ' yet.');
        var tax = R.tax, reb = R.reb, DASH = '—', PORTION = { assessed: 'Greater of price and assessed value', ns: 'Purchase price', nl_deed: '$100 plus 40 cents per $100 over $500', nl_mort: 'Same scale, up to ' + money(T.NL.mort_cap),
          ab_title: '$50 plus $5 for each $5,000 of value', ab_mort: '$50 plus $5 for each $5,000 of principal', sk_rate: '0.4% of the value', sk_flat: 'Flat fee', sk_mort: 'Flat fee by mortgage amount' };
        var rows = R.items.map(function (x) {
          if (x.desc === 'slice') return [x.label, money(x.lo) + (x.hi == null ? ' and up' : ' to ' + money(x.hi)), pct(x.rate, 2), money2(x.amt)];
          if (x.desc === 'bc_extra') return [x.label, 'Residential portion over ' + money(x.lo), pct(x.rate, 0), money2(x.amt)];
          return [x.label, PORTION[x.desc], x.desc === 'assessed' ? pct(x.rate, 0) : (x.desc === 'ns' ? pct(x.rate, 2) : (x.desc === 'sk_rate' ? '0.40%' : DASH)), money2(x.amt)];
        });
        if (loc === 'ON' || loc === 'TO') {
          note = 'First-time buyers can get a refund of up to ' + money(T.ON.fthb) + ' of Ontario tax' + (loc === 'TO' ? ' and a rebate of up to ' + money(T.TO.fthb) + ' of Toronto tax' : '') + ' if they are 18 or older, have never owned a home anywhere, and move in within nine months.';
        } else if (loc === 'BC') {
          if (nb) note = 'Newly built home exemption: full up to ' + money(T.BC.nbh_full) + ', reduced to $0 at ' + money(T.BC.nbh_zero) + '.';
          else if (ftb) note = 'First-time buyers\' exemption: tax on the first ' + money(T.BC.fthb_part) + ' (up to ' + money(T.BC.fthb_max) + ') for homes up to ' + money(T.BC.fthb_full) + ', reduced proportionally to $0 at ' + money(T.BC.fthb_zero) + '.';
        } else if (loc === 'QC' || loc === 'MTL' || loc === 'QCC') {
          note = loc === 'QC' ? 'Municipalities may charge a higher rate (up to 3%) on the part above $500,000; Montreal and Quebec City do.' : 'The base is the greatest of the price paid, the price stated and the market value.';
          if (loc === 'MTL' && T.MTL.fthb_none) note += ' Montreal\'s welcome tax has no first-time buyer exemption' + (T.MTL.fthb_closed ? ', and the City\'s home-buyer assistance program closed to new applications on ' + fmtDate(T.MTL.fthb_closed) + '; since April 2026, Quebec\'s refundable tax credit for access to homeownership replaces it' : '') + '.';
        } else if (loc === 'MB') { note = 'Manitoba charges this tax on the fair market value of the property on the date the transfer is registered.';
        } else if (loc === 'NS') { note = 'Each municipality sets its own rate.';
        } else if (loc === 'PE') { note = 'Qualifying first-time buyers are exempt; no tax applies at ' + money(T.PE.low) + ' or less.';
        } else if (loc === 'NL') { note = 'Newfoundland and Labrador charges deed and mortgage registration fees on a purchase.';
        } else if (loc === 'AB') { note = 'Alberta charges land titles registration fees. The fee schedule does not say how part of $5,000 is counted, so this estimate counts full $5,000 steps.';
        } else if (loc === 'SK') { note = 'Saskatchewan charges land registry fees: 0.4% of the value of the title over $6,300, and a flat mortgage registration fee by amount.'; }
        h = head('Tax and fees on closing', money2(tax - reb)) + kv([['Before rebates', money2(tax)], ['First-time buyer or new home rebate', money2(reb)], ['Share of the price', pct(price ? (tax - reb) / price : 0, 2)]]);
        if (rows.length) h += table(['Tax', 'Portion of the price', 'Rate', 'Amount'], rows, 'How it is worked out');
        return h + (note ? how(note + ' Rates as of ' + fmtDate(D.asOf) + '. Other closing costs such as legal fees are extra.') : '');
      },
      next: [['/calculators/mortgage-affordability-calculator/', 'Mortgage affordability calculator'], ['/calculators/mortgage-payment-calculator/', 'Mortgage payment calculator']]
    });
  };

  /* =====================================================================
   * 4c. WIDGETS ADDED FOR PAGES 202 TO 296 (October 28, 2026)
   * A figure the research registers have not confirmed is null in the data; the widgets show TBD for it.
   * ===================================================================== */
  var TBD = 'Figure being confirmed';
  function isNum(x) { return typeof x === 'number' && isFinite(x); }
  function ym(m) { var y = Math.floor(m / 12), r = m % 12; return (y ? y + ' year' + (y === 1 ? '' : 's') : '') + (y && r ? ' and ' : '') + (r ? r + ' month' + (r === 1 ? '' : 's') : ''); }
  function shares(x) { return rnd(x, 4).toLocaleString('en-CA', { maximumFractionDigits: 4 }); }

  /* ---------- FIRE ---------- */
  // Months until savings reach spend / wr, compounding monthly at the monthly equivalent of the yearly real return r, contributions at month end.
  C.fire = function (spend, sav, contrib, r, wr) {
    if (!(wr > 0) || !(r > -1)) return null;
    var number = spend / wr, i = Math.pow(1 + r, 1 / 12) - 1, pm = contrib / 12, bal = sav, m = 0;
    while (bal < number && m < 1200) { bal = bal * (1 + i) + pm; m++; }
    var ok = bal >= number;
    return { number: number, months: ok ? m : null, years: ok ? m / 12 : null };
  };
  C.coastFire = function (number, r, years) { return years > 0 ? number / Math.pow(1 + r, years) : number; };
  C.fireTable = function (income, sav, r, wr) {
    var rows = [];
    for (var k = 1; k <= 7; k++) { var s = k / 10, c = income * s, sp = income - c; rows.push({ rate: s, save: c, spend: sp, f: C.fire(sp, sav, c, r, wr) }); }
    return rows;
  };

  W['fire-calc'] = function (el) {
    shell(el, 'fire-calc', {
      title: 'FIRE calculator',
      intro: 'Your financial independence number, how long it takes to get there, and the Coast FIRE amount you need today.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'spend', 'Yearly spending in retirement', 40000, { min: 0 }) + fNum(p, 'sav', 'Invested savings today', 100000, { min: 0 }) +
          fNum(p, 'contrib', 'Yearly contributions', 25000, { min: 0 }) + fNum(p, 'r', 'Expected real return (% a year, after inflation)', 4, { min: -10, max: 15 }) +
          fNum(p, 'wr', 'Withdrawal rate (%)', 4, { min: 0.5, max: 10 }) + fNum(p, 'age', 'Your age now', CUR - bornDefault(), { min: 16, max: 90, step: 1 }) +
          fNum(p, 'tage', 'Target age for Coast FIRE', 55, { min: 20, max: 90, step: 1 }) +
          fNum(p, 'inc', 'Yearly take-home income (for the savings-rate table)', 80000, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var r = a.n('r') / 100, wr = a.n('wr') / 100, sav = a.n('sav'), age = a.n('age'), tage = a.n('tage');
        if (!(wr > 0)) return msg('warnmsg', 'Please enter a withdrawal rate above 0%.');
        if (!(r > -1)) return msg('warnmsg', 'Please enter a return above -100%.');
        var f = C.fire(a.n('spend'), sav, a.n('contrib'), r, wr), coast = C.coastFire(f.number, r, tage - age);
        var when = f.months == null ? 'More than 100 years' : (f.months === 0 ? 'Already reached' : ym(f.months));
        var rows = C.fireTable(a.n('inc'), sav, r, wr).map(function (x) { return [pct(x.rate, 0), money(x.save), money(x.spend), money(x.f.number), x.f.months == null ? 'More than 100' : nf(x.f.years, 1)]; });
        return head('Your FIRE number', money(f.number)) + kv([['Time to reach it', when], ['Age when you reach it', f.months == null ? '—' : String(Math.floor(age + f.years))],
          ['Coast FIRE amount needed today (to reach it by ' + tage + ')', money(coast)], ['Your savings compared with Coast FIRE', sav >= coast ? 'Reached' : money(coast - sav) + ' short']]) +
          table(['Savings rate', 'Yearly saving', 'Yearly spending', 'FIRE number', 'Years to reach it'], rows, 'Years to financial independence on ' + money(a.n('inc')) + ' of take-home income, starting from your savings today') +
          how('FIRE number = yearly spending divided by the withdrawal rate (' + pct(wr, 1) + ' means ' + nf(1 / wr, 1) + ' times spending). Savings grow each month at the monthly equivalent of the real return, and contributions are added at the end of each month. A real return is after inflation, so every amount is in today\'s dollars. Coast FIRE is the amount that would grow to your FIRE number by the target age with no more contributions. The table treats the income you enter as take-home pay: what you do not save, you spend. Tax on withdrawals is not included, and neither are CPP and OAS, which reduce how much your savings need to cover. Returns are an assumption, not a forecast.');
      },
      next: [['/retirement/early-retirement-fire/', 'FIRE in Canada'], ['/retirement/safe-withdrawal-rate/', 'Safe withdrawal rate'], ['/retirement/how-much-to-retire/', 'How much you need to retire']]
    });
  };

  /* ---------- Withdrawal rate ---------- */
  // Withdrawal at the start of each year, then a year of growth. path: optional returns for the first years, then r.
  C.drawdown = function (B, w, r, n, path) {
    var bal = B, lasts = null, endN = null;
    for (var y = 1; y <= 100; y++) {
      var ry = Math.max(-1, path && y <= path.length ? path[y - 1] : r);
      if (lasts == null) {
        if (w > 0 && bal < w) { lasts = y - 1 + bal / w; bal = 0; }
        else bal = (bal - w) * (1 + ry);
      }
      if (y === n) endN = bal;
      if (lasts != null && y >= n) break;
    }
    var forever = lasts == null && !path && (w <= 0 || (B - w) * (1 + r) >= B);
    return { lasts: lasts, forever: forever, endN: endN == null ? 0 : endN };
  };
  C.seqPath = [-0.15, -0.10, -0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0];
  C.withdrawal = function (B, w, r, n) {
    var bad = C.seqPath.map(function (o) { return r + o; }), good = bad.slice().reverse();
    return { base: C.drawdown(B, w, r, n), table: [0.03, 0.04, 0.05, 0.06].map(function (q) { return { rate: q, w: B * q, d: C.drawdown(B, B * q, r, n) }; }),
             bad: C.drawdown(B, w, r, n, bad), good: C.drawdown(B, w, r, n, good) };
  };
  function lastsTxt(d) { return d.lasts != null ? nf(d.lasts, 1) + ' years' : (d.forever ? 'Does not run out' : 'More than 100 years'); }

  W['withdrawal-rate'] = function (el) {
    shell(el, 'withdrawal-rate', {
      title: 'Withdrawal rate calculator',
      intro: 'How long your savings last at a yearly withdrawal, and how the order of good and bad years changes the result.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'bal', 'Portfolio today', 1000000, { min: 0 }) +
          fRadio(p, 'mode', 'Enter the withdrawal as', [['amt', 'A dollar amount'], ['pct', 'A percentage']], 'amt') +
          fNum(p, 'w', 'Yearly withdrawal ($)', 40000, { min: 0 }) + fNum(p, 'wp', 'Or yearly withdrawal (% of the portfolio today)', 4, { min: 0, max: 50 }) +
          fNum(p, 'r', 'Expected real return (% a year, after inflation)', 4, { min: -10, max: 15 }) + fNum(p, 'n', 'Years to show the balance for', 30, { min: 1, max: 100, step: 1 }) + '</div>';
      },
      calc: function (a) {
        var B = a.n('bal'), r = a.n('r') / 100, n = clamp(Math.round(a.n('n')), 1, 100);
        var w = a.val('mode') === 'pct' ? B * a.n('wp') / 100 : a.n('w');
        if (!(r > -1)) return msg('warnmsg', 'Please enter a return above -100%.');
        var X = C.withdrawal(B, w, r, n);
        return head('Your money lasts', lastsTxt(X.base)) + kv([['Yearly withdrawal', money(w)], ['Withdrawal rate', pct(B ? w / B : 0, 2)], ['Balance after ' + n + ' years', money(X.base.endN)]]) +
          table(['Withdrawal rate', 'Yearly withdrawal', 'Money lasts', 'Balance after ' + n + ' years'], X.table.map(function (t) { return [pct(t.rate, 0), money(t.w), lastsTxt(t.d), money(t.d.endN)]; }), 'At a ' + pct(r, 1) + ' real return') +
          table(['Order of returns', 'Money lasts', 'Balance after ' + n + ' years'], [['The same return every year', lastsTxt(X.base), money(X.base.endN)], ['Bad years first', lastsTxt(X.bad), money(X.bad.endN)], ['Bad years last', lastsTxt(X.good), money(X.good.endN)]], 'Sequence of returns: same average return, different order') +
          how('Each year\'s withdrawal comes out at the start of the year and the rest grows at the real return, so amounts are in today\'s dollars. The sequence example uses a fixed ten-year path. Bad years first: your return minus 15, 10 and 5 percentage points in years 1 to 3, plus 5 points in years 4 to 9 and your return in year 10. Bad years last: the same ten returns in reverse order. Both paths have the same average return, and both earn your return from year 11. Losses early in retirement do more damage because withdrawals sell more of the portfolio while it is down. Tax, fees, CPP and OAS are not included. Returns are an assumption, not a forecast.');
      },
      next: [['/retirement/safe-withdrawal-rate/', 'Safe withdrawal rate'], ['/retirement/retirement-withdrawal-order/', 'Which accounts to draw from first'], ['/calculators/fire-calculator/', 'FIRE calculator']]
    });
  };

  /* ---------- Adjusted cost base (average cost) ---------- */
  // tx: [{type: buy | sell | reinv | roc | split, shares, amount}]. Empty rows are skipped.
  C.acb = function (tx) {
    var sh = 0, acb = 0, gains = 0, rows = [], err = null;
    for (var k = 0; k < tx.length; k++) {
      var t = tx[k], q = t.shares, amt = t.amount, gain = null, cost = null;
      var empty = t.type === 'roc' ? amt === 0 : (t.type === 'split' ? q === 0 : q === 0 && amt === 0);
      if (empty) { rows.push({ skip: true }); continue; }
      if (t.type === 'buy' || t.type === 'reinv') { sh += q; acb += amt; }
      else if (t.type === 'roc') { acb -= amt; if (acb < 0) { gain = -acb; acb = 0; } }
      else if (t.type === 'split') { sh = q; }
      else if (t.type === 'sell') {
        if (q === 0) { err = { row: k, text: 'enter the number of shares or units sold' }; break; }
        if (sh <= 0 || q > sh + 1e-9) { err = { row: k, text: 'sells more shares or units than you hold at that point' }; break; }
        cost = acb * q / sh; gain = amt - cost; acb -= cost; sh -= q;
        if (sh < 1e-9) { sh = 0; acb = 0; }
      }
      if (gain != null) gains += gain;
      rows.push({ skip: false, shares: sh, acb: acb, per: sh > 0 ? acb / sh : 0, cost: cost, gain: gain });
    }
    return { rows: rows, shares: sh, acb: acb, per: sh > 0 ? acb / sh : 0, gains: gains, error: err };
  };

  W['acb-calc'] = function (el) {
    var TYPES = [['buy', 'Buy'], ['sell', 'Sell'], ['reinv', 'Reinvested distribution'], ['roc', 'Return of capital'], ['split', 'Split or consolidation']];
    var SAMPLE = [['2024-02-01', 'buy', 100, 5000], ['2025-01-15', 'buy', 50, 3000], ['2026-06-10', 'sell', 60, 4200]];
    var P = '', count = 0;
    function row(r) {
      var i = count++;
      return '<div class="ws-w-grid ws-acb-row" data-row="' + i + '" style="border-top:1px solid var(--ws-step1);padding-top:10px;margin-top:10px">' +
        fDate(P, 'd' + i, 'Date (optional)', r[0]) + fSel(P, 't' + i, 'Type', TYPES, r[1]) + fNum(P, 'q' + i, 'Shares or units', r[2], { min: 0 }) + fNum(P, 'a' + i, 'Total amount ($)', r[3], { min: 0 }) +
        '<div class="ws-field"><span class="ws-flabel">Transaction ' + (i + 1) + '</span><button type="button" class="ws-w-btn ws-secondary" data-rm="1">Remove</button></div></div>';
    }
    function sample() { count = 0; return SAMPLE.map(row).join(''); }
    shell(el, 'acb-calc', {
      title: 'Adjusted cost base (ACB) calculator',
      intro: 'List your purchases, sales, reinvested distributions, returns of capital and splits. We work out your ACB per share and the gain or loss on each sale with the average cost method.',
      fields: function (p) {
        P = p;
        return '<p class="ws-note">Enter transactions in the order they happened. Total amount: for a buy or reinvested distribution, the cost including commissions; for a sale, the proceeds after commissions; for a return of capital, the amount returned. For a split, enter the shares you hold after it.</p>' +
          '<div class="ws-acb-rows">' + sample() + '</div><div class="ws-w-actions"><button type="button" class="ws-w-btn ws-secondary" data-add="1">Add a transaction</button></div>';
      },
      init: function (a) {
        var box = a.form.querySelector('.ws-acb-rows');
        a.form.addEventListener('click', function (e) {
          var t = e.target;
          if (t.getAttribute('data-add')) { box.insertAdjacentHTML('beforeend', row(['', 'buy', '', ''])); a.form.dispatchEvent(new Event('change')); }
          else if (t.getAttribute('data-rm')) { var r = t.closest('.ws-acb-row'); if (r) r.parentNode.removeChild(r); a.form.dispatchEvent(new Event('change')); }
        });
        a.form.addEventListener('reset', function () { setTimeout(function () { box.innerHTML = sample(); }, 0); });
      },
      calc: function (a) {
        var els = a.form.querySelectorAll('.ws-acb-row'), tx = [], dates = [];
        Array.prototype.forEach.call(els, function (e) {
          var i = e.getAttribute('data-row');
          tx.push({ type: a.val('t' + i), shares: Math.max(0, a.n('q' + i)), amount: Math.max(0, a.n('a' + i)), date: a.val('d' + i) });
        });
        if (!tx.length) return msg('warnmsg', 'Please add at least one transaction.');
        var r = C.acb(tx);
        if (r.error) return msg('warnmsg', 'Transaction ' + (r.error.row + 1) + ' ' + r.error.text + '. Please check it.');
        tx.forEach(function (t, k) { if (t.date && !r.rows[k].skip) dates.push(t.date); });
        var sorted = dates.every(function (d, k) { return !k || d >= dates[k - 1]; });
        var lab = {}; TYPES.forEach(function (x) { lab[x[0]] = x[1]; });
        var rows = [];
        tx.forEach(function (t, k) {
          var x = r.rows[k]; if (x.skip) return;
          rows.push([k + 1, t.date ? fmtDate(t.date, { year: 'numeric', month: 'short', day: 'numeric' }) : '—', lab[t.type] || t.type, t.type === 'roc' ? '—' : shares(t.shares), t.type === 'split' ? '—' : money2(t.amount),
            shares(x.shares), money2(x.acb), x.shares > 0 ? money2(x.per) : '—', x.gain == null ? '—' : money2(x.gain)]);
        });
        var incl = D.tax.capital_gains_inclusion;
        return head('Adjusted cost base per share', r.shares > 0 ? money2(r.per) : 'No shares left') +
          kv([['Shares or units held', shares(r.shares)], ['Total ACB', money2(r.acb)], ['Net capital gain or loss on these transactions', money2(r.gains)], ['Taxable capital gain (' + pct(incl, 0) + ')', r.gains > 0 ? money2(r.gains * incl) : 'None']]) +
          (sorted ? '' : msg('warnmsg', 'Your dates are not in order. Transactions are worked out in the order listed, so please put them in date order.')) +
          table(['#', 'Date', 'Type', 'Shares', 'Amount', 'Shares held after', 'Total ACB after', 'ACB per share', 'Gain or loss'], rows, 'Your transactions, step by step') +
          how('Average cost method: each purchase or reinvested distribution adds its cost to the total ACB, and each sale removes the average cost of the shares sold (total ACB divided by shares held, times shares sold). Gain or loss = proceeds after commissions minus that cost. A return of capital lowers the ACB without changing the number of shares; if the ACB would fall below zero, the negative amount is a capital gain for that year and the ACB becomes zero. A split changes the number of shares but not the total ACB. Identical shares held in all your non-registered accounts are pooled into one ACB. The superficial loss rule is not checked here.');
      },
      next: [['/tax/adjusted-cost-base/', 'Adjusted cost base explained'], ['/calculators/capital-gains-tax-calculator/', 'Capital gains tax calculator'], ['/tax/return-of-capital/', 'Return of capital']]
    });
  };

  /* ---------- Dividend income ---------- */
  C.divIncome = function (prov, value, y, kind, share, other) {
    var T = D.tax, yearly = value * y, e = kind === 'elig' ? yearly : (kind === 'nonelig' ? 0 : yearly * clamp(share, 0, 1)), n = yearly - e;
    var ok = !!T.dividends.provincial_dtc[prov];
    var eg = e * (1 + T.dividends.eligible_grossup), ng = n * (1 + T.dividends.noneligible_grossup);
    var tax = ok ? C.tax(prov, other + eg + ng, { elig: eg, nonelig: ng }).total - C.tax(prov, other).total : null;
    return { yearly: yearly, monthly: yearly / 12, elig: e, nonelig: n, grossed: eg + ng, tax: tax, after: ok ? yearly - tax : null, ok: ok };
  };
  C.divNeeded = function (monthly, y) { return y > 0 ? monthly * 12 / y : null; };

  W['dividend-income'] = function (el) {
    shell(el, 'dividend-income', {
      title: 'Dividend income calculator',
      intro: 'Yearly and monthly income from a dividend portfolio, the tax on it, and the portfolio you need for a monthly income target.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'val', 'Portfolio value', 100000, { min: 0 }) +
          fNum(p, 'y', 'Dividend yield (% a year)', 4, { min: 0, max: 20 }) +
          fSel(p, 'kind', 'Type of dividends', [['elig', 'Eligible'], ['nonelig', 'Other than eligible'], ['mixed', 'A mix of both']], 'elig') +
          fNum(p, 'es', 'If a mix: share that is eligible (%)', 50, { min: 0, max: 100 }) +
          fNum(p, 'inc', 'Other taxable income', MEM.get('income', 75000), { min: 0 }) + fNum(p, 'goal', 'Monthly income target', 1000, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), y = a.n('y') / 100; MEM.set('prov', prov);
        var r = C.divIncome(prov, a.n('val'), y, a.val('kind'), a.n('es') / 100, a.n('inc')), need = C.divNeeded(a.n('goal'), y);
        var h = head('Yearly dividend income, before tax', money(r.yearly)) + kv([['Monthly, before tax', money(r.monthly)], ['Tax on these dividends', r.ok ? money(r.tax) : 'Being confirmed'],
          ['Yearly, after tax', r.ok ? money(r.after) : 'Being confirmed'], ['Monthly, after tax', r.ok ? money(r.after / 12) : 'Being confirmed'], ['Effective tax rate on the dividends', r.ok ? pct(r.yearly ? r.tax / r.yearly : 0, 1) : 'Being confirmed'],
          ['Portfolio needed for ' + money(a.n('goal')) + ' a month', need == null ? 'Enter a yield above 0%' : money(need)]]);
        if (!r.ok) h += msg('warnmsg', 'Dividend tax credit rates for ' + D.provName[prov] + ' are being confirmed for ' + CUR + '. The after-tax figures currently cover ' + Object.keys(D.tax.dividends.provincial_dtc).map(function (k) { return D.provName[k]; }).join(', ') + '.');
        return h + how('Yearly income = portfolio value x yield. Eligible dividends are grossed up by ' + pct(D.tax.dividends.eligible_grossup, 0) + ' and other than eligible dividends by ' + pct(D.tax.dividends.noneligible_grossup, 0) + ', and federal and provincial dividend tax credits then reduce the tax. Tax = your ' + CUR + ' tax with the dividends minus your tax without them, so it can be below zero when the credits also shelter tax on your other income. Assumes Canadian dividends in a non-registered account; dividends in a TFSA or RRSP are not taxed this way, and foreign dividends get no gross-up or credit. Yields change and dividends are not guaranteed.');
      },
      next: [['/calculators/dividend-tax-calculator/', 'Dividend tax calculator'], ['/tax/dividend-tax-credit/', 'Dividend tax credit'], ['/tax/t5-slip/', 'T5 slips']]
    });
  };

  /* ---------- Prescribed rate loan ---------- */
  C.prescribedLoan = function (prov, loan, rate, y, hi, lo) {
    var inc = loan * y, it = loan * rate, tHi = C.tax(prov, hi).total, tLo = C.tax(prov, lo).total;
    var dHi = C.tax(prov, hi + inc).total, lHi = C.tax(prov, hi + it).total, lLo = C.tax(prov, lo + inc - it).total;
    return { income: inc, interest: it, lowNet: inc - it, direct: { hi: dHi, lo: tLo, total: dHi + tLo }, loan: { hi: lHi, lo: lLo, total: lHi + lLo }, saving: dHi + tLo - lHi - lLo };
  };
  function prescribedNow() { var x = D.prescribed_rate && D.prescribed_rate.current; return isNum(x) ? (x >= 1 ? x / 100 : x) : null; }

  W['prescribed-loan'] = function (el) {
    var pr = prescribedNow();
    shell(el, 'prescribed-loan', {
      title: 'Prescribed rate loan calculator',
      intro: 'Estimate the yearly family tax saved when the higher-income spouse lends money to the lower-income spouse at the CRA prescribed rate.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'loan', 'Loan amount', 100000, { min: 0 }) +
          fNum(p, 'rate', 'Prescribed rate on the loan (%)', pr == null ? '' : rnd(pr * 100, 2), { min: 0, max: 20, ph: pr == null ? 'Enter the rate' : '', help: pr == null ? 'The current prescribed rate is being confirmed. Enter the rate in your loan agreement.' : 'The CRA rate in effect when the loan is made.' }) +
          fNum(p, 'y', 'Expected yearly investment income (% of the loan)', 5, { min: 0, max: 30 }) +
          fNum(p, 'hi', 'Higher-income spouse: taxable income', 150000, { min: 0 }) + fNum(p, 'lo', 'Lower-income spouse: taxable income', 30000, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'); MEM.set('prov', prov);
        if (a.val('rate') === '') return msg('warnmsg', 'The current prescribed rate is being confirmed. Enter the rate in your loan agreement to see the result.');
        var r = C.prescribedLoan(prov, a.n('loan'), a.n('rate') / 100, a.n('y') / 100, a.n('hi'), a.n('lo'));
        return head('Estimated family tax saved each year', money(r.saving), r.saving < 0) +
          kv([['Investment income', money(r.income)], ['Interest paid to the higher-income spouse (deductible for the borrower, taxable to the lender)', money(r.interest)], ['Income taxed to the lower-income spouse after the interest', money(r.lowNet)]]) +
          table(['', 'Higher earner invests directly', 'Prescribed rate loan'], [['Higher-income spouse tax', money(r.direct.hi), money(r.loan.hi)], ['Lower-income spouse tax', money(r.direct.lo), money(r.loan.lo)], ['<b>Family total</b>', '<b>' + money(r.direct.total) + '</b>', '<b>' + money(r.loan.total) + '</b>']], 'Yearly tax for each spouse') +
          how('The higher-income spouse lends money to the lower-income spouse at the CRA prescribed rate in effect when the loan is made, and that rate applies for the life of the loan. The borrower invests the money and reports the investment income. The interest is deductible for the borrower and taxable to the lender. The borrower must pay the interest for each year no later than January 30 of the following year; if a payment is late or missed, the attribution rules apply to the income for that year and every later year. Investment income is taxed here as ordinary income such as interest; dividends and capital gains are taxed differently, which changes the saving. Uses ' + CUR + ' brackets.');
      },
      next: [['/tax/prescribed-rate-loan/', 'Prescribed rate loans'], ['/tax/attribution-rules/', 'Attribution rules']]
    });
  };

  /* ---------- Donation tax credit ---------- */
  C.donation = function (prov, amt, income, inKind, acb) {
    var F = D.donation_federal, first = Math.min(amt, 200), rest = Math.max(0, amt - 200);
    var top = Math.min(rest, Math.max(0, income - F.top_from));
    var fed = first * F.first + top * F.top + (rest - top) * F.above;
    if (prov === 'QC') fed = fed * (1 - D.tax.qc_abatement);
    var R = (D.donation_rates || {})[prov], pv = null;
    if (R && isNum(R[0]) && isNum(R[1])) { var hp = isNum(R[2]) && isNum(R[3]) ? Math.min(rest, Math.max(0, income - R[3])) : 0; pv = first * R[0] + (rest - hp) * R[1] + (hp > 0 ? hp * R[2] : 0); }
    var gain = inKind ? Math.max(0, amt - acb) : 0;
    var cg = gain > 0 ? C.tax(prov, income + gain * D.tax.capital_gains_inclusion).total - C.tax(prov, income).total : 0;
    var cr = fed + (pv || 0);
    return { fed: fed, prov: pv, credits: pv == null ? null : cr, gain: gain, cgTax: cg, net: pv == null ? null : amt - cr, netFed: amt - fed, netSold: pv == null ? null : amt - cr + cg };
  };

  W['donation-credit'] = function (el) {
    shell(el, 'donation-credit', {
      title: 'Charitable donation tax credit calculator',
      intro: 'Your federal and provincial donation credits, the net cost of a gift, and the capital gains tax you avoid by donating shares directly.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'amt', 'Donations in the year (or value of the shares)', 5000, { min: 0 }) +
          fNum(p, 'inc', 'Taxable income', MEM.get('income', 100000), { min: 0 }) +
          fRadio(p, 'kind', 'Donating publicly listed shares directly (in kind)?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fNum(p, 'acb', 'If shares: their adjusted cost base', 2000, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), amt = a.n('amt'), inc = a.n('inc'), kind = a.val('kind') === 'y'; MEM.set('prov', prov);
        var r = C.donation(prov, amt, inc, kind, a.n('acb')), F = D.donation_federal;
        var h = r.prov == null ? head('Net cost after the federal credit', money(r.netFed)) : head('Net cost of your gift', money(r.net));
        var items = [['Federal credit', money(r.fed)], [D.provName[prov] + ' credit', r.prov == null ? TBD : money(r.prov)], ['Total credits', r.prov == null ? TBD : money(r.credits)]];
        if (kind) items.push(['Capital gain on the shares', money(r.gain)], ['Capital gains tax avoided compared with selling', money(r.cgTax)], ['Net cost if you sold the shares and gave cash', r.prov == null ? TBD : money(r.netSold)]);
        h += kv(items);
        if (r.prov == null) h += msg('warnmsg', D.provName[prov] + '\'s donation credit rates for ' + CUR + ' are being confirmed, so the net cost shown includes the federal credit only.');
        if (amt > 0.75 * inc) h += msg('warnmsg', 'You can claim gifts up to 75% of your net income in a year. The rest can be carried forward up to five years.');
        return h + how('Federal credit: ' + pct(F.first, 0) + ' (the lowest federal rate) on the first $200 of gifts in the year, ' + pct(F.above, 0) + ' on the rest, and ' + pct(F.top, 0) + ' instead of ' + pct(F.above, 0) + ' on the part of the rest that is not more than your taxable income above ' + money(F.top_from) + '.' + (prov === 'QC' ? ' For Quebec residents the federal credit is reduced by the 16.5% Quebec abatement.' : '') + ' Your province adds its own credit' + ((D.donation_rates_year || {})[prov] && D.donation_rates_year[prov] < CUR ? ' (provincial rates from the ' + D.donation_rates_year[prov] + ' tax forms; the ' + CUR + ' forms come out in early ' + (CUR + 1) + ')' : '') + '. Credits are non-refundable: they reduce tax you owe. Donating publicly listed shares directly to a registered charity makes the taxable capital gain zero; selling them first taxes ' + pct(D.tax.capital_gains_inclusion, 0) + ' of the gain at your marginal rate (' + CUR + ' brackets).');
      },
      next: [['/tax/donating-securities/', 'Donating shares to charity'], ['/tax/capital-gains-tax/', 'Capital gains tax']]
    });
  };

  /* ---------- Mortgage prepayment penalty ---------- */
  C.mortgagePenalty = function (bal, rate, months, comp, variable) {
    var three = bal * rate * 3 / 12, ird = Math.max(0, bal * (rate - comp) * months / 12);
    var useIrd = !variable && ird > three;
    return { three: three, ird: ird, penalty: useIrd ? ird : three, method: useIrd ? 'ird' : 'three' };
  };

  W['mortgage-penalty'] = function (el) {
    shell(el, 'mortgage-penalty', {
      title: 'Mortgage penalty calculator',
      intro: 'Estimate the penalty for breaking your mortgage: three months\' interest or the interest rate differential (IRD).',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'bal', 'Mortgage balance', 400000, { min: 0 }) + fNum(p, 'rate', 'Your contract rate (%)', 5, { min: 0, max: 25, step: 0.01 }) +
          fNum(p, 'm', 'Months left in your term', 36, { min: 0, max: 120, step: 1 }) +
          fNum(p, 'comp', 'Comparison rate (%)', 3.5, { min: 0, max: 25, step: 0.01, help: 'The lender\'s current rate for a term matching the time left, minus any discount you received.' }) +
          fRadio(p, 'type', 'Rate type', [['fixed', 'Fixed'], ['variable', 'Variable']], 'fixed') + '</div>';
      },
      calc: function (a) {
        var v = a.val('type') === 'variable', r = C.mortgagePenalty(a.n('bal'), a.n('rate') / 100, a.n('m'), a.n('comp') / 100, v);
        return head('Estimated prepayment penalty', money2(r.penalty)) + kv([['Three months\' interest', money2(r.three)], ['Interest rate differential (IRD)', v ? 'Not usually charged on a variable rate' : money2(r.ird)],
          ['Method used', r.method === 'ird' ? 'Interest rate differential (the greater amount)' : (v ? 'Three months\' interest (variable rate)' : 'Three months\' interest (the greater amount)')]]) +
          how('Three months\' interest = balance x contract rate x 3 / 12. IRD = balance x (contract rate minus comparison rate) x months left in the term / 12, and never below zero. A fixed-rate mortgage is usually charged the greater of the two, and a variable-rate mortgage three months\' interest. Lenders\' exact methods differ, for example in the comparison rate and discount they use, and your lender\'s payout statement governs.');
      },
      next: [['/mortgages/mortgage-renewal-guide/', 'Mortgage renewal guide'], ['/vs/fixed-vs-variable-mortgage/', 'Fixed vs variable mortgage'], ['/calculators/mortgage-payment-calculator/', 'Mortgage payment calculator']]
    });
  };

  /* ---------- EI benefit ---------- */
  C.eiWeekly = function (awie) {
    var E = D.ei, capE = D.payroll.ei.mie / 52, ins = Math.min(Math.max(0, awie), capE), b = ins * E.benefit_rate;
    if (isNum(E.max_weekly)) b = awie >= capE ? E.max_weekly : Math.min(b, E.max_weekly);
    return { insurable: ins, benefit: b, capEarnings: capE };
  };
  C.eiPremium = function (prov, yearly) { var P = D.payroll.ei; return Math.min(Math.max(0, yearly), P.mie) * (prov === 'QC' ? P.rate_qc : P.rate); };

  W['ei-calc'] = function (el) {
    shell(el, 'ei-calc', {
      title: 'EI benefits calculator',
      intro: 'Estimate your weekly Employment Insurance regular benefit, before tax.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) +
          fRadio(p, 'mode', 'Enter your earnings as', [['wk', 'Average weekly earnings'], ['yr', 'Yearly salary']], 'yr') +
          fNum(p, 'wk', 'Average weekly insurable earnings', 1000, { min: 0 }) + fNum(p, 'sal', 'Or yearly salary', MEM.get('income', 52000), { min: 0, help: 'Divided by 52 to get weekly earnings.' }) + '</div>';
      },
      calc: function (a) {
        if (!D.payroll) return msg('warnmsg', 'Payroll figures for ' + CUR + ' are being confirmed.');
        var prov = a.val('prov'), yr = a.val('mode') === 'yr', wk = yr ? a.n('sal') / 52 : a.n('wk'), r = C.eiWeekly(wk), E = D.ei, P = D.payroll.ei, qc = prov === 'QC';
        var prem = C.eiPremium(prov, yr ? a.n('sal') : a.n('wk') * 52);
        return head('Estimated weekly EI benefit, before tax', money2(r.benefit)) +
          kv([['Weekly insurable earnings used', money2(r.insurable)], ['Benefit rate', pct(E.benefit_rate, 0)], ['Maximum weekly benefit for ' + CUR, isNum(E.max_weekly) ? money2(E.max_weekly) : TBD], ['Your yearly EI premiums at these earnings', money2(prem)]]) +
          msg('ok', 'EI benefits are taxable income, so the amount you keep after tax is lower.') +
          how('Weekly benefit = ' + pct(E.benefit_rate, 0) + ' of your average weekly insurable earnings, which count up to the ' + CUR + ' maximum insurable earnings of ' + money(P.mie) + ' a year (' + money2(r.capEarnings) + ' a week).' + (isNum(E.max_weekly) ? ' At or above that weekly amount, the benefit is the published ' + CUR + ' maximum of ' + money(E.max_weekly) + ' a week.' : ' The ' + CUR + ' maximum weekly benefit is being confirmed.') + ' Service Canada works out your average from your best weeks of earnings in the qualifying period, usually the last 52 weeks; how many weeks it uses depends on the unemployment rate where you live.' + (qc ? ' In Quebec, EI premiums are lower (' + pct(P.rate_qc, 2) + ' instead of ' + pct(P.rate, 2) + ') because the Quebec Parental Insurance Plan pays maternity and parental benefits; EI regular benefits are worked out the same way.' : ''));
      },
      next: [['/benefits/ei-payment-dates/', 'EI payment dates'], ['/calculators/take-home-pay-calculator/', 'Take-home pay calculator'], ['/tax/cpp-ei-contributions/', 'CPP and EI contributions']]
    });
  };

  /* ---------- RRSP loan ---------- */
  C.rrspLoan = function (prov, loan, rate, months, income) {
    var n = Math.max(1, Math.round(months)), pay = C.pmt(loan, rate / 12, n), it = pay * n - loan;
    var refund = C.tax(prov, income).total - C.tax(prov, income - loan).total;
    return { payment: pay, n: n, interest: it, refund: refund, own: loan + it - refund, net: refund - it };
  };

  W['rrsp-loan'] = function (el) {
    shell(el, 'rrsp-loan', {
      title: 'RRSP loan calculator',
      intro: 'Compare the interest on a loan to make an RRSP contribution with the tax refund the contribution creates.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'loan', 'Loan amount (your RRSP contribution)', 10000, { min: 0 }) +
          fNum(p, 'rate', 'Loan interest rate (%)', 6, { min: 0, max: 30, step: 0.01 }) + fNum(p, 'm', 'Loan term (months)', 12, { min: 1, max: 120, step: 1 }) +
          fNum(p, 'inc', 'Taxable income before the RRSP deduction', MEM.get('income', 80000), { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'); MEM.set('prov', prov);
        var r = C.rrspLoan(prov, a.n('loan'), a.n('rate') / 100, a.n('m'), a.n('inc'));
        return head(r.net >= 0 ? 'Estimated gain after the refund and interest' : 'Estimated cost after the refund and interest', money(Math.abs(r.net)), r.net < 0) +
          kv([['Monthly loan payment', money2(r.payment)], ['Total interest over ' + r.n + ' months', money2(r.interest)], ['RRSP tax refund (tax saved)', money(r.refund)], ['Your own money after the refund repays the loan', money(r.own)], ['Is the loan interest deductible?', 'No']]) +
          how('Payments are equal monthly amounts over the term at your rate. The refund is the tax saved by deducting the contribution, using ' + CUR + ' brackets, and it arrives only after you file. Net result = refund minus total interest; using the refund to pay down the loan as soon as it arrives lowers the interest further. Interest on money borrowed to contribute to an RRSP is not tax-deductible. Check that you have enough RRSP contribution room first.');
      },
      next: [['/accounts/rrsp-loans/', 'RRSP loans'], ['/calculators/rrsp-calculator/', 'RRSP refund calculator'], ['/accounts/rrsp-contribution-limit/', 'RRSP limit by year']]
    });
  };

  /* ---------- Disability tax credit ---------- */
  C.dtc = function (prov, u18) {
    var X = D.dtc, fl = D.tax.federal.brackets[0][1], pl = (D.tax.provinces[prov] || D.tax.provinces.ON).brackets[0][1], ab = prov === 'QC' ? 1 - D.tax.qc_abatement : 1;
    var fedBase = X.federal * fl * ab, fedSup = u18 ? (isNum(X.federal_supplement) ? X.federal_supplement * fl * ab : null) : 0;
    var pa = (X.provincial || {})[prov], ps = (X.provincial_supplement || {})[prov];
    var provBase = isNum(pa) ? pa * pl : null, provSup = u18 ? (isNum(ps) ? ps * pl : null) : 0;
    var parts = [fedBase, fedSup, provBase, provSup], known = sum(parts.filter(isNum));
    return { fedBase: fedBase, fedSup: fedSup, provBase: provBase, provSup: provSup, fed: fedSup == null ? null : fedBase + fedSup, prov: provBase == null || provSup == null ? null : provBase + provSup,
             total: parts.every(isNum) ? known : null, known: known, fedRate: fl, provRate: pl };
  };

  W['dtc-calc'] = function (el) {
    shell(el, 'dtc-calc', {
      title: 'Disability tax credit calculator',
      intro: 'What the disability tax credit is worth each year in federal and provincial tax savings.',
      fields: function (p) { return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fRadio(p, 'u18', 'Is the person with the disability under 18 at the end of the year?', [['n', 'No'], ['y', 'Yes']], 'n') + '</div>'; },
      calc: function (a) {
        var prov = a.val('prov'), u18 = a.val('u18') === 'y', r = C.dtc(prov, u18), X = D.dtc; MEM.set('prov', prov);
        var h = r.total != null ? head('Yearly value of the disability tax credit', money(r.total)) : head('Federal credit value each year', money(r.fedBase + (r.fedSup || 0)) + (r.fedSup == null ? ' plus the supplement' : ''));
        var items = [['Federal disability amount', money(X.federal)], ['Federal credit (' + pct(r.fedRate, 0) + (prov === 'QC' ? ', less the Quebec abatement' : '') + ')', money(r.fedBase)]];
        if (u18) items.push(['Federal supplement for a person under 18', r.fedSup == null ? TBD : money(r.fedSup)]);
        items.push([D.provName[prov] + ' credit', r.provBase == null ? TBD : money(r.provBase)]);
        if (u18) items.push([D.provName[prov] + ' supplement for a person under 18', r.provSup == null ? TBD : money(r.provSup)]);
        items.push(['Total yearly value', r.total == null ? TBD : money(r.total)]);
        h += kv(items);
        if (r.total == null) h += msg('warnmsg', 'Some ' + CUR + ' amounts are being confirmed, so the total includes only the parts shown.');
        return h + how('Federal value = the ' + CUR + ' disability amount of ' + money(X.federal) + (u18 ? ', plus the supplement for a person under 18,' : '') + ' x ' + pct(r.fedRate, 0) + ', the lowest federal rate.' + (prov === 'QC' ? ' For Quebec residents the federal credit is reduced by the 16.5% Quebec abatement.' : '') + ' Provincial value = the ' + D.provName[prov] + ' disability amount x its lowest rate (' + pct(r.provRate, 2) + '). The credit is non-refundable: it reduces tax owing, and an unused part can be transferred to a spouse, partner or supporting family member. The CRA must approve Form T2201 first.');
      },
      next: [['/benefits/disability-tax-credit/', 'Disability tax credit guide'], ['/accounts/rdsp-grants-bonds/', 'RDSP grants and bonds'], ['/benefits/canada-disability-benefit/', 'Canada Disability Benefit']]
    });
  };

  /* ---------- RDSP grants and bonds ---------- */
  function tiers(t, c) { var lo = 0, g = 0; t.forEach(function (x) { if (c > lo) g += (Math.min(c, lo + x[0]) - lo) * x[1]; lo += x[0]; }); return g; }
  C.rdsp = function (contrib, income, age, gSoFar, bSoFar) {
    var R = D.rdsp, c = Math.max(0, contrib), ok = age <= R.max_age;
    var gLeft = Math.max(0, R.grant_lifetime - (gSoFar || 0)), bLeft = Math.max(0, R.bond_lifetime - (bSoFar || 0));
    var low = ok ? Math.min(tiers(R.grant_low, c), gLeft) : 0, high = ok ? Math.min(tiers(R.grant_high, c), gLeft) : 0;
    var grant = isNum(R.income_threshold) ? (income <= R.income_threshold ? low : high) : (ok ? null : 0);
    var bond = ok ? null : 0;
    if (ok && isNum(R.bond_lower) && isNum(R.bond_upper)) bond = Math.min(bLeft, income <= R.bond_lower ? R.bond_max : (income >= R.bond_upper ? 0 : R.bond_max * (R.bond_upper - income) / (R.bond_upper - R.bond_lower)));
    return { eligible: ok, low: low, high: high, grant: grant, bond: bond, total: grant == null || bond == null ? null : grant + bond, gLeft: gLeft, bLeft: bLeft };
  };

  W['rdsp-grant'] = function (el) {
    var R = D.rdsp;
    shell(el, 'rdsp-grant', {
      title: 'RDSP grant and bond calculator',
      intro: 'The Canada Disability Savings Grant on your contribution and the Canada Disability Savings Bond for this year.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'c', 'Contribution this year', 1500, { min: 0 }) + fNum(p, 'inc', 'Family net income', 80000, { min: 0, help: 'Up to the end of the year the beneficiary turns 18, the parents\' income; after that, the beneficiary\'s and any spouse\'s.' }) +
          fNum(p, 'age', 'Beneficiary\'s age at the end of the year', 30, { min: 0, max: 100, step: 1 }) +
          fNum(p, 'gs', 'Grants received so far (optional)', 0, { min: 0 }) + fNum(p, 'bs', 'Bonds received so far (optional)', 0, { min: 0 }) + '</div>';
      },
      calc: function (a) {
        var r = C.rdsp(a.n('c'), a.n('inc'), a.n('age'), a.n('gs'), a.n('bs'));
        if (!r.eligible) return head('Grants and bonds this year', 'None', true) + msg('warnmsg', 'Grants and bonds are paid until December 31 of the year the beneficiary turns ' + R.max_age + '.');
        var h = r.total != null ? head('Grant and bond this year', money(r.total)) : (r.grant != null ? head('Grant this year', money(r.grant)) : head('Grant on your contribution', money(r.low) + ' or ' + money(r.high)));
        h += kv([['Canada Disability Savings Grant', r.grant != null ? money(r.grant) : money(r.low) + ' if family income is at or below the threshold, ' + money(r.high) + ' if above'],
          ['Canada Disability Savings Bond (no contribution needed)', r.bond == null ? TBD : money(r.bond)], ['Grant room left (lifetime ' + money(R.grant_lifetime) + ')', money(r.gLeft - (r.grant != null ? r.grant : 0))],
          ['Bond room left (lifetime ' + money(R.bond_lifetime) + ')', money(r.bLeft - (r.bond != null ? r.bond : 0))]]);
        if (r.grant == null || r.bond == null) h += msg('warnmsg', 'The ' + CUR + ' family income thresholds are being confirmed, so the grant shows both possible amounts and the bond is not yet worked out.');
        return h + how('Grant: when family income is at or below the threshold, 300% on the first $500 contributed and 200% on the next $1,000 (up to $3,500 a year); above it, 100% on the first $1,000 (up to $1,000). Bond: up to ' + money(R.bond_max) + ' a year with no contribution needed, reduced gradually as income rises between two thresholds. Lifetime limits: ' + money(R.grant_lifetime) + ' of grants and ' + money(R.bond_lifetime) + ' of bonds. Grants and bonds are paid until the end of the year the beneficiary turns ' + R.max_age + ', and unused entitlements can be carried forward up to 10 years.');
      },
      next: [['/accounts/rdsp-grants-bonds/', 'RDSP grants and bonds'], ['/benefits/disability-tax-credit/', 'Disability tax credit']]
    });
  };

  /* ---------- Stock market status (TSX and NYSE) ---------- */
  C.tzParts = function (date, tz) {
    var o = {};
    new Intl.DateTimeFormat('en-US', { timeZone: tz, hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', weekday: 'short' }).formatToParts(date).forEach(function (x) { o[x.type] = x.value; });
    return { y: +o.year, m: +o.month, d: +o.day, h: (+o.hour) % 24, mi: +o.minute, s: +o.second, wd: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(o.weekday) };
  };
  function validIso(s) { if (typeof s !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(s)) return false; var q = s.split('-'), d = new Date(Date.UTC(+q[0], +q[1] - 1, +q[2])); return d.getUTCFullYear() === +q[0] && d.getUTCMonth() === +q[1] - 1 && d.getUTCDate() === +q[2]; }
  function hm(s) { var q = /^(\d{1,2}):(\d{2})$/.exec(String(s || '')); return q && +q[1] < 24 && +q[2] < 60 ? +q[1] * 60 + +q[2] : null; }
  function entry(x, k2) { // 'YYYY-MM-DD', [date, name or close] or {date, name or close}
    var d = typeof x === 'string' ? x : (Array.isArray(x) ? x[0] : (x && x.date)), v = typeof x === 'string' ? '' : (Array.isArray(x) ? x[1] : (x && x[k2]));
    return validIso(d) ? { date: d, v: v == null ? '' : String(v) } : null;
  }
  C.marketState = function (ex, now) {
    var H = ex && ex.hours, tz = (H && H.tz) || 'America/Toronto', o = H && hm(H.open), c = H && hm(H.close);
    if (o == null || c == null || !(now instanceof Date) || !isFinite(now.getTime())) return null;
    var hol = [].concat(ex.holidays_2026 || [], ex.holidays_2027 || []).map(function (x) { return entry(x, 'name'); }).filter(Boolean).sort(function (x, y) { return x.date < y.date ? -1 : 1; });
    var early = (ex.early_closes || []).map(function (x) { return entry(x, 'close'); }).filter(function (x) { return x && hm(x.v) != null; });
    var p = C.tzParts(now, tz), today = p.y + '-' + ('0' + p.m).slice(-2) + '-' + ('0' + p.d).slice(-2), nowMin = p.h * 60 + p.mi + p.s / 60;
    function holiday(d) { return hol.filter(function (x) { return x.date === d; })[0] || null; }
    function closeOn(d) { var e = early.filter(function (x) { return x.date === d; })[0]; return e ? hm(e.v) : c; }
    function trading(d, wd) { return wd >= 1 && wd <= 5 && !holiday(d); }
    function offAt(t) { var x = C.tzParts(new Date(t), tz); return Date.UTC(x.y, x.m - 1, x.d, x.h, x.mi, x.s) - t; }
    function instant(d, min) { var q = d.split('-'), w = Date.UTC(+q[0], +q[1] - 1, +q[2], 0, min); return w - offAt(w - offAt(w)); }
    var open = trading(today, p.wd) && nowMin >= o && nowMin < closeOn(today), nextDay = today, nextMin, k = 0;
    if (open) nextMin = closeOn(today);
    else if (trading(today, p.wd) && nowMin < o) nextMin = o;
    else { for (k = 1; k <= 30; k++) { nextDay = isoAdd(today, k); if (trading(nextDay, (p.wd + k) % 7)) break; } nextMin = o; }
    var upcoming = hol.filter(function (x) { return x.date >= today; });
    return { open: open, today: today, holidayToday: holiday(today), nextDay: nextDay, nextMin: nextMin, mins: Math.max(0, (instant(nextDay, nextMin) - now.getTime()) / 60000),
             earlyToday: closeOn(today) !== c ? closeOn(today) : null, listed: hol.length > 0, nextHoliday: upcoming[0] || null };
  };
  function clock(min) { var h = Math.floor(min / 60), m = min % 60, ap = h < 12 ? 'a.m.' : 'p.m.', h12 = h % 12 || 12; return h12 + ':' + ('0' + m).slice(-2) + ' ' + ap; }
  function span(mins) {
    var t = Math.floor(mins), d = Math.floor(t / 1440), h = Math.floor(t % 1440 / 60), m = t % 60;
    if (t < 1) return 'less than a minute';
    return [d ? d + ' day' + (d === 1 ? '' : 's') : '', h ? h + ' h' : '', m && d === 0 ? m + ' min' : ''].filter(Boolean).join(' ');
  }

  W['market-status'] = function (el) {
    var M = D.markets || {}, EX = [['tsx', 'Toronto Stock Exchange (TSX)'], ['nyse', 'New York Stock Exchange (NYSE)']];
    shell(el, 'market-status', {
      title: 'Is the stock market open right now?',
      intro: 'Live status of the TSX and the NYSE, in Toronto time.',
      button: false,
      fields: function () { return ''; },
      init: function (a) { setInterval(function () { a.form.dispatchEvent(new Event('change')); }, 60000); },
      calc: function () {
        var now = new Date(), rows = [], first = null, list = true;
        EX.forEach(function (x) {
          var ex = M[x[0]], s = ex ? C.marketState(ex, now) : null; if (!s) return;
          if (!first) first = [x, s];
          if (!s.listed) list = false;
          var when = s.open ? 'Closes in ' + span(s.mins) + ' (' + clock(s.nextMin) + ')' : 'Opens in ' + span(s.mins) + ' (' + fmtDate(s.nextDay, { weekday: 'long', month: 'long', day: 'numeric' }) + ', ' + clock(s.nextMin) + ')';
          rows.push([x[1], s.open ? 'Open' : (s.holidayToday ? 'Closed (holiday' + (s.holidayToday.v ? ': ' + esc(s.holidayToday.v) : '') + ')' : 'Closed'), when, clock(hm(ex.hours.open)) + ' to ' + clock(hm(ex.hours.close)) + (s.earlyToday != null ? ' (closes ' + clock(s.earlyToday) + ' today)' : ''),
            s.listed ? (s.nextHoliday ? fmtDate(s.nextHoliday.date, { weekday: 'short', month: 'long', day: 'numeric', year: 'numeric' }) + (s.nextHoliday.v ? ' (' + esc(s.nextHoliday.v) + ')' : '') : 'None listed') : 'Holiday list being confirmed']);
        });
        if (!first) return msg('warnmsg', 'Market hours are being confirmed.');
        var tp = C.tzParts(now, 'America/Toronto');
        return head(first[0][1] + ' right now', first[1].open ? 'Open' : 'Closed', !first[1].open) + '<p class="ws-note">Toronto time: ' + clock(tp.h * 60 + tp.mi) + ', ' + fmtDate(first[1].today, { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' }) + '.</p>' +
          table(['Exchange', 'Status', 'Next change', 'Regular hours (Toronto time)', 'Next holiday'], rows) +
          (list ? '' : msg('warnmsg', 'Holiday list being confirmed, so this check does not yet allow for market holidays or early closes.')) +
          how('Regular trading runs Monday to Friday during the hours shown, in Eastern time, which is the same in Toronto and New York. Markets close on their holidays and close early on some days. The status uses the clock on your device, shown in Toronto time, and refreshes every minute.');
      },
      next: [['/learn/stock-market-hours/', 'Stock market hours'], ['/learn/stock-market-holidays/', 'Stock market holidays']]
    });
  };

  /* ---------- Business chequing cost ---------- */
  C.bizBankCost = function (b, tx, cash, bal, deps) {
    deps = isNum(deps) ? Math.max(0, deps) : 1;
    var fee = isNum(b.waive_balance) && bal >= b.waive_balance ? 0 : (isNum(b.fee) ? b.fee : null), txf = null, cf = null;
    if (tx <= 0 || (isNum(b.included_tx) && tx <= b.included_tx)) txf = 0;
    else if (isNum(b.included_tx) && isNum(b.fee_per_tx)) txf = (tx - b.included_tx) * b.fee_per_tx;
    if (cash <= 0 || (isNum(b.cash_deposit_free) && cash <= b.cash_deposit_free)) cf = 0;
    else if (isNum(b.cash_deposit_free) && isNum(b.cash_fee_per_1000)) cf = (cash - b.cash_deposit_free) * b.cash_fee_per_1000 / 1000 + (isNum(b.cash_fee_per_deposit) ? deps * b.cash_fee_per_deposit : 0);
    var known = (fee || 0) + (txf || 0) + (cf || 0);
    return { fee: fee, tx: txf, cash: cf, known: known, total: fee == null || txf == null || cf == null ? null : known };
  };

  W['biz-bank-cost'] = function (el) {
    shell(el, 'biz-bank-cost', {
      title: 'Business bank account cost calculator',
      intro: 'Your monthly cost at each business chequing plan, based on your transactions, cash deposits and balance.',
      fields: function (p) { return '<div class="ws-w-grid">' + fNum(p, 'tx', 'Transactions a month', 20, { min: 0, step: 1 }) + fNum(p, 'cash', 'Cash deposited a month ($)', 2000, { min: 0 }) + fNum(p, 'deps', 'Cash deposits a month', 2, { min: 0, step: 1 }) + fNum(p, 'bal', 'Average monthly balance', 10000, { min: 0 }) + '</div>'; },
      calc: function (a) {
        var L = D.business_chequing || [];
        if (!L.length) return msg('warnmsg', 'Business account data being confirmed.');
        var rows = L.map(function (b) { return { b: b, c: C.bizBankCost(b, a.n('tx'), a.n('cash'), a.n('bal'), a.n('deps')) }; }).sort(function (x, y) {
          var cx = x.c.total != null, cy = y.c.total != null; if (cx !== cy) return cx ? -1 : 1; return x.c.known - y.c.known; });
        var NP = '<span class="ws-note">Not published</span>', mv = function (v) { return v == null ? NP : money2(v); };
        var best = rows[0].c.total != null ? head('Lowest estimated monthly cost', money2(rows[0].c.total) + ' at ' + esc(rows[0].b.name)) : msg('warnmsg', 'None of the plans publishes every fee that applies to these inputs.');
        return best +
          table(['Rank', 'Account', 'Monthly fee', 'Transaction fees', 'Cash deposit fees', 'Total a month', 'Total a year'], rows.map(function (r, i) {
            var nm = esc(r.b.name) + (r.b.bank ? ' <span class="ws-note">' + esc(r.b.bank) + '</span>' : '');
            return [i + 1, r.b.link ? '<a href="' + esc(r.b.link) + '">' + nm + '</a>' : nm, mv(r.c.fee), mv(r.c.tx), mv(r.c.cash), r.c.total != null ? '<b>' + money2(r.c.total) + '</b>' : 'At least ' + money2(r.c.known), r.c.total != null ? money2(r.c.total * 12) : 'At least ' + money2(r.c.known * 12)];
          })) + how('The monthly fee is waived where your balance meets the plan\'s published minimum. Transaction fees apply to transactions above the number included, and cash deposit fees to cash above the free amount, per $1,000, plus any fee the bank charges for each cash deposit (Desjardins: $0.95 at an ATM plus $0.25 per deposit item, used here as the lowest cost; a teller deposit costs more). Where a bank does not publish a fee that applies to your inputs, the table shows Not published, the total is shown as a minimum, and the plan is listed after plans with complete figures. Other fees, such as for e-Transfers and cheques, vary by plan; see each account\'s details.');
      },
      next: [['/business-owners/best-business-chequing-accounts/', 'Best business chequing accounts'], ['/business-owners/', 'Banking for business owners']]
    });
  };

  /* ---------- Small business deduction: passive income grind ---------- */
  C.sbdGrind = function (active, aaii, prov) {
    var R = D.corp_rates, lim = Math.max(0, R.business_limit - R.grind_rate * Math.max(0, aaii - R.aaii_threshold)), act = Math.max(0, active);
    var shifted = Math.max(0, Math.min(act, R.business_limit) - Math.min(act, lim)), fed = shifted * (R.federal_general - R.federal_small);
    var P = (R.provinces || {})[prov] || {}, pv = null;
    if (P.parallels_grind === false) pv = 0;
    else if (P.parallels_grind === true && isNum(P.small) && isNum(P.general)) pv = shifted * (P.general - P.small);
    return { limit: lim, shifted: shifted, fed: fed, prov: pv, total: pv == null ? null : fed + pv };
  };

  W['sbd-grind'] = function (el) {
    var R = D.corp_rates;
    shell(el, 'sbd-grind', {
      title: 'Passive income and the small business deduction',
      intro: 'See how investment income inside your corporation shrinks the small business limit and how much extra corporate tax that costs.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'act', 'Active business income this year', 600000, { min: 0 }) +
          fNum(p, 'aaii', 'Adjusted aggregate investment income (AAII) last year', 80000, { min: 0, help: 'Passive income such as interest, rent, dividends from portfolio shares and the taxable part of capital gains.' }) + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), r = C.sbdGrind(a.n('act'), a.n('aaii'), prov); MEM.set('prov', prov);
        var h = r.total != null ? head('Extra corporate tax from the reduced limit', money(r.total)) : head('Extra federal corporate tax from the reduced limit', money(r.fed));
        h += kv([['Small business limit after the reduction', money(r.limit)], ['Active income taxed at the general rate instead', money(r.shifted)],
          ['Extra federal tax (' + pct(R.federal_general, 0) + ' minus ' + pct(R.federal_small, 0) + ')', money(r.fed)], ['Extra ' + D.provName[prov] + ' tax', r.prov == null ? TBD : money(r.prov)], ['Total extra tax', r.total == null ? TBD : money(r.total)]]);
        if (r.prov == null) h += msg('warnmsg', D.provName[prov] + '\'s corporate rates, and whether it follows the federal reduction, are being confirmed, so the result shows federal tax only.');
        return h + how('The ' + money(R.business_limit) + ' small business limit falls by $' + R.grind_rate + ' for every $1 of adjusted aggregate investment income above ' + money(R.aaii_threshold) + ' in the previous year, reaching zero at ' + money(R.aaii_threshold + R.business_limit / R.grind_rate) + '. Active business income above the reduced limit is taxed at the general rate instead of the small business rate. Federal rates used: ' + pct(R.federal_small, 0) + ' small business and ' + pct(R.federal_general, 0) + ' general. The limit is shared by associated corporations and can also be reduced when taxable capital is over $10 million, which this does not include.');
      },
      next: [['/business-owners/corporate-cash/', 'Where to keep corporate cash'], ['/business-owners/', 'Banking and investing for business owners']]
    });
  };

  /* =====================================================================
   * 4d. WIDGETS ADDED FOR PAGES 297 TO 393 (October 28, 2026, v1.4)
   * A figure the research registers have not confirmed is null in the data; the widgets show TBD or Not published for it.
   * Every C.* helper below is mirrored in qa/wscalc.py and cross-checked.
   * ===================================================================== */
  var NOTPUB = '<span class="ws-note">Not published</span>';
  function pctTrim(x) { return rnd(x * 100, 3).toLocaleString('en-CA', { maximumFractionDigits: 3 }) + '%'; }
  function signed2(x) { return (rnd(x, 2) > 0 ? '+' : '') + money2(x); }

  /* ---------- Credit card rewards (data-list="cash-back", "no-fee", "travel", "low-interest", "secured", "student", "business" or "all") ---------- */
  var CC_CATS = [['grocery', 'Groceries'], ['gas', 'Gas'], ['dining', 'Dining'], ['transit', 'Transit'], ['recurring', 'Recurring bills'], ['travel', 'Travel'], ['other', 'Everything else']];
  var CC_LISTS = ['cash-back', 'no-fee', 'travel', 'low-interest', 'secured', 'student', 'business'];   // 'business' added in v1.5: cards tagged business
  // card: {earn: {grocery, gas, dining, transit, recurring, travel, other} (decimal cash-equivalent, null = not published), annual_fee, first_year_fee,
  // caps_struct: [{categories, annual_spend_limit, rate_after}]}. monthly: {category: $ a month}. A category is capped by the first group that lists it;
  // a group's yearly limit is shared in proportion to the spending in its categories, and spending above it earns rate_after.
  // A rate or limit needed for spending you enter that is null makes that category null (rewards then a minimum). firstYear: use first_year_fee when published.
  C.ccRewards = function (card, monthly, firstYear) {
    var E = card.earn || {}, spend = {}, by = {}, done = {}, missing = [], known = 0;
    CC_CATS.forEach(function (x) { spend[x[0]] = Math.max(0, (monthly && monthly[x[0]]) || 0) * 12; });
    (card.caps_struct || []).forEach(function (g) {
      var cats = [], S = 0, L = g.annual_spend_limit, ra = g.rate_after;
      (g.categories || []).forEach(function (c) { if (spend.hasOwnProperty(c) && !done[c]) { done[c] = true; cats.push(c); S += spend[c]; } });
      cats.forEach(function (c) {
        var s = spend[c], e = E[c];
        if (!(s > 0)) by[c] = 0;
        else if (!isNum(e) || !isNum(L)) by[c] = null;
        else if (S <= L) by[c] = s * e;
        else by[c] = isNum(ra) ? s * L / S * e + (s - s * L / S) * ra : null;
      });
    });
    CC_CATS.forEach(function (x) { var c = x[0], s = spend[c]; if (!done[c]) by[c] = !(s > 0) ? 0 : (isNum(E[c]) ? s * E[c] : null); });
    CC_CATS.forEach(function (x) { if (by[x[0]] == null) missing.push(x[0]); else known += by[x[0]]; });
    var fee = firstYear && isNum(card.first_year_fee) ? card.first_year_fee : (isNum(card.annual_fee) ? card.annual_fee : null), rewards = missing.length ? null : known;
    return { by: by, rewards: rewards, known: known, fee: fee, net: rewards == null || fee == null ? null : rewards - fee, netKnown: known - (fee || 0), missing: missing };
  };
  // Cards on the list (every personal card for "all" or no list), complete figures first by net value, then the rest by their known net value.
  // v1.5: cards tagged "business" appear only on the "business" list, so the personal lists and "all" stay as they were.
  C.ccRank = function (cards, monthly, firstYear, list) {
    var biz = function (c) { return (c.tags || []).indexOf('business') >= 0; };
    var use = list === 'business' ? cards.filter(biz) : cards.filter(function (c) { return !biz(c) && (CC_LISTS.indexOf(list) < 0 || (c.tags || []).indexOf(list) >= 0); });
    return use.map(function (c) { return { card: c, r: C.ccRewards(c, monthly, firstYear) }; }).sort(function (x, y) {
      var cx = x.r.net != null, cy = y.r.net != null; if (cx !== cy) return cx ? -1 : 1; return cx ? y.r.net - x.r.net : y.r.netKnown - x.r.netKnown; });
  };

  W['cc-rewards'] = function (el) {
    var list = el.getAttribute('data-list') || 'all', LB = { 'cash-back': 'cash back', 'no-fee': 'no-fee', travel: 'travel', 'low-interest': 'low-interest', secured: 'secured', student: 'student', business: 'business' };
    var DEF = { grocery: 600, gas: 200, dining: 250, transit: 100, recurring: 150, travel: 150, other: 700 }, lab = {};
    CC_CATS.forEach(function (x) { lab[x[0]] = x[1].toLowerCase(); });
    shell(el, 'cc-rewards', {
      title: 'Credit card rewards calculator',
      intro: 'Your yearly rewards at each ' + (LB[list] ? LB[list] + ' ' : '') + 'card for your own spending, minus the annual fee.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + CC_CATS.map(function (x) { return fNum(p, 's_' + x[0], x[1] + ' (per month)', DEF[x[0]], { min: 0 }); }).join('') +
          fRadio(p, 'fy', 'Count the first-year fee instead of the annual fee?', [['n', 'No'], ['y', 'Yes']], 'n') + '</div>';
      },
      calc: function (a) {
        var L = D.credit_cards || [];
        if (!L.length) return msg('warnmsg', 'Credit card data being confirmed.');
        var m = {}, fy = a.val('fy') === 'y', yr = 0;
        CC_CATS.forEach(function (x) { m[x[0]] = a.n('s_' + x[0]); yr += Math.max(0, m[x[0]]) * 12; });
        var rows = C.ccRank(L, m, fy, list);
        if (!rows.length) return msg('warnmsg', list === 'business' ? 'Business credit card data being confirmed.' : 'Card data for this list being confirmed.');
        var top = rows[0].r.net != null ? head('Highest estimated net value a year', money(rows[0].r.net) + ' at ' + esc(rows[0].card.name), rows[0].r.net < 0) : msg('warnmsg', 'None of these cards publishes every earn rate and fee needed for your spending.');
        return top + kv([['Your yearly card spending', money(yr)], ['Cards compared', String(rows.length)]]) +
          table(['Rank', 'Card', 'Rewards a year', fy ? 'First-year fee' : 'Annual fee', 'Net value a year'], rows.map(function (x, i) {
            var c = x.card, r = x.r, nm = esc(c.name) + (c.issuer ? ' <span class="ws-note">' + esc(c.issuer) + '</span>' : '');
            var nm2 = r.missing.length === CC_CATS.length ? 'earn rates' : r.missing.map(function (k) { return lab[k]; }).join(', ') + (r.missing.length > 1 ? ' rates' : ' rate');
            var rew = r.rewards != null ? money(r.rewards) : 'At least ' + money(r.known) + ' <span class="ws-note">(' + nm2 + ' not published)</span>';
            return [i + 1, c.link && String(c.link).charAt(0) === '/' ? '<a href="' + esc(c.link) + '">' + nm + '</a>' : nm, rew, r.fee == null ? NOTPUB : money(r.fee),
              r.fee == null ? NOTPUB : (r.net != null ? '<b>' + money(r.net) + '</b>' : 'At least ' + money(r.netKnown))];
          }), 'Ranked by net value for your spending') +
          how('Rewards = your yearly spending in each category x the card\'s earn rate for it. Earn rates are cash-equivalent: for a points card, the value of the points earned per dollar, as listed in our card data. Where a card caps a higher rate, spending above the yearly cap earns the rate that applies after it; when one cap covers several categories, it is shared in proportion to your spending in each. Net value = rewards minus the annual fee' + (fy ? ', or the first-year fee where a card publishes a different one (otherwise the annual fee)' : '') + '. Where an earn rate or fee you need is not published, the table shows Not published or a minimum, and the card is listed after cards with complete figures. Welcome offers, interest and other fees are not included.');
      },
      next: [['/credit-cards/', 'Compare credit cards'], ['/credit-cards/best-cash-back-credit-cards/', 'Best cash back credit cards'], ['/calculators/credit-card-payoff-calculator/', 'Credit card payoff calculator']]
    });
  };

  /* ---------- Credit card payoff ---------- */
  // Monthly compounding at apr / 12: each month the interest is added, then the payment is made (the last payment clears the balance).
  // mode 'fixed': x = monthly payment; 'months': x = months (level payment from C.pmt); 'min': x = minimum payment share of the balance after
  // that month's interest (decimal), floor = minimum payment in dollars. never: a payment does not reduce the balance. Capped at 1,200 months.
  C.ccPayoff = function (bal, apr, mode, x, floor) {
    var i = apr / 12, b = Math.max(0, bal), pay = mode === 'months' ? C.pmt(b, i, Math.max(1, Math.round(x))) : Math.max(0, x);
    var m = 0, tInt = 0, tPaid = 0, rows = [], never = false, first = null;
    while (b > 0.005 && m < 1200) {
      var it = b * i, s = b + it, p = Math.min(s, mode === 'min' ? Math.max(floor || 0, x * s) : pay);
      if (first == null) first = p;
      if (s - p >= b) { never = true; break; }
      m++; tInt += it; tPaid += p; b = s - p;
      if (m <= 12) rows.push([m, p, it, p - it, b]);
    }
    var done = !never && b <= 0.005;
    return { payment: mode === 'min' ? first : pay, months: done ? m : null, never: never, interest: done ? tInt : null, paid: done ? tPaid : null, firstInterest: Math.max(0, bal) * i, rows: rows };
  };

  W['cc-payoff'] = function (el) {
    shell(el, 'cc-payoff', {
      title: 'Credit card payoff calculator',
      intro: 'How long it takes to pay off a card balance, and the interest it costs, with a fixed payment, a target date or minimum payments.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'bal', 'Card balance', 5000, { min: 0 }) +
          fNum(p, 'apr', 'Interest rate (% a year)', 19.99, { min: 0, max: 60, step: 0.01, help: 'Example rate. Use the rate on your statement.' }) +
          fRadio(p, 'mode', 'How you will pay it off', [['fixed', 'A fixed monthly payment'], ['months', 'In a set number of months'], ['min', 'Minimum payments only']], 'fixed') +
          fNum(p, 'pay', 'Monthly payment ($)', 250, { min: 0 }) + fNum(p, 'n', 'Or months to pay it off', 24, { min: 1, max: 600, step: 1 }) +
          fNum(p, 'minp', 'Minimum payment (% of the balance)', 3, { min: 0, max: 100, step: 0.1, help: 'Example only. Your statement shows your card\'s minimum payment formula.' }) +
          fNum(p, 'minf', 'Minimum payment floor ($)', 10, { min: 0, help: 'Example only: the minimum payment is never less than this, unless the balance is smaller.' }) + '</div>';
      },
      calc: function (a) {
        var mode = a.val('mode'), bal = a.n('bal'), apr = a.n('apr') / 100;
        if (bal <= 0) return msg('warnmsg', 'Please enter your card balance.');
        if (mode === 'months' && !(a.n('n') >= 1)) return msg('warnmsg', 'Please enter at least 1 month.');
        var r = C.ccPayoff(bal, apr, mode, mode === 'fixed' ? a.n('pay') : (mode === 'months' ? a.n('n') : a.n('minp') / 100), a.n('minf'));
        var hw = how('Interest is charged each month at your yearly rate divided by 12 (monthly compounding at APR / 12) on the balance at the start of the month, and the payment is made at the end of the month. ' +
          (mode === 'fixed' ? 'You pay the same amount every month until the balance is paid; the last payment is smaller.' : (mode === 'months' ? 'The payment is the level monthly amount that clears the balance in the months you choose.' :
          'Each minimum payment is the percentage you enter of the balance after that month\'s interest, or the floor amount if that is more, so the payments shrink as the balance falls. The defaults are examples only; your card\'s formula is on your statement.')) +
          ' Most card issuers work out interest daily, so your statements can differ slightly. Assumes no new purchases, fees or rate changes, and every payment made on time.');
        if (r.never) return head('Paid off in', 'Never at this payment', true) + msg('warnmsg', 'The ' + (mode === 'min' ? 'first minimum payment' : 'payment') + ' of ' + money2(r.payment) + ' does not cover the ' + money2(r.firstInterest) + ' of interest charged in the first month, so the balance never goes down.') + hw;
        var rows = r.rows.map(function (x) { return [x[0], money2(x[1]), money2(x[2]), money2(x[3]), money2(x[4])]; });
        if (r.months != null) rows.push(['<b>Total, ' + r.months + ' month' + (r.months === 1 ? '' : 's') + '</b>', '<b>' + money2(r.paid) + '</b>', '<b>' + money2(r.interest) + '</b>', '<b>' + money2(r.paid - r.interest) + '</b>', '<b>' + money2(0) + '</b>']);
        return head('Paid off in', r.months == null ? 'More than 100 years' : ym(r.months), r.months == null) +
          kv([[mode === 'min' ? 'First minimum payment' : 'Monthly payment', money2(r.payment)], ['Total interest', r.interest == null ? '—' : money2(r.interest)], ['Total paid', r.paid == null ? '—' : money2(r.paid)], ['Interest in the first month', money2(r.firstInterest)]]) +
          table(['Month', 'Payment', 'Interest', 'Principal', 'Balance after'], rows, 'First 12 months' + (r.months != null ? ' and totals' : '')) + hw;
      },
      next: [['/credit-cards/best-low-interest-credit-cards/', 'Best low-interest credit cards'], ['/credit-cards/credit-score/', 'Credit scores in Canada'], ['/calculators/emergency-fund-calculator/', 'Emergency fund calculator']]
    });
  };

  /* ---------- Sales tax (GST, HST, PST, QST) ---------- */
  // D.sales_tax[prov] = {gst, hst, pst, label} as decimals, null until verified. An HST province uses hst alone; elsewhere gst + pst (pst 0 where none).
  C.salesTax = function (prov, amount, remove) {
    var R = (D.sales_tax || {})[prov] || {}, h = isNum(R.hst) && R.hst > 0, rate = h ? R.hst : (isNum(R.gst) && isNum(R.pst) ? R.gst + R.pst : null);
    if (rate == null) return { ok: false, rate: null, kind: null, pre: null, gst: null, pst: null, hst: null, tax: null, total: null };
    var pre = remove ? amount / (1 + rate) : amount, g = h ? 0 : pre * R.gst, ps = h ? 0 : pre * R.pst, hs = h ? pre * R.hst : 0, tax = h ? hs : g + ps;
    return { ok: true, rate: rate, kind: h ? 'hst' : 'gst_pst', pre: pre, gst: g, pst: ps, hst: hs, tax: tax, total: pre + tax };
  };

  W['sales-tax'] = function (el) {
    shell(el, 'sales-tax', {
      title: 'Sales tax calculator',
      intro: 'Add GST, HST, PST or QST to a price, or take it out of a total, for any province or territory.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'prov', 'Province or territory', provOpts(), provDefault()) + fNum(p, 'amt', 'Amount ($)', 100, { min: 0 }) +
          fRadio(p, 'mode', 'What do you want to do?', [['add', 'Add tax to a price'], ['remove', 'Take tax out of a total']], 'add') + '</div>';
      },
      calc: function (a) {
        var prov = a.val('prov'), rem = a.val('mode') === 'remove', R = (D.sales_tax || {})[prov] || {}, r = C.salesTax(prov, a.n('amt'), rem); MEM.set('prov', prov);
        if (!r.ok) return msg('warnmsg', D.provName[prov] + ' sales tax rates are being confirmed.');
        var items = [];
        if (r.kind === 'hst') items.push(['HST (' + pctTrim(R.hst) + ')', money2(r.hst)]);
        else { items.push(['GST (' + pctTrim(R.gst) + ')', money2(r.gst)]); if (R.pst > 0) items.push([esc(R.label || 'PST') + ' (' + pctTrim(R.pst) + ')', money2(r.pst)]); }
        items.push(['Total tax (' + pctTrim(r.rate) + ')', money2(r.tax)], ['Price before tax', money2(r.pre)], ['Total with tax', money2(r.total)]);
        return head(rem ? 'Price before tax' : 'Total with tax', money2(rem ? r.pre : r.total)) + kv(items) +
          how('In provinces with the harmonized sales tax (HST), one combined rate covers federal and provincial tax. Elsewhere, the GST and any provincial sales tax are each worked out on the price before tax. Taking tax out of a total: price before tax = total / (1 + the combined rate). Some goods and services are zero-rated or exempt, and some provinces tax certain items at other rates. Each tax is shown to the cent; sellers round each tax on a receipt, so totals can differ by a cent.');
      },
      next: [['/benefits/gst-hst-credit/', 'GST/HST credit'], ['/calculators/income-tax-calculator/', 'Income tax calculator']]
    });
  };

  /* ---------- Inflation (Consumer Price Index) ---------- */
  // D.cpi = {annual: {'YYYY': index}, monthly: {'YYYY-MM': index}, latest_month: 'YYYY-MM'}. from / to: years, or 'YYYY-MM' when monthly.
  function monthIdx(k) { var q = String(k).split('-'); return +q[0] * 12 + (+q[1] - 1); }
  C.inflation = function (amount, from, to, monthly) {
    var S = (D.cpi || {})[monthly ? 'monthly' : 'annual'] || {}, i0 = S[from], i1 = S[to], miss = [];
    if (!(isNum(i0) && i0 > 0)) miss.push(String(from));
    if (!(isNum(i1) && i1 > 0) && miss.indexOf(String(to)) < 0) miss.push(String(to));
    var yrs = monthly ? (monthIdx(to) - monthIdx(from)) / 12 : to - from;
    if (miss.length) return { ok: false, missing: miss, i0: null, i1: null, value: null, cum: null, avg: null, years: yrs };
    var f = i1 / i0;
    return { ok: true, missing: miss, i0: i0, i1: i1, value: amount * f, cum: f - 1, avg: yrs !== 0 ? Math.pow(f, 1 / yrs) - 1 : null, years: yrs };
  };

  W['inflation'] = function (el) {
    var P = D.cpi || {}, yrs = Object.keys(P.annual || {}).map(Number).filter(isFinite).sort(function (x, y) { return x - y; });
    var lm = /^\d{4}-\d{2}$/.test(String(P.latest_month || '')) ? P.latest_month : null, MON = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    var mopts = MON.map(function (x, k) { return [String(k + 1), x]; });
    shell(el, 'inflation', {
      title: 'Inflation calculator',
      intro: 'What an amount from one year (or month) is worth in another, using Canada\'s Consumer Price Index.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'amt', 'Amount ($)', 100, { min: 0 }) +
          fRadio(p, 'mode', 'Compare', [['yr', 'Yearly averages'], ['mo', 'Specific months']], 'yr') +
          fNum(p, 'y0', 'From year', 2000, { min: 1914, max: CUR, step: 1 }) + fSel(p, 'm0', 'From month (specific months)', mopts, '1') +
          fNum(p, 'y1', 'To year', yrs.length ? yrs[yrs.length - 1] : CUR - 1, { min: 1914, max: CUR, step: 1 }) + fSel(p, 'm1', 'To month (specific months)', mopts, lm ? String(+lm.slice(5)) : '1') + '</div>';
      },
      calc: function (a) {
        var mo = a.val('mode') === 'mo', y0 = Math.round(a.n('y0')), y1 = Math.round(a.n('y1')), amt = a.n('amt');
        var k0 = mo ? y0 + '-' + ('0' + a.val('m0')).slice(-2) : y0, k1 = mo ? y1 + '-' + ('0' + a.val('m1')).slice(-2) : y1;
        var lab = function (k) { return mo ? fmtDate(k + '-01', { year: 'numeric', month: 'long' }) : String(k); }, r = C.inflation(amt, k0, k1, mo);
        var hw = how('Equivalent value = amount x (CPI in the later period / CPI in the earlier period). Yearly averages use the average CPI for each calendar year; specific months use the CPI for each month. Average yearly inflation = (later CPI / earlier CPI)^(1 / years) − 1. The CPI is Statistics Canada\'s all-items Consumer Price Index for Canada; your own costs can rise faster or slower than the average basket.' + (lm ? ' Latest month available: ' + fmtDate(lm + '-01', { year: 'numeric', month: 'long' }) + '.' : ''));
        if (!r.ok) return msg('warnmsg', 'Consumer Price Index figures for ' + r.missing.map(lab).join(' and ') + ' are being confirmed.') + hw;
        return head(money2(amt) + ' in ' + lab(k0) + ' is worth', money2(r.value) + ' in ' + lab(k1)) +
          kv([['Cumulative inflation', pct(r.cum, 1)], ['Average yearly inflation', r.avg == null ? '—' : pct(r.avg, 2)], ['Consumer Price Index', nf(r.i0, 1) + ' to ' + nf(r.i1, 1)]]) + hw;
      },
      next: [['/calculators/compound-interest-calculator/', 'Compound interest calculator'], ['/calculators/rule-of-72-calculator/', 'Rule of 72 calculator']]
    });
  };

  /* ---------- Hourly to salary ---------- */
  // unit: hour, year, month, biweek (every two weeks) or week. Yearly = hourly x hours x paid weeks; monthly x 12; a two-week amount / 2 x paid weeks; weekly x paid weeks.
  C.hourlySalary = function (amount, unit, hours, weeks) {
    var y = unit === 'hour' ? amount * hours * weeks : (unit === 'year' ? amount : (unit === 'month' ? amount * 12 : (unit === 'biweek' ? amount / 2 * weeks : amount * weeks)));
    return { yearly: y, monthly: y / 12, semimonthly: y / 24, biweekly: weeks > 0 ? y / weeks * 2 : null, weekly: weeks > 0 ? y / weeks : null, hourly: hours > 0 && weeks > 0 ? y / (hours * weeks) : null };
  };

  W['hourly-salary'] = function (el) {
    shell(el, 'hourly-salary', {
      title: 'Hourly to salary calculator',
      intro: 'Turn an hourly wage into a yearly salary, or any pay amount into every other pay period.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'unit', 'I am entering my pay', [['hour', 'Per hour'], ['year', 'Per year'], ['month', 'Per month'], ['biweek', 'Every two weeks'], ['week', 'Per week']], 'hour') +
          fNum(p, 'amt', 'Pay before deductions ($)', 25, { min: 0 }) + fNum(p, 'hrs', 'Hours a week', 40, { min: 0, max: 168 }) +
          fNum(p, 'wks', 'Paid weeks a year', 52, { min: 0, max: 52, help: 'Use 52 if you are paid for vacation and holidays.' }) + '</div>';
      },
      calc: function (a) {
        if (!(a.n('hrs') > 0) || !(a.n('wks') > 0)) return msg('warnmsg', 'Please enter hours a week and paid weeks a year above 0.');
        var u = a.val('unit'), r = C.hourlySalary(a.n('amt'), u, a.n('hrs'), a.n('wks'));
        MEM.set('income', rnd(r.yearly, 0));
        return head(u === 'hour' ? 'Yearly salary' : 'Hourly rate', u === 'hour' ? money(r.yearly) : money2(r.hourly)) +
          table(['Pay period', 'Before deductions'], [['Hourly', money2(r.hourly)], ['Weekly', money2(r.weekly)], ['Every two weeks', money2(r.biweekly)], ['Twice a month', money2(r.semimonthly)], ['Monthly', money2(r.monthly)], ['Yearly', money2(r.yearly)]], 'Your pay in every period') +
          how('Yearly pay = hourly rate x hours a week x paid weeks a year. Weekly = yearly / paid weeks, every two weeks = two weekly amounts, twice a month = yearly / 24 and monthly = yearly / 12. A monthly amount is taken as paid 12 times a year. These are amounts before tax, CPP or QPP, EI and other deductions; the take-home pay calculator works out what you keep.');
      },
      next: [['/calculators/take-home-pay-calculator/', 'Take-home pay calculator'], ['/calculators/income-tax-calculator/', 'Income tax calculator']]
    });
  };

  /* ---------- Stock average ---------- */
  // rows: [{shares, price, fee}] (rows without shares are skipped). Shares to buy at the current price to bring the average price
  // (without commissions) to the target: shares x (average - target) / (target - current), possible only when current < target < average.
  C.stockAverage = function (rows, cur, target) {
    var sh = 0, cost = 0, fees = 0;
    rows.forEach(function (r) { if (r.shares > 0) { sh += r.shares; cost += r.shares * r.price; fees += r.fee || 0; } });
    var avg = sh > 0 ? cost / sh : null, ok = null, need = null;
    if (avg != null && isNum(cur) && isNum(target)) { ok = target > cur && target < avg; if (ok) need = sh * (avg - target) / (target - cur); }
    return { shares: sh, cost: cost, fees: fees, avg: avg, avgFees: sh > 0 ? (cost + fees) / sh : null, possible: ok, need: need, needCost: need == null ? null : need * cur, newShares: need == null ? null : sh + need };
  };

  W['stock-average'] = function (el) {
    var SAMPLE = [[100, 50, 0], [50, 44, 0]], P = '', count = 0;
    function row(r) {
      var i = count++;
      return '<div class="ws-w-grid ws-sa-row" data-row="' + i + '" style="border-top:1px solid var(--ws-step1);padding-top:10px;margin-top:10px">' +
        fNum(P, 'q' + i, 'Shares bought', r[0], { min: 0 }) + fNum(P, 'pr' + i, 'Price per share ($)', r[1], { min: 0 }) + fNum(P, 'c' + i, 'Commission ($)', r[2], { min: 0 }) +
        '<div class="ws-field"><span class="ws-flabel">Purchase ' + (i + 1) + '</span><button type="button" class="ws-w-btn ws-secondary" data-rm="1">Remove</button></div></div>';
    }
    function sample() { count = 0; return SAMPLE.map(row).join(''); }
    shell(el, 'stock-average', {
      title: 'Stock average calculator',
      intro: 'Your average price per share across several purchases, with and without commissions, and how many shares to buy to bring it down to a target.',
      fields: function (p) {
        P = p;
        return '<div class="ws-sa-rows">' + sample() + '</div><div class="ws-w-actions"><button type="button" class="ws-w-btn ws-secondary" data-add="1">Add a purchase</button></div>' +
          '<div class="ws-w-grid" style="margin-top:10px">' + fNum(p, 'cur', 'Current share price ($, optional)', 40, { min: 0 }) + fNum(p, 'tgt', 'Target average price ($, optional)', 45, { min: 0 }) + '</div>';
      },
      init: function (a) {
        var box = a.form.querySelector('.ws-sa-rows');
        a.form.addEventListener('click', function (e) {
          var t = e.target;
          if (t.getAttribute('data-add')) { box.insertAdjacentHTML('beforeend', row(['', '', ''])); a.form.dispatchEvent(new Event('change')); }
          else if (t.getAttribute('data-rm')) { var r = t.closest('.ws-sa-row'); if (r) r.parentNode.removeChild(r); a.form.dispatchEvent(new Event('change')); }
        });
        a.form.addEventListener('reset', function () { setTimeout(function () { box.innerHTML = sample(); }, 0); });
      },
      calc: function (a) {
        var rows = [];
        Array.prototype.forEach.call(a.form.querySelectorAll('.ws-sa-row'), function (e) {
          var i = e.getAttribute('data-row'); rows.push({ shares: Math.max(0, a.n('q' + i)), price: Math.max(0, a.n('pr' + i)), fee: Math.max(0, a.n('c' + i)) });
        });
        var cur = a.val('cur') === '' ? null : a.n('cur'), tgt = a.val('tgt') === '' ? null : a.n('tgt'), r = C.stockAverage(rows, cur, tgt);
        if (!(r.shares > 0)) return msg('warnmsg', 'Please enter at least one purchase with a number of shares.');
        var h = head('Average price per share', money2(r.avg)) + kv([['Shares held', shares(r.shares)], ['Total cost, without commissions', money2(r.cost)], ['Commissions', money2(r.fees)], ['Average cost per share, with commissions', money2(r.avgFees)]]);
        if (r.possible === true) h += kv([['Shares to buy at ' + money2(cur) + ' to average ' + money2(tgt), shares(r.need)], ['Cost of that purchase', money2(r.needCost)], ['Shares you would then hold', shares(r.newShares)]]);
        else if (r.possible === false) h += msg('warnmsg', 'Not possible: buying at the current price can only bring your average to a target above the current price (' + money2(cur) + ') and below your average now (' + money2(r.avg) + ').');
        return h + how('Average price = the total paid for the shares (shares x price for each purchase) / shares held. With commissions, the commissions are added to the cost, which is your adjusted cost base if these are all your purchases and you have not sold any. Shares to buy = shares held x (average now − target) / (target − current price), using the average without commissions and leaving out the commission on the new purchase. Fractional results are shown; round up if your broker trades whole shares only.');
      },
      next: [['/calculators/acb-calculator/', 'ACB calculator'], ['/learn/how-to-buy-stocks/', 'How to buy stocks in Canada']]
    });
  };

  /* ---------- ROI and annualized return ---------- */
  C.roi = function (inv, fin, inc, years) {
    var tot = fin + (inc || 0), gain = tot - inv;
    return { total: tot, gain: gain, roi: inv > 0 ? gain / inv : null, cagr: inv > 0 && years > 0 && tot >= 0 ? Math.pow(tot / inv, 1 / years) - 1 : null, years: years };
  };
  C.yearsBetween = function (a, b) {   // days between two YYYY-MM-DD dates / 365.25 (null for an invalid date)
    if (!validIso(a) || !validIso(b)) return null;
    var p = a.split('-'), q = b.split('-');
    return (Date.UTC(+q[0], +q[1] - 1, +q[2]) - Date.UTC(+p[0], +p[1] - 1, +p[2])) / 86400000 / 365.25;
  };

  W['roi'] = function (el) {
    shell(el, 'roi', {
      title: 'ROI calculator',
      intro: 'Your total return on investment and the annualized return (CAGR) for any holding period.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'inv', 'Amount invested', 10000, { min: 0 }) + fNum(p, 'fin', 'Value now or when sold', 15000, { min: 0 }) +
          fNum(p, 'inc', 'Income received along the way (optional)', 0, { min: 0, help: 'Dividends, interest or rent you took out.' }) +
          fRadio(p, 'mode', 'Holding period', [['yrs', 'Number of years'], ['dates', 'Start and end dates']], 'yrs') +
          fNum(p, 'yrs', 'Years held', 5, { min: 0 }) + fDate(p, 'd0', 'Start date', (CUR - 5) + '-01-01') + fDate(p, 'd1', 'End date', todayIso()) + '</div>';
      },
      calc: function (a) {
        var inv = a.n('inv'), dates = a.val('mode') === 'dates', yrs = dates ? C.yearsBetween(a.val('d0'), a.val('d1')) : a.n('yrs');
        if (!(inv > 0)) return msg('warnmsg', 'Please enter the amount invested.');
        if (dates && yrs == null) return msg('warnmsg', 'Please enter a start date and an end date.');
        var r = C.roi(inv, a.n('fin'), a.n('inc'), yrs);
        return head('Total return on investment (ROI)', pct(r.roi, 2), r.roi < 0) +
          kv([['Annualized return (CAGR)', r.cagr == null ? (yrs > 0 ? '—' : 'Enter a holding period') : pct(r.cagr, 2)], ['Gain or loss', money(r.gain)], ['Value plus income', money(r.total)], ['Years held', nf(yrs, 2)]]) +
          (yrs > 0 && yrs < 1 ? msg('warnmsg', 'For less than a year, the annualized return assumes the same pace for a full year.') : '') +
          how('ROI = (value now + income received − amount invested) / amount invested. Annualized return (compound annual growth rate, CAGR) = ((value now + income) / amount invested)^(1 / years) − 1, which counts the income as if it were received at the end. With dates, years = the days between them / 365.25. Fees and taxes count only if they are already reflected in the amounts you enter. If you added or took out money along the way, a money-weighted rate of return is more accurate.');
      },
      next: [['/calculators/compound-interest-calculator/', 'Compound interest calculator'], ['/calculators/rule-of-72-calculator/', 'Rule of 72 calculator'], ['/calculators/investment-fee-calculator/', 'Investment fee calculator']]
    });
  };

  /* ---------- Rule of 72 ---------- */
  // mode 'rate': x = yearly return (decimal) -> years to double; 'years': x = years -> yearly return needed (decimal). Exact uses yearly compounding.
  C.rule72 = function (mode, x) {
    if (!(x > 0)) return null;
    if (mode === 'years') { var e = 0.72 / x, ex = Math.pow(2, 1 / x) - 1; return { est: e, exact: ex, diff: e - ex }; }
    var est = 72 / (x * 100), t = Math.log(2) / Math.log(1 + x);
    return { est: est, exact: t, diff: est - t };
  };
  C.rule72Table = function () { var rows = []; for (var k = 1; k <= 12; k++) { var r = C.rule72('rate', k / 100); rows.push({ rate: k / 100, est: r.est, exact: r.exact, diff: r.diff }); } return rows; };

  W['rule-of-72'] = function (el) {
    shell(el, 'rule-of-72', {
      title: 'Rule of 72 calculator',
      intro: 'How many years it takes to double your money at a yearly return, or the return you need to double it in a number of years.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fRadio(p, 'mode', 'What do you know?', [['rate', 'The yearly return'], ['years', 'The years to double']], 'rate') +
          fNum(p, 'r', 'Yearly return (%)', 6, { min: 0, max: 100, step: 0.01 }) + fNum(p, 'n', 'Or years to double', 10, { min: 0, max: 200 }) + '</div>';
      },
      calc: function (a) {
        var yrs = a.val('mode') === 'years', r = C.rule72(yrs ? 'years' : 'rate', yrs ? a.n('n') : a.n('r') / 100), h;
        if (!r) return msg('warnmsg', yrs ? 'Please enter a number of years above 0.' : 'Please enter a yearly return above 0%.');
        if (yrs) h = head('Yearly return needed (rule of 72)', pct(r.est, 2)) + kv([['Exact return needed', pct(r.exact, 2)], ['Difference', nf(r.diff * 100, 2) + ' percentage points']]);
        else h = head('Years to double (rule of 72)', nf(r.est, 1) + ' years') + kv([['Exact years to double', nf(r.exact, 2)], ['Difference', nf(r.diff, 2) + ' years']]);
        return h + table(['Yearly return', 'Rule of 72 (years)', 'Exact (years)', 'Difference (years)'], C.rule72Table().map(function (t) { return [pct(t.rate, 0), nf(t.est, 2), nf(t.exact, 2), nf(t.diff, 2)]; }), 'Rule of 72 compared with the exact answer') +
          how('Rule of 72: years to double ≈ 72 / the yearly return in percent, and the return needed ≈ 72 / the years. Exact, with the return compounded once a year: years = ln 2 / ln(1 + return), and return = 2^(1 / years) − 1. The rule is closest to exact at returns near 8% a year. Returns are an assumption, not a forecast, and tax and fees lower them.');
      },
      next: [['/calculators/compound-interest-calculator/', 'Compound interest calculator'], ['/calculators/roi-calculator/', 'ROI calculator'], ['/calculators/inflation-calculator/', 'Inflation calculator']]
    });
  };

  /* ---------- Emergency fund ---------- */
  // Target = monthly costs x months. Months to reach it: interest at rate / 12 on the balance each month, then the monthly saving is added (capped at 1,200 months).
  C.emergencyFund = function (costs, months, saved, monthly, rate) {
    var target = Math.max(0, costs) * Math.max(0, months), have = Math.max(0, saved), i = Math.max(0, rate || 0) / 12, pm = Math.max(0, monthly), bal = have, m = 0;
    while (bal < target && m < 1200) { bal = bal * (1 + i) + pm; m++; }
    var ok = bal >= target;
    return { target: target, gap: Math.max(0, target - have), months: ok ? m : null, balance: ok ? bal : null, interest: ok ? bal - have - pm * m : null };
  };

  W['emergency-fund'] = function (el) {
    shell(el, 'emergency-fund', {
      title: 'Emergency fund calculator',
      intro: 'How much to keep for emergencies, how far you are from it, and how long it takes to get there.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'costs', 'Monthly essential costs', 3000, { min: 0, help: 'Housing, utilities, food, insurance, transportation and minimum debt payments.' }) +
          fSel(p, 'cover', 'Months of costs to cover', [['3', '3 months'], ['6', '6 months'], ['9', '9 months'], ['custom', 'Another number']], '6', { help: '3, 6 and 9 months are common planning choices, not rules.' }) +
          fNum(p, 'cm', 'If another number: months', 4, { min: 0, max: 60 }) + fNum(p, 'have', 'Saved so far', 5000, { min: 0 }) + fNum(p, 'save', 'Amount you save each month', 500, { min: 0 }) +
          fNum(p, 'rate', 'Savings interest rate (% a year, optional)', '', { min: 0, max: 20, step: 0.01, ph: 'Optional' }) + '</div>';
      },
      calc: function (a) {
        var mo = a.val('cover') === 'custom' ? a.n('cm') : +a.val('cover'), rate = a.n('rate') / 100;
        if (!(mo > 0)) return msg('warnmsg', 'Please enter the number of months to cover.');
        var r = C.emergencyFund(a.n('costs'), mo, a.n('have'), a.n('save'), rate);
        var items = [['Still to save', r.gap > 0 ? money(r.gap) : 'Target reached'], ['Time to reach it', r.months == null ? 'More than 100 years' : (r.months === 0 ? 'Already reached' : ym(r.months))]];
        if (rate > 0 && r.months) items.push(['Interest earned on the way', money(r.interest)]);
        return head('Your emergency fund target', money(r.target)) + kv(items) +
          how('Target = monthly essential costs x months of cover (' + nf(mo, mo % 1 ? 1 : 0) + '). Time to reach it adds your monthly saving at the end of each month' + (rate > 0 ? ', after a month of interest at the yearly rate / 12' : ', with no interest') + '. Keep an emergency fund where it is safe and easy to reach, such as a high-interest savings account; interest is taxable unless the account is a TFSA.');
      },
      next: [['/savings/high-interest-savings-accounts/', 'Best savings accounts'], ['/accounts/tfsa/', 'TFSA guide'], ['/calculators/credit-card-payoff-calculator/', 'Credit card payoff calculator']]
    });
  };

  /* ---------- Mortgage renewal ---------- */
  // Payment, interest over the term and balance at the end of the term from mortgageSchedule, the mortgage-payment engine (no new maths).
  C.mortgageTerm = function (bal, rate, years, f, term) {
    var s = mortgageSchedule(bal, rate, years, f), it = 0, pr = 0;
    s.years.forEach(function (y) { if (y[0] <= term) { it += y[1]; pr += y[2]; } });
    return { pay: s.pay, n: s.n, interest: it, principal: pr, balance: s.years.length >= term ? s.years[term - 1][3] : 0, periods: s.periods };
  };

  W['mortgage-renewal'] = function (el) {
    shell(el, 'mortgage-renewal', {
      title: 'Mortgage renewal calculator',
      intro: 'Compare two renewal offers: your new payment, the change from what you pay now, the interest over the term and the balance at the end of it.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'bal', 'Mortgage balance at renewal', 400000, { min: 0 }) +
          fNum(p, 'am', 'Amortization left (years)', 20, { min: 1, max: 40, help: 'Decimals are fine, for example 22.5.' }) + fSel(p, 'f', 'Payment frequency', FREQ, '12') +
          fNum(p, 'cr', 'Current rate (%, optional)', 2.5, { min: 0, max: 25, step: 0.01 }) + fNum(p, 'cp', 'Current payment ($, optional)', '', { min: 0, ph: 'Optional', help: 'Leave blank to work it out from the current rate.' }) +
          fNum(p, 'ra', 'Offer A rate (%)', 4.2, { min: 0, max: 25, step: 0.01 }) + fNum(p, 'rb', 'Offer B rate (%, optional)', 4.5, { min: 0, max: 25, step: 0.01 }) +
          fSel(p, 'term', 'Term', [['1', '1 year'], ['2', '2 years'], ['3', '3 years'], ['4', '4 years'], ['5', '5 years'], ['7', '7 years'], ['10', '10 years']], '5') + '</div>';
      },
      calc: function (a) {
        var bal = a.n('bal'), am = a.n('am'), f = a.val('f'), term = +a.val('term'), lab = FREQ.filter(function (x) { return x[0] === f; })[0][1].toLowerCase();
        if (!(bal > 0)) return msg('warnmsg', 'Please enter your mortgage balance at renewal.');
        if (!(am > 0) || am > 40) return msg('warnmsg', 'Please enter the amortization left, from 1 to 40 years.');
        if (a.val('ra') === '') return msg('warnmsg', 'Please enter the rate for offer A.');
        var O = [['Offer A', a.n('ra') / 100]]; if (a.val('rb') !== '') O.push(['Offer B', a.n('rb') / 100]);
        var fromRate = a.val('cp') === '' && a.val('cr') !== '', cur = a.val('cp') !== '' ? a.n('cp') : (fromRate ? C.mortgageTerm(bal, a.n('cr') / 100, am, f, term).pay : null);
        var R = O.map(function (o) { return { name: o[0], rate: o[1], t: C.mortgageTerm(bal, o[1], am, f, term) }; });
        var lo = R.length > 1 && R[1].t.pay < R[0].t.pay ? R[1] : R[0], hi = lo === R[0] ? R[R.length - 1] : R[0];
        var col = function (fn) { return R.map(fn); };
        var rows = [['Rate'].concat(col(function (x) { return pct(x.rate, 2); })), ['New ' + lab + ' payment'].concat(col(function (x) { return '<b>' + money2(x.t.pay) + '</b>'; })),
          ['Change from your current payment'].concat(col(function (x) { return cur == null ? '—' : signed2(x.t.pay - cur); })),
          ['Interest over the ' + term + '-year term'].concat(col(function (x) { return money(x.t.interest); })), ['Balance at the end of the term'].concat(col(function (x) { return money(x.t.balance); }))];
        var items = [['Current ' + lab + ' payment', cur == null ? 'Not entered' : money2(cur) + (fromRate ? ' (from your current rate)' : '')]];
        if (R.length > 1) items.push(['Interest saved over the term with ' + lo.name, money(hi.t.interest - lo.t.interest)]);
        return head('Your new ' + lab + ' payment' + (R.length > 1 ? ' at the lower rate (' + lo.name + ')' : ''), money2(lo.t.pay)) + kv(items) +
          table([''].concat(R.map(function (x) { return x.name; })), rows, 'Your renewal offers') +
          how('Each offer uses the same engine as our mortgage payment calculator: Canadian fixed-rate compounding (semi-annual, not in advance) for every frequency, with semi-monthly, biweekly and accelerated payments set from the monthly payment the same way. The payment is worked out on your balance over the amortization left and held for the whole term.' + (fromRate ? ' Your current payment is worked out the same way at your current rate, which matches what you pay if your mortgage is on schedule.' : '') + ' A variable rate can change during the term, so treat a variable-rate result as an estimate. Switching lenders can bring legal, appraisal or discharge costs, which are not included.');
      },
      next: [['/mortgages/mortgage-renewal-rates/', 'Mortgage renewal rates'], ['/mortgages/switching-mortgage-lenders/', 'Switching lenders at renewal'], ['/calculators/mortgage-payment-calculator/', 'Mortgage payment calculator']]
    });
  };

  /* ---------- EI maternity and parental benefits ---------- */
  // Weekly benefit at a rate with the ei-calc rule: earnings count up to the maximum insurable earnings / 52, the benefit is capped at the
  // published maximum, and at or above the earnings ceiling it is that maximum. null while the rate is not verified.
  function eiCapped(awie, rate, max) {
    var capE = D.payroll.ei.mie / 52, ins = Math.min(Math.max(0, awie), capE);
    if (!isNum(rate)) return null;
    var b = ins * rate;
    if (isNum(max)) b = awie >= capE ? max : Math.min(b, max);
    return b;
  }
  // opt: mat_std (maternity + standard parental), mat_ext (maternity + extended), std or ext (parental only). shared: parental weeks shared by two parents.
  C.eiParental = function (awie, opt, shared) {
    var P = D.ei_parental || {}, capE = D.payroll.ei.mie / 52, ext = opt === 'mat_ext' || opt === 'ext', mat = opt === 'mat_std' || opt === 'mat_ext';
    var std = eiCapped(awie, P.standard_rate, P.max_weekly_standard), par = ext ? eiCapped(awie, P.extended_rate, P.max_weekly_extended) : std;
    var mw = mat ? (isNum(P.maternity_weeks) ? P.maternity_weeks : null) : 0;
    var pk = shared ? (ext ? P.shared_extended_weeks : P.shared_standard_weeks) : (ext ? P.extended_weeks : P.standard_weeks), pw = isNum(pk) ? pk : null;
    var mt = mat ? (mw == null || std == null ? null : mw * std) : 0, pt = pw == null || par == null ? null : pw * par;
    return { insurable: Math.min(Math.max(0, awie), capE), capEarnings: capE, matWeeks: mw, matWeekly: mat ? std : null, matTotal: mt, parWeeks: pw, parWeekly: par, parTotal: pt,
             weeks: mw == null || pw == null ? null : mw + pw, total: mt == null || pt == null ? null : mt + pt };
  };

  W['ei-parental'] = function (el) {
    shell(el, 'ei-parental', {
      title: 'EI maternity and parental benefits calculator',
      intro: 'Estimate your weekly EI maternity and parental benefit, the number of weeks and the total before tax.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fRadio(p, 'mode', 'Enter your earnings as', [['yr', 'Yearly insurable earnings'], ['wk', 'Average weekly insurable earnings']], 'yr') +
          fNum(p, 'sal', 'Yearly insurable earnings', MEM.get('income', 60000), { min: 0, help: 'Divided by 52 to get weekly earnings.' }) + fNum(p, 'wk', 'Or average weekly insurable earnings', 1000, { min: 0 }) +
          fSel(p, 'opt', 'Benefits', [['mat_std', 'Maternity plus standard parental'], ['mat_ext', 'Maternity plus extended parental'], ['std', 'Parental only, standard'], ['ext', 'Parental only, extended']], 'mat_std') +
          fRadio(p, 'sh', 'Sharing parental benefits with the other parent?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fRadio(p, 'qc', 'Do you live in Quebec?', [['n', 'No'], ['y', 'Yes']], provDefault() === 'QC' ? 'y' : 'n') + '</div>';
      },
      calc: function (a) {
        if (a.val('qc') === 'y') return msg('warnmsg', 'Quebec parents receive maternity, paternity and parental benefits from the Quebec Parental Insurance Plan (QPIP), not EI. This calculator does not cover QPIP.');
        if (!D.payroll) return msg('warnmsg', 'Payroll figures for ' + CUR + ' are being confirmed.');
        var opt = a.val('opt'), sh = a.val('sh') === 'y', ext = opt === 'mat_ext' || opt === 'ext', mat = opt.indexOf('mat') === 0, P = D.ei_parental || {};
        var r = C.eiParental(a.val('mode') === 'yr' ? a.n('sal') / 52 : a.n('wk'), opt, sh), v2 = function (x) { return x == null ? TBD : money2(x); };
        var h = r.total != null ? head('Estimated total before tax', money(r.total)) : (r.parWeekly != null ? head('Weekly ' + (ext ? 'extended' : 'standard') + ' parental benefit, before tax', money2(r.parWeekly)) :
          (mat && r.matWeekly != null ? head('Weekly maternity benefit, before tax', money2(r.matWeekly)) : head('Weekly benefit, before tax', TBD)));
        var items = [['Weekly insurable earnings used', money2(r.insurable)]];
        if (mat) items.push(['Maternity weeks', r.matWeeks == null ? TBD : String(r.matWeeks)], ['Weekly maternity benefit' + (isNum(P.standard_rate) ? ' (' + pct(P.standard_rate, 0) + ')' : ''), v2(r.matWeekly)]);
        items.push(['Parental weeks' + (sh ? ', shared by both parents' : ''), r.parWeeks == null ? TBD : String(r.parWeeks)], ['Weekly ' + (ext ? 'extended' : 'standard') + ' parental benefit' + (isNum(ext ? P.extended_rate : P.standard_rate) ? ' (' + pct(ext ? P.extended_rate : P.standard_rate, 0) + ')' : ''), v2(r.parWeekly)],
          ['Total weeks', r.weeks == null ? TBD : String(r.weeks)], ['Total before tax', r.total == null ? TBD : money(r.total)]);
        h += kv(items);
        if (r.total == null) h += msg('warnmsg', 'Some ' + CUR + ' EI maternity and parental figures are being confirmed, so parts of the result show ' + TBD + '.');
        if (sh) h += msg('ok', 'With sharing, the total assumes both parents have the same insurable earnings. Each parent applies separately, and each parent\'s weekly benefit is based on their own earnings.');
        return h + msg('ok', 'EI benefits are taxable income, so the amount you keep after tax is lower.') +
          how('Maternity and standard parental benefits pay ' + (isNum(P.standard_rate) ? pct(P.standard_rate, 0) : 'a set share') + ' of your average weekly insurable earnings; extended parental benefits pay ' + (isNum(P.extended_rate) ? pct(P.extended_rate, 0) : 'a lower share (being confirmed)') + ' over more weeks. Earnings count up to the ' + CUR + ' maximum insurable earnings of ' + money(D.payroll.ei.mie) + ' a year (' + money2(r.capEarnings) + ' a week), and each weekly benefit is capped at its published maximum' + (isNum(P.max_weekly_standard) ? ' (' + money(P.max_weekly_standard) + ' at the standard rate' + (isNum(P.max_weekly_extended) ? ', ' + money(P.max_weekly_extended) + ' extended' : '') + ')' : '') + '; at or above that weekly amount, the benefit is the maximum. Total = weeks x weekly benefit. Maternity benefits are paid at the standard rate whichever parental option you choose. Service Canada works out your average from your best weeks of earnings and decides your actual benefit, and you need enough insurable hours to qualify.');
      },
      next: [['/benefits/ei-payment-dates/', 'EI payment dates'], ['/benefits/canada-child-benefit/', 'Canada Child Benefit'], ['/calculators/take-home-pay-calculator/', 'Take-home pay calculator']]
    });
  };

  /* ---------- Canada Dental Care Plan eligibility ---------- */
  // D.cdcp = {income_limit, tiers: [[upper, copay], ...], groups_note}. Income below a tier's upper limit (null = no upper limit) falls in that tier.
  C.cdcp = function (income, insured, filed) {
    var X = D.cdcp || {}, why = [], tier = null, copay = null;
    if (insured) why.push('insurance');
    if (!filed) why.push('return');
    if (isNum(X.income_limit) && income >= X.income_limit) why.push('income');
    var status = why.length ? 'not' : (isNum(X.income_limit) ? 'eligible' : 'tbd');
    if (status !== 'not' && Array.isArray(X.tiers)) {
      for (var k = 0; k < X.tiers.length; k++) { var t = X.tiers[k]; if (Array.isArray(t) && t.length >= 2 && (t[0] == null || income < t[0])) { tier = k; copay = isNum(t[1]) ? t[1] : null; break; } }
    }
    return { status: status, reasons: why, tier: tier, copay: copay };
  };

  W['cdcp-check'] = function (el) {
    shell(el, 'cdcp-check', {
      title: 'Canada Dental Care Plan eligibility check',
      intro: 'Answer three questions to see whether you are likely eligible for the Canada Dental Care Plan, and your co-payment.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'inc', 'Adjusted family net income', 60000, { min: 0, help: 'Your net income plus your spouse\'s or common-law partner\'s, from last year\'s returns, as adjusted by the CRA.' }) +
          fRadio(p, 'ins', 'Do you have access to dental insurance?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fRadio(p, 'filed', 'Did you (and your spouse or partner) file last year\'s tax return?', [['y', 'Yes'], ['n', 'No']], 'y') + '</div>';
      },
      calc: function (a) {
        var inc = a.n('inc'), r = C.cdcp(inc, a.val('ins') === 'y', a.val('filed') === 'y'), X = D.cdcp || {}, h;
        var WHY = { insurance: 'You have access to dental insurance.', 'return': 'You (and your spouse or partner) need to have filed last year\'s tax return.', income: 'Your adjusted family net income is at or above the ' + (isNum(X.income_limit) ? money(X.income_limit) : '') + ' limit.' };
        if (r.status === 'not') h = head('Canada Dental Care Plan', 'Likely not eligible', true) + msg('warnmsg', r.reasons.map(function (k) { return WHY[k]; }).join(' '));
        else if (r.status === 'eligible') h = head('Canada Dental Care Plan', 'Likely eligible') + kv([['Your co-payment', r.copay == null ? TBD : (r.copay === 0 ? 'None' : pct(r.copay, 0) + ' of the plan\'s fee')], ['Income limit', money(X.income_limit)]]);
        else h = head('Canada Dental Care Plan', 'Income limit being confirmed') + msg('warnmsg', 'You meet the dental insurance and tax return conditions. The income limit and co-payment levels for ' + CUR + ' are being confirmed.');
        if (Array.isArray(X.tiers) && X.tiers.length) {
          var lo = 0, rows = [];
          X.tiers.forEach(function (t, k) {
            if (!Array.isArray(t) || t.length < 2) return;
            var band = t[0] == null ? money(lo) + ' or more' : (lo ? money(lo) + ' to under ' : 'Under ') + money(t[0]), c = isNum(t[1]) ? (t[1] === 0 ? 'None' : pct(t[1], 0)) : TBD;
            rows.push(k === r.tier ? ['<b>' + band + '</b>', '<b>' + c + '</b>'] : [band, c]); if (t[0] != null) lo = t[0];
          });
          h += table(['Adjusted family net income', 'Co-payment'], rows, 'Co-payment by income');
        }
        if (typeof X.groups_note === 'string' && X.groups_note) h += msg('ok', esc(X.groups_note));
        return h + how('You may qualify for the Canada Dental Care Plan if you are a resident of Canada for tax purposes, do not have access to dental insurance, have filed last year\'s tax return (and so has your spouse or common-law partner), and your adjusted family net income is below the income limit. The co-payment is the share of the plan\'s fee for each covered service that you pay, and it depends on your income. This is a guide only: eligibility is confirmed when you apply.');
      },
      next: [['/benefits/', 'Government benefits'], ['/benefits/canada-child-benefit/', 'Canada Child Benefit']]
    });
  };

  /* =====================================================================
   * 4e. WIDGETS ADDED FOR PAGES 394 TO 489 (November 9, 2026, v1.5)
   * Every C.* helper below is mirrored in qa/wscalc.py and cross-checked. A jurisdiction whose table the registers have not
   * verified is null in the data and shows "being confirmed" with no figures.
   * ===================================================================== */

  /* ---------- LIF minimum and maximum (lif-max) ---------- */
  // D.lif.jur[code] = null (not verified) or {basis, kind, from, rates, below, plus, greater} for kind 'pct' (rates = share of the
  // January 1 value) or 'factor' (Manitoba factor F, applied to the January 1 value plus transfers in, taken as none), or {basis, kind: 'qc',
  // age, under} (Quebec: no maximum from age 55; under 55 the prescribed rate x the balance). basis: the age each table uses, 'dec31' (age
  // on December 31 of last year), 'attained' (age reached this year) or 'jan1' (age at the start of this year). rates[i] is for age from + i;
  // below covers every younger age; plus = the last row also covers older ages. Returns null outside the table.
  C.lifRate = function (J, age) {
    if (age < J.from) return isNum(J.below) ? J.below : null;
    var i = age - J.from;
    if (i < J.rates.length) return J.rates[i];
    return J.plus ? J.rates[J.rates.length - 1] : null;
  };
  // jur: a LIF_J code. age: on the jurisdiction's basis (rounded). value: LIF value on January 1. ret: last year's investment return in
  // dollars (null = not entered), used only where greater is true. Minimum = RRIF minimum for the age at the start of the year (age - 1 on
  // the 'attained' basis). Maximum = the table amount, or last year's return if greater, never below the minimum nor above the balance.
  // status: 'tbd' (not verified: no figures), 'range' (age outside the table: minimum only), 'nomax' (Quebec 55 and over) or 'ok'.
  C.lifMax = function (jur, age, value, ret) {
    var J = ((D.lif || {}).jur || {})[jur];
    age = Math.round(age); value = Math.max(0, value || 0); ret = isNum(ret) ? ret : null;
    var o = { status: 'tbd', basis: J ? J.basis : null, age: age, jan1: null, value: value, min_rate: null, min: null, max_rate: null, formula: null, ret: null, greater: false, max: null, max_from: null };
    if (!J) return o;
    o.jan1 = J.basis === 'attained' ? age - 1 : age; o.min_rate = C.rrifFactor(o.jan1); o.min = value * o.min_rate;
    var rate;
    if (J.kind === 'qc') {
      if (age >= J.age) { o.status = 'nomax'; o.max = value; o.max_from = 'balance'; return o; }
      rate = J.under;
    } else rate = C.lifRate(J, age);
    if (!isNum(rate)) { o.status = 'range'; return o; }
    o.status = 'ok'; o.max_rate = rate; o.formula = value * rate; o.greater = !!J.greater;
    var mx = o.formula, from = 'formula';
    if (o.greater && ret != null) { o.ret = ret; if (ret > mx) { mx = ret; from = 'return'; } }
    if (o.min > mx) { mx = o.min; from = 'minimum'; }
    if (mx > value) { mx = value; from = 'balance'; }
    o.max = mx; o.max_from = from;
    return o;
  };

  var LIF_J = [['ON', 'Ontario'], ['FED', 'Federal (federally regulated pension)'], ['BC', 'British Columbia'], ['AB', 'Alberta'], ['MB', 'Manitoba'], ['NB', 'New Brunswick'],
               ['NL', 'Newfoundland and Labrador'], ['NS', 'Nova Scotia'], ['QC', 'Quebec'], ['SK', 'Saskatchewan']];
  W['lif-max'] = function (el) {
    var L = D.lif || { jur: {} }, Y = L.year || CUR, NM = {};
    LIF_J.forEach(function (x) { NM[x[0]] = x[1]; });
    function basis(j) { var J = L.jur[j]; return J ? J.basis : 'jan1'; }
    function ageLabel(j) { var b = basis(j); return b === 'dec31' ? 'Age on December 31, ' + (Y - 1) : (b === 'attained' ? 'Age you reach in ' + Y : 'Age on January 1, ' + Y); }
    function ageAt(j, age) { var b = basis(j); return 'age ' + age + (b === 'dec31' ? ' on December 31, ' + (Y - 1) : (b === 'attained' ? ' reached in ' + Y : ' on January 1, ' + Y)); }
    function basisText(j) { var b = basis(j); return b === 'dec31' ? 'age on December 31, ' + (Y - 1) : (b === 'attained' ? 'age reached in ' + Y : 'age on January 1, ' + Y); }
    function relabel(api) { var lb = api.form.querySelector('label[for="' + api.p + 'age"]'); if (lb) lb.textContent = ageLabel(api.val('jur')); }
    var def = PRESET.prov && NM[PRESET.prov] ? PRESET.prov : (NM[MEM.get('prov', 'ON')] ? MEM.get('prov', 'ON') : 'ON');
    function nf5(x) { return rnd(x, 5).toLocaleString('en-CA', { maximumFractionDigits: 5 }); }
    var METHOD = {
      FED: function (J) { return 'Federal: the maximum is your January 1 value times the OSFI ' + Y + ' percentage for your age on December 31, ' + (Y - 1) + '. The table uses the November ' + (Y - 1) + ' long-term Government of Canada bond yield (' + pct(L.ref, 2) + ') for the first 15 years and 6.00% after, to the end of the year you turn 90; from that year there is no maximum. In the first year the maximum is prorated by the months remaining, and money transferred in during the year does not raise it. If the minimum is higher than the table amount, the maximum equals the minimum.'; },
      ON: function (J) { return 'Ontario: the maximum is the greater of your January 1 value divided by the annuity factor in FSRA\'s table (by the age you reach in the year) and your LIF\'s investment earnings in the previous year, including unrealized gains or losses. The table uses 6.00%, because the November ' + (Y - 1) + ' bond yield (' + pct(L.ref, 2) + ') is below that floor. It is prorated for a short first fiscal year.'; },
      BC: function (J) { return 'British Columbia: the maximum is the greater of the previous year\'s LIF investment return and your January 1 value times the BC maximum percentage for your age. The ' + Y + ' table uses 6.00%, because the November ' + (Y - 1) + ' bond yield (' + pct(L.ref, 2) + ') is below that floor. It applies to LIFs opened on or after September 30, 2015.'; },
      MB: function (J) { return 'Manitoba: the maximum is the larger of Option 1, factor F for your age at the end of the previous year (at Manitoba\'s ' + Y + ' reference rate of ' + pct(L.mb_ref, 1) + ') times your January 1 value plus money transferred in during the year, and Option 2, the growth in your LIF in the previous year plus 6% of that money transferred in (money never held in a LIF, PRPP or VB account). This calculator assumes no money is transferred in during the year.'; },
      NB: function (J) { return 'New Brunswick: the maximum is your January 1 value times the FCNB ' + Y + ' percentage for the age you will be during ' + Y + '. The FCNB table and guide do not state a "last year\'s return" option.'; },
      NL: function (J) { return 'Newfoundland and Labrador: the maximum is the greater of your January 1 value divided by the annuity factor F (the ' + Y + ' table, by age at the start of the year) and the previous year\'s investment earnings, including unrealized gains or losses. The table uses 6.00%, because the November ' + (Y - 1) + ' bond yield (' + pct(L.ref, 2) + ') is below that floor.'; },
      QC: function (J) { return 'Quebec: from age 55 there is no maximum; you can withdraw any amount each year until the balance is $0. Under 55, the upper limit of the life income is the prescribed rate (' + pct(J.under, 2) + ' for ' + Y + ') times the LIF balance on December 31 or January 1, and any temporary income, where the contract offers it, reduces it. The life income must be at least the RRIF minimum.'; }
    };
    shell(el, 'lif-max', {
      title: 'LIF minimum and maximum withdrawal calculator',
      intro: 'Your ' + Y + ' LIF minimum and maximum from the pension law that governs your LIF, your age and your LIF value on January 1.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fSel(p, 'jur', 'Pension law that governs your LIF', LIF_J, def, { help: 'The law of the pension plan the locked-in money came from, as shown on your LIF contract.' }) +
          fNum(p, 'age', ageLabel(def), 65, { min: 0, max: 120, step: 1, help: 'Each table uses its own age date, shown in this label.' }) +
          fNum(p, 'value', 'LIF value on January 1, ' + Y, 200000, { min: 0 }) +
          fNum(p, 'ret', 'Last year\'s investment return ($, optional)', '', { help: 'Ontario, British Columbia, Manitoba and Newfoundland and Labrador only: the LIF\'s investment earnings in ' + (Y - 1) + ', including unrealized gains or losses. Leave blank to use the table only.' }) + '</div>';
      },
      init: function (api) {
        relabel(api);
        api.form.addEventListener('change', function (e) { if (e.target && e.target.name === 'jur') relabel(api); });
        api.form.addEventListener('reset', function () { setTimeout(function () { relabel(api); }, 0); });
      },
      calc: function (a) {
        var jur = a.val('jur'), nm = jur === 'FED' ? 'federal' : (NM[jur] || jur), J = L.jur[jur], rv = String(a.val('ret')).trim(), ret = rv === '' ? null : a.n('ret');
        relabel(a);
        var r = C.lifMax(jur, a.n('age'), a.n('value'), ret), h, items = [], notes = '';
        if (r.status === 'tbd') return head(nm + ' LIF, ' + Y, 'Being confirmed') + msg('warnmsg', 'The ' + Y + ' ' + nm + ' LIF rules and maximum are being confirmed, so no figures are shown yet. Your LIF provider can tell you this year\'s minimum and maximum.');
        var maxLabel = 'Maximum withdrawal for ' + Y;
        if (r.status === 'nomax') h = head(maxLabel, 'No maximum');
        else if (r.status === 'range') h = head(maxLabel, 'Not in the ' + Y + ' table', true);
        else h = head(maxLabel, money(r.max));
        items.push(['Minimum withdrawal for ' + Y, money(r.min)]);
        if (r.status === 'ok') items.push(['Maximum per month', money(r.max / 12)]);
        items.push(['Minimum factor (age ' + r.jan1 + ' at the start of ' + Y + ')', pct(r.min_rate, 2)]);
        if (r.status === 'ok') {
          if (J.kind === 'qc') items.push(['Upper limit rate (under 55)', pct(r.max_rate, 2)]);
          else if (J.kind === 'factor') items.push(['Maximum factor F (' + ageAt(jur, r.age) + ')', nf5(r.max_rate)]);
          else items.push(['Maximum percentage (' + ageAt(jur, r.age) + ')', nf5(r.max_rate * 100) + '%']);
          if (r.ret != null || r.max_from !== 'formula') items.push(['Maximum by the table', money(r.formula)]);
          if (r.ret != null) items.push(['Last year\'s investment return', money(r.ret)]);
        }
        h += kv(items);
        if (r.status === 'range') {
          var last = J.from + J.rates.length - 1;
          notes += msg('warnmsg', 'The ' + Y + ' ' + nm + ' table covers ' + (isNum(J.below) ? 'every age up to ' + last : 'ages ' + J.from + ' to ' + last) + (J.plus ? ' and over' : '') + ' (' + basisText(jur) + '). For other ages, ask your LIF provider for the maximum.');
        }
        if (r.status === 'nomax') notes += msg('ok', 'Holders 55 and over have no maximum: you can withdraw any amount this year, up to the whole balance of ' + money(r.max) + '. The minimum still applies.');
        if (r.max_from === 'return') notes += msg('ok', 'Last year\'s investment return is higher than the table amount, so it sets your maximum.');
        if (r.max_from === 'minimum') notes += msg('ok', 'The minimum is higher than the table amount, so the maximum equals the minimum.');
        if (r.status === 'ok' && r.max_from === 'balance') notes += msg('ok', 'The maximum is capped at your LIF balance.');
        if (ret != null && r.status === 'ok' && !r.greater) notes += msg('warnmsg', 'The ' + nm + ' rules as published do not include a "last year\'s return" option, so the return you entered is not used.');
        if (J.kind === 'qc' && r.status === 'ok') notes += msg('ok', 'If your contract offers temporary income, it reduces this upper limit.');
        return h + notes + how((METHOD[jur] ? METHOD[jur](J) + ' ' : '') +
          'The minimum is the RRIF minimum: your LIF value on January 1 times the factor for your age at the start of the year (1 / (90 - age) under 71, then the prescribed factors, reaching 20% at 95 and over)' +
          (J.basis === 'attained' ? '; this table uses the age you reach in ' + Y + ', so the minimum uses one year less, unless your birthday is January 1' : '') +
          '. If you chose to base the minimum on a younger spouse\'s or partner\'s age, your minimum is lower than shown. No minimum applies in the year the LIF is opened. All LIF payments are taxable income in the year you receive them.');
      },
      next: [['/accounts/lif/', 'LIF guide'], ['/accounts/rrif-minimum-withdrawal/', 'RRIF minimum withdrawal table'], ['/compare/best-lira-accounts/', 'Best LIRA accounts']]
    });
  };

  function byId(id) { return D.brokers.filter(function (b) { return b.id === id; })[0]; }


  /* =====================================================================
   * 5. START
   * ===================================================================== */
  function start() {
    var els = document.querySelectorAll('[data-ws-widget]');
    Array.prototype.forEach.call(els, function (el) {
      if (el.getAttribute('data-ws-ready')) return;
      var name = el.getAttribute('data-ws-widget');
      if (!W[name]) { if (window.console) console.warn('WealthScale widget not found: ' + name); return; }
      el.setAttribute('data-ws-ready', '1');
      PRESET = { prov: el.getAttribute('data-province') };
      try { W[name](el); } catch (e) { el.innerHTML = '<p class="ws-note">This calculator could not load. Please refresh the page.</p>'; if (window.console) console.error(e); }
      PRESET = {};
    });
  }
  window.WS.start = start;
  window.WS.widgets = Object.keys(W);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
