### 5.3 endpoints.yml

The `endpoints.yml` file defines **where Rasa can find custom actions**.

**Why it exists**: In Level 2 you'll add Python actions. Rasa needs to know where to find them; this file points to the `actions/` module. In Level 1 you don't use actions, but the file is here so the project is ready when you move on.

**File Location**: `endpoints.yml` (root of your bot folder)

#### Key sections

- **`action_endpoint:`** – The setting `actions_module: "actions"` means Rasa looks in the `actions/` folder for custom actions. For Level 1 this folder is empty.
- **`nlg:` / `model_groups:`** – Not used in Level 1. Later levels may add these when you enable LLM features.

For Level 1, the `actions/` folder doesn't exist yet. Level 2 adds it.

---
