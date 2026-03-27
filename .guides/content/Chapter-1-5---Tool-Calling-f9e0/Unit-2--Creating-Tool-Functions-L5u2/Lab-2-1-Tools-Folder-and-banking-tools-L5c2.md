**Starting point:** Work in **`level5/`** with the Chapter 1.4 completion baseline from the start of this chapter.

**Objective.** The **previous page** showed a complete **`check_balance`** example. In this lab you complete a **fill-in-the-blanks** version of **`banking_tools.py`**, then **create** **`level5/tools/`** and save the **finished script** as **`level5/tools/banking_tools.py`**. The module must define **`check_balance`**, **`process_transfer`**, and **`get_account_info`**, export them in **`__all__`**, and return **dicts** with type hints and docstrings.

You do **not** need to activate the virtual environment for the fill-in exercise or the code test (the grader only reads your saved files).

---

#### Part 1 — Fill in the blanks

Complete the **`banking_tools.py`** script below. **Part A** matches **Unit 2.1** (three tools, **`__all__`**, demo return dicts). Distractors include similar-but-wrong names and values—pick the choice that matches the **`def`** lines and the patterns you learned.

{Check It!|assessment}(fill-in-the-blanks-501020010)

---

#### Part 2 — Create files in **`level5/`**

1. In **`level5/`**, create a directory named **`tools`** (if it does not exist).
2. Create **`level5/tools/__init__.py`** (can be empty or a short comment that this is the tools module).
3. Open **`level5/tools/banking_tools.py`** (create the file if needed).
4. **Paste** the **full** Python module from **Part 1** with **every blank filled**—the file on disk must match your completed exercise (same function names, **`__all__`**, docstrings, and return dicts).
5. **Save** the file.

---

#### Part 3 — Code test

{Check It!|assessment}(code-output-compare-501020001)

---

**Success criteria.** Code test passes (**10/10**). Then continue to **Lab 3.1** (register **`tools:`** in **`endpoints.yml`**).

---

## Running locally

1. Open the project and **`cd level5`**.
2. Complete **Part 1** in the fill-in-the-blanks exercise, then create **`tools/`**, **`tools/__init__.py`**, and **`tools/banking_tools.py`** with the completed script (same as **Part 2**).
3. Run the **Code Test** when your files match the exercise.
