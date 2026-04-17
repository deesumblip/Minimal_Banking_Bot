**Where to work:** Do this lab from the **level2** folder. All file paths below are relative to `level2`.

- **In Codio:** The terminal opens in the workspace (`~/workspace`), which is the main project folder. Run `cd level2` and you're in the right place.
- **Running locally:** Open your terminal in the main project folder (the one that contains `level1`, `level2`, and `.guides`), then run `cd level2`.

---

In **Unit 5.1** you saw how actions are used in flows, including the **hours** flow with `action_bank_hours`. In this lab you **create** two new flow files. The **example** flow is `hours.yml` and calls `action_bank_hours`. **Your** flow is `holiday_hours.yml` and calls `action_holiday_hours`, which is the action you created in **Lab 3.1**. Follow the steps below, then run the assessment.

### Step 1: Navigate to the data folder

1. Go to the `data/basics/` folder inside your `level2` project.
2. You should see your Level 1 flows: `greet.yml`, `help.yml`, `contact.yml`, `goodbye.yml`.

### Step 2: Create the hours flow

1. Create a new file: `data/basics/hours.yml`
2. Add the following flow so it uses `action_bank_hours`:

```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours
```

- **`hours:`** identifies the flow. **`name:`** and **`description:`** help the LLM match what the user said, such as asking for bank hours. **`steps:`** calls your custom action.

### Step 3: Create your holiday_hours flow

1. Create a new file: `data/basics/holiday_hours.yml`
2. Add a flow that uses **action_holiday_hours**. That is the action you created in **Lab 3.1**.

```yaml
flows:
  holiday_hours:
    name: holiday hours
    description: Tell the user when the bank is closed or has limited hours for holidays.
    steps:
      - action: action_holiday_hours
```

- **`holiday_hours:`** identifies the flow. **`name:`** and **`description:`** should make it easy for the LLM to match questions about holiday hours or specific holidays such as Christmas.

### Step 4: Verify

- Both files are in `data/basics/`
- Each flow has `name:`, `description:`, and `steps:` with the correct action
- YAML syntax uses spaces, not tabs

Run the **Lab 5.1 assessment** when you're done. In Unit 6 you’ll train and test both flows; **Lab 6.2** includes Inspector setup, example questions, and debugging tips.

{Check It!|assessment}(code-output-compare-389374509)
