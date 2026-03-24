To test the sub-agent:

1. **Start the MCP server** (if your setup uses one), e.g. from level6: `python mcp_server/banking.py` (or the script that starts the banking MCP server on the URL you set in endpoints.yml, e.g. http://localhost:8080).
2. **Start the action server**, from level6: `rasa run actions`.
3. **Start Rasa**, from level6: `rasa run` or `rasa inspect`.
4. **Open Inspector** (e.g. Rasa Inspect tab on Codio, or http://localhost:5005/.../inspect). Trigger the "ask banking assistant" flow (e.g. say you want to talk to the banking assistant). Confirm the main agent runs the flow and the sub-agent handles the conversation until completion, then control returns.

**Lab 5.2** is a completion check: it verifies that sub_agents config, endpoints mcp_servers, ask_banking_assistant flow, and (optionally) a trained model are in place.
