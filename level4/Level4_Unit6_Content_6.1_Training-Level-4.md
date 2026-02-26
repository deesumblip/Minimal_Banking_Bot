Training your Level 4 bot works the same way as Level 3: use the virtual environment in the **project root**, then navigate to the **level4** folder and run Rasa train.

## Steps

1. **Activate the virtual environment** in the main project folder (the one that contains `level1`, `level2`, `level3`, `level4`, and `.guides`). For example:
   - Codio/Linux: `source .venv/bin/activate`
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
2. **Navigate to level4:** `cd level4`
3. **Train:** `python -m rasa train`
4. **Verify:** A new `.tar.gz` model file appears in `level4/models/`

Rasa will read your domain (including the new slots and ask responses), your flows (including `transfer_money`), and your actions (including `action_process_transfer`). When training finishes without errors, you can run the assessment for **Lab 4.4** and then test the transfer flow in Inspector (Lab 4.5).

If you see errors about missing slots or responses, double-check your domain and flow files from Labs 4.1 and 4.3.
