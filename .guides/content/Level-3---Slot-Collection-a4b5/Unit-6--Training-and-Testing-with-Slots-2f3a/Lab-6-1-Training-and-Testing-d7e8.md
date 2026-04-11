**Objective**: Train your Level 3 agent (with slots) and verify it works.

**Before you begin**: Complete **Lab 5.1** so your **`check_balance`** flow and domain include slot collection and **`utter_ask_*`** responses. Training will fail if slots, ask responses, or flows are inconsistent.

**Where training runs**: Run **`python -m rasa train`** only from the **`level3`** folder with your virtual environment active. Rasa needs **`config.yml`**, **`domain/`**, and **`data/`** from **`level3`**. Do not run the command from the repository root, which is the folder that contains **`level1`**, **`level2`**, and **`level3`**.

---

#### In Codio

The terminal opens in your workspace root. If **`ls`** does not show **`level3`**, **`level2`**, and **`.guides`**, change directory to your main project folder first.

Use one continuous sequence from the project root. The venv from **Lab 0.1** in **Level 1** lives next to **`level3`**, not inside it.

```bash
ls -la .venv
source .venv/bin/activate
# If .venv is missing: python3.11 -m venv .venv && source .venv/bin/activate

cd level3
pwd
python -m rasa --version
python -m rasa train
```

Your prompt should show **`(.venv)`**, and **`pwd`** should end with **`level3`**. If **`python -m rasa --version`** fails, install Rasa Pro with the venv active: **`pip install rasa-pro`**.

Training can take **several minutes** the first time. Log output is normal. Wait until the command finishes. Do not close the terminal while it runs.

When training succeeds, the tail of the output looks roughly like this. Your model filename will differ.

```text
...
INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'
```

Confirm that **`level3/models/`** contains a new **`.tar.gz`** file.

**Success checklist** before **Check It!**:

- Your prompt shows **`(.venv)`**.
- Your current directory is **`level3`**, not the repo root.
- Training finished without errors and produced a new file under **`level3/models/`**.

The graded **Check It!** expects a **recent** model, usually within about **10 minutes** of running the assessment. If you trained earlier, run **`python -m rasa train`** again from **`level3`**, then use **Check It!**.

If training fails, Rasa usually prints a file path and line number for YAML problems. Open that file, fix the issue, save, and run **`python -m rasa train`** again from **`level3`**.

#### Common errors

| Symptom | What to do |
|--------|------------|
| **YAML or parse error with a file path and line** | Open the file at that line. Use **2 spaces**, not tabs. Save and train again from **`level3`**. |
| **Missing `utter_ask_*` for a collected slot** | Every `collect:` step needs a matching **`utter_ask_<slot_name>`** response in the domain. Add or rename it in **`domain/basics.yml`**. |
| **Slot not defined** | Ensure **`slots:`** in the domain lists the slot you collect, with a valid type. |
| **Response `utter_…` or action not found** | Align **`domain/basics.yml`** with your flows and **`actions/`** files. |
| **No module named `rasa`** | Activate the venv from the project root, **`cd level3`**, then run **`pip install rasa-pro`** if needed. |
| **`RASA_LICENSE` or `OPENAI_API_KEY` not set** | See **Lab 0.1** in **Level 1**, or ask your instructor. Level 3 may use a **`.env`** file under **`level3`** in local setups. |

---

#### Not using Codio? Training on your own machine

Follow the same rules: activate the venv from the **project root**, then **`cd level3`**, then train.

1. Open a terminal and go to the **project root**, the folder that contains **`level1`**, **`level2`**, **`level3`**, and **`.guides`**.
2. Activate the virtual environment. The **`.venv`** folder sits in the project root.
   - **Windows PowerShell**: `.\.venv\Scripts\Activate.ps1`
   - **Windows Command Prompt**: `.venv\Scripts\activate.bat`
   - **macOS or Linux**: `source .venv/bin/activate`  
   Your prompt should show **`(.venv)`**.
3. Run **`cd level3`**. Confirm with **`pwd`** that you are inside **`level3`**.
4. Ensure **`RASA_LICENSE`** and **`OPENAI_API_KEY`** are available to the process. **Lab 0.1** describes patterns; many local setups use a **`.env`** file in **`level3`**.
5. From **`level3`**, run **`python -m rasa train`**. Wait until you see **Successfully saved model**.
6. Confirm that a new **`.tar.gz`** appears under **`level3/models/`**.

Success matches Codio: training completes with no errors and a fresh model under **`models/`**. Use the **Common errors** table above if something goes wrong.

---

**Next**: In **Lab 6.2**, test slot collection and persistence in Inspector.

**Check It!** runs in the course workspace after you have a new model under **`level3/models/`**.

{Check It!|assessment}(code-output-compare-1029038275)
