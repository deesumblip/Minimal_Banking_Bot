# Level 5: Tool Calling - Implementation Overview for Codio Team

## Executive Summary

This document provides implementation guidance for **Level 5: Tool Calling** on the Codio platform. Content is split into unit, lab, and assessment files (same pattern as Level 4) so you can copy into Codio and configure assessments per lab.

**Key goals**:
- Use the **same conventions** as Level 4 (venv in project root, Codio vs local, Rasa Inspect tab)
- **Storyline**: Level 5 **starts** from **Level 4 completion** (final banking agent); **`level5/`** in the repo is that baseline by default; labs **add** tools, `endpoints.yml` registration, and tool-based transfer flow/action
- Preserve student tutorial content in separate `Level5_Unit*` and `Level5_Lab*` files
- Support auto-grading for all labs (2.1, 3.1, 4.1, 5.1, 5.2) via grader scripts or LLM Rubric
- Single source of truth: content lives in `level5/*.md`; Codio `.guides` content is copied from there

### Virtual Environment (Critical)

- **One .venv for the whole course**: Created in **project root** in Lab 0.1 (Level 1). Students do **not** create a new venv in `level5/`.
- **Every lab**: Students **activate from project root** (`source .venv/bin/activate`), then **`cd level5`**, then run commands.
- **Grader scripts**: Run from **workspace root** (`/home/codio/workspace`); script activates venv and `cd`s to `level5` for file/command checks.

### Codio guide folder ID (Do Not Overlap)

Existing guide folder IDs in `.guides/content/` include **Level-1---Just-Responses-d3b4**, **Level-2---Custom-Actions-30d6**, **Level-3---Slot-Collection-a4b5**, **Level-4---Multiple-Slots-e5f6**. **Use a unique ID for Level 5**, e.g. **Level-5---Tool-Calling-f9e0** (suffix `f9e0`). When creating or syncing Level 5 content, ensure unit and page IDs under this guide do not duplicate IDs used in other levels.

### Codio vs Local

- **Part 1 (In Codio)**: Terminal opens at `~/workspace`. Activate venv, `cd level5`. For Inspector: use the **Rasa Inspect** tab in the menu bar (do **not** use Tools -> Ports or port 5005).
- **Part 2 (Running locally)**: Instructions broken down by OS (Windows PowerShell, Windows Command Prompt, macOS/Linux).

---

## File Layout (Level 5)

### Content Files (Copy into Codio)
- `Level5_Unit0_Content_0.1_*.md`, `Level5_Unit0_Content_0.2_*.md`
- `Level5_Unit1_Content_1.1_*.md`, `Level5_Unit1_Content_1.2_*.md`
- `Level5_Unit2_Content_2.1_*.md`
- `Level5_Unit3_Content_3.1_*.md`
- `Level5_Unit4_Content_4.1_*.md`
- `Level5_Unit5_Content_5.1_*.md`, `Level5_Unit5_Content_5.2_*.md`
- `Level5_Unit6_Content_6.1_*.md` … `Level5_Unit6_Content_6.7_*.md` (6.4 Knowledge Check, 6.5 Limitations, 6.6 What's Next Level 6 Preview, 6.7 Course Completion Checklist)

### Lab Content (Student-facing)
- `Level5_Lab2.1_Content.md` - Creating the tools folder and banking_tools.py (graded)
- `Level5_Lab3.1_Content.md` - Registering tools in endpoints.yml (graded)
- `Level5_Lab4.1_Content.md` - Creating transfer_money_tools flow and action (graded)
- `Level5_Lab5.1_Content.md` - Training (graded)
- `Level5_Lab5.2_Content.md` - Testing / completion check (graded)

### Assessment Setup (Implementers)
- `Level5_Lab2.1_Assessment_Setup.md` through `Level5_Lab5.2_Assessment_Setup.md` - each lab graded (LLM Rubric or Code Test)

---

## Technical Specifications

### Lab Environment
- **Base**: Same as L4 (Linux on Codio, Python 3.11, Rasa Pro)
- **Virtual environment**: **Project root** (e.g. `/home/codio/workspace/.venv`). Not inside `level5/`.
- **Rasa Inspector on Codio**: **Rasa Inspect** tab only. No port forwarding or Ports view for students.

### Project Structure (Level 5)
```
level5/
├── domain/
│   └── basics.yml
├── data/
│   └── basics/
│       ├── greet.yml, help.yml, contact.yml, hours.yml, check_balance.yml
│       ├── transfer_money.yml
│       └── transfer_money_tools.yml   # NEW
├── actions/
│   ├── __init__.py
│   ├── action_bank_hours.py
│   ├── action_check_balance_simple.py
│   ├── action_process_transfer.py
│   └── action_process_transfer_with_tools.py   # NEW
├── tools/                              # NEW
│   ├── __init__.py
│   └── banking_tools.py
├── config.yml
├── credentials.yml
├── endpoints.yml   # includes tools: tools_module: "tools"
├── .env
└── models/   # created after rasa train
```

### Grader Scripts
- Store in `.guides/secure/level5_graders/`
- Labs 2.1, 3.1, 4.1: Option A = LLM Rubric (solution_reference.md). Option B = Python grader (lab_X.X_grader.py).
- Labs 5.1, 5.2: Code Test (lab_5.1_grader.py, lab_5.2_grader.py).
- **Working Directory**: `/home/codio/workspace` (project root)
- **Success output**: Script must print a line containing `PASS` or `Successfully passed!` for Codio expected-output match.
- **Environment note**: Graders are **Codio-only**. They run in Codio with working directory `/home/codio/workspace`; no need to support Windows or local runs.

---

## Alignment with Level 4

| L4 | Level 5 |
|----|--------|
| Venv in project root | Same |
| Activate venv, then cd to level folder | `cd level5` after activate |
| Codio: Rasa Inspect tab | Same (no Ports) |
| Grader: root WD, venv then cd | Same, cd to `level5` |
| PASS / Successfully passed! | Same |
| LevelN_Unit*_Content*.md | Level5_Unit*_Content*.md |
| LevelN_Lab*_Content.md + _Assessment_Setup.md | Same |
| Codio chapter ID unique | Use Level-5---Tool-Calling-f9e0 (no overlap with 1-1..1-4) |
