# Lab 6.1: Training Your Agent

**Objective**: Train your agent and verify it works.

**Why this lab**: So far you've only edited YAML. Training is what turns that into a runnable agent. You run one command; Rasa validates your domain and flows and writes a model file. If something is wrong, for example a flow references a response that doesn't exist, training will fail and tell you. Once it succeeds, you have a model you can run in Inspector and test. No training, no agent.

**Before you begin**: Complete Lab 3.6 (Adding New Flows) so your domain and flows (hours, balance) are set up; then training will pass validation.

**Where training runs**: Always run `python -m rasa train` from the **`level1`** folder with your virtual environment active. Do **not** run it from the repository root (the folder that contains `level1` and `level2`)—Rasa needs `config.yml`, `domain/`, and `data/` from inside `level1`.

**Confirm you are in the right project root** (before `cd level1`): In the terminal, `ls` should list folders such as `level1`, `level2`, and `.guides`. If you do not see those, `cd` to the main project folder first, then activate the venv there.

Typical command sequence (project root contains `level1`, `level2`, `.guides`, and `.venv` after Lab 0.1):

```bash
# From project root
ls -la .venv
source .venv/bin/activate
# If .venv is missing: python3.11 -m venv .venv && source .venv/bin/activate

cd level1
pwd
python -m rasa --version
python -m rasa train
```

1. **Virtual environment**: Open the terminal (it starts in your workspace root). Go to the main project folder if needed—the one that contains `level1`, `level2`, and `.guides`. Run `ls -la .venv`. If it exists: `source .venv/bin/activate`. If not: `python3.11 -m venv .venv` then `source .venv/bin/activate`. Your prompt should show `(.venv)`.
2. **Navigate to level1**: `cd level1`. Confirm with `pwd` (the path should end in `level1`).
3. **Rasa**: Run `python -m rasa --version`. If you see an error, install Rasa Pro with the venv active: `pip install rasa-pro`.
4. **Train**: With the venv still active and your **current directory still `level1`**, run `python -m rasa train`.

   Training can take **several minutes** the first time. The terminal will print many log lines; that is normal. Wait until the command finishes—do not close the terminal while it runs.

   When training succeeds, the tail of the output looks roughly like this (your model filename will differ):

   ```text
   ...
   INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'
   ```

5. **Verify**: You should see a line like **Successfully saved model to 'models/...'**. In the file tree, `level1/models/` should contain a new `.tar.gz` file.

**Success checklist** (before you use Check It!):

- Prompt shows `(.venv)`.
- `pwd` ends with `level1` (you did not run `rasa train` from the repo root).
- Training exited without an error and created a new file under `level1/models/`.

The graded Check It! expects a **recent** model (typically within about **10 minutes** of running the assessment). If you trained a long time ago, run `python -m rasa train` again in `level1`, then use Check It!.

**If training fails**, Rasa usually names the file and line number (for example a YAML parse error). Open that file in the editor, fix the issue, save, and run `python -m rasa train` again from `level1`.

#### Common errors

| Symptom | What to do |
|--------|------------|
| **YAML / parse error with a file path and line** | Open the file at that line. Use **2 spaces** (not tabs), colons after keys, list items with `-`. Save and train again from `level1`. |
| **YAML syntax** (e.g. "block mapping") | Same as above: fix indentation and structure, save, train again. |
| **Response `utter_…` not found** | The flow references a response missing from the domain (often `domain/basics.yml`). Add the response or fix the name in the flow. |
| **No module named `rasa`** | Activate the venv from project root, `cd level1`, then `pip install rasa-pro` if needed. |
| **RASA_LICENSE not set** | Check Lab 0.1 (set `RASA_LICENSE`) or ask your instructor. |

**Next**: In **Lab 6.2**, you will start Rasa Inspector and chat with the model you just built.

**Use Check It!** after training finishes and you have a new model under `level1/models/`. Run it from the normal course workspace (same project as your terminal); you do not need a separate step beyond clicking Check It! below.

{Check It!|assessment}(code-output-compare-2562507355)
