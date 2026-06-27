# Classification Matrix

This matrix classifies the loop specifications, standards, and assets from the original repository, justifying their inclusion as **General Purpose**, **Project Specific**, or **Mixed**.

| Original Asset | Classification | Justification |
| :--- | :--- | :--- |
| `LOOP-STANDARD.md` | **General Purpose** | Canonical specification format; applicable to any loop-based system. |
| `SPEC-001-LOOP-CONTRACTS.md` | **General Purpose** | Defines state machines and data contracts for loop runs. |
| `SPEC-005-Metrics.md` | **General Purpose** | Defines metrics (duration, status) that apply universally. |
| `SPEC-006-Governance.md` | **General Purpose** | Defines human oversight and emergency stops. |
| `SPEC-007-Versioning.md` | **General Purpose** | Rules for semantically versioning loop specifications. |
| `SPEC-010-Loop-Catalog.md` | **General Purpose** | Standards for indexing active and deprecated loops. |
| `SPEC-011-LOOP-AUTHORING-GUIDE.md`| **General Purpose** | Developer instructions for writing conformant loop files. |
| `LOOP-001` to `LOOP-007` (Core) | **General Purpose** | Fundamental discovery, planning, implementation, verification, and reflection loops. |
| `LOOP-101` to `LOOP-180` (Eng) | **General Purpose** | Standard engineering tasks (bug fixing, testing, code review, structural quality, security, and configuration). |
| `LOOP-201` to `LOOP-212` (Plat) | **Mixed / General Purpose** | Abstracted platform and integration validation, resilience testing, FinOps, and traffic checks. |
| `LOOP-301` to `LOOP-307` (Gov) | **General Purpose** | General governance tasks (ADR generation, compliance, doc governance, telemetry, and SaaS optimization). |
| `LOOP-401` to `LOOP-406` (Rel) | **General Purpose** | Release planning, deployment validation, edge rollbacks, and feature flag lifecycles. |
| `shared/rules/` (Java code) | **General Purpose** | Thread-safe condition expression evaluator. Remapped package imports. |
| `shared/execution/` (Java code) | **Mixed** | Contained generic retry and circuit-breaker code alongside WhatsApp clients. Decoupled and harvested only core execution utilities. |
