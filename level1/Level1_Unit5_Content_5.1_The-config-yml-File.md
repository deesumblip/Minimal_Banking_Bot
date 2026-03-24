### 5.1 The config.yml File

The `config.yml` file tells Rasa **how to build your agent**. It's the blueprint that defines the agent's architecture.

**Why it matters**: Your domain and flows say *what* the agent can say and do. The config says *how* Rasa turns that into a running agent: which language model understands the user, which policy picks flows, and so on. You rarely edit it in Level 1, but knowing where it is and what it controls helps when something doesn't work or when you move to later levels.

**File Location**: `config.yml` (root of your agent folder)

#### Key sections

- **`recipe: default.v1`** – Standard Rasa Pro recipe
- **`language: en`** – Agent language, such as `en`, `es`, or `fr`
- **`assistant_id: level1-agent`** – Unique identifier for this agent
- **`pipeline:`** – How Rasa understands user messages (LLM-based command generator)
- **`policies:`** – How Rasa decides what to do next; for example, `FlowPolicy` uses your flows.

**Mental model**: config.yml defines how to build the agent: recipe, language, pipeline, and policies.

---
