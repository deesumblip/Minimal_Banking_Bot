# Level 3 Codio Implementation Playbook

**Purpose**: Deploy Level 3 (“Slot Collection”) to Codio, layering memory concepts (slots, slot prompts, slot-aware actions) on top of the existing Level 1–2 infrastructure without modifying `level3/CODIO_IMPLEMENTATION_GUIDE.md`.

---

## 1. Reference Materials

- Level 3 curriculum: `level3/CODIO_IMPLEMENTATION_GUIDE.md`
- Codio Guides: [Codio Guides documentation](https://www.codio.com/docs/guides)
- Assessments/auto-grading: [Codio Auto-Grading overview](https://www.codio.com/features/auto-grading), [Global Assessments Library](https://www.codio.com/blog/codio-launches-global-assessments-library)
- Virtual Coach: [Virtual Coach settings](https://docs.codio.com/instructors/setupcourses/assignment-settings/virtual-coach.html)
- Code Playback: [Code Playback docs](https://docs.codio.com/common/tools/code-playback.html)
- Analytics & Behavior Insights: [Learning Insights](https://www.codio.com/features/learning-insights), [Behavior Insights config](https://docs.codio.com/instructors/teaching/behaviorinsights.html)

---

## 2. Authoring the Codio Guide

1. Duplicate the Level 2 Guide project into Level 3 so navigation, tabs, and layout settings persist.  
2. Replace content with Module 0 recap + Modules 1–8 focused on slots (definitions, slot types, collecting, reading).  
3. Configure sections to auto-open: `domain/basics.yml` (slots block + new `utter_ask_*` responses), `data/basics/check_balance.yml`, and `actions/action_check_balance_simple.py`.  
4. Include inline callouts explaining how `collect:` steps work and how slot prompts map to `utter_ask_*` responses.

---

## 3. Designing Assessments & Auto-Graders

| Goal | Action Items | Reference |
| --- | --- | --- |
| Validate slot definitions | Parse `domain/basics.yml` to ensure `slots:` exists with `account` (type `text`, `influence_conversation: false`, etc.). Provide precise error output. | [Auto-grading overview](https://www.codio.com/features/auto-grading) |
| Check slot prompts | Ensure `utter_ask_account` is present with required copy. Bonus: allow regex for phrasing but ensure placeholders exist. | same |
| Flow behavior | Run `rasa inspect` scenario: user says “Check balance”, verify the bot asks for account, stores slot, and action responds with account number. Compare transcripts to expected JSON. | same |
| Action logic | Execute Python snippet importing `action_check_balance_simple` to confirm `tracker.get_slot("account")` usage and formatted response string. | same |
| Concept checks | MCQs about slot types, `collect:` semantics, and difference between slot prompts vs. responses. | [Assessments library](https://www.codio.com/blog/codio-launches-global-assessments-library) |

Graders should fail fast when YAML indentation or slot naming is incorrect to save student time.

---

## 4. Configuring Codio Coach

- **Summarize Prompt**: Remind students to add the slot definition, prompt response, flow `collect` step, and action usage.  
- **Error Augmentation**: Map common Rasa errors (“Slot account is not defined in domain”) to friendly explanations.  
- **Next Steps**: Suggest verifying `rasa data validate` output or checking if `utter_ask_*` naming matches the slot.  
- Use Coach logs to identify whether students forget to re-run `rasa train` after slot changes.

---

## 5. Instrumenting Code Playback

Track: `domain/basics.yml` (slots + responses), `data/basics/check_balance.yml`, `actions/action_check_balance_simple.py`. Playback will help verify that learners typed the `collect:` block themselves instead of pasting large chunks.

---

## 6. Analytics, Behavior Insights, LMS

- Monitor time spent on the slot-collection lab; expect longer durations than Level 2. Flag extremes for instructor follow-up.  
- Update Behavior Insights thresholds to allow slightly higher debugging ratios (since slot wiring is error-prone).  
- Align LMS grading so the Level 3 lab weight reflects its higher difficulty.

---

## 7. Recommended Timeline Slice (Two-Week Program)

Level 3 can start as soon as Level 2 assets land, overlapping slightly with instrumentation work.

| Day | Focus | Deliverables |
| --- | --- | --- |
| Week 1, Day 5 | Guide migration + slot visuals | Port Level 3 content, set auto-open panes for slot files, add diagrams explaining slot lifecycle. |
| Week 2, Day 1 | Auto-graders + Coach + playback | Implement slot-aware graders, enable Coach hints for slots, confirm playback + analytics capture slot edits, run LMS smoke test for this assignment. |

---

## 8. Handoff Checklist

- [ ] Guides updated with slot walkthroughs and inline reminders.  
- [ ] Graders cover slot definition, prompt responses, flows, and action output.  
- [ ] Coach knowledge base includes slot-specific troubleshooting.  
- [ ] Playback shows edits to slot blocks + actions; QA reviewed sample sessions.  
- [ ] Analytics/Behavior thresholds tuned; LMS grade weight updated.  
- [ ] Instructor cheat sheet explains how to spot missing slots quickly (e.g., run `rasa data validate`).
