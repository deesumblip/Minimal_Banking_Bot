**Objective**: Create a new `goodbye.yml` flow that uses the `utter_goodbye` response from Lab 2.1.

#### Steps

**Step 1: Navigate to the Data Folder**

1. In your project folder, navigate to the `data/` folder
2. Open the `basics/` subfolder
3. You should see files like `greet.yml`, `help.yml`, and `contact.yml`

**What you should see**: Multiple YAML files, each containing flow definitions.

---


**Step 2: Create the New Flow File**

1. In the `data/basics/` folder, create a new file
2. Name it exactly: `goodbye.yml` (all lowercase, `.yml` extension)
3. Make sure the file is saved in `data/basics/` (not in `data/` root)

⚠️ **File naming tips**:
- Use lowercase letters
- Use underscores for multi-word names (e.g., `check_balance.yml`)
- Always use `.yml` extension (not `.yaml`)

---

**Step 3: Add the Flow Structure**

1. Open `goodbye.yml` in your editor (it will be empty)
2. Add this exact structure:

```yaml
flows:
  goodbye:
    name: say goodbye
    description: Farewell the user when they end the conversation.
    steps:
      - action: utter_goodbye
```



| Property | What it does |
|---|---|
| `flows:` | Top-level key. Tells Rasa this file contains flow definitions. |
| `goodbye:` | The flow ID. Alphanumeric characters, underscores, and hyphens only. |
| `name: say goodbye` | Human-readable label for logs and debugging. Does not affect behavior. |
| `description:` | The Command Generator uses an LLM to read this and decide when to start a flow. A good description helps the flow be activated at the right times. |
| `steps:` | The ordered list of actions the flow executes. |
| `- action: utter_goodbye` | Calls the response defined in your domain file. Spelling and casing must match exactly. |

---

**Step 4: Save and Verify**

1. Save the file (Ctrl+S or Cmd+S)
2. Your file should now contain a complete flow definition

{Check It!|assessment}(code-output-compare-303200002)

---

