When a flow has a `collect:` step:

- **If slot is empty**: Agent asks for it (using `utter_ask_*` response)
- **If slot has value**: Flow continues immediately (no asking)
- **User provides value**: Agent stores it in the slot

## Example Flow

```yaml
steps:
  - collect: account        # Step 1: Get account number
    description: "account number"
  - action: action_check_balance_simple  # Step 2: Use it
```

**What happens**:

1. Flow starts.
2. The agent checks whether the `account` slot has a value.
 - **No.** The agent asks using the `utter_ask_account` response, for example "What is your account number?" After the user replies, Rasa stores the value and the flow continues.
 - **Yes.** The agent skips asking and continues.
3. The user may provide or confirm the account number. Rasa keeps the slot updated as needed.
4. The flow continues to the action step.
5. The action reads the `account` slot and uses it.

For the **`collect:`** syntax used in YAML, see **5.1 The Collect Step** in this chapter.
