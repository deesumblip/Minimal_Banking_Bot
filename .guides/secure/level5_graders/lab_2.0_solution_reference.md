# Lab 2.0 – Reference solution for LLM Rubric / Code Test

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 2.0 (Command-generator prompt), or as reference for the code-output-compare grader.

---

## Required artifacts

1. **`level5/data/prompts/command_prompt_v3_slot_names.jinja2`** — Copy from **`level5/resources/command_prompt_v3_slot_names.jinja2`** (same filename).

2. **`level5/config.yml`** — Under **`pipeline`** → **`SearchReadyLLMCommandGenerator`**, set **`prompt_template`** so it references **`data/prompts/command_prompt_v3_slot_names.jinja2`** (path relative to the bot root `level5/`).

Example:

```yaml
pipeline:
  - name: SearchReadyLLMCommandGenerator
    prompt_template: data/prompts/command_prompt_v3_slot_names.jinja2
    llm:
      model_group: openai-gpt-5-1
```

---

## Rubric summary for autograde

- Prompt file exists at **`level5/data/prompts/command_prompt_v3_slot_names.jinja2`**.
- **`config.yml`** parses as YAML; **`SearchReadyLLMCommandGenerator`** has **`prompt_template`** whose string contains **`data/prompts/command_prompt_v3_slot_names.jinja2`**.
