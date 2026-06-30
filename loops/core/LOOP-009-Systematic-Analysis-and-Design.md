---
# PROVENANCE METADATA
Original Path: loops/core/LOOP-009-Systematic-Analysis-and-Design.md
Original Version: 1.0
Extraction Date: 2026-06-30
Original Purpose: Systematically transform any subject into an enterprise-grade, expert-level analysis and design.
Generalized Purpose: Systematically transform any subject into an enterprise-grade, expert-level analysis and design.
Dependencies Removed: None
Dependencies Retained: None
Compatibility Notes: Fully compatible with standard loop orchestrators and documentation frameworks.
Migration Notes: N/A
---
# LOOP-009 — Systematic Analysis and Design

**Loop ID:** LOOP-009
**Name:** Systematic Analysis and Design
**Version:** 1.0
**Status:** Active
**Category:** Core
**Depends On:** None
**Human Gates:** Soft
**Owner:** Principal Architecture Function
**Maintainer:** Principal Architecture Function

---

## Purpose

To establish a reusable, repeatable, and exhaustive reasoning and design framework that systematically transforms any subject or problem space into an enterprise-grade, expert-level analysis and design. This loop enforces continuous iteration and self-challenge, refining the target design until no material gaps, hidden assumptions, undocumented risks, or architectural weaknesses remain.

---

## Problem Statement

Ad-hoc engineering analysis and design prompts frequently result in solutions that look plausible but suffer from critical omissions: unstated or weak assumptions, overlooked edge cases, missing regulatory or compliance considerations, single-point-of-failure vulnerabilities, and unjustified architectural choices. Without a structured, multi-phase loop that systematically understand, discovers, decomposes, analyzes, designs, challenges, validates, and optimizes a problem space, the resulting designs contain high technical debt and require significant, costly refactoring downstream.

---

## Why This Loop Exists

Systematic analysis and design requires high cognitive discipline and is prone to confirmation bias. Codifying the reasoning framework as a formal execution loop forces the agent to play both "Maker" and "Checker" roles, systematically iterating and refining the solution from first principles. It ensures that every architectural recommendation is evidence-based, every risk is quantified, and the final design is demonstrably aligned with business objectives.

---

## Scope

**In scope:**
- Analyzing any given subject, topic, capability, system, or organizational domain (e.g., RBAC, IAM, Enterprise Architecture, Governance, AI, Cloud, Business Capabilities).
- Iteratively refining the problem statement, business objectives, and success criteria.
- Executing systematic discovery, decomposition, analysis, and design phases.
- Critically challenging and validating the proposed design against operational, technical, and security principles.
- Optimizing the design for simplicity, reusability, and risk reduction.
- Enforcing a strict Output Contract.

**Out of scope:**
- Implementing the actual designed code or infrastructure (this is deferred to LOOP-005 — Implementation).
- Running runtime system verification tests (LOOP-006).
- Creating new workflows or task backlogs outside the domain of the selected subject.

**Maximum run duration:** 4 hours.

---

## Inputs

| Input | Type | Source | Required |
|-------|------|--------|----------|
| `INPUT_TOPIC` | Configuration / Text | User Prompt | Required |
| `OPTIONAL_CONTEXT` | Configuration / Text | User Prompt / Filesystem | Optional |
| `OPTIONAL_CONSTRAINTS` | Configuration / Text | User Prompt / Filesystem | Optional |

### Input Validation

- Ensure `INPUT_TOPIC` is defined and contains a non-empty string.
- If context or constraints files are specified, verify their existence and readability.

---

## Outputs

All outputs are written to `docs/analysis/`. On first run, this directory is created; on subsequent runs, files are updated in place.

| Artifact | Path | Description |
|----------|------|-------------|
| Systematic Analysis & Design | `docs/analysis/analysis-and-design-LOOP-009.md` | The final structured output conforming to the Output Contract |
| Loop Status | `docs/loops/core/STATUS-009.md` | Run state, metrics, and open blockers for this loop |
| Loop Skill | `docs/loops/core/SKILL-009.md` | Calibration knowledge accumulated across runs |
| Run Metadata | `docs/analysis/metadata/METADATA-009-{run-id}.md` | Provenance: run ID, duration, and status |
| Reflection | `docs/analysis/reflections/REFLECTION-009-{run-id}.md` | Per-run structured reflection |

---

## Dependencies

None. This is a chain-head loop that functions as a general reasoning framework.

---

## Trigger

A run is initiated by any of the following:
1. **Manual invocation** — An engineer or agent explicitly triggers the loop with a topic to analyze.
2. **Upstream loop trigger** — A task discovery or planning step requires detailed capability design before implementation can proceed.

---

## Preconditions

| ID | Precondition | Check Method |
|----|-------------|--------------|
| PRE-1 | Executing agent has write access to `docs/analysis/` | Verify directory write permissions |
| PRE-2 | `INPUT_TOPIC` is provided and valid | Check inputs for non-empty string |

---

## External State

None. This loop is fully self-contained and does not modify external databases, networks, or non-repository environments.

---

## Required Context

Before beginning Step 1, the executing agent must have loaded:
1. `docs/loops/shared/LOOP-STANDARD.md` — governing standard for loop execution
2. `docs/loops/core/LOOP-009-Systematic-Analysis-and-Design.md` — this document

---

## Agents

| Agent ID | Role | Responsibilities | Tools | Human Oversight |
|----------|------|-----------------|-------|-----------------|
| `DESIGN-MAKER` | Maker | Steps 1–5, 8–9: understands, discovers, decomposes, designs, optimizes, and compiles output | Analysis tools | Reports progress to reviewer |
| `DESIGN-CHALLENGER` | Checker | Steps 6–7: challenges assumptions, checks edge cases, validates against objectives | Verification tools | Soft gate reviewer |

---

## Workflow

The loop executes through 9 sequential, iterative phases. At any phase, if a material gap or verification failure is identified, execution must return to the relevant previous phase.

### LOOP 1 — Understand
Determine:
- What problem is actually being solved.
- Why the problem exists.
- Who is affected.
- Desired business outcomes.
- Success criteria.
- Constraints.
- Assumptions.
- Unknowns.

*If uncertainty exists, identify it explicitly rather than guessing.*

### LOOP 2 — Discover
Identify everything required before designing a solution. Discover:
- Business context, Stakeholders, Capabilities, Processes, Systems, Data, Security, Governance, Compliance, Risks, Dependencies, Existing state, Target state.

*Continue discovery until no critical unknowns remain.*

### LOOP 3 — Decompose
Break the problem into logical components. Identify:
- Domains, Subdomains, Capabilities, Services, Functions, Interfaces, Dependencies, Decision points.

*Continue decomposition until each component can be solved independently.*

### LOOP 4 — Analyze
For every component:
- Determine objectives and requirements.
- Identify assumptions, constraints, and risks.
- Identify alternatives and explain trade-offs.
- Justify recommendations.

*Never recommend a solution without explaining why it is appropriate.*

### LOOP 5 — Design
Design the capability from first principles. Define:
- Architecture, Operating model, Governance, Roles and responsibilities, Processes, Policies, Controls, Technology, Integration, Lifecycle, Metrics, Continuous improvement.

*Design for scalability, maintainability, security, auditability, and future adaptability.*

### LOOP 6 — Challenge
Critically review the proposed design. Ask:
- What assumptions are weak?
- What evidence is missing?
- What risks remain?
- What edge cases exist?
- What failure modes exist?
- What alternatives were ignored?
- What dependencies were overlooked?

*Revise the design until these questions produce no material deficiencies.*

### LOOP 7 — Validate
Validate against:
- Business objectives, Technical feasibility, Security principles, Governance principles, Compliance obligations, Operational practicality, Scalability, Maintainability, Cost, Performance, Future readiness.

*If validation fails, return to the appropriate previous loop.*

### LOOP 8 — Optimize
Improve:
- Simplicity, Consistency, Reusability, Automation, Risk reduction, Performance, Governance, User experience, Operational efficiency.

*Repeat optimization until improvements become marginal.*

### LOOP 9 — Final Review
Before producing the final response verify:
- [ ] No unsupported assumptions remain.
- [ ] Missing information is identified.
- [ ] Recommendations are evidence-based.
- [ ] Trade-offs are explained.
- [ ] Risks are documented.
- [ ] Decisions are justified.
- [ ] Architecture is internally consistent.
- [ ] Outputs align with stated objectives.

*If any verification fails, return to the relevant loop and refine.*

---

## Output Contract

Every run must produce a structured response at `docs/analysis/analysis-and-design-LOOP-009.md` containing the following sections:

1. **Executive Summary** — High-level summary of the analysis and key recommendations.
2. **Problem Definition** — Clear statement of what problem is being solved, why it exists, and who is affected.
3. **Discovery Findings** — Detailed summary of capabilities, systems, data, and compliance context discovered.
4. **Requirements** — Prioritized functional and non-functional requirements.
5. **Architecture / Design** — Detailed design, component breakdown, operating model, policies, and controls.
6. **Alternatives Considered** — Clear mapping of alternative paths explored.
7. **Trade-off Analysis** — Structured evaluation of pros and cons for each alternative.
8. **Risk Assessment** — Quantified risk register with mitigation strategies.
9. **Governance Considerations** — Roles, responsibilities, policies, and auditability requirements.
10. **Implementation Approach** — Phased deployment, sequencing, and migration strategy.
11. **Validation Results** — Scorecard showing validation against all business and technical principles.
12. **Recommendations** — Justified, evidence-based recommendations.
13. **Open Questions** — Remaining areas of uncertainty requiring human stakeholder input.
14. **Assumptions** — Explicit list of all assumptions relied upon.
15. **Next Actions** — Discrete, actionable next steps.

---

## Quality Controls

- **Never fabricate facts.** State "No verified information" when evidence is insufficient.
- Clearly distinguish facts, assumptions, and recommendations.
- Challenge your own conclusions before presenting them.
- Prefer first-principles reasoning over convention.
- Optimize for correctness, completeness, traceability, and reproducibility.
- Continue iterating through the loop until no significant improvements can be identified or additional information is required to proceed.

---

## Verification

The agent must verify that:
- [ ] The output file `docs/analysis/analysis-and-design-LOOP-009.md` contains all 15 sections of the Output Contract.
- [ ] No placeholder tags or TODOs remain in the output.
- [ ] Every recommendation is backed by a corresponding trade-off analysis and risk assessment.

---

## Failure Recovery

- If validation fails, immediately roll back the working draft to the state at the end of the last successful phase, record the failure mode, and restart iteration from the most upstream affected loop.

---

## Metrics

| Metric | Description |
|--------|-------------|
| `run.duration_seconds` | Total execution time |
| `run.status` | Final execution status (`completed`, `failed`) |
| `analysis.iterations` | Number of loops back to earlier steps during execution |
| `analysis.risks_identified` | Total number of risks documented in the final output |

---

## Risks

- **RISK-1: Analysis Paralysis** — Iterations could run indefinitely without converging. (Mitigation: Maximum duration check forces exit after 4 hours).
- **RISK-2: Unsupported Recommendations** — Recommending solutions based on unverified assumptions. (Mitigation: Checked strictly in LOOP-9).

---

## Stop Conditions

- **SC-1** — Output document compiles fully and passes all validation checks in LOOP-7 and LOOP-9.
- **SC-2** — Run duration exceeds 4 hours.

---

## References

- `docs/loops/shared/LOOP-STANDARD.md`

---

## Version History

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0 | 2026-06-30 | Principal AI Engineering Architect | Initial active version establishing systematic analysis framework. |
