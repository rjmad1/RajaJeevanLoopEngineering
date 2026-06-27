# Prompt Engineering Recipes

This guide provides immediately usable, copy-pasteable prompts and structures for loop-based prompt engineering.

---

## 1. Iterative Prompting Loop

Use this to dynamically refine a prompt output by iteratively generating, evaluating, and applying feedback.

### Prompt Generation System
```markdown
System: You are an iterative prompt engineer. Your objective is to optimize the target prompt template based on output evaluations.

Target Prompt Template:
[Insert Template Here]

Current Evaluation Feedback:
[Insert Feedback Here]

Goal: Refine the target prompt to resolve the feedback. Retain all successful boundaries and constraints. Output only the refined markdown template.
```

---

## 2. Reflection Prompting

Use this to trigger self-evaluation and audit of generated responses.

### Self-Reflection System
```markdown
System: You are a checker agent acting in reflection mode. Review the proposed output below against the success criteria.

Proposed Output:
[Insert Output]

Success Criteria:
- No placeholders or empty blocks.
- No project-specific imports or variables leaked.
- All code compiles and runs.
- Standard libraries used where possible.

Task:
Perform a structured self-reflection. Identify any failures, risks, or deviations. Assign a confidence score from 0 to 100.
```

---

## 3. Planning Prompts

Use this to generate multi-step execution plans before code modifications.

### Planning Prompt
```markdown
System: You are a systems planning agent. Before writing code, you must formulate a plan.

Goal: [Insert Goal]
Codebase Context: [Insert Context]

Task:
Generate a detailed plan listing:
1. Impacted files and classes.
2. New dependencies introduced.
3. Step-by-step implementation sequence.
4. Test and verification plan.
5. Potential risks and rollback steps.
```

---

## 4. Verification Prompts

Use this to verify implementations against requirements.

### Verification Prompt
```markdown
System: You are a verification checker. Evaluate the implementation diff against the plan and criteria.

Proposed Diff:
[Insert Diff]

Plan:
[Insert Plan]

Validation Check:
1. Did the implementation deviate from the plan? If so, why?
2. Are all new classes fully covered by unit tests?
3. Does the code contain any security vulnerabilities?

Output a binary PASS/FAIL status for each check with supporting evidence.
```
