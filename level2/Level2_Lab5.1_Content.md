# Lab 5.1: Using Actions in Flows

## Guide Content (For Students)

**Placement**: This lab follows Unit 5: Using Actions in Flows.

---

### Your Task

1. **Example flow** – Ensure the `hours` flow exists in `data/basics/hours.yml` and uses `action_bank_hours` (your starter may already include this).
2. **Your flow** – Create `data/basics/holiday_hours.yml` with a flow that uses **action_holiday_hours** (the action you created in Lab 3.1). The flow should have:
   - A flow id (e.g. `holiday_hours`)
   - `name:` and `description:` so the LLM can match questions about holiday hours
   - `steps:` with `- action: action_holiday_hours`

---

### Verification

Before submitting, confirm:

- `hours.yml` has the `hours` flow and calls `action_bank_hours`
- `holiday_hours.yml` exists, has a flow (e.g. `holiday_hours`), and calls `action_holiday_hours`

Run the assessment when you're done.

#### Review in Inspector

Train your bot, then open the Rasa Inspector GUI (see Unit 6.3). Use the questions from Unit 5.2 (hours, holiday hours, hello) and check that the bot's replies and the triggered flow/action match. If a question doesn't trigger the right flow, check the flow's `description` and that you re-trained after adding or changing flows.
