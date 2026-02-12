# Level 2: Assessment vs Content Alignment

## Lab 3.1: Creating Your First Action

| Content step (Unit 3) | Assessment check | Aligned? |
|-------------------------|------------------|----------|
| Step 1: actions/ folder, __init__.py | Check 1: actions/ exists; Check 2: __init__.py exists | ✅ |
| Step 2: Create action_bank_hours.py | Check 3: action_bank_hours.py exists | ✅ |
| Step 3: Imports (Action, CollectingDispatcher) | Check 4: Correct imports | ✅ |
| Step 3: class ActionBankHours(Action) | Check 5: class inherits from Action | ✅ |
| Step 3: name() returns "action_bank_hours" | Check 6: name() method | ✅ |
| Step 3: run() with dispatcher.utter_message(), return [] | Check 7: def run + dispatcher.utter_message | ✅ (added) |

**Verdict**: Fully aligned (Check 7 added to grader).

---

## Lab 4.1: Registering Actions in the Domain

| Content step (Unit 4) | Assessment check | Aligned? |
|-------------------------|------------------|----------|
| Step 1: Open domain/basics.yml | Check 1: domain/basics.yml exists | ✅ |
| Step 2: Add actions: section, - action_bank_hours | Check 2: actions: section; Check 3: action_bank_hours registered | ✅ |
| Step 3: Proper YAML (indentation, dashes) | Check 4: YAML syntax; Check 5: valid YAML | ✅ |

**Verdict**: Fully aligned.

---

## Lab 5.1: Using Actions in Flows

| Content step (Unit 5) | Assessment check | Aligned? |
|-------------------------|------------------|----------|
| Step 1: Go to data/basics/ | Implicit (file path check) | ✅ |
| Step 2: Create hours.yml with flows:, hours:, name, description, steps, action_bank_hours | Check 1: hours.yml exists; Check 2: flows:; Check 3: hours flow; Check 4: name & description; Check 5: steps:; Check 6: action_bank_hours in steps | ✅ |
| Step 4: Verify structure | Covered by checks above | ✅ |

**Verdict**: Fully aligned.

---

## Lab 6.1: Training and Testing with Actions

| Content step (Unit 6) | Assessment check | Aligned? |
|-------------------------|------------------|----------|
| Run training (venv active, rasa train) | Check 0: .venv exists; Check 1: model file exists; Check 2: model recent | ✅ |
| Model in models/ | Check 1: models/*.tar.gz | ✅ |
| No critical errors | Check 3: logs | ✅ |
| Action file present | Check 4: action_bank_hours.py exists | ✅ |

**Fix applied**: Unit 6 content now says **"cd level2"** for Codio (was "cd level1").

**Verdict**: Fully aligned.

---

## Summary

| Lab | Alignment | Notes |
|-----|-----------|--------|
| 3.1 | Full | Grader includes Check 7: run() and dispatcher.utter_message(); Check 4b: datetime for date-based logic (12 points total) |
| 4.1 | Full | — |
| 5.1 | Full | — |
| 6.1 | Full | Content training command fixed to cd level2 |
