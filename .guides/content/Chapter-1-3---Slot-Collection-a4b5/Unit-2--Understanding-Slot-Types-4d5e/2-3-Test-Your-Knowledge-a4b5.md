Answer the following to check your understanding of Level 3 so far (Units 0–2).

---

**1. What is a slot?**

a) A flow step that asks the user for information  
b) A memory variable that stores information from the conversation  
c) A type of response the bot can say  
d) A Python function that runs during the conversation  

**2. When a flow has a `collect: account` step and the `account` slot is empty, what does the bot do?**

a) Skips the step and continues to the next step  
b) Asks the user for the value (using the `utter_ask_account` response) and stores it in the slot  
c) Reads the slot from the tracker  
d) Deletes the slot value  

**3. In Level 3, which slot type do we use in the domain, and which of these is a good slot name?**

a) Type: `bool`, good name: `slot1`  
b) Type: `text`, good name: `account`  
c) Type: `list`, good name: `a`  
d) Type: `text`, good name: `data`  

---

## Answer Key

| Question | Answer | Brief explanation |
|----------|--------|-------------------|
| 1 | **b** | A slot is the bot's memory: it stores information from the conversation. |
| 2 | **b** | The `collect:` step gets the slot value; if empty, the bot asks using `utter_ask_*` and stores the answer. |
| 3 | **b** | We use `text` slots in Level 3. Good names are descriptive and lowercase (e.g. `account`); avoid vague names like `a`, `slot1`, or `data`. |
