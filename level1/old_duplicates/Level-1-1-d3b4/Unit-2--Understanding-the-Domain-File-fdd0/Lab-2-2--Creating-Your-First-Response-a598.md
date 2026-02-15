**Objective**: Add a new `utter_goodbye` response to your bot's domain file.

#### Step-by-Step Tutorial

**Step 1: Navigate to the Domain File**

1. In your project folder, navigate to the `domain/` folder
2. Open the file named `basics.yml` in your text editor
3. You should see a file that starts with `version: "3.1"` followed by a `responses:` section

**What you should see**: The file should contain existing responses like `utter_greet`, `utter_help`, and `utter_contact`.

---

**Step 2: Locate the Responses Section**

1. Scroll to find the `responses:` section (it should be near the top, after `version: "3.1"`)
2. You'll see existing responses like:
   ```yaml
   responses:
     utter_greet:
       - text: "Hi! I'm a banking assistant. How can I help you today?"
         metadata:
           rephrase: True
     
     utter_help:
       - text: |
           I can help you with:
           ...
     
     utter_contact:
       - text: "You can reach us at support@bank.com or call 1-800-BANK-123."
         metadata:
           rephrase: True
   ```

**What you should see**: Multiple responses, each with the `utter_` prefix, indented properly with 2 spaces.

---

**Step 3: Add Your New Response**

1. Find the last response in the list
2. After this response, add a blank line
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

**Why add it here?** The order doesn't matter for functionality, but keeping responses organized helps with readability.

---

**Step 4: Verify Your Syntax**

Before saving, double-check:

**Indentation**: 
- Use exactly 2 spaces (not tabs, not 4 spaces)
- Use your editor's "show whitespace" feature if available

**Structure**:
- Response name ends with `:` (colon)
- `-` (dash) before `text:`
- `metadata:` is aligned with `text:`
- `rephrase: True` is under `metadata:`

**Spelling**: 
- `utter_goodbye` is spelled correctly
- `rephrase` is spelled correctly

**Common mistakes to avoid**:
- Missing dash: `text: "..."` instead of `- text: "..."`
- Wrong indentation: Using tabs or wrong number of spaces
- Missing colon: `utter_goodbye` instead of `utter_goodbye:`
- Wrong metadata indentation: `metadata:` aligned with `-` instead of `text:`

---

**Step 5: Save the File**

1. Save your changes (Ctrl+S or Cmd+S)
2. Your file should now have the new `utter_goodbye` response

#### Complete Example

Your `responses:` section should now be formatted to look like this:

```yaml
responses:
  utter_greet:
    - text: "Hi! I'm a banking assistant. How can I help you today?"
      metadata:
        rephrase: True

  utter_help:
    - text: |
        I can help you with:
        - Checking your balance
        - Transferring money
        - Bank hours
        - Contact information
      metadata:
        rephrase: True

  utter_contact:
    - text: "You can reach us at support@bank.com or call 1-800-BANK-123."
      metadata:
        rephrase: True

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

---

### 2.3 Response Variations

Having multiple variations of the same response makes your bot feel more natural and less robotic.

#### When to Use Variations{Check It!|assessment}(llm-based-auto-rubric-3895222681)


**Good for**:
- Greetings (various ways to say hello)
- Confirmations (different ways to say "yes")
- General information (can be phrased differently)

**Not good for**:
- Critical information (account numbers, error codes)
- Legal disclaimers (must be exact)
- Step-by-step instructions (clarity is more important than variety)

#### Example: Multiple Variations

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
  - text: "Hello! I'm here to help with your banking needs."
  - text: "Welcome! How can I assist you today?"
    metadata:
      rephrase: True
```

When `utter_greet` is called, Rasa randomly selects one of these three options.


---