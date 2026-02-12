# Unit 4: Registering Actions in the Domain

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
  - action_bank_hours   # ← Register your actions here
```

#### How to Register an Action

1. **Open `domain/basics.yml`**
2. **Add `actions:` section** (if it doesn't exist), and list **both** the example action and the action you created in Lab 3.1:
   ```yaml
   actions:
     - action_bank_hours
     - action_holiday_hours
   ```

3. **The action name must match**:
   - The return value of `name()` method: `"action_bank_hours"`
   - The class name (without `Action` prefix): `ActionBankHours` → `action_bank_hours`
   - Convention: lowercase with underscores

---
