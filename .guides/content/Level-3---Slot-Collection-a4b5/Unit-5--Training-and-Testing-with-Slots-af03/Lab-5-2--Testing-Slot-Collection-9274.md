Run Inspector and confirm that the `account` slot is collected, used, and persisted correctly.

Make sure you have a trained model in `level3/models/` before starting.

## Start Inspector

If the venv is not active, go to the project root, then run:

```bash
source .venv/bin/activate
cd level3
```

Then from `level3` with the venv active:

```bash
mkdir -p logs
python -m rasa inspect --debug --log-file logs/logs.out
```

Click the **Rasa Inspect** button in the menu above to open Inspector.

## What to test

**Slot collection.** Type `Check my balance`. The agent should ask for your account number. Type `1234`. The agent should respond with a balance for that account.

**Slot persistence.** Type `What's my balance?` again. The agent should use `1234` without asking again.

**Previous flows.** Type `What are your hours?` and `Hello` to confirm Level 1 and 2 flows still work.

Use the debug panel to watch the `account` slot being set and reused across turns.

---

## Check Your Knowledge

{Check It!|assessment}(multiple-choice-2446085116)

{Check It!|assessment}(multiple-choice-3751028362)

{Check It!|assessment}(multiple-choice-2697467428)
