- Flow starts → Step 1: `collect: account`
- Does `account` slot have a value?
  - **No** → Bot asks: "What is your account number?" → User provides → Bot stores value in slot → Flow continues to Step 2
  - **Yes** → Skip asking; use existing value → Flow continues to Step 2
- Step 2: `action_check_balance_simple` runs and reads the slot.

**Key point**: The bot only asks if the slot is empty. If it already has a value, it uses that value immediately.
