A **response** is a predefined message the bot can send to users. Responses are defined in the domain file and used in flows.

#### Response Structure

Let's examine a real response from `domain/basics.yml`:

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
    metadata:
      rephrase: True
```

**Breaking it down**:

1. **`utter_greet`**: The response name
   - Must start with `utter_` (Rasa convention)
   - `greet` is the descriptive part
   - This is how you reference the response in flows

2. **`- text: "..."`**: The actual message
   - The dash (`-`) means this is a list item
   - `text:` is the field name
   - The quoted string is what the bot will say

3. **`metadata: rephrase: True`**: Optional configuration
   - Tells the LLM it can vary the wording
   - Makes the bot feel more natural
   - The bot might say "Hello!" instead of "Hi!" sometimes

⚠️ **Important**: `rephrase: True` allows the LLM to vary the wording while keeping the same meaning. This makes conversations feel more natural - users notice when a bot says the exact same thing every time!

**Why this matters**: Real conversations aren't repetitive. Without `rephrase: True`, your bot will always say exactly the same thing. With it enabled, the bot can say "Hello!" one time and "Hi there!" another time, while meaning the same thing.

#### Why a List?

Responses are defined as lists because you can have multiple variations:

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
  - text: "Hello! How can I help you?"
  - text: "Welcome! I'm here to assist you."
```

Rasa will randomly select one of these when the response is used, making the bot feel more natural.

{Check It!|assessment}(multiple-choice-2055505786)

---
