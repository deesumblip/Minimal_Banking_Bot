### 5.1 The config.yml File

The `config.yml` file tells Rasa **how to build your bot**. It's the blueprint that defines the bot's architecture.

**File Location**: `config.yml` (root of your bot folder)

#### Key sections

- **`recipe: default.v1`** – Standard Rasa Pro recipe
- **`language: en`** – Bot language (e.g. `en`, `es`, `fr`)
- **`assistant_id: level1-bot`** – Unique identifier for this bot
- **`pipeline:`** – How Rasa understands user messages (e.g. `SearchReadyLLMCommandGenerator` with `model_group: gpt-4o-mini`)
- **`policies:`** – How Rasa decides what to do next (e.g. `FlowPolicy` – uses your flows)

**Mental model**: config.yml = how to build the bot (recipe, language, pipeline, policies).

---
