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
| `LOOP-101` to `LOOP-105` (Eng) | **General Purpose** | Standard engineering tasks (bug fixing, testing, code review). |
| `LOOP-201` to `LOOP-204` (Plat) | **Mixed** | Originally checked Temporal and specific schemas. Abstracted in this library to support general workflow engines and API contracts. |
| `LOOP-205` to `LOOP-207` (Plat) | **Project Specific** | Coupled to Conductor's internal tenant isolation and Keycloak configs. Kept as draft templates in the library. |
| `LOOP-301` to `LOOP-304` (Gov) | **General Purpose** | General governance tasks (ADR generation, doc governance, release checks). |
| `shared/rules/` (Java code) | **General Purpose** | Thread-safe condition expression evaluator. Remapped package imports. |
| `shared/execution/` (Java code) | **Mixed** | Contained generic retry and circuit-breaker code alongside WhatsApp clients. Decoupled and harvested only core execution utilities. |
