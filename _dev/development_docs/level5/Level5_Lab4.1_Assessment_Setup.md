# Lab 4.1: Creating the transfer_money_tools Flow and Action - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 4 (Using Tools in Conversations), Level 5.

**Task.** Create `level5/data/basics/transfer_money_tools.yml` with a flow that collects amount, recipient, account_from and then runs `action_process_transfer_with_tools`. Create `level5/actions/action_process_transfer_with_tools.py` and add `action_process_transfer_with_tools` to the domain `actions:` list. Run the assessment when done.

**Codio guide (Level 5).** The Lab 4.1 page in the Level 5 guide includes: `{Check It!|assessment}(code-output-compare-501040001)`. Assessment JSON: `.guides/assessments/code-output-compare-501040001.json`.

---

## Assessment Setup (For Implementers)

### Overview

Verifies: (1) transfer_money_tools.yml exists with collect steps and action step action_process_transfer_with_tools; (2) action file action_process_transfer_with_tools.py exists with correct name(); (3) domain basics.yml lists action_process_transfer_with_tools in actions.

### Assessment Type

**LLM Rubric** or **Code Test**.

### Option A: LLM Rubric

Solution: `.guides/secure/level5_graders/lab_4.1_solution_reference.md`. Criteria: flow file with transfer_money_tools, collect amount/recipient/account_from, action action_process_transfer_with_tools; action file with name returning "action_process_transfer_with_tools"; domain actions list. Points: 10. Files: level5/data/basics/transfer_money_tools.yml, level5/actions/action_process_transfer_with_tools.py, level5/domain/basics.yml.

### Option B: Code Test

Grader: `.guides/secure/level5_graders/lab_4.1_grader.py`. **Check 1–4**, Lab 6.2-style; **` PASS: Lab 4.1 verification complete! Score: 10/10`**. COMMAND: venv Python + grader. Sequence: `code-output-compare-501040001.json`.
