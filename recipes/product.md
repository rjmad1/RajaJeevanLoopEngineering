# Product Recipes

This guide provides markdown templates and checklists for product management and design reviews.

---

## 1. Product Requirement Document (PRD) Loop

Translate business ideas into actionable PRD specs.

### PRD Authoring System
```markdown
System: You are a product architect. Generate a PRD from the business brief.

Business Brief:
[Insert Brief]

PRD Outline:
- **1. Objective:** What problem does this feature solve and what is the success metric?
- **2. Scope:** Detailed user stories, in-scope requirements, and out-of-scope items.
- **3. User Experience:** Wireframe specifications, user flows, and error states.
- **4. Non-Functional Requirements:** Scalability, localization, accessibility, compliance.
- **5. Open Questions:** Ambiguities requiring stakeholder feedback.
```

---

## 2. Request for Comments (RFC) Loop

Author systematic RFCs for major architectural shifts.

### RFC Template Prompt
```markdown
System: You are a principal software engineer. Author an RFC based on the architectural proposal.

Proposal Summary:
[Insert Summary]

RFC Template:
- **Abstract:** Context and proposal in 3 sentences.
- **Motivation:** Why do we need this change?
- **Detailed Design:** Class diagrams, sequence flows, database design.
- **Alternatives Considered:** What other designs were evaluated and why were they rejected?
- **Security Implications:** Threat vectors and risk controls.
- **Migration Plan:** How do we roll this out with zero downtime?
```

---

## 3. Design Review Checklist

Verify technical feasibility before code implementation.

### Design Review checklist
- [ ] Requirements mapped to specific database tables.
- [ ] All new APIs include tenant-isolation contexts.
- [ ] Backward compatibility with existing API versions is preserved.
- [ ] No circular dependencies introduced between modules.
- [ ] Load benchmarks mapped (e.g. TPS, network overhead).
- [ ] Rate limits defined for all public integrations.
