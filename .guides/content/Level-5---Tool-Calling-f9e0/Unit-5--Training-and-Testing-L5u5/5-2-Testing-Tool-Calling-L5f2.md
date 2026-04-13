**Starting point:** Work in **`level5/`** after **Lab 5.1**. You should have a trained model under **`level5/models/`**. (Training assumes **Labs 2.0–4.1**, including **Lab 2.0** **`prompt_template`** and **`data/prompts/`**.)

Run the assistant and exercise tool calling.

## Run

1. Start the **action server** in one terminal: from **project root**, activate the venv, **`cd level5`**, then **`python -m rasa run actions`**.
2. Start **Rasa** in another terminal: from **project root**, activate the venv, **`cd level5`**, then **`python -m rasa run`** or **`python -m rasa inspect`** (add **`--debug`** and **`--log-file`** if you want logs under **`level5/logs/`**).
3. Open **Rasa Inspector** (for example the **Rasa Inspect** tab in Codio, or **`http://localhost:5005/webhooks/socketio/inspect.html`** locally. Use another port if **`--port`** is busy, for example **`http://localhost:5025/webhooks/socketio/inspect.html`**).

## Test

Trigger the tool-enabled flow. For example, ask to **transfer money using tools** so the assistant picks **`transfer_money_tools`**. Supply **amount**, **recipient**, and **account_from** when asked.

The reply should match your **`action_process_transfer_with_tools`** text (the reference includes **“(Demo with Tools)”**).

In a **new conversation**, run **`transfer_money`** and confirm the classic **`action_process_transfer`** wording differs.

**Lab 5.2** next runs an automated **completion check** on files and config.
