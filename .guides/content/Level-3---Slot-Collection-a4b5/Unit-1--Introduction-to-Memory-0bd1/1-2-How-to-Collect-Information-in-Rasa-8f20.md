Every slot follows three steps.

**Define** it in `domain/*.yml`:

```yaml
slots:
  account:
    type: text
    mappings:
      - type: from_llm
```

**Collect** it in a flow using a `collect:` step. When the flow reaches this step, Rasa checks whether the slot already has a value. If it does, the step is skipped. If it does not, Rasa sends the matching `utter_ask_<slot_name>` response, waits for a reply, and stores the extracted value.

```yaml
steps:
  - collect: account
  - action: action_check_balance_simple
```

**Read** it in a custom action via the tracker:

```python
account = tracker.get_slot("account")
```

In Level 3 you use all three steps. The labs follow this order: domain first, action second, flow last.

