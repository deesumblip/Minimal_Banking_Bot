 Level 3 built an agent that collects one value, `account`, and passes it to an action. Level 4 extends that pattern to flows that collect several values before running an action.
 
You will build a money transfer flow. It needs three pieces of information: the account number, how much to transfer, and who to send it to. The `account` slot already exists from Level 3. You add `amount` and `recipient`. If the user already checked their balance in the same session, the transfer flow skips asking for the account number because the slot is already set.
 
## What you add in Level 4
 
| File | What changes |
|---|---|
`domain/basics.yml` | Two new slots, two new ask responses, one new action name |
`actions/action_process_transfer.py` | Action that reads all three slots |
`data/basics/transfer_money.yml` | Flow with three collect steps |
`models/` | Trained model |
 Inspector | End-to-end transfer test |
 
Your Level 3 work stays in place, and you can add the transfer pieces on top.
 
