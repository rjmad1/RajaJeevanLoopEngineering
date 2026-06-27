package com.rajajeevan.loop.prompts;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class PromptAssemblerTest {

  private PromptAssembler assembler;
  private PromptAssembler.PromptTemplateSpec spec;

  @BeforeEach
  void setUp() {
    assembler = new PromptAssembler();
    
    spec = new PromptAssembler.PromptTemplateSpec();
    spec.templateName = "Code Refactoring Spec";
    spec.version = "1.0";
    spec.systemInstructions = "System Instructions: Clean up redundant code.";
    spec.templateText = "Refactor source code files: {files}. Target metric is {targetScore}%.";
    
    PromptAssembler.VariableDef filesVar = new PromptAssembler.VariableDef();
    filesVar.type = "array";
    
    PromptAssembler.VariableDef scoreVar = new PromptAssembler.VariableDef();
    scoreVar.type = "number";
    
    spec.variables = Map.of(
        "files", filesVar,
        "targetScore", scoreVar
    );
    spec.required = List.of("files");
  }

  @Test
  @DisplayName("Assemble performs clean interpolation on correct inputs")
  void testSuccessfulAssembly() {
    Map<String, Object> vars = Map.of(
        "files", List.of("index.js", "styles.css"),
        "targetScore", 95
    );

    PromptAssembler.RenderedPrompt prompt = assembler.assemble(spec, vars);
    assertThat(prompt.systemPrompt).isEqualTo("System Instructions: Clean up redundant code.");
    assertThat(prompt.userPrompt).contains("[\"index.js\",\"styles.css\"]");
    assertThat(prompt.userPrompt).contains("95%");
  }

  @Test
  @DisplayName("Assemble fails when a required variable is missing")
  void testMissingRequiredVariable() {
    Map<String, Object> vars = Map.of(
        "targetScore", 95
    );

    assertThatThrownBy(() -> assembler.assemble(spec, vars))
        .isInstanceOf(IllegalArgumentException.class)
        .hasMessageContaining("Missing required prompt variable: files");
  }

  @Test
  @DisplayName("Assemble fails when variable type is incorrect")
  void testIncorrectVariableType() {
    Map<String, Object> vars = Map.of(
        "files", "not-an-array-string", // should be array
        "targetScore", 95
    );

    assertThatThrownBy(() -> assembler.assemble(spec, vars))
        .isInstanceOf(IllegalArgumentException.class)
        .hasMessageContaining("Variable 'files' must be an array");
  }
}
