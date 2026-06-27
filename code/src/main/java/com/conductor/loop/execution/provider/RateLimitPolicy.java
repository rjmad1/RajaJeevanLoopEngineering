package com.conductor.loop.execution.provider;

import lombok.Builder;
import lombok.Getter;

/** Configuration policy for client-side rate limiting on loop execution requests. */
@Getter
@Builder
public class RateLimitPolicy {
  @Builder.Default private final double requestsPerSecond = 10.0;
  @Builder.Default private final int burstLimit = 20;
  @Builder.Default private final boolean enabled = false;
}
