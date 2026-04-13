**Starting point:** Work in **`level4/`** (see **Unit 0.1**).

## What you added in Level 4

You followed **Lab 0.1** (pipeline YAML), **Labs 2.1–4.1** (domain, action, flow), then **Labs 5.1–5.2** (train and verify). The **step-by-step lab list and deliverables table** live in **Unit 0.2** (sections 2–4) and on each lab page. Use those as the canonical checklist. This page only pulls out **ideas**.

## Key ideas

- **Multiple slots** let the agent remember several values in one conversation and use them together in one action.
- The **order of `collect:` steps** is the order the agent asks for values.
- **Naming** stays consistent: slot names and `utter_ask_<slot_name>` in the domain must match the flow and the action’s `get_slot(...)` calls.

At this point your assistant supports greet, help, contact, goodbye, hours, holiday hours, check_balance, and **transfer_money** (plus unchanged Level 1–3 paths as before).
