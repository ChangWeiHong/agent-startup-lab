# Marketing & advertising — repeatable experiment SOP

**Goal:** discover paid demand and viable acquisition economics, not maximize clicks. Ads are a **customer acquisition cost**, not an ad-revenue business model.

## Channel choice

| Context | Start with | Why |
| --- | --- | --- |
| Reachable vertical B2B / Malaysia local businesses | direct conversation, demo and paid pilot ask | cheapest qualified learning |
| Consumer idea pre-product | useful organic content, interactive landing page, manual demo | validates message before extensive build |
| Live iOS product with search demand | Apple Ads / Search Ads small keyword test | search intent; requires eligible store listing |
| Demonstrable visual consumer pain | capped Meta / TikTok creative experiment | message/angle discovery; verify platform policies and current minimum spend |
| Long-lived search queries | helpful SEO page / keyword research | slower but testable |

Platform spend minimums, CPC/CPI benchmarks and attribution capabilities change; verify current rules per country before buying.

## Creative preparation

Write the buyer problem in one sentence and the product action in one sentence. Prepare variants around **one changed variable** at a time:
- hook (first seconds / first line);
- pain framing vs demonstrated outcome;
- short user-style video vs product demo screenshot;
- local Malay/English/Chinese wording where relevant.

Each creative receives `creative_id`, script/asset link, audience, hypothesis and version. Do not fabricate testimonials or app capabilities.

## Measurement contract

Map `campaign_id → creative_id → attributable visit/install → activation → verified paid subscription → repeat use / renewal` where technically possible. Capture UTM parameters for web paths; use platform-compatible install and purchase attribution with consent and documented blind spots. RevenueCat or equivalent can help **only when supported by the product's subscription architecture**.

Record:
- spend + currency + attribution window;
- impressions, clicks, unique landing visits, installs, activations, trial starts;
- **verified paid conversions**, refunds, renewals and cancelled subscriptions;
- cohort date, geography, channel, creative and limits.

Formulas:
- `CTR = clicks / impressions`
- `CPC = spend / clicks`
- `CPI = spend / installs`
- `CPS = attributable spend / verified new paying subscribers`
- `CAC = attributable customer-acquisition spend / acquired paying customers`

If no paid subscriptions are observed, **CPS is undefined/not measurable**, not zero. Short tests cannot reliably establish LTV or profitability.

## Experiment procedure

1. Select a single falsifiable message / audience / price hypothesis.
2. Write a [validation plan](../../templates/experiment.md) with a clear metric and stopping rules.
3. Propose maximum total spend, daily spend, dates, billing entity and hard stop; obtain **human approval** before enabling ads.
4. Use correctly tracked campaigns and clearly versioned creatives. Check activation/purchase events work before launch.
5. Run only within approved scope; monitor spend and policy issues. Small sample results are exploratory.
6. Compare subscribers and quality of customers, not just low CPI or high CTR. Segment by attribution limitations.
7. Document observations and decision in GitHub. If potentially promising, **replicate** before increasing budget.

## Statistical discipline

No universal “50 conversions makes a test significant” rule exists. Estimate sample needs from desired effect size, baseline and uncertainty; make low-budget decisions as directional evidence, not statistical proof. Also avoid changing audience, price and hook all at once then attributing outcome to a single factor.

## Knowledge update

After each completed experiment, copy only generalized **tested lessons** here, referencing the experiment and date. Do not overwrite original measurements or claim a result outside its observed audience.
