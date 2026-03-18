# Welcome to Building Conversational Agents with Rasa

We’ve all heard a lot of names for systems that can “talk”: *bots*, *digital assistants*, *virtual agents*, or more recently just *agents* (not to be confused with human agents!). Names have changed over the years, but the core idea hasn’t: these are **conversational interfaces**. Systems that communicate with humans in natural language.

In this course, we’ll use the term **conversational agent**, or simply **agent**. With Rasa, you’re not just wiring up scripts that return canned replies. You’re building **dialogue systems that can manage conversations across a spectrum of autonomy**, from fully guided flows to semi- or fully autonomous interactions.

---

## Key Characteristics

### Dialogue Understanding
Users don’t follow scripts, they speak like humans. A strong agent understands all the variations of user input well.

**Example:**
- “What are your hours?”
- “And on Sundays?”
- “When can I stop by?”

Even though these look different, they express the same intent. A good agent can **recognize meaning** even when phrasing changes or a message only makes sense in the context of previous conversation.

---

### Memory
Conversations aren’t one-offs. Humans remember what was said before, and your agent should too. Nobody likes repeating themselves.

Memory is an artifact that needs to be preserved and managed to keep your agent **context-aware**. Tracking relevant facts and previous conversation history to guide interactions naturally is a native function of Rasa.

*(In this course, memory features are introduced in Level 3.)*

---

### Dialogue Management
Conversations don’t manage themselves. Agents need to **make decisions at every turn**.

**For example:**
- Allow users to correct information they already gave you
- Determine when to call a tool, API, or external system
- Choose the next action to move toward a goal
- Handle topic changes while keeping the original conversation thread in mind

A good dialogue management system can help the user achieve their goals without having to adjust their langauge or approach for your system. 

---

## Types of Agent skills

**Rule-Based Agents** – Fully scripted flows  
- ✅ Pros: predictable, no hallucinations  
- ❌ Cons: rigid; conversations can feel robotic  
- Best for regulated or process-heavy scenarios where the steps are clear and the system should not deviate. 

**Fully-Autonomous Agents** – Chains of reasoning that can decide how to accomplish a goal using a set of tools  
- ✅ Pros: flexible, great for open-ended, exploratory, or research-driven conversations  
- ❌ Cons: needs careful design to stay accurate and reliable
- Best for open-ended consultation, research, or negotiation. 

**Hybrid Agents** – A mix of both  
- Orchestrate guided and autonomous skills together  
- Flexibility when you need it, precision when you want it. Rasa excells here. 

---

## Why Use Rasa?

- **Proven developer framework** – Rasa has been powering production-grade conversational interfaces since 2016. We’ve seen what it takes to take a conversation from prototype to scalable system, and the framework gives you the conversation native primitives you actually need to ship great agents.  

- **Flexible dialogue management** – Start simple with fully guided flows, go all-in with fully autonomous agents, or mix and match with a hybrid approach. You’re in control: scale complexity at your own pace, experiment freely, and push the boundaries of what your agents can do.  

- **End-to-end orchestration** – Understanding, memory, reasoning—all in one cohesive system. Rasa’s modular design means you can split, port, and publish components independently, making it easy for teams to collaborate without stepping on each other’s toes. Build smarter agents, faster, and keep your team sane while doing it.

---

## What you will learn

By the end of this course, you’ll be able to build agents that handle:

- **Dialogue Understanding** – Use language models to truly understand the intent of your users and what they want to accomplish.  
- **Guided Flows** – Build predictable, maintainable flows that don’t hallucinate.  
- **Autonomous Skills** – ReAct-style skills that can reason and act using tools.  
- **Memory** – Capture, store, and leverage conversation data to inform decisions and update systems.  
- **Orchestration** – Combine guided and autonomous skills into a single, flexible agent.

By the end of this course, you’ll have an **intelligent agent** that can think, act, and remember.