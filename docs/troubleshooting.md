# Troubleshooting Guide

This guide covers common issues encountered during loop setup, execution, and verification, along with remediation steps.

---

## 1. Loop Run Hangs or Fails to Terminate

### Symptoms
- The agent runs indefinitely without producing outputs.
- Token consumption climbs rapidly.

### Causes
- Missing or misconfigured `Max Run Duration` in the loop specification.
- Recursive loops or infinite retry policies on failure events.
- Hard Gate blocking execution without notification channels set up.

### Resolution
- Check that the runner parses and respects `Max Run Duration`.
- Verify the retry count in `RetryPolicy` (default is 3, make sure it is not set to infinite).
- Check the run's `STATUS` document to see if a Hard Gate is active. Locate the approver and record approval or termination.

---

## 2. Condition Evaluation returns False unexpectedly

### Symptoms
- The step fails postcondition checks even though outputs look correct.

### Causes
- The dot-notation variable path in `Condition` field does not exist in `ExecutionContext` variables.
- Case-sensitivity differences or type mismatches (e.g. comparing numeric `500` to string `"500"` using strict comparator).

### Resolution
- Add debug logging in `ConditionEvaluator` to print the resolved variables map.
- Ensure that expected values are formatted correctly (the evaluator compares string representations for basic equivalence and parses doubles for numeric comparisons).

---

## 3. Provenance Check Fails

### Symptoms
- Upstream dependencies reported as stale.
- Git SHA checks return mismatched errors.

### Causes
- The branch HEAD changed since the last execution of LOOP-001.
- Running loops out of order (e.g., executing LOOP-005 without updating LOOP-002 context).

### Resolution
- Always execute loop sequences sequentially: `Discovery` -> `Context` -> `Planning` -> `Implementation` -> `Verification`.
- Re-run `LOOP-001` to refresh the architecture catalog before starting a new execution plan.
