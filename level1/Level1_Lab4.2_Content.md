# Lab 4.2: Modifying System Patterns

**Objective**: Modify `pattern_session_start` to greet the user and provide contact information.

**Why modify session start**: By default the agent might only greet. Adding a second step, such as contact info, means every new user immediately sees how to reach you. You're designing the first impression of the agent: what it says before the user has typed anything.

#### Steps

1. Open `data/system/patterns/patterns.yml`
2. Find `pattern_session_start`
3. Add a second step: `- action: utter_contact`
4. Save and test

**Expected Result**:
```yaml
pattern_session_start:
  name: pattern session start
  description: Start the conversation with a greeting
  nlu_trigger:
    - intent: session_start
  steps:
    - action: utter_greet
    - action: utter_contact
```

**What Happens**: New conversations start with greeting, then contact info.
