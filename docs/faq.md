# Frequently Asked Questions (FAQ)

Here are answers to the most common questions about the Loop Engineering Framework.

---

## 1. Can loops be executed without Java?
Yes! The loop specifications, standards, and templates are written in standard Markdown and are completely framework-agnostic. You can run them using Python scripts, TypeScript agent systems, or simple bash pipelines. The Java library in `code/` is a set of helper utilities for Java-based environments but is not a prerequisite.

## 2. What is the difference between a Hard Gate and a Soft Gate?
- A **Hard Gate** halts the run completely and requires explicit human sign-off (e.g. approving a pull request or hitting a button).
- A **Soft Gate** registers a notification and waits for a timeout (e.g. 5 minutes). If no human operator cancels the run during the timeout, it resumes automatically.

## 3. How do I add new loops to my project?
Assign a sequence number based on category ranges (e.g. `LOOP-501`), copy the template in `templates/LOOP-TEMPLATE.md`, fill in the required sections, and submit it for peer review. Once approved, mark it as `Active`.

## 4. Why does the framework require Reflection logs?
Reflection logs capture errors, root causes, duration, and metrics. This telemetry is critical for audit compliance, identifying optimization gaps, and updating the agent's long-term memory.
