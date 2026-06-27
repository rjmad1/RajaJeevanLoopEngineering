package com.rajajeevan.loop.execution;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class GitRollbackServiceTest {

  @Test
  @DisplayName("Rollback fails gracefully on non-existent directories")
  void testInvalidDirectoryGracefulFailure() {
    GitRollbackService service = GitRollbackService.builder()
        .repoPath("./non_existent_folder_xyz_123")
        .useStash(true)
        .build();

    boolean result = service.rollback();
    assertThat(result).isFalse();
  }

  @Test
  @DisplayName("Service builders map default configuration correctly")
  void testServiceBuilderDefaults() {
    GitRollbackService service = GitRollbackService.builder().build();
    assertThat(service.getRepoPath()).isEqualTo(".");
    assertThat(service.isUseStash()).isTrue();
    assertThat(service.isCleanUntracked()).isTrue();
  }
}
