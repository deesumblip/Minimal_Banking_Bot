After **Lab 5.1** (training), **Lab 5.2** finishes Unit 5 with two parts:

1. **Completion check (graded)** — Confirms your domain, action, flow, and trained model are in place. The grader **does not** start Rasa or open Inspector; it only checks files and structure.
2. **Testing in Rasa Inspector (optional)** — Walk through the **transfer** flow live: trigger it, answer the prompts, and confirm `action_process_transfer` runs. You can also spot-check **Level 3** flows (e.g. balance, hours).

**Recommended order:** Run **Check It!** in Part 1 first. If that passes, your project is ready to run; Part 2 is for hands-on verification.

**Prerequisite.** Complete **Labs 2.1, 3.1, and 4.1**, then **Lab 5.1** (so a model exists in `level4/models/`). You need: domain with transfer slots and ask responses, `action_process_transfer.py`, `transfer_money.yml`, and a trained model.

---

## Part 1: Completion check (Codio)

1. Use **Check It!** below. The grader checks that:
   - The domain has the three transfer slots, three ask responses, and `action_process_transfer` in the actions list
   - `level4/actions/action_process_transfer.py` exists and reads the three slots
   - `level4/data/basics/transfer_money.yml` exists with the three collect steps and the action step
   - A model file exists in `level4/models/`

{Check It!|assessment}(code-output-compare-401050002)

2. If any check fails, fix the corresponding lab (**2.1** domain, **3.1** action, **4.1** flow, or **5.1** training), then use **Check It!** again.

---

## Part 2: Test in Rasa Inspector (optional)

Use this after Part 1 passes (or when you are ready to exercise the bot). Start from **`level4`** with the virtual environment active.

1. **Start the bot** — For example: `python -m rasa inspect --debug`. Your course may use `python -m rasa run` instead; follow your instructor if unsure. Leave the process running.
2. **Open the UI** — On **Codio**, when you see **Starting Worker** in the terminal, open the **Rasa Inspect** tab. **Locally**, open the URL shown (e.g. `http://localhost:5005`).
3. **Trigger the transfer flow** — Try phrases like “I want to transfer money” or “Transfer funds.”
4. **Answer the prompts** — The bot should ask for **amount**, then **recipient**, then **source account**. Example values: `50`, `Alice`, `1234`.
5. **Confirm** — You should see the confirmation from `action_process_transfer` using all three values.
6. **Verify other flows (optional)** — Try “Check my balance” and “What are your hours?” to confirm Level 3 / Level 2 behavior still works.

### If the bot says “unable to understand you” when collecting the recipient (or account)

**What you might see:** Amount works, then after you type a name (e.g. “Alice” or “Ronald McDonald”) the bot replies with something like *“I’m sorry I am unable to understand you, could you please rephrase?”* and asks again—sometimes losing the amount in the follow-up prompt.

**Why:** With **Rasa Pro** (CALM + `SearchReadyLLMCommandGenerator`), **slot collection** is sensitive to how ask prompts are generated. If **`utter_ask_amount` / `utter_ask_recipient` / `utter_ask_account_from`** use **`metadata: rephrase: True`**, the model can rephrase those questions during collection; the command layer may then fail to map your free-text answer to the slot and fall back to that generic message.

**Fix (domain):** In **`level4/domain/basics.yml`**, set **`rephrase: False`** for those three `utter_ask_*` responses (keep `rephrase: True` on greetings/help if you want). **Retrain** (`python -m rasa train` from `level4`) and test again. This is the pattern recommended in **Lab 2.1**.

**Still stuck? Fix (flow YAML):** In **`level4/data/basics/transfer_money.yml`**, expand the **`description:`** under **`collect: recipient`** (and each collect step) so the LLM command generator knows to treat the **whole user message** as free text, including **multi-word names**. Short strings like `"recipient name or account"` are often **not** enough for CALM. Use the **Lab 4.1** example (longer descriptions). **Retrain** after editing the flow.

**Optional (advanced):** Rasa docs recommend **`CompactLLMCommandGenerator`** when you are **not** using Enterprise Search / RAG. This course’s **`config.yml`** uses **`SearchReadyLLMCommandGenerator`** (fine for many setups). If problems persist after domain + flow fixes, ask your instructor about trying **`CompactLLMCommandGenerator`** in `level4/config.yml` per [Rasa LLM command generators](https://rasa.com/docs/reference/config/components/llm-command-generators/).

---

## Part 3: Running locally (optional)

Same flow as Part 2 on your own machine: activate `.venv` at the project root, `cd level4`, then `python -m rasa inspect --debug` (or `rasa run` per your setup). Open **Rasa Inspect** or the served URL as above.

---

**Done when:** The completion check in Part 1 passes. Optionally, you have also walked through the transfer flow in Inspector (and any extra checks you care about).
