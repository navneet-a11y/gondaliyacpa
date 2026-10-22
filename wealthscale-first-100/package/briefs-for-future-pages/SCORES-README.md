# How to use scores.json (October 22, 2026)

File: /home/claude/ws100/briefs/scores.json. Never change a score or an order. Show scores to one decimal as "4.4 / 5".

- `brokers`: one row per broker with `sub` (sub-scores 0 to 5: cost, accounts, us, cash_margin, platform, beginner_platform, safety, options_cost), `profile_costs` (yearly cost in dollars for the active profile, the buy-and-hold profile and the options profile) and unrounded scores `score_overall`, `score_us_stocks`, `score_beginners`, `score_options`.
- `broker_lists`: the exact ranked order for each list page:
  - `best-online-brokers` (overall), `best-brokers-for-us-stocks`, `best-brokers-for-beginners`, `best-options-trading-platforms`, `best-commission-free-brokers`, `best-investing-apps`.
  - `brokers-offering-tfsa`, `-rrsp`, `-fhsa`, `-resp`, `-rrif`, `-lira`: brokers that offer that account, by overall score. Use these on the account listing pages.
  - `best-tfsa-for-us-stocks`, `best-rrsp-for-us-stocks`: by the US-stocks score.
  - `lowest-fx-fees_by_cost_on_10000` (sorted by cost on $10,000, the stated metric) and `lowest-fx-fees_not_published`.
  - `margin-rates_by_rate` (sorted by CAD margin rate, the stated metric) and `margin-rates_not_published`.
- `robos`: four ranked robo-advisors (management fee and fund costs both published) with `total_cost_pct_at_50000`; `robos_not_ranked`: robo-advisors listed separately with the reason. Account listing pages may add a short "managed options" section that lists the ranked robos offering that account (check `accounts_text` in /home/claude/ws100/site-wide/src/providers-widget-data.json).
- `crypto`: nine CSA-authorized platforms ranked by the crypto score.
- `tax_software`: seven NETFILE-certified products ranked by the tax software score.
- `chequing` and `no_fee_chequing_order`: chequing ranks (see scores_banking.json).
- `methodology`: the exact published rubric text and weights. The methodology page prints these rules in plain words; other pages summarize them in one or two sentences and link /methodology/brokers/.

Facts about each provider come from /home/claude/ws100/research/providers-investing.json (and facts-wealthsimple.json for Wealthsimple). Values marked "unknown", "conflict" or "not stated" are written as "not published" in tables; never fill them in. The widget data in /home/claude/ws100/site-wide/src/providers-widget-data.json holds the same numbers in structured form (commission per trade on a 40-share order, FX rate, options pricing, margin rate, transfer policy) and is handy for Python calculations.

Review pages: a provider's review score is its `score_overall` (brokers), robo `score` (robo-advisors) or chequing score (banks). The Questrade review also covers Questwealth Portfolios, the RBC Direct Investing review also mentions RBC InvestEase, and the TD review covers TD Easy Trade, each with its own scores where they exist.

## Rounding (added October 22, 2026)
Always show the one-decimal value already in the file: `score` in each `broker_lists` entry, `display_overall` / `display_us_stocks` / `display_beginners` / `display_options` on broker rows, and `score_1dp` on robos, crypto and tax_software. These use Python's round(), so for example Wealthsimple Tax shows 4.8 / 5 (unrounded 4.85). Never round the unrounded values yourself.
