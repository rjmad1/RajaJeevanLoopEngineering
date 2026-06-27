# =============================================================================
# Agnostic Loop Engine — Multi-Stage Docker Build
# =============================================================================
# Build phase: compile and package the shadow JAR using JDK 21
FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /app

# Copy Gradle wrapper and build files first (layer caching for dependencies)
COPY code/build.gradle code/settings.gradle ./
COPY gradle/ ../gradle/
COPY gradlew gradlew.bat ../

# Copy source code
COPY code/src/ src/

# Build the fat JAR
RUN chmod +x ../gradlew && ../gradlew shadowJar --no-daemon

# =============================================================================
# Runtime phase: minimal JRE image with non-root execution
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app

# Create non-root user for sandboxed execution
RUN addgroup -S loopengine && adduser -S loopengine -G loopengine

COPY --from=builder /app/build/libs/*-all.jar loop-engine.jar

# Drop to non-root user
USER loopengine

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget -qO- http://localhost:8080/health || exit 1

ENTRYPOINT ["java", "-jar", "loop-engine.jar"]
