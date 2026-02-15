**Objective**: Modify `greet.yml` to have two steps.

**Before You Begin**:
- You understand how flows work
- You know where `data/basics/greet.yml` is located
- The responses `utter_greet` and `utter_help` exist in your domain

#### Steps

1. Open `data/basics/greet.yml` in your editor
2. Find the `steps:` section (it should have one step: `- action: utter_greet`)
3. Add a second step: `- action: utter_help`
   - Make sure it's at the same indentation level as the first step
   - Use a dash (`-`) before `action:`
4. Save the file

**Expected Result**:
```yaml
flows:
  greet:
    name: say hello
    description: Greet the user when they start a conversation.
    steps:
      - action: utter_greet
      - action: utter_help
```

**How to Verify**:
1. Both steps are at the same indentation level (4 spaces from the left)
2. Both steps start with `- action:`
3. Both response names exist in your domain file
4. YAML syntax is correct (no errors when you save)
5. Try training your bot (Unit 6) - if training succeeds, your flow is correct!

**What Happens**: When a user says "hello", the bot will:
1. First greet them (`utter_greet`)
2. Then immediately show the help message (`utter_help`)
3. Flow completes

This creates a more helpful greeting experience!

---

### 3.4 Flow Descriptions and LLM Understanding

The `description` field is **critical** because the LLM uses it to match user messages to flows.

#### How It Works

1. User sends a message: "I need help"
2. LLM reads all flow descriptions
3. LLM matches the message to the best-fitting description
4. Rasa triggers that flow

#### Writing Good Descriptions

**Good descriptions**:
- Clear and specific: "Greet the user when they start a conversation"
- Action-oriented: "Provide contact information for the bank"
- Context-aware: "Explain what the bot can help with"

**Bad descriptions**:
- Too vague: "Help user" (what kind of help?)
- Too specific: "Respond when user says exactly 'hello'" (misses "hi", "hey")
- Missing context: "Say hello" (when? why?)

#### Example: Matching Process

**Flow Description**: "Greet the user when they start a conversation"

**User Messages That Match**:
- "hello"
- "hi"
- "hey there"
- "good morning"
- "greetings"

**Why**: The LLM understands all these are greetings that start conversations.

{Check It!|assessment}(llm-based-auto-rubric-1352381554)

---