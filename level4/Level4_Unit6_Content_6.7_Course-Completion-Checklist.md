**Starting point:** Chapter 1.4 assumes you began with the **final banking agent at the end of Chapter 1.3** and extended it in **`level4/`** (see **`Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md`**).

Before moving to Level 5, ensure you can:

- Explain the **full delta** from Chapter 1.3 end → Chapter 1.4 end: **`level4/config.yml`** (**`CompactLLMCommandGenerator`**, **`flow_retrieval`**) and **`level4/endpoints.yml`** (**`model_groups`** / temperature), not only domain and labs (**Unit 0.2**)
- Add multiple slots to the domain and matching `utter_ask_*` responses (with **`rephrase: False`** on transfer asks)
- Create an action that reads multiple slots, caps **recipient** at **100** characters, handles placeholders, and sends the demo confirmation
- Create a flow with multiple `collect:` steps in order, then an `action:` step
- Explain why the order of `collect:` steps matters
- Train the Level 4 agent from the `level4` folder and run the completion check (and the **scripted transfer** in Inspector from Lab 5.2)
- Understand that Level 4 builds on Level 3 and that all Level 3 content remains in `level4/`

If you can do all of the above, you're ready for Level 5!
