**Starting point:** Work in **`level5/`** from the Chapter 1.4 completion baseline (**Unit 0.1**).

In Chapter 1.4, **custom actions** are what the flow names at an **`action:`** step—for example **`- action: action_process_transfer`**. When execution reaches that step, that action **always** runs.

**Collect** steps use **`utter_ask_*`** responses (for example **`utter_ask_amount`**). Those names appear under **`actions:`** in the domain. **`action:`** steps point at **Python** classes in **`actions/`**.

**Tools** work differently. They are **functions the LLM may call** at runtime. The flow never lists a tool by name. The model sees registered tools (for example **check_balance**, **process_transfer**, **get_account_info**) and chooses which to invoke from the user’s wording.

## Comparison

| | Actions | Tools |
|--|--------|-------|
| **Invoked by** | Flow step (`- action: action_name`) | LLM at runtime |
| **When** | When the flow reaches that step | When the LLM decides it fits the conversation |
| **Definition** | Python class in `actions/`, registered in domain | Python functions in `tools/`, registered in endpoints.yml |
| **Use case** | Predictable, required steps (e.g. "always run transfer after collecting slots") | Flexible operations (e.g. "user asked for balance? call check_balance") |

Chapter 1.5 adds **tools** next to your existing actions. The **`transfer_money_tools`** flow still collects slots, then runs one **action** (`action_process_transfer_with_tools`).

In that step’s context, the **LLM** may call your **tools** (`check_balance`, `process_transfer`, `get_account_info`, …) as needed.

## Example: Actions in a flow

In Chapter 1.4 a flow step explicitly calls an action. For example, in a transfer flow you might see:

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

The flow does **not** list this function. The LLM calls it when the user’s message fits the tool’s intent. You implement and register tools in **Labs 2.1** and **3.1**, then use them from the flow in **Lab 4.1**.
