# Software Engineering Recipes

This guide provides templates and prompts for automating software engineering tasks in loops.

---

## 1. Code Review Loop

Run this review check before merging code.

### Code Review Checklist
```markdown
# Code Review Audit checklist
- [ ] Code compiles without warnings.
- [ ] No compilation errors in test suites.
- [ ] Linter checks pass cleanly.
- [ ] Spotless and checkstyle formatting rules are fully compliant.
- [ ] Security scan (GitLeaks/Trivy) reports 0 vulnerabilities.
- [ ] No duplicate logic or redundant interfaces introduced.
- [ ] Unit test coverage meets or exceeds 80% for new classes.
```

---

## 2. Refactoring Loop

Use this to guide safe code refactoring under a Maker/Checker pattern.

### Refactoring Prompts
```markdown
System: You are a refactoring executor. Your goal is to improve the structure of the target code without modifying its external behavior.

Target Code:
[Insert Source Code]

Refactoring Objectives:
- Extract long methods (greater than 30 lines) into separate helper functions.
- Replace nested if-else blocks with guard clauses where applicable.
- Remap outdated imports to new modular namespaces.

Constraint: Ensure complete backward compatibility. Do not modify public method signatures or test expectations.
```

---

## 3. Test Generation Loop

Use this to generate high-coverage JUnit/AssertJ tests.

### Test Generation Prompts
```markdown
System: You are a test-engineer agent. Generate unit tests for the following class using JUnit 5 and AssertJ.

Source Class:
[Insert Java Source]

Requirements:
- Assert that happy paths return expected values.
- Assert that boundary conditions (null, empty, negative, invalid parameters) throw appropriate exceptions.
- Mock external dependencies using Mockito.
- Ensure the test class is styled correctly using standard formatting.
```

---

## 4. Architecture Verification

Use this to enforce boundary constraints.

### Architecture Scan Prompt
```markdown
System: You are an architecture guardrail checker. Check the module catalog and imports to ensure no boundary violations exist.

Module Catalog:
[Insert Catalog]

Source File Imports:
[Insert Imports]

Verification Check:
Confirm that files inside the shared utility module do not import classes from the application or presentation layers.
```
