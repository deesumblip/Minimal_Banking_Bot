**Objective**: Start Inspector and test a simple conversation.

---

## Part 1: In Codio

1. **Terminal**: From the main project folder (root, where `level1` and `.venv` live), run `source .venv/bin/activate`, then `cd level1`. Your prompt should show `(.venv)` and you should be in `level1`.
2. **Start Inspector**: Run `python -m rasa inspect --debug --log-file logs/logs.out`. Wait for "Starting Rasa server on http://0.0.0.0:5005". Leave the terminal open.
3. **Open Inspector**: In the top menu bar, click the **Rasa Inspect** tab. The chat interface opens.
4. **Test**: In the chat, type **hello** and press Enter. The bot should respond. Check the flow/debug panel to see which flow triggered.

**AI Coach**: Ask "How do I access Inspector in Codio?" or "Why won't Inspector start?"

---

## Part 2: Running locally

If you're on your own computer (not Codio), follow the steps below for your operating system.

### 1. Open a terminal and go to `level1`

- **Windows (PowerShell)**  
  Open PowerShell, then:
  ```powershell
  cd path\to\Minimal_Banking_Bot\level1
  ..\.venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt)**  
  Open Command Prompt, then:
  ```cmd
  cd path\to\Minimal_Banking_Bot\level1
  ..\\.venv\Scripts\activate.bat
  ```
- **macOS / Linux**  
  Open Terminal, then:
  ```bash
  cd ~/Minimal_Banking_Bot/level1
  source ../.venv/bin/activate
  ```

Use your actual project path. Your prompt should show `(.venv)`.

### 2. Start Inspector

From the `level1` folder with venv active:

- **Windows (PowerShell or Command Prompt)**  
  ```powershell
  python -m rasa inspect --debug --log-file logs/logs.out
  ```
- **macOS / Linux**  
  ```bash
  python -m rasa inspect --debug --log-file logs/logs.out
  ```

Wait for "Starting Rasa server on http://0.0.0.0:5005". Leave this terminal open.

### 3. Open Inspector in your browser

- Open a browser and go to **http://localhost:5005**.
- If you see a status page instead of the chat, try **http://localhost:5005/webhooks/socketio/inspect.html**.

### 4. Test

In the Inspector chat, type **hello** and press Enter. The bot should respond.

**Troubleshooting (local only):** If you see "Address already in use" or port 5005 is in use, run Inspector on another port: `python -m rasa inspect --debug --port 5006` and open **http://localhost:5006** (or …/inspect.html on 5006) in your browser.
