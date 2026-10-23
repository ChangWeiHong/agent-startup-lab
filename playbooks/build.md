# 05 Build — agent-assisted engineering loop

Approved PRD / issue → scoped context → isolated branch or worktree → minimal implementation → tests → PR → review → merge → approved deployment → observation.

- Coding agent must read venture repo's `AGENTS.md`, linked PRD, relevant skill and acceptance criteria, **not every venture document**.
- Implement the smallest observable workflow end to end. Prefer managed infrastructure and a modular monolith when a backend is necessary.
- Add realistic tests: business logic, input validation, failure handling, permission boundaries and payment webhook idempotency when billing exists.
- CI should check syntax/tests/security relevant to the tech stack, without requiring paid services.
- PR links the Issue, changes, acceptance evidence, screenshots where appropriate, risk/rollback and operational effects.
- Human review is required for production, billing, data policy and security-impacting code changes.

**Exit:** reviewed code with executable evidence, not an agent's assertion that it works.
