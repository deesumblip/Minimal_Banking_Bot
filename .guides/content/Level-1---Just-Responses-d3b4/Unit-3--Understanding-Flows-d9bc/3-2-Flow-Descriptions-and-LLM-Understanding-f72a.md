Rasa uses a component called the **Command Generator** to decide which flows and sub-agents to run. When a user sends a message, the Command Generator analyzes it using the current conversation context and relevant descriptions, then outputs commands like `StartFlow("greet")` that represent how the user wants to progress the conversation.

This makes `description:` the most critical field in a flow. The Command Generator relies on your description to understand when to trigger each flow. If your description is unclear or inaccurate, the right flow may never run.

**The routing process:**

1. User sends a message
2. The Command Generator analyzes the message using the current conversation context and relevant flow descriptions (not necessarily every flow)
3. The Command Generator outputs commands like `StartFlow("greet")` that represent how the user wants to progress the conversation

No intent classifiers. No keyword matching. No training data required. Just the sentences you write in your flow descriptions, measured against what the user said in the context of the conversation.

---

### What makes a description work

Write the **situation**, not the action. Be precise about the flow's purpose and scope. The Command Generator needs to know *when* the flow applies, not just *what* it does.

| Description | Problem |
|---|---|
| *Say hello* | Describes the action, not the trigger |
| *Help user* | Too vague, every flow could claim this |
| *Respond only when the user types hello exactly* | Too narrow, misses "hi", "hey", "good morning" |
| *Greet the user when they start a conversation* | Names the situation, matches naturally |

Additional tips:
- Use action verbs
- Use clear and standard language - avoid unusual phrasing
- Explain specialized terms or brand names
- Clarify implicit knowledge 

> If a flow is not activating at the right time, the `description:` is the first thing to check and adjust.

---

**Next:** In **Lab 3.4**, complete the hours and balance flow YAML with the fill-in-the-blank exercises. In **Lab 3.5**, add those flows and their responses to your **`level1`** project.

---
