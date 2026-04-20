**Objective**: Train your agent and verify it works.

#### Steps

Run all commands from the **`level1`** folder with your virtual environment active. Do not run from the repository root.

```bash
ls -la .venv
source .venv/bin/activate
# If .venv is missing: python3.11 -m venv .venv && source .venv/bin/activate

cd level1
pwd
python -m rasa --version
python -m rasa train
```

Your prompt should show `(.venv)` and `pwd` should end with `level1`.

If `python -m rasa --version` fails, install Rasa with the venv active:
```bash
pip install rasa-pro==3.16.3
```

Training takes several minutes the first time. When it succeeds you will see something like:

```text
INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'
```

#### Common errors

| Symptom | What to do |
|--------|------------|
| **YAML or parse error with a file path and line** | Open the file at that line. Use **2 spaces**, not tabs. Check colons after keys and list items that start with **`-`**. Save and train again from **`level1`**. |
| **YAML syntax such as “block mapping”** | Fix indentation and structure, save, train again from **`level1`**. |
| **Response `utter_…` not found** | A flow references a response that is not in the domain, often **`domain/basics.yml`**. Add the response or correct the name in the flow. |
| **No module named `rasa`** | Activate the venv from the project root, **`cd level1`**, then run **`pip install rasa-pro==3.16.3`** if needed. |
| **RASA_LICENSE not set** | See **Lab 0.1** for setting **`RASA_LICENSE`**, or ask your instructor. |

Confirm that `level1/models/` contains a new `.tar.gz` file before clicking **Check It!** The assessment expects a model trained within the last 10 minutes. If you trained earlier, run `python -m rasa train` again.

---

**Next**: In **Lab 6.2**, start Rasa Inspector and chat with the model you just built.

**Check It!** runs in the course workspace after you have a new model under **`level1/models/`**. Click **Check It!** below when you are ready.

{Check It!|assessment}(code-output-compare-2562507355)





---