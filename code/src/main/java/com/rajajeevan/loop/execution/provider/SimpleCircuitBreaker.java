package com.rajajeevan.loop.execution.provider;

import com.rajajeevan.loop.execution.GitRollbackService;
import com.rajajeevan.loop.telemetry.TelemetryService;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.atomic.AtomicReference;

/**
 * Thread-safe default implementation of a Circuit Breaker. Transitions CLOSED -> OPEN on
 * consecutive failures, resets to HALF_OPEN after a timeout. Integrates automated git rollbacks
 * and OpenTelemetry tracing.
 */
public class SimpleCircuitBreaker implements CircuitBreaker {

  public enum State {
    CLOSED,
    OPEN,
    HALF_OPEN
  }

  private final int failureThreshold;
  private final long resetTimeoutMs;
  private final GitRollbackService rollbackService;

  private final AtomicReference<State> state = new AtomicReference<>(State.CLOSED);
  private final AtomicInteger consecutiveFailures = new AtomicInteger(0);
  private final AtomicLong lastStateChangeTime = new AtomicLong(System.currentTimeMillis());

  public SimpleCircuitBreaker(int failureThreshold, long resetTimeoutMs) {
    this(failureThreshold, resetTimeoutMs, null);
  }

  public SimpleCircuitBreaker(int failureThreshold, long resetTimeoutMs, GitRollbackService rollbackService) {
    this.failureThreshold = failureThreshold;
    this.resetTimeoutMs = resetTimeoutMs;
    this.rollbackService = rollbackService;
  }

  @Override
  public boolean allowRequest() {
    State currentState = state.get();
    if (currentState == State.OPEN) {
      long elapsed = System.currentTimeMillis() - lastStateChangeTime.get();
      if (elapsed >= resetTimeoutMs) {
        if (state.compareAndSet(State.OPEN, State.HALF_OPEN)) {
          TelemetryService.recordCircuitBreakerTransition("SimpleCircuitBreaker", State.OPEN.name(), State.HALF_OPEN.name());
          lastStateChangeTime.set(System.currentTimeMillis());
          return true;
        }
      }
      return false;
    }
    return true;
  }

  @Override
  public void recordSuccess() {
    consecutiveFailures.set(0);
    State prev = state.getAndSet(State.CLOSED);
    if (prev != State.CLOSED) {
      TelemetryService.recordCircuitBreakerTransition("SimpleCircuitBreaker", prev.name(), State.CLOSED.name());
    }
  }

  @Override
  public void recordFailure(Throwable throwable) {
    consecutiveFailures.incrementAndGet();
    State current = state.get();
    if (current == State.HALF_OPEN || consecutiveFailures.get() >= failureThreshold) {
      boolean transitioned = false;
      if (state.compareAndSet(State.CLOSED, State.OPEN)) {
        TelemetryService.recordCircuitBreakerTransition("SimpleCircuitBreaker", State.CLOSED.name(), State.OPEN.name());
        transitioned = true;
      } else if (state.compareAndSet(State.HALF_OPEN, State.OPEN)) {
        TelemetryService.recordCircuitBreakerTransition("SimpleCircuitBreaker", State.HALF_OPEN.name(), State.OPEN.name());
        transitioned = true;
      }
      if (transitioned) {
        lastStateChangeTime.set(System.currentTimeMillis());
        if (rollbackService != null) {
          System.out.println("SimpleCircuitBreaker: Circuit breaker tripped to OPEN. Initiating state rollback...");
          rollbackService.rollback();
        }
      }
    }
  }

  @Override
  public String getState() {
    return state.get().name();
  }
}
