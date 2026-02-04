# Level 4 Codio Implementation Playbook

**Purpose**: Implement Level 4 (“Multiple Slots”) inside Codio by extending the slot framework from Level 3 to cover multi-slot forms and transfer actions, while keeping `level4/CODIO_IMPLEMENTATION_GUIDE.md` untouched.

---

## 1. Reference Materials

- Level 4 curriculum: `level4/CODIO_IMPLEMENTATION_GUIDE.md`
- Codio Guides authoring: [Codio Guides documentation](https://www.codio.com/docs/guides)
- Auto-grading/assessments: [Codio Auto-Grading overview](https://www.codio.com/features/auto-grading), [Global Assessments Library](https://www.codio.com/blog/codio-launches-global-assessments-library)
- Virtual Coach: [Virtual Coach settings](https://docs.codio.com/instructors/setupcourses/assignment-settings/virtual-coach.html)
- Code Playback: [Code Playback docs](https://docs.codio.com/common/tools/code-playback.html)
- Analytics & Behavior Insights: [Learning Insights](https://www.codio.com/features/learning-insights), [Behavior Insights config](https://docs.codio.com/instructors/teaching/behaviorinsights.html)

---

## 2. Authoring the Codio Guide

1. Copy the Level 3 Guide project to preserve layouts and navigation, then replace content with the Level 4 modules (recap + multiple-slot lessons).  
2. Configure each practical section to open all relevant files simultaneously: `domain/basics.yml` (new slots + `utter_ask_*` prompts), `data/basics/transfer_money.yml`, `actions/action_process_transfer.py`.  
3. Use tabbed callouts to compare single-slot vs. multi-slot flows; embed diagrams showing slot collection order.  
4. Highlight validation logic inside actions (e.g., ensuring amount > 0) to prepare students for advanced checks.

---

## 3. Designing Assessments & Auto-Graders

| Goal | Action Items | Reference |
| --- | --- | --- |
| Slot presence & ordering | Validate that `amount`, `recipient`, and `account_from` slots exist with correct prompts and `collect` order. Diff-friendly messages help students fix specific slots. | [Auto-grading overview](https://www.codio.com/features/auto-grading) |
| Flow integrity | Run scripted `rasa inspect` conversation that walks through the transfer flow, verifying each prompt appears only once and in the right order. | same |
| Action correctness | Execute Python test harness that calls `action_process_transfer` with a mocked tracker (slots filled) and ensures the response summarises all slot values. | same |
| Branching checks | Add negative test (missing slot) to confirm the flow re-prompts; auto-grader should detect if `not_set` fallback is missing. | same |
| Concept assessments | MCQs about collecting multiple slots vs. separate flows; short answers on when to validate slot combinations. | [Assessments library](https://www.codio.com/blog/codio-launches-global-assessments-library) |

Keep grading scripts modular so later levels (tool calling) can re-use their slot validators.

---

## 4. Configuring Codio Coach

- Emphasize sequencing hints (“After collecting amount, verify `next: collect recipient` is present”).  
- Include troubleshooting for repeated prompts or missing slot definitions.  
- Offer reminders to re-run `rasa train` after editing multiple files.  
- Monitor Coach logs for confusion around `collect:` arrays vs. `slot_was_set` events and update FAQs accordingly.

---

## 5. Instrumenting Code Playback

Capture edits across `domain/basics.yml`, `data/basics/transfer_money.yml`, and `actions/action_process_transfer.py`. Multi-slot flows involve repetitive YAML edits; Playback helps instructors confirm students built them incrementally.

---

## 6. Analytics, Behavior Insights, LMS

- Expect longer time-on-task; adjust Behavior Insight thresholds upward (~60–75 minutes) so genuine effort isn’t flagged.  
- Track how many attempts students need to pass the flow test—use analytics to refine instructions if failure rate is high.  
- In the LMS, weight the Level 4 lab slightly higher because it introduces multi-slot complexity.

---

## 7. Recommended Timeline Slice (Two-Week Program)

Level 4 work should land immediately after Level 3 sign-off to keep momentum while still fitting the overall two-week window.

| Day | Focus | Deliverables |
| --- | --- | --- |
| Week 2, Day 2 (AM) | Guide migration + flow visuals | Port modules, embed multi-slot diagrams, configure auto-open panes for transfer files. |
| Week 2, Day 2 (PM) | Auto-graders + Coach + instrumentation | Implement multi-slot graders, enable Coach hints for sequencing issues, verify Code Playback/analytics capture all files, run LMS sync test. |

---

## 8. Handoff Checklist

- [ ] Guides highlight differences between single-slot and multi-slot flows.  
- [ ] Graders validate slot definitions, flow ordering, and action output.  
- [ ] Virtual Coach handles sequencing and validation errors.  
- [ ] Playback shows edits to transfer flow + action; QA reviewed.  
- [ ] Analytics & Behavior thresholds tuned to longer sessions; LMS weights updated.  
- [ ] Instructor notes explain how to diagnose repeated prompts and slot mis-ordering.
