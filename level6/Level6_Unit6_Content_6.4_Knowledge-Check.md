Answer the following to check your understanding of Level 6.

---

**1. What does a flow step `call: banking_assistant` do?**

a) Runs the action_process_transfer_with_tools action  
b) Hands off to the banking_assistant sub-agent, which runs until it completes, then control returns to the main flow  
c) Sends a message to the user  
d) Registers the MCP server  

**2. Where is the sub-agent config file located?**

a) level6/domain/basics.yml  
b) level6/sub_agents/banking_assistant/config.yml  
c) level6/endpoints.yml  
d) level6/data/basics/ask_banking_assistant.yml  

**3. Why do we add mcp_servers to endpoints.yml in Level 6?**

a) To register custom actions  
b) So the main agent can call tools directly  
c) So the sub-agent can connect to the MCP server and use its tools  
d) To train the model  

**4. What is the relationship between the main agent and the sub-agent?**

a) The sub-agent replaces the main agent  
b) The main agent orchestrates; it runs a flow that calls the sub-agent; the sub-agent runs until done, then control returns  
c) They share the same flows  
d) The sub-agent calls the main agent  

**5. When should you use a sub-agent instead of tools in the main agent?**

a) Always; sub-agents replace tools  
b) When you want to delegate a whole task to another agent that runs until it completes  
c) Only for check_balance  
d) When you have more than one flow  

---

## Answer Key

| Question | Answer | Brief explanation |
|----------|--------|-------------------|
| 1 | **b** | `call: banking_assistant` invokes the sub-agent; it runs until completion, then the main flow continues. |
| 2 | **b** | Sub-agent config lives in sub_agents/<name>/config.yml. |
| 3 | **c** | The sub-agent uses MCP tools; the MCP server must be registered in endpoints.yml. |
| 4 | **b** | Main agent runs a flow; the flow has a step that calls the sub-agent; sub-agent runs until done, then control returns. |
| 5 | **b** | Use sub-agents to delegate a whole task; use tools in the main agent for dynamic tool calls in one context. |
