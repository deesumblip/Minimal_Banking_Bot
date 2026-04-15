**Objective**: Add a new feature to your banking agent (new response + new flow).

Create one new response in `domain/basics.yml` and one new flow in `data/basics/` that uses it. Choose something simple (e.g. Branch locations, FAQ). Use clear flow names and descriptions. **Train** your agent (Lab 6.1), then test in Inspector.

---

#### After you change domain or flows: train again, then restart Inspector

Any time you add or edit a response or flow, Rasa must **train a new model** before those changes appear in chat. A **Rasa Inspector** session that was started earlier is still using the **previous** model until you stop it and launch Inspector again after training.

**Stop the old Inspector first.** In the terminal where Inspector is running (`rasa inspect` or the course script), press **Ctrl+C** to stop the process. If the shell is stuck or you want a completely clean session, **reset** or **close** that terminal tab and open a new terminal from the workspace or guide. You should not stack a new `rasa train` or a new Inspector launch on top of a still-running Inspect process.

**Get back to a known state, then train (Lab 6.1).** From the **project root**—the folder that contains `level1`, `level2`, and `.venv`—activate the virtual environment from Lab 0.1, then move into **`level1`**. Training must run **inside** `level1`, not from the repo root. In Codio, use a single sequence like this:

```bash
cd /home/codio/workspace
source .venv/bin/activate
cd level1
pwd
```

Your prompt should show `(.venv)`, and `pwd` should end with `level1`. If you are unsure whether you are in the right place, follow the full **In Codio** steps in **Lab 6.1** (including `ls` checks from the project root).

Train from **`level1`** with the venv active:

```bash
python -m rasa train
```

Wait until training finishes and a new model file appears under `level1/models/`, as described in Lab 6.1.

**Start Inspector again after training.** Do not assume an old Inspector tab picked up the new model. After a successful training run, **close** any leftover Inspector terminal if it is still open, then start a **new** Inspector session with the button below and open **Rasa Inspect** from the toolbar so you are chatting against the model you just built.

> To restart your agent, click **[Start Rasa Inspector](open_terminal panel=1. Cmd bash /home/codio/workspace/.guides/scripts/start_rasa_inspect.sh)**.
> Then click **Rasa Inspect** in the main toolbar above to load the chat tab.

**Working locally (not Codio)?** Activate the venv from the project root, `cd level1`, and run `python -m rasa train` as in Lab 6.1 (Windows: `.\.venv\Scripts\Activate.ps1`). Stop the old `rasa inspect` process, train again, then start Inspector in a fresh terminal.

---

**Use Check It!** below when done (Codio).

{Check It!|assessment}(code-output-compare-7772000001)
