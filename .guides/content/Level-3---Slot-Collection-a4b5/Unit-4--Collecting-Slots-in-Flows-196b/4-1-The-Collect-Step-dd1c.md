A `collect:` step pauses the flow and asks the user for a slot value. When the step runs, Rasa sends `utter_ask_<slot_name>` and waits. The LLM reads the user's reply, extracts the value, and stores it in the slot. The flow then moves to the next step.

If the slot already has a value when the step is reached, it is skipped entirely.

## Guiding the LLM with description

The slot `description` field tells the LLM what a valid value looks like for this slot. It is included in the LLM prompt at the point of collection.

Without it, the LLM guesses from the slot name alone. A slot named `account` might cause the LLM to accept the phrase `"account number"` — a label, not an actual number.

```yaml
- collect: account
  description: |
          A numeric account number consisting ONLY of digits (e.g., 123456, 987654321).
          CRITICAL: Do NOT extract this slot unless the user explicitly provides numbers.
          Do NOT extract from phrases like "account balance", "check account", "my account".
          Only extract when the user says actual digits like "123456" or "my account number is 789012".
```

The description gives the LLM specific instructions: digits only, at least four of them, nothing else. The more specific the description, the more reliably the LLM extracts the right kind of value.

## Catching bad values with rejections

The LLM can still extract a value that doesn't meet your requirements. A `rejections` block is a second check that runs after extraction, on the collected value itself. Slot rejections are useful for simple scenarios like this one, where you need to check if an account number fits a specific pattern. 

Each rejection has two fields:

- `if`: a condition on the slot value. This can be for example a regex. 
- `utter`: the response to send if the condition is true

When a rejection fires, Rasa sends the `utter` response, clears the slot, and repeats the collect step from the beginning. The user sees the rejection message, then `utter_ask_account` again. If no rejection fires, the slot is set and the flow continues. You can use an action to validate for more complex scenarios.

```yaml
- collect: account
  description: |
          A numeric account number consisting ONLY of digits (e.g., 123456, 987654321).
          CRITICAL: Do NOT extract this slot unless the user explicitly provides numbers.
          Do NOT extract from phrases like "account balance", "check account", "my account".
          Only extract when the user says actual digits like "123456" or "my account number is 789012".
  rejections:
    - if: not (slots.account matches "^[0-9]{4,}$")
      utter: utter_invalid_account
```

This condition rejects any value that is not a string of four or more digits. `"account number"`, `"abc123"`, and `"12"` all fail. `"48291"` passes.



{Check It!|assessment}(multiple-choice-2502214147)
{Check It!|assessment}(fill-in-the-blanks-1454903744)
---

