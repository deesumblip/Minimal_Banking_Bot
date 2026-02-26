Your goal is to run the **completion check** for Level 4 and, optionally, test the transfer flow in Rasa Inspector.

**Prerequisite.** Complete Labs 4.1–4.4. You need: domain with transfer slots and ask responses, `action_process_transfer.py`, `transfer_money.yml`, and a trained model in `level4/models/`.

---

## Part 1: Completion check (assessment)

1. Run the **Lab 4.5 assessment**. The grader checks that:
   - The domain has the three transfer slots, three ask responses, and `action_process_transfer` in the actions list
   - `level4/actions/action_process_transfer.py` exists and reads the three slots
   - `level4/data/basics/transfer_money.yml` exists with the three collect steps and the action step
   - A model file exists in `level4/models/`

2. If any check fails, complete the corresponding lab (4.1–4.4) and re-run training if needed, then run the assessment again.

---

## Part 2: Test in Inspector (optional)

1. **Start the bot.** From `level4` with venv active, run `python -m rasa inspect --debug`. Leave the terminal open. When you see "Starting Worker", open the **Rasa Inspect** tab (Codio) or the URL shown (e.g. http://localhost:5005).

2. **Trigger the transfer flow.** Type "I want to transfer money" or "Transfer funds."

3. **Answer the prompts.** The bot should ask for amount, then recipient, then source account. Provide values (e.g. 50, Alice, 1234).

4. **Confirm.** You should see the confirmation message from `action_process_transfer` using the three values.

5. **Verify other flows.** Try "Check my balance" and "What are your hours?" to confirm Level 3 and Level 2 flows still work.

You're done when the completion check passes and, if you ran Inspector, the transfer flow and other flows behave as expected.
