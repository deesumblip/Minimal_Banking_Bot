# Module 4: Registering Actions in the Domain

### 4.1 Why Register Actions?

Actions must be registered in the domain file so Rasa knows they exist. Without registration, Rasa won't find your actions even if the Python files exist.

**File Location**: `domain/basics.yml`

**Analogy**: Registering an action is like adding a phone number to your contacts - you need to tell Rasa "this action exists and here's its name."

---

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
2. **Add `actions:` section** (if it doesn't exist):
   ```yaml
   actions:
     - action_bank_hours
   ```

3. **The action name must match**:
   - The return value of `name()` method: `"action_bank_hours"`
   - The class name (without `Action` prefix): `ActionBankHours` → `action_bank_hours`
   - Convention: lowercase with underscores

---

### 4.3 Step-by-Step: Registering Your Action

**Step 1: Open the Domain File**

1. Navigate to `domain/basics.yml`
2. Open it in your editor

**What you should see**: Your Level 1 responses (`utter_greet`, `utter_help`, `utter_contact`)

---

**Step 2: Add the Actions Section**

1. Find the end of the `responses:` section
2. Add a blank line
3. Add the `actions:` section:

```yaml
responses:
  utter_greet:
    - text: "Hi! I'm a banking assistant. How can I help you today?"
      metadata:
        rephrase: True

  utter_help:
    - text: |
        I can help you with:
        - Checking your balance
        - Transferring money
        - Bank hours
        - Contact information
      metadata:
        rephrase: True

  utter_contact:
    - text: "You can reach us at support@bank.com or call 1-800-BANK-123."
      metadata:
        rephrase: True

actions:                # ← NEW: Add this section
  - action_bank_hours   # ← List your actions here
```

⚠️ **Important**:
- `actions:` is at the same indentation level as `responses:`
- The dash (`-`) indicates a list item
- Action name must match exactly what `name()` returns

---

**Step 3: Verify Registration**

Check:
- ✅ `actions:` section exists
- ✅ Action name matches `name()` return value exactly
- ✅ Proper YAML syntax (indentation, dashes)
- ✅ No typos in action name

**Common mistakes**:
- ❌ Wrong action name (e.g., `action_bank_hour` instead of `action_bank_hours`)
- ❌ Missing dash before action name
- ❌ Wrong indentation
- ❌ Action name doesn't match `name()` method return value

---

### 4.4 Multiple Actions

When you have multiple actions, list them all:

```yaml
actions:
  - action_bank_hours
  - action_check_balance
  - action_process_transfer
```

Each action gets its own line with a dash.

---
