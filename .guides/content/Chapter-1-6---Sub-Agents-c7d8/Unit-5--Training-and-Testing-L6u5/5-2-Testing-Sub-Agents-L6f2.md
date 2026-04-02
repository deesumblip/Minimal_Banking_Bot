To test the sub-agent, run **three processes** from **`level6/`** (use a separate terminal for each):

```bash
# Terminal 1 — MCP server (URL must match endpoints.yml, e.g. http://127.0.0.1:8080/mcp)
python mcp_server/banking.py

# Terminal 2 — action server
python -m rasa run actions

# Terminal 3 — Rasa (inspect UI recommended)
rasa inspect
# or: rasa run
```

Then **open Inspector** (e.g. **`http://localhost:5005/webhooks/socketio/inspect.html`**). Start a **new chat**, then trigger the **ask banking assistant** flow.

Confirm: the main agent runs the flow, the **banking_assistant** sub-agent handles the banking request (via MCP tools), then control returns (e.g. **`utter_help`**).

---

## Clean demo script (recommended)

The **SearchReady** command generator may start **`check_balance`** or **`transfer_money`** if the user only says “check my balance” without naming the sub-agent—**interrupting** the stacked flow. For a **clean recording**, use **one user message** that names the **banking assistant** (or **sub-agent**) **and** states the request.

**Suggested order (new chat):**

1. **Greeting:** `Hi!`
2. **Sub-agent + balance:** `Please use the banking assistant sub-agent to check my balance for account 88889999.`
3. **Sub-agent + transfer:** `I want the banking assistant to transfer $25 from my account 11112222 to account 33334444.`
4. **Sub-agent + account info:** `Ask the specialist banking assistant for account info on 88889999.`
5. **Institutional (non-competing):** `What are your hours?`

**Avoid in a “clean” demo** (optional stress tests only): a short message like `Check balance for 88889999` **without** “banking assistant” — that often routes to the main **`check_balance`** flow instead of the sub-agent.

**Lab 5.2** is a completion check: it verifies that sub_agents config, endpoints **`mcp_servers`**, **`ask_banking_assistant`** flow, and (optionally) a trained model are in place.
