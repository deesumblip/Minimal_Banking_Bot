**Starting point:** Chapter 1.4 assumes you began with the **final banking agent at the end of Chapter 1.3** and extended it in **`level4/`** (see **`Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md`**).

**Objective.** After **Lab 5.1** (training), **Lab 5.2** completes Unit 5: (1) a **graded completion check** that your domain, action, flow, and model are present—the grader does **not** start Rasa or Inspector; (2) **hands-on testing** in **Rasa Inspector** to run the transfer flow and confirm **`action_process_transfer`** and the **free-text recipient** behavior (including the **100-character** cap in code + flow).

**Recommended order:** Pass the completion check first, then use Inspector with the **scripted turns** below.

**Prerequisite.** Finish **Labs 2.1, 3.1, and 4.1**, then **Lab 5.1** (a model must exist under `level4/models/`).

---

## Part 1: Completion check

1. In **Codio**, use **Check It!** for Lab 5.2 (`code-output-compare-401050002`).

The grader checks that:
   - The domain has the three transfer slots, three ask responses, and `action_process_transfer` in the actions list (keep Level 3 actions listed too so training succeeds—see Lab 2.1)
   - `level4/actions/action_process_transfer.py` exists and reads the three slots
   - `level4/data/basics/transfer_money.yml` exists with the three collect steps and the action step
   - A model file exists in `level4/models/`

2. If any check fails, fix **Labs 2.1, 3.1, or 4.1** as needed, complete **Lab 5.1** (train), then run the assessment again.

---

## Part 2: Rasa Inspector (recommended)

From **`level4`** with the virtual environment active:

1. Start the agent (e.g. `python -m rasa inspect --debug`, or `python -m rasa run` per your course).
2. Open **Rasa Inspect** (Codio) or the local URL (e.g. `http://localhost:5005`).

**Scripted transfer (type in order):**

| Step | You type (example) | What to verify |
|------|--------------------|----------------|
| 1 | `Can I transfer some money?` | Transfer flow starts. |
| 2 | `let's say 300 dollars` | Amount collected; agent asks for recipient. |
| 3 | `Alice` (or any short free text) | Recipient stored as plain text; agent asks for account. |
| 4 | `savings` (or e.g. `1234`) | Confirmation from **`action_process_transfer`**: `(Demo) Transfer of $…` |

3. Optionally try balance / hours to confirm other flows still work.

**Troubleshooting:** If the agent accepts the amount but then **cannot understand** you on recipient or account:

1. **Domain:** In **`level4/domain/basics.yml`**, set **`metadata: rephrase: False`** on **`utter_ask_amount`**, **`utter_ask_recipient`**, and **`utter_ask_account_from`** (see Lab 2.1).

2. **Flow:** In **`level4/data/basics/transfer_money.yml`**, ensure **`collect: recipient`** and **`account_from`** **`description:`** lines tell the command generator to store the **full user message** as text with a **clear length range** (Lab 4.1: **1–100** chars for recipient, **1–120** for account). **Retrain** after edits.

3. **Pipeline:** The **`level4`** repo uses **`CompactLLMCommandGenerator`** (Chapter 1.3 / **`level3`** stays **`SearchReadyLLMCommandGenerator`**). Confirm **`level4/config.yml`** and **`python -m rasa train`** from **`level4`**. See **`PIPELINE_CHAPTER_1_3_AND_4.md`**.

---

## Part 3: Running locally (optional)

Same as Part 2: activate `.venv` at the project root, `cd level4`, start Inspect or run, then use the **same table** as above.

---

**Done when:** The completion check passes; Inspector is recommended for confidence.
