# Lab 3.1: Defining a Slot in the Domain - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Unit 3: Defining Slots in the Domain.

**Task**: Add `slots:` with `account` (type: text) and `utter_ask_account` response to `domain/basics.yml` in the `level3` folder. Run the assessment when done.

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that the student has added the `slots:` section with an `account` slot and the `utter_ask_account` response to `level3/domain/basics.yml`.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

```
.guides/assessments/level3_graders/lab_3.1_grader.sh
```

## Grader Script

- Run from **workspace root**: activate venv, then `cd level3`.
- Check: `domain/basics.yml` exists; file contains `slots:` section; `account` slot present (type: text); `utter_ask_account` present under responses.
- Print `PASS` / `Successfully passed!` on full score; `FAIL` and exit 1 on failure.
- Suggested points: 6–8 total (e.g. file exists 1, slots section 2, account slot 2, utter_ask_account 2).

## Codio Configuration

- COMMAND: `bash /home/codio/workspace/.guides/assessments/level3_graders/lab_3.1_grader.sh`
- Working Directory: `/home/codio/workspace`
- Expected output: `PASS` or `Successfully passed!`
