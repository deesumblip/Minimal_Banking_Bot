You've now registered both actions in the domain (Unit 4), connected them to flows (Lab 5.1), and trained (Lab 6.1). This lab verifies that your agent is **ready to run**:

- Both actions are registered in the domain: **`action_bank_hours`** (example) and **`action_holiday_hours`** (your Lab 3.1 action)
- You have a trained model under **`level2/models/`**

---

#### Optional: Test and debug in Inspector

Use the steps below to run the Level 2 agent and confirm that both flows and actions trigger correctly.

1. **Go to the main folder** (the project root, one level *above* `level2`—the folder that contains `level1`, `level2`, and `.guides`). If you're inside `level2` or a subfolder, run `cd ..` (or `cd ../..` as needed) until you're in that main folder.
2. **Activate the virtual environment** (it lives in the main folder at the project root, e.g. `.venv`). Your prompt should show `(.venv)` when active.
   - **In Codio:** Codio’s terminal runs **Linux**. From the main folder, run:

     ```bash
     source .venv/bin/activate
     ```

   - **Running locally (your own machine):**
     - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
     - **Windows (Command Prompt):** `.venv\Scripts\activate.bat`
     - **macOS / Linux:** `source .venv/bin/activate`
3. **Go into `level2`:** run `cd level2`.
4. **Train the Level 2 agent:** run:

```bash
python -m rasa train
```

Wait for training to finish and for a new `.tar.gz` to appear under `models/`.

5. **Start Inspector:** run the server and write logs to `logs/logs.out`:

```bash
python -m rasa inspect --debug --log-file logs/logs.out
```

Leave this running, then open the Inspector interface:
   - **In Codio:** Click the **Rasa Inspect** tab on the top menu bar to open the chat.
   - **Running locally:** Open your browser and go to **http://localhost:5005** (or **http://localhost:5005/webhooks/socketio/inspect.html** if the chat doesn’t appear). Same on Windows, macOS, and Linux.

##### Questions to ask in the Inspector chat

Use these to verify the latest flows and actions:

| You ask | Expected flow | Expected action / behavior |
|--------|----------------|----------------------------|
| **"Hello"** | `greet` | Level 1 greeting |
| **"What are your hours?"** / **"When are you open?"** | `hours` | `action_bank_hours` |
| **"What are your holiday hours?"** / **"Are you open on holidays?"** / **"Are you open on Christmas?"** | `holiday_hours` | `action_holiday_hours` |
| **"Help"** | `help` | Level 1 help |
| **"How can I contact you?"** | `contact` | Level 1 contact |

##### Check the debug panel

With `--debug` and the log file from step 5, use Inspector’s debug output (and `logs/logs.out`) to confirm which **flow** fired, which **action** ran, and whether the action finished without errors.

##### Common issues

1. **Action doesn't trigger** — Does the flow `description` match what the user said? Is the action listed under `actions:` in the domain? Does the Python file exist under `actions/`?
2. **Action runs but no message** — Is `dispatcher.utter_message()` called? Check `logs/logs.out` for Python errors.
3. **Python errors** — Fix syntax, imports, and method names (`name()`, `run()`, etc.), then train again.

---

#### Run the assessment

Submit the Check It! below once you meet the checks (domain registration and a trained model under `models/`).

{Check It!|assessment}(code-output-compare-1597644299)
