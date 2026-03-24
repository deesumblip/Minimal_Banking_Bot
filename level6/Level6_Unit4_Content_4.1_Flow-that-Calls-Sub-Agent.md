To let users "talk to the banking assistant," you need a **flow** that the main agent can run and whose steps include **calling** the sub-agent. The flow does not implement the sub-agent’s behaviour; it has a step that hands off to the sub-agent by name.

## Example: The ask_banking_assistant flow

Below is an example of the flow file. You will create your own version in Lab 4.1 (e.g. with a name and description that fit your agent). The key step is `call: banking_assistant` — the name must match the sub-agent’s `agent.name` in its config.

```yaml
flows:
  ask_banking_assistant:
    name: ask banking assistant
    description: |
      Delegates to the banking assistant sub-agent (ReAct + LLM).
      The sub-agent uses MCP tools and runs until it calls task_completed.
    steps:
      - call: banking_assistant
      - action: utter_help
```

- **name** and **description** — Help the LLM know when to trigger this flow (e.g. user says they want to talk to the banking assistant).
- **steps** — First step `call: banking_assistant` runs the sub-agent until it completes; then `action: utter_help` runs so the main agent can offer help again.

In **Lab 4.1** you will create the file `level6/data/basics/ask_banking_assistant.yml` with your own version of this flow. When you are done, run the assessment for Lab 4.1.
