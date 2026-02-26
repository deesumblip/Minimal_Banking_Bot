After training (Lab 4.4), you can test the transfer flow in Rasa Inspector.

## What to Do

1. **Start the bot** (e.g. from `level4` with venv active): `python -m rasa inspect --debug` (or `rasa run` if your course uses that). Leave it running.
2. **Open Rasa Inspect** — On Codio, when you see "Starting Worker" in the terminal, open the **Rasa Inspect** tab. Locally, open the URL shown (e.g. http://localhost:5005).
3. **Trigger the transfer flow** — Type something like "I want to transfer money" or "Transfer funds."
4. **Answer the prompts** — The bot should ask for amount, then recipient, then source account. Provide values (e.g. 50, Alice, 1234).
5. **Confirm** — You should see the confirmation message from `action_process_transfer` using the three values.

You can also run the **Lab 4.5 completion check** to verify that your domain, action file, flow file, and model are all in place. That assessment does not run the bot; it only checks that the required files and structure exist so the transfer flow can run.
