# Level 5 Additional Resources

## Extension Exercises

### Exercise 1: Add another tool

**Task**: Add a fourth tool to `tools/banking_tools.py`, e.g. `close_account(account: str)` that returns a dict with a confirmation message. Add it to `__all__`. Train and test; trigger a conversation where the LLM might use it.

**Goal**: Practice extending the tools module and discovery.

---

### Exercise 2: Different balances per account

**Task**: Modify `check_balance(account)` in `banking_tools.py` to return different mock balances for different account numbers (e.g. account "1001" -> 500.00, "1002" -> 1200.00, default -> 0.00).

**Goal**: Practice using parameters inside tool functions.

---

### Exercise 3: Tool that uses multiple parameters

**Task**: Add a tool `transfer_between_own_accounts(amount: str, from_account: str, to_account: str)` that "moves" money between two accounts (mock). Return a dict with success and new balances. Add to `__all__`.

**Goal**: Practice multi-parameter tools the LLM can call.

---

## What You Can Do Now

- Define tools as Python functions and register them in endpoints.yml
- Let the LLM choose which tools to call based on conversation context
- Combine flows (slot collection) with tool calling (action that runs in a tool-calling context)
- Extend the agent with new tools without changing flow structure

## What's Next

- **Level 6**: Sub-agents — delegate whole tasks to another agent (ReAct sub-agent) that uses its own tools (e.g. via MCP). The main agent orchestrates; the sub-agent runs until completion.
