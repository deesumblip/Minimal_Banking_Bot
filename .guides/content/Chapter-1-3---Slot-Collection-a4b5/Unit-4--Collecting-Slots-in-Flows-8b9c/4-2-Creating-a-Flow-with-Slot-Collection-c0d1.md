You've seen the syntax. Here's what actually happens when the flow runs.

**When the flow runs**

1. Flow starts at Step 1, `collect: account`.
2. Rasa checks whether the `account` slot already has a value.
   - **No.** The bot asks for it using `utter_ask_account`, for example "What is your account number?" The user replies, Rasa stores the value in the slot, and the flow continues to Step 2.
   - **Yes.** The bot skips asking and uses the existing value, then continues to Step 2.
3. Step 2. `action_check_balance_simple` runs and reads the slot.

The bot only asks when the slot is empty. If the slot already has a value, for example from an earlier turn in the conversation, Rasa uses that value immediately.
