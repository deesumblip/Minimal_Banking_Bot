# Level 3 Development Plan: Same Treatment as L1/L2, Minimal Dev Time

**Goal:** Give Level 3 the same structure and conventions as Level 1 and Level 2, reusing what we’ve learned to keep development time down.

**Current state:** Level 3 has bot code (`level3/`), a long combined tutorial+implementation doc (`CODIO_IMPLEMENTATION_GUIDE.md`), and a short `README.md`. It does **not** yet have: per-unit/content per-lab markdown in `level3/`, assessment setup docs, grader scripts, or a Codio `.guides` chapter.

---

## Conventions to Reuse (from L1/L2)

| Convention | Apply to Level 3 |
|------------|------------------|
| **Single .venv in project root** | No venv inside `level3/`. Students activate from root (`source .venv/bin/activate`), then `cd level3`. |
| **Codio vs local split** | Every lab: Part 1 (In Codio) then Part 2 (Running locally), with local steps by OS (Windows PowerShell, CMD, macOS/Linux). |
| **Inspector on Codio** | Use **Rasa Inspect** tab only; no “Tools → Ports” or “port 5005”. |
| **Assessment pattern** | Grader in `.guides/secure/level3_graders/`, prints `PASS` / `Successfully passed!`, exit 0 on full score. Codio: Working Directory = workspace root; script activates venv then `cd level3`. |
| **Content file naming** | `Level3_UnitN_Content_*.md`, `Level3_LabX.Y_Content.md`, `Level3_LabX.Y_Assessment_Setup.md`. |
| **One source of truth** | Student-facing content lives in `level3/*.md`; Codio `.guides` content is copied from there (or linked) so we don’t maintain two versions. |

---

## Phased Approach (Cut Down Dev Time)

### Phase 1: Foundation (minimal new writing)

1. **Level 3 course outline**  
   - Create `level3/Level3_Course_Outline.md` using **Level 2’s outline as a template**.  
   - Map Level 3 to units from the existing `CODIO_IMPLEMENTATION_GUIDE.md` (Module 0 → Unit 0, Module 1 → Unit 1, etc.).  
   - List which units are content-only and which labs have assessments.  
   - **Source:** Table of contents and module list in `level3/CODIO_IMPLEMENTATION_GUIDE.md` + `Course_Topics_By_Level.md` (Level 3 row).

2. **Level 3 implementation overview**  
   - Create `level3/Level3_Implementation_Overview.md` (short).  
   - Include: venv in root then `cd level3`, Codio vs local, where assessments live, that Inspector is via Rasa Inspect tab.  
   - **Template:** Copy from `level1/Level1_Implementation_Overview.md` or `level2/Level2_Implementation_Overview.md` and replace level → level3, ports/Inspector note.

3. **Update `level3/README.md`**  
   - **Quick Start:** Assume one venv in project root. Steps: from root, `source .venv/bin/activate`, then `cd level3`; then `python -m rasa train`, `python -m rasa inspect --debug`.  
   - **Codio:** “Open the **Rasa Inspect** tab” (no Ports).  
   - **Local:** One short subsection with PowerShell / CMD / macOS-Linux variants.  
   - Removes the need for a separate “create venv in level3” flow.

**Outcome:** Clear map of Level 3 (outline + overview) and a single, correct setup story (venv root + Inspector) in the repo.

---

### Phase 2: Extract and Split Content (reuse existing text)

4. **Unit and lab content files**  
   - **Don’t rewrite.** Treat `level3/CODIO_IMPLEMENTATION_GUIDE.md` as the source.  
   - Create one file per unit/lab, e.g.  
     - `Level3_Unit0_Content_0.1_Your-Level-2-Bot.md`, `Level3_Unit0_Content_0.2_What-Level-3-Adds.md`  
     - `Level3_Unit1_Content_1.1_What-is-a-Slot.md`, …  
     - `Level3_Lab3.1_Content.md`, `Level3_Lab6.1_Content.md`, etc.  
   - **Copy-paste** from the relevant sections of `CODIO_IMPLEMENTATION_GUIDE.md`, then:  
     - Add **Part 1 (Codio)** / **Part 2 (Running locally)** for any step that involves terminal or Inspector.  
     - Replace “port 5005” / “Ports” with “Rasa Inspect tab” where applicable.  
     - Ensure every terminal sequence is: **activate venv from root → `cd level3` → command.**  
   - Use **Level 2’s** `Level2_Unit*_Content*.md` and `Level2_Lab*_Content.md` as layout/styling templates (headings, code blocks, bullets).

5. **Lab assessment setup docs**  
   - For each lab that will have an assessment (e.g. “define slot + flow”, “train”, “run Inspector”): add `Level3_LabX.Y_Assessment_Setup.md`.  
   - **Template:** Copy `level2/Level2_Lab6.1_Assessment_Setup.md` (or L1 Lab 6.1). Replace: level2 → level3, paths, and what the grader checks (e.g. slot in domain, flow with `collect:`, model file, no critical errors).  
   - In each setup doc: Working Directory = workspace root; grader activates venv then `cd level3`; expected output = `PASS` or `Successfully passed!`.

**Outcome:** All student-facing narrative lives in `level3/Level3_*` and `level3/Level3_Lab*` files; no new long-form writing, only restructure + convention fixes.

---

### Phase 3: Assessments and Graders

6. **Decide which labs are graded**  
   - Suggested minimum: one “setup/train” style lab (e.g. Lab 6.1: train Level 3 bot) and optionally one “slot/flow” lab (e.g. add slot + collect flow).  
   - List them in `Level3_Course_Outline.md` and in `Level3_Implementation_Overview.md`.

7. **Grader scripts**  
   - Add `.guides/secure/level3_graders/` (e.g. `lab_6.1_grader.sh`).  
   - **Reuse L1/L2 logic:** run from workspace root, check/activate `.venv`, `cd level3`, then check model file / optional log / optional slot or flow.  
   - Script must print a line containing `PASS` or `Successfully passed!` on full score and `exit 0`; on failure print `FAIL` and `exit 1`.  
   - **Template:** Copy `level1` or `level2` Lab 6.1 grader and change paths to `level3`, adjust checks (e.g. `level3/models/*.tar.gz`, `level3/domain/basics.yml` for slot if needed).

8. **Codio assessment configuration**  
   - Document in the relevant `Level3_Lab*_Assessment_Setup.md`: COMMAND, Working Directory = `/home/codio/workspace`, expected output, points.  
   - So implementers can follow the same pattern as L1/L2 without re-deciding.

**Outcome:** Level 3 has the same assessment pattern as L1/L2 (root venv, clear pass/fail, Codio-friendly).

---

### Phase 4: Codio .guides (optional / last)

9. **Add a Level 3 chapter under `.guides/content`**  
   - e.g. `Chapter-1-3---Slot-Collection-xxxx` (or similar naming used for L1/L2).  
   - Add `Unit-*` and lab pages; **paste** from `level3/Level3_Unit*_Content*.md` and `level3/Level3_Lab*_Content.md` so the single source of truth remains in `level3/`.  
   - Add `index.json` and any page `.json` files so the guide tree matches the outline.

10. **Codio implementation guide for Level 3**  
    - **Done.** Shortened `level3/CODIO_IMPLEMENTATION_GUIDE.md` to implementer-only; references `Level3_*` content and assessment setup docs.  
    - **Done.** Added Level 3 section to `.guides/CODIO_IMPLEMENTATION_OVERVIEW.md` (shared entry point for L1/L2/L3).

**Outcome:** Codio has a Level 3 guide that matches the repo and uses the same conventions as L1/L2.

---

## Checklist (Quick Reference)

- [x] **Level3_Course_Outline.md** – Units and labs listed; assessments marked.  
- [x] **Level3_Implementation_Overview.md** – Venv root, Codio vs local, Inspector tab, assessment locations.  
- [x] **level3/README.md** – Quick Start uses venv from root, `cd level3`, Rasa Inspect tab only.  
- [x] **Level3_Unit*_Content*.md** – Units 0–8; Codio/local and venv order fixed; 7.3 Best Practices, 8.1 Knowledge Check added.  
- [x] **Level3_Lab*_Content.md** – Labs 3.1, 4.1, 5.1, 6.1, 6.2, 7.1; Part 1 (Codio) / Part 2 (local); no Ports.  
- [x] **Level3_Lab*_Assessment_Setup.md** – All six labs; graded labs have LLM Rubric (3.1, 4.1) or Python grader (6.1); ungraded (5.1, 6.2, 7.1) documented.  
- [ ] **.guides/secure/level3_graders/** – Lab 6.1: `lab_6.1_grader.py` done. Lab 3.1/5.1: solution references done; **optional** `lab_3.1_grader.sh`, `lab_5.1_grader.sh` if offering Option B (Bash).  
- [x] **.guides/content** – Level 3 chapter (Chapter-1-3---Slot-Collection-a4b5) added; Units 0–8 with content and labs pasted from level3.
- [x] **level3/CODIO_IMPLEMENTATION_GUIDE.md** – Shortened to implementer-only; **.guides/CODIO_IMPLEMENTATION_OVERVIEW.md** – Level 3 section added (shared L1/L2/L3 entry point).

---

## What's Left to Do

| Phase | Item | Status |
|-------|------|--------|
| **Phase 3** | Bash graders for Lab 3.1 and 5.1 (Option B) | Optional: create `lab_3.1_grader.sh`, `lab_5.1_grader.sh` if implementers want Standard Code Test instead of LLM Rubric. |
| **Phase 4** | Level 3 chapter in `.guides/content` | **Done.** Chapter-1-3---Slot-Collection-a4b5 with Units 0–8, all content/lab pages pasted from level3. |
| **Phase 4** | Codio implementation guide | **Done.** `CODIO_IMPLEMENTATION_GUIDE.md` shortened to implementer-only; Level 3 added to `.guides/CODIO_IMPLEMENTATION_OVERVIEW.md`. |

---

## What to Do First

1. **Phase 1** (outline, implementation overview, README) – gives you a clear target and one consistent setup story.  
2. **Phase 2** (extract unit/lab content + assessment setup docs) – reuses the existing long guide and applies L1/L2 conventions.  
3. **Phase 3** (graders + Codio config) – makes Level 3 assessable the same way as L1/L2.  
4. **Phase 4** (Codio .guides chapter) – do when you’re ready to publish Level 3 on Codio; can be skipped if you only need repo content and assessments for now.

If you want, next step can be: drafting **Level3_Course_Outline.md** and **Level3_Implementation_Overview.md** (and the README changes) so Phase 1 is done in one go.
