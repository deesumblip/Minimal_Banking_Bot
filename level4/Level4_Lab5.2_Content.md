**Starting point:** Chapter 1.4 assumes you began with the **final banking agent at the end of Chapter 1.3** and extended it in **`level4/`** (see **Unit 0.1**).

**Objective.** After **Lab 5.1** (training), **Lab 5.2** completes Unit 5: (1) a **graded completion check** that your domain (including legacy actions), action, flow, model, **`level4/config.yml`** pipeline, and **`level4/endpoints.yml`** **`model_groups`** (Lab 0.1 pattern) are correct—the grader does **not** start Rasa or Inspector; (2) **hands-on testing** in **Rasa Inspector** to run the transfer flow and confirm **`action_process_transfer`** and the **free-text recipient** behavior (including the **100-character** cap in code + flow).

**Recommended order:** Pass the completion check first, then use Inspector with the **scripted turns** below.

**Prerequisite.** Finish **Labs 2.1, 3.1, and 4.1**, then **Lab 5.1** (a model must exist under `level4/models/`).

---

## Part 1: Completion check

1. In **Codio**, use **Check It!** for Lab 5.2 (`code-output-compare-401050002`).

The grader checks that:
   - The domain has the three transfer slots, **`account`** and **`utter_ask_account`**, the other ask responses, `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`, and `action_process_transfer` in the actions list (see Lab 2.1)
   - `level4/actions/action_process_transfer.py` exists and reads the three transfer slots
   - `level4/data/basics/transfer_money.yml` exists with the three collect steps and the action step
   - A model file exists in `level4/models/`
   - `level4/config.yml` uses **`CompactLLMCommandGenerator`** in **`pipeline:`** (not **`SearchReadyLLMCommandGenerator`**)
   - `level4/endpoints.yml` — under **`model_groups`**, **`id: gpt-4o-mini`** uses **`model: gpt-4o-2024-11-20`** and **`temperature: 0.1`** (**Unit 0.2** / Lab 0.1)

**Inspector:** If the completion check passes but **Part 2** still mis-fills **recipient**, double-check **`endpoints.yml`** and **`config.yml`** and retrain from **`level4/`**.

2. If any check fails, fix **Labs 2.1, 3.1, or 4.1** as needed, align **`level4/config.yml`** and **`level4/endpoints.yml`** with Unit 0.2, complete **Lab 5.1** (train), then run the assessment again.

---

## Part 2: Rasa Inspector (recommended)

From **`level4`** with the virtual environment active:

1. Start the agent from **`level4`** (after `cd level4`), e.g. `python -m rasa inspect --debug --log-file logs/logs.out` (same pattern as **Lab 5.1**). Use **`python -m rasa …`**, not a global `rasa` binary. Alternatively `python -m rasa run` from **`level4`**.
2. Open **Rasa Inspect** (Codio) or the local URL (e.g. `http://localhost:5005`).

**Scripted transfer (type in order):**

| Step | You type (example) | What to verify |
|------|--------------------|----------------|
| 1 | `Can I transfer some money?` | Transfer flow starts. |
| 2 | `let's say 300 dollars` | Amount collected; agent asks for recipient. |
| 3 | `Alice` (or any short free text) | Recipient stored as plain text; agent asks for account. |
| 4 | `savings` (or e.g. `1234`) | Confirmation from **`action_process_transfer`**: `(Demo) Transfer of $…` |

3. Optionally try balance / hours to confirm other flows still work.

**Troubleshooting:** If the agent says *unable to understand you* during **amount**, **recipient**, or **account** collection:

1. **Domain:** In **`level4/domain/basics.yml`**, set **`metadata: rephrase: False`** on **`utter_ask_amount`**, **`utter_ask_recipient`**, and **`utter_ask_account_from`** (see Lab 2.1).

2. **Flow:** In **`level4/data/basics/transfer_money.yml`**, ensure each **`collect:`** has a clear **`description:`** (Lab 4.1). **Retrain** after edits.

3. **Pipeline:** The **`level4`** repo uses **`CompactLLMCommandGenerator`**. **`SearchReadyLLMCommandGenerator`** (Chapter 1.3) can produce commands like **`set slot transfer_money_amount …`** while your domain only defines **`amount`**—Rasa then rejects the command and you see *unable to understand you*. Confirm **`level4/config.yml`**, **`python -m rasa train`** from **`level4`**, **restart** Inspector. Check logs for **`skip_command_slot_not_in_domain`** with **`transfer_money_*`** vs **`amount`** / **`recipient`**. Background is in **Unit 0.2** (section 2) in Chapter 1.4.

---

## Part 3: Running locally (optional)

Same as Part 2: activate `.venv` at the project root, `cd level4`, `python -m rasa inspect --debug --log-file logs/logs.out` (or `python -m rasa run`), then use the **same table** as above.

---

**Done when:** The completion check passes; Inspector is recommended for confidence.
