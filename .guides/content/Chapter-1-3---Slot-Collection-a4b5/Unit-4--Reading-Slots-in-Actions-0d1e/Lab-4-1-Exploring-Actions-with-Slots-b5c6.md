Your goal is to **complete** the action file that reads the `account` slot and handles placeholder values. The domain already lists `action_check_balance_simple` from Lab 3.1.

---

#### Complete the action file (fill in the blanks)

Use the same structure you learned in Level 2 (`Action`, `name()`, `run()`, `CollectingDispatcher`) and Chapter 1.3 (`tracker.get_slot`, placeholders, `utter_ask_*` responses). When every blank is correct, **copy the full completed script** into `level3/actions/action_check_balance_simple.py` (see steps below), then run the **Code Test**.

{Check It!|assessment}(fill-in-the-blanks-2346557111)

---

### After you complete the blanks

1. **Open** `level3/actions/action_check_balance_simple.py` in the file tree (create the file if needed).
2. **Paste** your completed script from the exercise above so the file matches your answers (all blanks filled).
3. **Save** the file.

---

### Run the code assessment

The grader checks that the file exists, has the right structure, reads the `account` slot, handles placeholders, re-prompts with `utter_ask_account`, and sends a balance message.

{Check It!|assessment}(code-output-compare-2346557110)

---

### Optional

After Lab 6.1, train and run Inspector. Trigger the check_balance flow and watch the action use the slot and re-ask when the LLM extracts a placeholder.

**Instructor answer key** (blanks and full script): `level3/Level3_Lab4.1_Assessment_Setup.md`.
