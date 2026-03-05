# Lab 3.2: Creating Your First Flow

**Objective**: Create a new `goodbye.yml` flow that uses the `utter_goodbye` response from Lab 2.2.

#### Before You Begin

✅ **Checklist**:
- You've completed Lab 2.2 (created `utter_goodbye` in the domain)
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

3. **Verify**: Required fields present (`flows:`, flow identifier, `name:`, `description:`, `steps:`, at least one step). Response `utter_goodbye` exists in `domain/basics.yml`.

4. **Save** the file.

**Common mistakes**: Missing `flows:` at the top; missing `description:`; wrong indentation; response name typo.
