# Level 5 Codio Implementation Playbook

**Purpose**: Launch Level 5 (“Tool Calling”) inside Codio, extending the prior action/slot foundations to cover dynamic tool selection, `tools/` packages, and LLM tool registration—without modifying `level5/CODIO_IMPLEMENTATION_GUIDE.md`.

---

## 1. Reference Materials

- Level 5 curriculum: `level5/CODIO_IMPLEMENTATION_GUIDE.md`
- Codio Guides authoring: [Codio Guides documentation](https://www.codio.com/docs/guides)
- Auto-grading/assessments: [Codio Auto-Grading overview](https://www.codio.com/features/auto-grading), [Global Assessments Library](https://www.codio.com/blog/codio-launches-global-assessments-library)
- Virtual Coach: [Virtual Coach settings](https://docs.codio.com/instructors/setupcourses/assignment-settings/virtual-coach.html)
- Code Playback: [Code Playback docs](https://www.codio.com/common/tools/code-playback.html)
- Analytics & Behavior Insights: [Learning Insights](https://www.codio.com/features/learning-insights), [Behavior Insights config](https://docs.codio.com/instructors/teaching/behaviorinsights.html)

---

## 2. Authoring the Codio Guide

1. Clone the Level 4 Guide layout, then import Level 5 units (recap + tool calling labs).  
2. Configure sections to open `tools/__init__.py`, `tools/banking_tools.py`, `actions/action_process_transfer_with_tools.py`, `endpoints.yml`, and `data/basics/transfer_money_tools.yml`.  
3. Add callouts explaining the difference between explicit flows vs. LLM-driven tool selection. Embed diagrams showing how CALM selects tools.  
4. Provide inline instructions for enabling tool logging so students can inspect when the LLM calls each tool.

---

## 3. Designing Assessments & Auto-Graders

| Goal | Action Items | Reference |
| --- | --- | --- |
| Tool registration | Write grader to confirm `endpoints.yml` (or appropriate config) includes `tools:` block referencing `tools.banking_tools`. | [Auto-grading overview](https://www.codio.com/features/auto-grading) |
| Tool schema validation | Parse `tools/banking_tools.py` to ensure each tool has name, description, parameter schema, and returns expected JSON. Static analysis (AST) can catch missing decorators. | same |
| Conversation replay | Script `rasa inspect` conversation where the LLM must call `check_balance_tool` then `process_transfer_tool`. Use Inspector logs to verify both tool calls executed. | same |
| Error handling | Add negative tests ensuring the bot surfaces graceful errors when a tool raises an exception. | same |
| Concept assessments | Quizzes comparing actions vs. tools, best practices for tool descriptions, and when to prefer tool calling. | [Assessments library](https://www.codio.com/blog/codio-launches-global-assessments-library) |

Keep graders lightweight but deterministic—parse logs or JSON transcripts rather than free-form output.

---

## 4. Configuring Codio Coach

- **Summarize Prompt**: remind students to update `tools/`, register in `endpoints.yml`, and verify flows referencing tool-enabled actions.  
- **Error Augmentation**: translate tool errors (“Tool not registered” or `ActionException`) into actionable steps (e.g., re-run `rasa train`, check `tools` key).  
- **Next Steps**: suggest running `python -m rasa inspect --debug` to confirm tool invocation order.  
- Feed recurring tool-misconfiguration issues back into the Guide’s troubleshooting appendix.

---

## 5. Instrumenting Code Playback

Record edits across `tools/`, `actions/action_process_transfer_with_tools.py`, `data/basics/transfer_money_tools.yml`, and `endpoints.yml`. Playback will help instructors confirm students didn’t paste wholesale tool dictionaries and actually iterated on schemas.

---

## 6. Analytics, Behavior Insights, LMS

- Track the ratio of successful tool invocations during graded runs; high failure rates indicate instructions need clarification.  
- Behavior Insights should flag extremely short sessions (possible copy/paste of tool code) and zero-debug runs (unlikely at this level).  
- Adjust LMS weighting so Level 5 contributes the final portion of the cumulative grade, rewarding students for mastering tool orchestration.

---

## 7. Recommended Timeline Slice (Two-Week Program)

Level 5 wraps up the sprint; aim to finish by the end of the second week so there’s time for pilot feedback.

| Day | Focus | Deliverables |
| --- | --- | --- |
| Week 2, Day 3 | Guide + tooling setup | Import Level 5 content, configure auto-open panes for `tools/`, add tool-calling diagrams, document logging instructions. |
| Week 2, Day 4 | Auto-graders + Coach + final instrumentation | Implement tool-aware graders, enable Coach hints for tool failures, verify playback/analytics capture `tools/`, run LMS sync test, perform end-to-end QA. |
| Week 2, Day 5 (shared) | Pilot + sign-off | Run pilot conversations covering tool calling, monitor dashboards, capture final issues. |

---

## 8. Handoff Checklist

- [ ] Guides emphasize tool-calling workflow vs. explicit actions.  
- [ ] Graders verify tool registration, schemas, and multi-tool conversations.  
- [ ] Virtual Coach messages cover tool misconfigurations and debugging steps.  
- [ ] Playback includes `tools/` edits; QA reviewed recorded sessions.  
- [ ] Analytics thresholds updated; LMS final grade weighting configured.  
- [ ] Pilot feedback documented with follow-up tasks (if any) before broad release.
