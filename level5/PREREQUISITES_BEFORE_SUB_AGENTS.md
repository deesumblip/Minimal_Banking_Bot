# Strategic Prerequisites Before Sub-Agents (Level 6)

This document lists **all content and examples** students should cover before diving into **Level 6: Sub-agents** (orchestrating a ReAct sub-agent with its own tools, e.g. via MCP). Sub-agents build on a single main agent that already uses flows, actions, slots, and **tool calling**; the list below ensures that foundation is solid.

---

## 1. Learning Path Overview

| Level | Focus | Must complete before sub-agents |
|-------|--------|----------------------------------|
| **Level 1** | Just responses (domain, flows, patterns, training) | ✓ |
| **Level 2** | Custom actions (Python actions, dispatcher, tracker) | ✓ |
| **Level 3** | Slot collection (slots, collect steps, reading in actions) | ✓ |
| **Level 4** | Multiple slots (transfer flow, multiple collect steps) | ✓ |
| **Level 5** | Tool calling (tools folder, registration, flow + action with tools) | ✓ |

**Sub-agents (Level 6)** assume: one main agent that can run flows, call actions, use slots, and **invoke tools**; the main agent will then delegate whole tasks to a sub-agent that has its own tools (e.g. MCP).

---

## 1b. Minimal concepts (from Rasa documentation)

Based on the [Rasa sub-agents overview](https://rasa.com/docs/reference/config/agents/overview-agents/), [ReAct sub-agents](https://rasa.com/docs/reference/config/agents/react-sub-agents/), and [flow steps](https://rasa.com/docs/reference/primitives/flow-steps/) (Rasa 3.14+), learners should **minimally** be comfortable with these concepts before sub-agents:

| Concept | Why it's needed for sub-agents |
|--------|---------------------------------|
| **Flows** | Sub-agents are **only** invoked from inside a flow. Flows are the place where an "autonomous step" runs and delegates to a sub-agent. |
| **Flow steps** | Sub-agents are triggered by a specific step type: **autonomous steps** (vs prescriptive steps like `action`, `collect`). Learners need to know what a step is and that there are different types. |
| **Slots** | Rasa shares **slot values** (and event history, conversation history) with sub-agents as context. Task-specific ReAct sub-agents fill slots and use **exit conditions** on slots; they get built-in `set_slot_*` tools. So "conversation state" and slots are central. |
| **Actions** | Prescriptive steps use `action` (and `collect`). Understanding when the flow runs an action vs when it delegates to a sub-agent avoids confusion. |
| **Tools** | ReAct sub-agents use **MCP tools** and/or **custom Python tools** in a ReAct loop. Learners need the idea that "tools" are callable functions the LLM chooses at runtime (as in Level 5). |
| **MCP (Model Context Protocol)** | ReAct sub-agents get their tools from **MCP servers** (configured in `endpoints.yml` or sub-agent config). Learners need at least the idea that tools can be exposed via MCP. |
| **Orchestration** | The main agent runs a flow; when it hits an **autonomous step**, it invokes a sub-agent and passes context; the sub-agent runs until it signals completion (or exit conditions) or returns `INPUT_REQUIRED`. So "main agent orchestrates, sub-agent does one task" is the mental model. |
| **Config and project layout** | Sub-agents live in a `sub_agents/<name>/` directory with their own `config.yml`; MCP servers and LLM are configured there or in `endpoints.yml`. Familiarity with `config.yml` and `endpoints.yml` is needed. |

**In short:** Learners should be able to build a **single-agent** agent that uses **flows**, **prescriptive steps** (action, collect), **slots**, and **tools** (LLM-invoked). Sub-agents then add **autonomous steps** that delegate to a **sub-agent** with its **own tools** (e.g. via MCP) and **completion signalling** (task_completed or exit conditions on slots).

---

## 2. Level 1: Just Responses — Content & Examples

### Content to cover
- **Unit 0:** Prerequisites and setup; what you need before starting.
- **Unit 1:** What a conversational agent is; domain, intents, responses, flows.
- **Unit 2:** Domain structure (`domain/basics.yml`): intents, responses, session_config.
- **Unit 3:** Flows and patterns (flow YAML, steps, `utter_*`, patterns).
- **Unit 4:** Training data (`data/basics/`, NLU examples, response rules).
- **Unit 5:** Config and credentials (`config.yml`, `credentials.yml`, `endpoints.yml`).
- **Unit 6:** Training and running the agent; Rasa Inspector.
- **Unit 7–8:** Complete agent walkthrough; what you've learned; what's next.

### Examples / artifacts students must have seen or built
- **Domain:** `intents:`, `responses:`, at least one flow referenced in domain or patterns.
- **Flows:** At least one flow (e.g. greet, help, contact, hours, goodbye) with `utter_*` steps.
- **Data:** `data/basics/*.yml` (e.g. greet, help, contact) and system patterns.
- **Training:** Run `rasa train` from `level1` and run the agent (e.g. Inspector).
- **Labs (minimum):** Lab 0.1 (venv + Rasa install), Lab 6.1 (training); ideally Lab 7.2 (add response + flow).

### Concepts that carry forward to sub-agents
- How a **flow** is defined and executed.
- How **responses** and **steps** are ordered in a flow.
- Single source of truth: **domain**, **data**, **config**; train from one folder.

---

## 3. Level 2: Custom Actions — Content & Examples

### Content to cover
- **Unit 0:** Recap - What you built in Level 1; what Level 2 adds (actions).
- **Unit 1:** What an action is; actions vs responses; when to use actions.
- **Unit 2:** Action class structure (`name()`, `run()`); dispatcher, tracker, domain.
- **Unit 3:** Creating your first action (e.g. bank hours).
- **Unit 4:** Registering actions in `endpoints.yml` and using them in flows.
- **Unit 5:** Training and testing with actions.
- **Unit 6:** Complete agent walkthrough; what you've learned.

### Examples / artifacts students must have seen or built
- **Action class:** At least one custom action (e.g. `action_bank_hours.py`) with `name()` and `run()`.
- **Sending messages:** Use of `dispatcher.utter_message()` (or equivalent) inside `run()`.
- **Endpoints:** `endpoints.yml` with `action_endpoint` pointing to the actions module.
- **Flow:** A flow that includes an `action_*` step (e.g. after greet or in a help path).
- **Labs (minimum):** Lab 3.1 (create first action), Lab 4.1 (register and use in flow), Lab 5.1 (train), Lab 6.1 (integration).

### Concepts that carry forward to sub-agents
- **Actions** extend the agent with Python; they are **explicitly** referenced in flows.
- **Orchestration:** The flow decides which action to run; the action runs and returns control.

---

## 4. Level 3: Slot Collection — Content & Examples

### Content to cover
- **Unit 0:** Recap - What you built in Level 2; what Level 3 adds (slots = memory).
- **Unit 1:** What a slot is; how slots work; slot collection (ask when empty).
- **Unit 2:** Slot types (e.g. text); slot naming conventions.
- **Unit 3:** Defining slots in the domain (`slots:`, `utter_ask_<slot>`).
- **Unit 4:** Reading slots in actions (`tracker.get_slot("slot_name")`); placeholder handling.
- **Unit 5:** Collect steps in flows (`collect:` with `description:`); flow with collect + action.
- **Unit 6–8:** Training, testing, complete walkthrough; what you've learned.

### Examples / artifacts students must have seen or built
- **Domain:** `slots:` section with at least one slot (e.g. `account`); `utter_ask_account` (or equivalent).
- **Action:** An action that reads a slot (e.g. `action_check_balance_simple.py`) and uses `tracker.get_slot()`.
- **Flow:** A flow with a `collect` step for that slot and an `action_*` step that uses it (e.g. `check_balance.yml`).
- **Labs (minimum):** Lab 3.1 (domain slot), Lab 4.1 (explore action with slots), Lab 5.1 (flow with collect), Lab 6.1 (train/test).

### Concepts that carry forward to sub-agents
- **Slots** = conversation memory; **collect** = "ask if empty, then proceed."
- **Tracker** provides conversation state; sub-agents may receive context derived from slots.

---

## 5. Level 4: Multiple Slots — Content & Examples

### Content to cover
- **Unit 0:** Recap - What you built in Level 3; what Level 4 adds (transfer flow, multiple slots).
- **Unit 1:** Multiple slots in one flow; order of collection; slot naming with multiple slots.
- **Unit 2:** Adding slots and responses (e.g. amount, recipient, account_from); domain and utter_ask_*.
- **Unit 3:** Reading multiple slots in one action (`tracker.get_slot` for each).
- **Unit 4:** Flows with multiple collect steps; one flow that collects several slots then runs one action.
- **Unit 5:** Training Level 4; testing transfer; completion check.
- **Unit 6:** Complete agent walkthrough (all flows); what you've learned; what's next.

### Examples / artifacts students must have seen or built
- **Domain:** Multiple slots (e.g. `amount`, `recipient`, `account_from`); corresponding `utter_ask_*` responses.
- **Action:** One action that uses all slots (e.g. `action_process_transfer`) and returns a confirmation message.
- **Flow:** One flow (e.g. `transfer_money.yml`) with multiple `collect` steps in a defined order, then the action.
- **Labs (minimum):** Lab 2.1 (domain slots), Lab 3.1 (action with multiple slots), Lab 4.1 (transfer flow), Lab 5.1 (train), Lab 5.2 (completion check).

### Concepts that carry forward to sub-agents
- **Multi-step flows** with ordered collection; one action that consumes several pieces of context.
- **End state:** A working "transfer" path that collects data and runs one action — analogous to "one task" a sub-agent might perform.

---

## 6. Level 5: Tool Calling — Content & Examples (Critical for Sub-Agents)

### Content to cover
- **Unit 0:** Recap - What you built in Level 4; what Level 5 adds (tools, tools_module, transfer_money_tools flow).
- **Unit 1:** Tools vs actions (tools = LLM-selected at runtime; actions = explicit in flow).
- **Unit 2:** Creating tool functions (`tools/` folder, `banking_tools.py`, `__all__`, docstrings, return dicts).
- **Unit 3:** Registering tools (`endpoints.yml` tools section, `tools_module`).
- **Unit 4:** Using tools in a flow (e.g. `transfer_money_tools.yml`, `action_process_transfer_with_tools`).
- **Unit 5:** Training Level 5; testing tool calling; completion check.
- **Unit 6:** Complete agent walkthrough; what you've learned; what's next (including Level 6 sub-agents).

### Examples / artifacts students must have seen or built
- **Tools module:** `tools/banking_tools.py` (or equivalent) with at least one tool function; `__all__`; clear docstrings; return value as dict (e.g. for LLM).
- **Endpoints:** `endpoints.yml` with `tools:` and `tools_module` pointing to that module.
- **Flow:** A flow that uses an action which invokes tools (e.g. `transfer_money_tools` → `action_process_transfer_with_tools`).
- **Action:** An action that runs in a "tool-calling" flow and interacts with the LLM/tool layer (e.g. process transfer with tools).
- **Labs (minimum):** Lab 2.1 (tools folder + banking_tools), Lab 3.1 (register tools), Lab 4.1 (flow + action for tools), Lab 5.1 (train), Lab 5.2 (testing/completion).

### Concepts that carry forward to sub-agents
- **Tools** = functions the **LLM** selects at runtime (vs actions chosen by the flow).
- **Registration** of tools in `endpoints.yml`; the main agent's LLM can call these tools.
- **Orchestration:** One flow + one "tool-aware" action that lets the LLM pick and run tools — sub-agents extend this by delegating a **whole task** to another agent with its **own** tools (e.g. MCP).

---

## 7. Checklist: Ready for Sub-Agents?

Use this as a strategic checklist before starting Level 6.

### Environment & project
- [ ] Single project with level folders (`level1` … `level5`); one venv at project root.
- [ ] Can activate venv, `cd level5`, run `rasa train` and run the agent (e.g. Inspector).

### Level 1–4 (foundation)
- [ ] **Flows:** Understand flow YAML, steps, `utter_*`, and at least one flow that runs an `action_*`.
- [ ] **Actions:** Written at least one custom action; know `name()`, `run()`, `dispatcher`, `tracker`.
- [ ] **Slots:** Defined slots in domain; used `collect` in a flow; read slots in an action with `tracker.get_slot()`.
- [ ] **Multiple slots:** Built one flow that collects several slots in order and runs one action (e.g. transfer).

### Level 5 (tool calling — essential)
- [ ] **Tool functions:** Created a `tools/` module with at least one callable tool (docstrings, `__all__`, return dict).
- [ ] **Registration:** Added `tools:` and `tools_module` in `endpoints.yml`.
- [ ] **Flow + action with tools:** Built a flow (e.g. `transfer_money_tools`) and an action that uses the tool-calling mechanism so the LLM can select and invoke tools.
- [ ] **Trained and tested:** Trained from `level5` and verified tool calling in conversation (e.g. transfer with LLM-selected tools).

### Concepts (no gaps)
- [ ] Difference between **actions** (flow-driven) and **tools** (LLM-driven).
- [ ] How **slots** and **tracker** provide context; how **flows** orchestrate steps.
- [ ] That the **main agent** in Level 5 already "orchestrates" by running a flow and an action that uses tools — Level 6 will add a **sub-agent** that does a whole task with its own tools (e.g. ReAct + MCP).

---

## 8. Optional but helpful before sub-agents

- **NLU:** Refining intents and training data so the agent reliably triggers the right flow (e.g. `transfer_money` vs `transfer_money_tools`).
- **Channels:** Running the agent on a channel and testing tool calling there.
- **More tools:** Adding extra tool functions (e.g. `close_account`, `list_transactions`) and exporting them in `__all__` — reinforces the "tool as callable" and registration pattern.

---

## 9. Where this lives in the repo

- **Level 5 content:** `level5/Level5_Unit*_Content_*.md`, `level5/Level5_Lab*_Content.md`.
- **Level 5 outline:** `level5/Level5_Course_Outline.md`.
- **Codio chapter (Level 5):** `.guides/content/Chapter-1-5---Tool-Calling-f9e0/`.
- **This prerequisite list:** `level5/PREREQUISITES_BEFORE_SUB_AGENTS.md` — can be linked from Level 5 "What's Next" or a future Level 6 intro.

If you are building Level 6 (sub-agents) content, you can reference this document as the **strategic list of content and examples** students must cover before diving into sub-agents.
