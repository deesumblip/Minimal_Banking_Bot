### 5.3 endpoints.yml

The `endpoints.yml` file defines **where Rasa can find actions, tools, and LLM configuration**.

**File Location**: `endpoints.yml` (root of your bot folder)

#### Key sections

- **`action_endpoint:`** – `actions_module: "actions"` means Rasa looks in the `actions/` folder for custom actions. For Level 1 this folder is empty.
- **`nlg:`** – Natural Language Generation; `type: rephrase` and `model_group` enable response rephrasing (why `rephrase: True` in responses works).
- **`model_groups:`** – LLM config (provider, model, `temperature`). `temperature: 0.3` means somewhat creative but mostly consistent.

For Level 1, the `actions/` folder doesn't exist yet (Level 2 adds it).

---
