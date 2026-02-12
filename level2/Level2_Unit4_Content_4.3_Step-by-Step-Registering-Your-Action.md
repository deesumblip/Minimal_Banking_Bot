### 4.3 Step-by-Step: Registering Your Action

**Step 1: Open the Domain File**

1. Navigate to `domain/basics.yml`
2. Open it in your editor

**What you should see**: Your Level 1 responses (`utter_greet`, `utter_help`, `utter_contact`). If the starter already has an `actions:` section with `action_bank_hours`, add `action_holiday_hours` to the same list (the action you created in Lab 3.1).

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

actions:                # ← NEW: Add this section (or add to existing)
  - action_bank_hours   # ← Example action
  - action_holiday_hours   # ← Your action from Lab 3.1
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
