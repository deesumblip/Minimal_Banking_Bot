# Lab 4.1: Creating a Flow with Slot Collection - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Unit 4: Collecting Slots in Flows.

**Task**: Create `data/basics/check_balance.yml` in the `level3` folder with a flow that has `collect: account` and `action: action_check_balance_simple`. Run the assessment when done.

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that the student has created `level3/data/basics/check_balance.yml` with a flow containing a `collect: account` step and the `action_check_balance_simple` action step.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

```
.guides/assessments/level3_graders/lab_4.1_grader.sh
```

## Grader Script

- Run from **workspace root**: activate venv, then `cd level3`.
- Check: `data/basics/check_balance.yml` exists; file contains a flow with `collect: account` (or equivalent) and `action: action_check_balance_simple`.
- Print `PASS` / `Successfully passed!` on full score; `FAIL` and exit 1 on failure.
- Suggested points: 6–8.

## Codio Configuration

- COMMAND: `bash /home/codio/workspace/.guides/assessments/level3_graders/lab_4.1_grader.sh`
- Working Directory: `/home/codio/workspace`
- Expected output: `PASS` or `Successfully passed!`
