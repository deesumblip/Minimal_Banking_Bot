**Objective**: Modify `greet.yml` to have two steps.

#### Steps

1. Open `data/basics/greet.yml` in your editor
2. Find the `steps:` section (it should have one step: `- action: utter_greet`)
3. Add a second step: `- action: utter_help`
   - Make sure it's at the same indentation level as the first step
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

**What Happens**: When a user says "hello", the agent will run both steps in order: greet first (`utter_greet`), then show the help message (`utter_help`). This allows you to stack multiple steps in a row. 

**Next:** Read **3.2 Flow Descriptions and LLM Understanding** for how the `description` field helps the LLM match user messages to flows. Then apply that in **Lab 3.4** with the hours and balance fill-in exercises.

{Check It!|assessment}(code-output-compare-303300002)
