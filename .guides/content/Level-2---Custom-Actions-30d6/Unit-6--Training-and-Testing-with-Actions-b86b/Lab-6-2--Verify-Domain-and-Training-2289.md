You’ve already trained your Level 2 agent in **Lab 6.1**. This lab is about **testing** your flows and actions end-to-end in **Rasa Inspector**.

**Before you start:** Activate your virtual environment (from the project root) and run these commands from inside `level2/` (same setup as Lab 6.1).

---

#### Step 1: Start Inspector

From the `level2` folder, start Inspector and write logs to `logs/logs.out`:

```bash
python -m rasa inspect --debug --log-file logs/logs.out
```

Leave this running, then open the Inspector interface:
   - **In Codio:** Click the **Rasa Inspect** tab on the top menu bar to open the chat.
   - **Running locally:** Open your browser and go to **http://localhost:5005** (or **http://localhost:5005/webhooks/socketio/inspect.html** if the chat doesn’t appear). Same on Windows, macOS, and Linux.

#### Step 2: Run test prompts in the chat

Use these prompts to verify the latest flows and actions:

| You ask | Expected flow | Expected action / behavior |
|--------|----------------|----------------------------|
| **"Hello"** | `greet` | Level 1 greeting |
| **"What are your hours?"** / **"When are you open?"** | `hours` | `action_bank_hours` |
| **"What are your holiday hours?"** / **"Are you open on holidays?"** / **"Are you open on Christmas?"** | `holiday_hours` | `action_holiday_hours` |
| **"Help"** | `help` | Level 1 help |
| **"How can I contact you?"** | `contact` | Level 1 contact |

#### Step 3: Check the debug panel

With `--debug` and the log file from step 1, use Inspector’s debug output (and `logs/logs.out`) to confirm which **flow** fired, which **action** ran, and whether the action finished without errors.

##### Common issues

1. **Action doesn't trigger** — Does the flow `description` match what the user said? Is the action listed under `actions:` in the domain? Does the Python file exist under `actions/`?
2. **Action runs but no message** — Is `dispatcher.utter_message()` called? Check `logs/logs.out` for Python errors.
3. **Python errors** — Fix syntax, imports, and method names (`name()`, `run()`, etc.), then train again.

---

#### Run the Lab 6.2 assessment

When you’re done testing, run the Check It! below (it verifies your domain registration plus that a trained model exists under `level2/models/`).

{Check It!|assessment}(code-output-compare-1597644299)
