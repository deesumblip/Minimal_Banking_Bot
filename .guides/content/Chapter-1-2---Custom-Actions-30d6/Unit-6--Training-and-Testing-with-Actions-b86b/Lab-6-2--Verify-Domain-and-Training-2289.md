**Placement:** You completed Unit 4 (registering both actions in the domain) and Lab 6.1 (training). This check verifies that **both** your domain registration and your trained model are in place—so run it right after Lab 6.1.

---

### Lab 6.2: Verify Domain and Training

The assessment below runs the same domain checks as Lab 4.1, then confirms that a model file exists in `level2/models/` (i.e. you've run `python -m rasa train`). If you haven't trained yet, complete Lab 6.1 first.

**In the terminal, do the following:**

1. Activate the virtual environment and go to `level2`:
   ```bash
   source .venv/bin/activate
   cd level2
   ```
   You should see a prompt like `(.venv) codio@...:~/workspace/level2$`.

2. **Before using Check It! in Codio**, start the Inspector so you can verify your bot:
   ```bash
   python -m rasa inspect --debug
   ```
   Leave it running (or run it whenever you want to test in the Inspector). When you're ready, **use Check It!** below (Codio).

{Check It!|assessment}(code-output-compare-1597644299)

---

#### Review in Inspector (optional)

1. **Start the Inspector:** Run `python -m rasa inspect --debug` and leave it running. Then open the Inspector:
   - **In Codio:** Click the **Rasa Inspect** tab on the top menu bar.
   - **Locally:** Open **http://localhost:5005** in your browser.

In the chat, try **"What are your hours?"** and **"What are your holiday hours?"** to confirm both actions and flows work.
