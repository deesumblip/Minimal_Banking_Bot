Training in Level 2 is the same idea as Level 1: you run `rasa train` and Rasa writes a packaged model under **`models/`**. What changes is that Rasa now **also reads your custom actions** under **`actions/`** and folds them together with **`domain/`** and **`data/`**—so the model knows about `action_bank_hours` and `action_holiday_hours`, not only `utter_*` responses.

You should already have finished **Labs 3.1–5.1**: both actions appear in the domain, **`hours.yml`** uses `action_bank_hours`, and **`holiday_hours.yml`** uses `action_holiday_hours`.

#### Step 1: Go to the main folder (project root)

Go to the project root (one level *above* `level2`—the folder that contains `level1`, `level2`, and `.guides`).

#### Step 2: Activate the virtual environment

Activate the virtual environment from the project root (e.g. `.venv`). Your prompt should show `(.venv)` when active.

- **In Codio (Linux):**

```bash
source .venv/bin/activate
```

- **Running locally:**
  - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
  - **Windows (Command Prompt):** `.venv\Scripts\activate.bat`
  - **macOS / Linux:** `source .venv/bin/activate`

#### Step 3: Train from inside `level2`

From the project root, go into `level2` and run training:

```bash
cd level2
python -m rasa train
```

When that command runs, Rasa loads flows from **`data/`** (including `hours.yml`, `holiday_hours.yml`, and your unchanged Level 1 flows). It loads **`domain/`** (Level 1 responses plus every entry under **`actions:`**). It validates that registered actions exist under **`actions/`** and that each action’s `name()` matches the domain exactly. It then writes a **`.tar.gz`** model into **`models/`**.

#### Step 4: Verify the model file exists

Confirm that `level2/models/` now contains at least one new **`.tar.gz`** model file.

---

#### Run the Lab 6.1 assessment

Run the Check It! below once training has finished without errors and `level2/models/` contains a `.tar.gz`.

{Check It!|assessment}(code-output-compare-1070925386)

Next, go to **Lab 6.2** to start Rasa Inspector and test both flows end-to-end.
