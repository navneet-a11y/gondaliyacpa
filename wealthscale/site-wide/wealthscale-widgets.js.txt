/*! WealthScale widgets v1.2 | October 24, 2026 (dividend credits for AB, SK, MB, YT, NT, NU added November 5, 2026) | (c) WealthScale Media Inc.
 * One file, loaded site-wide. Place <div data-ws-widget="NAME"></div> in any page.
 * All figures live in the WS_DATA block below. Update a figure there once and every page updates.
 * General information only. Not financial, investment, tax or legal advice.
 */
(function () {
  'use strict';

  /* =====================================================================
   * 1. DATA: every figure the widgets use. EDIT FIGURES HERE ONLY.
   * ===================================================================== */
  var D = {"asOf":"2026-10-23","year":2026,"provinces":[["AB","Alberta"],["BC","British Columbia"],["MB","Manitoba"],["NB","New Brunswick"],["NL","Newfoundland and Labrador"],["NS","Nova Scotia"],["NT","Northwest Territories"],["NU","Nunavut"],["ON","Ontario"],["PE","Prince Edward Island"],["QC","Quebec"],["SK","Saskatchewan"],["YT","Yukon"]],"provName":{"AB":"Alberta","BC":"British Columbia","MB":"Manitoba","NB":"New Brunswick","NL":"Newfoundland and Labrador","NS":"Nova Scotia","NT":"Northwest Territories","NU":"Nunavut","ON":"Ontario","PE":"Prince Edward Island","QC":"Quebec","SK":"Saskatchewan","YT":"Yukon"},"age_of_majority":{"AB":18,"BC":19,"MB":18,"NB":19,"NL":19,"NS":19,"NT":19,"NU":19,"ON":18,"PE":18,"QC":18,"SK":18,"YT":19},"tax":{"federal":{"brackets":[[58523,0.14],[117045,0.205],[181440,0.26],[258482,0.29],[null,0.33]],"bpa":16452,"bpa_min":14829,"bpa_phase":[181440,258482]},"provinces":{"AB":{"brackets":[[61200,0.08],[154259,0.1],[185111,0.12],[246813,0.13],[370220,0.14],[null,0.15]],"bpa":22769},"BC":{"brackets":[[50363,0.056],[100728,0.077],[115648,0.105],[140430,0.1229],[190405,0.147],[265545,0.168],[null,0.205]],"bpa":13216,"reduction":{"type":"bc","base":690,"threshold":25570,"rate":0.0356}},"MB":{"brackets":[[47000,0.108],[100000,0.1275],[null,0.174]],"bpa":15780,"bpa_phase":[200000,400000,0]},"NB":{"brackets":[[52333,0.094],[104666,0.14],[193861,0.16],[null,0.195]],"bpa":13664},"NL":{"brackets":[[44678,0.087],[89354,0.145],[159528,0.158],[223340,0.178],[285319,0.198],[570638,0.208],[1141275,0.213],[null,0.218]],"bpa":13094},"NS":{"brackets":[[30995,0.0879],[61991,0.1495],[97417,0.1667],[157124,0.175],[null,0.21]],"bpa":11932},"NT":{"brackets":[[53003,0.059],[106009,0.086],[172346,0.122],[null,0.1405]],"bpa":18198},"NU":{"brackets":[[55801,0.04],[111602,0.07],[181439,0.09],[null,0.115]],"bpa":19659},"ON":{"brackets":[[53891,0.0505],[107785,0.0915],[150000,0.1116],[220000,0.1216],[null,0.1316]],"bpa":12989,"surtax":[[5818,0.2],[7446,0.36]],"health_premium":[[20000,36000,0,0.06,300],[36000,48000,300,0.06,450],[48000,72000,450,0.25,600],[72000,200000,600,0.25,750],[200000,null,750,0.25,900]],"reduction":{"type":"on","base":300.0,"dep":554.0}},"PE":{"brackets":[[33928,0.095],[65820,0.1347],[106890,0.166],[142520,0.1762],[200000,0.19],[null,0.2]],"bpa":15000},"QC":{"brackets":[[54345,0.14],[108680,0.19],[132245,0.24],[null,0.2575]],"bpa":18952},"SK":{"brackets":[[54532,0.105],[155805,0.125],[null,0.145]],"bpa":20381},"YT":{"brackets":[[58523,0.064],[117045,0.09],[181440,0.109],[500000,0.128],[null,0.15]],"bpa":16452,"bpa_phase":[181440,258482,14829]}},"qc_abatement":0.165,"dividends":{"eligible_grossup":0.38,"noneligible_grossup":0.15,"federal_dtc_eligible":0.150198,"federal_dtc_noneligible":0.090301,"provincial_dtc":{"ON":[0.1,0.029863],"BC":[0.12,0.0196],"QC":[0.117,0.0342],"NB":[0.14,0.0275],"NS":[0.0885,0.015],"PE":[0.105,0.013043],"NL":[0.063,0.032],"AB":[0.0812,0.0218],"SK":[0.11,0.02519],"MB":[0.08,0.007835],"YT":[0.1202,0.0067],"NT":[0.115,0.06],"NU":[0.0551,0.0261]}},"capital_gains_inclusion":0.5},"tfsa":{"limits":{"2009":5000,"2010":5000,"2011":5000,"2012":5000,"2013":5500,"2014":5500,"2015":10000,"2016":5500,"2017":5500,"2018":5500,"2019":6000,"2020":6000,"2021":6000,"2022":6000,"2023":6500,"2024":7000,"2025":7000,"2026":7000},"over_tax_month":0.01},"rrsp":{"limits":{"2020":27230,"2021":27830,"2022":29210,"2023":30780,"2024":31560,"2025":32490,"2026":33810,"2027":35390},"pct":0.18,"cushion":2000,"deadline":{"2025":"2026-03-02","2026":"2027-03-01"},"withholding":{"other":[[5000,0.1],[15000,0.2],[null,0.3]],"QC":[[5000,0.05],[15000,0.1],[null,0.15]],"QC_prov":0.14},"withholding_text":"10% up to $5,000, 20% over $5,000 to $15,000 and 30% over $15,000 (outside Quebec)"},"fhsa":{"annual":8000,"lifetime":40000,"carry":8000,"max_years":15,"max_age":71,"first_year":2023},"resp":{"lifetime":50000,"cesg_rate":0.2,"cesg_on":2500,"cesg_annual":500,"cesg_max_year":1000,"cesg_lifetime":7200,"cesg_age16_total":2000,"cesg_age16_years":4,"acesg_rates":[0.2,0.1],"acesg_on_first":500,"acesg_income":[58523,117045],"clb_first":500,"clb_yearly":100,"clb_max":2000,"clb_thresholds":[null,58523,58523,58523,66036,73577],"bctesg":1200,"qesi_rate":0.1,"qesi_annual":250,"qesi_lifetime":3600},"rrif":{"factors":{"71":0.0528,"72":0.054,"73":0.0553,"74":0.0567,"75":0.0582,"76":0.0598,"77":0.0617,"78":0.0636,"79":0.0658,"80":0.0682,"81":0.0708,"82":0.0738,"83":0.0771,"84":0.0808,"85":0.0851,"86":0.0899,"87":0.0955,"88":0.1021,"89":0.1099,"90":0.1192,"91":0.1306,"92":0.1449,"93":0.1634,"94":0.1879,"95":0.2}},"hbp":{"max":60000,"repay_years":15,"deferral":[2022,2028],"deferral_start":5},"us_withholding":{"treaty":0.15,"no_w8":0.3,"accounts":[["rrsp","RRSP",true,"Not needed","RRSPs are exempt from US withholding on dividends from US-listed securities held directly, under Article XXI of the Canada-US tax treaty."],["rrif","RRIF",true,"Not needed","RRIFs are treated like RRSPs: no US withholding on dividends from US-listed securities held directly."],["lira","LIRA or LIF",true,"Not needed","Locked-in retirement accounts are retirement arrangements, so the treaty exemption applies."],["tfsa","TFSA",false,"No","The tax withheld in a TFSA is a permanent cost: there is no Canadian tax to credit it against."],["fhsa","FHSA",false,"No","FHSAs are not retirement accounts, so withholding applies and cannot be recovered."],["resp","RESP",false,"No","RESPs are not retirement accounts, so withholding applies and cannot be recovered."],["nonreg","Non-registered (cash or margin)",false,"Yes, as a foreign tax credit","You report the gross dividend and claim a foreign tax credit for the US tax on your Canadian return."]]},"deposit_insurance":{"limit":100000,"categories":["Deposits in your name","Joint deposits","Deposits in trust","RRSP deposits","RRIF deposits","TFSA deposits","FHSA deposits","RESP deposits","RDSP deposits"],"note":"Credit unions are covered by provincial deposit insurance instead."},"cipf":{"limit":1000000,"groups":[["General accounts","cash, margin, TFSA and FHSA accounts combined"],["Registered retirement accounts","RRSP, RRIF and LIF accounts combined"],["RESPs","RESP accounts"]]},"benefits":{"cpp_oas":{"name":"CPP and OAS","dates":["2026-01-28","2026-02-25","2026-03-27","2026-04-28","2026-05-27","2026-06-26","2026-07-29","2026-08-27","2026-09-25","2026-10-28","2026-11-26","2026-12-22"],"note":"Old Age Security and the Guaranteed Income Supplement are paid on the same day as the Canada Pension Plan. 2027 dates have not been published yet."},"gst":{"name":"Canada Groceries and Essentials Benefit (formerly the GST/HST credit)","dates":["2026-01-05","2026-04-02","2026-07-03","2026-10-05","2027-01-05","2027-04-05"],"note":"The Canada Groceries and Essentials Benefit replaced the GST/HST credit in July 2026."},"ccb":{"name":"Canada Child Benefit","dates":["2026-01-20","2026-02-20","2026-03-20","2026-04-20","2026-05-20","2026-06-19","2026-07-20","2026-08-20","2026-09-18","2026-10-20","2026-11-20","2026-12-11"],"note":"2027 dates have not been published yet."},"otb":{"name":"Ontario Trillium Benefit","dates":["2026-01-09","2026-02-10","2026-03-10","2026-04-10","2026-05-08","2026-06-10","2026-07-10","2026-08-10","2026-09-10","2026-10-09","2026-11-10","2026-12-10"],"note":"2027 dates have not been published yet."},"cdb":{"name":"Canada Disability Benefit","dates":["2026-01-15","2026-02-19","2026-03-19","2026-04-16","2026-05-21","2026-06-18","2026-07-16","2026-08-20","2026-09-17","2026-10-15","2026-11-19","2026-12-17"],"note":"2027 dates have not been published yet."},"acwb":{"name":"Canada Workers Benefit advance payments","dates":["2026-01-12","2026-07-10","2026-10-09"],"note":"2027 dates have not been published yet."}},"oas":{"threshold":95323,"rate":0.15,"income_year":2026,"max65":762.5,"max75":838.75,"defer":0.006,"full_years":40,"min_years":10,"inc75":0.1},"cpp":{"max65":1507.65,"avg65":858.34,"early":0.006,"late":0.007},"gst_credit":{"period":"July 2026 to June 2027","income_year":2025,"adult":445,"child":234,"single_supp":234,"supp_base":11564,"supp_rate":0.02,"threshold":46432,"reduce":0.05,"note":"From July 2026 this payment is the Canada Groceries and Essentials Benefit, which replaced the GST/HST credit with amounts 25% higher. The 2% phase-in of the single supplement and the 5% income reduction are set by the Income Tax Act for this benefit; CRA calculates your exact amount from your return."},"superficial":{"days":30},"pension":{"split_max":0.5,"amount":2000},"spousal":{"years":3,"lesser":true},"fedcred":{"age":9208.0,"age_thr":46432.0,"age_rate":0.15,"pension":2000.0},"ccb":{"period":"July 2026 to June 2027","income_year":2025,"max_u6":8157.0,"max_6_17":6883.0,"t1":38237.0,"t2":82847.0,"r1":[0.07,0.135,0.19,0.23],"b2":[3123.0,6022.0,8476.0,10260.0],"r2":[0.032,0.057,0.08,0.095],"cdb_max":3480.0,"cdb_t":82847.0,"cdb_r":[0.032,0.057]},"cdb":{"period":"July 2026 to June 2027","max_month":204.2,"A":1.021,"wie_single":10210.0,"wie_couple":14294.0,"t_single":23483.0,"t_couple":33182.5,"rate":0.2,"rate_both":0.1},"cwb":{"year":2026,"max_single":1665.0,"max_family":2869.0,"wit":3000.0,"phase_in":0.27,"po_single":27392,"po_family":31251,"po_rate":0.15,"sec_exempt":16714.0,"dis_max":860.0,"dis_wit":1150.0,"dis_po_single":38495.0,"dis_po_family":50377.0,"dis_rate":0.15,"dis_rate_both":0.075,"advance":0.5,"reconfigured":["AB","QC","NU"]},"gis":{"quarter":"October to December 2026","rows":[["single","Single, widowed or divorced, receiving OAS",1138.9,23112.0],["spouse_full_oas","Spouse or partner receives the full OAS pension",685.56,30528.0],["spouse_no_oas","Spouse or partner does not receive OAS",1138.9,55392.0],["spouse_allowance","Spouse or partner receives the Allowance",685.56,42768.0]],"allowance":[1448.06,42768],"survivor":[1726.18,31152.0]},"otb":{"period":"July 2026 to June 2027","income_year":2025,"lump":500.0,"energy_max":290.0,"pt_ns":[944,73],"pt_s":[581,617],"t_single_ns":29047.0,"t_family_ns":36309.0,"t_single_s":36309.0,"t_couple_s":43571.0,"oeptc_rate":0.02,"noec":[189.0,290.0,50833.0,65356.0,0.01],"ostc":[378.0,29047.0,36309.0,37273.0,0.04]},"ltt":{"ON":{"br":[[55000,0.005],[250000,0.01],[400000,0.015],[2000000,0.02],[null,0.025]],"fthb":4000.0},"TO":{"br":[[55000,0.005],[250000,0.01],[400000,0.015],[2000000,0.02],[3000000,0.025],[4000000,0.044000000000000004],[5000000,0.0545],[10000000,0.065],[20000000,0.0755],[null,0.086]],"fthb":4475.0},"BC":{"br":[[200000,0.01],[2000000,0.02],[null,0.03]],"extra_from":3000000,"extra":0.02,"fthb_full":835000.0,"fthb_part":500000.0,"fthb_max":8000.0,"fthb_zero":860000,"nbh_full":1100000.0,"nbh_zero":1150000.0},"QC":{"br":[[62900,0.005],[315000,0.01],[null,0.015]]},"MTL":{"br":[[62900,0.005],[315000,0.01],[552300,0.015],[1104700,0.02],[2136500,0.025],[3113000,0.035],[null,0.04]]},"QCC":{"br":[[62900,0.005],[315000,0.01],[500000,0.015],[750000,0.025],[null,0.03]]},"MB":{"br":[[30000,0.0],[90000,0.005],[150000,0.01],[200000,0.015],[null,0.02]]},"NB":{"rate":0.01},"NS":{"halifax":0.015},"PE":{"rate":0.01,"low":30000.0},"NL":{"base":100,"per100":0.4,"from":500,"mort_cap":5000.0},"AB":{"base":50.0,"per5000":5,"mort_base":50.0},"SK":{"transfer":[[500,0,"flat"],[6300,25.0,"flat"],[null,0.004,"rate"]],"mortgage":[[249999.99,200.0],[500000,275.0],[750000,525.0],[1000000,775.0],[null,1000.0]]}},"mortgage":{"insured_max":1500000,"premium_non_trad":0.045,"premiums":[[0.65,0.006],[0.75,0.017],[0.8,0.024],[0.85,0.027999999999999997],[0.9,0.031],[0.95,0.04]],"surcharge_30":0.002,"pst":{"ON":0.08,"QC":0.09,"SK":0.06},"pst_text":"in Ontario (8%), Quebec (9%, rising to 9.975% for premiums paid after December 31, 2026) and Saskatchewan (6%), provincial sales tax on the premium is paid in cash at closing and cannot be added to the loan.","buffer":0.02,"floor":0.0525,"gds":0.39,"tds":0.44},"payroll":{"year":2026,"cpp":{"ympe":74600.0,"exemption":3500.0,"base_rate":0.0495,"first_add_rate":0.01,"yampe":85000.0,"rate2":0.04,"max1":4230.45,"max2":416.0},"qpp":{"ympe":74600.0,"exemption":3500.0,"base_rate":0.053,"first_add_rate":0.01,"yampe":85000.0,"rate2":0.04,"max1":4479.3,"max2":416.0},"ei":{"mie":68900.0,"rate":0.0163,"rate_qc":0.013000000000000001,"max":1123.07,"max_qc":895.7},"qpip":{"mie":103000.0,"rate":0.0043,"max":442.9},"cea":1501.0,"k2p":{"AB":"lowest","BC":"lowest","MB":"lowest","NB":"lowest","NL":"lowest","NS":"lowest","NT":"lowest","NU":"lowest","ON":"lowest","PE":"lowest","SK":"lowest","YT":"lowest"},"qc_workers":{"rate":0.06,"max":1450.0}},"chequing":[{"name":"EQ Bank Personal Account","link":"/reviews/eq-bank/","fee":0,"fee_text":"$0","waive_bal":null,"rate":0.01},{"name":"Wealthsimple Chequing","link":"/reviews/wealthsimple/chequing/","fee":0,"fee_text":"$0","waive_bal":null,"rate":0.0125},{"name":"Manulife Bank Advantage Account","link":null,"fee":0,"fee_text":"$0; transaction fees below a $1,000 balance","waive_bal":1000,"rate":0.015},{"name":"KOHO Essential","link":null,"fee":0,"fee_text":"$7 a month, $0 with direct deposit or $1,000 a month in deposits","waive_bal":null,"rate":0.02},{"name":"Simplii No Fee Chequing Account","link":null,"fee":0,"fee_text":"$0","waive_bal":null,"rate":0.0},{"name":"Tangerine No-Fee Daily Chequing Account","link":null,"fee":0,"fee_text":"$0","waive_bal":null,"rate":0.0},{"name":"PC Money Account","link":null,"fee":0,"fee_text":"$0","waive_bal":null,"rate":0.0},{"name":"Neo Chequing","link":null,"fee":0,"fee_text":"$0","waive_bal":null,"rate":0.001},{"name":"National Bank The Connected","link":null,"fee":15.95,"fee_text":"$15.95 a month, $0 with a $4,500 balance","waive_bal":4500,"rate":0.0},{"name":"TD Unlimited Chequing Account","link":null,"fee":17.95,"fee_text":"$17.95 a month, $0 with a $4,000 daily balance","waive_bal":4000,"rate":0.0},{"name":"BMO Performance Chequing","link":null,"fee":17.95,"fee_text":"$17.95 a month, $0 with a $4,000 daily balance","waive_bal":4000,"rate":0.0},{"name":"CIBC Smart Account","link":null,"fee":16.95,"fee_text":"$16.95 a month, rebate with $4,000 every day","waive_bal":4000,"rate":0.0},{"name":"Scotiabank Preferred Package","link":null,"fee":16.95,"fee_text":"$16.95 a month, $0 with $4,000 every day","waive_bal":4000,"rate":0.0},{"name":"National Bank The Minimalist","link":null,"fee":3.95,"fee_text":"$3.95 a month (ages 25 and up)","waive_bal":null,"rate":0.0},{"name":"CIBC Everyday Chequing Account","link":null,"fee":4.0,"fee_text":"$4 a month","waive_bal":null,"rate":0.0},{"name":"Scotiabank Basic Bank Account","link":null,"fee":3.95,"fee_text":"$3.95 a month","waive_bal":null,"rate":0.0},{"name":"BMO Practical Chequing","link":null,"fee":4.0,"fee_text":"$4 a month","waive_bal":null,"rate":0.0},{"name":"RBC Day to Day Banking","link":null,"fee":4.0,"fee_text":"$4 a month","waive_bal":null,"rate":0.0},{"name":"TD Minimum Chequing Account","link":null,"fee":3.95,"fee_text":"$3.95 a month","waive_bal":null,"rate":0.0},{"name":"RBC Signature No Limit Banking","link":null,"fee":16.95,"fee_text":"$16.95 a month","waive_bal":null,"rate":0.0}],"hisa":[{"name":"Saven High Interest Savings","rate":0.0285,"ins":"DICO, up to $250,000"},{"name":"Oaken Savings Account","rate":0.028,"ins":"CDIC"},{"name":"EQ Bank 30 Day Notice Savings","link":"/reviews/eq-bank/","rate":0.0275,"rate_note":"30 days' notice to withdraw","ins":"CDIC"},{"name":"Hubert High Interest Savings","rate":0.025,"ins":"Deposit Guarantee Corporation of Manitoba"},{"name":"Wealthsimple Savings","link":"/reviews/wealthsimple/","rate":0.025,"ins":"CIPF, not CDIC"},{"name":"KOHO Essential","rate":0.02,"rate_note":"$7 a month plan, $0 with direct deposit","ins":"CDIC through partner institutions (opt-in)"},{"name":"Neo Savings (Essentials)","rate":0.02,"ins":"Not stated"},{"name":"Outlook High Interest Savings","rate":0.0195,"ins":"Deposit Guarantee Corporation of Manitoba"},{"name":"Manulife Bank Advantage Account","rate":0.015,"ins":"CDIC"},{"name":"Peoples Trust e-Savings","rate":0.012,"ins":"CDIC"},{"name":"Alterna High Interest eSavings","rate":0.0105,"ins":"CDIC"},{"name":"EQ Bank Personal Account","link":"/reviews/eq-bank/","rate":0.01,"rate_note":"2.75% with pay direct deposit","ins":"CDIC"},{"name":"RBC High Interest eSavings","rate":0.0055,"ins":"CDIC"},{"name":"National Bank High Interest Savings","rate":0.0055,"ins":"CDIC"},{"name":"Scotia MomentumPLUS Savings","rate":0.004,"rate_note":"base rate","ins":"CDIC"},{"name":"Simplii High Interest Savings","rate":0.003,"rate_note":"up to $50,000","ins":"CDIC"}],"usd_savings":[{"name":"EQ Bank US Dollar Account","link":"/reviews/eq-bank/","rate":0.025,"ins":"Not stated for USD on the product page"},{"name":"Manulife US Dollar Advantage Account","rate":0.002,"ins":"Not stated for USD on the product page"},{"name":"National Bank USD Progress Account","rate":0.001,"rate_note":"from $10,000","ins":"Not stated for USD on the product page"},{"name":"Scotia U.S. Dollar Daily Interest","rate":0.0005,"rate_note":"top tier","ins":"Not stated for USD on the product page"},{"name":"TD U.S. Daily Interest Chequing","rate":0.0001,"ins":"Not stated for USD on the product page"}],"gic_best":{"1":3.85,"2":4.25,"3":4.3,"4":4.35,"5":4.5},"gic_default_rate":3.85,"brokers":[{"id":"wealthsimple","name":"Wealthsimple","review":"/reviews/wealthsimple/trade/","cad_trade":0,"us_trade":0,"usd_reg_text":"TFSA, FHSA, RRSP, spousal RRSP, LIRA and RESP: $10 a month on Core, included on Premium and Generation","annual_fee":0,"opt_base":0,"opt_contract":0,"opt_min":0,"opt_text":"$0 per contract on US equity and ETF options","margin_cad":0.0495,"margin_text":"4.95% Core, 4.45% Premium, 3.95% Generation","transfer_in_text":"Reimburses the other institution's transfer-out fee, up to $150 per account, on transfers of $25,000 or more","transfer_min":25000,"transfer_max":150,"per_client":false,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","joint","corporate","fractional","drip","zero_commission","usd_reg"],"score":4.2},{"id":"questrade","name":"Questrade","review":"/reviews/questrade/","cad_trade":0,"us_trade":0,"usd_reg_text":"USD held in registered accounts at no extra cost","annual_fee":0,"opt_base":0,"opt_contract":0,"opt_min":0,"opt_text":"$0 on US equity options; Canadian options $0.99 per contract","margin_cad":0.087,"margin_text":"Prime + 4.25% under $100,000 (8.70%)","transfer_in_text":"Rebates the other institution's fee, up to $150 per account, on eligible transfers","transfer_min":null,"transfer_max":150,"per_client":false,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","joint","corporate","fractional","drip","zero_commission","usd_reg"],"score":4.3},{"id":"interactive-brokers","name":"Interactive Brokers Canada","review":"/reviews/interactive-brokers/","cad_trade":1.0,"us_trade":1.0,"usd_reg_text":"Not stated for registered accounts","annual_fee":0,"opt_base":0,"opt_contract":0.65,"opt_min":1.0,"opt_text":"US$0.65 per contract, minimum US$1","margin_cad":0.03675,"margin_text":"3.675% up to CAD 130,000 (IBKR Pro)","transfer_in_text":null,"transfer_min":null,"transfer_max":null,"per_client":false,"cad_text":"CAD 0.01 a share, minimum CAD 1","us_text":"USD 0.005 a share, minimum USD 1","flags":["tfsa","rrsp","spousal","fhsa","rrif","margin","joint","corporate","fractional","drip"],"score":4.2},{"id":"moomoo","name":"moomoo Canada","review":"/reviews/moomoo/","cad_trade":1.49,"us_trade":1.99,"usd_reg_text":"TFSA and RRSP can hold CAD and USD; no fee stated","annual_fee":0,"opt_base":0,"opt_contract":0.65,"opt_min":1.0,"opt_text":"US$0.65 per contract, minimum US$1","margin_cad":0.0385,"margin_text":"From 3.85% (as of November 3, 2025)","transfer_in_text":"Promotion: typically reimburses $100 on transfers of $10,000 or more","transfer_min":10000,"transfer_max":100,"per_client":true,"cad_text":"CA$0.0149 a share, minimum CA$1.49","us_text":"US$0.0099 a share, minimum US$1.99","flags":["tfsa","rrsp","spousal","margin","usd_reg"],"score":3.7},{"id":"webull","name":"Webull Canada","review":"/reviews/webull/","cad_trade":0,"us_trade":0,"usd_reg_text":"Not stated","annual_fee":8.4,"opt_base":0,"opt_contract":0.99,"opt_min":0,"opt_text":"US$0.99 per contract","margin_cad":0.0745,"margin_text":"Prime + 3% under $100,000 (7.45%)","transfer_in_text":"Transfer bonus of $150 (terms not published)","transfer_min":null,"transfer_max":null,"per_client":true,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","margin","zero_commission"],"score":3.2},{"id":"qtrade","name":"Qtrade Direct Investing","review":"/reviews/qtrade/","cad_trade":0,"us_trade":0,"usd_reg_text":"RRSP, RRIF and TFSA: US$15 a quarter per account (free with Investor Plus)","annual_fee":0,"opt_base":0,"opt_contract":0.75,"opt_min":0,"opt_text":"$0.75 per contract","margin_cad":0.06,"margin_text":"Prime + 1.55% under $100,000 (6.00%)","transfer_in_text":"Fall Offer 2026: up to $150 per client on transfers of $15,000 or more","transfer_min":15000,"transfer_max":150,"per_client":true,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","joint","corporate","drip","zero_commission","usd_reg"],"score":4.0},{"id":"national-bank","name":"National Bank Direct Brokerage","review":"/compare/best-online-brokers/","cad_trade":0,"us_trade":0,"usd_reg_text":"TFSA, RRSP, RRIF, spousal RRSP and LIRA (not FHSA); no USD fee listed","annual_fee":0,"opt_base":0,"opt_contract":1.25,"opt_min":6.25,"opt_text":"$1.25 per contract, minimum $6.25","margin_cad":0.0625,"margin_text":"6.25%","transfer_in_text":"Reimburses transfer fees depending on the amount (threshold not published)","transfer_min":null,"transfer_max":null,"per_client":false,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","corporate","drip","zero_commission","usd_reg"],"score":4.2},{"id":"cibc","name":"CIBC Investor's Edge","review":"/compare/best-online-brokers/","cad_trade":6.95,"us_trade":6.95,"usd_reg_text":"Not stated","annual_fee":0,"opt_base":6.95,"opt_contract":1.25,"opt_min":0,"opt_text":"$6.95 + $1.25 per contract","margin_cad":0.0625,"margin_text":"6.25% under $100,000","transfer_in_text":null,"transfer_min":null,"transfer_max":null,"per_client":false,"cad_text":"$6.95 ($0 under 25 with Smart Start)","us_text":"$6.95","flags":["tfsa","rrsp","fhsa","resp","rrif","lira","margin","joint","corporate","fractional"],"score":2.8},{"id":"td","name":"TD Direct Investing","review":"/reviews/td-direct-investing/","cad_trade":9.99,"us_trade":9.99,"usd_reg_text":"TD Easy Trade: no fee for USD in TFSA and RRSP; TD Direct Investing not stated","annual_fee":0,"opt_base":9.99,"opt_contract":1.25,"opt_min":0,"opt_text":"$9.99 + $1.25 per contract","margin_cad":null,"margin_text":"Not published","transfer_in_text":null,"transfer_min":null,"transfer_max":null,"per_client":false,"cad_text":"$9.99 (TD Easy Trade: 100 free trades a year)","us_text":"$9.99","flags":["tfsa","rrsp","fhsa","margin","fractional","drip"],"score":2.4},{"id":"rbc","name":"RBC Direct Investing","review":"/reviews/rbc-direct-investing/","cad_trade":9.95,"us_trade":9.95,"usd_reg_text":"Accounts can hold CAD and USD; USD registered pricing not stated","annual_fee":0,"opt_base":9.95,"opt_contract":1.25,"opt_min":0,"opt_text":"$9.95 + $1.25 per contract","margin_cad":null,"margin_text":"Not published","transfer_in_text":"Reimburses up to $200 of transfer fees on transfers of $15,000 or more","transfer_min":15000,"transfer_max":200,"per_client":true,"cad_text":"$9.95","us_text":"$9.95","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","joint","corporate","drip"],"score":2.7},{"id":"bmo","name":"BMO InvestorLine","review":"/compare/best-online-brokers/","cad_trade":0,"us_trade":0,"usd_reg_text":"Not stated","annual_fee":0,"opt_base":0,"opt_contract":0.9,"opt_min":0,"opt_text":"$0.90 per contract","margin_cad":null,"margin_text":"Not published","transfer_in_text":null,"transfer_min":null,"transfer_max":null,"per_client":false,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","fhsa","resp","rrif","lira","margin","joint","corporate","zero_commission"],"score":3.8},{"id":"scotia","name":"Scotia iTRADE","review":"/compare/best-online-brokers/","cad_trade":9.99,"us_trade":9.99,"usd_reg_text":"USD RRSP and RRIF available; no USD fee listed (TFSA and FHSA not stated)","annual_fee":0,"opt_base":9.99,"opt_contract":1.25,"opt_min":0,"opt_text":"$9.99 + $1.25 per contract","margin_cad":0.061,"margin_text":"Prime + 1.65% under $25,000 (6.10%)","transfer_in_text":"Newcomers (StartRight): credit of up to $150","transfer_min":null,"transfer_max":null,"per_client":true,"cad_text":"$9.99","us_text":"$9.99","flags":["tfsa","rrsp","fhsa","resp","rrif","lira","margin","corporate","usd_reg"],"score":2.6},{"id":"desjardins","name":"Desjardins Online Brokerage (Disnat)","review":"/compare/best-online-brokers/","cad_trade":0,"us_trade":0,"usd_reg_text":"USD RRSP, TFSA, LIRA, RRIF and LIF; no fee stated","annual_fee":0,"opt_base":0,"opt_contract":1.25,"opt_min":8.75,"opt_text":"$1.25 per contract, minimum $8.75","margin_cad":0.056999999999999995,"margin_text":"Prime + 1.25% under $100,000 (5.70%)","transfer_in_text":null,"transfer_min":null,"transfer_max":null,"per_client":false,"cad_text":"$0","us_text":"$0","flags":["tfsa","rrsp","spousal","fhsa","resp","rrif","lira","margin","corporate","zero_commission","usd_reg"],"score":4.3}],"robos":[{"name":"Questwealth Portfolios","review":"/reviews/questrade/","tiers":[[99999.99,0.0025],[null,0.002]],"tier_mode":"flat","mer":0.0012,"mer_text":"up to 0.12% (standard portfolios)","fee_text":"0.25%; 0.20% from $100,000","min":250},{"name":"Wealthsimple Managed Investing","review":"/reviews/wealthsimple/managed-investing/","tiers":[[99999.99,0.005],[null,0.004]],"tier_mode":"flat","mer":0.0015,"mer_text":"up to 0.15% (Classic portfolios)","fee_text":"0.5% Core; 0.4% Premium ($100,000+); 0.4% falling to 0.2% at $10M+ on Generation","min":1},{"name":"RBC InvestEase","review":"/reviews/rbc-direct-investing/","tiers":[[null,0.005]],"tier_mode":"flat","mer":0.002,"mer_text":"up to 0.20% (Core portfolios)","fee_text":"0.50% flat","min":100},{"name":"CI Direct Investing","review":null,"tiers":[[150000,0.006],[500000,0.004],[null,0.0035]],"tier_mode":"marginal","mer":0.0023,"mer_text":"up to 0.23% (ETF portfolios)","fee_text":"0.60% on the first $150,000; 0.40% on the next $350,000; 0.35% above $500,000","min":100}],"crypto":[{"name":"NDAX","link":null,"fee_pct":0.002,"fee_text":"0.20% flat"},{"name":"Wealthsimple Crypto","link":"/reviews/wealthsimple/crypto/","fee_pct":0.005,"fee_text":"0.5% plus a spread (no spread on limit orders)"},{"name":"Kraken","link":null,"fee_pct":0.01,"fee_text":"1% on app instant buys; Kraken Pro 0.40% maker, 0.80% taker"},{"name":"Newton","link":null,"fee_pct":0.0115,"fee_text":"Up to 1.15% on BTC, ETH and USDC; up to 1.60% on other coins"},{"name":"Coinbase Canada","link":null,"fee_pct":null,"fee_text":"Varies by payment method and order size; spread included in the price"},{"name":"Shakepay","link":null,"fee_pct":null,"fee_text":"No commission; spread of undisclosed size"},{"name":"Netcoins","link":null,"fee_pct":null,"fee_text":"No separate fee; spread of undisclosed size"},{"name":"Crypto.com","link":null,"fee_pct":null,"fee_text":"No app trading fee up to Level Up limits; spread may apply"},{"name":"Robinhood Canada (Coinsquare)","link":null,"fee_pct":null,"fee_text":"Fee schedule not published on the pages checked"}],"tax_software":[{"name":"Wealthsimple Tax","link":"/reviews/wealthsimple/tax/","netfile":true,"qc":true,"tiers":[{"name":"Basic","price_text":"Pay what you want, including $0 (up to 2 returns)","self":true,"rent":null,"inv":true,"help":false,"qc":true},{"name":"Plus","price_text":"$40 plus tax (included for Premium clients)","self":true,"rent":null,"inv":true,"help":false,"qc":true},{"name":"Pro","price_text":"$80 plus tax (included for Generation clients); 30-minute expert consultation","self":true,"rent":null,"inv":true,"help":true,"qc":false}]},{"name":"TurboTax Canada","netfile":true,"qc":true,"tiers":[{"name":"TurboTax Free","price_text":"$0 for simple returns","self":false,"rent":false,"inv":false,"help":false,"qc":true},{"name":"Do It Yourself","price_text":"Price depends on the complexity of your return","self":true,"rent":null,"inv":true,"help":false,"qc":true},{"name":"Expert Assist","price_text":"Price depends on the complexity of your return","self":true,"rent":null,"inv":true,"help":true,"qc":true}]},{"name":"H&R Block Canada","netfile":true,"qc":true,"tiers":[{"name":"Free","price_text":"$0 for returns that qualify","self":false,"rent":null,"inv":null,"help":false,"qc":true},{"name":"Self Employed","price_text":"Paid tier (price for the 2025 tax year not confirmed)","self":true,"rent":null,"inv":null,"help":false,"qc":true}]},{"name":"UFile","netfile":true,"qc":true,"tiers":[{"name":"UFile ONLINE","price_text":"From $20.95; free for students, first-time filers and family income under $20,000","self":null,"rent":null,"inv":null,"help":false,"qc":true},{"name":"UFile PREMIUM","price_text":"From $32.95","self":null,"rent":null,"inv":null,"help":false,"qc":true}]},{"name":"CloudTax","netfile":true,"qc":null,"tiers":[{"name":"Free","price_text":"$0 or pay what you want (up to 2 returns)","self":null,"rent":null,"inv":null,"help":false,"qc":null},{"name":"Review & File","price_text":"From $49 per return","self":null,"rent":null,"inv":null,"help":true,"qc":null}]},{"name":"GenuTax","netfile":true,"qc":null,"tiers":[{"name":"GenuTax Standard","price_text":"Free (donations optional)","self":null,"rent":null,"inv":null,"help":false,"qc":null}]},{"name":"StudioTax","netfile":true,"qc":null,"tiers":[{"name":"Mobile app","price_text":"Free","self":null,"rent":null,"inv":null,"help":false,"qc":null},{"name":"Computer download","price_text":"Paid; price not published","self":null,"rent":null,"inv":null,"help":false,"qc":null}]}],"tax_software_year":2025,"broker_features":[["tfsa","TFSA"],["rrsp","RRSP"],["spousal","Spousal RRSP"],["fhsa","FHSA"],["resp","RESP"],["rrif","RRIF"],["lira","LIRA or LIF"],["margin","Margin"],["joint","Joint account"],["corporate","Corporate account"],["usd_reg","USD in registered accounts"],["zero_commission","$0 stock and ETF commissions"],["fractional","Fractional shares"],["drip","DRIP"]],"ws_tiers":{"household":true,"list":[{"name":"Core","from":1,"perks":["Chequing interest 1.25% (1.75% with $2,000+ direct deposit in 30 days)","Managed investing fee 0.5%","USD account $10 a month","CAD margin 4.95%","Instant deposits up to $50,000"]},{"name":"Premium","from":100000,"perks":["Chequing interest 1.75% (2.25% with $2,000+ direct deposit in 30 days)","Managed investing fee 0.4% and tax-loss harvesting","USD account included","CAD margin 4.45%","Wealthsimple Tax Plus included","Priority phone support","Credit card monthly fee waived ($100,000+ in assets)"]},{"name":"Generation","from":500000,"perks":["Chequing interest 2.25%","Managed investing fee 0.4%, falling to 0.2% at $10,000,000+","USD account included","CAD margin 3.95%","Wealthsimple Tax Pro included","Priority phone and email support","Domestic wire fee waived"]}],"rows":[["Assets needed","$1","$100,000","$500,000"],["Chequing interest","1.25%","1.75%","2.25%"],["With $2,000+ direct deposit","1.75%","2.25%","2.25%"],["Managed investing fee","0.5%","0.4%","0.4%, down to 0.2%"],["USD account","$10 a month","Included","Included"],["CAD margin rate","4.95%","4.45%","3.95%"],["Wealthsimple Tax","Basic","Plus included","Pro included"]]},"cards":[{"name":"Wealthsimple Visa Infinite+","rate":0.02,"fee_month":20,"fee_note":"$20 a month, waived with $100,000+ in assets or $4,000+ a month in direct deposits"}]};
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
        else if (left < 0) h += msg('warnmsg', 'You are within the $2,000 lifetime buffer, so no penalty tax applies, but the extra amount is not deductible until you have new room.');
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
        var amt = Math.min(a.n('amt'), D.hbp.max), y = a.n('yr');
        var deferred = y >= D.hbp.deferral[0] && y <= D.hbp.deferral[1];
        var start = y + (deferred ? D.hbp.deferral_start : 2);
        var ann = amt / D.hbp.repay_years;
        var h = head('Minimum yearly repayment', money2(ann)) + kv([['First repayment year', String(start)], ['Last repayment year', String(start + D.hbp.repay_years - 1)], ['Repay by', 'within 60 days after December 31, ' + start]]);
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
          how('Uses the published rate for this loan size where a broker tiers its rates. Rates float with the prime rate or the broker\'s benchmark and change without notice. Margin interest on money borrowed to earn investment income in a non-registered account is generally tax-deductible.');
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
    var K = D.cards || [];
    shell(el, 'card-cashback', {
      title: 'Cash back calculator',
      intro: 'Your yearly cash back after the card fee, at your own spending.',
      fields: function (p) {
        return '<div class="ws-w-grid">' + fNum(p, 'spend', 'Monthly card spending', 2000, { min: 0 }) +
          fNum(p, 'rate', 'Cash back rate (%)', K[0] ? K[0].rate * 100 : 2, { min: 0, max: 10 }) +
          fNum(p, 'fee', 'Card fee per month', K[0] ? K[0].fee_month : 0, { min: 0, help: K[0] ? K[0].fee_note : '' }) + '</div>';
      },
      calc: function (a) {
        var yr = a.n('spend') * 12, cb = yr * a.n('rate') / 100, fee = a.n('fee') * 12, net = cb - fee;
        var be = a.n('rate') ? a.n('fee') / (a.n('rate') / 100) : 0;
        return head('Net cash back a year', money(net), net < 0) + kv([['Cash back earned', money(cb)], ['Card fees', money(fee)], ['Monthly spend to cover the fee', money(be)]]) +
          how('Cash back = yearly spending x the rate. Net = cash back minus fees. Fee waivers and caps on rewards are listed in the card review.');
      },
      next: [['/reviews/wealthsimple/visa-infinite-card/', 'Wealthsimple credit card review'], ['/reviews/wealthsimple/membership-tiers/', 'Wealthsimple tiers']]
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
          '<p class="ws-note">Not shown because no single fee is published: ' + D.crypto.filter(function (c) { return c.fee_pct == null; }).map(function (c) { return c.name + ' (' + c.fee_text + ')'; }).join('; ') + '.</p>' +
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
    var keys = which === 'all' ? Object.keys(B) : [which];
    shell(el, 'benefit-dates', {
      title: which === 'all' ? 'Next government payment dates' : 'Next ' + B[which].name + ' payment',
      intro: 'Today is ' + NOW.toLocaleDateString('en-CA', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }) + '.',
      button: false,
      fields: function (p) { return keys.length > 1 ? fSel(p, 'b', 'Benefit', keys.map(function (k) { return [k, B[k].name]; }), keys[0]) : ''; },
      calc: function (a) {
        var k = keys.length > 1 ? a.val('b') : keys[0], b = B[k];
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
  W['land-transfer-tax'] = function (el) {
    var LOC = [['ON', 'Ontario (outside Toronto)'], ['TO', 'Toronto'], ['BC', 'British Columbia'], ['QC', 'Quebec (provincial rates)'], ['MTL', 'Montreal'], ['QCC', 'Quebec City'], ['MB', 'Manitoba'], ['NB', 'New Brunswick'],
               ['NS', 'Nova Scotia'], ['PE', 'Prince Edward Island'], ['NL', 'Newfoundland and Labrador'], ['AB', 'Alberta'], ['SK', 'Saskatchewan'], ['YT', 'Yukon'], ['NT', 'Northwest Territories'], ['NU', 'Nunavut']];
    shell(el, 'land-transfer-tax', {
      title: 'Land transfer tax calculator',
      intro: 'Land transfer tax or registration fees on a home purchase, with first-time buyer rebates where they apply.',
      fields: function (p) {
        var d = PRESET.prov && D.provName[PRESET.prov] ? PRESET.prov : 'ON';
        return '<div class="ws-w-grid">' + fSel(p, 'loc', 'Where the home is', LOC, d) + fNum(p, 'price', 'Purchase price', 700000, { min: 0 }) +
          fNum(p, 'mort', 'Mortgage amount (Alberta, Saskatchewan and Newfoundland and Labrador registration fees)', 560000, { min: 0 }) +
          fRadio(p, 'ftb', 'First-time buyer?', [['n', 'No'], ['y', 'Yes']], 'y') + fRadio(p, 'nb', 'Newly built home (British Columbia)?', [['n', 'No'], ['y', 'Yes']], 'n') +
          fNum(p, 'assess', 'Assessed value, if higher than the price (New Brunswick and Prince Edward Island)', 0, { min: 0 }) +
          fNum(p, 'ns', 'Nova Scotia municipal deed transfer tax rate (%)', 1.5, { min: 0, max: 2, step: 0.05, help: 'Halifax charges 1.5%; other municipalities charge 1% to 1.5%.' }) + '</div>';
      },
      calc: function (a) {
        var T = D.ltt; if (!T) return msg('warnmsg', 'Figures are being confirmed.');
        var loc = a.val('loc'), price = a.n('price'), ftb = a.val('ftb') === 'y', rows = [], tax = 0, reb = 0, note = '', h;
        function addSlices(label, br) { var s = C.slices(br, price); s.rows.forEach(function (r) { rows.push([label, money(r[0]) + (r[1] === Infinity ? ' and up' : ' to ' + money(r[1])), pct(r[2], 2), money2(r[4])]); }); return s.total; }
        if (loc === 'ON' || loc === 'TO') {
          var on = addSlices('Ontario', T.ON.br); tax += on; if (ftb) reb += Math.min(T.ON.fthb, on);
          if (loc === 'TO') { var to = addSlices('Toronto', T.TO.br); tax += to; if (ftb) reb += Math.min(T.TO.fthb, to); }
          note = 'First-time buyers can get a refund of up to ' + money(T.ON.fthb) + ' of Ontario tax' + (loc === 'TO' ? ' and a rebate of up to ' + money(T.TO.fthb) + ' of Toronto tax' : '') + ' if they are 18 or older, have never owned a home anywhere, and move in within nine months.';
        } else if (loc === 'BC') {
          tax = addSlices('B.C.', T.BC.br);
          if (price > T.BC.extra_from) { var ex = (price - T.BC.extra_from) * T.BC.extra; rows.push(['B.C. further tax', 'Residential portion over ' + money(T.BC.extra_from), pct(T.BC.extra, 0), money2(ex)]); tax += ex; }
          if (a.val('nb') === 'y') { reb = price <= T.BC.nbh_full ? tax : (price < T.BC.nbh_zero ? tax * (T.BC.nbh_zero - price) / (T.BC.nbh_zero - T.BC.nbh_full) : 0); note = 'Newly built home exemption: full up to ' + money(T.BC.nbh_full) + ', reduced to $0 at ' + money(T.BC.nbh_zero) + '.'; }
          else if (ftb) { reb = price <= T.BC.fthb_part ? tax : (price <= T.BC.fthb_full ? T.BC.fthb_max : (price < T.BC.fthb_zero ? T.BC.fthb_max * (T.BC.fthb_zero - price) / (T.BC.fthb_zero - T.BC.fthb_full) : 0)); note = 'First-time buyers\' exemption: tax on the first ' + money(T.BC.fthb_part) + ' (up to ' + money(T.BC.fthb_max) + ') for homes up to ' + money(T.BC.fthb_full) + ', reduced proportionally to $0 at ' + money(T.BC.fthb_zero) + '.'; }
        } else if (loc === 'QC' || loc === 'MTL' || loc === 'QCC') {
          var base = Math.max(price, a.n('assess')), s = C.slices(T[loc].br, base); s.rows.forEach(function (r) { rows.push([loc === 'MTL' ? 'Montreal' : (loc === 'QCC' ? 'Quebec City' : 'Quebec'), money(r[0]) + (r[1] === Infinity ? ' and up' : ' to ' + money(r[1])), pct(r[2], 2), money2(r[4])]); }); tax = s.total;
          note = loc === 'QC' ? 'Municipalities may charge a higher rate (up to 3%) on the part above $500,000; Montreal and Quebec City do.' : 'The base is the greatest of the price paid, the price stated and the market value.';
        } else if (loc === 'MB') { tax = addSlices('Manitoba', T.MB.br); note = 'Manitoba charges this tax on the fair market value of the property on the date the transfer is registered.';
        } else if (loc === 'NB') { var b = Math.max(price, a.n('assess')); tax = b * T.NB.rate; rows.push(['New Brunswick', 'Greater of price and assessed value', pct(T.NB.rate, 0), money2(tax)]);
        } else if (loc === 'NS') { var r = a.n('ns') / 100; tax = price * r; rows.push(['Municipal deed transfer tax', 'Purchase price', pct(r, 2), money2(tax)]); note = 'Each municipality sets its own rate.';
        } else if (loc === 'PE') { var bp = Math.max(price, a.n('assess')); tax = bp <= T.PE.low ? 0 : bp * T.PE.rate; rows.push(['Prince Edward Island', 'Greater of price and assessed value', pct(T.PE.rate, 0), money2(tax)]); if (ftb) reb = tax; note = 'Qualifying first-time buyers are exempt; no tax applies at ' + money(T.PE.low) + ' or less.';
        } else if (loc === 'NL') { var d1 = T.NL.base + Math.ceil(Math.max(0, price - T.NL.from) / 100) * T.NL.per100, m = a.n('mort'), d2 = m > 0 ? Math.min(T.NL.mort_cap, T.NL.base + Math.ceil(Math.max(0, m - T.NL.from) / 100) * T.NL.per100) : 0; tax = d1 + d2; rows.push(['Deed registration', '$100 plus 40 cents per $100 over $500', '—', money2(d1)]); if (d2) rows.push(['Mortgage registration', 'Same scale, up to ' + money(T.NL.mort_cap), '—', money2(d2)]); note = 'Newfoundland and Labrador charges deed and mortgage registration fees on a purchase.';
        } else if (loc === 'AB') { var f1 = T.AB.base + T.AB.per5000 * Math.floor(price / 5000), mm = a.n('mort'), f2 = mm > 0 ? T.AB.mort_base + T.AB.per5000 * Math.floor(mm / 5000) : 0; tax = f1 + f2; rows.push(['Land title transfer', '$50 plus $5 for each $5,000 of value', '—', money2(f1)]); if (f2) rows.push(['Mortgage registration', '$50 plus $5 for each $5,000 of principal', '—', money2(f2)]); note = 'Alberta charges land titles registration fees. The fee schedule does not say how part of $5,000 is counted, so this estimate counts full $5,000 steps.';
        } else if (loc === 'SK' && T.SK) {
          var tf = 0, tt = T.SK.transfer; for (var j = 0; j < tt.length; j++) { if (tt[j][0] == null || price <= tt[j][0]) { tf = tt[j][2] === 'rate' ? price * tt[j][1] : tt[j][1]; break; } }
          var sm = a.n('mort'), mf = 0; if (sm > 0) { var mt = T.SK.mortgage; for (var q = 0; q < mt.length; q++) { if (mt[q][0] == null || sm <= mt[q][0]) { mf = mt[q][1]; break; } } }
          tax = tf + mf; rows.push(['Title transfer', price > 6300 ? '0.4% of the value' : 'Flat fee', price > 6300 ? '0.40%' : '\u2014', money2(tf)]); if (mf) rows.push(['Mortgage registration', 'Flat fee by mortgage amount', '\u2014', money2(mf)]);
          note = 'Saskatchewan charges land registry fees: 0.4% of the value of the title over $6,300, and a flat mortgage registration fee by amount.';
        } else { return msg('warnmsg', 'This calculator does not cover ' + LOC.filter(function (x) { return x[0] === loc; })[0][1] + ' yet.'); }
        h = head('Tax and fees on closing', money2(tax - reb)) + kv([['Before rebates', money2(tax)], ['First-time buyer or new home rebate', money2(reb)], ['Share of the price', pct(price ? (tax - reb) / price : 0, 2)]]);
        if (rows.length) h += table(['Tax', 'Portion of the price', 'Rate', 'Amount'], rows, 'How it is worked out');
        return h + (note ? how(note + ' Rates as of ' + fmtDate(D.asOf) + '. Other closing costs such as legal fees are extra.') : '');
      },
      next: [['/calculators/mortgage-affordability-calculator/', 'Mortgage affordability calculator'], ['/calculators/mortgage-payment-calculator/', 'Mortgage payment calculator']]
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
