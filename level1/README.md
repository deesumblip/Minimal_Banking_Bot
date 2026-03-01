# 🟢 Level 1: Just Responses

**Goal:** Build the simplest possible bot that only uses predefined responses (no memory, no custom code).

## What You'll Learn

- How to define bot responses in the domain
- How to create simple flows that just say things
- The basic structure of a Rasa bot

## Quick Start

1. **Create and activate a virtual environment:**
   ```powershell
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   ```

2. **Install Rasa Pro:**
   ```powershell
   python -m pip install --no-cache-dir rasa-pro
   ```

3. **Set `RASA_LICENSE` and `OPENAI_API_KEY`:** Create a `.env` file in the project root with:
   ```text
   RASA_LICENSE=rasaxxx-your-license-here
   OPENAI_API_KEY=sk-your-openai-key-here
   ```
   Replace with your actual values. See Lab 0.1 for Codio vs local (Windows/macOS/Linux).

4. **Train and run:**
   ```powershell
   . .\load_env.ps1
   python -m rasa train
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

   Or use the helper script:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1
   ```

5. **Open Inspector:**
   - `http://localhost:5005/webhooks/socketio/inspect.html`

## What's in This Level

### Domain (`domain/basics.yml`)
- **Only `responses:` section** - predefined bot messages
- No slots (memory)
- No actions (custom code)

### Flows (`data/basics/*.yml`)
- `greet.yml` - Says hello
- `help.yml` - Lists what the bot can do
- `contact.yml` - Provides contact information

All flows are simple: they just call `utter_*` actions (predefined responses).

## Exercises

1. **Add a new response:** Edit `domain/basics.yml`, add `utter_goodbye` with a farewell message.
2. **Create a new flow:** Create `data/basics/goodbye.yml` that uses `utter_goodbye`.
3. **Change existing text:** Modify any `utter_*` response text and retrain.

## Next Level

Once you're comfortable with responses, move to **Level 2** to learn about custom actions!
