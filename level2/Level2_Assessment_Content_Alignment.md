# Level 2: Assessment vs Content Alignment

## Lab 3.1: Creating Your First Action

| Content step (Unit 3) | Assessment check | Aligned? |
|-------------------------|------------------|----------|
| Step 1: actions/ folder, __init__.py | Check 1: actions/ exists; Check 2: __init__.py exists |  |
| Step 2: Create action_bank_hours.py | Check 3: action_bank_hours.py exists |  |
| Step 3: Imports (Action, CollectingDispatcher) | Check 4: Correct imports |  |
| Step 3: class ActionBankHours(Action) | Check 5: class inherits from Action |  |
| Step 3: name() returns "action_bank_hours" | Check 6: name() method |  |
| Step 3: run() with dispatcher.utter_message(), return [] | Check 7: def run + dispatcher.utter_message |  (added) |

**Verdict**: Fully aligned (Check 7 added to grader).

---

## Lab 4.1: Registering Actions in the Domain

| Content step (Unit 4) | Assessment check | Aligned? |
|-------------------------|------------------|----------|
| Step 1: Open domain/basics.yml | Check 1: domain/basics.yml exists |  |
| Step 2: Add actions: section, both actions | Check 2: actions: section; Check 3: action_bank_hours; Check 4: action_holiday_hours |  |
| Step 3: Proper YAML (indentation, dashes) | Check 5: YAML list syntax; Check 6: valid YAML |  |

No venv check. **Verdict**: Fully aligned (11 points).

---

## Lab 5.1: Using Actions in Flows

| Content step (Unit 5) | Assessment check | Aligned? |
|-------------------------|------------------|----------|
| Ensure hours flow in hours.yml, uses action_bank_hours | Check 1: hours.yml exists; Check 2: hours flow; Check 3: action_bank_hours in steps |  |
| Create holiday_hours.yml with flow id, name, description, steps, action_holiday_hours | Check 4: holiday_hours.yml exists; Check 5: flows:, holiday_hours:, steps:, action_holiday_hours; Check 6: name & description (holiday_hours only) |  |

No venv check; name/description required only for holiday_hours flow. **Verdict**: Fully aligned (12 points).

---

## Lab 6.1: Training and Testing with Actions

| Content step (Unit 6) | Assessment check | Aligned? |
|-------------------------|------------------|----------|
| Run training (rasa train); verification: model exists, training completed without errors | Check 1: model file exists in models/; Check 2: no errors in logs |  |

No venv, model recency, or action file checks. **Verdict**: Fully aligned (4 points).

---

## Summary

| Lab | Alignment | Notes |
|-----|-----------|--------|
| 3.1 | Full | Grader includes only what the lab instructs: action file, imports, datetime, class, name(), run() (8 pts) |
| 4.1 | Full | Domain actions section, both actions, valid YAML; no venv (11 pts) |
| 5.1 | Full | hours.yml + holiday_hours.yml flows and actions; name/description only for holiday_hours; no venv (12 pts) |
| 6.1 | Full | Model exists, no errors in logs; no venv, recency, or action file (4 pts) |
