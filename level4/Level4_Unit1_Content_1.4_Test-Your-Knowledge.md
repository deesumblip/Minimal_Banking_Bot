Answer the following to check your understanding of Level 4 so far (Units 0–1).

---

**1. What do we mean by "multiple slots" in Level 4?**

a) Multiple flows that each collect one slot  
b) Several memory variables (e.g. amount, recipient, account_from) that the bot can collect and use together in one flow  
c) Multiple actions that each read one slot  
d) Several response messages for the same slot  

**2. Why does the order of `collect:` steps in a flow matter?**

a) It doesn't; Rasa ignores the order  
b) The order is the order in which the bot will ask the user for each value  
c) Only the first collect step runs  
d) The order must match the alphabetical order of slot names  

**3. What naming convention do we use for the response that asks for a slot value?**

a) `response_<slot_name>`  
b) `utter_ask_<slot_name>`  
c) `ask_<slot_name>`  
d) `slot_<slot_name>`  

**4. For the transfer flow, which slots do we collect before running the action?**

a) Only `account`  
b) `amount`, `recipient`, and `account_from`  
c) `from_account` and `to_account`  
d) Any three slots the student chooses  

---

## Answer Key

| Question | Answer | Brief explanation |
|----------|--------|-------------------|
| 1 | **b** | Multiple slots are several memory variables the bot collects in one conversation and can use together (e.g. in one action). |
| 2 | **b** | The order of `collect:` steps is the order in which the bot prompts for each slot value. |
| 3 | **b** | We use `utter_ask_<slot_name>` (e.g. `utter_ask_amount`, `utter_ask_recipient`). |
| 4 | **b** | The transfer flow collects `amount`, `recipient`, and `account_from` before running action_process_transfer. |
