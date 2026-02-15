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
