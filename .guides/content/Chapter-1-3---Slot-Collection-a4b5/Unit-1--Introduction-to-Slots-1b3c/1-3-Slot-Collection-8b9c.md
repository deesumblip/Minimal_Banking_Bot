# 1.3 Slot Collection

When a flow has a `collect:` step:

- **If slot is empty**: Bot asks for it (using `utter_ask_*` response)
- **If slot has value**: Flow continues immediately (no asking)
- **User provides value**: Bot stores it in the slot

## Example Flow

```yaml
steps:
  - collect: account        # Step 1: Get account number
    description: "account number"
  - action: action_check_balance_simple  # Step 2: Use it
```

**What happens**:
1. Flow starts
2. Bot checks: Does `account` slot have a value?
   - **No** → Bot asks: "What is your account number?" (using `utter_ask_account`)
   - **Yes** → Skip to step 2
3. User provides account number
4. Bot stores it in `account` slot
5. Flow continues to step 2
6. Action reads `account` slot and uses it
