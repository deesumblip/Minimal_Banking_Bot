

## In the terminal

The terminal opens at your workspace root. Activate the virtual environment and move into `level4`. :

```bash
ls -la .venv
source .venv/bin/activate
# If .venv is missing: python3.11 -m venv .venv && source .venv/bin/activate

cd level4
pwd
python -m rasa --version
python -m rasa train
```

Your prompt should show `(.venv)` and `pwd` should end with `level4`. Training can take a minute.

When it succeeds you'll see something like:

```text
INFO  rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'
```
## Verify

`level4/models/` contains a new `.tar.gz` file.
Use Check It! below to confirm.

{Check It!|assessment}(code-output-compare-401050001)

