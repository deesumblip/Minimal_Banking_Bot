After adding the sub-agent config, MCP registration, and the ask_banking_assistant flow, **train** the Level 6 agent.

From **project root**, activate the venv, then:

- `cd level6`
- `rasa train`

A model is created in `level6/models/`. Use the same venv as Level 1–5 (no new venv in level6). The trained assistant will include the new flow and sub-agent so the main agent can call the banking_assistant when the flow is triggered.

**Lab 5.1** is graded (training). **In Codio**, use **Check It!** after training completes.
