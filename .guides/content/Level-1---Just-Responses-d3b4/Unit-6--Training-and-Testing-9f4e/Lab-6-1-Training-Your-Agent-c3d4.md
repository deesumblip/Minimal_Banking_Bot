**Objective**: Train your agent and verify it works.

**Before you begin**: Finish **Lab 3.5** so your domain and flows include **hours** and **balance**. Training will fail validation if those pieces are missing.

**Where training runs**: Run `python -m rasa train` only from the **`level1`** folder with your virtual environment active. Rasa needs `config.yml`, `domain/`, and `data/` from **`level1`**. Do not run the command from the repository root, which is the folder that contains **`level1`** and **`level2`**.

---

#### In Codio

The terminal opens in your workspace root. If `ls` does not show **`level1`**, **`level2`**, and **`.guides`**, change directory to your main project folder first.

Use one continuous sequence from the project root. The venv from **Lab 0.1** lives next to **`level1`**, not inside it.

```bash
ls -la .venv
source .venv/bin/activate
# If .venv is missing: python3.11 -m venv .venv && source .venv/bin/activate

cd level1
pwd
python -m rasa --version
python -m rasa train
```

Your prompt should show **`(.venv)`**, and **`pwd`** should end with **`level1`**. If `python -m rasa --version` fails, install Rasa Pro with the venv active: **`pip install rasa-pro`**.

Training can take **several minutes** the first time. Log output is normal. Wait until the command finishes. Do not close the terminal while it runs.

When training succeeds, the tail of the output looks roughly like this. Your model filename will differ.

```text
...
INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'
```

Confirm that **`level1/models/`** contains a new **`.tar.gz`** file.

**Success checklist** before **Check It!**:

- Your prompt shows **`(.venv)`**.
- Your current directory is **`level1`**, not the repo root.
- Training finished without errors and produced a new file under **`level1/models/`**.

The graded **Check It!** expects a **recent** model, usually within about **10 minutes** of running the assessment. If you trained earlier, run **`python -m rasa train`** again from **`level1`**, then use **Check It!**.

If training fails, Rasa usually prints a file path and line number for YAML problems. Open that file, fix the issue, save, and run **`python -m rasa train`** again from **`level1`**.

#### Common errors

| Symptom | What to do |
|--------|------------|
| **YAML or parse error with a file path and line** | Open the file at that line. Use **2 spaces**, not tabs. Check colons after keys and list items that start with **`-`**. Save and train again from **`level1`**. |
| **YAML syntax such as “block mapping”** | Fix indentation and structure, save, train again from **`level1`**. |
| **Response `utter_…` not found** | A flow references a response that is not in the domain, often **`domain/basics.yml`**. Add the response or correct the name in the flow. |
| **No module named `rasa`** | Activate the venv from the project root, **`cd level1`**, then run **`pip install rasa-pro`** if needed. |
| **RASA_LICENSE not set** | See **Lab 0.1** for setting **`RASA_LICENSE`**, or ask your instructor. |

---

#### Not using Codio? Training on your own machine

Follow the same rules as above: activate the venv from the **project root**, then **`cd level1`**, then train. Use your own terminal on Windows, macOS, or Linux.

1. Open a terminal and go to the **project root**, the folder that contains **`level1`**, **`level2`**, and **`.guides`**. For example, use **`cd`** with the path where you cloned the course repository.
2. Activate the virtual environment. The **`.venv`** folder sits in the project root.
   - **Windows PowerShell**: `.\.venv\Scripts\Activate.ps1`
   - **Windows Command Prompt**: `.venv\Scripts\activate.bat`
   - **macOS or Linux**: `source .venv/bin/activate`  
   Your prompt should show **`(.venv)`**.
3. Run **`cd level1`**. Confirm with **`pwd`** or **`cd`** that you are inside **`level1`**.
4. Set **`RASA_LICENSE`** if it is not already in your environment. **Lab 0.1** describes how to do this for local setups. A common pattern is a **`.env`** file in the project root with **`RASA_LICENSE=your-license-key`** without quotes, loaded according to your shell or tooling before you **`cd level1`**.
5. From **`level1`**, run **`python -m rasa train`**. Wait until you see a **Successfully saved model** message.
6. Confirm that a new **`.tar.gz`** appears under **`level1/models/`**.

Success means the same thing as in Codio: training completes with no errors and a fresh model file exists under **`models/`**. Use the **Common errors** table above if something goes wrong.

---

**Next**: In **Lab 6.2**, start Rasa Inspector and chat with the model you just built.

**Check It!** runs in the course workspace after you have a new model under **`level1/models/`**. Click **Check It!** below when you are ready.

{Check It!|assessment}(code-output-compare-2562507355)
