In Level 3 you read one slot in `action_check_balance_simple` with `tracker.get_slot("account")`. In Level 4 you will read **three** slots in `action_process_transfer`.

## Reading Multiple Slots in the Action

Inside `run()` of your action you can read each slot the same way:

```python
amount = tracker.get_slot("amount") or ""
recipient = tracker.get_slot("recipient") or ""
account_from = tracker.get_slot("account_from") or ""
```

The flow will have collected these before the action runs (or the slots may be empty/placeholder if the LLM filled them with generic text). Your action can:

- Check that all three have real values (not empty or placeholder).
- If any are missing or placeholder, send one message asking for real values and `return []`.
- Otherwise, send a confirmation message that uses amount, account_from, and recipient (e.g. "Transfer of $X from account Y to Z processed.") and `return []`.

## Lab 4.2

In **Lab 4.2** you will create `level4/actions/action_process_transfer.py` with this logic. You can use the fill-in-the-blanks script in the lab to complete the action, then paste it into the file and run the assessment.
