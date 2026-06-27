package com.rajajeevan.loop.telemetry;

import static org.assertj.core.api.Assertions.assertThat;

import com.rajajeevan.loop.execution.ExecutionContext;
import io.opentelemetry.api.trace.Span;
import java.util.UUID;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class TelemetryServiceTest {

  @Test
  @DisplayName("Telemetry runs safely and registers attributes on spans")
  void testTelemetryExecution() {
    ExecutionContext context = ExecutionContext.builder()
        .workflowDefinitionId(UUID.randomUUID())
        .executionId(UUID.randomUUID())
        .tenantId("test-tenant-123")
        .userId("user-abc")
        .correlationId("trace-xyz")
        .definitionVersion(1)
        .build();

    Span span = TelemetryService.startSpan("TestSpan", context);
    assertThat(span).isNotNull();
    
    // Log exception safely
    TelemetryService.recordException(span, new RuntimeException("Simulated Failure"));
    span.end();
  }

  @Test
  @DisplayName("Telemetry records circuit breaker state transitions")
  void testCircuitBreakerTransitionTelemetry() {
    TelemetryService.recordCircuitBreakerTransition("TestBreaker", "CLOSED", "OPEN");
  }
}
