# Level 5 Troubleshooting Guide

**Open in \`level5/\`:** All paths and commands below refer to the **`level5/`** agent directory.

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

---

### Issue: Slot filling fails or fallback during collect flows

**Symptoms**: The bot asks for a slot but then fails to accept your reply, shows a generic “unable to understand” style response, or ignores a value you gave in the **same message** as starting the flow.

**Tips**:
1. When the bot asks for a slot, answer with a **short, literal** value for that slot (for example `100` or `100 dollars` for amount; account numbers as plain digits).
2. In **CALM**, slot values often come from **LLM-based extraction**; informal or noisy phrasing can be missed. Plain numbers and simple names usually work best.
3. A **`$`** in amounts can be unreliable in some setups; if extraction fails, try **`100`** or **`100 dollars`** without the symbol.

**After changing flow YAML** (including `description` on `collect:` steps), run **`rasa train`** from `level5/` again so the updated guidance is loaded.

**Digits after another flow:** If you just finished **check balance** (which uses the **`account`** slot) and then start **transfer**, a short reply like **`50`** can be mis-attributed to **`account`** instead of **`amount`** because both are free-text slots filled by the LLM. The Level 5 **`domain/basics.yml`** ties each slot’s **`from_llm`** mapping to the correct **`active_flow`** so digits go to **`amount`** during **`transfer_money`** / **`transfer_money_tools`**, and to **`account`** only during **`check_balance`**. Retrain after domain changes.

**“Unable to understand” when replying to a collect step (e.g. amount):** In debug logs, look for **`skip_command_slot_not_in_domain`** and a **`SetSlotCommand`** whose **`name`** is not in your domain (for example **`transfer_money_amount`**). The stock command prompt’s example used **`set slot transfer_money_recipient`**-style names, which are **not** valid domain slots (`amount`, `recipient`, `account_from`, `account`). **Lab 2.0** fixes this: copy **`command_prompt_v3_slot_names.jinja2`** from **`level5/resources/`** into **`level5/data/prompts/`**, then set **`prompt_template: data/prompts/command_prompt_v3_slot_names.jinja2`** on **`SearchReadyLLMCommandGenerator`** in **`level5/config.yml`**. Retrain after changing the prompt.

---

### Logging: Inspector does not write logs by default

**`rasa inspect`** only prints to the terminal unless you pass logging flags. From **`level5/`**, for example:

```bash
rasa inspect --debug --log-file logs/inspect.log
```

On Windows PowerShell, use the same path. Use **`--log-file`** (and optionally **`--debug`**) to capture **`command_processor`** lines such as **`slot_not_in_domain`** and the LLM’s **`set slot ...`** output.
