# Cost and approval policy

**Default cash expenditure authority: RM 0.** A suggested budget is not permission to spend.

## Cost ladder

1. **Free:** market desk research, competitor mapping, customer conversations, local prototype, manual concierge test.
2. **Cheap validation:** simple landing page, static hosting, limited paid trial of a tool only with explicit authorization.
3. **First paying users:** modest managed backend, hosted database/payment processor, backup and monitored usage.
4. **Scale after evidence:** invest in redundancy, observability and more automation as operational risk justifies it.

## Required spend request

- Purpose and hypothesis; audience; channel/provider
- Currency, total cap, daily cap, dates, and stop condition
- Expected signal and minimum interpretable sample
- Tracking plan and baseline; uncertainty about CAC/LTV
- Who approves and what access scope is needed

## Gates

- Never create an ad campaign, set it live, increase budget, charge a card or subscribe to a paid service without explicit owner approval.
- Human approval for production deployments, DNS changes, customer outreach under owner's name, personal data processing and irreversible actions.
- Use least-privilege tokens and spending/usage alerts where provided.
- Record actual cost in experiment results; distinguish spend from forecast.

## Unit economics

`CAC = attributable acquisition spend / acquired paying customers`

`CPS = attributable spend / new paying subscriptions`

`Contribution = collected revenue - payment fees - variable AI/hosting/support costs`

Compare **cohort retention and contribution-margin LTV** to CAC; do not assume gross billed price is realized profit. If there are zero paid users, CPS/CAC is **not measurable**, not zero.
