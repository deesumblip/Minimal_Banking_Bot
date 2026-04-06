**Starting point:** Work in **`level4/`** with transfer pieces in place (see **Unit 0.1**).

**Unit 5, Lab 5.2.** You already **trained** the agent in **Lab 5.1**. This lab has two parts in order:

1. **Completion check (graded)**. Confirms domain (including legacy **`account`** / **`utter_ask_account`**), action, flow YAML, trained model, **`config.yml`** pipeline (**`CompactLLMCommandGenerator`**), and **`endpoints.yml`** **`model_groups`** (same pattern as Lab 0.1). The grader **does not** start Rasa or Inspector.
2. **Rasa Inspector (recommended)**. Run the **transfer** flow and confirm **`action_process_transfer`** fires with the expected demo message (free-text **recipient**, **100-character cap** in code + flow).

**Prerequisite:** **Labs 2.1 → 3.1 → 4.1** done, then **Lab 5.1** so `level4/models/` contains a `.tar.gz` file.

---

## Part 1: Completion check (Codio)

1. Use **Check It!** below. The grader verifies:
   - **Domain:** slots `amount`, `recipient`, `account_from`, `account`; `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`, `utter_ask_account`; `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`, and `action_process_transfer` in `actions:` (see Lab 2.1)
   - **Action:** `level4/actions/action_process_transfer.py` reads the three transfer slots (via `get_slot`)
   - **Flow:** `level4/data/basics/transfer_money.yml` has the three `collect:` steps and `action: action_process_transfer`
   - **Model:** at least one `.tar.gz` under `level4/models/`
   - **Config:** `level4/config.yml` **`pipeline:`** uses **`CompactLLMCommandGenerator`** (not **`SearchReadyLLMCommandGenerator`**)
   - **Endpoints:** `level4/endpoints.yml` — under **`model_groups`**, **`id: openai-gpt-5-1`** uses **`model: openai-gpt-5-1`** and **`temperature: 0.1`** (**Unit 0.2** / Lab 0.1)

**Inspector:** If the completion check passes but **Part 2** still mis-fills **recipient**, double-check **`endpoints.yml`** and **`config.yml`** against **Unit 0.2** and retrain from **`level4/`**.

{Check It!|assessment}(code-output-compare-401050002)

2. If a check fails, fix the matching lab (**2.1** domain, **3.1** action, **4.1** flow, **5.1** train / config), then run **Check It!** again.

---

## Part 2: Test in Rasa Inspector (hands-on)

**When:** After Part 1 passes (or whenever you want to see the agent live).

**Where:** From **`level4`** with the project **virtual environment** active (same as Lab 5.1).

### Start the assistant

- `cd` to **`level4`** (same shell pattern as **Lab 5.1**).
- Start Rasa from **`level4`**, for example:
  - `python -m rasa inspect --debug --log-file logs/logs.out` — logs under **`level4/logs/`** for debugging.
  - Or chat-only: `python -m rasa run` from **`level4`**.
- Always use **`python -m rasa …`** from the **venv**, not a global `rasa` binary.
- **Leave the process running** while you use the UI below.

### Open the UI

| Environment | What to do |
|---------------|------------|
| **Codio** | When the terminal shows the server is up, open the **Rasa Inspect** tab. |
| **Local** | Open the URL in the terminal output (often `http://localhost:5005`). |

### Scripted transfer (type in order)

Goal: exercise **amount → recipient → account_from → confirmation** in one thread.

| Step | You type (example) | What you’re checking |
|------|--------------------|----------------------|
| 1 | `Can I transfer some money?` | Agent enters the transfer flow (may greet first). |
| 2 | `let's say 300 dollars` | **Amount** slot filled; agent asks for recipient. |
| 3 | `Alice` *(or any short free text, e.g. `MC hammer`)* | **Recipient** is stored as plain text (up to **100** chars in action + flow); agent asks for source account. |
| 4 | `savings` *(or e.g. `1234`)* | **account_from** filled; agent runs **`action_process_transfer`**. |
| 5 | *(read only)* | Final line should match the demo pattern: **`(Demo) Transfer of $… from account … to … has been processed successfully.`** |

### Optional: other flows

Try **“What’s my balance?”** or **“What are your hours?”** to confirm **check_balance** and **hours** still work with the same **`level4`** model.

### If you see “unable to understand you” during transfer

Work through these in order (domain → flow → pipeline):

1. **Domain** — In **`level4/domain/basics.yml`**, set **`metadata: rephrase: False`** on **`utter_ask_amount`**, **`utter_ask_recipient`**, and **`utter_ask_account_from`** (Lab 2.1).
2. **Flow** — In **`level4/data/basics/transfer_money.yml`**, each **`collect:`** step needs a clear **`description:`** (Lab 4.1: amount; **1–100** chars for recipient; **1–120** for account_from). **Retrain** after edits.
3. **Pipeline** *(most common for repeated failures)* — Use **`level4/config.yml`** with **`CompactLLMCommandGenerator`** (this repo’s Lab 0.1 pattern). **`SearchReadyLLMCommandGenerator`** can emit commands like **`set slot transfer_money_amount …`** while your slots are **`amount`**, **`recipient`**, **`account_from`** only—Rasa **drops** those commands (see **`skip_command_slot_not_in_domain`** in logs) and you get *unable to understand you*. **Fix:** align **`config.yml`** with this repo, run **`python -m rasa train`** from **`level4`**, **restart** Inspector so it loads the new **`.tar.gz`**. Details: **Unit 0.2** (section 2).
4. **Logs (optional)** — If you see **`SetSlotCommand(name='transfer_money_amount', …)`** or **`transfer_money_recipient`** but your domain uses **`amount`** / **`recipient`**, that is the mismatch above—**retrain** with **`CompactLLMCommandGenerator`**, not a domain rename.

---

## Part 3: Running locally (optional)

Same as Part 2: activate `.venv` at the **project root**, `cd level4`, run `python -m rasa inspect --debug --log-file logs/logs.out` (or `python -m rasa run`), open the UI, then follow the **Scripted transfer** table above.

---

**Done when:** Part 1 **Check It!** passes. Part 2 is strongly recommended so you see the **multi-slot + free-text recipient** behavior end-to-end.
