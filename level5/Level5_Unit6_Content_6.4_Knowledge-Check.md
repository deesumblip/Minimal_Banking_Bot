Answer the following to check your understanding of Level 5 (tool calling).

---

**1. How do tools differ from actions?**

a) Tools are in the domain; actions are in endpoints.yml  
b) Actions are explicitly called in flow steps; tools are functions the LLM can choose to call at runtime  
c) Tools and actions are the same thing  
d) Only tools can read slots  

**2. Where do you register tools so Rasa can discover them?**

a) In the domain under `tools:`  
b) In `endpoints.yml` under a `tools:` section with `tools_module: "tools"`  
c) In the flow file  
d) In config.yml  

**3. What must be in `tools/banking_tools.py` for Rasa to discover the tool functions?**

a) Only the function definitions  
b) The functions and an `__all__` list that exports their names  
c) A class that inherits from Action  
d) A YAML configuration  

**4. In Level 5, what does the transfer_money_tools flow do?**

a) Lists each tool (check_balance, process_transfer) as a separate step  
b) Collects amount, recipient, account_from, then runs the action `action_process_transfer_with_tools`; the LLM can call tools in that context  
c) Only runs tools, no action  
d) Replaces the Level 4 transfer_money flow  

**5. From where do you train the Level 5 agent?**

a) From project root only  
b) Activate the venv at project root, then `cd level5`, then `rasa train`  
c) From inside a new venv in the level5 folder  
d) You don't train; Level 5 uses the Level 4 model  

---

## Answer Key

| Question | Answer | Brief explanation |
|----------|--------|-------------------|
| 1 | **b** | Actions are invoked by flow steps; tools are selected and invoked by the LLM based on conversation context. |
| 2 | **b** | The `tools:` section in `endpoints.yml` with `tools_module: "tools"` registers the tools module. |
| 3 | **b** | Rasa discovers functions listed in `__all__` in the registered tools module. |
| 4 | **b** | The flow collects slots and runs one action; that action runs in a context where the LLM can call the registered tools. |
| 5 | **b** | Use the same venv at project root, then `cd level5` and run `rasa train`. |
