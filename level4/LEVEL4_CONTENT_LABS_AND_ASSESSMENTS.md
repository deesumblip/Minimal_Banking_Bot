# Level 4: Content, Labs, and Assessment Files — How to Mirror Level 3

This document describes how to create **Level 4** content, labs, and assessment files so they mirror the structure and style of Level 3. **Instructional content** assumes Chapter 1.4 **begins** from **Chapter 1.3 completion** (what the student finished in **`level3/`**); labs **add** transfer domain fields, **`action_process_transfer`**, **`transfer_money.yml`**, then train and test.

---

## 1. Level 3 → Level 4 mapping

| Level 3 | Level 4 equivalent |
|--------|---------------------|
| **Starter** = Level 2 end state | **Starter** = Level 3 / Ch. 1.3 **completion** (then **add** transfer work in Chapter 1.4 labs) |
| Unit 0: Your Level 2 agent / What Level 3 adds | Unit 0: Your Level 3 agent / What Level 4 adds |
| Unit 1: Slots intro, types, naming | Unit 1: Multiple slots intro, ordering, slot naming (1.1, 1.2, 1.3) |
| Unit 2 + **Lab 3.1** (domain: account, utter_ask_account, register action) | Unit 2 + **Lab 2.1** (domain: amount, recipient, account_from + utter_ask_* + register action_process_transfer) |
| Unit 3 + **Lab 4.1** (action file: action_check_balance_simple) | Unit 3 + **Lab 3.1** (action file: action_process_transfer) |
| Unit 4 + **Lab 5.1** (flow: check_balance.yml, collect account + action) | Unit 4 + **Lab 4.1** (flow: transfer_money.yml, collect amount/recipient/account_from + action) |
| Unit 5 + Lab 6.1 (train) + Lab 6.2 (test Inspector) | Unit 5 + Lab 5.1 (train) + Lab 5.2 (completion check + Inspector with **scripted transfer** table) |
| Unit 6: Walkthrough, summary, Level 4 preview | Unit 6: Complete walkthrough, What you've learned, What's next (6.1, 6.2, 6.3) |

**Lab numbering (this course):** Level 4 uses **Lab 2.1** (domain), **3.1** (action), **4.1** (flow), **5.1** (train), **5.2** (completion check + Inspector)—same pattern as Level 3’s chapter lab index, not a single “4.x-only” sequence.

---

## 2. Level 4 course outline (mirror Level3_Course_Outline.md)

Create **Level4_Course_Outline.md** in `level4/` with:

- **Prerequisites:** Level 1, 2, and 3 completed.
- **Learning objective:** Add multiple slots, multiple ask responses, one new action, and one flow that collects several slots then runs the action.
- **Unit 0:** Recap Level 3 (domain with account slot, check_balance flow, action_check_balance_simple). **0.2** includes the **complete delta** (pipeline **`config.yml`** / **`endpoints.yml`** + lab deliverables). Lab adds: slots `amount`, `recipient`, `account_from`; utter_ask_*; action_process_transfer; transfer_money flow.
- **Unit 1:** Concept content only (what are multiple slots, why order matters, slot naming — 1.1, 1.2, 1.3).
- **Unit 2:** Domain — add three slots, three ask responses, register action_process_transfer → **Lab 2.1** (graded).
- **Unit 3:** Reading multiple slots in actions → **Lab 3.1** (create action_process_transfer.py) (graded).
- **Unit 4:** Flows with multiple collect steps → **Lab 4.1** (create transfer_money.yml) (graded).
- **Unit 5:** Training and testing → **Lab 5.1** (train from level4), **Lab 5.2** (completion check graded + **Rasa Inspector** using a **fixed sequence of user turns** in the Lab 5.2 page—see **Scripted transfer** below). No separate Unit 5 concept-only pages.
- **Unit 6:** Complete agent walkthrough, summary, what’s next.

**Assessment summary table:** Lab 2.1 (domain), 3.1 (action), 4.1 (flow), 5.1 (train), 5.2 (test); same Codio pattern as Level 3 Lab 3.1 / Chapter 1.2 Lab 6.2: **sequence** of `Check N: PASSED` substring tests (see `code-output-compare-40102*` – `401050002.json`), not a single `PASS` line.

---

## 3. Unit content files (source of truth in level4/)

Create one markdown file per section, same naming pattern as Level 3. Paths under `level4/`:

| File | Purpose |
|------|--------|
| `Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md` | Recap: level4 folder = your Level 3 agent; what’s in domain (account slot, utter_ask_account, actions), data/basics (check_balance, hours, holiday_hours, …), actions (`action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`). What Level 3 couldn’t do: collect several pieces of info in one flow (e.g. amount, recipient, account). |
| `Level4_Unit0_Content_0.2_What-Level-4-Adds.md` | Concept + **authoritative Ch 1.3 end → Ch 1.4 end checklist**: pipeline (**`config.yml`** / **`endpoints.yml`**), lab deliverables, summary table; lab order 2.1 → 3.1 → 4.1 → 5.1 → 5.2. |
| `Level4_Unit1_Content_1.1_Multiple-Slots.md` | Multiple slots = agent remembers several values in one conversation (e.g. amount, recipient, account_from for a transfer). |
| `Level4_Unit1_Content_1.2_Order-of-Collection.md` | Order of `collect:` steps in the flow determines the order the agent asks; keep order consistent with the action’s expectations. |
| `Level4_Unit1_Content_1.3_Slot-Naming-Multiple.md` | Naming: utter_ask_<slot_name>; slot names used in action must match domain and flow. |
| `Level4_Unit2_Content_2.1_Adding-Slots-and-Responses.md` | Domain: add slots amount, recipient, account_from (type text); add utter_ask_amount, utter_ask_recipient, utter_ask_account_from; **append** action_process_transfer to actions **without removing** Level 3 actions. Pointer to Lab 2.1. |
| `Level4_Unit3_Content_3.1_Reading-Multiple-Slots.md` | In an action, use `tracker.get_slot` for all three slots; cap **recipient** at **100** characters in code to match the flow; validate placeholders; pointer to Lab 3.1. |
| `Level4_Unit4_Content_4.1_Multiple-Collect-Steps.md` | Flow steps: multiple `collect:` steps (e.g. amount, then recipient, then account_from), then `action: action_process_transfer`. **`collect: recipient`** `description:` should state free text up to **100** chars (course build). Pointer to Lab 4.1. |
| `Level4_Unit6_Content_6.1_Complete-Agent-Walkthrough.md` | Short recap + same **scripted transfer** turns as Lab 5.2 / Unit 6.1 guide page (optional hands-on). |
| `Level4_Unit6_Content_6.2_What-Youve-Learned.md` | Summary: multiple slots, multiple collect steps, one action using all slots. |
| `Level4_Unit6_Content_6.3_Whats-Next.md` | What's next: forms, NLU, channels. |

You can add or remove sections within units (e.g. 2.2 Test Your Knowledge, 5.3 Common Issues) to match Level 3 density.

---

## 4. Lab content files (level4/)

Each lab has one **Content** markdown file that students see. Match the style of Level 3 (objective, step-by-step, Part 1 Codio / Part 2 local, success criteria).

### Lab 2.1 — Domain (add slots + ask responses + register action)

**File:** `level4/Level4_Lab2.1_Content.md`

- **Objective:** Add slots `amount`, `recipient`, `account_from`; add utter_ask_amount, utter_ask_recipient, utter_ask_account_from; add `action_process_transfer` to the `actions:` list in `level4/domain/basics.yml`. (Action file is created in Lab 3.1.)
- **Steps:** 1) Open level4/domain/basics.yml. 2) Add the three slots under `slots:` (each type: text). 3) Add the three responses under `responses:` with appropriate ask text. 4) Add `action_process_transfer` to `actions:`. 5) Verify YAML and that Level 3 content is unchanged.
- **Part 1 (Codio):** Terminal from workspace root → activate venv, cd level4, edit domain. Run assessment when done.
- **Part 2 (Local):** Same steps for local env.
- **Success criteria:** domain has slots amount, recipient, account_from; has utter_ask_amount, utter_ask_recipient, utter_ask_account_from; has action_process_transfer in actions.

### Lab 3.1 — Action (create action_process_transfer.py)

**File:** `level4/Level4_Lab3.1_Content.md`

- **Objective:** Create `level4/actions/action_process_transfer.py` that reads `amount`, `recipient`, and `account_from` from the tracker, caps **recipient** at **100** characters (course build), validates placeholders, and sends the demo confirmation (`(Demo) Transfer of $…`).
- **Steps:** 1) Create the file in level4/actions/. 2) Use Action base class, name() returning "action_process_transfer". 3) In run(), get the three slots; apply `[:100]` to recipient; check placeholders (case-insensitive); re-prompt or utter the demo confirmation. 4) Return [].
- **Part 1 / Part 2:** Same Codio vs local pattern. Run assessment when done.
- **Success criteria:** File exists; has correct name; run() reads all three slots and sends a message.

Use the **fill-in-the-blanks** assessment **`fill-in-the-blanks-401030010.json`** (twelve blanks, aligned with the repo action); regenerate via `.guides/scripts/regen_fill_401030010.py` if the canonical action changes.

### Lab 4.1 — Flow (create transfer_money.yml)

**File:** `level4/Level4_Lab4.1_Content.md`

- **Objective:** Create `level4/data/basics/transfer_money.yml` with a flow that has collect: amount, collect: recipient, collect: account_from, then action: action_process_transfer.
- **Steps:** 1) Create file in level4/data/basics/. 2) Add flows.transfer_money with name, description, steps: three collect steps (with optional description), then action step. 3) Verify path and structure.
- **Part 1 / Part 2:** Same pattern. Run assessment when done.
- **Success criteria:** File exists; valid YAML; flow has the three collect steps and action_process_transfer.

### Lab 5.1 — Training

**File:** `level4/Level4_Lab5.1_Content.md`

- Same workflow as Level 3 training: venv from project root → `cd level4` → `python -m rasa train` → verify a new `.tar.gz` in `level4/models/`. Includes short context on what Rasa loads (domain, flows, actions), troubleshooting mapped to Labs 2.1 / 3.1 / 4.1, pointer to Lab 5.2 after **Check It!** (Codio). No separate Unit 5 “5.1 concept” page — all student-facing training content lives here.

### Lab 5.2 — Completion check & Inspector

**File:** `level4/Level4_Lab5.2_Content.md`

- **Part 1:** Graded **completion check** (`lab_5.2_grader.py`) — domain, action, flow, and model present. Does not run Rasa.
- **Parts 2–3:** **Rasa Inspector** (Codio or local): start `rasa inspect` / `rasa run`, then follow the **scripted transfer** on the lab page. Spot-check other flows (balance, hours) if time. Same page as the check (no separate Unit 5 “5.2 concept” file).

#### Scripted transfer (Inspector) — canonical user turns

Students should type **in order** (mirrors **Chapter 1.4** `.guides/.../Lab-5-2-Testing-Completion-f9a0.md` and `level4/README.md`):

| Step | Example user message | What to verify |
|------|----------------------|----------------|
| 1 | `Can I transfer some money?` | Transfer flow starts. |
| 2 | `let's say 300 dollars` | **Amount** collected; agent asks for recipient. |
| 3 | `Alice` (or any short free-text **recipient**; **≤100** chars in action + flow) | **Recipient** stored; agent asks for source account. |
| 4 | `savings` (or e.g. `1234`) | **`action_process_transfer`** runs; confirmation starts with **`(Demo) Transfer of $`** … |

**Expected shape:** `(Demo) Transfer of $300 from account savings to Alice has been processed successfully.` (exact wording may vary slightly with slot values.)

**Troubleshooting** (if “unable to understand you” on names): `rephrase: False` on `utter_ask_*` in domain; clear `description:` on `collect: recipient` / `account_from` in flow; **`level4/config.yml`** uses **`CompactLLMCommandGenerator`**; retrain from `level4`. See `PIPELINE_CHAPTER_1_3_AND_4.md`.

---

## 5. Assessment setup files (level4/)

For each graded lab, create an **Assessment_Setup** markdown file for implementers. Same structure as Level 3: Guide Content (for students), Assessment Setup (for implementers), Option A (LLM Rubric), Option B (Standard Code Test with Python grader), and any script template/key in “implementers only” section.

### Level4_Lab2.1_Assessment_Setup.md

- **Guide content:** Placement after Unit 2. Task: In level4/domain/basics.yml add slots amount, recipient, account_from; add utter_ask_amount, utter_ask_recipient, utter_ask_account_from; add action_process_transfer to actions. Run assessment when done.
- **Overview:** Verifies domain has the three slots, the three ask responses, and action_process_transfer in actions.
- **Option A:** LLM Rubric; solution file `.guides/secure/level4_graders/lab_2.1_solution_reference.md`; rubric criteria: slots section with amount, recipient, account_from; utter_ask_amount, utter_ask_recipient, utter_ask_account_from present with text; action_process_transfer in actions; valid YAML and Level 3 content preserved.
- **Option B:** Standard Code Test; COMMAND: venv Python running `.guides/secure/level4_graders/lab_2.1_grader.py`; Working Directory `/home/codio/workspace`; EXPECTED OUTPUT `PASS` with **substring match**; rationale text for students.

### Level4_Lab3.1_Assessment_Setup.md

- **Guide content:** Task: Create level4/actions/action_process_transfer.py that reads amount, recipient, account_from and sends a confirmation (and optionally handles placeholders). Run assessment when done.
- **Overview:** Verifies file exists; class ActionProcessTransfer(Action); name() returns "action_process_transfer"; run() reads the three slots and sends a message.
- **Option A:** LLM Rubric; solution file lab_3.1_solution_reference.md.
- **Option B:** Standard Code Test; lab_3.1_grader.py; substring match for PASS.

### Level4_Lab4.1_Assessment_Setup.md

- **Guide content:** Task: Create level4/data/basics/transfer_money.yml with flow that has collect amount, recipient, account_from and action action_process_transfer. Run assessment when done.
- **Overview:** Verifies file exists; valid YAML; flows with transfer_money; steps include collect: amount, collect: recipient, collect: account_from, action: action_process_transfer.
- **Option A:** LLM Rubric; solution file lab_4.1_solution_reference.md.
- **Option B:** Standard Code Test; lab_4.1_grader.py; substring match for PASS.

### Level4_Lab5.1_Assessment_Setup.md

- Mirror **Level3_Lab6.1_Assessment_Setup.md**: checks venv, cd level4, model exists in level4/models/. Use a lab_5.1_grader.py (or reuse pattern from lab_6.1_grader.py adapted for level4).

---

## 6. Grader scripts (.guides/secure/level4_graders/)

Create a directory `.guides/secure/level4_graders/` and add Python graders that run from workspace root (`/home/codio/workspace`). Each script should print check results, then a summary line (`PASS: Lab X.X verification complete!` or similar) and exit 0 on full score, or `FAIL` and exit 1. Codio **code-output-compare** assessments use **substring** matches on each **`Check N: PASSED`** line (see `40102*`–`401050002.json`), not a single `PASS` token.

### lab_2.1_grader.py

- **Checks:** level4/domain/basics.yml exists; valid YAML; `slots` dict with keys amount, recipient, account_from (type text or equivalent); `responses` has utter_ask_amount, utter_ask_recipient, utter_ask_account_from with at least one text each; `actions` list includes "action_process_transfer".
- **Points:** e.g. 2 (file + YAML) + 2 (slots) + 2 (ask responses) + 2 (action) = 8; or 10 with partials. Print PASS when all pass.

### lab_3.1_grader.py

- **Checks:** level4/actions/action_process_transfer.py exists; file contains class ActionProcessTransfer(Action) (or equivalent); name() returns "action_process_transfer"; run() uses tracker.get_slot("amount"), get_slot("recipient"), get_slot("account_from"); sends a message (dispatcher.utter_message). No need to execute the action; parsing the file or importing and inspecting is enough.
- **Points:** e.g. 2 (file) + 2 (class/name) + 3 (run reads slots) + 2 (utter_message) = 9 or 10. Print PASS when all pass.

### lab_4.1_grader.py

- **Checks:** level4/data/basics/transfer_money.yml exists; valid YAML; top-level flows; a flow (e.g. transfer_money) with steps; steps contain collect: amount, collect: recipient, collect: account_from, action: action_process_transfer. Order of collect steps can be flexible if you want; strict order can match transfer_money.yml (amount, recipient, account_from).
- **Points:** e.g. 2 (file) + 2 (flows structure) + 2 (three collect steps) + 2 (action step) = 8. Print PASS when all pass.

### lab_5.1_grader.py

- Mirror lab_6.1_grader.py: check level4/models/ has a .tar.gz model file (and optionally that it’s recent). Paths: WORKSPACE_ROOT / "level4" / "models".

### lab_5.2_grader.py

- **Checks:** Composite “completion”: domain (three transfer slots + three `utter_ask_*` + `action_process_transfer` in actions); `action_process_transfer.py` reads amount, recipient, account_from; `transfer_money.yml` has the three `collect:` steps and `action: action_process_transfer`; `level4/models/*.tar.gz` exists. Prints **`Check N: PASSED`** sequence for Codio **code-output-compare** (`401050002.json`). Does **not** run Inspector—the **scripted transfer** table is manual QA (documented in Lab 5.2 content and this file §4).

---

## 7. Solution reference files (.guides/secure/level4_graders/)

For each graded lab, add a **solution reference** markdown file used as the Instructor Provided Solution File for LLM Rubric.

- **lab_2.1_solution_reference.md:** Describe required domain changes: slots amount, recipient, account_from (type text); utter_ask_amount, utter_ask_recipient, utter_ask_account_from with example text; action_process_transfer in actions. Include minimal YAML snippets.
- **lab_3.1_solution_reference.md:** Describe required action: class name, name() return value, run() reading three slots (recipient capped at **100** chars), placeholder check, demo confirmation. Include minimal code snippets or full reference.
- **lab_4.1_solution_reference.md:** Describe required flow: flows.transfer_money, steps with collect amount, recipient, account_from and action action_process_transfer. Include full transfer_money.yml reference.
- **lab_5.1_solution_reference.md:** Describe that student must train from level4 and that a model file must exist in level4/models/.
- **lab_5.2_solution_reference.md:** Describe completion criteria (domain + action + flow + model); point authors to the **scripted transfer** turns (§4) for optional Inspector QA.

---

## 8. File checklist (what to create)

| Category | Files to create |
|----------|------------------|
| **Outline** | level4/Level4_Course_Outline.md |
| **Unit content** | Level4_Unit0_Content_0.1_*.md, 0.2_*.md (includes complete delta); Unit1 (1.1, 1.2, 1.3); Unit2 (2.1); Unit3 (3.1); Unit4 (4.1); Unit5 (5.1, 5.2); Unit6 (6.1, 6.2, 6.3). |
| **Lab content** | Level4_Lab2.1_Content.md, Level4_Lab3.1_Content.md, Level4_Lab4.1_Content.md, Level4_Lab5.1_Content.md, Level4_Lab5.2_Content.md |
| **Assessment setup** | Level4_Lab2.1_Assessment_Setup.md, Level4_Lab3.1_Assessment_Setup.md, Level4_Lab4.1_Assessment_Setup.md, Level4_Lab5.1_Assessment_Setup.md, Level4_Lab5.2_Assessment_Setup.md |
| **Graders** | .guides/secure/level4_graders/lab_2.1_grader.py, lab_3.1_grader.py, lab_4.1_grader.py, lab_5.1_grader.py, lab_5.2_grader.py |
| **Solution refs** | .guides/secure/level4_graders/lab_2.1_solution_reference.md … lab_5.2_solution_reference.md |

---

## 9. Codio and .guides sync

- **Chapter/section:** Add a Level 4 chapter (or section) in Codio; create units and lab pages that link to the assessments.
- **Content:** Copy or sync from level4/Level4_Unit*_Content_*.md and Level4_Lab*_Content.md into `.guides/content/...` (or paste into Codio Guide Editor). Remove duplicate H1 if the guide adds its own title.
- **Assessments:** For each lab, add either LLM Rubric (Option A) or Standard Code Test (Option B). For Option B, set COMMAND (venv Python + grader path), Working Directory `/home/codio/workspace`, **enable substring match**, and add rationale text as in Level 3. Level 4 **code-output-compare** JSONs use a **sequence** of outputs (`Check 1: PASSED` … `Check N: PASSED`), not a single `PASS` line—see `code-output-compare-40102*` through `401050002.json`.
- **index.json:** Update so Level 4 units and labs appear in the course navigation.

---

## 10. Summary

| Step | Action |
|------|--------|
| 1 | Align instructional story: Chapter 1.4 **starts** from Chapter 1.3 **completion** (see **LEVEL4_BUILD_FROM_LEVEL3_APPROACH.md**). |
| 2 | Create Level4_Course_Outline.md and all Level4_Unit*_Content_*.md files. |
| 3 | Create Level4_Lab2.1, 3.1, 4.1, 5.1, 5.2_Content.md with step-by-step and success criteria. |
| 4 | Create `Level4_Lab2.1`, `3.1`, `4.1`, `5.1`, `5.2_Assessment_Setup.md` (Option A + B, rationale, substring match). |
| 5 | Add .guides/secure/level4_graders/ with lab_2.1, 3.1, 4.1, 5.1, 5.2_grader.py and solution_reference.md files. |
| 6 | Sync content to Codio; configure assessments; update index/navigation. |

This mirrors Level 3: same types of content (units + labs), same assessment pattern (LLM Rubric or Python grader, substring match for **`Check N: PASSED`** on Level 4), and the same “start from previous level’s end state, add only what this level teaches” approach. **Lab 5.2** adds a **scripted Inspector script** (§4, **Scripted transfer**) so you can exercise **multi-slot + free-text recipient** behavior in a repeatable way.
