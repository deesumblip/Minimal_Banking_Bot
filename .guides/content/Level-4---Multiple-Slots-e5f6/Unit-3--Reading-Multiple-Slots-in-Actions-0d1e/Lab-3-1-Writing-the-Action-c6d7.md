Now that we have registered everything in the domain, we need to create the file, `actions/action_process_transfer.py` so that we can send all the values we collect from the user (account number, transfer recipient, and amount) to the backend system. 


---
#### Complete the action file (fill in the blanks)

The exercise uses the same pieces you saw in *The Action Class Deep Dive*, and allows you to build the custom action that will leverage the information you set in the slots to complete a money transfer flow. 

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

