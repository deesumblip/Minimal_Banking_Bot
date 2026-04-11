**Why sub-agents:** In Level 5, **tools** and **`transfer_money_tools`** let the **main** agent call Python functions in a controlled flow. That still fits **one** assistant context. **Sub-agents** add **orchestration**: the main agent can run a flow step that **hands off** a whole task to another agent (its own LLM and tools, e.g. via MCP) until that agent finishes, then **control returns** to the main flow.

**Level 6 starting point:** This chapter builds on your **Level 5 banking agent** (SearchReady, **`prompt_template`**, **`tools/`**, **`transfer_money_tools`**, **`endpoints.yml`** with **`tools:`**, and everything you trained under **`level5/`**). You are **not** starting from scratch. The course uses a **separate project folder** for Level 6: **`level6/`** (same repo; it does **not** replace **`level5/`**).

Activate the **virtual environment at project root**, then run all Rasa and MCP commands from **`level6/`**:

```bash
cd level6
```

**Naming:** *Level 6* is the chapter skill name; **`level6/`** is the project folder. The **lab order** is under **Unit 0.2 What Level 6 Adds** below.

---

## Where Level 6 happens

Do all Level 6 work under **`level6/`**. Keep **`level5/`** as your reference for “what Level 5 completion looks like”; **`level6/`** extends that design with sub-agents, MCP registration for the specialist, and a new flow that **`call:`**s the sub-agent.

---

## What you have at Level 5 completion

### Domain (`level5/domain/basics.yml`)

- Responses: `utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`, and utterances for slots (`utter_ask_*`) as in Level 5.
- Slots: `account`, `amount`, `recipient`, `account_from` (and any conditions your chapter used for **`transfer_money`** / **`transfer_money_tools`**).
- Actions: including **`action_process_transfer`**, **`action_process_transfer_with_tools`**, **`action_check_balance_simple`**, **`action_bank_hours`**, etc.

### Flows (`level5/data/basics/`)

- At minimum: `greet`, `help`, `contact`, `goodbye`, `hours`, `check_balance`, `transfer_money`, **`transfer_money_tools`** (as completed in Level 5).

### Tools (`level5/tools/`)

- **`banking_tools.py`** (or equivalent) with **`check_balance`**, **`process_transfer`**, **`get_account_info`** registered via **`endpoints.yml`** **`tools:`**.

### Config (Level 5 **done**)

- **`level5/config.yml`**: SearchReady + **`prompt_template`** pointing at your command prompt under **`data/prompts/`** (copied from **`resources/`** in Lab 2.0).
- **`level5/endpoints.yml`**: **`action_endpoint`**, **`nlg`**, **`model_groups`**, **`tools:`** — **no** **`mcp_servers`** yet (that is Level 6).

---

## What you add in Level 6

In order, you will:

| Order | Lab | What you add (under **`level6/`**) |
|------|-----|-----------------------------------|
| 1 | **Lab 2.1** | **`sub_agents/banking_assistant/config.yml`** — sub-agent name, protocol, description, LLM **`model_group`**, MCP server name, and (in this course) **`configuration.module`** for the tutorial-compatible agent. |
| 2 | **Lab 3.1** | Top-level **`mcp_servers:`** in **`endpoints.yml`** (name, url, type) so the sub-agent can reach the MCP process. |
| 3 | **Lab 4.1** | **`data/basics/ask_banking_assistant.yml`** — a flow whose steps include **`call: banking_assistant`**. |
| 4 | **Lab 5.1** | **`rasa train`** from **`level6/`** so the package includes the new flow and sub-agent. |
| 5 | **Lab 5.2** | Completion check (graded) that the files above (and optionally a trained model) are present. |

**Scaffolding (same idea as Levels 4–5):** For **Labs 2.1, 3.1, and 4.1**, the guide provides **Fill in the blanks** exercises that produce complete YAML snippets. **After you pass** each fill-in, **copy or merge** that YAML into the path in the table above, then run the **Code Test** (**Check It!**) for that lab.

**Heads-up (course deployment):** **`level6/endpoints.yml`** uses the **Rasa-hosted tutorial LLM** (**`provider: rasa`**, **`api_base`** for the tutorial host) and **only** **`RASA_LICENSE`** — no separate vendor API key. The sub-agent therefore uses a **provided** Python module (**`BankingAssistantLiteAgent`**) that works with that host; in Lab 2.1 you set **`configuration.module`** to that import path. Your **`main`** agent still uses the same **`model_group`** id (e.g. **`openai-gpt-5-1`**) as in the template.

---

## How Level 6 extends Level 5

Level 5 **does not** define sub-agents or MCP for a specialist. Level 6 **adds**:

1. A **sub-agent** definition under **`sub_agents/<name>/config.yml`**.
2. **`mcp_servers`** in the **main** project’s **`endpoints.yml`** so the sub-agent can use MCP tools.
3. A **flow** with **`call: banking_assistant`** so the main assistant can delegate.

You **train** the **Level 6** assistant from **`level6/`** once those pieces exist. To **run** the full stack locally or in Codio, you start the **MCP server**, the **action server**, and **Rasa** (often **`rasa inspect`**), then use **Inspector** — see **Unit 5**.
