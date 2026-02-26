# Level 4: Multiple Slots - Course Outline

## Course Overview

**Title**: Level 4: Multiple Slots  
**Description**: Adding a Transfer Flow with Multiple Slot Collection  
**Prerequisites**: Level 1, Level 2, and Level 3 must be completed  
**Learning Objective**: Students learn to add multiple slots, multiple ask responses, one new action that uses all slots, and one flow that collects several slots then runs the action. Labs are ordered: domain (Lab 4.1) → action (Lab 4.2) → flow (Lab 4.3) → train (Lab 4.4) → completion check (Lab 4.5).

---

## Course Structure (7 units: 0–6)

### Unit 0: Recap - What You Built in Level 3
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 0.1 Your Level 3 Banking Bot — `Level4_Unit0_Content_0.1_Your-Level-3-Banking-Bot.md`
- 0.2 What Level 4 Adds — `Level4_Unit0_Content_0.2_What-Level-4-Adds.md`

**Key Concepts**: Recap Level 3, level4 folder = Level 3 end state, what Level 4 adds (transfer flow)

---

### Unit 1: Multiple Slots
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 1.1 Multiple Slots — `Level4_Unit1_Content_1.1_Multiple-Slots.md`
- 1.2 Order of Collection — `Level4_Unit1_Content_1.2_Order-of-Collection.md`
- 1.3 Slot Naming — `Level4_Unit1_Content_1.3_Slot-Naming-Multiple.md`

**Key Concepts**: Multiple slots in one flow, order of collect steps, utter_ask_<slot_name>, slot names match domain, flow, and action

---

### Unit 2: Adding Slots and Responses
**Type**: Content + Lab (with Assessment)  
**Assessment**: Lab 4.1 - Adding Multiple Slots in the Domain

**Sections**:
- 2.1 Adding Slots and Responses — `Level4_Unit2_Content_2.1_Adding-Slots-and-Responses.md`
- Lab 4.1: Adding Multiple Slots in the Domain — `Level4_Lab4.1_Content.md` / `Level4_Lab4.1_Assessment_Setup.md`

**Key Concepts**: Domain slots amount, recipient, account_from; utter_ask_*; action_process_transfer in actions

---

### Unit 3: Reading Multiple Slots in Actions
**Type**: Content + Lab (with Assessment)  
**Assessment**: Lab 4.2 - Writing the Action That Uses Multiple Slots

**Sections**:
- 3.1 Reading Multiple Slots — `Level4_Unit3_Content_3.1_Reading-Multiple-Slots.md`
- Lab 4.2: Writing the Action — `Level4_Lab4.2_Content.md` / `Level4_Lab4.2_Assessment_Setup.md`

**Key Concepts**: tracker.get_slot for amount, recipient, account_from; confirmation message

---

### Unit 4: Flows with Multiple Collect Steps
**Type**: Content + Lab (with Assessment)  
**Assessment**: Lab 4.3 - Creating the Transfer Flow

**Sections**:
- 4.1 Multiple Collect Steps — `Level4_Unit4_Content_4.1_Multiple-Collect-Steps.md`
- Lab 4.3: Creating the Transfer Flow — `Level4_Lab4.3_Content.md` / `Level4_Lab4.3_Assessment_Setup.md`

**Key Concepts**: transfer_money.yml, collect amount/recipient/account_from, action_process_transfer

---

### Unit 5: Training and Testing
**Type**: Content + Labs (with Assessments)  
**Assessment**: Lab 4.4 (training), Lab 4.5 (completion check)

**Sections**:
- 5.1 Training Level 4 — `Level4_Unit5_Content_5.1_Training-Level-4.md`
- 5.2 Testing Transfer — `Level4_Unit5_Content_5.2_Testing-Transfer.md`
- Lab 4.4: Training — `Level4_Lab4.4_Content.md` / `Level4_Lab4.4_Assessment_Setup.md`
- Lab 4.5: Testing / Completion Check — `Level4_Lab4.5_Content.md` / `Level4_Lab4.5_Assessment_Setup.md`

**Key Concepts**: Train from level4, model in level4/models/, completion check (domain + action + flow + model)

---

### Unit 6: Summary and Next Steps
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 6.1 Complete Bot Walkthrough — `Level4_Unit6_Content_6.1_Complete-Bot-Walkthrough.md`
- 6.2 What You've Learned — `Level4_Unit6_Content_6.2_What-Youve-Learned.md`
- 6.3 What's Next — `Level4_Unit6_Content_6.3_Whats-Next.md`

**Key Concepts**: Summary of all flows (greet, help, contact, goodbye, hours, check_balance, transfer_money); Level 4 summary; possible next steps (forms, NLU, channels)

---

## Assessment Summary

| Lab   | Points | Type                    | Grader Script / Solution Ref                    |
|-------|--------|-------------------------|-------------------------------------------------|
| 4.1   | 10     | LLM Rubric or Code Test | lab_4.1_grader.py / lab_4.1_solution_reference.md |
| 4.2   | 10     | LLM Rubric or Code Test | lab_4.2_grader.py / lab_4.2_solution_reference.md |
| 4.3   | 8      | LLM Rubric or Code Test | lab_4.3_grader.py / lab_4.3_solution_reference.md |
| 4.4   | 12     | Code Test               | lab_4.4_grader.py / lab_4.4_solution_reference.md |
| 4.5   | 10     | Code Test (completion)  | lab_4.5_grader.py / lab_4.5_solution_reference.md |

**Total assessment points**: 50. All graders are Python scripts in `.guides/assessments/level4_graders/`. Codio: use **substring match** for expected output `PASS`, Working Directory `/home/codio/workspace`, venv Python in COMMAND.

---

## File Organization (Sync to Codio)

All source files live in **level4/** so you can push to GitHub and sync the same paths to Codio (e.g. copy into `.guides/content/` or paste into Codio Guide Editor for the Level 4 chapter).

### Unit Content (one file per section) — 7 units (0–6)

| Unit | File |
|------|------|
| 0.1 | Level4_Unit0_Content_0.1_Your-Level-3-Banking-Bot.md |
| 0.2 | Level4_Unit0_Content_0.2_What-Level-4-Adds.md |
| 1.1 | Level4_Unit1_Content_1.1_Multiple-Slots.md |
| 1.2 | Level4_Unit1_Content_1.2_Order-of-Collection.md |
| 1.3 | Level4_Unit1_Content_1.3_Slot-Naming-Multiple.md |
| 2.1 | Level4_Unit2_Content_2.1_Adding-Slots-and-Responses.md |
| 3.1 | Level4_Unit3_Content_3.1_Reading-Multiple-Slots.md |
| 4.1 | Level4_Unit4_Content_4.1_Multiple-Collect-Steps.md |
| 5.1 | Level4_Unit5_Content_5.1_Training-Level-4.md |
| 5.2 | Level4_Unit5_Content_5.2_Testing-Transfer.md |
| 6.1 | Level4_Unit6_Content_6.1_Complete-Bot-Walkthrough.md |
| 6.2 | Level4_Unit6_Content_6.2_What-Youve-Learned.md |
| 6.3 | Level4_Unit6_Content_6.3_Whats-Next.md |

### Lab Content + Assessment Setup

| Lab   | Content File              | Assessment Setup File                 |
|-------|---------------------------|---------------------------------------|
| 4.1   | Level4_Lab4.1_Content.md  | Level4_Lab4.1_Assessment_Setup.md     |
| 4.2   | Level4_Lab4.2_Content.md  | Level4_Lab4.2_Assessment_Setup.md     |
| 4.3   | Level4_Lab4.3_Content.md  | Level4_Lab4.3_Assessment_Setup.md     |
| 4.4   | Level4_Lab4.4_Content.md  | Level4_Lab4.4_Assessment_Setup.md     |
| 4.5   | Level4_Lab4.5_Content.md  | Level4_Lab4.5_Assessment_Setup.md     |

### Graders and Solution References (in repo, not student-facing)

- `.guides/assessments/level4_graders/lab_4.1_grader.py` … `lab_4.5_grader.py`
- `.guides/assessments/level4_graders/lab_4.1_solution_reference.md` … `lab_4.5_solution_reference.md`

---

## Technical Requirements

- **Environment**: Same as Level 3 (Codio or local)
- **Virtual environment**: One .venv in project root. Activate from root, then `cd level4`.
- **Rasa**: Rasa Pro (latest stable)
- **Inspector on Codio**: Use Rasa Inspect tab when "Starting Worker" is shown (no Ports / 5005).
- **Prerequisites**: Level 1, 2, and 3 completed.
