# Level 4 – Codio Delivery Manual (Multiple Slots)

Purpose-built manual that merges Level 4 student guidance with all Codio implementation steps. Designed for implementers familiar with Levels 1–3 but still novice on Codio—follow this to deliver the multi-slot “Transfer Money” experience end to end.

---

## 0. Orientation

### Prerequisites Checklist

- Level 3 Codio deployment completed.
- Codio permissions for Guides, assessments, Virtual Coach, analytics.
- Rasa Pro/OpenAI keys available (reuse `.env.template`).
- Comfortable editing multi-file YAML flows and Python validation logic.
- Time commitment: one full day (Week 2 Day 2).

### Overview

- **Goal**: teach students to collect multiple pieces of information (amount, recipient, account_from), validate them, and execute a transfer action.
- **Key files**: `domain/basics.yml` (new slots & prompts), `data/basics/transfer_money.yml`, `actions/action_process_transfer.py`.
- **Sprint allocation**: **Week 2 Day 2** (half-day guide migration + half-day automation).

---

## 1. Course Content Snapshot

| Module | Focus | Student Outcomes |
| --- | --- | --- |
| Module 0 | Recap Level 3 | Confirm single-slot flow still works |
| Module 1 | Why multiple slots? | Explore real-world scenarios (transfers) |
| Module 2 | Defining additional slots | Add `amount`, `recipient`, `account_from` |
| Module 3 | Collecting multiple slots | Build `transfer_money.yml` with ordered prompts |
| Module 4 | Validating slots in actions | Ensure action handles missing/malformed data |
| Module 5 | Handling complex conversations | Understand slot order & re-prompts |
| Module 6 | Train/test multi-slot flows | Run scripted conversations |
| Module 7 | Final build | Combine everything |
| Module 8 | Assessment | Evaluate full transfer build |

---

## 2. Workspace Preparation

1. Create new Codio project `BankingBot-Level4` (import `level4/` folder).  
2. Verify Python 3.11 + `rasa-pro` installation.  
3. Remove any leftover `level3/` artifacts—Level 4 contains its own updated files.  
   - **Codio OS reminder**: Codio boxes run Ubuntu. Windows-specific commands in the curriculum are for learners’ local setups and should not be executed inside Codio.
4. Virtualenv smoke test:
   ```bash
   cd level4
   python3.11 -m venv .venv && source .venv/bin/activate
   python -m pip install --upgrade pip
   python -m rasa data validate
   ```
5. Confirm `actions/action_process_transfer.py` runs unit test (provided below) before exposing to students.

---

## 3. Guides Authoring

1. Copy `.guides/` from Level 3 to Level 4, update metadata (`title: Level 4 – Multiple Slots`).  
2. Suggested section outline (reference `CODIO_IMPLEMENTATION_GUIDE.md` modules as noted):
   ```markdown
   ## Welcome
   <Explain multi-slot upgrade — “Course Introduction”>

   ## Module 0 – Level 3 Recap
   <Checklist verifying account slot flow — “Module 0: Recap - What You Built in Level 3”>

   ## Module 1 – Why Multiple Slots?
   <Real-world examples — “Module 1: Introduction to Multiple Slots”>

   ## Module 2 – Defining New Slots
   @open{"path":"/home/codio/workspace/level4/domain/basics.yml"}
   <Add amount/recipient/account_from + prompts — “Module 2: Defining Multiple Slots”>

   ## Module 3 – Collecting Slots
   @open{"path":"/home/codio/workspace/level4/data/basics/transfer_money.yml"}
   <Explain collect order — “Module 3: Collecting Multiple Slots in Flows”>

   ## Module 4 – Validating in Actions
   @open{"path":"/home/codio/workspace/level4/actions/action_process_transfer.py"}
   <Walkthrough validation logic — “Module 4: Validating Multiple Slots in Actions”>

   ## Module 5 – Handling Complex Conversations
   <Branching, re-prompts — “Module 5: Handling Complex Conversations”>

   ## Module 6 – Train & Test
   @term{"command":"python -m rasa train"}
   <Script for testing multi-slot flow — “Module 6: Training and Testing with Multiple Slots”>

   ## Module 7 – Putting It Together
   <Full scenario narration — “Module 7: Putting It All Together”>

   ## Module 8 – Assessment & Reflection
   <Rubric + next steps — “Module 8: Assessment and Next Steps”>

   ## Troubleshooting
   <Multi-slot specific issues from “Troubleshooting Guide” and “Glossary”>
   ```
3. Use tables or timelines to visualize slot order: `amount → recipient → account_from → confirm → action`.
4. Add caution callouts about indentation and reusing prompt names.

---

## 4. Assessments & Auto-Grading

| Module | Assessment | Notes |
| --- | --- | --- |
| Module 2 | Slot validator | Ensure all three slots exist with `type: text`, `required: true`, and correct prompts (`utter_ask_*`). |
| Module 3 | Flow order check | Confirm `transfer_money.yml` collects slots in proper sequence; fail if any `collect` missing or misordered. |
| Module 4 | Action unit test | Simulate tracker with slot values, verify transfer summary includes all three. Check error branches when slot missing. |
| Module 6 | Conversation script | Run `rasa inspect` with script containing both happy path and missing slot scenario; ensure bot re-prompts correctly. |
| Module 8 | Rubric | Evaluate slot coverage, validation logic, documentation of transfers. |

**Example unit test** (`.guides/graders/test_transfer_action.py`):
```python
import importlib
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

module = importlib.import_module("actions.action_process_transfer")
action = module.ActionProcessTransfer()
dispatcher = CollectingDispatcher()
tracker = Tracker("test", {"amount": "100", "recipient": "Alex", "account_from": "Checking"}, {}, [], False, None, {}, "action_listen")

action.run(dispatcher, tracker, {})
message = dispatcher.messages[-1]["text"]
assert "100" in message and "Alex" in message and "Checking" in message, "Transfer summary missing slot data"
```

---

## 5. Virtual Coach Setup

- **Summaries**: remind students to update three files for every change (domain, flow, action).  
- **Error hints**:
  - “Bot keeps asking for the same slot” → check `slot_was_set` events or ensure slot filled before `action_process_transfer`.  
  - “Action crashed with KeyError” → confirm slot names match between domain, flow, and action.  
- Encourage students to re-run `python -m rasa data validate` after editing any YAML.

---

## 6. Code Playback & Analytics

Track `domain/basics.yml`, `data/basics/transfer_money.yml`, `actions/action_process_transfer.py`. Playback should show repeated edits—use to confirm incremental development.

Analytics focus:
- Time spent on Module 3 (usually longest).  
- Number of grader attempts for multi-slot validator.  
- Coach usage referencing “collect” or “slot order.”  
Adjust Behavior Insight thresholds: max time ~110 minutes before flagging; allow moderate debugging ratio.

---

## 7. Optional: LMS & Instructor Notes

- Assign Level 4 lab weight (~25%) due to higher complexity.  
- Document how instructors can quickly diagnose misordered slots: run grader, check Code Playback around `transfer_money.yml`.  
- Provide example conversation transcripts for both happy path and missing slot scenarios in instructor notes.

---

## 8. Timeline Slice

| Time | Tasks |
| --- | --- |
| Week 2 Day 2 — Morning | Port Guides content (Modules 0–6), embed multi-slot diagrams, configure auto-open panes for flow/action files. |
| Week 2 Day 2 — Afternoon | Implement slot/action/conversation graders, enable Coach & analytics, test LMS sync, run QA walkthrough. |

Checkpoint list:
- [ ] All three slots validated by grader.  
- [ ] Conversation script exercises both happy path and re-prompt path.  
- [ ] Coach hints mention slot order and re-prompts.  
- [ ] Analytics registers QA run.  
- [ ] Instructor notes updated.

---

## 9. Final QA

1. Reset environment; walk through Guide as student.  
2. Confirm transfer flow collects all slots and summarizes correctly.  
3. Trigger missing-slot scenario to ensure re-prompt logic works.  
4. Review Code Playback for slot edits.  
5. Verify LMS entry and analytics logs.  
6. Record observations in instructor notes.

### Acceptance Test Commands

- `cd /home/codio/workspace/level4 && python3.11 -m venv .venv && source .venv/bin/activate`
- `python -m rasa train`
- `python -m pytest .guides/graders/test_transfer_action.py`
- `python -m rasa inspect --script scripts/level4_transfer_story.json --debug`
- Review Code Playback for `domain/basics.yml`, `data/basics/transfer_money.yml`, and `actions/action_process_transfer.py`

Level 4 is ready. Proceed to Level 5 for tool calling.
