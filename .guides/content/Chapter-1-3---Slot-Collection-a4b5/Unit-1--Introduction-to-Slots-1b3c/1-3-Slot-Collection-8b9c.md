When a flow has a `collect:` step:

- **If slot is empty**: Agent asks for it (using `utter_ask_*` response)
- **If slot has value**: Flow continues immediately (no asking)
- **User provides value**: Agent stores it in the slot

## Example Flow


steps:
  - collect: account        # Step 1: Get account number
    description: "account number"
  - action: action_check_balance_simple  # Step 2: Use it

**What happens**:
1. Flow starts
2. Agent checks: Does `account` slot have a value?
   - **No** → Agent asks: "What is your account number?" (using `utter_ask_account`)
   - **Yes** → Skip to step 2
3. User provides account number
4. Agent stores it in `account` slot
5. Flow continues to step 2
6. Action reads `account` slot and uses it
