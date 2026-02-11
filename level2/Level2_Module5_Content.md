# Module 5: Using Actions in Flows

### 5.1 Actions vs. Responses in Flows

In Level 1, flows used `utter_*` responses. In Level 2, flows can use `action_*` actions.

#### Level 1 Flow (Response)

```yaml
flows:
  greet:
    name: say hello
    description: Greet the user when they start a conversation.
    steps:
      - action: utter_greet  # ← Uses a response
```

#### Level 2 Flow (Action)

```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours  # ← Uses an action
```

**Key Difference**: 
- `utter_*` = Predefined text (response)
- `action_*` = Custom Python code (action)

Both use `- action:` in the flow, but Rasa knows the difference based on the name.

---

### 5.2 Creating a Flow That Uses an Action

Let's create the `hours.yml` flow that uses `action_bank_hours`.

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

### 5.3 Mixing Responses and Actions

You can use both responses and actions in the same flow:

```yaml
flows:
  hours_and_contact:
    name: hours and contact
    description: Tell the user bank hours and provide contact information.
    steps:
      - action: action_bank_hours      # ← Action (custom code)
      - action: utter_contact          # ← Response (predefined text)
```

**Execution order**:
1. First: Action executes (returns dynamic hours)
2. Second: Response sends (static contact info)

---
