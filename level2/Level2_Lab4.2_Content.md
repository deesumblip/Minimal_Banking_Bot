# Lab 4.2: Multiple Actions

You've now registered both actions in the domain: **action_bank_hours** (the example) and **action_holiday_hours** (the one you created in Lab 3.1). With both registered, Rasa can invoke them—in Unit 5 you'll connect them to flows. When you add more actions later, list each on its own line under `actions:` with a dash.

---

#### Review in Inspector (optional)

After you run the Lab 4.1 assessment, you can see how registration affects the bot. **In the terminal:**

1. **Go to the main folder** (the project root, one level *above* `level2`—the folder that contains `level1`, `level2`, and `.guides`). If you're inside `level2` or a subfolder, run `cd ..` (or `cd ../..` as needed) until you're in that main folder.
2. **Go into `level2`:** run `cd level2`.
3. **Activate the virtual environment**, then train.
   - **In Codio:** Codio’s terminal runs **Linux**. From the `level2` folder, run:
     ```bash
     source .venv/bin/activate
     python -m rasa train
     ```
   - **Running locally (your own machine):**
     - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1` then `python -m rasa train`
     - **Windows (Command Prompt):** `.venv\Scripts\activate.bat` then `python -m rasa train`
     - **macOS / Linux:** `source .venv/bin/activate` then `python -m rasa train`
   Your prompt should show `(.venv)` when the environment is active.
4. Start and open the Rasa Inspector GUI. In the Inspector chat, try:

- **"What are your hours?"** — If the `hours` flow exists, the bot should use `action_bank_hours` and reply with bank hours.
- **"What are your holiday hours?"** — The bot likely won't handle this yet, because there's no flow that uses your action. You'll add that flow in Unit 5.

---
