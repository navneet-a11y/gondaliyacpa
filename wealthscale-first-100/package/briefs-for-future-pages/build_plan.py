#!/usr/bin/env python3
"""Builds plan.json, plan.csv and links.csv for the WealthScale first-100 rebuild."""
import csv, json, os

OUT = os.path.dirname(os.path.abspath(__file__))

# id, url, h1, focus keyword, page type, year_in_title, publish_day, neha_scope, widgets, secondary keywords, must cover
P = []
def add(i, url, h1, kw, ptype, year, day, neha, widgets, sec, cover, notes=""):
    P.append(dict(id=i, url=url, h1=h1, focus_keyword=kw, page_type=ptype, year_in_title=year, publish_day=day,
                  neha_scope=neha, widgets=widgets, secondary_keywords=sec, must_cover=cover, notes=notes))

# ---------------- Day 1: home, trust, hubs, TFSA ----------------
add(1, "/", "Compare Canadian Investing Accounts, Platforms and Banking", "best investment platform canada", "home", "no", 1, "yes",
    "account-chooser, tfsa-room, benefit-dates",
    "best investing platform canada, online brokers canada, tfsa rrsp fhsa resp, best savings account canada, investment calculators canada",
    "Answer-first lead naming what WealthScale compares and the 2026 key limits; brand line 'Written by a CPA. Financial review by a CFA charterholder.'; "
    "key figures: 2026 TFSA limit, cumulative TFSA room since 2009, 2026 RRSP dollar limit, FHSA annual and lifetime limit, RESP CESG lifetime; "
    "account-chooser widget near the top; a section per hub (accounts, compare, reviews, versus, savings, banking, calculators, benefits, markets, learn) with ws-cards linking every child page in links.csv; "
    "top-ranked brokers, robo-advisors and savings rates from scores.json as a short table each with links; how WealthScale ranks (link methodology) and how it makes money; "
    "next CPP/OAS and GST/HST credit dates via benefit-dates; TFSA room widget teaser section; 'why trust us' section about the CPA writer and CFA charterholder reviewer; "
    "popular guides list; FAQ about who runs WealthScale, how rankings work, advice, update frequency, crypto coverage, cost to use the site",
    "Replace the current home page completely. Keep 'Compare. Choose. Grow.' as the eyebrow.")
add(2, "/about/", "About WealthScale", "wealthscale", "trust", "no", 1, "no", "",
    "about wealthscale, wealthscale media inc, who runs wealthscale",
    "Who we are (WealthScale Media Inc., federal corporation, 55 Queen St E, Suite 1205, Toronto); mission: compare Canadian investing accounts, platforms and banking on real costs; "
    "'Our reviewers' block with both people (photo, name, one-line credit, link); how pages are written (CPA) and reviewed (CFA charterholder for investing and account pages, Sharad gives final approval); "
    "what we cover (list of hubs with links); independence and how we make money (link); editorial standards (link); methodology (link); contact (link); "
    "what we do not do (no personal advice, no stock picks, no paid rankings); FAQ",
    "No widgets. 1,800 words.")
add(3, "/about/sharad-gondaliya/", "Sharad Gondaliya, CPA", "sharad gondaliya cpa", "profile", "no", 1, "no", "",
    "sharad gondaliya, sharadkumar gondaliya cpa, wealthscale cpa reviewer",
    "Use docs content word for word: full bio, education, writing, recognition, what Sharad does for WealthScale, areas of expertise, verify credentials table WITH the four verification links (allowed exception), LinkedIn link with rel=me; "
    "add the line 'Investing pages are also reviewed by Neha Gupta, CFA' linked to /about/neha-gupta/; section 'Pages Sharad wrote' with ws-cards to 12 key pages; Person JSON-LD from the bio file (ProfilePage graph like Neha's)",
    "Profile template. Writer uses /home/claude/ws100/briefs/people/sharad.md.")
add(101, "/about/neha-gupta/", "Neha Gupta, CFA", "neha gupta cfa", "profile", "no", 1, "no", "",
    "neha gupta cfa winnipeg, wealthscale financial reviewer, neha gupta whiteland real estate",
    "Use the approved profile text word for word (briefs/people/neha.md): headshot, H1, one-line role, three-paragraph bio, what Neha does for WealthScale (link Sharad), independence, education and credentials, areas of expertise, "
    "verify credentials table WITH the CFA Institute directory link (allowed exception), find Neha elsewhere links (LinkedIn, Insider Monkey, Investing in the Web) with rel='me noopener', last updated date and trademark line; "
    "ProfilePage + Person JSON-LD Block 1 with image https://wealthscale.ca/wp-content/uploads/ws/people/neha-gupta-cfa-400.jpg width 400 height 400",
    "Title tag 'Neha Gupta, CFA: Financial Reviewer'. Meta description exactly: Neha Gupta, CFA reviews WealthScale's investing pages. CFA charterholder in Winnipeg, in financial markets since 2005, with 2,600+ published articles.")
add(4, "/editorial-standards/", "Editorial Standards", "wealthscale editorial standards", "trust", "no", 1, "no", "",
    "how wealthscale writes, fact checking, financial review process",
    "Who writes (Sharad Gondaliya, CPA) and who reviews (Neha Gupta, CFA, a CFA charterholder, for investing and account pages; she checks fees, account features and investment terms against providers' own pages and regulator sources; Sharad gives final approval); "
    "the review-status line and what 'review scheduled' means; sources we use (described in words, no links): CRA, Service Canada, provincial governments, provider pricing pages, CIRO, CIPF, CDIC, the CSA; "
    "how figures are dated and re-checked (rates weekly, fees monthly, limits each January and when announced); corrections policy and how to report an error (contact page); general information only (NI 31-103); no stock picks; "
    "independence from advertisers; use of AI tools? say 'Every page is written and checked by people named on it' only if true; instead describe the human review steps; updates log section; FAQ",
    "Do not claim anything about process that is not in this plan.")
add(5, "/how-we-make-money/", "How WealthScale Makes Money", "wealthscale advertiser disclosure", "trust", "no", 1, "no", "",
    "advertiser disclosure, affiliate disclosure, partner links",
    "We may earn a commission when a reader opens an account through some labelled partner links; partner applications are in progress, so the site has no paid links yet; "
    "what payment never changes (inclusion, score, order, button style); how partner links will be labelled ('Partner link'); rel sponsored; reviewers' pay is a flat fee and never depends on rankings; no paid reviews, no sponsored rankings; how to tell us if something looks wrong; FAQ",
    "Be accurate: today there are no affiliate links on the site.")
add(6, "/contact/", "Contact WealthScale", "contact wealthscale", "trust", "no", 1, "no", "",
    "wealthscale email, report an error, media enquiries",
    "info@wealthscale.ca for general, corrections and media; privacy@wealthscale.ca for privacy requests (privacy officer: Sharad Gondaliya); mailing address; what we can and cannot help with (no personal advice, cannot access your accounts); "
    "how to report a wrong figure (page URL, the figure, where you saw the correct one); response time 'we aim to reply within two business days'; partnership enquiries; FAQ",
    "No phone number. No form widget.")
add(7, "/privacy-policy/", "Privacy Policy", "wealthscale privacy policy", "legal", "no", 5, "no", "",
    "wealthscale privacy, personal information, cookies",
    "Keep the existing lawyer-reviewed policy; only update: publisher WealthScale Media Inc. and address, privacy officer Sharad Gondaliya at privacy@wealthscale.ca, that calculators run in the browser and inputs are not sent to us (a browser may remember your birth year, province and income on your own device to prefill other calculators; clearing site data removes it), analytics only after consent",
    "LEGAL: Navneet publishes only after the lawyer review. Writer produces a draft of the changed sections only, clearly marked.")
add(8, "/terms-of-use/", "Terms of Use and Disclaimer", "wealthscale terms of use", "legal", "no", 5, "no", "",
    "wealthscale disclaimer, terms and conditions",
    "Keep the existing lawyer-reviewed terms; only update: publisher name and address, general information only (not financial, investment, tax or legal advice), calculators are estimates, no warranty on third-party rates and fees, reviewers' roles",
    "LEGAL: same as privacy policy.")
add(9, "/methodology/brokers/", "How We Rate Online Brokers and Robo-Advisors", "broker rating methodology", "trust", "no", 1, "yes", "broker-match",
    "how we rank brokers, broker scoring, robo-advisor ratings",
    "Publish the full scoring model from scores.json: six broker factors and weights, robo-advisor factors and weights, crypto, chequing and tax software factors; how each factor is measured from published pricing; "
    "category weights for 'best for US stocks', 'beginners', 'options', 'margin', 'TFSA', 'RRSP', 'FHSA', 'RESP'; how ties are broken; how often scores update; what we never use (affiliate status, ad spend); "
    "the current overall broker scores table and robo-advisor scores table; savings and GIC lists are sorted by rate, not score; how to challenge a score; FAQ",
    "Scores must match scores.json exactly.")
add(10, "/accounts/", "Investment Accounts in Canada: TFSA, RRSP, FHSA, RESP and More", "types of investment accounts canada", "hub", "no", 1, "yes", "account-chooser, tfsa-room",
    "registered accounts canada, tfsa vs rrsp vs fhsa, registered vs non-registered",
    "One section per account: TFSA, RRSP (and spousal RRSP), FHSA, RESP, RRIF, LIRA and LIF, non-registered, with 2026 limits, tax treatment in, during, out; a master comparison table of all accounts; "
    "which goal each account fits (account-chooser); order many Canadians use; US stocks in each account (withholding table); where to open each (link compare pages); ws-cards to every account guide and calculator",
    "")
add(11, "/compare/", "Compare Online Brokers and Investing Platforms in Canada", "compare online brokers canada", "hub", "no", 1, "yes", "broker-match, broker-cost",
    "online brokerage comparison canada, investing platforms canada, discount brokers canada",
    "Master broker comparison table (all brokers in providers-investing: CAD and US commissions, FX fee, USD registered accounts, FHSA, RESP, minimum, score); robo-advisor table; crypto platform table; "
    "how to choose (costs, accounts, US investing, tools, safety: CIRO and CIPF); ws-cards to every best-of and account-listing page; broker-cost widget",
    "")
add(12, "/reviews/", "Canadian Broker, Bank and Platform Reviews", "online broker reviews canada", "hub", "no", 1, "yes", "broker-match",
    "questrade review, wealthsimple review, eq bank review, broker reviews",
    "List every review page with its score and one-line verdict (ws-cards); what each review covers (fees, accounts, platform, safety, who it suits); how we review without paid placement; table of scores; FAQ",
    "")
add(13, "/vs/", "Broker Comparison: Any Two Platforms Side by Side", "broker comparison canada", "hub", "no", 1, "yes", "broker-cost",
    "wealthsimple vs questrade, tfsa vs rrsp, platform comparison",
    "Every versus page as ws-cards with the one-line winner by category; a side-by-side matrix of the main brokers; account-versus pages (TFSA vs RRSP, FHSA vs RRSP, FHSA vs TFSA, GIC vs HISA); how to compare two platforms in 6 steps; FAQ",
    "")
add(14, "/savings/", "Best Places to Save Money in Canada: Savings Accounts and GICs", "best place to save money canada", "hub", "no", 1, "yes", "hisa-earnings, gic-calc, savings-goal",
    "high interest savings canada, gic rates canada, where to keep emergency fund",
    "Top everyday savings rates and GIC rates tables (from providers-banking, dated); HISA vs GIC vs TFSA savings; CDIC coverage basics; emergency fund guidance (general); USD savings; ws-cards to savings pages",
    "")
add(15, "/banking/", "Bank Accounts in Canada Compared", "best bank account canada", "hub", "no", 1, "yes", "chequing-cost",
    "best chequing account canada, no fee bank account, online banks canada",
    "Chequing comparison table (monthly fee, waiver, interest, e-Transfer, CDIC); big banks vs online banks vs fintech; how to switch banks; deposit insurance; ws-cards to banking and savings pages",
    "")
add(16, "/calculators/", "Investing, Savings and Tax Calculators", "investment calculators canada", "hub", "no", 1, "yes", "income-tax",
    "tfsa calculator, rrsp calculator, tax calculator canada 2026, compound interest calculator canada",
    "Every calculator page as ws-cards with what it answers; embedded income-tax widget; a table of every 2026 rate and limit the calculators use (federal brackets, TFSA, RRSP, FHSA, RESP, RRIF factors at 71 to 75); how our calculators work (browser-only, no sign-up, nothing stored on our servers); FAQ",
    "")
add(17, "/benefits/", "CRA Benefit Payment Dates", "cra payment dates 2026", "hub", "yes", 1, "no", "benefit-dates, gst-credit, oas-clawback",
    "cra benefit payment dates, cpp payment dates, gst payment dates, canada groceries and essentials benefit, ccb payment dates, ontario trillium benefit payment dates",
    "Full 2026 (and 2027 where published) payment calendars for CPP and OAS, GST/HST credit, Canada Child Benefit, Ontario Trillium Benefit, Canada Workers Benefit advance, Canada Disability Benefit, in static tables; "
    "benefit-dates widget; what to do if a payment is late; direct deposit; amounts for the current benefit year; ws-cards to CPP/OAS and GST pages",
    "Every date from facts-tax-benefits only.")
add(18, "/markets/", "International Investing From Canada: World Markets", "international investing canada", "hub", "no", 1, "yes", "fx-cost, us-withholding",
    "investing in us stocks from canada, global investing canada, foreign stocks canada",
    "US market access from Canada (brokers, USD accounts, FX costs); withholding tax by account; other markets that Canadian brokers can access (from providers-investing: which brokers offer which exchanges); currency risk basics; foreign property reporting T1135 threshold (only if verified); ws-cards",
    "")
add(19, "/learn/", "Investing for Beginners in Canada", "investing for beginners canada", "hub", "no", 1, "yes", "compound-interest, account-chooser",
    "how to start investing canada, beginner investing, investing basics canada",
    "Step-by-step starting path: emergency savings, account choice, platform choice (DIY vs robo), what to hold (asset classes in general terms, no picks), costs, taxes; glossary of 30 terms; ws-cards to learn, account and compare pages",
    "")
add(20, "/calculators/tfsa-calculator/", "TFSA Contribution Room Calculator", "tfsa contribution room calculator", "calculator", "no", 1, "yes", "tfsa-room, tfsa-overcontribution, compound-interest",
    "tfsa calculator, how much tfsa room do i have, tfsa room by age, tfsa limit calculator",
    "Widget first; static table: TFSA room by birth year (born 1991 or earlier = full cumulative room, then each later birth year) as of 2026; newcomer rule; how withdrawals and re-contributions work; over-contribution tax; worked examples; how to check CRA My Account figure vs ours; FAQ",
    "")
add(28, "/accounts/tfsa/", "TFSA Guide: How a Tax-Free Savings Account Works", "tfsa", "account-guide", "no", 1, "yes", "tfsa-room, tfsa-overcontribution",
    "tax-free savings account, tfsa rules, tfsa limit 2026, tfsa withdrawal, what can you hold in a tfsa",
    "Everything about the TFSA: eligibility, room accrual, limits by year table, cumulative, newcomers and non-residents, withdrawals and re-contribution, over-contributions, qualified/non-qualified/prohibited investments, "
    "business-income risk for frequent trading, US stocks and withholding, successor holder vs beneficiary, multiple TFSAs and transfers, TFSA vs RRSP vs FHSA, where to open (link listing), strategies, example, FAQ",
    "")

# ---------------- Day 2: calculators and account guides ----------------
add(21, "/calculators/rrsp-calculator/", "RRSP Tax Refund Calculator", "rrsp calculator", "calculator", "no", 2, "yes", "rrsp-refund, rrsp-room, rrsp-withdrawal",
    "rrsp tax refund calculator, rrsp tax savings calculator, how much tax will i save rrsp",
    "Widget first; static table of tax saved on a $5,000 contribution at 6 income levels in ON, BC, AB, QC (compute with the tax tables in research; show arithmetic basis); marginal vs average; deadline for 2026 contributions; refund vs tax saved; RRSP room; withdrawals; FAQ",
    "Compute any static numbers with the same 2026 brackets the widget uses; run the arithmetic in Python before writing.")
add(22, "/calculators/fhsa-calculator/", "FHSA Calculator", "fhsa calculator", "calculator", "no", 2, "yes", "fhsa-room, fhsa-eligibility, first-home",
    "fhsa contribution calculator, fhsa carry forward, fhsa room calculator",
    "Room by opening year table; carry-forward examples; lifetime cap; deduction carry-forward; projected balance; FHSA plus HBP for couples; eligibility; closing deadline; FAQ", "")
add(23, "/calculators/resp-calculator/", "RESP Grant Calculator", "resp calculator", "calculator", "no", 2, "yes", "resp-grant",
    "resp grant calculator, cesg calculator, resp savings calculator",
    "Widget first; CESG rules table; A-CESG income thresholds; CLB; BC and Quebec grants; catch-up strategy table (contribution needed to get the maximum by age); projections; age 16 and 17 rule; FAQ", "")
add(24, "/calculators/rrif-calculator/", "RRIF Minimum Withdrawal Calculator", "rrif calculator", "calculator", "no", 2, "yes", "rrif-minimum",
    "rrif withdrawal calculator, rrif minimum calculator, rrif payment calculator",
    "Widget first; full factor table ages 55 to 95+; younger-spouse election; withholding above the minimum; RRIF timing (convert by end of year you turn 71, first minimum the following year); LIF note; FAQ", "")
add(25, "/calculators/compound-interest-calculator/", "Compound Interest Calculator", "compound interest calculator canada", "calculator", "no", 2, "yes", "compound-interest, savings-goal, fee-drag",
    "compound interest canada, investment growth calculator, savings growth calculator",
    "Widget first; formula explained; compounding frequency table for $10,000 at 5% over 10 years (compute exactly); rule of 72; effect of fees; taxes and why TFSA/RRSP matter; FAQ", "")
add(26, "/calculators/capital-gains-tax-calculator/", "Capital Gains Tax Calculator", "capital gains tax calculator canada", "calculator", "no", 2, "no", "capital-gains, dividend-tax, income-tax",
    "capital gains tax canada 2026, capital gains inclusion rate, how is capital gains taxed in canada",
    "Widget first; 2026 inclusion rate and the cancelled increase; ACB and selling costs; superficial loss rule; capital losses carry-back and forward; principal residence exemption basics; "
    "top marginal rate on capital gains by province (compute from tables); gains in registered accounts; T5008 and Schedule 3; FAQ", "")
add(27, "/calculators/currency-conversion-calculator/", "Brokerage Currency Conversion Fee Calculator", "currency conversion fee calculator", "calculator", "no", 2, "yes", "fx-cost, norberts-gambit",
    "broker fx fees canada, usd conversion fee, cad to usd broker fee",
    "Widget first; FX fee table by broker; how spreads work; USD accounts; Norbert's Gambit; cost on $1,000, $10,000, $50,000 (computed); FAQ", "")
add(29, "/accounts/tfsa-contribution-limit/", "TFSA Contribution Limit and Room by Year", "tfsa limit 2026", "account-guide", "yes", 2, "yes", "tfsa-room",
    "tfsa contribution limit, tfsa limit by year, cumulative tfsa limit 2026, tfsa limit 2027",
    "Static year-by-year limit table 2009 to 2026 with cumulative total; how indexing and rounding to $500 work; 2027 limit status (only if verified, else 'announced in late 2026'); room by birth year table; newcomers; over-contribution; FAQ", "")
add(30, "/accounts/tfsa-withdrawals/", "TFSA Withdrawal Rules", "tfsa withdrawal rules", "account-guide", "no", 2, "yes", "tfsa-room, tfsa-overcontribution",
    "tfsa withdrawal, re-contribute tfsa, tfsa withdrawal tax, how long tfsa withdrawal",
    "Withdrawals tax-free, room back January 1; re-contribution trap; transfers between institutions; withdrawals while non-resident; effects on benefits (none); timing tips; examples; FAQ", "")
add(31, "/accounts/us-stocks-in-tfsa/", "US Stocks in a TFSA: Withholding Tax and Currency Costs", "us stocks in tfsa", "account-guide", "no", 2, "yes", "us-withholding, fx-cost",
    "us dividends tfsa withholding tax, w-8ben tfsa, usd tfsa",
    "15% treaty withholding not recoverable in TFSA; RRSP exemption comparison; W-8BEN; US-listed vs Canadian-listed vs Canadian-wrapped (levels of withholding in general terms, no picks); FX costs and USD TFSA availability by broker table; US estate tax mention only if verified; FAQ", "")
add(32, "/accounts/rrsp/", "RRSP Guide: How a Registered Retirement Savings Plan Works", "rrsp", "account-guide", "no", 2, "yes", "rrsp-room, rrsp-refund, rrsp-withdrawal",
    "registered retirement savings plan, rrsp rules, rrsp deadline 2026, spousal rrsp, rrsp withdrawal",
    "Deduction and room; limits table; deadline; carry-forward; contributions vs deductions timing; spousal RRSP and attribution; withdrawals and withholding table; HBP and LLP; age 71 options; RRSP vs TFSA; US stocks treaty exemption; death and rollover basics; strategies; example; FAQ", "")
add(33, "/accounts/rrsp-contribution-limit/", "RRSP Contribution Limit", "rrsp contribution limit 2026", "account-guide", "yes", 2, "yes", "rrsp-room",
    "rrsp limit 2026, rrsp deduction limit, rrsp dollar limit by year, rrsp over contribution",
    "Dollar limit by year table (as far back as verified); 18% rule; PA and PAR; carry-forward; $2,000 buffer and 1% tax; group RRSP; where to find your number; examples; FAQ", "")
add(34, "/accounts/home-buyers-plan/", "RRSP Home Buyers' Plan: Limit, Rules and Repayment", "home buyers plan", "account-guide", "no", 2, "yes", "hbp-repayment, first-home",
    "hbp limit, home buyers plan repayment, rrsp first time home buyer, hbp and fhsa",
    "Current limit and date it applies from; first-time buyer test; qualifying home; 90-day contribution rule; repayment start and deferral for 2022 to 2025 withdrawals (as verified); Schedule 7; using with FHSA; couples; examples; FAQ", "")
add(35, "/accounts/fhsa/", "FHSA Guide: First Home Savings Account Rules", "fhsa", "account-guide", "no", 2, "yes", "fhsa-room, fhsa-eligibility, first-home",
    "first home savings account, fhsa rules, fhsa limit, fhsa withdrawal, fhsa deadline",
    "Eligibility; room and carry-forward; deductions and deduction carry-forward; qualifying withdrawal rules; what if you never buy (transfer to RRSP/RRIF); 15-year and age 71 limits; FHSA + HBP; couples; investments allowed; over-contribution; strategies; example; FAQ", "")
add(36, "/accounts/fhsa-eligibility/", "FHSA Eligibility: Who Counts as a First-Time Home Buyer", "fhsa eligibility", "account-guide", "no", 2, "yes", "fhsa-eligibility",
    "first time home buyer definition canada, fhsa first time home buyer, fhsa spouse owns home",
    "The four tests with examples; spouse rule details; newcomers; separation and divorce; age of majority; qualifying withdrawal vs opening tests; scenarios table (12 situations with yes/no); FAQ", "")
add(37, "/accounts/resp/", "RESP Guide: Grants, Limits and Withdrawals", "resp", "account-guide", "no", 2, "yes", "resp-grant",
    "registered education savings plan, resp rules, family vs individual resp, resp withdrawal",
    "Types of plans (family, individual, group in general terms); lifetime limit; grants overview; EAP vs PSE withdrawals; AIP and RRSP rollover; what if the child does not study; closing; self-directed vs group; where to open; FAQ", "")
add(38, "/accounts/resp-grants/", "RESP Grants: CESG, Additional CESG and Canada Learning Bond", "resp grant", "account-guide", "no", 2, "yes", "resp-grant",
    "cesg, canada education savings grant, canada learning bond, bctesg, qesi",
    "CESG rules and carry-forward table by age; A-CESG income thresholds 2026; CLB amounts and eligibility; BCTESG; QESI; age 16 and 17 rule; repayment of grants; maximize-grants contribution schedule; FAQ", "")
add(39, "/accounts/rrif-minimum-withdrawal/", "RRIF Minimum Withdrawal Table", "rrif minimum withdrawal", "account-guide", "no", 2, "yes", "rrif-minimum",
    "rrif minimum withdrawal table 2026, rrif withdrawal rules, rrif factors",
    "Full factor table; how the minimum is computed; younger spouse; timing; withholding; pension credit and splitting; converting RRSP to RRIF; LIF max/min note; example; FAQ", "")
add(95, "/markets/how-to-buy-us-stocks/", "How to Buy US Stocks in Canada and Cut FX Fees", "how to buy us stocks in canada", "markets-guide", "no", 2, "yes", "fx-cost, us-withholding, norberts-gambit",
    "buy us stocks canada, usd account, best way to buy us stocks canada",
    "Step-by-step: pick a broker with USD accounts, fund, convert (broker FX vs Norbert's Gambit vs USD deposits), place orders, taxes (withholding, foreign tax credit, T1135 only if verified), account placement, broker table; FAQ", "")
add(96, "/learn/how-to-invest/", "How to Invest in Canada: A Step-by-Step Guide", "how to invest in canada", "learn-guide", "no", 2, "yes", "account-chooser, compound-interest, fee-drag",
    "how to start investing in canada, investing for beginners, where to invest money canada",
    "Ten steps from budget to first trade; accounts; DIY vs robo vs advisor (fees compared); asset classes; diversification in general terms; costs; taxes; mistakes; FAQ (no picks)", "")

# ---------------- Day 3: Wealthsimple and learn ----------------
WS = "Opening sentence in hero: 'WealthScale is independent and not affiliated with Wealthsimple.' Facts only from facts-wealthsimple (verified)."
add(40, "/reviews/wealthsimple/", "Wealthsimple Review: Every Account, Fee and Product", "wealthsimple review", "ws-review", "no", 3, "yes", "ws-tier, broker-cost",
    "is wealthsimple good, wealthsimple pros and cons, wealthsimple fees, wealthsimple premium",
    "Every product (investing, managed, crypto, chequing, savings, USD, credit card, tax, mortgages, business) with fees by tier; tiers; safety; score from scores.json; pros/cons; vs Questrade and IBKR; who it suits; ws-cards to all 12 Wealthsimple pages; FAQ", WS)
add(41, "/reviews/wealthsimple/trade/", "Wealthsimple Trade Review: Self-Directed Investing", "wealthsimple trade review", "ws-review", "no", 3, "yes", "broker-cost, fx-cost",
    "wealthsimple self directed investing, wealthsimple trade fees, wealthsimple options", "Commissions; FX by tier; USD accounts; options; fractional; margin; accounts; app and web; limits; transfer coverage; safety; score; FAQ", WS)
add(42, "/reviews/wealthsimple/managed-investing/", "Wealthsimple Managed Investing Review", "wealthsimple managed investing review", "ws-review", "no", 3, "yes", "robo-fee, fee-drag",
    "wealthsimple robo advisor, wealthsimple managed fees, wealthsimple portfolios", "Fees by tier; portfolio types; MER; accounts; rebalancing and tax-loss harvesting; advice access; vs other robos table; score; FAQ", WS)
add(43, "/reviews/wealthsimple/chequing/", "Wealthsimple Chequing Review", "wealthsimple chequing review", "ws-review", "no", 3, "yes", "chequing-cost, deposit-insurance",
    "wealthsimple chequing interest rate, wealthsimple cash, wealthsimple chequing cdic", "Rates by tier and direct-deposit rule; fees; card; ATM reimbursement; CDIC via partner banks; e-Transfer, bill pay, cheques; overdraft; vs EQ Bank and big banks; FAQ", WS)
add(44, "/reviews/wealthsimple/visa-infinite-card/", "Wealthsimple Credit Card Review: Visa Infinite+", "wealthsimple credit card", "ws-review", "no", 3, "no", "card-cashback",
    "wealthsimple visa infinite, wealthsimple cash back card, wealthsimple credit card fee", "Cash back; fee and waiver; FX fee; insurance; eligibility; Privilege card; break-even math; vs other cash back cards only if verified data exists, otherwise skip; FAQ", WS)
add(45, "/reviews/wealthsimple/crypto/", "Wealthsimple Crypto Review", "wealthsimple crypto review", "ws-review", "no", 3, "yes", "crypto-fee",
    "wealthsimple crypto fees, wealthsimple staking, is wealthsimple crypto safe", "Fee or spread; coins; staking; transfers; regulation and custody; tax on crypto (general, link capital gains calculator); vs other CSA-authorized platforms; FAQ", WS)
add(46, "/reviews/wealthsimple/tax/", "Wealthsimple Tax Review", "wealthsimple tax review", "ws-review", "no", 3, "no", "tax-software-picker",
    "wealthsimple tax free, wealthsimple tax pricing, wealthsimple tax plus", "Pricing tiers; what each covers; expert help; NETFILE; Quebec; self-employed and rental; vs TurboTax and others table; FAQ", WS)
add(47, "/reviews/wealthsimple/fees/", "Wealthsimple Fees: Every Fee by Product and Tier", "wealthsimple fees", "ws-guide", "no", 3, "yes", "ws-tier, fx-cost",
    "wealthsimple fx fee, wealthsimple premium fees, wealthsimple transfer fee", "One master fee table by product and tier; FX; USD accounts; managed fees; crypto; card; transfer out; how to avoid each fee; FAQ", WS)
add(48, "/reviews/wealthsimple/is-wealthsimple-safe/", "Is Wealthsimple Safe? CIPF and CDIC Coverage", "is wealthsimple safe", "ws-guide", "no", 3, "yes", "deposit-insurance",
    "wealthsimple cipf, wealthsimple cdic, is wealthsimple legit", "Legal entities; CIRO; CIPF coverage and what it covers; CDIC for chequing via partner banks; crypto custody; ownership; security features (2FA etc. only if verified); what CIPF/CDIC do not cover; FAQ", WS)
add(49, "/reviews/wealthsimple/membership-tiers/", "Wealthsimple Core vs Premium vs Generation", "wealthsimple premium", "ws-review", "no", 3, "yes", "ws-tier",
    "wealthsimple generation, wealthsimple core, wealthsimple tiers", "Thresholds; every benefit by tier table; household rules; is upgrading worth it math (FX saving, managed fee saving, interest); FAQ", WS)
add(50, "/reviews/wealthsimple/usd-accounts/", "Wealthsimple USD Accounts Review", "wealthsimple usd account", "ws-review", "no", 3, "yes", "fx-cost, hisa-earnings[usd]",
    "wealthsimple usd tfsa, wealthsimple usd rrsp, wealthsimple usd savings", "USD accounts by account type; cost by tier; USD savings rates; conversion; withholding by account; FAQ", WS + " Use the usd variant: <div data-ws-widget=\"hisa-earnings\" data-list=\"usd\"></div>.")
add(51, "/reviews/wealthsimple/fhsa/", "Wealthsimple FHSA Review", "wealthsimple fhsa", "ws-review", "no", 3, "yes", "fhsa-room",
    "wealthsimple first home savings account, fhsa wealthsimple managed", "Self-directed vs managed FHSA; fees; transfers; promotions; FHSA rules recap; vs other FHSA providers table; FAQ", WS)
add(52, "/reviews/wealthsimple/tfsa/", "Wealthsimple TFSA Review", "wealthsimple tfsa", "ws-review", "no", 3, "yes", "tfsa-room",
    "wealthsimple tfsa fees, wealthsimple tfsa usd, wealthsimple tfsa transfer", "Self-directed, managed and crypto-in-TFSA status; USD TFSA; fees; transfers; TFSA rules recap; vs other TFSA providers; FAQ", WS)
add(86, "/vs/wealthsimple-vs-questrade/", "Wealthsimple vs Questrade", "wealthsimple vs questrade", "versus-platform", "no", 3, "yes", "broker-cost, fx-cost",
    "questrade or wealthsimple, wealthsimple questrade fees", "Side-by-side table (20+ rows); category winners; costs for 4 investor profiles (computed); accounts; USD; managed; safety; scores; FAQ", WS)
add(87, "/vs/wealthsimple-vs-interactive-brokers/", "Wealthsimple vs Interactive Brokers", "wealthsimple vs interactive brokers", "versus-platform", "no", 3, "yes", "broker-cost, fx-cost",
    "wealthsimple vs ibkr", "Same structure as Wealthsimple vs Questrade", WS)
add(88, "/vs/wealthsimple-vs-moomoo/", "Wealthsimple vs moomoo", "wealthsimple vs moomoo", "versus-platform", "no", 3, "yes", "broker-cost",
    "moomoo or wealthsimple", "Same structure as Wealthsimple vs Questrade", WS)
add(89, "/vs/wealthsimple-vs-eq-bank/", "Wealthsimple vs EQ Bank", "wealthsimple vs eq bank", "versus-platform", "no", 3, "yes", "hisa-earnings, chequing-cost",
    "eq bank or wealthsimple, wealthsimple chequing vs eq bank", "Chequing and savings side by side; rates; fees; cards; CDIC; USD; GICs; who suits which; FAQ", WS)
add(97, "/learn/norberts-gambit/", "Norbert's Gambit: Step-by-Step Guide", "norberts gambit", "learn-guide", "no", 3, "yes", "norberts-gambit, fx-cost",
    "norbert's gambit questrade, norbert's gambit wealthsimple, dlr dlr.u", "What it is; when it saves money (break-even); step-by-step per broker (journal process, from providers-investing); timing and settlement; tax (superficial loss, ACB in CAD); risks; FAQ", "")
add(98, "/learn/transfer-investment-account/", "How to Transfer a TFSA, RRSP or Investment Account", "how to transfer investment account", "learn-guide", "no", 3, "yes", "transfer-fee",
    "transfer tfsa to another bank, rrsp transfer, in-kind transfer, t2033", "Direct transfer vs withdrawal (TFSA room trap); forms by account type (T2033, T2151 only if verified); in-kind vs cash; timelines; fees and coverage table; partial vs full; step-by-step; FAQ", "")
add(99, "/benefits/cpp-oas-payment-dates/", "CPP and OAS Payment Dates", "cpp payment dates 2026", "benefit-dates", "yes", 3, "no", "benefit-dates[cpp_oas], cpp-start-age, oas-clawback",
    "oas payment dates 2026, cpp payment dates 2027, when is cpp paid, oas clawback 2026",
    "Static table of every 2026 and 2027 date (as verified); amounts for this quarter (CPP max and average, OAS 65-74 and 75+, GIS); OAS clawback threshold; deferral; how payments arrive; what if late; FAQ",
    "Use <div data-ws-widget=\"benefit-dates\" data-benefit=\"cpp_oas\"></div>.")

# ---------------- Day 4: listings ----------------
L = "Rank by scores.json for this list; one ws-rank card per provider; master comparison table wrapped in table-filter; ItemList JSON-LD."
add(53, "/compare/best-online-brokers/", "Best Online Brokers in Canada", "best online brokerage canada", "best-of", "yes", 4, "yes", "broker-match, broker-cost",
    "best online broker canada, best discount brokerage, cheapest online broker canada", "All 13 brokers ranked; best-for picks by category from scores.json; master table; costs for 4 investor profiles; how to choose; switching; safety; FAQ", L)
add(54, "/compare/best-robo-advisors/", "Best Robo-Advisors in Canada", "best robo advisor canada", "best-of", "yes", 4, "yes", "robo-fee, fee-drag",
    "robo advisor canada fees, cheapest robo advisor canada", "All robos ranked; fee table at $10k, $50k, $100k, $250k (computed); portfolio types; accounts; minimums; robo vs DIY vs advisor; FAQ", L)
add(55, "/compare/best-investing-apps/", "Best Investing Apps in Canada", "best investing app canada", "best-of", "yes", 4, "yes", "broker-match",
    "best stock trading app canada, investing apps canada", "Mobile-first brokers and robos ranked (app features from providers-investing only); fees; accounts; safety; FAQ", L)
add(56, "/compare/best-tfsa-accounts/", "Best TFSA Accounts in Canada", "best tfsa account canada", "account-listing", "yes", 4, "yes", "tfsa-room, broker-cost",
    "where to open a tfsa, best tfsa investment platform", "Self-directed, robo and savings TFSA options ranked; USD TFSA; fees; TFSA rules recap; FAQ", L)
add(57, "/compare/best-rrsp-accounts/", "Best RRSP Accounts in Canada", "best rrsp account canada", "account-listing", "yes", 4, "yes", "rrsp-refund",
    "where to open rrsp, best rrsp platform", "Ranked; spousal RRSP support; USD RRSP; RRIF conversion; fees; FAQ", L)
add(58, "/compare/best-fhsa-accounts/", "Best FHSA Accounts in Canada", "best fhsa account canada", "account-listing", "yes", 4, "yes", "fhsa-room",
    "where to open fhsa, best fhsa investment", "Ranked; self-directed vs managed vs savings FHSA; fees; FHSA rules recap; FAQ", L)
add(59, "/compare/best-resp-providers/", "Best RESP Providers in Canada", "best resp providers canada", "account-listing", "yes", 4, "yes", "resp-grant",
    "best resp account, family resp providers", "Ranked self-directed and robo RESPs (family and individual support); group plans explained in general terms; fees; grants handling; FAQ", L)
add(60, "/compare/best-brokers-for-us-stocks/", "Best Brokers for US Stocks in Canada", "best broker for us stocks canada", "best-of", "yes", 4, "yes", "fx-cost, us-withholding",
    "cheapest way to buy us stocks canada, usd account broker", "Ranked by the US-stocks weighting; USD account availability by account type; FX fees; Norbert's Gambit support; FAQ", L)
add(61, "/compare/best-commission-free-brokers/", "Best Commission-Free Trading Platforms in Canada", "commission free trading canada", "best-of", "yes", 4, "yes", "broker-cost",
    "zero commission broker canada, free stock trading canada", "Which brokers charge $0 on what; remaining costs (FX, ECN, options, transfers); ranked; FAQ", L)
add(62, "/compare/best-crypto-platforms/", "Best Crypto Exchanges and Platforms in Canada", "best crypto exchange canada", "best-of", "yes", 4, "yes", "crypto-fee",
    "crypto platforms canada, csa registered crypto exchange", "Only CSA-authorized platforms; ranked by crypto score; fees; coins; staking; custody; taxes (general); FAQ", L)
add(63, "/compare/best-brokers-for-beginners/", "Best Online Brokers for Beginners in Canada", "best brokerage for beginners canada", "best-of", "yes", 4, "yes", "broker-match, compound-interest",
    "easiest investing platform canada, beginner investing app", "Ranked by beginner weighting; minimums; fractional shares; recurring buys; education; FAQ", L)
add(64, "/compare/best-brokers-low-fx-fees/", "Brokers With the Lowest Currency Conversion Fees", "lowest fx fee broker canada", "best-of", "yes", 4, "yes", "fx-cost, norberts-gambit",
    "broker currency conversion fees, cheapest usd conversion canada", "FX fee table sorted by cost; cost at $10,000 (computed); USD accounts; Norbert's Gambit; FAQ", "Sorted by published FX cost (stated metric), not score. " + L)
add(65, "/compare/best-options-trading-platforms/", "Best Options Trading Platforms in Canada", "best options trading platform canada", "best-of", "yes", 4, "yes", "options-cost",
    "options trading canada fees, cheapest options broker canada", "Ranked by options weighting; per-contract fees; account types allowing options (TFSA/RRSP levels); tools; FAQ", L)
add(66, "/compare/best-margin-accounts/", "Lowest Margin Rates in Canada", "margin rates canada", "best-of", "yes", 4, "yes", "margin-interest",
    "margin account canada, lowest margin interest rate canada", "Margin rate table sorted by rate (stated metric); tiers; margin requirements basics; interest deductibility; risks; FAQ", "Sorted by published margin rate. " + L)
add(67, "/compare/best-tax-software/", "Best Tax Software in Canada", "best tax software canada", "best-of", "yes", 4, "no", "tax-software-picker",
    "free tax software canada, netfile software", "Ranked by tax-software score; prices by tier; free options with conditions; Quebec; expert help; FAQ", L)
add(68, "/compare/best-tfsa-for-us-stocks/", "Best TFSA Accounts for US Stocks", "best tfsa account for us stocks", "account-listing", "no", 4, "yes", "us-withholding, fx-cost",
    "usd tfsa account, us stocks tfsa canada", "Ranked; USD TFSA availability and cost; FX; withholding recap; FAQ", L)
add(69, "/compare/best-rrsp-for-us-stocks/", "Best RRSP Accounts for US Stocks", "best rrsp for us stocks", "account-listing", "no", 4, "yes", "us-withholding, fx-cost",
    "usd rrsp account, us dividends rrsp", "Ranked; treaty exemption; USD RRSP availability and cost; FAQ", L)
add(70, "/compare/best-self-directed-resp/", "Best Self-Directed RESP Accounts", "best self directed resp account", "account-listing", "no", 4, "yes", "resp-grant",
    "self directed resp canada, family resp online broker", "Ranked; family vs individual support; grants applied (CESG, CLB, BC, QC) by provider where verified; fees; FAQ", L)
add(71, "/compare/best-rrif-accounts/", "Best RRIF Accounts in Canada", "best rrif account", "account-listing", "no", 4, "yes", "rrif-minimum",
    "self directed rrif, rrif providers canada", "Ranked; RRIF availability and fees; withdrawal scheduling; FAQ", L)
add(72, "/compare/best-lira-accounts/", "Best LIRA Accounts in Canada", "best lira account", "account-listing", "no", 4, "yes", "rrif-minimum",
    "self directed lira, lira to lif", "Ranked; LIRA and LIF availability; locked-in rules in general terms (provincial differences, unlocking only if verified); FAQ", L)

# ---------------- Day 5: banking, savings, reviews, versus, GST, legal ----------------
add(73, "/banking/best-chequing-accounts/", "Best Chequing Accounts in Canada", "best chequing account canada", "best-of", "yes", 5, "yes", "chequing-cost",
    "chequing account canada, best bank account canada, high interest chequing", "Ranked by chequing score; fee and waiver table; interest; e-Transfers; ATM; welcome offers with end dates; FAQ", L)
add(74, "/banking/best-no-fee-chequing-accounts/", "Best No-Fee Chequing Accounts in Canada", "no fee chequing account", "best-of", "yes", 5, "yes", "chequing-cost",
    "free chequing account canada, no monthly fee bank account", "Only $0-monthly-fee accounts; what can still cost money; ranked; FAQ", L)
add(75, "/savings/high-interest-savings-accounts/", "Best High-Interest Savings Accounts in Canada", "best high interest savings account canada", "rates", "yes", 5, "yes", "hisa-earnings, savings-goal",
    "high interest savings account canada, best savings rates canada, hisa rates", "Rate table sorted by everyday rate (dated); promo rates with terms; deposit insurance; TFSA savings; how interest is taxed; FAQ", "Sorted by everyday rate.")
add(76, "/savings/usd-savings-accounts/", "Best USD Savings Accounts in Canada", "usd savings account canada", "rates", "no", 5, "yes", "hisa-earnings[usd]",
    "us dollar savings account canada, usd hisa", "USD rate table; CDIC coverage of USD deposits (only as verified); fees; tax in CAD; FAQ", "Use <div data-ws-widget=\"hisa-earnings\" data-list=\"usd\"></div>.")
add(77, "/savings/gic-rates/", "Best GIC Rates in Canada", "best gic rates canada", "rates", "yes", 5, "yes", "gic-calc, gic-ladder",
    "gic rates today, 1 year gic rates, 5 year gic rates, cashable gic", "Best rate by term table (dated); big bank posted rates; cashable vs non-redeemable; registered GICs; ladder; CDIC; FAQ", "Sorted by rate.")
R = "Review template; Review JSON-LD with score from scores.json."
add(78, "/reviews/questrade/", "Questrade Review", "questrade review", "review", "yes", 5, "yes", "broker-cost, fx-cost", "questrade fees, questrade fx fee, questwealth", "Full review per template", R)
add(79, "/reviews/interactive-brokers/", "Interactive Brokers Canada Review", "interactive brokers canada review", "review", "yes", 5, "yes", "broker-cost, margin-interest", "ibkr canada fees, interactive brokers tfsa", "Full review", R)
add(80, "/reviews/moomoo/", "moomoo Canada Review", "moomoo canada review", "review", "yes", 5, "yes", "broker-cost", "moomoo fees canada, moomoo tfsa", "Full review", R)
add(81, "/reviews/webull/", "Webull Canada Review", "webull canada review", "review", "yes", 5, "yes", "broker-cost", "webull fees canada, webull tfsa", "Full review", R)
add(82, "/reviews/qtrade/", "Qtrade Direct Investing Review", "qtrade review", "review", "yes", 5, "yes", "broker-cost", "qtrade fees, qtrade guided portfolios", "Full review", R)
add(83, "/reviews/td-direct-investing/", "TD Direct Investing Review", "td direct investing review", "review", "yes", 5, "yes", "broker-cost, transfer-fee", "td direct investing fees, td easy trade", "Full review incl. TD Easy Trade", R)
add(84, "/reviews/rbc-direct-investing/", "RBC Direct Investing Review", "rbc direct investing review", "review", "yes", 5, "yes", "broker-cost", "rbc direct investing fees, rbc investease", "Full review", R)
add(85, "/reviews/eq-bank/", "EQ Bank Review", "eq bank review", "review", "yes", 5, "yes", "hisa-earnings, gic-calc", "eq bank personal account, eq bank gic rates, eq bank usd", "Full review of EQ Bank accounts, GICs, USD, cards", R)
add(90, "/vs/questrade-vs-interactive-brokers/", "Questrade vs Interactive Brokers", "questrade vs interactive brokers", "versus-platform", "no", 5, "yes", "broker-cost, options-cost", "questrade or ibkr", "Same structure as Wealthsimple vs Questrade", "")
add(91, "/vs/tfsa-vs-rrsp/", "TFSA vs RRSP: Which Should You Use First?", "tfsa vs rrsp", "versus-account", "no", 5, "yes", "tfsa-vs-rrsp, rrsp-refund",
    "rrsp or tfsa, tfsa or rrsp first", "Side-by-side table (20 rows); marginal rate logic with computed examples at 4 incomes; benefits clawback; matching; HBP/FHSA interplay; decision rules; FAQ", "")
add(92, "/vs/fhsa-vs-rrsp/", "FHSA vs RRSP Home Buyers' Plan", "fhsa vs rrsp", "versus-account", "no", 5, "yes", "first-home, hbp-repayment",
    "fhsa or hbp, fhsa and rrsp together", "Side-by-side; using both; couples maximum; repayment vs no repayment; examples; FAQ", "")
add(93, "/vs/fhsa-vs-tfsa/", "FHSA vs TFSA for a Down Payment", "fhsa vs tfsa", "versus-account", "no", 5, "yes", "first-home, fhsa-room",
    "fhsa or tfsa for house, down payment savings canada", "Side-by-side; deduction value; flexibility; what if you do not buy; order of use; examples; FAQ", "")
add(94, "/vs/gic-vs-hisa/", "GIC vs High-Interest Savings Account", "gic vs hisa", "versus-account", "no", 5, "yes", "gic-calc, hisa-earnings",
    "gic or savings account, gic vs savings account canada", "Rates compared (dated); liquidity; CDIC; ladders; tax; registered options; examples; FAQ", "")
add(100, "/benefits/gst-hst-credit/", "GST/HST Credit: Payment Dates and Amounts", "gst payment dates 2026", "benefit-dates", "yes", 5, "no", "benefit-dates[gst], gst-credit",
    "canada groceries and essentials benefit, cgeb payment dates, gst hst credit 2026, gst credit amount, gst payment dates 2027",
    "Static table of payment dates (2026 and 2027 as verified); amounts for the current benefit year; eligibility; how it is calculated (income threshold, reduction); the July 2026 replacement of the GST/HST credit by the Canada Groceries and Essentials Benefit (CGEB), the 25% increase and the June 2026 one-time top-up, exactly as verified; provincial add-ons paid with it (only verified); late payment steps; FAQ",
    "Use <div data-ws-widget=\"benefit-dates\" data-benefit=\"gst\"></div>.")

def slug(url):
    s = url.strip('/').replace('/', '-')
    return s or 'home'

for p in P:
    p['slug'] = slug(p['url'])
    p['file'] = f"{p['id']:03d}-{p['slug']}.html"
    parts = p['url'].strip('/').split('/')
    p['wp_parent'] = ('/' + '/'.join(parts[:-1]) + '/') if len(parts) > 1 else ''

ids = [p['id'] for p in P]
assert len(ids) == len(set(ids)) == 101, (len(ids), len(set(ids)))
P.sort(key=lambda x: (x['publish_day'], x['id']))
for d in range(1, 6):
    print('day', d, sum(1 for p in P if p['publish_day'] == d))

json.dump(P, open(os.path.join(OUT, 'plan.json'), 'w'), indent=1)
with open(os.path.join(OUT, 'plan.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['id', 'publish_day', 'url', 'file', 'wp_parent', 'h1', 'focus_keyword', 'secondary_keywords', 'page_type', 'year_in_title', 'neha_scope', 'widgets', 'must_cover', 'notes'])
    w.writeheader()
    for p in P:
        w.writerow({k: p[k] for k in w.fieldnames})
with open(os.path.join(OUT, 'links.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['id', 'url', 'h1', 'focus_keyword', 'page_type'])
    for p in sorted(P, key=lambda x: x['id']):
        w.writerow([p['id'], p['url'], p['h1'], p['focus_keyword'], p['page_type']])
print('ok', len(P))
