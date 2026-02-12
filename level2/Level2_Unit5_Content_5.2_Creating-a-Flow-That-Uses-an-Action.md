# Unit 5: Using Actions in Flows

### 5.2 Creating a Flow That Uses an Action

You need two flows that use actions: the **example** flow `hours.yml` (for `action_bank_hours`) and **your** flow `holiday_hours.yml` (for the action you created in Lab 3.1, `action_holiday_hours`).

#### The example: hours.yml

If your starter doesn’t already include it, create the `hours.yml` flow that uses `action_bank_hours` as follows.

#### Step-by-Step Tutorial

**Step 1: Navigate to Data Folder**

1. Go to `data/basics/` folder
2. You should see your Level 1 flows: `greet.yml`, `help.yml`, `contact.yml`

---

**Step 2: Create the Hours Flow**

1. Create a new file: `data/basics/hours.yml`
2. Add the flow structure:

```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours
```

**Complete file**:
```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours
```

---

**Step 3: Understanding the Flow**

- **`hours:`** - Flow identifier
- **`name: bank hours`** - Human-readable name
- **`description:`** - Critical! The LLM uses this to match user messages
- **`steps:`** - List of steps to execute
- **`- action: action_bank_hours`** - Calls your custom action

**What happens**:
1. User asks "What are your hours?"
2. LLM matches to `hours` flow (based on description)
3. Flow executes `action_bank_hours`
4. Action runs Python code
5. Action sends message via `dispatcher.utter_message()`
6. User sees: "Our bank hours are Monday-Friday 9am-5pm..."

---

**Step 4: Verify the Flow**

Check:
- ✅ File is in `data/basics/` folder
- ✅ Flow has `name:`, `description:`, and `steps:`
- ✅ Action name matches registered action exactly
- ✅ YAML syntax is correct

---

#### Your flow: holiday_hours.yml

Create a second flow for the action you built in Lab 3.1.

1. Create a new file: `data/basics/holiday_hours.yml`
2. Add a flow that uses `action_holiday_hours`:

```yaml
flows:
  holiday_hours:
    name: holiday hours
    description: Tell the user when the bank is closed or has limited hours for holidays.
    steps:
      - action: action_holiday_hours
```

- **`holiday_hours:`** – Flow identifier (used by Rasa).
- **`name:`** – Short human-readable name (e.g. "holiday hours").
- **`description:`** – Used by the LLM to match user questions (e.g. "What are your holiday hours?" or "Are you open on Christmas?"). Make it clear so the bot can trigger this flow.
- **`steps:`** – One step: call your action.

After this, you’ll have both the example flow (`hours`) and your own flow (`holiday_hours`) wired up. In Unit 6 you’ll train and test both.

**Optional:** The `utter_help` response in the domain lists what the bot can do. After adding the holiday hours flow, you can edit that response to include “Holiday hours” in the list so users know they can ask about it.

---
