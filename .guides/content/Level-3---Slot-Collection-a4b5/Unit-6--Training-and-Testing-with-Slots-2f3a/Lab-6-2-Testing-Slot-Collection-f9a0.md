Your goal is to test your Level 3 agent in Inspector so you see slot collection and persistence in action.

**Prerequisite.** Complete **Lab 6.1** (training). A model file must exist in **`level3/models/`**.

---

## Part 1: In Codio

#### Virtual environment and folder

Stay in the same setup as **Lab 6.1**. You should be in **`level3`** with the venv active. Run **`pwd`** and check that the path ends with **`level3`**. Your prompt should start with **`(.venv)`**.

If the venv is not active, go to the **project root**, then run:

```bash
source .venv/bin/activate
cd level3
```

#### Logs folder

From **`level3`**, create a **`logs`** directory if needed:

```bash
mkdir -p logs
```

#### Start Inspector

From **`level3`**, with the venv still active, run:

```bash
python -m rasa inspect --debug --log-file logs/logs.out
```

Leave the terminal open. When you see output such as **Starting Worker** or a server line, open the **Rasa Inspect** tab in the top menu. Do not rely on Tools → Ports unless your course explicitly uses that workflow.

#### Test the agent

1. **Slot collection.** Type **Check my balance**. The agent should ask for your account number. Type **1234**. The agent should respond with a balance for that account.

2. **Slot persistence.** Type **What's my balance?** again. The agent should remember **1234** without asking again.

3. **Level 2 and Level 1.** Type **What are your hours?** and **Hello** to confirm older flows still run.

Use the **debug** panel to see which flow ran and how the **`account`** slot is set and reused.

You are done with the hands-on checklist when collection, persistence, and cross-level flows behave as above. That checklist is **completion-based** and is not a separate graded automation task.

---

## Part 2: Not using Codio? Inspector locally

Use this when you run the course on your own machine. You need **`level3`**, Rasa Pro in the venv, and the same license and API keys you used for training.

1. Open a terminal and **`cd`** to the **project root**, the folder that contains **`level3`** and **`.venv`**.
2. **Activate the venv** from that root.
   - **Windows PowerShell**: `.\.venv\Scripts\Activate.ps1`
   - **Windows Command Prompt**: `.venv\Scripts\activate.bat`
   - **macOS or Linux**: `source .venv/bin/activate`
3. Run **`cd level3`**.
4. Create **`logs`** if needed: **`mkdir -p logs`** on macOS or Linux, or **`mkdir logs`** on Windows when the folder is missing.
5. From **`level3`**, run:

   ```bash
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

   Leave the window open. When the server is listening, open a browser at **http://localhost:5005**. If the chat does not load, try **http://localhost:5005/webhooks/socketio/inspect.html**.

**Local troubleshooting**

- **`No module named 'rasa'`**, Reactivate the venv, **`cd level3`**, install **`rasa-pro`** if needed.
- **License or API key errors**, Match your **Lab 6.1** environment. Fix **`.env`** or shell exports, open a fresh terminal, **`cd level3`**, run **`python -m rasa inspect`** again.
- **Port 5005 in use**, Stop other Rasa processes or run  
  **`python -m rasa inspect --debug --log-file logs/logs.out --port 5006`**  
  and open **http://localhost:5006** or **http://localhost:5006/webhooks/socketio/inspect.html**.

Repeat the same chat tests as in Part 1.

---

## Check Your Knowledge

{Check It!|assessment}(multiple-choice-2446085116)

{Check It!|assessment}(multiple-choice-3751028362)

{Check It!|assessment}(multiple-choice-2697467428)
