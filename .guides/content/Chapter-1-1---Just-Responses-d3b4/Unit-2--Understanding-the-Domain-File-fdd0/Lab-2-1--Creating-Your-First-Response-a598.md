**Objective**: Add a new `utter_goodbye` response to your agent’s domain file.

#### Step-by-Step Tutorial

**Step 1: Open the domain file**

1. In your project, open **`level1/domain/basics.yml`**.
2. Confirm it starts with `version: "3.1"` and contains a `responses:` section with entries such as `utter_greet`, `utter_help`, and `utter_contact`.

**Step 2: Find `responses:`**

Scroll to `responses:` (near the top). You should see blocks like:

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

Each response name uses the `utter_` prefix and is indented under `responses:`.

**Step 3: Add `utter_goodbye`**

1. After the **last** response in the list, add a blank line, then paste:

   ```yaml
   utter_goodbye:
     - text: "Goodbye! Have a great day!"
       metadata:
         rephrase: True
   ```

2. **Indentation**: `utter_goodbye:` lines up with `utter_contact:`; `- text:` is indented two more spaces; `metadata:` lines up with `text:`; `rephrase: True` is under `metadata:`.

**Step 4: Check before you save**

- Spaces only (no tabs); consistent 2-space indents.
- Response name ends with `:`; `-` before `text:`; `metadata:` aligned with `text:`.
- Spelling: `utter_goodbye`, `rephrase`.

**Step 5: Save**

Save `basics.yml` (e.g. Ctrl+S / Cmd+S).

#### Complete example

Your `responses:` section should look like this (with your new block at the end):

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

1. **Missing `-`** before `text:` (YAML expects a list item).
2. **Wrong indentation** — YAML is strict; use 2 spaces per level.
3. **Missing `:`** after the response name (`utter_goodbye:`).
4. **`metadata:`** must align with `text:`, not with the `-`.

{Check It!|assessment}(code-output-compare-101020002)

---
