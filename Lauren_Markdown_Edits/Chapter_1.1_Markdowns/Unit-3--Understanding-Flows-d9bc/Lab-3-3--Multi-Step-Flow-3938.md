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
5. Try training your agent (Unit 6) - if training succeeds, your flow is correct!

**What Happens**: When a user says "hello", the agent will:
1. First greet them (`utter_greet`)
2. Then immediately show the help message (`utter_help`)
3. Flow completes

This creates a more helpful greeting experience!

**Next:** Read **3.3 Flow Descriptions and LLM Understanding** for how the `description` field helps the LLM match user messages to flows. Then apply that in **Lab 3.4** with the hours and balance fill-in exercises.

{Check It!|assessment}(code-output-compare-303300002)
