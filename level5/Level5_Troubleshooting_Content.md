# Level 5 Troubleshooting Guide

## Common Issues and Solutions

### Issue: Tools module not found / tools_module error

**Symptoms**: Training or run error referring to tools module or tools_module.

**Possible Causes**:
1. `tools/` folder missing in level5
2. `tools/__init__.py` or `tools/banking_tools.py` missing
3. `endpoints.yml` missing `tools:` section or `tools_module: "tools"`

**Solutions**:
1. Create `level5/tools/` with `__init__.py` and `banking_tools.py` (Lab 2.1)
2. Add to `endpoints.yml`: `tools:` and `tools_module: "tools"` (Lab 3.1)
3. Ensure you are running from the level5 directory (or that Rasa is started with the correct project path)

---

### Issue: Action action_process_transfer_with_tools not found

**Symptoms**: Training error: action not found.

**Possible Causes**:
1. Action file not in `level5/actions/`
2. Action not in domain `actions:` list
3. `name()` return value does not match exactly

**Solutions**:
1. Create `level5/actions/action_process_transfer_with_tools.py` (Lab 4.1)
2. Add `- action_process_transfer_with_tools` under `actions:` in `domain/basics.yml`
3. Ensure `name(self)` returns `"action_process_transfer_with_tools"`

---

### Issue: LLM never calls my tools

**Symptoms**: The transfer_money_tools flow runs but the agent does not seem to call check_balance or process_transfer.

**Possible Causes**:
1. Tools not registered (endpoints.yml) or not in __all__
2. Flow or action not correctly set up for tool-calling context (implementation depends on Rasa version)
3. OPENAI_API_KEY not set or invalid

**Solutions**:
1. Verify `endpoints.yml` has `tools:` and `tools_module: "tools"`; verify `tools/banking_tools.py` has `__all__ = ["check_balance", "process_transfer", "get_account_info"]`
2. Check Rasa docs for your version: tool calling may require a specific pipeline or action pattern
3. Set OPENAI_API_KEY in .env or environment before running Rasa

---

### Issue: Import or syntax error in banking_tools.py

**Symptoms**: Training fails with ImportError or SyntaxError in tools module.

**Solutions**:
1. Check that `banking_tools.py` has no syntax errors and that all three functions are defined with correct signatures
2. Ensure `__all__` is a list of strings matching the function names
3. Run `python -c "from tools.banking_tools import check_balance, process_transfer, get_account_info"` from level5 to test the module
