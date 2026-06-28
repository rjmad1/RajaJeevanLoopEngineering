---
# PROVENANCE METADATA
Original Path: docs/loops/engineering/LOOP-107-Minimal-System-Diagram-Generation.md
Original Version: 1.0
Extraction Date: 2026-06-28
Original Purpose: Continuously produce and maintain the complete minimal architecture diagram set.
Generalized Purpose: Generate and verify a core suite of architectural system diagrams.
Dependencies Removed: None
Dependencies Retained: LOOP-001 — Architecture Discovery, LOOP-002 — Context Assembly
Compatibility Notes: Fully compatible with standard loop orchestrators and documentation frameworks.
Migration Notes: New loop based on user specification.
---
# LOOP-107 — Minimal System Diagram Generation

**Loop ID:** LOOP-107
**Name:** Minimal System Diagram Generation
**Version:** 1.0
**Status:** Active
**Category:** Engineering
**Depends On:** LOOP-001 — Architecture Discovery, LOOP-002 — Context Assembly
**Human Gates:** Hard, Soft
**Owner:** Principal Engineering Function
**Maintainer:** Principal Engineering Function

---

## Purpose

LOOP-107 continuously produces and maintains the complete minimal architecture diagram set until every required diagram exists, passes quality checks, and accurately reflects the current system. This loop combines research/discovery, artifact generation, and iterative validation as recommended in the Loop Engineering architecture.

---

## Scope

**In scope:**
- System Context Diagram (C4 L1)
- Container Diagram (C4 L2)
- Happy Path Sequence Diagram
- Domain Model
- State Machine
- Data Flow Diagram
- Deployment Diagram
- Architecture Review Report
- Gap Analysis

**Out of scope:**
- Code implementation
- Testing (non-diagrams)

**Limits:**
- Hard limit: 25 iterations, 150k tokens, or human stop.

---

## Inputs

| Input | Type | Source | Required |
|-------|------|--------|----------|
| Product requirements | Document | Repository / LOOP-002 | Required |
| Existing architecture | Documents | LOOP-001 | Required |
| Source code | Files | LOOP-002 | Required |
| Infrastructure | Config | LOOP-002 | Required |
| APIs | Specs | LOOP-002 | Required |
| Database schemas | Specs | LOOP-002 | Required |
| Engineering interviews | Notes | Repository | Optional |
| Diagram specification | Spec | Repository | Required |

---

## Outputs

| Artifact | Path | Description |
|----------|------|-------------|
| System Diagrams | `docs/architecture/diagrams/` | The generated diagrams (C4, Sequence, etc.) |
| Loop Status | `STATUS-107.md` | Run status, metrics, and open blockers |
| Loop Skill | `SKILL-107.md` | Calibration observations accumulated across runs |
| Diagram Index | `DIAGRAMS.md` | Index of all generated and verified diagrams |
| Gap Analysis | `GAPS.md` | Record of missing or inadequate diagrams |
| Review Report | `REVIEW.md` | Results of diagram reviews against rubric |

---

## Pattern

**Discovery Loop** → **Draft–Refine Loop** → **Verification Loop**

---

## Agents

| Agent           | Responsibility                       |
| --------------- | ------------------------------------ |
| Discovery       | Collect architecture knowledge       |
| Planner         | Decide next missing diagram          |
| Diagram Builder | Produce diagram                      |
| Reviewer        | Compare against checklist            |
| Domain Expert   | Validate terminology                 |
| Reflector       | Update STATUS.md and lessons learned |

---

## Stopping Criteria

- All required diagrams exist.
- Every diagram contains the mandatory fields.
- No missing architecture components.
- All review checks pass.
- Stakeholders approve.

---

## Verification Rubric

Every generated diagram is checked against the minimum requirements.

### System Context
- **Verify:** system boundary, external actors, external systems, high-level flows
- **Reject if:** databases shown, services shown, implementation details shown

### Container
- **Verify:** UI, Gateway/BFF, Services, Datastores, Queues, Integrations
- **Reject if:** responsibilities unclear, excessive granularity

### Sequence
- **Verify:** trigger, request path, reads, writes, external calls, response, timeout, retries
- **Reject if:** writes omitted, failure path missing

### Domain Model
- **Verify:** bounded contexts, entities, relationships, ownership
- **Reject if:** ER diagram, database schema, God Domain

### State Machine
- **Verify:** states, transitions, invalid transitions, retry paths, terminal states
- **Reject if:** failure states omitted

### Data Flow
- **Verify:** trust boundaries, encryption, PII, audit logging, retention
- **Reject if:** unlabeled sensitive data

### Deployment
- **Verify:** environments, regions, ingress, compute, cache, database, networking
- **Reject if:** logical architecture confused with runtime

---

## Loop Lifecycle

```
START
↓
Load STATUS.md
↓
Discover current documentation
↓
Identify missing diagram
↓
Generate diagram
↓
Review against checklist
↓
Pass?
├── No
│  Record deficiencies
│  Update STATUS.md
│  Improve diagram
│
└── Yes
↓
Persist diagram
↓
More diagrams missing?
├── Yes
│     Continue
│
└── No
↓
Architecture Review
↓
Human Approval
↓
END
```

---

## Reflection Step

After every iteration record:
- Completed Diagram
- Reviewer Score
- Missing Information
- Questions for SMEs
- Architecture Risks
- Lessons Learned

---

## Human Approval Gates

Pause when:
- bounded context ownership is unclear
- conflicting documentation exists
- security classification is unknown
- deployment topology cannot be inferred
- reviewer confidence < 4/5

---

## Risk Controls

- Maker and Reviewer must be separate (avoid self-verification).
- Persist progress to `STATUS.md` after every iteration.
- Use fresh context each iteration to avoid context drift.
- Halt after three consecutive verification failures and require human review.

---

### Success Criteria

The loop completes when the architecture repository contains a complete, internally consistent diagram set satisfying the checklist from the "Minimal System Diagram Set" reference and passing independent verification before the loop terminates.
