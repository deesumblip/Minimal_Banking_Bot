
A **response** is a predefined message the agent can send. Responses are defined in the domain file and used in flows.

#### A real response from `domain/basics.yml`

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
    metadata:
      rephrase: True
```

#### What each part does

**Name, `utter_greet`.** Every response name starts with the `utter_` prefix. The part after the underscore is yours to choose. Flows reference this name when they want the agent to speak.

**List item, `- text: "..."`.** The dash means this entry is one item in a **list**. That matters because a single response can list several `text` lines. Rasa can pick among them. More on that below.

**Optional metadata, `rephrase: True`.** When this is set, the **LLM** may rephrase the wording while keeping the meaning. You can tune the rephraser in Rasa if you need tighter control. Without **`rephrase: True`**, the agent repeats the same string every time. Users notice when an agent sounds like a broken record.

With rephrasing enabled, “Hi! I'm a banking assistant.” might become “Hello! What can I help you with today?” on the next turn. Same intent, different words, and a less robotic feel.

⚠️ **Important:** `rephrase: True` is optional, but it is the main lever for natural variation at Level 1. Real conversations are not perfectly repetitive. This setting helps your agent match that expectation.

#### When to set `rephrase: False`

Rephrasing is great for conversational lines but risky for **exact information**. Set **`rephrase: False`** whenever a response contains literal text that must not change, for example:

- Email addresses and phone numbers
- Account numbers, reference codes, or IDs
- Legal disclaimers or policy wording
- Specific amounts, dates, or times

You'll see this pattern in the next lab: **`utter_contact`** uses **`rephrase: False`** so the support email and phone number stay exactly as written.

#### Why responses are lists

Responses are lists so you can offer **multiple canned lines** for the same intent. Rasa can choose one at random, which adds variety **without** relying on the LLM:

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
  - text: "Hello! How can I help you?"
  - text: "Welcome! I'm here to assist you."
```

You can combine that random pick with **`rephrase: True`** so both the template list *and* the rephraser contribute to variety.

{Check It!|assessment}(multiple-choice-2055505786)

---
