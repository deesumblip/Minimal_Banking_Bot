# Lab 0.1: Pipeline Config and Endpoints — Assessment Setup

## Guide Content (For Students)

**Placement.** **Unit 0** (Level 4 / Chapter 1.4), after **0.2 What Level 4 Adds**. Students complete **fill-in-the-blanks**, paste into **`level4/config.yml`** and **`level4/endpoints.yml`**, then run the **Code Test**. Same pattern as **Lab 3.1** (blanks → paste → grader).

**Codio guide.** The **Lab 0.1** page (Unit 0 in Chapter 1.4) includes `{Check It!|assessment}(fill-in-the-blanks-401010010)` and `{Check It!|assessment}(code-output-compare-401010001)`.

---

## Assessment Setup (For Implementers)

### Overview

Two assessments: **Fill in the Blanks** (5 points), then **Standard Code Test** (10 points). The grader verifies `assistant_id`, **Compact** command generator, **flow_retrieval**, **nlg**, and **model_groups** (see **`lab_0.1_grader.py`**).

### Fill in the Blanks

- **JSON:** `.guides/assessments/fill-in-the-blanks-401010010.json`
- **Points:** 5 (Codio)

### Standard Code Test

- **Script:** `.guides/secure/level4_graders/lab_0.1_grader.py`
- **COMMAND:** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level4_graders/lab_0.1_grader.py`
- **Working Directory:** `/home/codio/workspace`
- **Timeout:** 60 seconds
- **JSON:** `.guides/assessments/code-output-compare-401010001.json`
- **Sequence:** `Check 1: PASSED` … `Check 5: PASSED`, substring match, **points 10**

### Reference

- **Solution reference:** instructor rubric input alongside **`lab_0.1_grader.py`** in **`.guides/secure/level4_graders/`**
