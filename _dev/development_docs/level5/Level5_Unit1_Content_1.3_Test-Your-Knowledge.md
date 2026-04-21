**Work in \`level5/\`:** This chapter assumes you are building the **`level5/`** agent.

Answer the following to check your understanding of Level 5 so far (Units 0-1).

---

**1. How do tools differ from actions?**

a) Tools are defined in the domain; actions are in endpoints.yml  
b) Actions are explicitly called in flow steps; tools are functions the LLM can choose to call at runtime  
c) Tools and actions are the same thing  
d) Only actions can read slots  

**2. Where do you register tools so Rasa can discover them?**

a) In the domain under `tools:`  
b) In `endpoints.yml` under a `tools:` section with `tools_module: "tools"`  
c) In the flow file  
d) In config.yml  

**3. What must be in your tools module for Rasa to discover the tool functions?**

a) Only the function definitions  
b) The functions and an `__all__` list that exports their names  
c) A class that inherits from Action  
d) A YAML configuration  

**4. When should you use tools rather than actions?**

a) Always; tools replace actions  
b) When you want the LLM to decide which function to call based on conversation context  
c) Only for check_balance and process_transfer  
d) When you have more than one flow  

**5. What does Level 5 add on top of Level 4?**

a) New slots and responses only  
b) A tools folder, tools registration in endpoints.yml, and flows/actions that use tool calling  
c) A new virtual environment inside level5  
d) Replacement of all Level 4 actions with tools  

---

## Answer Key

| Question | Answer | Brief explanation |
|----------|--------|-------------------|
| 1 | **b** | Actions are invoked by flow steps; tools are selected and invoked by the LLM based on context. |
| 2 | **b** | The `tools:` section in `endpoints.yml` with `tools_module: "tools"` registers the tools module. |
| 3 | **b** | Rasa discovers functions listed in `__all__` in the registered tools module. |
| 4 | **b** | Use tools when you want the LLM to dynamically choose which function to call. |
| 5 | **b** | Level 5 adds a tools module, registration in endpoints, and flows/actions that use tool calling; Level 4 content remains. |
