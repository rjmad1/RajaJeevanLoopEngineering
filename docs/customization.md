# Customizing Loops and Checkers

The Loop Engineering Framework is highly extensible. Developers can easily write custom loops, define application-specific gate structures, and build custom rule evaluators.

---

## 1. Creating a Custom Loop Spec

1. Copy the standard `templates/LOOP-TEMPLATE.md` to your local execution folder.
2. Define a unique ID (e.g. `LOOP-501` for custom workflows).
3. Specify your required inputs, preconditions, and outputs.
4. Set up Maker and Checker assignments under the `## Agents` section.
5. Define the step-by-step workflow.

---

## 2. Implementing Custom Verification Rules

> [!NOTE]
> **Not Implemented in Current Release:** The Java classes `ConditionEvaluator`, `Condition`, and `ExecutionContext` are not implemented in the current standalone Loop Engine codebase. 

Instead, custom verification checks should be implemented within your client-side agent runner or validation scripts (e.g. Python scripts, Shell tasks). The Checker agent evaluates the output, logs the results, and communicates the binary pass/fail result to the Loop Engine by making a state transition API call.

For example, a custom python validator would evaluate the conditions locally and invoke `loop-control.sh`:
```python
def verify_output(artifact_path):
    # Run custom linter or scanner checks locally
    success = run_custom_security_scan(artifact_path)
    if success:
        # Transit state to VERIFICATION or PLANNING
        os.system("./loop-control.sh transit my-loop IMPLEMENTATION VERIFICATION")
    else:
        # Record failure (will increment consecutive failures)
        os.system("./loop-control.sh transit my-loop IMPLEMENTATION IMPLEMENTATION 'Security checks failed'")
```

---

## 3. Defining Custom Gates

You can hook custom gate triggers in your orchestrator (like Temporal, Airflow, or custom script engines) by matching the gate IDs (e.g., `GATE-1`, `GATE-2`) defined in the markdown spec:

- **Hard Gate integration:** Hook your PR creation step. When the runner encounters `Hard Gate`, it halts the pipeline, posts a Slack message or GitHub review request, and waits for a webhook sign-off.
- **Soft Gate integration:** Set a timer (e.g. `DurationSeconds = 300`). Send a notification. If the timer fires without an alert cancellation, proceed to the next step.
