# Grader Building & Troubleshooting Guidance

Reference for building and fixing Codio lab graders (Level 2 and similar). Pull this when adding new graders or when a grader passes checks but shows the wrong total score on Codio.

---

## 1. Where graders live

- **Path:** `.guides/secure/level2_graders/lab_X.Y_grader.sh`
- **Run context:** Scripts assume they are run with **working directory** = `/home/codio/workspace/level2` (Level 2 labs). The script does `cd /home/codio/workspace/level2` at the top, so all paths in the script are relative to `level2` (e.g. `data/basics/hours.yml`, `domain/basics.yml`).

---

## 2. Codio sync: run from workspace, don’t embed

For grader updates (pushed to GitHub and pulled on Codio) to take effect:

- **Execution** in the Codio Code Test must run the script **from the workspace path**, e.g.  
  `bash /home/codio/workspace/.guides/secure/level2_graders/lab_5.1_grader.sh`
- **Working directory:** `/home/codio/workspace/level2`
- **Do not** upload or paste the script content into the assessment. If the test runs an embedded/uploaded copy, `git pull` will not update what students see.

Document this in assessment setup docs so implementers configure the test to run the file by path.

---

## 3. Codio score arithmetic quirk

On Codio, bash arithmetic can report the wrong total even when every check prints PASSED and per-check variables are correct (e.g. `c1=2 c2=1 c3=2 c4=2 c5=2 c6=1` but `score=10` instead of 12).

**Workaround that works:**

- Use **per-check variables** (e.g. `c1`, `c2`, …) and set their value when the check passes (e.g. `c1=2`, `c2=1`).
- **When all checks pass**, set the total score **directly** instead of summing:
  ```bash
  if [ "$c1" = 2 ] && [ "$c2" = 1 ] && [ "$c3" = 2 ] && ... ; then
    score=12
  else
    score=$(expr $c1 + $c2 + $c3 + ... 2>/dev/null || echo "0")
  fi
  ```
- Avoid relying on a single `score=$((c1 + c2 + ...))` or even `expr` for the **full-pass** case on Codio; use the direct assignment when all expected values are present.

For graders with a small number of checks and low total (e.g. 11 points), cumulative `score=$((score + n))` may still work; if you see a wrong total on Codio, switch to per-check variables + direct score when all pass.

---

## 4. Check logic: keep it simple

- Prefer **simple `grep -q "string"`** checks. Avoid fragile patterns (e.g. long `awk` ranges, complex pipes) that can behave differently in Codio’s environment.
- For “X and Y must both be present”, use:  
  `grep -q "X" file && grep -q "Y" file`
- Use **full points or zero** per check when possible (no PARTIAL) so behavior is easy to reason about and to avoid extra arithmetic.

---

## 5. Script structure (recommended)

```bash
#!/bin/bash
cd /home/codio/workspace/level2

max_score=<total>
c1=0; c2=0; c3=0; ...   # one variable per check

echo "Running Lab X.Y Assessment Checks..."
echo ""

# Check 1: ...
if <condition>; then
  echo " Check 1: PASSED - ... (N points)"
  c1=N
else
  echo "❌ Check 1: FAILED - ..."
  echo "Hint: ..."
fi
echo ""

# ... repeat for each check ...

# Set score (use direct assignment when all pass for Codio)
if [ "$c1" = ... ] && [ "$c2" = ... ] && ... ; then
  score=$max_score
else
  score=$(expr $c1 + $c2 + ... 2>/dev/null || echo "0")
fi

echo "=========================================="
if [ "$score" -eq "$max_score" ]; then
  echo " PASS: ... complete! Score: $score/$max_score"
else
  echo "❌ FAIL: Score $score/$max_score - ..."
fi
echo "=========================================="
echo "Score: $score/$max_score"
[ "$score" -lt "$max_score" ] && exit 1
```

---

## 6. Testing the grader on Codio

In the Codio terminal (from workspace or level2):

```bash
cd /home/codio/workspace/level2 && bash /home/codio/workspace/.guides/secure/level2_graders/lab_5.1_grader.sh
```

Replace `lab_5.1_grader.sh` with the script you’re testing. Confirm:

- All checks that should pass show PASSED.
- The final score matches the expected total (e.g. 12/12).
- If the total is wrong but all checks look correct, add a temporary debug line (e.g. `echo "DEBUG: c1=$c1 c2=$c2 ... => score=$score" >&2`) to verify variable values, then apply the “direct score when all pass” pattern above.

---

## 7. Codio assessment configuration (summary)

- **Execution command:** `bash /home/codio/workspace/.guides/secure/level2_graders/lab_X.Y_grader.sh`
- **Working directory:** `/home/codio/workspace/level2`
- **Expected output (substring):** ` PASS: ... complete!` (with leading space) so the test passes when the script prints the success line.
- **Timeout:** 60 seconds is usually enough.

---

## 8. Reference: graders that work

- **Lab 4.1** – Cumulative `score=$((score + n))`; lower total (11); file/domain checks with `grep`.
- **Lab 5.1** – Per-check variables (`c1`–`c6`); direct `score=12` when all six pass; simple `grep -q` checks; path `level2/data/basics/` for `hours.yml` and `holiday_hours.yml`.

When adding a new grader, mirror the Lab 5.1 pattern (per-check variables + direct score when all pass) to avoid Codio arithmetic issues.

---

## 9. More robust approaches

### Prefer Python for new graders

**Why:** Bash on Codio has shown arithmetic and environment quirks. Python gives predictable arithmetic, no shell differences, and is usually available on Codio as `python3`.

**How:**

- Add a grader script: `.guides/secure/level2_graders/lab_X.Y_grader.py`
- In the script: `os.chdir('/home/codio/workspace/level2')` (or rely on Codio’s working directory), run your checks, keep points in a list or variables, set `score = sum(points)` or `score = c1 + c2 + ...`. Print the **same human-readable output** (e.g. "Check 1: PASSED ...", " PASS: ... complete! Score: 12/12") so the existing Codio test (substring match) still works.
- Codio execution: `python3 /home/codio/workspace/.guides/secure/level2_graders/lab_5.1_grader.py` with working directory `/home/codio/workspace/level2` (or run from repo root if the script does the `chdir`).

**Optional:** Keep a one-line bash wrapper (e.g. `lab_5.1_grader.sh` that does `cd /home/codio/workspace/level2 && exec python3 "$(dirname "$0")/lab_5.1_grader.py"`) so the Codio command can stay `bash .../lab_5.1_grader.sh` while the real logic lives in Python.

### Single source of truth for points

- Define **max_score** and each check’s points in one place at the top (e.g. in bash a comment block or in Python a list/dict). Use those values for both the per-check messages and the final score. Reduces drift and copy-paste errors.

### Standardized final line (optional)

- End the script with a consistent last line, e.g. `Score: $score/$max_score` or `SCORE: $score`. Codio currently matches a substring of the success message; a fixed format makes it easier to add parsing later or to grep in logs.

### When to use bash vs Python

- **Bash:** Fine for very simple graders (few checks, low total, cumulative score works). Use the “direct score when all pass” pattern if the total is wrong on Codio.
- **Python:** Prefer for new graders, especially when there are many checks, non-trivial logic, or you want to avoid Codio bash quirks entirely.
