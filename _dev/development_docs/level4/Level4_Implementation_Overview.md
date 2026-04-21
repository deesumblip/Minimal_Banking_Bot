# Level 4: Multiple Slots - Implementation Overview for Codio Team

## Executive Summary

This document provides implementation guidance for **Level 4: Multiple Slots** on the Codio platform. Content is split into unit, lab, and assessment files (same pattern as Level 1-3) so you can copy into Codio and configure assessments per lab.

**Key goals**:
- Use the **same conventions** as Level 1-3 (venv in project root, Codio vs local, Rasa Inspect tab)
- **Storyline**: Level 4 **starts** from **Level 3 completion**; **`level4/`** in the repo is that baseline by default; labs **add** transfer domain, action, and flow in **`level4/`**; **Lab 5.1** produces **`level4/models/`** for **Lab 5.2**
- Preserve student tutorial content in separate unit and lab mirrors under **`level4/`**
- Support auto-grading for Labs 2.1, 3.1, 4.1, 5.1 (and completion check 5.2) via Python grader scripts
- Single source of truth: content lives under **`level4/`**; Codio **`.guides`** content is copied from there

### Virtual Environment (Critical)

- **One .venv for the whole course**: Created in **project root** in Lab 0.1 (Level 1). Students do **not** create a new venv in `level4/`.
- **Every lab**: Students **activate from project root** (`source .venv/bin/activate`), then **`cd level4`**, then run commands.
- **Grader scripts**: Run from **workspace root** (`/home/codio/workspace`); script activates venv and `cd`s to `level4` for file/command checks.

### Codio vs Local

- **Part 1 (In Codio)**: Terminal opens at `~/workspace`. Activate venv, `cd level4`. For Inspector: use the **Rasa Inspect** tab in the menu bar (do **not** use Tools -> Ports or port 5005).
- **Part 2 (Running locally)**: Instructions broken down by OS (Windows PowerShell, Windows Command Prompt, macOS/Linux).

---

## File Layout (Level 4)

### Content files (copy into Codio)
- **Units 0.1–0.2**, **1.1–1.4**, **2.1**, **3.1**, **4.1**, **6.1–6.7** — one mirror per section under **`level4/`** (same pattern as earlier levels).
- **Unit 5** has no separate unit-only pages; training and testing are **Lab 5.1** and **Lab 5.2** only.

### Lab content (student-facing)
- **Lab 0.1** — Pipeline YAML (`config.yml` / `endpoints.yml`)
- **Lab 2.1** — Domain: slots and asks (graded)
- **Lab 3.1** — Action: `action_process_transfer` (graded)
- **Lab 4.1** — Flow: `transfer_money.yml` (graded)
- **Lab 5.1** — Training (graded)
- **Lab 5.2** — Completion check (graded) + optional Inspector (single lab page; no separate Unit 5 “5.2 concept” file)

### Assessment setup (implementers)
- Instructor notes for **Labs 2.1, 3.1, 4.1, 5.1, 5.2** under **`level4/`** (Code Output Compare + Python grader; Lab 5.2 = completion check)

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
- **Labs 2.1, 3.1, 4.1, 5.1**: Python graders (lab_2.1_grader.py, lab_3.1_grader.py, lab_4.1_grader.py, lab_5.1_grader.py). Option A = LLM Rubric using corresponding solution references in the same folder.
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
| Unit/lab mirrors under **levelN/** | Same pattern under **level4/** |
| Lab content + instructor assessment setup | Same |

Use the same workflow: copy unit content into guide pages, copy lab content into lab pages, configure assessments from instructor setup notes and grader scripts.

**Level 4 (Codio guide)**  
The Level 4 guide in `.guides/content/Level-4---Multiple-Slots-e5f6/` includes code-output-compare (or LLM Rubric) on Labs 2.1, 3.1, 4.1, 5.1 and a completion check on Lab 5.2.
