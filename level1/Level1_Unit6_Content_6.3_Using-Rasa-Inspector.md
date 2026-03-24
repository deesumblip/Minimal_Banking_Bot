### 6.3 Using Rasa Inspector

**Inspector** is Rasa's built-in testing interface. It lets you chat with your agent in a web page so you can see how it responds. You start it from the **terminal**, then open the chat in your **browser** or in Codio's Rasa Inspect tab.

**Why use Inspector**: You need a way to try the agent without deploying it. Inspector gives you a chat UI and, in debug mode, shows which flow triggered and what the LLM understood. That makes it easy to check that "when are you open?" hits the hours flow and that your descriptions and responses work as intended.

#### Step 1: Activate the virtual environment

1. **In the terminal, make sure you're in the right folder** with the venv active (same as Lab 6.1):
   - You should be in the `level1` folder (run `pwd`; you should see a path ending in `level1`).
   - Your prompt should start with `(.venv)`. If not, from the **main project folder (root)** run:
     ```bash
     source .venv/bin/activate
     cd level1
     ```

#### Step 2: Start Inspector in the terminal

From the `level1` folder (with venv active), run:

```bash
python -m rasa inspect --debug
```

**What you'll see**: The terminal will show a lot of output, including something like:
```
Starting Rasa server on http://0.0.0.0:5005
...
```
**Leave this terminal open.** Inspector is running as a server; if you close the terminal, it will stop.

#### Step 3: Open the chat in Codio

In Codio, go to the top menu bar and click the **Rasa Inspect** tab. The chat interface should open.

Try a few questions, for example:
- "How do I contact support?"
- "What can you do?"
- "Hi!"

At this stage the agent only uses simple responses, so the answers will be straightforward.

#### Inspector interface: what you see (beginner guide)

When Inspector opens, you'll see several areas. You don't need to understand every part to use it. Here's what matters at Level 1.

1. **Chat area (main part)**
   - This is where you type and where the agent's replies appear.
   - Use it like a normal chat: type a message, press Enter, and see what the agent says.
   - Your conversation history stays visible so you can scroll back.

2. **Flow / diagram area**
   - This shows which **flow** the agent is following right now (e.g. "greet", "help", "contact").
   - Think of it as "which conversation path the agent chose." When you type "Hi!", you should see something like the greet flow; when you ask for help, the help flow.
   - If the wrong flow appears for what you said, you can use this to notice and then improve your flow descriptions later.

3. **Debug / technical details**
   - This area shows more technical information: which flow was triggered, what the agent "thought" your message meant, and so on.
   - You can ignore it at first. When something doesn't work as expected, this is where you can look to see why the wrong flow might have run.

4. **Slots**
   - Slots are for "remembering" information in a conversation. **In Level 1 we don't use them**, so this will be empty. You can ignore it until later levels.

**In short**: Use the **chat** to talk to your agent. Use the **flow** and **debug** areas to see which flow ran and to fix things when the agent doesn't do what you want.

#### Launching Rasa Inspector locally

If you're **not** using Codio and want to run Inspector on your own computer, follow the steps for your operating system. You'll need the `level1` project folder, a virtual environment with Rasa Pro installed, and **RASA_LICENSE** set. You can set it via a `.env` file in the project root; see Unit 0 and Lab 0.1.

**1. Go to your project folder**

- Open a terminal (or PowerShell on Windows).
- Navigate into the `level1` folder (the one that contains `config.yml`, `domain/`, and `data/`).
- Example: `cd C:\Users\You\Minimal_Banking_Agent\level1` or `cd ~/Minimal_Banking_Agent/level1`.

**2. Activate the virtual environment and start Inspector**

- **Windows (PowerShell)**  
  ```powershell
  .venv\Scripts\Activate.ps1
  python -m rasa inspect --debug
  ```
- **Windows (Command Prompt)**  
  ```cmd
  .venv\Scripts\activate.bat
  python -m rasa inspect --debug
  ```
- **macOS / Linux**  
  ```bash
  source .venv/bin/activate
  python -m rasa inspect --debug
  ```

Leave this terminal window open. When you see something like `Starting Rasa server on http://0.0.0.0:5005`, Inspector is running.

**3. Open Inspector in your browser**

- Open a web browser (Chrome, Firefox, Edge, etc.).
- Go to: **http://localhost:5005**  
  If that shows a status page or doesn't open the chat, try: **http://localhost:5005/webhooks/socketio/inspect.html**
- You should see the Inspector chat interface. Type a message and press Enter to talk to your agent.

**Troubleshooting (local)**

- **"No module named 'rasa'"** – Activate the virtual environment again and make sure Rasa is installed (`pip install rasa-pro`).
- **"RASA_LICENSE" not set** – Create or edit `.env` in the project root with `RASA_LICENSE=your-license` (no quotes), source it, then run `rasa inspect` again (see Lab 0.1).
- **"Address already in use" or port 5005 in use** – Another program is using port 5005. Close other Rasa or Python processes, or use a different port: `python -m rasa inspect --debug --port 5006` and then open **http://localhost:5006** (or …/inspect.html on 5006) in your browser.

---
