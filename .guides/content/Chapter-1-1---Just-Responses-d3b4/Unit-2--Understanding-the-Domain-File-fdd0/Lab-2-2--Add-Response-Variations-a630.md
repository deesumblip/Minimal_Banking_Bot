**Objective**: Add a second variation to `utter_goodbye`.

**Before you begin**

- Finish **Lab 2.1** first so `utter_goodbye` already exists in the domain.
- Keep **`domain/basics.yml`** open in your editor.

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

#### How to verify

Both **`- text:`** lines should sit at the same indent. **`metadata:`** should align with **`text:`**, and **`rephrase: True`** should nest under **`metadata:`**. When you later run **`python -m rasa train`** from **`level1`** in Unit 6, valid YAML will train successfully; if training fails with a parse error, open the file at the line number in the message and fix indentation.

#### What this does

Each time the flow uses **`utter_goodbye`**, Rasa picks **one** of the **`text:`** lines at random, so the agent is less likely to repeat the exact same line if the user triggers goodbye several times. If **`rephrase: True`** is also set, the LLM can still vary wording on top of those templates, which stacks two kinds of variety together.

{Check It!|assessment}(code-output-compare-302300002)

---
