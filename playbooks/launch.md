# 06 Launch — minimum safe deployment

## Readiness gate for **real users**

- Secure hosting: HTTPS, least privilege, separate secrets/config, a stable domain/URL and reasonable availability.
- Data: only collect necessary personal data; documented retention/deletion; reliable backup and restore procedure if storing user data.
- Money: reputable payment provider, clear currency/prices, consent, cancellation/refund/support process, verified payment event and webhook integrity.
- Observability: error monitoring, uptime checks, basic analytics/events, alerts and usage/budget ceilings.
- Testing: realistic path from signup to value to payment, rate-limit/abuse handling, rollback instructions.
- Compliance: check relevant Malaysian/international privacy, consumer, payments and platform obligations rather than assuming this template gives legal advice.

## Stage-appropriate infrastructure

Research locally → optionally static/demo hosting → low-maintenance managed runtime and DB for initial customers → redundancy/scale only when justified.

**Exit:** owner-approved release; record exact URL, change/commit, observability owner, costs and rollback path. No automatic deploy to prod without approval.
