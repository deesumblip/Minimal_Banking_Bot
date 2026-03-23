**Objective.** In Unit 3 you saw an example of the `mcp_servers` block in endpoints.yml. In this lab you will add your own version to `level6/endpoints.yml`: register the MCP server (e.g. `banking_mcp`) with URL and type so the sub-agent can use it.

## Step-by-Step Instructions

**Step 1.** Open `level6/endpoints.yml`. Keep existing sections (action_endpoint, nlg, tools, model_groups) unchanged.

**Step 2.** Add a top-level key `mcp_servers:` with at least one entry, for example:
- `name: banking_mcp`
- `url: http://localhost:8080` (or the URL where your MCP server runs)
- `type: http`

**Step 3.** Save the file. Verify YAML is valid and the name matches the sub-agent config from Lab 2.1. **Use Check It!** below when done (Codio).

{Check It!|assessment}(code-output-compare-501060002)

## Running locally

From project root activate the venv, `cd level6`. Edit endpoints.yml as above.
