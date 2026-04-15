

The `endpoints.yml` file defines **where Rasa can find actions and how LLM features are configured**.

**File Location**: `endpoints.yml` (root of your agent folder)

#### Complete endpoints.yml Breakdown

```yaml
action_endpoint:
  actions_module: "actions"

nlg:
  type: rephrase
  llm:
    model_group: rasa_command_generation_model

model_groups:
  - id: rasa_command_generation_model
    models:
      - provider: rasa
        model: rasa/command-generator-llama-3.1-8b-instruct
        api_base: "https://tutorial-llm.rasa.ai"
```

#### Section-by-Section Explanation

1. **`action_endpoint:`**
   - Tells Rasa where to find custom actions
   - `actions_module: "actions"` means "look in the `actions/` folder"
   - For Level 1, this folder is empty (no actions yet)

2. **`nlg:`** (Natural Language Generation)
   - `type: rephrase` enables response rephrasing when a response has `metadata: rephrase: True`
   - `model_group: rasa_command_generation_model` selects which model group to use for rephrasing (same group id as in `config.yml`)

3. **`model_groups:`**
   - Declares which LLM provider and model to use
   - `provider: rasa` with `api_base: "https://tutorial-llm.rasa.ai"` uses the **course tutorial** hosted model (no personal OpenAI API key required for this setup)
   - `model: rasa/command-generator-llama-3.1-8b-instruct` is the model id served for command generation and related LLM features

#### Understanding `actions_module`

When you write `actions_module: "actions"`, Rasa:
1. Looks for a folder named `actions/`
2. Looks for Python files in that folder
3. Looks for classes that inherit from `Action`
4. Makes those available as actions in your flows

For Level 1, the `actions/` folder doesn't exist yet (we'll create it in Level 2).

{Check It!|assessment}(multiple-choice-2982013912)


---
