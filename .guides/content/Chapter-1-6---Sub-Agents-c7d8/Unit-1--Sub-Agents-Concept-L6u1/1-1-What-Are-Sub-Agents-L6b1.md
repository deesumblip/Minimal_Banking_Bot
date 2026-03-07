A **sub-agent** is a separate agent that the main agent can **call** from a flow. When a flow step runs `call: agent_name`, the main agent hands off to that sub-agent; the sub-agent runs (e.g. using its own LLM and tools) until it signals completion (e.g. `task_completed`), then control returns to the main flow.

## Comparison

| | Main agent only (Level 5) | With sub-agent (Level 6) |
|--|---------------------------|---------------------------|
| **Who does the work** | One agent; tools called in one action context | Main agent can delegate a **whole task** to another agent |
| **Flow step** | `action: action_process_transfer_with_tools` | `call: banking_assistant` (sub-agent runs until done) |
| **Use case** | Single conversation with tool calls | Orchestration: "let the banking assistant handle this" |

## Example: What a call step looks like

In Level 6 you will add a flow whose steps include **calling** a sub-agent. The flow does not list the sub-agent’s internal steps; it has one step that hands off:

```yaml
steps:
  - call: banking_assistant
  - action: utter_help
```

When the flow reaches `call: banking_assistant`, the **banking_assistant** sub-agent runs (with its own LLM and MCP tools). When the sub-agent finishes, the main flow continues with `action: utter_help`. So the user "talks to the banking assistant" until that agent is done, then the main bot can offer help again.
