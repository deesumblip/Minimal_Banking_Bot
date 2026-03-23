**Objective.** After **Lab 5.1** (training), **Lab 5.2** completes Unit 5: (1) a **graded completion check** that your domain, action, flow, and model are present—the grader does **not** start Rasa or Inspector; (2) **optional** testing in **Rasa Inspector** to run the transfer flow and confirm behavior.

**Recommended order:** Complete the completion check first, then use Inspector if you want hands-on verification.

**Prerequisite.** Finish **Labs 2.1, 3.1, and 4.1**, then **Lab 5.1** (a model must exist under `level4/models/`).

---

## Part 1: Completion check

1. In **Codio**, use **Check It!** for Lab 5.2 (assessment `code-output-compare-401050002`).

The grader checks that:
   - The domain has the three transfer slots, three ask responses, and `action_process_transfer` in the actions list
   - `level4/actions/action_process_transfer.py` exists and reads the three slots
   - `level4/data/basics/transfer_money.yml` exists with the three collect steps and the action step
   - A model file exists in `level4/models/`

2. If any check fails, fix **Labs 2.1, 3.1, or 4.1** as needed, complete **Lab 5.1** (train), then run the assessment again.

---

## Part 2: Test in Rasa Inspector (optional)

From **`level4`** with the virtual environment active:

1. Start the bot (e.g. `python -m rasa inspect --debug`, or `python -m rasa run` if your course uses that). Leave it running.
2. Open **Rasa Inspect** (Codio tab) or the local URL (e.g. `http://localhost:5005`).
3. Trigger the transfer flow (“I want to transfer money”, etc.).
4. Provide amount, recipient, and source account when asked.
5. Confirm the message from `action_process_transfer`.
6. Optionally try balance / hours to confirm other flows still work.

**Troubleshooting:** If the bot accepts the amount but then says it **cannot understand** you when you enter the recipient (or account), check **`level4/domain/basics.yml`**: for **`utter_ask_amount`**, **`utter_ask_recipient`**, and **`utter_ask_account_from`**, use **`metadata: rephrase: False`**. With `rephrase: True`, Rasa Pro’s LLM layer can fail to fill the next text slot and fall back to a generic error. **Retrain** after changing the domain.

---

## Part 3: Running locally (optional)

Same as Part 2 on your machine: activate `.venv` at the project root, `cd level4`, then start Inspect or run as above.

---

**Done when:** The completion check passes; Inspector testing is optional but recommended for confidence.
