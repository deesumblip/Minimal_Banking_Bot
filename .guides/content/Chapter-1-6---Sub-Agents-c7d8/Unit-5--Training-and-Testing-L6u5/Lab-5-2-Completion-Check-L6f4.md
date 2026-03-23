**Objective.** Run a completion check to verify that your Level 6 bot has all required components: sub_agents/banking_assistant config, mcp_servers in endpoints.yml, ask_banking_assistant flow, and (optionally) a trained model.

## Step-by-Step Instructions

**Step 1.** Ensure you have completed Labs 2.1, 3.1, and 4.1 (sub-agent config, MCP registration, flow file). Optionally complete Lab 5.1 (training).

**Step 2.** **In Codio**, use **Check It!** below. The grader will check for: level6/sub_agents/banking_assistant/config.yml, level6/endpoints.yml with mcp_servers, level6/data/basics/ask_banking_assistant.yml with a flow that has `call: banking_assistant`, and optionally level6/models/ or successful train.

**Step 3.** Optionally start the MCP server, action server, and Rasa; open Inspector and trigger the ask_banking_assistant flow to confirm the sub-agent runs.

{Check It!|assessment}(code-output-compare-501060005)

## Running locally

From project root activate the venv, `cd level6`. Ensure your files match the labs above; **Check It!** graded runs are in Codio only.
