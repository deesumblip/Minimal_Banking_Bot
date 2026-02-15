**Objective**: Add a second variation to `utter_goodbye`.

**Before You Begin**:
- You've completed Lab 2.2 (created `utter_goodbye`)
- You have `domain/basics.yml` open in your editor

#### Steps

1. Find `utter_goodbye` in `domain/basics.yml` (it should be at the end of the responses section)
2. Add a second `- text:` item with a different farewell message
   - The second `- text:` should be at the same indentation level as the first
   - Use a different farewell phrase (e.g., "See you later!", "Take care!", "Have a great day!")
3. Keep the `metadata:` section (it can be under the last text item)

**Example Solution**:
```yaml
utter_goodbye:
  - text: "Goodbye! Have a great day!"
  - text: "See you later! Take care!"
    metadata:
      rephrase: True
```

**How to Verify**:
1. Check that both `- text:` items are at the same indentation level (4 spaces from the left)
2. Check that `metadata:` is aligned with `text:` (6 spaces from the left)
3. Check that `rephrase: True` is under `metadata:` (8 spaces from the left)
4. Try training your bot (we'll learn this in Unit 6) - if training succeeds, your YAML is correct!

**What This Means**: When `utter_goodbye` is used, Rasa will randomly select one of the two variations, making your bot feel more natural.

{Check It!|assessment}(llm-based-auto-rubric-3562566144)


---