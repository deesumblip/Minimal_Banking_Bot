# Level 3 – Codio Delivery Manual (Slot Collection)

Unified reference for building the Level 3 “Slot Collection” course on Codio. It blends student curriculum highlights with all implementation steps so even a Codio novice can deliver memory-enabled flows without external documentation.

---

## 0. Orientation

### Prerequisites Checklist

- Level 2 Codio course deployed (or accessible for reference).
- Codio permissions for Guides, assessments, Virtual Coach, analytics.
- Rasa Pro licence/OpenAI API keys (reuse `.env.template`).
- Comfortable editing YAML (slots) and Python (actions).
- Time commitment: one full day plus a follow-up half-day (Week 1 Day 5 and Week 2 Day 1).

### Overview

- **Goal**: teach students to capture user information via slots, prompt for missing data, and use slots in actions.
- **Key artifacts**: new `slots:` block, `utter_ask_*` prompts, `data/basics/check_balance.yml`, and `actions/action_check_balance_simple.py`.
- **Sprint allocation**: **Week 1 Day 5** (Guides) + **Week 2 Day 1** (graders & instrumentation).

---

## 1. Course Content Snapshot

| Module | Focus | Student Outcomes |
| --- | --- | --- |
| Module 0 | Recap Level 2 | Confirm existing actions still function |
| Module 1 | Slot introduction | Understand slot purpose & lifecycle |
| Module 2 | Slot types | Learn text vs. categorical vs. others |
| Module 3 | Defining slots in domain | Add `account` slot & prompts |
| Module 4 | Collecting slots in flows | Use `collect:` step in `check_balance.yml` |
| Module 5 | Reading slots in actions | Access slot values inside Python |
| Module 6 | Training/testing with slots | Validate bot prompts and remembers data |
| Module 7 | Putting it together | Run full check-balance conversation |
| Module 8 | Assessment | Evaluate understanding & implementation |

---

## 2. Workspace Preparation

1. **Clone Level 2 Codio project** (optional) or create new `BankingBot-Level3` project using `level3/` folder.
2. **Stack validation**: same Python 3.11 + `rasa-pro` install as previous levels.
3. **Folder hygiene**: ensure only `level3/` contents exist. Slots rely on updated domain/flows; remove Level 2 leftovers.
   - **Codio OS reminder**: Codio workspaces are Ubuntu-based. Windows-specific commands in the curriculum provide learner context only—keep Codio instructions Linux-focused.
4. **Virtualenv smoke test**:
   ```bash
   cd level3
   python3.11 -m venv .venv && source .venv/bin/activate
   python -m pip install --upgrade pip
   python -m rasa data validate
   ```
   Validation should succeed after copying baseline files.

---

## 3. Codio Guides Build-Out

1. Copy `.guides/` from Level 2, rename title to `Level 3 – Slot Collection`.
2. Update sections as follows (source content from `CODIO_IMPLEMENTATION_GUIDE.md`):
   ```markdown
   ## Welcome Back
   <Explain memory upgrade — “Course Introduction” section>

   ## Module 0 – Level 2 Recap
   <Checklist ensuring actions still pass tests — “Module 0: Recap - What You Built in Level 2”>

   ## Module 1 – Why Slots Matter
   <Conceptual discussion — “Module 1: Introduction to Slots”>

   ## Module 2 – Slot Types
   @open{"path":"/home/codio/workspace/level3/domain/basics.yml"}
   <Introduce different slot configs — “Module 2: Understanding Slot Types”>

   ## Module 3 – Defining the Account Slot
   <Step-by-step instructions adding slot + `utter_ask_account` — “Module 3: Defining Slots in the Domain”>

   ## Module 4 – Collecting Slots in Flows
   @open{"path":"/home/codio/workspace/level3/data/basics/check_balance.yml"}
   <Walkthrough of `collect:` syntax — “Module 4: Collecting Slots in Flows”>

   ## Module 5 – Reading Slots in Actions
   @open{"path":"/home/codio/workspace/level3/actions/action_check_balance_simple.py"}
   <Explain tracker.get_slot & message formatting — “Module 5: Reading Slots in Actions”>

   ## Module 6 – Train & Test with Slots
   @term{"command":"python -m rasa train"}
   <Instructions for inspector scenario — “Module 6: Training and Testing with Slots”>

   ## Module 7 – Putting It Together
   <Full conversation script — “Module 7: Putting It All Together”>

   ## Module 8 – Assessment & Next Steps
   <Quiz + extension ideas — “Module 8: Assessment and Next Steps”>

   ## Troubleshooting & Glossary
   <Slot-specific errors from “Troubleshooting Guide” and “Glossary”>
   ```
3. Use OTP callouts to highlight slot lifecycle: `Ask → Fill slot → Confirm → Use in action`.
4. Embed flow diagram (`.guides/img/slot_flow.png`) to illustrate the `collect` step.

---

## 4. Assessments & Auto-Grading

| Module | Assessment | Implementation Notes |
| --- | --- | --- |
| Module 3 | YAML validator | Ensure `account` slot exists with correct attributes (`type: text`, `influence_conversation: false`). |
| Module 3 | Prompt check | Confirm `utter_ask_account` text exists. |
| Module 4 | Flow test | Parse `check_balance.yml` verifying `collect: account` sequence appears before calling the action. |
| Module 5 | Python unit test | Call `ActionCheckBalanceSimple` with mocked slot value and assert response includes account number. |
| Module 6 | Conversation script | Run `rasa inspect` with `check_balance` story: user asks for balance, bot asks for account, user provides number, bot responds with account info. Compare transcript to expected JSON. |
| Module 8 | Rubric | Criteria: slot definition, flow prompts, action reading slot, conversation success. |

**Sample validator (Python)** for slot definition:
```python
import yaml, sys
from pathlib import Path
domain = yaml.safe_load(Path("/home/codio/workspace/level3/domain/basics.yml").read_text())
slots = domain.get("slots", {})
acc = slots.get("account")
if not acc:
    sys.exit("Missing 'account' slot in domain/basics.yml")
if acc.get("type") != "text":
    sys.exit("Slot 'account' must be type 'text'")
if acc.get("influence_conversation") is not False:
    sys.exit("Slot 'account' should set influence_conversation: false")
print("Slot checks passed!")
```
Hook into a Code Test assessment with `python .guides/graders/check_slot.py`.

---

## 5. Virtual Coach Configuration

- **Summaries**: remind students to 1) create slot, 2) define ask response, 3) update flow, 4) update action, 5) retrain.
- **Error augmentations**:
  - `ValueError: Slot account not found in domain`: instruct to add slot block.
  - Bot keeps asking for account repeatedly: suggest checking `slot_was_set` event in flow or verifying slot value formatting.
- **Next steps**: encourage running `rasa data validate` and using the provided conversation script.

Test Coach by intentionally removing the slot and observing hints.

---

## 6. Code Playback & Analytics

Track edits to:

- `domain/basics.yml` (slot definition + prompts)
- `data/basics/check_balance.yml`
- `actions/action_check_balance_simple.py`

Analytics focus points:

- Time spent on Module 4 (usually longest).
- Number of attempts for slot validator grader.
- Frequency of Coach interactions about “slot” or “account” – adjust hints accordingly.

Set Behavior Insight thresholds higher than Level 2 (up to 90 minutes) to avoid false positives while students debug.

---

## 7. Optional: LMS Integration

- Map Level 3 assessments to LMS grade items worth ~20% (adjust as needed).
- Provide instructor note on how to manually verify slot behavior using Code Playback (playback should show slot definition typed before action edit).

---

## 8. Timeline Slice

| Day | Morning | Afternoon |
| --- | --- | --- |
| Week 1 – Day 5 | Guides migration for Modules 0–5, embed slot diagrams | Build YAML + action validators, initial Coach messages |
| Week 2 – Day 1 | Finalize Modules 6–8, add conversation scripts, update troubleshooting | Implement conversation grader, enable Coach/Playback/analytics, run LMS sync and QA walkthrough |

Daily checks:
- [ ] Slot validators pass/fail correctly.
- [ ] Conversation script produces expected transcript.
- [ ] Coach hints correctly suggest missing slot steps.
- [ ] Analytics show your QA run.

---

## 9. Final QA

1. Reset environment and follow Guide as student.  
2. Verify the bot prompts for account and remembers it.  
3. Ensure Code Playback timeline shows slot definition and action edit steps.  
4. Confirm LMS grade entry and analytics record the session.  
5. Update instructor notes with any observed student pitfalls before handoff.

### Acceptance Test Commands

- `cd /home/codio/workspace/level3 && python3.11 -m venv .venv && source .venv/bin/activate`
- `python -m rasa train`
- `python -m pytest .guides/graders/check_slot.py`
- `python -m rasa inspect --script scripts/level3_slot_story.json --debug`
- Confirm Code Playback captures edits to `domain/basics.yml`, `data/basics/check_balance.yml`, and `actions/action_check_balance_simple.py`

Level 3 is now ready; proceed to Level 4 for multi-slot collection.
