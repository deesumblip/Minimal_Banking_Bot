# 8.1 Knowledge Check

Answer the following to check your understanding of Level 3 (slots).

---

**1. What is a slot?**

a) A flow step that asks the user for information  
b) A memory variable that stores information from the conversation  
c) A type of response the bot can say  
d) A Python function that runs during the conversation  

**2. Where are slots defined?**

a) In `data/basics/*.yml`  
b) In `config.yml`  
c) In `domain/basics.yml` under a `slots:` section  
d) In the actions Python files  

**3. What does a `collect:` step in a flow do?**

a) Sends the slot value to an action  
b) Tells Rasa to get the slot value from the user, asking with the `utter_ask_*` response when the slot is empty, before continuing  
c) Deletes the slot value  
d) Reads the slot value from the tracker  

**4. How do you read a slot in an action?**

a) `slot = domain.get_slot("account")`  
b) `account = tracker.get_slot("account")`  
c) `account = dispatcher.get_slot("account")`  
d) `account = flow.collect("account")`  

**5. What is the naming convention for the response used when asking for a slot value?**

a) `response_ask_<slot_name>`  
b) `utter_ask_<slot_name>`  
c) `ask_<slot_name>`  
d) `slot_<slot_name>_prompt`  

---

## Answer Key

| Question | Answer | Brief explanation |
|----------|--------|-------------------|
| 1 | **b** | A slot is the bot's memory: it stores information from the conversation. |
| 2 | **c** | Slots are defined in the domain file under the top-level `slots:` section. |
| 3 | **b** | The `collect:` step tells Rasa to get the slot value; if empty, the bot asks (using the `utter_ask_*` response) and stores the answer. |
| 4 | **b** | In an action, you read a slot from the `tracker`: `tracker.get_slot("slot_name")`. |
| 5 | **b** | The convention is `utter_ask_<slot_name>`; for the `account` slot you use `utter_ask_account`. |
