# Level 1 scope

Level 1 covers the minimum needed to run a Rasa agent. We start simple to establish the core primitives and show all the ways dialogue can be managed in Rasa, from fully guided flows to more autonomous setups.

Even in largely autonomous systems where most user journeys are prompt-driven, the basics here remain useful when you need control and predictability in specific scenarios.

---

## What's included in Level 1

- **Responses** — predefined messages your agent can send
- **Flows** — the logic that decides when to send them
- **Basic config** — wiring everything together so it runs

## What's coming soon in later levels

- **Memory (slots)** — no persistence across turns
- **Tools (actions)** — no external logic or tool calls
- **Dynamic responses** — everything here is static
- **Autonomous behavior** — no LLM-driven reasoning

## What this level is good for

Answering FAQs, surfacing company or product information, and simple help flows where the path is known in advance and the agent doesn't need to remember anything between turns.

---

> At this level, the agent can respond. It can't yet remember, reason, or act.