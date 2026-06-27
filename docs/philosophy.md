# Loop Engineering Philosophy

The General Purpose Loop Engineering Framework is built on three core philosophical pillars: **Deterministic Isolation**, **Independent Auditability (Maker/Checker)**, and **Structured Continuous Learning**.

---

## 1. Deterministic Isolation

In loop engineering, an AI agent's execution must be tightly bounded:
- **Sandboxing:** Every loop must declare its `## Scope` and `## External State` impacts. Agents cannot modify state or run tasks outside their declared bounds.
- **Preconditions:** Before a loop can make changes, it must verify programmatically that the codebase and system environment are in a safe, expected state.
- **Self-Termination:** Loops have strict time limits (`Max Run Duration`) to prevent runaway recursive calls and token billing inflation.

---

## 2. Independent Auditability (Maker/Checker)

AI agents should never grade their own homework.
- **Maker:** The agent instance responsible for generating the change or artifact.
- **Checker:** A separate, independent agent instance or human validator that evaluates the Maker's work against objective metrics and tests.
- **Audited Gates:** Transitions to key states (such as merging code or deploying to staging) are guarded by Hard Gates (requiring human confirmation) or Soft Gates (time-bound notifications).

---

## 3. Structured Continuous Learning

A loop is not a one-off execution; it is an iterative system that learns from failures.
- **Reflection:** Every completed or failed run produces a structured `REFLECTION` log.
- **Error Capture:** Failure modes are classified, root causes are evaluated, and telemetry is fed back into the next run's context.
- **Evolution:** Loop specifications themselves evolve, using semantic versioning to bump execution rules as the underlying models or frameworks change.
