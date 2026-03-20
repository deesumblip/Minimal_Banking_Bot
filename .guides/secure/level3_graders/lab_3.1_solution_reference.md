# Lab 3.1 – Reference solution for LLM Rubric Autograde

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 3.1 (Defining a Slot in the Domain).

**Standard Code Test:** The Python grader (`.guides/secure/level3_graders/lab_3.1_grader.py`) follows the **Chapter 1.2 Lab 6.2** template (`lab_4.1_grader.sh`): **Check 1–8** (1-based), **PASSED** lines with a **leading space** (no emoji on pass), **❌** / **⚠️** on fail/partial, **`==========================================`** band, then **` PASS: Lab 3.1 verification complete! Score: 10/10`** on full score.

**Codio Code Output Compare:** `code-output-compare-3187585640.json` uses the same **sequence** pattern as **`code-output-compare-1597644299`** (Lab 6.2): **`Check 1: PASSED`** through **`Check 8: PASSED`**, **`showFeedback`: false**, **`showGuidanceAfterResponseOption`: Never**, **`showExpectedAnswerOption`: Always**.

---

## Required changes in level3/domain/basics.yml

1. **slots: section** – Add a `slots:` section (before or after other top-level keys). It must contain at least the `account` slot.

2. **account slot** – The slot must be named `account` and have `type: text` (or equivalent valid slot type). Example:

```yaml
slots:
  account:
    type: text
```

3. **utter_ask_account response** – Under `responses:`, add a response named `utter_ask_account` with at least one message (e.g. "What is your account number?"). Example:

```yaml
responses:
  # ... other responses ...
  utter_ask_account:
    - text: "What is your account number?"
      metadata:
        rephrase: True
```

4. **actions: list** – The Chapter 1.3 `level3` starter preloads **`action_bank_hours.py`** and **`action_holiday_hours.py`**. The finished `actions:` list includes **`action_bank_hours`**, **`action_holiday_hours`**, and **`action_check_balance_simple`** (Python file for the latter created in Lab 4.1). Example:

```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
  - action_check_balance_simple
```

If the student's domain lists other entries, those may remain; the list must include all three names above.

---

## Rubric summary for autograde

- **slots: section:** Present in domain/basics.yml with valid YAML.
- **account slot:** Present under slots with type text (or equivalent).
- **utter_ask_account:** Present under responses with at least one message.
- **actions: list:** Includes `action_bank_hours`, `action_holiday_hours`, and `action_check_balance_simple`.
- **Valid YAML / structure:** File is valid; existing Level 1 responses and other domain content is preserved.
