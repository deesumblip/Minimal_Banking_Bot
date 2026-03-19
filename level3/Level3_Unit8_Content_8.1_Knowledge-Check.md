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

**6. A flow reaches `collect: account`, but the `account` slot already has a value from earlier in the conversation. What happens next?**

a) The bot skips asking and continues to the next step in the flow, using the existing slot value  
b) The bot always asks again for the account number before continuing  
c) The bot clears the slot and ends the conversation  
d) The flow stops and never runs the action that comes after the collect step  

---

## Answer Key

| Question | Answer | Brief explanation |
|----------|--------|-------------------|
| 1 | **b** | A slot is the bot's memory: it stores information from the conversation. |
| 2 | **c** | Slots are defined in the domain file under the top-level `slots:` section. |
| 3 | **b** | The `collect:` step tells Rasa to get the slot value; if empty, the bot asks (using the `utter_ask_*` response) and stores the answer. |
| 4 | **b** | In an action, you read a slot from the `tracker`: `tracker.get_slot("slot_name")`. |
| 5 | **b** | The convention is `utter_ask_<slot_name>`; for the `account` slot you use `utter_ask_account`. |
| 6 | **a** | Rasa only prompts when the slot is empty; if a value is already set, the collect step continues without re-asking. |

---

## Codio guide — Check It! tags

The Chapter 1.3 page `.guides/content/Chapter-1-3---Slot-Collection-a4b5/Unit-8--Assessment-and-Next-Steps-6d7e/8-1-Knowledge-Check-a6b7.md` uses these assessments (in order):

```
{Check It!|assessment}(multiple-choice-2551391875)
{Check It!|assessment}(multiple-choice-2502214147)
{Check It!|assessment}(multiple-choice-932698064)
{Check It!|assessment}(multiple-choice-2132752574)
{Check It!|assessment}(multiple-choice-5130520013)
```
