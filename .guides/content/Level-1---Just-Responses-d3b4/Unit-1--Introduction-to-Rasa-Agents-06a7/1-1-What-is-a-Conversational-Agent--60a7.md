
Chatbots, digital assistants, virtual agents. The labels change, but the idea is steady: software that talks with people in **natural language**. This course uses **conversational agent**, or **agent** for short.

Shipping one is harder than it sounds. Users paraphrase, change their minds, and expect the system to track what they just said. **Rasa** exists to build **dialogue systems** that can span the whole range from **guided, step-by-step flows** to behavior that **reasons and uses tools**. Not canned replies or a decision tree with a thin coat of “AI.”

#### What good agents get right

First, **understanding**: mapping many phrasings to the same goal and using **context** so follow-ups still make sense. For example, someone might say “What are your hours?”, then “And on Sundays?”, then “When can I stop by?” A brittle system treats those as unrelated strings. A capable agent treats them as one conversation.

Second, **memory**: state carried from turn to turn so people are not repeating themselves. Rasa supports this. **rich memory** appears in **Level 3**, while **Level 1** stays deliberately small.

Third, **dialogue management**: the layer that decides each turn whether to clarify, move a flow forward, call a **tool**, or end. Without those decisions, you have a lookup table, not an agent.

#### Rule-based, autonomous, and hybrid agents

Design is a tradeoff about how much freedom you give the system. **Rule-based** agents follow fixed scripts. They are predictable and safe for strict processes such as **compliance** workflows and **onboarding**, but they struggle when users go off-script. **Fully autonomous** agents take a goal plus **tools** and reason toward an outcome. They suit open-ended tasks but need careful design so flexibility does not turn into chaos.

**Hybrid** agents mix **guided flows** with more open-ended steps. **Rasa is aimed at that blend**: precision where you need it, flexibility where you do not. Most serious production agents end up hybrid, and this course prepares you for that path.

#### Why Rasa Pro and CALM

Rasa has years of production use. The framework is built for **dialogue**. Understanding, memory, reasoning, and orchestration in one place. Instead of generic ML pieces you wire up yourself. **Rasa Pro** with **CALM** adds **LLM-powered understanding** and **flow-based structure**, so you can start with a modest agent and grow without throwing your work away.

#### What you will do in this course

The levels stack. **Level 1** gives you concepts, terminology, **flows**, and **responses**. The mental model for everything after. As you continue, you will move toward agents that cover varied phrasing, dependable flows, tools where they matter, and stronger context, wired together as **one orchestrated system**.

---
