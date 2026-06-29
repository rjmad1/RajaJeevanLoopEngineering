# AEOS — Loop Instructions by Project Type

This reference guide provides copy-paste ready, context-specific instructions for executing and auditing **AEOS (Agentic Engineering Operating System)** loops. It is segmented by project type to ensure that AI agents and human overseers align with the codebase's maturity, risk profile, and architecture conventions.

---

## Table of Contents

- [Overview & How to Use](#overview--how-to-use)
- [Project Type 1 — Greenfield](#project-type-1--greenfield)
- [Project Type 2 — Brownfield](#project-type-2--brownfield)
- [Project Type 3 — Legacy Modernisation](#project-type-3--legacy-modernisation)
- [Project Type 4 — Open Source Contribution](#project-type-4--open-source-contribution)
- [Project Type 5 — Maintenance and Sustaining Engineering](#project-type-5--maintenance-and-sustaining-engineering)
- [Cross-Type Reference — Loop Trigger Conditions](#cross-type-reference--loop-trigger-conditions)
- [Common Mistakes — What Not to Do](#common-mistakes--what-not-to-do)

---

## Overview & How to Use

This guide contains copy-paste prompts (instructions) for using AEOS (Agentic Engineering Operating System) loops. These loops are predefined templates that help you structure, write, review, test, and document your code.

### What are loops and how do I use them?
Think of a "loop" as a recipe for a specific task (like fixing a bug, writing a test, or cleaning up code). You use them by copying the templates (the code blocks in this guide) and pasting them directly to your AI coding assistant or AEOS command prompt.

### Simple 3-Step Guide to Run a Loop

1. **Find your project type**: Scroll down to find the section that matches your project (for example, **Greenfield** for new projects, or **Brownfield** for working on existing codebases).
2. **Copy the template**: Find the loop you need (e.g. `LOOP-101` for bug fixing) and copy the template code block.
3. **Fill in the brackets and send**: Replace any placeholder text in brackets `[like this]` with your actual task details, and paste it to your AI tool.

> [!TIP]
> Always verify that your target file paths and folder names match the actual structure of your project before sending the prompt.

---

### Step-by-Step Example

Let's say you need to fix a bug in your payment code and your task number is `TASK-104`. You are working on an existing codebase, so you are in **Project Type 2 — Brownfield**.

1. You scroll down to **Project Type 2 — Brownfield** and find **LOOP-101 — Bug Fixing**.
2. You copy the prompt template:
   ```markdown
   Loop: LOOP-101
   Goal: Fix the defect described in [TASK-NNN].
   Task: [paste your task record here]
   Context: [paste LOOP-001's module-catalog entry for the affected module]
   Constraints:
     - Identify the root cause before proposing a fix. Document it in the
       engineering-analysis.md.
     - The fix must not change the public interface of any module.
     - All existing tests must pass after the fix.
   ```
3. You replace the bracketed sections with your actual details. Your final message to your AI assistant will look like this:
   ```markdown
   Loop: LOOP-101
   Goal: Fix the defect described in TASK-104.
   Task: TASK-104: Payment checkout form crashes on blank zip code input.
   Context: payment-service: Handles user credit card checkouts and validation.
   Constraints:
     - Identify the root cause before proposing a fix. Document it in the
       engineering-analysis.md.
     - The fix must not change the public interface of any module.
     - All existing tests must pass after the fix.
   ```
4. Paste it and run!

---

## Project Type 1 — Greenfield

*New project with little or no existing code. Run loops in the order listed.*

### Loop Sequence and When to Use

| # | Loop | When to Use It | Key Gate/Constraint |
| :--- | :--- | :--- | :--- |
| 1 | **LOOP-001** | At project start, and again after any new module, dependency, or structural folder is added. | Sparse catalog initially; capture boundaries early. |
| 2 | **LOOP-002** | Automatically invoked before every task — no manual trigger required. | Context assembly matches empty state. |
| 3 | **LOOP-003** | When you are ready to pull the next task from your backlog. | ARCH tasks must precede FEAT tasks. |
| 4 | **LOOP-004** | After LOOP-003 selects a task — produces the execution plan you must approve. | Requires human approval before coding. |
| 5 | **LOOP-005** | After you approve the plan at LOOP-004's review gate. | Enforces YAGNI; code strictly to spec. |
| 6 | **LOOP-103** | Alongside every LOOP-005 run for a new feature — generate tests as code is written, not after. | Test-first philosophy: do not defer. |
| 7 | **LOOP-104** | After every public interface, API, or module boundary is implemented. | Serves as the active architecture record. |
| 8 | **LOOP-006** | Automatically invoked after every LOOP-005 run — no manual trigger required. | Checks functional correctness and coverage. |
| 9 | **LOOP-007** | Automatically invoked at the end of every session — no manual trigger required. | Captures design decisions and assumptions. |
| 10 | **LOOP-008** | On-demand when a new repeatable workflow is needed. | End-to-end loop creation with duplication checks. |

### LOOP-001 — Architecture Discovery

**When:** At project start. Again after adding a new module, folder structure, external dependency, or integration.

**Explainer:** Scans the newly initialized workspace to capture intended module boundaries, directories, and technology stacks.

```markdown
Loop: LOOP-001
Goal: Perform a full architecture discovery of this repository.
Scope: Full repository scan — all directories, all source files, all configuration files.
Output: docs/architecture/
Expected artefacts:
  - module-catalog.md
  - api-catalog.md
  - event-catalog.md
  - dependency-map.md
  - technology-stack.md
  - architecture-summary.md
Note: This is a greenfield project. The module catalog will be sparse initially.
Capture intended module boundaries and conventions even if implementation is minimal.
```

### LOOP-003 — Task Discovery

**When:** You are ready to start the next unit of work and want the runtime to select and confirm the highest-priority ready task.

**Explainer:** Queries the backlog to pick the highest priority task, enforcing that architectural setup tasks are completed before feature work.

```markdown
Loop: LOOP-003
Goal: Select the next task from the backlog.
Backlog path: docs/loops/core/task-catalog.md
Filter: status = ready
Priority order: ARCH before FEAT before TEST before DOCS
Return: The single highest-priority ready task with its full task record.
Note: In a greenfield project, ARCH tasks should precede FEAT tasks.
Do not select a FEAT task if an ARCH task is ready and not yet completed.
```

### LOOP-004 — Planning

**When:** A task has been selected by LOOP-003 and you need an execution plan before implementation begins.

**Explainer:** Creates an isolated step-by-step path for implementing a task. In greenfield, the plan must define the public interface before writing implementation.

```markdown
Loop: LOOP-004
Goal: Produce a step-by-step execution plan for the selected task.
Task: [TASK-NNN — paste your task record here]
Constraints:
  - Each step must modify at most one module.
  - No step may modify files outside the declared affected_modules.
  - Plan must include a rollback action for every step.
  - Plan must declare acceptance criteria for each step's output.
  - For greenfield: include a step to define the module's public interface
    before any implementation steps.
Await human approval before proceeding to LOOP-005.
```

### LOOP-005 — Implementation

**When:** You have reviewed and approved the execution plan from LOOP-004.

**Explainer:** Directs the agent to write code according to the approved plan and conventions defined in discovery.

```markdown
Loop: LOOP-005
Goal: Execute the approved plan for [TASK-NNN].
Plan: [paste the approved execution plan from LOOP-004 here]
Constraints:
  - Modify only files declared in the plan's files_modified list.
  - Do not make architectural decisions mid-step. If the declared approach
    is not achievable, raise a step_deviation signal.
  - For greenfield: follow the coding conventions captured in
    docs/architecture/technology-stack.md.
  - Record all assumptions in the implementation-summary.md.
```

### LOOP-103 — Test Generation

**When:** A feature or module has been implemented via LOOP-005. Run immediately after, not deferred.

**Explainer:** Generates unit and integration tests alongside implementation. Greenfield tests are foundational to prevent immediate regression.

```markdown
Loop: LOOP-103
Goal: Generate tests for the implementation produced by LOOP-005 for [TASK-NNN].
Scope: [list the files or modules implemented in the preceding LOOP-005 run]
Test types to generate:
  - Unit tests for all public functions and methods
  - Integration tests for all module boundaries crossed
  - Edge cases for all declared acceptance criteria
Coverage target: 80% line coverage minimum for new code.
Note: In a greenfield project, tests are foundational — generate them alongside
implementation, not as a separate sprint.
```

### LOOP-104 — Documentation

**When:** A public API, external interface, or module boundary has been implemented. Run once per module before moving to the next.

**Explainer:** Formally documents the newly introduced module boundaries, API endpoints, and usage constraints.

```markdown
Loop: LOOP-104
Goal: Document the public interface implemented in [TASK-NNN].
Scope: [list the public APIs, interfaces, or module boundaries to document]
Documentation types:
  - API reference for all public methods and endpoints
  - Module purpose and responsibility statement
  - Usage examples for the primary use cases
  - Any constraints or invariants callers must respect
Output path: docs/
Note: In a greenfield project, documentation written now becomes the
architecture record. Write it as if a new team member will read it first.
```

### LOOP-006 — Verification

**When:** Automatically triggered after every LOOP-005 run. If you need to trigger it manually:

**Explainer:** Independent checker agent verifies correctness, ensuring the new components satisfy functional requirements and meet the 80% coverage mark.

```markdown
Loop: LOOP-006
Goal: Independently verify the implementation produced for [TASK-NNN].
Implementation artefacts: [path to LOOP-005's implementation-summary.md]
Verification profile:
  - Category 1 (Functional correctness): MANDATORY
  - Category 3 (Test coverage): MANDATORY — minimum 80% for new code
  - Category 4 (Code quality): MANDATORY
  - Category 5 (Documentation completeness): MANDATORY for public interfaces
  - Minimum confidence score: 75
Note: Verifier must be a different agent instance from the implementer.
```

### LOOP-007 — Reflection

**When:** Automatically triggered at the end of every session. If you need to trigger it manually:

**Explainer:** Compiles architectural insights, design trade-offs, and lessons from the session to refine future project plans.

```markdown
Loop: LOOP-007
Goal: Capture lessons and patterns from the completed session for [TASK-NNN].
Artefact set: [session artefact registry path]
Focus areas for greenfield:
  - Module boundary decisions and their rationale
  - Interface design choices and alternatives considered
  - Patterns emerging from the early architecture
  - Any assumption made during planning that proved incorrect
Output: docs/reflection/
```

---

## Project Type 2 — Brownfield

*Existing codebase with active development. Focus is on context isolation and regression prevention.*

### Loop Sequence and When to Use

| # | Loop | When to Use It | Key Gate/Constraint |
| :--- | :--- | :--- | :--- |
| 1 | **LOOP-001** | At adoption start; again after major merges, framework upgrades, or structural changes. Minimum: once per sprint. | Identifies hidden coupling and high-regression risks. |
| 2 | **LOOP-002** | Automatically invoked before every task — no manual trigger required. | Gathers file contexts for the target task. |
| 3 | **LOOP-003** | When selecting the next task — runtime enforces SEC before BUG before FEAT priority. | Priority: SEC → BUG → ARCH → FEAT. |
| 4 | **LOOP-004** | After task selection — scrutinise plan scope at review gate; send back if more than 3–5 files are in scope for a BUG. | Reject plan if it modifies > 5 files for a bug. |
| 5 | **LOOP-005** | After plan approval — runtime enforces write scope boundaries. | Strictly enforces target write scopes. |
| 6 | **LOOP-101** | For BUG and SEC classified tasks. | Surgical fixes; no architectural decisions mid-way. |
| 7 | **LOOP-102** | For RFCT classified tasks — only after test coverage is confirmed sufficient. | Forbidden if coverage is below 70%. |
| 8 | **LOOP-105** | Before any LOOP-005 implementation is merged — simulate peer review. | Peer review simulation; blocks on critical findings. |
| 9 | **LOOP-006** | Automatically invoked after LOOP-005 — do not skip; regression detection is critical. | Regression check against `session_start_sha` is mandatory. |
| 10 | **LOOP-007** | Automatically invoked at session end — review output after every 3–4 cycles. | Review findings to identify structural patterns. |
| 11 | **LOOP-008** | On-demand when a new repeatable workflow is needed. | End-to-end loop creation with duplication checks. |

### Specialized Engineering & Operational Audit Loops

These loops are triggered either periodically or based on specific task categories to manage ongoing health, telemetry, experimental variants, dependencies, and environments.

| Loop | Name | When to Use It | Key Gate/Constraint |
| :--- | :--- | :--- | :--- |
| **LOOP-106** | Customer Journey Analytics | On-demand; correlating runtime exceptions to business conversion drop-offs. | Requires integration with business logs. |
| **LOOP-111** | Technical Debt Remediation | Weekly/monthly scheduled runs; prioritizing complexity and refactoring backlog. | Focus on high-churn files first. |
| **LOOP-150** | Dependency Patching | Weekly, or immediately on critical CVE vulnerability disclosures. | Strictly upgrade one package per PR. |
| **LOOP-170** | Zero-Trust Token Rotation | Periodic scheduled rotation, or immediately following key exposures. | Must maintain zero downtime. |
| **LOOP-180** | Environment Drift Audit | Monthly scheduled check; validating IaC alignments. | Highlights mismatches in staging/production. |
| **LOOP-205** | Multi-Tenant Isolation Audit | Periodic security audits; tests tenant data bleed via query injection. | Enforces strict data boundaries. |
| **LOOP-209** | Partner API Degradation | Monthly or on-demand; checks circuit-breaker resilient degradation. | Simulates third-party service failures. |
| **LOOP-211** | FinOps Cloud Bursting | On cost alerts; recommends workload scaling/relocation options. | Optimizes resource configuration costs. |
| **LOOP-212** | Chaos Engineering Resilience | Periodic drills; injects service failures to verify system self-healing. | Validates recovery bounds. |
| **LOOP-305** | Telemetry Compliance | When changing event pipelines, schemas, or analytics tracking. | Matches tracking specifications. |
| **LOOP-306** | SaaS Cost Optimization | Monthly licensing audits; flags inactive seats for deprovisioning. | Lowers software seat licensing waste. |
| **LOOP-307** | Regulatory Compliance Drift | Pre-audit reviews; checks changes against GDPR/HIPAA standards. | Prevents silent data compliance failures. |
| **LOOP-404** | Feature Flag Lifecycle | Rollout/rollback of toggles, or automated removal of stale toggles. | Prevents tech debt from stale flags. |
| **LOOP-405** | Experimentation Guardrail | Active A/B experiments; tracks health and auto-terminates failing variants. | Blocks variants breaking safety thresholds. |
| **LOOP-406** | Edge Deployment Rollback | Automatically on edge alert spikes; reverts to last known good image. | Minimizes blast radius at edge locations. |

### LOOP-001 — Architecture Discovery

**When:** First time adopting AEOS on this codebase. After major branch merges. After dependency upgrades that change the module graph. After any team adds or removes modules.

**Explainer:** Establishes the current architectural state, highlighting high-coupling risk zones where code changes are most dangerous.

```markdown
Loop: LOOP-001
Goal: Perform a full architecture discovery of this repository.
Scope: Full repository scan — all source directories, all configuration, all build files.
Output: docs/architecture/
Expected artefacts:
  - module-catalog.md      (every module with its responsibilities)
  - api-catalog.md         (all internal and external API surfaces)
  - event-catalog.md       (all events, messages, queues)
  - dependency-map.md      (inter-module dependencies and external dependencies)
  - technology-stack.md    (languages, frameworks, tools)
  - architecture-summary.md
Note: This is a brownfield project. Discovery will surface existing coupling,
hidden dependencies, and undocumented conventions. Review the dependency-map.md
carefully — high-coupling modules are the highest regression risk for future tasks.
```

### LOOP-003 — Task Discovery

**When:** Starting a new work cycle. Let the runtime enforce priority ordering.

**Explainer:** Automates backlog selection, prioritizing security and bugs over new features to maintain system stability.

```markdown
Loop: LOOP-003
Goal: Select the next task from the backlog.
Backlog path: docs/loops/core/task-catalog.md
Filter: status = ready
Priority order: SEC → BUG → ARCH → FEAT → PERF → RFCT → DEP → TEST → DOCS
Return: The single highest-priority ready task with its full task record.
Note: In a brownfield project, do not override priority to work on features
before bugs. The framework's priority ordering exists to prevent exactly this.
```

### LOOP-004 — Planning

**When:** A task has been selected. Apply scope discipline at the review gate.

**Explainer:** Creates an execution plan. For bugs, changes must be constrained to a maximum of 5 files to prevent scope creep.

```markdown
Loop: LOOP-004
Goal: Produce a step-by-step execution plan for [TASK-NNN].
Task: [paste your task record here]
Constraints:
  - BUG tasks: maximum 5 files modified. If the plan exceeds 5 files,
    return it — the task is likely an architectural issue, not a bug fix.
  - FEAT tasks: each step must modify at most one module.
  - Every step must declare a rollback action.
  - Plan must identify which existing tests cover the affected code
    (these become the regression baseline for LOOP-006).
  - Plan must NOT propose changes to modules not listed in affected_modules
    without a separate gate approval.
Await human approval before proceeding to LOOP-005.
```

### LOOP-101 — Bug Fixing

**When:** Task is classified BUG or SEC.

**Explainer:** Performs a targeted, surgical fix for a defect. Requires documenting root cause first and preserving public module interfaces.

```markdown
Loop: LOOP-101
Goal: Fix the defect described in [TASK-NNN].
Task: [paste your task record here]
Context: [paste LOOP-001's module-catalog entry for the affected module]
Constraints:
  - Identify the root cause before proposing a fix. Document it in the
    engineering-analysis.md artefact.
  - The fix must not change the public interface of any module unless the
    task record explicitly permits it.
  - Regression baseline: all tests passing in the affected modules at
    session_start_sha must still pass after the fix.
  - If the root cause is architectural (not a localised defect), halt and
    raise a GATE-1 with the architectural assessment. Do not fix symptoms.
```

### LOOP-102 — Refactoring

**When:** Task is classified RFCT. Only trigger after confirming test coverage is sufficient for the affected module.

**Explainer:** Executes behavior-preserving improvements. Enforces a strict pre-condition of 70% test coverage before any changes are allowed.

```markdown
Loop: LOOP-102
Goal: Refactor the code described in [TASK-NNN].
Task: [paste your task record here]
Pre-condition check (complete before submitting):
  - Confirm test coverage for affected modules is at or above 70%.
  - If below 70%, run LOOP-103 first and complete that task before this one.
Constraints:
  - Refactoring must be behaviour-preserving. No functional changes.
  - All existing tests must pass after refactoring (verified by LOOP-006).
  - Do not expand refactoring scope beyond the declared affected_modules
    even if adjacent code would benefit from similar changes. File a
    separate task for adjacent refactoring.
  - Document the structural improvement in the implementation-summary.md.
```

### LOOP-105 — Code Review

**When:** After LOOP-005 completes and before changes are merged. Simulates peer review.

**Explainer:** Simulates peer review by scanning changes for security, backward-compatibility, style compliance, and testing validity.

```markdown
Loop: LOOP-105
Goal: Review the implementation produced for [TASK-NNN].
Implementation artefacts: [path to LOOP-005's implementation-summary.md and changed files]
Review focus:
  - Does the implementation match the approved plan?
  - Are there any security concerns in the changed code?
  - Are there hidden side effects not declared in the plan?
  - Are the changed APIs backward compatible?
  - Is the code consistent with the patterns in docs/architecture/?
  - Are the new or modified tests meaningful (not just coverage padding)?
Output: A structured review report with findings classified by severity.
Blocker findings must be resolved before the changes are merged.
```

### LOOP-006 — Verification

**When:** Automatically triggered after LOOP-005. In brownfield this is most critical — regression detection runs against the session_start_sha baseline.

**Explainer:** Verifies correctness and checks for regressions against `session_start_sha` across all modules.

```markdown
Loop: LOOP-006
Goal: Independently verify the implementation produced for [TASK-NNN].
Implementation artefacts: [path to LOOP-005's implementation-summary.md]
Verification profile:
  - Category 1 (Functional correctness): MANDATORY
  - Category 2 (Regression testing): MANDATORY — compare against session_start_sha
  - Category 3 (Test coverage): MANDATORY
  - Category 4 (Code quality): MANDATORY
  - Category 9 (Backward compatibility): MANDATORY if any public API was changed
  - Minimum confidence score: 70
Regression rule: A test that was passing at session_start_sha and fails after
implementation is a regression regardless of whether it is in the declared scope.
```

### LOOP-007 — Reflection

**When:** Automatically triggered at session end. Review the output every 3–4 cycles.

**Explainer:** Documents insights on coupling, planning assumptions, and recurring defect patterns, driving backlog creation for refactoring.

```markdown
Loop: LOOP-007
Goal: Capture lessons and patterns from the completed session for [TASK-NNN].
Artefact set: [session artefact registry path]
Focus areas for brownfield:
  - Hidden coupling discovered during implementation
  - Assumptions in the plan that did not match reality
  - Modules where regression risk is consistently high
  - Patterns in recurring defects (same module, same type, same root cause)
Output: docs/reflection/
Review docs/reflection/improvement-opportunities.md after every 4 cycles and
schedule the top P1 items as ARCH or RFCT tasks in the backlog.
```

### LOOP-106 — Customer Journey Analytics

**When:** Run on-demand when runtime errors or exceptions correlate with drops in conversion funnels or user drop-offs.

**Explainer:** Maps application error telemetry to user checkout or conversion logs to evaluate business impact.

```markdown
Loop: LOOP-106
Goal: Correlate runtime errors with drops in customer conversion funnels.
Scope: Application error logs and user journey telemetry.
Target Funnel: [e.g., checkout flow, user signup]
Expected output: A report mapping specific exception patterns to funnel drops with estimated business impact.
```

### LOOP-111 — Technical Debt Remediation

**When:** Weekly or monthly scheduled run to evaluate complexity trends and schedule localized refactoring.

**Explainer:** Scans code churn and files with high cyclomatic complexity to generate refactoring tasks.

```markdown
Loop: LOOP-111
Goal: Quantify technical debt and identify top refactoring candidates.
Scope: Codebase complexity analysis and file edit history (git churn).
Expected output: A technical debt report listing candidate modules for refactoring under LOOP-102.
```

### LOOP-150 — Dependency Patching

**When:** Weekly, or immediately upon a security vulnerability disclosure (CVE) affecting third-party packages.

**Explainer:** Scans package manifests, identifies out-of-date or vulnerable packages, and updates them safely.

```markdown
Loop: LOOP-150
Goal: Scan and apply upgrades to third-party dependencies.
Target Package: [e.g., spring-core or express]
Scope: Build manifests (e.g., package.json, build.gradle, pom.xml).
Expected output: Updated dependency file and verified clean build/test output.
Constraints: Upgrade only one package at a time to prevent multi-point failure.
```

### LOOP-170 — Zero-Trust Token Rotation

**When:** Periodic schedule or immediately following a security incident or credential exposure.

**Explainer:** Automates rotation of keys, API tokens, and access credentials without system downtime.

```markdown
Loop: LOOP-170
Goal: Rotate active credentials or API tokens safely.
Target secret: [Name of secret or token to rotate]
Expected output: Verified successful token rotation with zero-downtime service execution.
```

### LOOP-180 — Environment Drift Audit

**When:** Monthly, or after major environment configuration changes in staging, UAT, or production.

**Explainer:** Compares infrastructure-as-code configurations with actual deployed states to flag drift.

```markdown
Loop: LOOP-180
Goal: Audit environment configuration drift across staging, UAT, and production.
Scope: Infrastructure-as-code files and environment deployment descriptors.
Expected output: Drift audit report highlighting mismatches and remediation scripts.
```

### LOOP-205 — Multi-Tenant Isolation Audit

**When:** Periodic schedule, or after significant changes to data routing, schemas, or tenant isolation layers.

**Explainer:** Validates data boundary safety by injecting cross-tenant data query simulations.

```markdown
Loop: LOOP-205
Goal: Audit multi-tenant isolation and verify zero data bleed across tenants.
Scope: Database queries, API routing middleware, and session context resolvers.
Expected output: Tenant isolation validation report detailing security test execution.
```

### LOOP-209 — Partner API Degradation

**When:** Monthly scheduled run or after updating integrations with critical third-party APIs.

**Explainer:** Simulates partner API failures (latency, errors) to verify that circuit breakers trigger correctly.

```markdown
Loop: LOOP-209
Goal: Validate resilience and circuit-breaker behavior under partner API degradation.
Target API: [Name/URL of the external integration]
Expected output: Circuit-breaker threshold validation report.
```

### LOOP-211 — FinOps Cloud Bursting

**When:** On-demand when cloud resource cost alert thresholds are exceeded.

**Explainer:** Identifies cost-saving workload placement opportunities and maps workload transfers.

```markdown
Loop: LOOP-211
Goal: Analyze cloud consumption and recommend workload scaling or migration.
Scope: Billing telemetry and deployment resource manifests.
Expected output: Recommendations for FinOps cost reduction and workload placement.
```

### LOOP-212 — Chaos Engineering Resilience

**When:** Scheduled periodic drills in non-production environments to verify system self-healing.

**Explainer:** Injects service outages, network latency, or pod kills to verify clustering recovery.

```markdown
Loop: LOOP-212
Goal: Verify resilience by injecting target service failures.
Target service: [Name of service/component to fail]
Failure type: [e.g., Pod kill, network latency injection]
Expected output: System recovery analysis detailing failover success and duration.
```

### LOOP-305 — Telemetry Compliance

**When:** Run when feature updates alter tracking logs, event pipelines, or analytics triggers.

**Explainer:** Verifies event formats and payloads match defined business schema specifications.

```markdown
Loop: LOOP-305
Goal: Verify telemetry event emission schema compliance.
Tracking Spec: [Path to tracking dictionary or specification]
Expected output: Compliance report checking emitted events against the dictionary.
```

### LOOP-306 — SaaS Cost Optimization

**When:** Monthly or quarterly licensing review.

**Explainer:** Identifies underutilized SaaS seats and generates lists of candidate accounts to deprovision.

```markdown
Loop: LOOP-306
Goal: Identify unused SaaS seat licenses for cost savings.
Target SaaS: [Name of SaaS application]
Expected output: Audit report listing inactive accounts and potential cost savings.
```

### LOOP-307 — Regulatory Compliance Drift

**When:** After changes in legal frameworks (e.g. GDPR, HIPAA updates) or prior to compliance audits.

**Explainer:** Assesses recent commits and database schemas for compliance alignment.

```markdown
Loop: LOOP-307
Goal: Audit codebase compliance against regulatory frameworks.
Target Regulation: [e.g., GDPR, HIPAA]
Scope: Recent database schema changes and PII data handlers.
Expected output: Compliance check report identifying potential drift or exposure risks.
```

### LOOP-404 — Feature Flag Lifecycle

**When:** When rolling out new features behind flags, or cleaning up stale/completed feature flags.

**Explainer:** Manages rollout schedules, flags health metrics, and automates stale toggle removal.

```markdown
Loop: LOOP-404
Goal: Rollout, rollback, or clean up feature flags.
Feature Flag: [Feature Flag Key]
Action: [Rollout / Rollback / Cleanup]
Expected output: Surgical removal of feature flag code path or updated rollout configurations.
```

### LOOP-405 — Experimentation Guardrail

**When:** During live A/B experiments to ensure variant performance doesn't cause customer harm.

**Explainer:** Monitors metrics like latency or signup rates to automatically disable failing variants.

```markdown
Loop: LOOP-405
Goal: Monitor live experimentation variants against health guardrails.
Experiment Key: [Experiment ID]
Expected output: Guardrail compliance log, with auto-termination trigger if safety bounds are breached.
```

### LOOP-406 — Edge Deployment Rollback

**When:** Automatically on deployment anomaly alerts, or manually to revert container states at edge networks.

**Explainer:** Monitors edge telemetry and deploys previous known good images upon error rate spike.

```markdown
Loop: LOOP-406
Goal: Monitor edge deployment health and trigger rollbacks on error spikes.
Scope: Edge container deployments and health checkers.
Expected output: Edge rollback status and validation report.
```

---

## Project Type 3 — Legacy Modernisation

*Incrementally restructuring an existing system — migration, decomposition, framework upgrade.*

### Loop Sequence and When to Use

| # | Loop | When to Use It | Key Gate/Constraint |
| :--- | :--- | :--- | :--- |
| 1 | **LOOP-001 (Baseline)** | At start (establishes baseline). | Authoritative as-is baseline. Commit it immediately. |
| 2 | **LOOP-103** | Before touching any module — raise coverage to threshold first. | Line coverage must reach 70% threshold first. |
| 3 | **LOOP-002** | Automatically invoked — no manual trigger required. | Gathers legacy contexts. |
| 4 | **LOOP-003** | Selects the next ARCH or RFCT task — module with lowest coupling migrates first. | Migration of lowest-coupled modules first. |
| 5 | **LOOP-004** | After task selection — plan must include target module boundary and rollback strategy. | Reject plan if boundary and rollback are unclear. |
| 6 | **LOOP-102** | Primary capability for structural refactoring. | Behavior-preserving; halt on hidden dependencies. |
| 7 | **LOOP-104** | After each module migration — document the new interface. | Establish contract to prevent future coupling. |
| 8 | **LOOP-105** | After every structural change — scrutinise for hidden side effects. | Verify boundary compliance; check for side effects. |
| 9 | **LOOP-006** | Automatically invoked — regression detection is the primary safety net. | Characterization tests must pass; high safety score (80). |
| 10 | **LOOP-007** | Automatically invoked — review after every module migration. | Review learnings to update future migration plans. |
| 11 | **LOOP-001 (Post)** | After every module migration is complete. | Confirm boundary has moved and no coupling was added. |
| 12 | **LOOP-008** | On-demand when a new repeatable workflow is needed. | End-to-end loop creation with duplication checks. |

> [!IMPORTANT]
> **Mandatory Cycle Per Module:**
> `LOOP-103` (Raise Coverage) ➔ `LOOP-102` (Refactor/Migrate) ➔ `LOOP-006` (Verify) ➔ `LOOP-001` (Rediscover Boundaries) ➔ `LOOP-104` (Document Contract)

### LOOP-001 — Architecture Discovery (Baseline)

**When:** Before any code is changed. This run establishes the as-is baseline that all subsequent verification compares against.

**Explainer:** Captures the initial state of the codebase. Commit the results to Git as a benchmark.

```markdown
Loop: LOOP-001
Goal: Establish the as-is architecture baseline for this repository.
Scope: Full repository scan.
Output: docs/architecture/
Note: This is a legacy modernisation project. Treat this run as the
authoritative as-is baseline. Do not change any code before reviewing
and confirming these outputs. The dependency-map.md will show coupling
patterns — modules with the fewest inbound dependencies are candidates
for migration first (lowest risk). Version-control the outputs of this
run explicitly with a commit message: "chore: LOOP-001 as-is baseline".
```

### LOOP-001 — Architecture Discovery (Post-Migration)

**When:** After completing migration of each module. Confirms the boundary has moved as intended.

**Explainer:** Verifies that a migration successfully isolated the target module and didn't add new accidental dependencies.

```markdown
Loop: LOOP-001
Goal: Rediscover the architecture after migrating [module name].
Scope: Full repository scan.
Output: docs/architecture/
Note: Compare this run's dependency-map.md with the previous run.
Confirm that:
  1. [module name] no longer has inbound dependencies from modules
     it should not be coupled to.
  2. The module's public interface is correctly captured in api-catalog.md.
  3. No unintended dependencies were introduced during migration.
If unexpected dependencies appear, halt further migration until resolved.
```

### LOOP-103 — Test Generation (Pre-Refactoring Gate)

**When:** Before starting any RFCT or ARCH task on a module. Coverage must reach threshold before refactoring begins.

**Explainer:** Creates characterization tests to document actual legacy behavior and ensure a safety net before modification.

```markdown
Loop: LOOP-103
Goal: Raise test coverage for [module name] to the minimum threshold before refactoring.
Scope: [module name] — all source files in this module only.
Coverage target: 70% line coverage minimum.
Test types to generate:
  - Unit tests for all public methods
  - Integration tests for all calls crossing module boundaries
  - Characterisation tests for any behaviour that is not formally specified
    (tests that document what the code currently does, to detect regressions)
Note: Characterisation tests are especially important in legacy code where
the intended behaviour is unclear. Generate them before any changes so that
LOOP-006 has a verified baseline to compare against.
Do not proceed to LOOP-102 until this loop completes and LOOP-006 accepts it.
```

### LOOP-004 — Planning

**When:** After selecting an ARCH or RFCT task. The plan must specify the target boundary explicitly.

**Explainer:** Formulates the migration path. Stricter than standard planning: prohibits mixing functional changes with restructuring.

```markdown
Loop: LOOP-004
Goal: Produce an execution plan for [TASK-NNN].
Task: [paste your task record here]
Constraints for legacy modernisation:
  - The plan must state the target module boundary explicitly:
    what this module will and will not be responsible for after migration.
  - The plan must state the migration approach:
    strangler fig / extract module / interface-first / other.
  - The plan must include a rollback strategy for the entire module migration,
    not just per-step rollbacks.
  - The plan must NOT mix structural changes with functional changes.
    If a bug is found during migration, file a separate BUG task.
  - Maximum parallelism: 1 parallel step group. Legacy migrations are
    sequenced, not parallelised.
Await human approval. At the review gate, confirm the target boundary
is clearly stated and the rollback strategy is credible.
```

### LOOP-102 — Refactoring

**When:** Coverage gate is cleared. Plan is approved. This is the primary loop for legacy modernisation.

**Explainer:** Executes the code extraction or restructuring. Halts and raises a gate alert if undocumented dependencies are found.

```markdown
Loop: LOOP-102
Goal: Migrate [module name] according to the approved plan for [TASK-NNN].
Plan: [paste approved plan from LOOP-004]
Pre-conditions (confirm before submitting):
  - LOOP-103 has completed for this module with LOOP-006 accepted.
  - LOOP-001 baseline from before migration is committed and retrievable.
Constraints:
  - Behaviour-preserving: all characterisation tests must still pass.
  - Interface changes must be backward compatible unless the plan explicitly
    declares a breaking change with a stated migration path for callers.
  - If a hidden dependency is discovered during migration (a module that
    unexpectedly calls into this module), halt and fire a GATE-1.
    Do not refactor around a hidden dependency — surface it.
  - Record every assumption and every discovered coupling in
    implementation-summary.md.
```

### LOOP-104 — Documentation

**When:** After each module migration is complete and LOOP-006 has accepted it.

**Explainer:** Documents the newly decoupled interface to establish an explicit contract for downstream teams.

```markdown
Loop: LOOP-104
Goal: Document the migrated interface of [module name].
Scope: [module name] — public interface only.
Documentation to produce:
  - Module responsibility statement (what this module does and does not do)
  - Public API reference for all interfaces exposed to other modules
  - Migration notes: what changed from the prior interface and why
  - Caller migration guide: if callers need to update how they call this
    module, document the before/after
Output path: docs/architecture/ and inline as code comments where appropriate.
Note: This documentation becomes the contract that prevents future callers
from reintroducing the coupling patterns that migration removed.
```

### LOOP-105 — Code Review

**When:** After every structural change. Structural changes have wide blast radius; review is mandatory.

**Explainer:** Validates that the refactored code meets architectural goals and that characterization tests remain structurally valid.

```markdown
Loop: LOOP-105
Goal: Review the structural changes produced for [TASK-NNN].
Implementation artefacts: [path to LOOP-005's implementation-summary.md and changed files]
Review focus for legacy modernisation:
  - Does the module boundary match the plan's declared target boundary?
  - Have any hidden dependencies been introduced rather than removed?
  - Are all callers of the changed module still compatible?
  - Is the rollback strategy still viable given what was actually changed?
  - Are the characterisation tests still meaningful after the structural change?
  - Does the new code follow the conventions captured in docs/architecture/?
Finding severity: Any finding that reveals an unexpected inbound dependency
or a broken caller interface is CRITICAL and must be resolved before merging.
```

### LOOP-006 — Verification

**When:** Automatically triggered after every LOOP-005. In legacy modernisation this is your safety net — do not skip and do not accept anything below the minimum confidence score.

**Explainer:** Demands a higher confidence score (80) to ensure that legacy refactoring does not break downstream processes.

```markdown
Loop: LOOP-006
Goal: Verify the structural changes produced for [TASK-NNN].
Implementation artefacts: [path to LOOP-005's implementation-summary.md]
Verification profile:
  - Category 1 (Functional correctness): MANDATORY
  - Category 2 (Regression testing): MANDATORY — characterisation tests must pass
  - Category 3 (Test coverage): MANDATORY — must not fall below the pre-refactoring level
  - Category 4 (Code quality): MANDATORY
  - Category 8 (Architecture compliance): MANDATORY — verify boundary matches plan
  - Category 9 (Backward compatibility): MANDATORY
  - Minimum confidence score: 80 (higher than standard — structural changes warrant it)
Regression rule: Any characterisation test that was passing before refactoring
and fails after is a regression, regardless of whether the test was in scope.
```

### LOOP-007 — Reflection

**When:** Automatically triggered at session end. Review after every module migration.

**Explainer:** Records patterns discovered in the legacy code to streamline the next phase of the modernization roadmap.

```markdown
Loop: LOOP-007
Goal: Capture lessons from the migration of [module name].
Artefact set: [session artefact registry path]
Focus areas for legacy modernisation:
  - What hidden coupling was discovered during migration?
  - Which assumptions in the plan proved incorrect and why?
  - What characterisation test failures revealed about undocumented behaviour?
  - Which migration approach worked and which should be avoided for the next module?
  - What patterns in the legacy code make future migration harder or easier?
Output: docs/reflection/
Note: The patterns captured here directly inform LOOP-004 planning for the
next module migration. Review docs/reflection/engineering-patterns.md before
planning each new module migration.
```

---

## Project Type 4 — Open Source Contribution

*Contributing to a repository you do not own. Respecting upstream conventions.*

### Loop Sequence and When to Use

| # | Loop | When to Use It | Key Gate/Constraint |
| :--- | :--- | :--- | :--- |
| 1 | **LOOP-001** | Once, on the upstream repository. Outputs are your map of upstream conventions — do not deviate from them. | Treat outputs as READ-ONLY; do not propose structural changes. |
| 2 | **LOOP-002** | Automatically invoked — no manual trigger required. | Isolates context to the specific issue files. |
| 3 | **LOOP-003** | Select the one task that corresponds to your contribution. | Backlog should contain exactly one task. |
| 4 | **LOOP-004** | Plan the contribution — scope must be minimal and strictly within declared affected_modules. | Reject plan if it modifies unnecessary files. |
| 5 | **LOOP-101** | For bug fix contributions (most common). | Fix root cause surgically; add upstream-friendly tests. |
| 6 | **LOOP-105** | Before opening the PR — simulate the maintainer's review. | Catches styling/dependency issues before maintainers see them. |
| 7 | **LOOP-006** | Must return Accepted before the PR is opened. | Requires full pass of the upstream test suite. |
| 8 | **LOOP-007** | Automatically triggered at session end. | Capture insights to speed up future contributions. |

### LOOP-001 — Architecture Discovery

**When:** Once, when you first fork or clone the upstream repository. Do not re-run unless the upstream project has had a major release that changes its structure.

**Explainer:** Identifies upstream module boundaries, tooling, and coding styles. Treat these as absolute constraints.

```markdown
Loop: LOOP-001
Goal: Discover the architecture of the upstream repository to understand its
conventions, module structure, and contribution constraints.
Scope: Full repository scan.
Output: docs/architecture/
Note: This is an open source contribution project. Treat all outputs as
READ-ONLY intelligence. The module boundaries, coding conventions, and
API patterns discovered here are constraints on your contribution —
not suggestions for improvement. Do not propose structural changes
unless the upstream project has explicitly invited them in its
CONTRIBUTING.md or in the issue you are addressing.
```

### LOOP-003 — Task Discovery

**When:** Once — your task backlog contains exactly one task (the contribution you intend to make).

**Explainer:** Confirms that the target issue is open, unassigned, and that the task record aligns with maintainer expectations.

```markdown
Loop: LOOP-003
Goal: Confirm the contribution task.
Backlog path: docs/loops/core/task-catalog.md
Note: For an open source contribution, there should be one task in the backlog
corresponding to the upstream issue or feature request you are addressing.
Before running this loop, confirm:
  - The upstream issue is open and not already assigned to another contributor.
  - The maintainer has indicated the contribution is welcome (look for
    "good first issue", "help wanted", or a direct response to your comment).
  - Your task record's acceptance_criteria matches the upstream issue's
    stated requirements exactly.
```

### LOOP-004 — Planning

**When:** After confirming the task. Keep scope minimal.

**Explainer:** Outlines a surgical patch. Restricts changes strictly to files required for the issue.

```markdown
Loop: LOOP-004
Goal: Produce an execution plan for [TASK-NNN].
Task: [paste your task record here]
Constraints for open source contribution:
  - Scope: touch only the files directly required to resolve the issue.
    A PR that changes 3 files is far more likely to be merged than one
    that changes 30.
  - Follow the upstream project's conventions exactly as captured by
    LOOP-001. Do not introduce new patterns, dependencies, or abstractions
    that are not already present in the codebase.
  - Do not include refactoring, formatting, or cleanup in the plan unless
    the upstream issue explicitly requests it.
  - Plan must include running the upstream project's existing test suite
    as the final verification step.
  - Plan must NOT propose changes to: project structure, build configuration,
    CI pipelines, or dependency versions unless the issue specifically requires it.
Await human approval. At the review gate, verify scope is minimal.
```

### LOOP-101 — Bug Fixing

**When:** Your contribution is a bug fix (the most common contribution type).

**Explainer:** Implements the fix. Stresses adding a localized test that reproduces the defect and passes after the fix.

```markdown
Loop: LOOP-101
Goal: Fix the defect described in [TASK-NNN] in the upstream repository.
Task: [paste your task record here]
Upstream issue: [link or description of the upstream issue]
Constraints:
  - Root cause first: document the root cause in engineering-analysis.md
    before proposing any fix. If the root cause is architectural, comment
    on the upstream issue rather than submitting a code fix.
  - The fix must use the patterns and abstractions already present in
    the upstream codebase. Do not introduce new patterns.
  - Do not change the public interface of any class, function, or module
    unless the upstream issue explicitly requires it.
  - Regression check: all upstream tests must pass after the fix.
  - Add a test that reproduces the defect before the fix and passes after.
    This is expected by most maintainers.
```

### LOOP-105 — Code Review

**When:** After implementation, before opening the PR. This simulates the maintainer's review so you resolve findings before they appear in the public review.

**Explainer:** Checks the code against the upstream project's style guide and checks for unapproved third-party dependencies.

```markdown
Loop: LOOP-105
Goal: Simulate the upstream maintainer's review of the contribution for [TASK-NNN].
Implementation artefacts: [path to changed files]
Review focus for open source contribution:
  - Is the code consistent with the upstream project's style and conventions?
  - Does the fix address only the stated issue — nothing more?
  - Are there any new dependencies introduced? (Most maintainers reject
    contributions that add dependencies without prior discussion.)
  - Does the new test reproduce the defect clearly?
  - Is the commit message format consistent with the upstream project's history?
  - Is there anything in the change that would require the maintainer to
    understand context outside of the PR itself? If yes, that context must
    be in the PR description.
Blocker: Any finding at High severity or above must be resolved before the PR
is opened. Do not rely on the maintainer to catch these in review.
```

### LOOP-006 — Verification

**When:** After LOOP-005. This is your PR readiness check. Do not open the PR until this returns Accepted.

**Explainer:** The final gateway. Blocks PR submission if any tests fail or if the verification confidence score is too low.

```markdown
Loop: LOOP-006
Goal: Verify the contribution is ready for upstream submission.
Implementation artefacts: [path to LOOP-005's implementation-summary.md]
Verification profile:
  - Category 1 (Functional correctness): MANDATORY
  - Category 2 (Regression testing): MANDATORY — all upstream existing tests must pass
  - Category 3 (Test coverage): MANDATORY — the new test must reproduce and then pass
  - Category 4 (Code quality): MANDATORY — no quality findings above Medium
  - Category 9 (Backward compatibility): MANDATORY — no breaking changes
  - Minimum confidence score: 75
PR readiness rule: Do not open the PR if the outcome is anything other than
Accepted. A Requires Rework or Requires Human Review outcome from LOOP-006
will become a reviewer finding — fix it before submission.
```

### LOOP-007 — Reflection

**When:** Automatically triggered at session end.

**Explainer:** Collects learnings regarding upstream maintainer responsiveness, review cycles, and project constraints.

```markdown
Loop: LOOP-007
Goal: Capture lessons from the contribution to [upstream project name].
Artefact set: [session artefact registry path]
Focus areas for open source contribution:
  - What did LOOP-001 reveal about the upstream project's conventions
    that was not obvious from reading the code?
  - What scope adjustments were made during planning and why?
  - What did LOOP-105's review reveal that would have been a PR comment?
Output: docs/reflection/
Note: LOOP-007 outputs are yours — they are not committed upstream.
They improve your effectiveness as a contributor to this and similar projects.
```

---

## Project Type 5 — Maintenance and Sustaining Engineering

*Stable production system. Defect fixes, security patches, dependency updates.*

### Loop Sequence and When to Use

| # | Loop | When to Use It | Key Gate/Constraint |
| :--- | :--- | :--- | :--- |
| 1 | **LOOP-001** | Monthly scheduled run. Immediately after any dependency upgrade or structural change. | Detects architectural drift or dependency updates. |
| 2 | **LOOP-002** | Automatically invoked — no manual trigger required. | Resolves exact dependency versions. |
| 3 | **LOOP-003** | Selects next task — SEC tasks always first, no exceptions. | Enforces SEC tasks take precedence over everything. |
| 4 | **LOOP-004** | Narrow plans only — BUG tasks exceeding 5 files need scrutiny. Stricter templates for SEC and DEP updates. | Reject BUG plans with > 5 files; require security approvals for SEC. |
| 5 | **LOOP-101** | For all BUG and SEC tasks. | Surgical defect/vulnerability patch; document root cause. |
| 6 | **LOOP-006** | Automatically invoked — regression detection is the primary value. | Regression is a CRITICAL finding. Escalate on 3rd failure. |
| 7 | **LOOP-007** | Automatically invoked — review output monthly to surface operational risk patterns. | Review monthly to flag structurally fragile modules. |

### LOOP-001 — Architecture Discovery (Scheduled)

**When:** Monthly. Also immediately after any dependency version upgrade or any commit that adds/removes modules.

**Explainer:** Run periodically to discover structural updates, new external dependencies, or unreviewed architectural drift.

```markdown
Loop: LOOP-001
Goal: Refresh the architecture discovery for this production repository.
Scope: Full repository scan.
Output: docs/architecture/
Note: Compare this run's dependency-map.md with the previous run.
Alert on any of the following changes:
  - A new external dependency that was not previously in the map
  - A module that has gained new inbound dependencies since the last scan
  - Any dependency whose version has changed since the last scan
These changes represent unreviewed architectural drift in a production system.
Flag them as ARCH tasks in the backlog if they require deliberate action.
```

### LOOP-003 — Task Discovery

**When:** Starting any work cycle. The priority ordering is enforced — do not override it.

**Explainer:** Backlog picking that strictly executes security tasks (SEC) first, checking SLA constraints dynamically.

```markdown
Loop: LOOP-003
Goal: Select the next task from the backlog.
Backlog path: docs/loops/core/task-catalog.md
Filter: status = ready
Priority order: SEC → BUG → DEP → PERF → RFCT → TEST
Important: SEC tasks at any priority_rank take precedence over all other
classifications. A SEC task filed at priority_rank 99 executes before a
BUG task at priority_rank 1. This is not configurable.
Return: The single highest-priority ready task with its full task record.
SLA check: If a SEC task in the backlog has a created_date older than 48 hours
and status = ready (not started), flag this as an SLA breach in the session notes.
```

### LOOP-004 — Planning (BUG Tasks)

**When:** Selected task is classified BUG.

**Explainer:** Creates an execution plan for a bug fix. Restricts scope to 5 files maximum and forbids opportunistic cleanup.

```markdown
Loop: LOOP-004
Goal: Produce an execution plan for [TASK-NNN] — bug fix.
Task: [paste your task record here]
Constraints for maintenance bug fixes:
  - Maximum 5 files modified. If the plan requires more than 5 files,
    return it. The defect is likely a symptom of a structural problem
    that needs an ARCH task, not a bug fix.
  - The plan must identify which existing tests cover the affected code.
    These are the regression baseline.
  - The plan must include a step to add or update a test that reproduces
    the defect. This test must fail before the fix and pass after.
  - The plan must NOT include opportunistic cleanup, refactoring, or
    style changes. One task, one purpose.
  - Rollback action must be specified for every step.
Await human approval.
```

### LOOP-004 — Planning (SEC Tasks)

**When:** Selected task is classified SEC. Use this instruction — it is stricter than the standard BUG plan instruction.

**Explainer:** Planning for security patches. Stresses specifying the attack vector, exposure window, and obtaining designated security reviewer approval.

```markdown
Loop: LOOP-004
Goal: Produce an execution plan for [TASK-NNN] — security patch.
Task: [paste your task record here]
CVE or vulnerability reference: [CVE number or description]
Constraints for security patches:
  - The plan must state the attack vector being addressed.
  - The plan must state the exposure window (when was this vulnerability
    introduced — which version or commit).
  - Changes must be minimal and surgical. Do not refactor around the fix.
  - If the fix requires a dependency version upgrade, the plan must include
    a step to verify no breaking changes in the upgraded dependency.
  - The plan must include verification that the attack vector is closed
    (not just that tests pass).
  - Notify channel: [your security notification channel] — SEC plans must
    be reviewed by a team member with security context, not just the author.
Await human approval. SEC plan approvals require a reviewer with security role.
```

### LOOP-004 — Planning (DEP Tasks)

**When:** Selected task is classified DEP (dependency update).

**Explainer:** Formulates the plan for updating a third-party dependency, isolating changes to a single library upgrade per task.

```markdown
Loop: LOOP-004
Goal: Produce an execution plan for [TASK-NNN] — dependency update.
Task: [paste your task record here]
Dependency to update: [dependency name, from version, to version]
Constraints for dependency updates:
  - The plan must include a step to review the dependency's changelog
    between the current version and the target version for breaking changes.
  - The plan must identify all modules that directly import this dependency.
  - The plan must identify all places where the dependency's API surface is used.
  - If the dependency has a new major version (breaking changes), the plan must
    include explicit steps for each call site that requires migration.
  - The plan must NOT batch multiple dependency updates in the same task.
    One dependency per task — this makes rollback clean.
  - Rollback: restoring the prior version must be specified as the rollback action.
Note: DEP tasks are verification exercises, not implementation exercises.
The value is in LOOP-006's regression detection, not in the version bump itself.
```

### LOOP-101 — Bug Fixing

**When:** Task is classified BUG or SEC and the plan is approved.

**Explainer:** Surgical implementation of a bug or vulnerability fix. Demands recording CVE vectors and adding reproduction unit tests.

```markdown
Loop: LOOP-101
Goal: Fix the defect or security issue described in [TASK-NNN].
Task: [paste your task record here]
Plan: [paste approved plan from LOOP-004]
Constraints:
  - Root cause first: document the root cause in engineering-analysis.md.
    If the root cause differs from the task record's description, halt
    and update the task record before proceeding.
  - The fix must be surgical. Touch only what is necessary to close the defect.
  - For SEC tasks: after implementation, document the remediation in
    engineering-analysis.md using the format:
      Attack vector: [description]
      Remediation: [what was changed and why it closes the vector]
      Residual risk: [any remaining exposure, if any]
  - Add or update the test that reproduces the defect as part of this run.
    Do not defer test addition to a separate task.
```

### LOOP-006 — Verification

**When:** Automatically triggered after LOOP-005. In maintenance projects this is the most important output — regression detection protects production.

**Explainer:** Enforces zero regression tolerance for production releases. Tripping verification three times halts the cycle for escalation.

```markdown
Loop: LOOP-006
Goal: Verify the fix produced for [TASK-NNN].
Implementation artefacts: [path to LOOP-005's implementation-summary.md]
Verification profile:
  - Category 1 (Functional correctness): MANDATORY
  - Category 2 (Regression testing): MANDATORY — any test passing at
    session_start_sha that fails now is a production regression
  - Category 3 (Test coverage): MANDATORY — the defect reproduction test must pass
  - Category 4 (Code quality): MANDATORY
  - Category 10 (Security) — for SEC tasks: MANDATORY
  - Minimum confidence score: 75
Production regression rule: A regression finding in a maintenance project
is always a CRITICAL severity finding. There is no "Low regression". A fix
that breaks something else is worse than the original defect in a production system.
Do not accept Requires Rework more than twice for the same task — on the third
rework cycle, halt and escalate to human review.
```

### LOOP-007 — Reflection

**When:** Automatically triggered at session end. Review the accumulated output monthly.

**Explainer:** Reviews learnings monthly to identify fragile modules, creating refactoring tickets to eliminate root-cause fragility.

```markdown
Loop: LOOP-007
Goal: Capture lessons from the fix for [TASK-NNN].
Artefact set: [session artefact registry path]
Focus areas for maintenance:
  - What was the actual root cause versus the initially reported cause?
  - Which module produced this defect — is this a recurring pattern in this module?
  - Was the regression baseline sufficient or were there coverage gaps?
  - How long did the vulnerability or defect exist before being reported?
Output: docs/reflection/
Monthly review instruction: At the end of each month, read
docs/reflection/lessons-learned.md and filter for lessons whose category
matches your most frequently failing modules. If the same module appears in
3 or more lessons, file an ARCH task to address its structural fragility.
```

---

## Cross-Type Reference — Loop Trigger Conditions

| Loop | Trigger Condition | Run Mode | Scope & Context |
| :--- | :--- | :--- | :--- |
| **LOOP-001** | Project initialization, major merges, dependency upgrades, or monthly maintenance check. | Manual | Full repository scan. |
| **LOOP-002** | Triggered immediately before planning any task. | **Automatic** | Gathers local module boundaries and definitions. |
| **LOOP-003** | When selecting the next work item from the backlog. | Manual | Backlog catalog matching priority filters. |
| **LOOP-004** | After a task is discovered by LOOP-003. | Manual | Restricts implementation steps and rollback criteria. |
| **LOOP-005** | When the execution plan from LOOP-004 receives human approval. | Manual | Surgical code edits. |
| **LOOP-101** | When the active task is classified as a BUG or SEC issue. | Manual | Isolated defect resolution. |
| **LOOP-102** | When the active task is classified as a RFCT (Refactoring) or ARCH migration. | Manual | Structure improvement; behavior-preserving. |
| **LOOP-103** | Greenfield: run with implementation. Modernisation: before refactoring. | Manual | Unit, integration, and characterization tests. |
| **LOOP-104** | Upon adding or updating a public API boundary or interface. | Manual | Documentation updates to catalog or architecture records. |
| **LOOP-105** | After implementation completes and before changes are merged. | Manual | Structural peer-review simulation. |
| **LOOP-006** | Triggered immediately after any code changes (LOOP-005/101/102). | **Automatic** | Functional, regression, and coverage check. |
| **LOOP-007** | Triggered at the end of every active loop session. | **Automatic** | Compiles lessons learned and reflection logs. |

---

## Common Mistakes — What Not to Do

| Mistake | Operational Risk | Correct Action |
| :--- | :--- | :--- |
| **Skipping LOOP-001 on adoption** | Downstream loops lack architectural boundaries and fail validation. | Always run `LOOP-001` first to establish catalogs. |
| **Running LOOP-102 without LOOP-103** | Modifying code without test coverage introduces silent regressions. | Verify line coverage is at least 70% before refactoring. |
| **Approving wide-scope BUG tasks** | Plan scopes that touch over 5 files obscure architectural flaws. | Reject plans with wide changes; file an ARCH task instead. |
| **Opening a PR on verification failure** | Submitting when `LOOP-006` returns "Requires Rework" wastes review time. | Resolve all verifier findings before staging a pull request. |
| **Batching dependency updates (DEP)** | Upgrading multiple libraries simultaneously makes rollbacks impossible. | Keep updates isolated: strictly one library upgrade per task. |
| **Skipping reflection (LOOP-007)** | Canceling reflection blocks the accumulation of developer intelligence. | Let `LOOP-007` execute to summarize insights for future runs. |
| **Deferring SEC tasks for features** | Prioritizing features over vulnerability patches breaches security SLAs. | Keep `SEC` tasks at the top of the queue; run them first. |
| **LOOP-110** | Legacy Strangler | Engineering | Medium | LOOP-002 — Context Assembly, LOOP-004 — Planning, LOOP-006 — Verification | Auto-generated standard template execution for Legacy Strangler. |
| **LOOP-112** | Component Deprecation Lifecycle | Engineering | Medium | LOOP-002 — Context Assembly, LOOP-004 — Planning, LOOP-006 — Verification | Auto-generated standard template execution for Component Deprecation Lifecycle. |
| **LOOP-113** | Dead Code Elimination | Engineering | Medium | LOOP-002 — Context Assembly, LOOP-004 — Planning, LOOP-006 — Verification | Auto-generated standard template execution for Dead Code Elimination. |
| **LOOP-130** | Localization and Internationalization Audit | Engineering | Medium | LOOP-002 — Context Assembly, LOOP-004 — Planning, LOOP-006 — Verification | Auto-generated standard template execution for Localization and Internationalization Audit. |
| **LOOP-160** | Database Deadlock Resolution | Engineering | Medium | LOOP-002 — Context Assembly, LOOP-004 — Planning, LOOP-006 — Verification | Auto-generated standard template execution for Database Deadlock Resolution. |
| **LOOP-161** | Memory Leak Detection | Engineering | Medium | LOOP-002 — Context Assembly, LOOP-004 — Planning, LOOP-006 — Verification | Auto-generated standard template execution for Memory Leak Detection. |
| **LOOP-171** | Secrets Lifecycle Enforcement | Engineering | Medium | LOOP-002 — Context Assembly, LOOP-004 — Planning, LOOP-006 — Verification | Auto-generated standard template execution for Secrets Lifecycle Enforcement. |
| **LOOP-181** | Container Layer Optimization | Engineering | Medium | LOOP-002 — Context Assembly, LOOP-004 — Planning, LOOP-006 — Verification | Auto-generated standard template execution for Container Layer Optimization. |
| **LOOP-308** | Contract-to-Code Enforcement | Governance | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Contract-to-Code Enforcement. |
| **LOOP-309** | License Compliance Audit | Governance | Medium | LOOP-006 — Verification | Auto-generated standard template execution for License Compliance Audit. |
| **LOOP-310** | Infrastructure Cost Attribution | Governance | Medium | LOOP-007 — Reflection | Auto-generated standard template execution for Infrastructure Cost Attribution. |
| **LOOP-311** | Feature Access Entitlement | Governance | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Feature Access Entitlement. |
| **LOOP-312** | Data Privacy Anonymization | Governance | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Data Privacy Anonymization. |
| **LOOP-206** | Observability Validation | Platform | Medium | LOOP-005 — Implementation | Auto-generated standard template execution for Observability Validation. |
| **LOOP-207** | Security Validation | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Security Validation. |
| **LOOP-208** | Data Migration | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Data Migration. |
| **LOOP-210** | API Shadow IT Discovery | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for API Shadow IT Discovery. |
| **LOOP-213** | Multi-Region State Sync | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Multi-Region State Sync. |
| **LOOP-214** | Resource Quota Guardrail | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Resource Quota Guardrail. |
| **LOOP-215** | Secret Leakage Prevention | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Secret Leakage Prevention. |
| **LOOP-216** | Database Index Optimization | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Database Index Optimization. |
| **LOOP-217** | System Event Idempotency | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for System Event Idempotency. |
| **LOOP-218** | Backward Compatibility Verification | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Backward Compatibility Verification. |
| **LOOP-219** | Load Balancing Anomaly Mitigation | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Load Balancing Anomaly Mitigation. |
| **LOOP-220** | API Rate Limiting Guardrail | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for API Rate Limiting Guardrail. |
| **LOOP-221** | Accessibility Compliance Guardrail | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Accessibility Compliance Guardrail. |
| **LOOP-222** | Telemetry Anomaly Detection | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Telemetry Anomaly Detection. |
| **LOOP-223** | Multi-Cloud Disaster Recovery | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Multi-Cloud Disaster Recovery. |
| **LOOP-224** | Edge Cache Invalidation | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Edge Cache Invalidation. |
| **LOOP-225** | Cross-Site Scripting Guardrail | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Cross-Site Scripting Guardrail. |
| **LOOP-226** | Tenant Onboarding Validation | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Tenant Onboarding Validation. |
| **LOOP-227** | Third-Party Webhook Reliability | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Third-Party Webhook Reliability. |
| **LOOP-228** | Log Aggregation Sanity | Platform | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Log Aggregation Sanity. |
| **LOOP-401** | Release Checklist | Release | Medium | LOOP-304 — Release Readiness | Auto-generated standard template execution for Release Checklist. |
| **LOOP-402** | Deployment Validation | Release | Medium | LOOP-401 — Release Checklist | Auto-generated standard template execution for Deployment Validation. |
| **LOOP-403** | Post-Release Verification | Release | Medium | LOOP-402 — Deployment Validation | Auto-generated standard template execution for Post-Release Verification. |
| **LOOP-407** | Synthetic User Verification | Release | Medium | LOOP-006 — Verification | Auto-generated standard template execution for Synthetic User Verification. |

---

*AEOS Loop Instructions — Generic Edition. Replace bracketed values before submitting.*

## Additional Specialized Loops

### LOOP-107 — Minimal System Diagram Generation

**When:** Run on-demand when system architecture diagrams are missing or outdated.

**Explainer:** Generates a core suite of architectural system diagrams from current state.

`markdown
Loop: LOOP-107
Goal: Generate and verify a core suite of architectural system diagrams.
Expected output: Verified and updated architecture diagrams.
`

### LOOP-408 — Delivery Change Steward

**When:** Run on-demand for delivery and change stewardship.

**Explainer:** Oversees release and delivery changes for governance.

`markdown
Loop: LOOP-408
Goal: Delivery and Change Stewardship.
Expected output: Validated changes ready for delivery.
`

### LOOP-502 — Product Intelligence Architect

**When:** Run on-demand for product intelligence.

**Explainer:** Oversees product intelligence and architectural decisions.

`markdown
Loop: LOOP-502
Goal: Product intelligence architecture analysis.
Expected output: Strategic product intelligence insights.
`

### LOOP-504 — Knowledge Integrity Steward

**When:** Run on-demand for knowledge integrity.

**Explainer:** Oversees documentation and knowledge integrity across the project.

`markdown
Loop: LOOP-504
Goal: Ensure knowledge integrity.
Expected output: Verified and aligned documentation knowledge base.
`

