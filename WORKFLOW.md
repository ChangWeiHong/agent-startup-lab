# One core, two execution flows

## Shared state and handoff

- **Knowledge:** Markdown in Git, with evidence links. Research drafts only become accepted knowledge through PR review.
- **Live tasks:** GitHub Issues. Each active issue has one accountable owner, next action and explicit blockers.
- **Code:** separate product repo when required; PR is the proof of implementation.
- **Experiment outcome:** versioned summary in `experiments/` and decision in `decisions/`.
- **Project board:** optional readout of issues; do not create another state machine.

## Flow A — autonomous agent

Trigger (human/schedule/event) → select an Issue or create a proposed task → read work contract + scoped skill → retrieve and verify sources → prepare evidence → propose result via issue comment/PR → await approval on material actions → hand off next Issue.

Default scope is **research and recommendation**. Scheduling is provider-specific; this repo does not schedule anything by itself.

## Flow B — local/cloud coding agent

Approved Issue → check out product or venture repo → read `AGENTS.md`, scoped PRD and acceptance criteria → create branch/worktree → implement → run relevant tests → open PR with evidence → review/merge → update Issue → monitor issues after release.

Coding agents may research. Autonomous agents may code if authorized. These are workflows, not fixed capability restrictions.

## Concurrency rules

1. One primary owner per active Issue; secondary agents comment instead of overwriting.
2. One task, one branch/worktree; PR into protected main when configured.
3. Before rerunning a scheduled task, search for an open equivalent issue by experiment ID and period.
4. Prefer an idempotency key of `task-type:entity-id:period` in issue body.
5. Do not consider a GitHub Action check a replacement for a business spend/launch approval.
6. Resolve conflicting evidence through a decision record, not silently overwriting it.

## Minimal task cycle

**Propose → Approve if needed → Execute → Verify → Record Evidence → Decide → Next Work Item.**

See [contracts/work-item.md](contracts/work-item.md). External provider adapters never fork this logic.
