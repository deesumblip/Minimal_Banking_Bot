# Level 6 / Chapter 1.6: What to Do (Based on Levels 4 & 5)

This document lists what to do for **Level 6** (Sub-Agents) and **Chapter 1.6** so they follow the same principles and structure as Level 4 and Level 5.

---

## 1. Principles to Apply (from Levels 4 & 5)

| Principle | Level 4 / 5 | Apply to Level 6 |
|-----------|-------------|-------------------|
| **Examples before labs** | Each unit that leads to a “create” lab shows a **full example** (YAML, Python, or config) of the thing students will create. | For every lab that asks students to create or add something, ensure the **preceding unit content** includes a complete example of that thing. |
| **Lab objectives tie to content** | Lab objectives say: “In Unit X you saw an example of … In this lab you will create your own version …” | Use the same wording pattern so labs explicitly reference the examples students saw. |
| **Source content in level folder** | Unit content lives in `level4/Level4_Unit*_Content_*.md` and `level5/Level5_Unit*_Content_*.md`; labs in `Level*_Lab*_Content.md`. | Create `level6/Level6_Unit*_Content_*.md` and `Level6_Lab*_Content.md`; keep in sync with `.guides` Chapter 1.6. |
| **TUTORIAL.md** | level4 and level5 have TUTORIAL.md with ToC and short module summaries. | Add `level6/TUTORIAL.md` with ToC (Modules 0–6) and one-paragraph summaries per module. |
| **CONTENT_LABS_AND_ASSESSMENTS** | level4 has LEVEL4_CONTENT_LABS_AND_ASSESSMENTS.md; level5 has LEVEL5_CONTENT_LABS_AND_ASSESSMENTS.md (mapping, task IDs, grader paths). | Add `level6/LEVEL6_CONTENT_LABS_AND_ASSESSMENTS.md` with Level 5→6 mapping, unit/lab list, task IDs (e.g. 501060001…), grader paths `.guides/secure/level6_graders/`. |
| **Graders under .guides/secure** | All graders in `.guides/secure/level*_graders/`. | Put Level 6 graders in `.guides/secure/level6_graders/`; reference only that path in docs and assessment JSONs. |
| **Unit 6 closing block** | Level 5 has 6.1–6.7 (walkthrough, learned, next, knowledge check, limitations, Level 7 preview, checklist). | Level 6 Unit 6: 6.1 Walkthrough, 6.2 What You’ve Learned, 6.3 What’s Next, 6.4 Knowledge Check, 6.5 Limitations of Level 6, 6.6 What’s Next (beyond course), 6.7 Course Completion Checklist. Mirror in both `.guides` and `level6/`. |

---

## 2. Chapter 1.6 and level6 Structure (Proposed)

**Starter:** level6 folder = Level 5 end state (no Level 6–only content pre-added). Students add sub-agent(s), flow(s) that call them, and any MCP/config.

**Suggested units (align with Course_Topics_By_Level and Verify_Bots/level6):**

| Unit | Content | Lab (if any) | Example to show in content before lab |
|------|---------|---------------|----------------------------------------|
| 0 | Recap Level 5; what Level 6 adds (sub-agents, handoff, `call: agent_name`) | — | Optional: one diagram or snippet of “main flow calls sub-agent.” |
| 1 | Sub-agents concept: what they are, when to use vs tools in main agent | — | Short example: flow step `- call: banking_assistant` and one sentence on what the sub-agent does. |
| 2 | Sub-agent layout and config (e.g. `sub_agents/<name>/config.yml`, protocol, description) | Lab 2.1 | **Full example** of one sub-agent config (e.g. `sub_agents/banking_assistant/config.yml`) so students create a variant. |
| 3 | MCP / ReAct: why ReAct needs MCP, endpoints and sub-agent config | Lab 3.1 | **Full example** of `mcp_servers` in endpoints and (if applicable) sub-agent MCP config so students add their own. |
| 4 | Flow that calls sub-agent (`ask_banking_assistant`, `call: banking_assistant`, exit) | Lab 4.1 | **Full example** of `ask_banking_assistant` flow YAML so students create their own version. |
| 5 | Training and testing Level 6 (run MCP server, actions, Rasa; Inspector) | Lab 5.1, 5.2 | Commands and optional Inspector check; no “create” — examples of how to run/verify. |
| 6 | Walkthrough, What You’ve Learned, What’s Next, Knowledge Check, Limitations, Completion Checklist | — | — |

**Labs:** For each lab that involves **creating or adding** something (e.g. sub-agent config, MCP config, flow that calls sub-agent):

- The **unit content** must include a **complete example** of that artifact.
- The **lab objective** must say: “In Unit X you saw an example of … In this lab you will create your own version …” (or “add your own version” where appropriate).

---

## 3. Checklist for Implementers

- [ ] **.guides/content/Chapter-1-6---Sub-Agents-XXXX**  
  Create chapter folder with unique ID (e.g. suffix like Level 5’s f9e0). Add one page per unit/section; lab pages with `{Check It!|assessment}(code-output-compare-50106XXXX)`.

- [ ] **level6/ unit content**  
  Create `Level6_Unit0_Content_0.1_*.md`, `0.2_*.md`, then Unit 1–6 content files. Each “concept before a create-lab” unit must contain a **full example** (YAML/config or code) of what the lab will ask students to create.

- [ ] **level6/ lab content**  
  Create `Level6_Lab2.1_Content.md`, `Level6_Lab3.1_Content.md`, etc. Each lab objective: “In Unit X you saw … In this lab you will create/add your own version …”

- [ ] **level6/TUTORIAL.md**  
  Table of contents (Modules 0–6) and short summary per module; pointers to Unit 6.x and Lab files.

- [ ] **level6/LEVEL6_CONTENT_LABS_AND_ASSESSMENTS.md**  
  Level 5→6 mapping; list of unit content files and lab content + assessment setup files; task IDs (e.g. 501060001, 501060002, …); grader paths `.guides/secure/level6_graders/`; Codio chapter ID.

- [ ] **level6/ Level 6 Unit 6 closing**  
  Add Level6_Unit6_Content_6.1 through 6.7 (walkthrough, learned, next, knowledge check, limitations, what’s next, completion checklist) in level6 and mirror in .guides.

- [ ] **Graders**  
  Implement graders under `.guides/secure/level6_graders/` (e.g. `lab_2.1_grader.py`, …). All references in assessment JSONs and docs use `.guides/secure/level6_graders/` only.

- [ ] **Assessment setup files**  
  Create `Level6_Lab*.1_Assessment_Setup.md` (and any .2) with task IDs, COMMAND, grader path, and “expected PASS” criteria.

- [ ] **level6/README.md**  
  Fix current README (it describes Level 5). Replace with Level 6 final bot: contents (sub-agents, MCP, flows), what the bot can do, how to run (MCP server, actions, Rasa).

- [ ] **RASA_LICENSE / Codio vs local**  
  If Level 6 has setup or env steps, follow the same pattern as Lab 0.1: RASA_LICENSE only where specified; separate Codio vs local instructions; no OPENAI_API_KEY in student-facing Lab 0.1–style steps unless required for that level.

---

## 4. Summary

For Level 6 / Chapter 1.6, do the following **on the basis of what we’ve done for each chapter/level**:

1. **Content first, then labs** — For every “create” or “add” lab, the preceding unit has a **full example** of the artifact (config, flow YAML, etc.).
2. **Lab wording** — Labs explicitly say “you saw an example in Unit X” and “create/add your own version.”
3. **Single source in level6** — All unit and lab narrative content lives in `level6/` (Level6_Unit*_Content_*.md, Level6_Lab*_Content.md) and is kept in sync with `.guides` Chapter 1.6.
4. **TUTORIAL + CONTENT_LABS doc** — level6/TUTORIAL.md and level6/LEVEL6_CONTENT_LABS_AND_ASSESSMENTS.md, following level4/level5.
5. **Secure graders** — All Level 6 graders under `.guides/secure/level6_graders/`; all references point there.
6. **Unit 6 bookend** — Full Unit 6 set (6.1–6.7) in both .guides and level6.
7. **README** — level6/README.md describes the Level 6 final bot and how to run it.

This keeps Level 6 consistent with the “examples before labs” and “create your own version” approach used in Levels 4 and 5.
