**Objective.** In Unit 2 you saw an example of the sub-agent config (agent name, protocol, description, LLM, mcp_servers). In this lab you will create your own version: the folder `level6/sub_agents/banking_assistant/` and the file `config.yml` so the main agent can call the `banking_assistant` sub-agent.

## Step-by-Step Instructions

**Step 1.** In the `level6` folder, create the directory `sub_agents/banking_assistant/` (if it does not exist).

**Step 2.** Create `sub_agents/banking_assistant/config.yml` with:
- `agent:` with `name: banking_assistant`, `protocol: RASA`, and a `description:` (e.g. helps with balance, transfers, banking questions using MCP tools).
- `configuration:` with `llm:` and `model_group:` (e.g. gpt-4o-mini) matching your config.
- `connections:` with `mcp_servers:` listing the name of the MCP server (e.g. `banking_mcp`, you will register it in Lab 3.1).

**Step 3.** Verify: the file exists at `level6/sub_agents/banking_assistant/config.yml` and has the required keys. **Use Check It!** below when done (Codio).

{Check It!|assessment}(code-output-compare-501060001)

## Running locally

From project root activate the venv, `cd level6`. Create the folder and config file as above.
