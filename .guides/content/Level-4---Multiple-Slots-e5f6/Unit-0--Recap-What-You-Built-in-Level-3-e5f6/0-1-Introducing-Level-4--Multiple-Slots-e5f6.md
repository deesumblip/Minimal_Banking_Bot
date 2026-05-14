Level 3 built an agent that collects one value and passes it to an action. Level 4 extends that pattern to flows that collect several values before running an action.
 
You will build a money transfer flow that needs three pieces of information: the account number, the amount, and the recipient. The `account` slot already exists from Level 3. You add `amount` and `recipient`. If the user already checked their balance in the same session, the transfer flow skips asking for the account number because the slot is already set.
 
| File | What changes |
|---|---|
| `domain/basics.yml` | Two new slots, two new ask responses, one new action name |
| `actions/action_process_transfer.py` | Action that reads all three slots |
| `data/basics/transfer_money.yml` | Flow with three collect steps |
| `models/` | Trained model |
| Inspector | End-to-end transfer test |
  
---
 