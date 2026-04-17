**Unit 3** starts here. In **Unit 2.1** you already walked through the full **`action_bank_hours.py`** example (imports, class, `name()`, `run()`, `dispatcher.utter_message`, `return []`). This lab applies that same pattern to a new file: **`action_holiday_hours`**, with date logic for holidays instead of weekdays. At the **end of this page**, a short section summarizes what Rasa does when it runs your action. Next you will register the action (**Lab 4.1**) and add a flow (**Lab 5.1**).

---

### Your Task

Create **`action_holiday_hours`**: the bank's holiday schedule **based on today's date**. If today is a holiday, say we're closed today. Otherwise return the general holiday schedule. That requires an action, not a single `utter_*` response.

You do **not** need to activate the virtual environment for the assessments below. **Check It!** checks your saved file on disk (and the fill-in exercise). Keep **`action_bank_hours.py`** open on the right if you want to compare while you work.

---

#### Complete the action file (fill in the blanks)

The exercise matches the **`action_bank_hours`** structure from **Unit 2.1**. Imports, class, `name()`, `run()` return type, `datetime.now()`, holiday date checks, `dispatcher.utter_message`, and `return []`. **Thirteen blanks** cover those pieces. Complete every blank, then **copy the full script** from the exercise into `level2/actions/action_holiday_hours.py`. Run the **Code Test** when the file is saved.

{Check It!|assessment}(fill-in-the-blanks-201030010)

---

### After you complete the blanks

1. **Open** `level2/actions/` in the file tree and **create** a new file named **`action_holiday_hours.py`** (if it does not exist yet).
2. **Paste** your completed script from the exercise above so the file matches your answers (all blanks filled).
3. **Save** the file.

---

### Run the code assessment

The grader checks that the file exists, has the right structure, imports, `datetime`-based logic, `ActionHolidayHours`, `name()`, and `run()` as described in the lab.

{Check It!|assessment}(code-output-compare-2266471391)

---

### Quick checklist

Before the Code Test, confirm your pasted file matches what you submitted in the fill-in exercise:

- File is under **`level2/actions/`** and named **`action_holiday_hours.py`**
- You import **`datetime`** and use it, for example **`datetime.now()`**, to choose the message
- Class is **`ActionHolidayHours(Action)`**
- **`name()`** returns **`"action_holiday_hours"`**
- **`run()`** calls **`dispatcher.utter_message()`** and returns **`[]`**

---

### When Rasa executes your action

When Rasa executes your action:

1. **Rasa finds the action**: Looks for the action in the `actions/` folder
2. **Rasa instantiates the class**: Creates an instance of your action class
3. **Rasa calls `name()`**: Verifies the action name matches what's registered
4. **Rasa calls `run()`**: Executes your custom code
5. **Your code runs**: Python executes your logic
6. **Message is sent**: `dispatcher.utter_message()` sends text to the user
7. **Action completes**: Returns empty list `[]`

**Key Point**: Rasa handles all the infrastructure, you just write the `run()` method with your logic.

---
