**Inspector** is Rasa’s built-in testing UI. You start a small server from the terminal, then talk to the agent in a browser-like chat. In **Codio**, use the **Rasa Inspect** tab in the top menu. On your **own computer**, you open a normal browser to **localhost**, as described at the end of this page.

---

#### In Codio

##### Step 1: Virtual environment and folder

Stay in the same setup as **Lab 6.1**. You should be in **`level1`** with the venv active. Run **`pwd`** and check that the path ends with **`level1`**. Your prompt should start with **`(.venv)`**.

If the venv is not active, go to the **project root**, the folder above **`level1`** that contains **`.venv`**, then run:

```bash
source .venv/bin/activate
cd level1
```

##### Step 2: Logs folder

From **`level1`**, create a **`logs`** directory so Inspector can write its log file.

```bash
mkdir -p logs
```

##### Step 3: Start Inspector

From **`level1`**, with the venv still active, run:

```bash
python -m rasa inspect --debug --log-file logs/logs.out
```

The terminal will print a lot of output. You should see a line similar to the following.

```text
Starting Rasa server on http://0.0.0.0:5005
...
```

**Leave this terminal open.** Inspector is a server process. If you close the terminal, Inspector stops.

##### Step 4: Open the chat

Click the **Rasa Inspect** tab in the top menu. The chat view should load.

Type **hello** and press Enter. The agent should reply. Use the flow or debug panel to see which flow ran.

Try a few more messages, for example:

- "How do I contact support?"
- "What can you do?"
- "Hi!"

At this stage the agent uses simple responses, so replies stay short and direct.

---

**Use Check It!** when Inspector is running and you have exercised the chat.

{Check It!|assessment}(code-output-compare-2562507356)

---

#### Inspector interface: what you see

You do not need every panel for Level 1. These are the parts that matter first.

1. **Chat**  
   You type here and read the agent’s replies. Messages stay in view so you can scroll back.

2. **Flow or diagram**  
   This shows which **flow** is active, for example **greet**, **help**, or **contact**. It is the path the agent chose for your last turn. If the wrong flow appears, you will often fix it later by improving **description** text on flows.

3. **Debug or technical details**  
   This area lists what was triggered and related metadata. You can ignore it at first. When behavior is wrong, it helps explain why a flow fired.

4. **Slots**  
   Slots store remembered values across turns. Level 1 does not use them yet, so this area may stay empty.

**Summary**: Use **chat** to probe behavior. Use **flow** and **debug** when you need to see why a path was chosen.

---

#### Not using Codio? Launching Inspector locally

Use this path when you run the course on your own machine instead of the Codio workspace. You need the **`level1`** tree, Rasa Pro installed in your venv, and **`RASA_LICENSE`** set as in **Unit 0** and **Lab 0.1**.

1. Open a terminal and **`cd`** to the **project root**, the folder that contains **`level1`** and **`.venv`**.
2. **Activate the venv** from that root.
   - **Windows PowerShell**: `.\.venv\Scripts\Activate.ps1`
   - **Windows Command Prompt**: `.venv\Scripts\activate.bat`
   - **macOS or Linux**: `source .venv/bin/activate`
3. Run **`cd level1`** so your working directory is **`level1`**.
4. Create **`logs`** if it does not exist. On macOS or Linux use **`mkdir -p logs`**. On Windows use **`mkdir logs`** when the folder is missing.
5. With the venv still active, start Inspector from **`level1`**:

   **Windows PowerShell**

   ```powershell
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

   **Windows Command Prompt**

   ```cmd
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

   **macOS or Linux**

   ```bash
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

   Leave the window open. When you see a line such as **`Starting Rasa server on http://0.0.0.0:5005`**, the server is running.

6. Open a browser and go to **http://localhost:5005**. If you see a status page or the chat does not load, try **http://localhost:5005/webhooks/socketio/inspect.html**.

**Local troubleshooting**

- **`No module named 'rasa'`**, Activate the venv again, **`cd level1`**, and install Rasa Pro if needed: **`pip install rasa-pro==3.16.3`**.
- **`RASA_LICENSE` not set**, Set the variable the same way you did for training. **Lab 0.1** covers local options. Fix the environment, open a new terminal if needed, **`cd`** to **`level1`**, and run **`python -m rasa inspect`** again.
- **Address already in use or port 5005 in use**, Another process owns the port. Stop other Rasa or Python servers, or pick another port, for example:

  ```bash
  python -m rasa inspect --debug --log-file logs/logs.out --port 5006
  ```

  Then open **http://localhost:5006** or **http://localhost:5006/webhooks/socketio/inspect.html**.
