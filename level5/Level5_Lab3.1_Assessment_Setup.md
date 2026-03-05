# Lab 3.1: Registering Tools in endpoints.yml - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 3 (Registering Tools), Level 5.

**Task.** Add a `tools:` section to `level5/endpoints.yml` with `tools_module: "tools"`. Run the assessment when done.

**Codio guide (Chapter 1.5).** The Lab 3.1 page in the Chapter 1.5 guide includes: `{Check It!|assessment}(code-output-compare-501030001)`. Assessment JSON: `.guides/assessments/code-output-compare-501030001.json`.

---

## Assessment Setup (For Implementers)

### Overview

Verifies that `level5/endpoints.yml` contains a top-level `tools:` key and `tools_module: "tools"`.

### Assessment Type

**LLM Rubric** or **Code Test**.

### Option A: LLM Rubric

Solution reference: `.guides/secure/level5_graders/lab_3.1_solution_reference.md`. Criteria: tools section present; tools_module: "tools". Points: 10. Files: `/home/codio/workspace/level5/endpoints.yml`.

### Option B: Code Test

Grader: `.guides/secure/level5_graders/lab_3.1_grader.py`. Checks: endpoints.yml exists; valid YAML; key "tools" present; "tools_module" with value "tools". COMMAND: `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level5_graders/lab_3.1_grader.py`. WD: `/home/codio/workspace`. Expected: `PASS`.
