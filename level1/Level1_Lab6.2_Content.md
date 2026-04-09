# Lab 6.2: Using Rasa Inspector

**Objective**: Start Inspector and test a simple conversation.

**Why this lab**: You need to see the agent in action. Inspector is the place to do that: you start it, open the chat, and send messages. You'll see which flow runs and what the agent says. That confirms your training worked and gives you a baseline before you add more flows or move to Level 2.

---

1. **Terminal**: From the main project folder—the root where `level1` and `.venv` live—run `source .venv/bin/activate`, then `cd level1`. Your prompt should show `(.venv)` and you should be in `level1`.
2. **Create logs** (if needed): From `level1`, run `mkdir -p logs`.
3. **Start Inspector**: Run `python -m rasa inspect --debug --log-file logs/logs.out`. Wait for "Starting Rasa server on http://0.0.0.0:5005". Leave the terminal open.
4. **Open Inspector**: In the top menu bar, click the **Rasa Inspect** tab. The chat interface opens.
5. **Test**: In the chat, type **hello** and press Enter. The agent should respond. Check the flow/debug panel to see which flow triggered.
