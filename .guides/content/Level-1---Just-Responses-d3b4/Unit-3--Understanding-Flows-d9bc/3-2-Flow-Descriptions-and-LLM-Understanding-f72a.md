Rasa uses a component called the **Command Generator** to decide how to progress the conversation based on incoming user messages. The command generator is governed by a prompt that outlines how Rasa should orchestrate the conversation across different skills (flows and sub-agents). You can learn how to edit this prompt and see the defaults being used [here](https://rasa.com/docs/reference/config/components/llm-command-generators/). We are using the [SearchReadyLLMCommandGenerator](https://rasa.com/docs/reference/config/components/llm-command-generators/#searchreadyllmcommandgenerator) in this course. 

**How it works:**

1. A user sends a message
2. The Command Generator uses a language model to analyze the message, including the full conversation context (active flows, filled slots, relevant patterns, conversation history) alongside your flow descriptions
3. It outputs commands like `StartFlow("greet")` that represent how the user wants to progress the conversation

This makes `description:` one of the most important properties in a flow. If it is vague or inaccurate, the correct flow may never run, even if everything else is configured correctly.

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
