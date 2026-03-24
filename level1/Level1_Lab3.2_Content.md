# Lab 3.2: Creating Your First Flow

**Objective**: In Unit 3.2 you saw the structure of a flow (e.g. `greet.yml`). In this lab you create your own flow: `goodbye.yml`, using the `utter_goodbye` response from Lab 2.2.

**Why create a goodbye flow**: You already added the goodbye response in the domain (Lab 2.2). The agent still doesn't know *when* to say it. A flow ties "user is ending the conversation" to "say utter_goodbye." Once this flow exists and has a clear description, the LLM can match phrases like "bye" or "that's all" and the agent will respond with your goodbye message.

#### Before You Begin

✅ **Checklist**:
- You've completed Lab 2.2 and created `utter_goodbye` in the domain
- You know where the `data/basics/` folder is
- You have a text editor ready

#### Steps

1. **Navigate to** `data/basics/` and create a new file named `goodbye.yml`.

2. **Add this structure** (pay attention to 2-space indentation):

```yaml
flows:
  goodbye:
    name: say goodbye
    description: Farewell the user when they end the conversation.
    steps:
      - action: utter_goodbye
```

3. **Verify**: Required fields are present: `flows:`, flow identifier, `name:`, `description:`, `steps:`, and at least one step. Confirm that the response `utter_goodbye` exists in `domain/basics.yml`.

4. **Save** the file.

**Common mistakes**: Missing `flows:` at the top; missing `description:`; wrong indentation; response name typo.
