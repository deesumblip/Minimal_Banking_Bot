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
| Field | What it does |
|---|---|
| `action_endpoint` | Tells Rasa where to find custom actions. `actions_module: "actions"` points to the `actions/` folder. This folder is not used in Level 1 of this course and will be used in Level 2. |
| `nlg` | Enables response rephrasing. When `type: rephrase` is set, Rasa uses an LLM to rewrite templated responses in the context of the conversation before sending them, making replies sound more natural. |
| `model_groups` | Declares the LLM provider and model used for command generation and rephrasing. The `id` here matches the `model_group` reference in `config.yml`, keeping model definitions in one place. |
| `provider: rasa` | Uses the course tutorial model hosted at https://tutorial-llm.rasa.ai. |
| `model` | The specific model used for this course: a fine-tuned Llama 3.1 8B instruct model optimized for the simple tasks in this course so you don't have to bring your own API key. |


{Check It!|assessment}(multiple-choice-2982013912)


---


