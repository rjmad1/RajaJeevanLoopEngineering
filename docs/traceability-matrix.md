# Traceability Matrix

This matrix maps every generalized/extracted file in `RajaJeevanLoopEngineering` back to its original file and path in the `RajaJeevanLoopEngineering` repository.

| Library Path | Original Path | Original Version | Notes |
| :--- | :--- | :--- | :--- |
| `shared/` | `docs/loops/shared/` | 1.0 | Standard rules and specifications. |
| `loops/core/` | `docs/loops/core/` | 1.0 | Core loop specs. |
| `loops/engineering/` | `docs/loops/engineering/` | 1.0 | Coding and debug loop specs. |
| `loops/platform/` | `docs/loops/platform/` | 1.0 | Generalized platform validation specs. |
| `loops/governance/` | `docs/loops/governance/` | 1.0 | Governance loops. |
| `templates/` | `docs/loops/templates/` | 1.0 | Reusable loop templates. |
| `examples/` | `docs/loops/examples/` | 1.0 | Worked execution logs. |
| `code/src/main/java/com/rajajeevan/loop/rules/Condition.java` | `shared/rules/src/main/java/com/conductor/shared/rules/Condition.java` | 1.0.0 | Remapped package. |
| `code/src/main/java/com/rajajeevan/loop/rules/Operator.java` | `shared/rules/src/main/java/com/conductor/shared/rules/Operator.java` | 1.0.0 | Remapped package. |
| `code/src/main/java/com/rajajeevan/loop/rules/ConditionEvaluator.java` | `shared/rules/src/main/java/com/conductor/shared/rules/ConditionEvaluator.java` | 1.0.0 | Remapped package. |
| `code/src/main/java/com/rajajeevan/loop/execution/ExecutionContext.java` | `shared/execution/src/main/java/com/conductor/shared/execution/ExecutionContext.java` | 1.0.0 | Decoupled imports. |
| `code/src/main/java/com/rajajeevan/loop/execution/RetryPolicy.java` | `shared/execution/src/main/java/com/conductor/shared/execution/RetryPolicy.java` | 1.0.0 | Decoupled imports. |
| `code/src/main/java/com/rajajeevan/loop/execution/provider/CircuitBreaker.java` | `shared/execution/src/main/java/com/conductor/shared/execution/provider/CircuitBreaker.java` | 1.0.0 | Remapped package. |
| `code/src/main/java/com/rajajeevan/loop/execution/provider/SimpleCircuitBreaker.java` | `shared/execution/src/main/java/com/conductor/shared/execution/provider/SimpleCircuitBreaker.java` | 1.0.0 | Remapped package. |
| `code/src/main/java/com/rajajeevan/loop/execution/provider/RateLimitPolicy.java` | `shared/execution/src/main/java/com/conductor/shared/execution/provider/RateLimitPolicy.java` | 1.0.0 | Remapped package. |
| `code/src/test/java/com/rajajeevan/loop/rules/ConditionEvaluatorTest.java` | `shared/rules/src/test/java/com/conductor/shared/rules/ConditionEvaluatorTest.java` | 1.0.0 | Remapped package. |
| `code/src/test/java/com/rajajeevan/loop/execution/RetryPolicyTest.java` | `shared/execution/src/test/java/com/conductor/shared/execution/RetryPolicyTest.java` | 1.0.0 | Remapped package. |
