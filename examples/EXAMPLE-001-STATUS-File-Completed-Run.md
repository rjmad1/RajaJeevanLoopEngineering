---
# PROVENANCE METADATA
Original Path: docs/loops/examples/EXAMPLE-001-STATUS-File-Completed-Run.md
Original Version: 1.0
Extraction Date: 2026-06-27
Original Purpose: Loop specification or framework asset.
Generalized Purpose: Loop specification or framework asset.
Dependencies Removed: RajaJeevanLoopEngineering business workflow configurations
Dependencies Retained: None
Compatibility Notes: Fully compatible with standard loop orchestrators and documentation frameworks.
Migration Notes: Direct copy of the general loop framework specification.
---
# EXAMPLE-001 — STATUS-001.md: Completed Run

<!-- This file is a worked example demonstrating what a correctly populated STATUS-001.md looks like after a successful LOOP-001 scheduled run. It follows the structure defined in docs/loops/templates/STATUS-TEMPLATE.md. Use this as the primary reference when writing or testing a loop runtime. -->

---

## What This Example Shows

This is the STATUS file state for LOOP-001 after its second-ever run (RUN-001, 2026-06-27), a scheduled refresh that found 3 new unknowns and triggered GATE-2 (Soft Gate). GATE-2 auto-proceeded after the 24-hour timeout. All 13 steps completed. All 10 verification criteria passed.

The prior run (RUN-000, 2026-06-26) was a first-ever manual run with no prior state.

---

## STATUS File

```yaml
loop_id: "LOOP-001"
current_status: "idle"
# Valid values: idle | running | completed | failed | stopped | precondition_failed | blocked_on_dependency | emergency_stopped

current_run_id: null
# Null because the loop is idle between runs.

current_task_id: null
# Null when idle.

last_updated: "2026-06-27T16:42:00Z"
# Timestamp of the write at the end of Step 11 (Update STATUS-001.md) of RUN-001.

last_completed_run: "LOOP-001-20260627-001"
# The run ID of RUN-001, which completed successfully.

last_outcome: "completed"
# RUN-001 reached all Stop Conditions and produced all required artifacts.

open_blockers: []
# No open blockers. The three new unknowns (UNK-041, UNK-042, UNK-043) are recorded in
# docs/architecture/unknowns.md with status "open" but do not block a future run — they
# are inputs to the next discovery pass, not execution blockers.

gate_outcomes:
  GATE-2:
    gate_type: "Soft"
    trigger_condition: "Unknown count increased by 3 since prior run (UNK-041, UNK-042, UNK-043)"
    reviewer: "auto-proceeded"
    reviewer_role: "Any engineer with repository write access"
    decision: "auto-proceeded"
    rationale: "No objection received within 24-hour timeout window"
    timestamp: "2026-06-26T14:05:00Z"
    # Note: timestamp records when the gate fired, not when it resolved.
    # The auto-proceed resolved at 2026-06-27T14:05:00Z (24 hours later),
    # at which point Step 9 began.

emergency_stopped: false
```

---

## Run History

| Run ID | Date | Trigger | Outcome | Steps Completed | Gate Outcomes | Notes |
|--------|------|---------|---------|-----------------|---------------|-------|
| LOOP-001-20260627-001 | 2026-06-27 | scheduled | completed | 13/13 | GATE-2 auto-proceeded | First refresh run after major platform refactor |
| LOOP-001-20260626-000 | 2026-06-26 | manual | completed | 13/13 | none fired | First-ever run (first_run=true) |

---

## Metrics — Most Recent Run (LOOP-001-20260627-001)

### Standard Metrics (Required by LOOP-STANDARD §11)

| Metric | Value |
|--------|-------|
| `run.duration_seconds` | 4823 |
| `run.status` | completed |
| `run.steps_completed` | 13 |
| `run.steps_total` | 13 |
| `gate.hard.count` | 0 |
| `gate.hard.approved` | 0 |
| `gate.hard.denied` | 0 |
| `gate.soft.count` | 1 |
| `gate.soft.auto_proceeded` | 1 |
| `verification.level1.pass` | 10 |
| `verification.level1.fail` | 0 |
| `reflection.produced` | true |

### LOOP-001-Specific Metrics

| Metric | Value |
|--------|-------|
| `discovery.files_analyzed` | 2847 |
| `discovery.files_excluded` | 143 |
| `discovery.scan_gaps` | 0 |
| `discovery.modules_found` | 11 |
| `discovery.services_found` | 9 |
| `discovery.apis_found` | 47 |
| `discovery.events_found` | 23 |
| `discovery.adrs_found` | 12 |
| `discovery.technical_debt_items` | 34 |
| `discovery.unknowns_open` | 3 |
| `discovery.unknowns_resolved_this_run` | 2 |
| `discovery.unknowns_new_this_run` | 3 |
| `coverage.repository_pct` | 94 |
| `coverage.documentation_pct` | 82 |
| `confidence.modules` | 91 |
| `confidence.services` | 88 |
| `confidence.apis` | 76 |
| `confidence.events` | 84 |
| `confidence.schemas` | 79 |
| `drift.added` | 7 |
| `drift.removed` | 1 |
| `drift.changed` | 4 |
| `drift.magnitude` | 12 |

---

## Open Issues

| ID | Description | Opened | Assigned To | Resolution |
|----|-------------|--------|-------------|------------|
| _(none)_ | — | — | — | — |

---

## Skill Observations Pending

_(none pending)_

---

## Annotation Notes

The following notes explain choices that may not be obvious from the field values alone. These annotations appear only in this example file; a real STATUS-001.md does not include them.

**On `gate_outcomes` containing only GATE-2:**
The `gate_outcomes` map holds outcomes for gates that fired in the most recent run. GATE-1 did not fire in RUN-001 (confidence scores were all above 60, no module was removed, drift magnitude was 12 — below the 20-item threshold, no concurrent change detected). Only GATE-2 fired. If GATE-1 had also fired in a prior run, its record would not appear here; STATUS holds the current run's gate state. The full gate history for all runs is preserved in the Reflection artifacts.

**On `open_blockers: []`:**
The three new unknowns (UNK-041 through UNK-043) are not represented as blockers. Unknowns are expected outputs of discovery; they live in `docs/architecture/unknowns.md`. A blocker in STATUS represents something that prevents the *next run* from beginning or completing. No such condition exists here.

**On `discovery.unknowns_resolved_this_run: 2`:**
Two unknowns from RUN-000 were resolved in this run. UNK-039 (purpose of `shared/execution/provider/` directory) was resolved when Step 5 discovered and parsed the `ProviderClient.java` and `WhatsAppProvider.java` entry points added in the refactor. UNK-040 (purpose of `platform/integrations/` module) was resolved when the `OAuthTokenExchangeService.java` class name and associated test made the module's responsibility unambiguous.

**On `coverage.repository_pct: 94`:**
The 6% uncovered is accounted for: 3% is generated protobuf output in `build/generated/`; 3% is a `platform/legacy/` subdirectory flagged as UNK-043 (no README, no build entry, no evident production consumer). Neither gap triggers GATE-1 because no item in either category has evidence strength above 80%.

