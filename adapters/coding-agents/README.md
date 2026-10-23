# Flow B — local/cloud coding agents

Examples: Codex CLI/cloud, Claude Code, Cursor and GitHub coding assistants. No vendor-specific SDK required.

## Entry

`Open the linked GitHub Issue. Read AGENTS.md, contracts/work-item.md, and the referenced PRD. Work only within scope. Propose a plan, implement on an isolated branch/worktree, run tests and open a PR. Do not deploy or spend without authorization.`

## Steps

1. Check out the **product** repo if a product already exists; this repo holds the venture knowledge and link.
2. Verify branch and current Issue ownership, retrieve scoped acceptance criteria and latest PRD.
3. Plan implementation and identify risks. Challenge ambiguous requirements instead of inventing them.
4. Code and test in a dedicated branch/worktree. Avoid loading unrelated opportunities.
5. Open PR with tests, results, screenshots where relevant, risk and rollback steps.
6. Report status to Issue and wait for review or explicitly authorized release.
7. Support next validation loop using observed production issues and analytics (aggregated, anonymized).

For cloud agents with only repository access, supply the task package explicitly. They cannot assume access to your machine, GitHub Projects, ad accounts or private data.
