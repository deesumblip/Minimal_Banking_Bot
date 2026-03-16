**Placement:** You completed Unit 4 (registering both actions in the domain) and Lab 6.1 (training). This check verifies that **both** your domain registration and your trained model are in place—so run it right after Lab 6.1.

---

### Lab 6.2: Verify Domain and Training

The assessment below runs the same domain checks as Lab 4.1, then confirms that a model file exists in `level2/models/` (i.e. you've run `python -m rasa train`). If you haven't trained yet, complete Lab 6.1 first.

Run the assessment when you're done.

{Check It!|assessment}(code-output-compare-1597644299)

---

#### Review in Inspector (optional)

After you pass the check, you can try your bot in the Inspector. **In the terminal** use the **virtual environment in the main folder** (project root); then go into `level2` and run the Level 2 bot from there.

1. **Go to the main folder** (the project root, one level *above* `level2`—the folder that contains `level1`, `level2`, and `.guides`). If you're inside `level2` or a subfolder, run `cd ..` (or `cd ../..` as needed) until you're in that main folder.
2. **Activate the virtual environment** (it lives in the main folder at the project root, e.g. `.venv`). Your prompt should show `(.venv)` when active.
   - **In Codio:** From the main folder, run `source .venv/bin/activate`
   - **Running locally (Windows PowerShell):** `.venv\Scripts\Activate.ps1`
   - **macOS / Linux:** `source .venv/bin/activate`
3. **Go into `level2`:** run `cd level2`.
4. **Train** (if needed): run `python -m rasa train`. Wait for the model to save.
5. **Start the Inspector:** Run `python -m rasa inspect --debug` and leave it running. Then open the Inspector:
   - **In Codio:** Click the **Rasa Inspect** tab on the top menu bar.
   - **Locally:** Open **http://localhost:5005** in your browser.

In the chat, try **"What are your hours?"** and **"What are your holiday hours?"** to confirm both actions and flows work.
