**Starting point:** Work in **`level5/`** (Chapter 1.4 completion in **Unit 0.1**; what Chapter 1.5 adds in **Unit 0.2**).

In Chapter 1.4 you used **actions**: a flow step names an action (for example **`- action: action_process_transfer`**). When the flow reaches that step, the agent **always** runs that action.

**Tools** are different. They are **functions the LLM may choose to call** at runtime. The flow does not list a tool by name; the LLM sees the registered tools (for example **check_balance**, **process_transfer**, **get_account_info**) and decides which to call and when, from what the user said.

## Comparison

| | Actions | Tools |
|--|--------|-------|
| **Invoked by** | Flow step (`- action: action_name`) | LLM at runtime |
| **When** | When the flow reaches that step | When the LLM decides it fits the conversation |
| **Definition** | Python class in `actions/`, registered in domain | Python functions in `tools/`, registered in endpoints.yml |
| **Use case** | Predictable, required steps (e.g. "always run transfer after collecting slots") | Flexible operations (e.g. "user asked for balance? call check_balance") |

In Chapter 1.5 you add **tools** alongside your existing actions. The **`transfer_money_tools`** flow still collects slots, then runs one **action** (`action_process_transfer_with_tools`). Inside that step’s context, the **LLM** can call your **tools** (`check_balance`, `process_transfer`, `get_account_info`, …) as needed.

## Example: What you already have (actions)

In Chapter 1.4 a flow step explicitly calls an action. For example, in a transfer flow you might see:


steps:
  - collect: amount
    description: "amount to transfer"
  - collect: recipient
    description: "recipient"
  - collect: account_from
    description: "source account"
  - action: action_process_transfer

When the flow reaches that last step, the agent **always** runs `action_process_transfer`. There is no choice at runtime.

## Example: What tools look like (Python functions)

Tools are plain Python functions in a `tools/` module. The LLM sees their names and docstrings and decides when to call them. For example, in `tools/banking_tools.py` you will have functions like:


def check_balance(account: str) -> dict:
    """Check the balance for a given account."""
    return {"account": account, "balance": 1234.56, "currency": "USD"}

The flow does **not** list this function. The LLM chooses to call it when the user’s message matches the tool’s intent. In the next units you will create a full **`tools`** module and register it in **`endpoints.yml`**, then use it from a flow in **Lab 4.1**.
