# Lab 6.1: Training and Testing with Slots

Your goal is to train your Level 3 bot (with slots) and verify it works.

## Part 1: In Codio

1. **Virtual environment.** In the terminal (it opens at `~/workspace`), run `source .venv/bin/activate`. The prompt should show `(.venv)`.
2. **Navigate to level3.** Run `cd level3`. Confirm with `pwd` (path should end in `level3`).
3. **Rasa.** Run `python -m rasa --version`. If you see an error, ensure the venv is activated and Rasa Pro is installed (from Lab 0.1).
4. **Train.** From `level3` with venv active, run `python -m rasa train`. Wait for "Successfully saved model" (about 1–3 minutes).
5. **Verify.** The terminal shows "Successfully saved model to 'models/...'". In the file tree, `level3/models/` should contain a new `.tar.gz` file.

**Common errors.** If you get slot or utter_ask errors, check the domain and flow. If you get "No module 'rasa'", activate the venv from the project root. If RASA_LICENSE or OPENAI_API_KEY is not set, check Lab 0.1 or ask your instructor.

Run the assessment when done.

## Part 2: Running locally

Follow the same logic as Part 1, but use your own terminal and OS-specific commands.

1. **Open a terminal** (PowerShell, Command Prompt, or Terminal.app / your Linux terminal).
2. **Go to the main project folder** (the one that contains `level1`, `level2`, `level3`, and `.guides`). For example `cd C:\Users\You\Minimal_Banking_Bot` or `cd ~/Minimal_Banking_Bot`.
3. **Activate the virtual environment.** The `.venv` folder is in the main project folder. On Windows (PowerShell) use `.venv\Scripts\Activate.ps1`. On Windows (Command Prompt) use `.venv\Scripts\activate.bat`. On macOS or Linux use `source .venv/bin/activate`. Your prompt should show `(.venv)`.
4. **Navigate to level3.** Go to the `level3` folder with `cd level3` (the one that contains `config.yml`, `domain/`, and `data/`).
5. **Ensure `.env` exists** in the `level3` folder with `RASA_LICENSE` and `OPENAI_API_KEY`. See Lab 0.1 or your instructor if you need these.
6. **Train.** With venv active and from the `level3` folder, run `python -m rasa train`. Wait for "Successfully saved model".
7. **Verify.** A new `.tar.gz` file appears in `level3/models/`.

You're done when training completes with no errors and a new model file appears in `models/`.

---

## Check Your Knowledge

**1. From which folder should you run `python -m rasa train`?**

a) Project root (the folder with `level1`, `level2`, `level3`)  
b) `level3` (the folder with `config.yml`, `domain/`, `data/`)  
c) `level3/models`  
d) `level3/data`  

**2. How do you confirm that training succeeded?**

a) The terminal shows "Successfully saved model to 'models/...'"  
b) A new `.tar.gz` file appears in `level3/models/`  
c) Both a and b  
d) The Rasa Inspect tab opens automatically  

**3. If you get "No module 'rasa'", what is the most likely fix?**

a) Run `pip install rasa-pro`  
b) Activate the virtual environment from the project root, then `cd level3`  
c) Check that `config.yml` exists  
d) Reboot Codio  

---

### Answer Key

| Q | Answer | Brief explanation |
|---|--------|-------------------|
| 1 | **b** | You must run `rasa train` from the `level3` folder where `config.yml` and the domain/data live. |
| 2 | **c** | Both the terminal message and the new model file in `models/` confirm success. |
| 3 | **b** | Rasa is installed in the venv; activate it from the project root, then navigate to `level3`. |
