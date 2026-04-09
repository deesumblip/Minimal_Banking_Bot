
People call them chatbots, digital assistants, and virtual agents. The names change; the idea does not: **software that holds natural-language conversations with users**. In this course we say **conversational agent** or **agent**.

With **Rasa**, you build dialogue systems that span a real range of autonomy—from **tightly guided flows** to parts that **reason and use tools**—not just canned replies or a decision tree dressed up as intelligence.

#### What makes an agent useful

**Understanding, not just matching.** Real users ignore your docs and ask the same thing in different ways—for example:

- "What are your hours?"
- "And on Sundays?"
- "When can I stop by?"

A weak system treats those as unrelated strings. A strong one ties them to **intent** and uses **context** so a follow-up still makes sense after the first message.

**State across turns.** People expect the agent to remember what was just said. That is **memory**: state carried forward and fed back on the next turn. Rasa supports this; **full memory features come in Level 3**. Level 1 keeps scope small on purpose.

**Decisions every turn.** Clarify, advance a flow, call a tool, or end? **Dialogue management** answers that. Without it, you have a lookup table, not an agent.

#### Rule-based, autonomous, and hybrid

**Rule-based** agents follow explicit scripts—strong when the process must be exact (compliance, onboarding); brittle when users go off-script.

**Fully autonomous** agents take a goal and **tools** and reason toward an outcome. They fit open-ended tasks but need tight design so flexibility does not become unpredictability.

**Hybrid** agents combine **guided flows** and **autonomous** reasoning. **Rasa is built for this**: precision where you need it, flexibility where you do not. Most production agents end up hybrid; this course prepares you for that path.

#### Why Rasa Pro and CALM

Rasa has years of production use. The framework targets **dialogue**—understanding, memory, reasoning, and orchestration in one stack—rather than generic ML pieces you bolt on yourself. **Rasa Pro** with **CALM** adds **LLM-powered understanding** and **flow-based structure**: you can start simple and grow without throwing your work away.

#### What you will build in this course

Levels stack on each other. **Level 1** is the foundation: concepts, terminology, flows, and responses—the mental model for everything that follows. As you advance, you move toward agents that handle varied phrasing, reliable flows, tools where they matter, and stronger context for decisions—**wiring it together in one orchestrated system**.

---
