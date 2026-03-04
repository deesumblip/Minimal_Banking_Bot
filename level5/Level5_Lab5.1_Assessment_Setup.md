# Lab 5.1: Training - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 5 (Training and Testing), Level 5.

**Task.** From project root activate venv, `cd level5`, run `rasa train`. Run the assessment when done.

---

## Assessment Setup (For Implementers)

### Overview

Verifies that the student can train from level5 (or that required files are present so training would succeed). Grader may run `rasa train` from level5 or check for domain, data, config, tools, and model output.

### Assessment Type

**Code Test** (Python or shell script).

### Code Test

Grader: `.guides/secure/level5_graders/lab_5.1_grader.py`. May execute: activate venv, cd level5, rasa train; or verify presence of level5/domain, level5/data, level5/config.yml, level5/endpoints.yml with tools, level5/tools/. On success print `PASS`. COMMAND: `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level5_graders/lab_5.1_grader.py`. WD: `/home/codio/workspace`. Expected: `PASS`.
