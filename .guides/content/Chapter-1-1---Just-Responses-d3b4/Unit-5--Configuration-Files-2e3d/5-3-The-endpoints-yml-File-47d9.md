

The `endpoints.yml` file defines **where Rasa can find actions, tools, and LLM configuration**.

**File Location**: `endpoints.yml` (root of your bot folder)

#### Complete endpoints.yml Breakdown

```yaml
action_endpoint:
  actions_module: "actions"

nlg:
  type: rephrase
  llm:
    model_group: gpt-4o-mini

model_groups:
  - id: gpt-4o-mini
    models:
      - provider: openai
        model: gpt-4o-mini-2024-07-18
        temperature: 0.3
```

#### Section-by-Section Explanation

1. **`action_endpoint:`**
   - Tells Rasa where to find custom actions
   - `actions_module: "actions"` means "look in the `actions/` folder"
   - For Level 1, this folder is empty (no actions yet)

2. **`nlg:`** (Natural Language Generation)
   - Defines how responses are generated
   - `type: rephrase`: Allows LLM to rephrase responses
   - This is why `rephrase: True` in responses works
   - `model_group: gpt-4o-mini`: Which LLM to use for rephrasing

3. **`model_groups:`**
   - Defines LLM configurations
   - `id: gpt-4o-mini`: Name of this model group
   - `provider: openai`: Which LLM provider to use
   - `model: gpt-4o-mini-2024-07-18`: Specific model version
   - `temperature: 0.3`: How creative the LLM should be (0.0 = deterministic, 1.0 = very creative)

#### Understanding `actions_module`

When you write `actions_module: "actions"`, Rasa:
1. Looks for a folder named `actions/`
2. Looks for Python files in that folder
3. Looks for classes that inherit from `Action`
4. Makes those available as actions in your flows

For Level 1, the `actions/` folder doesn't exist yet (we'll create it in Level 2).

{Check It!|assessment}(multiple-choice-2982013912)


---