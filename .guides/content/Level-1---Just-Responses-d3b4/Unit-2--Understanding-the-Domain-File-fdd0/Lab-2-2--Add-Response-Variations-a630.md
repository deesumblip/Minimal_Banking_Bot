**Objective**: Add a second variation to `utter_goodbye`.

#### Steps

1. Find **`utter_goodbye`** in **`domain/basics.yml`**. It should be the last block in the **`responses:`** section.
2. Add a second **`- text:`** line with a different farewell message. The new **`- text:`** must sit at the **same** indentation as the first **`- text:`** line. You might use lines such as “See you later!”, “Take care!”, or another short goodbye you prefer.
3. Keep a single **`metadata:`** block. It may sit under the last **`text:`** entry, which is the usual pattern when both lines share the same rephrasing settings.

**Example:**

```yaml
utter_goodbye:
  - text: "Goodbye! Have a great day!"
  - text: "See you later! Take care!"
    metadata:
      rephrase: True
```

#### What this does

Each time the flow uses **`utter_goodbye`**, Rasa picks **one** of the **`text:`** lines at random, so the agent is less likely to repeat the exact same line if the user triggers goodbye several times. If **`rephrase: True`** is also set, the LLM can still vary wording on top of those templates, which stacks two kinds of variety together.

{Check It!|assessment}(code-output-compare-302300002)

---
