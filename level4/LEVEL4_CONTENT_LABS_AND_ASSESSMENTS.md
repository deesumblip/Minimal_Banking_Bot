# Level 4: Content, Labs, and Assessment Files — How to Mirror Level 3

This document describes how to create **Level 4** content, labs, and assessment files so they mirror the structure and style of Level 3. The **starting point** for Level 4 is the **end of the Level 3 bot** (level4 folder = Level 3 end state). Students add multiple slots, a new action, and the transfer flow in guided labs.

---

## 1. Level 3 → Level 4 mapping

| Level 3 | Level 4 equivalent |
|--------|---------------------|
| **Starter** = Level 2 end state | **Starter** = Level 3 end state (level4 = level3 after Labs 3.1, 4.1, 5.1) |
| Unit 0: Your Level 2 bot / What Level 3 adds | Unit 0: Your Level 3 bot / What Level 4 adds |
| Unit 1–2: Slots intro, types, naming | Unit 1–2: Multiple slots intro, ordering, naming |
| Unit 3 + **Lab 3.1** (domain: account, utter_ask_account, register action) | Unit 3 + **Lab 4.1** (domain: amount, recipient, account_from + utter_ask_* + register action_process_transfer) |
| Unit 4 + **Lab 4.1** (action file: action_check_balance_simple) | Unit 4 + **Lab 4.2** (action file: action_process_transfer) |
| Unit 5 + **Lab 5.1** (flow: check_balance.yml, collect account + action) | Unit 5 + **Lab 4.3** (flow: transfer_money.yml, collect amount/recipient/account_from + action) |
| Unit 6 + Lab 6.1 (train) + Lab 6.2 (test Inspector) | Unit 6 + Lab 4.4 (train) + Lab 4.5 (test transfer in Inspector) |
| Unit 7–8: Walkthrough, summary, Level 4 preview | Unit 7–8: Walkthrough, summary, “What’s next” (e.g. forms or NLU) |

**Lab numbering:** Level 3 uses Labs 3.1, 4.1, 5.1, 6.1, 6.2, 7.1. For Level 4 you can use **Lab 4.1 (domain), 4.2 (action), 4.3 (flow), 4.4 (train), 4.5 (test)** so the “4.x” sequence is self-contained. Alternatively keep a global lab index (e.g. Lab 8.1, 8.2, …) if your course numbers across levels; the structure below uses 4.1–4.5 for clarity.

---

## 2. Level 4 course outline (mirror Level3_Course_Outline.md)

Create **Level4_Course_Outline.md** in `level4/` with:

- **Prerequisites:** Level 1, 2, and 3 completed.
- **Learning objective:** Add multiple slots, multiple ask responses, one new action, and one flow that collects several slots then runs the action.
- **Unit 0:** Recap Level 3 (domain with account slot, check_balance flow, action_check_balance_simple). What Level 4 adds: slots `amount`, `recipient`, `account_from`; utter_ask_amount, utter_ask_recipient, utter_ask_account_from; action_process_transfer; transfer_money flow.
- **Units 1–2:** Concept content only (what are multiple slots, why order matters, naming).
- **Unit 3:** Domain — add three slots, three ask responses, register action_process_transfer → **Lab 4.1** (graded).
- **Unit 4:** Reading multiple slots in actions → **Lab 4.2** (create action_process_transfer.py) (graded).
- **Unit 5:** Flows with multiple collect steps → **Lab 4.3** (create transfer_money.yml) (graded).
- **Unit 6:** Training and testing → **Lab 4.4** (train from level4), **Lab 4.5** (test transfer in Inspector) (4.4 graded like 6.1; 4.5 optional/ungraded).
- **Units 7–8:** Complete bot walkthrough, summary, what’s next.

**Assessment summary table:** Lab 4.1 (domain), 4.2 (action), 4.3 (flow), 4.4 (train); points and types as in Level 3 (LLM Rubric or Standard Code Test with Python grader; substring match for PASS).

---

## 3. Unit content files (source of truth in level4/)

Create one markdown file per section, same naming pattern as Level 3. Paths under `level4/`:

| File | Purpose |
|------|--------|
| `Level4_Unit0_Content_0.1_Your-Level-3-Banking-Bot.md` | Recap: level4 folder = your Level 3 bot; what’s in domain (account slot, utter_ask_account, actions), data/basics (check_balance, hours, …), actions (action_bank_hours, action_check_balance_simple). What Level 3 couldn’t do: collect several pieces of info in one flow (e.g. amount, recipient, account). |
| `Level4_Unit0_Content_0.2_What-Level-4-Adds.md` | Level 4 adds: three slots (amount, recipient, account_from), three utter_ask_* responses, action_process_transfer, transfer_money flow. Order: domain (Lab 4.1) → action (Lab 4.2) → flow (Lab 4.3) → train/test (4.4, 4.5). |
| `Level4_Unit1_Content_1.1_Multiple-Slots.md` | Multiple slots = bot remembers several values in one conversation (e.g. amount, recipient, account_from for a transfer). |
| `Level4_Unit1_Content_1.2_Order-of-Collection.md` | Order of `collect:` steps in the flow determines the order the bot asks; keep order consistent with the action’s expectations. |
| `Level4_Unit2_Content_2.1_Slot-Naming-Multiple.md` | Naming: utter_ask_<slot_name>; slot names used in action must match domain and flow. |
| `Level4_Unit3_Content_3.1_Adding-Slots-and-Responses.md` | Domain: add slots amount, recipient, account_from (type text); add utter_ask_amount, utter_ask_recipient, utter_ask_account_from; add action_process_transfer to actions. Pointer to Lab 4.1. |
| `Level4_Unit4_Content_4.1_Reading-Multiple-Slots.md` | In an action, use tracker.get_slot("amount"), get_slot("recipient"), get_slot("account_from"); validate or re-prompt as needed. Pointer to Lab 4.2. |
| `Level4_Unit5_Content_5.1_Multiple-Collect-Steps.md` | Flow steps: multiple `collect:` steps (e.g. amount, then recipient, then account_from), then `action: action_process_transfer`. Pointer to Lab 4.3. |
| `Level4_Unit6_Content_6.1_Training-Level-4.md` | Train from level4 (same as Level 3: venv, cd level4, rasa train). Lab 4.4. |
| `Level4_Unit6_Content_6.2_Testing-Transfer.md` | Run Inspector, trigger transfer flow, provide amount/recipient/account_from; Lab 4.5. |
| `Level4_Unit7_Content_7.1_Complete-Bot-Walkthrough.md` | Guided walkthrough of Level 4 bot (optional). |
| `Level4_Unit8_Content_8.1_What-Youve-Learned.md` | Summary: multiple slots, multiple collect steps, one action using all slots. |

You can add or remove units (e.g. 2.2 Test Your Knowledge, 6.3 Common Issues) to match Level 3 density.

---

## 4. Lab content files (level4/)

Each lab has one **Content** markdown file that students see. Match the style of Level 3 (objective, step-by-step, Part 1 Codio / Part 2 local, success criteria).

### Lab 4.1 — Domain (add slots + ask responses + register action)

**File:** `level4/Level4_Lab4.1_Content.md`

- **Objective:** Add slots `amount`, `recipient`, `account_from`; add utter_ask_amount, utter_ask_recipient, utter_ask_account_from; add `action_process_transfer` to the `actions:` list in `level4/domain/basics.yml`. (Action file is created in Lab 4.2.)
- **Steps:** 1) Open level4/domain/basics.yml. 2) Add the three slots under `slots:` (each type: text). 3) Add the three responses under `responses:` with appropriate ask text. 4) Add `action_process_transfer` to `actions:`. 5) Verify YAML and that Level 3 content is unchanged.
- **Part 1 (Codio):** Terminal from workspace root → activate venv, cd level4, edit domain. Run assessment when done.
- **Part 2 (Local):** Same steps for local env.
- **Success criteria:** domain has slots amount, recipient, account_from; has utter_ask_amount, utter_ask_recipient, utter_ask_account_from; has action_process_transfer in actions.

### Lab 4.2 — Action (create action_process_transfer.py)

**File:** `level4/Level4_Lab4.2_Content.md`

- **Objective:** Create `level4/actions/action_process_transfer.py` that reads `amount`, `recipient`, and `account_from` from the tracker and sends a confirmation message (and optionally validates placeholders).
- **Steps:** 1) Create the file in level4/actions/. 2) Use Action base class, name() returning "action_process_transfer". 3) In run(), get the three slots; optionally check for placeholders and re-prompt; then utter a demo confirmation (e.g. “Transfer of $X from account Y to Z processed”). 4) Return [].
- **Part 1 / Part 2:** Same Codio vs local pattern. Run assessment when done.
- **Success criteria:** File exists; has correct name; run() reads all three slots and sends a message.

You can add a **fill-in-the-blanks** version (like Level 3 Lab 4.1) with a template and key in the **assessment setup** doc (implementers only), or keep it “write from scratch” with hints.

### Lab 4.3 — Flow (create transfer_money.yml)

**File:** `level4/Level4_Lab4.3_Content.md`

- **Objective:** Create `level4/data/basics/transfer_money.yml` with a flow that has collect: amount, collect: recipient, collect: account_from, then action: action_process_transfer.
- **Steps:** 1) Create file in level4/data/basics/. 2) Add flows.transfer_money with name, description, steps: three collect steps (with optional description), then action step. 3) Verify path and structure.
- **Part 1 / Part 2:** Same pattern. Run assessment when done.
- **Success criteria:** File exists; valid YAML; flow has the three collect steps and action_process_transfer.

### Lab 4.4 — Training

**File:** `level4/Level4_Lab4.4_Content.md`

- Mirror **Level3_Lab6.1_Content.md**: venv from project root, cd level4, rasa train, verify model in level4/models/. Run assessment when done.

### Lab 4.5 — Testing transfer in Inspector

**File:** `level4/Level4_Lab4.5_Content.md`

- Mirror **Level3_Lab6.2_Content.md**: start Rasa (e.g. rasa run), open Rasa Inspect, trigger transfer flow, provide amount/recipient/account_from. No graded assessment (or optional completion check).

---

## 5. Assessment setup files (level4/)

For each graded lab, create an **Assessment_Setup** markdown file for implementers. Same structure as Level 3: Guide Content (for students), Assessment Setup (for implementers), Option A (LLM Rubric), Option B (Standard Code Test with Python grader), and any script template/key in “implementers only” section.

### Level4_Lab4.1_Assessment_Setup.md

- **Guide content:** Placement after Unit 3. Task: In level4/domain/basics.yml add slots amount, recipient, account_from; add utter_ask_amount, utter_ask_recipient, utter_ask_account_from; add action_process_transfer to actions. Run assessment when done.
- **Overview:** Verifies domain has the three slots, the three ask responses, and action_process_transfer in actions.
- **Option A:** LLM Rubric; solution file `.guides/assessments/level4_graders/lab_4.1_solution_reference.md`; rubric criteria: slots section with amount, recipient, account_from; utter_ask_amount, utter_ask_recipient, utter_ask_account_from present with text; action_process_transfer in actions; valid YAML and Level 3 content preserved.
- **Option B:** Standard Code Test; COMMAND: venv Python running `.guides/assessments/level4_graders/lab_4.1_grader.py`; Working Directory `/home/codio/workspace`; EXPECTED OUTPUT `PASS` with **substring match**; rationale text for students.

### Level4_Lab4.2_Assessment_Setup.md

- **Guide content:** Task: Create level4/actions/action_process_transfer.py that reads amount, recipient, account_from and sends a confirmation (and optionally handles placeholders). Run assessment when done.
- **Overview:** Verifies file exists; class ActionProcessTransfer(Action); name() returns "action_process_transfer"; run() reads the three slots and sends a message.
- **Option A:** LLM Rubric; solution file lab_4.2_solution_reference.md.
- **Option B:** Standard Code Test; lab_4.2_grader.py; substring match for PASS.

### Level4_Lab4.3_Assessment_Setup.md

- **Guide content:** Task: Create level4/data/basics/transfer_money.yml with flow that has collect amount, recipient, account_from and action action_process_transfer. Run assessment when done.
- **Overview:** Verifies file exists; valid YAML; flows with transfer_money; steps include collect: amount, collect: recipient, collect: account_from, action: action_process_transfer.
- **Option A:** LLM Rubric; solution file lab_4.3_solution_reference.md.
- **Option B:** Standard Code Test; lab_4.3_grader.py; substring match for PASS.

### Level4_Lab4.4_Assessment_Setup.md

- Mirror **Level3_Lab6.1_Assessment_Setup.md**: checks venv, cd level4, model exists in level4/models/. Use a lab_4.4_grader.py (or reuse pattern from lab_6.1_grader.py adapted for level4).

---

## 6. Grader scripts (.guides/assessments/level4_graders/)

Create a directory `.guides/assessments/level4_graders/` and add Python graders that run from workspace root (`/home/codio/workspace`). Each script should print check results, then `PASS` and exit 0 on full score, or `FAIL` and exit 1. Codio Standard Code Test: COMMAND = venv Python + script path; EXPECTED OUTPUT = `PASS` with **substring match** enabled.

### lab_4.1_grader.py

- **Checks:** level4/domain/basics.yml exists; valid YAML; `slots` dict with keys amount, recipient, account_from (type text or equivalent); `responses` has utter_ask_amount, utter_ask_recipient, utter_ask_account_from with at least one text each; `actions` list includes "action_process_transfer".
- **Points:** e.g. 2 (file + YAML) + 2 (slots) + 2 (ask responses) + 2 (action) = 8; or 10 with partials. Print PASS when all pass.

### lab_4.2_grader.py

- **Checks:** level4/actions/action_process_transfer.py exists; file contains class ActionProcessTransfer(Action) (or equivalent); name() returns "action_process_transfer"; run() uses tracker.get_slot("amount"), get_slot("recipient"), get_slot("account_from"); sends a message (dispatcher.utter_message). No need to execute the action; parsing the file or importing and inspecting is enough.
- **Points:** e.g. 2 (file) + 2 (class/name) + 3 (run reads slots) + 2 (utter_message) = 9 or 10. Print PASS when all pass.

### lab_4.3_grader.py

- **Checks:** level4/data/basics/transfer_money.yml exists; valid YAML; top-level flows; a flow (e.g. transfer_money) with steps; steps contain collect: amount, collect: recipient, collect: account_from, action: action_process_transfer. Order of collect steps can be flexible if you want; strict order can match transfer_money.yml (amount, recipient, account_from).
- **Points:** e.g. 2 (file) + 2 (flows structure) + 2 (three collect steps) + 2 (action step) = 8. Print PASS when all pass.

### lab_4.4_grader.py

- Mirror lab_6.1_grader.py: check level4/models/ has a .tar.gz model file (and optionally that it’s recent). Paths: WORKSPACE_ROOT / "level4" / "models".

---

## 7. Solution reference files (.guides/assessments/level4_graders/)

For each graded lab, add a **solution reference** markdown file used as the Instructor Provided Solution File for LLM Rubric.

- **lab_4.1_solution_reference.md:** Describe required domain changes: slots amount, recipient, account_from (type text); utter_ask_amount, utter_ask_recipient, utter_ask_account_from with example text; action_process_transfer in actions. Include minimal YAML snippets.
- **lab_4.2_solution_reference.md:** Describe required action: class name, name() return value, run() reading three slots and sending confirmation; optional placeholder check. Include minimal code snippets or full reference.
- **lab_4.3_solution_reference.md:** Describe required flow: flows.transfer_money, steps with collect amount, recipient, account_from and action action_process_transfer. Include full transfer_money.yml reference.
- **lab_4.4_solution_reference.md:** Describe that student must train from level4 and that a model file must exist in level4/models/.

---

## 8. File checklist (what to create)

| Category | Files to create |
|----------|------------------|
| **Outline** | level4/Level4_Course_Outline.md |
| **Unit content** | Level4_Unit0_Content_0.1_*.md, 0.2_*.md; Unit1 (1.1, 1.2); Unit2 (2.1); Unit3 (3.1); Unit4 (4.1); Unit5 (5.1); Unit6 (6.1, 6.2); Unit7 (7.1); Unit8 (8.1). |
| **Lab content** | Level4_Lab4.1_Content.md, Level4_Lab4.2_Content.md, Level4_Lab4.3_Content.md, Level4_Lab4.4_Content.md, Level4_Lab4.5_Content.md |
| **Assessment setup** | Level4_Lab4.1_Assessment_Setup.md, Level4_Lab4.2_Assessment_Setup.md, Level4_Lab4.3_Assessment_Setup.md, Level4_Lab4.4_Assessment_Setup.md |
| **Graders** | .guides/assessments/level4_graders/lab_4.1_grader.py, lab_4.2_grader.py, lab_4.3_grader.py, lab_4.4_grader.py |
| **Solution refs** | .guides/assessments/level4_graders/lab_4.1_solution_reference.md, lab_4.2_solution_reference.md, lab_4.3_solution_reference.md, lab_4.4_solution_reference.md |

---

## 9. Codio and .guides sync

- **Chapter/section:** Add a Level 4 chapter (or section) in Codio; create units and lab pages that link to the assessments.
- **Content:** Copy or sync from level4/Level4_Unit*_Content_*.md and Level4_Lab*_Content.md into `.guides/content/...` (or paste into Codio Guide Editor). Remove duplicate H1 if the guide adds its own title.
- **Assessments:** For each lab, add either LLM Rubric (Option A) or Standard Code Test (Option B). For Option B, set COMMAND (venv Python + grader path), Working Directory `/home/codio/workspace`, EXPECTED OUTPUT `PASS`, **enable substring match**, and add rationale text as in Level 3.
- **index.json:** Update so Level 4 units and labs appear in the course navigation.

---

## 10. Summary

| Step | Action |
|------|--------|
| 1 | Ensure level4 **starter** = Level 3 end state (see LEVEL4_BUILD_FROM_LEVEL3_APPROACH.md). |
| 2 | Create Level4_Course_Outline.md and all Level4_Unit*_Content_*.md files. |
| 3 | Create Level4_Lab4.1–4.5_Content.md with step-by-step and success criteria. |
| 4 | Create Level4_Lab4.1–4.4_Assessment_Setup.md (Option A + B, rationale, substring match). |
| 5 | Add .guides/assessments/level4_graders/ with lab_4.1–4.4_grader.py and solution_reference.md files. |
| 6 | Sync content to Codio; configure assessments; update index/navigation. |

This mirrors Level 3: same types of content (units + labs), same assessment pattern (LLM Rubric or Python grader, substring match for PASS), and the same “start from previous level’s end state, add only what this level teaches” approach.
