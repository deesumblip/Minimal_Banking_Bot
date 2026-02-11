# Lab 3.1: Creating Your First Action - Assessment Setup

## Overview

This assessment verifies that students can create a custom action file with the correct structure, imports, and methods.

## Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level2_graders/lab_3.1_grader.sh
```

## Grader Script

```bash
#!/bin/bash
set -e
cd /home/codio/workspace/level2

score=0
max_score=10

echo "Running Lab 3.1 Assessment Checks..."
echo ""

# Check 0: Virtual environment exists and is activated (2 points)
echo "Check 0: Verifying virtual environment..."
if [ ! -d ".venv" ]; then
    echo "❌ Check 0: FAILED - Virtual environment (.venv) not found (0 points)"
    echo "Hint: Create virtual environment with 'python3.11 -m venv .venv'"
    exit 1
fi

# Activate venv for checks
source .venv/bin/activate
echo "✅ Check 0: PASSED - Virtual environment found and activated (2 points)"
score=$((score + 2))
echo ""

# Check 1: Actions folder exists (1 point)
echo "Check 1: Verifying actions folder exists..."
if [ ! -d "actions" ]; then
    echo "❌ Check 1: FAILED - actions/ folder not found (0 points)"
    echo "Hint: Create the actions folder with 'mkdir -p actions'"
    exit 1
fi
echo "✅ Check 1: PASSED - actions/ folder exists (1 point)"
score=$((score + 1))
echo ""

# Check 2: __init__.py exists in actions folder (1 point)
echo "Check 2: Verifying __init__.py exists..."
if [ ! -f "actions/__init__.py" ]; then
    echo "❌ Check 2: FAILED - actions/__init__.py not found (0 points)"
    echo "Hint: Create __init__.py in the actions folder (can be empty)"
    exit 1
fi
echo "✅ Check 2: PASSED - actions/__init__.py exists (1 point)"
score=$((score + 1))
echo ""

# Check 3: action_bank_hours.py file exists (2 points)
echo "Check 3: Verifying action_bank_hours.py exists..."
if [ ! -f "actions/action_bank_hours.py" ]; then
    echo "❌ Check 3: FAILED - actions/action_bank_hours.py not found (0 points)"
    echo "Hint: Create the action file in the actions/ folder"
    exit 1
fi
echo "✅ Check 3: PASSED - action_bank_hours.py file exists (2 points)"
score=$((score + 2))
echo ""

# Check 4: Action file has correct imports (2 points)
echo "Check 4: Verifying action file imports..."
if grep -q "from rasa_sdk import Action" actions/action_bank_hours.py && \
   grep -q "from rasa_sdk.executor import CollectingDispatcher" actions/action_bank_hours.py; then
    echo "✅ Check 4: PASSED - Correct imports found (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 4: FAILED - Missing required imports (0 points)"
    echo "Hint: Import Action from rasa_sdk and CollectingDispatcher from rasa_sdk.executor"
    exit 1
fi
echo ""

# Check 5: Action class inherits from Action (1 point)
echo "Check 5: Verifying Action class structure..."
if grep -q "class ActionBankHours(Action)" actions/action_bank_hours.py; then
    echo "✅ Check 5: PASSED - ActionBankHours class inherits from Action (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 5: FAILED - ActionBankHours class not found or doesn't inherit from Action (0 points)"
    echo "Hint: Class should be 'class ActionBankHours(Action):'"
    exit 1
fi
echo ""

# Check 6: name() method exists and returns correct value (1 point)
echo "Check 6: Verifying name() method..."
if grep -q "def name" actions/action_bank_hours.py && \
   grep -q "return \"action_bank_hours\"" actions/action_bank_hours.py; then
    echo "✅ Check 6: PASSED - name() method exists and returns 'action_bank_hours' (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 6: FAILED - name() method missing or incorrect return value (0 points)"
    echo "Hint: name() method should return 'action_bank_hours'"
    exit 1
fi
echo ""

# Final summary
echo "=========================================="
echo "✅ PASS: Action creation verification complete! Score: $score/$max_score"
echo "=========================================="
echo ""
echo "Summary of checks:"
echo "✓ Check 0: Virtual environment exists and activated"
echo "✓ Check 1: actions/ folder exists"
echo "✓ Check 2: __init__.py exists"
echo "✓ Check 3: action_bank_hours.py file exists"
echo "✓ Check 4: Correct imports"
echo "✓ Check 5: Action class inherits from Action"
echo "✓ Check 6: name() method exists and returns correct value"
echo ""
echo "✅ PASS: Action creation verification complete! Score: $score/$max_score"
```

## Assessment Configuration

### General Tab
- **Name**: Lab 3.1: Creating Your First Action
- **Description**: Verify that students can create a custom action file with correct structure
- **Points**: `10`
- **Language**: `Bash`

### Execution Tab
- **COMMAND**: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_3.1_grader.sh`
- **TIMEOUT**: `60` seconds
- **Working Directory**: `/home/codio/workspace/level2`

### Grading Tab
- **Points**: `10`
- **Test Cases**: Single test case
- **Expected Output**: Should contain "✅ PASS: Action creation verification complete!"
- **Matching**: Contains (case-insensitive)

### Files Tab
- **Grader Script**: `.guides/assessments/level2_graders/lab_3.1_grader.sh`
- Make sure the script is executable: `chmod +x .guides/assessments/level2_graders/lab_3.1_grader.sh`

## Setup Instructions

1. Navigate to the Lab 3.1 section in Codio Guide Editor
2. Click **Add Code Test** → **Standard Code Test**
3. In the **General** tab:
   - Set Name: "Lab 3.1: Creating Your First Action"
   - Set Points: `10`
   - Set Language: `Bash`
4. In the **Execution** tab:
   - Set COMMAND: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_3.1_grader.sh`
   - Set TIMEOUT: `60`
   - Set Working Directory: `/home/codio/workspace/level2`
5. In the **Grading** tab:
   - Set Points: `10`
   - Add test case with Expected Output containing "✅ PASS"
   - Set matching to "Contains"
6. In the **Files** tab:
   - Create the grader script at the specified path
   - Make it executable
7. **Save & Test** the assessment
8. Enable **Learning Analytics** if desired

---
