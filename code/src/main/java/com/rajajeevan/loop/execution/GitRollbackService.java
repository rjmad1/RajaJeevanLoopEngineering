package com.rajajeevan.loop.execution;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import lombok.Builder;
import lombok.Getter;

/**
 * Service to execute automated Git state rollbacks. Triggered automatically on circuit breaker
 * trips to revert unstable LLM code generations back to a known baseline.
 */
@Getter
@Builder
public class GitRollbackService {

  @Builder.Default private final String repoPath = ".";
  @Builder.Default private final boolean useStash = true;
  @Builder.Default private final boolean cleanUntracked = true;

  /**
   * Reverts current codebase changes using Git.
   *
   * @return true if Git rollback succeeded, false otherwise
   */
  public boolean rollback() {
    File repoDir = new File(repoPath);
    if (!repoDir.exists() || !repoDir.isDirectory()) {
      System.err.println("GitRollbackService Error: Path does not exist or is not a directory: " + repoPath);
      return false;
    }

    try {
      if (useStash) {
        // Run git stash -u to save changes including untracked files
        System.out.println("GitRollbackService: Running git stash -u in " + repoPath);
        executeCommand(List.of("git", "stash", "-u", "-m", "Auto-rollback triggered by circuit breaker"), repoDir);
      } else {
        // Run git reset --hard HEAD
        System.out.println("GitRollbackService: Running git reset --hard HEAD in " + repoPath);
        executeCommand(List.of("git", "reset", "--hard", "HEAD"), repoDir);
      }

      if (cleanUntracked && !useStash) {
        // Run git clean -fd to purge untracked files
        System.out.println("GitRollbackService: Running git clean -fd in " + repoPath);
        executeCommand(List.of("git", "clean", "-fd"), repoDir);
      }

      return true;
    } catch (Exception e) {
      System.err.println("GitRollbackService Error: Git rollback command failed: " + e.getMessage());
      e.printStackTrace();
      return false;
    }
  }

  private void executeCommand(List<String> command, File workingDir) throws Exception {
    ProcessBuilder builder = new ProcessBuilder(command);
    builder.directory(workingDir);
    builder.redirectErrorStream(true);
    
    Process process = builder.start();
    try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
      String line;
      while ((line = reader.readLine()) != null) {
        System.out.println("Git: " + line);
      }
    }
    
    int exitCode = process.waitFor();
    if (exitCode != 0) {
      throw new RuntimeException("Process exited with code " + exitCode);
    }
  }
}
