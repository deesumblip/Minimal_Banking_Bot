A **flow** is a conversational path your agent can run from start to finish. It encodes the **business logic** for a single process: an ordered plan for what should happen when that process applies.

Flows lean toward the **guided** end of the autonomy spectrum. They are the right tool when the steps are known in advance, **order matters**, and you do **not** want the language model inventing the sequence on the fly. Examples include onboarding checklists, scripted help, or any journey where straying from the path is a problem, not a feature.

**Where flows live:** YAML files under `data/basics/`. You may use one file per flow or place several related flows in the same file.

---

### Flow structure

Every flow requires three elements: an ID, a `description`, and `steps`. The `name` field is optional.

```yaml
flows:                          # Top level key
  greet:                        # Flow ID — unique, lowercase
    name: say hello             # Optional, human readable label
    description: Greet the user when they start a conversation  # LLM reads to decide when to activate
    steps:                      # Ordered list of actions the agent runs
      - action: utter_greet     # Sends a response, text defined in domain/basics.yml
```

The LLM routes by reading `description:` not `name:`, not the flow ID. A vague or missing description means the flow won't trigger reliably.

---

### Flow execution

When the `greet` flow is  activated by a user greeting, Rasa runs its steps in sequence:

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
