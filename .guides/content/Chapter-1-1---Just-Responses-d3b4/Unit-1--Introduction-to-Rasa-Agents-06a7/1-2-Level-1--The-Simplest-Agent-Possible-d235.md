
Level 1 is the **absolute minimum** a working Rasa agent needs: **responses**, **flows**, and **configuration**—nothing else. We start here so the core ideas stick before you add memory, tools, and richer logic.

#### What Level 1 includes

You work with three building blocks:

- **Responses** — predefined messages the agent can send.
- **Flows** — simple conversation scripts that decide **when** to send which response.
- **Basic configuration** — files that tell Rasa how to assemble and run the agent.

#### What Level 1 does not include

There is **no memory across turns** (no **slots**), **no custom Python or external integrations** (no **actions** / tool calls), and **no responses that change from context alone**—what the agent says is declared in advance. Heavier **autonomy** and **LLM-driven reasoning** belong in later levels. Here the surface area stays small on purpose.

#### Why we begin here

The cognitive load stays low: you mostly think about **responses** and how **flows** trigger them. You can get a runnable agent quickly, and many real systems stay close to this shape for straight FAQ-style help. Later, when you build more open-ended or hybrid agents, you will still reach for these same pieces whenever you need a **controlled, predictable** path.

#### What Level 1 is good for

Use cases like **FAQs, hours, contact information, and simple guided help**—situations where the conversation path is known ahead of time and the user does not need the agent to remember earlier turns. In short: at this level the agent can **reply** from fixed content; it does not yet **remember**, **reason**, or **act** beyond those scripted responses.

---
