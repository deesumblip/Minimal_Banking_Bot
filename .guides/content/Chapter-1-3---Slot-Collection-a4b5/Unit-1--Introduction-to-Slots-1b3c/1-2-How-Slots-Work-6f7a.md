Slots work in three steps:

1. **Define the slot** in `domain/basics.yml`:
   ```yaml
   slots:
     account:
       type: text
   ```

2. **Collect the slot** in a flow:
   ```yaml
   steps:
     - collect: account
       description: "account number"
   ```

3. **Read the slot** in an action:
   ```python
   account = tracker.get_slot("account")
   ```

These three steps—define, collect, read—are the core of slot-based memory in Level 3.
