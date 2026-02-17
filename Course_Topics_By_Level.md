# Course Topics by Level

**Purpose:** A single reference for the topics covered in each level of the Minimal Banking Bot course. Each level builds on the previous one.

---

## 📊 Quick Reference: Course Progression

| Level | Core Concept | Key Capability Added | Status |
|-------|--------------|---------------------|--------|
| **1** | **Responses** | Predefined messages, simple flows, project structure | ✅ Active |
| **2** | **Actions** | Custom Python code, action class, domain registration | ✅ Active |
| **3** | **Slots** | Conversation memory, collect steps, ask responses | ✅ Active |
| **4** | **Multiple Slots** | Multi-slot collection per flow, complex conversations | ✅ Active |
| **5** | **Tool Calling** | LLM-driven tool selection, dynamic function calls | ✅ Active |
| **6** | **Sub-Agents** | Orchestration, `call` step, ReAct/MCP, A2A | 🚧 Planned |

---

## 🎯 Executive Summary

**Course Structure:** 6 progressive levels teaching Rasa Pro capabilities from basic responses to advanced orchestration.

**Teaching Approach:** Each level introduces one core concept, builds on previous levels, and adds concrete artifacts (domain files, flows, actions, tools).

**Progression:** Simple → Complex
- **Levels 1–2:** Static responses and explicit actions
- **Levels 3–4:** Memory (slots) and multi-step conversations
- **Levels 5–6:** Dynamic LLM-driven behavior (tools, sub-agents)

**Key Technical Concepts Covered:**
- Domain definition (responses, actions, slots)
- Flow-based conversation design
- Custom Python actions
- Slot collection and validation
- LLM tool calling
- Agent orchestration (planned)

---

## 📚 Detailed Level Breakdown

### Level 1: Just Responses

**Goal:** Build the simplest possible bot that only uses predefined responses (no memory, no custom code).

**Core Concept:** Static, predefined responses triggered by flows.

#### Topics Covered

| Topic | What you learn |
|-------|----------------|
| **Domain – responses** | How to define bot responses in `domain/basics.yml` under the `responses:` section. Predefined messages only; no slots or actions. |
| **Flows** | How to create simple flows in `data/basics/*.yml` that call `utter_*` responses. Flows have `name`, `description`, and `steps`. |
| **System patterns** | Basic patterns (e.g. `pattern_session_start`, `pattern_completed`) and where they live (`data/system/patterns/patterns.yml`). |
| **Project structure** | Where domain, flows, config, credentials, and endpoints live. |
| **Training and running** | Virtual environment, Rasa Pro install, `rasa train`, and Rasa Inspector for testing. |

#### Key Artifacts

- **Domain:** `responses:` only (`utter_greet`, `utter_help`, `utter_contact`)
- **Flows:** `greet.yml`, `help.yml`, `contact.yml` (each uses one or more `utter_*`)
- **No:** slots, actions, or custom code

#### Prerequisites

- None (first level)

---

### Level 2: Simple Actions

**Goal:** Add custom Python code to the bot by creating and using actions.

**Core Concept:** Custom Python code executed by the bot (vs. predefined text responses).

#### Topics Covered

| Topic | What you learn |
|-------|----------------|
| **Actions vs. responses** | `utter_*` = predefined text; `action_*` = custom Python code the bot can run. When to use each. |
| **Action class structure** | Imports (`Action`, `Tracker`, `CollectingDispatcher`), `name()` method, `run()` method, and sending messages with `dispatcher.utter_message()`. |
| **Creating an action** | Where to put action files (`actions/`), file naming (`action_bank_hours.py`), and the required class structure. |
| **Registering actions** | Adding an `actions:` section in `domain/basics.yml` and listing action names. |
| **Using actions in flows** | Defining a flow whose step is `- action: action_bank_hours` (or another action). |
| **Training and testing with actions** | Same train/inspect workflow; common errors (action not found, import error, name mismatch). |

#### Key Artifacts

- **New:** `actions/` folder, `actions/__init__.py`, `actions/action_bank_hours.py`
- **Domain:** `actions:` section with `action_bank_hours`
- **Flows:** `hours.yml` that calls `action_bank_hours`
- **Unchanged:** All Level 1 responses and flows

#### Prerequisites

- Level 1 (responses, flows, project structure)

---

### Level 3: Slot Collection

**Goal:** Give the bot memory by collecting and using information from the user (slots).

**Core Concept:** Conversation memory that persists user-provided data across turns.

#### Topics Covered

| Topic | What you learn |
|-------|----------------|
| **Slots** | What slots are (conversation memory), where they are defined (`domain/basics.yml` under `slots:`), and how they store user-provided data. |
| **Collect steps** | Using `collect: slot_name` in a flow so the bot asks for that slot (e.g. account number) before continuing. |
| **Ask responses** | `utter_ask_*` responses used when a slot is empty (e.g. `utter_ask_account`). |
| **Reading slots in actions** | Using `tracker.get_slot("slot_name")` inside an action to use collected information. |
| **Placeholder handling** | Detecting when the LLM extracted a placeholder instead of a real value and re-prompting the user. |

#### Key Artifacts

- **Domain:** `slots:` (e.g. `account`), `utter_ask_account`
- **New action:** `action_check_balance_simple` (reads `account` slot)
- **New flow:** `check_balance.yml` with `collect: account` then action
- **Unchanged:** All Level 1–2 responses, flows, and actions

#### Prerequisites

- Level 1 (responses, flows)
- Level 2 (actions, domain registration, flows that use actions)

---

### Level 4: Multiple Slots

**Goal:** Collect multiple pieces of information in one flow before performing an action.

**Core Concept:** Multi-step slot collection within a single flow for complex use cases.

#### Topics Covered

| Topic | What you learn |
|-------|----------------|
| **Multiple slots** | Defining several slots in the domain (e.g. `amount`, `recipient`, `account_from`) for one use case (e.g. transfer). |
| **Multiple collect steps** | Ordering several `collect:` steps in a single flow so the bot gathers amount, recipient, and source account in sequence. |
| **Multiple ask responses** | `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from` (or custom ask actions). |
| **Actions that use multiple slots** | Reading and validating several slots in one action (e.g. `action_process_transfer` using `amount`, `recipient`, `account_from`). |
| **Complex multi-step conversations** | Flows that don't proceed until all required slots are filled; validation and re-prompting. |

#### Key Artifacts

- **Domain:** Additional slots (`amount`, `recipient`, `account_from`) and ask responses
- **New action:** `action_process_transfer` (reads and uses multiple slots)
- **New flow:** `transfer_money.yml` with multiple `collect:` steps then action
- **Unchanged:** All Level 1–3 content

#### Prerequisites

- Level 1–3 (responses, flows, actions, single-slot collection)

---

### Level 5: Tool Calling

**Goal:** Let the LLM dynamically choose which functions to call based on conversation context.

**Core Concept:** LLM-driven function selection at runtime (vs. explicit action calls in flows).

#### Topics Covered

| Topic | What you learn |
|-------|----------------|
| **Tools vs. actions** | Tools = functions the LLM selects at runtime; actions = explicitly called in flows. When to use each. |
| **Creating tool functions** | Python functions in `tools/` (e.g. `banking_tools.py`) with docstrings, typing, and return dicts; `__all__` for discovery. |
| **Registering tools** | `endpoints.yml`: `tools:` section and `tools_module: "tools"`. |
| **Using tools in conversations** | Flows that collect slots and then run an action in a context where the LLM can call tools (e.g. `action_process_transfer_with_tools`). |
| **Dynamic tool selection** | The main agent's LLM decides which tools to call and when; no explicit tool steps in the flow. |
| **Training and testing with tools** | Same train/inspect workflow; verifying tool-calling behaviour. |

#### Key Artifacts

- **New:** `tools/` folder, `tools/banking_tools.py` (e.g. `check_balance`, `process_transfer`, `get_account_info`)
- **endpoints.yml:** `tools:` and `tools_module: "tools"`
- **New action:** `action_process_transfer_with_tools`
- **New flow:** `transfer_money_tools.yml` (collect + action that uses tools)
- **Unchanged:** All Level 1–4 responses, flows, actions, and slots

#### Prerequisites

- Level 1–4 (responses, flows, actions, single and multiple slot collection)

---

### Level 6: Orchestration and Sub-Agents (Planned)

**Goal (proposed):** Delegate whole tasks to a sub-agent that runs until it completes, then return control to the main flow.

**Core Concept:** Multi-agent orchestration with autonomous sub-agents handling complete tasks.

#### Topics That Would Be Covered

| Topic | What you would learn |
|-------|------------------------|
| **Orchestration** | Main agent as orchestrator; delegating a task to another "agent" that runs until done. |
| **Autonomous steps** | Flow step `- call: agent_name` (and optional `exit_if`); flow paused until sub-agent completes. |
| **Sub-agent types** | ReAct (built-in, MCP + optional Python tools) vs External (A2A protocol). |
| **Sub-agent layout** | `sub_agents/<name>/config.yml` (name, protocol, description, configuration). |
| **MCP (ReAct)** | Model Context Protocol; why ReAct requires at least one MCP server; configuring MCP in `endpoints.yml` and in the sub-agent. |
| **ReAct behaviour** | General-purpose (open-ended, `task_completed`) vs task-specific (slot-filling, `exit_if`, `set_slot_<name>` tools). |
| **Context and handback** | What the orchestrator passes in; what the sub-agent can return (slots, messages); state integration. |
| **When to use sub-agents** | Delegating a whole task vs using tools in the main agent. |

#### Prerequisites (proposed)

- Level 1–5 (especially tools, flows, slots)
- Rasa 3.14+
- MCP concept and at least one MCP server

---

*This guide summarizes topics for the Minimal Banking Bot course. Content may be updated as levels are revised.*
