Now that you have registered your actions in the domain in **Lab 4.1**, you need flows that call them: the example **hours** flow and your **holiday_hours** flow. In Level 1, flows used only `utter_*` responses. In Level 2, flows can also call `action_*` custom actions.

#### Level 1 flow (response)

```yaml
flows:
  greet:
    name: say hello
    description: Greet the user when they start a conversation.
    steps:
      - action: utter_greet  # ← Uses a response
```

#### Level 2 flow (action)

```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours  # ← Uses an action
```

**What changes:** names starting with `utter_` refer to predefined text in the domain; names starting with `action_` refer to Python in `actions/`. In both cases you still write `- action:` under `steps:`. Rasa decides which kind of step it is from the name.

#### Mixing responses and actions in one flow

The same flow can chain both kinds of step. For example, you might run an action for dynamic content, then a response for static text:

```yaml
flows:
  hours_and_contact:
    name: hours and contact
    description: Tell the user bank hours and provide contact information.
    steps:
      - action: action_bank_hours      # ← Action (custom code)
      - action: utter_contact          # ← Response (predefined text)
```

**Execution order**

1. **`action_bank_hours`** runs first and sends the dynamic hours message.
2. **`utter_contact`** runs next and sends the static contact text.

---
