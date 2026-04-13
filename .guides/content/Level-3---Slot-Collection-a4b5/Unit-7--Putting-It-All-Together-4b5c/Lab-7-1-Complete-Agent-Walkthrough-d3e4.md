Your goal is to see how Level 1, 2, and 3 pieces work together in **one** Inspector session.

**Prerequisites.** Trained model under **`level3/models/`**, Inspector available (**Lab 6.2**).

---

## Steps

1. **Start Inspector** if it is not running. From **`level3`** with venv active:

 ```bash
   mkdir -p logs
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

 Open the **Rasa Inspect** tab in Codio, or **http://localhost:5005** (or **`.../inspect.html`**) locally.

2. **Run through the scenarios** in order:
 - Let **session start** run so the agent greets you.
 - Say you want to check your balance. When the **`account`** slot is empty, the agent should ask for it. Provide **1234** and confirm you get a balance reply driven by your action.
 - Ask for your balance again without giving a new account number. The agent should **not** re-ask. The slot should still hold **1234**.
 - Ask something that hits a **Level 2** path, for example bank hours, and a simple **Level 1** greeting.

3. **Observe.** Use the debug or flow panel to see which flow ran and how **`account`** is set and reused.

You are done when you have seen **collection**, **persistence**, and **Level 1 / 2** flows in one session. This lab has no separate graded Check It! beyond the knowledge questions below.

---

## Check Your Knowledge

{Check It!|assessment}(multiple-choice-3020000001)

{Check It!|assessment}(multiple-choice-3020000002)

{Check It!|assessment}(multiple-choice-3020000003)
