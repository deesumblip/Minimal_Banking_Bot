# Lab 4.1: Writing the Action That Uses the Slot

Your goal is to **create** the action file that reads the `account` slot and handles placeholder values. The domain already lists `action_check_balance_simple` from Lab 3.1; here you write the Python file so the action exists.

---

## Steps

1. **Create** the file `level3/actions/action_check_balance_simple.py` in your project (if a file with this name exists from an older version, replace it or follow the steps below so the content matches).

2. **Add imports** at the top:
   - From `typing`: `Any`, `Dict`, `List`, `Text`
   - From `rasa_sdk`: `Action`, `Tracker`, `CollectingDispatcher`

3. **Define the class** `ActionCheckBalanceSimple(Action)` with:
   - **`name(self)`** – return the string `"action_check_balance_simple"`.
   - **`run(self, dispatcher, tracker, domain)`** – implement:
     - Read the slot: `account = tracker.get_slot("account") or "<missing>"`.
     - Define a list of placeholder values, e.g. `["account number", "user_account_number", "<missing>"]`.
     - If `account` (lowercased) is in that list: call `dispatcher.utter_message(response="utter_ask_account")` and `return []`.
     - Otherwise: call `dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")` and `return []`.

4. **Verify** the file is in `level3/actions/` and that your domain (from Lab 3.1) already lists `action_check_balance_simple` in the `actions:` section.

5. **Optional.** After Lab 6.1, train and run Inspector. Trigger the check_balance flow and watch the action use the slot and re-ask when the LLM extracts a placeholder.

You're done when the action file exists, reads the slot, handles placeholders by re-prompting with `utter_ask_account`, and otherwise shows the demo balance message. This lab has no graded assessment.

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
b) To detect values that are not real account numbers so the bot can re-ask  
c) To define the slot type in the domain  
d) To set default values when the slot is empty  

---

### Answer Key

| Q | Answer | Brief explanation |
|---|--------|-------------------|
| 1 | **b** | The action uses `tracker.get_slot("account")` to read the slot from conversation memory. |
| 2 | **b** | Placeholder values trigger a re-prompt with `utter_ask_account`; the action returns without showing a balance. |
| 3 | **b** | `placeholder_values` lists strings that the LLM might incorrectly extract instead of a real account number; the action checks for these to re-ask. |
