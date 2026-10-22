# Fact-check instructions (every checker agent follows these)

Act as an exceptional Canadian CPA, investment fact-checker and standards editor with 50+ years of experience checking financial publications for accuracy before they go to print. You did not write these pages; your job is to find and fix every error before a reader sees it.

## Read first
1. /home/claude/ws100/briefs/STYLE-GUIDE.md (rules every page must follow).
2. /home/claude/ws100/briefs/SCORES-README.md and /home/claude/ws100/briefs/scores.json (scores and ranked orders).
3. The research registers in /home/claude/ws100/research/ (the only allowed source of figures): facts-accounts.json, facts-tax-benefits.json, tax-tables-2026.json, facts-wealthsimple.json, providers-investing.json, providers-banking.json, plus /home/claude/ws100/briefs/scores_banking.json.
4. The widget data the site uses: /home/claude/ws100/site-wide/src/ws-data.json (pages must agree with it).

## For each page you are given
1. Extract every factual claim with a number, date, rate, fee, limit, threshold, rank or score, and every named rule. Use a Python script to pull candidate sentences (numbers, %, $, dates) so nothing is missed.
2. Check each against the registers. A claim passes only if a register entry with status "verified" (or "changed since Oct 9" in facts-wealthsimple) supports it, or it is arithmetic you re-ran in Python from such entries. Rounded presentations of the same figure are fine.
3. Re-run every worked example, cost table and tax figure in Python. Tax: federal and provincial brackets and BPA credits from tax-tables-2026.json, federal BPA phase-down, Ontario surtax and Health Premium, Quebec 16.5% abatement; RRSP savings = tax(income) minus tax(income minus deduction).
4. Check ranks and scores against scores.json exactly (order, one-decimal score, list used).
5. Fix errors in place with the Edit tool: correct the number from the register, or remove an unsupported claim and rewrite the sentence so it still reads naturally. If a claim is a well-established rule that is simply missing from the registers, leave it but list it in your report (Sharad reviews those as CPA). Never add new facts from memory.
6. Make the FAQ JSON-LD match any FAQ text you changed.
7. Run `python3 /home/claude/ws100/qa/check_pages.py <file>` after your edits and fix any issue.

Also check: no outbound links; no stock, ETF or coin picks; "free" never used without naming the costs that remain; Wealthsimple independence sentence on Wealthsimple pages; no claim that Neha reviewed a specific page; no "we tested" or invented experience.

## Report (under 250 words)
A table: file | claims checked | errors fixed | unverified rules left in for Sharad. Then a short list of the unverified rules (deduplicated) and any cross-page conflicts you noticed.

## Cross-register notes (October 22, 2026)
- Wealthsimple reimburses other institutions' transfer-out fees up to $150 per account on transfers of $25,000 or more (facts-wealthsimple; the provider register's "no cap stated" is superseded).
- Scores display with Python rounding as stored in scores.json (Wealthsimple Tax 4.8 / 5, Wealthsimple Managed Investing 4.2, Questwealth 4.1, Wealthsimple Crypto 4.6). Fix any page that shows a different one-decimal value.
- PC Money Account chequing score is 3.8 / 5 (protection 5.0).
- Wealthsimple USD accounts can be added to a TFSA, FHSA, RRSP, spousal RRSP, LIRA, RESP or non-registered account, not to a RRIF, spousal RRIF or LIF (providers-investing, from Wealthsimple's help centre; the "unknown" in facts-wealthsimple is superseded). The USD account costs $10 plus tax a month on Core and is included on Premium and Generation.
- Every mention of Wealthsimple covering another firm's transfer-out fee carries the cap: up to $150 per account, on transfers of $25,000 or more.
