### 6.3 Testing and Debugging Your Action

You can use Rasa Inspector as in **Lab 6.2** (optional walkthrough) before this section. This section formalizes the testing workflow and gives you a checklist against the table below.

**Setup reminder**: If you need to review Inspector setup (go to main folder → activate virtual environment → `cd level2` → train → start Inspector), see **Lab 6.2** for the full step-by-step instructions.

#### Questions to ask in the Inspector chat

Use these in the Inspector chat to check that the most recent implementations work:

| You ask | Expected flow | Expected action / behavior |
|--------|----------------|----------------------------|
| **"Hello"** | `greet` | Level 1 greeting |
| **"What are your hours?"** / **"When are you open?"** | `hours` | `action_bank_hours`, message varies by day (weekday vs weekend) |
| **"What are your holiday hours?"** / **"Are you open on holidays?"** / **"Are you open on Christmas?"** | `holiday_hours` | `action_holiday_hours`, message varies by whether today is a holiday (date-based) |
| **"Help"** | `help` | Level 1 help |
| **"How can I contact you?"** | `contact` | Level 1 contact |

#### Formal testing workflow

1. **Train your agent** — From the `level2` folder (with the virtual environment activated):

```bash
python -m rasa train
```

Wait for training to finish.

2. **Start Inspector** — Leave the server running and open Inspector in your browser (Codio port forwarding or local URL: **Lab 6.2**).

```bash
python -m rasa inspect --debug --log-file logs/logs.out
```

3. **Run through the table** — For each row, confirm the **flow** and **action** (or Level 1 behavior) match. Pay special attention to **`hours`** vs **`holiday_hours`** so you see both the example action and your Lab 3.1 action.

4. **Watch routing in Inspector** — For the same user goal, compare phrasing (e.g. hours vs holiday hours) and observe how **flow** and **action** change—that reflects your **domain** and **flow YAML**.

**Key point**: All Level 1 paths should still work. If your new action does not trigger, check **domain** registration and a clear **`description`** on the flow.

#### Check the debug panel

With **`--debug`** and the log file from step 2, use Inspector’s **debug** output to confirm which **flow** fired, which **action** ran, and whether the action finished without errors.

#### Common issues

1. **Action doesn't trigger** — Does the flow **`description`** match what the user said? Is the action in **`domain/`**? Does the file exist under **`actions/`**?
2. **Action runs but no message** — Is **`dispatcher.utter_message()`** called? Check the terminal or **`logs/`** for Python errors in the action.
3. **Python errors** — Fix syntax, imports, and method names (`name()`, `run()`, etc.).

---
