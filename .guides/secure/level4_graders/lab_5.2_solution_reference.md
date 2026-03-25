# Lab 5.2 – Completion Check (Transfer Flow) — Reference

Use this file as the **Instructor Provided Solution File** for **Lab 5.2** (completion check) if you use an LLM Rubric. The primary assessment is the Standard Code Test (`lab_5.2_grader.py`), which verifies that the student has completed all Level 4 components so the transfer flow can run.

---

## What “completion” means

The completion check verifies that the student has:

1. **Domain (Lab 2.1)** – `level4/domain/basics.yml` contains:
   - Slots: `amount`, `recipient`, `account_from` (type text).
   - Responses: `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from` (each with at least one message).
   - `action_process_transfer` in the `actions:` list.

2. **Action file (Lab 3.1)** – `level4/actions/action_process_transfer.py` exists and:
   - Defines a class with `name()` returning `"action_process_transfer"`.
   - `run()` reads `tracker.get_slot("amount")`, `get_slot("recipient")`, `get_slot("account_from")` and sends a message (e.g. transfer confirmation).

3. **Flow file (Lab 4.1)** – `level4/data/basics/transfer_money.yml` exists and:
   - Has valid YAML with a `flows:` section.
   - The transfer flow has steps that include `collect: amount`, `collect: recipient`, `collect: account_from`, and `action: action_process_transfer`.

4. **Trained model (Lab 5.1)** – At least one `.tar.gz` file exists in `level4/models/`, indicating the student ran `python -m rasa train` from `level4`.

5. **Pipeline (Chapter 1.4)** – `level4/config.yml` has **`CompactLLMCommandGenerator`** in **`pipeline:`** and does **not** use **`SearchReadyLLMCommandGenerator`** as a pipeline step `name`, so the model matches the course slot names (`amount`, `recipient`, `account_from`).

Together, these indicate the student can start the agent and test the transfer flow in Rasa Inspector. The grader does not run the agent or Inspector; it only checks files and structure.

**Hands-on check (optional):** In Inspector, run the scripted turns from **Lab 5.2** (e.g. “Can I transfer some money?” → amount → free-text recipient → source account) and confirm the **`(Demo) Transfer of $…`** confirmation.

---

## Rubric summary (if using LLM Rubric)

- **Domain:** Transfer slots and ask responses, legacy custom actions, and `action_process_transfer` present in `level4/domain/basics.yml`.
- **Action:** `action_process_transfer.py` exists and reads the three slots and sends a message.
- **Flow:** `transfer_money.yml` exists with the three collect steps and the action step.
- **Model:** A model file exists in `level4/models/`.
- **Config:** `level4/config.yml` pipeline uses **Compact** LLM command generation (not SearchReady).
