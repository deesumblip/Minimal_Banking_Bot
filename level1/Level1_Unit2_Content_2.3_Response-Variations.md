### 2.3 Response Variations

Having multiple variations of the same response makes your agent feel more natural and less robotic.

**Why we use them**: Users notice when a agent repeats the exact same phrase. Variations, plus `rephrase: True` where appropriate, keep the meaning the same but change the wording, so the agent feels more like a person and less like a script.

#### When to Use Variations

✅ **Good for**:
- Greetings: various ways to say hello
- Confirmations: different ways to say "yes"
- General information that can be phrased differently

❌ **Not good for**:
- Critical information such as account numbers or error codes
- Legal disclaimers that must be exact
- Step-by-step instructions where clarity matters more than variety

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
