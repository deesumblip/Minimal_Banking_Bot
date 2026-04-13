# Lab 3.3: Multi-Step Flow

**Objective**: Modify `greet.yml` to have two steps.

**Why multi-step flows**: So far each flow has done one thing, such as say greet or say goodbye. In real conversations you often want a short sequence: for example, greet the user and then immediately show what the agent can do. Adding a second step to the greet flow does exactly that. One trigger like "hello" runs two actions in order: greet, then help. You'll use the same idea whenever one user message should lead to several agent replies.

**Before You Begin**: You understand how flows work; you know where `data/basics/greet.yml` is; `utter_greet` and `utter_help` exist in your domain.

#### Steps

1. Open `data/basics/greet.yml` in your editor.
2. Find the `steps:` section. It has one step: `- action: utter_greet`.
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

**What Happens**: When a user says "hello", the agent will first greet them, then show the help message.

**Next:** Read **3.3 Flow Descriptions and LLM Understanding** for how the `description` field helps the LLM match user messages to flows. Then apply that in **Lab 3.4** (hours and balance fill-in exercises in the guides), followed by **Lab 3.5** to add those flows to your project.
