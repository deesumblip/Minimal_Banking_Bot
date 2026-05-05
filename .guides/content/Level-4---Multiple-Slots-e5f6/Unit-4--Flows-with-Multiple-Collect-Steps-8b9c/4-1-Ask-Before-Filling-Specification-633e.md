All three flows you have built so far share a pattern: Rasa fills a slot the moment it sees a valid value, even if the user mentioned it before the flow started. Say "send $50 to Jen" and both `amount` and `recipient` are filled before the first question is asked. That is the default, and for many slots it is the right call.

There is one wrinkle in this unit. The `check_balance` flow uses `persisted_slots`:

```yaml
flows:
  check_balance:
    persisted_slots:
      - account
    steps:
      - collect: account
```

`persisted_slots` tells Rasa to keep the slot value after the flow ends. This allowed us to demonstrate how Rasa can save values and reuse them later in the conversation.

But it creates a risk. If we reuse the `account` slot and is already set from a previous flow, the `collect` step in `transfer_money` would be skipped entirely, and whatever value was stored would go straight to the transfer action. For a slot that feeds a financial transaction, silently reusing a value is not acceptable.

`ask_before_filling: true` fixes this. Rasa will always pause and ask, even if the slot already has a value.

```yaml
- collect: account
  ask_before_filling: true
```

Use it sparingly, asking when you could infer adds friction. But when a persisted slot could cause a silent wrong answer, it is the right call.

In the next lab you write the full flow.