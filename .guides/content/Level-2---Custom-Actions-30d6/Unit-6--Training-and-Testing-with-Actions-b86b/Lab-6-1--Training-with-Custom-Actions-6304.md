Training in Level 2 works the same as Level 1: `rasa train` reads `domain/` and `data/` and writes a packaged model to `models/`. The model learns your custom action names from the domain's `actions:` section. The Python code in `actions/` runs separately on the action server at runtime, so changes to `actions/*.py` do not require retraining. Changes to `domain/` or `data/` do.

#### Step 1: Go to the project root

Look at the terminal on the right. Go to the project root. It sits one level above `level2` and contains `level1`, `level2`, and `.guides`. Your terminal prompt should end with **`~/workspace$`** so you are in that root before you activate the venv and `cd level2`.

#### Step 2: Activate the virtual environment

Activate the virtual environment from the project root. Your prompt should show `(.venv)` when active.


```bash
source .venv/bin/activate
```


#### Step 3: Train from inside `level2`

From the project root, go into `level2` and run training with the following commands:

```bash
cd level2
python -m rasa train
```

`rasa train` loads flows from `data/` (including `hours.yml`, `holiday_hours.yml`, and your Level 1 flows), reads `domain/` (Level 1 responses plus the new `actions:` entries), and writes a `.tar.gz` model into `models/`.


#### Step 4: Verify the model file exists

Confirm that `level2/models/` now contains at least one new **`.tar.gz`** model file.

---

#### Run the assessment

Run the Check It! assessment below once training has finished without errors and `level2/models/` contains a `.tar.gz`.

{Check It!|assessment}(code-output-compare-1070925386)

Next, go to **Lab 6.2** to start Rasa Inspector and test both flows end-to-end.

---
