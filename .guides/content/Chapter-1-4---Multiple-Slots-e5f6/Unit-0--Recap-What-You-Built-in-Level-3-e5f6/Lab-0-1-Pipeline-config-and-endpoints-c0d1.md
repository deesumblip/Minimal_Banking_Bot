**Starting point:** You have the **Chapter 1.3–complete** agent in **`level3/`** (see **Unit 0.1**). Chapter 1.4 work lives under **`level4/`**—usually a **copy** of that tree. Before you add transfer slots in **Lab 2.1**, you must align the **pipeline** files so CALM can fill free-text slots reliably (**Unit 0.2**, section 2).

**Repository note:** In the course repo, **`level4/`** may ship with Chapter 1.3–style pipeline files until you replace them. You still **complete this lab**: use the fill-in-the-blanks exercise, then paste your completed YAML into **`level4/config.yml`** and **`level4/endpoints.yml`** (same pattern as Chapter 1.3 **Lab 3.1**: blanks → paste → code test).

**Objective.** Build **`level4/config.yml`** and **`level4/endpoints.yml`** yourself using the blanks exercise, then verify with **Check It!**

You do **not** need to activate the virtual environment for the fill-in or code test (the grader only reads your saved files).

---

#### Part 1 — Fill in the blanks

The exercise has **Part A** (`config.yml`) and **Part B** (`endpoints.yml`). It matches **Unit 0.2** and (for extra depth) **`level4/PIPELINE_CHAPTER_1_3_AND_4.md`** *—repository Markdown; not a guide page*.

{Check It!|assessment}(fill-in-the-blanks-401010010)

---

#### Part 2 — Paste into `level4/`

1. Open **`level4/config.yml`** in the editor (or create it if you are working from a fresh **`level3/`** copy).
2. **Replace** the file contents with **Part A** from your completed exercise (full YAML from the exercise, with every blank filled).
3. Open **`level4/endpoints.yml`**.
4. **Replace** the file contents with **Part B** from your completed exercise.
5. **Save** both files.

---

#### Part 3 — Code test

{Check It!|assessment}(code-output-compare-401010001)

---

**Success criteria.** Code test **10/10**. Then continue to **Lab 2.1** (domain).

**Next:** **Lab 2.1** — add transfer slots and ask responses in **`level4/domain/basics.yml`**.
