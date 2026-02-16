# Lab 0.1: Create Virtual Environment and Install Rasa Pro

**Objective**: Create a virtual environment, install Rasa Pro in it, and verify the installation is successful.

**Important**: This is your first step! You must create a virtual environment and install Rasa Pro before you can proceed with any other exercises.

**Before you start**: Open a terminal in Codio. Run `cd level1` so you are in the `level1` folder. All commands in this lab should be run from there.

#### Steps

1. **Create a Virtual Environment**
   
   In the terminal, first check that Python 3.11 is installed correctly:
   ```bash
   python3.11 -V
   ```
   Then type:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```
   
   **What to expect**: Your command prompt should show `(.venv)` at the beginning, indicating the virtual environment is active.

2. **Install Rasa Pro**
   
   With the virtual environment activated, run:
   ```bash
   pip install --no-cache-dir rasa-pro
   ```
   
   **What to expect**:
   - Installation will take 2-5 minutes
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
   ```bash
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

   **Codio**: Credentials are pre-configured. To verify they're loaded, run:
   ```bash
   [ -n "$RASA_LICENSE" ] && echo "RASA_LICENSE is set" || echo "RASA_LICENSE is not set"
   [ -n "$OPENAI_API_KEY" ] && echo "OPENAI_API_KEY is set" || echo "OPENAI_API_KEY is not set"
   ```
   Both should report "is set". If not, ask your instructor.
   
   **Local setup**: The .env file should exist in your project root. Run **ls -la .env** to confirm. If it doesn't, create it using the instructions in section 0.1.

**✅ Success Criteria**: Once you can run `rasa --version` successfully and see version information, you're ready to move on to the next exercises. You can then run the assessment for this lab to confirm your setup.
