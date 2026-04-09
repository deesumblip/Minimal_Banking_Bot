A **flow** is a unit of conversation. It encodes the business logic for a specific process: a step-by-step plan for how your agent handles a particular interaction.

Flows sit toward the guided end of the autonomy spectrum. They're the right tool when the process is well-defined, order matters, and you don't want a language model improvising. Think multi-step onboarding, form collection, account verification. Anything where deviation from the path is a bug, not a feature.

**File location:** `data/basics/*.yml` — one file per flow, or group related flows in the same file.

**Analogy**: A flow is like a recipe. It has:
- A name (what recipe is this?)
- A description (what does this recipe make?)
- Steps (what should it do, in what order?)


#### Flow Execution

When a flow is activated, Rasa executes each step in order:

```
User says "hello"
    ↓
Flow: greet is activated
    ↓
Step 1: utter_greet
    ↓
Agent responds: "Hi! I'm a banking assistant..."
    ↓
Flow completes
```
Linear, predictable, inspectable. When something goes wrong, you know exactly where to look.

---