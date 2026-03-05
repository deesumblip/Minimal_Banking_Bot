# Lab 2.2: Creating Your First Response

**Objective**: Add a new `utter_goodbye` response to your bot's domain file.

#### Before You Begin

✅ **Checklist**:
- You have a text editor or IDE open
- You know where the `domain/` folder is in your project
- You understand basic YAML syntax (review Unit 0.3 if needed)

#### Step-by-Step Tutorial

**Step 1: Navigate to the Domain File**

1. In your project folder, navigate to the `domain/` folder
2. Open the file named `basics.yml` in your text editor
3. You should see a file that starts with `version: "3.1"` followed by a `responses:` section

**What you should see**: The file should contain existing responses like `utter_greet`, `utter_help`, and `utter_contact`.

---

**Step 2: Locate the Responses Section**

1. Scroll to find the `responses:` section (it should be near the top, after `version: "3.1"`)
2. You'll see existing responses (utter_greet, utter_help, utter_contact).

**What you should see**: Multiple responses, each with the `utter_` prefix, indented properly with 2 spaces.

---

**Step 3: Add Your New Response**

1. Find the `utter_contact` response (the last one in the list)
2. After `utter_contact`, add a blank line
3. Add your new response using this exact pattern:
   ```yaml
   utter_goodbye:
     - text: "Goodbye! Have a great day!"
       metadata:
         rephrase: True
   ```

⚠️ **Important**: Pay attention to indentation:
- `utter_goodbye:` should be at the same level as `utter_contact:` (2 spaces from the left)
- `- text:` should be indented 2 more spaces (4 spaces total)
- `metadata:` should be at the same level as `text:` (6 spaces from the start of the line)
- `rephrase: True` should be indented 2 more spaces under `metadata:` (8 spaces total)

---

**Step 4: Verify Your Syntax**

Before saving, double-check:

✅ **Indentation**: Use exactly 2 spaces (not tabs, not 4 spaces)  
✅ **Structure**: Response name ends with `:`, dash before `text:`, `metadata:` aligned with `text:`  
✅ **Spelling**: `utter_goodbye` and `rephrase` spelled correctly

**Common mistakes to avoid**:
- ❌ Missing dash: `text: "..."` instead of `- text: "..."`
- ❌ Wrong indentation: Using tabs or wrong number of spaces
- ❌ Missing colon: `utter_goodbye` instead of `utter_goodbye:`

---

**Step 5: Save the File**

1. Save your changes (Ctrl+S or Cmd+S)
2. Your file should now have the new `utter_goodbye` response

#### Complete Example

Your `responses:` section should now include:

```yaml
  utter_goodbye:
    - text: "Goodbye! Have a great day!"
      metadata:
        rephrase: True
```

#### Common Mistakes

1. **Missing dash**: Forgetting the `-` before `text:` causes YAML parsing errors
2. **Wrong indentation**: YAML is very sensitive to spacing - use 2 spaces consistently
3. **Missing colon**: The response name must end with `:`
4. **Forgetting `utter_` prefix**: While not strictly required, it's a strong convention
