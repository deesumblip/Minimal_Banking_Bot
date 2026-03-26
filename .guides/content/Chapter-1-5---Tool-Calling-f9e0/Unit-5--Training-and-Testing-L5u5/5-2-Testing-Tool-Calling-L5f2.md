**Starting point:** Work in **`level5/`** after **Lab 5.1** (a model under **`level5/models/`** ).

After training, run the assistant and test tool calling.

## Run

1. Start the **action server** in one terminal: from **project root**, activate the venv, **`cd level5`**, then **`python -m rasa run actions`**.
2. Start **Rasa** in another terminal: from **project root**, activate the venv, **`cd level5`**, then **`python -m rasa run`** or **`python -m rasa inspect`** (add **`--debug`** and **`--log-file`** if you want logs under **`level5/logs/`**).
3. Open **Rasa Inspector** (for example the **Rasa Inspect** tab in Codio, or **`http://localhost:5005/webhooks/socketio/inspect.html`** locally).

## Test

Trigger the flow that uses tools (for example, ask to transfer money or check a balance in a way that reaches **`transfer_money_tools`**). Confirm that the agent collects the slots and that the LLM can call the tools (you should see balance or transfer-related behavior from your tool functions). **Lab 5.2** adds a **completion check** that verifies required files and configuration.
