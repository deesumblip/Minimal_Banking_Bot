**Objective**: Add a new `utter_goodbye` response to your agent’s domain file.

#### Step-by-step

**Step 1: Open the domain file**

In your project, open **`level1/domain/basics.yml`**. Confirm the file begins with `version: "3.1"` and that a **`responses:`** section lists entries such as `utter_greet`, `utter_help`, and `utter_contact`.

**Step 2: Review existing responses**

Scroll to **`responses:`** near the top. You should see blocks similar to:

```yaml
responses:
  utter_greet:
    - text: "Hi! I'm a banking assistant. How can I help you today?"
      metadata:
        rephrase: True

  utter_help:
    - text: |
        I can help you with:
        ...
  utter_contact:
    - text: "You can reach us at support@bank.com or call 1-800-BANK-123."
      metadata:
        rephrase: True
```

Each response name uses the `utter_` prefix and sits under **`responses:`** with consistent indentation.

**Step 3: Add `utter_goodbye`**

1. After the **last** response block, add a blank line, then add your new response. You may change the farewell text, but keep the same shape as the other responses:

 ```yaml
   utter_goodbye:
     - text: "Goodbye! Have a great day!"
       metadata:
         rephrase: True
   ```

2. **Indentation:** Align **`utter_goodbye:`** with names like **`utter_contact:`**. The **`- text:`** line is indented two spaces deeper than the response name. **`metadata:`** lines up with **`text:`**, and **`rephrase: True`** sits under **`metadata:`**.

Response order does not change how Rasa runs, but keeping the file tidy makes later edits easier.

**Step 4: Check before you save**

- Use spaces only, no tabs, with two spaces per indent level.
- The response name ends with a colon. Each message line starts with **`-`** before **`text:`**.
- Spell **`utter_goodbye`** and **`rephrase`** exactly as shown.

**Step 5: Save**

Save **`basics.yml`**, for example with Ctrl+S on Windows or Cmd+S on macOS.

#### Complete example

Your **`responses:`** section should look like the following, with your new block at the end:

```yaml
responses:
  utter_greet:
    - text: "Hi! I'm a banking assistant. How can I help you today?"
      metadata:
        rephrase: True

  utter_help:
    - text: |
        I can help you with:
        - Checking your balance
        - Transferring money
        - Bank hours
        - Contact information
      metadata:
        rephrase: True

  utter_contact:
    - text: "You can reach us at support@bank.com or call 1-800-BANK-123."
      metadata:
        rephrase: True

  utter_goodbye:
    - text: "Goodbye! Have a great day!"
      metadata:
        rephrase: True
```

#### Common mistakes

1. **Missing `-`** before **`text:`**. YAML expects each message to be a list item.
2. **Wrong indentation.** YAML is strict. Use two spaces per level and do not mix tabs.
3. **Missing `:`** after the response name, for example **`utter_goodbye:`**.
4. **`metadata:`** must line up with **`text:`**, not with the leading **`-`**.

{Check It!|assessment}(code-output-compare-101020002)

---
