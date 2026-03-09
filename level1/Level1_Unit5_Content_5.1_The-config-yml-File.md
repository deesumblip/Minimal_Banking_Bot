### 5.1 The config.yml File

The `config.yml` file tells Rasa **how to build your bot**. It's the blueprint that defines the bot's architecture.

**Why it matters**: Your domain and flows say *what* the bot can say and do. The config says *how* Rasa turns that into a running bot: which language model understands the user, which policy picks flows, and so on. You rarely edit it in Level 1, but knowing where it is and what it controls helps when something doesn't work or when you move to later levels.

**File Location**: `config.yml` (root of your bot folder)

#### Key sections

- **`recipe: default.v1`** – Standard Rasa Pro recipe
- **`language: en`** – Bot language, such as `en`, `es`, or `fr`
- **`assistant_id: level1-bot`** – Unique identifier for this bot
- **`pipeline:`** – How Rasa understands user messages (LLM-based command generator)
- **`policies:`** – How Rasa decides what to do next; for example, `FlowPolicy` uses your flows.

**Mental model**: config.yml defines how to build the bot: recipe, language, pipeline, and policies.

---
