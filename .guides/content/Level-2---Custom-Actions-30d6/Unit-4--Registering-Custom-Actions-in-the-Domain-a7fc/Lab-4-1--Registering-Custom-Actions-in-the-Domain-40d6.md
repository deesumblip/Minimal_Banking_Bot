Look at the domain/basics.yml on your right. You will see your responses from Level 1 and no `actions:` section yet. 

### Step 1: Add an actions section with your new custom actions just after responses in the domain:

```yaml
# In domain/basics.yml, top level (same indentation as responses:)
actions:
  - action_bank_hours
  - action_holiday_hours
```

### Step 2: Check your work

Important:
- `actions:` is at the same indentation level as `responses:`. Both are top-level keys.
- Action names must match exactly what each action’s `name()` method returns


### Step 3: Run the assessment when you are done. 

{Check It!|assessment}(code-output-compare-1451983168)

---

