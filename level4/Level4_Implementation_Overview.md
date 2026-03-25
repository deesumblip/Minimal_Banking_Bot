# Level 4: Multiple Slots - Implementation Overview for Codio Team

## Executive Summary

This document provides implementation guidance for **Level 4: Multiple Slots** on the Codio platform. Content is split into unit, lab, and assessment files (same pattern as Level 1-3) so you can copy into Codio and configure assessments per lab.

**Key goals**:
- Use the **same conventions** as Level 1-3 (venv in project root, Codio vs local, Rasa Inspect tab)
- **Storyline**: Chapter 1.4 **starts** from **Chapter 1.3 completion**; content describes copying that baseline into **`level4/`** and **adding** transfer domain, action, and flow in labs; **Lab 5.1** produces **`level4/models/`** for **Lab 5.2**
- Preserve student tutorial content in separate `Level4_Unit*` and `Level4_Lab*` files
- Support auto-grading for Labs 2.1, 3.1, 4.1, 5.1 (and completion check 5.2) via Python grader scripts
- Single source of truth: content lives in `level4/*.md`; Codio `.guides` content is copied from there

### Virtual Environment (Critical)

- **One .venv for the whole course**: Created in **project root** in Lab 0.1 (Level 1). Students do **not** create a new venv in `level4/`.
- **Every lab**: Students **activate from project root** (`source .venv/bin/activate`), then **`cd level4`**, then run commands.
- **Grader scripts**: Run from **workspace root** (`/home/codio/workspace`); script activates venv and `cd`s to `level4` for file/command checks.

### Codio vs Local

- **Part 1 (In Codio)**: Terminal opens at `~/workspace`. Activate venv, `cd level4`. For Inspector: use the **Rasa Inspect** tab in the menu bar (do **not** use Tools -> Ports or port 5005).
- **Part 2 (Running locally)**: Instructions broken down by OS (Windows PowerShell, Windows Command Prompt, macOS/Linux).

---

## File Layout (Level 4)

### Content Files (Copy into Codio)
- `Level4_Unit0_Content_0.1_*.md`, `Level4_Unit0_Content_0.2_*.md`
- `Level4_Unit1_Content_1.1_*.md`, `1.2_*.md`, `1.3_*.md`, `1.4_Test-Your-Knowledge.md`
- `Level4_Unit2_Content_2.1_*.md`
- `Level4_Unit3_Content_3.1_*.md`
- `Level4_Unit4_Content_4.1_*.md`
- **Unit 5** has no separate unit-only content files; training and testing are **`Level4_Lab5.1_Content.md`** and **`Level4_Lab5.2_Content.md`** only.
- `Level4_Unit6_Content_6.1_*.md`, `6.2_*.md`, `6.3_*.md`, `6.4_Knowledge-Check.md`, `6.5_Limitations-of-Level-4.md`, `6.6_Whats-Next-Level-5-Preview.md`, `6.7_Course-Completion-Checklist.md`

### Lab Content (Student-facing)
- `Level4_Lab2.1_Content.md` – Adding slots and ask responses in the domain (graded)
- `Level4_Lab3.1_Content.md` – Writing the action that uses multiple slots (graded)
- `Level4_Lab4.1_Content.md` – Creating the transfer flow (graded)
- `Level4_Lab5.1_Content.md` – Training Level 4 (graded)
- `Level4_Lab5.2_Content.md` – Completion check (graded) + optional Inspector testing (single lab page; no separate Unit 5 “5.2 concept” file)

### Assessment Setup (Implementers)
- `Level4_Lab2.1_Assessment_Setup.md` – Lab 2.1 (Code Output Compare, Python grader)
- `Level4_Lab3.1_Assessment_Setup.md` – Lab 3.1 (Code Output Compare, Python grader)
- `Level4_Lab4.1_Assessment_Setup.md` – Lab 4.1 (Code Output Compare, Python grader)
- `Level4_Lab5.1_Assessment_Setup.md` – Lab 5.1 (Code Output Compare, Python grader)
- `Level4_Lab5.2_Assessment_Setup.md` – Lab 5.2 (completion check)

---

## Technical Specifications

### Lab Environment
- **Base**: Same as L1/L2/L3 (Linux on Codio, Python 3.11, Rasa Pro)
- **Virtual environment**: **Project root** (e.g. `/home/codio/workspace/.venv`). Not inside `level4/`.
- **Rasa Inspector on Codio**: **Rasa Inspect** tab only. No port forwarding or Ports view for students.

### Project Structure (Level 4)

**Starter** (what the repo ships): Level 3 end state only.

```
level4/
  domain/
    basics.yml       # slots: account; utter_ask_account; actions: action_bank_hours, action_holiday_hours, action_check_balance_simple
  data/
    basics/
      greet.yml, help.yml, contact.yml, goodbye.yml, hours.yml
      check_balance.yml, holiday_hours.yml
  actions/
    __init__.py
    action_bank_hours.py
    action_holiday_hours.py
    action_check_balance_simple.py
  config.yml
  credentials.yml
  endpoints.yml
  .env
  models/   # created after rasa train
```

**After labs**: Students add in domain (Lab 2.1) slots amount, recipient, account_from and utter_ask_* and register action_process_transfer; create actions/action_process_transfer.py (Lab 3.1); create data/basics/transfer_money.yml (Lab 4.1); then train and test (Labs 5.1, 5.2).

### Grader Scripts
- Store in `.guides/secure/level4_graders/`
- **Labs 2.1, 3.1, 4.1, 5.1**: Python graders (lab_2.1_grader.py, lab_3.1_grader.py, lab_4.1_grader.py, lab_5.1_grader.py). Option A = LLM Rubric using corresponding lab_*_solution_reference.md.
- **Lab 5.2**: lab_5.2_grader.py (completion check: domain, action file, flow file, model present).
- **Working Directory**: `/home/codio/workspace` (project root)
- **Success output**: Script must print a line containing `PASS` or `Successfully passed!` so Codio's expected-output match works.

---

## Alignment with Level 1-3

| L1/L2/L3 | Level 4 |
|----------|--------|
| Venv in project root | Same |
| Activate venv, then cd to level folder | cd level4 after activate |
| Codio: Rasa Inspect tab | Same (no Ports) |
| Part 1 (Codio) / Part 2 (Local by OS) | Same |
| Grader: root WD, venv then cd | Same, cd to level4 |
| PASS / Successfully passed! | Same |
| LevelN_Unit*_Content*.md | Level4_Unit*_Content*.md |
| LevelN_Lab*_Content.md + _Assessment_Setup.md | Same |

Use the same workflow: copy unit content into guide pages, copy lab content into lab pages, configure assessments from Assessment_Setup files and grader scripts.

**Chapter 1.4 (Codio guide)**  
The Chapter 1.4 guide in `.guides/content/Chapter-1-4---Multiple-Slots-e5f6/` includes code-output-compare (or LLM Rubric) on Labs 2.1, 3.1, 4.1, 5.1 and a completion check on Lab 5.2.
