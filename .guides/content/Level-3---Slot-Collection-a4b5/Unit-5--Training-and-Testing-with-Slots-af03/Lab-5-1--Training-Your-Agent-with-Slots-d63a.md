Training validates that all slots, responses, and flows are consistent and packages them into a model.

**Before you begin:** Complete Labs 2.1 through 4.1. Training will fail if any slot, response, or action name is missing or mismatched.

---

## In the terminal

The terminal opens at your workspace root. Activate the virtual environment and move into `level3`:

```bash
ls -la .venv
source .venv/bin/activate
# If .venv is missing: python3.11 -m venv .venv && source .venv/bin/activate

cd level3
pwd
python -m rasa --version
python -m rasa train
```

Your prompt should show `(.venv)` and `pwd` should end with `level3`. Training takes about a minute.

When it succeeds you'll see something like:

```text
INFO  rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'
```

## Verify

`level3/models/` contains a new `.tar.gz` file.

Use **Check It!** below to confirm.

{Check It!|assessment}(code-output-compare-1029038275)
