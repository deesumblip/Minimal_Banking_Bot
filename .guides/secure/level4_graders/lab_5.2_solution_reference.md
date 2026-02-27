# Lab 4.5 – Completion Check Reference

Use this file as the **Instructor Provided Solution File** for Lab 4.5 (Testing the Transfer Flow – Completion Check) if you use an LLM Rubric. The primary assessment is the Standard Code Test (lab_4.5_grader.py), which verifies that the student has completed all Level 4 components so the transfer flow can run.

---

## What “completion” means

The completion check verifies that the student has:

1. **Domain (Lab 4.1)** – level4/domain/basics.yml contains:
   - Slots: amount, recipient, account_from (type text).
   - Responses: utter_ask_amount, utter_ask_recipient, utter_ask_account_from (each with at least one message).
   - action_process_transfer in the actions: list.

2. **Action file (Lab 4.2)** – level4/actions/action_process_transfer.py exists and:
   - Defines a class with name() returning "action_process_transfer".
   - run() reads tracker.get_slot("amount"), get_slot("recipient"), get_slot("account_from") and sends a message (e.g. transfer confirmation).

3. **Flow file (Lab 4.3)** – level4/data/basics/transfer_money.yml exists and:
   - Has valid YAML with a flows: section.
   - At least one flow has steps that include collect: amount, collect: recipient, collect: account_from, and action: action_process_transfer.

4. **Trained model (Lab 4.4)** – At least one `.tar.gz` file exists in level4/models/, indicating the student ran `python -m rasa train` from level4.

Together, these indicate the student can start the bot and test the transfer flow in Rasa Inspector. The grader does not run the bot or Inspector; it only checks files and structure.

---

## Rubric summary (if using LLM Rubric)

- **Domain:** Transfer slots and ask responses and action_process_transfer present in level4/domain/basics.yml.
- **Action:** action_process_transfer.py exists and reads the three slots and sends a message.
- **Flow:** transfer_money.yml exists with the three collect steps and the action step.
- **Model:** A model file exists in level4/models/.
