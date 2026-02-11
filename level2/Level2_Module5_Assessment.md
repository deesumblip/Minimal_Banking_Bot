# Lab 5.1: Using Actions in Flows - Assessment Setup

## Overview

This assessment verifies that students can create a flow file that uses an action, with correct YAML structure and action reference.

## Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level2_graders/lab_5.1_grader.sh
```

## Grader Script

```bash
#!/bin/bash
set -e
cd /home/codio/workspace/level2

score=0
max_score=10

echo "Running Lab 5.1 Assessment Checks..."
echo ""

# Check 0: Virtual environment exists and is activated (1 point)
echo "Check 0: Verifying virtual environment..."
if [ ! -d ".venv" ]; then
    echo "❌ Check 0: FAILED - Virtual environment (.venv) not found (0 points)"
    echo "Hint: Create virtual environment with 'python3.11 -m venv .venv'"
    exit 1
fi

# Activate venv for checks
source .venv/bin/activate
echo "✅ Check 0: PASSED - Virtual environment found and activated (1 point)"
score=$((score + 1))
echo ""

# Check 1: hours.yml file exists in data/basics/ (2 points)
echo "Check 1: Verifying hours.yml flow file exists..."
if [ ! -f "data/basics/hours.yml" ]; then
    echo "❌ Check 1: FAILED - data/basics/hours.yml not found (0 points)"
    echo "Hint: Create hours.yml in the data/basics/ folder"
    exit 1
fi
echo "✅ Check 1: PASSED - hours.yml file exists (2 points)"
score=$((score + 2))
echo ""

# Check 2: Flow file has flows: section (1 point)
echo "Check 2: Verifying flows: section exists..."
if grep -q "^flows:" data/basics/hours.yml; then
    echo "✅ Check 2: PASSED - flows: section found (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 2: FAILED - flows: section not found (0 points)"
    echo "Hint: Add 'flows:' section to hours.yml"
    exit 1
fi
echo ""

# Check 3: hours flow exists (1 point)
echo "Check 3: Verifying hours flow exists..."
if grep -q "^  hours:" data/basics/hours.yml; then
    echo "✅ Check 3: PASSED - hours flow found (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 3: FAILED - hours flow not found (0 points)"
    echo "Hint: Add 'hours:' flow under flows: section"
    exit 1
fi
echo ""

# Check 4: Flow has name and description (2 points)
echo "Check 4: Verifying flow has name and description..."
if grep -q "name:" data/basics/hours.yml && grep -q "description:" data/basics/hours.yml; then
    echo "✅ Check 4: PASSED - Flow has name and description (2 points)"
    score=$((score + 2))
else
    echo "⚠️  Check 4: PARTIAL - Flow missing name or description (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 5: Flow has steps: section (1 point)
echo "Check 5: Verifying flow has steps: section..."
if grep -q "steps:" data/basics/hours.yml; then
    echo "✅ Check 5: PASSED - steps: section found (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 5: FAILED - steps: section not found (0 points)"
    echo "Hint: Add 'steps:' section to the hours flow"
    exit 1
fi
echo ""

# Check 6: Flow uses action_bank_hours (2 points)
echo "Check 6: Verifying flow uses action_bank_hours..."
if grep -q "action_bank_hours" data/basics/hours.yml; then
    # Check it's in the steps section
    if awk '/steps:/,/^[a-z]/ {if (/action_bank_hours/) found=1} END {exit !found}' data/basics/hours.yml; then
        echo "✅ Check 6: PASSED - action_bank_hours is used in steps (2 points)"
        score=$((score + 2))
    else
        echo "⚠️  Check 6: PARTIAL - action_bank_hours found but may not be in steps (1 point)"
        score=$((score + 1))
    fi
else
    echo "❌ Check 6: FAILED - action_bank_hours not found in flow (0 points)"
    echo "Hint: Add '- action: action_bank_hours' under steps:"
    exit 1
fi
echo ""

# Final summary
echo "=========================================="
echo "✅ PASS: Flow creation verification complete! Score: $score/$max_score"
echo "=========================================="
echo ""
echo "Summary of checks:"
echo "✓ Check 0: Virtual environment exists and activated"
echo "✓ Check 1: hours.yml file exists"
echo "✓ Check 2: flows: section exists"
echo "✓ Check 3: hours flow exists"
echo "✓ Check 4: Flow has name and description"
echo "✓ Check 5: Flow has steps: section"
echo "✓ Check 6: Flow uses action_bank_hours"
echo ""
echo "✅ PASS: Flow creation verification complete! Score: $score/$max_score"
```

## Assessment Configuration

### General Tab
- **Name**: Lab 5.1: Using Actions in Flows
- **Description**: Verify that students can create a flow that uses an action
- **Points**: `10`
- **Language**: `Bash`

### Execution Tab
- **COMMAND**: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_5.1_grader.sh`
- **TIMEOUT**: `60` seconds
- **Working Directory**: `/home/codio/workspace/level2`

### Grading Tab
- **Points**: `10`
- **Test Cases**: Single test case
- **Expected Output**: Should contain "✅ PASS: Flow creation verification complete!"
- **Matching**: Contains (case-insensitive)

### Files Tab
- **Grader Script**: `.guides/assessments/level2_graders/lab_5.1_grader.sh`
- Make sure the script is executable: `chmod +x .guides/assessments/level2_graders/lab_5.1_grader.sh`

## Setup Instructions

1. Navigate to the Lab 5.1 section in Codio Guide Editor
2. Click **Add Code Test** → **Standard Code Test**
3. In the **General** tab:
   - Set Name: "Lab 5.1: Using Actions in Flows"
   - Set Points: `10`
   - Set Language: `Bash`
4. In the **Execution** tab:
   - Set COMMAND: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_5.1_grader.sh`
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
