# Level 4: Multiple Slots - Course Outline

## Course Overview

**Title**: Level 4: Multiple Slots  
**Description**: Adding a Transfer Flow with Multiple Slot Collection  
**Prerequisites**: Level 1, Level 2, and Level 3 must be completed (Level 4 **assumes** the **final banking agent at the end of Level 3** described in Unit 0.1)  
**Learning Objective**: Students learn to add multiple slots, multiple ask responses, one new action that uses all slots, and one flow that collects several slots then runs the action. They first **build** **`level4/config.yml`** and **`level4/endpoints.yml`** in **Lab 0.1** (fill-in-the-blanks + code test), then align domain and flows in later labs. Lab order: **pipeline (Lab 0.1)** → domain (Lab 2.1) → action (Lab 3.1) → flow (Lab 4.1) → train (Lab 5.1) → completion check (Lab 5.2).

---

## Course Structure (7 units: 0–6)

### Unit 0: Recap - What you built in Level 3
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 0.1 Your Level 3 Banking Agent
- 0.2 What Level 4 Adds — full Level 3 end → Level 4 end checklist, pipeline, labs, and summary

**Key Concepts**: Recap Level 3, **`level4/`** baseline, pipeline + lab delta in **0.2**, transfer flow

---

### Unit 1: Multiple Slots
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 1.1 Multiple Slots
- 1.2 Order of Collection
- 1.3 Slot Naming
- 1.4 Test Your Knowledge

**Key Concepts**: Multiple slots in one flow, order of collect steps, utter_ask_<slot_name>, slot names match domain, flow, and action

---

### Unit 2: Adding Slots and Responses
**Type**: Content + Lab (with Assessment)  
**Assessment**: Lab 2.1 - Adding Multiple Slots in the Domain

**Sections**:
- 2.1 Adding Slots and Responses
- Lab 2.1: Adding Multiple Slots in the Domain (lab + instructor assessment setup under **level4/**)

**Key Concepts**: Domain slots amount, recipient, account_from; utter_ask_*; action_process_transfer in actions

---

### Unit 3: Reading Multiple Slots in Actions
**Type**: Content + Lab (with Assessment)  
**Assessment**: Lab 3.1 - Writing the Action That Uses Multiple Slots

**Sections**:
- 3.1 Reading Multiple Slots
- Lab 3.1: Writing the Action (lab + instructor assessment setup under **level4/**)

**Key Concepts**: tracker.get_slot for amount, recipient, account_from; confirmation message

---

### Unit 4: Flows with Multiple Collect Steps
**Type**: Content + Lab (with Assessment)  
**Assessment**: Lab 4.1 - Creating the Transfer Flow

**Sections**:
- 4.1 Multiple Collect Steps
- Lab 4.1: Creating the Transfer Flow (lab + instructor assessment setup under **level4/**)

**Key Concepts**: transfer_money.yml, collect amount/recipient/account_from, action_process_transfer

---

### Unit 5: Training and Testing
**Type**: Labs (with Assessments); no separate unit-only content pages  
**Assessment**: Lab 5.1 (training), Lab 5.2 (completion check)

**Sections**:
- Lab 5.1: Training (steps + graded check) — lab + instructor assessment setup under **level4/**
- Lab 5.2: Completion check + optional Inspector — lab + instructor assessment setup under **level4/**

**Key Concepts**: Train from level4, model in level4/models/, completion check (domain + action + flow + model + config pipeline; **`endpoints.yml`** aligned in **Lab 0.1**)

---

### Unit 6: Summary and Next Steps
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 6.1 Complete Agent Walkthrough
- 6.2 What You've Learned
- 6.3 What's Next
- 6.4 Knowledge Check
- 6.5 Limitations of Level 4
- 6.6 What's Next: Level 5 Preview
- 6.7 Course Completion Checklist

**Key Concepts**: Summary of all flows; Level 4 summary; knowledge check; limitations; Level 5 preview; course completion checklist

---

## Assessment Summary

| Lab   | Points | Type                    | Grader Script / Solution Ref                    |
|-------|--------|-------------------------|-------------------------------------------------|
| 0.1   | 15     | Fill-in-the-blanks (5) + Code Test (10) | fill-in-the-blanks-401010010 + lab_0.1 grader + solution reference (in `.guides/secure/level4_graders/`) |
| 2.1   | 10     | LLM Rubric or Code Test | lab_2.1 grader + solution reference |
| 3.1   | 10     | LLM Rubric or Code Test | lab_3.1 grader + solution reference |
| 4.1   | 8      | LLM Rubric or Code Test | lab_4.1 grader + solution reference |
| 5.1   | 12     | Code Test               | lab_5.1 grader + solution reference |
| 5.2   | 12     | Code Test (completion)  | lab_5.2 grader + solution reference |

**Total assessment points**: 67. All graders are Python scripts in `.guides/secure/level4_graders/` (Lab 0.1 includes a fill-in-the-blanks assessment JSON). Codio: use **substring match** for expected output `PASS`, Working Directory `/home/codio/workspace`, venv Python in COMMAND.

---

## File Organization (Sync to Codio)

All source files live in **level4/** so you can push to GitHub and sync the same paths to Codio (e.g. copy into `.guides/content/` or paste into Codio Guide Editor for the Level 4 chapter).

### Unit content (mirror under **level4/**) — 7 units (0–6)

| Unit | Guide page (Level 4) |
|------|-------------------------|
| 0.1 | Your Level 3 Banking Agent |
| 0.2 | What Level 4 Adds |
| 1.1–1.4 | Multiple slots through Test Your Knowledge |
| 2.1 | Adding Slots and Responses |
| 3.1 | Reading Multiple Slots |
| 4.1 | Multiple Collect Steps |
| 6.1–6.7 | Summary unit (walkthrough through completion checklist) |

**Unit 5:** No separate concept pages (5.1 / 5.2)—only **Lab 5.1** and **Lab 5.2** in the guide.

### Labs (content + instructor assessment setup)

| Lab | Topic |
|-----|--------|
| 0.1 | Pipeline YAML (fill-in-the-blanks + code test) |
| 2.1 | Domain: multiple slots and asks |
| 3.1 | Action: `action_process_transfer` |
| 4.1 | Flow: `transfer_money.yml` |
| 5.1 | Training |
| 5.2 | Completion check + optional Inspector |

Instructor-facing copy and Codio configuration notes live under **`level4/`** alongside the chapter mirrors.

### Graders and solution references (in repo, not student-facing)

- Python graders and paired solution references for each lab: **`.guides/secure/level4_graders/`**

---

## Technical Requirements

- **Environment**: Same as Level 3 (Codio or local)
- **Virtual environment**: One .venv in project root. Activate from root, then `cd level4`.
- **Rasa**: Rasa Pro 3.16.3 (`rasa-pro==3.16.3`)
- **Inspector on Codio**: Use Rasa Inspect tab when "Starting Worker" is shown (no Ports / 5005).
- **Prerequisites**: Level 1, 2, and 3 completed.
