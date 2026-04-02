The banking_assistant sub-agent uses **MCP** (tools on a separate process). The main project must register the MCP server in `endpoints.yml`.

## MCP server registration in endpoints.yml

The sub-agent config references an MCP server by **name**. That name must appear under **`mcp_servers:`** in the main **`endpoints.yml`**, with **url** (Streamable HTTP, including **`/mcp`** for this repo) and **type** (`http`).

## Lab 3.1

Add **`mcp_servers`** to **`level6/endpoints.yml`** without removing other sections. The starter file may include a **commented** example; you add the real block in the lab. The script **`mcp_server/banking.py`** is provided.
