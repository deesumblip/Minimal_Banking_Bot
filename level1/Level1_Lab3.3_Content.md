# Lab 3.3: Multi-Step Flow

**Objective**: Modify `greet.yml` to have two steps.

**Before You Begin**: You understand how flows work; you know where `data/basics/greet.yml` is; `utter_greet` and `utter_help` exist in your domain.

#### Steps

1. Open `data/basics/greet.yml` in your editor.
2. Find the `steps:` section (one step: `- action: utter_greet`).
3. Add a second step: `- action: utter_help` at the same indentation level as the first step.
4. Save the file.

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

**What Happens**: When a user says "hello", the bot will first greet them, then show the help message.
