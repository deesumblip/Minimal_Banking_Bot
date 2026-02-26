# Lab 4.5: Testing the Transfer Flow - Completion Check - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 6: Training and Testing (Level 4), after Lab 4.4.

**Task.** Start your Level 4 bot (e.g. `rasa run` or use the Rasa Inspect tab), open Rasa Inspector, and run through the transfer flow: trigger the transfer intent, provide amount, recipient, and source account when asked, and confirm you see the transfer confirmation from `action_process_transfer`. The completion check verifies that your Level 4 bot has all required pieces in place so the transfer flow can run (domain, action file, flow file, and a trained model).

Run the assessment when you've verified the transfer flow works (or when you've completed the setup).

---

## Assessment Setup (For Implementers)

### Overview

This is a **completion check** (not a full run of the bot in Inspector). The grader verifies that the student has completed the full Level 4 build: (1) domain has the three transfer slots and three ask responses and action_process_transfer, (2) action_process_transfer.py exists and reads the three slots, (3) transfer_money.yml exists with the three collect steps and action step, (4) a model file exists in level4/models/. Together these indicate the student can run and test the transfer flow. No LLM or live Rasa run is required.

### Assessment Type

**Standard Code Test** (Python script)

### Grader Script Location

```
.guides/assessments/level4_graders/lab_4.5_grader.py
```

### Grader Script

The grader runs from **workspace root** (`/home/codio/workspace`). It performs the following checks (all file/structure based):

1. **Domain** (3 pts): `level4/domain/basics.yml` has slots amount, recipient, account_from; responses utter_ask_amount, utter_ask_recipient, utter_ask_account_from; action_process_transfer in actions list.
2. **Action file** (3 pts): `level4/actions/action_process_transfer.py` exists and contains get_slot for "amount", "recipient", "account_from" and name() returning "action_process_transfer".
3. **Flow file** (2 pts): `level4/data/basics/transfer_money.yml` exists with valid YAML, collect amount/recipient/account_from, and action action_process_transfer.
4. **Model** (2 pts): at least one `.tar.gz` in `level4/models/`.

**Total: 10 points.** Script prints `PASS` and `Successfully passed!` on full success; otherwise `FAIL` and exit 1. This allows every Level 4 lab to be evaluated without requiring a live Inspector session.

### Codio configuration (Standard Code Test)

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/assessments/level4_graders/lab_4.5_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty**.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **10**. Enable **Allow partial points** if desired.
   - **Test case:** One test case. **EXPECTED OUTPUT:** `PASS`. **Enable substring match**.
   - **SHOW RATIONALE TO STUDENT:** **AFTER [1] ATTEMPTS** (or **ALWAYS**).
   - **RATIONALE:** The completion check verifies that your Level 4 bot has: the domain updated with transfer slots and ask responses and action_process_transfer, the action file that reads the three slots, the transfer_money flow file, and a trained model. If any check fails, complete the corresponding lab (4.1–4.4) and re-run training if needed, then run this assessment again.
4. **Files.** Script at `.guides/assessments/level4_graders/lab_4.5_grader.py`; run from workspace.

---

## Reference for rubric / grading

- **Solution reference:** `.guides/assessments/level4_graders/lab_4.5_solution_reference.md` (describes what “completion” means for each check).
