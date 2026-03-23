Train your Level 4 assistant from the **`level4`** folder. The workflow matches **Level 3**: activate the virtual environment at the **project root**, then `cd level4` and run Rasa.

**What training uses:** Rasa loads your **domain** (slots and `utter_ask_*` responses), your **flows** (including `transfer_money`), and your **actions** (including `action_process_transfer`). Errors during training usually point back to files you edited in **Labs 2.1** (domain), **3.1** (action), or **4.1** (flow).

After training succeeds, use **Check It!** below (Codio). Then open **Lab 5.2** to run the completion check and try the transfer flow in Inspector.

---

## Part 1: In Codio

1. **Terminal** — It should open at `~/workspace` (project root).
2. **Activate the virtual environment:** `source .venv/bin/activate` — the prompt should show `(.venv)`.
3. **Go to Level 4:** `cd level4` — run `pwd` and confirm the path ends in `level4`.
4. **Check Rasa:** `python -m rasa --version`. If this fails, confirm the venv is active and Rasa Pro is installed (**Lab 0.1**).
5. **Train:** `python -m rasa train` — wait until you see **Successfully saved model** (often about 1–3 minutes).
6. **Verify:** In the file tree, open `level4/models/` and confirm a new `.tar.gz` file is there.

### If something goes wrong

| Symptom | What to check |
|--------|----------------|
| Slot or `utter_ask_*` errors | `level4/domain/basics.yml` (**Lab 2.1**) |
| Flow or collect-step errors | `level4/data/basics/transfer_money.yml` (**Lab 4.1**) |
| Action-related errors | `level4/actions/action_process_transfer.py` (**Lab 3.1**) |
| `No module named 'rasa'` | Activate `.venv` from the **project root**, then `cd level4` again |
| License or API key errors | `.env` and **Lab 0.1**; ask your instructor if needed |

**Use Check It!** below when the steps above are complete.

{Check It!|assessment}(code-output-compare-401050001)

---

## Part 2: Running locally

Same sequence on your machine; only the activate command changes by OS.

1. Open a terminal (PowerShell, Command Prompt, Terminal.app, or Linux shell).
2. **Project root:** `cd` to the folder that contains `level1`, `level2`, `level3`, `level4`, and `.guides` (for example `C:\Users\You\Minimal_Banking_Bot` or `~/Minimal_Banking_Bot`).
3. **Activate the virtual environment** (`.venv` lives in the project root):
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Windows (Command Prompt): `.venv\Scripts\activate.bat`
   - macOS / Linux: `source .venv/bin/activate`  
   Confirm `(.venv)` appears in the prompt.
4. **Enter Level 4:** `cd level4` (this folder should contain `config.yml`, `domain/`, and `data/`).
5. **Environment variables:** Ensure `.env` in the project (or under `level4`) includes `RASA_LICENSE` and `OPENAI_API_KEY` — see **Lab 0.1** if you need help.
6. **Train:** `python -m rasa train` until you see **Successfully saved model**.
7. **Verify:** A new `.tar.gz` appears under `level4/models/`.

You are done when training completes with no errors and `models/` contains a new model.

**Next:** Open **Lab 5.2** — run the **completion check** (`Check It!`), then **Rasa Inspector** using the **step-by-step turns** in the Lab 5.2 table (transfer: amount → recipient → account → demo confirmation).
