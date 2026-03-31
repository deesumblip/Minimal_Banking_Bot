# Level 6: Sub-Agents - Course Outline

## Course Overview

**Title**: Level 6: Sub-Agents  
**Description**: Adding orchestration with a sub-agent to your Level 5 banking agent  
**Prerequisites**: Level 1 through Level 5 must be completed  
**Learning Objective**: Students learn to define a sub-agent (config, MCP registration), add a flow that calls the sub-agent, and train and test the full agent. Labs are ordered: sub-agent config (Lab 2.1) → MCP registration (Lab 3.1) → flow (Lab 4.1) → train and test (Labs 5.1, 5.2).

---

## Course Structure (7 units: 0–6)

### Unit 0: Recap - What you built in Level 5
**Type**: Content Page | **Assessment**: None  
**Sections**: 0.1 Your Level 5 Banking Agent | 0.2 What Level 6 Adds  
**Key Concepts**: Recap Level 5 (domain, flows, actions, tools); Level 6 adds sub-agent, flow that calls it, MCP registration.

### Unit 1: Sub-Agents Concept
**Type**: Content Page | **Assessment**: None  
**Sections**: 1.1 What Are Sub-Agents | 1.2 When to Use Sub-Agents  
**Key Concepts**: Sub-agents = flow step `call: agent_name`; hand off, run until done, return; when to use vs tools in main agent.

### Unit 2: Sub-Agent Config
**Type**: Content + Lab | **Assessment**: Lab 2.1  
**Sections**: 2.1 Sub-Agent Layout and Config + Lab 2.1  
**Key Concepts**: sub_agents/banking_assistant/config.yml; name, protocol, description, LLM, MCP server reference.

### Unit 3: MCP and ReAct Config
**Type**: Content + Lab | **Assessment**: Lab 3.1  
**Sections**: 3.1 MCP and ReAct Config + Lab 3.1  
**Key Concepts**: endpoints.yml mcp_servers; register MCP server for sub-agent.

### Unit 4: Flow that Calls the Sub-Agent
**Type**: Content + Lab | **Assessment**: Lab 4.1  
**Sections**: 4.1 Flow that Calls the Sub-Agent + Lab 4.1  
**Key Concepts**: ask_banking_assistant flow; step `call: banking_assistant`.

### Unit 5: Training and Testing
**Type**: Content + Labs | **Assessment**: Lab 5.1, Lab 5.2  
**Sections**: 5.1 Training Level 6 | 5.2 Testing Sub-Agents + Labs 5.1, 5.2  
**Key Concepts**: Train from level6; run MCP server, actions, Rasa; test in Inspector.

### Unit 6: Summary and Next Steps
**Type**: Content Page | **Assessment**: None  
**Sections**: 6.1 Complete Agent Walkthrough | 6.2 What You've Learned | 6.3 What's Next | 6.4 Knowledge Check | 6.5 Limitations of Level 6 | 6.6 What's Next Beyond the Course | 6.7 Course Completion Checklist  
**Key Concepts**: Level 6 summary; knowledge check; limitations; beyond course; completion checklist.

---

## Assessment Summary

| Lab | Points | Type | Grader |
|-----|--------|------|--------|
| 2.1 | 10 | Code Output Compare | .guides/secure/level6_graders/lab_2.1_grader.py |
| 3.1 | 10 | Code Output Compare | lab_3.1_grader.py |
| 4.1 | 10 | Code Output Compare | lab_4.1_grader.py |
| 5.1 | 10 | Code Output Compare | lab_5.1_grader.py |
| 5.2 | 10 | Code Output Compare | lab_5.2_grader.py |

**Total**: 50 points. Task IDs: code-output-compare-501060001 through 501060005. Working Directory: `/home/codio/workspace`. Expected output: `PASS`.

---

## File Organization

- **Content and labs**: level6/LEVEL6_CONTENT_LABS_AND_ASSESSMENTS.md (unit list, lab list, task IDs, grader paths)  
- **Source content**: level6/Level6_Unit*_Content_*.md, level6/Level6_Lab*_Content.md  
- **Codio chapter**: Chapter-1-6---Sub-Agents-c7d8
