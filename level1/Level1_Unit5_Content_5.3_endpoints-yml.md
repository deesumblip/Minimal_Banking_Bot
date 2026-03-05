### 5.3 endpoints.yml

The `endpoints.yml` file defines **where Rasa can find custom actions**.

**File Location**: `endpoints.yml` (root of your bot folder)

#### Key sections

- **`action_endpoint:`** – `actions_module: "actions"` means Rasa looks in the `actions/` folder for custom actions. For Level 1 this folder is empty.
- **`nlg:` / `model_groups:`** – Not used in Level 1. Later levels may add these if you enable LLM features.

For Level 1, the `actions/` folder doesn't exist yet (Level 2 adds it).

---
