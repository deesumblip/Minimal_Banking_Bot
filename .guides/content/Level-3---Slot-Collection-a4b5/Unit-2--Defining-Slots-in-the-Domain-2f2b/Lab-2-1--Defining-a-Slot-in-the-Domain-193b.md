`domain/basics.yml` is where Rasa resolves every slot, response, and action name at runtime. This lab adds the three entries the check-balance flow depends on: the `account` slot, its ask and invalid-input responses, and the two action names.

## Instructions

Open `level3/domain/basics.yml`. The starter file already lists `action_bank_hours` and `action_holiday_hours` under `actions:`.

**Step 1.** Add the `slots:` block before `responses:`.

```yaml
slots:
  account:
    type: text
```

**Step 2.** Add both ask responses under `responses:`.

```yaml
  utter_ask_account:
    - text: "Can you provide your account number?"
      metadata:
        rephrase: True

  utter_invalid_account:
    - text: "Please enter a numeric account number."
      metadata:
        rephrase: True
```

Rasa sends `utter_ask_account` when the `account` slot is empty at a `collect` step. `rephrase: True` allows the LLM to reword the prompt to fit the conversation context. `utter_invalid_account` is sent when a flow-level rejection rejects the collected value.

**Step 3.** Add `action_check_balance_simple` to the `actions:` list, keeping the two actions already there.

```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
  - action_check_balance_simple
```

## Verify

Your `domain/basics.yml` should now contain:

- A `slots:` section with `account` of type `text` and mapping `from_llm`
- `utter_ask_account` with `rephrase: True`
- `utter_invalid_account` as a plain text response
- `action_bank_hours`, `action_holiday_hours`, and `action_check_balance_simple` under `actions:`

Use **Check It!** below to confirm.
 
{Check It!|assessment}(code-output-compare-3187585640)
 
