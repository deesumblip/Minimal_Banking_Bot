### 4.2 The Actions Section

In Level 1, your domain file only had a `responses:` section. Level 2 adds an `actions:` section.

#### Domain Structure in Level 2

```yaml
version: "3.1"

responses:              # ← From Level 1 (unchanged)
  utter_greet:
    - text: "Hi! I'm a banking assistant..."
  # ... other responses

actions:                # ← NEW in Level 2
  - action_bank_hours   # ← Example action
  - action_holiday_hours   # ← Your action from Lab 3.1
```

#### What You'll Do in Lab 4.1

In **Lab 4.1** you will open `domain/basics.yml`, add an `actions:` section (if needed), and list **both** the example action and the action you created in Lab 3.1. The lab gives step-by-step instructions for the file edits.

**Naming rule** (for when you do the lab): the action name in the domain must match exactly:
- The return value of the `name()` method (e.g. `"action_bank_hours"`)
- Convention: lowercase with underscores

---
