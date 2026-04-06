**Starting point:** Work in **`level4/`** with transfer pieces in place (see **Unit 0.1**).

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
   - `level4/endpoints.yml` — under **`model_groups`**, **`id: openai-gpt-5-1`** uses **`model: openai-gpt-5-1`** and **`temperature: 0.1`** (**Unit 0.2** / Lab 0.1)

**Inspector:** If the completion check passes but **Part 2** still mis-fills **recipient**, double-check **`endpoints.yml`** and **`config.yml`** and retrain from **`level4/`**.

2. If any check fails, fix **Labs 2.1, 3.1, or 4.1** as needed, align **`level4/config.yml`** and **`level4/endpoints.yml`** with Unit 0.2, complete **Lab 5.1** (train), then run the assessment again.

---

## Part 2: Rasa Inspector (recommended)

**When:** After the completion check passes (or whenever you want to see the agent live).

**Where:** From **`level4`** with the project **virtual environment** active (same as Lab 5.1).

### Start the assistant

- `cd` to **`level4`**, then start Rasa, for example:
  - `python -m rasa inspect --debug --log-file logs/logs.out` — logs under **`level4/logs/`** (same pattern as **Lab 5.1**).
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

| Step | You type (example) | What to verify |
|------|--------------------|----------------|
| 1 | `Can I transfer some money?` | Transfer flow starts (may greet first). |
| 2 | `let's say 300 dollars` | **Amount** collected; agent asks for recipient. |
| 3 | `Alice` *(or any short free text, e.g. `MC hammer`)* | **Recipient** as plain text (up to **100** chars); agent asks for source account. |
| 4 | `savings` *(or e.g. `1234`)* | **account_from** filled; **`action_process_transfer`** runs. |
| 5 | *(read only)* | Confirmation matches **`(Demo) Transfer of $… from account … to … has been processed successfully.`** |

### Optional: other flows

Try **“What’s my balance?”** or **“What are your hours?”** to confirm **check_balance** and **hours** still work.

### If you see “unable to understand you” during transfer

Work through these in order (domain → flow → pipeline):

1. **Domain** — In **`level4/domain/basics.yml`**, set **`metadata: rephrase: False`** on **`utter_ask_amount`**, **`utter_ask_recipient`**, and **`utter_ask_account_from`** (Lab 2.1).
2. **Flow** — In **`level4/data/basics/transfer_money.yml`**, each **`collect:`** needs a clear **`description:`** (Lab 4.1). **Retrain** after edits.
3. **Pipeline** *(most common for repeated failures)* — Use **`level4/config.yml`** with **`CompactLLMCommandGenerator`** (Lab 0.1 pattern). **`SearchReadyLLMCommandGenerator`** can emit **`transfer_money_*`** slot names while your domain uses **`amount`** / **`recipient`** / **`account_from`**—Rasa drops those commands (*unable to understand you*). Align **`config.yml`**, **`python -m rasa train`** from **`level4`**, **restart** Inspector. See **Unit 0.2** (section 2).
4. **Logs (optional)** — **`skip_command_slot_not_in_domain`** or **`SetSlotCommand(name='transfer_money_amount', …)`** with **`transfer_money_recipient`** point to the pipeline mismatch above—**retrain** with **Compact**, not a domain rename.

---

## Part 3: Running locally (optional)

Same as Part 2: activate `.venv` at the project root, `cd level4`, `python -m rasa inspect --debug --log-file logs/logs.out` (or `python -m rasa run`), open the UI, then follow the **Scripted transfer** table in Part 2.

---

**Done when:** The completion check passes; Inspector is recommended for confidence.
