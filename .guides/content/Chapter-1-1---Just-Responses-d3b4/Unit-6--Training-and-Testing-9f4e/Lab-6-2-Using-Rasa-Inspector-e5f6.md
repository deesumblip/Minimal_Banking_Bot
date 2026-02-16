**Objective**: Start Inspector and test a simple conversation.

#### Steps

1. **Terminal**: Be in `level1` with venv active (`cd level1`, `source .venv/bin/activate`; prompt shows `(.venv)`).
2. **Start Inspector**: `python -m rasa inspect --debug --log-file logs/logs.out`. Wait for "Starting Rasa server on http://0.0.0.0:5005". Leave the terminal open.
3. **Open in browser**: **Tools** → **Ports** (or Preview/Ports). Find **port 5005**, click its URL (or "Open in browser"). Inspector opens in a new tab.
4. **Test**: In the chat, type **hello** and press Enter. The bot should respond. Check the flow/debug panel to see which flow triggered.

**AI Coach**: Ask "How do I access Inspector in Codio?" or "Why won't Inspector start?"
