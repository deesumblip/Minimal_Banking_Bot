**Starting point:** Chapter 1.4 assumes you began with the **final banking agent at the end of Chapter 1.3** and extended it in **`level4/`** (see **Unit 0.1**).

**Unit 5, Lab 5.2.** You already **trained** the agent in **Lab 5.1**. This lab has two parts in order:

1. **Completion check (graded)**. Confirms domain, action, flow YAML, and a trained model are in place. The grader **does not** start Rasa or Inspector.
2. **Rasa Inspector (recommended)**. Run the **transfer** flow and confirm **`action_process_transfer`** fires with the expected demo message (free-text **recipient**, **100-character cap** in code + flow).

**Prerequisite:** **Labs 2.1 → 3.1 → 4.1** done, then **Lab 5.1** so `level4/models/` contains a `.tar.gz` file.

---

## Part 1: Completion check (Codio)

1. Use **Check It!** below. The grader verifies:
   - **Domain:** slots `amount`, `recipient`, `account_from`; `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`; `action_process_transfer` in `actions:` (keep Level 3 actions listed too so training succeeds—see Lab 2.1)
   - **Action:** `level4/actions/action_process_transfer.py` reads the three slots (via `get_slot`)
   - **Flow:** `level4/data/basics/transfer_money.yml` has the three `collect:` steps and `action: action_process_transfer`
   - **Model:** at least one `.tar.gz` under `level4/models/`

{Check It!|assessment}(code-output-compare-401050002)

2. If a check fails, fix the matching lab (**2.1** domain, **3.1** action, **4.1** flow, **5.1** train), then run **Check It!** again.

---

## Part 2: Test in Rasa Inspector (hands-on)

**When:** After Part 1 passes (or whenever you want to see the agent live).

**Where:** From **`level4`** with the project **virtual environment** active (same as Lab 5.1).

1. **Start the assistant**, e.g. `python -m rasa inspect --debug` (your environment may use `python -m rasa run` instead). Leave the process running.
2. **Open the UI**. On **Codio**, open the **Rasa Inspect** tab when the terminal shows the server is up. **Locally**, use the URL shown (often `http://localhost:5005`).
3. **Run the scripted transfer**. Type the turns **in order** so you exercise **amount → recipient → account_from → confirmation**:

| Step | You type (example) | What you’re checking |
|------|--------------------|----------------------|
| 1 | `Can I transfer some money?` | Agent enters the transfer flow (may greet first). |
| 2 | `let's say 300 dollars` | **Amount** slot filled; agent asks for recipient. |
| 3 | `Alice` *(or any short free text, e.g. `MC hammer`)* | **Recipient** is stored as plain text (up to **100** chars in action + flow); agent asks for source account. |
| 4 | `savings` *(or e.g. `1234`)* | **account_from** filled; agent runs **`action_process_transfer`**. |
| 5 | *(read only)* | Final line should match the demo pattern: **`(Demo) Transfer of $… from account … to … has been processed successfully.`** |

4. **Optional sanity checks**. Try **“What’s my balance?”** / **“What are your hours?”** to confirm Level 3 / Level 2 flows still work from the same `level4` model.

---

### If the agent says “unable to understand you” on recipient or account

1. **Domain:** In **`level4/domain/basics.yml`**, use **`metadata: rephrase: False`** on **`utter_ask_amount`**, **`utter_ask_recipient`**, and **`utter_ask_account_from`** (see Lab 2.1).
2. **Flow:** In **`level4/data/basics/transfer_money.yml`**, ensure **`collect: recipient`** and **`collect: account_from`** have clear **`description:`** text (full user message as text; **1–100** chars for recipient, **1–120** for account in Lab 4.1). **Retrain** after edits.
3. **Pipeline:** Use this repo’s **`level4/config.yml`** (**`CompactLLMCommandGenerator`**). Chapter 1.3 **`level3`** keeps **`SearchReadyLLMCommandGenerator`**. After any config or YAML change: **`python -m rasa train`** from **`level4`**. See **`level4/PIPELINE_CHAPTER_1_3_AND_4.md`**.

---

## Part 3: Running locally (optional)

Same as Part 2: activate `.venv` at the **project root**, `cd level4`, run Inspect or `rasa run`, open the UI, then use the **same table** as in Part 2.

---

**Done when:** Part 1 **Check It!** passes. Part 2 is strongly recommended so you see the **multi-slot + free-text recipient** behavior end-to-end.
