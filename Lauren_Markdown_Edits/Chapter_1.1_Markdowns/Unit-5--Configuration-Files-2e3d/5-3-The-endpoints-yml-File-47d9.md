

The `endpoints.yml` file defines **where Rasa can find actions and how LLM features are configured**.

**File Location**: `endpoints.yml` (root of your agent folder)

#### Complete endpoints.yml Breakdown

```yaml
action_endpoint:
  actions_module: "actions"

nlg:
  type: rephrase
  llm:
    model_group: openai-gpt-5-1

model_groups:
  - id: openai-gpt-5-1
    models:
      - provider: openai
        model: openai-gpt-5-1
        temperature: 0.3
```

#### Section-by-Section Explanation

1. **`action_endpoint:`**
   - Tells Rasa where to find custom actions
   - `actions_module: "actions"` means "look in the `actions/` folder"
   - For Level 1, this folder is empty (no actions yet)

2. **`nlg:`** (Natural Language Generation)
   - `type: rephrase` enables response rephrasing when a response has `metadata: rephrase: True`
   - `model_group: openai-gpt-5-1` selects which model group to use for rephrasing

3. **`model_groups:`**
   - Declares which LLM provider/model to use
   - `provider: openai` means the OpenAI API is used (requires `OPENAI_API_KEY`)
   - `temperature: 0.3` controls how “creative” the model is

#### Understanding `actions_module`

When you write `actions_module: "actions"`, Rasa:
1. Looks for a folder named `actions/`
2. Looks for Python files in that folder
3. Looks for classes that inherit from `Action`
4. Makes those available as actions in your flows

For Level 1, the `actions/` folder doesn't exist yet (we'll create it in Level 2).

{Check It!|assessment}(multiple-choice-2982013912)


---