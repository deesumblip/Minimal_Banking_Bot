# Lab 3.1 – Reference solution for LLM Rubric Autograde

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 3.1 (Defining a Slot in the Domain).

---

## Required changes in level3/domain/basics.yml

1. **slots: section** – Add a `slots:` section (before or after other top-level keys). It must contain at least the `account` slot.

2. **account slot** – The slot must be named `account` and have `type: text` (or equivalent valid slot type). Example:

```yaml
slots:
  account:
    type: text
```

3. **utter_ask_account response** – Under `responses:`, add a response named `utter_ask_account` with at least one message (e.g. "What is your account number?"). Example:

```yaml
responses:
  # ... other responses ...
  utter_ask_account:
    - text: "What is your account number?"
      metadata:
        rephrase: True
```

---

## Rubric summary for autograde

- **slots: section:** Present in domain/basics.yml with valid YAML.
- **account slot:** Present under slots with type text (or equivalent).
- **utter_ask_account:** Present under responses with at least one message.
- **Valid YAML / structure:** File is valid; existing Level 2 content (responses, actions) is preserved.
