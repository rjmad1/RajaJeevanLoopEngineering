# Enterprise Governance Recipes

This guide provides checklists and structures for compliance audits, governance reviews, and security guidelines.

---

## 1. Compliance Audit Checklist

Run this audit loop to verify codebase compliance with security and privacy regulations (like GDPR, HIPAA, or SOC2).

### Compliance Checklist
- [ ] No PII (Personally Identifiable Information) is logged in plain text.
- [ ] All database columns containing sensitive information are encrypted (e.g. using PiiEncryptedConverter).
- [ ] Authentication tokens and passwords are not committed in code or settings files (secrets management).
- [ ] Tenant context is explicitly validated on every incoming request.
- [ ] Access logs are produced for all authorization write events.
- [ ] Dependency licenses verified; no prohibited licenses (like GPL/AGPL in proprietary scopes) are imported.

---

## 2. Architecture Review Board (ARB) Submission Loop

Prepare systematic submissions for ARB or Architecture Review approval.

### ARB Submission Template Prompt
```markdown
System: You are an enterprise architect. Generate an ARB review document for the proposed system integration.

Integration Scope:
[Insert Scope Description]

Required Sections:
- **1. Context & Business Value:** Problem solved and business outcome.
- **2. Technology Selection:** Chosen components and licenses.
- **3. Trust Boundaries:** Network isolation, encryption in transit/rest, authentication model.
- **4. Operational Compliance:** Logging hooks, metrics dashboard, backup and recovery plans.
- **5. SLA & Reliability:** High availability strategy, failover, disaster recovery RTO/RPO.
```

---

## 3. Security Risk Register Loop

Track and mitigate architecture security risks.

### Security Scan and Risk Mapping
```markdown
System: You are a security engineer. Identify threat vectors in the proposed integration design.

Proposed Design:
[Insert Design Detail]

Task:
List all risks mapping to STRIDE categories (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege). For each risk, specify:
1. Likelihood (High/Med/Low).
2. Impact (High/Med/Low).
3. Mitigation Control (e.g., HMAC Validation, Tenant Context Filter).
4. Verification step.
```
