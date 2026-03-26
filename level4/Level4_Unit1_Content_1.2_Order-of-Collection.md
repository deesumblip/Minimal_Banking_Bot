**Starting point:** Chapter 1.4 assumes you begin with the **final banking agent at the end of Chapter 1.3** (your **`level3/`** project). You **add** work in **`level4/`**—see **Unit 0.1** and **Unit 0.2**.

The order of `collect:` steps in the flow is the order in which the agent asks for values when a slot is still empty.

## Flow steps define the order

In `transfer_money.yml` you will add steps like this:

```yaml
steps:
  - collect: amount        # asks first (utter_ask_amount)
  - collect: recipient     # then utter_ask_recipient
  - collect: account_from  # then utter_ask_account_from
  - action: action_process_transfer
```

Rasa walks the list in order. Match the sequence to what makes sense for the user (for example amount → recipient → source account) and to what your action reads (`amount`, `recipient`, `account_from`).

## Same Convention as Level 3

- Each collected slot needs a matching **response** in the domain: `utter_ask_<slot_name>` (e.g. `utter_ask_amount` for the `amount` slot).
- The action runs only after all collected slots have values (or after the user has been asked for each one in order).

In Lab 4.1 you will create the flow with the three collect steps in this order, then the action step.
