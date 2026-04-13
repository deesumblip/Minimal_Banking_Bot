# Lab 0.1: Pipeline Config and Endpoints — Assessment Setup

## Guide Content (For Students)

**Placement.** **Unit 0** (Level 4 / Level 4), after **0.2 What Level 4 Adds**. Students complete **fill-in-the-blanks**, paste into **`level4/config.yml`** and **`level4/endpoints.yml`**, then run the **Code Test**. Same pattern as **Lab 3.1** (blanks → paste → grader).

**Codio guide.** The **Lab 0.1** page (Unit 0 in Level 4) includes `{Check It!|assessment}(fill-in-the-blanks-401010010)` and `{Check It!|assessment}(code-output-compare-401010001)`.

---

## Assessment Setup (For Implementers)

### Overview

Two assessments: **Fill in the Blanks** (5 points), then **Standard Code Test** (10 points). The grader verifies `assistant_id`, **Compact** command generator, **flow_retrieval**, **nlg**, and **model_groups** (see **`lab_0.1_grader.py`**).

The grader uses **Python stdlib only** (no PyYAML import), matching **Level 1 Lab 2.2** (`lab_2.2_grader.py`), so the **Code Test** still runs if Codio uses plain `python3` without the project venv. **Recommended:** use the venv interpreter in **COMMAND** anyway (consistent with **Level 3 Lab 3.1** and **Level 4 Lab 2.1**).

### Fill in the Blanks

- **JSON:** `.guides/assessments/fill-in-the-blanks-401010010.json`
- **Points:** 5 (Codio)

### Standard Code Test

**Grader script location (in repo):**

```
.guides/secure/level4_graders/lab_0.1_grader.py
```

**Codio configuration (Standard Code Test):**

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** Use the project venv’s Python for consistency with other labs:  
     `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level4_graders/lab_0.1_grader.py`  
     Leave **Pre-Exec** empty when using this.  
     **Alternative:** Plain `python3` works for this grader (no PyYAML required):  
     `python3 /home/codio/workspace/.guides/secure/level4_graders/lab_0.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty** when using the venv Python path in **COMMAND**. Codio often runs pre-exec and **COMMAND** in separate shells, so activating the venv in pre-exec may not affect the grader process. Using **`.venv/bin/python3`** in **COMMAND** avoids that (same pattern as **Level 3 Lab 3.1**).
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** **10** (or match your course scale).
   - **Sequence / test cases:** Import from **`.guides/assessments/code-output-compare-401010001.json`**: `Check 1: PASSED` … `Check 5: PASSED`, substring match.
   - **SHOW RATIONALE TO STUDENT:** Optional; e.g. **AFTER [1] ATTEMPTS**.

**JSON:** `.guides/assessments/code-output-compare-401010001.json`

### Reference

- **Solution reference:** instructor rubric input alongside **`lab_0.1_grader.py`** in **`.guides/secure/level4_graders/`**

**Files.** The script lives in the repo at **`.guides/secure/level4_graders/lab_0.1_grader.py`**. Do **not** upload or paste it into the assessment; the **Execution** command runs this file from the workspace so `git pull` keeps the grader in sync.
