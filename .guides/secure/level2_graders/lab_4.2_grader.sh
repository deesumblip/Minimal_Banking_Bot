#!/bin/bash
# (Not used by Level 2 Lab 6.2 Codio assessment; that uses lab_6.2_grader.sh for Inspector logs only.)
# Lab 4.2: Multiple Actions – verification that domain is correct AND student has trained
# Runs Lab 4.1 checks (both actions registered), then verifies a model file exists (training was run).

WORKSPACE_ROOT="${CODIO_WORKSPACE:-/home/codio/workspace}"
LAB41_GRADER="$WORKSPACE_ROOT/.guides/secure/level2_graders/lab_4.1_grader.sh"
LEVEL2_MODELS="$WORKSPACE_ROOT/level2/models"

# Run Lab 4.1 grader (domain registration checks)
bash "$LAB41_GRADER"
LAB41_EXIT=$?
if [ $LAB41_EXIT -ne 0 ]; then
    exit 1
fi

# Lab 4.2 additional check: training was run (model file exists)
echo ""
echo "Check 7 (Lab 4.2): Verifying training was run (model file exists)..."
if [ -d "$LEVEL2_MODELS" ] && [ -n "$(find "$LEVEL2_MODELS" -maxdepth 1 -name '*.tar.gz' 2>/dev/null)" ]; then
    echo " Check 7: PASSED - Model file found in level2/models/ (Lab 4.2 complete)"
else
    echo "❌ Check 7: FAILED - No model file in level2/models/ (0 points)"
    echo "Hint: From the project root, activate the venv, then run 'cd level2' and 'python -m rasa train'"
    echo "=========================================="
    echo "❌ FAIL: Lab 4.2 incomplete (domain passed but training not run)."
    exit 1
fi
echo ""
echo "=========================================="
echo " PASS: Action registration verification complete! Lab 4.2 (domain + training) verified."
echo "=========================================="
exit 0
