# 2.2 Understanding Responses

A response is a predefined message your agent can send. You define them in the domain file, reference them in flows. That's the whole contract.

Here's a real one from `domain/basics.yml`:

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
    metadata:
      rephrase: True
```

Three things to notice:

**`utter_greet`** is the response name. The `utter_` prefix is a Rasa convention — every response starts with it. The part after the underscore is yours to name. This is what you'll reference inside flows when you want the agent to say something.

**`- text: "..."`** is the actual message. The dash marks it as a list item, which matters more than it looks like it does (more on that in a second).

**`metadata: rephrase: True`** is optional, but worth understanding. It tells the LLM it can vary the phrasing while keeping the meaning intact. You can also update and tune the Rephraser prompt in Rasa. Without it, your agent says the exact same string every single time. Users notice. Nobody wants to talk to a system that sounds like a broken record.

With `rephrase: True`, "Hi! I'm a banking assistant." might come out as "Hello! What can I help you with today?" on the next run. Same intent, different words. Conversations feel less robotic for basically free.

---

## Why responses are lists

Responses are defined as lists because you can give Rasa multiple options and it'll pick one at random:

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
  - text: "Hello! How can I help you?"
  - text: "Welcome! I'm here to assist you."
```

This is one additional way to add variation without an LLM. Just write a few alternatives and Rasa handles the rest. 

{Check It!|assessment}(multiple-choice-2055505786)

---
