# Lab 5.1: Training the Level 4 Agent - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab is **Unit 5: Training and Testing** (Level 4) — the first page in that unit (standalone **Lab 5.1**; there is no separate “5.1 concept” page).

**Structure.** Part 1 (In Codio) and Part 2 (Running locally). Both follow the same order: **activate the virtual environment in the main project folder (root)** first, then **navigate to `level4`**, then train. Run the assessment when done (Part 1 path).

**Codio guide (Level 4).** The Lab 5.1 page in the Level 4 guide includes: `{Check It!|assessment}(code-output-compare-401050001)`. Assessment JSON: `.guides/assessments/code-output-compare-401050001.json`.

### Your Task (summary)

Activate the virtual environment in the main project folder (root), navigate to `level4`, then train your agent by running:

```bash
cd level4
python -m rasa train
```

Wait for training to finish. A model file (`.tar.gz`) will be created in `level4/models/`.

### Verification

Before submitting, confirm:

- Training completed without errors
- A model file exists under `level4/models/`

Run the assessment when you're done (Part 1 path).

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that students can successfully train their Level 4 agent and that training completes without errors (model file created, no critical errors in logs), and that **`level4/config.yml`** uses the Level 4 pipeline (**CompactLLMCommandGenerator**, not SearchReady). Same conventions as Level 3: venv in workspace root, grader runs from root and checks `level4` for model, optional log checks, and parsed pipeline step names.

**Lab workflow:** Students (1) activate venv in project root, (2) `cd level4`, (3) run `python -m rasa train`. The grader script runs from **workspace root** and checks `level4` for model and optional logs.

### Assessment Type

**Standard Code Test** (Python script)

### Grader Script Location

```
.guides/secure/level4_graders/lab_5.1_grader.py
```

### Grader Script

The grader runs from **workspace root** (`/home/codio/workspace`): it verifies the venv exists, then checks `level4` for model files. Checks:

1. **Check 1 – Virtual environment** (2 pts): `.venv` exists in workspace root and Python is available.
2. **Check 2 – Model file exists** (2 pts): at least one `.tar.gz` in `level4/models/`.
3. **Check 3 – Model recent** (3 pts): newest model is under 10 minutes old (warnings / **PARTIAL** if older).
4. **Check 4 – Logs** (3 pts): if `level4/logs/logs.out` exists, check for error/exception/failed; if no log file, pass (**PARTIAL** if errors suspected).
5. **Check 5 – Pipeline in config.yml** (2 pts): `level4/config.yml` parses as YAML; **`pipeline:`** step `name`s include **`CompactLLMCommandGenerator`** and do **not** include **`SearchReadyLLMCommandGenerator`** (Level 4; avoids wrong slot commands baked into the model).

**Total: 12 points.** **Lab 6.2-style:** **` PASS: Lab 5.1 verification complete! Score: 12/12`** and exit **0** only on full score; checks 3–4 may print **⚠️ PARTIAL** (substring `Check N: PASSED` missing → assessment not fully passed).

### Codio configuration (Standard Code Test)

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level4_graders/lab_5.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty**.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **12**. Enable **Allow partial points** if desired.
   - **Sequence:** From `code-output-compare-401050001.json`: `Check 1: PASSED` … `Check 5: PASSED`, **`showFeedback`: false**, substring match.
   - **SHOW RATIONALE TO STUDENT:** **AFTER [1] ATTEMPTS** (or **ALWAYS**).
   - **RATIONALE:** The grader verifies the virtual environment in project root, that a model file (`.tar.gz`) exists in `level4/models/`, that the model is recent, that logs do not show critical errors, and that `level4/config.yml` uses **CompactLLMCommandGenerator** in the pipeline (not SearchReady). Ensure you ran `python -m rasa train` from the `level4` folder with the venv activated after aligning `config.yml` with Unit 0.2.
4. **Files.** Script at `.guides/secure/level4_graders/lab_5.1_grader.py`; run from workspace.
