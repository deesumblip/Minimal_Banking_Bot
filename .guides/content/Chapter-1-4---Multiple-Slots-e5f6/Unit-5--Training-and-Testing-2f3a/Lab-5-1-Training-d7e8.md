**Starting point:** Chapter 1.4 assumes you began with the **final banking agent at the end of Chapter 1.3** and added transfer pieces in **`level4/`** (see **Unit 0.1**).

Train your Level 4 assistant from the **`level4`** folder. The workflow matches **Level 3**: activate the virtual environment at the **project root**, then `cd level4` and run Rasa.

**What training uses:** Rasa loads your **domain** (slots and `utter_ask_*` responses), your **flows** (including `transfer_money`), and your **actions** (including `action_process_transfer`). Errors during training usually point back to files you edited in **Labs 2.1** (domain), **3.1** (action), or **4.1** (flow).

After training succeeds, use **Check It!** below (Codio). Then open **Lab 5.2** to run the completion check and try the transfer flow in Inspector.

---

## Part 1: In Codio

1. **Terminal**. It should open at `~/workspace` (project root).
2. **Activate the virtual environment:** `source .venv/bin/activate`, the prompt should show `(.venv)`.
3. **Go to Level 4:** `cd level4`, run `pwd` and confirm the path ends in `level4`.
4. **Check Rasa:** `python -m rasa --version`. If this fails, confirm the venv is active and Rasa Pro is installed (**Lab 0.1**).
5. **Pipeline check (important):** Open **`config.yml`** in this same **`level4/`** folder. It must use **`CompactLLMCommandGenerator`** for Chapter 1.4 (not **`SearchReadyLLMCommandGenerator`** from Chapter 1.3). If you copied **`level3/` → `level4/`** and have not applied **Unit 0.2** yet, fix **`config.yml`** and **`endpoints.yml`** first—otherwise training will **bake the wrong command generator into the model**, and you can see odd slot behavior or *“unable to understand you”* in Inspector even when domain and flows look correct. Compare with this repo’s **`level4/config.yml`** if unsure.
6. **Endpoints check:** Open **`endpoints.yml`**. Under **`model_groups`**, the group with **`id: gpt-4o-mini`** must use **`model: gpt-4o-2024-11-20`** and **`temperature: 0.1`** (**Unit 0.2** section 2). Avoid **`model: gpt-4o-mini-…`** with a high **`temperature`**—free-text **recipient** often mis-fills. Match this repo’s **`level4/endpoints.yml`**.
7. **Train:** `python -m rasa train`, wait until you see **Successfully saved model** (often about 1–3 minutes).
8. **Verify:** In the file tree, open **`models/`** (under **`level4`**) and confirm a new `.tar.gz` file is there.

### If something goes wrong

| Symptom | What to check |
|--------|----------------|
| Slot or `utter_ask_*` errors | `level4/domain/basics.yml` (**Lab 2.1**) |
| Flow or collect-step errors | `level4/data/basics/transfer_money.yml` (**Lab 4.1**) |
| Action-related errors | `level4/actions/action_process_transfer.py` (**Lab 3.1**) |
| `No module named 'rasa'` | Activate `.venv` from the **project root**, then `cd level4` again |
| License or API key errors | `.env` and **Lab 0.1**; confirm keys and paths for your workspace |
| Transfer slots mis-fill; *unable to understand you* on recipient/account; log shows **`SearchReadyLLMCommandGenerator`** | **`level4/config.yml`** must use **`CompactLLMCommandGenerator`** (**Unit 0.2**). Fix config, then **`python -m rasa train`** again from **`level4`** so the **new** model embeds the right pipeline (**Lab 5.2** troubleshooting, **`PIPELINE_CHAPTER_1_3_AND_4.md`**) |

**Use Check It!** below when the steps above are complete.

{Check It!|assessment}(code-output-compare-401050001)

---

## Part 2: Running locally

Same sequence on your machine; only the activate command changes by OS.

1. Open a terminal (PowerShell, Command Prompt, Terminal.app, or Linux shell).
2. **Project root:** `cd` to the folder that contains `level1`, `level2`, `level3`, `level4`, and `.guides` (for example `C:\Users\You\Minimal_Banking_Agent` or `~/Minimal_Banking_Agent`).
3. **Activate the virtual environment** (`.venv` lives in the project root):
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Windows (Command Prompt): `.venv\Scripts\activate.bat`
   - macOS / Linux: `source .venv/bin/activate`  
   Confirm `(.venv)` appears in the prompt.
4. **Enter Level 4:** `cd level4` (this folder should contain `config.yml`, `domain/`, and `data/`).
5. **Pipeline check:** Same as Part 1 step 5—confirm **`level4/config.yml`** uses **`CompactLLMCommandGenerator`** before training.
6. **Endpoints check:** Same as Part 1 step 6—**`level4/endpoints.yml`** **`model_groups`** matches **Unit 0.2** / this repo.
7. **Environment variables:** Ensure `.env` in the project (or under `level4`) includes `RASA_LICENSE` and `OPENAI_API_KEY`, see **Lab 0.1** if you need help.
8. **Train:** `python -m rasa train` until you see **Successfully saved model**.
9. **Verify:** A new `.tar.gz` appears under `level4/models/`.

You are done when training completes with no errors and `models/` contains a new model.

**Next:** Open **Lab 5.2**, run the **completion check** (`Check It!`), then **Rasa Inspector** using the **step-by-step turns** in the Lab 5.2 table (transfer: amount → recipient → account → demo confirmation).
