package com.rajajeevan.loop.telemetry;

import com.rajajeevan.loop.execution.ExecutionContext;
import io.opentelemetry.api.GlobalOpenTelemetry;
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.api.trace.StatusCode;

/**
 * Service providing OpenTelemetry instrumentation for AI Loop execution.
 * Creates trace spans, tracks parent/child contexts, and records telemetry attributes.
 */
public class TelemetryService {

  private static final String INSTRUMENTATION_NAME = "com.rajajeevan.loop.telemetry";
  private static final Tracer tracer = GlobalOpenTelemetry.getTracer(INSTRUMENTATION_NAME);

  /**
   * Starts a tracing span for a loop step.
   *
   * @param name Name of the loop phase or step
   * @param context Execution context for trace attributes
   * @return The started Span
   */
  public static Span startSpan(String name, ExecutionContext context) {
    Span span = tracer.spanBuilder(name).startSpan();
    
    if (context != null) {
      if (context.getWorkflowDefinitionId() != null) {
        span.setAttribute("loop.workflow_definition_id", context.getWorkflowDefinitionId().toString());
      }
      if (context.getExecutionId() != null) {
        span.setAttribute("loop.execution_id", context.getExecutionId().toString());
      }
      if (context.getTenantId() != null) {
        span.setAttribute("loop.tenant_id", context.getTenantId());
      }
      if (context.getUserId() != null) {
        span.setAttribute("loop.user_id", context.getUserId());
      }
      if (context.getCorrelationId() != null) {
        span.setAttribute("loop.correlation_id", context.getCorrelationId());
      }
      span.setAttribute("loop.definition_version", context.getDefinitionVersion());
    }
    
    return span;
  }

  /**
   * Records a circuit breaker state transition.
   *
   * @param circuitBreakerName Name of the breaker
   * @param fromState Originating state
   * @param toState Targeted state
   */
  public static void recordCircuitBreakerTransition(String circuitBreakerName, String fromState, String toState) {
    Span span = tracer.spanBuilder("circuit_breaker_transition")
        .setAttribute("cb.name", circuitBreakerName)
        .setAttribute("cb.from_state", fromState)
        .setAttribute("cb.to_state", toState)
        .startSpan();
    
    span.addEvent("State changed from " + fromState + " to " + toState);
    span.end();
  }

  /**
   * Records an execution failure onto the current span.
   *
   * @param span Current span
   * @param throwable Exception that caused the failure
   */
  public static void recordException(Span span, Throwable throwable) {
    if (span != null && throwable != null) {
      span.setStatus(StatusCode.ERROR, throwable.getMessage());
      span.recordException(throwable);
    }
  }
}
