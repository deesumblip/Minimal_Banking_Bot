# Lab 3.1: Creating Your First Action - Assessment Setup

## Overview

This assessment verifies that students can create a custom action file with the correct structure, imports, and methods.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level2_graders/lab_3.1_grader.sh
```

## Grader Script

```bash
#!/bin/bash
cd /home/codio/workspace/level2

score=0
max_score=11

echo "Running Lab 3.1 Assessment Checks..."
echo ""

# Check 0: Virtual environment exists and is activated (2 points)
echo "Check 0: Verifying virtual environment..."
if [ ! -d ".venv" ]; then
    echo "❌ Check 0: FAILED - Virtual environment (.venv) not found (0 points)"
    echo "Hint: Create virtual environment with 'python3.11 -m venv .venv'"
else
    source .venv/bin/activate 2>/dev/null || true
    echo "✅ Check 0: PASSED - Virtual environment found and activated (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 1: Actions folder exists (1 point)
echo "Check 1: Verifying actions folder exists..."
if [ ! -d "actions" ]; then
    echo "❌ Check 1: FAILED - actions/ folder not found (0 points)"
    echo "Hint: Create the actions folder with 'mkdir -p actions'"
else
    echo "✅ Check 1: PASSED - actions/ folder exists (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 2: __init__.py exists in actions folder (1 point)
echo "Check 2: Verifying __init__.py exists..."
if [ ! -f "actions/__init__.py" ]; then
    echo "❌ Check 2: FAILED - actions/__init__.py not found (0 points)"
    echo "Hint: Create __init__.py in the actions folder (can be empty)"
else
    echo "✅ Check 2: PASSED - actions/__init__.py exists (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 3: action_bank_hours.py file exists (2 points)
echo "Check 3: Verifying action_bank_hours.py exists..."
if [ ! -f "actions/action_bank_hours.py" ]; then
    echo "❌ Check 3: FAILED - actions/action_bank_hours.py not found (0 points)"
    echo "Hint: Create the action file in the actions/ folder"
else
    echo "✅ Check 3: PASSED - action_bank_hours.py file exists (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 4: Action file has correct imports (2 points)
echo "Check 4: Verifying action file imports..."
if [ -f "actions/action_bank_hours.py" ] && grep -q "from rasa_sdk import Action" actions/action_bank_hours.py 2>/dev/null && grep -q "from rasa_sdk.executor import CollectingDispatcher" actions/action_bank_hours.py 2>/dev/null; then
    echo "✅ Check 4: PASSED - Correct imports found (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 4: FAILED - Missing required imports (0 points)"
    echo "Hint: Import Action from rasa_sdk and CollectingDispatcher from rasa_sdk.executor"
fi
echo ""

# Check 5: Action class inherits from Action (1 point)
echo "Check 5: Verifying Action class structure..."
if [ -f "actions/action_bank_hours.py" ] && grep -q "class ActionBankHours(Action)" actions/action_bank_hours.py 2>/dev/null; then
    echo "✅ Check 5: PASSED - ActionBankHours class inherits from Action (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 5: FAILED - ActionBankHours class not found or doesn't inherit from Action (0 points)"
    echo "Hint: Class should be 'class ActionBankHours(Action):'"
fi
echo ""

# Check 6: name() method exists and returns correct value (1 point)
echo "Check 6: Verifying name() method..."
if [ -f "actions/action_bank_hours.py" ] && grep -q "def name" actions/action_bank_hours.py 2>/dev/null && grep -q "return \"action_bank_hours\"" actions/action_bank_hours.py 2>/dev/null; then
    echo "✅ Check 6: PASSED - name() method exists and returns 'action_bank_hours' (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 6: FAILED - name() method missing or incorrect return value (0 points)"
    echo "Hint: name() method should return 'action_bank_hours'"
fi
echo ""

# Check 7: run() method exists and uses dispatcher.utter_message (1 point)
echo "Check 7: Verifying run() method and message sending..."
if [ -f "actions/action_bank_hours.py" ] && grep -q "def run" actions/action_bank_hours.py 2>/dev/null && grep -q "dispatcher.utter_message" actions/action_bank_hours.py 2>/dev/null; then
    echo "✅ Check 7: PASSED - run() method exists and uses dispatcher.utter_message() (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 7: FAILED - run() method missing or dispatcher.utter_message() not found (0 points)"
    echo "Hint: run() must call dispatcher.utter_message() to send a message to the user"
fi
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo "✅ PASS: Action creation verification complete! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
fi
echo "=========================================="
echo ""
echo "Summary: Check 0 (venv) | Check 1 (actions/) | Check 2 (__init__.py) | Check 3 (action file) | Check 4 (imports) | Check 5 (class) | Check 6 (name()) | Check 7 (run())"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi
```

## Assessment Configuration

### General Tab
- **Name**: Lab 3.1: Creating Your First Action
- **Description**: Verify that students can create a custom action file with correct structure
- **Points**: `11`
- **Language**: `Bash`

### Execution Tab
- **COMMAND**: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_3.1_grader.sh`
- **TIMEOUT**: `60` seconds
- **Working Directory**: `/home/codio/workspace/level2`

### Grading Tab
- **Points**: `11`
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
   - Set Points: `11`
   - Set Language: `Bash`
4. In the **Execution** tab:
   - Set COMMAND: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_3.1_grader.sh`
   - Set TIMEOUT: `60`
   - Set Working Directory: `/home/codio/workspace/level2`
5. In the **Grading** tab:
   - Set Points: `11`
   - Add test case with Expected Output containing "✅ PASS"
   - Set matching to "Contains"
6. In the **Files** tab:
   - Create the grader script at the specified path
   - Make it executable
7. **Save & Test** the assessment
8. Enable **Learning Analytics** if desired

---
