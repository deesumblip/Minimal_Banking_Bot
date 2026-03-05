# Lab 4.2: Multiple Actions

You've now registered both actions in the domain: **action_bank_hours** (the example) and **action_holiday_hours** (the one you created in Lab 3.1). With both registered, Rasa can invoke them—in Unit 5 you'll connect them to flows. When you add more actions later, list each on its own line under `actions:` with a dash.

---

#### Review in Inspector (optional)

After you run the Lab 4.1 assessment, you can see how registration affects the bot. **In the terminal** use the **virtual environment in the main folder** (project root); then go into `level2` and run the Level 2 bot from there so it uses your Level 2 changes (domain, flows, actions).

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
3. **Go into `level2`:** run `cd level2`. All commands below run from here so Rasa uses the Level 2 bot (your domain, flows, and actions).
4. **Train the Level 2 bot:** run `python -m rasa train`. Wait for the model to save.
5. **Start and open the Rasa Inspector GUI.** Run `python -m rasa inspect --debug` in the terminal and leave it running. Then open the Inspector interface:
   - **In Codio:** Click the **Rasa Inspect** tab on the top menu bar to open the chat.
   - **Running locally:** Open your browser and go to **http://localhost:5005** (or **http://localhost:5005/webhooks/socketio/inspect.html** if the chat doesn’t appear). Same on Windows, macOS, and Linux.

In the Inspector chat, try:

- **"What are your hours?"** — If the `hours` flow exists, the bot should use `action_bank_hours` and reply with bank hours.
- **"What are your holiday hours?"** — The bot likely won't handle this yet, because there's no flow that uses your action. You'll add that flow in Unit 5.

---
