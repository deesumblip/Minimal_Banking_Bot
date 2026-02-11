# Lab 4.1: Registering Actions in the Domain - Assessment Setup

## Overview

This assessment verifies that students can register actions in the domain file with correct YAML syntax and matching action names.

## Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level2_graders/lab_4.1_grader.sh
```

## Grader Script

```bash
#!/bin/bash
set -e
cd /home/codio/workspace/level2

score=0
max_score=10

echo "Running Lab 4.1 Assessment Checks..."
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

# Check 1: domain/basics.yml exists (1 point)
echo "Check 1: Verifying domain file exists..."
if [ ! -f "domain/basics.yml" ]; then
    echo "❌ Check 1: FAILED - domain/basics.yml not found (0 points)"
    echo "Hint: Ensure domain/basics.yml exists"
    exit 1
fi
echo "✅ Check 1: PASSED - domain/basics.yml exists (1 point)"
score=$((score + 1))
echo ""

# Check 2: actions: section exists (2 points)
echo "Check 2: Verifying actions: section exists..."
if grep -q "^actions:" domain/basics.yml; then
    echo "✅ Check 2: PASSED - actions: section found (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 2: FAILED - actions: section not found (0 points)"
    echo "Hint: Add 'actions:' section to domain/basics.yml"
    exit 1
fi
echo ""

# Check 3: action_bank_hours is registered (2 points)
echo "Check 3: Verifying action_bank_hours is registered..."
if grep -q "action_bank_hours" domain/basics.yml; then
    # Check it's under actions: section (look for pattern)
    if awk '/^actions:/,/^[a-z]/ {if (/action_bank_hours/) found=1} END {exit !found}' domain/basics.yml; then
        echo "✅ Check 3: PASSED - action_bank_hours is registered under actions: (2 points)"
        score=$((score + 2))
    else
        echo "⚠️  Check 3: PARTIAL - action_bank_hours found but may not be under actions: section (1 point)"
        score=$((score + 1))
    fi
else
    echo "❌ Check 3: FAILED - action_bank_hours not found in domain file (0 points)"
    echo "Hint: Add '- action_bank_hours' under the actions: section"
    exit 1
fi
echo ""

# Check 4: Correct YAML syntax (indentation and dash) (2 points)
echo "Check 4: Verifying YAML syntax..."
# Check for proper list format (dash followed by space)
if grep -q "^- action_bank_hours" domain/basics.yml || grep -q "^- action_bank_hours" domain/basics.yml; then
    echo "✅ Check 4: PASSED - Correct YAML list syntax (dash format) (2 points)"
    score=$((score + 2))
else
    echo "⚠️  Check 4: PARTIAL - Action registered but may have syntax issues (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 5: Domain file is valid YAML (2 points)
echo "Check 5: Verifying domain file is valid YAML..."
if python3 -c "import yaml; yaml.safe_load(open('domain/basics.yml'))" 2>/dev/null; then
    echo "✅ Check 5: PASSED - domain/basics.yml is valid YAML (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 5: FAILED - domain/basics.yml has YAML syntax errors (0 points)"
    echo "Hint: Check YAML syntax (indentation, colons, dashes)"
    exit 1
fi
echo ""

# Final summary
echo "=========================================="
echo "✅ PASS: Action registration verification complete! Score: $score/$max_score"
echo "=========================================="
echo ""
echo "Summary of checks:"
echo "✓ Check 0: Virtual environment exists and activated"
echo "✓ Check 1: domain/basics.yml exists"
echo "✓ Check 2: actions: section exists"
echo "✓ Check 3: action_bank_hours is registered"
echo "✓ Check 4: Correct YAML syntax"
echo "✓ Check 5: Domain file is valid YAML"
echo ""
echo "✅ PASS: Action registration verification complete! Score: $score/$max_score"
```

## Assessment Configuration

### General Tab
- **Name**: Lab 4.1: Registering Actions in the Domain
- **Description**: Verify that students can register actions in the domain file
- **Points**: `10`
- **Language**: `Bash`

### Execution Tab
- **COMMAND**: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_4.1_grader.sh`
- **TIMEOUT**: `60` seconds
- **Working Directory**: `/home/codio/workspace/level2`

### Grading Tab
- **Points**: `10`
- **Test Cases**: Single test case
- **Expected Output**: Should contain "✅ PASS: Action registration verification complete!"
- **Matching**: Contains (case-insensitive)

### Files Tab
- **Grader Script**: `.guides/assessments/level2_graders/lab_4.1_grader.sh`
- Make sure the script is executable: `chmod +x .guides/assessments/level2_graders/lab_4.1_grader.sh`

## Setup Instructions

1. Navigate to the Lab 4.1 section in Codio Guide Editor
2. Click **Add Code Test** → **Standard Code Test**
3. In the **General** tab:
   - Set Name: "Lab 4.1: Registering Actions in the Domain"
   - Set Points: `10`
   - Set Language: `Bash`
4. In the **Execution** tab:
   - Set COMMAND: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_4.1_grader.sh`
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
