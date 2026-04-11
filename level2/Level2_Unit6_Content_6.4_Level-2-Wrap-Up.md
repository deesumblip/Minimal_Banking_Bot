This page of **Unit 6** walks through a **full conversation** (Level 1 plus the example action and your Lab 3.1 action), maps **where your files live**, suggests **practices** for testing and maintenance, and ends with a short **knowledge check** (use **Check It!** for each question). **6.5** adds a brief Level 2 checkpoint and readiness list; **Level 3 Unit 0** carries the full “what you built / what slots add” recap so it is not repeated here.

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

This matches the **Level 1 baseline** described in **Unit 0.1**, plus the Level 2 actions and flows you added in the labs—listed here so you can read it beside the **conversation trace** above. You have extended Level 1 with custom Python. Structurally, the Level 2 agent looks like this:

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

**Next:** Open **6.5 Before you continue**, then **Level 3 Unit 0** for the Level 3 overview.

---
