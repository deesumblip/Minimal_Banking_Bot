## 5.2 Testing and completion (Lab 5.2)

This page has two parts in order: **Lab 5.2** (graded completion check), then **optional** steps to run the full stack in Inspector.

### Prerequisites

- Labs **2.1**, **3.1**, and **4.1** done: **`sub_agents/banking_assistant/config.yml`**, **`mcp_servers`** in **`endpoints.yml`**, **`data/basics/ask_banking_assistant.yml`**.
- Lab **5.1** (training) is **recommended** so **`level6/models/`** exists; the Lab 5.2 grader may still pass in some setups without it.

### Part 1 — Lab 5.2 (graded, Codio)

Use **Check It!** below. The grader checks for the files above, **`call: banking_assistant`** in the flow, and optionally a trained model.

{Check It!|assessment}(code-output-compare-501060005)

### Part 2 — Optional: Inspector (full stack)

To see the sub-agent in the browser, run **three processes** in **three separate terminals**. **Every time you open a new terminal**, run the same first two lines (activate venv from **project root**, then **`cd level6`**) before the command for that role.

**Terminal 1 — MCP** (must match **`mcp_servers.url`** in **`endpoints.yml`**, e.g. **`http://127.0.0.1:8080/mcp`**):

```bash
# Windows: .venv\Scripts\activate
source .venv/bin/activate

cd level6
python mcp_server/banking.py
```

**Terminal 2 — action server**

```bash
# Windows: .venv\Scripts\activate
source .venv/bin/activate

cd level6
python -m rasa run actions
```

**Terminal 3 — Rasa (Inspector recommended)**

```bash
# Windows: .venv\Scripts\activate
source .venv/bin/activate

cd level6
rasa inspect
# or: rasa run
```

Open **Inspector** (e.g. **`http://localhost:5005/webhooks/socketio/inspect.html`**). Start a **new chat**, then trigger the **ask banking assistant** flow. You should see the main agent start the flow, the **banking_assistant** sub-agent handle the turn via MCP, then control return (e.g. **`utter_help`**).

#### Demo phrasing (recommended)

SearchReady may start **`check_balance`** or **`transfer_money`** if the user only asks for a balance **without** naming the sub-agent. For a **clean** demo, use **one** message that names the **banking assistant** (or **sub-agent**) **and** states the request, for example:

- `Please use the banking assistant sub-agent to check my balance for account 88889999.`
- `I want the banking assistant to transfer $25 from my account 11112222 to account 33334444.`

**Avoid** (unless stress-testing): a short line like `Check balance for 88889999` with no “banking assistant” — that often routes to the main **`check_balance`** flow instead of the sub-agent.
