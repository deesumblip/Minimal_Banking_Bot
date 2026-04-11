In this lab you finish the action that Lab 3.1 already registered in the domain. You will create `action_check_balance_simple.py`. The action reads the `account` slot and handles placeholder values, as you saw in Unit 4.2.

---

#### Complete the action file (fill in the blanks)

The exercise uses the same pieces you saw in Level 2 in *The Action Class Deep Dive* and in this chapter in Units 4.1 and 4.2. Complete every blank, then **copy the full script** into `level3/actions/action_check_balance_simple.py` using the steps below. Run the **Code Test** when the file is saved.

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
