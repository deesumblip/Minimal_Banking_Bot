# Lab 6.1: Training Your Agent

**Objective**: Train your agent and verify it works.

---

## Steps

**Where training runs**: Always run `python -m rasa train` from the **`level1`** folder with your virtual environment active—not from the repository root alone.

**1. Open the terminal and confirm project root**

- The terminal starts in your workspace root. You need the **main project folder** — the one that contains `level1`, `level2`, and `.guides`. Use `ls` to confirm you see those names before you activate the venv.
- Run `ls -la .venv`. If the virtual environment exists, activate it: `source .venv/bin/activate`. If not: `python3.11 -m venv .venv` then `source .venv/bin/activate`. Your prompt should show `(.venv)`.

**2. Navigate to level1**

- `cd level1` and confirm with `pwd` — the path should end in `level1`.

**3. Install Rasa Pro (if not already installed)**

- With the venv active, run `python -m rasa --version`. If you see an error (e.g. "No module named 'rasa'"): `python -m pip install --no-cache-dir rasa-pro`.

**4. Run the training command**

- From `level1` with venv active:

  ```bash
  python -m rasa train
  ```

- Training can take **several minutes**; log output is verbose and normal. Do not close the terminal until the command finishes or reports an error.

**5. What success looks like**

- You should see a line like **"Successfully saved model to 'models/...'"** and a new `.tar.gz` under `level1/models/`.

Example tail (your filename will differ):

```text
INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'
```

**6. Success checklist** (before Check It!)

- Prompt shows `(.venv)`.
- `pwd` ends with `level1`.
- A new `.tar.gz` exists under `level1/models/`.

The assessment expects a **recent** model (about **10 minutes**). Re-run `python -m rasa train` in `level1` if your last train was long ago, then use Check It!.

**7. If training fails**

- If Rasa prints a **file and line** for a YAML error, open that file, fix it, save, and train again from `level1`.

**8. Next**

- **Lab 6.2** starts Rasa Inspector so you can chat with this model.

#### Common errors

| Symptom | What to do |
|--------|------------|
| **YAML / parse error with file path and line** | Open that file at the line; fix indentation (2 spaces), save, train again from `level1`. |
| **YAML syntax** (e.g. "block mapping") | Fix structure and spacing, save, train again. |
| **Response `utter_xyz` not found** | Add the response in `domain/basics.yml` or fix the flow name. |
| **No module named 'rasa'** | `source .venv/bin/activate` from project root, `cd level1`, install `rasa-pro` if needed. |
| **RASA_LICENSE not set** | Credentials may be pre-configured in the course environment. Run Lab 0.1 verification; ask your instructor if needed. |

---

**Use Check It!** after a fresh train and a new model under `models/` (same workspace as your project).

{Check It!|assessment}(code-output-compare-2562507355)
