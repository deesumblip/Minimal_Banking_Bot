# Level 2: Simple Actions - Implementation Overview for Codio Team

## Executive Summary

This document provides implementation guidance for **Level 2: Simple Actions** on the Codio platform.

**Key goals**:
- Preserve the complete student tutorial content (provided in separate content files)
- Convert exercises into Codio labs with auto-grading and clear feedback
- Minimize setup friction (pre-configured environment, templates, helper scripts)
- Use Codio AI Coach for hints and troubleshooting support

### Content Integration Strategy

- The full content from the implementation guide is split into separate unit files:
  - `Level2_Unit0_Content.md` through `Level2_Unit8_Content.md` - Student-facing content
  - `Level2_Troubleshooting_Content.md` - Troubleshooting guide
  - `Level2_AdditionalResources_Content.md` - Extension exercises and resources
- Each unit's content can be copy/pasted directly into Codio Guide Editor content pages
- Exercises should be implemented as **auto-graded labs** wherever possible
- Student-facing lab content is in `Level2_Lab*_Content.md`; full setup (grader, config) is in `Level2_Lab*_Assessment_Setup.md` (synced to Codio Lab-Implementation folder):
  - `Level2_Lab3.1_Content.md` / `Level2_Lab3.1_Assessment_Setup.md` - Lab 3.1: Creating Your Own Action
  - `Level2_Lab4.1_Content.md` / `Level2_Lab4.1_Assessment_Setup.md` - Lab 4.1: Registering Actions in the Domain
  - `Level2_Lab5.1_Content.md` / `Level2_Lab5.1_Assessment_Setup.md` - Lab 5.1: Using Actions in Flows
  - `Level2_Lab6.1_Content.md` / `Level2_Lab6.1_Assessment_Setup.md` - Lab 6.1: Training and Testing with Actions

---

## Technical Specifications for Codio Team

### Lab Environment Configuration

**Base Environment Requirements**:
- Operating System: Linux (Ubuntu 22.04 or similar)
- Python: 3.11
- IDE: Browser-based VS Code (Codio standard)
- Terminal: Bash shell

**Pre-Installed Software**:
- Python 3.11 + pip (latest)
- `rasa-pro` (latest stable)
- `git` (optional)

**Pre-Configured Project Structure** (representative):
```
project/
├── domain/
│   └── basics.yml
├── data/
│   ├── basics/
│   │   └── *.yml
│   └── system/
│       └── patterns/
│           └── patterns.yml
├── config.yml
├── credentials.yml
├── endpoints.yml
├── .env (template with placeholders)
├── load_env.ps1 (for Windows-based local runs; optional in Codio)
└── run_inspector.ps1 (optional helper)

├── actions/
│   ├── __init__.py
│   └── action_*.py
```

**Environment Variables**:
- `RASA_LICENSE=...`
- `OPENAI_API_KEY=...`

**Port Configuration**:
- Rasa Inspector: 5005 (default)
- **Port Forwarding**: Required for Unit 6 (Testing with Rasa Inspector)
  - Students need to access Inspector via browser
  - See Unit 6 content for detailed port forwarding instructions

---

## Auto-Grading Guidance (Codio Team)

**Recommended auto-grading checks**:
- Validate YAML files parse successfully and required keys exist (domain + flows + patterns)
- Validate required new artifacts for Level 2 exist (e.g., new flows/actions/tools)
- Smoke-test bot starts (`rasa inspect`) and responds to a small scripted conversation

**Implementation notes**:
- Prefer deterministic checks (file existence + YAML structure + expected strings) over LLM-output matching.
- Provide actionable error output ("Expected `actions:` section in `domain/basics.yml`", etc.).
- Each assessment grader script includes:
  - Virtual environment verification
  - File existence checks
  - Content/structure validation
  - Clear PASS/FAIL messages with hints

**Assessment Files**:
- All grader scripts should be saved in `.guides/secure/level2_graders/`
- Make scripts executable: `chmod +x .guides/secure/level2_graders/*.sh`
- Use absolute paths in COMMAND field: `/home/codio/workspace/.guides/secure/level2_graders/lab_X.X_grader.sh`

---

## AI Coach Configuration Reference (Codio Team)

**Guidelines**:
- Provide hints, not full solutions
- Point learners to the right file and the relevant section
- Explain why a concept matters (actions vs responses, slots, tools, etc.)
- Encourage incremental testing (train + inspect frequently)

**Common Topics for AI Coach**:
- Action class structure and required methods
- Import statements for Rasa SDK
- Domain registration syntax
- Flow creation and action references
- Training errors and troubleshooting

---

## Terminal Configuration

### Unit 6: Rasa Inspector Setup

For Unit 6 (Testing with Actions), configure the terminal so students can "jump right in":

**Terminal Tab Configuration**:
- **Initial Command**: 
  ```bash
  cd /home/codio/workspace/level2 && source .venv/bin/activate
  ```
- This ensures students are:
  - In the correct directory (`level2`)
  - Virtual environment is already activated
  - Ready to run `python -m rasa inspect` immediately

**Port Forwarding Setup**:
- Students need access to Rasa Inspector via browser (port 5005)
- Provide clear instructions for accessing Ports view:
  - **Tools** → **Ports**
  - **Preview** menu → **Ports**
  - Bottom panel tabs → **Ports**
- Direct URL format: `https://your-project-5005.codio.io`
- See `Level2_Unit6_Content.md` for detailed student instructions

---

## Quality Assurance Checklist (Codio Team)

- [ ] Course runs end-to-end in a clean Codio environment
- [ ] All links/anchors in the student tutorial work in Codio's markdown renderer
- [ ] Auto-grader messages are specific and helpful
- [ ] At least one "happy-path" conversation is validated for this level's new capability
- [ ] Virtual environment setup is consistent across all labs
- [ ] Port forwarding is configured and accessible for Unit 6
- [ ] All grader scripts are executable and use correct paths
- [ ] Terminal is pre-configured for Unit 6 (cd + venv activation)
- [ ] Level 1 content remains intact (Level 2 builds on Level 1)

---

## File Organization

### Content Files (Copy/Paste into Codio Guide Editor)
- `Level2_Unit0_Content.md` - Recap of Level 1
- `Level2_Unit1_Content.md` - Introduction to Actions
- `Level2_Unit2_Content.md` - Understanding the Action Class
- `Level2_Unit3_Content_3.1_*.md`, `Level2_Unit3_Content_3.2_*.md` - Creating Your First Action (Unit 3)
- `Level2_Unit4_Content.md` - Registering Actions in the Domain
- `Level2_Unit5_Content.md` - Using Actions in Flows
- `Level2_Unit6_Content.md` - Training and Testing with Actions
- `Level2_Unit7_Content.md` - Putting It All Together
- `Level2_Unit8_Content.md` - Assessment and Next Steps
- `Level2_Troubleshooting_Content.md` - Troubleshooting Guide
- `Level2_AdditionalResources_Content.md` - Extension Exercises

### Assessment Files (Implementation Instructions)
- `Level2_Lab3.1_Assessment_Setup.md` - Lab 3.1 setup (student content in `Level2_Lab3.1_Content.md`)
- `Level2_Lab4.1_Assessment_Setup.md` - Lab 4.1 setup (student content in `Level2_Lab4.1_Content.md`)
- `Level2_Lab5.1_Assessment_Setup.md` - Lab 5.1 setup (student content in `Level2_Lab5.1_Content.md`)
- `Level2_Lab6.1_Assessment_Setup.md` - Lab 6.1 setup (student content in `Level2_Lab6.1_Content.md`)

### Implementation Files
- `Level2_Implementation_Overview.md` - This file (for Codio team)

---

## Dependencies

**Required for Level 2**:
- Level 1 must be completed first (all Level 1 files remain)
- Rasa Pro installed and licensed
- Virtual environment with Rasa Pro
- Port forwarding capability (for Unit 6 testing)

**Not Required**:
- SSH access (port forwarding handles Inspector access)
- External API keys beyond RASA_LICENSE and OPENAI_API_KEY

---

## Next Steps

1. Review all content files and ensure they're ready for Codio Guide Editor
2. Set up assessments using the provided grader scripts
3. Configure terminal settings for Unit 6
4. Test port forwarding for Rasa Inspector access
5. Verify all grader scripts work correctly
6. Test end-to-end student workflow

---
