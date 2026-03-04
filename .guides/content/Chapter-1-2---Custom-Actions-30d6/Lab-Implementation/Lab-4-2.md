# Lab 4.2: Multiple Actions – Assessment Setup

## Overview

Lab 4.2 reinforces that both actions are registered and adds optional Inspector exploration (train, run Inspector, try questions). The lab uses the **virtual environment in the main folder** (project root): students go to main folder, activate that venv, then `cd level2` and train/run the Level 2 bot from there.

**Lab 4.2 has a graded assessment.** It verifies (1) the same domain registration as Lab 4.1 (both actions in `domain/basics.yml`) and (2) that the student has run training (a model file exists in `level2/models/`). The guide includes a Check It! tag that runs the Lab 4.2 grader.

### Assessment Type

**Standard Code Test** – Run the grader script from workspace root.

- **Grader script:** `.guides/secure/level2_graders/lab_4.2_grader.sh`
- **Command:** `bash /home/codio/workspace/.guides/secure/level2_graders/lab_4.2_grader.sh`
- **Working directory:** `/home/codio/workspace`
- **Expected output (substring):** `PASS: Action registration verification complete!`
- **Task ID (for Check It! tag):** `code-output-compare-1597644299`

Configure in Codio as a Code Test with substring match so that when the grader prints the PASS line (after domain and training checks), the assessment passes.

---
