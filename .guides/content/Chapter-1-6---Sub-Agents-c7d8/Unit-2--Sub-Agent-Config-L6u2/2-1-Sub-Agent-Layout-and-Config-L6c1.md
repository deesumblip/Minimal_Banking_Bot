A sub-agent lives in a folder under `sub_agents/<name>/`. Rasa discovers it by name (e.g. `banking_assistant`). The main agent calls it with `call: banking_assistant` in a flow step.

## Layout

- **Folder:** `level6/sub_agents/banking_assistant/`
- **Config file:** `sub_agents/banking_assistant/config.yml` — defines the agent’s name, protocol (e.g. RASA for ReAct), description, LLM configuration, and which MCP server(s) it uses.

## Example: Sub-agent config

Below is an example of a ReAct sub-agent config. You will create your own version in Lab 2.1 (e.g. with a description that fits your bot). The sub-agent uses an LLM and connects to one MCP server named `banking_mcp` (you will register that server in endpoints.yml in Lab 3.1).

```yaml
agent:
  name: banking_assistant
  protocol: RASA
  description: "Helps users with balance checks, transfers, and general banking questions using MCP tools."

configuration:
  llm:
    model_group: gpt-4o-mini

connections:
  mcp_servers:
    - name: banking_mcp
```

- **agent.name** — Must match the name you use in the flow step (`call: banking_assistant`).
- **agent.protocol** — `RASA` for the built-in ReAct sub-agent (LLM + MCP tools).
- **agent.description** — Helps the orchestrator and LLM understand when to use this sub-agent.
- **configuration.llm.model_group** — Model group ID from your config (e.g. gpt-4o-mini).
- **connections.mcp_servers** — List of MCP server names; each must be defined in `endpoints.yml` under `mcp_servers`.

In **Lab 2.1** you will create the folder `level6/sub_agents/banking_assistant/` and add `config.yml` with your own version of this config.
