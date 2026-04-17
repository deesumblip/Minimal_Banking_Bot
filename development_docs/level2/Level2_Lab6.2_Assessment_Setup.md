# Lab 6.2: Training and Testing – Assessment Setup

## Overview

Lab 6.2 reinforces that both actions are registered and verifies that the student has trained the agent. The lab uses the **virtual environment in the main folder** (project root): students go to main folder, activate that venv, then `cd level2` and train/run the Level 2 agent from there so Rasa uses level2's domain, flows, and actions. Steps separate **In Codio** (Linux) from **Running locally** (Windows/macOS/Linux).

**Lab 6.2 has its own graded assessment.** It runs the Lab 4.1 grader (domain registration) and additionally verifies that the student has trained the agent (a model file exists in `level2/models/`). Students run this assessment after completing Lab 4.1 (Unit 4) and Lab 6.1 (training). The lab is placed in Unit 6 right after Lab 6.1.

### Assessment Type

**Code Output Compare** – Runs `lab_4.2_grader.sh`, which:
1. Runs all Lab 4.1 checks (both actions in `domain/basics.yml`).
2. Verifies at least one `*.tar.gz` model file exists in `level2/models/`.

**Task ID (Codio)**: `code-output-compare-1597644299`  
**Assessment JSON**: `.guides/assessments/code-output-compare-1597644299.json`  
**Grader script**: `.guides/secure/level2_graders/lab_4.2_grader.sh`  
**Points**: 11

### Codio Setup

1. Create a **Code Test** (code-output-compare) for Lab 6.2.
2. **Execution** – Command (run from workspace):
   ```bash
   bash /home/codio/workspace/.guides/secure/level2_graders/lab_4.2_grader.sh
   ```
   Do **not** upload or paste the script into the assessment; run it from the workspace so `git pull` keeps the grader in sync.
3. Configure expected output / sequence per `.guides/assessments/code-output-compare-1597644299.json` (e.g. expected substring: `PASS: Action registration verification complete!`).
4. **Points**: 11. Enable **Learning Analytics** if desired.

### Check It! Tag (Level 2 guide)

The Lab 6.2 page in the Level 2 Codio guide (Unit 6, right after Lab 6.1) includes:
`{Check It!|assessment}(code-output-compare-1597644299)`  
so students can run the assessment from the guide.

---

