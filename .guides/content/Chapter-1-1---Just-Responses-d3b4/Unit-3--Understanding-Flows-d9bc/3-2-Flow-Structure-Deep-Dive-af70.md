Let's examine a real flow from `data/basics/greet.yml`:

```yaml
flows:
  greet:
    name: say hello
    description: Greet the user when they start a conversation.
    steps:
      - action: utter_greet
```

#### Breaking down each part

1. **`flows:`** — Top-level key. It tells Rasa that this file defines flows. Every flow in the file nests under **`flows:`**.

2. **`greet:`** — The flow **id** your project uses internally. Keep it **unique**, **lowercase**, and descriptive.

3. **`name: say hello`** — A human-readable label for logs and debugging. It can differ from the id **`greet`**.

4. **`description:`** — **Critical for matching.** The LLM reads this text to decide when the flow fits the user’s message. Be concrete. For example, *Greet the user when they start a conversation* signals that “hello”, “hi”, and “hey” should all route here.

   Compare weaker and stronger wording:
   - **Too vague:** *Say hello* does not state **when** the flow should run.
   - **Too narrow:** *Respond only when the user types the word hello exactly* will miss natural variants such as “hi” or “hey.”
   - **Balanced:** *Greet the user when they start a conversation* gives enough context without locking you to one phrase.

5. **`steps:`** — Ordered actions to run. Each entry is a list item starting with **`-`**.

6. **`- action: utter_greet`** — One step. **`utter_greet`** must exist as a **response** in the domain.

⚠️ **Remember:** If **`description:`** is missing or fuzzy, the LLM cannot **trigger** the flow reliably. Clear sentences here pay off immediately in matching quality.

{Check It!|assessment}(multiple-choice-1420316307)

---
