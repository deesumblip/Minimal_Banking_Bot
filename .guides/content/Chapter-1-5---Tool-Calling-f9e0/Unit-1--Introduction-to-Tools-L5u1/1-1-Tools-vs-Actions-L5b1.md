In Level 4 you used **actions**: steps in a flow explicitly call an action (e.g. `- action: action_process_transfer`). The bot always runs that action when the flow reaches that step.

**Tools** are different. They are **functions the LLM can choose to call** based on the conversation. The flow does not name a specific tool; instead, the LLM sees the available tools (e.g. check_balance, process_transfer, get_account_info) and decides which to call and when, depending on what the user said.

## Comparison

| | Actions | Tools |
|--|--------|-------|
| **Invoked by** | Flow step (`- action: action_name`) | LLM at runtime |
| **When** | When the flow reaches that step | When the LLM decides it fits the conversation |
| **Definition** | Python class in `actions/`, registered in domain | Python functions in `tools/`, registered in endpoints.yml |
| **Use case** | Predictable, required steps (e.g. "always run transfer after collecting slots") | Flexible operations (e.g. "user asked for balance? call check_balance") |

In Level 5 you add **tools** alongside your existing actions. The transfer_money_tools flow still collects slots, but then runs an **action** (action_process_transfer_with_tools) inside which the **LLM can call tools** (check_balance, process_transfer, get_account_info) as needed.
