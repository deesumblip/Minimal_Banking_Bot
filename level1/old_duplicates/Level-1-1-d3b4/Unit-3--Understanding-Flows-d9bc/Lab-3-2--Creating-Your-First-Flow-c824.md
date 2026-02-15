**Objective**: Create a new `goodbye.yml` flow that uses the `utter_goodbye` response from Lab 2.2.

#### Before You Begin

**Checklist**:
- You've completed Lab 2.2 (created `utter_goodbye` in the domain)
- You know where the `data/basics/` folder is
- You have a text editor ready

#### Step-by-Step Tutorial

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

⚠️ **Pay attention to indentation**:
- `flows:` is at the start (no indentation)
- `goodbye:` is indented 2 spaces under `flows:`
- `name:`, `description:`, and `steps:` are indented 2 spaces under `goodbye:`
- `- action: utter_goodbye` is indented 4 spaces (under `steps:`)

**What each part does**:
- `flows:` - Top-level key (tells Rasa this file contains flows)
- `goodbye:` - Flow identifier (how you reference it internally)
- `name: say goodbye` - Human-readable name (for logs/debugging)
- `description: ...` - **Critical!** The LLM uses this to match user messages
- `steps:` - List of actions to execute
- `- action: utter_goodbye` - The action to perform (uses the response we created)

---

**Step 4: Verify the Structure**

Before saving, check:

**Required fields present**:
- `flows:` at the top
- Flow identifier (`goodbye:`) with colon
- `name:` field (human-readable name)
- `description:` field (what the flow does - very important!)
- `steps:` section
- At least one step (`- action: ...`)

**Indentation correct**:
- Use 2 spaces consistently
- `goodbye:` aligned under `flows:`
- `name:`, `description:`, `steps:` aligned under `goodbye:`
- `- action:` indented under `steps:`

**Response exists**:
- The response `utter_goodbye` exists in `domain/basics.yml`
- Spelling matches exactly (case-sensitive!)

**Common mistakes to avoid**:
- Missing `flows:` at the top
- Missing `description:` field (this is critical - flows won't match without it!)
- Wrong indentation
- Response name typo (e.g., `utter_goodby` instead of `utter_goodbye`)
- Missing colon after flow name (`goodbye` instead of `goodbye:`)

---

**Step 5: Save and Verify**

1. Save the file (Ctrl+S or Cmd+S)
2. Your file should now contain a complete flow definition

{Check It!|assessment}(llm-based-auto-rubric-4035286235)

#### Complete File

`data/basics/goodbye.yml`:
```yaml
flows:
  goodbye:
    name: say goodbye
    description: Farewell the user when they end the conversation.
    steps:
      - action: utter_goodbye
```

#### How Rasa Finds Flows

Rasa automatically searches the `data/` folder (and subfolders) for `.yml` files containing flows. You can organize flows however you like:
- One flow per file (recommended for clarity)
- Multiple flows per file (okay for related flows)
- Nested folders (good for organization)

---