# Lean hosting, security and operational baseline

## Phases

| Stage | Default | Security minimum |
| --- | --- | --- |
| Research | local files / GitHub | no secrets or real customer PII in Git |
| Prototype | local-first; static hosting for feedback | HTTPS for public URLs, no embedded keys |
| First real users | reliable managed runtime/database where needed | backups, least privilege, monitoring, privacy, cost alerts, rollback |
| Repeat revenue | invest based on measured reliability / usage | incident handling, restore tests, patching, rate limits, payments reconciliation |

Favor a small monolith and managed services over Kubernetes/microservices for early experiments. “Free” hosting is not justification for unsafe authentication or no backups.

## Real-user release checklist

- AuthN/AuthZ for protected data, server-side input validation, least-privilege secrets and service accounts.
- Payment provider with verified webhook signatures, idempotency and explicit billing/cancellation terms.
- Data minimization and access-controlled storage; privacy notice where required; relevant jurisdictions/platform policies checked.
- Backups tested for restore; errors/uptime tracked; spend cap and incident contact documented.
- Repeatable deployment with rollback; separate testing/production configuration when necessary.
- Support contact and user data deletion path available if collecting user data.

No ad-account token, raw customer transaction, secret or contact list belongs in the **public** Venture OS repo. Store only anonymized summaries and private references.
