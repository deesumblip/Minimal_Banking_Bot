Let's examine a real flow from `data/basics/greet.yml`:

```yaml
flows:
  greet:
    name: say hello
    description: Greet the user when they start a conversation.
    steps:
      - action: utter_greet
```

#### Breaking Down Each Component

1. **`flows:`**: Top-level key
   - Indicates this file contains flow definitions
   - All flows in this file go under this key

2. **`greet:`**: Flow name
   - This is the identifier used to reference the flow
   - Must be unique within the bot
   - Convention: lowercase, descriptive

3. **`name: say hello`**: Human-readable name
   - Used in logs and debugging
   - Helps humans understand what the flow doesgggh
   - Can be different from the flow identifier

4. **`description: ...`**: What the flow does
   - **Critical**: The LLM uses this to match user messages to flows
   - Should be clear and specific
   - Example: "Greet the user when they start a conversation" helps the LLM understand this flow should trigger on "hello", "hi", "hey", etc.

⚠️ **Critical**: Flow descriptions are **essential**! The LLM reads flow descriptions to understand what each flow does. Without a good description, the LLM won't know when to trigger your flow. Always write clear, specific descriptions.

**Example of good vs bad descriptions**:
- **Bad**: "Say hello" (too vague - when? why?)
- **Good**: "Greet the user when they start a conversation" (clear context and purpose)

5. **`steps:`**: The actual steps to execute
   - A list of actions to perform in order
   - Each step is indented with a dash (`-`)

6. **`- action: utter_greet`**: A single step
   - `action:` indicates this is an action step
   - `utter_greet` is the response to use (must be defined in domain)

{Check It!|assessment}(multiple-choice-1420316307)

---