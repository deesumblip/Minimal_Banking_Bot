# Lab 4.4: Training the Level 4 Bot - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 6: Training and Testing (Level 4).

**Structure.** Part 1 (In Codio) and Part 2 (Running locally). Both follow the same order: **activate the virtual environment in the main project folder (root)** first, then **navigate to `level4`**, then train. Run the assessment when done (Part 1 path).

### Your Task (summary)

Activate the virtual environment in the main project folder (root), navigate to `level4`, then train your bot by running:

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

This assessment verifies that students can successfully train their Level 4 bot and that training completes without errors (model file created, no critical errors in logs). Same conventions as Level 3: venv in workspace root, grader runs from root and checks `level4` for model and optional log checks.

**Lab workflow:** Students (1) activate venv in project root, (2) `cd level4`, (3) run `python -m rasa train`. The grader script runs from **workspace root** and checks `level4` for model and optional logs.

### Assessment Type

**Standard Code Test** (Python script)

### Grader Script Location

```
.guides/assessments/level4_graders/lab_4.4_grader.py
```

### Grader Script

The grader runs from **workspace root** (`/home/codio/workspace`): it verifies the venv exists, then checks `level4` for model files. Checks:

1. **Check 0 – Virtual environment** (2 pts): `.venv` exists in workspace root and Python is available.
2. **Check 1 – Model file exists** (2 pts): at least one `.tar.gz` in `level4/models/`.
3. **Check 2 – Model recent** (3 pts): newest model is under 10 minutes old (file modification time).
4. **Check 3 – Logs** (3 pts): if `level4/logs/logs.out` exists, check for error/exception/failed; if no log file, pass.
5. **Check 4 – Training completed** (2 pts): implied by passing above.

**Total: 12 points.** Script must print a line containing `PASS` and `Successfully passed!` on full success. On failure print `FAIL` and exit 1.

### Codio configuration (Standard Code Test)

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/assessments/level4_graders/lab_4.4_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty**.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **12**. Enable **Allow partial points** if desired.
   - **Test case:** One test case. **EXPECTED OUTPUT:** `PASS`. **Enable substring match**.
   - **SHOW RATIONALE TO STUDENT:** **AFTER [1] ATTEMPTS** (or **ALWAYS**).
   - **RATIONALE:** The grader verifies the virtual environment in project root, that a model file (`.tar.gz`) exists in `level4/models/`, that the model is recent, and that logs do not show critical errors. Ensure you ran `python -m rasa train` from the `level4` folder with the venv activated.
4. **Files.** Script at `.guides/assessments/level4_graders/lab_4.4_grader.py`; run from workspace.
