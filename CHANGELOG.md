# Changelog

All notable changes to the General Purpose Loop Engineering Library will be documented in this file.

## [Unreleased]

### Added
- **UI Styling:** Enhanced modal readability and typography (`.modal-body h1`, `.info-btn`) in `loops-quick-reckoner.html` and `remote-loops-quick-reckoner.html`.
- **Loop Strategy Insights:** Appended recent semantic context, telemetry insights, and self-correction patterns to `LOOP-502` and `LOOP-507`.

## [1.0.0] — 2026-06-27

### Added
- **Framework Standards:** Extracted canonical loop standard documents from RajaJeevanLoopEngineering's internal specs to `shared/`.
- **General Purpose Loops:** Extracted and generalized Core, Engineering, Platform, and Governance loops.
- **Remapped Rules Engine:** Extracted `Condition`, `Operator`, and `ConditionEvaluator` Java rules into independent `com.rajajeevan.loop.rules` namespace.
- **Decoupled Execution Helpers:** Extracted thread-safe `SimpleCircuitBreaker`, `RetryPolicy`, and `ExecutionContext` into `com.rajajeevan.loop.execution` with zero external dependencies.
- **Recipes & Snippets:** Created copy-paste guides for autonomous AI agents, prompt engineering, product specs, and enterprise compliance.
- **Standalone Build:** Set up isolated Gradle build configs with JUnit 5 test setups. All compiled checks and static assertions successfully validated.
