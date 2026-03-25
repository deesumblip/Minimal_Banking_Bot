**Starting point:** Chapter 1.4 assumes you began with the **final banking agent at the end of Chapter 1.3** and extended it in **`level4/`** (see **`Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md`**).

Answer the following to check your understanding of Level 4 (multiple slots).

---

**1. In Level 4, which slots do we add for the transfer flow?**

a) Only `account`  
b) `amount`, `recipient`, and `account_from`  
c) `transfer`, `money`, and `flow`  
d) `from_account` and `to_account`  

**2. What is the correct order of steps in the transfer_money flow?**

a) Action first, then collect steps  
b) Collect amount, then recipient, then account_from, then action_process_transfer  
c) Collect all three slots in any order in one step  
d) action_process_transfer, then collect amount, recipient, account_from  

**3. How does an action read multiple slots?**

a) `tracker.get_slots(["amount", "recipient", "account_from"])`  
b) `tracker.get_slot("amount")`, `tracker.get_slot("recipient")`, `tracker.get_slot("account_from")`  
c) `dispatcher.get_slot("amount")` for each slot  
d) Slots are read automatically from the flow  

**4. Why is the order of `collect:` steps in the flow important?**

a) It doesn't matter; Rasa collects them in any order  
b) The order determines the order in which the agent asks the user for each value  
c) The first collect step must always be amount  
d) Only the last collect step is used by the action  

**5. What must be in the domain for each new slot used in a flow?**

a) Only the slot name under `slots:`  
b) The slot under `slots:` and a corresponding `utter_ask_<slot_name>` under `responses:`  
c) The slot and an action that uses it  
d) Only the response; slots are optional  

---

## Answer Key

| Question | Answer | Brief explanation |
|----------|--------|-------------------|
| 1 | **b** | Level 4 adds `amount`, `recipient`, and `account_from` for the transfer flow. |
| 2 | **b** | The flow collects amount, then recipient, then account_from, then runs action_process_transfer. |
| 3 | **b** | You call `tracker.get_slot("slot_name")` once per slot in the action's `run()` method. |
| 4 | **b** | The order of `collect:` steps is the order in which the agent prompts the user for each value. |
| 5 | **b** | Each slot needs an entry under `slots:` and a matching `utter_ask_<slot_name>` under `responses:` so the agent can ask when the slot is empty. |
