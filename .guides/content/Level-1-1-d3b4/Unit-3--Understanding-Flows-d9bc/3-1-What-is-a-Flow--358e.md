A **flow** is a conversation script - a step-by-step plan for how the bot should handle a particular conversation path.

**File Location**: `data/basics/*.yml` (one file per flow, or multiple flows per file)

**Analogy**: A flow is like a recipe. It has:
- A name (what recipe is this?)
- A description (what does this recipe make?)
- Steps (what do I do, in order?)

#### Flow Execution

When a flow is triggered, Rasa executes each step in order:

```
User says "hello"
    ↓
Flow: greet is triggered
    ↓
Step 1: utter_greet
    ↓
Bot responds: "Hi! I'm a banking assistant..."
    ↓
Flow completes
```

---