#!/bin/bash
# Lab 3.1: Step-by-Step: Creating an Action
# Verifies the Level 2 actions setup (actions folder and example action_bank_hours.py).
cd /home/codio/workspace/level2

score=0
max_score=4

echo "Running Lab 3.1 Assessment Checks..."
echo ""

# Check 1: actions folder exists (2 points)
echo "Check 1: Verifying actions folder exists..."
if [ ! -d "actions" ]; then
    echo "❌ Check 1: FAILED - actions/ folder not found (0 points)"
    echo "Hint: Ensure you are in the level2 folder and have the Level 2 project structure."
else
    echo " Check 1: PASSED - actions folder exists (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 2: action_bank_hours.py exists (2 points) - the example file from the step-by-step
echo "Check 2: Verifying action_bank_hours.py (example action) exists..."
if [ ! -f "actions/action_bank_hours.py" ]; then
    echo "❌ Check 2: FAILED - actions/action_bank_hours.py not found (0 points)"
    echo "Hint: The example action file should be in the actions/ folder. If you started from Chapter 1.1 end state, add the Level 2 starter files or create action_bank_hours.py from the reference in this lab."
else
    echo " Check 2: PASSED - action_bank_hours.py exists (2 points)"
    score=$((score + 2))
fi
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo " PASS: Lab 3.1 setup verified! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the checks above."
fi
echo "=========================================="
echo ""
echo "Summary: Check 1 (actions folder) | Check 2 (action_bank_hours.py)"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi
