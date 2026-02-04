# Level 2 Codio Implementation Playbook

**Purpose**: Stand up Level 2 (“Simple Actions”) in Codio without altering `level2/CODIO_IMPLEMENTATION_GUIDE.md`, using the Level 1 flow as a template while accounting for the new Python `actions/` package and action-driven flows.

---

## 1. Reference Materials

- Level 2 curriculum: `level2/CODIO_IMPLEMENTATION_GUIDE.md`
- Codio Guides editor: [Codio Guides documentation](https://www.codio.com/docs/guides)
- Auto-grading/assessments: [Codio Auto-Grading overview](https://www.codio.com/features/auto-grading) and [Global Assessments Library](https://www.codio.com/blog/codio-launches-global-assessments-library)
- Virtual Coach configuration: [Virtual Coach settings](https://docs.codio.com/instructors/setupcourses/assignment-settings/virtual-coach.html)
- Code Playback tooling: [Code Playback docs](https://docs.codio.com/common/tools/code-playback.html)
- Analytics & Behavior Insights: [Learning Insights](https://www.codio.com/features/learning-insights) and [Behavior Insights config](https://docs.codio.com/instructors/teaching/behaviorinsights.html)

---

## 2. Authoring the Codio Guide

1. **Clone Level 1’s `.guides` structure** into `level2/` so navigation, tabs, and layout boilerplate are already wired.
2. **Swap in Level 2 modules** (Recap + Modules 1–8) from the guide, keeping the “recap from Level 1” callouts to remind students nothing regresses.
3. **Pre-open action files**: configure Guide steps so editing sections automatically open `actions/__init__.py`, `actions/action_bank_hours.py`, and `domain/basics.yml`.
4. **Embed action flow diagrams** or GIFs showing how `hours.yml` triggers `action_bank_hours` to reinforce the difference between responses vs. actions.

Outcome: Students stay in Codio, editing the new `actions/` folder while reviewing instructions in the Guide panes.

---

## 3. Designing Assessments & Auto-Graders

| Goal | Action Items | Reference |
| --- | --- | --- |
| Validate action registration | Ensure `domain/basics.yml` contains `actions:` with `- action_bank_hours`. Fail with a clear message if missing. | [Auto-grading overview](https://www.codio.com/features/auto-grading) |
| Confirm action code | Run a unit-style Python script that imports `actions.action_bank_hours.ActionBankHours`, instantiates it, and checks that `name()` returns `action_bank_hours`. | same |
| Flow testing | Execute `rasa inspect` with a scripted conversation hitting the hours flow; confirm the response text includes dynamic hours string. | same |
| Concept checks | Short quizzes explaining differences between `utter_*` and `action_*`, when to use each, and how endpoints register action servers. | [Assessments library](https://www.codio.com/blog/codio-launches-global-assessments-library) |
| Rubric alignment | For the final “Putting it together” lab, grade on: action file exists, registered, flow calls action, bot responds correctly. | same |

Keep graders idempotent and deterministic so engineers can run them locally before uploading.

---

## 4. Configuring Codio Coach

1. Activate Virtual Coach for Level 2 assignments with emphasis on: “Have you run `python -m rasa run actions`?”, “Did you add your action to `domain/basics.yml`?”, etc.  
2. **Summarize Prompt** should remind learners to update both the Python file and the domain registration.  
3. **Error Augmentation**: map common stack traces (e.g., “ActionException: No registered action found”) to human-readable explanations.  
4. Feed Coach logs back into the Guide FAQ so repeated misunderstandings are addressed directly.

---

## 5. Instrumenting Code Playback

- Track the following files: `domain/basics.yml`, `data/basics/hours.yml`, `actions/__init__.py`, `actions/action_bank_hours.py`, `endpoints.yml`.  
- During QA, scrub to ensure the action file is authored keystroke-by-keystroke (green paste bars should be rare).  
- Note in the instructor docs how to replay a student session to verify they wrote the action themselves.

---

## 6. Analytics, Behavior Insights, LMS

- Reuse the analytics setup from Level 1; extend dashboards with filters that isolate Level 2 to evaluate how long students spend on action authoring.  
- Configure Behavior Insight thresholds to flag zero-debugging sessions (possible paste) or extremely short time-on-task.  
- Tie the Level 2 assignment to an LMS grade column that weights action correctness appropriately.

---

## 7. Recommended Timeline Slice (Two-Week Program)

Level 2 should immediately follow the Level 1 handoff so shared assets stay warm.

| Day | Focus | Deliverables |
| --- | --- | --- |
| Week 1, Day 3 | Guide migration & layouts | Import Level 2 sections into Guides, set auto-open panes for `actions/` files, update media. |
| Week 1, Day 4 | Auto-graders + Coach + instrumentation | Implement action-aware graders, enable Coach modes with action-specific hints, verify Code Playback + analytics are capturing new files, run a quick LMS sync test. |

Proceed to Level 3 once sample conversations pass and dashboards show healthy telemetry.

---

## 8. Handoff Checklist

- [ ] `.guides` mirrors Level 2 modules with action callouts.  
- [ ] Graders validate action code, domain registration, and flow behavior.  
- [ ] Virtual Coach responses cover action creation/registration errors.  
- [ ] Code Playback includes `actions/` files; QA reviewed sample sessions.  
- [ ] Analytics/Behavior thresholds updated; LMS grade column connected.  
- [ ] Instructor notes describe how to rerun graders locally and inspect action logs.

Meeting these items ensures Level 2 fits inside the shared two-week implementation window without blocking later levels.
