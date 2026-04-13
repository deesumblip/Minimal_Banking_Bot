The banking_assistant sub-agent uses **MCP** so tools run on a separate process. In this course the tools are provided by an **MCP server** implemented with **FastMCP** (**Streamable HTTP**). The main project must register that MCP server in `endpoints.yml` so the sub-agent can connect to it.

## MCP server registration in endpoints.yml

The sub-agent config references an MCP server by **name** (e.g. `banking_mcp`). That name must be defined in the main agent’s `endpoints.yml` under `mcp_servers:`, with a **URL** and **type**.

## What you add (Lab 3.1)

You **edit** the main project’s **`level6/endpoints.yml`** and add a top-level **`mcp_servers:`** list. Do **not** remove **`action_endpoint`**, **`nlg`**, **`tools`**, or **`model_groups`**.

Each entry needs:

- **`name`**, Must match the name in the sub-agent’s **`connections.mcp_servers`** (e.g. `banking_mcp`).
- **`url`**, Full URL for **Streamable HTTP**, including the path (for this repo’s server: **`http://127.0.0.1:8080/mcp`** when you run **`python mcp_server/banking.py`** from **`level6`** with defaults).
- **`type`**, `http` for the HTTP MCP transport used here.

Example shape for one MCP server (values must match your environment and Lab 3.1 fill-in):

```yaml
mcp_servers:
  - name: banking_mcp
    url: http://127.0.0.1:8080/mcp
    type: http
```

The starter **`endpoints.yml`** may show these lines **commented out** so you uncomment or type them in the lab. Follow your instructor’s starter.

In **Lab 3.1** you complete a **Fill in the blanks** for the **`mcp_servers`** block, **merge** it into **`endpoints.yml`**, then run the **Code Test** (same pattern as **Level 5 Lab 3.1**). The MCP implementation **`mcp_server/banking.py`** is **provided** in the repo. The lab checks that **`endpoints.yml`** registers it.
