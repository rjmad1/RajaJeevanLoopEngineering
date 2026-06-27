# Loop Catalog

This catalog indexes all generalized loops available in the General Purpose Loop Engineering Library.

| Loop ID | Name | Category | Complexity | Dependencies | Primary Use Cases |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **LOOP-001** | Architecture Discovery | Core | Low | None | Mapping a repository's folder structures and interfaces. |
| **LOOP-002** | Context Assembly | Core | Low | LOOP-001 | Gathering specific target source files and dependencies. |
| **LOOP-003** | Task Discovery | Core | Medium | LOOP-001, LOOP-002 | Decomposing raw tasks into detailed checklist items. |
| **LOOP-004** | Planning | Core | Medium | LOOP-002, LOOP-003 | Generating step-by-step implementation plans. |
| **LOOP-005** | Implementation | Core | High | LOOP-004 | Making sandbox-bounded edits in the codebase. |
| **LOOP-006** | Verification | Core | Low | LOOP-005 | Running test suites, checkstyle, and code scanners. |
| **LOOP-007** | Reflection | Core | Low | LOOP-006 | Conducting post-run assessments and memory updates. |
| **LOOP-101** | Bug Fixing | Engineering | High | LOOP-002, LOOP-004, LOOP-006 | Troubleshooting, replicating, and patching codebase bugs. |
| **LOOP-102** | Refactoring | Engineering | Medium | LOOP-002, LOOP-004, LOOP-006 | Structural cleanups and technical debt reduction. |
| **LOOP-103** | Test Generation | Engineering | Medium | LOOP-001, LOOP-002, LOOP-005 | Authoring unit and integration tests. |
| **LOOP-104** | Documentation | Engineering | Low | LOOP-001, LOOP-002 | Generating READMEs, wikis, and reference guides. |
| **LOOP-105** | Code Review | Engineering | Medium | LOOP-001, LOOP-002 | Automated auditing of pull requests. |
| **LOOP-201** | Workflow Validation | Platform | Medium | LOOP-006 | Validating pipeline flow and state boundaries. |
| **LOOP-202** | Integration Validation | Platform | Medium | LOOP-006 | Validating third-party API keys and rate limits. |
| **LOOP-203** | Event Validation | Platform | Medium | LOOP-006 | Auditing event schema and publisher topics. |
| **LOOP-204** | API Contract Validation | Platform | Medium | LOOP-006 | Ensuring REST and gRPC API contract compliance. |
| **LOOP-301** | ADR Generation | Governance | Low | LOOP-004 | Generating Architectural Decision Records. |
| **LOOP-302** | Doc Governance | Governance | Low | LOOP-007 | Auditing documents for stale links and formats. |
| **LOOP-304** | Release Readiness | Governance | Medium | LOOP-006, LOOP-007 | Performing checklist checks before main merges. |
