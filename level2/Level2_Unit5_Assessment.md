# Lab 5.1: Using Actions in Flows

## Guide Content (For Students)

**Placement**: This lab follows Unit 5: Using Actions in Flows.

---

### Your Task

1. **Example flow** – Ensure the `hours` flow exists in `data/basics/hours.yml` and uses `action_bank_hours` (your starter may already include this).
2. **Your flow** – Create `data/basics/holiday_hours.yml` with a flow that uses **action_holiday_hours** (the action you created in Lab 3.1). The flow should have:
   - A flow id (e.g. `holiday_hours`)
   - `name:` and `description:` so the LLM can match questions about holiday hours
   - `steps:` with `- action: action_holiday_hours`

---

### Verification

Before submitting, confirm:

- `hours.yml` has the `hours` flow and calls `action_bank_hours`
- `holiday_hours.yml` exists, has a flow (e.g. `holiday_hours`), and calls `action_holiday_hours`

Run the assessment when you're done.

#### Review in Inspector

Train your bot, then open the Rasa Inspector GUI (see Unit 6.3). Use the questions from Unit 5.2 (hours, holiday hours, hello) and check that the bot's replies and the triggered flow/action match. If a question doesn't trigger the right flow, check the flow's `description` and that you re-trained after adding or changing flows.

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students can create flow files that use actions: the example `hours.yml` (action_bank_hours) and their own `holiday_hours.yml` (action_holiday_hours), with correct YAML structure.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level2_graders/lab_5.1_grader.sh
```

## Grader Script

```bash
#!/bin/bash
cd /home/codio/workspace/level2

score=0
max_score=15

echo "Running Lab 5.1 Assessment Checks..."
echo ""

# Check 0: Virtual environment exists and is activated (1 point)
echo "Check 0: Verifying virtual environment..."
if [ ! -d ".venv" ]; then
    echo "❌ Check 0: FAILED - Virtual environment (.venv) not found (0 points)"
    echo "Hint: Create virtual environment with 'python3.11 -m venv .venv'"
else
    source .venv/bin/activate 2>/dev/null || true
    echo " Check 0: PASSED - Virtual environment found and activated (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 1: hours.yml file exists in data/basics/ (2 points)
echo "Check 1: Verifying hours.yml flow file exists..."
if [ ! -f "data/basics/hours.yml" ]; then
    echo "❌ Check 1: FAILED - data/basics/hours.yml not found (0 points)"
    echo "Hint: Create hours.yml in the data/basics/ folder"
else
    echo " Check 1: PASSED - hours.yml file exists (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 2: Flow file has flows: section (1 point)
echo "Check 2: Verifying flows: section exists..."
if [ -f "data/basics/hours.yml" ] && grep -q "^flows:" data/basics/hours.yml 2>/dev/null; then
    echo " Check 2: PASSED - flows: section found (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 2: FAILED - flows: section not found (0 points)"
    echo "Hint: Add 'flows:' section to hours.yml"
fi
echo ""

# Check 3: hours flow exists (1 point)
echo "Check 3: Verifying hours flow exists..."
if [ -f "data/basics/hours.yml" ] && grep -q "^  hours:" data/basics/hours.yml 2>/dev/null; then
    echo " Check 3: PASSED - hours flow found (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 3: FAILED - hours flow not found (0 points)"
    echo "Hint: Add 'hours:' flow under flows: section"
fi
echo ""

# Check 4: Flow has name and description (2 points)
echo "Check 4: Verifying flow has name and description..."
if [ -f "data/basics/hours.yml" ] && grep -q "name:" data/basics/hours.yml 2>/dev/null && grep -q "description:" data/basics/hours.yml 2>/dev/null; then
    echo " Check 4: PASSED - Flow has name and description (2 points)"
    score=$((score + 2))
else
    echo "⚠️  Check 4: PARTIAL - Flow missing name or description (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 5: Flow has steps: section (1 point)
echo "Check 5: Verifying flow has steps: section..."
if [ -f "data/basics/hours.yml" ] && grep -q "steps:" data/basics/hours.yml 2>/dev/null; then
    echo " Check 5: PASSED - steps: section found (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 5: FAILED - steps: section not found (0 points)"
    echo "Hint: Add 'steps:' section to the hours flow"
fi
echo ""

# Check 6: Flow uses action_bank_hours (2 points)
echo "Check 6: Verifying flow uses action_bank_hours..."
if [ -f "data/basics/hours.yml" ] && grep -q "action_bank_hours" data/basics/hours.yml 2>/dev/null; then
    if awk '/steps:/,/^[a-z]/ {if (/action_bank_hours/) found=1} END {exit !found}' data/basics/hours.yml 2>/dev/null; then
        echo " Check 6: PASSED - action_bank_hours is used in steps (2 points)"
        score=$((score + 2))
    else
        echo "⚠️  Check 6: PARTIAL - action_bank_hours found but may not be in steps (1 point)"
        score=$((score + 1))
    fi
else
    echo "❌ Check 6: FAILED - action_bank_hours not found in flow (0 points)"
    echo "Hint: Add '- action: action_bank_hours' under steps:"
fi
echo ""

# Check 7: holiday_hours.yml exists (2 points)
echo "Check 7: Verifying holiday_hours.yml flow file exists..."
if [ ! -f "data/basics/holiday_hours.yml" ]; then
    echo "❌ Check 7: FAILED - data/basics/holiday_hours.yml not found (0 points)"
    echo "Hint: Create holiday_hours.yml in the data/basics/ folder (flow for your action from Lab 3.1)"
else
    echo " Check 7: PASSED - holiday_hours.yml file exists (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 8: holiday_hours.yml has flows:, flow id holiday_hours, and uses action_holiday_hours (2 points)
echo "Check 8: Verifying holiday_hours flow structure..."
if [ -f "data/basics/holiday_hours.yml" ] && grep -q "^flows:" data/basics/holiday_hours.yml 2>/dev/null && grep -q "^  holiday_hours:" data/basics/holiday_hours.yml 2>/dev/null && grep -q "action_holiday_hours" data/basics/holiday_hours.yml 2>/dev/null; then
    if grep -q "steps:" data/basics/holiday_hours.yml 2>/dev/null; then
        echo " Check 8: PASSED - holiday_hours.yml has flows, holiday_hours flow, and uses action_holiday_hours (2 points)"
        score=$((score + 2))
    else
        echo "⚠️  Check 8: PARTIAL - flow found but steps: may be missing (1 point)"
        score=$((score + 1))
    fi
else
    echo "❌ Check 8: FAILED - holiday_hours.yml needs flows:, a flow named holiday_hours:, and - action: action_holiday_hours (0 points)"
    echo "Hint: Add flows: then '  holiday_hours:' with name:, description:, steps: and - action: action_holiday_hours"
fi
echo ""

# Check 9: holiday_hours flow has name and description (1 point)
echo "Check 9: Verifying holiday_hours flow has name and description..."
if [ -f "data/basics/holiday_hours.yml" ] && grep -q "name:" data/basics/holiday_hours.yml 2>/dev/null && grep -q "description:" data/basics/holiday_hours.yml 2>/dev/null; then
    echo " Check 9: PASSED - Flow has name and description (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 9: FAILED - Flow missing name or description (0 points)"
    echo "Hint: Add name: and description: to your holiday_hours flow so the LLM can match user questions"
fi
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo " PASS: Flow creation verification complete! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
fi
echo "=========================================="
echo ""
echo "Summary: Check 0 (venv) | Check 1-6 (hours.yml) | Check 7-9 (holiday_hours.yml)"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi
```

## Assessment Setup and Configuration

1. **Navigate** to the Lab 5.1 section in the Codio Guide Editor.

2. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure each tab as follows.

   **General** – Name: *Lab 5.1: Using Actions in Flows*. Description: *Verify that students can create flows that use actions (hours.yml and holiday_hours.yml)*. Points: `15`. Language: `Bash`.

   **Execution** – COMMAND: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_5.1_grader.sh`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace/level2`.

   **Grading** – Points: `15`. Allow partial points: `OFF`. Use maximum score: `OFF`. Case insensitive: `ON`. Ignore white spaces: `ON`. Substring match: `ON`. One test case: **INPUT – Arguments** and **INPUT – STDIN** empty; **Expected output**: ` PASS: Flow creation verification complete!` (include the leading space). Show expected answer: `ALWAYS`. Show rationale to student: `NEVER` (or as desired). Defined number of attempts: `OFF`. **Rationale** (optional): e.g. *The grader checks that `data/basics/hours.yml` and `data/basics/holiday_hours.yml` exist and define flows that use the correct actions.*

   **Files** – Create the grader script at `.guides/assessments/level2_graders/lab_5.1_grader.sh` and make it executable: `chmod +x .guides/assessments/level2_graders/lab_5.1_grader.sh`.

3. **Save & Test** the assessment. Enable **Learning Analytics** if desired.

---
