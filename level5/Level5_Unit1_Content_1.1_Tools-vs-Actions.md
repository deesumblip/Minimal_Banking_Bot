In Level 4 you used **actions**: steps in a flow explicitly call an action (e.g. `- action: action_process_transfer`). The agent always runs that action when the flow reaches that step.

**Tools** are different. They are **functions the LLM can choose to call** based on the conversation. The flow does not name a specific tool; instead, the LLM sees the available tools (e.g. check_balance, process_transfer, get_account_info) and decides which to call and when, depending on what the user said.

## Comparison

| | Actions | Tools |
|--|--------|-------|
| **Invoked by** | Flow step (`- action: action_name`) | LLM at runtime |
| **When** | When the flow reaches that step | When the LLM decides it fits the conversation |
| **Definition** | Python class in `actions/`, registered in domain | Python functions in `tools/`, registered in endpoints.yml |
| **Use case** | Predictable, required steps (e.g. "always run transfer after collecting slots") | Flexible operations (e.g. "user asked for balance? call check_balance") |

In Level 5 you add **tools** alongside your existing actions. The transfer_money_tools flow still collects slots, but then runs an **action** (action_process_transfer_with_tools) inside which the **LLM can call tools** (check_balance, process_transfer, get_account_info) as needed.

## Example: What you already have (actions)

In Level 4 a flow step explicitly calls an action. For example, in a transfer flow you might see:

```yaml
steps:
  - collect: amount
    description: "amount to transfer"
  - collect: recipient
    description: "recipient"
  - collect: account_from
    description: "source account"
  - action: action_process_transfer
```

When the flow reaches that last step, the agent **always** runs `action_process_transfer`. There is no choice at runtime.

## Example: What tools look like (Python functions)

Tools are plain Python functions in a `tools/` module. The LLM sees their names and docstrings and decides when to call them. For example, in `tools/banking_tools.py` you will have functions like:

```python
def check_balance(account: str) -> dict:
    """Check the balance for a given account."""
    return {"account": account, "balance": 1234.56, "currency": "USD"}
```

The flow does **not** list this function. The LLM chooses to call it when the user asks for a balance. Later in this chapter you will create the **`tools`** module, register it in **`endpoints.yml`**, and connect it to a flow.
