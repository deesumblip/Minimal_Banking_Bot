# Lab 0.1: Create Virtual Environment and Install Rasa Pro

**Objective**: Create a virtual environment in the **project root**, install Rasa Pro in it, and verify the installation is successful.

**Important**: This is your first step! You must create a virtual environment and install Rasa Pro before you can proceed with any other exercises.

---

> **📌 One virtual environment for the whole course**  
> We create a **single** `.venv` in the **main project folder (root)** and use it for **all levels** (Level 1, Level 2, and beyond). You will **not** create a new virtual environment for each level—you’ll activate this same one whenever you work in any level folder. That keeps the setup simple and consistent.

---

**Before you start**: Open a terminal in Codio. The terminal opens at the project root (e.g. `~/workspace`—the folder that contains `level1`, `level2`, and `.guides`). **Stay in this root folder** for Steps 1–3. Do not `cd` into `level1` yet.

#### Steps

1. **Create a Virtual Environment (in the project root)**
   
   In the terminal, make sure you're in the **main project folder** (run `pwd`; you should see a path that does **not** end in `level1`). Then check that Python 3.11 is installed:
   ```bash
   python3.11 -V
   ```
   Create the virtual environment and activate it:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```
   
   **What to expect**: Your command prompt should show `(.venv)` at the beginning, indicating the virtual environment is active. The `.venv` folder is now in the **project root** and will be reused for every level.

2. **Install Rasa Pro**
   
   With the virtual environment activated (still in the project root), run:
   ```bash
   pip install --no-cache-dir rasa-pro
   ```
   
   **What to expect**:
   - Installation will take 2–5 minutes
   - You'll see progress messages as packages are downloaded and installed
   - At the end, you should see "Successfully installed rasa-pro-x.x.x" along with a list of dependencies

3. **Verify Installation**
   
   Once installation completes, verify Rasa Pro is installed correctly:
   ```bash
   rasa --version
   ```
   
   **Expected output**: You should see version information like "Rasa 3.x.x" (no errors).
   
   **If you see an error**: The installation may not have completed successfully. Review any error messages from Step 1 and try installing again.

4. **Check Project Structure** *(After installation)*
   
   Go to the `level1` folder and confirm the bot structure is present:
   ```bash
   cd level1
   # Check that project folders exist
   ls -la domain/
   ls -la data/
   ```
   Confirm:
   - The `domain/` folder exists
   - The `data/` folder exists

   ```bash
   # Check that the following .yml files exist
   ls -la config.yml credentials.yml endpoints.yml
   ```

5. **Check Environment Variables**

   **Codio**: Credentials are pre-configured. To verify they're loaded, run (from `level1` or root):
   ```bash
   [ -n "$RASA_LICENSE" ] && echo "RASA_LICENSE is set" || echo "RASA_LICENSE is not set"
   [ -n "$OPENAI_API_KEY" ] && echo "OPENAI_API_KEY is set" || echo "OPENAI_API_KEY is not set"
   ```
   Both should report "is set". If not, ask your instructor.
   
   **Local setup**: The `.env` file should exist in your **level1** folder (same folder as `config.yml`). From `level1`, run **ls -la .env** to confirm. If it doesn't, create it using the instructions in section 0.1.

**✅ Success Criteria**: Once you can run `rasa --version` successfully and see version information, you're ready to move on. You can then run the assessment for this lab to confirm your setup. For later labs, remember: **activate the venv from the project root** (`source .venv/bin/activate`), then **cd** into the level folder you're working in (e.g. `cd level1`).
