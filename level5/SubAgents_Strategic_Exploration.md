# Sub-Agents: Strategic Exploration for Level 5

**Purpose:** Assess whether Rasa’s official **sub-agents** (ReAct and External/A2A) could be integrated into the Level 5 bot, and how, without making any implementation changes yet.

---

## 1. What the Official Rasa Docs Say About Sub-Agents

### 1.1 Two Types (Beta, Rasa 3.14+)

| Type | Protocol | Description |
|------|----------|-------------|
| **ReAct Sub Agent** | RASA | Built-in autonomous agent that uses **MCP tools** and/or **custom Python tools** in a ReAct loop. Can be general-purpose (open-ended) or task-specific (slot-filling with `exit_if`). |
| **External Sub Agent** | A2A | External agent (different stack/team) connected via Agent-to-Agent protocol. Rasa orchestrates; context and handoff are managed via A2A. |

### 1.2 How They Are Invoked

- Both are invoked from a **flow** using an **autonomous step**:
  ```yaml
  - call: agent_name
  ```
- For **task-specific ReAct** agents, you can add **exit conditions**:
  ```yaml
  - call: booking_agent
    exit_if:
      - slots.appointment_time is not null
  ```
- Sub-agents **take control** of the conversation until they signal completion (or exit conditions are met), then control returns to the main flow.

### 1.3 ReAct Sub-Agent Details (Relevant to Level 5)

- **Configuration:** Each sub-agent lives under `sub_agents/<agent_name>/` with its own `config.yml`.
- **Connections:** The `connections` section is **mandatory**: at least one **MCP server** must be configured. Custom Python tools can be added *in addition* via `get_custom_tool_definitions()` in a custom module.
- **General-purpose:** Uses a built-in `task_completed` tool to signal “I’m done”; no slot-based exit.
- **Task-specific:** Gets automatic `set_slot_<slot_name>` tools for each slot in `exit_if`; completes when those conditions are satisfied.
- **Context:** Sub-agents receive user message, conversation history, slots, and events; they can update slots and send messages.

### 1.4 External (A2A) Sub-Agent Details

- **Configuration:** `sub_agents/<name>/config.yml` with `protocol: A2A` and an **agent card** (local file or URL). Optional auth (API key, OAuth, token).
- **Use case:** Integrating agents built by other teams or on other tech stacks. Not for “extending our same bot with another process in the same repo” in the simple sense.

---

## 2. What Level 5 Does Today

- **Single agent** with **tool calling**:
  - `endpoints.yml`: `tools_module: "tools"` → `tools/banking_tools.py` (e.g. `check_balance`, `process_transfer`, `get_account_info`).
  - The **main agent’s LLM** decides when to call these tools during the conversation.
- **Flow pattern:** e.g. `transfer_money_tools`: `collect` steps (amount, recipient, account_from) then `action: action_process_transfer_with_tools`. No handoff to another “agent.”
- **Concept taught:** “LLM dynamically selects and calls functions (tools) based on context.”

So: Level 5 = **one agent + tools**. Sub-agents = **orchestrator + one or more child agents** (each with its own ReAct loop or external A2A service).

---

## 3. Conceptual Fit: Sub-Agents vs Level 5

| Aspect | Level 5 (current) | Sub-agents |
|--------|-------------------|------------|
| **Architecture** | One agent, one LLM, tools in same process | Orchestrator + sub-agents (each can have own LLM, tools, MCP) |
| **Who calls tools** | Main agent’s LLM | Sub-agent’s ReAct loop (or external A2A agent) |
| **Invocation** | Tools called during normal flow/action | Flow step `- call: agent_name` hands off until sub-agent completes |
| **Completion** | After action/tool use, flow continues | Sub-agent runs until it signals done (`task_completed` or `exit_if`) |
| **Use case** | “LLM picks which tools to call in this flow” | “Delegate this whole task to another agent (exploratory or slot-filling)” |

So sub-agents are a **different pattern** (delegation/orchestration), not a drop-in replacement for Level 5’s tool calling.

---

## 4. Could Sub-Agents Be “Easily” Integrated into Level 5?

### 4.1 ReAct Sub-Agent

- **Conceptually:** Yes. You could add a “banking assistant” ReAct sub-agent that has access to tools (e.g. balance, transfer) and is invoked with `- call: banking_assistant` (and optionally `exit_if` for task-specific behaviour).
- **Practically:**
  - ReAct sub-agents **require** at least one **MCP server** in `connections.mcp_servers`. Level 5 currently has **no MCP** (only `tools_module`).
  - So you’d need to either:
    - Expose the existing banking tools via an **MCP server** and point the ReAct agent at it, or
    - Add a minimal MCP server that wraps the same logic, and keep custom Python tools only as an *extra* on top of that.
  - You also need: `sub_agents/<name>/config.yml`, optional prompt template, optional custom module (e.g. for `process_input` / `process_output` or custom tools).
- **Verdict:** **Not “easy”** in the sense of “add one file and one step.” It requires new concepts (orchestration, `call` step, sub-agent config, MCP or MCP+Python tools) and new infrastructure (MCP server or integration). Better treated as a **separate level or advanced module** (e.g. Level 6: “Orchestration and sub-agents”) rather than a small change inside Level 5.

### 4.2 External (A2A) Sub-Agent

- **Fit for “extend Level 5 bot”:** Low. A2A is for **external** agents (different process/team/stack). You could use Level 5 as the **orchestrator** and call an external “banking service” agent via A2A, but that’s an integration/architecture topic, not a simple extension of the current Level 5 codebase.
- **Verdict:** Not a natural “integrate into Level 5” feature; more of a “Level 5 bot as orchestrator of external systems” scenario.

---

## 5. Strategic Options

### Option A: Leave Level 5 As-Is (Recommended for now)

- Level 5 already teaches **dynamic tool selection** by the LLM without orchestration or MCP.
- No curriculum or code change; no dependency on 3.14 beta or MCP.

### Option B: Add a Future Level (e.g. Level 6) on Sub-Agents

- **Topic:** “Orchestration and sub-agents” (ReAct first; A2A as optional/advanced).
- **Scope:** One ReAct sub-agent (e.g. “transfer assistant”) with:
  - `sub_agents/transfer_assistant/config.yml`
  - At least one MCP server (e.g. a small server exposing `check_balance` / `process_transfer` or a generic tool server), plus optional custom Python tools
  - A flow that uses `- call: transfer_assistant` (and optionally `exit_if` for task-specific behaviour)
- **Prerequisites:** Rasa 3.14+, MCP server setup, understanding of `call` step and exit conditions.
- **Benefit:** Clear progression: Level 5 = tools in one agent; Level 6 = delegating a task to another agent.

### Option C: Minimal “Sub-agent flavour” Inside Level 5 (Not recommended)

- Try to squeeze a ReAct sub-agent into Level 5 without a full “Level 6” story. Con: Level 5 would mix two different paradigms (tool calling vs orchestration) and require MCP and 3.14 beta, which complicates the course and support.

---

## 6. Level 5 vs Level 6: Concept Comparison

### 6.1 Concepts Covered in Level 5 (Current)

| Module | Concept | What the student learns |
|--------|---------|--------------------------|
| 0 | Recap Level 4 | Level 4 = multiple slots, transfer flow, action_process_transfer; Level 5 builds on it. |
| 1 | Introduction to Tools | Tools = functions the LLM can call dynamically; tools vs actions (explicit vs dynamic). |
| 2 | Tools vs. Actions | When to use tools (flexible, LLM-driven) vs actions (predictable, flow-driven). |
| 3 | Creating Tool Functions | Python functions in `tools/`, docstrings, typing, return dicts; `__all__` for discovery. |
| 4 | Registering Tools | `endpoints.yml` → `tools:` and `tools_module: "tools"`. |
| 5 | Using Tools in Conversations | Flows that use tools: collect slots + action that runs in a context where the LLM can call tools. |
| 6 | Training and Testing | Same as earlier levels; train, inspect, test tool-calling flows. |
| 7–8 | Putting It Together / Assessment | Full picture: one agent, one LLM, tools in the same process; when to use tools vs actions. |

**Level 5 mental model:** One agent. One conversation. The LLM decides *which* tools to call and *when*, but everything runs in the same agent and flow.

---

### 6.2 What Level 6 Would Need to Cover (Sub-Agents)

| Topic | Concept | What the student would need to learn |
|-------|---------|-------------------------------------|
| **Orchestration** | Main agent as orchestrator | The Rasa bot can *delegate* a whole task to another “agent” that runs until it’s done, then control returns. |
| **Autonomous steps** | `call` step | Flow step `- call: agent_name` (and optional `exit_if`) invokes a sub-agent; flow is paused until the sub-agent completes. |
| **Sub-agent types** | ReAct vs External (A2A) | ReAct = built-in agent with tools (MCP + optional Python). A2A = external service; different stack/team. |
| **Sub-agent layout** | `sub_agents/` | Each sub-agent has its own directory and `config.yml` (name, protocol, description, configuration). |
| **MCP (ReAct)** | Model Context Protocol | ReAct sub-agents *require* at least one MCP server. What MCP is, why it’s used, how to configure it in `endpoints.yml` and in the sub-agent’s `connections.mcp_servers`. |
| **ReAct behaviour** | General-purpose vs task-specific | General-purpose: open-ended, completes by calling `task_completed`. Task-specific: fills slots, completes when `exit_if` conditions are met; gets `set_slot_<name>` tools. |
| **Context and handback** | What the sub-agent sees and returns | Orchestrator passes context (message, history, slots); sub-agent can update slots and send messages; state is integrated when it finishes. |
| **When to use sub-agents** | vs tools in main agent | Sub-agents for “hand off this whole task”; tools for “main agent chooses which operations to run in this flow.” |
| **(Optional) A2A** | External sub-agents | Agent card, auth, when to use external vs ReAct; can be brief or advanced. |

**Level 6 mental model:** Orchestrator + sub-agents. The main flow *calls* an agent that runs its own loop (ReAct or A2A) and then returns control.

---

### 6.3 Side-by-Side Comparison

| Dimension | Level 5 (current) | Level 6 (sub-agents) |
|-----------|-------------------|----------------------|
| **Main idea** | LLM dynamically selects and calls tools in the same agent. | Main agent delegates a task to another agent that runs until done. |
| **Architecture** | Single agent; tools in `tools/`; `endpoints.yml` `tools_module`. | Orchestrator + sub-agents; `sub_agents/<name>/config.yml`; ReAct needs MCP. |
| **Flow step** | `action: action_*` (and optionally collect before); tools are used *inside* the agent. | `call: agent_name` (autonomous step); sub-agent runs independently. |
| **Who calls tools** | Main agent’s LLM. | Sub-agent’s ReAct loop (or external A2A agent). |
| **Completion** | After the action (and any tool calls) the flow continues to the next step. | Sub-agent signals completion (`task_completed` or `exit_if`); then flow continues. |
| **Config surface** | `endpoints.yml` (tools), `tools/*.py`. | `sub_agents/<name>/config.yml`, MCP in `endpoints.yml`, optional prompt template and custom module. |
| **New infra** | None beyond Rasa + tools module. | MCP server(s) required for ReAct. |
| **Prerequisites** | Levels 1–4 (responses, actions, slots, multi-slot flows). | Level 5 (tools, flows, slots); Rasa 3.14+; MCP concept and setup. |

---

### 6.4 Is It Strategically Reasonable to Grow from Level 5 to Level 6?

**Yes, with clear boundaries.** Reasons:

1. **Natural progression**  
   Level 5 = “one agent, dynamic tool use.” Level 6 = “same bot, but some tasks are delegated to another agent.” The step from “LLM chooses tools” to “LLM (orchestrator) chooses when to hand off to an agent that uses tools” is a single, understandable extension.

2. **Conceptual clarity**  
   Keeping sub-agents in a separate level avoids overloading Level 5. Level 5 stays about tools and one-agent behaviour; Level 6 is explicitly about orchestration and the `call` step.

3. **Reuse of existing skills**  
   Students already have: flows, slots, actions, and tools (Level 5). Level 6 reuses flows and slots and adds: `call`, sub-agent config, MCP, and completion behaviour. No need to re-teach fundamentals.

4. **Manageable new load**  
   The main new pieces are: (a) orchestration and `call`, (b) `sub_agents/` and config, (c) MCP (what it is + one server), (d) ReAct general vs task-specific and exit behaviour. That’s one level’s worth of content, not two.

5. **Beta and dependencies**  
   Sub-agents are beta and require 3.14+ and MCP. Putting that in Level 6 makes the dependency explicit and keeps Level 5 stable and production-oriented.

6. **Optional depth**  
   Level 6 can focus on ReAct only; A2A can be a short “when to use external agents” note or an optional advanced section, so scope stays controllable.

**Risks to watch:**  
- MCP and ReAct are newer; docs and tooling may change.  
- Lab environment must support Rasa 3.14+ and running (or mocking) an MCP server.

**Conclusion:** Growing from Level 5 to Level 6 to cover sub-agents is strategically reasonable: one clear step, separated concepts, builds on Level 5, and keeps Level 5 unchanged.

---

## 7. Summary Table

| Question | Answer |
|----------|--------|
| Can sub-agents be **easily** integrated into the current Level 5 bot? | **No.** They need a different structure (sub_agents/, MCP or MCP+custom tools, `call` step) and teach a different concept (orchestration). |
| Is the **concept** compatible with Level 5? | **Partially.** ReAct sub-agents are a natural “next step” after “one agent + tools,” but they are a step up in complexity. |
| Best way to use sub-agents with this course? | Introduce them in a **separate level** (e.g. Level 6) focused on orchestration and ReAct (and optionally A2A), with MCP and 3.14+ clearly stated as requirements. |
| Should we change Level 5 now? | **No.** Keep Level 5 as single-agent tool calling; plan sub-agents as a later, dedicated level or optional advanced module. |
| Is growing Level 5 → Level 6 for sub-agents **strategically reasonable**? | **Yes.** Clear progression, separated concepts, builds on Level 5; keep Level 5 unchanged and treat beta/MCP as Level 6 prerequisites. |

---

## 8. References (Official Rasa Docs)

- [Sub-agents overview](https://rasa.com/docs/reference/config/agents/overview-agents/)
- [ReAct Sub Agent](https://rasa.com/docs/reference/config/agents/react-sub-agents/)
- [External Sub Agent (A2A)](https://rasa.com/docs/reference/config/agents/external-sub-agents/)
- [Integrating external agents via A2A](https://rasa.com/docs/pro/build/integrating-external-agents)
- [Flow steps – Autonomous steps / Call](https://rasa.com/docs/reference/primitives/flow-steps/) (prescriptive vs autonomous, `call` step)

---

*Document created for strategic discussion only. No code or Level 5 content has been changed.*
