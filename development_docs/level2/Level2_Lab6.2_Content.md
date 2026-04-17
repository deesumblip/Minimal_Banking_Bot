# Lab 6.2: Training and Testing

You’ve already trained your Level 2 agent in **Lab 6.1**. This lab is about **testing** your flows and actions end-to-end in **Rasa Inspector**.

**Before you start:** Activate your virtual environment from the project root. Run the steps below from inside `level2/`, using the same setup as **Lab 6.1**.

---

#### Step 1: Start Inspector

From the `level2` folder, create the `logs` folder, then start Inspector and write logs to `logs/logs.out`. In **Codio** or **macOS / Linux**, run `mkdir -p logs`. In **Windows PowerShell**, run `mkdir logs`.

```bash
mkdir -p logs
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

With `--debug` and the log file from step 1, use Inspector’s debug output and `logs/logs.out` to confirm which **flow** fired, which **action** ran, and whether the action finished without errors.

##### Common issues

1. **Action doesn't trigger.** Check whether the flow `description` matches what the user said, whether the action is listed under `actions:` in the domain, and whether the Python file exists under `actions/`.
2. **Action runs but no message.** Confirm `dispatcher.utter_message()` is called. Check `logs/logs.out` for Python errors.
3. **Python errors.** Fix syntax, imports, and method names such as `name()` and `run()`, then train again.

---

#### Run the Lab 6.2 assessment

When you’re done testing, run the Check It! below. It only checks that **`level2/logs/logs.out`** exists and shows you ran **`rasa inspect`** with **`--log-file`**, using the same command as in step 1. It does not re-check domain or training.

{Check It!|assessment}(code-output-compare-1597644299)
