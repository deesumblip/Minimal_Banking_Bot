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

**What This Means**: When `utter_goodbye` is used, Rasa will randomly select one of the two variations, this ensures your agent won't use the same response back to back if it is activated more than once. When the rephraser is added on top, as you can see in the example, the responses will sound more varied. 


{Check It!|assessment}(code-output-compare-302300002)


---