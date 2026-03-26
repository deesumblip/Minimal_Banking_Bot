# Lab 5.2: Completion Check & Testing in Inspector — Assessment Setup

## Guide Content (For Students)

**Placement.** This lab is in **Unit 5: Training and Testing** (Level 4), immediately after **Lab 5.1**. Student-facing instructions for the **graded completion check** and **optional Inspector** steps live on the single **Lab 5.2** guide page (there is no separate Unit 5 “5.2 concept” page).

**Task.** Students run **Check It!** (completion check) first; it verifies domain (including legacy Level 2–3 actions and Level 3 **`account`** / **`utter_ask_account`**), action file, flow file, model, **`level4/config.yml`** pipeline, and **`level4/endpoints.yml`** **`model_groups`** (same pattern as Lab 0.1)—**without** starting Rasa. **Optional:** Start the agent (`rasa inspect` / `rasa run`), open **Rasa Inspect**, walk through the transfer flow, and confirm `action_process_transfer`. Guide page order: Part 1 = assessment, Part 2–3 = Inspector (optional).

**Codio guide (Chapter 1.4).** The Lab 5.2 page in the Chapter 1.4 guide includes: `{Check It!|assessment}(code-output-compare-401050002)`. Assessment JSON: `.guides/assessments/code-output-compare-401050002.json`.

---

## Assessment Setup (For Implementers)

### Overview

This is a **completion check** (not a full run of the agent in Inspector). The grader verifies that the student has completed the full Level 4 build: (1) domain has the three transfer slots plus **`account`**, four ask responses (including **`utter_ask_account`**), **legacy** actions (`action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`), and `action_process_transfer`; (2) `action_process_transfer.py` exists and reads the three transfer slots; (3) `transfer_money.yml` exists with the three collect steps and action step; (4) a model file exists in `level4/models/`; (5) **`level4/config.yml`** uses **CompactLLMCommandGenerator** in **`pipeline:`** (not SearchReady); (6) **`level4/endpoints.yml`** under **`model_groups`**, **`id: gpt-4o-mini`**, uses **`model: gpt-4o-2024-11-20`** and **`temperature: 0.1`** (Unit 0.2 / Lab 0.1). Together these indicate the student can run and test the transfer flow. No live Rasa run is required.

### Assessment Type

**Standard Code Test** (Python script)

### Grader Script Location

```
.guides/secure/level4_graders/lab_5.2_grader.py
```

### Grader Script

The grader runs from **workspace root** (resolved from the script path). It performs the following checks (**2 points each**, **12 total**):

1. **Domain** (2 pts): `level4/domain/basics.yml` has slots `amount`, `recipient`, `account_from`, `account`; responses `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`, `utter_ask_account`; `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`, and `action_process_transfer` in actions list.
2. **Action file** (2 pts): `level4/actions/action_process_transfer.py` exists and contains `get_slot` for `"amount"`, `"recipient"`, `"account_from"` and `name()` returning `"action_process_transfer"`.
3. **Flow file** (2 pts): `level4/data/basics/transfer_money.yml` exists with valid YAML, collect `amount` / `recipient` / `account_from`, and action `action_process_transfer`.
4. **Model** (2 pts): at least one `.tar.gz` in `level4/models/`.
5. **Config pipeline** (2 pts): `level4/config.yml` includes **CompactLLMCommandGenerator** and does not use **SearchReadyLLMCommandGenerator** as a pipeline step `name`.
6. **Endpoints** (2 pts): `level4/endpoints.yml` has **`model_groups`** entry **`id: gpt-4o-mini`** whose first model uses **`model: gpt-4o-2024-11-20`** and **`temperature: 0.1`**.

**Total: 12 points.** **Lab 6.2-style:** **Check 1–6**, **` PASS: Lab 5.2 completion check passed! Score: 12/12`** on full pass; exit **0** only on full score.

### Codio configuration (Standard Code Test)

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level4_graders/lab_5.2_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty**.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **12**. Enable **Allow partial points** if desired.
   - **Sequence:** From `code-output-compare-401050002.json`: `Check 1: PASSED` … `Check 6: PASSED`, **`showFeedback`: false**, substring match.
   - **SHOW RATIONALE TO STUDENT:** **AFTER [1] ATTEMPTS** (or **ALWAYS**).
   - **RATIONALE:** The completion check verifies that your Level 4 agent has: the domain updated with transfer slots, **`account`** and **`utter_ask_account`**, ask responses, legacy custom actions, and `action_process_transfer`; the action file that reads the three transfer slots; the `transfer_money` flow file; a trained model; **`level4/config.yml`** using **CompactLLMCommandGenerator**; and **`level4/endpoints.yml`** **`model_groups`** matching Unit 0.2. If any check fails, fix **Labs 0.1, 2.1, 3.1, or 4.1** as needed, complete **Lab 5.1** (train), then run this assessment again.
4. **Files.** Script at `.guides/secure/level4_graders/lab_5.2_grader.py`; run from workspace.

---

## Reference for rubric / grading

- **Solution reference:** **`.guides/secure/level4_graders/`** (lab 5.2, alongside **`lab_5.2_grader.py`** — describes what “completion” means for each check).
