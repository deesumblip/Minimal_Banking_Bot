### 3.2 Flow Structure Deep Dive

Before you create your own flow, it helps to see how an existing one is built. Every flow you add will follow this same pattern: a name, a description the LLM uses to match user messages, and steps that run in order.

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

1. **`flows:`**: Top-level key – indicates this file contains flow definitions.

2. **`greet:`**: Flow name – the identifier used to reference the flow. Must be unique. Convention: lowercase, descriptive.

3. **`name: say hello`**: Human-readable name for logs and debugging.

4. **`description: ...`**: **Critical.** The LLM uses this to match user messages to flows. It should be clear and specific. For example, "Greet the user when they start a conversation" helps the LLM trigger on "hello", "hi", and "hey".

⚠️ **Critical**: Flow descriptions are **essential**! Without a good description, the LLM won't know when to trigger your flow.

**Example of good vs bad descriptions**:
- ❌ **Bad**: "Say hello" (too vague)
- ✅ **Good**: "Greet the user when they start a conversation," because it gives clear context and purpose.

5. **`steps:`**: The actual steps to execute – a list of actions in order.

6. **`- action: utter_greet`**: A single step – `action:` indicates an action step; `utter_greet` must be defined in the domain.

---
