# Lab 4.1: Registering Actions in the Domain

## Guide Content (For Students)

**Placement**: This lab follows Unit 4: Registering Actions in the Domain.

---

### Your Task

Add an `actions:` section to `domain/basics.yml` (if it isn’t already there) and register **both**:

- **action_bank_hours** – the example action you studied in the units  
- **action_holiday_hours** – the action you created in Lab 3.1  

Each action must appear as a list item under `actions:` (e.g. `- action_bank_hours`).

---

### Verification

Before submitting, confirm:

- The file `domain/basics.yml` has an `actions:` section  
- Both `action_bank_hours` and `action_holiday_hours` are listed  
- YAML is valid (correct indentation and dashes)  

Run the assessment when you’re done.

---

#### Review in Inspector (optional)

After the assessment, train and open the Rasa Inspector GUI (see Unit 6.3). In the chat, try **"What are your hours?"** (should work if the `hours` flow exists) and **"What are your holiday hours?"** (likely not yet—you'll add that flow in Unit 5).

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students can register actions in the domain file with correct YAML syntax, including both the example action and the action they created in Lab 3.1.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level2_graders/lab_4.1_grader.sh
```

## Grader Script

```bash
#!/bin/bash
cd /home/codio/workspace/level2

score=0
max_score=12

echo "Running Lab 4.1 Assessment Checks..."
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

# Check 1: domain/basics.yml exists (1 point)
echo "Check 1: Verifying domain file exists..."
if [ ! -f "domain/basics.yml" ]; then
    echo "❌ Check 1: FAILED - domain/basics.yml not found (0 points)"
    echo "Hint: Ensure domain/basics.yml exists"
else
    echo " Check 1: PASSED - domain/basics.yml exists (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 2: actions: section exists (2 points)
echo "Check 2: Verifying actions: section exists..."
if [ -f "domain/basics.yml" ] && grep -q "^actions:" domain/basics.yml 2>/dev/null; then
    echo " Check 2: PASSED - actions: section found (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 2: FAILED - actions: section not found (0 points)"
    echo "Hint: Add 'actions:' section to domain/basics.yml"
fi
echo ""

# Check 3: action_bank_hours is registered (2 points)
echo "Check 3: Verifying action_bank_hours is registered..."
if [ -f "domain/basics.yml" ] && grep -q "action_bank_hours" domain/basics.yml 2>/dev/null; then
    if awk '/^actions:/,/^[a-z]/ {if (/action_bank_hours/) found=1} END {exit !found}' domain/basics.yml 2>/dev/null; then
        echo " Check 3: PASSED - action_bank_hours is registered under actions: (2 points)"
        score=$((score + 2))
    else
        echo "⚠️  Check 3: PARTIAL - action_bank_hours found but may not be under actions: section (1 point)"
        score=$((score + 1))
    fi
else
    echo "❌ Check 3: FAILED - action_bank_hours not found in domain file (0 points)"
    echo "Hint: Add '- action_bank_hours' under the actions: section"
fi
echo ""

# Check 4: action_holiday_hours is registered (2 points)
echo "Check 4: Verifying action_holiday_hours is registered..."
if [ -f "domain/basics.yml" ] && grep -q "action_holiday_hours" domain/basics.yml 2>/dev/null; then
    if awk '/^actions:/,/^[a-z]/ {if (/action_holiday_hours/) found=1} END {exit !found}' domain/basics.yml 2>/dev/null; then
        echo " Check 4: PASSED - action_holiday_hours is registered under actions: (2 points)"
        score=$((score + 2))
    else
        echo "⚠️  Check 4: PARTIAL - action_holiday_hours found but may not be under actions: section (1 point)"
        score=$((score + 1))
    fi
else
    echo "❌ Check 4: FAILED - action_holiday_hours not found in domain file (0 points)"
    echo "Hint: Add '- action_holiday_hours' under the actions: section (the action you created in Lab 3.1)"
fi
echo ""

# Check 5: Correct YAML syntax (indentation and dash) (2 points)
echo "Check 5: Verifying YAML syntax..."
if [ -f "domain/basics.yml" ] && (grep -q "^- action_bank_hours" domain/basics.yml 2>/dev/null || grep -q "^- action_bank_hours" domain/basics.yml 2>/dev/null); then
    echo " Check 5: PASSED - Correct YAML list syntax (dash format) (2 points)"
    score=$((score + 2))
else
    echo "⚠️  Check 5: PARTIAL - Action registered but may have syntax issues (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 6: Domain file is valid YAML (2 points)
echo "Check 6: Verifying domain file is valid YAML..."
if [ -f "domain/basics.yml" ] && python3 -c "import yaml; yaml.safe_load(open('domain/basics.yml'))" 2>/dev/null; then
    echo " Check 6: PASSED - domain/basics.yml is valid YAML (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 6: FAILED - domain/basics.yml has YAML syntax errors or file missing (0 points)"
    echo "Hint: Check YAML syntax (indentation, colons, dashes)"
fi
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo " PASS: Action registration verification complete! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
fi
echo "=========================================="
echo ""
echo "Summary: Check 0 (venv) | Check 1 (domain) | Check 2 (actions:) | Check 3 (action_bank_hours) | Check 4 (action_holiday_hours) | Check 5 (syntax) | Check 6 (valid YAML)"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi
```

## Assessment Setup and Configuration

1. **Navigate** to the Lab 4.1 section in the Codio Guide Editor.

2. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure each tab as follows.

   **General** – Name: *Lab 4.1: Registering Actions in the Domain*. Description: *Verify that students can register actions in the domain file (both action_bank_hours and action_holiday_hours)*. Points: `12`. Language: `Bash`.

   **Execution** – COMMAND: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_4.1_grader.sh`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace/level2`.

   **Grading** – Points: `12`. Allow partial points: `OFF`. Use maximum score: `OFF`. Case insensitive: `ON`. Ignore white spaces: `ON`. Substring match: `ON`. One test case: **INPUT – Arguments** and **INPUT – STDIN** empty; **Expected output**: ` PASS: Action registration verification complete!` (include the leading space). Show expected answer: `ALWAYS`. Show rationale to student: `NEVER` (or as desired). Defined number of attempts: `OFF`. **Rationale** (optional): e.g. *The grader checks that `domain/basics.yml` has an `actions:` section listing both `action_bank_hours` and `action_holiday_hours` with valid YAML.*

   **Files** – Create the grader script at `.guides/assessments/level2_graders/lab_4.1_grader.sh` and make it executable: `chmod +x .guides/assessments/level2_graders/lab_4.1_grader.sh`.

3. **Save & Test** the assessment. Enable **Learning Analytics** if desired.

---
