# Level 1: Content, Labs, and Assessments

This document lists Level 1 unit content files, lab content files, and assessment references so implementers can sync with Codio and keep content in one place.

**Codio guide (Level 1)** no longer includes guide pages for Unit **0.3**; Unit **1.3**, **1.4**; **Lab 2.1**; Unit **6.4** (Understanding Agent Behavior); Unit **8.2**, **8.4**, **8.5**. The rows for those topics were removed from the table below (except **0.4** is in the Codio TOC again). Mirror markdown files for some omitted topics may still exist under `level1/` for offline reference (see `.guides/JSON_COHERENCE_REPORT.md` §8).

---

## 1. Course structure

Level 1 uses **9 units** (0–8): Setup → Domain → Flows → Patterns → Config → Training → Walkthrough → Assessment.

- **Unit content** is in separate files (below) for copy/paste into Codio where a matching guide page exists.

---

## 2. Unit content files (source of truth in level1/)

| File | Purpose |
|------|---------|
| `Level1_Unit0_Content_0.1_What-You-Need-Before-Starting.md` | Prerequisites, Rasa Pro license |
| `Level1_Unit0_Content_0.2_Project-Structure.md` | File structure, level1 folder |
| `Level1_Unit0_Content_0.4_Getting-Help.md` | Resources, troubleshooting (Codio page **0.4**) |
| `Level1_Unit1_Content_1.1_What-is-a-Conversational-Agent.md` | Agent intro, NLU |
| `Level1_Unit1_Content_1.2_The-Simplest-Agent-Possible.md` | Minimal agent concept |
| `Level1_Unit2_Content_2.1_What-is-a-Domain.md` | Domain, responses section |
| `Level1_Unit2_Content_2.2_Understanding-Responses.md` | Response structure, examples |
| `Level1_Unit2_Content_2.3_Response-Variations.md` | Multiple text variations |
| `Level1_Unit3_Content_3.1_What-is-a-Flow.md` | Flow concept |
| `Level1_Unit3_Content_3.2_Flow-Structure-Deep-Dive.md` | greet.yml structure |
| `Level1_Unit3_Content_3.3_Flow-Descriptions-and-LLM-Understanding.md` | Descriptions, LLM matching (Codio page **3.3**) |
| `Level1_Unit4_Content_4.1_What-are-System-Patterns.md` | Patterns intro |
| `Level1_Unit4_Content_4.2_Session-Start-Pattern.md` | pattern_session_start |
| `Level1_Unit4_Content_4.3_Pattern-Completed.md` | pattern_completed |
| `Level1_Unit4_Content_4.4_Modifying-System-Patterns.md` | Customization |
| `Level1_Unit5_Content_5.1_The-config-yml-File.md` | config.yml |
| `Level1_Unit5_Content_5.2_credentials-yml.md` | credentials.yml |
| `Level1_Unit5_Content_5.3_endpoints-yml.md` | endpoints.yml |
| `Level1_Unit6_Content_6.1_What-is-Training.md` | Training concept, `python -m rasa train`, success criteria (merged former 6.1 + 6.2) |
| `Level1_Unit6_Content_6.2_Using-Rasa-Inspector.md` | Inspector |
| `Level1_Unit6_Content_6.4_Testing-Your-Agent.md` | Testing (Codio reading **6.2** Testing Your Agent) |
| `Level1_Unit7_Content_7.1_Complete-Agent-Walkthrough.md` | Walkthrough |
| `Level1_Unit7_Content_7.2_Your-Level-1-Banking-Agent-Summary.md` | Summary |
| `Level1_Unit8_Content_8.1_Knowledge-Check.md` | Knowledge check |
| `Level1_Unit8_Content_8.3_Limitations-of-Level-1.md` | Limitations |

---

## 3. Lab content and assessment files

| Lab | Content File | Assessment Setup File | Notes |
|-----|--------------|----------------------|--------|
| 0.1 | Level1_Lab0.1_Content.md | Level1_Lab0.1_Assessment_Setup.md | Venv, Rasa Pro, RASA_LICENSE |
| 2.2 | Level1_Lab2.2_Content.md | — | Add utter_goodbye response |
| 2.3 | Level1_Lab2.3_Content.md | — | Add response variations |
| 3.1 | Level1_Lab3.1_Content.md | — | Explore flows |
| 3.2 | Level1_Lab3.2_Content.md | — | Create goodbye.yml flow |
| 3.3 | Level1_Lab3.3_Content.md | — | Multi-step flow |
| 3.4 | Level1_Lab3.4_Content.md | — | Hours and balance flow YAML (fill-in-the-blank; assessments embedded in Codio guide) |
| 3.5 | Level1_Lab3.5_Content.md | Level1_Lab3.5_Assessment_Setup.md | Add hours/balance responses and flows to `level1`; Check It! in guide Lab 3.5 |
| 4.1 | Level1_Lab4.1_Content.md | — | Explore system patterns |
| 4.2 | Level1_Lab4.2_Content.md | — | Modify patterns |
| 5.1 | Level1_Lab5.1_Content.md | — | Config |
| 6.1 | Level1_Lab6.1_Content.md | Level1_Lab6.1_Assessment_Setup.md | `rasa train` from `level1`; Codio primary path; optional “Not using Codio?” local training section mirrors guide |
| 6.2 | Level1_Lab6.2_Content.md | — | Inspector; Codio **Rasa Inspect** tab; optional local **localhost** section mirrors guide |
| 6.3 | Level1_Lab6.3_Content.md | — | Test-flow checklist (pairs with reading **6.2 Testing Your Agent**) |
| 7.1 | Level1_Lab7.1_Content.md | — | Walkthrough |
| 7.2 | Level1_Lab7.2_Content.md | Level1_Lab7.2_Assessment_Setup.md | Build your own feature |

**Task IDs / Graders:** Level 1 assessments (e.g. Check It! code-output-compare) are configured in the Codio guide (Level 1). See `.guides/content/` and assessment JSONs for task IDs and grader paths.

---

## 4. Summary

| Item | Location |
|------|----------|
| Narrative | level1/Level1_Unit*_Content_*.md (unit content files) |
| Units | 0–8 (Modules 0–8) |
| Content files | level1/Level1_Unit*_Content_*.md |
| Labs | level1/Level1_Lab*_Content.md, Level1_Lab*_Assessment_Setup.md |

For Codio guide structure and Check It! placement, see the Level 1 chapter in `.guides/content/`.
