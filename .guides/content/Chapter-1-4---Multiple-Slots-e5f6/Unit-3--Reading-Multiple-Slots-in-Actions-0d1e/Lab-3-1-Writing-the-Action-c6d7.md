In this lab you finish the action that **Lab 2.1** already registered in the domain. You will create `action_process_transfer.py`. The action reads the `amount`, `recipient`, and `account_from` slots and handles placeholder values, as you saw in **Unit 3.1** (*Example: Complete action class*).

---

#### Complete the action file (fill in the blanks)

The exercise uses the same pieces you saw in Level 2 in *The Action Class Deep Dive*, in Chapter 1.3 in **Lab 4.1** (`action_check_balance_simple`), and in this chapter in **Unit 3.1** (reading multiple slots with `tracker.get_slot(...)`). Complete every blank, then **copy the full script** into `level4/actions/action_process_transfer.py` using the steps below. Run the **Code Test** when the file is saved.

{Check It!|assessment}(fill-in-the-blanks-401030010)

---

### After you complete the blanks

1. **Open** `level4/actions/action_process_transfer.py` in the file tree (create the `actions` folder under `level4` if needed).
2. **Paste** your completed script from the exercise above so the file matches your answers (all blanks filled).
3. **Save** the file.

---

### Run the code assessment

The grader checks that the file exists, has the right structure, reads the `amount`, `recipient`, and `account_from` slots with `get_slot`, and sends a transfer-related confirmation message.

{Check It!|assessment}(code-output-compare-401030001)

---

### Optional

After Lab 5.1, train and run Inspector. Trigger the transfer flow and provide amount, recipient, and source account; watch the action send the confirmation.

**Instructor answer key** (blanks and full script): `level4/Level4_Lab3.1_Assessment_Setup.md` and `level4/Level4_Lab3.1_Content.md`.
