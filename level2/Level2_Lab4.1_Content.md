# Lab 4.1: Registering Actions in the Domain

You'll edit `domain/basics.yml` so Rasa knows about your actions. Without this step, Rasa won't use them even though the Python files exist.

### Your Task

Add an `actions:` section to `domain/basics.yml` (if it isn't already there) and register **both**:

- **action_bank_hours** – the example action you studied in the units  
- **action_holiday_hours** – the action you created in Lab 3.1  

Each action must appear as a list item under `actions:` (e.g. `- action_bank_hours`).

---

### Step-by-Step

**Step 1: Open the domain file**

1. Navigate to `domain/basics.yml`
2. Open it in your editor

You should see your Level 1 responses (`utter_greet`, `utter_help`, `utter_contact`). If the starter already has an `actions:` section with `action_bank_hours`, add `action_holiday_hours` to the same list.

---

**Step 2: Add the actions section**

1. Find the end of the `responses:` section
2. Add a blank line
3. Add the `actions:` section (or add `action_holiday_hours` to an existing list):

```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
```

Important:
- `actions:` is at the same indentation level as `responses:` (top-level key)
- The dash (`-`) indicates a list item
- Action names must match exactly what each action’s `name()` method returns

**Common mistakes**: wrong action name (e.g. `action_bank_hour`), missing dash, wrong indentation, or a name that doesn’t match `name()`.

---

**Step 3: Verify before submitting**

- `actions:` section exists
- Both `action_bank_hours` and `action_holiday_hours` are listed
- YAML is valid (correct indentation and dashes)

Run the assessment when you're done.

---

#### Review in Inspector (optional)

After the assessment, train and open the Rasa Inspector GUI (see Unit 6.3). In the chat, try **"What are your hours?"** (should work if the `hours` flow exists) and **"What are your holiday hours?"** (likely not yet—you'll add that flow in Unit 5).
