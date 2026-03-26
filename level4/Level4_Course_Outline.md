# Level 4: Multiple Slots - Course Outline

## Course Overview

**Title**: Level 4: Multiple Slots  
**Description**: Adding a Transfer Flow with Multiple Slot Collection  
**Prerequisites**: Level 1, Level 2, and Level 3 must be completed (Chapter 1.4 **assumes** the **final banking agent at the end of Chapter 1.3** described in Unit 0.1)  
**Learning Objective**: Students learn to add multiple slots, multiple ask responses, one new action that uses all slots, and one flow that collects several slots then runs the action. They first **build** **`level4/config.yml`** and **`level4/endpoints.yml`** in **Lab 0.1** (fill-in-the-blanks + code test), then align domain and flows in later labs. Lab order: **pipeline (Lab 0.1)** → domain (Lab 2.1) → action (Lab 3.1) → flow (Lab 4.1) → train (Lab 5.1) → completion check (Lab 5.2).

---

## Course Structure (7 units: 0–6)

### Unit 0: Recap - What You Built in Level 3
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 0.1 Your Level 3 Banking Agent — `Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md`
- 0.2 What Level 4 Adds — `Level4_Unit0_Content_0.2_What-Level-4-Adds.md` — full Chapter 1.3 end → Chapter 1.4 end checklist, pipeline, labs, and summary

**Key Concepts**: Recap Level 3, **`level4/`** baseline, pipeline + lab delta in **0.2**, transfer flow

---

### Unit 1: Multiple Slots
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 1.1 Multiple Slots — `Level4_Unit1_Content_1.1_Multiple-Slots.md`
- 1.2 Order of Collection — `Level4_Unit1_Content_1.2_Order-of-Collection.md`
- 1.3 Slot Naming — `Level4_Unit1_Content_1.3_Slot-Naming-Multiple.md`
- 1.4 Test Your Knowledge — `Level4_Unit1_Content_1.4_Test-Your-Knowledge.md`

**Key Concepts**: Multiple slots in one flow, order of collect steps, utter_ask_<slot_name>, slot names match domain, flow, and action

---

### Unit 2: Adding Slots and Responses
**Type**: Content + Lab (with Assessment)  
**Assessment**: Lab 2.1 - Adding Multiple Slots in the Domain

**Sections**:
- 2.1 Adding Slots and Responses — `Level4_Unit2_Content_2.1_Adding-Slots-and-Responses.md`
- Lab 2.1: Adding Multiple Slots in the Domain — `Level4_Lab2.1_Content.md` / `Level4_Lab2.1_Assessment_Setup.md`

**Key Concepts**: Domain slots amount, recipient, account_from; utter_ask_*; action_process_transfer in actions

---

### Unit 3: Reading Multiple Slots in Actions
**Type**: Content + Lab (with Assessment)  
**Assessment**: Lab 3.1 - Writing the Action That Uses Multiple Slots

**Sections**:
- 3.1 Reading Multiple Slots — `Level4_Unit3_Content_3.1_Reading-Multiple-Slots.md`
- Lab 3.1: Writing the Action — `Level4_Lab3.1_Content.md` / `Level4_Lab3.1_Assessment_Setup.md`

**Key Concepts**: tracker.get_slot for amount, recipient, account_from; confirmation message

---

### Unit 4: Flows with Multiple Collect Steps
**Type**: Content + Lab (with Assessment)  
**Assessment**: Lab 4.1 - Creating the Transfer Flow

**Sections**:
- 4.1 Multiple Collect Steps — `Level4_Unit4_Content_4.1_Multiple-Collect-Steps.md`
- Lab 4.1: Creating the Transfer Flow — `Level4_Lab4.1_Content.md` / `Level4_Lab4.1_Assessment_Setup.md`

**Key Concepts**: transfer_money.yml, collect amount/recipient/account_from, action_process_transfer

---

### Unit 5: Training and Testing
**Type**: Labs (with Assessments); no separate unit-only content pages  
**Assessment**: Lab 5.1 (training), Lab 5.2 (completion check)

**Sections**:
- Lab 5.1: Training (steps + graded check) — `Level4_Lab5.1_Content.md` / `Level4_Lab5.1_Assessment_Setup.md`
- Lab 5.2: Completion check + optional Inspector — `Level4_Lab5.2_Content.md` / `Level4_Lab5.2_Assessment_Setup.md`

**Key Concepts**: Train from level4, model in level4/models/, completion check (domain + action + flow + model + config pipeline; **`endpoints.yml`** aligned in **Lab 0.1**)

---

### Unit 6: Summary and Next Steps
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 6.1 Complete Agent Walkthrough — `Level4_Unit6_Content_6.1_Complete-Agent-Walkthrough.md`
- 6.2 What You've Learned — `Level4_Unit6_Content_6.2_What-Youve-Learned.md`
- 6.3 What's Next — `Level4_Unit6_Content_6.3_Whats-Next.md`
- 6.4 Knowledge Check — `Level4_Unit6_Content_6.4_Knowledge-Check.md`
- 6.5 Limitations of Level 4 — `Level4_Unit6_Content_6.5_Limitations-of-Level-4.md`
- 6.6 What's Next: Level 5 Preview — `Level4_Unit6_Content_6.6_Whats-Next-Level-5-Preview.md`
- 6.7 Course Completion Checklist — `Level4_Unit6_Content_6.7_Course-Completion-Checklist.md`

**Key Concepts**: Summary of all flows; Level 4 summary; knowledge check; limitations; Level 5 preview; course completion checklist

---

## Assessment Summary

| Lab   | Points | Type                    | Grader Script / Solution Ref                    |
|-------|--------|-------------------------|-------------------------------------------------|
| 0.1   | 15     | Fill-in-the-blanks (5) + Code Test (10) | fill-in-the-blanks-401010010 + lab_0.1_grader.py / lab_0.1_solution_reference.md |
| 2.1   | 10     | LLM Rubric or Code Test | lab_2.1_grader.py / lab_2.1_solution_reference.md |
| 3.1   | 10     | LLM Rubric or Code Test | lab_3.1_grader.py / lab_3.1_solution_reference.md |
| 4.1   | 8      | LLM Rubric or Code Test | lab_4.1_grader.py / lab_4.1_solution_reference.md |
| 5.1   | 12     | Code Test               | lab_5.1_grader.py / lab_5.1_solution_reference.md |
| 5.2   | 12     | Code Test (completion)  | lab_5.2_grader.py / lab_5.2_solution_reference.md |

**Total assessment points**: 67. All graders are Python scripts in `.guides/secure/level4_graders/` (Lab 0.1 includes a fill-in-the-blanks assessment JSON). Codio: use **substring match** for expected output `PASS`, Working Directory `/home/codio/workspace`, venv Python in COMMAND.

---

## File Organization (Sync to Codio)

All source files live in **level4/** so you can push to GitHub and sync the same paths to Codio (e.g. copy into `.guides/content/` or paste into Codio Guide Editor for the Level 4 chapter).

### Unit Content (one file per section) — 7 units (0–6)

| Unit | File |
|------|------|
| 0.1 | Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md |
| 0.2 | Level4_Unit0_Content_0.2_What-Level-4-Adds.md |
| 1.1 | Level4_Unit1_Content_1.1_Multiple-Slots.md |
| 1.2 | Level4_Unit1_Content_1.2_Order-of-Collection.md |
| 1.3 | Level4_Unit1_Content_1.3_Slot-Naming-Multiple.md |
| 1.4 | Level4_Unit1_Content_1.4_Test-Your-Knowledge.md |
| 2.1 | Level4_Unit2_Content_2.1_Adding-Slots-and-Responses.md |
| 3.1 | Level4_Unit3_Content_3.1_Reading-Multiple-Slots.md |
| 4.1 | Level4_Unit4_Content_4.1_Multiple-Collect-Steps.md |
| 6.1 | Level4_Unit6_Content_6.1_Complete-Agent-Walkthrough.md |
| 6.2 | Level4_Unit6_Content_6.2_What-Youve-Learned.md |
| 6.3 | Level4_Unit6_Content_6.3_Whats-Next.md |
| 6.4 | Level4_Unit6_Content_6.4_Knowledge-Check.md |
| 6.5 | Level4_Unit6_Content_6.5_Limitations-of-Level-4.md |
| 6.6 | Level4_Unit6_Content_6.6_Whats-Next-Level-5-Preview.md |
| 6.7 | Level4_Unit6_Content_6.7_Course-Completion-Checklist.md |

**Unit 5:** There are no `Level4_Unit5_Content_*` files—training and testing are only in **`Level4_Lab5.1_Content.md`** and **`Level4_Lab5.2_Content.md`**.

### Lab Content + Assessment Setup

| Lab   | Content File              | Assessment Setup File                 |
|-------|---------------------------|---------------------------------------|
| 0.1   | Level4_Lab0.1_Content.md  | Level4_Lab0.1_Assessment_Setup.md     |
| 2.1   | Level4_Lab2.1_Content.md  | Level4_Lab2.1_Assessment_Setup.md     |
| 3.1   | Level4_Lab3.1_Content.md  | Level4_Lab3.1_Assessment_Setup.md     |
| 4.1   | Level4_Lab4.1_Content.md  | Level4_Lab4.1_Assessment_Setup.md     |
| 5.1   | Level4_Lab5.1_Content.md  | Level4_Lab5.1_Assessment_Setup.md     |
| 5.2   | Level4_Lab5.2_Content.md  | Level4_Lab5.2_Assessment_Setup.md     |

### Graders and Solution References (in repo, not student-facing)

- `.guides/secure/level4_graders/lab_0.1_grader.py`, `lab_2.1_grader.py`, `lab_3.1_grader.py`, `lab_4.1_grader.py`, `lab_5.1_grader.py`, `lab_5.2_grader.py`
- `.guides/secure/level4_graders/lab_0.1_solution_reference.md` … `lab_5.2_solution_reference.md`

---

## Technical Requirements

- **Environment**: Same as Level 3 (Codio or local)
- **Virtual environment**: One .venv in project root. Activate from root, then `cd level4`.
- **Rasa**: Rasa Pro (latest stable)
- **Inspector on Codio**: Use Rasa Inspect tab when "Starting Worker" is shown (no Ports / 5005).
- **Prerequisites**: Level 1, 2, and 3 completed.
