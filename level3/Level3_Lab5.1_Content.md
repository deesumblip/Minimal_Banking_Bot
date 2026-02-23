# Lab 5.1: Exploring Actions with Slots

Your goal is to see how the provided action uses the `account` slot and handles placeholders.

The action file `action_check_balance_simple.py` is already in `level3/actions/`. You are not writing code. You are exploring how it works.

---

## Steps

1. **Open** `level3/actions/action_check_balance_simple.py` in your editor.

2. **Find** where it reads the slot (for example `account = tracker.get_slot("account")` or similar).

3. **Find** where it checks for placeholders (for example "account number" or "<missing>") and re-prompts with `utter_ask_account` when the value is not real.

4. **Optional.** After Lab 6.1, train and run Inspector. Trigger the check_balance flow and watch the action use the slot and re-ask when the LLM extracts a placeholder.

You're done when you understand how the action reads the slot and handles missing or placeholder values. This lab has no graded assessment.

---

## Check Your Knowledge

**1. How does the action read the account slot?**

a) `account = domain.get_slot("account")`  
b) `account = tracker.get_slot("account")`  
c) `account = dispatcher.get_slot("account")`  
d) `account = flow.collect("account")`  

**2. When the slot contains "account number" or "<missing>", what does the action do?**

a) Uses it as the account number and shows a balance  
b) Re-prompts with `utter_ask_account` and does not show a balance  
c) Returns an error and crashes  
d) Ignores it and continues to the next step  

**3. What is the purpose of the `placeholder_values` list?**

a) To store valid account numbers for testing  
b) To detect values that are not real account numbers (so the bot can re-ask)  
c) To define the slot type in the domain  
d) To set default values when the slot is empty  

---

### Answer Key

| Q | Answer | Brief explanation |
|---|--------|-------------------|
| 1 | **b** | The action uses `tracker.get_slot("account")` to read the slot from conversation memory. |
| 2 | **b** | Placeholder values trigger a re-prompt with `utter_ask_account`; the action returns without showing a balance. |
| 3 | **b** | `placeholder_values` lists strings that the LLM might incorrectly extract instead of a real account number; the action checks for these to re-ask. |
