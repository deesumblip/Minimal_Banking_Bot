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
