The **`description`** field on each flow is **critical** because the LLM uses it to connect user messages to the correct flow.

#### How matching works

1. The user sends a message.
2. The LLM reads every flow **`description`** in your project.
3. The model picks the description that best fits the message.
4. Rasa **triggers** that flow.

#### Writing useful descriptions

**Strong patterns**

- Be clear and specific, for example *Greet the user when they start a conversation*.
- Describe the outcome, for example *Provide contact information for the bank*.
- Give enough context, for example *Explain what the agent can help with*.

**Common mistakes**

- **Too vague:** *Help user* does not say what kind of help you mean.
- **Overfitted:** *Respond only when the user says the word hello exactly* misses natural variants such as “hi” or “hey.”
- **Missing intent:** *Say hello* does not state **when** the flow should run or **why**.

#### Example: one description, many phrasings

**Description:** *Greet the user when they start a conversation.*

**Messages that can match**

- "hello"
- "hi"
- "hey there"
- "good morning"
- "greetings"

The model treats these as the same kind of opening because the description names the **situation**, not a single keyword.

**Next:** In **Lab 3.5**, complete the hours and balance flow YAML with the fill-in-the-blank exercises. In **Lab 3.6**, add those flows and their responses to your **`level1`** project.

---
