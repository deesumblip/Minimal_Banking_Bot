Level 6 adds **orchestration with sub-agents**:

1. **Sub-agent.** A separate agent (e.g. `banking_assistant`) with its own config under **`sub_agents/<name>/config.yml`**, description, LLM **`model_group`**, MCP server name(s), and (in this course) **`configuration.module`** pointing at a **tutorial-compatible** agent class so the hosted Rasa LLM can run without a separate vendor API key.
2. **Flow that calls the sub-agent.** A flow (e.g. `ask_banking_assistant`) with a step **`call: banking_assistant`**. When the user asks to use the banking assistant, the main agent runs this flow; the flow delegates to the sub-agent, which runs until done, then control returns to the main agent (e.g. **`utter_help`**).
3. **MCP server and registration.** The sub-agent uses tools via MCP. You register the MCP server in **`endpoints.yml`** (`mcp_servers:`) and reference the same **name** in the sub-agent config. You run the MCP process (e.g. **`python mcp_server/banking.py`**) on the **URL** you configured (including the **`/mcp`** path for Streamable HTTP in this repo).

**Order of work:** Sub-agent config (Lab 2.1) → MCP registration (Lab 3.1) → Flow that calls the sub-agent (Lab 4.1) → Train and test (Labs 5.1, 5.2).

---

## Delta checklist: end of Level 5 → end of Level 6

Use this as a **linear** checklist. Items above the line are Level 5; below the line is what you add in **`level6/`** for Level 6.

**Already true when you finish Level 5 (in `level5/`):**

- [ ] SearchReady + **`prompt_template`** and trained model under **`level5/`**
- [ ] **`tools/`** + **`endpoints.yml`** **`tools:`** + **`transfer_money_tools`** flow and actions

**Add for Level 6 (in `level6/`):** (each lab: **Fill in the blanks** in the guide → **copy/merge** into the file → **Code Test**)

- [ ] **Lab 2.1:** Pass **`fill-in-the-blanks-501060111`**, copy YAML to **`sub_agents/banking_assistant/config.yml`**, pass **`code-output-compare-501060001`**
- [ ] **Lab 3.1:** Pass **`fill-in-the-blanks-501060112`**, merge **`mcp_servers`** into **`endpoints.yml`**, pass **`code-output-compare-501060002`**
- [ ] **Lab 4.1:** Pass **`fill-in-the-blanks-501060110`**, save as **`data/basics/ask_banking_assistant.yml`**, pass **`code-output-compare-501060003`**
- [ ] **`rasa train`** from **`level6/`** (Lab 5.1)
- [ ] Pass Lab 5.2 completion check; optionally run MCP + **`rasa run actions`** + **`rasa inspect`** and trigger the sub-agent flow (Unit 5)

---

## Files you do **not** duplicate from Level 5

You do **not** re-create the whole **`level5/`** tree inside **`level6/`**. The **`level6/`** starter repo includes the main agent (domain, flows, tools, config, **`banking_assistant_lite_agent.py`**, **`mcp_server/banking.py`**). You **author** the Lab 2.1–4.1 deliverables: **`sub_agents/banking_assistant/config.yml`**, **`mcp_servers`** in **`endpoints.yml`**, and **`data/basics/ask_banking_assistant.yml`**.
