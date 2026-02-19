**Objective**: See how the provided action uses the `account` slot and handles placeholders.

**Note**: The action file `action_check_balance_simple.py` is already in `level3/actions/`. You are not writing code; you are exploring how it works.

---

## Steps

1. **Open** `level3/actions/action_check_balance_simple.py` in your editor.

2. **Find** where it reads the slot:  
   `account = tracker.get_slot("account")` (or similar).

3. **Find** where it checks for placeholders (e.g. "account number", "<missing>") and re-prompts with `utter_ask_account` when the value is not real.

4. **Optional**: After Lab 6.1, train and run Inspector. Trigger the check_balance flow and watch the action use the slot (and re-ask when the LLM extracts a placeholder).

**Success criteria**: You understand how the action reads the slot and handles missing/placeholder values. No graded assessment.
