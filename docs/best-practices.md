# Best Practices for Loop Engineering

Follow these standards to maintain high-quality, safe, and reliable execution loops.

---

## 1. Keep Loops Focused (YAGNI)

- Avoid designing monster loops that try to do everything (e.g. implementing code, writing docs, and deploying in a single run).
- Break tasks down into cohesive, narrow loops. For example, use `LOOP-104` for documentation and `LOOP-103` for testing, rather than doing both in `LOOP-105`.
- Declare strict `Out of scope` bounds in every loop document.

---

## 2. Enforce the Maker / Checker Pattern

- Never assign the same agent instance as both Maker and Checker for a step.
- Verify outputs using independent logic. If the Maker uses unit tests, the Checker should run static analysis or boundary validations.
- For all code changes, a human reviewer must be the final Checker before merge.

---

## 3. Monitor Telemetry and Telemetry Decay

- Ensure every loop records standard metrics (`run.duration_seconds`, `run.status`, `gate.hard.count`).
- Audit reflection logs periodically to identify decaying success rates. If a loop's success rate falls below 60%, pause it and review the prompt configurations.
- Use loop versioning to update prompt layouts as backend model weights evolve.
