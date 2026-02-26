The `config.yml` file tells Rasa **how to build your bot**. It's like the blueprint that defines the bot's architecture.

**File Location**: `config.yml` (root of your bot folder)

#### Complete config.yml Breakdown

```yaml
recipe: default.v1
language: en
assistant_id: level1-bot

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
   - The language your bot speaks
   - `en` = English
   - Change to `es` for Spanish, `fr` for French, etc.

3. **`assistant_id: level1-bot`**
   - Unique identifier for this bot
   - Used in logs and tracking
   - Should be unique if you have multiple bots

4. **`pipeline:`**
   - Defines how Rasa understands user messages
   - `SearchReadyLLMCommandGenerator`: Uses an LLM to understand natural language
   - `model_group: gpt-4o-mini`: Which LLM to use (OpenAI's GPT-4o-mini)

5. **`policies:`**
   - Defines how Rasa decides what to do next
   - `FlowPolicy`: Uses the flows you defined to decide responses
   - This is what makes your flows actually work

#### Simplified Mental Model

```
config.yml = "How to build this bot"
  ├── recipe: "Use Rasa Pro standard recipe"
  ├── language: "English"
  ├── assistant_id: "level1-bot (unique name)"
  ├── pipeline: "Use LLM to understand messages"
  └── policies: "Use flows to decide responses"
```

{Check It!|assessment}(multiple-choice-2496482437)


---