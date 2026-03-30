**Starting point:** Work in **`level5/`** after **Lab 5.1** in this unit—you should have a trained model under **`level5/models/`**. (Training assumes **Labs 2.0–4.1** are complete, including **`prompt_template`** and **`data/prompts/`** from **Lab 2.0**.)

After training, run the assistant and test tool calling.

## Run

1. Start the **action server** in one terminal: from **project root**, activate the venv, **`cd level5`**, then **`python -m rasa run actions`**.
2. Start **Rasa** in another terminal: from **project root**, activate the venv, **`cd level5`**, then **`python -m rasa run`** or **`python -m rasa inspect`** (add **`--debug`** and **`--log-file`** if you want logs under **`level5/logs/`**).
3. Open **Rasa Inspector** (for example the **Rasa Inspect** tab in Codio, or **`http://localhost:5005/webhooks/socketio/inspect.html`** locally—use another port if **`--port`** is busy, for example **`http://localhost:5025/webhooks/socketio/inspect.html`**).

## Test

Trigger the flow that uses tools (for example, ask to **transfer money using tools** so the assistant selects **`transfer_money_tools`**). Complete **amount**, **recipient**, and **account_from** when prompted. You should see a confirmation that matches your **`action_process_transfer_with_tools`** message (in the course reference, that includes **“(Demo with Tools)”**). To compare paths, run **`transfer_money`** in a **new conversation** and confirm the classic **`action_process_transfer`** message differs. The **next lab** in this unit runs a **completion check** that verifies required files and configuration.
