### 2.3 Response Variations

Having multiple variations of the same response makes your bot feel more natural and less robotic.

#### When to Use Variations

✅ **Good for**:
- Greetings (various ways to say hello)
- Confirmations (different ways to say "yes")
- General information (can be phrased differently)

❌ **Not good for**:
- Critical information (account numbers, error codes)
- Legal disclaimers (must be exact)
- Step-by-step instructions (clarity is more important than variety)

#### Example: Multiple Variations

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
  - text: "Hello! I'm here to help with your banking needs."
  - text: "Welcome! How can I assist you today?"
    metadata:
      rephrase: True
```

When `utter_greet` is called, Rasa randomly selects one of these three options.

---
