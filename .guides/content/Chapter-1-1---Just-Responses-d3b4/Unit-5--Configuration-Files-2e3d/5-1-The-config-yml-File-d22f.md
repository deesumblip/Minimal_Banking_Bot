The `config.yml` file tells Rasa **how to build your agent**. It's like the blueprint that defines the agent's architecture.

**File Location**: `config.yml` (root of your agent folder)

#### Complete config.yml Breakdown

```yaml
recipe: default.v1
language: en
assistant_id: level1-agent

pipeline:
  - name: SearchReadyLLMCommandGenerator
    llm:
      model_group: gpt-4o-mini

policies:
  - name: FlowPolicy
```

#### Section-by-Section Explanation

1. **`recipe: default.v1`**
   - Which Rasa recipe to use
   - `default.v1` is the standard Rasa Pro recipe
   - Recipes define the default configuration

2. **`language: en`**
   - The language your agent speaks
   - `en` = English
   - Change to `es` for Spanish, `fr` for French, etc.

3. **`assistant_id: level1-agent`**
   - Unique identifier for this agent
   - Used in logs and tracking
   - Should be unique if you have multiple agents

4. **`pipeline:`**
   - Defines how Rasa understands user messages
   - `SearchReadyLLMCommandGenerator`: Uses an LLM to understand messages and start the right flow.
   - `model_group: gpt-4o-mini`: Which model group to use (configured in `endpoints.yml`).

5. **`policies:`**
   - Defines how Rasa decides what to do next
   - `FlowPolicy`: Uses the flows you defined to decide responses
   - This is what makes your flows actually work

#### Simplified Mental Model

```text
config.yml = "How to build this agent"
  ├── recipe: "Use Rasa Pro standard recipe"
  ├── language: "English"
  ├── assistant_id: "level1-agent (unique name)"
  ├── pipeline: "Use an LLM to start flows"
  └── policies: "Use flows to decide responses"
```

{Check It!|assessment}(multiple-choice-2496482437)


---