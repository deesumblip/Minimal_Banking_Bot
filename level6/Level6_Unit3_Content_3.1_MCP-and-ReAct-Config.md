The banking_assistant sub-agent uses **ReAct** (LLM + tools). In this course the tools are provided by an **MCP server**. The main project must register that MCP server in `endpoints.yml` so the sub-agent can connect to it.

## MCP server registration in endpoints.yml

The sub-agent config references an MCP server by **name** (e.g. `banking_mcp`). That name must be defined in the main agent’s `endpoints.yml` under `mcp_servers:`, with a URL and type.

## Example: mcp_servers in endpoints.yml

Below is an example of what you will add. You will add your own version in Lab 3.1. Do not remove existing sections (action_endpoint, nlg, tools, model_groups); add the `mcp_servers:` block.

```yaml
mcp_servers:
  - name: banking_mcp
    url: http://localhost:8080
    type: http
```

- **name** — Must match the name in the sub-agent’s `connections.mcp_servers` (e.g. `banking_mcp`).
- **url** — Where the MCP server is running (e.g. the banking MCP server started with `python mcp_server/banking.py` or similar, listening on port 8080).
- **type** — `http` for an HTTP MCP server.

In **Lab 3.1** you will add this block to `level6/endpoints.yml`. The MCP server itself (e.g. `mcp_server/banking.py`) may be provided or you may create it; the lab assessment verifies that `endpoints.yml` contains the `mcp_servers` entry.
