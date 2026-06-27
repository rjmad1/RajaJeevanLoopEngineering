# Dependency Graph

This document details the dependencies between different loops and components in the Loop Engineering Framework.

## 1. Loop Specification Chains

Below is the execution flow and dependency chain of the core loops:

```mermaid
graph TD
    LOOP001["LOOP-001 (Architecture Discovery)"] --> LOOP002["LOOP-002 (Context Assembly)"]
    LOOP001 --> LOOP003["LOOP-003 (Task Discovery)"]
    LOOP002 --> LOOP003
    LOOP002 --> LOOP004["LOOP-004 (Planning)"]
    LOOP003 --> LOOP004
    LOOP004 --> LOOP005["LOOP-005 (Implementation)"]
    LOOP005 --> LOOP006["LOOP-006 (Verification)"]
    LOOP006 --> LOOP007["LOOP-007 (Reflection)"]
    
    %% Engineering Loops
    LOOP002 --> LOOP101["LOOP-101 (Bug Fixing)"]
    LOOP004 --> LOOP101
    LOOP006 --> LOOP101
    
    LOOP002 --> LOOP102["LOOP-102 (Refactoring)"]
    LOOP004 --> LOOP102
    LOOP006 --> LOOP102
```

## 2. Decoupled Java Module Dependency Graph

The harvested code structure has zero circular dependencies and is isolated from the `Conductor` application core:

```mermaid
graph LR
    ExecutionContext["ExecutionContext"]
    RetryPolicy["RetryPolicy"]
    RateLimitPolicy["RateLimitPolicy"]
    CircuitBreaker["CircuitBreaker"]
    SimpleCircuitBreaker["SimpleCircuitBreaker"] --> CircuitBreaker
    
    Condition["Condition"] --> Operator["Operator"]
    ConditionEvaluator["ConditionEvaluator"] --> Condition
    ConditionEvaluator --> ExecutionContext
```
