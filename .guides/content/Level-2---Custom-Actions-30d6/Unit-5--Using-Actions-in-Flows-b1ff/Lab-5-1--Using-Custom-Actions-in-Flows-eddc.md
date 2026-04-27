In this lab you **create** two new flow files that can call your custom actions. 

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

### Step 3: Create your holiday_hours flow

1. Create a new file: `data/basics/holiday_hours.yml`
2. Add a flow that uses **action_holiday_hours**. That is the action you created in the prior labs.

```yaml
flows:
  holiday_hours:
    name: holiday hours
    description: Tell the user when the bank is closed or has limited hours for holidays.
    steps:
      - action: action_holiday_hours
```

### Step 4: Verify

- Both files are in `data/basics/`
- Each flow has `name:`, `description:`, and `steps:` with the correct action
- YAML syntax is correct. You can always use https://yamlchecker.com/ to check. 

Run the **below assessment** when you're done to check that everything is correct. In Unit 6 you’ll train and test both flows in Rasa Inspector. 

{Check It!|assessment}(code-output-compare-389374509)
