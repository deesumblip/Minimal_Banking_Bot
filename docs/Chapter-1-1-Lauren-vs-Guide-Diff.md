# Chapter 1.1 — Lauren markdown vs student guide (diff & merge notes)

This document compares **`Lauren_Markdown_Edits/Chapter_1.1_Markdowns/`** to the latest student-facing guide **`.guides/content/Chapter-1-1---Just-Responses-d3b4/`**. The mirror branch **`origin/lauren-markdown-edits-only`** matches the Lauren folder in this repo; the **guide** evolves separately (assessments, Codio wording, lab renumbering, LLM IDs).

## Page titles (Codio)

**Page titles** below match the student-facing **`title`** in each page’s **`.json`** file beside the markdown (e.g. `0-3-Getting-Help-8218.json` → `"0.3 Getting Help"`). The chapter root title is **`Chapter 1.1 - Just Responses`** (see `.guides/content/Chapter-1-1---Just-Responses-d3b4/index.json`).

**Regenerate full diffs** (PowerShell, from repo root):

```powershell
git diff --no-index `
  "Lauren_Markdown_Edits/Chapter_1.1_Markdowns/<path>" `
  ".guides/content/Chapter-1-1---Just-Responses-d3b4/<path>"
```

Use the **guide** path (right-hand file) as the canonical page in Codio.

---

## Filename mapping (Lauren → guide)

Some stems differ only by numbering or article (“the” vs “a”). The **guide title** is what students see in the TOC.

| Guide page title (Codio) | Lauren file | Guide file |
|--------------------------|-------------|------------|
| **0.3 Getting Help** | `0-4-Getting-Help-8218.md` | `0-3-Getting-Help-8218.md` |
| **2.1 What is a Domain?** | `2-1-What-is-the-Domain--1094.md` | `2-1-What-is-a-Domain--1094.md` |
| **Lab 2.1: Creating Your First Response** | `Lab-2-2--Creating-Your-First-Response-a598.md` | `Lab-2-1--...a598.md` |
| **Lab 2.2: Add Response Variations** | `Lab-2-3--Add-Response-Variations-a630.md` | `Lab-2-2--...a630.md` |
| **3.4 Flow Descriptions and LLM Understanding** | `3-3-Flow-Descriptions-and-LLM-Understanding-f72a.md` | `3-4-...f72a.md` |
| **3.7 Test Your Knowledge** | `3-6--Test-Your-Knowledge-26ac.md` | `3-7--Test-Your-Knowledge-26ac.md` |
| **Lab 3.5: Flow Descriptions and LLM Matching** | `Lab-3-4--Flow-Descriptions-and-LLM-Matching-5cc1.md` | `Lab-3-5--...5cc1.md` |
| **Lab 3.6: Complete Your Agent for Training** | `Lab-3-5--Complete-Your-Agent-for-Training-c4f0.md` | `Lab-3-6--...c4f0.md` |
| **8.2 Limitations of Level 1** | `8-3-Limitations-of-Level-1-f9a1.md` | `8-2-Limitations-of-Level-1-f9a1.md` |
| **Lab 7.4: Build Your Own Feature** | `Lab-7-1-Build-Your-Own-Feature-b5c6.md` | `Lab-7-4-Build-Your-Own-Feature-b5c6.md` |

**Guide-only / restructure:** the standalone **`6.2`** reading page was merged into **`6.1 Training: What It Does and How to Run It`**; Lauren still has **`6-2-How-to-Train-Your-Agent-b2c3.md`** (short lab pointer only).

**Lauren-only (not a normal student TOC page):** `Unit-6--.../CODIO_AUTO_START_INSPECTOR.md` (instructor Codio layout notes for auto-starting Inspector).

---

## Diff size snapshot (`git diff --no-index --numstat`)

Approximate line churn (numstat: first column ≈ lines only in Lauren, second ≈ lines only in guide). **IDENTICAL** = same text for that file pair.

| Guide page title | Lauren vs guide |
|------------------|-----------------|
| **0.1 What You Need Before Starting** | IDENTICAL (guide aligned with Lauren’s prerequisite copy) |
| **0.2 Project Structure** | Large (guide: starter layout, fixed tree, `logs/`, Lauren intro on sub-agents/tools, Codio `.env` note) |
| **0.3 Getting Help** | Small after merge (guide adds docs “Ask AI” + Discord like Lauren; **AI Coach** omitted by policy) |
| **Lab 0.1: Create Virtual Environment and Install Rasa Pro** | Small (Rasa Pro wording, **Check It!**, fenced code blocks with a `text` label, punctuation) |
| **1.1 What is a Conversational Agent?** | Large (Lauren: long essay; guide: short structured bullets, CALM) |
| **1.2 Level 1: The Simplest Agent Possible** | Medium (different structure, analogies, bullet layout) |
| **2.1 What is a Domain?** | Trivial (Lauren filename “the Domain”; guide may add leading blank line) |
| **2.2 Understanding Responses** | Medium (Lauren: narrative “contract” style; guide: numbered “Breaking it down”) |
| **Lab 2.1: Creating Your First Response** | Large (guide: `level1/domain/basics.yml`, common mistakes, **Check It!**) |
| **Lab 2.2: Add Response Variations** | Small (prerequisite lab numbers; Lauren longer “what this means”) |
| **3.1 What is a Flow?** | Small (Lauren: autonomy paragraph; “activated” vs “triggered”) |
| **3.2 Flow Structure Deep Dive** | Small (Lauren typo `doesgggh`; guide fixes; activate/trigger wording) |
| **3.4 Flow Descriptions and LLM Understanding** | Trivial (cross-refs to Lab 3.5/3.6 vs Lauren 3.4/3.5) |
| **3.7 Test Your Knowledge** | IDENTICAL |
| **Lab 3.1: Exploring Existing Flows** | IDENTICAL |
| **Lab 3.2** – **Lab 3.6** | Small (lab number cross-refs; **Check It!** phrasing) |
| **4.1** – **4.4**, **4.5 Test Your Knowledge**, **Lab 4.1** | IDENTICAL |
| **4.2 Session Start Pattern** | Trivial (code fence `text`) |
| **Lab 4.2: Modifying System Patterns** | Trivial (blank line before yaml) |
| **5.1 The config.yml File** / **5.3 The endpoints.yml File** | Small (Lauren: `gpt-4o-mini`; guide: `openai-gpt-5-1`) |
| **5.2 The credentials.yml File** / **Lab 5.1 Exploring the Configuration Files** | IDENTICAL |
| **6.1 Training: What It Does and How to Run It** | Medium (guide adds when to train, Lab 6.1 preview, `python -m rasa train` block) |
| **Lauren-only `6-2` vs same guide 6.1** | Large (Lauren 6-2 is only “run training in lab”; guide 6-1 is full concept + lab) |
| **Lab 6.1: Training Your Agent** | Large (guide: long Codio-first steps, troubleshooting table; Lauren: Part 1 Codio / Part 2 local) |
| **Lab 6.2: Using Rasa Inspector** | Large (Lauren: full **local** Inspector + AI Coach; guide: Codio **Rasa Inspect** tab, drops local) |
| **6.3 Testing Your Agent** | Tiny (Lauren: AI Coach prompt) |
| **7.1 Complete Agent Walkthrough** | Tiny (Lauren: AI Coach prompt) |
| **7.2 Your Level 1 Banking Agent: Summary** / **8.1 Knowledge Check** / **8.2 Limitations of Level 1** | IDENTICAL |
| **Lab 7.4: Build Your Own Feature** | Trivial (“Run the assessment” vs “Use **Check It!**”) |

---

## Lauren’s edits in detail (by guide page title)

Recommendations assume keeping the guide’s lab numbering, assessments, **`openai-gpt-5-1`** in snippets, and Codio-first flow unless policy changes.

### Unit 0: Prerequisites and Setup

| Guide page title | What Lauren wrote (vs guide) | Merge to guide? |
|------------------|------------------------------|-----------------|
| **0.1 What You Need Before Starting** | Bullet prerequisites (timing 2–3h, Python/CLI/editing, Rasa license link). Guide had matched this intentionally; may later re-add Codio/local **RASA_LICENSE** callouts if desired. | **Done** (aligned). |
| **0.2 Project Structure** | Titled “Course File Tree” in Lauren; longer “how files work together” diagram including **sub-agent** branch; bold formatting quirks. Guide: “Complete File Tree,” corrected nesting, `logs/`, starter vs finished sentence, Lauren’s two intro sentences (beginning of course; sub-agents/tools later), non-agent files disclaimer. | **Partial** — guide is source of truth; optional phrasing only from Lauren beyond what’s merged. |
| **0.3 Getting Help** | Docs + **Ask AI**, **Discord** (Rasa University), error/common issues, **AI Coach**. Guide now includes Ask AI + Discord **without** AI Coach. | **Merged** (policy: no AI Coach). |
| **Lab 0.1: Create Virtual Environment and Install Rasa Pro** | Says “install Rasa” in places; “Run the assessment.” Guide: “Rasa Pro,” **Check It!**, explicit `level1` tree with a fenced `text` block. | **No** — keep guide terminology and Codio assessment wording. |

### Unit 1: Introduction to Rasa Agents

| Guide page title | What Lauren wrote (vs guide) | Merge to guide? |
|------------------|------------------------------|-----------------|
| **1.1 What is a Conversational Agent?** | Long editorial: names for chatbots, what makes agents good (NLU, memory, decisions), rule vs autonomous vs **hybrid**, **why Rasa**, bullet list of what you’ll build by end of course. Guide: short definition, key characteristics, types, Rasa Pro + CALM, analogy. | **Optional supplement** only (appendix / “Go deeper”), not a TOC replacement. |
| **1.2 Level 1: The Simplest Agent Possible** | Sections: what’s included / what’s coming in later levels / what Level 1 is good for; FAQ analogy. Guide: “absolute minimum,” explicit **does NOT include**, “Why start here” bullets, different analogy. | **Optional** — one short callout if you want Lauren’s “production use” framing. |

### Unit 2: Understanding the Domain File

| Guide page title | What Lauren wrote (vs guide) | Merge to guide? |
|------------------|------------------------------|-----------------|
| **2.1 What is a Domain?** | Filename “**the** Domain”; body essentially the same. | **No** — title wording only. |
| **2.2 Understanding Responses** | Conversational walkthrough of `utter_`, list items, `rephrase`; section heading “2.2 Understanding Responses.” Guide: tutorial-style numbered breakdown; fix grammar “an agent” if needed. | **No** — preference; keep guide structure. |
| **Lab 2.1: Creating Your First Response** | Shorter steps; no `level1/...` path; no “common mistakes”; assessment placement differs. Guide: explicit path, YAML checks, **Check It!** at end. | **No** — guide is stronger for learners. |
| **Lab 2.2: Add Response Variations** | Prerequisite “Lab 2.2” in Lauren’s numbering; longer closing on random selection + rephraser stack. Guide: prerequisite Lab 2.1; “How to verify” indentation bullets. | **Optional** — one sentence on variation + rephraser if the guide feels thin. |

### Unit 3: Understanding Flows

| Guide page title | What Lauren wrote (vs guide) | Merge to guide? |
|------------------|------------------------------|-----------------|
| **3.1 What is a Flow?** | Extra paragraph on guided flows vs LLM improvisation; “activated” wording. Guide: shorter “script” definition; “triggered.” | **Optional** — short callout on when flows are the right tool. |
| **3.2 Flow Structure Deep Dive** | Typo **doesgggh**; “outline of actions”; “activate your flow.” Guide: corrected text; “trigger.” | **No** — take guide. |
| **3.4 Flow Descriptions and LLM Understanding** | “Next: Lab 3.4 / 3.5” in Lauren numbering. Guide: Lab 3.5 / 3.6. | **No** — use guide numbers. |
| **3.7 Test Your Knowledge** | Same as guide. | **N/A** |
| **Lab 3.1** – **Lab 3.6** | Mostly lab index cross-refs (2.1 vs 2.2, 3.4 vs 3.5, etc.) and “Run assessment” vs **Check It!** on Lab 3.6. | **No** — guide numbering canonical. |

### Unit 4: System Patterns

| Guide page title | What Lauren wrote (vs guide) | Merge to guide? |
|------------------|------------------------------|-----------------|
| **4.1** – **4.4**, **4.5 Test Your Knowledge**, **Lab 4.1** | Same as guide. | **N/A** |
| **4.2 Session Start Pattern** | Plain ` ``` ` vs ` ```text` ` for diagram. | **No** (cosmetic). |
| **Lab 4.2: Modifying System Patterns** | Missing blank line before expected-result block. | **No** (cosmetic). |

### Unit 5: Configuration Files

| Guide page title | What Lauren wrote (vs guide) | Merge to guide? |
|------------------|------------------------------|-----------------|
| **5.1 The config.yml File** / **5.3 The endpoints.yml File** | Example and prose use **`model_group: gpt-4o-mini`** and matching `model_groups` / model id. Guide: **`openai-gpt-5-1`**. | **Do not merge** Lauren’s model IDs unless product reverts stack. |
| **5.2 The credentials.yml File** / **Lab 5.1 Exploring the Configuration Files** | Same as guide. | **N/A** |

### Unit 6: Training and Testing

| Guide page title | What Lauren wrote (vs guide) | Merge to guide? |
|------------------|------------------------------|-----------------|
| **6.1 Training: What It Does and How to Run It** | Shorter conceptual open; guide adds bridge to Lab 6.1, `rasa train` example, success line. Lauren’s separate **6-2** file is redundant with merged guide page. | **No** — guide supersedes. |
| **Lab 6.1: Training Your Agent** | Split **Part 1: Codio** / **Part 2: Running locally**; shorter troubleshooting. Guide: single long Codio-first flow, success checklist, error table, prerequisite Lab 3.6. | **Partial** — reintroduce **local training** subsection if non-Codio students are in scope. |
| **Lab 6.2: Using Rasa Inspector** | Codio + **long “Launching Inspector locally”** (Windows/macOS/Linux, localhost URLs, port troubleshooting); AI Coach. Guide: emphasize **Rasa Inspect** tab; dropped entire local section. | **Partial** — merge **local Inspector** steps for off-Codio learners; skip AI Coach if policy forbids. |
| **6.3 Testing Your Agent** | Extra **AI Coach** suggestion line. Guide: omitted. | **Conditional** on AI Coach policy. |
| **`CODIO_AUTO_START_INSPECTOR.md` (Lauren only)** | Step-by-step Codio Layout command to run `start_rasa_inspect.sh` when opening testing page. | **Instructor/author doc**, not a student page. |

### Unit 7–8

| Guide page title | What Lauren wrote (vs guide) | Merge to guide? |
|------------------|------------------------------|-----------------|
| **7.1 Complete Agent Walkthrough** | AI Coach line. | **Conditional** |
| **7.2 Your Level 1 Banking Agent: Summary** | Same as guide. | **N/A** |
| **Lab 7.4: Build Your Own Feature** | “Run the assessment” vs guide “Use **Check It!** (Codio).” | **No** — keep guide. |
| **8.1 Knowledge Check** / **8.2 Limitations of Level 1** | Same as guide. | **N/A** |

---

## Summary: highest-value merges (substantive)

1. **Lab 6.2: Using Rasa Inspector** — Restore **local** Inspector instructions from Lauren (subsection or linked doc).  
2. **Lab 6.1: Training Your Agent** — Restore **local / non-Codio** training steps if applicable.  
3. **0.3 Getting Help** — **Done** for Discord + Ask AI; AI Coach excluded.  
4. **3.1 What is a Flow?** — Optional callout on when flow-based design fits.  
5. **1.1** / **1.2** — Optional supplemental reading, not replacements.

**Do not merge:** Lauren’s **`gpt-4o-mini`** snippets; wholesale swap of **1.1** body; reverting **Lab 2.1** to shorter Lauren version; restoring **6-2** as its own student page.

---

## Related repo docs

- Starter vs finished Level 1 file layout: `level1/LEVEL1_STARTER_STATE.md`
