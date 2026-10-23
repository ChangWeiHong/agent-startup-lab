---
name: prd-engineering
description: Implement approved PRD tasks safely using a coding agent
---

# prd-engineering

**Use when:** Implement approved PRD tasks safely using a coding agent

## Inputs
- Approved PRD + linked Issue
- Product repository and relevant code
- Acceptance criteria, tests, risk and rollout guardrails

## Steps
1. Inspect only scoped files and dependency instructions
2. Work on isolated branch/worktree and implement smallest vertical slice
3. Run relevant tests and check security-sensitive changes
4. Open a PR with evidence and rollback; require review for releases

## Outputs / acceptance
- Tests / manual check outputs and reproducible notes
- Pull Request and Issue update with no unapproved production action

## Gates
Read [work contract](../../../contracts/work-item.md) and [evidence](../../../contracts/evidence.md). Never claim fabricated verification, spend funds, contact customers, deploy or manipulate private data without explicit authorization. Return GitHub links when supported; otherwise structured handoff.
