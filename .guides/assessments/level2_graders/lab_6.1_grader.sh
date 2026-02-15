#!/bin/bash
cd /home/codio/workspace/level2

score=0
max_score=10

echo "Running Lab 6.1 Assessment Checks..."
echo ""

# Check 0: Virtual environment exists and is activated (2 points)
echo "Check 0: Verifying virtual environment..."
if [ ! -d ".venv" ]; then
    echo "❌ Check 0: FAILED - Virtual environment (.venv) not found (0 points)"
    echo "Hint: Create virtual environment with 'python3.11 -m venv .venv'"
else
    source .venv/bin/activate 2>/dev/null || true
    echo " Check 0: PASSED - Virtual environment found and activated (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 1: Model file exists (2 points)
echo "Check 1: Verifying model file exists..."
if [ -d "models" ] && [ -n "$(ls -A models/*.tar.gz 2>/dev/null)" ]; then
    echo " Check 1: PASSED - Model file created (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 1: FAILED - No model file found in models/ directory (0 points)"
    echo "Hint: Run 'python -m rasa train' (with venv activated) to create the model"
fi
echo ""

# Check 2: Training completed successfully (check for recent model) (3 points)
echo "Check 2: Verifying model is recent..."
model_file=$(ls -t models/*.tar.gz 2>/dev/null | head -1)
if [ -z "$model_file" ]; then
    echo "❌ Check 2: FAILED - No model files found (0 points)"
    echo "Hint: Run 'python -m rasa train' and wait for it to finish"
elif [ -f "$model_file" ]; then
    model_age=$(( $(date +%s) - $(stat -c %Y "$model_file") ))
    if [ $model_age -lt 600 ]; then
        echo " Check 2: PASSED - Model file is recent (training completed within 10 minutes) (3 points)"
        score=$((score + 3))
    else
        echo "⚠️  WARNING: Model file is old. Re-run training to ensure it's current."
        echo "⚠️  Check 2: PARTIAL - Model exists but is older than 10 minutes (0 points)"
    fi
fi
echo ""

# Check 3: No obvious errors (check for common error patterns in logs if available) (2 points)
echo "Check 3: Checking for errors in logs..."
if [ -f "logs/logs.out" ]; then
    if grep -qi "error\|exception\|failed" logs/logs.out 2>/dev/null; then
        echo "⚠️  WARNING: Possible errors found in logs. Review logs/logs.out"
        echo "⚠️  Check 3: PARTIAL - Logs found but may contain errors (0 points)"
    else
        echo " Check 3: PASSED - No obvious errors in logs (2 points)"
        score=$((score + 2))
    fi
else
    echo " Check 3: PASSED - No log file found (training may not have logged) (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 4: Action file exists and is valid (1 point)
echo "Check 4: Verifying action file exists..."
if [ -f "actions/action_bank_hours.py" ]; then
    echo " Check 4: PASSED - action_bank_hours.py exists (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 4: FAILED - action_bank_hours.py not found (0 points)"
    echo "Hint: Ensure actions/action_bank_hours.py exists (provided in starter). Lab 3.1 adds your action_holiday_hours.py"
fi
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo " PASS: Training verification complete! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
fi
echo "=========================================="
echo ""
echo "Summary: Check 0 (venv) | Check 1 (model exists) | Check 2 (model recent) | Check 3 (no errors) | Check 4 (action file)"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi
