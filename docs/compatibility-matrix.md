# Compatibility Matrix

This matrix describes the system requirements and compatibility boundaries of the Loop Engineering Framework components.

## 1. Java Code Dependencies

| Framework / Tool | Minimum Version | Supported Versions | Notes |
| :--- | :--- | :--- | :--- |
| **Java SDK** | JDK 21 | JDK 21+ | Compiled under Java 21 toolchain. |
| **Lombok** | 1.18.30 | 1.18.x | Code generation annotations. |
| **JUnit Jupiter** | 5.10.2 | 5.10.x | Running unit test suites. |
| **AssertJ** | 3.25.3 | 3.25.x | Fluent assertions for unit tests. |
| **Gradle** | 8.9 | 8.x+ | Gradle build runner. |

## 2. Loop Documents & Orchestration Compatibility

| Environment | Compatibility | Notes |
| :--- | :--- | :--- |
| **AI Agents** | Fully compatible | Standard Markdown guides can be loaded directly into LLM prompts. |
| **Temporal Workflow** | Fully compatible | Core state machines translate directly into Temporal activity/saga implementations. |
| **GitHub Actions** | Fully compatible | Loop verification steps map to standard CI/CD workflow scripts. |
| **Git Lab Pipelines** | Fully compatible | Can be executed as separate pipeline stages. |
