# Level 6: Sub-Agents

This folder is the **Level 6** banking agent (Level 5 behavior plus **sub-agent orchestration**).

## Starter repo vs. lab deliverables

The repo **includes** the main agent, domain, flows from Level 5, tools, **`actions/banking_assistant_lite_agent.py`** (tutorial-compatible sub-agent implementation), and the **MCP server** script. **`rasa train`** / `rasa inspect` for the full Level 6 story assume you have **completed Labs 2.1–4.1** (see Chapter 1.6).

**You add in Labs 2.1–4.1** (not committed in the starter tree). **Same workflow as Chapters 1.4–1.5:** complete the **Fill in the blanks** in the guide for each lab, **copy or merge** the passed YAML into the path below, then run the **Code Test** (**Check It!**).

- **`sub_agents/banking_assistant/config.yml`** (Lab 2.1 fill-in → `501060111`)
- **`mcp_servers:`** in **`endpoints.yml`** (Lab 3.1 fill-in → `501060112`; starter may show commented hints only)
- **`data/basics/ask_banking_assistant.yml`** (Lab 4.1 fill-in → `501060110`)

## What is in this folder

- **Main agent:** `config.yml` (SearchReady + `prompt_template` → `data/prompts/command_prompt_v3_slot_names.jinja2`), `domain/basics.yml`, `credentials.yml`, `endpoints.yml` (`action_endpoint`, `nlg`, `tools`, `model_groups`; add **`mcp_servers`** in Lab 3.1).
- **Sub-agent (your Lab 2.1 file):** `sub_agents/banking_assistant/config.yml` — the folder exists with **`.gitkeep`** only until you create the config. Implementation class: **`actions/banking_assistant_lite_agent.py`** (provided).
- **Flows:** `data/basics/` includes greet, help, contact, hours, check_balance, transfer_money, transfer_money_tools. You **add** **`ask_banking_assistant.yml`** in Lab 4.1.
- **Actions & tools:** `actions/` (including `action_process_transfer_with_tools`), `tools/banking_tools.py`.
- **MCP server:** `mcp_server/banking.py` — **Streamable HTTP** MCP (FastMCP). After Lab 3.1, **`mcp_servers.url`** should match this server (e.g. **`http://127.0.0.1:8080/mcp`**).

Follow the **Chapter 1.6** Unit/Lab pages to create the three deliverables above, then **validate**, **train**, and test.

## Environment (Rasa license only)

This course deployment passes **only `RASA_LICENSE`** (no separate OpenAI or other vendor API keys).

- Set **`RASA_LICENSE`** before `rasa train` / `rasa run` / `rasa inspect`.
- **`endpoints.yml`** uses **`provider: rasa`** and **`https://tutorial-llm.rasa.ai`** for model group **`gpt-4o-mini`** (main agent NLG, command generator, and sub-agent **`llm`** all reference that group).

**Flow retrieval:** **`config.yml`** sets **`flow_retrieval.active: false`** so training does not require OpenAI embeddings for semantic flow retrieval.

### Sub-agent runtime (tutorial LLM + `RASA_LICENSE` only)

The stock **`MCPOpenAgent`** ReAct loop sends **tool definitions** on every LLM call; the **tutorial LLM** host does not support that API shape. This project therefore sets **`configuration.module`** to **`actions.banking_assistant_lite_agent.BankingAssistantLiteAgent`**, a subclass that:

1. **Routes** user text to MCP tools (`check_balance`, `process_transfer`, `get_account_info`) with simple, explainable rules.
2. Uses the same **`model_group`** for **text-only** completions to polish replies—compatible with **`provider: rasa`** and **`https://tutorial-llm.rasa.ai`**.

For Chapter **1.6**, you still demonstrate **delegation** (`call: banking_assistant`), **MCP-backed tools**, and a **specialist sub-agent**; the implementation trades default multi-step ReAct for a **deterministic router** so demos work in Codio without a separate vendor API key.

Optional PowerShell: `$env:RASA_LICENSE = "…"` before Rasa commands, or load from a `.env` file with a small script (do not commit secrets).

## Train and validate

Use the **same virtual environment** as the rest of the course (typically **`.venv`** at **Minimal_Banking_Bot** repo root). From project root:

```powershell
.\.venv\Scripts\Activate.ps1
cd level6
```

Then:

```text
python -m rasa data validate
python -m rasa train
```

After Labs 2.1–4.1, `rasa data validate` should report sub-agents loaded (e.g. `banking_assistant`) and flows validated.

## Run the full stack (Inspector / local test)

Use **three terminals**. In **each** new terminal, from **project root** activate **`.venv`**, then **`cd level6`**, then run **one** of the roles below (same pattern as Chapter 1.6 Unit **5.2**):

1. **MCP:** `python mcp_server/banking.py` (Streamable HTTP at **`http://127.0.0.1:8080/mcp`**).
2. **Actions:** `python -m rasa run actions`
3. **Rasa Inspector:** `python -m rasa inspect` (or `powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1` — logs to **`level6/logs/inspect.log`**).

**Inspector UI:** open **`http://localhost:5005/webhooks/socketio/inspect.html`** in your browser. If **5005** is busy, run **`python -m rasa inspect -p 5025`** and use **`5025`** in that URL.

Start a **new chat** in Inspector, then try the example under **Illustrating sub-agents** below.

**Short messages (e.g. “Hi!”):** The command prompt (`data/prompts/command_prompt_v3_slot_names.jinja2`) instructs the SearchReady model to emit **`start flow greet`** for greeting-only turns so Inspector does not fall into **`pattern_cannot_handle`**. Retrain after prompt edits (`rasa train`) so the new wording is baked into the model package.

**Debug logs (full stack in background):** `powershell -ExecutionPolicy Bypass -File level6/scripts/run-stack-inspector-debug.ps1` — writes timestamped files under **`level6/logs/`** (MCP, **`rasa run actions -vv`**, **`rasa inspect -vv --log-file …`**). **`run_inspector.ps1`** alone runs only Inspector with **`-vv`** and **`logs/inspect.log`** (start MCP + actions separately).

### Illustrating sub-agents (what we verified)

With MCP + actions + Rasa running, the **SearchReady** command generator can emit **`start flow ask_banking_assistant`**. The tracker then shows **`flow_started`** for **`ask_banking_assistant`**, **`agent_started`** for **`banking_assistant`**, and bot metadata **`utter_source`: `BankingAssistantLiteAgent`** — that is the sub-agent path.

**Reliable demo (single user turn):** Ask for the **sub-agent** and include a concrete request in the **same** message so the specialist can call MCP without another main-agent flow stealing the turn, for example:

> “Please use the banking assistant sub-agent to check my balance for account **88889999**.”

You should see a balance line consistent with the demo MCP (e.g. **$123.45**), then the flow can continue to **`utter_help`**.

**Follow-up turns:** A later message like “check my balance for account …” can still produce **`start flow check_balance`** from the command LLM (another flow **interrupts** the stack). Flow descriptions discourage that, but the LLM does not always obey them. For a clean **Chapter 1.6** recording, prefer the **one-shot** example above.

If the MCP server URL or port changes, update `mcp_servers` in `endpoints.yml` to match.

## Smoke test and logs (troubleshooting)

From the repo root, with **`.venv`** available:

```powershell
powershell -ExecutionPolicy Bypass -File level6/scripts/run-smoke-with-logs.ps1
```

This starts **MCP** (port **8080**), **`rasa run actions`** (default **5055**), and **`rasa run --enable-api`** (default **5005**), then calls **`/version`**, **`/status`**, and **`POST /webhooks/rest/webhook`** with `"hi"`. It writes timestamped files under **`level6/logs/`** (`mcp-*.log`, `actions-*.log`, `rasa-*.log`, `smoke-*.summary.txt`). Log contents are gitignored; keep copies when reporting issues.

If **`OSError: ... bind ... 5005`** (or **8080**) appears in `rasa-*.err.log`, another process is already using that port—stop it or run:

```powershell
powershell -ExecutionPolicy Bypass -File level6/scripts/run-smoke-with-logs.ps1 -RasaPort 5006
```

(and use `http://127.0.0.1:5006` for manual tests). Use **`-SkipStop`** to leave the three processes running after the probes.
