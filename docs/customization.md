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

You can extend `ConditionEvaluator` or add custom logic to execute complex checks:

```java
public class SecurityChecksEvaluator extends ConditionEvaluator {
    
    @Override
    public boolean evaluate(Condition condition, ExecutionContext context) {
        if ("security.scan.failed".equals(condition.getField())) {
            // Implement custom integration validation
            return runCustomSecurityScan(context);
        }
        return super.evaluate(condition, context);
    }
}
```

---

## 3. Defining Custom Gates

You can hook custom gate triggers in your orchestrator (like Temporal, Airflow, or custom script engines) by matching the gate IDs (e.g., `GATE-1`, `GATE-2`) defined in the markdown spec:

- **Hard Gate integration:** Hook your PR creation step. When the runner encounters `Hard Gate`, it halts the pipeline, posts a Slack message or GitHub review request, and waits for a webhook sign-off.
- **Soft Gate integration:** Set a timer (e.g. `DurationSeconds = 300`). Send a notification. If the timer fires without an alert cancellation, proceed to the next step.
