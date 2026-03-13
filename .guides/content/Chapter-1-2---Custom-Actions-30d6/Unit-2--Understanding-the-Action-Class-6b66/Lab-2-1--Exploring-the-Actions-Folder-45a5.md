**Placement**: This lab comes right after Unit 2 Test Your Knowledge. You should understand that every action is a Python class that inherits from `Action`, with required methods `name()` and `run()`.

---

#### Complete the action file (fill in the blanks)

Fill in the blanks to complete a **branch address** action that returns the bank's main branch address and the current day (e.g. "Our main branch is at 123 High Street. Today is Mon."). Because the message changes with the day, it must be an action—not a static `utter_` response. The structure is the same as the bank hours action: class name, `name()`, `run()` with `dispatcher`, `tracker`, `domain`, and sending a message.

{Check It!|assessment}(fill-in-the-blanks-1202100001)

---

### Your Task

Explore the `level2` folder, focusing on the `actions/` subfolder. Use the file tree and open the files to see how the structure you learned is implemented in code.

**What to do:**
1. Navigate to the `level2` folder in your workspace
2. Expand the `actions/` folder in the file tree
3. Open `actions/__init__.py` and `actions/action_bank_hours.py`
4. Read the code and compare it to the basic structure you learned
5. Answer the assessment questions below

---

### What You're Looking For

- **`actions/` folder** – Where all custom action files live
- **`__init__.py`** – Makes the folder a Python package so Rasa can find your actions
- **`action_bank_hours.py`** – An example action: imports (including `datetime`), class, `name()`, `run()` with conditional logic

Use what you see to answer the questions.

{Check It!|assessment}(multiple-choice-2271484345)
{Check It!|assessment}(multiple-choice-2658905164)
{Check It!|assessment}(multiple-choice-2658905165)
{Check It!|assessment}(multiple-choice-2658905166)
{Check It!|assessment}(multiple-choice-1522273536)
{Check It!|assessment}(multiple-choice-2658905167)

{Check It!|assessment}(fill-in-the-blanks-2658905168)
{Check It!|assessment}(fill-in-the-blanks-2658905169)
{Check It!|assessment}(fill-in-the-blanks-2658905170)
{Check It!|assessment}(fill-in-the-blanks-341339148)
{Check It!|assessment}(fill-in-the-blanks-235818681)
