### 3.1 What is a Flow?

A **flow** is a conversation script - a step-by-step plan for how the agent should handle a particular conversation path.

**Why flows matter**: The agent has to decide what to do when the user says something. Flows are that decision map: when the user asks for help, run these steps, such as saying the help response. Without flows, the agent would have responses defined but no rule for when to use them. With flows, you design clear paths: greeting, help, contact, goodbye, hours, balance. The agent then behaves predictably.

**File Location**: `data/basics/*.yml`. You can put one flow per file or multiple flows per file.

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
Agent responds: "Hi! I'm a banking assistant..."
    ↓
Flow completes
```

---
