
The **domain file** is the agent’s knowledge base. It defines everything the agent is allowed to “know” in one place:

- What it can **say**, using **responses**
- What it could **remember**, using **slots** in later levels. **Level 1** does not use slots yet.
- What code it could **run**, using **actions** in later levels. **Level 1** does not use actions yet.

**Where it lives:** `domain/basics.yml`.

**Analogy:** The domain is like a dictionary of the phrases the agent is permitted to use. Flows choose *when* to speak; the domain defines *what* can be said.

#### Domain structure

A full Rasa domain may declare **responses**, **slots**, and **actions**, but **Level 1** only uses the **`responses:`** block:

```yaml
version: "3.1"        # Rasa version (always "3.1" for current Rasa Pro)

responses:            # ← Level 1: We use this section
                      # All predefined messages go here

slots:                # ← Level 3: Memory variables (not used in Level 1)
                      # Memory variables go here

actions:              # ← Level 2: Custom Python code (not used in Level 1)
                      # Custom Python code goes here
```

⚠️ **For Level 1:** Put all canned messages under **`responses:`**. Leave **`slots:`** and **`actions:`** empty for now; later units introduce memory and custom code when you are ready.

---
