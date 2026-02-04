# Level 5 – Codio Delivery Manual (Tool Calling)

Comprehensive build guide for launching Level 5 (“Tool Calling”) on Codio. Combines the student curriculum with platform tasks so a Codio newcomer can deliver the LLM tool orchestration experience without consulting other docs.

---

## 0. Orientation

### Prerequisites Checklist

- Level 4 Codio project delivered (tool calling builds on multi-slot flow).
- Codio account with rights to edit Guides, assessments, Virtual Coach, analytics.
- Rasa Pro licence/OpenAI API keys (reuse `.env.template`).
- Comfortable reading inspector logs and basic Python tooling.
- Time allocation: two days (Week 2 Days 3–4) plus pilot buffer on Day 5.

### Overview

- **Goal**: allow the LLM-powered assistant to choose from multiple banking tools at runtime, demonstrating tool registration, schemas, and tool-aware actions.
- **Key assets**: `tools/banking_tools.py`, `actions/action_process_transfer_with_tools.py`, `data/basics/transfer_money_tools.yml`, updated `endpoints.yml`.
- **Sprint allocation**: **Week 2 Days 3–4** (with Day 5 reserved for combined pilot).

---

## 1. Course Content Snapshot

| Module | Focus | Outcomes |
| --- | --- | --- |
| Module 0 | Recap Level 4 | Confirm multi-slot flows continue to work |
| Module 1 | Introduction to tools | Understand tool vs. action |
| Module 2 | Tools vs. actions comparison | Identify when to rely on LLM tool selection |
| Module 3 | Creating tool functions | Implement banking utility functions |
| Module 4 | Registering tools | Wire tool metadata in `endpoints.yml` |
| Module 5 | Using tools in conversations | Understand LLM decision-making |
| Module 6 | Training/testing with tools | Capture logs, inspect tool calls |
| Module 7 | Putting it together | Complex scenarios combining tools |
| Module 8 | Assessment | Evaluate mastery of tool orchestration |

---

## 2. Workspace Setup

1. Create `BankingBot-Level5` Codio project, import `level5/` directory.  
2. Ensure Python 3.11 + `rasa-pro` installed (same procedure as previous levels).  
3. Remove earlier levels from workspace to avoid confusion.  
   - **Codio OS reminder**: Codio boxes run Ubuntu. Treat Windows-only commands from the curriculum as contextual info for learners; use Linux commands inside Codio.
4. Virtualenv smoke test:
   ```bash
   cd level5
   python3.11 -m venv .venv && source .venv/bin/activate
   python -m pip install --upgrade pip
   python -m rasa data validate
   ```
5. Run the provided tool demo script (optional) to ensure tools import correctly:
   ```bash
   python scripts/test_tools.py  # create if desired, see below
   ```

**Optional helper script (`scripts/test_tools.py`)**
```python
import tools.banking_tools as bt
print(bt.check_balance_tool({"account": "1234"}))
```

---

## 3. Guides Authoring

1. Copy `.guides/` from Level 4. Update metadata to `Level 5 – Tool Calling`.  
2. Suggested Guide outline (reference `CODIO_IMPLEMENTATION_GUIDE.md` modules when copying content):
   ```markdown
   ## Welcome
   <Explain transition from scripted flows to tool-enabled LLM — “Course Introduction”>

   ## Module 0 – Level 4 Recap
   <Checklist: transfer flow still works — “Module 0: Recap - What You Built in Level 4”>

   ## Module 1 – What Are Tools?
   <Explain LLM tool concept — “Module 1: Introduction to Tools”>

   ## Module 2 – Tools vs. Actions
   <Comparative table — “Module 2: Understanding Tools vs Actions”>

   ## Module 3 – Building Tool Functions
   @open{"path":"/home/codio/workspace/level5/tools/banking_tools.py"}
   <Walkthrough tool schema, return values — “Module 3: Creating Tool Functions”>

   ## Module 4 – Registering Tools
   @open{"path":"/home/codio/workspace/level5/endpoints.yml"}
   <Explain tools: block — “Module 4: Registering Tools”>

   ## Module 5 – Using Tools in Conversations
   @open{"path":"/home/codio/workspace/level5/actions/action_process_transfer_with_tools.py"}
   <Explain bridging logic — “Module 5: Using Tools in Conversations”>

   ## Module 6 – Train, Run, Inspect
   @term{"command":"python -m rasa train"}
   <Instructions to run inspector with debug logging — “Module 6: Training and Testing with Tools”>

   ## Module 7 – Advanced Scenarios
   <Multi-tool scenario walkthrough — “Module 7: Putting It All Together”>

   ## Module 8 – Assessment
   <Quiz + project rubric — “Module 8: Assessment and Next Steps”>

   ## Troubleshooting
   <Tool registration errors, logging tips from “Troubleshooting Guide” and “Glossary”>
   ```
3. Embed diagrams showing how the LLM decides which tool to invoke. Include instructions to view inspector logs (`.rasa/logs/`) for tool call traces.
4. Add callouts reminding students to restart the assistant after changing `tools/` definitions.

---

## 4. Assessments & Auto-Grading

| Module | Assessment | Notes |
| --- | --- | --- |
| Module 3 | Tool schema validator | Parse `tools/banking_tools.py` ensuring each tool defines `name`, `description`, `args_schema`, and returns dict with `success`/`content`. |
| Module 4 | Configuration check | Ensure `endpoints.yml` contains `tools:` block referencing `tools.banking_tools`. |
| Module 5 | Action bridge test | Run Python unit test verifying `action_process_transfer_with_tools` calls the correct tool based on tracker plans. |
| Module 6 | Conversation replay | Run `python -m rasa inspect --script scripts/tool_call_story.json --debug` and assert logs show each tool invocation. |
| Module 8 | Rubric assessment | Evaluate tool registration, error handling, documentation. |

**Example schema validator**:
```python
import tools.banking_tools as bt
required_tools = ["check_balance_tool", "process_transfer_tool"]
for name in required_tools:
    tool = getattr(bt, name, None)
    if tool is None:
        raise SystemExit(f"Missing tool function: {name}")
    if not hasattr(tool, "name") or not tool.name:
        raise SystemExit(f"Tool {name} missing name attribute")
    if not hasattr(tool, "args_schema"):
        raise SystemExit(f"Tool {name} missing args_schema")
print("Tool schema checks passed!")
```
Run via Code Test command `python .guides/graders/check_tools.py`.

**Conversation script ideas**:
- Happy path: check balance → transfer if sufficient funds.  
- Error path: missing tool registration should produce friendly error message.

---

## 5. Virtual Coach Configuration

- **Summaries**: highlight the three-step workflow (write tool → register tool → test conversation).  
- **Error augmentations**:
  - `ToolValidationError` or `SchemaValidationError` → remind to ensure `args_schema` matches expected parameters.  
  - No tool invocation logs → suggest running inspector with `--debug` and ensuring `endpoints.yml` saved.  
- **Next steps**: instruct students to rerun `python -m rasa run actions` and check `.rasa/logs/llm.log` for tool call traces.

---

## 6. Code Playback & Analytics

Track `tools/`, `actions/action_process_transfer_with_tools.py`, `data/basics/transfer_money_tools.yml`, and `endpoints.yml`. Playback verifies students authored tool schemas themselves.

Analytics focus:
- Time spent on tool schema section (expect increased iterations).  
- Number of grader attempts for conversation replay.  
- Coach usage mentioning “tool” or “schema.”  
Adjust Behavior Insight thresholds to allow up to 120 minutes—tool debugging can be lengthy.

---

## 7. Optional: LMS & Instructor Support

- Set Level 5 weighting (~20%) and ensure final grade aggregation lines up with earlier levels.  
- Prepare instructor quick reference describing how to inspect tool logs and replay sessions via Code Playback.  
- Encourage instructors to review `tools/banking_tools.py` via playback to detect copy/paste vs. genuine typing.

---

## 8. Timeline Slice (Two-Week Sprint)

| Day | Morning | Afternoon |
| --- | --- | --- |
| Week 2 – Day 3 | Migrate Guides (Modules 0–5), embed tool diagrams, configure auto-open panes | Build schema/config/action graders, draft Coach hints |
| Week 2 – Day 4 | Add Modules 6–8 content, create conversation scripts, update troubleshooting | Enable Coach/Playback/analytics, run LMS sync, execute full QA run |
| Week 2 – Day 5 (shared) | Pilot with sample learners, monitor dashboards, capture feedback | Triage issues; finalize instructor handoff |

Daily checks:
- [ ] Tool schemas validated automatically.  
- [ ] Conversation script shows tool invocations in logs.  
- [ ] Coach hints guide students through registration errors.  
- [ ] Analytics capture QA run; Behavior Insights thresholds adjusted.  
- [ ] LMS grade items updated.

---

## 9. Final QA

1. Reset environment; follow the Guide as a student.  
2. Run inspector with debug logging; confirm tool invocations appear.  
3. Review Code Playback to ensure tools and actions were hand-authored.  
4. Verify LMS gradebook updates and analytics record the session.  
5. Document pilot findings in instructor notes before release.

### Acceptance Test Commands

- `cd /home/codio/workspace/level5 && python3.11 -m venv .venv && source .venv/bin/activate`
- `python -m rasa train`
- `python -m pytest .guides/graders/check_tools.py`
- `python -m rasa inspect --script scripts/tool_call_story.json --debug`
- Review Code Playback for edits to `tools/banking_tools.py`, `actions/action_process_transfer_with_tools.py`, and `endpoints.yml`

Level 5 is now launch-ready. Combine with earlier levels for the full two-week Codio rollout.
