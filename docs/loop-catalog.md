# Loop Catalog

This catalog indexes all generalized loops available in the General Purpose Loop Engineering Library.

| Loop ID | Name | Category | Complexity | Dependencies | Primary Use Cases |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **LOOP-001** | Architecture Discovery | Core | Low | None | Mapping a repository's folder structures and interfaces. |
| **LOOP-002** | Context Assembly | Core | Low | LOOP-001 | Gathering specific target source files and dependencies. |
| **LOOP-003** | Task Discovery | Core | Medium | LOOP-001, LOOP-002 | Decomposing raw tasks into detailed checklist items. |
| **LOOP-004** | Planning | Core | Medium | LOOP-002, LOOP-003 | Generating step-by-step implementation plans. |
| **LOOP-005** | Implementation | Core | High | LOOP-004 | Making sandbox-bounded edits in the codebase. |
| **LOOP-006** | Verification | Core | Low | LOOP-005 | Running test suites, checkstyle, and code scanners. |
| **LOOP-007** | Reflection | Core | Low | LOOP-006 | Conducting post-run assessments and memory updates. |
| **LOOP-101** | Bug Fixing | Engineering | High | LOOP-002, LOOP-004, LOOP-006 | Troubleshooting, replicating, and patching codebase bugs. |
| **LOOP-102** | Refactoring | Engineering | Medium | LOOP-002, LOOP-004, LOOP-006 | Structural cleanups and technical debt reduction. |
| **LOOP-103** | Test Generation | Engineering | Medium | LOOP-001, LOOP-002, LOOP-005 | Authoring unit and integration tests. |
| **LOOP-104** | Documentation | Engineering | Low | LOOP-001, LOOP-002 | Generating READMEs, wikis, and reference guides. |
| **LOOP-105** | Code Review | Engineering | Medium | LOOP-001, LOOP-002 | Automated auditing of pull requests. |
| **LOOP-106** | Customer Journey Analytics | Engineering | Medium | LOOP-002, LOOP-006 | Mapping runtime errors to conversion funnel drop-offs. |
| **LOOP-110** | Legacy Strangler | Engineering | High | LOOP-002, LOOP-004, LOOP-006 | Encapsulating monolithic features into modern microservices. |
| **LOOP-111** | Technical Debt Remediation | Engineering | Medium | LOOP-002, LOOP-004, LOOP-006 | Quantifying complexity trends and scheduling refactoring. |
| **LOOP-112** | Component Deprecation Lifecycle | Engineering | Medium | LOOP-002, LOOP-004, LOOP-006 | Tracks usage of older internal software libraries and schedules refactoring. |
| **LOOP-113** | Dead Code Elimination | Engineering | High | LOOP-002, LOOP-004, LOOP-006 | Detects unused modules in production and generates PRs to prune them. |
| **LOOP-130** | Localization and Internationalization Audit | Engineering | Medium | LOOP-002, LOOP-004, LOOP-006 | Scans frontend files for hardcoded strings and extracts to translation files. |
| **LOOP-150** | Dependency Patching | Engineering | Medium | LOOP-002, LOOP-004, LOOP-006 | Scanning open-source packages and applying upgrades. |
| **LOOP-160** | Database Deadlock Resolution | Engineering | High | LOOP-002, LOOP-004, LOOP-006 | Captures deadlock bottlenecks and recommends query restructuring. |
| **LOOP-161** | Memory Leak Detection | Engineering | High | LOOP-002, LOOP-004, LOOP-006 | Subjects staging instances to synthetic traffic spikes to flag memory leaks. |
| **LOOP-170** | Zero-Trust Token Rotation | Engineering | High | LOOP-002, LOOP-004, LOOP-006 | Automated key and auth token rotation. |
| **LOOP-171** | Secrets Lifecycle Enforcement | Engineering | High | LOOP-002, LOOP-004, LOOP-006 | Audits operational credentials age and orchestrates zero-downtime rolling updates. |
| **LOOP-180** | Environment Drift Audit | Engineering | Medium | LOOP-002, LOOP-004, LOOP-006 | Detecting and reconciling IaC mismatches. |
| **LOOP-181** | Container Layer Optimization | Engineering | Medium | LOOP-002, LOOP-004, LOOP-006 | Scans container images and strips redundant packages to minimize size/attack surface. |
| **LOOP-201** | Workflow Validation | Platform | Medium | LOOP-006 | Validating pipeline flow and state boundaries. |
| **LOOP-202** | Integration Validation | Platform | Medium | LOOP-006 | Validating third-party API keys and rate limits. |
| **LOOP-203** | Event Validation | Platform | Medium | LOOP-006 | Auditing event schema and publisher topics. |
| **LOOP-204** | API Contract Validation | Platform | Medium | LOOP-006 | Ensuring REST and gRPC API contract compliance. |
| **LOOP-205** | Multi-Tenant Isolation Audit | Platform | High | LOOP-006 | Synthetic cross-tenant query injection to prevent data bleed. |
| **LOOP-206** | Observability Validation | Platform | Medium | LOOP-006 | Auditing metrics, logging, and tracing coverage. |
| **LOOP-207** | Security Validation | Platform | Medium | LOOP-006 | Running static application security tests (SAST). |
| **LOOP-208** | Data Migration | Platform | High | LOOP-006 | Validating data sync integrity during legacy-to-cloud transition. |
| **LOOP-209** | Partner API Degradation | Platform | Medium | LOOP-006 | Simulating external endpoint failures and validating circuit breakers. |
| **LOOP-210** | API Shadow IT Discovery | Platform | Medium | LOOP-006 | Scanning traffic to automatically inventory undocumented endpoints. |
| **LOOP-211** | FinOps Cloud Bursting | Platform | High | LOOP-006 | Dynamic migration of workloads to lower-cost regions. |
| **LOOP-212** | Chaos Engineering Resilience | Platform | High | LOOP-006 | Verifying architectural self-healing through failure injection. |
| **LOOP-213** | Multi-Region State Sync | Platform | High | LOOP-006 | Monitors replication lag and adjusts query routing to prevent read inconsistencies. |
| **LOOP-214** | Resource Quota Guardrail | Platform | High | LOOP-006 | Triggers microservice containment/scaling alerts if tenant resource usage drifts. |
| **LOOP-215** | Secret Leakage Prevention | Platform | High | LOOP-006 | Scans code commits, containers, and logs in real-time to block exposed secrets. |
| **LOOP-216** | Database Index Optimization | Platform | High | LOOP-006 | Analyzes query execution plans to automatically apply missing indexes and drop redundant ones. |
| **LOOP-217** | System Event Idempotency | Platform | Medium | LOOP-006 | Intentionally duplicates event payloads to verify once-and-only-once state changes. |
| **LOOP-218** | Backward Compatibility Verification | Platform | Medium | LOOP-006 | Executes consumer-driven contract tests to verify data schema changes do not break partners. |
| **LOOP-219** | Load Balancing Anomaly Mitigation | Platform | High | LOOP-006 | Monitors traffic distribution across regions and updates ingress routing dynamically on latency spikes. |
| **LOOP-220** | API Rate Limiting Guardrail | Platform | Medium | LOOP-006 | Simulates high-velocity traffic to verify that throttling triggers correctly. |
| **LOOP-221** | Accessibility Compliance Guardrail | Platform | Medium | LOOP-006 | Validates front-end builds against WCAG standards and blocks non-compliant builds. |
| **LOOP-222** | Telemetry Anomaly Detection | Platform | Medium | LOOP-006 | Correlates application logs with API metrics to flag hidden feature failures. |
| **LOOP-223** | Multi-Cloud Disaster Recovery | Platform | High | LOOP-006 | Regularly runs isolated failover simulations to verify disaster recovery objectives. |
| **LOOP-224** | Edge Cache Invalidation | Platform | Medium | LOOP-006 | Instantly pushes targeted cache purge commands to edge networks on content updates. |
| **LOOP-225** | Cross-Site Scripting Guardrail | Platform | Medium | LOOP-006 | Injects synthetic malicious scripts into open inputs to verify sanitization layers block execution. |
| **LOOP-226** | Tenant Onboarding Validation | Platform | Medium | LOOP-006 | Runs configuration scripts and smoke tests to verify dedicated resource isolation. |
| **LOOP-227** | Third-Party Webhook Reliability | Platform | Medium | LOOP-006 | Tracks outbound webhook delivery rates, implementing backoff/dead-letter queues on failure. |
| **LOOP-228** | Log Aggregation Sanity | Platform | Medium | LOOP-006 | Emits test events to verify centralized logging agents capture and index telemetry. |
| **LOOP-301** | ADR Generation | Governance | Low | LOOP-004 | Generating Architectural Decision Records. |
| **LOOP-302** | Doc Governance | Governance | Low | LOOP-007 | Auditing documents for stale links and formats. |
| **LOOP-303** | Compliance | Governance | High | LOOP-006 | General project regulatory and compliance reviews. |
| **LOOP-304** | Release Readiness | Governance | Medium | LOOP-006, LOOP-007 | Performing checklist checks before main merges. |
| **LOOP-305** | Telemetry Compliance | Governance | Medium | LOOP-006 | Verifying that analytics match tracking specifications. |
| **LOOP-306** | SaaS Cost Optimization | Governance | Medium | LOOP-007 | Real-time user license analysis and account deprovisioning. |
| **LOOP-307** | Regulatory Compliance Drift | Governance | High | LOOP-006 | Evaluating code changes against changing legal frameworks. |
| **LOOP-308** | Contract-to-Code Enforcement | Governance | High | LOOP-006 | Verifies autogenerated API code matches service level agreements and privacy clauses. |
| **LOOP-309** | License Compliance Audit | Governance | Medium | LOOP-006 | Scans third-party code packages to block restrictive or unauthorized licenses in build pipeline. |
| **LOOP-310** | Infrastructure Cost Attribution | Governance | Medium | LOOP-007 | Maps cloud resource consumption to specific components, generating efficiency dashboards. |
| **LOOP-311** | Feature Access Entitlement | Governance | Medium | LOOP-006 | Audits subscription levels against feature flag configs to block access to unpurchased tiers. |
| **LOOP-312** | Data Privacy Anonymization | Governance | Medium | LOOP-006 | Scans and scrubs personally identifiable details from database staging exports. |
| **LOOP-401** | Release Checklist | Release | Medium | LOOP-304 | Step-by-step validation of release parameters. |
| **LOOP-402** | Deployment Validation | Release | High | LOOP-401 | Smoke testing and verifying active deployments. |
| **LOOP-403** | Post-Release Verification | Release | Medium | LOOP-402 | Long-term monitoring and verification post-release. |
| **LOOP-404** | Feature Flag Lifecycle | Release | High | LOOP-006, LOOP-007 | Automated rollout, rollback, and cleanup of toggles. |
| **LOOP-405** | Experimentation Guardrail | Release | High | LOOP-006 | Tracking live A/B test metrics and terminating failing variants. |
| **LOOP-406** | Edge Deployment Rollback | Release | High | LOOP-006 | Monitoring containerized edge apps and executing local rollbacks. |
| **LOOP-407** | Synthetic User Verification | Release | High | LOOP-006 | Runs continuous simulated E2E workflows on production to detect silent UI degradations. |
| **LOOP-408** | Delivery & Change Steward | Release | High | LOOP-005, LOOP-006, LOOP-504 | Delivery, release coordination, and Git change governance. |
| **LOOP-502** | Product Intelligence Architect | Strategy | High | LOOP-501 | Continuously build and maintain a complete understanding of a product. |
| **LOOP-504** | Knowledge Integrity Steward | Strategy | High | LOOP-502 | Synchronize canonical memory in the knowledge directory. |
