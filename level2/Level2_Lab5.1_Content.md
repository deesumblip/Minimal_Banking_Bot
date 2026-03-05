# Lab 5.1: Using Actions in Flows

**Where to work:** Do this lab from the **level2** folder. All file paths below are relative to `level2`.

- **In Codio:** The terminal opens in the workspace (`~/workspace`), which is the main project folder. Run `cd level2` and you're in the right place.
- **Running locally:** Open your terminal in the main project folder (the one that contains `level1`, `level2`, and `.guides`), then run `cd level2`.

---

You need two flows that use actions: the **example** flow `hours.yml` (for `action_bank_hours`) and **your** flow `holiday_hours.yml` (for the action you created in Lab 3.1, `action_holiday_hours`). Follow the steps below, then run the assessment.

### Step 1: Navigate to the data folder

1. Go to the `data/basics/` folder (under `level2`).
2. You should see your Level 1 flows: `greet.yml`, `help.yml`, `contact.yml`.

### Step 2: Create or ensure the hours flow

1. Create a new file (or open it if your starter already has it): `data/basics/hours.yml`
2. Add the following flow so it uses `action_bank_hours`:

```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours
```

- **`hours:`** – Flow identifier. **`name:`** and **`description:`** – The LLM uses the description to match user messages (e.g. "What are your hours?"). **`steps:`** – Calls your custom action.

### Step 3: Create your holiday_hours flow

1. Create a new file: `data/basics/holiday_hours.yml`
2. Add a flow that uses **action_holiday_hours** (the action you created in Lab 3.1):

```yaml
flows:
  holiday_hours:
    name: holiday hours
    description: Tell the user when the bank is closed or has limited hours for holidays.
    steps:
      - action: action_holiday_hours
```

- **`holiday_hours:`** – Flow identifier. **`name:`** and **`description:`** – Make the description clear so the LLM can match questions like "What are your holiday hours?" or "Are you open on Christmas?"

### Step 4: Verify

- Both files are in `data/basics/`
- Each flow has `name:`, `description:`, and `steps:` with the correct action
- YAML syntax is correct (spaces, no tabs)

Run the **Lab 5.1 assessment** when you're done. In Unit 6 you'll train and test both flows.

#### Review in Inspector (optional)

Follow the steps in **Lab 4.2** (go to main folder → activate the virtual environment → `cd level2` → train → start Inspector and open the GUI) to see if your bot is working. Then try: **"What are your hours?"** (should trigger `hours` and `action_bank_hours`), **"What are your holiday hours?"** or **"Are you open on Christmas?"** (should trigger `holiday_hours` and `action_holiday_hours`), and **"Hello"** (Level 1 greet). If something doesn't trigger, check the flow's `description` and re-train; see Unit 6.4 for debugging.

**Optional:** You can edit the `utter_help` response in the domain to include "Holiday hours" so users know they can ask about it.
