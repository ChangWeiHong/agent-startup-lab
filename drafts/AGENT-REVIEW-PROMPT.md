# Independent Review Prompt (copy to any agent)

Read **[Original Request Brief](ORIGINAL-REQUEST-BRIEF.md)** first. This is the stakeholder's **informal original intent**, not a finalized architecture.

Then independently review `README.md`, `WORKFLOW.md`, `strategy/`, `contracts/`, `playbooks/`, `adapters/` and `.agents/skills/`.

**Do not make code changes or launch paid services.** Return:

1. **Requirement coverage:** missing or distorted parts of the original request.
2. **Assumption challenges:** unverified market claims, weak subscription arguments, incorrect statistical tests or poor cost/attribution assumptions.
3. **Architecture critique:** duplication, unnecessary directories, missing source-of-truth rules, cross-agent handoff failures, local/cloud agent compatibility.
4. **Safety review:** ad budgets, customer data, PII, deployment gates, public repo exposure, prompt injection, Agent access.
5. **Simplification:** lowest useful two-week V1 that can lead to first credible paying-customer evidence.
6. **Concrete recommendations:** ordered changes with severity, rationale, affected files and acceptance criteria.

Clearly distinguish **facts, observations, hypotheses and recommendations**. External public claims need citations and observation dates. Put results into a GitHub issue or PR (or return a structured handoff if no GitHub write access). Do not edit the historical original brief to make your own design look better.
