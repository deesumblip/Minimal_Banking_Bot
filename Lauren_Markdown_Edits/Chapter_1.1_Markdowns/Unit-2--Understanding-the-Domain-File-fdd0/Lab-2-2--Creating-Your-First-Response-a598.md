**Objective**: Add a new `utter_goodbye` response to your agent's domain file.

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

**What you should see**: Different responses, each with the `utter_` prefix.

---

**Step 3: Add Your New Response**

1. Find the last response in the list
2. After this response, add a blank line
3. Add your new response. Here is an example, you can make the text your own:
   ```yaml
   utter_goodbye:
     - text: "Goodbye! Have a great day!"
       metadata:
         rephrase: True
   ```

**Why add it here?** The order doesn't matter for functionality, but keeping responses organized helps with readability.

---

**Step 4: Save the File**

1. Save your changes (Ctrl+S or Cmd+S)
2. Your file should now have the new `utter_goodbye` response that looks similar to this:

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
