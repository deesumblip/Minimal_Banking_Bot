The **domain file** is a Rasa agent's knowledge base. It defines everything the agent "knows":
- What it can **say** (responses)
- What code it can **run** (actions) - introduced in Level 2
- What it can **remember** (slots) - introduced in Level 3

**File Location**: `domain/basics.yml`

**Analogy**: The domain is like a dictionary that defines all the words (responses) the agent can use.

#### Domain Structure

The domain file has three main sections (but Level 1 only uses `responses:`):

```yaml
version: "3.1"        # Rasa YAML schema version (always "3.1")

responses:            # ← Level 1: We use this section
                      # All predefined messages go here

slots:                # ← Level 3: Memory variables (not used in Level 1)
                      # Memory variables go here

actions:              # ← Level 2: Names of available actions (not used in Level 1)
                      # Custom Python code goes in actions/
```

⚠️ **For Level 1**: We only use the `responses:` section. The `slots:` and `actions:` sections are empty (we'll learn about them in later levels).

---
