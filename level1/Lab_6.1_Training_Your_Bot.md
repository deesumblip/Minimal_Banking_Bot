# Lab 6.1: Training Your Bot

**Objective**: Train your bot and verify it works.

---

## Part 1: In Codio

**1. In the terminal, go to the project folder**
- In Codio, click **Tools** → **Terminal** (or use the terminal icon).
- Navigate to the `level1` folder where your bot files live:
  ```bash
  cd level1
  ```
- Confirm you're in the right place: run `pwd` — you should see something like `/home/codio/workspace/level1`.

**2. Create and activate the virtual environment**
- Check if a virtual environment already exists:
  ```bash
  ls -la .venv
  ```
- **If `.venv` exists**: Activate it:
  ```bash
  source .venv/bin/activate
  ```
- **If `.venv` doesn't exist**: Create it first, then activate:
  ```bash
  python3.11 -m venv .venv
  source .venv/bin/activate
  ```
- **Verify activation**: Your prompt should start with `(.venv)`. If not, run `source .venv/bin/activate` again.
- **Note**: Rasa loads your `.env` when you run from `level1/`, so being in this folder with venv active is required.

**3. Install Rasa Pro (if not already installed)**
- With the venv active, check if Rasa is installed:
  ```bash
  python -m rasa --version
  ```
- **If you see an error** (e.g., "No module named 'rasa'"): Install Rasa Pro:
  ```bash
  python -m pip install --no-cache-dir rasa-pro
  ```
- Wait for installation to complete (2-5 minutes). You should see "Successfully installed rasa-pro-x.x.x" at the end.

**4. Run the training command**
- From the `level1` folder (with venv active), run:
  ```bash
  python -m rasa train
  ```
- Wait for training to complete (usually 1–3 minutes). Do not close the terminal until you see "Successfully saved model" or an error.

**5. What you'll see**
- When training starts, output will look like:
  ```
  Training Core model...
  2025-01-12 12:08:17 INFO     rasa.core.training  - Training FlowPolicy...
  2025-01-12 12:08:17 INFO     rasa.core.training  - FlowPolicy training completed.
  2025-01-12 12:08:17 INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'.
  ```
- **"Training Core model"**: Building the conversation logic  
- **"Training FlowPolicy"**: Processing your flows  
- **"Successfully saved model"**: Training completed, model saved

**6. Verify success**
- The terminal shows **"Successfully saved model to 'models/...'"** and there are no error messages at the end.
- In the file tree, open `level1/models/` — you should see a new `.tar.gz` file with a timestamp (e.g. `20250112-120817-descent-lard.tar.gz`).
- If `models/` is empty or there's no new file, training did not complete; see **Common training errors** below, fix the issue, and run the command again.

**7. Common training errors (Codio)**

| Error | What to do |
|-------|------------|
| **YAML syntax error** (e.g. "block mapping", line/column given) | Check that line: use **2 spaces** (not tabs, not 4 spaces), colons after keys, dashes before list items. Fix and save, then train again. |
| **Response 'utter_xyz' not found** | The flow uses a response that isn't in `domain/basics.yml`. Add the response in the domain or fix the typo in the flow so the name matches exactly. |
| **No module named 'rasa'** | Venv not active or Rasa not installed. Run `source .venv/bin/activate`, then `rasa --version`. If it fails, install Rasa Pro: `python -m pip install --no-cache-dir rasa-pro`. |
| **RASA_LICENSE not set** | Credentials may be pre-configured on Codio. Run the verification commands from Lab 0.1 step 5; if they report "is not set", ask your instructor. Otherwise run training from the `level1/` folder. |

**AI Coach**: Ask "How do I know training succeeded?" or "What should I see when training works?"

---

## Part 2: Running locally

If you're **not** using Codio, follow these steps:

**1. Open a terminal and go to the project folder**
- Open a terminal (PowerShell on Windows, Terminal.app on Mac, or Terminal on Linux).
- Navigate to your project root, then `cd level1` (or whatever folder contains `config.yml`, `domain/`, `data/`).
- Confirm you're in the right place: check that `config.yml` exists in the current directory.

**2. Create and activate the virtual environment**
- Check if a virtual environment already exists:
  - Linux/Mac: `ls -la .venv`
  - Windows: `dir .venv` (PowerShell) or `dir .venv` (Cmd)
- **If `.venv` exists**: Activate it:
  - Linux/Mac: `source .venv/bin/activate`
  - Windows PowerShell: `.venv\Scripts\Activate.ps1`
  - Windows Cmd: `.venv\Scripts\activate.bat`
- **If `.venv` doesn't exist**: Create it first, then activate:
  - Linux/Mac: `python3.11 -m venv .venv` then `source .venv/bin/activate`
  - Windows: `python -m venv .venv` then `.venv\Scripts\Activate.ps1` (PowerShell) or `.venv\Scripts\activate.bat` (Cmd)
- **Verify activation**: Your prompt should start with `(.venv)`. If not, activate it again.

**3. Install Rasa Pro (if not already installed)**
- With the venv active, check if Rasa is installed:
  ```bash
  python -m rasa --version
  ```
- **If you see an error** (e.g., "No module named 'rasa'"): Install Rasa Pro:
  ```bash
  python -m pip install --no-cache-dir rasa-pro
  ```
- Wait for installation to complete (2-5 minutes). You should see "Successfully installed rasa-pro-x.x.x" at the end.

**4. Set up environment variables**
- Rasa loads `.env` from the current directory. Create a `.env` file in the same folder as `config.yml` with:
  ```
  RASA_LICENSE=your-actual-license
  ```
- **Important**: No quotes around values; no placeholder values. If you see "RASA_LICENSE not set", check that `.env` exists, has the right variable name, and you're running `rasa train` from that folder.

**5. Run the training command**
- From the project folder (with venv active), run:
  ```bash
  python -m rasa train
  ```
- Wait for training to complete (usually 1–3 minutes). Do not close the terminal until you see "Successfully saved model" or an error.

**6. What you'll see**
- When training starts, output will look like:
  ```
  Training Core model...
  2025-01-12 12:08:17 INFO     rasa.core.training  - Training FlowPolicy...
  2025-01-12 12:08:17 INFO     rasa.core.training  - FlowPolicy training completed.
  2025-01-12 12:08:17 INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'.
  ```
- **"Training Core model"**: Building the conversation logic  
- **"Training FlowPolicy"**: Processing your flows  
- **"Successfully saved model"**: Training completed, model saved

**7. Verify success**
- The terminal shows **"Successfully saved model to 'models/...'"** and there are no error messages at the end.
- Check the `models/` folder — you should see a new `.tar.gz` file with a timestamp (e.g. `20250112-120817-descent-lard.tar.gz`).
- If `models/` is empty or there's no new file, training did not complete; check error messages and fix the issue, then run the command again.

**8. Common training errors (local)**

| Error | What to do |
|-------|------------|
| **YAML syntax error** (e.g. "block mapping", line/column given) | Check that line: use **2 spaces** (not tabs, not 4 spaces), colons after keys, dashes before list items. Fix and save, then train again. |
| **Response 'utter_xyz' not found** | The flow uses a response that isn't in `domain/basics.yml`. Add the response in the domain or fix the typo in the flow so the name matches exactly. |
| **No module named 'rasa'** | Venv not active or Rasa not installed. Activate the venv, then run `python -m pip install --no-cache-dir rasa-pro`. |
| **RASA_LICENSE not set** | Create a `.env` file in the same folder as `config.yml` with `RASA_LICENSE=...` (no quotes, no placeholders). Make sure you're running `rasa train` from that folder. |

**AI Coach**: Ask "Where do I put my Rasa license?" or "How do I set environment variables?"

---
