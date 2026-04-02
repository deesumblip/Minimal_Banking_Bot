A sub-agent lives in a folder under `sub_agents/<name>/`. Rasa discovers it by name (e.g. `banking_assistant`). The main agent calls it with `call: banking_assistant` in a flow step.

## Layout

- **Folder:** `level6/sub_agents/banking_assistant/` (create in Lab 2.1; starter may only have `.gitkeep`).
- **Config file:** `sub_agents/banking_assistant/config.yml` — you write this in Lab 2.1: `agent` (name, protocol, description), `configuration.llm.model_group`, **`configuration.module`** → `BankingAssistantLiteAgent`, `connections.mcp_servers` (names).

## Lab 2.1

Create **`config.yml`** with the required keys. The **`BankingAssistantLiteAgent`** class is provided under **`actions/`**; you set **`configuration.module`** to point at it. Register the MCP **name** in **`endpoints.yml`** in Lab 3.1.
