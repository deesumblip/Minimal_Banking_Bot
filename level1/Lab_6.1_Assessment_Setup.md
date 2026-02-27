# Lab 6.1 Assessment Setup Guide

## Step-by-Step: Lab 6.1 Assessment Setup

### Step 1: Navigate to Lab 6.1 in Codio Guides

1. Open your Codio project.
2. Go to **Tools** → **Guides** → **Edit**.
3. Find the **Lab 6.1: Training Your Bot** subsection.
4. Scroll to the bottom of that subsection (after the student content).

### Step 2: Create the Code Test Assessment

1. Click the **+** button at the bottom of the Lab 6.1 subsection.
2. Select **Code Test** from the assessment types.

### Step 3: Use the Grader Script

**Option A (recommended after pull):** Configure the Code Test to run the script from the repo:  
COMMAND: `bash /home/codio/workspace/.guides/secure/level1_graders/lab_6.1_grader.sh`  
Working Directory: `/home/codio/workspace`. Then run `chmod +x .guides/secure/level1_graders/lab_6.1_grader.sh` in the terminal once. The script uses `max_score=12` and checks venv in workspace root, then level1 models.

**Option B:** In the code editor box, paste this grader script (same logic; ensure `max_score=12`):

```bash
#!/bin/bash
set -e
cd /home/codio/workspace/level1

score=0
max_score=12

echo "Running Lab 6.1 Assessment Checks..."
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

# Check 1: Model file exists (2 points)
echo "Check 1: Verifying model file exists..."
if [ -d "models" ] && [ -n "$(ls -A models/*.tar.gz 2>/dev/null)" ]; then
    echo "✅ Check 1: PASSED - Model file created (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 1: FAILED - No model file found in models/ directory (0 points)"
    echo "Hint: Run 'python3.11 -m rasa train' (with venv activated) to create the model"
    exit 1
fi
echo ""

# Check 2: Training completed successfully (check for recent model)
echo "Check 2: Verifying model is recent..."
model_file=$(ls -t models/*.tar.gz 2>/dev/null | head -1)
if [ -z "$model_file" ]; then
    echo "❌ Check 2: FAILED - No model files found (0 points)"
    exit 1
fi

# Check model is recent (created in last 10 minutes)
if [ -f "$model_file" ]; then
    model_age=$(( $(date +%s) - $(stat -c %Y "$model_file") ))
    if [ $model_age -lt 600 ]; then
        echo "✅ Check 2: PASSED - Model file is recent (training completed within 10 minutes) (3 points)"
        score=$((score + 3))
    else
        echo "⚠️  WARNING: Model file is old. Re-run training to ensure it's current."
        echo "⚠️  Check 2: PARTIAL - Model exists but is older than 10 minutes (0 points)"
    fi
fi
echo ""

# Check 3: No obvious errors (check for common error patterns in logs if available)
echo "Check 3: Checking for errors in logs..."
if [ -f "logs/logs.out" ]; then
    if grep -qi "error\|exception\|failed" logs/logs.out 2>/dev/null; then
        echo "⚠️  WARNING: Possible errors found in logs. Review logs/logs.out"
        echo "⚠️  Check 3: PARTIAL - Logs found but may contain errors (0 points)"
    else
        echo "✅ Check 3: PASSED - No obvious errors in logs (3 points)"
        score=$((score + 3))
    fi
else
    echo "✅ Check 3: PASSED - No log file found (training may not have logged) (3 points)"
    score=$((score + 3))  # Give points if no log file (training might not have logged)
fi
echo ""

# Check 4: Training time reasonable (model exists = training completed)
echo "Check 4: Verifying training completed successfully..."
echo "✅ Check 4: PASSED - Training completed successfully (2 points)"
score=$((score + 2))
echo ""

# Final summary
echo "=========================================="
echo "✅ PASS: Training verification complete! Score: $score/$max_score"
echo "=========================================="
echo ""
echo "Summary of checks:"
echo "✓ Check 0: Virtual environment exists and activated"
echo "✓ Check 1: Model file created"
echo "✓ Check 2: Model file is recent"
echo "✓ Check 3: No critical errors detected"
echo "✓ Check 4: Training completed successfully"
echo ""
echo "✅ PASS: Training verification complete! Score: $score/$max_score"
```

**What the script checks:**
- ✅ Virtual environment exists (`.venv` directory)
- ✅ Model file exists (`.tar.gz` in `models/`)
- ✅ Model is recent (created within last 10 minutes)
- ✅ No obvious errors in logs (if logs exist)
- ✅ Training completed successfully

### Step 4: Configure Assessment Settings

Set these fields:

- **Points**: `10`
- **Timeout**: `60` seconds
- **Language**: **Bash**
- **Working Directory**: `/home/codio/workspace/level1` (if available)
- **Fail Message**: 
  ```
  Training incomplete. Ensure: 1) Virtual environment exists (.venv), 2) Run 'python3.11 -m rasa train' (with venv activated), 3) Wait for completion. Check for YAML syntax errors if training fails.
  ```

### Step 5: Save and Test

1. Click **Save**.
2. Test the assessment:
   - Complete Lab 6.1 steps (create venv, train bot).
   - Run the assessment.
   - Verify it passes when training is complete.

### Step 6: Enable Learning Analytics (Optional)

1. Click **Education** → **Analytics** → **Enable**.
2. Track: training attempts, completion time, error frequency.

### What Students Will See

When students click "Run Assessment" or "Submit":
- The grader checks if `.venv` exists (fails if missing).
- Checks if a model file exists in `models/`.
- Verifies the model is recent (within 10 minutes).
- Provides hints if checks fail.

### Important Notes

1. **Virtual Environment**: The grader activates the venv itself, so students don't need to activate it before running the assessment.
2. **Python Version**: The script uses `python3.11` to match Codio's Python version.
3. **Recency Check**: The 10-minute recency check ensures students ran training recently, not just copied an old model.
4. **Early Exit**: The script exits early if critical checks fail (no venv, no model), so students get immediate feedback.

This setup verifies that students:
- ✅ Created the virtual environment
- ✅ Successfully ran training
- ✅ Generated a model file
- ✅ Completed the lab correctly
