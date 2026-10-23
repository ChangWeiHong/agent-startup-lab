# Work item contract — all agents

The GitHub Issue is the **live task record**. Include:

- **ID / title / primary owner:** one accountable agent/person at a time.
- **Objective:** measurable problem to solve; related venture or experiment ID.
- **Stage / trigger / idempotency key:** e.g. `market-scan:EV-owners:2026-W44`.
- **Inputs:** canonical doc paths, URLs and version/commit where relevant.
- **Scope / non-goals:** what to do and what not to change.
- **Required outputs:** exact file(s), Issue comment, experiment report, or PR.
- **Evidence:** expected verification, dated sources and observable results.
- **Constraints:** cost cap, PII, secrets, permitted external actions.
- **Acceptance criteria:** observable condition for completion.
- **Human gate:** precise step requiring authorization; owner decision not inferred.
- **Next action:** suggested next task or explicit blocker.

## Handoff reply format

`Outcome | Changed artifacts/links | Observed evidence | Assumptions/uncertainty | Tests | Spend | Approval needed | Next action`

If a connector cannot update GitHub, return a work package with the same fields for an authorized adapter/human; never claim completion of a GitHub write.
