### 5.3 endpoints.yml

The `endpoints.yml` file defines **where Rasa can find custom actions** and **how LLM-backed features (such as NLG rephrasing) reach a model**.

**Why it exists**: In Level 2 you'll add Python actions. Rasa needs to know where to find them; this file points to the `actions/` module. It also defines **`model_groups`** so the pipeline and NLG can use the same tutorial LLM (`rasa/command-generator-llama-3.1-8b-instruct` at `https://tutorial-llm.rasa.ai`) configured for this course—matching **`config.yml`**.

**File Location**: `endpoints.yml` (root of your agent folder)

#### Key sections

- **`action_endpoint:`** – The setting `actions_module: "actions"` means Rasa looks in the `actions/` folder for custom actions. For Level 1 this folder is empty.
- **`nlg:` / `model_groups:`** – Used when NLG rephrasing (or other LLM-backed NLG) runs; the **`model_group`** id must match **`config.yml`**. Level 1 still ships a full `endpoints.yml` so training and Inspector work with the same stack as later units.

For Level 1, the `actions/` folder doesn't exist yet. Level 2 adds it.

---
