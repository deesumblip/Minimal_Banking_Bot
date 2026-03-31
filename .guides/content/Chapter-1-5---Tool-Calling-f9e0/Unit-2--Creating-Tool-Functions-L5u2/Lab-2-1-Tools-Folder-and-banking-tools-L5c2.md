**Starting point:** Work in **`level5/`** with **Lab 2.0** complete (command-generator prompt in **`data/prompts/`** and **`config.yml`**). See **Unit 0.1** for the Chapter 1.4 baseline if needed.

You finish **`banking_tools.py`** in the fill-in-the-blanks exercise. Then you create **`level5/tools/`** and save the completed module as **`level5/tools/banking_tools.py`**.

The module must define **`check_balance`**, **`process_transfer`**, and **`get_account_info`**, list them in **`__all__`**, and match **Unit 2.1** (type hints, docstrings, return dicts).

You do **not** need the virtual environment for this lab; **Check It!** reads your saved files only.

---

#### Complete the `banking_tools` module (fill in the blanks)

The exercise matches **Unit 2.1**: **`str`** hints on **`account`**, docstrings that say **when** to call each tool, and **return dict keys** like the **`check_balance`** example on the previous page. The **`__all__`** line is **printed in full** (no blanks).

There are **twelve blanks** in total:

- **`str`** type hints: twice (**`check_balance`** and **`get_account_info`**)
- The **three** function docstrings
- First **`return`** dict: keys **`balance`**, **`currency`**, **`status`**
- Second **`return`** dict: keys **`success`**, **`message`**, **`account_type`**, **`status`**

Demo values in the return dicts stay visible. Fill every blank, **paste the full script** into **`level5/tools/banking_tools.py`**, then run the **Code Test**.

{Check It!|assessment}(fill-in-the-blanks-501020010)

---

### After you complete the blanks

1. In **`level5/`**, create a directory named **`tools`** (if it does not exist).
2. Create **`level5/tools/__init__.py`** (can be empty or a short comment that this is the tools module).
3. **Open** **`level5/tools/banking_tools.py`** in the file tree (create the file if needed).
4. **Paste** your completed script from the exercise above so the file matches your answers (all blanks filled).
5. **Save** the file.

---

### Run the code assessment

The grader checks that **`level5/tools/`** exists, **`banking_tools.py`** is present, **`check_balance`**, **`process_transfer`**, and **`get_account_info`** appear in the file, and **`__all__`** is defined.

{Check It!|assessment}(code-output-compare-501020001)

---

**Success criteria.** Code test passes (**10/10**). Then continue to **Lab 3.1** (register **`tools:`** in **`endpoints.yml`**). (If you skipped **Lab 2.0**, go back and add the **prompt template** first—**Lab 3.1** assumes **Lab 2.0** and **Lab 2.1** are done.)

---

## Running locally

1. Open the project and **`cd level5`**.
2. Complete the **fill-in-the-blanks** exercise, then create **`tools/`**, **`tools/__init__.py`**, and **`tools/banking_tools.py`** with the completed script.
3. Run the **Code Test** when your files match the exercise.
