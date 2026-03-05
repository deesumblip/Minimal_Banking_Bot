# Lab 5.2: Testing / Completion Check - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Lab 5.1, Level 5.

**Task.** Run a completion check: verify tools folder, endpoints tools section, transfer_money_tools flow, action_process_transfer_with_tools action and domain registration, and (optionally) trained model. Run the assessment when done.

**Codio guide (Chapter 1.5).** The Lab 5.2 page in the Chapter 1.5 guide includes: `{Check It!|assessment}(code-output-compare-501050002)`. Assessment JSON: `.guides/assessments/code-output-compare-501050002.json`.

---

## Assessment Setup (For Implementers)

### Overview

Verifies all Level 5 artifacts: level5/tools/ and banking_tools.py with __all__; level5/endpoints.yml tools section; level5/data/basics/transfer_money_tools.yml; level5/actions/action_process_transfer_with_tools.py; level5/domain/basics.yml with action in actions list; optionally level5/models/ or successful train.

### Assessment Type

**Code Test**.

### Code Test

Grader: `.guides/secure/level5_graders/lab_5.2_grader.py`. Checks all of the above. On full pass print `PASS`. COMMAND: `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level5_graders/lab_5.2_grader.py`. WD: `/home/codio/workspace`. Expected: `PASS`.
