# Execution adapters

Adapters explain **how a particular executor invokes the shared work contract**. They MUST NOT duplicate business playbooks, accepted metrics, or evidence.

- [Autonomous agent](autonomous-agents/README.md): long-running / scheduled / connector-native systems.
- [Coding agent](coding-agents/README.md): local or cloud agent with git checkout, file access, tests and PRs.

Adapters are guidance, not proof a named vendor supports an operation. Check the actual tool permissions/capabilities during each session. Map unavailable capabilities to a structured GitHub handoff, not silent failure.
