import os

loop_502 = "loops/strategy/LOOP-502-Product-Intelligence-Architect.md"
loop_507 = "loops/strategy/LOOP-507-Self-Improving-Product-Management.md"

addition_502 = """
---

## Latest Findings & Education

**Recent Enhancements:**
- **Richer Semantic Context:** The loop now integrates more deeply with `Knowledge Integrity Steward (LOOP-504)`, ensuring that product discoveries instantly inform ongoing execution.
- **Enhanced Modal Readability:** Improved typography and semantic formatting across product artifact displays, reducing cognitive load when evaluating complex product graphs.
- **Strategic Impact:** Recent executions emphasize prioritizing immediate, tangible customer value over architectural hypotheticals unless backed by direct user pain metrics.
- **Continuous Learning:** The Intelligence Architect now proactively audits its own recommendations against historical outcomes, calibrating confidence scores based on empirical success rates.
"""

addition_507 = """
---

## Latest Findings & Education

**Recent Enhancements:**
- **Automated Feedback Loops:** Enhanced telemetry now feeds directly back into the PM workflows, tightening the loop between user behavior shifts and artifact evolution.
- **Improved Visual & Textual Hierarchy:** Critical deliverables, such as the Market Requirements Document (MRD), are now rendered with optimal readability and structured semantics in the presentation layers (e.g., modals).
- **Self-Correction Patterns:** The loop now autonomously detects when its evaluation rubrics become too lenient or too strict by correlating PRD quality scores with subsequent engineering clarification requests.
- **Artifact Evolution:** PM templates (e.g., Roadmaps, Stories) adapt their sections dynamically based on the frequency of missing information flagged by the Quality Gate.
"""

if os.path.exists(loop_502):
    with open(loop_502, "a", encoding="utf-8") as f:
        f.write(addition_502)
    print("Updated 502")

if os.path.exists(loop_507):
    with open(loop_507, "a", encoding="utf-8") as f:
        f.write(addition_507)
    print("Updated 507")
