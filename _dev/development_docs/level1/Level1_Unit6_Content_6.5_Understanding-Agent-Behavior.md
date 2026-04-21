### 6.5 Understanding Agent Behavior

**Why this matters**: When the agent says something unexpected, you need a mental model of what happened. Message → pipeline (LLM) → flow match → steps → domain responses. Knowing that chain helps you fix issues: for example, if the wrong flow runs, improve the description; if the text is wrong, fix the domain.

#### How the Agent Decides What to Do

1. User sends a message (e.g. "hello").
2. Pipeline (LLM) processes the message and understands intent.
3. FlowPolicy searches flows and matches the best flow description.
4. Rasa runs that flow's steps (e.g. `utter_greet`).
5. Domain provides the response text; the agent replies.

Training builds a model that encodes your flows and domain so this process runs correctly at runtime.

---
