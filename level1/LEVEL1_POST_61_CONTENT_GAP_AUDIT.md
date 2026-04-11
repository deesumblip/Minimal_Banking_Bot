# Level 1 content gap audit: Lab 6.1 onwards

**Question**: Do any assignments from Lab 6.1 onwards assume students have already created something that was never actually created in an earlier lab?

**Sequentiality**: Each graded lab must not be passable using only the previous lab's configuration. Changes made:
- **Starter domain**: `utter_goodbye` removed from `level1/domain/basics.yml` so Lab 2.2 (Creating Your First Response) cannot be passed with the starter alone; students must add `utter_goodbye`.
- **Lab 3.5 grader**: Step 1 now requires key phrases from the Lab 3.5 handout in the domain (`Monday` or `9am` for `utter_hours`; `account number` for `utter_balance`) so Lab 3.5 cannot be passed with only Lab 3.4's student-written content.
- **Lab 7.2 grader**: `hours.yml` and `balance.yml` are in the known-files list so Lab 7.2 requires a new flow beyond those from Lab 3.5.

---

## What the course creates (by lab)

| Created in | Domain | data/basics flows |
|------------|--------|-------------------|
| **Starter repo** | utter_greet, utter_help, utter_contact, utter_goodbye | greet.yml, help.yml, contact.yml |
| Lab 3.2 | — | goodbye.yml |
| Lab 3.4 | (optional / student-written) | hours.yml, balance.yml (student content) |
| Lab 3.5 | utter_hours, utter_balance | Replace hours.yml, balance.yml with given content |

So after Lab 3.5, students have: greet, help, contact, goodbye, hours, balance (flows + domain responses for all).

---

## Lab 6.1 – Training Your Agent

- **Assumes**: Lab 3.5 done (domain + hours/balance flows) so `rasa train` passes validation.
- **Gap?** **No.** Lab 6.1 text says "Before you begin: Complete Lab 3.5 (Adding New Flows)".

---

## Lab 6.2 – Using Rasa Inspector

- **Assumes**: Trained model (Lab 6.1), and that typing "hello" triggers a response (greet flow).
- **Gap?** **No.** Greet flow is in the starter repo; model exists after 6.1.

---

## Lab 6.3 – Testing Your Agent

- **Assumes**: greet, help, contact flows (and optionally goodbye).
- **Gap?** **No.** Greet/help/contact are in the repo; goodbye is created in Lab 3.2. Lab 6.3 says "Test the goodbye flow (if you created it)".
- **Note**: Lab 6.3 does not ask students to test hours or balance; that’s a design choice, not a missing prerequisite.

---

## Lab 7.1 – Complete Agent Walkthrough

- **Assumes**: Session start → greet; help flow; contact flow; pattern_completed.
- **Gap?** **No.** All of these are in the starter (patterns + greet/help/contact).

---

## Lab 7.2 – Build Your Own Feature

- **Assignment**: Create *one new* response and *one new* flow (e.g. branch locations, FAQ).
- **Gap?** **Yes (grading).** The Lab 7.2 grader treats as "known" only: greet, help, contact, goodbye, check_balance. It does **not** treat `hours.yml` or `balance.yml` as "already from the course." So a student who has only done through Lab 3.5 (and has hours + balance) can pass Lab 7.2 without adding any new feature—the grader accepts hours or balance as the "new" flow.
- **Fix**: Add `hours.yml` and `balance.yml` to the grader’s list of known (pre–Lab 7.2) flow files so that Lab 7.2 requires a flow *other than* greet, help, contact, goodbye, hours, balance.

---

## Unit 8 (Knowledge Check)

- No hands-on assignment that assumes specific files; no gap identified.

---

## Summary

| Lab / Unit | Content gap? | Action |
|------------|--------------|--------|
| 6.1 | No | — |
| 6.2 | No | — |
| 6.3 | No | — |
| 7.1 | No | — |
| 7.2 | **Yes** (grader accepts hours/balance as "new") | Add hours.yml and balance.yml to grader’s known-files list |
| Unit 8 | No | — |
