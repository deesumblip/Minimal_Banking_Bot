**Starting point:** Work in **`level4/`** (see **Unit 0.1**).

Before moving to Level 5, ensure you can:

- Explain the **full delta** in **Unit 0.2** (pipeline **`config.yml`** / **`endpoints.yml`** plus labs), not only domain and flow edits
- Add multiple slots to the domain and matching `utter_ask_*` responses (with **`rephrase: False`** on transfer asks)
- Create an action that reads multiple slots, caps **recipient** at **100** characters, handles placeholders, and sends the demo confirmation
- Create a flow with multiple `collect:` steps in order, then an `action:` step
- Explain why the order of `collect:` steps matters
- Train the Level 4 agent from the `level4` folder and run the completion check (and the **scripted transfer** in Inspector from Lab 5.2)
- Understand that **Level 4** extends the baseline agent and that **greet, hours, check_balance, …** still live in **`level4/`**

If you can do all of the above, you're ready for Level 5!
