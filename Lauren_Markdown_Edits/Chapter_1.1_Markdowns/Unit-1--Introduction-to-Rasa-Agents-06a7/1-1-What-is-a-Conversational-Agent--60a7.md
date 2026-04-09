# Level 1: What is a conversational agent?

You've probably heard a dozen names for the thing you're about to build. Digital assistant. Virtual agent. Voicebot. Chatbot (if someone is being dismissive). The terminology has shifted every few years, but the idea underneath all of it has stayed the same: a system that communicates with humans in natural language. A conversational interface. 

In this course, we call it a **conversational agent**, or just an **agent**. And with Rasa, you're not gluing together canned responses or wiring up a decision tree disguised as intelligence. You're building dialogue systems that can orchestrate conversations across a real spectrum of autonomy, from tightly guided flows to sub-agents that reason and act on their own.

There's a meaningful difference between those two things. Let's make sure it lands before we go further.

---

## What actually makes a conversational agent good?

Three things separate an agent that works from one that frustrates users into giving up.

### It understands what people mean, not just what they type

Real users don't read your documentation. They don't phrase things the way your training data expected. They'll ask the same question five different ways:

- "What are your hours?"
- "And on Sundays?"
- "When can I stop by?"

Those three messages look totally different on the surface. A naive system treats them as three separate, unrelated inputs. A good agent recognizes they're all circling the same intent, and that the second one only makes sense in the context of the first. Dialogue understanding is about building that kind of recognition into your system, not just matching keywords.

### It remembers

Humans remember what was said ten seconds ago. Your agent needs to as well. Nothing kills user trust faster than a system that makes you repeat yourself.

Memory isn't magic. It's state that gets tracked, stored, and fed back into the conversation at the right moments. Rasa handles this natively. You're not bolting it on as an afterthought. *(Full memory features come in Level 3, but you'll see the groundwork for them throughout.)*

### It makes decisions

A conversation is a sequence of micro-decisions. Should I ask a clarifying question or make an assumption? Has the user changed topics, or are they still pursuing the same goal? Is it time to call an external API, or do I have enough information already?

These decisions happen at every turn. A dialogue management system is the part of your agent that makes them. Without it, you don't have a conversational agent. You have a lookup table.

---

## Three types of agents, one spectrum

When you start designing an agent, the first real question is: how much control do you want to hand to the system?

**Rule-based agents** follow explicit scripts. Every path is defined in advance. They're predictable, they won't hallucinate, and they're the right tool when the process is well-defined and deviating from it would cause real problems. Think compliance workflows, regulated industries, step-by-step onboarding. The tradeoff is rigidity. If a user goes off-script, the agent struggles.

**Fully autonomous agents** work differently. You give them a goal and a set of tools, and they reason their way to a result. They're well-suited for open-ended tasks where the right path isn't knowable in advance. The tradeoff is that they require more care to keep reliable. Flexibility can become unpredictability if the design isn't tight.

**Hybrid agents** are where Rasa shines. You orchestrate guided flows and autonomous reasoning together in the same system. Predictable steps where you need precision, autonomous reasoning where you need flexibility. The architecture supports both, and you control the balance.

Most production agents worth building end up hybrid. That's what this course prepares you for.

---

## Why Rasa

Rasa has been running in production since 2016. That's not a marketing point, it's a signal about what the framework prioritizes: systems that actually ship to real users, at scale, with the edge cases and failures that don't show up in demos.

The framework gives you conversation-native primitives, tools built specifically for the problems you run into when building dialogue systems, not generic ML infrastructure you have to adapt. Understanding, memory, reasoning, and orchestration all live in one coherent system. The components are modular, so teams can split work across the stack without constantly stepping on each other.

You can start simple. You can get more complex without rewriting everything. That arc is intentional.

---

## What you'll build in this course

By the end, you'll have an agent that can:

- Understand user reliably, even when phrasing varies
- Follow guided flows that behave predictably and don't hallucinate
- Run autonomous skills that reason through problems using tools
- Remember context across turns and use it to make better decisions
- Combine all of the above in a single, orchestrated system

Each level builds on the last. Level 1 is the foundation: concepts, terminology, and the mental model you'll need to make sense of everything that follows.

Let's get into it.