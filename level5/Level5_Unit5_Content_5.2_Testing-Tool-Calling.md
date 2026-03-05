After training, run the assistant and test tool calling.

## Run

1. Start the **action server** in one terminal: from project root, activate venv, `cd level5`, then `rasa run actions`.
2. Start **Rasa** in another terminal: from project root, activate venv, `cd level5`, then `rasa run` or `rasa inspect` (with `--debug` and `--log-file` if you want logs).
3. Open **Rasa Inspector** (e.g. the Rasa Inspect tab in Codio or http://localhost:5005/webhooks/socketio/inspect.html locally).

## Test

Trigger the flow that uses tools (e.g. say you want to transfer money or check balance in a way that triggers the transfer_money_tools flow). Confirm that the bot collects the slots and that the LLM can call the tools (e.g. you get a balance or transfer confirmation). Lab 5.2 provides a completion check to verify that all required files and config are in place.
