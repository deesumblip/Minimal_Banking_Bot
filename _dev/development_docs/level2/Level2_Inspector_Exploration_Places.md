# Where to Explore "Modifications → Inspector Behavior" in Level 2

This note suggests **where in the Level 2 narrative** it’s useful for students to open Rasa Inspector and see how their changes affect the agent’s behavior.

---

## 1. **After Unit 4 / Lab 4.1 (Registering actions)**

**Modification so far:** Actions are registered in the domain; no flow yet for `holiday_hours` (unless the starter has one).

**Why it’s useful:**  
Students can train, open Inspector, and try:
- “What are your hours?” → Should work if the `hours` flow exists (example flow).
- “What are your holiday hours?” → Often won’t be handled yet (no `holiday_hours` flow), or may fall back to something generic.

**Learning:** Registration alone doesn’t make the agent answer new questions; you need a **flow** that uses the action. That motivates Unit 5.

**Suggested placement:** Optional short “Explore in Inspector” paragraph at the **end of Unit 4** (e.g. after 4.4) or start of **Unit 5.1**, with a one-line “try these two questions and notice…” and “In Unit 5 you’ll add the flow.”

---

## 2. **After Unit 5 / Lab 5.1 (Flows added)**

**Modification so far:** Both `hours` and `holiday_hours` flows exist and use the two actions.

**Why it’s useful:**  
Students train, open Inspector, and try:
- “What are your hours?” → `hours` flow, `action_bank_hours`.
- “What are your holiday hours?” → `holiday_hours` flow, `action_holiday_hours` (message varies by date).

**Learning:** They see that their YAML and flow changes **directly** change what the agent does in the UI. Good “sneak peek” before Unit 6 formalizes training and testing.

**Suggested placement:** Optional short “Preview in Inspector” at the **end of Unit 5** (e.g. after **5.1** and **Lab 5.1**): “Train and open Inspector; try both questions and see both flows trigger. Unit 6 will cover training and testing step by step.”

---

## 3. **Lab 6.2 (Training and Testing)** — main place

**Modification so far:** Everything is in place (actions, domain, flows); students are doing formal testing.

**Why it’s useful:**  
This is already the main “test in Inspector” moment. It’s the right place to **spell out** the link between modifications and Inspector:

- Which **flow** the LLM selected (e.g. `hours` vs `holiday_hours`).
- Which **action** ran (e.g. `action_bank_hours` vs `action_holiday_hours`).
- How the **message** varies (e.g. date-based for holiday hours).

**Suggested placement:** In **Lab 6.2**, add a sentence or two: when testing in Inspector, **observe** which flow and action are shown (e.g. in the debug/flow view) so you can see how your code and YAML changes map to behavior.

---

## 4. **Unit 7.1 (Complete agent walkthrough)**

**Modification:** None here; it’s a recap/walkthrough.

**Why it’s useful:**  
The walkthrough describes the same kind of conversation students can have in Inspector. A short line like “In Inspector you can run this same conversation and see which flow and action run at each step” ties the narrative to the tool.

**Suggested placement:** One sentence in **7.1** near the conversation example: e.g. “You can replay this in Inspector and see which flow and action run for each message.”

---

## Summary

| Place in narrative        | What students see in Inspector                         | Main takeaway                                      |
|---------------------------|--------------------------------------------------------|----------------------------------------------------|
| After Unit 4 (optional)   | Hours works; holiday hours often doesn’t (no flow)    | Need a flow that uses the action → Unit 5          |
| After Unit 5 (optional)   | Both questions work; both flows trigger                | My changes show up in the agent → Unit 6             |
| Lab 6.2                   | Which flow/action run; how messages vary               | Connect edits to observable behavior               |
| Unit 7.1                  | Walkthrough = what you’d see in Inspector              | Inspector is where you see the full picture        |

The **must-have** is **Lab 6.2** (already there; can add explicit “observe flow/action in Inspector”). The **after Unit 4** and **after Unit 5** checkpoints are **optional** and work well if you want students to “explore early” and see how each modification step changes Inspector behavior.
