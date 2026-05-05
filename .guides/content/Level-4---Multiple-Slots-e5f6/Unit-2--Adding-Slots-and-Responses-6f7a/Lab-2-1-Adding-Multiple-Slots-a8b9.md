 Similar to the prior level, we need to register slots and responses in the domain. Open `domain/basics.yml`. The `account` slot and `utter_ask_account` response are already there from Level 3. You are adding two new slots and two new responses on top.
 
**Step 1.** Add `amount` and `recipient` under the existing `slots:` block.
 
```yaml
  amount:
    type: text
  recipient:
    type: text
```
 
**Step 2.** Add two ask responses under `responses:`.
 
```yaml
  utter_ask_amount:
    - text: "How much would you like to transfer?"
      metadata:
        rephrase: False
 
  utter_ask_recipient:
    - text: "Who would you like to transfer money to?"
      metadata:
        rephrase: False
```
 
**Step 3.** Add `action_process_transfer` to the `actions:` list. Keep every action already there.
 
```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
  - action_check_balance_simple
  - action_process_transfer
```
 
**Check It!** below to confirm.
 

{Check It!|assessment}(code-output-compare-401020001)

#