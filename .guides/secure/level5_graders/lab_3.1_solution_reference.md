# Lab 3.1 – Reference solution for LLM Rubric / Code Test

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 3.1 (Registering Tools in endpoints.yml), or as reference for the code-output-compare grader.

---

## Required changes in level5/endpoints.yml

1. **tools: section** – Add a top-level key `tools:` (alongside `action_endpoint:`, etc.).
2. **tools_module** – Under `tools:`, set `tools_module: "tools"` so Rasa discovers the tools from the `tools` package (level5/tools/).

Example:

```yaml
action_endpoint:
  url: "http://localhost:5055/webhook"

tools:
  tools_module: "tools"
```

---

## Rubric summary for autograde

- **endpoints.yml** exists in level5.
- **tools:** key is present at top level.
- **tools_module: "tools"** is set under the tools section.
- File remains valid YAML; other sections (e.g. action_endpoint) can remain unchanged.
