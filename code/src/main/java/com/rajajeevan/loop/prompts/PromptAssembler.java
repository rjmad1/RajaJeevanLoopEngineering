package com.rajajeevan.loop.prompts;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.Map;

/**
 * Handles JSON-Schema driven prompt assembly. Loads prompt templates, validates input variables
 * against declared schemas, and renders the formatted LLM prompts.
 */
public class PromptAssembler {

  private static final ObjectMapper objectMapper = new ObjectMapper();

  /** Specification structure matching prompt-schema.json. */
  public static class PromptTemplateSpec {
    public String templateName;
    public String version;
    public String systemInstructions;
    public String templateText;
    public Map<String, VariableDef> variables;
    public List<String> required;
  }

  public static class VariableDef {
    public String type; // string, number, boolean, array, object
    public String description;
  }

  /** Holds the final rendered prompt messages. */
  public static class RenderedPrompt {
    public final String systemPrompt;
    public final String userPrompt;

    public RenderedPrompt(String systemPrompt, String userPrompt) {
      this.systemPrompt = systemPrompt;
      this.userPrompt = userPrompt;
    }
  }

  /**
   * Loads a template specification from file, validates input variables, and renders the prompt.
   *
   * @param specFile Prompt specification file
   * @param inputVariables Input values to interpolate
   * @return Rendered prompt containing system and user prompts
   * @throws IOException If parsing the specification fails
   * @throws IllegalArgumentException If variable validation fails
   */
  public RenderedPrompt assemble(File specFile, Map<String, Object> inputVariables)
      throws IOException, IllegalArgumentException {
    PromptTemplateSpec spec = objectMapper.readValue(specFile, PromptTemplateSpec.class);
    return assemble(spec, inputVariables);
  }

  /**
   * Validates input variables against specification constraints and renders the prompt.
   *
   * @param spec Prompt template specification object
   * @param inputVariables Input values to interpolate
   * @return Rendered prompt
   * @throws IllegalArgumentException If variable validation fails
   */
  public RenderedPrompt assemble(PromptTemplateSpec spec, Map<String, Object> inputVariables)
      throws IllegalArgumentException {
    validateVariables(spec, inputVariables);
    String userPrompt = interpolate(spec.templateText, inputVariables);
    return new RenderedPrompt(spec.systemInstructions, userPrompt);
  }

  private void validateVariables(PromptTemplateSpec spec, Map<String, Object> inputVariables) {
    if (spec.variables == null) {
      return;
    }

    // Check required fields
    if (spec.required != null) {
      for (String req : spec.required) {
        if (inputVariables == null || !inputVariables.containsKey(req) || inputVariables.get(req) == null) {
          throw new IllegalArgumentException("Validation Error: Missing required prompt variable: " + req);
        }
      }
    }

    if (inputVariables == null) {
      return;
    }

    // Check types
    for (Map.Entry<String, Object> entry : inputVariables.entrySet()) {
      String key = entry.getKey();
      Object val = entry.getValue();
      if (val == null) {
        continue;
      }

      VariableDef def = spec.variables.get(key);
      if (def == null) {
        // Undeclared variable - ignore or throw depending on policy. We will allow it but warning.
        continue;
      }

      switch (def.type.toLowerCase()) {
        case "string":
          if (!(val instanceof String)) {
            throw new IllegalArgumentException(
                String.format("Validation Error: Variable '%s' must be a string. Found: %s", key, val.getClass().getSimpleName()));
          }
          break;
        case "number":
          if (!(val instanceof Number)) {
            throw new IllegalArgumentException(
                String.format("Validation Error: Variable '%s' must be a number. Found: %s", key, val.getClass().getSimpleName()));
          }
          break;
        case "boolean":
          if (!(val instanceof Boolean)) {
            throw new IllegalArgumentException(
                String.format("Validation Error: Variable '%s' must be a boolean. Found: %s", key, val.getClass().getSimpleName()));
          }
          break;
        case "array":
          if (!(val instanceof Collection) && !(val instanceof Object[])) {
            throw new IllegalArgumentException(
                String.format("Validation Error: Variable '%s' must be an array. Found: %s", key, val.getClass().getSimpleName()));
          }
          break;
        case "object":
          if (!(val instanceof Map)) {
            throw new IllegalArgumentException(
                String.format("Validation Error: Variable '%s' must be an object (Map). Found: %s", key, val.getClass().getSimpleName()));
          }
          break;
        default:
          // Unknown type restriction
          break;
      }
    }
  }

  private String interpolate(String template, Map<String, Object> variables) {
    if (template == null) {
      return "";
    }
    if (variables == null) {
      return template;
    }
    String result = template;
    for (Map.Entry<String, Object> entry : variables.entrySet()) {
      String placeholder = "{" + entry.getKey() + "}";
      Object value = entry.getValue();
      String replacement;
      if (value instanceof Collection || value instanceof Object[]) {
        try {
          replacement = objectMapper.writeValueAsString(value);
        } catch (Exception e) {
          replacement = String.valueOf(value);
        }
      } else if (value instanceof Map) {
        try {
          replacement = objectMapper.writeValueAsString(value);
        } catch (Exception e) {
          replacement = String.valueOf(value);
        }
      } else {
        replacement = value != null ? value.toString() : "";
      }
      result = result.replace(placeholder, replacement);
    }
    return result;
  }
}
