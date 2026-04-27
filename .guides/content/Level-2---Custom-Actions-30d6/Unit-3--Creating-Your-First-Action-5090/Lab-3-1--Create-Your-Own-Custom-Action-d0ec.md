In this lab we will build out `action_holiday_hours`, a custom action that uses the same pattern as `action_bank_hours`. It checks today's date. If it's a public holiday, it tells the user the bank is closed; otherwise it returns the general holiday schedule. You build the action here, register it in Lab 4.1, and add a flow to activate it in Lab 5.1.

---

### Step 1: Fill in the blanks to create the action

Fill in the blanks for `action_holiday_hours` below. Take a look at the existing action, `action_bank_hours`, to get a sense of how the action should be written. 

{Check It!|assessment}(fill-in-the-blanks-201030010)

---

### Step 2: Add your completed action to a file

1. **Open** `level2/actions/` in the file tree and **create** a new file named **`action_holiday_hours.py`** (if it does not exist yet).
2. **Paste** your completed script from the exercise above so the file matches your answers (all blanks filled).
3. **Save** the file. 

---

### Run the code assessment

The grader checks that the file exists, has the right structure, imports, `datetime`-based logic, `ActionHolidayHours`, `name()`, and `run()` as described in the lab. 

{Check It!|assessment}(code-output-compare-2266471391)

---

### When Rasa executes your action

1. **Rasa finds the action**: Looks for the action in the `actions/` folder
2. **Rasa instantiates the class**: Creates an instance of your action class
3. **Rasa calls `name()`**: Verifies the action name matches what's registered
4. **Rasa calls `run()`**: Executes your custom code
5. **Your code runs**: Python executes your logic
6. **Message is sent**: `dispatcher.utter_message()` sends text to the user
7. **Action completes**: Returns empty list `[]`

**Key Point**: Rasa handles all the infrastructure, you just write the `run()` method with your logic.

---
