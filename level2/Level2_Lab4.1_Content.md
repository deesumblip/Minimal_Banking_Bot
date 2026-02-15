# Lab 4.1: Registering Actions in the Domain

## Guide Content (For Students)

**Placement**: This lab follows Unit 4: Registering Actions in the Domain.

---

### Your Task

Add an `actions:` section to `domain/basics.yml` (if it isn't already there) and register **both**:

- **action_bank_hours** – the example action you studied in the units  
- **action_holiday_hours** – the action you created in Lab 3.1  

Each action must appear as a list item under `actions:` (e.g. `- action_bank_hours`).

---

### Verification

Before submitting, confirm:

- The file `domain/basics.yml` has an `actions:` section  
- Both `action_bank_hours` and `action_holiday_hours` are listed  
- YAML is valid (correct indentation and dashes)  

Run the assessment when you're done.

---

#### Review in Inspector (optional)

After the assessment, train and open the Rasa Inspector GUI (see Unit 6.3). In the chat, try **"What are your hours?"** (should work if the `hours` flow exists) and **"What are your holiday hours?"** (likely not yet—you'll add that flow in Unit 5).
