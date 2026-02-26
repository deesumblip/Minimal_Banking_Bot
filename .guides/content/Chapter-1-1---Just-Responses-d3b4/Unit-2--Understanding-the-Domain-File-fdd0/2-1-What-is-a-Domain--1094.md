
The **domain file** is the bot's knowledge base. It defines everything the bot "knows":
- What it can **say** (responses)
- What it can **remember** (slots) - not in Level 1
- What code it can **run** (actions) - not in Level 1

**File Location**: `domain/basics.yml`

**Analogy**: The domain is like a dictionary that defines all the words (responses) the bot can use.

#### Domain Structure

The domain file has three main sections (but Level 1 only uses `responses:`):

```yaml
version: "3.1"        # Rasa version (always "3.1" for current Rasa Pro)

responses:            # ← Level 1: We use this section
                      # All predefined messages go here

slots:                # ← Level 3: Memory variables (not used in Level 1)
                      # Memory variables go here

actions:              # ← Level 2: Custom Python code (not used in Level 1)
                      # Custom Python code goes here
```

⚠️ **For Level 1**: We only use the `responses:` section. The `slots:` and `actions:` sections are empty (we'll learn about them in later levels).

---
