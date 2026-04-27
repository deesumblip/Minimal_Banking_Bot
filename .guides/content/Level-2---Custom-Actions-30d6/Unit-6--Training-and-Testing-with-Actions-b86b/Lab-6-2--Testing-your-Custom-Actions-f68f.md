Now that you have trained your agent, this lab is to reinforce how to test your flows and your new actions end-to-end in Rasa Inspector. 

**Before you start:** If it isn't still activated, activate your virtual environment from the project root and make sure you are in `level2/`. 

---

#### Step 1: Start Inspector
In this step we start the inspector with `rasa inspect`. With the following commands, you will also set up a logs folder so we can assess that inspector was started. 

```bash
mkdir -p logs
python -m rasa inspect --debug --log-file logs/logs.out
```

Leave this running and click on the **Rasa Inspect** button in the menu at the top of the screen to open the Rasa Inspector interface. 


#### Step 2: Run test inputs in the chat

Use these inputs to verify the latest flows and actions:

| You ask | Expected flow | Expected action / behavior |
|--------|----------------|----------------------------|
| **"Hello"** | `greet` | Level 1 greeting |
| **"What are your hours?"** / **"When are you open?"** | `hours` | `action_bank_hours` |
| **"What are your holiday hours?"** / **"Are you open on holidays?"** / **"Are you open on Christmas?"** | `holiday_hours` | `action_holiday_hours` |
| **"Help"** | `help` | Level 1 help |
| **"How can I contact you?"** | `contact` | Level 1 contact |

#### Step 3: Take a tour of inspector

When you are in Inspector, you can see the flows being activated during the conversation. Take a look at the "Tracker State" tab to get a deep dive look at how Rasa is interpreting the user input and selecting what to do next. 

##### Common issues

1. **Action doesn't trigger.** Check whether the flow `description` matches what the user said, whether the action is listed under `actions:` in the domain, and whether the Python file exists under `actions/`.
2. **Action runs but no message.** Confirm `dispatcher.utter_message()` is called. Check `logs/logs.out` for Python errors.
3. **Python errors.** Fix syntax, imports, and method names such as `name()` and `run()`, then train again.

---

#### Run the Lab 6.2 assessment

Run the assessment when done. It checks that `level2/logs/logs.out` exists and that you ran `rasa inspect` with `--log-file`.


{Check It!|assessment}(code-output-compare-1597644299)

