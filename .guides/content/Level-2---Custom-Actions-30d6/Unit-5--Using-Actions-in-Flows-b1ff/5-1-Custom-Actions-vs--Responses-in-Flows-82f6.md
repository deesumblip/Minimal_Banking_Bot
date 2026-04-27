Both actions are now registered in the domain. The missing piece is flows that call them. In Level 1, flow steps called only `utter_*` responses. In Level 2, they can also call `action_*` custom actions.

| Step name | What Rasa calls |
|---|---|
| `utter_contact` | Template text in `domain/basics.yml` |
| `action_bank_hours` | Dynamic python class in `actions/*.py` |

The syntax for a response step or a custom action step is identical.
```yaml
# Level 1: response
steps:
  - action: utter_contact

# Level 2: custom action
steps:
  - action: action_bank_hours
```

The same flow can chain both. Rasa executes steps in order:

```yaml
flows:
  hours_and_contact:
    name: hours and contact
    description: Tell the user bank hours and provide contact information.
    steps:
      - action: action_bank_hours   # runs Python, returns dynamic hours
      - action: utter_contact       # sends static contact text
```