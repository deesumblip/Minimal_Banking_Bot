# Verify Lab 0.1 / RASA_LICENSE changes after git pull (Codio)

Run this **in Codio** after `git pull` to confirm the updates were pulled correctly.

## 1. Pull the latest code

```bash
cd /home/codio/workspace
git pull origin main
```

## 2. Quick file checks

Run these and confirm each file exists and (optionally) contains the expected text:

```bash
# Key Lab 0.1 content (should mention RASA_LICENSE only, Codio vs Local)
grep -l "RASA_LICENSE" .guides/content/Chapter-1-1---Just-Responses-d3b4/Unit-0--Prerequisites-and-Setup-1039/Lab-0-1--Create-Virtual-Environment-and-Install-Rasa-Pro-4434.md
grep -q "Set up your own RASA_LICENSE\|Set Up Your Own RASA_LICENSE" .guides/content/Chapter-1-1---Just-Responses-d3b4/Unit-0--Prerequisites-and-Setup-1039/Lab-0-1--Create-Virtual-Environment-and-Install-Rasa-Pro-4434.md && echo "Lab 0.1 content: OK"

# Lab 0.1 Step 5 includes expected file tree (level1 structure)
grep -q "level1/" .guides/content/Chapter-1-1---Just-Responses-d3b4/Unit-0--Prerequisites-and-Setup-1039/Lab-0-1--Create-Virtual-Environment-and-Install-Rasa-Pro-4434.md && grep -q "basics.yml" .guides/content/Chapter-1-1---Just-Responses-d3b4/Unit-0--Prerequisites-and-Setup-1039/Lab-0-1--Create-Virtual-Environment-and-Install-Rasa-Pro-4434.md && echo "Lab 0.1 file tree: OK"

# Prerequisites (no OpenAI API key)
grep -q "Rasa Pro license" .guides/content/Chapter-1-1---Just-Responses-d3b4/Unit-0--Prerequisites-and-Setup-1039/0-1-What-You-Need-Before-Starting-b29b.md && echo "Prerequisites: OK"

# Grader has Step 4 (RASA_LICENSE)
grep -q "Step 4: Verifying RASA_LICENSE" .guides/secure/level1_graders/lab_0.1_grader.py && echo "Grader Step 4: OK"

# Assessment setup mentions 7 points and Step 4
grep -q "Step 4: PASSED" level1/Level1_Lab0.1_Assessment_Setup.md && echo "Assessment setup: OK"

# No OPENAI_API_KEY in Lab 0.1 guide
! grep -q "OPENAI_API_KEY" .guides/content/Chapter-1-1---Just-Responses-d3b4/Unit-0--Prerequisites-and-Setup-1039/Lab-0-1--Create-Virtual-Environment-and-Install-Rasa-Pro-4434.md && echo "Lab 0.1 (no API key): OK"
```

## 3. Optional: run the Lab 0.1 grader

From workspace root (with venv and RASA_LICENSE set if you want a full pass):

```bash
cd /home/codio/workspace
python3 .guides/secure/level1_graders/lab_0.1_grader.py
```

You should see Step 1–4 checks; Step 4 verifies RASA_LICENSE is set (or a non-placeholder in `.env`).

---

After verification, you can delete this file or keep it for future pulls.
