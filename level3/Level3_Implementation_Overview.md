# Level 3: Slot Collection - Implementation Overview for Codio Team

## Executive Summary

This document provides implementation guidance for **Level 3: Slot Collection** on the Codio platform. Content is split into unit, lab, and assessment files (same pattern as Level 1 and Level 2) so you can copy into Codio and configure assessments per lab.

**Key goals**:
- Use the **same conventions** as Level 1 and Level 2 (venv in project root, Codio vs local, Rasa Inspect tab)
- Preserve student tutorial content in separate `Level3_Unit*` and `Level3_Lab*` files
- Support auto-grading for key labs (e.g. Lab 3.1, Lab 4.1, Lab 6.1) via grader scripts
- Single source of truth: content lives in `level3/*.md`; Codio `.guides` content is copied from there

### Virtual Environment (Critical)

- **One .venv for the whole course**: Created in **project root** in Lab 0.1 (Level 1). Students do **not** create a new venv in `level3/`.
- **Every lab**: Students **activate from project root** (`source .venv/bin/activate`), then **`cd level3`**, then run commands.
- **Grader scripts**: Run from **workspace root** (`/home/codio/workspace`); script activates venv and `cd`s to `level3` for file/command checks.

### Codio vs Local

- **Part 1 (In Codio)**: Terminal opens at `~/workspace`. Activate venv, `cd level3`. For Inspector: use the **Rasa Inspect** tab in the menu bar (do **not** use Tools → Ports or port 5005).
- **Part 2 (Running locally)**: Instructions broken down by OS (Windows PowerShell, Windows Command Prompt, macOS/Linux).

---

## File Layout (Level 3)

### Content Files (Copy into Codio)
- `Level3_Unit0_Content_0.1_*.md`, `Level3_Unit0_Content_0.2_*.md`
- `Level3_Unit1_Content_1.1_*.md` … `1.3_*.md`
- `Level3_Unit2_Content_2.1_*.md`, `2.2_*.md`
- `Level3_Unit3_Content_3.1_*.md`, `3.2_*.md`
- `Level3_Unit4_Content_4.1_*.md` … `4.3_*.md`
- `Level3_Unit5_Content_5.1_*.md` … `5.4_*.md`
- `Level3_Unit6_Content_6.1_*.md` … `6.4_*.md`
- `Level3_Unit7_Content_7.1_*.md` … `7.3_*.md`
- `Level3_Unit8_Content_8.1_*.md` … `8.5_*.md`

### Lab Content (Student-facing)
- `Level3_Lab3.1_Content.md` – Defining a slot in the domain
- `Level3_Lab4.1_Content.md` – Creating a flow with slot collection
- `Level3_Lab6.1_Content.md` – Training and testing with slots

### Assessment Setup (Implementers)
- `Level3_Lab3.1_Assessment_Setup.md` – Lab 3.1 grader and Codio config
- `Level3_Lab4.1_Assessment_Setup.md` – Lab 4.1 grader and config
- `Level3_Lab6.1_Assessment_Setup.md` – Lab 6.1 grader and config

---

## Technical Specifications

### Lab Environment
- **Base**: Same as L1/L2 (Linux on Codio, Python 3.11, Rasa Pro)
- **Virtual environment**: **Project root** (e.g. `/home/codio/workspace/.venv`). Not inside `level3/`.
- **Rasa Inspector on Codio**: **Rasa Inspect** tab only. No port forwarding or Ports view for students.

### Project Structure (Level 3)
```
level3/
├── domain/
│   └── basics.yml       # includes slots:, utter_ask_account
├── data/
│   └── basics/
│       ├── greet.yml, help.yml, contact.yml, hours.yml  # from L2
│       └── check_balance.yml   # NEW: collect account + action
├── actions/
│   ├── __init__.py
│   ├── action_bank_hours.py    # from L2
│   └── action_check_balance_simple.py   # NEW
├── config.yml
├── credentials.yml
├── endpoints.yml
├── .env
└── models/   # created after rasa train
```

### Grader Scripts
- Store in `.guides/assessments/level3_graders/` (e.g. `lab_3.1_grader.sh`, `lab_4.1_grader.sh`, `lab_6.1_grader.sh`)
- **Working Directory**: `/home/codio/workspace` (project root)
- Script: activate venv in workspace root, then `cd level3`, then run checks
- **Success output**: Script must print a line containing `PASS` or `Successfully passed!` so Codio's expected-output match works.
- COMMAND: `bash /home/codio/workspace/.guides/assessments/level3_graders/lab_X.X_grader.sh`

---

## Alignment with Level 1 and Level 2

| L1/L2 | Level 3 |
|-------|--------|
| Venv in project root | Same |
| Activate venv, then cd to level folder | `cd level3` after activate |
| Codio: Rasa Inspect tab | Same (no Ports) |
| Part 1 (Codio) / Part 2 (Local by OS) | Same |
| Grader: root WD, venv then cd | Same, cd to `level3` |
| PASS / Successfully passed! | Same |
| `LevelN_Unit*_Content*.md` | `Level3_Unit*_Content*.md` |
| `LevelN_Lab*_Content.md` + `_Assessment_Setup.md` | Same |

Use the same workflow: copy unit content into guide pages, copy lab content into lab pages, configure assessments from Assessment_Setup files and grader scripts.
