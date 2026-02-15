# Lab 4.2: Multiple Actions – Assessment Setup

## Overview

Lab 4.2 reinforces that both actions are registered and adds optional Inspector exploration. The **testable instruction** is that registration is complete (same as Lab 4.1). The optional "Review in Inspector" steps are not graded. This assessment reuses the Lab 4.1 verification so students who completed Lab 4.1 will pass Lab 4.2; it gives a second checkpoint if you want one.

### Assessment Type

**Standard Code Test** (Bash script; script invokes the Lab 4.1 grader)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level2_graders/lab_4.2_grader.sh
```

## Grader Script

The Lab 4.2 grader invokes the Lab 4.1 grader. It verifies the same deliverable: `domain/basics.yml` has an `actions:` section with both `action_bank_hours` and `action_holiday_hours` and valid YAML. Optional Inspector steps are not checked.

```bash
#!/bin/bash
# Lab 4.2 verifies the same deliverable as Lab 4.1: both actions registered in the domain.
# Lab 4.2 is recap + optional Inspector; the only testable instruction is that registration is complete.
cd /home/codio/workspace
exec bash .guides/assessments/level2_graders/lab_4.1_grader.sh
```

## Assessment Setup and Configuration

1. **Navigate** to the Lab 4.2 section in the Codio Guide Editor.

2. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure each tab as follows.

   **General** – Name: *Lab 4.2: Multiple Actions*. Description: *Verify that both actions are registered in the domain (same verification as Lab 4.1); optional Inspector steps are ungraded*. Points: `11`. Language: `Bash`.

   **Execution** – COMMAND: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_4.2_grader.sh`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace/level2` (or leave default; the 4.1 script changes to level2).

   **Grading**
   - **Points**: `11` – Same as Lab 4.1 (verification is identical).
   - **Allow partial points**: `OFF` – Single run; pass/fail from the invoked script.
   - **Use maximum score**: `OFF` – No cap.
   - **Case insensitive**: `ON` – Output comparison ignores letter case.
   - **Ignore white spaces**: `ON` – Extra spaces or newlines do not cause failure.
   - **Substring match**: `ON` – Pass if the expected string appears in the output.
   - **Test case** (one case):
     - **INPUT – Arguments**: leave empty – No command-line arguments.
     - **INPUT – STDIN**: leave empty – No stdin.
     - **Expected output**: ` PASS: Action registration verification complete!` (include the leading space) – Same as Lab 4.1; the 4.2 script runs the 4.1 grader.
   - **Show expected answer**: `ALWAYS` – Students can see the required output phrase after submission.
   - **Show rationale to student**: `NEVER` (or as desired)
   - **Defined number of attempts**: `OFF` – No limit on submission attempts (or set if desired).
   - **Rationale** (optional): e.g. *Lab 4.2 assessment reuses Lab 4.1 verification (both actions registered). Optional Inspector review is not graded.*

   **Files** – Create the grader script at `.guides/assessments/level2_graders/lab_4.2_grader.sh`. In the Codio workspace terminal (from the workspace root), make it executable: `chmod +x .guides/assessments/level2_graders/lab_4.2_grader.sh`.

3. **Save & Test** the assessment. Enable **Learning Analytics** if desired.

---
