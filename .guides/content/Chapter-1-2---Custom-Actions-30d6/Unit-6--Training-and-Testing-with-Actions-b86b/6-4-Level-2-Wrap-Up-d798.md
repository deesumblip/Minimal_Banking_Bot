This last page of **Unit 6** finishes Level 2. It walks through a **full conversation** (Level 1 plus the example action and your Lab 3.1 action), maps **where your files live**, and suggests **practices** for testing and maintenance. After that, you will find a short **knowledge check** (use **Check It!** for each question), a recap of **core ideas and skills**, what Level 2 **still cannot** do, how **Level 3** builds on the **same** banking agent, and a **readiness** checklist before you leave this level.

#### A complete conversation

The trace below shows static responses, the course example action (`action_bank_hours` / `hours`), and the action you added in Lab 3.1 (`action_holiday_hours` / `holiday_hours`). Replay the same turns in Rasa Inspector to watch which flow and step run after each message—that is how domain entries, flow YAML, and Python under `actions/` show up in the running agent.

```text
[User opens chat - new session starts]

1. pattern_session_start triggers automatically (Level 1)
   ↓
   Flow: pattern_session_start
   Step: utter_greet
   ↓
Agent: "Hi! I'm a banking assistant. How can I help you today?"

[User types: "What are your hours?"]

2. LLM understands: "User wants to know bank hours"
   ↓
   FlowPolicy matches to: hours flow (Level 2)
   (Description: "Tell the user when the bank is open")
   ↓
   Flow: hours
   Step: action_bank_hours (Level 2 - custom Python code!)
   ↓
   Action executes Python code (checks current day via datetime)
   dispatcher.utter_message() sends message
   ↓
Agent: [Dynamic message, e.g., "Today is Saturday, we're open 10am-2pm." or full schedule on weekdays]

[User types: "What are your holiday hours?"]

3. LLM understands: "User wants holiday hours"
   ↓
   FlowPolicy matches to: holiday_hours flow (Level 2 - your flow)
   ↓
   Flow: holiday_hours
   Step: action_holiday_hours (Level 2 - the action you created in Lab 3.1!)
   ↓
   Action runs (checks if today is a holiday via datetime), sends message
   ↓
Agent: [Dynamic message, e.g. "We're closed today for Christmas." or the general holiday schedule]

[User types: "How can I contact you?"]

4. LLM understands: "User wants contact information"
   ↓
   FlowPolicy matches to: contact flow (Level 1)
   ↓
   Flow: contact
   Step: utter_contact (Level 1 - static response)
   ↓
Agent: "You can reach us at support@bank.com or call 1-800-BANK-123."
```

#### Your project at a glance

You have extended Level 1 with custom Python. Structurally, the Level 2 agent looks like this:

**Domain (`domain/basics.yml`)** — Level 1 responses (`utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`) plus an `actions:` section listing `action_bank_hours` and `action_holiday_hours` (after Lab 4.1).

**Flows (`data/basics/`)** — Level 1 flows (`greet`, `help`, `contact`, `goodbye`), the example `hours` flow that calls `action_bank_hours`, and your `holiday_hours` flow that calls `action_holiday_hours`.

**Actions (`actions/`)** — `action_bank_hours.py` (example: hours vary by day) and `action_holiday_hours.py` (yours: holiday logic and messaging from Lab 3.1).

**System patterns and configuration** — Same as Level 1 aside from any small `endpoints.yml` updates you made for actions.

Together, the agent still does everything Level 1 did, and it can run custom code for dynamic answers—processing data, branching on dates, and returning calculated or conditional text.

#### Practices that pay off

Organize **flows** so each lives in its own file when practical, use descriptive names, and group related YAML in folders if the project grows. Keep **responses** clear and concise; add variations where the platform supports them, and give users a hint toward the next useful step when it helps. Write **flow descriptions** so they are specific: say what information the user gets, using action-oriented wording—good descriptions make it easier for the policy to match the right flow.

When **testing**, cover one flow at a time, try alternate phrasings, then run a longer conversation that mixes Level 1 and Level 2 paths. Use Inspector to confirm which flow and action fired, and use `--debug` and logs when something fails to trigger, stays silent, or raises a Python error.

#### Knowledge check

Answer the five questions using **Check It!** below. Questions, choices, and feedback appear in the assessment panel after you submit.

{Check It!|assessment}(multiple-choice-1208100001)

{Check It!|assessment}(multiple-choice-1208100002)

{Check It!|assessment}(multiple-choice-1208100003)

{Check It!|assessment}(multiple-choice-1208100004)

{Check It!|assessment}(multiple-choice-1208100005)

#### Core ideas and what you can do now

You should be solid on how **actions** differ from static **responses**, how an **Action** class is structured and **registered** in the domain, how the **dispatcher** sends messages from **`run()`**, and how Rasa **executes** actions from flows. In hands-on work you created **`action_holiday_hours`**, registered it, and wired **`holiday_hours`**—alongside the Level 1 work and the **`hours` / `action_bank_hours`** example. **Level 2 keeps all Level 1 behavior**; you extended the same project rather than replacing it. The **knowledge check** above and the **readiness** list below tie those ideas to what you built in the labs.

#### What Level 2 still doesn't do

Level 2 is a strong fit for **dynamic** answers from code, **formatting** and **branching** without remembering user-specific facts across turns, and **simple integrations** when each request can be handled in isolation. It does **not** give you durable **memory** of what the user said earlier: for example, if they mention an account number once, the agent will not reliably retain it for the next turn. That is what **slots** address in Level 3. Similarly, **collecting several fields** in one task (for example transfer amount, payee, and source account) is out of scope until **multiple-slot** patterns in a later level, and **tool-style** orchestration appears in the tools-focused level—so plan to advance when your design needs memory, multi-step data collection, or richer tool use.

#### Continuing with the same agent in Level 3

When you open Level 3, you **keep the same banking agent**: your Level 1 responses, your **`hours`** and **`holiday_hours`** flows, and both **`action_bank_hours`** and **`action_holiday_hours`**, stay in the project. Level 3 adds **slots** (conversation memory), **`utter_ask_*`** style prompts, flows that **collect** slot values, and actions that **read** slots via the tracker—without starting a new codebase from scratch.

A typical Level 3 story is **“check my balance”**: at Level 2 the agent cannot hold an account number between turns; at Level 3 you can store something like an `account` slot, ask with `utter_ask_account`, and read it in an action such as `action_check_balance_simple` inside a **`check_balance`**-style flow. Expect to work with **`collect:`** in flows, **`tracker.get_slot()`** in actions, and clear **flow descriptions** so the policy still routes well.

Move to Level 3 when you need **remembered** user details, **multi-turn** tasks that depend on earlier messages, or **personalized** behavior based on stored information. Your Level 2 work remains the **foundation**; Level 3 layers memory on top.

#### Readiness for Level 3

Use this as a final pass before you leave Level 2:

- You can explain what an action is and how it differs from a response.
- You created **`action_holiday_hours`** in Lab 3.1 and understand its place next to the example action.
- **`action_holiday_hours`** (and the example action) appear under **`actions:`** in the domain where required.
- You have a flow (**`holiday_hours`**) that uses your action, in addition to the example **`hours`** flow.
- You know how actions are triggered from flows and how to spot failures in Inspector or logs.

If those points feel true, you are in good shape to start Level 3.

---
