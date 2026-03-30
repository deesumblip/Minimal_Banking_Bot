# Lab 5.1: Training - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 5 (Training and Testing), Level 5.

**Task.** From project root activate venv, `cd level5`, run `rasa train`. Run the assessment when done.

**Codio guide (Chapter 1.5).** The Lab 5.1 page in the Chapter 1.5 guide includes: `{Check It!|assessment}(code-output-compare-501050001)`. Assessment JSON: `.guides/assessments/code-output-compare-501050001.json`.

---

## Assessment Setup (For Implementers)

### Overview

Verifies that the student can train from level5 (or that required files are present so training would succeed). Grader may run `rasa train` from level5 or check for domain, data, config, tools, and model output.

### Assessment Type

**Code Test** (Python or shell script).

### Code Test

Grader: `.guides/secure/level5_graders/lab_5.1_grader.py`. **Check 1–4**, Lab 6.2-style; **` PASS: Lab 5.1 verification complete! Score: 10/10`**. Verifies venv, level5 structure, **Lab 2.0** prompt file + `prompt_template` in `config.yml`, and trained model. COMMAND: venv Python + grader. Sequence: `code-output-compare-501050001.json`.
