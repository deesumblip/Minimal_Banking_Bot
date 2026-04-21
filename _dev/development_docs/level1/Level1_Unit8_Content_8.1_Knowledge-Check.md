### 8.1 Knowledge Check

**Why check your knowledge**: These questions reinforce the main ideas: where responses live, what flows do, how the LLM uses descriptions, and what system patterns are for. If you can answer them, you're ready to move to Level 2 or to design your own agent from scratch.

**Q1: What is a Flow?**  
a) A predefined agent message  b) A guided conversational interaction with a clear sequence of steps  c) A Python function  d) A configuration file  
**Answer**: b) A guided conversational interaction with a clear sequence of steps. A Flow defines how a conversation progresses between a user and an agent, including the logic needed to handle a specific scenario.

**Q2: Where are Responses Defined?**  
a) data/basics/*.yml  b) domain/basics.yml  c) config.yml  d) actions/*.py  
**Answer**: b) domain/basics.yml.

**Q3: What Triggers pattern_session_start?**  
a) User says "hello"  b) A flow completes  c) A new conversation begins  d) User asks for help  
**Answer**: c) A new conversation begins.

**Q4: What Does rephrase: True Do?**  
a) Makes the agent remember  b) Allows the LLM to vary the wording of responses  c) Forces exact text  d) Enables custom code  
**Answer**: b) Allows the LLM to vary the wording of responses.

**Q5: Purpose of Flow Descriptions?**  
a) Comments for developers  b) The LLM uses them to match user messages to flows  c) Required for YAML  d) Displayed to users  
**Answer**: b) The LLM uses them to match user messages to flows.

---
