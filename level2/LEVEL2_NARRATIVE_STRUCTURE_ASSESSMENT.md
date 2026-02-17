# Level 2: Narrative Structure Assessment

Assessment of the **Level2_*** content and lab files read in sequence from start to finish. Intended order: **Unit 0 → 1 → 2 → [Lab 2.1] → Unit 3 → Lab 3.1 → Unit 4 → Lab 4.1 → Unit 5 → Lab 5.1 → Unit 6 → Lab 6.1 → Unit 7 → Unit 8.**

---

## 1. Overall Arc

| Phase | Content | Narrative role |
|-------|---------|-----------------|
| **Setup** | Unit 0 (0.1, 0.2) | Recap Level 1; set expectation: "you'll build action_holiday_hours in Unit 3 / Lab 3.1, then register and add flow in Labs 4.1 and 5.1." |
| **Concepts** | Unit 1 (1.1–1.3), Unit 2 (2.1–2.2) | What actions are; how they work; full example `action_bank_hours`. No hands-on yet. |
| **Explore (optional)** | Lab 2.1 | Explore `actions/` and `action_bank_hours.py`; MC/FIB. Fits after Unit 2. |
| **Create** | Unit 3 (3.1, 3.2), Lab 3.1 | "Create your own action" (action_holiday_hours); execution model. Lab 3.1 = build the file. |
| **Wire in** | Unit 4 + Lab 4.1, Unit 5 + Lab 5.1 | Register both actions; create hours.yml + holiday_hours.yml. |
| **Run** | Unit 6 + Lab 6.1 | Train and test; verify both flows. |
| **Integrate** | Unit 7 (7.1–7.3) | Walkthrough (including holiday_hours); summary; best practices. |
| **Close** | Unit 8 (8.1–8.5) | Knowledge check; what you've learned; limitations; Level 3 preview; checklist. |

**Verdict:** The arc is clear: **recap → concepts → create your action → register it → add a flow → train/test → integrate → review.** The "example vs. your action" thread (action_bank_hours vs. action_holiday_hours) is consistent.

---

## 2. Forward and Backward References

### Strong handoffs
- **0.2** → "In Unit 3 / Lab 3.1 you'll create … action_holiday_hours; Labs 4.1 and 5.1 … register and add flow."
- **1.3** → "In Unit 2 you'll see the full action_bank_hours…"
- **3.1** → Names action_holiday_hours, Lab 3.1, and "Later (Labs 4.1 and 5.1) you'll register it and add a flow"; "Next: Lab 3.1 … then Unit 4 / Lab 4.1 … Unit 5 / Lab 5.1."
- **4.2, 4.3, 4.4** → "the action you created in Lab 3.1", "action_holiday_hours."
- **Lab 5.1** → "the action you created in Lab 3.1", "your flow holiday_hours.yml"; "In Unit 6 you'll train and test both."
- **7.1, 7.2** → "the action you created in Lab 3.1", "your flow (holiday_hours)."
- **8.2, 8.5** → "you built action_holiday_hours", "Lab 3.1", "holiday_hours.yml."

### Gaps (weaker or missing links)
- **Unit 2.2 (end):** No forward pointer. A single line would help: e.g. *"In Unit 3 you'll use this structure to create your own action (Lab 3.1)."*
- **Unit 3.2 (end):** No "Next." Reader might not be sure to do Lab 3.1 next. Add: *"Next: Complete Lab 3.1 to create action_holiday_hours.py."*
- **Unit 4.1 (start):** Jumps straight to "register actions" without reminding that they just created an action in Lab 3.1. Add: *"You created action_holiday_hours in Lab 3.1. For Rasa to use it (and the example action), both must be registered in the domain."*
- **Unit 5.1 (start):** Doesn't assume "you've registered your action in Lab 4.1." Optional: *"Now that your actions are registered (Lab 4.1), you need flows that use them—the example hours flow and your holiday_hours flow."*
- **Unit 6.1 ("What Happens During Training"):** Only mentions `hours.yml` and `action_bank_hours`. For consistency with the rest of the narrative, add that training also picks up `holiday_hours.yml` and `action_holiday_hours` (e.g. in the bullet list).

### Backward references
- References to "Level 1," "action_bank_hours," "the pattern you've seen," and "Lab 3.1" are consistent. No broken "as you saw in Unit X" that assume old file names or order.

**Verdict:** The main story (0 → 3.1 → 4.1 → 5.1 → 6 → 7 → 8) is well connected. The gaps above are small and mostly about one-line bridges or reminders.

---

## 3. Consistency of Terminology and Voice

- **"You" / "your":** Used consistently (your action, your flow, you created, you'll register).
- **"Example" vs "yours":** Clear in 0.2, 3.1, 4.4, Lab 5.1, 7.2 (action_bank_hours / hours = example; action_holiday_hours / holiday_hours = yours).
- **Lab and unit names:** "Lab 3.1," "Unit 4," "Lab 4.1," etc. used consistently.
- **File/action names:** action_holiday_hours, holiday_hours.yml, action_bank_hours, hours.yml used consistently.

**Verdict:** Terminology and voice are consistent across the Level2_ content.

---

## 4. Lab 2.1 and Other Side Content

- **Lab 2.1** ("Exploring the Actions Folder"): Placement is stated as "right after the section on the Action Class Structure" (i.e. after Unit 2). It is not in the Course Outline's main flow diagram (Unit 0 → 1 → 2 → 3 → …). So either:
  - Treat it as optional and add a short note in the outline (e.g. "Optional: Lab 2.1 – Explore actions folder after Unit 2"), or
  - Insert it explicitly in the diagram: Unit 2 → Lab 2.1 → Unit 3.
- **Level2_AdditionalResources_Content.md, Level2_Troubleshooting_Content.md:** Supporting material; not part of the linear narrative. Fine as-is.
- **Level2_Lab1.1_Assessment_OLD.md:** Name suggests deprecated; no impact on current narrative if unused.

**Verdict:** The core narrative doesn't depend on Lab 2.1. Only the outline/flow diagram needs a clear decision: optional vs. explicit step.

---

## 5. Redundancy and Pacing

- **Repetition of "action you created in Lab 3.1" / "action_holiday_hours":** Used in 4.2, 4.3, 4.4, Lab 5.1, 7.1, 7.2, 8.2, 8.5. This reinforces the thread without feeling heavy.
- **Recap of structure (imports, name(), run(), return []):** In Unit 1.3, 2.1, 3.1. Appropriate for learning; 3.1 is the one that ties it to "your" action.
- **Training/testing:** Unit 6.1 and 6.3 describe training and testing; 7.1 shows a full conversation. No unnecessary duplication.

**Verdict:** Redundancy is controlled and supports the narrative. Pacing (concepts → one hands-on create → register → flow → train → integrate → review) is good.

---

## 6. Summary Table: Narrative Fit

| Segment | Fits arc? | Forward/back references | Suggested tweaks |
|---------|-----------|--------------------------|-------------------|
| Unit 0 | ✓ | 0.2 sets full journey | — |
| Unit 1 | ✓ | 1.3 → Unit 2 | — |
| Unit 2 | ✓ | — | Add one-line forward to Unit 3 / Lab 3.1 at end of 2.2 |
| Lab 2.1 | ✓ | "After Action Class Structure" | Clarify in outline: optional or explicit step |
| Unit 3 | ✓ | 3.1 → Lab 3.1, 4.1, 5.1 | Add "Next" at end of 3.2 |
| Lab 3.1 | ✓ | "Follows Unit 3" | — |
| Unit 4 | ✓ | "action you created in Lab 3.1" | Add one-line bridge at start of 4.1 |
| Lab 4.1 | ✓ | "register both …" | — |
| Unit 5 | ✓ | "action you created in Lab 3.1", → Unit 6 | Optional bridge at 5.1 |
| Lab 5.1 | ✓ | "example flow" + "your flow" | — |
| Unit 6 | ✓ | 6.3 tests both flows | 6.1: mention holiday_hours.yml / action_holiday_hours in training |
| Lab 6.1 | ✓ | — | — |
| Unit 7 | ✓ | 7.1 includes holiday_hours turn; 7.2 lists both | — |
| Unit 8 | ✓ | 8.2, 8.5 reference Lab 3.1 and your action | — |

---

## 7. Conclusion

The Level2_ narrative is **coherent and consistent** from start to finish: one clear path (recap → concepts → create your action → register → add flow → train/test → integrate → review), with a single "your action" story (action_holiday_hours, created in Lab 3.1, registered in 4.1, used in holiday_hours.yml in 5.1).

**Recommended small edits:**
1. **Unit 2.2** – Add one sentence at the end pointing to Unit 3 / Lab 3.1.
2. **Unit 3.2** – Add "Next: Complete Lab 3.1 to create action_holiday_hours.py."
3. **Unit 4.1** – Add one sentence at the start: you created action_holiday_hours in Lab 3.1; register it (and the example) in the domain.
4. **Unit 6.1** – In "What Happens During Training," mention holiday_hours.yml and action_holiday_hours alongside hours/action_bank_hours.
5. **Course Outline** – Clarify Lab 2.1 (optional vs. explicit step after Unit 2).

Optional: **Unit 5.1** – Short bridge that "your actions are registered (Lab 4.1), so now you need flows for them."
