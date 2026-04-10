A **flow** is one conversational path your agent runs from start to finish. It encodes the **business logic** for a single process: an ordered plan for what should happen when that process applies.

Flows lean toward the **guided** end of the autonomy spectrum. They are the right tool when the steps are known in advance, **order matters**, and you do **not** want the language model inventing the sequence on the fly. Examples include onboarding checklists, scripted help, or any journey where straying from the path is a defect rather than a feature.

**Where flows live:** YAML files under **`data/basics/`**. You may use **one file per flow** or place **several related flows** in the same file.

**Analogy:** A flow works like a recipe. It needs a **name**, a short **description** of what it produces, and **steps** that say what to do, in order.

#### Flow execution

When a flow **triggers**, Rasa runs its **steps** in sequence:

```text
User says "hello"
    ↓
Flow greet runs
    ↓
Step 1: utter_greet
    ↓
Agent responds: "Hi! I'm a banking assistant..."
    ↓
Flow completes
```

The sequence is linear and easy to inspect. When behavior is wrong, you can usually tie it to a specific step.

---
