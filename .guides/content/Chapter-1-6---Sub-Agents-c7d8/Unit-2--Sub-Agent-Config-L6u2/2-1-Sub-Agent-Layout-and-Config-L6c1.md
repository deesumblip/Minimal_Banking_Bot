A sub-agent lives in a folder under `sub_agents/<name>/`. Rasa discovers it by name (e.g. `banking_assistant`). The main agent calls it with `call: banking_assistant` in a flow step.

## Layout

- **Folder:** `level6/sub_agents/banking_assistant/` (you create this in Lab 2.1; the starter repo may ship an empty folder with **`.gitkeep`** only).
- **Config file:** `sub_agents/banking_assistant/config.yml` — defines the agent’s name, protocol (e.g. RASA), description, LLM **`model_group`**, **`configuration.module`**, and which MCP server name(s) it uses under **`connections.mcp_servers`**.

## What goes in `config.yml` (Lab 2.1)

You **author** this file in the lab; it is not copy-pasted from the starter tree. It must include:

- **`agent`:** `name` (must match `call:` in the flow), `protocol`, `description`.
- **`configuration.llm`:** `model_group` matching **`endpoints.yml`** (e.g. `gpt-4o-mini`).
- **`configuration.module`:** **`actions.banking_assistant_lite_agent.BankingAssistantLiteAgent`** — required in this course so the **Rasa tutorial LLM** works without a separate vendor API key. The class **`BankingAssistantLiteAgent`** is **provided** under **`actions/`**; you reference it, you do not reimplement it in the lab.
- **`connections.mcp_servers`:** at least one **name** (e.g. `banking_mcp`) that you will register in **`endpoints.yml`** in Lab 3.1.

**Why `module`:** The default ReAct sub-agent sends **tool definitions** on every LLM call; the tutorial host does not support that API shape. The **Lite** agent routes user text to MCP tools with simple rules and uses the same **`model_group`** for **text-only** completions.

In **Lab 2.1** you first complete a **Fill in the blanks** exercise (full **`config.yml`** skeleton), **copy** the passed YAML into **`level6/sub_agents/banking_assistant/config.yml`**, then run the **Code Test** — same **fill-in → copy → Check It!** pattern as **Chapter 1.5 Lab 2.1** (`banking_tools.py`).
